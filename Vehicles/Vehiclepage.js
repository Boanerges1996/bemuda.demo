import React from 'react';
import Vehiclebodies from './Vehiclebodie';
import './vehicleRentPage.css';
import VehicleData from './vehicleRegistered.json';


class Vehiclepage extends React.Component{

    render(){

        return (
            <div className='VehicleRentPage'>
                {VehicleData.map((postDetail,index)=>{
                    return <Vehiclebodies imageUrl={postDetail.imageUrl} 
                    CompanyName={postDetail.companyName} location={postDetail.location} 
                    Capacity={postDetail.Capacity} CarNumber={postDetail.Car_number}/>
                })}
            </div>
        )
    }
}


export default Vehiclepage;