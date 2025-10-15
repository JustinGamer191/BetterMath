import { Link } from "react-router-dom";

function Astronomy() {
  return (
    <Link to="astronomy">
      <img
        src="/Astronomy.svg"
        alt="Astronomy Animations"
        className="cover-image"
      />
    </Link>
  );
}

export default Astronomy;
