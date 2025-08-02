_I='rlEnvFanDataStackUnit'
_H='rlEnvMonSupplyStatusIndex'
_G='not-accessible'
_F='rlEnvMonFanStatusIndex'
_E='DisplayString'
_D='Integer32'
_C='Dell-HWENVIROMENT'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
rlEnv=ModuleIdentity((1,3,6,1,4,1,89,83))
if mibBuilder.loadTexts:rlEnv.setRevisions(('2003-09-21 00:00',))
class RlEnvMonState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('normal',1),('warning',2),('critical',3),('shutdown',4),('notPresent',5),('notFunctioning',6)))
class RlEnvMonDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unKnown',1),('frontToBack',2),('backToFront',3),('clockwise',4),('unClockwise',5),('insideOut',6),('outsideIn',7),('rightToLeft',8),('leftToRight',9)))
_RlEnvPhysicalDescription_ObjectIdentity=ObjectIdentity
rlEnvPhysicalDescription=_RlEnvPhysicalDescription_ObjectIdentity((1,3,6,1,4,1,89,83,1))
_RlEnvMonFanStatusTable_Object=MibTable
rlEnvMonFanStatusTable=_RlEnvMonFanStatusTable_Object((1,3,6,1,4,1,89,83,1,1))
if mibBuilder.loadTexts:rlEnvMonFanStatusTable.setStatus(_A)
_RlEnvMonFanStatusEntry_Object=MibTableRow
rlEnvMonFanStatusEntry=_RlEnvMonFanStatusEntry_Object((1,3,6,1,4,1,89,83,1,1,1))
rlEnvMonFanStatusEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:rlEnvMonFanStatusEntry.setStatus(_A)
_RlEnvMonFanStatusIndex_Type=Integer32
_RlEnvMonFanStatusIndex_Object=MibTableColumn
rlEnvMonFanStatusIndex=_RlEnvMonFanStatusIndex_Object((1,3,6,1,4,1,89,83,1,1,1,1),_RlEnvMonFanStatusIndex_Type())
rlEnvMonFanStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlEnvMonFanStatusIndex.setStatus(_A)
class _RlEnvMonFanStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlEnvMonFanStatusDescr_Type.__name__=_E
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
rlEnvMonSupplyStatusEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:rlEnvMonSupplyStatusEntry.setStatus(_A)
class _RlEnvMonSupplyStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlEnvMonSupplyStatusIndex_Type.__name__=_D
_RlEnvMonSupplyStatusIndex_Object=MibTableColumn
rlEnvMonSupplyStatusIndex=_RlEnvMonSupplyStatusIndex_Object((1,3,6,1,4,1,89,83,1,2,1,1),_RlEnvMonSupplyStatusIndex_Type())
rlEnvMonSupplyStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlEnvMonSupplyStatusIndex.setStatus(_A)
class _RlEnvMonSupplyStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlEnvMonSupplyStatusDescr_Type.__name__=_E
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
_RlEnvMonSupplySource_Type.__name__=_D
_RlEnvMonSupplySource_Object=MibTableColumn
rlEnvMonSupplySource=_RlEnvMonSupplySource_Object((1,3,6,1,4,1,89,83,1,2,1,4),_RlEnvMonSupplySource_Type())
rlEnvMonSupplySource.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonSupplySource.setStatus(_A)
_RlEnvMonSupplyFanDirection_Type=RlEnvMonDirection
_RlEnvMonSupplyFanDirection_Object=MibTableColumn
rlEnvMonSupplyFanDirection=_RlEnvMonSupplyFanDirection_Object((1,3,6,1,4,1,89,83,1,2,1,5),_RlEnvMonSupplyFanDirection_Type())
rlEnvMonSupplyFanDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEnvMonSupplyFanDirection.setStatus(_A)
_RlEnvFanData_ObjectIdentity=ObjectIdentity
rlEnvFanData=_RlEnvFanData_ObjectIdentity((1,3,6,1,4,1,89,83,5))
_RlEnvFanDataTable_Object=MibTable
rlEnvFanDataTable=_RlEnvFanDataTable_Object((1,3,6,1,4,1,89,83,5,1))
if mibBuilder.loadTexts:rlEnvFanDataTable.setStatus(_A)
_RlEnvFanDataEntry_Object=MibTableRow
rlEnvFanDataEntry=_RlEnvFanDataEntry_Object((1,3,6,1,4,1,89,83,5,1,1))
rlEnvFanDataEntry.setIndexNames((0,_C,_I))
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
mibBuilder.exportSymbols(_C,**{'RlEnvMonState':RlEnvMonState,'RlEnvMonDirection':RlEnvMonDirection,'rlEnv':rlEnv,'rlEnvPhysicalDescription':rlEnvPhysicalDescription,'rlEnvMonFanStatusTable':rlEnvMonFanStatusTable,'rlEnvMonFanStatusEntry':rlEnvMonFanStatusEntry,_F:rlEnvMonFanStatusIndex,'rlEnvMonFanStatusDescr':rlEnvMonFanStatusDescr,'rlEnvMonFanState':rlEnvMonFanState,'rlEnvMonSupplyStatusTable':rlEnvMonSupplyStatusTable,'rlEnvMonSupplyStatusEntry':rlEnvMonSupplyStatusEntry,_H:rlEnvMonSupplyStatusIndex,'rlEnvMonSupplyStatusDescr':rlEnvMonSupplyStatusDescr,'rlEnvMonSupplyState':rlEnvMonSupplyState,'rlEnvMonSupplySource':rlEnvMonSupplySource,'rlEnvMonSupplyFanDirection':rlEnvMonSupplyFanDirection,'rlEnvFanData':rlEnvFanData,'rlEnvFanDataTable':rlEnvFanDataTable,'rlEnvFanDataEntry':rlEnvFanDataEntry,_I:rlEnvFanDataStackUnit,'rlEnvFanDataTemp':rlEnvFanDataTemp,'rlEnvFanDataSpeed':rlEnvFanDataSpeed,'rlEnvFanDataOperLevel':rlEnvFanDataOperLevel,'rlEnvFanDataAdminLevel':rlEnvFanDataAdminLevel,'rlEnvFanDataDirection':rlEnvFanDataDirection})