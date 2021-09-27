/**
 * Data classes mirroring JSON object returned by Game State Integration (GSI)
 * Nullable fields are null when playing, and filled when obs, it's a cheat protection
 * @see [GSI Doc][https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration]
 * @see [Lib Example][https://github.com/xzion/dota2-gsi#clients-and-events]
 */

/**
 * Main JSON Object sent to the endpoint by a POST request
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
 */
data class GSIProvider(
    var name: String = "",
    var appid: Int = 0,
    var version: Int = 0,
    var timestamp: Int = 0
)

/**
 * Information about the match played
 */
data class GSIMap(
    var name: String = "start",
    var matchid: String = "",
    var game_time: Int = 0,
    var clock_time: Int = 0,
    var daytime: Boolean = false,
    var nightstalker_night: Boolean = false,
    var game_state: String = "",
    var paused: Boolean = false,
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
 */
data class GSIPlayerInfo(
    var steamid: String = "",
    var name: String = "",
    var team_name: String = ""
)
