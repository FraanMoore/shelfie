
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<div>Home</div>} />
      <Route path="/books" element={<div>Books</div>} />
      <Route path="/movies" element={<div>Movies</div>} />
      <Route path="/series" element={<div>Series</div>} />
    </Routes>
    </BrowserRouter>
  )
}

export default App
