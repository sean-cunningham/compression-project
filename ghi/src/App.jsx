import { useState } from 'react';
import Dropzone from './Dropzone';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Result_Card from './Card';
import './App.css'


function App() {

  const [results, setResults] = useState({});


  const handleResults = (results) => {
    console.log("handling results: ", results)
    setResults(results)
  };

  console.log("results: ", results)

  return (

      <Box className="container">
        <Box className="top">
          <Typography variant="h3" component="div" gutterBottom>
            Drop Files here to Compress
          </Typography>
        </Box>
        <Box className="middle">
          <Dropzone handleResults={handleResults}/>
        </Box>
        <Box className="bottom">
          {Object.entries(results).map(([name, result])=>{
              console.log("name: ", name)
              console.log("result: ", result)
              return <Result_Card key={name} name={name} result={result}/>
          })}
        </Box>
      </Box>





  )
}

export default App
