import { Outlet, Link } from "react-router-dom";
import Cookies from "js-cookie";
import logo from '../assets/img/logo.png'

function IsAutheticated(props) {
  if (props.user) {
    return (
      <>
        <li className="nav-item">
          <Link to={"/pedidos/"}> 
            <p className="nav-link">Meus Pedidos</p>
          </Link>
        </li>
        <li className="nav-item">
          <Link to={"/carrinho/"}> 
            <p className="nav-link">Carrinho</p>
          </Link>
        </li>
        <li className="nav-item"><a className="nav-link">Olá, {props.user}</a></li>
      </>
    );
  } 
  return <li className="nav-item">
    <Link to={"/login/"}>
      <p className="nav-link">
        Login
      </p>
    </Link>
  </li>;
  
}

function Layout() {
  let user = Cookies.get('user');

  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <p className="navbar-brand">
          <Link to={"/"}> 
            <img src={logo} className="rounded float-left" alt="logo"></img>
          </Link>
        </p>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <Link to={"/"}> 
                <a className="nav-link">
                  Home <span className="sr-only">(current)</span>
                </a>
              </Link>
            </li>
            <IsAutheticated user={user}/>
          </ul>
        </div>
      </nav>

      <Outlet />
    </>
  )
};

export default Layout;
