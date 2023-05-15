import LoadingIndicator from "../LoadingIndicator";
import SidbarNav from "../SidbarNav";
import { Alert, Col, Container, Row } from 'react-bootstrap';
import { GetResults } from "./api/results";
import ResultCard from "./ResultCard";


const Results = () => {
    
    const {loading, results, error} = GetResults();


    return (
        <SidbarNav>
                <Container>
      {loading ? (
        <LoadingIndicator className="align-content-center" />
      ) : error ? (
        <Alert variant="danger">{error}</Alert>
      ) : results.length ? (
        <div>
          <h1>Results</h1>
          <Row>
            {results.map((result) => (
              <Col key={result.id} sm={6} md={4} lg={3} className="mb-3">
                <ResultCard result={result}></ResultCard>
              </Col>
            ))}
          </Row>
        </div>
      ): <Alert style={{margin: "10px"}} variant="info">No results published, stay tuned.</Alert>}
    </Container>
        </SidbarNav>
        )
}

export default Results;