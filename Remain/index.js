import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
// import firebase from 'firebase/app';
// import 'firebase/storage';

// Your web app's Firebase configuration
// var firebaseConfig = {
//     apiKey: "AIzaSyCzukecsl2blavSOZwsi81uTPl7Nz-rLGw",
//     authDomain: "vehicle-rental-a0b39.firebaseapp.com",
//     databaseURL: "https://vehicle-rental-a0b39.firebaseio.com",
//     projectId: "vehicle-rental-a0b39",
//     storageBucket: "vehicle-rental-a0b39.appspot.com",
//     messagingSenderId: "74637671229",
//     appId: "1:74637671229:web:f223fbc79f02d914"
//   };
//   // Initialize Firebase
//   firebase.initializeApp(firebaseConfig);

// const storage = firebase.storage()
// export {
//     storage,firebase as default
// }

ReactDOM.render(<App />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
