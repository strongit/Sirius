import React from 'react'
import Task from 'public/Task'
import './index.less'
import Percentage from 'bfd-ui/lib/Percentage'

const TabMonitor = React.createClass({
  render: function() {
    return (
        <div className="row">
          <div className="col-sm-6 col-md-4 col-lg-3">
            <div className="thumbnail function-service-div-border" style={{width:'100px'}}><a href="javascript:">space1</a></div>
            <div className="caption"><Percentage percent={30} style={{width: '150px'}}></Percentage></div>
          </div>
          <div className="col-sm-6 col-md-4 col-lg-3">
            <div className="thumbnail function-service-div-border" style={{width:'100px'}}><a href="javascript:">space2</a></div>
            <div className="caption"><Percentage percent={30} style={{width: '150px'}}></Percentage></div>
          </div>
          <div className="col-sm-6 col-md-4 col-lg-3">
            <div className="thumbnail function-service-div-border" style={{width:'100px'}}><a href="javascript:">space3</a></div>
            <div className="caption"><Percentage percent={30} style={{width: '150px'}}></Percentage></div>
          </div>
          <div className="col-sm-6 col-md-4 col-lg-3">
            <div className="thumbnail function-service-div-border" style={{width:'100px'}}><a href="javascript:">space4</a></div>
            <div className="caption"><Percentage percent={30} style={{width: '150px'}}></Percentage></div>
          </div>
          <div className="col-sm-6 col-md-4 col-lg-3">
            <div className="thumbnail function-service-div-border" style={{width:'100px'}}><a href="javascript:">space5</a></div>
            <div className="caption"><Percentage percent={30} style={{width: '150px'}}></Percentage></div>
          </div>
        </div>
      );
    }
});
export default TabMonitor