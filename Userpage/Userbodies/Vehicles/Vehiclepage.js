import React from 'react';
import Vehiclebodies from './Vehiclebodie';
import './vehicleRentPage.css';
import VehicleData from './vehicleRegistered.json';
import Userpage from '../../Header/Userheader';




class Vehiclepage extends React.Component{

    state = {
        showUserDetail:true
    }


    render(){

        return (
            <div className='VehicleRentPage'>
                <Userpage />
                {VehicleData.map((postDetail,index)=>{
                    return <Vehiclebodies imageUrl={postDetail.imageUrl} 
                    CompanyName={postDetail.companyName} location={postDetail.location} 
                    Capacity={postDetail.Capacity} CarNumber={postDetail.Car_number} Username={postDetail.Name} ImageUrl={postDetail.imageurl}
                    sex={postDetail.Sex} age={postDetail.Age} location={postDetail.city} tel={postDetail.telephone}/>
                })}
            </div>
        )
    }
}


export default Vehiclepage;