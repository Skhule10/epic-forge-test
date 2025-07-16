// UserAuthentication.test.js

// Import necessary modules for testing
const request = require('supertest');
const app = require('../UserAuthentication.js');
const assert = require('assert');

describe('User Authentication Feature', function() {
  it('should redirect to OAuth2 provider login on /auth/login', function(done) {
    request(app)
      .get('/auth/login')
      .expect('Location', /oauth2Provider/, done);
  });

  it('should authenticate and redirect home on /auth/callback', function(done) {
    request(app)
      .get('/auth/callback')
      .expect(302)
      .expect('Location', '/', done);
  });

  it('should fail authentication and redirect to login on error', function(done) {
    request(app)
      .get('/auth/callback?error=true')
      .expect(302)
      .expect('Location', '/login', done);
  });
});