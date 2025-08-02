_Y='myMemoryPoolUtilizationMIBGroup'
_X='myNodeMemoryPoolCritical'
_W='myNodeMemoryPoolWarning'
_V='myNodeMemoryPoolFree'
_U='myNodeMemoryPoolUsed'
_T='myNodeMemoryPoolSize'
_S='myNodeMemoryPoolLargestUtilization'
_R='myNodeMemoryPoolLowestUtilization'
_Q='myNodeMemoryPoolCurrentUtilization'
_P='myNodeMemoryPoolName'
_O='myMemoryPoolCritical'
_N='myMemoryPoolWarning'
_M='myMemoryPoolFree'
_L='myMemoryPoolUsed'
_K='myMemoryPoolSize'
_J='myMemoryPoolLargestUtilization'
_I='myMemoryPoolLowestUtilization'
_H='myMemoryPoolCurrentUtilization'
_G='myMemoryPoolName'
_F='myNodeMemoryPoolIndex'
_E='myMemoryPoolIndex'
_D='read-write'
_C='read-only'
_B='DES7200-MEMORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
myMemoryMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,35))
if mibBuilder.loadTexts:myMemoryMIB.setRevisions(('2003-10-14 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MyMemoryPoolMIBObjects_ObjectIdentity=ObjectIdentity
myMemoryPoolMIBObjects=_MyMemoryPoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,35,1))
_MyMemoryPoolUtilizationTable_Object=MibTable
myMemoryPoolUtilizationTable=_MyMemoryPoolUtilizationTable_Object((1,3,6,1,4,1,171,10,97,2,35,1,1))
if mibBuilder.loadTexts:myMemoryPoolUtilizationTable.setStatus(_A)
_MyMemoryPoolUtilizationEntry_Object=MibTableRow
myMemoryPoolUtilizationEntry=_MyMemoryPoolUtilizationEntry_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1))
myMemoryPoolUtilizationEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:myMemoryPoolUtilizationEntry.setStatus(_A)
_MyMemoryPoolIndex_Type=Integer32
_MyMemoryPoolIndex_Object=MibTableColumn
myMemoryPoolIndex=_MyMemoryPoolIndex_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,1),_MyMemoryPoolIndex_Type())
myMemoryPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolIndex.setStatus(_A)
_MyMemoryPoolName_Type=DisplayString
_MyMemoryPoolName_Object=MibTableColumn
myMemoryPoolName=_MyMemoryPoolName_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,2),_MyMemoryPoolName_Type())
myMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolName.setStatus(_A)
_MyMemoryPoolCurrentUtilization_Type=Percent
_MyMemoryPoolCurrentUtilization_Object=MibTableColumn
myMemoryPoolCurrentUtilization=_MyMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,3),_MyMemoryPoolCurrentUtilization_Type())
myMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolCurrentUtilization.setStatus(_A)
_MyMemoryPoolLowestUtilization_Type=Percent
_MyMemoryPoolLowestUtilization_Object=MibTableColumn
myMemoryPoolLowestUtilization=_MyMemoryPoolLowestUtilization_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,4),_MyMemoryPoolLowestUtilization_Type())
myMemoryPoolLowestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolLowestUtilization.setStatus(_A)
_MyMemoryPoolLargestUtilization_Type=Percent
_MyMemoryPoolLargestUtilization_Object=MibTableColumn
myMemoryPoolLargestUtilization=_MyMemoryPoolLargestUtilization_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,5),_MyMemoryPoolLargestUtilization_Type())
myMemoryPoolLargestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolLargestUtilization.setStatus(_A)
_MyMemoryPoolSize_Type=Integer32
_MyMemoryPoolSize_Object=MibTableColumn
myMemoryPoolSize=_MyMemoryPoolSize_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,6),_MyMemoryPoolSize_Type())
myMemoryPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolSize.setStatus(_A)
_MyMemoryPoolUsed_Type=Integer32
_MyMemoryPoolUsed_Object=MibTableColumn
myMemoryPoolUsed=_MyMemoryPoolUsed_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,7),_MyMemoryPoolUsed_Type())
myMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolUsed.setStatus(_A)
_MyMemoryPoolFree_Type=Integer32
_MyMemoryPoolFree_Object=MibTableColumn
myMemoryPoolFree=_MyMemoryPoolFree_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,8),_MyMemoryPoolFree_Type())
myMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:myMemoryPoolFree.setStatus(_A)
_MyMemoryPoolWarning_Type=Percent
_MyMemoryPoolWarning_Object=MibTableColumn
myMemoryPoolWarning=_MyMemoryPoolWarning_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,9),_MyMemoryPoolWarning_Type())
myMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:myMemoryPoolWarning.setStatus(_A)
_MyMemoryPoolCritical_Type=Percent
_MyMemoryPoolCritical_Object=MibTableColumn
myMemoryPoolCritical=_MyMemoryPoolCritical_Object((1,3,6,1,4,1,171,10,97,2,35,1,1,1,10),_MyMemoryPoolCritical_Type())
myMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:myMemoryPoolCritical.setStatus(_A)
_MyNodeMemoryPoolTable_Object=MibTable
myNodeMemoryPoolTable=_MyNodeMemoryPoolTable_Object((1,3,6,1,4,1,171,10,97,2,35,1,2))
if mibBuilder.loadTexts:myNodeMemoryPoolTable.setStatus(_A)
_MyNodeMemoryPoolEntry_Object=MibTableRow
myNodeMemoryPoolEntry=_MyNodeMemoryPoolEntry_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1))
myNodeMemoryPoolEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:myNodeMemoryPoolEntry.setStatus(_A)
_MyNodeMemoryPoolIndex_Type=Integer32
_MyNodeMemoryPoolIndex_Object=MibTableColumn
myNodeMemoryPoolIndex=_MyNodeMemoryPoolIndex_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,1),_MyNodeMemoryPoolIndex_Type())
myNodeMemoryPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolIndex.setStatus(_A)
_MyNodeMemoryPoolName_Type=DisplayString
_MyNodeMemoryPoolName_Object=MibTableColumn
myNodeMemoryPoolName=_MyNodeMemoryPoolName_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,2),_MyNodeMemoryPoolName_Type())
myNodeMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolName.setStatus(_A)
_MyNodeMemoryPoolCurrentUtilization_Type=Percent
_MyNodeMemoryPoolCurrentUtilization_Object=MibTableColumn
myNodeMemoryPoolCurrentUtilization=_MyNodeMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,3),_MyNodeMemoryPoolCurrentUtilization_Type())
myNodeMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolCurrentUtilization.setStatus(_A)
_MyNodeMemoryPoolLowestUtilization_Type=Percent
_MyNodeMemoryPoolLowestUtilization_Object=MibTableColumn
myNodeMemoryPoolLowestUtilization=_MyNodeMemoryPoolLowestUtilization_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,4),_MyNodeMemoryPoolLowestUtilization_Type())
myNodeMemoryPoolLowestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolLowestUtilization.setStatus(_A)
_MyNodeMemoryPoolLargestUtilization_Type=Percent
_MyNodeMemoryPoolLargestUtilization_Object=MibTableColumn
myNodeMemoryPoolLargestUtilization=_MyNodeMemoryPoolLargestUtilization_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,5),_MyNodeMemoryPoolLargestUtilization_Type())
myNodeMemoryPoolLargestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolLargestUtilization.setStatus(_A)
_MyNodeMemoryPoolSize_Type=Integer32
_MyNodeMemoryPoolSize_Object=MibTableColumn
myNodeMemoryPoolSize=_MyNodeMemoryPoolSize_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,6),_MyNodeMemoryPoolSize_Type())
myNodeMemoryPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolSize.setStatus(_A)
_MyNodeMemoryPoolUsed_Type=Integer32
_MyNodeMemoryPoolUsed_Object=MibTableColumn
myNodeMemoryPoolUsed=_MyNodeMemoryPoolUsed_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,7),_MyNodeMemoryPoolUsed_Type())
myNodeMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolUsed.setStatus(_A)
_MyNodeMemoryPoolFree_Type=Integer32
_MyNodeMemoryPoolFree_Object=MibTableColumn
myNodeMemoryPoolFree=_MyNodeMemoryPoolFree_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,8),_MyNodeMemoryPoolFree_Type())
myNodeMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeMemoryPoolFree.setStatus(_A)
_MyNodeMemoryPoolWarning_Type=Percent
_MyNodeMemoryPoolWarning_Object=MibTableColumn
myNodeMemoryPoolWarning=_MyNodeMemoryPoolWarning_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,9),_MyNodeMemoryPoolWarning_Type())
myNodeMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:myNodeMemoryPoolWarning.setStatus(_A)
_MyNodeMemoryPoolCritical_Type=Percent
_MyNodeMemoryPoolCritical_Object=MibTableColumn
myNodeMemoryPoolCritical=_MyNodeMemoryPoolCritical_Object((1,3,6,1,4,1,171,10,97,2,35,1,2,1,10),_MyNodeMemoryPoolCritical_Type())
myNodeMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:myNodeMemoryPoolCritical.setStatus(_A)
_MyMemoryMIBConformance_ObjectIdentity=ObjectIdentity
myMemoryMIBConformance=_MyMemoryMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,35,2))
_MyMemoryMIBCompliances_ObjectIdentity=ObjectIdentity
myMemoryMIBCompliances=_MyMemoryMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,35,2,1))
_MyMemoryMIBGroups_ObjectIdentity=ObjectIdentity
myMemoryMIBGroups=_MyMemoryMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,35,2,2))
myMemoryPoolUtilizationMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,35,2,2,1))
myMemoryPoolUtilizationMIBGroup.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:myMemoryPoolUtilizationMIBGroup.setStatus(_A)
myNodeMemoryPoolMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,35,2,2,2))
myNodeMemoryPoolMIBGroup.setObjects(*((_B,_F),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:myNodeMemoryPoolMIBGroup.setStatus(_A)
myMemoryMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,35,2,1,1))
myMemoryMIBCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:myMemoryMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Percent':Percent,'myMemoryMIB':myMemoryMIB,'myMemoryPoolMIBObjects':myMemoryPoolMIBObjects,'myMemoryPoolUtilizationTable':myMemoryPoolUtilizationTable,'myMemoryPoolUtilizationEntry':myMemoryPoolUtilizationEntry,_E:myMemoryPoolIndex,_G:myMemoryPoolName,_H:myMemoryPoolCurrentUtilization,_I:myMemoryPoolLowestUtilization,_J:myMemoryPoolLargestUtilization,_K:myMemoryPoolSize,_L:myMemoryPoolUsed,_M:myMemoryPoolFree,_N:myMemoryPoolWarning,_O:myMemoryPoolCritical,'myNodeMemoryPoolTable':myNodeMemoryPoolTable,'myNodeMemoryPoolEntry':myNodeMemoryPoolEntry,_F:myNodeMemoryPoolIndex,_P:myNodeMemoryPoolName,_Q:myNodeMemoryPoolCurrentUtilization,_R:myNodeMemoryPoolLowestUtilization,_S:myNodeMemoryPoolLargestUtilization,_T:myNodeMemoryPoolSize,_U:myNodeMemoryPoolUsed,_V:myNodeMemoryPoolFree,_W:myNodeMemoryPoolWarning,_X:myNodeMemoryPoolCritical,'myMemoryMIBConformance':myMemoryMIBConformance,'myMemoryMIBCompliances':myMemoryMIBCompliances,'myMemoryMIBCompliance':myMemoryMIBCompliance,'myMemoryMIBGroups':myMemoryMIBGroups,_Y:myMemoryPoolUtilizationMIBGroup,'myNodeMemoryPoolMIBGroup':myNodeMemoryPoolMIBGroup})