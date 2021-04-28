const ChampionThumbnail = ({championName}) => {
    let additive = '';

    let _0ChampionName = ['aphelios', 'gwen', 'yone', 'senna', 'sett', 'lillia']
    if(_0ChampionName.includes(championName)){
        additive = '_0.' + championName
    }
    
    let _0 = ['darius', 'jax', 'leblanc']
    if(_0.includes(championName)){
        additive = '_0'
    }
    
    
    switch (championName){
        case 'viego':
            additive = '.ruinedking'
            break   
        case 'volibear':
            additive = '_0.voli'
            break
        case 'rell':
            additive = '_0.darksupport'
            break
    }

    return ( 

        <div className="champion-thumbnail">
            <img src={`https://raw.communitydragon.org/${window.patch}/game/assets/characters/${championName}/hud/${championName}_circle${additive}.png`} alt=""/>
        </div> 

    );
}
 
export default ChampionThumbnail;