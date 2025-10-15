const videos = [
  {
    src: "/finished_videos/OldProducts/Geometry/AreaVsCircumference/AreaVsCircumference.mp4",
    title: "Area Vs Circumference",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/InscribedAngle/InscribedAngle.mp4",
    title: "Inscribed Angle",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/LawOfSines/LawOfSines.mp4",
    title: "Law Of Sines",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/OvalArea/OvalArea.mp4",
    title: "Oval Area",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/PowerOfAPoint/PowerOfAPoint.mp4",
    title: "Power Of A Point",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/ProbabilityGeometryConnection/ProbabilityGeometryConnection.mp4",
    title: "Probability-Geometry Connection",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/ShoelaceTheorem/ShoelaceTheorem.mp4",
    title: "Shoelace Theorem",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/SineAdditionFormula/SineAdditionFormula.mp4",
    title: "Sine Addition Formula",
  },
  {
    src: "/finished_videos/OldProducts/Geometry/SineAreaFormula/SineAreaFormula.mp4",
    title: "Sine Area Formula",
  },
];

function GeometryPage() {
  return (
    <div>
      <h1 className="animation-text">Geometry Animations</h1>
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

export default GeometryPage;
