_Ab='juniFrMlFrGroup'
_Aa='juniFrGroup2'
_AZ='juniFrGroup'
_AY='juniFrMlFrBindRowStatus'
_AX='juniFrMlFrMajorRowStatus'
_AW='juniFrMlFrMajorBundleName'
_AV='juniFrMlFrMajorConfigLowerIfIndex'
_AU='juniFrMlFrLinkConfigRowStatus'
_AT='juniFrMlFrLinkConfigLowerIfIndex'
_AS='juniFrMlFrNextLinkIfIndex'
_AR='juniFrMlFrBundleRowStatus'
_AQ='juniFrDlcmiMultilinkFrBundleName'
_AP='juniFrSubIfCktRowStatus'
_AO='juniFrSubIfId'
_AN='juniFrSubIfLowerIfIndex'
_AM='juniFrSubIfRowStatus'
_AL='juniFrSubIfNextIfIndex'
_AK='juniFrMlFrBindLinkIfIndex'
_AJ='juniFrMlFrBindMajorIfIndex'
_AI='juniFrMlFrMajorConfigIfIndex'
_AH='juniFrMlFrLinkConfigIfIndex'
_AG='juniFrMlFrBundleName'
_AF='juniFrSubIfCktDlci'
_AE='juniFrCircuitDlci'
_AD='juniFrCircuitIfIndex'
_AC='JuniFrMlFrBundleName'
_AB='juniFrSubIfGroup'
_AA='juniFrCircuitSentBECNs'
_A9='juniFrCircuitSentFECNs'
_A8='juniFrCircuitRowStatus'
_A7='juniFrCircuitLogicalIfIndex'
_A6='juniFrCircuitSentDEs'
_A5='juniFrCircuitReceivedDEs'
_A4='juniFrCircuitDiscards'
_A3='juniFrCircuitType'
_A2='juniFrCircuitMulticast'
_A1='juniFrCircuitThroughput'
_A0='juniFrCircuitExcessBurst'
_z='juniFrCircuitCommittedBurst'
_y='juniFrCircuitLastTimeChange'
_x='juniFrCircuitCreationTime'
_w='juniFrCircuitReceivedOctets'
_v='juniFrCircuitReceivedFrames'
_u='juniFrCircuitSentOctets'
_t='juniFrCircuitSentFrames'
_s='juniFrCircuitReceivedBECNs'
_r='juniFrCircuitReceivedFECNs'
_q='juniFrCircuitState'
_p='juniFrDlcmiStatsDiscontinuityTime'
_o='juniFrDlcmiStatsDceNoResponseTimeouts'
_n='juniFrDlcmiStatsDceLossOfSequences'
_m='juniFrDlcmiStatsDceUnknownRxMessages'
_l='juniFrDlcmiStatsDceAsyncUpdates'
_k='juniFrDlcmiStatsDceFullEnquiryResponses'
_j='juniFrDlcmiStatsDceEnquiryResponses'
_i='juniFrDlcmiStatsDceFullEnquiries'
_h='juniFrDlcmiStatsDceEnquiries'
_g='juniFrDlcmiStatsDteNoResponseTimeouts'
_f='juniFrDlcmiStatsDteLossOfSequences'
_e='juniFrDlcmiStatsDteUnknownRxMessages'
_d='juniFrDlcmiStatsDteAsyncUpdates'
_c='juniFrDlcmiStatsDteFullEnquiryResponses'
_b='juniFrDlcmiStatsDteEnquiryResponses'
_a='juniFrDlcmiStatsDteFullEnquiries'
_Z='juniFrDlcmiStatsDteEnquiries'
_Y='juniFrDlcmiDceMonitoredEvents'
_X='juniFrDlcmiDceErrorThreshold'
_W='juniFrDlcmiDcePollingInterval'
_V='juniFrDlcmiRole'
_U='juniFrDlcmiLowerIfIndex'
_T='juniFrDlcmiRowStatus'
_S='juniFrDlcmiStatus'
_R='juniFrDlcmiMulticast'
_Q='juniFrDlcmiMaxSupportedVCs'
_P='juniFrDlcmiMonitoredEvents'
_O='juniFrDlcmiErrorThreshold'
_N='juniFrDlcmiFullEnquiryInterval'
_M='juniFrDlcmiPollingInterval'
_L='juniFrDlcmiAddressLen'
_K='juniFrDlcmiAddress'
_J='juniFrDlcmiState'
_I='juniFrNextIfIndex'
_H='juniFrSubIfIndex'
_G='juniFrDlcmiIfIndex'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='Juniper-FRAME-RELAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DLCI,=mibBuilder.importSymbols('FRAME-RELAY-DTE-MIB','DLCI')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
juniFrameRelayMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,10))
if mibBuilder.loadTexts:juniFrameRelayMIB.setRevisions(('2002-12-13 14:35','2000-09-26 17:30','1999-06-01 00:00','1998-11-13 00:00'))
class JuniFrMlFrBundleName(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniFrObjects_ObjectIdentity=ObjectIdentity
juniFrObjects=_JuniFrObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,10,1))
_JuniFrIfLayer_ObjectIdentity=ObjectIdentity
juniFrIfLayer=_JuniFrIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,10,1,1))
_JuniFrNextIfIndex_Type=JuniNextIfIndex
_JuniFrNextIfIndex_Object=MibScalar
juniFrNextIfIndex=_JuniFrNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,1,1),_JuniFrNextIfIndex_Type())
juniFrNextIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrNextIfIndex.setStatus(_B)
_JuniFrDlcmiTable_Object=MibTable
juniFrDlcmiTable=_JuniFrDlcmiTable_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2))
if mibBuilder.loadTexts:juniFrDlcmiTable.setStatus(_B)
_JuniFrDlcmiEntry_Object=MibTableRow
juniFrDlcmiEntry=_JuniFrDlcmiEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1))
juniFrDlcmiEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:juniFrDlcmiEntry.setStatus(_B)
_JuniFrDlcmiIfIndex_Type=InterfaceIndex
_JuniFrDlcmiIfIndex_Object=MibTableColumn
juniFrDlcmiIfIndex=_JuniFrDlcmiIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,1),_JuniFrDlcmiIfIndex_Type())
juniFrDlcmiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiIfIndex.setStatus(_B)
class _JuniFrDlcmiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLmiConfigured',1),('lmiRev1',2),('ansiT1617D',3),('ansiT1617B',4),('itut933A',5),('ansiT1617D1994',6)))
_JuniFrDlcmiState_Type.__name__=_E
_JuniFrDlcmiState_Object=MibTableColumn
juniFrDlcmiState=_JuniFrDlcmiState_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,2),_JuniFrDlcmiState_Type())
juniFrDlcmiState.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiState.setStatus(_B)
class _JuniFrDlcmiAddress_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('q921',1),('q922March90',2),('q922November90',3),('q922',4)))
_JuniFrDlcmiAddress_Type.__name__=_E
_JuniFrDlcmiAddress_Object=MibTableColumn
juniFrDlcmiAddress=_JuniFrDlcmiAddress_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,3),_JuniFrDlcmiAddress_Type())
juniFrDlcmiAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiAddress.setStatus(_B)
class _JuniFrDlcmiAddressLen_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('twoOctets',2),('threeOctets',3),('fourOctets',4)))
_JuniFrDlcmiAddressLen_Type.__name__=_E
_JuniFrDlcmiAddressLen_Object=MibTableColumn
juniFrDlcmiAddressLen=_JuniFrDlcmiAddressLen_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,4),_JuniFrDlcmiAddressLen_Type())
juniFrDlcmiAddressLen.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiAddressLen.setStatus(_B)
class _JuniFrDlcmiPollingInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_JuniFrDlcmiPollingInterval_Type.__name__=_E
_JuniFrDlcmiPollingInterval_Object=MibTableColumn
juniFrDlcmiPollingInterval=_JuniFrDlcmiPollingInterval_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,5),_JuniFrDlcmiPollingInterval_Type())
juniFrDlcmiPollingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiPollingInterval.setStatus(_B)
if mibBuilder.loadTexts:juniFrDlcmiPollingInterval.setUnits('seconds')
class _JuniFrDlcmiFullEnquiryInterval_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_JuniFrDlcmiFullEnquiryInterval_Type.__name__=_E
_JuniFrDlcmiFullEnquiryInterval_Object=MibTableColumn
juniFrDlcmiFullEnquiryInterval=_JuniFrDlcmiFullEnquiryInterval_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,6),_JuniFrDlcmiFullEnquiryInterval_Type())
juniFrDlcmiFullEnquiryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiFullEnquiryInterval.setStatus(_B)
class _JuniFrDlcmiErrorThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_JuniFrDlcmiErrorThreshold_Type.__name__=_E
_JuniFrDlcmiErrorThreshold_Object=MibTableColumn
juniFrDlcmiErrorThreshold=_JuniFrDlcmiErrorThreshold_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,7),_JuniFrDlcmiErrorThreshold_Type())
juniFrDlcmiErrorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiErrorThreshold.setStatus(_B)
class _JuniFrDlcmiMonitoredEvents_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_JuniFrDlcmiMonitoredEvents_Type.__name__=_E
_JuniFrDlcmiMonitoredEvents_Object=MibTableColumn
juniFrDlcmiMonitoredEvents=_JuniFrDlcmiMonitoredEvents_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,8),_JuniFrDlcmiMonitoredEvents_Type())
juniFrDlcmiMonitoredEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiMonitoredEvents.setStatus(_B)
_JuniFrDlcmiMaxSupportedVCs_Type=DLCI
_JuniFrDlcmiMaxSupportedVCs_Object=MibTableColumn
juniFrDlcmiMaxSupportedVCs=_JuniFrDlcmiMaxSupportedVCs_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,9),_JuniFrDlcmiMaxSupportedVCs_Type())
juniFrDlcmiMaxSupportedVCs.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiMaxSupportedVCs.setStatus(_B)
class _JuniFrDlcmiMulticast_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonBroadcast',1),('broadcast',2)))
_JuniFrDlcmiMulticast_Type.__name__=_E
_JuniFrDlcmiMulticast_Object=MibTableColumn
juniFrDlcmiMulticast=_JuniFrDlcmiMulticast_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,10),_JuniFrDlcmiMulticast_Type())
juniFrDlcmiMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiMulticast.setStatus(_B)
class _JuniFrDlcmiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('fault',2),('initializing',3)))
_JuniFrDlcmiStatus_Type.__name__=_E
_JuniFrDlcmiStatus_Object=MibTableColumn
juniFrDlcmiStatus=_JuniFrDlcmiStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,11),_JuniFrDlcmiStatus_Type())
juniFrDlcmiStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatus.setStatus(_B)
_JuniFrDlcmiRowStatus_Type=RowStatus
_JuniFrDlcmiRowStatus_Object=MibTableColumn
juniFrDlcmiRowStatus=_JuniFrDlcmiRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,12),_JuniFrDlcmiRowStatus_Type())
juniFrDlcmiRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiRowStatus.setStatus(_B)
_JuniFrDlcmiLowerIfIndex_Type=InterfaceIndexOrZero
_JuniFrDlcmiLowerIfIndex_Object=MibTableColumn
juniFrDlcmiLowerIfIndex=_JuniFrDlcmiLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,13),_JuniFrDlcmiLowerIfIndex_Type())
juniFrDlcmiLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiLowerIfIndex.setStatus(_B)
class _JuniFrDlcmiRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dte',0),('dce',1),('nni',2)))
_JuniFrDlcmiRole_Type.__name__=_E
_JuniFrDlcmiRole_Object=MibTableColumn
juniFrDlcmiRole=_JuniFrDlcmiRole_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,14),_JuniFrDlcmiRole_Type())
juniFrDlcmiRole.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiRole.setStatus(_B)
class _JuniFrDlcmiDcePollingInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_JuniFrDlcmiDcePollingInterval_Type.__name__=_E
_JuniFrDlcmiDcePollingInterval_Object=MibTableColumn
juniFrDlcmiDcePollingInterval=_JuniFrDlcmiDcePollingInterval_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,15),_JuniFrDlcmiDcePollingInterval_Type())
juniFrDlcmiDcePollingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiDcePollingInterval.setStatus(_B)
if mibBuilder.loadTexts:juniFrDlcmiDcePollingInterval.setUnits('seconds')
class _JuniFrDlcmiDceErrorThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_JuniFrDlcmiDceErrorThreshold_Type.__name__=_E
_JuniFrDlcmiDceErrorThreshold_Object=MibTableColumn
juniFrDlcmiDceErrorThreshold=_JuniFrDlcmiDceErrorThreshold_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,16),_JuniFrDlcmiDceErrorThreshold_Type())
juniFrDlcmiDceErrorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiDceErrorThreshold.setStatus(_B)
class _JuniFrDlcmiDceMonitoredEvents_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_JuniFrDlcmiDceMonitoredEvents_Type.__name__=_E
_JuniFrDlcmiDceMonitoredEvents_Object=MibTableColumn
juniFrDlcmiDceMonitoredEvents=_JuniFrDlcmiDceMonitoredEvents_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,17),_JuniFrDlcmiDceMonitoredEvents_Type())
juniFrDlcmiDceMonitoredEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiDceMonitoredEvents.setStatus(_B)
class _JuniFrDlcmiMultilinkFrBundleName_Type(JuniFrMlFrBundleName):defaultValue=OctetString('')
_JuniFrDlcmiMultilinkFrBundleName_Type.__name__=_AC
_JuniFrDlcmiMultilinkFrBundleName_Object=MibTableColumn
juniFrDlcmiMultilinkFrBundleName=_JuniFrDlcmiMultilinkFrBundleName_Object((1,3,6,1,4,1,4874,2,2,10,1,1,2,1,18),_JuniFrDlcmiMultilinkFrBundleName_Type())
juniFrDlcmiMultilinkFrBundleName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrDlcmiMultilinkFrBundleName.setStatus(_B)
_JuniFrDlcmiStatsTable_Object=MibTable
juniFrDlcmiStatsTable=_JuniFrDlcmiStatsTable_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3))
if mibBuilder.loadTexts:juniFrDlcmiStatsTable.setStatus(_B)
_JuniFrDlcmiStatsEntry_Object=MibTableRow
juniFrDlcmiStatsEntry=_JuniFrDlcmiStatsEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1))
juniFrDlcmiStatsEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:juniFrDlcmiStatsEntry.setStatus(_B)
_JuniFrDlcmiStatsDteEnquiries_Type=Counter32
_JuniFrDlcmiStatsDteEnquiries_Object=MibTableColumn
juniFrDlcmiStatsDteEnquiries=_JuniFrDlcmiStatsDteEnquiries_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,1),_JuniFrDlcmiStatsDteEnquiries_Type())
juniFrDlcmiStatsDteEnquiries.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteEnquiries.setStatus(_B)
_JuniFrDlcmiStatsDteFullEnquiries_Type=Counter32
_JuniFrDlcmiStatsDteFullEnquiries_Object=MibTableColumn
juniFrDlcmiStatsDteFullEnquiries=_JuniFrDlcmiStatsDteFullEnquiries_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,2),_JuniFrDlcmiStatsDteFullEnquiries_Type())
juniFrDlcmiStatsDteFullEnquiries.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteFullEnquiries.setStatus(_B)
_JuniFrDlcmiStatsDteEnquiryResponses_Type=Counter32
_JuniFrDlcmiStatsDteEnquiryResponses_Object=MibTableColumn
juniFrDlcmiStatsDteEnquiryResponses=_JuniFrDlcmiStatsDteEnquiryResponses_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,3),_JuniFrDlcmiStatsDteEnquiryResponses_Type())
juniFrDlcmiStatsDteEnquiryResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteEnquiryResponses.setStatus(_B)
_JuniFrDlcmiStatsDteFullEnquiryResponses_Type=Counter32
_JuniFrDlcmiStatsDteFullEnquiryResponses_Object=MibTableColumn
juniFrDlcmiStatsDteFullEnquiryResponses=_JuniFrDlcmiStatsDteFullEnquiryResponses_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,4),_JuniFrDlcmiStatsDteFullEnquiryResponses_Type())
juniFrDlcmiStatsDteFullEnquiryResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteFullEnquiryResponses.setStatus(_B)
_JuniFrDlcmiStatsDteAsyncUpdates_Type=Counter32
_JuniFrDlcmiStatsDteAsyncUpdates_Object=MibTableColumn
juniFrDlcmiStatsDteAsyncUpdates=_JuniFrDlcmiStatsDteAsyncUpdates_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,5),_JuniFrDlcmiStatsDteAsyncUpdates_Type())
juniFrDlcmiStatsDteAsyncUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteAsyncUpdates.setStatus(_B)
_JuniFrDlcmiStatsDteUnknownRxMessages_Type=Counter32
_JuniFrDlcmiStatsDteUnknownRxMessages_Object=MibTableColumn
juniFrDlcmiStatsDteUnknownRxMessages=_JuniFrDlcmiStatsDteUnknownRxMessages_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,6),_JuniFrDlcmiStatsDteUnknownRxMessages_Type())
juniFrDlcmiStatsDteUnknownRxMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteUnknownRxMessages.setStatus(_B)
_JuniFrDlcmiStatsDteLossOfSequences_Type=Counter32
_JuniFrDlcmiStatsDteLossOfSequences_Object=MibTableColumn
juniFrDlcmiStatsDteLossOfSequences=_JuniFrDlcmiStatsDteLossOfSequences_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,7),_JuniFrDlcmiStatsDteLossOfSequences_Type())
juniFrDlcmiStatsDteLossOfSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteLossOfSequences.setStatus(_B)
_JuniFrDlcmiStatsDteNoResponseTimeouts_Type=Counter32
_JuniFrDlcmiStatsDteNoResponseTimeouts_Object=MibTableColumn
juniFrDlcmiStatsDteNoResponseTimeouts=_JuniFrDlcmiStatsDteNoResponseTimeouts_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,8),_JuniFrDlcmiStatsDteNoResponseTimeouts_Type())
juniFrDlcmiStatsDteNoResponseTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDteNoResponseTimeouts.setStatus(_B)
_JuniFrDlcmiStatsDceEnquiries_Type=Counter32
_JuniFrDlcmiStatsDceEnquiries_Object=MibTableColumn
juniFrDlcmiStatsDceEnquiries=_JuniFrDlcmiStatsDceEnquiries_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,9),_JuniFrDlcmiStatsDceEnquiries_Type())
juniFrDlcmiStatsDceEnquiries.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceEnquiries.setStatus(_B)
_JuniFrDlcmiStatsDceFullEnquiries_Type=Counter32
_JuniFrDlcmiStatsDceFullEnquiries_Object=MibTableColumn
juniFrDlcmiStatsDceFullEnquiries=_JuniFrDlcmiStatsDceFullEnquiries_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,10),_JuniFrDlcmiStatsDceFullEnquiries_Type())
juniFrDlcmiStatsDceFullEnquiries.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceFullEnquiries.setStatus(_B)
_JuniFrDlcmiStatsDceEnquiryResponses_Type=Counter32
_JuniFrDlcmiStatsDceEnquiryResponses_Object=MibTableColumn
juniFrDlcmiStatsDceEnquiryResponses=_JuniFrDlcmiStatsDceEnquiryResponses_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,11),_JuniFrDlcmiStatsDceEnquiryResponses_Type())
juniFrDlcmiStatsDceEnquiryResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceEnquiryResponses.setStatus(_B)
_JuniFrDlcmiStatsDceFullEnquiryResponses_Type=Counter32
_JuniFrDlcmiStatsDceFullEnquiryResponses_Object=MibTableColumn
juniFrDlcmiStatsDceFullEnquiryResponses=_JuniFrDlcmiStatsDceFullEnquiryResponses_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,12),_JuniFrDlcmiStatsDceFullEnquiryResponses_Type())
juniFrDlcmiStatsDceFullEnquiryResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceFullEnquiryResponses.setStatus(_B)
_JuniFrDlcmiStatsDceAsyncUpdates_Type=Counter32
_JuniFrDlcmiStatsDceAsyncUpdates_Object=MibTableColumn
juniFrDlcmiStatsDceAsyncUpdates=_JuniFrDlcmiStatsDceAsyncUpdates_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,13),_JuniFrDlcmiStatsDceAsyncUpdates_Type())
juniFrDlcmiStatsDceAsyncUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceAsyncUpdates.setStatus(_B)
_JuniFrDlcmiStatsDceUnknownRxMessages_Type=Counter32
_JuniFrDlcmiStatsDceUnknownRxMessages_Object=MibTableColumn
juniFrDlcmiStatsDceUnknownRxMessages=_JuniFrDlcmiStatsDceUnknownRxMessages_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,14),_JuniFrDlcmiStatsDceUnknownRxMessages_Type())
juniFrDlcmiStatsDceUnknownRxMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceUnknownRxMessages.setStatus(_B)
_JuniFrDlcmiStatsDceLossOfSequences_Type=Counter32
_JuniFrDlcmiStatsDceLossOfSequences_Object=MibTableColumn
juniFrDlcmiStatsDceLossOfSequences=_JuniFrDlcmiStatsDceLossOfSequences_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,15),_JuniFrDlcmiStatsDceLossOfSequences_Type())
juniFrDlcmiStatsDceLossOfSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceLossOfSequences.setStatus(_B)
_JuniFrDlcmiStatsDceNoResponseTimeouts_Type=Counter32
_JuniFrDlcmiStatsDceNoResponseTimeouts_Object=MibTableColumn
juniFrDlcmiStatsDceNoResponseTimeouts=_JuniFrDlcmiStatsDceNoResponseTimeouts_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,16),_JuniFrDlcmiStatsDceNoResponseTimeouts_Type())
juniFrDlcmiStatsDceNoResponseTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDceNoResponseTimeouts.setStatus(_B)
_JuniFrDlcmiStatsDiscontinuityTime_Type=TimeTicks
_JuniFrDlcmiStatsDiscontinuityTime_Object=MibTableColumn
juniFrDlcmiStatsDiscontinuityTime=_JuniFrDlcmiStatsDiscontinuityTime_Object((1,3,6,1,4,1,4874,2,2,10,1,1,3,1,17),_JuniFrDlcmiStatsDiscontinuityTime_Type())
juniFrDlcmiStatsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrDlcmiStatsDiscontinuityTime.setStatus(_B)
_JuniFrCircuitTable_Object=MibTable
juniFrCircuitTable=_JuniFrCircuitTable_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4))
if mibBuilder.loadTexts:juniFrCircuitTable.setStatus(_B)
_JuniFrCircuitEntry_Object=MibTableRow
juniFrCircuitEntry=_JuniFrCircuitEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1))
juniFrCircuitEntry.setIndexNames((0,_A,_AD),(0,_A,_AE))
if mibBuilder.loadTexts:juniFrCircuitEntry.setStatus(_B)
_JuniFrCircuitIfIndex_Type=InterfaceIndex
_JuniFrCircuitIfIndex_Object=MibTableColumn
juniFrCircuitIfIndex=_JuniFrCircuitIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,1),_JuniFrCircuitIfIndex_Type())
juniFrCircuitIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrCircuitIfIndex.setStatus(_B)
_JuniFrCircuitDlci_Type=DLCI
_JuniFrCircuitDlci_Object=MibTableColumn
juniFrCircuitDlci=_JuniFrCircuitDlci_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,2),_JuniFrCircuitDlci_Type())
juniFrCircuitDlci.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrCircuitDlci.setStatus(_B)
class _JuniFrCircuitState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('active',2),('inactive',3)))
_JuniFrCircuitState_Type.__name__=_E
_JuniFrCircuitState_Object=MibTableColumn
juniFrCircuitState=_JuniFrCircuitState_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,3),_JuniFrCircuitState_Type())
juniFrCircuitState.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrCircuitState.setStatus(_B)
_JuniFrCircuitReceivedFECNs_Type=Counter32
_JuniFrCircuitReceivedFECNs_Object=MibTableColumn
juniFrCircuitReceivedFECNs=_JuniFrCircuitReceivedFECNs_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,4),_JuniFrCircuitReceivedFECNs_Type())
juniFrCircuitReceivedFECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitReceivedFECNs.setStatus(_B)
_JuniFrCircuitReceivedBECNs_Type=Counter32
_JuniFrCircuitReceivedBECNs_Object=MibTableColumn
juniFrCircuitReceivedBECNs=_JuniFrCircuitReceivedBECNs_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,5),_JuniFrCircuitReceivedBECNs_Type())
juniFrCircuitReceivedBECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitReceivedBECNs.setStatus(_B)
_JuniFrCircuitSentFrames_Type=Counter32
_JuniFrCircuitSentFrames_Object=MibTableColumn
juniFrCircuitSentFrames=_JuniFrCircuitSentFrames_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,6),_JuniFrCircuitSentFrames_Type())
juniFrCircuitSentFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitSentFrames.setStatus(_B)
_JuniFrCircuitSentOctets_Type=Counter32
_JuniFrCircuitSentOctets_Object=MibTableColumn
juniFrCircuitSentOctets=_JuniFrCircuitSentOctets_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,7),_JuniFrCircuitSentOctets_Type())
juniFrCircuitSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitSentOctets.setStatus(_B)
_JuniFrCircuitReceivedFrames_Type=Counter32
_JuniFrCircuitReceivedFrames_Object=MibTableColumn
juniFrCircuitReceivedFrames=_JuniFrCircuitReceivedFrames_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,8),_JuniFrCircuitReceivedFrames_Type())
juniFrCircuitReceivedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitReceivedFrames.setStatus(_B)
_JuniFrCircuitReceivedOctets_Type=Counter32
_JuniFrCircuitReceivedOctets_Object=MibTableColumn
juniFrCircuitReceivedOctets=_JuniFrCircuitReceivedOctets_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,9),_JuniFrCircuitReceivedOctets_Type())
juniFrCircuitReceivedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitReceivedOctets.setStatus(_B)
_JuniFrCircuitCreationTime_Type=TimeStamp
_JuniFrCircuitCreationTime_Object=MibTableColumn
juniFrCircuitCreationTime=_JuniFrCircuitCreationTime_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,10),_JuniFrCircuitCreationTime_Type())
juniFrCircuitCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitCreationTime.setStatus(_B)
_JuniFrCircuitLastTimeChange_Type=TimeStamp
_JuniFrCircuitLastTimeChange_Object=MibTableColumn
juniFrCircuitLastTimeChange=_JuniFrCircuitLastTimeChange_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,11),_JuniFrCircuitLastTimeChange_Type())
juniFrCircuitLastTimeChange.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitLastTimeChange.setStatus(_B)
class _JuniFrCircuitCommittedBurst_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniFrCircuitCommittedBurst_Type.__name__=_E
_JuniFrCircuitCommittedBurst_Object=MibTableColumn
juniFrCircuitCommittedBurst=_JuniFrCircuitCommittedBurst_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,12),_JuniFrCircuitCommittedBurst_Type())
juniFrCircuitCommittedBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrCircuitCommittedBurst.setStatus(_B)
class _JuniFrCircuitExcessBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniFrCircuitExcessBurst_Type.__name__=_E
_JuniFrCircuitExcessBurst_Object=MibTableColumn
juniFrCircuitExcessBurst=_JuniFrCircuitExcessBurst_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,13),_JuniFrCircuitExcessBurst_Type())
juniFrCircuitExcessBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrCircuitExcessBurst.setStatus(_B)
class _JuniFrCircuitThroughput_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniFrCircuitThroughput_Type.__name__=_E
_JuniFrCircuitThroughput_Object=MibTableColumn
juniFrCircuitThroughput=_JuniFrCircuitThroughput_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,14),_JuniFrCircuitThroughput_Type())
juniFrCircuitThroughput.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrCircuitThroughput.setStatus(_B)
class _JuniFrCircuitMulticast_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unicast',1),('oneWay',2),('twoWay',3),('nWay',4)))
_JuniFrCircuitMulticast_Type.__name__=_E
_JuniFrCircuitMulticast_Object=MibTableColumn
juniFrCircuitMulticast=_JuniFrCircuitMulticast_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,15),_JuniFrCircuitMulticast_Type())
juniFrCircuitMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrCircuitMulticast.setStatus(_B)
class _JuniFrCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_JuniFrCircuitType_Type.__name__=_E
_JuniFrCircuitType_Object=MibTableColumn
juniFrCircuitType=_JuniFrCircuitType_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,16),_JuniFrCircuitType_Type())
juniFrCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitType.setStatus(_B)
_JuniFrCircuitDiscards_Type=Counter32
_JuniFrCircuitDiscards_Object=MibTableColumn
juniFrCircuitDiscards=_JuniFrCircuitDiscards_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,17),_JuniFrCircuitDiscards_Type())
juniFrCircuitDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitDiscards.setStatus(_B)
_JuniFrCircuitReceivedDEs_Type=Counter32
_JuniFrCircuitReceivedDEs_Object=MibTableColumn
juniFrCircuitReceivedDEs=_JuniFrCircuitReceivedDEs_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,18),_JuniFrCircuitReceivedDEs_Type())
juniFrCircuitReceivedDEs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitReceivedDEs.setStatus(_B)
_JuniFrCircuitSentDEs_Type=Counter32
_JuniFrCircuitSentDEs_Object=MibTableColumn
juniFrCircuitSentDEs=_JuniFrCircuitSentDEs_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,19),_JuniFrCircuitSentDEs_Type())
juniFrCircuitSentDEs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitSentDEs.setStatus(_B)
_JuniFrCircuitLogicalIfIndex_Type=InterfaceIndex
_JuniFrCircuitLogicalIfIndex_Object=MibTableColumn
juniFrCircuitLogicalIfIndex=_JuniFrCircuitLogicalIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,20),_JuniFrCircuitLogicalIfIndex_Type())
juniFrCircuitLogicalIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrCircuitLogicalIfIndex.setStatus(_B)
_JuniFrCircuitRowStatus_Type=RowStatus
_JuniFrCircuitRowStatus_Object=MibTableColumn
juniFrCircuitRowStatus=_JuniFrCircuitRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,21),_JuniFrCircuitRowStatus_Type())
juniFrCircuitRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrCircuitRowStatus.setStatus(_B)
_JuniFrCircuitSentFECNs_Type=Counter32
_JuniFrCircuitSentFECNs_Object=MibTableColumn
juniFrCircuitSentFECNs=_JuniFrCircuitSentFECNs_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,22),_JuniFrCircuitSentFECNs_Type())
juniFrCircuitSentFECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitSentFECNs.setStatus(_B)
_JuniFrCircuitSentBECNs_Type=Counter32
_JuniFrCircuitSentBECNs_Object=MibTableColumn
juniFrCircuitSentBECNs=_JuniFrCircuitSentBECNs_Object((1,3,6,1,4,1,4874,2,2,10,1,1,4,1,23),_JuniFrCircuitSentBECNs_Type())
juniFrCircuitSentBECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrCircuitSentBECNs.setStatus(_B)
_JuniFrSubIfLayer_ObjectIdentity=ObjectIdentity
juniFrSubIfLayer=_JuniFrSubIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,10,1,2))
_JuniFrSubIfNextIfIndex_Type=JuniNextIfIndex
_JuniFrSubIfNextIfIndex_Object=MibScalar
juniFrSubIfNextIfIndex=_JuniFrSubIfNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,2,1),_JuniFrSubIfNextIfIndex_Type())
juniFrSubIfNextIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrSubIfNextIfIndex.setStatus(_B)
_JuniFrSubIfTable_Object=MibTable
juniFrSubIfTable=_JuniFrSubIfTable_Object((1,3,6,1,4,1,4874,2,2,10,1,2,2))
if mibBuilder.loadTexts:juniFrSubIfTable.setStatus(_B)
_JuniFrSubIfEntry_Object=MibTableRow
juniFrSubIfEntry=_JuniFrSubIfEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,2,2,1))
juniFrSubIfEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:juniFrSubIfEntry.setStatus(_B)
_JuniFrSubIfIndex_Type=InterfaceIndex
_JuniFrSubIfIndex_Object=MibTableColumn
juniFrSubIfIndex=_JuniFrSubIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,2,2,1,1),_JuniFrSubIfIndex_Type())
juniFrSubIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrSubIfIndex.setStatus(_B)
_JuniFrSubIfRowStatus_Type=RowStatus
_JuniFrSubIfRowStatus_Object=MibTableColumn
juniFrSubIfRowStatus=_JuniFrSubIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,2,2,1,2),_JuniFrSubIfRowStatus_Type())
juniFrSubIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrSubIfRowStatus.setStatus(_B)
_JuniFrSubIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniFrSubIfLowerIfIndex_Object=MibTableColumn
juniFrSubIfLowerIfIndex=_JuniFrSubIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,2,2,1,3),_JuniFrSubIfLowerIfIndex_Type())
juniFrSubIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrSubIfLowerIfIndex.setStatus(_B)
class _JuniFrSubIfId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_JuniFrSubIfId_Type.__name__=_E
_JuniFrSubIfId_Object=MibTableColumn
juniFrSubIfId=_JuniFrSubIfId_Object((1,3,6,1,4,1,4874,2,2,10,1,2,2,1,4),_JuniFrSubIfId_Type())
juniFrSubIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrSubIfId.setStatus(_B)
_JuniFrSubIfCktTable_Object=MibTable
juniFrSubIfCktTable=_JuniFrSubIfCktTable_Object((1,3,6,1,4,1,4874,2,2,10,1,2,3))
if mibBuilder.loadTexts:juniFrSubIfCktTable.setStatus(_B)
_JuniFrSubIfCktEntry_Object=MibTableRow
juniFrSubIfCktEntry=_JuniFrSubIfCktEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,2,3,1))
juniFrSubIfCktEntry.setIndexNames((0,_A,_H),(0,_A,_AF))
if mibBuilder.loadTexts:juniFrSubIfCktEntry.setStatus(_B)
_JuniFrSubIfCktDlci_Type=DLCI
_JuniFrSubIfCktDlci_Object=MibTableColumn
juniFrSubIfCktDlci=_JuniFrSubIfCktDlci_Object((1,3,6,1,4,1,4874,2,2,10,1,2,3,1,1),_JuniFrSubIfCktDlci_Type())
juniFrSubIfCktDlci.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrSubIfCktDlci.setStatus(_B)
_JuniFrSubIfCktRowStatus_Type=RowStatus
_JuniFrSubIfCktRowStatus_Object=MibTableColumn
juniFrSubIfCktRowStatus=_JuniFrSubIfCktRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,2,3,1,2),_JuniFrSubIfCktRowStatus_Type())
juniFrSubIfCktRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrSubIfCktRowStatus.setStatus(_B)
_JuniFrMlFr_ObjectIdentity=ObjectIdentity
juniFrMlFr=_JuniFrMlFr_ObjectIdentity((1,3,6,1,4,1,4874,2,2,10,1,3))
_JuniFrMlFrBundleTable_Object=MibTable
juniFrMlFrBundleTable=_JuniFrMlFrBundleTable_Object((1,3,6,1,4,1,4874,2,2,10,1,3,1))
if mibBuilder.loadTexts:juniFrMlFrBundleTable.setStatus(_B)
_JuniFrMlFrBundleEntry_Object=MibTableRow
juniFrMlFrBundleEntry=_JuniFrMlFrBundleEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,3,1,1))
juniFrMlFrBundleEntry.setIndexNames((0,_A,_AG))
if mibBuilder.loadTexts:juniFrMlFrBundleEntry.setStatus(_B)
_JuniFrMlFrBundleName_Type=JuniFrMlFrBundleName
_JuniFrMlFrBundleName_Object=MibTableColumn
juniFrMlFrBundleName=_JuniFrMlFrBundleName_Object((1,3,6,1,4,1,4874,2,2,10,1,3,1,1,1),_JuniFrMlFrBundleName_Type())
juniFrMlFrBundleName.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrMlFrBundleName.setStatus(_B)
_JuniFrMlFrBundleRowStatus_Type=RowStatus
_JuniFrMlFrBundleRowStatus_Object=MibTableColumn
juniFrMlFrBundleRowStatus=_JuniFrMlFrBundleRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,3,1,1,2),_JuniFrMlFrBundleRowStatus_Type())
juniFrMlFrBundleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrMlFrBundleRowStatus.setStatus(_B)
_JuniFrMlFrNextLinkIfIndex_Type=JuniNextIfIndex
_JuniFrMlFrNextLinkIfIndex_Object=MibScalar
juniFrMlFrNextLinkIfIndex=_JuniFrMlFrNextLinkIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,3,2),_JuniFrMlFrNextLinkIfIndex_Type())
juniFrMlFrNextLinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFrMlFrNextLinkIfIndex.setStatus(_B)
_JuniFrMlFrLinkConfigTable_Object=MibTable
juniFrMlFrLinkConfigTable=_JuniFrMlFrLinkConfigTable_Object((1,3,6,1,4,1,4874,2,2,10,1,3,3))
if mibBuilder.loadTexts:juniFrMlFrLinkConfigTable.setStatus(_B)
_JuniFrMlFrLinkConfigEntry_Object=MibTableRow
juniFrMlFrLinkConfigEntry=_JuniFrMlFrLinkConfigEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,3,3,1))
juniFrMlFrLinkConfigEntry.setIndexNames((0,_A,_AH))
if mibBuilder.loadTexts:juniFrMlFrLinkConfigEntry.setStatus(_B)
_JuniFrMlFrLinkConfigIfIndex_Type=InterfaceIndex
_JuniFrMlFrLinkConfigIfIndex_Object=MibTableColumn
juniFrMlFrLinkConfigIfIndex=_JuniFrMlFrLinkConfigIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,3,3,1,1),_JuniFrMlFrLinkConfigIfIndex_Type())
juniFrMlFrLinkConfigIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrMlFrLinkConfigIfIndex.setStatus(_B)
_JuniFrMlFrLinkConfigLowerIfIndex_Type=InterfaceIndexOrZero
_JuniFrMlFrLinkConfigLowerIfIndex_Object=MibTableColumn
juniFrMlFrLinkConfigLowerIfIndex=_JuniFrMlFrLinkConfigLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,3,3,1,2),_JuniFrMlFrLinkConfigLowerIfIndex_Type())
juniFrMlFrLinkConfigLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrMlFrLinkConfigLowerIfIndex.setStatus(_B)
_JuniFrMlFrLinkConfigRowStatus_Type=RowStatus
_JuniFrMlFrLinkConfigRowStatus_Object=MibTableColumn
juniFrMlFrLinkConfigRowStatus=_JuniFrMlFrLinkConfigRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,3,3,1,3),_JuniFrMlFrLinkConfigRowStatus_Type())
juniFrMlFrLinkConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrMlFrLinkConfigRowStatus.setStatus(_B)
_JuniFrMlFrMajorConfigTable_Object=MibTable
juniFrMlFrMajorConfigTable=_JuniFrMlFrMajorConfigTable_Object((1,3,6,1,4,1,4874,2,2,10,1,3,4))
if mibBuilder.loadTexts:juniFrMlFrMajorConfigTable.setStatus(_B)
_JuniFrMlFrMajorConfigEntry_Object=MibTableRow
juniFrMlFrMajorConfigEntry=_JuniFrMlFrMajorConfigEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,3,4,1))
juniFrMlFrMajorConfigEntry.setIndexNames((0,_A,_AI))
if mibBuilder.loadTexts:juniFrMlFrMajorConfigEntry.setStatus(_B)
_JuniFrMlFrMajorConfigIfIndex_Type=InterfaceIndex
_JuniFrMlFrMajorConfigIfIndex_Object=MibTableColumn
juniFrMlFrMajorConfigIfIndex=_JuniFrMlFrMajorConfigIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,3,4,1,1),_JuniFrMlFrMajorConfigIfIndex_Type())
juniFrMlFrMajorConfigIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrMlFrMajorConfigIfIndex.setStatus(_B)
_JuniFrMlFrMajorConfigLowerIfIndex_Type=InterfaceIndex
_JuniFrMlFrMajorConfigLowerIfIndex_Object=MibTableColumn
juniFrMlFrMajorConfigLowerIfIndex=_JuniFrMlFrMajorConfigLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,3,4,1,2),_JuniFrMlFrMajorConfigLowerIfIndex_Type())
juniFrMlFrMajorConfigLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrMlFrMajorConfigLowerIfIndex.setStatus(_B)
_JuniFrMlFrMajorBundleName_Type=JuniFrMlFrBundleName
_JuniFrMlFrMajorBundleName_Object=MibTableColumn
juniFrMlFrMajorBundleName=_JuniFrMlFrMajorBundleName_Object((1,3,6,1,4,1,4874,2,2,10,1,3,4,1,3),_JuniFrMlFrMajorBundleName_Type())
juniFrMlFrMajorBundleName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrMlFrMajorBundleName.setStatus(_B)
_JuniFrMlFrMajorRowStatus_Type=RowStatus
_JuniFrMlFrMajorRowStatus_Object=MibTableColumn
juniFrMlFrMajorRowStatus=_JuniFrMlFrMajorRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,3,4,1,4),_JuniFrMlFrMajorRowStatus_Type())
juniFrMlFrMajorRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrMlFrMajorRowStatus.setStatus(_B)
_JuniFrMlFrLinkBindTable_Object=MibTable
juniFrMlFrLinkBindTable=_JuniFrMlFrLinkBindTable_Object((1,3,6,1,4,1,4874,2,2,10,1,3,5))
if mibBuilder.loadTexts:juniFrMlFrLinkBindTable.setStatus(_B)
_JuniFrMlFrLinkBindEntry_Object=MibTableRow
juniFrMlFrLinkBindEntry=_JuniFrMlFrLinkBindEntry_Object((1,3,6,1,4,1,4874,2,2,10,1,3,5,1))
juniFrMlFrLinkBindEntry.setIndexNames((0,_A,_AJ),(0,_A,_AK))
if mibBuilder.loadTexts:juniFrMlFrLinkBindEntry.setStatus(_B)
_JuniFrMlFrBindMajorIfIndex_Type=InterfaceIndex
_JuniFrMlFrBindMajorIfIndex_Object=MibTableColumn
juniFrMlFrBindMajorIfIndex=_JuniFrMlFrBindMajorIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,3,5,1,1),_JuniFrMlFrBindMajorIfIndex_Type())
juniFrMlFrBindMajorIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrMlFrBindMajorIfIndex.setStatus(_B)
_JuniFrMlFrBindLinkIfIndex_Type=InterfaceIndex
_JuniFrMlFrBindLinkIfIndex_Object=MibTableColumn
juniFrMlFrBindLinkIfIndex=_JuniFrMlFrBindLinkIfIndex_Object((1,3,6,1,4,1,4874,2,2,10,1,3,5,1,2),_JuniFrMlFrBindLinkIfIndex_Type())
juniFrMlFrBindLinkIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniFrMlFrBindLinkIfIndex.setStatus(_B)
_JuniFrMlFrBindRowStatus_Type=RowStatus
_JuniFrMlFrBindRowStatus_Object=MibTableColumn
juniFrMlFrBindRowStatus=_JuniFrMlFrBindRowStatus_Object((1,3,6,1,4,1,4874,2,2,10,1,3,5,1,3),_JuniFrMlFrBindRowStatus_Type())
juniFrMlFrBindRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniFrMlFrBindRowStatus.setStatus(_B)
_JuniFrConformance_ObjectIdentity=ObjectIdentity
juniFrConformance=_JuniFrConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,10,4))
_JuniFrCompliances_ObjectIdentity=ObjectIdentity
juniFrCompliances=_JuniFrCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,10,4,1))
_JuniFrGroups_ObjectIdentity=ObjectIdentity
juniFrGroups=_JuniFrGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,10,4,2))
juniFrGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,10,4,2,1))
juniFrGroup.setObjects(*((_A,_I),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:juniFrGroup.setStatus('obsolete')
juniFrSubIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,10,4,2,2))
juniFrSubIfGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:juniFrSubIfGroup.setStatus(_B)
juniFrGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,10,4,2,3))
juniFrGroup2.setObjects(*((_A,_I),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_AQ),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:juniFrGroup2.setStatus(_B)
juniFrMlFrGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,10,4,2,4))
juniFrMlFrGroup.setObjects(*((_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:juniFrMlFrGroup.setStatus(_B)
juniFrCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,10,4,1,1))
juniFrCompliance.setObjects(*((_A,_AZ),(_A,_AB)))
if mibBuilder.loadTexts:juniFrCompliance.setStatus('obsolete')
juniFrCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,10,4,1,2))
juniFrCompliance2.setObjects(*((_A,_Aa),(_A,_AB),(_A,_Ab)))
if mibBuilder.loadTexts:juniFrCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_AC:JuniFrMlFrBundleName,'juniFrameRelayMIB':juniFrameRelayMIB,'juniFrObjects':juniFrObjects,'juniFrIfLayer':juniFrIfLayer,_I:juniFrNextIfIndex,'juniFrDlcmiTable':juniFrDlcmiTable,'juniFrDlcmiEntry':juniFrDlcmiEntry,_G:juniFrDlcmiIfIndex,_J:juniFrDlcmiState,_K:juniFrDlcmiAddress,_L:juniFrDlcmiAddressLen,_M:juniFrDlcmiPollingInterval,_N:juniFrDlcmiFullEnquiryInterval,_O:juniFrDlcmiErrorThreshold,_P:juniFrDlcmiMonitoredEvents,_Q:juniFrDlcmiMaxSupportedVCs,_R:juniFrDlcmiMulticast,_S:juniFrDlcmiStatus,_T:juniFrDlcmiRowStatus,_U:juniFrDlcmiLowerIfIndex,_V:juniFrDlcmiRole,_W:juniFrDlcmiDcePollingInterval,_X:juniFrDlcmiDceErrorThreshold,_Y:juniFrDlcmiDceMonitoredEvents,_AQ:juniFrDlcmiMultilinkFrBundleName,'juniFrDlcmiStatsTable':juniFrDlcmiStatsTable,'juniFrDlcmiStatsEntry':juniFrDlcmiStatsEntry,_Z:juniFrDlcmiStatsDteEnquiries,_a:juniFrDlcmiStatsDteFullEnquiries,_b:juniFrDlcmiStatsDteEnquiryResponses,_c:juniFrDlcmiStatsDteFullEnquiryResponses,_d:juniFrDlcmiStatsDteAsyncUpdates,_e:juniFrDlcmiStatsDteUnknownRxMessages,_f:juniFrDlcmiStatsDteLossOfSequences,_g:juniFrDlcmiStatsDteNoResponseTimeouts,_h:juniFrDlcmiStatsDceEnquiries,_i:juniFrDlcmiStatsDceFullEnquiries,_j:juniFrDlcmiStatsDceEnquiryResponses,_k:juniFrDlcmiStatsDceFullEnquiryResponses,_l:juniFrDlcmiStatsDceAsyncUpdates,_m:juniFrDlcmiStatsDceUnknownRxMessages,_n:juniFrDlcmiStatsDceLossOfSequences,_o:juniFrDlcmiStatsDceNoResponseTimeouts,_p:juniFrDlcmiStatsDiscontinuityTime,'juniFrCircuitTable':juniFrCircuitTable,'juniFrCircuitEntry':juniFrCircuitEntry,_AD:juniFrCircuitIfIndex,_AE:juniFrCircuitDlci,_q:juniFrCircuitState,_r:juniFrCircuitReceivedFECNs,_s:juniFrCircuitReceivedBECNs,_t:juniFrCircuitSentFrames,_u:juniFrCircuitSentOctets,_v:juniFrCircuitReceivedFrames,_w:juniFrCircuitReceivedOctets,_x:juniFrCircuitCreationTime,_y:juniFrCircuitLastTimeChange,_z:juniFrCircuitCommittedBurst,_A0:juniFrCircuitExcessBurst,_A1:juniFrCircuitThroughput,_A2:juniFrCircuitMulticast,_A3:juniFrCircuitType,_A4:juniFrCircuitDiscards,_A5:juniFrCircuitReceivedDEs,_A6:juniFrCircuitSentDEs,_A7:juniFrCircuitLogicalIfIndex,_A8:juniFrCircuitRowStatus,_A9:juniFrCircuitSentFECNs,_AA:juniFrCircuitSentBECNs,'juniFrSubIfLayer':juniFrSubIfLayer,_AL:juniFrSubIfNextIfIndex,'juniFrSubIfTable':juniFrSubIfTable,'juniFrSubIfEntry':juniFrSubIfEntry,_H:juniFrSubIfIndex,_AM:juniFrSubIfRowStatus,_AN:juniFrSubIfLowerIfIndex,_AO:juniFrSubIfId,'juniFrSubIfCktTable':juniFrSubIfCktTable,'juniFrSubIfCktEntry':juniFrSubIfCktEntry,_AF:juniFrSubIfCktDlci,_AP:juniFrSubIfCktRowStatus,'juniFrMlFr':juniFrMlFr,'juniFrMlFrBundleTable':juniFrMlFrBundleTable,'juniFrMlFrBundleEntry':juniFrMlFrBundleEntry,_AG:juniFrMlFrBundleName,_AR:juniFrMlFrBundleRowStatus,_AS:juniFrMlFrNextLinkIfIndex,'juniFrMlFrLinkConfigTable':juniFrMlFrLinkConfigTable,'juniFrMlFrLinkConfigEntry':juniFrMlFrLinkConfigEntry,_AH:juniFrMlFrLinkConfigIfIndex,_AT:juniFrMlFrLinkConfigLowerIfIndex,_AU:juniFrMlFrLinkConfigRowStatus,'juniFrMlFrMajorConfigTable':juniFrMlFrMajorConfigTable,'juniFrMlFrMajorConfigEntry':juniFrMlFrMajorConfigEntry,_AI:juniFrMlFrMajorConfigIfIndex,_AV:juniFrMlFrMajorConfigLowerIfIndex,_AW:juniFrMlFrMajorBundleName,_AX:juniFrMlFrMajorRowStatus,'juniFrMlFrLinkBindTable':juniFrMlFrLinkBindTable,'juniFrMlFrLinkBindEntry':juniFrMlFrLinkBindEntry,_AJ:juniFrMlFrBindMajorIfIndex,_AK:juniFrMlFrBindLinkIfIndex,_AY:juniFrMlFrBindRowStatus,'juniFrConformance':juniFrConformance,'juniFrCompliances':juniFrCompliances,'juniFrCompliance':juniFrCompliance,'juniFrCompliance2':juniFrCompliance2,'juniFrGroups':juniFrGroups,_AZ:juniFrGroup,_AB:juniFrSubIfGroup,_Aa:juniFrGroup2,_Ab:juniFrMlFrGroup})