# AUTO GENERATED FILE - DO NOT EDIT

export dashcreditcards

"""
    dashcreditcards(;kwargs...)

A DashCreditCards component.

Keyword arguments:
- `id` (String; optional)
- `acceptedCards` (Array; optional)
- `cvc` (String | Real; optional)
- `expiry` (String | Real; optional)
- `focused` (String; optional)
- `issuer` (String; optional)
- `locale` (Dict; optional)
- `name` (String | Real; optional)
- `number` (String | Real; optional)
- `placeholders` (Dict; optional)
- `preview` (Bool; optional)
"""
function dashcreditcards(; kwargs...)
        available_props = Symbol[:id, :acceptedCards, :cvc, :expiry, :focused, :issuer, :locale, :name, :number, :placeholders, :preview]
        wild_props = Symbol[]
        return Component("dashcreditcards", "DashCreditCards", "dash_credit_cards", available_props, wild_props; kwargs...)
end

