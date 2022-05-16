
import React from 'react';
import ENVIRONMENT_VARIABLES from "./ENVIRONMENT_VARIABLES.json";
import {HTTPget, HTTPpost} from "./EasyHTTP";
import ListOfGames from './ListOfGames';

const Home = () => {

<<<<<<< HEAD
    const [games, setGames] = React.useState([]);
    const [notes, setNotes] = React.useState([]);
    const [isLoading, setIsLoading] = React.useState(true);

    const getAllGames = () => {
        setIsLoading(true)
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/gamesHistory`)
        .then( data => {
                console.log(data);
                setGames(data[0])
                setNotes(data[1])
                setIsLoading(false);
=======
    const [games, setGames] = React.useState({});
    const [notes, setNotes] = React.useState([])

    const getAllGames = () => {
        console.log("fetching");
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/gamesHistory`)
        .then( data => {
                console.log(data);
                // setGames(games_)
                // setNotes(notes_)
>>>>>>> parent of 85a8f3a... Data properly retrieved in Home, ListOfGames and Games work, starting on Search function
            }
        ).then(
            () => {console.log(games)}
        )
    }

<<<<<<< HEAD

    React.useEffect(() => {
        getAllGames();
    }, [])


=======
>>>>>>> parent of 85a8f3a... Data properly retrieved in Home, ListOfGames and Games work, starting on Search function
    return ( 
        <div className="home">
            {/* add search bar */}
            <button onClick={getAllGames}>Fetch</button>
<<<<<<< HEAD
            <ListOfGames games={games} notes={notes}/>
=======
            {/* <ListOfGames searchTerm="" games={games} notes={notes}/> */}
>>>>>>> parent of 85a8f3a... Data properly retrieved in Home, ListOfGames and Games work, starting on Search function
        </div>
     );
}
 
export default Home;