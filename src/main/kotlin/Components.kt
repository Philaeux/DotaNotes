import androidx.compose.foundation.BoxWithTooltip
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Person
import androidx.compose.material.icons.outlined.Warning
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.launch

const val playerSteamNameWidth = 350
const val playerProNameWidth = 175
const val behaviorWidth = 80
const val matchCountWidth = 80
const val languagesWidth = 150

@Composable
fun applicationInterface(applicationState: ApplicationState) {
    Column(
        modifier = Modifier
            .fillMaxHeight()
            .fillMaxWidth(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
    ) {
        if (applicationState.gameId.value != "0") {
            Row(
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "Game ${applicationState.gameId.value}",
                    fontSize = 17.sp,
                    modifier = Modifier
                        .padding(8.dp, 0.dp, 8.dp, 0.dp)
                )

                val coroutineScope = rememberCoroutineScope()
                Spacer(modifier = Modifier.size(12.dp))
                Button(
                    onClick =
                    {
                        coroutineScope.launch {
                            applicationState.updateWithStratz()
                        }
                    }
                ) {
                    Text(text = "Stratz")
                }
            }
            Spacer(modifier = Modifier.size(12.dp))
            Card(
                modifier = Modifier
                    .width(1400.dp)
                    .height(IntrinsicSize.Min)
                    .padding(16.dp),
                elevation = 6.dp
            ) {
                Column {
                    // Header
                    Row(
                        Modifier
                            .height(IntrinsicSize.Min)
                    ) {
                        Text(
                            modifier = Modifier.width(40.dp),
                            fontSize = 20.sp,
                            text = " "
                        )
                        Divider(Modifier.fillMaxHeight().width(2.dp), color = Color(0x00000000))
                        Column(Modifier.padding(4.dp)) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(50.dp)
                                    .padding(8.dp)
                            ) {
                                BoxWithTooltip(
                                    tooltip = {
                                        Surface(
                                            shape = MaterialTheme.shapes.small,
                                            color = MaterialTheme.colors.secondary
                                        )
                                        {
                                            Text(
                                                modifier = Modifier.padding(6.dp),
                                                text = "Profile status\n\n" +
                                                        "Blue = Not Fetched\n" +
                                                        "Red = Private\n" +
                                                        "Green = Public"
                                            )
                                        }
                                    }) {
                                    Icon(
                                        imageVector = Icons.Outlined.Person,
                                        contentDescription = null,
                                        tint = Color(0xff1976d2)
                                    )
                                }
                                Spacer(modifier = Modifier.size(16.dp))
                                BoxWithTooltip(
                                    tooltip = {
                                        Surface(
                                            shape = MaterialTheme.shapes.small,
                                            color = MaterialTheme.colors.secondary
                                        )
                                        {
                                            Text(
                                                modifier = Modifier.padding(6.dp),
                                                text = "Stratz smurf detection\n\n" +
                                                        "Blue = 1\n" +
                                                        "Yellow = 2\n" +
                                                        "Orange = 3\n" +
                                                        "Red = 4"
                                            )
                                        }
                                    }) {
                                    Icon(
                                        imageVector = Icons.Outlined.Warning,
                                        contentDescription = null,
                                        tint = Color(0xff000000)
                                    )
                                }

                                Spacer(modifier = Modifier.size(16.dp))
                                Divider(Modifier.fillMaxHeight().width(1.dp))
                                Spacer(modifier = Modifier.size(8.dp))

                                Column(
                                    modifier = Modifier
                                        .width(playerSteamNameWidth.dp)
                                        .height(IntrinsicSize.Min),
                                    horizontalAlignment = Alignment.CenterHorizontally
                                ) {
                                    Text(
                                        text = "Player Steam Name",
                                        fontSize = 17.sp
                                    )
                                }

                                Spacer(modifier = Modifier.size(8.dp))
                                Divider(Modifier.fillMaxHeight().width(1.dp))
                                Spacer(modifier = Modifier.size(8.dp))

                                Column(
                                    modifier = Modifier
                                        .width(playerProNameWidth.dp)
                                        .height(IntrinsicSize.Min),
                                    horizontalAlignment = Alignment.CenterHorizontally
                                ) {
                                    Text(
                                        text = "Pro/Custom Name",
                                        fontSize = 17.sp
                                    )
                                }

                                Spacer(modifier = Modifier.size(8.dp))
                                Divider(Modifier.fillMaxHeight().width(1.dp))
                                Spacer(modifier = Modifier.size(8.dp))

                                Column(
                                    modifier = Modifier
                                        .width(behaviorWidth.dp)
                                        .height(IntrinsicSize.Min),
                                    horizontalAlignment = Alignment.CenterHorizontally
                                ) {
                                    Text(
                                        text = "Behavior",
                                        fontSize = 17.sp
                                    )
                                }

                                Spacer(modifier = Modifier.size(8.dp))
                                Divider(Modifier.fillMaxHeight().width(1.dp))
                                Spacer(modifier = Modifier.size(8.dp))

                                // Games
                                Column(
                                    modifier = Modifier
                                        .width(matchCountWidth.dp)
                                        .height(IntrinsicSize.Min),
                                    horizontalAlignment = Alignment.CenterHorizontally
                                ) {
                                    Text(
                                        text = "Games",
                                        fontSize = 17.sp
                                    )
                                }

                                Spacer(modifier = Modifier.size(8.dp))
                                Divider(Modifier.fillMaxHeight().width(1.dp))
                                Spacer(modifier = Modifier.size(8.dp))

                                // Languages
                                Column(
                                    modifier = Modifier
                                        .width(languagesWidth.dp)
                                        .height(IntrinsicSize.Min),
                                    horizontalAlignment = Alignment.CenterHorizontally
                                ) {
                                    Text(
                                        text = "Languages",
                                        fontSize = 17.sp
                                    )
                                }

                                Spacer(modifier = Modifier.size(8.dp))
                                Divider(Modifier.fillMaxHeight().width(1.dp))
                                Spacer(modifier = Modifier.size(8.dp))
                            }
                        }

                    }

                    // Content
                    Divider(Modifier.fillMaxWidth().height(2.dp))
                    teamInfo("Radiant", applicationState.radiant)
                    Divider(Modifier.fillMaxWidth().height(2.dp))
                    teamInfo("Dire", applicationState.dire)
                }
            }
        } else {
            Text(
                text = "Waiting game detection...",
                modifier = Modifier
                    .padding(8.dp, 0.dp, 8.dp, 0.dp)
            )
        }
    }
}


