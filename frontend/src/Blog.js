import React, { Component } from 'react';
import Post from './Post'

class Blog extends Component {

    constructor(props) {
        super(props)
        this.state = {
            posts: []
        }
    }

    componentDidMount() {
        fetch('http://localhost:5000/blog/post')
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                this.setState({posts: data})
            })
    }

    render() {
        return (
            <div>
                {this.state.posts.map((post, index) =>
                    <Post
                        key={post.id}
                        title={post.title}
                        content={post.content}
                        date={post.date}/>)
                }
            </div>
        )
    }
}

export default Blog
