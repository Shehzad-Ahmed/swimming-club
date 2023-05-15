import useAxios from "../../../utils/useAxios";

const CreateMember = () => {
    const axios = useAxios();

    const createMemberAPI = async (userDetails) => {
        return await axios.post(
            "api/swimmers/families/add-member/", {
                  first_name: userDetails.firstName,
                  last_name: userDetails.lastName,
                  email: userDetails.email,
                  date_of_birth: userDetails.dateOfBirth,
                  password: userDetails.password
              }
            )
    }

    return {createMemberAPI}
}


export default CreateMember
