import React from 'react';
import './UserServicesModal.css';



function UserServiceModal (props){
    //A property of click will be added so that when clicked the modal will closes;
    //Also when the Services Modal closes the particular clicked COMPONENT will be render
    //Example when VEHICLE REGISTER is clicked it will render that particular COMPONENT

    return(
        <div className='UserServiceModal'>
            <div className='ServicesNames'>
                Vehicle
            </div>
            <div className='ServicesNames'>
                Drivers
            </div>
            <div className='ServicesNames'>
                Register Vehicle
            </div>
            <div className='ServicesNames'>
                Register Driver
            </div>
        </div>
    )
}

export default UserServiceModal;