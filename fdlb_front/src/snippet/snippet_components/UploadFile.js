import React from 'react';
import { Upload } from 'antd';


import '../Snippet.css';
import BaseView from './BaseView';

export default class UploadFile extends BaseView {

    handleChange = (info) => {
        if (info.file.status !== 'done') {
            return;
        }
        console.log(info);
        const reader = new FileReader();
        reader.addEventListener('load', () => {
            console.log('Info:: ');
            console.log(reader.result);
            const base64 = btoa(String.fromCharCode(...new Uint8Array(reader.result)));
            console.log(base64);
        });
        reader.readAsArrayBuffer(info.file.originFileObj);
    }

    renderContent() {
        return (
            <div className="LabelView">
                <Upload
                    showUploadList={false}
                    action="//jsonplaceholder.typicode.com/posts/"
                    onChange={this.handleChange}>
                    Upload
                </Upload>
            </div>
        );
    }
}
