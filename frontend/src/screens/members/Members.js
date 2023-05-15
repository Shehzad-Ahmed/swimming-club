import { useNavigate } from 'react-router-dom';
import AddMemberForm from './AddMemberForm';
import SidbarNav from '../SidbarNav';
import { GetUsers } from './api/getUsers';
import UpdateMember from './UpdateMember';

const Members = () => {
  const navigate = useNavigate();
  const {loading, error, users} = GetUsers();

  const onSuccessHandler = () => {
    navigate('/')
  };

  return <SidbarNav><AddMemberForm onSuccess={onSuccessHandler}></AddMemberForm>
  {loading || error ? '': users.map((user) => {
    return <UpdateMember user={user}></UpdateMember>
  })}
  </SidbarNav>
};

export default Members;
