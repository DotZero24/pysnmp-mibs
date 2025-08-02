_r='ciscoLwappDhcpMIBConfigGroup'
_q='cLDhcpTrapSet'
_p='cLDhcpScopeName'
_o='cLDhcpLastRequestTime'
_n='cLDhcpLastResponseTime'
_m='cLDhcpTxFailures'
_l='cLDhcpNakPackets'
_k='cLDhcpAckPackets'
_j='cLDhcpOfferPackets'
_i='cLDhcpReplyPackets'
_h='cLDhcpReleasePackets'
_g='cLDhcpInformPackets'
_f='cLDhcpDeclinePackets'
_e='cLDhcpRequestPackets'
_d='cLDhcpDiscoverPackets'
_c='cLDhcpProxy'
_b='cLDhcpClearDiscontinuityTime'
_a='cLDhcpClearStats'
_Z='cLDhcpOpt37RemoteIdFormat'
_Y='cLDhcpTimeout'
_X='cLDhcpClearAllDiscontinuityTime'
_W='cLDhcpOpt82RemoteIdFormat'
_V='cLDhcpClearAllStats'
_U='cLDhcpScopeIndex'
_T='apEthMacSsid'
_S='apNameVlanId'
_R='apMacVlanId'
_Q='apLocation'
_P='flexGroupName'
_O='apGroupName'
_N='apNameSsid'
_M='apEthMac'
_L='apMacSsid'
_K='not-accessible'
_J='cLDhcpServerInetAddress'
_I='cLDhcpServerInetAddressType'
_H='seconds'
_G='TruthValue'
_F='Integer32'
_E='read-write'
_D='packets'
_C='read-only'
_B='CISCO-LWAPP-DHCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoURLString,=mibBuilder.importSymbols('CISCO-TC','CiscoURLString')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_G)
ciscoLwappDhcpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,792))
if mibBuilder.loadTexts:ciscoLwappDhcpMIB.setRevisions(('2017-04-27 00:00','2012-01-31 00:00'))
_CiscoLwappDhcpMIBNotif_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpMIBNotif=_CiscoLwappDhcpMIBNotif_ObjectIdentity((1,3,6,1,4,1,9,9,792,0))
_CiscoLwappDhcpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpMIBObjects=_CiscoLwappDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,792,1))
_CiscoLwappDhcpGlobalConfig_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpGlobalConfig=_CiscoLwappDhcpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,792,1,1))
class _CLDhcpClearAllStats_Type(TruthValue):defaultValue=2
_CLDhcpClearAllStats_Type.__name__=_G
_CLDhcpClearAllStats_Object=MibScalar
cLDhcpClearAllStats=_CLDhcpClearAllStats_Object((1,3,6,1,4,1,9,9,792,1,1,1),_CLDhcpClearAllStats_Type())
cLDhcpClearAllStats.setMaxAccess(_E)
if mibBuilder.loadTexts:cLDhcpClearAllStats.setStatus(_A)
class _CLDhcpOpt82RemoteIdFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('apMac',1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8),(_S,9),(_T,10)))
_CLDhcpOpt82RemoteIdFormat_Type.__name__=_F
_CLDhcpOpt82RemoteIdFormat_Object=MibScalar
cLDhcpOpt82RemoteIdFormat=_CLDhcpOpt82RemoteIdFormat_Object((1,3,6,1,4,1,9,9,792,1,1,2),_CLDhcpOpt82RemoteIdFormat_Type())
cLDhcpOpt82RemoteIdFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:cLDhcpOpt82RemoteIdFormat.setStatus(_A)
_CLDhcpClearAllDiscontinuityTime_Type=TimeStamp
_CLDhcpClearAllDiscontinuityTime_Object=MibScalar
cLDhcpClearAllDiscontinuityTime=_CLDhcpClearAllDiscontinuityTime_Object((1,3,6,1,4,1,9,9,792,1,1,3),_CLDhcpClearAllDiscontinuityTime_Type())
cLDhcpClearAllDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpClearAllDiscontinuityTime.setStatus(_A)
_CLDhcpTimeout_Type=Unsigned32
_CLDhcpTimeout_Object=MibScalar
cLDhcpTimeout=_CLDhcpTimeout_Object((1,3,6,1,4,1,9,9,792,1,1,4),_CLDhcpTimeout_Type())
cLDhcpTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cLDhcpTimeout.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpTimeout.setUnits(_H)
class _CLDhcpOpt37RemoteIdFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('apMac',1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8),(_S,9),(_T,10)))
_CLDhcpOpt37RemoteIdFormat_Type.__name__=_F
_CLDhcpOpt37RemoteIdFormat_Object=MibScalar
cLDhcpOpt37RemoteIdFormat=_CLDhcpOpt37RemoteIdFormat_Object((1,3,6,1,4,1,9,9,792,1,1,5),_CLDhcpOpt37RemoteIdFormat_Type())
cLDhcpOpt37RemoteIdFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:cLDhcpOpt37RemoteIdFormat.setStatus(_A)
_CiscoLwappDhcpStatsConfig_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpStatsConfig=_CiscoLwappDhcpStatsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,792,1,2))
_CLDhcpStatsConfigTable_Object=MibTable
cLDhcpStatsConfigTable=_CLDhcpStatsConfigTable_Object((1,3,6,1,4,1,9,9,792,1,2,1))
if mibBuilder.loadTexts:cLDhcpStatsConfigTable.setStatus(_A)
_CLDhcpStatsConfigEntry_Object=MibTableRow
cLDhcpStatsConfigEntry=_CLDhcpStatsConfigEntry_Object((1,3,6,1,4,1,9,9,792,1,2,1,1))
cLDhcpStatsConfigEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cLDhcpStatsConfigEntry.setStatus(_A)
_CLDhcpServerInetAddressType_Type=InetAddressType
_CLDhcpServerInetAddressType_Object=MibTableColumn
cLDhcpServerInetAddressType=_CLDhcpServerInetAddressType_Object((1,3,6,1,4,1,9,9,792,1,2,1,1,1),_CLDhcpServerInetAddressType_Type())
cLDhcpServerInetAddressType.setMaxAccess(_K)
if mibBuilder.loadTexts:cLDhcpServerInetAddressType.setStatus(_A)
_CLDhcpServerInetAddress_Type=InetAddress
_CLDhcpServerInetAddress_Object=MibTableColumn
cLDhcpServerInetAddress=_CLDhcpServerInetAddress_Object((1,3,6,1,4,1,9,9,792,1,2,1,1,2),_CLDhcpServerInetAddress_Type())
cLDhcpServerInetAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:cLDhcpServerInetAddress.setStatus(_A)
class _CLDhcpClearStats_Type(TruthValue):defaultValue=2
_CLDhcpClearStats_Type.__name__=_G
_CLDhcpClearStats_Object=MibTableColumn
cLDhcpClearStats=_CLDhcpClearStats_Object((1,3,6,1,4,1,9,9,792,1,2,1,1,3),_CLDhcpClearStats_Type())
cLDhcpClearStats.setMaxAccess(_E)
if mibBuilder.loadTexts:cLDhcpClearStats.setStatus(_A)
_CLDhcpClearDiscontinuityTime_Type=TimeStamp
_CLDhcpClearDiscontinuityTime_Object=MibTableColumn
cLDhcpClearDiscontinuityTime=_CLDhcpClearDiscontinuityTime_Object((1,3,6,1,4,1,9,9,792,1,2,1,1,4),_CLDhcpClearDiscontinuityTime_Type())
cLDhcpClearDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpClearDiscontinuityTime.setStatus(_A)
_CiscoLwappDhcpStats_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpStats=_CiscoLwappDhcpStats_ObjectIdentity((1,3,6,1,4,1,9,9,792,1,3))
_CLDhcpStatsShowTable_Object=MibTable
cLDhcpStatsShowTable=_CLDhcpStatsShowTable_Object((1,3,6,1,4,1,9,9,792,1,3,1))
if mibBuilder.loadTexts:cLDhcpStatsShowTable.setStatus(_A)
_CLDhcpStatsShowEntry_Object=MibTableRow
cLDhcpStatsShowEntry=_CLDhcpStatsShowEntry_Object((1,3,6,1,4,1,9,9,792,1,3,1,1))
cLDhcpStatsShowEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cLDhcpStatsShowEntry.setStatus(_A)
_CLDhcpProxy_Type=TruthValue
_CLDhcpProxy_Object=MibTableColumn
cLDhcpProxy=_CLDhcpProxy_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,1),_CLDhcpProxy_Type())
cLDhcpProxy.setMaxAccess(_E)
if mibBuilder.loadTexts:cLDhcpProxy.setStatus(_A)
_CLDhcpDiscoverPackets_Type=Counter32
_CLDhcpDiscoverPackets_Object=MibTableColumn
cLDhcpDiscoverPackets=_CLDhcpDiscoverPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,2),_CLDhcpDiscoverPackets_Type())
cLDhcpDiscoverPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpDiscoverPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpDiscoverPackets.setUnits(_D)
_CLDhcpRequestPackets_Type=Counter32
_CLDhcpRequestPackets_Object=MibTableColumn
cLDhcpRequestPackets=_CLDhcpRequestPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,3),_CLDhcpRequestPackets_Type())
cLDhcpRequestPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpRequestPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpRequestPackets.setUnits(_D)
_CLDhcpDeclinePackets_Type=Counter32
_CLDhcpDeclinePackets_Object=MibTableColumn
cLDhcpDeclinePackets=_CLDhcpDeclinePackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,4),_CLDhcpDeclinePackets_Type())
cLDhcpDeclinePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpDeclinePackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpDeclinePackets.setUnits(_D)
_CLDhcpInformPackets_Type=Counter32
_CLDhcpInformPackets_Object=MibTableColumn
cLDhcpInformPackets=_CLDhcpInformPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,5),_CLDhcpInformPackets_Type())
cLDhcpInformPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpInformPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpInformPackets.setUnits(_D)
_CLDhcpReleasePackets_Type=Counter32
_CLDhcpReleasePackets_Object=MibTableColumn
cLDhcpReleasePackets=_CLDhcpReleasePackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,6),_CLDhcpReleasePackets_Type())
cLDhcpReleasePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpReleasePackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpReleasePackets.setUnits(_D)
_CLDhcpReplyPackets_Type=Counter32
_CLDhcpReplyPackets_Object=MibTableColumn
cLDhcpReplyPackets=_CLDhcpReplyPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,7),_CLDhcpReplyPackets_Type())
cLDhcpReplyPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpReplyPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpReplyPackets.setUnits(_D)
_CLDhcpOfferPackets_Type=Counter32
_CLDhcpOfferPackets_Object=MibTableColumn
cLDhcpOfferPackets=_CLDhcpOfferPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,8),_CLDhcpOfferPackets_Type())
cLDhcpOfferPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpOfferPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpOfferPackets.setUnits(_D)
_CLDhcpAckPackets_Type=Counter32
_CLDhcpAckPackets_Object=MibTableColumn
cLDhcpAckPackets=_CLDhcpAckPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,9),_CLDhcpAckPackets_Type())
cLDhcpAckPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpAckPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpAckPackets.setUnits(_D)
_CLDhcpNakPackets_Type=Counter32
_CLDhcpNakPackets_Object=MibTableColumn
cLDhcpNakPackets=_CLDhcpNakPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,10),_CLDhcpNakPackets_Type())
cLDhcpNakPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpNakPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpNakPackets.setUnits(_D)
_CLDhcpTxFailures_Type=Counter32
_CLDhcpTxFailures_Object=MibTableColumn
cLDhcpTxFailures=_CLDhcpTxFailures_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,11),_CLDhcpTxFailures_Type())
cLDhcpTxFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpTxFailures.setStatus(_A)
_CLDhcpLastResponseTime_Type=TimeStamp
_CLDhcpLastResponseTime_Object=MibTableColumn
cLDhcpLastResponseTime=_CLDhcpLastResponseTime_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,12),_CLDhcpLastResponseTime_Type())
cLDhcpLastResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpLastResponseTime.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpLastResponseTime.setUnits(_H)
_CLDhcpLastRequestTime_Type=TimeStamp
_CLDhcpLastRequestTime_Object=MibTableColumn
cLDhcpLastRequestTime=_CLDhcpLastRequestTime_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,13),_CLDhcpLastRequestTime_Type())
cLDhcpLastRequestTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpLastRequestTime.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpLastRequestTime.setUnits(_H)
_CLDhcpRxDiscoverPackets_Type=Counter32
_CLDhcpRxDiscoverPackets_Object=MibTableColumn
cLDhcpRxDiscoverPackets=_CLDhcpRxDiscoverPackets_Object((1,3,6,1,4,1,9,9,792,1,3,1,1,14),_CLDhcpRxDiscoverPackets_Type())
cLDhcpRxDiscoverPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpRxDiscoverPackets.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpRxDiscoverPackets.setUnits(_D)
_CiscoLwappDhcpScopeStats_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpScopeStats=_CiscoLwappDhcpScopeStats_ObjectIdentity((1,3,6,1,4,1,9,9,792,1,4))
_CLDhcpScopeStatsTable_Object=MibTable
cLDhcpScopeStatsTable=_CLDhcpScopeStatsTable_Object((1,3,6,1,4,1,9,9,792,1,4,1))
if mibBuilder.loadTexts:cLDhcpScopeStatsTable.setStatus(_A)
_CLDhcpScopeStatsEntry_Object=MibTableRow
cLDhcpScopeStatsEntry=_CLDhcpScopeStatsEntry_Object((1,3,6,1,4,1,9,9,792,1,4,1,1))
cLDhcpScopeStatsEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:cLDhcpScopeStatsEntry.setStatus(_A)
_CLDhcpScopeIndex_Type=Unsigned32
_CLDhcpScopeIndex_Object=MibTableColumn
cLDhcpScopeIndex=_CLDhcpScopeIndex_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,1),_CLDhcpScopeIndex_Type())
cLDhcpScopeIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cLDhcpScopeIndex.setStatus(_A)
_CLDhcpScopeAddressPoolUsage_Type=Unsigned32
_CLDhcpScopeAddressPoolUsage_Object=MibTableColumn
cLDhcpScopeAddressPoolUsage=_CLDhcpScopeAddressPoolUsage_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,2),_CLDhcpScopeAddressPoolUsage_Type())
cLDhcpScopeAddressPoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeAddressPoolUsage.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpScopeAddressPoolUsage.setUnits('Percent')
_CLDhcpScopeName_Type=SnmpAdminString
_CLDhcpScopeName_Object=MibTableColumn
cLDhcpScopeName=_CLDhcpScopeName_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,3),_CLDhcpScopeName_Type())
cLDhcpScopeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeName.setStatus(_A)
_CLDhcpScopeAllocatedIP_Type=Counter32
_CLDhcpScopeAllocatedIP_Object=MibTableColumn
cLDhcpScopeAllocatedIP=_CLDhcpScopeAllocatedIP_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,4),_CLDhcpScopeAllocatedIP_Type())
cLDhcpScopeAllocatedIP.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeAllocatedIP.setStatus(_A)
_CLDhcpScopeAvailableIP_Type=Counter32
_CLDhcpScopeAvailableIP_Object=MibTableColumn
cLDhcpScopeAvailableIP=_CLDhcpScopeAvailableIP_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,5),_CLDhcpScopeAvailableIP_Type())
cLDhcpScopeAvailableIP.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeAvailableIP.setStatus(_A)
_CLDhcpScopeDiscoverPkts_Type=Counter32
_CLDhcpScopeDiscoverPkts_Object=MibTableColumn
cLDhcpScopeDiscoverPkts=_CLDhcpScopeDiscoverPkts_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,6),_CLDhcpScopeDiscoverPkts_Type())
cLDhcpScopeDiscoverPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeDiscoverPkts.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpScopeDiscoverPkts.setUnits(_D)
_CLDhcpScopeAckPkts_Type=Counter32
_CLDhcpScopeAckPkts_Object=MibTableColumn
cLDhcpScopeAckPkts=_CLDhcpScopeAckPkts_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,7),_CLDhcpScopeAckPkts_Type())
cLDhcpScopeAckPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeAckPkts.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpScopeAckPkts.setUnits(_D)
_CLDhcpScopeOfferPkts_Type=Counter32
_CLDhcpScopeOfferPkts_Object=MibTableColumn
cLDhcpScopeOfferPkts=_CLDhcpScopeOfferPkts_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,8),_CLDhcpScopeOfferPkts_Type())
cLDhcpScopeOfferPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeOfferPkts.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpScopeOfferPkts.setUnits(_D)
_CLDhcpScopeTotalAckPkts_Type=Counter32
_CLDhcpScopeTotalAckPkts_Object=MibTableColumn
cLDhcpScopeTotalAckPkts=_CLDhcpScopeTotalAckPkts_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,9),_CLDhcpScopeTotalAckPkts_Type())
cLDhcpScopeTotalAckPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeTotalAckPkts.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpScopeTotalAckPkts.setUnits(_D)
_CLDhcpScopeRequestPkts_Type=Counter32
_CLDhcpScopeRequestPkts_Object=MibTableColumn
cLDhcpScopeRequestPkts=_CLDhcpScopeRequestPkts_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,10),_CLDhcpScopeRequestPkts_Type())
cLDhcpScopeRequestPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeRequestPkts.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpScopeRequestPkts.setUnits(_D)
_CLDhcpScopeRequestGoodPkts_Type=Counter32
_CLDhcpScopeRequestGoodPkts_Object=MibTableColumn
cLDhcpScopeRequestGoodPkts=_CLDhcpScopeRequestGoodPkts_Object((1,3,6,1,4,1,9,9,792,1,4,1,1,11),_CLDhcpScopeRequestGoodPkts_Type())
cLDhcpScopeRequestGoodPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpScopeRequestGoodPkts.setStatus(_A)
if mibBuilder.loadTexts:cLDhcpScopeRequestGoodPkts.setUnits(_D)
_CiscoLwappDhcpMIBNotifObjects_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpMIBNotifObjects=_CiscoLwappDhcpMIBNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,792,1,5))
_CLDhcpTrapSet_Type=TruthValue
_CLDhcpTrapSet_Object=MibScalar
cLDhcpTrapSet=_CLDhcpTrapSet_Object((1,3,6,1,4,1,9,9,792,1,5,1),_CLDhcpTrapSet_Type())
cLDhcpTrapSet.setMaxAccess(_C)
if mibBuilder.loadTexts:cLDhcpTrapSet.setStatus(_A)
_CiscoLwappDhcpMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpMIBConform=_CiscoLwappDhcpMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,792,2))
_CiscoLwappDhcpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpMIBCompliances=_CiscoLwappDhcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,792,2,1))
_CiscoLwappDhcpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappDhcpMIBGroups=_CiscoLwappDhcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,792,2,2))
ciscoLwappDhcpMIBConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,792,2,2,1))
ciscoLwappDhcpMIBConfigGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoLwappDhcpMIBConfigGroup.setStatus(_A)
ciscoLwappDhcpScopeAddressExhaust=NotificationType((1,3,6,1,4,1,9,9,792,0,1))
ciscoLwappDhcpScopeAddressExhaust.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoLwappDhcpScopeAddressExhaust.setStatus(_A)
ciscoLwappDhcpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,792,2,1,1))
ciscoLwappDhcpMIBCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:ciscoLwappDhcpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLwappDhcpMIB':ciscoLwappDhcpMIB,'ciscoLwappDhcpMIBNotif':ciscoLwappDhcpMIBNotif,'ciscoLwappDhcpScopeAddressExhaust':ciscoLwappDhcpScopeAddressExhaust,'ciscoLwappDhcpMIBObjects':ciscoLwappDhcpMIBObjects,'ciscoLwappDhcpGlobalConfig':ciscoLwappDhcpGlobalConfig,_V:cLDhcpClearAllStats,_W:cLDhcpOpt82RemoteIdFormat,_X:cLDhcpClearAllDiscontinuityTime,_Y:cLDhcpTimeout,_Z:cLDhcpOpt37RemoteIdFormat,'ciscoLwappDhcpStatsConfig':ciscoLwappDhcpStatsConfig,'cLDhcpStatsConfigTable':cLDhcpStatsConfigTable,'cLDhcpStatsConfigEntry':cLDhcpStatsConfigEntry,_I:cLDhcpServerInetAddressType,_J:cLDhcpServerInetAddress,_a:cLDhcpClearStats,_b:cLDhcpClearDiscontinuityTime,'ciscoLwappDhcpStats':ciscoLwappDhcpStats,'cLDhcpStatsShowTable':cLDhcpStatsShowTable,'cLDhcpStatsShowEntry':cLDhcpStatsShowEntry,_c:cLDhcpProxy,_d:cLDhcpDiscoverPackets,_e:cLDhcpRequestPackets,_f:cLDhcpDeclinePackets,_g:cLDhcpInformPackets,_h:cLDhcpReleasePackets,_i:cLDhcpReplyPackets,_j:cLDhcpOfferPackets,_k:cLDhcpAckPackets,_l:cLDhcpNakPackets,_m:cLDhcpTxFailures,_n:cLDhcpLastResponseTime,_o:cLDhcpLastRequestTime,'cLDhcpRxDiscoverPackets':cLDhcpRxDiscoverPackets,'ciscoLwappDhcpScopeStats':ciscoLwappDhcpScopeStats,'cLDhcpScopeStatsTable':cLDhcpScopeStatsTable,'cLDhcpScopeStatsEntry':cLDhcpScopeStatsEntry,_U:cLDhcpScopeIndex,'cLDhcpScopeAddressPoolUsage':cLDhcpScopeAddressPoolUsage,_p:cLDhcpScopeName,'cLDhcpScopeAllocatedIP':cLDhcpScopeAllocatedIP,'cLDhcpScopeAvailableIP':cLDhcpScopeAvailableIP,'cLDhcpScopeDiscoverPkts':cLDhcpScopeDiscoverPkts,'cLDhcpScopeAckPkts':cLDhcpScopeAckPkts,'cLDhcpScopeOfferPkts':cLDhcpScopeOfferPkts,'cLDhcpScopeTotalAckPkts':cLDhcpScopeTotalAckPkts,'cLDhcpScopeRequestPkts':cLDhcpScopeRequestPkts,'cLDhcpScopeRequestGoodPkts':cLDhcpScopeRequestGoodPkts,'ciscoLwappDhcpMIBNotifObjects':ciscoLwappDhcpMIBNotifObjects,_q:cLDhcpTrapSet,'ciscoLwappDhcpMIBConform':ciscoLwappDhcpMIBConform,'ciscoLwappDhcpMIBCompliances':ciscoLwappDhcpMIBCompliances,'ciscoLwappDhcpMIBCompliance':ciscoLwappDhcpMIBCompliance,'ciscoLwappDhcpMIBGroups':ciscoLwappDhcpMIBGroups,_r:ciscoLwappDhcpMIBConfigGroup})