_Y='synchronization'
_X='aggregation'
_W='lacpTimeout'
_V='lacpActivity'
_U='expired'
_T='defaulted'
_S='distributing'
_R='collecting'
_Q='TruthValue'
_P='Bits'
_O='adGenPortTrapIdentifier'
_N='ADTRAN-GENPORT-MIB'
_M='notAvailable'
_L='sysName'
_K='SNMPv2-MIB'
_J='adTrapInformSeqNum'
_I='ADTRAN-GENTRAPINFORM-MIB'
_H='adGenSlotInfoIndex'
_G='ADTRAN-GENSLOT-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols(_N,_O)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_G,_H)
adTa5kLinkAggregation,adTa5kLinkAggregationID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adTa5kLinkAggregation','adTa5kLinkAggregationID')
adTrapInformSeqNum,=mibBuilder.importSymbols(_I,_J)
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_Q)
adTa5kLinkAggregationModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,33,1))
if mibBuilder.loadTexts:adTa5kLinkAggregationModuleIdentity.setRevisions(('2014-07-23 00:00','2013-09-25 00:00','2011-11-30 19:18','2011-10-26 18:00'))
_AdTa5kLinkAggregationAlarmPrefix_ObjectIdentity=ObjectIdentity
adTa5kLinkAggregationAlarmPrefix=_AdTa5kLinkAggregationAlarmPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,33,1))
_AdTa5kLinkAggregationAlarms_ObjectIdentity=ObjectIdentity
adTa5kLinkAggregationAlarms=_AdTa5kLinkAggregationAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,33,1,0))
_AdTa5kLinkAggregationProvisioning_ObjectIdentity=ObjectIdentity
adTa5kLinkAggregationProvisioning=_AdTa5kLinkAggregationProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,33,2))
_AdTa5kLinkAggLACPProvTable_Object=MibTable
adTa5kLinkAggLACPProvTable=_AdTa5kLinkAggLACPProvTable_Object((1,3,6,1,4,1,664,5,67,1,33,2,1))
if mibBuilder.loadTexts:adTa5kLinkAggLACPProvTable.setStatus(_A)
_AdTa5kLinkAggLACPProvEntry_Object=MibTableRow
adTa5kLinkAggLACPProvEntry=_AdTa5kLinkAggLACPProvEntry_Object((1,3,6,1,4,1,664,5,67,1,33,2,1,1))
adTa5kLinkAggLACPProvEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kLinkAggLACPProvEntry.setStatus(_A)
class _AdTa5kLinkAggLACPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('active',2),('passive',3)))
_AdTa5kLinkAggLACPMode_Type.__name__=_B
_AdTa5kLinkAggLACPMode_Object=MibTableColumn
adTa5kLinkAggLACPMode=_AdTa5kLinkAggLACPMode_Object((1,3,6,1,4,1,664,5,67,1,33,2,1,1,1),_AdTa5kLinkAggLACPMode_Type())
adTa5kLinkAggLACPMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPMode.setStatus(_A)
class _AdTa5kLinkAggLACPGrammar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standbyAggregation',1),('noStandbyAggregation',2)))
_AdTa5kLinkAggLACPGrammar_Type.__name__=_B
_AdTa5kLinkAggLACPGrammar_Object=MibTableColumn
adTa5kLinkAggLACPGrammar=_AdTa5kLinkAggLACPGrammar_Object((1,3,6,1,4,1,664,5,67,1,33,2,1,1,2),_AdTa5kLinkAggLACPGrammar_Type())
adTa5kLinkAggLACPGrammar.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPGrammar.setStatus(_A)
_AdTa5kLinkAggAlarmProvTable_Object=MibTable
adTa5kLinkAggAlarmProvTable=_AdTa5kLinkAggAlarmProvTable_Object((1,3,6,1,4,1,664,5,67,1,33,2,2))
if mibBuilder.loadTexts:adTa5kLinkAggAlarmProvTable.setStatus(_A)
_AdTa5kLinkAggAlarmProvEntry_Object=MibTableRow
adTa5kLinkAggAlarmProvEntry=_AdTa5kLinkAggAlarmProvEntry_Object((1,3,6,1,4,1,664,5,67,1,33,2,2,1))
adTa5kLinkAggAlarmProvEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kLinkAggAlarmProvEntry.setStatus(_A)
class _AdTa5kLinkAggLACPTimeOutAlarmEnable_Type(TruthValue):defaultValue=1
_AdTa5kLinkAggLACPTimeOutAlarmEnable_Type.__name__=_Q
_AdTa5kLinkAggLACPTimeOutAlarmEnable_Object=MibTableColumn
adTa5kLinkAggLACPTimeOutAlarmEnable=_AdTa5kLinkAggLACPTimeOutAlarmEnable_Object((1,3,6,1,4,1,664,5,67,1,33,2,2,1,1),_AdTa5kLinkAggLACPTimeOutAlarmEnable_Type())
adTa5kLinkAggLACPTimeOutAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPTimeOutAlarmEnable.setStatus(_A)
class _AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Type(TruthValue):defaultValue=1
_AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Type.__name__=_Q
_AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Object=MibTableColumn
adTa5kLinkAggMinimumActiveLnkAlarmEnable=_AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Object((1,3,6,1,4,1,664,5,67,1,33,2,2,1,2),_AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Type())
adTa5kLinkAggMinimumActiveLnkAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggMinimumActiveLnkAlarmEnable.setStatus(_A)
_AdTa5kLinkAggLACPSlotProvTable_Object=MibTable
adTa5kLinkAggLACPSlotProvTable=_AdTa5kLinkAggLACPSlotProvTable_Object((1,3,6,1,4,1,664,5,67,1,33,2,3))
if mibBuilder.loadTexts:adTa5kLinkAggLACPSlotProvTable.setStatus(_A)
_AdTa5kLinkAggLACPSlotProvEntry_Object=MibTableRow
adTa5kLinkAggLACPSlotProvEntry=_AdTa5kLinkAggLACPSlotProvEntry_Object((1,3,6,1,4,1,664,5,67,1,33,2,3,1))
adTa5kLinkAggLACPSlotProvEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adTa5kLinkAggLACPSlotProvEntry.setStatus(_A)
class _AdTa5kLinkAggLACPResponseMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reporterOnly',1),('interactive',2)))
_AdTa5kLinkAggLACPResponseMode_Type.__name__=_B
_AdTa5kLinkAggLACPResponseMode_Object=MibTableColumn
adTa5kLinkAggLACPResponseMode=_AdTa5kLinkAggLACPResponseMode_Object((1,3,6,1,4,1,664,5,67,1,33,2,3,1,1),_AdTa5kLinkAggLACPResponseMode_Type())
adTa5kLinkAggLACPResponseMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPResponseMode.setStatus(_A)
class _AdTa5kLinkAggLACPSlotSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,35535))
_AdTa5kLinkAggLACPSlotSystemPriority_Type.__name__=_B
_AdTa5kLinkAggLACPSlotSystemPriority_Object=MibTableColumn
adTa5kLinkAggLACPSlotSystemPriority=_AdTa5kLinkAggLACPSlotSystemPriority_Object((1,3,6,1,4,1,664,5,67,1,33,2,3,1,2),_AdTa5kLinkAggLACPSlotSystemPriority_Type())
adTa5kLinkAggLACPSlotSystemPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPSlotSystemPriority.setStatus(_A)
_AdTa5kLinkAggregationPerformance_ObjectIdentity=ObjectIdentity
adTa5kLinkAggregationPerformance=_AdTa5kLinkAggregationPerformance_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,33,3))
_AdTa5kLinkAggLACPPortStatsTable_Object=MibTable
adTa5kLinkAggLACPPortStatsTable=_AdTa5kLinkAggLACPPortStatsTable_Object((1,3,6,1,4,1,664,5,67,1,33,3,1))
if mibBuilder.loadTexts:adTa5kLinkAggLACPPortStatsTable.setStatus(_A)
_AdTa5kLinkAggLACPPortStatsEntry_Object=MibTableRow
adTa5kLinkAggLACPPortStatsEntry=_AdTa5kLinkAggLACPPortStatsEntry_Object((1,3,6,1,4,1,664,5,67,1,33,3,1,1))
adTa5kLinkAggLACPPortStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kLinkAggLACPPortStatsEntry.setStatus(_A)
_AdTa5kLinkAggPortStatsLACPDUsTx_Type=Gauge32
_AdTa5kLinkAggPortStatsLACPDUsTx_Object=MibTableColumn
adTa5kLinkAggPortStatsLACPDUsTx=_AdTa5kLinkAggPortStatsLACPDUsTx_Object((1,3,6,1,4,1,664,5,67,1,33,3,1,1,1),_AdTa5kLinkAggPortStatsLACPDUsTx_Type())
adTa5kLinkAggPortStatsLACPDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggPortStatsLACPDUsTx.setStatus(_A)
_AdTa5kLinkAggPortStatsLACPDUsRx_Type=Gauge32
_AdTa5kLinkAggPortStatsLACPDUsRx_Object=MibTableColumn
adTa5kLinkAggPortStatsLACPDUsRx=_AdTa5kLinkAggPortStatsLACPDUsRx_Object((1,3,6,1,4,1,664,5,67,1,33,3,1,1,2),_AdTa5kLinkAggPortStatsLACPDUsRx_Type())
adTa5kLinkAggPortStatsLACPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggPortStatsLACPDUsRx.setStatus(_A)
_AdTa5kLinkAggPortStatsMarkerPDUsRx_Type=Gauge32
_AdTa5kLinkAggPortStatsMarkerPDUsRx_Object=MibTableColumn
adTa5kLinkAggPortStatsMarkerPDUsRx=_AdTa5kLinkAggPortStatsMarkerPDUsRx_Object((1,3,6,1,4,1,664,5,67,1,33,3,1,1,3),_AdTa5kLinkAggPortStatsMarkerPDUsRx_Type())
adTa5kLinkAggPortStatsMarkerPDUsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggPortStatsMarkerPDUsRx.setStatus(_A)
_AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Type=Gauge32
_AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Object=MibTableColumn
adTa5kLinkAggPortStatsMarkerResponsePDUsTx=_AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Object((1,3,6,1,4,1,664,5,67,1,33,3,1,1,4),_AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Type())
adTa5kLinkAggPortStatsMarkerResponsePDUsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggPortStatsMarkerResponsePDUsTx.setStatus(_A)
_AdTa5kLinkAggregationStatus_ObjectIdentity=ObjectIdentity
adTa5kLinkAggregationStatus=_AdTa5kLinkAggregationStatus_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,33,4))
_AdTa5kLinkAggLACPStatusTable_Object=MibTable
adTa5kLinkAggLACPStatusTable=_AdTa5kLinkAggLACPStatusTable_Object((1,3,6,1,4,1,664,5,67,1,33,4,1))
if mibBuilder.loadTexts:adTa5kLinkAggLACPStatusTable.setStatus(_A)
_AdTa5kLinkAggLACPStatusEntry_Object=MibTableRow
adTa5kLinkAggLACPStatusEntry=_AdTa5kLinkAggLACPStatusEntry_Object((1,3,6,1,4,1,664,5,67,1,33,4,1,1))
adTa5kLinkAggLACPStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kLinkAggLACPStatusEntry.setStatus(_A)
_AdTa5kLinkAggLACPSystemID_Type=MacAddress
_AdTa5kLinkAggLACPSystemID_Object=MibTableColumn
adTa5kLinkAggLACPSystemID=_AdTa5kLinkAggLACPSystemID_Object((1,3,6,1,4,1,664,5,67,1,33,4,1,1,1),_AdTa5kLinkAggLACPSystemID_Type())
adTa5kLinkAggLACPSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPSystemID.setStatus(_A)
class _AdTa5kLinkAggLACPSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPSystemPriority_Type.__name__=_B
_AdTa5kLinkAggLACPSystemPriority_Object=MibTableColumn
adTa5kLinkAggLACPSystemPriority=_AdTa5kLinkAggLACPSystemPriority_Object((1,3,6,1,4,1,664,5,67,1,33,4,1,1,2),_AdTa5kLinkAggLACPSystemPriority_Type())
adTa5kLinkAggLACPSystemPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPSystemPriority.setStatus(_A)
_AdTa5kLinkAggLACPPortStatusTable_Object=MibTable
adTa5kLinkAggLACPPortStatusTable=_AdTa5kLinkAggLACPPortStatusTable_Object((1,3,6,1,4,1,664,5,67,1,33,4,2))
if mibBuilder.loadTexts:adTa5kLinkAggLACPPortStatusTable.setStatus(_A)
_AdTa5kLinkAggLACPPortStatusEntry_Object=MibTableRow
adTa5kLinkAggLACPPortStatusEntry=_AdTa5kLinkAggLACPPortStatusEntry_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1))
adTa5kLinkAggLACPPortStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kLinkAggLACPPortStatusEntry.setStatus(_A)
class _AdTa5kLinkAggLACPActorPortState_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_R,4),(_S,5),(_T,6),(_U,7)))
_AdTa5kLinkAggLACPActorPortState_Type.__name__=_P
_AdTa5kLinkAggLACPActorPortState_Object=MibTableColumn
adTa5kLinkAggLACPActorPortState=_AdTa5kLinkAggLACPActorPortState_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,1),_AdTa5kLinkAggLACPActorPortState_Type())
adTa5kLinkAggLACPActorPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPActorPortState.setStatus(_A)
class _AdTa5kLinkAggLACPActorPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPActorPortID_Type.__name__=_B
_AdTa5kLinkAggLACPActorPortID_Object=MibTableColumn
adTa5kLinkAggLACPActorPortID=_AdTa5kLinkAggLACPActorPortID_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,2),_AdTa5kLinkAggLACPActorPortID_Type())
adTa5kLinkAggLACPActorPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPActorPortID.setStatus(_A)
class _AdTa5kLinkAggLACPActorPortKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPActorPortKey_Type.__name__=_B
_AdTa5kLinkAggLACPActorPortKey_Object=MibTableColumn
adTa5kLinkAggLACPActorPortKey=_AdTa5kLinkAggLACPActorPortKey_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,3),_AdTa5kLinkAggLACPActorPortKey_Type())
adTa5kLinkAggLACPActorPortKey.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPActorPortKey.setStatus(_A)
class _AdTa5kLinkAggLACPActorPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPActorPortPriority_Type.__name__=_B
_AdTa5kLinkAggLACPActorPortPriority_Object=MibTableColumn
adTa5kLinkAggLACPActorPortPriority=_AdTa5kLinkAggLACPActorPortPriority_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,4),_AdTa5kLinkAggLACPActorPortPriority_Type())
adTa5kLinkAggLACPActorPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPActorPortPriority.setStatus(_A)
class _AdTa5kLinkAggLACPPartnerPortState_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_R,4),(_S,5),(_T,6),(_U,7)))
_AdTa5kLinkAggLACPPartnerPortState_Type.__name__=_P
_AdTa5kLinkAggLACPPartnerPortState_Object=MibTableColumn
adTa5kLinkAggLACPPartnerPortState=_AdTa5kLinkAggLACPPartnerPortState_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,5),_AdTa5kLinkAggLACPPartnerPortState_Type())
adTa5kLinkAggLACPPartnerPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPPartnerPortState.setStatus(_A)
class _AdTa5kLinkAggLACPPartnerPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPPartnerPortID_Type.__name__=_B
_AdTa5kLinkAggLACPPartnerPortID_Object=MibTableColumn
adTa5kLinkAggLACPPartnerPortID=_AdTa5kLinkAggLACPPartnerPortID_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,6),_AdTa5kLinkAggLACPPartnerPortID_Type())
adTa5kLinkAggLACPPartnerPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPPartnerPortID.setStatus(_A)
class _AdTa5kLinkAggLACPPartnerPortKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPPartnerPortKey_Type.__name__=_B
_AdTa5kLinkAggLACPPartnerPortKey_Object=MibTableColumn
adTa5kLinkAggLACPPartnerPortKey=_AdTa5kLinkAggLACPPartnerPortKey_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,7),_AdTa5kLinkAggLACPPartnerPortKey_Type())
adTa5kLinkAggLACPPartnerPortKey.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPPartnerPortKey.setStatus(_A)
class _AdTa5kLinkAggLACPPartnerPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPPartnerPortPriority_Type.__name__=_B
_AdTa5kLinkAggLACPPartnerPortPriority_Object=MibTableColumn
adTa5kLinkAggLACPPartnerPortPriority=_AdTa5kLinkAggLACPPartnerPortPriority_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,8),_AdTa5kLinkAggLACPPartnerPortPriority_Type())
adTa5kLinkAggLACPPartnerPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kLinkAggLACPPartnerPortPriority.setStatus(_A)
_AdTa5kLinkAggLACPPartnerPortSystemID_Type=MacAddress
_AdTa5kLinkAggLACPPartnerPortSystemID_Object=MibTableColumn
adTa5kLinkAggLACPPartnerPortSystemID=_AdTa5kLinkAggLACPPartnerPortSystemID_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,9),_AdTa5kLinkAggLACPPartnerPortSystemID_Type())
adTa5kLinkAggLACPPartnerPortSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPPartnerPortSystemID.setStatus(_A)
class _AdTa5kLinkAggLACPPartnerPortSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdTa5kLinkAggLACPPartnerPortSystemPriority_Type.__name__=_B
_AdTa5kLinkAggLACPPartnerPortSystemPriority_Object=MibTableColumn
adTa5kLinkAggLACPPartnerPortSystemPriority=_AdTa5kLinkAggLACPPartnerPortSystemPriority_Object((1,3,6,1,4,1,664,5,67,1,33,4,2,1,10),_AdTa5kLinkAggLACPPartnerPortSystemPriority_Type())
adTa5kLinkAggLACPPartnerPortSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPPartnerPortSystemPriority.setStatus(_A)
_AdTa5kLinkAggLACPStateMachineTable_Object=MibTable
adTa5kLinkAggLACPStateMachineTable=_AdTa5kLinkAggLACPStateMachineTable_Object((1,3,6,1,4,1,664,5,67,1,33,4,3))
if mibBuilder.loadTexts:adTa5kLinkAggLACPStateMachineTable.setStatus(_A)
_AdTa5kLinkAggLACPStateMachineEntry_Object=MibTableRow
adTa5kLinkAggLACPStateMachineEntry=_AdTa5kLinkAggLACPStateMachineEntry_Object((1,3,6,1,4,1,664,5,67,1,33,4,3,1))
adTa5kLinkAggLACPStateMachineEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kLinkAggLACPStateMachineEntry.setStatus(_A)
class _AdTa5kLinkAggLACPSelectedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('unselected',0),('selected',1),('standby',2),(_M,255)))
_AdTa5kLinkAggLACPSelectedState_Type.__name__=_B
_AdTa5kLinkAggLACPSelectedState_Object=MibTableColumn
adTa5kLinkAggLACPSelectedState=_AdTa5kLinkAggLACPSelectedState_Object((1,3,6,1,4,1,664,5,67,1,33,4,3,1,1),_AdTa5kLinkAggLACPSelectedState_Type())
adTa5kLinkAggLACPSelectedState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPSelectedState.setStatus(_A)
class _AdTa5kLinkAggLACPReceiveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*(('initialize',0),('portDisabled',1),(_U,2),('lacpDisabled',3),(_T,4),(_A,5),(_M,255)))
_AdTa5kLinkAggLACPReceiveState_Type.__name__=_B
_AdTa5kLinkAggLACPReceiveState_Object=MibTableColumn
adTa5kLinkAggLACPReceiveState=_AdTa5kLinkAggLACPReceiveState_Object((1,3,6,1,4,1,664,5,67,1,33,4,3,1,2),_AdTa5kLinkAggLACPReceiveState_Type())
adTa5kLinkAggLACPReceiveState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPReceiveState.setStatus(_A)
class _AdTa5kLinkAggLACPPeriodicTxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,255)));namedValues=NamedValues(*(('noPeriodic',0),('fastPeriodic',1),('slowPeriodic',2),('periodicTx',3),(_M,255)))
_AdTa5kLinkAggLACPPeriodicTxState_Type.__name__=_B
_AdTa5kLinkAggLACPPeriodicTxState_Object=MibTableColumn
adTa5kLinkAggLACPPeriodicTxState=_AdTa5kLinkAggLACPPeriodicTxState_Object((1,3,6,1,4,1,664,5,67,1,33,4,3,1,3),_AdTa5kLinkAggLACPPeriodicTxState_Type())
adTa5kLinkAggLACPPeriodicTxState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPPeriodicTxState.setStatus(_A)
class _AdTa5kLinkAggLACPMuxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,255)));namedValues=NamedValues(*(('detached',0),('waiting',1),('attached',2),(_R,3),(_S,4),(_M,255)))
_AdTa5kLinkAggLACPMuxState_Type.__name__=_B
_AdTa5kLinkAggLACPMuxState_Object=MibTableColumn
adTa5kLinkAggLACPMuxState=_AdTa5kLinkAggLACPMuxState_Object((1,3,6,1,4,1,664,5,67,1,33,4,3,1,4),_AdTa5kLinkAggLACPMuxState_Type())
adTa5kLinkAggLACPMuxState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kLinkAggLACPMuxState.setStatus(_A)
adTa5kSmLACPTimeOutClear=NotificationType((1,3,6,1,4,1,664,5,67,1,33,1,0,2))
adTa5kSmLACPTimeOutClear.setObjects(*((_I,_J),(_K,_L),(_G,_H),(_N,_O)))
if mibBuilder.loadTexts:adTa5kSmLACPTimeOutClear.setStatus(_A)
adTa5kSmLACPTimeOutActive=NotificationType((1,3,6,1,4,1,664,5,67,1,33,1,0,3))
adTa5kSmLACPTimeOutActive.setObjects(*((_I,_J),(_K,_L),(_G,_H),(_N,_O)))
if mibBuilder.loadTexts:adTa5kSmLACPTimeOutActive.setStatus(_A)
adTa5kSmUnderMiniActiveLnkClear=NotificationType((1,3,6,1,4,1,664,5,67,1,33,1,0,4))
adTa5kSmUnderMiniActiveLnkClear.setObjects(*((_I,_J),(_K,_L),(_G,_H),(_E,_F)))
if mibBuilder.loadTexts:adTa5kSmUnderMiniActiveLnkClear.setStatus(_A)
adTa5kSmUnderMiniActiveLnk=NotificationType((1,3,6,1,4,1,664,5,67,1,33,1,0,5))
adTa5kSmUnderMiniActiveLnk.setObjects(*((_I,_J),(_K,_L),(_G,_H),(_E,_F)))
if mibBuilder.loadTexts:adTa5kSmUnderMiniActiveLnk.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-LINK-AGGREGATION-MIB',**{'adTa5kLinkAggregationAlarmPrefix':adTa5kLinkAggregationAlarmPrefix,'adTa5kLinkAggregationAlarms':adTa5kLinkAggregationAlarms,'adTa5kSmLACPTimeOutClear':adTa5kSmLACPTimeOutClear,'adTa5kSmLACPTimeOutActive':adTa5kSmLACPTimeOutActive,'adTa5kSmUnderMiniActiveLnkClear':adTa5kSmUnderMiniActiveLnkClear,'adTa5kSmUnderMiniActiveLnk':adTa5kSmUnderMiniActiveLnk,'adTa5kLinkAggregationProvisioning':adTa5kLinkAggregationProvisioning,'adTa5kLinkAggLACPProvTable':adTa5kLinkAggLACPProvTable,'adTa5kLinkAggLACPProvEntry':adTa5kLinkAggLACPProvEntry,'adTa5kLinkAggLACPMode':adTa5kLinkAggLACPMode,'adTa5kLinkAggLACPGrammar':adTa5kLinkAggLACPGrammar,'adTa5kLinkAggAlarmProvTable':adTa5kLinkAggAlarmProvTable,'adTa5kLinkAggAlarmProvEntry':adTa5kLinkAggAlarmProvEntry,'adTa5kLinkAggLACPTimeOutAlarmEnable':adTa5kLinkAggLACPTimeOutAlarmEnable,'adTa5kLinkAggMinimumActiveLnkAlarmEnable':adTa5kLinkAggMinimumActiveLnkAlarmEnable,'adTa5kLinkAggLACPSlotProvTable':adTa5kLinkAggLACPSlotProvTable,'adTa5kLinkAggLACPSlotProvEntry':adTa5kLinkAggLACPSlotProvEntry,'adTa5kLinkAggLACPResponseMode':adTa5kLinkAggLACPResponseMode,'adTa5kLinkAggLACPSlotSystemPriority':adTa5kLinkAggLACPSlotSystemPriority,'adTa5kLinkAggregationPerformance':adTa5kLinkAggregationPerformance,'adTa5kLinkAggLACPPortStatsTable':adTa5kLinkAggLACPPortStatsTable,'adTa5kLinkAggLACPPortStatsEntry':adTa5kLinkAggLACPPortStatsEntry,'adTa5kLinkAggPortStatsLACPDUsTx':adTa5kLinkAggPortStatsLACPDUsTx,'adTa5kLinkAggPortStatsLACPDUsRx':adTa5kLinkAggPortStatsLACPDUsRx,'adTa5kLinkAggPortStatsMarkerPDUsRx':adTa5kLinkAggPortStatsMarkerPDUsRx,'adTa5kLinkAggPortStatsMarkerResponsePDUsTx':adTa5kLinkAggPortStatsMarkerResponsePDUsTx,'adTa5kLinkAggregationStatus':adTa5kLinkAggregationStatus,'adTa5kLinkAggLACPStatusTable':adTa5kLinkAggLACPStatusTable,'adTa5kLinkAggLACPStatusEntry':adTa5kLinkAggLACPStatusEntry,'adTa5kLinkAggLACPSystemID':adTa5kLinkAggLACPSystemID,'adTa5kLinkAggLACPSystemPriority':adTa5kLinkAggLACPSystemPriority,'adTa5kLinkAggLACPPortStatusTable':adTa5kLinkAggLACPPortStatusTable,'adTa5kLinkAggLACPPortStatusEntry':adTa5kLinkAggLACPPortStatusEntry,'adTa5kLinkAggLACPActorPortState':adTa5kLinkAggLACPActorPortState,'adTa5kLinkAggLACPActorPortID':adTa5kLinkAggLACPActorPortID,'adTa5kLinkAggLACPActorPortKey':adTa5kLinkAggLACPActorPortKey,'adTa5kLinkAggLACPActorPortPriority':adTa5kLinkAggLACPActorPortPriority,'adTa5kLinkAggLACPPartnerPortState':adTa5kLinkAggLACPPartnerPortState,'adTa5kLinkAggLACPPartnerPortID':adTa5kLinkAggLACPPartnerPortID,'adTa5kLinkAggLACPPartnerPortKey':adTa5kLinkAggLACPPartnerPortKey,'adTa5kLinkAggLACPPartnerPortPriority':adTa5kLinkAggLACPPartnerPortPriority,'adTa5kLinkAggLACPPartnerPortSystemID':adTa5kLinkAggLACPPartnerPortSystemID,'adTa5kLinkAggLACPPartnerPortSystemPriority':adTa5kLinkAggLACPPartnerPortSystemPriority,'adTa5kLinkAggLACPStateMachineTable':adTa5kLinkAggLACPStateMachineTable,'adTa5kLinkAggLACPStateMachineEntry':adTa5kLinkAggLACPStateMachineEntry,'adTa5kLinkAggLACPSelectedState':adTa5kLinkAggLACPSelectedState,'adTa5kLinkAggLACPReceiveState':adTa5kLinkAggLACPReceiveState,'adTa5kLinkAggLACPPeriodicTxState':adTa5kLinkAggLACPPeriodicTxState,'adTa5kLinkAggLACPMuxState':adTa5kLinkAggLACPMuxState,'adTa5kLinkAggregationModuleIdentity':adTa5kLinkAggregationModuleIdentity})