import React from 'react';

function Parent({ children, onMouseEnter }) {
  return (
    <button onMouseEnter={onMouseEnter}>
      {children}
    </button>
  );
}

export default Parent;