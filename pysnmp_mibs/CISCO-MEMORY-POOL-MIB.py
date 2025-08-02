_a='ciscoMemoryPoolNotificationCtrlGroup'
_Z='ciscoMemoryPoolNotificationGroup'
_Y='ciscoMemoryPoolGroupRev1'
_X='ciscoMemoryPoolLowMemoryRecoveryNotif'
_W='ciscoMemoryPoolLowMemoryNotif'
_V='ciscoMemoryPoolLowMemoryNotifThreshold'
_U='ciscoMemoryPoolLowMemoryNotifEnable'
_T='ciscoMemoryPoolUtilization10Min'
_S='ciscoMemoryPoolUtilization5Min'
_R='ciscoMemoryPoolUtilization1Min'
_Q='ciscoMemoryPoolUtilizationEntry'
_P='read-write'
_O='ciscoMemoryPoolType'
_N='Integer32'
_M='ciscoMemoryPoolUtilizationGroup'
_L='ciscoMemoryPoolGroup'
_K='deprecated'
_J='ciscoMemoryPoolLargestFree'
_I='ciscoMemoryPoolFree'
_H='ciscoMemoryPoolValid'
_G='ciscoMemoryPoolAlternate'
_F='bytes'
_E='ciscoMemoryPoolUsed'
_D='ciscoMemoryPoolName'
_C='read-only'
_B='current'
_A='CISCO-MEMORY-POOL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percent,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','Percent')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoMemoryPoolMIB=ModuleIdentity((1,3,6,1,4,1,9,9,48))
if mibBuilder.loadTexts:ciscoMemoryPoolMIB.setRevisions(('2013-09-18 00:00','2001-07-31 00:00','1996-02-01 00:00'))
class CiscoMemoryPoolTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiscoMemoryPoolObjects_ObjectIdentity=ObjectIdentity
ciscoMemoryPoolObjects=_CiscoMemoryPoolObjects_ObjectIdentity((1,3,6,1,4,1,9,9,48,1))
_CiscoMemoryPoolTable_Object=MibTable
ciscoMemoryPoolTable=_CiscoMemoryPoolTable_Object((1,3,6,1,4,1,9,9,48,1,1))
if mibBuilder.loadTexts:ciscoMemoryPoolTable.setStatus(_B)
_CiscoMemoryPoolEntry_Object=MibTableRow
ciscoMemoryPoolEntry=_CiscoMemoryPoolEntry_Object((1,3,6,1,4,1,9,9,48,1,1,1))
ciscoMemoryPoolEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:ciscoMemoryPoolEntry.setStatus(_B)
_CiscoMemoryPoolType_Type=CiscoMemoryPoolTypes
_CiscoMemoryPoolType_Object=MibTableColumn
ciscoMemoryPoolType=_CiscoMemoryPoolType_Object((1,3,6,1,4,1,9,9,48,1,1,1,1),_CiscoMemoryPoolType_Type())
ciscoMemoryPoolType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoMemoryPoolType.setStatus(_B)
_CiscoMemoryPoolName_Type=DisplayString
_CiscoMemoryPoolName_Object=MibTableColumn
ciscoMemoryPoolName=_CiscoMemoryPoolName_Object((1,3,6,1,4,1,9,9,48,1,1,1,2),_CiscoMemoryPoolName_Type())
ciscoMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolName.setStatus(_B)
class _CiscoMemoryPoolAlternate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoMemoryPoolAlternate_Type.__name__=_N
_CiscoMemoryPoolAlternate_Object=MibTableColumn
ciscoMemoryPoolAlternate=_CiscoMemoryPoolAlternate_Object((1,3,6,1,4,1,9,9,48,1,1,1,3),_CiscoMemoryPoolAlternate_Type())
ciscoMemoryPoolAlternate.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolAlternate.setStatus(_B)
_CiscoMemoryPoolValid_Type=TruthValue
_CiscoMemoryPoolValid_Object=MibTableColumn
ciscoMemoryPoolValid=_CiscoMemoryPoolValid_Object((1,3,6,1,4,1,9,9,48,1,1,1,4),_CiscoMemoryPoolValid_Type())
ciscoMemoryPoolValid.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolValid.setStatus(_B)
_CiscoMemoryPoolUsed_Type=Gauge32
_CiscoMemoryPoolUsed_Object=MibTableColumn
ciscoMemoryPoolUsed=_CiscoMemoryPoolUsed_Object((1,3,6,1,4,1,9,9,48,1,1,1,5),_CiscoMemoryPoolUsed_Type())
ciscoMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolUsed.setStatus(_B)
if mibBuilder.loadTexts:ciscoMemoryPoolUsed.setUnits(_F)
_CiscoMemoryPoolFree_Type=Gauge32
_CiscoMemoryPoolFree_Object=MibTableColumn
ciscoMemoryPoolFree=_CiscoMemoryPoolFree_Object((1,3,6,1,4,1,9,9,48,1,1,1,6),_CiscoMemoryPoolFree_Type())
ciscoMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolFree.setStatus(_B)
if mibBuilder.loadTexts:ciscoMemoryPoolFree.setUnits(_F)
_CiscoMemoryPoolLargestFree_Type=Gauge32
_CiscoMemoryPoolLargestFree_Object=MibTableColumn
ciscoMemoryPoolLargestFree=_CiscoMemoryPoolLargestFree_Object((1,3,6,1,4,1,9,9,48,1,1,1,7),_CiscoMemoryPoolLargestFree_Type())
ciscoMemoryPoolLargestFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolLargestFree.setStatus(_B)
if mibBuilder.loadTexts:ciscoMemoryPoolLargestFree.setUnits(_F)
_CiscoMemoryPoolLowMemoryNotifThreshold_Type=Percent
_CiscoMemoryPoolLowMemoryNotifThreshold_Object=MibTableColumn
ciscoMemoryPoolLowMemoryNotifThreshold=_CiscoMemoryPoolLowMemoryNotifThreshold_Object((1,3,6,1,4,1,9,9,48,1,1,1,8),_CiscoMemoryPoolLowMemoryNotifThreshold_Type())
ciscoMemoryPoolLowMemoryNotifThreshold.setMaxAccess(_P)
if mibBuilder.loadTexts:ciscoMemoryPoolLowMemoryNotifThreshold.setStatus(_B)
_CiscoMemoryPoolUtilizationTable_Object=MibTable
ciscoMemoryPoolUtilizationTable=_CiscoMemoryPoolUtilizationTable_Object((1,3,6,1,4,1,9,9,48,1,2))
if mibBuilder.loadTexts:ciscoMemoryPoolUtilizationTable.setStatus(_B)
_CiscoMemoryPoolUtilizationEntry_Object=MibTableRow
ciscoMemoryPoolUtilizationEntry=_CiscoMemoryPoolUtilizationEntry_Object((1,3,6,1,4,1,9,9,48,1,2,1))
if mibBuilder.loadTexts:ciscoMemoryPoolUtilizationEntry.setStatus(_B)
_CiscoMemoryPoolUtilization1Min_Type=Percent
_CiscoMemoryPoolUtilization1Min_Object=MibTableColumn
ciscoMemoryPoolUtilization1Min=_CiscoMemoryPoolUtilization1Min_Object((1,3,6,1,4,1,9,9,48,1,2,1,1),_CiscoMemoryPoolUtilization1Min_Type())
ciscoMemoryPoolUtilization1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolUtilization1Min.setStatus(_B)
_CiscoMemoryPoolUtilization5Min_Type=Percent
_CiscoMemoryPoolUtilization5Min_Object=MibTableColumn
ciscoMemoryPoolUtilization5Min=_CiscoMemoryPoolUtilization5Min_Object((1,3,6,1,4,1,9,9,48,1,2,1,2),_CiscoMemoryPoolUtilization5Min_Type())
ciscoMemoryPoolUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolUtilization5Min.setStatus(_B)
_CiscoMemoryPoolUtilization10Min_Type=Percent
_CiscoMemoryPoolUtilization10Min_Object=MibTableColumn
ciscoMemoryPoolUtilization10Min=_CiscoMemoryPoolUtilization10Min_Object((1,3,6,1,4,1,9,9,48,1,2,1,3),_CiscoMemoryPoolUtilization10Min_Type())
ciscoMemoryPoolUtilization10Min.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMemoryPoolUtilization10Min.setStatus(_B)
_CiscoMemoryPoolLowMemoryNotifEnable_Type=TruthValue
_CiscoMemoryPoolLowMemoryNotifEnable_Object=MibScalar
ciscoMemoryPoolLowMemoryNotifEnable=_CiscoMemoryPoolLowMemoryNotifEnable_Object((1,3,6,1,4,1,9,9,48,1,3),_CiscoMemoryPoolLowMemoryNotifEnable_Type())
ciscoMemoryPoolLowMemoryNotifEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:ciscoMemoryPoolLowMemoryNotifEnable.setStatus(_B)
_CiscoMemoryPoolNotifications_ObjectIdentity=ObjectIdentity
ciscoMemoryPoolNotifications=_CiscoMemoryPoolNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,48,2))
_CiscoMemoryPoolMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoMemoryPoolMIBNotificationPrefix=_CiscoMemoryPoolMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,48,2,0))
_CiscoMemoryPoolConformance_ObjectIdentity=ObjectIdentity
ciscoMemoryPoolConformance=_CiscoMemoryPoolConformance_ObjectIdentity((1,3,6,1,4,1,9,9,48,3))
_CiscoMemoryPoolCompliances_ObjectIdentity=ObjectIdentity
ciscoMemoryPoolCompliances=_CiscoMemoryPoolCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,48,3,1))
_CiscoMemoryPoolGroups_ObjectIdentity=ObjectIdentity
ciscoMemoryPoolGroups=_CiscoMemoryPoolGroups_ObjectIdentity((1,3,6,1,4,1,9,9,48,3,2))
ciscoMemoryPoolEntry.registerAugmentions((_A,_Q))
ciscoMemoryPoolUtilizationEntry.setIndexNames(*ciscoMemoryPoolEntry.getIndexNames())
ciscoMemoryPoolGroup=ObjectGroup((1,3,6,1,4,1,9,9,48,3,2,1))
ciscoMemoryPoolGroup.setObjects(*((_A,_D),(_A,_G),(_A,_H),(_A,_E),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoMemoryPoolGroup.setStatus(_K)
ciscoMemoryPoolUtilizationGroup=ObjectGroup((1,3,6,1,4,1,9,9,48,3,2,2))
ciscoMemoryPoolUtilizationGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoMemoryPoolUtilizationGroup.setStatus(_B)
ciscoMemoryPoolNotificationCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,48,3,2,4))
ciscoMemoryPoolNotificationCtrlGroup.setObjects((_A,_U))
if mibBuilder.loadTexts:ciscoMemoryPoolNotificationCtrlGroup.setStatus(_B)
ciscoMemoryPoolGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,48,3,2,5))
ciscoMemoryPoolGroupRev1.setObjects(*((_A,_D),(_A,_G),(_A,_H),(_A,_E),(_A,_I),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:ciscoMemoryPoolGroupRev1.setStatus(_B)
ciscoMemoryPoolLowMemoryNotif=NotificationType((1,3,6,1,4,1,9,9,48,2,0,1))
ciscoMemoryPoolLowMemoryNotif.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:ciscoMemoryPoolLowMemoryNotif.setStatus(_B)
ciscoMemoryPoolLowMemoryRecoveryNotif=NotificationType((1,3,6,1,4,1,9,9,48,2,0,2))
ciscoMemoryPoolLowMemoryRecoveryNotif.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:ciscoMemoryPoolLowMemoryRecoveryNotif.setStatus(_B)
ciscoMemoryPoolNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,48,3,2,3))
ciscoMemoryPoolNotificationGroup.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoMemoryPoolNotificationGroup.setStatus(_B)
ciscoMemoryPoolCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,48,3,1,1))
ciscoMemoryPoolCompliance.setObjects((_A,_L))
if mibBuilder.loadTexts:ciscoMemoryPoolCompliance.setStatus(_K)
ciscoMemoryPoolComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,48,3,1,2))
ciscoMemoryPoolComplianceRev1.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoMemoryPoolComplianceRev1.setStatus(_K)
ciscoMemoryPoolComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,48,3,1,3))
ciscoMemoryPoolComplianceRev2.setObjects(*((_A,_Y),(_A,_M),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoMemoryPoolComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoMemoryPoolTypes':CiscoMemoryPoolTypes,'ciscoMemoryPoolMIB':ciscoMemoryPoolMIB,'ciscoMemoryPoolObjects':ciscoMemoryPoolObjects,'ciscoMemoryPoolTable':ciscoMemoryPoolTable,'ciscoMemoryPoolEntry':ciscoMemoryPoolEntry,_O:ciscoMemoryPoolType,_D:ciscoMemoryPoolName,_G:ciscoMemoryPoolAlternate,_H:ciscoMemoryPoolValid,_E:ciscoMemoryPoolUsed,_I:ciscoMemoryPoolFree,_J:ciscoMemoryPoolLargestFree,_V:ciscoMemoryPoolLowMemoryNotifThreshold,'ciscoMemoryPoolUtilizationTable':ciscoMemoryPoolUtilizationTable,_Q:ciscoMemoryPoolUtilizationEntry,_R:ciscoMemoryPoolUtilization1Min,_S:ciscoMemoryPoolUtilization5Min,_T:ciscoMemoryPoolUtilization10Min,_U:ciscoMemoryPoolLowMemoryNotifEnable,'ciscoMemoryPoolNotifications':ciscoMemoryPoolNotifications,'ciscoMemoryPoolMIBNotificationPrefix':ciscoMemoryPoolMIBNotificationPrefix,_W:ciscoMemoryPoolLowMemoryNotif,_X:ciscoMemoryPoolLowMemoryRecoveryNotif,'ciscoMemoryPoolConformance':ciscoMemoryPoolConformance,'ciscoMemoryPoolCompliances':ciscoMemoryPoolCompliances,'ciscoMemoryPoolCompliance':ciscoMemoryPoolCompliance,'ciscoMemoryPoolComplianceRev1':ciscoMemoryPoolComplianceRev1,'ciscoMemoryPoolComplianceRev2':ciscoMemoryPoolComplianceRev2,'ciscoMemoryPoolGroups':ciscoMemoryPoolGroups,_L:ciscoMemoryPoolGroup,_M:ciscoMemoryPoolUtilizationGroup,_Z:ciscoMemoryPoolNotificationGroup,_a:ciscoMemoryPoolNotificationCtrlGroup,_Y:ciscoMemoryPoolGroupRev1})