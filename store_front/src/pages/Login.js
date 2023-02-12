import slide from "../assets/img/slide.jpg";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
import { useState } from "react";

const Login = () => {
  const navigate = useNavigate();
  const [message, setMessage] = useState("");

  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");

  const loginStore = (event) => {

    const url = "http://localhost:8000/login/"
    axios.post(url, { username: username, password: password }, { withCredentials: true })
    .then(function (response) {
      if (response.status == 202) {
        Cookies.set("token", response.data.token)
        Cookies.set("user", username)
        navigate("/");
        window.location.reload();
      } else {
        setMessage("Login ou senha inválidos")
      }
    })
    .catch(function (error) {
      setMessage("Login ou senha inválidos")
    });
  }

  return (
    <div className="position-relative">
      <img src={slide} className="img-fluid w-100 h-100"/>
      <div className="bg-dark position-absolute login-form p-3 text-light">
        <form>
          <div className="form-group">
            <label htmlFor="userField">Usuário</label>
            <input type="text" 
              className="form-control" 
              id="userField" 
              placeholder="Usuário" 
              onChange={(e) => setUserName(e.target.value)}/>
          </div>
          <div className="form-group">
            <label htmlFor="passwordField">Senha</label>
            <input type="password" 
              className="form-control" 
              id="passwordField" 
              placeholder="Senha" 
              onChange={(e) => setPassword(e.target.value)}/>
          </div>
          <p className="text-light">{message}</p>
          <div className="text-right mb-2 mr-2">
            <button type="button" className="btn btn-outline-success" onClick={loginStore}>Logar</button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Login


const url = '<your url>';
