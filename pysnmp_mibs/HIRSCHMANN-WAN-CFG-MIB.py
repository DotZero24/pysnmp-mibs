_N='hmWanStaticDhcpIndex'
_M='hmWanLeaseDhcpIndex'
_L='hmWanIfIndex'
_K='enabled'
_J='disabled'
_I='HIRSCHMANN-WAN-CFG-MIB'
_H='none'
_G='read-only'
_F='enable'
_E='disable'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
hmWanCfgMib=ModuleIdentity((1,3,6,1,4,1,248,40,1,8))
if mibBuilder.loadTexts:hmWanCfgMib.setRevisions(('2015-02-13 00:00',))
class HmWanIfIndexTc(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
class HmWanLeaseDhcpIndexTc(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
class HmWanStaticDhcpIndexTc(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_HmWanEth_ObjectIdentity=ObjectIdentity
hmWanEth=_HmWanEth_ObjectIdentity((1,3,6,1,4,1,248,40,1,8,1))
_HmWanIfNumber_Type=Integer32
_HmWanIfNumber_Object=MibScalar
hmWanIfNumber=_HmWanIfNumber_Object((1,3,6,1,4,1,248,40,1,8,1,1),_HmWanIfNumber_Type())
hmWanIfNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hmWanIfNumber.setStatus(_A)
_HmWanIfTable_Object=MibTable
hmWanIfTable=_HmWanIfTable_Object((1,3,6,1,4,1,248,40,1,8,1,2))
if mibBuilder.loadTexts:hmWanIfTable.setStatus(_A)
_HmWanIfEntry_Object=MibTableRow
hmWanIfEntry=_HmWanIfEntry_Object((1,3,6,1,4,1,248,40,1,8,1,2,1))
hmWanIfEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:hmWanIfEntry.setStatus(_A)
_HmWanIfIndex_Type=HmWanIfIndexTc
_HmWanIfIndex_Object=MibTableColumn
hmWanIfIndex=_HmWanIfIndex_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,1),_HmWanIfIndex_Type())
hmWanIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hmWanIfIndex.setStatus(_A)
class _HmWanIfDhcpClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HmWanIfDhcpClient_Type.__name__=_C
_HmWanIfDhcpClient_Object=MibTableColumn
hmWanIfDhcpClient=_HmWanIfDhcpClient_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,2),_HmWanIfDhcpClient_Type())
hmWanIfDhcpClient.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIfDhcpClient.setStatus(_A)
_HmWanIfIpAddress_Type=IpAddress
_HmWanIfIpAddress_Object=MibTableColumn
hmWanIfIpAddress=_HmWanIfIpAddress_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,3),_HmWanIfIpAddress_Type())
hmWanIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIfIpAddress.setStatus(_A)
_HmWanIfSubnetMask_Type=IpAddress
_HmWanIfSubnetMask_Object=MibTableColumn
hmWanIfSubnetMask=_HmWanIfSubnetMask_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,4),_HmWanIfSubnetMask_Type())
hmWanIfSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIfSubnetMask.setStatus(_A)
class _HmWanIfBridged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_HmWanIfBridged_Type.__name__=_C
_HmWanIfBridged_Object=MibTableColumn
hmWanIfBridged=_HmWanIfBridged_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,5),_HmWanIfBridged_Type())
hmWanIfBridged.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIfBridged.setStatus(_A)
class _HmWanIfMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('auto-negotiation',1),('full-duplex-100-Mbps',2),('half-duplex-100-Mbps',3),('full-duplex-10-Mbps',4),('half-duplex-10-Mbps',5)))
_HmWanIfMediaType_Type.__name__=_C
_HmWanIfMediaType_Object=MibTableColumn
hmWanIfMediaType=_HmWanIfMediaType_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,6),_HmWanIfMediaType_Type())
hmWanIfMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIfMediaType.setStatus(_A)
_HmWanIfDefaultGateway_Type=IpAddress
_HmWanIfDefaultGateway_Object=MibTableColumn
hmWanIfDefaultGateway=_HmWanIfDefaultGateway_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,7),_HmWanIfDefaultGateway_Type())
hmWanIfDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIfDefaultGateway.setStatus(_A)
_HmWanIfDnsServer_Type=IpAddress
_HmWanIfDnsServer_Object=MibTableColumn
hmWanIfDnsServer=_HmWanIfDnsServer_Object((1,3,6,1,4,1,248,40,1,8,1,2,1,8),_HmWanIfDnsServer_Type())
hmWanIfDnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIfDnsServer.setStatus(_A)
_HmWanLeaseDhcpNumber_Type=Integer32
_HmWanLeaseDhcpNumber_Object=MibScalar
hmWanLeaseDhcpNumber=_HmWanLeaseDhcpNumber_Object((1,3,6,1,4,1,248,40,1,8,1,3),_HmWanLeaseDhcpNumber_Type())
hmWanLeaseDhcpNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hmWanLeaseDhcpNumber.setStatus(_A)
_HmWanLeaseDhcpTable_Object=MibTable
hmWanLeaseDhcpTable=_HmWanLeaseDhcpTable_Object((1,3,6,1,4,1,248,40,1,8,1,4))
if mibBuilder.loadTexts:hmWanLeaseDhcpTable.setStatus(_A)
_HmWanLeaseDhcpEntry_Object=MibTableRow
hmWanLeaseDhcpEntry=_HmWanLeaseDhcpEntry_Object((1,3,6,1,4,1,248,40,1,8,1,4,1))
hmWanLeaseDhcpEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:hmWanLeaseDhcpEntry.setStatus(_A)
_HmWanLeaseDhcpIndex_Type=HmWanLeaseDhcpIndexTc
_HmWanLeaseDhcpIndex_Object=MibTableColumn
hmWanLeaseDhcpIndex=_HmWanLeaseDhcpIndex_Object((1,3,6,1,4,1,248,40,1,8,1,4,1,1),_HmWanLeaseDhcpIndex_Type())
hmWanLeaseDhcpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hmWanLeaseDhcpIndex.setStatus(_A)
class _HmWanLeaseDhcpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HmWanLeaseDhcpServer_Type.__name__=_C
_HmWanLeaseDhcpServer_Object=MibTableColumn
hmWanLeaseDhcpServer=_HmWanLeaseDhcpServer_Object((1,3,6,1,4,1,248,40,1,8,1,4,1,2),_HmWanLeaseDhcpServer_Type())
hmWanLeaseDhcpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanLeaseDhcpServer.setStatus(_A)
_HmWanLeaseDhcpIpPoolStart_Type=IpAddress
_HmWanLeaseDhcpIpPoolStart_Object=MibTableColumn
hmWanLeaseDhcpIpPoolStart=_HmWanLeaseDhcpIpPoolStart_Object((1,3,6,1,4,1,248,40,1,8,1,4,1,3),_HmWanLeaseDhcpIpPoolStart_Type())
hmWanLeaseDhcpIpPoolStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanLeaseDhcpIpPoolStart.setStatus(_A)
_HmWanLeaseDhcpIpPoolEnd_Type=IpAddress
_HmWanLeaseDhcpIpPoolEnd_Object=MibTableColumn
hmWanLeaseDhcpIpPoolEnd=_HmWanLeaseDhcpIpPoolEnd_Object((1,3,6,1,4,1,248,40,1,8,1,4,1,4),_HmWanLeaseDhcpIpPoolEnd_Type())
hmWanLeaseDhcpIpPoolEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanLeaseDhcpIpPoolEnd.setStatus(_A)
class _HmWanLeaseDhcpTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_HmWanLeaseDhcpTime_Type.__name__=_C
_HmWanLeaseDhcpTime_Object=MibTableColumn
hmWanLeaseDhcpTime=_HmWanLeaseDhcpTime_Object((1,3,6,1,4,1,248,40,1,8,1,4,1,5),_HmWanLeaseDhcpTime_Type())
hmWanLeaseDhcpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanLeaseDhcpTime.setStatus(_A)
if mibBuilder.loadTexts:hmWanLeaseDhcpTime.setUnits('sec')
class _HmWanStaticDhcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HmWanStaticDhcp_Type.__name__=_C
_HmWanStaticDhcp_Object=MibScalar
hmWanStaticDhcp=_HmWanStaticDhcp_Object((1,3,6,1,4,1,248,40,1,8,1,5),_HmWanStaticDhcp_Type())
hmWanStaticDhcp.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanStaticDhcp.setStatus(_A)
_HmWanStaticDhcpNumber_Type=Integer32
_HmWanStaticDhcpNumber_Object=MibScalar
hmWanStaticDhcpNumber=_HmWanStaticDhcpNumber_Object((1,3,6,1,4,1,248,40,1,8,1,6),_HmWanStaticDhcpNumber_Type())
hmWanStaticDhcpNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hmWanStaticDhcpNumber.setStatus(_A)
_HmWanStaticDhcpTable_Object=MibTable
hmWanStaticDhcpTable=_HmWanStaticDhcpTable_Object((1,3,6,1,4,1,248,40,1,8,1,7))
if mibBuilder.loadTexts:hmWanStaticDhcpTable.setStatus(_A)
_HmWanStaticDhcpEntry_Object=MibTableRow
hmWanStaticDhcpEntry=_HmWanStaticDhcpEntry_Object((1,3,6,1,4,1,248,40,1,8,1,7,1))
hmWanStaticDhcpEntry.setIndexNames((0,_I,_N))
if mibBuilder.loadTexts:hmWanStaticDhcpEntry.setStatus(_A)
_HmWanStaticDhcpIndex_Type=HmWanStaticDhcpIndexTc
_HmWanStaticDhcpIndex_Object=MibTableColumn
hmWanStaticDhcpIndex=_HmWanStaticDhcpIndex_Object((1,3,6,1,4,1,248,40,1,8,1,7,1,1),_HmWanStaticDhcpIndex_Type())
hmWanStaticDhcpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hmWanStaticDhcpIndex.setStatus(_A)
_HmWanStaticDhcpMacAddress_Type=MacAddress
_HmWanStaticDhcpMacAddress_Object=MibTableColumn
hmWanStaticDhcpMacAddress=_HmWanStaticDhcpMacAddress_Object((1,3,6,1,4,1,248,40,1,8,1,7,1,2),_HmWanStaticDhcpMacAddress_Type())
hmWanStaticDhcpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanStaticDhcpMacAddress.setStatus(_A)
_HmWanStaticDhcpIpAddress_Type=IpAddress
_HmWanStaticDhcpIpAddress_Object=MibTableColumn
hmWanStaticDhcpIpAddress=_HmWanStaticDhcpIpAddress_Object((1,3,6,1,4,1,248,40,1,8,1,7,1,3),_HmWanStaticDhcpIpAddress_Type())
hmWanStaticDhcpIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanStaticDhcpIpAddress.setStatus(_A)
_HmWanSnmpCfg_ObjectIdentity=ObjectIdentity
hmWanSnmpCfg=_HmWanSnmpCfg_ObjectIdentity((1,3,6,1,4,1,248,40,1,8,17))
class _HmWanSnmpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HmWanSnmpAdminStatus_Type.__name__=_C
_HmWanSnmpAdminStatus_Object=MibScalar
hmWanSnmpAdminStatus=_HmWanSnmpAdminStatus_Object((1,3,6,1,4,1,248,40,1,8,17,1),_HmWanSnmpAdminStatus_Type())
hmWanSnmpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpAdminStatus.setStatus(_A)
class _HmWanSnmpSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanSnmpSysName_Type.__name__=_D
_HmWanSnmpSysName_Object=MibScalar
hmWanSnmpSysName=_HmWanSnmpSysName_Object((1,3,6,1,4,1,248,40,1,8,17,2),_HmWanSnmpSysName_Type())
hmWanSnmpSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpSysName.setStatus(_A)
class _HmWanSnmpSysLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanSnmpSysLocation_Type.__name__=_D
_HmWanSnmpSysLocation_Object=MibScalar
hmWanSnmpSysLocation=_HmWanSnmpSysLocation_Object((1,3,6,1,4,1,248,40,1,8,17,3),_HmWanSnmpSysLocation_Type())
hmWanSnmpSysLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpSysLocation.setStatus(_A)
class _HmWanSnmpSysContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanSnmpSysContact_Type.__name__=_D
_HmWanSnmpSysContact_Object=MibScalar
hmWanSnmpSysContact=_HmWanSnmpSysContact_Object((1,3,6,1,4,1,248,40,1,8,17,4),_HmWanSnmpSysContact_Type())
hmWanSnmpSysContact.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpSysContact.setStatus(_A)
class _HmWanSnmpV1AccessAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HmWanSnmpV1AccessAdminStatus_Type.__name__=_C
_HmWanSnmpV1AccessAdminStatus_Object=MibScalar
hmWanSnmpV1AccessAdminStatus=_HmWanSnmpV1AccessAdminStatus_Object((1,3,6,1,4,1,248,40,1,8,17,5),_HmWanSnmpV1AccessAdminStatus_Type())
hmWanSnmpV1AccessAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV1AccessAdminStatus.setStatus(_A)
class _HmWanSnmpV1ReadCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanSnmpV1ReadCommunity_Type.__name__=_D
_HmWanSnmpV1ReadCommunity_Object=MibScalar
hmWanSnmpV1ReadCommunity=_HmWanSnmpV1ReadCommunity_Object((1,3,6,1,4,1,248,40,1,8,17,6),_HmWanSnmpV1ReadCommunity_Type())
hmWanSnmpV1ReadCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV1ReadCommunity.setStatus(_A)
class _HmWanSnmpV1WriteCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanSnmpV1WriteCommunity_Type.__name__=_D
_HmWanSnmpV1WriteCommunity_Object=MibScalar
hmWanSnmpV1WriteCommunity=_HmWanSnmpV1WriteCommunity_Object((1,3,6,1,4,1,248,40,1,8,17,7),_HmWanSnmpV1WriteCommunity_Type())
hmWanSnmpV1WriteCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV1WriteCommunity.setStatus(_A)
class _HmWanSnmpV3AccessAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HmWanSnmpV3AccessAdminStatus_Type.__name__=_C
_HmWanSnmpV3AccessAdminStatus_Object=MibScalar
hmWanSnmpV3AccessAdminStatus=_HmWanSnmpV3AccessAdminStatus_Object((1,3,6,1,4,1,248,40,1,8,17,8),_HmWanSnmpV3AccessAdminStatus_Type())
hmWanSnmpV3AccessAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3AccessAdminStatus.setStatus(_A)
class _HmWanSnmpV33ReadUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanSnmpV33ReadUsername_Type.__name__=_D
_HmWanSnmpV33ReadUsername_Object=MibScalar
hmWanSnmpV33ReadUsername=_HmWanSnmpV33ReadUsername_Object((1,3,6,1,4,1,248,40,1,8,17,9),_HmWanSnmpV33ReadUsername_Type())
hmWanSnmpV33ReadUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV33ReadUsername.setStatus(_A)
class _HmWanSnmpV3ReadAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('md5',2),('sha1',3)))
_HmWanSnmpV3ReadAuth_Type.__name__=_C
_HmWanSnmpV3ReadAuth_Object=MibScalar
hmWanSnmpV3ReadAuth=_HmWanSnmpV3ReadAuth_Object((1,3,6,1,4,1,248,40,1,8,17,10),_HmWanSnmpV3ReadAuth_Type())
hmWanSnmpV3ReadAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3ReadAuth.setStatus(_A)
class _HmWanSnmpV3ReadAuthPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,255))
_HmWanSnmpV3ReadAuthPwd_Type.__name__=_D
_HmWanSnmpV3ReadAuthPwd_Object=MibScalar
hmWanSnmpV3ReadAuthPwd=_HmWanSnmpV3ReadAuthPwd_Object((1,3,6,1,4,1,248,40,1,8,17,11),_HmWanSnmpV3ReadAuthPwd_Type())
hmWanSnmpV3ReadAuthPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3ReadAuthPwd.setStatus(_A)
class _HmWanSnmpV3ReadPrivProt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('des',2),('aes',3)))
_HmWanSnmpV3ReadPrivProt_Type.__name__=_C
_HmWanSnmpV3ReadPrivProt_Object=MibScalar
hmWanSnmpV3ReadPrivProt=_HmWanSnmpV3ReadPrivProt_Object((1,3,6,1,4,1,248,40,1,8,17,12),_HmWanSnmpV3ReadPrivProt_Type())
hmWanSnmpV3ReadPrivProt.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3ReadPrivProt.setStatus(_A)
class _HmWanSnmpV3ReadPrivPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,255))
_HmWanSnmpV3ReadPrivPwd_Type.__name__=_D
_HmWanSnmpV3ReadPrivPwd_Object=MibScalar
hmWanSnmpV3ReadPrivPwd=_HmWanSnmpV3ReadPrivPwd_Object((1,3,6,1,4,1,248,40,1,8,17,13),_HmWanSnmpV3ReadPrivPwd_Type())
hmWanSnmpV3ReadPrivPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3ReadPrivPwd.setStatus(_A)
class _HmWanSnmpV3WriteUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanSnmpV3WriteUsername_Type.__name__=_D
_HmWanSnmpV3WriteUsername_Object=MibScalar
hmWanSnmpV3WriteUsername=_HmWanSnmpV3WriteUsername_Object((1,3,6,1,4,1,248,40,1,8,17,14),_HmWanSnmpV3WriteUsername_Type())
hmWanSnmpV3WriteUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3WriteUsername.setStatus(_A)
class _HmWanSnmpV3WriteAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('md5',2),('sha1',3)))
_HmWanSnmpV3WriteAuth_Type.__name__=_C
_HmWanSnmpV3WriteAuth_Object=MibScalar
hmWanSnmpV3WriteAuth=_HmWanSnmpV3WriteAuth_Object((1,3,6,1,4,1,248,40,1,8,17,15),_HmWanSnmpV3WriteAuth_Type())
hmWanSnmpV3WriteAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3WriteAuth.setStatus(_A)
class _HmWanSnmpV3WriteAuthPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,255))
_HmWanSnmpV3WriteAuthPwd_Type.__name__=_D
_HmWanSnmpV3WriteAuthPwd_Object=MibScalar
hmWanSnmpV3WriteAuthPwd=_HmWanSnmpV3WriteAuthPwd_Object((1,3,6,1,4,1,248,40,1,8,17,16),_HmWanSnmpV3WriteAuthPwd_Type())
hmWanSnmpV3WriteAuthPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3WriteAuthPwd.setStatus(_A)
class _HmWanSnmpV3WritePrivProt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('des',2),('aes',3)))
_HmWanSnmpV3WritePrivProt_Type.__name__=_C
_HmWanSnmpV3WritePrivProt_Object=MibScalar
hmWanSnmpV3WritePrivProt=_HmWanSnmpV3WritePrivProt_Object((1,3,6,1,4,1,248,40,1,8,17,17),_HmWanSnmpV3WritePrivProt_Type())
hmWanSnmpV3WritePrivProt.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3WritePrivProt.setStatus(_A)
class _HmWanSnmpV3WritePrivPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,255))
_HmWanSnmpV3WritePrivPwd_Type.__name__=_D
_HmWanSnmpV3WritePrivPwd_Object=MibScalar
hmWanSnmpV3WritePrivPwd=_HmWanSnmpV3WritePrivPwd_Object((1,3,6,1,4,1,248,40,1,8,17,18),_HmWanSnmpV3WritePrivPwd_Type())
hmWanSnmpV3WritePrivPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanSnmpV3WritePrivPwd.setStatus(_A)
class _HmWanIoExtensionAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HmWanIoExtensionAdminStatus_Type.__name__=_C
_HmWanIoExtensionAdminStatus_Object=MibScalar
hmWanIoExtensionAdminStatus=_HmWanIoExtensionAdminStatus_Object((1,3,6,1,4,1,248,40,1,8,17,19),_HmWanIoExtensionAdminStatus_Type())
hmWanIoExtensionAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanIoExtensionAdminStatus.setStatus(_A)
class _HmWanXccntExtensionAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HmWanXccntExtensionAdminStatus_Type.__name__=_C
_HmWanXccntExtensionAdminStatus_Object=MibScalar
hmWanXccntExtensionAdminStatus=_HmWanXccntExtensionAdminStatus_Object((1,3,6,1,4,1,248,40,1,8,17,20),_HmWanXccntExtensionAdminStatus_Type())
hmWanXccntExtensionAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanXccntExtensionAdminStatus.setStatus(_A)
class _HmWanMbusExtensionAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HmWanMbusExtensionAdminStatus_Type.__name__=_C
_HmWanMbusExtensionAdminStatus_Object=MibScalar
hmWanMbusExtensionAdminStatus=_HmWanMbusExtensionAdminStatus_Object((1,3,6,1,4,1,248,40,1,8,17,21),_HmWanMbusExtensionAdminStatus_Type())
hmWanMbusExtensionAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanMbusExtensionAdminStatus.setStatus(_A)
class _HmWanMbusBaudrate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,300),ValueRangeConstraint(600,600),ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600))
_HmWanMbusBaudrate_Type.__name__=_C
_HmWanMbusBaudrate_Object=MibScalar
hmWanMbusBaudrate=_HmWanMbusBaudrate_Object((1,3,6,1,4,1,248,40,1,8,17,22),_HmWanMbusBaudrate_Type())
hmWanMbusBaudrate.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanMbusBaudrate.setStatus(_A)
class _HmWanMbusParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('even',2),('odd',3)))
_HmWanMbusParity_Type.__name__=_C
_HmWanMbusParity_Object=MibScalar
hmWanMbusParity=_HmWanMbusParity_Object((1,3,6,1,4,1,248,40,1,8,17,23),_HmWanMbusParity_Type())
hmWanMbusParity.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanMbusParity.setStatus(_A)
class _HmWanMbusStopbits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_HmWanMbusStopbits_Type.__name__=_C
_HmWanMbusStopbits_Object=MibScalar
hmWanMbusStopbits=_HmWanMbusStopbits_Object((1,3,6,1,4,1,248,40,1,8,17,24),_HmWanMbusStopbits_Type())
hmWanMbusStopbits.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanMbusStopbits.setStatus(_A)
class _HmWanReportAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HmWanReportAdminStatus_Type.__name__=_C
_HmWanReportAdminStatus_Object=MibScalar
hmWanReportAdminStatus=_HmWanReportAdminStatus_Object((1,3,6,1,4,1,248,40,1,8,17,25),_HmWanReportAdminStatus_Type())
hmWanReportAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanReportAdminStatus.setStatus(_A)
class _HmWanReportIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmWanReportIPAddress_Type.__name__=_D
_HmWanReportIPAddress_Object=MibScalar
hmWanReportIPAddress=_HmWanReportIPAddress_Object((1,3,6,1,4,1,248,40,1,8,17,26),_HmWanReportIPAddress_Type())
hmWanReportIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanReportIPAddress.setStatus(_A)
class _HmWanReportPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_HmWanReportPeriod_Type.__name__=_C
_HmWanReportPeriod_Object=MibScalar
hmWanReportPeriod=_HmWanReportPeriod_Object((1,3,6,1,4,1,248,40,1,8,17,27),_HmWanReportPeriod_Type())
hmWanReportPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hmWanReportPeriod.setStatus(_A)
if mibBuilder.loadTexts:hmWanReportPeriod.setUnits('min')
mibBuilder.exportSymbols(_I,**{'HmWanIfIndexTc':HmWanIfIndexTc,'HmWanLeaseDhcpIndexTc':HmWanLeaseDhcpIndexTc,'HmWanStaticDhcpIndexTc':HmWanStaticDhcpIndexTc,'hmWanCfgMib':hmWanCfgMib,'hmWanEth':hmWanEth,'hmWanIfNumber':hmWanIfNumber,'hmWanIfTable':hmWanIfTable,'hmWanIfEntry':hmWanIfEntry,_L:hmWanIfIndex,'hmWanIfDhcpClient':hmWanIfDhcpClient,'hmWanIfIpAddress':hmWanIfIpAddress,'hmWanIfSubnetMask':hmWanIfSubnetMask,'hmWanIfBridged':hmWanIfBridged,'hmWanIfMediaType':hmWanIfMediaType,'hmWanIfDefaultGateway':hmWanIfDefaultGateway,'hmWanIfDnsServer':hmWanIfDnsServer,'hmWanLeaseDhcpNumber':hmWanLeaseDhcpNumber,'hmWanLeaseDhcpTable':hmWanLeaseDhcpTable,'hmWanLeaseDhcpEntry':hmWanLeaseDhcpEntry,_M:hmWanLeaseDhcpIndex,'hmWanLeaseDhcpServer':hmWanLeaseDhcpServer,'hmWanLeaseDhcpIpPoolStart':hmWanLeaseDhcpIpPoolStart,'hmWanLeaseDhcpIpPoolEnd':hmWanLeaseDhcpIpPoolEnd,'hmWanLeaseDhcpTime':hmWanLeaseDhcpTime,'hmWanStaticDhcp':hmWanStaticDhcp,'hmWanStaticDhcpNumber':hmWanStaticDhcpNumber,'hmWanStaticDhcpTable':hmWanStaticDhcpTable,'hmWanStaticDhcpEntry':hmWanStaticDhcpEntry,_N:hmWanStaticDhcpIndex,'hmWanStaticDhcpMacAddress':hmWanStaticDhcpMacAddress,'hmWanStaticDhcpIpAddress':hmWanStaticDhcpIpAddress,'hmWanSnmpCfg':hmWanSnmpCfg,'hmWanSnmpAdminStatus':hmWanSnmpAdminStatus,'hmWanSnmpSysName':hmWanSnmpSysName,'hmWanSnmpSysLocation':hmWanSnmpSysLocation,'hmWanSnmpSysContact':hmWanSnmpSysContact,'hmWanSnmpV1AccessAdminStatus':hmWanSnmpV1AccessAdminStatus,'hmWanSnmpV1ReadCommunity':hmWanSnmpV1ReadCommunity,'hmWanSnmpV1WriteCommunity':hmWanSnmpV1WriteCommunity,'hmWanSnmpV3AccessAdminStatus':hmWanSnmpV3AccessAdminStatus,'hmWanSnmpV33ReadUsername':hmWanSnmpV33ReadUsername,'hmWanSnmpV3ReadAuth':hmWanSnmpV3ReadAuth,'hmWanSnmpV3ReadAuthPwd':hmWanSnmpV3ReadAuthPwd,'hmWanSnmpV3ReadPrivProt':hmWanSnmpV3ReadPrivProt,'hmWanSnmpV3ReadPrivPwd':hmWanSnmpV3ReadPrivPwd,'hmWanSnmpV3WriteUsername':hmWanSnmpV3WriteUsername,'hmWanSnmpV3WriteAuth':hmWanSnmpV3WriteAuth,'hmWanSnmpV3WriteAuthPwd':hmWanSnmpV3WriteAuthPwd,'hmWanSnmpV3WritePrivProt':hmWanSnmpV3WritePrivProt,'hmWanSnmpV3WritePrivPwd':hmWanSnmpV3WritePrivPwd,'hmWanIoExtensionAdminStatus':hmWanIoExtensionAdminStatus,'hmWanXccntExtensionAdminStatus':hmWanXccntExtensionAdminStatus,'hmWanMbusExtensionAdminStatus':hmWanMbusExtensionAdminStatus,'hmWanMbusBaudrate':hmWanMbusBaudrate,'hmWanMbusParity':hmWanMbusParity,'hmWanMbusStopbits':hmWanMbusStopbits,'hmWanReportAdminStatus':hmWanReportAdminStatus,'hmWanReportIPAddress':hmWanReportIPAddress,'hmWanReportPeriod':hmWanReportPeriod})