import { useState } from 'react';
import { Button, Container, Form, InputGroup } from 'react-bootstrap';
import { toast } from 'react-toastify';
import signup from './api/signup';

const SignUpForm = (props) => {
  
  const { onSuccess } = props;
  const [fullName, setFullName] = useState(null);
  const [email, setEmail] = useState(null);
  const [familyName, setFamilyName] = useState(null);
  const [isParent, setIsParent] = useState(false);
  const [dateOfBirth, setDateOfBirth] = useState(null);
  const [password, setPassword] = useState(null);


  const onSignInSubmitHandler = async (event) => {
    event.preventDefault();
    event.stopPropagation();
    let [firstName, ...lastName] = fullName.split(" ")
    try {
      await signup({
        firstName: firstName,
        lastName: lastName? lastName.join(" "): "",
        familyName: familyName,
        email: email,
        isParent: isParent,
        dateOfBirth: dateOfBirth,
        password: password
      });
      toast.success("Registration successful, please sign in to continue")
      onSuccess();
    } catch (error) {
      toast.error(JSON.stringify(error.response.data));
    }
  };

  return (
    <Container className="main-container" style={{ maxWidth: '40rem' }}>
      <h1 className="my-3">Sign Up</h1>
      <Form onSubmit={onSignInSubmitHandler}>
      <Form.Group className="mb-3" controlId="fullName">
        <Form.Label>Full Name</Form.Label>
        <Form.Control
          onChange={(e) => setFullName(e.target.value)}
          type="text"
          required
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="family Name">
        <Form.Label>Family Name</Form.Label>
        <Form.Control
          onChange={(e) => setFamilyName(e.target.value)}
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
      <InputGroup className="mb-3">
      <InputGroup.Text>Sign up as Parent.</InputGroup.Text>
        <InputGroup.Checkbox aria-label="Sign up as Parent."
            onChange={(e) => setIsParent(e.target.value)}
        />
      </InputGroup>
        <div className="mb-3">
          <Button type="submit" disabled>Sign Up</Button>
        </div>
      </Form>
    </Container>
  );
};
export default SignUpForm;
