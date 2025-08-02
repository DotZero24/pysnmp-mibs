_F='Unsigned32'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','TextualConvention','TruthValue')
dlinkPrimeDeviceInfoMIB=ModuleIdentity((1,3,6,1,4,1,171,15,3))
if mibBuilder.loadTexts:dlinkPrimeDeviceInfoMIB.setRevisions(('2014-05-30 00:00',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_DpDeviceInfoMIBObjects_ObjectIdentity=ObjectIdentity
dpDeviceInfoMIBObjects=_DpDeviceInfoMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,3,1))
_DpDeviceInfoSysConfiguration_ObjectIdentity=ObjectIdentity
dpDeviceInfoSysConfiguration=_DpDeviceInfoSysConfiguration_ObjectIdentity((1,3,6,1,4,1,171,15,3,1,1))
class _DpDeviceInfoIpV4AddrCfgMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('dhcp',2),('bootp',3)))
_DpDeviceInfoIpV4AddrCfgMode_Type.__name__=_E
_DpDeviceInfoIpV4AddrCfgMode_Object=MibScalar
dpDeviceInfoIpV4AddrCfgMode=_DpDeviceInfoIpV4AddrCfgMode_Object((1,3,6,1,4,1,171,15,3,1,1,1),_DpDeviceInfoIpV4AddrCfgMode_Type())
dpDeviceInfoIpV4AddrCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dpDeviceInfoIpV4AddrCfgMode.setStatus(_A)
_DpDeviceInfoIpV4Addr_Type=IpAddress
_DpDeviceInfoIpV4Addr_Object=MibScalar
dpDeviceInfoIpV4Addr=_DpDeviceInfoIpV4Addr_Object((1,3,6,1,4,1,171,15,3,1,1,2),_DpDeviceInfoIpV4Addr_Type())
dpDeviceInfoIpV4Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:dpDeviceInfoIpV4Addr.setStatus(_A)
_DpDeviceInfoIpV4SubnetMask_Type=IpAddress
_DpDeviceInfoIpV4SubnetMask_Object=MibScalar
dpDeviceInfoIpV4SubnetMask=_DpDeviceInfoIpV4SubnetMask_Object((1,3,6,1,4,1,171,15,3,1,1,3),_DpDeviceInfoIpV4SubnetMask_Type())
dpDeviceInfoIpV4SubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dpDeviceInfoIpV4SubnetMask.setStatus(_A)
_DpDeviceInfoGateway_Type=IpAddress
_DpDeviceInfoGateway_Object=MibScalar
dpDeviceInfoGateway=_DpDeviceInfoGateway_Object((1,3,6,1,4,1,171,15,3,1,1,4),_DpDeviceInfoGateway_Type())
dpDeviceInfoGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:dpDeviceInfoGateway.setStatus(_A)
class _DpDeviceInfoDhcpRetry_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,128))
_DpDeviceInfoDhcpRetry_Type.__name__=_F
_DpDeviceInfoDhcpRetry_Object=MibScalar
dpDeviceInfoDhcpRetry=_DpDeviceInfoDhcpRetry_Object((1,3,6,1,4,1,171,15,3,1,1,5),_DpDeviceInfoDhcpRetry_Type())
dpDeviceInfoDhcpRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:dpDeviceInfoDhcpRetry.setStatus(_A)
class _DpDeviceInfoIpV6GlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_DpDeviceInfoIpV6GlobalState_Type.__name__=_E
_DpDeviceInfoIpV6GlobalState_Object=MibScalar
dpDeviceInfoIpV6GlobalState=_DpDeviceInfoIpV6GlobalState_Object((1,3,6,1,4,1,171,15,3,1,1,6),_DpDeviceInfoIpV6GlobalState_Type())
dpDeviceInfoIpV6GlobalState.setMaxAccess(_B)
if mibBuilder.loadTexts:dpDeviceInfoIpV6GlobalState.setStatus(_A)
_DpDeviceInfoIpV6AddressIpAddr_Type=Ipv6Address
_DpDeviceInfoIpV6AddressIpAddr_Object=MibScalar
dpDeviceInfoIpV6AddressIpAddr=_DpDeviceInfoIpV6AddressIpAddr_Object((1,3,6,1,4,1,171,15,3,1,1,7),_DpDeviceInfoIpV6AddressIpAddr_Type())
dpDeviceInfoIpV6AddressIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dpDeviceInfoIpV6AddressIpAddr.setStatus(_A)
_DpDeviceInfoMacAddr_Type=MacAddress
_DpDeviceInfoMacAddr_Object=MibScalar
dpDeviceInfoMacAddr=_DpDeviceInfoMacAddr_Object((1,3,6,1,4,1,171,15,3,1,2),_DpDeviceInfoMacAddr_Type())
dpDeviceInfoMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dpDeviceInfoMacAddr.setStatus(_A)
class _DpDeviceInfoBootPromVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DpDeviceInfoBootPromVersion_Type.__name__=_D
_DpDeviceInfoBootPromVersion_Object=MibScalar
dpDeviceInfoBootPromVersion=_DpDeviceInfoBootPromVersion_Object((1,3,6,1,4,1,171,15,3,1,3),_DpDeviceInfoBootPromVersion_Type())
dpDeviceInfoBootPromVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dpDeviceInfoBootPromVersion.setStatus(_A)
class _DpDeviceInfoFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DpDeviceInfoFirmwareVersion_Type.__name__=_D
_DpDeviceInfoFirmwareVersion_Object=MibScalar
dpDeviceInfoFirmwareVersion=_DpDeviceInfoFirmwareVersion_Object((1,3,6,1,4,1,171,15,3,1,4),_DpDeviceInfoFirmwareVersion_Type())
dpDeviceInfoFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dpDeviceInfoFirmwareVersion.setStatus(_A)
class _DpDeviceInfoHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DpDeviceInfoHardwareVersion_Type.__name__=_D
_DpDeviceInfoHardwareVersion_Object=MibScalar
dpDeviceInfoHardwareVersion=_DpDeviceInfoHardwareVersion_Object((1,3,6,1,4,1,171,15,3,1,5),_DpDeviceInfoHardwareVersion_Type())
dpDeviceInfoHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dpDeviceInfoHardwareVersion.setStatus(_A)
_DpDeviceInfoSerialNumber_Type=DisplayString
_DpDeviceInfoSerialNumber_Object=MibScalar
dpDeviceInfoSerialNumber=_DpDeviceInfoSerialNumber_Object((1,3,6,1,4,1,171,15,3,1,6),_DpDeviceInfoSerialNumber_Type())
dpDeviceInfoSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dpDeviceInfoSerialNumber.setStatus(_A)
mibBuilder.exportSymbols('DLINKPRIME-DEVICE-INFORMATION-MIB',**{'MacAddress':MacAddress,'Ipv6Address':Ipv6Address,'dlinkPrimeDeviceInfoMIB':dlinkPrimeDeviceInfoMIB,'dpDeviceInfoMIBObjects':dpDeviceInfoMIBObjects,'dpDeviceInfoSysConfiguration':dpDeviceInfoSysConfiguration,'dpDeviceInfoIpV4AddrCfgMode':dpDeviceInfoIpV4AddrCfgMode,'dpDeviceInfoIpV4Addr':dpDeviceInfoIpV4Addr,'dpDeviceInfoIpV4SubnetMask':dpDeviceInfoIpV4SubnetMask,'dpDeviceInfoGateway':dpDeviceInfoGateway,'dpDeviceInfoDhcpRetry':dpDeviceInfoDhcpRetry,'dpDeviceInfoIpV6GlobalState':dpDeviceInfoIpV6GlobalState,'dpDeviceInfoIpV6AddressIpAddr':dpDeviceInfoIpV6AddressIpAddr,'dpDeviceInfoMacAddr':dpDeviceInfoMacAddr,'dpDeviceInfoBootPromVersion':dpDeviceInfoBootPromVersion,'dpDeviceInfoFirmwareVersion':dpDeviceInfoFirmwareVersion,'dpDeviceInfoHardwareVersion':dpDeviceInfoHardwareVersion,'dpDeviceInfoSerialNumber':dpDeviceInfoSerialNumber})