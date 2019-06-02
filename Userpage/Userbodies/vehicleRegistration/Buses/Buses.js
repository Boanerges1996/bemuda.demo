import React from 'react';
import './Buses.css';
import { Button } from 'semantic-ui-react';
import BusReg from './BusReg'



export default class Buses extends React.Component{
    state={
        addVehicle:false
    }

    addVehicleToggle =()=>{
        this.setState({
            addVehicle:true
        })
    }

    render(){
        let addVehicle = null
        if(this.state.addVehicle){
            addVehicle = <BusReg />
        }

        return(
            <div className="buses">
                <Info Name="Company Name" Holder="Please enter your company name" Type="text"/>
                <Info Name="Location" Holder="Location" Type="Text"/>
                <div className="imgUpload"> 
                   <p></p> Click to upload profile image<br/>
                    <input type="file" accept="image/*" name="Upload" className="uploadImgStyle" />
                </div>
                <br />
                <Button className="btnStyle" onClick={this.addVehicleToggle}>
                    Add vehicle
                </Button>
                {addVehicle}
                
            </div>
           
           
        )
    }
}


export function Info(props){

    return (
        <div className="Infostyle">
            <div className="InfostyleA">
                {props.Name}
            </div>
            <div className="InfostyleB">
                <input type={props.Type} placeholder={props.Holder} className="styleInput"/>
            </div>
        </div>
    )
}

