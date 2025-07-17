"use client";

import { useState } from "react";
import { Box } from "@mui/material";

const CellWordle = () => {
	const [letter, setLetter] = useState("");

	const handleKeyPress = (keyCode, key) => {
		console.log(keyCode, key);
	}
	return (
		<div
			style={{ width: '4rem', height: '4rem' }}
			tabIndex={0}
			onKeyDown={(e) => handleKeyPress(e.detail, e.key)}
			>
			<p style={{ color: 'black', fontSize: '1.2rem' }}>{letter}</p>
		</div>
	)
};

export default CellWordle;