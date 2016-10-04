import React, { Component } from 'react';
import { Link } from 'react-router'

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
                return response.json().then((data) => {
                    this.setState({posts: data})
                })
            })
    }

    render() {
        return (
            <div>
                <ol>
                    {this.state.posts.map((post, index) =>
                        <li key={post.id}>
                            <Link to={`/blog/${post.slug}/`}>{post.title}</Link>
                            <p>{post.date}</p>
                        </li>)
                    }
                </ol>
                <Link to='/blog/post'>New Post</Link>
            </div>
        )
    }
}

export default Blog
