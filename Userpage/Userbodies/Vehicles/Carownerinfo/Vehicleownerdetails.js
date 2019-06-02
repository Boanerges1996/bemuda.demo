import React from 'react';
import './Vehicleownerdetails.css';



class Vehicleownerdetails extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            
        }
    }

    
    render(){
        return(
            <div className='Vehicleownerdetails'>
            
                <img src={this.props.imageUrl} alt='Boanerges' className='carImgSearch'/>
                <div className='Vehicleinfomation'>
                    <Vehicleinfocard name="Name " value={this.props.Name}/>
                    <Vehicleinfocard name="Age " value={this.props.Age}/>
                    <Vehicleinfocard name="Sex" value={this.props.Sex}/>
                    <Vehicleinfocard name="Location" value={this.props.location}/>
                    <Vehicleinfocard name="Tel. " value={this.props.Tel}/>
                </div>
                
            </div>
        )
    }
}

export default Vehicleownerdetails;

function Vehicleinfocard(props){
    return (
        <div className='Vehicleinfocard'>
            <h4> {props.name}</h4>&nbsp;
            <h3> {props.value}</h3>
        </div>
    )
}


