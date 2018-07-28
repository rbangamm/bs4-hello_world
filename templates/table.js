'use strict';

class Table extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      reviewer: null,
      time_requested: null,
      table: [],
      isLoaded: false
    };
  }

  componentDidMount() {
    fetch("http://localhost:5000/api/tables/ign")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
          	reviewer = result.reviewer,
          	time_requested = result.time_requested,
            table: result.table,
            isLoaded: true
          });
        }
      )
  }

  render() {
    const { reviewer, time_requested, table, isLoaded } = this.state
  	return table
  }
}

ReactDOM.render(
	<Table />,
	document.getElementById('ign')
);

ReactDOM.render(
	<Table />,
	document.getElementById('metacritic')
);