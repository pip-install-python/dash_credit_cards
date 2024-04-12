import React from 'react';
import PropTypes from 'prop-types';
import Cards from 'react-credit-cards';
import 'react-credit-cards/es/styles-compiled.css';
const DashCreditCards = (props) => {
    const { id, name, number, expiry, cvc, focused, locale, placeholders, preview, issuer, acceptedCards } = props;

    return (
        <div id={id}>
            <Cards
                name={name}
                number={number}
                expiry={expiry}
                cvc={cvc}
                focused={focused}
                locale={locale}
                placeholders={placeholders}
                preview={preview}
                issuer={issuer}
                acceptedCards={acceptedCards}
            />

        </div>
    );
}

DashCreditCards.defaultProps = {

};

DashCreditCards.propTypes = {
    id: PropTypes.string,
    name: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    number: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    expiry: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    cvc: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    focused: PropTypes.string,
    locale: PropTypes.object,
    placeholders: PropTypes.object,
    preview: PropTypes.bool,
    issuer: PropTypes.string,
    acceptedCards: PropTypes.array,
};

export default DashCreditCards;
