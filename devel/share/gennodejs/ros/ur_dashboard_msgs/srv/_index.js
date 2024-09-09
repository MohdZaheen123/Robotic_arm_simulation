
"use strict";

let AddToLog = require('./AddToLog.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let GetProgramState = require('./GetProgramState.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let Load = require('./Load.js')
let GetRobotMode = require('./GetRobotMode.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')
let RawRequest = require('./RawRequest.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let Popup = require('./Popup.js')

module.exports = {
  AddToLog: AddToLog,
  IsProgramRunning: IsProgramRunning,
  GetProgramState: GetProgramState,
  IsProgramSaved: IsProgramSaved,
  Load: Load,
  GetRobotMode: GetRobotMode,
  GetSafetyMode: GetSafetyMode,
  IsInRemoteControl: IsInRemoteControl,
  RawRequest: RawRequest,
  GetLoadedProgram: GetLoadedProgram,
  Popup: Popup,
};
