# LEAGUE MATCHUPS
A simple flask/react app that allows you to type notes about your matchup, the goal is to improve by slowly and surely building a vast knowledge about how to adapt to your opposing champions and how to avoid redundant mistakes and wasted opportunities. 
<br />
<br />
League matchups finds your current game and asks you to pick the champion you're laning against, you could then add notes through your games and review them once it's over, all your previous games will be visible in yout home screen.

<br />
<br />

# Screenshots:
## Login screen
![Screenshot of the home screen](https://raw.githubusercontent.com/AChillFeeder/league-matchups/main/screenshots/login_screen.png)
## Home screen
![Screenshot of the home screen](https://raw.githubusercontent.com/AChillFeeder/league-matchups/main/screenshots/home_screen.png)
## Champion choice at the start of the game
![Screenshot of the home screen](https://raw.githubusercontent.com/AChillFeeder/league-matchups/main/screenshots/champion_choice.png)
## Taking notes in-game
![Screenshot of the home screen](https://raw.githubusercontent.com/AChillFeeder/league-matchups/main/screenshots/notes_form.png)
## Home screen after the changes
![Screenshot of the home screen](https://raw.githubusercontent.com/AChillFeeder/league-matchups/main/screenshots/home_screen2.png)

## Next features 

### Tags 
- [x] Using @ or # (or settings), allow the user to dynamically add tags.
- [ ] ~~(scraped) Users can choose tags for notes from a dropdown menu to save time.~~

### Settings
- [ ] Allow the user to set his theme in the settings


### Stats 
Calculate and show stats in clear numbers and pretty graphs
- [x] general winrate
- [ ] winrate on champion
- [ ] worst general matchup
- [ ] best general matchup
- [ ] most used tags
- [ ] least used tags
- [ ] winrate improvement over time
- [ ] matchup winrate improvement over time

### Search 
Search bar in home screen to filter through previous games, filter by:
- [ ] champion name
- [ ] note
- [ ] tag
<br />

- [ ] Remove interactions with Community Dragon Api from React and into Flask
- [ ] Use CD Api instead of raw data
- [ ] Build tests
- [ ] Spread classes into multiple files
- [ ] Extensive use of Exceptions

- [ ] patch should be updated automatically
- [ ] move champion_{patch}.json file to data

- [ ] Email sign up and account comfirmation
<br />

## Next direction:
A bit ambitious but try to turn it into a sort of social experience, notes can be public and other users can vote on the ones they like.
This way you can find relevant information about matchups you're first-timing, or maybe correct wrong conclusions.
Also it would be necessary to somehow comfirm your league account when making a league matchups account.
