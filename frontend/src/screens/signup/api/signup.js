import axios from 'axios';

const signup = async (userDetails) => {
  const payload = {
    family_name: userDetails.familyName,
    parent: userDetails.isParent,
    users: {
      first_name: userDetails.firstName,
      last_name: userDetails.lastName,
      email: userDetails.email,
      date_of_birth: userDetails.dateOfBirth,
      password: userDetails.password
    }
  };
  return await axios.post('/api/swimmers/register/', payload);
};

export default signup;
