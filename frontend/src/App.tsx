import { BrowserRouter,Routes,Route } from "react-router-dom";
import { Home } from "./Pages/Home";
import { Login } from './Pages/Login';
import { Signup } from './Pages/Signup';

export default function App(){
   return (
    <div>
         <BrowserRouter>
         <Routes>
            <Route path="/" element={<Home/>}></Route>
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
         </Routes>
         </BrowserRouter>
      </div>
   )
}
