const videos = [
  { src: "/videos/DrakeEquation1/DrakeEquation1.mov", title: "Drake Equation" },
  {
    src: "/videos/TotalInternalReflection/TotalInternalReflection.mov",
    title: "Total Internal Reflection",
  },
  {
    src: "/videos/CelestialSphere/CelestialSphere.mp4",
    title: "Celestial Sphere",
  },
  { src: "/videos/MontyHall/MontyHall.mov", title: "Monty Hall Problem" },
];

function AnimationsPage() {
  return (
    <div className="app-container">
      <h1 className="animation-text">Recent Animations</h1>
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          gap: "2rem",
        }}
      >
        {videos.map((video) => (
          <div key={video.src} style={{ maxWidth: "200px" }}>
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
    </div>
  );
}

export default AnimationsPage;
