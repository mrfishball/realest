import React, { Component } from 'react'
import Landing from './Landing'
import Property from './Property'
import Seller from './Seller'
import Buyer from './Buyer'
import Terms from './Terms'
import Condition from './Condition'
import Amenity from './Amenity'
import Listing from './Listing'
import Selling from './Selling'
import SAttorney from './SAttorney'
import BAttorney from './BAttorney'
import SellerSign from './SellerSign'
import BuyerSign from './BuyerSign'
import Success from './Success'
import '../styles/index.css'

class OTP extends Component {
  state = {
    step: 0,
  }

  nextStep = () => {
    this.setState((state) => {
      return { step: state.step + 1 }
    })
  }

  previousStep = () => {
    this.setState((state) => {
      return { step: state.step - 1 }
    })
  }

  showStep = () => {
    switch (this.state.step) {
      case 1:
        return <Property nextStep={this.nextStep}
                         previousStep={this.previousStep} />
      case 2:
        return <Seller nextStep={this.nextStep}
                       previousStep={this.previousStep} />
      case 3:
        return <Buyer nextStep={this.nextStep}
                       previousStep={this.previousStep} />
      case 4:
        return <Terms nextStep={this.nextStep}
                      previousStep={this.previousStep} />
      case 5:
        return <Condition nextStep={this.nextStep}
                          previousStep={this.previousStep} />
      case 6:
        return <Amenity nextStep={this.nextStep}
                      previousStep={this.previousStep} />
      case 7:
        return <Listing nextStep={this.nextStep}
                          previousStep={this.previousStep} />
      case 8:
        return <Selling nextStep={this.nextStep}
                        previousStep={this.previousStep} />
      case 9:
        return <SAttorney nextStep={this.nextStep}
                          previousStep={this.previousStep} />
      case 10:
        return <BAttorney nextStep={this.nextStep}
                          previousStep={this.previousStep} />
      case 11:
        return <SellerSign nextStep={this.nextStep}
                           previousStep={this.previousStep} />
      case 12:
        return <BuyerSign nextStep={this.nextStep}
                          previousStep={this.previousStep} />
      case 13:
        return <Success />
      default:
        return <Landing nextStep={this.nextStep} />

    }
  }

  render() {
    let style = {
     width: (this.state.step / 13 * 100) + '%'
    }

    const { step } = this.state

    return (
      <main>
        {step !== 0 &&
          <div>
            <span className="progress-step">Step {this.state.step} / 13</span>
            <progress className="progress" style={style}></progress>
          </div>
        }
        {this.showStep()}
      </main>
    )
  }
}

export default OTP
