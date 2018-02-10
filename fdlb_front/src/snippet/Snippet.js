import React, { Component } from 'react';
import './Snippet.css';
import { SERVER_URL } from '../Const';

const $ = require('jquery');

class Snippet extends Component {
    state = {
        apiUrl: this.props.location.state.apiUrl,
        layout: {},
    };


    Snippet() {
        $.getJSON(SERVER_URL + this.state.apiUrl)
            .then((results) => {
                this.state.layout = results;
                console.log(results);
            });
    }

    componentDidMount() {
        this.Snippet();
    }

    render() {
        return (
            <div className="Snippet">
                blank
            </div>
        );
    }
}

export default Snippet;
