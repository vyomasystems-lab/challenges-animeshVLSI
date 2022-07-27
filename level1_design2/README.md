# FSM Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![INTRO](https://user-images.githubusercontent.com/109648435/181350774-e56c2732-2758-4de1-a2d2-eb415969504f.JPG)

The corrected state machine diagram is shown in below,

![state_diagram](https://user-images.githubusercontent.com/109648435/181353352-0a70372a-4d68-44ba-b2dd-a9f506e30ec3.jpg)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (FSM module) which takes 8 single bit input.

The values are assigned to the input port using 
###### Directed Test
```
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
```

The assert statement is used for comparing the FSM's output to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1, "Test failed with: {A}! = {1}".format(
            A=dut.seq_seen.value)
```
Also I have used one more condition for PASS and FAIL
```
if expected_Value == Design_Value:
        print("PASS")
else:
        print("FAIL")
```

## Test Scenario **(Important)**
```
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
```

Output mismatches for the above inputs proving that there is a design bug


## Design Bug
Based on the above test input and analysing the design, we see the following

```
 // BUGGY FSM
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;  ------>    //BUG
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;	----->	//BUG
      end
      SEQ_1011:					------>	// COMPLETE CASE IS BUGGY
      begin
        next_state = IDLE;
      end
    endcase
  end
endmodule
```


###### Buggy FSM output
We can observe that, in the buggy design the overlapping sequence is not working.

![bug_Wave](https://user-images.githubusercontent.com/109648435/181353070-2f03dda8-31e8-438e-a340-92dac9d6e7e0.JPG)

###### Buggy_FSM PASS/FAIL message

![fail2](https://user-images.githubusercontent.com/109648435/181354389-bbe88d20-7f85-4ed4-b8a6-113bfd4104ed.JPG)

## Design Fix
Updating the design and re-running the test makes the test pass.

```
//BUG LESS DESIGN
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output  seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;     
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_101;   
      end
      SEQ_1011:						
      begin
		if (inp_bit == 1)
		   next_state = SEQ_1;
		else
           next_state = SEQ_10;
      end
    endcase
  end
endmodule
```
###### Waveform
Corrected waveform of FSM


![fixed](https://user-images.githubusercontent.com/109648435/181354003-9bd5aa54-9378-436c-9b32-46d6f79daa26.JPG)

###### PASS/FAIL message
After correction, PASS messages are comming

![PASS](https://user-images.githubusercontent.com/109648435/181354556-8cbaacd6-faa1-4046-8f6a-d80dec75b031.JPG)



