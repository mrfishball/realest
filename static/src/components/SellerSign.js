import React, { Component } from 'react'

class SellerSign extends Component {
  handleNextClick = () => {
      this.props.nextStep()
  }

  handleBackClick = () => {
    this.props.previousStep()
  }

  render() {
    return(
      <div>
        <h2 className="section">Seller Signature</h2>
          <form class="form-horizontal">
              <fieldset>
                    <div class="control-group">
                      <label class="control-label">Full Name</label>
                      <div class="controls">
                          <input id="full-name" name="full-name" type="text" placeholder="full name"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Today's Date</label>
                      <div class="controls">
                          <input id="address-line1" name="address-line1" type="text" placeholder="Today's Date"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                    <buttom className="btn -primary pull-right" onClick={this.handleNextClick}>Next Step</buttom>
                    <button className="btn -default pull-left"onClick={this.handleBackClick}>Back</button>
              </fieldset>
          </form>
      </div>
    )
  }
}

export default SellerSign
