import React, { Component } from 'react';
import { Col, Input, Row } from 'antd';

import '../Snippet.css';

export default class ScalarView extends Component {
    state = {
        value: 0,
    };

    constructor(props) {
        super(props);
        this.state.value = props.value;
    }

    render() {
        return (
            <div className="LabelView">
                <h2>

                    <Row key="SizeChanger" gutter={16}>
                        <Col key="row_count" span={3}>
                            <Input
                                type="flex"
                                defaultValue={this.state.value}
                                onChange={e => this.setState({
                                    value: e.target.value,
                                })} />
                        </Col>
                    </Row>
                </h2>
            </div>
        );
    }
}
