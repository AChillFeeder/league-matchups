import Game from "./Game";
<<<<<<< HEAD
const ListOfGames = ({games, notes}) => {

    const getNotesByID = (id) => {
        let filtered_array = [];
        notes.map((note) => {
            if(note.gameID === id){
                filtered_array.push(note);
            }
        })
        return filtered_array
    }


    return ( 
        <div className='listOfGames'>
            { games.map((game) => (
                <Game key={game.id} game={games} notes={getNotesByID(game.id)}/>
            ))}
=======
const ListOfGames = (props) => {
    return ( 
        <div class='listOfGames'>
            {props.games.map( (object, i) => {
                <Game game={object}/>     
            } )
            }
>>>>>>> parent of 85a8f3a... Data properly retrieved in Home, ListOfGames and Games work, starting on Search function
        </div>
     );
}
 
export default ListOfGames;