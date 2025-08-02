_AZ='sleSynceSelectionModeChanged'
_AY='sleSynceSyncOptionChanged'
_AX='sleSynceInputSourceLockoutChanged'
_AW='sleSynceInputSourceSwitchChanged'
_AV='sleSynceIfWaitToRestoreChanged'
_AU='sleSynceIfHoldOffChanged'
_AT='sleSynceIfSendQlChanged'
_AS='sleSynceIfRecvQlChanged'
_AR='sleSynceIfDelOutputSourceChanged'
_AQ='sleSynceIfAddOutputSourceChanged'
_AP='sleSynceIfDelInputSourceChanged'
_AO='sleSynceIfAddInputSourceChanged'
_AN='sleSynceIfEnableStateChanged'
_AM='sleSynceInputSourceControlTimer'
_AL='sleSynceInputSourcePriority'
_AK='sleSynceModeControlTimer'
_AJ='sleSynceSelectionMode'
_AI='sleSynceSyncOption'
_AH='sleSynceOutputSourceSendQl'
_AG='sleSynceOutputSourceSystemQl'
_AF='sleSynceOutputSourceConfigSendQl'
_AE='sleSynceOutputSourceName'
_AD='sleSynceInputSourceCmd'
_AC='sleSynceInputSourceSignalFail'
_AB='sleSynceInputSourceRecvQl'
_AA='sleSynceInputSourceConfigRecvQl'
_A9='sleSynceInputSourceSelected'
_A8='sleSynceInputSourceEsmcState'
_A7='sleSynceInputSourceName'
_A6='sleSynceIfControlTimer'
_A5='sleSynceIfWaitToRestore'
_A4='sleSynceIfHoldOff'
_A3='sleSynceIfSendQl'
_A2='sleSynceIfRecvQl'
_A1='sleSynceIfPriority'
_A0='sleSynceIfOoutputSource'
_z='sleSynceIfInputSource'
_y='sleSynceIfName'
_x='sleSynceIfEnableControlTimer'
_w='sleSynceIfEnableState'
_v='sleSynceIfEnableName'
_u='manual'
_t='qlDisable'
_s='qlEnable'
_r='option2gen2'
_q='option2gen1'
_p='option1'
_o='sleSynceModeControlSelectionMode'
_n='sleSynceModeControlSyncOption'
_m='sleSynceInputSourceControlLockoutState'
_l='sleSynceInputSourceControlSwitchType'
_k='sleSynceIfControlWaitToRestore'
_j='sleSynceIfControlHoldOff'
_i='sleSynceIfControlConfigSendQl'
_h='sleSynceIfControlConfigRecvQl'
_g='sleSynceIfControlPriority'
_f='sleSynceIfEnableControlState'
_e='sleSynceIfEnableControlIfIndex'
_d='sleSynceIfEnableControlReqResult'
_c='sleSynceIfEnableControlTimeStamp'
_b='sleSynceIfEnableControlStatus'
_a='sleSynceIfEnableControlRequest'
_Z='sleSynceOutputSourceIfIndex'
_Y='sleSynceInputSourceIfIndex'
_X='sleSynceIfIfIndex'
_W='sleSynceIfEnableIfIndex'
_V='sleSynceInputSourceControlReqResult'
_U='sleSynceInputSourceControlTimeStamp'
_T='sleSynceInputSourceControlStatus'
_S='sleSynceInputSourceControlRequest'
_R='sleSynceModeControlReqResult'
_Q='sleSynceModeControlTimeStamp'
_P='sleSynceModeControlStatus'
_O='sleSynceModeControlRequest'
_N='sleSynceInputSourceControlIfIndex'
_M='enable'
_L='disable'
_K='OctetString'
_J='sleSynceIfControlIfIndex'
_I='sleSynceIfControlReqResult'
_H='sleSynceIfControlTimeStamp'
_G='sleSynceIfControlStatus'
_F='sleSynceIfControlRequest'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='SLE-SYNCE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleSynce=ModuleIdentity((1,3,6,1,4,1,6296,101,93))
class SynceClockQualityLevel(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('none',0),('prc',1),('ssua',2),('ssub',3),('sec',4),('dnu',5),('stu',7),('st2',8),('tnc',9),('st3e',10),('st3',11),('smc',12),('prov',13),('dus',14)))
_SleSynceBaseMode_ObjectIdentity=ObjectIdentity
sleSynceBaseMode=_SleSynceBaseMode_ObjectIdentity((1,3,6,1,4,1,6296,101,93,1))
_SleSynceBaseModeInfo_ObjectIdentity=ObjectIdentity
sleSynceBaseModeInfo=_SleSynceBaseModeInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,93,1,1))
class _SleSynceSyncOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3)))
_SleSynceSyncOption_Type.__name__=_D
_SleSynceSyncOption_Object=MibScalar
sleSynceSyncOption=_SleSynceSyncOption_Object((1,3,6,1,4,1,6296,101,93,1,1,1),_SleSynceSyncOption_Type())
sleSynceSyncOption.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceSyncOption.setStatus(_B)
class _SleSynceSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_t,2)))
_SleSynceSelectionMode_Type.__name__=_D
_SleSynceSelectionMode_Object=MibScalar
sleSynceSelectionMode=_SleSynceSelectionMode_Object((1,3,6,1,4,1,6296,101,93,1,1,2),_SleSynceSelectionMode_Type())
sleSynceSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceSelectionMode.setStatus(_B)
_SleSynceBaseModeControl_ObjectIdentity=ObjectIdentity
sleSynceBaseModeControl=_SleSynceBaseModeControl_ObjectIdentity((1,3,6,1,4,1,6296,101,93,1,2))
class _SleSynceModeControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('setSelectionMode',2))
_SleSynceModeControlRequest_Type.__name__=_D
_SleSynceModeControlRequest_Object=MibScalar
sleSynceModeControlRequest=_SleSynceModeControlRequest_Object((1,3,6,1,4,1,6296,101,93,1,2,1),_SleSynceModeControlRequest_Type())
sleSynceModeControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceModeControlRequest.setStatus(_B)
_SleSynceModeControlStatus_Type=SleControlStatusType
_SleSynceModeControlStatus_Object=MibScalar
sleSynceModeControlStatus=_SleSynceModeControlStatus_Object((1,3,6,1,4,1,6296,101,93,1,2,2),_SleSynceModeControlStatus_Type())
sleSynceModeControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceModeControlStatus.setStatus(_B)
_SleSynceModeControlTimer_Type=Gauge32
_SleSynceModeControlTimer_Object=MibScalar
sleSynceModeControlTimer=_SleSynceModeControlTimer_Object((1,3,6,1,4,1,6296,101,93,1,2,3),_SleSynceModeControlTimer_Type())
sleSynceModeControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceModeControlTimer.setStatus(_B)
_SleSynceModeControlTimeStamp_Type=TimeTicks
_SleSynceModeControlTimeStamp_Object=MibScalar
sleSynceModeControlTimeStamp=_SleSynceModeControlTimeStamp_Object((1,3,6,1,4,1,6296,101,93,1,2,4),_SleSynceModeControlTimeStamp_Type())
sleSynceModeControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceModeControlTimeStamp.setStatus(_B)
_SleSynceModeControlReqResult_Type=SleControlRequestResultType
_SleSynceModeControlReqResult_Object=MibScalar
sleSynceModeControlReqResult=_SleSynceModeControlReqResult_Object((1,3,6,1,4,1,6296,101,93,1,2,5),_SleSynceModeControlReqResult_Type())
sleSynceModeControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceModeControlReqResult.setStatus(_B)
class _SleSynceModeControlSyncOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3)))
_SleSynceModeControlSyncOption_Type.__name__=_D
_SleSynceModeControlSyncOption_Object=MibScalar
sleSynceModeControlSyncOption=_SleSynceModeControlSyncOption_Object((1,3,6,1,4,1,6296,101,93,1,2,6),_SleSynceModeControlSyncOption_Type())
sleSynceModeControlSyncOption.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceModeControlSyncOption.setStatus(_B)
class _SleSynceModeControlSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_t,2)))
_SleSynceModeControlSelectionMode_Type.__name__=_D
_SleSynceModeControlSelectionMode_Object=MibScalar
sleSynceModeControlSelectionMode=_SleSynceModeControlSelectionMode_Object((1,3,6,1,4,1,6296,101,93,1,2,7),_SleSynceModeControlSelectionMode_Type())
sleSynceModeControlSelectionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceModeControlSelectionMode.setStatus(_B)
_SleSynceBaseModeNotification_ObjectIdentity=ObjectIdentity
sleSynceBaseModeNotification=_SleSynceBaseModeNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,93,1,3))
_SleSynceIfEnable_ObjectIdentity=ObjectIdentity
sleSynceIfEnable=_SleSynceIfEnable_ObjectIdentity((1,3,6,1,4,1,6296,101,93,2))
_SleSynceIfEnableTable_Object=MibTable
sleSynceIfEnableTable=_SleSynceIfEnableTable_Object((1,3,6,1,4,1,6296,101,93,2,1))
if mibBuilder.loadTexts:sleSynceIfEnableTable.setStatus(_B)
_SleSynceIfEnableEntry_Object=MibTableRow
sleSynceIfEnableEntry=_SleSynceIfEnableEntry_Object((1,3,6,1,4,1,6296,101,93,2,1,1))
sleSynceIfEnableEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:sleSynceIfEnableEntry.setStatus(_B)
class _SleSynceIfEnableIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSynceIfEnableIfIndex_Type.__name__=_D
_SleSynceIfEnableIfIndex_Object=MibTableColumn
sleSynceIfEnableIfIndex=_SleSynceIfEnableIfIndex_Object((1,3,6,1,4,1,6296,101,93,2,1,1,1),_SleSynceIfEnableIfIndex_Type())
sleSynceIfEnableIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfEnableIfIndex.setStatus(_B)
class _SleSynceIfEnableName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleSynceIfEnableName_Type.__name__=_K
_SleSynceIfEnableName_Object=MibTableColumn
sleSynceIfEnableName=_SleSynceIfEnableName_Object((1,3,6,1,4,1,6296,101,93,2,1,1,2),_SleSynceIfEnableName_Type())
sleSynceIfEnableName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfEnableName.setStatus(_B)
class _SleSynceIfEnableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleSynceIfEnableState_Type.__name__=_D
_SleSynceIfEnableState_Object=MibTableColumn
sleSynceIfEnableState=_SleSynceIfEnableState_Object((1,3,6,1,4,1,6296,101,93,2,1,1,3),_SleSynceIfEnableState_Type())
sleSynceIfEnableState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfEnableState.setStatus(_B)
_SleSynceIfEnableControl_ObjectIdentity=ObjectIdentity
sleSynceIfEnableControl=_SleSynceIfEnableControl_ObjectIdentity((1,3,6,1,4,1,6296,101,93,2,2))
class _SleSynceIfEnableControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setSynceEnable',1))
_SleSynceIfEnableControlRequest_Type.__name__=_D
_SleSynceIfEnableControlRequest_Object=MibScalar
sleSynceIfEnableControlRequest=_SleSynceIfEnableControlRequest_Object((1,3,6,1,4,1,6296,101,93,2,2,1),_SleSynceIfEnableControlRequest_Type())
sleSynceIfEnableControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfEnableControlRequest.setStatus(_B)
_SleSynceIfEnableControlStatus_Type=SleControlStatusType
_SleSynceIfEnableControlStatus_Object=MibScalar
sleSynceIfEnableControlStatus=_SleSynceIfEnableControlStatus_Object((1,3,6,1,4,1,6296,101,93,2,2,2),_SleSynceIfEnableControlStatus_Type())
sleSynceIfEnableControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfEnableControlStatus.setStatus(_B)
_SleSynceIfEnableControlTimer_Type=Gauge32
_SleSynceIfEnableControlTimer_Object=MibScalar
sleSynceIfEnableControlTimer=_SleSynceIfEnableControlTimer_Object((1,3,6,1,4,1,6296,101,93,2,2,3),_SleSynceIfEnableControlTimer_Type())
sleSynceIfEnableControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfEnableControlTimer.setStatus(_B)
_SleSynceIfEnableControlTimeStamp_Type=TimeTicks
_SleSynceIfEnableControlTimeStamp_Object=MibScalar
sleSynceIfEnableControlTimeStamp=_SleSynceIfEnableControlTimeStamp_Object((1,3,6,1,4,1,6296,101,93,2,2,4),_SleSynceIfEnableControlTimeStamp_Type())
sleSynceIfEnableControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfEnableControlTimeStamp.setStatus(_B)
_SleSynceIfEnableControlReqResult_Type=SleControlRequestResultType
_SleSynceIfEnableControlReqResult_Object=MibScalar
sleSynceIfEnableControlReqResult=_SleSynceIfEnableControlReqResult_Object((1,3,6,1,4,1,6296,101,93,2,2,5),_SleSynceIfEnableControlReqResult_Type())
sleSynceIfEnableControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfEnableControlReqResult.setStatus(_B)
class _SleSynceIfEnableControlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleSynceIfEnableControlIfIndex_Type.__name__=_D
_SleSynceIfEnableControlIfIndex_Object=MibScalar
sleSynceIfEnableControlIfIndex=_SleSynceIfEnableControlIfIndex_Object((1,3,6,1,4,1,6296,101,93,2,2,6),_SleSynceIfEnableControlIfIndex_Type())
sleSynceIfEnableControlIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfEnableControlIfIndex.setStatus(_B)
class _SleSynceIfEnableControlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleSynceIfEnableControlState_Type.__name__=_D
_SleSynceIfEnableControlState_Object=MibScalar
sleSynceIfEnableControlState=_SleSynceIfEnableControlState_Object((1,3,6,1,4,1,6296,101,93,2,2,7),_SleSynceIfEnableControlState_Type())
sleSynceIfEnableControlState.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfEnableControlState.setStatus(_B)
_SleSynceIfEnableNotification_ObjectIdentity=ObjectIdentity
sleSynceIfEnableNotification=_SleSynceIfEnableNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,93,2,3))
_SleSynceIf_ObjectIdentity=ObjectIdentity
sleSynceIf=_SleSynceIf_ObjectIdentity((1,3,6,1,4,1,6296,101,93,3))
_SleSynceIfTable_Object=MibTable
sleSynceIfTable=_SleSynceIfTable_Object((1,3,6,1,4,1,6296,101,93,3,1))
if mibBuilder.loadTexts:sleSynceIfTable.setStatus(_B)
_SleSynceIfEntry_Object=MibTableRow
sleSynceIfEntry=_SleSynceIfEntry_Object((1,3,6,1,4,1,6296,101,93,3,1,1))
sleSynceIfEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:sleSynceIfEntry.setStatus(_B)
class _SleSynceIfIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSynceIfIfIndex_Type.__name__=_D
_SleSynceIfIfIndex_Object=MibTableColumn
sleSynceIfIfIndex=_SleSynceIfIfIndex_Object((1,3,6,1,4,1,6296,101,93,3,1,1,1),_SleSynceIfIfIndex_Type())
sleSynceIfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfIfIndex.setStatus(_B)
class _SleSynceIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleSynceIfName_Type.__name__=_K
_SleSynceIfName_Object=MibTableColumn
sleSynceIfName=_SleSynceIfName_Object((1,3,6,1,4,1,6296,101,93,3,1,1,2),_SleSynceIfName_Type())
sleSynceIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfName.setStatus(_B)
class _SleSynceIfInputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleSynceIfInputSource_Type.__name__=_D
_SleSynceIfInputSource_Object=MibTableColumn
sleSynceIfInputSource=_SleSynceIfInputSource_Object((1,3,6,1,4,1,6296,101,93,3,1,1,3),_SleSynceIfInputSource_Type())
sleSynceIfInputSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfInputSource.setStatus(_B)
class _SleSynceIfOoutputSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SleSynceIfOoutputSource_Type.__name__=_D
_SleSynceIfOoutputSource_Object=MibTableColumn
sleSynceIfOoutputSource=_SleSynceIfOoutputSource_Object((1,3,6,1,4,1,6296,101,93,3,1,1,4),_SleSynceIfOoutputSource_Type())
sleSynceIfOoutputSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfOoutputSource.setStatus(_B)
class _SleSynceIfPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SleSynceIfPriority_Type.__name__=_D
_SleSynceIfPriority_Object=MibTableColumn
sleSynceIfPriority=_SleSynceIfPriority_Object((1,3,6,1,4,1,6296,101,93,3,1,1,5),_SleSynceIfPriority_Type())
sleSynceIfPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfPriority.setStatus(_B)
_SleSynceIfRecvQl_Type=SynceClockQualityLevel
_SleSynceIfRecvQl_Object=MibTableColumn
sleSynceIfRecvQl=_SleSynceIfRecvQl_Object((1,3,6,1,4,1,6296,101,93,3,1,1,6),_SleSynceIfRecvQl_Type())
sleSynceIfRecvQl.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfRecvQl.setStatus(_B)
_SleSynceIfSendQl_Type=SynceClockQualityLevel
_SleSynceIfSendQl_Object=MibTableColumn
sleSynceIfSendQl=_SleSynceIfSendQl_Object((1,3,6,1,4,1,6296,101,93,3,1,1,7),_SleSynceIfSendQl_Type())
sleSynceIfSendQl.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfSendQl.setStatus(_B)
class _SleSynceIfHoldOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1800))
_SleSynceIfHoldOff_Type.__name__=_D
_SleSynceIfHoldOff_Object=MibTableColumn
sleSynceIfHoldOff=_SleSynceIfHoldOff_Object((1,3,6,1,4,1,6296,101,93,3,1,1,8),_SleSynceIfHoldOff_Type())
sleSynceIfHoldOff.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfHoldOff.setStatus(_B)
class _SleSynceIfWaitToRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_SleSynceIfWaitToRestore_Type.__name__=_D
_SleSynceIfWaitToRestore_Object=MibTableColumn
sleSynceIfWaitToRestore=_SleSynceIfWaitToRestore_Object((1,3,6,1,4,1,6296,101,93,3,1,1,9),_SleSynceIfWaitToRestore_Type())
sleSynceIfWaitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfWaitToRestore.setStatus(_B)
_SleSynceIfControl_ObjectIdentity=ObjectIdentity
sleSynceIfControl=_SleSynceIfControl_ObjectIdentity((1,3,6,1,4,1,6296,101,93,3,2))
class _SleSynceIfControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('setSynceIfAddInputSource',1),('setSynceIfDelInputSource',2),('setSynceIfAddOutputSource',3),('setSynceIfDelOutputSource',4),('setSynceIfRecvQl',5),('setSynceIfSendQl',6),('setSynceIfHoldOff',7),('setSynceIfWaitToRestore',8)))
_SleSynceIfControlRequest_Type.__name__=_D
_SleSynceIfControlRequest_Object=MibScalar
sleSynceIfControlRequest=_SleSynceIfControlRequest_Object((1,3,6,1,4,1,6296,101,93,3,2,1),_SleSynceIfControlRequest_Type())
sleSynceIfControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlRequest.setStatus(_B)
_SleSynceIfControlStatus_Type=SleControlStatusType
_SleSynceIfControlStatus_Object=MibScalar
sleSynceIfControlStatus=_SleSynceIfControlStatus_Object((1,3,6,1,4,1,6296,101,93,3,2,2),_SleSynceIfControlStatus_Type())
sleSynceIfControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfControlStatus.setStatus(_B)
_SleSynceIfControlTimer_Type=Gauge32
_SleSynceIfControlTimer_Object=MibScalar
sleSynceIfControlTimer=_SleSynceIfControlTimer_Object((1,3,6,1,4,1,6296,101,93,3,2,3),_SleSynceIfControlTimer_Type())
sleSynceIfControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlTimer.setStatus(_B)
_SleSynceIfControlTimeStamp_Type=TimeTicks
_SleSynceIfControlTimeStamp_Object=MibScalar
sleSynceIfControlTimeStamp=_SleSynceIfControlTimeStamp_Object((1,3,6,1,4,1,6296,101,93,3,2,4),_SleSynceIfControlTimeStamp_Type())
sleSynceIfControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfControlTimeStamp.setStatus(_B)
_SleSynceIfControlReqResult_Type=SleControlRequestResultType
_SleSynceIfControlReqResult_Object=MibScalar
sleSynceIfControlReqResult=_SleSynceIfControlReqResult_Object((1,3,6,1,4,1,6296,101,93,3,2,5),_SleSynceIfControlReqResult_Type())
sleSynceIfControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceIfControlReqResult.setStatus(_B)
class _SleSynceIfControlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleSynceIfControlIfIndex_Type.__name__=_D
_SleSynceIfControlIfIndex_Object=MibScalar
sleSynceIfControlIfIndex=_SleSynceIfControlIfIndex_Object((1,3,6,1,4,1,6296,101,93,3,2,6),_SleSynceIfControlIfIndex_Type())
sleSynceIfControlIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlIfIndex.setStatus(_B)
class _SleSynceIfControlPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleSynceIfControlPriority_Type.__name__=_D
_SleSynceIfControlPriority_Object=MibScalar
sleSynceIfControlPriority=_SleSynceIfControlPriority_Object((1,3,6,1,4,1,6296,101,93,3,2,7),_SleSynceIfControlPriority_Type())
sleSynceIfControlPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlPriority.setStatus(_B)
_SleSynceIfControlConfigRecvQl_Type=SynceClockQualityLevel
_SleSynceIfControlConfigRecvQl_Object=MibScalar
sleSynceIfControlConfigRecvQl=_SleSynceIfControlConfigRecvQl_Object((1,3,6,1,4,1,6296,101,93,3,2,8),_SleSynceIfControlConfigRecvQl_Type())
sleSynceIfControlConfigRecvQl.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlConfigRecvQl.setStatus(_B)
_SleSynceIfControlConfigSendQl_Type=SynceClockQualityLevel
_SleSynceIfControlConfigSendQl_Object=MibScalar
sleSynceIfControlConfigSendQl=_SleSynceIfControlConfigSendQl_Object((1,3,6,1,4,1,6296,101,93,3,2,9),_SleSynceIfControlConfigSendQl_Type())
sleSynceIfControlConfigSendQl.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlConfigSendQl.setStatus(_B)
class _SleSynceIfControlHoldOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1800))
_SleSynceIfControlHoldOff_Type.__name__=_D
_SleSynceIfControlHoldOff_Object=MibScalar
sleSynceIfControlHoldOff=_SleSynceIfControlHoldOff_Object((1,3,6,1,4,1,6296,101,93,3,2,10),_SleSynceIfControlHoldOff_Type())
sleSynceIfControlHoldOff.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlHoldOff.setStatus(_B)
class _SleSynceIfControlWaitToRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_SleSynceIfControlWaitToRestore_Type.__name__=_D
_SleSynceIfControlWaitToRestore_Object=MibScalar
sleSynceIfControlWaitToRestore=_SleSynceIfControlWaitToRestore_Object((1,3,6,1,4,1,6296,101,93,3,2,11),_SleSynceIfControlWaitToRestore_Type())
sleSynceIfControlWaitToRestore.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceIfControlWaitToRestore.setStatus(_B)
_SleSynceIfNotification_ObjectIdentity=ObjectIdentity
sleSynceIfNotification=_SleSynceIfNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,93,3,3))
_SleSynceInputSource_ObjectIdentity=ObjectIdentity
sleSynceInputSource=_SleSynceInputSource_ObjectIdentity((1,3,6,1,4,1,6296,101,93,4))
_SleSynceInputSourceTable_Object=MibTable
sleSynceInputSourceTable=_SleSynceInputSourceTable_Object((1,3,6,1,4,1,6296,101,93,4,1))
if mibBuilder.loadTexts:sleSynceInputSourceTable.setStatus(_B)
_SleSynceInputSourceEntry_Object=MibTableRow
sleSynceInputSourceEntry=_SleSynceInputSourceEntry_Object((1,3,6,1,4,1,6296,101,93,4,1,1))
sleSynceInputSourceEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:sleSynceInputSourceEntry.setStatus(_B)
class _SleSynceInputSourceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSynceInputSourceIfIndex_Type.__name__=_D
_SleSynceInputSourceIfIndex_Object=MibTableColumn
sleSynceInputSourceIfIndex=_SleSynceInputSourceIfIndex_Object((1,3,6,1,4,1,6296,101,93,4,1,1,1),_SleSynceInputSourceIfIndex_Type())
sleSynceInputSourceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceIfIndex.setStatus(_B)
class _SleSynceInputSourceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleSynceInputSourceName_Type.__name__=_K
_SleSynceInputSourceName_Object=MibTableColumn
sleSynceInputSourceName=_SleSynceInputSourceName_Object((1,3,6,1,4,1,6296,101,93,4,1,1,2),_SleSynceInputSourceName_Type())
sleSynceInputSourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceName.setStatus(_B)
class _SleSynceInputSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SleSynceInputSourcePriority_Type.__name__=_D
_SleSynceInputSourcePriority_Object=MibTableColumn
sleSynceInputSourcePriority=_SleSynceInputSourcePriority_Object((1,3,6,1,4,1,6296,101,93,4,1,1,3),_SleSynceInputSourcePriority_Type())
sleSynceInputSourcePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourcePriority.setStatus(_B)
class _SleSynceInputSourceEsmcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('idle',0),('start',1),('ok',2),('failed',3)))
_SleSynceInputSourceEsmcState_Type.__name__=_D
_SleSynceInputSourceEsmcState_Object=MibTableColumn
sleSynceInputSourceEsmcState=_SleSynceInputSourceEsmcState_Object((1,3,6,1,4,1,6296,101,93,4,1,1,4),_SleSynceInputSourceEsmcState_Type())
sleSynceInputSourceEsmcState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceEsmcState.setStatus(_B)
class _SleSynceInputSourceSelected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_SleSynceInputSourceSelected_Type.__name__=_D
_SleSynceInputSourceSelected_Object=MibTableColumn
sleSynceInputSourceSelected=_SleSynceInputSourceSelected_Object((1,3,6,1,4,1,6296,101,93,4,1,1,5),_SleSynceInputSourceSelected_Type())
sleSynceInputSourceSelected.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceSelected.setStatus(_B)
_SleSynceInputSourceConfigRecvQl_Type=SynceClockQualityLevel
_SleSynceInputSourceConfigRecvQl_Object=MibTableColumn
sleSynceInputSourceConfigRecvQl=_SleSynceInputSourceConfigRecvQl_Object((1,3,6,1,4,1,6296,101,93,4,1,1,6),_SleSynceInputSourceConfigRecvQl_Type())
sleSynceInputSourceConfigRecvQl.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceConfigRecvQl.setStatus(_B)
_SleSynceInputSourceRecvQl_Type=SynceClockQualityLevel
_SleSynceInputSourceRecvQl_Object=MibTableColumn
sleSynceInputSourceRecvQl=_SleSynceInputSourceRecvQl_Object((1,3,6,1,4,1,6296,101,93,4,1,1,7),_SleSynceInputSourceRecvQl_Type())
sleSynceInputSourceRecvQl.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceRecvQl.setStatus(_B)
class _SleSynceInputSourceSignalFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_SleSynceInputSourceSignalFail_Type.__name__=_D
_SleSynceInputSourceSignalFail_Object=MibTableColumn
sleSynceInputSourceSignalFail=_SleSynceInputSourceSignalFail_Object((1,3,6,1,4,1,6296,101,93,4,1,1,8),_SleSynceInputSourceSignalFail_Type())
sleSynceInputSourceSignalFail.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceSignalFail.setStatus(_B)
class _SleSynceInputSourceCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lockout',1),(_u,2)))
_SleSynceInputSourceCmd_Type.__name__=_D
_SleSynceInputSourceCmd_Object=MibTableColumn
sleSynceInputSourceCmd=_SleSynceInputSourceCmd_Object((1,3,6,1,4,1,6296,101,93,4,1,1,9),_SleSynceInputSourceCmd_Type())
sleSynceInputSourceCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceCmd.setStatus(_B)
_SleSynceInputSourceControl_ObjectIdentity=ObjectIdentity
sleSynceInputSourceControl=_SleSynceInputSourceControl_ObjectIdentity((1,3,6,1,4,1,6296,101,93,4,2))
class _SleSynceInputSourceControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setSynceInputsourceSwitch',1),('setSynceInputsourceLockout',2)))
_SleSynceInputSourceControlRequest_Type.__name__=_D
_SleSynceInputSourceControlRequest_Object=MibScalar
sleSynceInputSourceControlRequest=_SleSynceInputSourceControlRequest_Object((1,3,6,1,4,1,6296,101,93,4,2,1),_SleSynceInputSourceControlRequest_Type())
sleSynceInputSourceControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceInputSourceControlRequest.setStatus(_B)
_SleSynceInputSourceControlStatus_Type=SleControlStatusType
_SleSynceInputSourceControlStatus_Object=MibScalar
sleSynceInputSourceControlStatus=_SleSynceInputSourceControlStatus_Object((1,3,6,1,4,1,6296,101,93,4,2,2),_SleSynceInputSourceControlStatus_Type())
sleSynceInputSourceControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceControlStatus.setStatus(_B)
_SleSynceInputSourceControlTimer_Type=Gauge32
_SleSynceInputSourceControlTimer_Object=MibScalar
sleSynceInputSourceControlTimer=_SleSynceInputSourceControlTimer_Object((1,3,6,1,4,1,6296,101,93,4,2,3),_SleSynceInputSourceControlTimer_Type())
sleSynceInputSourceControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceInputSourceControlTimer.setStatus(_B)
_SleSynceInputSourceControlTimeStamp_Type=TimeTicks
_SleSynceInputSourceControlTimeStamp_Object=MibScalar
sleSynceInputSourceControlTimeStamp=_SleSynceInputSourceControlTimeStamp_Object((1,3,6,1,4,1,6296,101,93,4,2,4),_SleSynceInputSourceControlTimeStamp_Type())
sleSynceInputSourceControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceControlTimeStamp.setStatus(_B)
_SleSynceInputSourceControlReqResult_Type=SleControlRequestResultType
_SleSynceInputSourceControlReqResult_Object=MibScalar
sleSynceInputSourceControlReqResult=_SleSynceInputSourceControlReqResult_Object((1,3,6,1,4,1,6296,101,93,4,2,5),_SleSynceInputSourceControlReqResult_Type())
sleSynceInputSourceControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceInputSourceControlReqResult.setStatus(_B)
class _SleSynceInputSourceControlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleSynceInputSourceControlIfIndex_Type.__name__=_D
_SleSynceInputSourceControlIfIndex_Object=MibScalar
sleSynceInputSourceControlIfIndex=_SleSynceInputSourceControlIfIndex_Object((1,3,6,1,4,1,6296,101,93,4,2,6),_SleSynceInputSourceControlIfIndex_Type())
sleSynceInputSourceControlIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceInputSourceControlIfIndex.setStatus(_B)
class _SleSynceInputSourceControlSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_u,2)))
_SleSynceInputSourceControlSwitchType_Type.__name__=_D
_SleSynceInputSourceControlSwitchType_Object=MibScalar
sleSynceInputSourceControlSwitchType=_SleSynceInputSourceControlSwitchType_Object((1,3,6,1,4,1,6296,101,93,4,2,7),_SleSynceInputSourceControlSwitchType_Type())
sleSynceInputSourceControlSwitchType.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceInputSourceControlSwitchType.setStatus(_B)
class _SleSynceInputSourceControlLockoutState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('clear',0),('set',1)))
_SleSynceInputSourceControlLockoutState_Type.__name__=_D
_SleSynceInputSourceControlLockoutState_Object=MibScalar
sleSynceInputSourceControlLockoutState=_SleSynceInputSourceControlLockoutState_Object((1,3,6,1,4,1,6296,101,93,4,2,8),_SleSynceInputSourceControlLockoutState_Type())
sleSynceInputSourceControlLockoutState.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSynceInputSourceControlLockoutState.setStatus(_B)
_SleSynceInputSourceNotification_ObjectIdentity=ObjectIdentity
sleSynceInputSourceNotification=_SleSynceInputSourceNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,93,4,3))
_SleSynceOutputSource_ObjectIdentity=ObjectIdentity
sleSynceOutputSource=_SleSynceOutputSource_ObjectIdentity((1,3,6,1,4,1,6296,101,93,5))
_SleSynceOutputSourceTable_Object=MibTable
sleSynceOutputSourceTable=_SleSynceOutputSourceTable_Object((1,3,6,1,4,1,6296,101,93,5,1))
if mibBuilder.loadTexts:sleSynceOutputSourceTable.setStatus(_B)
_SleSynceOutputSourceEntry_Object=MibTableRow
sleSynceOutputSourceEntry=_SleSynceOutputSourceEntry_Object((1,3,6,1,4,1,6296,101,93,5,1,1))
sleSynceOutputSourceEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:sleSynceOutputSourceEntry.setStatus(_B)
class _SleSynceOutputSourceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSynceOutputSourceIfIndex_Type.__name__=_D
_SleSynceOutputSourceIfIndex_Object=MibTableColumn
sleSynceOutputSourceIfIndex=_SleSynceOutputSourceIfIndex_Object((1,3,6,1,4,1,6296,101,93,5,1,1,1),_SleSynceOutputSourceIfIndex_Type())
sleSynceOutputSourceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceOutputSourceIfIndex.setStatus(_B)
class _SleSynceOutputSourceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleSynceOutputSourceName_Type.__name__=_K
_SleSynceOutputSourceName_Object=MibTableColumn
sleSynceOutputSourceName=_SleSynceOutputSourceName_Object((1,3,6,1,4,1,6296,101,93,5,1,1,2),_SleSynceOutputSourceName_Type())
sleSynceOutputSourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceOutputSourceName.setStatus(_B)
_SleSynceOutputSourceConfigSendQl_Type=SynceClockQualityLevel
_SleSynceOutputSourceConfigSendQl_Object=MibTableColumn
sleSynceOutputSourceConfigSendQl=_SleSynceOutputSourceConfigSendQl_Object((1,3,6,1,4,1,6296,101,93,5,1,1,3),_SleSynceOutputSourceConfigSendQl_Type())
sleSynceOutputSourceConfigSendQl.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceOutputSourceConfigSendQl.setStatus(_B)
_SleSynceOutputSourceSystemQl_Type=SynceClockQualityLevel
_SleSynceOutputSourceSystemQl_Object=MibTableColumn
sleSynceOutputSourceSystemQl=_SleSynceOutputSourceSystemQl_Object((1,3,6,1,4,1,6296,101,93,5,1,1,4),_SleSynceOutputSourceSystemQl_Type())
sleSynceOutputSourceSystemQl.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceOutputSourceSystemQl.setStatus(_B)
_SleSynceOutputSourceSendQl_Type=SynceClockQualityLevel
_SleSynceOutputSourceSendQl_Object=MibTableColumn
sleSynceOutputSourceSendQl=_SleSynceOutputSourceSendQl_Object((1,3,6,1,4,1,6296,101,93,5,1,1,5),_SleSynceOutputSourceSendQl_Type())
sleSynceOutputSourceSendQl.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSynceOutputSourceSendQl.setStatus(_B)
sleSynceObjectGroup=ObjectGroup((1,3,6,1,4,1,6296,101,93,29))
sleSynceObjectGroup.setObjects(*((_A,_W),(_A,_v),(_A,_w),(_A,_a),(_A,_b),(_A,_x),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_X),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_F),(_A,_G),(_A,_A6),(_A,_H),(_A,_I),(_A,_J),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_Y),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_N),(_A,_l),(_A,_m),(_A,_Z),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_O),(_A,_P),(_A,_AK),(_A,_Q),(_A,_R),(_A,_n),(_A,_o),(_A,_AL),(_A,_S),(_A,_T),(_A,_AM),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:sleSynceObjectGroup.setStatus(_B)
sleSynceSyncOptionChanged=NotificationType((1,3,6,1,4,1,6296,101,93,1,3,1))
sleSynceSyncOptionChanged.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_n)))
if mibBuilder.loadTexts:sleSynceSyncOptionChanged.setStatus(_B)
sleSynceSelectionModeChanged=NotificationType((1,3,6,1,4,1,6296,101,93,1,3,2))
sleSynceSelectionModeChanged.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_o)))
if mibBuilder.loadTexts:sleSynceSelectionModeChanged.setStatus(_B)
sleSynceIfEnableStateChanged=NotificationType((1,3,6,1,4,1,6296,101,93,2,3,1))
sleSynceIfEnableStateChanged.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:sleSynceIfEnableStateChanged.setStatus(_B)
sleSynceIfAddInputSourceChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,1))
sleSynceIfAddInputSourceChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_g)))
if mibBuilder.loadTexts:sleSynceIfAddInputSourceChanged.setStatus(_B)
sleSynceIfDelInputSourceChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,2))
sleSynceIfDelInputSourceChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:sleSynceIfDelInputSourceChanged.setStatus(_B)
sleSynceIfAddOutputSourceChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,3))
sleSynceIfAddOutputSourceChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:sleSynceIfAddOutputSourceChanged.setStatus(_B)
sleSynceIfDelOutputSourceChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,4))
sleSynceIfDelOutputSourceChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:sleSynceIfDelOutputSourceChanged.setStatus(_B)
sleSynceIfRecvQlChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,5))
sleSynceIfRecvQlChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_h)))
if mibBuilder.loadTexts:sleSynceIfRecvQlChanged.setStatus(_B)
sleSynceIfSendQlChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,6))
sleSynceIfSendQlChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_i)))
if mibBuilder.loadTexts:sleSynceIfSendQlChanged.setStatus(_B)
sleSynceIfHoldOffChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,7))
sleSynceIfHoldOffChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_j)))
if mibBuilder.loadTexts:sleSynceIfHoldOffChanged.setStatus(_B)
sleSynceIfWaitToRestoreChanged=NotificationType((1,3,6,1,4,1,6296,101,93,3,3,8))
sleSynceIfWaitToRestoreChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_k)))
if mibBuilder.loadTexts:sleSynceIfWaitToRestoreChanged.setStatus(_B)
sleSynceInputSourceSwitchChanged=NotificationType((1,3,6,1,4,1,6296,101,93,4,3,1))
sleSynceInputSourceSwitchChanged.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_N),(_A,_l)))
if mibBuilder.loadTexts:sleSynceInputSourceSwitchChanged.setStatus(_B)
sleSynceInputSourceLockoutChanged=NotificationType((1,3,6,1,4,1,6296,101,93,4,3,2))
sleSynceInputSourceLockoutChanged.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_N),(_A,_m)))
if mibBuilder.loadTexts:sleSynceInputSourceLockoutChanged.setStatus(_B)
sleSynceNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,93,30))
sleSynceNotificationGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:sleSynceNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SynceClockQualityLevel':SynceClockQualityLevel,'sleSynce':sleSynce,'sleSynceBaseMode':sleSynceBaseMode,'sleSynceBaseModeInfo':sleSynceBaseModeInfo,_AI:sleSynceSyncOption,_AJ:sleSynceSelectionMode,'sleSynceBaseModeControl':sleSynceBaseModeControl,_O:sleSynceModeControlRequest,_P:sleSynceModeControlStatus,_AK:sleSynceModeControlTimer,_Q:sleSynceModeControlTimeStamp,_R:sleSynceModeControlReqResult,_n:sleSynceModeControlSyncOption,_o:sleSynceModeControlSelectionMode,'sleSynceBaseModeNotification':sleSynceBaseModeNotification,_AY:sleSynceSyncOptionChanged,_AZ:sleSynceSelectionModeChanged,'sleSynceIfEnable':sleSynceIfEnable,'sleSynceIfEnableTable':sleSynceIfEnableTable,'sleSynceIfEnableEntry':sleSynceIfEnableEntry,_W:sleSynceIfEnableIfIndex,_v:sleSynceIfEnableName,_w:sleSynceIfEnableState,'sleSynceIfEnableControl':sleSynceIfEnableControl,_a:sleSynceIfEnableControlRequest,_b:sleSynceIfEnableControlStatus,_x:sleSynceIfEnableControlTimer,_c:sleSynceIfEnableControlTimeStamp,_d:sleSynceIfEnableControlReqResult,_e:sleSynceIfEnableControlIfIndex,_f:sleSynceIfEnableControlState,'sleSynceIfEnableNotification':sleSynceIfEnableNotification,_AN:sleSynceIfEnableStateChanged,'sleSynceIf':sleSynceIf,'sleSynceIfTable':sleSynceIfTable,'sleSynceIfEntry':sleSynceIfEntry,_X:sleSynceIfIfIndex,_y:sleSynceIfName,_z:sleSynceIfInputSource,_A0:sleSynceIfOoutputSource,_A1:sleSynceIfPriority,_A2:sleSynceIfRecvQl,_A3:sleSynceIfSendQl,_A4:sleSynceIfHoldOff,_A5:sleSynceIfWaitToRestore,'sleSynceIfControl':sleSynceIfControl,_F:sleSynceIfControlRequest,_G:sleSynceIfControlStatus,_A6:sleSynceIfControlTimer,_H:sleSynceIfControlTimeStamp,_I:sleSynceIfControlReqResult,_J:sleSynceIfControlIfIndex,_g:sleSynceIfControlPriority,_h:sleSynceIfControlConfigRecvQl,_i:sleSynceIfControlConfigSendQl,_j:sleSynceIfControlHoldOff,_k:sleSynceIfControlWaitToRestore,'sleSynceIfNotification':sleSynceIfNotification,_AO:sleSynceIfAddInputSourceChanged,_AP:sleSynceIfDelInputSourceChanged,_AQ:sleSynceIfAddOutputSourceChanged,_AR:sleSynceIfDelOutputSourceChanged,_AS:sleSynceIfRecvQlChanged,_AT:sleSynceIfSendQlChanged,_AU:sleSynceIfHoldOffChanged,_AV:sleSynceIfWaitToRestoreChanged,'sleSynceInputSource':sleSynceInputSource,'sleSynceInputSourceTable':sleSynceInputSourceTable,'sleSynceInputSourceEntry':sleSynceInputSourceEntry,_Y:sleSynceInputSourceIfIndex,_A7:sleSynceInputSourceName,_AL:sleSynceInputSourcePriority,_A8:sleSynceInputSourceEsmcState,_A9:sleSynceInputSourceSelected,_AA:sleSynceInputSourceConfigRecvQl,_AB:sleSynceInputSourceRecvQl,_AC:sleSynceInputSourceSignalFail,_AD:sleSynceInputSourceCmd,'sleSynceInputSourceControl':sleSynceInputSourceControl,_S:sleSynceInputSourceControlRequest,_T:sleSynceInputSourceControlStatus,_AM:sleSynceInputSourceControlTimer,_U:sleSynceInputSourceControlTimeStamp,_V:sleSynceInputSourceControlReqResult,_N:sleSynceInputSourceControlIfIndex,_l:sleSynceInputSourceControlSwitchType,_m:sleSynceInputSourceControlLockoutState,'sleSynceInputSourceNotification':sleSynceInputSourceNotification,_AW:sleSynceInputSourceSwitchChanged,_AX:sleSynceInputSourceLockoutChanged,'sleSynceOutputSource':sleSynceOutputSource,'sleSynceOutputSourceTable':sleSynceOutputSourceTable,'sleSynceOutputSourceEntry':sleSynceOutputSourceEntry,_Z:sleSynceOutputSourceIfIndex,_AE:sleSynceOutputSourceName,_AF:sleSynceOutputSourceConfigSendQl,_AG:sleSynceOutputSourceSystemQl,_AH:sleSynceOutputSourceSendQl,'sleSynceObjectGroup':sleSynceObjectGroup,'sleSynceNotificationGroup':sleSynceNotificationGroup})