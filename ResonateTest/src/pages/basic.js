import React, { Component } from 'react'
import Table from "../components/table"

export class basic extends Component {
    render() {
        return (
          <div style={{padding:"15px"}}>
            <h1 style={{textAlign:"left", padding:"15px",fontSize:"30px",color:"darkred"}}>Q1: Basics: </h1>
                <h4 style={{ textAlign: "left", fontweight:"bold",fontSize:"20px"}}>1.How important is logging in an application?</h4>
            <h5 style={{textAlign: "left", padding: "15px", fontSize: "20px" }}>Because log is a useful tool to look inside of program when they are running ,
            and provides developer with instruments to monitor , trouble and debug the application.</h5>
                <h4 style={{ textAlign: "left", fontSize: "20px" }}>2.When do you think use of global variables is appropriate? </h4>
                <h5 style={{ textAlign: "left", padding: "15px", fontSize: "20px" }}>When multiple functions need to access the data or write to an object </h5>
                <h4 style={{ textAlign: "left", fontSize: "20px" }}>3.Name 3 DO's and 3 DON'Ts around Exception Handling</h4>
                <Table />
          </div>
        );
    }
}

export default basic
