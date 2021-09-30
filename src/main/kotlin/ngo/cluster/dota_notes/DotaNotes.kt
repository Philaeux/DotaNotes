/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes

import androidx.compose.material.MaterialTheme
import androidx.compose.material.darkColors
import androidx.compose.material.lightColors
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import applicationInterface
import ngo.cluster.dota_notes.services.HttpServer

/**
 * Application main class
 * @property[themeColors] Colors to apply on the MaterialTheme
 * @property[lightColors] Light color scheme based on themeColors
 * @property[darkColors] Dark color scheme based on themeColors
 * @property[useDarkColors] Selector between light and dark theme
 */
class DotaNotes {
    private val themeColors = object {
        val primary = Color(0xff616161)
        val primaryVariant = Color(0xff455a64)
        val onPrimary = Color(0xffffffff)
        val secondary = Color(0xff1976d2)
        val secondaryVariant = Color(0xff1565c0)
        val onSecondary = Color(0xffffffff)
    }
    private val lightColors = lightColors(
        primary = themeColors.primary,
        primaryVariant = themeColors.primaryVariant,
        onPrimary = themeColors.onPrimary,
        secondary = themeColors.secondary,
        secondaryVariant = themeColors.secondaryVariant,
        onSecondary = themeColors.onSecondary
    )
    private val darkColors = darkColors(
        primary = themeColors.primary,
        primaryVariant = themeColors.primaryVariant,
        onPrimary = themeColors.onPrimary,
        secondary = themeColors.secondary,
        secondaryVariant = themeColors.secondaryVariant,
        onSecondary = themeColors.onSecondary
    )
    private val useDarkColors = false

    /** Entry point of the application */
    fun run() = application {
        Window(
            onCloseRequest = ::exitApplication,
            title = "Dota 2 Notes",
        ) {
            // Listen to Dota Updates
            HttpServer.server.start(wait = false)

            // UI
            MaterialTheme(
                colors = if (useDarkColors) darkColors else lightColors
            ) {
                applicationInterface(ApplicationData)
            }
        }
    }
}
