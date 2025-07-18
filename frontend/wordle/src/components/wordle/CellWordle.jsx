
const CellWordle = ({letter}) => {
	return (
		<div
			style={{ height:'100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}
		>
			<p style={{ color: 'black', fontSize: '2rem', fontWeight: 'bolder', textAlign:'center', textTransform:'capitalize'}}>{letter}</p>
		</div>
	)
};

export default CellWordle;