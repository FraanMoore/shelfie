
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Books from './pages/Books'
import Home from './pages/Home'
import Movies from './pages/Movies'
import Series from './pages/Series'
import Navbar from './components/ui/Navbar'

const App = () => {
  return (
    <BrowserRouter>
    <Navbar />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/books" element={<Books />} />
      <Route path="/movies" element={<Movies />} />
      <Route path="/series" element={<Series />} />
    </Routes>
    </BrowserRouter>
  )
}

export default App
