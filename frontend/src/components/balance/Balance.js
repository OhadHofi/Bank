import React, { useState , useEffect } from 'react'
import axios from "axios";
import './Balance.css';

const TRANSACTIONS_API = 'http://localhost:8000/transactions/balance'
const SECOND = 1000

export default function Balance() {

    const [balance, setBalance] = useState(0)

    useEffect(()=>{
        featchBalance()
        // setInterval(featchBalance, SECOND);
    },[])

    const featchBalance = async function(){
        const response = await axios.get(TRANSACTIONS_API)
        console.log(response)
        setBalance(response.data.balance)
    }
    
    return (
      <div className='balance-container'>
          <p>Balance: {balance}</p>
      </div>
    )
}