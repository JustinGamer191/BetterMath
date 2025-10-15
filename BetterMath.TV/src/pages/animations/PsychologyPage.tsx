const videos = [
  {
    src: "/finished_videos/MontyHall/MontyHall.mp4",
    title: "Monty Hall Problem",
  },
  {
    src: "/finished_videos/MontyHallMath/MontyHallMath.mp4",
    title: "Monty Hall(Mathematical Approach)",
  },
];

function PsychologyPage() {
  return (
    <div>
      <h1 className="animation-text">Psychology Animations</h1>
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

export default PsychologyPage;
