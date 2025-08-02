_AS='vmwVCOPSNotificationGroup2'
_AR='vmwVCOPSNotificationInfoGroup2'
_AQ='vmwVCOPSNotificationGroup1'
_AP='vmwVCOPSNotificationInfoGroup1'
_AO='vmwareTrapProblemChange'
_AN='vmwareTrapProblemClear'
_AM='vmwareTrapProblemActive'
_AL='vmwareTrapResourceDisconnectedClear'
_AK='vmwareTrapResourceDisconnectedActive'
_AJ='vmwareTrapAliveComponentFailureClear'
_AI='vmwareTrapAliveComponentFailureActive'
_AH='vmwareTrapDensityChange'
_AG='vmwareTrapDensityClear'
_AF='vmwareTrapDensityActive'
_AE='vmwareTrapWasteChange'
_AD='vmwareTrapWasteClear'
_AC='vmwareTrapWasteActive'
_AB='vmwareTrapStressChange'
_AA='vmwareTrapStressClear'
_A9='vmwareTrapStressActive'
_A8='vmwareTrapCapacityRemainingChange'
_A7='vmwareTrapCapacityRemainingClear'
_A6='vmwareTrapCapacityRemainingActive'
_A5='vmwareTrapTimeRemainingChange'
_A4='vmwareTrapTimeRemainingClear'
_A3='vmwareTrapTimeRemainingActive'
_A2='vmwareTrapFaultChange'
_A1='vmwareTrapFaultClear'
_A0='vmwareTrapFaultActive'
_z='vmwareTrapAnomalyChange'
_y='vmwareTrapAnomalyClear'
_x='vmwareTrapAnomalyActive'
_w='vmwareTrapWorkloadChange'
_v='vmwareTrapWorkloadClear'
_u='vmwareTrapWorkloadActive'
_t='vmwareTrapAbnormalityChange'
_s='vmwareTrapAbnormalityClear'
_r='vmwareTrapAbnormalityActive'
_q='vmwareTrapNotificationChange'
_p='vmwareTrapNotificationClear'
_o='vmwareTrapNotificationActive'
_n='vmwareTrapKPIHTBreachChange'
_m='vmwareTrapKPIHTBreachClear'
_l='vmwareTrapKPIHTBreachActive'
_k='vmwareTrapAggregateAnomalyClear'
_j='vmwareTrapAggregateAnomalyActive'
_i='vmwareTrapKPIPredictionChange'
_h='vmwareTrapKPIPredictionClear'
_g='vmwareTrapKPIPredictionActive'
_f='vmwareTrapKPIBreachChange'
_e='vmwareTrapKPIBreachClear'
_d='vmwareTrapKPIBreachActive'
_c='vmwareTrapTest'
_b='vmwareTrapConsolidatedAlertChange'
_a='vmwareTrapConsolidatedAlertClear'
_Z='vmwareTrapConsolidatedAlertActive'
_Y='vmwareTrapComplianceChange'
_X='vmwareTrapComplianceClear'
_W='vmwareTrapComplianceActive'
_V='vmwareAlertImpact'
_U='vmwareAlertDefinitionDesc'
_T='vmwareAlertDefinitionName'
_S='vmwareAlertEfficiency'
_R='vmwareAlertRisk'
_Q='vmwareAlertHealth'
_P='accessible-for-notify'
_O='vmwareAlertResourceKind'
_N='vmwareAlertMetricName'
_M='vmwareAlertSubtype'
_L='vmwareAlertType'
_K='vmwareAlertMessage'
_J='vmwareAlertID'
_I='vmwareAlertURL'
_H='vmwareAlertRootCause'
_G='vmwareAlertCriticality'
_F='vmwareAlertTimestamp'
_E='vmwareAlertEntityType'
_D='vmwareAlertEntityName'
_C='vmwareAlertAliveServerName'
_B='obsolete'
_A='VMWARE-VCOPS-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwVCOps,=mibBuilder.importSymbols('VMWARE-PRODUCTS-MIB','vmwVCOps')
vmwVcopsMIB=ModuleIdentity((1,3,6,1,4,1,6876,4,5,1))
if mibBuilder.loadTexts:vmwVcopsMIB.setRevisions(('2016-10-13 00:00','2013-02-01 00:00','2011-10-19 00:00','2009-01-26 00:00'))
_VmwareAlertTrap_ObjectIdentity=ObjectIdentity
vmwareAlertTrap=_VmwareAlertTrap_ObjectIdentity((1,3,6,1,4,1,6876,4,5,1,0))
if mibBuilder.loadTexts:vmwareAlertTrap.setStatus(_B)
_VmwareGenericAlertData_ObjectIdentity=ObjectIdentity
vmwareGenericAlertData=_VmwareGenericAlertData_ObjectIdentity((1,3,6,1,4,1,6876,4,5,1,2))
if mibBuilder.loadTexts:vmwareGenericAlertData.setStatus(_B)
_VmwareAlertAliveServerName_Type=OctetString
_VmwareAlertAliveServerName_Object=MibScalar
vmwareAlertAliveServerName=_VmwareAlertAliveServerName_Object((1,3,6,1,4,1,6876,4,5,1,2,1),_VmwareAlertAliveServerName_Type())
vmwareAlertAliveServerName.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertAliveServerName.setStatus(_B)
_VmwareAlertEntityName_Type=OctetString
_VmwareAlertEntityName_Object=MibScalar
vmwareAlertEntityName=_VmwareAlertEntityName_Object((1,3,6,1,4,1,6876,4,5,1,2,2),_VmwareAlertEntityName_Type())
vmwareAlertEntityName.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertEntityName.setStatus(_B)
_VmwareAlertEntityType_Type=OctetString
_VmwareAlertEntityType_Object=MibScalar
vmwareAlertEntityType=_VmwareAlertEntityType_Object((1,3,6,1,4,1,6876,4,5,1,2,3),_VmwareAlertEntityType_Type())
vmwareAlertEntityType.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertEntityType.setStatus(_B)
_VmwareAlertTimestamp_Type=OctetString
_VmwareAlertTimestamp_Object=MibScalar
vmwareAlertTimestamp=_VmwareAlertTimestamp_Object((1,3,6,1,4,1,6876,4,5,1,2,4),_VmwareAlertTimestamp_Type())
vmwareAlertTimestamp.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertTimestamp.setStatus(_B)
_VmwareAlertCriticality_Type=OctetString
_VmwareAlertCriticality_Object=MibScalar
vmwareAlertCriticality=_VmwareAlertCriticality_Object((1,3,6,1,4,1,6876,4,5,1,2,5),_VmwareAlertCriticality_Type())
vmwareAlertCriticality.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertCriticality.setStatus(_B)
_VmwareAlertRootCause_Type=OctetString
_VmwareAlertRootCause_Object=MibScalar
vmwareAlertRootCause=_VmwareAlertRootCause_Object((1,3,6,1,4,1,6876,4,5,1,2,6),_VmwareAlertRootCause_Type())
vmwareAlertRootCause.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertRootCause.setStatus(_B)
_VmwareAlertURL_Type=OctetString
_VmwareAlertURL_Object=MibScalar
vmwareAlertURL=_VmwareAlertURL_Object((1,3,6,1,4,1,6876,4,5,1,2,7),_VmwareAlertURL_Type())
vmwareAlertURL.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertURL.setStatus(_B)
_VmwareAlertID_Type=OctetString
_VmwareAlertID_Object=MibScalar
vmwareAlertID=_VmwareAlertID_Object((1,3,6,1,4,1,6876,4,5,1,2,8),_VmwareAlertID_Type())
vmwareAlertID.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertID.setStatus(_B)
_VmwareAlertMessage_Type=OctetString
_VmwareAlertMessage_Object=MibScalar
vmwareAlertMessage=_VmwareAlertMessage_Object((1,3,6,1,4,1,6876,4,5,1,2,9),_VmwareAlertMessage_Type())
vmwareAlertMessage.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertMessage.setStatus(_B)
_VmwareAlertType_Type=OctetString
_VmwareAlertType_Object=MibScalar
vmwareAlertType=_VmwareAlertType_Object((1,3,6,1,4,1,6876,4,5,1,2,10),_VmwareAlertType_Type())
vmwareAlertType.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertType.setStatus(_B)
_VmwareAlertSubtype_Type=OctetString
_VmwareAlertSubtype_Object=MibScalar
vmwareAlertSubtype=_VmwareAlertSubtype_Object((1,3,6,1,4,1,6876,4,5,1,2,11),_VmwareAlertSubtype_Type())
vmwareAlertSubtype.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertSubtype.setStatus(_B)
_VmwareAlertHealth_Type=SnmpAdminString
_VmwareAlertHealth_Object=MibScalar
vmwareAlertHealth=_VmwareAlertHealth_Object((1,3,6,1,4,1,6876,4,5,1,2,12),_VmwareAlertHealth_Type())
vmwareAlertHealth.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertHealth.setStatus(_B)
_VmwareAlertRisk_Type=SnmpAdminString
_VmwareAlertRisk_Object=MibScalar
vmwareAlertRisk=_VmwareAlertRisk_Object((1,3,6,1,4,1,6876,4,5,1,2,13),_VmwareAlertRisk_Type())
vmwareAlertRisk.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertRisk.setStatus(_B)
_VmwareAlertEfficiency_Type=SnmpAdminString
_VmwareAlertEfficiency_Object=MibScalar
vmwareAlertEfficiency=_VmwareAlertEfficiency_Object((1,3,6,1,4,1,6876,4,5,1,2,14),_VmwareAlertEfficiency_Type())
vmwareAlertEfficiency.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertEfficiency.setStatus(_B)
_VmwareAlertMetricName_Type=SnmpAdminString
_VmwareAlertMetricName_Object=MibScalar
vmwareAlertMetricName=_VmwareAlertMetricName_Object((1,3,6,1,4,1,6876,4,5,1,2,15),_VmwareAlertMetricName_Type())
vmwareAlertMetricName.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertMetricName.setStatus(_B)
_VmwareAlertResourceKind_Type=SnmpAdminString
_VmwareAlertResourceKind_Object=MibScalar
vmwareAlertResourceKind=_VmwareAlertResourceKind_Object((1,3,6,1,4,1,6876,4,5,1,2,16),_VmwareAlertResourceKind_Type())
vmwareAlertResourceKind.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertResourceKind.setStatus(_B)
_VmwareAlertDefinitionName_Type=SnmpAdminString
_VmwareAlertDefinitionName_Object=MibScalar
vmwareAlertDefinitionName=_VmwareAlertDefinitionName_Object((1,3,6,1,4,1,6876,4,5,1,2,17),_VmwareAlertDefinitionName_Type())
vmwareAlertDefinitionName.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertDefinitionName.setStatus(_B)
_VmwareAlertDefinitionDesc_Type=SnmpAdminString
_VmwareAlertDefinitionDesc_Object=MibScalar
vmwareAlertDefinitionDesc=_VmwareAlertDefinitionDesc_Object((1,3,6,1,4,1,6876,4,5,1,2,18),_VmwareAlertDefinitionDesc_Type())
vmwareAlertDefinitionDesc.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertDefinitionDesc.setStatus(_B)
_VmwareAlertImpact_Type=SnmpAdminString
_VmwareAlertImpact_Object=MibScalar
vmwareAlertImpact=_VmwareAlertImpact_Object((1,3,6,1,4,1,6876,4,5,1,2,19),_VmwareAlertImpact_Type())
vmwareAlertImpact.setMaxAccess(_P)
if mibBuilder.loadTexts:vmwareAlertImpact.setStatus(_B)
_VmwVCOPSMIBConformance_ObjectIdentity=ObjectIdentity
vmwVCOPSMIBConformance=_VmwVCOPSMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,4,5,1,99))
_VmwVCOPSMIBCompliances_ObjectIdentity=ObjectIdentity
vmwVCOPSMIBCompliances=_VmwVCOPSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,4,5,1,99,1))
_VmwVCOPSMIBGroups_ObjectIdentity=ObjectIdentity
vmwVCOPSMIBGroups=_VmwVCOPSMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,4,5,1,99,2))
vmwVCOPSNotificationInfoGroup1=ObjectGroup((1,3,6,1,4,1,6876,4,5,1,99,2,2))
vmwVCOPSNotificationInfoGroup1.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwVCOPSNotificationInfoGroup1.setStatus(_B)
vmwVCOPSNotificationInfoGroup2=ObjectGroup((1,3,6,1,4,1,6876,4,5,1,99,2,4))
vmwVCOPSNotificationInfoGroup2.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:vmwVCOPSNotificationInfoGroup2.setStatus(_B)
vmwareTrapKPIBreachActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,1))
vmwareTrapKPIBreachActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIBreachActive.setStatus(_B)
vmwareTrapKPIBreachClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,2))
vmwareTrapKPIBreachClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIBreachClear.setStatus(_B)
vmwareTrapKPIBreachChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,3))
vmwareTrapKPIBreachChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIBreachChange.setStatus(_B)
vmwareTrapKPIPredictionActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,4))
vmwareTrapKPIPredictionActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIPredictionActive.setStatus(_B)
vmwareTrapKPIPredictionClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,5))
vmwareTrapKPIPredictionClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIPredictionClear.setStatus(_B)
vmwareTrapKPIPredictionChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,6))
vmwareTrapKPIPredictionChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIPredictionChange.setStatus(_B)
vmwareTrapAggregateAnomalyActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,7))
vmwareTrapAggregateAnomalyActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAggregateAnomalyActive.setStatus(_B)
vmwareTrapAggregateAnomalyClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,8))
vmwareTrapAggregateAnomalyClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAggregateAnomalyClear.setStatus(_B)
vmwareTrapKPIHTBreachActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,10))
vmwareTrapKPIHTBreachActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIHTBreachActive.setStatus(_B)
vmwareTrapKPIHTBreachClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,11))
vmwareTrapKPIHTBreachClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIHTBreachClear.setStatus(_B)
vmwareTrapKPIHTBreachChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,12))
vmwareTrapKPIHTBreachChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapKPIHTBreachChange.setStatus(_B)
vmwareTrapNotificationActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,13))
vmwareTrapNotificationActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapNotificationActive.setStatus(_B)
vmwareTrapNotificationClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,14))
vmwareTrapNotificationClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapNotificationClear.setStatus(_B)
vmwareTrapNotificationChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,15))
vmwareTrapNotificationChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapNotificationChange.setStatus(_B)
vmwareTrapAbnormalityActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,16))
vmwareTrapAbnormalityActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAbnormalityActive.setStatus(_B)
vmwareTrapAbnormalityClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,17))
vmwareTrapAbnormalityClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAbnormalityClear.setStatus(_B)
vmwareTrapAbnormalityChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,18))
vmwareTrapAbnormalityChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAbnormalityChange.setStatus(_B)
vmwareTrapWorkloadActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,19))
vmwareTrapWorkloadActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapWorkloadActive.setStatus(_B)
vmwareTrapWorkloadClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,20))
vmwareTrapWorkloadClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapWorkloadClear.setStatus(_B)
vmwareTrapWorkloadChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,21))
vmwareTrapWorkloadChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapWorkloadChange.setStatus(_B)
vmwareTrapAnomalyActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,22))
vmwareTrapAnomalyActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAnomalyActive.setStatus(_B)
vmwareTrapAnomalyClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,23))
vmwareTrapAnomalyClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAnomalyClear.setStatus(_B)
vmwareTrapAnomalyChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,24))
vmwareTrapAnomalyChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAnomalyChange.setStatus(_B)
vmwareTrapFaultActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,25))
vmwareTrapFaultActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapFaultActive.setStatus(_B)
vmwareTrapFaultClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,26))
vmwareTrapFaultClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapFaultClear.setStatus(_B)
vmwareTrapFaultChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,27))
vmwareTrapFaultChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapFaultChange.setStatus(_B)
vmwareTrapTimeRemainingActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,28))
vmwareTrapTimeRemainingActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapTimeRemainingActive.setStatus(_B)
vmwareTrapTimeRemainingClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,29))
vmwareTrapTimeRemainingClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapTimeRemainingClear.setStatus(_B)
vmwareTrapTimeRemainingChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,30))
vmwareTrapTimeRemainingChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapTimeRemainingChange.setStatus(_B)
vmwareTrapCapacityRemainingActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,31))
vmwareTrapCapacityRemainingActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapCapacityRemainingActive.setStatus(_B)
vmwareTrapCapacityRemainingClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,32))
vmwareTrapCapacityRemainingClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapCapacityRemainingClear.setStatus(_B)
vmwareTrapCapacityRemainingChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,33))
vmwareTrapCapacityRemainingChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapCapacityRemainingChange.setStatus(_B)
vmwareTrapStressActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,34))
vmwareTrapStressActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapStressActive.setStatus(_B)
vmwareTrapStressClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,35))
vmwareTrapStressClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapStressClear.setStatus(_B)
vmwareTrapStressChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,36))
vmwareTrapStressChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapStressChange.setStatus(_B)
vmwareTrapWasteActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,37))
vmwareTrapWasteActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapWasteActive.setStatus(_B)
vmwareTrapWasteClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,38))
vmwareTrapWasteClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapWasteClear.setStatus(_B)
vmwareTrapWasteChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,39))
vmwareTrapWasteChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapWasteChange.setStatus(_B)
vmwareTrapDensityActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,40))
vmwareTrapDensityActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapDensityActive.setStatus(_B)
vmwareTrapDensityClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,41))
vmwareTrapDensityClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapDensityClear.setStatus(_B)
vmwareTrapDensityChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,42))
vmwareTrapDensityChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapDensityChange.setStatus(_B)
vmwareTrapComplianceActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,43))
vmwareTrapComplianceActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapComplianceActive.setStatus(_B)
vmwareTrapComplianceClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,44))
vmwareTrapComplianceClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapComplianceClear.setStatus(_B)
vmwareTrapComplianceChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,45))
vmwareTrapComplianceChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapComplianceChange.setStatus(_B)
vmwareTrapProblemActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,46))
vmwareTrapProblemActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_N),(_A,_O),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:vmwareTrapProblemActive.setStatus(_B)
vmwareTrapProblemClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,47))
vmwareTrapProblemClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_N),(_A,_O),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:vmwareTrapProblemClear.setStatus(_B)
vmwareTrapProblemChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,48))
vmwareTrapProblemChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_N),(_A,_O),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:vmwareTrapProblemChange.setStatus(_B)
vmwareTrapConsolidatedAlertActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,60))
vmwareTrapConsolidatedAlertActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapConsolidatedAlertActive.setStatus(_B)
vmwareTrapConsolidatedAlertClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,61))
vmwareTrapConsolidatedAlertClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapConsolidatedAlertClear.setStatus(_B)
vmwareTrapConsolidatedAlertChange=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,62))
vmwareTrapConsolidatedAlertChange.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapConsolidatedAlertChange.setStatus(_B)
vmwareTrapAliveComponentFailureActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,101))
vmwareTrapAliveComponentFailureActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAliveComponentFailureActive.setStatus(_B)
vmwareTrapAliveComponentFailureClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,102))
vmwareTrapAliveComponentFailureClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapAliveComponentFailureClear.setStatus(_B)
vmwareTrapResourceDisconnectedActive=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,103))
vmwareTrapResourceDisconnectedActive.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapResourceDisconnectedActive.setStatus(_B)
vmwareTrapResourceDisconnectedClear=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,104))
vmwareTrapResourceDisconnectedClear.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapResourceDisconnectedClear.setStatus(_B)
vmwareTrapTest=NotificationType((1,3,6,1,4,1,6876,4,5,1,0,200))
vmwareTrapTest.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwareTrapTest.setStatus(_B)
vmwVCOPSNotificationGroup1=NotificationGroup((1,3,6,1,4,1,6876,4,5,1,99,2,3))
vmwVCOPSNotificationGroup1.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:vmwVCOPSNotificationGroup1.setStatus(_B)
vmwVCOPSNotificationGroup2=NotificationGroup((1,3,6,1,4,1,6876,4,5,1,99,2,5))
vmwVCOPSNotificationGroup2.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:vmwVCOPSNotificationGroup2.setStatus(_B)
vmwVCOPSMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,4,5,1,99,1,3))
vmwVCOPSMIBBasicCompliance.setObjects(*((_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:vmwVCOPSMIBBasicCompliance.setStatus(_B)
vmwVCOPSMIBBasicCompliance2016=ModuleCompliance((1,3,6,1,4,1,6876,4,5,1,99,1,4))
vmwVCOPSMIBBasicCompliance2016.setObjects(*((_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:vmwVCOPSMIBBasicCompliance2016.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwVcopsMIB':vmwVcopsMIB,'vmwareAlertTrap':vmwareAlertTrap,_d:vmwareTrapKPIBreachActive,_e:vmwareTrapKPIBreachClear,_f:vmwareTrapKPIBreachChange,_g:vmwareTrapKPIPredictionActive,_h:vmwareTrapKPIPredictionClear,_i:vmwareTrapKPIPredictionChange,_j:vmwareTrapAggregateAnomalyActive,_k:vmwareTrapAggregateAnomalyClear,_l:vmwareTrapKPIHTBreachActive,_m:vmwareTrapKPIHTBreachClear,_n:vmwareTrapKPIHTBreachChange,_o:vmwareTrapNotificationActive,_p:vmwareTrapNotificationClear,_q:vmwareTrapNotificationChange,_r:vmwareTrapAbnormalityActive,_s:vmwareTrapAbnormalityClear,_t:vmwareTrapAbnormalityChange,_u:vmwareTrapWorkloadActive,_v:vmwareTrapWorkloadClear,_w:vmwareTrapWorkloadChange,_x:vmwareTrapAnomalyActive,_y:vmwareTrapAnomalyClear,_z:vmwareTrapAnomalyChange,_A0:vmwareTrapFaultActive,_A1:vmwareTrapFaultClear,_A2:vmwareTrapFaultChange,_A3:vmwareTrapTimeRemainingActive,_A4:vmwareTrapTimeRemainingClear,_A5:vmwareTrapTimeRemainingChange,_A6:vmwareTrapCapacityRemainingActive,_A7:vmwareTrapCapacityRemainingClear,_A8:vmwareTrapCapacityRemainingChange,_A9:vmwareTrapStressActive,_AA:vmwareTrapStressClear,_AB:vmwareTrapStressChange,_AC:vmwareTrapWasteActive,_AD:vmwareTrapWasteClear,_AE:vmwareTrapWasteChange,_AF:vmwareTrapDensityActive,_AG:vmwareTrapDensityClear,_AH:vmwareTrapDensityChange,_W:vmwareTrapComplianceActive,_X:vmwareTrapComplianceClear,_Y:vmwareTrapComplianceChange,_AM:vmwareTrapProblemActive,_AN:vmwareTrapProblemClear,_AO:vmwareTrapProblemChange,_Z:vmwareTrapConsolidatedAlertActive,_a:vmwareTrapConsolidatedAlertClear,_b:vmwareTrapConsolidatedAlertChange,_AI:vmwareTrapAliveComponentFailureActive,_AJ:vmwareTrapAliveComponentFailureClear,_AK:vmwareTrapResourceDisconnectedActive,_AL:vmwareTrapResourceDisconnectedClear,_c:vmwareTrapTest,'vmwareGenericAlertData':vmwareGenericAlertData,_C:vmwareAlertAliveServerName,_D:vmwareAlertEntityName,_E:vmwareAlertEntityType,_F:vmwareAlertTimestamp,_G:vmwareAlertCriticality,_H:vmwareAlertRootCause,_I:vmwareAlertURL,_J:vmwareAlertID,_K:vmwareAlertMessage,_L:vmwareAlertType,_M:vmwareAlertSubtype,_Q:vmwareAlertHealth,_R:vmwareAlertRisk,_S:vmwareAlertEfficiency,_N:vmwareAlertMetricName,_O:vmwareAlertResourceKind,_T:vmwareAlertDefinitionName,_U:vmwareAlertDefinitionDesc,_V:vmwareAlertImpact,'vmwVCOPSMIBConformance':vmwVCOPSMIBConformance,'vmwVCOPSMIBCompliances':vmwVCOPSMIBCompliances,'vmwVCOPSMIBBasicCompliance':vmwVCOPSMIBBasicCompliance,'vmwVCOPSMIBBasicCompliance2016':vmwVCOPSMIBBasicCompliance2016,'vmwVCOPSMIBGroups':vmwVCOPSMIBGroups,_AP:vmwVCOPSNotificationInfoGroup1,_AQ:vmwVCOPSNotificationGroup1,_AR:vmwVCOPSNotificationInfoGroup2,_AS:vmwVCOPSNotificationGroup2})