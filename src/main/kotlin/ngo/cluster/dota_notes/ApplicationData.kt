/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes

import ngo.cluster.dota_notes.services.GSIGameState
import ngo.cluster.dota_notes.services.StratzPlayer
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.mutableStateOf
import io.ktor.client.*
import io.ktor.client.engine.jetty.*
import io.ktor.client.features.json.*
import io.ktor.client.request.*
import serverLogJoinRegex
import serverLogSteamIdRegex
import steamIdTo32bits
import java.io.File

object ApplicationData {
    var gameId: MutableState<String> = mutableStateOf("0")
    val radiant: Array<Player> = arrayOf(Player(), Player(), Player(), Player(), Player())
    val dire: Array<Player> = arrayOf(Player(), Player(), Player(), Player(), Player())

    private val httpClient = HttpClient(Jetty) {
        install(JsonFeature) {
            serializer = GsonSerializer()
        }
    }

    /**
     *
     */
    fun readFromLog(logFile: File) {
        val log = logFile.readLines()
        val playerLog = log.lastOrNull { serverLogJoinRegex.matches(it) }
        if (playerLog != null) {
            val players = serverLogSteamIdRegex
                .findAll(playerLog)
                .map { it.value.subSequence(1, it.value.length - 1) }
                .toList()
            radiant[0].setSteamId(players[0].toString().substring(4))
            radiant[1].setSteamId(players[1].toString().substring(4))
            radiant[2].setSteamId(players[2].toString().substring(4))
            radiant[3].setSteamId(players[3].toString().substring(4))
            radiant[4].setSteamId(players[4].toString().substring(4))
            dire[0].setSteamId(players[5].toString().substring(4))
            dire[1].setSteamId(players[6].toString().substring(4))
            dire[2].setSteamId(players[7].toString().substring(4))
            dire[3].setSteamId(players[8].toString().substring(4))
            dire[4].setSteamId(players[9].toString().substring(4))
        }
    }

    /**
     *
     */
    fun readFromGSI(gsiGameState: GSIGameState) {
        if (gsiGameState.map.matchid != "")
            gameId.value = gsiGameState.map.matchid
        if (gsiGameState.player.team2 != null) {
            radiant[0].setSteamId(steamIdTo32bits(gsiGameState.player.team2!!.player0.steamid))
            radiant[1].setSteamId(steamIdTo32bits(gsiGameState.player.team2!!.player1.steamid))
            radiant[2].setSteamId(steamIdTo32bits(gsiGameState.player.team2!!.player2.steamid))
            radiant[3].setSteamId(steamIdTo32bits(gsiGameState.player.team2!!.player3.steamid))
            radiant[4].setSteamId(steamIdTo32bits(gsiGameState.player.team2!!.player4.steamid))
        }
        if (gsiGameState.player.team3 != null) {
            dire[0].setSteamId(steamIdTo32bits(gsiGameState.player.team3!!.player5.steamid))
            dire[1].setSteamId(steamIdTo32bits(gsiGameState.player.team3!!.player6.steamid))
            dire[2].setSteamId(steamIdTo32bits(gsiGameState.player.team3!!.player7.steamid))
            dire[3].setSteamId(steamIdTo32bits(gsiGameState.player.team3!!.player8.steamid))
            dire[4].setSteamId(steamIdTo32bits(gsiGameState.player.team3!!.player9.steamid))
        }
    }

    suspend fun updateWithStratz() {
        (radiant + dire).forEach {
            if (it.steamId.value != 0) {
                val info: StratzPlayer =
                    httpClient.get("https://api.stratz.com/api/v1/Player/${it.steamId.value}")
                println(info)
                it.currentName.value = info.steamAccount.name
                it.isAnonymous.value = info.steamAccount.isAnonymous
                it.matchCount.value = info.matchCount
                it.winCount.value = info.winCount
                it.behaviorScore.value = info.behaviorScore
                it.smurfFlag.value = info.steamAccount.smurfFlag
                if (info.steamAccount.proSteamAccount != null) {
                    it.name.value = info.steamAccount.proSteamAccount.name
                }
                if (info.languageCode != null) {
                    it.stratzLanguages.value =
                        info.languageCode.filter { listOf("en", "fr", "ru").contains(it) }.joinToString(" ")
                }
            }
        }
    }
}

/**
 * A Dota Player information stored into the ApplicationData
 * @param[steamId] 32bit steam identifier
 * @param[name] Pro dota name or custom user name
 * @param[currentName] Current steam name
 * @param[isAnonymous]
 */
class Player(
    var steamId: MutableState<Int> = mutableStateOf(0),
    var name: MutableState<String> = mutableStateOf(""),
    var currentName: MutableState<String> = mutableStateOf(""),
    var isAnonymous: MutableState<Boolean?> = mutableStateOf(null),
    var matchCount: MutableState<Int> = mutableStateOf(0),
    var winCount: MutableState<Int> = mutableStateOf(0),
    var behaviorScore: MutableState<Int> = mutableStateOf(0),
    var smurfFlag: MutableState<Int> = mutableStateOf(0),
    var stratzLanguages: MutableState<String> = mutableStateOf("")
) {
    fun setSteamId(newSteamId: Int) {
        if (newSteamId != steamId.value) {
            steamId.value = newSteamId
            name.value = ""
            currentName.value = ""
            isAnonymous.value = null
            matchCount.value = 0
            winCount.value = 0
            behaviorScore.value = 0
            smurfFlag.value = 0
            stratzLanguages.value = ""
        }
    }

    fun setSteamId(newSteamId: String) {
        setSteamId(newSteamId.toInt())
    }

}
