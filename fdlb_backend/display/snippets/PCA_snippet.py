import uuid
from io import StringIO
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from django.core.files import File
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from sklearn.decomposition import PCA

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.models import RawUserFile, ImageModel
from core.snippets_view.simple_view import LabelView, ScalarView, UploadFile, ButtonView, Image


class PCA_DisplaySnippet(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('PCA Display')))
                .add(UploadFile(view_id='basis', on_upload=self.on_upload))

                .add(LabelView(view_id='available_columns', visible=False))

                .add(LabelView(view_id='select_label_label', value='Set label name', visible=False))
                .add(ScalarView(view_id='select_label', value='', visible=False))
                .add(LabelView(view_id='data_columns_label', value='Set data columns, separated by `;`', visible=False))
                .add(ScalarView(view_id='data_columns', value='', visible=False))

                .add(ButtonView(view_id='draw', text=_('Draw!!'), on_submit=self.on_draw_press, visible=False))
                .add(Image(view_id='result', visible=False))
        )

    @property
    def content_url(self) -> str:
        return reverse('display:pca_display')

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return _(u'PCA Display')

    @property
    def description(self) -> str:
        return _(u'PCA Display')

    def on_upload(self):
        filepath = RawUserFile.objects.get(id=self.basis.value).filename
        data = pd.read_csv(filepath, delimiter=',')

        self.available_columns.value = str(list(data.columns))
        self.available_columns.visible = True

        self.select_label_label.visible = True
        self.select_label.visible = True
        self.data_columns_label.visible = True
        self.data_columns.visible = True

        self.draw.visible = True

    def get_data(self):
        raw_data = pd.read_csv(RawUserFile.objects.get(id=int(self.basis.value)).filename, delimiter=',')
        label_column_name = self.select_label.value
        if len(str(label_column_name)) > 1:
            labels = raw_data[label_column_name].values
        else:
            labels = np.array([])
        data_names = list(map(str.strip, str(self.data_columns.value).split(';')))
        input = raw_data.loc[:, data_names].values
        return labels, input

    def generate_colors(self, labels):
        if labels.size <= 0:
            return None
        colors = {l: list(np.random.random(size=3)) for l in np.unique(labels)}
        return np.array([colors[l] for l in labels])

    def on_draw_press(self):
        labels, input = self.get_data()
        pca = PCA(n_components=2)
        pca.fit(input)
        transformed = pca.transform(input)

        plt.scatter(transformed[:, 0], transformed[:, 1], c=self.generate_colors(labels))
        f = StringIO()
        plt.savefig(f, dpi=1000, format='svg', bbox_inches='tight')

        image = ImageModel()
        image.name = f'{uuid.uuid4().hex}_pca.svg'
        image.image.save(image.name,  File(f))
        image.mimetype = 'image/svg+xml'
        image.save()

        self.result.value = reverse('image',  kwargs={'image_name': image.name})
        self.result.visible = True
        print('ok')

# PetalWidthCm ;PetalLengthCm ;SepalLengthCm; SepalWidthCm
# Species
