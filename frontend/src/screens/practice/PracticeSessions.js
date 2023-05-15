import LoadingIndicator from "../LoadingIndicator";
import SidbarNav from "../SidbarNav";
import { Alert, Col, Container, Row } from 'react-bootstrap';
import { GetPracticeSessions } from "./api/practiceSessions";
import SessionDetails from "./SessionDetails";


const PracticeSessions = () => {
    
    const {loading, sessions, error} = GetPracticeSessions();


    return (
        <SidbarNav>
                <Container>
      {loading ? (
        <LoadingIndicator className="align-content-center" />
      ) : error ? (
        <Alert variant="danger">{error}</Alert>
      ) : sessions.length ? (
        <div>
          <h1>Practice Sessions</h1>
          <Row>
            {sessions.map((session) => (
              <Col key={session.id} sm={6} md={4} lg={3} className="mb-3">
                <SessionDetails session={session}></SessionDetails>
              </Col>
            ))}
          </Row>
        </div>
      ): <Alert style={{margin: "10px"}} variant="info">No upcoming practice sessions, stay tuned.</Alert>}
    </Container>
        </SidbarNav>
        )
}

export default PracticeSessions;