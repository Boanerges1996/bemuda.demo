import React, { Component } from "react";
import ReactDOM from "react-dom";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from "react-responsive-carousel";

class DemoCarousel extends Component {
  render() {
    return (
      <Carousel className="slider">
        <div>
          <img className="ima" src={require("./assets/trotro.jpg")} />
          <p className="legend">
            <a>JOIN US</a>
          </p>
        </div>
        <div>
          <img className="ima" src={require("./assets/slide_1.jpg")} />
          <p className="legend">
            <a>BOOK NOW TO DRIVE THIS BEAUTY</a>
          </p>
        </div>
        <div>
          <img className="ima" src={require("./assets/bugatti.jpg")} />
          <p className="legend">
            <a>YOU DONT KNOW WHAT IS GOING ON!!!!!!!!!!!!</a>
          </p>
        </div>

        <div>
          <img className="ima" src={require("./assets/cover2.png")} />
          <p className="legend">
            <a>JOIN US</a>
          </p>
        </div>

        <div>
          <img className="ima" src={require("./assets/bus2.jpg")} />
          <p className="legend">
            <a>JOIN US</a>
          </p>
        </div>

        <div>
          <img className="ima" src={require("./assets/bus1.jpg")} />
          <p className="legend">
            <a>JOIN US</a>
          </p>
        </div>

        <div>
          <img className="ima" src={require("./assets/trotro2.jpg")} />
          <p className="legend">
            <a>JOIN US</a>
          </p>
        </div>
      </Carousel>
    );
  }
}
export default DemoCarousel;
