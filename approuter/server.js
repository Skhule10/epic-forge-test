const approuter = require('@sap/approuter');
const app = approuter();

app.beforeRequestHandler.use((req, res, next) => {
    // Custom logic before request
    console.log('Request URL:', req.url);
    next();
});

module.exports = app;