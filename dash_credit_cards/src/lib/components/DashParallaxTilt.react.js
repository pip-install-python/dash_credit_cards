import React from 'react';
import PropTypes from 'prop-types';
import Tilt from 'react-parallax-tilt';

const DashParallaxTilt = (props) => {
    const {id, children, style, className, ...tiltProps} = props;

    return (
        <Tilt className={className} {...tiltProps}>
            <div id={id} style={{ ...style }}>
                {children}
            </div>
        </Tilt>
    );
}

DashParallaxTilt.defaultProps = {
    className: '',
    tiltEnable: true,
    tiltReverse: false,
    tiltAngleXInitial: 0,
    tiltAngleYInitial: 0,
    tiltMaxAngleX: 20,
    tiltMaxAngleY: 20,
    tiltAxis: undefined,
    tiltAngleXManual: null,
    tiltAngleYManual: null,
    glareEnable: false,
    glareMaxOpacity: 0.7,
    glareColor: '#ffffff',
    glareBorderRadius: '0',
    glarePosition: 'bottom',
    glareReverse: false,
    scale: 1,
    perspective: 1000,
    flipVertically: false,
    flipHorizontally: false,
    reset: true,
    transitionEasing: 'cubic-bezier(.03,.98,.52,.99)',
    transitionSpeed: 400,
    trackOnWindow: false,
    gyroscope: false,
    onMove: () => {},
    onEnter: () => {},
    onLeave: () => {},
};

DashParallaxTilt.propTypes = {
    id: PropTypes.string,
    children: PropTypes.node,
    style: PropTypes.object,
    className: PropTypes.string,
    tiltEnable: PropTypes.bool,
    tiltReverse: PropTypes.bool,
    tiltAngleXInitial: PropTypes.number,
    tiltAngleYInitial: PropTypes.number,
    tiltMaxAngleX: PropTypes.number,
    tiltMaxAngleY: PropTypes.number,
    tiltAxis: PropTypes.oneOf(['x', 'y']),
    tiltAngleXManual: PropTypes.number,
    tiltAngleYManual: PropTypes.number,
    glareEnable: PropTypes.bool,
    glareMaxOpacity: PropTypes.number,
    glareColor: PropTypes.string,
    glareBorderRadius: PropTypes.string,
    glarePosition: PropTypes.oneOf(['top', 'right', 'bottom', 'left', 'all']),
    glareReverse: PropTypes.bool,
    scale: PropTypes.number,
    perspective: PropTypes.number,
    flipVertically: PropTypes.bool,
    flipHorizontally: PropTypes.bool,
    reset: PropTypes.bool,
    transitionEasing: PropTypes.string,
    transitionSpeed: PropTypes.number,
    trackOnWindow: PropTypes.bool,
    gyroscope: PropTypes.bool,
    onMove: PropTypes.func,
    onEnter: PropTypes.func,
    onLeave: PropTypes.func,
};

export default DashParallaxTilt;