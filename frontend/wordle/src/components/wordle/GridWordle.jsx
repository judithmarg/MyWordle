"use client"
import { useState } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import styles from './wordle.module.css';
import Zoom from '@mui/material/Zoom';
import { compareWord } from '@/lib/gameService';
import Paper from '@mui/material/Paper';
import CellWordle from './CellWordle';

const icon = (
	<Paper sx={{ m: 1, width: 100, height: 100 }} elevation={4}>
		<svg>
			<Box
				component="polygon"
				points='0,100 50,00, 100,100'
				sx={{ fill: 'white', strokeWidth: 1 }}
			/>
		</svg>
	</Paper>
)



export default function GridWordle({ idInfo = 17 }) { //info sera la respuesta de put o post
	const [checked, setChecked] = useState(true);
	const [textCompare, setTextCompare] = useState("");
	const [wordleArray, setWordleArray] = useState(['pink', 'pink', 'pink', 'pink', 'pink']);
	const handleKeyPress = (keyCode, key) => {
		console.log(keyCode, key);
	}
	const icon2 = 
	(
		<div
			style={{ width: '4rem', height: '4rem' }}
			tabIndex={0}
			onKeyDown={(e) => handleKeyPress(e.detail, e.key)}>
			<p style={{ color: 'black', fontSize: '1.2rem' }}>letter</p>
		</div>
	)
	const fetchCompareWord = async () => {
		try {
			const compareResult = await compareWord(idInfo);
			const cellGreen = compareResult.correct_pos_index.map(arrayRes => arrayRes[0]);
			const cellYellow = compareResult.different_pos_index.map(arrayRes => arrayRes[0]);

			const wordleUpdated = wordleArray.map((valCol, index) => {
				return cellGreen.includes(index) ? 'green' : cellYellow.includes(index) ? "yellow" : 'gray'
			});

			setWordleArray(wordleUpdated);
		}
		catch (error) {
			console.error("Error al comparar palabra", error)
		}
	}

	const handleChange = (e) => {
		setTextCompare(e.target.value);
	};

	return (
		<Box sx={{maxWidth:'50vw', minWidth:'30vh'}}>
			<Grid container spacing={1}>
				<Grid size={2.4} sx={{ backgroundColor: wordleArray[0], width: '50px', height: '50px'  }}>
					<>
						<Zoom in={checked} >
							<Paper sx={{ width: '100%', height: '100%' }}>
								<svg><Box><p style={{ color: 'black', fontSize: '1rem' }}>holitaa</p></Box></svg>
							</Paper>
						</Zoom>
					</>

				</Grid>
				 <Grid size={2.4} sx={{ backgroundColor: wordleArray[1] }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '500ms' : '0ms' }}>{icon2}</Zoom>
				</Grid>
				<Grid size={2.4} sx={{ backgroundColor: wordleArray[2] }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '800ms' : '0ms' }}><CellWordle /></Zoom>
				</Grid>
				{/*<Grid size={2.4} sx={{ backgroundColor: wordleArray[3] }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '1000ms' : '0ms' }}><CellWordle /></Zoom>
				</Grid>
				<Grid size={2.4} sx={{ backgroundColor: wordleArray[4] }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '1000ms' : '0ms' }}><CellWordle /></Zoom>
				</Grid> */}
			</Grid>
		</Box>
	);
};
