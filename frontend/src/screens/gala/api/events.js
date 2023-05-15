import { useEffect, useReducer } from "react";
import useAxios from "../../../utils/useAxios"
import apiCallReducer from "../../../utils/apiCallReducer";

const GetEvents = (queryParams=null) => {
    const [{ loading, error, data: events }, dispatch] = useReducer(
        apiCallReducer,
        {
          data: [],
          loading: true,
          error: '',
        }
      );

    const axios = useAxios();
    
    useEffect(()=> {

      dispatch({ type: 'FETCH_REQUEST' });
      const fetchEvents = async () => {
        try {
            const response = await axios.get("/api/competitions/events/");
         
          dispatch({
            type: 'FETCH_SUCCESS',
            payload: response.data.map((data) => transformData(data)),
          });
        } catch (error) {
          dispatch({ type: 'FETCH_FAIL', error: error.message });
        }
    }

    const transformData = (data) => {
      // to do: transform response and return.
      return {
        id: data.id,
        type: data.type,
        startOn: data.start_on,
        duration: data.duration,
        skillLevel: data.skill_level,
        gala: {
          title: data.gala.title,
          about: data.gala.about,
          startOn: data.gala.start_on,
          endOn: data.gala.end_on,
        },
        participationId: data.participation_id,
      }
  }
    fetchEvents();  
    }, [])

    return {loading, error, events}

}

export {GetEvents};
