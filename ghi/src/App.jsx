import { useState } from 'react';
import Dropzone from './Dropzone';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Result_Card from './Card';


function App() {

  const [results, setResults] = useState({});


  const handleResults = (results) => { setResults(results)};


  return (

      <Box sx={{
        width: '100%',
        maxWidth: 500,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center"
        }}>
        <Typography variant="h3" gutterBottom>
          Drop Files here to compress
        </Typography>
        <Dropzone handleResults={handleResults}/>
        {Object.entries(results).map(([name, result])=>{
            return <Result_Card key={name} name={name} result={result}/>
        })}
      </Box>

  )
}

export default App
