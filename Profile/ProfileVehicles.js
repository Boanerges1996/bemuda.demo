import React, { Component } from "react";
// written by Lawrence Ofoli Mensah
class ProfileVehicle extends Component {
  state = {
    Vehicles: [{ title: "VEHICLE", noRegCars: "30" }]
  };

  render() {
    return (
      <div className="ProfileVehicle">
        <h1> {this.state.Vehicles[0].title}</h1>
        <p> Registered Cars {this.state.Vehicles[0].noRegCars}</p>
        <button>Display Vehicles</button>
      </div>
    );
  }
}
export default ProfileVehicle;
