const videos = [
  {
    src: "/finished_videos/KingRemake/KingRemake.mp4",
    title: "King's Property(Fixed Mistakes)",
  },
  {
    src: "/finished_videos/DiffEqRemake/DiffEqRemake.mp4",
    title: "Differential Equations(Fixed Mistakes)",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/ArcLengthFormula/ArcLengthFormula.mp4",
    title: "Arc Length Formula",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/GaussianIntegral/GaussianIntegral.mp4",
    title: "Gaussian Integral",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/InverseTrigDerivatives/InverseTrigDerivatives.mp4",
    title: "Inverse Trigonometric Derivatives",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/OldDifferentialEquations/OldDifferentialEquations.mp4",
    title: "DifferentialEquations(Old)",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/OldKingsProperty/OldKingsProperty.mp4",
    title: "King's Property(Old)",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/PiExpansion/PiExpansion.mp4",
    title: "Expansion of Pi",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/PiFromCalculus/PiFromCalculus.mp4",
    title: "Deriving Pi From Calculus",
  },
  {
    src: "/finished_videos/OldProducts/Calculus/TaylorSine/TaylorSine.mp4",
    title: "Taylor Series for Sine Function",
  },
];

function CalculusPage() {
  return (
    <div>
      <h1 className="animation-text">Calculus Animations</h1>
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

export default CalculusPage;
