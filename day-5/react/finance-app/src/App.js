import React, { useState, useEffect } from 'react';
import api from './api';
import './App.css';

function App() {
  const [transactions, setTransactions] = useState([]);
  const [formData, setFormData] = useState({
    amount: '',
    category: '',
    description: '',
    is_income: false,
    date: '',
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const response = await api.get('/transactions/');
        setTransactions(response.data);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };
    fetchTransactions();
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: type === 'checkbox' ? checked : value,
    }));
  }

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/transactions/', formData);
      setTransactions((prev) => [response.data, ...prev]);
      setFormData({
        amount: '',
        category: '',
        description: '',
        is_income: false,
        date: '',
      });
      setError(null);
    } catch (error) {
      setError(error);
    }
  };

  return (
    <div className="App">
      <h1>Finance Transactions</h1>
      <form onSubmit={handleSubmit} className="transaction-form">
        <input
          type="number"
          name="amount"
          placeholder="Amount"
          value={formData.amount}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="category"
          placeholder="Category"
          value={formData.category}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="description"
          placeholder="Description"
          value={formData.description}
          onChange={handleChange}
        />
        <label>
          Income?
          <input
            type="checkbox"
            name="is_income"
            checked={formData.is_income}
            onChange={handleChange}
          />
        </label>
        <input
          type="date"
          name="date"
          value={formData.date}
          onChange={handleChange}
          required
        />
        <button type="submit">Add Transaction</button>
      </form>
      <h2>Transactions List</h2>
      <ul className="transaction-list">
        {transactions.map((transaction) => (
          <li key={transaction.id} className={transaction.is_income ? 'income' : 'expense'}>
            <span>{transaction.date}</span> | 
            <span>{transaction.category}</span> | 
            <span>{transaction.description}</span> | 
            <span>{transaction.is_income ? '+' : '-'}${transaction.amount}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
