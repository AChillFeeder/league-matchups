const ChampionPortrait = ({championName}) => {
    let additive = '';
    switch (championName){
        case 'aphelios':
            additive = '.aphelios'
            break
        case 'viego':
            additive = '.ruinedking'
            break
        case 'gwen':
            additive = '_0.gwen'
            break
        case 'volibear':
            additive = '.voli'
            break
    }
    return ( 
        <div className="champion-portrait">
            <img src={`https://raw.communitydragon.org/${window.patch}/game/assets/characters/${championName}/skins/base/${championName}loadscreen${additive}.png`} alt=""/>
        </div>
     );
}
 
export default ChampionPortrait;