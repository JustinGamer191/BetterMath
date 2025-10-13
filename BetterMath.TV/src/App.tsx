import Header from "./components/Header.tsx";
import AnimationsCover from "./components/Animations.tsx";
import SourceCode from "./components/SourceCode.tsx";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <div className="text-center">
        <div className="header-text">
          <Header />
        </div>

        <div className="content-row">
          <AnimationsCover />
          <SourceCode />
        </div>
      </div>
    </div>
  );
}

export default App;
