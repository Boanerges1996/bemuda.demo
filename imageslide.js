import React from "react";
import { Slide } from "react-slideshow-image";
import "./imageslide.css";
import { Fade } from "react-slideshow-image";

//written by Azungah Hillary

const properties = {
  duration: 4000,
  transitionDuration: 500,
  infinite: true,
  indicators: true,
  arrows: true
};
const fadeProperties = {
  duration: 5000,
  transitionDuration: 500,
  infinite: true,
  indicators: true
};

const Slideshow = () => {
  return (
    <Fade {...fadeProperties}>
      <div className="each-slide">
        <img src={require("./assets/trotro.jpg")} className="imageEdit" />
      </div>
      <div className="each-slide">
        <img src={require("./assets/trotro.jpg")} className="imageEdit" />
      </div>
      <div className="each-slide">
        <img src={require("./assets/trotro.jpg")} className="imageEdit" />
      </div>
      <div className="each-slide">
        <img src={require("./assets/trotro.jpg")} className="imageEdit" />
      </div>
    </Fade>
  );

  {
    /* <Slide {...properties}>
      <div className="each-slide">
        <img src={require('./slide_1.jpg')} className='imageEdit'/>
      </div>
      <div className="each-slide">
        <img src={require('./slide_2.jpg')} className='imageEdit'/>
      </div>
      <div className="each-slide">
          <img src={require('./slide_3.jpg')}  className='imageEdit'/>
      </div>
      <div className="each-slide">
          <img src={require('./slide_4.jpg')} className='imageEdit'/>
      </div>
  </Slide>*/
  }
};
export default Slideshow;
