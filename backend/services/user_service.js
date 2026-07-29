// Import the registerUser function from the correct module
const { registerUser } = require('./user_registration');

// Rest of the file remains the same
// rest of the code remains the same, assuming the function is used correctly afterwards
// Add a null check to ensure registerUser is a function before calling it
if (typeof registerUser === 'function') {
  // Call the registerUser function
  registerUser();
} else {
  // Handle the case where registerUser is not a function
  throw new Error('registerUser is not a function');
}
