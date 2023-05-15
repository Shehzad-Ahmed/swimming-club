import { useEffect, useReducer } from "react";
import useAxios from "../../../utils/useAxios"
import apiCallReducer from "../../../utils/apiCallReducer";

const GetScoreboard = (queryParams=null) => {
    const [{ loading, error, data: scoreboard }, dispatch] = useReducer(
        apiCallReducer,
        {
          data: [],
          loading: true,
          error: '',
        }
      );

    const axios = useAxios();
    
    useEffect(()=> {

      dispatch( { type: 'FETCH_REQUEST' });
      const fetchScoreboard = async () => {
        try {
            const response = await axios.get(`/api/competitions/results/scoreboard/?participation__event=${queryParams?.eventId}`);
        
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
        name: `${data.participant.first_name} ${data.participant.last_name}`,
        score: data.score,
        ranking: data.position
      }
  }
    fetchScoreboard();  
    }, [])

    return {loading, error, scoreboard}

}

export {GetScoreboard};
