import React, { Component } from 'react';
import { Link } from 'react-router'
import './App.css';

class App extends Component {
    render() {
        return (
            <div>
                <div id="menu">
                    <div id="logo">
                        <h1>israelbgf</h1>
                    </div>
                    <ol id="navigation">
                        <li><Link to='/about/' activeClassName="menu-highlight">About</Link></li>
                        <li><Link to='/blog/' activeClassName="menu-highlight">Blog</Link></li>
                    </ol>
                </div>
                <div id="content">
                    {this.props.children}
                </div>
            </div>
        );
    }
}

export default App;
