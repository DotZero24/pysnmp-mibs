_N='dseGroup'
_M='dseCtrlLoopTimer'
_L='dseRowStatus'
_K='dseConvergenceStatus'
_J='dseEqualizationCtrlLoop'
_I='dseSpectrumTiltOffset'
_H='dseProvEqptType'
_G='dseMoId'
_F='read-write'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-DSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnConvergenceStatus,InfnEqptType,InfnEqualizationCtrlLoop=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnConvergenceStatus','InfnEqptType','InfnEqualizationCtrlLoop')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
dseMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,17))
_DseTable_Object=MibTable
dseTable=_DseTable_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1))
if mibBuilder.loadTexts:dseTable.setStatus(_A)
_DseEntry_Object=MibTableRow
dseEntry=_DseEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1))
dseEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dseEntry.setStatus(_A)
_DseMoId_Type=DisplayString
_DseMoId_Object=MibTableColumn
dseMoId=_DseMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1,1),_DseMoId_Type())
dseMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:dseMoId.setStatus(_A)
_DseProvEqptType_Type=InfnEqptType
_DseProvEqptType_Object=MibTableColumn
dseProvEqptType=_DseProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1,2),_DseProvEqptType_Type())
dseProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:dseProvEqptType.setStatus(_A)
_DseSpectrumTiltOffset_Type=FloatTenths
_DseSpectrumTiltOffset_Object=MibTableColumn
dseSpectrumTiltOffset=_DseSpectrumTiltOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1,3),_DseSpectrumTiltOffset_Type())
dseSpectrumTiltOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:dseSpectrumTiltOffset.setStatus(_A)
_DseEqualizationCtrlLoop_Type=InfnEqualizationCtrlLoop
_DseEqualizationCtrlLoop_Object=MibTableColumn
dseEqualizationCtrlLoop=_DseEqualizationCtrlLoop_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1,4),_DseEqualizationCtrlLoop_Type())
dseEqualizationCtrlLoop.setMaxAccess(_F)
if mibBuilder.loadTexts:dseEqualizationCtrlLoop.setStatus(_A)
_DseConvergenceStatus_Type=InfnConvergenceStatus
_DseConvergenceStatus_Object=MibTableColumn
dseConvergenceStatus=_DseConvergenceStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1,5),_DseConvergenceStatus_Type())
dseConvergenceStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:dseConvergenceStatus.setStatus(_A)
_DseRowStatus_Type=RowStatus
_DseRowStatus_Object=MibTableColumn
dseRowStatus=_DseRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1,6),_DseRowStatus_Type())
dseRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dseRowStatus.setStatus(_A)
_DseCtrlLoopTimer_Type=Integer32
_DseCtrlLoopTimer_Object=MibTableColumn
dseCtrlLoopTimer=_DseCtrlLoopTimer_Object((1,3,6,1,4,1,21296,2,2,2,1,17,1,1,7),_DseCtrlLoopTimer_Type())
dseCtrlLoopTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:dseCtrlLoopTimer.setStatus(_A)
_DseConformance_ObjectIdentity=ObjectIdentity
dseConformance=_DseConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,17,3))
_DseCompliances_ObjectIdentity=ObjectIdentity
dseCompliances=_DseCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,17,3,1))
_DseGroups_ObjectIdentity=ObjectIdentity
dseGroups=_DseGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,17,3,2))
dseGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,17,3,2,1))
dseGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:dseGroup.setStatus(_A)
dseCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,17,3,1,1))
dseCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:dseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dseMIB':dseMIB,'dseTable':dseTable,'dseEntry':dseEntry,_G:dseMoId,_H:dseProvEqptType,_I:dseSpectrumTiltOffset,_J:dseEqualizationCtrlLoop,_K:dseConvergenceStatus,_L:dseRowStatus,_M:dseCtrlLoopTimer,'dseConformance':dseConformance,'dseCompliances':dseCompliances,'dseCompliance':dseCompliance,'dseGroups':dseGroups,_N:dseGroup})