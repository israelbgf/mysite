import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { Router, Route, browserHistory } from 'react-router'

const About = () => <p>I'am a nice guy.</p>
const Blog = () => <p>Blogging about.</p>
const NoMatch = () => <p>404. :(</p>

ReactDOM.render((
    <Router history={browserHistory}>
        <Route path="/" component={App}>
            <Route path="about" component={About}/>
            <Route path="blog" component={Blog}/>
            <Route path="*" component={NoMatch}/>
        </Route>
    </Router>
), document.getElementById('root'))
