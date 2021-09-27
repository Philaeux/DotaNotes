import androidx.compose.material.MaterialTheme
import androidx.compose.material.darkColors
import androidx.compose.material.lightColors
import androidx.compose.runtime.mutableStateOf
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.IntSize
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import io.ktor.application.*
import io.ktor.features.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.application.install
import io.ktor.request.*
import io.ktor.gson.*

val applicationState = mutableStateOf(ApplicationState())



fun main() {
    application {
        Window(
            onCloseRequest = ::exitApplication,
            title = "Dota 2 Notes",
        ) {
            val themeColors = lightColors(
                primary= Color(0xff616161),
                primaryVariant = Color(0xff455a64),
                onPrimary = Color(0xffffffff),
                secondary = Color(0xff1976d2),
                secondaryVariant = Color(0xff1565c0),
                onSecondary = Color(0xffffffff)
            )
            var serverLogLastModified: Long = 0

            // Listen to Dota Updates
            embeddedServer(Netty, port = 8765, host = "0.0.0.0") {
                install(ContentNegotiation) {
                    gson()
                }
                routing {
                    post("/") {
                        if (serverLogFile.lastModified() != serverLogLastModified) {
                            serverLogLastModified = serverLogFile.lastModified()
                            applicationState.value.readFromLog(serverLogFile)
                        }

//                      var payload = call.receive<String>()
//                      println(payload)
//                      /ISteamUser/GetPlayerSummaries/v0002?format=json&steamids=76561198059151539%2c76561198355035901%2c76561198113266963%2c76561198143742900%2c76561198086478594%2c76561198304708845%2c76561198002109366%2c76561198182913823%2c76561198066570770%2c76561198131528630&key=68908607EF1439E75D7C58CE8D71A6E3

                        val payload = call.receive<GSIGameState>()
                        applicationState.value.readFromGSI(payload)
                        call.respondText("{}")
                    }
                }
            }.start(wait = false)

            // UI
            MaterialTheme(
                colors = themeColors
            ) {
                applicationInterface(applicationState.value)
            }

        }
    }
}
