import axios from "axios";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import { useEffect, useState } from "react";
import Product from "../components/Product/Product";

const MyCart = () => {
  const navigate = useNavigate();

  const [mycart, setMyCart] = useState([]);
  const [product, setProduct] = useState([]);

  let token = "Token ".concat(Cookies.get('token'));
  let url = "http://localhost:8000/carrinho/";
  axios.defaults.headers.common['Authorization'] = token
  const fetchData = () => {
    return axios.get(url)
          .then((response) => {
            setMyCart(response.data);
            setProduct(response.data.cartitem_set);
          });
  }

  useEffect(() => {
    if (!Cookies.get('token')) {
      navigate("/login/");
    }
    fetchData();
  },[])

  function Checkout() {
    let token = "Token ".concat(Cookies.get('token'));
    let csrftoken = Cookies.get('csrftoken');

    if (token) {
      let url = "http://localhost:8000/carrinho/checkout/";
      axios.defaults.headers.common['Authorization'] = token
      axios.defaults.headers.common['X-CSRFTOKEN'] = csrftoken


      axios.post(url).then((response) => {
        alert("Compra finalizada")
        window.location.reload();
      });
    }
  }

  if (mycart && product) {
    return (
      <div className="bg-dark p-5">
        <div className="mb-5 d-inline-flex">
          <div className="text-light">
            <p className="h3">SubTotal: R$ { Math.round(mycart.total*100)/100 }</p>
            <p className="h3">Frete: { Math.round(mycart.freight*100)/100 }</p>
            <p className="h3">Total: { Math.round((mycart.total + mycart.freight)*100)/100 }</p>
            <button type="button" className="btn btn-outline-success" onClick={Checkout}>Checkout</button>
          </div>
        </div>
        <div className="container-fluid text-light"> 
          <div className="row w-100 mb-3">
          {
            product.map((MyProductObj, index) => 
              <Product 
                id={MyProductObj.product.id} 
                name={MyProductObj.product.name} 
                price={MyProductObj.product.price} 
                score={MyProductObj.product.score} 
                image={"http://localhost:8000".concat(MyProductObj.product.image)} 
                options={1}
                quantity={MyProductObj.quantity}/>)
          }
          </div> 
        </div>
      </div>
    )
  } else {
    return (
      <div className="p-5 w-100 text-center">
        <p className="h1 text-Dark">Carrinho vázio.</p>
      </div>
    )
  }
}

export default MyCart;