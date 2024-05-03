import Homepage from './pages/Home'
function App() {
  const url = "http://localhost:5005/"
  return (
    <div className="App p-5">
      <Homepage url ={url}></Homepage>
    </div>
  );
}

export default App;
