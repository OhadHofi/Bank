import React from 'react'
import './Category.css';

export default function Category(props) {
    const category = props.category

    return (
      <div className='category-container'>
        <table className='transaction'>
          <tr className='plus'>
            <td className='dynam-info text'>{category.category}: </td>
            <td className='dynam-info number'>{category.totalAmount}</td>
          </tr>
        </table>
      </div>
    )
}