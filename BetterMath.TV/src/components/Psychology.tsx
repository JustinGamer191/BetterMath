import { Link } from "react-router-dom";

function Psychology() {
  return (
    <Link to="psychology">
      <img
        src="/Psychology.svg"
        alt="Psychology Animations"
        className="cover-image"
      />
    </Link>
  );
}

export default Psychology;
