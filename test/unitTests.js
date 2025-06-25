
    const cds = require('@sap/cds');
    const { expect } = require('chai');

    describe('DigitalAssistantService Tests', () => {
        let Queries;

        before(async () => {
            const db = await cds.connect.to('db');
            Queries = db.entities('DigitalAssistantService.Queries');
        });

        it('should create a query entry', async () => {
            const queryEntry = {
                ID: cds.utils.uuid(),
                queryText: 'Hello, what is the weather today?',
                responseText: 'The weather today is sunny with a high of 75°F.'
            };
            await INSERT.into(Queries).entries(queryEntry);

            const result = await SELECT.one.from(Queries).where({ ID: queryEntry.ID });
            expect(result).to.exist;
            expect(result.queryText).to.equal(queryEntry.queryText);
            expect(result.responseText).to.equal(queryEntry.responseText);
        });
    });
