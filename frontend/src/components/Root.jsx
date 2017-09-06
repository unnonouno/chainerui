import React from 'react';
import { Provider } from 'react-redux';
import { Router, Route, browserHistory } from 'react-router';
import { persistStore } from 'redux-persist';
import { syncHistoryWithStore } from 'react-router-redux';
import configureStore from '../store/configureStore';
import ChainerUIContainer from '../containers/ChainerUIContainer';
import ResultDetail from '../containers/ResultDetail';


const store = configureStore();
const history = syncHistoryWithStore(browserHistory, store);

class Root extends React.Component {
  constructor() {
    super();
    this.state = {
      rehydrated: false
    };
  }

  componentDidMount() {
    persistStore(store, {}, () => {
      this.setState({ rehydrated: true });
    });
  }

  render() {
    if (!this.state.rehydrated) {
      return (<div>loading...</div>);
    }
    return (
      <Provider store={store}>
        <Router history={history}>
          <Route path="/" component={ChainerUIContainer} />
          <Route path="/results/(:resultId)" component={ResultDetail} />
        </Router>
      </Provider>
    );
  }
}

export default Root;

