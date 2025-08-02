_Ac='sfpsRestrictedMobilityHashIndex'
_Ab='sfpsRestrictedMobilityPort'
_Aa='sfpsRestrictedMobilityHash'
_AZ='sfpsRestrictedPortHashIndex'
_AY='sfpsRestrictedPortHash'
_AX='sfpsRestrictedPortPort'
_AW='sfpsDirViolationDeltaIndex'
_AV='aoInetIPMask'
_AU='aoNetBiosName'
_AT='aoHostName'
_AS='aoMacDXMcast'
_AR='aoInetRIP'
_AQ='aoInetRPC'
_AP='aoInetUDP'
_AO='restrictPort'
_AN='sfpsDirViolationHashIndex'
_AM='sfpsDirViolationHash'
_AL='hostControl'
_AK='hostManagement'
_AJ='sfpsTopologyFCLFunctionalLevel'
_AI='goingToAcces'
_AH='sfpsTopologyServerTestTopRelayRelayNumber'
_AG='sfpsTopologyServerTestRelayNumber'
_AF='sfpsVMTopServerDeltaIndex'
_AE='sfpsESPTopAgentPortPort'
_AD='backupWait'
_AC='sfpsRATopAgentPortLogicalPort'
_AB='sfpsRATopAgentNeighborSwitchID'
_AA='sfpsRATopAgentNeighborInPort'
_A9='versionOther'
_A8='sfpsVLANTopAgentPortPort'
_A7='sfpsVLANTopAgentNeighborSwitchID'
_A6='sfpsVLANTopAgentNeighborInPort'
_A5='sfpsIncompatibleNeighborSwitchID'
_A4='sfpsIncompatibleNeighborLogicalPort'
_A3='notCompatible'
_A2='compatible'
_A1='unknown-ra-standy'
_A0='downlingFlood'
_z='uplinkFlood'
_y='raStandby'
_x='loopStandby'
_w='fclStandby'
_v='uplink'
_u='raPrimary'
_t='accessOnly'
_s='notified'
_r='unNotified'
_q='twoWay'
_p='oneWay'
_o='sfpsCommonNeighborSwitchID'
_n='sfpsCommonNeighborLogicalPort'
_m='getPortInfo'
_l='sfpsTPMPortLogicalPort'
_k='twoWayCommLoss'
_j='versionedPortNghLoss'
_i='functionalLevelNghLoss'
_h='crossedPortNghLoss'
_g='subtractPortNghLoss'
_f='duplicateNghLoss'
_e='portDownNghLoss'
_d='agingNghLoss'
_c='optionsLoss'
_b='optionsGain'
_a='foundNeighbor'
_Z='sfpsHistoryTopologyServerIndex'
_Y='sfpsServiceCenterTopologyHashLeaf'
_X='vlan'
_W='vns'
_V='deleted'
_U='added'
_T='hostMgnt'
_S='hostMgmt'
_R='networkOnly'
_Q='init'
_P='enabled'
_O='disabled'
_N='add'
_M='hybrid'
_L='goingToAccess'
_K='hostCtrl'
_J='standBy'
_I='network'
_H='access'
_G='unknown'
_F='other'
_E='CTRON-SFPS-TOPOLOGY-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsDapiNvramStats,sfpsDirLockConfig,sfpsDirLockStats,sfpsDirRestriction,sfpsDirViolation,sfpsDirViolationAPI,sfpsDirViolationDeltaAPI,sfpsESPTopologyAgent,sfpsNeighborEvents,sfpsRATopAgentPortTableAPIIn,sfpsRATopAgentPortTableAPIOut,sfpsRATopologyAgent,sfpsRestrictedMobility,sfpsRestrictedMobilityAPI,sfpsServiceCenter,sfpsTAPITestIn,sfpsTAPITestOut,sfpsTPMPortTableAPIIn,sfpsTPMPortTableAPIOut,sfpsTopologyAgentCommon,sfpsTopologyFCL,sfpsTopologyPortManager,sfpsTopologyServerPortEventRelay,sfpsTopologyServerTest,sfpsTopologyServerTestIn,sfpsTopologyVNSNeighbors,sfpsVLANTopAgentPortTableAPIIn,sfpsVLANTopologyAgent,sfpsVMTopologyServer=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsDapiNvramStats','sfpsDirLockConfig','sfpsDirLockStats','sfpsDirRestriction','sfpsDirViolation','sfpsDirViolationAPI','sfpsDirViolationDeltaAPI','sfpsESPTopologyAgent','sfpsNeighborEvents','sfpsRATopAgentPortTableAPIIn','sfpsRATopAgentPortTableAPIOut','sfpsRATopologyAgent','sfpsRestrictedMobility','sfpsRestrictedMobilityAPI','sfpsServiceCenter','sfpsTAPITestIn','sfpsTAPITestOut','sfpsTPMPortTableAPIIn','sfpsTPMPortTableAPIOut','sfpsTopologyAgentCommon','sfpsTopologyFCL','sfpsTopologyPortManager','sfpsTopologyServerPortEventRelay','sfpsTopologyServerTest','sfpsTopologyServerTestIn','sfpsTopologyVNSNeighbors','sfpsVLANTopAgentPortTableAPIIn','sfpsVLANTopologyAgent','sfpsVMTopologyServer')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsServiceCenterTopologyTable_Object=MibTable
sfpsServiceCenterTopologyTable=_SfpsServiceCenterTopologyTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8))
if mibBuilder.loadTexts:sfpsServiceCenterTopologyTable.setStatus(_A)
_SfpsServiceCenterTopologyEntry_Object=MibTableRow
sfpsServiceCenterTopologyEntry=_SfpsServiceCenterTopologyEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1))
sfpsServiceCenterTopologyEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:sfpsServiceCenterTopologyEntry.setStatus(_A)
_SfpsServiceCenterTopologyHashLeaf_Type=HexInteger
_SfpsServiceCenterTopologyHashLeaf_Object=MibTableColumn
sfpsServiceCenterTopologyHashLeaf=_SfpsServiceCenterTopologyHashLeaf_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,1),_SfpsServiceCenterTopologyHashLeaf_Type())
sfpsServiceCenterTopologyHashLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyHashLeaf.setStatus(_A)
_SfpsServiceCenterTopologyMetric_Type=Integer32
_SfpsServiceCenterTopologyMetric_Object=MibTableColumn
sfpsServiceCenterTopologyMetric=_SfpsServiceCenterTopologyMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,2),_SfpsServiceCenterTopologyMetric_Type())
sfpsServiceCenterTopologyMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyMetric.setStatus(_A)
_SfpsServiceCenterTopologyName_Type=DisplayString
_SfpsServiceCenterTopologyName_Object=MibTableColumn
sfpsServiceCenterTopologyName=_SfpsServiceCenterTopologyName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,3),_SfpsServiceCenterTopologyName_Type())
sfpsServiceCenterTopologyName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyName.setStatus(_A)
class _SfpsServiceCenterTopologyOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kStatusRunning',1),('kStatusHalted',2),('kStatusPending',3),('kStatusFaulted',4),('kStatusNotStarted',5)))
_SfpsServiceCenterTopologyOperStatus_Type.__name__=_D
_SfpsServiceCenterTopologyOperStatus_Object=MibTableColumn
sfpsServiceCenterTopologyOperStatus=_SfpsServiceCenterTopologyOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,4),_SfpsServiceCenterTopologyOperStatus_Type())
sfpsServiceCenterTopologyOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyOperStatus.setStatus(_A)
class _SfpsServiceCenterTopologyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('disable',2),('enable',3)))
_SfpsServiceCenterTopologyAdminStatus_Type.__name__=_D
_SfpsServiceCenterTopologyAdminStatus_Object=MibTableColumn
sfpsServiceCenterTopologyAdminStatus=_SfpsServiceCenterTopologyAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,5),_SfpsServiceCenterTopologyAdminStatus_Type())
sfpsServiceCenterTopologyAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyAdminStatus.setStatus(_A)
_SfpsServiceCenterTopologyStatusTime_Type=TimeTicks
_SfpsServiceCenterTopologyStatusTime_Object=MibTableColumn
sfpsServiceCenterTopologyStatusTime=_SfpsServiceCenterTopologyStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,6),_SfpsServiceCenterTopologyStatusTime_Type())
sfpsServiceCenterTopologyStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyStatusTime.setStatus(_A)
_SfpsServiceCenterTopologyRequests_Type=Integer32
_SfpsServiceCenterTopologyRequests_Object=MibTableColumn
sfpsServiceCenterTopologyRequests=_SfpsServiceCenterTopologyRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,7),_SfpsServiceCenterTopologyRequests_Type())
sfpsServiceCenterTopologyRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyRequests.setStatus(_A)
_SfpsServiceCenterTopologyResponses_Type=Integer32
_SfpsServiceCenterTopologyResponses_Object=MibTableColumn
sfpsServiceCenterTopologyResponses=_SfpsServiceCenterTopologyResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,8,1,8),_SfpsServiceCenterTopologyResponses_Type())
sfpsServiceCenterTopologyResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterTopologyResponses.setStatus(_A)
_SfpsHistoryTopologyServerTable_Object=MibTable
sfpsHistoryTopologyServerTable=_SfpsHistoryTopologyServerTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7))
if mibBuilder.loadTexts:sfpsHistoryTopologyServerTable.setStatus(_A)
_SfpsHistoryTopologyServerEntry_Object=MibTableRow
sfpsHistoryTopologyServerEntry=_SfpsHistoryTopologyServerEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1))
sfpsHistoryTopologyServerEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:sfpsHistoryTopologyServerEntry.setStatus(_A)
_SfpsHistoryTopologyServerIndex_Type=Integer32
_SfpsHistoryTopologyServerIndex_Object=MibTableColumn
sfpsHistoryTopologyServerIndex=_SfpsHistoryTopologyServerIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,1),_SfpsHistoryTopologyServerIndex_Type())
sfpsHistoryTopologyServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerIndex.setStatus(_A)
_SfpsHistoryTopologyServerLogicalPort_Type=Integer32
_SfpsHistoryTopologyServerLogicalPort_Object=MibTableColumn
sfpsHistoryTopologyServerLogicalPort=_SfpsHistoryTopologyServerLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,2),_SfpsHistoryTopologyServerLogicalPort_Type())
sfpsHistoryTopologyServerLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerLogicalPort.setStatus(_A)
_SfpsHistoryTopologyServerSwitchID_Type=OctetString
_SfpsHistoryTopologyServerSwitchID_Object=MibTableColumn
sfpsHistoryTopologyServerSwitchID=_SfpsHistoryTopologyServerSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,3),_SfpsHistoryTopologyServerSwitchID_Type())
sfpsHistoryTopologyServerSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerSwitchID.setStatus(_A)
class _SfpsHistoryTopologyServerEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),(_d,4),(_e,5),(_f,6),(_g,7),('loopedPortNhgLoss',8),(_h,9),(_i,10),(_j,11),(_k,12),('sequenceNumberReset',13)))
_SfpsHistoryTopologyServerEvent_Type.__name__=_D
_SfpsHistoryTopologyServerEvent_Object=MibTableColumn
sfpsHistoryTopologyServerEvent=_SfpsHistoryTopologyServerEvent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,4),_SfpsHistoryTopologyServerEvent_Type())
sfpsHistoryTopologyServerEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerEvent.setStatus(_A)
_SfpsHistoryTopologyServerSwitchIP_Type=IpAddress
_SfpsHistoryTopologyServerSwitchIP_Object=MibTableColumn
sfpsHistoryTopologyServerSwitchIP=_SfpsHistoryTopologyServerSwitchIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,5),_SfpsHistoryTopologyServerSwitchIP_Type())
sfpsHistoryTopologyServerSwitchIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerSwitchIP.setStatus(_A)
_SfpsHistoryTopologyServerChassisMAC_Type=SfpsAddress
_SfpsHistoryTopologyServerChassisMAC_Object=MibTableColumn
sfpsHistoryTopologyServerChassisMAC=_SfpsHistoryTopologyServerChassisMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,6),_SfpsHistoryTopologyServerChassisMAC_Type())
sfpsHistoryTopologyServerChassisMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerChassisMAC.setStatus(_A)
_SfpsHistoryTopologyServerChassisIP_Type=IpAddress
_SfpsHistoryTopologyServerChassisIP_Object=MibTableColumn
sfpsHistoryTopologyServerChassisIP=_SfpsHistoryTopologyServerChassisIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,7),_SfpsHistoryTopologyServerChassisIP_Type())
sfpsHistoryTopologyServerChassisIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerChassisIP.setStatus(_A)
_SfpsHistoryTopologyServerAgent_Type=DisplayString
_SfpsHistoryTopologyServerAgent_Object=MibTableColumn
sfpsHistoryTopologyServerAgent=_SfpsHistoryTopologyServerAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,8),_SfpsHistoryTopologyServerAgent_Type())
sfpsHistoryTopologyServerAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerAgent.setStatus(_A)
_SfpsHistoryTopologyServerDeltaOptionsMask_Type=Integer32
_SfpsHistoryTopologyServerDeltaOptionsMask_Object=MibTableColumn
sfpsHistoryTopologyServerDeltaOptionsMask=_SfpsHistoryTopologyServerDeltaOptionsMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,9),_SfpsHistoryTopologyServerDeltaOptionsMask_Type())
sfpsHistoryTopologyServerDeltaOptionsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerDeltaOptionsMask.setStatus(_A)
_SfpsHistoryTopologyServerCurrentOptionsMask_Type=Integer32
_SfpsHistoryTopologyServerCurrentOptionsMask_Object=MibTableColumn
sfpsHistoryTopologyServerCurrentOptionsMask=_SfpsHistoryTopologyServerCurrentOptionsMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,10),_SfpsHistoryTopologyServerCurrentOptionsMask_Type())
sfpsHistoryTopologyServerCurrentOptionsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerCurrentOptionsMask.setStatus(_A)
_SfpsHistoryTopologyServerFCL_Type=Integer32
_SfpsHistoryTopologyServerFCL_Object=MibTableColumn
sfpsHistoryTopologyServerFCL=_SfpsHistoryTopologyServerFCL_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,11),_SfpsHistoryTopologyServerFCL_Type())
sfpsHistoryTopologyServerFCL.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerFCL.setStatus(_A)
_SfpsHistoryTopologyServerSysTime_Type=TimeTicks
_SfpsHistoryTopologyServerSysTime_Object=MibTableColumn
sfpsHistoryTopologyServerSysTime=_SfpsHistoryTopologyServerSysTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,7,7,1,12),_SfpsHistoryTopologyServerSysTime_Type())
sfpsHistoryTopologyServerSysTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsHistoryTopologyServerSysTime.setStatus(_A)
_SfpsTPMPortTable_Object=MibTable
sfpsTPMPortTable=_SfpsTPMPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1))
if mibBuilder.loadTexts:sfpsTPMPortTable.setStatus(_A)
_SfpsTPMPortEntry_Object=MibTableRow
sfpsTPMPortEntry=_SfpsTPMPortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1,1))
sfpsTPMPortEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:sfpsTPMPortEntry.setStatus(_A)
_SfpsTPMPortLogicalPort_Type=Integer32
_SfpsTPMPortLogicalPort_Object=MibTableColumn
sfpsTPMPortLogicalPort=_SfpsTPMPortLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1,1,1),_SfpsTPMPortLogicalPort_Type())
sfpsTPMPortLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortLogicalPort.setStatus(_A)
class _SfpsTPMPortMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('ethernet',1),('fddi',2),('atm-lec',3),('token-ring',4),('wan',5),('inb',6),('hcp',7),('hdp',8),('atm-encap',9),('atm-pvc',10),(_G,11),('atm-forum-lec',12),('atm-forum-pvc',13),('atm-forum-svc',14)))
_SfpsTPMPortMediaType_Type.__name__=_D
_SfpsTPMPortMediaType_Object=MibTableColumn
sfpsTPMPortMediaType=_SfpsTPMPortMediaType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1,1,2),_SfpsTPMPortMediaType_Type())
sfpsTPMPortMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortMediaType.setStatus(_A)
_SfpsTPMPortTopologyAgent_Type=DisplayString
_SfpsTPMPortTopologyAgent_Object=MibTableColumn
sfpsTPMPortTopologyAgent=_SfpsTPMPortTopologyAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1,1,3),_SfpsTPMPortTopologyAgent_Type())
sfpsTPMPortTopologyAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortTopologyAgent.setStatus(_A)
_SfpsTPMPortVlanAttributes_Type=Integer32
_SfpsTPMPortVlanAttributes_Object=MibTableColumn
sfpsTPMPortVlanAttributes=_SfpsTPMPortVlanAttributes_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1,1,8),_SfpsTPMPortVlanAttributes_Type())
sfpsTPMPortVlanAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortVlanAttributes.setStatus(_A)
_SfpsTPMPortNVRAMStatus_Type=Integer32
_SfpsTPMPortNVRAMStatus_Object=MibTableColumn
sfpsTPMPortNVRAMStatus=_SfpsTPMPortNVRAMStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1,1,9),_SfpsTPMPortNVRAMStatus_Type())
sfpsTPMPortNVRAMStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortNVRAMStatus.setStatus(_A)
_SfpsTPMPortCorePortVID_Type=Integer32
_SfpsTPMPortCorePortVID_Object=MibTableColumn
sfpsTPMPortCorePortVID=_SfpsTPMPortCorePortVID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,1,1,10),_SfpsTPMPortCorePortVID_Type())
sfpsTPMPortCorePortVID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortCorePortVID.setStatus(_A)
class _SfpsTPMPortTableAPIInVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_m,3)))
_SfpsTPMPortTableAPIInVerb_Type.__name__=_D
_SfpsTPMPortTableAPIInVerb_Object=MibScalar
sfpsTPMPortTableAPIInVerb=_SfpsTPMPortTableAPIInVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,2,1),_SfpsTPMPortTableAPIInVerb_Type())
sfpsTPMPortTableAPIInVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIInVerb.setStatus(_A)
_SfpsTPMPortTableAPIInLogicalPort_Type=Integer32
_SfpsTPMPortTableAPIInLogicalPort_Object=MibScalar
sfpsTPMPortTableAPIInLogicalPort=_SfpsTPMPortTableAPIInLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,2,2),_SfpsTPMPortTableAPIInLogicalPort_Type())
sfpsTPMPortTableAPIInLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIInLogicalPort.setStatus(_A)
_SfpsTPMPortTableAPIInTopologyAgent_Type=Integer32
_SfpsTPMPortTableAPIInTopologyAgent_Object=MibScalar
sfpsTPMPortTableAPIInTopologyAgent=_SfpsTPMPortTableAPIInTopologyAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,2,3),_SfpsTPMPortTableAPIInTopologyAgent_Type())
sfpsTPMPortTableAPIInTopologyAgent.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIInTopologyAgent.setStatus(_A)
class _SfpsTPMPortTableAPIInAdminPortUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_O,2),(_P,3)))
_SfpsTPMPortTableAPIInAdminPortUp_Type.__name__=_D
_SfpsTPMPortTableAPIInAdminPortUp_Object=MibScalar
sfpsTPMPortTableAPIInAdminPortUp=_SfpsTPMPortTableAPIInAdminPortUp_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,2,4),_SfpsTPMPortTableAPIInAdminPortUp_Type())
sfpsTPMPortTableAPIInAdminPortUp.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIInAdminPortUp.setStatus(_A)
class _SfpsTPMPortTableAPIInAdminPortDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_O,2),(_P,3)))
_SfpsTPMPortTableAPIInAdminPortDown_Type.__name__=_D
_SfpsTPMPortTableAPIInAdminPortDown_Object=MibScalar
sfpsTPMPortTableAPIInAdminPortDown=_SfpsTPMPortTableAPIInAdminPortDown_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,2,5),_SfpsTPMPortTableAPIInAdminPortDown_Type())
sfpsTPMPortTableAPIInAdminPortDown.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIInAdminPortDown.setStatus(_A)
_SfpsTPMPortTableAPIInCorePortVID_Type=Integer32
_SfpsTPMPortTableAPIInCorePortVID_Object=MibScalar
sfpsTPMPortTableAPIInCorePortVID=_SfpsTPMPortTableAPIInCorePortVID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,2,6),_SfpsTPMPortTableAPIInCorePortVID_Type())
sfpsTPMPortTableAPIInCorePortVID.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIInCorePortVID.setStatus(_A)
_SfpsTPMPortTableAPIOutLogicalPort_Type=Integer32
_SfpsTPMPortTableAPIOutLogicalPort_Object=MibScalar
sfpsTPMPortTableAPIOutLogicalPort=_SfpsTPMPortTableAPIOutLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,3,1),_SfpsTPMPortTableAPIOutLogicalPort_Type())
sfpsTPMPortTableAPIOutLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIOutLogicalPort.setStatus(_A)
_SfpsTPMPortTableAPIOutTopologyAgent_Type=Integer32
_SfpsTPMPortTableAPIOutTopologyAgent_Object=MibScalar
sfpsTPMPortTableAPIOutTopologyAgent=_SfpsTPMPortTableAPIOutTopologyAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,1,3,2),_SfpsTPMPortTableAPIOutTopologyAgent_Type())
sfpsTPMPortTableAPIOutTopologyAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTPMPortTableAPIOutTopologyAgent.setStatus(_A)
_SfpsCommonNeighborTable_Object=MibTable
sfpsCommonNeighborTable=_SfpsCommonNeighborTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1))
if mibBuilder.loadTexts:sfpsCommonNeighborTable.setStatus(_A)
_SfpsCommonNeighborEntry_Object=MibTableRow
sfpsCommonNeighborEntry=_SfpsCommonNeighborEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1))
sfpsCommonNeighborEntry.setIndexNames((0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:sfpsCommonNeighborEntry.setStatus(_A)
_SfpsCommonNeighborLogicalPort_Type=Integer32
_SfpsCommonNeighborLogicalPort_Object=MibTableColumn
sfpsCommonNeighborLogicalPort=_SfpsCommonNeighborLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,1),_SfpsCommonNeighborLogicalPort_Type())
sfpsCommonNeighborLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborLogicalPort.setStatus(_A)
_SfpsCommonNeighborSwitchID_Type=DisplayString
_SfpsCommonNeighborSwitchID_Object=MibTableColumn
sfpsCommonNeighborSwitchID=_SfpsCommonNeighborSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,2),_SfpsCommonNeighborSwitchID_Type())
sfpsCommonNeighborSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborSwitchID.setStatus(_A)
_SfpsCommonNeighborSwitchIP_Type=IpAddress
_SfpsCommonNeighborSwitchIP_Object=MibTableColumn
sfpsCommonNeighborSwitchIP=_SfpsCommonNeighborSwitchIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,3),_SfpsCommonNeighborSwitchIP_Type())
sfpsCommonNeighborSwitchIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborSwitchIP.setStatus(_A)
_SfpsCommonNeighborSwitchMAC_Type=SfpsAddress
_SfpsCommonNeighborSwitchMAC_Object=MibTableColumn
sfpsCommonNeighborSwitchMAC=_SfpsCommonNeighborSwitchMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,4),_SfpsCommonNeighborSwitchMAC_Type())
sfpsCommonNeighborSwitchMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborSwitchMAC.setStatus(_A)
class _SfpsCommonNeighborSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_SfpsCommonNeighborSwitchType_Type.__name__=_D
_SfpsCommonNeighborSwitchType_Object=MibTableColumn
sfpsCommonNeighborSwitchType=_SfpsCommonNeighborSwitchType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,5),_SfpsCommonNeighborSwitchType_Type())
sfpsCommonNeighborSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborSwitchType.setStatus(_A)
_SfpsCommonNeighborHellosReceived_Type=Integer32
_SfpsCommonNeighborHellosReceived_Object=MibTableColumn
sfpsCommonNeighborHellosReceived=_SfpsCommonNeighborHellosReceived_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,6),_SfpsCommonNeighborHellosReceived_Type())
sfpsCommonNeighborHellosReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborHellosReceived.setStatus(_A)
_SfpsCommonNeighborFirstHeard_Type=TimeTicks
_SfpsCommonNeighborFirstHeard_Object=MibTableColumn
sfpsCommonNeighborFirstHeard=_SfpsCommonNeighborFirstHeard_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,7),_SfpsCommonNeighborFirstHeard_Type())
sfpsCommonNeighborFirstHeard.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborFirstHeard.setStatus(_A)
_SfpsCommonNeighborLastHeard_Type=TimeTicks
_SfpsCommonNeighborLastHeard_Object=MibTableColumn
sfpsCommonNeighborLastHeard=_SfpsCommonNeighborLastHeard_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,8),_SfpsCommonNeighborLastHeard_Type())
sfpsCommonNeighborLastHeard.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborLastHeard.setStatus(_A)
_SfpsCommonNeighborReceiveFrequency_Type=Integer32
_SfpsCommonNeighborReceiveFrequency_Object=MibTableColumn
sfpsCommonNeighborReceiveFrequency=_SfpsCommonNeighborReceiveFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,9),_SfpsCommonNeighborReceiveFrequency_Type())
sfpsCommonNeighborReceiveFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborReceiveFrequency.setStatus(_A)
_SfpsCommonNeighborTopologyAgent_Type=DisplayString
_SfpsCommonNeighborTopologyAgent_Object=MibTableColumn
sfpsCommonNeighborTopologyAgent=_SfpsCommonNeighborTopologyAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,10),_SfpsCommonNeighborTopologyAgent_Type())
sfpsCommonNeighborTopologyAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborTopologyAgent.setStatus(_A)
_SfpsCommonNeighborChassisMAC_Type=SfpsAddress
_SfpsCommonNeighborChassisMAC_Object=MibTableColumn
sfpsCommonNeighborChassisMAC=_SfpsCommonNeighborChassisMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,11),_SfpsCommonNeighborChassisMAC_Type())
sfpsCommonNeighborChassisMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborChassisMAC.setStatus(_A)
class _SfpsCommonNeighborCommState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_p,2),(_q,3)))
_SfpsCommonNeighborCommState_Type.__name__=_D
_SfpsCommonNeighborCommState_Object=MibTableColumn
sfpsCommonNeighborCommState=_SfpsCommonNeighborCommState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,12),_SfpsCommonNeighborCommState_Type())
sfpsCommonNeighborCommState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborCommState.setStatus(_A)
class _SfpsCommonNeighborNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_r,2),(_s,3)))
_SfpsCommonNeighborNotifyState_Type.__name__=_D
_SfpsCommonNeighborNotifyState_Object=MibTableColumn
sfpsCommonNeighborNotifyState=_SfpsCommonNeighborNotifyState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,13),_SfpsCommonNeighborNotifyState_Type())
sfpsCommonNeighborNotifyState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborNotifyState.setStatus(_A)
_SfpsCommonNeighborTwoWayLossCount_Type=Integer32
_SfpsCommonNeighborTwoWayLossCount_Object=MibTableColumn
sfpsCommonNeighborTwoWayLossCount=_SfpsCommonNeighborTwoWayLossCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,14),_SfpsCommonNeighborTwoWayLossCount_Type())
sfpsCommonNeighborTwoWayLossCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborTwoWayLossCount.setStatus(_A)
_SfpsCommonNeighborTwoWayLossTime_Type=TimeTicks
_SfpsCommonNeighborTwoWayLossTime_Object=MibTableColumn
sfpsCommonNeighborTwoWayLossTime=_SfpsCommonNeighborTwoWayLossTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,15),_SfpsCommonNeighborTwoWayLossTime_Type())
sfpsCommonNeighborTwoWayLossTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborTwoWayLossTime.setStatus(_A)
_SfpsCommonNeighborSeqNumLossCount_Type=Integer32
_SfpsCommonNeighborSeqNumLossCount_Object=MibTableColumn
sfpsCommonNeighborSeqNumLossCount=_SfpsCommonNeighborSeqNumLossCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,16),_SfpsCommonNeighborSeqNumLossCount_Type())
sfpsCommonNeighborSeqNumLossCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborSeqNumLossCount.setStatus(_A)
_SfpsCommonNeighborSeqNumLossTime_Type=TimeTicks
_SfpsCommonNeighborSeqNumLossTime_Object=MibTableColumn
sfpsCommonNeighborSeqNumLossTime=_SfpsCommonNeighborSeqNumLossTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,17),_SfpsCommonNeighborSeqNumLossTime_Type())
sfpsCommonNeighborSeqNumLossTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborSeqNumLossTime.setStatus(_A)
_SfpsCommonNeighborFalseAgingCount_Type=Integer32
_SfpsCommonNeighborFalseAgingCount_Object=MibTableColumn
sfpsCommonNeighborFalseAgingCount=_SfpsCommonNeighborFalseAgingCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,18),_SfpsCommonNeighborFalseAgingCount_Type())
sfpsCommonNeighborFalseAgingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborFalseAgingCount.setStatus(_A)
_SfpsCommonNeighborFalseAgingTime_Type=TimeTicks
_SfpsCommonNeighborFalseAgingTime_Object=MibTableColumn
sfpsCommonNeighborFalseAgingTime=_SfpsCommonNeighborFalseAgingTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,19),_SfpsCommonNeighborFalseAgingTime_Type())
sfpsCommonNeighborFalseAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborFalseAgingTime.setStatus(_A)
_SfpsCommonNeighborChassisIP_Type=IpAddress
_SfpsCommonNeighborChassisIP_Object=MibTableColumn
sfpsCommonNeighborChassisIP=_SfpsCommonNeighborChassisIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,20),_SfpsCommonNeighborChassisIP_Type())
sfpsCommonNeighborChassisIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborChassisIP.setStatus(_A)
_SfpsCommonNeighborFCL_Type=HexInteger
_SfpsCommonNeighborFCL_Object=MibTableColumn
sfpsCommonNeighborFCL=_SfpsCommonNeighborFCL_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,21),_SfpsCommonNeighborFCL_Type())
sfpsCommonNeighborFCL.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborFCL.setStatus(_A)
_SfpsCommonNeighborOptionsMask_Type=Integer32
_SfpsCommonNeighborOptionsMask_Object=MibTableColumn
sfpsCommonNeighborOptionsMask=_SfpsCommonNeighborOptionsMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,22),_SfpsCommonNeighborOptionsMask_Type())
sfpsCommonNeighborOptionsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborOptionsMask.setStatus(_A)
class _SfpsCommonNeighborRcvdPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_T,4),(_K,5),(_G,6),(_L,7),(_M,8),(_J,9),(_R,10),(_t,11),(_u,12),(_v,13),(_w,14),(_x,15),(_y,16),('flood',17),(_z,18),(_A0,19),(_A1,20)))
_SfpsCommonNeighborRcvdPortState_Type.__name__=_D
_SfpsCommonNeighborRcvdPortState_Object=MibTableColumn
sfpsCommonNeighborRcvdPortState=_SfpsCommonNeighborRcvdPortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,23),_SfpsCommonNeighborRcvdPortState_Type())
sfpsCommonNeighborRcvdPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborRcvdPortState.setStatus(_A)
class _SfpsCommonNeighborSendPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_T,4),(_K,5),(_G,6),(_L,7),(_M,8),(_J,9),(_R,10),(_t,11),(_u,12),(_v,13),(_w,14),(_x,15),(_y,16),('flood',17),(_z,18),(_A0,19),(_A1,20)))
_SfpsCommonNeighborSendPortState_Type.__name__=_D
_SfpsCommonNeighborSendPortState_Object=MibTableColumn
sfpsCommonNeighborSendPortState=_SfpsCommonNeighborSendPortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,24),_SfpsCommonNeighborSendPortState_Type())
sfpsCommonNeighborSendPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborSendPortState.setStatus(_A)
class _SfpsCommonNeighborCompatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A2,1),(_A3,2),(_G,3)))
_SfpsCommonNeighborCompatibility_Type.__name__=_D
_SfpsCommonNeighborCompatibility_Object=MibTableColumn
sfpsCommonNeighborCompatibility=_SfpsCommonNeighborCompatibility_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,25),_SfpsCommonNeighborCompatibility_Type())
sfpsCommonNeighborCompatibility.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborCompatibility.setStatus(_A)
_SfpsCommonNeighborCorePortVID_Type=Integer32
_SfpsCommonNeighborCorePortVID_Object=MibTableColumn
sfpsCommonNeighborCorePortVID=_SfpsCommonNeighborCorePortVID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,1,1,26),_SfpsCommonNeighborCorePortVID_Type())
sfpsCommonNeighborCorePortVID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCommonNeighborCorePortVID.setStatus(_A)
_SfpsIncompatibleNeighborTable_Object=MibTable
sfpsIncompatibleNeighborTable=_SfpsIncompatibleNeighborTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2))
if mibBuilder.loadTexts:sfpsIncompatibleNeighborTable.setStatus(_A)
_SfpsIncompatibleNeighborEntry_Object=MibTableRow
sfpsIncompatibleNeighborEntry=_SfpsIncompatibleNeighborEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1))
sfpsIncompatibleNeighborEntry.setIndexNames((0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:sfpsIncompatibleNeighborEntry.setStatus(_A)
_SfpsIncompatibleNeighborLogicalPort_Type=Integer32
_SfpsIncompatibleNeighborLogicalPort_Object=MibTableColumn
sfpsIncompatibleNeighborLogicalPort=_SfpsIncompatibleNeighborLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,1),_SfpsIncompatibleNeighborLogicalPort_Type())
sfpsIncompatibleNeighborLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborLogicalPort.setStatus(_A)
_SfpsIncompatibleNeighborSwitchID_Type=DisplayString
_SfpsIncompatibleNeighborSwitchID_Object=MibTableColumn
sfpsIncompatibleNeighborSwitchID=_SfpsIncompatibleNeighborSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,2),_SfpsIncompatibleNeighborSwitchID_Type())
sfpsIncompatibleNeighborSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborSwitchID.setStatus(_A)
_SfpsIncompatibleNeighborSwitchIP_Type=IpAddress
_SfpsIncompatibleNeighborSwitchIP_Object=MibTableColumn
sfpsIncompatibleNeighborSwitchIP=_SfpsIncompatibleNeighborSwitchIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,3),_SfpsIncompatibleNeighborSwitchIP_Type())
sfpsIncompatibleNeighborSwitchIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborSwitchIP.setStatus(_A)
_SfpsIncompatibleNeighborSwitchMAC_Type=SfpsAddress
_SfpsIncompatibleNeighborSwitchMAC_Object=MibTableColumn
sfpsIncompatibleNeighborSwitchMAC=_SfpsIncompatibleNeighborSwitchMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,4),_SfpsIncompatibleNeighborSwitchMAC_Type())
sfpsIncompatibleNeighborSwitchMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborSwitchMAC.setStatus(_A)
class _SfpsIncompatibleNeighborSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_SfpsIncompatibleNeighborSwitchType_Type.__name__=_D
_SfpsIncompatibleNeighborSwitchType_Object=MibTableColumn
sfpsIncompatibleNeighborSwitchType=_SfpsIncompatibleNeighborSwitchType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,5),_SfpsIncompatibleNeighborSwitchType_Type())
sfpsIncompatibleNeighborSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborSwitchType.setStatus(_A)
_SfpsIncompatibleNeighborHellosReceived_Type=Integer32
_SfpsIncompatibleNeighborHellosReceived_Object=MibTableColumn
sfpsIncompatibleNeighborHellosReceived=_SfpsIncompatibleNeighborHellosReceived_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,6),_SfpsIncompatibleNeighborHellosReceived_Type())
sfpsIncompatibleNeighborHellosReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborHellosReceived.setStatus(_A)
_SfpsIncompatibleNeighborFirstHeard_Type=TimeTicks
_SfpsIncompatibleNeighborFirstHeard_Object=MibTableColumn
sfpsIncompatibleNeighborFirstHeard=_SfpsIncompatibleNeighborFirstHeard_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,7),_SfpsIncompatibleNeighborFirstHeard_Type())
sfpsIncompatibleNeighborFirstHeard.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborFirstHeard.setStatus(_A)
_SfpsIncompatibleNeighborLastHeard_Type=TimeTicks
_SfpsIncompatibleNeighborLastHeard_Object=MibTableColumn
sfpsIncompatibleNeighborLastHeard=_SfpsIncompatibleNeighborLastHeard_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,8),_SfpsIncompatibleNeighborLastHeard_Type())
sfpsIncompatibleNeighborLastHeard.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborLastHeard.setStatus(_A)
_SfpsIncompatibleNeighborReceiveFrequency_Type=Integer32
_SfpsIncompatibleNeighborReceiveFrequency_Object=MibTableColumn
sfpsIncompatibleNeighborReceiveFrequency=_SfpsIncompatibleNeighborReceiveFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,9),_SfpsIncompatibleNeighborReceiveFrequency_Type())
sfpsIncompatibleNeighborReceiveFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborReceiveFrequency.setStatus(_A)
_SfpsIncompatibleNeighborTopologyAgent_Type=DisplayString
_SfpsIncompatibleNeighborTopologyAgent_Object=MibTableColumn
sfpsIncompatibleNeighborTopologyAgent=_SfpsIncompatibleNeighborTopologyAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,10),_SfpsIncompatibleNeighborTopologyAgent_Type())
sfpsIncompatibleNeighborTopologyAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborTopologyAgent.setStatus(_A)
_SfpsIncompatibleNeighborChassisMAC_Type=SfpsAddress
_SfpsIncompatibleNeighborChassisMAC_Object=MibTableColumn
sfpsIncompatibleNeighborChassisMAC=_SfpsIncompatibleNeighborChassisMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,11),_SfpsIncompatibleNeighborChassisMAC_Type())
sfpsIncompatibleNeighborChassisMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborChassisMAC.setStatus(_A)
class _SfpsIncompatibleNeighborCommState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_p,2),(_q,3)))
_SfpsIncompatibleNeighborCommState_Type.__name__=_D
_SfpsIncompatibleNeighborCommState_Object=MibTableColumn
sfpsIncompatibleNeighborCommState=_SfpsIncompatibleNeighborCommState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,12),_SfpsIncompatibleNeighborCommState_Type())
sfpsIncompatibleNeighborCommState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborCommState.setStatus(_A)
class _SfpsIncompatibleNeighborNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_r,2),(_s,3)))
_SfpsIncompatibleNeighborNotifyState_Type.__name__=_D
_SfpsIncompatibleNeighborNotifyState_Object=MibTableColumn
sfpsIncompatibleNeighborNotifyState=_SfpsIncompatibleNeighborNotifyState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,13),_SfpsIncompatibleNeighborNotifyState_Type())
sfpsIncompatibleNeighborNotifyState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborNotifyState.setStatus(_A)
_SfpsIncompatibleNeighborTwoWayLossCount_Type=Integer32
_SfpsIncompatibleNeighborTwoWayLossCount_Object=MibTableColumn
sfpsIncompatibleNeighborTwoWayLossCount=_SfpsIncompatibleNeighborTwoWayLossCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,14),_SfpsIncompatibleNeighborTwoWayLossCount_Type())
sfpsIncompatibleNeighborTwoWayLossCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborTwoWayLossCount.setStatus(_A)
_SfpsIncompatibleNeighborTwoWayLossTime_Type=TimeTicks
_SfpsIncompatibleNeighborTwoWayLossTime_Object=MibTableColumn
sfpsIncompatibleNeighborTwoWayLossTime=_SfpsIncompatibleNeighborTwoWayLossTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,15),_SfpsIncompatibleNeighborTwoWayLossTime_Type())
sfpsIncompatibleNeighborTwoWayLossTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborTwoWayLossTime.setStatus(_A)
_SfpsIncompatibleNeighborSeqNumLossCount_Type=Integer32
_SfpsIncompatibleNeighborSeqNumLossCount_Object=MibTableColumn
sfpsIncompatibleNeighborSeqNumLossCount=_SfpsIncompatibleNeighborSeqNumLossCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,16),_SfpsIncompatibleNeighborSeqNumLossCount_Type())
sfpsIncompatibleNeighborSeqNumLossCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborSeqNumLossCount.setStatus(_A)
_SfpsIncompatibleNeighborSeqNumLossTime_Type=TimeTicks
_SfpsIncompatibleNeighborSeqNumLossTime_Object=MibTableColumn
sfpsIncompatibleNeighborSeqNumLossTime=_SfpsIncompatibleNeighborSeqNumLossTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,17),_SfpsIncompatibleNeighborSeqNumLossTime_Type())
sfpsIncompatibleNeighborSeqNumLossTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborSeqNumLossTime.setStatus(_A)
_SfpsIncompatibleNeighborFalseAgingCount_Type=Integer32
_SfpsIncompatibleNeighborFalseAgingCount_Object=MibTableColumn
sfpsIncompatibleNeighborFalseAgingCount=_SfpsIncompatibleNeighborFalseAgingCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,18),_SfpsIncompatibleNeighborFalseAgingCount_Type())
sfpsIncompatibleNeighborFalseAgingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborFalseAgingCount.setStatus(_A)
_SfpsIncompatibleNeighborFalseAgingTime_Type=TimeTicks
_SfpsIncompatibleNeighborFalseAgingTime_Object=MibTableColumn
sfpsIncompatibleNeighborFalseAgingTime=_SfpsIncompatibleNeighborFalseAgingTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,19),_SfpsIncompatibleNeighborFalseAgingTime_Type())
sfpsIncompatibleNeighborFalseAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborFalseAgingTime.setStatus(_A)
_SfpsIncompatibleNeighborChassisIP_Type=IpAddress
_SfpsIncompatibleNeighborChassisIP_Object=MibTableColumn
sfpsIncompatibleNeighborChassisIP=_SfpsIncompatibleNeighborChassisIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,20),_SfpsIncompatibleNeighborChassisIP_Type())
sfpsIncompatibleNeighborChassisIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborChassisIP.setStatus(_A)
_SfpsIncompatibleNeighborFCL_Type=HexInteger
_SfpsIncompatibleNeighborFCL_Object=MibTableColumn
sfpsIncompatibleNeighborFCL=_SfpsIncompatibleNeighborFCL_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,21),_SfpsIncompatibleNeighborFCL_Type())
sfpsIncompatibleNeighborFCL.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborFCL.setStatus(_A)
_SfpsIncompatibleNeighborOptionsMask_Type=Integer32
_SfpsIncompatibleNeighborOptionsMask_Object=MibTableColumn
sfpsIncompatibleNeighborOptionsMask=_SfpsIncompatibleNeighborOptionsMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,22),_SfpsIncompatibleNeighborOptionsMask_Type())
sfpsIncompatibleNeighborOptionsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborOptionsMask.setStatus(_A)
class _SfpsIncompatibleNeighborLocalPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_T,4),(_K,5),(_G,6),(_L,7),(_M,8),(_J,9)))
_SfpsIncompatibleNeighborLocalPortState_Type.__name__=_D
_SfpsIncompatibleNeighborLocalPortState_Object=MibTableColumn
sfpsIncompatibleNeighborLocalPortState=_SfpsIncompatibleNeighborLocalPortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,23),_SfpsIncompatibleNeighborLocalPortState_Type())
sfpsIncompatibleNeighborLocalPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborLocalPortState.setStatus(_A)
class _SfpsIncompatibleNeighborRemotePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_T,4),(_K,5),(_G,6),(_L,7),(_M,8),(_J,9)))
_SfpsIncompatibleNeighborRemotePortState_Type.__name__=_D
_SfpsIncompatibleNeighborRemotePortState_Object=MibTableColumn
sfpsIncompatibleNeighborRemotePortState=_SfpsIncompatibleNeighborRemotePortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,24),_SfpsIncompatibleNeighborRemotePortState_Type())
sfpsIncompatibleNeighborRemotePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborRemotePortState.setStatus(_A)
class _SfpsIncompatibleNeighborCompatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A2,1),(_A3,2),(_G,3)))
_SfpsIncompatibleNeighborCompatibility_Type.__name__=_D
_SfpsIncompatibleNeighborCompatibility_Object=MibTableColumn
sfpsIncompatibleNeighborCompatibility=_SfpsIncompatibleNeighborCompatibility_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,2,2,1,25),_SfpsIncompatibleNeighborCompatibility_Type())
sfpsIncompatibleNeighborCompatibility.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsIncompatibleNeighborCompatibility.setStatus(_A)
_SfpsVLANTopAgentNeighborTable_Object=MibTable
sfpsVLANTopAgentNeighborTable=_SfpsVLANTopAgentNeighborTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,1))
if mibBuilder.loadTexts:sfpsVLANTopAgentNeighborTable.setStatus(_A)
_SfpsVLANTopAgentNeighborEntry_Object=MibTableRow
sfpsVLANTopAgentNeighborEntry=_SfpsVLANTopAgentNeighborEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,1,1))
sfpsVLANTopAgentNeighborEntry.setIndexNames((0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:sfpsVLANTopAgentNeighborEntry.setStatus(_A)
_SfpsVLANTopAgentNeighborInPort_Type=Integer32
_SfpsVLANTopAgentNeighborInPort_Object=MibTableColumn
sfpsVLANTopAgentNeighborInPort=_SfpsVLANTopAgentNeighborInPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,1,1,1),_SfpsVLANTopAgentNeighborInPort_Type())
sfpsVLANTopAgentNeighborInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentNeighborInPort.setStatus(_A)
_SfpsVLANTopAgentNeighborSwitchID_Type=DisplayString
_SfpsVLANTopAgentNeighborSwitchID_Object=MibTableColumn
sfpsVLANTopAgentNeighborSwitchID=_SfpsVLANTopAgentNeighborSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,1,1,2),_SfpsVLANTopAgentNeighborSwitchID_Type())
sfpsVLANTopAgentNeighborSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentNeighborSwitchID.setStatus(_A)
_SfpsVLANTopAgentNeighborOptions_Type=Integer32
_SfpsVLANTopAgentNeighborOptions_Object=MibTableColumn
sfpsVLANTopAgentNeighborOptions=_SfpsVLANTopAgentNeighborOptions_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,1,1,3),_SfpsVLANTopAgentNeighborOptions_Type())
sfpsVLANTopAgentNeighborOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentNeighborOptions.setStatus(_A)
_SfpsVLANTopAgentPortTable_Object=MibTable
sfpsVLANTopAgentPortTable=_SfpsVLANTopAgentPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2))
if mibBuilder.loadTexts:sfpsVLANTopAgentPortTable.setStatus(_A)
_SfpsVLANTopAgentPortEntry_Object=MibTableRow
sfpsVLANTopAgentPortEntry=_SfpsVLANTopAgentPortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2,1))
sfpsVLANTopAgentPortEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:sfpsVLANTopAgentPortEntry.setStatus(_A)
_SfpsVLANTopAgentPortPort_Type=Integer32
_SfpsVLANTopAgentPortPort_Object=MibTableColumn
sfpsVLANTopAgentPortPort=_SfpsVLANTopAgentPortPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2,1,1),_SfpsVLANTopAgentPortPort_Type())
sfpsVLANTopAgentPortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortPort.setStatus(_A)
class _SfpsVLANTopAgentPortHelloVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A9,1),('version2',2),('version3',3),('version4',4)))
_SfpsVLANTopAgentPortHelloVersion_Type.__name__=_D
_SfpsVLANTopAgentPortHelloVersion_Object=MibTableColumn
sfpsVLANTopAgentPortHelloVersion=_SfpsVLANTopAgentPortHelloVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2,1,2),_SfpsVLANTopAgentPortHelloVersion_Type())
sfpsVLANTopAgentPortHelloVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortHelloVersion.setStatus(_A)
_SfpsVLANTopAgentPortSendFrequency_Type=Integer32
_SfpsVLANTopAgentPortSendFrequency_Object=MibTableColumn
sfpsVLANTopAgentPortSendFrequency=_SfpsVLANTopAgentPortSendFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2,1,3),_SfpsVLANTopAgentPortSendFrequency_Type())
sfpsVLANTopAgentPortSendFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortSendFrequency.setStatus(_A)
_SfpsVLANTopAgentPortRecvFrequency_Type=Integer32
_SfpsVLANTopAgentPortRecvFrequency_Object=MibTableColumn
sfpsVLANTopAgentPortRecvFrequency=_SfpsVLANTopAgentPortRecvFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2,1,4),_SfpsVLANTopAgentPortRecvFrequency_Type())
sfpsVLANTopAgentPortRecvFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortRecvFrequency.setStatus(_A)
_SfpsVLANTopAgentPortPortOptions_Type=Integer32
_SfpsVLANTopAgentPortPortOptions_Object=MibTableColumn
sfpsVLANTopAgentPortPortOptions=_SfpsVLANTopAgentPortPortOptions_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2,1,5),_SfpsVLANTopAgentPortPortOptions_Type())
sfpsVLANTopAgentPortPortOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortPortOptions.setStatus(_A)
class _SfpsVLANTopAgentPortNVRAMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('unset',2)))
_SfpsVLANTopAgentPortNVRAMStatus_Type.__name__=_D
_SfpsVLANTopAgentPortNVRAMStatus_Object=MibTableColumn
sfpsVLANTopAgentPortNVRAMStatus=_SfpsVLANTopAgentPortNVRAMStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,2,1,6),_SfpsVLANTopAgentPortNVRAMStatus_Type())
sfpsVLANTopAgentPortNVRAMStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortNVRAMStatus.setStatus(_A)
class _SfpsVLANTopAgentPortTableAPIInVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_N,2)))
_SfpsVLANTopAgentPortTableAPIInVerb_Type.__name__=_D
_SfpsVLANTopAgentPortTableAPIInVerb_Object=MibScalar
sfpsVLANTopAgentPortTableAPIInVerb=_SfpsVLANTopAgentPortTableAPIInVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,3,1),_SfpsVLANTopAgentPortTableAPIInVerb_Type())
sfpsVLANTopAgentPortTableAPIInVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortTableAPIInVerb.setStatus(_A)
_SfpsVLANTopAgentPortTableAPIInLogicalPort_Type=Integer32
_SfpsVLANTopAgentPortTableAPIInLogicalPort_Object=MibScalar
sfpsVLANTopAgentPortTableAPIInLogicalPort=_SfpsVLANTopAgentPortTableAPIInLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,3,2),_SfpsVLANTopAgentPortTableAPIInLogicalPort_Type())
sfpsVLANTopAgentPortTableAPIInLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortTableAPIInLogicalPort.setStatus(_A)
_SfpsVLANTopAgentPortTableAPIInHelloVersion_Type=Integer32
_SfpsVLANTopAgentPortTableAPIInHelloVersion_Object=MibScalar
sfpsVLANTopAgentPortTableAPIInHelloVersion=_SfpsVLANTopAgentPortTableAPIInHelloVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,3,3),_SfpsVLANTopAgentPortTableAPIInHelloVersion_Type())
sfpsVLANTopAgentPortTableAPIInHelloVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortTableAPIInHelloVersion.setStatus(_A)
_SfpsVLANTopAgentPortTableAPIInSendFrequency_Type=Integer32
_SfpsVLANTopAgentPortTableAPIInSendFrequency_Object=MibScalar
sfpsVLANTopAgentPortTableAPIInSendFrequency=_SfpsVLANTopAgentPortTableAPIInSendFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,3,4),_SfpsVLANTopAgentPortTableAPIInSendFrequency_Type())
sfpsVLANTopAgentPortTableAPIInSendFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortTableAPIInSendFrequency.setStatus(_A)
_SfpsVLANTopAgentPortTableAPIInRecvFrequency_Type=Integer32
_SfpsVLANTopAgentPortTableAPIInRecvFrequency_Object=MibScalar
sfpsVLANTopAgentPortTableAPIInRecvFrequency=_SfpsVLANTopAgentPortTableAPIInRecvFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,1,3,5),_SfpsVLANTopAgentPortTableAPIInRecvFrequency_Type())
sfpsVLANTopAgentPortTableAPIInRecvFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANTopAgentPortTableAPIInRecvFrequency.setStatus(_A)
_SfpsRATopAgentNeighborTable_Object=MibTable
sfpsRATopAgentNeighborTable=_SfpsRATopAgentNeighborTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1))
if mibBuilder.loadTexts:sfpsRATopAgentNeighborTable.setStatus(_A)
_SfpsRATopAgentNeighborEntry_Object=MibTableRow
sfpsRATopAgentNeighborEntry=_SfpsRATopAgentNeighborEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1))
sfpsRATopAgentNeighborEntry.setIndexNames((0,_E,_AA),(0,_E,_AB))
if mibBuilder.loadTexts:sfpsRATopAgentNeighborEntry.setStatus(_A)
_SfpsRATopAgentNeighborInPort_Type=Integer32
_SfpsRATopAgentNeighborInPort_Object=MibTableColumn
sfpsRATopAgentNeighborInPort=_SfpsRATopAgentNeighborInPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,1),_SfpsRATopAgentNeighborInPort_Type())
sfpsRATopAgentNeighborInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborInPort.setStatus(_A)
_SfpsRATopAgentNeighborSwitchID_Type=OctetString
_SfpsRATopAgentNeighborSwitchID_Object=MibTableColumn
sfpsRATopAgentNeighborSwitchID=_SfpsRATopAgentNeighborSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,2),_SfpsRATopAgentNeighborSwitchID_Type())
sfpsRATopAgentNeighborSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborSwitchID.setStatus(_A)
_SfpsRATopAgentNeighborPriority_Type=Integer32
_SfpsRATopAgentNeighborPriority_Object=MibTableColumn
sfpsRATopAgentNeighborPriority=_SfpsRATopAgentNeighborPriority_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,3),_SfpsRATopAgentNeighborPriority_Type())
sfpsRATopAgentNeighborPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborPriority.setStatus(_A)
_SfpsRATopAgentNeighborNetworkPort_Type=Integer32
_SfpsRATopAgentNeighborNetworkPort_Object=MibTableColumn
sfpsRATopAgentNeighborNetworkPort=_SfpsRATopAgentNeighborNetworkPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,4),_SfpsRATopAgentNeighborNetworkPort_Type())
sfpsRATopAgentNeighborNetworkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborNetworkPort.setStatus(_A)
_SfpsRATopAgentNeighborCallTag_Type=Integer32
_SfpsRATopAgentNeighborCallTag_Object=MibTableColumn
sfpsRATopAgentNeighborCallTag=_SfpsRATopAgentNeighborCallTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,5),_SfpsRATopAgentNeighborCallTag_Type())
sfpsRATopAgentNeighborCallTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborCallTag.setStatus(_A)
_SfpsRATopAgentNeighborNetHellosRcvd_Type=Integer32
_SfpsRATopAgentNeighborNetHellosRcvd_Object=MibTableColumn
sfpsRATopAgentNeighborNetHellosRcvd=_SfpsRATopAgentNeighborNetHellosRcvd_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,6),_SfpsRATopAgentNeighborNetHellosRcvd_Type())
sfpsRATopAgentNeighborNetHellosRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborNetHellosRcvd.setStatus(_A)
_SfpsRATopAgentNeighborSeqNumMismatch_Type=Integer32
_SfpsRATopAgentNeighborSeqNumMismatch_Object=MibTableColumn
sfpsRATopAgentNeighborSeqNumMismatch=_SfpsRATopAgentNeighborSeqNumMismatch_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,7),_SfpsRATopAgentNeighborSeqNumMismatch_Type())
sfpsRATopAgentNeighborSeqNumMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborSeqNumMismatch.setStatus(_A)
_SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Type=Integer32
_SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Object=MibTableColumn
sfpsRATopAgentNeighborNetHelloAgeTimeOuts=_SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,8),_SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Type())
sfpsRATopAgentNeighborNetHelloAgeTimeOuts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborNetHelloAgeTimeOuts.setStatus(_A)
_SfpsRATopAgentNeighborNetHelloNetPortLosses_Type=Integer32
_SfpsRATopAgentNeighborNetHelloNetPortLosses_Object=MibTableColumn
sfpsRATopAgentNeighborNetHelloNetPortLosses=_SfpsRATopAgentNeighborNetHelloNetPortLosses_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,9),_SfpsRATopAgentNeighborNetHelloNetPortLosses_Type())
sfpsRATopAgentNeighborNetHelloNetPortLosses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborNetHelloNetPortLosses.setStatus(_A)
_SfpsRATopAgentNeighborNetHelloNetPortChanges_Type=Integer32
_SfpsRATopAgentNeighborNetHelloNetPortChanges_Object=MibTableColumn
sfpsRATopAgentNeighborNetHelloNetPortChanges=_SfpsRATopAgentNeighborNetHelloNetPortChanges_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,1,1,10),_SfpsRATopAgentNeighborNetHelloNetPortChanges_Type())
sfpsRATopAgentNeighborNetHelloNetPortChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentNeighborNetHelloNetPortChanges.setStatus(_A)
_SfpsRATopAgentPortTable_Object=MibTable
sfpsRATopAgentPortTable=_SfpsRATopAgentPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2))
if mibBuilder.loadTexts:sfpsRATopAgentPortTable.setStatus(_A)
_SfpsRATopAgentPortEntry_Object=MibTableRow
sfpsRATopAgentPortEntry=_SfpsRATopAgentPortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1))
sfpsRATopAgentPortEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:sfpsRATopAgentPortEntry.setStatus(_A)
_SfpsRATopAgentPortLogicalPort_Type=Integer32
_SfpsRATopAgentPortLogicalPort_Object=MibTableColumn
sfpsRATopAgentPortLogicalPort=_SfpsRATopAgentPortLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,1),_SfpsRATopAgentPortLogicalPort_Type())
sfpsRATopAgentPortLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortLogicalPort.setStatus(_A)
class _SfpsRATopAgentPortHelloVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('version1',1))
_SfpsRATopAgentPortHelloVersion_Type.__name__=_D
_SfpsRATopAgentPortHelloVersion_Object=MibTableColumn
sfpsRATopAgentPortHelloVersion=_SfpsRATopAgentPortHelloVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,2),_SfpsRATopAgentPortHelloVersion_Type())
sfpsRATopAgentPortHelloVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortHelloVersion.setStatus(_A)
_SfpsRATopAgentPortSendFrequency_Type=Integer32
_SfpsRATopAgentPortSendFrequency_Object=MibTableColumn
sfpsRATopAgentPortSendFrequency=_SfpsRATopAgentPortSendFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,3),_SfpsRATopAgentPortSendFrequency_Type())
sfpsRATopAgentPortSendFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortSendFrequency.setStatus(_A)
_SfpsRATopAgentPortRecvFrequency_Type=Integer32
_SfpsRATopAgentPortRecvFrequency_Object=MibTableColumn
sfpsRATopAgentPortRecvFrequency=_SfpsRATopAgentPortRecvFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,4),_SfpsRATopAgentPortRecvFrequency_Type())
sfpsRATopAgentPortRecvFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortRecvFrequency.setStatus(_A)
_SfpsRATopAgentPortPriority_Type=Integer32
_SfpsRATopAgentPortPriority_Object=MibTableColumn
sfpsRATopAgentPortPriority=_SfpsRATopAgentPortPriority_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,5),_SfpsRATopAgentPortPriority_Type())
sfpsRATopAgentPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortPriority.setStatus(_A)
class _SfpsRATopAgentPortPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_U,1),(_Q,2),('poised',3),('primary',4),('backup',5),('down',6),('halted',7),(_V,8),(_AD,9)))
_SfpsRATopAgentPortPortState_Type.__name__=_D
_SfpsRATopAgentPortPortState_Object=MibTableColumn
sfpsRATopAgentPortPortState=_SfpsRATopAgentPortPortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,6),_SfpsRATopAgentPortPortState_Type())
sfpsRATopAgentPortPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortPortState.setStatus(_A)
_SfpsRATopAgentPortPrimarySwitch_Type=SfpsAddress
_SfpsRATopAgentPortPrimarySwitch_Object=MibTableColumn
sfpsRATopAgentPortPrimarySwitch=_SfpsRATopAgentPortPrimarySwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,7),_SfpsRATopAgentPortPrimarySwitch_Type())
sfpsRATopAgentPortPrimarySwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortPrimarySwitch.setStatus(_A)
_SfpsRATopAgentPortNetHelloRecvFreq_Type=Integer32
_SfpsRATopAgentPortNetHelloRecvFreq_Object=MibTableColumn
sfpsRATopAgentPortNetHelloRecvFreq=_SfpsRATopAgentPortNetHelloRecvFreq_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,8),_SfpsRATopAgentPortNetHelloRecvFreq_Type())
sfpsRATopAgentPortNetHelloRecvFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortNetHelloRecvFreq.setStatus(_A)
_SfpsRATopAgentPortStateChangeCount_Type=Integer32
_SfpsRATopAgentPortStateChangeCount_Object=MibTableColumn
sfpsRATopAgentPortStateChangeCount=_SfpsRATopAgentPortStateChangeCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,9),_SfpsRATopAgentPortStateChangeCount_Type())
sfpsRATopAgentPortStateChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortStateChangeCount.setStatus(_A)
class _SfpsRATopAgentPortNVRAMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('unset',2)))
_SfpsRATopAgentPortNVRAMStatus_Type.__name__=_D
_SfpsRATopAgentPortNVRAMStatus_Object=MibTableColumn
sfpsRATopAgentPortNVRAMStatus=_SfpsRATopAgentPortNVRAMStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,2,1,10),_SfpsRATopAgentPortNVRAMStatus_Type())
sfpsRATopAgentPortNVRAMStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortNVRAMStatus.setStatus(_A)
class _SfpsRATopAgentPortTableAPIInVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_m,3)))
_SfpsRATopAgentPortTableAPIInVerb_Type.__name__=_D
_SfpsRATopAgentPortTableAPIInVerb_Object=MibScalar
sfpsRATopAgentPortTableAPIInVerb=_SfpsRATopAgentPortTableAPIInVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,3,1),_SfpsRATopAgentPortTableAPIInVerb_Type())
sfpsRATopAgentPortTableAPIInVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIInVerb.setStatus(_A)
_SfpsRATopAgentPortTableAPIInLogicalPort_Type=Integer32
_SfpsRATopAgentPortTableAPIInLogicalPort_Object=MibScalar
sfpsRATopAgentPortTableAPIInLogicalPort=_SfpsRATopAgentPortTableAPIInLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,3,2),_SfpsRATopAgentPortTableAPIInLogicalPort_Type())
sfpsRATopAgentPortTableAPIInLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIInLogicalPort.setStatus(_A)
_SfpsRATopAgentPortTableAPIInHelloVersion_Type=Integer32
_SfpsRATopAgentPortTableAPIInHelloVersion_Object=MibScalar
sfpsRATopAgentPortTableAPIInHelloVersion=_SfpsRATopAgentPortTableAPIInHelloVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,3,3),_SfpsRATopAgentPortTableAPIInHelloVersion_Type())
sfpsRATopAgentPortTableAPIInHelloVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIInHelloVersion.setStatus(_A)
_SfpsRATopAgentPortTableAPIInSendFrequency_Type=Integer32
_SfpsRATopAgentPortTableAPIInSendFrequency_Object=MibScalar
sfpsRATopAgentPortTableAPIInSendFrequency=_SfpsRATopAgentPortTableAPIInSendFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,3,4),_SfpsRATopAgentPortTableAPIInSendFrequency_Type())
sfpsRATopAgentPortTableAPIInSendFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIInSendFrequency.setStatus(_A)
_SfpsRATopAgentPortTableAPIInRecvFrequency_Type=Integer32
_SfpsRATopAgentPortTableAPIInRecvFrequency_Object=MibScalar
sfpsRATopAgentPortTableAPIInRecvFrequency=_SfpsRATopAgentPortTableAPIInRecvFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,3,5),_SfpsRATopAgentPortTableAPIInRecvFrequency_Type())
sfpsRATopAgentPortTableAPIInRecvFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIInRecvFrequency.setStatus(_A)
_SfpsRATopAgentPortTableAPIInPriority_Type=Integer32
_SfpsRATopAgentPortTableAPIInPriority_Object=MibScalar
sfpsRATopAgentPortTableAPIInPriority=_SfpsRATopAgentPortTableAPIInPriority_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,3,6),_SfpsRATopAgentPortTableAPIInPriority_Type())
sfpsRATopAgentPortTableAPIInPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIInPriority.setStatus(_A)
_SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Type=Integer32
_SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Object=MibScalar
sfpsRATopAgentPortTableAPIInNetHelloRecvFreq=_SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,3,7),_SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Type())
sfpsRATopAgentPortTableAPIInNetHelloRecvFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIInNetHelloRecvFreq.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutLogicalPort_Type=Integer32
_SfpsRATopAgentPortTableAPIOutLogicalPort_Object=MibScalar
sfpsRATopAgentPortTableAPIOutLogicalPort=_SfpsRATopAgentPortTableAPIOutLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,1),_SfpsRATopAgentPortTableAPIOutLogicalPort_Type())
sfpsRATopAgentPortTableAPIOutLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutLogicalPort.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutHelloVersion_Type=Integer32
_SfpsRATopAgentPortTableAPIOutHelloVersion_Object=MibScalar
sfpsRATopAgentPortTableAPIOutHelloVersion=_SfpsRATopAgentPortTableAPIOutHelloVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,2),_SfpsRATopAgentPortTableAPIOutHelloVersion_Type())
sfpsRATopAgentPortTableAPIOutHelloVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutHelloVersion.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutSendFrequency_Type=Integer32
_SfpsRATopAgentPortTableAPIOutSendFrequency_Object=MibScalar
sfpsRATopAgentPortTableAPIOutSendFrequency=_SfpsRATopAgentPortTableAPIOutSendFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,3),_SfpsRATopAgentPortTableAPIOutSendFrequency_Type())
sfpsRATopAgentPortTableAPIOutSendFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutSendFrequency.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutRecvFrequency_Type=Integer32
_SfpsRATopAgentPortTableAPIOutRecvFrequency_Object=MibScalar
sfpsRATopAgentPortTableAPIOutRecvFrequency=_SfpsRATopAgentPortTableAPIOutRecvFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,4),_SfpsRATopAgentPortTableAPIOutRecvFrequency_Type())
sfpsRATopAgentPortTableAPIOutRecvFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutRecvFrequency.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutPriority_Type=Integer32
_SfpsRATopAgentPortTableAPIOutPriority_Object=MibScalar
sfpsRATopAgentPortTableAPIOutPriority=_SfpsRATopAgentPortTableAPIOutPriority_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,5),_SfpsRATopAgentPortTableAPIOutPriority_Type())
sfpsRATopAgentPortTableAPIOutPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutPriority.setStatus(_A)
class _SfpsRATopAgentPortTableAPIOutPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_U,1),(_Q,2),('poised',3),('primary',4),('backup',5),('down',6),('halted',7),(_V,8),(_AD,9)))
_SfpsRATopAgentPortTableAPIOutPortState_Type.__name__=_D
_SfpsRATopAgentPortTableAPIOutPortState_Object=MibScalar
sfpsRATopAgentPortTableAPIOutPortState=_SfpsRATopAgentPortTableAPIOutPortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,6),_SfpsRATopAgentPortTableAPIOutPortState_Type())
sfpsRATopAgentPortTableAPIOutPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutPortState.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutPrimarySwitch_Type=SfpsAddress
_SfpsRATopAgentPortTableAPIOutPrimarySwitch_Object=MibScalar
sfpsRATopAgentPortTableAPIOutPrimarySwitch=_SfpsRATopAgentPortTableAPIOutPrimarySwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,7),_SfpsRATopAgentPortTableAPIOutPrimarySwitch_Type())
sfpsRATopAgentPortTableAPIOutPrimarySwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutPrimarySwitch.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Type=Integer32
_SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Object=MibScalar
sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq=_SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,8),_SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Type())
sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq.setStatus(_A)
_SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Type=Integer32
_SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Object=MibScalar
sfpsRATopAgentPortTableAPIOutPortStateChangeCount=_SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,2,4,9),_SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Type())
sfpsRATopAgentPortTableAPIOutPortStateChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRATopAgentPortTableAPIOutPortStateChangeCount.setStatus(_A)
_SfpsESPTopAgentPortTable_Object=MibTable
sfpsESPTopAgentPortTable=_SfpsESPTopAgentPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,3,2))
if mibBuilder.loadTexts:sfpsESPTopAgentPortTable.setStatus(_A)
_SfpsESPTopAgentPortEntry_Object=MibTableRow
sfpsESPTopAgentPortEntry=_SfpsESPTopAgentPortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,3,2,1))
sfpsESPTopAgentPortEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:sfpsESPTopAgentPortEntry.setStatus(_A)
_SfpsESPTopAgentPortPort_Type=Integer32
_SfpsESPTopAgentPortPort_Object=MibTableColumn
sfpsESPTopAgentPortPort=_SfpsESPTopAgentPortPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,3,2,1,1),_SfpsESPTopAgentPortPort_Type())
sfpsESPTopAgentPortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsESPTopAgentPortPort.setStatus(_A)
class _SfpsESPTopAgentPortHelloVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A9,1),('version2',2),('version3',3),('version4',4)))
_SfpsESPTopAgentPortHelloVersion_Type.__name__=_D
_SfpsESPTopAgentPortHelloVersion_Object=MibTableColumn
sfpsESPTopAgentPortHelloVersion=_SfpsESPTopAgentPortHelloVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,3,2,1,2),_SfpsESPTopAgentPortHelloVersion_Type())
sfpsESPTopAgentPortHelloVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsESPTopAgentPortHelloVersion.setStatus(_A)
_SfpsESPTopAgentPortSendFrequency_Type=Integer32
_SfpsESPTopAgentPortSendFrequency_Object=MibTableColumn
sfpsESPTopAgentPortSendFrequency=_SfpsESPTopAgentPortSendFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,3,2,1,3),_SfpsESPTopAgentPortSendFrequency_Type())
sfpsESPTopAgentPortSendFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsESPTopAgentPortSendFrequency.setStatus(_A)
_SfpsESPTopAgentPortRecvFrequency_Type=Integer32
_SfpsESPTopAgentPortRecvFrequency_Object=MibTableColumn
sfpsESPTopAgentPortRecvFrequency=_SfpsESPTopAgentPortRecvFrequency_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,3,3,2,1,4),_SfpsESPTopAgentPortRecvFrequency_Type())
sfpsESPTopAgentPortRecvFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsESPTopAgentPortRecvFrequency.setStatus(_A)
_SfpsVMTopServerDeltaTable_Object=MibTable
sfpsVMTopServerDeltaTable=_SfpsVMTopServerDeltaTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1))
if mibBuilder.loadTexts:sfpsVMTopServerDeltaTable.setStatus(_A)
_SfpsVMTopServerDeltaEntry_Object=MibTableRow
sfpsVMTopServerDeltaEntry=_SfpsVMTopServerDeltaEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1,1))
sfpsVMTopServerDeltaEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:sfpsVMTopServerDeltaEntry.setStatus(_A)
_SfpsVMTopServerDeltaIndex_Type=Integer32
_SfpsVMTopServerDeltaIndex_Object=MibTableColumn
sfpsVMTopServerDeltaIndex=_SfpsVMTopServerDeltaIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1,1,1),_SfpsVMTopServerDeltaIndex_Type())
sfpsVMTopServerDeltaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerDeltaIndex.setStatus(_A)
_SfpsVMTopServerDeltaInPort_Type=Integer32
_SfpsVMTopServerDeltaInPort_Object=MibTableColumn
sfpsVMTopServerDeltaInPort=_SfpsVMTopServerDeltaInPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1,1,2),_SfpsVMTopServerDeltaInPort_Type())
sfpsVMTopServerDeltaInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerDeltaInPort.setStatus(_A)
_SfpsVMTopServerDeltaSwitchID_Type=DisplayString
_SfpsVMTopServerDeltaSwitchID_Object=MibTableColumn
sfpsVMTopServerDeltaSwitchID=_SfpsVMTopServerDeltaSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1,1,3),_SfpsVMTopServerDeltaSwitchID_Type())
sfpsVMTopServerDeltaSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerDeltaSwitchID.setStatus(_A)
class _SfpsVMTopServerDeltaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_U,2),(_V,3)))
_SfpsVMTopServerDeltaState_Type.__name__=_D
_SfpsVMTopServerDeltaState_Object=MibTableColumn
sfpsVMTopServerDeltaState=_SfpsVMTopServerDeltaState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1,1,4),_SfpsVMTopServerDeltaState_Type())
sfpsVMTopServerDeltaState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerDeltaState.setStatus(_A)
_SfpsVMTopServerDeltaIPAddress_Type=IpAddress
_SfpsVMTopServerDeltaIPAddress_Object=MibTableColumn
sfpsVMTopServerDeltaIPAddress=_SfpsVMTopServerDeltaIPAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1,1,5),_SfpsVMTopServerDeltaIPAddress_Type())
sfpsVMTopServerDeltaIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerDeltaIPAddress.setStatus(_A)
_SfpsVMTopServerDeltaAgent_Type=DisplayString
_SfpsVMTopServerDeltaAgent_Object=MibTableColumn
sfpsVMTopServerDeltaAgent=_SfpsVMTopServerDeltaAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,1,1,6),_SfpsVMTopServerDeltaAgent_Type())
sfpsVMTopServerDeltaAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerDeltaAgent.setStatus(_A)
_SfpsVMTopServerDeltaCount_Type=Integer32
_SfpsVMTopServerDeltaCount_Object=MibScalar
sfpsVMTopServerDeltaCount=_SfpsVMTopServerDeltaCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,2),_SfpsVMTopServerDeltaCount_Type())
sfpsVMTopServerDeltaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerDeltaCount.setStatus(_A)
class _SfpsVMTopServerTableLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lock',1),('unlock',2)))
_SfpsVMTopServerTableLock_Type.__name__=_D
_SfpsVMTopServerTableLock_Object=MibScalar
sfpsVMTopServerTableLock=_SfpsVMTopServerTableLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,3),_SfpsVMTopServerTableLock_Type())
sfpsVMTopServerTableLock.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsVMTopServerTableLock.setStatus(_A)
class _SfpsVMTopServerPortChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noPortChange',1),('portChange',2)))
_SfpsVMTopServerPortChange_Type.__name__=_D
_SfpsVMTopServerPortChange_Object=MibScalar
sfpsVMTopServerPortChange=_SfpsVMTopServerPortChange_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,4),_SfpsVMTopServerPortChange_Type())
sfpsVMTopServerPortChange.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerPortChange.setStatus(_A)
class _SfpsVMTopServerTableFull_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tableFull',1),('tableNotFull',2)))
_SfpsVMTopServerTableFull_Type.__name__=_D
_SfpsVMTopServerTableFull_Object=MibScalar
sfpsVMTopServerTableFull=_SfpsVMTopServerTableFull_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,5),_SfpsVMTopServerTableFull_Type())
sfpsVMTopServerTableFull.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVMTopServerTableFull.setStatus(_A)
_SfpsVMTopServerChangeCnt_Type=Integer32
_SfpsVMTopServerChangeCnt_Object=MibScalar
sfpsVMTopServerChangeCnt=_SfpsVMTopServerChangeCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,4,1,6),_SfpsVMTopServerChangeCnt_Type())
sfpsVMTopServerChangeCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsVMTopServerChangeCnt.setStatus(_A)
class _SfpsTAPITestInVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_F,1),(_N,2),('portUp',3),('portDown',4),('changePortAccess',5),('resolvePortNameToPort',6),('resolveBaseMACToPorts',7),('resolveINBNeighbor',8),('getPortNeighbors',9),('getTotalNeighbors',10),('getLogicalNetworkPortMask',11),('getPhysicalNetworkPortMask',12),('getPhysicalStandByPortMask',13),('getLogicalINBNetworkPortMask',14),('getPhysicalINBNetworkPortMask',15),('enableAccessPortOnly',16),('disableAccessPortOnly',17),('getPhysicalPortDownPortMask',18),('getLogicalSameFCLPortMask',19),('getNeighborFCL',20)))
_SfpsTAPITestInVerb_Type.__name__=_D
_SfpsTAPITestInVerb_Object=MibScalar
sfpsTAPITestInVerb=_SfpsTAPITestInVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,1,1),_SfpsTAPITestInVerb_Type())
sfpsTAPITestInVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestInVerb.setStatus(_A)
_SfpsTAPITestInLogicalPort_Type=Integer32
_SfpsTAPITestInLogicalPort_Object=MibScalar
sfpsTAPITestInLogicalPort=_SfpsTAPITestInLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,1,2),_SfpsTAPITestInLogicalPort_Type())
sfpsTAPITestInLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestInLogicalPort.setStatus(_A)
_SfpsTAPITestInSwitchID_Type=DisplayString
_SfpsTAPITestInSwitchID_Object=MibScalar
sfpsTAPITestInSwitchID=_SfpsTAPITestInSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,1,3),_SfpsTAPITestInSwitchID_Type())
sfpsTAPITestInSwitchID.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestInSwitchID.setStatus(_A)
_SfpsTAPITestInMAC_Type=DisplayString
_SfpsTAPITestInMAC_Object=MibScalar
sfpsTAPITestInMAC=_SfpsTAPITestInMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,1,4),_SfpsTAPITestInMAC_Type())
sfpsTAPITestInMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestInMAC.setStatus(_A)
class _SfpsTAPITestInPortTypeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_S,4),(_K,5),(_G,6),(_L,7),(_M,8),(_J,9),(_R,10)))
_SfpsTAPITestInPortTypeState_Type.__name__=_D
_SfpsTAPITestInPortTypeState_Object=MibScalar
sfpsTAPITestInPortTypeState=_SfpsTAPITestInPortTypeState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,1,5),_SfpsTAPITestInPortTypeState_Type())
sfpsTAPITestInPortTypeState.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestInPortTypeState.setStatus(_A)
_SfpsTAPITestInTopologyAgentID_Type=Integer32
_SfpsTAPITestInTopologyAgentID_Object=MibScalar
sfpsTAPITestInTopologyAgentID=_SfpsTAPITestInTopologyAgentID_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,1,6),_SfpsTAPITestInTopologyAgentID_Type())
sfpsTAPITestInTopologyAgentID.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestInTopologyAgentID.setStatus(_A)
_SfpsTAPITestInUNIT321_Type=Integer32
_SfpsTAPITestInUNIT321_Object=MibScalar
sfpsTAPITestInUNIT321=_SfpsTAPITestInUNIT321_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,1,7),_SfpsTAPITestInUNIT321_Type())
sfpsTAPITestInUNIT321.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestInUNIT321.setStatus(_A)
_SfpsTAPITestOutOutputInteger_Type=Integer32
_SfpsTAPITestOutOutputInteger_Object=MibScalar
sfpsTAPITestOutOutputInteger=_SfpsTAPITestOutOutputInteger_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,2,1),_SfpsTAPITestOutOutputInteger_Type())
sfpsTAPITestOutOutputInteger.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestOutOutputInteger.setStatus(_A)
_SfpsTAPITestOutOutPutString_Type=DisplayString
_SfpsTAPITestOutOutPutString_Object=MibScalar
sfpsTAPITestOutOutPutString=_SfpsTAPITestOutOutPutString_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,1,2,2),_SfpsTAPITestOutOutPutString_Type())
sfpsTAPITestOutOutPutString.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTAPITestOutOutPutString.setStatus(_A)
class _SfpsTopologyServerTestInVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_N,2),('clear',3),('lostEvent',4),('foundEvent',5),('portEvent',6)))
_SfpsTopologyServerTestInVerb_Type.__name__=_D
_SfpsTopologyServerTestInVerb_Object=MibScalar
sfpsTopologyServerTestInVerb=_SfpsTopologyServerTestInVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,1,1),_SfpsTopologyServerTestInVerb_Type())
sfpsTopologyServerTestInVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestInVerb.setStatus(_A)
_SfpsTopologyServerTestInServer_Type=DisplayString
_SfpsTopologyServerTestInServer_Object=MibScalar
sfpsTopologyServerTestInServer=_SfpsTopologyServerTestInServer_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,1,2),_SfpsTopologyServerTestInServer_Type())
sfpsTopologyServerTestInServer.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestInServer.setStatus(_A)
_SfpsTopologyServerTestInNumberOfRelays_Type=Integer32
_SfpsTopologyServerTestInNumberOfRelays_Object=MibScalar
sfpsTopologyServerTestInNumberOfRelays=_SfpsTopologyServerTestInNumberOfRelays_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,1,3),_SfpsTopologyServerTestInNumberOfRelays_Type())
sfpsTopologyServerTestInNumberOfRelays.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestInNumberOfRelays.setStatus(_A)
_SfpsTopologyServerTestTable_Object=MibTable
sfpsTopologyServerTestTable=_SfpsTopologyServerTestTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2))
if mibBuilder.loadTexts:sfpsTopologyServerTestTable.setStatus(_A)
_SfpsTopologyServerTestEntry_Object=MibTableRow
sfpsTopologyServerTestEntry=_SfpsTopologyServerTestEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1))
sfpsTopologyServerTestEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:sfpsTopologyServerTestEntry.setStatus(_A)
_SfpsTopologyServerTestRelayNumber_Type=Integer32
_SfpsTopologyServerTestRelayNumber_Object=MibTableColumn
sfpsTopologyServerTestRelayNumber=_SfpsTopologyServerTestRelayNumber_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,1),_SfpsTopologyServerTestRelayNumber_Type())
sfpsTopologyServerTestRelayNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestRelayNumber.setStatus(_A)
class _SfpsTopologyServerTestServerFlavor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_SfpsTopologyServerTestServerFlavor_Type.__name__=_D
_SfpsTopologyServerTestServerFlavor_Object=MibTableColumn
sfpsTopologyServerTestServerFlavor=_SfpsTopologyServerTestServerFlavor_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,2),_SfpsTopologyServerTestServerFlavor_Type())
sfpsTopologyServerTestServerFlavor.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestServerFlavor.setStatus(_A)
_SfpsTopologyServerTestPortNumber_Type=Integer32
_SfpsTopologyServerTestPortNumber_Object=MibTableColumn
sfpsTopologyServerTestPortNumber=_SfpsTopologyServerTestPortNumber_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,3),_SfpsTopologyServerTestPortNumber_Type())
sfpsTopologyServerTestPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestPortNumber.setStatus(_A)
_SfpsTopologyServerTestPortName_Type=DisplayString
_SfpsTopologyServerTestPortName_Object=MibTableColumn
sfpsTopologyServerTestPortName=_SfpsTopologyServerTestPortName_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,4),_SfpsTopologyServerTestPortName_Type())
sfpsTopologyServerTestPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestPortName.setStatus(_A)
_SfpsTopologyServerTestIpAddr_Type=DisplayString
_SfpsTopologyServerTestIpAddr_Object=MibTableColumn
sfpsTopologyServerTestIpAddr=_SfpsTopologyServerTestIpAddr_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,5),_SfpsTopologyServerTestIpAddr_Type())
sfpsTopologyServerTestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestIpAddr.setStatus(_A)
class _SfpsTopologyServerTestLostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_O,2),(_P,3)))
_SfpsTopologyServerTestLostPort_Type.__name__=_D
_SfpsTopologyServerTestLostPort_Object=MibTableColumn
sfpsTopologyServerTestLostPort=_SfpsTopologyServerTestLostPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,6),_SfpsTopologyServerTestLostPort_Type())
sfpsTopologyServerTestLostPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestLostPort.setStatus(_A)
class _SfpsTopologyServerTestOldState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_S,4),(_K,5),(_G,6),(_L,7),(_M,8),(_J,9)))
_SfpsTopologyServerTestOldState_Type.__name__=_D
_SfpsTopologyServerTestOldState_Object=MibTableColumn
sfpsTopologyServerTestOldState=_SfpsTopologyServerTestOldState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,7),_SfpsTopologyServerTestOldState_Type())
sfpsTopologyServerTestOldState.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestOldState.setStatus(_A)
class _SfpsTopologyServerTestNewState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_S,4),(_K,5),(_G,6),(_L,7),(_M,8),(_J,9)))
_SfpsTopologyServerTestNewState_Type.__name__=_D
_SfpsTopologyServerTestNewState_Object=MibTableColumn
sfpsTopologyServerTestNewState=_SfpsTopologyServerTestNewState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,8),_SfpsTopologyServerTestNewState_Type())
sfpsTopologyServerTestNewState.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestNewState.setStatus(_A)
_SfpsTopologyServerTestTopologyAgent_Type=DisplayString
_SfpsTopologyServerTestTopologyAgent_Object=MibTableColumn
sfpsTopologyServerTestTopologyAgent=_SfpsTopologyServerTestTopologyAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,2,1,9),_SfpsTopologyServerTestTopologyAgent_Type())
sfpsTopologyServerTestTopologyAgent.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopologyAgent.setStatus(_A)
_SfpsTopologyServerTestTopRelayTable_Object=MibTable
sfpsTopologyServerTestTopRelayTable=_SfpsTopologyServerTestTopRelayTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3))
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayTable.setStatus(_A)
_SfpsTopologyServerTestTopRelayEntry_Object=MibTableRow
sfpsTopologyServerTestTopRelayEntry=_SfpsTopologyServerTestTopRelayEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1))
sfpsTopologyServerTestTopRelayEntry.setIndexNames((0,_E,_AH))
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayEntry.setStatus(_A)
_SfpsTopologyServerTestTopRelayRelayNumber_Type=Integer32
_SfpsTopologyServerTestTopRelayRelayNumber_Object=MibTableColumn
sfpsTopologyServerTestTopRelayRelayNumber=_SfpsTopologyServerTestTopRelayRelayNumber_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,1),_SfpsTopologyServerTestTopRelayRelayNumber_Type())
sfpsTopologyServerTestTopRelayRelayNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayRelayNumber.setStatus(_A)
_SfpsTopologyServerTestTopRelayEvent_Type=Integer32
_SfpsTopologyServerTestTopRelayEvent_Object=MibTableColumn
sfpsTopologyServerTestTopRelayEvent=_SfpsTopologyServerTestTopRelayEvent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,2),_SfpsTopologyServerTestTopRelayEvent_Type())
sfpsTopologyServerTestTopRelayEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayEvent.setStatus(_A)
class _SfpsTopologyServerTestTopRelayDeltaOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),(_d,4),(_e,5),(_f,6),(_g,7),('loopedPortNghLoss',8),(_h,9),(_i,10),(_j,11),(_k,12)))
_SfpsTopologyServerTestTopRelayDeltaOptions_Type.__name__=_D
_SfpsTopologyServerTestTopRelayDeltaOptions_Object=MibTableColumn
sfpsTopologyServerTestTopRelayDeltaOptions=_SfpsTopologyServerTestTopRelayDeltaOptions_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,3),_SfpsTopologyServerTestTopRelayDeltaOptions_Type())
sfpsTopologyServerTestTopRelayDeltaOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayDeltaOptions.setStatus(_A)
_SfpsTopologyServerTestTopRelayCurrentOptions_Type=Integer32
_SfpsTopologyServerTestTopRelayCurrentOptions_Object=MibTableColumn
sfpsTopologyServerTestTopRelayCurrentOptions=_SfpsTopologyServerTestTopRelayCurrentOptions_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,4),_SfpsTopologyServerTestTopRelayCurrentOptions_Type())
sfpsTopologyServerTestTopRelayCurrentOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayCurrentOptions.setStatus(_A)
_SfpsTopologyServerTestTopRelayLogicalPort_Type=Integer32
_SfpsTopologyServerTestTopRelayLogicalPort_Object=MibTableColumn
sfpsTopologyServerTestTopRelayLogicalPort=_SfpsTopologyServerTestTopRelayLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,5),_SfpsTopologyServerTestTopRelayLogicalPort_Type())
sfpsTopologyServerTestTopRelayLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayLogicalPort.setStatus(_A)
_SfpsTopologyServerTestTopRelayPortName_Type=OctetString
_SfpsTopologyServerTestTopRelayPortName_Object=MibTableColumn
sfpsTopologyServerTestTopRelayPortName=_SfpsTopologyServerTestTopRelayPortName_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,6),_SfpsTopologyServerTestTopRelayPortName_Type())
sfpsTopologyServerTestTopRelayPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayPortName.setStatus(_A)
_SfpsTopologyServerTestTopRelayIPAddr_Type=IpAddress
_SfpsTopologyServerTestTopRelayIPAddr_Object=MibTableColumn
sfpsTopologyServerTestTopRelayIPAddr=_SfpsTopologyServerTestTopRelayIPAddr_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,7),_SfpsTopologyServerTestTopRelayIPAddr_Type())
sfpsTopologyServerTestTopRelayIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayIPAddr.setStatus(_A)
_SfpsTopologyServerTestTopRelayChassisMAC_Type=SfpsAddress
_SfpsTopologyServerTestTopRelayChassisMAC_Object=MibTableColumn
sfpsTopologyServerTestTopRelayChassisMAC=_SfpsTopologyServerTestTopRelayChassisMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,8),_SfpsTopologyServerTestTopRelayChassisMAC_Type())
sfpsTopologyServerTestTopRelayChassisMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayChassisMAC.setStatus(_A)
_SfpsTopologyServerTestTopRelayChassisIP_Type=IpAddress
_SfpsTopologyServerTestTopRelayChassisIP_Object=MibTableColumn
sfpsTopologyServerTestTopRelayChassisIP=_SfpsTopologyServerTestTopRelayChassisIP_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,9),_SfpsTopologyServerTestTopRelayChassisIP_Type())
sfpsTopologyServerTestTopRelayChassisIP.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayChassisIP.setStatus(_A)
_SfpsTopologyServerTestTopRelayFLevel_Type=Integer32
_SfpsTopologyServerTestTopRelayFLevel_Object=MibTableColumn
sfpsTopologyServerTestTopRelayFLevel=_SfpsTopologyServerTestTopRelayFLevel_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,10),_SfpsTopologyServerTestTopRelayFLevel_Type())
sfpsTopologyServerTestTopRelayFLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayFLevel.setStatus(_A)
_SfpsTopologyServerTestTopRelayTopologyAgent_Type=OctetString
_SfpsTopologyServerTestTopRelayTopologyAgent_Object=MibTableColumn
sfpsTopologyServerTestTopRelayTopologyAgent=_SfpsTopologyServerTestTopRelayTopologyAgent_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,3,1,11),_SfpsTopologyServerTestTopRelayTopologyAgent_Type())
sfpsTopologyServerTestTopRelayTopologyAgent.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerTestTopRelayTopologyAgent.setStatus(_A)
_SfpsTopologyServerPortEventRelayLogicalPort_Type=Integer32
_SfpsTopologyServerPortEventRelayLogicalPort_Object=MibScalar
sfpsTopologyServerPortEventRelayLogicalPort=_SfpsTopologyServerPortEventRelayLogicalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,4,1),_SfpsTopologyServerPortEventRelayLogicalPort_Type())
sfpsTopologyServerPortEventRelayLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerPortEventRelayLogicalPort.setStatus(_A)
class _SfpsTopologyServerPortEventRelayOldState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_S,4),(_K,5),(_G,6),(_AI,7),(_J,8),(_R,10)))
_SfpsTopologyServerPortEventRelayOldState_Type.__name__=_D
_SfpsTopologyServerPortEventRelayOldState_Object=MibScalar
sfpsTopologyServerPortEventRelayOldState=_SfpsTopologyServerPortEventRelayOldState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,4,2),_SfpsTopologyServerPortEventRelayOldState_Type())
sfpsTopologyServerPortEventRelayOldState.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerPortEventRelayOldState.setStatus(_A)
class _SfpsTopologyServerPortEventRelayNewState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_S,4),(_K,5),(_G,6),(_AI,7),(_J,8),(_R,10)))
_SfpsTopologyServerPortEventRelayNewState_Type.__name__=_D
_SfpsTopologyServerPortEventRelayNewState_Object=MibScalar
sfpsTopologyServerPortEventRelayNewState=_SfpsTopologyServerPortEventRelayNewState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,5,2,4,3),_SfpsTopologyServerPortEventRelayNewState_Type())
sfpsTopologyServerPortEventRelayNewState.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTopologyServerPortEventRelayNewState.setStatus(_A)
_SfpsNeighborEventsFoundEvents_Type=Integer32
_SfpsNeighborEventsFoundEvents_Object=MibScalar
sfpsNeighborEventsFoundEvents=_SfpsNeighborEventsFoundEvents_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,6,1,1),_SfpsNeighborEventsFoundEvents_Type())
sfpsNeighborEventsFoundEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNeighborEventsFoundEvents.setStatus(_A)
_SfpsNeighborEventsLostEvents_Type=Integer32
_SfpsNeighborEventsLostEvents_Object=MibScalar
sfpsNeighborEventsLostEvents=_SfpsNeighborEventsLostEvents_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,6,1,2),_SfpsNeighborEventsLostEvents_Type())
sfpsNeighborEventsLostEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNeighborEventsLostEvents.setStatus(_A)
_SfpsTopologyFCLTable_Object=MibTable
sfpsTopologyFCLTable=_SfpsTopologyFCLTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,7,1))
if mibBuilder.loadTexts:sfpsTopologyFCLTable.setStatus(_A)
_SfpsTopologyFCLEntry_Object=MibTableRow
sfpsTopologyFCLEntry=_SfpsTopologyFCLEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,7,1,1))
sfpsTopologyFCLEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:sfpsTopologyFCLEntry.setStatus(_A)
_SfpsTopologyFCLFunctionalLevel_Type=Integer32
_SfpsTopologyFCLFunctionalLevel_Object=MibTableColumn
sfpsTopologyFCLFunctionalLevel=_SfpsTopologyFCLFunctionalLevel_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,7,1,1,1),_SfpsTopologyFCLFunctionalLevel_Type())
sfpsTopologyFCLFunctionalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyFCLFunctionalLevel.setStatus(_A)
class _SfpsTopologyFCLCompatability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('compatable',1),('notCompatable',2)))
_SfpsTopologyFCLCompatability_Type.__name__=_D
_SfpsTopologyFCLCompatability_Object=MibTableColumn
sfpsTopologyFCLCompatability=_SfpsTopologyFCLCompatability_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,7,1,1,2),_SfpsTopologyFCLCompatability_Type())
sfpsTopologyFCLCompatability.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyFCLCompatability.setStatus(_A)
class _SfpsTopologyFCLThisPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_AK,4),(_AL,5),(_G,6),(_L,7),(_M,8),(_J,9)))
_SfpsTopologyFCLThisPortState_Type.__name__=_D
_SfpsTopologyFCLThisPortState_Object=MibTableColumn
sfpsTopologyFCLThisPortState=_SfpsTopologyFCLThisPortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,7,1,1,3),_SfpsTopologyFCLThisPortState_Type())
sfpsTopologyFCLThisPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyFCLThisPortState.setStatus(_A)
class _SfpsTopologyFCLSendPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3),(_AK,4),(_AL,5),(_G,6),(_L,7),(_M,8),(_J,9)))
_SfpsTopologyFCLSendPortState_Type.__name__=_D
_SfpsTopologyFCLSendPortState_Object=MibTableColumn
sfpsTopologyFCLSendPortState=_SfpsTopologyFCLSendPortState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,12,7,1,1,4),_SfpsTopologyFCLSendPortState_Type())
sfpsTopologyFCLSendPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyFCLSendPortState.setStatus(_A)
_SfpsDirViolationTable_Object=MibTable
sfpsDirViolationTable=_SfpsDirViolationTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1))
if mibBuilder.loadTexts:sfpsDirViolationTable.setStatus(_A)
_SfpsDirViolationEntry_Object=MibTableRow
sfpsDirViolationEntry=_SfpsDirViolationEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1))
sfpsDirViolationEntry.setIndexNames((0,_E,_AM),(0,_E,_AN))
if mibBuilder.loadTexts:sfpsDirViolationEntry.setStatus(_A)
_SfpsDirViolationHash_Type=Integer32
_SfpsDirViolationHash_Object=MibTableColumn
sfpsDirViolationHash=_SfpsDirViolationHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,1),_SfpsDirViolationHash_Type())
sfpsDirViolationHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationHash.setStatus(_A)
_SfpsDirViolationHashIndex_Type=Integer32
_SfpsDirViolationHashIndex_Object=MibTableColumn
sfpsDirViolationHashIndex=_SfpsDirViolationHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,2),_SfpsDirViolationHashIndex_Type())
sfpsDirViolationHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationHashIndex.setStatus(_A)
class _SfpsDirViolationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('userLock',1),(_AO,2),('ipNotLearned',3),('ipInvalid',4),('restrictMobility',5),('userLockSamePort',6),('sapDisabled',7)))
_SfpsDirViolationType_Type.__name__=_D
_SfpsDirViolationType_Object=MibTableColumn
sfpsDirViolationType=_SfpsDirViolationType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,3),_SfpsDirViolationType_Type())
sfpsDirViolationType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationType.setStatus(_A)
_SfpsDirViolationSrcPort_Type=Integer32
_SfpsDirViolationSrcPort_Object=MibTableColumn
sfpsDirViolationSrcPort=_SfpsDirViolationSrcPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,4),_SfpsDirViolationSrcPort_Type())
sfpsDirViolationSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationSrcPort.setStatus(_A)
class _SfpsDirViolationAOType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('aoMacDX',1),('aoIpxSap',2),('aoIpxRIP',3),('aoInetYP',4),(_AP,5),('aoIpxIpx',6),('aoInetIP',7),(_AQ,8),(_AR,9),(_AS,10),('aoAtDDP',11),('aoEmpty',12),('aoVlan',13),(_AT,14),(_AU,15),(_AV,16)))
_SfpsDirViolationAOType_Type.__name__=_D
_SfpsDirViolationAOType_Object=MibTableColumn
sfpsDirViolationAOType=_SfpsDirViolationAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,5),_SfpsDirViolationAOType_Type())
sfpsDirViolationAOType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationAOType.setStatus(_A)
_SfpsDirViolationAOValue_Type=DisplayString
_SfpsDirViolationAOValue_Object=MibTableColumn
sfpsDirViolationAOValue=_SfpsDirViolationAOValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,6),_SfpsDirViolationAOValue_Type())
sfpsDirViolationAOValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationAOValue.setStatus(_A)
_SfpsDirViolationLocalPort_Type=Integer32
_SfpsDirViolationLocalPort_Object=MibTableColumn
sfpsDirViolationLocalPort=_SfpsDirViolationLocalPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,7),_SfpsDirViolationLocalPort_Type())
sfpsDirViolationLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationLocalPort.setStatus(_A)
_SfpsDirViolationCount_Type=Integer32
_SfpsDirViolationCount_Object=MibTableColumn
sfpsDirViolationCount=_SfpsDirViolationCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,8),_SfpsDirViolationCount_Type())
sfpsDirViolationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationCount.setStatus(_A)
_SfpsDirViolationLastSeen_Type=TimeTicks
_SfpsDirViolationLastSeen_Object=MibTableColumn
sfpsDirViolationLastSeen=_SfpsDirViolationLastSeen_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,9),_SfpsDirViolationLastSeen_Type())
sfpsDirViolationLastSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationLastSeen.setStatus(_A)
_SfpsDirViolationFirstSeen_Type=TimeTicks
_SfpsDirViolationFirstSeen_Object=MibTableColumn
sfpsDirViolationFirstSeen=_SfpsDirViolationFirstSeen_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,10),_SfpsDirViolationFirstSeen_Type())
sfpsDirViolationFirstSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationFirstSeen.setStatus(_A)
_SfpsDirViolationSrcMac_Type=OctetString
_SfpsDirViolationSrcMac_Object=MibTableColumn
sfpsDirViolationSrcMac=_SfpsDirViolationSrcMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,11),_SfpsDirViolationSrcMac_Type())
sfpsDirViolationSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationSrcMac.setStatus(_A)
_SfpsDirViolationCPId_Type=OctetString
_SfpsDirViolationCPId_Object=MibTableColumn
sfpsDirViolationCPId=_SfpsDirViolationCPId_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,1,1,12),_SfpsDirViolationCPId_Type())
sfpsDirViolationCPId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationCPId.setStatus(_A)
class _SfpsDirViolationAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_N,2),('delete',3),('reset',4)))
_SfpsDirViolationAPIVerb_Type.__name__=_D
_SfpsDirViolationAPIVerb_Object=MibScalar
sfpsDirViolationAPIVerb=_SfpsDirViolationAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,2,1),_SfpsDirViolationAPIVerb_Type())
sfpsDirViolationAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirViolationAPIVerb.setStatus(_A)
class _SfpsDirViolationAPIViolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_AO,2)))
_SfpsDirViolationAPIViolType_Type.__name__=_D
_SfpsDirViolationAPIViolType_Object=MibScalar
sfpsDirViolationAPIViolType=_SfpsDirViolationAPIViolType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,2,2),_SfpsDirViolationAPIViolType_Type())
sfpsDirViolationAPIViolType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirViolationAPIViolType.setStatus(_A)
_SfpsDirViolationAPISourcePort_Type=Integer32
_SfpsDirViolationAPISourcePort_Object=MibScalar
sfpsDirViolationAPISourcePort=_SfpsDirViolationAPISourcePort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,2,3),_SfpsDirViolationAPISourcePort_Type())
sfpsDirViolationAPISourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirViolationAPISourcePort.setStatus(_A)
_SfpsDirViolationAPIAOType_Type=DisplayString
_SfpsDirViolationAPIAOType_Object=MibScalar
sfpsDirViolationAPIAOType=_SfpsDirViolationAPIAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,2,4),_SfpsDirViolationAPIAOType_Type())
sfpsDirViolationAPIAOType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirViolationAPIAOType.setStatus(_A)
_SfpsDirViolationAPIAOValue_Type=DisplayString
_SfpsDirViolationAPIAOValue_Object=MibScalar
sfpsDirViolationAPIAOValue=_SfpsDirViolationAPIAOValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,2,5),_SfpsDirViolationAPIAOValue_Type())
sfpsDirViolationAPIAOValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirViolationAPIAOValue.setStatus(_A)
_SfpsDirViolationAPIChangeCount_Type=Integer32
_SfpsDirViolationAPIChangeCount_Object=MibScalar
sfpsDirViolationAPIChangeCount=_SfpsDirViolationAPIChangeCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,2,6),_SfpsDirViolationAPIChangeCount_Type())
sfpsDirViolationAPIChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationAPIChangeCount.setStatus(_A)
_SfpsDirViolationAPICPId_Type=DisplayString
_SfpsDirViolationAPICPId_Object=MibScalar
sfpsDirViolationAPICPId=_SfpsDirViolationAPICPId_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,2,7),_SfpsDirViolationAPICPId_Type())
sfpsDirViolationAPICPId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationAPICPId.setStatus(_A)
_SfpsDirViolationDeltaTable_Object=MibTable
sfpsDirViolationDeltaTable=_SfpsDirViolationDeltaTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,3))
if mibBuilder.loadTexts:sfpsDirViolationDeltaTable.setStatus(_A)
_SfpsDirViolationDeltaEntry_Object=MibTableRow
sfpsDirViolationDeltaEntry=_SfpsDirViolationDeltaEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,3,1))
sfpsDirViolationDeltaEntry.setIndexNames((0,_E,_AW))
if mibBuilder.loadTexts:sfpsDirViolationDeltaEntry.setStatus(_A)
_SfpsDirViolationDeltaIndex_Type=Integer32
_SfpsDirViolationDeltaIndex_Object=MibTableColumn
sfpsDirViolationDeltaIndex=_SfpsDirViolationDeltaIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,3,1,1),_SfpsDirViolationDeltaIndex_Type())
sfpsDirViolationDeltaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationDeltaIndex.setStatus(_A)
_SfpsDirViolationDeltaSrcPort_Type=Integer32
_SfpsDirViolationDeltaSrcPort_Object=MibTableColumn
sfpsDirViolationDeltaSrcPort=_SfpsDirViolationDeltaSrcPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,3,1,2),_SfpsDirViolationDeltaSrcPort_Type())
sfpsDirViolationDeltaSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationDeltaSrcPort.setStatus(_A)
class _SfpsDirViolationDeltaAOType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('aoMacDX',1),('aoIpxSap',2),('aoIpxRIP',3),('aoInetYP',4),(_AP,5),('aoIpxIpx',6),('aoInetIP',7),(_AQ,8),(_AR,9),(_AS,10),('aoAtDDP',11),('aoEmpty',12),('aoVlan',13),(_AT,14),(_AU,15),(_AV,16)))
_SfpsDirViolationDeltaAOType_Type.__name__=_D
_SfpsDirViolationDeltaAOType_Object=MibTableColumn
sfpsDirViolationDeltaAOType=_SfpsDirViolationDeltaAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,3,1,3),_SfpsDirViolationDeltaAOType_Type())
sfpsDirViolationDeltaAOType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationDeltaAOType.setStatus(_A)
_SfpsDirViolationDeltaAOValue_Type=Integer32
_SfpsDirViolationDeltaAOValue_Object=MibTableColumn
sfpsDirViolationDeltaAOValue=_SfpsDirViolationDeltaAOValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,3,1,4),_SfpsDirViolationDeltaAOValue_Type())
sfpsDirViolationDeltaAOValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationDeltaAOValue.setStatus(_A)
class _SfpsDirViolationDeltaEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_U,2),(_V,3)))
_SfpsDirViolationDeltaEntryType_Type.__name__=_D
_SfpsDirViolationDeltaEntryType_Object=MibTableColumn
sfpsDirViolationDeltaEntryType=_SfpsDirViolationDeltaEntryType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,3,1,5),_SfpsDirViolationDeltaEntryType_Type())
sfpsDirViolationDeltaEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationDeltaEntryType.setStatus(_A)
_SfpsDirViolationDeltaAPINumEntries_Type=Integer32
_SfpsDirViolationDeltaAPINumEntries_Object=MibScalar
sfpsDirViolationDeltaAPINumEntries=_SfpsDirViolationDeltaAPINumEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,4,1),_SfpsDirViolationDeltaAPINumEntries_Type())
sfpsDirViolationDeltaAPINumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirViolationDeltaAPINumEntries.setStatus(_A)
class _SfpsDirViolationDeltaAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lock',1),('unlock',2)))
_SfpsDirViolationDeltaAPIVerb_Type.__name__=_D
_SfpsDirViolationDeltaAPIVerb_Object=MibScalar
sfpsDirViolationDeltaAPIVerb=_SfpsDirViolationDeltaAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,1,4,2),_SfpsDirViolationDeltaAPIVerb_Type())
sfpsDirViolationDeltaAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirViolationDeltaAPIVerb.setStatus(_A)
_SfpsRestrictedPortTable_Object=MibTable
sfpsRestrictedPortTable=_SfpsRestrictedPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,2,1))
if mibBuilder.loadTexts:sfpsRestrictedPortTable.setStatus(_A)
_SfpsRestrictedPortEntry_Object=MibTableRow
sfpsRestrictedPortEntry=_SfpsRestrictedPortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,2,1,1))
sfpsRestrictedPortEntry.setIndexNames((0,_E,_AX),(0,_E,_AY),(0,_E,_AZ))
if mibBuilder.loadTexts:sfpsRestrictedPortEntry.setStatus(_A)
_SfpsRestrictedPortPort_Type=Integer32
_SfpsRestrictedPortPort_Object=MibTableColumn
sfpsRestrictedPortPort=_SfpsRestrictedPortPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,2,1,1,1),_SfpsRestrictedPortPort_Type())
sfpsRestrictedPortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedPortPort.setStatus(_A)
_SfpsRestrictedPortHash_Type=Integer32
_SfpsRestrictedPortHash_Object=MibTableColumn
sfpsRestrictedPortHash=_SfpsRestrictedPortHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,2,1,1,2),_SfpsRestrictedPortHash_Type())
sfpsRestrictedPortHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedPortHash.setStatus(_A)
_SfpsRestrictedPortHashIndex_Type=Integer32
_SfpsRestrictedPortHashIndex_Object=MibTableColumn
sfpsRestrictedPortHashIndex=_SfpsRestrictedPortHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,2,1,1,3),_SfpsRestrictedPortHashIndex_Type())
sfpsRestrictedPortHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedPortHashIndex.setStatus(_A)
_SfpsRestrictedPortSrcMac_Type=DisplayString
_SfpsRestrictedPortSrcMac_Object=MibTableColumn
sfpsRestrictedPortSrcMac=_SfpsRestrictedPortSrcMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,2,1,1,4),_SfpsRestrictedPortSrcMac_Type())
sfpsRestrictedPortSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedPortSrcMac.setStatus(_A)
class _SfpsDirLockConfigUserLocking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_SfpsDirLockConfigUserLocking_Type.__name__=_D
_SfpsDirLockConfigUserLocking_Object=MibScalar
sfpsDirLockConfigUserLocking=_SfpsDirLockConfigUserLocking_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,3,1),_SfpsDirLockConfigUserLocking_Type())
sfpsDirLockConfigUserLocking.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirLockConfigUserLocking.setStatus(_A)
class _SfpsDirLockConfigRestrictedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_SfpsDirLockConfigRestrictedPort_Type.__name__=_D
_SfpsDirLockConfigRestrictedPort_Object=MibScalar
sfpsDirLockConfigRestrictedPort=_SfpsDirLockConfigRestrictedPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,3,2),_SfpsDirLockConfigRestrictedPort_Type())
sfpsDirLockConfigRestrictedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirLockConfigRestrictedPort.setStatus(_A)
class _SfpsDirLockConfigRouterPortLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_SfpsDirLockConfigRouterPortLock_Type.__name__=_D
_SfpsDirLockConfigRouterPortLock_Object=MibScalar
sfpsDirLockConfigRouterPortLock=_SfpsDirLockConfigRouterPortLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,3,3),_SfpsDirLockConfigRouterPortLock_Type())
sfpsDirLockConfigRouterPortLock.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsDirLockConfigRouterPortLock.setStatus(_A)
class _SfpsDirLockConfigRAPortLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_SfpsDirLockConfigRAPortLock_Type.__name__=_D
_SfpsDirLockConfigRAPortLock_Object=MibScalar
sfpsDirLockConfigRAPortLock=_SfpsDirLockConfigRAPortLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,3,4),_SfpsDirLockConfigRAPortLock_Type())
sfpsDirLockConfigRAPortLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockConfigRAPortLock.setStatus(_A)
_SfpsDirLockStatsNumViolators_Type=Integer32
_SfpsDirLockStatsNumViolators_Object=MibScalar
sfpsDirLockStatsNumViolators=_SfpsDirLockStatsNumViolators_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,1),_SfpsDirLockStatsNumViolators_Type())
sfpsDirLockStatsNumViolators.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsNumViolators.setStatus(_A)
_SfpsDirLockStatsNumNodeLocked_Type=Integer32
_SfpsDirLockStatsNumNodeLocked_Object=MibScalar
sfpsDirLockStatsNumNodeLocked=_SfpsDirLockStatsNumNodeLocked_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,2),_SfpsDirLockStatsNumNodeLocked_Type())
sfpsDirLockStatsNumNodeLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsNumNodeLocked.setStatus(_A)
_SfpsDirLockStatsNumAliasLocked_Type=Integer32
_SfpsDirLockStatsNumAliasLocked_Object=MibScalar
sfpsDirLockStatsNumAliasLocked=_SfpsDirLockStatsNumAliasLocked_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,3),_SfpsDirLockStatsNumAliasLocked_Type())
sfpsDirLockStatsNumAliasLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsNumAliasLocked.setStatus(_A)
_SfpsDirLockStatsNumRestrictedPort_Type=Integer32
_SfpsDirLockStatsNumRestrictedPort_Object=MibScalar
sfpsDirLockStatsNumRestrictedPort=_SfpsDirLockStatsNumRestrictedPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,4),_SfpsDirLockStatsNumRestrictedPort_Type())
sfpsDirLockStatsNumRestrictedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsNumRestrictedPort.setStatus(_A)
_SfpsDirLockStatsNumRestrictMob_Type=Integer32
_SfpsDirLockStatsNumRestrictMob_Object=MibScalar
sfpsDirLockStatsNumRestrictMob=_SfpsDirLockStatsNumRestrictMob_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,5),_SfpsDirLockStatsNumRestrictMob_Type())
sfpsDirLockStatsNumRestrictMob.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsNumRestrictMob.setStatus(_A)
_SfpsDirLockStatsViolationTblSize_Type=Integer32
_SfpsDirLockStatsViolationTblSize_Object=MibScalar
sfpsDirLockStatsViolationTblSize=_SfpsDirLockStatsViolationTblSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,6),_SfpsDirLockStatsViolationTblSize_Type())
sfpsDirLockStatsViolationTblSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsViolationTblSize.setStatus(_A)
_SfpsDirLockStatsRestrictPortTblSize_Type=Integer32
_SfpsDirLockStatsRestrictPortTblSize_Object=MibScalar
sfpsDirLockStatsRestrictPortTblSize=_SfpsDirLockStatsRestrictPortTblSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,7),_SfpsDirLockStatsRestrictPortTblSize_Type())
sfpsDirLockStatsRestrictPortTblSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsRestrictPortTblSize.setStatus(_A)
_SfpsDirLockStatsRestrictMobTblSize_Type=Integer32
_SfpsDirLockStatsRestrictMobTblSize_Object=MibScalar
sfpsDirLockStatsRestrictMobTblSize=_SfpsDirLockStatsRestrictMobTblSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,4,8),_SfpsDirLockStatsRestrictMobTblSize_Type())
sfpsDirLockStatsRestrictMobTblSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirLockStatsRestrictMobTblSize.setStatus(_A)
_SfpsRestrictedMobilityTable_Object=MibTable
sfpsRestrictedMobilityTable=_SfpsRestrictedMobilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,1))
if mibBuilder.loadTexts:sfpsRestrictedMobilityTable.setStatus(_A)
_SfpsRestrictedMobilityEntry_Object=MibTableRow
sfpsRestrictedMobilityEntry=_SfpsRestrictedMobilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,1,1))
sfpsRestrictedMobilityEntry.setIndexNames((0,_E,_Aa),(0,_E,_Ab),(0,_E,_Ac))
if mibBuilder.loadTexts:sfpsRestrictedMobilityEntry.setStatus(_A)
_SfpsRestrictedMobilityHash_Type=Integer32
_SfpsRestrictedMobilityHash_Object=MibTableColumn
sfpsRestrictedMobilityHash=_SfpsRestrictedMobilityHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,1,1,1),_SfpsRestrictedMobilityHash_Type())
sfpsRestrictedMobilityHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedMobilityHash.setStatus(_A)
_SfpsRestrictedMobilityPort_Type=Integer32
_SfpsRestrictedMobilityPort_Object=MibTableColumn
sfpsRestrictedMobilityPort=_SfpsRestrictedMobilityPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,1,1,2),_SfpsRestrictedMobilityPort_Type())
sfpsRestrictedMobilityPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedMobilityPort.setStatus(_A)
_SfpsRestrictedMobilityHashIndex_Type=Integer32
_SfpsRestrictedMobilityHashIndex_Object=MibTableColumn
sfpsRestrictedMobilityHashIndex=_SfpsRestrictedMobilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,1,1,3),_SfpsRestrictedMobilityHashIndex_Type())
sfpsRestrictedMobilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedMobilityHashIndex.setStatus(_A)
_SfpsRestrictedMobilitySrcMac_Type=OctetString
_SfpsRestrictedMobilitySrcMac_Object=MibTableColumn
sfpsRestrictedMobilitySrcMac=_SfpsRestrictedMobilitySrcMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,1,1,4),_SfpsRestrictedMobilitySrcMac_Type())
sfpsRestrictedMobilitySrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedMobilitySrcMac.setStatus(_A)
_SfpsRestrictedMobilitySwitch_Type=SfpsAddress
_SfpsRestrictedMobilitySwitch_Object=MibTableColumn
sfpsRestrictedMobilitySwitch=_SfpsRestrictedMobilitySwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,1,1,5),_SfpsRestrictedMobilitySwitch_Type())
sfpsRestrictedMobilitySwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRestrictedMobilitySwitch.setStatus(_A)
class _SfpsRestrictedMobilityAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_N,2),('delete',3),('reset',4)))
_SfpsRestrictedMobilityAPIVerb_Type.__name__=_D
_SfpsRestrictedMobilityAPIVerb_Object=MibScalar
sfpsRestrictedMobilityAPIVerb=_SfpsRestrictedMobilityAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,2,1),_SfpsRestrictedMobilityAPIVerb_Type())
sfpsRestrictedMobilityAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRestrictedMobilityAPIVerb.setStatus(_A)
_SfpsRestrictedMobilityAPISourcePort_Type=Integer32
_SfpsRestrictedMobilityAPISourcePort_Object=MibScalar
sfpsRestrictedMobilityAPISourcePort=_SfpsRestrictedMobilityAPISourcePort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,2,2),_SfpsRestrictedMobilityAPISourcePort_Type())
sfpsRestrictedMobilityAPISourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRestrictedMobilityAPISourcePort.setStatus(_A)
_SfpsRestrictedMobilityAPISrcMac_Type=SfpsAddress
_SfpsRestrictedMobilityAPISrcMac_Object=MibScalar
sfpsRestrictedMobilityAPISrcMac=_SfpsRestrictedMobilityAPISrcMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,2,3),_SfpsRestrictedMobilityAPISrcMac_Type())
sfpsRestrictedMobilityAPISrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRestrictedMobilityAPISrcMac.setStatus(_A)
_SfpsRestrictedMobilityAPISwitch_Type=SfpsAddress
_SfpsRestrictedMobilityAPISwitch_Object=MibScalar
sfpsRestrictedMobilityAPISwitch=_SfpsRestrictedMobilityAPISwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,15,5,2,4),_SfpsRestrictedMobilityAPISwitch_Type())
sfpsRestrictedMobilityAPISwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsRestrictedMobilityAPISwitch.setStatus(_A)
class _SfpsDapiNvramStatsVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('clearAllEntries',2),('clearAllUserLock',3),('clearAllSrcUnblock',4),('clearAllPortUnblock',5),('clearAllLimitMobility',6)))
_SfpsDapiNvramStatsVerb_Type.__name__=_D
_SfpsDapiNvramStatsVerb_Object=MibScalar
sfpsDapiNvramStatsVerb=_SfpsDapiNvramStatsVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,16,1),_SfpsDapiNvramStatsVerb_Type())
sfpsDapiNvramStatsVerb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDapiNvramStatsVerb.setStatus(_A)
_SfpsDapiNvramStatsTotalEntries_Type=Integer32
_SfpsDapiNvramStatsTotalEntries_Object=MibScalar
sfpsDapiNvramStatsTotalEntries=_SfpsDapiNvramStatsTotalEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,16,2),_SfpsDapiNvramStatsTotalEntries_Type())
sfpsDapiNvramStatsTotalEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDapiNvramStatsTotalEntries.setStatus(_A)
_SfpsDapiNvramStatsMacEntries_Type=Integer32
_SfpsDapiNvramStatsMacEntries_Object=MibScalar
sfpsDapiNvramStatsMacEntries=_SfpsDapiNvramStatsMacEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,16,3),_SfpsDapiNvramStatsMacEntries_Type())
sfpsDapiNvramStatsMacEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDapiNvramStatsMacEntries.setStatus(_A)
_SfpsDapiNvramStatsAliasEntries_Type=Integer32
_SfpsDapiNvramStatsAliasEntries_Object=MibScalar
sfpsDapiNvramStatsAliasEntries=_SfpsDapiNvramStatsAliasEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,16,4),_SfpsDapiNvramStatsAliasEntries_Type())
sfpsDapiNvramStatsAliasEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDapiNvramStatsAliasEntries.setStatus(_A)
_SfpsDapiNvramStatsMaxEntries_Type=Integer32
_SfpsDapiNvramStatsMaxEntries_Object=MibScalar
sfpsDapiNvramStatsMaxEntries=_SfpsDapiNvramStatsMaxEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,16,5),_SfpsDapiNvramStatsMaxEntries_Type())
sfpsDapiNvramStatsMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDapiNvramStatsMaxEntries.setStatus(_A)
_SfpsDapiNvramStatsNvramUsed_Type=Integer32
_SfpsDapiNvramStatsNvramUsed_Object=MibScalar
sfpsDapiNvramStatsNvramUsed=_SfpsDapiNvramStatsNvramUsed_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,16,6),_SfpsDapiNvramStatsNvramUsed_Type())
sfpsDapiNvramStatsNvramUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDapiNvramStatsNvramUsed.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'HexInteger':HexInteger,'SfpsAddress':SfpsAddress,'sfpsServiceCenterTopologyTable':sfpsServiceCenterTopologyTable,'sfpsServiceCenterTopologyEntry':sfpsServiceCenterTopologyEntry,_Y:sfpsServiceCenterTopologyHashLeaf,'sfpsServiceCenterTopologyMetric':sfpsServiceCenterTopologyMetric,'sfpsServiceCenterTopologyName':sfpsServiceCenterTopologyName,'sfpsServiceCenterTopologyOperStatus':sfpsServiceCenterTopologyOperStatus,'sfpsServiceCenterTopologyAdminStatus':sfpsServiceCenterTopologyAdminStatus,'sfpsServiceCenterTopologyStatusTime':sfpsServiceCenterTopologyStatusTime,'sfpsServiceCenterTopologyRequests':sfpsServiceCenterTopologyRequests,'sfpsServiceCenterTopologyResponses':sfpsServiceCenterTopologyResponses,'sfpsHistoryTopologyServerTable':sfpsHistoryTopologyServerTable,'sfpsHistoryTopologyServerEntry':sfpsHistoryTopologyServerEntry,_Z:sfpsHistoryTopologyServerIndex,'sfpsHistoryTopologyServerLogicalPort':sfpsHistoryTopologyServerLogicalPort,'sfpsHistoryTopologyServerSwitchID':sfpsHistoryTopologyServerSwitchID,'sfpsHistoryTopologyServerEvent':sfpsHistoryTopologyServerEvent,'sfpsHistoryTopologyServerSwitchIP':sfpsHistoryTopologyServerSwitchIP,'sfpsHistoryTopologyServerChassisMAC':sfpsHistoryTopologyServerChassisMAC,'sfpsHistoryTopologyServerChassisIP':sfpsHistoryTopologyServerChassisIP,'sfpsHistoryTopologyServerAgent':sfpsHistoryTopologyServerAgent,'sfpsHistoryTopologyServerDeltaOptionsMask':sfpsHistoryTopologyServerDeltaOptionsMask,'sfpsHistoryTopologyServerCurrentOptionsMask':sfpsHistoryTopologyServerCurrentOptionsMask,'sfpsHistoryTopologyServerFCL':sfpsHistoryTopologyServerFCL,'sfpsHistoryTopologyServerSysTime':sfpsHistoryTopologyServerSysTime,'sfpsTPMPortTable':sfpsTPMPortTable,'sfpsTPMPortEntry':sfpsTPMPortEntry,_l:sfpsTPMPortLogicalPort,'sfpsTPMPortMediaType':sfpsTPMPortMediaType,'sfpsTPMPortTopologyAgent':sfpsTPMPortTopologyAgent,'sfpsTPMPortVlanAttributes':sfpsTPMPortVlanAttributes,'sfpsTPMPortNVRAMStatus':sfpsTPMPortNVRAMStatus,'sfpsTPMPortCorePortVID':sfpsTPMPortCorePortVID,'sfpsTPMPortTableAPIInVerb':sfpsTPMPortTableAPIInVerb,'sfpsTPMPortTableAPIInLogicalPort':sfpsTPMPortTableAPIInLogicalPort,'sfpsTPMPortTableAPIInTopologyAgent':sfpsTPMPortTableAPIInTopologyAgent,'sfpsTPMPortTableAPIInAdminPortUp':sfpsTPMPortTableAPIInAdminPortUp,'sfpsTPMPortTableAPIInAdminPortDown':sfpsTPMPortTableAPIInAdminPortDown,'sfpsTPMPortTableAPIInCorePortVID':sfpsTPMPortTableAPIInCorePortVID,'sfpsTPMPortTableAPIOutLogicalPort':sfpsTPMPortTableAPIOutLogicalPort,'sfpsTPMPortTableAPIOutTopologyAgent':sfpsTPMPortTableAPIOutTopologyAgent,'sfpsCommonNeighborTable':sfpsCommonNeighborTable,'sfpsCommonNeighborEntry':sfpsCommonNeighborEntry,_n:sfpsCommonNeighborLogicalPort,_o:sfpsCommonNeighborSwitchID,'sfpsCommonNeighborSwitchIP':sfpsCommonNeighborSwitchIP,'sfpsCommonNeighborSwitchMAC':sfpsCommonNeighborSwitchMAC,'sfpsCommonNeighborSwitchType':sfpsCommonNeighborSwitchType,'sfpsCommonNeighborHellosReceived':sfpsCommonNeighborHellosReceived,'sfpsCommonNeighborFirstHeard':sfpsCommonNeighborFirstHeard,'sfpsCommonNeighborLastHeard':sfpsCommonNeighborLastHeard,'sfpsCommonNeighborReceiveFrequency':sfpsCommonNeighborReceiveFrequency,'sfpsCommonNeighborTopologyAgent':sfpsCommonNeighborTopologyAgent,'sfpsCommonNeighborChassisMAC':sfpsCommonNeighborChassisMAC,'sfpsCommonNeighborCommState':sfpsCommonNeighborCommState,'sfpsCommonNeighborNotifyState':sfpsCommonNeighborNotifyState,'sfpsCommonNeighborTwoWayLossCount':sfpsCommonNeighborTwoWayLossCount,'sfpsCommonNeighborTwoWayLossTime':sfpsCommonNeighborTwoWayLossTime,'sfpsCommonNeighborSeqNumLossCount':sfpsCommonNeighborSeqNumLossCount,'sfpsCommonNeighborSeqNumLossTime':sfpsCommonNeighborSeqNumLossTime,'sfpsCommonNeighborFalseAgingCount':sfpsCommonNeighborFalseAgingCount,'sfpsCommonNeighborFalseAgingTime':sfpsCommonNeighborFalseAgingTime,'sfpsCommonNeighborChassisIP':sfpsCommonNeighborChassisIP,'sfpsCommonNeighborFCL':sfpsCommonNeighborFCL,'sfpsCommonNeighborOptionsMask':sfpsCommonNeighborOptionsMask,'sfpsCommonNeighborRcvdPortState':sfpsCommonNeighborRcvdPortState,'sfpsCommonNeighborSendPortState':sfpsCommonNeighborSendPortState,'sfpsCommonNeighborCompatibility':sfpsCommonNeighborCompatibility,'sfpsCommonNeighborCorePortVID':sfpsCommonNeighborCorePortVID,'sfpsIncompatibleNeighborTable':sfpsIncompatibleNeighborTable,'sfpsIncompatibleNeighborEntry':sfpsIncompatibleNeighborEntry,_A4:sfpsIncompatibleNeighborLogicalPort,_A5:sfpsIncompatibleNeighborSwitchID,'sfpsIncompatibleNeighborSwitchIP':sfpsIncompatibleNeighborSwitchIP,'sfpsIncompatibleNeighborSwitchMAC':sfpsIncompatibleNeighborSwitchMAC,'sfpsIncompatibleNeighborSwitchType':sfpsIncompatibleNeighborSwitchType,'sfpsIncompatibleNeighborHellosReceived':sfpsIncompatibleNeighborHellosReceived,'sfpsIncompatibleNeighborFirstHeard':sfpsIncompatibleNeighborFirstHeard,'sfpsIncompatibleNeighborLastHeard':sfpsIncompatibleNeighborLastHeard,'sfpsIncompatibleNeighborReceiveFrequency':sfpsIncompatibleNeighborReceiveFrequency,'sfpsIncompatibleNeighborTopologyAgent':sfpsIncompatibleNeighborTopologyAgent,'sfpsIncompatibleNeighborChassisMAC':sfpsIncompatibleNeighborChassisMAC,'sfpsIncompatibleNeighborCommState':sfpsIncompatibleNeighborCommState,'sfpsIncompatibleNeighborNotifyState':sfpsIncompatibleNeighborNotifyState,'sfpsIncompatibleNeighborTwoWayLossCount':sfpsIncompatibleNeighborTwoWayLossCount,'sfpsIncompatibleNeighborTwoWayLossTime':sfpsIncompatibleNeighborTwoWayLossTime,'sfpsIncompatibleNeighborSeqNumLossCount':sfpsIncompatibleNeighborSeqNumLossCount,'sfpsIncompatibleNeighborSeqNumLossTime':sfpsIncompatibleNeighborSeqNumLossTime,'sfpsIncompatibleNeighborFalseAgingCount':sfpsIncompatibleNeighborFalseAgingCount,'sfpsIncompatibleNeighborFalseAgingTime':sfpsIncompatibleNeighborFalseAgingTime,'sfpsIncompatibleNeighborChassisIP':sfpsIncompatibleNeighborChassisIP,'sfpsIncompatibleNeighborFCL':sfpsIncompatibleNeighborFCL,'sfpsIncompatibleNeighborOptionsMask':sfpsIncompatibleNeighborOptionsMask,'sfpsIncompatibleNeighborLocalPortState':sfpsIncompatibleNeighborLocalPortState,'sfpsIncompatibleNeighborRemotePortState':sfpsIncompatibleNeighborRemotePortState,'sfpsIncompatibleNeighborCompatibility':sfpsIncompatibleNeighborCompatibility,'sfpsVLANTopAgentNeighborTable':sfpsVLANTopAgentNeighborTable,'sfpsVLANTopAgentNeighborEntry':sfpsVLANTopAgentNeighborEntry,_A6:sfpsVLANTopAgentNeighborInPort,_A7:sfpsVLANTopAgentNeighborSwitchID,'sfpsVLANTopAgentNeighborOptions':sfpsVLANTopAgentNeighborOptions,'sfpsVLANTopAgentPortTable':sfpsVLANTopAgentPortTable,'sfpsVLANTopAgentPortEntry':sfpsVLANTopAgentPortEntry,_A8:sfpsVLANTopAgentPortPort,'sfpsVLANTopAgentPortHelloVersion':sfpsVLANTopAgentPortHelloVersion,'sfpsVLANTopAgentPortSendFrequency':sfpsVLANTopAgentPortSendFrequency,'sfpsVLANTopAgentPortRecvFrequency':sfpsVLANTopAgentPortRecvFrequency,'sfpsVLANTopAgentPortPortOptions':sfpsVLANTopAgentPortPortOptions,'sfpsVLANTopAgentPortNVRAMStatus':sfpsVLANTopAgentPortNVRAMStatus,'sfpsVLANTopAgentPortTableAPIInVerb':sfpsVLANTopAgentPortTableAPIInVerb,'sfpsVLANTopAgentPortTableAPIInLogicalPort':sfpsVLANTopAgentPortTableAPIInLogicalPort,'sfpsVLANTopAgentPortTableAPIInHelloVersion':sfpsVLANTopAgentPortTableAPIInHelloVersion,'sfpsVLANTopAgentPortTableAPIInSendFrequency':sfpsVLANTopAgentPortTableAPIInSendFrequency,'sfpsVLANTopAgentPortTableAPIInRecvFrequency':sfpsVLANTopAgentPortTableAPIInRecvFrequency,'sfpsRATopAgentNeighborTable':sfpsRATopAgentNeighborTable,'sfpsRATopAgentNeighborEntry':sfpsRATopAgentNeighborEntry,_AA:sfpsRATopAgentNeighborInPort,_AB:sfpsRATopAgentNeighborSwitchID,'sfpsRATopAgentNeighborPriority':sfpsRATopAgentNeighborPriority,'sfpsRATopAgentNeighborNetworkPort':sfpsRATopAgentNeighborNetworkPort,'sfpsRATopAgentNeighborCallTag':sfpsRATopAgentNeighborCallTag,'sfpsRATopAgentNeighborNetHellosRcvd':sfpsRATopAgentNeighborNetHellosRcvd,'sfpsRATopAgentNeighborSeqNumMismatch':sfpsRATopAgentNeighborSeqNumMismatch,'sfpsRATopAgentNeighborNetHelloAgeTimeOuts':sfpsRATopAgentNeighborNetHelloAgeTimeOuts,'sfpsRATopAgentNeighborNetHelloNetPortLosses':sfpsRATopAgentNeighborNetHelloNetPortLosses,'sfpsRATopAgentNeighborNetHelloNetPortChanges':sfpsRATopAgentNeighborNetHelloNetPortChanges,'sfpsRATopAgentPortTable':sfpsRATopAgentPortTable,'sfpsRATopAgentPortEntry':sfpsRATopAgentPortEntry,_AC:sfpsRATopAgentPortLogicalPort,'sfpsRATopAgentPortHelloVersion':sfpsRATopAgentPortHelloVersion,'sfpsRATopAgentPortSendFrequency':sfpsRATopAgentPortSendFrequency,'sfpsRATopAgentPortRecvFrequency':sfpsRATopAgentPortRecvFrequency,'sfpsRATopAgentPortPriority':sfpsRATopAgentPortPriority,'sfpsRATopAgentPortPortState':sfpsRATopAgentPortPortState,'sfpsRATopAgentPortPrimarySwitch':sfpsRATopAgentPortPrimarySwitch,'sfpsRATopAgentPortNetHelloRecvFreq':sfpsRATopAgentPortNetHelloRecvFreq,'sfpsRATopAgentPortStateChangeCount':sfpsRATopAgentPortStateChangeCount,'sfpsRATopAgentPortNVRAMStatus':sfpsRATopAgentPortNVRAMStatus,'sfpsRATopAgentPortTableAPIInVerb':sfpsRATopAgentPortTableAPIInVerb,'sfpsRATopAgentPortTableAPIInLogicalPort':sfpsRATopAgentPortTableAPIInLogicalPort,'sfpsRATopAgentPortTableAPIInHelloVersion':sfpsRATopAgentPortTableAPIInHelloVersion,'sfpsRATopAgentPortTableAPIInSendFrequency':sfpsRATopAgentPortTableAPIInSendFrequency,'sfpsRATopAgentPortTableAPIInRecvFrequency':sfpsRATopAgentPortTableAPIInRecvFrequency,'sfpsRATopAgentPortTableAPIInPriority':sfpsRATopAgentPortTableAPIInPriority,'sfpsRATopAgentPortTableAPIInNetHelloRecvFreq':sfpsRATopAgentPortTableAPIInNetHelloRecvFreq,'sfpsRATopAgentPortTableAPIOutLogicalPort':sfpsRATopAgentPortTableAPIOutLogicalPort,'sfpsRATopAgentPortTableAPIOutHelloVersion':sfpsRATopAgentPortTableAPIOutHelloVersion,'sfpsRATopAgentPortTableAPIOutSendFrequency':sfpsRATopAgentPortTableAPIOutSendFrequency,'sfpsRATopAgentPortTableAPIOutRecvFrequency':sfpsRATopAgentPortTableAPIOutRecvFrequency,'sfpsRATopAgentPortTableAPIOutPriority':sfpsRATopAgentPortTableAPIOutPriority,'sfpsRATopAgentPortTableAPIOutPortState':sfpsRATopAgentPortTableAPIOutPortState,'sfpsRATopAgentPortTableAPIOutPrimarySwitch':sfpsRATopAgentPortTableAPIOutPrimarySwitch,'sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq':sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq,'sfpsRATopAgentPortTableAPIOutPortStateChangeCount':sfpsRATopAgentPortTableAPIOutPortStateChangeCount,'sfpsESPTopAgentPortTable':sfpsESPTopAgentPortTable,'sfpsESPTopAgentPortEntry':sfpsESPTopAgentPortEntry,_AE:sfpsESPTopAgentPortPort,'sfpsESPTopAgentPortHelloVersion':sfpsESPTopAgentPortHelloVersion,'sfpsESPTopAgentPortSendFrequency':sfpsESPTopAgentPortSendFrequency,'sfpsESPTopAgentPortRecvFrequency':sfpsESPTopAgentPortRecvFrequency,'sfpsVMTopServerDeltaTable':sfpsVMTopServerDeltaTable,'sfpsVMTopServerDeltaEntry':sfpsVMTopServerDeltaEntry,_AF:sfpsVMTopServerDeltaIndex,'sfpsVMTopServerDeltaInPort':sfpsVMTopServerDeltaInPort,'sfpsVMTopServerDeltaSwitchID':sfpsVMTopServerDeltaSwitchID,'sfpsVMTopServerDeltaState':sfpsVMTopServerDeltaState,'sfpsVMTopServerDeltaIPAddress':sfpsVMTopServerDeltaIPAddress,'sfpsVMTopServerDeltaAgent':sfpsVMTopServerDeltaAgent,'sfpsVMTopServerDeltaCount':sfpsVMTopServerDeltaCount,'sfpsVMTopServerTableLock':sfpsVMTopServerTableLock,'sfpsVMTopServerPortChange':sfpsVMTopServerPortChange,'sfpsVMTopServerTableFull':sfpsVMTopServerTableFull,'sfpsVMTopServerChangeCnt':sfpsVMTopServerChangeCnt,'sfpsTAPITestInVerb':sfpsTAPITestInVerb,'sfpsTAPITestInLogicalPort':sfpsTAPITestInLogicalPort,'sfpsTAPITestInSwitchID':sfpsTAPITestInSwitchID,'sfpsTAPITestInMAC':sfpsTAPITestInMAC,'sfpsTAPITestInPortTypeState':sfpsTAPITestInPortTypeState,'sfpsTAPITestInTopologyAgentID':sfpsTAPITestInTopologyAgentID,'sfpsTAPITestInUNIT321':sfpsTAPITestInUNIT321,'sfpsTAPITestOutOutputInteger':sfpsTAPITestOutOutputInteger,'sfpsTAPITestOutOutPutString':sfpsTAPITestOutOutPutString,'sfpsTopologyServerTestInVerb':sfpsTopologyServerTestInVerb,'sfpsTopologyServerTestInServer':sfpsTopologyServerTestInServer,'sfpsTopologyServerTestInNumberOfRelays':sfpsTopologyServerTestInNumberOfRelays,'sfpsTopologyServerTestTable':sfpsTopologyServerTestTable,'sfpsTopologyServerTestEntry':sfpsTopologyServerTestEntry,_AG:sfpsTopologyServerTestRelayNumber,'sfpsTopologyServerTestServerFlavor':sfpsTopologyServerTestServerFlavor,'sfpsTopologyServerTestPortNumber':sfpsTopologyServerTestPortNumber,'sfpsTopologyServerTestPortName':sfpsTopologyServerTestPortName,'sfpsTopologyServerTestIpAddr':sfpsTopologyServerTestIpAddr,'sfpsTopologyServerTestLostPort':sfpsTopologyServerTestLostPort,'sfpsTopologyServerTestOldState':sfpsTopologyServerTestOldState,'sfpsTopologyServerTestNewState':sfpsTopologyServerTestNewState,'sfpsTopologyServerTestTopologyAgent':sfpsTopologyServerTestTopologyAgent,'sfpsTopologyServerTestTopRelayTable':sfpsTopologyServerTestTopRelayTable,'sfpsTopologyServerTestTopRelayEntry':sfpsTopologyServerTestTopRelayEntry,_AH:sfpsTopologyServerTestTopRelayRelayNumber,'sfpsTopologyServerTestTopRelayEvent':sfpsTopologyServerTestTopRelayEvent,'sfpsTopologyServerTestTopRelayDeltaOptions':sfpsTopologyServerTestTopRelayDeltaOptions,'sfpsTopologyServerTestTopRelayCurrentOptions':sfpsTopologyServerTestTopRelayCurrentOptions,'sfpsTopologyServerTestTopRelayLogicalPort':sfpsTopologyServerTestTopRelayLogicalPort,'sfpsTopologyServerTestTopRelayPortName':sfpsTopologyServerTestTopRelayPortName,'sfpsTopologyServerTestTopRelayIPAddr':sfpsTopologyServerTestTopRelayIPAddr,'sfpsTopologyServerTestTopRelayChassisMAC':sfpsTopologyServerTestTopRelayChassisMAC,'sfpsTopologyServerTestTopRelayChassisIP':sfpsTopologyServerTestTopRelayChassisIP,'sfpsTopologyServerTestTopRelayFLevel':sfpsTopologyServerTestTopRelayFLevel,'sfpsTopologyServerTestTopRelayTopologyAgent':sfpsTopologyServerTestTopRelayTopologyAgent,'sfpsTopologyServerPortEventRelayLogicalPort':sfpsTopologyServerPortEventRelayLogicalPort,'sfpsTopologyServerPortEventRelayOldState':sfpsTopologyServerPortEventRelayOldState,'sfpsTopologyServerPortEventRelayNewState':sfpsTopologyServerPortEventRelayNewState,'sfpsNeighborEventsFoundEvents':sfpsNeighborEventsFoundEvents,'sfpsNeighborEventsLostEvents':sfpsNeighborEventsLostEvents,'sfpsTopologyFCLTable':sfpsTopologyFCLTable,'sfpsTopologyFCLEntry':sfpsTopologyFCLEntry,_AJ:sfpsTopologyFCLFunctionalLevel,'sfpsTopologyFCLCompatability':sfpsTopologyFCLCompatability,'sfpsTopologyFCLThisPortState':sfpsTopologyFCLThisPortState,'sfpsTopologyFCLSendPortState':sfpsTopologyFCLSendPortState,'sfpsDirViolationTable':sfpsDirViolationTable,'sfpsDirViolationEntry':sfpsDirViolationEntry,_AM:sfpsDirViolationHash,_AN:sfpsDirViolationHashIndex,'sfpsDirViolationType':sfpsDirViolationType,'sfpsDirViolationSrcPort':sfpsDirViolationSrcPort,'sfpsDirViolationAOType':sfpsDirViolationAOType,'sfpsDirViolationAOValue':sfpsDirViolationAOValue,'sfpsDirViolationLocalPort':sfpsDirViolationLocalPort,'sfpsDirViolationCount':sfpsDirViolationCount,'sfpsDirViolationLastSeen':sfpsDirViolationLastSeen,'sfpsDirViolationFirstSeen':sfpsDirViolationFirstSeen,'sfpsDirViolationSrcMac':sfpsDirViolationSrcMac,'sfpsDirViolationCPId':sfpsDirViolationCPId,'sfpsDirViolationAPIVerb':sfpsDirViolationAPIVerb,'sfpsDirViolationAPIViolType':sfpsDirViolationAPIViolType,'sfpsDirViolationAPISourcePort':sfpsDirViolationAPISourcePort,'sfpsDirViolationAPIAOType':sfpsDirViolationAPIAOType,'sfpsDirViolationAPIAOValue':sfpsDirViolationAPIAOValue,'sfpsDirViolationAPIChangeCount':sfpsDirViolationAPIChangeCount,'sfpsDirViolationAPICPId':sfpsDirViolationAPICPId,'sfpsDirViolationDeltaTable':sfpsDirViolationDeltaTable,'sfpsDirViolationDeltaEntry':sfpsDirViolationDeltaEntry,_AW:sfpsDirViolationDeltaIndex,'sfpsDirViolationDeltaSrcPort':sfpsDirViolationDeltaSrcPort,'sfpsDirViolationDeltaAOType':sfpsDirViolationDeltaAOType,'sfpsDirViolationDeltaAOValue':sfpsDirViolationDeltaAOValue,'sfpsDirViolationDeltaEntryType':sfpsDirViolationDeltaEntryType,'sfpsDirViolationDeltaAPINumEntries':sfpsDirViolationDeltaAPINumEntries,'sfpsDirViolationDeltaAPIVerb':sfpsDirViolationDeltaAPIVerb,'sfpsRestrictedPortTable':sfpsRestrictedPortTable,'sfpsRestrictedPortEntry':sfpsRestrictedPortEntry,_AX:sfpsRestrictedPortPort,_AY:sfpsRestrictedPortHash,_AZ:sfpsRestrictedPortHashIndex,'sfpsRestrictedPortSrcMac':sfpsRestrictedPortSrcMac,'sfpsDirLockConfigUserLocking':sfpsDirLockConfigUserLocking,'sfpsDirLockConfigRestrictedPort':sfpsDirLockConfigRestrictedPort,'sfpsDirLockConfigRouterPortLock':sfpsDirLockConfigRouterPortLock,'sfpsDirLockConfigRAPortLock':sfpsDirLockConfigRAPortLock,'sfpsDirLockStatsNumViolators':sfpsDirLockStatsNumViolators,'sfpsDirLockStatsNumNodeLocked':sfpsDirLockStatsNumNodeLocked,'sfpsDirLockStatsNumAliasLocked':sfpsDirLockStatsNumAliasLocked,'sfpsDirLockStatsNumRestrictedPort':sfpsDirLockStatsNumRestrictedPort,'sfpsDirLockStatsNumRestrictMob':sfpsDirLockStatsNumRestrictMob,'sfpsDirLockStatsViolationTblSize':sfpsDirLockStatsViolationTblSize,'sfpsDirLockStatsRestrictPortTblSize':sfpsDirLockStatsRestrictPortTblSize,'sfpsDirLockStatsRestrictMobTblSize':sfpsDirLockStatsRestrictMobTblSize,'sfpsRestrictedMobilityTable':sfpsRestrictedMobilityTable,'sfpsRestrictedMobilityEntry':sfpsRestrictedMobilityEntry,_Aa:sfpsRestrictedMobilityHash,_Ab:sfpsRestrictedMobilityPort,_Ac:sfpsRestrictedMobilityHashIndex,'sfpsRestrictedMobilitySrcMac':sfpsRestrictedMobilitySrcMac,'sfpsRestrictedMobilitySwitch':sfpsRestrictedMobilitySwitch,'sfpsRestrictedMobilityAPIVerb':sfpsRestrictedMobilityAPIVerb,'sfpsRestrictedMobilityAPISourcePort':sfpsRestrictedMobilityAPISourcePort,'sfpsRestrictedMobilityAPISrcMac':sfpsRestrictedMobilityAPISrcMac,'sfpsRestrictedMobilityAPISwitch':sfpsRestrictedMobilityAPISwitch,'sfpsDapiNvramStatsVerb':sfpsDapiNvramStatsVerb,'sfpsDapiNvramStatsTotalEntries':sfpsDapiNvramStatsTotalEntries,'sfpsDapiNvramStatsMacEntries':sfpsDapiNvramStatsMacEntries,'sfpsDapiNvramStatsAliasEntries':sfpsDapiNvramStatsAliasEntries,'sfpsDapiNvramStatsMaxEntries':sfpsDapiNvramStatsMaxEntries,'sfpsDapiNvramStatsNvramUsed':sfpsDapiNvramStatsNvramUsed})