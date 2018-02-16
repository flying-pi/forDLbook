import React, { Component } from 'react';
import '../Snippet.css';
import ComponentsFactory from './ComponentsFactory';


export default class SimpleLayout extends Component {
    state = {
        layout: '',
    };


    constructor(props) {
        super(props);
        console.log('Simple layout constructor');
        let position = 0;
        this.state.layout = props.childrenView.map(entry =>
            ComponentsFactory.getComponentByViewInfo(entry, `pos${position += 1}`));
    }

    render() {
        return (
            <div className="SimpleLayout">
                {this.state.layout}
            </div>
        );
    }
}
