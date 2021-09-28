
data class StratzPlayer(
    val steamAccount: StratzSteamAccount,
    val winCount: Int,
    val matchCount: Int,
    val behaviorScore: Int,
    val languageCode: List<String>?,
)

data class StratzSteamAccount(
    val id: Int,
    val name: String,
    val isAnonymous: Boolean,
    val proSteamAccount: StratzProSteamAccount?,
    val smurfFlag: Int,
)

data class StratzProSteamAccount(
    val name: String
)
