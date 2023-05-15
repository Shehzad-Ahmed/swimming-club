import {useState} from 'react';
import { Button, Container, Form, InputGroup } from 'react-bootstrap';
import { toast } from 'react-toastify';
import UpdateUser from './api/updateUser';

const UpdateMember = (props) => {

    const {user} = props;
    
    const [firstName, setFirstName] = useState(user.firstName);
    const [lastName, setLastName] = useState(user.lastName);
    const [email, setEmail] = useState(user.email);
    const {updateUserAPI} = UpdateUser();

    const onSaveHandler = async (event) => {
        event.preventDefault();
        event.stopPropagation();
        try{
            await updateUserAPI({id: user.id, firstName, lastName, email});
            toast.success("User changes updated.");
        } catch(error){
            toast.error(JSON.stringify(error.response.data));
        }
    }

    return (
        <Container className="main-container" style={{ maxWidth: '40rem' }}>
    <h1 className="my-3">Children details</h1>
    <Form onSubmit={onSaveHandler}>
    <InputGroup className="mb-3" controlId="firstName">
      <InputGroup.Text>First Name</InputGroup.Text>
      <Form.Control
        onChange={(e) => setFirstName(e.target.value)}
        type="text"
        value={firstName}
      />
    </InputGroup>
    <InputGroup className="mb-3" controlId="lastName">
      <InputGroup.Text>Last Name</InputGroup.Text>
      <Form.Control
        onChange={(e) => setLastName(e.target.value)}
        type="text"
        value={lastName}
      />
    </InputGroup>
    <InputGroup className="mb-3" controlId="familyName">
      <InputGroup.Text>Email</InputGroup.Text>
      <Form.Control
        onChange={(e) => setEmail(e.target.value)}
        type="email"
        value={email}
      />
    </InputGroup>
      <div className="mb-3">
        <Button type="submit">Save</Button>
      </div>
    </Form>
  </Container>)

}

export default UpdateMember;
