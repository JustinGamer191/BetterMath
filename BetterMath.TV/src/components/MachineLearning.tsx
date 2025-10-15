import { Link } from "react-router-dom";

function MachineLearning() {
  return (
    <Link to="machinelearning">
      <img
        src="/MachineLearning.svg"
        alt="Machine Learning Animations"
        className="cover-image"
      />
    </Link>
  );
}

export default MachineLearning;
