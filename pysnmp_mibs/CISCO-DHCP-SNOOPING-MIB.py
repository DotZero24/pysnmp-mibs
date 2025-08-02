_Ab='cdsVlanOperStatusGroup'
_Aa='cdsIfSrcGuardGroup'
_AZ='cdsBindingsNotification'
_AY='cdsVlanDhcpSnoopingOperStatus'
_AX='cdsIfVlanRelayInfoOptCircuitIdDirect'
_AW='cdsBindingsNotifEnabled'
_AV='cdsForwardedWithoutOption82Pkts'
_AU='cdsIfVlanRelayInfoOptCircuitIdStatus'
_AT='cdsIfVlanRelayInfoOptCircuitId'
_AS='cdsRelayAgentInfoOptRemoteIdSub'
_AR='cdsBindingsHostname'
_AQ='cdsIfSrcGuardFilterType'
_AP='cdsIfSrcGuardVlansHigh'
_AO='cdsIfSrcGuardVlansLow'
_AN='cdsIfSrcGuardMacFilterAction'
_AM='cdsIfSrcGuardMacAddress'
_AL='cdsIfSrcGuardFilterMode'
_AK='cdsIfSrcGuardIpFilterAction'
_AJ='cdsStaticBindingsStatus'
_AI='cdsStaticBindingsInterface'
_AH='cdsStaticBindingsIpAddress'
_AG='cdsStaticBindingsAddrType'
_AF='cdsIfBindingsLimit'
_AE='cdsGlobalMaxBindingsLimit'
_AD='cdsIfFeatureEnable'
_AC='cdsMatchMacAddressEnable'
_AB='cdsRelayAgentInfoOptRemoteId'
_AA='cdsIfSrcGuardEnable'
_A9='cdsRelayAgentInfoOptEnable'
_A8='cdsUntrustedPortDroppedPkts'
_A7='cdsTotalDroppedPkts'
_A6='cdsTotalForwardedPkts'
_A5='cdsBindingsStatus'
_A4='cdsBindingsLeasedTime'
_A3='cdsBindingsInterface'
_A2='cdsIfRateLimit'
_A1='cdsIfTrustEnable'
_A0='cdsVlanDhcpSnoopingEnable'
_z='cdsDatabaseUpdateInterval'
_y='cdsDatabaseFile'
_x='cdsFeatureEnable'
_w='cdsIfSrcGuardIndex'
_v='cdsStaticBindingsMacAddress'
_u='cdsStaticBindingsVlan'
_t='cdsBindingsMacAddress'
_s='cdsBindingsVlan'
_r='cdsIfVlan'
_q='cdsVlanIndex'
_p='seconds'
_o='ifName'
_n='cdsIfVlanRelayInfoOptCircuitIdGroupSup1'
_m='cdsRelayAgentRemoteIdGroup'
_l='cdsIfSrcGuardAddress'
_k='cdsIfSrcGuardAddrType'
_j='cdsBindingsIpAddress'
_i='cdsBindingsAddrType'
_h='cdsBindingsNotificationGroup'
_g='cdsNotifControlGroup'
_f='packets'
_e='cdsStatisticsExtGroup'
_d='cdsIfVlanRelayInfoOptCircuitIdGroup'
_c='cdsRelayAgentInfoOptRemoteIdSubGroup'
_b='OctetString'
_a='cdsBindingsHostnameGroup'
_Z='Integer32'
_Y='cdsIfSrcGuardTrafficFilterGroup'
_X='cdsIfSrcGuardExtGroup'
_W='cdsIfSrcGuardIpFilterGroup'
_V='cdsStaticBindingsGroup'
_U='cdsBindingsLimitGroup'
_T='cdsIfFeatureConfigGroup'
_S='cdsIfSrcGuardGroupRev1'
_R='not-accessible'
_Q='cdsMatchMacAddressGroup'
_P='cdsRelayAgentInfoOptGroup'
_O='cdsStatisticsGroup'
_N='cdsIfRateLimitGroup'
_M='cdsVlanConfigGroup'
_L='cdsDatabaseGroup'
_K='cdsGlobalEnableGroup'
_J='cdsBindingsGroup'
_I='cdsIfConfigGroup'
_H='read-create'
_G='ifIndex'
_F='IF-MIB'
_E='deprecated'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-DHCP-SNOOPING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_b,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex,ifName=mibBuilder.importSymbols(_F,'InterfaceIndex',_G,_o)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Z,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoDhcpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,9,9,380))
if mibBuilder.loadTexts:ciscoDhcpSnoopingMIB.setRevisions(('2009-08-26 00:00','2009-08-10 00:00','2009-04-12 00:00','2007-11-13 00:00','2007-07-12 00:00','2007-05-30 00:00','2006-03-16 16:00','2005-10-26 00:00','2004-03-04 00:00'))
_CiscoDhcpSnoopingMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDhcpSnoopingMIBNotifs=_CiscoDhcpSnoopingMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,380,0))
_CiscoDhcpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDhcpSnoopingMIBObjects=_CiscoDhcpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,380,1))
_CdsGlobal_ObjectIdentity=ObjectIdentity
cdsGlobal=_CdsGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,380,1,1))
_CdsFeatureEnable_Type=TruthValue
_CdsFeatureEnable_Object=MibScalar
cdsFeatureEnable=_CdsFeatureEnable_Object((1,3,6,1,4,1,9,9,380,1,1,1),_CdsFeatureEnable_Type())
cdsFeatureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsFeatureEnable.setStatus(_B)
_CdsDatabaseFile_Type=SnmpAdminString
_CdsDatabaseFile_Object=MibScalar
cdsDatabaseFile=_CdsDatabaseFile_Object((1,3,6,1,4,1,9,9,380,1,1,2),_CdsDatabaseFile_Type())
cdsDatabaseFile.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsDatabaseFile.setStatus(_B)
_CdsDatabaseUpdateInterval_Type=Unsigned32
_CdsDatabaseUpdateInterval_Object=MibScalar
cdsDatabaseUpdateInterval=_CdsDatabaseUpdateInterval_Object((1,3,6,1,4,1,9,9,380,1,1,3),_CdsDatabaseUpdateInterval_Type())
cdsDatabaseUpdateInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsDatabaseUpdateInterval.setStatus(_B)
if mibBuilder.loadTexts:cdsDatabaseUpdateInterval.setUnits(_p)
_CdsRelayAgentInfoOptEnable_Type=TruthValue
_CdsRelayAgentInfoOptEnable_Object=MibScalar
cdsRelayAgentInfoOptEnable=_CdsRelayAgentInfoOptEnable_Object((1,3,6,1,4,1,9,9,380,1,1,4),_CdsRelayAgentInfoOptEnable_Type())
cdsRelayAgentInfoOptEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsRelayAgentInfoOptEnable.setStatus(_B)
_CdsRelayAgentInfoOptRemoteId_Type=MacAddress
_CdsRelayAgentInfoOptRemoteId_Object=MibScalar
cdsRelayAgentInfoOptRemoteId=_CdsRelayAgentInfoOptRemoteId_Object((1,3,6,1,4,1,9,9,380,1,1,5),_CdsRelayAgentInfoOptRemoteId_Type())
cdsRelayAgentInfoOptRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsRelayAgentInfoOptRemoteId.setStatus(_E)
_CdsMatchMacAddressEnable_Type=TruthValue
_CdsMatchMacAddressEnable_Object=MibScalar
cdsMatchMacAddressEnable=_CdsMatchMacAddressEnable_Object((1,3,6,1,4,1,9,9,380,1,1,6),_CdsMatchMacAddressEnable_Type())
cdsMatchMacAddressEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsMatchMacAddressEnable.setStatus(_B)
_CdsGlobalMaxBindingsLimit_Type=Unsigned32
_CdsGlobalMaxBindingsLimit_Object=MibScalar
cdsGlobalMaxBindingsLimit=_CdsGlobalMaxBindingsLimit_Object((1,3,6,1,4,1,9,9,380,1,1,7),_CdsGlobalMaxBindingsLimit_Type())
cdsGlobalMaxBindingsLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsGlobalMaxBindingsLimit.setStatus(_B)
class _CdsRelayAgentInfoOptRemoteIdSub_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CdsRelayAgentInfoOptRemoteIdSub_Type.__name__=_b
_CdsRelayAgentInfoOptRemoteIdSub_Object=MibScalar
cdsRelayAgentInfoOptRemoteIdSub=_CdsRelayAgentInfoOptRemoteIdSub_Object((1,3,6,1,4,1,9,9,380,1,1,8),_CdsRelayAgentInfoOptRemoteIdSub_Type())
cdsRelayAgentInfoOptRemoteIdSub.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsRelayAgentInfoOptRemoteIdSub.setStatus(_B)
_CdsBindingsNotifEnabled_Type=TruthValue
_CdsBindingsNotifEnabled_Object=MibScalar
cdsBindingsNotifEnabled=_CdsBindingsNotifEnabled_Object((1,3,6,1,4,1,9,9,380,1,1,9),_CdsBindingsNotifEnabled_Type())
cdsBindingsNotifEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsBindingsNotifEnabled.setStatus(_B)
_CdsVlan_ObjectIdentity=ObjectIdentity
cdsVlan=_CdsVlan_ObjectIdentity((1,3,6,1,4,1,9,9,380,1,2))
_CdsVlanConfigTable_Object=MibTable
cdsVlanConfigTable=_CdsVlanConfigTable_Object((1,3,6,1,4,1,9,9,380,1,2,1))
if mibBuilder.loadTexts:cdsVlanConfigTable.setStatus(_B)
_CdsVlanConfigEntry_Object=MibTableRow
cdsVlanConfigEntry=_CdsVlanConfigEntry_Object((1,3,6,1,4,1,9,9,380,1,2,1,1))
cdsVlanConfigEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:cdsVlanConfigEntry.setStatus(_B)
_CdsVlanIndex_Type=VlanIndex
_CdsVlanIndex_Object=MibTableColumn
cdsVlanIndex=_CdsVlanIndex_Object((1,3,6,1,4,1,9,9,380,1,2,1,1,1),_CdsVlanIndex_Type())
cdsVlanIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:cdsVlanIndex.setStatus(_B)
_CdsVlanDhcpSnoopingEnable_Type=TruthValue
_CdsVlanDhcpSnoopingEnable_Object=MibTableColumn
cdsVlanDhcpSnoopingEnable=_CdsVlanDhcpSnoopingEnable_Object((1,3,6,1,4,1,9,9,380,1,2,1,1,2),_CdsVlanDhcpSnoopingEnable_Type())
cdsVlanDhcpSnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsVlanDhcpSnoopingEnable.setStatus(_B)
class _CdsVlanDhcpSnoopingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operational',1),('notOperational',2)))
_CdsVlanDhcpSnoopingOperStatus_Type.__name__=_Z
_CdsVlanDhcpSnoopingOperStatus_Object=MibTableColumn
cdsVlanDhcpSnoopingOperStatus=_CdsVlanDhcpSnoopingOperStatus_Object((1,3,6,1,4,1,9,9,380,1,2,1,1,3),_CdsVlanDhcpSnoopingOperStatus_Type())
cdsVlanDhcpSnoopingOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsVlanDhcpSnoopingOperStatus.setStatus(_B)
_CdsInterface_ObjectIdentity=ObjectIdentity
cdsInterface=_CdsInterface_ObjectIdentity((1,3,6,1,4,1,9,9,380,1,3))
_CdsIfConfigTable_Object=MibTable
cdsIfConfigTable=_CdsIfConfigTable_Object((1,3,6,1,4,1,9,9,380,1,3,1))
if mibBuilder.loadTexts:cdsIfConfigTable.setStatus(_B)
_CdsIfConfigEntry_Object=MibTableRow
cdsIfConfigEntry=_CdsIfConfigEntry_Object((1,3,6,1,4,1,9,9,380,1,3,1,1))
cdsIfConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cdsIfConfigEntry.setStatus(_B)
_CdsIfTrustEnable_Type=TruthValue
_CdsIfTrustEnable_Object=MibTableColumn
cdsIfTrustEnable=_CdsIfTrustEnable_Object((1,3,6,1,4,1,9,9,380,1,3,1,1,1),_CdsIfTrustEnable_Type())
cdsIfTrustEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsIfTrustEnable.setStatus(_B)
_CdsIfRateLimitTable_Object=MibTable
cdsIfRateLimitTable=_CdsIfRateLimitTable_Object((1,3,6,1,4,1,9,9,380,1,3,2))
if mibBuilder.loadTexts:cdsIfRateLimitTable.setStatus(_B)
_CdsIfRateLimitEntry_Object=MibTableRow
cdsIfRateLimitEntry=_CdsIfRateLimitEntry_Object((1,3,6,1,4,1,9,9,380,1,3,2,1))
cdsIfRateLimitEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cdsIfRateLimitEntry.setStatus(_B)
_CdsIfRateLimit_Type=Unsigned32
_CdsIfRateLimit_Object=MibTableColumn
cdsIfRateLimit=_CdsIfRateLimit_Object((1,3,6,1,4,1,9,9,380,1,3,2,1,1),_CdsIfRateLimit_Type())
cdsIfRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsIfRateLimit.setStatus(_B)
if mibBuilder.loadTexts:cdsIfRateLimit.setUnits('packets per second')
_CdsIfFeatureConfigTable_Object=MibTable
cdsIfFeatureConfigTable=_CdsIfFeatureConfigTable_Object((1,3,6,1,4,1,9,9,380,1,3,3))
if mibBuilder.loadTexts:cdsIfFeatureConfigTable.setStatus(_B)
_CdsIfFeatureConfigEntry_Object=MibTableRow
cdsIfFeatureConfigEntry=_CdsIfFeatureConfigEntry_Object((1,3,6,1,4,1,9,9,380,1,3,3,1))
cdsIfFeatureConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cdsIfFeatureConfigEntry.setStatus(_B)
_CdsIfFeatureEnable_Type=TruthValue
_CdsIfFeatureEnable_Object=MibTableColumn
cdsIfFeatureEnable=_CdsIfFeatureEnable_Object((1,3,6,1,4,1,9,9,380,1,3,3,1,1),_CdsIfFeatureEnable_Type())
cdsIfFeatureEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsIfFeatureEnable.setStatus(_B)
_CdsIfBindingsLimitTable_Object=MibTable
cdsIfBindingsLimitTable=_CdsIfBindingsLimitTable_Object((1,3,6,1,4,1,9,9,380,1,3,4))
if mibBuilder.loadTexts:cdsIfBindingsLimitTable.setStatus(_B)
_CdsIfBindingsLimitEntry_Object=MibTableRow
cdsIfBindingsLimitEntry=_CdsIfBindingsLimitEntry_Object((1,3,6,1,4,1,9,9,380,1,3,4,1))
cdsIfBindingsLimitEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cdsIfBindingsLimitEntry.setStatus(_B)
_CdsIfBindingsLimit_Type=Unsigned32
_CdsIfBindingsLimit_Object=MibTableColumn
cdsIfBindingsLimit=_CdsIfBindingsLimit_Object((1,3,6,1,4,1,9,9,380,1,3,4,1,1),_CdsIfBindingsLimit_Type())
cdsIfBindingsLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsIfBindingsLimit.setStatus(_B)
_CdsIfVlanRelayInfoOptCircuitIdTable_Object=MibTable
cdsIfVlanRelayInfoOptCircuitIdTable=_CdsIfVlanRelayInfoOptCircuitIdTable_Object((1,3,6,1,4,1,9,9,380,1,3,5))
if mibBuilder.loadTexts:cdsIfVlanRelayInfoOptCircuitIdTable.setStatus(_B)
_CdsIfVlanRelayInfoOptCircuitIdEntry_Object=MibTableRow
cdsIfVlanRelayInfoOptCircuitIdEntry=_CdsIfVlanRelayInfoOptCircuitIdEntry_Object((1,3,6,1,4,1,9,9,380,1,3,5,1))
cdsIfVlanRelayInfoOptCircuitIdEntry.setIndexNames((0,_F,_G),(0,_A,_r))
if mibBuilder.loadTexts:cdsIfVlanRelayInfoOptCircuitIdEntry.setStatus(_B)
_CdsIfVlan_Type=VlanIndex
_CdsIfVlan_Object=MibTableColumn
cdsIfVlan=_CdsIfVlan_Object((1,3,6,1,4,1,9,9,380,1,3,5,1,1),_CdsIfVlan_Type())
cdsIfVlan.setMaxAccess(_R)
if mibBuilder.loadTexts:cdsIfVlan.setStatus(_B)
class _CdsIfVlanRelayInfoOptCircuitId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CdsIfVlanRelayInfoOptCircuitId_Type.__name__=_b
_CdsIfVlanRelayInfoOptCircuitId_Object=MibTableColumn
cdsIfVlanRelayInfoOptCircuitId=_CdsIfVlanRelayInfoOptCircuitId_Object((1,3,6,1,4,1,9,9,380,1,3,5,1,2),_CdsIfVlanRelayInfoOptCircuitId_Type())
cdsIfVlanRelayInfoOptCircuitId.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsIfVlanRelayInfoOptCircuitId.setStatus(_B)
_CdsIfVlanRelayInfoOptCircuitIdStatus_Type=RowStatus
_CdsIfVlanRelayInfoOptCircuitIdStatus_Object=MibTableColumn
cdsIfVlanRelayInfoOptCircuitIdStatus=_CdsIfVlanRelayInfoOptCircuitIdStatus_Object((1,3,6,1,4,1,9,9,380,1,3,5,1,3),_CdsIfVlanRelayInfoOptCircuitIdStatus_Type())
cdsIfVlanRelayInfoOptCircuitIdStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsIfVlanRelayInfoOptCircuitIdStatus.setStatus(_B)
_CdsIfVlanRelayInfoOptCircuitIdDirect_Type=TruthValue
_CdsIfVlanRelayInfoOptCircuitIdDirect_Object=MibTableColumn
cdsIfVlanRelayInfoOptCircuitIdDirect=_CdsIfVlanRelayInfoOptCircuitIdDirect_Object((1,3,6,1,4,1,9,9,380,1,3,5,1,4),_CdsIfVlanRelayInfoOptCircuitIdDirect_Type())
cdsIfVlanRelayInfoOptCircuitIdDirect.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsIfVlanRelayInfoOptCircuitIdDirect.setStatus(_B)
_CdsBindings_ObjectIdentity=ObjectIdentity
cdsBindings=_CdsBindings_ObjectIdentity((1,3,6,1,4,1,9,9,380,1,4))
_CdsBindingsTable_Object=MibTable
cdsBindingsTable=_CdsBindingsTable_Object((1,3,6,1,4,1,9,9,380,1,4,1))
if mibBuilder.loadTexts:cdsBindingsTable.setStatus(_B)
_CdsBindingsEntry_Object=MibTableRow
cdsBindingsEntry=_CdsBindingsEntry_Object((1,3,6,1,4,1,9,9,380,1,4,1,1))
cdsBindingsEntry.setIndexNames((0,_A,_s),(0,_A,_t))
if mibBuilder.loadTexts:cdsBindingsEntry.setStatus(_B)
_CdsBindingsVlan_Type=VlanIndex
_CdsBindingsVlan_Object=MibTableColumn
cdsBindingsVlan=_CdsBindingsVlan_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,1),_CdsBindingsVlan_Type())
cdsBindingsVlan.setMaxAccess(_R)
if mibBuilder.loadTexts:cdsBindingsVlan.setStatus(_B)
_CdsBindingsMacAddress_Type=MacAddress
_CdsBindingsMacAddress_Object=MibTableColumn
cdsBindingsMacAddress=_CdsBindingsMacAddress_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,2),_CdsBindingsMacAddress_Type())
cdsBindingsMacAddress.setMaxAccess(_R)
if mibBuilder.loadTexts:cdsBindingsMacAddress.setStatus(_B)
_CdsBindingsAddrType_Type=InetAddressType
_CdsBindingsAddrType_Object=MibTableColumn
cdsBindingsAddrType=_CdsBindingsAddrType_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,3),_CdsBindingsAddrType_Type())
cdsBindingsAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsBindingsAddrType.setStatus(_B)
_CdsBindingsIpAddress_Type=InetAddress
_CdsBindingsIpAddress_Object=MibTableColumn
cdsBindingsIpAddress=_CdsBindingsIpAddress_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,4),_CdsBindingsIpAddress_Type())
cdsBindingsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsBindingsIpAddress.setStatus(_B)
_CdsBindingsInterface_Type=InterfaceIndex
_CdsBindingsInterface_Object=MibTableColumn
cdsBindingsInterface=_CdsBindingsInterface_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,5),_CdsBindingsInterface_Type())
cdsBindingsInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsBindingsInterface.setStatus(_B)
_CdsBindingsLeasedTime_Type=Unsigned32
_CdsBindingsLeasedTime_Object=MibTableColumn
cdsBindingsLeasedTime=_CdsBindingsLeasedTime_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,6),_CdsBindingsLeasedTime_Type())
cdsBindingsLeasedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsBindingsLeasedTime.setStatus(_B)
if mibBuilder.loadTexts:cdsBindingsLeasedTime.setUnits(_p)
_CdsBindingsStatus_Type=RowStatus
_CdsBindingsStatus_Object=MibTableColumn
cdsBindingsStatus=_CdsBindingsStatus_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,7),_CdsBindingsStatus_Type())
cdsBindingsStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsBindingsStatus.setStatus(_B)
_CdsBindingsHostname_Type=SnmpAdminString
_CdsBindingsHostname_Object=MibTableColumn
cdsBindingsHostname=_CdsBindingsHostname_Object((1,3,6,1,4,1,9,9,380,1,4,1,1,8),_CdsBindingsHostname_Type())
cdsBindingsHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsBindingsHostname.setStatus(_B)
_CdsStaticBindingsTable_Object=MibTable
cdsStaticBindingsTable=_CdsStaticBindingsTable_Object((1,3,6,1,4,1,9,9,380,1,4,2))
if mibBuilder.loadTexts:cdsStaticBindingsTable.setStatus(_B)
_CdsStaticBindingsEntry_Object=MibTableRow
cdsStaticBindingsEntry=_CdsStaticBindingsEntry_Object((1,3,6,1,4,1,9,9,380,1,4,2,1))
cdsStaticBindingsEntry.setIndexNames((0,_A,_u),(0,_A,_v))
if mibBuilder.loadTexts:cdsStaticBindingsEntry.setStatus(_B)
_CdsStaticBindingsVlan_Type=VlanIndex
_CdsStaticBindingsVlan_Object=MibTableColumn
cdsStaticBindingsVlan=_CdsStaticBindingsVlan_Object((1,3,6,1,4,1,9,9,380,1,4,2,1,1),_CdsStaticBindingsVlan_Type())
cdsStaticBindingsVlan.setMaxAccess(_R)
if mibBuilder.loadTexts:cdsStaticBindingsVlan.setStatus(_B)
_CdsStaticBindingsMacAddress_Type=MacAddress
_CdsStaticBindingsMacAddress_Object=MibTableColumn
cdsStaticBindingsMacAddress=_CdsStaticBindingsMacAddress_Object((1,3,6,1,4,1,9,9,380,1,4,2,1,2),_CdsStaticBindingsMacAddress_Type())
cdsStaticBindingsMacAddress.setMaxAccess(_R)
if mibBuilder.loadTexts:cdsStaticBindingsMacAddress.setStatus(_B)
_CdsStaticBindingsAddrType_Type=InetAddressType
_CdsStaticBindingsAddrType_Object=MibTableColumn
cdsStaticBindingsAddrType=_CdsStaticBindingsAddrType_Object((1,3,6,1,4,1,9,9,380,1,4,2,1,3),_CdsStaticBindingsAddrType_Type())
cdsStaticBindingsAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsStaticBindingsAddrType.setStatus(_B)
_CdsStaticBindingsIpAddress_Type=InetAddress
_CdsStaticBindingsIpAddress_Object=MibTableColumn
cdsStaticBindingsIpAddress=_CdsStaticBindingsIpAddress_Object((1,3,6,1,4,1,9,9,380,1,4,2,1,4),_CdsStaticBindingsIpAddress_Type())
cdsStaticBindingsIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsStaticBindingsIpAddress.setStatus(_B)
_CdsStaticBindingsInterface_Type=InterfaceIndex
_CdsStaticBindingsInterface_Object=MibTableColumn
cdsStaticBindingsInterface=_CdsStaticBindingsInterface_Object((1,3,6,1,4,1,9,9,380,1,4,2,1,5),_CdsStaticBindingsInterface_Type())
cdsStaticBindingsInterface.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsStaticBindingsInterface.setStatus(_B)
_CdsStaticBindingsStatus_Type=RowStatus
_CdsStaticBindingsStatus_Object=MibTableColumn
cdsStaticBindingsStatus=_CdsStaticBindingsStatus_Object((1,3,6,1,4,1,9,9,380,1,4,2,1,6),_CdsStaticBindingsStatus_Type())
cdsStaticBindingsStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cdsStaticBindingsStatus.setStatus(_B)
_CdsStatistics_ObjectIdentity=ObjectIdentity
cdsStatistics=_CdsStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,380,1,5))
_CdsTotalForwardedPkts_Type=Counter64
_CdsTotalForwardedPkts_Object=MibScalar
cdsTotalForwardedPkts=_CdsTotalForwardedPkts_Object((1,3,6,1,4,1,9,9,380,1,5,1),_CdsTotalForwardedPkts_Type())
cdsTotalForwardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsTotalForwardedPkts.setStatus(_B)
if mibBuilder.loadTexts:cdsTotalForwardedPkts.setUnits(_f)
_CdsTotalDroppedPkts_Type=Counter64
_CdsTotalDroppedPkts_Object=MibScalar
cdsTotalDroppedPkts=_CdsTotalDroppedPkts_Object((1,3,6,1,4,1,9,9,380,1,5,2),_CdsTotalDroppedPkts_Type())
cdsTotalDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsTotalDroppedPkts.setStatus(_B)
if mibBuilder.loadTexts:cdsTotalDroppedPkts.setUnits(_f)
_CdsUntrustedPortDroppedPkts_Type=Counter64
_CdsUntrustedPortDroppedPkts_Object=MibScalar
cdsUntrustedPortDroppedPkts=_CdsUntrustedPortDroppedPkts_Object((1,3,6,1,4,1,9,9,380,1,5,3),_CdsUntrustedPortDroppedPkts_Type())
cdsUntrustedPortDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsUntrustedPortDroppedPkts.setStatus(_B)
if mibBuilder.loadTexts:cdsUntrustedPortDroppedPkts.setUnits(_f)
_CdsForwardedWithoutOption82Pkts_Type=Counter32
_CdsForwardedWithoutOption82Pkts_Object=MibScalar
cdsForwardedWithoutOption82Pkts=_CdsForwardedWithoutOption82Pkts_Object((1,3,6,1,4,1,9,9,380,1,5,4),_CdsForwardedWithoutOption82Pkts_Type())
cdsForwardedWithoutOption82Pkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsForwardedWithoutOption82Pkts.setStatus(_B)
if mibBuilder.loadTexts:cdsForwardedWithoutOption82Pkts.setUnits(_f)
_CdsSrcGuard_ObjectIdentity=ObjectIdentity
cdsSrcGuard=_CdsSrcGuard_ObjectIdentity((1,3,6,1,4,1,9,9,380,1,6))
_CdsIfSrcGuardConfigTable_Object=MibTable
cdsIfSrcGuardConfigTable=_CdsIfSrcGuardConfigTable_Object((1,3,6,1,4,1,9,9,380,1,6,1))
if mibBuilder.loadTexts:cdsIfSrcGuardConfigTable.setStatus(_B)
_CdsIfSrcGuardConfigEntry_Object=MibTableRow
cdsIfSrcGuardConfigEntry=_CdsIfSrcGuardConfigEntry_Object((1,3,6,1,4,1,9,9,380,1,6,1,1))
cdsIfSrcGuardConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cdsIfSrcGuardConfigEntry.setStatus(_B)
_CdsIfSrcGuardEnable_Type=TruthValue
_CdsIfSrcGuardEnable_Object=MibTableColumn
cdsIfSrcGuardEnable=_CdsIfSrcGuardEnable_Object((1,3,6,1,4,1,9,9,380,1,6,1,1,1),_CdsIfSrcGuardEnable_Type())
cdsIfSrcGuardEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsIfSrcGuardEnable.setStatus(_E)
class _CdsIfSrcGuardFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disable',1),('ip',2),('ipMac',3),('strictIpMac',4)))
_CdsIfSrcGuardFilterType_Type.__name__=_Z
_CdsIfSrcGuardFilterType_Object=MibTableColumn
cdsIfSrcGuardFilterType=_CdsIfSrcGuardFilterType_Object((1,3,6,1,4,1,9,9,380,1,6,1,1,2),_CdsIfSrcGuardFilterType_Type())
cdsIfSrcGuardFilterType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdsIfSrcGuardFilterType.setStatus(_B)
_CdsIfSrcGuardAddrTable_Object=MibTable
cdsIfSrcGuardAddrTable=_CdsIfSrcGuardAddrTable_Object((1,3,6,1,4,1,9,9,380,1,6,2))
if mibBuilder.loadTexts:cdsIfSrcGuardAddrTable.setStatus(_B)
_CdsIfSrcGuardAddrEntry_Object=MibTableRow
cdsIfSrcGuardAddrEntry=_CdsIfSrcGuardAddrEntry_Object((1,3,6,1,4,1,9,9,380,1,6,2,1))
cdsIfSrcGuardAddrEntry.setIndexNames((0,_F,_G),(0,_A,_w))
if mibBuilder.loadTexts:cdsIfSrcGuardAddrEntry.setStatus(_B)
_CdsIfSrcGuardIndex_Type=Unsigned32
_CdsIfSrcGuardIndex_Object=MibTableColumn
cdsIfSrcGuardIndex=_CdsIfSrcGuardIndex_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,1),_CdsIfSrcGuardIndex_Type())
cdsIfSrcGuardIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:cdsIfSrcGuardIndex.setStatus(_B)
_CdsIfSrcGuardAddrType_Type=InetAddressType
_CdsIfSrcGuardAddrType_Object=MibTableColumn
cdsIfSrcGuardAddrType=_CdsIfSrcGuardAddrType_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,2),_CdsIfSrcGuardAddrType_Type())
cdsIfSrcGuardAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardAddrType.setStatus(_B)
_CdsIfSrcGuardAddress_Type=InetAddress
_CdsIfSrcGuardAddress_Object=MibTableColumn
cdsIfSrcGuardAddress=_CdsIfSrcGuardAddress_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,3),_CdsIfSrcGuardAddress_Type())
cdsIfSrcGuardAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardAddress.setStatus(_B)
class _CdsIfSrcGuardIpFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permitIpAddress',1),('denyAllIpAddress',2)))
_CdsIfSrcGuardIpFilterAction_Type.__name__=_Z
_CdsIfSrcGuardIpFilterAction_Object=MibTableColumn
cdsIfSrcGuardIpFilterAction=_CdsIfSrcGuardIpFilterAction_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,4),_CdsIfSrcGuardIpFilterAction_Type())
cdsIfSrcGuardIpFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardIpFilterAction.setStatus(_B)
class _CdsIfSrcGuardFilterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactiveTrustPort',2),('inactiveNoSnoopingVlan',3)))
_CdsIfSrcGuardFilterMode_Type.__name__=_Z
_CdsIfSrcGuardFilterMode_Object=MibTableColumn
cdsIfSrcGuardFilterMode=_CdsIfSrcGuardFilterMode_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,5),_CdsIfSrcGuardFilterMode_Type())
cdsIfSrcGuardFilterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardFilterMode.setStatus(_B)
_CdsIfSrcGuardMacAddress_Type=MacAddress
_CdsIfSrcGuardMacAddress_Object=MibTableColumn
cdsIfSrcGuardMacAddress=_CdsIfSrcGuardMacAddress_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,6),_CdsIfSrcGuardMacAddress_Type())
cdsIfSrcGuardMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardMacAddress.setStatus(_B)
class _CdsIfSrcGuardMacFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allowMacAddress',1),('denyAllMacAddresses',2),('permitAllMacAddresses',3)))
_CdsIfSrcGuardMacFilterAction_Type.__name__=_Z
_CdsIfSrcGuardMacFilterAction_Object=MibTableColumn
cdsIfSrcGuardMacFilterAction=_CdsIfSrcGuardMacFilterAction_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,7),_CdsIfSrcGuardMacFilterAction_Type())
cdsIfSrcGuardMacFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardMacFilterAction.setStatus(_B)
class _CdsIfSrcGuardVlansLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CdsIfSrcGuardVlansLow_Type.__name__=_b
_CdsIfSrcGuardVlansLow_Object=MibTableColumn
cdsIfSrcGuardVlansLow=_CdsIfSrcGuardVlansLow_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,8),_CdsIfSrcGuardVlansLow_Type())
cdsIfSrcGuardVlansLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardVlansLow.setStatus(_B)
class _CdsIfSrcGuardVlansHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CdsIfSrcGuardVlansHigh_Type.__name__=_b
_CdsIfSrcGuardVlansHigh_Object=MibTableColumn
cdsIfSrcGuardVlansHigh=_CdsIfSrcGuardVlansHigh_Object((1,3,6,1,4,1,9,9,380,1,6,2,1,9),_CdsIfSrcGuardVlansHigh_Type())
cdsIfSrcGuardVlansHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsIfSrcGuardVlansHigh.setStatus(_B)
_CiscoDhcpSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDhcpSnoopingMIBConformance=_CiscoDhcpSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,380,2))
_CdsMIBCompliances_ObjectIdentity=ObjectIdentity
cdsMIBCompliances=_CdsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,380,2,1))
_CdsMIBGroups_ObjectIdentity=ObjectIdentity
cdsMIBGroups=_CdsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,380,2,2))
cdsGlobalEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,1))
cdsGlobalEnableGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:cdsGlobalEnableGroup.setStatus(_B)
cdsDatabaseGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,2))
cdsDatabaseGroup.setObjects(*((_A,_y),(_A,_z)))
if mibBuilder.loadTexts:cdsDatabaseGroup.setStatus(_B)
cdsVlanConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,3))
cdsVlanConfigGroup.setObjects((_A,_A0))
if mibBuilder.loadTexts:cdsVlanConfigGroup.setStatus(_B)
cdsIfConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,4))
cdsIfConfigGroup.setObjects((_A,_A1))
if mibBuilder.loadTexts:cdsIfConfigGroup.setStatus(_B)
cdsIfRateLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,5))
cdsIfRateLimitGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:cdsIfRateLimitGroup.setStatus(_B)
cdsBindingsGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,6))
cdsBindingsGroup.setObjects(*((_A,_i),(_A,_j),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cdsBindingsGroup.setStatus(_B)
cdsStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,7))
cdsStatisticsGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:cdsStatisticsGroup.setStatus(_B)
cdsRelayAgentInfoOptGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,8))
cdsRelayAgentInfoOptGroup.setObjects((_A,_A9))
if mibBuilder.loadTexts:cdsRelayAgentInfoOptGroup.setStatus(_B)
cdsIfSrcGuardGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,9))
cdsIfSrcGuardGroup.setObjects(*((_A,_AA),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:cdsIfSrcGuardGroup.setStatus(_E)
cdsRelayAgentRemoteIdGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,10))
cdsRelayAgentRemoteIdGroup.setObjects((_A,_AB))
if mibBuilder.loadTexts:cdsRelayAgentRemoteIdGroup.setStatus(_E)
cdsMatchMacAddressGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,11))
cdsMatchMacAddressGroup.setObjects((_A,_AC))
if mibBuilder.loadTexts:cdsMatchMacAddressGroup.setStatus(_B)
cdsIfFeatureConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,12))
cdsIfFeatureConfigGroup.setObjects((_A,_AD))
if mibBuilder.loadTexts:cdsIfFeatureConfigGroup.setStatus(_B)
cdsBindingsLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,13))
cdsBindingsLimitGroup.setObjects(*((_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:cdsBindingsLimitGroup.setStatus(_B)
cdsStaticBindingsGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,14))
cdsStaticBindingsGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:cdsStaticBindingsGroup.setStatus(_B)
cdsIfSrcGuardIpFilterGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,15))
cdsIfSrcGuardIpFilterGroup.setObjects(*((_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:cdsIfSrcGuardIpFilterGroup.setStatus(_B)
cdsIfSrcGuardExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,16))
cdsIfSrcGuardExtGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:cdsIfSrcGuardExtGroup.setStatus(_B)
cdsIfSrcGuardTrafficFilterGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,17))
cdsIfSrcGuardTrafficFilterGroup.setObjects((_A,_AQ))
if mibBuilder.loadTexts:cdsIfSrcGuardTrafficFilterGroup.setStatus(_B)
cdsIfSrcGuardGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,18))
cdsIfSrcGuardGroupRev1.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:cdsIfSrcGuardGroupRev1.setStatus(_B)
cdsBindingsHostnameGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,19))
cdsBindingsHostnameGroup.setObjects((_A,_AR))
if mibBuilder.loadTexts:cdsBindingsHostnameGroup.setStatus(_B)
cdsRelayAgentInfoOptRemoteIdSubGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,20))
cdsRelayAgentInfoOptRemoteIdSubGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:cdsRelayAgentInfoOptRemoteIdSubGroup.setStatus(_B)
cdsIfVlanRelayInfoOptCircuitIdGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,21))
cdsIfVlanRelayInfoOptCircuitIdGroup.setObjects(*((_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:cdsIfVlanRelayInfoOptCircuitIdGroup.setStatus(_B)
cdsStatisticsExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,22))
cdsStatisticsExtGroup.setObjects((_A,_AV))
if mibBuilder.loadTexts:cdsStatisticsExtGroup.setStatus(_B)
cdsNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,23))
cdsNotifControlGroup.setObjects((_A,_AW))
if mibBuilder.loadTexts:cdsNotifControlGroup.setStatus(_B)
cdsIfVlanRelayInfoOptCircuitIdGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,25))
cdsIfVlanRelayInfoOptCircuitIdGroupSup1.setObjects((_A,_AX))
if mibBuilder.loadTexts:cdsIfVlanRelayInfoOptCircuitIdGroupSup1.setStatus(_B)
cdsVlanOperStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,380,2,2,26))
cdsVlanOperStatusGroup.setObjects((_A,_AY))
if mibBuilder.loadTexts:cdsVlanOperStatusGroup.setStatus(_B)
cdsBindingsNotification=NotificationType((1,3,6,1,4,1,9,9,380,0,1))
cdsBindingsNotification.setObjects(*((_A,_i),(_A,_j),(_F,_o)))
if mibBuilder.loadTexts:cdsBindingsNotification.setStatus(_B)
cdsBindingsNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,380,2,2,24))
cdsBindingsNotificationGroup.setObjects((_A,_AZ))
if mibBuilder.loadTexts:cdsBindingsNotificationGroup.setStatus(_B)
cdsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,380,2,1,1))
cdsMIBCompliance.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Aa),(_A,_Q)))
if mibBuilder.loadTexts:cdsMIBCompliance.setStatus(_E)
cdsMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,380,2,1,2))
cdsMIBCompliance2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_Q),(_A,_m),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cdsMIBCompliance2.setStatus(_E)
cdsMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,380,2,1,3))
cdsMIBCompliance3.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_Q),(_A,_m),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_a)))
if mibBuilder.loadTexts:cdsMIBCompliance3.setStatus(_E)
cdsMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,380,2,1,4))
cdsMIBCompliance4.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_Q),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_a),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cdsMIBCompliance4.setStatus(_E)
cdsMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,380,2,1,5))
cdsMIBCompliance5.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_Q),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_a),(_A,_c),(_A,_d),(_A,_e),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cdsMIBCompliance5.setStatus(_E)
cdsMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,380,2,1,6))
cdsMIBCompliance6.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_Q),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_a),(_A,_c),(_A,_d),(_A,_e),(_A,_g),(_A,_h),(_A,_n)))
if mibBuilder.loadTexts:cdsMIBCompliance6.setStatus(_E)
cdsMIBCompliance7=ModuleCompliance((1,3,6,1,4,1,9,9,380,2,1,7))
cdsMIBCompliance7.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_S),(_A,_Q),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_a),(_A,_c),(_A,_d),(_A,_e),(_A,_g),(_A,_h),(_A,_n),(_A,_Ab)))
if mibBuilder.loadTexts:cdsMIBCompliance7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDhcpSnoopingMIB':ciscoDhcpSnoopingMIB,'ciscoDhcpSnoopingMIBNotifs':ciscoDhcpSnoopingMIBNotifs,_AZ:cdsBindingsNotification,'ciscoDhcpSnoopingMIBObjects':ciscoDhcpSnoopingMIBObjects,'cdsGlobal':cdsGlobal,_x:cdsFeatureEnable,_y:cdsDatabaseFile,_z:cdsDatabaseUpdateInterval,_A9:cdsRelayAgentInfoOptEnable,_AB:cdsRelayAgentInfoOptRemoteId,_AC:cdsMatchMacAddressEnable,_AE:cdsGlobalMaxBindingsLimit,_AS:cdsRelayAgentInfoOptRemoteIdSub,_AW:cdsBindingsNotifEnabled,'cdsVlan':cdsVlan,'cdsVlanConfigTable':cdsVlanConfigTable,'cdsVlanConfigEntry':cdsVlanConfigEntry,_q:cdsVlanIndex,_A0:cdsVlanDhcpSnoopingEnable,_AY:cdsVlanDhcpSnoopingOperStatus,'cdsInterface':cdsInterface,'cdsIfConfigTable':cdsIfConfigTable,'cdsIfConfigEntry':cdsIfConfigEntry,_A1:cdsIfTrustEnable,'cdsIfRateLimitTable':cdsIfRateLimitTable,'cdsIfRateLimitEntry':cdsIfRateLimitEntry,_A2:cdsIfRateLimit,'cdsIfFeatureConfigTable':cdsIfFeatureConfigTable,'cdsIfFeatureConfigEntry':cdsIfFeatureConfigEntry,_AD:cdsIfFeatureEnable,'cdsIfBindingsLimitTable':cdsIfBindingsLimitTable,'cdsIfBindingsLimitEntry':cdsIfBindingsLimitEntry,_AF:cdsIfBindingsLimit,'cdsIfVlanRelayInfoOptCircuitIdTable':cdsIfVlanRelayInfoOptCircuitIdTable,'cdsIfVlanRelayInfoOptCircuitIdEntry':cdsIfVlanRelayInfoOptCircuitIdEntry,_r:cdsIfVlan,_AT:cdsIfVlanRelayInfoOptCircuitId,_AU:cdsIfVlanRelayInfoOptCircuitIdStatus,_AX:cdsIfVlanRelayInfoOptCircuitIdDirect,'cdsBindings':cdsBindings,'cdsBindingsTable':cdsBindingsTable,'cdsBindingsEntry':cdsBindingsEntry,_s:cdsBindingsVlan,_t:cdsBindingsMacAddress,_i:cdsBindingsAddrType,_j:cdsBindingsIpAddress,_A3:cdsBindingsInterface,_A4:cdsBindingsLeasedTime,_A5:cdsBindingsStatus,_AR:cdsBindingsHostname,'cdsStaticBindingsTable':cdsStaticBindingsTable,'cdsStaticBindingsEntry':cdsStaticBindingsEntry,_u:cdsStaticBindingsVlan,_v:cdsStaticBindingsMacAddress,_AG:cdsStaticBindingsAddrType,_AH:cdsStaticBindingsIpAddress,_AI:cdsStaticBindingsInterface,_AJ:cdsStaticBindingsStatus,'cdsStatistics':cdsStatistics,_A6:cdsTotalForwardedPkts,_A7:cdsTotalDroppedPkts,_A8:cdsUntrustedPortDroppedPkts,_AV:cdsForwardedWithoutOption82Pkts,'cdsSrcGuard':cdsSrcGuard,'cdsIfSrcGuardConfigTable':cdsIfSrcGuardConfigTable,'cdsIfSrcGuardConfigEntry':cdsIfSrcGuardConfigEntry,_AA:cdsIfSrcGuardEnable,_AQ:cdsIfSrcGuardFilterType,'cdsIfSrcGuardAddrTable':cdsIfSrcGuardAddrTable,'cdsIfSrcGuardAddrEntry':cdsIfSrcGuardAddrEntry,_w:cdsIfSrcGuardIndex,_k:cdsIfSrcGuardAddrType,_l:cdsIfSrcGuardAddress,_AK:cdsIfSrcGuardIpFilterAction,_AL:cdsIfSrcGuardFilterMode,_AM:cdsIfSrcGuardMacAddress,_AN:cdsIfSrcGuardMacFilterAction,_AO:cdsIfSrcGuardVlansLow,_AP:cdsIfSrcGuardVlansHigh,'ciscoDhcpSnoopingMIBConformance':ciscoDhcpSnoopingMIBConformance,'cdsMIBCompliances':cdsMIBCompliances,'cdsMIBCompliance':cdsMIBCompliance,'cdsMIBCompliance2':cdsMIBCompliance2,'cdsMIBCompliance3':cdsMIBCompliance3,'cdsMIBCompliance4':cdsMIBCompliance4,'cdsMIBCompliance5':cdsMIBCompliance5,'cdsMIBCompliance6':cdsMIBCompliance6,'cdsMIBCompliance7':cdsMIBCompliance7,'cdsMIBGroups':cdsMIBGroups,_K:cdsGlobalEnableGroup,_L:cdsDatabaseGroup,_M:cdsVlanConfigGroup,_I:cdsIfConfigGroup,_N:cdsIfRateLimitGroup,_J:cdsBindingsGroup,_O:cdsStatisticsGroup,_P:cdsRelayAgentInfoOptGroup,_Aa:cdsIfSrcGuardGroup,_m:cdsRelayAgentRemoteIdGroup,_Q:cdsMatchMacAddressGroup,_T:cdsIfFeatureConfigGroup,_U:cdsBindingsLimitGroup,_V:cdsStaticBindingsGroup,_W:cdsIfSrcGuardIpFilterGroup,_X:cdsIfSrcGuardExtGroup,_Y:cdsIfSrcGuardTrafficFilterGroup,_S:cdsIfSrcGuardGroupRev1,_a:cdsBindingsHostnameGroup,_c:cdsRelayAgentInfoOptRemoteIdSubGroup,_d:cdsIfVlanRelayInfoOptCircuitIdGroup,_e:cdsStatisticsExtGroup,_g:cdsNotifControlGroup,_h:cdsBindingsNotificationGroup,_n:cdsIfVlanRelayInfoOptCircuitIdGroupSup1,_Ab:cdsVlanOperStatusGroup})