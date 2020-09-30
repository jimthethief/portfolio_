import React from 'react';
import { Row, Col, Accordion, Card, Image } from 'react-bootstrap';
import ProjectLinks from './ProjectLinks';
import ProjectIcons from './ProjectIcons';
import ProjectPercent from './ProjectPercent';


class Project extends React.Component {
    constructor(props) {
        super(props);
        this.wrapper = React.createRef();
    }

    render() {
        return (
            <Row ref={this.wrapper} className={`project-row bg-${this.props.project.title}`}>
                <Col md={
                    this.props.project.priority % 2 == 0
                    ? {span: 6, order: 'last'}
                    : {span: 6, order: 'first'}
                } className="stack-col">
                    <div className="img-container mx-auto">
                    <div className="img-overlay"></div>
                    <code className="large img-overlay-title">{this.props.project.title}</code>
                    <Image className="project-image" src={this.props.project.media[0].project_image} fluid />
                    </div>
                    {this.props.project.hobby_server && 
                            (<Row className="hobby text-center justify-content-center">
                                <code className="hobby-text"><i className="hobby-bot fas fa-robot"></i>
                                &nbsp;Bear with me while I boot up - I'm on a hobby server
                                </code>
                            </Row>)
                    }
                    
                    <ProjectLinks links={this.props.project.links} project={this.props.project.title} />

                </Col>
                <Col md={
                    this.props.project.priority % 2 == 0
                    ? {span: 6, order: 'first'}
                    : {span: 6, order: 'last'}
                } className="my-auto stack-col">
                    <Accordion className="mx-auto text-center">
                    <div className="project-cards">
                        <Card>
                            <Accordion.Toggle className={`${this.props.project.title} rounded-0`} as={Card.Header} eventKey="0">

                            <code>Summary</code>

                            </Accordion.Toggle>
                            <Accordion.Collapse eventKey="0">
                                <Card.Body>
                                
                                {this.props.project.summary}
                                
                                </Card.Body>
                            </Accordion.Collapse>
                        </Card>
                        <Card>
                            <Accordion.Toggle className={`${this.props.project.title} rounded-0`} as={Card.Header} eventKey="1">

                            <code>Tools</code>

                            </Accordion.Toggle>

                            <Accordion.Collapse eventKey="1">
                            <Card.Body>

                                <ProjectIcons languageInfo={this.props.project.languages}/>

                            </Card.Body>
                            </Accordion.Collapse>
                        </Card>
                        <Card>
                            <Accordion.Toggle className={`${this.props.project.title} rounded-0`} as={Card.Header} eventKey="2">

                            <code>%</code>

                            </Accordion.Toggle>
                            <Accordion.Collapse eventKey="2">
                            <Card.Body>

                                <ProjectPercent languageInfo={this.props.project.languages}/>

                            </Card.Body>
                            </Accordion.Collapse>
                        </Card>
                    </div>
                    </Accordion>
                </Col>
            </Row>
        );
    }
}

export default Project;