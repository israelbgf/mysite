import 'whatwg-fetch';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import PostForm from './PostForm';
import Blog from './Blog';
import { Router, Route, IndexRoute, browserHistory } from 'react-router'

const About = () => <p>I'am a nice guy.</p>
const NoMatch = () => <p>404. :(</p>

ReactDOM.render((
    <Router history={browserHistory}>
        <Route path="/" component={App}>
            <IndexRoute component={About}/>
            <Route path="blog" component={Blog}/>
            <Route path="blog/post" component={PostForm}/>
        </Route>
        <Route path="*" component={NoMatch}/>
    </Router>
), document.getElementById('root'))
