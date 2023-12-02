import React from "react";
import { ThemeProvider } from "@mui/material/styles";
import theme from "./theme/theme";
import Header from "./components/Header";
import FileUpload from "./components/FileUpload";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div className="App">
        <Header />
        <FileUpload />
      </div>
    </ThemeProvider>
  );
}

export default App;
