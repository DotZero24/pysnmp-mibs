_Q='ctpcVsanTargetGroup'
_P='ctpcTargetAvgKbPerSec'
_O='ctpcTargetMaxXcopy'
_N='ctpcTargetMinXcopy'
_M='ctpcTargetNumXcopies'
_L='ctpcTargetState'
_K='ctpcTargetPortName'
_J='ctpcTargetNodeName'
_I='ctpcVsanRowStatus'
_H='Kilobytes'
_G='ctpcTargetIndex'
_F='vsanIndex'
_E='CISCO-VSAN-MIB'
_D='ctpcModuleId'
_C='read-only'
_B='CISCO-TPC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameIdOrZero,=mibBuilder.importSymbols('CISCO-ST-TC','FcNameIdOrZero')
vsanIndex,=mibBuilder.importSymbols(_E,_F)
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoTpcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,460))
if mibBuilder.loadTexts:ciscoTpcMIB.setRevisions(('2005-01-24 00:00',))
class TpcTargetState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('initializing',2),('error',3)))
_CiscoTpcNotification_ObjectIdentity=ObjectIdentity
ciscoTpcNotification=_CiscoTpcNotification_ObjectIdentity((1,3,6,1,4,1,9,9,460,0))
_CiscoTpcObjects_ObjectIdentity=ObjectIdentity
ciscoTpcObjects=_CiscoTpcObjects_ObjectIdentity((1,3,6,1,4,1,9,9,460,1))
_CiscoTpcConfig_ObjectIdentity=ObjectIdentity
ciscoTpcConfig=_CiscoTpcConfig_ObjectIdentity((1,3,6,1,4,1,9,9,460,1,1))
_CtpcModuleTable_Object=MibTable
ctpcModuleTable=_CtpcModuleTable_Object((1,3,6,1,4,1,9,9,460,1,1,1))
if mibBuilder.loadTexts:ctpcModuleTable.setStatus(_A)
_CtpcModuleEntry_Object=MibTableRow
ctpcModuleEntry=_CtpcModuleEntry_Object((1,3,6,1,4,1,9,9,460,1,1,1,1))
ctpcModuleEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ctpcModuleEntry.setStatus(_A)
_CtpcModuleId_Type=PhysicalIndex
_CtpcModuleId_Object=MibTableColumn
ctpcModuleId=_CtpcModuleId_Object((1,3,6,1,4,1,9,9,460,1,1,1,1,1),_CtpcModuleId_Type())
ctpcModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcModuleId.setStatus(_A)
_CtpcVsanTable_Object=MibTable
ctpcVsanTable=_CtpcVsanTable_Object((1,3,6,1,4,1,9,9,460,1,1,2))
if mibBuilder.loadTexts:ctpcVsanTable.setStatus(_A)
_CtpcVsanEntry_Object=MibTableRow
ctpcVsanEntry=_CtpcVsanEntry_Object((1,3,6,1,4,1,9,9,460,1,1,2,1))
ctpcVsanEntry.setIndexNames((0,_B,_D),(0,_E,_F))
if mibBuilder.loadTexts:ctpcVsanEntry.setStatus(_A)
_CtpcVsanRowStatus_Type=RowStatus
_CtpcVsanRowStatus_Object=MibTableColumn
ctpcVsanRowStatus=_CtpcVsanRowStatus_Object((1,3,6,1,4,1,9,9,460,1,1,2,1,1),_CtpcVsanRowStatus_Type())
ctpcVsanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:ctpcVsanRowStatus.setStatus(_A)
_CtpcTargetTable_Object=MibTable
ctpcTargetTable=_CtpcTargetTable_Object((1,3,6,1,4,1,9,9,460,1,1,3))
if mibBuilder.loadTexts:ctpcTargetTable.setStatus(_A)
_CtpcTargetEntry_Object=MibTableRow
ctpcTargetEntry=_CtpcTargetEntry_Object((1,3,6,1,4,1,9,9,460,1,1,3,1))
ctpcTargetEntry.setIndexNames((0,_B,_D),(0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:ctpcTargetEntry.setStatus(_A)
_CtpcTargetIndex_Type=Unsigned32
_CtpcTargetIndex_Object=MibTableColumn
ctpcTargetIndex=_CtpcTargetIndex_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,1),_CtpcTargetIndex_Type())
ctpcTargetIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ctpcTargetIndex.setStatus(_A)
_CtpcTargetNodeName_Type=FcNameIdOrZero
_CtpcTargetNodeName_Object=MibTableColumn
ctpcTargetNodeName=_CtpcTargetNodeName_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,2),_CtpcTargetNodeName_Type())
ctpcTargetNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTargetNodeName.setStatus(_A)
_CtpcTargetPortName_Type=FcNameIdOrZero
_CtpcTargetPortName_Object=MibTableColumn
ctpcTargetPortName=_CtpcTargetPortName_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,3),_CtpcTargetPortName_Type())
ctpcTargetPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTargetPortName.setStatus(_A)
_CtpcTargetState_Type=TpcTargetState
_CtpcTargetState_Object=MibTableColumn
ctpcTargetState=_CtpcTargetState_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,4),_CtpcTargetState_Type())
ctpcTargetState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTargetState.setStatus(_A)
_CtpcTargetNumXcopies_Type=Counter32
_CtpcTargetNumXcopies_Object=MibTableColumn
ctpcTargetNumXcopies=_CtpcTargetNumXcopies_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,5),_CtpcTargetNumXcopies_Type())
ctpcTargetNumXcopies.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTargetNumXcopies.setStatus(_A)
if mibBuilder.loadTexts:ctpcTargetNumXcopies.setUnits('commands')
_CtpcTargetMinXcopy_Type=Gauge32
_CtpcTargetMinXcopy_Object=MibTableColumn
ctpcTargetMinXcopy=_CtpcTargetMinXcopy_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,6),_CtpcTargetMinXcopy_Type())
ctpcTargetMinXcopy.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTargetMinXcopy.setStatus(_A)
if mibBuilder.loadTexts:ctpcTargetMinXcopy.setUnits(_H)
_CtpcTargetMaxXcopy_Type=Gauge32
_CtpcTargetMaxXcopy_Object=MibTableColumn
ctpcTargetMaxXcopy=_CtpcTargetMaxXcopy_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,7),_CtpcTargetMaxXcopy_Type())
ctpcTargetMaxXcopy.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTargetMaxXcopy.setStatus(_A)
if mibBuilder.loadTexts:ctpcTargetMaxXcopy.setUnits(_H)
_CtpcTargetAvgKbPerSec_Type=Gauge32
_CtpcTargetAvgKbPerSec_Object=MibTableColumn
ctpcTargetAvgKbPerSec=_CtpcTargetAvgKbPerSec_Object((1,3,6,1,4,1,9,9,460,1,1,3,1,8),_CtpcTargetAvgKbPerSec_Type())
ctpcTargetAvgKbPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:ctpcTargetAvgKbPerSec.setStatus(_A)
if mibBuilder.loadTexts:ctpcTargetAvgKbPerSec.setUnits('Kilobytes/second')
_CiscoTpcMIBConformance_ObjectIdentity=ObjectIdentity
ciscoTpcMIBConformance=_CiscoTpcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,460,2))
_CtpcMIBCompliances_ObjectIdentity=ObjectIdentity
ctpcMIBCompliances=_CtpcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,460,2,1))
_CtpcMIBGroups_ObjectIdentity=ObjectIdentity
ctpcMIBGroups=_CtpcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,460,2,2))
ctpcVsanTargetGroup=ObjectGroup((1,3,6,1,4,1,9,9,460,2,2,1))
ctpcVsanTargetGroup.setObjects(*((_B,_D),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ctpcVsanTargetGroup.setStatus(_A)
ctpcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,460,2,1,1))
ctpcMIBCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:ctpcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TpcTargetState':TpcTargetState,'ciscoTpcMIB':ciscoTpcMIB,'ciscoTpcNotification':ciscoTpcNotification,'ciscoTpcObjects':ciscoTpcObjects,'ciscoTpcConfig':ciscoTpcConfig,'ctpcModuleTable':ctpcModuleTable,'ctpcModuleEntry':ctpcModuleEntry,_D:ctpcModuleId,'ctpcVsanTable':ctpcVsanTable,'ctpcVsanEntry':ctpcVsanEntry,_I:ctpcVsanRowStatus,'ctpcTargetTable':ctpcTargetTable,'ctpcTargetEntry':ctpcTargetEntry,_G:ctpcTargetIndex,_J:ctpcTargetNodeName,_K:ctpcTargetPortName,_L:ctpcTargetState,_M:ctpcTargetNumXcopies,_N:ctpcTargetMinXcopy,_O:ctpcTargetMaxXcopy,_P:ctpcTargetAvgKbPerSec,'ciscoTpcMIBConformance':ciscoTpcMIBConformance,'ctpcMIBCompliances':ctpcMIBCompliances,'ctpcMIBCompliance':ctpcMIBCompliance,'ctpcMIBGroups':ctpcMIBGroups,_Q:ctpcVsanTargetGroup})