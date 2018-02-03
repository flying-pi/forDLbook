import React, { Component } from 'react';
import { Row, Col, Card } from 'antd';

import { Link } from 'react-router-dom';
import './App.css';

const Const = require('./Const');
const $ = require('jquery');

class App extends Component {
    state = {
        loading: false,
        snippets: [],
        snippetsList: '',
    };

    onCardClick = function (content) {
        console.log(content);
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
                                <div className="Main-page-card" onClick={() => this.onCardClick(snippet)}>
                                    <Card title={snippet.name}>
                                        {snippet.description}
                                    </Card>
                                </div>
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
                <Link to="/test"><button>Test</button></Link>
                {this.state.snippetsList}
            </div>
        );
    }
}

export default App;
