import React from 'react';

import '../Snippet.css';
import BaseView from './BaseView';

export default class LabelView extends BaseView {
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
