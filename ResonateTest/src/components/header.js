import React, { Component } from 'react'

export class header extends Component {
    render() {
        return (
                <div className="header">
                    <a href="/">Basics</a>
                    <a href="/q2">Level 100</a>
                    <a href="/q3">Level 200</a>
                    <a href="/q4">Real World Problem</a>
                </div>
        )
    }
}

export default header
