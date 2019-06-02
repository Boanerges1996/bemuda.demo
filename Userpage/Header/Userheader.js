import React from 'react';
import './Userheader.css';
import UserServiceModal from './UserHeadeServiceModal/UserServiceModal';
import UserServiceModalBackDrop from './UserHeadeServiceModal/UserServiceModalBack';
import UserprofileModal from './UserprofileInfo/Userprofileinfo';
import { Route,Link } from 'react-router-dom';
{/*import '../../../../../node_modules/font-awesome/css/font-awesome.min.css';*/}

class Userheader extends React.Component{
    constructor(props){
        super(props)
    }
    state = {
        servicesModal:false,
        userProfileStatus:false
    }

    //SERVICES MODAL
    //This Shows the Services Modal when Click and also closes it when clicked
    showServices=()=>{
        let modalChanger = this.state.servicesModal
        this.setState({
            servicesModal:!modalChanger,
            userProfileStatus:false
        })
    }

    //----------------------------------------------------------
    //This closes the service modal when double click
    closeServicesModal = ()=>{
        this.setState({
            servicesModal:false,
            
        })
    }
    //----------------------------------------------------
    

    //USERPROFILE MODAL
    //--------Toggle Profile Status ---------------------
    toggleUserProfile=()=>{
        let toggleMe = this.state.userProfileStatus
        this.setState({
            userProfileStatus:!toggleMe,
            servicesModal:false,
        })
    }


    render(){
        //For the opening and closing of the services modal
        //---------------------------------------------------------------------------------
        let serviceModal = null;
        let serviceModalBackDrop = null;
        let userProfileModalInfo = null;

        if(this.state.servicesModal){
            serviceModal = <UserServiceModal />
            serviceModalBackDrop =<UserServiceModalBackDrop click={this.closeServicesModal}/>
            
        }
        if(this.state.userProfileStatus){
            userProfileModalInfo = <UserprofileModal />
        }
        //-----------------------------------------------------------------------------------


        return(
            <div className='Userheader'>
                <div className='Userlogo'>
                    <img src={require('./BermudaLogo.png')} className='BermudaLogoStyles'/>
                </div>
                {/* This will be for the Services at a width of 640px, 
                    Vehicles
                    Drivers
                    Register Drivers
                    Register Vehicles
                */}
                {/*------------------------------------------------------------------ */}
                <div className='serviceAt' onClick={this.showServices}>
                    <i class="fa fa-bars fa-3x positionme"></i>
                </div>
                {/*------------------------------------------------------------------ */}

                <div className='Userservices'>
                    <div className='UserserviceMid'>
                        <div className='bServicesSmall'>
                            <Link to='/user/vehicles'>VEHICLE</Link>
                        </div>
                        <div className='bServices'>
                            <Link to="/user/vehicle/registration" >REGISTER VEHICLE</Link>
                        </div>
                        <div className='bServicesSmall'>
                            <Link to='/user/driver' >DRIVERS</Link>
                        </div>
                        <div className='bServices'>
                            <Link to='/user/driver/registration' >REGISTER DRIVER</Link>
                        </div>
                    </div>
                </div>

                {/*------------------------Central Logo at 640px-------------------- */}
                <div className='LogoAt640'>
                    <img src={require('./BermudaLogo.png')} className='BermudaLogo'/>
                </div>
                {/*------------------------------------------------------------------ */}

                {/*This will show the user account details through a dropdown */}
                {/*View and Edit Account */}
                {/*Setting */}
                {/*Logout*/}
                <div className='Useravatar'>
                    <div className='Avatar'>
                        {/*The SRC of the image file will come from FIREBASE and will be rendered here*/}
                        <img src={require('./boanerges.jpg')} className='avatarstyles' onClick={this.toggleUserProfile}/>

                    </div>
                </div>
                {serviceModal}
                {serviceModalBackDrop}
                {userProfileModalInfo}
            </div>
        )
    }
}
export default Userheader;