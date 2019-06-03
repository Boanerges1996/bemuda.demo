import React, { Component } from "react";
// written by Lawrence Ofoli Mensah

class ProfileDriver extends Component {
  state = {
    Drivers: [
      {
        title: "DRIVER",
        age: "30",
        gender: "male",
        address: "GGG",
        lincence: "lawrence"
      }
    ]
  };
  render() {
    return (
      <div className="ProfileDriver">
        <h1> {this.state.Drivers[0].title}</h1>
        <p>age{this.state.Drivers[0].age}</p>
        <p>gender{this.state.Drivers[0].gender}</p>
        <p>address{this.state.Drivers[0].address}</p>
        <p>lincence {this.state.Drivers[0].lincence}</p>
      </div>
    );
  }
}
export default ProfileDriver;
