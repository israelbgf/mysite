import React, { Component } from 'react';

class PostReader extends Component {

    constructor(props) {
        super(props)
        this.state = {
            post: {}
        }
    }


    componentDidMount() {
        fetch(`http://localhost:5000/blog/${this.props.params.slug}`)
            .then((response) => {
                if (response.ok)
                    response.json().then((data) =>
                        this.setState({post: data}))
            })
    }


    render() {
        return (
            <div>
                <h1>{this.state.post.title}</h1>
                <p>{this.state.post.date}</p>
                <p>{this.state.post.content}</p>
            </div>
        )
    }


}

export default PostReader
