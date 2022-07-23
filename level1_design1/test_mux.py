# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random


@cocotb.test()
async def test_directed_mux(dut):
    """Test for mux2"""
    A = 12
    B =  2
    C =  3

    # input driving
    dut.sel.value = A
    dut.inp12.value = B
    dut.inp13.value = C
    await Timer(2, units='ns')
    assert dut.out.value == dut.inp12.value, f"Adder result is incorrect: {dut.out.value} != dut.inp12.value"
    #cocotb.log.info('##### CTB: Develop your test here ########')


@cocotb.test()
async def test_randomised_mux(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(30):

        A = random.randint(0, 31)
        B = random.randint(0, 3)
        C = random.randint(0, 3)

        dut.sel.value = A
        dut.inp12.value = B
        dut.inp13.value = C
        await Timer(2, units='ns')
        
        #dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.out.value == B, "Randomised test failed with: {out} != {OUT}".format(
            A=dut.sel.value, B=dut.inp12.value, OUT=dut.out.value)
