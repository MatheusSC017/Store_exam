import slide from "../assets/img/slide.jpg";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import { useEffect, useState } from "react";
import Order from "../components/Order/Order";


const MyOrders = () => {
  const navigate = useNavigate();

  const [order, setOrder] = useState([]);

  let url = "http://localhost:8000/pedidos/";
  let token = "Token ".concat(Cookies.get('token'));
  let csrftoken = Cookies.get('csrftoken');

  axios.defaults.headers.common['Authorization'] = token
  axios.defaults.headers.common['X-CSRFTOKEN'] = csrftoken
  const fetchData = () => {
    return axios.get(url)
      .then((response) => {
        setOrder(response.data.results);
      });
  }

  useEffect(() => {
    if (!Cookies.get('token')) {
      navigate("/login/");
    }
    fetchData();
  },[])

  return (
    <div className="position-relative">
      <img src={slide} className="img-fluid w-100 h-100"/>
      <div className="bg-dark position-absolute login-form p-3 text-light">
      <table className="table table-dark">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">SubTotal</th>
            <th scope="col">Frete</th>
            <th scope="col">Total</th>
          </tr>
        </thead>
        <tbody>
        {
            order && order.length > 0 && order.map((orderObj, index) => <Order
                id={orderObj.id}
                total={orderObj.total}
                freight={orderObj.freight}/>)
        }
        </tbody>
      </table>
      </div>
    </div>
  )
}

export default MyOrders;