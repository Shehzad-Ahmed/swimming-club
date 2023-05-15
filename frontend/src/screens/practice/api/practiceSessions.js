import { useEffect, useReducer } from "react";
import useAxios from "../../../utils/useAxios"
import apiCallReducer from "../../../utils/apiCallReducer";

const GetPracticeSessions = (queryParams=null) => {
    const [{ loading, error, data: sessions }, dispatch] = useReducer(
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
            const response = await axios.get("/api/training/practice-sessions/");
         
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
        startAt: data.start_at,
        duration: data.duration,
        squad: data.squad,
        poolCode: data.pool_code,
        performanceUploaded: data.performance_uploaded,
        exercise: {
            name: data.exercise.name,
        }
      }
  }
    fetchResults();  
    }, [])

    return {loading, error, sessions}

}

export {GetPracticeSessions};
