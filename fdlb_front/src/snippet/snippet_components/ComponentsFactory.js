import React from 'react';

import MatrixView from './MatrixView';
import SimpleLayout from './SimpleLayout';
import LabelView from './LabelView';
import ScalarView from './ScalarView';
import ButtonView from './ButtonView';
import SelectView from './SelectView';
import UploadFile from './UploadFile';
import Image from './Image';

export default class ComponentsFactory {
    // TODO return some stub in default case
    static getComponentClassByViewInfo(viewInfo) {
        switch (viewInfo.className) {
            case 'core.snippets_view.simple_view.MatrixView':
                return React.createFactory(MatrixView);

            case 'core.snippets_view.simple_view.LabelView':
                return React.createFactory(LabelView);

            case 'core.snippets_view.simple_view.ButtonView':
                return React.createFactory(ButtonView);

            case 'core.snippets_view.simple_view.ScalarView':
                return React.createFactory(ScalarView);

            case 'core.snippets_view.simple_view.SelectView':
                return React.createFactory(SelectView);

            case 'core.snippets_view.simple_view.UploadFile':
                return React.createFactory(UploadFile);

            case 'core.base_components.SimpleLayout':
                return React.createFactory(SimpleLayout);

            case 'core.snippets_view.simple_view.Image':
                return React.createFactory(Image);

            default:
                return null;
        }
    }

    static getComponentByViewInfo(viewInfo, key = '') {
        const componentClass = ComponentsFactory.getComponentClassByViewInfo(viewInfo);
        return componentClass ? (React.createElement(componentClass, { ...viewInfo, key })) : 'blank';
    }
}

