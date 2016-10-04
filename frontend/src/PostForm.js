import React, { Component } from 'react';


class PostForm extends Component {

    constructor(props) {
        super(props)
        this.state = {
            title: '',
            slug: '',
            content: '',
        }

        this.onChangeTitleHandler = this.onChangeInput.bind(this, 'title')
        this.onChangeSlugHandler = this.onChangeInput.bind(this, 'slug')
        this.onChangeContentHandler = this.onChangeInput.bind(this, 'content')
    }

    onChangeInput(field, event) {
        const value = event.target.value
        const state = {}
        state[field] = value
        this.setState(state)
    }

    render() {
        return (
            <div>
                <h1>New Post</h1>
                <form onSubmit={this.handleSubmit.bind(this)}>
                    <div>
                        <label htmlFor='title'>Title</label>
                        <input onChange={this.onChangeTitleHandler}/>
                        <span style={{color: 'red'}}>{this.state.title ? '' : '*'}</span>
                    </div>
                    <div>
                        <label htmlFor='slug'>Slug</label>
                        <input onChange={this.onChangeSlugHandler}/>
                        <span style={{color: 'red'}}>{this.state.slug ? '' : '*'}</span>
                    </div>
                    <div>
                        <label htmlFor='content'>Content</label>
                        <textarea onChange={this.onChangeContentHandler}/>
                        <span style={{color: 'red'}}>{this.state.content ? '' : '*'}</span>
                    </div>
                    <div>
                        <input type='submit' value='Pos'/>
                    </div>
                </form>
            </div>
        )
    }

    handleSubmit(event) {
        event.preventDefault()
        if(this.state.title && this.state.slug && this.state.content)
            console.log('valid!')
    }

}

export default PostForm
