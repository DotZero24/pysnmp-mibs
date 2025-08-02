_U='fsCPUUtilizationMIBGroup'
_T='fsNodeCPUTotalCritical'
_S='fsNodeCPUTotalWarning'
_R='fsNodeCPUTotal5min'
_Q='fsNodeCPUTotal1min'
_P='fsNodeCPUTotal5sec'
_O='fsNodeCPUTotalName'
_N='fsCPUUtilizationCurrent'
_M='fsCPUUtilizationCollectSwitch'
_L='fsCPUMaxUtilization5Min'
_K='fsCPUMaxUtilization1Min'
_J='fsCPUMaxUtilization5Sec'
_I='fsCPUUtilization5Min'
_H='fsCPUUtilization1Min'
_G='fsCPUUtilization5Sec'
_F='fsLankApCPUMacAddr'
_E='fsNodeCPUTotalIndex'
_D='read-write'
_C='read-only'
_B='FS-PROCESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsProcessMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,36))
if mibBuilder.loadTexts:fsProcessMIB.setRevisions(('2003-10-14 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsCPUMIBObjects_ObjectIdentity=ObjectIdentity
fsCPUMIBObjects=_FsCPUMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,36,1))
_FsCpuGeneralMibsGroup_ObjectIdentity=ObjectIdentity
fsCpuGeneralMibsGroup=_FsCpuGeneralMibsGroup_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,36,1,1))
_FsCPUUtilization5Sec_Type=Percent
_FsCPUUtilization5Sec_Object=MibScalar
fsCPUUtilization5Sec=_FsCPUUtilization5Sec_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,1),_FsCPUUtilization5Sec_Type())
fsCPUUtilization5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCPUUtilization5Sec.setStatus(_A)
_FsCPUUtilization1Min_Type=Percent
_FsCPUUtilization1Min_Object=MibScalar
fsCPUUtilization1Min=_FsCPUUtilization1Min_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,2),_FsCPUUtilization1Min_Type())
fsCPUUtilization1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCPUUtilization1Min.setStatus(_A)
_FsCPUUtilization5Min_Type=Percent
_FsCPUUtilization5Min_Object=MibScalar
fsCPUUtilization5Min=_FsCPUUtilization5Min_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,3),_FsCPUUtilization5Min_Type())
fsCPUUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCPUUtilization5Min.setStatus(_A)
_FsCPUUtilizationWarning_Type=Percent
_FsCPUUtilizationWarning_Object=MibScalar
fsCPUUtilizationWarning=_FsCPUUtilizationWarning_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,4),_FsCPUUtilizationWarning_Type())
fsCPUUtilizationWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCPUUtilizationWarning.setStatus(_A)
_FsCPUUtilizationCritical_Type=Percent
_FsCPUUtilizationCritical_Object=MibScalar
fsCPUUtilizationCritical=_FsCPUUtilizationCritical_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,5),_FsCPUUtilizationCritical_Type())
fsCPUUtilizationCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCPUUtilizationCritical.setStatus(_A)
_FsCPUMaxUtilization5Sec_Type=Percent
_FsCPUMaxUtilization5Sec_Object=MibScalar
fsCPUMaxUtilization5Sec=_FsCPUMaxUtilization5Sec_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,6),_FsCPUMaxUtilization5Sec_Type())
fsCPUMaxUtilization5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCPUMaxUtilization5Sec.setStatus(_A)
_FsCPUMaxUtilization1Min_Type=Percent
_FsCPUMaxUtilization1Min_Object=MibScalar
fsCPUMaxUtilization1Min=_FsCPUMaxUtilization1Min_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,7),_FsCPUMaxUtilization1Min_Type())
fsCPUMaxUtilization1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCPUMaxUtilization1Min.setStatus(_A)
_FsCPUMaxUtilization5Min_Type=Percent
_FsCPUMaxUtilization5Min_Object=MibScalar
fsCPUMaxUtilization5Min=_FsCPUMaxUtilization5Min_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,8),_FsCPUMaxUtilization5Min_Type())
fsCPUMaxUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCPUMaxUtilization5Min.setStatus(_A)
_FsCPUUtilizationCollectSwitch_Type=Integer32
_FsCPUUtilizationCollectSwitch_Object=MibScalar
fsCPUUtilizationCollectSwitch=_FsCPUUtilizationCollectSwitch_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,9),_FsCPUUtilizationCollectSwitch_Type())
fsCPUUtilizationCollectSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCPUUtilizationCollectSwitch.setStatus(_A)
_FsCPUUtilizationCurrent_Type=Percent
_FsCPUUtilizationCurrent_Object=MibScalar
fsCPUUtilizationCurrent=_FsCPUUtilizationCurrent_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,1,10),_FsCPUUtilizationCurrent_Type())
fsCPUUtilizationCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCPUUtilizationCurrent.setStatus(_A)
_FsNodeCPUTotalTable_Object=MibTable
fsNodeCPUTotalTable=_FsNodeCPUTotalTable_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2))
if mibBuilder.loadTexts:fsNodeCPUTotalTable.setStatus(_A)
_FsNodeCPUTotalEntry_Object=MibTableRow
fsNodeCPUTotalEntry=_FsNodeCPUTotalEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1))
fsNodeCPUTotalEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsNodeCPUTotalEntry.setStatus(_A)
_FsNodeCPUTotalIndex_Type=Integer32
_FsNodeCPUTotalIndex_Object=MibTableColumn
fsNodeCPUTotalIndex=_FsNodeCPUTotalIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1,1),_FsNodeCPUTotalIndex_Type())
fsNodeCPUTotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeCPUTotalIndex.setStatus(_A)
_FsNodeCPUTotalName_Type=DisplayString
_FsNodeCPUTotalName_Object=MibTableColumn
fsNodeCPUTotalName=_FsNodeCPUTotalName_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1,2),_FsNodeCPUTotalName_Type())
fsNodeCPUTotalName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeCPUTotalName.setStatus(_A)
_FsNodeCPUTotal5sec_Type=Percent
_FsNodeCPUTotal5sec_Object=MibTableColumn
fsNodeCPUTotal5sec=_FsNodeCPUTotal5sec_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1,3),_FsNodeCPUTotal5sec_Type())
fsNodeCPUTotal5sec.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeCPUTotal5sec.setStatus(_A)
_FsNodeCPUTotal1min_Type=Percent
_FsNodeCPUTotal1min_Object=MibTableColumn
fsNodeCPUTotal1min=_FsNodeCPUTotal1min_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1,4),_FsNodeCPUTotal1min_Type())
fsNodeCPUTotal1min.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeCPUTotal1min.setStatus(_A)
_FsNodeCPUTotal5min_Type=Percent
_FsNodeCPUTotal5min_Object=MibTableColumn
fsNodeCPUTotal5min=_FsNodeCPUTotal5min_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1,5),_FsNodeCPUTotal5min_Type())
fsNodeCPUTotal5min.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNodeCPUTotal5min.setStatus(_A)
_FsNodeCPUTotalWarning_Type=Percent
_FsNodeCPUTotalWarning_Object=MibTableColumn
fsNodeCPUTotalWarning=_FsNodeCPUTotalWarning_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1,6),_FsNodeCPUTotalWarning_Type())
fsNodeCPUTotalWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:fsNodeCPUTotalWarning.setStatus(_A)
_FsNodeCPUTotalCritical_Type=Percent
_FsNodeCPUTotalCritical_Object=MibTableColumn
fsNodeCPUTotalCritical=_FsNodeCPUTotalCritical_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,2,1,7),_FsNodeCPUTotalCritical_Type())
fsNodeCPUTotalCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:fsNodeCPUTotalCritical.setStatus(_A)
_FsLankApCPUTotalTable_Object=MibTable
fsLankApCPUTotalTable=_FsLankApCPUTotalTable_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3))
if mibBuilder.loadTexts:fsLankApCPUTotalTable.setStatus(_A)
_FsLankApCPUTotalEntry_Object=MibTableRow
fsLankApCPUTotalEntry=_FsLankApCPUTotalEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3,1))
fsLankApCPUTotalEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsLankApCPUTotalEntry.setStatus(_A)
_FsLankApCPUMacAddr_Type=MacAddress
_FsLankApCPUMacAddr_Object=MibTableColumn
fsLankApCPUMacAddr=_FsLankApCPUMacAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3,1,1),_FsLankApCPUMacAddr_Type())
fsLankApCPUMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLankApCPUMacAddr.setStatus(_A)
_FsLankApCPUUtilizationCollectSwitch_Type=Integer32
_FsLankApCPUUtilizationCollectSwitch_Object=MibTableColumn
fsLankApCPUUtilizationCollectSwitch=_FsLankApCPUUtilizationCollectSwitch_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3,1,2),_FsLankApCPUUtilizationCollectSwitch_Type())
fsLankApCPUUtilizationCollectSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLankApCPUUtilizationCollectSwitch.setStatus(_A)
_FsLankApCPUUtilizationWarning_Type=Percent
_FsLankApCPUUtilizationWarning_Object=MibTableColumn
fsLankApCPUUtilizationWarning=_FsLankApCPUUtilizationWarning_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3,1,3),_FsLankApCPUUtilizationWarning_Type())
fsLankApCPUUtilizationWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLankApCPUUtilizationWarning.setStatus(_A)
_FsLankApCPUUtilizationCritical_Type=Percent
_FsLankApCPUUtilizationCritical_Object=MibTableColumn
fsLankApCPUUtilizationCritical=_FsLankApCPUUtilizationCritical_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3,1,4),_FsLankApCPUUtilizationCritical_Type())
fsLankApCPUUtilizationCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLankApCPUUtilizationCritical.setStatus(_A)
_FsLankApCPUUtilizationCurrent_Type=Percent
_FsLankApCPUUtilizationCurrent_Object=MibTableColumn
fsLankApCPUUtilizationCurrent=_FsLankApCPUUtilizationCurrent_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3,1,5),_FsLankApCPUUtilizationCurrent_Type())
fsLankApCPUUtilizationCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLankApCPUUtilizationCurrent.setStatus(_A)
_FsLankApCPUUtilization5Min_Type=Percent
_FsLankApCPUUtilization5Min_Object=MibTableColumn
fsLankApCPUUtilization5Min=_FsLankApCPUUtilization5Min_Object((1,3,6,1,4,1,52642,1,1,10,2,36,1,3,1,6),_FsLankApCPUUtilization5Min_Type())
fsLankApCPUUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLankApCPUUtilization5Min.setStatus(_A)
_FsProcessMIBConformance_ObjectIdentity=ObjectIdentity
fsProcessMIBConformance=_FsProcessMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,36,2))
_FsProcessMIBCompliances_ObjectIdentity=ObjectIdentity
fsProcessMIBCompliances=_FsProcessMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,36,2,1))
_FsProcessMIBGroups_ObjectIdentity=ObjectIdentity
fsProcessMIBGroups=_FsProcessMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,36,2,2))
fsCPUUtilizationMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,36,2,2,1))
fsCPUUtilizationMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fsCPUUtilizationMIBGroup.setStatus(_A)
fsNodeCPUTotalGroups=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,36,2,2,2))
fsNodeCPUTotalGroups.setObjects(*((_B,_E),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:fsNodeCPUTotalGroups.setStatus(_A)
fsProcessMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,36,2,1,1))
fsProcessMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:fsProcessMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Percent':Percent,'fsProcessMIB':fsProcessMIB,'fsCPUMIBObjects':fsCPUMIBObjects,'fsCpuGeneralMibsGroup':fsCpuGeneralMibsGroup,_G:fsCPUUtilization5Sec,_H:fsCPUUtilization1Min,_I:fsCPUUtilization5Min,'fsCPUUtilizationWarning':fsCPUUtilizationWarning,'fsCPUUtilizationCritical':fsCPUUtilizationCritical,_J:fsCPUMaxUtilization5Sec,_K:fsCPUMaxUtilization1Min,_L:fsCPUMaxUtilization5Min,_M:fsCPUUtilizationCollectSwitch,_N:fsCPUUtilizationCurrent,'fsNodeCPUTotalTable':fsNodeCPUTotalTable,'fsNodeCPUTotalEntry':fsNodeCPUTotalEntry,_E:fsNodeCPUTotalIndex,_O:fsNodeCPUTotalName,_P:fsNodeCPUTotal5sec,_Q:fsNodeCPUTotal1min,_R:fsNodeCPUTotal5min,_S:fsNodeCPUTotalWarning,_T:fsNodeCPUTotalCritical,'fsLankApCPUTotalTable':fsLankApCPUTotalTable,'fsLankApCPUTotalEntry':fsLankApCPUTotalEntry,_F:fsLankApCPUMacAddr,'fsLankApCPUUtilizationCollectSwitch':fsLankApCPUUtilizationCollectSwitch,'fsLankApCPUUtilizationWarning':fsLankApCPUUtilizationWarning,'fsLankApCPUUtilizationCritical':fsLankApCPUUtilizationCritical,'fsLankApCPUUtilizationCurrent':fsLankApCPUUtilizationCurrent,'fsLankApCPUUtilization5Min':fsLankApCPUUtilization5Min,'fsProcessMIBConformance':fsProcessMIBConformance,'fsProcessMIBCompliances':fsProcessMIBCompliances,'fsProcessMIBCompliance':fsProcessMIBCompliance,'fsProcessMIBGroups':fsProcessMIBGroups,_U:fsCPUUtilizationMIBGroup,'fsNodeCPUTotalGroups':fsNodeCPUTotalGroups})