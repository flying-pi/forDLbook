import React from 'react';
import { Button } from 'antd';

import '../Snippet.css';
import BaseView from './BaseView';

export default class ButtonView extends BaseView {

    EVENT_NAME = 'submit';
    onClick = () => {
        if (this.state.events.indexOf(this.EVENT_NAME) < 0) {
            return;
        }
        this.sendEvent(this.EVENT_NAME);
    };

    constructor(props) {
        super(props);
        this.state.events = props.events;
        this.state.editable = props.editable;
    }

    render() {
        return (
            <div className="LabelView">
                <Button onClick={() => this.onClick.bind(this)()}>{this.state.value}</Button>
            </div>
        );
    }
}
