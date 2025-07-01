// Unit tests for MyService
const cds = require('@sap/cds');

cds.test(__dirname + '/..', ({ expect }) => {
    describe('MyService', () => {
        it('should return entity data', async () => {
            const { MyService } = await cds.connect.to('MyService');
            const result = await MyService.read('MyEntity');
            expect(result).to.be.an('array');
        });
    });
});