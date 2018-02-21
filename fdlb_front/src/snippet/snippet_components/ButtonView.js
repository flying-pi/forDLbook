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

    renderContent() {
        return (
            <div className="LabelView">
                <Button onClick={() => this.onClick.bind(this)()}>{this.state.value}</Button>
            </div>
        );
    }
}