@Composable
fun teamInfo(teamName: String, team: Array<Player>) {
    Row(
        Modifier.height(IntrinsicSize.Min)
    ) {
        Column(
            modifier = Modifier
                .fillMaxHeight()
                .width(40.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            for (c in teamName) {
                Text(
                    fontSize = 20.sp,
                    text = "${c.uppercaseChar()}"
                )
            }
        }
        Divider(Modifier.fillMaxHeight().width(2.dp))
        Column(Modifier.padding(4.dp)) {
            val teamIterator = team.iterator()
            while (teamIterator.hasNext()) {
                val player = teamIterator.next()
                playerInfo(player)
                if (teamIterator.hasNext()) {
                    Divider(Modifier.fillMaxWidth().width(1.dp))
                }
            }
        }
    }
}

@Composable
fun playerInfo(player: Player) {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier
            .fillMaxWidth()
            .height(50.dp)
            .padding(8.dp)
    ) {
        // Profile anonymous status
        val personColor: Color = when (player.isAnonymous.value) {
            null -> Color(0xff1976d2)
            true -> Color(0xffc62828)
            false -> Color(0xff388e3c)
        }
        Icon(
            imageVector = Icons.Outlined.Person,
            contentDescription = null,
            tint = personColor
        )
        Spacer(modifier = Modifier.size(16.dp))

        // Smurf detection
        val smurfColor: Color = when (player.smurfFlag.value) {
            1 -> Color(0xff1976d2)
            2 -> Color(0xfffdd835)
            3 -> Color(0xffffb300)
            4 -> Color(0xffc62828)
            else -> Color(0x00000000)
        }
        Icon(
            imageVector = Icons.Outlined.Warning,
            contentDescription = null,
            tint = smurfColor
        )


        Spacer(modifier = Modifier.size(16.dp))
        Divider(Modifier.fillMaxHeight().width(1.dp))
        Spacer(modifier = Modifier.size(8.dp))

        // Current Steam name
        Column(
            modifier = Modifier
                .width(playerSteamNameWidth.dp)
                .height(IntrinsicSize.Min),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(
                text = player.currentName.value,
                fontSize = 17.sp
            )
        }

        Spacer(modifier = Modifier.size(8.dp))
        Divider(Modifier.fillMaxHeight().width(1.dp))
        Spacer(modifier = Modifier.size(8.dp))

        // Pro Name
        Column(
            modifier = Modifier
                .width(playerProNameWidth.dp)
                .height(IntrinsicSize.Min),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(
                text = player.name.value,
                fontSize = 17.sp
            )
        }

        Spacer(modifier = Modifier.size(8.dp))
        Divider(Modifier.fillMaxHeight().width(1.dp))
        Spacer(modifier = Modifier.size(8.dp))

        // Behavior
        Column(
            modifier = Modifier
                .width(behaviorWidth.dp)
                .height(IntrinsicSize.Min),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            if (player.isAnonymous.value == false) {
                Text(
                    text = player.behaviorScore.value.toString(),
                    fontSize = 17.sp
                )
            }
        }

        Spacer(modifier = Modifier.size(8.dp))
        Divider(Modifier.fillMaxHeight().width(1.dp))
        Spacer(modifier = Modifier.size(8.dp))

        // Games
        Column(
            modifier = Modifier
                .width(matchCountWidth.dp)
                .height(IntrinsicSize.Min),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            if (player.isAnonymous.value == false) {
                Text(
                    text = "${player.matchCount.value}",
                    fontSize = 17.sp
                )
            }
        }

        Spacer(modifier = Modifier.size(8.dp))
        Divider(Modifier.fillMaxHeight().width(1.dp))
        Spacer(modifier = Modifier.size(8.dp))

        // Languages
        Column(
            modifier = Modifier
                .width(languagesWidth.dp)
                .height(40.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Row {
                if ("en" in player.stratzLanguages.value)
                    Column(modifier = Modifier.padding(8.dp, 0.dp, 8.dp, 0.dp)) {
                        Image(
                            painter = painterResource("languages/en.png"),
                            contentDescription = null
                        )
                    }
                if ("ru" in player.stratzLanguages.value)
                    Column(modifier = Modifier.padding(8.dp, 0.dp, 8.dp, 0.dp)) {
                        Image(
                            painter = painterResource("languages/ru.png"),
                            contentDescription = null
                        )
                    }
                if ("fr" in player.stratzLanguages.value)
                    Column(modifier = Modifier.padding(8.dp, 0.dp, 8.dp, 0.dp)) {
                        Image(
                            painter = painterResource("languages/fr.png"),
                            contentDescription = null
                        )
                    }
            }
        }

        Spacer(modifier = Modifier.size(8.dp))
        Divider(Modifier.fillMaxHeight().width(1.dp))
        Spacer(modifier = Modifier.size(8.dp))
    }
}
