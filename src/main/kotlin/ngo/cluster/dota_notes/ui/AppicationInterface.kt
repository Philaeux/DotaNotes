/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.ui

import androidx.compose.foundation.layout.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import ngo.cluster.dota_notes.ApplicationData
import ngo.cluster.dota_notes.ui.views.gameInformationHeader
import gameInformationTable
import ngo.cluster.dota_notes.ui.views.waitingForGameDetectionView

const val playerSteamNameWidth = 350
const val playerProNameWidth = 175
const val behaviorWidth = 80
const val matchCountWidth = 80
const val languagesWidth = 150

/** UI Entrypoint, switch according to application state */
@Composable
fun applicationInterface(applicationData: ApplicationData) {
    Column(
        modifier = Modifier
            .fillMaxHeight()
            .fillMaxWidth(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
    ) {
        if (applicationData.gameId.value == "0") {
            waitingForGameDetectionView()
        } else {
            gameInformationHeader(applicationData)
            Spacer(modifier = Modifier.size(12.dp))
            gameInformationTable(applicationData)
        }
    }
}
