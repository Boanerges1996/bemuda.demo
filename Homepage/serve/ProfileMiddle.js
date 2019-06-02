import React from 'react';
import {Jumbotron, Container} from "reactstrap";


class ProfileMiddle extends React.Component {
  render() {
    return <Jumbotron className="about">
      <Container>
        <h1 className="display-3">ABOUT US</h1>
        <p className="lead">
        <ul>
<li><strong>Mission</strong> : We want to bring modernisation, speed and efficiency to vehicle rentals and we are dedicated in giving you the very best
            service rentals can offer. We pride ourselves in the services we offer.We offer an advanced rental frontier that is very effective.
            Bermuda Rentals is an advancement in the rental business. It is a platform every individual who owns a vehicle as well as every
            eligible driver can use to make some extra money during their free time.</li>

            <li>
            <strong>Vision</strong> : Here at Bermuda rentals our vision goes beyond the borders of the country. We envision our services being patronised on
            an international scale.
            </li>

        </ul>
        </p>
        

      </Container>
    </Jumbotron>;
  }
}

export default ProfileMiddle;
