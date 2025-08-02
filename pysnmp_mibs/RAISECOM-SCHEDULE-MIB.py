_J='raisecomScheduleCommandNo'
_I='raisecomScheduleIndex'
_H='raisecomScheduleListIndex'
_G='not-accessible'
_F='OctetString'
_E='RAISECOM-SCHEDULE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
raisecomSchedule=ModuleIdentity((1,3,6,1,4,1,8886,1,8))
_RaisecomScheduleconfig_ObjectIdentity=ObjectIdentity
raisecomScheduleconfig=_RaisecomScheduleconfig_ObjectIdentity((1,3,6,1,4,1,8886,1,8,1))
_RaisecomScheduleList_ObjectIdentity=ObjectIdentity
raisecomScheduleList=_RaisecomScheduleList_ObjectIdentity((1,3,6,1,4,1,8886,1,8,2))
_RaisecomScheduleListTable_Object=MibTable
raisecomScheduleListTable=_RaisecomScheduleListTable_Object((1,3,6,1,4,1,8886,1,8,2,1))
if mibBuilder.loadTexts:raisecomScheduleListTable.setStatus(_A)
_RaisecomScheduleListEntry_Object=MibTableRow
raisecomScheduleListEntry=_RaisecomScheduleListEntry_Object((1,3,6,1,4,1,8886,1,8,2,1,1))
raisecomScheduleListEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:raisecomScheduleListEntry.setStatus(_A)
class _RaisecomScheduleListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_RaisecomScheduleListIndex_Type.__name__=_C
_RaisecomScheduleListIndex_Object=MibTableColumn
raisecomScheduleListIndex=_RaisecomScheduleListIndex_Object((1,3,6,1,4,1,8886,1,8,2,1,1,1),_RaisecomScheduleListIndex_Type())
raisecomScheduleListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomScheduleListIndex.setStatus(_A)
class _RaisecomScheduleListFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('startup',1),('realdate',2)))
_RaisecomScheduleListFlag_Type.__name__=_C
_RaisecomScheduleListFlag_Object=MibTableColumn
raisecomScheduleListFlag=_RaisecomScheduleListFlag_Object((1,3,6,1,4,1,8886,1,8,2,1,1,2),_RaisecomScheduleListFlag_Type())
raisecomScheduleListFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomScheduleListFlag.setStatus(_A)
_RaisecomScheduleListStartTime_Type=Integer32
_RaisecomScheduleListStartTime_Object=MibTableColumn
raisecomScheduleListStartTime=_RaisecomScheduleListStartTime_Object((1,3,6,1,4,1,8886,1,8,2,1,1,3),_RaisecomScheduleListStartTime_Type())
raisecomScheduleListStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomScheduleListStartTime.setStatus(_A)
class _RaisecomScheduleListPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31622400))
_RaisecomScheduleListPeriod_Type.__name__=_C
_RaisecomScheduleListPeriod_Object=MibTableColumn
raisecomScheduleListPeriod=_RaisecomScheduleListPeriod_Object((1,3,6,1,4,1,8886,1,8,2,1,1,4),_RaisecomScheduleListPeriod_Type())
raisecomScheduleListPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomScheduleListPeriod.setStatus(_A)
_RaisecomScheduleListStopTime_Type=Integer32
_RaisecomScheduleListStopTime_Object=MibTableColumn
raisecomScheduleListStopTime=_RaisecomScheduleListStopTime_Object((1,3,6,1,4,1,8886,1,8,2,1,1,5),_RaisecomScheduleListStopTime_Type())
raisecomScheduleListStopTime.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomScheduleListStopTime.setStatus(_A)
_RaisecomScheduleListLastExeTime_Type=Integer32
_RaisecomScheduleListLastExeTime_Object=MibTableColumn
raisecomScheduleListLastExeTime=_RaisecomScheduleListLastExeTime_Object((1,3,6,1,4,1,8886,1,8,2,1,1,6),_RaisecomScheduleListLastExeTime_Type())
raisecomScheduleListLastExeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleListLastExeTime.setStatus(_A)
_RaisecomScheduleListNextExeTime_Type=Integer32
_RaisecomScheduleListNextExeTime_Object=MibTableColumn
raisecomScheduleListNextExeTime=_RaisecomScheduleListNextExeTime_Object((1,3,6,1,4,1,8886,1,8,2,1,1,7),_RaisecomScheduleListNextExeTime_Type())
raisecomScheduleListNextExeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleListNextExeTime.setStatus(_A)
_RaisecomScheduleRef_Type=Integer32
_RaisecomScheduleRef_Object=MibTableColumn
raisecomScheduleRef=_RaisecomScheduleRef_Object((1,3,6,1,4,1,8886,1,8,2,1,1,8),_RaisecomScheduleRef_Type())
raisecomScheduleRef.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleRef.setStatus(_A)
_RaisecomScheduleListStatus_Type=RowStatus
_RaisecomScheduleListStatus_Object=MibTableColumn
raisecomScheduleListStatus=_RaisecomScheduleListStatus_Object((1,3,6,1,4,1,8886,1,8,2,1,1,9),_RaisecomScheduleListStatus_Type())
raisecomScheduleListStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomScheduleListStatus.setStatus(_A)
_RaisecomScheduleCommandTable_Object=MibTable
raisecomScheduleCommandTable=_RaisecomScheduleCommandTable_Object((1,3,6,1,4,1,8886,1,8,2,2))
if mibBuilder.loadTexts:raisecomScheduleCommandTable.setStatus(_A)
_RaisecomScheduleCommandEntry_Object=MibTableRow
raisecomScheduleCommandEntry=_RaisecomScheduleCommandEntry_Object((1,3,6,1,4,1,8886,1,8,2,2,1))
raisecomScheduleCommandEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:raisecomScheduleCommandEntry.setStatus(_A)
class _RaisecomScheduleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_RaisecomScheduleIndex_Type.__name__=_C
_RaisecomScheduleIndex_Object=MibTableColumn
raisecomScheduleIndex=_RaisecomScheduleIndex_Object((1,3,6,1,4,1,8886,1,8,2,2,1,1),_RaisecomScheduleIndex_Type())
raisecomScheduleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomScheduleIndex.setStatus(_A)
class _RaisecomScheduleCommandNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_RaisecomScheduleCommandNo_Type.__name__=_C
_RaisecomScheduleCommandNo_Object=MibTableColumn
raisecomScheduleCommandNo=_RaisecomScheduleCommandNo_Object((1,3,6,1,4,1,8886,1,8,2,2,1,2),_RaisecomScheduleCommandNo_Type())
raisecomScheduleCommandNo.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomScheduleCommandNo.setStatus(_A)
class _RaisecomScheduleCommandString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RaisecomScheduleCommandString_Type.__name__=_F
_RaisecomScheduleCommandString_Object=MibTableColumn
raisecomScheduleCommandString=_RaisecomScheduleCommandString_Object((1,3,6,1,4,1,8886,1,8,2,2,1,3),_RaisecomScheduleCommandString_Type())
raisecomScheduleCommandString.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleCommandString.setStatus(_A)
class _RaisecomScheduleCommandMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('user-mode',0),('auth-mode',1),('view-mode',2),('auth-enable-mode',3),('enable-mode',4),('vlan-mode',5),('interface-mode',6),('interface-range-mode',7),('aggregator-mode',8),('ip-mode',9),('config-mode',10),('rip-mode',11),('bgp-mode',12),('ospf-mode',13),('factory-mode',14),('game-mode',15),('hide-mode',16),('cluster-mode',17)))
_RaisecomScheduleCommandMode_Type.__name__=_C
_RaisecomScheduleCommandMode_Object=MibTableColumn
raisecomScheduleCommandMode=_RaisecomScheduleCommandMode_Object((1,3,6,1,4,1,8886,1,8,2,2,1,4),_RaisecomScheduleCommandMode_Type())
raisecomScheduleCommandMode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleCommandMode.setStatus(_A)
class _RaisecomScheduleCommandNodeInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RaisecomScheduleCommandNodeInfo_Type.__name__=_F
_RaisecomScheduleCommandNodeInfo_Object=MibTableColumn
raisecomScheduleCommandNodeInfo=_RaisecomScheduleCommandNodeInfo_Object((1,3,6,1,4,1,8886,1,8,2,2,1,5),_RaisecomScheduleCommandNodeInfo_Type())
raisecomScheduleCommandNodeInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleCommandNodeInfo.setStatus(_A)
_RaisecomScheduleCommandExeCount_Type=Integer32
_RaisecomScheduleCommandExeCount_Object=MibTableColumn
raisecomScheduleCommandExeCount=_RaisecomScheduleCommandExeCount_Object((1,3,6,1,4,1,8886,1,8,2,2,1,6),_RaisecomScheduleCommandExeCount_Type())
raisecomScheduleCommandExeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleCommandExeCount.setStatus(_A)
_RaisecomScheduleCommandLastExeTime_Type=Integer32
_RaisecomScheduleCommandLastExeTime_Object=MibTableColumn
raisecomScheduleCommandLastExeTime=_RaisecomScheduleCommandLastExeTime_Object((1,3,6,1,4,1,8886,1,8,2,2,1,7),_RaisecomScheduleCommandLastExeTime_Type())
raisecomScheduleCommandLastExeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomScheduleCommandLastExeTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'raisecomSchedule':raisecomSchedule,'raisecomScheduleconfig':raisecomScheduleconfig,'raisecomScheduleList':raisecomScheduleList,'raisecomScheduleListTable':raisecomScheduleListTable,'raisecomScheduleListEntry':raisecomScheduleListEntry,_H:raisecomScheduleListIndex,'raisecomScheduleListFlag':raisecomScheduleListFlag,'raisecomScheduleListStartTime':raisecomScheduleListStartTime,'raisecomScheduleListPeriod':raisecomScheduleListPeriod,'raisecomScheduleListStopTime':raisecomScheduleListStopTime,'raisecomScheduleListLastExeTime':raisecomScheduleListLastExeTime,'raisecomScheduleListNextExeTime':raisecomScheduleListNextExeTime,'raisecomScheduleRef':raisecomScheduleRef,'raisecomScheduleListStatus':raisecomScheduleListStatus,'raisecomScheduleCommandTable':raisecomScheduleCommandTable,'raisecomScheduleCommandEntry':raisecomScheduleCommandEntry,_I:raisecomScheduleIndex,_J:raisecomScheduleCommandNo,'raisecomScheduleCommandString':raisecomScheduleCommandString,'raisecomScheduleCommandMode':raisecomScheduleCommandMode,'raisecomScheduleCommandNodeInfo':raisecomScheduleCommandNodeInfo,'raisecomScheduleCommandExeCount':raisecomScheduleCommandExeCount,'raisecomScheduleCommandLastExeTime':raisecomScheduleCommandLastExeTime})