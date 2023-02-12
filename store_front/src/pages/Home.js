import slide from "../assets/img/slide.jpg"
import Product from "../components/Product/Product";
import axios from "axios";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useEffect, useState } from "react";

const Home = () => {
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const order_by = searchParams.get("order_by");

  const [product, setProduct] = useState([]);


  const orderByChanged = (event) => {
    if (event.target.value){
      navigate("/?order_by=" + event.target.value);
    } else {
      navigate("/");
    }
    window.location.reload();
  }

  let url = "http://localhost:8000/produtos/";
  if (order_by) {
    url = url.concat("?order_by=");
    url = url.concat(order_by);
  }

  const fetchData = () => {
    return axios.get(url)
          .then((response) => {
            setProduct(response.data.results);
          });
  }

  useEffect(() => {
    fetchData();
  },[])

  return (
    <div>
      <div className="w-100">
        <img src={slide} className="img-fluid w-100" alt="Slide"></img>
      </div>
      <div className="bg-dark p-5">

        <div className="text-right">
          <select className="custom-select custom-select-lg mb-3 order_by_select" onChange={orderByChanged}>
            <option value="">Ordenar por</option>
            <option value="name">A-Z</option>
            <option value="price">Menor preço</option>
            <option value="score">Menor score</option>
            <option value="-name">Z-A</option>
            <option value="-price">Maior preço</option>
            <option value="-score">Maior score</option>
          </select>
        </div>

        <div className="container-fluid text-light"> 
          <div className="row w-100 mb-3">
          {
            product && product.length > 0 && product.map((productObj, index) => 
              <Product 
                id={productObj.id} 
                name={productObj.name} 
                price={productObj.price} 
                score={productObj.score} 
                image={productObj.image} 
                options={2} />)
          }
          </div> 
        </div>
      </div>
    </div>
  );
};

export default Home;