import React, { useContext, useEffect } from "react";
import { 
  CDBSidebar,
  CDBSidebarContent,
  CDBSidebarFooter,
  CDBSidebarHeader,
  CDBSidebarMenu,
  CDBSidebarMenuItem } from "cdbreact";
import { NavLink, useNavigate } from "react-router-dom";
import RefreshToken from "../utils/refreshToken";
import { Store } from "../store/StoreProvider";

const Sidebar = ({children}) => {

  const { state, dispatch: contextDispatch } = useContext(Store);
  const { refresh } = RefreshToken();
  const navigate = useNavigate();

  useEffect(()=>{

    // Sidebar will be only used for Private Routes.
    if (!state.userDetails) {
      navigate('/home');
    }
    
    // Refreshes the token when the sidebar loads, 
    // this way the user won't log out if stays active on website.
    refresh();

  },[])  

  const signOutHandler = () => {
    contextDispatch({ type: 'USER_SIGN_OUT' });
  };

  return (
    <div className="d-flex">
      <div>
    <div
      className={`app`}
      style={{ display: "flex", height: "100vh", overflow:"scroll initial"}}
    >
      <CDBSidebar
        textColor="#fff"
        backgroundColor="#333"
      >
        <CDBSidebarHeader
          prefix={
            <i className="fa fa-bars fa-large"></i>
          }
        >
          <a href="/" className="text-decoration-none" style={{color:"inherit"}}>
            Road College
          </a>
        </CDBSidebarHeader>

        <CDBSidebarContent className="sidebar-content">
          <CDBSidebarMenu>
            <NavLink
              exact
              to="/"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="columns"
              >
                Dashboard
              </CDBSidebarMenuItem>
            </NavLink>
            <NavLink
              exact
              to="/gala-events"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="calendar"
              >
                Gala Events
              </CDBSidebarMenuItem>
            </NavLink>
            <NavLink
              exact
              to="/results"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="bar-chart"
              >
                Results
              </CDBSidebarMenuItem>
            </NavLink>
            <NavLink
              exact
              to="/practice-sessions"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="thermometer-half"
              >
                Practice Sessions
              </CDBSidebarMenuItem>
            </NavLink>
            <NavLink
              exact
              to="/profile"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="user"
              >
                Profile
              </CDBSidebarMenuItem>
            </NavLink>
            {state?.userDetails?.role === "Parents"? <NavLink
              exact
              to="/members"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="user-plus"
              >
                Members
              </CDBSidebarMenuItem>
            </NavLink>: <div></div>}
            <NavLink
              exact
              to="/home"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="sign-out"
                onClick={signOutHandler}
              >
                Sign Out
              </CDBSidebarMenuItem>
            </NavLink>
          </CDBSidebarMenu>
          <CDBSidebarMenu>
          </CDBSidebarMenu>
        </CDBSidebarContent>

        <CDBSidebarFooter style={{ textAlign: "center" }}>
          <div
            className="sidebar-btn-wrapper"
            style={{
              padding: "20px 5px"
            }}
          >
            Sidebar Footer
          </div>
        </CDBSidebarFooter>
      </CDBSidebar>
    </div>
    </div>
    {children}
    </div>
  );
}

export default Sidebar;
