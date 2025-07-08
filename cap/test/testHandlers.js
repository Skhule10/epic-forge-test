const cds = require('@sap/cds');
const { expect } = require('chai');

describe('ChatService Handlers', () => {
  it('should send a message successfully', async () => {
    const ChatService = await cds.connect.to('ChatService');
    const result = await ChatService.sendMessage({ text: 'Hello', author: 'John Doe' });
    expect(result.message).to.equal('Message sent successfully!');
  });

  // Additional tests can be added here
});