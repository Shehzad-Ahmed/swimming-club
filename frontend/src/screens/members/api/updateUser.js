import useAxios from "../../../utils/useAxios";

const UpdateUser = () => {
    const axios = useAxios();

    const updateUserAPI = async (userDetails) => {
        return await axios.patch(
            `api/core/users/${userDetails.id}/`, {
                  first_name: userDetails.firstName,
                  last_name: userDetails.lastName,
                  email: userDetails.email,
                  date_of_birth: userDetails.dateOfBirth,
              }
            )
    }

    return {updateUserAPI}
}


export default UpdateUser
