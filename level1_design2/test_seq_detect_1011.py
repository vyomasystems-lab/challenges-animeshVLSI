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
    print(dut.seq_seen.value.binstr)
    A=dut.seq_seen.value.binstr
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    B= A+dut.seq_seen.value.binstr
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    C=B+dut.seq_seen.value.binstr
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    D=C+dut.seq_seen.value.binstr
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    E=D+dut.seq_seen.value.binstr
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    F=E+dut.seq_seen.value.binstr
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    G=F+dut.seq_seen.value.binstr
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    H=G+dut.seq_seen.value.binstr
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    print(dut.seq_seen.value.binstr)
    I=H+dut.seq_seen.value.binstr
 

        
    print("How many times will we gets 1 at output")
    #out=dut.seq_seen.value
    #print(out.binstr)
    print(I)

        
    dut._log.info(f'expected_Value = {2} Design_Value = {out.binstr}')
    assert dut.seq_seen.value == 2, "test is failed with: {expected_Value}! = {Design_Value}".format(
        Design_Value=out.binstr)