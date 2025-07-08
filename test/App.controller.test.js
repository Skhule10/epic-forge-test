sap.ui.define([
    "copilot/controller/App.controller"
], function (AppController) {
    "use strict";

    QUnit.module("App Controller");

    QUnit.test("I should test the App controller initialization", function (assert) {
        var oAppController = new AppController();
        oAppController.onInit();
        assert.ok(oAppController);
    });

    QUnit.test("Test the onSend function", function (assert) {
        var oAppController = new AppController();
        oAppController.onInit();

        oAppController.byId = function (id) {
            return {
                getValue: function () {
                    return "Test message";
                },
                setValue: function () {}
            };
        };

        var oModel = oAppController.getView().getModel();
        assert.equal(oModel.getProperty("/messages").length, 0, "Initial messages array is empty");

        oAppController.onSend();

        assert.equal(oModel.getProperty("/messages").length, 1, "A message is added");
        assert.equal(oModel.getProperty("/messages")[0].text, "Test message", "Message text matches");
    });
});