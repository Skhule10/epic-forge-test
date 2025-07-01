
const cds = require('@sap/cds');
const { xsuaa } = require('./xsuaa-config');

// Initialize the CDS service
cds.on('bootstrap', app => {
  app.use((req, res, next) => {
    // Security middlewares can be added here
    next();
  });
});

cds.listen();
