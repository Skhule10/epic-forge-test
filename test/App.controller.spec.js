sap.ui.define([
    "copilot/controller/App"
], function (AppController) {
    "use strict";

    QUnit.module("App Controller Tests", {
        beforeEach: function () {
            this.oAppController = new AppController();
        },
        afterEach: function () {
            this.oAppController.destroy();
        }
    });

    QUnit.test("Test onPress Event", function (assert) {
        // Arrange
        var bButtonPressed = false;
        var fnOriginalAlert = window.alert;
        window.alert = function() {
            bButtonPressed = true;
        };

        // Act
        this.oAppController.onPress();

        // Assert
        assert.ok(bButtonPressed, "Button press event was handled correctly.");

        // Cleanup
        window.alert = fnOriginalAlert;
    });
});