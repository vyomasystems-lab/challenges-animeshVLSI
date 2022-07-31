# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test3(dut):
    """Test for seq detection """

    clock = Clock(dut.clock, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clock)  
    dut.reset.value = 0
    await FallingEdge(dut.clock)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    #print("****Corresponding output for each input****")
    @cocotb.test()
    async def test3_directed(dut):
   
     A = 3
     B =  140
     C =  1

    # input driving
    dut.baud_rate_select.value = 3
    dut.Byte_To_Send.value = 140
    dut.start.value = 1
    #dut.Tx_Done.value = D
  
    await Timer(2, units='ns')

    assert dut.Tx_Done.value == 1, "correct baud rate checking failed: {D} != {1}".format(
            D=int(dut.Tx_Done.value))
    
 

        
   

        
    
