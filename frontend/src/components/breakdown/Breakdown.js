import React, { useState , useEffect } from 'react'
import axios from "axios"
import Category from '../category/Category'
// import { GET_TRANSACTIONS_SUMMARY_BY_CATEGORY } from "../../consts";
import './Breakdown.css';

const GET_TRANSACTIONS_SUMMARY_BY_CATEGORY = 'http://localhost:8000/transactions/category'

export default function Breakdown() {
    const [breakdown, setBreakdown] = useState([])

    useEffect(()=>{
        fetchSumTransactionByCategory()
    },[])

    const fetchSumTransactionByCategory = async function(){
        const response = await axios.get(GET_TRANSACTIONS_SUMMARY_BY_CATEGORY)
        setBreakdown(response.data)
    }

    return (
      <div className='breakdown-container'>
            <h2 className="title">Breakdown</h2>
            <div className='category-info-container'>
                {breakdown.map((category, id) => (
                    <Category key={id} category={category} />
                ))}
            </div>
      </div>
    )
}