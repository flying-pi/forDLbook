import React from 'react';

import MatrixView from './MatrixView';
import SimpleLayout from './SimpleLayout';
import LabelView from './LabelView';
import ScalarView from './ScalarView';
import ButtonView from './ButtonView';

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

            case 'core.base_components.SimpleLayout':
                return React.createFactory(SimpleLayout);

            default:
                return null;
        }
    }

    static getComponentByViewInfo(viewInfo, key = '') {
        const componentClass = ComponentsFactory.getComponentClassByViewInfo(viewInfo);
        return componentClass ? (React.createElement(componentClass, { ...viewInfo, key })) : 'blank';
    }
}

