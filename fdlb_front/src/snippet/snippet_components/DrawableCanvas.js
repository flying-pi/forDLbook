import React from 'react';
import ReactPaint from 'react-paint';

import '../Snippet.css';
import BaseView from './BaseView';


export default class DrawableCanvas extends BaseView {

    update(props, stateUpdater) {
        console.log('boorr');
        super.update(props, stateUpdater);

        stateUpdater({ imageProps: {
            style: {
                background: '#ff7979',
                    /* Arbitrary css styles */
            },
            brushCol: '#000000',
            lineWidth: 20,
            className: 'react-paint',
            height: 500,
            width: 500,
            onDraw: e => this.setState({ value: e.currentTarget.toDataURL() }),
        } });
    }

    renderContent() {
        return (
            <div className="DrawableCanvas">
                <ReactPaint {...this.state.imageProps} />
            </div>
        );
    }
}
