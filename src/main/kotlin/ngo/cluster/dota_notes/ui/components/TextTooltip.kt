/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.ui.components

import androidx.compose.foundation.BoxWithTooltip
import androidx.compose.foundation.layout.padding
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Surface
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp


/**
 * Simple tooltip containing only text, using material default Theme
 * @param[tooltip] Text to write on the tooltip
 * @param[content] Content getting tooltiped
 */
@Composable
fun TextTooltip(
    tooltip: String,
    content: @Composable () -> Unit
) {
    BoxWithTooltip(
        tooltip = {
            Surface(
                shape = MaterialTheme.shapes.small,
                color = MaterialTheme.colors.secondary
            ) {
                Text(
                    modifier = Modifier.padding(6.dp),
                    color = MaterialTheme.colors.onSecondary,
                    text = tooltip
                )
            }
        }) {
        content()
    }
}
