import React from 'react';

// Takes props

const Game = (props) => {
    return ( 
        <li className='game'>
            {console.log(props.game)}
        </li>
     );
}
 
export default Game;
