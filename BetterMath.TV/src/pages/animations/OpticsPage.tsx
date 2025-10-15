const videos = [
  {
    src: "/finished_videos/LawOfReflection/LawOfReflection.mp4",
    title: "Law Of Reflection",
  },
  {
    src: "/finished_videos/SnellsLaw/SnellsLaw.mp4",
    title: "Snells Law",
  },
  {
    src: "/finished_videos/TotalInternalReflection/TotalInternalReflection.mp4",
    title: "Total Internal Reflection",
  },
];

function OpticsPage() {
  return (
    <div>
      <h1 className="animation-text">Optics Animations</h1>
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

export default OpticsPage;
