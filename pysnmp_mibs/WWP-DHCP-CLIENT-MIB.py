_E='TruthValue'
_D='DisplayString'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention',_E)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpDhcpClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,18))
if mibBuilder.loadTexts:wwpDhcpClientMIB.setRevisions(('2001-04-03 17:00',))
_WwpDhcpClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpDhcpClientMIBObjects=_WwpDhcpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,18,1))
_WwpDhcpClient_ObjectIdentity=ObjectIdentity
wwpDhcpClient=_WwpDhcpClient_ObjectIdentity((1,3,6,1,4,1,6141,2,18,1,1))
class _WwpDhcpActivate_Type(TruthValue):defaultValue=2
_WwpDhcpActivate_Type.__name__=_E
_WwpDhcpActivate_Object=MibScalar
wwpDhcpActivate=_WwpDhcpActivate_Object((1,3,6,1,4,1,6141,2,18,1,1,1),_WwpDhcpActivate_Type())
wwpDhcpActivate.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpDhcpActivate.setStatus(_B)
class _WwpDhcpIfName_Type(DisplayString):defaultValue=OctetString('mgmt');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpDhcpIfName_Type.__name__=_D
_WwpDhcpIfName_Object=MibScalar
wwpDhcpIfName=_WwpDhcpIfName_Object((1,3,6,1,4,1,6141,2,18,1,1,2),_WwpDhcpIfName_Type())
wwpDhcpIfName.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpDhcpIfName.setStatus(_B)
class _WwpDhcpDiscoveryMsgInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpDiscoveryMsgInterval_Type.__name__=_C
_WwpDhcpDiscoveryMsgInterval_Object=MibScalar
wwpDhcpDiscoveryMsgInterval=_WwpDhcpDiscoveryMsgInterval_Object((1,3,6,1,4,1,6141,2,18,1,1,3),_WwpDhcpDiscoveryMsgInterval_Type())
wwpDhcpDiscoveryMsgInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpDhcpDiscoveryMsgInterval.setStatus(_B)
if mibBuilder.loadTexts:wwpDhcpDiscoveryMsgInterval.setUnits('miliseconds')
class _WwpDhcpLeaseTime_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpLeaseTime_Type.__name__=_C
_WwpDhcpLeaseTime_Object=MibScalar
wwpDhcpLeaseTime=_WwpDhcpLeaseTime_Object((1,3,6,1,4,1,6141,2,18,1,1,4),_WwpDhcpLeaseTime_Type())
wwpDhcpLeaseTime.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpDhcpLeaseTime.setStatus(_B)
if mibBuilder.loadTexts:wwpDhcpLeaseTime.setUnits('Hours')
_WwpDhcpClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpDhcpClientMIBNotificationPrefix=_WwpDhcpClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,18,2))
_WwpDhcpClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpDhcpClientMIBNotifications=_WwpDhcpClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,18,2,0))
_WwpDhcpClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpDhcpClientMIBConformance=_WwpDhcpClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,18,3))
_WwpDhcpClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpDhcpClientMIBCompliances=_WwpDhcpClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,18,3,1))
_WwpDhcpClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpDhcpClientMIBGroups=_WwpDhcpClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,18,3,2))
mibBuilder.exportSymbols('WWP-DHCP-CLIENT-MIB',**{'wwpDhcpClientMIB':wwpDhcpClientMIB,'wwpDhcpClientMIBObjects':wwpDhcpClientMIBObjects,'wwpDhcpClient':wwpDhcpClient,'wwpDhcpActivate':wwpDhcpActivate,'wwpDhcpIfName':wwpDhcpIfName,'wwpDhcpDiscoveryMsgInterval':wwpDhcpDiscoveryMsgInterval,'wwpDhcpLeaseTime':wwpDhcpLeaseTime,'wwpDhcpClientMIBNotificationPrefix':wwpDhcpClientMIBNotificationPrefix,'wwpDhcpClientMIBNotifications':wwpDhcpClientMIBNotifications,'wwpDhcpClientMIBConformance':wwpDhcpClientMIBConformance,'wwpDhcpClientMIBCompliances':wwpDhcpClientMIBCompliances,'wwpDhcpClientMIBGroups':wwpDhcpClientMIBGroups})