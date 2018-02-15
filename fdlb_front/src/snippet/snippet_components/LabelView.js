import React, { Component } from 'react';

import '../Snippet.css';

export default class LabelView extends Component {
    state = {
        layout: '',
    };

    constructor(props) {
        super(props);
        this.state.layout = props.value;
    }

    render() {
        return (
            <div className="LabelView">
                <h2>
                    {this.state.layout}
                </h2>
            </div>
        );
    }
}
