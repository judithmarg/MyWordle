import Box from '@mui/material/Box';
import GridWordle from '@/components/wordle/GridWordle';

export default function Home() {
  const defaultStyles = {
    maxContainer: {
      display:'flex', 
      flexDirection: 'column',
      width:'100vw', 
      height:"100vh", 
      justifyContent:"center", 
      alignItems:"center"
    }
  }
  return (
    <Box style={defaultStyles.maxContainer}>
      <GridWordle />
      <p>Judith</p>
    </Box>
  );
}
