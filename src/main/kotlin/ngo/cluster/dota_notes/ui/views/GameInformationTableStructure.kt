/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

import androidx.compose.foundation.layout.*
import androidx.compose.material.Card
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
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import ngo.cluster.dota_notes.ApplicationData
import ngo.cluster.dota_notes.ui.*
import ngo.cluster.dota_notes.ui.components.TextTooltip
import ngo.cluster.dota_notes.ui.components.VerticalCellDivider
import ngo.cluster.dota_notes.ui.views.gameInformationTableTeam

/**
 * Show player information in the form of a table.
 * Table with a header then one player per row, with some
 */
@Composable
fun gameInformationTable(applicationData: ApplicationData) {
    Card(
        modifier = Modifier
            .width(1400.dp)
            .height(IntrinsicSize.Min)
            .padding(16.dp),
        elevation = 6.dp
    ) {
        Column {
            gameInformationTableHeader()
            Divider(Modifier.fillMaxWidth().height(2.dp))
            gameInformationTableTeam("Radiant", ApplicationData.radiant)
            Divider(Modifier.fillMaxWidth().height(2.dp))
            gameInformationTableTeam("Dire", ApplicationData.dire)
        }
    }
}

/** First Row of the table, header */
@Composable
fun gameInformationTableHeader() {
    Row(
        modifier = Modifier.height(IntrinsicSize.Min)
    ) {
        Spacer(Modifier.width(42.dp))
        Column(Modifier.padding(4.dp)) {
            Row(
                verticalAlignment = Alignment.CenterVertically,
                modifier = Modifier
                    .fillMaxWidth()
                    .height(50.dp)
                    .padding(8.dp)
            ) {
                TextTooltip(
                    """Profile status
                                      |
                                      |Blue = Not Fetched
                                      |Red = Private
                                      |Green = Public
                                    """.trimMargin()
                ) {
                    Icon(
                        imageVector = Icons.Outlined.Person,
                        contentDescription = null,
                        tint = Color(0xff1976d2)
                    )
                }
                Spacer(modifier = Modifier.size(16.dp))
                TextTooltip(
                    """Stratz smurf detection
                                      |
                                      |
                                    """.trimMargin()
                ) {
                    Icon(
                        imageVector = Icons.Outlined.Warning,
                        contentDescription = null,
                        tint = Color(0xff000000)
                    )
                }

                VerticalCellDivider(16.dp, 8.dp, 1.dp)

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

                VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

                VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

                VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

                VerticalCellDivider(8.dp, 8.dp, 1.dp)

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

                VerticalCellDivider(8.dp, 8.dp, 1.dp)
            }
        }
    }
}
