import React from 'react';
import './Vehiclebodies.css';



class VehicleBodies extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            one:{
                capacity:120,
                imageUrl:"https://firebasestorage.googleapis.com/v0/b/vehicle-rental-a0b39.appspot.com/o/Vehicles%2FBus%2F3.jpg?alt=media&token=8e46b803-af6d-4722-9155-caa3cac39e89",
                ownerName:'VIP',
                carNumber:'GT 3421-18',
                location:'Accra',
                Comment:'We serve you well',

            }
        }
    }

    
    render(){
        return(
            <div className='VehiclesCarousel'>
                <img src={this.props.imageUrl} alt='Boanerges' className='carImgSearch'/>
                <div className='Vehicleinfomation'>
                    <Vehicleinfocard name="Name " value={this.props.CompanyName}/>
                    <Vehicleinfocard name="Capacity " value={this.props.Capacity}/>
                    <Vehicleinfocard name="Location" value={this.props.location}/>
                    <Vehicleinfocard name="Car number" value={this.props.CarNumber}/>
                </div>
                <div className='Vehiclesearchbottom'>

                </div>
            </div>
        )
    }
}

export default VehicleBodies;

function Vehicleinfocard(props){
    return (
        <div className='Vehicleinfocard'>
            <h4> {props.name}</h4>&nbsp;
            <h3> {props.value}</h3>
        </div>
    )
}