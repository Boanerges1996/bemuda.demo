import React from 'react';
import {Jumbotron, Container} from "reactstrap";


class ProfileContact extends React.Component {
  render() {
    return <Jumbotron>
      <Container>
        <h1 className="display-3">CONTACT US</h1>
        <p className="lead">
        <ul>
          <li>
              087255267288278
          </li>

          <li>
            0987655678998
          </li>
        </ul>
        </p>
      </Container>
    </Jumbotron>;
  }
}

export default ProfileContact;
