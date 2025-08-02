_f='ifFhObsaiGroupV1'
_e='ifFhCpriGroupV1'
_d='ifFhGeneralGroupV1'
_c='ifFhObsaiTxLossOfFrame'
_b='ifFhObsaiRxLossOfFrame'
_a='ifFhObsaiRxSignalStatus'
_Z='ifFhObsaiTxSignalStatus'
_Y='ifFhObsaiConnIfBasicIfIndex'
_X='ifFhObsaiName'
_W='ifFhObsaiUId'
_V='ifFhCpriRxRemoteAlarmInd'
_U='ifFhCpriRxSAPDefectInd'
_T='ifFhCpriRxLossOfFrame'
_S='ifFhCpriTxLossOfFrame'
_R='ifFhCpriRxSignalStatus'
_Q='ifFhCpriTxSignalStatus'
_P='ifFhCpriConnIfBasicIfIndex'
_O='ifFhCpriName'
_N='ifFhCpriUId'
_M='ifFhGeneralIfFhObsaiStateLastChangeTime'
_L='ifFhGeneralIfFhObsaiConfigLastChangeTime'
_K='ifFhGeneralIfFhObsaiTableSize'
_J='ifFhGeneralIfFhCpriStateLastChangeTime'
_I='ifFhGeneralIfFhCpriConfigLastChangeTime'
_H='ifFhGeneralIfFhCpriTableSize'
_G='ifFhGeneralStateLastChangeTime'
_F='ifFhGeneralConfigLastChangeTime'
_E='ifFhObsaiIndex'
_D='ifFhCpriIndex'
_C='read-only'
_B='LUM-IFFH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfFhMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfFhMIB','lumModules')
FaultStatusWithNA,MgmtNameString,SignalStatusWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','FaultStatusWithNA','MgmtNameString','SignalStatusWithNA','Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfFhMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,68))
if mibBuilder.loadTexts:lumIfFhMIBModule.setRevisions(('2017-06-15 00:00','2016-06-14 00:00'))
_LumIfFhConfs_ObjectIdentity=ObjectIdentity
lumIfFhConfs=_LumIfFhConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,68,1))
_LumIfFhGroups_ObjectIdentity=ObjectIdentity
lumIfFhGroups=_LumIfFhGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,68,1,1))
_LumIfFhCompl_ObjectIdentity=ObjectIdentity
lumIfFhCompl=_LumIfFhCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,68,1,2))
_LumIfFhMIBObjects_ObjectIdentity=ObjectIdentity
lumIfFhMIBObjects=_LumIfFhMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,68,2))
_IfFhGeneral_ObjectIdentity=ObjectIdentity
ifFhGeneral=_IfFhGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,68,2,1))
_IfFhGeneralConfigLastChangeTime_Type=DateAndTime
_IfFhGeneralConfigLastChangeTime_Object=MibScalar
ifFhGeneralConfigLastChangeTime=_IfFhGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,68,2,1,1),_IfFhGeneralConfigLastChangeTime_Type())
ifFhGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralConfigLastChangeTime.setStatus(_A)
_IfFhGeneralStateLastChangeTime_Type=DateAndTime
_IfFhGeneralStateLastChangeTime_Object=MibScalar
ifFhGeneralStateLastChangeTime=_IfFhGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,68,2,1,2),_IfFhGeneralStateLastChangeTime_Type())
ifFhGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralStateLastChangeTime.setStatus(_A)
_IfFhGeneralIfFhCpriTableSize_Type=Unsigned32
_IfFhGeneralIfFhCpriTableSize_Object=MibScalar
ifFhGeneralIfFhCpriTableSize=_IfFhGeneralIfFhCpriTableSize_Object((1,3,6,1,4,1,8708,2,68,2,1,3),_IfFhGeneralIfFhCpriTableSize_Type())
ifFhGeneralIfFhCpriTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralIfFhCpriTableSize.setStatus(_A)
_IfFhGeneralIfFhCpriConfigLastChangeTime_Type=DateAndTime
_IfFhGeneralIfFhCpriConfigLastChangeTime_Object=MibScalar
ifFhGeneralIfFhCpriConfigLastChangeTime=_IfFhGeneralIfFhCpriConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,68,2,1,4),_IfFhGeneralIfFhCpriConfigLastChangeTime_Type())
ifFhGeneralIfFhCpriConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralIfFhCpriConfigLastChangeTime.setStatus(_A)
_IfFhGeneralIfFhCpriStateLastChangeTime_Type=DateAndTime
_IfFhGeneralIfFhCpriStateLastChangeTime_Object=MibScalar
ifFhGeneralIfFhCpriStateLastChangeTime=_IfFhGeneralIfFhCpriStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,68,2,1,5),_IfFhGeneralIfFhCpriStateLastChangeTime_Type())
ifFhGeneralIfFhCpriStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralIfFhCpriStateLastChangeTime.setStatus(_A)
_IfFhGeneralIfFhObsaiTableSize_Type=Unsigned32
_IfFhGeneralIfFhObsaiTableSize_Object=MibScalar
ifFhGeneralIfFhObsaiTableSize=_IfFhGeneralIfFhObsaiTableSize_Object((1,3,6,1,4,1,8708,2,68,2,1,6),_IfFhGeneralIfFhObsaiTableSize_Type())
ifFhGeneralIfFhObsaiTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralIfFhObsaiTableSize.setStatus(_A)
_IfFhGeneralIfFhObsaiConfigLastChangeTime_Type=DateAndTime
_IfFhGeneralIfFhObsaiConfigLastChangeTime_Object=MibScalar
ifFhGeneralIfFhObsaiConfigLastChangeTime=_IfFhGeneralIfFhObsaiConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,68,2,1,7),_IfFhGeneralIfFhObsaiConfigLastChangeTime_Type())
ifFhGeneralIfFhObsaiConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralIfFhObsaiConfigLastChangeTime.setStatus(_A)
_IfFhGeneralIfFhObsaiStateLastChangeTime_Type=DateAndTime
_IfFhGeneralIfFhObsaiStateLastChangeTime_Object=MibScalar
ifFhGeneralIfFhObsaiStateLastChangeTime=_IfFhGeneralIfFhObsaiStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,68,2,1,8),_IfFhGeneralIfFhObsaiStateLastChangeTime_Type())
ifFhGeneralIfFhObsaiStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhGeneralIfFhObsaiStateLastChangeTime.setStatus(_A)
_IfFhCpriList_ObjectIdentity=ObjectIdentity
ifFhCpriList=_IfFhCpriList_ObjectIdentity((1,3,6,1,4,1,8708,2,68,2,2))
_IfFhCpriTable_Object=MibTable
ifFhCpriTable=_IfFhCpriTable_Object((1,3,6,1,4,1,8708,2,68,2,2,1))
if mibBuilder.loadTexts:ifFhCpriTable.setStatus(_A)
_IfFhCpriEntry_Object=MibTableRow
ifFhCpriEntry=_IfFhCpriEntry_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1))
ifFhCpriEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ifFhCpriEntry.setStatus(_A)
_IfFhCpriIndex_Type=Unsigned32
_IfFhCpriIndex_Object=MibTableColumn
ifFhCpriIndex=_IfFhCpriIndex_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,1),_IfFhCpriIndex_Type())
ifFhCpriIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriIndex.setStatus(_A)
_IfFhCpriUId_Type=Unsigned32
_IfFhCpriUId_Object=MibTableColumn
ifFhCpriUId=_IfFhCpriUId_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,2),_IfFhCpriUId_Type())
ifFhCpriUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriUId.setStatus(_A)
_IfFhCpriName_Type=MgmtNameString
_IfFhCpriName_Object=MibTableColumn
ifFhCpriName=_IfFhCpriName_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,3),_IfFhCpriName_Type())
ifFhCpriName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriName.setStatus(_A)
_IfFhCpriConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfFhCpriConnIfBasicIfIndex_Object=MibTableColumn
ifFhCpriConnIfBasicIfIndex=_IfFhCpriConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,4),_IfFhCpriConnIfBasicIfIndex_Type())
ifFhCpriConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriConnIfBasicIfIndex.setStatus(_A)
_IfFhCpriTxSignalStatus_Type=SignalStatusWithNA
_IfFhCpriTxSignalStatus_Object=MibTableColumn
ifFhCpriTxSignalStatus=_IfFhCpriTxSignalStatus_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,5),_IfFhCpriTxSignalStatus_Type())
ifFhCpriTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriTxSignalStatus.setStatus(_A)
_IfFhCpriRxSignalStatus_Type=SignalStatusWithNA
_IfFhCpriRxSignalStatus_Object=MibTableColumn
ifFhCpriRxSignalStatus=_IfFhCpriRxSignalStatus_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,6),_IfFhCpriRxSignalStatus_Type())
ifFhCpriRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriRxSignalStatus.setStatus(_A)
_IfFhCpriTxLossOfFrame_Type=FaultStatusWithNA
_IfFhCpriTxLossOfFrame_Object=MibTableColumn
ifFhCpriTxLossOfFrame=_IfFhCpriTxLossOfFrame_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,7),_IfFhCpriTxLossOfFrame_Type())
ifFhCpriTxLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriTxLossOfFrame.setStatus(_A)
_IfFhCpriRxLossOfFrame_Type=FaultStatusWithNA
_IfFhCpriRxLossOfFrame_Object=MibTableColumn
ifFhCpriRxLossOfFrame=_IfFhCpriRxLossOfFrame_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,8),_IfFhCpriRxLossOfFrame_Type())
ifFhCpriRxLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriRxLossOfFrame.setStatus(_A)
_IfFhCpriRxSAPDefectInd_Type=FaultStatusWithNA
_IfFhCpriRxSAPDefectInd_Object=MibTableColumn
ifFhCpriRxSAPDefectInd=_IfFhCpriRxSAPDefectInd_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,9),_IfFhCpriRxSAPDefectInd_Type())
ifFhCpriRxSAPDefectInd.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriRxSAPDefectInd.setStatus(_A)
_IfFhCpriRxRemoteAlarmInd_Type=FaultStatusWithNA
_IfFhCpriRxRemoteAlarmInd_Object=MibTableColumn
ifFhCpriRxRemoteAlarmInd=_IfFhCpriRxRemoteAlarmInd_Object((1,3,6,1,4,1,8708,2,68,2,2,1,1,10),_IfFhCpriRxRemoteAlarmInd_Type())
ifFhCpriRxRemoteAlarmInd.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhCpriRxRemoteAlarmInd.setStatus(_A)
_IfFhObsaiList_ObjectIdentity=ObjectIdentity
ifFhObsaiList=_IfFhObsaiList_ObjectIdentity((1,3,6,1,4,1,8708,2,68,2,3))
_IfFhObsaiTable_Object=MibTable
ifFhObsaiTable=_IfFhObsaiTable_Object((1,3,6,1,4,1,8708,2,68,2,3,1))
if mibBuilder.loadTexts:ifFhObsaiTable.setStatus(_A)
_IfFhObsaiEntry_Object=MibTableRow
ifFhObsaiEntry=_IfFhObsaiEntry_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1))
ifFhObsaiEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ifFhObsaiEntry.setStatus(_A)
_IfFhObsaiIndex_Type=Unsigned32
_IfFhObsaiIndex_Object=MibTableColumn
ifFhObsaiIndex=_IfFhObsaiIndex_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,1),_IfFhObsaiIndex_Type())
ifFhObsaiIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiIndex.setStatus(_A)
_IfFhObsaiUId_Type=Unsigned32
_IfFhObsaiUId_Object=MibTableColumn
ifFhObsaiUId=_IfFhObsaiUId_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,2),_IfFhObsaiUId_Type())
ifFhObsaiUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiUId.setStatus(_A)
_IfFhObsaiName_Type=MgmtNameString
_IfFhObsaiName_Object=MibTableColumn
ifFhObsaiName=_IfFhObsaiName_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,3),_IfFhObsaiName_Type())
ifFhObsaiName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiName.setStatus(_A)
_IfFhObsaiConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfFhObsaiConnIfBasicIfIndex_Object=MibTableColumn
ifFhObsaiConnIfBasicIfIndex=_IfFhObsaiConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,4),_IfFhObsaiConnIfBasicIfIndex_Type())
ifFhObsaiConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiConnIfBasicIfIndex.setStatus(_A)
_IfFhObsaiTxSignalStatus_Type=SignalStatusWithNA
_IfFhObsaiTxSignalStatus_Object=MibTableColumn
ifFhObsaiTxSignalStatus=_IfFhObsaiTxSignalStatus_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,5),_IfFhObsaiTxSignalStatus_Type())
ifFhObsaiTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiTxSignalStatus.setStatus(_A)
_IfFhObsaiRxSignalStatus_Type=SignalStatusWithNA
_IfFhObsaiRxSignalStatus_Object=MibTableColumn
ifFhObsaiRxSignalStatus=_IfFhObsaiRxSignalStatus_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,6),_IfFhObsaiRxSignalStatus_Type())
ifFhObsaiRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiRxSignalStatus.setStatus(_A)
_IfFhObsaiRxLossOfFrame_Type=FaultStatusWithNA
_IfFhObsaiRxLossOfFrame_Object=MibTableColumn
ifFhObsaiRxLossOfFrame=_IfFhObsaiRxLossOfFrame_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,7),_IfFhObsaiRxLossOfFrame_Type())
ifFhObsaiRxLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiRxLossOfFrame.setStatus(_A)
_IfFhObsaiTxLossOfFrame_Type=FaultStatusWithNA
_IfFhObsaiTxLossOfFrame_Object=MibTableColumn
ifFhObsaiTxLossOfFrame=_IfFhObsaiTxLossOfFrame_Object((1,3,6,1,4,1,8708,2,68,2,3,1,1,8),_IfFhObsaiTxLossOfFrame_Type())
ifFhObsaiTxLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFhObsaiTxLossOfFrame.setStatus(_A)
ifFhGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,68,1,1,1))
ifFhGeneralGroupV1.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ifFhGeneralGroupV1.setStatus(_A)
ifFhCpriGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,68,1,1,2))
ifFhCpriGroupV1.setObjects(*((_B,_D),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ifFhCpriGroupV1.setStatus(_A)
ifFhObsaiGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,68,1,1,3))
ifFhObsaiGroupV1.setObjects(*((_B,_E),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ifFhObsaiGroupV1.setStatus(_A)
lumIfFhComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,68,1,2,1))
lumIfFhComplV1.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:lumIfFhComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lumIfFhMIBModule':lumIfFhMIBModule,'lumIfFhConfs':lumIfFhConfs,'lumIfFhGroups':lumIfFhGroups,_d:ifFhGeneralGroupV1,_e:ifFhCpriGroupV1,_f:ifFhObsaiGroupV1,'lumIfFhCompl':lumIfFhCompl,'lumIfFhComplV1':lumIfFhComplV1,'lumIfFhMIBObjects':lumIfFhMIBObjects,'ifFhGeneral':ifFhGeneral,_F:ifFhGeneralConfigLastChangeTime,_G:ifFhGeneralStateLastChangeTime,_H:ifFhGeneralIfFhCpriTableSize,_I:ifFhGeneralIfFhCpriConfigLastChangeTime,_J:ifFhGeneralIfFhCpriStateLastChangeTime,_K:ifFhGeneralIfFhObsaiTableSize,_L:ifFhGeneralIfFhObsaiConfigLastChangeTime,_M:ifFhGeneralIfFhObsaiStateLastChangeTime,'ifFhCpriList':ifFhCpriList,'ifFhCpriTable':ifFhCpriTable,'ifFhCpriEntry':ifFhCpriEntry,_D:ifFhCpriIndex,_N:ifFhCpriUId,_O:ifFhCpriName,_P:ifFhCpriConnIfBasicIfIndex,_Q:ifFhCpriTxSignalStatus,_R:ifFhCpriRxSignalStatus,_S:ifFhCpriTxLossOfFrame,_T:ifFhCpriRxLossOfFrame,_U:ifFhCpriRxSAPDefectInd,_V:ifFhCpriRxRemoteAlarmInd,'ifFhObsaiList':ifFhObsaiList,'ifFhObsaiTable':ifFhObsaiTable,'ifFhObsaiEntry':ifFhObsaiEntry,_E:ifFhObsaiIndex,_W:ifFhObsaiUId,_X:ifFhObsaiName,_Y:ifFhObsaiConnIfBasicIfIndex,_Z:ifFhObsaiTxSignalStatus,_a:ifFhObsaiRxSignalStatus,_b:ifFhObsaiRxLossOfFrame,_c:ifFhObsaiTxLossOfFrame})