const handlePrompt = () => {
  const fname = prompt('Enter your first name');
  const lname = prompt('Enter your last name');
  if (fname && lname) {
    alert(`Hello, ${fname} ${lname}!`);
  }
};

function ClickMe() {
  return (
    <>
      <button onClick={handlePrompt}>Click Me</button>
    </>
  );
}

export default ClickMe;
