import { useHistory } from 'react-router';
import PreviousGames from './previousGames/PreviousGames.js';
import useFetch from './usables/useFetch.js';
import {ReactSession} from 'react-client-session';

const Home = () => {

    const {data: profile, isLoading, error} = useFetch(`http://localhost/gamesHistory`);


    return ( 
        <div className="home">
            {error && <p>Error: {error}</p>}
            {profile && <PreviousGames games={profile["games"]}/>}
        </div>
     );
}
 
export default Home;