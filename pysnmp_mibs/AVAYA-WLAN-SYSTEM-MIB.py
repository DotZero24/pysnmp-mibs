_G='TruthValue'
_F='InetPortNumber'
_E='InetAddress'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,'InetAddressType',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
avayaWlanMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','avayaWlanMibs')
avayaWlanSystemMib=ModuleIdentity((1,3,6,1,4,1,45,7,16))
if mibBuilder.loadTexts:avayaWlanSystemMib.setRevisions(('2010-05-25 00:00',))
_AvWlanSystemObjects_ObjectIdentity=ObjectIdentity
avWlanSystemObjects=_AvWlanSystemObjects_ObjectIdentity((1,3,6,1,4,1,45,7,16,1))
_AvWlanSystemConfig_ObjectIdentity=ObjectIdentity
avWlanSystemConfig=_AvWlanSystemConfig_ObjectIdentity((1,3,6,1,4,1,45,7,16,1,1))
_AvWlanSystemConfigScalars_ObjectIdentity=ObjectIdentity
avWlanSystemConfigScalars=_AvWlanSystemConfigScalars_ObjectIdentity((1,3,6,1,4,1,45,7,16,1,1,1))
class _AvWlanSystemConfigWirelessEnabled_Type(TruthValue):defaultValue=2
_AvWlanSystemConfigWirelessEnabled_Type.__name__=_G
_AvWlanSystemConfigWirelessEnabled_Object=MibScalar
avWlanSystemConfigWirelessEnabled=_AvWlanSystemConfigWirelessEnabled_Object((1,3,6,1,4,1,45,7,16,1,1,1,1),_AvWlanSystemConfigWirelessEnabled_Type())
avWlanSystemConfigWirelessEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:avWlanSystemConfigWirelessEnabled.setStatus(_A)
_AvWlanSystemConfigSystemInetAddressType_Type=InetAddressType
_AvWlanSystemConfigSystemInetAddressType_Object=MibScalar
avWlanSystemConfigSystemInetAddressType=_AvWlanSystemConfigSystemInetAddressType_Object((1,3,6,1,4,1,45,7,16,1,1,1,2),_AvWlanSystemConfigSystemInetAddressType_Type())
avWlanSystemConfigSystemInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:avWlanSystemConfigSystemInetAddressType.setStatus(_A)
_AvWlanSystemConfigSystemInetAddress_Type=InetAddress
_AvWlanSystemConfigSystemInetAddress_Object=MibScalar
avWlanSystemConfigSystemInetAddress=_AvWlanSystemConfigSystemInetAddress_Object((1,3,6,1,4,1,45,7,16,1,1,1,3),_AvWlanSystemConfigSystemInetAddress_Type())
avWlanSystemConfigSystemInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:avWlanSystemConfigSystemInetAddress.setStatus(_A)
class _AvWlanSystemConfigTcpUdpBasePort_Type(InetPortNumber):defaultValue=61000;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(49152,64983))
_AvWlanSystemConfigTcpUdpBasePort_Type.__name__=_F
_AvWlanSystemConfigTcpUdpBasePort_Object=MibScalar
avWlanSystemConfigTcpUdpBasePort=_AvWlanSystemConfigTcpUdpBasePort_Object((1,3,6,1,4,1,45,7,16,1,1,1,4),_AvWlanSystemConfigTcpUdpBasePort_Type())
avWlanSystemConfigTcpUdpBasePort.setMaxAccess(_D)
if mibBuilder.loadTexts:avWlanSystemConfigTcpUdpBasePort.setStatus(_A)
_AvWlanSystemStatus_ObjectIdentity=ObjectIdentity
avWlanSystemStatus=_AvWlanSystemStatus_ObjectIdentity((1,3,6,1,4,1,45,7,16,1,2))
_AvWlanSystemStatusScalars_ObjectIdentity=ObjectIdentity
avWlanSystemStatusScalars=_AvWlanSystemStatusScalars_ObjectIdentity((1,3,6,1,4,1,45,7,16,1,2,1))
class _AvWlanSystemStatusOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),('enablePending',2),('disabled',3),('disablePending',4)))
_AvWlanSystemStatusOperationalStatus_Type.__name__=_C
_AvWlanSystemStatusOperationalStatus_Object=MibScalar
avWlanSystemStatusOperationalStatus=_AvWlanSystemStatusOperationalStatus_Object((1,3,6,1,4,1,45,7,16,1,2,1,1),_AvWlanSystemStatusOperationalStatus_Type())
avWlanSystemStatusOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanSystemStatusOperationalStatus.setStatus(_A)
class _AvWlanSystemStatusOperationalStatusDisableReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('adminDisabled',2),('routingDisabled',3),('badSystemInetAddress',4),('badTcpUdpBasePort',5),('wirelessSystemError',6)))
_AvWlanSystemStatusOperationalStatusDisableReason_Type.__name__=_C
_AvWlanSystemStatusOperationalStatusDisableReason_Object=MibScalar
avWlanSystemStatusOperationalStatusDisableReason=_AvWlanSystemStatusOperationalStatusDisableReason_Object((1,3,6,1,4,1,45,7,16,1,2,1,2),_AvWlanSystemStatusOperationalStatusDisableReason_Type())
avWlanSystemStatusOperationalStatusDisableReason.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanSystemStatusOperationalStatusDisableReason.setStatus(_A)
_AvWlanSystemStatusWlanSystemAddrType_Type=InetAddressType
_AvWlanSystemStatusWlanSystemAddrType_Object=MibScalar
avWlanSystemStatusWlanSystemAddrType=_AvWlanSystemStatusWlanSystemAddrType_Object((1,3,6,1,4,1,45,7,16,1,2,1,3),_AvWlanSystemStatusWlanSystemAddrType_Type())
avWlanSystemStatusWlanSystemAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanSystemStatusWlanSystemAddrType.setStatus(_A)
class _AvWlanSystemStatusWlanSystemAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AvWlanSystemStatusWlanSystemAddr_Type.__name__=_E
_AvWlanSystemStatusWlanSystemAddr_Object=MibScalar
avWlanSystemStatusWlanSystemAddr=_AvWlanSystemStatusWlanSystemAddr_Object((1,3,6,1,4,1,45,7,16,1,2,1,4),_AvWlanSystemStatusWlanSystemAddr_Type())
avWlanSystemStatusWlanSystemAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanSystemStatusWlanSystemAddr.setStatus(_A)
class _AvWlanSystemStatusOperationalRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('wcp',1),('wsp',2),('wcpAndwsp',3)))
_AvWlanSystemStatusOperationalRole_Type.__name__=_C
_AvWlanSystemStatusOperationalRole_Object=MibScalar
avWlanSystemStatusOperationalRole=_AvWlanSystemStatusOperationalRole_Object((1,3,6,1,4,1,45,7,16,1,2,1,5),_AvWlanSystemStatusOperationalRole_Type())
avWlanSystemStatusOperationalRole.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanSystemStatusOperationalRole.setStatus(_A)
_AvWlanSystemStatusWlanVersion_Type=DisplayString
_AvWlanSystemStatusWlanVersion_Object=MibScalar
avWlanSystemStatusWlanVersion=_AvWlanSystemStatusWlanVersion_Object((1,3,6,1,4,1,45,7,16,1,2,1,6),_AvWlanSystemStatusWlanVersion_Type())
avWlanSystemStatusWlanVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanSystemStatusWlanVersion.setStatus(_A)
mibBuilder.exportSymbols('AVAYA-WLAN-SYSTEM-MIB',**{'avayaWlanSystemMib':avayaWlanSystemMib,'avWlanSystemObjects':avWlanSystemObjects,'avWlanSystemConfig':avWlanSystemConfig,'avWlanSystemConfigScalars':avWlanSystemConfigScalars,'avWlanSystemConfigWirelessEnabled':avWlanSystemConfigWirelessEnabled,'avWlanSystemConfigSystemInetAddressType':avWlanSystemConfigSystemInetAddressType,'avWlanSystemConfigSystemInetAddress':avWlanSystemConfigSystemInetAddress,'avWlanSystemConfigTcpUdpBasePort':avWlanSystemConfigTcpUdpBasePort,'avWlanSystemStatus':avWlanSystemStatus,'avWlanSystemStatusScalars':avWlanSystemStatusScalars,'avWlanSystemStatusOperationalStatus':avWlanSystemStatusOperationalStatus,'avWlanSystemStatusOperationalStatusDisableReason':avWlanSystemStatusOperationalStatusDisableReason,'avWlanSystemStatusWlanSystemAddrType':avWlanSystemStatusWlanSystemAddrType,'avWlanSystemStatusWlanSystemAddr':avWlanSystemStatusWlanSystemAddr,'avWlanSystemStatusOperationalRole':avWlanSystemStatusOperationalRole,'avWlanSystemStatusWlanVersion':avWlanSystemStatusWlanVersion})