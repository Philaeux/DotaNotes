import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf

@Composable
@Preview
fun applicationInterfacePreview() {
    val applicationState = ApplicationState(mutableStateOf("6198777153"))
    applicationState.radiant[0].apply {
        this.currentName.value = "KNP"
        this.isAnonymous.value = true
    }
    applicationState.radiant[1].apply {
        this.currentName.value = "PH"
        this.isAnonymous.value = true
        this.smurfFlag.value = 1
    }
    applicationState.radiant[2].apply {
        this.currentName.value = "趁早"
        this.isAnonymous.value = false
        this.matchCount.value = 6814
        this.winCount.value = 3746
        this.smurfFlag.value = 2
        this.behaviorScore.value = 10000
    }
    applicationState.radiant[3].apply {
        this.currentName.value = "RAYUM"
        this.isAnonymous.value = false
        this.matchCount.value = 6468
        this.winCount.value = 3609
        this.smurfFlag.value = 3
        this.behaviorScore.value = 9500
    }
    applicationState.radiant[4].apply {
        this.currentName.value = "-152-"
        this.isAnonymous.value = false
        this.matchCount.value = 8269
        this.winCount.value = 4205
        this.smurfFlag.value = 4
        this.behaviorScore.value = 8767
    }
    applicationState.dire[0].apply {
        this.currentName.value = "RusmαÑ"
        this.isAnonymous.value = false
        this.matchCount.value = 10083
        this.winCount.value = 5363
        this.behaviorScore.value = 10000
    }
    applicationState.dire[1].apply {
        this.currentName.value = "dark"
        this.isAnonymous.value = true
    }
    applicationState.dire[2].apply {
        this.currentName.value = "Gracia"
        this.isAnonymous.value = true
    }
    applicationState.dire[3].apply {
        this.currentName.value = "magnum opus"
        this.isAnonymous.value = false
        this.matchCount.value = 14548
        this.winCount.value = 7461
        this.behaviorScore.value = 10000
    }
    applicationState.dire[4].apply {
        this.currentName.value = "dexter"
        this.isAnonymous.value = true
        this.behaviorScore.value = 10000
    }
    applicationInterface(applicationState)
}
