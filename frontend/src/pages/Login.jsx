import React from 'react'
import Form from '../components/Form'

const Login = () => {
    console.log('login')
  return <Form route='/api/token' method="login" />
}

export default Login;