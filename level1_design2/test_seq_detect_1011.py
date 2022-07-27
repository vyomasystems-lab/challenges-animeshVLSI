# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    print("****Corresponding output for each input****")
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    A=dut.seq_seen.value
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    B= A+dut.seq_seen.value
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    C=B+dut.seq_seen.value
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    D=C+dut.seq_seen.value
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    E=D+dut.seq_seen.value

    assert dut.seq_seen.value == 1, "Test failed with: {A}! = {1}".format(
            A=dut.sel.value)
    dut.inp_bit.value = 0

    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    F=E+dut.seq_seen.value
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    G=F+dut.seq_seen.value
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)

    assert dut.seq_seen.value == 1, "Test failed with: {A}! = {1}".format(
            A=dut.sel.value)

    H=G+dut.seq_seen.value
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    I=H+dut.seq_seen.value
 

        
    print("How many times will we gets 1 at output?")
    #out=dut.seq_seen.value
    #print(out.binstr)
    print(I)

        
    dut._log.info(f'expected_Value = {2} Design_Value = {I}')
    expected_Value=2
    Design_Value=I
    if expected_Value == Design_Value:
        print("PASS")
    else:
        print("FAIL")
