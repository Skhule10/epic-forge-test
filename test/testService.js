const cds = require('@sap/cds');
const { expect } = require('chai');

describe('CatalogService', () => {
    it('should project Books entity correctly', async () => {
        const srv = await cds.connect.to('CatalogService');
        const { Books } = srv.entities;
        expect(Books).to.exist;
    });

    it('should have a Books entity with correct attributes', async () => {
        const srv = await cds.connect.to('CatalogService');
        const { Books } = srv.entities;
        expect(Books.elements).to.have.property('ID');
        expect(Books.elements).to.have.property('title');
        expect(Books.elements).to.have.property('author');
    });
});