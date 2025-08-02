_y='mfrMibTrapGroup'
_x='mfrMibBundleLinkGroup'
_w='mfrMibBundleGroup'
_v='mfrMibTrapBundleLinkMismatch'
_u='mfrBundleLinkMismatch'
_t='mfrBundleLinkUnexpectedSequence'
_s='mfrBundleLinkLoopbackSuspected'
_r='mfrBundleLinkTimerExpiredCount'
_q='mfrBundleLinkFramesControlInvalid'
_p='mfrBundleLinkFramesControlRx'
_o='mfrBundleLinkFramesControlTx'
_n='mfrBundleLinkDelay'
_m='mfrBundleLinkState'
_l='mfrBundleLinkConfigBundleIndex'
_k='mfrBundleLinkRowStatus'
_j='mfrBundleIfIndexMappingIndex'
_i='mfrBundleResequencingErrors'
_h='mfrBundleSeqNumSize'
_g='mfrBundleBandwidth'
_f='mfrBundleLinksActive'
_e='mfrBundleLinksConfigured'
_d='mfrBundleMaxBundleLinks'
_c='mfrBundleMaxDiffDelay'
_b='mfrBundleThreshold'
_a='mfrBundleActivationClass'
_Z='mfrBundleCountMaxRetry'
_Y='mfrBundleTimerAck'
_X='mfrBundleTimerHello'
_W='mfrBundleMaxFragSize'
_V='mfrBundleFragmentation'
_U='mfrBundleRowStatus'
_T='mfrBundleIfIndex'
_S='mfrBundleNextIndex'
_R='mfrBundleMaxNumBundles'
_Q='Milliseconds'
_P='Seconds'
_O='mfrBundleIndex'
_N='mfrBundleLinkFarEndBundleName'
_M='mfrBundleLinkFarEndName'
_L='mfrBundleLinkNearEndName'
_K='mfrBundleFarEndName'
_J='mfrBundleNearEndName'
_I='ifIndex'
_H='IF-MIB'
_G='Frames'
_F='Bundle Links'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='FR-MFR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr')
mfrMib=ModuleIdentity((1,3,6,1,2,1,10,47))
if mibBuilder.loadTexts:mfrMib.setRevisions(('2000-11-30 00:00',))
class MfrBundleLinkState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('mfrBundleLinkStateAddSent',1),('mfrBundleLinkStateAddRx',2),('mfrBundleLinkStateAddAckRx',3),('mfrBundleLinkStateUp',4),('mfrBundleLinkStateIdlePending',5),('mfrBundleLinkStateIdle',6),('mfrBundleLinkStateDown',7),('mfrBundleLinkStateDownIdle',8)))
_MfrMibScalarObjects_ObjectIdentity=ObjectIdentity
mfrMibScalarObjects=_MfrMibScalarObjects_ObjectIdentity((1,3,6,1,2,1,10,47,1))
_MfrBundleMaxNumBundles_Type=Integer32
_MfrBundleMaxNumBundles_Object=MibScalar
mfrBundleMaxNumBundles=_MfrBundleMaxNumBundles_Object((1,3,6,1,2,1,10,47,1,1),_MfrBundleMaxNumBundles_Type())
mfrBundleMaxNumBundles.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleMaxNumBundles.setStatus(_A)
_MfrBundleNextIndex_Type=TestAndIncr
_MfrBundleNextIndex_Object=MibScalar
mfrBundleNextIndex=_MfrBundleNextIndex_Object((1,3,6,1,2,1,10,47,1,2),_MfrBundleNextIndex_Type())
mfrBundleNextIndex.setMaxAccess('read-write')
if mibBuilder.loadTexts:mfrBundleNextIndex.setStatus(_A)
_MfrMibBundleObjects_ObjectIdentity=ObjectIdentity
mfrMibBundleObjects=_MfrMibBundleObjects_ObjectIdentity((1,3,6,1,2,1,10,47,2))
_MfrBundleTable_Object=MibTable
mfrBundleTable=_MfrBundleTable_Object((1,3,6,1,2,1,10,47,2,3))
if mibBuilder.loadTexts:mfrBundleTable.setStatus(_A)
_MfrBundleEntry_Object=MibTableRow
mfrBundleEntry=_MfrBundleEntry_Object((1,3,6,1,2,1,10,47,2,3,1))
mfrBundleEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:mfrBundleEntry.setStatus(_A)
class _MfrBundleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MfrBundleIndex_Type.__name__=_D
_MfrBundleIndex_Object=MibTableColumn
mfrBundleIndex=_MfrBundleIndex_Object((1,3,6,1,2,1,10,47,2,3,1,1),_MfrBundleIndex_Type())
mfrBundleIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mfrBundleIndex.setStatus(_A)
_MfrBundleIfIndex_Type=InterfaceIndex
_MfrBundleIfIndex_Object=MibTableColumn
mfrBundleIfIndex=_MfrBundleIfIndex_Object((1,3,6,1,2,1,10,47,2,3,1,2),_MfrBundleIfIndex_Type())
mfrBundleIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleIfIndex.setStatus(_A)
_MfrBundleRowStatus_Type=RowStatus
_MfrBundleRowStatus_Object=MibTableColumn
mfrBundleRowStatus=_MfrBundleRowStatus_Object((1,3,6,1,2,1,10,47,2,3,1,3),_MfrBundleRowStatus_Type())
mfrBundleRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleRowStatus.setStatus(_A)
_MfrBundleNearEndName_Type=SnmpAdminString
_MfrBundleNearEndName_Object=MibTableColumn
mfrBundleNearEndName=_MfrBundleNearEndName_Object((1,3,6,1,2,1,10,47,2,3,1,4),_MfrBundleNearEndName_Type())
mfrBundleNearEndName.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleNearEndName.setStatus(_A)
class _MfrBundleFragmentation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MfrBundleFragmentation_Type.__name__=_D
_MfrBundleFragmentation_Object=MibTableColumn
mfrBundleFragmentation=_MfrBundleFragmentation_Object((1,3,6,1,2,1,10,47,2,3,1,5),_MfrBundleFragmentation_Type())
mfrBundleFragmentation.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleFragmentation.setStatus(_A)
class _MfrBundleMaxFragSize_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,8184))
_MfrBundleMaxFragSize_Type.__name__=_D
_MfrBundleMaxFragSize_Object=MibTableColumn
mfrBundleMaxFragSize=_MfrBundleMaxFragSize_Object((1,3,6,1,2,1,10,47,2,3,1,6),_MfrBundleMaxFragSize_Type())
mfrBundleMaxFragSize.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleMaxFragSize.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleMaxFragSize.setUnits('Octets')
class _MfrBundleTimerHello_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_MfrBundleTimerHello_Type.__name__=_D
_MfrBundleTimerHello_Object=MibTableColumn
mfrBundleTimerHello=_MfrBundleTimerHello_Object((1,3,6,1,2,1,10,47,2,3,1,7),_MfrBundleTimerHello_Type())
mfrBundleTimerHello.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleTimerHello.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleTimerHello.setUnits(_P)
class _MfrBundleTimerAck_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MfrBundleTimerAck_Type.__name__=_D
_MfrBundleTimerAck_Object=MibTableColumn
mfrBundleTimerAck=_MfrBundleTimerAck_Object((1,3,6,1,2,1,10,47,2,3,1,8),_MfrBundleTimerAck_Type())
mfrBundleTimerAck.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleTimerAck.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleTimerAck.setUnits(_P)
class _MfrBundleCountMaxRetry_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_MfrBundleCountMaxRetry_Type.__name__=_D
_MfrBundleCountMaxRetry_Object=MibTableColumn
mfrBundleCountMaxRetry=_MfrBundleCountMaxRetry_Object((1,3,6,1,2,1,10,47,2,3,1,9),_MfrBundleCountMaxRetry_Type())
mfrBundleCountMaxRetry.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleCountMaxRetry.setStatus(_A)
class _MfrBundleActivationClass_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mfrBundleActivationClassA',1),('mfrBundleActivationClassB',2),('mfrBundleActivationClassC',3),('mfrBundleActivationClassD',4)))
_MfrBundleActivationClass_Type.__name__=_D
_MfrBundleActivationClass_Object=MibTableColumn
mfrBundleActivationClass=_MfrBundleActivationClass_Object((1,3,6,1,2,1,10,47,2,3,1,10),_MfrBundleActivationClass_Type())
mfrBundleActivationClass.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleActivationClass.setStatus(_A)
class _MfrBundleThreshold_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MfrBundleThreshold_Type.__name__=_D
_MfrBundleThreshold_Object=MibTableColumn
mfrBundleThreshold=_MfrBundleThreshold_Object((1,3,6,1,2,1,10,47,2,3,1,11),_MfrBundleThreshold_Type())
mfrBundleThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleThreshold.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleThreshold.setUnits(_F)
class _MfrBundleMaxDiffDelay_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MfrBundleMaxDiffDelay_Type.__name__=_D
_MfrBundleMaxDiffDelay_Object=MibTableColumn
mfrBundleMaxDiffDelay=_MfrBundleMaxDiffDelay_Object((1,3,6,1,2,1,10,47,2,3,1,12),_MfrBundleMaxDiffDelay_Type())
mfrBundleMaxDiffDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleMaxDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleMaxDiffDelay.setUnits(_Q)
class _MfrBundleSeqNumSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('seqNumSize12bit',1),('seqNumSize24bit',2)))
_MfrBundleSeqNumSize_Type.__name__=_D
_MfrBundleSeqNumSize_Object=MibTableColumn
mfrBundleSeqNumSize=_MfrBundleSeqNumSize_Object((1,3,6,1,2,1,10,47,2,3,1,13),_MfrBundleSeqNumSize_Type())
mfrBundleSeqNumSize.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleSeqNumSize.setStatus(_A)
class _MfrBundleMaxBundleLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MfrBundleMaxBundleLinks_Type.__name__=_D
_MfrBundleMaxBundleLinks_Object=MibTableColumn
mfrBundleMaxBundleLinks=_MfrBundleMaxBundleLinks_Object((1,3,6,1,2,1,10,47,2,3,1,14),_MfrBundleMaxBundleLinks_Type())
mfrBundleMaxBundleLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleMaxBundleLinks.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleMaxBundleLinks.setUnits(_F)
class _MfrBundleLinksConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MfrBundleLinksConfigured_Type.__name__=_D
_MfrBundleLinksConfigured_Object=MibTableColumn
mfrBundleLinksConfigured=_MfrBundleLinksConfigured_Object((1,3,6,1,2,1,10,47,2,3,1,15),_MfrBundleLinksConfigured_Type())
mfrBundleLinksConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinksConfigured.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinksConfigured.setUnits(_F)
class _MfrBundleLinksActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MfrBundleLinksActive_Type.__name__=_D
_MfrBundleLinksActive_Object=MibTableColumn
mfrBundleLinksActive=_MfrBundleLinksActive_Object((1,3,6,1,2,1,10,47,2,3,1,16),_MfrBundleLinksActive_Type())
mfrBundleLinksActive.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinksActive.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinksActive.setUnits(_F)
_MfrBundleBandwidth_Type=Integer32
_MfrBundleBandwidth_Object=MibTableColumn
mfrBundleBandwidth=_MfrBundleBandwidth_Object((1,3,6,1,2,1,10,47,2,3,1,17),_MfrBundleBandwidth_Type())
mfrBundleBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleBandwidth.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleBandwidth.setUnits('Bits/Sec')
_MfrBundleFarEndName_Type=SnmpAdminString
_MfrBundleFarEndName_Object=MibTableColumn
mfrBundleFarEndName=_MfrBundleFarEndName_Object((1,3,6,1,2,1,10,47,2,3,1,18),_MfrBundleFarEndName_Type())
mfrBundleFarEndName.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleFarEndName.setStatus(_A)
_MfrBundleResequencingErrors_Type=Counter32
_MfrBundleResequencingErrors_Object=MibTableColumn
mfrBundleResequencingErrors=_MfrBundleResequencingErrors_Object((1,3,6,1,2,1,10,47,2,3,1,19),_MfrBundleResequencingErrors_Type())
mfrBundleResequencingErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleResequencingErrors.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleResequencingErrors.setUnits('Error Events')
_MfrBundleIfIndexMappingTable_Object=MibTable
mfrBundleIfIndexMappingTable=_MfrBundleIfIndexMappingTable_Object((1,3,6,1,2,1,10,47,2,4))
if mibBuilder.loadTexts:mfrBundleIfIndexMappingTable.setStatus(_A)
_MfrBundleIfIndexMappingEntry_Object=MibTableRow
mfrBundleIfIndexMappingEntry=_MfrBundleIfIndexMappingEntry_Object((1,3,6,1,2,1,10,47,2,4,1))
mfrBundleIfIndexMappingEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mfrBundleIfIndexMappingEntry.setStatus(_A)
class _MfrBundleIfIndexMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MfrBundleIfIndexMappingIndex_Type.__name__=_D
_MfrBundleIfIndexMappingIndex_Object=MibTableColumn
mfrBundleIfIndexMappingIndex=_MfrBundleIfIndexMappingIndex_Object((1,3,6,1,2,1,10,47,2,4,1,2),_MfrBundleIfIndexMappingIndex_Type())
mfrBundleIfIndexMappingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleIfIndexMappingIndex.setStatus(_A)
_MfrMibBundleLinkObjects_ObjectIdentity=ObjectIdentity
mfrMibBundleLinkObjects=_MfrMibBundleLinkObjects_ObjectIdentity((1,3,6,1,2,1,10,47,3))
_MfrBundleLinkTable_Object=MibTable
mfrBundleLinkTable=_MfrBundleLinkTable_Object((1,3,6,1,2,1,10,47,3,1))
if mibBuilder.loadTexts:mfrBundleLinkTable.setStatus(_A)
_MfrBundleLinkEntry_Object=MibTableRow
mfrBundleLinkEntry=_MfrBundleLinkEntry_Object((1,3,6,1,2,1,10,47,3,1,1))
mfrBundleLinkEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mfrBundleLinkEntry.setStatus(_A)
_MfrBundleLinkRowStatus_Type=RowStatus
_MfrBundleLinkRowStatus_Object=MibTableColumn
mfrBundleLinkRowStatus=_MfrBundleLinkRowStatus_Object((1,3,6,1,2,1,10,47,3,1,1,1),_MfrBundleLinkRowStatus_Type())
mfrBundleLinkRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleLinkRowStatus.setStatus(_A)
class _MfrBundleLinkConfigBundleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MfrBundleLinkConfigBundleIndex_Type.__name__=_D
_MfrBundleLinkConfigBundleIndex_Object=MibTableColumn
mfrBundleLinkConfigBundleIndex=_MfrBundleLinkConfigBundleIndex_Object((1,3,6,1,2,1,10,47,3,1,1,2),_MfrBundleLinkConfigBundleIndex_Type())
mfrBundleLinkConfigBundleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleLinkConfigBundleIndex.setStatus(_A)
_MfrBundleLinkNearEndName_Type=SnmpAdminString
_MfrBundleLinkNearEndName_Object=MibTableColumn
mfrBundleLinkNearEndName=_MfrBundleLinkNearEndName_Object((1,3,6,1,2,1,10,47,3,1,1,3),_MfrBundleLinkNearEndName_Type())
mfrBundleLinkNearEndName.setMaxAccess(_E)
if mibBuilder.loadTexts:mfrBundleLinkNearEndName.setStatus(_A)
_MfrBundleLinkState_Type=MfrBundleLinkState
_MfrBundleLinkState_Object=MibTableColumn
mfrBundleLinkState=_MfrBundleLinkState_Object((1,3,6,1,2,1,10,47,3,1,1,4),_MfrBundleLinkState_Type())
mfrBundleLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkState.setStatus(_A)
_MfrBundleLinkFarEndName_Type=SnmpAdminString
_MfrBundleLinkFarEndName_Object=MibTableColumn
mfrBundleLinkFarEndName=_MfrBundleLinkFarEndName_Object((1,3,6,1,2,1,10,47,3,1,1,5),_MfrBundleLinkFarEndName_Type())
mfrBundleLinkFarEndName.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkFarEndName.setStatus(_A)
_MfrBundleLinkFarEndBundleName_Type=SnmpAdminString
_MfrBundleLinkFarEndBundleName_Object=MibTableColumn
mfrBundleLinkFarEndBundleName=_MfrBundleLinkFarEndBundleName_Object((1,3,6,1,2,1,10,47,3,1,1,6),_MfrBundleLinkFarEndBundleName_Type())
mfrBundleLinkFarEndBundleName.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkFarEndBundleName.setStatus(_A)
class _MfrBundleLinkDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MfrBundleLinkDelay_Type.__name__=_D
_MfrBundleLinkDelay_Object=MibTableColumn
mfrBundleLinkDelay=_MfrBundleLinkDelay_Object((1,3,6,1,2,1,10,47,3,1,1,7),_MfrBundleLinkDelay_Type())
mfrBundleLinkDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkDelay.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkDelay.setUnits(_Q)
_MfrBundleLinkFramesControlTx_Type=Counter32
_MfrBundleLinkFramesControlTx_Object=MibTableColumn
mfrBundleLinkFramesControlTx=_MfrBundleLinkFramesControlTx_Object((1,3,6,1,2,1,10,47,3,1,1,8),_MfrBundleLinkFramesControlTx_Type())
mfrBundleLinkFramesControlTx.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkFramesControlTx.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkFramesControlTx.setUnits(_G)
_MfrBundleLinkFramesControlRx_Type=Counter32
_MfrBundleLinkFramesControlRx_Object=MibTableColumn
mfrBundleLinkFramesControlRx=_MfrBundleLinkFramesControlRx_Object((1,3,6,1,2,1,10,47,3,1,1,9),_MfrBundleLinkFramesControlRx_Type())
mfrBundleLinkFramesControlRx.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkFramesControlRx.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkFramesControlRx.setUnits(_G)
_MfrBundleLinkFramesControlInvalid_Type=Counter32
_MfrBundleLinkFramesControlInvalid_Object=MibTableColumn
mfrBundleLinkFramesControlInvalid=_MfrBundleLinkFramesControlInvalid_Object((1,3,6,1,2,1,10,47,3,1,1,10),_MfrBundleLinkFramesControlInvalid_Type())
mfrBundleLinkFramesControlInvalid.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkFramesControlInvalid.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkFramesControlInvalid.setUnits(_G)
_MfrBundleLinkTimerExpiredCount_Type=Counter32
_MfrBundleLinkTimerExpiredCount_Object=MibTableColumn
mfrBundleLinkTimerExpiredCount=_MfrBundleLinkTimerExpiredCount_Object((1,3,6,1,2,1,10,47,3,1,1,11),_MfrBundleLinkTimerExpiredCount_Type())
mfrBundleLinkTimerExpiredCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkTimerExpiredCount.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkTimerExpiredCount.setUnits('Timer Expiration Events')
_MfrBundleLinkLoopbackSuspected_Type=Counter32
_MfrBundleLinkLoopbackSuspected_Object=MibTableColumn
mfrBundleLinkLoopbackSuspected=_MfrBundleLinkLoopbackSuspected_Object((1,3,6,1,2,1,10,47,3,1,1,12),_MfrBundleLinkLoopbackSuspected_Type())
mfrBundleLinkLoopbackSuspected.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkLoopbackSuspected.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkLoopbackSuspected.setUnits('Loopback Suspected Events')
_MfrBundleLinkUnexpectedSequence_Type=Counter32
_MfrBundleLinkUnexpectedSequence_Object=MibTableColumn
mfrBundleLinkUnexpectedSequence=_MfrBundleLinkUnexpectedSequence_Object((1,3,6,1,2,1,10,47,3,1,1,13),_MfrBundleLinkUnexpectedSequence_Type())
mfrBundleLinkUnexpectedSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkUnexpectedSequence.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkUnexpectedSequence.setUnits(_G)
_MfrBundleLinkMismatch_Type=Counter32
_MfrBundleLinkMismatch_Object=MibTableColumn
mfrBundleLinkMismatch=_MfrBundleLinkMismatch_Object((1,3,6,1,2,1,10,47,3,1,1,14),_MfrBundleLinkMismatch_Type())
mfrBundleLinkMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:mfrBundleLinkMismatch.setStatus(_A)
if mibBuilder.loadTexts:mfrBundleLinkMismatch.setUnits('Bundle Name Mismatch Events')
_MfrMibTraps_ObjectIdentity=ObjectIdentity
mfrMibTraps=_MfrMibTraps_ObjectIdentity((1,3,6,1,2,1,10,47,4))
_MfrMibTrapsPrefix_ObjectIdentity=ObjectIdentity
mfrMibTrapsPrefix=_MfrMibTrapsPrefix_ObjectIdentity((1,3,6,1,2,1,10,47,4,0))
_MfrMibConformance_ObjectIdentity=ObjectIdentity
mfrMibConformance=_MfrMibConformance_ObjectIdentity((1,3,6,1,2,1,10,47,5))
_MfrMibGroups_ObjectIdentity=ObjectIdentity
mfrMibGroups=_MfrMibGroups_ObjectIdentity((1,3,6,1,2,1,10,47,5,1))
_MfrMibCompliances_ObjectIdentity=ObjectIdentity
mfrMibCompliances=_MfrMibCompliances_ObjectIdentity((1,3,6,1,2,1,10,47,5,2))
mfrMibBundleGroup=ObjectGroup((1,3,6,1,2,1,10,47,5,1,1))
mfrMibBundleGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_J),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_K),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:mfrMibBundleGroup.setStatus(_A)
mfrMibBundleLinkGroup=ObjectGroup((1,3,6,1,2,1,10,47,5,1,2))
mfrMibBundleLinkGroup.setObjects(*((_B,_k),(_B,_l),(_B,_L),(_B,_m),(_B,_M),(_B,_N),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:mfrMibBundleLinkGroup.setStatus(_A)
mfrMibTrapBundleLinkMismatch=NotificationType((1,3,6,1,2,1,10,47,4,0,1))
mfrMibTrapBundleLinkMismatch.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mfrMibTrapBundleLinkMismatch.setStatus(_A)
mfrMibTrapGroup=NotificationGroup((1,3,6,1,2,1,10,47,5,1,3))
mfrMibTrapGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:mfrMibTrapGroup.setStatus(_A)
mfrMibCompliance=ModuleCompliance((1,3,6,1,2,1,10,47,5,2,1))
mfrMibCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:mfrMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MfrBundleLinkState':MfrBundleLinkState,'mfrMib':mfrMib,'mfrMibScalarObjects':mfrMibScalarObjects,_R:mfrBundleMaxNumBundles,_S:mfrBundleNextIndex,'mfrMibBundleObjects':mfrMibBundleObjects,'mfrBundleTable':mfrBundleTable,'mfrBundleEntry':mfrBundleEntry,_O:mfrBundleIndex,_T:mfrBundleIfIndex,_U:mfrBundleRowStatus,_J:mfrBundleNearEndName,_V:mfrBundleFragmentation,_W:mfrBundleMaxFragSize,_X:mfrBundleTimerHello,_Y:mfrBundleTimerAck,_Z:mfrBundleCountMaxRetry,_a:mfrBundleActivationClass,_b:mfrBundleThreshold,_c:mfrBundleMaxDiffDelay,_h:mfrBundleSeqNumSize,_d:mfrBundleMaxBundleLinks,_e:mfrBundleLinksConfigured,_f:mfrBundleLinksActive,_g:mfrBundleBandwidth,_K:mfrBundleFarEndName,_i:mfrBundleResequencingErrors,'mfrBundleIfIndexMappingTable':mfrBundleIfIndexMappingTable,'mfrBundleIfIndexMappingEntry':mfrBundleIfIndexMappingEntry,_j:mfrBundleIfIndexMappingIndex,'mfrMibBundleLinkObjects':mfrMibBundleLinkObjects,'mfrBundleLinkTable':mfrBundleLinkTable,'mfrBundleLinkEntry':mfrBundleLinkEntry,_k:mfrBundleLinkRowStatus,_l:mfrBundleLinkConfigBundleIndex,_L:mfrBundleLinkNearEndName,_m:mfrBundleLinkState,_M:mfrBundleLinkFarEndName,_N:mfrBundleLinkFarEndBundleName,_n:mfrBundleLinkDelay,_o:mfrBundleLinkFramesControlTx,_p:mfrBundleLinkFramesControlRx,_q:mfrBundleLinkFramesControlInvalid,_r:mfrBundleLinkTimerExpiredCount,_s:mfrBundleLinkLoopbackSuspected,_t:mfrBundleLinkUnexpectedSequence,_u:mfrBundleLinkMismatch,'mfrMibTraps':mfrMibTraps,'mfrMibTrapsPrefix':mfrMibTrapsPrefix,_v:mfrMibTrapBundleLinkMismatch,'mfrMibConformance':mfrMibConformance,'mfrMibGroups':mfrMibGroups,_w:mfrMibBundleGroup,_x:mfrMibBundleLinkGroup,_y:mfrMibTrapGroup,'mfrMibCompliances':mfrMibCompliances,'mfrMibCompliance':mfrMibCompliance})