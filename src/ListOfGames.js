import Game from "./Game";
const ListOfGames = (props) => {
    return ( 
        <div class='listOfGames'>
            {props.games.map( (object, i) => {
                <Game game={object}/>     
            } )
            }
        </div>
     );
}
 
export default ListOfGames;