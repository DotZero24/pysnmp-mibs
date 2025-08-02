_E='read-write'
_D='dot1dStpPort'
_C='BRIDGE-MIB'
_B='current'
_A='TruthValue'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPort,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_A)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpSysCtrlMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,30))
if mibBuilder.loadTexts:wwpSysCtrlMIB.setRevisions(('2001-04-03 17:00',))
_WwpSysCtrlMIBObjects_ObjectIdentity=ObjectIdentity
wwpSysCtrlMIBObjects=_WwpSysCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,30,1))
_WwpSysCtrl_ObjectIdentity=ObjectIdentity
wwpSysCtrl=_WwpSysCtrl_ObjectIdentity((1,3,6,1,4,1,6141,2,30,1,1))
class _WwpSysCtrlBridgeRSTPEnable_Type(TruthValue):defaultValue=2
_WwpSysCtrlBridgeRSTPEnable_Type.__name__=_A
_WwpSysCtrlBridgeRSTPEnable_Object=MibScalar
wwpSysCtrlBridgeRSTPEnable=_WwpSysCtrlBridgeRSTPEnable_Object((1,3,6,1,4,1,6141,2,30,1,1,1),_WwpSysCtrlBridgeRSTPEnable_Type())
wwpSysCtrlBridgeRSTPEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpSysCtrlBridgeRSTPEnable.setStatus(_B)
class _WwpSysCtrlLacpEnable_Type(TruthValue):defaultValue=2
_WwpSysCtrlLacpEnable_Type.__name__=_A
_WwpSysCtrlLacpEnable_Object=MibScalar
wwpSysCtrlLacpEnable=_WwpSysCtrlLacpEnable_Object((1,3,6,1,4,1,6141,2,30,1,1,2),_WwpSysCtrlLacpEnable_Type())
wwpSysCtrlLacpEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpSysCtrlLacpEnable.setStatus(_B)
_WwpSysCtrlMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpSysCtrlMIBNotificationPrefix=_WwpSysCtrlMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,30,2))
_WwpSysCtrlMIBNotifications_ObjectIdentity=ObjectIdentity
wwpSysCtrlMIBNotifications=_WwpSysCtrlMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,30,2,0))
_WwpSysCtrlMIBConformance_ObjectIdentity=ObjectIdentity
wwpSysCtrlMIBConformance=_WwpSysCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,30,3))
_WwpSysCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
wwpSysCtrlMIBCompliances=_WwpSysCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,30,3,1))
_WwpSysCtrlMIBGroups_ObjectIdentity=ObjectIdentity
wwpSysCtrlMIBGroups=_WwpSysCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,30,3,2))
wwpPvstBpduReceived=NotificationType((1,3,6,1,4,1,6141,2,30,2,0,1))
wwpPvstBpduReceived.setObjects((_C,_D))
if mibBuilder.loadTexts:wwpPvstBpduReceived.setStatus(_B)
mibBuilder.exportSymbols('WWP-SYSTEM-CONTROL-MIB',**{'wwpSysCtrlMIB':wwpSysCtrlMIB,'wwpSysCtrlMIBObjects':wwpSysCtrlMIBObjects,'wwpSysCtrl':wwpSysCtrl,'wwpSysCtrlBridgeRSTPEnable':wwpSysCtrlBridgeRSTPEnable,'wwpSysCtrlLacpEnable':wwpSysCtrlLacpEnable,'wwpSysCtrlMIBNotificationPrefix':wwpSysCtrlMIBNotificationPrefix,'wwpSysCtrlMIBNotifications':wwpSysCtrlMIBNotifications,'wwpPvstBpduReceived':wwpPvstBpduReceived,'wwpSysCtrlMIBConformance':wwpSysCtrlMIBConformance,'wwpSysCtrlMIBCompliances':wwpSysCtrlMIBCompliances,'wwpSysCtrlMIBGroups':wwpSysCtrlMIBGroups})