const $ = require('jquery');

export default class ViewBridge {
    viewByIdMap = {};

    addMeToComponent = (component) => {
        for (const key in component) { // eslint-disable-line no-restricted-syntax
            if (component.hasOwnProperty(key)) { // eslint-disable-line no-prototype-builtins
                const value = component[key];
                if (value instanceof Object) {
                    this.addMeToComponent(value);
                }
            }
        }
        if (component.className) {
            component.bridge = this; // eslint-disable-line no-param-reassign
        }
    };

    sendEvent = (name, callerId) => {
        const eventBody = {
            type: name,
            caller: callerId,
            data: this.getViewValues(),
        };
        $.ajax({
            url: this.url,
            type: 'post',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            success: ((data) => {
                this.addMeToComponent(data);
                const params = { ...data, bridge: this };
                const rootView = this.viewByIdMap[params.id];
                if (rootView) {
                    rootView.setNewDaya(params);
                }
            }),
            error: (error) => {
                console.log(error);
            },
            data: JSON.stringify(eventBody),
        });
        console.log(name + callerId);
    };

    getViewValues = () => {
        const result = {};
        for (const key in this.viewByIdMap) { // eslint-disable-line no-restricted-syntax
            if (this.viewByIdMap.hasOwnProperty(key)) { // eslint-disable-line no-prototype-builtins
                result[key] = this.viewByIdMap[key].getViewValue();
            }
        }
        return result;
    };

    bindViewToID = (view, ID) => {
        this.viewByIdMap[ID] = view;
    };

    constructor(layoutData, url) {
        this.addMeToComponent(layoutData);
        this.url = url;
    }

}
