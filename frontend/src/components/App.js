import React, { Component } from "react";
import { render } from "react-dom";
import Form from "@rjsf/core";


const log = (type) => console.log.bind(console, type);


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      schema: {},
      loaded: false,
      placeholder: "Loading",
      uiSchema: {body: {"ui:widget": "textarea"}},
    };
  }

  componentDidMount() {
    fetch("/openapi/?format=openapi-json")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          const schema = data.paths['http://127.0.0.1:8000/api/homepages/'].post.requestBody.content["application/json"].schema
          return {
            schema: {
              title: "Homepage",
              type: "object",
              required: schema.required,
              properties: schema.properties,
            },
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <div className="container-fluid">
        <div className="page-header">
          <h1>Wagtail model to React form via Open</h1>
          <div className="row">
            <div className="col-sm-8">
              <Form
                  schema={this.state.schema}
                  uiSchema={this.state.uiSchema}
                  onChange={log("changed")}
                  onSubmit={log("submitted")}
                  onError={log("errors")}
              />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
