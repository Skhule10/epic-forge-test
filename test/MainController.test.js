
const sinon = require('sinon');
const assert = require('assert');
const MainController = require('../controller/Main.controller');

describe('Main Controller', function() {
    let controller, oModel;

    beforeEach(function() {
        controller = new MainController();
        oModel = new sap.ui.model..JSONModel({
            userQuery: "",
            assistantResponse: ""
        });
        controller.setModel(oModel);
    });

    it('should process user query and generate response', function() {
        oModel.setProperty("/userQuery", "Test query");
        controller.onUserQuerySubmit();
        const response = oModel.getProperty("/assistantResponse");
        assert.strictEqual(response, "This is a response to your query: Test query");
    });
});
