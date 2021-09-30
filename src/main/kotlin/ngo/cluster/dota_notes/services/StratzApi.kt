/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.services

/**
 * Stratz JSON data sent from the player endpoint
 * @see https://api.stratz.com/api/v1/Player/{id}
 * @property[steamAccount] Detailed data about the steam account
 * @property[winCount] Number of wins done
 * @property[matchCount] Number of games played
 * @property[behaviorScore] Behavior score associated
 * @property[languageCode] Languages spoken
 */
data class StratzPlayer(
    val steamAccount: StratzSteamAccount,
    val winCount: Int,
    val matchCount: Int,
    val behaviorScore: Int,
    val languageCode: List<String>?,
)

/**
 * Data about the Steam account of a player
 * @property[id] 32bits steam identifier
 * @property[name] Current steam name
 * @property[isAnonymous] Shows if Dota APIs will give data or not
 * @property[proSteamAccount] Pro information
 * @property[smurfFlag] Stratz smurf marker
 */
data class StratzSteamAccount(
    val id: Int,
    val name: String,
    val isAnonymous: Boolean,
    val proSteamAccount: StratzProSteamAccount?,
    val smurfFlag: Int,
)

/**
 * Pro details of a Dota account
 * @property[name] Pro player nickname
 */
data class StratzProSteamAccount(
    val name: String
)
