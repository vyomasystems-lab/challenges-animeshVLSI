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
    H=G+dut.seq_seen.value
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value)
    I=H+dut.seq_seen.value
 

        
    print("How many times will we gets 1 at output")
    #out=dut.seq_seen.value
    #print(out.binstr)
    print(I)

        
    dut._log.info(f'expected_Value = {2} Design_Value = {I}')
    assert dut.seq_seen.value == expected_Value, "test is failed with: {expected_Value}! = {Design_Value}".format(
        Design_Value = int(I), expected_Value =2)