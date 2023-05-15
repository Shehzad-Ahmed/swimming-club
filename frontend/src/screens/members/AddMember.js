import { useNavigate } from 'react-router-dom';
import AddMemberForm from './AddMemberForm';
import SidbarNav from '../SidbarNav';

const AddMember = () => {
  const navigate = useNavigate();

  const onSuccessHandler = () => {
    navigate('/')
  };

  return <SidbarNav><AddMemberForm onSuccess={onSuccessHandler}></AddMemberForm></SidbarNav>
};

export default AddMember;
