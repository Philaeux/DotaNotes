import java.io.File

/**
 * Transform a 32bits Steam identifier to a 64bits Steam identifier
 *
 * @param[steamId] 32bits Steam identifier
 * @return Steam 64bits identifier
 */
fun steamIdTo64bits(steamId: Int): Long {
    return 76561197960265728 + steamId.toLong()
}

/**
 * Transform a 64bits Steam identifier to a 32bits Steam identifier
 *
 * @param[steamId] 64bits Steam identifier
 * @return 32bits Steam identifier
 */
fun steamIdTo32bits(steamId: Long): Int {
    val temp = steamId - 76561197960265728
    return temp.toInt()
}
fun steamIdTo32bits(steamId: String): Int {
    return steamIdTo32bits(steamId.toLong())
}

// TODO: Replace with registry path check
const val serverLogURI: String = "E:\\Steam\\steamapps\\common\\dota 2 beta\\game\\dota\\server_log.txt"
val serverLogFile: File = File(serverLogURI)
var serverLogJoinRegex = Regex("""\d+/\d+/\d+ - \d+:\d+:\d+: =\[A:\d+:\d+:\d+] \(Lobby \d+ \w+ 0:\[U:\d+:\d+] 1:\[U:\d+:\d+] 2:\[U:\d+:\d+] 3:\[U:\d+:\d+] 4:\[U:\d+:\d+] 5:\[U:\d+:\d+] 6:\[U:\d+:\d+] 7:\[U:\d+:\d+] 8:\[U:\d+:\d+] 9:\[U:\d+:\d+]\) .*""")
var serverLogSteamIdRegex = Regex("""\[U:\d:\d+]""")
