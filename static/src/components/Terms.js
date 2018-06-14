import React, { Component } from 'react'

class Terms extends Component {
  handleNextClick = () => {
      this.props.nextStep()
  }

  handleBackClick = () => {
    this.props.previousStep()
  }

  render() {
    return(
      <div>
        <h2 className="section">Terms</h2>
          <form class="form-horizontal">
              <fieldset>
                    <div class="control-group">
                      <label class="control-label">Selling Price</label>
                      <div class="controls">
                          <input id="full-name" name="full-name" type="text" placeholder="Selling Price"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Contract Down Payment</label>
                      <div class="controls">
                          <input id="address-line1" name="address-line1" type="text" placeholder="Contract Down Payment"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Closing Down Payment</label>
                      <div class="controls">
                          <input id="address-line2" name="address-line2" type="text" placeholder="Closing Down Payment"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Loan Amount</label>
                      <div class="controls">
                          <input id="city" name="city" type="text" placeholder="Loan Amount" class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Loan Type</label>
                      <div class="controls">
                          <input id="region" name="region" type="text" placeholder="Loan Type"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Anticipated Closing Date</label>
                      <div class="controls">
                          <input id="postal-code" name="postal-code" type="text" placeholder="Anticipated Closing Date"
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

export default Terms
