_U='cIfXcvrMonStatusChangeNotifGroup'
_T='cIfXcvrDigitalDiagMonStatusGroup'
_S='cIfXcvrMonStatusChangeNotif'
_R='cIfXcvrMonStatusChangeNotifEnable'
_Q='Integer32'
_P='ifName'
_O='IF-MIB'
_N='cIfXcvrMonDigitalDiagTxFaultAlarm'
_M='cIfXcvrMonDigitalDiagTxPwrWarning'
_L='cIfXcvrMonDigitalDiagTxPwrAlarm'
_K='cIfXcvrMonDigitalDiagRxPwrWarning'
_J='cIfXcvrMonDigitalDiagRxPwrAlarm'
_I='cIfXcvrMonDigitalDiagCurrWarning'
_H='cIfXcvrMonDigitalDiagCurrAlarm'
_G='cIfXcvrMonDigitalDiagVoltWarning'
_F='cIfXcvrMonDigitalDiagVoltAlarm'
_E='cIfXcvrMonDigitalDiagTempWarning'
_D='cIfXcvrMonDigitalDiagTempAlarm'
_C='accessible-for-notify'
_B='current'
_A='CISCO-INTERFACE-XCVR-MONITOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifName,=mibBuilder.importSymbols(_O,_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Q,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoInterfaceXcvrMonitorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,706))
if mibBuilder.loadTexts:ciscoInterfaceXcvrMonitorMIB.setRevisions(('2009-10-09 00:00',))
class CiscoInterfaceXcvrMonitorStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('highSet',1),('lowSet',2),('highClear',3),('lowClear',4),('normal',5)))
_CiscoInterfaceXcvrMonMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoInterfaceXcvrMonMIBNotifs=_CiscoInterfaceXcvrMonMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,706,0))
_CiscoInterfaceXcvrMonMIBObjects_ObjectIdentity=ObjectIdentity
ciscoInterfaceXcvrMonMIBObjects=_CiscoInterfaceXcvrMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,706,1))
_CIfXcvrMonDigitalDiagTempAlarm_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTempAlarm_Object=MibScalar
cIfXcvrMonDigitalDiagTempAlarm=_CIfXcvrMonDigitalDiagTempAlarm_Object((1,3,6,1,4,1,9,9,706,1,1),_CIfXcvrMonDigitalDiagTempAlarm_Type())
cIfXcvrMonDigitalDiagTempAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagTempAlarm.setStatus(_B)
_CIfXcvrMonDigitalDiagTempWarning_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTempWarning_Object=MibScalar
cIfXcvrMonDigitalDiagTempWarning=_CIfXcvrMonDigitalDiagTempWarning_Object((1,3,6,1,4,1,9,9,706,1,2),_CIfXcvrMonDigitalDiagTempWarning_Type())
cIfXcvrMonDigitalDiagTempWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagTempWarning.setStatus(_B)
_CIfXcvrMonDigitalDiagVoltAlarm_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagVoltAlarm_Object=MibScalar
cIfXcvrMonDigitalDiagVoltAlarm=_CIfXcvrMonDigitalDiagVoltAlarm_Object((1,3,6,1,4,1,9,9,706,1,3),_CIfXcvrMonDigitalDiagVoltAlarm_Type())
cIfXcvrMonDigitalDiagVoltAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagVoltAlarm.setStatus(_B)
_CIfXcvrMonDigitalDiagVoltWarning_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagVoltWarning_Object=MibScalar
cIfXcvrMonDigitalDiagVoltWarning=_CIfXcvrMonDigitalDiagVoltWarning_Object((1,3,6,1,4,1,9,9,706,1,4),_CIfXcvrMonDigitalDiagVoltWarning_Type())
cIfXcvrMonDigitalDiagVoltWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagVoltWarning.setStatus(_B)
_CIfXcvrMonDigitalDiagCurrAlarm_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagCurrAlarm_Object=MibScalar
cIfXcvrMonDigitalDiagCurrAlarm=_CIfXcvrMonDigitalDiagCurrAlarm_Object((1,3,6,1,4,1,9,9,706,1,5),_CIfXcvrMonDigitalDiagCurrAlarm_Type())
cIfXcvrMonDigitalDiagCurrAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagCurrAlarm.setStatus(_B)
_CIfXcvrMonDigitalDiagCurrWarning_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagCurrWarning_Object=MibScalar
cIfXcvrMonDigitalDiagCurrWarning=_CIfXcvrMonDigitalDiagCurrWarning_Object((1,3,6,1,4,1,9,9,706,1,6),_CIfXcvrMonDigitalDiagCurrWarning_Type())
cIfXcvrMonDigitalDiagCurrWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagCurrWarning.setStatus(_B)
_CIfXcvrMonDigitalDiagRxPwrAlarm_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagRxPwrAlarm_Object=MibScalar
cIfXcvrMonDigitalDiagRxPwrAlarm=_CIfXcvrMonDigitalDiagRxPwrAlarm_Object((1,3,6,1,4,1,9,9,706,1,7),_CIfXcvrMonDigitalDiagRxPwrAlarm_Type())
cIfXcvrMonDigitalDiagRxPwrAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagRxPwrAlarm.setStatus(_B)
_CIfXcvrMonDigitalDiagRxPwrWarning_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagRxPwrWarning_Object=MibScalar
cIfXcvrMonDigitalDiagRxPwrWarning=_CIfXcvrMonDigitalDiagRxPwrWarning_Object((1,3,6,1,4,1,9,9,706,1,8),_CIfXcvrMonDigitalDiagRxPwrWarning_Type())
cIfXcvrMonDigitalDiagRxPwrWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagRxPwrWarning.setStatus(_B)
_CIfXcvrMonDigitalDiagTxPwrAlarm_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTxPwrAlarm_Object=MibScalar
cIfXcvrMonDigitalDiagTxPwrAlarm=_CIfXcvrMonDigitalDiagTxPwrAlarm_Object((1,3,6,1,4,1,9,9,706,1,9),_CIfXcvrMonDigitalDiagTxPwrAlarm_Type())
cIfXcvrMonDigitalDiagTxPwrAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagTxPwrAlarm.setStatus(_B)
_CIfXcvrMonDigitalDiagTxPwrWarning_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTxPwrWarning_Object=MibScalar
cIfXcvrMonDigitalDiagTxPwrWarning=_CIfXcvrMonDigitalDiagTxPwrWarning_Object((1,3,6,1,4,1,9,9,706,1,10),_CIfXcvrMonDigitalDiagTxPwrWarning_Type())
cIfXcvrMonDigitalDiagTxPwrWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagTxPwrWarning.setStatus(_B)
_CIfXcvrMonDigitalDiagTxFaultAlarm_Type=CiscoInterfaceXcvrMonitorStatus
_CIfXcvrMonDigitalDiagTxFaultAlarm_Object=MibScalar
cIfXcvrMonDigitalDiagTxFaultAlarm=_CIfXcvrMonDigitalDiagTxFaultAlarm_Object((1,3,6,1,4,1,9,9,706,1,11),_CIfXcvrMonDigitalDiagTxFaultAlarm_Type())
cIfXcvrMonDigitalDiagTxFaultAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cIfXcvrMonDigitalDiagTxFaultAlarm.setStatus(_B)
class _CIfXcvrMonStatusChangeNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CIfXcvrMonStatusChangeNotifEnable_Type.__name__=_Q
_CIfXcvrMonStatusChangeNotifEnable_Object=MibScalar
cIfXcvrMonStatusChangeNotifEnable=_CIfXcvrMonStatusChangeNotifEnable_Object((1,3,6,1,4,1,9,9,706,1,12),_CIfXcvrMonStatusChangeNotifEnable_Type())
cIfXcvrMonStatusChangeNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cIfXcvrMonStatusChangeNotifEnable.setStatus(_B)
_CiscoInterfaceXcvrMonMIBConform_ObjectIdentity=ObjectIdentity
ciscoInterfaceXcvrMonMIBConform=_CiscoInterfaceXcvrMonMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,706,2))
_CiscoInterfaceXcvrMonMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoInterfaceXcvrMonMIBCompliances=_CiscoInterfaceXcvrMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,706,2,1))
_CiscoInterfaceXcvrMonMIBGroups_ObjectIdentity=ObjectIdentity
ciscoInterfaceXcvrMonMIBGroups=_CiscoInterfaceXcvrMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,706,2,2))
cIfXcvrDigitalDiagMonStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,706,2,2,1))
cIfXcvrDigitalDiagMonStatusGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_R)))
if mibBuilder.loadTexts:cIfXcvrDigitalDiagMonStatusGroup.setStatus(_B)
cIfXcvrMonStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,706,0,1))
cIfXcvrMonStatusChangeNotif.setObjects(*((_O,_P),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cIfXcvrMonStatusChangeNotif.setStatus(_B)
cIfXcvrMonStatusChangeNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,706,2,2,2))
cIfXcvrMonStatusChangeNotifGroup.setObjects((_A,_S))
if mibBuilder.loadTexts:cIfXcvrMonStatusChangeNotifGroup.setStatus(_B)
cIfXcvrMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,706,2,1,1))
cIfXcvrMonMIBCompliance.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:cIfXcvrMonMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoInterfaceXcvrMonitorStatus':CiscoInterfaceXcvrMonitorStatus,'ciscoInterfaceXcvrMonitorMIB':ciscoInterfaceXcvrMonitorMIB,'ciscoInterfaceXcvrMonMIBNotifs':ciscoInterfaceXcvrMonMIBNotifs,_S:cIfXcvrMonStatusChangeNotif,'ciscoInterfaceXcvrMonMIBObjects':ciscoInterfaceXcvrMonMIBObjects,_D:cIfXcvrMonDigitalDiagTempAlarm,_E:cIfXcvrMonDigitalDiagTempWarning,_F:cIfXcvrMonDigitalDiagVoltAlarm,_G:cIfXcvrMonDigitalDiagVoltWarning,_H:cIfXcvrMonDigitalDiagCurrAlarm,_I:cIfXcvrMonDigitalDiagCurrWarning,_J:cIfXcvrMonDigitalDiagRxPwrAlarm,_K:cIfXcvrMonDigitalDiagRxPwrWarning,_L:cIfXcvrMonDigitalDiagTxPwrAlarm,_M:cIfXcvrMonDigitalDiagTxPwrWarning,_N:cIfXcvrMonDigitalDiagTxFaultAlarm,_R:cIfXcvrMonStatusChangeNotifEnable,'ciscoInterfaceXcvrMonMIBConform':ciscoInterfaceXcvrMonMIBConform,'ciscoInterfaceXcvrMonMIBCompliances':ciscoInterfaceXcvrMonMIBCompliances,'cIfXcvrMonMIBCompliance':cIfXcvrMonMIBCompliance,'ciscoInterfaceXcvrMonMIBGroups':ciscoInterfaceXcvrMonMIBGroups,_T:cIfXcvrDigitalDiagMonStatusGroup,_U:cIfXcvrMonStatusChangeNotifGroup})