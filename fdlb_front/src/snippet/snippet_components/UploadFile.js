import React from 'react';
import { Upload } from 'antd';


import '../Snippet.css';
import BaseView from './BaseView';

export default class UploadFile extends BaseView {

    handleChange = (file) => {
        console.log(file);
        const reader = new FileReader();
        reader.addEventListener('load', () => {
            this.setState({ value: reader.result });
            console.log('file uploaded!');
        });
        reader.readAsDataURL(file);
        return false;
    };

    renderContent() {
        return (
            <div className="LabelView">
                <Upload
                    showUploadList={false}
                    beforeUpload={this.handleChange}>
                    Upload
                </Upload>
            </div>
        );
    }
}
