import React from 'react';
import { Select } from 'antd';
import '../Snippet.css';
import BaseView from './BaseView';

const Option = Select.Option;

export default class SelectView extends BaseView {

    onChange = (e) => {
        console.log(e);
        const newValue = this.state.value;
        newValue.selected = e;
        this.setState({ value: newValue });
    };

    renderContent() {
        return (
            <div className="SelectView">
                <Select
                    defaultValue={this.state.value.selected || this.state.value.placeholder}
                    onChange={e => this.onChange.bind(this)(e)}>
                    {this.state.value.options.map((option, pos) => <Option key={`option${pos + 1}`} value={pos}>{option}</Option>)}
                </Select>
            </div>
        );
    }
}
