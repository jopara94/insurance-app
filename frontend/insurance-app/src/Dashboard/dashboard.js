import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

export default class Dashboard extends Component {
    constructor() {
        super();
        this.state = {
            listOfDoctors: []
        };
    }

    componentDidMount() {
        axios.get()
        .then(res => {
            console.log(res.data);
            this.setState({ listOfDoctors: res.data });
        })
        .catch(error => {
            console.log(error);
        })
    }

    render() {
        console.log("logged");
        let 
    }
}