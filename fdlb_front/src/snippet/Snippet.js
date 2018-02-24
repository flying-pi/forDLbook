import React, { Component } from 'react';
import { Divider } from 'antd';
import './Snippet.css';
import { SERVER_URL } from '../Const';
import ComponentsFactory from './snippet_components/ComponentsFactory';
import ViewBridge from './snippet_components/ViewBridge';


const $ = require('jquery');

class Snippet extends Component {
    state = {
        apiUrl: this.props.location.state.apiUrl,
        layout: '',
    };

    Snippet() {
        const url = SERVER_URL + this.state.apiUrl;
        $.getJSON(url)
            .then((results) => {
                const viewBridge = new ViewBridge(results, url);
                const params = { ...results, bridge: viewBridge };
                this.setState({
                    layout: [ComponentsFactory.getComponentByViewInfo(params, results.className)],
                });
                this.setState({ watcher: viewBridge });
            });
    }

    componentDidMount() {
        this.Snippet();
    }

    render() {
        return (
            <div className="Snippet">
                {this.state.layout}
                <Divider />
            </div>
        );
    }
}

export default Snippet;
