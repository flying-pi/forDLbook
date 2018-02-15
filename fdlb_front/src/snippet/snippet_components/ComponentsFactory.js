import React from 'react';

import MatrixView from './MatrixView';
import SimpleLayout from './SimpleLayout';
import LabelView from './LabelView';

export default class ComponentsFactory {
    // TODO return some stub in default case
    static getComponentByViewInfo(className) {
        switch (className) {
            case 'core.snippets_view.simple_view.MatrixView':
                return React.createFactory(MatrixView);
            case 'core.snippets_view.simple_view.LabelView':
                return React.createFactory(LabelView);
            case 'core.base_components.SimpleLayout':
                return React.createFactory(SimpleLayout);
            default:
                return null;
        }
    }
}

