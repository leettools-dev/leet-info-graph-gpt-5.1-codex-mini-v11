import React from "react";
import ReactDOM from "react-dom/client";

const App = () => (
  <div className="app-root" style={{ fontFamily: "Inter, system-ui", padding: "2rem" }}>
    <header style={{ marginBottom: "1.5rem" }}>
      <h1>Research Infographic Studio</h1>
      <p>Generate shareable infographics with contextual articles and verified citations.</p>
    </header>

    <section>
      <h2>Sign in to begin</h2>
      <p>
        Authenticate with Google to submit a research prompt. Results include an AI-generated infographic,
        explanatory article, and supporting sources.
      </p>
    </section>

    <section style={{ marginTop: "2rem" }}>
      <h2>History & exports soon</h2>
      <p>
        We track your generated research results so you can revisit past prompts, refine outputs, and
        export infographics/articles with citations.
      </p>
    </section>
  </div>
);

ReactDOM.createRoot(document.getElementById("root")!).render(<App />);
