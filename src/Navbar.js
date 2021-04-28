import {Link, useHistory} from 'react-router-dom';
import {ReactSession} from 'react-client-session';

const Navbar = () => {
    return ( 
        <div className="nav-bar">
            <h1>League matchups</h1>
            <ul>
                <Link to='/home'>Home</Link>
                <Link to='/new-game'>New game</Link>
                <Link to='/' onClick={() => ReactSession.set("summonerName", null)}>log out</Link>
            </ul>
        </div>
     );
}
 
export default Navbar;