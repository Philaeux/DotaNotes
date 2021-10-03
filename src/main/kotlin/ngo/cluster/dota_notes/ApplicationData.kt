/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes

import androidx.compose.runtime.MutableState
import androidx.compose.runtime.mutableStateOf
import io.ktor.client.*
import io.ktor.client.engine.jetty.*
import io.ktor.client.features.json.*
import io.ktor.client.request.*
import ngo.cluster.dota_notes.ApplicationData.dire
import ngo.cluster.dota_notes.ApplicationData.gameId
import ngo.cluster.dota_notes.ApplicationData.httpClient
import ngo.cluster.dota_notes.ApplicationData.radiant
import ngo.cluster.dota_notes.services.*
import java.io.File


/**
 * Singleton holding application data
 * @property[gameId] Current game Identifier
 * @property[radiant] Data about the Radiant players
 * @property[dire] Data about the Dire players
 * @property[httpClient] Client used to do Stratz API GET request
 */
object ApplicationData {
    var steamPath: MutableState<String> = mutableStateOf("")
    var gameId: MutableState<String> = mutableStateOf("0")
    val radiant: Array<Player> = arrayOf(Player(), Player(), Player(), Player(), Player())
    val dire: Array<Player> = arrayOf(Player(), Player(), Player(), Player(), Player())
    private val httpClient = HttpClient(Jetty) {
        install(JsonFeature) {
            serializer = GsonSerializer()
        }
    }

    init {
        val regValue = """reg query HKCU\Software\Valve\Steam /v SteamPath""".runCommand()
        val keyResult = regValue?.split("\n")?.firstOrNull { it.contains("SteamPath") }
        if (keyResult != null) {
            steamPath.value = keyResult.substring(27)
        }
    }

    /**
     * Update application data using local server_log file
     * @param[logFile] File to read log from
     */
    fun readFromLog(logFile: File) {
        val log = logFile.readLines()
        val playerLog = log.lastOrNull { serverLogJoinRegex.matches(it) }
        if (playerLog != null) {
            val players = serverLogSteamIdRegex
                .findAll(playerLog)
                .map { it.value.subSequence(1, it.value.length - 1) }
                .toList()
            for(i in 0..4) {
                radiant[i].setSteamId(players[i].toString().substring(4))
                dire[i].setSteamId(players[i+5].toString().substring(4))
            }
        }
    }

    /**
     * Update application data using game state integration packet
     * @param[gsiGameState] GSI JSON received on the http Server
     */
    fun readFromGSI(gsiGameState: GSIGameState) {
        if (gsiGameState.map.matchid != "")
            gameId.value = gsiGameState.map.matchid
        if (gsiGameState.player.team2 != null && gsiGameState.player.team3 != null) {
            for (i in 0..4) {
                radiant[i].setSteamId(steamIdTo32bits(gsiGameState.player.team2!!.getPlayer(i).steamid))
                dire[i].setSteamId(steamIdTo32bits(gsiGameState.player.team3!!.getPlayer(i+5).steamid))
            }
        }
    }

    /** Update players data using Stratz API */
    // TODO: secure API call
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
    /**
     * Update the SteamID of a player, reset all related information
     * @param[newSteamId] New player steamId
     */
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

    /**
     * Update the SteamID of a player, reset all related information
     * @param[newSteamId] New player steamId
     */
    fun setSteamId(newSteamId: String) {
        setSteamId(newSteamId.toInt())
    }

}
