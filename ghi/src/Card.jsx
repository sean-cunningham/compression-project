import { Card, CardContent, Typography, List, ListItem, ListItemText } from '@mui/material';

const Result_Card = ({ name, result }) => {
  return (
    <Card sx={{ maxWidth: 345, margin: '1rem' }}>
      <CardContent>
        <Typography variant="h5" component="div">
          {name}
        </Typography>
        <List>
          <ListItem>
            <ListItemText primary={`Original Size: ${result.original_size}`} />
          </ListItem>
          <ListItem>
            <ListItemText primary={`Compressed Size: ${result.compressed_size}`} />
          </ListItem>
          <ListItem>
            <ListItemText primary={`Decompression %: ${result['decompression %']}`} />
          </ListItem>
          <ListItem>
            <ListItemText primary={`Compression Time: ${result.compress_time}s`} />
          </ListItem>
          <ListItem>
            <ListItemText primary={`Decompression Time: ${result.decompress_time}s`} />
          </ListItem>
        </List>
      </CardContent>
    </Card>
  );
};

export default Result_Card
