const cds = require('@sap/cds');

module.exports = cds.service.impl(async function() {
  const { Messages } = this.entities;

  this.on('sendMessage', async req => {
    const { text, author } = req.data;
    const message = {
      ID: cds.utils.uuid(),
      text,
      author,
      timestamp: new Date()
    };
    await cds.run(INSERT.into(Messages).entries(message));
    req.reply({ message: 'Message sent successfully!' });
  });
});