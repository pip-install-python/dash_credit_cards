# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashParallaxTilt(Component):
    """A DashParallaxTilt component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- className (string; default '')

- flipHorizontally (boolean; default False)

- flipVertically (boolean; default False)

- glareBorderRadius (string; default '0')

- glareColor (string; default '#ffffff')

- glareEnable (boolean; default False)

- glareMaxOpacity (number; default 0.7)

- glarePosition (a value equal to: 'top', 'right', 'bottom', 'left', 'all'; default 'bottom')

- glareReverse (boolean; default False)

- gyroscope (boolean; default False)

- perspective (number; default 1000)

- reset (boolean; default True)

- scale (number; default 1)

- style (dict; optional)

- tiltAngleXInitial (number; default 0)

- tiltAngleXManual (number; optional)

- tiltAngleYInitial (number; default 0)

- tiltAngleYManual (number; optional)

- tiltAxis (a value equal to: 'x', 'y'; default undefined)

- tiltEnable (boolean; default True)

- tiltMaxAngleX (number; default 20)

- tiltMaxAngleY (number; default 20)

- tiltReverse (boolean; default False)

- trackOnWindow (boolean; default False)

- transitionEasing (string; default 'cubic-bezier(.03,.98,.52,.99)')

- transitionSpeed (number; default 400)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_credit_cards'
    _type = 'DashParallaxTilt'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, tiltEnable=Component.UNDEFINED, tiltReverse=Component.UNDEFINED, tiltAngleXInitial=Component.UNDEFINED, tiltAngleYInitial=Component.UNDEFINED, tiltMaxAngleX=Component.UNDEFINED, tiltMaxAngleY=Component.UNDEFINED, tiltAxis=Component.UNDEFINED, tiltAngleXManual=Component.UNDEFINED, tiltAngleYManual=Component.UNDEFINED, glareEnable=Component.UNDEFINED, glareMaxOpacity=Component.UNDEFINED, glareColor=Component.UNDEFINED, glareBorderRadius=Component.UNDEFINED, glarePosition=Component.UNDEFINED, glareReverse=Component.UNDEFINED, scale=Component.UNDEFINED, perspective=Component.UNDEFINED, flipVertically=Component.UNDEFINED, flipHorizontally=Component.UNDEFINED, reset=Component.UNDEFINED, transitionEasing=Component.UNDEFINED, transitionSpeed=Component.UNDEFINED, trackOnWindow=Component.UNDEFINED, gyroscope=Component.UNDEFINED, onMove=Component.UNDEFINED, onEnter=Component.UNDEFINED, onLeave=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'flipHorizontally', 'flipVertically', 'glareBorderRadius', 'glareColor', 'glareEnable', 'glareMaxOpacity', 'glarePosition', 'glareReverse', 'gyroscope', 'perspective', 'reset', 'scale', 'style', 'tiltAngleXInitial', 'tiltAngleXManual', 'tiltAngleYInitial', 'tiltAngleYManual', 'tiltAxis', 'tiltEnable', 'tiltMaxAngleX', 'tiltMaxAngleY', 'tiltReverse', 'trackOnWindow', 'transitionEasing', 'transitionSpeed']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'flipHorizontally', 'flipVertically', 'glareBorderRadius', 'glareColor', 'glareEnable', 'glareMaxOpacity', 'glarePosition', 'glareReverse', 'gyroscope', 'perspective', 'reset', 'scale', 'style', 'tiltAngleXInitial', 'tiltAngleXManual', 'tiltAngleYInitial', 'tiltAngleYManual', 'tiltAxis', 'tiltEnable', 'tiltMaxAngleX', 'tiltMaxAngleY', 'tiltReverse', 'trackOnWindow', 'transitionEasing', 'transitionSpeed']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DashParallaxTilt, self).__init__(children=children, **args)
