import React from 'react';

// Takes props

const Game = ({game, notes}) => {
    return ( 
        <div className='game' style={{border: "2px solid black"}}>
            <h4>Games Information</h4>
            <ul key={game.id}>
                <li><strong>Player Champion: </strong></li>
                <li>Champion Name: {game.playerChampion.name}</li>
                <img src={game.playerChampion.image} alt={`${game.playerChampion.name}`} />
                <img src={game.playerChampion.full_image} alt={`${game.playerChampion.name} full`} />
                <li>Champion Id: {game.playerChampion.id}</li>

                <li><strong>Opponent Champion: </strong></li>
                <li>Champion Name: {game.opponentChampion.name}</li>
                <img src={game.opponentChampion.image} alt={`${game.opponentChampion.name}`} />
                <img src={game.opponentChampion.full_image} alt={`${game.playerChampion.name} full`} />
                <li>Champion ID: {game.opponentChampion.id}</li>

                <li><strong>Other Information: </strong></li>
                <li>Victory: {game.victory}</li>
                <li>Game ID: {game.id}</li>
            </ul>
            <h4>Notes</h4>
            {notes.map(note => {
                return(
                    <ul key={note.id} style={{border: "1px solid black"}}>
                        <li>game ID: {note.gameID}</li>
                        <li>Note ID: {note.id}</li>
                        <li>Note Content: {note.noteContent}</li>
                    </ul> 
                ) 
            })}

        </div>    
    );
}
 
export default Game;