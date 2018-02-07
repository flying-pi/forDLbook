import React, { Component } from 'react';
import { Card, Col, Row } from 'antd';

import { Link } from 'react-router-dom';
import './App.css';

const Const = require('../Const');
const $ = require('jquery');

class App extends Component {
    state = {
        loading: false,
        snippets: [],
        snippetsList: '',
    };

    App() {
        $.getJSON(Const.SERVER_URL)
            .then((results) => {
                const snippets = results.snippets;
                const row = [];
                const columnSpan = 24 / Const.MAIN_GRID_COUTN;
                for (let r = 0; r < snippets.length; r += Const.MAIN_GRID_COUTN) {
                    const col = [];
                    for (let c = 0; c < Const.MAIN_GRID_COUTN && r + c < snippets.length; c += 1) {
                        const itemPos = r + c;
                        const snippet = snippets[itemPos];
                        col.push(
                            <Col span={columnSpan} key={itemPos}>
                                <Link to={{ pathname: '/snippet', state: { apiUrl: snippet.url } }} >
                                    <div className="Main-page-card">
                                        <Card title={snippet.name}>
                                            {snippet.description}
                                        </Card>
                                    </div>
                                </Link>
                            </Col>,
                        );
                    }
                    row.push(<Row key={r}>{col} </Row>);
                }
                this.setState({ snippets: results.snippets });
                this.setState({ snippetsList: row });
            });
    }

    componentDidMount() {
        this.App();
    }

    render() {
        return (
            <div className="App">
                {this.state.snippetsList}
            </div>
        );
    }
}

export default App;
