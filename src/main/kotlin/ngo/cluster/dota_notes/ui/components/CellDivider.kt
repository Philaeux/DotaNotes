/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.ui.components

import androidx.compose.foundation.layout.*
import androidx.compose.material.Divider
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp

@Composable
fun VerticalCellDivider(
    leftPadding: Dp,
    rightPadding: Dp,
    dividerWidth: Dp
) {
    Spacer(modifier = Modifier.size(leftPadding))
    Divider(Modifier.fillMaxHeight().width(dividerWidth))
    Spacer(modifier = Modifier.size(rightPadding))
}
