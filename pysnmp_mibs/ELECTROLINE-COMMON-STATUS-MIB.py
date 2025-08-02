_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonStatus,electrolineCommon=mibBuilder.importSymbols('ELECTROLINE-COMMON-ROOT-MIB','commonStatus','electrolineCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
commonLogicalID,commonPhysAddress=mibBuilder.importSymbols('SCTE-HMS-COMMON-MIB','commonLogicalID','commonPhysAddress')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
class _InternalTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,130))
_InternalTemperature_Type.__name__=_C
_InternalTemperature_Object=MibScalar
internalTemperature=_InternalTemperature_Object((1,3,6,1,4,1,5802,1,3,1,4,3,1),_InternalTemperature_Type())
internalTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:internalTemperature.setStatus(_B)
_InetNetworkAddressType_Type=InetAddressType
_InetNetworkAddressType_Object=MibScalar
inetNetworkAddressType=_InetNetworkAddressType_Object((1,3,6,1,4,1,5802,1,3,1,4,3,2),_InetNetworkAddressType_Type())
inetNetworkAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:inetNetworkAddressType.setStatus(_B)
_InetNetworkAddress_Type=InetAddress
_InetNetworkAddress_Object=MibScalar
inetNetworkAddress=_InetNetworkAddress_Object((1,3,6,1,4,1,5802,1,3,1,4,3,3),_InetNetworkAddress_Type())
inetNetworkAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:inetNetworkAddress.setStatus(_B)
_InetMonitoringNetworkAddressType_Type=InetAddressType
_InetMonitoringNetworkAddressType_Object=MibScalar
inetMonitoringNetworkAddressType=_InetMonitoringNetworkAddressType_Object((1,3,6,1,4,1,5802,1,3,1,4,3,4),_InetMonitoringNetworkAddressType_Type())
inetMonitoringNetworkAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:inetMonitoringNetworkAddressType.setStatus(_B)
_InetMonitoringNetworkAddress_Type=InetAddress
_InetMonitoringNetworkAddress_Object=MibScalar
inetMonitoringNetworkAddress=_InetMonitoringNetworkAddress_Object((1,3,6,1,4,1,5802,1,3,1,4,3,5),_InetMonitoringNetworkAddress_Type())
inetMonitoringNetworkAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:inetMonitoringNetworkAddress.setStatus(_B)
mibBuilder.exportSymbols('ELECTROLINE-COMMON-STATUS-MIB',**{'internalTemperature':internalTemperature,'inetNetworkAddressType':inetNetworkAddressType,'inetNetworkAddress':inetNetworkAddress,'inetMonitoringNetworkAddressType':inetMonitoringNetworkAddressType,'inetMonitoringNetworkAddress':inetMonitoringNetworkAddress})