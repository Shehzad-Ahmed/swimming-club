import './App.css';
// import Navbar from './components/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import SignUp from './screens/signup/SignUp';
import Login from './screens/login/Login';
import Dashboard from './screens/dashboard/Dashboard2';
import Home from './screens/home/Home';
import Profile from './screens/profile/Profile';
import GalaEvents from './screens/gala/GalaEvents';
import Results from './screens/results/Results';
import PracticeSessions from './screens/practice/PracticeSessions';
import Members from './screens/members/Members';
// import Sidebar from './screens/Sidebar';

function App() {

  return (
    <BrowserRouter>
      <div className="d-flex flex-column site-container">
        <ToastContainer position="bottom-center" limit={1} />
        <header>
          <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
          ></link>
          {/* <Navbar></Navbar> */}
          {/* <Sidebar></Sidebar> */}
        </header>
        <main>
          <Routes>
            <Route path="signup/" element={<SignUp />}></Route>
            <Route path="signin/" element={<Login />}></Route>
            <Route path="/" element={<Dashboard/>}></Route>
            <Route path="home/" element={<Home></Home>}></Route>
            <Route path="profile/" element={<Profile></Profile>}></Route>
            <Route path="gala-events/" element={<GalaEvents></GalaEvents>}></Route>
            <Route path="results/" element={<Results></Results>}></Route>
            <Route path="practice-sessions" element={<PracticeSessions></PracticeSessions>}></Route>
            <Route path="members/" element={<Members></Members>}></Route>
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
