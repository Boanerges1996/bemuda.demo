import React, { Component } from "react";
import "./Login.css";

// import "../../node_modules/font-awesome/css/font-awesome.min.css";

{
  /*import '../../../node_modules/font-awesome/css/font-awesome.min.css';*/
}
/*
Written by Azungah Hillary 


EDITING REQUIRED
1. The Submit button animation on hover.
2. Add an image to the front of the
*/

class Login extends Component {
  state = {
    username: ""
  };

  render() {
    const style = {
      fontSize: "20px"
    };
    return (
      <div className="Login">
        <div className="LoginActual">
          <div className="LoginActualComment">
            <h1 className="head">
              <strong>Bemuda Rentals</strong>
            </h1>
            <p style={style}>Login to enjoy our wondeful services</p>
            <img src={require("./Logo.png")} alt="LoginLogo" />
          </div>
          <form className="myForm">
            <input
              type="text"
              name="username"
              className="LoginInputBox"
              placeholder="&#xf007; Username"
            />
            <br />
            <input
              type="password"
              name="password"
              placeholder="&#xf09c; Password"
              className="LoginInputBox"
            />
            <br />
            <input
              type="submit"
              name="submit"
              className="LoginSubmitStyle"
              value="Login"
            />
          </form>
        </div>

        <div className="LoginOther">
          <div className="LoginOtherCovering" />
        </div>
      </div>
    );
  }
}

export default Login;
