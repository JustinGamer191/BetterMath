import { Link } from "react-router-dom";

function Astronomy() {
  return (
    <Link to="geometry">
      <img
        src="/Geometry.svg"
        alt="Geometry Animations"
        className="cover-image"
      />
    </Link>
  );
}

export default Astronomy;
