import { Routes, Route } from "react-router-dom";
import Astronomy from "../components/Astronomy";
import Calculus from "../components/Calculus";
import Geometry from "../components/Geometry";
import MachineLearning from "../components/MachineLearning";
import Optics from "../components/Optics";
import Psychology from "../components/Psychology";
const videos = [
  {
    src: "/finished_videos/DrakeEquation1/DrakeEquation1.mp4",
    title: "Drake Equation",
  },
  {
    src: "/finished_videos/TotalInternalReflection/TotalInternalReflection.mp4",
    title: "Total Internal Reflection",
  },
  {
    src: "/finished_videos/CelestialSphere/CelestialSphere.mp4",
    title: "Celestial Sphere",
  },
];

function AnimationsPage() {
  return (
    <div className="app-container">
      <h1 className="animation-text">Recent Animations</h1>
      <div className="content-row">
        {videos.map((video) => (
          <div key={video.src} className="video-item">
            <video
              src={video.src}
              controls
              style={{
                width: "100%",
                borderRadius: "0.5rem",
                boxShadow: "0 0 2rem rgba(255,255,255,0.2)",
              }}
            />
            <p
              style={{
                color: "white",
                textAlign: "center",
                marginTop: "0.5rem",
              }}
            >
              {video.title}
            </p>
          </div>
        ))}
      </div>
      <h1 className="animation-text">All Animations</h1>
      <Routes>
        <Route
          path="/"
          element={
            <div className="content-row">
              <Astronomy />
              <Calculus />
              <Geometry />
              <MachineLearning />
              <Optics />
              <Psychology />
            </div>
          }
        />
      </Routes>
    </div>
  );
}

export default AnimationsPage;
