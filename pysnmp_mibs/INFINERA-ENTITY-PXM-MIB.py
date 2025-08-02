_a='pxmGroup'
_Z='pxmMPLSTPNodeID'
_Y='pxmGlobalId'
_X='pxmVsiOrInterface'
_W='pxmFlushFdbType'
_V='pxmMacFlapAction'
_U='pxmMacFlapTimeInterval'
_T='pxmMacFlapCountThreshold'
_S='pxmMacAgingTime'
_R='pxmEqptMaxPowerDraw'
_Q='pxmInstalledEqptType'
_P='pxmProvEqptType'
_O='pxmMaxSwitchingCapacity'
_N='pxmAvailableSwitchingCapacity'
_M='pxmMaxSwitchingCapacityFactor'
_L='pxmMeterActionRed'
_K='pxmTotalAvailableBW'
_J='pxmTotalBandwidth'
_I='pxmNetworkMappingMode'
_H='pxmSchedulerType'
_G='pxmMoId'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-ENTITY-PXM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatHundredths,FloatTenths,InfnEqptType,InfnFlushFdbType,InfnMacFlapAction,InfnMeterActionRed,InfnNetworkMappingMode,InfnSchedulerType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnEqptType','InfnFlushFdbType','InfnMacFlapAction','InfnMeterActionRed','InfnNetworkMappingMode','InfnSchedulerType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,30))
_PxmTable_Object=MibTable
pxmTable=_PxmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1))
if mibBuilder.loadTexts:pxmTable.setStatus(_A)
_PxmEntry_Object=MibTableRow
pxmEntry=_PxmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1))
pxmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pxmEntry.setStatus(_A)
_PxmMoId_Type=DisplayString
_PxmMoId_Object=MibTableColumn
pxmMoId=_PxmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,1),_PxmMoId_Type())
pxmMoId.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmMoId.setStatus(_A)
_PxmSchedulerType_Type=InfnSchedulerType
_PxmSchedulerType_Object=MibTableColumn
pxmSchedulerType=_PxmSchedulerType_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,2),_PxmSchedulerType_Type())
pxmSchedulerType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmSchedulerType.setStatus(_A)
_PxmNetworkMappingMode_Type=InfnNetworkMappingMode
_PxmNetworkMappingMode_Object=MibTableColumn
pxmNetworkMappingMode=_PxmNetworkMappingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,3),_PxmNetworkMappingMode_Type())
pxmNetworkMappingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmNetworkMappingMode.setStatus(_A)
_PxmTotalBandwidth_Type=Unsigned32
_PxmTotalBandwidth_Object=MibTableColumn
pxmTotalBandwidth=_PxmTotalBandwidth_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,4),_PxmTotalBandwidth_Type())
pxmTotalBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmTotalBandwidth.setStatus(_A)
_PxmTotalAvailableBW_Type=Unsigned32
_PxmTotalAvailableBW_Object=MibTableColumn
pxmTotalAvailableBW=_PxmTotalAvailableBW_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,5),_PxmTotalAvailableBW_Type())
pxmTotalAvailableBW.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmTotalAvailableBW.setStatus(_A)
_PxmMeterActionRed_Type=InfnMeterActionRed
_PxmMeterActionRed_Object=MibTableColumn
pxmMeterActionRed=_PxmMeterActionRed_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,6),_PxmMeterActionRed_Type())
pxmMeterActionRed.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMeterActionRed.setStatus(_A)
_PxmMaxSwitchingCapacityFactor_Type=FloatTenths
_PxmMaxSwitchingCapacityFactor_Object=MibTableColumn
pxmMaxSwitchingCapacityFactor=_PxmMaxSwitchingCapacityFactor_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,7),_PxmMaxSwitchingCapacityFactor_Type())
pxmMaxSwitchingCapacityFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMaxSwitchingCapacityFactor.setStatus(_A)
_PxmAvailableSwitchingCapacity_Type=FloatTenths
_PxmAvailableSwitchingCapacity_Object=MibTableColumn
pxmAvailableSwitchingCapacity=_PxmAvailableSwitchingCapacity_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,8),_PxmAvailableSwitchingCapacity_Type())
pxmAvailableSwitchingCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmAvailableSwitchingCapacity.setStatus(_A)
_PxmMaxSwitchingCapacity_Type=FloatTenths
_PxmMaxSwitchingCapacity_Object=MibTableColumn
pxmMaxSwitchingCapacity=_PxmMaxSwitchingCapacity_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,9),_PxmMaxSwitchingCapacity_Type())
pxmMaxSwitchingCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmMaxSwitchingCapacity.setStatus(_A)
_PxmProvEqptType_Type=InfnEqptType
_PxmProvEqptType_Object=MibTableColumn
pxmProvEqptType=_PxmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,10),_PxmProvEqptType_Type())
pxmProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmProvEqptType.setStatus(_A)
_PxmInstalledEqptType_Type=InfnEqptType
_PxmInstalledEqptType_Object=MibTableColumn
pxmInstalledEqptType=_PxmInstalledEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,11),_PxmInstalledEqptType_Type())
pxmInstalledEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmInstalledEqptType.setStatus(_A)
_PxmEqptMaxPowerDraw_Type=FloatHundredths
_PxmEqptMaxPowerDraw_Object=MibTableColumn
pxmEqptMaxPowerDraw=_PxmEqptMaxPowerDraw_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,12),_PxmEqptMaxPowerDraw_Type())
pxmEqptMaxPowerDraw.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmEqptMaxPowerDraw.setStatus(_A)
_PxmMacAgingTime_Type=Integer32
_PxmMacAgingTime_Object=MibTableColumn
pxmMacAgingTime=_PxmMacAgingTime_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,13),_PxmMacAgingTime_Type())
pxmMacAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMacAgingTime.setStatus(_A)
_PxmMacFlapCountThreshold_Type=Integer32
_PxmMacFlapCountThreshold_Object=MibTableColumn
pxmMacFlapCountThreshold=_PxmMacFlapCountThreshold_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,14),_PxmMacFlapCountThreshold_Type())
pxmMacFlapCountThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMacFlapCountThreshold.setStatus(_A)
_PxmMacFlapTimeInterval_Type=Integer32
_PxmMacFlapTimeInterval_Object=MibTableColumn
pxmMacFlapTimeInterval=_PxmMacFlapTimeInterval_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,15),_PxmMacFlapTimeInterval_Type())
pxmMacFlapTimeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMacFlapTimeInterval.setStatus(_A)
_PxmMacFlapAction_Type=InfnMacFlapAction
_PxmMacFlapAction_Object=MibTableColumn
pxmMacFlapAction=_PxmMacFlapAction_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,16),_PxmMacFlapAction_Type())
pxmMacFlapAction.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMacFlapAction.setStatus(_A)
_PxmFlushFdbType_Type=InfnFlushFdbType
_PxmFlushFdbType_Object=MibTableColumn
pxmFlushFdbType=_PxmFlushFdbType_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,17),_PxmFlushFdbType_Type())
pxmFlushFdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmFlushFdbType.setStatus(_A)
_PxmVsiOrInterface_Type=DisplayString
_PxmVsiOrInterface_Object=MibTableColumn
pxmVsiOrInterface=_PxmVsiOrInterface_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,18),_PxmVsiOrInterface_Type())
pxmVsiOrInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmVsiOrInterface.setStatus(_A)
_PxmGlobalId_Type=Integer32
_PxmGlobalId_Object=MibTableColumn
pxmGlobalId=_PxmGlobalId_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,19),_PxmGlobalId_Type())
pxmGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmGlobalId.setStatus(_A)
_PxmMPLSTPNodeID_Type=Integer32
_PxmMPLSTPNodeID_Object=MibTableColumn
pxmMPLSTPNodeID=_PxmMPLSTPNodeID_Object((1,3,6,1,4,1,21296,2,2,2,1,30,1,1,20),_PxmMPLSTPNodeID_Type())
pxmMPLSTPNodeID.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMPLSTPNodeID.setStatus(_A)
_PxmConformance_ObjectIdentity=ObjectIdentity
pxmConformance=_PxmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,30,3))
_PxmCompliances_ObjectIdentity=ObjectIdentity
pxmCompliances=_PxmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,30,3,1))
_PxmGroups_ObjectIdentity=ObjectIdentity
pxmGroups=_PxmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,30,3,2))
pxmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,30,3,2,1))
pxmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pxmGroup.setStatus(_A)
pxmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,30,3,1,1))
pxmCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:pxmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmMIB':pxmMIB,'pxmTable':pxmTable,'pxmEntry':pxmEntry,_G:pxmMoId,_H:pxmSchedulerType,_I:pxmNetworkMappingMode,_J:pxmTotalBandwidth,_K:pxmTotalAvailableBW,_L:pxmMeterActionRed,_M:pxmMaxSwitchingCapacityFactor,_N:pxmAvailableSwitchingCapacity,_O:pxmMaxSwitchingCapacity,_P:pxmProvEqptType,_Q:pxmInstalledEqptType,_R:pxmEqptMaxPowerDraw,_S:pxmMacAgingTime,_T:pxmMacFlapCountThreshold,_U:pxmMacFlapTimeInterval,_V:pxmMacFlapAction,_W:pxmFlushFdbType,_X:pxmVsiOrInterface,_Y:pxmGlobalId,_Z:pxmMPLSTPNodeID,'pxmConformance':pxmConformance,'pxmCompliances':pxmCompliances,'pxmCompliance':pxmCompliance,'pxmGroups':pxmGroups,_a:pxmGroup})