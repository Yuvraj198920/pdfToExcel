import React, { useState } from "react";
import { Button, Typography, Paper, Box } from "@mui/material";
import axios from "axios";
import * as XLSX from "xlsx";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleDownload = async (data) => {
    // Create a new workbook
    const wb = XLSX.utils.book_new();
    // Convert JSON data to sheet
    const ws = XLSX.utils.json_to_sheet(data);
    // Add sheet to workbook
    XLSX.utils.book_append_sheet(wb, ws, "Transactions");
    // Write workbook and trigger download
    XLSX.writeFile(wb, "Transactions.xlsx");
  };
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      if (response.status === 200) {
        handleDownload(response.data);
      }
      alert("File uploaded successfully!");
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Error uploading file");
    }
  };
  return (
    <Box sx={{ padding: 2 }}>
      <Paper elevation={3} sx={{ padding: 2 }}>
        <Typography variant="h6">Upload your PDF</Typography>
        <input
          accept="application/pdf"
          style={{ display: "none" }}
          id="raised-button-file"
          type="file"
          onChange={handleFileChange}
        />
        <label htmlFor="raised-button-file">
          <Button variant="contained" component="span">
            Choose File
          </Button>
        </label>
        <Button
          variant="contained"
          color="primary"
          onClick={handleUpload}
          sx={{ marginLeft: 2 }}
        >
          Upload
        </Button>
      </Paper>
    </Box>
  );
};

export default FileUpload;
