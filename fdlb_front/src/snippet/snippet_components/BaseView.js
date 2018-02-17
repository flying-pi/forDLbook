import React, { Component } from 'react';


export default class BaseView extends Component {
    state = {
        value: undefined,
    };
    getViewValue = () => this.state.value;

    constructor(props) {
        super(props);
        if (props.wathcer && props.id) {
            props.wathcer.bindViewToID(this, props.id);
        }
    }

    render() {
        return (
            <div className="LabelView" />
        );
    }
}
