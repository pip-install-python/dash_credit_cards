# AUTO GENERATED FILE - DO NOT EDIT

export dashcreditcardinput

"""
    dashcreditcardinput(;kwargs...)
    dashcreditcardinput(children::Any;kwargs...)
    dashcreditcardinput(children_maker::Function;kwargs...)


A DashCreditCardInput component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `acceptedCards` (Array; optional)
- `cardCVCInputProps` (Dict; optional)
- `cardExpiryInputProps` (Dict; optional)
- `cardImageClassName` (String; optional)
- `cardImageStyle` (Dict; optional)
- `cardNumber` (String; optional)
- `cardNumberInputProps` (Dict; optional)
- `className` (String; optional)
- `containerClassName` (String; optional)
- `containerStyle` (Dict; optional)
- `customTextLabels` (Dict; optional)
- `cvc` (String; optional)
- `dangerTextClassName` (String; optional)
- `dangerTextStyle` (Dict; optional)
- `expiry` (String; optional)
- `fieldClassName` (String; optional)
- `fieldStyle` (Dict; optional)
- `inputClassName` (String; optional)
- `inputComponent` (String; optional)
- `inputStyle` (Dict; optional)
- `invalidClassName` (String; optional)
- `invalidStyle` (Dict; optional)
- `issuer` (String; optional)
- `placeholders` (Dict; optional)
- `preview` (Bool; optional)
- `style` (Dict; optional)
"""
function dashcreditcardinput(; kwargs...)
        available_props = Symbol[:children, :id, :acceptedCards, :cardCVCInputProps, :cardExpiryInputProps, :cardImageClassName, :cardImageStyle, :cardNumber, :cardNumberInputProps, :className, :containerClassName, :containerStyle, :customTextLabels, :cvc, :dangerTextClassName, :dangerTextStyle, :expiry, :fieldClassName, :fieldStyle, :inputClassName, :inputComponent, :inputStyle, :invalidClassName, :invalidStyle, :issuer, :placeholders, :preview, :style]
        wild_props = Symbol[]
        return Component("dashcreditcardinput", "DashCreditCardInput", "dash_credit_cards", available_props, wild_props; kwargs...)
end

dashcreditcardinput(children::Any; kwargs...) = dashcreditcardinput(;kwargs..., children = children)
dashcreditcardinput(children_maker::Function; kwargs...) = dashcreditcardinput(children_maker(); kwargs...)

