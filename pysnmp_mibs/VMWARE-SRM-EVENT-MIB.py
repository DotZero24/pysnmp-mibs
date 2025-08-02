_f='vmwSRMNotificationGroup'
_e='vmwSRMNotificationInfoGroup'
_d='vmwSrmRecoveryPlanExecuteCleanupEnd'
_c='vmwareVmwSrmRecoveryPlanExecuteCleanupBegin'
_b='vmwareSrmRecoveryPlanExecuteReprotectEnd'
_a='vmwareSrmRecoveryPlanExecuteReprotectBegin'
_Z='vmwareSrmRecoveryPlanVmCommandEnd'
_Y='vmwareSrmRecoveryPlanVmCommandBegin'
_X='vmwareSrmRecoveryPlanServerCommandEnd'
_W='vmwareVmwSrmRecoveryPlanServerCommandBegin'
_V='vmwareSrmRecoveryPlanPromptResponse'
_U='vmwareSrmRecoveryPlanPromptDisplay'
_T='vmwareSrmRecoveryVmEndEvent'
_S='vmwareVmwSrmRecoveryVmBeginEvent'
_R='vmwareVmwSrmRecoveryPlanExecuteEndEvent'
_Q='vmwareSrmRecoveryPlanExecuteBeginEvent'
_P='vmwareSrmRecoveryPlanExecuteTestEndEvent'
_O='vmwareSrmRecoveryPlanExecuteTestBeginTrap'
_N='cancelled'
_M='vmwSrmPromptString'
_L='Integer32'
_K='vmwSrmCommandName'
_J='vmwSrmVmUuid'
_I='vmwSrmVmName'
_H='vmwSrmResult'
_G='accessible-for-notify'
_F='vmwSrmSiteString'
_E='vmwSrmRecoveryState'
_D='vmwSrmRecoveryType'
_C='vmwSrmRecoveryName'
_B='current'
_A='VMWARE-SRM-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwSRM,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwSRM')
vmwSRMMIB=ModuleIdentity((1,3,6,1,4,1,6876,51,10))
if mibBuilder.loadTexts:vmwSRMMIB.setRevisions(('2012-02-07 00:00',))
_VmwSRMevents_ObjectIdentity=ObjectIdentity
vmwSRMevents=_VmwSRMevents_ObjectIdentity((1,3,6,1,4,1,6876,51,0))
_VmwSrmNotification_ObjectIdentity=ObjectIdentity
vmwSrmNotification=_VmwSrmNotification_ObjectIdentity((1,3,6,1,4,1,6876,51,1))
_VmwSrmVmName_Type=DisplayString
_VmwSrmVmName_Object=MibScalar
vmwSrmVmName=_VmwSrmVmName_Object((1,3,6,1,4,1,6876,51,1,1),_VmwSrmVmName_Type())
vmwSrmVmName.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmVmName.setStatus(_B)
_VmwSrmRecoveryName_Type=DisplayString
_VmwSrmRecoveryName_Object=MibScalar
vmwSrmRecoveryName=_VmwSrmRecoveryName_Object((1,3,6,1,4,1,6876,51,1,2),_VmwSrmRecoveryName_Type())
vmwSrmRecoveryName.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmRecoveryName.setStatus(_B)
_VmwSrmPromptString_Type=DisplayString
_VmwSrmPromptString_Object=MibScalar
vmwSrmPromptString=_VmwSrmPromptString_Object((1,3,6,1,4,1,6876,51,1,3),_VmwSrmPromptString_Type())
vmwSrmPromptString.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmPromptString.setStatus(_B)
class _VmwSrmRecoveryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('test',1),('recovery',2),('reprotect',3),('cleanup',4)))
_VmwSrmRecoveryType_Type.__name__=_L
_VmwSrmRecoveryType_Object=MibScalar
vmwSrmRecoveryType=_VmwSrmRecoveryType_Object((1,3,6,1,4,1,6876,51,1,4),_VmwSrmRecoveryType_Type())
vmwSrmRecoveryType.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmRecoveryType.setStatus(_B)
class _VmwSrmRecoveryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('uninitialized',1),('running',2),('paused',3),(_N,4),('completed',5)))
_VmwSrmRecoveryState_Type.__name__=_L
_VmwSrmRecoveryState_Object=MibScalar
vmwSrmRecoveryState=_VmwSrmRecoveryState_Object((1,3,6,1,4,1,6876,51,1,5),_VmwSrmRecoveryState_Type())
vmwSrmRecoveryState.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmRecoveryState.setStatus(_B)
_VmwSrmSiteString_Type=DisplayString
_VmwSrmSiteString_Object=MibScalar
vmwSrmSiteString=_VmwSrmSiteString_Object((1,3,6,1,4,1,6876,51,1,6),_VmwSrmSiteString_Type())
vmwSrmSiteString.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmSiteString.setStatus(_B)
_VmwSrmVmUuid_Type=DisplayString
_VmwSrmVmUuid_Object=MibScalar
vmwSrmVmUuid=_VmwSrmVmUuid_Object((1,3,6,1,4,1,6876,51,1,7),_VmwSrmVmUuid_Type())
vmwSrmVmUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmVmUuid.setStatus(_B)
class _VmwSrmResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('success',1),('failure',2),('warning',3),(_N,4)))
_VmwSrmResult_Type.__name__=_L
_VmwSrmResult_Object=MibScalar
vmwSrmResult=_VmwSrmResult_Object((1,3,6,1,4,1,6876,51,1,8),_VmwSrmResult_Type())
vmwSrmResult.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmResult.setStatus(_B)
_VmwSrmCommandName_Type=DisplayString
_VmwSrmCommandName_Object=MibScalar
vmwSrmCommandName=_VmwSrmCommandName_Object((1,3,6,1,4,1,6876,51,1,9),_VmwSrmCommandName_Type())
vmwSrmCommandName.setMaxAccess(_G)
if mibBuilder.loadTexts:vmwSrmCommandName.setStatus(_B)
_VmwSRMMIBConformance_ObjectIdentity=ObjectIdentity
vmwSRMMIBConformance=_VmwSRMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,51,10,2))
_VmwSRMMIBCompliances_ObjectIdentity=ObjectIdentity
vmwSRMMIBCompliances=_VmwSRMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,51,10,2,1))
_VmwSRMMIBGroups_ObjectIdentity=ObjectIdentity
vmwSRMMIBGroups=_VmwSRMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,51,10,2,2))
vmwSRMNotificationInfoGroup=ObjectGroup((1,3,6,1,4,1,6876,51,10,2,2,1))
vmwSRMNotificationInfoGroup.setObjects(*((_A,_I),(_A,_C),(_A,_M),(_A,_D),(_A,_E),(_A,_F),(_A,_J),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:vmwSRMNotificationInfoGroup.setStatus(_B)
vmwareSrmRecoveryPlanExecuteTestBeginTrap=NotificationType((1,3,6,1,4,1,6876,51,0,1))
vmwareSrmRecoveryPlanExecuteTestBeginTrap.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanExecuteTestBeginTrap.setStatus(_B)
vmwareSrmRecoveryPlanExecuteTestEndEvent=NotificationType((1,3,6,1,4,1,6876,51,0,2))
vmwareSrmRecoveryPlanExecuteTestEndEvent.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanExecuteTestEndEvent.setStatus(_B)
vmwareSrmRecoveryPlanExecuteBeginEvent=NotificationType((1,3,6,1,4,1,6876,51,0,3))
vmwareSrmRecoveryPlanExecuteBeginEvent.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanExecuteBeginEvent.setStatus(_B)
vmwareVmwSrmRecoveryPlanExecuteEndEvent=NotificationType((1,3,6,1,4,1,6876,51,0,4))
vmwareVmwSrmRecoveryPlanExecuteEndEvent.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:vmwareVmwSrmRecoveryPlanExecuteEndEvent.setStatus(_B)
vmwareVmwSrmRecoveryVmBeginEvent=NotificationType((1,3,6,1,4,1,6876,51,0,5))
vmwareVmwSrmRecoveryVmBeginEvent.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:vmwareVmwSrmRecoveryVmBeginEvent.setStatus(_B)
vmwareSrmRecoveryVmEndEvent=NotificationType((1,3,6,1,4,1,6876,51,0,6))
vmwareSrmRecoveryVmEndEvent.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_I),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:vmwareSrmRecoveryVmEndEvent.setStatus(_B)
vmwareSrmRecoveryPlanPromptDisplay=NotificationType((1,3,6,1,4,1,6876,51,0,7))
vmwareSrmRecoveryPlanPromptDisplay.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_M)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanPromptDisplay.setStatus(_B)
vmwareSrmRecoveryPlanPromptResponse=NotificationType((1,3,6,1,4,1,6876,51,0,8))
vmwareSrmRecoveryPlanPromptResponse.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanPromptResponse.setStatus(_B)
vmwareVmwSrmRecoveryPlanServerCommandBegin=NotificationType((1,3,6,1,4,1,6876,51,0,9))
vmwareVmwSrmRecoveryPlanServerCommandBegin.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:vmwareVmwSrmRecoveryPlanServerCommandBegin.setStatus(_B)
vmwareSrmRecoveryPlanServerCommandEnd=NotificationType((1,3,6,1,4,1,6876,51,0,10))
vmwareSrmRecoveryPlanServerCommandEnd.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanServerCommandEnd.setStatus(_B)
vmwareSrmRecoveryPlanVmCommandBegin=NotificationType((1,3,6,1,4,1,6876,51,0,11))
vmwareSrmRecoveryPlanVmCommandBegin.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_K),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanVmCommandBegin.setStatus(_B)
vmwareSrmRecoveryPlanVmCommandEnd=NotificationType((1,3,6,1,4,1,6876,51,0,12))
vmwareSrmRecoveryPlanVmCommandEnd.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_K),(_A,_I),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanVmCommandEnd.setStatus(_B)
vmwareSrmRecoveryPlanExecuteReprotectBegin=NotificationType((1,3,6,1,4,1,6876,51,0,13))
vmwareSrmRecoveryPlanExecuteReprotectBegin.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanExecuteReprotectBegin.setStatus(_B)
vmwareSrmRecoveryPlanExecuteReprotectEnd=NotificationType((1,3,6,1,4,1,6876,51,0,14))
vmwareSrmRecoveryPlanExecuteReprotectEnd.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:vmwareSrmRecoveryPlanExecuteReprotectEnd.setStatus(_B)
vmwareVmwSrmRecoveryPlanExecuteCleanupBegin=NotificationType((1,3,6,1,4,1,6876,51,0,15))
vmwareVmwSrmRecoveryPlanExecuteCleanupBegin.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:vmwareVmwSrmRecoveryPlanExecuteCleanupBegin.setStatus(_B)
vmwSrmRecoveryPlanExecuteCleanupEnd=NotificationType((1,3,6,1,4,1,6876,51,0,16))
vmwSrmRecoveryPlanExecuteCleanupEnd.setObjects(*((_A,_F),(_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:vmwSrmRecoveryPlanExecuteCleanupEnd.setStatus(_B)
vmwSRMNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,51,10,2,2,2))
vmwSRMNotificationGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:vmwSRMNotificationGroup.setStatus(_B)
vmwSRMMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,51,10,2,1,2))
vmwSRMMIBBasicCompliance.setObjects(*((_A,_e),(_A,_f)))
if mibBuilder.loadTexts:vmwSRMMIBBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwSRMevents':vmwSRMevents,_O:vmwareSrmRecoveryPlanExecuteTestBeginTrap,_P:vmwareSrmRecoveryPlanExecuteTestEndEvent,_Q:vmwareSrmRecoveryPlanExecuteBeginEvent,_R:vmwareVmwSrmRecoveryPlanExecuteEndEvent,_S:vmwareVmwSrmRecoveryVmBeginEvent,_T:vmwareSrmRecoveryVmEndEvent,_U:vmwareSrmRecoveryPlanPromptDisplay,_V:vmwareSrmRecoveryPlanPromptResponse,_W:vmwareVmwSrmRecoveryPlanServerCommandBegin,_X:vmwareSrmRecoveryPlanServerCommandEnd,_Y:vmwareSrmRecoveryPlanVmCommandBegin,_Z:vmwareSrmRecoveryPlanVmCommandEnd,_a:vmwareSrmRecoveryPlanExecuteReprotectBegin,_b:vmwareSrmRecoveryPlanExecuteReprotectEnd,_c:vmwareVmwSrmRecoveryPlanExecuteCleanupBegin,_d:vmwSrmRecoveryPlanExecuteCleanupEnd,'vmwSrmNotification':vmwSrmNotification,_I:vmwSrmVmName,_C:vmwSrmRecoveryName,_M:vmwSrmPromptString,_D:vmwSrmRecoveryType,_E:vmwSrmRecoveryState,_F:vmwSrmSiteString,_J:vmwSrmVmUuid,_H:vmwSrmResult,_K:vmwSrmCommandName,'vmwSRMMIB':vmwSRMMIB,'vmwSRMMIBConformance':vmwSRMMIBConformance,'vmwSRMMIBCompliances':vmwSRMMIBCompliances,'vmwSRMMIBBasicCompliance':vmwSRMMIBBasicCompliance,'vmwSRMMIBGroups':vmwSRMMIBGroups,_e:vmwSRMNotificationInfoGroup,_f:vmwSRMNotificationGroup})