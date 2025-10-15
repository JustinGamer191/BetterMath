const videos = [
  {
    src: "/finished_videos/LinearRegression/LinearRegression.mp4",
    title: "Linear Regression",
  },
  {
    src: "/finished_videos/Compare/Compare.mp4",
    title: "Compare Faces",
  },
  {
    src: "/finished_videos/ImageSearch/ImageSearch.mp4",
    title: "Facial Recognition",
  },
  {
    src: "/finished_videos/GradientDescent/GradientDescent.mp4",
    title: "Gradient Descent",
  },
];

function MachineLearningPage() {
  return (
    <div>
      <h1 className="animation-text">Machine Learning Animations</h1>
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          gap: "2rem",
        }}
      >
        {videos.map((video) => (
          <div key={video.src} style={{ width: "300px", maxWidth: "90%" }}>
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

export default MachineLearningPage;
