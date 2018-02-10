import React, {Component} from 'react';
import './Snippet.css';
import {SERVER_URL} from '../Const';

const $ = require('jquery');

export class MatrixView extends Component {
    state = {
        apiUrl: this.props.location.state.apiUrl,
        layout: {},
    };

    viewInfo = {};

    render() {
        return (
            <div className="MatrixView">
                blank
            </div>
        );
    }
}

