import {useContext, useState} from 'react';
import { Store } from '../../store/StoreProvider';
import { Button, Container, Form, InputGroup } from 'react-bootstrap';
import Sidebar from '../Sidebar';
import UpdateProfile from './api/profile';
import { toast } from 'react-toastify';
import RefreshToken from '../../utils/refreshToken';

const Profile = () => {

    const  {state}  = useContext(Store);
    const userId = state?.userDetails?.user_id;
    const [firstName, setFirstName] = useState(state?.userDetails?.first_name);
    const [lastName, setLastName] = useState(state?.userDetails?.last_name);
    const [familyName, setFamilyName] = useState(state?.userDetails?.family);
    const isDisabled =  state?.userDetails?.role === "Young Swimmer";
    const {api} = UpdateProfile();
    const {refresh} = RefreshToken();

    const onSaveHandler = async (event) => {
        event.preventDefault();
        event.stopPropagation();
        try{
            await api({userId, firstName, lastName, familyName});
            await refresh();
            toast.success("Profile changes updated.");
        } catch(error){
            toast.error(JSON.stringify(error.response.data));
        }
    }

    return (<Sidebar>
        <Container className="main-container" style={{ maxWidth: '40rem' }}>
    <h1 className="my-3">Profile</h1>
    <Form onSubmit={onSaveHandler}>
    <InputGroup className="mb-3" controlId="firstName">
      <InputGroup.Text>First Name</InputGroup.Text>
      <Form.Control
        onChange={(e) => setFirstName(e.target.value)}
        type="text"
        disabled={isDisabled}
        value={firstName}
      />
    </InputGroup>
    <InputGroup className="mb-3" controlId="lastName">
      <InputGroup.Text>Last Name</InputGroup.Text>
      <Form.Control
        onChange={(e) => setLastName(e.target.value)}
        type="text"
        disabled={isDisabled}
        value={lastName}
      />
    </InputGroup>
    <InputGroup className="mb-3" controlId="familyName">
      <InputGroup.Text>Family Name</InputGroup.Text>
      <Form.Control
        onChange={(e) => setFamilyName(e.target.value)}
        type="text"
        disabled={isDisabled}
        value={familyName}
      />
    </InputGroup>
      <div className="mb-3">
        <Button type="submit" hidden={isDisabled}>Save</Button>
      </div>
    </Form>
  </Container></Sidebar>)

}

export default Profile;