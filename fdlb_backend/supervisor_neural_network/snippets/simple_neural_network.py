import base64
from io import BytesIO
from typing import List

import re

import io
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.snippets_view.simple_view import LabelView, SelectView, ButtonView
from supervisor_neural_network.models import WeightModel
from supervisor_neural_network.snippets.simple_network_creator import SimpleNeuralNetworkCreator
from supervisor_neural_network.snippets_view.views import DrawableCanvas

from PIL import Image,ImageFilter
import numpy as np
import pickle



class SimpleNeuralNetwork(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('Simple NN')))
                .add(SelectView(
                    view_id='network_select',
                    options=list(WeightModel.objects.values_list('name', flat=True)),
                    placeholder=_('Select one of the network')
                ))
                .add(ButtonView(text=_('Add network'),redirect_to=SimpleNeuralNetworkCreator().content_url,))
                .add(DrawableCanvas(view_id='canvas'))
                .add(ButtonView(view_id='recognize', text=_('Recognize!!'), on_submit=self.on_recognize))

                .add(LabelView(view_id='result', ))
        )

    @property
    def content_url(self) -> str:
        return reverse('supervisor_neural_network:simple_neural_network')

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return _(u'Simple Neural Network')

    @property
    def description(self) -> str:
        return _(u'Simple Neural Network')

    def on_recognize(self):
        name = self.network_select.selected()
        network = WeightModel.objects.filter(name=name).first()
        imgstr = re.search(r'base64,(.*)', self.canvas.value).group(1)
        image_bytes = io.BytesIO(base64.b64decode(imgstr))
        im = (Image.open(image_bytes)
              .filter(ImageFilter.GaussianBlur(5))
              .resize(size=(280,280))
              .filter(ImageFilter.SMOOTH)
              .resize(size=(28,28))
              )
        # im = im.filter(ImageFilter.GaussianBlur)
        buffered = BytesIO()
        im.save(buffered, format="PNG")
        img_str = print(base64.b64encode(buffered.getvalue()))
        arr = np.array(im)[:,:,3].flatten()/ 255.0 * 2.0 - 1.0
        clf2 = pickle.loads(network.body)
        result = list(clf2.predict_proba(arr.reshape(-1, 1).T)[0])
        answer = (clf2.predict(arr.reshape(-1, 1).T))
        result = {i:result[i] for i in range(len(result))}

        output = str(result) + "\n\nAnswer:"+str(answer)
        print(output)
        self.result.value = output


# arr = np.array(im)[:,:,0]