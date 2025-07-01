
    // File: copilot/test/App.controller.spec.js
    // Unit Tests for SAP UI5/Fiori frontend

    const { expect } = require('chai');
    const sinon = require('sinon');
    const AppController = require('../src/App.controller');

    describe('App.controller', function() {
        let controller;

        beforeEach(function() {
            controller = new AppController();
        });

        it('should initialize the response model', function() {
            const initSpy = sinon.spy(controller, 'onInit');
            controller.onInit();
            expect(initSpy.calledOnce).to.be.true;
            const model = controller.getView().getModel('responseModel');
            expect(model.getProperty('/response')).to.equal('');
        });

        it('should process query and update response model', function(done) {
            const ajaxStub = sinon.stub($, 'ajax').callsFake(function(options) {
                options.success('Mock response');
            });

            controller.onSubmitQuery();
            setTimeout(() => {
                const model = controller.getView().getModel('responseModel');
                expect(model.getProperty('/response')).to.equal('Mock response');
                ajaxStub.restore();
                done();
            }, 100);
        });

        it('should handle errors during query processing', function(done) {
            const ajaxStub = sinon.stub($, 'ajax').callsFake(function(options) {
                options.error();
            });

            controller.onSubmitQuery();
            setTimeout(() => {
                const model = controller.getView().getModel('responseModel');
                expect(model.getProperty('/response')).to.equal('Error processing query.');
                ajaxStub.restore();
                done();
            }, 100);
        });
    });

    