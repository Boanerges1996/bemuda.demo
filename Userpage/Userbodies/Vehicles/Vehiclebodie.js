import React from 'react';
import './Vehiclebodies.css';
import Vehicleownerdetails from './Carownerinfo/Vehicleownerdetails';
import Vehicleownerbackdrop from './Carownerinfo/Ownerdetailsbackdrop';



class VehicleBodies extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            showDetails:false,
        }
    }

    showOwnerDetails = ()=>{
        let valid = this.state.showDetails
        this.setState({
            showDetails:!valid
        })
    }

    
    render(){
        let userDetails = null;
        let backdrop = null;
        if(this.state.showDetails){
            userDetails = <Vehicleownerdetails Name={this.props.Username} imageUrl={this.props.ImageUrl} Sex={this.props.sex}
            Age={this.props.age} location={this.props.location} Tel={this.props.tel} />
            backdrop = <Vehicleownerbackdrop close={this.showOwnerDetails} />
        }

        return(
            <div className='VehiclesCarousel'>
            
                <img src={this.props.imageUrl} alt='Boanerges' className='carImgSearch'/>
                <div className='Vehicleinfomation'>
                    <Vehicleinfocard name="Name " value={this.props.CompanyName}/>
                    <Vehicleinfocard name="Capacity " value={this.props.Capacity}/>
                    <Vehicleinfocard name="Location" value={this.props.location}/>
                    <Vehicleinfocard name="Car number" value={this.props.CarNumber}/>
                </div>
                <div className='Vehiclesearchbottom' onClick={this.showOwnerDetails}>

                </div>
                {userDetails}
                {backdrop}
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


