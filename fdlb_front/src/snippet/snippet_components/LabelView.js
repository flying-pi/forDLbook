import React from 'react';

import '../Snippet.css';
import BaseView from './BaseView';

export default class LabelView extends BaseView {
    renderContent() {
        return (
            <div className="LabelView">
                <h2>
                    {this.state.value}
                </h2>
            </div>
        );
    }
}
