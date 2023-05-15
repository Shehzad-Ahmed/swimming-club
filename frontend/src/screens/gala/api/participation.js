import { useContext } from "react";
import useAxios from "../../../utils/useAxios";
import { Store } from "../../../store/StoreProvider";

const Participation = () => {
    const axios = useAxios();
    const {state} = useContext(Store);

    const participateAPI = async (eventId) => {
        return await axios.post("api/competitions/events/participation/", {event: eventId, participant: state?.userDetails?.user_id})
    }

    const withdrawAPI = async (participationId) => {
        return await axios.delete(`api/competitions/events/participation/${participationId}/`)
    }

    return {participateAPI, withdrawAPI}
}


export default Participation
