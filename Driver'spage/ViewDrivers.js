import React, { Component } from "react";
import "./ViewDrivers.css";
import DriverClass from "./DriverClass";
import Base from "./Base";
import Userpage from "../Userpage/Userpage";
// written by Lawrence Ofoli Mensah

class ViewDrivers extends Component {
  state = {
    Drivers: [
      {
        ImgUrl: require("./pic.jpg"),
        id: 1,
        name: "francis",
        Age: 45,
        Gender: "Male"
      },
      {
        ImgUrl: require("./pic.jpg"),
        id: 2,
        name: "frank",
        Age: 25,
        Gender: "Male"
      },
      {
        ImgUrl: require("./pic.jpg"),
        id: "3",
        name: "beatson",
        Age: 35,
        Gender: "Female"
      }
    ],
    ViewDetail: false
  };

  ViewDetailHandler = () => {
    this.setState({ ViewDetail: true });
  };
  ViewedHandler = () => {
    this.setState({ ViewDetail: false });
  };

  render() {
    let BaseContent = null;
    return (
      <div className="ViewDrivers">
        <Userpage />
        {this.state.Drivers.map(driver => {
          return (
            <DriverClass
              ImgUrl={driver.ImgUrl}
              name={driver.name}
              Age={driver.Age}
              Gender={driver.Gender}
              key={driver.id}
              click={this.ViewDetailHandler}
            />
          );
        })}
        {this.state.ViewDetail
          ? (BaseContent = <Base bclick={this.ViewedHandler} />)
          : null}
        {BaseContent}
      </div>
    );
  }
}
export default ViewDrivers;
