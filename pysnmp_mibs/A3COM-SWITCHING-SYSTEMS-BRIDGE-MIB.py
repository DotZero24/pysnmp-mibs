_d='a3ComSysBridgePortLoopDetectState'
_c='a3ComSysBridgePortRateLimitReceiveState'
_b='a3ComSysBridgePortAddressState'
_a='a3ComSysBridgeVlanPortAddressIndex'
_Z='a3ComSysBridgeVlanPortAddressPortIndex'
_Y='a3ComSysBridgeVlanPortAddressVlanIndex'
_X='a3ComSysBridgeVlanPortAddressBridgeIndex'
_W='obsolete'
_V='isDynamic'
_U='isStatic'
_T='invalid'
_S='a3ComSysBridgePortAddressIndex'
_R='a3ComSysBridgePortAddressPortIndex'
_Q='a3ComSysBridgePortAddressBridgeIndex'
_P='active'
_O='a3ComSysBridgePortBridgeIndex'
_N='NotificationType'
_M='notSupported'
_L='a3ComSysBridgeIndex'
_K='a3ComSysBridgePortIndex'
_J='disabled'
_I='enabled'
_H='false'
_G='true'
_F='OctetString'
_E='A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComSysBridge_ObjectIdentity=ObjectIdentity
a3ComSysBridge=_A3ComSysBridge_ObjectIdentity((1,3,6,1,4,1,43,29,4,10))
_A3ComSysBridgeCount_Type=Integer32
_A3ComSysBridgeCount_Object=MibScalar
a3ComSysBridgeCount=_A3ComSysBridgeCount_Object((1,3,6,1,4,1,43,29,4,10,1),_A3ComSysBridgeCount_Type())
a3ComSysBridgeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeCount.setStatus(_A)
_A3ComSysBridgeTable_Object=MibTable
a3ComSysBridgeTable=_A3ComSysBridgeTable_Object((1,3,6,1,4,1,43,29,4,10,2))
if mibBuilder.loadTexts:a3ComSysBridgeTable.setStatus(_A)
_A3ComSysBridgeEntry_Object=MibTableRow
a3ComSysBridgeEntry=_A3ComSysBridgeEntry_Object((1,3,6,1,4,1,43,29,4,10,2,1))
a3ComSysBridgeEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:a3ComSysBridgeEntry.setStatus(_A)
class _A3ComSysBridgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgeIndex_Type.__name__=_C
_A3ComSysBridgeIndex_Object=MibTableColumn
a3ComSysBridgeIndex=_A3ComSysBridgeIndex_Object((1,3,6,1,4,1,43,29,4,10,2,1,1),_A3ComSysBridgeIndex_Type())
a3ComSysBridgeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeIndex.setStatus(_A)
_A3ComSysBridgePortCount_Type=Integer32
_A3ComSysBridgePortCount_Object=MibTableColumn
a3ComSysBridgePortCount=_A3ComSysBridgePortCount_Object((1,3,6,1,4,1,43,29,4,10,2,1,2),_A3ComSysBridgePortCount_Type())
a3ComSysBridgePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortCount.setStatus(_A)
_A3ComSysBridgeAddressTableSize_Type=Integer32
_A3ComSysBridgeAddressTableSize_Object=MibTableColumn
a3ComSysBridgeAddressTableSize=_A3ComSysBridgeAddressTableSize_Object((1,3,6,1,4,1,43,29,4,10,2,1,3),_A3ComSysBridgeAddressTableSize_Type())
a3ComSysBridgeAddressTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeAddressTableSize.setStatus(_A)
_A3ComSysBridgeAddressTableCount_Type=Integer32
_A3ComSysBridgeAddressTableCount_Object=MibTableColumn
a3ComSysBridgeAddressTableCount=_A3ComSysBridgeAddressTableCount_Object((1,3,6,1,4,1,43,29,4,10,2,1,4),_A3ComSysBridgeAddressTableCount_Type())
a3ComSysBridgeAddressTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeAddressTableCount.setStatus(_A)
_A3ComSysBridgeAddressTablePeakCount_Type=Integer32
_A3ComSysBridgeAddressTablePeakCount_Object=MibTableColumn
a3ComSysBridgeAddressTablePeakCount=_A3ComSysBridgeAddressTablePeakCount_Object((1,3,6,1,4,1,43,29,4,10,2,1,5),_A3ComSysBridgeAddressTablePeakCount_Type())
a3ComSysBridgeAddressTablePeakCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeAddressTablePeakCount.setStatus(_A)
_A3ComSysBridgeAddressThreshold_Type=Integer32
_A3ComSysBridgeAddressThreshold_Object=MibTableColumn
a3ComSysBridgeAddressThreshold=_A3ComSysBridgeAddressThreshold_Object((1,3,6,1,4,1,43,29,4,10,2,1,6),_A3ComSysBridgeAddressThreshold_Type())
a3ComSysBridgeAddressThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeAddressThreshold.setStatus(_A)
class _A3ComSysBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('expressMode',1),('ieee8021dBridgeMode',2),(_M,3),('ieee8021dSRTBridgeMode',4),('ieee8021dSRBridgeMode',5),('ibmSRBridgeMode',6),('srtBBridgeMode',7),('srExpressBridgeMode',8)))
_A3ComSysBridgeMode_Type.__name__=_C
_A3ComSysBridgeMode_Object=MibTableColumn
a3ComSysBridgeMode=_A3ComSysBridgeMode_Object((1,3,6,1,4,1,43,29,4,10,2,1,7),_A3ComSysBridgeMode_Type())
a3ComSysBridgeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeMode.setStatus(_A)
_A3ComSysBridgeBackbonePort_Type=Integer32
_A3ComSysBridgeBackbonePort_Object=MibTableColumn
a3ComSysBridgeBackbonePort=_A3ComSysBridgeBackbonePort_Object((1,3,6,1,4,1,43,29,4,10,2,1,8),_A3ComSysBridgeBackbonePort_Type())
a3ComSysBridgeBackbonePort.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeBackbonePort.setStatus(_A)
class _A3ComSysBridgeIpFragmentationEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,3)))
_A3ComSysBridgeIpFragmentationEnabled_Type.__name__=_C
_A3ComSysBridgeIpFragmentationEnabled_Object=MibTableColumn
a3ComSysBridgeIpFragmentationEnabled=_A3ComSysBridgeIpFragmentationEnabled_Object((1,3,6,1,4,1,43,29,4,10,2,1,9),_A3ComSysBridgeIpFragmentationEnabled_Type())
a3ComSysBridgeIpFragmentationEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeIpFragmentationEnabled.setStatus(_A)
class _A3ComSysBridgeTrFddiTranslationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('native',1),('backbone',2)))
_A3ComSysBridgeTrFddiTranslationMode_Type.__name__=_C
_A3ComSysBridgeTrFddiTranslationMode_Object=MibTableColumn
a3ComSysBridgeTrFddiTranslationMode=_A3ComSysBridgeTrFddiTranslationMode_Object((1,3,6,1,4,1,43,29,4,10,2,1,10),_A3ComSysBridgeTrFddiTranslationMode_Type())
a3ComSysBridgeTrFddiTranslationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeTrFddiTranslationMode.setStatus(_A)
class _A3ComSysBridgeSTPGroupAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_A3ComSysBridgeSTPGroupAddress_Type.__name__=_F
_A3ComSysBridgeSTPGroupAddress_Object=MibTableColumn
a3ComSysBridgeSTPGroupAddress=_A3ComSysBridgeSTPGroupAddress_Object((1,3,6,1,4,1,43,29,4,10,2,1,11),_A3ComSysBridgeSTPGroupAddress_Type())
a3ComSysBridgeSTPGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeSTPGroupAddress.setStatus(_A)
class _A3ComSysBridgeSTPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_A3ComSysBridgeSTPEnable_Type.__name__=_C
_A3ComSysBridgeSTPEnable_Object=MibTableColumn
a3ComSysBridgeSTPEnable=_A3ComSysBridgeSTPEnable_Object((1,3,6,1,4,1,43,29,4,10,2,1,12),_A3ComSysBridgeSTPEnable_Type())
a3ComSysBridgeSTPEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeSTPEnable.setStatus(_A)
class _A3ComSysBridgeIpxSnapTranslationEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_A3ComSysBridgeIpxSnapTranslationEnable_Type.__name__=_C
_A3ComSysBridgeIpxSnapTranslationEnable_Object=MibTableColumn
a3ComSysBridgeIpxSnapTranslationEnable=_A3ComSysBridgeIpxSnapTranslationEnable_Object((1,3,6,1,4,1,43,29,4,10,2,1,13),_A3ComSysBridgeIpxSnapTranslationEnable_Type())
a3ComSysBridgeIpxSnapTranslationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeIpxSnapTranslationEnable.setStatus(_A)
class _A3ComSysBridgeLowLatencyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_A3ComSysBridgeLowLatencyEnable_Type.__name__=_C
_A3ComSysBridgeLowLatencyEnable_Object=MibTableColumn
a3ComSysBridgeLowLatencyEnable=_A3ComSysBridgeLowLatencyEnable_Object((1,3,6,1,4,1,43,29,4,10,2,1,14),_A3ComSysBridgeLowLatencyEnable_Type())
a3ComSysBridgeLowLatencyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeLowLatencyEnable.setStatus(_A)
class _A3ComSysBridgeVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('open',1),('closed',2),('mixed',3),(_M,4)))
_A3ComSysBridgeVlanMode_Type.__name__=_C
_A3ComSysBridgeVlanMode_Object=MibTableColumn
a3ComSysBridgeVlanMode=_A3ComSysBridgeVlanMode_Object((1,3,6,1,4,1,43,29,4,10,2,1,15),_A3ComSysBridgeVlanMode_Type())
a3ComSysBridgeVlanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeVlanMode.setStatus(_A)
class _A3ComSysBridgeRateLimitReceiveMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgeRateLimitReceiveMulticast_Type.__name__=_C
_A3ComSysBridgeRateLimitReceiveMulticast_Object=MibTableColumn
a3ComSysBridgeRateLimitReceiveMulticast=_A3ComSysBridgeRateLimitReceiveMulticast_Object((1,3,6,1,4,1,43,29,4,10,2,1,16),_A3ComSysBridgeRateLimitReceiveMulticast_Type())
a3ComSysBridgeRateLimitReceiveMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeRateLimitReceiveMulticast.setStatus(_A)
class _A3ComSysBridgeRateLimitReceiveBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgeRateLimitReceiveBroadcast_Type.__name__=_C
_A3ComSysBridgeRateLimitReceiveBroadcast_Object=MibTableColumn
a3ComSysBridgeRateLimitReceiveBroadcast=_A3ComSysBridgeRateLimitReceiveBroadcast_Object((1,3,6,1,4,1,43,29,4,10,2,1,17),_A3ComSysBridgeRateLimitReceiveBroadcast_Type())
a3ComSysBridgeRateLimitReceiveBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeRateLimitReceiveBroadcast.setStatus(_A)
class _A3ComSysBridgeRateLimitReceiveFlood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgeRateLimitReceiveFlood_Type.__name__=_C
_A3ComSysBridgeRateLimitReceiveFlood_Object=MibTableColumn
a3ComSysBridgeRateLimitReceiveFlood=_A3ComSysBridgeRateLimitReceiveFlood_Object((1,3,6,1,4,1,43,29,4,10,2,1,18),_A3ComSysBridgeRateLimitReceiveFlood_Type())
a3ComSysBridgeRateLimitReceiveFlood.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeRateLimitReceiveFlood.setStatus(_A)
class _A3ComSysBridgeAddressLearnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('secure',2)))
_A3ComSysBridgeAddressLearnMode_Type.__name__=_C
_A3ComSysBridgeAddressLearnMode_Object=MibTableColumn
a3ComSysBridgeAddressLearnMode=_A3ComSysBridgeAddressLearnMode_Object((1,3,6,1,4,1,43,29,4,10,2,1,19),_A3ComSysBridgeAddressLearnMode_Type())
a3ComSysBridgeAddressLearnMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeAddressLearnMode.setStatus(_A)
class _A3ComSysBridgeAddressAgingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgeAddressAgingInterval_Type.__name__=_C
_A3ComSysBridgeAddressAgingInterval_Object=MibTableColumn
a3ComSysBridgeAddressAgingInterval=_A3ComSysBridgeAddressAgingInterval_Object((1,3,6,1,4,1,43,29,4,10,2,1,20),_A3ComSysBridgeAddressAgingInterval_Type())
a3ComSysBridgeAddressAgingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeAddressAgingInterval.setStatus(_A)
class _A3ComSysBridgeLoopDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('immediate',3)))
_A3ComSysBridgeLoopDetectMode_Type.__name__=_C
_A3ComSysBridgeLoopDetectMode_Object=MibTableColumn
a3ComSysBridgeLoopDetectMode=_A3ComSysBridgeLoopDetectMode_Object((1,3,6,1,4,1,43,29,4,10,2,1,21),_A3ComSysBridgeLoopDetectMode_Type())
a3ComSysBridgeLoopDetectMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeLoopDetectMode.setStatus(_A)
_A3ComSysBridgeLoopDetectSrcAddress_Type=OctetString
_A3ComSysBridgeLoopDetectSrcAddress_Object=MibTableColumn
a3ComSysBridgeLoopDetectSrcAddress=_A3ComSysBridgeLoopDetectSrcAddress_Object((1,3,6,1,4,1,43,29,4,10,2,1,22),_A3ComSysBridgeLoopDetectSrcAddress_Type())
a3ComSysBridgeLoopDetectSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeLoopDetectSrcAddress.setStatus(_A)
_A3ComSysBridgePortTable_Object=MibTable
a3ComSysBridgePortTable=_A3ComSysBridgePortTable_Object((1,3,6,1,4,1,43,29,4,10,3))
if mibBuilder.loadTexts:a3ComSysBridgePortTable.setStatus(_A)
_A3ComSysBridgePortEntry_Object=MibTableRow
a3ComSysBridgePortEntry=_A3ComSysBridgePortEntry_Object((1,3,6,1,4,1,43,29,4,10,3,1))
a3ComSysBridgePortEntry.setIndexNames((0,_E,_O),(0,_E,_K))
if mibBuilder.loadTexts:a3ComSysBridgePortEntry.setStatus(_A)
class _A3ComSysBridgePortBridgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgePortBridgeIndex_Type.__name__=_C
_A3ComSysBridgePortBridgeIndex_Object=MibTableColumn
a3ComSysBridgePortBridgeIndex=_A3ComSysBridgePortBridgeIndex_Object((1,3,6,1,4,1,43,29,4,10,3,1,1),_A3ComSysBridgePortBridgeIndex_Type())
a3ComSysBridgePortBridgeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortBridgeIndex.setStatus(_A)
class _A3ComSysBridgePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgePortIndex_Type.__name__=_C
_A3ComSysBridgePortIndex_Object=MibTableColumn
a3ComSysBridgePortIndex=_A3ComSysBridgePortIndex_Object((1,3,6,1,4,1,43,29,4,10,3,1,2),_A3ComSysBridgePortIndex_Type())
a3ComSysBridgePortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortIndex.setStatus(_A)
class _A3ComSysBridgePortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgePortIfIndex_Type.__name__=_C
_A3ComSysBridgePortIfIndex_Object=MibTableColumn
a3ComSysBridgePortIfIndex=_A3ComSysBridgePortIfIndex_Object((1,3,6,1,4,1,43,29,4,10,3,1,3),_A3ComSysBridgePortIfIndex_Type())
a3ComSysBridgePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortIfIndex.setStatus(_A)
class _A3ComSysBridgePortReceiveMulticastLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000))
_A3ComSysBridgePortReceiveMulticastLimit_Type.__name__=_C
_A3ComSysBridgePortReceiveMulticastLimit_Object=MibTableColumn
a3ComSysBridgePortReceiveMulticastLimit=_A3ComSysBridgePortReceiveMulticastLimit_Object((1,3,6,1,4,1,43,29,4,10,3,1,4),_A3ComSysBridgePortReceiveMulticastLimit_Type())
a3ComSysBridgePortReceiveMulticastLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveMulticastLimit.setStatus(_A)
class _A3ComSysBridgePortAddressAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('freezeAddress',2),('flushAddress',3),('flushDynamicAddress',4)))
_A3ComSysBridgePortAddressAction_Type.__name__=_C
_A3ComSysBridgePortAddressAction_Object=MibTableColumn
a3ComSysBridgePortAddressAction=_A3ComSysBridgePortAddressAction_Object((1,3,6,1,4,1,43,29,4,10,3,1,5),_A3ComSysBridgePortAddressAction_Type())
a3ComSysBridgePortAddressAction.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressAction.setStatus(_A)
_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Type=Counter32
_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Object=MibTableColumn
a3ComSysBridgePortSpanningTreeFrameReceivedCounts=_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Object((1,3,6,1,4,1,43,29,4,10,3,1,6),_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Type())
a3ComSysBridgePortSpanningTreeFrameReceivedCounts.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortSpanningTreeFrameReceivedCounts.setStatus(_A)
_A3ComSysBridgePortReceiveBlockedDiscards_Type=Counter32
_A3ComSysBridgePortReceiveBlockedDiscards_Object=MibTableColumn
a3ComSysBridgePortReceiveBlockedDiscards=_A3ComSysBridgePortReceiveBlockedDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,7),_A3ComSysBridgePortReceiveBlockedDiscards_Type())
a3ComSysBridgePortReceiveBlockedDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveBlockedDiscards.setStatus(_A)
_A3ComSysBridgePortReceiveMulticastLimitExceededs_Type=Counter32
_A3ComSysBridgePortReceiveMulticastLimitExceededs_Object=MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitExceededs=_A3ComSysBridgePortReceiveMulticastLimitExceededs_Object((1,3,6,1,4,1,43,29,4,10,3,1,8),_A3ComSysBridgePortReceiveMulticastLimitExceededs_Type())
a3ComSysBridgePortReceiveMulticastLimitExceededs.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveMulticastLimitExceededs.setStatus(_A)
_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Type=Counter32
_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Object=MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitExceededDiscards=_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,9),_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Type())
a3ComSysBridgePortReceiveMulticastLimitExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveMulticastLimitExceededDiscards.setStatus(_A)
_A3ComSysBridgePortReceiveSecurityDiscards_Type=Counter32
_A3ComSysBridgePortReceiveSecurityDiscards_Object=MibTableColumn
a3ComSysBridgePortReceiveSecurityDiscards=_A3ComSysBridgePortReceiveSecurityDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,10),_A3ComSysBridgePortReceiveSecurityDiscards_Type())
a3ComSysBridgePortReceiveSecurityDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveSecurityDiscards.setStatus(_A)
_A3ComSysBridgePortReceiveUnknownDiscards_Type=Counter32
_A3ComSysBridgePortReceiveUnknownDiscards_Object=MibTableColumn
a3ComSysBridgePortReceiveUnknownDiscards=_A3ComSysBridgePortReceiveUnknownDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,11),_A3ComSysBridgePortReceiveUnknownDiscards_Type())
a3ComSysBridgePortReceiveUnknownDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveUnknownDiscards.setStatus(_A)
_A3ComSysBridgePortReceiveOtherDiscards_Type=Counter32
_A3ComSysBridgePortReceiveOtherDiscards_Object=MibTableColumn
a3ComSysBridgePortReceiveOtherDiscards=_A3ComSysBridgePortReceiveOtherDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,12),_A3ComSysBridgePortReceiveOtherDiscards_Type())
a3ComSysBridgePortReceiveOtherDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveOtherDiscards.setStatus(_A)
_A3ComSysBridgePortReceiveErrorDiscards_Type=Counter32
_A3ComSysBridgePortReceiveErrorDiscards_Object=MibTableColumn
a3ComSysBridgePortReceiveErrorDiscards=_A3ComSysBridgePortReceiveErrorDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,13),_A3ComSysBridgePortReceiveErrorDiscards_Type())
a3ComSysBridgePortReceiveErrorDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveErrorDiscards.setStatus(_A)
_A3ComSysBridgePortSameSegmentDiscards_Type=Counter32
_A3ComSysBridgePortSameSegmentDiscards_Object=MibTableColumn
a3ComSysBridgePortSameSegmentDiscards=_A3ComSysBridgePortSameSegmentDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,14),_A3ComSysBridgePortSameSegmentDiscards_Type())
a3ComSysBridgePortSameSegmentDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortSameSegmentDiscards.setStatus(_A)
_A3ComSysBridgePortTransmitBlockedDiscards_Type=Counter32
_A3ComSysBridgePortTransmitBlockedDiscards_Object=MibTableColumn
a3ComSysBridgePortTransmitBlockedDiscards=_A3ComSysBridgePortTransmitBlockedDiscards_Object((1,3,6,1,4,1,43,29,4,10,3,1,15),_A3ComSysBridgePortTransmitBlockedDiscards_Type())
a3ComSysBridgePortTransmitBlockedDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortTransmitBlockedDiscards.setStatus(_A)
_A3ComSysBridgePortReceiveAllPathFilteredFrames_Type=Counter32
_A3ComSysBridgePortReceiveAllPathFilteredFrames_Object=MibTableColumn
a3ComSysBridgePortReceiveAllPathFilteredFrames=_A3ComSysBridgePortReceiveAllPathFilteredFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,16),_A3ComSysBridgePortReceiveAllPathFilteredFrames_Type())
a3ComSysBridgePortReceiveAllPathFilteredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveAllPathFilteredFrames.setStatus(_A)
_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Type=Counter32
_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Object=MibTableColumn
a3ComSysBridgePortReceiveMulticastPathFilteredFrames=_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,17),_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Type())
a3ComSysBridgePortReceiveMulticastPathFilteredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveMulticastPathFilteredFrames.setStatus(_A)
_A3ComSysBridgePortTransmitAllPathFilteredFrames_Type=Counter32
_A3ComSysBridgePortTransmitAllPathFilteredFrames_Object=MibTableColumn
a3ComSysBridgePortTransmitAllPathFilteredFrames=_A3ComSysBridgePortTransmitAllPathFilteredFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,18),_A3ComSysBridgePortTransmitAllPathFilteredFrames_Type())
a3ComSysBridgePortTransmitAllPathFilteredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortTransmitAllPathFilteredFrames.setStatus(_A)
_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Type=Counter32
_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Object=MibTableColumn
a3ComSysBridgePortTransmitMulticastPathFilteredFrames=_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,19),_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Type())
a3ComSysBridgePortTransmitMulticastPathFilteredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortTransmitMulticastPathFilteredFrames.setStatus(_A)
_A3ComSysBridgePortForwardedUnicastFrames_Type=Counter32
_A3ComSysBridgePortForwardedUnicastFrames_Object=MibTableColumn
a3ComSysBridgePortForwardedUnicastFrames=_A3ComSysBridgePortForwardedUnicastFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,20),_A3ComSysBridgePortForwardedUnicastFrames_Type())
a3ComSysBridgePortForwardedUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortForwardedUnicastFrames.setStatus(_A)
_A3ComSysBridgePortForwardedUnicastOctets_Type=Counter32
_A3ComSysBridgePortForwardedUnicastOctets_Object=MibTableColumn
a3ComSysBridgePortForwardedUnicastOctets=_A3ComSysBridgePortForwardedUnicastOctets_Object((1,3,6,1,4,1,43,29,4,10,3,1,21),_A3ComSysBridgePortForwardedUnicastOctets_Type())
a3ComSysBridgePortForwardedUnicastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortForwardedUnicastOctets.setStatus(_A)
_A3ComSysBridgePortForwardedMulticastFrames_Type=Counter32
_A3ComSysBridgePortForwardedMulticastFrames_Object=MibTableColumn
a3ComSysBridgePortForwardedMulticastFrames=_A3ComSysBridgePortForwardedMulticastFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,22),_A3ComSysBridgePortForwardedMulticastFrames_Type())
a3ComSysBridgePortForwardedMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortForwardedMulticastFrames.setStatus(_A)
_A3ComSysBridgePortForwardedMulticastOctets_Type=Counter32
_A3ComSysBridgePortForwardedMulticastOctets_Object=MibTableColumn
a3ComSysBridgePortForwardedMulticastOctets=_A3ComSysBridgePortForwardedMulticastOctets_Object((1,3,6,1,4,1,43,29,4,10,3,1,23),_A3ComSysBridgePortForwardedMulticastOctets_Type())
a3ComSysBridgePortForwardedMulticastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortForwardedMulticastOctets.setStatus(_A)
_A3ComSysBridgePortFloodedUnicastFrames_Type=Counter32
_A3ComSysBridgePortFloodedUnicastFrames_Object=MibTableColumn
a3ComSysBridgePortFloodedUnicastFrames=_A3ComSysBridgePortFloodedUnicastFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,24),_A3ComSysBridgePortFloodedUnicastFrames_Type())
a3ComSysBridgePortFloodedUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortFloodedUnicastFrames.setStatus(_A)
_A3ComSysBridgePortFloodedUnicastOctets_Type=Counter32
_A3ComSysBridgePortFloodedUnicastOctets_Object=MibTableColumn
a3ComSysBridgePortFloodedUnicastOctets=_A3ComSysBridgePortFloodedUnicastOctets_Object((1,3,6,1,4,1,43,29,4,10,3,1,25),_A3ComSysBridgePortFloodedUnicastOctets_Type())
a3ComSysBridgePortFloodedUnicastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortFloodedUnicastOctets.setStatus(_A)
class _A3ComSysBridgePortStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),('remove',3)))
_A3ComSysBridgePortStpMode_Type.__name__=_C
_A3ComSysBridgePortStpMode_Object=MibTableColumn
a3ComSysBridgePortStpMode=_A3ComSysBridgePortStpMode_Object((1,3,6,1,4,1,43,29,4,10,3,1,26),_A3ComSysBridgePortStpMode_Type())
a3ComSysBridgePortStpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortStpMode.setStatus(_A)
class _A3ComSysBridgePortReceiveMulticastLimitFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('broadcastAndMulticast',1),('broadcastOnly',2)))
_A3ComSysBridgePortReceiveMulticastLimitFrameType_Type.__name__=_C
_A3ComSysBridgePortReceiveMulticastLimitFrameType_Object=MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitFrameType=_A3ComSysBridgePortReceiveMulticastLimitFrameType_Object((1,3,6,1,4,1,43,29,4,10,3,1,27),_A3ComSysBridgePortReceiveMulticastLimitFrameType_Type())
a3ComSysBridgePortReceiveMulticastLimitFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveMulticastLimitFrameType.setStatus(_A)
_A3ComSysBridgePortForwardedFrames_Type=Counter32
_A3ComSysBridgePortForwardedFrames_Object=MibTableColumn
a3ComSysBridgePortForwardedFrames=_A3ComSysBridgePortForwardedFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,28),_A3ComSysBridgePortForwardedFrames_Type())
a3ComSysBridgePortForwardedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortForwardedFrames.setStatus(_A)
_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Type=Integer32
_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Object=MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitMultiplier=_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Object((1,3,6,1,4,1,43,29,4,10,3,1,29),_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Type())
a3ComSysBridgePortReceiveMulticastLimitMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveMulticastLimitMultiplier.setStatus(_A)
class _A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Type.__name__=_C
_A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Object=MibTableColumn
a3ComSysBridgePortRateLimitReceiveMulticastEnabled=_A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Object((1,3,6,1,4,1,43,29,4,10,3,1,30),_A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Type())
a3ComSysBridgePortRateLimitReceiveMulticastEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortRateLimitReceiveMulticastEnabled.setStatus(_A)
class _A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Type.__name__=_C
_A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Object=MibTableColumn
a3ComSysBridgePortRateLimitReceiveBroadcastEnabled=_A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Object((1,3,6,1,4,1,43,29,4,10,3,1,31),_A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Type())
a3ComSysBridgePortRateLimitReceiveBroadcastEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortRateLimitReceiveBroadcastEnabled.setStatus(_A)
class _A3ComSysBridgePortRateLimitReceiveFloodEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_A3ComSysBridgePortRateLimitReceiveFloodEnabled_Type.__name__=_C
_A3ComSysBridgePortRateLimitReceiveFloodEnabled_Object=MibTableColumn
a3ComSysBridgePortRateLimitReceiveFloodEnabled=_A3ComSysBridgePortRateLimitReceiveFloodEnabled_Object((1,3,6,1,4,1,43,29,4,10,3,1,32),_A3ComSysBridgePortRateLimitReceiveFloodEnabled_Type())
a3ComSysBridgePortRateLimitReceiveFloodEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortRateLimitReceiveFloodEnabled.setStatus(_A)
class _A3ComSysBridgePortRateLimitReceiveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('bmfrl-disabled',3)))
_A3ComSysBridgePortRateLimitReceiveState_Type.__name__=_C
_A3ComSysBridgePortRateLimitReceiveState_Object=MibTableColumn
a3ComSysBridgePortRateLimitReceiveState=_A3ComSysBridgePortRateLimitReceiveState_Object((1,3,6,1,4,1,43,29,4,10,3,1,33),_A3ComSysBridgePortRateLimitReceiveState_Type())
a3ComSysBridgePortRateLimitReceiveState.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortRateLimitReceiveState.setStatus(_A)
class _A3ComSysBridgePortLoopDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('loopDetected',2),('bpduDetected',3)))
_A3ComSysBridgePortLoopDetectState_Type.__name__=_C
_A3ComSysBridgePortLoopDetectState_Object=MibTableColumn
a3ComSysBridgePortLoopDetectState=_A3ComSysBridgePortLoopDetectState_Object((1,3,6,1,4,1,43,29,4,10,3,1,34),_A3ComSysBridgePortLoopDetectState_Type())
a3ComSysBridgePortLoopDetectState.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortLoopDetectState.setStatus(_A)
class _A3ComSysBridgePortAddressMaxLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgePortAddressMaxLimit_Type.__name__=_C
_A3ComSysBridgePortAddressMaxLimit_Object=MibTableColumn
a3ComSysBridgePortAddressMaxLimit=_A3ComSysBridgePortAddressMaxLimit_Object((1,3,6,1,4,1,43,29,4,10,3,1,35),_A3ComSysBridgePortAddressMaxLimit_Type())
a3ComSysBridgePortAddressMaxLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressMaxLimit.setStatus(_A)
class _A3ComSysBridgePortAddressState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('limitationExceeded',2),('securityViolation',3)))
_A3ComSysBridgePortAddressState_Type.__name__=_C
_A3ComSysBridgePortAddressState_Object=MibTableColumn
a3ComSysBridgePortAddressState=_A3ComSysBridgePortAddressState_Object((1,3,6,1,4,1,43,29,4,10,3,1,36),_A3ComSysBridgePortAddressState_Type())
a3ComSysBridgePortAddressState.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressState.setStatus(_A)
_A3ComSysBridgePortReceiveInternalPathFilteredFrames_Type=Counter32
_A3ComSysBridgePortReceiveInternalPathFilteredFrames_Object=MibTableColumn
a3ComSysBridgePortReceiveInternalPathFilteredFrames=_A3ComSysBridgePortReceiveInternalPathFilteredFrames_Object((1,3,6,1,4,1,43,29,4,10,3,1,37),_A3ComSysBridgePortReceiveInternalPathFilteredFrames_Type())
a3ComSysBridgePortReceiveInternalPathFilteredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortReceiveInternalPathFilteredFrames.setStatus(_A)
_A3ComSysBridgePortAddressTable_Object=MibTable
a3ComSysBridgePortAddressTable=_A3ComSysBridgePortAddressTable_Object((1,3,6,1,4,1,43,29,4,10,5))
if mibBuilder.loadTexts:a3ComSysBridgePortAddressTable.setStatus(_A)
_A3ComSysBridgePortAddressEntry_Object=MibTableRow
a3ComSysBridgePortAddressEntry=_A3ComSysBridgePortAddressEntry_Object((1,3,6,1,4,1,43,29,4,10,5,1))
a3ComSysBridgePortAddressEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:a3ComSysBridgePortAddressEntry.setStatus(_A)
class _A3ComSysBridgePortAddressBridgeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgePortAddressBridgeIndex_Type.__name__=_C
_A3ComSysBridgePortAddressBridgeIndex_Object=MibTableColumn
a3ComSysBridgePortAddressBridgeIndex=_A3ComSysBridgePortAddressBridgeIndex_Object((1,3,6,1,4,1,43,29,4,10,5,1,1),_A3ComSysBridgePortAddressBridgeIndex_Type())
a3ComSysBridgePortAddressBridgeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressBridgeIndex.setStatus(_A)
class _A3ComSysBridgePortAddressPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgePortAddressPortIndex_Type.__name__=_C
_A3ComSysBridgePortAddressPortIndex_Object=MibTableColumn
a3ComSysBridgePortAddressPortIndex=_A3ComSysBridgePortAddressPortIndex_Object((1,3,6,1,4,1,43,29,4,10,5,1,2),_A3ComSysBridgePortAddressPortIndex_Type())
a3ComSysBridgePortAddressPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressPortIndex.setStatus(_A)
class _A3ComSysBridgePortAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComSysBridgePortAddressIndex_Type.__name__=_C
_A3ComSysBridgePortAddressIndex_Object=MibTableColumn
a3ComSysBridgePortAddressIndex=_A3ComSysBridgePortAddressIndex_Object((1,3,6,1,4,1,43,29,4,10,5,1,3),_A3ComSysBridgePortAddressIndex_Type())
a3ComSysBridgePortAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressIndex.setStatus(_A)
class _A3ComSysBridgePortAddressRemoteAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_A3ComSysBridgePortAddressRemoteAddress_Type.__name__=_F
_A3ComSysBridgePortAddressRemoteAddress_Object=MibTableColumn
a3ComSysBridgePortAddressRemoteAddress=_A3ComSysBridgePortAddressRemoteAddress_Object((1,3,6,1,4,1,43,29,4,10,5,1,4),_A3ComSysBridgePortAddressRemoteAddress_Type())
a3ComSysBridgePortAddressRemoteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressRemoteAddress.setStatus(_A)
class _A3ComSysBridgePortAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_T,2)))
_A3ComSysBridgePortAddressType_Type.__name__=_C
_A3ComSysBridgePortAddressType_Object=MibTableColumn
a3ComSysBridgePortAddressType=_A3ComSysBridgePortAddressType_Object((1,3,6,1,4,1,43,29,4,10,5,1,5),_A3ComSysBridgePortAddressType_Type())
a3ComSysBridgePortAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressType.setStatus(_A)
class _A3ComSysBridgePortAddressIsStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_A3ComSysBridgePortAddressIsStatic_Type.__name__=_C
_A3ComSysBridgePortAddressIsStatic_Object=MibTableColumn
a3ComSysBridgePortAddressIsStatic=_A3ComSysBridgePortAddressIsStatic_Object((1,3,6,1,4,1,43,29,4,10,5,1,6),_A3ComSysBridgePortAddressIsStatic_Type())
a3ComSysBridgePortAddressIsStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressIsStatic.setStatus(_A)
_A3ComSysBridgePortAddressStaticPort_Type=Integer32
_A3ComSysBridgePortAddressStaticPort_Object=MibTableColumn
a3ComSysBridgePortAddressStaticPort=_A3ComSysBridgePortAddressStaticPort_Object((1,3,6,1,4,1,43,29,4,10,5,1,7),_A3ComSysBridgePortAddressStaticPort_Type())
a3ComSysBridgePortAddressStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressStaticPort.setStatus(_A)
_A3ComSysBridgePortAddressAge_Type=Integer32
_A3ComSysBridgePortAddressAge_Object=MibTableColumn
a3ComSysBridgePortAddressAge=_A3ComSysBridgePortAddressAge_Object((1,3,6,1,4,1,43,29,4,10,5,1,8),_A3ComSysBridgePortAddressAge_Type())
a3ComSysBridgePortAddressAge.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgePortAddressAge.setStatus(_A)
class _A3ComSysBridgeStpGroupAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_A3ComSysBridgeStpGroupAddress_Type.__name__=_F
_A3ComSysBridgeStpGroupAddress_Object=MibScalar
a3ComSysBridgeStpGroupAddress=_A3ComSysBridgeStpGroupAddress_Object((1,3,6,1,4,1,43,29,4,10,6),_A3ComSysBridgeStpGroupAddress_Type())
a3ComSysBridgeStpGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeStpGroupAddress.setStatus(_W)
class _A3ComSysBridgeStpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_A3ComSysBridgeStpEnable_Type.__name__=_C
_A3ComSysBridgeStpEnable_Object=MibScalar
a3ComSysBridgeStpEnable=_A3ComSysBridgeStpEnable_Object((1,3,6,1,4,1,43,29,4,10,7),_A3ComSysBridgeStpEnable_Type())
a3ComSysBridgeStpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeStpEnable.setStatus(_W)
_A3ComSysBridgeVlanPortAddressTable_Object=MibTable
a3ComSysBridgeVlanPortAddressTable=_A3ComSysBridgeVlanPortAddressTable_Object((1,3,6,1,4,1,43,29,4,10,8))
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressTable.setStatus(_A)
_A3ComSysBridgeVlanPortAddressEntry_Object=MibTableRow
a3ComSysBridgeVlanPortAddressEntry=_A3ComSysBridgeVlanPortAddressEntry_Object((1,3,6,1,4,1,43,29,4,10,8,1))
a3ComSysBridgeVlanPortAddressEntry.setIndexNames((0,_E,_X),(0,_E,_Y),(0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressEntry.setStatus(_A)
_A3ComSysBridgeVlanPortAddressBridgeIndex_Type=Integer32
_A3ComSysBridgeVlanPortAddressBridgeIndex_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressBridgeIndex=_A3ComSysBridgeVlanPortAddressBridgeIndex_Object((1,3,6,1,4,1,43,29,4,10,8,1,1),_A3ComSysBridgeVlanPortAddressBridgeIndex_Type())
a3ComSysBridgeVlanPortAddressBridgeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressBridgeIndex.setStatus(_A)
_A3ComSysBridgeVlanPortAddressVlanIndex_Type=Integer32
_A3ComSysBridgeVlanPortAddressVlanIndex_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressVlanIndex=_A3ComSysBridgeVlanPortAddressVlanIndex_Object((1,3,6,1,4,1,43,29,4,10,8,1,2),_A3ComSysBridgeVlanPortAddressVlanIndex_Type())
a3ComSysBridgeVlanPortAddressVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressVlanIndex.setStatus(_A)
_A3ComSysBridgeVlanPortAddressPortIndex_Type=Integer32
_A3ComSysBridgeVlanPortAddressPortIndex_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressPortIndex=_A3ComSysBridgeVlanPortAddressPortIndex_Object((1,3,6,1,4,1,43,29,4,10,8,1,3),_A3ComSysBridgeVlanPortAddressPortIndex_Type())
a3ComSysBridgeVlanPortAddressPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressPortIndex.setStatus(_A)
_A3ComSysBridgeVlanPortAddressIndex_Type=Integer32
_A3ComSysBridgeVlanPortAddressIndex_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressIndex=_A3ComSysBridgeVlanPortAddressIndex_Object((1,3,6,1,4,1,43,29,4,10,8,1,4),_A3ComSysBridgeVlanPortAddressIndex_Type())
a3ComSysBridgeVlanPortAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressIndex.setStatus(_A)
class _A3ComSysBridgeVlanPortAddressRemoteAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_A3ComSysBridgeVlanPortAddressRemoteAddress_Type.__name__=_F
_A3ComSysBridgeVlanPortAddressRemoteAddress_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressRemoteAddress=_A3ComSysBridgeVlanPortAddressRemoteAddress_Object((1,3,6,1,4,1,43,29,4,10,8,1,5),_A3ComSysBridgeVlanPortAddressRemoteAddress_Type())
a3ComSysBridgeVlanPortAddressRemoteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressRemoteAddress.setStatus(_A)
class _A3ComSysBridgeVlanPortAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_T,2)))
_A3ComSysBridgeVlanPortAddressType_Type.__name__=_C
_A3ComSysBridgeVlanPortAddressType_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressType=_A3ComSysBridgeVlanPortAddressType_Object((1,3,6,1,4,1,43,29,4,10,8,1,6),_A3ComSysBridgeVlanPortAddressType_Type())
a3ComSysBridgeVlanPortAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressType.setStatus(_A)
class _A3ComSysBridgeVlanPortAddressIsStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_A3ComSysBridgeVlanPortAddressIsStatic_Type.__name__=_C
_A3ComSysBridgeVlanPortAddressIsStatic_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressIsStatic=_A3ComSysBridgeVlanPortAddressIsStatic_Object((1,3,6,1,4,1,43,29,4,10,8,1,7),_A3ComSysBridgeVlanPortAddressIsStatic_Type())
a3ComSysBridgeVlanPortAddressIsStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressIsStatic.setStatus(_A)
_A3ComSysBridgeVlanPortAddressStaticPort_Type=Integer32
_A3ComSysBridgeVlanPortAddressStaticPort_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressStaticPort=_A3ComSysBridgeVlanPortAddressStaticPort_Object((1,3,6,1,4,1,43,29,4,10,8,1,8),_A3ComSysBridgeVlanPortAddressStaticPort_Type())
a3ComSysBridgeVlanPortAddressStaticPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressStaticPort.setStatus(_A)
_A3ComSysBridgeVlanPortAddressAge_Type=Integer32
_A3ComSysBridgeVlanPortAddressAge_Object=MibTableColumn
a3ComSysBridgeVlanPortAddressAge=_A3ComSysBridgeVlanPortAddressAge_Object((1,3,6,1,4,1,43,29,4,10,8,1,9),_A3ComSysBridgeVlanPortAddressAge_Type())
a3ComSysBridgeVlanPortAddressAge.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComSysBridgeVlanPortAddressAge.setStatus(_A)
a3ComSysBridgeAddressThresholdEvent=NotificationType((1,3,6,1,4,1,43,29,4,0,6))
a3ComSysBridgeAddressThresholdEvent.setObjects((_E,_L))
if mibBuilder.loadTexts:a3ComSysBridgeAddressThresholdEvent.setStatus('')
a3ComSysBridgePortLearnEvent=NotificationType((1,3,6,1,4,1,43,29,4,10,0,60))
a3ComSysBridgePortLearnEvent.setObjects(*((_E,_K),(_E,_b)))
if mibBuilder.loadTexts:a3ComSysBridgePortLearnEvent.setStatus('')
a3ComSysBridgePortRateLimitEvent=NotificationType((1,3,6,1,4,1,43,29,4,10,0,61))
a3ComSysBridgePortRateLimitEvent.setObjects(*((_E,_K),(_E,_c)))
if mibBuilder.loadTexts:a3ComSysBridgePortRateLimitEvent.setStatus('')
a3ComSysBridgePortLoopDetectEvent=NotificationType((1,3,6,1,4,1,43,29,4,10,0,62))
a3ComSysBridgePortLoopDetectEvent.setObjects(*((_E,_K),(_E,_d)))
if mibBuilder.loadTexts:a3ComSysBridgePortLoopDetectEvent.setStatus('')
mibBuilder.exportSymbols(_E,**{'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComSysBridgeAddressThresholdEvent':a3ComSysBridgeAddressThresholdEvent,'a3ComSysBridge':a3ComSysBridge,'a3ComSysBridgePortLearnEvent':a3ComSysBridgePortLearnEvent,'a3ComSysBridgePortRateLimitEvent':a3ComSysBridgePortRateLimitEvent,'a3ComSysBridgePortLoopDetectEvent':a3ComSysBridgePortLoopDetectEvent,'a3ComSysBridgeCount':a3ComSysBridgeCount,'a3ComSysBridgeTable':a3ComSysBridgeTable,'a3ComSysBridgeEntry':a3ComSysBridgeEntry,_L:a3ComSysBridgeIndex,'a3ComSysBridgePortCount':a3ComSysBridgePortCount,'a3ComSysBridgeAddressTableSize':a3ComSysBridgeAddressTableSize,'a3ComSysBridgeAddressTableCount':a3ComSysBridgeAddressTableCount,'a3ComSysBridgeAddressTablePeakCount':a3ComSysBridgeAddressTablePeakCount,'a3ComSysBridgeAddressThreshold':a3ComSysBridgeAddressThreshold,'a3ComSysBridgeMode':a3ComSysBridgeMode,'a3ComSysBridgeBackbonePort':a3ComSysBridgeBackbonePort,'a3ComSysBridgeIpFragmentationEnabled':a3ComSysBridgeIpFragmentationEnabled,'a3ComSysBridgeTrFddiTranslationMode':a3ComSysBridgeTrFddiTranslationMode,'a3ComSysBridgeSTPGroupAddress':a3ComSysBridgeSTPGroupAddress,'a3ComSysBridgeSTPEnable':a3ComSysBridgeSTPEnable,'a3ComSysBridgeIpxSnapTranslationEnable':a3ComSysBridgeIpxSnapTranslationEnable,'a3ComSysBridgeLowLatencyEnable':a3ComSysBridgeLowLatencyEnable,'a3ComSysBridgeVlanMode':a3ComSysBridgeVlanMode,'a3ComSysBridgeRateLimitReceiveMulticast':a3ComSysBridgeRateLimitReceiveMulticast,'a3ComSysBridgeRateLimitReceiveBroadcast':a3ComSysBridgeRateLimitReceiveBroadcast,'a3ComSysBridgeRateLimitReceiveFlood':a3ComSysBridgeRateLimitReceiveFlood,'a3ComSysBridgeAddressLearnMode':a3ComSysBridgeAddressLearnMode,'a3ComSysBridgeAddressAgingInterval':a3ComSysBridgeAddressAgingInterval,'a3ComSysBridgeLoopDetectMode':a3ComSysBridgeLoopDetectMode,'a3ComSysBridgeLoopDetectSrcAddress':a3ComSysBridgeLoopDetectSrcAddress,'a3ComSysBridgePortTable':a3ComSysBridgePortTable,'a3ComSysBridgePortEntry':a3ComSysBridgePortEntry,_O:a3ComSysBridgePortBridgeIndex,_K:a3ComSysBridgePortIndex,'a3ComSysBridgePortIfIndex':a3ComSysBridgePortIfIndex,'a3ComSysBridgePortReceiveMulticastLimit':a3ComSysBridgePortReceiveMulticastLimit,'a3ComSysBridgePortAddressAction':a3ComSysBridgePortAddressAction,'a3ComSysBridgePortSpanningTreeFrameReceivedCounts':a3ComSysBridgePortSpanningTreeFrameReceivedCounts,'a3ComSysBridgePortReceiveBlockedDiscards':a3ComSysBridgePortReceiveBlockedDiscards,'a3ComSysBridgePortReceiveMulticastLimitExceededs':a3ComSysBridgePortReceiveMulticastLimitExceededs,'a3ComSysBridgePortReceiveMulticastLimitExceededDiscards':a3ComSysBridgePortReceiveMulticastLimitExceededDiscards,'a3ComSysBridgePortReceiveSecurityDiscards':a3ComSysBridgePortReceiveSecurityDiscards,'a3ComSysBridgePortReceiveUnknownDiscards':a3ComSysBridgePortReceiveUnknownDiscards,'a3ComSysBridgePortReceiveOtherDiscards':a3ComSysBridgePortReceiveOtherDiscards,'a3ComSysBridgePortReceiveErrorDiscards':a3ComSysBridgePortReceiveErrorDiscards,'a3ComSysBridgePortSameSegmentDiscards':a3ComSysBridgePortSameSegmentDiscards,'a3ComSysBridgePortTransmitBlockedDiscards':a3ComSysBridgePortTransmitBlockedDiscards,'a3ComSysBridgePortReceiveAllPathFilteredFrames':a3ComSysBridgePortReceiveAllPathFilteredFrames,'a3ComSysBridgePortReceiveMulticastPathFilteredFrames':a3ComSysBridgePortReceiveMulticastPathFilteredFrames,'a3ComSysBridgePortTransmitAllPathFilteredFrames':a3ComSysBridgePortTransmitAllPathFilteredFrames,'a3ComSysBridgePortTransmitMulticastPathFilteredFrames':a3ComSysBridgePortTransmitMulticastPathFilteredFrames,'a3ComSysBridgePortForwardedUnicastFrames':a3ComSysBridgePortForwardedUnicastFrames,'a3ComSysBridgePortForwardedUnicastOctets':a3ComSysBridgePortForwardedUnicastOctets,'a3ComSysBridgePortForwardedMulticastFrames':a3ComSysBridgePortForwardedMulticastFrames,'a3ComSysBridgePortForwardedMulticastOctets':a3ComSysBridgePortForwardedMulticastOctets,'a3ComSysBridgePortFloodedUnicastFrames':a3ComSysBridgePortFloodedUnicastFrames,'a3ComSysBridgePortFloodedUnicastOctets':a3ComSysBridgePortFloodedUnicastOctets,'a3ComSysBridgePortStpMode':a3ComSysBridgePortStpMode,'a3ComSysBridgePortReceiveMulticastLimitFrameType':a3ComSysBridgePortReceiveMulticastLimitFrameType,'a3ComSysBridgePortForwardedFrames':a3ComSysBridgePortForwardedFrames,'a3ComSysBridgePortReceiveMulticastLimitMultiplier':a3ComSysBridgePortReceiveMulticastLimitMultiplier,'a3ComSysBridgePortRateLimitReceiveMulticastEnabled':a3ComSysBridgePortRateLimitReceiveMulticastEnabled,'a3ComSysBridgePortRateLimitReceiveBroadcastEnabled':a3ComSysBridgePortRateLimitReceiveBroadcastEnabled,'a3ComSysBridgePortRateLimitReceiveFloodEnabled':a3ComSysBridgePortRateLimitReceiveFloodEnabled,_c:a3ComSysBridgePortRateLimitReceiveState,_d:a3ComSysBridgePortLoopDetectState,'a3ComSysBridgePortAddressMaxLimit':a3ComSysBridgePortAddressMaxLimit,_b:a3ComSysBridgePortAddressState,'a3ComSysBridgePortReceiveInternalPathFilteredFrames':a3ComSysBridgePortReceiveInternalPathFilteredFrames,'a3ComSysBridgePortAddressTable':a3ComSysBridgePortAddressTable,'a3ComSysBridgePortAddressEntry':a3ComSysBridgePortAddressEntry,_Q:a3ComSysBridgePortAddressBridgeIndex,_R:a3ComSysBridgePortAddressPortIndex,_S:a3ComSysBridgePortAddressIndex,'a3ComSysBridgePortAddressRemoteAddress':a3ComSysBridgePortAddressRemoteAddress,'a3ComSysBridgePortAddressType':a3ComSysBridgePortAddressType,'a3ComSysBridgePortAddressIsStatic':a3ComSysBridgePortAddressIsStatic,'a3ComSysBridgePortAddressStaticPort':a3ComSysBridgePortAddressStaticPort,'a3ComSysBridgePortAddressAge':a3ComSysBridgePortAddressAge,'a3ComSysBridgeStpGroupAddress':a3ComSysBridgeStpGroupAddress,'a3ComSysBridgeStpEnable':a3ComSysBridgeStpEnable,'a3ComSysBridgeVlanPortAddressTable':a3ComSysBridgeVlanPortAddressTable,'a3ComSysBridgeVlanPortAddressEntry':a3ComSysBridgeVlanPortAddressEntry,_X:a3ComSysBridgeVlanPortAddressBridgeIndex,_Y:a3ComSysBridgeVlanPortAddressVlanIndex,_Z:a3ComSysBridgeVlanPortAddressPortIndex,_a:a3ComSysBridgeVlanPortAddressIndex,'a3ComSysBridgeVlanPortAddressRemoteAddress':a3ComSysBridgeVlanPortAddressRemoteAddress,'a3ComSysBridgeVlanPortAddressType':a3ComSysBridgeVlanPortAddressType,'a3ComSysBridgeVlanPortAddressIsStatic':a3ComSysBridgeVlanPortAddressIsStatic,'a3ComSysBridgeVlanPortAddressStaticPort':a3ComSysBridgeVlanPortAddressStaticPort,'a3ComSysBridgeVlanPortAddressAge':a3ComSysBridgeVlanPortAddressAge})