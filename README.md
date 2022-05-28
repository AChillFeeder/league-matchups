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

### Settings
- [ ] Allow the user to set his theme in the settings

### Stats 
Calculate and show stats in clear numbers and pretty graphs
For recorded games:
- [ ] general winrate
- [ ] winrate on champion
- [ ] worst general matchup
- [ ] best general matchup
- [ ] winrate improvement over time
- [ ] matchup winrate improvement over time

### Search 
Search bar in home screen to filter through previous games, filter by:
- [x] champion name
<br />

- [x] Remove interactions with Community Dragon Api from React and into Flask
- [x] Use CD Api instead of raw data
- [x] Build tests
- [x] Spread classes into multiple files
- [x] patch should be updated automatically
- [x] show past notes of the matchup/champion on live game screen
- [x] notes should a "popularity" attribute
- [ ] limit number of notes shown based on settings 
- [ ] get some basic stats going on the stats page
- [ ] some basic settings on settings page
- [ ] advanced search, specify keywords (search by opponent Champion...) searcheable_keywords = {"all":..., "champions":...}
- [ ] decorator for login and session purposes
- [ ] spread player.py methods into more files
- [ ] audio notes
- [ ] pepper and salt the password hash
- [ ] Email sign up and account confirmation
<br />

## Next direction:
A bit ambitious but try to turn it into a sort of social experience, notes can be public and other users can vote on the ones they like.
This way you can find relevant information about matchups you're first-timing, or maybe correct wrong conclusions.
Also it would be necessary to somehow comfirm your league account when making a league matchups account.
