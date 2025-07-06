"use client"
import {useState} from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import styles from './wordle.module.css';
import Zoom from '@mui/material/Zoom';
import { compareWord } from '@/lib/gameService';

const  GridWordle = ({idInfo}) => { //info sera la respuesta de put o post
	const [checked, setChecked] = useState(false);
	const [infoCompare, setInfoCompare] = useState(null);
	const [wordleArray, setWordleArray] = useState(['gray','gray','gray','gray','gray']);

	const compareWord = async () => {
		try {
			const compareResult = await compareWord(idInfo);
			const cellGreen = compareResult.correct_pos_index.map(arrayRes => arrayRes[0]);
			const cellYellow = compareResult.different_pos_index.map(arrayRes => arrayRes[0]);

			const wordleUpdated = wordleArray.map(valCol, index => {
				return cellGreen.includes(index) ? 'green' : cellYellow.includes(index) ? "yellow" : 'gray'
			});

			setWordleArray(wordleUpdated);
			
		}
		catch (error) {
			console.error("Error al comparar palabra", error)
		}
	}
	
	return (
	<div className={styles.container}>
		<Grid container spacing={2}>
			<Grid size={2}>
				<Zoom in={checked}style={{backgroundColor:wordleArray[0]}}>hola</Zoom>
			</Grid>
			<Grid size={2}>
				<Zoom in={checked} style={{ transitionDelay: checked ? '500ms' : '0ms', backgroundColor:wordleArray[1] }}>hola2</Zoom>
			</Grid>
			<Grid size={2}>
				<Zoom in={checked} style={{ transitionDelay: checked ? '800ms' : '0ms', backgroundColor:wordleArray[2] }}>hola3</Zoom>
			</Grid>
			<Grid size={2}>
				<Zoom  in={checked} style={{ transitionDelay: checked ? '1000ms' : '0ms', backgroundColor:wordleArray[3] }}>hola4</Zoom>
			</Grid>
			<Grid size={2}>
				<Zoom  in={checked} style={{ transitionDelay: checked ? '1000ms' : '0ms', backgroundColor:wordleArray[4] }}>hola5</Zoom>
			</Grid>
		</Grid>
	</div>
	);
};

export default GridWordle;
