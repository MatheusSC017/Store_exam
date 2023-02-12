import { Link } from "react-router-dom";

function Order(props) {
  return (
    <tr>
      <th scope="row"><Link to={"/pedidos/".concat(props.id)}> {props.id}</Link></th>
      <td>R$ { Math.round(props.total * 100)/100 }</td>
      <td>R$ { Math.round(props.freight * 100)/100 }</td>
      <td>R$ { Math.round((props.total +  props.freight) * 100)/100 }</td>
    </tr>
  )
}

export default Order
