import { useState } from 'react';
import { Button, Card } from 'react-bootstrap';
import PerformanceModal from './PerformanceModal';

const SessionDetails = (props) => {
    const { session } = props;
    const [modalShow, setModalShow] = useState(false);


    return (
        <div>
        <PerformanceModal show={modalShow} onHide={() => setModalShow(false)} sessionId={session.id}/>
        <Card>
          <Card.Body>
            {/* <Link to={`/product/${product.id}`} className="nav-link"> */}
              <Card.Title>Exercise Name: {session.exercise.name}</Card.Title>
            {/* </Link> */}
            <Card.Text>
              Start at: {session.startAt}
              <br />
              <div>
              Duration: {session.duration}
              </div>
              <div>
                Pool Code: {session.poolCode}
              </div>
              <div>
              </div>
            </Card.Text>
            {
             <Button disabled={!session.performanceUploaded} onClick={()=>{setModalShow(true)}}>Performance Metrices</Button>
            }
          </Card.Body>
        </Card>
        </div>
      );
}

export default SessionDetails;