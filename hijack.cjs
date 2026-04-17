const os = require('os');
const original = os.networkInterfaces;
os.networkInterfaces = () => {
  try {
    return original();
  } catch (e) {
    return { lo: [{ address: '127.0.0.1', family: 'IPv4', internal: true }] };
  }
};
