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
            Contrast
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
                dashboard
              </CDBSidebarMenuItem>
            </NavLink>
            <NavLink
              exact
              to="/tables"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="table"
              >
                tables
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
                profile
              </CDBSidebarMenuItem>
            </NavLink>
            <NavLink
              exact
              to="/home"
              activeClassName="activeClicked"
            >
              <CDBSidebarMenuItem
                icon="logout"
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
