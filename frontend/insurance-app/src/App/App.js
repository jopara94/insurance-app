import React, { Component } from "react";
import Dashboard from "../Dashboard/dashboard";
import Plans from "../Plans/plans";
import Profile from "../Profile/profile";
import drList from "../Drs/doctors.json"
// define our Hello component
class Hello extends Component {
  // what should the component render
  render() {
    // Make sure to return some UI
    return <h1>Hello World!</h1>;
  }
}

export default Hello;