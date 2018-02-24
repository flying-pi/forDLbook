import React from 'react';
import { Col, Input, Row } from 'antd';

import '../Snippet.css';
import BaseView from './BaseView';

export default class ScalarView extends BaseView {

    renderContent() {
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
