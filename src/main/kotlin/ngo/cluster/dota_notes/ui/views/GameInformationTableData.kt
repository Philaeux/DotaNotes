/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.ui.views

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material.Divider
import androidx.compose.material.Icon
import androidx.compose.material.Text
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Person
import androidx.compose.material.icons.outlined.Warning
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import ngo.cluster.dota_notes.Player
import ngo.cluster.dota_notes.ui.*
import ngo.cluster.dota_notes.ui.components.VerticalCellDivider

/** Team details = 5 rows */
@Composable
fun gameInformationTableTeam(
    teamName: String,
    team: Array<Player>
) {
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
                gameInformationTablePlayer(player)
                if (teamIterator.hasNext()) {
                    Divider(Modifier.fillMaxWidth().width(1.dp))
                }
            }
        }
    }
}

/** Player details = one row */
@Composable
fun gameInformationTablePlayer(player: Player) {
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

        VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

        VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

        VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

        VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

        VerticalCellDivider(8.dp, 8.dp, 1.dp)

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
                            painter = painterResource("images/languages/en.png"),
                            contentDescription = null
                        )
                    }
                if ("ru" in player.stratzLanguages.value)
                    Column(modifier = Modifier.padding(8.dp, 0.dp, 8.dp, 0.dp)) {
                        Image(
                            painter = painterResource("images/languages/ru.png"),
                            contentDescription = null
                        )
                    }
                if ("fr" in player.stratzLanguages.value)
                    Column(modifier = Modifier.padding(8.dp, 0.dp, 8.dp, 0.dp)) {
                        Image(
                            painter = painterResource("images/languages/fr.png"),
                            contentDescription = null
                        )
                    }
            }
        }

        VerticalCellDivider(8.dp, 8.dp, 1.dp)
    }
}
