sap.ui.define([
    "sap/ui/core/mvc/Controller"
], function (Controller) {
    "use strict";

    return Controller.extend("copilot.controller.App", {
        onPress: function () {
            alert("Button pressed!");
        }
    });
});