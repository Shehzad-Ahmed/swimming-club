import { useEffect, useReducer } from "react";
import useAxios from "../../../utils/useAxios"
import apiCallReducer from "../../../utils/apiCallReducer";

const GetPerformance = (queryParams=null) => {
    const [{ loading, error, data: performance }, dispatch] = useReducer(
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
      const fetchPerformance = async () => {
        try {
            const response = await axios.get(`/api/training/performance/?session=${queryParams?.sessionId}`);
        
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
        repetitions: data.repetitions,
        duration: data.duration,
        distance: data.distance,
        pace: data.pace,
        intensity: data.intensity,
        restFrequency: data.rest_frequency,
        restLengthAvg: data.rest_length_avg,
        heartRate: data.heart_rate,
        technique: data.technique,
        goal: data.goal,
        feedback: data.feedback
      }
  }
    fetchPerformance();  
    }, [])

    return {loading, error, performance}

}

export {GetPerformance};
