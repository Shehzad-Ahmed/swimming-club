import React from 'react';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Modal from 'react-bootstrap/Modal';
import Row from 'react-bootstrap/Row';
import { GetScoreboard } from './api/scoreboard';

function ScoreboardModal(props) {
    
    const {eventId} = props;
    const {loading, error, scoreboard} = GetScoreboard({eventId});

  return (
    <Modal {...props} aria-labelledby="contained-modal-title-vcenter">
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Scoreboard
        </Modal.Title>
      </Modal.Header>
      <Modal.Body className="show-grid">
        <Container>

          <Row>
            <Col xs={8} md={6}>
              Name
            </Col>
            <Col xs={4} md={3}>
              Score
            </Col>
            <Col xs={4} md={3}>
              Ranking
            </Col>
          </Row>
          {(loading || error? '':
          scoreboard.map((listing) => {

                      return <Row>
                      <Col xs={8} md={6}>
                        {listing.name}
                      </Col>
                      <Col xs={4} md={3}>
                        {listing.score}
                      </Col>
                      <Col xs={4} md={3}>
                        {listing.ranking}
                      </Col>
                    </Row>
          }))}
        </Container>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

// function App() {
//   const [modalShow, setModalShow] = useState(false);

//   return (
//     <>
//       <Button variant="primary" onClick={() => setModalShow(true)}>
//         Launch modal with grid
//       </Button>

//       <MydModalWithGrid show={modalShow} onHide={() => setModalShow(false)} />
//     </>
//   );
// }

export default ScoreboardModal;