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

#@cocotb.test()
#async def test_randomised_mux(dut):
    """Test for 2 random numbers multiple times for inp12 and inp13 under select line 13"""

    #for i in range(1):

        #A = random.randint(0, 1)

    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 1
    dut.inp_bit.value = 0
        
    await Timer(2, units='ns')
    #OUT=dut.seq_seen.value
    p#rint(OUT.binstr)
        
        #dut._log.info(f'A={A:01} expected_Value = {C:01} Design_Value = {int(dut.seq_seen.value):01}')
       # assert dut.seq_seen.value == C, "Randomised test failed with: {C}! = {OUT}".format(
            #A=dut.inp_bit.value, OUT=dut.out.value)