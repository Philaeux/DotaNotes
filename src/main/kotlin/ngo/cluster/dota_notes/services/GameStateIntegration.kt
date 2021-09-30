/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.services

/**
 * Main JSON Object sent to the endpoint by a POST request
 * @property[provider] Data about the application being run
 * @property[map] Data about the game being played
 * @property[player] Data about the players connected to the game
 */
data class GSIGameState(
    var provider: GSIProvider = GSIProvider(),
    var map: GSIMap = GSIMap(),
    var player: GSIPlayers = GSIPlayers(),
)

/**
 * Information about the game running
 * @property[name] Always 'dota2'
 * @property[appid] Always '570'
 * @property[version] Dota version runninng
 * @property[timestamp] Timestamp the JSON was sent at
 */
data class GSIProvider(
    var name: String = "",
    var appid: Int = 0,
    var version: Int = 0,
    var timestamp: Int = 0
)

/**
 * Information about the match being played
 * @property[name] Name of the map
 * @property[matchid] Unique match identifier
 * @property[game_time] In game time
 * @property[game_state] State the game is in
 * @property[win_team] Team that won the game
 * @property[customgamename] Name of the custom game if one is played
 */
data class GSIMap(
    var name: String = "start",
    var matchid: String = "",
    var game_time: Int = 0,
    var game_state: String = "",
    var win_team: String = "none",
    var customgamename: String = "",
)

/**
 * Team compositions, only available when obs
 * @property[team2] Radiant
 * @property[team3] Dire
 */
data class GSIPlayers(
    var team2: GSIPlayersRadiant? = null,
    var team3: GSIPlayersDire? = null
)

/**
 * Radiant team composition
 * @property[player0] Blue player
 * @property[player1] Teal player
 * @property[player2] Purple player
 * @property[player3] Yellow player
 * @property[player4] Orange player
 */
data class GSIPlayersRadiant(
    var player0: GSIPlayerInfo = GSIPlayerInfo(),
    var player1: GSIPlayerInfo = GSIPlayerInfo(),
    var player2: GSIPlayerInfo = GSIPlayerInfo(),
    var player3: GSIPlayerInfo = GSIPlayerInfo(),
    var player4: GSIPlayerInfo = GSIPlayerInfo(),
)

/**
 * Dire team composition
 * @property[player5] Pink player
 * @property[player6] Olive player
 * @property[player7] SkyBlue player
 * @property[player8] Green player
 * @property[player9] Brown player
 */
data class GSIPlayersDire(
    var player5: GSIPlayerInfo = GSIPlayerInfo(),
    var player6: GSIPlayerInfo = GSIPlayerInfo(),
    var player7: GSIPlayerInfo = GSIPlayerInfo(),
    var player8: GSIPlayerInfo = GSIPlayerInfo(),
    var player9: GSIPlayerInfo = GSIPlayerInfo(),
)

/**
 * A player in a team
 * @property[steamid] 64bit steam identifier
 * @property[name] Current steam name of the player
 */
data class GSIPlayerInfo(
    var steamid: String = "",
    var name: String = "",
)
