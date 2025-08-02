_R='bdcomMemoryPoolUtilizationGroup'
_Q='bdcomMemoryPoolUtilization10Min'
_P='bdcomMemoryPoolUtilization5Min'
_O='bdcomMemoryPoolUtilization1Min'
_N='bdcomMemoryPoolLargestFree'
_M='bdcomMemoryPoolFree'
_L='bdcomMemoryPoolUsed'
_K='bdcomMemoryPoolValid'
_J='bdcomMemoryPoolAlternate'
_I='bdcomMemoryPoolName'
_H='bdcomMemoryPoolUtilizationEntry'
_G='bdcomMemoryPoolType'
_F='Integer32'
_E='bdcomMemoryPoolGroup'
_D='bytes'
_C='read-only'
_B='BDCOM-MEMORY-POOL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percent,=mibBuilder.importSymbols('BDCOM-QOS-PIB-MIB','Percent')
bdMgmt,=mibBuilder.importSymbols('BDCOM-SMI','bdMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
bdcomMemoryPoolMIB=ModuleIdentity((1,3,6,1,4,1,3320,9,48))
if mibBuilder.loadTexts:bdcomMemoryPoolMIB.setRevisions(('2003-10-16 00:00',))
class BDCOMMemoryPoolTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BdcomMemoryPoolObjects_ObjectIdentity=ObjectIdentity
bdcomMemoryPoolObjects=_BdcomMemoryPoolObjects_ObjectIdentity((1,3,6,1,4,1,3320,9,48,1))
_BdcomMemoryPoolTable_Object=MibTable
bdcomMemoryPoolTable=_BdcomMemoryPoolTable_Object((1,3,6,1,4,1,3320,9,48,1,1))
if mibBuilder.loadTexts:bdcomMemoryPoolTable.setStatus(_A)
_BdcomMemoryPoolEntry_Object=MibTableRow
bdcomMemoryPoolEntry=_BdcomMemoryPoolEntry_Object((1,3,6,1,4,1,3320,9,48,1,1,1))
bdcomMemoryPoolEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:bdcomMemoryPoolEntry.setStatus(_A)
_BdcomMemoryPoolType_Type=BDCOMMemoryPoolTypes
_BdcomMemoryPoolType_Object=MibTableColumn
bdcomMemoryPoolType=_BdcomMemoryPoolType_Object((1,3,6,1,4,1,3320,9,48,1,1,1,1),_BdcomMemoryPoolType_Type())
bdcomMemoryPoolType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bdcomMemoryPoolType.setStatus(_A)
_BdcomMemoryPoolName_Type=DisplayString
_BdcomMemoryPoolName_Object=MibTableColumn
bdcomMemoryPoolName=_BdcomMemoryPoolName_Object((1,3,6,1,4,1,3320,9,48,1,1,1,2),_BdcomMemoryPoolName_Type())
bdcomMemoryPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolName.setStatus(_A)
class _BdcomMemoryPoolAlternate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BdcomMemoryPoolAlternate_Type.__name__=_F
_BdcomMemoryPoolAlternate_Object=MibTableColumn
bdcomMemoryPoolAlternate=_BdcomMemoryPoolAlternate_Object((1,3,6,1,4,1,3320,9,48,1,1,1,3),_BdcomMemoryPoolAlternate_Type())
bdcomMemoryPoolAlternate.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolAlternate.setStatus(_A)
_BdcomMemoryPoolValid_Type=TruthValue
_BdcomMemoryPoolValid_Object=MibTableColumn
bdcomMemoryPoolValid=_BdcomMemoryPoolValid_Object((1,3,6,1,4,1,3320,9,48,1,1,1,4),_BdcomMemoryPoolValid_Type())
bdcomMemoryPoolValid.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolValid.setStatus(_A)
_BdcomMemoryPoolUsed_Type=Gauge32
_BdcomMemoryPoolUsed_Object=MibTableColumn
bdcomMemoryPoolUsed=_BdcomMemoryPoolUsed_Object((1,3,6,1,4,1,3320,9,48,1,1,1,5),_BdcomMemoryPoolUsed_Type())
bdcomMemoryPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolUsed.setStatus(_A)
if mibBuilder.loadTexts:bdcomMemoryPoolUsed.setUnits(_D)
_BdcomMemoryPoolFree_Type=Gauge32
_BdcomMemoryPoolFree_Object=MibTableColumn
bdcomMemoryPoolFree=_BdcomMemoryPoolFree_Object((1,3,6,1,4,1,3320,9,48,1,1,1,6),_BdcomMemoryPoolFree_Type())
bdcomMemoryPoolFree.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolFree.setStatus(_A)
if mibBuilder.loadTexts:bdcomMemoryPoolFree.setUnits(_D)
_BdcomMemoryPoolLargestFree_Type=Gauge32
_BdcomMemoryPoolLargestFree_Object=MibTableColumn
bdcomMemoryPoolLargestFree=_BdcomMemoryPoolLargestFree_Object((1,3,6,1,4,1,3320,9,48,1,1,1,7),_BdcomMemoryPoolLargestFree_Type())
bdcomMemoryPoolLargestFree.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolLargestFree.setStatus(_A)
if mibBuilder.loadTexts:bdcomMemoryPoolLargestFree.setUnits(_D)
_BdcomMemoryPoolUtilizationTable_Object=MibTable
bdcomMemoryPoolUtilizationTable=_BdcomMemoryPoolUtilizationTable_Object((1,3,6,1,4,1,3320,9,48,1,2))
if mibBuilder.loadTexts:bdcomMemoryPoolUtilizationTable.setStatus(_A)
_BdcomMemoryPoolUtilizationEntry_Object=MibTableRow
bdcomMemoryPoolUtilizationEntry=_BdcomMemoryPoolUtilizationEntry_Object((1,3,6,1,4,1,3320,9,48,1,2,1))
if mibBuilder.loadTexts:bdcomMemoryPoolUtilizationEntry.setStatus(_A)
_BdcomMemoryPoolUtilization1Min_Type=Percent
_BdcomMemoryPoolUtilization1Min_Object=MibTableColumn
bdcomMemoryPoolUtilization1Min=_BdcomMemoryPoolUtilization1Min_Object((1,3,6,1,4,1,3320,9,48,1,2,1,1),_BdcomMemoryPoolUtilization1Min_Type())
bdcomMemoryPoolUtilization1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolUtilization1Min.setStatus(_A)
_BdcomMemoryPoolUtilization5Min_Type=Percent
_BdcomMemoryPoolUtilization5Min_Object=MibTableColumn
bdcomMemoryPoolUtilization5Min=_BdcomMemoryPoolUtilization5Min_Object((1,3,6,1,4,1,3320,9,48,1,2,1,2),_BdcomMemoryPoolUtilization5Min_Type())
bdcomMemoryPoolUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolUtilization5Min.setStatus(_A)
_BdcomMemoryPoolUtilization10Min_Type=Percent
_BdcomMemoryPoolUtilization10Min_Object=MibTableColumn
bdcomMemoryPoolUtilization10Min=_BdcomMemoryPoolUtilization10Min_Object((1,3,6,1,4,1,3320,9,48,1,2,1,3),_BdcomMemoryPoolUtilization10Min_Type())
bdcomMemoryPoolUtilization10Min.setMaxAccess(_C)
if mibBuilder.loadTexts:bdcomMemoryPoolUtilization10Min.setStatus(_A)
_BdcomMemoryPoolNotifications_ObjectIdentity=ObjectIdentity
bdcomMemoryPoolNotifications=_BdcomMemoryPoolNotifications_ObjectIdentity((1,3,6,1,4,1,3320,9,48,2))
_BdcomMemoryPoolConformance_ObjectIdentity=ObjectIdentity
bdcomMemoryPoolConformance=_BdcomMemoryPoolConformance_ObjectIdentity((1,3,6,1,4,1,3320,9,48,3))
_BdcomMemoryPoolCompliances_ObjectIdentity=ObjectIdentity
bdcomMemoryPoolCompliances=_BdcomMemoryPoolCompliances_ObjectIdentity((1,3,6,1,4,1,3320,9,48,3,1))
_BdcomMemoryPoolGroups_ObjectIdentity=ObjectIdentity
bdcomMemoryPoolGroups=_BdcomMemoryPoolGroups_ObjectIdentity((1,3,6,1,4,1,3320,9,48,3,2))
bdcomMemoryPoolEntry.registerAugmentions((_B,_H))
bdcomMemoryPoolUtilizationEntry.setIndexNames(*bdcomMemoryPoolEntry.getIndexNames())
bdcomMemoryPoolGroup=ObjectGroup((1,3,6,1,4,1,3320,9,48,3,2,1))
bdcomMemoryPoolGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:bdcomMemoryPoolGroup.setStatus(_A)
bdcomMemoryPoolUtilizationGroup=ObjectGroup((1,3,6,1,4,1,3320,9,48,3,2,2))
bdcomMemoryPoolUtilizationGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:bdcomMemoryPoolUtilizationGroup.setStatus(_A)
bdcomMemoryPoolCompliance=ModuleCompliance((1,3,6,1,4,1,3320,9,48,3,1,1))
bdcomMemoryPoolCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:bdcomMemoryPoolCompliance.setStatus('deprecated')
bdcomMemoryPoolComplianceRev1=ModuleCompliance((1,3,6,1,4,1,3320,9,48,3,1,2))
bdcomMemoryPoolComplianceRev1.setObjects(*((_B,_E),(_B,_R)))
if mibBuilder.loadTexts:bdcomMemoryPoolComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BDCOMMemoryPoolTypes':BDCOMMemoryPoolTypes,'bdcomMemoryPoolMIB':bdcomMemoryPoolMIB,'bdcomMemoryPoolObjects':bdcomMemoryPoolObjects,'bdcomMemoryPoolTable':bdcomMemoryPoolTable,'bdcomMemoryPoolEntry':bdcomMemoryPoolEntry,_G:bdcomMemoryPoolType,_I:bdcomMemoryPoolName,_J:bdcomMemoryPoolAlternate,_K:bdcomMemoryPoolValid,_L:bdcomMemoryPoolUsed,_M:bdcomMemoryPoolFree,_N:bdcomMemoryPoolLargestFree,'bdcomMemoryPoolUtilizationTable':bdcomMemoryPoolUtilizationTable,_H:bdcomMemoryPoolUtilizationEntry,_O:bdcomMemoryPoolUtilization1Min,_P:bdcomMemoryPoolUtilization5Min,_Q:bdcomMemoryPoolUtilization10Min,'bdcomMemoryPoolNotifications':bdcomMemoryPoolNotifications,'bdcomMemoryPoolConformance':bdcomMemoryPoolConformance,'bdcomMemoryPoolCompliances':bdcomMemoryPoolCompliances,'bdcomMemoryPoolCompliance':bdcomMemoryPoolCompliance,'bdcomMemoryPoolComplianceRev1':bdcomMemoryPoolComplianceRev1,'bdcomMemoryPoolGroups':bdcomMemoryPoolGroups,_E:bdcomMemoryPoolGroup,_R:bdcomMemoryPoolUtilizationGroup})