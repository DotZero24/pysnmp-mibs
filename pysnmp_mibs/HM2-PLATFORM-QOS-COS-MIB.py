_R='hm2AgentCosQueueDropPrecIndex'
_Q='taildrop'
_P='hm2AgentCosMapIntfTrustIntfIndex'
_O='hm2AgentCosMapIpDscpValue'
_N='hm2AgentCosMapIpDscpIntfIndex'
_M='hm2AgentCosMapIpPrecValue'
_L='hm2AgentCosMapIpPrecIntfIndex'
_K='hm2AgentCosQueueIndex'
_J='obsolete'
_I='Percent'
_H='hm2AgentCosQueueIntfIndex'
_G='read-only'
_F='Integer32'
_E='not-accessible'
_D='Unsigned32'
_C='HM2-PLATFORM-QOS-COS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2PlatformQoS,=mibBuilder.importSymbols('HM2-PLATFORM-QOS-MIB','hm2PlatformQoS')
HmEnabledStatus,=mibBuilder.importSymbols('HM2-TC-MIB','HmEnabledStatus')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2PlatformQosCos=ModuleIdentity((1,3,6,1,4,1,248,12,3,3))
if mibBuilder.loadTexts:hm2PlatformQosCos.setRevisions(('2011-10-12 00:00',))
class Percent(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class Sixteenths(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Hm2AgentCosMapCfgGroup_ObjectIdentity=ObjectIdentity
hm2AgentCosMapCfgGroup=_Hm2AgentCosMapCfgGroup_ObjectIdentity((1,3,6,1,4,1,248,12,3,3,1))
_Hm2AgentCosMapIpPrecTable_Object=MibTable
hm2AgentCosMapIpPrecTable=_Hm2AgentCosMapIpPrecTable_Object((1,3,6,1,4,1,248,12,3,3,1,1))
if mibBuilder.loadTexts:hm2AgentCosMapIpPrecTable.setStatus(_A)
_Hm2AgentCosMapIpPrecEntry_Object=MibTableRow
hm2AgentCosMapIpPrecEntry=_Hm2AgentCosMapIpPrecEntry_Object((1,3,6,1,4,1,248,12,3,3,1,1,1))
hm2AgentCosMapIpPrecEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:hm2AgentCosMapIpPrecEntry.setStatus(_A)
_Hm2AgentCosMapIpPrecIntfIndex_Type=InterfaceIndexOrZero
_Hm2AgentCosMapIpPrecIntfIndex_Object=MibTableColumn
hm2AgentCosMapIpPrecIntfIndex=_Hm2AgentCosMapIpPrecIntfIndex_Object((1,3,6,1,4,1,248,12,3,3,1,1,1,1),_Hm2AgentCosMapIpPrecIntfIndex_Type())
hm2AgentCosMapIpPrecIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosMapIpPrecIntfIndex.setStatus(_A)
class _Hm2AgentCosMapIpPrecValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2AgentCosMapIpPrecValue_Type.__name__=_D
_Hm2AgentCosMapIpPrecValue_Object=MibTableColumn
hm2AgentCosMapIpPrecValue=_Hm2AgentCosMapIpPrecValue_Object((1,3,6,1,4,1,248,12,3,3,1,1,1,2),_Hm2AgentCosMapIpPrecValue_Type())
hm2AgentCosMapIpPrecValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosMapIpPrecValue.setStatus(_A)
class _Hm2AgentCosMapIpPrecTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2AgentCosMapIpPrecTrafficClass_Type.__name__=_D
_Hm2AgentCosMapIpPrecTrafficClass_Object=MibTableColumn
hm2AgentCosMapIpPrecTrafficClass=_Hm2AgentCosMapIpPrecTrafficClass_Object((1,3,6,1,4,1,248,12,3,3,1,1,1,3),_Hm2AgentCosMapIpPrecTrafficClass_Type())
hm2AgentCosMapIpPrecTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosMapIpPrecTrafficClass.setStatus(_A)
_Hm2AgentCosMapIpDscpTable_Object=MibTable
hm2AgentCosMapIpDscpTable=_Hm2AgentCosMapIpDscpTable_Object((1,3,6,1,4,1,248,12,3,3,1,2))
if mibBuilder.loadTexts:hm2AgentCosMapIpDscpTable.setStatus(_A)
_Hm2AgentCosMapIpDscpEntry_Object=MibTableRow
hm2AgentCosMapIpDscpEntry=_Hm2AgentCosMapIpDscpEntry_Object((1,3,6,1,4,1,248,12,3,3,1,2,1))
hm2AgentCosMapIpDscpEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:hm2AgentCosMapIpDscpEntry.setStatus(_A)
_Hm2AgentCosMapIpDscpIntfIndex_Type=InterfaceIndexOrZero
_Hm2AgentCosMapIpDscpIntfIndex_Object=MibTableColumn
hm2AgentCosMapIpDscpIntfIndex=_Hm2AgentCosMapIpDscpIntfIndex_Object((1,3,6,1,4,1,248,12,3,3,1,2,1,1),_Hm2AgentCosMapIpDscpIntfIndex_Type())
hm2AgentCosMapIpDscpIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosMapIpDscpIntfIndex.setStatus(_A)
class _Hm2AgentCosMapIpDscpValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Hm2AgentCosMapIpDscpValue_Type.__name__=_D
_Hm2AgentCosMapIpDscpValue_Object=MibTableColumn
hm2AgentCosMapIpDscpValue=_Hm2AgentCosMapIpDscpValue_Object((1,3,6,1,4,1,248,12,3,3,1,2,1,2),_Hm2AgentCosMapIpDscpValue_Type())
hm2AgentCosMapIpDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosMapIpDscpValue.setStatus(_A)
class _Hm2AgentCosMapIpDscpTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2AgentCosMapIpDscpTrafficClass_Type.__name__=_D
_Hm2AgentCosMapIpDscpTrafficClass_Object=MibTableColumn
hm2AgentCosMapIpDscpTrafficClass=_Hm2AgentCosMapIpDscpTrafficClass_Object((1,3,6,1,4,1,248,12,3,3,1,2,1,3),_Hm2AgentCosMapIpDscpTrafficClass_Type())
hm2AgentCosMapIpDscpTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosMapIpDscpTrafficClass.setStatus(_A)
_Hm2AgentCosMapIntfTrustTable_Object=MibTable
hm2AgentCosMapIntfTrustTable=_Hm2AgentCosMapIntfTrustTable_Object((1,3,6,1,4,1,248,12,3,3,1,3))
if mibBuilder.loadTexts:hm2AgentCosMapIntfTrustTable.setStatus(_A)
_Hm2AgentCosMapIntfTrustEntry_Object=MibTableRow
hm2AgentCosMapIntfTrustEntry=_Hm2AgentCosMapIntfTrustEntry_Object((1,3,6,1,4,1,248,12,3,3,1,3,1))
hm2AgentCosMapIntfTrustEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:hm2AgentCosMapIntfTrustEntry.setStatus(_A)
_Hm2AgentCosMapIntfTrustIntfIndex_Type=InterfaceIndexOrZero
_Hm2AgentCosMapIntfTrustIntfIndex_Object=MibTableColumn
hm2AgentCosMapIntfTrustIntfIndex=_Hm2AgentCosMapIntfTrustIntfIndex_Object((1,3,6,1,4,1,248,12,3,3,1,3,1,1),_Hm2AgentCosMapIntfTrustIntfIndex_Type())
hm2AgentCosMapIntfTrustIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosMapIntfTrustIntfIndex.setStatus(_A)
class _Hm2AgentCosMapIntfTrustMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('untrusted',1),('trustDot1p',2),('trustIpPrecedence',3),('trustIpDscp',4)))
_Hm2AgentCosMapIntfTrustMode_Type.__name__=_F
_Hm2AgentCosMapIntfTrustMode_Object=MibTableColumn
hm2AgentCosMapIntfTrustMode=_Hm2AgentCosMapIntfTrustMode_Object((1,3,6,1,4,1,248,12,3,3,1,3,1,2),_Hm2AgentCosMapIntfTrustMode_Type())
hm2AgentCosMapIntfTrustMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosMapIntfTrustMode.setStatus(_A)
_Hm2AgentCosMapUntrustedTrafficClass_Type=Unsigned32
_Hm2AgentCosMapUntrustedTrafficClass_Object=MibTableColumn
hm2AgentCosMapUntrustedTrafficClass=_Hm2AgentCosMapUntrustedTrafficClass_Object((1,3,6,1,4,1,248,12,3,3,1,3,1,3),_Hm2AgentCosMapUntrustedTrafficClass_Type())
hm2AgentCosMapUntrustedTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentCosMapUntrustedTrafficClass.setStatus(_A)
_Hm2AgentCosQueueCfgGroup_ObjectIdentity=ObjectIdentity
hm2AgentCosQueueCfgGroup=_Hm2AgentCosQueueCfgGroup_ObjectIdentity((1,3,6,1,4,1,248,12,3,3,2))
_Hm2AgentCosQueueNumQueuesPerPort_Type=Unsigned32
_Hm2AgentCosQueueNumQueuesPerPort_Object=MibScalar
hm2AgentCosQueueNumQueuesPerPort=_Hm2AgentCosQueueNumQueuesPerPort_Object((1,3,6,1,4,1,248,12,3,3,2,1),_Hm2AgentCosQueueNumQueuesPerPort_Type())
hm2AgentCosQueueNumQueuesPerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentCosQueueNumQueuesPerPort.setStatus(_A)
_Hm2AgentCosQueueNumDropPrecedenceLevels_Type=Unsigned32
_Hm2AgentCosQueueNumDropPrecedenceLevels_Object=MibScalar
hm2AgentCosQueueNumDropPrecedenceLevels=_Hm2AgentCosQueueNumDropPrecedenceLevels_Object((1,3,6,1,4,1,248,12,3,3,2,2),_Hm2AgentCosQueueNumDropPrecedenceLevels_Type())
hm2AgentCosQueueNumDropPrecedenceLevels.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentCosQueueNumDropPrecedenceLevels.setStatus(_A)
_Hm2AgentCosQueueControlTable_Object=MibTable
hm2AgentCosQueueControlTable=_Hm2AgentCosQueueControlTable_Object((1,3,6,1,4,1,248,12,3,3,2,3))
if mibBuilder.loadTexts:hm2AgentCosQueueControlTable.setStatus(_A)
_Hm2AgentCosQueueControlEntry_Object=MibTableRow
hm2AgentCosQueueControlEntry=_Hm2AgentCosQueueControlEntry_Object((1,3,6,1,4,1,248,12,3,3,2,3,1))
hm2AgentCosQueueControlEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:hm2AgentCosQueueControlEntry.setStatus(_A)
_Hm2AgentCosQueueIntfIndex_Type=InterfaceIndexOrZero
_Hm2AgentCosQueueIntfIndex_Object=MibTableColumn
hm2AgentCosQueueIntfIndex=_Hm2AgentCosQueueIntfIndex_Object((1,3,6,1,4,1,248,12,3,3,2,3,1,1),_Hm2AgentCosQueueIntfIndex_Type())
hm2AgentCosQueueIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosQueueIntfIndex.setStatus(_A)
class _Hm2AgentCosQueueIntfShapingRate_Type(Unsigned32):defaultValue=0
_Hm2AgentCosQueueIntfShapingRate_Type.__name__=_D
_Hm2AgentCosQueueIntfShapingRate_Object=MibTableColumn
hm2AgentCosQueueIntfShapingRate=_Hm2AgentCosQueueIntfShapingRate_Object((1,3,6,1,4,1,248,12,3,3,2,3,1,2),_Hm2AgentCosQueueIntfShapingRate_Type())
hm2AgentCosQueueIntfShapingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueIntfShapingRate.setStatus(_A)
class _Hm2AgentCosQueueMgmtTypeIntf_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('wred',2)))
_Hm2AgentCosQueueMgmtTypeIntf_Type.__name__=_F
_Hm2AgentCosQueueMgmtTypeIntf_Object=MibTableColumn
hm2AgentCosQueueMgmtTypeIntf=_Hm2AgentCosQueueMgmtTypeIntf_Object((1,3,6,1,4,1,248,12,3,3,2,3,1,3),_Hm2AgentCosQueueMgmtTypeIntf_Type())
hm2AgentCosQueueMgmtTypeIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtTypeIntf.setStatus(_A)
class _Hm2AgentCosQueueWredDecayExponent_Type(Unsigned32):defaultValue=9;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Hm2AgentCosQueueWredDecayExponent_Type.__name__=_D
_Hm2AgentCosQueueWredDecayExponent_Object=MibTableColumn
hm2AgentCosQueueWredDecayExponent=_Hm2AgentCosQueueWredDecayExponent_Object((1,3,6,1,4,1,248,12,3,3,2,3,1,4),_Hm2AgentCosQueueWredDecayExponent_Type())
hm2AgentCosQueueWredDecayExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueWredDecayExponent.setStatus(_A)
_Hm2AgentCosQueueDefaultsRestore_Type=HmEnabledStatus
_Hm2AgentCosQueueDefaultsRestore_Object=MibTableColumn
hm2AgentCosQueueDefaultsRestore=_Hm2AgentCosQueueDefaultsRestore_Object((1,3,6,1,4,1,248,12,3,3,2,3,1,5),_Hm2AgentCosQueueDefaultsRestore_Type())
hm2AgentCosQueueDefaultsRestore.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueDefaultsRestore.setStatus(_A)
class _Hm2AgentCosQueueIntfShapingRateUnits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('percent',1),('kbps',2)))
_Hm2AgentCosQueueIntfShapingRateUnits_Type.__name__=_F
_Hm2AgentCosQueueIntfShapingRateUnits_Object=MibTableColumn
hm2AgentCosQueueIntfShapingRateUnits=_Hm2AgentCosQueueIntfShapingRateUnits_Object((1,3,6,1,4,1,248,12,3,3,2,3,1,6),_Hm2AgentCosQueueIntfShapingRateUnits_Type())
hm2AgentCosQueueIntfShapingRateUnits.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentCosQueueIntfShapingRateUnits.setStatus(_A)
_Hm2AgentCosQueueTable_Object=MibTable
hm2AgentCosQueueTable=_Hm2AgentCosQueueTable_Object((1,3,6,1,4,1,248,12,3,3,2,4))
if mibBuilder.loadTexts:hm2AgentCosQueueTable.setStatus(_A)
_Hm2AgentCosQueueEntry_Object=MibTableRow
hm2AgentCosQueueEntry=_Hm2AgentCosQueueEntry_Object((1,3,6,1,4,1,248,12,3,3,2,4,1))
hm2AgentCosQueueEntry.setIndexNames((0,_C,_H),(0,_C,_K))
if mibBuilder.loadTexts:hm2AgentCosQueueEntry.setStatus(_A)
_Hm2AgentCosQueueIndex_Type=Unsigned32
_Hm2AgentCosQueueIndex_Object=MibTableColumn
hm2AgentCosQueueIndex=_Hm2AgentCosQueueIndex_Object((1,3,6,1,4,1,248,12,3,3,2,4,1,1),_Hm2AgentCosQueueIndex_Type())
hm2AgentCosQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosQueueIndex.setStatus(_A)
class _Hm2AgentCosQueueSchedulerType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('weighted',2)))
_Hm2AgentCosQueueSchedulerType_Type.__name__=_F
_Hm2AgentCosQueueSchedulerType_Object=MibTableColumn
hm2AgentCosQueueSchedulerType=_Hm2AgentCosQueueSchedulerType_Object((1,3,6,1,4,1,248,12,3,3,2,4,1,2),_Hm2AgentCosQueueSchedulerType_Type())
hm2AgentCosQueueSchedulerType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueSchedulerType.setStatus(_A)
class _Hm2AgentCosQueueMinBandwidth_Type(Percent):defaultValue=0
_Hm2AgentCosQueueMinBandwidth_Type.__name__=_I
_Hm2AgentCosQueueMinBandwidth_Object=MibTableColumn
hm2AgentCosQueueMinBandwidth=_Hm2AgentCosQueueMinBandwidth_Object((1,3,6,1,4,1,248,12,3,3,2,4,1,3),_Hm2AgentCosQueueMinBandwidth_Type())
hm2AgentCosQueueMinBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMinBandwidth.setStatus(_A)
class _Hm2AgentCosQueueMaxBandwidth_Type(Percent):defaultValue=0
_Hm2AgentCosQueueMaxBandwidth_Type.__name__=_I
_Hm2AgentCosQueueMaxBandwidth_Object=MibTableColumn
hm2AgentCosQueueMaxBandwidth=_Hm2AgentCosQueueMaxBandwidth_Object((1,3,6,1,4,1,248,12,3,3,2,4,1,4),_Hm2AgentCosQueueMaxBandwidth_Type())
hm2AgentCosQueueMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMaxBandwidth.setStatus(_A)
class _Hm2AgentCosQueueMgmtType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('wred',2)))
_Hm2AgentCosQueueMgmtType_Type.__name__=_F
_Hm2AgentCosQueueMgmtType_Object=MibTableColumn
hm2AgentCosQueueMgmtType=_Hm2AgentCosQueueMgmtType_Object((1,3,6,1,4,1,248,12,3,3,2,4,1,5),_Hm2AgentCosQueueMgmtType_Type())
hm2AgentCosQueueMgmtType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtType.setStatus(_A)
_Hm2AgentCosQueueMgmtTable_Object=MibTable
hm2AgentCosQueueMgmtTable=_Hm2AgentCosQueueMgmtTable_Object((1,3,6,1,4,1,248,12,3,3,2,5))
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtTable.setStatus(_A)
_Hm2AgentCosQueueMgmtEntry_Object=MibTableRow
hm2AgentCosQueueMgmtEntry=_Hm2AgentCosQueueMgmtEntry_Object((1,3,6,1,4,1,248,12,3,3,2,5,1))
hm2AgentCosQueueMgmtEntry.setIndexNames((0,_C,_H),(0,_C,_K),(0,_C,_R))
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtEntry.setStatus(_A)
_Hm2AgentCosQueueDropPrecIndex_Type=Unsigned32
_Hm2AgentCosQueueDropPrecIndex_Object=MibTableColumn
hm2AgentCosQueueDropPrecIndex=_Hm2AgentCosQueueDropPrecIndex_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,1),_Hm2AgentCosQueueDropPrecIndex_Type())
hm2AgentCosQueueDropPrecIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2AgentCosQueueDropPrecIndex.setStatus(_A)
_Hm2AgentCosQueueMgmtTailDropThreshold_Type=Sixteenths
_Hm2AgentCosQueueMgmtTailDropThreshold_Object=MibTableColumn
hm2AgentCosQueueMgmtTailDropThreshold=_Hm2AgentCosQueueMgmtTailDropThreshold_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,2),_Hm2AgentCosQueueMgmtTailDropThreshold_Type())
hm2AgentCosQueueMgmtTailDropThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtTailDropThreshold.setStatus(_J)
_Hm2AgentCosQueueMgmtWredMinThreshold_Type=Sixteenths
_Hm2AgentCosQueueMgmtWredMinThreshold_Object=MibTableColumn
hm2AgentCosQueueMgmtWredMinThreshold=_Hm2AgentCosQueueMgmtWredMinThreshold_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,3),_Hm2AgentCosQueueMgmtWredMinThreshold_Type())
hm2AgentCosQueueMgmtWredMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtWredMinThreshold.setStatus(_J)
_Hm2AgentCosQueueMgmtWredMaxThreshold_Type=Sixteenths
_Hm2AgentCosQueueMgmtWredMaxThreshold_Object=MibTableColumn
hm2AgentCosQueueMgmtWredMaxThreshold=_Hm2AgentCosQueueMgmtWredMaxThreshold_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,4),_Hm2AgentCosQueueMgmtWredMaxThreshold_Type())
hm2AgentCosQueueMgmtWredMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtWredMaxThreshold.setStatus(_J)
class _Hm2AgentCosQueueMgmtWredDropProbScale_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Hm2AgentCosQueueMgmtWredDropProbScale_Type.__name__=_D
_Hm2AgentCosQueueMgmtWredDropProbScale_Object=MibTableColumn
hm2AgentCosQueueMgmtWredDropProbScale=_Hm2AgentCosQueueMgmtWredDropProbScale_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,5),_Hm2AgentCosQueueMgmtWredDropProbScale_Type())
hm2AgentCosQueueMgmtWredDropProbScale.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtWredDropProbScale.setStatus(_J)
_Hm2AgentCosQueueMgmtPercentTailDropThreshold_Type=Percent
_Hm2AgentCosQueueMgmtPercentTailDropThreshold_Object=MibTableColumn
hm2AgentCosQueueMgmtPercentTailDropThreshold=_Hm2AgentCosQueueMgmtPercentTailDropThreshold_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,6),_Hm2AgentCosQueueMgmtPercentTailDropThreshold_Type())
hm2AgentCosQueueMgmtPercentTailDropThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtPercentTailDropThreshold.setStatus(_A)
_Hm2AgentCosQueueMgmtPercentWredMinThreshold_Type=Percent
_Hm2AgentCosQueueMgmtPercentWredMinThreshold_Object=MibTableColumn
hm2AgentCosQueueMgmtPercentWredMinThreshold=_Hm2AgentCosQueueMgmtPercentWredMinThreshold_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,7),_Hm2AgentCosQueueMgmtPercentWredMinThreshold_Type())
hm2AgentCosQueueMgmtPercentWredMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtPercentWredMinThreshold.setStatus(_A)
_Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Type=Percent
_Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Object=MibTableColumn
hm2AgentCosQueueMgmtPercentWredMaxThreshold=_Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,8),_Hm2AgentCosQueueMgmtPercentWredMaxThreshold_Type())
hm2AgentCosQueueMgmtPercentWredMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtPercentWredMaxThreshold.setStatus(_A)
class _Hm2AgentCosQueueMgmtWredDropProbability_Type(Percent):defaultValue=10
_Hm2AgentCosQueueMgmtWredDropProbability_Type.__name__=_I
_Hm2AgentCosQueueMgmtWredDropProbability_Object=MibTableColumn
hm2AgentCosQueueMgmtWredDropProbability=_Hm2AgentCosQueueMgmtWredDropProbability_Object((1,3,6,1,4,1,248,12,3,3,2,5,1,9),_Hm2AgentCosQueueMgmtWredDropProbability_Type())
hm2AgentCosQueueMgmtWredDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentCosQueueMgmtWredDropProbability.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_I:Percent,'Sixteenths':Sixteenths,'hm2PlatformQosCos':hm2PlatformQosCos,'hm2AgentCosMapCfgGroup':hm2AgentCosMapCfgGroup,'hm2AgentCosMapIpPrecTable':hm2AgentCosMapIpPrecTable,'hm2AgentCosMapIpPrecEntry':hm2AgentCosMapIpPrecEntry,_L:hm2AgentCosMapIpPrecIntfIndex,_M:hm2AgentCosMapIpPrecValue,'hm2AgentCosMapIpPrecTrafficClass':hm2AgentCosMapIpPrecTrafficClass,'hm2AgentCosMapIpDscpTable':hm2AgentCosMapIpDscpTable,'hm2AgentCosMapIpDscpEntry':hm2AgentCosMapIpDscpEntry,_N:hm2AgentCosMapIpDscpIntfIndex,_O:hm2AgentCosMapIpDscpValue,'hm2AgentCosMapIpDscpTrafficClass':hm2AgentCosMapIpDscpTrafficClass,'hm2AgentCosMapIntfTrustTable':hm2AgentCosMapIntfTrustTable,'hm2AgentCosMapIntfTrustEntry':hm2AgentCosMapIntfTrustEntry,_P:hm2AgentCosMapIntfTrustIntfIndex,'hm2AgentCosMapIntfTrustMode':hm2AgentCosMapIntfTrustMode,'hm2AgentCosMapUntrustedTrafficClass':hm2AgentCosMapUntrustedTrafficClass,'hm2AgentCosQueueCfgGroup':hm2AgentCosQueueCfgGroup,'hm2AgentCosQueueNumQueuesPerPort':hm2AgentCosQueueNumQueuesPerPort,'hm2AgentCosQueueNumDropPrecedenceLevels':hm2AgentCosQueueNumDropPrecedenceLevels,'hm2AgentCosQueueControlTable':hm2AgentCosQueueControlTable,'hm2AgentCosQueueControlEntry':hm2AgentCosQueueControlEntry,_H:hm2AgentCosQueueIntfIndex,'hm2AgentCosQueueIntfShapingRate':hm2AgentCosQueueIntfShapingRate,'hm2AgentCosQueueMgmtTypeIntf':hm2AgentCosQueueMgmtTypeIntf,'hm2AgentCosQueueWredDecayExponent':hm2AgentCosQueueWredDecayExponent,'hm2AgentCosQueueDefaultsRestore':hm2AgentCosQueueDefaultsRestore,'hm2AgentCosQueueIntfShapingRateUnits':hm2AgentCosQueueIntfShapingRateUnits,'hm2AgentCosQueueTable':hm2AgentCosQueueTable,'hm2AgentCosQueueEntry':hm2AgentCosQueueEntry,_K:hm2AgentCosQueueIndex,'hm2AgentCosQueueSchedulerType':hm2AgentCosQueueSchedulerType,'hm2AgentCosQueueMinBandwidth':hm2AgentCosQueueMinBandwidth,'hm2AgentCosQueueMaxBandwidth':hm2AgentCosQueueMaxBandwidth,'hm2AgentCosQueueMgmtType':hm2AgentCosQueueMgmtType,'hm2AgentCosQueueMgmtTable':hm2AgentCosQueueMgmtTable,'hm2AgentCosQueueMgmtEntry':hm2AgentCosQueueMgmtEntry,_R:hm2AgentCosQueueDropPrecIndex,'hm2AgentCosQueueMgmtTailDropThreshold':hm2AgentCosQueueMgmtTailDropThreshold,'hm2AgentCosQueueMgmtWredMinThreshold':hm2AgentCosQueueMgmtWredMinThreshold,'hm2AgentCosQueueMgmtWredMaxThreshold':hm2AgentCosQueueMgmtWredMaxThreshold,'hm2AgentCosQueueMgmtWredDropProbScale':hm2AgentCosQueueMgmtWredDropProbScale,'hm2AgentCosQueueMgmtPercentTailDropThreshold':hm2AgentCosQueueMgmtPercentTailDropThreshold,'hm2AgentCosQueueMgmtPercentWredMinThreshold':hm2AgentCosQueueMgmtPercentWredMinThreshold,'hm2AgentCosQueueMgmtPercentWredMaxThreshold':hm2AgentCosQueueMgmtPercentWredMaxThreshold,'hm2AgentCosQueueMgmtWredDropProbability':hm2AgentCosQueueMgmtWredDropProbability})