import React from 'react';
import { Upload } from 'antd';
import '../Snippet.css';
import BaseView from './BaseView';

const $ = require('jquery');


const Const = require('../../Const');

export default class UploadFile extends BaseView {

    handleChange = (file) => {
        const data = new FormData();
        data.append('file', file, file.name);
        data.append('test', 'simple string');
        $.ajax({
            url: Const.FILE_UPLOAD_URL,
            type: 'POST',
            dataType: false,
            contentType: false,
            processData: false,
            cache: false,
            success: ((response) => {
                this.setState({ value: response.fileID });
            }),
            error: (error) => {
                console.log(error);
                // todo show some message!
            },
            data,
        });
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
