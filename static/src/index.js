import React from 'react';
import ReactDOM from 'react-dom';
import OTP from './components/OTP';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<OTP />, document.getElementById('root'));
registerServiceWorker();
