import Game from "./Game";
const ListOfGames = ({games, notes}) => {

    const getNotesByID = (id) => {
        let filtered_array = [];
        notes.map((note) => {
            if(note.gameID === id){
                filtered_array.push(note);
            }
        })
        // console.log(filtered_array)
        return filtered_array
    }

    return ( 
        <div className='listOfGames'>
            { games.map((game) => (
                <Game key={game.id} game={game} notes={getNotesByID(game.id)}/>
            ))}
        </div>
     );
}
 
export default ListOfGames;