
import React from 'react';
import ENVIRONMENT_VARIABLES from "./ENVIRONMENT_VARIABLES.json";
import {HTTPget, HTTPpost} from "./EasyHTTP";
import ListOfGames from './ListOfGames';

const Home = () => {

    const [games, setGames] = React.useState([]);
    const [notes, setNotes] = React.useState([]);
    const [isLoading, setIsLoading] = React.useState(true);
    const [searchTerm, setSearchTerm] = React.useState("");

    const getAllGames = () => {
        setIsLoading(true)
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/gamesHistory`)
        .then( data => {
                setGames(data[0])
                setNotes(data[1])
                setIsLoading(false);
            }
        )

        .then( () => {
            console.log(games);
            console.log(notes)
        }

        )
    }

    const handleSearch = event => {
        setSearchTerm(event.target.value);
    }


    React.useEffect(() => {
        getAllGames();
    }, [])


    return ( 
        <div className="home">
            <button onClick={getAllGames}>Fetch</button>
            <input type="text" id="search_bar" placeholder='search...' onChange={handleSearch} value={searchTerm}/>
            {isLoading ? <p>Loading...</p> : <ListOfGames games={games} notes={notes} />}
        </div>
    );
}
 
export default Home;