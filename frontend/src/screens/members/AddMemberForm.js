import { useState } from 'react';
import { Button, Container, Form, InputGroup } from 'react-bootstrap';
import { toast } from 'react-toastify';
import CreateMember from './api/createMember';

const AddMemberForm = (props) => {
  
  const { onSuccess } = props;
  const [fullName, setFullName] = useState(null);
  const [email, setEmail] = useState(null);
  const [dateOfBirth, setDateOfBirth] = useState(null);
  const [password, setPassword] = useState(null);
  const {createMemberAPI} = CreateMember();


  const onSignInSubmitHandler = async (event) => {
    event.preventDefault();
    event.stopPropagation();
    let [firstName, ...lastName] = fullName.split(" ")
    try {
      await createMemberAPI({
        firstName: firstName,
        lastName: lastName? lastName.join(" "): "",
        email: email,
        dateOfBirth: dateOfBirth,
        password: password
      });
      toast.success("Member added successfully.")
      onSuccess();
    } catch (error) {
      toast.error(JSON.stringify(error.response.data));
    }
  };

  return (
    <Container className="main-container" style={{ maxWidth: '40rem' }}>
      <h1 className="my-3">Add children details.</h1>
      <Form onSubmit={onSignInSubmitHandler}>
      <Form.Group className="mb-3" controlId="fullName">
        <Form.Label>Full Name</Form.Label>
        <Form.Control
          onChange={(e) => setFullName(e.target.value)}
          type="text"
          required
        />
      </Form.Group>
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            onChange={(e) => setEmail(e.target.value)}
            type="email"
            required
          />
        </Form.Group>
        <InputGroup className="mb-3" controlId="password">
          <InputGroup.Text>Password</InputGroup.Text>
          <Form.Control
            onChange={(e) => setPassword(e.target.value)}
            type="password"
            required
          />
        </InputGroup>
        <InputGroup className="mb-3" controlId="dateOfBirth">
          <InputGroup.Text>Date of Birth</InputGroup.Text>
          <Form.Control
            onChange={(e) => setDateOfBirth(e.target.value)}
            type="date"
            required
          />
        </InputGroup>
        <div className="mb-3">
          <Button type="submit">Create</Button>
        </div>
      </Form>
    </Container>
  );
};
export default AddMemberForm;
