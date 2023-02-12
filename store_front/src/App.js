import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Login from "./pages/Login";
import MyCart from "./pages/MyCart";
import MyOrders from "./pages/MyOrders";
import OrderDetail from "./pages/OrderDetail";
import "./assets/css/bootstrap.css";
import "./assets/css/store.css";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="login" element={<Login />} />
          <Route path="carrinho" element={<MyCart />} />
          <Route path="pedidos" element={<MyOrders />} />
          <Route path="pedidos/:id" element={<OrderDetail />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}


export default App;