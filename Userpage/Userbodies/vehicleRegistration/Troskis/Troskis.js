import React from "react";
import "./troskis.css";
import { Form, Button } from "react-bootstrap";
import BusReg from "../Buses/BusReg";

export default class Troski extends React.Component {
  state = {
    addVehicle: false
  };

  addVehicleToggle = () => {
    this.setState({
      addVehicle: true
    });
  };
  render() {
    let addVehicle = null;
    if (this.state.addVehicle) {
      addVehicle = <BusReg />;
    }

    return (
      <div className="troski">
        <Info Name="Location" Type="text" />
        <div className="imgUpload">
          <p /> Click to upload profile image
          <br />
          <input
            type="file"
            accept="image/*"
            name="Upload"
            className="uploadImgStyle"
          />
        </div>
        <br />
        <Button className="btnStyle" onClick={this.addVehicleToggle}>
          Add vehicle
        </Button>
        {addVehicle}
      </div>
    );
  }
}

function Info(props) {
  return (
    <div className="Infostyle">
      <div className="InfostyleA">{props.Name}</div>
      <div className="InfostyleB">
        <input
          type={props.Type}
          placeholder={props.Holder}
          className="styleInput"
        />
      </div>
    </div>
  );
}
