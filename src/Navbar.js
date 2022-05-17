import {Link, useHistory} from 'react-router-dom';
import {ReactSession} from 'react-client-session';

const Navbar = () => {
    return ( 
        <div className="nav-bar">
            <h1>League matchups</h1>
            <ul>
                <Link to='/home'>Home</Link>
                <Link to='/currentGame'>Current game</Link>
                <Link to='/home'>Stats</Link>
                <Link to='/home'>Settings</Link>
                <Link to='/'>log out</Link>
            </ul>
        </div>
     );
}
 
export default Navbar;