_O='myCPUUtilizationMIBGroup'
_N='myNodeCPUTotalCritical'
_M='myNodeCPUTotalWarning'
_L='myNodeCPUTotal5min'
_K='myNodeCPUTotal1min'
_J='myNodeCPUTotal5sec'
_I='myNodeCPUTotalName'
_H='myCPUUtilization5Min'
_G='myCPUUtilization1Min'
_F='myCPUUtilization5Sec'
_E='myNodeCPUTotalIndex'
_D='read-write'
_C='read-only'
_B='DES7200-PROCESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
myProcessMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,36))
if mibBuilder.loadTexts:myProcessMIB.setRevisions(('2003-10-14 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MyCPUMIBObjects_ObjectIdentity=ObjectIdentity
myCPUMIBObjects=_MyCPUMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,36,1))
_MyCpuGeneralMibsGroup_ObjectIdentity=ObjectIdentity
myCpuGeneralMibsGroup=_MyCpuGeneralMibsGroup_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,36,1,1))
_MyCPUUtilization5Sec_Type=Percent
_MyCPUUtilization5Sec_Object=MibScalar
myCPUUtilization5Sec=_MyCPUUtilization5Sec_Object((1,3,6,1,4,1,171,10,97,2,36,1,1,1),_MyCPUUtilization5Sec_Type())
myCPUUtilization5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:myCPUUtilization5Sec.setStatus(_A)
_MyCPUUtilization1Min_Type=Percent
_MyCPUUtilization1Min_Object=MibScalar
myCPUUtilization1Min=_MyCPUUtilization1Min_Object((1,3,6,1,4,1,171,10,97,2,36,1,1,2),_MyCPUUtilization1Min_Type())
myCPUUtilization1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:myCPUUtilization1Min.setStatus(_A)
_MyCPUUtilization5Min_Type=Percent
_MyCPUUtilization5Min_Object=MibScalar
myCPUUtilization5Min=_MyCPUUtilization5Min_Object((1,3,6,1,4,1,171,10,97,2,36,1,1,3),_MyCPUUtilization5Min_Type())
myCPUUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:myCPUUtilization5Min.setStatus(_A)
_MyCPUUtilizationWarning_Type=Percent
_MyCPUUtilizationWarning_Object=MibScalar
myCPUUtilizationWarning=_MyCPUUtilizationWarning_Object((1,3,6,1,4,1,171,10,97,2,36,1,1,4),_MyCPUUtilizationWarning_Type())
myCPUUtilizationWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:myCPUUtilizationWarning.setStatus(_A)
_MyCPUUtilizationCritical_Type=Percent
_MyCPUUtilizationCritical_Object=MibScalar
myCPUUtilizationCritical=_MyCPUUtilizationCritical_Object((1,3,6,1,4,1,171,10,97,2,36,1,1,5),_MyCPUUtilizationCritical_Type())
myCPUUtilizationCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:myCPUUtilizationCritical.setStatus(_A)
_MyNodeCPUTotalTable_Object=MibTable
myNodeCPUTotalTable=_MyNodeCPUTotalTable_Object((1,3,6,1,4,1,171,10,97,2,36,1,2))
if mibBuilder.loadTexts:myNodeCPUTotalTable.setStatus(_A)
_MyNodeCPUTotalEntry_Object=MibTableRow
myNodeCPUTotalEntry=_MyNodeCPUTotalEntry_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1))
myNodeCPUTotalEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:myNodeCPUTotalEntry.setStatus(_A)
_MyNodeCPUTotalIndex_Type=Integer32
_MyNodeCPUTotalIndex_Object=MibTableColumn
myNodeCPUTotalIndex=_MyNodeCPUTotalIndex_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1,1),_MyNodeCPUTotalIndex_Type())
myNodeCPUTotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeCPUTotalIndex.setStatus(_A)
_MyNodeCPUTotalName_Type=DisplayString
_MyNodeCPUTotalName_Object=MibTableColumn
myNodeCPUTotalName=_MyNodeCPUTotalName_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1,2),_MyNodeCPUTotalName_Type())
myNodeCPUTotalName.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeCPUTotalName.setStatus(_A)
_MyNodeCPUTotal5sec_Type=Percent
_MyNodeCPUTotal5sec_Object=MibTableColumn
myNodeCPUTotal5sec=_MyNodeCPUTotal5sec_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1,3),_MyNodeCPUTotal5sec_Type())
myNodeCPUTotal5sec.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeCPUTotal5sec.setStatus(_A)
_MyNodeCPUTotal1min_Type=Percent
_MyNodeCPUTotal1min_Object=MibTableColumn
myNodeCPUTotal1min=_MyNodeCPUTotal1min_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1,4),_MyNodeCPUTotal1min_Type())
myNodeCPUTotal1min.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeCPUTotal1min.setStatus(_A)
_MyNodeCPUTotal5min_Type=Percent
_MyNodeCPUTotal5min_Object=MibTableColumn
myNodeCPUTotal5min=_MyNodeCPUTotal5min_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1,5),_MyNodeCPUTotal5min_Type())
myNodeCPUTotal5min.setMaxAccess(_C)
if mibBuilder.loadTexts:myNodeCPUTotal5min.setStatus(_A)
_MyNodeCPUTotalWarning_Type=Percent
_MyNodeCPUTotalWarning_Object=MibTableColumn
myNodeCPUTotalWarning=_MyNodeCPUTotalWarning_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1,6),_MyNodeCPUTotalWarning_Type())
myNodeCPUTotalWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:myNodeCPUTotalWarning.setStatus(_A)
_MyNodeCPUTotalCritical_Type=Percent
_MyNodeCPUTotalCritical_Object=MibTableColumn
myNodeCPUTotalCritical=_MyNodeCPUTotalCritical_Object((1,3,6,1,4,1,171,10,97,2,36,1,2,1,7),_MyNodeCPUTotalCritical_Type())
myNodeCPUTotalCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:myNodeCPUTotalCritical.setStatus(_A)
_MyProcessMIBConformance_ObjectIdentity=ObjectIdentity
myProcessMIBConformance=_MyProcessMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,36,2))
_MyProcessMIBCompliances_ObjectIdentity=ObjectIdentity
myProcessMIBCompliances=_MyProcessMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,36,2,1))
_MyProcessMIBGroups_ObjectIdentity=ObjectIdentity
myProcessMIBGroups=_MyProcessMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,36,2,2))
myCPUUtilizationMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,36,2,2,1))
myCPUUtilizationMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:myCPUUtilizationMIBGroup.setStatus(_A)
myNodeCPUTotalGroups=ObjectGroup((1,3,6,1,4,1,171,10,97,2,36,2,2,2))
myNodeCPUTotalGroups.setObjects(*((_B,_E),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:myNodeCPUTotalGroups.setStatus(_A)
myProcessMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,36,2,1,1))
myProcessMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:myProcessMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Percent':Percent,'myProcessMIB':myProcessMIB,'myCPUMIBObjects':myCPUMIBObjects,'myCpuGeneralMibsGroup':myCpuGeneralMibsGroup,_F:myCPUUtilization5Sec,_G:myCPUUtilization1Min,_H:myCPUUtilization5Min,'myCPUUtilizationWarning':myCPUUtilizationWarning,'myCPUUtilizationCritical':myCPUUtilizationCritical,'myNodeCPUTotalTable':myNodeCPUTotalTable,'myNodeCPUTotalEntry':myNodeCPUTotalEntry,_E:myNodeCPUTotalIndex,_I:myNodeCPUTotalName,_J:myNodeCPUTotal5sec,_K:myNodeCPUTotal1min,_L:myNodeCPUTotal5min,_M:myNodeCPUTotalWarning,_N:myNodeCPUTotalCritical,'myProcessMIBConformance':myProcessMIBConformance,'myProcessMIBCompliances':myProcessMIBCompliances,'myProcessMIBCompliance':myProcessMIBCompliance,'myProcessMIBGroups':myProcessMIBGroups,_O:myCPUUtilizationMIBGroup,'myNodeCPUTotalGroups':myNodeCPUTotalGroups})