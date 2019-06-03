import React, { Component } from "react";
import "./Styling.css";
import ProfileBlocks from "./ProfileBlocks";
import Userpage from "../Userpage/Userpage";
// written by Lawrence Ofoli Mensah

class UserDriverProfile extends Component {
  render() {
    return (
      <div className="UserDriverProfile">
        <Userpage />
        <div className="UpperBlock">
          <div className="ProfileConstant">
            <div className="IMG" />
            <h2>marie@gmail.com</h2>
          </div>
        </div>
        <ProfileBlocks />

        <div className="ftr">
          <h1>Footer</h1>
        </div>
      </div>
    );
  }
}
export default UserDriverProfile;
