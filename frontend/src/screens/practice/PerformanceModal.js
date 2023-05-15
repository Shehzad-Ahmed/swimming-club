import React from 'react';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Modal from 'react-bootstrap/Modal';
import Row from 'react-bootstrap/Row';
import { GetPerformance } from './api/performance';

function PerformanceModal(props) {
    
    const {sessionId} = props;
    const {loading, error, performance} = GetPerformance({sessionId});

  return (
    <Modal {...props} aria-labelledby="contained-modal-title-vcenter">
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Performance
        </Modal.Title>
      </Modal.Header>
      <Modal.Body className="show-grid">
      {(loading || error? '':
        <Container>
          <Row>
            <Col xs={8} md={6}>
              Repetitions
            </Col>
            <Col xs={8} md={6}>
              {performance[0].repetitions}
            </Col>
          </Row>          
            <Row>
                <Col xs={8} md={6}>
                Duration
                </Col>
                <Col xs={8} md={6}>
                {performance[0].duration}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Distance
                </Col>
                <Col xs={8} md={6}>
                {performance[0].distance}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Pace
                </Col>
                <Col xs={8} md={6}>
                {performance[0].pace}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Intensity
                </Col>
                <Col xs={8} md={6}>
                {performance[0].intensity}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Rest Frequency
                </Col>
                <Col xs={8} md={6}>
                {performance[0].restFrequence}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Rest Length Average 
                </Col>
                <Col xs={8} md={6}>
                {performance[0].restLengthAvg}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Heart Rate 
                </Col>
                <Col xs={8} md={6}>
                {performance[0].heartRate}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Technique 
                </Col>
                <Col xs={8} md={6}>
                {performance[0].technique}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Goal
                </Col>
                <Col xs={8} md={6}>
                {performance[0].goal}
                </Col>
            </Row>
            <Row>
                <Col xs={8} md={6}>
                Feedback
                </Col>
                <Col xs={8} md={6}>
                {performance[0].feedback}
                </Col>
            </Row>
        </Container>
          )}
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

export default PerformanceModal;