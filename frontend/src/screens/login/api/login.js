import axios from 'axios';

const login = async (email, password) => {
  return await axios.post('/api/token/', {
    email: email,
    password: password,
  });
};

export default login;
