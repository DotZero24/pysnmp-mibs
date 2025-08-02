_B5='cgkRemoteZoneGroup'
_B4='cgkLocalZoneGroupRev1'
_B3='cgkLocalZoneGroup'
_B2='ciscoGatekeeperEvent'
_B1='cgkRZoneAllocTotalBandwidth'
_B0='cgkRZoneTotalBandwidth'
_A_='cgkStatsSentDisengageRejects'
_Az='cgkStatsRcvdDisengageRejects'
_Ay='cgkStatsSentDisengageConfirms'
_Ax='cgkStatsRcvdDisengageConfirms'
_Aw='cgkStatsSentDisengageRequests'
_Av='cgkStatsRcvdDisengageRequests'
_Au='cgkStatsRegisteredEndpoints'
_At='cgkStatsSentLocationRejects'
_As='cgkStatsRcvdLocationRejects'
_Ar='cgkStatsSentLocationConfirms'
_Aq='cgkStatsRcvdLocationConfirms'
_Ap='cgkStatsSentLocationRequests'
_Ao='cgkStatsRcvdLocationRequests'
_An='cgkStatsOriginTotalConcurrentCalls'
_Am='cgkStatsTotalConcurrentCalls'
_Al='cgkStatsOriginAdmissionRejects'
_Ak='cgkStatsAdmissionRejects'
_Aj='cgkStatsOriginAdmissionConfirms'
_Ai='cgkStatsAdmissionConfirms'
_Ah='cgkStatsOriginAdmissionRequests'
_Ag='cgkStatsAdmissionRequests'
_Af='cgkLZoneStatsSentDisengageRejects'
_Ae='cgkLZoneStatsRcvdDisengageRejects'
_Ad='cgkLZoneStatsSentDisengageConfirms'
_Ac='cgkLZoneStatsRcvdDisengageConfirms'
_Ab='cgkLZoneStatsSentDisengageRequests'
_Aa='cgkLZoneStatsRcvdDisengageRequests'
_AZ='cgkLZoneStatsSentUnregistrationRejects'
_AY='cgkLZoneStatsRcvdUnregistrationRejects'
_AX='cgkLZoneStatsSentUnregistrationConfirms'
_AW='cgkLZoneStatsRcvdUnregistrationConfirms'
_AV='cgkLZoneStatsTimeoutSentUnregistrationRequests'
_AU='cgkLZoneStatsSentUnregistrationRequests'
_AT='cgkLZoneStatsRcvdUnregistrationRequests'
_AS='cgkLZoneStatsRegisteredEndpoints'
_AR='cgkLZoneStatsRegistrationRejects'
_AQ='cgkLZoneStatsRegistrationConfirms'
_AP='cgkLZoneStatsLightRegistrationRequests'
_AO='cgkLZoneStatsFullRegistrationRequests'
_AN='cgkLZoneStatsSentLocationRejects'
_AM='cgkLZoneStatsRcvdLocationRejects'
_AL='cgkLZoneStatsSentLocationConfirms'
_AK='cgkLZoneStatsRcvdLocationConfirms'
_AJ='cgkLZoneStatsSentLocationRequests'
_AI='cgkLZoneStatsOriginTotalConcurrentCalls'
_AH='cgkLZoneStatsOriginAdmissionRejects'
_AG='cgkLZoneStatsOriginAdmissionConfirms'
_AF='cgkLZoneStatsOriginAdmissionRequests'
_AE='cgkLZoneStatsAdmissionRequests'
_AD='cgkLZoneTotalConcurrentCalls'
_AC='cgkMIBDefaultSessionBandwidth'
_AB='cgkMIBDefaultInterzoneBandwidth'
_AA='cgkMIBDefaultTotalBandwidth'
_A9='cgkMIBEnableEventNotification'
_A8='cgkHistoryEventText'
_A7='cgkHistoryEventTime'
_A6='cgkHistoryMaxEventEntries'
_A5='cgkZoneSubnetRowStatus'
_A4='cgkZoneSubnetFlags'
_A3='cgkZoneSubnetMask'
_A2='cgkZoneRowStatus'
_A1='cgkZoneLRQs'
_A0='cgkZoneOtherFailures'
_z='cgkZoneEndpointTimeouts'
_y='cgkZoneAddressLookupFailures'
_x='cgkZoneDefaultSubnetFlags'
_w='cgkZoneLocalZone'
_v='cgkZoneIrrFrequency'
_u='cgkZoneRasAddress'
_t='cgkZoneRasAddressTag'
_s='cgkZoneDomain'
_r='cgkZoneZoneName'
_q='cgkHistoryEventIndex'
_p='cgkZoneSubnetAddress'
_o='cgkZoneSubnetTag'
_n='disable'
_m='enable'
_l='TAddress'
_k='Unsigned32'
_j='SnmpAdminString'
_i='CgkTAddressTag'
_h='cgkGeneralMgmtStatsGroup'
_g='cgkZoneMgmtStatsGroup'
_f='cgkLZoneProxiedCallBits'
_e='cgkHistoryEventEndpointH323id'
_d='cgkHistoryEventEndpointAddrTag'
_c='cgkHistoryEventEndpointAddress'
_b='cgkHistoryEventEndpointType'
_a='cgkHistoryEventType'
_Z='cgkLZoneProxiedCall'
_Y='TruthValue'
_X='cgkLocalZoneGroupRev2'
_W='cgkLZoneSessionBandwidth'
_V='cgkLZoneAllocInterzoneBandwidth'
_U='cgkLZoneInterzoneBandwidth'
_T='cgkLZoneAllocTotalBandwidth'
_S='cgkLZoneTotalBandwidth'
_R='cgkLZoneARJs'
_Q='cgkLZoneACFs'
_P='not-accessible'
_O='Gauge32'
_N='cgkNotificationsGroup'
_M='cgkGeneralGroup'
_L='cgkHistoryEventGroup'
_K='cgkZoneSubnetGroup'
_J='cgkZoneGroup'
_I='deprecated'
_H='cgkZoneIndex'
_G='100 bps'
_F='read-write'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-GATEKEEPER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CgkGatekeeperID,CgkNAddress,CgkNAddressTag,CgkTAddressTag=mibBuilder.importSymbols('CISCO-H323-TC-MIB','CgkGatekeeperID','CgkNAddress','CgkNAddressTag',_i)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_j)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_O,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_k,'iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_l,'TextualConvention','TimeStamp',_Y)
ciscoGatekeeperMIB=ModuleIdentity((1,3,6,1,4,1,9,10,40))
if mibBuilder.loadTexts:ciscoGatekeeperMIB.setRevisions(('2007-08-29 00:00','2007-08-28 00:00','2003-03-13 00:00','2002-03-12 00:00','2001-09-20 00:00','2001-04-09 00:00','2000-06-26 00:00','2000-03-10 00:00','1998-10-09 12:00'))
_CiscoGatekeeperMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGatekeeperMIBObjects=_CiscoGatekeeperMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,40,1))
_CgkZone_ObjectIdentity=ObjectIdentity
cgkZone=_CgkZone_ObjectIdentity((1,3,6,1,4,1,9,10,40,1,1))
_CgkZoneTable_Object=MibTable
cgkZoneTable=_CgkZoneTable_Object((1,3,6,1,4,1,9,10,40,1,1,1))
if mibBuilder.loadTexts:cgkZoneTable.setStatus(_B)
_CgkZoneEntry_Object=MibTableRow
cgkZoneEntry=_CgkZoneEntry_Object((1,3,6,1,4,1,9,10,40,1,1,1,1))
cgkZoneEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cgkZoneEntry.setStatus(_B)
class _CgkZoneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CgkZoneIndex_Type.__name__=_k
_CgkZoneIndex_Object=MibTableColumn
cgkZoneIndex=_CgkZoneIndex_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,1),_CgkZoneIndex_Type())
cgkZoneIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cgkZoneIndex.setStatus(_B)
_CgkZoneZoneName_Type=CgkGatekeeperID
_CgkZoneZoneName_Object=MibTableColumn
cgkZoneZoneName=_CgkZoneZoneName_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,2),_CgkZoneZoneName_Type())
cgkZoneZoneName.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneZoneName.setStatus(_B)
class _CgkZoneDomain_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CgkZoneDomain_Type.__name__=_j
_CgkZoneDomain_Object=MibTableColumn
cgkZoneDomain=_CgkZoneDomain_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,3),_CgkZoneDomain_Type())
cgkZoneDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneDomain.setStatus(_B)
class _CgkZoneRasAddressTag_Type(CgkTAddressTag):defaultValue=1
_CgkZoneRasAddressTag_Type.__name__=_i
_CgkZoneRasAddressTag_Object=MibTableColumn
cgkZoneRasAddressTag=_CgkZoneRasAddressTag_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,4),_CgkZoneRasAddressTag_Type())
cgkZoneRasAddressTag.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneRasAddressTag.setStatus(_B)
class _CgkZoneRasAddress_Type(TAddress):defaultHexValue='00'
_CgkZoneRasAddress_Type.__name__=_l
_CgkZoneRasAddress_Object=MibTableColumn
cgkZoneRasAddress=_CgkZoneRasAddress_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,5),_CgkZoneRasAddress_Type())
cgkZoneRasAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneRasAddress.setStatus(_B)
class _CgkZoneIrrFrequency_Type(Integer32):defaultValue=240;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CgkZoneIrrFrequency_Type.__name__=_D
_CgkZoneIrrFrequency_Object=MibTableColumn
cgkZoneIrrFrequency=_CgkZoneIrrFrequency_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,6),_CgkZoneIrrFrequency_Type())
cgkZoneIrrFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneIrrFrequency.setStatus(_B)
class _CgkZoneLocalZone_Type(TruthValue):defaultValue=1
_CgkZoneLocalZone_Type.__name__=_Y
_CgkZoneLocalZone_Object=MibTableColumn
cgkZoneLocalZone=_CgkZoneLocalZone_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,7),_CgkZoneLocalZone_Type())
cgkZoneLocalZone.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneLocalZone.setStatus(_B)
class _CgkZoneDefaultSubnetFlags_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_CgkZoneDefaultSubnetFlags_Type.__name__=_D
_CgkZoneDefaultSubnetFlags_Object=MibTableColumn
cgkZoneDefaultSubnetFlags=_CgkZoneDefaultSubnetFlags_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,8),_CgkZoneDefaultSubnetFlags_Type())
cgkZoneDefaultSubnetFlags.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneDefaultSubnetFlags.setStatus(_B)
_CgkZoneAddressLookupFailures_Type=Counter32
_CgkZoneAddressLookupFailures_Object=MibTableColumn
cgkZoneAddressLookupFailures=_CgkZoneAddressLookupFailures_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,9),_CgkZoneAddressLookupFailures_Type())
cgkZoneAddressLookupFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkZoneAddressLookupFailures.setStatus(_B)
_CgkZoneEndpointTimeouts_Type=Counter32
_CgkZoneEndpointTimeouts_Object=MibTableColumn
cgkZoneEndpointTimeouts=_CgkZoneEndpointTimeouts_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,10),_CgkZoneEndpointTimeouts_Type())
cgkZoneEndpointTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkZoneEndpointTimeouts.setStatus(_B)
_CgkZoneOtherFailures_Type=Counter32
_CgkZoneOtherFailures_Object=MibTableColumn
cgkZoneOtherFailures=_CgkZoneOtherFailures_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,11),_CgkZoneOtherFailures_Type())
cgkZoneOtherFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkZoneOtherFailures.setStatus(_B)
_CgkZoneLRQs_Type=Counter32
_CgkZoneLRQs_Object=MibTableColumn
cgkZoneLRQs=_CgkZoneLRQs_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,12),_CgkZoneLRQs_Type())
cgkZoneLRQs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkZoneLRQs.setStatus(_B)
_CgkZoneRowStatus_Type=RowStatus
_CgkZoneRowStatus_Object=MibTableColumn
cgkZoneRowStatus=_CgkZoneRowStatus_Object((1,3,6,1,4,1,9,10,40,1,1,1,1,13),_CgkZoneRowStatus_Type())
cgkZoneRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneRowStatus.setStatus(_B)
_CgkZoneSubnetTable_Object=MibTable
cgkZoneSubnetTable=_CgkZoneSubnetTable_Object((1,3,6,1,4,1,9,10,40,1,1,2))
if mibBuilder.loadTexts:cgkZoneSubnetTable.setStatus(_B)
_CgkZoneSubnetEntry_Object=MibTableRow
cgkZoneSubnetEntry=_CgkZoneSubnetEntry_Object((1,3,6,1,4,1,9,10,40,1,1,2,1))
cgkZoneSubnetEntry.setIndexNames((0,_A,_H),(0,_A,_o),(1,_A,_p))
if mibBuilder.loadTexts:cgkZoneSubnetEntry.setStatus(_B)
_CgkZoneSubnetTag_Type=CgkNAddressTag
_CgkZoneSubnetTag_Object=MibTableColumn
cgkZoneSubnetTag=_CgkZoneSubnetTag_Object((1,3,6,1,4,1,9,10,40,1,1,2,1,1),_CgkZoneSubnetTag_Type())
cgkZoneSubnetTag.setMaxAccess(_P)
if mibBuilder.loadTexts:cgkZoneSubnetTag.setStatus(_B)
_CgkZoneSubnetAddress_Type=CgkNAddress
_CgkZoneSubnetAddress_Object=MibTableColumn
cgkZoneSubnetAddress=_CgkZoneSubnetAddress_Object((1,3,6,1,4,1,9,10,40,1,1,2,1,2),_CgkZoneSubnetAddress_Type())
cgkZoneSubnetAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:cgkZoneSubnetAddress.setStatus(_B)
_CgkZoneSubnetMask_Type=CgkNAddress
_CgkZoneSubnetMask_Object=MibTableColumn
cgkZoneSubnetMask=_CgkZoneSubnetMask_Object((1,3,6,1,4,1,9,10,40,1,1,2,1,3),_CgkZoneSubnetMask_Type())
cgkZoneSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneSubnetMask.setStatus(_B)
class _CgkZoneSubnetFlags_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_CgkZoneSubnetFlags_Type.__name__=_D
_CgkZoneSubnetFlags_Object=MibTableColumn
cgkZoneSubnetFlags=_CgkZoneSubnetFlags_Object((1,3,6,1,4,1,9,10,40,1,1,2,1,4),_CgkZoneSubnetFlags_Type())
cgkZoneSubnetFlags.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneSubnetFlags.setStatus(_B)
_CgkZoneSubnetRowStatus_Type=RowStatus
_CgkZoneSubnetRowStatus_Object=MibTableColumn
cgkZoneSubnetRowStatus=_CgkZoneSubnetRowStatus_Object((1,3,6,1,4,1,9,10,40,1,1,2,1,5),_CgkZoneSubnetRowStatus_Type())
cgkZoneSubnetRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cgkZoneSubnetRowStatus.setStatus(_B)
_CgkLocalZoneTable_Object=MibTable
cgkLocalZoneTable=_CgkLocalZoneTable_Object((1,3,6,1,4,1,9,10,40,1,1,3))
if mibBuilder.loadTexts:cgkLocalZoneTable.setStatus(_B)
_CgkLocalZoneEntry_Object=MibTableRow
cgkLocalZoneEntry=_CgkLocalZoneEntry_Object((1,3,6,1,4,1,9,10,40,1,1,3,1))
cgkLocalZoneEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cgkLocalZoneEntry.setStatus(_B)
_CgkLZoneACFs_Type=Counter32
_CgkLZoneACFs_Object=MibTableColumn
cgkLZoneACFs=_CgkLZoneACFs_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,1),_CgkLZoneACFs_Type())
cgkLZoneACFs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneACFs.setStatus(_B)
_CgkLZoneARJs_Type=Counter32
_CgkLZoneARJs_Object=MibTableColumn
cgkLZoneARJs=_CgkLZoneARJs_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,2),_CgkLZoneARJs_Type())
cgkLZoneARJs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneARJs.setStatus(_B)
class _CgkLZoneTotalBandwidth_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000000000))
_CgkLZoneTotalBandwidth_Type.__name__=_D
_CgkLZoneTotalBandwidth_Object=MibTableColumn
cgkLZoneTotalBandwidth=_CgkLZoneTotalBandwidth_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,3),_CgkLZoneTotalBandwidth_Type())
cgkLZoneTotalBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkLZoneTotalBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkLZoneTotalBandwidth.setUnits(_G)
class _CgkLZoneAllocTotalBandwidth_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CgkLZoneAllocTotalBandwidth_Type.__name__=_O
_CgkLZoneAllocTotalBandwidth_Object=MibTableColumn
cgkLZoneAllocTotalBandwidth=_CgkLZoneAllocTotalBandwidth_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,4),_CgkLZoneAllocTotalBandwidth_Type())
cgkLZoneAllocTotalBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneAllocTotalBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkLZoneAllocTotalBandwidth.setUnits(_G)
class _CgkLZoneInterzoneBandwidth_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000000000))
_CgkLZoneInterzoneBandwidth_Type.__name__=_D
_CgkLZoneInterzoneBandwidth_Object=MibTableColumn
cgkLZoneInterzoneBandwidth=_CgkLZoneInterzoneBandwidth_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,5),_CgkLZoneInterzoneBandwidth_Type())
cgkLZoneInterzoneBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkLZoneInterzoneBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkLZoneInterzoneBandwidth.setUnits(_G)
class _CgkLZoneAllocInterzoneBandwidth_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CgkLZoneAllocInterzoneBandwidth_Type.__name__=_O
_CgkLZoneAllocInterzoneBandwidth_Object=MibTableColumn
cgkLZoneAllocInterzoneBandwidth=_CgkLZoneAllocInterzoneBandwidth_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,6),_CgkLZoneAllocInterzoneBandwidth_Type())
cgkLZoneAllocInterzoneBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneAllocInterzoneBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkLZoneAllocInterzoneBandwidth.setUnits(_G)
class _CgkLZoneSessionBandwidth_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,50000))
_CgkLZoneSessionBandwidth_Type.__name__=_D
_CgkLZoneSessionBandwidth_Object=MibTableColumn
cgkLZoneSessionBandwidth=_CgkLZoneSessionBandwidth_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,7),_CgkLZoneSessionBandwidth_Type())
cgkLZoneSessionBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkLZoneSessionBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkLZoneSessionBandwidth.setUnits(_G)
class _CgkLZoneProxiedCall_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CgkLZoneProxiedCall_Type.__name__=_D
_CgkLZoneProxiedCall_Object=MibTableColumn
cgkLZoneProxiedCall=_CgkLZoneProxiedCall_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,8),_CgkLZoneProxiedCall_Type())
cgkLZoneProxiedCall.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkLZoneProxiedCall.setStatus(_I)
class _CgkLZoneProxiedCallBits_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('inboundToTerminal',0),('inboundToGateway',1),('outboundFromTerminal',2),('outboundFromGateway',3),('inboundToMcu',4),('outboundFromMcu',5)))
_CgkLZoneProxiedCallBits_Type.__name__='Bits'
_CgkLZoneProxiedCallBits_Object=MibTableColumn
cgkLZoneProxiedCallBits=_CgkLZoneProxiedCallBits_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,9),_CgkLZoneProxiedCallBits_Type())
cgkLZoneProxiedCallBits.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkLZoneProxiedCallBits.setStatus(_B)
_CgkLZoneTotalConcurrentCalls_Type=Gauge32
_CgkLZoneTotalConcurrentCalls_Object=MibTableColumn
cgkLZoneTotalConcurrentCalls=_CgkLZoneTotalConcurrentCalls_Object((1,3,6,1,4,1,9,10,40,1,1,3,1,10),_CgkLZoneTotalConcurrentCalls_Type())
cgkLZoneTotalConcurrentCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneTotalConcurrentCalls.setStatus(_B)
_CgkZoneStats_ObjectIdentity=ObjectIdentity
cgkZoneStats=_CgkZoneStats_ObjectIdentity((1,3,6,1,4,1,9,10,40,1,1,4))
_CgkLocalZoneStatsAdmissionTable_Object=MibTable
cgkLocalZoneStatsAdmissionTable=_CgkLocalZoneStatsAdmissionTable_Object((1,3,6,1,4,1,9,10,40,1,1,4,1))
if mibBuilder.loadTexts:cgkLocalZoneStatsAdmissionTable.setStatus(_B)
_CgkLocalZoneStatsAdmissionTableEntry_Object=MibTableRow
cgkLocalZoneStatsAdmissionTableEntry=_CgkLocalZoneStatsAdmissionTableEntry_Object((1,3,6,1,4,1,9,10,40,1,1,4,1,1))
cgkLocalZoneStatsAdmissionTableEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cgkLocalZoneStatsAdmissionTableEntry.setStatus(_B)
_CgkLZoneStatsAdmissionRequests_Type=Counter32
_CgkLZoneStatsAdmissionRequests_Object=MibTableColumn
cgkLZoneStatsAdmissionRequests=_CgkLZoneStatsAdmissionRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,1,1,1),_CgkLZoneStatsAdmissionRequests_Type())
cgkLZoneStatsAdmissionRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsAdmissionRequests.setStatus(_B)
_CgkLZoneStatsOriginAdmissionRequests_Type=Counter32
_CgkLZoneStatsOriginAdmissionRequests_Object=MibTableColumn
cgkLZoneStatsOriginAdmissionRequests=_CgkLZoneStatsOriginAdmissionRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,1,1,2),_CgkLZoneStatsOriginAdmissionRequests_Type())
cgkLZoneStatsOriginAdmissionRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsOriginAdmissionRequests.setStatus(_B)
_CgkLZoneStatsOriginAdmissionConfirms_Type=Counter32
_CgkLZoneStatsOriginAdmissionConfirms_Object=MibTableColumn
cgkLZoneStatsOriginAdmissionConfirms=_CgkLZoneStatsOriginAdmissionConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,1,1,3),_CgkLZoneStatsOriginAdmissionConfirms_Type())
cgkLZoneStatsOriginAdmissionConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsOriginAdmissionConfirms.setStatus(_B)
_CgkLZoneStatsOriginAdmissionRejects_Type=Counter32
_CgkLZoneStatsOriginAdmissionRejects_Object=MibTableColumn
cgkLZoneStatsOriginAdmissionRejects=_CgkLZoneStatsOriginAdmissionRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,1,1,4),_CgkLZoneStatsOriginAdmissionRejects_Type())
cgkLZoneStatsOriginAdmissionRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsOriginAdmissionRejects.setStatus(_B)
_CgkLZoneStatsOriginTotalConcurrentCalls_Type=Gauge32
_CgkLZoneStatsOriginTotalConcurrentCalls_Object=MibTableColumn
cgkLZoneStatsOriginTotalConcurrentCalls=_CgkLZoneStatsOriginTotalConcurrentCalls_Object((1,3,6,1,4,1,9,10,40,1,1,4,1,1,5),_CgkLZoneStatsOriginTotalConcurrentCalls_Type())
cgkLZoneStatsOriginTotalConcurrentCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsOriginTotalConcurrentCalls.setStatus(_B)
_CgkLocalZoneStatsLocationTable_Object=MibTable
cgkLocalZoneStatsLocationTable=_CgkLocalZoneStatsLocationTable_Object((1,3,6,1,4,1,9,10,40,1,1,4,2))
if mibBuilder.loadTexts:cgkLocalZoneStatsLocationTable.setStatus(_B)
_CgkLocalZoneStatsLocationTableEntry_Object=MibTableRow
cgkLocalZoneStatsLocationTableEntry=_CgkLocalZoneStatsLocationTableEntry_Object((1,3,6,1,4,1,9,10,40,1,1,4,2,1))
cgkLocalZoneStatsLocationTableEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cgkLocalZoneStatsLocationTableEntry.setStatus(_B)
_CgkLZoneStatsSentLocationRequests_Type=Counter32
_CgkLZoneStatsSentLocationRequests_Object=MibTableColumn
cgkLZoneStatsSentLocationRequests=_CgkLZoneStatsSentLocationRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,2,1,1),_CgkLZoneStatsSentLocationRequests_Type())
cgkLZoneStatsSentLocationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentLocationRequests.setStatus(_B)
_CgkLZoneStatsRcvdLocationConfirms_Type=Counter32
_CgkLZoneStatsRcvdLocationConfirms_Object=MibTableColumn
cgkLZoneStatsRcvdLocationConfirms=_CgkLZoneStatsRcvdLocationConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,2,1,2),_CgkLZoneStatsRcvdLocationConfirms_Type())
cgkLZoneStatsRcvdLocationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdLocationConfirms.setStatus(_B)
_CgkLZoneStatsSentLocationConfirms_Type=Counter32
_CgkLZoneStatsSentLocationConfirms_Object=MibTableColumn
cgkLZoneStatsSentLocationConfirms=_CgkLZoneStatsSentLocationConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,2,1,3),_CgkLZoneStatsSentLocationConfirms_Type())
cgkLZoneStatsSentLocationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentLocationConfirms.setStatus(_B)
_CgkLZoneStatsRcvdLocationRejects_Type=Counter32
_CgkLZoneStatsRcvdLocationRejects_Object=MibTableColumn
cgkLZoneStatsRcvdLocationRejects=_CgkLZoneStatsRcvdLocationRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,2,1,4),_CgkLZoneStatsRcvdLocationRejects_Type())
cgkLZoneStatsRcvdLocationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdLocationRejects.setStatus(_B)
_CgkLZoneStatsSentLocationRejects_Type=Counter32
_CgkLZoneStatsSentLocationRejects_Object=MibTableColumn
cgkLZoneStatsSentLocationRejects=_CgkLZoneStatsSentLocationRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,2,1,5),_CgkLZoneStatsSentLocationRejects_Type())
cgkLZoneStatsSentLocationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentLocationRejects.setStatus(_B)
_CgkLocalZoneStatsRegistrationTable_Object=MibTable
cgkLocalZoneStatsRegistrationTable=_CgkLocalZoneStatsRegistrationTable_Object((1,3,6,1,4,1,9,10,40,1,1,4,3))
if mibBuilder.loadTexts:cgkLocalZoneStatsRegistrationTable.setStatus(_B)
_CgkLocalZoneStatsRegistrationTableEntry_Object=MibTableRow
cgkLocalZoneStatsRegistrationTableEntry=_CgkLocalZoneStatsRegistrationTableEntry_Object((1,3,6,1,4,1,9,10,40,1,1,4,3,1))
cgkLocalZoneStatsRegistrationTableEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cgkLocalZoneStatsRegistrationTableEntry.setStatus(_B)
_CgkLZoneStatsFullRegistrationRequests_Type=Counter32
_CgkLZoneStatsFullRegistrationRequests_Object=MibTableColumn
cgkLZoneStatsFullRegistrationRequests=_CgkLZoneStatsFullRegistrationRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,3,1,1),_CgkLZoneStatsFullRegistrationRequests_Type())
cgkLZoneStatsFullRegistrationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsFullRegistrationRequests.setStatus(_B)
_CgkLZoneStatsLightRegistrationRequests_Type=Counter32
_CgkLZoneStatsLightRegistrationRequests_Object=MibTableColumn
cgkLZoneStatsLightRegistrationRequests=_CgkLZoneStatsLightRegistrationRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,3,1,2),_CgkLZoneStatsLightRegistrationRequests_Type())
cgkLZoneStatsLightRegistrationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsLightRegistrationRequests.setStatus(_B)
_CgkLZoneStatsRegistrationConfirms_Type=Counter32
_CgkLZoneStatsRegistrationConfirms_Object=MibTableColumn
cgkLZoneStatsRegistrationConfirms=_CgkLZoneStatsRegistrationConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,3,1,3),_CgkLZoneStatsRegistrationConfirms_Type())
cgkLZoneStatsRegistrationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRegistrationConfirms.setStatus(_B)
_CgkLZoneStatsRegistrationRejects_Type=Counter32
_CgkLZoneStatsRegistrationRejects_Object=MibTableColumn
cgkLZoneStatsRegistrationRejects=_CgkLZoneStatsRegistrationRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,3,1,4),_CgkLZoneStatsRegistrationRejects_Type())
cgkLZoneStatsRegistrationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRegistrationRejects.setStatus(_B)
_CgkLZoneStatsRegisteredEndpoints_Type=Counter32
_CgkLZoneStatsRegisteredEndpoints_Object=MibTableColumn
cgkLZoneStatsRegisteredEndpoints=_CgkLZoneStatsRegisteredEndpoints_Object((1,3,6,1,4,1,9,10,40,1,1,4,3,1,5),_CgkLZoneStatsRegisteredEndpoints_Type())
cgkLZoneStatsRegisteredEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRegisteredEndpoints.setStatus(_B)
_CgkLocalZoneStatsUnRegistrationTable_Object=MibTable
cgkLocalZoneStatsUnRegistrationTable=_CgkLocalZoneStatsUnRegistrationTable_Object((1,3,6,1,4,1,9,10,40,1,1,4,4))
if mibBuilder.loadTexts:cgkLocalZoneStatsUnRegistrationTable.setStatus(_B)
_CgkLocalZoneStatsUnRegistrationTableEntry_Object=MibTableRow
cgkLocalZoneStatsUnRegistrationTableEntry=_CgkLocalZoneStatsUnRegistrationTableEntry_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1))
cgkLocalZoneStatsUnRegistrationTableEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cgkLocalZoneStatsUnRegistrationTableEntry.setStatus(_B)
_CgkLZoneStatsRcvdUnregistrationRequests_Type=Counter32
_CgkLZoneStatsRcvdUnregistrationRequests_Object=MibTableColumn
cgkLZoneStatsRcvdUnregistrationRequests=_CgkLZoneStatsRcvdUnregistrationRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1,1),_CgkLZoneStatsRcvdUnregistrationRequests_Type())
cgkLZoneStatsRcvdUnregistrationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdUnregistrationRequests.setStatus(_B)
_CgkLZoneStatsSentUnregistrationRequests_Type=Counter32
_CgkLZoneStatsSentUnregistrationRequests_Object=MibTableColumn
cgkLZoneStatsSentUnregistrationRequests=_CgkLZoneStatsSentUnregistrationRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1,2),_CgkLZoneStatsSentUnregistrationRequests_Type())
cgkLZoneStatsSentUnregistrationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentUnregistrationRequests.setStatus(_B)
_CgkLZoneStatsTimeoutSentUnregistrationRequests_Type=Counter32
_CgkLZoneStatsTimeoutSentUnregistrationRequests_Object=MibTableColumn
cgkLZoneStatsTimeoutSentUnregistrationRequests=_CgkLZoneStatsTimeoutSentUnregistrationRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1,3),_CgkLZoneStatsTimeoutSentUnregistrationRequests_Type())
cgkLZoneStatsTimeoutSentUnregistrationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsTimeoutSentUnregistrationRequests.setStatus(_B)
_CgkLZoneStatsRcvdUnregistrationConfirms_Type=Counter32
_CgkLZoneStatsRcvdUnregistrationConfirms_Object=MibTableColumn
cgkLZoneStatsRcvdUnregistrationConfirms=_CgkLZoneStatsRcvdUnregistrationConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1,4),_CgkLZoneStatsRcvdUnregistrationConfirms_Type())
cgkLZoneStatsRcvdUnregistrationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdUnregistrationConfirms.setStatus(_B)
_CgkLZoneStatsSentUnregistrationConfirms_Type=Counter32
_CgkLZoneStatsSentUnregistrationConfirms_Object=MibTableColumn
cgkLZoneStatsSentUnregistrationConfirms=_CgkLZoneStatsSentUnregistrationConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1,5),_CgkLZoneStatsSentUnregistrationConfirms_Type())
cgkLZoneStatsSentUnregistrationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentUnregistrationConfirms.setStatus(_B)
_CgkLZoneStatsRcvdUnregistrationRejects_Type=Counter32
_CgkLZoneStatsRcvdUnregistrationRejects_Object=MibTableColumn
cgkLZoneStatsRcvdUnregistrationRejects=_CgkLZoneStatsRcvdUnregistrationRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1,6),_CgkLZoneStatsRcvdUnregistrationRejects_Type())
cgkLZoneStatsRcvdUnregistrationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdUnregistrationRejects.setStatus(_B)
_CgkLZoneStatsSentUnregistrationRejects_Type=Counter32
_CgkLZoneStatsSentUnregistrationRejects_Object=MibTableColumn
cgkLZoneStatsSentUnregistrationRejects=_CgkLZoneStatsSentUnregistrationRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,4,1,7),_CgkLZoneStatsSentUnregistrationRejects_Type())
cgkLZoneStatsSentUnregistrationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentUnregistrationRejects.setStatus(_B)
_CgkLocalZoneStatsDisengageTable_Object=MibTable
cgkLocalZoneStatsDisengageTable=_CgkLocalZoneStatsDisengageTable_Object((1,3,6,1,4,1,9,10,40,1,1,4,5))
if mibBuilder.loadTexts:cgkLocalZoneStatsDisengageTable.setStatus(_B)
_CgkLocalZoneStatsDisengageTableEntry_Object=MibTableRow
cgkLocalZoneStatsDisengageTableEntry=_CgkLocalZoneStatsDisengageTableEntry_Object((1,3,6,1,4,1,9,10,40,1,1,4,5,1))
cgkLocalZoneStatsDisengageTableEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cgkLocalZoneStatsDisengageTableEntry.setStatus(_B)
_CgkLZoneStatsRcvdDisengageRequests_Type=Counter32
_CgkLZoneStatsRcvdDisengageRequests_Object=MibTableColumn
cgkLZoneStatsRcvdDisengageRequests=_CgkLZoneStatsRcvdDisengageRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,5,1,1),_CgkLZoneStatsRcvdDisengageRequests_Type())
cgkLZoneStatsRcvdDisengageRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdDisengageRequests.setStatus(_B)
_CgkLZoneStatsSentDisengageRequests_Type=Counter32
_CgkLZoneStatsSentDisengageRequests_Object=MibTableColumn
cgkLZoneStatsSentDisengageRequests=_CgkLZoneStatsSentDisengageRequests_Object((1,3,6,1,4,1,9,10,40,1,1,4,5,1,2),_CgkLZoneStatsSentDisengageRequests_Type())
cgkLZoneStatsSentDisengageRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentDisengageRequests.setStatus(_B)
_CgkLZoneStatsRcvdDisengageConfirms_Type=Counter32
_CgkLZoneStatsRcvdDisengageConfirms_Object=MibTableColumn
cgkLZoneStatsRcvdDisengageConfirms=_CgkLZoneStatsRcvdDisengageConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,5,1,3),_CgkLZoneStatsRcvdDisengageConfirms_Type())
cgkLZoneStatsRcvdDisengageConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdDisengageConfirms.setStatus(_B)
_CgkLZoneStatsSentDisengageConfirms_Type=Counter32
_CgkLZoneStatsSentDisengageConfirms_Object=MibTableColumn
cgkLZoneStatsSentDisengageConfirms=_CgkLZoneStatsSentDisengageConfirms_Object((1,3,6,1,4,1,9,10,40,1,1,4,5,1,4),_CgkLZoneStatsSentDisengageConfirms_Type())
cgkLZoneStatsSentDisengageConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentDisengageConfirms.setStatus(_B)
_CgkLZoneStatsRcvdDisengageRejects_Type=Counter32
_CgkLZoneStatsRcvdDisengageRejects_Object=MibTableColumn
cgkLZoneStatsRcvdDisengageRejects=_CgkLZoneStatsRcvdDisengageRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,5,1,5),_CgkLZoneStatsRcvdDisengageRejects_Type())
cgkLZoneStatsRcvdDisengageRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsRcvdDisengageRejects.setStatus(_B)
_CgkLZoneStatsSentDisengageRejects_Type=Counter32
_CgkLZoneStatsSentDisengageRejects_Object=MibTableColumn
cgkLZoneStatsSentDisengageRejects=_CgkLZoneStatsSentDisengageRejects_Object((1,3,6,1,4,1,9,10,40,1,1,4,5,1,6),_CgkLZoneStatsSentDisengageRejects_Type())
cgkLZoneStatsSentDisengageRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkLZoneStatsSentDisengageRejects.setStatus(_B)
_CgkRemoteZone_ObjectIdentity=ObjectIdentity
cgkRemoteZone=_CgkRemoteZone_ObjectIdentity((1,3,6,1,4,1,9,10,40,1,1,5))
class _CgkRZoneTotalBandwidth_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000000000))
_CgkRZoneTotalBandwidth_Type.__name__=_D
_CgkRZoneTotalBandwidth_Object=MibScalar
cgkRZoneTotalBandwidth=_CgkRZoneTotalBandwidth_Object((1,3,6,1,4,1,9,10,40,1,1,5,1),_CgkRZoneTotalBandwidth_Type())
cgkRZoneTotalBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkRZoneTotalBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkRZoneTotalBandwidth.setUnits(_G)
class _CgkRZoneAllocTotalBandwidth_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CgkRZoneAllocTotalBandwidth_Type.__name__=_O
_CgkRZoneAllocTotalBandwidth_Object=MibScalar
cgkRZoneAllocTotalBandwidth=_CgkRZoneAllocTotalBandwidth_Object((1,3,6,1,4,1,9,10,40,1,1,5,2),_CgkRZoneAllocTotalBandwidth_Type())
cgkRZoneAllocTotalBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkRZoneAllocTotalBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkRZoneAllocTotalBandwidth.setUnits(_G)
_CgkHistory_ObjectIdentity=ObjectIdentity
cgkHistory=_CgkHistory_ObjectIdentity((1,3,6,1,4,1,9,10,40,1,2))
class _CgkHistoryMaxEventEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CgkHistoryMaxEventEntries_Type.__name__=_D
_CgkHistoryMaxEventEntries_Object=MibScalar
cgkHistoryMaxEventEntries=_CgkHistoryMaxEventEntries_Object((1,3,6,1,4,1,9,10,40,1,2,1),_CgkHistoryMaxEventEntries_Type())
cgkHistoryMaxEventEntries.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkHistoryMaxEventEntries.setStatus(_B)
_CgkHistoryEventTable_Object=MibTable
cgkHistoryEventTable=_CgkHistoryEventTable_Object((1,3,6,1,4,1,9,10,40,1,2,2))
if mibBuilder.loadTexts:cgkHistoryEventTable.setStatus(_B)
_CgkHistoryEventEntry_Object=MibTableRow
cgkHistoryEventEntry=_CgkHistoryEventEntry_Object((1,3,6,1,4,1,9,10,40,1,2,2,1))
cgkHistoryEventEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:cgkHistoryEventEntry.setStatus(_B)
class _CgkHistoryEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CgkHistoryEventIndex_Type.__name__=_D
_CgkHistoryEventIndex_Object=MibTableColumn
cgkHistoryEventIndex=_CgkHistoryEventIndex_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,1),_CgkHistoryEventIndex_Type())
cgkHistoryEventIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:cgkHistoryEventIndex.setStatus(_B)
class _CgkHistoryEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('register',2),('unregister',3),('unregisterForced',4),('overload',5)))
_CgkHistoryEventType_Type.__name__=_D
_CgkHistoryEventType_Object=MibTableColumn
cgkHistoryEventType=_CgkHistoryEventType_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,2),_CgkHistoryEventType_Type())
cgkHistoryEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkHistoryEventType.setStatus(_B)
_CgkHistoryEventTime_Type=TimeStamp
_CgkHistoryEventTime_Object=MibTableColumn
cgkHistoryEventTime=_CgkHistoryEventTime_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,3),_CgkHistoryEventTime_Type())
cgkHistoryEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkHistoryEventTime.setStatus(_B)
_CgkHistoryEventText_Type=DisplayString
_CgkHistoryEventText_Object=MibTableColumn
cgkHistoryEventText=_CgkHistoryEventText_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,4),_CgkHistoryEventText_Type())
cgkHistoryEventText.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkHistoryEventText.setStatus(_B)
class _CgkHistoryEventEndpointType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('other',2),('gatekeeper',3),('gateway',4),('mcu',5),('terminal',6),('proxy',7)))
_CgkHistoryEventEndpointType_Type.__name__=_D
_CgkHistoryEventEndpointType_Object=MibTableColumn
cgkHistoryEventEndpointType=_CgkHistoryEventEndpointType_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,5),_CgkHistoryEventEndpointType_Type())
cgkHistoryEventEndpointType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkHistoryEventEndpointType.setStatus(_B)
_CgkHistoryEventEndpointAddrTag_Type=CgkNAddressTag
_CgkHistoryEventEndpointAddrTag_Object=MibTableColumn
cgkHistoryEventEndpointAddrTag=_CgkHistoryEventEndpointAddrTag_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,6),_CgkHistoryEventEndpointAddrTag_Type())
cgkHistoryEventEndpointAddrTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkHistoryEventEndpointAddrTag.setStatus(_B)
_CgkHistoryEventEndpointAddress_Type=CgkNAddress
_CgkHistoryEventEndpointAddress_Object=MibTableColumn
cgkHistoryEventEndpointAddress=_CgkHistoryEventEndpointAddress_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,7),_CgkHistoryEventEndpointAddress_Type())
cgkHistoryEventEndpointAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkHistoryEventEndpointAddress.setStatus(_B)
_CgkHistoryEventEndpointH323id_Type=SnmpAdminString
_CgkHistoryEventEndpointH323id_Object=MibTableColumn
cgkHistoryEventEndpointH323id=_CgkHistoryEventEndpointH323id_Object((1,3,6,1,4,1,9,10,40,1,2,2,1,8),_CgkHistoryEventEndpointH323id_Type())
cgkHistoryEventEndpointH323id.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkHistoryEventEndpointH323id.setStatus(_B)
_CgkGeneralConfig_ObjectIdentity=ObjectIdentity
cgkGeneralConfig=_CgkGeneralConfig_ObjectIdentity((1,3,6,1,4,1,9,10,40,1,3))
class _CgkMIBEnableEventNotification_Type(TruthValue):defaultValue=2
_CgkMIBEnableEventNotification_Type.__name__=_Y
_CgkMIBEnableEventNotification_Object=MibScalar
cgkMIBEnableEventNotification=_CgkMIBEnableEventNotification_Object((1,3,6,1,4,1,9,10,40,1,3,1),_CgkMIBEnableEventNotification_Type())
cgkMIBEnableEventNotification.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkMIBEnableEventNotification.setStatus(_B)
class _CgkMIBDefaultTotalBandwidth_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000000000))
_CgkMIBDefaultTotalBandwidth_Type.__name__=_D
_CgkMIBDefaultTotalBandwidth_Object=MibScalar
cgkMIBDefaultTotalBandwidth=_CgkMIBDefaultTotalBandwidth_Object((1,3,6,1,4,1,9,10,40,1,3,2),_CgkMIBDefaultTotalBandwidth_Type())
cgkMIBDefaultTotalBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkMIBDefaultTotalBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkMIBDefaultTotalBandwidth.setUnits(_G)
class _CgkMIBDefaultInterzoneBandwidth_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000000000))
_CgkMIBDefaultInterzoneBandwidth_Type.__name__=_D
_CgkMIBDefaultInterzoneBandwidth_Object=MibScalar
cgkMIBDefaultInterzoneBandwidth=_CgkMIBDefaultInterzoneBandwidth_Object((1,3,6,1,4,1,9,10,40,1,3,3),_CgkMIBDefaultInterzoneBandwidth_Type())
cgkMIBDefaultInterzoneBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkMIBDefaultInterzoneBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkMIBDefaultInterzoneBandwidth.setUnits(_G)
class _CgkMIBDefaultSessionBandwidth_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,50000))
_CgkMIBDefaultSessionBandwidth_Type.__name__=_D
_CgkMIBDefaultSessionBandwidth_Object=MibScalar
cgkMIBDefaultSessionBandwidth=_CgkMIBDefaultSessionBandwidth_Object((1,3,6,1,4,1,9,10,40,1,3,4),_CgkMIBDefaultSessionBandwidth_Type())
cgkMIBDefaultSessionBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:cgkMIBDefaultSessionBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cgkMIBDefaultSessionBandwidth.setUnits(_G)
_CgkGeneralStats_ObjectIdentity=ObjectIdentity
cgkGeneralStats=_CgkGeneralStats_ObjectIdentity((1,3,6,1,4,1,9,10,40,1,4))
_CgkStatsAdmissionRequests_Type=Counter32
_CgkStatsAdmissionRequests_Object=MibScalar
cgkStatsAdmissionRequests=_CgkStatsAdmissionRequests_Object((1,3,6,1,4,1,9,10,40,1,4,1),_CgkStatsAdmissionRequests_Type())
cgkStatsAdmissionRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsAdmissionRequests.setStatus(_B)
_CgkStatsOriginAdmissionRequests_Type=Counter32
_CgkStatsOriginAdmissionRequests_Object=MibScalar
cgkStatsOriginAdmissionRequests=_CgkStatsOriginAdmissionRequests_Object((1,3,6,1,4,1,9,10,40,1,4,2),_CgkStatsOriginAdmissionRequests_Type())
cgkStatsOriginAdmissionRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsOriginAdmissionRequests.setStatus(_B)
_CgkStatsAdmissionConfirms_Type=Counter32
_CgkStatsAdmissionConfirms_Object=MibScalar
cgkStatsAdmissionConfirms=_CgkStatsAdmissionConfirms_Object((1,3,6,1,4,1,9,10,40,1,4,3),_CgkStatsAdmissionConfirms_Type())
cgkStatsAdmissionConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsAdmissionConfirms.setStatus(_B)
_CgkStatsOriginAdmissionConfirms_Type=Counter32
_CgkStatsOriginAdmissionConfirms_Object=MibScalar
cgkStatsOriginAdmissionConfirms=_CgkStatsOriginAdmissionConfirms_Object((1,3,6,1,4,1,9,10,40,1,4,4),_CgkStatsOriginAdmissionConfirms_Type())
cgkStatsOriginAdmissionConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsOriginAdmissionConfirms.setStatus(_B)
_CgkStatsAdmissionRejects_Type=Counter32
_CgkStatsAdmissionRejects_Object=MibScalar
cgkStatsAdmissionRejects=_CgkStatsAdmissionRejects_Object((1,3,6,1,4,1,9,10,40,1,4,5),_CgkStatsAdmissionRejects_Type())
cgkStatsAdmissionRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsAdmissionRejects.setStatus(_B)
_CgkStatsOriginAdmissionRejects_Type=Counter32
_CgkStatsOriginAdmissionRejects_Object=MibScalar
cgkStatsOriginAdmissionRejects=_CgkStatsOriginAdmissionRejects_Object((1,3,6,1,4,1,9,10,40,1,4,6),_CgkStatsOriginAdmissionRejects_Type())
cgkStatsOriginAdmissionRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsOriginAdmissionRejects.setStatus(_B)
_CgkStatsTotalConcurrentCalls_Type=Gauge32
_CgkStatsTotalConcurrentCalls_Object=MibScalar
cgkStatsTotalConcurrentCalls=_CgkStatsTotalConcurrentCalls_Object((1,3,6,1,4,1,9,10,40,1,4,7),_CgkStatsTotalConcurrentCalls_Type())
cgkStatsTotalConcurrentCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsTotalConcurrentCalls.setStatus(_B)
_CgkStatsOriginTotalConcurrentCalls_Type=Gauge32
_CgkStatsOriginTotalConcurrentCalls_Object=MibScalar
cgkStatsOriginTotalConcurrentCalls=_CgkStatsOriginTotalConcurrentCalls_Object((1,3,6,1,4,1,9,10,40,1,4,8),_CgkStatsOriginTotalConcurrentCalls_Type())
cgkStatsOriginTotalConcurrentCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsOriginTotalConcurrentCalls.setStatus(_B)
_CgkStatsRcvdLocationRequests_Type=Counter32
_CgkStatsRcvdLocationRequests_Object=MibScalar
cgkStatsRcvdLocationRequests=_CgkStatsRcvdLocationRequests_Object((1,3,6,1,4,1,9,10,40,1,4,9),_CgkStatsRcvdLocationRequests_Type())
cgkStatsRcvdLocationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsRcvdLocationRequests.setStatus(_B)
_CgkStatsSentLocationRequests_Type=Counter32
_CgkStatsSentLocationRequests_Object=MibScalar
cgkStatsSentLocationRequests=_CgkStatsSentLocationRequests_Object((1,3,6,1,4,1,9,10,40,1,4,10),_CgkStatsSentLocationRequests_Type())
cgkStatsSentLocationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsSentLocationRequests.setStatus(_B)
_CgkStatsRcvdLocationConfirms_Type=Counter32
_CgkStatsRcvdLocationConfirms_Object=MibScalar
cgkStatsRcvdLocationConfirms=_CgkStatsRcvdLocationConfirms_Object((1,3,6,1,4,1,9,10,40,1,4,11),_CgkStatsRcvdLocationConfirms_Type())
cgkStatsRcvdLocationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsRcvdLocationConfirms.setStatus(_B)
_CgkStatsSentLocationConfirms_Type=Counter32
_CgkStatsSentLocationConfirms_Object=MibScalar
cgkStatsSentLocationConfirms=_CgkStatsSentLocationConfirms_Object((1,3,6,1,4,1,9,10,40,1,4,12),_CgkStatsSentLocationConfirms_Type())
cgkStatsSentLocationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsSentLocationConfirms.setStatus(_B)
_CgkStatsRcvdLocationRejects_Type=Counter32
_CgkStatsRcvdLocationRejects_Object=MibScalar
cgkStatsRcvdLocationRejects=_CgkStatsRcvdLocationRejects_Object((1,3,6,1,4,1,9,10,40,1,4,13),_CgkStatsRcvdLocationRejects_Type())
cgkStatsRcvdLocationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsRcvdLocationRejects.setStatus(_B)
_CgkStatsSentLocationRejects_Type=Counter32
_CgkStatsSentLocationRejects_Object=MibScalar
cgkStatsSentLocationRejects=_CgkStatsSentLocationRejects_Object((1,3,6,1,4,1,9,10,40,1,4,14),_CgkStatsSentLocationRejects_Type())
cgkStatsSentLocationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsSentLocationRejects.setStatus(_B)
_CgkStatsRegisteredEndpoints_Type=Counter32
_CgkStatsRegisteredEndpoints_Object=MibScalar
cgkStatsRegisteredEndpoints=_CgkStatsRegisteredEndpoints_Object((1,3,6,1,4,1,9,10,40,1,4,15),_CgkStatsRegisteredEndpoints_Type())
cgkStatsRegisteredEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsRegisteredEndpoints.setStatus(_B)
_CgkStatsRcvdDisengageRequests_Type=Counter32
_CgkStatsRcvdDisengageRequests_Object=MibScalar
cgkStatsRcvdDisengageRequests=_CgkStatsRcvdDisengageRequests_Object((1,3,6,1,4,1,9,10,40,1,4,16),_CgkStatsRcvdDisengageRequests_Type())
cgkStatsRcvdDisengageRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsRcvdDisengageRequests.setStatus(_B)
_CgkStatsSentDisengageRequests_Type=Counter32
_CgkStatsSentDisengageRequests_Object=MibScalar
cgkStatsSentDisengageRequests=_CgkStatsSentDisengageRequests_Object((1,3,6,1,4,1,9,10,40,1,4,17),_CgkStatsSentDisengageRequests_Type())
cgkStatsSentDisengageRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsSentDisengageRequests.setStatus(_B)
_CgkStatsRcvdDisengageConfirms_Type=Counter32
_CgkStatsRcvdDisengageConfirms_Object=MibScalar
cgkStatsRcvdDisengageConfirms=_CgkStatsRcvdDisengageConfirms_Object((1,3,6,1,4,1,9,10,40,1,4,18),_CgkStatsRcvdDisengageConfirms_Type())
cgkStatsRcvdDisengageConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsRcvdDisengageConfirms.setStatus(_B)
_CgkStatsSentDisengageConfirms_Type=Counter32
_CgkStatsSentDisengageConfirms_Object=MibScalar
cgkStatsSentDisengageConfirms=_CgkStatsSentDisengageConfirms_Object((1,3,6,1,4,1,9,10,40,1,4,19),_CgkStatsSentDisengageConfirms_Type())
cgkStatsSentDisengageConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsSentDisengageConfirms.setStatus(_B)
_CgkStatsRcvdDisengageRejects_Type=Counter32
_CgkStatsRcvdDisengageRejects_Object=MibScalar
cgkStatsRcvdDisengageRejects=_CgkStatsRcvdDisengageRejects_Object((1,3,6,1,4,1,9,10,40,1,4,20),_CgkStatsRcvdDisengageRejects_Type())
cgkStatsRcvdDisengageRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsRcvdDisengageRejects.setStatus(_B)
_CgkStatsSentDisengageRejects_Type=Counter32
_CgkStatsSentDisengageRejects_Object=MibScalar
cgkStatsSentDisengageRejects=_CgkStatsSentDisengageRejects_Object((1,3,6,1,4,1,9,10,40,1,4,21),_CgkStatsSentDisengageRejects_Type())
cgkStatsSentDisengageRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cgkStatsSentDisengageRejects.setStatus(_B)
_CiscoGatekeeperMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoGatekeeperMIBNotificationPrefix=_CiscoGatekeeperMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,40,2))
_CiscoGatekeeperMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoGatekeeperMIBNotifications=_CiscoGatekeeperMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,40,2,0))
_CiscoGatekeeperMIBConformance_ObjectIdentity=ObjectIdentity
ciscoGatekeeperMIBConformance=_CiscoGatekeeperMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,40,3))
_CiscoGatekeeperMIBCompliance_ObjectIdentity=ObjectIdentity
ciscoGatekeeperMIBCompliance=_CiscoGatekeeperMIBCompliance_ObjectIdentity((1,3,6,1,4,1,9,10,40,3,1))
_CiscoGatekeeperMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGatekeeperMIBGroups=_CiscoGatekeeperMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,40,3,2))
cgkZoneGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,1))
cgkZoneGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:cgkZoneGroup.setStatus(_B)
cgkZoneSubnetGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,2))
cgkZoneSubnetGroup.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cgkZoneSubnetGroup.setStatus(_B)
cgkLocalZoneGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,3))
cgkLocalZoneGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_Z)))
if mibBuilder.loadTexts:cgkLocalZoneGroup.setStatus(_I)
cgkHistoryEventGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,4))
cgkHistoryEventGroup.setObjects(*((_A,_A6),(_A,_a),(_A,_A7),(_A,_A8),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A9)))
if mibBuilder.loadTexts:cgkHistoryEventGroup.setStatus(_B)
cgkGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,5))
cgkGeneralGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:cgkGeneralGroup.setStatus(_B)
cgkLocalZoneGroupRev1=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,7))
cgkLocalZoneGroupRev1.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_Z),(_A,_f)))
if mibBuilder.loadTexts:cgkLocalZoneGroupRev1.setStatus(_I)
cgkLocalZoneGroupRev2=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,8))
cgkLocalZoneGroupRev2.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_f),(_A,_AD)))
if mibBuilder.loadTexts:cgkLocalZoneGroupRev2.setStatus(_B)
cgkZoneMgmtStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,9))
cgkZoneMgmtStatsGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:cgkZoneMgmtStatsGroup.setStatus(_B)
cgkGeneralMgmtStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,10))
cgkGeneralMgmtStatsGroup.setObjects(*((_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:cgkGeneralMgmtStatsGroup.setStatus(_B)
cgkRemoteZoneGroup=ObjectGroup((1,3,6,1,4,1,9,10,40,3,2,11))
cgkRemoteZoneGroup.setObjects(*((_A,_B0),(_A,_B1)))
if mibBuilder.loadTexts:cgkRemoteZoneGroup.setStatus(_B)
ciscoGatekeeperEvent=NotificationType((1,3,6,1,4,1,9,10,40,2,0,1))
ciscoGatekeeperEvent.setObjects(*((_A,_a),(_A,_b),(_A,_d),(_A,_c),(_A,_e)))
if mibBuilder.loadTexts:ciscoGatekeeperEvent.setStatus(_B)
cgkNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,40,3,2,6))
cgkNotificationsGroup.setObjects((_A,_B2))
if mibBuilder.loadTexts:cgkNotificationsGroup.setStatus(_B)
cgkGatekeeperCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,40,3,1,1))
cgkGatekeeperCompliance.setObjects(*((_A,_J),(_A,_K),(_A,_B3),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cgkGatekeeperCompliance.setStatus(_I)
cgkGatekeeperComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,40,3,1,2))
cgkGatekeeperComplianceRev1.setObjects(*((_A,_J),(_A,_K),(_A,_B4),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cgkGatekeeperComplianceRev1.setStatus(_I)
cgkGatekeeperComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,10,40,3,1,3))
cgkGatekeeperComplianceRev2.setObjects(*((_A,_J),(_A,_K),(_A,_X),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cgkGatekeeperComplianceRev2.setStatus(_I)
cgkGatekeeperComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,10,40,3,1,4))
cgkGatekeeperComplianceRev3.setObjects(*((_A,_J),(_A,_K),(_A,_X),(_A,_L),(_A,_M),(_A,_g),(_A,_h),(_A,_N)))
if mibBuilder.loadTexts:cgkGatekeeperComplianceRev3.setStatus(_I)
cgkGatekeeperComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,10,40,3,1,5))
cgkGatekeeperComplianceRev4.setObjects(*((_A,_J),(_A,_K),(_A,_X),(_A,_L),(_A,_M),(_A,_g),(_A,_h),(_A,_N),(_A,_B5)))
if mibBuilder.loadTexts:cgkGatekeeperComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoGatekeeperMIB':ciscoGatekeeperMIB,'ciscoGatekeeperMIBObjects':ciscoGatekeeperMIBObjects,'cgkZone':cgkZone,'cgkZoneTable':cgkZoneTable,'cgkZoneEntry':cgkZoneEntry,_H:cgkZoneIndex,_r:cgkZoneZoneName,_s:cgkZoneDomain,_t:cgkZoneRasAddressTag,_u:cgkZoneRasAddress,_v:cgkZoneIrrFrequency,_w:cgkZoneLocalZone,_x:cgkZoneDefaultSubnetFlags,_y:cgkZoneAddressLookupFailures,_z:cgkZoneEndpointTimeouts,_A0:cgkZoneOtherFailures,_A1:cgkZoneLRQs,_A2:cgkZoneRowStatus,'cgkZoneSubnetTable':cgkZoneSubnetTable,'cgkZoneSubnetEntry':cgkZoneSubnetEntry,_o:cgkZoneSubnetTag,_p:cgkZoneSubnetAddress,_A3:cgkZoneSubnetMask,_A4:cgkZoneSubnetFlags,_A5:cgkZoneSubnetRowStatus,'cgkLocalZoneTable':cgkLocalZoneTable,'cgkLocalZoneEntry':cgkLocalZoneEntry,_Q:cgkLZoneACFs,_R:cgkLZoneARJs,_S:cgkLZoneTotalBandwidth,_T:cgkLZoneAllocTotalBandwidth,_U:cgkLZoneInterzoneBandwidth,_V:cgkLZoneAllocInterzoneBandwidth,_W:cgkLZoneSessionBandwidth,_Z:cgkLZoneProxiedCall,_f:cgkLZoneProxiedCallBits,_AD:cgkLZoneTotalConcurrentCalls,'cgkZoneStats':cgkZoneStats,'cgkLocalZoneStatsAdmissionTable':cgkLocalZoneStatsAdmissionTable,'cgkLocalZoneStatsAdmissionTableEntry':cgkLocalZoneStatsAdmissionTableEntry,_AE:cgkLZoneStatsAdmissionRequests,_AF:cgkLZoneStatsOriginAdmissionRequests,_AG:cgkLZoneStatsOriginAdmissionConfirms,_AH:cgkLZoneStatsOriginAdmissionRejects,_AI:cgkLZoneStatsOriginTotalConcurrentCalls,'cgkLocalZoneStatsLocationTable':cgkLocalZoneStatsLocationTable,'cgkLocalZoneStatsLocationTableEntry':cgkLocalZoneStatsLocationTableEntry,_AJ:cgkLZoneStatsSentLocationRequests,_AK:cgkLZoneStatsRcvdLocationConfirms,_AL:cgkLZoneStatsSentLocationConfirms,_AM:cgkLZoneStatsRcvdLocationRejects,_AN:cgkLZoneStatsSentLocationRejects,'cgkLocalZoneStatsRegistrationTable':cgkLocalZoneStatsRegistrationTable,'cgkLocalZoneStatsRegistrationTableEntry':cgkLocalZoneStatsRegistrationTableEntry,_AO:cgkLZoneStatsFullRegistrationRequests,_AP:cgkLZoneStatsLightRegistrationRequests,_AQ:cgkLZoneStatsRegistrationConfirms,_AR:cgkLZoneStatsRegistrationRejects,_AS:cgkLZoneStatsRegisteredEndpoints,'cgkLocalZoneStatsUnRegistrationTable':cgkLocalZoneStatsUnRegistrationTable,'cgkLocalZoneStatsUnRegistrationTableEntry':cgkLocalZoneStatsUnRegistrationTableEntry,_AT:cgkLZoneStatsRcvdUnregistrationRequests,_AU:cgkLZoneStatsSentUnregistrationRequests,_AV:cgkLZoneStatsTimeoutSentUnregistrationRequests,_AW:cgkLZoneStatsRcvdUnregistrationConfirms,_AX:cgkLZoneStatsSentUnregistrationConfirms,_AY:cgkLZoneStatsRcvdUnregistrationRejects,_AZ:cgkLZoneStatsSentUnregistrationRejects,'cgkLocalZoneStatsDisengageTable':cgkLocalZoneStatsDisengageTable,'cgkLocalZoneStatsDisengageTableEntry':cgkLocalZoneStatsDisengageTableEntry,_Aa:cgkLZoneStatsRcvdDisengageRequests,_Ab:cgkLZoneStatsSentDisengageRequests,_Ac:cgkLZoneStatsRcvdDisengageConfirms,_Ad:cgkLZoneStatsSentDisengageConfirms,_Ae:cgkLZoneStatsRcvdDisengageRejects,_Af:cgkLZoneStatsSentDisengageRejects,'cgkRemoteZone':cgkRemoteZone,_B0:cgkRZoneTotalBandwidth,_B1:cgkRZoneAllocTotalBandwidth,'cgkHistory':cgkHistory,_A6:cgkHistoryMaxEventEntries,'cgkHistoryEventTable':cgkHistoryEventTable,'cgkHistoryEventEntry':cgkHistoryEventEntry,_q:cgkHistoryEventIndex,_a:cgkHistoryEventType,_A7:cgkHistoryEventTime,_A8:cgkHistoryEventText,_b:cgkHistoryEventEndpointType,_d:cgkHistoryEventEndpointAddrTag,_c:cgkHistoryEventEndpointAddress,_e:cgkHistoryEventEndpointH323id,'cgkGeneralConfig':cgkGeneralConfig,_A9:cgkMIBEnableEventNotification,_AA:cgkMIBDefaultTotalBandwidth,_AB:cgkMIBDefaultInterzoneBandwidth,_AC:cgkMIBDefaultSessionBandwidth,'cgkGeneralStats':cgkGeneralStats,_Ag:cgkStatsAdmissionRequests,_Ah:cgkStatsOriginAdmissionRequests,_Ai:cgkStatsAdmissionConfirms,_Aj:cgkStatsOriginAdmissionConfirms,_Ak:cgkStatsAdmissionRejects,_Al:cgkStatsOriginAdmissionRejects,_Am:cgkStatsTotalConcurrentCalls,_An:cgkStatsOriginTotalConcurrentCalls,_Ao:cgkStatsRcvdLocationRequests,_Ap:cgkStatsSentLocationRequests,_Aq:cgkStatsRcvdLocationConfirms,_Ar:cgkStatsSentLocationConfirms,_As:cgkStatsRcvdLocationRejects,_At:cgkStatsSentLocationRejects,_Au:cgkStatsRegisteredEndpoints,_Av:cgkStatsRcvdDisengageRequests,_Aw:cgkStatsSentDisengageRequests,_Ax:cgkStatsRcvdDisengageConfirms,_Ay:cgkStatsSentDisengageConfirms,_Az:cgkStatsRcvdDisengageRejects,_A_:cgkStatsSentDisengageRejects,'ciscoGatekeeperMIBNotificationPrefix':ciscoGatekeeperMIBNotificationPrefix,'ciscoGatekeeperMIBNotifications':ciscoGatekeeperMIBNotifications,_B2:ciscoGatekeeperEvent,'ciscoGatekeeperMIBConformance':ciscoGatekeeperMIBConformance,'ciscoGatekeeperMIBCompliance':ciscoGatekeeperMIBCompliance,'cgkGatekeeperCompliance':cgkGatekeeperCompliance,'cgkGatekeeperComplianceRev1':cgkGatekeeperComplianceRev1,'cgkGatekeeperComplianceRev2':cgkGatekeeperComplianceRev2,'cgkGatekeeperComplianceRev3':cgkGatekeeperComplianceRev3,'cgkGatekeeperComplianceRev4':cgkGatekeeperComplianceRev4,'ciscoGatekeeperMIBGroups':ciscoGatekeeperMIBGroups,_J:cgkZoneGroup,_K:cgkZoneSubnetGroup,_B3:cgkLocalZoneGroup,_L:cgkHistoryEventGroup,_M:cgkGeneralGroup,_N:cgkNotificationsGroup,_B4:cgkLocalZoneGroupRev1,_X:cgkLocalZoneGroupRev2,_g:cgkZoneMgmtStatsGroup,_h:cgkGeneralMgmtStatsGroup,_B5:cgkRemoteZoneGroup})