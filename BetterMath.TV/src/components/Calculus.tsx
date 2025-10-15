import { Link } from "react-router-dom";

function Psychology() {
  return (
    <Link to="calculus">
      <img
        src="/Calculus.svg"
        alt="Calculus Animations"
        className="cover-image"
      />
    </Link>
  );
}

export default Psychology;
