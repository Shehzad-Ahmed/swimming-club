import Navbar from "./Navbar";
import Sidebar from "./Sidebar"



const SidbarNav = ({children}) => {
    
    return (<Sidebar>
        <div style={{flex:"1 1 auto", display:"flex", flexFlow:"column", height:"100vh", overflowY:"hidden"}}>
        <Navbar></Navbar>
        <div style={{height:"100%"}}>
	        <div style={{height:"calc(100% - 64px)", overflowY:"scroll"}}>
        {children}
        </div>
        </div>
        </div>
        </Sidebar>
        )
}

export default SidbarNav;