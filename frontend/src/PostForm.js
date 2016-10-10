import React, { Component } from 'react';
import { browserHistory } from 'react-router'

class PostForm extends Component {

    constructor(props) {
        super(props)
        this.state = {
            post: {
                title: '',
                slug: '',
                content: '',
            }
        }

        this.onChangeTitleHandler = this.onChangeInput.bind(this, 'title')
        this.onChangeSlugHandler = this.onChangeInput.bind(this, 'slug')
        this.onChangeContentHandler = this.onChangeInput.bind(this, 'content')
    }

    onChangeInput(field, event) {
        const value = event.target.value
        const post = {...this.state.post}
        post[field] = value
        this.setState({post})
    }

    componentDidMount() {
        if (this.props.params.id)
            fetch(`http://localhost:5000/blog/post/${this.props.params.id}`)
                .then((response) => {
                    return response.json().then((data) => {
                        this.setState({post: data})
                    })
                })
    }


    render() {
        return (
            <div>
                <h1>{this.state.post.id ? 'Update Post': 'New Post'}</h1>
                <form onSubmit={this.handleSubmit.bind(this)}>
                    <div>
                        <label htmlFor='title'>Title</label>
                        <input onChange={this.onChangeTitleHandler} value={this.state.post.title}/>
                        <span style={{color: 'red'}}>{this.state.post.title ? '' : '*'}</span>
                    </div>
                    <div>
                        <label htmlFor='slug'>Slug</label>
                        <input onChange={this.onChangeSlugHandler} value={this.state.post.slug}/>
                        <span style={{color: 'red'}}>{this.state.post.slug ? '' : '*'}</span>
                    </div>
                    <div>
                        <label htmlFor='content'>Content</label>
                        <textarea onChange={this.onChangeContentHandler} value={this.state.post.content}/>
                        <span style={{color: 'red'}}>{this.state.post.content ? '' : '*'}</span>
                    </div>
                    <div>
                        <input type='submit' value='Submit'/>
                    </div>
                </form>
            </div>
        )
    }

    handleSubmit(event) {
        event.preventDefault()
        if (this.state.post.title && this.state.post.slug && this.state.post.content)
            this.createPost()
    }

    createPost() {
        let editURL = ''
        let method = 'post'
        if (this.props.params.id) {
            editURL = '/' + this.props.params.id
            method = 'put'
        }

        fetch(`http://localhost:5000/blog/post${editURL}`, {
            method: method,
            body: JSON.stringify({
                title: this.state.post.title,
                slug: this.state.post.slug,
                content: this.state.post.content,
            }),
            headers: {'Content-Type': 'application/json'}
        }).then((response) => {
            if (response.ok) {
                alert('Post created.')
                browserHistory.push('/blog/')
            }
        })

    }
}

export default PostForm
