import React, { useState , useEffect } from 'react'
import axios from "axios";
import Transaction from '../Transaction/Transaction';
import './Transactions.css';

// import { GET_ALL_TRANSACTIONS } from "../../consts";

const TRANSACTIONS_API = 'http://localhost:8000/transactions'

export default function Transactions() {

    const [transactions, setTransactions] = useState([])

    useEffect(()=>{
        getAllTransactions()
    },[])

    const getAllTransactions = async function(){
        const response = await axios.get(TRANSACTIONS_API)
        setTransactions(response.data.transactions)
    }

    const deleteTransaction = async function(id){
        axios.delete(`http://localhost:8000/transactions/${id}`)
        .then(function (response) { 
            console.log(response); 
            getAllTransactions()
        })
        .catch(function (error) { console.error(error); });
    }

    return (
      <div className='transactions-container'>
          {transactions.map(transaction => (
            <Transaction key={transaction.id} transaction={transaction} deleteTransaction={deleteTransaction}></Transaction>
          ))}
      </div>
    )
}