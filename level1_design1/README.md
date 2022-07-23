# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![gitpod](https://user-images.githubusercontent.com/109648435/180613473-845f1e64-34b7-48c8-a9ec-341590286967.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (multiplexer module) which takes 5-bit select line (*sel*) and 31 input lines each having 2-bit and 2-bit output line called *out*. The inputs are *inp0*, *inp1*, *inp2*, *inp3*, *inp4*, *inp5*, *inp6*, *inp7*, *inp8*, *inp9*, *inp10*, *inp11*, *inp12*, *inp13*, *inp14*, *inp15*, *inp16*, *inp17*, *inp18*, *inp19*, *inp20*, *inp21*, *inp22*, *inp23*, *inp24*, *inp25*, *inp26*, *inp27*, *inp28*, *inp29*, *inp30*

Both directed test case and random test case are applied into the testbench to verify the design.

The values are assigned to the input port using 
###### Directed Test
```
A = 13
B =  2
C =  3
    
dut.sel.value = A
dut.inp12.value = B
dut.inp13.value = C
```
###### Random Test

```
A = 13
B = random.randint(0, 1)
C = random.randint(2, 3)

dut.sel.value = A
dut.inp12.value = B
dut.inp13.value = C
```
The assert statement is used for comparing the multiplexer's output to the expected value.

The following error is seen:
```
assert dut.out.value == C, "MUX result is incorrect: {C} != {OUT}, expected_value={EXP}".format(
            A=int(dut.sel.value), B=int(dut.inp12.value), C=int(dut.inp13.value) , OUT=int(dut.out.value), EXP=C)
```
## Test Scenario **(Important)**
###### Directed Test 
- Test Inputs: sel=13, inp12=2, inp13=3
- Expected Output: out=3
- Observed Output in the DUT dut.out=2

Output mismatches for the above inputs proving that there is a design bug

###### Random Test
- Test Inputs: sel=13, inp12=1, inp13=2
- Expected Output: out=2
- Observed Output in the DUT dut.out=1

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;   -------> BUG
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      default: out = 0;
    endcase
```
For the mux design, for out=inp12 the sel should be 5'b01100 instead of 5'b01101 and for out=inp13 the sel is 5'b01101 

###### Buggy mux output

![Fail](https://user-images.githubusercontent.com/109648435/180621146-e2ca54ca-b3f9-491b-aba0-8c09e6fa0822.png)


## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
