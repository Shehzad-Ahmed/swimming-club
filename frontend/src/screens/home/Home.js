import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Button, Grid, Typography } from '@material-ui/core';
import PoolIcon from '@material-ui/icons/Pool';
import SchoolIcon from '@material-ui/icons/School';
import { useNavigate } from 'react-router-dom';
import FitnessCenterIcon from '@material-ui/icons/FitnessCenter';

const useStyles = makeStyles((theme) => ({
  jumbotron: {
    backgroundImage: 'url(/img/swiming-pool.jpg)',
    backgroundSize: 'cover',
    height: 'calc(100vh - 64px)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'column',
    color: 'white',
    textAlign: 'center',
  },
  section: {
    padding: theme.spacing(8, 0),
  },
  icon: {
    fontSize: 64,
    marginBottom: theme.spacing(2),
  },
  button: {
    margin: theme.spacing(2),
  }
}));

function Home() {
  const classes = useStyles();
  const navigate = useNavigate();



  return (
    <div>
      <div className={classes.jumbotron}>
        <Typography variant="h1">Welcome to our Swimming Club</Typography>
        <Typography variant="h4" gutterBottom>
          Join us for a fun and challenging workout in the water!
        </Typography>
        <Grid>
        <Button className={classes.button} variant="contained" color="dark" size="large" onClick={()=>navigate('/signin')}>
          Sign In
        </Button>
        <Button className={classes.button} variant="contained" color="secondary" size="large" onClick={()=>navigate('/signup')}>
          Join Now
        </Button>
        </Grid>
      </div>
      <Grid container className={classes.section}>
        <Grid item xs={12} md={4}>
          <PoolIcon className={classes.icon} />
          <Typography variant="h4" gutterBottom>
            Swimming Lessons
          </Typography>
          <Typography variant="body1" gutterBottom>
            We offer a variety of swimming lessons for all ages and skill levels.
          </Typography>
          <Button variant="outlined" color="secondary">
            Learn More
          </Button>
        </Grid>
        <Grid item xs={12} md={4}>
          <SchoolIcon className={classes.icon} />
          <Typography variant="h4" gutterBottom>
            Swim Team
          </Typography>
          <Typography variant="body1" gutterBottom>
            Join our competitive swim team and compete against other clubs.
          </Typography>
          <Button variant="outlined" color="secondary">
            Learn More
          </Button>
        </Grid>
        <Grid item xs={12} md={4}>
          <FitnessCenterIcon className={classes.icon} />
          <Typography variant="h4" gutterBottom>
            Aquatic Fitness
          </Typography>
          <Typography variant="body1" gutterBottom>
            Our aquatic fitness classes offer a low-impact workout that's easy on your joints.
          </Typography>
          <Button variant="outlined" color="secondary">
            Learn More
          </Button>
        </Grid>
      </Grid>
    </div>
  );
}

export default Home;
