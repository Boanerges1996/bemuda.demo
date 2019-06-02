import React from "react";
import BackgroundSlider from "react-background-slider";
import Header from "./Components/Homepage/Header/Header";
import Vehiclepage from "./Components/Homepage/Vehicles/Vehiclepage";
import { Jumbotron, Button } from "reactstrap";

import ScrollableAnchor from "react-scrollable-anchor";
import DemoCarousel from "./Components/Homepage/slide";
import Footer from "./Components/Homepage/footer";
import Login from "./Components/Homepage/Login/Login";
import LoginBackDrop from "./Components/Homepage/Login/LoginBackdrop";
import Signin from "./Components/Homepage/Signin/signin";
import SigninBackdrop from "./Components/Homepage/Signin/signinBackdrop";

import image1 from "./Components/Homepage/assets/bus1.jpg";
import image2 from "./Components/Homepage/assets/bus2.jpg";
import image3 from "./Components/Homepage/assets/trotro.jpg";
import image4 from "./Components/Homepage/assets/trotro2.jpg";
import image5 from "./Components/Homepage/assets/bugatti.jpg";
import image6 from "./Components/Homepage/assets/slide_1.jpg";


class Homepage extends React.Component {
  state = {
    LoginStatus: false,
    SigninStatus: false
  };
  /* Login Part */
  loginToggle = () => {
    this.setState({
      LoginStatus: true
    });
  };
  closeLoginModal = () => {
    this.setState({
      LoginStatus: false
    });
  };
  /* Sign in part */
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
    let Log = null;
    let loginBackdrop = null;
    let signin = null;
    if (this.state.LoginStatus) {
      Log = <Login />;
    }
    if (this.state.SigninStatus) {
      signin = <Signin />;
    }

    return (
      <div className="App">
        <Jumbotron>
          <div className="main">
            <div className="header">
              <Header />
            </div>

            <div className="backgroundSlider">
              <BackgroundSlider
                images={[image1, image2, image3, image4, image5, image6]}
                duration={8}
                transition={2}
              />
            </div>

            <div className="backwork">
              <p>WELCOME TO BERMUDA</p>
              <div>
                <Button onClick={this.signinToggle}>SIGN UP</Button>
              </div>
            </div>
          </div>
        </Jumbotron>
        <Jumbotron className="card">
          <p className="note"> SAVE YOURSELF THE STRESS AND RENT ONLINE</p>
          <Vehiclepage />
          <Button className="button">EXPLORE MORE</Button>
        </Jumbotron>

        <div className="slide">
          <DemoCarousel />
        </div>

        <div className="instructions">
          <Jumbotron>
            <div className="note"> HOW TO JOIN THE ROYAL FAMILY</div>
            <div>
              <img className="image" src={require("./Components/Homepage/assets/HowitWorks.png")} />
              <p className="instruct">
                <ul>
                  <li>REGISTER AS A USER</li>
                  <li>
                    ADD DRIVER'S LINENSE TO REQUISTER AS A DRIVER(OPTIONAL)
                  </li>
                  <li>ADD VEHICLES YOU WISH TO RENT OUT(OPTIONAL)</li>
                  <li>HIRE A DRIVER OR CAR OF YOUR CHOICE</li>
                  <li>UPDATE YOUR PROFILE AS ANY TIME AS U WISH</li>
                </ul>
              </p>
            </div>
          </Jumbotron>
        </div>

        <ScrollableAnchor id={"section1"}>
          <div className="aboutus">
            <Jumbotron>
              <h1 className="display-3"> ABOUT US</h1>
              <div className="about">
                <p className="lead">
                  <strong> MISSION : </strong> We want to bring modernisation,
                  speed and efficiency to vehicle rentals and we are dedicated
                  in giving you the very best service rentals can offer. We
                  pride ourselves in the services we offer.We offer an advanced
                  rental frontier that is very effective. Bermuda Rentals is an
                  advancement in the rental business. It is a platform every
                  individual who owns a vehicle as well as every eligible driver
                  can use to make some extra money during their free time.
                </p>
              </div>
              <hr className="my-2" />
              <div className="about">
                <p className="lead">
                  {" "}
                  <strong>VISION: </strong> Here at Bermuda rentals our vision
                  goes beyond the borders of the country. We envision our
                  services being patronised on an international scale.
                </p>
              </div>
            </Jumbotron>
          </div>
        </ScrollableAnchor>

        <ScrollableAnchor id={"section2"}>
          <div className="services">
            <Jumbotron>
              <h1 className="display-32"> SERVICES</h1>
              <p className="lead2">
                {" "}
                Our services range from personal vehicle rentals to ABOBOYA
                rentals. Our present services are
                <ol className="list">
                  <li>Vehicle Rental</li>
                  <li>Chauffuer Services</li>
                  <li>Driver Hiring</li>
                </ol>
              </p>
              <hr className="my-2" />
              <p className="lead2">
                {" "}
                <strong>
                  {" "}
                  Here at Bermuda rentals we treat you like FAMILY and Royalty{" "}
                </strong>
              </p>
            </Jumbotron>
          </div>
        </ScrollableAnchor>

        <ScrollableAnchor id={"section3"}>
          <div className="aboutus">
            <Jumbotron>
              <h1 className="display-3"> CONTACT US</h1>
              <div className="about">
                {" "}
                <p className="lead">
                  <strong> EMAILS : </strong>
                  <ul>
                    <li>hazungah@gmail.com</li>
                    <li>hazungah@gmail.com</li>
                    <li>hazungah@gmail.com</li>
                  </ul>
                </p>
              </div>

              <div className="about">
                <p className="lead">
                  {" "}
                  <strong>NUMBERS: </strong>
                  <ul>
                    <li>02445687738</li>
                    <li>02445687738</li>
                    <li>02445687738</li>
                    <li>02445687738</li>
                  </ul>
                </p>
              </div>
            </Jumbotron>
          </div>
        </ScrollableAnchor>
        <Footer />

        {Log}
        {signin}
        {this.state.LoginStatus ? (
          <LoginBackDrop click={this.closeLoginModal} />
        ) : null}
        {this.state.SigninStatus ? (
          <SigninBackdrop click={this.closeSigninBack} />
        ) : null}
      </div>
    );
  }
}

export default Homepage;
