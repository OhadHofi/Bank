import React from 'react'
import { Link } from 'react-router-dom'
import Balance from '../balance/Balance'
import './Header.css';

export default function Header() {
    return (
        <div className="header-container">
            <Link to="/transactions" className='link'>Transactions</Link>
            <Link to="/operations" className='link'>Operations</Link>
            <Link to="/breakdown" className='link'>Breakdown</Link>
            <Balance />
        </div>
    )
}
