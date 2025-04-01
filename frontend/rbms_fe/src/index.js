import React from 'react';
import ReactDOM from 'react-dom/client';
import { Navbar } from './components/Layout';
import { Footer } from './components/Layout';
import Home from './pages/Home';  
import { Notfound } from './pages/Notfound';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Admin } from './pages/Admin';
import { Profile } from './pages/Profile';
import { Logout } from './pages/Logout';
import InsertMortgage  from './pages/InsertMortgage';
import UpdateMortgage  from './pages/UpdateMortgage';

function App(){
  return (
    <>
    <BrowserRouter>
    <Navbar/>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/get-mortgages' element={<Home/>} />
      <Route path='/insert-mortgage' element={<InsertMortgage/>} />
      <Route path="/update-mortgage/:id" element={<UpdateMortgage  />} />
      <Route path='/admin' element={<Admin/>} />
      <Route path='/profile' element={<Profile/>} />
      <Route path='/logout' element={<Logout/>} />
      <Route path='*' element={<Notfound/>} />
    </Routes>
    <Footer/>
    </BrowserRouter>
    </>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

