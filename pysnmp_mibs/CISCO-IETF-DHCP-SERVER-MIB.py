_Ae='cDhcpv4ServerNotificationsGroup'
_Ad='cDhcpv4ServerNotifyObjectsGroup'
_Ac='cDhcpv4ServerClientObjects'
_Ab='cDhcpv4ServerRangeObjects'
_Aa='cDhcpv4ServerSubnetObjects'
_AZ='cDhcpv4ServerSharedNetObjects'
_AY='cDhcpv4ServerDuplicateAddress'
_AX='cDhcpv4ServerStopTime'
_AW='cDhcpv4ServerStartTime'
_AV='cDhcpv4ServerFreeAddressHigh'
_AU='cDhcpv4ServerFreeAddressLow'
_AT='cDhcpv4ServerClientDomainName'
_AS='cDhcpv4ServerClientHostName'
_AR='cDhcpv4ServerClientClientId'
_AQ='cDhcpv4ServerClientPhysicalAddress'
_AP='cDhcpv4ServerClientServedProtocol'
_AO='cDhcpv4ServerClientAllowedProtocol'
_AN='cDhcpv4ServerClientTimeRemaining'
_AM='cDhcpv4ServerClientLeaseType'
_AL='cDhcpv4ServerClientRange'
_AK='cDhcpv4ServerClientSubnetMask'
_AJ='cDhcpv4ServerRangeOutstandingOffers'
_AI='cDhcpv4ServerRangeInUse'
_AH='cDhcpv4ServerRangeSubnetMask'
_AG='cDhcpv4ServerSubnetFreeAddresses'
_AF='cDhcpv4ServerSubnetFreeAddrHighThreshold'
_AE='cDhcpv4ServerSubnetFreeAddrLowThreshold'
_AD='cDhcpv4ServerSubnetSharedNetworkName'
_AC='cDhcpv4ServerSubnetMask'
_AB='cDhcpv4ServerSharedNetTotalAddresses'
_AA='cDhcpv4ServerSharedNetReservedAddresses'
_A9='cDhcpv4HCCountDropNotServingSubnet'
_A8='cDhcpv4HCCountDropUnknownClient'
_A7='cDhcpv4HCCountInvalids'
_A6='cDhcpv4HCCountForcedRenews'
_A5='cDhcpv4HCCountInforms'
_A4='cDhcpv4HCCountReleases'
_A3='cDhcpv4HCCountNaks'
_A2='cDhcpv4HCCountAcks'
_A1='cDhcpv4HCCountDeclines'
_A0='cDhcpv4HCCountRequests'
_z='cDhcpv4HCCountOffers'
_y='cDhcpv4HCCountDiscovers'
_x='cBootpHCCountDropNotServingSubnet'
_w='cBootpHCCountDropUnknownClients'
_v='cBootpHCCountReplies'
_u='cBootpHCCountInvalids'
_t='cBootpHCCountRequests'
_s='cDhcpv4CountDropNotServingSubnet'
_r='cDhcpv4CountDropUnknownClient'
_q='cDhcpv4CountInvalids'
_p='cDhcpv4CountInforms'
_o='cDhcpv4CountReleases'
_n='cDhcpv4CountNaks'
_m='cDhcpv4CountAcks'
_l='cDhcpv4CountDeclines'
_k='cDhcpv4CountRequests'
_j='cDhcpv4CountOffers'
_i='cDhcpv4CountDiscovers'
_h='cBootpCountDropNotServingSubnet'
_g='cBootpCountDropUnknownClients'
_f='cBootpCountReplies'
_e='cBootpCountInvalids'
_d='cBootpCountRequests'
_c='cDhcpv4SrvSystemObjectID'
_b='cDhcpv4SrvSystemDescr'
_a='cDhcpv4ServerClient'
_Z='cDhcpv4ServerRangeEndAddress'
_Y='cDhcpv4ServerRangeStartAddress'
_X='cDhcpv4ServerSubnetAddress'
_W='cDhcpv4ServerSharedNetName'
_V='OctetString'
_U='cDhcpv4HCCounterObjects'
_T='cBootpHCCountersGroup'
_S='cDhcpv4CounterObjects'
_R='cBootpCountersGroup'
_Q='cDhcpv4SrvSystemObjects'
_P='cDhcpv4ServerNotifyServerStop'
_O='cDhcpv4ServerNotifyServerStart'
_N='cDhcpv4ServerNotifyClientOrServerDetected'
_M='cDhcpv4ServerNotifyDuplicateMac'
_L='cDhcpv4ServerNotifyDuplicateIpAddr'
_K='cDhcpv4ServerSharedNetFreeAddrHighThreshold'
_J='cDhcpv4ServerSharedNetFreeAddrLowThreshold'
_I='cDhcpv4ServerSharedNetFreeAddresses'
_H='read-write'
_G='accessible-for-notify'
_F='not-accessible'
_E='Integer32'
_D='SnmpAdminString'
_C='read-only'
_B='CISCO-IETF-DHCP-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InetAddressIPv4,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressPrefixLength')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ciscoIetfDhcpSrvMIB=ModuleIdentity((1,3,6,1,4,1,9,10,102))
if mibBuilder.loadTexts:ciscoIetfDhcpSrvMIB.setRevisions(('2007-03-27 00:00','2007-02-14 12:00','2004-03-01 12:00'))
class CDhcpv4PhysicalAddress(TextualConvention,OctetString):status=_A;displayHint='1d,1d,1x:1x:1x:1x:1x:1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(18,18));fixedLength=18
_CiscoIetfDhcpv4SrvMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIetfDhcpv4SrvMIBNotifs=_CiscoIetfDhcpv4SrvMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,102,0))
_CDhcpv4ServerNotificationPrefix_ObjectIdentity=ObjectIdentity
cDhcpv4ServerNotificationPrefix=_CDhcpv4ServerNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,102,0,2))
_CDhcpv4ServerNotifications_ObjectIdentity=ObjectIdentity
cDhcpv4ServerNotifications=_CDhcpv4ServerNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,102,0,2,0))
_CiscoIetfDhcpv4SrvMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfDhcpv4SrvMIBObjects=_CiscoIetfDhcpv4SrvMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,102,1))
_CDhcpv4SrvSystem_ObjectIdentity=ObjectIdentity
cDhcpv4SrvSystem=_CDhcpv4SrvSystem_ObjectIdentity((1,3,6,1,4,1,9,10,102,1,1))
if mibBuilder.loadTexts:cDhcpv4SrvSystem.setStatus(_A)
class _CDhcpv4SrvSystemDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CDhcpv4SrvSystemDescr_Type.__name__=_D
_CDhcpv4SrvSystemDescr_Object=MibScalar
cDhcpv4SrvSystemDescr=_CDhcpv4SrvSystemDescr_Object((1,3,6,1,4,1,9,10,102,1,1,1),_CDhcpv4SrvSystemDescr_Type())
cDhcpv4SrvSystemDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4SrvSystemDescr.setStatus(_A)
_CDhcpv4SrvSystemObjectID_Type=ObjectIdentifier
_CDhcpv4SrvSystemObjectID_Object=MibScalar
cDhcpv4SrvSystemObjectID=_CDhcpv4SrvSystemObjectID_Object((1,3,6,1,4,1,9,10,102,1,1,2),_CDhcpv4SrvSystemObjectID_Type())
cDhcpv4SrvSystemObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4SrvSystemObjectID.setStatus(_A)
_CBootpCounters_ObjectIdentity=ObjectIdentity
cBootpCounters=_CBootpCounters_ObjectIdentity((1,3,6,1,4,1,9,10,102,1,2))
if mibBuilder.loadTexts:cBootpCounters.setStatus(_A)
_CBootpCountRequests_Type=Counter32
_CBootpCountRequests_Object=MibScalar
cBootpCountRequests=_CBootpCountRequests_Object((1,3,6,1,4,1,9,10,102,1,2,1),_CBootpCountRequests_Type())
cBootpCountRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpCountRequests.setStatus(_A)
_CBootpCountInvalids_Type=Counter32
_CBootpCountInvalids_Object=MibScalar
cBootpCountInvalids=_CBootpCountInvalids_Object((1,3,6,1,4,1,9,10,102,1,2,2),_CBootpCountInvalids_Type())
cBootpCountInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpCountInvalids.setStatus(_A)
_CBootpCountReplies_Type=Counter32
_CBootpCountReplies_Object=MibScalar
cBootpCountReplies=_CBootpCountReplies_Object((1,3,6,1,4,1,9,10,102,1,2,3),_CBootpCountReplies_Type())
cBootpCountReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpCountReplies.setStatus(_A)
_CBootpCountDropUnknownClients_Type=Counter32
_CBootpCountDropUnknownClients_Object=MibScalar
cBootpCountDropUnknownClients=_CBootpCountDropUnknownClients_Object((1,3,6,1,4,1,9,10,102,1,2,4),_CBootpCountDropUnknownClients_Type())
cBootpCountDropUnknownClients.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpCountDropUnknownClients.setStatus(_A)
_CBootpCountDropNotServingSubnet_Type=Counter32
_CBootpCountDropNotServingSubnet_Object=MibScalar
cBootpCountDropNotServingSubnet=_CBootpCountDropNotServingSubnet_Object((1,3,6,1,4,1,9,10,102,1,2,5),_CBootpCountDropNotServingSubnet_Type())
cBootpCountDropNotServingSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpCountDropNotServingSubnet.setStatus(_A)
_CDhcpv4Counters_ObjectIdentity=ObjectIdentity
cDhcpv4Counters=_CDhcpv4Counters_ObjectIdentity((1,3,6,1,4,1,9,10,102,1,3))
if mibBuilder.loadTexts:cDhcpv4Counters.setStatus(_A)
_CDhcpv4CountDiscovers_Type=Counter32
_CDhcpv4CountDiscovers_Object=MibScalar
cDhcpv4CountDiscovers=_CDhcpv4CountDiscovers_Object((1,3,6,1,4,1,9,10,102,1,3,1),_CDhcpv4CountDiscovers_Type())
cDhcpv4CountDiscovers.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountDiscovers.setStatus(_A)
_CDhcpv4CountOffers_Type=Counter32
_CDhcpv4CountOffers_Object=MibScalar
cDhcpv4CountOffers=_CDhcpv4CountOffers_Object((1,3,6,1,4,1,9,10,102,1,3,2),_CDhcpv4CountOffers_Type())
cDhcpv4CountOffers.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountOffers.setStatus(_A)
_CDhcpv4CountRequests_Type=Counter32
_CDhcpv4CountRequests_Object=MibScalar
cDhcpv4CountRequests=_CDhcpv4CountRequests_Object((1,3,6,1,4,1,9,10,102,1,3,3),_CDhcpv4CountRequests_Type())
cDhcpv4CountRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountRequests.setStatus(_A)
_CDhcpv4CountDeclines_Type=Counter32
_CDhcpv4CountDeclines_Object=MibScalar
cDhcpv4CountDeclines=_CDhcpv4CountDeclines_Object((1,3,6,1,4,1,9,10,102,1,3,4),_CDhcpv4CountDeclines_Type())
cDhcpv4CountDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountDeclines.setStatus(_A)
_CDhcpv4CountAcks_Type=Counter32
_CDhcpv4CountAcks_Object=MibScalar
cDhcpv4CountAcks=_CDhcpv4CountAcks_Object((1,3,6,1,4,1,9,10,102,1,3,5),_CDhcpv4CountAcks_Type())
cDhcpv4CountAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountAcks.setStatus(_A)
_CDhcpv4CountNaks_Type=Counter32
_CDhcpv4CountNaks_Object=MibScalar
cDhcpv4CountNaks=_CDhcpv4CountNaks_Object((1,3,6,1,4,1,9,10,102,1,3,6),_CDhcpv4CountNaks_Type())
cDhcpv4CountNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountNaks.setStatus(_A)
_CDhcpv4CountReleases_Type=Counter32
_CDhcpv4CountReleases_Object=MibScalar
cDhcpv4CountReleases=_CDhcpv4CountReleases_Object((1,3,6,1,4,1,9,10,102,1,3,7),_CDhcpv4CountReleases_Type())
cDhcpv4CountReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountReleases.setStatus(_A)
_CDhcpv4CountInforms_Type=Counter32
_CDhcpv4CountInforms_Object=MibScalar
cDhcpv4CountInforms=_CDhcpv4CountInforms_Object((1,3,6,1,4,1,9,10,102,1,3,8),_CDhcpv4CountInforms_Type())
cDhcpv4CountInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountInforms.setStatus(_A)
_CDhcpv4CountInvalids_Type=Counter32
_CDhcpv4CountInvalids_Object=MibScalar
cDhcpv4CountInvalids=_CDhcpv4CountInvalids_Object((1,3,6,1,4,1,9,10,102,1,3,10),_CDhcpv4CountInvalids_Type())
cDhcpv4CountInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountInvalids.setStatus(_A)
_CDhcpv4CountDropUnknownClient_Type=Counter32
_CDhcpv4CountDropUnknownClient_Object=MibScalar
cDhcpv4CountDropUnknownClient=_CDhcpv4CountDropUnknownClient_Object((1,3,6,1,4,1,9,10,102,1,3,11),_CDhcpv4CountDropUnknownClient_Type())
cDhcpv4CountDropUnknownClient.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountDropUnknownClient.setStatus(_A)
_CDhcpv4CountDropNotServingSubnet_Type=Counter32
_CDhcpv4CountDropNotServingSubnet_Object=MibScalar
cDhcpv4CountDropNotServingSubnet=_CDhcpv4CountDropNotServingSubnet_Object((1,3,6,1,4,1,9,10,102,1,3,12),_CDhcpv4CountDropNotServingSubnet_Type())
cDhcpv4CountDropNotServingSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4CountDropNotServingSubnet.setStatus(_A)
_CDhcpv4SrvConfiguration_ObjectIdentity=ObjectIdentity
cDhcpv4SrvConfiguration=_CDhcpv4SrvConfiguration_ObjectIdentity((1,3,6,1,4,1,9,10,102,1,4))
if mibBuilder.loadTexts:cDhcpv4SrvConfiguration.setStatus(_A)
_CDhcpv4ServerSharedNetTable_Object=MibTable
cDhcpv4ServerSharedNetTable=_CDhcpv4ServerSharedNetTable_Object((1,3,6,1,4,1,9,10,102,1,4,1))
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetTable.setStatus(_A)
_CDhcpv4ServerSharedNetEntry_Object=MibTableRow
cDhcpv4ServerSharedNetEntry=_CDhcpv4ServerSharedNetEntry_Object((1,3,6,1,4,1,9,10,102,1,4,1,1))
cDhcpv4ServerSharedNetEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetEntry.setStatus(_A)
class _CDhcpv4ServerSharedNetName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CDhcpv4ServerSharedNetName_Type.__name__=_D
_CDhcpv4ServerSharedNetName_Object=MibTableColumn
cDhcpv4ServerSharedNetName=_CDhcpv4ServerSharedNetName_Object((1,3,6,1,4,1,9,10,102,1,4,1,1,1),_CDhcpv4ServerSharedNetName_Type())
cDhcpv4ServerSharedNetName.setMaxAccess(_F)
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetName.setStatus(_A)
_CDhcpv4ServerSharedNetFreeAddrLowThreshold_Type=Unsigned32
_CDhcpv4ServerSharedNetFreeAddrLowThreshold_Object=MibTableColumn
cDhcpv4ServerSharedNetFreeAddrLowThreshold=_CDhcpv4ServerSharedNetFreeAddrLowThreshold_Object((1,3,6,1,4,1,9,10,102,1,4,1,1,2),_CDhcpv4ServerSharedNetFreeAddrLowThreshold_Type())
cDhcpv4ServerSharedNetFreeAddrLowThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetFreeAddrLowThreshold.setStatus(_A)
_CDhcpv4ServerSharedNetFreeAddrHighThreshold_Type=Unsigned32
_CDhcpv4ServerSharedNetFreeAddrHighThreshold_Object=MibTableColumn
cDhcpv4ServerSharedNetFreeAddrHighThreshold=_CDhcpv4ServerSharedNetFreeAddrHighThreshold_Object((1,3,6,1,4,1,9,10,102,1,4,1,1,3),_CDhcpv4ServerSharedNetFreeAddrHighThreshold_Type())
cDhcpv4ServerSharedNetFreeAddrHighThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetFreeAddrHighThreshold.setStatus(_A)
_CDhcpv4ServerSharedNetFreeAddresses_Type=Unsigned32
_CDhcpv4ServerSharedNetFreeAddresses_Object=MibTableColumn
cDhcpv4ServerSharedNetFreeAddresses=_CDhcpv4ServerSharedNetFreeAddresses_Object((1,3,6,1,4,1,9,10,102,1,4,1,1,4),_CDhcpv4ServerSharedNetFreeAddresses_Type())
cDhcpv4ServerSharedNetFreeAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetFreeAddresses.setStatus(_A)
_CDhcpv4ServerSharedNetReservedAddresses_Type=Unsigned32
_CDhcpv4ServerSharedNetReservedAddresses_Object=MibTableColumn
cDhcpv4ServerSharedNetReservedAddresses=_CDhcpv4ServerSharedNetReservedAddresses_Object((1,3,6,1,4,1,9,10,102,1,4,1,1,5),_CDhcpv4ServerSharedNetReservedAddresses_Type())
cDhcpv4ServerSharedNetReservedAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetReservedAddresses.setStatus(_A)
_CDhcpv4ServerSharedNetTotalAddresses_Type=Unsigned32
_CDhcpv4ServerSharedNetTotalAddresses_Object=MibTableColumn
cDhcpv4ServerSharedNetTotalAddresses=_CDhcpv4ServerSharedNetTotalAddresses_Object((1,3,6,1,4,1,9,10,102,1,4,1,1,6),_CDhcpv4ServerSharedNetTotalAddresses_Type())
cDhcpv4ServerSharedNetTotalAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetTotalAddresses.setStatus(_A)
_CDhcpv4ServerSubnetTable_Object=MibTable
cDhcpv4ServerSubnetTable=_CDhcpv4ServerSubnetTable_Object((1,3,6,1,4,1,9,10,102,1,4,2))
if mibBuilder.loadTexts:cDhcpv4ServerSubnetTable.setStatus(_A)
_CDhcpv4ServerSubnetEntry_Object=MibTableRow
cDhcpv4ServerSubnetEntry=_CDhcpv4ServerSubnetEntry_Object((1,3,6,1,4,1,9,10,102,1,4,2,1))
cDhcpv4ServerSubnetEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:cDhcpv4ServerSubnetEntry.setStatus(_A)
_CDhcpv4ServerSubnetAddress_Type=InetAddressIPv4
_CDhcpv4ServerSubnetAddress_Object=MibTableColumn
cDhcpv4ServerSubnetAddress=_CDhcpv4ServerSubnetAddress_Object((1,3,6,1,4,1,9,10,102,1,4,2,1,1),_CDhcpv4ServerSubnetAddress_Type())
cDhcpv4ServerSubnetAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetAddress.setStatus(_A)
_CDhcpv4ServerSubnetMask_Type=InetAddressPrefixLength
_CDhcpv4ServerSubnetMask_Object=MibTableColumn
cDhcpv4ServerSubnetMask=_CDhcpv4ServerSubnetMask_Object((1,3,6,1,4,1,9,10,102,1,4,2,1,2),_CDhcpv4ServerSubnetMask_Type())
cDhcpv4ServerSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetMask.setStatus(_A)
class _CDhcpv4ServerSubnetSharedNetworkName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CDhcpv4ServerSubnetSharedNetworkName_Type.__name__=_D
_CDhcpv4ServerSubnetSharedNetworkName_Object=MibTableColumn
cDhcpv4ServerSubnetSharedNetworkName=_CDhcpv4ServerSubnetSharedNetworkName_Object((1,3,6,1,4,1,9,10,102,1,4,2,1,3),_CDhcpv4ServerSubnetSharedNetworkName_Type())
cDhcpv4ServerSubnetSharedNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetSharedNetworkName.setStatus(_A)
_CDhcpv4ServerSubnetFreeAddrLowThreshold_Type=Unsigned32
_CDhcpv4ServerSubnetFreeAddrLowThreshold_Object=MibTableColumn
cDhcpv4ServerSubnetFreeAddrLowThreshold=_CDhcpv4ServerSubnetFreeAddrLowThreshold_Object((1,3,6,1,4,1,9,10,102,1,4,2,1,4),_CDhcpv4ServerSubnetFreeAddrLowThreshold_Type())
cDhcpv4ServerSubnetFreeAddrLowThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetFreeAddrLowThreshold.setStatus(_A)
_CDhcpv4ServerSubnetFreeAddrHighThreshold_Type=Unsigned32
_CDhcpv4ServerSubnetFreeAddrHighThreshold_Object=MibTableColumn
cDhcpv4ServerSubnetFreeAddrHighThreshold=_CDhcpv4ServerSubnetFreeAddrHighThreshold_Object((1,3,6,1,4,1,9,10,102,1,4,2,1,5),_CDhcpv4ServerSubnetFreeAddrHighThreshold_Type())
cDhcpv4ServerSubnetFreeAddrHighThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetFreeAddrHighThreshold.setStatus(_A)
_CDhcpv4ServerSubnetFreeAddresses_Type=Unsigned32
_CDhcpv4ServerSubnetFreeAddresses_Object=MibTableColumn
cDhcpv4ServerSubnetFreeAddresses=_CDhcpv4ServerSubnetFreeAddresses_Object((1,3,6,1,4,1,9,10,102,1,4,2,1,6),_CDhcpv4ServerSubnetFreeAddresses_Type())
cDhcpv4ServerSubnetFreeAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetFreeAddresses.setStatus(_A)
_CDhcpv4ServerRangeTable_Object=MibTable
cDhcpv4ServerRangeTable=_CDhcpv4ServerRangeTable_Object((1,3,6,1,4,1,9,10,102,1,4,3))
if mibBuilder.loadTexts:cDhcpv4ServerRangeTable.setStatus(_A)
_CDhcpv4ServerRangeEntry_Object=MibTableRow
cDhcpv4ServerRangeEntry=_CDhcpv4ServerRangeEntry_Object((1,3,6,1,4,1,9,10,102,1,4,3,1))
cDhcpv4ServerRangeEntry.setIndexNames((0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:cDhcpv4ServerRangeEntry.setStatus(_A)
_CDhcpv4ServerRangeStartAddress_Type=InetAddressIPv4
_CDhcpv4ServerRangeStartAddress_Object=MibTableColumn
cDhcpv4ServerRangeStartAddress=_CDhcpv4ServerRangeStartAddress_Object((1,3,6,1,4,1,9,10,102,1,4,3,1,1),_CDhcpv4ServerRangeStartAddress_Type())
cDhcpv4ServerRangeStartAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cDhcpv4ServerRangeStartAddress.setStatus(_A)
_CDhcpv4ServerRangeEndAddress_Type=InetAddressIPv4
_CDhcpv4ServerRangeEndAddress_Object=MibTableColumn
cDhcpv4ServerRangeEndAddress=_CDhcpv4ServerRangeEndAddress_Object((1,3,6,1,4,1,9,10,102,1,4,3,1,2),_CDhcpv4ServerRangeEndAddress_Type())
cDhcpv4ServerRangeEndAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cDhcpv4ServerRangeEndAddress.setStatus(_A)
_CDhcpv4ServerRangeSubnetMask_Type=InetAddressPrefixLength
_CDhcpv4ServerRangeSubnetMask_Object=MibTableColumn
cDhcpv4ServerRangeSubnetMask=_CDhcpv4ServerRangeSubnetMask_Object((1,3,6,1,4,1,9,10,102,1,4,3,1,3),_CDhcpv4ServerRangeSubnetMask_Type())
cDhcpv4ServerRangeSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerRangeSubnetMask.setStatus(_A)
_CDhcpv4ServerRangeInUse_Type=Gauge32
_CDhcpv4ServerRangeInUse_Object=MibTableColumn
cDhcpv4ServerRangeInUse=_CDhcpv4ServerRangeInUse_Object((1,3,6,1,4,1,9,10,102,1,4,3,1,4),_CDhcpv4ServerRangeInUse_Type())
cDhcpv4ServerRangeInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerRangeInUse.setStatus(_A)
_CDhcpv4ServerRangeOutstandingOffers_Type=Gauge32
_CDhcpv4ServerRangeOutstandingOffers_Object=MibTableColumn
cDhcpv4ServerRangeOutstandingOffers=_CDhcpv4ServerRangeOutstandingOffers_Object((1,3,6,1,4,1,9,10,102,1,4,3,1,5),_CDhcpv4ServerRangeOutstandingOffers_Type())
cDhcpv4ServerRangeOutstandingOffers.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerRangeOutstandingOffers.setStatus(_A)
_CDhcpv4ServerClientTable_Object=MibTable
cDhcpv4ServerClientTable=_CDhcpv4ServerClientTable_Object((1,3,6,1,4,1,9,10,102,1,4,4))
if mibBuilder.loadTexts:cDhcpv4ServerClientTable.setStatus(_A)
_CDhcpv4ServerClientEntry_Object=MibTableRow
cDhcpv4ServerClientEntry=_CDhcpv4ServerClientEntry_Object((1,3,6,1,4,1,9,10,102,1,4,4,1))
cDhcpv4ServerClientEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:cDhcpv4ServerClientEntry.setStatus(_A)
_CDhcpv4ServerClient_Type=InetAddressIPv4
_CDhcpv4ServerClient_Object=MibTableColumn
cDhcpv4ServerClient=_CDhcpv4ServerClient_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,1),_CDhcpv4ServerClient_Type())
cDhcpv4ServerClient.setMaxAccess(_F)
if mibBuilder.loadTexts:cDhcpv4ServerClient.setStatus(_A)
_CDhcpv4ServerClientSubnetMask_Type=InetAddressPrefixLength
_CDhcpv4ServerClientSubnetMask_Object=MibTableColumn
cDhcpv4ServerClientSubnetMask=_CDhcpv4ServerClientSubnetMask_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,2),_CDhcpv4ServerClientSubnetMask_Type())
cDhcpv4ServerClientSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientSubnetMask.setStatus(_A)
_CDhcpv4ServerClientRange_Type=InetAddressIPv4
_CDhcpv4ServerClientRange_Object=MibTableColumn
cDhcpv4ServerClientRange=_CDhcpv4ServerClientRange_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,3),_CDhcpv4ServerClientRange_Type())
cDhcpv4ServerClientRange.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientRange.setStatus(_A)
class _CDhcpv4ServerClientLeaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('dynamic',2),('expired',3),('configurationReserved',4),('serverReserved',5)))
_CDhcpv4ServerClientLeaseType_Type.__name__=_E
_CDhcpv4ServerClientLeaseType_Object=MibTableColumn
cDhcpv4ServerClientLeaseType=_CDhcpv4ServerClientLeaseType_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,4),_CDhcpv4ServerClientLeaseType_Type())
cDhcpv4ServerClientLeaseType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientLeaseType.setStatus(_A)
_CDhcpv4ServerClientTimeRemaining_Type=Unsigned32
_CDhcpv4ServerClientTimeRemaining_Object=MibTableColumn
cDhcpv4ServerClientTimeRemaining=_CDhcpv4ServerClientTimeRemaining_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,5),_CDhcpv4ServerClientTimeRemaining_Type())
cDhcpv4ServerClientTimeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientTimeRemaining.setStatus(_A)
class _CDhcpv4ServerClientAllowedProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('bootp',2),('dhcp',3),('bootpOrDhcp',4)))
_CDhcpv4ServerClientAllowedProtocol_Type.__name__=_E
_CDhcpv4ServerClientAllowedProtocol_Object=MibTableColumn
cDhcpv4ServerClientAllowedProtocol=_CDhcpv4ServerClientAllowedProtocol_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,6),_CDhcpv4ServerClientAllowedProtocol_Type())
cDhcpv4ServerClientAllowedProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientAllowedProtocol.setStatus(_A)
class _CDhcpv4ServerClientServedProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('bootp',2),('dhcp',3)))
_CDhcpv4ServerClientServedProtocol_Type.__name__=_E
_CDhcpv4ServerClientServedProtocol_Object=MibTableColumn
cDhcpv4ServerClientServedProtocol=_CDhcpv4ServerClientServedProtocol_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,7),_CDhcpv4ServerClientServedProtocol_Type())
cDhcpv4ServerClientServedProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientServedProtocol.setStatus(_A)
_CDhcpv4ServerClientPhysicalAddress_Type=CDhcpv4PhysicalAddress
_CDhcpv4ServerClientPhysicalAddress_Object=MibTableColumn
cDhcpv4ServerClientPhysicalAddress=_CDhcpv4ServerClientPhysicalAddress_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,8),_CDhcpv4ServerClientPhysicalAddress_Type())
cDhcpv4ServerClientPhysicalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientPhysicalAddress.setStatus(_A)
class _CDhcpv4ServerClientClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CDhcpv4ServerClientClientId_Type.__name__=_V
_CDhcpv4ServerClientClientId_Object=MibTableColumn
cDhcpv4ServerClientClientId=_CDhcpv4ServerClientClientId_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,9),_CDhcpv4ServerClientClientId_Type())
cDhcpv4ServerClientClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientClientId.setStatus(_A)
class _CDhcpv4ServerClientHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CDhcpv4ServerClientHostName_Type.__name__=_D
_CDhcpv4ServerClientHostName_Object=MibTableColumn
cDhcpv4ServerClientHostName=_CDhcpv4ServerClientHostName_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,10),_CDhcpv4ServerClientHostName_Type())
cDhcpv4ServerClientHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientHostName.setStatus(_A)
class _CDhcpv4ServerClientDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CDhcpv4ServerClientDomainName_Type.__name__=_D
_CDhcpv4ServerClientDomainName_Object=MibTableColumn
cDhcpv4ServerClientDomainName=_CDhcpv4ServerClientDomainName_Object((1,3,6,1,4,1,9,10,102,1,4,4,1,11),_CDhcpv4ServerClientDomainName_Type())
cDhcpv4ServerClientDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerClientDomainName.setStatus(_A)
_CDhcpv4ServerNotifyObjects_ObjectIdentity=ObjectIdentity
cDhcpv4ServerNotifyObjects=_CDhcpv4ServerNotifyObjects_ObjectIdentity((1,3,6,1,4,1,9,10,102,1,7))
if mibBuilder.loadTexts:cDhcpv4ServerNotifyObjects.setStatus(_A)
_CDhcpv4ServerNotifyDuplicateIpAddr_Type=InetAddressIPv4
_CDhcpv4ServerNotifyDuplicateIpAddr_Object=MibScalar
cDhcpv4ServerNotifyDuplicateIpAddr=_CDhcpv4ServerNotifyDuplicateIpAddr_Object((1,3,6,1,4,1,9,10,102,1,7,1),_CDhcpv4ServerNotifyDuplicateIpAddr_Type())
cDhcpv4ServerNotifyDuplicateIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:cDhcpv4ServerNotifyDuplicateIpAddr.setStatus(_A)
_CDhcpv4ServerNotifyDuplicateMac_Type=CDhcpv4PhysicalAddress
_CDhcpv4ServerNotifyDuplicateMac_Object=MibScalar
cDhcpv4ServerNotifyDuplicateMac=_CDhcpv4ServerNotifyDuplicateMac_Object((1,3,6,1,4,1,9,10,102,1,7,2),_CDhcpv4ServerNotifyDuplicateMac_Type())
cDhcpv4ServerNotifyDuplicateMac.setMaxAccess(_G)
if mibBuilder.loadTexts:cDhcpv4ServerNotifyDuplicateMac.setStatus(_A)
class _CDhcpv4ServerNotifyClientOrServerDetected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('client',1),('server',2)))
_CDhcpv4ServerNotifyClientOrServerDetected_Type.__name__=_E
_CDhcpv4ServerNotifyClientOrServerDetected_Object=MibScalar
cDhcpv4ServerNotifyClientOrServerDetected=_CDhcpv4ServerNotifyClientOrServerDetected_Object((1,3,6,1,4,1,9,10,102,1,7,3),_CDhcpv4ServerNotifyClientOrServerDetected_Type())
cDhcpv4ServerNotifyClientOrServerDetected.setMaxAccess(_G)
if mibBuilder.loadTexts:cDhcpv4ServerNotifyClientOrServerDetected.setStatus(_A)
_CDhcpv4ServerNotifyServerStart_Type=DateAndTime
_CDhcpv4ServerNotifyServerStart_Object=MibScalar
cDhcpv4ServerNotifyServerStart=_CDhcpv4ServerNotifyServerStart_Object((1,3,6,1,4,1,9,10,102,1,7,4),_CDhcpv4ServerNotifyServerStart_Type())
cDhcpv4ServerNotifyServerStart.setMaxAccess(_G)
if mibBuilder.loadTexts:cDhcpv4ServerNotifyServerStart.setStatus(_A)
_CDhcpv4ServerNotifyServerStop_Type=DateAndTime
_CDhcpv4ServerNotifyServerStop_Object=MibScalar
cDhcpv4ServerNotifyServerStop=_CDhcpv4ServerNotifyServerStop_Object((1,3,6,1,4,1,9,10,102,1,7,5),_CDhcpv4ServerNotifyServerStop_Type())
cDhcpv4ServerNotifyServerStop.setMaxAccess(_G)
if mibBuilder.loadTexts:cDhcpv4ServerNotifyServerStop.setStatus(_A)
_CBootpHCCounters_ObjectIdentity=ObjectIdentity
cBootpHCCounters=_CBootpHCCounters_ObjectIdentity((1,3,6,1,4,1,9,10,102,1,8))
if mibBuilder.loadTexts:cBootpHCCounters.setStatus(_A)
_CBootpHCCountRequests_Type=Counter64
_CBootpHCCountRequests_Object=MibScalar
cBootpHCCountRequests=_CBootpHCCountRequests_Object((1,3,6,1,4,1,9,10,102,1,8,1),_CBootpHCCountRequests_Type())
cBootpHCCountRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpHCCountRequests.setStatus(_A)
_CBootpHCCountInvalids_Type=Counter64
_CBootpHCCountInvalids_Object=MibScalar
cBootpHCCountInvalids=_CBootpHCCountInvalids_Object((1,3,6,1,4,1,9,10,102,1,8,2),_CBootpHCCountInvalids_Type())
cBootpHCCountInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpHCCountInvalids.setStatus(_A)
_CBootpHCCountReplies_Type=Counter64
_CBootpHCCountReplies_Object=MibScalar
cBootpHCCountReplies=_CBootpHCCountReplies_Object((1,3,6,1,4,1,9,10,102,1,8,3),_CBootpHCCountReplies_Type())
cBootpHCCountReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpHCCountReplies.setStatus(_A)
_CBootpHCCountDropUnknownClients_Type=Counter64
_CBootpHCCountDropUnknownClients_Object=MibScalar
cBootpHCCountDropUnknownClients=_CBootpHCCountDropUnknownClients_Object((1,3,6,1,4,1,9,10,102,1,8,4),_CBootpHCCountDropUnknownClients_Type())
cBootpHCCountDropUnknownClients.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpHCCountDropUnknownClients.setStatus(_A)
_CBootpHCCountDropNotServingSubnet_Type=Counter64
_CBootpHCCountDropNotServingSubnet_Object=MibScalar
cBootpHCCountDropNotServingSubnet=_CBootpHCCountDropNotServingSubnet_Object((1,3,6,1,4,1,9,10,102,1,8,5),_CBootpHCCountDropNotServingSubnet_Type())
cBootpHCCountDropNotServingSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:cBootpHCCountDropNotServingSubnet.setStatus(_A)
_CDhcpv4HCCounters_ObjectIdentity=ObjectIdentity
cDhcpv4HCCounters=_CDhcpv4HCCounters_ObjectIdentity((1,3,6,1,4,1,9,10,102,1,9))
if mibBuilder.loadTexts:cDhcpv4HCCounters.setStatus(_A)
_CDhcpv4HCCountDiscovers_Type=Counter64
_CDhcpv4HCCountDiscovers_Object=MibScalar
cDhcpv4HCCountDiscovers=_CDhcpv4HCCountDiscovers_Object((1,3,6,1,4,1,9,10,102,1,9,1),_CDhcpv4HCCountDiscovers_Type())
cDhcpv4HCCountDiscovers.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountDiscovers.setStatus(_A)
_CDhcpv4HCCountOffers_Type=Counter64
_CDhcpv4HCCountOffers_Object=MibScalar
cDhcpv4HCCountOffers=_CDhcpv4HCCountOffers_Object((1,3,6,1,4,1,9,10,102,1,9,2),_CDhcpv4HCCountOffers_Type())
cDhcpv4HCCountOffers.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountOffers.setStatus(_A)
_CDhcpv4HCCountRequests_Type=Counter64
_CDhcpv4HCCountRequests_Object=MibScalar
cDhcpv4HCCountRequests=_CDhcpv4HCCountRequests_Object((1,3,6,1,4,1,9,10,102,1,9,3),_CDhcpv4HCCountRequests_Type())
cDhcpv4HCCountRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountRequests.setStatus(_A)
_CDhcpv4HCCountDeclines_Type=Counter64
_CDhcpv4HCCountDeclines_Object=MibScalar
cDhcpv4HCCountDeclines=_CDhcpv4HCCountDeclines_Object((1,3,6,1,4,1,9,10,102,1,9,4),_CDhcpv4HCCountDeclines_Type())
cDhcpv4HCCountDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountDeclines.setStatus(_A)
_CDhcpv4HCCountAcks_Type=Counter64
_CDhcpv4HCCountAcks_Object=MibScalar
cDhcpv4HCCountAcks=_CDhcpv4HCCountAcks_Object((1,3,6,1,4,1,9,10,102,1,9,5),_CDhcpv4HCCountAcks_Type())
cDhcpv4HCCountAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountAcks.setStatus(_A)
_CDhcpv4HCCountNaks_Type=Counter64
_CDhcpv4HCCountNaks_Object=MibScalar
cDhcpv4HCCountNaks=_CDhcpv4HCCountNaks_Object((1,3,6,1,4,1,9,10,102,1,9,6),_CDhcpv4HCCountNaks_Type())
cDhcpv4HCCountNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountNaks.setStatus(_A)
_CDhcpv4HCCountReleases_Type=Counter64
_CDhcpv4HCCountReleases_Object=MibScalar
cDhcpv4HCCountReleases=_CDhcpv4HCCountReleases_Object((1,3,6,1,4,1,9,10,102,1,9,7),_CDhcpv4HCCountReleases_Type())
cDhcpv4HCCountReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountReleases.setStatus(_A)
_CDhcpv4HCCountInforms_Type=Counter64
_CDhcpv4HCCountInforms_Object=MibScalar
cDhcpv4HCCountInforms=_CDhcpv4HCCountInforms_Object((1,3,6,1,4,1,9,10,102,1,9,8),_CDhcpv4HCCountInforms_Type())
cDhcpv4HCCountInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountInforms.setStatus(_A)
_CDhcpv4HCCountForcedRenews_Type=Counter64
_CDhcpv4HCCountForcedRenews_Object=MibScalar
cDhcpv4HCCountForcedRenews=_CDhcpv4HCCountForcedRenews_Object((1,3,6,1,4,1,9,10,102,1,9,9),_CDhcpv4HCCountForcedRenews_Type())
cDhcpv4HCCountForcedRenews.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountForcedRenews.setStatus(_A)
_CDhcpv4HCCountInvalids_Type=Counter64
_CDhcpv4HCCountInvalids_Object=MibScalar
cDhcpv4HCCountInvalids=_CDhcpv4HCCountInvalids_Object((1,3,6,1,4,1,9,10,102,1,9,10),_CDhcpv4HCCountInvalids_Type())
cDhcpv4HCCountInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountInvalids.setStatus(_A)
_CDhcpv4HCCountDropUnknownClient_Type=Counter64
_CDhcpv4HCCountDropUnknownClient_Object=MibScalar
cDhcpv4HCCountDropUnknownClient=_CDhcpv4HCCountDropUnknownClient_Object((1,3,6,1,4,1,9,10,102,1,9,11),_CDhcpv4HCCountDropUnknownClient_Type())
cDhcpv4HCCountDropUnknownClient.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountDropUnknownClient.setStatus(_A)
_CDhcpv4HCCountDropNotServingSubnet_Type=Counter64
_CDhcpv4HCCountDropNotServingSubnet_Object=MibScalar
cDhcpv4HCCountDropNotServingSubnet=_CDhcpv4HCCountDropNotServingSubnet_Object((1,3,6,1,4,1,9,10,102,1,9,12),_CDhcpv4HCCountDropNotServingSubnet_Type())
cDhcpv4HCCountDropNotServingSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4HCCountDropNotServingSubnet.setStatus(_A)
_CiscoIetfDhcpv4SrvMIBConform_ObjectIdentity=ObjectIdentity
ciscoIetfDhcpv4SrvMIBConform=_CiscoIetfDhcpv4SrvMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,102,2))
_CDhcpv4SrvCompliances_ObjectIdentity=ObjectIdentity
cDhcpv4SrvCompliances=_CDhcpv4SrvCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,102,2,1))
_CDhcpv4SrvGroups_ObjectIdentity=ObjectIdentity
cDhcpv4SrvGroups=_CDhcpv4SrvGroups_ObjectIdentity((1,3,6,1,4,1,9,10,102,2,2))
cDhcpv4SrvSystemObjects=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,1))
cDhcpv4SrvSystemObjects.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cDhcpv4SrvSystemObjects.setStatus(_A)
cBootpCountersGroup=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,2))
cBootpCountersGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:cBootpCountersGroup.setStatus(_A)
cDhcpv4CounterObjects=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,3))
cDhcpv4CounterObjects.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:cDhcpv4CounterObjects.setStatus(_A)
cBootpHCCountersGroup=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,4))
cBootpHCCountersGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:cBootpHCCountersGroup.setStatus(_A)
cDhcpv4HCCounterObjects=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,5))
cDhcpv4HCCounterObjects.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:cDhcpv4HCCounterObjects.setStatus(_A)
cDhcpv4ServerSharedNetObjects=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,6))
cDhcpv4ServerSharedNetObjects.setObjects(*((_B,_J),(_B,_K),(_B,_I),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:cDhcpv4ServerSharedNetObjects.setStatus(_A)
cDhcpv4ServerSubnetObjects=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,7))
cDhcpv4ServerSubnetObjects.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:cDhcpv4ServerSubnetObjects.setStatus(_A)
cDhcpv4ServerRangeObjects=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,8))
cDhcpv4ServerRangeObjects.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cDhcpv4ServerRangeObjects.setStatus(_A)
cDhcpv4ServerClientObjects=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,9))
cDhcpv4ServerClientObjects.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:cDhcpv4ServerClientObjects.setStatus(_A)
cDhcpv4ServerNotifyObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,10,102,2,2,10))
cDhcpv4ServerNotifyObjectsGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cDhcpv4ServerNotifyObjectsGroup.setStatus(_A)
cDhcpv4ServerFreeAddressLow=NotificationType((1,3,6,1,4,1,9,10,102,0,2,0,1))
cDhcpv4ServerFreeAddressLow.setObjects(*((_B,_J),(_B,_I)))
if mibBuilder.loadTexts:cDhcpv4ServerFreeAddressLow.setStatus(_A)
cDhcpv4ServerFreeAddressHigh=NotificationType((1,3,6,1,4,1,9,10,102,0,2,0,2))
cDhcpv4ServerFreeAddressHigh.setObjects(*((_B,_K),(_B,_I)))
if mibBuilder.loadTexts:cDhcpv4ServerFreeAddressHigh.setStatus(_A)
cDhcpv4ServerStartTime=NotificationType((1,3,6,1,4,1,9,10,102,0,2,0,3))
cDhcpv4ServerStartTime.setObjects((_B,_O))
if mibBuilder.loadTexts:cDhcpv4ServerStartTime.setStatus(_A)
cDhcpv4ServerStopTime=NotificationType((1,3,6,1,4,1,9,10,102,0,2,0,4))
cDhcpv4ServerStopTime.setObjects((_B,_P))
if mibBuilder.loadTexts:cDhcpv4ServerStopTime.setStatus(_A)
cDhcpv4ServerDuplicateAddress=NotificationType((1,3,6,1,4,1,9,10,102,0,2,0,5))
cDhcpv4ServerDuplicateAddress.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cDhcpv4ServerDuplicateAddress.setStatus(_A)
cDhcpv4ServerNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,102,2,2,11))
cDhcpv4ServerNotificationsGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:cDhcpv4ServerNotificationsGroup.setStatus(_A)
cDhcpv4SrvCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,102,2,1,1))
cDhcpv4SrvCompliance.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cDhcpv4SrvCompliance.setStatus('deprecated')
cDhcpv4SrvComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,102,2,1,2))
cDhcpv4SrvComplianceRev1.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:cDhcpv4SrvComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CDhcpv4PhysicalAddress':CDhcpv4PhysicalAddress,'ciscoIetfDhcpSrvMIB':ciscoIetfDhcpSrvMIB,'ciscoIetfDhcpv4SrvMIBNotifs':ciscoIetfDhcpv4SrvMIBNotifs,'cDhcpv4ServerNotificationPrefix':cDhcpv4ServerNotificationPrefix,'cDhcpv4ServerNotifications':cDhcpv4ServerNotifications,_AU:cDhcpv4ServerFreeAddressLow,_AV:cDhcpv4ServerFreeAddressHigh,_AW:cDhcpv4ServerStartTime,_AX:cDhcpv4ServerStopTime,_AY:cDhcpv4ServerDuplicateAddress,'ciscoIetfDhcpv4SrvMIBObjects':ciscoIetfDhcpv4SrvMIBObjects,'cDhcpv4SrvSystem':cDhcpv4SrvSystem,_b:cDhcpv4SrvSystemDescr,_c:cDhcpv4SrvSystemObjectID,'cBootpCounters':cBootpCounters,_d:cBootpCountRequests,_e:cBootpCountInvalids,_f:cBootpCountReplies,_g:cBootpCountDropUnknownClients,_h:cBootpCountDropNotServingSubnet,'cDhcpv4Counters':cDhcpv4Counters,_i:cDhcpv4CountDiscovers,_j:cDhcpv4CountOffers,_k:cDhcpv4CountRequests,_l:cDhcpv4CountDeclines,_m:cDhcpv4CountAcks,_n:cDhcpv4CountNaks,_o:cDhcpv4CountReleases,_p:cDhcpv4CountInforms,_q:cDhcpv4CountInvalids,_r:cDhcpv4CountDropUnknownClient,_s:cDhcpv4CountDropNotServingSubnet,'cDhcpv4SrvConfiguration':cDhcpv4SrvConfiguration,'cDhcpv4ServerSharedNetTable':cDhcpv4ServerSharedNetTable,'cDhcpv4ServerSharedNetEntry':cDhcpv4ServerSharedNetEntry,_W:cDhcpv4ServerSharedNetName,_J:cDhcpv4ServerSharedNetFreeAddrLowThreshold,_K:cDhcpv4ServerSharedNetFreeAddrHighThreshold,_I:cDhcpv4ServerSharedNetFreeAddresses,_AA:cDhcpv4ServerSharedNetReservedAddresses,_AB:cDhcpv4ServerSharedNetTotalAddresses,'cDhcpv4ServerSubnetTable':cDhcpv4ServerSubnetTable,'cDhcpv4ServerSubnetEntry':cDhcpv4ServerSubnetEntry,_X:cDhcpv4ServerSubnetAddress,_AC:cDhcpv4ServerSubnetMask,_AD:cDhcpv4ServerSubnetSharedNetworkName,_AE:cDhcpv4ServerSubnetFreeAddrLowThreshold,_AF:cDhcpv4ServerSubnetFreeAddrHighThreshold,_AG:cDhcpv4ServerSubnetFreeAddresses,'cDhcpv4ServerRangeTable':cDhcpv4ServerRangeTable,'cDhcpv4ServerRangeEntry':cDhcpv4ServerRangeEntry,_Y:cDhcpv4ServerRangeStartAddress,_Z:cDhcpv4ServerRangeEndAddress,_AH:cDhcpv4ServerRangeSubnetMask,_AI:cDhcpv4ServerRangeInUse,_AJ:cDhcpv4ServerRangeOutstandingOffers,'cDhcpv4ServerClientTable':cDhcpv4ServerClientTable,'cDhcpv4ServerClientEntry':cDhcpv4ServerClientEntry,_a:cDhcpv4ServerClient,_AK:cDhcpv4ServerClientSubnetMask,_AL:cDhcpv4ServerClientRange,_AM:cDhcpv4ServerClientLeaseType,_AN:cDhcpv4ServerClientTimeRemaining,_AO:cDhcpv4ServerClientAllowedProtocol,_AP:cDhcpv4ServerClientServedProtocol,_AQ:cDhcpv4ServerClientPhysicalAddress,_AR:cDhcpv4ServerClientClientId,_AS:cDhcpv4ServerClientHostName,_AT:cDhcpv4ServerClientDomainName,'cDhcpv4ServerNotifyObjects':cDhcpv4ServerNotifyObjects,_L:cDhcpv4ServerNotifyDuplicateIpAddr,_M:cDhcpv4ServerNotifyDuplicateMac,_N:cDhcpv4ServerNotifyClientOrServerDetected,_O:cDhcpv4ServerNotifyServerStart,_P:cDhcpv4ServerNotifyServerStop,'cBootpHCCounters':cBootpHCCounters,_t:cBootpHCCountRequests,_u:cBootpHCCountInvalids,_v:cBootpHCCountReplies,_w:cBootpHCCountDropUnknownClients,_x:cBootpHCCountDropNotServingSubnet,'cDhcpv4HCCounters':cDhcpv4HCCounters,_y:cDhcpv4HCCountDiscovers,_z:cDhcpv4HCCountOffers,_A0:cDhcpv4HCCountRequests,_A1:cDhcpv4HCCountDeclines,_A2:cDhcpv4HCCountAcks,_A3:cDhcpv4HCCountNaks,_A4:cDhcpv4HCCountReleases,_A5:cDhcpv4HCCountInforms,_A6:cDhcpv4HCCountForcedRenews,_A7:cDhcpv4HCCountInvalids,_A8:cDhcpv4HCCountDropUnknownClient,_A9:cDhcpv4HCCountDropNotServingSubnet,'ciscoIetfDhcpv4SrvMIBConform':ciscoIetfDhcpv4SrvMIBConform,'cDhcpv4SrvCompliances':cDhcpv4SrvCompliances,'cDhcpv4SrvCompliance':cDhcpv4SrvCompliance,'cDhcpv4SrvComplianceRev1':cDhcpv4SrvComplianceRev1,'cDhcpv4SrvGroups':cDhcpv4SrvGroups,_Q:cDhcpv4SrvSystemObjects,_R:cBootpCountersGroup,_S:cDhcpv4CounterObjects,_T:cBootpHCCountersGroup,_U:cDhcpv4HCCounterObjects,_AZ:cDhcpv4ServerSharedNetObjects,_Aa:cDhcpv4ServerSubnetObjects,_Ab:cDhcpv4ServerRangeObjects,_Ac:cDhcpv4ServerClientObjects,_Ad:cDhcpv4ServerNotifyObjectsGroup,_Ae:cDhcpv4ServerNotificationsGroup})