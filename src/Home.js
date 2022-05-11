

const Home = () => {
    return ( 
        <div className="home">
            {error && <p>Error: {error}</p>}
            {profile && <PreviousGames/>}
        </div>
     );
}
 
export default Home;