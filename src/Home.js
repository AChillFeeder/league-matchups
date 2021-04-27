import { useHistory } from 'react-router';
import PreviousGames from './previousGames/PreviousGames.js';
import useFetch from './usables/useFetch.js';
import {ReactSession} from 'react-client-session';

const Home = () => {

    // don't forget to change region
    
    window.patch = "11.8";
    var summonerName = ReactSession.get("summonerName");

    let history = useHistory();

    if (!summonerName){
        history.push('/'); // send back to the login screen
    }
    
    console.log('Home page summoner name: ' + summonerName)

    const {data: profile, isLoading, error} = useFetch(`http://192.168.1.150:8000/${summonerName}/games`);


    return ( 
        <div className="home">
            {error && <p>Error: {error}</p>}
            {profile && <PreviousGames games={profile["games"]}/>}
        </div>
     );
}
 
export default Home;