_g='qtechMemoryPoolUtilizationMIBGroup'
_f='qtechNodeMemoryPoolFreeSize'
_e='qtechNodeMemoryPoolUsedSize'
_d='qtechNodeMemoryPoolTotalSize'
_c='qtechNodeMemoryPoolCritical'
_b='qtechNodeMemoryPoolWarning'
_a='qtechNodeMemoryPoolFree'
_Z='qtechNodeMemoryPoolUsed'
_Y='qtechNodeMemoryPoolSize'
_X='qtechNodeMemoryPoolLargestUtilization'
_W='qtechNodeMemoryPoolLowestUtilization'
_V='qtechNodeMemoryPoolCurrentUtilization'
_U='qtechNodeMemoryPoolName'
_T='qtechMemoryPoolFreeSize'
_S='qtechMemoryPoolUsedSize'
_R='qtechMemoryPoolTotalSize'
_Q='qtechMemoryPoolAverageUtilization'
_P='qtechMemoryPoolCritical'
_O='qtechMemoryPoolWarning'
_N='qtechMemoryPoolFree'
_M='qtechMemoryPoolUsed'
_L='qtechMemoryPoolSize'
_K='qtechMemoryPoolLargestUtilization'
_J='qtechMemoryPoolLowestUtilization'
_I='qtechMemoryPoolCurrentUtilization'
_H='qtechMemoryPoolName'
_G='qtechLankApMemoryPoolMacAddr'
_F='qtechNodeMemoryPoolIndex'
_E='qtechMemoryPoolIndex'
_D='read-write'
_C='read-only'
_B='QTECH-MEMORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
qtechMemoryMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,35))
if mibBuilder.loadTexts:qtechMemoryMIB.setRevisions(('2003-10-14 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechMemoryPoolMIBObjects_ObjectIdentity=ObjectIdentity
qtechMemoryPoolMIBObjects=_QtechMemoryPoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,35,1))
_QtechMemoryPoolUtilizationTable_Object=MibTable
qtechMemoryPoolUtilizationTable=_QtechMemoryPoolUtilizationTable_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1))
if mibBuilder.loadTexts:qtechMemoryPoolUtilizationTable.setStatus(_A)
_QtechMemoryPoolUtilizationEntry_Object=MibTableRow
qtechMemoryPoolUtilizationEntry=_QtechMemoryPoolUtilizationEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1))
qtechMemoryPoolUtilizationEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechMemoryPoolUtilizationEntry.setStatus(_A)
_QtechMemoryPoolIndex_Type=Integer32
_QtechMemoryPoolIndex_Object=MibTableColumn
qtechMemoryPoolIndex=_QtechMemoryPoolIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,1),_QtechMemoryPoolIndex_Type())
qtechMemoryPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolIndex.setStatus(_A)
_QtechMemoryPoolName_Type=DisplayString
_QtechMemoryPoolName_Object=MibTableColumn
qtechMemoryPoolName=_QtechMemoryPoolName_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,2),_QtechMemoryPoolName_Type())
qtechMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolName.setStatus(_A)
_QtechMemoryPoolCurrentUtilization_Type=Percent
_QtechMemoryPoolCurrentUtilization_Object=MibTableColumn
qtechMemoryPoolCurrentUtilization=_QtechMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,3),_QtechMemoryPoolCurrentUtilization_Type())
qtechMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolCurrentUtilization.setStatus(_A)
_QtechMemoryPoolLowestUtilization_Type=Percent
_QtechMemoryPoolLowestUtilization_Object=MibTableColumn
qtechMemoryPoolLowestUtilization=_QtechMemoryPoolLowestUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,4),_QtechMemoryPoolLowestUtilization_Type())
qtechMemoryPoolLowestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolLowestUtilization.setStatus(_A)
_QtechMemoryPoolLargestUtilization_Type=Percent
_QtechMemoryPoolLargestUtilization_Object=MibTableColumn
qtechMemoryPoolLargestUtilization=_QtechMemoryPoolLargestUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,5),_QtechMemoryPoolLargestUtilization_Type())
qtechMemoryPoolLargestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolLargestUtilization.setStatus(_A)
_QtechMemoryPoolSize_Type=Integer32
_QtechMemoryPoolSize_Object=MibTableColumn
qtechMemoryPoolSize=_QtechMemoryPoolSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,6),_QtechMemoryPoolSize_Type())
qtechMemoryPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolSize.setStatus(_A)
_QtechMemoryPoolUsed_Type=Integer32
_QtechMemoryPoolUsed_Object=MibTableColumn
qtechMemoryPoolUsed=_QtechMemoryPoolUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,7),_QtechMemoryPoolUsed_Type())
qtechMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolUsed.setStatus(_A)
_QtechMemoryPoolFree_Type=Integer32
_QtechMemoryPoolFree_Object=MibTableColumn
qtechMemoryPoolFree=_QtechMemoryPoolFree_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,8),_QtechMemoryPoolFree_Type())
qtechMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolFree.setStatus(_A)
_QtechMemoryPoolWarning_Type=Percent
_QtechMemoryPoolWarning_Object=MibTableColumn
qtechMemoryPoolWarning=_QtechMemoryPoolWarning_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,9),_QtechMemoryPoolWarning_Type())
qtechMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMemoryPoolWarning.setStatus(_A)
_QtechMemoryPoolCritical_Type=Percent
_QtechMemoryPoolCritical_Object=MibTableColumn
qtechMemoryPoolCritical=_QtechMemoryPoolCritical_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,10),_QtechMemoryPoolCritical_Type())
qtechMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMemoryPoolCritical.setStatus(_A)
_QtechMemoryPoolAverageUtilization_Type=Percent
_QtechMemoryPoolAverageUtilization_Object=MibTableColumn
qtechMemoryPoolAverageUtilization=_QtechMemoryPoolAverageUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,11),_QtechMemoryPoolAverageUtilization_Type())
qtechMemoryPoolAverageUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolAverageUtilization.setStatus(_A)
_QtechMemoryPoolTotalSize_Type=Gauge32
_QtechMemoryPoolTotalSize_Object=MibTableColumn
qtechMemoryPoolTotalSize=_QtechMemoryPoolTotalSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,12),_QtechMemoryPoolTotalSize_Type())
qtechMemoryPoolTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolTotalSize.setStatus(_A)
_QtechMemoryPoolUsedSize_Type=Gauge32
_QtechMemoryPoolUsedSize_Object=MibTableColumn
qtechMemoryPoolUsedSize=_QtechMemoryPoolUsedSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,13),_QtechMemoryPoolUsedSize_Type())
qtechMemoryPoolUsedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolUsedSize.setStatus(_A)
_QtechMemoryPoolFreeSize_Type=Gauge32
_QtechMemoryPoolFreeSize_Object=MibTableColumn
qtechMemoryPoolFreeSize=_QtechMemoryPoolFreeSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,1,1,14),_QtechMemoryPoolFreeSize_Type())
qtechMemoryPoolFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMemoryPoolFreeSize.setStatus(_A)
_QtechNodeMemoryPoolTable_Object=MibTable
qtechNodeMemoryPoolTable=_QtechNodeMemoryPoolTable_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2))
if mibBuilder.loadTexts:qtechNodeMemoryPoolTable.setStatus(_A)
_QtechNodeMemoryPoolEntry_Object=MibTableRow
qtechNodeMemoryPoolEntry=_QtechNodeMemoryPoolEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1))
qtechNodeMemoryPoolEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechNodeMemoryPoolEntry.setStatus(_A)
_QtechNodeMemoryPoolIndex_Type=Integer32
_QtechNodeMemoryPoolIndex_Object=MibTableColumn
qtechNodeMemoryPoolIndex=_QtechNodeMemoryPoolIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,1),_QtechNodeMemoryPoolIndex_Type())
qtechNodeMemoryPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolIndex.setStatus(_A)
_QtechNodeMemoryPoolName_Type=DisplayString
_QtechNodeMemoryPoolName_Object=MibTableColumn
qtechNodeMemoryPoolName=_QtechNodeMemoryPoolName_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,2),_QtechNodeMemoryPoolName_Type())
qtechNodeMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolName.setStatus(_A)
_QtechNodeMemoryPoolCurrentUtilization_Type=Percent
_QtechNodeMemoryPoolCurrentUtilization_Object=MibTableColumn
qtechNodeMemoryPoolCurrentUtilization=_QtechNodeMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,3),_QtechNodeMemoryPoolCurrentUtilization_Type())
qtechNodeMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolCurrentUtilization.setStatus(_A)
_QtechNodeMemoryPoolLowestUtilization_Type=Percent
_QtechNodeMemoryPoolLowestUtilization_Object=MibTableColumn
qtechNodeMemoryPoolLowestUtilization=_QtechNodeMemoryPoolLowestUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,4),_QtechNodeMemoryPoolLowestUtilization_Type())
qtechNodeMemoryPoolLowestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolLowestUtilization.setStatus(_A)
_QtechNodeMemoryPoolLargestUtilization_Type=Percent
_QtechNodeMemoryPoolLargestUtilization_Object=MibTableColumn
qtechNodeMemoryPoolLargestUtilization=_QtechNodeMemoryPoolLargestUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,5),_QtechNodeMemoryPoolLargestUtilization_Type())
qtechNodeMemoryPoolLargestUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolLargestUtilization.setStatus(_A)
_QtechNodeMemoryPoolSize_Type=Integer32
_QtechNodeMemoryPoolSize_Object=MibTableColumn
qtechNodeMemoryPoolSize=_QtechNodeMemoryPoolSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,6),_QtechNodeMemoryPoolSize_Type())
qtechNodeMemoryPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolSize.setStatus(_A)
_QtechNodeMemoryPoolUsed_Type=Integer32
_QtechNodeMemoryPoolUsed_Object=MibTableColumn
qtechNodeMemoryPoolUsed=_QtechNodeMemoryPoolUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,7),_QtechNodeMemoryPoolUsed_Type())
qtechNodeMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolUsed.setStatus(_A)
_QtechNodeMemoryPoolFree_Type=Integer32
_QtechNodeMemoryPoolFree_Object=MibTableColumn
qtechNodeMemoryPoolFree=_QtechNodeMemoryPoolFree_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,8),_QtechNodeMemoryPoolFree_Type())
qtechNodeMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolFree.setStatus(_A)
_QtechNodeMemoryPoolWarning_Type=Percent
_QtechNodeMemoryPoolWarning_Object=MibTableColumn
qtechNodeMemoryPoolWarning=_QtechNodeMemoryPoolWarning_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,9),_QtechNodeMemoryPoolWarning_Type())
qtechNodeMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechNodeMemoryPoolWarning.setStatus(_A)
_QtechNodeMemoryPoolCritical_Type=Percent
_QtechNodeMemoryPoolCritical_Object=MibTableColumn
qtechNodeMemoryPoolCritical=_QtechNodeMemoryPoolCritical_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,10),_QtechNodeMemoryPoolCritical_Type())
qtechNodeMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechNodeMemoryPoolCritical.setStatus(_A)
_QtechNodeMemoryPoolTotalSize_Type=Gauge32
_QtechNodeMemoryPoolTotalSize_Object=MibTableColumn
qtechNodeMemoryPoolTotalSize=_QtechNodeMemoryPoolTotalSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,11),_QtechNodeMemoryPoolTotalSize_Type())
qtechNodeMemoryPoolTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolTotalSize.setStatus(_A)
_QtechNodeMemoryPoolUsedSize_Type=Gauge32
_QtechNodeMemoryPoolUsedSize_Object=MibTableColumn
qtechNodeMemoryPoolUsedSize=_QtechNodeMemoryPoolUsedSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,12),_QtechNodeMemoryPoolUsedSize_Type())
qtechNodeMemoryPoolUsedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolUsedSize.setStatus(_A)
_QtechNodeMemoryPoolFreeSize_Type=Gauge32
_QtechNodeMemoryPoolFreeSize_Object=MibTableColumn
qtechNodeMemoryPoolFreeSize=_QtechNodeMemoryPoolFreeSize_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,2,1,13),_QtechNodeMemoryPoolFreeSize_Type())
qtechNodeMemoryPoolFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeMemoryPoolFreeSize.setStatus(_A)
_QtechLankApMemoryPoolTable_Object=MibTable
qtechLankApMemoryPoolTable=_QtechLankApMemoryPoolTable_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,3))
if mibBuilder.loadTexts:qtechLankApMemoryPoolTable.setStatus(_A)
_QtechLankApMemoryPoolEntry_Object=MibTableRow
qtechLankApMemoryPoolEntry=_QtechLankApMemoryPoolEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,3,1))
qtechLankApMemoryPoolEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechLankApMemoryPoolEntry.setStatus(_A)
_QtechLankApMemoryPoolMacAddr_Type=MacAddress
_QtechLankApMemoryPoolMacAddr_Object=MibTableColumn
qtechLankApMemoryPoolMacAddr=_QtechLankApMemoryPoolMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,3,1,1),_QtechLankApMemoryPoolMacAddr_Type())
qtechLankApMemoryPoolMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLankApMemoryPoolMacAddr.setStatus(_A)
_QtechLankApMemoryPoolWarning_Type=Percent
_QtechLankApMemoryPoolWarning_Object=MibTableColumn
qtechLankApMemoryPoolWarning=_QtechLankApMemoryPoolWarning_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,3,1,2),_QtechLankApMemoryPoolWarning_Type())
qtechLankApMemoryPoolWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLankApMemoryPoolWarning.setStatus(_A)
_QtechLankApMemoryPoolCritical_Type=Percent
_QtechLankApMemoryPoolCritical_Object=MibTableColumn
qtechLankApMemoryPoolCritical=_QtechLankApMemoryPoolCritical_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,3,1,3),_QtechLankApMemoryPoolCritical_Type())
qtechLankApMemoryPoolCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLankApMemoryPoolCritical.setStatus(_A)
_QtechLankApMemoryPoolCurrentUtilization_Type=Percent
_QtechLankApMemoryPoolCurrentUtilization_Object=MibTableColumn
qtechLankApMemoryPoolCurrentUtilization=_QtechLankApMemoryPoolCurrentUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,3,1,4),_QtechLankApMemoryPoolCurrentUtilization_Type())
qtechLankApMemoryPoolCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLankApMemoryPoolCurrentUtilization.setStatus(_A)
_QtechLankApMemoryPoolAverageUtilization_Type=Percent
_QtechLankApMemoryPoolAverageUtilization_Object=MibTableColumn
qtechLankApMemoryPoolAverageUtilization=_QtechLankApMemoryPoolAverageUtilization_Object((1,3,6,1,4,1,27514,1,1,10,2,35,1,3,1,5),_QtechLankApMemoryPoolAverageUtilization_Type())
qtechLankApMemoryPoolAverageUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLankApMemoryPoolAverageUtilization.setStatus(_A)
_QtechMemoryMIBConformance_ObjectIdentity=ObjectIdentity
qtechMemoryMIBConformance=_QtechMemoryMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,35,2))
_QtechMemoryMIBCompliances_ObjectIdentity=ObjectIdentity
qtechMemoryMIBCompliances=_QtechMemoryMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,35,2,1))
_QtechMemoryMIBGroups_ObjectIdentity=ObjectIdentity
qtechMemoryMIBGroups=_QtechMemoryMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,35,2,2))
qtechMemoryPoolUtilizationMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,35,2,2,1))
qtechMemoryPoolUtilizationMIBGroup.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:qtechMemoryPoolUtilizationMIBGroup.setStatus(_A)
qtechNodeMemoryPoolMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,35,2,2,2))
qtechNodeMemoryPoolMIBGroup.setObjects(*((_B,_F),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:qtechNodeMemoryPoolMIBGroup.setStatus(_A)
qtechMemoryMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,35,2,1,1))
qtechMemoryMIBCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:qtechMemoryMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Percent':Percent,'qtechMemoryMIB':qtechMemoryMIB,'qtechMemoryPoolMIBObjects':qtechMemoryPoolMIBObjects,'qtechMemoryPoolUtilizationTable':qtechMemoryPoolUtilizationTable,'qtechMemoryPoolUtilizationEntry':qtechMemoryPoolUtilizationEntry,_E:qtechMemoryPoolIndex,_H:qtechMemoryPoolName,_I:qtechMemoryPoolCurrentUtilization,_J:qtechMemoryPoolLowestUtilization,_K:qtechMemoryPoolLargestUtilization,_L:qtechMemoryPoolSize,_M:qtechMemoryPoolUsed,_N:qtechMemoryPoolFree,_O:qtechMemoryPoolWarning,_P:qtechMemoryPoolCritical,_Q:qtechMemoryPoolAverageUtilization,_R:qtechMemoryPoolTotalSize,_S:qtechMemoryPoolUsedSize,_T:qtechMemoryPoolFreeSize,'qtechNodeMemoryPoolTable':qtechNodeMemoryPoolTable,'qtechNodeMemoryPoolEntry':qtechNodeMemoryPoolEntry,_F:qtechNodeMemoryPoolIndex,_U:qtechNodeMemoryPoolName,_V:qtechNodeMemoryPoolCurrentUtilization,_W:qtechNodeMemoryPoolLowestUtilization,_X:qtechNodeMemoryPoolLargestUtilization,_Y:qtechNodeMemoryPoolSize,_Z:qtechNodeMemoryPoolUsed,_a:qtechNodeMemoryPoolFree,_b:qtechNodeMemoryPoolWarning,_c:qtechNodeMemoryPoolCritical,_d:qtechNodeMemoryPoolTotalSize,_e:qtechNodeMemoryPoolUsedSize,_f:qtechNodeMemoryPoolFreeSize,'qtechLankApMemoryPoolTable':qtechLankApMemoryPoolTable,'qtechLankApMemoryPoolEntry':qtechLankApMemoryPoolEntry,_G:qtechLankApMemoryPoolMacAddr,'qtechLankApMemoryPoolWarning':qtechLankApMemoryPoolWarning,'qtechLankApMemoryPoolCritical':qtechLankApMemoryPoolCritical,'qtechLankApMemoryPoolCurrentUtilization':qtechLankApMemoryPoolCurrentUtilization,'qtechLankApMemoryPoolAverageUtilization':qtechLankApMemoryPoolAverageUtilization,'qtechMemoryMIBConformance':qtechMemoryMIBConformance,'qtechMemoryMIBCompliances':qtechMemoryMIBCompliances,'qtechMemoryMIBCompliance':qtechMemoryMIBCompliance,'qtechMemoryMIBGroups':qtechMemoryMIBGroups,_g:qtechMemoryPoolUtilizationMIBGroup,'qtechNodeMemoryPoolMIBGroup':qtechNodeMemoryPoolMIBGroup})