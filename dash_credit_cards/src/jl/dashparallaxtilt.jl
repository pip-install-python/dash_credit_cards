# AUTO GENERATED FILE - DO NOT EDIT

export dashparallaxtilt

"""
    dashparallaxtilt(;kwargs...)
    dashparallaxtilt(children::Any;kwargs...)
    dashparallaxtilt(children_maker::Function;kwargs...)


A DashParallaxTilt component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `flipHorizontally` (Bool; optional)
- `flipVertically` (Bool; optional)
- `glareBorderRadius` (String; optional)
- `glareColor` (String; optional)
- `glareEnable` (Bool; optional)
- `glareMaxOpacity` (Real; optional)
- `glarePosition` (a value equal to: 'top', 'right', 'bottom', 'left', 'all'; optional)
- `glareReverse` (Bool; optional)
- `gyroscope` (Bool; optional)
- `perspective` (Real; optional)
- `reset` (Bool; optional)
- `scale` (Real; optional)
- `style` (Dict; optional)
- `tiltAngleXInitial` (Real; optional)
- `tiltAngleXManual` (Real; optional)
- `tiltAngleYInitial` (Real; optional)
- `tiltAngleYManual` (Real; optional)
- `tiltAxis` (a value equal to: 'x', 'y'; optional)
- `tiltEnable` (Bool; optional)
- `tiltMaxAngleX` (Real; optional)
- `tiltMaxAngleY` (Real; optional)
- `tiltReverse` (Bool; optional)
- `trackOnWindow` (Bool; optional)
- `transitionEasing` (String; optional)
- `transitionSpeed` (Real; optional)
"""
function dashparallaxtilt(; kwargs...)
        available_props = Symbol[:children, :id, :className, :flipHorizontally, :flipVertically, :glareBorderRadius, :glareColor, :glareEnable, :glareMaxOpacity, :glarePosition, :glareReverse, :gyroscope, :perspective, :reset, :scale, :style, :tiltAngleXInitial, :tiltAngleXManual, :tiltAngleYInitial, :tiltAngleYManual, :tiltAxis, :tiltEnable, :tiltMaxAngleX, :tiltMaxAngleY, :tiltReverse, :trackOnWindow, :transitionEasing, :transitionSpeed]
        wild_props = Symbol[]
        return Component("dashparallaxtilt", "DashParallaxTilt", "dash_credit_cards", available_props, wild_props; kwargs...)
end

dashparallaxtilt(children::Any; kwargs...) = dashparallaxtilt(;kwargs..., children = children)
dashparallaxtilt(children_maker::Function; kwargs...) = dashparallaxtilt(children_maker(); kwargs...)

