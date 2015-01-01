'use strict'

var assert = require("assert");
var should = require("should"); //npm install -g should
var Solution = require("../solution.js");

describe('Testing Suite',function () {
  describe('Array', function(){
    describe('#indexOf()', function(){
      it('should return -1 when the value is not present', function(){
        [1,2,3].indexOf(5).should.equal(-1);
        [1,2,3].indexOf(0).should.equal(-1);
      });
    });
  });

  describe("Solution" ,function () {
    it('should return the solution for 1000',function () {
      Solution.solve(1000).should.equal(233168);
    })

    it('should reqturn nothing', function () {
      Solution.solve(0).should.equal(0);
    })

    it('should return the solution for 10', function () {
      Solution.solve(10).should.equal(23);
    })

  })

});