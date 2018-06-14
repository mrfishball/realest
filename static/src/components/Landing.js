import React, { Component } from 'react';

class Landing extends Component {

  handleClick = () => {
    this.props.nextStep()
  }

  render() {
    return (
      <div>
        <p>This form is used to make an offer to purchase real estate.
        The form is completed by a potential Buyer then presented to the Seller, outlining the basic terms under which the potential Buyer would purchase the property.
  If the proposed terms offered by the Buyer are acceptable to the Seller, the Seller signs the Offer Form to begin the sales transaction.
  If the terms offered are NOT acceptable to the Seller, the Seller can either make and initial changes to the form then return it unsigned to the Buyer to initial,
  or the Seller can prepare a brand new form as a Counter-Offer and present that new version to the Buyer.
  Only when the Buyer and Seller both agree to the terms on the Offer Form should the document contain signatures from both parties.
  (Please note that this is a demo version of the OPT website which is
  still in its development phase.)</p>
<button className="btn -primary center" onClick={this.handleClick}>Start</button>
      </div>
    )
  }
}

export default Landing
