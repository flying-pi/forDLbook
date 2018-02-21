import React from 'react';
import '../Snippet.css';
import ComponentsFactory from './ComponentsFactory';
import BaseView from './BaseView';


export default class SimpleLayout extends BaseView {
    update(props, stateUpdater) {
        super.update(props, stateUpdater);
        console.log('Simple layout constructor');
        let position = 0;
        stateUpdater({
            layout: props.childrenView.map(entry =>
                ComponentsFactory.getComponentByViewInfo(entry, `pos${position += 1}`)),
        });
    }

    renderContent() {
        return (
            <div className="SimpleLayout">
                {this.state.layout}
            </div>
        );
    }
}
