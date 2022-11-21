import './Transaction.css';

export default function Transaction(props) {
    const transaction = props.transaction

    return (
        <div className={"transaction-container " + (transaction.amount < 0 ? 'negative' : 'non-negative')}>
            <table className='transaction'>
              <tr className='plus'>
                <td>Category: </td>
                <td className='dynam-info text'>{transaction.category}</td>
              </tr>
              <tr>
                <td>Vendor: </td>
                <td className='dynam-info text'>{transaction.vendor}</td>
              </tr>
              <tr>
                <td>Anount: </td>
                <td className='dynam-info number'>{transaction.amount}</td>
              </tr>
              <tr>
                <td colspan="2"><button className='transaction-button' onClick={()=>props.deleteTransaction(transaction.id)}>Delete</button></td>
              </tr>
            </table>
        </div>
    )
}