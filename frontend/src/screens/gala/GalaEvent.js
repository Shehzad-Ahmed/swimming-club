import React, { useState } from 'react';
import { Button, Card } from 'react-bootstrap';
import Participation from './api/participation';
// import { Link } from 'react-router-dom';
import { toast } from 'react-toastify';

export default function GalaEvent(props) {
  const { event } = props;
  const {participateAPI, withdrawAPI} = Participation();
  const [participationId, setParticipationId] = useState(event.participationId);

  const participateHandler = async () => {
    try{
        let response = await participateAPI(event.id)
        setParticipationId(response.data.id);
    }catch(error){
        toast.error(JSON.stringify(error.response.data));
    }
  }

  const withdrawHandler = async () => {
    try{
        await withdrawAPI(participationId)
        setParticipationId(null);
    }catch(error){
        toast.error(JSON.stringify(error.response.data));
    }
  }

  return (
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
          <Card.Title>{event.gala.name}</Card.Title>
        {/* </Link> */}
        <Card.Text>
          {event.type}
          <br />
          Start on: {event.startOn}
          <div>
          </div>
        </Card.Text>
        {
         participationId? <Button onClick={withdrawHandler} variant='danger'>Withdraw</Button>:<Button  onClick={participateHandler}>Participate</Button>
        }
      </Card.Body>
    </Card>
  );
}
