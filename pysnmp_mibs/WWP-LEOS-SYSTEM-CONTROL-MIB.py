_D='TruthValue'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPort,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dStpPort')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_D)
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosSysCtrlMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,25))
if mibBuilder.loadTexts:wwpLeosSysCtrlMIB.setRevisions(('2006-03-15 18:55','2001-04-03 17:00'))
_WwpLeosSysCtrlMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrlMIBObjects=_WwpLeosSysCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,1))
_WwpLeosSysCtrl_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrl=_WwpLeosSysCtrl_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,1,1))
class _WwpLeosSysCtrlBridgeRstpEnable_Type(TruthValue):defaultValue=2
_WwpLeosSysCtrlBridgeRstpEnable_Type.__name__=_D
_WwpLeosSysCtrlBridgeRstpEnable_Object=MibScalar
wwpLeosSysCtrlBridgeRstpEnable=_WwpLeosSysCtrlBridgeRstpEnable_Object((1,3,6,1,4,1,6141,2,60,25,1,1,1),_WwpLeosSysCtrlBridgeRstpEnable_Type())
wwpLeosSysCtrlBridgeRstpEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpLeosSysCtrlBridgeRstpEnable.setStatus(_B)
class _WwpLeosSysCtrlLacpEnable_Type(TruthValue):defaultValue=1
_WwpLeosSysCtrlLacpEnable_Type.__name__=_D
_WwpLeosSysCtrlLacpEnable_Object=MibScalar
wwpLeosSysCtrlLacpEnable=_WwpLeosSysCtrlLacpEnable_Object((1,3,6,1,4,1,6141,2,60,25,1,1,2),_WwpLeosSysCtrlLacpEnable_Type())
wwpLeosSysCtrlLacpEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpLeosSysCtrlLacpEnable.setStatus(_B)
class _WwpLeosSysCtrlLldpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('disabled',2),('enabled',3)))
_WwpLeosSysCtrlLldpState_Type.__name__=_C
_WwpLeosSysCtrlLldpState_Object=MibScalar
wwpLeosSysCtrlLldpState=_WwpLeosSysCtrlLldpState_Object((1,3,6,1,4,1,6141,2,60,25,1,1,3),_WwpLeosSysCtrlLldpState_Type())
wwpLeosSysCtrlLldpState.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpLeosSysCtrlLldpState.setStatus(_B)
_WwpLeosSysCtrlLldpExt_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrlLldpExt=_WwpLeosSysCtrlLldpExt_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,1,2))
_WwpLeosSysCtrlLldpDaMac_Type=MacAddress
_WwpLeosSysCtrlLldpDaMac_Object=MibScalar
wwpLeosSysCtrlLldpDaMac=_WwpLeosSysCtrlLldpDaMac_Object((1,3,6,1,4,1,6141,2,60,25,1,2,1),_WwpLeosSysCtrlLldpDaMac_Type())
wwpLeosSysCtrlLldpDaMac.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpLeosSysCtrlLldpDaMac.setStatus(_B)
class _WwpLeosSysCtrlLldpEthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosSysCtrlLldpEthType_Type.__name__=_C
_WwpLeosSysCtrlLldpEthType_Object=MibScalar
wwpLeosSysCtrlLldpEthType=_WwpLeosSysCtrlLldpEthType_Object((1,3,6,1,4,1,6141,2,60,25,1,2,2),_WwpLeosSysCtrlLldpEthType_Type())
wwpLeosSysCtrlLldpEthType.setMaxAccess(_A)
if mibBuilder.loadTexts:wwpLeosSysCtrlLldpEthType.setStatus(_B)
_WwpLeosSysCtrlMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrlMIBNotificationPrefix=_WwpLeosSysCtrlMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,2))
_WwpLeosSysCtrlMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrlMIBNotifications=_WwpLeosSysCtrlMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,2,0))
_WwpLeosSysCtrlMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrlMIBConformance=_WwpLeosSysCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,3))
_WwpLeosSysCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrlMIBCompliances=_WwpLeosSysCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,3,1))
_WwpLeosSysCtrlMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosSysCtrlMIBGroups=_WwpLeosSysCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,25,3,2))
mibBuilder.exportSymbols('WWP-LEOS-SYSTEM-CONTROL-MIB',**{'wwpLeosSysCtrlMIB':wwpLeosSysCtrlMIB,'wwpLeosSysCtrlMIBObjects':wwpLeosSysCtrlMIBObjects,'wwpLeosSysCtrl':wwpLeosSysCtrl,'wwpLeosSysCtrlBridgeRstpEnable':wwpLeosSysCtrlBridgeRstpEnable,'wwpLeosSysCtrlLacpEnable':wwpLeosSysCtrlLacpEnable,'wwpLeosSysCtrlLldpState':wwpLeosSysCtrlLldpState,'wwpLeosSysCtrlLldpExt':wwpLeosSysCtrlLldpExt,'wwpLeosSysCtrlLldpDaMac':wwpLeosSysCtrlLldpDaMac,'wwpLeosSysCtrlLldpEthType':wwpLeosSysCtrlLldpEthType,'wwpLeosSysCtrlMIBNotificationPrefix':wwpLeosSysCtrlMIBNotificationPrefix,'wwpLeosSysCtrlMIBNotifications':wwpLeosSysCtrlMIBNotifications,'wwpLeosSysCtrlMIBConformance':wwpLeosSysCtrlMIBConformance,'wwpLeosSysCtrlMIBCompliances':wwpLeosSysCtrlMIBCompliances,'wwpLeosSysCtrlMIBGroups':wwpLeosSysCtrlMIBGroups})