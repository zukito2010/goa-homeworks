import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

import ClickMe from './App.jsx'; 

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ClickMe />
  </StrictMode>
);