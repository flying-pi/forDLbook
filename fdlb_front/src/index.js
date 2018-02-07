import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import App from './home/App';
import Snippet from './snippet/Snippet';
import './index.css';


ReactDOM.render(
    <Router>
        <div>
            <Route exact path="/" component={App} />
            <Route exact path="/snippet" component={Snippet} />
        </div>
    </Router>,
    document.getElementById('root'),
);
