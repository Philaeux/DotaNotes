/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.ui.views

import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.launch
import ngo.cluster.dota_notes.ApplicationData

/**
 * Show some data about the game in the header
 * Display a button to update data using Stratz
 */
@Composable
fun gameInformationHeader(applicationData: ApplicationData) {
    Row(
        verticalAlignment = Alignment.CenterVertically
    ) {
        Text(
            text = "Game ${ApplicationData.gameId.value}",
            fontSize = 17.sp,
            modifier = Modifier.padding(8.dp, 0.dp, 8.dp, 0.dp)
        )

        Spacer(modifier = Modifier.size(12.dp))

        // The coroutine is cancelled if view is refreshed
        val stratzCoroutineScope = rememberCoroutineScope()
        Button(onClick =
        {
            stratzCoroutineScope.launch {
                ApplicationData.updateWithStratz()
            }
        }
        ) {
            Text(text = "Stratz")
        }
    }
}
