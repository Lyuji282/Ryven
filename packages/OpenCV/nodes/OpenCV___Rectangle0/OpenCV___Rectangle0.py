from NIENV import *

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class Rectangle_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Rectangle_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.img_unrectangled = None
        self.img_rectangled = None


    def update_event(self, input_called=-1):
        self.img_unrectangled = self.input(0).copy()
        startpoint = self.input(1)
        endpoint=self.input(2)
        color=self.input(3) #COLOR is in BGR
        thickness=self.input(4)

        self.img_rectangled = cv2.rectangle( self.img_unrectangled,startpoint,endpoint,color,thickness)
        self.main_widget.show_image(self.img_rectangled)
        self.set_output_val(0, self.img_rectangled)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
