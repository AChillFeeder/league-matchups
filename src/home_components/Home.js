
import React from 'react';
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";
import {HTTPget} from "../usables/EasyHTTP";
import ListOfGames from './ListOfGames';

const Home = () => {

    const [games, setGames] = React.useState([]);
    const [notes, setNotes] = React.useState([]);
    const [searchTerm, setSearchTerm] = React.useState("");
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

    const handleSearch = (event) => {
        setSearchTerm(event.target.value);
    }

    React.useEffect(() => console.log(searchTerm), [searchTerm])

    return ( 
        <div className="home">
            {/* add search bar */}
            <input type="text" id="search-bar" onChange={handleSearch} value={searchTerm}/>
            <button onClick={getAllGames}>Fetch</button>
            {isLoading ? <p>Loading...</p> : <ListOfGames games={games} notes={notes} searchTerm={searchTerm}/>}
        </div>
     );
}
 
export default Home;