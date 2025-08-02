_Af='ciscoNetRegistrarNotificatGroup'
_Ae='ciscoNetRegistrarNotEnableGroup'
_Ad='ciscoNetRegistrarNotifInfoGroup'
_Ac='ciscoNetworkRegistrarNotifCfgObjectsGroup'
_Ab='ciscoNetworkRegistrarNotifObjectsGroup'
_Aa='ciscoNetworkRegistrarDHCPScopeObjectsGroup'
_AZ='ciscoNetRegFailoverSyncFailure'
_AY='ciscoNetRegHaDnsConfigErr'
_AX='ciscoNetRegDnsForwardersResp'
_AW='ciscoNetRegDnsForwardersNotResp'
_AV='ciscoNetRegSecondaryZonesExpired'
_AU='ciscoNetRegMastersResp'
_AT='ciscoNetRegMastersNotResp'
_AS='ciscoNetRegHaDnsPartnerUp'
_AR='ciscoNetRegHaDnsPartnerDown'
_AQ='ciscoNetRegOtherServerResp'
_AP='ciscoNetRegOtherServerNotResp'
_AO='ciscoNetRegFreeAddrHighThreshold'
_AN='ciscoNetRegFreeAddrLowThreshold'
_AM='ciscoNetRegOtherServerResponding'
_AL='ciscoNetRegOtherServerNotResponding'
_AK='ciscoNetRegFreeAddressHigh'
_AJ='ciscoNetRegFreeAddressLow'
_AI='cnrEnableFailoverSyncFailure'
_AH='cnrEnableHaDnsConfigErr'
_AG='cnrEnableDnsForwardersResp'
_AF='cnrEnableDnsForwardersNotResp'
_AE='cnrEnableSecondaryZoneExpired'
_AD='cnrEnableMastersResp'
_AC='cnrEnableMastersNotResp'
_AB='cnrEnableHaDnsPartnerUp'
_AA='cnrEnableHaDnsPartnerDown'
_A9='cnrEnableOtherServerResp'
_A8='cnrEnableOtherServerNotResp'
_A7='cnrEnableFreeAddrHigh'
_A6='cnrEnableFreeAddrLow'
_A5='cnrEnableOtherServerResponding'
_A4='cnrEnableOtherServerNotResponding'
_A3='cnrEnableFreeAddressHigh'
_A2='cnrEnableFreeAddressLow'
_A1='percentage'
_A0='cnrDHCPScopeName'
_z='ciscoNetRegFailoverConfigMismatch'
_y='ciscoNetRegAddressConflict'
_x='ciscoNetRegDuplicateAddress'
_w='ciscoNetRegDNSQueueTooBig'
_v='ciscoNetRegServerStop'
_u='ciscoNetRegServerStart'
_t='cnrNotifSyncError'
_s='cnrNotifSyncDirection'
_r='cnrNotifBackupIPv6Address'
_q='cnrNotifBackupIPAddress'
_p='cnrNotifMainIPv6Address'
_o='cnrNotifMainIPAddress'
_n='cnrNotifFailoverCfgErrType'
_m='cnrNotifDHCPScopeFreeAddrHigh'
_l='cnrNotifDHCPScopeFreeAddrLow'
_k='cnrEnableFailoverConfigMismatch'
_j='cnrEnableAddressConflict'
_i='cnrEnableDuplicateAddress'
_h='cnrEnableDNSQueueTooBig'
_g='cnrEnableServerStop'
_f='cnrEnableServerStart'
_e='cnrDHCPScopeFreeAddrHighThreshold'
_d='cnrDHCPScopeFreeAddrLowThreshold'
_c='SnmpAdminString'
_b='cnrNotifRelatedServerType'
_a='cnrNotifPrimarySubnetNumber'
_Z='cnrNotifDHCPScopeName'
_Y='cnrNotifDHCPThresholdValue'
_X='cnrNotifDHCPThresholdType'
_W='cnrNotifDHCPScopeFreeAddrValue'
_V='cnrNotifContestedIpAddress'
_U='cnrNotifDupIpAddressDetectedBy'
_T='cnrNotifMACAddress'
_S='cnrNotifDupIpAddress'
_R='cnrDHCPScopeFreeAddrUnits'
_Q='cnrDHCPScopeFreeAddrValue'
_P='cnrNotifDnsServerIp6Address'
_O='cnrNotifFailoverPairName'
_N='DisplayString'
_M='cnrNotifZoneName'
_L='cnrNotifDnsRemoteServersList'
_K='cnrNotifDnsServerIpAddress'
_J='cnrNotifServerType'
_I='Integer32'
_H='cnrNotifIPv6Server'
_G='cnrNotifServer'
_F='deprecated'
_E='read-write'
_D='TruthValue'
_C='accessible-for-notify'
_B='current'
_A='CISCO-NETWORK-REGISTRAR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddressIPv6,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_c)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention',_D)
ciscoNetworkRegistrarMIB=ModuleIdentity((1,3,6,1,4,1,9,9,120))
if mibBuilder.loadTexts:ciscoNetworkRegistrarMIB.setRevisions(('2023-01-22 00:00','2017-04-03 00:00','2016-09-23 00:00','2014-06-13 00:00','2013-05-24 00:00','2010-05-24 00:00','2005-03-03 00:00','2003-01-11 00:00','1999-06-17 00:00','1998-11-01 00:00'))
class CnrPhysAddress(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,18))
_CiscoNetworkRegistrarMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNetworkRegistrarMIBObjects=_CiscoNetworkRegistrarMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,120,1))
_CnrDHCP_ObjectIdentity=ObjectIdentity
cnrDHCP=_CnrDHCP_ObjectIdentity((1,3,6,1,4,1,9,9,120,1,1))
_CnrDHCPScopeTable_Object=MibTable
cnrDHCPScopeTable=_CnrDHCPScopeTable_Object((1,3,6,1,4,1,9,9,120,1,1,1))
if mibBuilder.loadTexts:cnrDHCPScopeTable.setStatus(_F)
_CnrDHCPScopeEntry_Object=MibTableRow
cnrDHCPScopeEntry=_CnrDHCPScopeEntry_Object((1,3,6,1,4,1,9,9,120,1,1,1,1))
cnrDHCPScopeEntry.setIndexNames((0,_A,_A0))
if mibBuilder.loadTexts:cnrDHCPScopeEntry.setStatus(_F)
class _CnrDHCPScopeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CnrDHCPScopeName_Type.__name__=_N
_CnrDHCPScopeName_Object=MibTableColumn
cnrDHCPScopeName=_CnrDHCPScopeName_Object((1,3,6,1,4,1,9,9,120,1,1,1,1,1),_CnrDHCPScopeName_Type())
cnrDHCPScopeName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnrDHCPScopeName.setStatus(_F)
_CnrDHCPScopeFreeAddrLowThreshold_Type=Unsigned32
_CnrDHCPScopeFreeAddrLowThreshold_Object=MibTableColumn
cnrDHCPScopeFreeAddrLowThreshold=_CnrDHCPScopeFreeAddrLowThreshold_Object((1,3,6,1,4,1,9,9,120,1,1,1,1,2),_CnrDHCPScopeFreeAddrLowThreshold_Type())
cnrDHCPScopeFreeAddrLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrDHCPScopeFreeAddrLowThreshold.setStatus(_F)
_CnrDHCPScopeFreeAddrHighThreshold_Type=Unsigned32
_CnrDHCPScopeFreeAddrHighThreshold_Object=MibTableColumn
cnrDHCPScopeFreeAddrHighThreshold=_CnrDHCPScopeFreeAddrHighThreshold_Object((1,3,6,1,4,1,9,9,120,1,1,1,1,3),_CnrDHCPScopeFreeAddrHighThreshold_Type())
cnrDHCPScopeFreeAddrHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrDHCPScopeFreeAddrHighThreshold.setStatus(_F)
_CnrDHCPScopeFreeAddrValue_Type=Unsigned32
_CnrDHCPScopeFreeAddrValue_Object=MibTableColumn
cnrDHCPScopeFreeAddrValue=_CnrDHCPScopeFreeAddrValue_Object((1,3,6,1,4,1,9,9,120,1,1,1,1,4),_CnrDHCPScopeFreeAddrValue_Type())
cnrDHCPScopeFreeAddrValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrDHCPScopeFreeAddrValue.setStatus(_F)
class _CnrDHCPScopeFreeAddrUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('value',1),('percent',2)))
_CnrDHCPScopeFreeAddrUnits_Type.__name__=_I
_CnrDHCPScopeFreeAddrUnits_Object=MibTableColumn
cnrDHCPScopeFreeAddrUnits=_CnrDHCPScopeFreeAddrUnits_Object((1,3,6,1,4,1,9,9,120,1,1,1,1,5),_CnrDHCPScopeFreeAddrUnits_Type())
cnrDHCPScopeFreeAddrUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrDHCPScopeFreeAddrUnits.setStatus(_F)
_CnrNotifObjects_ObjectIdentity=ObjectIdentity
cnrNotifObjects=_CnrNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,120,1,2))
_CnrNotifDupIpAddress_Type=IpAddress
_CnrNotifDupIpAddress_Object=MibScalar
cnrNotifDupIpAddress=_CnrNotifDupIpAddress_Object((1,3,6,1,4,1,9,9,120,1,2,1),_CnrNotifDupIpAddress_Type())
cnrNotifDupIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDupIpAddress.setStatus(_B)
_CnrNotifMACAddress_Type=CnrPhysAddress
_CnrNotifMACAddress_Object=MibScalar
cnrNotifMACAddress=_CnrNotifMACAddress_Object((1,3,6,1,4,1,9,9,120,1,2,2),_CnrNotifMACAddress_Type())
cnrNotifMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifMACAddress.setStatus(_B)
_CnrNotifServer_Type=IpAddress
_CnrNotifServer_Object=MibScalar
cnrNotifServer=_CnrNotifServer_Object((1,3,6,1,4,1,9,9,120,1,2,3),_CnrNotifServer_Type())
cnrNotifServer.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifServer.setStatus(_B)
class _CnrNotifServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('dns',1),('dhcp',2),('ldap',3),('tftp',4),('ccm',5)))
_CnrNotifServerType_Type.__name__=_I
_CnrNotifServerType_Object=MibScalar
cnrNotifServerType=_CnrNotifServerType_Object((1,3,6,1,4,1,9,9,120,1,2,4),_CnrNotifServerType_Type())
cnrNotifServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifServerType.setStatus(_B)
class _CnrNotifDupIpAddressDetectedBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dhcpClient',1),('dhcpServer',2)))
_CnrNotifDupIpAddressDetectedBy_Type.__name__=_I
_CnrNotifDupIpAddressDetectedBy_Object=MibScalar
cnrNotifDupIpAddressDetectedBy=_CnrNotifDupIpAddressDetectedBy_Object((1,3,6,1,4,1,9,9,120,1,2,5),_CnrNotifDupIpAddressDetectedBy_Type())
cnrNotifDupIpAddressDetectedBy.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDupIpAddressDetectedBy.setStatus(_B)
_CnrNotifContestedIpAddress_Type=IpAddress
_CnrNotifContestedIpAddress_Object=MibScalar
cnrNotifContestedIpAddress=_CnrNotifContestedIpAddress_Object((1,3,6,1,4,1,9,9,120,1,2,6),_CnrNotifContestedIpAddress_Type())
cnrNotifContestedIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifContestedIpAddress.setStatus(_B)
_CnrNotifDHCPScopeFreeAddrLow_Type=Unsigned32
_CnrNotifDHCPScopeFreeAddrLow_Object=MibScalar
cnrNotifDHCPScopeFreeAddrLow=_CnrNotifDHCPScopeFreeAddrLow_Object((1,3,6,1,4,1,9,9,120,1,2,7),_CnrNotifDHCPScopeFreeAddrLow_Type())
cnrNotifDHCPScopeFreeAddrLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDHCPScopeFreeAddrLow.setStatus(_B)
if mibBuilder.loadTexts:cnrNotifDHCPScopeFreeAddrLow.setUnits(_A1)
_CnrNotifDHCPScopeFreeAddrHigh_Type=Unsigned32
_CnrNotifDHCPScopeFreeAddrHigh_Object=MibScalar
cnrNotifDHCPScopeFreeAddrHigh=_CnrNotifDHCPScopeFreeAddrHigh_Object((1,3,6,1,4,1,9,9,120,1,2,8),_CnrNotifDHCPScopeFreeAddrHigh_Type())
cnrNotifDHCPScopeFreeAddrHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDHCPScopeFreeAddrHigh.setStatus(_B)
if mibBuilder.loadTexts:cnrNotifDHCPScopeFreeAddrHigh.setUnits(_A1)
_CnrNotifDHCPScopeFreeAddrValue_Type=Gauge32
_CnrNotifDHCPScopeFreeAddrValue_Object=MibScalar
cnrNotifDHCPScopeFreeAddrValue=_CnrNotifDHCPScopeFreeAddrValue_Object((1,3,6,1,4,1,9,9,120,1,2,9),_CnrNotifDHCPScopeFreeAddrValue_Type())
cnrNotifDHCPScopeFreeAddrValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDHCPScopeFreeAddrValue.setStatus(_B)
if mibBuilder.loadTexts:cnrNotifDHCPScopeFreeAddrValue.setUnits('IP addresses')
class _CnrNotifDHCPThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('scope',1),('network',2),('selectionTags',3)))
_CnrNotifDHCPThresholdType_Type.__name__=_I
_CnrNotifDHCPThresholdType_Object=MibScalar
cnrNotifDHCPThresholdType=_CnrNotifDHCPThresholdType_Object((1,3,6,1,4,1,9,9,120,1,2,10),_CnrNotifDHCPThresholdType_Type())
cnrNotifDHCPThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDHCPThresholdType.setStatus(_B)
class _CnrNotifDHCPThresholdValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CnrNotifDHCPThresholdValue_Type.__name__=_N
_CnrNotifDHCPThresholdValue_Object=MibScalar
cnrNotifDHCPThresholdValue=_CnrNotifDHCPThresholdValue_Object((1,3,6,1,4,1,9,9,120,1,2,11),_CnrNotifDHCPThresholdValue_Type())
cnrNotifDHCPThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDHCPThresholdValue.setStatus(_B)
class _CnrNotifDHCPScopeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CnrNotifDHCPScopeName_Type.__name__=_N
_CnrNotifDHCPScopeName_Object=MibScalar
cnrNotifDHCPScopeName=_CnrNotifDHCPScopeName_Object((1,3,6,1,4,1,9,9,120,1,2,12),_CnrNotifDHCPScopeName_Type())
cnrNotifDHCPScopeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDHCPScopeName.setStatus(_B)
_CnrNotifPrimarySubnetNumber_Type=DisplayString
_CnrNotifPrimarySubnetNumber_Object=MibScalar
cnrNotifPrimarySubnetNumber=_CnrNotifPrimarySubnetNumber_Object((1,3,6,1,4,1,9,9,120,1,2,13),_CnrNotifPrimarySubnetNumber_Type())
cnrNotifPrimarySubnetNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifPrimarySubnetNumber.setStatus(_B)
class _CnrNotifRelatedServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dnsPrimary',1),('ldap',2),('failoverPartner',3),('relay-agent',4)))
_CnrNotifRelatedServerType_Type.__name__=_I
_CnrNotifRelatedServerType_Object=MibScalar
cnrNotifRelatedServerType=_CnrNotifRelatedServerType_Object((1,3,6,1,4,1,9,9,120,1,2,14),_CnrNotifRelatedServerType_Type())
cnrNotifRelatedServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifRelatedServerType.setStatus(_B)
_CnrNotifDnsServerIpAddress_Type=IpAddress
_CnrNotifDnsServerIpAddress_Object=MibScalar
cnrNotifDnsServerIpAddress=_CnrNotifDnsServerIpAddress_Object((1,3,6,1,4,1,9,9,120,1,2,15),_CnrNotifDnsServerIpAddress_Type())
cnrNotifDnsServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDnsServerIpAddress.setStatus(_B)
_CnrNotifZoneName_Type=DisplayString
_CnrNotifZoneName_Object=MibScalar
cnrNotifZoneName=_CnrNotifZoneName_Object((1,3,6,1,4,1,9,9,120,1,2,16),_CnrNotifZoneName_Type())
cnrNotifZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifZoneName.setStatus(_B)
class _CnrNotifDnsRemoteServersList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_CnrNotifDnsRemoteServersList_Type.__name__=_N
_CnrNotifDnsRemoteServersList_Object=MibScalar
cnrNotifDnsRemoteServersList=_CnrNotifDnsRemoteServersList_Object((1,3,6,1,4,1,9,9,120,1,2,17),_CnrNotifDnsRemoteServersList_Type())
cnrNotifDnsRemoteServersList.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDnsRemoteServersList.setStatus(_B)
_CnrNotifIPv6Server_Type=InetAddressIPv6
_CnrNotifIPv6Server_Object=MibScalar
cnrNotifIPv6Server=_CnrNotifIPv6Server_Object((1,3,6,1,4,1,9,9,120,1,2,18),_CnrNotifIPv6Server_Type())
cnrNotifIPv6Server.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifIPv6Server.setStatus(_B)
class _CnrNotifFailoverPairName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CnrNotifFailoverPairName_Type.__name__=_c
_CnrNotifFailoverPairName_Object=MibScalar
cnrNotifFailoverPairName=_CnrNotifFailoverPairName_Object((1,3,6,1,4,1,9,9,120,1,2,19),_CnrNotifFailoverPairName_Type())
cnrNotifFailoverPairName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifFailoverPairName.setStatus(_B)
class _CnrNotifFailoverCfgErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('mclt-error',1),('hba-error',2),('backup-percentage-error',3),('server-address-error',4),('config-error',5),('internal-error',6),('backup-load-balancing-config-error',7),('main-load-balancing-config-error',8)))
_CnrNotifFailoverCfgErrType_Type.__name__=_I
_CnrNotifFailoverCfgErrType_Object=MibScalar
cnrNotifFailoverCfgErrType=_CnrNotifFailoverCfgErrType_Object((1,3,6,1,4,1,9,9,120,1,2,20),_CnrNotifFailoverCfgErrType_Type())
cnrNotifFailoverCfgErrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifFailoverCfgErrType.setStatus(_B)
_CnrNotifDnsServerIp6Address_Type=InetAddressIPv6
_CnrNotifDnsServerIp6Address_Object=MibScalar
cnrNotifDnsServerIp6Address=_CnrNotifDnsServerIp6Address_Object((1,3,6,1,4,1,9,9,120,1,2,21),_CnrNotifDnsServerIp6Address_Type())
cnrNotifDnsServerIp6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifDnsServerIp6Address.setStatus(_B)
_CnrNotifMainIPAddress_Type=IpAddress
_CnrNotifMainIPAddress_Object=MibScalar
cnrNotifMainIPAddress=_CnrNotifMainIPAddress_Object((1,3,6,1,4,1,9,9,120,1,2,22),_CnrNotifMainIPAddress_Type())
cnrNotifMainIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifMainIPAddress.setStatus(_B)
_CnrNotifMainIPv6Address_Type=InetAddressIPv6
_CnrNotifMainIPv6Address_Object=MibScalar
cnrNotifMainIPv6Address=_CnrNotifMainIPv6Address_Object((1,3,6,1,4,1,9,9,120,1,2,23),_CnrNotifMainIPv6Address_Type())
cnrNotifMainIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifMainIPv6Address.setStatus(_B)
_CnrNotifBackupIPAddress_Type=IpAddress
_CnrNotifBackupIPAddress_Object=MibScalar
cnrNotifBackupIPAddress=_CnrNotifBackupIPAddress_Object((1,3,6,1,4,1,9,9,120,1,2,24),_CnrNotifBackupIPAddress_Type())
cnrNotifBackupIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifBackupIPAddress.setStatus(_B)
_CnrNotifBackupIPv6Address_Type=InetAddressIPv6
_CnrNotifBackupIPv6Address_Object=MibScalar
cnrNotifBackupIPv6Address=_CnrNotifBackupIPv6Address_Object((1,3,6,1,4,1,9,9,120,1,2,25),_CnrNotifBackupIPv6Address_Type())
cnrNotifBackupIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifBackupIPv6Address.setStatus(_B)
class _CnrNotifSyncDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main-to-backup',1),('backup-to-main',2)))
_CnrNotifSyncDirection_Type.__name__=_I
_CnrNotifSyncDirection_Object=MibScalar
cnrNotifSyncDirection=_CnrNotifSyncDirection_Object((1,3,6,1,4,1,9,9,120,1,2,26),_CnrNotifSyncDirection_Type())
cnrNotifSyncDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifSyncDirection.setStatus(_B)
class _CnrNotifSyncError_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CnrNotifSyncError_Type.__name__=_c
_CnrNotifSyncError_Object=MibScalar
cnrNotifSyncError=_CnrNotifSyncError_Object((1,3,6,1,4,1,9,9,120,1,2,27),_CnrNotifSyncError_Type())
cnrNotifSyncError.setMaxAccess(_C)
if mibBuilder.loadTexts:cnrNotifSyncError.setStatus(_B)
_CnrNotifCfgObjects_ObjectIdentity=ObjectIdentity
cnrNotifCfgObjects=_CnrNotifCfgObjects_ObjectIdentity((1,3,6,1,4,1,9,9,120,1,3))
class _CnrEnableFreeAddressLow_Type(TruthValue):defaultValue=2
_CnrEnableFreeAddressLow_Type.__name__=_D
_CnrEnableFreeAddressLow_Object=MibScalar
cnrEnableFreeAddressLow=_CnrEnableFreeAddressLow_Object((1,3,6,1,4,1,9,9,120,1,3,1),_CnrEnableFreeAddressLow_Type())
cnrEnableFreeAddressLow.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableFreeAddressLow.setStatus(_F)
class _CnrEnableFreeAddressHigh_Type(TruthValue):defaultValue=2
_CnrEnableFreeAddressHigh_Type.__name__=_D
_CnrEnableFreeAddressHigh_Object=MibScalar
cnrEnableFreeAddressHigh=_CnrEnableFreeAddressHigh_Object((1,3,6,1,4,1,9,9,120,1,3,2),_CnrEnableFreeAddressHigh_Type())
cnrEnableFreeAddressHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableFreeAddressHigh.setStatus(_F)
class _CnrEnableServerStart_Type(TruthValue):defaultValue=2
_CnrEnableServerStart_Type.__name__=_D
_CnrEnableServerStart_Object=MibScalar
cnrEnableServerStart=_CnrEnableServerStart_Object((1,3,6,1,4,1,9,9,120,1,3,3),_CnrEnableServerStart_Type())
cnrEnableServerStart.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableServerStart.setStatus(_B)
class _CnrEnableServerStop_Type(TruthValue):defaultValue=2
_CnrEnableServerStop_Type.__name__=_D
_CnrEnableServerStop_Object=MibScalar
cnrEnableServerStop=_CnrEnableServerStop_Object((1,3,6,1,4,1,9,9,120,1,3,4),_CnrEnableServerStop_Type())
cnrEnableServerStop.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableServerStop.setStatus(_B)
class _CnrEnableDNSQueueTooBig_Type(TruthValue):defaultValue=2
_CnrEnableDNSQueueTooBig_Type.__name__=_D
_CnrEnableDNSQueueTooBig_Object=MibScalar
cnrEnableDNSQueueTooBig=_CnrEnableDNSQueueTooBig_Object((1,3,6,1,4,1,9,9,120,1,3,5),_CnrEnableDNSQueueTooBig_Type())
cnrEnableDNSQueueTooBig.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableDNSQueueTooBig.setStatus(_B)
class _CnrEnableOtherServerNotResponding_Type(TruthValue):defaultValue=2
_CnrEnableOtherServerNotResponding_Type.__name__=_D
_CnrEnableOtherServerNotResponding_Object=MibScalar
cnrEnableOtherServerNotResponding=_CnrEnableOtherServerNotResponding_Object((1,3,6,1,4,1,9,9,120,1,3,6),_CnrEnableOtherServerNotResponding_Type())
cnrEnableOtherServerNotResponding.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableOtherServerNotResponding.setStatus(_F)
class _CnrEnableDuplicateAddress_Type(TruthValue):defaultValue=2
_CnrEnableDuplicateAddress_Type.__name__=_D
_CnrEnableDuplicateAddress_Object=MibScalar
cnrEnableDuplicateAddress=_CnrEnableDuplicateAddress_Object((1,3,6,1,4,1,9,9,120,1,3,7),_CnrEnableDuplicateAddress_Type())
cnrEnableDuplicateAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableDuplicateAddress.setStatus(_B)
class _CnrEnableAddressConflict_Type(TruthValue):defaultValue=2
_CnrEnableAddressConflict_Type.__name__=_D
_CnrEnableAddressConflict_Object=MibScalar
cnrEnableAddressConflict=_CnrEnableAddressConflict_Object((1,3,6,1,4,1,9,9,120,1,3,8),_CnrEnableAddressConflict_Type())
cnrEnableAddressConflict.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableAddressConflict.setStatus(_B)
class _CnrEnableOtherServerResponding_Type(TruthValue):defaultValue=2
_CnrEnableOtherServerResponding_Type.__name__=_D
_CnrEnableOtherServerResponding_Object=MibScalar
cnrEnableOtherServerResponding=_CnrEnableOtherServerResponding_Object((1,3,6,1,4,1,9,9,120,1,3,9),_CnrEnableOtherServerResponding_Type())
cnrEnableOtherServerResponding.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableOtherServerResponding.setStatus(_F)
class _CnrEnableFailoverConfigMismatch_Type(TruthValue):defaultValue=2
_CnrEnableFailoverConfigMismatch_Type.__name__=_D
_CnrEnableFailoverConfigMismatch_Object=MibScalar
cnrEnableFailoverConfigMismatch=_CnrEnableFailoverConfigMismatch_Object((1,3,6,1,4,1,9,9,120,1,3,10),_CnrEnableFailoverConfigMismatch_Type())
cnrEnableFailoverConfigMismatch.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableFailoverConfigMismatch.setStatus(_B)
class _CnrEnableFreeAddrLow_Type(TruthValue):defaultValue=2
_CnrEnableFreeAddrLow_Type.__name__=_D
_CnrEnableFreeAddrLow_Object=MibScalar
cnrEnableFreeAddrLow=_CnrEnableFreeAddrLow_Object((1,3,6,1,4,1,9,9,120,1,3,11),_CnrEnableFreeAddrLow_Type())
cnrEnableFreeAddrLow.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableFreeAddrLow.setStatus(_B)
class _CnrEnableFreeAddrHigh_Type(TruthValue):defaultValue=2
_CnrEnableFreeAddrHigh_Type.__name__=_D
_CnrEnableFreeAddrHigh_Object=MibScalar
cnrEnableFreeAddrHigh=_CnrEnableFreeAddrHigh_Object((1,3,6,1,4,1,9,9,120,1,3,12),_CnrEnableFreeAddrHigh_Type())
cnrEnableFreeAddrHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableFreeAddrHigh.setStatus(_B)
class _CnrEnableOtherServerNotResp_Type(TruthValue):defaultValue=2
_CnrEnableOtherServerNotResp_Type.__name__=_D
_CnrEnableOtherServerNotResp_Object=MibScalar
cnrEnableOtherServerNotResp=_CnrEnableOtherServerNotResp_Object((1,3,6,1,4,1,9,9,120,1,3,13),_CnrEnableOtherServerNotResp_Type())
cnrEnableOtherServerNotResp.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableOtherServerNotResp.setStatus(_B)
class _CnrEnableOtherServerResp_Type(TruthValue):defaultValue=2
_CnrEnableOtherServerResp_Type.__name__=_D
_CnrEnableOtherServerResp_Object=MibScalar
cnrEnableOtherServerResp=_CnrEnableOtherServerResp_Object((1,3,6,1,4,1,9,9,120,1,3,14),_CnrEnableOtherServerResp_Type())
cnrEnableOtherServerResp.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableOtherServerResp.setStatus(_B)
class _CnrEnableHaDnsPartnerDown_Type(TruthValue):defaultValue=2
_CnrEnableHaDnsPartnerDown_Type.__name__=_D
_CnrEnableHaDnsPartnerDown_Object=MibScalar
cnrEnableHaDnsPartnerDown=_CnrEnableHaDnsPartnerDown_Object((1,3,6,1,4,1,9,9,120,1,3,15),_CnrEnableHaDnsPartnerDown_Type())
cnrEnableHaDnsPartnerDown.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableHaDnsPartnerDown.setStatus(_B)
class _CnrEnableHaDnsPartnerUp_Type(TruthValue):defaultValue=2
_CnrEnableHaDnsPartnerUp_Type.__name__=_D
_CnrEnableHaDnsPartnerUp_Object=MibScalar
cnrEnableHaDnsPartnerUp=_CnrEnableHaDnsPartnerUp_Object((1,3,6,1,4,1,9,9,120,1,3,16),_CnrEnableHaDnsPartnerUp_Type())
cnrEnableHaDnsPartnerUp.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableHaDnsPartnerUp.setStatus(_B)
class _CnrEnableMastersNotResp_Type(TruthValue):defaultValue=2
_CnrEnableMastersNotResp_Type.__name__=_D
_CnrEnableMastersNotResp_Object=MibScalar
cnrEnableMastersNotResp=_CnrEnableMastersNotResp_Object((1,3,6,1,4,1,9,9,120,1,3,17),_CnrEnableMastersNotResp_Type())
cnrEnableMastersNotResp.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableMastersNotResp.setStatus(_B)
class _CnrEnableMastersResp_Type(TruthValue):defaultValue=2
_CnrEnableMastersResp_Type.__name__=_D
_CnrEnableMastersResp_Object=MibScalar
cnrEnableMastersResp=_CnrEnableMastersResp_Object((1,3,6,1,4,1,9,9,120,1,3,18),_CnrEnableMastersResp_Type())
cnrEnableMastersResp.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableMastersResp.setStatus(_B)
class _CnrEnableSecondaryZoneExpired_Type(TruthValue):defaultValue=2
_CnrEnableSecondaryZoneExpired_Type.__name__=_D
_CnrEnableSecondaryZoneExpired_Object=MibScalar
cnrEnableSecondaryZoneExpired=_CnrEnableSecondaryZoneExpired_Object((1,3,6,1,4,1,9,9,120,1,3,19),_CnrEnableSecondaryZoneExpired_Type())
cnrEnableSecondaryZoneExpired.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableSecondaryZoneExpired.setStatus(_B)
class _CnrEnableDnsForwardersNotResp_Type(TruthValue):defaultValue=2
_CnrEnableDnsForwardersNotResp_Type.__name__=_D
_CnrEnableDnsForwardersNotResp_Object=MibScalar
cnrEnableDnsForwardersNotResp=_CnrEnableDnsForwardersNotResp_Object((1,3,6,1,4,1,9,9,120,1,3,20),_CnrEnableDnsForwardersNotResp_Type())
cnrEnableDnsForwardersNotResp.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableDnsForwardersNotResp.setStatus(_B)
class _CnrEnableDnsForwardersResp_Type(TruthValue):defaultValue=2
_CnrEnableDnsForwardersResp_Type.__name__=_D
_CnrEnableDnsForwardersResp_Object=MibScalar
cnrEnableDnsForwardersResp=_CnrEnableDnsForwardersResp_Object((1,3,6,1,4,1,9,9,120,1,3,21),_CnrEnableDnsForwardersResp_Type())
cnrEnableDnsForwardersResp.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableDnsForwardersResp.setStatus(_B)
class _CnrEnableHaDnsConfigErr_Type(TruthValue):defaultValue=2
_CnrEnableHaDnsConfigErr_Type.__name__=_D
_CnrEnableHaDnsConfigErr_Object=MibScalar
cnrEnableHaDnsConfigErr=_CnrEnableHaDnsConfigErr_Object((1,3,6,1,4,1,9,9,120,1,3,22),_CnrEnableHaDnsConfigErr_Type())
cnrEnableHaDnsConfigErr.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableHaDnsConfigErr.setStatus(_B)
class _CnrEnableFailoverSyncFailure_Type(TruthValue):defaultValue=2
_CnrEnableFailoverSyncFailure_Type.__name__=_D
_CnrEnableFailoverSyncFailure_Object=MibScalar
cnrEnableFailoverSyncFailure=_CnrEnableFailoverSyncFailure_Object((1,3,6,1,4,1,9,9,120,1,3,23),_CnrEnableFailoverSyncFailure_Type())
cnrEnableFailoverSyncFailure.setMaxAccess(_E)
if mibBuilder.loadTexts:cnrEnableFailoverSyncFailure.setStatus(_B)
_CiscoNetRegMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoNetRegMIBNotificationPrefix=_CiscoNetRegMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,120,2))
_CiscoNetRegMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoNetRegMIBNotifications=_CiscoNetRegMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,120,2,0))
_CiscoNetworkRegistrarMIBConformance_ObjectIdentity=ObjectIdentity
ciscoNetworkRegistrarMIBConformance=_CiscoNetworkRegistrarMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,120,3))
_CiscoNetworkRegistrarMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNetworkRegistrarMIBCompliances=_CiscoNetworkRegistrarMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,120,3,1))
_CiscoNetworkRegistrarMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNetworkRegistrarMIBGroups=_CiscoNetworkRegistrarMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,120,3,2))
ciscoNetworkRegistrarDHCPScopeObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,120,3,2,1))
ciscoNetworkRegistrarDHCPScopeObjectsGroup.setObjects(*((_A,_d),(_A,_e),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoNetworkRegistrarDHCPScopeObjectsGroup.setStatus(_F)
ciscoNetworkRegistrarNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,120,3,2,2))
ciscoNetworkRegistrarNotifObjectsGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_G),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:ciscoNetworkRegistrarNotifObjectsGroup.setStatus(_F)
ciscoNetworkRegistrarNotifCfgObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,120,3,2,3))
ciscoNetworkRegistrarNotifCfgObjectsGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_f),(_A,_g),(_A,_h),(_A,_A4),(_A,_i),(_A,_j),(_A,_A5),(_A,_k)))
if mibBuilder.loadTexts:ciscoNetworkRegistrarNotifCfgObjectsGroup.setStatus(_F)
ciscoNetRegistrarNotifInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,120,3,2,5))
ciscoNetRegistrarNotifInfoGroup.setObjects(*((_A,_S),(_A,_T),(_A,_G),(_A,_J),(_A,_U),(_A,_V),(_A,_l),(_A,_m),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_K),(_A,_M),(_A,_L),(_A,_H),(_A,_O),(_A,_n),(_A,_P),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ciscoNetRegistrarNotifInfoGroup.setStatus(_B)
ciscoNetRegistrarNotEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,120,3,2,6))
ciscoNetRegistrarNotEnableGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:ciscoNetRegistrarNotEnableGroup.setStatus(_B)
ciscoNetRegFreeAddressLow=NotificationType((1,3,6,1,4,1,9,9,120,2,0,1))
ciscoNetRegFreeAddressLow.setObjects(*((_A,_d),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoNetRegFreeAddressLow.setStatus(_F)
ciscoNetRegFreeAddressHigh=NotificationType((1,3,6,1,4,1,9,9,120,2,0,2))
ciscoNetRegFreeAddressHigh.setObjects(*((_A,_e),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoNetRegFreeAddressHigh.setStatus(_F)
ciscoNetRegServerStart=NotificationType((1,3,6,1,4,1,9,9,120,2,0,3))
ciscoNetRegServerStart.setObjects((_A,_J))
if mibBuilder.loadTexts:ciscoNetRegServerStart.setStatus(_B)
ciscoNetRegServerStop=NotificationType((1,3,6,1,4,1,9,9,120,2,0,4))
ciscoNetRegServerStop.setObjects((_A,_J))
if mibBuilder.loadTexts:ciscoNetRegServerStop.setStatus(_B)
ciscoNetRegDNSQueueTooBig=NotificationType((1,3,6,1,4,1,9,9,120,2,0,5))
if mibBuilder.loadTexts:ciscoNetRegDNSQueueTooBig.setStatus(_B)
ciscoNetRegOtherServerNotResponding=NotificationType((1,3,6,1,4,1,9,9,120,2,0,6))
ciscoNetRegOtherServerNotResponding.setObjects(*((_A,_G),(_A,_J)))
if mibBuilder.loadTexts:ciscoNetRegOtherServerNotResponding.setStatus(_F)
ciscoNetRegDuplicateAddress=NotificationType((1,3,6,1,4,1,9,9,120,2,0,7))
ciscoNetRegDuplicateAddress.setObjects(*((_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoNetRegDuplicateAddress.setStatus(_B)
ciscoNetRegAddressConflict=NotificationType((1,3,6,1,4,1,9,9,120,2,0,8))
ciscoNetRegAddressConflict.setObjects(*((_A,_V),(_A,_G),(_A,_H),(_A,_O)))
if mibBuilder.loadTexts:ciscoNetRegAddressConflict.setStatus(_B)
ciscoNetRegOtherServerResponding=NotificationType((1,3,6,1,4,1,9,9,120,2,0,9))
ciscoNetRegOtherServerResponding.setObjects(*((_A,_G),(_A,_J)))
if mibBuilder.loadTexts:ciscoNetRegOtherServerResponding.setStatus(_F)
ciscoNetRegFailoverConfigMismatch=NotificationType((1,3,6,1,4,1,9,9,120,2,0,10))
ciscoNetRegFailoverConfigMismatch.setObjects(*((_A,_G),(_A,_H),(_A,_O),(_A,_n)))
if mibBuilder.loadTexts:ciscoNetRegFailoverConfigMismatch.setStatus(_B)
ciscoNetRegFreeAddrLowThreshold=NotificationType((1,3,6,1,4,1,9,9,120,2,0,11))
ciscoNetRegFreeAddrLowThreshold.setObjects(*((_A,_l),(_A,_W),(_A,_Z),(_A,_a),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoNetRegFreeAddrLowThreshold.setStatus(_B)
ciscoNetRegFreeAddrHighThreshold=NotificationType((1,3,6,1,4,1,9,9,120,2,0,12))
ciscoNetRegFreeAddrHighThreshold.setObjects(*((_A,_m),(_A,_W),(_A,_Z),(_A,_a),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoNetRegFreeAddrHighThreshold.setStatus(_B)
ciscoNetRegOtherServerNotResp=NotificationType((1,3,6,1,4,1,9,9,120,2,0,13))
ciscoNetRegOtherServerNotResp.setObjects(*((_A,_G),(_A,_b),(_A,_H)))
if mibBuilder.loadTexts:ciscoNetRegOtherServerNotResp.setStatus(_B)
ciscoNetRegOtherServerResp=NotificationType((1,3,6,1,4,1,9,9,120,2,0,14))
ciscoNetRegOtherServerResp.setObjects(*((_A,_G),(_A,_b),(_A,_H)))
if mibBuilder.loadTexts:ciscoNetRegOtherServerResp.setStatus(_B)
ciscoNetRegHaDnsPartnerDown=NotificationType((1,3,6,1,4,1,9,9,120,2,0,15))
ciscoNetRegHaDnsPartnerDown.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoNetRegHaDnsPartnerDown.setStatus(_B)
ciscoNetRegHaDnsPartnerUp=NotificationType((1,3,6,1,4,1,9,9,120,2,0,16))
ciscoNetRegHaDnsPartnerUp.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoNetRegHaDnsPartnerUp.setStatus(_B)
ciscoNetRegMastersNotResp=NotificationType((1,3,6,1,4,1,9,9,120,2,0,17))
ciscoNetRegMastersNotResp.setObjects(*((_A,_K),(_A,_P),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:ciscoNetRegMastersNotResp.setStatus(_B)
ciscoNetRegMastersResp=NotificationType((1,3,6,1,4,1,9,9,120,2,0,18))
ciscoNetRegMastersResp.setObjects(*((_A,_K),(_A,_P),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:ciscoNetRegMastersResp.setStatus(_B)
ciscoNetRegSecondaryZonesExpired=NotificationType((1,3,6,1,4,1,9,9,120,2,0,19))
ciscoNetRegSecondaryZonesExpired.setObjects(*((_A,_K),(_A,_P),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:ciscoNetRegSecondaryZonesExpired.setStatus(_B)
ciscoNetRegDnsForwardersNotResp=NotificationType((1,3,6,1,4,1,9,9,120,2,0,20))
ciscoNetRegDnsForwardersNotResp.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoNetRegDnsForwardersNotResp.setStatus(_F)
ciscoNetRegDnsForwardersResp=NotificationType((1,3,6,1,4,1,9,9,120,2,0,21))
ciscoNetRegDnsForwardersResp.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoNetRegDnsForwardersResp.setStatus(_F)
ciscoNetRegHaDnsConfigErr=NotificationType((1,3,6,1,4,1,9,9,120,2,0,22))
ciscoNetRegHaDnsConfigErr.setObjects(*((_A,_G),(_A,_M),(_A,_H)))
if mibBuilder.loadTexts:ciscoNetRegHaDnsConfigErr.setStatus(_B)
ciscoNetRegFailoverSyncFailure=NotificationType((1,3,6,1,4,1,9,9,120,2,0,23))
ciscoNetRegFailoverSyncFailure.setObjects(*((_A,_O),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ciscoNetRegFailoverSyncFailure.setStatus(_B)
ciscoNetworkRegistrarNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,120,3,2,4))
ciscoNetworkRegistrarNotificationsGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_u),(_A,_v),(_A,_w),(_A,_AL),(_A,_x),(_A,_y),(_A,_AM),(_A,_z)))
if mibBuilder.loadTexts:ciscoNetworkRegistrarNotificationsGroup.setStatus(_F)
ciscoNetRegistrarNotificatGroup=NotificationGroup((1,3,6,1,4,1,9,9,120,3,2,7))
ciscoNetRegistrarNotificatGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_AN),(_A,_AO),(_A,_y),(_A,_x),(_A,_AP),(_A,_AQ),(_A,_z),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:ciscoNetRegistrarNotificatGroup.setStatus(_B)
ciscoNetworkRegistrarMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,120,3,1,1))
ciscoNetworkRegistrarMIBCompliance.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:ciscoNetworkRegistrarMIBCompliance.setStatus(_F)
ciscoNetworkRegistrarMIBCompRev1=ModuleCompliance((1,3,6,1,4,1,9,9,120,3,1,2))
ciscoNetworkRegistrarMIBCompRev1.setObjects(*((_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:ciscoNetworkRegistrarMIBCompRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CnrPhysAddress':CnrPhysAddress,'ciscoNetworkRegistrarMIB':ciscoNetworkRegistrarMIB,'ciscoNetworkRegistrarMIBObjects':ciscoNetworkRegistrarMIBObjects,'cnrDHCP':cnrDHCP,'cnrDHCPScopeTable':cnrDHCPScopeTable,'cnrDHCPScopeEntry':cnrDHCPScopeEntry,_A0:cnrDHCPScopeName,_d:cnrDHCPScopeFreeAddrLowThreshold,_e:cnrDHCPScopeFreeAddrHighThreshold,_Q:cnrDHCPScopeFreeAddrValue,_R:cnrDHCPScopeFreeAddrUnits,'cnrNotifObjects':cnrNotifObjects,_S:cnrNotifDupIpAddress,_T:cnrNotifMACAddress,_G:cnrNotifServer,_J:cnrNotifServerType,_U:cnrNotifDupIpAddressDetectedBy,_V:cnrNotifContestedIpAddress,_l:cnrNotifDHCPScopeFreeAddrLow,_m:cnrNotifDHCPScopeFreeAddrHigh,_W:cnrNotifDHCPScopeFreeAddrValue,_X:cnrNotifDHCPThresholdType,_Y:cnrNotifDHCPThresholdValue,_Z:cnrNotifDHCPScopeName,_a:cnrNotifPrimarySubnetNumber,_b:cnrNotifRelatedServerType,_K:cnrNotifDnsServerIpAddress,_M:cnrNotifZoneName,_L:cnrNotifDnsRemoteServersList,_H:cnrNotifIPv6Server,_O:cnrNotifFailoverPairName,_n:cnrNotifFailoverCfgErrType,_P:cnrNotifDnsServerIp6Address,_o:cnrNotifMainIPAddress,_p:cnrNotifMainIPv6Address,_q:cnrNotifBackupIPAddress,_r:cnrNotifBackupIPv6Address,_s:cnrNotifSyncDirection,_t:cnrNotifSyncError,'cnrNotifCfgObjects':cnrNotifCfgObjects,_A2:cnrEnableFreeAddressLow,_A3:cnrEnableFreeAddressHigh,_f:cnrEnableServerStart,_g:cnrEnableServerStop,_h:cnrEnableDNSQueueTooBig,_A4:cnrEnableOtherServerNotResponding,_i:cnrEnableDuplicateAddress,_j:cnrEnableAddressConflict,_A5:cnrEnableOtherServerResponding,_k:cnrEnableFailoverConfigMismatch,_A6:cnrEnableFreeAddrLow,_A7:cnrEnableFreeAddrHigh,_A8:cnrEnableOtherServerNotResp,_A9:cnrEnableOtherServerResp,_AA:cnrEnableHaDnsPartnerDown,_AB:cnrEnableHaDnsPartnerUp,_AC:cnrEnableMastersNotResp,_AD:cnrEnableMastersResp,_AE:cnrEnableSecondaryZoneExpired,_AF:cnrEnableDnsForwardersNotResp,_AG:cnrEnableDnsForwardersResp,_AH:cnrEnableHaDnsConfigErr,_AI:cnrEnableFailoverSyncFailure,'ciscoNetRegMIBNotificationPrefix':ciscoNetRegMIBNotificationPrefix,'ciscoNetRegMIBNotifications':ciscoNetRegMIBNotifications,_AJ:ciscoNetRegFreeAddressLow,_AK:ciscoNetRegFreeAddressHigh,_u:ciscoNetRegServerStart,_v:ciscoNetRegServerStop,_w:ciscoNetRegDNSQueueTooBig,_AL:ciscoNetRegOtherServerNotResponding,_x:ciscoNetRegDuplicateAddress,_y:ciscoNetRegAddressConflict,_AM:ciscoNetRegOtherServerResponding,_z:ciscoNetRegFailoverConfigMismatch,_AN:ciscoNetRegFreeAddrLowThreshold,_AO:ciscoNetRegFreeAddrHighThreshold,_AP:ciscoNetRegOtherServerNotResp,_AQ:ciscoNetRegOtherServerResp,_AR:ciscoNetRegHaDnsPartnerDown,_AS:ciscoNetRegHaDnsPartnerUp,_AT:ciscoNetRegMastersNotResp,_AU:ciscoNetRegMastersResp,_AV:ciscoNetRegSecondaryZonesExpired,_AW:ciscoNetRegDnsForwardersNotResp,_AX:ciscoNetRegDnsForwardersResp,_AY:ciscoNetRegHaDnsConfigErr,_AZ:ciscoNetRegFailoverSyncFailure,'ciscoNetworkRegistrarMIBConformance':ciscoNetworkRegistrarMIBConformance,'ciscoNetworkRegistrarMIBCompliances':ciscoNetworkRegistrarMIBCompliances,'ciscoNetworkRegistrarMIBCompliance':ciscoNetworkRegistrarMIBCompliance,'ciscoNetworkRegistrarMIBCompRev1':ciscoNetworkRegistrarMIBCompRev1,'ciscoNetworkRegistrarMIBGroups':ciscoNetworkRegistrarMIBGroups,_Aa:ciscoNetworkRegistrarDHCPScopeObjectsGroup,_Ab:ciscoNetworkRegistrarNotifObjectsGroup,_Ac:ciscoNetworkRegistrarNotifCfgObjectsGroup,'ciscoNetworkRegistrarNotificationsGroup':ciscoNetworkRegistrarNotificationsGroup,_Ad:ciscoNetRegistrarNotifInfoGroup,_Ae:ciscoNetRegistrarNotEnableGroup,_Af:ciscoNetRegistrarNotificatGroup})