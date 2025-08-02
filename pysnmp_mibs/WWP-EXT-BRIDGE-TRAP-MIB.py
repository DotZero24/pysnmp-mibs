_L='read-write'
_K='wwpPortType'
_J='wwpPortOperStatus'
_I='wwpPortName'
_H='wwpPortId'
_G='wwpPortAdminStatus'
_F='TruthValue'
_E='sysName'
_D='sysLocation'
_C='current'
_B='SNMPv2-MIB'
_A='WWP-EXT-BRIDGE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,sysName=mibBuilder.importSymbols(_B,_D,_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
wwpPortAdminStatus,wwpPortId,wwpPortName,wwpPortOperStatus,wwpPortType=mibBuilder.importSymbols(_A,_G,_H,_I,_J,_K)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpExtBridgeTrapMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,41))
if mibBuilder.loadTexts:wwpExtBridgeTrapMIB.setRevisions(('2002-10-27 17:00',))
_WwpExtBridgeTrapMIBObjects_ObjectIdentity=ObjectIdentity
wwpExtBridgeTrapMIBObjects=_WwpExtBridgeTrapMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,41,1))
class _WwpStndLinkUpDownTrapsEnable_Type(TruthValue):defaultValue=1
_WwpStndLinkUpDownTrapsEnable_Type.__name__=_F
_WwpStndLinkUpDownTrapsEnable_Object=MibScalar
wwpStndLinkUpDownTrapsEnable=_WwpStndLinkUpDownTrapsEnable_Object((1,3,6,1,4,1,6141,2,41,1,1),_WwpStndLinkUpDownTrapsEnable_Type())
wwpStndLinkUpDownTrapsEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:wwpStndLinkUpDownTrapsEnable.setStatus(_C)
class _WwpLinkUpDownTrapsEnable_Type(TruthValue):defaultValue=2
_WwpLinkUpDownTrapsEnable_Type.__name__=_F
_WwpLinkUpDownTrapsEnable_Object=MibScalar
wwpLinkUpDownTrapsEnable=_WwpLinkUpDownTrapsEnable_Object((1,3,6,1,4,1,6141,2,41,1,2),_WwpLinkUpDownTrapsEnable_Type())
wwpLinkUpDownTrapsEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:wwpLinkUpDownTrapsEnable.setStatus(_C)
_WwpExtBridgeTrapMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpExtBridgeTrapMIBNotificationPrefix=_WwpExtBridgeTrapMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,41,2))
_WwpExtBridgeTrapMIBNotifications_ObjectIdentity=ObjectIdentity
wwpExtBridgeTrapMIBNotifications=_WwpExtBridgeTrapMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,41,2,0))
_WwpExtBridgeTrapMIBConformance_ObjectIdentity=ObjectIdentity
wwpExtBridgeTrapMIBConformance=_WwpExtBridgeTrapMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,41,3))
_WwpExtBridgeTrapMIBCompliances_ObjectIdentity=ObjectIdentity
wwpExtBridgeTrapMIBCompliances=_WwpExtBridgeTrapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,41,3,1))
_WwpExtBridgeTrapMIBGroups_ObjectIdentity=ObjectIdentity
wwpExtBridgeTrapMIBGroups=_WwpExtBridgeTrapMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,41,3,2))
wwpLinkUp=NotificationType((1,3,6,1,4,1,6141,2,41,2,0,1))
wwpLinkUp.setObjects(*((_B,_E),(_B,_D),(_A,_H),(_A,_I),(_A,_K),(_A,_G),(_A,_J)))
if mibBuilder.loadTexts:wwpLinkUp.setStatus(_C)
wwpLinkDown=NotificationType((1,3,6,1,4,1,6141,2,41,2,0,2))
wwpLinkDown.setObjects(*((_B,_E),(_B,_D),(_A,_H),(_A,_K),(_A,_I),(_A,_G),(_A,_J)))
if mibBuilder.loadTexts:wwpLinkDown.setStatus(_C)
mibBuilder.exportSymbols('WWP-EXT-BRIDGE-TRAP-MIB',**{'wwpExtBridgeTrapMIB':wwpExtBridgeTrapMIB,'wwpExtBridgeTrapMIBObjects':wwpExtBridgeTrapMIBObjects,'wwpStndLinkUpDownTrapsEnable':wwpStndLinkUpDownTrapsEnable,'wwpLinkUpDownTrapsEnable':wwpLinkUpDownTrapsEnable,'wwpExtBridgeTrapMIBNotificationPrefix':wwpExtBridgeTrapMIBNotificationPrefix,'wwpExtBridgeTrapMIBNotifications':wwpExtBridgeTrapMIBNotifications,'wwpLinkUp':wwpLinkUp,'wwpLinkDown':wwpLinkDown,'wwpExtBridgeTrapMIBConformance':wwpExtBridgeTrapMIBConformance,'wwpExtBridgeTrapMIBCompliances':wwpExtBridgeTrapMIBCompliances,'wwpExtBridgeTrapMIBGroups':wwpExtBridgeTrapMIBGroups})