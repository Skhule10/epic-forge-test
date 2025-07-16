// UserAuthentication.js

// Import necessary modules and services
const xsenv = require('@sap/xsenv');
const passport = require('passport');
const OAuth2Strategy = require('passport-oauth2').Strategy;
const express = require('express');
const app = express();

// Configure environment variables
xsenv.loadEnv();

// Set up the OAuth2 strategy
passport.use(new OAuth2Strategy({
  authorizationURL: process.env.AUTHORIZATION_URL,
  tokenURL: process.env.TOKEN_URL,
  clientID: process.env.CLIENT_ID,
  clientSecret: process.env.CLIENT_SECRET,
  callbackURL: process.env.CALLBACK_URL
}, function(accessToken, refreshToken, profile, done) {
  // Verify user profile and tokens
  User.findOrCreate({ oauthId: profile.id }, function (err, user) {
    return done(err, user);
  });
}));

// Initialize passport and session handling
app.use(passport.initialize());
app.use(passport.session());

// Define authentication routes
app.get('/auth/login', passport.authenticate('oauth2'));
app.get('/auth/callback', passport.authenticate('oauth2', { failureRedirect: '/login' }),
  function(req, res) {
    // Successful authentication, redirect home.
    res.redirect('/');
  });

// Export the app module
module.exports = app;
