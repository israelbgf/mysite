import React, { Component } from 'react';
import { Link, IndexLink } from 'react-router'
import './App.css';

class App extends Component {
    render() {
        return (
            <div>
                <div id="menu" style={{float: "left"}}>
                    <div id="logo">
                        <h1>israelbgf</h1>
                    </div>
                    <ol id="navigation">
                        <li><IndexLink to='/' activeClassName="menu-highlight">About</IndexLink></li>
                        <li><Link to='/blog/' activeClassName="menu-highlight">Blog</Link></li>
                    </ol>
                </div>
                <div id="content" style={{float: "left", marginLeft: "10px"}}>
                    {this.props.children}
                </div>
            </div>
        );
    }
}

export default App;
