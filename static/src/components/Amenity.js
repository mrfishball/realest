import React, { Component } from 'react'

class Amenity extends Component {
  handleNextClick = () => {
      this.props.nextStep()
  }

  handleBackClick = () => {
    this.props.previousStep()
  }

  render() {
    return(
      <div>
        <h2 className="section">Amenity</h2>
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
                      <label class="control-label">Address Line 1</label>
                      <div class="controls">
                          <input id="address-line1" name="address-line1" type="text" placeholder="Street address, P.O. box, company name, c/o"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Address Line 2</label>
                      <div class="controls">
                          <input id="address-line2" name="address-line2" type="text" placeholder="Apartment, suite , unit, building, floor, etc."
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">City / Town</label>
                      <div class="controls">
                          <input id="city" name="city" type="text" placeholder="city" class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">State / Province / Region</label>
                      <div class="controls">
                          <input id="region" name="region" type="text" placeholder="state / province / region"
                          class="input-xlarge"/>
                          <p class="help-block"></p>
                      </div>
                  </div>
                  <div class="control-group">
                      <label class="control-label">Zip / Postal Code</label>
                      <div class="controls">
                          <input id="postal-code" name="postal-code" type="text" placeholder="zip or postal code"
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

export default Amenity
