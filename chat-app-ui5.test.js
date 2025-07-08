// Unit tests for SAP UI5/Fiori Chat Application UI
const { render } = require('@testing-library/sap-ui5');

// Test UI rendering
describe('Chat Application UI Rendering', () => {
  it('should render chat list and input correctly', async () => {
    const { getByPlaceholderText, getByText } = await render('<mvc:View xmlns:mvc="sap.ui.core.mvc" xmlns="sap.m" controllerName="copilot.ui.ChatAppController">...');

    // Check if input for message is rendered
    const messageInput = getByPlaceholderText('Type your message...');
    expect(messageInput).toBeInTheDocument();

    // Check if send button is rendered
    const sendButton = getByText('Send');
    expect(sendButton).toBeInTheDocument();
  });

  it('should handle sending messages', async () => {
    const { getByPlaceholderText, getByText } = await render('<mvc:View xmlns:mvc="sap.ui.core.mvc" xmlns="sap.m" controllerName="copilot.ui.ChatAppController">...');

    const messageInput = getByPlaceholderText('Type your message...');
    const sendButton = getByText('Send');

    // Simulate user typing and sending a message
    await userEvent.type(messageInput, 'Hello World');
    await userEvent.click(sendButton);

    // Check if message appears in chat list
    const chatItem = getByText('Hello World');
    expect(chatItem).toBeInTheDocument();
  });
});
