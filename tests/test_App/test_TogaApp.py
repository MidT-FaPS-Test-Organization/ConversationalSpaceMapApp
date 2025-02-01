import unittest
import matplotlib

matplotlib.use("Agg")

import tests.TestResources as TestResources

import conversationalspacemapapp.App.TogaApp.app as TogaApp
import conversationalspacemapapp.Plotter.StylePicker as StylePicker


class TestTogaApp(unittest.TestCase):
    sut: TogaApp.ConversationalSpaceMapAppToga

    def setUp(self):
        TestTogaApp.sut = TogaApp.main()
        TestTogaApp.sut.startup()

    def test_run(self):
        pass

    def test_plot(self):
        TestTogaApp.sut._set_path(path=TestResources.path_multiple_speaker_transcript)

    def test_change_color_palette(self):
        TestTogaApp.sut._set_path(path=TestResources.path_multiple_speaker_transcript)
        TestTogaApp.sut.color_palette.value = StylePicker.Palette.Pastel
