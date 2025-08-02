_O='sysName'
_N='SNMPv2-MIB'
_M='ifDescr'
_L='adTrapInformSeqNum'
_K='ADTRAN-GENTRAPINFORM-MIB'
_J='adGenSlotInfoIndex'
_I='ADTRAN-GENSLOT-MIB'
_H='TruthValue'
_G='DisplayString'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_I,_J)
adTrapInformSeqNum,=mibBuilder.importSymbols(_K,_L)
adGenSubtendedHost,adGenSubtendedHostID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenSubtendedHost','adGenSubtendedHostID')
AdGenTrapVersion,=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-TC-MIB','AdGenTrapVersion')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_M,_E)
InetAddressIPv4,InetAddressIPv6,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','TextualConvention',_H)
adGenSubtendedHostMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,12,1))
if mibBuilder.loadTexts:adGenSubtendedHostMIB.setRevisions(('2015-08-21 00:00','2015-05-27 00:00','2015-03-06 00:00','2014-05-16 00:00','2009-03-09 00:00'))
_AdGenSubtendedHostProvisioning_ObjectIdentity=ObjectIdentity
adGenSubtendedHostProvisioning=_AdGenSubtendedHostProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,12,1))
_AdGenSubHostProvMgmtTable_Object=MibTable
adGenSubHostProvMgmtTable=_AdGenSubHostProvMgmtTable_Object((1,3,6,1,4,1,664,5,70,12,1,1))
if mibBuilder.loadTexts:adGenSubHostProvMgmtTable.setStatus(_A)
_AdGenSubHostProvMgmtEntry_Object=MibTableRow
adGenSubHostProvMgmtEntry=_AdGenSubHostProvMgmtEntry_Object((1,3,6,1,4,1,664,5,70,12,1,1,1))
adGenSubHostProvMgmtEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenSubHostProvMgmtEntry.setStatus(_A)
_AdGenSubHostProvMgmtIpAddress_Type=IpAddress
_AdGenSubHostProvMgmtIpAddress_Object=MibTableColumn
adGenSubHostProvMgmtIpAddress=_AdGenSubHostProvMgmtIpAddress_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,1),_AdGenSubHostProvMgmtIpAddress_Type())
adGenSubHostProvMgmtIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpAddress.setStatus(_A)
_AdGenSubHostProvMgmtIpSubnetMask_Type=IpAddress
_AdGenSubHostProvMgmtIpSubnetMask_Object=MibTableColumn
adGenSubHostProvMgmtIpSubnetMask=_AdGenSubHostProvMgmtIpSubnetMask_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,2),_AdGenSubHostProvMgmtIpSubnetMask_Type())
adGenSubHostProvMgmtIpSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpSubnetMask.setStatus(_A)
_AdGenSubHostProvMgmtIpGateway_Type=IpAddress
_AdGenSubHostProvMgmtIpGateway_Object=MibTableColumn
adGenSubHostProvMgmtIpGateway=_AdGenSubHostProvMgmtIpGateway_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,3),_AdGenSubHostProvMgmtIpGateway_Type())
adGenSubHostProvMgmtIpGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpGateway.setStatus(_A)
_AdGenSubHostProvMgmtIpVlan_Type=Integer32
_AdGenSubHostProvMgmtIpVlan_Object=MibTableColumn
adGenSubHostProvMgmtIpVlan=_AdGenSubHostProvMgmtIpVlan_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,4),_AdGenSubHostProvMgmtIpVlan_Type())
adGenSubHostProvMgmtIpVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpVlan.setStatus(_A)
_AdGenSubHostProvMgmtTftpServer_Type=IpAddress
_AdGenSubHostProvMgmtTftpServer_Object=MibTableColumn
adGenSubHostProvMgmtTftpServer=_AdGenSubHostProvMgmtTftpServer_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,5),_AdGenSubHostProvMgmtTftpServer_Type())
adGenSubHostProvMgmtTftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtTftpServer.setStatus(_A)
_AdGenSubHostProvMgmtSnmpWriteCommunity_Type=DisplayString
_AdGenSubHostProvMgmtSnmpWriteCommunity_Object=MibTableColumn
adGenSubHostProvMgmtSnmpWriteCommunity=_AdGenSubHostProvMgmtSnmpWriteCommunity_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,6),_AdGenSubHostProvMgmtSnmpWriteCommunity_Type())
adGenSubHostProvMgmtSnmpWriteCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtSnmpWriteCommunity.setStatus(_A)
_AdGenSubHostProvMgmtSnmpReadCommunity_Type=DisplayString
_AdGenSubHostProvMgmtSnmpReadCommunity_Object=MibTableColumn
adGenSubHostProvMgmtSnmpReadCommunity=_AdGenSubHostProvMgmtSnmpReadCommunity_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,7),_AdGenSubHostProvMgmtSnmpReadCommunity_Type())
adGenSubHostProvMgmtSnmpReadCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtSnmpReadCommunity.setStatus(_A)
_AdGenSubHostProvMgmtSysName_Type=DisplayString
_AdGenSubHostProvMgmtSysName_Object=MibTableColumn
adGenSubHostProvMgmtSysName=_AdGenSubHostProvMgmtSysName_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,8),_AdGenSubHostProvMgmtSysName_Type())
adGenSubHostProvMgmtSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtSysName.setStatus(_A)
_AdGenSubHostProvMgmtPriority_Type=Integer32
_AdGenSubHostProvMgmtPriority_Object=MibTableColumn
adGenSubHostProvMgmtPriority=_AdGenSubHostProvMgmtPriority_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,9),_AdGenSubHostProvMgmtPriority_Type())
adGenSubHostProvMgmtPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtPriority.setStatus(_A)
class _AdGenSubHostProvMgmtIpAssignMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_AdGenSubHostProvMgmtIpAssignMode_Type.__name__=_F
_AdGenSubHostProvMgmtIpAssignMode_Object=MibTableColumn
adGenSubHostProvMgmtIpAssignMode=_AdGenSubHostProvMgmtIpAssignMode_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,10),_AdGenSubHostProvMgmtIpAssignMode_Type())
adGenSubHostProvMgmtIpAssignMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpAssignMode.setStatus(_A)
class _AdGenSubHostProvMgmtSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('resync',1),('reset',2)))
_AdGenSubHostProvMgmtSync_Type.__name__=_F
_AdGenSubHostProvMgmtSync_Object=MibTableColumn
adGenSubHostProvMgmtSync=_AdGenSubHostProvMgmtSync_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,11),_AdGenSubHostProvMgmtSync_Type())
adGenSubHostProvMgmtSync.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtSync.setStatus(_A)
_AdGenSubHostProvMgmtSnmpSysLocation_Type=DisplayString
_AdGenSubHostProvMgmtSnmpSysLocation_Object=MibTableColumn
adGenSubHostProvMgmtSnmpSysLocation=_AdGenSubHostProvMgmtSnmpSysLocation_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,12),_AdGenSubHostProvMgmtSnmpSysLocation_Type())
adGenSubHostProvMgmtSnmpSysLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtSnmpSysLocation.setStatus(_A)
_AdGenSubHostProvMgmtEzProvHostOneIpAddress_Type=IpAddress
_AdGenSubHostProvMgmtEzProvHostOneIpAddress_Object=MibTableColumn
adGenSubHostProvMgmtEzProvHostOneIpAddress=_AdGenSubHostProvMgmtEzProvHostOneIpAddress_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,13),_AdGenSubHostProvMgmtEzProvHostOneIpAddress_Type())
adGenSubHostProvMgmtEzProvHostOneIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtEzProvHostOneIpAddress.setStatus(_A)
_AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Type=AdGenTrapVersion
_AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Object=MibTableColumn
adGenSubHostProvMgmtEzProvHostOneTrapVersion=_AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,14),_AdGenSubHostProvMgmtEzProvHostOneTrapVersion_Type())
adGenSubHostProvMgmtEzProvHostOneTrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtEzProvHostOneTrapVersion.setStatus(_A)
_AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Type=IpAddress
_AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Object=MibTableColumn
adGenSubHostProvMgmtEzProvHostTwoIpAddress=_AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,15),_AdGenSubHostProvMgmtEzProvHostTwoIpAddress_Type())
adGenSubHostProvMgmtEzProvHostTwoIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtEzProvHostTwoIpAddress.setStatus(_A)
_AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Type=AdGenTrapVersion
_AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Object=MibTableColumn
adGenSubHostProvMgmtEzProvHostTwoTrapVersion=_AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,16),_AdGenSubHostProvMgmtEzProvHostTwoTrapVersion_Type())
adGenSubHostProvMgmtEzProvHostTwoTrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtEzProvHostTwoTrapVersion.setStatus(_A)
_AdGenSubHostProvMgmtEzProvEnabled_Type=TruthValue
_AdGenSubHostProvMgmtEzProvEnabled_Object=MibTableColumn
adGenSubHostProvMgmtEzProvEnabled=_AdGenSubHostProvMgmtEzProvEnabled_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,17),_AdGenSubHostProvMgmtEzProvEnabled_Type())
adGenSubHostProvMgmtEzProvEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtEzProvEnabled.setStatus(_A)
_AdGenSubHostProvMgmtIpv6AddressPrefixLength_Type=InetAddressPrefixLength
_AdGenSubHostProvMgmtIpv6AddressPrefixLength_Object=MibTableColumn
adGenSubHostProvMgmtIpv6AddressPrefixLength=_AdGenSubHostProvMgmtIpv6AddressPrefixLength_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,18),_AdGenSubHostProvMgmtIpv6AddressPrefixLength_Type())
adGenSubHostProvMgmtIpv6AddressPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpv6AddressPrefixLength.setStatus(_A)
_AdGenSubHostProvMgmtIpv6AddressEui64_Type=TruthValue
_AdGenSubHostProvMgmtIpv6AddressEui64_Object=MibTableColumn
adGenSubHostProvMgmtIpv6AddressEui64=_AdGenSubHostProvMgmtIpv6AddressEui64_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,19),_AdGenSubHostProvMgmtIpv6AddressEui64_Type())
adGenSubHostProvMgmtIpv6AddressEui64.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpv6AddressEui64.setStatus(_A)
_AdGenSubHostProvMgmtIpv6Address_Type=InetAddressIPv6
_AdGenSubHostProvMgmtIpv6Address_Object=MibTableColumn
adGenSubHostProvMgmtIpv6Address=_AdGenSubHostProvMgmtIpv6Address_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,20),_AdGenSubHostProvMgmtIpv6Address_Type())
adGenSubHostProvMgmtIpv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpv6Address.setStatus(_A)
_AdGenSubHostProvMgmtIpv6AddressLinkLocal_Type=InetAddressIPv6
_AdGenSubHostProvMgmtIpv6AddressLinkLocal_Object=MibTableColumn
adGenSubHostProvMgmtIpv6AddressLinkLocal=_AdGenSubHostProvMgmtIpv6AddressLinkLocal_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,21),_AdGenSubHostProvMgmtIpv6AddressLinkLocal_Type())
adGenSubHostProvMgmtIpv6AddressLinkLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtIpv6AddressLinkLocal.setStatus(_A)
class _AdGenSubHostProvMgmtAutoConfigMode_Type(TruthValue):defaultValue=2
_AdGenSubHostProvMgmtAutoConfigMode_Type.__name__=_H
_AdGenSubHostProvMgmtAutoConfigMode_Object=MibTableColumn
adGenSubHostProvMgmtAutoConfigMode=_AdGenSubHostProvMgmtAutoConfigMode_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,22),_AdGenSubHostProvMgmtAutoConfigMode_Type())
adGenSubHostProvMgmtAutoConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtAutoConfigMode.setStatus(_A)
class _AdGenSubHostProvMgmtAutoConfigFilename_Type(DisplayString):defaultValue=OctetString('')
_AdGenSubHostProvMgmtAutoConfigFilename_Type.__name__=_G
_AdGenSubHostProvMgmtAutoConfigFilename_Object=MibTableColumn
adGenSubHostProvMgmtAutoConfigFilename=_AdGenSubHostProvMgmtAutoConfigFilename_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,23),_AdGenSubHostProvMgmtAutoConfigFilename_Type())
adGenSubHostProvMgmtAutoConfigFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtAutoConfigFilename.setStatus(_A)
class _AdGenSubHostProvMgmtAutoConfigGroupName_Type(DisplayString):defaultValue=OctetString('')
_AdGenSubHostProvMgmtAutoConfigGroupName_Type.__name__=_G
_AdGenSubHostProvMgmtAutoConfigGroupName_Object=MibTableColumn
adGenSubHostProvMgmtAutoConfigGroupName=_AdGenSubHostProvMgmtAutoConfigGroupName_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,24),_AdGenSubHostProvMgmtAutoConfigGroupName_Type())
adGenSubHostProvMgmtAutoConfigGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtAutoConfigGroupName.setStatus(_A)
_AdGenSubHostProvMgmtAutoConfigHostIpv4_Type=InetAddressIPv4
_AdGenSubHostProvMgmtAutoConfigHostIpv4_Object=MibTableColumn
adGenSubHostProvMgmtAutoConfigHostIpv4=_AdGenSubHostProvMgmtAutoConfigHostIpv4_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,25),_AdGenSubHostProvMgmtAutoConfigHostIpv4_Type())
adGenSubHostProvMgmtAutoConfigHostIpv4.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtAutoConfigHostIpv4.setStatus(_A)
_AdGenSubHostProvMgmtAutoConfigHostIpv6_Type=InetAddressIPv6
_AdGenSubHostProvMgmtAutoConfigHostIpv6_Object=MibTableColumn
adGenSubHostProvMgmtAutoConfigHostIpv6=_AdGenSubHostProvMgmtAutoConfigHostIpv6_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,26),_AdGenSubHostProvMgmtAutoConfigHostIpv6_Type())
adGenSubHostProvMgmtAutoConfigHostIpv6.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvMgmtAutoConfigHostIpv6.setStatus(_A)
class _AdGenSubHostProvMgmtLastErrorString_Type(DisplayString):defaultValue=OctetString('')
_AdGenSubHostProvMgmtLastErrorString_Type.__name__=_G
_AdGenSubHostProvMgmtLastErrorString_Object=MibTableColumn
adGenSubHostProvMgmtLastErrorString=_AdGenSubHostProvMgmtLastErrorString_Object((1,3,6,1,4,1,664,5,70,12,1,1,1,27),_AdGenSubHostProvMgmtLastErrorString_Type())
adGenSubHostProvMgmtLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostProvMgmtLastErrorString.setStatus(_A)
_AdGenSubHostProvIfTable_Object=MibTable
adGenSubHostProvIfTable=_AdGenSubHostProvIfTable_Object((1,3,6,1,4,1,664,5,70,12,1,2))
if mibBuilder.loadTexts:adGenSubHostProvIfTable.setStatus(_A)
_AdGenSubHostProvIfEntry_Object=MibTableRow
adGenSubHostProvIfEntry=_AdGenSubHostProvIfEntry_Object((1,3,6,1,4,1,664,5,70,12,1,2,1))
adGenSubHostProvIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenSubHostProvIfEntry.setStatus(_A)
class _AdGenSubHostProvIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('listener',2),('sender',3)))
_AdGenSubHostProvIfMode_Type.__name__=_F
_AdGenSubHostProvIfMode_Object=MibTableColumn
adGenSubHostProvIfMode=_AdGenSubHostProvIfMode_Object((1,3,6,1,4,1,664,5,70,12,1,2,1,1),_AdGenSubHostProvIfMode_Type())
adGenSubHostProvIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvIfMode.setStatus(_A)
class _AdGenSubHostProvIfAutoDiscoveryMode_Type(TruthValue):defaultValue=2
_AdGenSubHostProvIfAutoDiscoveryMode_Type.__name__=_H
_AdGenSubHostProvIfAutoDiscoveryMode_Object=MibTableColumn
adGenSubHostProvIfAutoDiscoveryMode=_AdGenSubHostProvIfAutoDiscoveryMode_Object((1,3,6,1,4,1,664,5,70,12,1,2,1,2),_AdGenSubHostProvIfAutoDiscoveryMode_Type())
adGenSubHostProvIfAutoDiscoveryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvIfAutoDiscoveryMode.setStatus(_A)
class _AdGenSubHostProvIfAutoDiscoveryAck_Type(TruthValue):defaultValue=2
_AdGenSubHostProvIfAutoDiscoveryAck_Type.__name__=_H
_AdGenSubHostProvIfAutoDiscoveryAck_Object=MibTableColumn
adGenSubHostProvIfAutoDiscoveryAck=_AdGenSubHostProvIfAutoDiscoveryAck_Object((1,3,6,1,4,1,664,5,70,12,1,2,1,3),_AdGenSubHostProvIfAutoDiscoveryAck_Type())
adGenSubHostProvIfAutoDiscoveryAck.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubHostProvIfAutoDiscoveryAck.setStatus(_A)
_AdGenSubtendedHostStatus_ObjectIdentity=ObjectIdentity
adGenSubtendedHostStatus=_AdGenSubtendedHostStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,12,2))
_AdGenSubHostStatTable_Object=MibTable
adGenSubHostStatTable=_AdGenSubHostStatTable_Object((1,3,6,1,4,1,664,5,70,12,2,1))
if mibBuilder.loadTexts:adGenSubHostStatTable.setStatus(_A)
_AdGenSubHostStatEntry_Object=MibTableRow
adGenSubHostStatEntry=_AdGenSubHostStatEntry_Object((1,3,6,1,4,1,664,5,70,12,2,1,1))
adGenSubHostStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenSubHostStatEntry.setStatus(_A)
_AdGenSubHostStatMacAddress_Type=MacAddress
_AdGenSubHostStatMacAddress_Object=MibTableColumn
adGenSubHostStatMacAddress=_AdGenSubHostStatMacAddress_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,1),_AdGenSubHostStatMacAddress_Type())
adGenSubHostStatMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatMacAddress.setStatus(_A)
_AdGenSubHostStatIpAddress_Type=IpAddress
_AdGenSubHostStatIpAddress_Object=MibTableColumn
adGenSubHostStatIpAddress=_AdGenSubHostStatIpAddress_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,2),_AdGenSubHostStatIpAddress_Type())
adGenSubHostStatIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatIpAddress.setStatus(_A)
_AdGenSubHostStatGateway_Type=IpAddress
_AdGenSubHostStatGateway_Object=MibTableColumn
adGenSubHostStatGateway=_AdGenSubHostStatGateway_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,3),_AdGenSubHostStatGateway_Type())
adGenSubHostStatGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatGateway.setStatus(_A)
_AdGenSubHostStatProvSync_Type=DisplayString
_AdGenSubHostStatProvSync_Object=MibTableColumn
adGenSubHostStatProvSync=_AdGenSubHostStatProvSync_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,4),_AdGenSubHostStatProvSync_Type())
adGenSubHostStatProvSync.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatProvSync.setStatus(_A)
_AdGenSubHostStatIpSubnetMask_Type=IpAddress
_AdGenSubHostStatIpSubnetMask_Object=MibTableColumn
adGenSubHostStatIpSubnetMask=_AdGenSubHostStatIpSubnetMask_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,5),_AdGenSubHostStatIpSubnetMask_Type())
adGenSubHostStatIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatIpSubnetMask.setStatus(_A)
_AdGenSubHostStatIpv6AddressPrefixLength_Type=InetAddressPrefixLength
_AdGenSubHostStatIpv6AddressPrefixLength_Object=MibTableColumn
adGenSubHostStatIpv6AddressPrefixLength=_AdGenSubHostStatIpv6AddressPrefixLength_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,6),_AdGenSubHostStatIpv6AddressPrefixLength_Type())
adGenSubHostStatIpv6AddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatIpv6AddressPrefixLength.setStatus(_A)
_AdGenSubHostStatIpv6AddressEui64_Type=TruthValue
_AdGenSubHostStatIpv6AddressEui64_Object=MibTableColumn
adGenSubHostStatIpv6AddressEui64=_AdGenSubHostStatIpv6AddressEui64_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,7),_AdGenSubHostStatIpv6AddressEui64_Type())
adGenSubHostStatIpv6AddressEui64.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatIpv6AddressEui64.setStatus(_A)
_AdGenSubHostStatIpv6Address_Type=InetAddressIPv6
_AdGenSubHostStatIpv6Address_Object=MibTableColumn
adGenSubHostStatIpv6Address=_AdGenSubHostStatIpv6Address_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,8),_AdGenSubHostStatIpv6Address_Type())
adGenSubHostStatIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatIpv6Address.setStatus(_A)
_AdGenSubHostStatIpv6AddressLinkLocal_Type=InetAddressIPv6
_AdGenSubHostStatIpv6AddressLinkLocal_Object=MibTableColumn
adGenSubHostStatIpv6AddressLinkLocal=_AdGenSubHostStatIpv6AddressLinkLocal_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,9),_AdGenSubHostStatIpv6AddressLinkLocal_Type())
adGenSubHostStatIpv6AddressLinkLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatIpv6AddressLinkLocal.setStatus(_A)
_AdGenSubHostStatAutoConfigMode_Type=TruthValue
_AdGenSubHostStatAutoConfigMode_Object=MibTableColumn
adGenSubHostStatAutoConfigMode=_AdGenSubHostStatAutoConfigMode_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,10),_AdGenSubHostStatAutoConfigMode_Type())
adGenSubHostStatAutoConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatAutoConfigMode.setStatus(_A)
_AdGenSubHostStatAutoConfigFilename_Type=DisplayString
_AdGenSubHostStatAutoConfigFilename_Object=MibTableColumn
adGenSubHostStatAutoConfigFilename=_AdGenSubHostStatAutoConfigFilename_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,11),_AdGenSubHostStatAutoConfigFilename_Type())
adGenSubHostStatAutoConfigFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatAutoConfigFilename.setStatus(_A)
_AdGenSubHostStatAutoConfigGroupName_Type=DisplayString
_AdGenSubHostStatAutoConfigGroupName_Object=MibTableColumn
adGenSubHostStatAutoConfigGroupName=_AdGenSubHostStatAutoConfigGroupName_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,12),_AdGenSubHostStatAutoConfigGroupName_Type())
adGenSubHostStatAutoConfigGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatAutoConfigGroupName.setStatus(_A)
_AdGenSubHostStatAutoConfigHostIpv4_Type=InetAddressIPv4
_AdGenSubHostStatAutoConfigHostIpv4_Object=MibTableColumn
adGenSubHostStatAutoConfigHostIpv4=_AdGenSubHostStatAutoConfigHostIpv4_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,13),_AdGenSubHostStatAutoConfigHostIpv4_Type())
adGenSubHostStatAutoConfigHostIpv4.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatAutoConfigHostIpv4.setStatus(_A)
_AdGenSubHostStatAutoConfigHostIpv6_Type=InetAddressIPv6
_AdGenSubHostStatAutoConfigHostIpv6_Object=MibTableColumn
adGenSubHostStatAutoConfigHostIpv6=_AdGenSubHostStatAutoConfigHostIpv6_Object((1,3,6,1,4,1,664,5,70,12,2,1,1,14),_AdGenSubHostStatAutoConfigHostIpv6_Type())
adGenSubHostStatAutoConfigHostIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatAutoConfigHostIpv6.setStatus(_A)
_AdGenSubHostStatFarEndTable_Object=MibTable
adGenSubHostStatFarEndTable=_AdGenSubHostStatFarEndTable_Object((1,3,6,1,4,1,664,5,70,12,2,2))
if mibBuilder.loadTexts:adGenSubHostStatFarEndTable.setStatus(_A)
_AdGenSubHostStatFarEndEntry_Object=MibTableRow
adGenSubHostStatFarEndEntry=_AdGenSubHostStatFarEndEntry_Object((1,3,6,1,4,1,664,5,70,12,2,2,1))
adGenSubHostStatFarEndEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenSubHostStatFarEndEntry.setStatus(_A)
_AdGenSubHostStatFarEndIfIndex_Type=InterfaceIndex
_AdGenSubHostStatFarEndIfIndex_Object=MibTableColumn
adGenSubHostStatFarEndIfIndex=_AdGenSubHostStatFarEndIfIndex_Object((1,3,6,1,4,1,664,5,70,12,2,2,1,1),_AdGenSubHostStatFarEndIfIndex_Type())
adGenSubHostStatFarEndIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatFarEndIfIndex.setStatus(_A)
_AdGenSubHostStatFarEndIpAddress_Type=IpAddress
_AdGenSubHostStatFarEndIpAddress_Object=MibTableColumn
adGenSubHostStatFarEndIpAddress=_AdGenSubHostStatFarEndIpAddress_Object((1,3,6,1,4,1,664,5,70,12,2,2,1,2),_AdGenSubHostStatFarEndIpAddress_Type())
adGenSubHostStatFarEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatFarEndIpAddress.setStatus(_A)
_AdGenSubHostStatFarEndSysName_Type=DisplayString
_AdGenSubHostStatFarEndSysName_Object=MibTableColumn
adGenSubHostStatFarEndSysName=_AdGenSubHostStatFarEndSysName_Object((1,3,6,1,4,1,664,5,70,12,2,2,1,3),_AdGenSubHostStatFarEndSysName_Type())
adGenSubHostStatFarEndSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSubHostStatFarEndSysName.setStatus(_A)
_AdGenSubtendedHostNotificationsPrefix_ObjectIdentity=ObjectIdentity
adGenSubtendedHostNotificationsPrefix=_AdGenSubtendedHostNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,70,12,3))
_AdGenSubtendedHostNotifications_ObjectIdentity=ObjectIdentity
adGenSubtendedHostNotifications=_AdGenSubtendedHostNotifications_ObjectIdentity((1,3,6,1,4,1,664,5,70,12,3,0))
adGenSubHostProvIfAutoDiscoveryAlm=NotificationType((1,3,6,1,4,1,664,5,70,12,3,0,1))
adGenSubHostProvIfAutoDiscoveryAlm.setObjects(*((_K,_L),(_N,_O),(_I,_J),(_D,_M),(_D,_E)))
if mibBuilder.loadTexts:adGenSubHostProvIfAutoDiscoveryAlm.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENSUBTENDEDHOST-MIB',**{'adGenSubtendedHostProvisioning':adGenSubtendedHostProvisioning,'adGenSubHostProvMgmtTable':adGenSubHostProvMgmtTable,'adGenSubHostProvMgmtEntry':adGenSubHostProvMgmtEntry,'adGenSubHostProvMgmtIpAddress':adGenSubHostProvMgmtIpAddress,'adGenSubHostProvMgmtIpSubnetMask':adGenSubHostProvMgmtIpSubnetMask,'adGenSubHostProvMgmtIpGateway':adGenSubHostProvMgmtIpGateway,'adGenSubHostProvMgmtIpVlan':adGenSubHostProvMgmtIpVlan,'adGenSubHostProvMgmtTftpServer':adGenSubHostProvMgmtTftpServer,'adGenSubHostProvMgmtSnmpWriteCommunity':adGenSubHostProvMgmtSnmpWriteCommunity,'adGenSubHostProvMgmtSnmpReadCommunity':adGenSubHostProvMgmtSnmpReadCommunity,'adGenSubHostProvMgmtSysName':adGenSubHostProvMgmtSysName,'adGenSubHostProvMgmtPriority':adGenSubHostProvMgmtPriority,'adGenSubHostProvMgmtIpAssignMode':adGenSubHostProvMgmtIpAssignMode,'adGenSubHostProvMgmtSync':adGenSubHostProvMgmtSync,'adGenSubHostProvMgmtSnmpSysLocation':adGenSubHostProvMgmtSnmpSysLocation,'adGenSubHostProvMgmtEzProvHostOneIpAddress':adGenSubHostProvMgmtEzProvHostOneIpAddress,'adGenSubHostProvMgmtEzProvHostOneTrapVersion':adGenSubHostProvMgmtEzProvHostOneTrapVersion,'adGenSubHostProvMgmtEzProvHostTwoIpAddress':adGenSubHostProvMgmtEzProvHostTwoIpAddress,'adGenSubHostProvMgmtEzProvHostTwoTrapVersion':adGenSubHostProvMgmtEzProvHostTwoTrapVersion,'adGenSubHostProvMgmtEzProvEnabled':adGenSubHostProvMgmtEzProvEnabled,'adGenSubHostProvMgmtIpv6AddressPrefixLength':adGenSubHostProvMgmtIpv6AddressPrefixLength,'adGenSubHostProvMgmtIpv6AddressEui64':adGenSubHostProvMgmtIpv6AddressEui64,'adGenSubHostProvMgmtIpv6Address':adGenSubHostProvMgmtIpv6Address,'adGenSubHostProvMgmtIpv6AddressLinkLocal':adGenSubHostProvMgmtIpv6AddressLinkLocal,'adGenSubHostProvMgmtAutoConfigMode':adGenSubHostProvMgmtAutoConfigMode,'adGenSubHostProvMgmtAutoConfigFilename':adGenSubHostProvMgmtAutoConfigFilename,'adGenSubHostProvMgmtAutoConfigGroupName':adGenSubHostProvMgmtAutoConfigGroupName,'adGenSubHostProvMgmtAutoConfigHostIpv4':adGenSubHostProvMgmtAutoConfigHostIpv4,'adGenSubHostProvMgmtAutoConfigHostIpv6':adGenSubHostProvMgmtAutoConfigHostIpv6,'adGenSubHostProvMgmtLastErrorString':adGenSubHostProvMgmtLastErrorString,'adGenSubHostProvIfTable':adGenSubHostProvIfTable,'adGenSubHostProvIfEntry':adGenSubHostProvIfEntry,'adGenSubHostProvIfMode':adGenSubHostProvIfMode,'adGenSubHostProvIfAutoDiscoveryMode':adGenSubHostProvIfAutoDiscoveryMode,'adGenSubHostProvIfAutoDiscoveryAck':adGenSubHostProvIfAutoDiscoveryAck,'adGenSubtendedHostStatus':adGenSubtendedHostStatus,'adGenSubHostStatTable':adGenSubHostStatTable,'adGenSubHostStatEntry':adGenSubHostStatEntry,'adGenSubHostStatMacAddress':adGenSubHostStatMacAddress,'adGenSubHostStatIpAddress':adGenSubHostStatIpAddress,'adGenSubHostStatGateway':adGenSubHostStatGateway,'adGenSubHostStatProvSync':adGenSubHostStatProvSync,'adGenSubHostStatIpSubnetMask':adGenSubHostStatIpSubnetMask,'adGenSubHostStatIpv6AddressPrefixLength':adGenSubHostStatIpv6AddressPrefixLength,'adGenSubHostStatIpv6AddressEui64':adGenSubHostStatIpv6AddressEui64,'adGenSubHostStatIpv6Address':adGenSubHostStatIpv6Address,'adGenSubHostStatIpv6AddressLinkLocal':adGenSubHostStatIpv6AddressLinkLocal,'adGenSubHostStatAutoConfigMode':adGenSubHostStatAutoConfigMode,'adGenSubHostStatAutoConfigFilename':adGenSubHostStatAutoConfigFilename,'adGenSubHostStatAutoConfigGroupName':adGenSubHostStatAutoConfigGroupName,'adGenSubHostStatAutoConfigHostIpv4':adGenSubHostStatAutoConfigHostIpv4,'adGenSubHostStatAutoConfigHostIpv6':adGenSubHostStatAutoConfigHostIpv6,'adGenSubHostStatFarEndTable':adGenSubHostStatFarEndTable,'adGenSubHostStatFarEndEntry':adGenSubHostStatFarEndEntry,'adGenSubHostStatFarEndIfIndex':adGenSubHostStatFarEndIfIndex,'adGenSubHostStatFarEndIpAddress':adGenSubHostStatFarEndIpAddress,'adGenSubHostStatFarEndSysName':adGenSubHostStatFarEndSysName,'adGenSubtendedHostNotificationsPrefix':adGenSubtendedHostNotificationsPrefix,'adGenSubtendedHostNotifications':adGenSubtendedHostNotifications,'adGenSubHostProvIfAutoDiscoveryAlm':adGenSubHostProvIfAutoDiscoveryAlm,'adGenSubtendedHostMIB':adGenSubtendedHostMIB})