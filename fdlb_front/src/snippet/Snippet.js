import React, { Component } from 'react';
import { Button, Divider } from 'antd';
import './Snippet.css';
import { SERVER_URL } from '../Const';
import ComponentsFactory from './snippet_components/ComponentsFactory';
import ViewWatcher from './snippet_components/ViewWatcher';


const $ = require('jquery');

class Snippet extends Component {
    state = {
        apiUrl: this.props.location.state.apiUrl,
        layout: '',
        responseLayout: '',
    };

    Snippet() {
        $.getJSON(SERVER_URL + this.state.apiUrl)
            .then((results) => {
                const viewStateWatcher = new ViewWatcher(results.layout);
                this.setState({
                    layout: [ComponentsFactory.getComponentByViewInfo(results.layout, results.layout.className)],
                });
                this.setState({ watcher: viewStateWatcher });
            });
    }

    componentDidMount() {
        this.Snippet();
    }

    onSubmit() {
        $.ajax({
            url: SERVER_URL + this.state.apiUrl,
            type: 'post',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            success: (data) => {
                const responseLayout = data.responseLayout;
                this.setState({
                    responseLayout: [ComponentsFactory.getComponentByViewInfo(responseLayout, 'response')],
                });
            },
            error: (error) => {
                console.log(error);
            },
            data: JSON.stringify({ state: this.state.watcher.getViewValues() }),
        });
    }

    render() {
        return (
            <div className="Snippet">
                {this.state.layout}
                <Divider />
                <Button type="primary" onClick={() => this.onSubmit.bind(this)()}>Submit</Button>
                <Divider />
                <h2>RESULT ::</h2>
                <Divider />
                {this.state.responseLayout}
            </div>
        );
    }
}

export default Snippet;
