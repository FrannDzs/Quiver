package com.deflatedpickle.quiver.packexport

import com.deflatedpickle.haruhi.api.Registry
import com.deflatedpickle.haruhi.util.PluginUtil
import com.deflatedpickle.haruhi.util.RegistryUtil
import com.deflatedpickle.marvin.util.OSUtil
import com.deflatedpickle.quiver.backend.extension.toPatternFilter
import com.deflatedpickle.quiver.backend.util.DotMinecraft
import com.deflatedpickle.quiver.backend.util.Filters
import com.deflatedpickle.quiver.frontend.widget.ButtonField
import com.deflatedpickle.quiver.packexport.api.ExportStep
import com.deflatedpickle.rawky.ui.constraints.FillBothFinishLine
import com.deflatedpickle.rawky.ui.constraints.FillHorizontalFinishLine
import com.deflatedpickle.rawky.ui.constraints.StickEast
import com.jidesoft.swing.CheckBoxList
import java.awt.GridBagLayout
import javax.swing.BorderFactory
import javax.swing.JFileChooser
import javax.swing.JPanel
import javax.swing.JScrollPane
import javax.swing.text.PlainDocument
import org.jdesktop.swingx.JXLabel
import org.jdesktop.swingx.JXTextField
import org.jdesktop.swingx.JXTitledSeparator
import org.oxbow.swingbits.dialog.task.TaskDialog

class ExportPackDialog : TaskDialog(PluginUtil.window, "Export Pack")  {
    val locationEntry = ButtonField(
        "Location",
        "The location to export to",
        OSUtil.getOS().toPatternFilter(),
        "Open"
    ) {
        val directoryChooser = JFileChooser(
            it.field.text
        ).apply {
            fileSelectionMode = JFileChooser.DIRECTORIES_ONLY
            isAcceptAllFileFilterUsed = false
        }
        val openResult = directoryChooser.showOpenDialog(PluginUtil.window)

        if (openResult == JFileChooser.APPROVE_OPTION) {
            it.field.text = directoryChooser.selectedFile.absolutePath
        }
    }.apply {
        this.field.text = DotMinecraft.dotMinecraft.resolve("resourcepacks").absolutePath
    }

    val exportStepToggleList: CheckBoxList

    init {
        setCommands(StandardCommand.OK, StandardCommand.CANCEL)

        @Suppress("UNCHECKED_CAST")
        val registry = RegistryUtil.get("export") as Registry<String, ExportStep>
        val exportStepList = registry.getAll().values

        exportStepToggleList = CheckBoxList(exportStepList.toTypedArray()).apply {
            toolTipText = "Steps to run when the pack is exported"

            // Select all the checkboxes of enabled steps
            // addCheckBoxListSelectedValues(exportStepList.filter { it.toggled }.toTypedArray())
        }

        this.fixedComponent = JScrollPane(JPanel().apply {
            isOpaque = false
            layout = GridBagLayout()

            /* Pack */
            this.add(JXTitledSeparator("Pack"), FillHorizontalFinishLine)

            this.add(JXLabel("Location" + ":"), StickEast)
            this.add(locationEntry, FillHorizontalFinishLine)

            this.add(JXTitledSeparator("Steps"), FillHorizontalFinishLine)

            this.add(JScrollPane(exportStepToggleList), FillBothFinishLine)
        }).apply {
            isOpaque = false
            viewport.isOpaque = false

            border = BorderFactory.createEmptyBorder()
        }
    }
}