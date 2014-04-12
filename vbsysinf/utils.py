# -*- coding: utf-8 -*-
import os
import museo


def get_image_path(instance, filename):
    if isinstance(instance, museo.models.Produttore):
        return os.path.join('museo', 'logoproduttore', filename)

    raise Exception(
        'Non so dove mettere/reperire l\'immagine per il tipo "%s"'
        % instance.__class__.__name__)
