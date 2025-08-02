_M='zxAnMulticastIfTestLogicalId'
_L='zxAnMulticastIfTestIfType'
_K='zxAnMulticastIfTestOnu'
_J='zxAnMulticastIfTestPort'
_I='zxAnMulticastIfTestSlot'
_H='zxAnMulticastIfTestShelf'
_G='zxAnMulticastIfTestRack'
_F='read-create'
_E='not-accessible'
_D='read-only'
_C='ZTE-AN-MULTICAST-TEST-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnMulticastTestMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,28))
_ZxAnMulticastTestGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnMulticastTestGlobalObjects=_ZxAnMulticastTestGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,28,1))
class _ZxAnMulticastTestCapabilities_Type(Bits):namedValues=NamedValues(('supportPriorityAndDuration',0))
_ZxAnMulticastTestCapabilities_Type.__name__='Bits'
_ZxAnMulticastTestCapabilities_Object=MibScalar
zxAnMulticastTestCapabilities=_ZxAnMulticastTestCapabilities_Object((1,3,6,1,4,1,3902,1015,28,1,1),_ZxAnMulticastTestCapabilities_Type())
zxAnMulticastTestCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMulticastTestCapabilities.setStatus(_A)
_ZxAnMulticastTestObjects_ObjectIdentity=ObjectIdentity
zxAnMulticastTestObjects=_ZxAnMulticastTestObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,28,2))
_ZxAnMulticastIfTest_ObjectIdentity=ObjectIdentity
zxAnMulticastIfTest=_ZxAnMulticastIfTest_ObjectIdentity((1,3,6,1,4,1,3902,1015,28,2,1))
_ZxAnMulticastIfTestTable_Object=MibTable
zxAnMulticastIfTestTable=_ZxAnMulticastIfTestTable_Object((1,3,6,1,4,1,3902,1015,28,2,1,2))
if mibBuilder.loadTexts:zxAnMulticastIfTestTable.setStatus(_A)
_ZxAnMulticastIfTestEntry_Object=MibTableRow
zxAnMulticastIfTestEntry=_ZxAnMulticastIfTestEntry_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1))
zxAnMulticastIfTestEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:zxAnMulticastIfTestEntry.setStatus(_A)
_ZxAnMulticastIfTestRack_Type=Integer32
_ZxAnMulticastIfTestRack_Object=MibTableColumn
zxAnMulticastIfTestRack=_ZxAnMulticastIfTestRack_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,1),_ZxAnMulticastIfTestRack_Type())
zxAnMulticastIfTestRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMulticastIfTestRack.setStatus(_A)
_ZxAnMulticastIfTestShelf_Type=Integer32
_ZxAnMulticastIfTestShelf_Object=MibTableColumn
zxAnMulticastIfTestShelf=_ZxAnMulticastIfTestShelf_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,2),_ZxAnMulticastIfTestShelf_Type())
zxAnMulticastIfTestShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMulticastIfTestShelf.setStatus(_A)
_ZxAnMulticastIfTestSlot_Type=Integer32
_ZxAnMulticastIfTestSlot_Object=MibTableColumn
zxAnMulticastIfTestSlot=_ZxAnMulticastIfTestSlot_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,3),_ZxAnMulticastIfTestSlot_Type())
zxAnMulticastIfTestSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMulticastIfTestSlot.setStatus(_A)
_ZxAnMulticastIfTestPort_Type=Integer32
_ZxAnMulticastIfTestPort_Object=MibTableColumn
zxAnMulticastIfTestPort=_ZxAnMulticastIfTestPort_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,4),_ZxAnMulticastIfTestPort_Type())
zxAnMulticastIfTestPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMulticastIfTestPort.setStatus(_A)
_ZxAnMulticastIfTestOnu_Type=Integer32
_ZxAnMulticastIfTestOnu_Object=MibTableColumn
zxAnMulticastIfTestOnu=_ZxAnMulticastIfTestOnu_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,5),_ZxAnMulticastIfTestOnu_Type())
zxAnMulticastIfTestOnu.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMulticastIfTestOnu.setStatus(_A)
class _ZxAnMulticastIfTestIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('physicalPort',1),('bridgePort',2),('ponOnu',3),('ponVPort',4),('onuUni',5)))
_ZxAnMulticastIfTestIfType_Type.__name__=_B
_ZxAnMulticastIfTestIfType_Object=MibTableColumn
zxAnMulticastIfTestIfType=_ZxAnMulticastIfTestIfType_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,6),_ZxAnMulticastIfTestIfType_Type())
zxAnMulticastIfTestIfType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMulticastIfTestIfType.setStatus(_A)
_ZxAnMulticastIfTestLogicalId_Type=ObjectIdentifier
_ZxAnMulticastIfTestLogicalId_Object=MibTableColumn
zxAnMulticastIfTestLogicalId=_ZxAnMulticastIfTestLogicalId_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,7),_ZxAnMulticastIfTestLogicalId_Type())
zxAnMulticastIfTestLogicalId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMulticastIfTestLogicalId.setStatus(_A)
class _ZxAnMulticastIfTestMvlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnMulticastIfTestMvlanId_Type.__name__=_B
_ZxAnMulticastIfTestMvlanId_Object=MibTableColumn
zxAnMulticastIfTestMvlanId=_ZxAnMulticastIfTestMvlanId_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,8),_ZxAnMulticastIfTestMvlanId_Type())
zxAnMulticastIfTestMvlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMulticastIfTestMvlanId.setStatus(_A)
_ZxAnMulticastIfTestGroupIpType_Type=InetAddressType
_ZxAnMulticastIfTestGroupIpType_Object=MibTableColumn
zxAnMulticastIfTestGroupIpType=_ZxAnMulticastIfTestGroupIpType_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,9),_ZxAnMulticastIfTestGroupIpType_Type())
zxAnMulticastIfTestGroupIpType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMulticastIfTestGroupIpType.setStatus(_A)
_ZxAnMulticastIfTestGroupIp_Type=InetAddress
_ZxAnMulticastIfTestGroupIp_Object=MibTableColumn
zxAnMulticastIfTestGroupIp=_ZxAnMulticastIfTestGroupIp_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,10),_ZxAnMulticastIfTestGroupIp_Type())
zxAnMulticastIfTestGroupIp.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMulticastIfTestGroupIp.setStatus(_A)
class _ZxAnMulticastIfTestPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnMulticastIfTestPriority_Type.__name__=_B
_ZxAnMulticastIfTestPriority_Object=MibTableColumn
zxAnMulticastIfTestPriority=_ZxAnMulticastIfTestPriority_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,11),_ZxAnMulticastIfTestPriority_Type())
zxAnMulticastIfTestPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMulticastIfTestPriority.setStatus(_A)
class _ZxAnMulticastIfTestDuration_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_ZxAnMulticastIfTestDuration_Type.__name__=_B
_ZxAnMulticastIfTestDuration_Object=MibTableColumn
zxAnMulticastIfTestDuration=_ZxAnMulticastIfTestDuration_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,12),_ZxAnMulticastIfTestDuration_Type())
zxAnMulticastIfTestDuration.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMulticastIfTestDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnMulticastIfTestDuration.setUnits('Seconds')
class _ZxAnMulticastIfTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('inProgress',2),('success',3),('failed',4)))
_ZxAnMulticastIfTestStatus_Type.__name__=_B
_ZxAnMulticastIfTestStatus_Object=MibTableColumn
zxAnMulticastIfTestStatus=_ZxAnMulticastIfTestStatus_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,20),_ZxAnMulticastIfTestStatus_Type())
zxAnMulticastIfTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMulticastIfTestStatus.setStatus(_A)
class _ZxAnMulticastIfTestFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,255)));namedValues=NamedValues(*(('none',1),('pvcNotExist',2),('mvlanNotExist',3),('groupNotExist',4),('groupInvalid',5),('parameterError',6),('noTrafficDetected',7),('joinFailed',8),('leaveFailed',9),('setAclFailed',10),('setLoopbackFailed',11),('getStatsFailed',12),('hardwareNotSupport',13),('unknown',255)))
_ZxAnMulticastIfTestFailedReason_Type.__name__=_B
_ZxAnMulticastIfTestFailedReason_Object=MibTableColumn
zxAnMulticastIfTestFailedReason=_ZxAnMulticastIfTestFailedReason_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,21),_ZxAnMulticastIfTestFailedReason_Type())
zxAnMulticastIfTestFailedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMulticastIfTestFailedReason.setStatus(_A)
_ZxAnMulticastIfTestBwAfterJoin_Type=Integer32
_ZxAnMulticastIfTestBwAfterJoin_Object=MibTableColumn
zxAnMulticastIfTestBwAfterJoin=_ZxAnMulticastIfTestBwAfterJoin_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,23),_ZxAnMulticastIfTestBwAfterJoin_Type())
zxAnMulticastIfTestBwAfterJoin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMulticastIfTestBwAfterJoin.setStatus(_A)
_ZxAnMulticastIfTestBwAfterLeave_Type=Integer32
_ZxAnMulticastIfTestBwAfterLeave_Object=MibTableColumn
zxAnMulticastIfTestBwAfterLeave=_ZxAnMulticastIfTestBwAfterLeave_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,24),_ZxAnMulticastIfTestBwAfterLeave_Type())
zxAnMulticastIfTestBwAfterLeave.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMulticastIfTestBwAfterLeave.setStatus(_A)
class _ZxAnMulticastIfTestBwUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pps',1),('kbps',2)))
_ZxAnMulticastIfTestBwUnit_Type.__name__=_B
_ZxAnMulticastIfTestBwUnit_Object=MibTableColumn
zxAnMulticastIfTestBwUnit=_ZxAnMulticastIfTestBwUnit_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,25),_ZxAnMulticastIfTestBwUnit_Type())
zxAnMulticastIfTestBwUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMulticastIfTestBwUnit.setStatus(_A)
_ZxAnMulticastIfTestMcastPkts_Type=Counter32
_ZxAnMulticastIfTestMcastPkts_Object=MibTableColumn
zxAnMulticastIfTestMcastPkts=_ZxAnMulticastIfTestMcastPkts_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,26),_ZxAnMulticastIfTestMcastPkts_Type())
zxAnMulticastIfTestMcastPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMulticastIfTestMcastPkts.setStatus(_A)
class _ZxAnMulticastIfTestAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_ZxAnMulticastIfTestAction_Type.__name__=_B
_ZxAnMulticastIfTestAction_Object=MibTableColumn
zxAnMulticastIfTestAction=_ZxAnMulticastIfTestAction_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,30),_ZxAnMulticastIfTestAction_Type())
zxAnMulticastIfTestAction.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMulticastIfTestAction.setStatus(_A)
_ZxAnMulticastIfTestRowStatus_Type=RowStatus
_ZxAnMulticastIfTestRowStatus_Object=MibTableColumn
zxAnMulticastIfTestRowStatus=_ZxAnMulticastIfTestRowStatus_Object((1,3,6,1,4,1,3902,1015,28,2,1,2,1,50),_ZxAnMulticastIfTestRowStatus_Type())
zxAnMulticastIfTestRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnMulticastIfTestRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zxAnMulticastTestMib':zxAnMulticastTestMib,'zxAnMulticastTestGlobalObjects':zxAnMulticastTestGlobalObjects,'zxAnMulticastTestCapabilities':zxAnMulticastTestCapabilities,'zxAnMulticastTestObjects':zxAnMulticastTestObjects,'zxAnMulticastIfTest':zxAnMulticastIfTest,'zxAnMulticastIfTestTable':zxAnMulticastIfTestTable,'zxAnMulticastIfTestEntry':zxAnMulticastIfTestEntry,_G:zxAnMulticastIfTestRack,_H:zxAnMulticastIfTestShelf,_I:zxAnMulticastIfTestSlot,_J:zxAnMulticastIfTestPort,_K:zxAnMulticastIfTestOnu,_L:zxAnMulticastIfTestIfType,_M:zxAnMulticastIfTestLogicalId,'zxAnMulticastIfTestMvlanId':zxAnMulticastIfTestMvlanId,'zxAnMulticastIfTestGroupIpType':zxAnMulticastIfTestGroupIpType,'zxAnMulticastIfTestGroupIp':zxAnMulticastIfTestGroupIp,'zxAnMulticastIfTestPriority':zxAnMulticastIfTestPriority,'zxAnMulticastIfTestDuration':zxAnMulticastIfTestDuration,'zxAnMulticastIfTestStatus':zxAnMulticastIfTestStatus,'zxAnMulticastIfTestFailedReason':zxAnMulticastIfTestFailedReason,'zxAnMulticastIfTestBwAfterJoin':zxAnMulticastIfTestBwAfterJoin,'zxAnMulticastIfTestBwAfterLeave':zxAnMulticastIfTestBwAfterLeave,'zxAnMulticastIfTestBwUnit':zxAnMulticastIfTestBwUnit,'zxAnMulticastIfTestMcastPkts':zxAnMulticastIfTestMcastPkts,'zxAnMulticastIfTestAction':zxAnMulticastIfTestAction,'zxAnMulticastIfTestRowStatus':zxAnMulticastIfTestRowStatus})