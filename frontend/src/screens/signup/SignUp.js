import { useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Store } from '../../store/StoreProvider';
import SignUpForm from './SignUpForm';

const SignUp = () => {
  const { state } = useContext(Store);
  const navigate = useNavigate();

  const onSuccessHandler = () => {
    navigate('/signin')
  };

  useEffect(() => {
    //if already logged in.
    if (state.userDetails) {
      navigate('/');
    }
  }, []);

  return <SignUpForm onSuccess={onSuccessHandler}></SignUpForm>
};

export default SignUp;
