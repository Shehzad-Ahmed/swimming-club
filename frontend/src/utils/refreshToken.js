import axios from "axios";
import jwt_decode from 'jwt-decode';
import { Store } from '../store/StoreProvider';
import { useContext } from "react";

const RefreshToken = () => {

    const { state, dispatch: contextDispatch } = useContext(Store);

    const refresh = async () => {
    
    const response = await axios.post(`/api/token/refresh/`, {
        refresh: state.userDetails.authTokens.refresh,
      });
  
      const updatedUserDetails = jwt_decode(response.data.access);
      contextDispatch({
        type: 'USER_SIGN_IN',
        payload: { authTokens: response.data, ...updatedUserDetails },
      });
    return response  
    }

    return {refresh}

}

export default RefreshToken;
