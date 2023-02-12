import axios from "axios";
import Cookies from "js-cookie";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Product(props) {
  const [product, _] = useState(props.id);
  const navigate = useNavigate();
  

  const star_icon = (
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-star-fill" viewBox="0 0 16 16">
      <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
    </svg>
  )

  function AddProduct() {
    let token = "Token ".concat(Cookies.get('token'));
    let csrftoken = Cookies.get('csrftoken');

    if (!Cookies.get('token')) {
      navigate("/login/");
    }
    
    let url = "http://localhost:8000/carrinho/adicionar/";
    axios.defaults.headers.common['Authorization'] = token
    axios.defaults.headers.common['X-CSRFTOKEN'] = csrftoken


    axios.post(url, { "product": product, "quantity": 1 }).then((response) => {
      alert("Produto adicionado")
      window.location.reload();
    });

  }

  function RemoveProduct() {
    let token = "Token ".concat(Cookies.get('token'));
    let csrftoken = Cookies.get('csrftoken');

    if (!Cookies.get('token')) {
      navigate("/login/");
    }

    let url = "http://localhost:8000/carrinho/remover/";
    axios.defaults.headers.common['Authorization'] = token
    axios.defaults.headers.common['X-CSRFTOKEN'] = csrftoken


    axios.post(url, { "product": product, "quantity": 1 }).then((response) => {
      alert("Produto removido")
      window.location.reload();
    });

  }

  function OptionAvailable(props) {
    if (props.options == 1) {
      return ( 
        <div className="d-inline-flex">
          <button type="button" className="btn btn-outline-danger" onClick={ RemoveProduct }>Remover</button>
          <p className="h3 pl-3 pr-3">{props.quantity}</p>
          <button type="button" className="btn btn-outline-success" onClick={ AddProduct }>Adicionar</button>
        </div>
      );
    }
    if (props.options == 2) {
      return <button type="button" className="btn btn-outline-success" onClick={ AddProduct }>Adicionar</button>;
    }
    return <></>;
    
  }

  return (
    <div className="col-12 col-md-6 col-lg-4 mb-3">
      <div className="card bg-dark-2 position-relative">
        <div className="h6 bg-dark-2 position-absolute product-score">{star_icon} {props.score}</div>
        <img className="card-img-top p-1" src={props.image} alt="Card image cap"></img>
        <div className="card-body">
          <p className="h4">{props.name}</p>
          <p className="h4">{props.price}</p>
        </div>

        <div className="text-right mb-2 mr-2">
          <OptionAvailable options={props.options} quantity={props.quantity} />
        </div>
      </div>
    </div>
  );
}

export default Product
