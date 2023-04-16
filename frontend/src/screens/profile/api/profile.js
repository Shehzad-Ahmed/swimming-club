import useAxios from "../../../utils/useAxios";


const UpdateProfile = () => {
    const axios = useAxios();

    const api = async (profileDetails) => await axios.patch(`/api/core/users/${profileDetails.userId}/`, transformPayload(profileDetails))
    return {api}

}

const transformPayload = (profileDetails) => {
    return {
        first_name: profileDetails.firstName,
        last_name: profileDetails.lastName,
        family_name: profileDetails.familyName
    }
}

export default UpdateProfile;