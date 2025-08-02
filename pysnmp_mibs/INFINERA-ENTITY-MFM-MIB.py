_O='mfmGroup'
_N='mfmASEIdlerMuxOprMode'
_M='mfmScheduledOPMScanGranularity'
_L='mfmScheduledOPMScanTime'
_K='mfmScheduledOPMScan'
_J='mfmOPMScanGranularity'
_I='mfmOPMSwitchSelector'
_H='mfmAssociatedDegree'
_G='mfmProvEqptType'
_F='mfmMoId'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='INFINERA-ENTITY-MFM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnASEIdlerMuxOprMode,InfnEnableDisableType,InfnEqptType,InfnOPMScanGranularity,InfnOPMSwitchPosition=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnASEIdlerMuxOprMode','InfnEnableDisableType','InfnEqptType','InfnOPMScanGranularity','InfnOPMSwitchPosition')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
mfmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,58))
_MfmTable_Object=MibTable
mfmTable=_MfmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1))
if mibBuilder.loadTexts:mfmTable.setStatus(_A)
_MfmEntry_Object=MibTableRow
mfmEntry=_MfmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1))
mfmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mfmEntry.setStatus(_A)
_MfmMoId_Type=DisplayString
_MfmMoId_Object=MibTableColumn
mfmMoId=_MfmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,1),_MfmMoId_Type())
mfmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmMoId.setStatus(_A)
_MfmProvEqptType_Type=InfnEqptType
_MfmProvEqptType_Object=MibTableColumn
mfmProvEqptType=_MfmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,2),_MfmProvEqptType_Type())
mfmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmProvEqptType.setStatus(_A)
_MfmAssociatedDegree_Type=DisplayString
_MfmAssociatedDegree_Object=MibTableColumn
mfmAssociatedDegree=_MfmAssociatedDegree_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,3),_MfmAssociatedDegree_Type())
mfmAssociatedDegree.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmAssociatedDegree.setStatus(_A)
_MfmOPMSwitchSelector_Type=InfnOPMSwitchPosition
_MfmOPMSwitchSelector_Object=MibTableColumn
mfmOPMSwitchSelector=_MfmOPMSwitchSelector_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,4),_MfmOPMSwitchSelector_Type())
mfmOPMSwitchSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmOPMSwitchSelector.setStatus(_A)
_MfmOPMScanGranularity_Type=InfnOPMScanGranularity
_MfmOPMScanGranularity_Object=MibTableColumn
mfmOPMScanGranularity=_MfmOPMScanGranularity_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,5),_MfmOPMScanGranularity_Type())
mfmOPMScanGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmOPMScanGranularity.setStatus(_A)
_MfmScheduledOPMScan_Type=InfnEnableDisableType
_MfmScheduledOPMScan_Object=MibTableColumn
mfmScheduledOPMScan=_MfmScheduledOPMScan_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,6),_MfmScheduledOPMScan_Type())
mfmScheduledOPMScan.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmScheduledOPMScan.setStatus(_A)
_MfmScheduledOPMScanTime_Type=Unsigned32
_MfmScheduledOPMScanTime_Object=MibTableColumn
mfmScheduledOPMScanTime=_MfmScheduledOPMScanTime_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,7),_MfmScheduledOPMScanTime_Type())
mfmScheduledOPMScanTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmScheduledOPMScanTime.setStatus(_A)
_MfmScheduledOPMScanGranularity_Type=InfnOPMScanGranularity
_MfmScheduledOPMScanGranularity_Object=MibTableColumn
mfmScheduledOPMScanGranularity=_MfmScheduledOPMScanGranularity_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,8),_MfmScheduledOPMScanGranularity_Type())
mfmScheduledOPMScanGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmScheduledOPMScanGranularity.setStatus(_A)
_MfmASEIdlerMuxOprMode_Type=InfnASEIdlerMuxOprMode
_MfmASEIdlerMuxOprMode_Object=MibTableColumn
mfmASEIdlerMuxOprMode=_MfmASEIdlerMuxOprMode_Object((1,3,6,1,4,1,21296,2,2,2,1,58,1,1,9),_MfmASEIdlerMuxOprMode_Type())
mfmASEIdlerMuxOprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mfmASEIdlerMuxOprMode.setStatus(_A)
_MfmConformance_ObjectIdentity=ObjectIdentity
mfmConformance=_MfmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,58,3))
_MfmCompliances_ObjectIdentity=ObjectIdentity
mfmCompliances=_MfmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,58,3,1))
_MfmGroups_ObjectIdentity=ObjectIdentity
mfmGroups=_MfmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,58,3,2))
mfmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,58,3,2,1))
mfmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mfmGroup.setStatus(_A)
mfmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,58,3,1,1))
mfmCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:mfmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mfmMIB':mfmMIB,'mfmTable':mfmTable,'mfmEntry':mfmEntry,_F:mfmMoId,_G:mfmProvEqptType,_H:mfmAssociatedDegree,_I:mfmOPMSwitchSelector,_J:mfmOPMScanGranularity,_K:mfmScheduledOPMScan,_L:mfmScheduledOPMScanTime,_M:mfmScheduledOPMScanGranularity,_N:mfmASEIdlerMuxOprMode,'mfmConformance':mfmConformance,'mfmCompliances':mfmCompliances,'mfmCompliance':mfmCompliance,'mfmGroups':mfmGroups,_O:mfmGroup})