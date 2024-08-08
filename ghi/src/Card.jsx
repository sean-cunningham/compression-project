import { Card, CardContent, Typography, List, ListItem, ListItemText } from '@mui/material';
import PropTypes from 'prop-types'

const Result_Card = ({ name, result }) => {

    let size = result.original_size;
    let compressed_size = result.compressed_size
    let compression = Math.round((result.compression)*100)
    console.log("Compression: ", compression)
    let [unit, c_unit] = ["", ""];
    // let d_unit = ""
    // let decompressed_size = result.decompress_size
    let c_time = (result.compress_time*1000).toFixed(2)
    // let d_time = (result.decompress_time*1000).toFixed(2)


    if (size / (1024**2) >=1){
        size = (size/(1024**2)).toFixed(2);
        unit = "MB";
     } else if (size / 1024 >= 1){
        size = (size/1024).toFixed(2);
        unit = "KB";
     } else {unit = "bytes"}

     if (compressed_size / (1024**2) >=1){
        compressed_size = (compressed_size/(1024**2)).toFixed(2);
        c_unit = "MB";
     } else if (compressed_size / 1024 >= 1){
        compressed_size = (compressed_size/1024).toFixed(2);
        c_unit = "KB";
     } else {c_unit = "bytes"}

    //  if (decompressed_size / (1024**2) >=1){
    //     decompressed_size = (decompressed_size/(1024**2)).toFixed(2);
    //     d_unit = "MB";
    //  } else if (decompressed_size / 1024 >= 1){
    //     decompressed_size = (decompressed_size/1024).toFixed(2);
    //     d_unit = "KB";
    //  } else {d_unit = "bytes"}


    return (
        <Card className="card">
            <CardContent>
                <Typography variant="h6" component="div" className='title'>
                    {name}
                </Typography>
                <List>
                    <ListItem className='li'>
                        <ListItemText primary={`Original Size: ${size} ${unit}`} />
                    </ListItem>
                    <ListItem>
                        <ListItemText primary={`Compressed Size: ${compressed_size} ${c_unit}`} />
                    </ListItem>
                    <ListItem>
                        <ListItemText primary={`Decompression: ${compression}%`} />
                    </ListItem>
                    <ListItem>
                        <ListItemText primary={`Compression Time: ${c_time}ms`} />
                    </ListItem>
                    {/* <ListItem>
                        <ListItemText primary={`Decompression Time: ${d_time}ms`} />
                    </ListItem>
                    <ListItem>
                        <ListItemText primary={`Decompression size: ${decompressed_size} ${d_unit}`} />
                    </ListItem> */}
                </List>
            </CardContent>
        </Card>
    );
};

Result_Card.propTypes = {
    name: PropTypes.string.isRequired,
    result: PropTypes.shape({
        original_size: PropTypes.number.isRequired,
        compressed_size: PropTypes.number.isRequired,
        compression: PropTypes.number.isRequired,
        compress_time: PropTypes.number.isRequired,
        // decompress_time: PropTypes.number.isRequired,
        // decompress_size: PropTypes.number.isRequired,
    }).isRequired,
};

export default Result_Card
