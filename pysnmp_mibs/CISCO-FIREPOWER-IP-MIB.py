_J='cfprIpServiceIfInstanceId'
_I='cfprIpIpV4StaticTargetAddrInstanceId'
_H='cfprIpIpV4StaticAddrInstanceId'
_G='cfprIpIPv4WinsServerInstanceId'
_F='cfprIpIPv4DnsInstanceId'
_E='cfprIpDnsSuffixInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-IP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprIpIPv4DnsPref,CfprIpIpV4StaticAddrPref,CfprIpServiceIfPref=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprIpIPv4DnsPref','CfprIpIpV4StaticAddrPref','CfprIpServiceIfPref')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprIpObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,40))
_CfprIpDnsSuffixTable_Object=MibTable
cfprIpDnsSuffixTable=_CfprIpDnsSuffixTable_Object((1,3,6,1,4,1,9,9,826,1,40,1))
if mibBuilder.loadTexts:cfprIpDnsSuffixTable.setStatus(_A)
_CfprIpDnsSuffixEntry_Object=MibTableRow
cfprIpDnsSuffixEntry=_CfprIpDnsSuffixEntry_Object((1,3,6,1,4,1,9,9,826,1,40,1,1))
cfprIpDnsSuffixEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprIpDnsSuffixEntry.setStatus(_A)
_CfprIpDnsSuffixInstanceId_Type=CfprManagedObjectId
_CfprIpDnsSuffixInstanceId_Object=MibTableColumn
cfprIpDnsSuffixInstanceId=_CfprIpDnsSuffixInstanceId_Object((1,3,6,1,4,1,9,9,826,1,40,1,1,1),_CfprIpDnsSuffixInstanceId_Type())
cfprIpDnsSuffixInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIpDnsSuffixInstanceId.setStatus(_A)
_CfprIpDnsSuffixDn_Type=CfprManagedObjectDn
_CfprIpDnsSuffixDn_Object=MibTableColumn
cfprIpDnsSuffixDn=_CfprIpDnsSuffixDn_Object((1,3,6,1,4,1,9,9,826,1,40,1,1,2),_CfprIpDnsSuffixDn_Type())
cfprIpDnsSuffixDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpDnsSuffixDn.setStatus(_A)
_CfprIpDnsSuffixRn_Type=SnmpAdminString
_CfprIpDnsSuffixRn_Object=MibTableColumn
cfprIpDnsSuffixRn=_CfprIpDnsSuffixRn_Object((1,3,6,1,4,1,9,9,826,1,40,1,1,3),_CfprIpDnsSuffixRn_Type())
cfprIpDnsSuffixRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpDnsSuffixRn.setStatus(_A)
_CfprIpDnsSuffixGuid_Type=SnmpAdminString
_CfprIpDnsSuffixGuid_Object=MibTableColumn
cfprIpDnsSuffixGuid=_CfprIpDnsSuffixGuid_Object((1,3,6,1,4,1,9,9,826,1,40,1,1,4),_CfprIpDnsSuffixGuid_Type())
cfprIpDnsSuffixGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpDnsSuffixGuid.setStatus(_A)
_CfprIpDnsSuffixHost_Type=SnmpAdminString
_CfprIpDnsSuffixHost_Object=MibTableColumn
cfprIpDnsSuffixHost=_CfprIpDnsSuffixHost_Object((1,3,6,1,4,1,9,9,826,1,40,1,1,5),_CfprIpDnsSuffixHost_Type())
cfprIpDnsSuffixHost.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpDnsSuffixHost.setStatus(_A)
_CfprIpDnsSuffixName_Type=SnmpAdminString
_CfprIpDnsSuffixName_Object=MibTableColumn
cfprIpDnsSuffixName=_CfprIpDnsSuffixName_Object((1,3,6,1,4,1,9,9,826,1,40,1,1,6),_CfprIpDnsSuffixName_Type())
cfprIpDnsSuffixName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpDnsSuffixName.setStatus(_A)
_CfprIpIPv4DnsTable_Object=MibTable
cfprIpIPv4DnsTable=_CfprIpIPv4DnsTable_Object((1,3,6,1,4,1,9,9,826,1,40,2))
if mibBuilder.loadTexts:cfprIpIPv4DnsTable.setStatus(_A)
_CfprIpIPv4DnsEntry_Object=MibTableRow
cfprIpIPv4DnsEntry=_CfprIpIPv4DnsEntry_Object((1,3,6,1,4,1,9,9,826,1,40,2,1))
cfprIpIPv4DnsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprIpIPv4DnsEntry.setStatus(_A)
_CfprIpIPv4DnsInstanceId_Type=CfprManagedObjectId
_CfprIpIPv4DnsInstanceId_Object=MibTableColumn
cfprIpIPv4DnsInstanceId=_CfprIpIPv4DnsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,40,2,1,1),_CfprIpIPv4DnsInstanceId_Type())
cfprIpIPv4DnsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIpIPv4DnsInstanceId.setStatus(_A)
_CfprIpIPv4DnsDn_Type=CfprManagedObjectDn
_CfprIpIPv4DnsDn_Object=MibTableColumn
cfprIpIPv4DnsDn=_CfprIpIPv4DnsDn_Object((1,3,6,1,4,1,9,9,826,1,40,2,1,2),_CfprIpIPv4DnsDn_Type())
cfprIpIPv4DnsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4DnsDn.setStatus(_A)
_CfprIpIPv4DnsRn_Type=SnmpAdminString
_CfprIpIPv4DnsRn_Object=MibTableColumn
cfprIpIPv4DnsRn=_CfprIpIPv4DnsRn_Object((1,3,6,1,4,1,9,9,826,1,40,2,1,3),_CfprIpIPv4DnsRn_Type())
cfprIpIPv4DnsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4DnsRn.setStatus(_A)
_CfprIpIPv4DnsAddr_Type=InetAddressIPv4
_CfprIpIPv4DnsAddr_Object=MibTableColumn
cfprIpIPv4DnsAddr=_CfprIpIPv4DnsAddr_Object((1,3,6,1,4,1,9,9,826,1,40,2,1,4),_CfprIpIPv4DnsAddr_Type())
cfprIpIPv4DnsAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4DnsAddr.setStatus(_A)
_CfprIpIPv4DnsDefGw_Type=InetAddressIPv4
_CfprIpIPv4DnsDefGw_Object=MibTableColumn
cfprIpIPv4DnsDefGw=_CfprIpIPv4DnsDefGw_Object((1,3,6,1,4,1,9,9,826,1,40,2,1,5),_CfprIpIPv4DnsDefGw_Type())
cfprIpIPv4DnsDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4DnsDefGw.setStatus(_A)
_CfprIpIPv4DnsPref_Type=CfprIpIPv4DnsPref
_CfprIpIPv4DnsPref_Object=MibTableColumn
cfprIpIPv4DnsPref=_CfprIpIPv4DnsPref_Object((1,3,6,1,4,1,9,9,826,1,40,2,1,6),_CfprIpIPv4DnsPref_Type())
cfprIpIPv4DnsPref.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4DnsPref.setStatus(_A)
_CfprIpIPv4DnsSubnet_Type=InetAddressIPv4
_CfprIpIPv4DnsSubnet_Object=MibTableColumn
cfprIpIPv4DnsSubnet=_CfprIpIPv4DnsSubnet_Object((1,3,6,1,4,1,9,9,826,1,40,2,1,7),_CfprIpIPv4DnsSubnet_Type())
cfprIpIPv4DnsSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4DnsSubnet.setStatus(_A)
_CfprIpIPv4WinsServerTable_Object=MibTable
cfprIpIPv4WinsServerTable=_CfprIpIPv4WinsServerTable_Object((1,3,6,1,4,1,9,9,826,1,40,3))
if mibBuilder.loadTexts:cfprIpIPv4WinsServerTable.setStatus(_A)
_CfprIpIPv4WinsServerEntry_Object=MibTableRow
cfprIpIPv4WinsServerEntry=_CfprIpIPv4WinsServerEntry_Object((1,3,6,1,4,1,9,9,826,1,40,3,1))
cfprIpIPv4WinsServerEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprIpIPv4WinsServerEntry.setStatus(_A)
_CfprIpIPv4WinsServerInstanceId_Type=CfprManagedObjectId
_CfprIpIPv4WinsServerInstanceId_Object=MibTableColumn
cfprIpIPv4WinsServerInstanceId=_CfprIpIPv4WinsServerInstanceId_Object((1,3,6,1,4,1,9,9,826,1,40,3,1,1),_CfprIpIPv4WinsServerInstanceId_Type())
cfprIpIPv4WinsServerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIpIPv4WinsServerInstanceId.setStatus(_A)
_CfprIpIPv4WinsServerDn_Type=CfprManagedObjectDn
_CfprIpIPv4WinsServerDn_Object=MibTableColumn
cfprIpIPv4WinsServerDn=_CfprIpIPv4WinsServerDn_Object((1,3,6,1,4,1,9,9,826,1,40,3,1,2),_CfprIpIPv4WinsServerDn_Type())
cfprIpIPv4WinsServerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4WinsServerDn.setStatus(_A)
_CfprIpIPv4WinsServerRn_Type=SnmpAdminString
_CfprIpIPv4WinsServerRn_Object=MibTableColumn
cfprIpIPv4WinsServerRn=_CfprIpIPv4WinsServerRn_Object((1,3,6,1,4,1,9,9,826,1,40,3,1,3),_CfprIpIPv4WinsServerRn_Type())
cfprIpIPv4WinsServerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4WinsServerRn.setStatus(_A)
_CfprIpIPv4WinsServerIPv4Address_Type=InetAddressIPv4
_CfprIpIPv4WinsServerIPv4Address_Object=MibTableColumn
cfprIpIPv4WinsServerIPv4Address=_CfprIpIPv4WinsServerIPv4Address_Object((1,3,6,1,4,1,9,9,826,1,40,3,1,4),_CfprIpIPv4WinsServerIPv4Address_Type())
cfprIpIPv4WinsServerIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4WinsServerIPv4Address.setStatus(_A)
_CfprIpIPv4WinsServerGuid_Type=SnmpAdminString
_CfprIpIPv4WinsServerGuid_Object=MibTableColumn
cfprIpIPv4WinsServerGuid=_CfprIpIPv4WinsServerGuid_Object((1,3,6,1,4,1,9,9,826,1,40,3,1,5),_CfprIpIPv4WinsServerGuid_Type())
cfprIpIPv4WinsServerGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4WinsServerGuid.setStatus(_A)
_CfprIpIPv4WinsServerHost_Type=SnmpAdminString
_CfprIpIPv4WinsServerHost_Object=MibTableColumn
cfprIpIPv4WinsServerHost=_CfprIpIPv4WinsServerHost_Object((1,3,6,1,4,1,9,9,826,1,40,3,1,6),_CfprIpIPv4WinsServerHost_Type())
cfprIpIPv4WinsServerHost.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4WinsServerHost.setStatus(_A)
_CfprIpIPv4WinsServerName_Type=SnmpAdminString
_CfprIpIPv4WinsServerName_Object=MibTableColumn
cfprIpIPv4WinsServerName=_CfprIpIPv4WinsServerName_Object((1,3,6,1,4,1,9,9,826,1,40,3,1,7),_CfprIpIPv4WinsServerName_Type())
cfprIpIPv4WinsServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIPv4WinsServerName.setStatus(_A)
_CfprIpIpV4StaticAddrTable_Object=MibTable
cfprIpIpV4StaticAddrTable=_CfprIpIpV4StaticAddrTable_Object((1,3,6,1,4,1,9,9,826,1,40,4))
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrTable.setStatus(_A)
_CfprIpIpV4StaticAddrEntry_Object=MibTableRow
cfprIpIpV4StaticAddrEntry=_CfprIpIpV4StaticAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,40,4,1))
cfprIpIpV4StaticAddrEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrEntry.setStatus(_A)
_CfprIpIpV4StaticAddrInstanceId_Type=CfprManagedObjectId
_CfprIpIpV4StaticAddrInstanceId_Object=MibTableColumn
cfprIpIpV4StaticAddrInstanceId=_CfprIpIpV4StaticAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,40,4,1,1),_CfprIpIpV4StaticAddrInstanceId_Type())
cfprIpIpV4StaticAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrInstanceId.setStatus(_A)
_CfprIpIpV4StaticAddrDn_Type=CfprManagedObjectDn
_CfprIpIpV4StaticAddrDn_Object=MibTableColumn
cfprIpIpV4StaticAddrDn=_CfprIpIpV4StaticAddrDn_Object((1,3,6,1,4,1,9,9,826,1,40,4,1,2),_CfprIpIpV4StaticAddrDn_Type())
cfprIpIpV4StaticAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrDn.setStatus(_A)
_CfprIpIpV4StaticAddrRn_Type=SnmpAdminString
_CfprIpIpV4StaticAddrRn_Object=MibTableColumn
cfprIpIpV4StaticAddrRn=_CfprIpIpV4StaticAddrRn_Object((1,3,6,1,4,1,9,9,826,1,40,4,1,3),_CfprIpIpV4StaticAddrRn_Type())
cfprIpIpV4StaticAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrRn.setStatus(_A)
_CfprIpIpV4StaticAddrAddr_Type=InetAddressIPv4
_CfprIpIpV4StaticAddrAddr_Object=MibTableColumn
cfprIpIpV4StaticAddrAddr=_CfprIpIpV4StaticAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,40,4,1,4),_CfprIpIpV4StaticAddrAddr_Type())
cfprIpIpV4StaticAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrAddr.setStatus(_A)
_CfprIpIpV4StaticAddrDefGw_Type=InetAddressIPv4
_CfprIpIpV4StaticAddrDefGw_Object=MibTableColumn
cfprIpIpV4StaticAddrDefGw=_CfprIpIpV4StaticAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,40,4,1,5),_CfprIpIpV4StaticAddrDefGw_Type())
cfprIpIpV4StaticAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrDefGw.setStatus(_A)
_CfprIpIpV4StaticAddrPref_Type=CfprIpIpV4StaticAddrPref
_CfprIpIpV4StaticAddrPref_Object=MibTableColumn
cfprIpIpV4StaticAddrPref=_CfprIpIpV4StaticAddrPref_Object((1,3,6,1,4,1,9,9,826,1,40,4,1,6),_CfprIpIpV4StaticAddrPref_Type())
cfprIpIpV4StaticAddrPref.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrPref.setStatus(_A)
_CfprIpIpV4StaticAddrSubnet_Type=InetAddressIPv4
_CfprIpIpV4StaticAddrSubnet_Object=MibTableColumn
cfprIpIpV4StaticAddrSubnet=_CfprIpIpV4StaticAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,40,4,1,7),_CfprIpIpV4StaticAddrSubnet_Type())
cfprIpIpV4StaticAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticAddrSubnet.setStatus(_A)
_CfprIpIpV4StaticTargetAddrTable_Object=MibTable
cfprIpIpV4StaticTargetAddrTable=_CfprIpIpV4StaticTargetAddrTable_Object((1,3,6,1,4,1,9,9,826,1,40,5))
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrTable.setStatus(_A)
_CfprIpIpV4StaticTargetAddrEntry_Object=MibTableRow
cfprIpIpV4StaticTargetAddrEntry=_CfprIpIpV4StaticTargetAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,40,5,1))
cfprIpIpV4StaticTargetAddrEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrEntry.setStatus(_A)
_CfprIpIpV4StaticTargetAddrInstanceId_Type=CfprManagedObjectId
_CfprIpIpV4StaticTargetAddrInstanceId_Object=MibTableColumn
cfprIpIpV4StaticTargetAddrInstanceId=_CfprIpIpV4StaticTargetAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,40,5,1,1),_CfprIpIpV4StaticTargetAddrInstanceId_Type())
cfprIpIpV4StaticTargetAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrInstanceId.setStatus(_A)
_CfprIpIpV4StaticTargetAddrDn_Type=CfprManagedObjectDn
_CfprIpIpV4StaticTargetAddrDn_Object=MibTableColumn
cfprIpIpV4StaticTargetAddrDn=_CfprIpIpV4StaticTargetAddrDn_Object((1,3,6,1,4,1,9,9,826,1,40,5,1,2),_CfprIpIpV4StaticTargetAddrDn_Type())
cfprIpIpV4StaticTargetAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrDn.setStatus(_A)
_CfprIpIpV4StaticTargetAddrRn_Type=SnmpAdminString
_CfprIpIpV4StaticTargetAddrRn_Object=MibTableColumn
cfprIpIpV4StaticTargetAddrRn=_CfprIpIpV4StaticTargetAddrRn_Object((1,3,6,1,4,1,9,9,826,1,40,5,1,3),_CfprIpIpV4StaticTargetAddrRn_Type())
cfprIpIpV4StaticTargetAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrRn.setStatus(_A)
_CfprIpIpV4StaticTargetAddrAddr_Type=InetAddressIPv4
_CfprIpIpV4StaticTargetAddrAddr_Object=MibTableColumn
cfprIpIpV4StaticTargetAddrAddr=_CfprIpIpV4StaticTargetAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,40,5,1,4),_CfprIpIpV4StaticTargetAddrAddr_Type())
cfprIpIpV4StaticTargetAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrAddr.setStatus(_A)
_CfprIpIpV4StaticTargetAddrDefGw_Type=InetAddressIPv4
_CfprIpIpV4StaticTargetAddrDefGw_Object=MibTableColumn
cfprIpIpV4StaticTargetAddrDefGw=_CfprIpIpV4StaticTargetAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,40,5,1,5),_CfprIpIpV4StaticTargetAddrDefGw_Type())
cfprIpIpV4StaticTargetAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrDefGw.setStatus(_A)
_CfprIpIpV4StaticTargetAddrSubnet_Type=InetAddressIPv4
_CfprIpIpV4StaticTargetAddrSubnet_Object=MibTableColumn
cfprIpIpV4StaticTargetAddrSubnet=_CfprIpIpV4StaticTargetAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,40,5,1,6),_CfprIpIpV4StaticTargetAddrSubnet_Type())
cfprIpIpV4StaticTargetAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpIpV4StaticTargetAddrSubnet.setStatus(_A)
_CfprIpServiceIfTable_Object=MibTable
cfprIpServiceIfTable=_CfprIpServiceIfTable_Object((1,3,6,1,4,1,9,9,826,1,40,6))
if mibBuilder.loadTexts:cfprIpServiceIfTable.setStatus(_A)
_CfprIpServiceIfEntry_Object=MibTableRow
cfprIpServiceIfEntry=_CfprIpServiceIfEntry_Object((1,3,6,1,4,1,9,9,826,1,40,6,1))
cfprIpServiceIfEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprIpServiceIfEntry.setStatus(_A)
_CfprIpServiceIfInstanceId_Type=CfprManagedObjectId
_CfprIpServiceIfInstanceId_Object=MibTableColumn
cfprIpServiceIfInstanceId=_CfprIpServiceIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,1),_CfprIpServiceIfInstanceId_Type())
cfprIpServiceIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIpServiceIfInstanceId.setStatus(_A)
_CfprIpServiceIfDn_Type=CfprManagedObjectDn
_CfprIpServiceIfDn_Object=MibTableColumn
cfprIpServiceIfDn=_CfprIpServiceIfDn_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,2),_CfprIpServiceIfDn_Type())
cfprIpServiceIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpServiceIfDn.setStatus(_A)
_CfprIpServiceIfRn_Type=SnmpAdminString
_CfprIpServiceIfRn_Object=MibTableColumn
cfprIpServiceIfRn=_CfprIpServiceIfRn_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,3),_CfprIpServiceIfRn_Type())
cfprIpServiceIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpServiceIfRn.setStatus(_A)
_CfprIpServiceIfAddr_Type=InetAddressIPv4
_CfprIpServiceIfAddr_Object=MibTableColumn
cfprIpServiceIfAddr=_CfprIpServiceIfAddr_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,4),_CfprIpServiceIfAddr_Type())
cfprIpServiceIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpServiceIfAddr.setStatus(_A)
_CfprIpServiceIfDefGw_Type=InetAddressIPv4
_CfprIpServiceIfDefGw_Object=MibTableColumn
cfprIpServiceIfDefGw=_CfprIpServiceIfDefGw_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,5),_CfprIpServiceIfDefGw_Type())
cfprIpServiceIfDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpServiceIfDefGw.setStatus(_A)
_CfprIpServiceIfPort_Type=Gauge32
_CfprIpServiceIfPort_Object=MibTableColumn
cfprIpServiceIfPort=_CfprIpServiceIfPort_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,6),_CfprIpServiceIfPort_Type())
cfprIpServiceIfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpServiceIfPort.setStatus(_A)
_CfprIpServiceIfPref_Type=CfprIpServiceIfPref
_CfprIpServiceIfPref_Object=MibTableColumn
cfprIpServiceIfPref=_CfprIpServiceIfPref_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,7),_CfprIpServiceIfPref_Type())
cfprIpServiceIfPref.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpServiceIfPref.setStatus(_A)
_CfprIpServiceIfSubnet_Type=InetAddressIPv4
_CfprIpServiceIfSubnet_Object=MibTableColumn
cfprIpServiceIfSubnet=_CfprIpServiceIfSubnet_Object((1,3,6,1,4,1,9,9,826,1,40,6,1,8),_CfprIpServiceIfSubnet_Type())
cfprIpServiceIfSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIpServiceIfSubnet.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprIpObjects':cfprIpObjects,'cfprIpDnsSuffixTable':cfprIpDnsSuffixTable,'cfprIpDnsSuffixEntry':cfprIpDnsSuffixEntry,_E:cfprIpDnsSuffixInstanceId,'cfprIpDnsSuffixDn':cfprIpDnsSuffixDn,'cfprIpDnsSuffixRn':cfprIpDnsSuffixRn,'cfprIpDnsSuffixGuid':cfprIpDnsSuffixGuid,'cfprIpDnsSuffixHost':cfprIpDnsSuffixHost,'cfprIpDnsSuffixName':cfprIpDnsSuffixName,'cfprIpIPv4DnsTable':cfprIpIPv4DnsTable,'cfprIpIPv4DnsEntry':cfprIpIPv4DnsEntry,_F:cfprIpIPv4DnsInstanceId,'cfprIpIPv4DnsDn':cfprIpIPv4DnsDn,'cfprIpIPv4DnsRn':cfprIpIPv4DnsRn,'cfprIpIPv4DnsAddr':cfprIpIPv4DnsAddr,'cfprIpIPv4DnsDefGw':cfprIpIPv4DnsDefGw,'cfprIpIPv4DnsPref':cfprIpIPv4DnsPref,'cfprIpIPv4DnsSubnet':cfprIpIPv4DnsSubnet,'cfprIpIPv4WinsServerTable':cfprIpIPv4WinsServerTable,'cfprIpIPv4WinsServerEntry':cfprIpIPv4WinsServerEntry,_G:cfprIpIPv4WinsServerInstanceId,'cfprIpIPv4WinsServerDn':cfprIpIPv4WinsServerDn,'cfprIpIPv4WinsServerRn':cfprIpIPv4WinsServerRn,'cfprIpIPv4WinsServerIPv4Address':cfprIpIPv4WinsServerIPv4Address,'cfprIpIPv4WinsServerGuid':cfprIpIPv4WinsServerGuid,'cfprIpIPv4WinsServerHost':cfprIpIPv4WinsServerHost,'cfprIpIPv4WinsServerName':cfprIpIPv4WinsServerName,'cfprIpIpV4StaticAddrTable':cfprIpIpV4StaticAddrTable,'cfprIpIpV4StaticAddrEntry':cfprIpIpV4StaticAddrEntry,_H:cfprIpIpV4StaticAddrInstanceId,'cfprIpIpV4StaticAddrDn':cfprIpIpV4StaticAddrDn,'cfprIpIpV4StaticAddrRn':cfprIpIpV4StaticAddrRn,'cfprIpIpV4StaticAddrAddr':cfprIpIpV4StaticAddrAddr,'cfprIpIpV4StaticAddrDefGw':cfprIpIpV4StaticAddrDefGw,'cfprIpIpV4StaticAddrPref':cfprIpIpV4StaticAddrPref,'cfprIpIpV4StaticAddrSubnet':cfprIpIpV4StaticAddrSubnet,'cfprIpIpV4StaticTargetAddrTable':cfprIpIpV4StaticTargetAddrTable,'cfprIpIpV4StaticTargetAddrEntry':cfprIpIpV4StaticTargetAddrEntry,_I:cfprIpIpV4StaticTargetAddrInstanceId,'cfprIpIpV4StaticTargetAddrDn':cfprIpIpV4StaticTargetAddrDn,'cfprIpIpV4StaticTargetAddrRn':cfprIpIpV4StaticTargetAddrRn,'cfprIpIpV4StaticTargetAddrAddr':cfprIpIpV4StaticTargetAddrAddr,'cfprIpIpV4StaticTargetAddrDefGw':cfprIpIpV4StaticTargetAddrDefGw,'cfprIpIpV4StaticTargetAddrSubnet':cfprIpIpV4StaticTargetAddrSubnet,'cfprIpServiceIfTable':cfprIpServiceIfTable,'cfprIpServiceIfEntry':cfprIpServiceIfEntry,_J:cfprIpServiceIfInstanceId,'cfprIpServiceIfDn':cfprIpServiceIfDn,'cfprIpServiceIfRn':cfprIpServiceIfRn,'cfprIpServiceIfAddr':cfprIpServiceIfAddr,'cfprIpServiceIfDefGw':cfprIpServiceIfDefGw,'cfprIpServiceIfPort':cfprIpServiceIfPort,'cfprIpServiceIfPref':cfprIpServiceIfPref,'cfprIpServiceIfSubnet':cfprIpServiceIfSubnet})