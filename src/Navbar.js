import {Link} from 'react-router-dom';

const Navbar = () => {
    return ( 
        <div className="nav-bar">
            <h1>League matchups</h1>
            <ul>
                <Link to='/home'>Home</Link>
                <Link to='/currentGame'>Current game</Link>
                <Link to='/home'>Stats</Link>
                <Link to='/home'>Matchups</Link>
                <Link to='/home'>Settings</Link>
                <Link to='/'>log out</Link>
            </ul>
        </div>
     );
}
 
export default Navbar;