sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/m/MessageToast",
    "sap/ui/model//JSONModel"
], function (Controller, MessageToast, JSONModel) {
    "use strict";

    return Controller.extend("copilot.controller.App", {
        onInit: function () {
            var oData = {
                recipient: {
                    name: "World"
                }
            };
            var oModel = new JSONModel(oData);
            this.getView().setModel(oModel);
        },

        onPress: function () {
            var oBundle = this.getView().getModel("i18n").getResourceBundle();
            var sRecipient = this.getView().getModel().getProperty("/recipient/name");
            var sMsg = oBundle.getText("helloMsg", [sRecipient]);
            MessageToast.show(sMsg);
        },

        onAfterRendering: function() {
            // Implement responsiveness
            var oView = this.getView();
            oView.attachBrowserEvent("resize", function() {
                var width = oView.getDomRef().clientWidth;
                if (width < 600) {
                    // Adjust layout or styles for small screens
                }
            });
        }
    });
});