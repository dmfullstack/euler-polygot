'use strict'

//javascript has bad errors.

module.exports = {

  solve: function (x) {
    var sol = 0
    for (var i = x-1; i >= 0; i--) {
      if((i%3 == 0) || (i%5 == 0)){
        sol = sol + i;
      }
    }
    return sol;
  }
}
