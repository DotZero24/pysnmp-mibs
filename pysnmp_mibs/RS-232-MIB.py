_x='rs232SyncGroup'
_w='rs232AsyncGroup'
_v='rs232Group'
_u='rs232SyncPortMinFlags'
_t='rs232SyncPortIdlePattern'
_s='rs232SyncPortMode'
_r='rs232SyncPortRTSCTSDelay'
_q='rs232SyncPortRTSControl'
_p='rs232SyncPortEncoding'
_o='rs232SyncPortRole'
_n='rs232SyncPortAbortedFrames'
_m='rs232SyncPortInterruptedFrames'
_l='rs232SyncPortReceiveOverrunErrs'
_k='rs232SyncPortTransmitUnderrunErrs'
_j='rs232SyncPortFrameCheckErrs'
_i='rs232SyncPortClockSource'
_h='rs232AsyncPortOverrunErrs'
_g='rs232AsyncPortFramingErrs'
_f='rs232AsyncPortParityErrs'
_e='rs232AsyncPortAutobaud'
_d='rs232AsyncPortParity'
_c='rs232AsyncPortStopBits'
_b='rs232AsyncPortBits'
_a='rs232OutSigChanges'
_Z='rs232OutSigState'
_Y='rs232InSigChanges'
_X='rs232InSigState'
_W='rs232PortOutFlowType'
_V='rs232PortInFlowType'
_U='rs232PortOutSpeed'
_T='rs232PortInSpeed'
_S='rs232PortOutSigNumber'
_R='rs232PortInSigNumber'
_Q='rs232PortType'
_P='rs232Number'
_O='dsrDtr'
_N='ctsRts'
_M='rs232OutSigName'
_L='rs232OutSigPortIndex'
_K='rs232InSigName'
_J='rs232InSigPortIndex'
_I='rs232SyncPortIndex'
_H='rs232AsyncPortIndex'
_G='rs232PortIndex'
_F='none'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='RS-232-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rs232=ModuleIdentity((1,3,6,1,2,1,10,33))
_Rs232Number_Type=Integer32
_Rs232Number_Object=MibScalar
rs232Number=_Rs232Number_Object((1,3,6,1,2,1,10,33,1),_Rs232Number_Type())
rs232Number.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232Number.setStatus(_A)
_Rs232PortTable_Object=MibTable
rs232PortTable=_Rs232PortTable_Object((1,3,6,1,2,1,10,33,2))
if mibBuilder.loadTexts:rs232PortTable.setStatus(_A)
_Rs232PortEntry_Object=MibTableRow
rs232PortEntry=_Rs232PortEntry_Object((1,3,6,1,2,1,10,33,2,1))
rs232PortEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:rs232PortEntry.setStatus(_A)
_Rs232PortIndex_Type=InterfaceIndex
_Rs232PortIndex_Object=MibTableColumn
rs232PortIndex=_Rs232PortIndex_Object((1,3,6,1,2,1,10,33,2,1,1),_Rs232PortIndex_Type())
rs232PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232PortIndex.setStatus(_A)
class _Rs232PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('rs232',2),('rs422',3),('rs423',4),('v35',5),('x21',6)))
_Rs232PortType_Type.__name__=_D
_Rs232PortType_Object=MibTableColumn
rs232PortType=_Rs232PortType_Object((1,3,6,1,2,1,10,33,2,1,2),_Rs232PortType_Type())
rs232PortType.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232PortType.setStatus(_A)
_Rs232PortInSigNumber_Type=Integer32
_Rs232PortInSigNumber_Object=MibTableColumn
rs232PortInSigNumber=_Rs232PortInSigNumber_Object((1,3,6,1,2,1,10,33,2,1,3),_Rs232PortInSigNumber_Type())
rs232PortInSigNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232PortInSigNumber.setStatus(_A)
_Rs232PortOutSigNumber_Type=Integer32
_Rs232PortOutSigNumber_Object=MibTableColumn
rs232PortOutSigNumber=_Rs232PortOutSigNumber_Object((1,3,6,1,2,1,10,33,2,1,4),_Rs232PortOutSigNumber_Type())
rs232PortOutSigNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232PortOutSigNumber.setStatus(_A)
_Rs232PortInSpeed_Type=Integer32
_Rs232PortInSpeed_Object=MibTableColumn
rs232PortInSpeed=_Rs232PortInSpeed_Object((1,3,6,1,2,1,10,33,2,1,5),_Rs232PortInSpeed_Type())
rs232PortInSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232PortInSpeed.setStatus(_A)
_Rs232PortOutSpeed_Type=Integer32
_Rs232PortOutSpeed_Object=MibTableColumn
rs232PortOutSpeed=_Rs232PortOutSpeed_Object((1,3,6,1,2,1,10,33,2,1,6),_Rs232PortOutSpeed_Type())
rs232PortOutSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232PortOutSpeed.setStatus(_A)
class _Rs232PortInFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_Rs232PortInFlowType_Type.__name__=_D
_Rs232PortInFlowType_Object=MibTableColumn
rs232PortInFlowType=_Rs232PortInFlowType_Object((1,3,6,1,2,1,10,33,2,1,7),_Rs232PortInFlowType_Type())
rs232PortInFlowType.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232PortInFlowType.setStatus(_A)
class _Rs232PortOutFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_Rs232PortOutFlowType_Type.__name__=_D
_Rs232PortOutFlowType_Object=MibTableColumn
rs232PortOutFlowType=_Rs232PortOutFlowType_Object((1,3,6,1,2,1,10,33,2,1,8),_Rs232PortOutFlowType_Type())
rs232PortOutFlowType.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232PortOutFlowType.setStatus(_A)
_Rs232AsyncPortTable_Object=MibTable
rs232AsyncPortTable=_Rs232AsyncPortTable_Object((1,3,6,1,2,1,10,33,3))
if mibBuilder.loadTexts:rs232AsyncPortTable.setStatus(_A)
_Rs232AsyncPortEntry_Object=MibTableRow
rs232AsyncPortEntry=_Rs232AsyncPortEntry_Object((1,3,6,1,2,1,10,33,3,1))
rs232AsyncPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:rs232AsyncPortEntry.setStatus(_A)
_Rs232AsyncPortIndex_Type=InterfaceIndex
_Rs232AsyncPortIndex_Object=MibTableColumn
rs232AsyncPortIndex=_Rs232AsyncPortIndex_Object((1,3,6,1,2,1,10,33,3,1,1),_Rs232AsyncPortIndex_Type())
rs232AsyncPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232AsyncPortIndex.setStatus(_A)
class _Rs232AsyncPortBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,8))
_Rs232AsyncPortBits_Type.__name__=_D
_Rs232AsyncPortBits_Object=MibTableColumn
rs232AsyncPortBits=_Rs232AsyncPortBits_Object((1,3,6,1,2,1,10,33,3,1,2),_Rs232AsyncPortBits_Type())
rs232AsyncPortBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232AsyncPortBits.setStatus(_A)
class _Rs232AsyncPortStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('one',1),('two',2),('oneAndHalf',3),('dynamic',4)))
_Rs232AsyncPortStopBits_Type.__name__=_D
_Rs232AsyncPortStopBits_Object=MibTableColumn
rs232AsyncPortStopBits=_Rs232AsyncPortStopBits_Object((1,3,6,1,2,1,10,33,3,1,3),_Rs232AsyncPortStopBits_Type())
rs232AsyncPortStopBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232AsyncPortStopBits.setStatus(_A)
class _Rs232AsyncPortParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('odd',2),('even',3),('mark',4),('space',5)))
_Rs232AsyncPortParity_Type.__name__=_D
_Rs232AsyncPortParity_Object=MibTableColumn
rs232AsyncPortParity=_Rs232AsyncPortParity_Object((1,3,6,1,2,1,10,33,3,1,4),_Rs232AsyncPortParity_Type())
rs232AsyncPortParity.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232AsyncPortParity.setStatus(_A)
class _Rs232AsyncPortAutobaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Rs232AsyncPortAutobaud_Type.__name__=_D
_Rs232AsyncPortAutobaud_Object=MibTableColumn
rs232AsyncPortAutobaud=_Rs232AsyncPortAutobaud_Object((1,3,6,1,2,1,10,33,3,1,5),_Rs232AsyncPortAutobaud_Type())
rs232AsyncPortAutobaud.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232AsyncPortAutobaud.setStatus(_A)
_Rs232AsyncPortParityErrs_Type=Counter32
_Rs232AsyncPortParityErrs_Object=MibTableColumn
rs232AsyncPortParityErrs=_Rs232AsyncPortParityErrs_Object((1,3,6,1,2,1,10,33,3,1,6),_Rs232AsyncPortParityErrs_Type())
rs232AsyncPortParityErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232AsyncPortParityErrs.setStatus(_A)
_Rs232AsyncPortFramingErrs_Type=Counter32
_Rs232AsyncPortFramingErrs_Object=MibTableColumn
rs232AsyncPortFramingErrs=_Rs232AsyncPortFramingErrs_Object((1,3,6,1,2,1,10,33,3,1,7),_Rs232AsyncPortFramingErrs_Type())
rs232AsyncPortFramingErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232AsyncPortFramingErrs.setStatus(_A)
_Rs232AsyncPortOverrunErrs_Type=Counter32
_Rs232AsyncPortOverrunErrs_Object=MibTableColumn
rs232AsyncPortOverrunErrs=_Rs232AsyncPortOverrunErrs_Object((1,3,6,1,2,1,10,33,3,1,8),_Rs232AsyncPortOverrunErrs_Type())
rs232AsyncPortOverrunErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232AsyncPortOverrunErrs.setStatus(_A)
_Rs232SyncPortTable_Object=MibTable
rs232SyncPortTable=_Rs232SyncPortTable_Object((1,3,6,1,2,1,10,33,4))
if mibBuilder.loadTexts:rs232SyncPortTable.setStatus(_A)
_Rs232SyncPortEntry_Object=MibTableRow
rs232SyncPortEntry=_Rs232SyncPortEntry_Object((1,3,6,1,2,1,10,33,4,1))
rs232SyncPortEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:rs232SyncPortEntry.setStatus(_A)
_Rs232SyncPortIndex_Type=InterfaceIndex
_Rs232SyncPortIndex_Object=MibTableColumn
rs232SyncPortIndex=_Rs232SyncPortIndex_Object((1,3,6,1,2,1,10,33,4,1,1),_Rs232SyncPortIndex_Type())
rs232SyncPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232SyncPortIndex.setStatus(_A)
class _Rs232SyncPortClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internal',1),('external',2),('split',3)))
_Rs232SyncPortClockSource_Type.__name__=_D
_Rs232SyncPortClockSource_Object=MibTableColumn
rs232SyncPortClockSource=_Rs232SyncPortClockSource_Object((1,3,6,1,2,1,10,33,4,1,2),_Rs232SyncPortClockSource_Type())
rs232SyncPortClockSource.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortClockSource.setStatus(_A)
_Rs232SyncPortFrameCheckErrs_Type=Counter32
_Rs232SyncPortFrameCheckErrs_Object=MibTableColumn
rs232SyncPortFrameCheckErrs=_Rs232SyncPortFrameCheckErrs_Object((1,3,6,1,2,1,10,33,4,1,3),_Rs232SyncPortFrameCheckErrs_Type())
rs232SyncPortFrameCheckErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232SyncPortFrameCheckErrs.setStatus(_A)
_Rs232SyncPortTransmitUnderrunErrs_Type=Counter32
_Rs232SyncPortTransmitUnderrunErrs_Object=MibTableColumn
rs232SyncPortTransmitUnderrunErrs=_Rs232SyncPortTransmitUnderrunErrs_Object((1,3,6,1,2,1,10,33,4,1,4),_Rs232SyncPortTransmitUnderrunErrs_Type())
rs232SyncPortTransmitUnderrunErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232SyncPortTransmitUnderrunErrs.setStatus(_A)
_Rs232SyncPortReceiveOverrunErrs_Type=Counter32
_Rs232SyncPortReceiveOverrunErrs_Object=MibTableColumn
rs232SyncPortReceiveOverrunErrs=_Rs232SyncPortReceiveOverrunErrs_Object((1,3,6,1,2,1,10,33,4,1,5),_Rs232SyncPortReceiveOverrunErrs_Type())
rs232SyncPortReceiveOverrunErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232SyncPortReceiveOverrunErrs.setStatus(_A)
_Rs232SyncPortInterruptedFrames_Type=Counter32
_Rs232SyncPortInterruptedFrames_Object=MibTableColumn
rs232SyncPortInterruptedFrames=_Rs232SyncPortInterruptedFrames_Object((1,3,6,1,2,1,10,33,4,1,6),_Rs232SyncPortInterruptedFrames_Type())
rs232SyncPortInterruptedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232SyncPortInterruptedFrames.setStatus(_A)
_Rs232SyncPortAbortedFrames_Type=Counter32
_Rs232SyncPortAbortedFrames_Object=MibTableColumn
rs232SyncPortAbortedFrames=_Rs232SyncPortAbortedFrames_Object((1,3,6,1,2,1,10,33,4,1,7),_Rs232SyncPortAbortedFrames_Type())
rs232SyncPortAbortedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232SyncPortAbortedFrames.setStatus(_A)
class _Rs232SyncPortRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dte',1),('dce',2)))
_Rs232SyncPortRole_Type.__name__=_D
_Rs232SyncPortRole_Object=MibTableColumn
rs232SyncPortRole=_Rs232SyncPortRole_Object((1,3,6,1,2,1,10,33,4,1,8),_Rs232SyncPortRole_Type())
rs232SyncPortRole.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortRole.setStatus(_A)
class _Rs232SyncPortEncoding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nrz',1),('nrzi',2)))
_Rs232SyncPortEncoding_Type.__name__=_D
_Rs232SyncPortEncoding_Object=MibTableColumn
rs232SyncPortEncoding=_Rs232SyncPortEncoding_Object((1,3,6,1,2,1,10,33,4,1,9),_Rs232SyncPortEncoding_Type())
rs232SyncPortEncoding.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortEncoding.setStatus(_A)
class _Rs232SyncPortRTSControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlled',1),('constant',2)))
_Rs232SyncPortRTSControl_Type.__name__=_D
_Rs232SyncPortRTSControl_Object=MibTableColumn
rs232SyncPortRTSControl=_Rs232SyncPortRTSControl_Object((1,3,6,1,2,1,10,33,4,1,10),_Rs232SyncPortRTSControl_Type())
rs232SyncPortRTSControl.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortRTSControl.setStatus(_A)
class _Rs232SyncPortRTSCTSDelay_Type(Integer32):defaultValue=0
_Rs232SyncPortRTSCTSDelay_Type.__name__=_D
_Rs232SyncPortRTSCTSDelay_Object=MibTableColumn
rs232SyncPortRTSCTSDelay=_Rs232SyncPortRTSCTSDelay_Object((1,3,6,1,2,1,10,33,4,1,11),_Rs232SyncPortRTSCTSDelay_Type())
rs232SyncPortRTSCTSDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortRTSCTSDelay.setStatus(_A)
class _Rs232SyncPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fdx',1),('hdx',2),('simplex-receive',3),('simplex-send',4)))
_Rs232SyncPortMode_Type.__name__=_D
_Rs232SyncPortMode_Object=MibTableColumn
rs232SyncPortMode=_Rs232SyncPortMode_Object((1,3,6,1,2,1,10,33,4,1,12),_Rs232SyncPortMode_Type())
rs232SyncPortMode.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortMode.setStatus(_A)
class _Rs232SyncPortIdlePattern_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mark',1),('space',2)))
_Rs232SyncPortIdlePattern_Type.__name__=_D
_Rs232SyncPortIdlePattern_Object=MibTableColumn
rs232SyncPortIdlePattern=_Rs232SyncPortIdlePattern_Object((1,3,6,1,2,1,10,33,4,1,13),_Rs232SyncPortIdlePattern_Type())
rs232SyncPortIdlePattern.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortIdlePattern.setStatus(_A)
class _Rs232SyncPortMinFlags_Type(Integer32):defaultValue=2
_Rs232SyncPortMinFlags_Type.__name__=_D
_Rs232SyncPortMinFlags_Object=MibTableColumn
rs232SyncPortMinFlags=_Rs232SyncPortMinFlags_Object((1,3,6,1,2,1,10,33,4,1,14),_Rs232SyncPortMinFlags_Type())
rs232SyncPortMinFlags.setMaxAccess(_E)
if mibBuilder.loadTexts:rs232SyncPortMinFlags.setStatus(_A)
_Rs232InSigTable_Object=MibTable
rs232InSigTable=_Rs232InSigTable_Object((1,3,6,1,2,1,10,33,5))
if mibBuilder.loadTexts:rs232InSigTable.setStatus(_A)
_Rs232InSigEntry_Object=MibTableRow
rs232InSigEntry=_Rs232InSigEntry_Object((1,3,6,1,2,1,10,33,5,1))
rs232InSigEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:rs232InSigEntry.setStatus(_A)
_Rs232InSigPortIndex_Type=InterfaceIndex
_Rs232InSigPortIndex_Object=MibTableColumn
rs232InSigPortIndex=_Rs232InSigPortIndex_Object((1,3,6,1,2,1,10,33,5,1,1),_Rs232InSigPortIndex_Type())
rs232InSigPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232InSigPortIndex.setStatus(_A)
class _Rs232InSigName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('rts',1),('cts',2),('dsr',3),('dtr',4),('ri',5),('dcd',6),('sq',7),('srs',8),('srts',9),('scts',10),('sdcd',11)))
_Rs232InSigName_Type.__name__=_D
_Rs232InSigName_Object=MibTableColumn
rs232InSigName=_Rs232InSigName_Object((1,3,6,1,2,1,10,33,5,1,2),_Rs232InSigName_Type())
rs232InSigName.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232InSigName.setStatus(_A)
class _Rs232InSigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('on',2),('off',3)))
_Rs232InSigState_Type.__name__=_D
_Rs232InSigState_Object=MibTableColumn
rs232InSigState=_Rs232InSigState_Object((1,3,6,1,2,1,10,33,5,1,3),_Rs232InSigState_Type())
rs232InSigState.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232InSigState.setStatus(_A)
_Rs232InSigChanges_Type=Counter32
_Rs232InSigChanges_Object=MibTableColumn
rs232InSigChanges=_Rs232InSigChanges_Object((1,3,6,1,2,1,10,33,5,1,4),_Rs232InSigChanges_Type())
rs232InSigChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232InSigChanges.setStatus(_A)
_Rs232OutSigTable_Object=MibTable
rs232OutSigTable=_Rs232OutSigTable_Object((1,3,6,1,2,1,10,33,6))
if mibBuilder.loadTexts:rs232OutSigTable.setStatus(_A)
_Rs232OutSigEntry_Object=MibTableRow
rs232OutSigEntry=_Rs232OutSigEntry_Object((1,3,6,1,2,1,10,33,6,1))
rs232OutSigEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:rs232OutSigEntry.setStatus(_A)
_Rs232OutSigPortIndex_Type=InterfaceIndex
_Rs232OutSigPortIndex_Object=MibTableColumn
rs232OutSigPortIndex=_Rs232OutSigPortIndex_Object((1,3,6,1,2,1,10,33,6,1,1),_Rs232OutSigPortIndex_Type())
rs232OutSigPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232OutSigPortIndex.setStatus(_A)
class _Rs232OutSigName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('rts',1),('cts',2),('dsr',3),('dtr',4),('ri',5),('dcd',6),('sq',7),('srs',8),('srts',9),('scts',10),('sdcd',11)))
_Rs232OutSigName_Type.__name__=_D
_Rs232OutSigName_Object=MibTableColumn
rs232OutSigName=_Rs232OutSigName_Object((1,3,6,1,2,1,10,33,6,1,2),_Rs232OutSigName_Type())
rs232OutSigName.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232OutSigName.setStatus(_A)
class _Rs232OutSigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('on',2),('off',3)))
_Rs232OutSigState_Type.__name__=_D
_Rs232OutSigState_Object=MibTableColumn
rs232OutSigState=_Rs232OutSigState_Object((1,3,6,1,2,1,10,33,6,1,3),_Rs232OutSigState_Type())
rs232OutSigState.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232OutSigState.setStatus(_A)
_Rs232OutSigChanges_Type=Counter32
_Rs232OutSigChanges_Object=MibTableColumn
rs232OutSigChanges=_Rs232OutSigChanges_Object((1,3,6,1,2,1,10,33,6,1,4),_Rs232OutSigChanges_Type())
rs232OutSigChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:rs232OutSigChanges.setStatus(_A)
_Rs232Conformance_ObjectIdentity=ObjectIdentity
rs232Conformance=_Rs232Conformance_ObjectIdentity((1,3,6,1,2,1,10,33,7))
_Rs232Groups_ObjectIdentity=ObjectIdentity
rs232Groups=_Rs232Groups_ObjectIdentity((1,3,6,1,2,1,10,33,7,1))
_Rs232Compliances_ObjectIdentity=ObjectIdentity
rs232Compliances=_Rs232Compliances_ObjectIdentity((1,3,6,1,2,1,10,33,7,2))
rs232Group=ObjectGroup((1,3,6,1,2,1,10,33,7,1,1))
rs232Group.setObjects(*((_B,_P),(_B,_G),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_J),(_B,_K),(_B,_X),(_B,_Y),(_B,_L),(_B,_M),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:rs232Group.setStatus(_A)
rs232AsyncGroup=ObjectGroup((1,3,6,1,2,1,10,33,7,1,2))
rs232AsyncGroup.setObjects(*((_B,_H),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:rs232AsyncGroup.setStatus(_A)
rs232SyncGroup=ObjectGroup((1,3,6,1,2,1,10,33,7,1,3))
rs232SyncGroup.setObjects(*((_B,_I),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:rs232SyncGroup.setStatus(_A)
rs232SyncSDLCGroup=ObjectGroup((1,3,6,1,2,1,10,33,7,1,4))
rs232SyncSDLCGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:rs232SyncSDLCGroup.setStatus(_A)
rs232Compliance=ModuleCompliance((1,3,6,1,2,1,10,33,7,2,1))
rs232Compliance.setObjects(*((_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:rs232Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rs232':rs232,_P:rs232Number,'rs232PortTable':rs232PortTable,'rs232PortEntry':rs232PortEntry,_G:rs232PortIndex,_Q:rs232PortType,_R:rs232PortInSigNumber,_S:rs232PortOutSigNumber,_T:rs232PortInSpeed,_U:rs232PortOutSpeed,_V:rs232PortInFlowType,_W:rs232PortOutFlowType,'rs232AsyncPortTable':rs232AsyncPortTable,'rs232AsyncPortEntry':rs232AsyncPortEntry,_H:rs232AsyncPortIndex,_b:rs232AsyncPortBits,_c:rs232AsyncPortStopBits,_d:rs232AsyncPortParity,_e:rs232AsyncPortAutobaud,_f:rs232AsyncPortParityErrs,_g:rs232AsyncPortFramingErrs,_h:rs232AsyncPortOverrunErrs,'rs232SyncPortTable':rs232SyncPortTable,'rs232SyncPortEntry':rs232SyncPortEntry,_I:rs232SyncPortIndex,_i:rs232SyncPortClockSource,_j:rs232SyncPortFrameCheckErrs,_k:rs232SyncPortTransmitUnderrunErrs,_l:rs232SyncPortReceiveOverrunErrs,_m:rs232SyncPortInterruptedFrames,_n:rs232SyncPortAbortedFrames,_o:rs232SyncPortRole,_p:rs232SyncPortEncoding,_q:rs232SyncPortRTSControl,_r:rs232SyncPortRTSCTSDelay,_s:rs232SyncPortMode,_t:rs232SyncPortIdlePattern,_u:rs232SyncPortMinFlags,'rs232InSigTable':rs232InSigTable,'rs232InSigEntry':rs232InSigEntry,_J:rs232InSigPortIndex,_K:rs232InSigName,_X:rs232InSigState,_Y:rs232InSigChanges,'rs232OutSigTable':rs232OutSigTable,'rs232OutSigEntry':rs232OutSigEntry,_L:rs232OutSigPortIndex,_M:rs232OutSigName,_Z:rs232OutSigState,_a:rs232OutSigChanges,'rs232Conformance':rs232Conformance,'rs232Groups':rs232Groups,_v:rs232Group,_w:rs232AsyncGroup,_x:rs232SyncGroup,'rs232SyncSDLCGroup':rs232SyncSDLCGroup,'rs232Compliances':rs232Compliances,'rs232Compliance':rs232Compliance})