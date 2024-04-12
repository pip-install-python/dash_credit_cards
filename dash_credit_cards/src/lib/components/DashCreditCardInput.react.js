import React, { Component } from 'react';
import PropTypes from 'prop-types';
import CreditCardInput from 'react-credit-card-input';

class DashCreditCardInput extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cardNumber: '',
            expiry: '',
            cvc: '',
        };
         // Bind the methods
        this.handleCardNumberChange = this.handleCardNumberChange.bind(this);
        this.handleExpiryChange = this.handleExpiryChange.bind(this);
        this.handleCvcChange = this.handleCvcChange.bind(this);
    }

    handleCardNumberChange(e) {
        this.setState({ cardNumber: e.target.value });
        if (this.props.setProps) {
            this.props.setProps({ cardNumber: e.target.value });
        }
    }

    handleExpiryChange(e) {
        this.setState({ expiry: e.target.value });
        if (this.props.setProps) {
            this.props.setProps({ expiry: e.target.value });
        }
    }

    handleCvcChange(e) {
        this.setState({ cvc: e.target.value });
        if (this.props.setProps) {
            this.props.setProps({ cvc: e.target.value });
        }
    }

    componentDidUpdate(prevProps) {
        if (this.props.cardNumber !== prevProps.cardNumber) {
            this.setState({ cardNumber: this.props.cardNumber });
        }
        if (this.props.expiry !== prevProps.expiry) {
            this.setState({ expiry: this.props.expiry });
        }
        if (this.props.cvc !== prevProps.cvc) {
            this.setState({ cvc: this.props.cvc });
        }
    }
    render() {
        const { id, children, style, className, ...otherProps } = this.props;
        const { cardNumber, expiry, cvc } = this.state;

        return (
            <CreditCardInput
                className={className}
                {...otherProps}
                cardNumberInputProps={{ value: cardNumber, onChange: this.handleCardNumberChange }}
                cardExpiryInputProps={{ value: expiry, onChange: this.handleExpiryChange }}
                cardCVCInputProps={{ value: cvc, onChange: this.handleCvcChange }}
            >
                <div id={id} style={{ ...style }}>
                    {children}
                </div>
            </CreditCardInput>
        );
    }
}

DashCreditCardInput.defaultProps = {
    cardNumber: '',
    expiry: '',
    cvc: '',
};

DashCreditCardInput.propTypes = {
    id: PropTypes.string,
    children: PropTypes.node,
    style: PropTypes.object,
    className: PropTypes.string,
    cardNumberInputProps: PropTypes.object,
    cardExpiryInputProps: PropTypes.object,
    cardCVCInputProps: PropTypes.object,
    fieldClassName: PropTypes.string,
    inputComponent: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    containerClassName: PropTypes.string,
    customTextLabels: PropTypes.object,
    placeholders: PropTypes.object,
    issuer: PropTypes.string,
    preview: PropTypes.bool,
    acceptedCards: PropTypes.array,
    callback: PropTypes.func,
    onError: PropTypes.func,
    cardNumberInputRenderer: PropTypes.func,
    cardExpiryInputRenderer: PropTypes.func,
    cardCVCInputRenderer: PropTypes.func,
    cardImageClassName: PropTypes.string,
    cardImageStyle: PropTypes.object,
    containerStyle: PropTypes.object,
    dangerTextClassName: PropTypes.string,
    dangerTextStyle: PropTypes.object,
    fieldStyle: PropTypes.object,
    inputClassName: PropTypes.string,
    inputStyle: PropTypes.object,
    invalidClassName: PropTypes.string,
    invalidStyle: PropTypes.object,
    cardNumber: PropTypes.string,
    expiry: PropTypes.string,
    cvc: PropTypes.string,
    setProps: PropTypes.func,
};

export default DashCreditCardInput;