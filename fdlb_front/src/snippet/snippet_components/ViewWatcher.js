export default class ViewWatcher {
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
            component.wathcer = this; // eslint-disable-line no-param-reassign
        }
    };

    constructor(layoutData) {
        this.addMeToComponent(layoutData);
    }

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
    }

}
