_I='egrUsedTCAMEntries'
_H='egrUsedTCAMPercent'
_G='ingUsedTCAMEntries'
_F='ingUsedTCAMPercent'
_E='egrTCAMGroupName'
_D='ingTCAMGroupName'
_C='IPI-TCAM-UTILIZATION-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
ipiTCAMutilization=ModuleIdentity((1,3,6,1,4,1,36673,108))
class CodeType(TextualConvention,Unsigned32):status=_A;displayHint='x'
class UnitType(TextualConvention,Unsigned32):status=_A;displayHint='x'
_TCAMUtilizationObjects_ObjectIdentity=ObjectIdentity
TCAMUtilizationObjects=_TCAMUtilizationObjects_ObjectIdentity((1,3,6,1,4,1,36673,108,1))
_IngressTCAMUtilizationTable_Object=MibTable
ingressTCAMUtilizationTable=_IngressTCAMUtilizationTable_Object((1,3,6,1,4,1,36673,108,1,1))
if mibBuilder.loadTexts:ingressTCAMUtilizationTable.setStatus(_A)
_IngressTCAMUtilizationEntry_Object=MibTableRow
ingressTCAMUtilizationEntry=_IngressTCAMUtilizationEntry_Object((1,3,6,1,4,1,36673,108,1,1,1))
ingressTCAMUtilizationEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ingressTCAMUtilizationEntry.setStatus(_A)
_IngTCAMGroupName_Type=DisplayString
_IngTCAMGroupName_Object=MibTableColumn
ingTCAMGroupName=_IngTCAMGroupName_Object((1,3,6,1,4,1,36673,108,1,1,1,1),_IngTCAMGroupName_Type())
ingTCAMGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:ingTCAMGroupName.setStatus(_A)
_IngFreeTCAMEntries_Type=Integer
_IngFreeTCAMEntries_Object=MibTableColumn
ingFreeTCAMEntries=_IngFreeTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,1,1,2),_IngFreeTCAMEntries_Type())
ingFreeTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ingFreeTCAMEntries.setStatus(_A)
_IngUsedTCAMPercent_Type=Integer
_IngUsedTCAMPercent_Object=MibTableColumn
ingUsedTCAMPercent=_IngUsedTCAMPercent_Object((1,3,6,1,4,1,36673,108,1,1,1,3),_IngUsedTCAMPercent_Type())
ingUsedTCAMPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:ingUsedTCAMPercent.setStatus(_A)
_IngUsedTCAMEntries_Type=Integer
_IngUsedTCAMEntries_Object=MibTableColumn
ingUsedTCAMEntries=_IngUsedTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,1,1,4),_IngUsedTCAMEntries_Type())
ingUsedTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ingUsedTCAMEntries.setStatus(_A)
_IngTotalTCAMEntries_Type=Integer
_IngTotalTCAMEntries_Object=MibTableColumn
ingTotalTCAMEntries=_IngTotalTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,1,1,5),_IngTotalTCAMEntries_Type())
ingTotalTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ingTotalTCAMEntries.setStatus(_A)
_IngDedicatedTCAMEntries_Type=Integer
_IngDedicatedTCAMEntries_Object=MibTableColumn
ingDedicatedTCAMEntries=_IngDedicatedTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,1,1,6),_IngDedicatedTCAMEntries_Type())
ingDedicatedTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ingDedicatedTCAMEntries.setStatus(_A)
_IngSharedTCAMEntries_Type=Integer
_IngSharedTCAMEntries_Object=MibTableColumn
ingSharedTCAMEntries=_IngSharedTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,1,1,7),_IngSharedTCAMEntries_Type())
ingSharedTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ingSharedTCAMEntries.setStatus(_A)
_EgressTCAMUtilizationTable_Object=MibTable
egressTCAMUtilizationTable=_EgressTCAMUtilizationTable_Object((1,3,6,1,4,1,36673,108,1,2))
if mibBuilder.loadTexts:egressTCAMUtilizationTable.setStatus(_A)
_EgressTCAMUtilizationEntry_Object=MibTableRow
egressTCAMUtilizationEntry=_EgressTCAMUtilizationEntry_Object((1,3,6,1,4,1,36673,108,1,2,1))
egressTCAMUtilizationEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:egressTCAMUtilizationEntry.setStatus(_A)
_EgrTCAMGroupName_Type=DisplayString
_EgrTCAMGroupName_Object=MibTableColumn
egrTCAMGroupName=_EgrTCAMGroupName_Object((1,3,6,1,4,1,36673,108,1,2,1,1),_EgrTCAMGroupName_Type())
egrTCAMGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:egrTCAMGroupName.setStatus(_A)
_EgrFreeTCAMEntries_Type=Integer
_EgrFreeTCAMEntries_Object=MibTableColumn
egrFreeTCAMEntries=_EgrFreeTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,2,1,2),_EgrFreeTCAMEntries_Type())
egrFreeTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:egrFreeTCAMEntries.setStatus(_A)
_EgrUsedTCAMPercent_Type=Integer
_EgrUsedTCAMPercent_Object=MibTableColumn
egrUsedTCAMPercent=_EgrUsedTCAMPercent_Object((1,3,6,1,4,1,36673,108,1,2,1,3),_EgrUsedTCAMPercent_Type())
egrUsedTCAMPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:egrUsedTCAMPercent.setStatus(_A)
_EgrUsedTCAMEntries_Type=Integer
_EgrUsedTCAMEntries_Object=MibTableColumn
egrUsedTCAMEntries=_EgrUsedTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,2,1,4),_EgrUsedTCAMEntries_Type())
egrUsedTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:egrUsedTCAMEntries.setStatus(_A)
_EgrTotalTCAMEntries_Type=Integer
_EgrTotalTCAMEntries_Object=MibTableColumn
egrTotalTCAMEntries=_EgrTotalTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,2,1,5),_EgrTotalTCAMEntries_Type())
egrTotalTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:egrTotalTCAMEntries.setStatus(_A)
_EgrDedicatedTCAMEntries_Type=Integer
_EgrDedicatedTCAMEntries_Object=MibTableColumn
egrDedicatedTCAMEntries=_EgrDedicatedTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,2,1,6),_EgrDedicatedTCAMEntries_Type())
egrDedicatedTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:egrDedicatedTCAMEntries.setStatus(_A)
_EgrSharedTCAMEntries_Type=Integer
_EgrSharedTCAMEntries_Object=MibTableColumn
egrSharedTCAMEntries=_EgrSharedTCAMEntries_Object((1,3,6,1,4,1,36673,108,1,2,1,7),_EgrSharedTCAMEntries_Type())
egrSharedTCAMEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:egrSharedTCAMEntries.setStatus(_A)
_TCAMWarningThresholdLevel_Type=Integer
_TCAMWarningThresholdLevel_Object=MibScalar
tCAMWarningThresholdLevel=_TCAMWarningThresholdLevel_Object((1,3,6,1,4,1,36673,108,1,3),_TCAMWarningThresholdLevel_Type())
tCAMWarningThresholdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tCAMWarningThresholdLevel.setStatus(_A)
_TCAMAlertThresholdLevel_Type=Integer
_TCAMAlertThresholdLevel_Object=MibScalar
tCAMAlertThresholdLevel=_TCAMAlertThresholdLevel_Object((1,3,6,1,4,1,36673,108,1,4),_TCAMAlertThresholdLevel_Type())
tCAMAlertThresholdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tCAMAlertThresholdLevel.setStatus(_A)
_TCAMUtilizationAlarmObjects_ObjectIdentity=ObjectIdentity
TCAMUtilizationAlarmObjects=_TCAMUtilizationAlarmObjects_ObjectIdentity((1,3,6,1,4,1,36673,108,2))
_TCAMUtilizationAlarmNotifications_ObjectIdentity=ObjectIdentity
TCAMUtilizationAlarmNotifications=_TCAMUtilizationAlarmNotifications_ObjectIdentity((1,3,6,1,4,1,36673,108,2,1))
ingTCAMWarningThresholdTrap=NotificationType((1,3,6,1,4,1,36673,108,2,1,1))
ingTCAMWarningThresholdTrap.setObjects(*((_C,_D),(_C,_F),(_C,_G)))
if mibBuilder.loadTexts:ingTCAMWarningThresholdTrap.setStatus(_A)
ingTCAMCriticalThresholdTrap=NotificationType((1,3,6,1,4,1,36673,108,2,1,2))
ingTCAMCriticalThresholdTrap.setObjects(*((_C,_D),(_C,_F),(_C,_G)))
if mibBuilder.loadTexts:ingTCAMCriticalThresholdTrap.setStatus(_A)
egrTCAMWarningThresholdTrap=NotificationType((1,3,6,1,4,1,36673,108,2,1,3))
egrTCAMWarningThresholdTrap.setObjects(*((_C,_E),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:egrTCAMWarningThresholdTrap.setStatus(_A)
egrTCAMCriticalThresholdTrap=NotificationType((1,3,6,1,4,1,36673,108,2,1,4))
egrTCAMCriticalThresholdTrap.setObjects(*((_C,_E),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:egrTCAMCriticalThresholdTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'CodeType':CodeType,'UnitType':UnitType,'ipiTCAMutilization':ipiTCAMutilization,'TCAMUtilizationObjects':TCAMUtilizationObjects,'ingressTCAMUtilizationTable':ingressTCAMUtilizationTable,'ingressTCAMUtilizationEntry':ingressTCAMUtilizationEntry,_D:ingTCAMGroupName,'ingFreeTCAMEntries':ingFreeTCAMEntries,_F:ingUsedTCAMPercent,_G:ingUsedTCAMEntries,'ingTotalTCAMEntries':ingTotalTCAMEntries,'ingDedicatedTCAMEntries':ingDedicatedTCAMEntries,'ingSharedTCAMEntries':ingSharedTCAMEntries,'egressTCAMUtilizationTable':egressTCAMUtilizationTable,'egressTCAMUtilizationEntry':egressTCAMUtilizationEntry,_E:egrTCAMGroupName,'egrFreeTCAMEntries':egrFreeTCAMEntries,_H:egrUsedTCAMPercent,_I:egrUsedTCAMEntries,'egrTotalTCAMEntries':egrTotalTCAMEntries,'egrDedicatedTCAMEntries':egrDedicatedTCAMEntries,'egrSharedTCAMEntries':egrSharedTCAMEntries,'tCAMWarningThresholdLevel':tCAMWarningThresholdLevel,'tCAMAlertThresholdLevel':tCAMAlertThresholdLevel,'TCAMUtilizationAlarmObjects':TCAMUtilizationAlarmObjects,'TCAMUtilizationAlarmNotifications':TCAMUtilizationAlarmNotifications,'ingTCAMWarningThresholdTrap':ingTCAMWarningThresholdTrap,'ingTCAMCriticalThresholdTrap':ingTCAMCriticalThresholdTrap,'egrTCAMWarningThresholdTrap':egrTCAMWarningThresholdTrap,'egrTCAMCriticalThresholdTrap':egrTCAMCriticalThresholdTrap})