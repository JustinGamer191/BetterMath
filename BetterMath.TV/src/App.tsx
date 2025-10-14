import { Routes, Route } from "react-router-dom";
import Header from "./components/Header.tsx";
import AnimationsCover from "./components/Animations.tsx";
import SourceCode from "./components/SourceCode.tsx";
import Community from "./components/Community.tsx";
import AnimationsPage from "./pages/AnimationsPage.tsx";
import "./App.css";

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
              <div className="content-row">
                <Community />
                <AnimationsCover />
                <SourceCode />
              </div>
            }
          />
          <Route path="/animations" element={<AnimationsPage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
