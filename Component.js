
sap.ui.define([
    "sap/ui/core/UIComponent",
    "sap/ui/model//JSONModel"
], function (UIComponent, JSONModel) {
    "use strict";

    return UIComponent.extend("sap.cap.digitalassistant.Component", {
        metadata: {
            manifest: ""
        },

        init: function () {
            UIComponent.prototype.init.apply(this, arguments);

            // Set up models
            var oDataModel = new JSONModel({
                userQuery: "",
                assistantResponse: ""
            });
            this.setModel(oDataModel);
        }
    });
});
