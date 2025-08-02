_U='qtechCPUUtilizationMIBGroup'
_T='qtechNodeCPUTotalCritical'
_S='qtechNodeCPUTotalWarning'
_R='qtechNodeCPUTotal5min'
_Q='qtechNodeCPUTotal1min'
_P='qtechNodeCPUTotal5sec'
_O='qtechNodeCPUTotalName'
_N='qtechCPUUtilizationCurrent'
_M='qtechCPUUtilizationCollectSwitch'
_L='qtechCPUMaxUtilization5Min'
_K='qtechCPUMaxUtilization1Min'
_J='qtechCPUMaxUtilization5Sec'
_I='qtechCPUUtilization5Min'
_H='qtechCPUUtilization1Min'
_G='qtechCPUUtilization5Sec'
_F='qtechLankApCPUMacAddr'
_E='qtechNodeCPUTotalIndex'
_D='read-write'
_C='read-only'
_B='QTECH-PROCESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
qtechProcessMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,36))
if mibBuilder.loadTexts:qtechProcessMIB.setRevisions(('2003-10-14 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechCPUMIBObjects_ObjectIdentity=ObjectIdentity
qtechCPUMIBObjects=_QtechCPUMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,36,1))
_QtechCpuGeneralMibsGroup_ObjectIdentity=ObjectIdentity
qtechCpuGeneralMibsGroup=_QtechCpuGeneralMibsGroup_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,36,1,1))
_QtechCPUUtilization5Sec_Type=Percent
_QtechCPUUtilization5Sec_Object=MibScalar
qtechCPUUtilization5Sec=_QtechCPUUtilization5Sec_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,1),_QtechCPUUtilization5Sec_Type())
qtechCPUUtilization5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCPUUtilization5Sec.setStatus(_A)
_QtechCPUUtilization1Min_Type=Percent
_QtechCPUUtilization1Min_Object=MibScalar
qtechCPUUtilization1Min=_QtechCPUUtilization1Min_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,2),_QtechCPUUtilization1Min_Type())
qtechCPUUtilization1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCPUUtilization1Min.setStatus(_A)
_QtechCPUUtilization5Min_Type=Percent
_QtechCPUUtilization5Min_Object=MibScalar
qtechCPUUtilization5Min=_QtechCPUUtilization5Min_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,3),_QtechCPUUtilization5Min_Type())
qtechCPUUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCPUUtilization5Min.setStatus(_A)
_QtechCPUUtilizationWarning_Type=Percent
_QtechCPUUtilizationWarning_Object=MibScalar
qtechCPUUtilizationWarning=_QtechCPUUtilizationWarning_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,4),_QtechCPUUtilizationWarning_Type())
qtechCPUUtilizationWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCPUUtilizationWarning.setStatus(_A)
_QtechCPUUtilizationCritical_Type=Percent
_QtechCPUUtilizationCritical_Object=MibScalar
qtechCPUUtilizationCritical=_QtechCPUUtilizationCritical_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,5),_QtechCPUUtilizationCritical_Type())
qtechCPUUtilizationCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCPUUtilizationCritical.setStatus(_A)
_QtechCPUMaxUtilization5Sec_Type=Percent
_QtechCPUMaxUtilization5Sec_Object=MibScalar
qtechCPUMaxUtilization5Sec=_QtechCPUMaxUtilization5Sec_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,6),_QtechCPUMaxUtilization5Sec_Type())
qtechCPUMaxUtilization5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCPUMaxUtilization5Sec.setStatus(_A)
_QtechCPUMaxUtilization1Min_Type=Percent
_QtechCPUMaxUtilization1Min_Object=MibScalar
qtechCPUMaxUtilization1Min=_QtechCPUMaxUtilization1Min_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,7),_QtechCPUMaxUtilization1Min_Type())
qtechCPUMaxUtilization1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCPUMaxUtilization1Min.setStatus(_A)
_QtechCPUMaxUtilization5Min_Type=Percent
_QtechCPUMaxUtilization5Min_Object=MibScalar
qtechCPUMaxUtilization5Min=_QtechCPUMaxUtilization5Min_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,8),_QtechCPUMaxUtilization5Min_Type())
qtechCPUMaxUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCPUMaxUtilization5Min.setStatus(_A)
_QtechCPUUtilizationCollectSwitch_Type=Integer32
_QtechCPUUtilizationCollectSwitch_Object=MibScalar
qtechCPUUtilizationCollectSwitch=_QtechCPUUtilizationCollectSwitch_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,9),_QtechCPUUtilizationCollectSwitch_Type())
qtechCPUUtilizationCollectSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCPUUtilizationCollectSwitch.setStatus(_A)
_QtechCPUUtilizationCurrent_Type=Percent
_QtechCPUUtilizationCurrent_Object=MibScalar
qtechCPUUtilizationCurrent=_QtechCPUUtilizationCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,1,10),_QtechCPUUtilizationCurrent_Type())
qtechCPUUtilizationCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCPUUtilizationCurrent.setStatus(_A)
_QtechNodeCPUTotalTable_Object=MibTable
qtechNodeCPUTotalTable=_QtechNodeCPUTotalTable_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2))
if mibBuilder.loadTexts:qtechNodeCPUTotalTable.setStatus(_A)
_QtechNodeCPUTotalEntry_Object=MibTableRow
qtechNodeCPUTotalEntry=_QtechNodeCPUTotalEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1))
qtechNodeCPUTotalEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechNodeCPUTotalEntry.setStatus(_A)
_QtechNodeCPUTotalIndex_Type=Integer32
_QtechNodeCPUTotalIndex_Object=MibTableColumn
qtechNodeCPUTotalIndex=_QtechNodeCPUTotalIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1,1),_QtechNodeCPUTotalIndex_Type())
qtechNodeCPUTotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeCPUTotalIndex.setStatus(_A)
_QtechNodeCPUTotalName_Type=DisplayString
_QtechNodeCPUTotalName_Object=MibTableColumn
qtechNodeCPUTotalName=_QtechNodeCPUTotalName_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1,2),_QtechNodeCPUTotalName_Type())
qtechNodeCPUTotalName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeCPUTotalName.setStatus(_A)
_QtechNodeCPUTotal5sec_Type=Percent
_QtechNodeCPUTotal5sec_Object=MibTableColumn
qtechNodeCPUTotal5sec=_QtechNodeCPUTotal5sec_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1,3),_QtechNodeCPUTotal5sec_Type())
qtechNodeCPUTotal5sec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeCPUTotal5sec.setStatus(_A)
_QtechNodeCPUTotal1min_Type=Percent
_QtechNodeCPUTotal1min_Object=MibTableColumn
qtechNodeCPUTotal1min=_QtechNodeCPUTotal1min_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1,4),_QtechNodeCPUTotal1min_Type())
qtechNodeCPUTotal1min.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeCPUTotal1min.setStatus(_A)
_QtechNodeCPUTotal5min_Type=Percent
_QtechNodeCPUTotal5min_Object=MibTableColumn
qtechNodeCPUTotal5min=_QtechNodeCPUTotal5min_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1,5),_QtechNodeCPUTotal5min_Type())
qtechNodeCPUTotal5min.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNodeCPUTotal5min.setStatus(_A)
_QtechNodeCPUTotalWarning_Type=Percent
_QtechNodeCPUTotalWarning_Object=MibTableColumn
qtechNodeCPUTotalWarning=_QtechNodeCPUTotalWarning_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1,6),_QtechNodeCPUTotalWarning_Type())
qtechNodeCPUTotalWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechNodeCPUTotalWarning.setStatus(_A)
_QtechNodeCPUTotalCritical_Type=Percent
_QtechNodeCPUTotalCritical_Object=MibTableColumn
qtechNodeCPUTotalCritical=_QtechNodeCPUTotalCritical_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,2,1,7),_QtechNodeCPUTotalCritical_Type())
qtechNodeCPUTotalCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechNodeCPUTotalCritical.setStatus(_A)
_QtechLankApCPUTotalTable_Object=MibTable
qtechLankApCPUTotalTable=_QtechLankApCPUTotalTable_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3))
if mibBuilder.loadTexts:qtechLankApCPUTotalTable.setStatus(_A)
_QtechLankApCPUTotalEntry_Object=MibTableRow
qtechLankApCPUTotalEntry=_QtechLankApCPUTotalEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3,1))
qtechLankApCPUTotalEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechLankApCPUTotalEntry.setStatus(_A)
_QtechLankApCPUMacAddr_Type=MacAddress
_QtechLankApCPUMacAddr_Object=MibTableColumn
qtechLankApCPUMacAddr=_QtechLankApCPUMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3,1,1),_QtechLankApCPUMacAddr_Type())
qtechLankApCPUMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLankApCPUMacAddr.setStatus(_A)
_QtechLankApCPUUtilizationCollectSwitch_Type=Integer32
_QtechLankApCPUUtilizationCollectSwitch_Object=MibTableColumn
qtechLankApCPUUtilizationCollectSwitch=_QtechLankApCPUUtilizationCollectSwitch_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3,1,2),_QtechLankApCPUUtilizationCollectSwitch_Type())
qtechLankApCPUUtilizationCollectSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLankApCPUUtilizationCollectSwitch.setStatus(_A)
_QtechLankApCPUUtilizationWarning_Type=Percent
_QtechLankApCPUUtilizationWarning_Object=MibTableColumn
qtechLankApCPUUtilizationWarning=_QtechLankApCPUUtilizationWarning_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3,1,3),_QtechLankApCPUUtilizationWarning_Type())
qtechLankApCPUUtilizationWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLankApCPUUtilizationWarning.setStatus(_A)
_QtechLankApCPUUtilizationCritical_Type=Percent
_QtechLankApCPUUtilizationCritical_Object=MibTableColumn
qtechLankApCPUUtilizationCritical=_QtechLankApCPUUtilizationCritical_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3,1,4),_QtechLankApCPUUtilizationCritical_Type())
qtechLankApCPUUtilizationCritical.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLankApCPUUtilizationCritical.setStatus(_A)
_QtechLankApCPUUtilizationCurrent_Type=Percent
_QtechLankApCPUUtilizationCurrent_Object=MibTableColumn
qtechLankApCPUUtilizationCurrent=_QtechLankApCPUUtilizationCurrent_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3,1,5),_QtechLankApCPUUtilizationCurrent_Type())
qtechLankApCPUUtilizationCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLankApCPUUtilizationCurrent.setStatus(_A)
_QtechLankApCPUUtilization5Min_Type=Percent
_QtechLankApCPUUtilization5Min_Object=MibTableColumn
qtechLankApCPUUtilization5Min=_QtechLankApCPUUtilization5Min_Object((1,3,6,1,4,1,27514,1,1,10,2,36,1,3,1,6),_QtechLankApCPUUtilization5Min_Type())
qtechLankApCPUUtilization5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLankApCPUUtilization5Min.setStatus(_A)
_QtechProcessMIBConformance_ObjectIdentity=ObjectIdentity
qtechProcessMIBConformance=_QtechProcessMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,36,2))
_QtechProcessMIBCompliances_ObjectIdentity=ObjectIdentity
qtechProcessMIBCompliances=_QtechProcessMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,36,2,1))
_QtechProcessMIBGroups_ObjectIdentity=ObjectIdentity
qtechProcessMIBGroups=_QtechProcessMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,36,2,2))
qtechCPUUtilizationMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,36,2,2,1))
qtechCPUUtilizationMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:qtechCPUUtilizationMIBGroup.setStatus(_A)
qtechNodeCPUTotalGroups=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,36,2,2,2))
qtechNodeCPUTotalGroups.setObjects(*((_B,_E),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:qtechNodeCPUTotalGroups.setStatus(_A)
qtechProcessMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,36,2,1,1))
qtechProcessMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:qtechProcessMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Percent':Percent,'qtechProcessMIB':qtechProcessMIB,'qtechCPUMIBObjects':qtechCPUMIBObjects,'qtechCpuGeneralMibsGroup':qtechCpuGeneralMibsGroup,_G:qtechCPUUtilization5Sec,_H:qtechCPUUtilization1Min,_I:qtechCPUUtilization5Min,'qtechCPUUtilizationWarning':qtechCPUUtilizationWarning,'qtechCPUUtilizationCritical':qtechCPUUtilizationCritical,_J:qtechCPUMaxUtilization5Sec,_K:qtechCPUMaxUtilization1Min,_L:qtechCPUMaxUtilization5Min,_M:qtechCPUUtilizationCollectSwitch,_N:qtechCPUUtilizationCurrent,'qtechNodeCPUTotalTable':qtechNodeCPUTotalTable,'qtechNodeCPUTotalEntry':qtechNodeCPUTotalEntry,_E:qtechNodeCPUTotalIndex,_O:qtechNodeCPUTotalName,_P:qtechNodeCPUTotal5sec,_Q:qtechNodeCPUTotal1min,_R:qtechNodeCPUTotal5min,_S:qtechNodeCPUTotalWarning,_T:qtechNodeCPUTotalCritical,'qtechLankApCPUTotalTable':qtechLankApCPUTotalTable,'qtechLankApCPUTotalEntry':qtechLankApCPUTotalEntry,_F:qtechLankApCPUMacAddr,'qtechLankApCPUUtilizationCollectSwitch':qtechLankApCPUUtilizationCollectSwitch,'qtechLankApCPUUtilizationWarning':qtechLankApCPUUtilizationWarning,'qtechLankApCPUUtilizationCritical':qtechLankApCPUUtilizationCritical,'qtechLankApCPUUtilizationCurrent':qtechLankApCPUUtilizationCurrent,'qtechLankApCPUUtilization5Min':qtechLankApCPUUtilization5Min,'qtechProcessMIBConformance':qtechProcessMIBConformance,'qtechProcessMIBCompliances':qtechProcessMIBCompliances,'qtechProcessMIBCompliance':qtechProcessMIBCompliance,'qtechProcessMIBGroups':qtechProcessMIBGroups,_U:qtechCPUUtilizationMIBGroup,'qtechNodeCPUTotalGroups':qtechNodeCPUTotalGroups})