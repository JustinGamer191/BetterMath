import { Routes, Route } from "react-router-dom";
import Header from "./components/Header.tsx";
import AnimationsCover from "./components/Animations.tsx";
import SourceCode from "./components/SourceCode.tsx";
import Community from "./components/Community.tsx";
import AnimationsPage from "./pages/AnimationsPage.tsx";
import "./App.css";
import AstronomyPage from "./pages/animations/AstronomyPage.tsx";
import CalculusPage from "./pages/animations/CalculusPage.tsx";
import GeometryPage from "./pages/animations/GeometryPage.tsx";
import MachineLearningPage from "./pages/animations/MachineLearningPage.tsx";
import OpticsPage from "./pages/animations/OpticsPage.tsx";
import PsychologyPage from "./pages/animations/PsychologyPage.tsx";

function App() {
  return (
    <div className="app-container">
      <div className="text-center">
        <div className="header-text">
          <Header />
        </div>
        <Routes>
          <Route
            path="/"
            element={
              <div className="main-row">
                <Community />
                <AnimationsCover />
                <SourceCode />
              </div>
            }
          />
          <Route path="/animations" element={<AnimationsPage />} />
          <Route path="/animations/astronomy" element={<AstronomyPage />} />
          <Route path="/animations/calculus" element={<CalculusPage />} />
          <Route path="/animations/geometry" element={<GeometryPage />} />
          <Route
            path="/animations/machinelearning"
            element={<MachineLearningPage />}
          />
          <Route path="/animations/optics" element={<OpticsPage />} />
          <Route path="/animations/psychology" element={<PsychologyPage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
