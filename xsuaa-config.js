
module.exports = {
  authentication: {
    xsuaa: {
      clientId: process.env.XSUAA_CLIENT_ID,
      clientSecret: process.env.XSUAA_CLIENT_SECRET,
      url: process.env.XSUAA_URL
    }
  },
  authorization: {
    scopes: ['read', 'write']
  }
};
