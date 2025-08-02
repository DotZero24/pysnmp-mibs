_O='rlEnvRedundantFanIndex'
_N='rlEnvRedundantFanUnitId'
_M='rlEnvFanDataStackUnit'
_L='rlEnvMonIndexObjIndex'
_K='rlEnvMonIndexObjType'
_J='rlEnvMonIndexUnitId'
_I='rlEnvMonSupplyStatusIndex'
_H='rlEnvMonFanStatusIndex'
_G='notPresent'
_F='DisplayString'
_E='Integer32'
_D='not-accessible'
_C='RADLAN-HWENVIROMENT'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TruthValue')
rlEnv=ModuleIdentity((1,3,6,1,4,1,89,83))
if mibBuilder.loadTexts:rlEnv.setRevisions(('2003-09-21 00:00',))
class RlEnvMonState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('normal',1),('warning',2),('critical',3),('shutdown',4),(_G,5),('notFunctioning',6),('restore',7),('notAvailable',8),('backingUp',9)))
class RlEnvMonDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unKnown',1),('frontToBack',2),('backToFront',3),('clockwise',4),('unClockwise',5),('insideOut',6),('outsideIn',7),('rightToLeft',8),('leftToRight',9)))
class RlEnvRedundantFanStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ready',1),('active',2),('failure',3),(_G,4)))
_RlEnvPhysicalDescription_ObjectIdentity=ObjectIdentity
rlEnvPhysicalDescription=_RlEnvPhysicalDescription_ObjectIdentity((1,3,6,1,4,1,89,83,1))
_RlEnvMonFanStatusTable_Object=MibTable
rlEnvMonFanStatusTable=_RlEnvMonFanStatusTable_Object((1,3,6,1,4,1,89,83,1,1))
if mibBuilder.loadTexts:rlEnvMonFanStatusTable.setStatus(_A)
_RlEnvMonFanStatusEntry_Object=MibTableRow
rlEnvMonFanStatusEntry=_RlEnvMonFanStatusEntry_Object((1,3,6,1,4,1,89,83,1,1,1))
rlEnvMonFanStatusEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:rlEnvMonFanStatusEntry.setStatus(_A)
_RlEnvMonFanStatusIndex_Type=Integer32
_RlEnvMonFanStatusIndex_Object=MibTableColumn
rlEnvMonFanStatusIndex=_RlEnvMonFanStatusIndex_Object((1,3,6,1,4,1,89,83,1,1,1,1),_RlEnvMonFanStatusIndex_Type())
rlEnvMonFanStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlEnvMonFanStatusIndex.setStatus(_A)
class _RlEnvMonFanStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlEnvMonFanStatusDescr_Type.__name__=_F
_RlEnvMonFanStatusDescr_Object=MibTableColumn
rlEnvMonFanStatusDescr=_RlEnvMonFanStatusDescr_Object((1,3,6,1,4,1,89,83,1,1,1,2),_RlEnvMonFanStatusDescr_Type())
rlEnvMonFanStatusDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonFanStatusDescr.setStatus(_A)
_RlEnvMonFanState_Type=RlEnvMonState
_RlEnvMonFanState_Object=MibTableColumn
rlEnvMonFanState=_RlEnvMonFanState_Object((1,3,6,1,4,1,89,83,1,1,1,3),_RlEnvMonFanState_Type())
rlEnvMonFanState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonFanState.setStatus(_A)
_RlEnvMonSupplyStatusTable_Object=MibTable
rlEnvMonSupplyStatusTable=_RlEnvMonSupplyStatusTable_Object((1,3,6,1,4,1,89,83,1,2))
if mibBuilder.loadTexts:rlEnvMonSupplyStatusTable.setStatus(_A)
_RlEnvMonSupplyStatusEntry_Object=MibTableRow
rlEnvMonSupplyStatusEntry=_RlEnvMonSupplyStatusEntry_Object((1,3,6,1,4,1,89,83,1,2,1))
rlEnvMonSupplyStatusEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:rlEnvMonSupplyStatusEntry.setStatus(_A)
class _RlEnvMonSupplyStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlEnvMonSupplyStatusIndex_Type.__name__=_E
_RlEnvMonSupplyStatusIndex_Object=MibTableColumn
rlEnvMonSupplyStatusIndex=_RlEnvMonSupplyStatusIndex_Object((1,3,6,1,4,1,89,83,1,2,1,1),_RlEnvMonSupplyStatusIndex_Type())
rlEnvMonSupplyStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlEnvMonSupplyStatusIndex.setStatus(_A)
class _RlEnvMonSupplyStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlEnvMonSupplyStatusDescr_Type.__name__=_F
_RlEnvMonSupplyStatusDescr_Object=MibTableColumn
rlEnvMonSupplyStatusDescr=_RlEnvMonSupplyStatusDescr_Object((1,3,6,1,4,1,89,83,1,2,1,2),_RlEnvMonSupplyStatusDescr_Type())
rlEnvMonSupplyStatusDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonSupplyStatusDescr.setStatus(_A)
_RlEnvMonSupplyState_Type=RlEnvMonState
_RlEnvMonSupplyState_Object=MibTableColumn
rlEnvMonSupplyState=_RlEnvMonSupplyState_Object((1,3,6,1,4,1,89,83,1,2,1,3),_RlEnvMonSupplyState_Type())
rlEnvMonSupplyState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonSupplyState.setStatus(_A)
class _RlEnvMonSupplySource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('ac',2),('dc',3),('externalPowerSupply',4),('internalRedundant',5)))
_RlEnvMonSupplySource_Type.__name__=_E
_RlEnvMonSupplySource_Object=MibTableColumn
rlEnvMonSupplySource=_RlEnvMonSupplySource_Object((1,3,6,1,4,1,89,83,1,2,1,4),_RlEnvMonSupplySource_Type())
rlEnvMonSupplySource.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonSupplySource.setStatus(_A)
_RlEnvMonSupplyFanDirection_Type=RlEnvMonDirection
_RlEnvMonSupplyFanDirection_Object=MibTableColumn
rlEnvMonSupplyFanDirection=_RlEnvMonSupplyFanDirection_Object((1,3,6,1,4,1,89,83,1,2,1,5),_RlEnvMonSupplyFanDirection_Type())
rlEnvMonSupplyFanDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonSupplyFanDirection.setStatus(_A)
_RlEnvMonIndexTable_Object=MibTable
rlEnvMonIndexTable=_RlEnvMonIndexTable_Object((1,3,6,1,4,1,89,83,1,10))
if mibBuilder.loadTexts:rlEnvMonIndexTable.setStatus(_A)
_RlEnvMonIndexEntry_Object=MibTableRow
rlEnvMonIndexEntry=_RlEnvMonIndexEntry_Object((1,3,6,1,4,1,89,83,1,10,1))
rlEnvMonIndexEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:rlEnvMonIndexEntry.setStatus(_A)
_RlEnvMonIndexUnitId_Type=Integer32
_RlEnvMonIndexUnitId_Object=MibTableColumn
rlEnvMonIndexUnitId=_RlEnvMonIndexUnitId_Object((1,3,6,1,4,1,89,83,1,10,1,1),_RlEnvMonIndexUnitId_Type())
rlEnvMonIndexUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlEnvMonIndexUnitId.setStatus(_A)
class _RlEnvMonIndexObjType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,14)));namedValues=NamedValues(*(('powerSupply',5),('fan',6),('thermalSensorUnderCard',14)))
_RlEnvMonIndexObjType_Type.__name__=_E
_RlEnvMonIndexObjType_Object=MibTableColumn
rlEnvMonIndexObjType=_RlEnvMonIndexObjType_Object((1,3,6,1,4,1,89,83,1,10,1,2),_RlEnvMonIndexObjType_Type())
rlEnvMonIndexObjType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlEnvMonIndexObjType.setStatus(_A)
_RlEnvMonIndexObjIndex_Type=Integer32
_RlEnvMonIndexObjIndex_Object=MibTableColumn
rlEnvMonIndexObjIndex=_RlEnvMonIndexObjIndex_Object((1,3,6,1,4,1,89,83,1,10,1,3),_RlEnvMonIndexObjIndex_Type())
rlEnvMonIndexObjIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlEnvMonIndexObjIndex.setStatus(_A)
_RlEnvMonIndexValue_Type=Integer32
_RlEnvMonIndexValue_Object=MibTableColumn
rlEnvMonIndexValue=_RlEnvMonIndexValue_Object((1,3,6,1,4,1,89,83,1,10,1,4),_RlEnvMonIndexValue_Type())
rlEnvMonIndexValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonIndexValue.setStatus(_A)
_RlEnvFanData_ObjectIdentity=ObjectIdentity
rlEnvFanData=_RlEnvFanData_ObjectIdentity((1,3,6,1,4,1,89,83,5))
_RlEnvFanDataTable_Object=MibTable
rlEnvFanDataTable=_RlEnvFanDataTable_Object((1,3,6,1,4,1,89,83,5,1))
if mibBuilder.loadTexts:rlEnvFanDataTable.setStatus(_A)
_RlEnvFanDataEntry_Object=MibTableRow
rlEnvFanDataEntry=_RlEnvFanDataEntry_Object((1,3,6,1,4,1,89,83,5,1,1))
rlEnvFanDataEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:rlEnvFanDataEntry.setStatus(_A)
_RlEnvFanDataStackUnit_Type=Integer32
_RlEnvFanDataStackUnit_Object=MibTableColumn
rlEnvFanDataStackUnit=_RlEnvFanDataStackUnit_Object((1,3,6,1,4,1,89,83,5,1,1,1),_RlEnvFanDataStackUnit_Type())
rlEnvFanDataStackUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvFanDataStackUnit.setStatus(_A)
_RlEnvFanDataTemp_Type=Integer32
_RlEnvFanDataTemp_Object=MibTableColumn
rlEnvFanDataTemp=_RlEnvFanDataTemp_Object((1,3,6,1,4,1,89,83,5,1,1,2),_RlEnvFanDataTemp_Type())
rlEnvFanDataTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvFanDataTemp.setStatus(_A)
_RlEnvFanDataSpeed_Type=Integer32
_RlEnvFanDataSpeed_Object=MibTableColumn
rlEnvFanDataSpeed=_RlEnvFanDataSpeed_Object((1,3,6,1,4,1,89,83,5,1,1,3),_RlEnvFanDataSpeed_Type())
rlEnvFanDataSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvFanDataSpeed.setStatus(_A)
_RlEnvFanDataOperLevel_Type=Integer32
_RlEnvFanDataOperLevel_Object=MibTableColumn
rlEnvFanDataOperLevel=_RlEnvFanDataOperLevel_Object((1,3,6,1,4,1,89,83,5,1,1,4),_RlEnvFanDataOperLevel_Type())
rlEnvFanDataOperLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvFanDataOperLevel.setStatus(_A)
_RlEnvFanDataAdminLevel_Type=Integer32
_RlEnvFanDataAdminLevel_Object=MibTableColumn
rlEnvFanDataAdminLevel=_RlEnvFanDataAdminLevel_Object((1,3,6,1,4,1,89,83,5,1,1,5),_RlEnvFanDataAdminLevel_Type())
rlEnvFanDataAdminLevel.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlEnvFanDataAdminLevel.setStatus(_A)
_RlEnvFanDataDirection_Type=RlEnvMonDirection
_RlEnvFanDataDirection_Object=MibTableColumn
rlEnvFanDataDirection=_RlEnvFanDataDirection_Object((1,3,6,1,4,1,89,83,5,1,1,6),_RlEnvFanDataDirection_Type())
rlEnvFanDataDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvFanDataDirection.setStatus(_A)
_RlEnvRedundantFanTable_Object=MibTable
rlEnvRedundantFanTable=_RlEnvRedundantFanTable_Object((1,3,6,1,4,1,89,83,6))
if mibBuilder.loadTexts:rlEnvRedundantFanTable.setStatus(_A)
_RlEnvRedundantFanEntry_Object=MibTableRow
rlEnvRedundantFanEntry=_RlEnvRedundantFanEntry_Object((1,3,6,1,4,1,89,83,6,1))
rlEnvRedundantFanEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:rlEnvRedundantFanEntry.setStatus(_A)
_RlEnvRedundantFanUnitId_Type=Unsigned32
_RlEnvRedundantFanUnitId_Object=MibTableColumn
rlEnvRedundantFanUnitId=_RlEnvRedundantFanUnitId_Object((1,3,6,1,4,1,89,83,6,1,1),_RlEnvRedundantFanUnitId_Type())
rlEnvRedundantFanUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvRedundantFanUnitId.setStatus(_A)
_RlEnvRedundantFanIndex_Type=Integer32
_RlEnvRedundantFanIndex_Object=MibTableColumn
rlEnvRedundantFanIndex=_RlEnvRedundantFanIndex_Object((1,3,6,1,4,1,89,83,6,1,2),_RlEnvRedundantFanIndex_Type())
rlEnvRedundantFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvRedundantFanIndex.setStatus(_A)
_RlEnvRedundantFanStatus_Type=RlEnvRedundantFanStatus
_RlEnvRedundantFanStatus_Object=MibTableColumn
rlEnvRedundantFanStatus=_RlEnvRedundantFanStatus_Object((1,3,6,1,4,1,89,83,6,1,3),_RlEnvRedundantFanStatus_Type())
rlEnvRedundantFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvRedundantFanStatus.setStatus(_A)
_RlEnvRedundantFanSupported_Type=TruthValue
_RlEnvRedundantFanSupported_Object=MibScalar
rlEnvRedundantFanSupported=_RlEnvRedundantFanSupported_Object((1,3,6,1,4,1,89,83,7),_RlEnvRedundantFanSupported_Type())
rlEnvRedundantFanSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvRedundantFanSupported.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlEnvMonState':RlEnvMonState,'RlEnvMonDirection':RlEnvMonDirection,'RlEnvRedundantFanStatus':RlEnvRedundantFanStatus,'rlEnv':rlEnv,'rlEnvPhysicalDescription':rlEnvPhysicalDescription,'rlEnvMonFanStatusTable':rlEnvMonFanStatusTable,'rlEnvMonFanStatusEntry':rlEnvMonFanStatusEntry,_H:rlEnvMonFanStatusIndex,'rlEnvMonFanStatusDescr':rlEnvMonFanStatusDescr,'rlEnvMonFanState':rlEnvMonFanState,'rlEnvMonSupplyStatusTable':rlEnvMonSupplyStatusTable,'rlEnvMonSupplyStatusEntry':rlEnvMonSupplyStatusEntry,_I:rlEnvMonSupplyStatusIndex,'rlEnvMonSupplyStatusDescr':rlEnvMonSupplyStatusDescr,'rlEnvMonSupplyState':rlEnvMonSupplyState,'rlEnvMonSupplySource':rlEnvMonSupplySource,'rlEnvMonSupplyFanDirection':rlEnvMonSupplyFanDirection,'rlEnvMonIndexTable':rlEnvMonIndexTable,'rlEnvMonIndexEntry':rlEnvMonIndexEntry,_J:rlEnvMonIndexUnitId,_K:rlEnvMonIndexObjType,_L:rlEnvMonIndexObjIndex,'rlEnvMonIndexValue':rlEnvMonIndexValue,'rlEnvFanData':rlEnvFanData,'rlEnvFanDataTable':rlEnvFanDataTable,'rlEnvFanDataEntry':rlEnvFanDataEntry,_M:rlEnvFanDataStackUnit,'rlEnvFanDataTemp':rlEnvFanDataTemp,'rlEnvFanDataSpeed':rlEnvFanDataSpeed,'rlEnvFanDataOperLevel':rlEnvFanDataOperLevel,'rlEnvFanDataAdminLevel':rlEnvFanDataAdminLevel,'rlEnvFanDataDirection':rlEnvFanDataDirection,'rlEnvRedundantFanTable':rlEnvRedundantFanTable,'rlEnvRedundantFanEntry':rlEnvRedundantFanEntry,_N:rlEnvRedundantFanUnitId,_O:rlEnvRedundantFanIndex,'rlEnvRedundantFanStatus':rlEnvRedundantFanStatus,'rlEnvRedundantFanSupported':rlEnvRedundantFanSupported})