_c='vmwVROPSNotificationGroup'
_b='vmwVROPSNotificationInfoGroup'
_a='vmwTrapProblemChange'
_Z='vmwTrapProblemClear'
_Y='vmwTrapProblemActive'
_X='vmwTrapTest'
_W='vmwAlertNotificationRules'
_V='vmwAlertImpact'
_U='vmwAlertDefinitionDesc'
_T='vmwAlertDefinitionName'
_S='vmwAlertEfficiency'
_R='vmwAlertRisk'
_Q='vmwAlertHealth'
_P='vmwAlertResourceKind'
_O='vmwAlertMetricName'
_N='vmwAlertSubtype'
_M='vmwAlertType'
_L='vmwAlertMessage'
_K='vmwAlertID'
_J='vmwAlertURL'
_I='vmwAlertRootCause'
_H='vmwAlertCriticality'
_G='vmwAlertTimestamp'
_F='vmwAlertEntityType'
_E='vmwAlertEntityName'
_D='vmwAlertAliveServerName'
_C='accessible-for-notify'
_B='current'
_A='VMWARE-VROPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwVrops,=mibBuilder.importSymbols('VMWARE-PRODUCTS-MIB','vmwVrops')
VmwLongDisplayString,=mibBuilder.importSymbols('VMWARE-TC-MIB','VmwLongDisplayString')
vmwVropsMIB=ModuleIdentity((1,3,6,1,4,1,6876,4,50,1))
if mibBuilder.loadTexts:vmwVropsMIB.setRevisions(('2018-06-27 00:00',))
_VmwAlertTrap_ObjectIdentity=ObjectIdentity
vmwAlertTrap=_VmwAlertTrap_ObjectIdentity((1,3,6,1,4,1,6876,4,50,1,0))
if mibBuilder.loadTexts:vmwAlertTrap.setStatus(_B)
_VmwGenericAlertData_ObjectIdentity=ObjectIdentity
vmwGenericAlertData=_VmwGenericAlertData_ObjectIdentity((1,3,6,1,4,1,6876,4,50,1,2))
if mibBuilder.loadTexts:vmwGenericAlertData.setStatus(_B)
_VmwAlertAliveServerName_Type=VmwLongDisplayString
_VmwAlertAliveServerName_Object=MibScalar
vmwAlertAliveServerName=_VmwAlertAliveServerName_Object((1,3,6,1,4,1,6876,4,50,1,2,1),_VmwAlertAliveServerName_Type())
vmwAlertAliveServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertAliveServerName.setStatus(_B)
_VmwAlertEntityName_Type=VmwLongDisplayString
_VmwAlertEntityName_Object=MibScalar
vmwAlertEntityName=_VmwAlertEntityName_Object((1,3,6,1,4,1,6876,4,50,1,2,2),_VmwAlertEntityName_Type())
vmwAlertEntityName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertEntityName.setStatus(_B)
_VmwAlertEntityType_Type=VmwLongDisplayString
_VmwAlertEntityType_Object=MibScalar
vmwAlertEntityType=_VmwAlertEntityType_Object((1,3,6,1,4,1,6876,4,50,1,2,3),_VmwAlertEntityType_Type())
vmwAlertEntityType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertEntityType.setStatus(_B)
_VmwAlertTimestamp_Type=VmwLongDisplayString
_VmwAlertTimestamp_Object=MibScalar
vmwAlertTimestamp=_VmwAlertTimestamp_Object((1,3,6,1,4,1,6876,4,50,1,2,4),_VmwAlertTimestamp_Type())
vmwAlertTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertTimestamp.setStatus(_B)
_VmwAlertCriticality_Type=VmwLongDisplayString
_VmwAlertCriticality_Object=MibScalar
vmwAlertCriticality=_VmwAlertCriticality_Object((1,3,6,1,4,1,6876,4,50,1,2,5),_VmwAlertCriticality_Type())
vmwAlertCriticality.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertCriticality.setStatus(_B)
_VmwAlertRootCause_Type=VmwLongDisplayString
_VmwAlertRootCause_Object=MibScalar
vmwAlertRootCause=_VmwAlertRootCause_Object((1,3,6,1,4,1,6876,4,50,1,2,6),_VmwAlertRootCause_Type())
vmwAlertRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertRootCause.setStatus(_B)
_VmwAlertURL_Type=VmwLongDisplayString
_VmwAlertURL_Object=MibScalar
vmwAlertURL=_VmwAlertURL_Object((1,3,6,1,4,1,6876,4,50,1,2,7),_VmwAlertURL_Type())
vmwAlertURL.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertURL.setStatus(_B)
_VmwAlertID_Type=VmwLongDisplayString
_VmwAlertID_Object=MibScalar
vmwAlertID=_VmwAlertID_Object((1,3,6,1,4,1,6876,4,50,1,2,8),_VmwAlertID_Type())
vmwAlertID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertID.setStatus(_B)
_VmwAlertMessage_Type=VmwLongDisplayString
_VmwAlertMessage_Object=MibScalar
vmwAlertMessage=_VmwAlertMessage_Object((1,3,6,1,4,1,6876,4,50,1,2,9),_VmwAlertMessage_Type())
vmwAlertMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertMessage.setStatus(_B)
_VmwAlertType_Type=VmwLongDisplayString
_VmwAlertType_Object=MibScalar
vmwAlertType=_VmwAlertType_Object((1,3,6,1,4,1,6876,4,50,1,2,10),_VmwAlertType_Type())
vmwAlertType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertType.setStatus(_B)
_VmwAlertSubtype_Type=VmwLongDisplayString
_VmwAlertSubtype_Object=MibScalar
vmwAlertSubtype=_VmwAlertSubtype_Object((1,3,6,1,4,1,6876,4,50,1,2,11),_VmwAlertSubtype_Type())
vmwAlertSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertSubtype.setStatus(_B)
_VmwAlertHealth_Type=SnmpAdminString
_VmwAlertHealth_Object=MibScalar
vmwAlertHealth=_VmwAlertHealth_Object((1,3,6,1,4,1,6876,4,50,1,2,12),_VmwAlertHealth_Type())
vmwAlertHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertHealth.setStatus(_B)
_VmwAlertRisk_Type=SnmpAdminString
_VmwAlertRisk_Object=MibScalar
vmwAlertRisk=_VmwAlertRisk_Object((1,3,6,1,4,1,6876,4,50,1,2,13),_VmwAlertRisk_Type())
vmwAlertRisk.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertRisk.setStatus(_B)
_VmwAlertEfficiency_Type=SnmpAdminString
_VmwAlertEfficiency_Object=MibScalar
vmwAlertEfficiency=_VmwAlertEfficiency_Object((1,3,6,1,4,1,6876,4,50,1,2,14),_VmwAlertEfficiency_Type())
vmwAlertEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertEfficiency.setStatus(_B)
_VmwAlertMetricName_Type=SnmpAdminString
_VmwAlertMetricName_Object=MibScalar
vmwAlertMetricName=_VmwAlertMetricName_Object((1,3,6,1,4,1,6876,4,50,1,2,15),_VmwAlertMetricName_Type())
vmwAlertMetricName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertMetricName.setStatus(_B)
_VmwAlertResourceKind_Type=SnmpAdminString
_VmwAlertResourceKind_Object=MibScalar
vmwAlertResourceKind=_VmwAlertResourceKind_Object((1,3,6,1,4,1,6876,4,50,1,2,16),_VmwAlertResourceKind_Type())
vmwAlertResourceKind.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertResourceKind.setStatus(_B)
_VmwAlertDefinitionName_Type=SnmpAdminString
_VmwAlertDefinitionName_Object=MibScalar
vmwAlertDefinitionName=_VmwAlertDefinitionName_Object((1,3,6,1,4,1,6876,4,50,1,2,17),_VmwAlertDefinitionName_Type())
vmwAlertDefinitionName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertDefinitionName.setStatus(_B)
_VmwAlertDefinitionDesc_Type=SnmpAdminString
_VmwAlertDefinitionDesc_Object=MibScalar
vmwAlertDefinitionDesc=_VmwAlertDefinitionDesc_Object((1,3,6,1,4,1,6876,4,50,1,2,18),_VmwAlertDefinitionDesc_Type())
vmwAlertDefinitionDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertDefinitionDesc.setStatus(_B)
_VmwAlertImpact_Type=SnmpAdminString
_VmwAlertImpact_Object=MibScalar
vmwAlertImpact=_VmwAlertImpact_Object((1,3,6,1,4,1,6876,4,50,1,2,19),_VmwAlertImpact_Type())
vmwAlertImpact.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertImpact.setStatus(_B)
_VmwAlertNotificationRules_Type=VmwLongDisplayString
_VmwAlertNotificationRules_Object=MibScalar
vmwAlertNotificationRules=_VmwAlertNotificationRules_Object((1,3,6,1,4,1,6876,4,50,1,2,20),_VmwAlertNotificationRules_Type())
vmwAlertNotificationRules.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwAlertNotificationRules.setStatus(_B)
_VmwVROPSMIBConformance_ObjectIdentity=ObjectIdentity
vmwVROPSMIBConformance=_VmwVROPSMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,4,50,1,99))
_VmwVROPSMIBCompliances_ObjectIdentity=ObjectIdentity
vmwVROPSMIBCompliances=_VmwVROPSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,4,50,1,99,1))
_VmwVROPSMIBGroups_ObjectIdentity=ObjectIdentity
vmwVROPSMIBGroups=_VmwVROPSMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,4,50,1,99,2))
vmwVROPSNotificationInfoGroup=ObjectGroup((1,3,6,1,4,1,6876,4,50,1,99,2,1))
vmwVROPSNotificationInfoGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:vmwVROPSNotificationInfoGroup.setStatus(_B)
vmwTrapProblemActive=NotificationType((1,3,6,1,4,1,6876,4,50,1,0,46))
vmwTrapProblemActive.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_O),(_A,_P),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:vmwTrapProblemActive.setStatus(_B)
vmwTrapProblemClear=NotificationType((1,3,6,1,4,1,6876,4,50,1,0,47))
vmwTrapProblemClear.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_O),(_A,_P),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:vmwTrapProblemClear.setStatus(_B)
vmwTrapProblemChange=NotificationType((1,3,6,1,4,1,6876,4,50,1,0,48))
vmwTrapProblemChange.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:vmwTrapProblemChange.setStatus(_B)
vmwTrapTest=NotificationType((1,3,6,1,4,1,6876,4,50,1,0,200))
vmwTrapTest.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:vmwTrapTest.setStatus(_B)
vmwVROPSNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,4,50,1,99,2,2))
vmwVROPSNotificationGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:vmwVROPSNotificationGroup.setStatus(_B)
vmwVROPSMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,4,50,1,99,1,1))
vmwVROPSMIBBasicCompliance.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:vmwVROPSMIBBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwVropsMIB':vmwVropsMIB,'vmwAlertTrap':vmwAlertTrap,_Y:vmwTrapProblemActive,_Z:vmwTrapProblemClear,_a:vmwTrapProblemChange,_X:vmwTrapTest,'vmwGenericAlertData':vmwGenericAlertData,_D:vmwAlertAliveServerName,_E:vmwAlertEntityName,_F:vmwAlertEntityType,_G:vmwAlertTimestamp,_H:vmwAlertCriticality,_I:vmwAlertRootCause,_J:vmwAlertURL,_K:vmwAlertID,_L:vmwAlertMessage,_M:vmwAlertType,_N:vmwAlertSubtype,_Q:vmwAlertHealth,_R:vmwAlertRisk,_S:vmwAlertEfficiency,_O:vmwAlertMetricName,_P:vmwAlertResourceKind,_T:vmwAlertDefinitionName,_U:vmwAlertDefinitionDesc,_V:vmwAlertImpact,_W:vmwAlertNotificationRules,'vmwVROPSMIBConformance':vmwVROPSMIBConformance,'vmwVROPSMIBCompliances':vmwVROPSMIBCompliances,'vmwVROPSMIBBasicCompliance':vmwVROPSMIBBasicCompliance,'vmwVROPSMIBGroups':vmwVROPSMIBGroups,_b:vmwVROPSNotificationInfoGroup,_c:vmwVROPSNotificationGroup})