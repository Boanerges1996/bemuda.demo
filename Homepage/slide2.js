import React, { Component } from 'react'
 
import BackgroundSlideshow from 'react-background-slideshow'
 
import image1 from './assets/trotro.jpg'
import image2 from './assets/trotro.jpg'
import image3 from './assets/trotro.jpg'
 
export default class App extends Component {
  render () {
    return (
      <div>
        <BackgroundSlideshow images={[ image1, image2, image3 ]} />
      </div>
    )
  }
}