import React, { Component } from 'react';



class BaseView extends Component {
    state = {
        value: undefined,
    };

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="LabelView">

            </div>
        );
    }
}
