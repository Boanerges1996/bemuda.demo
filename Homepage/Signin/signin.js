import React from "react";
import "./signin.css";
import { Jumbotron, Container } from "reactstrap";

// written by Azungah Hillary

class Signin extends React.Component {
  state = {
    firstname: "",
    lastname: "",
    phonenumber: "",
    email: "",
    password: "",
    confirmpass: "",

    firstnameError: "",
    lastnameError: "",
    phonenumberError: "",
    emailError: "",
    passwordError: "",
    confirmpassError: "",
    showError: false
  };

  /*
    Handling submit functions and events
     */
  isNum = num => {
    return /[0-9]$/.test(num);
  };

  change = e => {
    let value = e.target.value;
    this.setState({
      phonenumber: value
    });
  };
  validateSignForm = () => {
    let emailError = "";
    if (!this.state.email.includes("@")) {
      this.setState({
        showError: true,
        emailError: "error"
      });
    }
    if (emailError) {
      this.setState({
        emailError: emailError
      });
      return false;
    }

    // let phonenumberError ='';
    // if(!this.isNum(this.state.phonenumber)){
    //     this.setState({
    //         showError:true,
    //         phonenumberError:"error"
    //     })
    // }
    // if(phonenumberError){
    //     this.setState({
    //         phonenumberError:phonenumberError
    //     })
    // }
  };

  sigininSubmit = event => {
    event.preventDefault();
    const isVal = this.validateSignForm;
  };
  render() {
    const style = {
      fontSize: "20px"
    };
    const formErrors = {
      color: "red",
      fontSize: "12px"
    };
    let errorMessage = null;
    if (this.state.showError) {
      errorMessage = <div>{this.state.emailError}</div>;
    }

    return (
      <Container>
        <div className="Signin">
          <div className="SigninActual">
            <div className="SigninActualComment">
              <h1>BERMUDA RENTALS</h1>
              {/* <p style={style}>
                <p>Welcome to Bermuda Rentals</p> */}
              {/* <p>SIGNUP HERE</p> */}
              {/* </p> */}
            </div>
            <Jumbotron className="forms">
              <form className="myForm" onSubmit={this.sigininSubmit}>
                <input
                  type="text"
                  name="firtname"
                  className="SigninInputBox"
                  placeholder="&#xf007; Firstname"
                />
                <br />
                <div style={formErrors}>{this.state.firstnameError}</div>

                <input
                  type="text"
                  name="lastname"
                  placeholder="&#xf007; Lastname"
                  className="SigninInputBox"
                />
                <br />
                <div style={formErrors}>{this.state.lastnameError}</div>

                <input
                  type="text"
                  name="othernames"
                  placeholder="&#xf007; Othernames"
                  className="SigninInputBox"
                />
                <br />

                <input
                  type="text"
                  name="phonenumber"
                  placeholder="&#xf095; Phone"
                  onChange={this.change}
                  className="SigninInputBox"
                />
                <br />
                <div style={formErrors}>{this.state.phonenumberError}</div>

                <input
                  type="email"
                  name="email"
                  placeholder="&#xf199; Email"
                  className="SigninInputBox"
                />
                <br />
                {errorMessage}

                <input
                  type="password"
                  name="password"
                  placeholder="&#xf084; Password"
                  className="SigninInputBox"
                />
                <br />
                <div style={formErrors}>{this.state.passwordError}</div>

                <input
                  type="password"
                  name="confirmpass"
                  placeholder="&#xf084; Confirm Password"
                  className="SigninInputBox"
                />
                <br />
                <div style={formErrors}>{this.state.confirmpassError}</div>
                <input
                  type="submit"
                  name="submit"
                  className="SigninSubmitStyle"
                  value="SIGNUP"
                />
              </form>
            </Jumbotron>
          </div>
          <div className="SigninOther">
            <div className="SigninOtherCovering" />
          </div>
        </div>
      </Container>
    );
  }
}
export default Signin;
