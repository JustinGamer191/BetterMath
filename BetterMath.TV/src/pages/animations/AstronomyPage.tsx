const videos = [
  {
    src: "/finished_videos/DrakeEquation1/DrakeEquation1.mp4",
    title: "Drake Equation",
  },
  {
    src: "/finished_videos/DrakeEquation1/DrakeEquation1.mp4",
    title: "Drake Equation",
  },
  {
    src: "/finished_videos/CelestialSphere/CelestialSphere.mp4",
    title: "Celestial Sphere",
  },
];

function AstronomyPage() {
  return (
    <div>
      <h1 className="animation-text">Astronomy Animations</h1>
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          gap: "2rem",
        }}
      >
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
    </div>
  );
}

export default AstronomyPage;
