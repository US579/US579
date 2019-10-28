import React, { Component } from 'react'

export class table extends Component {
    render() {
        return (
            <div style={{ float: "left" ,padding:"20px"}} class="container">
                   
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Three Do</th>
                                <th>Three Don't</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                            <td>Do use try/finally blocks to handle potential exception</td>
                            <td>Don't use an exception when if statement can be used to check an error</td>
                              
                            </tr>
                            <tr>
                            <td>Do release intermediate results and resources when throwing an exception</td>
                            <td>Don't put an empty catch block to swallow an exception</td>
                               
                            </tr>
                            <tr>
                            <td>Do return specific code for specific situation instead of exception</td>
                            <td>Don't catch exception instead of only catch specific exception</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
        )
    }
}

export default table
