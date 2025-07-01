// File: copilot/src/App.controller.js
// Controller logic for SAP UI5/Fiori frontend

sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/ui/model/JSONModel"
], function (Controller, JSONModel) {
    "use strict";

    return Controller.extend("copilot.src.App.controller", {
        onInit: function () {
            var oModel = new JSONModel({
                response: ""
            });
            this.getView().setModel(oModel, "responseModel");
        },

        onSubmitQuery: function () {
            var sQuery = this.byId("userQueryInput").getValue();
            var oModel = this.getView().getModel("responseModel");

            // Call backend service to process query
            $.ajax({
                url: "/app/processQuery",
                method: "POST",
                data: JSON.stringify({ query: sQuery }),
                contentType: "application/", // Corrected contentType
                success: function (data) {
                    oModel.setProperty("/response", data);
                },
                error: function () {
                    oModel.setProperty("/response", "Error processing query.");
                }
            });
        }
    });
});
