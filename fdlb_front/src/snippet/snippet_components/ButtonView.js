import React from 'react';
import { Button } from 'antd';
import { Link } from 'react-router-dom';

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
        let button = null;
        if (this.state.value.redirect_to) {
            // conditional for /
            button = (
                <Link to={{ pathname: '/snippet', state: { apiUrl: this.state.value.redirect_to } }} replace>
                    <Button>
                        {this.state.value.text}
                    </Button>
                </Link>);
        } else {
            button = (<Button onClick={() => this.onClick.bind(this)()}>
                {this.state.value.text}
            </Button>);
        }
        return (
            <div className="ButtonView">
                {button}
            </div>
        );
    }
}
