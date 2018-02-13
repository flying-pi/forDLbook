import React, { Component } from 'react';
import './Snippet.css';
import { SERVER_URL } from '../Const';
import ComponentsFactory from './snippet_components/ComponentsFactory';

const $ = require('jquery');

class Snippet extends Component {
    state = {
        apiUrl: this.props.location.state.apiUrl,
        layout: '',
    };


    Snippet() {
        $.getJSON(SERVER_URL + this.state.apiUrl)
            .then((results) => {
                console.log(results);
                const ComponentView = ComponentsFactory.getComponentByViewInfo(results.layout.className);
                const newLayout = ComponentView ? (React.createElement(ComponentView, results.layout)) : 'blank';
                this.setState({ layout: newLayout });
                console.log(this.state.layout);
            });
    }

    componentDidMount() {
        this.Snippet();
    }

    render() {
        return (
            <div className="Snippet">
                {this.state.layout}
            </div>
        );
    }
}

export default Snippet;
