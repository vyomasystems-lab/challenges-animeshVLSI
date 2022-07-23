# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random


@cocotb.test()
async def test_directed_mux(dut):
    """Test for mux2"""
    A = 13
    B =  2
    C =  3

    # input driving
    dut.sel.value = A
    dut.inp12.value = B
    dut.inp13.value = C
  
    await Timer(2, units='ns')
   #cocotb.log.info('##### CTB: Develop your test here ########')

    assert dut.out.value == C, "MUX result is incorrect: {C} != {OUT}, expected_value={EXP}".format(
            A=int(dut.sel.value), B=int(dut.inp12.value), C=int(dut.inp13.value) , OUT=int(dut.out.value), EXP=C)


@cocotb.test()
async def test_randomised_mux(dut):
    """Test for 2 random numbers multiple times for inp12 and inp13 under select line 13"""

    for i in range(1):

        A = 13
        B = random.randint(0, 1)
        C = random.randint(2, 3)

        dut.sel.value = A
        dut.inp12.value = B
        dut.inp13.value = C
        
        await Timer(2, units='ns')
        
        dut._log.info(f'B={B:01} C={C:01} expected_Value = {C:01} Design_Value = {int(dut.out.value):01}')
        assert dut.out.value == C, "Randomised test failed with: {C}! = {OUT}".format(
            A=dut.sel.value, B=dut.b.value, OUT=dut.out.value)