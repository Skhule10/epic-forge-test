sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/ui/model//JSONModel"
], function (Controller, JSONModel) {
    "use strict";

    return Controller.extend("copilot.controller.App", {
        onInit: function () {
            var oModel = new JSONModel({
                messages: []
            });
            this.getView().setModel(oModel);
        },

        onSend: function () {
            var oInput = this.byId("userInput");
            var sText = oInput.getValue();
            if (sText) {
                var oModel = this.getView().getModel();
                var aMessages = oModel.getProperty("/messages");
                aMessages.push({
                    text: sText,
                    timestamp: new Date().toLocaleString()
                });
                oModel.setProperty("/messages", aMessages);
                oInput.setValue("");
            }
        }
    });
});