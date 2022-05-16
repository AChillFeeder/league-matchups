
import React from 'react';
import ENVIRONMENT_VARIABLES from "./ENVIRONMENT_VARIABLES.json";
import {HTTPget, HTTPpost} from "./EasyHTTP";
import ListOfGames from './ListOfGames';

const Home = () => {

    const [games, setGames] = React.useState([]);
    const [notes, setNotes] = React.useState([]);
    const [isLoading, setIsLoading] = React.useState(true);

    const getAllGames = () => {
        setIsLoading(true);
        console.log("fetching");
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/gamesHistory`)
        .then( data => {
                console.log(data);
                setGames(data[0]);
                setNotes(data[1]);
                setIsLoading(false);
            }
        )
    }
    
    React.useEffect(() => {
        getAllGames();
    }, [])

    React.useEffect(() => {
        console.log(notes)
    }, [isLoading])

    return ( 
        <div className="home">
            {/* add search bar */}
            <button onClick={getAllGames}>Fetch</button>
            {isLoading ? <p>Loading...</p> : <ListOfGames games={games} notes={notes} />}
        </div>
     );
}
 
export default Home;