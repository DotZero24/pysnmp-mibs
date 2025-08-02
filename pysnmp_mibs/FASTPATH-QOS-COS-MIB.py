_R='agentCosQueueDropPrecIndex'
_Q='taildrop'
_P='agentCosMapIntfTrustIntfIndex'
_O='agentCosMapIpDscpValue'
_N='agentCosMapIpDscpIntfIndex'
_M='agentCosMapIpPrecValue'
_L='agentCosMapIpPrecIntfIndex'
_K='agentCosQueueIndex'
_J='obsolete'
_I='Percent'
_H='agentCosQueueIntfIndex'
_G='read-only'
_F='Integer32'
_E='not-accessible'
_D='Unsigned32'
_C='FASTPATH-QOS-COS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPathQOS,=mibBuilder.importSymbols('FASTPATH-QOS-MIB','fastPathQOS')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathQOSCOS=ModuleIdentity((1,3,6,1,4,1,4413,1,1,3,3))
if mibBuilder.loadTexts:fastPathQOSCOS.setRevisions(('2010-03-17 00:00','2009-10-27 00:00','2009-01-06 00:00','2008-09-23 00:00','2007-12-19 00:00','2007-05-23 00:00','2004-05-03 00:00'))
class PercentByFives(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,5),ValueRangeConstraint(10,10),ValueRangeConstraint(15,15),ValueRangeConstraint(20,20),ValueRangeConstraint(25,25),ValueRangeConstraint(30,30),ValueRangeConstraint(35,35),ValueRangeConstraint(40,40),ValueRangeConstraint(45,45),ValueRangeConstraint(50,50),ValueRangeConstraint(55,55),ValueRangeConstraint(60,60),ValueRangeConstraint(65,65),ValueRangeConstraint(70,70),ValueRangeConstraint(75,75),ValueRangeConstraint(80,80),ValueRangeConstraint(85,85),ValueRangeConstraint(90,90),ValueRangeConstraint(95,95),ValueRangeConstraint(100,100))
class Percent(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class Sixteenths(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AgentCosMapCfgGroup_ObjectIdentity=ObjectIdentity
agentCosMapCfgGroup=_AgentCosMapCfgGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,3,3,1))
_AgentCosMapIpPrecTable_Object=MibTable
agentCosMapIpPrecTable=_AgentCosMapIpPrecTable_Object((1,3,6,1,4,1,4413,1,1,3,3,1,1))
if mibBuilder.loadTexts:agentCosMapIpPrecTable.setStatus(_A)
_AgentCosMapIpPrecEntry_Object=MibTableRow
agentCosMapIpPrecEntry=_AgentCosMapIpPrecEntry_Object((1,3,6,1,4,1,4413,1,1,3,3,1,1,1))
agentCosMapIpPrecEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:agentCosMapIpPrecEntry.setStatus(_A)
_AgentCosMapIpPrecIntfIndex_Type=InterfaceIndexOrZero
_AgentCosMapIpPrecIntfIndex_Object=MibTableColumn
agentCosMapIpPrecIntfIndex=_AgentCosMapIpPrecIntfIndex_Object((1,3,6,1,4,1,4413,1,1,3,3,1,1,1,1),_AgentCosMapIpPrecIntfIndex_Type())
agentCosMapIpPrecIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosMapIpPrecIntfIndex.setStatus(_A)
class _AgentCosMapIpPrecValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentCosMapIpPrecValue_Type.__name__=_D
_AgentCosMapIpPrecValue_Object=MibTableColumn
agentCosMapIpPrecValue=_AgentCosMapIpPrecValue_Object((1,3,6,1,4,1,4413,1,1,3,3,1,1,1,2),_AgentCosMapIpPrecValue_Type())
agentCosMapIpPrecValue.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosMapIpPrecValue.setStatus(_A)
class _AgentCosMapIpPrecTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentCosMapIpPrecTrafficClass_Type.__name__=_D
_AgentCosMapIpPrecTrafficClass_Object=MibTableColumn
agentCosMapIpPrecTrafficClass=_AgentCosMapIpPrecTrafficClass_Object((1,3,6,1,4,1,4413,1,1,3,3,1,1,1,3),_AgentCosMapIpPrecTrafficClass_Type())
agentCosMapIpPrecTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosMapIpPrecTrafficClass.setStatus(_A)
_AgentCosMapIpDscpTable_Object=MibTable
agentCosMapIpDscpTable=_AgentCosMapIpDscpTable_Object((1,3,6,1,4,1,4413,1,1,3,3,1,2))
if mibBuilder.loadTexts:agentCosMapIpDscpTable.setStatus(_A)
_AgentCosMapIpDscpEntry_Object=MibTableRow
agentCosMapIpDscpEntry=_AgentCosMapIpDscpEntry_Object((1,3,6,1,4,1,4413,1,1,3,3,1,2,1))
agentCosMapIpDscpEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:agentCosMapIpDscpEntry.setStatus(_A)
_AgentCosMapIpDscpIntfIndex_Type=InterfaceIndexOrZero
_AgentCosMapIpDscpIntfIndex_Object=MibTableColumn
agentCosMapIpDscpIntfIndex=_AgentCosMapIpDscpIntfIndex_Object((1,3,6,1,4,1,4413,1,1,3,3,1,2,1,1),_AgentCosMapIpDscpIntfIndex_Type())
agentCosMapIpDscpIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosMapIpDscpIntfIndex.setStatus(_A)
class _AgentCosMapIpDscpValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AgentCosMapIpDscpValue_Type.__name__=_D
_AgentCosMapIpDscpValue_Object=MibTableColumn
agentCosMapIpDscpValue=_AgentCosMapIpDscpValue_Object((1,3,6,1,4,1,4413,1,1,3,3,1,2,1,2),_AgentCosMapIpDscpValue_Type())
agentCosMapIpDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosMapIpDscpValue.setStatus(_A)
class _AgentCosMapIpDscpTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentCosMapIpDscpTrafficClass_Type.__name__=_D
_AgentCosMapIpDscpTrafficClass_Object=MibTableColumn
agentCosMapIpDscpTrafficClass=_AgentCosMapIpDscpTrafficClass_Object((1,3,6,1,4,1,4413,1,1,3,3,1,2,1,3),_AgentCosMapIpDscpTrafficClass_Type())
agentCosMapIpDscpTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosMapIpDscpTrafficClass.setStatus(_A)
_AgentCosMapIntfTrustTable_Object=MibTable
agentCosMapIntfTrustTable=_AgentCosMapIntfTrustTable_Object((1,3,6,1,4,1,4413,1,1,3,3,1,3))
if mibBuilder.loadTexts:agentCosMapIntfTrustTable.setStatus(_A)
_AgentCosMapIntfTrustEntry_Object=MibTableRow
agentCosMapIntfTrustEntry=_AgentCosMapIntfTrustEntry_Object((1,3,6,1,4,1,4413,1,1,3,3,1,3,1))
agentCosMapIntfTrustEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:agentCosMapIntfTrustEntry.setStatus(_A)
_AgentCosMapIntfTrustIntfIndex_Type=InterfaceIndexOrZero
_AgentCosMapIntfTrustIntfIndex_Object=MibTableColumn
agentCosMapIntfTrustIntfIndex=_AgentCosMapIntfTrustIntfIndex_Object((1,3,6,1,4,1,4413,1,1,3,3,1,3,1,1),_AgentCosMapIntfTrustIntfIndex_Type())
agentCosMapIntfTrustIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosMapIntfTrustIntfIndex.setStatus(_A)
class _AgentCosMapIntfTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('untrusted',1),('trustDot1p',2),('trustIpPrecedence',3),('trustIpDscp',4)))
_AgentCosMapIntfTrustMode_Type.__name__=_F
_AgentCosMapIntfTrustMode_Object=MibTableColumn
agentCosMapIntfTrustMode=_AgentCosMapIntfTrustMode_Object((1,3,6,1,4,1,4413,1,1,3,3,1,3,1,2),_AgentCosMapIntfTrustMode_Type())
agentCosMapIntfTrustMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosMapIntfTrustMode.setStatus(_A)
_AgentCosMapUntrustedTrafficClass_Type=Unsigned32
_AgentCosMapUntrustedTrafficClass_Object=MibTableColumn
agentCosMapUntrustedTrafficClass=_AgentCosMapUntrustedTrafficClass_Object((1,3,6,1,4,1,4413,1,1,3,3,1,3,1,3),_AgentCosMapUntrustedTrafficClass_Type())
agentCosMapUntrustedTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:agentCosMapUntrustedTrafficClass.setStatus(_A)
_AgentCosQueueCfgGroup_ObjectIdentity=ObjectIdentity
agentCosQueueCfgGroup=_AgentCosQueueCfgGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,3,3,2))
_AgentCosQueueNumQueuesPerPort_Type=Unsigned32
_AgentCosQueueNumQueuesPerPort_Object=MibScalar
agentCosQueueNumQueuesPerPort=_AgentCosQueueNumQueuesPerPort_Object((1,3,6,1,4,1,4413,1,1,3,3,2,1),_AgentCosQueueNumQueuesPerPort_Type())
agentCosQueueNumQueuesPerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:agentCosQueueNumQueuesPerPort.setStatus(_A)
_AgentCosQueueNumDropPrecedenceLevels_Type=Unsigned32
_AgentCosQueueNumDropPrecedenceLevels_Object=MibScalar
agentCosQueueNumDropPrecedenceLevels=_AgentCosQueueNumDropPrecedenceLevels_Object((1,3,6,1,4,1,4413,1,1,3,3,2,2),_AgentCosQueueNumDropPrecedenceLevels_Type())
agentCosQueueNumDropPrecedenceLevels.setMaxAccess(_G)
if mibBuilder.loadTexts:agentCosQueueNumDropPrecedenceLevels.setStatus(_A)
_AgentCosQueueControlTable_Object=MibTable
agentCosQueueControlTable=_AgentCosQueueControlTable_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3))
if mibBuilder.loadTexts:agentCosQueueControlTable.setStatus(_A)
_AgentCosQueueControlEntry_Object=MibTableRow
agentCosQueueControlEntry=_AgentCosQueueControlEntry_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3,1))
agentCosQueueControlEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:agentCosQueueControlEntry.setStatus(_A)
_AgentCosQueueIntfIndex_Type=InterfaceIndexOrZero
_AgentCosQueueIntfIndex_Object=MibTableColumn
agentCosQueueIntfIndex=_AgentCosQueueIntfIndex_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3,1,1),_AgentCosQueueIntfIndex_Type())
agentCosQueueIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosQueueIntfIndex.setStatus(_A)
class _AgentCosQueueIntfShapingRate_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AgentCosQueueIntfShapingRate_Type.__name__=_D
_AgentCosQueueIntfShapingRate_Object=MibTableColumn
agentCosQueueIntfShapingRate=_AgentCosQueueIntfShapingRate_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3,1,2),_AgentCosQueueIntfShapingRate_Type())
agentCosQueueIntfShapingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueIntfShapingRate.setStatus(_A)
class _AgentCosQueueMgmtTypeIntf_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('wred',2)))
_AgentCosQueueMgmtTypeIntf_Type.__name__=_F
_AgentCosQueueMgmtTypeIntf_Object=MibTableColumn
agentCosQueueMgmtTypeIntf=_AgentCosQueueMgmtTypeIntf_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3,1,3),_AgentCosQueueMgmtTypeIntf_Type())
agentCosQueueMgmtTypeIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtTypeIntf.setStatus(_A)
class _AgentCosQueueWredDecayExponent_Type(Unsigned32):defaultValue=9;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AgentCosQueueWredDecayExponent_Type.__name__=_D
_AgentCosQueueWredDecayExponent_Object=MibTableColumn
agentCosQueueWredDecayExponent=_AgentCosQueueWredDecayExponent_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3,1,4),_AgentCosQueueWredDecayExponent_Type())
agentCosQueueWredDecayExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueWredDecayExponent.setStatus(_A)
class _AgentCosQueueDefaultsRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentCosQueueDefaultsRestore_Type.__name__=_F
_AgentCosQueueDefaultsRestore_Object=MibTableColumn
agentCosQueueDefaultsRestore=_AgentCosQueueDefaultsRestore_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3,1,5),_AgentCosQueueDefaultsRestore_Type())
agentCosQueueDefaultsRestore.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueDefaultsRestore.setStatus(_A)
class _AgentCosQueueIntfShapingRateUnits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('percent',1),('kbps',2)))
_AgentCosQueueIntfShapingRateUnits_Type.__name__=_F
_AgentCosQueueIntfShapingRateUnits_Object=MibTableColumn
agentCosQueueIntfShapingRateUnits=_AgentCosQueueIntfShapingRateUnits_Object((1,3,6,1,4,1,4413,1,1,3,3,2,3,1,6),_AgentCosQueueIntfShapingRateUnits_Type())
agentCosQueueIntfShapingRateUnits.setMaxAccess(_G)
if mibBuilder.loadTexts:agentCosQueueIntfShapingRateUnits.setStatus(_A)
_AgentCosQueueTable_Object=MibTable
agentCosQueueTable=_AgentCosQueueTable_Object((1,3,6,1,4,1,4413,1,1,3,3,2,4))
if mibBuilder.loadTexts:agentCosQueueTable.setStatus(_A)
_AgentCosQueueEntry_Object=MibTableRow
agentCosQueueEntry=_AgentCosQueueEntry_Object((1,3,6,1,4,1,4413,1,1,3,3,2,4,1))
agentCosQueueEntry.setIndexNames((0,_C,_H),(0,_C,_K))
if mibBuilder.loadTexts:agentCosQueueEntry.setStatus(_A)
_AgentCosQueueIndex_Type=Unsigned32
_AgentCosQueueIndex_Object=MibTableColumn
agentCosQueueIndex=_AgentCosQueueIndex_Object((1,3,6,1,4,1,4413,1,1,3,3,2,4,1,1),_AgentCosQueueIndex_Type())
agentCosQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosQueueIndex.setStatus(_A)
class _AgentCosQueueSchedulerType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('weighted',2)))
_AgentCosQueueSchedulerType_Type.__name__=_F
_AgentCosQueueSchedulerType_Object=MibTableColumn
agentCosQueueSchedulerType=_AgentCosQueueSchedulerType_Object((1,3,6,1,4,1,4413,1,1,3,3,2,4,1,2),_AgentCosQueueSchedulerType_Type())
agentCosQueueSchedulerType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueSchedulerType.setStatus(_A)
class _AgentCosQueueMinBandwidth_Type(Percent):defaultValue=0
_AgentCosQueueMinBandwidth_Type.__name__=_I
_AgentCosQueueMinBandwidth_Object=MibTableColumn
agentCosQueueMinBandwidth=_AgentCosQueueMinBandwidth_Object((1,3,6,1,4,1,4413,1,1,3,3,2,4,1,3),_AgentCosQueueMinBandwidth_Type())
agentCosQueueMinBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMinBandwidth.setStatus(_A)
class _AgentCosQueueMaxBandwidth_Type(Percent):defaultValue=0
_AgentCosQueueMaxBandwidth_Type.__name__=_I
_AgentCosQueueMaxBandwidth_Object=MibTableColumn
agentCosQueueMaxBandwidth=_AgentCosQueueMaxBandwidth_Object((1,3,6,1,4,1,4413,1,1,3,3,2,4,1,4),_AgentCosQueueMaxBandwidth_Type())
agentCosQueueMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMaxBandwidth.setStatus(_A)
class _AgentCosQueueMgmtType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('wred',2)))
_AgentCosQueueMgmtType_Type.__name__=_F
_AgentCosQueueMgmtType_Object=MibTableColumn
agentCosQueueMgmtType=_AgentCosQueueMgmtType_Object((1,3,6,1,4,1,4413,1,1,3,3,2,4,1,5),_AgentCosQueueMgmtType_Type())
agentCosQueueMgmtType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtType.setStatus(_A)
_AgentCosQueueMgmtTable_Object=MibTable
agentCosQueueMgmtTable=_AgentCosQueueMgmtTable_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5))
if mibBuilder.loadTexts:agentCosQueueMgmtTable.setStatus(_A)
_AgentCosQueueMgmtEntry_Object=MibTableRow
agentCosQueueMgmtEntry=_AgentCosQueueMgmtEntry_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1))
agentCosQueueMgmtEntry.setIndexNames((0,_C,_H),(0,_C,_K),(0,_C,_R))
if mibBuilder.loadTexts:agentCosQueueMgmtEntry.setStatus(_A)
_AgentCosQueueDropPrecIndex_Type=Unsigned32
_AgentCosQueueDropPrecIndex_Object=MibTableColumn
agentCosQueueDropPrecIndex=_AgentCosQueueDropPrecIndex_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,1),_AgentCosQueueDropPrecIndex_Type())
agentCosQueueDropPrecIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCosQueueDropPrecIndex.setStatus(_A)
_AgentCosQueueMgmtTailDropThreshold_Type=Sixteenths
_AgentCosQueueMgmtTailDropThreshold_Object=MibTableColumn
agentCosQueueMgmtTailDropThreshold=_AgentCosQueueMgmtTailDropThreshold_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,2),_AgentCosQueueMgmtTailDropThreshold_Type())
agentCosQueueMgmtTailDropThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtTailDropThreshold.setStatus(_J)
_AgentCosQueueMgmtWredMinThreshold_Type=Sixteenths
_AgentCosQueueMgmtWredMinThreshold_Object=MibTableColumn
agentCosQueueMgmtWredMinThreshold=_AgentCosQueueMgmtWredMinThreshold_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,3),_AgentCosQueueMgmtWredMinThreshold_Type())
agentCosQueueMgmtWredMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtWredMinThreshold.setStatus(_J)
_AgentCosQueueMgmtWredMaxThreshold_Type=Sixteenths
_AgentCosQueueMgmtWredMaxThreshold_Object=MibTableColumn
agentCosQueueMgmtWredMaxThreshold=_AgentCosQueueMgmtWredMaxThreshold_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,4),_AgentCosQueueMgmtWredMaxThreshold_Type())
agentCosQueueMgmtWredMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtWredMaxThreshold.setStatus(_J)
class _AgentCosQueueMgmtWredDropProbScale_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AgentCosQueueMgmtWredDropProbScale_Type.__name__=_D
_AgentCosQueueMgmtWredDropProbScale_Object=MibTableColumn
agentCosQueueMgmtWredDropProbScale=_AgentCosQueueMgmtWredDropProbScale_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,5),_AgentCosQueueMgmtWredDropProbScale_Type())
agentCosQueueMgmtWredDropProbScale.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtWredDropProbScale.setStatus(_J)
_AgentCosQueueMgmtPercentTailDropThreshold_Type=Percent
_AgentCosQueueMgmtPercentTailDropThreshold_Object=MibTableColumn
agentCosQueueMgmtPercentTailDropThreshold=_AgentCosQueueMgmtPercentTailDropThreshold_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,6),_AgentCosQueueMgmtPercentTailDropThreshold_Type())
agentCosQueueMgmtPercentTailDropThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtPercentTailDropThreshold.setStatus(_A)
_AgentCosQueueMgmtPercentWredMinThreshold_Type=Percent
_AgentCosQueueMgmtPercentWredMinThreshold_Object=MibTableColumn
agentCosQueueMgmtPercentWredMinThreshold=_AgentCosQueueMgmtPercentWredMinThreshold_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,7),_AgentCosQueueMgmtPercentWredMinThreshold_Type())
agentCosQueueMgmtPercentWredMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtPercentWredMinThreshold.setStatus(_A)
_AgentCosQueueMgmtPercentWredMaxThreshold_Type=Percent
_AgentCosQueueMgmtPercentWredMaxThreshold_Object=MibTableColumn
agentCosQueueMgmtPercentWredMaxThreshold=_AgentCosQueueMgmtPercentWredMaxThreshold_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,8),_AgentCosQueueMgmtPercentWredMaxThreshold_Type())
agentCosQueueMgmtPercentWredMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtPercentWredMaxThreshold.setStatus(_A)
class _AgentCosQueueMgmtWredDropProbability_Type(Percent):defaultValue=10
_AgentCosQueueMgmtWredDropProbability_Type.__name__=_I
_AgentCosQueueMgmtWredDropProbability_Object=MibTableColumn
agentCosQueueMgmtWredDropProbability=_AgentCosQueueMgmtWredDropProbability_Object((1,3,6,1,4,1,4413,1,1,3,3,2,5,1,9),_AgentCosQueueMgmtWredDropProbability_Type())
agentCosQueueMgmtWredDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCosQueueMgmtWredDropProbability.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PercentByFives':PercentByFives,_I:Percent,'Sixteenths':Sixteenths,'fastPathQOSCOS':fastPathQOSCOS,'agentCosMapCfgGroup':agentCosMapCfgGroup,'agentCosMapIpPrecTable':agentCosMapIpPrecTable,'agentCosMapIpPrecEntry':agentCosMapIpPrecEntry,_L:agentCosMapIpPrecIntfIndex,_M:agentCosMapIpPrecValue,'agentCosMapIpPrecTrafficClass':agentCosMapIpPrecTrafficClass,'agentCosMapIpDscpTable':agentCosMapIpDscpTable,'agentCosMapIpDscpEntry':agentCosMapIpDscpEntry,_N:agentCosMapIpDscpIntfIndex,_O:agentCosMapIpDscpValue,'agentCosMapIpDscpTrafficClass':agentCosMapIpDscpTrafficClass,'agentCosMapIntfTrustTable':agentCosMapIntfTrustTable,'agentCosMapIntfTrustEntry':agentCosMapIntfTrustEntry,_P:agentCosMapIntfTrustIntfIndex,'agentCosMapIntfTrustMode':agentCosMapIntfTrustMode,'agentCosMapUntrustedTrafficClass':agentCosMapUntrustedTrafficClass,'agentCosQueueCfgGroup':agentCosQueueCfgGroup,'agentCosQueueNumQueuesPerPort':agentCosQueueNumQueuesPerPort,'agentCosQueueNumDropPrecedenceLevels':agentCosQueueNumDropPrecedenceLevels,'agentCosQueueControlTable':agentCosQueueControlTable,'agentCosQueueControlEntry':agentCosQueueControlEntry,_H:agentCosQueueIntfIndex,'agentCosQueueIntfShapingRate':agentCosQueueIntfShapingRate,'agentCosQueueMgmtTypeIntf':agentCosQueueMgmtTypeIntf,'agentCosQueueWredDecayExponent':agentCosQueueWredDecayExponent,'agentCosQueueDefaultsRestore':agentCosQueueDefaultsRestore,'agentCosQueueIntfShapingRateUnits':agentCosQueueIntfShapingRateUnits,'agentCosQueueTable':agentCosQueueTable,'agentCosQueueEntry':agentCosQueueEntry,_K:agentCosQueueIndex,'agentCosQueueSchedulerType':agentCosQueueSchedulerType,'agentCosQueueMinBandwidth':agentCosQueueMinBandwidth,'agentCosQueueMaxBandwidth':agentCosQueueMaxBandwidth,'agentCosQueueMgmtType':agentCosQueueMgmtType,'agentCosQueueMgmtTable':agentCosQueueMgmtTable,'agentCosQueueMgmtEntry':agentCosQueueMgmtEntry,_R:agentCosQueueDropPrecIndex,'agentCosQueueMgmtTailDropThreshold':agentCosQueueMgmtTailDropThreshold,'agentCosQueueMgmtWredMinThreshold':agentCosQueueMgmtWredMinThreshold,'agentCosQueueMgmtWredMaxThreshold':agentCosQueueMgmtWredMaxThreshold,'agentCosQueueMgmtWredDropProbScale':agentCosQueueMgmtWredDropProbScale,'agentCosQueueMgmtPercentTailDropThreshold':agentCosQueueMgmtPercentTailDropThreshold,'agentCosQueueMgmtPercentWredMinThreshold':agentCosQueueMgmtPercentWredMinThreshold,'agentCosQueueMgmtPercentWredMaxThreshold':agentCosQueueMgmtPercentWredMaxThreshold,'agentCosQueueMgmtWredDropProbability':agentCosQueueMgmtWredDropProbability})