_h='ogOMTRAPSNotificationsGroup'
_g='ogOMTRAPSMibGroup'
_f='ogOMTRAPSSensorTemperatureRangeAlert'
_e='ogOMTRAPSNetworkLinkStateAlert'
_d='ogOMTRAPSSerialPortLogoutAlert'
_c='ogOMTRAPSSerialPortLoginAlert'
_b='ogOMTRAPSConsoleLogin'
_a='ogOMTRAPSConfigChange'
_Z='ogOMTRAPSCellSignalAlert'
_Y='ogOMTRAPSReboot'
_X='ogOMTRAPSPSU2VoltageRangeAlert'
_W='ogOMTRAPSPSU1VoltageRangeAlert'
_V='ogOMTRAPSWebLogin'
_U='ogOMTRAPSSSHLogin'
_T='ogOMTRAPSConnectivityTest'
_S='ogOMTRAPSAlarmSummary'
_R='ogOMTRAPSSensorDevice'
_Q='ogOMTRAPSSensorTemperature'
_P='ogOMTRAPSNetworkLinkDescription'
_O='ogOMTRAPSNetworkLinkState'
_N='ogOMTRAPSConsoleLoginStatus'
_M='ogOMTRAPSCellSignal'
_L='ogOMTRAPSRebootStatus'
_K='ogOMTRAPSWebLoginStatus'
_J='ogOMTRAPSSSHLoginStatus'
_I='ogOMTRAPSConnectivityTestSignalStatus'
_H='ogOMTRAPSConnectivityTestSignal'
_G='ogOMTRAPSConnectivityTestResult'
_F='ogOMTRAPSSerialPortUser'
_E='ogOMTRAPSSerialPortID'
_D='ogOMTRAPSBusVoltage'
_C='read-only'
_B='current'
_A='OG-OMTRAPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogOMTRAPSMib=ModuleIdentity((1,3,6,1,4,1,25049,10,18))
if mibBuilder.loadTexts:ogOMTRAPSMib.setRevisions(('2020-11-10 15:00','2019-08-29 15:00','2019-08-07 15:00'))
_OgOMTRAPSObjects_ObjectIdentity=ObjectIdentity
ogOMTRAPSObjects=_OgOMTRAPSObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,18,1))
_OgOMTRAPSEvent_ObjectIdentity=ObjectIdentity
ogOMTRAPSEvent=_OgOMTRAPSEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,18,1,1))
_OgOMTRAPSConnectivityTestResult_Type=DisplayString
_OgOMTRAPSConnectivityTestResult_Object=MibScalar
ogOMTRAPSConnectivityTestResult=_OgOMTRAPSConnectivityTestResult_Object((1,3,6,1,4,1,25049,10,18,1,1,1),_OgOMTRAPSConnectivityTestResult_Type())
ogOMTRAPSConnectivityTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSConnectivityTestResult.setStatus(_B)
_OgOMTRAPSConnectivityTestSignal_Type=DisplayString
_OgOMTRAPSConnectivityTestSignal_Object=MibScalar
ogOMTRAPSConnectivityTestSignal=_OgOMTRAPSConnectivityTestSignal_Object((1,3,6,1,4,1,25049,10,18,1,1,2),_OgOMTRAPSConnectivityTestSignal_Type())
ogOMTRAPSConnectivityTestSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSConnectivityTestSignal.setStatus(_B)
_OgOMTRAPSConnectivityTestSignalStatus_Type=DisplayString
_OgOMTRAPSConnectivityTestSignalStatus_Object=MibScalar
ogOMTRAPSConnectivityTestSignalStatus=_OgOMTRAPSConnectivityTestSignalStatus_Object((1,3,6,1,4,1,25049,10,18,1,1,3),_OgOMTRAPSConnectivityTestSignalStatus_Type())
ogOMTRAPSConnectivityTestSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSConnectivityTestSignalStatus.setStatus(_B)
_OgOMTRAPSSSHLoginStatus_Type=DisplayString
_OgOMTRAPSSSHLoginStatus_Object=MibScalar
ogOMTRAPSSSHLoginStatus=_OgOMTRAPSSSHLoginStatus_Object((1,3,6,1,4,1,25049,10,18,1,1,4),_OgOMTRAPSSSHLoginStatus_Type())
ogOMTRAPSSSHLoginStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSSSHLoginStatus.setStatus(_B)
_OgOMTRAPSWebLoginStatus_Type=DisplayString
_OgOMTRAPSWebLoginStatus_Object=MibScalar
ogOMTRAPSWebLoginStatus=_OgOMTRAPSWebLoginStatus_Object((1,3,6,1,4,1,25049,10,18,1,1,5),_OgOMTRAPSWebLoginStatus_Type())
ogOMTRAPSWebLoginStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSWebLoginStatus.setStatus(_B)
_OgOMTRAPSBusVoltage_Type=Integer32
_OgOMTRAPSBusVoltage_Object=MibScalar
ogOMTRAPSBusVoltage=_OgOMTRAPSBusVoltage_Object((1,3,6,1,4,1,25049,10,18,1,1,6),_OgOMTRAPSBusVoltage_Type())
ogOMTRAPSBusVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSBusVoltage.setStatus(_B)
if mibBuilder.loadTexts:ogOMTRAPSBusVoltage.setUnits('0.1 Volt DC')
_OgOMTRAPSRebootStatus_Type=DisplayString
_OgOMTRAPSRebootStatus_Object=MibScalar
ogOMTRAPSRebootStatus=_OgOMTRAPSRebootStatus_Object((1,3,6,1,4,1,25049,10,18,1,1,7),_OgOMTRAPSRebootStatus_Type())
ogOMTRAPSRebootStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSRebootStatus.setStatus(_B)
_OgOMTRAPSCellSignal_Type=Integer32
_OgOMTRAPSCellSignal_Object=MibScalar
ogOMTRAPSCellSignal=_OgOMTRAPSCellSignal_Object((1,3,6,1,4,1,25049,10,18,1,1,8),_OgOMTRAPSCellSignal_Type())
ogOMTRAPSCellSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSCellSignal.setStatus(_B)
_OgOMTRAPSConsoleLoginStatus_Type=DisplayString
_OgOMTRAPSConsoleLoginStatus_Object=MibScalar
ogOMTRAPSConsoleLoginStatus=_OgOMTRAPSConsoleLoginStatus_Object((1,3,6,1,4,1,25049,10,18,1,1,9),_OgOMTRAPSConsoleLoginStatus_Type())
ogOMTRAPSConsoleLoginStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSConsoleLoginStatus.setStatus(_B)
_OgOMTRAPSSerialPortID_Type=DisplayString
_OgOMTRAPSSerialPortID_Object=MibScalar
ogOMTRAPSSerialPortID=_OgOMTRAPSSerialPortID_Object((1,3,6,1,4,1,25049,10,18,1,1,10),_OgOMTRAPSSerialPortID_Type())
ogOMTRAPSSerialPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSSerialPortID.setStatus(_B)
_OgOMTRAPSSerialPortUser_Type=DisplayString
_OgOMTRAPSSerialPortUser_Object=MibScalar
ogOMTRAPSSerialPortUser=_OgOMTRAPSSerialPortUser_Object((1,3,6,1,4,1,25049,10,18,1,1,11),_OgOMTRAPSSerialPortUser_Type())
ogOMTRAPSSerialPortUser.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSSerialPortUser.setStatus(_B)
_OgOMTRAPSNetworkLinkState_Type=DisplayString
_OgOMTRAPSNetworkLinkState_Object=MibScalar
ogOMTRAPSNetworkLinkState=_OgOMTRAPSNetworkLinkState_Object((1,3,6,1,4,1,25049,10,18,1,1,12),_OgOMTRAPSNetworkLinkState_Type())
ogOMTRAPSNetworkLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSNetworkLinkState.setStatus(_B)
_OgOMTRAPSNetworkLinkDescription_Type=DisplayString
_OgOMTRAPSNetworkLinkDescription_Object=MibScalar
ogOMTRAPSNetworkLinkDescription=_OgOMTRAPSNetworkLinkDescription_Object((1,3,6,1,4,1,25049,10,18,1,1,13),_OgOMTRAPSNetworkLinkDescription_Type())
ogOMTRAPSNetworkLinkDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSNetworkLinkDescription.setStatus(_B)
_OgOMTRAPSSensorTemperature_Type=Integer32
_OgOMTRAPSSensorTemperature_Object=MibScalar
ogOMTRAPSSensorTemperature=_OgOMTRAPSSensorTemperature_Object((1,3,6,1,4,1,25049,10,18,1,1,14),_OgOMTRAPSSensorTemperature_Type())
ogOMTRAPSSensorTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSSensorTemperature.setStatus(_B)
if mibBuilder.loadTexts:ogOMTRAPSSensorTemperature.setUnits('millidegrees Celsius')
_OgOMTRAPSSensorDevice_Type=DisplayString
_OgOMTRAPSSensorDevice_Object=MibScalar
ogOMTRAPSSensorDevice=_OgOMTRAPSSensorDevice_Object((1,3,6,1,4,1,25049,10,18,1,1,15),_OgOMTRAPSSensorDevice_Type())
ogOMTRAPSSensorDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSSensorDevice.setStatus(_B)
_OgOMTRAPSAlarmSummary_Type=DisplayString
_OgOMTRAPSAlarmSummary_Object=MibScalar
ogOMTRAPSAlarmSummary=_OgOMTRAPSAlarmSummary_Object((1,3,6,1,4,1,25049,10,18,1,1,16),_OgOMTRAPSAlarmSummary_Type())
ogOMTRAPSAlarmSummary.setMaxAccess(_C)
if mibBuilder.loadTexts:ogOMTRAPSAlarmSummary.setStatus(_B)
_OgOMTRAPSNotificationPrefix_ObjectIdentity=ObjectIdentity
ogOMTRAPSNotificationPrefix=_OgOMTRAPSNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,18,2))
_OgOMTRAPSNotification_ObjectIdentity=ObjectIdentity
ogOMTRAPSNotification=_OgOMTRAPSNotification_ObjectIdentity((1,3,6,1,4,1,25049,10,18,2,0))
_OgOMTRAPSMibConformance_ObjectIdentity=ObjectIdentity
ogOMTRAPSMibConformance=_OgOMTRAPSMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,18,3))
_OgOMTRAPSMibCompliances_ObjectIdentity=ObjectIdentity
ogOMTRAPSMibCompliances=_OgOMTRAPSMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,18,3,1))
_OgOMTRAPSMibGroups_ObjectIdentity=ObjectIdentity
ogOMTRAPSMibGroups=_OgOMTRAPSMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,18,3,2))
ogOMTRAPSMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,18,3,2,1))
ogOMTRAPSMibGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_D),(_A,_L),(_A,_M),(_A,_N),(_A,_E),(_A,_F),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ogOMTRAPSMibGroup.setStatus(_B)
ogOMTRAPSConnectivityTest=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,1))
ogOMTRAPSConnectivityTest.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ogOMTRAPSConnectivityTest.setStatus(_B)
ogOMTRAPSSSHLogin=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,2))
ogOMTRAPSSSHLogin.setObjects((_A,_J))
if mibBuilder.loadTexts:ogOMTRAPSSSHLogin.setStatus(_B)
ogOMTRAPSWebLogin=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,3))
ogOMTRAPSWebLogin.setObjects((_A,_K))
if mibBuilder.loadTexts:ogOMTRAPSWebLogin.setStatus(_B)
ogOMTRAPSPSU1VoltageRangeAlert=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,4))
ogOMTRAPSPSU1VoltageRangeAlert.setObjects((_A,_D))
if mibBuilder.loadTexts:ogOMTRAPSPSU1VoltageRangeAlert.setStatus(_B)
ogOMTRAPSPSU2VoltageRangeAlert=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,5))
ogOMTRAPSPSU2VoltageRangeAlert.setObjects((_A,_D))
if mibBuilder.loadTexts:ogOMTRAPSPSU2VoltageRangeAlert.setStatus(_B)
ogOMTRAPSReboot=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,6))
ogOMTRAPSReboot.setObjects((_A,_L))
if mibBuilder.loadTexts:ogOMTRAPSReboot.setStatus(_B)
ogOMTRAPSCellSignalAlert=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,7))
ogOMTRAPSCellSignalAlert.setObjects((_A,_M))
if mibBuilder.loadTexts:ogOMTRAPSCellSignalAlert.setStatus(_B)
ogOMTRAPSConfigChange=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,8))
if mibBuilder.loadTexts:ogOMTRAPSConfigChange.setStatus(_B)
ogOMTRAPSConsoleLogin=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,9))
ogOMTRAPSConsoleLogin.setObjects((_A,_N))
if mibBuilder.loadTexts:ogOMTRAPSConsoleLogin.setStatus(_B)
ogOMTRAPSSerialPortLoginAlert=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,10))
ogOMTRAPSSerialPortLoginAlert.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ogOMTRAPSSerialPortLoginAlert.setStatus(_B)
ogOMTRAPSSerialPortLogoutAlert=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,11))
ogOMTRAPSSerialPortLogoutAlert.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ogOMTRAPSSerialPortLogoutAlert.setStatus(_B)
ogOMTRAPSNetworkLinkStateAlert=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,12))
ogOMTRAPSNetworkLinkStateAlert.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ogOMTRAPSNetworkLinkStateAlert.setStatus(_B)
ogOMTRAPSSensorTemperatureRangeAlert=NotificationType((1,3,6,1,4,1,25049,10,18,2,0,13))
ogOMTRAPSSensorTemperatureRangeAlert.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ogOMTRAPSSensorTemperatureRangeAlert.setStatus(_B)
ogOMTRAPSNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,18,3,2,2))
ogOMTRAPSNotificationsGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ogOMTRAPSNotificationsGroup.setStatus(_B)
ogOMTRAPSMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,18,3,1,1))
ogOMTRAPSMibCompliance.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ogOMTRAPSMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ogOMTRAPSMib':ogOMTRAPSMib,'ogOMTRAPSObjects':ogOMTRAPSObjects,'ogOMTRAPSEvent':ogOMTRAPSEvent,_G:ogOMTRAPSConnectivityTestResult,_H:ogOMTRAPSConnectivityTestSignal,_I:ogOMTRAPSConnectivityTestSignalStatus,_J:ogOMTRAPSSSHLoginStatus,_K:ogOMTRAPSWebLoginStatus,_D:ogOMTRAPSBusVoltage,_L:ogOMTRAPSRebootStatus,_M:ogOMTRAPSCellSignal,_N:ogOMTRAPSConsoleLoginStatus,_E:ogOMTRAPSSerialPortID,_F:ogOMTRAPSSerialPortUser,_O:ogOMTRAPSNetworkLinkState,_P:ogOMTRAPSNetworkLinkDescription,_Q:ogOMTRAPSSensorTemperature,_R:ogOMTRAPSSensorDevice,_S:ogOMTRAPSAlarmSummary,'ogOMTRAPSNotificationPrefix':ogOMTRAPSNotificationPrefix,'ogOMTRAPSNotification':ogOMTRAPSNotification,_T:ogOMTRAPSConnectivityTest,_U:ogOMTRAPSSSHLogin,_V:ogOMTRAPSWebLogin,_W:ogOMTRAPSPSU1VoltageRangeAlert,_X:ogOMTRAPSPSU2VoltageRangeAlert,_Y:ogOMTRAPSReboot,_Z:ogOMTRAPSCellSignalAlert,_a:ogOMTRAPSConfigChange,_b:ogOMTRAPSConsoleLogin,_c:ogOMTRAPSSerialPortLoginAlert,_d:ogOMTRAPSSerialPortLogoutAlert,_e:ogOMTRAPSNetworkLinkStateAlert,_f:ogOMTRAPSSensorTemperatureRangeAlert,'ogOMTRAPSMibConformance':ogOMTRAPSMibConformance,'ogOMTRAPSMibCompliances':ogOMTRAPSMibCompliances,'ogOMTRAPSMibCompliance':ogOMTRAPSMibCompliance,'ogOMTRAPSMibGroups':ogOMTRAPSMibGroups,_g:ogOMTRAPSMibGroup,_h:ogOMTRAPSNotificationsGroup})