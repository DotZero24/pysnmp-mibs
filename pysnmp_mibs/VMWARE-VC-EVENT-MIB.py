_T='vmwVCAlarmNotificationGroup'
_S='vmwVCAlarmGroup'
_R='vmwVCNotificationGroup'
_Q='vmwVCAlarmInfoGroup'
_P='vpxdAlarmInfo'
_O='vpxdAlarm'
_N='Integer32'
_M='vpxdDiagnostic'
_L='vmwVpxdTargetObj'
_K='vmwVpxdTargetObjType'
_J='vmwVpxdVMName'
_I='vmwVpxdHostName'
_H='vmwVpxdTrapType'
_G='vmwVpxdObjValue'
_F='vmwVpxdNewStatus'
_E='vmwVpxdOldStatus'
_D='obsolete'
_C='accessible-for-notify'
_B='current'
_A='VMWARE-VC-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwVC,=mibBuilder.importSymbols('VMWARE-PRODUCTS-MIB','vmwVC')
VmwLongSnmpAdminString,=mibBuilder.importSymbols('VMWARE-TC-MIB','VmwLongSnmpAdminString')
vmwVCMIB=ModuleIdentity((1,3,6,1,4,1,6876,4,3,1))
if mibBuilder.loadTexts:vmwVCMIB.setRevisions(('2009-12-15 00:00','2009-09-08 00:00','2009-05-27 00:00','2009-04-06 00:00','2009-03-17 00:00','2008-02-22 00:00'))
_VmwVCNotifications_ObjectIdentity=ObjectIdentity
vmwVCNotifications=_VmwVCNotifications_ObjectIdentity((1,3,6,1,4,1,6876,4,3,0))
_VmwVCMIBConformance_ObjectIdentity=ObjectIdentity
vmwVCMIBConformance=_VmwVCMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,4,3,1,2))
_VmwVCMIBCompliances_ObjectIdentity=ObjectIdentity
vmwVCMIBCompliances=_VmwVCMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,4,3,1,2,1))
_VmwVCMIBGroups_ObjectIdentity=ObjectIdentity
vmwVCMIBGroups=_VmwVCMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,4,3,1,2,2))
_VmwVpxdTrapType_Type=SnmpAdminString
_VmwVpxdTrapType_Object=MibScalar
vmwVpxdTrapType=_VmwVpxdTrapType_Object((1,3,6,1,4,1,6876,4,3,301),_VmwVpxdTrapType_Type())
vmwVpxdTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdTrapType.setStatus(_D)
_VmwVpxdHostName_Type=SnmpAdminString
_VmwVpxdHostName_Object=MibScalar
vmwVpxdHostName=_VmwVpxdHostName_Object((1,3,6,1,4,1,6876,4,3,302),_VmwVpxdHostName_Type())
vmwVpxdHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdHostName.setStatus(_D)
_VmwVpxdVMName_Type=SnmpAdminString
_VmwVpxdVMName_Object=MibScalar
vmwVpxdVMName=_VmwVpxdVMName_Object((1,3,6,1,4,1,6876,4,3,303),_VmwVpxdVMName_Type())
vmwVpxdVMName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdVMName.setStatus(_D)
_VmwVpxdOldStatus_Type=SnmpAdminString
_VmwVpxdOldStatus_Object=MibScalar
vmwVpxdOldStatus=_VmwVpxdOldStatus_Object((1,3,6,1,4,1,6876,4,3,304),_VmwVpxdOldStatus_Type())
vmwVpxdOldStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdOldStatus.setStatus(_B)
_VmwVpxdNewStatus_Type=SnmpAdminString
_VmwVpxdNewStatus_Object=MibScalar
vmwVpxdNewStatus=_VmwVpxdNewStatus_Object((1,3,6,1,4,1,6876,4,3,305),_VmwVpxdNewStatus_Type())
vmwVpxdNewStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdNewStatus.setStatus(_B)
_VmwVpxdObjValue_Type=VmwLongSnmpAdminString
_VmwVpxdObjValue_Object=MibScalar
vmwVpxdObjValue=_VmwVpxdObjValue_Object((1,3,6,1,4,1,6876,4,3,306),_VmwVpxdObjValue_Type())
vmwVpxdObjValue.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdObjValue.setStatus(_B)
_VmwVpxdTargetObj_Type=SnmpAdminString
_VmwVpxdTargetObj_Object=MibScalar
vmwVpxdTargetObj=_VmwVpxdTargetObj_Object((1,3,6,1,4,1,6876,4,3,307),_VmwVpxdTargetObj_Type())
vmwVpxdTargetObj.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdTargetObj.setStatus(_B)
class _VmwVpxdTargetObjType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('host',2),('vm',3),('other',4)))
_VmwVpxdTargetObjType_Type.__name__=_N
_VmwVpxdTargetObjType_Object=MibScalar
vmwVpxdTargetObjType=_VmwVpxdTargetObjType_Object((1,3,6,1,4,1,6876,4,3,308),_VmwVpxdTargetObjType_Type())
vmwVpxdTargetObjType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVpxdTargetObjType.setStatus(_B)
vmwVCAlarmInfoGroup=ObjectGroup((1,3,6,1,4,1,6876,4,3,1,2,2,1))
vmwVCAlarmInfoGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmwVCAlarmInfoGroup.setStatus(_D)
vmwVCAlarmGroup=ObjectGroup((1,3,6,1,4,1,6876,4,3,1,2,2,3))
vmwVCAlarmGroup.setObjects(*((_A,_K),(_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:vmwVCAlarmGroup.setStatus(_B)
vpxdAlarm=NotificationType((1,3,6,1,4,1,6876,4,3,0,201))
vpxdAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vpxdAlarm.setStatus(_D)
vpxdDiagnostic=NotificationType((1,3,6,1,4,1,6876,4,3,0,202))
if mibBuilder.loadTexts:vpxdDiagnostic.setStatus(_B)
vpxdAlarmInfo=NotificationType((1,3,6,1,4,1,6876,4,3,0,203))
vpxdAlarmInfo.setObjects(*((_A,_K),(_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:vpxdAlarmInfo.setStatus(_B)
vmwVCNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,4,3,1,2,2,2))
vmwVCNotificationGroup.setObjects(*((_A,_O),(_A,_M)))
if mibBuilder.loadTexts:vmwVCNotificationGroup.setStatus(_D)
vmwVCAlarmNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,4,3,1,2,2,4))
vmwVCAlarmNotificationGroup.setObjects(*((_A,_P),(_A,_M)))
if mibBuilder.loadTexts:vmwVCAlarmNotificationGroup.setStatus(_B)
vmwVCMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,4,3,1,2,1,2))
vmwVCMIBBasicCompliance.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vmwVCMIBBasicCompliance.setStatus(_D)
vmwVCMIBBasicComplianceRev2=ModuleCompliance((1,3,6,1,4,1,6876,4,3,1,2,1,3))
vmwVCMIBBasicComplianceRev2.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:vmwVCMIBBasicComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwVCNotifications':vmwVCNotifications,_O:vpxdAlarm,_M:vpxdDiagnostic,_P:vpxdAlarmInfo,'vmwVCMIB':vmwVCMIB,'vmwVCMIBConformance':vmwVCMIBConformance,'vmwVCMIBCompliances':vmwVCMIBCompliances,'vmwVCMIBBasicCompliance':vmwVCMIBBasicCompliance,'vmwVCMIBBasicComplianceRev2':vmwVCMIBBasicComplianceRev2,'vmwVCMIBGroups':vmwVCMIBGroups,_Q:vmwVCAlarmInfoGroup,_R:vmwVCNotificationGroup,_S:vmwVCAlarmGroup,_T:vmwVCAlarmNotificationGroup,_H:vmwVpxdTrapType,_I:vmwVpxdHostName,_J:vmwVpxdVMName,_E:vmwVpxdOldStatus,_F:vmwVpxdNewStatus,_G:vmwVpxdObjValue,_L:vmwVpxdTargetObj,_K:vmwVpxdTargetObjType})