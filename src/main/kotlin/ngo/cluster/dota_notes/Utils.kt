/**
 * Copyright MIT License
 * @author Vincent 'Philaeux' Lamotte
 */

package ngo.cluster.dota_notes

import java.io.File
import java.io.IOException
import java.util.concurrent.TimeUnit

fun String.runCommand(workingDir: File? = null): String? {
    return try {
        val parts = this.split("""\s""".toRegex())
        val proc = ProcessBuilder(*parts.toTypedArray())
            .directory(workingDir)
            .redirectOutput(ProcessBuilder.Redirect.PIPE)
            .redirectError(ProcessBuilder.Redirect.PIPE)
            .start()

        proc.waitFor(60, TimeUnit.MINUTES)
        proc.inputStream.bufferedReader().readText()
    } catch(e: IOException) {
        e.printStackTrace()
        null
    }
}
