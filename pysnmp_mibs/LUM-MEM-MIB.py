_u='memProcessGroupV2'
_t='memControlGroup'
_s='memProcessLatestSampleTime'
_r='memControlMaxReportFiles'
_q='memBoardHistory'
_p='memBoardTotalMemFreePercent'
_o='memBoardTotalMemFree'
_n='memBoardTotalMemUsed'
_m='memBoardResetPeriodAction'
_l='memBoardReportMode'
_k='memBoardProcessSupervision'
_j='memBoardName'
_i='memGeneralStateLastChangeTime'
_h='memGeneralLastChangeTime'
_g='normal'
_f='memControlGroupV2'
_e='memProcessGroup'
_d='memControlReportInterval'
_c='memControlSampleInterval'
_b='deprecated'
_a='memProcessHistory'
_Z='memProcessState'
_Y='memProcessResetPeriodAction'
_X='memProcessMaxPeriodTime'
_W='memProcessStartPeriodTime'
_V='memProcessMaxTotalTime'
_U='memProcessStartTime'
_T='memProcessIncrSizePeriod'
_S='memProcessMinSizePeriod'
_R='memProcessMaxSizePeriod'
_Q='memProcessStartSizePeriod'
_P='memProcessMinSizeTotal'
_O='memProcessMaxSizeTotal'
_N='memProcessCurSize'
_M='memProcessPid'
_L='memProcessName'
_K='memBoardIndex'
_J='DisplayString'
_I='memBoardGroup'
_H='memGeneralGroup'
_G='memProcessIndex'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='LUM-MEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumMemMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumMemMIB','lumModules')
MgmtNameString,=mibBuilder.importSymbols('LUM-TC','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_J,'PhysAddress','TextualConvention')
lumMemMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,22))
if mibBuilder.loadTexts:lumMemMIBModule.setRevisions(('2017-06-15 00:00','2003-01-09 00:00','2002-11-26 00:00'))
_LumMemConfs_ObjectIdentity=ObjectIdentity
lumMemConfs=_LumMemConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,21,1))
_LumMemGroups_ObjectIdentity=ObjectIdentity
lumMemGroups=_LumMemGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,21,1,1))
_LumMemCompl_ObjectIdentity=ObjectIdentity
lumMemCompl=_LumMemCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,21,1,2))
_LumMemMIBObjects_ObjectIdentity=ObjectIdentity
lumMemMIBObjects=_LumMemMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,21,2))
_MemGeneral_ObjectIdentity=ObjectIdentity
memGeneral=_MemGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,21,2,1))
_MemGeneralLastChangeTime_Type=DateAndTime
_MemGeneralLastChangeTime_Object=MibScalar
memGeneralLastChangeTime=_MemGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,21,2,1,1),_MemGeneralLastChangeTime_Type())
memGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:memGeneralLastChangeTime.setStatus(_B)
_MemGeneralStateLastChangeTime_Type=DateAndTime
_MemGeneralStateLastChangeTime_Object=MibScalar
memGeneralStateLastChangeTime=_MemGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,21,2,1,2),_MemGeneralStateLastChangeTime_Type())
memGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:memGeneralStateLastChangeTime.setStatus(_B)
_MemProcessList_ObjectIdentity=ObjectIdentity
memProcessList=_MemProcessList_ObjectIdentity((1,3,6,1,4,1,8708,2,21,2,2))
_MemProcessTable_Object=MibTable
memProcessTable=_MemProcessTable_Object((1,3,6,1,4,1,8708,2,21,2,2,1))
if mibBuilder.loadTexts:memProcessTable.setStatus(_B)
_MemProcessEntry_Object=MibTableRow
memProcessEntry=_MemProcessEntry_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1))
memProcessEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:memProcessEntry.setStatus(_B)
class _MemProcessIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemProcessIndex_Type.__name__=_F
_MemProcessIndex_Object=MibTableColumn
memProcessIndex=_MemProcessIndex_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,1),_MemProcessIndex_Type())
memProcessIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessIndex.setStatus(_B)
_MemProcessName_Type=MgmtNameString
_MemProcessName_Object=MibTableColumn
memProcessName=_MemProcessName_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,2),_MemProcessName_Type())
memProcessName.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessName.setStatus(_B)
_MemProcessPid_Type=Unsigned32
_MemProcessPid_Object=MibTableColumn
memProcessPid=_MemProcessPid_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,3),_MemProcessPid_Type())
memProcessPid.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessPid.setStatus(_B)
_MemProcessCurSize_Type=Unsigned32
_MemProcessCurSize_Object=MibTableColumn
memProcessCurSize=_MemProcessCurSize_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,4),_MemProcessCurSize_Type())
memProcessCurSize.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessCurSize.setStatus(_B)
_MemProcessMaxSizeTotal_Type=Unsigned32
_MemProcessMaxSizeTotal_Object=MibTableColumn
memProcessMaxSizeTotal=_MemProcessMaxSizeTotal_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,5),_MemProcessMaxSizeTotal_Type())
memProcessMaxSizeTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessMaxSizeTotal.setStatus(_B)
_MemProcessMinSizeTotal_Type=Unsigned32
_MemProcessMinSizeTotal_Object=MibTableColumn
memProcessMinSizeTotal=_MemProcessMinSizeTotal_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,6),_MemProcessMinSizeTotal_Type())
memProcessMinSizeTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessMinSizeTotal.setStatus(_B)
_MemProcessStartSizePeriod_Type=Unsigned32
_MemProcessStartSizePeriod_Object=MibTableColumn
memProcessStartSizePeriod=_MemProcessStartSizePeriod_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,7),_MemProcessStartSizePeriod_Type())
memProcessStartSizePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessStartSizePeriod.setStatus(_B)
_MemProcessMaxSizePeriod_Type=Unsigned32
_MemProcessMaxSizePeriod_Object=MibTableColumn
memProcessMaxSizePeriod=_MemProcessMaxSizePeriod_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,8),_MemProcessMaxSizePeriod_Type())
memProcessMaxSizePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessMaxSizePeriod.setStatus(_B)
_MemProcessMinSizePeriod_Type=Unsigned32
_MemProcessMinSizePeriod_Object=MibTableColumn
memProcessMinSizePeriod=_MemProcessMinSizePeriod_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,9),_MemProcessMinSizePeriod_Type())
memProcessMinSizePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessMinSizePeriod.setStatus(_B)
_MemProcessIncrSizePeriod_Type=Unsigned32
_MemProcessIncrSizePeriod_Object=MibTableColumn
memProcessIncrSizePeriod=_MemProcessIncrSizePeriod_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,10),_MemProcessIncrSizePeriod_Type())
memProcessIncrSizePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessIncrSizePeriod.setStatus(_B)
_MemProcessStartTime_Type=DateAndTime
_MemProcessStartTime_Object=MibTableColumn
memProcessStartTime=_MemProcessStartTime_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,11),_MemProcessStartTime_Type())
memProcessStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessStartTime.setStatus(_B)
_MemProcessMaxTotalTime_Type=DateAndTime
_MemProcessMaxTotalTime_Object=MibTableColumn
memProcessMaxTotalTime=_MemProcessMaxTotalTime_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,12),_MemProcessMaxTotalTime_Type())
memProcessMaxTotalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessMaxTotalTime.setStatus(_B)
_MemProcessStartPeriodTime_Type=DateAndTime
_MemProcessStartPeriodTime_Object=MibTableColumn
memProcessStartPeriodTime=_MemProcessStartPeriodTime_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,13),_MemProcessStartPeriodTime_Type())
memProcessStartPeriodTime.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessStartPeriodTime.setStatus(_B)
_MemProcessMaxPeriodTime_Type=DateAndTime
_MemProcessMaxPeriodTime_Object=MibTableColumn
memProcessMaxPeriodTime=_MemProcessMaxPeriodTime_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,14),_MemProcessMaxPeriodTime_Type())
memProcessMaxPeriodTime.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessMaxPeriodTime.setStatus(_B)
class _MemProcessResetPeriodAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('reset',2)))
_MemProcessResetPeriodAction_Type.__name__=_E
_MemProcessResetPeriodAction_Object=MibTableColumn
memProcessResetPeriodAction=_MemProcessResetPeriodAction_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,15),_MemProcessResetPeriodAction_Type())
memProcessResetPeriodAction.setMaxAccess(_D)
if mibBuilder.loadTexts:memProcessResetPeriodAction.setStatus(_B)
class _MemProcessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alive',1),('dead',2)))
_MemProcessState_Type.__name__=_E
_MemProcessState_Object=MibTableColumn
memProcessState=_MemProcessState_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,16),_MemProcessState_Type())
memProcessState.setMaxAccess(_D)
if mibBuilder.loadTexts:memProcessState.setStatus(_B)
class _MemProcessHistory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_MemProcessHistory_Type.__name__=_J
_MemProcessHistory_Object=MibTableColumn
memProcessHistory=_MemProcessHistory_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,17),_MemProcessHistory_Type())
memProcessHistory.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessHistory.setStatus(_B)
_MemProcessLatestSampleTime_Type=DateAndTime
_MemProcessLatestSampleTime_Object=MibTableColumn
memProcessLatestSampleTime=_MemProcessLatestSampleTime_Object((1,3,6,1,4,1,8708,2,21,2,2,1,1,18),_MemProcessLatestSampleTime_Type())
memProcessLatestSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:memProcessLatestSampleTime.setStatus(_B)
_MemBoardList_ObjectIdentity=ObjectIdentity
memBoardList=_MemBoardList_ObjectIdentity((1,3,6,1,4,1,8708,2,21,2,3))
_MemBoardTable_Object=MibTable
memBoardTable=_MemBoardTable_Object((1,3,6,1,4,1,8708,2,21,2,3,1))
if mibBuilder.loadTexts:memBoardTable.setStatus(_B)
_MemBoardEntry_Object=MibTableRow
memBoardEntry=_MemBoardEntry_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1))
memBoardEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:memBoardEntry.setStatus(_B)
class _MemBoardIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemBoardIndex_Type.__name__=_F
_MemBoardIndex_Object=MibTableColumn
memBoardIndex=_MemBoardIndex_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,1),_MemBoardIndex_Type())
memBoardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:memBoardIndex.setStatus(_B)
_MemBoardName_Type=MgmtNameString
_MemBoardName_Object=MibTableColumn
memBoardName=_MemBoardName_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,2),_MemBoardName_Type())
memBoardName.setMaxAccess(_C)
if mibBuilder.loadTexts:memBoardName.setStatus(_B)
class _MemBoardProcessSupervision_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_MemBoardProcessSupervision_Type.__name__=_E
_MemBoardProcessSupervision_Object=MibTableColumn
memBoardProcessSupervision=_MemBoardProcessSupervision_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,3),_MemBoardProcessSupervision_Type())
memBoardProcessSupervision.setMaxAccess(_D)
if mibBuilder.loadTexts:memBoardProcessSupervision.setStatus(_B)
class _MemBoardReportMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_MemBoardReportMode_Type.__name__=_E
_MemBoardReportMode_Object=MibTableColumn
memBoardReportMode=_MemBoardReportMode_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,4),_MemBoardReportMode_Type())
memBoardReportMode.setMaxAccess(_D)
if mibBuilder.loadTexts:memBoardReportMode.setStatus(_B)
class _MemBoardResetPeriodAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('reset',2)))
_MemBoardResetPeriodAction_Type.__name__=_E
_MemBoardResetPeriodAction_Object=MibTableColumn
memBoardResetPeriodAction=_MemBoardResetPeriodAction_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,5),_MemBoardResetPeriodAction_Type())
memBoardResetPeriodAction.setMaxAccess(_D)
if mibBuilder.loadTexts:memBoardResetPeriodAction.setStatus(_B)
_MemBoardTotalMemUsed_Type=Unsigned32
_MemBoardTotalMemUsed_Object=MibTableColumn
memBoardTotalMemUsed=_MemBoardTotalMemUsed_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,6),_MemBoardTotalMemUsed_Type())
memBoardTotalMemUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:memBoardTotalMemUsed.setStatus(_B)
_MemBoardTotalMemFree_Type=Unsigned32
_MemBoardTotalMemFree_Object=MibTableColumn
memBoardTotalMemFree=_MemBoardTotalMemFree_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,7),_MemBoardTotalMemFree_Type())
memBoardTotalMemFree.setMaxAccess(_C)
if mibBuilder.loadTexts:memBoardTotalMemFree.setStatus(_B)
_MemBoardTotalMemFreePercent_Type=Unsigned32
_MemBoardTotalMemFreePercent_Object=MibTableColumn
memBoardTotalMemFreePercent=_MemBoardTotalMemFreePercent_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,8),_MemBoardTotalMemFreePercent_Type())
memBoardTotalMemFreePercent.setMaxAccess(_C)
if mibBuilder.loadTexts:memBoardTotalMemFreePercent.setStatus(_B)
class _MemBoardHistory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_MemBoardHistory_Type.__name__=_J
_MemBoardHistory_Object=MibTableColumn
memBoardHistory=_MemBoardHistory_Object((1,3,6,1,4,1,8708,2,21,2,3,1,1,9),_MemBoardHistory_Type())
memBoardHistory.setMaxAccess(_C)
if mibBuilder.loadTexts:memBoardHistory.setStatus(_B)
_MemControl_ObjectIdentity=ObjectIdentity
memControl=_MemControl_ObjectIdentity((1,3,6,1,4,1,8708,2,21,2,4))
class _MemControlSampleInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_MemControlSampleInterval_Type.__name__=_F
_MemControlSampleInterval_Object=MibScalar
memControlSampleInterval=_MemControlSampleInterval_Object((1,3,6,1,4,1,8708,2,21,2,4,1),_MemControlSampleInterval_Type())
memControlSampleInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:memControlSampleInterval.setStatus(_B)
class _MemControlReportInterval_Type(Unsigned32):defaultValue=360;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_MemControlReportInterval_Type.__name__=_F
_MemControlReportInterval_Object=MibScalar
memControlReportInterval=_MemControlReportInterval_Object((1,3,6,1,4,1,8708,2,21,2,4,2),_MemControlReportInterval_Type())
memControlReportInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:memControlReportInterval.setStatus(_B)
class _MemControlMaxReportFiles_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000))
_MemControlMaxReportFiles_Type.__name__=_E
_MemControlMaxReportFiles_Object=MibScalar
memControlMaxReportFiles=_MemControlMaxReportFiles_Object((1,3,6,1,4,1,8708,2,21,2,4,3),_MemControlMaxReportFiles_Type())
memControlMaxReportFiles.setMaxAccess(_D)
if mibBuilder.loadTexts:memControlMaxReportFiles.setStatus(_B)
memGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,21,1,1,1))
memGeneralGroup.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:memGeneralGroup.setStatus(_B)
memProcessGroup=ObjectGroup((1,3,6,1,4,1,8708,2,21,1,1,2))
memProcessGroup.setObjects(*((_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:memProcessGroup.setStatus(_b)
memBoardGroup=ObjectGroup((1,3,6,1,4,1,8708,2,21,1,1,3))
memBoardGroup.setObjects(*((_A,_K),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:memBoardGroup.setStatus(_B)
memControlGroup=ObjectGroup((1,3,6,1,4,1,8708,2,21,1,1,4))
memControlGroup.setObjects(*((_A,_c),(_A,_d)))
if mibBuilder.loadTexts:memControlGroup.setStatus(_B)
memControlGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,21,1,1,5))
memControlGroupV2.setObjects(*((_A,_c),(_A,_d),(_A,_r)))
if mibBuilder.loadTexts:memControlGroupV2.setStatus(_B)
memProcessGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,21,1,1,6))
memProcessGroupV2.setObjects(*((_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_s)))
if mibBuilder.loadTexts:memProcessGroupV2.setStatus(_B)
lumMemBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,21,1,2,1))
lumMemBasicComplV1.setObjects(*((_A,_H),(_A,_e),(_A,_I),(_A,_t)))
if mibBuilder.loadTexts:lumMemBasicComplV1.setStatus(_b)
lumMemBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,21,1,2,2))
lumMemBasicComplV2.setObjects(*((_A,_H),(_A,_e),(_A,_I),(_A,_f)))
if mibBuilder.loadTexts:lumMemBasicComplV2.setStatus(_b)
lumMemBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,21,1,2,3))
lumMemBasicComplV3.setObjects(*((_A,_H),(_A,_u),(_A,_I),(_A,_f)))
if mibBuilder.loadTexts:lumMemBasicComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumMemMIBModule':lumMemMIBModule,'lumMemConfs':lumMemConfs,'lumMemGroups':lumMemGroups,_H:memGeneralGroup,_e:memProcessGroup,_I:memBoardGroup,_t:memControlGroup,_f:memControlGroupV2,_u:memProcessGroupV2,'lumMemCompl':lumMemCompl,'lumMemBasicComplV1':lumMemBasicComplV1,'lumMemBasicComplV2':lumMemBasicComplV2,'lumMemBasicComplV3':lumMemBasicComplV3,'lumMemMIBObjects':lumMemMIBObjects,'memGeneral':memGeneral,_h:memGeneralLastChangeTime,_i:memGeneralStateLastChangeTime,'memProcessList':memProcessList,'memProcessTable':memProcessTable,'memProcessEntry':memProcessEntry,_G:memProcessIndex,_L:memProcessName,_M:memProcessPid,_N:memProcessCurSize,_O:memProcessMaxSizeTotal,_P:memProcessMinSizeTotal,_Q:memProcessStartSizePeriod,_R:memProcessMaxSizePeriod,_S:memProcessMinSizePeriod,_T:memProcessIncrSizePeriod,_U:memProcessStartTime,_V:memProcessMaxTotalTime,_W:memProcessStartPeriodTime,_X:memProcessMaxPeriodTime,_Y:memProcessResetPeriodAction,_Z:memProcessState,_a:memProcessHistory,_s:memProcessLatestSampleTime,'memBoardList':memBoardList,'memBoardTable':memBoardTable,'memBoardEntry':memBoardEntry,_K:memBoardIndex,_j:memBoardName,_k:memBoardProcessSupervision,_l:memBoardReportMode,_m:memBoardResetPeriodAction,_n:memBoardTotalMemUsed,_o:memBoardTotalMemFree,_p:memBoardTotalMemFreePercent,_q:memBoardHistory,'memControl':memControl,_c:memControlSampleInterval,_d:memControlReportInterval,_r:memControlMaxReportFiles})