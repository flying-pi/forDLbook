/* eslint no-param-reassign: "error" */
import React, { Component } from 'react';


export default class BaseView extends Component {
    state = {
        value: undefined,
    };
    getViewValue = () => this.state.value;
    sendEvent = (eventName) => {
        if (this.state.viewID) {
            this.state.bridge.sendEvent(eventName, this.state.viewID);
        }
    };

    constructor(props) {
        super(props);
        this.state.bridge = props.bridge;
        this.update(props, ((newArgs) => {
            this.state = { ...this.state, ...newArgs };
        }));
        if (props.bridge && props.id) {
            props.bridge.bindViewToID(this, props.id);
        }
    }

    setNewDaya(data) {
        this.update(data, (newState) => {
            this.setState(newState);
        });
    }

    update(props, stateUpdater) {
        stateUpdater({ bridge: props.bridge });
        stateUpdater({ value: props.value });
        stateUpdater({ editable: props.editable });
        stateUpdater({ events: props.events || [] });
        stateUpdater({ visible: props.visible === undefined ? true : props.visible });
        if (props.id) {
            stateUpdater({ viewID: props.id });
        }
    }

    renderContent() {
        return (<div />);
    }

    render() {
        return this.state.visible ? this.renderContent() : (<div />);
    }
}
