import LoadingIndicator from "../LoadingIndicator";
import SidbarNav from "../SidbarNav";
import GalaEvent from "./GalaEvent";
import { GetEvents } from "./api/events";
import { Alert, Col, Container, Row } from 'react-bootstrap';


const GalaEvents = () => {
    
    const {loading, events, error} = GetEvents();


    return (
        <SidbarNav>
                <Container>
      {loading ? (
        <LoadingIndicator className="align-content-center" />
      ) : error ? (
        <Alert variant="danger">{error}</Alert>
      ) : events.length ? (
        <div>
          <h1>Gala Events</h1>
          <Row>
            {events.map((event) => (
              <Col key={event.id} sm={6} md={4} lg={3} className="mb-3">
                <GalaEvent event={event}></GalaEvent>
              </Col>
            ))}
          </Row>
        </div>
      ): <Alert style={{margin: "10px"}} variant="info">No events, stay tuned.</Alert>}
    </Container>
        </SidbarNav>
        )
}

export default GalaEvents;