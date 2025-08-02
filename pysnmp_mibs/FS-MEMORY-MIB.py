_g='fsMemoryPoolUtilizationMIBGroup'
_f='fsNodeMemoryPoolFreeSize'
_e='fsNodeMemoryPoolUsedSize'
_d='fsNodeMemoryPoolTotalSize'
_c='fsNodeMemoryPoolCritical'
_b='fsNodeMemoryPoolWarning'
_a='fsNodeMemoryPoolFree'
_Z='fsNodeMemoryPoolUsed'
_Y='fsNodeMemoryPoolSize'
_X='fsNodeMemoryPoolLargestUtilization'
_W='fsNodeMemoryPoolLowestUtilization'
_V='fsNodeMemoryPoolCurrentUtilization'
_U='fsNodeMemoryPoolName'
_T='fsMemoryPoolFreeSize'
_S='fsMemoryPoolUsedSize'
_R='fsMemoryPoolTotalSize'
_Q='fsMemoryPoolAverageUtilization'
_P='fsMemoryPoolCritical'
_O='fsMemoryPoolWarning'
_N='fsMemoryPoolFree'
_M='fsMemoryPoolUsed'
_L='fsMemoryPoolSize'
_K='fsMemoryPoolLargestUtilization'
_J='fsMemoryPoolLowestUtilization'
_I='fsMemoryPoolCurrentUtilization'
_H='fsMemoryPoolName'
_G='fsLankApMemoryPoolMacAddr'
_F='fsNodeMemoryPoolIndex'
_E='fsMemoryPoolIndex'
_D='read-write'
_C='read-only'
_B='FS-MEMORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsMemoryMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,35))
if mibBuilder.loadTexts:fsMemoryMIB.setRevisions(('2003-10-14 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsMemoryPoolMIBObjects_ObjectIdentity=ObjectIdentity
fsMemoryPoolMIBObjects=_FsMemoryPoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,35,1))
_FsMemoryPoolUtilizationTable_Object=MibTable
fsMemoryPoolUtilizationTable=_FsMemoryPoolUtilizationTable_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1))
if mibBuilder.loadTexts:fsMemoryPoolUtilizationTable.setStatus(_A)
_FsMemoryPoolUtilizationEntry_Object=MibTableRow
fsMemoryPoolUtilizationEntry=_FsMemoryPoolUtilizationEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1))
fsMemoryPoolUtilizationEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsMemoryPoolUtilizationEntry.setStatus(_A)
_FsMemoryPoolIndex_Type=Integer32
_FsMemoryPoolIndex_Object=MibTableColumn
fsMemoryPoolIndex=_FsMemoryPoolIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,1),_FsMemoryPoolIndex_Type())
fsMemoryPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolIndex.setStatus(_A)
_FsMemoryPoolName_Type=DisplayString
_FsMemoryPoolName_Object=MibTableColumn
fsMemoryPoolName=_FsMemoryPoolName_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,2),_FsMemoryPoolName_Type())
fsMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolName.setStatus(_A)
_FsMemoryPoolCurrentUtilization_Type=Percent
_FsMemoryPoolCurrentUtilization_Object=MibTableColumn
fsMemoryPoolCurrentUtilization=_FsMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,3),_FsMemoryPoolCurrentUtilization_Type())
fsMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolCurrentUtilization.setStatus(_A)
_FsMemoryPoolLowestUtilization_Type=Percent
_FsMemoryPoolLowestUtilization_Object=MibTableColumn
fsMemoryPoolLowestUtilization=_FsMemoryPoolLowestUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,4),_FsMemoryPoolLowestUtilization_Type())
fsMemoryPoolLowestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolLowestUtilization.setStatus(_A)
_FsMemoryPoolLargestUtilization_Type=Percent
_FsMemoryPoolLargestUtilization_Object=MibTableColumn
fsMemoryPoolLargestUtilization=_FsMemoryPoolLargestUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,5),_FsMemoryPoolLargestUtilization_Type())
fsMemoryPoolLargestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolLargestUtilization.setStatus(_A)
_FsMemoryPoolSize_Type=Integer32
_FsMemoryPoolSize_Object=MibTableColumn
fsMemoryPoolSize=_FsMemoryPoolSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,6),_FsMemoryPoolSize_Type())
fsMemoryPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolSize.setStatus(_A)
_FsMemoryPoolUsed_Type=Integer32
_FsMemoryPoolUsed_Object=MibTableColumn
fsMemoryPoolUsed=_FsMemoryPoolUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,7),_FsMemoryPoolUsed_Type())
fsMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolUsed.setStatus(_A)
_FsMemoryPoolFree_Type=Integer32
_FsMemoryPoolFree_Object=MibTableColumn
fsMemoryPoolFree=_FsMemoryPoolFree_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,8),_FsMemoryPoolFree_Type())
fsMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolFree.setStatus(_A)
_FsMemoryPoolWarning_Type=Percent
_FsMemoryPoolWarning_Object=MibTableColumn
fsMemoryPoolWarning=_FsMemoryPoolWarning_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,9),_FsMemoryPoolWarning_Type())
fsMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMemoryPoolWarning.setStatus(_A)
_FsMemoryPoolCritical_Type=Percent
_FsMemoryPoolCritical_Object=MibTableColumn
fsMemoryPoolCritical=_FsMemoryPoolCritical_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,10),_FsMemoryPoolCritical_Type())
fsMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMemoryPoolCritical.setStatus(_A)
_FsMemoryPoolAverageUtilization_Type=Percent
_FsMemoryPoolAverageUtilization_Object=MibTableColumn
fsMemoryPoolAverageUtilization=_FsMemoryPoolAverageUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,11),_FsMemoryPoolAverageUtilization_Type())
fsMemoryPoolAverageUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolAverageUtilization.setStatus(_A)
_FsMemoryPoolTotalSize_Type=Gauge32
_FsMemoryPoolTotalSize_Object=MibTableColumn
fsMemoryPoolTotalSize=_FsMemoryPoolTotalSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,12),_FsMemoryPoolTotalSize_Type())
fsMemoryPoolTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolTotalSize.setStatus(_A)
_FsMemoryPoolUsedSize_Type=Gauge32
_FsMemoryPoolUsedSize_Object=MibTableColumn
fsMemoryPoolUsedSize=_FsMemoryPoolUsedSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,13),_FsMemoryPoolUsedSize_Type())
fsMemoryPoolUsedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolUsedSize.setStatus(_A)
_FsMemoryPoolFreeSize_Type=Gauge32
_FsMemoryPoolFreeSize_Object=MibTableColumn
fsMemoryPoolFreeSize=_FsMemoryPoolFreeSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,1,1,14),_FsMemoryPoolFreeSize_Type())
fsMemoryPoolFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMemoryPoolFreeSize.setStatus(_A)
_FsNodeMemoryPoolTable_Object=MibTable
fsNodeMemoryPoolTable=_FsNodeMemoryPoolTable_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2))
if mibBuilder.loadTexts:fsNodeMemoryPoolTable.setStatus(_A)
_FsNodeMemoryPoolEntry_Object=MibTableRow
fsNodeMemoryPoolEntry=_FsNodeMemoryPoolEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1))
fsNodeMemoryPoolEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsNodeMemoryPoolEntry.setStatus(_A)
_FsNodeMemoryPoolIndex_Type=Integer32
_FsNodeMemoryPoolIndex_Object=MibTableColumn
fsNodeMemoryPoolIndex=_FsNodeMemoryPoolIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,1),_FsNodeMemoryPoolIndex_Type())
fsNodeMemoryPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolIndex.setStatus(_A)
_FsNodeMemoryPoolName_Type=DisplayString
_FsNodeMemoryPoolName_Object=MibTableColumn
fsNodeMemoryPoolName=_FsNodeMemoryPoolName_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,2),_FsNodeMemoryPoolName_Type())
fsNodeMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolName.setStatus(_A)
_FsNodeMemoryPoolCurrentUtilization_Type=Percent
_FsNodeMemoryPoolCurrentUtilization_Object=MibTableColumn
fsNodeMemoryPoolCurrentUtilization=_FsNodeMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,3),_FsNodeMemoryPoolCurrentUtilization_Type())
fsNodeMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolCurrentUtilization.setStatus(_A)
_FsNodeMemoryPoolLowestUtilization_Type=Percent
_FsNodeMemoryPoolLowestUtilization_Object=MibTableColumn
fsNodeMemoryPoolLowestUtilization=_FsNodeMemoryPoolLowestUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,4),_FsNodeMemoryPoolLowestUtilization_Type())
fsNodeMemoryPoolLowestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolLowestUtilization.setStatus(_A)
_FsNodeMemoryPoolLargestUtilization_Type=Percent
_FsNodeMemoryPoolLargestUtilization_Object=MibTableColumn
fsNodeMemoryPoolLargestUtilization=_FsNodeMemoryPoolLargestUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,5),_FsNodeMemoryPoolLargestUtilization_Type())
fsNodeMemoryPoolLargestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolLargestUtilization.setStatus(_A)
_FsNodeMemoryPoolSize_Type=Integer32
_FsNodeMemoryPoolSize_Object=MibTableColumn
fsNodeMemoryPoolSize=_FsNodeMemoryPoolSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,6),_FsNodeMemoryPoolSize_Type())
fsNodeMemoryPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolSize.setStatus(_A)
_FsNodeMemoryPoolUsed_Type=Integer32
_FsNodeMemoryPoolUsed_Object=MibTableColumn
fsNodeMemoryPoolUsed=_FsNodeMemoryPoolUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,7),_FsNodeMemoryPoolUsed_Type())
fsNodeMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolUsed.setStatus(_A)
_FsNodeMemoryPoolFree_Type=Integer32
_FsNodeMemoryPoolFree_Object=MibTableColumn
fsNodeMemoryPoolFree=_FsNodeMemoryPoolFree_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,8),_FsNodeMemoryPoolFree_Type())
fsNodeMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolFree.setStatus(_A)
_FsNodeMemoryPoolWarning_Type=Percent
_FsNodeMemoryPoolWarning_Object=MibTableColumn
fsNodeMemoryPoolWarning=_FsNodeMemoryPoolWarning_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,9),_FsNodeMemoryPoolWarning_Type())
fsNodeMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:fsNodeMemoryPoolWarning.setStatus(_A)
_FsNodeMemoryPoolCritical_Type=Percent
_FsNodeMemoryPoolCritical_Object=MibTableColumn
fsNodeMemoryPoolCritical=_FsNodeMemoryPoolCritical_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,10),_FsNodeMemoryPoolCritical_Type())
fsNodeMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:fsNodeMemoryPoolCritical.setStatus(_A)
_FsNodeMemoryPoolTotalSize_Type=Gauge32
_FsNodeMemoryPoolTotalSize_Object=MibTableColumn
fsNodeMemoryPoolTotalSize=_FsNodeMemoryPoolTotalSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,11),_FsNodeMemoryPoolTotalSize_Type())
fsNodeMemoryPoolTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolTotalSize.setStatus(_A)
_FsNodeMemoryPoolUsedSize_Type=Gauge32
_FsNodeMemoryPoolUsedSize_Object=MibTableColumn
fsNodeMemoryPoolUsedSize=_FsNodeMemoryPoolUsedSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,12),_FsNodeMemoryPoolUsedSize_Type())
fsNodeMemoryPoolUsedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolUsedSize.setStatus(_A)
_FsNodeMemoryPoolFreeSize_Type=Gauge32
_FsNodeMemoryPoolFreeSize_Object=MibTableColumn
fsNodeMemoryPoolFreeSize=_FsNodeMemoryPoolFreeSize_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,2,1,13),_FsNodeMemoryPoolFreeSize_Type())
fsNodeMemoryPoolFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeMemoryPoolFreeSize.setStatus(_A)
_FsLankApMemoryPoolTable_Object=MibTable
fsLankApMemoryPoolTable=_FsLankApMemoryPoolTable_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,3))
if mibBuilder.loadTexts:fsLankApMemoryPoolTable.setStatus(_A)
_FsLankApMemoryPoolEntry_Object=MibTableRow
fsLankApMemoryPoolEntry=_FsLankApMemoryPoolEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,3,1))
fsLankApMemoryPoolEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsLankApMemoryPoolEntry.setStatus(_A)
_FsLankApMemoryPoolMacAddr_Type=MacAddress
_FsLankApMemoryPoolMacAddr_Object=MibTableColumn
fsLankApMemoryPoolMacAddr=_FsLankApMemoryPoolMacAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,3,1,1),_FsLankApMemoryPoolMacAddr_Type())
fsLankApMemoryPoolMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLankApMemoryPoolMacAddr.setStatus(_A)
_FsLankApMemoryPoolWarning_Type=Percent
_FsLankApMemoryPoolWarning_Object=MibTableColumn
fsLankApMemoryPoolWarning=_FsLankApMemoryPoolWarning_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,3,1,2),_FsLankApMemoryPoolWarning_Type())
fsLankApMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLankApMemoryPoolWarning.setStatus(_A)
_FsLankApMemoryPoolCritical_Type=Percent
_FsLankApMemoryPoolCritical_Object=MibTableColumn
fsLankApMemoryPoolCritical=_FsLankApMemoryPoolCritical_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,3,1,3),_FsLankApMemoryPoolCritical_Type())
fsLankApMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLankApMemoryPoolCritical.setStatus(_A)
_FsLankApMemoryPoolCurrentUtilization_Type=Percent
_FsLankApMemoryPoolCurrentUtilization_Object=MibTableColumn
fsLankApMemoryPoolCurrentUtilization=_FsLankApMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,3,1,4),_FsLankApMemoryPoolCurrentUtilization_Type())
fsLankApMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLankApMemoryPoolCurrentUtilization.setStatus(_A)
_FsLankApMemoryPoolAverageUtilization_Type=Percent
_FsLankApMemoryPoolAverageUtilization_Object=MibTableColumn
fsLankApMemoryPoolAverageUtilization=_FsLankApMemoryPoolAverageUtilization_Object((1,3,6,1,4,1,52642,1,1,10,2,35,1,3,1,5),_FsLankApMemoryPoolAverageUtilization_Type())
fsLankApMemoryPoolAverageUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLankApMemoryPoolAverageUtilization.setStatus(_A)
_FsMemoryMIBConformance_ObjectIdentity=ObjectIdentity
fsMemoryMIBConformance=_FsMemoryMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,35,2))
_FsMemoryMIBCompliances_ObjectIdentity=ObjectIdentity
fsMemoryMIBCompliances=_FsMemoryMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,35,2,1))
_FsMemoryMIBGroups_ObjectIdentity=ObjectIdentity
fsMemoryMIBGroups=_FsMemoryMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,35,2,2))
fsMemoryPoolUtilizationMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,35,2,2,1))
fsMemoryPoolUtilizationMIBGroup.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:fsMemoryPoolUtilizationMIBGroup.setStatus(_A)
fsNodeMemoryPoolMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,35,2,2,2))
fsNodeMemoryPoolMIBGroup.setObjects(*((_B,_F),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:fsNodeMemoryPoolMIBGroup.setStatus(_A)
fsMemoryMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,35,2,1,1))
fsMemoryMIBCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:fsMemoryMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Percent':Percent,'fsMemoryMIB':fsMemoryMIB,'fsMemoryPoolMIBObjects':fsMemoryPoolMIBObjects,'fsMemoryPoolUtilizationTable':fsMemoryPoolUtilizationTable,'fsMemoryPoolUtilizationEntry':fsMemoryPoolUtilizationEntry,_E:fsMemoryPoolIndex,_H:fsMemoryPoolName,_I:fsMemoryPoolCurrentUtilization,_J:fsMemoryPoolLowestUtilization,_K:fsMemoryPoolLargestUtilization,_L:fsMemoryPoolSize,_M:fsMemoryPoolUsed,_N:fsMemoryPoolFree,_O:fsMemoryPoolWarning,_P:fsMemoryPoolCritical,_Q:fsMemoryPoolAverageUtilization,_R:fsMemoryPoolTotalSize,_S:fsMemoryPoolUsedSize,_T:fsMemoryPoolFreeSize,'fsNodeMemoryPoolTable':fsNodeMemoryPoolTable,'fsNodeMemoryPoolEntry':fsNodeMemoryPoolEntry,_F:fsNodeMemoryPoolIndex,_U:fsNodeMemoryPoolName,_V:fsNodeMemoryPoolCurrentUtilization,_W:fsNodeMemoryPoolLowestUtilization,_X:fsNodeMemoryPoolLargestUtilization,_Y:fsNodeMemoryPoolSize,_Z:fsNodeMemoryPoolUsed,_a:fsNodeMemoryPoolFree,_b:fsNodeMemoryPoolWarning,_c:fsNodeMemoryPoolCritical,_d:fsNodeMemoryPoolTotalSize,_e:fsNodeMemoryPoolUsedSize,_f:fsNodeMemoryPoolFreeSize,'fsLankApMemoryPoolTable':fsLankApMemoryPoolTable,'fsLankApMemoryPoolEntry':fsLankApMemoryPoolEntry,_G:fsLankApMemoryPoolMacAddr,'fsLankApMemoryPoolWarning':fsLankApMemoryPoolWarning,'fsLankApMemoryPoolCritical':fsLankApMemoryPoolCritical,'fsLankApMemoryPoolCurrentUtilization':fsLankApMemoryPoolCurrentUtilization,'fsLankApMemoryPoolAverageUtilization':fsLankApMemoryPoolAverageUtilization,'fsMemoryMIBConformance':fsMemoryMIBConformance,'fsMemoryMIBCompliances':fsMemoryMIBCompliances,'fsMemoryMIBCompliance':fsMemoryMIBCompliance,'fsMemoryMIBGroups':fsMemoryMIBGroups,_g:fsMemoryPoolUtilizationMIBGroup,'fsNodeMemoryPoolMIBGroup':fsNodeMemoryPoolMIBGroup})