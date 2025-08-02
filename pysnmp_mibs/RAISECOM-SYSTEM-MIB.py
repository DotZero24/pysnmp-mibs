_t='raisecomAlarmHistType'
_s='raisecomAlarmHistTimestamp'
_r='raisecomAlarmHistDescr'
_q='raisecomAlarmHistSource'
_p='raisecomProcessUtilization'
_o='raisecomAlarmCurtIndex'
_n='not-forward'
_m='link-falut'
_l='link-down'
_k='low-volt'
_j='high-volt'
_i='low-temperature'
_h='high-temperature'
_g='power-abnormal'
_f='dev-power-down'
_e='raisecomAlarmHistIndex'
_d='raisecomAlarmPortIndex'
_c='raisecomBasePort'
_b='raisecomDeadProcessIndex'
_a='raisecomProcessStatisticsPeriod'
_Z='raisecomCPUHistoryIndex'
_Y='raisecomCPUHistoryPeriod'
_X='twoHour'
_W='raisecomCPUUtilizationIndex'
_V='mandatory'
_U='raisecomVoltValue'
_T='raisecomVoltReference'
_S='raisecomTemperatureValue'
_R='raisecomCPUUtilization'
_Q='tenMin'
_P='oneMin'
_O='fiveSec'
_N='raisecomVoltIndex'
_M='raisecomProcessIndex'
_L='Celsius '
_K='OctetString'
_J='mV'
_I='deprecated'
_H='percent'
_G='not-accessible'
_F='EnableVar'
_E='Integer32'
_D='read-write'
_C='RAISECOM-SYSTEM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_F)
raisecomSystem=ModuleIdentity((1,3,6,1,4,1,8886,1,1))
raisecomCpu=ModuleIdentity((1,3,6,1,4,1,8886,1,1,1))
raisecomEndPool=ModuleIdentity((1,3,6,1,4,1,8886,1,1,2))
raisecomMemory=ModuleIdentity((1,3,6,1,4,1,8886,1,1,3))
raisecomInformation=ModuleIdentity((1,3,6,1,4,1,8886,1,1,4))
class ProcessStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ready',1),('delay',2),('delay-s',3),('pend',4),('pend-t',5),('pend-s',6),('pend-t-s',7),('suspend',8),('dead',9)))
class CPUTimeStamp(TextualConvention,OctetString):status=_A;displayHint='4d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class PortAlarmEventList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class _RaisecomCpuBusy1Per_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomCpuBusy1Per_Type.__name__=_E
_RaisecomCpuBusy1Per_Object=MibScalar
raisecomCpuBusy1Per=_RaisecomCpuBusy1Per_Object((1,3,6,1,4,1,8886,1,1,1,1),_RaisecomCpuBusy1Per_Type())
raisecomCpuBusy1Per.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCpuBusy1Per.setStatus(_V)
if mibBuilder.loadTexts:raisecomCpuBusy1Per.setUnits(_H)
class _RaisecomCpuBusy60Per_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomCpuBusy60Per_Type.__name__=_E
_RaisecomCpuBusy60Per_Object=MibScalar
raisecomCpuBusy60Per=_RaisecomCpuBusy60Per_Object((1,3,6,1,4,1,8886,1,1,1,2),_RaisecomCpuBusy60Per_Type())
raisecomCpuBusy60Per.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCpuBusy60Per.setStatus(_V)
if mibBuilder.loadTexts:raisecomCpuBusy60Per.setUnits(_H)
_RaisecomCPUTrapGroup_ObjectIdentity=ObjectIdentity
raisecomCPUTrapGroup=_RaisecomCPUTrapGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,1,1,3))
_RaisecomCPUScalarGroup_ObjectIdentity=ObjectIdentity
raisecomCPUScalarGroup=_RaisecomCPUScalarGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,1,1,4))
class _RaisecomCPUUtilizationTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomCPUUtilizationTotal_Type.__name__=_E
_RaisecomCPUUtilizationTotal_Object=MibScalar
raisecomCPUUtilizationTotal=_RaisecomCPUUtilizationTotal_Object((1,3,6,1,4,1,8886,1,1,1,4,1),_RaisecomCPUUtilizationTotal_Type())
raisecomCPUUtilizationTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCPUUtilizationTotal.setStatus(_A)
if mibBuilder.loadTexts:raisecomCPUUtilizationTotal.setUnits(_H)
class _RaisecomCPUHistoryTableSize_Type(Integer32):defaultValue=60
_RaisecomCPUHistoryTableSize_Type.__name__=_E
_RaisecomCPUHistoryTableSize_Object=MibScalar
raisecomCPUHistoryTableSize=_RaisecomCPUHistoryTableSize_Object((1,3,6,1,4,1,8886,1,1,1,4,2),_RaisecomCPUHistoryTableSize_Type())
raisecomCPUHistoryTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCPUHistoryTableSize.setStatus(_A)
_RaisecomCPUThresholdTrapEnable_Type=EnableVar
_RaisecomCPUThresholdTrapEnable_Object=MibScalar
raisecomCPUThresholdTrapEnable=_RaisecomCPUThresholdTrapEnable_Object((1,3,6,1,4,1,8886,1,1,1,4,3),_RaisecomCPUThresholdTrapEnable_Type())
raisecomCPUThresholdTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomCPUThresholdTrapEnable.setStatus(_A)
class _RaisecomCPURisingThresholdValue_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomCPURisingThresholdValue_Type.__name__=_E
_RaisecomCPURisingThresholdValue_Object=MibScalar
raisecomCPURisingThresholdValue=_RaisecomCPURisingThresholdValue_Object((1,3,6,1,4,1,8886,1,1,1,4,4),_RaisecomCPURisingThresholdValue_Type())
raisecomCPURisingThresholdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomCPURisingThresholdValue.setStatus(_A)
class _RaisecomCPUFallingThresholdValue_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomCPUFallingThresholdValue_Type.__name__=_E
_RaisecomCPUFallingThresholdValue_Object=MibScalar
raisecomCPUFallingThresholdValue=_RaisecomCPUFallingThresholdValue_Object((1,3,6,1,4,1,8886,1,1,1,4,5),_RaisecomCPUFallingThresholdValue_Type())
raisecomCPUFallingThresholdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomCPUFallingThresholdValue.setStatus(_A)
class _RaisecomCPUThresholdInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,36000))
_RaisecomCPUThresholdInterval_Type.__name__=_E
_RaisecomCPUThresholdInterval_Object=MibScalar
raisecomCPUThresholdInterval=_RaisecomCPUThresholdInterval_Object((1,3,6,1,4,1,8886,1,1,1,4,6),_RaisecomCPUThresholdInterval_Type())
raisecomCPUThresholdInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomCPUThresholdInterval.setStatus(_A)
class _RaisecomCpuTotalProcNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_RaisecomCpuTotalProcNum_Type.__name__=_E
_RaisecomCpuTotalProcNum_Object=MibScalar
raisecomCpuTotalProcNum=_RaisecomCpuTotalProcNum_Object((1,3,6,1,4,1,8886,1,1,1,4,7),_RaisecomCpuTotalProcNum_Type())
raisecomCpuTotalProcNum.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCpuTotalProcNum.setStatus(_A)
class _RaisecomCPUTrapUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomCPUTrapUtilization_Type.__name__=_E
_RaisecomCPUTrapUtilization_Object=MibScalar
raisecomCPUTrapUtilization=_RaisecomCPUTrapUtilization_Object((1,3,6,1,4,1,8886,1,1,1,4,8),_RaisecomCPUTrapUtilization_Type())
raisecomCPUTrapUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCPUTrapUtilization.setStatus(_A)
if mibBuilder.loadTexts:raisecomCPUTrapUtilization.setUnits(_H)
_RaisecomCPUTableGroup_ObjectIdentity=ObjectIdentity
raisecomCPUTableGroup=_RaisecomCPUTableGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,1,1,5))
_RaisecomCPUUtilizationGroup_ObjectIdentity=ObjectIdentity
raisecomCPUUtilizationGroup=_RaisecomCPUUtilizationGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,1,1,5,1))
_RaisecomCPUUtilizationTable_Object=MibTable
raisecomCPUUtilizationTable=_RaisecomCPUUtilizationTable_Object((1,3,6,1,4,1,8886,1,1,1,5,1,1))
if mibBuilder.loadTexts:raisecomCPUUtilizationTable.setStatus(_A)
_RaisecomCPUUtilizationEntry_Object=MibTableRow
raisecomCPUUtilizationEntry=_RaisecomCPUUtilizationEntry_Object((1,3,6,1,4,1,8886,1,1,1,5,1,1,1))
raisecomCPUUtilizationEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:raisecomCPUUtilizationEntry.setStatus(_A)
_RaisecomCPUUtilizationIndex_Type=Integer32
_RaisecomCPUUtilizationIndex_Object=MibTableColumn
raisecomCPUUtilizationIndex=_RaisecomCPUUtilizationIndex_Object((1,3,6,1,4,1,8886,1,1,1,5,1,1,1,1),_RaisecomCPUUtilizationIndex_Type())
raisecomCPUUtilizationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomCPUUtilizationIndex.setStatus(_A)
class _RaisecomCPUUtilizationPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('oneSec',1),(_O,2),(_P,3),(_Q,4),(_X,5)))
_RaisecomCPUUtilizationPeriod_Type.__name__=_E
_RaisecomCPUUtilizationPeriod_Object=MibTableColumn
raisecomCPUUtilizationPeriod=_RaisecomCPUUtilizationPeriod_Object((1,3,6,1,4,1,8886,1,1,1,5,1,1,1,2),_RaisecomCPUUtilizationPeriod_Type())
raisecomCPUUtilizationPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCPUUtilizationPeriod.setStatus(_A)
class _RaisecomCPUUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomCPUUtilization_Type.__name__=_E
_RaisecomCPUUtilization_Object=MibTableColumn
raisecomCPUUtilization=_RaisecomCPUUtilization_Object((1,3,6,1,4,1,8886,1,1,1,5,1,1,1,3),_RaisecomCPUUtilization_Type())
raisecomCPUUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCPUUtilization.setStatus(_A)
if mibBuilder.loadTexts:raisecomCPUUtilization.setUnits(_H)
_RaisecomCPUHistoryTable_Object=MibTable
raisecomCPUHistoryTable=_RaisecomCPUHistoryTable_Object((1,3,6,1,4,1,8886,1,1,1,5,1,2))
if mibBuilder.loadTexts:raisecomCPUHistoryTable.setStatus(_A)
_RaisecomCPUHistoryEntry_Object=MibTableRow
raisecomCPUHistoryEntry=_RaisecomCPUHistoryEntry_Object((1,3,6,1,4,1,8886,1,1,1,5,1,2,1))
raisecomCPUHistoryEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:raisecomCPUHistoryEntry.setStatus(_A)
class _RaisecomCPUHistoryPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_X,4)))
_RaisecomCPUHistoryPeriod_Type.__name__=_E
_RaisecomCPUHistoryPeriod_Object=MibTableColumn
raisecomCPUHistoryPeriod=_RaisecomCPUHistoryPeriod_Object((1,3,6,1,4,1,8886,1,1,1,5,1,2,1,1),_RaisecomCPUHistoryPeriod_Type())
raisecomCPUHistoryPeriod.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomCPUHistoryPeriod.setStatus(_A)
_RaisecomCPUHistoryIndex_Type=Integer32
_RaisecomCPUHistoryIndex_Object=MibTableColumn
raisecomCPUHistoryIndex=_RaisecomCPUHistoryIndex_Object((1,3,6,1,4,1,8886,1,1,1,5,1,2,1,2),_RaisecomCPUHistoryIndex_Type())
raisecomCPUHistoryIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomCPUHistoryIndex.setStatus(_A)
class _RaisecomCPUHistoryTotalUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomCPUHistoryTotalUtil_Type.__name__=_E
_RaisecomCPUHistoryTotalUtil_Object=MibTableColumn
raisecomCPUHistoryTotalUtil=_RaisecomCPUHistoryTotalUtil_Object((1,3,6,1,4,1,8886,1,1,1,5,1,2,1,3),_RaisecomCPUHistoryTotalUtil_Type())
raisecomCPUHistoryTotalUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomCPUHistoryTotalUtil.setStatus(_A)
if mibBuilder.loadTexts:raisecomCPUHistoryTotalUtil.setUnits(_H)
_RaisecomCPUProcessesGroup_ObjectIdentity=ObjectIdentity
raisecomCPUProcessesGroup=_RaisecomCPUProcessesGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,1,1,5,2))
_RaisecomProcessesTable_Object=MibTable
raisecomProcessesTable=_RaisecomProcessesTable_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1))
if mibBuilder.loadTexts:raisecomProcessesTable.setStatus(_A)
_RaisecomProcessesEntry_Object=MibTableRow
raisecomProcessesEntry=_RaisecomProcessesEntry_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1))
raisecomProcessesEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:raisecomProcessesEntry.setStatus(_A)
_RaisecomProcessIndex_Type=Integer32
_RaisecomProcessIndex_Object=MibTableColumn
raisecomProcessIndex=_RaisecomProcessIndex_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,1),_RaisecomProcessIndex_Type())
raisecomProcessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessIndex.setStatus(_A)
_RaisecomProcessPID_Type=Integer32
_RaisecomProcessPID_Object=MibTableColumn
raisecomProcessPID=_RaisecomProcessPID_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,2),_RaisecomProcessPID_Type())
raisecomProcessPID.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessPID.setStatus(_A)
class _RaisecomProcessName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomProcessName_Type.__name__=_K
_RaisecomProcessName_Object=MibTableColumn
raisecomProcessName=_RaisecomProcessName_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,3),_RaisecomProcessName_Type())
raisecomProcessName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessName.setStatus(_A)
_RaisecomProcessRunTimeTotal_Type=CPUTimeStamp
_RaisecomProcessRunTimeTotal_Object=MibTableColumn
raisecomProcessRunTimeTotal=_RaisecomProcessRunTimeTotal_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,4),_RaisecomProcessRunTimeTotal_Type())
raisecomProcessRunTimeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessRunTimeTotal.setStatus(_A)
_RaisecomProcessInvokedTotal_Type=Integer32
_RaisecomProcessInvokedTotal_Object=MibTableColumn
raisecomProcessInvokedTotal=_RaisecomProcessInvokedTotal_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,5),_RaisecomProcessInvokedTotal_Type())
raisecomProcessInvokedTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessInvokedTotal.setStatus(_A)
_RaisecomProcessTimeCreated_Type=TimeStamp
_RaisecomProcessTimeCreated_Object=MibTableColumn
raisecomProcessTimeCreated=_RaisecomProcessTimeCreated_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,6),_RaisecomProcessTimeCreated_Type())
raisecomProcessTimeCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessTimeCreated.setStatus(_A)
_RaisecomProcessNormalPriority_Type=Integer32
_RaisecomProcessNormalPriority_Object=MibTableColumn
raisecomProcessNormalPriority=_RaisecomProcessNormalPriority_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,7),_RaisecomProcessNormalPriority_Type())
raisecomProcessNormalPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessNormalPriority.setStatus(_A)
_RaisecomProcessCurrentPriority_Type=Integer32
_RaisecomProcessCurrentPriority_Object=MibTableColumn
raisecomProcessCurrentPriority=_RaisecomProcessCurrentPriority_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,8),_RaisecomProcessCurrentPriority_Type())
raisecomProcessCurrentPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessCurrentPriority.setStatus(_A)
_RaisecomProcessStatus_Type=ProcessStatus
_RaisecomProcessStatus_Object=MibTableColumn
raisecomProcessStatus=_RaisecomProcessStatus_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,9),_RaisecomProcessStatus_Type())
raisecomProcessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessStatus.setStatus(_A)
_RaisecomProcessErrorNo_Type=Integer32
_RaisecomProcessErrorNo_Object=MibTableColumn
raisecomProcessErrorNo=_RaisecomProcessErrorNo_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,10),_RaisecomProcessErrorNo_Type())
raisecomProcessErrorNo.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessErrorNo.setStatus(_A)
_RaisecomProcessStackSize_Type=Integer32
_RaisecomProcessStackSize_Object=MibTableColumn
raisecomProcessStackSize=_RaisecomProcessStackSize_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,11),_RaisecomProcessStackSize_Type())
raisecomProcessStackSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessStackSize.setStatus(_A)
_RaisecomProcessStackCurrentSize_Type=Integer32
_RaisecomProcessStackCurrentSize_Object=MibTableColumn
raisecomProcessStackCurrentSize=_RaisecomProcessStackCurrentSize_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,12),_RaisecomProcessStackCurrentSize_Type())
raisecomProcessStackCurrentSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessStackCurrentSize.setStatus(_A)
_RaisecomProcessStackMaxSize_Type=Integer32
_RaisecomProcessStackMaxSize_Object=MibTableColumn
raisecomProcessStackMaxSize=_RaisecomProcessStackMaxSize_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,13),_RaisecomProcessStackMaxSize_Type())
raisecomProcessStackMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessStackMaxSize.setStatus(_A)
_RaisecomProcessStackBegin_Type=Integer32
_RaisecomProcessStackBegin_Object=MibTableColumn
raisecomProcessStackBegin=_RaisecomProcessStackBegin_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,14),_RaisecomProcessStackBegin_Type())
raisecomProcessStackBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessStackBegin.setStatus(_A)
_RaisecomProcessStackPointer_Type=Integer32
_RaisecomProcessStackPointer_Object=MibTableColumn
raisecomProcessStackPointer=_RaisecomProcessStackPointer_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,15),_RaisecomProcessStackPointer_Type())
raisecomProcessStackPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessStackPointer.setStatus(_A)
_RaisecomProcessStackEnd_Type=Integer32
_RaisecomProcessStackEnd_Object=MibTableColumn
raisecomProcessStackEnd=_RaisecomProcessStackEnd_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,16),_RaisecomProcessStackEnd_Type())
raisecomProcessStackEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessStackEnd.setStatus(_A)
_RaisecomProcessProgramCounter_Type=Integer32
_RaisecomProcessProgramCounter_Object=MibTableColumn
raisecomProcessProgramCounter=_RaisecomProcessProgramCounter_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,17),_RaisecomProcessProgramCounter_Type())
raisecomProcessProgramCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessProgramCounter.setStatus(_A)
_RaisecomProcessEntry_Type=Integer32
_RaisecomProcessEntry_Object=MibTableColumn
raisecomProcessEntry=_RaisecomProcessEntry_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,18),_RaisecomProcessEntry_Type())
raisecomProcessEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessEntry.setStatus(_A)
_RaisecomProcessSemWait_Type=Integer32
_RaisecomProcessSemWait_Object=MibTableColumn
raisecomProcessSemWait=_RaisecomProcessSemWait_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,19),_RaisecomProcessSemWait_Type())
raisecomProcessSemWait.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessSemWait.setStatus(_A)
_RaisecomProcessDelay_Type=Integer32
_RaisecomProcessDelay_Object=MibTableColumn
raisecomProcessDelay=_RaisecomProcessDelay_Object((1,3,6,1,4,1,8886,1,1,1,5,2,1,1,20),_RaisecomProcessDelay_Type())
raisecomProcessDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessDelay.setStatus(_A)
_RaisecomProcessStatisticsTable_Object=MibTable
raisecomProcessStatisticsTable=_RaisecomProcessStatisticsTable_Object((1,3,6,1,4,1,8886,1,1,1,5,2,2))
if mibBuilder.loadTexts:raisecomProcessStatisticsTable.setStatus(_A)
_RaisecomProcessStatisticsEntry_Object=MibTableRow
raisecomProcessStatisticsEntry=_RaisecomProcessStatisticsEntry_Object((1,3,6,1,4,1,8886,1,1,1,5,2,2,1))
raisecomProcessStatisticsEntry.setIndexNames((0,_C,_M),(0,_C,_a))
if mibBuilder.loadTexts:raisecomProcessStatisticsEntry.setStatus(_A)
class _RaisecomProcessStatisticsPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3)))
_RaisecomProcessStatisticsPeriod_Type.__name__=_E
_RaisecomProcessStatisticsPeriod_Object=MibTableColumn
raisecomProcessStatisticsPeriod=_RaisecomProcessStatisticsPeriod_Object((1,3,6,1,4,1,8886,1,1,1,5,2,2,1,1),_RaisecomProcessStatisticsPeriod_Type())
raisecomProcessStatisticsPeriod.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomProcessStatisticsPeriod.setStatus(_A)
_RaisecomProcessRunTime_Type=CPUTimeStamp
_RaisecomProcessRunTime_Object=MibTableColumn
raisecomProcessRunTime=_RaisecomProcessRunTime_Object((1,3,6,1,4,1,8886,1,1,1,5,2,2,1,2),_RaisecomProcessRunTime_Type())
raisecomProcessRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessRunTime.setStatus(_A)
_RaisecomProcessInvoked_Type=Integer32
_RaisecomProcessInvoked_Object=MibTableColumn
raisecomProcessInvoked=_RaisecomProcessInvoked_Object((1,3,6,1,4,1,8886,1,1,1,5,2,2,1,3),_RaisecomProcessInvoked_Type())
raisecomProcessInvoked.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessInvoked.setStatus(_A)
class _RaisecomProcessUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomProcessUtilization_Type.__name__=_E
_RaisecomProcessUtilization_Object=MibTableColumn
raisecomProcessUtilization=_RaisecomProcessUtilization_Object((1,3,6,1,4,1,8886,1,1,1,5,2,2,1,4),_RaisecomProcessUtilization_Type())
raisecomProcessUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomProcessUtilization.setStatus(_A)
if mibBuilder.loadTexts:raisecomProcessUtilization.setUnits(_H)
_RaisecomDeadProcessesTable_Object=MibTable
raisecomDeadProcessesTable=_RaisecomDeadProcessesTable_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3))
if mibBuilder.loadTexts:raisecomDeadProcessesTable.setStatus(_A)
_RaisecomDeadProcessesEntry_Object=MibTableRow
raisecomDeadProcessesEntry=_RaisecomDeadProcessesEntry_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1))
raisecomDeadProcessesEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:raisecomDeadProcessesEntry.setStatus(_A)
_RaisecomDeadProcessIndex_Type=Integer32
_RaisecomDeadProcessIndex_Object=MibTableColumn
raisecomDeadProcessIndex=_RaisecomDeadProcessIndex_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,1),_RaisecomDeadProcessIndex_Type())
raisecomDeadProcessIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomDeadProcessIndex.setStatus(_A)
class _RaisecomDeadProcessName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomDeadProcessName_Type.__name__=_K
_RaisecomDeadProcessName_Object=MibTableColumn
raisecomDeadProcessName=_RaisecomDeadProcessName_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,2),_RaisecomDeadProcessName_Type())
raisecomDeadProcessName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessName.setStatus(_A)
_RaisecomDeadProcessEntry_Type=Integer32
_RaisecomDeadProcessEntry_Object=MibTableColumn
raisecomDeadProcessEntry=_RaisecomDeadProcessEntry_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,3),_RaisecomDeadProcessEntry_Type())
raisecomDeadProcessEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessEntry.setStatus(_A)
_RaisecomDeadProcessErrorNo_Type=Integer32
_RaisecomDeadProcessErrorNo_Object=MibTableColumn
raisecomDeadProcessErrorNo=_RaisecomDeadProcessErrorNo_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,4),_RaisecomDeadProcessErrorNo_Type())
raisecomDeadProcessErrorNo.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessErrorNo.setStatus(_A)
_RaisecomDeadProcessPriority_Type=Integer32
_RaisecomDeadProcessPriority_Object=MibTableColumn
raisecomDeadProcessPriority=_RaisecomDeadProcessPriority_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,5),_RaisecomDeadProcessPriority_Type())
raisecomDeadProcessPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessPriority.setStatus(_A)
_RaisecomDeadProcessMaxStackSize_Type=Integer32
_RaisecomDeadProcessMaxStackSize_Object=MibTableColumn
raisecomDeadProcessMaxStackSize=_RaisecomDeadProcessMaxStackSize_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,6),_RaisecomDeadProcessMaxStackSize_Type())
raisecomDeadProcessMaxStackSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessMaxStackSize.setStatus(_A)
_RaisecomDeadProcessTimeDelete_Type=TimeStamp
_RaisecomDeadProcessTimeDelete_Object=MibTableColumn
raisecomDeadProcessTimeDelete=_RaisecomDeadProcessTimeDelete_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,7),_RaisecomDeadProcessTimeDelete_Type())
raisecomDeadProcessTimeDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessTimeDelete.setStatus(_A)
_RaisecomDeadProcessDeadTimes_Type=Integer32
_RaisecomDeadProcessDeadTimes_Object=MibTableColumn
raisecomDeadProcessDeadTimes=_RaisecomDeadProcessDeadTimes_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,8),_RaisecomDeadProcessDeadTimes_Type())
raisecomDeadProcessDeadTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessDeadTimes.setStatus(_A)
_RaisecomDeadProcessStatus_Type=ProcessStatus
_RaisecomDeadProcessStatus_Object=MibTableColumn
raisecomDeadProcessStatus=_RaisecomDeadProcessStatus_Object((1,3,6,1,4,1,8886,1,1,1,5,2,3,1,9),_RaisecomDeadProcessStatus_Type())
raisecomDeadProcessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeadProcessStatus.setStatus(_A)
_RaisecomEndPoolTable_Object=MibTable
raisecomEndPoolTable=_RaisecomEndPoolTable_Object((1,3,6,1,4,1,8886,1,1,2,1))
if mibBuilder.loadTexts:raisecomEndPoolTable.setStatus(_A)
_RaisecomEndPoolEntry_Object=MibTableRow
raisecomEndPoolEntry=_RaisecomEndPoolEntry_Object((1,3,6,1,4,1,8886,1,1,2,1,1))
raisecomEndPoolEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:raisecomEndPoolEntry.setStatus(_A)
_RaisecomBasePort_Type=Integer32
_RaisecomBasePort_Object=MibTableColumn
raisecomBasePort=_RaisecomBasePort_Object((1,3,6,1,4,1,8886,1,1,2,1,1,1),_RaisecomBasePort_Type())
raisecomBasePort.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomBasePort.setStatus(_A)
_RaisecomTotalEndPool_Type=Integer32
_RaisecomTotalEndPool_Object=MibTableColumn
raisecomTotalEndPool=_RaisecomTotalEndPool_Object((1,3,6,1,4,1,8886,1,1,2,1,1,2),_RaisecomTotalEndPool_Type())
raisecomTotalEndPool.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTotalEndPool.setStatus(_A)
_RaisecomFreeEndPool_Type=Integer32
_RaisecomFreeEndPool_Object=MibTableColumn
raisecomFreeEndPool=_RaisecomFreeEndPool_Object((1,3,6,1,4,1,8886,1,1,2,1,1,3),_RaisecomFreeEndPool_Type())
raisecomFreeEndPool.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomFreeEndPool.setStatus(_A)
_RaisecomTotalMemory_Type=Integer32
_RaisecomTotalMemory_Object=MibScalar
raisecomTotalMemory=_RaisecomTotalMemory_Object((1,3,6,1,4,1,8886,1,1,3,1),_RaisecomTotalMemory_Type())
raisecomTotalMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTotalMemory.setStatus(_A)
if mibBuilder.loadTexts:raisecomTotalMemory.setUnits('Byte')
_RaisecomAvailableMemory_Type=Integer32
_RaisecomAvailableMemory_Object=MibScalar
raisecomAvailableMemory=_RaisecomAvailableMemory_Object((1,3,6,1,4,1,8886,1,1,3,2),_RaisecomAvailableMemory_Type())
raisecomAvailableMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAvailableMemory.setStatus(_A)
if mibBuilder.loadTexts:raisecomAvailableMemory.setUnits('Byte')
_RaisecomMaxUtilmemory_Type=Integer32
_RaisecomMaxUtilmemory_Object=MibScalar
raisecomMaxUtilmemory=_RaisecomMaxUtilmemory_Object((1,3,6,1,4,1,8886,1,1,3,3),_RaisecomMaxUtilmemory_Type())
raisecomMaxUtilmemory.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMaxUtilmemory.setStatus(_A)
if mibBuilder.loadTexts:raisecomMaxUtilmemory.setUnits(_H)
_RaisecomDeviceType_Type=OctetString
_RaisecomDeviceType_Object=MibScalar
raisecomDeviceType=_RaisecomDeviceType_Object((1,3,6,1,4,1,8886,1,1,4,1),_RaisecomDeviceType_Type())
raisecomDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDeviceType.setStatus(_A)
_RaisecomTemperature_ObjectIdentity=ObjectIdentity
raisecomTemperature=_RaisecomTemperature_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,2))
_RaisecomTemperatureValue_Type=Integer32
_RaisecomTemperatureValue_Object=MibScalar
raisecomTemperatureValue=_RaisecomTemperatureValue_Object((1,3,6,1,4,1,8886,1,1,4,2,1),_RaisecomTemperatureValue_Type())
raisecomTemperatureValue.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTemperatureValue.setStatus(_A)
if mibBuilder.loadTexts:raisecomTemperatureValue.setUnits(_L)
_RaisecomTemperatureMin_Type=Integer32
_RaisecomTemperatureMin_Object=MibScalar
raisecomTemperatureMin=_RaisecomTemperatureMin_Object((1,3,6,1,4,1,8886,1,1,4,2,2),_RaisecomTemperatureMin_Type())
raisecomTemperatureMin.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTemperatureMin.setStatus(_A)
if mibBuilder.loadTexts:raisecomTemperatureMin.setUnits(_L)
_RaisecomTemperatureMax_Type=Integer32
_RaisecomTemperatureMax_Object=MibScalar
raisecomTemperatureMax=_RaisecomTemperatureMax_Object((1,3,6,1,4,1,8886,1,1,4,2,3),_RaisecomTemperatureMax_Type())
raisecomTemperatureMax.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTemperatureMax.setStatus(_A)
if mibBuilder.loadTexts:raisecomTemperatureMax.setUnits(_L)
_RaisecomTemperatureTrapEnable_Type=EnableVar
_RaisecomTemperatureTrapEnable_Object=MibScalar
raisecomTemperatureTrapEnable=_RaisecomTemperatureTrapEnable_Object((1,3,6,1,4,1,8886,1,1,4,2,4),_RaisecomTemperatureTrapEnable_Type())
raisecomTemperatureTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomTemperatureTrapEnable.setStatus(_I)
_RaisecomTemperatureThresholdLow_Type=Integer32
_RaisecomTemperatureThresholdLow_Object=MibScalar
raisecomTemperatureThresholdLow=_RaisecomTemperatureThresholdLow_Object((1,3,6,1,4,1,8886,1,1,4,2,5),_RaisecomTemperatureThresholdLow_Type())
raisecomTemperatureThresholdLow.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomTemperatureThresholdLow.setStatus(_A)
if mibBuilder.loadTexts:raisecomTemperatureThresholdLow.setUnits(_L)
_RaisecomTemperatureThresholdHigh_Type=Integer32
_RaisecomTemperatureThresholdHigh_Object=MibScalar
raisecomTemperatureThresholdHigh=_RaisecomTemperatureThresholdHigh_Object((1,3,6,1,4,1,8886,1,1,4,2,6),_RaisecomTemperatureThresholdHigh_Type())
raisecomTemperatureThresholdHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomTemperatureThresholdHigh.setStatus(_A)
if mibBuilder.loadTexts:raisecomTemperatureThresholdHigh.setUnits(_L)
_RaisecomTemperatureTrapTimes_Type=Integer32
_RaisecomTemperatureTrapTimes_Object=MibScalar
raisecomTemperatureTrapTimes=_RaisecomTemperatureTrapTimes_Object((1,3,6,1,4,1,8886,1,1,4,2,7),_RaisecomTemperatureTrapTimes_Type())
raisecomTemperatureTrapTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTemperatureTrapTimes.setStatus(_A)
_RaisecomTemperatureHighTimes_Type=Integer32
_RaisecomTemperatureHighTimes_Object=MibScalar
raisecomTemperatureHighTimes=_RaisecomTemperatureHighTimes_Object((1,3,6,1,4,1,8886,1,1,4,2,8),_RaisecomTemperatureHighTimes_Type())
raisecomTemperatureHighTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTemperatureHighTimes.setStatus(_A)
_RaisecomTemperatureLowTimes_Type=Integer32
_RaisecomTemperatureLowTimes_Object=MibScalar
raisecomTemperatureLowTimes=_RaisecomTemperatureLowTimes_Object((1,3,6,1,4,1,8886,1,1,4,2,9),_RaisecomTemperatureLowTimes_Type())
raisecomTemperatureLowTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomTemperatureLowTimes.setStatus(_A)
_RaisecomVolt_ObjectIdentity=ObjectIdentity
raisecomVolt=_RaisecomVolt_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,3))
_RaisecomVoltTable_Object=MibTable
raisecomVoltTable=_RaisecomVoltTable_Object((1,3,6,1,4,1,8886,1,1,4,3,1))
if mibBuilder.loadTexts:raisecomVoltTable.setStatus(_A)
_RaisecomVoltEntry_Object=MibTableRow
raisecomVoltEntry=_RaisecomVoltEntry_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1))
raisecomVoltEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:raisecomVoltEntry.setStatus(_A)
_RaisecomVoltIndex_Type=Integer32
_RaisecomVoltIndex_Object=MibTableColumn
raisecomVoltIndex=_RaisecomVoltIndex_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,1),_RaisecomVoltIndex_Type())
raisecomVoltIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomVoltIndex.setStatus(_A)
_RaisecomVoltReference_Type=Integer32
_RaisecomVoltReference_Object=MibTableColumn
raisecomVoltReference=_RaisecomVoltReference_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,2),_RaisecomVoltReference_Type())
raisecomVoltReference.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVoltReference.setStatus(_A)
if mibBuilder.loadTexts:raisecomVoltReference.setUnits(_J)
_RaisecomVoltValue_Type=Integer32
_RaisecomVoltValue_Object=MibTableColumn
raisecomVoltValue=_RaisecomVoltValue_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,3),_RaisecomVoltValue_Type())
raisecomVoltValue.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVoltValue.setStatus(_A)
if mibBuilder.loadTexts:raisecomVoltValue.setUnits(_J)
_RaisecomVoltMin_Type=Integer32
_RaisecomVoltMin_Object=MibTableColumn
raisecomVoltMin=_RaisecomVoltMin_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,4),_RaisecomVoltMin_Type())
raisecomVoltMin.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVoltMin.setStatus(_A)
if mibBuilder.loadTexts:raisecomVoltMin.setUnits(_J)
_RaisecomVoltMax_Type=Integer32
_RaisecomVoltMax_Object=MibTableColumn
raisecomVoltMax=_RaisecomVoltMax_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,5),_RaisecomVoltMax_Type())
raisecomVoltMax.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVoltMax.setStatus(_A)
if mibBuilder.loadTexts:raisecomVoltMax.setUnits(_J)
_RaisecomVoltTrapEnable_Type=EnableVar
_RaisecomVoltTrapEnable_Object=MibTableColumn
raisecomVoltTrapEnable=_RaisecomVoltTrapEnable_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,6),_RaisecomVoltTrapEnable_Type())
raisecomVoltTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomVoltTrapEnable.setStatus(_I)
_RaisecomVoltThresholdLow_Type=Integer32
_RaisecomVoltThresholdLow_Object=MibTableColumn
raisecomVoltThresholdLow=_RaisecomVoltThresholdLow_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,7),_RaisecomVoltThresholdLow_Type())
raisecomVoltThresholdLow.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomVoltThresholdLow.setStatus(_A)
if mibBuilder.loadTexts:raisecomVoltThresholdLow.setUnits(_J)
_RaisecomVoltThresholdHigh_Type=Integer32
_RaisecomVoltThresholdHigh_Object=MibTableColumn
raisecomVoltThresholdHigh=_RaisecomVoltThresholdHigh_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,8),_RaisecomVoltThresholdHigh_Type())
raisecomVoltThresholdHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomVoltThresholdHigh.setStatus(_A)
if mibBuilder.loadTexts:raisecomVoltThresholdHigh.setUnits(_J)
_RaisecomVoltTrapTimes_Type=Integer32
_RaisecomVoltTrapTimes_Object=MibTableColumn
raisecomVoltTrapTimes=_RaisecomVoltTrapTimes_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,9),_RaisecomVoltTrapTimes_Type())
raisecomVoltTrapTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVoltTrapTimes.setStatus(_A)
_RaisecomVoltHighTimes_Type=Integer32
_RaisecomVoltHighTimes_Object=MibTableColumn
raisecomVoltHighTimes=_RaisecomVoltHighTimes_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,10),_RaisecomVoltHighTimes_Type())
raisecomVoltHighTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVoltHighTimes.setStatus(_A)
_RaisecomVoltLowTimes_Type=Integer32
_RaisecomVoltLowTimes_Object=MibTableColumn
raisecomVoltLowTimes=_RaisecomVoltLowTimes_Object((1,3,6,1,4,1,8886,1,1,4,3,1,1,11),_RaisecomVoltLowTimes_Type())
raisecomVoltLowTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVoltLowTimes.setStatus(_A)
_RaisecomInformationTrap_ObjectIdentity=ObjectIdentity
raisecomInformationTrap=_RaisecomInformationTrap_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,4))
_RaisecomAlarm_ObjectIdentity=ObjectIdentity
raisecomAlarm=_RaisecomAlarm_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5))
_RaisecomAlarmTrap_ObjectIdentity=ObjectIdentity
raisecomAlarmTrap=_RaisecomAlarmTrap_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,1))
_RaisecomAlarmGlobal_ObjectIdentity=ObjectIdentity
raisecomAlarmGlobal=_RaisecomAlarmGlobal_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,2))
class _RaisecomAlarmTrapEnable_Type(EnableVar):defaultValue=2
_RaisecomAlarmTrapEnable_Type.__name__=_F
_RaisecomAlarmTrapEnable_Object=MibScalar
raisecomAlarmTrapEnable=_RaisecomAlarmTrapEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,2,1),_RaisecomAlarmTrapEnable_Type())
raisecomAlarmTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmTrapEnable.setStatus(_A)
class _RaisecomAlarmSyslogEnable_Type(EnableVar):defaultValue=2
_RaisecomAlarmSyslogEnable_Type.__name__=_F
_RaisecomAlarmSyslogEnable_Object=MibScalar
raisecomAlarmSyslogEnable=_RaisecomAlarmSyslogEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,2,2),_RaisecomAlarmSyslogEnable_Type())
raisecomAlarmSyslogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmSyslogEnable.setStatus(_A)
_RaisecomAlarmClear_Type=TruthValue
_RaisecomAlarmClear_Object=MibScalar
raisecomAlarmClear=_RaisecomAlarmClear_Object((1,3,6,1,4,1,8886,1,1,4,5,2,3),_RaisecomAlarmClear_Type())
raisecomAlarmClear.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmClear.setStatus(_A)
_RaisecomAlarmHwmonitorPeriod_Type=Integer32
_RaisecomAlarmHwmonitorPeriod_Object=MibScalar
raisecomAlarmHwmonitorPeriod=_RaisecomAlarmHwmonitorPeriod_Object((1,3,6,1,4,1,8886,1,1,4,5,2,4),_RaisecomAlarmHwmonitorPeriod_Type())
raisecomAlarmHwmonitorPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmHwmonitorPeriod.setStatus(_A)
_RaisecomAlarmPower_ObjectIdentity=ObjectIdentity
raisecomAlarmPower=_RaisecomAlarmPower_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,3))
class _RaisecomAlarmPowerTrapEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmPowerTrapEnable_Type.__name__=_F
_RaisecomAlarmPowerTrapEnable_Object=MibScalar
raisecomAlarmPowerTrapEnable=_RaisecomAlarmPowerTrapEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,3,1),_RaisecomAlarmPowerTrapEnable_Type())
raisecomAlarmPowerTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmPowerTrapEnable.setStatus(_A)
class _RaisecomAlarmPowerRelayEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmPowerRelayEnable_Type.__name__=_F
_RaisecomAlarmPowerRelayEnable_Object=MibScalar
raisecomAlarmPowerRelayEnable=_RaisecomAlarmPowerRelayEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,3,2),_RaisecomAlarmPowerRelayEnable_Type())
raisecomAlarmPowerRelayEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmPowerRelayEnable.setStatus(_A)
class _RaisecomAlarmPowerSyslogEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmPowerSyslogEnable_Type.__name__=_F
_RaisecomAlarmPowerSyslogEnable_Object=MibScalar
raisecomAlarmPowerSyslogEnable=_RaisecomAlarmPowerSyslogEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,3,3),_RaisecomAlarmPowerSyslogEnable_Type())
raisecomAlarmPowerSyslogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmPowerSyslogEnable.setStatus(_A)
_RaisecomAlarmPowerOneTimes_Type=Integer32
_RaisecomAlarmPowerOneTimes_Object=MibScalar
raisecomAlarmPowerOneTimes=_RaisecomAlarmPowerOneTimes_Object((1,3,6,1,4,1,8886,1,1,4,5,3,4),_RaisecomAlarmPowerOneTimes_Type())
raisecomAlarmPowerOneTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmPowerOneTimes.setStatus(_A)
_RaisecomAlarmPowerTwoTimes_Type=Integer32
_RaisecomAlarmPowerTwoTimes_Object=MibScalar
raisecomAlarmPowerTwoTimes=_RaisecomAlarmPowerTwoTimes_Object((1,3,6,1,4,1,8886,1,1,4,5,3,5),_RaisecomAlarmPowerTwoTimes_Type())
raisecomAlarmPowerTwoTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmPowerTwoTimes.setStatus(_A)
class _RaisecomAlarmPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dual-power-on',1),('dual-power-off',2),('power1-off',3),('power2-off',4)))
_RaisecomAlarmPowerStatus_Type.__name__=_E
_RaisecomAlarmPowerStatus_Object=MibScalar
raisecomAlarmPowerStatus=_RaisecomAlarmPowerStatus_Object((1,3,6,1,4,1,8886,1,1,4,5,3,6),_RaisecomAlarmPowerStatus_Type())
raisecomAlarmPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmPowerStatus.setStatus(_A)
_RaisecomAlarmTemperature_ObjectIdentity=ObjectIdentity
raisecomAlarmTemperature=_RaisecomAlarmTemperature_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,4))
class _RaisecomAlarmTemperatureTrapEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmTemperatureTrapEnable_Type.__name__=_F
_RaisecomAlarmTemperatureTrapEnable_Object=MibScalar
raisecomAlarmTemperatureTrapEnable=_RaisecomAlarmTemperatureTrapEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,4,1),_RaisecomAlarmTemperatureTrapEnable_Type())
raisecomAlarmTemperatureTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmTemperatureTrapEnable.setStatus(_A)
class _RaisecomAlarmTemperatureRelayEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmTemperatureRelayEnable_Type.__name__=_F
_RaisecomAlarmTemperatureRelayEnable_Object=MibScalar
raisecomAlarmTemperatureRelayEnable=_RaisecomAlarmTemperatureRelayEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,4,2),_RaisecomAlarmTemperatureRelayEnable_Type())
raisecomAlarmTemperatureRelayEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmTemperatureRelayEnable.setStatus(_A)
class _RaisecomAlarmTemperatureSyslogEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmTemperatureSyslogEnable_Type.__name__=_F
_RaisecomAlarmTemperatureSyslogEnable_Object=MibScalar
raisecomAlarmTemperatureSyslogEnable=_RaisecomAlarmTemperatureSyslogEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,4,3),_RaisecomAlarmTemperatureSyslogEnable_Type())
raisecomAlarmTemperatureSyslogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmTemperatureSyslogEnable.setStatus(_A)
_RaisecomAlarmVoltage_ObjectIdentity=ObjectIdentity
raisecomAlarmVoltage=_RaisecomAlarmVoltage_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,5))
class _RaisecomAlarmVoltTrapEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmVoltTrapEnable_Type.__name__=_F
_RaisecomAlarmVoltTrapEnable_Object=MibScalar
raisecomAlarmVoltTrapEnable=_RaisecomAlarmVoltTrapEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,5,1),_RaisecomAlarmVoltTrapEnable_Type())
raisecomAlarmVoltTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmVoltTrapEnable.setStatus(_A)
class _RaisecomAlarmVoltRelayEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmVoltRelayEnable_Type.__name__=_F
_RaisecomAlarmVoltRelayEnable_Object=MibScalar
raisecomAlarmVoltRelayEnable=_RaisecomAlarmVoltRelayEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,5,2),_RaisecomAlarmVoltRelayEnable_Type())
raisecomAlarmVoltRelayEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmVoltRelayEnable.setStatus(_A)
class _RaisecomAlarmVoltSyslogEnable_Type(EnableVar):defaultValue=1
_RaisecomAlarmVoltSyslogEnable_Type.__name__=_F
_RaisecomAlarmVoltSyslogEnable_Object=MibScalar
raisecomAlarmVoltSyslogEnable=_RaisecomAlarmVoltSyslogEnable_Object((1,3,6,1,4,1,8886,1,1,4,5,5,3),_RaisecomAlarmVoltSyslogEnable_Type())
raisecomAlarmVoltSyslogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmVoltSyslogEnable.setStatus(_A)
_RaisecomAlarmPort_ObjectIdentity=ObjectIdentity
raisecomAlarmPort=_RaisecomAlarmPort_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,6))
_RaisecomAlarmPortTable_Object=MibTable
raisecomAlarmPortTable=_RaisecomAlarmPortTable_Object((1,3,6,1,4,1,8886,1,1,4,5,6,1))
if mibBuilder.loadTexts:raisecomAlarmPortTable.setStatus(_A)
_RaisecomAlarmPortEntry_Object=MibTableRow
raisecomAlarmPortEntry=_RaisecomAlarmPortEntry_Object((1,3,6,1,4,1,8886,1,1,4,5,6,1,1))
raisecomAlarmPortEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:raisecomAlarmPortEntry.setStatus(_A)
_RaisecomAlarmPortIndex_Type=Integer32
_RaisecomAlarmPortIndex_Object=MibTableColumn
raisecomAlarmPortIndex=_RaisecomAlarmPortIndex_Object((1,3,6,1,4,1,8886,1,1,4,5,6,1,1,1),_RaisecomAlarmPortIndex_Type())
raisecomAlarmPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomAlarmPortIndex.setStatus(_A)
_RaisecomAlarmPortSyslogEvList_Type=PortAlarmEventList
_RaisecomAlarmPortSyslogEvList_Object=MibTableColumn
raisecomAlarmPortSyslogEvList=_RaisecomAlarmPortSyslogEvList_Object((1,3,6,1,4,1,8886,1,1,4,5,6,1,1,2),_RaisecomAlarmPortSyslogEvList_Type())
raisecomAlarmPortSyslogEvList.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmPortSyslogEvList.setStatus(_A)
_RaisecomAlarmPortNotifiesEvList_Type=PortAlarmEventList
_RaisecomAlarmPortNotifiesEvList_Object=MibTableColumn
raisecomAlarmPortNotifiesEvList=_RaisecomAlarmPortNotifiesEvList_Object((1,3,6,1,4,1,8886,1,1,4,5,6,1,1,3),_RaisecomAlarmPortNotifiesEvList_Type())
raisecomAlarmPortNotifiesEvList.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmPortNotifiesEvList.setStatus(_A)
_RaisecomAlarmPortRelayEvList_Type=PortAlarmEventList
_RaisecomAlarmPortRelayEvList_Object=MibTableColumn
raisecomAlarmPortRelayEvList=_RaisecomAlarmPortRelayEvList_Object((1,3,6,1,4,1,8886,1,1,4,5,6,1,1,4),_RaisecomAlarmPortRelayEvList_Type())
raisecomAlarmPortRelayEvList.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomAlarmPortRelayEvList.setStatus(_A)
_RaisecomAlarmPortEvList_Type=PortAlarmEventList
_RaisecomAlarmPortEvList_Object=MibTableColumn
raisecomAlarmPortEvList=_RaisecomAlarmPortEvList_Object((1,3,6,1,4,1,8886,1,1,4,5,6,1,1,5),_RaisecomAlarmPortEvList_Type())
raisecomAlarmPortEvList.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmPortEvList.setStatus(_A)
_RaisecomAlarmHistory_ObjectIdentity=ObjectIdentity
raisecomAlarmHistory=_RaisecomAlarmHistory_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,7))
_RaisecomAlarmHistTable_Object=MibTable
raisecomAlarmHistTable=_RaisecomAlarmHistTable_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1))
if mibBuilder.loadTexts:raisecomAlarmHistTable.setStatus(_A)
_RaisecomAlarmHistEntry_Object=MibTableRow
raisecomAlarmHistEntry=_RaisecomAlarmHistEntry_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1,1))
raisecomAlarmHistEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:raisecomAlarmHistEntry.setStatus(_A)
_RaisecomAlarmHistIndex_Type=Integer32
_RaisecomAlarmHistIndex_Object=MibTableColumn
raisecomAlarmHistIndex=_RaisecomAlarmHistIndex_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1,1,1),_RaisecomAlarmHistIndex_Type())
raisecomAlarmHistIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomAlarmHistIndex.setStatus(_A)
class _RaisecomAlarmHistStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('asserted',1),('cleared',2),('clearall',3)))
_RaisecomAlarmHistStatus_Type.__name__=_E
_RaisecomAlarmHistStatus_Object=MibTableColumn
raisecomAlarmHistStatus=_RaisecomAlarmHistStatus_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1,1,2),_RaisecomAlarmHistStatus_Type())
raisecomAlarmHistStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmHistStatus.setStatus(_I)
_RaisecomAlarmHistSource_Type=Integer32
_RaisecomAlarmHistSource_Object=MibTableColumn
raisecomAlarmHistSource=_RaisecomAlarmHistSource_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1,1,3),_RaisecomAlarmHistSource_Type())
raisecomAlarmHistSource.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmHistSource.setStatus(_A)
class _RaisecomAlarmHistDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RaisecomAlarmHistDescr_Type.__name__=_K
_RaisecomAlarmHistDescr_Object=MibTableColumn
raisecomAlarmHistDescr=_RaisecomAlarmHistDescr_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1,1,4),_RaisecomAlarmHistDescr_Type())
raisecomAlarmHistDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmHistDescr.setStatus(_A)
_RaisecomAlarmHistTimestamp_Type=Integer32
_RaisecomAlarmHistTimestamp_Object=MibTableColumn
raisecomAlarmHistTimestamp=_RaisecomAlarmHistTimestamp_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1,1,5),_RaisecomAlarmHistTimestamp_Type())
raisecomAlarmHistTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmHistTimestamp.setStatus(_A)
class _RaisecomAlarmHistType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_f,0),(_g,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6),(_m,7),(_n,8),('power-normal',9),('normal-temperature',10),('normal-volt',11),('link-up',12),('link-ok',13),('forward',14),('all-alarm',15)))
_RaisecomAlarmHistType_Type.__name__=_E
_RaisecomAlarmHistType_Object=MibTableColumn
raisecomAlarmHistType=_RaisecomAlarmHistType_Object((1,3,6,1,4,1,8886,1,1,4,5,7,1,1,6),_RaisecomAlarmHistType_Type())
raisecomAlarmHistType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmHistType.setStatus(_A)
_RaisecomAlarmCurrent_ObjectIdentity=ObjectIdentity
raisecomAlarmCurrent=_RaisecomAlarmCurrent_ObjectIdentity((1,3,6,1,4,1,8886,1,1,4,5,8))
_RaisecomAlarmCurtTable_Object=MibTable
raisecomAlarmCurtTable=_RaisecomAlarmCurtTable_Object((1,3,6,1,4,1,8886,1,1,4,5,8,1))
if mibBuilder.loadTexts:raisecomAlarmCurtTable.setStatus(_A)
_RaisecomAlarmCurtEntry_Object=MibTableRow
raisecomAlarmCurtEntry=_RaisecomAlarmCurtEntry_Object((1,3,6,1,4,1,8886,1,1,4,5,8,1,1))
raisecomAlarmCurtEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:raisecomAlarmCurtEntry.setStatus(_A)
_RaisecomAlarmCurtIndex_Type=Integer32
_RaisecomAlarmCurtIndex_Object=MibTableColumn
raisecomAlarmCurtIndex=_RaisecomAlarmCurtIndex_Object((1,3,6,1,4,1,8886,1,1,4,5,8,1,1,1),_RaisecomAlarmCurtIndex_Type())
raisecomAlarmCurtIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomAlarmCurtIndex.setStatus(_A)
_RaisecomAlarmCurtSource_Type=Integer32
_RaisecomAlarmCurtSource_Object=MibTableColumn
raisecomAlarmCurtSource=_RaisecomAlarmCurtSource_Object((1,3,6,1,4,1,8886,1,1,4,5,8,1,1,2),_RaisecomAlarmCurtSource_Type())
raisecomAlarmCurtSource.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmCurtSource.setStatus(_A)
class _RaisecomAlarmCurtDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RaisecomAlarmCurtDescr_Type.__name__=_K
_RaisecomAlarmCurtDescr_Object=MibTableColumn
raisecomAlarmCurtDescr=_RaisecomAlarmCurtDescr_Object((1,3,6,1,4,1,8886,1,1,4,5,8,1,1,3),_RaisecomAlarmCurtDescr_Type())
raisecomAlarmCurtDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmCurtDescr.setStatus(_A)
_RaisecomAlarmCurtTimestamp_Type=Integer32
_RaisecomAlarmCurtTimestamp_Object=MibTableColumn
raisecomAlarmCurtTimestamp=_RaisecomAlarmCurtTimestamp_Object((1,3,6,1,4,1,8886,1,1,4,5,8,1,1,4),_RaisecomAlarmCurtTimestamp_Type())
raisecomAlarmCurtTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmCurtTimestamp.setStatus(_A)
class _RaisecomAlarmCurtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_f,0),(_g,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6),(_m,7),(_n,8)))
_RaisecomAlarmCurtType_Type.__name__=_E
_RaisecomAlarmCurtType_Object=MibTableColumn
raisecomAlarmCurtType=_RaisecomAlarmCurtType_Object((1,3,6,1,4,1,8886,1,1,4,5,8,1,1,5),_RaisecomAlarmCurtType_Type())
raisecomAlarmCurtType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmCurtType.setStatus(_A)
raisecomCPURisingThreshold=NotificationType((1,3,6,1,4,1,8886,1,1,1,3,1))
raisecomCPURisingThreshold.setObjects(*((_C,_M),(_C,_p),(_C,_R)))
if mibBuilder.loadTexts:raisecomCPURisingThreshold.setStatus(_A)
raisecomCPUFallingThreshold=NotificationType((1,3,6,1,4,1,8886,1,1,1,3,2))
raisecomCPUFallingThreshold.setObjects((_C,_R))
if mibBuilder.loadTexts:raisecomCPUFallingThreshold.setStatus(_A)
temperatureAbnormalTrap=NotificationType((1,3,6,1,4,1,8886,1,1,4,4,1))
temperatureAbnormalTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:temperatureAbnormalTrap.setStatus(_I)
temperatureNormalTrap=NotificationType((1,3,6,1,4,1,8886,1,1,4,4,2))
temperatureNormalTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:temperatureNormalTrap.setStatus(_I)
raisecomVoltAbnormalTrap=NotificationType((1,3,6,1,4,1,8886,1,1,4,4,3))
raisecomVoltAbnormalTrap.setObjects(*((_C,_N),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:raisecomVoltAbnormalTrap.setStatus(_I)
raisecomVoltNormalTrap=NotificationType((1,3,6,1,4,1,8886,1,1,4,4,4))
raisecomVoltNormalTrap.setObjects(*((_C,_N),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:raisecomVoltNormalTrap.setStatus(_I)
raisecomAlarmInformationTrap=NotificationType((1,3,6,1,4,1,8886,1,1,4,5,1,1))
raisecomAlarmInformationTrap.setObjects(*((_C,_q),(_C,_r),(_C,_s),(_C,_t)))
if mibBuilder.loadTexts:raisecomAlarmInformationTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ProcessStatus':ProcessStatus,'CPUTimeStamp':CPUTimeStamp,'PortAlarmEventList':PortAlarmEventList,'raisecomSystem':raisecomSystem,'raisecomCpu':raisecomCpu,'raisecomCpuBusy1Per':raisecomCpuBusy1Per,'raisecomCpuBusy60Per':raisecomCpuBusy60Per,'raisecomCPUTrapGroup':raisecomCPUTrapGroup,'raisecomCPURisingThreshold':raisecomCPURisingThreshold,'raisecomCPUFallingThreshold':raisecomCPUFallingThreshold,'raisecomCPUScalarGroup':raisecomCPUScalarGroup,'raisecomCPUUtilizationTotal':raisecomCPUUtilizationTotal,'raisecomCPUHistoryTableSize':raisecomCPUHistoryTableSize,'raisecomCPUThresholdTrapEnable':raisecomCPUThresholdTrapEnable,'raisecomCPURisingThresholdValue':raisecomCPURisingThresholdValue,'raisecomCPUFallingThresholdValue':raisecomCPUFallingThresholdValue,'raisecomCPUThresholdInterval':raisecomCPUThresholdInterval,'raisecomCpuTotalProcNum':raisecomCpuTotalProcNum,'raisecomCPUTrapUtilization':raisecomCPUTrapUtilization,'raisecomCPUTableGroup':raisecomCPUTableGroup,'raisecomCPUUtilizationGroup':raisecomCPUUtilizationGroup,'raisecomCPUUtilizationTable':raisecomCPUUtilizationTable,'raisecomCPUUtilizationEntry':raisecomCPUUtilizationEntry,_W:raisecomCPUUtilizationIndex,'raisecomCPUUtilizationPeriod':raisecomCPUUtilizationPeriod,_R:raisecomCPUUtilization,'raisecomCPUHistoryTable':raisecomCPUHistoryTable,'raisecomCPUHistoryEntry':raisecomCPUHistoryEntry,_Y:raisecomCPUHistoryPeriod,_Z:raisecomCPUHistoryIndex,'raisecomCPUHistoryTotalUtil':raisecomCPUHistoryTotalUtil,'raisecomCPUProcessesGroup':raisecomCPUProcessesGroup,'raisecomProcessesTable':raisecomProcessesTable,'raisecomProcessesEntry':raisecomProcessesEntry,_M:raisecomProcessIndex,'raisecomProcessPID':raisecomProcessPID,'raisecomProcessName':raisecomProcessName,'raisecomProcessRunTimeTotal':raisecomProcessRunTimeTotal,'raisecomProcessInvokedTotal':raisecomProcessInvokedTotal,'raisecomProcessTimeCreated':raisecomProcessTimeCreated,'raisecomProcessNormalPriority':raisecomProcessNormalPriority,'raisecomProcessCurrentPriority':raisecomProcessCurrentPriority,'raisecomProcessStatus':raisecomProcessStatus,'raisecomProcessErrorNo':raisecomProcessErrorNo,'raisecomProcessStackSize':raisecomProcessStackSize,'raisecomProcessStackCurrentSize':raisecomProcessStackCurrentSize,'raisecomProcessStackMaxSize':raisecomProcessStackMaxSize,'raisecomProcessStackBegin':raisecomProcessStackBegin,'raisecomProcessStackPointer':raisecomProcessStackPointer,'raisecomProcessStackEnd':raisecomProcessStackEnd,'raisecomProcessProgramCounter':raisecomProcessProgramCounter,'raisecomProcessEntry':raisecomProcessEntry,'raisecomProcessSemWait':raisecomProcessSemWait,'raisecomProcessDelay':raisecomProcessDelay,'raisecomProcessStatisticsTable':raisecomProcessStatisticsTable,'raisecomProcessStatisticsEntry':raisecomProcessStatisticsEntry,_a:raisecomProcessStatisticsPeriod,'raisecomProcessRunTime':raisecomProcessRunTime,'raisecomProcessInvoked':raisecomProcessInvoked,_p:raisecomProcessUtilization,'raisecomDeadProcessesTable':raisecomDeadProcessesTable,'raisecomDeadProcessesEntry':raisecomDeadProcessesEntry,_b:raisecomDeadProcessIndex,'raisecomDeadProcessName':raisecomDeadProcessName,'raisecomDeadProcessEntry':raisecomDeadProcessEntry,'raisecomDeadProcessErrorNo':raisecomDeadProcessErrorNo,'raisecomDeadProcessPriority':raisecomDeadProcessPriority,'raisecomDeadProcessMaxStackSize':raisecomDeadProcessMaxStackSize,'raisecomDeadProcessTimeDelete':raisecomDeadProcessTimeDelete,'raisecomDeadProcessDeadTimes':raisecomDeadProcessDeadTimes,'raisecomDeadProcessStatus':raisecomDeadProcessStatus,'raisecomEndPool':raisecomEndPool,'raisecomEndPoolTable':raisecomEndPoolTable,'raisecomEndPoolEntry':raisecomEndPoolEntry,_c:raisecomBasePort,'raisecomTotalEndPool':raisecomTotalEndPool,'raisecomFreeEndPool':raisecomFreeEndPool,'raisecomMemory':raisecomMemory,'raisecomTotalMemory':raisecomTotalMemory,'raisecomAvailableMemory':raisecomAvailableMemory,'raisecomMaxUtilmemory':raisecomMaxUtilmemory,'raisecomInformation':raisecomInformation,'raisecomDeviceType':raisecomDeviceType,'raisecomTemperature':raisecomTemperature,_S:raisecomTemperatureValue,'raisecomTemperatureMin':raisecomTemperatureMin,'raisecomTemperatureMax':raisecomTemperatureMax,'raisecomTemperatureTrapEnable':raisecomTemperatureTrapEnable,'raisecomTemperatureThresholdLow':raisecomTemperatureThresholdLow,'raisecomTemperatureThresholdHigh':raisecomTemperatureThresholdHigh,'raisecomTemperatureTrapTimes':raisecomTemperatureTrapTimes,'raisecomTemperatureHighTimes':raisecomTemperatureHighTimes,'raisecomTemperatureLowTimes':raisecomTemperatureLowTimes,'raisecomVolt':raisecomVolt,'raisecomVoltTable':raisecomVoltTable,'raisecomVoltEntry':raisecomVoltEntry,_N:raisecomVoltIndex,_T:raisecomVoltReference,_U:raisecomVoltValue,'raisecomVoltMin':raisecomVoltMin,'raisecomVoltMax':raisecomVoltMax,'raisecomVoltTrapEnable':raisecomVoltTrapEnable,'raisecomVoltThresholdLow':raisecomVoltThresholdLow,'raisecomVoltThresholdHigh':raisecomVoltThresholdHigh,'raisecomVoltTrapTimes':raisecomVoltTrapTimes,'raisecomVoltHighTimes':raisecomVoltHighTimes,'raisecomVoltLowTimes':raisecomVoltLowTimes,'raisecomInformationTrap':raisecomInformationTrap,'temperatureAbnormalTrap':temperatureAbnormalTrap,'temperatureNormalTrap':temperatureNormalTrap,'raisecomVoltAbnormalTrap':raisecomVoltAbnormalTrap,'raisecomVoltNormalTrap':raisecomVoltNormalTrap,'raisecomAlarm':raisecomAlarm,'raisecomAlarmTrap':raisecomAlarmTrap,'raisecomAlarmInformationTrap':raisecomAlarmInformationTrap,'raisecomAlarmGlobal':raisecomAlarmGlobal,'raisecomAlarmTrapEnable':raisecomAlarmTrapEnable,'raisecomAlarmSyslogEnable':raisecomAlarmSyslogEnable,'raisecomAlarmClear':raisecomAlarmClear,'raisecomAlarmHwmonitorPeriod':raisecomAlarmHwmonitorPeriod,'raisecomAlarmPower':raisecomAlarmPower,'raisecomAlarmPowerTrapEnable':raisecomAlarmPowerTrapEnable,'raisecomAlarmPowerRelayEnable':raisecomAlarmPowerRelayEnable,'raisecomAlarmPowerSyslogEnable':raisecomAlarmPowerSyslogEnable,'raisecomAlarmPowerOneTimes':raisecomAlarmPowerOneTimes,'raisecomAlarmPowerTwoTimes':raisecomAlarmPowerTwoTimes,'raisecomAlarmPowerStatus':raisecomAlarmPowerStatus,'raisecomAlarmTemperature':raisecomAlarmTemperature,'raisecomAlarmTemperatureTrapEnable':raisecomAlarmTemperatureTrapEnable,'raisecomAlarmTemperatureRelayEnable':raisecomAlarmTemperatureRelayEnable,'raisecomAlarmTemperatureSyslogEnable':raisecomAlarmTemperatureSyslogEnable,'raisecomAlarmVoltage':raisecomAlarmVoltage,'raisecomAlarmVoltTrapEnable':raisecomAlarmVoltTrapEnable,'raisecomAlarmVoltRelayEnable':raisecomAlarmVoltRelayEnable,'raisecomAlarmVoltSyslogEnable':raisecomAlarmVoltSyslogEnable,'raisecomAlarmPort':raisecomAlarmPort,'raisecomAlarmPortTable':raisecomAlarmPortTable,'raisecomAlarmPortEntry':raisecomAlarmPortEntry,_d:raisecomAlarmPortIndex,'raisecomAlarmPortSyslogEvList':raisecomAlarmPortSyslogEvList,'raisecomAlarmPortNotifiesEvList':raisecomAlarmPortNotifiesEvList,'raisecomAlarmPortRelayEvList':raisecomAlarmPortRelayEvList,'raisecomAlarmPortEvList':raisecomAlarmPortEvList,'raisecomAlarmHistory':raisecomAlarmHistory,'raisecomAlarmHistTable':raisecomAlarmHistTable,'raisecomAlarmHistEntry':raisecomAlarmHistEntry,_e:raisecomAlarmHistIndex,'raisecomAlarmHistStatus':raisecomAlarmHistStatus,_q:raisecomAlarmHistSource,_r:raisecomAlarmHistDescr,_s:raisecomAlarmHistTimestamp,_t:raisecomAlarmHistType,'raisecomAlarmCurrent':raisecomAlarmCurrent,'raisecomAlarmCurtTable':raisecomAlarmCurtTable,'raisecomAlarmCurtEntry':raisecomAlarmCurtEntry,_o:raisecomAlarmCurtIndex,'raisecomAlarmCurtSource':raisecomAlarmCurtSource,'raisecomAlarmCurtDescr':raisecomAlarmCurtDescr,'raisecomAlarmCurtTimestamp':raisecomAlarmCurtTimestamp,'raisecomAlarmCurtType':raisecomAlarmCurtType})