// written by Azungah Hillary

import React, { Component } from "react";
import Signin from "./Signin/signin";
import SigninBackdrop from "./Signin/signinBackdrop";


class Footer extends React.Component {
  state = {
    SigninStatus: false
  };

  signinToggle = () => {
    this.setState({
      SigninStatus: true
    });
  };
  closeSigninBack = () => {
    this.setState({
      SigninStatus: false
    });
  };

  render() {
    let signin = null;

    if (this.state.SigninStatus) {
      signin = <Signin />;
    }

    return (
      <div className="footer">
        <div className="word">
          <div className="Logo" />
          <div className="motivate">
            <p> BERMUDA </p>
          </div>
        </div>

        <div className="solutions">
          <ol className="solutionss">
            <li>SOLUTIONS</li>
            <li>CHAFFEUR SERVICESs</li>
            <li>VEHICLE RENTALS</li>
            <li>DRIVER RENTALS</li>
          </ol>
        </div>

        <div className="lastdiv">
          <a href="#section3" className="one">
            CONTACT US
          </a>
          <a className="two" onClick={this.signinToggle}>
            JOIN US
          </a>
        </div>

        {signin}
        {this.state.SigninStatus ? (
          <SigninBackdrop click={this.closeSigninBack} />
        ) : null}
      </div>
    );
  }
}

export default Footer;
