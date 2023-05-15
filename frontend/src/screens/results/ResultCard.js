import { useState } from 'react';
import { Button, Card } from 'react-bootstrap';
import ScoreboardModal from './LeaderboardModal';

const ResultCard = (props) => {
    const { result } = props;
    const [modalShow, setModalShow] = useState(false);


    return (
        <div>
        <ScoreboardModal show={modalShow} onHide={() => setModalShow(false)} eventId={result.eventId}/>
        <Card>
          {/* <Link to={`/product/${product.id}`}>
            <img
              src={product.imageUrl}
              className="card-img-top"
              alt={product.name}
              style={{ height: '25vh' }}
            />
          </Link> */}
          <Card.Body>
            {/* <Link to={`/product/${product.id}`} className="nav-link"> */}
              <Card.Title>Position: {result.position}</Card.Title>
            {/* </Link> */}
            <Card.Text>
              Score: {result.score}
              <br />
              <div>
              Gala title: {result.galaTitle}
              </div>
              <div>
                Event type: {result.eventType}
              </div>
              <div>
                Event Date: {result.eventDate}
              </div>
            </Card.Text>
            {
             <Button  onClick={()=>{setModalShow(true)}}>Scoreboard</Button>
            }
          </Card.Body>
        </Card>
        </div>
      );
}

export default ResultCard;