import React from 'react';
import {Jumbotron, Container} from "reactstrap";


class ProfileServices extends React.Component {
  render() {
    return <Jumbotron>
      <Container>
        <h1 className="display-3">OUR SERVICES</h1>
        <p className="lead">
        <ul>
          <li>
          Vehicle Rental
          </li>
          <li>
          Chauffuer Services

          </li>
          <li>
          Driver Hiring
          </li>
        </ul>
        </p>
      </Container>
    </Jumbotron>;
  }
}

export default ProfileServices;
