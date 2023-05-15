import { useEffect, useReducer } from "react";
import useAxios from "../../../utils/useAxios"
import apiCallReducer from "../../../utils/apiCallReducer";

const GetResults = (queryParams=null) => {
    const [{ loading, error, data: results }, dispatch] = useReducer(
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
      const fetchResults = async () => {
        try {
            const response = await axios.get("/api/competitions/results/");
         
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
        position: data.position,
        score: data.score,
        note: data.note,
        eventId: data.details.event.id,
        eventType: data.details.event.type,
        eventDate: data.details.event.start_on,
        galaTitle: data.details.event.gala.title,
      }
  }
    fetchResults();  
    }, [])

    return {loading, error, results}

}

export {GetResults};
