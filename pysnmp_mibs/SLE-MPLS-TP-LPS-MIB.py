_a='sleMplsTpLpsMeCfgInfoMegIndex'
_Z='sleMplsTpLspMeCfgInfoGroupIndex'
_Y='sleMplsTpLpsMeCfgInfoMPId'
_X='sleMplsTpLpsMeCfgInfoMeIndex'
_W='disable'
_V='enable'
_U='manual'
_T='micro-seconds'
_S='revertive'
_R='nonrevertive'
_Q='unidirectional'
_P='bidirectional'
_O='oneColonN'
_N='oneColonOne'
_M='onePlusOne'
_L='sleMplsTpLpsCfgInfoGroupIndex'
_K='not-accessible'
_J='backup'
_I='primary'
_H='OctetString'
_G='seconds'
_F='SLE-MPLS-TP-LPS-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleMplsTpLps=ModuleIdentity((1,3,6,1,4,1,6296,101,16,18))
if mibBuilder.loadTexts:sleMplsTpLps.setRevisions(('2012-07-15 00:00',))
_SleMpls_ObjectIdentity=ObjectIdentity
sleMpls=_SleMpls_ObjectIdentity((1,3,6,1,4,1,6296,101,16))
if mibBuilder.loadTexts:sleMpls.setStatus(_A)
_SleMplsTpLpsCfg_ObjectIdentity=ObjectIdentity
sleMplsTpLpsCfg=_SleMplsTpLpsCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,18,1))
_SleMplsTpLpsCfgInfoTable_Object=MibTable
sleMplsTpLpsCfgInfoTable=_SleMplsTpLpsCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,18,1,1))
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoTable.setStatus(_A)
_SleMplsTpLpsCfgInfoEntry_Object=MibTableRow
sleMplsTpLpsCfgInfoEntry=_SleMplsTpLpsCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1))
sleMplsTpLpsCfgInfoEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoEntry.setStatus(_A)
class _SleMplsTpLpsCfgInfoGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpLpsCfgInfoGroupIndex_Type.__name__=_E
_SleMplsTpLpsCfgInfoGroupIndex_Object=MibTableColumn
sleMplsTpLpsCfgInfoGroupIndex=_SleMplsTpLpsCfgInfoGroupIndex_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,1),_SleMplsTpLpsCfgInfoGroupIndex_Type())
sleMplsTpLpsCfgInfoGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoGroupIndex.setStatus(_A)
class _SleMplsTpLpsCfgInfoGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_SleMplsTpLpsCfgInfoGroupName_Type.__name__=_H
_SleMplsTpLpsCfgInfoGroupName_Object=MibTableColumn
sleMplsTpLpsCfgInfoGroupName=_SleMplsTpLpsCfgInfoGroupName_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,2),_SleMplsTpLpsCfgInfoGroupName_Type())
sleMplsTpLpsCfgInfoGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoGroupName.setStatus(_A)
class _SleMplsTpLpsCfgInfoMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_SleMplsTpLpsCfgInfoMode_Type.__name__=_D
_SleMplsTpLpsCfgInfoMode_Object=MibTableColumn
sleMplsTpLpsCfgInfoMode=_SleMplsTpLpsCfgInfoMode_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,3),_SleMplsTpLpsCfgInfoMode_Type())
sleMplsTpLpsCfgInfoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoMode.setStatus(_A)
class _SleMplsTpLpsCfgInfoProtectionScheme_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SleMplsTpLpsCfgInfoProtectionScheme_Type.__name__=_D
_SleMplsTpLpsCfgInfoProtectionScheme_Object=MibTableColumn
sleMplsTpLpsCfgInfoProtectionScheme=_SleMplsTpLpsCfgInfoProtectionScheme_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,4),_SleMplsTpLpsCfgInfoProtectionScheme_Type())
sleMplsTpLpsCfgInfoProtectionScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoProtectionScheme.setStatus(_A)
class _SleMplsTpLpsCfgInfoRevertive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SleMplsTpLpsCfgInfoRevertive_Type.__name__=_D
_SleMplsTpLpsCfgInfoRevertive_Object=MibTableColumn
sleMplsTpLpsCfgInfoRevertive=_SleMplsTpLpsCfgInfoRevertive_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,5),_SleMplsTpLpsCfgInfoRevertive_Type())
sleMplsTpLpsCfgInfoRevertive.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoRevertive.setStatus(_A)
class _SleMplsTpLpsCfgInfoWtr_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_SleMplsTpLpsCfgInfoWtr_Type.__name__=_E
_SleMplsTpLpsCfgInfoWtr_Object=MibTableColumn
sleMplsTpLpsCfgInfoWtr=_SleMplsTpLpsCfgInfoWtr_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,6),_SleMplsTpLpsCfgInfoWtr_Type())
sleMplsTpLpsCfgInfoWtr.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoWtr.setStatus(_A)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoWtr.setUnits(_G)
class _SleMplsTpLpsCfgInfoContinualTxInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SleMplsTpLpsCfgInfoContinualTxInterval_Type.__name__=_E
_SleMplsTpLpsCfgInfoContinualTxInterval_Object=MibTableColumn
sleMplsTpLpsCfgInfoContinualTxInterval=_SleMplsTpLpsCfgInfoContinualTxInterval_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,7),_SleMplsTpLpsCfgInfoContinualTxInterval_Type())
sleMplsTpLpsCfgInfoContinualTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoContinualTxInterval.setStatus(_A)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoContinualTxInterval.setUnits(_G)
class _SleMplsTpLpsCfgInfoRapidTxInterval_Type(Unsigned32):defaultValue=3300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,20000))
_SleMplsTpLpsCfgInfoRapidTxInterval_Type.__name__=_E
_SleMplsTpLpsCfgInfoRapidTxInterval_Object=MibTableColumn
sleMplsTpLpsCfgInfoRapidTxInterval=_SleMplsTpLpsCfgInfoRapidTxInterval_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,8),_SleMplsTpLpsCfgInfoRapidTxInterval_Type())
sleMplsTpLpsCfgInfoRapidTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoRapidTxInterval.setStatus(_A)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoRapidTxInterval.setUnits(_T)
class _SleMplsTpLpsCfgInfoSwitchOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('forced',1),(_U,2)))
_SleMplsTpLpsCfgInfoSwitchOver_Type.__name__=_D
_SleMplsTpLpsCfgInfoSwitchOver_Object=MibTableColumn
sleMplsTpLpsCfgInfoSwitchOver=_SleMplsTpLpsCfgInfoSwitchOver_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,9),_SleMplsTpLpsCfgInfoSwitchOver_Type())
sleMplsTpLpsCfgInfoSwitchOver.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoSwitchOver.setStatus(_A)
class _SleMplsTpLpsCfgInfoLockOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_SleMplsTpLpsCfgInfoLockOut_Type.__name__=_D
_SleMplsTpLpsCfgInfoLockOut_Object=MibTableColumn
sleMplsTpLpsCfgInfoLockOut=_SleMplsTpLpsCfgInfoLockOut_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,10),_SleMplsTpLpsCfgInfoLockOut_Type())
sleMplsTpLpsCfgInfoLockOut.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoLockOut.setStatus(_A)
_SleMplsTpLpsCfgInfoHoldOffTimer_Type=Unsigned32
_SleMplsTpLpsCfgInfoHoldOffTimer_Object=MibTableColumn
sleMplsTpLpsCfgInfoHoldOffTimer=_SleMplsTpLpsCfgInfoHoldOffTimer_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,11),_SleMplsTpLpsCfgInfoHoldOffTimer_Type())
sleMplsTpLpsCfgInfoHoldOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoHoldOffTimer.setStatus(_A)
class _SleMplsTpLpsCfgInfoActivePath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SleMplsTpLpsCfgInfoActivePath_Type.__name__=_D
_SleMplsTpLpsCfgInfoActivePath_Object=MibTableColumn
sleMplsTpLpsCfgInfoActivePath=_SleMplsTpLpsCfgInfoActivePath_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,12),_SleMplsTpLpsCfgInfoActivePath_Type())
sleMplsTpLpsCfgInfoActivePath.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoActivePath.setStatus(_A)
class _SleMplsTpLpsCfgInfoOperationState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_SleMplsTpLpsCfgInfoOperationState_Type.__name__=_D
_SleMplsTpLpsCfgInfoOperationState_Object=MibTableColumn
sleMplsTpLpsCfgInfoOperationState=_SleMplsTpLpsCfgInfoOperationState_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,13),_SleMplsTpLpsCfgInfoOperationState_Type())
sleMplsTpLpsCfgInfoOperationState.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoOperationState.setStatus(_A)
class _SleMplsTpLpsCfgInfoEventStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('normal',1),('protection',2),('localForce',3),('localManual',4),('localSgfProtection',5),('localSgfWorking',6),('localWtr',7),('localLock',8),('localClrSfProtection',9),('localClrSfWorking',10),('localClrEvent',11),('remoteLock',12),('remoteForce',13),('remoteManual',14),('remoteSfProtect',15),('remoteSfWork',16),('remoteWtr',17),('remoteNoReq',18),('remoteNotRevert',19),('noRequest',20),('remoteSdWork',21),('remoteSdProtection',22),('remoteExesWork',23),('remoteExesProtect',24),('remoteRrReqWork',25),('remoteRrReqProtec',26),('remoteNoReqWork',27),('remoteNoReqProtection',28),('localSdProtection',29),('localClearSdProtection',30),('localSdWorking',31),('localClearSdWorking',32),('localExercise',33)))
_SleMplsTpLpsCfgInfoEventStatus_Type.__name__=_D
_SleMplsTpLpsCfgInfoEventStatus_Object=MibTableColumn
sleMplsTpLpsCfgInfoEventStatus=_SleMplsTpLpsCfgInfoEventStatus_Object((1,3,6,1,4,1,6296,101,16,18,1,1,1,14),_SleMplsTpLpsCfgInfoEventStatus_Type())
sleMplsTpLpsCfgInfoEventStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgInfoEventStatus.setStatus(_A)
_SleMplsTpLpsCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpLpsCfgControl=_SleMplsTpLpsCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,18,1,2))
class _SleMplsTpLpsCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('createSleMplsTpLpsCfgEntry',1),('deleteSleMplsTpLpsCfgEntry',2),('setSleMplsTpLpsCfgControProtectionScheme',3),('unsetSleMplsTpLpsCfgControProtectionScheme',4),('setSleMplsLpsTpCfgControlRevertive',5),('setSleMplsLpsTpCfgControlWaitToRestoreset',6),('unsetSleMplsTpLpsCfgControlWaitToRestoreset',7),('setSleMplsLpsTpCfgControlContinualTxInterval',8),('unsetSleMplsTpLpsCfgControlContinualTxInterval',9),('setSleMplsLpsTpCfgControlRapidTxInterval',10),('unsetSleMplsTpLpsCfgControlRapidTxInterval',11),('setSleMplsLpsTpCfgControlSwitchover',12),('unsetSleMplsTpLpsCfgControlSwitchover',13),('setSleMplsTpLpsCfgControlLockOut',14),('unsetSleMplsTpLpsTpCfgControlLockOut',15),('setSleMplsTpLpsCfgControlHoldOffTimer',16),('unSetSleMplsTpLpsCfgControlHoldOffTimer',17)))
_SleMplsTpLpsCfgControlRequest_Type.__name__=_D
_SleMplsTpLpsCfgControlRequest_Object=MibScalar
sleMplsTpLpsCfgControlRequest=_SleMplsTpLpsCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,18,1,2,1),_SleMplsTpLpsCfgControlRequest_Type())
sleMplsTpLpsCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlRequest.setStatus(_A)
_SleMplsTpLpsCfgControlStatus_Type=SleControlStatusType
_SleMplsTpLpsCfgControlStatus_Object=MibScalar
sleMplsTpLpsCfgControlStatus=_SleMplsTpLpsCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,18,1,2,2),_SleMplsTpLpsCfgControlStatus_Type())
sleMplsTpLpsCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlStatus.setStatus(_A)
_SleMplsTpLpsCfgControlTimer_Type=Gauge32
_SleMplsTpLpsCfgControlTimer_Object=MibScalar
sleMplsTpLpsCfgControlTimer=_SleMplsTpLpsCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,18,1,2,3),_SleMplsTpLpsCfgControlTimer_Type())
sleMplsTpLpsCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlTimer.setStatus(_A)
_SleMplsTpLpsCfgControlTimeStamp_Type=TimeTicks
_SleMplsTpLpsCfgControlTimeStamp_Object=MibScalar
sleMplsTpLpsCfgControlTimeStamp=_SleMplsTpLpsCfgControlTimeStamp_Object((1,3,6,1,4,1,6296,101,16,18,1,2,4),_SleMplsTpLpsCfgControlTimeStamp_Type())
sleMplsTpLpsCfgControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlTimeStamp.setStatus(_A)
_SleMplsTpLpsCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpLpsCfgControlReqResult_Object=MibScalar
sleMplsTpLpsCfgControlReqResult=_SleMplsTpLpsCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,18,1,2,5),_SleMplsTpLpsCfgControlReqResult_Type())
sleMplsTpLpsCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlReqResult.setStatus(_A)
class _SleMplsTpLpsCfgControlGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SleMplsTpLpsCfgControlGroupName_Type.__name__=_H
_SleMplsTpLpsCfgControlGroupName_Object=MibScalar
sleMplsTpLpsCfgControlGroupName=_SleMplsTpLpsCfgControlGroupName_Object((1,3,6,1,4,1,6296,101,16,18,1,2,6),_SleMplsTpLpsCfgControlGroupName_Type())
sleMplsTpLpsCfgControlGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlGroupName.setStatus(_A)
class _SleMplsTpLpsCfgControlMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_SleMplsTpLpsCfgControlMode_Type.__name__=_D
_SleMplsTpLpsCfgControlMode_Object=MibScalar
sleMplsTpLpsCfgControlMode=_SleMplsTpLpsCfgControlMode_Object((1,3,6,1,4,1,6296,101,16,18,1,2,7),_SleMplsTpLpsCfgControlMode_Type())
sleMplsTpLpsCfgControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlMode.setStatus(_A)
class _SleMplsTpLpsCfgControlProtectionScheme_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SleMplsTpLpsCfgControlProtectionScheme_Type.__name__=_D
_SleMplsTpLpsCfgControlProtectionScheme_Object=MibScalar
sleMplsTpLpsCfgControlProtectionScheme=_SleMplsTpLpsCfgControlProtectionScheme_Object((1,3,6,1,4,1,6296,101,16,18,1,2,8),_SleMplsTpLpsCfgControlProtectionScheme_Type())
sleMplsTpLpsCfgControlProtectionScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlProtectionScheme.setStatus(_A)
class _SleMplsTpLpsCfgControlRevertive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SleMplsTpLpsCfgControlRevertive_Type.__name__=_D
_SleMplsTpLpsCfgControlRevertive_Object=MibScalar
sleMplsTpLpsCfgControlRevertive=_SleMplsTpLpsCfgControlRevertive_Object((1,3,6,1,4,1,6296,101,16,18,1,2,9),_SleMplsTpLpsCfgControlRevertive_Type())
sleMplsTpLpsCfgControlRevertive.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlRevertive.setStatus(_A)
class _SleMplsTpLpsCfgControlWtr_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_SleMplsTpLpsCfgControlWtr_Type.__name__=_E
_SleMplsTpLpsCfgControlWtr_Object=MibScalar
sleMplsTpLpsCfgControlWtr=_SleMplsTpLpsCfgControlWtr_Object((1,3,6,1,4,1,6296,101,16,18,1,2,10),_SleMplsTpLpsCfgControlWtr_Type())
sleMplsTpLpsCfgControlWtr.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlWtr.setStatus(_A)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlWtr.setUnits(_G)
class _SleMplsTpLpsCfgControlContinualTxInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SleMplsTpLpsCfgControlContinualTxInterval_Type.__name__=_E
_SleMplsTpLpsCfgControlContinualTxInterval_Object=MibScalar
sleMplsTpLpsCfgControlContinualTxInterval=_SleMplsTpLpsCfgControlContinualTxInterval_Object((1,3,6,1,4,1,6296,101,16,18,1,2,11),_SleMplsTpLpsCfgControlContinualTxInterval_Type())
sleMplsTpLpsCfgControlContinualTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlContinualTxInterval.setStatus(_A)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlContinualTxInterval.setUnits(_G)
class _SleMplsTpLpsCfgControlRapidTxInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,1000))
_SleMplsTpLpsCfgControlRapidTxInterval_Type.__name__=_E
_SleMplsTpLpsCfgControlRapidTxInterval_Object=MibScalar
sleMplsTpLpsCfgControlRapidTxInterval=_SleMplsTpLpsCfgControlRapidTxInterval_Object((1,3,6,1,4,1,6296,101,16,18,1,2,12),_SleMplsTpLpsCfgControlRapidTxInterval_Type())
sleMplsTpLpsCfgControlRapidTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlRapidTxInterval.setStatus(_A)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlRapidTxInterval.setUnits(_T)
class _SleMplsTpLpsCfgControlswitchOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('force',1),(_U,2)))
_SleMplsTpLpsCfgControlswitchOver_Type.__name__=_D
_SleMplsTpLpsCfgControlswitchOver_Object=MibScalar
sleMplsTpLpsCfgControlswitchOver=_SleMplsTpLpsCfgControlswitchOver_Object((1,3,6,1,4,1,6296,101,16,18,1,2,13),_SleMplsTpLpsCfgControlswitchOver_Type())
sleMplsTpLpsCfgControlswitchOver.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlswitchOver.setStatus(_A)
class _SleMplsTpLpsCfgControlLockOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_V,1)))
_SleMplsTpLpsCfgControlLockOut_Type.__name__=_D
_SleMplsTpLpsCfgControlLockOut_Object=MibScalar
sleMplsTpLpsCfgControlLockOut=_SleMplsTpLpsCfgControlLockOut_Object((1,3,6,1,4,1,6296,101,16,18,1,2,14),_SleMplsTpLpsCfgControlLockOut_Type())
sleMplsTpLpsCfgControlLockOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlLockOut.setStatus(_A)
_SleMplsTpLpsCfgControlHoldOffTimer_Type=Unsigned32
_SleMplsTpLpsCfgControlHoldOffTimer_Object=MibScalar
sleMplsTpLpsCfgControlHoldOffTimer=_SleMplsTpLpsCfgControlHoldOffTimer_Object((1,3,6,1,4,1,6296,101,16,18,1,2,15),_SleMplsTpLpsCfgControlHoldOffTimer_Type())
sleMplsTpLpsCfgControlHoldOffTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsCfgControlHoldOffTimer.setStatus(_A)
_SleMplsTpLpsMeCfg_ObjectIdentity=ObjectIdentity
sleMplsTpLpsMeCfg=_SleMplsTpLpsMeCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,18,2))
_SleMplsTpLpsMeCfgInfoTable_Object=MibTable
sleMplsTpLpsMeCfgInfoTable=_SleMplsTpLpsMeCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,18,2,1))
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgInfoTable.setStatus(_A)
_SleMplsTpLpsMeCfgInfoEntry_Object=MibTableRow
sleMplsTpLpsMeCfgInfoEntry=_SleMplsTpLpsMeCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,18,2,1,1))
sleMplsTpLpsMeCfgInfoEntry.setIndexNames((0,_F,_X),(0,_F,_Y),(0,_F,_Z),(0,_F,_a))
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgInfoEntry.setStatus(_A)
class _SleMplsTpLpsMeCfgInfoMegIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpLpsMeCfgInfoMegIndex_Type.__name__=_E
_SleMplsTpLpsMeCfgInfoMegIndex_Object=MibTableColumn
sleMplsTpLpsMeCfgInfoMegIndex=_SleMplsTpLpsMeCfgInfoMegIndex_Object((1,3,6,1,4,1,6296,101,16,18,2,1,1,1),_SleMplsTpLpsMeCfgInfoMegIndex_Type())
sleMplsTpLpsMeCfgInfoMegIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgInfoMegIndex.setStatus(_A)
class _SleMplsTpLpsMeCfgInfoMeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpLpsMeCfgInfoMeIndex_Type.__name__=_E
_SleMplsTpLpsMeCfgInfoMeIndex_Object=MibTableColumn
sleMplsTpLpsMeCfgInfoMeIndex=_SleMplsTpLpsMeCfgInfoMeIndex_Object((1,3,6,1,4,1,6296,101,16,18,2,1,1,2),_SleMplsTpLpsMeCfgInfoMeIndex_Type())
sleMplsTpLpsMeCfgInfoMeIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgInfoMeIndex.setStatus(_A)
class _SleMplsTpLpsMeCfgInfoMPId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_SleMplsTpLpsMeCfgInfoMPId_Type.__name__=_E
_SleMplsTpLpsMeCfgInfoMPId_Object=MibTableColumn
sleMplsTpLpsMeCfgInfoMPId=_SleMplsTpLpsMeCfgInfoMPId_Object((1,3,6,1,4,1,6296,101,16,18,2,1,1,3),_SleMplsTpLpsMeCfgInfoMPId_Type())
sleMplsTpLpsMeCfgInfoMPId.setMaxAccess(_K)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgInfoMPId.setStatus(_A)
class _SleMplsTpLspMeCfgInfoGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpLspMeCfgInfoGroupIndex_Type.__name__=_E
_SleMplsTpLspMeCfgInfoGroupIndex_Object=MibTableColumn
sleMplsTpLspMeCfgInfoGroupIndex=_SleMplsTpLspMeCfgInfoGroupIndex_Object((1,3,6,1,4,1,6296,101,16,18,2,1,1,4),_SleMplsTpLspMeCfgInfoGroupIndex_Type())
sleMplsTpLspMeCfgInfoGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLspMeCfgInfoGroupIndex.setStatus(_A)
class _SleMplsTpLpsMeCfgInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SleMplsTpLpsMeCfgInfoState_Type.__name__=_D
_SleMplsTpLpsMeCfgInfoState_Object=MibTableColumn
sleMplsTpLpsMeCfgInfoState=_SleMplsTpLpsMeCfgInfoState_Object((1,3,6,1,4,1,6296,101,16,18,2,1,1,5),_SleMplsTpLpsMeCfgInfoState_Type())
sleMplsTpLpsMeCfgInfoState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgInfoState.setStatus(_A)
_SleMplsTpLpsMeCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpLpsMeCfgControl=_SleMplsTpLpsMeCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,18,2,2))
class _SleMplsTpLpsMeCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('createSleMplsTpLpsMeConfigEntry',1),('deleteSleMplsTpLpsMeConfigEntry',2)))
_SleMplsTpLpsMeCfgControlRequest_Type.__name__=_D
_SleMplsTpLpsMeCfgControlRequest_Object=MibScalar
sleMplsTpLpsMeCfgControlRequest=_SleMplsTpLpsMeCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,18,2,2,1),_SleMplsTpLpsMeCfgControlRequest_Type())
sleMplsTpLpsMeCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlRequest.setStatus(_A)
_SleMplsTpLpsMeCfgControlStatus_Type=SleControlStatusType
_SleMplsTpLpsMeCfgControlStatus_Object=MibScalar
sleMplsTpLpsMeCfgControlStatus=_SleMplsTpLpsMeCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,18,2,2,2),_SleMplsTpLpsMeCfgControlStatus_Type())
sleMplsTpLpsMeCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlStatus.setStatus(_A)
_SleMplsTpLpsMeCfgControlTimer_Type=Gauge32
_SleMplsTpLpsMeCfgControlTimer_Object=MibScalar
sleMplsTpLpsMeCfgControlTimer=_SleMplsTpLpsMeCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,18,2,2,3),_SleMplsTpLpsMeCfgControlTimer_Type())
sleMplsTpLpsMeCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlTimer.setStatus(_A)
_SleMplsTpLpsMeCfgControlTimeStamp_Type=TimeTicks
_SleMplsTpLpsMeCfgControlTimeStamp_Object=MibScalar
sleMplsTpLpsMeCfgControlTimeStamp=_SleMplsTpLpsMeCfgControlTimeStamp_Object((1,3,6,1,4,1,6296,101,16,18,2,2,4),_SleMplsTpLpsMeCfgControlTimeStamp_Type())
sleMplsTpLpsMeCfgControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlTimeStamp.setStatus(_A)
_SleMplsTpLpsMeCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpLpsMeCfgControlReqResult_Object=MibScalar
sleMplsTpLpsMeCfgControlReqResult=_SleMplsTpLpsMeCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,18,2,2,5),_SleMplsTpLpsMeCfgControlReqResult_Type())
sleMplsTpLpsMeCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlReqResult.setStatus(_A)
_SleMplsTpLpsMeCfgControlMegName_Type=OctetString
_SleMplsTpLpsMeCfgControlMegName_Object=MibScalar
sleMplsTpLpsMeCfgControlMegName=_SleMplsTpLpsMeCfgControlMegName_Object((1,3,6,1,4,1,6296,101,16,18,2,2,6),_SleMplsTpLpsMeCfgControlMegName_Type())
sleMplsTpLpsMeCfgControlMegName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlMegName.setStatus(_A)
_SleMplsTpLpsMeCfgControlMeName_Type=OctetString
_SleMplsTpLpsMeCfgControlMeName_Object=MibScalar
sleMplsTpLpsMeCfgControlMeName=_SleMplsTpLpsMeCfgControlMeName_Object((1,3,6,1,4,1,6296,101,16,18,2,2,7),_SleMplsTpLpsMeCfgControlMeName_Type())
sleMplsTpLpsMeCfgControlMeName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlMeName.setStatus(_A)
_SleMplsTpLpsMeCfgControlMpId_Type=Unsigned32
_SleMplsTpLpsMeCfgControlMpId_Object=MibScalar
sleMplsTpLpsMeCfgControlMpId=_SleMplsTpLpsMeCfgControlMpId_Object((1,3,6,1,4,1,6296,101,16,18,2,2,8),_SleMplsTpLpsMeCfgControlMpId_Type())
sleMplsTpLpsMeCfgControlMpId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlMpId.setStatus(_A)
_SleMplsTpLpsMeCfgControlGroupName_Type=OctetString
_SleMplsTpLpsMeCfgControlGroupName_Object=MibScalar
sleMplsTpLpsMeCfgControlGroupName=_SleMplsTpLpsMeCfgControlGroupName_Object((1,3,6,1,4,1,6296,101,16,18,2,2,9),_SleMplsTpLpsMeCfgControlGroupName_Type())
sleMplsTpLpsMeCfgControlGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlGroupName.setStatus(_A)
class _SleMplsTpLpsMeCfgControlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SleMplsTpLpsMeCfgControlState_Type.__name__=_D
_SleMplsTpLpsMeCfgControlState_Object=MibScalar
sleMplsTpLpsMeCfgControlState=_SleMplsTpLpsMeCfgControlState_Object((1,3,6,1,4,1,6296,101,16,18,2,2,10),_SleMplsTpLpsMeCfgControlState_Type())
sleMplsTpLpsMeCfgControlState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpLpsMeCfgControlState.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'sleMpls':sleMpls,'sleMplsTpLps':sleMplsTpLps,'sleMplsTpLpsCfg':sleMplsTpLpsCfg,'sleMplsTpLpsCfgInfoTable':sleMplsTpLpsCfgInfoTable,'sleMplsTpLpsCfgInfoEntry':sleMplsTpLpsCfgInfoEntry,_L:sleMplsTpLpsCfgInfoGroupIndex,'sleMplsTpLpsCfgInfoGroupName':sleMplsTpLpsCfgInfoGroupName,'sleMplsTpLpsCfgInfoMode':sleMplsTpLpsCfgInfoMode,'sleMplsTpLpsCfgInfoProtectionScheme':sleMplsTpLpsCfgInfoProtectionScheme,'sleMplsTpLpsCfgInfoRevertive':sleMplsTpLpsCfgInfoRevertive,'sleMplsTpLpsCfgInfoWtr':sleMplsTpLpsCfgInfoWtr,'sleMplsTpLpsCfgInfoContinualTxInterval':sleMplsTpLpsCfgInfoContinualTxInterval,'sleMplsTpLpsCfgInfoRapidTxInterval':sleMplsTpLpsCfgInfoRapidTxInterval,'sleMplsTpLpsCfgInfoSwitchOver':sleMplsTpLpsCfgInfoSwitchOver,'sleMplsTpLpsCfgInfoLockOut':sleMplsTpLpsCfgInfoLockOut,'sleMplsTpLpsCfgInfoHoldOffTimer':sleMplsTpLpsCfgInfoHoldOffTimer,'sleMplsTpLpsCfgInfoActivePath':sleMplsTpLpsCfgInfoActivePath,'sleMplsTpLpsCfgInfoOperationState':sleMplsTpLpsCfgInfoOperationState,'sleMplsTpLpsCfgInfoEventStatus':sleMplsTpLpsCfgInfoEventStatus,'sleMplsTpLpsCfgControl':sleMplsTpLpsCfgControl,'sleMplsTpLpsCfgControlRequest':sleMplsTpLpsCfgControlRequest,'sleMplsTpLpsCfgControlStatus':sleMplsTpLpsCfgControlStatus,'sleMplsTpLpsCfgControlTimer':sleMplsTpLpsCfgControlTimer,'sleMplsTpLpsCfgControlTimeStamp':sleMplsTpLpsCfgControlTimeStamp,'sleMplsTpLpsCfgControlReqResult':sleMplsTpLpsCfgControlReqResult,'sleMplsTpLpsCfgControlGroupName':sleMplsTpLpsCfgControlGroupName,'sleMplsTpLpsCfgControlMode':sleMplsTpLpsCfgControlMode,'sleMplsTpLpsCfgControlProtectionScheme':sleMplsTpLpsCfgControlProtectionScheme,'sleMplsTpLpsCfgControlRevertive':sleMplsTpLpsCfgControlRevertive,'sleMplsTpLpsCfgControlWtr':sleMplsTpLpsCfgControlWtr,'sleMplsTpLpsCfgControlContinualTxInterval':sleMplsTpLpsCfgControlContinualTxInterval,'sleMplsTpLpsCfgControlRapidTxInterval':sleMplsTpLpsCfgControlRapidTxInterval,'sleMplsTpLpsCfgControlswitchOver':sleMplsTpLpsCfgControlswitchOver,'sleMplsTpLpsCfgControlLockOut':sleMplsTpLpsCfgControlLockOut,'sleMplsTpLpsCfgControlHoldOffTimer':sleMplsTpLpsCfgControlHoldOffTimer,'sleMplsTpLpsMeCfg':sleMplsTpLpsMeCfg,'sleMplsTpLpsMeCfgInfoTable':sleMplsTpLpsMeCfgInfoTable,'sleMplsTpLpsMeCfgInfoEntry':sleMplsTpLpsMeCfgInfoEntry,_a:sleMplsTpLpsMeCfgInfoMegIndex,_X:sleMplsTpLpsMeCfgInfoMeIndex,_Y:sleMplsTpLpsMeCfgInfoMPId,_Z:sleMplsTpLspMeCfgInfoGroupIndex,'sleMplsTpLpsMeCfgInfoState':sleMplsTpLpsMeCfgInfoState,'sleMplsTpLpsMeCfgControl':sleMplsTpLpsMeCfgControl,'sleMplsTpLpsMeCfgControlRequest':sleMplsTpLpsMeCfgControlRequest,'sleMplsTpLpsMeCfgControlStatus':sleMplsTpLpsMeCfgControlStatus,'sleMplsTpLpsMeCfgControlTimer':sleMplsTpLpsMeCfgControlTimer,'sleMplsTpLpsMeCfgControlTimeStamp':sleMplsTpLpsMeCfgControlTimeStamp,'sleMplsTpLpsMeCfgControlReqResult':sleMplsTpLpsMeCfgControlReqResult,'sleMplsTpLpsMeCfgControlMegName':sleMplsTpLpsMeCfgControlMegName,'sleMplsTpLpsMeCfgControlMeName':sleMplsTpLpsMeCfgControlMeName,'sleMplsTpLpsMeCfgControlMpId':sleMplsTpLpsMeCfgControlMpId,'sleMplsTpLpsMeCfgControlGroupName':sleMplsTpLpsMeCfgControlGroupName,'sleMplsTpLpsMeCfgControlState':sleMplsTpLpsMeCfgControlState})