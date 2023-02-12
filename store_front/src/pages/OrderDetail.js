import { useParams } from 'react-router-dom'
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import { useEffect, useState } from "react";
import Product from '../components/Product/Product';


const OrderDetail = () => {
	const navigate = useNavigate();

	const [myorder, setMyOrder] = useState([]);
  const [product, setProduct] = useState([]);

	const { id } = useParams();
	let url = "http://localhost:8000/pedidos/".concat(id);
	let token = "Token ".concat(Cookies.get('token'));
	let csrftoken = Cookies.get('csrftoken');

	axios.defaults.headers.common['Authorization'] = token
	axios.defaults.headers.common['X-CSRFTOKEN'] = csrftoken
	const fetchData = () => {
		return axios.get(url)
		.then((response) => {
			setMyOrder(response.data);
      setProduct(response.data.cartitem_set);
		});
	}

	useEffect(() => {
		if (!Cookies.get('token')) {
			navigate("/login/");
		}
		fetchData();
	},[])

	return (
		<div className="bg-dark p-5">
			<div className="mb-5 d-inline-flex">
				<div className="text-light">
					<p className="h3">SubTotal: R$ { Math.round(myorder.total*100)/100 }</p>
					<p className="h3">Frete: { Math.round(myorder.freight*100)/100 }</p>
					<p className="h3">Total: { Math.round((myorder.total + myorder.freight)*100)/100 }</p>
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
							image={MyProductObj.product.image} 
							myCart={true}
							quantity={MyProductObj.quantity}/>)
				}
				</div> 
			</div>
		</div>
	)
}

export default OrderDetail