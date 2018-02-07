import React, { Component } from 'react';
import './Snippet.css';

class Snippet extends Component {
    state = {
        apiUrl: this.props.location.state.apiUrl,
    };


    Snippet() {

    }

    componentDidMount() {
        this.Snippet();
    }

    render() {
        return (
            <div className="Snippet">
                {this.state.apiUrl}
            </div>
        );
    }
}

export default Snippet;
