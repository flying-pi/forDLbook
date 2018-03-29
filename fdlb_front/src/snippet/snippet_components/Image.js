import React from 'react';

import '../Snippet.css';
import BaseView from './BaseView';

const Const = require('../../Const');

export default class Image extends BaseView {
    renderContent() {
        return (
            <div className="ImageView">
                <img src={Const.SERVER_URL + this.state.value} alt="lorem ipsum" />
            </div>
        );
    }
}
