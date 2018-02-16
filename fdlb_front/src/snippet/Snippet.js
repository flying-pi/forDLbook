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
    };

    Snippet() {
        $.getJSON(SERVER_URL + this.state.apiUrl)
            .then((results) => {
                const viewStateWatcher = new ViewWatcher(results.layout);
                this.setState({
                    layout: [ComponentsFactory.getComponentByViewInfo(results.layout, results.layout.className)],
                });
                this.setState({ viewStateWatcher });
            });
    }

    componentDidMount() {
        this.Snippet();
    }

    onSubmit() {
        console.log('Snippet submitted');
        React.Children.forEach(this.props.children, (child) => {
            console.log(child);
        });
    }

    render() {
        return (
            <div className="Snippet">
                {this.state.layout}
                <Divider />
                <Button type="primary" onClick={() => this.onSubmit.bind(this)()}>Submit</Button>
            </div>
        );
    }
}

export default Snippet;
