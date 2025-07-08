// SAPUI5/Fiori Frontend Application Code
sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/m/MessageToast"
], function (Controller, MessageToast) {
    "use strict";

    return Controller.extend("my.namespace.controller.Main", {
        onInit: function () {
            // Initialization code
            console.log("SAP UI5 Application Initialized");
        },

        onPress: function () {
            // Sample event handler
            MessageToast.show("Button Pressed");
        }
    });
});
