from kivy.app import App

from kivy.lang import Builder

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.slider import Slider

from kivy.clock import Clock

from kivy.graphics.texture import Texture
from kivy.graphics import RenderContext, Color, Rectangle, BindTexture, PushMatrix, Rotate, PopMatrix

from kivy.properties import ObjectProperty

from kivy.core.window import Window

import cv2
from pathlib import Path
import numpy as np
# 1
# 2
# 3
# 4
# 5
class DrawCircle(BoxLayout):
    def draw_circle(self, instance):
        try:
            center_pos = (int(self.ids.circle_pos_x_ti.text), int(self.ids.circle_pos_y_ti.text))
            radius = int(self.ids.circle_radius_ti.text)
            color = (255, 0, 0)
            thickness = int(self.ids.circle_tickness_ti.text)
            cv2.circle(Image_Editor_Scr.img_new, center_pos, radius, color, thickness)

            # Display image
            Image_Editor_Scr.display_img(Image_Editor_Scr.img_new)

        except Exception as e:
            print(e)
# 1
# 2
# 3
# 4
# 5
class Image_Editor_Scr(Screen):
    cv2_version = cv2.__version__
    # color_space_flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
    color_space_flag = {'COLOR_BAYER_BG2BGR': cv2.COLOR_BAYER_BG2BGR, 'COLOR_BAYER_BG2BGRA': cv2.COLOR_BAYER_BG2BGRA, 'COLOR_BAYER_BG2BGR_EA': cv2.COLOR_BAYER_BG2BGR_EA, 'COLOR_BAYER_BG2BGR_VNG': cv2.COLOR_BAYER_BG2BGR_VNG, 'COLOR_BAYER_BG2GRAY': cv2.COLOR_BAYER_BG2GRAY, 'COLOR_BAYER_BG2RGB': cv2.COLOR_BAYER_BG2RGB, 'COLOR_BAYER_BG2RGBA': cv2.COLOR_BAYER_BG2RGBA, 'COLOR_BAYER_BG2RGB_EA': cv2.COLOR_BAYER_BG2RGB_EA, 'COLOR_BAYER_BG2RGB_VNG': cv2.COLOR_BAYER_BG2RGB_VNG, 'COLOR_BAYER_GB2BGR': cv2.COLOR_BAYER_GB2BGR, 'COLOR_BAYER_GB2BGRA': cv2.COLOR_BAYER_GB2BGRA, 'COLOR_BAYER_GB2BGR_EA': cv2.COLOR_BAYER_GB2BGR_EA, 'COLOR_BAYER_GB2BGR_VNG': cv2.COLOR_BAYER_GB2BGR_VNG, 'COLOR_BAYER_GB2GRAY': cv2.COLOR_BAYER_GB2GRAY, 'COLOR_BAYER_GB2RGB': cv2.COLOR_BAYER_GB2RGB, 'COLOR_BAYER_GB2RGBA': cv2.COLOR_BAYER_GB2RGBA, 'COLOR_BAYER_GB2RGB_EA': cv2.COLOR_BAYER_GB2RGB_EA, 'COLOR_BAYER_GB2RGB_VNG': cv2.COLOR_BAYER_GB2RGB_VNG, 'COLOR_BAYER_GR2BGR': cv2.COLOR_BAYER_GR2BGR, 'COLOR_BAYER_GR2BGRA': cv2.COLOR_BAYER_GR2BGRA, 'COLOR_BAYER_GR2BGR_EA': cv2.COLOR_BAYER_GR2BGR_EA, 'COLOR_BAYER_GR2BGR_VNG': cv2.COLOR_BAYER_GR2BGR_VNG, 'COLOR_BAYER_GR2GRAY': cv2.COLOR_BAYER_GR2GRAY, 'COLOR_BAYER_GR2RGB': cv2.COLOR_BAYER_GR2RGB, 'COLOR_BAYER_GR2RGBA': cv2.COLOR_BAYER_GR2RGBA, 'COLOR_BAYER_GR2RGB_EA': cv2.COLOR_BAYER_GR2RGB_EA, 'COLOR_BAYER_GR2RGB_VNG': cv2.COLOR_BAYER_GR2RGB_VNG, 'COLOR_BAYER_RG2BGR': cv2.COLOR_BAYER_RG2BGR, 'COLOR_BAYER_RG2BGRA': cv2.COLOR_BAYER_RG2BGRA, 'COLOR_BAYER_RG2BGR_EA': cv2.COLOR_BAYER_RG2BGR_EA, 'COLOR_BAYER_RG2BGR_VNG': cv2.COLOR_BAYER_RG2BGR_VNG, 'COLOR_BAYER_RG2GRAY': cv2.COLOR_BAYER_RG2GRAY, 'COLOR_BAYER_RG2RGB': cv2.COLOR_BAYER_RG2RGB, 'COLOR_BAYER_RG2RGBA': cv2.COLOR_BAYER_RG2RGBA, 'COLOR_BAYER_RG2RGB_EA': cv2.COLOR_BAYER_RG2RGB_EA, 'COLOR_BAYER_RG2RGB_VNG': cv2.COLOR_BAYER_RG2RGB_VNG, 'COLOR_BGR2BGR555': cv2.COLOR_BGR2BGR555, 'COLOR_BGR2BGR565': cv2.COLOR_BGR2BGR565, 'COLOR_BGR2BGRA': cv2.COLOR_BGR2BGRA, 'COLOR_BGR2GRAY': cv2.COLOR_BGR2GRAY, 'COLOR_BGR2HLS': cv2.COLOR_BGR2HLS, 'COLOR_BGR2HLS_FULL': cv2.COLOR_BGR2HLS_FULL, 'COLOR_BGR2HSV': cv2.COLOR_BGR2HSV, 'COLOR_BGR2HSV_FULL': cv2.COLOR_BGR2HSV_FULL, 'COLOR_BGR2LAB': cv2.COLOR_BGR2LAB, 'COLOR_BGR2LUV': cv2.COLOR_BGR2LUV, 'COLOR_BGR2Lab': cv2.COLOR_BGR2Lab, 'COLOR_BGR2Luv': cv2.COLOR_BGR2Luv, 'COLOR_BGR2RGB': cv2.COLOR_BGR2RGB, 'COLOR_BGR2RGBA': cv2.COLOR_BGR2RGBA, 'COLOR_BGR2XYZ': cv2.COLOR_BGR2XYZ, 'COLOR_BGR2YCR_CB': cv2.COLOR_BGR2YCR_CB, 'COLOR_BGR2YCrCb': cv2.COLOR_BGR2YCrCb, 'COLOR_BGR2YUV': cv2.COLOR_BGR2YUV, 'COLOR_BGR2YUV_I420': cv2.COLOR_BGR2YUV_I420, 'COLOR_BGR2YUV_IYUV': cv2.COLOR_BGR2YUV_IYUV, 'COLOR_BGR2YUV_YV12': cv2.COLOR_BGR2YUV_YV12, 'COLOR_BGR5552BGR': cv2.COLOR_BGR5552BGR, 'COLOR_BGR5552BGRA': cv2.COLOR_BGR5552BGRA, 'COLOR_BGR5552GRAY': cv2.COLOR_BGR5552GRAY, 'COLOR_BGR5552RGB': cv2.COLOR_BGR5552RGB, 'COLOR_BGR5552RGBA': cv2.COLOR_BGR5552RGBA, 'COLOR_BGR5652BGR': cv2.COLOR_BGR5652BGR, 'COLOR_BGR5652BGRA': cv2.COLOR_BGR5652BGRA, 'COLOR_BGR5652GRAY': cv2.COLOR_BGR5652GRAY, 'COLOR_BGR5652RGB': cv2.COLOR_BGR5652RGB, 'COLOR_BGR5652RGBA': cv2.COLOR_BGR5652RGBA, 'COLOR_BGRA2BGR': cv2.COLOR_BGRA2BGR, 'COLOR_BGRA2BGR555': cv2.COLOR_BGRA2BGR555, 'COLOR_BGRA2BGR565': cv2.COLOR_BGRA2BGR565, 'COLOR_BGRA2GRAY': cv2.COLOR_BGRA2GRAY, 'COLOR_BGRA2RGB': cv2.COLOR_BGRA2RGB, 'COLOR_BGRA2RGBA': cv2.COLOR_BGRA2RGBA, 'COLOR_BGRA2YUV_I420': cv2.COLOR_BGRA2YUV_I420, 'COLOR_BGRA2YUV_IYUV': cv2.COLOR_BGRA2YUV_IYUV, 'COLOR_BGRA2YUV_YV12': cv2.COLOR_BGRA2YUV_YV12, 'COLOR_BayerBG2BGR': cv2.COLOR_BayerBG2BGR, 'COLOR_BayerBG2BGRA': cv2.COLOR_BayerBG2BGRA, 'COLOR_BayerBG2BGR_EA': cv2.COLOR_BayerBG2BGR_EA, 'COLOR_BayerBG2BGR_VNG': cv2.COLOR_BayerBG2BGR_VNG, 'COLOR_BayerBG2GRAY': cv2.COLOR_BayerBG2GRAY, 'COLOR_BayerBG2RGB': cv2.COLOR_BayerBG2RGB, 'COLOR_BayerBG2RGBA': cv2.COLOR_BayerBG2RGBA, 'COLOR_BayerBG2RGB_EA': cv2.COLOR_BayerBG2RGB_EA, 'COLOR_BayerBG2RGB_VNG': cv2.COLOR_BayerBG2RGB_VNG, 'COLOR_BayerGB2BGR': cv2.COLOR_BayerGB2BGR, 'COLOR_BayerGB2BGRA': cv2.COLOR_BayerGB2BGRA, 'COLOR_BayerGB2BGR_EA': cv2.COLOR_BayerGB2BGR_EA, 'COLOR_BayerGB2BGR_VNG': cv2.COLOR_BayerGB2BGR_VNG, 'COLOR_BayerGB2GRAY': cv2.COLOR_BayerGB2GRAY, 'COLOR_BayerGB2RGB': cv2.COLOR_BayerGB2RGB, 'COLOR_BayerGB2RGBA': cv2.COLOR_BayerGB2RGBA, 'COLOR_BayerGB2RGB_EA': cv2.COLOR_BayerGB2RGB_EA, 'COLOR_BayerGB2RGB_VNG': cv2.COLOR_BayerGB2RGB_VNG, 'COLOR_BayerGR2BGR': cv2.COLOR_BayerGR2BGR, 'COLOR_BayerGR2BGRA': cv2.COLOR_BayerGR2BGRA, 'COLOR_BayerGR2BGR_EA': cv2.COLOR_BayerGR2BGR_EA, 'COLOR_BayerGR2BGR_VNG': cv2.COLOR_BayerGR2BGR_VNG, 'COLOR_BayerGR2GRAY': cv2.COLOR_BayerGR2GRAY, 'COLOR_BayerGR2RGB': cv2.COLOR_BayerGR2RGB, 'COLOR_BayerGR2RGBA': cv2.COLOR_BayerGR2RGBA, 'COLOR_BayerGR2RGB_EA': cv2.COLOR_BayerGR2RGB_EA, 'COLOR_BayerGR2RGB_VNG': cv2.COLOR_BayerGR2RGB_VNG, 'COLOR_BayerRG2BGR': cv2.COLOR_BayerRG2BGR, 'COLOR_BayerRG2BGRA': cv2.COLOR_BayerRG2BGRA, 'COLOR_BayerRG2BGR_EA': cv2.COLOR_BayerRG2BGR_EA, 'COLOR_BayerRG2BGR_VNG': cv2.COLOR_BayerRG2BGR_VNG, 'COLOR_BayerRG2GRAY': cv2.COLOR_BayerRG2GRAY, 'COLOR_BayerRG2RGB': cv2.COLOR_BayerRG2RGB, 'COLOR_BayerRG2RGBA': cv2.COLOR_BayerRG2RGBA, 'COLOR_BayerRG2RGB_EA': cv2.COLOR_BayerRG2RGB_EA, 'COLOR_BayerRG2RGB_VNG': cv2.COLOR_BayerRG2RGB_VNG, 'COLOR_COLORCVT_MAX': cv2.COLOR_COLORCVT_MAX, 'COLOR_GRAY2BGR': cv2.COLOR_GRAY2BGR, 'COLOR_GRAY2BGR555': cv2.COLOR_GRAY2BGR555, 'COLOR_GRAY2BGR565': cv2.COLOR_GRAY2BGR565, 'COLOR_GRAY2BGRA': cv2.COLOR_GRAY2BGRA, 'COLOR_GRAY2RGB': cv2.COLOR_GRAY2RGB, 'COLOR_GRAY2RGBA': cv2.COLOR_GRAY2RGBA, 'COLOR_HLS2BGR': cv2.COLOR_HLS2BGR, 'COLOR_HLS2BGR_FULL': cv2.COLOR_HLS2BGR_FULL, 'COLOR_HLS2RGB': cv2.COLOR_HLS2RGB, 'COLOR_HLS2RGB_FULL': cv2.COLOR_HLS2RGB_FULL, 'COLOR_HSV2BGR': cv2.COLOR_HSV2BGR, 'COLOR_HSV2BGR_FULL': cv2.COLOR_HSV2BGR_FULL, 'COLOR_HSV2RGB': cv2.COLOR_HSV2RGB, 'COLOR_HSV2RGB_FULL': cv2.COLOR_HSV2RGB_FULL, 'COLOR_LAB2BGR': cv2.COLOR_LAB2BGR, 'COLOR_LAB2LBGR': cv2.COLOR_LAB2LBGR, 'COLOR_LAB2LRGB': cv2.COLOR_LAB2LRGB, 'COLOR_LAB2RGB': cv2.COLOR_LAB2RGB, 'COLOR_LBGR2LAB': cv2.COLOR_LBGR2LAB, 'COLOR_LBGR2LUV': cv2.COLOR_LBGR2LUV, 'COLOR_LBGR2Lab': cv2.COLOR_LBGR2Lab, 'COLOR_LBGR2Luv': cv2.COLOR_LBGR2Luv, 'COLOR_LRGB2LAB': cv2.COLOR_LRGB2LAB, 'COLOR_LRGB2LUV': cv2.COLOR_LRGB2LUV, 'COLOR_LRGB2Lab': cv2.COLOR_LRGB2Lab, 'COLOR_LRGB2Luv': cv2.COLOR_LRGB2Luv, 'COLOR_LUV2BGR': cv2.COLOR_LUV2BGR, 'COLOR_LUV2LBGR': cv2.COLOR_LUV2LBGR, 'COLOR_LUV2LRGB': cv2.COLOR_LUV2LRGB, 'COLOR_LUV2RGB': cv2.COLOR_LUV2RGB, 'COLOR_Lab2BGR': cv2.COLOR_Lab2BGR, 'COLOR_Lab2LBGR': cv2.COLOR_Lab2LBGR, 'COLOR_Lab2LRGB': cv2.COLOR_Lab2LRGB, 'COLOR_Lab2RGB': cv2.COLOR_Lab2RGB, 'COLOR_Luv2BGR': cv2.COLOR_Luv2BGR, 'COLOR_Luv2LBGR': cv2.COLOR_Luv2LBGR, 'COLOR_Luv2LRGB': cv2.COLOR_Luv2LRGB, 'COLOR_Luv2RGB': cv2.COLOR_Luv2RGB, 'COLOR_M_RGBA2RGBA': cv2.COLOR_M_RGBA2RGBA, 'COLOR_RGB2BGR': cv2.COLOR_RGB2BGR, 'COLOR_RGB2BGR555': cv2.COLOR_RGB2BGR555, 'COLOR_RGB2BGR565': cv2.COLOR_RGB2BGR565, 'COLOR_RGB2BGRA': cv2.COLOR_RGB2BGRA, 'COLOR_RGB2GRAY': cv2.COLOR_RGB2GRAY, 'COLOR_RGB2HLS': cv2.COLOR_RGB2HLS, 'COLOR_RGB2HLS_FULL': cv2.COLOR_RGB2HLS_FULL, 'COLOR_RGB2HSV': cv2.COLOR_RGB2HSV, 'COLOR_RGB2HSV_FULL': cv2.COLOR_RGB2HSV_FULL, 'COLOR_RGB2LAB': cv2.COLOR_RGB2LAB, 'COLOR_RGB2LUV': cv2.COLOR_RGB2LUV, 'COLOR_RGB2Lab': cv2.COLOR_RGB2Lab, 'COLOR_RGB2Luv': cv2.COLOR_RGB2Luv, 'COLOR_RGB2RGBA': cv2.COLOR_RGB2RGBA, 'COLOR_RGB2XYZ': cv2.COLOR_RGB2XYZ, 'COLOR_RGB2YCR_CB': cv2.COLOR_RGB2YCR_CB, 'COLOR_RGB2YCrCb': cv2.COLOR_RGB2YCrCb, 'COLOR_RGB2YUV': cv2.COLOR_RGB2YUV, 'COLOR_RGB2YUV_I420': cv2.COLOR_RGB2YUV_I420, 'COLOR_RGB2YUV_IYUV': cv2.COLOR_RGB2YUV_IYUV, 'COLOR_RGB2YUV_YV12': cv2.COLOR_RGB2YUV_YV12, 'COLOR_RGBA2BGR': cv2.COLOR_RGBA2BGR, 'COLOR_RGBA2BGR555': cv2.COLOR_RGBA2BGR555, 'COLOR_RGBA2BGR565': cv2.COLOR_RGBA2BGR565, 'COLOR_RGBA2BGRA': cv2.COLOR_RGBA2BGRA, 'COLOR_RGBA2GRAY': cv2.COLOR_RGBA2GRAY, 'COLOR_RGBA2M_RGBA': cv2.COLOR_RGBA2M_RGBA, 'COLOR_RGBA2RGB': cv2.COLOR_RGBA2RGB, 'COLOR_RGBA2YUV_I420': cv2.COLOR_RGBA2YUV_I420, 'COLOR_RGBA2YUV_IYUV': cv2.COLOR_RGBA2YUV_IYUV, 'COLOR_RGBA2YUV_YV12': cv2.COLOR_RGBA2YUV_YV12, 'COLOR_RGBA2mRGBA': cv2.COLOR_RGBA2mRGBA, 'COLOR_XYZ2BGR': cv2.COLOR_XYZ2BGR, 'COLOR_XYZ2RGB': cv2.COLOR_XYZ2RGB, 'COLOR_YCR_CB2BGR': cv2.COLOR_YCR_CB2BGR, 'COLOR_YCR_CB2RGB': cv2.COLOR_YCR_CB2RGB, 'COLOR_YCrCb2BGR': cv2.COLOR_YCrCb2BGR, 'COLOR_YCrCb2RGB': cv2.COLOR_YCrCb2RGB, 'COLOR_YUV2BGR': cv2.COLOR_YUV2BGR, 'COLOR_YUV2BGRA_I420': cv2.COLOR_YUV2BGRA_I420, 'COLOR_YUV2BGRA_IYUV': cv2.COLOR_YUV2BGRA_IYUV, 'COLOR_YUV2BGRA_NV12': cv2.COLOR_YUV2BGRA_NV12, 'COLOR_YUV2BGRA_NV21': cv2.COLOR_YUV2BGRA_NV21, 'COLOR_YUV2BGRA_UYNV': cv2.COLOR_YUV2BGRA_UYNV, 'COLOR_YUV2BGRA_UYVY': cv2.COLOR_YUV2BGRA_UYVY, 'COLOR_YUV2BGRA_Y422': cv2.COLOR_YUV2BGRA_Y422, 'COLOR_YUV2BGRA_YUNV': cv2.COLOR_YUV2BGRA_YUNV, 'COLOR_YUV2BGRA_YUY2': cv2.COLOR_YUV2BGRA_YUY2, 'COLOR_YUV2BGRA_YUYV': cv2.COLOR_YUV2BGRA_YUYV, 'COLOR_YUV2BGRA_YV12': cv2.COLOR_YUV2BGRA_YV12, 'COLOR_YUV2BGRA_YVYU': cv2.COLOR_YUV2BGRA_YVYU, 'COLOR_YUV2BGR_I420': cv2.COLOR_YUV2BGR_I420, 'COLOR_YUV2BGR_IYUV': cv2.COLOR_YUV2BGR_IYUV, 'COLOR_YUV2BGR_NV12': cv2.COLOR_YUV2BGR_NV12, 'COLOR_YUV2BGR_NV21': cv2.COLOR_YUV2BGR_NV21, 'COLOR_YUV2BGR_UYNV': cv2.COLOR_YUV2BGR_UYNV, 'COLOR_YUV2BGR_UYVY': cv2.COLOR_YUV2BGR_UYVY, 'COLOR_YUV2BGR_Y422': cv2.COLOR_YUV2BGR_Y422, 'COLOR_YUV2BGR_YUNV': cv2.COLOR_YUV2BGR_YUNV, 'COLOR_YUV2BGR_YUY2': cv2.COLOR_YUV2BGR_YUY2, 'COLOR_YUV2BGR_YUYV': cv2.COLOR_YUV2BGR_YUYV, 'COLOR_YUV2BGR_YV12': cv2.COLOR_YUV2BGR_YV12, 'COLOR_YUV2BGR_YVYU': cv2.COLOR_YUV2BGR_YVYU, 'COLOR_YUV2GRAY_420': cv2.COLOR_YUV2GRAY_420, 'COLOR_YUV2GRAY_I420': cv2.COLOR_YUV2GRAY_I420, 'COLOR_YUV2GRAY_IYUV': cv2.COLOR_YUV2GRAY_IYUV, 'COLOR_YUV2GRAY_NV12': cv2.COLOR_YUV2GRAY_NV12, 'COLOR_YUV2GRAY_NV21': cv2.COLOR_YUV2GRAY_NV21, 'COLOR_YUV2GRAY_UYNV': cv2.COLOR_YUV2GRAY_UYNV, 'COLOR_YUV2GRAY_UYVY': cv2.COLOR_YUV2GRAY_UYVY, 'COLOR_YUV2GRAY_Y422': cv2.COLOR_YUV2GRAY_Y422, 'COLOR_YUV2GRAY_YUNV': cv2.COLOR_YUV2GRAY_YUNV, 'COLOR_YUV2GRAY_YUY2': cv2.COLOR_YUV2GRAY_YUY2, 'COLOR_YUV2GRAY_YUYV': cv2.COLOR_YUV2GRAY_YUYV, 'COLOR_YUV2GRAY_YV12': cv2.COLOR_YUV2GRAY_YV12, 'COLOR_YUV2GRAY_YVYU': cv2.COLOR_YUV2GRAY_YVYU, 'COLOR_YUV2RGB': cv2.COLOR_YUV2RGB, 'COLOR_YUV2RGBA_I420': cv2.COLOR_YUV2RGBA_I420, 'COLOR_YUV2RGBA_IYUV': cv2.COLOR_YUV2RGBA_IYUV, 'COLOR_YUV2RGBA_NV12': cv2.COLOR_YUV2RGBA_NV12, 'COLOR_YUV2RGBA_NV21': cv2.COLOR_YUV2RGBA_NV21, 'COLOR_YUV2RGBA_UYNV': cv2.COLOR_YUV2RGBA_UYNV, 'COLOR_YUV2RGBA_UYVY': cv2.COLOR_YUV2RGBA_UYVY, 'COLOR_YUV2RGBA_Y422': cv2.COLOR_YUV2RGBA_Y422, 'COLOR_YUV2RGBA_YUNV': cv2.COLOR_YUV2RGBA_YUNV, 'COLOR_YUV2RGBA_YUY2': cv2.COLOR_YUV2RGBA_YUY2, 'COLOR_YUV2RGBA_YUYV': cv2.COLOR_YUV2RGBA_YUYV, 'COLOR_YUV2RGBA_YV12': cv2.COLOR_YUV2RGBA_YV12, 'COLOR_YUV2RGBA_YVYU': cv2.COLOR_YUV2RGBA_YVYU, 'COLOR_YUV2RGB_I420': cv2.COLOR_YUV2RGB_I420, 'COLOR_YUV2RGB_IYUV': cv2.COLOR_YUV2RGB_IYUV, 'COLOR_YUV2RGB_NV12': cv2.COLOR_YUV2RGB_NV12, 'COLOR_YUV2RGB_NV21': cv2.COLOR_YUV2RGB_NV21, 'COLOR_YUV2RGB_UYNV': cv2.COLOR_YUV2RGB_UYNV, 'COLOR_YUV2RGB_UYVY': cv2.COLOR_YUV2RGB_UYVY, 'COLOR_YUV2RGB_Y422': cv2.COLOR_YUV2RGB_Y422, 'COLOR_YUV2RGB_YUNV': cv2.COLOR_YUV2RGB_YUNV, 'COLOR_YUV2RGB_YUY2': cv2.COLOR_YUV2RGB_YUY2, 'COLOR_YUV2RGB_YUYV': cv2.COLOR_YUV2RGB_YUYV, 'COLOR_YUV2RGB_YV12': cv2.COLOR_YUV2RGB_YV12, 'COLOR_YUV2RGB_YVYU': cv2.COLOR_YUV2RGB_YVYU, 'COLOR_YUV420P2BGR': cv2.COLOR_YUV420P2BGR, 'COLOR_YUV420P2BGRA': cv2.COLOR_YUV420P2BGRA, 'COLOR_YUV420P2GRAY': cv2.COLOR_YUV420P2GRAY, 'COLOR_YUV420P2RGB': cv2.COLOR_YUV420P2RGB, 'COLOR_YUV420P2RGBA': cv2.COLOR_YUV420P2RGBA, 'COLOR_YUV420SP2BGR': cv2.COLOR_YUV420SP2BGR, 'COLOR_YUV420SP2BGRA': cv2.COLOR_YUV420SP2BGRA, 'COLOR_YUV420SP2GRAY': cv2.COLOR_YUV420SP2GRAY, 'COLOR_YUV420SP2RGB': cv2.COLOR_YUV420SP2RGB, 'COLOR_YUV420SP2RGBA': cv2.COLOR_YUV420SP2RGBA, 'COLOR_YUV420p2BGR': cv2.COLOR_YUV420p2BGR, 'COLOR_YUV420p2BGRA': cv2.COLOR_YUV420p2BGRA, 'COLOR_YUV420p2GRAY': cv2.COLOR_YUV420p2GRAY, 'COLOR_YUV420p2RGB': cv2.COLOR_YUV420p2RGB, 'COLOR_YUV420p2RGBA': cv2.COLOR_YUV420p2RGBA, 'COLOR_YUV420sp2BGR': cv2.COLOR_YUV420sp2BGR, 'COLOR_YUV420sp2BGRA': cv2.COLOR_YUV420sp2BGRA, 'COLOR_YUV420sp2GRAY': cv2.COLOR_YUV420sp2GRAY, 'COLOR_YUV420sp2RGB': cv2.COLOR_YUV420sp2RGB, 'COLOR_YUV420sp2RGBA': cv2.COLOR_YUV420sp2RGBA, 'COLOR_mRGBA2RGBA': cv2.COLOR_mRGBA2RGBA}
    interpol_flag = {"INTER_AREA": cv2.INTER_AREA, "INTER_CUBIC": cv2.INTER_CUBIC, "INTER_LINEAR": cv2.INTER_LINEAR}
    cascades_flag = {"Face": "haarcascade_frontalface_default.xml", "Eyes": "haarcascade_eye.xml"}

    options = ["Draw Rectangle", "Draw Circle"]
    load_img_popup = ObjectProperty(None)
    # 1
    # 2
    # 3
    def __init__(self, **kwargs):
        super(Image_Editor_Scr, self).__init__(**kwargs)
        self.rotation = 0
        self.size = [0, 0]
        self.color = 0

        self.load_img_2("a")
    # 1
    # 2
    # 3
    def option_select(self, instance):
        print(instance.text)
        self.a = DrawCircle()
        self.ids.main_bl.add_widget(self.a, -1)
    # 1
    # 2
    # 3
    def load_img_popup(self, instance):
        #ontent = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        content = BoxLayout(orientation = "vertical")

        home = str(Path.home()) + "\Desktop"
        fc = FileChooserListView(path = home)
        content.add_widget(fc)

        bt_1 = Button(text = "Select")
        bt_1.bind(on_press = self.load_img)
        content.add_widget(bt_1)

        a = Popup(title = "Load file", content = content, size_hint = (0.5, 0.5))
        self.load_img_popup = a
        self.load_img_popup.open()
    # 1
    # 2
    # 3
    def load_img(self, instance):
        print(self.fc.path)
        self.load_img_popup.dismiss()
    # 1
    # 2
    # 3
    def save_img_popup(self, instance):
        #ontent = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        content = BoxLayout(orientation = "vertical")

        home = str(Path.home()) + "\Desktop"
        fc = FileChooserListView(path = home)
        content.add_widget(self.fc)

        ti_1 = TextInput()
        content.add_widget(ti_1)

        bt_1 = Button(text = "Select")
        bt_1.bind(on_press = self.save_img)
        content.add_widget(bt_1)

        self.save_img_popup = Popup(title = "Load file", content = content, size_hint=(0.9, 0.9))
        self.save_img_popup.open()
    # 1
    # 2
    # 3
    def save_img(self, instance):
        print(self.fc.path)
        cv2.imwrite(os.path.join(path , 'waka.jpg'), img)
        self.save_img_popup.dismiss()
    # 1
    # 2
    # 3
    def display_img(self, img):
        # image dimensions
        img_height, img_width = img.shape[:2]

        # Convert to String
        buf = img.tostring()

        image_texture = Texture.create(size = (img_width, img_height), colorfmt = 'bgr')
        image_texture.blit_buffer(pbuffer = buf, colorfmt = 'bgr', bufferfmt = 'ubyte')

        self.ids.image_widget.texture = image_texture

        self.ids.img_height_lb.text = f"Image height: {img_height}"
        self.ids.img_width_lb.text = f"Image width: {img_width}"


    def load_img_2(self, instance):
        # open image
        self.img_1 = cv2.imread("ff.jpg")

        self.img_new = self.img_1
        
        # image dimensions
        self.img_height, self.img_width, channels = self.img_new.shape      

        # Display image
        self.display_img(self.img_new)

    # 1
    # 2
    # 3
    def color_img(self, instance):
        # print(instance.text)
        try:
            color_flag = self.color_space_flag[self.ids.color_flag_sp.text]
            self.img_new = cv2.cvtColor(self.img_1, color_flag)
           
            # Display image
            self.display_img(self.img_new)

        except Exception as e:
            print(e)
    # 1
    # 2
    # 3
    def flip(self):
        angle = 45
        # flip
        self.img_new = cv2.flip(self.img_new, angle)

        self.display_img(self.img_new)
    # 1
    # 2
    # 3
    def cascade(self, instance):
        try:
            # load cascades
            cascade = cv2.CascadeClassifier(self.cascades_flag[self.ids.cascades_sp.text])

            gray = cv2.cvtColor(self.img_new, cv2.COLOR_BGR2GRAY)

            cascade_type = cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in cascade_type:
                top_left_corner = (x, y)
                bottom_right_corner = (x+w, y+h)
                color = (255, 0, 0)
                thickness = 10
                self.img_new = cv2.rectangle(self.img_new, top_left_corner, bottom_right_corner, color, thickness)

            # Display image
            self.display_img(self.img_new)

        except Exception as e:
            print(e)
    # 1
    # 2
    # 3
    def resize(self, instance):
        try:
            scale_percent = int(self.ids.resize_ti.text)

            self.img_width = int(self.img_width * scale_percent / 100)
            self.img_height = int(self.img_height * scale_percent / 100)
            dim = (self.img_width, self.img_height)

            # resize image
            interpol = self.interpol_flag[self.ids.resize_interpol_sp.text]
            
            self.img_new = cv2.resize(self.img_new, dim, interpolation = interpol)

            # Display image
            self.display_img(self.img_new)

        except Exception as e:
            print(e)
    # 1
    # 2
    # 3
    def rotate(self, instance):
        # print(self.ids.rotate_slider.value)
        # angle = self.rotation + self.ids.rotate_slider.value
        print(self.ids.rotate_ti.text)
        angle = int(self.ids.rotate_ti.text) - self.rotation
        self.rotation = int(self.ids.rotate_ti.text)

        try:
            rows, cols = self.img_new.shape[:2]
            scale = 1
            M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, scale)
            self.img_new = cv2.warpAffine(self.img_new, M, (cols,rows))

            # Display image
            self.display_img(self.img_new)

        except Exception as e:
            print(e)
    # 1
    # 2
    # 3
    def Harris_Corner_detector(self, instance):
        # try:
        gray = cv2.cvtColor(self.img_new, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        blockSize = int(self.ids.blockSize_ti.text)
        ksize = int(self.ids.ksize_ti.text)
        k = float(self.ids.k_ti.text)

        self.img_new = cv2.cornerHarris(gray, blockSize, ksize, k)

        # Display image
        self.display_img(self.img_new)

        # except Exception as e:
        #     print(e)
    # 1
    # 2
    # 3
    def Shi_Tomasi_Corner_Detector(self, instance):
        gray = cv2.cvtColor(self.img_new, cv2.COLOR_BGR2GRAY)
        maxCorners = 25
        qualityLevel = 0.01
        minDistance = 10
        corners = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)
        corners = np.int0(corners)
        
        # draw circles arround corners
        for i in corners:
            x, y = i.ravel()
            center_pos = (x, y)
            radius = 30
            color = (255, 0, 0)
            thickness = -1
            cv2.circle(self.img_new, center_pos, radius, color, thickness)

        # Display image
        self.display_img(self.img_new)
    # 1
    # 2
    # 3
    def draw_circle(self, instance):
        try:
            center_pos = (int(self.a.ids.circle_pos_x_ti.text), int(self.a.ids.circle_pos_y_ti.text))
            radius = int(self.a.ids.circle_radius_ti.text)
            color = (255, 0, 0)
            thickness = int(self.a.ids.circle_tickness_ti.text)
            cv2.circle(self.img_new, center_pos, radius, color, thickness)

            # Display image
            self.display_img(self.img_new)

        except Exception as e:
            print(e)





# 1
# 2
# 3
# 4
# 5
Builder.load_file("kivy_image_editor.kv")
class Image_EditorApp(App):
    def build(self):
        Window.bind(on_close = self.end)

        self.scr_mng = ScreenManager()

        self.image_editor_scr = Image_Editor_Scr(name='image_editor_scr')

        self.scr_mng.add_widget(self.image_editor_scr)

        return self.scr_mng

    def end(self, instance):
        print("App closed")
# 1
# 2
# 3
# 4
# 5
if __name__ == '__main__':
    Image_EditorApp().run()