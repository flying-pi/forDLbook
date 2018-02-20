import React from 'react';
import { Button, Card, Col, Input, Row } from 'antd';

import '../Snippet.css';
import './MatrixView.css';
import BaseView from './BaseView';

export default class MatrixView extends BaseView {


    constructor(props) {
        super(props);
        this.state = {
            layout: '',
            m: props.value.length,
            n: props.value[0].length,
            value: props.value,
            editable: props.editable,
            // value: [[11, 12, 13], [21, 22, 23], [31, 32, 33]],
        };
        this.state.layout = this.updateWith(this.state.value);
    }

    onChangeSize() {
        const newMatrix = [];
        for (let i = 0; i < this.state.m; i += 1) {
            const row = [];
            for (let j = 0; j < this.state.n; j += 1) {
                row.push(i < this.state.value.length && j < this.state.value[0].length ? this.state.value[i][j] : 0);
            }
            newMatrix.push(row);
        }
        this.setState({ value: newMatrix });
        this.setState({ layout: this.updateWith(this.state.value) });
    }

    updateWith(value) {
        let r = -1;
        const matrixView = value.map((row) => {
            r += 1;
            const rowNumber = r;
            let c = -1;
            const rowLayout = [...row.map((cell) => {
                c += 1;
                const columnNumber = c;
                let valueRepresentation;
                if (this.state.editable) {
                    valueRepresentation = (<Input
                        defaultValue={cell}
                        onChange={(e) => {
                            const newValue = this.state.value.slice();
                            newValue[rowNumber][columnNumber] = e.target.value;
                            this.setState({ value: newValue });
                        }} />);
                } else {
                    valueRepresentation = <div>{cell}</div>;
                }
                return (<Col key={`column${columnNumber}`}>{valueRepresentation}</Col>);
            })];
            return <Row key={`row${rowNumber}`} type="flex" gutter={8}>{rowLayout} </Row>;
        });
        if (this.state.editable) {
            const matrixSize = (
                <Row key="SizeChanger" gutter={16}>
                    <Col key="row_count" span={3}><Input
                        type="flex"
                        addonBefore="Rows:"
                        defaultValue={this.state.m}
                        onChange={e => this.setState({
                            m: e.target.value,
                        })} /></Col>
                    <Col key="cell_count" span={3}><Input
                        type="flex"
                        addonBefore="Column:"
                        defaultValue={this.state.n}
                        onChange={e => this.setState({
                            n: e.target.value,
                        })} /></Col>
                    <Col key="apply" span={6}><Button
                        type="primary"
                        onClick={() => this.onChangeSize.bind(this)()}>Apply</Button></Col>
                </Row>);
            return [...matrixView, matrixSize];
        }
        return matrixView;
    }

    render() {
        return (
            <div className="MatrixView">
                <Card>
                    {this.state.layout}
                </Card>
            </div>
        );
    }
}
