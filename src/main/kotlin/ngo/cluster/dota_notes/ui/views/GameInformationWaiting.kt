/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.ui.views

import androidx.compose.foundation.layout.*
import androidx.compose.material.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

/** View used when there is no Game id, so no game information */
@Composable
fun waitingForGameDetectionView() {
    Text(
        text = "Waiting game detection...",
        modifier = Modifier.padding(8.dp, 0.dp, 8.dp, 0.dp)
    )
}
