import React, { useState } from 'react'
import axios from "axios";
import './Operations.css';

// import { POST_TRANSACTION } from "../../consts";

const POST_TRANSACTION = 'http://localhost:8000/transactions'

export default function Operations() {
    const [transactionInput, setTransactionInput] = useState({amount: '', vendor: '' , category:''})

    const postTransaction = function(transaction){
        axios.post(POST_TRANSACTION, transaction)
        .then(function (response) { console.log(response); })
        .catch(function (error) { console.error(error); });
    }

    const hendleInput = function(event){
        const name = event.target.name
        const value = event.target.value
        setTransactionInput({...transactionInput, [name]:value})
    }

    const addTransaction = function(coefficient){
        const transaction = {...transactionInput}
        transaction.amount = coefficient * transaction.amount
        postTransaction(transaction)
    }

    return (
      <div className='operation-container'>
          <input name='amount' value={transactionInput.amount} onChange={hendleInput} type="number" placeholder='Transaction amount'/>
          <input name='vendor' value={transactionInput.vendor} onChange={hendleInput} type="text" placeholder='Transaction vendor'/>
          <input name='category' value={transactionInput.category} onChange={hendleInput} type="text" placeholder='Transaction category'/>
          <button className='operation-button deposit' onClick={()=>addTransaction(1)}>Deposit</button>
          <button className='operation-button withdrow' onClick={()=>addTransaction(-1)}>Withdraw</button>
      </div>
    )
}