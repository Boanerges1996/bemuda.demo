import React from "react";
// import {Form,Row,Col} from 'react-bootstrap';
import "./VehicleRegistration.css";
import Buses from "./Buses/Buses";
import Troskis from "./Troskis/Troskis";
import PrivateCar from "./PrivateCar/PrivateCar";
import OtherVehicle from "./otherVehicles/otherVehicles";
import Userpage from "../../Header/Userheader";

class VehicleRegistraion extends React.Component {
  state = {
    bus: false,
    troski: false,
    privateCar: false,
    otherVehicles: false
  };

  toggleToBus = () => {
    this.setState({
      bus: true,
      troski: false,
      privateCar: false,
      otherVehicles: false
    });
  };
  toggleToTroski = () => {
    this.setState({
      bus: false,
      troski: true,
      privateCar: false,
      otherVehicles: false
    });
  };
  toggleToPrivateCar = () => {
    this.setState({
      bus: false,
      troski: false,
      privateCar: true,
      otherVehicles: false
    });
  };
  toggleToOtherVehicles = () => {
    this.setState({
      bus: false,
      troski: false,
      privateCar: false,
      otherVehicles: true
    });
  };
  render() {
    let bus = null;
    let troski = null;
    let privateCar = null;
    let otherVehicle = null;
    if (this.state.bus) {
      bus = <Buses />;
    }
    if (this.state.troski) {
      troski = <Troskis />;
    }
    if (this.state.privateCar) {
      privateCar = <PrivateCar />;
    }
    if (this.state.otherVehicles) {
      otherVehicle = <OtherVehicle />;
    }

    return (
      <div>
        <Userpage />
        <div className="vehicleregistration">
          <div>
            <Myselections
              Name="Buses"
              name="vehicle"
              click={this.toggleToBus}
            />
            <Myselections
              Name="Troski"
              name="vehicle"
              click={this.toggleToTroski}
            />
            <Myselections
              Name="Private Car"
              name="vehicle"
              click={this.toggleToPrivateCar}
            />
            <Myselections
              Name="Other Vehicles"
              name="vehicle"
              click={this.toggleToOtherVehicles}
            />
          </div>
          {bus}
          {troski}
          {privateCar}
          {otherVehicle}
        </div>
      </div>
    );
  }
}

export default VehicleRegistraion;

function Myselections(props) {
  return (
    <div className="labelInput">
      <label>{props.Name}</label>
      <br />
      <input type="radio" name={props.name} onChange={props.click} />
    </div>
  );
}
