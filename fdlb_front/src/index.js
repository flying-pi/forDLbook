import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import App from './App';
import './index.css';

class MyTest extends Component {
    state = {
        loading: false,
    };

    render() {
        return (<h1>This is teeees</h1>);
    }
}

ReactDOM.render(
    <Router>
        <div>
            <Route exact path="/" component={App} />
            <Route path="/test" component={MyTest} />
        </div>
    </Router>,
    document.getElementById('root'),
);
