_E='TruthValue'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmManagement,=mibBuilder.importSymbols('HIRSCHMANN-MGMT-MIB','hmManagement')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_E)
hmMgmtDiscoveryGroup=ModuleIdentity((1,3,6,1,4,1,248,16,100))
if mibBuilder.loadTexts:hmMgmtDiscoveryGroup.setRevisions(('2014-07-07 12:00',))
_HmMgmtDiscoveryStatusGroup_ObjectIdentity=ObjectIdentity
hmMgmtDiscoveryStatusGroup=_HmMgmtDiscoveryStatusGroup_ObjectIdentity((1,3,6,1,4,1,248,16,100,1))
class _HmMgmtDiscMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_HmMgmtDiscMode_Type.__name__=_D
_HmMgmtDiscMode_Object=MibScalar
hmMgmtDiscMode=_HmMgmtDiscMode_Object((1,3,6,1,4,1,248,16,100,1,1),_HmMgmtDiscMode_Type())
hmMgmtDiscMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMgmtDiscMode.setStatus(_A)
_HmMgmtDiscMacAddr_Type=MacAddress
_HmMgmtDiscMacAddr_Object=MibScalar
hmMgmtDiscMacAddr=_HmMgmtDiscMacAddr_Object((1,3,6,1,4,1,248,16,100,1,2),_HmMgmtDiscMacAddr_Type())
hmMgmtDiscMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMgmtDiscMacAddr.setStatus(_A)
class _HmMgmtDiscIpIntfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loopback-intf',1),('router-intf',2),('mgmt-intf',3)))
_HmMgmtDiscIpIntfType_Type.__name__=_D
_HmMgmtDiscIpIntfType_Object=MibScalar
hmMgmtDiscIpIntfType=_HmMgmtDiscIpIntfType_Object((1,3,6,1,4,1,248,16,100,1,3),_HmMgmtDiscIpIntfType_Type())
hmMgmtDiscIpIntfType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMgmtDiscIpIntfType.setStatus(_A)
_HmMgmtDiscSwVersion_Type=SnmpAdminString
_HmMgmtDiscSwVersion_Object=MibScalar
hmMgmtDiscSwVersion=_HmMgmtDiscSwVersion_Object((1,3,6,1,4,1,248,16,100,1,4),_HmMgmtDiscSwVersion_Type())
hmMgmtDiscSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMgmtDiscSwVersion.setStatus(_A)
_HmMgmtDiscProductDescr_Type=SnmpAdminString
_HmMgmtDiscProductDescr_Object=MibScalar
hmMgmtDiscProductDescr=_HmMgmtDiscProductDescr_Object((1,3,6,1,4,1,248,16,100,1,5),_HmMgmtDiscProductDescr_Type())
hmMgmtDiscProductDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMgmtDiscProductDescr.setStatus(_A)
class _HmMgmtDiscForcePasswordChange_Type(TruthValue):defaultValue=1
_HmMgmtDiscForcePasswordChange_Type.__name__=_E
_HmMgmtDiscForcePasswordChange_Object=MibScalar
hmMgmtDiscForcePasswordChange=_HmMgmtDiscForcePasswordChange_Object((1,3,6,1,4,1,248,16,100,1,10),_HmMgmtDiscForcePasswordChange_Type())
hmMgmtDiscForcePasswordChange.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMgmtDiscForcePasswordChange.setStatus(_A)
_HmMgmtDiscoveryCfgGroup_ObjectIdentity=ObjectIdentity
hmMgmtDiscoveryCfgGroup=_HmMgmtDiscoveryCfgGroup_ObjectIdentity((1,3,6,1,4,1,248,16,100,2))
_HmMgmtDiscCfgUUID_Type=OctetString
_HmMgmtDiscCfgUUID_Object=MibScalar
hmMgmtDiscCfgUUID=_HmMgmtDiscCfgUUID_Object((1,3,6,1,4,1,248,16,100,2,1),_HmMgmtDiscCfgUUID_Type())
hmMgmtDiscCfgUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgUUID.setStatus(_A)
class _HmMgmtDiscCfgProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('bootp',2),('dhcp',3)))
_HmMgmtDiscCfgProto_Type.__name__=_D
_HmMgmtDiscCfgProto_Object=MibScalar
hmMgmtDiscCfgProto=_HmMgmtDiscCfgProto_Object((1,3,6,1,4,1,248,16,100,2,2),_HmMgmtDiscCfgProto_Type())
hmMgmtDiscCfgProto.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgProto.setStatus(_A)
_HmMgmtDiscCfgIPAddrType_Type=InetAddressType
_HmMgmtDiscCfgIPAddrType_Object=MibScalar
hmMgmtDiscCfgIPAddrType=_HmMgmtDiscCfgIPAddrType_Object((1,3,6,1,4,1,248,16,100,2,3),_HmMgmtDiscCfgIPAddrType_Type())
hmMgmtDiscCfgIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgIPAddrType.setStatus(_A)
_HmMgmtDiscCfgIPAddr_Type=InetAddress
_HmMgmtDiscCfgIPAddr_Object=MibScalar
hmMgmtDiscCfgIPAddr=_HmMgmtDiscCfgIPAddr_Object((1,3,6,1,4,1,248,16,100,2,4),_HmMgmtDiscCfgIPAddr_Type())
hmMgmtDiscCfgIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgIPAddr.setStatus(_A)
_HmMgmtDiscCfgPrefLen_Type=InetAddressPrefixLength
_HmMgmtDiscCfgPrefLen_Object=MibScalar
hmMgmtDiscCfgPrefLen=_HmMgmtDiscCfgPrefLen_Object((1,3,6,1,4,1,248,16,100,2,5),_HmMgmtDiscCfgPrefLen_Type())
hmMgmtDiscCfgPrefLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgPrefLen.setStatus(_A)
_HmMgmtDiscCfgGwIPAddrType_Type=InetAddressType
_HmMgmtDiscCfgGwIPAddrType_Object=MibScalar
hmMgmtDiscCfgGwIPAddrType=_HmMgmtDiscCfgGwIPAddrType_Object((1,3,6,1,4,1,248,16,100,2,6),_HmMgmtDiscCfgGwIPAddrType_Type())
hmMgmtDiscCfgGwIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgGwIPAddrType.setStatus(_A)
_HmMgmtDiscCfgGwIPAddr_Type=InetAddress
_HmMgmtDiscCfgGwIPAddr_Object=MibScalar
hmMgmtDiscCfgGwIPAddr=_HmMgmtDiscCfgGwIPAddr_Object((1,3,6,1,4,1,248,16,100,2,7),_HmMgmtDiscCfgGwIPAddr_Type())
hmMgmtDiscCfgGwIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgGwIPAddr.setStatus(_A)
class _HmMgmtDiscCfgAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('activate',2)))
_HmMgmtDiscCfgAction_Type.__name__=_D
_HmMgmtDiscCfgAction_Object=MibScalar
hmMgmtDiscCfgAction=_HmMgmtDiscCfgAction_Object((1,3,6,1,4,1,248,16,100,2,8),_HmMgmtDiscCfgAction_Type())
hmMgmtDiscCfgAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgAction.setStatus(_A)
class _HmMgmtDiscCfgBlinking_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HmMgmtDiscCfgBlinking_Type.__name__=_D
_HmMgmtDiscCfgBlinking_Object=MibScalar
hmMgmtDiscCfgBlinking=_HmMgmtDiscCfgBlinking_Object((1,3,6,1,4,1,248,16,100,2,9),_HmMgmtDiscCfgBlinking_Type())
hmMgmtDiscCfgBlinking.setMaxAccess(_B)
if mibBuilder.loadTexts:hmMgmtDiscCfgBlinking.setStatus(_A)
mibBuilder.exportSymbols('HIRSCHMANN-DISCOVERY-MGMT-MIB',**{'hmMgmtDiscoveryGroup':hmMgmtDiscoveryGroup,'hmMgmtDiscoveryStatusGroup':hmMgmtDiscoveryStatusGroup,'hmMgmtDiscMode':hmMgmtDiscMode,'hmMgmtDiscMacAddr':hmMgmtDiscMacAddr,'hmMgmtDiscIpIntfType':hmMgmtDiscIpIntfType,'hmMgmtDiscSwVersion':hmMgmtDiscSwVersion,'hmMgmtDiscProductDescr':hmMgmtDiscProductDescr,'hmMgmtDiscForcePasswordChange':hmMgmtDiscForcePasswordChange,'hmMgmtDiscoveryCfgGroup':hmMgmtDiscoveryCfgGroup,'hmMgmtDiscCfgUUID':hmMgmtDiscCfgUUID,'hmMgmtDiscCfgProto':hmMgmtDiscCfgProto,'hmMgmtDiscCfgIPAddrType':hmMgmtDiscCfgIPAddrType,'hmMgmtDiscCfgIPAddr':hmMgmtDiscCfgIPAddr,'hmMgmtDiscCfgPrefLen':hmMgmtDiscCfgPrefLen,'hmMgmtDiscCfgGwIPAddrType':hmMgmtDiscCfgGwIPAddrType,'hmMgmtDiscCfgGwIPAddr':hmMgmtDiscCfgGwIPAddr,'hmMgmtDiscCfgAction':hmMgmtDiscCfgAction,'hmMgmtDiscCfgBlinking':hmMgmtDiscCfgBlinking})