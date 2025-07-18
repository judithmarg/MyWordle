"use client"
import { useState } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import styles from './wordle.module.css';
import Zoom from '@mui/material/Zoom';
import { compareWord } from '@/lib/gameService';
import Paper from '@mui/material/Paper';
import CellWordle from './CellWordle';

export default function GridWordle({ idInfo = 17 }) { //info sera la respuesta de put o post
	const [checked, setChecked] = useState(true);
	const [textCompare, setTextCompare] = useState("");
	const [wordleArray, setWordleArray] = useState(['pink', 'pink', 'pink', 'pink', 'pink']);
	const handleKeyPress = (key) => {
		4
		console.log(key);
		setTextCompare(key);
	}
	const cell1 = (
		<div
			style={{ height:'100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}
			tabIndex={0}
			onKeyDown={(e) => handleKeyPress(e.key)}>
			<p style={{ color: 'black', fontSize: '2rem', fontWeight: 'bolder', textAlign:'center', textTransform:'capitalize' }}>{textCompare[0]}</p>
		</div>
	)
	const cell2 = (
		<div
			style={{ height:'100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}
			tabIndex={0}
			onKeyDown={(e) => handleKeyPress(e.key)}>
			<p style={{ color: 'black', fontSize: '2rem', fontWeight: 'bolder', textAlign:'center', textTransform:'capitalize'}}>{textCompare[1]}</p>
		</div>
	)
	const cell3 = (
		<div
			style={{ height:'100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}
			tabIndex={0}
			onKeyDown={(e) => handleKeyPress(e.key)}>
			<p style={{ color: 'black', fontSize: '2rem', fontWeight: 'bolder', textAlign:'center', textTransform:'capitalize'}}>{textCompare[2]}</p>
		</div>
	)
	const cell4 = (
		<div
			style={{ height:'100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}
			tabIndex={0}
			onKeyDown={(e) => handleKeyPress(e.key)}>
			<p style={{ color: 'black', fontSize: '2rem', fontWeight: 'bolder', textAlign:'center', textTransform:'capitalize'}}>{textCompare[3]}</p>
		</div>
	)
	const cell5 = (
		<div
			style={{ height:'100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}
			tabIndex={0}
			onKeyDown={(e) => handleKeyPress(e.key)}>
			<p style={{ color: 'black', fontSize: '2rem', fontWeight: 'bolder', textAlign:'center', textTransform:'capitalize'}}>{textCompare[4]}</p>
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

	const handleChangeText = (e) => {
		setTextCompare(e.target.value);
	};

	return (
		<Box sx={{position:'relative'}}>
			<input
				type="text"
				name="age"
				id="age"
				step="2"
				style={{ position: 'absolute', letterSpacing:'44px', fontSize:'2rem',textTransform:'capitalize',opacity: 0, width: 'auto', height: '50px', borderRadius:'30px', zIndex:40, left:'15px' }}
				onKeyDown={handleChangeText}
				tabIndex={0}
			/>

			<Grid container spacing={1}>
				<Grid size={2.4} sx={{ backgroundColor: wordleArray[1], width: '50px', height: '50px', borderRadius:'30px' }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '500ms' : '0ms' }}>{cell1}</Zoom>
				</Grid>
				<Grid size={2.4} sx={{ backgroundColor: wordleArray[1], width: '50px', height: '50px', borderRadius:'30px' }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '500ms' : '0ms' }}>{cell2}</Zoom>
				</Grid> <Grid size={2.4} sx={{ backgroundColor: wordleArray[1], width: '50px', height: '50px', borderRadius:'30px' }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '500ms' : '0ms' }}>{cell3}</Zoom>
				</Grid> <Grid size={2.4} sx={{ backgroundColor: wordleArray[1], width: '50px', height: '50px', borderRadius:'30px' }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '500ms' : '0ms' }}>{cell4}</Zoom>
				</Grid> <Grid size={2.4} sx={{ backgroundColor: wordleArray[1], width: '50px', height: '50px', borderRadius:'30px' }}>
					<Zoom in={checked} style={{ transitionDelay: checked ? '500ms' : '0ms' }}>
						<CellWordle letter={textCompare[4]} />
					</Zoom>
				</Grid>
			</Grid>
		</Box>
	);
};
