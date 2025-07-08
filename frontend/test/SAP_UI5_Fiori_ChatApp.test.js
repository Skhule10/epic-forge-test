/* Unit Test for SAP UI5/Fiori Frontend Code */

sap.ui.require([
  'sap/ui/test/opaQunit',
  'sap/ui/test/Opa5',
  'sap/ui/demo/walkthrough/test/integration/pages/App'
], function (opaTest, Opa5, App) {
  'use strict';

  Opa5.extendConfig({
    arrangements: new App(),
    viewNamespace: 'sap.ui.demo.walkthrough.view.'
  });

  opaTest('Should send a message successfully', function (Given, When, Then) {
    // Initialization
    Given.iStartMyApp();

    // Actions
    When.onTheAppPage.iPressTheSendButton();

    // Assertions
    Then.onTheAppPage.iShouldSeeTheMessageToast();

    // Cleanup
    Then.iTeardownMyApp();
  });

});

