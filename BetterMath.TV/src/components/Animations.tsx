import { Link } from "react-router-dom";

function AnimationsCover() {
  return (
    <Link to="/animations">
      <img
        src="/Animations.svg"
        alt="BetterMath Animations"
        className="cover-image"
      />
    </Link>
  );
}

export default AnimationsCover;
