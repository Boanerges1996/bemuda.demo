import React from 'react';
import './Ownerdetailsbackdrop.css';


class OwnerdetailsBackdrop extends React.Component{

    render(){


        return (
            <div className="Ownerdetailsbackdrop" onDoubleClick={this.props.close}>

            </div>
        )
    }
}

export default OwnerdetailsBackdrop;
