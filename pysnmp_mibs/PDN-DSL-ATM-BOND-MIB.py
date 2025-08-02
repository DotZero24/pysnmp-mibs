_Ag='pdnDslAtmBondAlarmConfAturThreshRateGroup'
_Af='pdnDslAtmBondAlarmConfAtucThreshRateGroup'
_Ae='pdnDslAtmBondAlarmConfProfileGroup'
_Ad='pdnDslATmBondAsmRxStatusGroup'
_Ac='pdnDslAtmBondTrafficCapGroup'
_Ab='pdnDslAtmBondUASGroup'
_Aa='pdnDslAtmBondFailCountGroup'
_AZ='pdnDslAtmBondPerfFailReasonGroup'
_AY='pdnDslAtmBondRxCellLossGroup'
_AX='pdnDslAtmBondRunTimeGroup'
_AW='pdnDslAtmBondDateAndTimeGroup'
_AV='pdnDslAtmBondInvMappingGroup'
_AU='pdnDslAtmBondIndexMappingGroup'
_AT='pdnDslAtmBondGroupStatusNotifyEnabledGroup'
_AS='pdnDslAtmBondDiffDelayGroup'
_AR='pdnDslAtmBondMinRateGroup'
_AQ='pdnDslAtmBondMaxRateGroup'
_AP='pdnDslAtmBondNotificationsGroup'
_AO='pdnDslAtmBondPerfBondGroupStatusGroup'
_AN='pdnDslAtmBondPerfAggDataRateGroup'
_AM='pdnDslAtmBondMappingGroup'
_AL='pdnDslAtmBondGroup'
_AK='pdnDslAtmBondGroupStatusChange'
_AJ='pdnDslAtmBondAturRateChange'
_AI='pdnDslAtmBondAtucRateChange'
_AH='pdnDslAtmBondAlarmConfAturThreshRateDown'
_AG='pdnDslAtmBondAlarmConfAturThreshRateUp'
_AF='pdnDslAtmBondAlarmConfAtucThreshRateDown'
_AE='pdnDslAtmBondAlarmConfAtucThreshRateUp'
_AD='pdnDslAtmBondAlarmConfNbrRefs'
_AC='pdnDslAtmBondAlarmConfRowStatus'
_AB='pdnDslAtmBondGroupAlarmConfProfileName'
_AA='pdnDslAtmBondLinkAturAsmRxStatus'
_A9='pdnDslAtmBondLinkAtucAsmRxStatus'
_A8='pdnDslAtmBondLinkAturTxLinkStatus'
_A7='pdnDslAtmBondLinkAtucTxLinkStatus'
_A6='pdnDslAtmBondLinkAturRxLinkStatus'
_A5='pdnDslAtmBondLinkAtucRxLinkStatus'
_A4='pdnDslAtmBond1DayIntervalUAS'
_A3='pdnDslAtmBond15MinIntervalUAS'
_A2='pdnDslAtmBondPerfUAS'
_A1='pdnDslAtmBond1DayIntervalFailCount'
_A0='pdnDslAtmBond15MinIntervalFailCount'
_z='pdnDslAtmBondPerfFailCount'
_y='pdnDslAtmBond1DayIntervalAturRxCellLoss'
_x='pdnDslAtmBond1DayIntervalAtucRxCellLoss'
_w='pdnDslAtmBond15MinIntervalAturRxCellLoss'
_v='pdnDslAtmBond15MinIntervalAtucRxCellLoss'
_u='pdnDslAtmBondPerfAturRxCellLoss'
_t='pdnDslAtmBondPerfAtucRxCellLoss'
_s='pdnDslAtmBond1DayIntervalRunTime'
_r='pdnDslAtmBond15MinIntervalRunTime'
_q='pdnDslAtmBondPerfRunTime'
_p='pdnDslAtmBond1DayIntervalStartDateAndTime'
_o='pdnDslAtmBond15MinIntervalStartDateAndTime'
_n='pdnDslAtmBondInvMappingBearerNbr'
_m='pdnDslAtmBondGroupIndexMappingIndex'
_l='pdnDslAtmBondMappingGroupIndex'
_k='pdnDslAtmBondMappingRowStatus'
_j='pdnDslAtmBondGroupStatusNotifyEnabled'
_i='pdnDslAtmBondGroupAturDiffDelay'
_h='pdnDslAtmBondGroupAtucDiffDelay'
_g='pdnDslAtmBondGroupAturMinNetDataRate'
_f='pdnDslAtmBondGroupAtucMinNetDataRate'
_e='pdnDslAtmBondGroupAturMaxNetDataRate'
_d='pdnDslAtmBondGroupAtucMaxNetDataRate'
_c='pdnDslAtmBondGroupID'
_b='pdnDslAtmBondGroupNbrRefs'
_a='pdnDslAtmBondGroupRowStatus'
_Z='pdnDslAtmBondNbrOfGroups'
_Y='pdnDslAtmBondNextGroupIndex'
_X='pdnDslAtmBondAlarmConfProfileName'
_W='pdnDslAtmBond1DayIntervalNumber'
_V='pdnDslAtmBond15MinIntervalNumber'
_U='seconds'
_T='pdnDslAtmBondBearerNbr'
_S='milliseconds'
_R='pdnDslAtmBondPerfFailReason'
_Q='pdnDslAtmBondPerfGroupStatus'
_P='pdnDslAtmBondPerfPrevAturNetDataRate'
_O='pdnDslAtmBondPerfPrevAtucNetDataRate'
_N='pdnDslAtmBondPerfCurrAturNetDataRate'
_M='pdnDslAtmBondPerfCurrAtucNetDataRate'
_L='SnmpAdminString'
_K='pdnDslAtmBondDslIfIndex'
_J='Integer32'
_I='pdnDslAtmBondGroupIfIndex'
_H='not-accessible'
_G='Unsigned32'
_F='pdnDslAtmBondGroupIndex'
_E='bps'
_D='read-create'
_C='read-only'
_B='PDN-DSL-ATM-BOND-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TruthValue')
pdnDslAtmBondMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,33))
if mibBuilder.loadTexts:pdnDslAtmBondMIB.setRevisions(('2005-08-03 00:00','2005-08-01 00:00','2005-07-26 00:00','2005-06-07 00:00'))
class PdnDslAtmBondGroupIndexTC(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class PdnDslAtmBondGroupIdentityTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class PdnDslAtmBondGroupBearerNumberTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
class PdnDslAtmBondLinkStatusAsmTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notProvisioned',1),('shouldNotBeUsed',2),('acceptableToCarryBondedTraffic',3),('selectedToCarryBondedTraffic',4)))
class PdnDslAtmBondAsmRxStatusTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receivedASM',1),('notReceivedASM',2)))
class PdnDslAtmBondGroupDataRateTC(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
class PdnDslAtmBondGroupDiffDelayTolTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class PdnDslAtmBondGroupStatusTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operational',1),('unavailable',2)))
class PdnDslAtmBondGroupFailReasonTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notApplicable',1),('unknown',2),('atucMinDataRateNotMet',3),('aturMinDataRateNotMet',4),('atucDiffDelayExceeded',5),('aturDiffDelayExceeded',6)))
_PdnDslAtmBondNotifications_ObjectIdentity=ObjectIdentity
pdnDslAtmBondNotifications=_PdnDslAtmBondNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,0))
_PdnDslAtmBondObjects_ObjectIdentity=ObjectIdentity
pdnDslAtmBondObjects=_PdnDslAtmBondObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,1))
_PdnDslAtmBondNextGroupIndex_Type=TestAndIncr
_PdnDslAtmBondNextGroupIndex_Object=MibScalar
pdnDslAtmBondNextGroupIndex=_PdnDslAtmBondNextGroupIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,1),_PdnDslAtmBondNextGroupIndex_Type())
pdnDslAtmBondNextGroupIndex.setMaxAccess('read-write')
if mibBuilder.loadTexts:pdnDslAtmBondNextGroupIndex.setStatus(_A)
class _PdnDslAtmBondNbrOfGroups_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDslAtmBondNbrOfGroups_Type.__name__=_G
_PdnDslAtmBondNbrOfGroups_Object=MibScalar
pdnDslAtmBondNbrOfGroups=_PdnDslAtmBondNbrOfGroups_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,2),_PdnDslAtmBondNbrOfGroups_Type())
pdnDslAtmBondNbrOfGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondNbrOfGroups.setStatus(_A)
_PdnDslAtmBondGroupTable_Object=MibTable
pdnDslAtmBondGroupTable=_PdnDslAtmBondGroupTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3))
if mibBuilder.loadTexts:pdnDslAtmBondGroupTable.setStatus(_A)
_PdnDslAtmBondGroupEntry_Object=MibTableRow
pdnDslAtmBondGroupEntry=_PdnDslAtmBondGroupEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1))
pdnDslAtmBondGroupEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:pdnDslAtmBondGroupEntry.setStatus(_A)
_PdnDslAtmBondGroupIndex_Type=PdnDslAtmBondGroupIndexTC
_PdnDslAtmBondGroupIndex_Object=MibTableColumn
pdnDslAtmBondGroupIndex=_PdnDslAtmBondGroupIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,1),_PdnDslAtmBondGroupIndex_Type())
pdnDslAtmBondGroupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnDslAtmBondGroupIndex.setStatus(_A)
_PdnDslAtmBondGroupRowStatus_Type=RowStatus
_PdnDslAtmBondGroupRowStatus_Object=MibTableColumn
pdnDslAtmBondGroupRowStatus=_PdnDslAtmBondGroupRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,2),_PdnDslAtmBondGroupRowStatus_Type())
pdnDslAtmBondGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupRowStatus.setStatus(_A)
class _PdnDslAtmBondGroupNbrRefs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDslAtmBondGroupNbrRefs_Type.__name__=_G
_PdnDslAtmBondGroupNbrRefs_Object=MibTableColumn
pdnDslAtmBondGroupNbrRefs=_PdnDslAtmBondGroupNbrRefs_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,3),_PdnDslAtmBondGroupNbrRefs_Type())
pdnDslAtmBondGroupNbrRefs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondGroupNbrRefs.setStatus(_A)
_PdnDslAtmBondGroupIfIndex_Type=InterfaceIndex
_PdnDslAtmBondGroupIfIndex_Object=MibTableColumn
pdnDslAtmBondGroupIfIndex=_PdnDslAtmBondGroupIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,4),_PdnDslAtmBondGroupIfIndex_Type())
pdnDslAtmBondGroupIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondGroupIfIndex.setStatus(_A)
_PdnDslAtmBondGroupID_Type=PdnDslAtmBondGroupIdentityTC
_PdnDslAtmBondGroupID_Object=MibTableColumn
pdnDslAtmBondGroupID=_PdnDslAtmBondGroupID_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,5),_PdnDslAtmBondGroupID_Type())
pdnDslAtmBondGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupID.setStatus(_A)
class _PdnDslAtmBondGroupAlarmConfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,32))
_PdnDslAtmBondGroupAlarmConfProfileName_Type.__name__=_L
_PdnDslAtmBondGroupAlarmConfProfileName_Object=MibTableColumn
pdnDslAtmBondGroupAlarmConfProfileName=_PdnDslAtmBondGroupAlarmConfProfileName_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,6),_PdnDslAtmBondGroupAlarmConfProfileName_Type())
pdnDslAtmBondGroupAlarmConfProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAlarmConfProfileName.setStatus(_A)
_PdnDslAtmBondGroupAtucMaxNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAtucMaxNetDataRate_Object=MibTableColumn
pdnDslAtmBondGroupAtucMaxNetDataRate=_PdnDslAtmBondGroupAtucMaxNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,7),_PdnDslAtmBondGroupAtucMaxNetDataRate_Type())
pdnDslAtmBondGroupAtucMaxNetDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAtucMaxNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAtucMaxNetDataRate.setUnits(_E)
_PdnDslAtmBondGroupAturMaxNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAturMaxNetDataRate_Object=MibTableColumn
pdnDslAtmBondGroupAturMaxNetDataRate=_PdnDslAtmBondGroupAturMaxNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,8),_PdnDslAtmBondGroupAturMaxNetDataRate_Type())
pdnDslAtmBondGroupAturMaxNetDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAturMaxNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAturMaxNetDataRate.setUnits(_E)
_PdnDslAtmBondGroupAtucMinNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAtucMinNetDataRate_Object=MibTableColumn
pdnDslAtmBondGroupAtucMinNetDataRate=_PdnDslAtmBondGroupAtucMinNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,9),_PdnDslAtmBondGroupAtucMinNetDataRate_Type())
pdnDslAtmBondGroupAtucMinNetDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAtucMinNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAtucMinNetDataRate.setUnits(_E)
_PdnDslAtmBondGroupAturMinNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAturMinNetDataRate_Object=MibTableColumn
pdnDslAtmBondGroupAturMinNetDataRate=_PdnDslAtmBondGroupAturMinNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,10),_PdnDslAtmBondGroupAturMinNetDataRate_Type())
pdnDslAtmBondGroupAturMinNetDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAturMinNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAturMinNetDataRate.setUnits(_E)
_PdnDslAtmBondGroupAtucDiffDelay_Type=PdnDslAtmBondGroupDiffDelayTolTC
_PdnDslAtmBondGroupAtucDiffDelay_Object=MibTableColumn
pdnDslAtmBondGroupAtucDiffDelay=_PdnDslAtmBondGroupAtucDiffDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,11),_PdnDslAtmBondGroupAtucDiffDelay_Type())
pdnDslAtmBondGroupAtucDiffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAtucDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAtucDiffDelay.setUnits(_S)
_PdnDslAtmBondGroupAturDiffDelay_Type=PdnDslAtmBondGroupDiffDelayTolTC
_PdnDslAtmBondGroupAturDiffDelay_Object=MibTableColumn
pdnDslAtmBondGroupAturDiffDelay=_PdnDslAtmBondGroupAturDiffDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,12),_PdnDslAtmBondGroupAturDiffDelay_Type())
pdnDslAtmBondGroupAturDiffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAturDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondGroupAturDiffDelay.setUnits(_S)
_PdnDslAtmBondGroupStatusNotifyEnabled_Type=TruthValue
_PdnDslAtmBondGroupStatusNotifyEnabled_Object=MibTableColumn
pdnDslAtmBondGroupStatusNotifyEnabled=_PdnDslAtmBondGroupStatusNotifyEnabled_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,3,1,13),_PdnDslAtmBondGroupStatusNotifyEnabled_Type())
pdnDslAtmBondGroupStatusNotifyEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondGroupStatusNotifyEnabled.setStatus(_A)
_PdnDslAtmBondMappingTable_Object=MibTable
pdnDslAtmBondMappingTable=_PdnDslAtmBondMappingTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,4))
if mibBuilder.loadTexts:pdnDslAtmBondMappingTable.setStatus(_A)
_PdnDslAtmBondMappingEntry_Object=MibTableRow
pdnDslAtmBondMappingEntry=_PdnDslAtmBondMappingEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,4,1))
pdnDslAtmBondMappingEntry.setIndexNames((0,_B,_K),(0,_B,_T))
if mibBuilder.loadTexts:pdnDslAtmBondMappingEntry.setStatus(_A)
_PdnDslAtmBondDslIfIndex_Type=InterfaceIndex
_PdnDslAtmBondDslIfIndex_Object=MibTableColumn
pdnDslAtmBondDslIfIndex=_PdnDslAtmBondDslIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,4,1,1),_PdnDslAtmBondDslIfIndex_Type())
pdnDslAtmBondDslIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnDslAtmBondDslIfIndex.setStatus(_A)
_PdnDslAtmBondBearerNbr_Type=PdnDslAtmBondGroupBearerNumberTC
_PdnDslAtmBondBearerNbr_Object=MibTableColumn
pdnDslAtmBondBearerNbr=_PdnDslAtmBondBearerNbr_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,4,1,2),_PdnDslAtmBondBearerNbr_Type())
pdnDslAtmBondBearerNbr.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnDslAtmBondBearerNbr.setStatus(_A)
_PdnDslAtmBondMappingRowStatus_Type=RowStatus
_PdnDslAtmBondMappingRowStatus_Object=MibTableColumn
pdnDslAtmBondMappingRowStatus=_PdnDslAtmBondMappingRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,4,1,3),_PdnDslAtmBondMappingRowStatus_Type())
pdnDslAtmBondMappingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondMappingRowStatus.setStatus(_A)
_PdnDslAtmBondMappingGroupIndex_Type=PdnDslAtmBondGroupIndexTC
_PdnDslAtmBondMappingGroupIndex_Object=MibTableColumn
pdnDslAtmBondMappingGroupIndex=_PdnDslAtmBondMappingGroupIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,4,1,4),_PdnDslAtmBondMappingGroupIndex_Type())
pdnDslAtmBondMappingGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondMappingGroupIndex.setStatus(_A)
_PdnDslAtmBondGroupIndexMappingTable_Object=MibTable
pdnDslAtmBondGroupIndexMappingTable=_PdnDslAtmBondGroupIndexMappingTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,5))
if mibBuilder.loadTexts:pdnDslAtmBondGroupIndexMappingTable.setStatus(_A)
_PdnDslAtmBondGroupIndexMappingEntry_Object=MibTableRow
pdnDslAtmBondGroupIndexMappingEntry=_PdnDslAtmBondGroupIndexMappingEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,5,1))
pdnDslAtmBondGroupIndexMappingEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:pdnDslAtmBondGroupIndexMappingEntry.setStatus(_A)
_PdnDslAtmBondGroupIndexMappingIndex_Type=PdnDslAtmBondGroupIndexTC
_PdnDslAtmBondGroupIndexMappingIndex_Object=MibTableColumn
pdnDslAtmBondGroupIndexMappingIndex=_PdnDslAtmBondGroupIndexMappingIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,5,1,1),_PdnDslAtmBondGroupIndexMappingIndex_Type())
pdnDslAtmBondGroupIndexMappingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondGroupIndexMappingIndex.setStatus(_A)
_PdnDslAtmBondGroupInvMappingTable_Object=MibTable
pdnDslAtmBondGroupInvMappingTable=_PdnDslAtmBondGroupInvMappingTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,6))
if mibBuilder.loadTexts:pdnDslAtmBondGroupInvMappingTable.setStatus(_A)
_PdnDslAtmBondGroupInvMappingEntry_Object=MibTableRow
pdnDslAtmBondGroupInvMappingEntry=_PdnDslAtmBondGroupInvMappingEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,6,1))
pdnDslAtmBondGroupInvMappingEntry.setIndexNames((0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:pdnDslAtmBondGroupInvMappingEntry.setStatus(_A)
_PdnDslAtmBondInvMappingBearerNbr_Type=PdnDslAtmBondGroupBearerNumberTC
_PdnDslAtmBondInvMappingBearerNbr_Object=MibTableColumn
pdnDslAtmBondInvMappingBearerNbr=_PdnDslAtmBondInvMappingBearerNbr_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,6,1,1),_PdnDslAtmBondInvMappingBearerNbr_Type())
pdnDslAtmBondInvMappingBearerNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondInvMappingBearerNbr.setStatus(_A)
_PdnDslAtmBondPerfTable_Object=MibTable
pdnDslAtmBondPerfTable=_PdnDslAtmBondPerfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7))
if mibBuilder.loadTexts:pdnDslAtmBondPerfTable.setStatus(_A)
_PdnDslAtmBondPerfEntry_Object=MibTableRow
pdnDslAtmBondPerfEntry=_PdnDslAtmBondPerfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1))
pdnDslAtmBondPerfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:pdnDslAtmBondPerfEntry.setStatus(_A)
_PdnDslAtmBondPerfCurrAtucNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfCurrAtucNetDataRate_Object=MibTableColumn
pdnDslAtmBondPerfCurrAtucNetDataRate=_PdnDslAtmBondPerfCurrAtucNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,1),_PdnDslAtmBondPerfCurrAtucNetDataRate_Type())
pdnDslAtmBondPerfCurrAtucNetDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfCurrAtucNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondPerfCurrAtucNetDataRate.setUnits(_E)
_PdnDslAtmBondPerfCurrAturNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfCurrAturNetDataRate_Object=MibTableColumn
pdnDslAtmBondPerfCurrAturNetDataRate=_PdnDslAtmBondPerfCurrAturNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,2),_PdnDslAtmBondPerfCurrAturNetDataRate_Type())
pdnDslAtmBondPerfCurrAturNetDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfCurrAturNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondPerfCurrAturNetDataRate.setUnits(_E)
_PdnDslAtmBondPerfPrevAtucNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfPrevAtucNetDataRate_Object=MibTableColumn
pdnDslAtmBondPerfPrevAtucNetDataRate=_PdnDslAtmBondPerfPrevAtucNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,3),_PdnDslAtmBondPerfPrevAtucNetDataRate_Type())
pdnDslAtmBondPerfPrevAtucNetDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfPrevAtucNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondPerfPrevAtucNetDataRate.setUnits(_E)
_PdnDslAtmBondPerfPrevAturNetDataRate_Type=PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfPrevAturNetDataRate_Object=MibTableColumn
pdnDslAtmBondPerfPrevAturNetDataRate=_PdnDslAtmBondPerfPrevAturNetDataRate_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,4),_PdnDslAtmBondPerfPrevAturNetDataRate_Type())
pdnDslAtmBondPerfPrevAturNetDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfPrevAturNetDataRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondPerfPrevAturNetDataRate.setUnits(_E)
_PdnDslAtmBondPerfGroupStatus_Type=PdnDslAtmBondGroupStatusTC
_PdnDslAtmBondPerfGroupStatus_Object=MibTableColumn
pdnDslAtmBondPerfGroupStatus=_PdnDslAtmBondPerfGroupStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,5),_PdnDslAtmBondPerfGroupStatus_Type())
pdnDslAtmBondPerfGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfGroupStatus.setStatus(_A)
_PdnDslAtmBondPerfFailReason_Type=PdnDslAtmBondGroupFailReasonTC
_PdnDslAtmBondPerfFailReason_Object=MibTableColumn
pdnDslAtmBondPerfFailReason=_PdnDslAtmBondPerfFailReason_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,6),_PdnDslAtmBondPerfFailReason_Type())
pdnDslAtmBondPerfFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfFailReason.setStatus(_A)
_PdnDslAtmBondPerfFailCount_Type=Counter32
_PdnDslAtmBondPerfFailCount_Object=MibTableColumn
pdnDslAtmBondPerfFailCount=_PdnDslAtmBondPerfFailCount_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,7),_PdnDslAtmBondPerfFailCount_Type())
pdnDslAtmBondPerfFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfFailCount.setStatus(_A)
_PdnDslAtmBondPerfRunTime_Type=Counter32
_PdnDslAtmBondPerfRunTime_Object=MibTableColumn
pdnDslAtmBondPerfRunTime=_PdnDslAtmBondPerfRunTime_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,8),_PdnDslAtmBondPerfRunTime_Type())
pdnDslAtmBondPerfRunTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfRunTime.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondPerfRunTime.setUnits(_U)
_PdnDslAtmBondPerfUAS_Type=Counter32
_PdnDslAtmBondPerfUAS_Object=MibTableColumn
pdnDslAtmBondPerfUAS=_PdnDslAtmBondPerfUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,9),_PdnDslAtmBondPerfUAS_Type())
pdnDslAtmBondPerfUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfUAS.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondPerfUAS.setUnits(_U)
_PdnDslAtmBondPerfAtucRxCellLoss_Type=Counter32
_PdnDslAtmBondPerfAtucRxCellLoss_Object=MibTableColumn
pdnDslAtmBondPerfAtucRxCellLoss=_PdnDslAtmBondPerfAtucRxCellLoss_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,10),_PdnDslAtmBondPerfAtucRxCellLoss_Type())
pdnDslAtmBondPerfAtucRxCellLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfAtucRxCellLoss.setStatus(_A)
_PdnDslAtmBondPerfAturRxCellLoss_Type=Counter32
_PdnDslAtmBondPerfAturRxCellLoss_Object=MibTableColumn
pdnDslAtmBondPerfAturRxCellLoss=_PdnDslAtmBondPerfAturRxCellLoss_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,7,1,11),_PdnDslAtmBondPerfAturRxCellLoss_Type())
pdnDslAtmBondPerfAturRxCellLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondPerfAturRxCellLoss.setStatus(_A)
_PdnDslAtmBond15MinIntervalTable_Object=MibTable
pdnDslAtmBond15MinIntervalTable=_PdnDslAtmBond15MinIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8))
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalTable.setStatus(_A)
_PdnDslAtmBond15MinIntervalEntry_Object=MibTableRow
pdnDslAtmBond15MinIntervalEntry=_PdnDslAtmBond15MinIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1))
pdnDslAtmBond15MinIntervalEntry.setIndexNames((0,_B,_F),(0,_B,_V))
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalEntry.setStatus(_A)
class _PdnDslAtmBond15MinIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_PdnDslAtmBond15MinIntervalNumber_Type.__name__=_G
_PdnDslAtmBond15MinIntervalNumber_Object=MibTableColumn
pdnDslAtmBond15MinIntervalNumber=_PdnDslAtmBond15MinIntervalNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1,1),_PdnDslAtmBond15MinIntervalNumber_Type())
pdnDslAtmBond15MinIntervalNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalNumber.setStatus(_A)
_PdnDslAtmBond15MinIntervalStartDateAndTime_Type=DateAndTime
_PdnDslAtmBond15MinIntervalStartDateAndTime_Object=MibTableColumn
pdnDslAtmBond15MinIntervalStartDateAndTime=_PdnDslAtmBond15MinIntervalStartDateAndTime_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1,2),_PdnDslAtmBond15MinIntervalStartDateAndTime_Type())
pdnDslAtmBond15MinIntervalStartDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalStartDateAndTime.setStatus(_A)
_PdnDslAtmBond15MinIntervalFailCount_Type=Counter32
_PdnDslAtmBond15MinIntervalFailCount_Object=MibTableColumn
pdnDslAtmBond15MinIntervalFailCount=_PdnDslAtmBond15MinIntervalFailCount_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1,3),_PdnDslAtmBond15MinIntervalFailCount_Type())
pdnDslAtmBond15MinIntervalFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalFailCount.setStatus(_A)
_PdnDslAtmBond15MinIntervalRunTime_Type=Counter32
_PdnDslAtmBond15MinIntervalRunTime_Object=MibTableColumn
pdnDslAtmBond15MinIntervalRunTime=_PdnDslAtmBond15MinIntervalRunTime_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1,4),_PdnDslAtmBond15MinIntervalRunTime_Type())
pdnDslAtmBond15MinIntervalRunTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalRunTime.setStatus(_A)
_PdnDslAtmBond15MinIntervalUAS_Type=Counter32
_PdnDslAtmBond15MinIntervalUAS_Object=MibTableColumn
pdnDslAtmBond15MinIntervalUAS=_PdnDslAtmBond15MinIntervalUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1,5),_PdnDslAtmBond15MinIntervalUAS_Type())
pdnDslAtmBond15MinIntervalUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalUAS.setStatus(_A)
_PdnDslAtmBond15MinIntervalAtucRxCellLoss_Type=Counter32
_PdnDslAtmBond15MinIntervalAtucRxCellLoss_Object=MibTableColumn
pdnDslAtmBond15MinIntervalAtucRxCellLoss=_PdnDslAtmBond15MinIntervalAtucRxCellLoss_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1,6),_PdnDslAtmBond15MinIntervalAtucRxCellLoss_Type())
pdnDslAtmBond15MinIntervalAtucRxCellLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalAtucRxCellLoss.setStatus(_A)
_PdnDslAtmBond15MinIntervalAturRxCellLoss_Type=Counter32
_PdnDslAtmBond15MinIntervalAturRxCellLoss_Object=MibTableColumn
pdnDslAtmBond15MinIntervalAturRxCellLoss=_PdnDslAtmBond15MinIntervalAturRxCellLoss_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,8,1,7),_PdnDslAtmBond15MinIntervalAturRxCellLoss_Type())
pdnDslAtmBond15MinIntervalAturRxCellLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond15MinIntervalAturRxCellLoss.setStatus(_A)
_PdnDslAtmBond1DayIntervalTable_Object=MibTable
pdnDslAtmBond1DayIntervalTable=_PdnDslAtmBond1DayIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9))
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalTable.setStatus(_A)
_PdnDslAtmBond1DayIntervalEntry_Object=MibTableRow
pdnDslAtmBond1DayIntervalEntry=_PdnDslAtmBond1DayIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1))
pdnDslAtmBond1DayIntervalEntry.setIndexNames((0,_B,_F),(0,_B,_W))
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalEntry.setStatus(_A)
class _PdnDslAtmBond1DayIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PdnDslAtmBond1DayIntervalNumber_Type.__name__=_G
_PdnDslAtmBond1DayIntervalNumber_Object=MibTableColumn
pdnDslAtmBond1DayIntervalNumber=_PdnDslAtmBond1DayIntervalNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1,1),_PdnDslAtmBond1DayIntervalNumber_Type())
pdnDslAtmBond1DayIntervalNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalNumber.setStatus(_A)
_PdnDslAtmBond1DayIntervalStartDateAndTime_Type=DateAndTime
_PdnDslAtmBond1DayIntervalStartDateAndTime_Object=MibTableColumn
pdnDslAtmBond1DayIntervalStartDateAndTime=_PdnDslAtmBond1DayIntervalStartDateAndTime_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1,2),_PdnDslAtmBond1DayIntervalStartDateAndTime_Type())
pdnDslAtmBond1DayIntervalStartDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalStartDateAndTime.setStatus(_A)
_PdnDslAtmBond1DayIntervalFailCount_Type=Counter32
_PdnDslAtmBond1DayIntervalFailCount_Object=MibTableColumn
pdnDslAtmBond1DayIntervalFailCount=_PdnDslAtmBond1DayIntervalFailCount_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1,3),_PdnDslAtmBond1DayIntervalFailCount_Type())
pdnDslAtmBond1DayIntervalFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalFailCount.setStatus(_A)
_PdnDslAtmBond1DayIntervalRunTime_Type=Counter32
_PdnDslAtmBond1DayIntervalRunTime_Object=MibTableColumn
pdnDslAtmBond1DayIntervalRunTime=_PdnDslAtmBond1DayIntervalRunTime_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1,4),_PdnDslAtmBond1DayIntervalRunTime_Type())
pdnDslAtmBond1DayIntervalRunTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalRunTime.setStatus(_A)
_PdnDslAtmBond1DayIntervalUAS_Type=Counter32
_PdnDslAtmBond1DayIntervalUAS_Object=MibTableColumn
pdnDslAtmBond1DayIntervalUAS=_PdnDslAtmBond1DayIntervalUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1,5),_PdnDslAtmBond1DayIntervalUAS_Type())
pdnDslAtmBond1DayIntervalUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalUAS.setStatus(_A)
_PdnDslAtmBond1DayIntervalAtucRxCellLoss_Type=Counter32
_PdnDslAtmBond1DayIntervalAtucRxCellLoss_Object=MibTableColumn
pdnDslAtmBond1DayIntervalAtucRxCellLoss=_PdnDslAtmBond1DayIntervalAtucRxCellLoss_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1,6),_PdnDslAtmBond1DayIntervalAtucRxCellLoss_Type())
pdnDslAtmBond1DayIntervalAtucRxCellLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalAtucRxCellLoss.setStatus(_A)
_PdnDslAtmBond1DayIntervalAturRxCellLoss_Type=Counter32
_PdnDslAtmBond1DayIntervalAturRxCellLoss_Object=MibTableColumn
pdnDslAtmBond1DayIntervalAturRxCellLoss=_PdnDslAtmBond1DayIntervalAturRxCellLoss_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,9,1,7),_PdnDslAtmBond1DayIntervalAturRxCellLoss_Type())
pdnDslAtmBond1DayIntervalAturRxCellLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBond1DayIntervalAturRxCellLoss.setStatus(_A)
_PdnDslAtmBondLinkTable_Object=MibTable
pdnDslAtmBondLinkTable=_PdnDslAtmBondLinkTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10))
if mibBuilder.loadTexts:pdnDslAtmBondLinkTable.setStatus(_A)
_PdnDslAtmBondLinkEntry_Object=MibTableRow
pdnDslAtmBondLinkEntry=_PdnDslAtmBondLinkEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10,1))
pdnDslAtmBondLinkEntry.setIndexNames((0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:pdnDslAtmBondLinkEntry.setStatus(_A)
_PdnDslAtmBondLinkAtucRxLinkStatus_Type=PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAtucRxLinkStatus_Object=MibTableColumn
pdnDslAtmBondLinkAtucRxLinkStatus=_PdnDslAtmBondLinkAtucRxLinkStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10,1,1),_PdnDslAtmBondLinkAtucRxLinkStatus_Type())
pdnDslAtmBondLinkAtucRxLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondLinkAtucRxLinkStatus.setStatus(_A)
_PdnDslAtmBondLinkAturRxLinkStatus_Type=PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAturRxLinkStatus_Object=MibTableColumn
pdnDslAtmBondLinkAturRxLinkStatus=_PdnDslAtmBondLinkAturRxLinkStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10,1,2),_PdnDslAtmBondLinkAturRxLinkStatus_Type())
pdnDslAtmBondLinkAturRxLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondLinkAturRxLinkStatus.setStatus(_A)
_PdnDslAtmBondLinkAtucTxLinkStatus_Type=PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAtucTxLinkStatus_Object=MibTableColumn
pdnDslAtmBondLinkAtucTxLinkStatus=_PdnDslAtmBondLinkAtucTxLinkStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10,1,3),_PdnDslAtmBondLinkAtucTxLinkStatus_Type())
pdnDslAtmBondLinkAtucTxLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondLinkAtucTxLinkStatus.setStatus(_A)
_PdnDslAtmBondLinkAturTxLinkStatus_Type=PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAturTxLinkStatus_Object=MibTableColumn
pdnDslAtmBondLinkAturTxLinkStatus=_PdnDslAtmBondLinkAturTxLinkStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10,1,4),_PdnDslAtmBondLinkAturTxLinkStatus_Type())
pdnDslAtmBondLinkAturTxLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondLinkAturTxLinkStatus.setStatus(_A)
_PdnDslAtmBondLinkAtucAsmRxStatus_Type=PdnDslAtmBondAsmRxStatusTC
_PdnDslAtmBondLinkAtucAsmRxStatus_Object=MibTableColumn
pdnDslAtmBondLinkAtucAsmRxStatus=_PdnDslAtmBondLinkAtucAsmRxStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10,1,5),_PdnDslAtmBondLinkAtucAsmRxStatus_Type())
pdnDslAtmBondLinkAtucAsmRxStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondLinkAtucAsmRxStatus.setStatus(_A)
_PdnDslAtmBondLinkAturAsmRxStatus_Type=PdnDslAtmBondAsmRxStatusTC
_PdnDslAtmBondLinkAturAsmRxStatus_Object=MibTableColumn
pdnDslAtmBondLinkAturAsmRxStatus=_PdnDslAtmBondLinkAturAsmRxStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,10,1,6),_PdnDslAtmBondLinkAturAsmRxStatus_Type())
pdnDslAtmBondLinkAturAsmRxStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondLinkAturAsmRxStatus.setStatus(_A)
_PdnDslAtmBondAlarmConfProfileTable_Object=MibTable
pdnDslAtmBondAlarmConfProfileTable=_PdnDslAtmBondAlarmConfProfileTable_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11))
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfProfileTable.setStatus(_A)
_PdnDslAtmBondAlarmConfProfileEntry_Object=MibTableRow
pdnDslAtmBondAlarmConfProfileEntry=_PdnDslAtmBondAlarmConfProfileEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1))
pdnDslAtmBondAlarmConfProfileEntry.setIndexNames((1,_B,_X))
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfProfileEntry.setStatus(_A)
class _PdnDslAtmBondAlarmConfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnDslAtmBondAlarmConfProfileName_Type.__name__=_L
_PdnDslAtmBondAlarmConfProfileName_Object=MibTableColumn
pdnDslAtmBondAlarmConfProfileName=_PdnDslAtmBondAlarmConfProfileName_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1,1),_PdnDslAtmBondAlarmConfProfileName_Type())
pdnDslAtmBondAlarmConfProfileName.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfProfileName.setStatus(_A)
_PdnDslAtmBondAlarmConfRowStatus_Type=RowStatus
_PdnDslAtmBondAlarmConfRowStatus_Object=MibTableColumn
pdnDslAtmBondAlarmConfRowStatus=_PdnDslAtmBondAlarmConfRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1,2),_PdnDslAtmBondAlarmConfRowStatus_Type())
pdnDslAtmBondAlarmConfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfRowStatus.setStatus(_A)
class _PdnDslAtmBondAlarmConfNbrRefs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDslAtmBondAlarmConfNbrRefs_Type.__name__=_G
_PdnDslAtmBondAlarmConfNbrRefs_Object=MibTableColumn
pdnDslAtmBondAlarmConfNbrRefs=_PdnDslAtmBondAlarmConfNbrRefs_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1,3),_PdnDslAtmBondAlarmConfNbrRefs_Type())
pdnDslAtmBondAlarmConfNbrRefs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfNbrRefs.setStatus(_A)
class _PdnDslAtmBondAlarmConfAtucThreshRateUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDslAtmBondAlarmConfAtucThreshRateUp_Type.__name__=_J
_PdnDslAtmBondAlarmConfAtucThreshRateUp_Object=MibTableColumn
pdnDslAtmBondAlarmConfAtucThreshRateUp=_PdnDslAtmBondAlarmConfAtucThreshRateUp_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1,4),_PdnDslAtmBondAlarmConfAtucThreshRateUp_Type())
pdnDslAtmBondAlarmConfAtucThreshRateUp.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAtucThreshRateUp.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAtucThreshRateUp.setUnits(_E)
class _PdnDslAtmBondAlarmConfAturThreshRateUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDslAtmBondAlarmConfAturThreshRateUp_Type.__name__=_J
_PdnDslAtmBondAlarmConfAturThreshRateUp_Object=MibTableColumn
pdnDslAtmBondAlarmConfAturThreshRateUp=_PdnDslAtmBondAlarmConfAturThreshRateUp_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1,5),_PdnDslAtmBondAlarmConfAturThreshRateUp_Type())
pdnDslAtmBondAlarmConfAturThreshRateUp.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAturThreshRateUp.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAturThreshRateUp.setUnits(_E)
class _PdnDslAtmBondAlarmConfAtucThreshRateDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDslAtmBondAlarmConfAtucThreshRateDown_Type.__name__=_J
_PdnDslAtmBondAlarmConfAtucThreshRateDown_Object=MibTableColumn
pdnDslAtmBondAlarmConfAtucThreshRateDown=_PdnDslAtmBondAlarmConfAtucThreshRateDown_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1,6),_PdnDslAtmBondAlarmConfAtucThreshRateDown_Type())
pdnDslAtmBondAlarmConfAtucThreshRateDown.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAtucThreshRateDown.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAtucThreshRateDown.setUnits(_E)
class _PdnDslAtmBondAlarmConfAturThreshRateDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDslAtmBondAlarmConfAturThreshRateDown_Type.__name__=_J
_PdnDslAtmBondAlarmConfAturThreshRateDown_Object=MibTableColumn
pdnDslAtmBondAlarmConfAturThreshRateDown=_PdnDslAtmBondAlarmConfAturThreshRateDown_Object((1,3,6,1,4,1,1795,2,24,2,6,33,1,11,1,7),_PdnDslAtmBondAlarmConfAturThreshRateDown_Type())
pdnDslAtmBondAlarmConfAturThreshRateDown.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAturThreshRateDown.setStatus(_A)
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAturThreshRateDown.setUnits(_E)
_PdnDslAtmBondAFNs_ObjectIdentity=ObjectIdentity
pdnDslAtmBondAFNs=_PdnDslAtmBondAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,2))
_PdnDslAtmBondConformance_ObjectIdentity=ObjectIdentity
pdnDslAtmBondConformance=_PdnDslAtmBondConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,3))
_PdnDslAtmBondCompliances_ObjectIdentity=ObjectIdentity
pdnDslAtmBondCompliances=_PdnDslAtmBondCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,3,1))
_PdnDslAtmBondGroups_ObjectIdentity=ObjectIdentity
pdnDslAtmBondGroups=_PdnDslAtmBondGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,3,2))
_PdnDslAtmBondObjGroups_ObjectIdentity=ObjectIdentity
pdnDslAtmBondObjGroups=_PdnDslAtmBondObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1))
_PdnDslAtmBondAfnGroups_ObjectIdentity=ObjectIdentity
pdnDslAtmBondAfnGroups=_PdnDslAtmBondAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,2))
_PdnDslAtmBondNtfyGroups_ObjectIdentity=ObjectIdentity
pdnDslAtmBondNtfyGroups=_PdnDslAtmBondNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,3))
pdnDslAtmBondGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,1))
pdnDslAtmBondGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_I),(_B,_c)))
if mibBuilder.loadTexts:pdnDslAtmBondGroup.setStatus(_A)
pdnDslAtmBondMaxRateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,2))
pdnDslAtmBondMaxRateGroup.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:pdnDslAtmBondMaxRateGroup.setStatus(_A)
pdnDslAtmBondMinRateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,3))
pdnDslAtmBondMinRateGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:pdnDslAtmBondMinRateGroup.setStatus(_A)
pdnDslAtmBondDiffDelayGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,4))
pdnDslAtmBondDiffDelayGroup.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:pdnDslAtmBondDiffDelayGroup.setStatus(_A)
pdnDslAtmBondGroupStatusNotifyEnabledGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,5))
pdnDslAtmBondGroupStatusNotifyEnabledGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:pdnDslAtmBondGroupStatusNotifyEnabledGroup.setStatus(_A)
pdnDslAtmBondMappingGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,6))
pdnDslAtmBondMappingGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:pdnDslAtmBondMappingGroup.setStatus(_A)
pdnDslAtmBondIndexMappingGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,7))
pdnDslAtmBondIndexMappingGroup.setObjects((_B,_m))
if mibBuilder.loadTexts:pdnDslAtmBondIndexMappingGroup.setStatus(_A)
pdnDslAtmBondInvMappingGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,8))
pdnDslAtmBondInvMappingGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:pdnDslAtmBondInvMappingGroup.setStatus(_A)
pdnDslAtmBondPerfAggDataRateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,9))
pdnDslAtmBondPerfAggDataRateGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:pdnDslAtmBondPerfAggDataRateGroup.setStatus(_A)
pdnDslAtmBondPerfBondGroupStatusGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,10))
pdnDslAtmBondPerfBondGroupStatusGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:pdnDslAtmBondPerfBondGroupStatusGroup.setStatus(_A)
pdnDslAtmBondDateAndTimeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,11))
pdnDslAtmBondDateAndTimeGroup.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:pdnDslAtmBondDateAndTimeGroup.setStatus(_A)
pdnDslAtmBondRunTimeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,12))
pdnDslAtmBondRunTimeGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:pdnDslAtmBondRunTimeGroup.setStatus(_A)
pdnDslAtmBondRxCellLossGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,13))
pdnDslAtmBondRxCellLossGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:pdnDslAtmBondRxCellLossGroup.setStatus(_A)
pdnDslAtmBondPerfFailReasonGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,14))
pdnDslAtmBondPerfFailReasonGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:pdnDslAtmBondPerfFailReasonGroup.setStatus(_A)
pdnDslAtmBondFailCountGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,15))
pdnDslAtmBondFailCountGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:pdnDslAtmBondFailCountGroup.setStatus(_A)
pdnDslAtmBondUASGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,16))
pdnDslAtmBondUASGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:pdnDslAtmBondUASGroup.setStatus(_A)
pdnDslAtmBondTrafficCapGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,17))
pdnDslAtmBondTrafficCapGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:pdnDslAtmBondTrafficCapGroup.setStatus(_A)
pdnDslATmBondAsmRxStatusGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,18))
pdnDslATmBondAsmRxStatusGroup.setObjects(*((_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:pdnDslATmBondAsmRxStatusGroup.setStatus(_A)
pdnDslAtmBondAlarmConfProfileGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,19))
pdnDslAtmBondAlarmConfProfileGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfProfileGroup.setStatus(_A)
pdnDslAtmBondAlarmConfAtucThreshRateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,20))
pdnDslAtmBondAlarmConfAtucThreshRateGroup.setObjects(*((_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAtucThreshRateGroup.setStatus(_A)
pdnDslAtmBondAlarmConfAturThreshRateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,1,21))
pdnDslAtmBondAlarmConfAturThreshRateGroup.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:pdnDslAtmBondAlarmConfAturThreshRateGroup.setStatus(_A)
pdnDslAtmBondAtucRateChange=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,33,0,1))
pdnDslAtmBondAtucRateChange.setObjects(*((_B,_I),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:pdnDslAtmBondAtucRateChange.setStatus(_A)
pdnDslAtmBondAturRateChange=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,33,0,2))
pdnDslAtmBondAturRateChange.setObjects(*((_B,_I),(_B,_N),(_B,_P)))
if mibBuilder.loadTexts:pdnDslAtmBondAturRateChange.setStatus(_A)
pdnDslAtmBondGroupStatusChange=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,33,0,3))
pdnDslAtmBondGroupStatusChange.setObjects(*((_B,_I),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:pdnDslAtmBondGroupStatusChange.setStatus(_A)
pdnDslAtmBondNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,6,33,3,2,3,1))
pdnDslAtmBondNotificationsGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:pdnDslAtmBondNotificationsGroup.setStatus(_A)
pdnDslAtmBondMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,33,3,1,1))
pdnDslAtmBondMIBCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:pdnDslAtmBondMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PdnDslAtmBondGroupIndexTC':PdnDslAtmBondGroupIndexTC,'PdnDslAtmBondGroupIdentityTC':PdnDslAtmBondGroupIdentityTC,'PdnDslAtmBondGroupBearerNumberTC':PdnDslAtmBondGroupBearerNumberTC,'PdnDslAtmBondLinkStatusAsmTC':PdnDslAtmBondLinkStatusAsmTC,'PdnDslAtmBondAsmRxStatusTC':PdnDslAtmBondAsmRxStatusTC,'PdnDslAtmBondGroupDataRateTC':PdnDslAtmBondGroupDataRateTC,'PdnDslAtmBondGroupDiffDelayTolTC':PdnDslAtmBondGroupDiffDelayTolTC,'PdnDslAtmBondGroupStatusTC':PdnDslAtmBondGroupStatusTC,'PdnDslAtmBondGroupFailReasonTC':PdnDslAtmBondGroupFailReasonTC,'pdnDslAtmBondMIB':pdnDslAtmBondMIB,'pdnDslAtmBondNotifications':pdnDslAtmBondNotifications,_AI:pdnDslAtmBondAtucRateChange,_AJ:pdnDslAtmBondAturRateChange,_AK:pdnDslAtmBondGroupStatusChange,'pdnDslAtmBondObjects':pdnDslAtmBondObjects,_Y:pdnDslAtmBondNextGroupIndex,_Z:pdnDslAtmBondNbrOfGroups,'pdnDslAtmBondGroupTable':pdnDslAtmBondGroupTable,'pdnDslAtmBondGroupEntry':pdnDslAtmBondGroupEntry,_F:pdnDslAtmBondGroupIndex,_a:pdnDslAtmBondGroupRowStatus,_b:pdnDslAtmBondGroupNbrRefs,_I:pdnDslAtmBondGroupIfIndex,_c:pdnDslAtmBondGroupID,_AB:pdnDslAtmBondGroupAlarmConfProfileName,_d:pdnDslAtmBondGroupAtucMaxNetDataRate,_e:pdnDslAtmBondGroupAturMaxNetDataRate,_f:pdnDslAtmBondGroupAtucMinNetDataRate,_g:pdnDslAtmBondGroupAturMinNetDataRate,_h:pdnDslAtmBondGroupAtucDiffDelay,_i:pdnDslAtmBondGroupAturDiffDelay,_j:pdnDslAtmBondGroupStatusNotifyEnabled,'pdnDslAtmBondMappingTable':pdnDslAtmBondMappingTable,'pdnDslAtmBondMappingEntry':pdnDslAtmBondMappingEntry,_K:pdnDslAtmBondDslIfIndex,_T:pdnDslAtmBondBearerNbr,_k:pdnDslAtmBondMappingRowStatus,_l:pdnDslAtmBondMappingGroupIndex,'pdnDslAtmBondGroupIndexMappingTable':pdnDslAtmBondGroupIndexMappingTable,'pdnDslAtmBondGroupIndexMappingEntry':pdnDslAtmBondGroupIndexMappingEntry,_m:pdnDslAtmBondGroupIndexMappingIndex,'pdnDslAtmBondGroupInvMappingTable':pdnDslAtmBondGroupInvMappingTable,'pdnDslAtmBondGroupInvMappingEntry':pdnDslAtmBondGroupInvMappingEntry,_n:pdnDslAtmBondInvMappingBearerNbr,'pdnDslAtmBondPerfTable':pdnDslAtmBondPerfTable,'pdnDslAtmBondPerfEntry':pdnDslAtmBondPerfEntry,_M:pdnDslAtmBondPerfCurrAtucNetDataRate,_N:pdnDslAtmBondPerfCurrAturNetDataRate,_O:pdnDslAtmBondPerfPrevAtucNetDataRate,_P:pdnDslAtmBondPerfPrevAturNetDataRate,_Q:pdnDslAtmBondPerfGroupStatus,_R:pdnDslAtmBondPerfFailReason,_z:pdnDslAtmBondPerfFailCount,_q:pdnDslAtmBondPerfRunTime,_A2:pdnDslAtmBondPerfUAS,_t:pdnDslAtmBondPerfAtucRxCellLoss,_u:pdnDslAtmBondPerfAturRxCellLoss,'pdnDslAtmBond15MinIntervalTable':pdnDslAtmBond15MinIntervalTable,'pdnDslAtmBond15MinIntervalEntry':pdnDslAtmBond15MinIntervalEntry,_V:pdnDslAtmBond15MinIntervalNumber,_o:pdnDslAtmBond15MinIntervalStartDateAndTime,_A0:pdnDslAtmBond15MinIntervalFailCount,_r:pdnDslAtmBond15MinIntervalRunTime,_A3:pdnDslAtmBond15MinIntervalUAS,_v:pdnDslAtmBond15MinIntervalAtucRxCellLoss,_w:pdnDslAtmBond15MinIntervalAturRxCellLoss,'pdnDslAtmBond1DayIntervalTable':pdnDslAtmBond1DayIntervalTable,'pdnDslAtmBond1DayIntervalEntry':pdnDslAtmBond1DayIntervalEntry,_W:pdnDslAtmBond1DayIntervalNumber,_p:pdnDslAtmBond1DayIntervalStartDateAndTime,_A1:pdnDslAtmBond1DayIntervalFailCount,_s:pdnDslAtmBond1DayIntervalRunTime,_A4:pdnDslAtmBond1DayIntervalUAS,_x:pdnDslAtmBond1DayIntervalAtucRxCellLoss,_y:pdnDslAtmBond1DayIntervalAturRxCellLoss,'pdnDslAtmBondLinkTable':pdnDslAtmBondLinkTable,'pdnDslAtmBondLinkEntry':pdnDslAtmBondLinkEntry,_A5:pdnDslAtmBondLinkAtucRxLinkStatus,_A6:pdnDslAtmBondLinkAturRxLinkStatus,_A7:pdnDslAtmBondLinkAtucTxLinkStatus,_A8:pdnDslAtmBondLinkAturTxLinkStatus,_A9:pdnDslAtmBondLinkAtucAsmRxStatus,_AA:pdnDslAtmBondLinkAturAsmRxStatus,'pdnDslAtmBondAlarmConfProfileTable':pdnDslAtmBondAlarmConfProfileTable,'pdnDslAtmBondAlarmConfProfileEntry':pdnDslAtmBondAlarmConfProfileEntry,_X:pdnDslAtmBondAlarmConfProfileName,_AC:pdnDslAtmBondAlarmConfRowStatus,_AD:pdnDslAtmBondAlarmConfNbrRefs,_AE:pdnDslAtmBondAlarmConfAtucThreshRateUp,_AG:pdnDslAtmBondAlarmConfAturThreshRateUp,_AF:pdnDslAtmBondAlarmConfAtucThreshRateDown,_AH:pdnDslAtmBondAlarmConfAturThreshRateDown,'pdnDslAtmBondAFNs':pdnDslAtmBondAFNs,'pdnDslAtmBondConformance':pdnDslAtmBondConformance,'pdnDslAtmBondCompliances':pdnDslAtmBondCompliances,'pdnDslAtmBondMIBCompliance':pdnDslAtmBondMIBCompliance,'pdnDslAtmBondGroups':pdnDslAtmBondGroups,'pdnDslAtmBondObjGroups':pdnDslAtmBondObjGroups,_AL:pdnDslAtmBondGroup,_AQ:pdnDslAtmBondMaxRateGroup,_AR:pdnDslAtmBondMinRateGroup,_AS:pdnDslAtmBondDiffDelayGroup,_AT:pdnDslAtmBondGroupStatusNotifyEnabledGroup,_AM:pdnDslAtmBondMappingGroup,_AU:pdnDslAtmBondIndexMappingGroup,_AV:pdnDslAtmBondInvMappingGroup,_AN:pdnDslAtmBondPerfAggDataRateGroup,_AO:pdnDslAtmBondPerfBondGroupStatusGroup,_AW:pdnDslAtmBondDateAndTimeGroup,_AX:pdnDslAtmBondRunTimeGroup,_AY:pdnDslAtmBondRxCellLossGroup,_AZ:pdnDslAtmBondPerfFailReasonGroup,_Aa:pdnDslAtmBondFailCountGroup,_Ab:pdnDslAtmBondUASGroup,_Ac:pdnDslAtmBondTrafficCapGroup,_Ad:pdnDslATmBondAsmRxStatusGroup,_Ae:pdnDslAtmBondAlarmConfProfileGroup,_Af:pdnDslAtmBondAlarmConfAtucThreshRateGroup,_Ag:pdnDslAtmBondAlarmConfAturThreshRateGroup,'pdnDslAtmBondAfnGroups':pdnDslAtmBondAfnGroups,'pdnDslAtmBondNtfyGroups':pdnDslAtmBondNtfyGroups,_AP:pdnDslAtmBondNotificationsGroup})