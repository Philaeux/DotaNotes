/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes.services

import io.ktor.application.*
import io.ktor.features.*
import io.ktor.gson.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import ngo.cluster.dota_notes.ApplicationData
import serverLogFile

/**
 * Singleton Http Server receiving GSI updates
 * @property[serverLogLastModified] Last log file processed by the server
 * @property[server] Netty HTTP server
 */
object HttpServer {
    var serverLogLastModified: Long = 0
    val server = embeddedServer(Netty, port = 8765, host = "0.0.0.0") {
        install(ContentNegotiation) {
            gson()
        }
        routing {
            post("/") {
                if (serverLogFile.lastModified() != serverLogLastModified) {
                    serverLogLastModified = serverLogFile.lastModified()
                    ApplicationData.readFromLog(serverLogFile)
                }

                val payload = call.receive<GSIGameState>()
                ApplicationData.readFromGSI(payload)
                call.respondText("{}")
            }
        }
    }
}
