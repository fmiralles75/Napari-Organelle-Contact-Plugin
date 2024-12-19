from typing import TYPE_CHECKING
import os
import numpy as np
from magicgui import magic_factory
from magicgui.widgets import Label, Container, Button, create_widget
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel, QComboBox
import skimage.filters.thresholding as st
from napari.layers import Image, Labels
import napari.types


if TYPE_CHECKING:
  import napari

"""
For thresholding, a single widget is defined that can be used for all thresholding methods. No options are available.
Manual thresholding is handled via a Container class definition. The main reason for this is that the threshold value
needs to be updated based on the image and more options (e.g. multi-threshold) can be added in the future.

Note to joe and francisco: for now let's stick to focusing on binary thresholding. We'll look into
other techniques in the future.
"""

import napari
from magicgui import magicgui
from napari.types import ImageData, LabelsData

@magicgui(call_button="Threshold")
def threshold(image: ImageData, threshold_value: int = 128) -> LabelsData:
    """Threshold an image and return a binary mask."""
    return (image > threshold_value).astype(int)

viewer = napari.Viewer()
viewer.window.add_dock_widget(threshold)

# class ThresholdWidget(QWidget):
#   def __init__(self, napari_viewer):
#     super().__init__()
#     self.viewer = napari_viewer
#     self.setLayout(QVBoxLayout())



# THE CODE BELOW IS DIRECTLY FROM EXISTING THRESHOLD FILES


  #   @magic_factory(
  #     auto_call=True,
  #     threshold={"widget_type": "FloatSlider", "min": 0.0, "max": 1.0, "step": 0.01},
  #     sigma={"widget_type": "FloatSpinBox", "min": 0.0, "max": 5.0, "step": 0.1},
  #   )

  #   self._image_layer_combo = create_widget(
  #       label="Image", annotation="napari.layers.Image"
  #   )

  #   self.threshold = create_widget(
  #       label="Threshold value", annotation=float,
  #       options={'value': 0, 'min': 0, 'max': 255, 'step': 1}
  #   )

  #   self.btn_apply = Button(text="Apply Thresholding")
  #   self.btn_apply.clicked.connect(self.apply_threshold)

  #   # append into/extend the container with your widgets
  #   self.extend(
  #       [
  #           self._image_layer_combo,
  #           self.threshold,
  #           self.btn_apply,
  #       ]
  #   )

  #   self._image_layer_combo.changed.connect(self._on_update_threshold_limits)
  #   self._on_update_threshold_limits(self)

  # def _on_update_threshold_limits(self, event=None):
  #   image_layer = self._image_layer_combo.value
  #   if image_layer is None:
  #       return
  #   if (self.threshold.value > image_layer.data.max()) or (self.threshold.value < image_layer.data.min()):
  #       self.threshold.value = image_layer.data.min()
  #   # setting the minimum creates the following problem. If the mimimum
  #   # is set to 7 and one wants to input 100, starting to type 1 turns it
  #   # automatically to 7. Leaving at 0 for the moment
  #   # self.threshold.min = image_layer.data.min()
  #   self.threshold.max = image_layer.data.max()
  #   self.threshold.step = (self.threshold.max - self.threshold.min) / 100

  # def apply_threshold(self, event=None):
  #   image_layer = self._image_layer_combo.value
  #   if image_layer is None:
  #       return
  #   mask = image_layer.data > self.threshold.value
  #   self._viewer.add_labels(
  #       mask,
  #       name=f"{image_layer.name}_threshold_manual",
  #   )