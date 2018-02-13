import React, { Component } from 'react';
import '../Snippet.css';

export default class MatrixView extends Component {
    state = {
        layout: '',
    };

    constructor(props) {
        super(props);
        this.state.layout = 'I am matrix!)';
    }

    render() {
        return (
            <div>
                {this.state.layout}
            </div>
        );
    }
}
