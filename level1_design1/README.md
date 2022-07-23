# Adder Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![gitpod](https://user-images.githubusercontent.com/109648435/180613473-845f1e64-34b7-48c8-a9ec-341590286967.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (multiplexer module here) which takes 5-bit select line (*sel*) and 31 input lines each having 2-bit and 2-bit output line called *out*. The inputs are *inp0*, *inp1*, *inp2*, *inp3*, *inp4*, *inp5*, *inp6*, *inp7*, *inp8*, *inp9*, *inp10*, *inp11*, *inp12*, *inp13*, *inp14*, *inp15*, *inp16*, *inp17*, *inp18*, *inp19*, *inp20*, *inp21*, *inp22*, *inp23*, *inp24*, *inp25*, *inp26*, *inp27*, *inp28*, *inp29*, *inp30*

The values are assigned to the input port using 
```
dut.sel.value = 12
dut.inp12.value = 2
```

The assert statement is used for comparing the multiplexer's output to the expected value.

The following error is seen:
```
assert dut.out.value == B, "MUX result is incorrect: {B} != {OUT}, expected value={EXP}".format(
            A=int(dut.sel.value), B=int(dut.inp12.value), OUT=int(dut.out.value), EXP=B)
```
## Test Scenario **(Important)**
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(a or b) 
  begin
    sum = a - b;             ====> BUG
  end
```
For the adder design, the logic should be ``a + b`` instead of ``a - b`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
