import React from 'react';
import './UserpageWhole.css';
import Userheader from './Header/Userheader';


class Userpage extends React.Component{


    render(){


        return(
            <div className='UserpageWhole'>
                <Userheader />
            </div>
        )
    }
}

export default Userpage;