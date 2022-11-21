import './App.css';
import React from 'react'
import { BrowserRouter as Router, Link, Route} from 'react-router-dom'
import Home from './components/home/Home';
import Transactions from './components/transactions/Transactions';
import Operations from './components/operations/Operations';
import Breakdown from './components/breakdown/Breakdown';
import Header from './components/header/Header';

function App() {
  return (
    <Router>
        <div className="App">
          <Header />
          <Route path="/" exact component={Home} />
          <Route path='/transactions' exact component={Transactions} />
          <Route path='/operations' exact component={Operations} />
          <Route path='/breakdown' exact component={Breakdown} />
          {/* <Route path="/catalog" exact render={({ match }) => <Catalog match={match} movies={this.state.movies} toggle={this.toggle} />}/> */}
          {/* <Route path="/movie/:id" exact render={({ match }) => <MovieInfo match={match} movies={this.state.movies}/>} /> */}
        </div>
    </Router>
  );
}

export default App;
