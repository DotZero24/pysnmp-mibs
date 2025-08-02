_O='swWredPortProfileClassIndex'
_N='swWredPortProfilePortIndex'
_M='swWredProfileCfgPacketColor'
_L='swWredProfileCfgPacketType'
_K='swWredProfileCfgIndex'
_J='read-create'
_I='swWredProfileIndex'
_H='swWredCtrlClassIndex'
_G='swWredCtrlPortIndex'
_F='swWredPortIndex'
_E='read-only'
_D='WRED-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swWredMIB=ModuleIdentity((1,3,6,1,4,1,171,12,31))
_SwWredCtrl_ObjectIdentity=ObjectIdentity
swWredCtrl=_SwWredCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,31,1))
class _SwWredGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disabled',2),('enabled',3)))
_SwWredGlobalState_Type.__name__=_B
_SwWredGlobalState_Object=MibScalar
swWredGlobalState=_SwWredGlobalState_Object((1,3,6,1,4,1,171,12,31,1,1),_SwWredGlobalState_Type())
swWredGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredGlobalState.setStatus(_A)
_SwWredInfo_ObjectIdentity=ObjectIdentity
swWredInfo=_SwWredInfo_ObjectIdentity((1,3,6,1,4,1,171,12,31,2))
_SwWredMgmt_ObjectIdentity=ObjectIdentity
swWredMgmt=_SwWredMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,31,3))
_SwWredAverageTimeTable_Object=MibTable
swWredAverageTimeTable=_SwWredAverageTimeTable_Object((1,3,6,1,4,1,171,12,31,3,1))
if mibBuilder.loadTexts:swWredAverageTimeTable.setStatus(_A)
_SwWredAverageTimeEntry_Object=MibTableRow
swWredAverageTimeEntry=_SwWredAverageTimeEntry_Object((1,3,6,1,4,1,171,12,31,3,1,1))
swWredAverageTimeEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:swWredAverageTimeEntry.setStatus(_A)
class _SwWredPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwWredPortIndex_Type.__name__=_B
_SwWredPortIndex_Object=MibTableColumn
swWredPortIndex=_SwWredPortIndex_Object((1,3,6,1,4,1,171,12,31,3,1,1,1),_SwWredPortIndex_Type())
swWredPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredPortIndex.setStatus(_A)
class _SwWredAverageTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_SwWredAverageTime_Type.__name__=_B
_SwWredAverageTime_Object=MibTableColumn
swWredAverageTime=_SwWredAverageTime_Object((1,3,6,1,4,1,171,12,31,3,1,1,2),_SwWredAverageTime_Type())
swWredAverageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredAverageTime.setStatus(_A)
_SwWredCtrlTable_Object=MibTable
swWredCtrlTable=_SwWredCtrlTable_Object((1,3,6,1,4,1,171,12,31,3,2))
if mibBuilder.loadTexts:swWredCtrlTable.setStatus(_A)
_SwWredCtrlEntry_Object=MibTableRow
swWredCtrlEntry=_SwWredCtrlEntry_Object((1,3,6,1,4,1,171,12,31,3,2,1))
swWredCtrlEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:swWredCtrlEntry.setStatus(_A)
class _SwWredCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwWredCtrlPortIndex_Type.__name__=_B
_SwWredCtrlPortIndex_Object=MibTableColumn
swWredCtrlPortIndex=_SwWredCtrlPortIndex_Object((1,3,6,1,4,1,171,12,31,3,2,1,1),_SwWredCtrlPortIndex_Type())
swWredCtrlPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredCtrlPortIndex.setStatus(_A)
class _SwWredCtrlClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwWredCtrlClassIndex_Type.__name__=_B
_SwWredCtrlClassIndex_Object=MibTableColumn
swWredCtrlClassIndex=_SwWredCtrlClassIndex_Object((1,3,6,1,4,1,171,12,31,3,2,1,2),_SwWredCtrlClassIndex_Type())
swWredCtrlClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredCtrlClassIndex.setStatus(_A)
class _SwWredCtrlDropStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwWredCtrlDropStart_Type.__name__=_B
_SwWredCtrlDropStart_Object=MibTableColumn
swWredCtrlDropStart=_SwWredCtrlDropStart_Object((1,3,6,1,4,1,171,12,31,3,2,1,3),_SwWredCtrlDropStart_Type())
swWredCtrlDropStart.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredCtrlDropStart.setStatus(_A)
class _SwWredCtrlDropSlope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_SwWredCtrlDropSlope_Type.__name__=_B
_SwWredCtrlDropSlope_Object=MibTableColumn
swWredCtrlDropSlope=_SwWredCtrlDropSlope_Object((1,3,6,1,4,1,171,12,31,3,2,1,4),_SwWredCtrlDropSlope_Type())
swWredCtrlDropSlope.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredCtrlDropSlope.setStatus(_A)
class _SwWredAllPortAverageTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32768))
_SwWredAllPortAverageTime_Type.__name__=_B
_SwWredAllPortAverageTime_Object=MibScalar
swWredAllPortAverageTime=_SwWredAllPortAverageTime_Object((1,3,6,1,4,1,171,12,31,3,3),_SwWredAllPortAverageTime_Type())
swWredAllPortAverageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredAllPortAverageTime.setStatus(_A)
_SwWredProfileTable_Object=MibTable
swWredProfileTable=_SwWredProfileTable_Object((1,3,6,1,4,1,171,12,31,3,4))
if mibBuilder.loadTexts:swWredProfileTable.setStatus(_A)
_SwWredProfileEntry_Object=MibTableRow
swWredProfileEntry=_SwWredProfileEntry_Object((1,3,6,1,4,1,171,12,31,3,4,1))
swWredProfileEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:swWredProfileEntry.setStatus(_A)
_SwWredProfileIndex_Type=Integer32
_SwWredProfileIndex_Object=MibTableColumn
swWredProfileIndex=_SwWredProfileIndex_Object((1,3,6,1,4,1,171,12,31,3,4,1,1),_SwWredProfileIndex_Type())
swWredProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredProfileIndex.setStatus(_A)
_SwWredProfileName_Type=DisplayString
_SwWredProfileName_Object=MibTableColumn
swWredProfileName=_SwWredProfileName_Object((1,3,6,1,4,1,171,12,31,3,4,1,2),_SwWredProfileName_Type())
swWredProfileName.setMaxAccess(_J)
if mibBuilder.loadTexts:swWredProfileName.setStatus(_A)
_SwWredProfileRowStatus_Type=RowStatus
_SwWredProfileRowStatus_Object=MibTableColumn
swWredProfileRowStatus=_SwWredProfileRowStatus_Object((1,3,6,1,4,1,171,12,31,3,4,1,3),_SwWredProfileRowStatus_Type())
swWredProfileRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swWredProfileRowStatus.setStatus(_A)
_SwWredProfileCfgTable_Object=MibTable
swWredProfileCfgTable=_SwWredProfileCfgTable_Object((1,3,6,1,4,1,171,12,31,3,5))
if mibBuilder.loadTexts:swWredProfileCfgTable.setStatus(_A)
_SwWredProfileCfgEntry_Object=MibTableRow
swWredProfileCfgEntry=_SwWredProfileCfgEntry_Object((1,3,6,1,4,1,171,12,31,3,5,1))
swWredProfileCfgEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:swWredProfileCfgEntry.setStatus(_A)
class _SwWredProfileCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_SwWredProfileCfgIndex_Type.__name__=_B
_SwWredProfileCfgIndex_Object=MibTableColumn
swWredProfileCfgIndex=_SwWredProfileCfgIndex_Object((1,3,6,1,4,1,171,12,31,3,5,1,1),_SwWredProfileCfgIndex_Type())
swWredProfileCfgIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredProfileCfgIndex.setStatus(_A)
class _SwWredProfileCfgPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('nonTcp',2)))
_SwWredProfileCfgPacketType_Type.__name__=_B
_SwWredProfileCfgPacketType_Object=MibTableColumn
swWredProfileCfgPacketType=_SwWredProfileCfgPacketType_Object((1,3,6,1,4,1,171,12,31,3,5,1,2),_SwWredProfileCfgPacketType_Type())
swWredProfileCfgPacketType.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredProfileCfgPacketType.setStatus(_A)
class _SwWredProfileCfgPacketColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('yellow',2),('red',3)))
_SwWredProfileCfgPacketColor_Type.__name__=_B
_SwWredProfileCfgPacketColor_Object=MibTableColumn
swWredProfileCfgPacketColor=_SwWredProfileCfgPacketColor_Object((1,3,6,1,4,1,171,12,31,3,5,1,3),_SwWredProfileCfgPacketColor_Type())
swWredProfileCfgPacketColor.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredProfileCfgPacketColor.setStatus(_A)
class _SwWredProfileCfgMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwWredProfileCfgMinThreshold_Type.__name__=_B
_SwWredProfileCfgMinThreshold_Object=MibTableColumn
swWredProfileCfgMinThreshold=_SwWredProfileCfgMinThreshold_Object((1,3,6,1,4,1,171,12,31,3,5,1,4),_SwWredProfileCfgMinThreshold_Type())
swWredProfileCfgMinThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredProfileCfgMinThreshold.setStatus(_A)
class _SwWredProfileCfgMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwWredProfileCfgMaxThreshold_Type.__name__=_B
_SwWredProfileCfgMaxThreshold_Object=MibTableColumn
swWredProfileCfgMaxThreshold=_SwWredProfileCfgMaxThreshold_Object((1,3,6,1,4,1,171,12,31,3,5,1,5),_SwWredProfileCfgMaxThreshold_Type())
swWredProfileCfgMaxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredProfileCfgMaxThreshold.setStatus(_A)
class _SwWredProfileCfgMaxDropRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwWredProfileCfgMaxDropRate_Type.__name__=_B
_SwWredProfileCfgMaxDropRate_Object=MibTableColumn
swWredProfileCfgMaxDropRate=_SwWredProfileCfgMaxDropRate_Object((1,3,6,1,4,1,171,12,31,3,5,1,6),_SwWredProfileCfgMaxDropRate_Type())
swWredProfileCfgMaxDropRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredProfileCfgMaxDropRate.setStatus(_A)
_SwWredPortProfileTable_Object=MibTable
swWredPortProfileTable=_SwWredPortProfileTable_Object((1,3,6,1,4,1,171,12,31,3,6))
if mibBuilder.loadTexts:swWredPortProfileTable.setStatus(_A)
_SwWredPortProfileEntry_Object=MibTableRow
swWredPortProfileEntry=_SwWredPortProfileEntry_Object((1,3,6,1,4,1,171,12,31,3,6,1))
swWredPortProfileEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:swWredPortProfileEntry.setStatus(_A)
class _SwWredPortProfilePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwWredPortProfilePortIndex_Type.__name__=_B
_SwWredPortProfilePortIndex_Object=MibTableColumn
swWredPortProfilePortIndex=_SwWredPortProfilePortIndex_Object((1,3,6,1,4,1,171,12,31,3,6,1,1),_SwWredPortProfilePortIndex_Type())
swWredPortProfilePortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredPortProfilePortIndex.setStatus(_A)
class _SwWredPortProfileClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwWredPortProfileClassIndex_Type.__name__=_B
_SwWredPortProfileClassIndex_Object=MibTableColumn
swWredPortProfileClassIndex=_SwWredPortProfileClassIndex_Object((1,3,6,1,4,1,171,12,31,3,6,1,2),_SwWredPortProfileClassIndex_Type())
swWredPortProfileClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swWredPortProfileClassIndex.setStatus(_A)
_SwWredPortProfileId_Type=Integer32
_SwWredPortProfileId_Object=MibTableColumn
swWredPortProfileId=_SwWredPortProfileId_Object((1,3,6,1,4,1,171,12,31,3,6,1,3),_SwWredPortProfileId_Type())
swWredPortProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredPortProfileId.setStatus(_A)
_SwWredPortWeightNum_Type=Integer32
_SwWredPortWeightNum_Object=MibTableColumn
swWredPortWeightNum=_SwWredPortWeightNum_Object((1,3,6,1,4,1,171,12,31,3,6,1,4),_SwWredPortWeightNum_Type())
swWredPortWeightNum.setMaxAccess(_C)
if mibBuilder.loadTexts:swWredPortWeightNum.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swWredMIB':swWredMIB,'swWredCtrl':swWredCtrl,'swWredGlobalState':swWredGlobalState,'swWredInfo':swWredInfo,'swWredMgmt':swWredMgmt,'swWredAverageTimeTable':swWredAverageTimeTable,'swWredAverageTimeEntry':swWredAverageTimeEntry,_F:swWredPortIndex,'swWredAverageTime':swWredAverageTime,'swWredCtrlTable':swWredCtrlTable,'swWredCtrlEntry':swWredCtrlEntry,_G:swWredCtrlPortIndex,_H:swWredCtrlClassIndex,'swWredCtrlDropStart':swWredCtrlDropStart,'swWredCtrlDropSlope':swWredCtrlDropSlope,'swWredAllPortAverageTime':swWredAllPortAverageTime,'swWredProfileTable':swWredProfileTable,'swWredProfileEntry':swWredProfileEntry,_I:swWredProfileIndex,'swWredProfileName':swWredProfileName,'swWredProfileRowStatus':swWredProfileRowStatus,'swWredProfileCfgTable':swWredProfileCfgTable,'swWredProfileCfgEntry':swWredProfileCfgEntry,_K:swWredProfileCfgIndex,_L:swWredProfileCfgPacketType,_M:swWredProfileCfgPacketColor,'swWredProfileCfgMinThreshold':swWredProfileCfgMinThreshold,'swWredProfileCfgMaxThreshold':swWredProfileCfgMaxThreshold,'swWredProfileCfgMaxDropRate':swWredProfileCfgMaxDropRate,'swWredPortProfileTable':swWredPortProfileTable,'swWredPortProfileEntry':swWredPortProfileEntry,_N:swWredPortProfilePortIndex,_O:swWredPortProfileClassIndex,'swWredPortProfileId':swWredPortProfileId,'swWredPortWeightNum':swWredPortWeightNum})