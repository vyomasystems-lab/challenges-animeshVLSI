# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random


@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    A = 12
    B =  2
    C =  3

    # input driving
    dut.sel.value = A
    dut.inp12.value = B
    dut.inp13.value = C
    await Timer(2, units='ns')

    assert dut.out.value == B, f"Adder result is incorrect: {dut.out.value} != B"
    #cocotb.log.info('##### CTB: Develop your test here ########')
