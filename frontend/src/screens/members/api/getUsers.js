import { useEffect, useReducer } from "react";
import useAxios from "../../../utils/useAxios"
import apiCallReducer from "../../../utils/apiCallReducer";

const GetUsers = (queryParams=null) => {
    const [{ loading, error, data: users }, dispatch] = useReducer(
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
      const getUsers = async () => {
        try {
            const response = await axios.get("/api/core/users/");
         
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
        firstName: data.first_name, 
        lastName: data.last_name,
        email: data.email,
        dateOfBirth: data.date_of_birth,
      }
  }
    getUsers();  
    }, [])

    return {loading, error, users}

}

export {GetUsers};
