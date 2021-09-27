import org.jetbrains.compose.compose
import org.jetbrains.compose.desktop.application.dsl.TargetFormat
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "1.5.21"
    id("org.jetbrains.compose") version "1.0.0-alpha3"
}

group = "org.the-cluster"
version = "1.0"

repositories {
    google()
    mavenCentral()
    maven("https://maven.pkg.jetbrains.space/public/p/compose/dev")
}

dependencies {
    implementation(compose.desktop.currentOs)
    implementation("io.ktor:ktor-client-core:1.5.4")
    implementation("io.ktor:ktor-client-gson:1.5.4")
    implementation("io.ktor:ktor-client-jetty:1.5.4")
    implementation("io.ktor:ktor-server-netty:1.5.4")
    implementation("io.ktor:ktor-gson:1.5.4")
}

tasks.withType<KotlinCompile>() {
    kotlinOptions.jvmTarget = "16"
}

compose.desktop {
    application {
        mainClass = "MainKt"
        nativeDistributions {
            targetFormats(TargetFormat.Msi)
            packageName = "DotaNotes"
            packageVersion = "1.0.0"
        }
    }
}
