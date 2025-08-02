_AO='ifOtnOpuGroupV4'
_AN='ifOtnOpuGroupV2'
_AM='ifOtnOpuGroupV1'
_AL='ifOtnOduGroupV1'
_AK='ifOtnOtuGroupV1'
_AJ='ifOtnOpuConnOduIndex'
_AI='ifOtnGeneralIfOtnTpStateLastChangeTime'
_AH='ifOtnGeneralIfOtnTpConfigLastChangeTime'
_AG='ifOtnGeneralIfOtnTpTableSize'
_AF='ifOtnOtuUpPortId'
_AE='ifOtnTpTribSlotView'
_AD='ifOtnTpTribSlotMask'
_AC='ifOtnOduParentOduIndex'
_AB='ifOtnOduType'
_AA='ifOtnGeneralGroupV2'
_A9='ifOtnTpGroupV1'
_A8='ifOtnOtuGroupV2'
_A7='ifOtnOpuLossOfOpuMultiFrameIdentifier'
_A6='ifOtnTpRxSignalStatus'
_A5='ifOtnTpTxSignalStatus'
_A4='ifOtnTpRxMultiplexStructureIdentifierMismatch'
_A3='ifOtnTpTribPortId'
_A2='ifOtnTpUsedTribSlots'
_A1='ifOtnTpConnIfBasicIfIndex'
_A0='ifOtnTpName'
_z='ifOtnOduRxSignalStatus'
_y='ifOtnOduTxSignalStatus'
_x='ifOtnOduUsedTcms'
_w='ifOtnOduGcc2Terminated'
_v='ifOtnOduGcc1Terminated'
_u='ifOtnOduConnIfBasicIfIndex'
_t='ifOtnOduName'
_s='ifOtnGeneralIfOtnOpuStateLastChangeTime'
_r='ifOtnGeneralIfOtnOpuConfigLastChangeTime'
_q='ifOtnGeneralIfOtnOpuTableSize'
_p='ifOtnGeneralIfOtnOduStateLastChangeTime'
_o='ifOtnGeneralIfOtnOduConfigLastChangeTime'
_n='ifOtnGeneralIfOtnOduTableSize'
_m='ifOtnGeneralIfOtnOtuStateLastChangeTime'
_l='ifOtnGeneralIfOtnOtuConfigLastChangeTime'
_k='ifOtnGeneralIfOtnOtuTableSize'
_j='ifOtnGeneralStateLastChangeTime'
_i='ifOtnGeneralConfigLastChangeTime'
_h='read-write'
_g='DisplayString'
_f='Integer32'
_e='TruthValueWithNA'
_d='ifOtnTpGroupV2'
_c='ifOtnOtuGroupV3'
_b='ifOtnOpuGroupV3'
_a='ifOtnOpuTxPayloadMismatch'
_Z='ifOtnOpuRxPayloadMismatch'
_Y='ifOtnOtuLossOfMultiframe'
_X='ifOtnOtuRxAlarmIndicationSignal'
_W='ifOtnOtuLossOfFrame'
_V='ifOtnOtuRxSignalStatus'
_U='ifOtnOtuTxSignalStatus'
_T='ifOtnOtuConnIfBasicIfIndex'
_S='ifOtnOtuName'
_R='ifOtnTpIndex'
_Q='ifOtnOduIndex'
_P='ifOtnGeneralGroupV1'
_O='ifOtnOpuTxClientSignalFail'
_N='ifOtnOpuTxClientMaintenanceIndication'
_M='ifOtnOpuRxSignalStatus'
_L='ifOtnOpuTxSignalStatus'
_K='ifOtnOpuConnIfBasicIfIndex'
_J='ifOtnOpuName'
_I='ifOtnOtuIndex'
_H='Unsigned32WithNA'
_G='ifOtnOduGroupV2'
_F='ifOtnOpuIndex'
_E='read-create'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-IFOTN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfOtnMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfOtnMIB','lumModules')
CommandString,FaultStatusWithNA,MgmtNameString,SignalStatusWithNA,TruthValueWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','CommandString','FaultStatusWithNA','MgmtNameString','SignalStatusWithNA',_e,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_f,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_g,'PhysAddress','TextualConvention')
lumIfOtnMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,50))
if mibBuilder.loadTexts:lumIfOtnMIBModule.setRevisions(('2018-06-29 00:00','2017-12-15 00:00','2017-06-15 00:00','2016-11-30 00:00','2015-01-23 00:00','2014-09-30 00:00','2014-05-16 00:00','2013-11-15 00:00','2013-05-01 00:00'))
_LumIfOtnConfs_ObjectIdentity=ObjectIdentity
lumIfOtnConfs=_LumIfOtnConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,50,1))
_LumIfOtnGroups_ObjectIdentity=ObjectIdentity
lumIfOtnGroups=_LumIfOtnGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,50,1,1))
_LumIfOtnCompl_ObjectIdentity=ObjectIdentity
lumIfOtnCompl=_LumIfOtnCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,50,1,2))
_LumIfOtnMIBObjects_ObjectIdentity=ObjectIdentity
lumIfOtnMIBObjects=_LumIfOtnMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,50,2))
_IfOtnGeneral_ObjectIdentity=ObjectIdentity
ifOtnGeneral=_IfOtnGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,50,2,1))
_IfOtnGeneralConfigLastChangeTime_Type=DateAndTime
_IfOtnGeneralConfigLastChangeTime_Object=MibScalar
ifOtnGeneralConfigLastChangeTime=_IfOtnGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,1),_IfOtnGeneralConfigLastChangeTime_Type())
ifOtnGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralConfigLastChangeTime.setStatus(_B)
_IfOtnGeneralStateLastChangeTime_Type=DateAndTime
_IfOtnGeneralStateLastChangeTime_Object=MibScalar
ifOtnGeneralStateLastChangeTime=_IfOtnGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,2),_IfOtnGeneralStateLastChangeTime_Type())
ifOtnGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralStateLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnOtuTableSize_Type=Unsigned32
_IfOtnGeneralIfOtnOtuTableSize_Object=MibScalar
ifOtnGeneralIfOtnOtuTableSize=_IfOtnGeneralIfOtnOtuTableSize_Object((1,3,6,1,4,1,8708,2,50,2,1,3),_IfOtnGeneralIfOtnOtuTableSize_Type())
ifOtnGeneralIfOtnOtuTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOtuTableSize.setStatus(_B)
_IfOtnGeneralIfOtnOtuConfigLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnOtuConfigLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnOtuConfigLastChangeTime=_IfOtnGeneralIfOtnOtuConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,4),_IfOtnGeneralIfOtnOtuConfigLastChangeTime_Type())
ifOtnGeneralIfOtnOtuConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOtuConfigLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnOtuStateLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnOtuStateLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnOtuStateLastChangeTime=_IfOtnGeneralIfOtnOtuStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,5),_IfOtnGeneralIfOtnOtuStateLastChangeTime_Type())
ifOtnGeneralIfOtnOtuStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOtuStateLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnOduTableSize_Type=Unsigned32
_IfOtnGeneralIfOtnOduTableSize_Object=MibScalar
ifOtnGeneralIfOtnOduTableSize=_IfOtnGeneralIfOtnOduTableSize_Object((1,3,6,1,4,1,8708,2,50,2,1,6),_IfOtnGeneralIfOtnOduTableSize_Type())
ifOtnGeneralIfOtnOduTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOduTableSize.setStatus(_B)
_IfOtnGeneralIfOtnOduConfigLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnOduConfigLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnOduConfigLastChangeTime=_IfOtnGeneralIfOtnOduConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,7),_IfOtnGeneralIfOtnOduConfigLastChangeTime_Type())
ifOtnGeneralIfOtnOduConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOduConfigLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnOduStateLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnOduStateLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnOduStateLastChangeTime=_IfOtnGeneralIfOtnOduStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,8),_IfOtnGeneralIfOtnOduStateLastChangeTime_Type())
ifOtnGeneralIfOtnOduStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOduStateLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnOpuTableSize_Type=Unsigned32
_IfOtnGeneralIfOtnOpuTableSize_Object=MibScalar
ifOtnGeneralIfOtnOpuTableSize=_IfOtnGeneralIfOtnOpuTableSize_Object((1,3,6,1,4,1,8708,2,50,2,1,9),_IfOtnGeneralIfOtnOpuTableSize_Type())
ifOtnGeneralIfOtnOpuTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOpuTableSize.setStatus(_B)
_IfOtnGeneralIfOtnOpuConfigLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnOpuConfigLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnOpuConfigLastChangeTime=_IfOtnGeneralIfOtnOpuConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,10),_IfOtnGeneralIfOtnOpuConfigLastChangeTime_Type())
ifOtnGeneralIfOtnOpuConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOpuConfigLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnOpuStateLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnOpuStateLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnOpuStateLastChangeTime=_IfOtnGeneralIfOtnOpuStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,11),_IfOtnGeneralIfOtnOpuStateLastChangeTime_Type())
ifOtnGeneralIfOtnOpuStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnOpuStateLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnTpTableSize_Type=Unsigned32
_IfOtnGeneralIfOtnTpTableSize_Object=MibScalar
ifOtnGeneralIfOtnTpTableSize=_IfOtnGeneralIfOtnTpTableSize_Object((1,3,6,1,4,1,8708,2,50,2,1,12),_IfOtnGeneralIfOtnTpTableSize_Type())
ifOtnGeneralIfOtnTpTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnTpTableSize.setStatus(_B)
_IfOtnGeneralIfOtnTpConfigLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnTpConfigLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnTpConfigLastChangeTime=_IfOtnGeneralIfOtnTpConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,13),_IfOtnGeneralIfOtnTpConfigLastChangeTime_Type())
ifOtnGeneralIfOtnTpConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnTpConfigLastChangeTime.setStatus(_B)
_IfOtnGeneralIfOtnTpStateLastChangeTime_Type=DateAndTime
_IfOtnGeneralIfOtnTpStateLastChangeTime_Object=MibScalar
ifOtnGeneralIfOtnTpStateLastChangeTime=_IfOtnGeneralIfOtnTpStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,50,2,1,14),_IfOtnGeneralIfOtnTpStateLastChangeTime_Type())
ifOtnGeneralIfOtnTpStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnGeneralIfOtnTpStateLastChangeTime.setStatus(_B)
_IfOtnOtuList_ObjectIdentity=ObjectIdentity
ifOtnOtuList=_IfOtnOtuList_ObjectIdentity((1,3,6,1,4,1,8708,2,50,2,2))
_IfOtnOtuTable_Object=MibTable
ifOtnOtuTable=_IfOtnOtuTable_Object((1,3,6,1,4,1,8708,2,50,2,2,1))
if mibBuilder.loadTexts:ifOtnOtuTable.setStatus(_B)
_IfOtnOtuEntry_Object=MibTableRow
ifOtnOtuEntry=_IfOtnOtuEntry_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1))
ifOtnOtuEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ifOtnOtuEntry.setStatus(_B)
_IfOtnOtuIndex_Type=Unsigned32
_IfOtnOtuIndex_Object=MibTableColumn
ifOtnOtuIndex=_IfOtnOtuIndex_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,1),_IfOtnOtuIndex_Type())
ifOtnOtuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuIndex.setStatus(_B)
_IfOtnOtuName_Type=MgmtNameString
_IfOtnOtuName_Object=MibTableColumn
ifOtnOtuName=_IfOtnOtuName_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,2),_IfOtnOtuName_Type())
ifOtnOtuName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuName.setStatus(_B)
_IfOtnOtuConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfOtnOtuConnIfBasicIfIndex_Object=MibTableColumn
ifOtnOtuConnIfBasicIfIndex=_IfOtnOtuConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,3),_IfOtnOtuConnIfBasicIfIndex_Type())
ifOtnOtuConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuConnIfBasicIfIndex.setStatus(_B)
_IfOtnOtuTxSignalStatus_Type=SignalStatusWithNA
_IfOtnOtuTxSignalStatus_Object=MibTableColumn
ifOtnOtuTxSignalStatus=_IfOtnOtuTxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,4),_IfOtnOtuTxSignalStatus_Type())
ifOtnOtuTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuTxSignalStatus.setStatus(_B)
_IfOtnOtuRxSignalStatus_Type=SignalStatusWithNA
_IfOtnOtuRxSignalStatus_Object=MibTableColumn
ifOtnOtuRxSignalStatus=_IfOtnOtuRxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,5),_IfOtnOtuRxSignalStatus_Type())
ifOtnOtuRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuRxSignalStatus.setStatus(_B)
_IfOtnOtuLossOfFrame_Type=FaultStatusWithNA
_IfOtnOtuLossOfFrame_Object=MibTableColumn
ifOtnOtuLossOfFrame=_IfOtnOtuLossOfFrame_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,6),_IfOtnOtuLossOfFrame_Type())
ifOtnOtuLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuLossOfFrame.setStatus(_B)
_IfOtnOtuRxAlarmIndicationSignal_Type=FaultStatusWithNA
_IfOtnOtuRxAlarmIndicationSignal_Object=MibTableColumn
ifOtnOtuRxAlarmIndicationSignal=_IfOtnOtuRxAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,7),_IfOtnOtuRxAlarmIndicationSignal_Type())
ifOtnOtuRxAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuRxAlarmIndicationSignal.setStatus(_B)
_IfOtnOtuLossOfMultiframe_Type=FaultStatusWithNA
_IfOtnOtuLossOfMultiframe_Object=MibTableColumn
ifOtnOtuLossOfMultiframe=_IfOtnOtuLossOfMultiframe_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,8),_IfOtnOtuLossOfMultiframe_Type())
ifOtnOtuLossOfMultiframe.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuLossOfMultiframe.setStatus(_B)
class _IfOtnOtuUpPortId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_IfOtnOtuUpPortId_Type.__name__=_f
_IfOtnOtuUpPortId_Object=MibTableColumn
ifOtnOtuUpPortId=_IfOtnOtuUpPortId_Object((1,3,6,1,4,1,8708,2,50,2,2,1,1,9),_IfOtnOtuUpPortId_Type())
ifOtnOtuUpPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOtuUpPortId.setStatus(_B)
_IfOtnOduList_ObjectIdentity=ObjectIdentity
ifOtnOduList=_IfOtnOduList_ObjectIdentity((1,3,6,1,4,1,8708,2,50,2,3))
_IfOtnOduTable_Object=MibTable
ifOtnOduTable=_IfOtnOduTable_Object((1,3,6,1,4,1,8708,2,50,2,3,1))
if mibBuilder.loadTexts:ifOtnOduTable.setStatus(_B)
_IfOtnOduEntry_Object=MibTableRow
ifOtnOduEntry=_IfOtnOduEntry_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1))
ifOtnOduEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:ifOtnOduEntry.setStatus(_B)
_IfOtnOduIndex_Type=Unsigned32
_IfOtnOduIndex_Object=MibTableColumn
ifOtnOduIndex=_IfOtnOduIndex_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,1),_IfOtnOduIndex_Type())
ifOtnOduIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOduIndex.setStatus(_B)
_IfOtnOduName_Type=MgmtNameString
_IfOtnOduName_Object=MibTableColumn
ifOtnOduName=_IfOtnOduName_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,2),_IfOtnOduName_Type())
ifOtnOduName.setMaxAccess(_E)
if mibBuilder.loadTexts:ifOtnOduName.setStatus(_B)
_IfOtnOduConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfOtnOduConnIfBasicIfIndex_Object=MibTableColumn
ifOtnOduConnIfBasicIfIndex=_IfOtnOduConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,3),_IfOtnOduConnIfBasicIfIndex_Type())
ifOtnOduConnIfBasicIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifOtnOduConnIfBasicIfIndex.setStatus(_B)
class _IfOtnOduGcc1Terminated_Type(TruthValueWithNA):defaultValue=1
_IfOtnOduGcc1Terminated_Type.__name__=_e
_IfOtnOduGcc1Terminated_Object=MibTableColumn
ifOtnOduGcc1Terminated=_IfOtnOduGcc1Terminated_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,4),_IfOtnOduGcc1Terminated_Type())
ifOtnOduGcc1Terminated.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOduGcc1Terminated.setStatus(_B)
class _IfOtnOduGcc2Terminated_Type(TruthValueWithNA):defaultValue=1
_IfOtnOduGcc2Terminated_Type.__name__=_e
_IfOtnOduGcc2Terminated_Object=MibTableColumn
ifOtnOduGcc2Terminated=_IfOtnOduGcc2Terminated_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,5),_IfOtnOduGcc2Terminated_Type())
ifOtnOduGcc2Terminated.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOduGcc2Terminated.setStatus(_B)
class _IfOtnOduUsedTcms_Type(Unsigned32WithNA):defaultValue=0
_IfOtnOduUsedTcms_Type.__name__=_H
_IfOtnOduUsedTcms_Object=MibTableColumn
ifOtnOduUsedTcms=_IfOtnOduUsedTcms_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,6),_IfOtnOduUsedTcms_Type())
ifOtnOduUsedTcms.setMaxAccess(_h)
if mibBuilder.loadTexts:ifOtnOduUsedTcms.setStatus(_B)
_IfOtnOduTxSignalStatus_Type=SignalStatusWithNA
_IfOtnOduTxSignalStatus_Object=MibTableColumn
ifOtnOduTxSignalStatus=_IfOtnOduTxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,7),_IfOtnOduTxSignalStatus_Type())
ifOtnOduTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOduTxSignalStatus.setStatus(_B)
_IfOtnOduRxSignalStatus_Type=SignalStatusWithNA
_IfOtnOduRxSignalStatus_Object=MibTableColumn
ifOtnOduRxSignalStatus=_IfOtnOduRxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,8),_IfOtnOduRxSignalStatus_Type())
ifOtnOduRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOduRxSignalStatus.setStatus(_B)
class _IfOtnOduType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,2147483647)));namedValues=NamedValues(*(('unused',1),('odu0',2),('odu1',3),('odu2',4),('odu3',5),('odu4',6),('oduFlex',7),('oduJ2',8),('odu2e',9),('notApplicable',2147483647)))
_IfOtnOduType_Type.__name__=_f
_IfOtnOduType_Object=MibTableColumn
ifOtnOduType=_IfOtnOduType_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,9),_IfOtnOduType_Type())
ifOtnOduType.setMaxAccess(_E)
if mibBuilder.loadTexts:ifOtnOduType.setStatus(_B)
class _IfOtnOduParentOduIndex_Type(Unsigned32WithNA):defaultValue=2147483647
_IfOtnOduParentOduIndex_Type.__name__=_H
_IfOtnOduParentOduIndex_Object=MibTableColumn
ifOtnOduParentOduIndex=_IfOtnOduParentOduIndex_Object((1,3,6,1,4,1,8708,2,50,2,3,1,1,10),_IfOtnOduParentOduIndex_Type())
ifOtnOduParentOduIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:ifOtnOduParentOduIndex.setStatus(_B)
_IfOtnOpuList_ObjectIdentity=ObjectIdentity
ifOtnOpuList=_IfOtnOpuList_ObjectIdentity((1,3,6,1,4,1,8708,2,50,2,4))
_IfOtnOpuTable_Object=MibTable
ifOtnOpuTable=_IfOtnOpuTable_Object((1,3,6,1,4,1,8708,2,50,2,4,1))
if mibBuilder.loadTexts:ifOtnOpuTable.setStatus(_B)
_IfOtnOpuEntry_Object=MibTableRow
ifOtnOpuEntry=_IfOtnOpuEntry_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1))
ifOtnOpuEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ifOtnOpuEntry.setStatus(_B)
_IfOtnOpuIndex_Type=Unsigned32
_IfOtnOpuIndex_Object=MibTableColumn
ifOtnOpuIndex=_IfOtnOpuIndex_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,1),_IfOtnOpuIndex_Type())
ifOtnOpuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuIndex.setStatus(_B)
_IfOtnOpuName_Type=MgmtNameString
_IfOtnOpuName_Object=MibTableColumn
ifOtnOpuName=_IfOtnOpuName_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,2),_IfOtnOpuName_Type())
ifOtnOpuName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuName.setStatus(_B)
_IfOtnOpuConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfOtnOpuConnIfBasicIfIndex_Object=MibTableColumn
ifOtnOpuConnIfBasicIfIndex=_IfOtnOpuConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,3),_IfOtnOpuConnIfBasicIfIndex_Type())
ifOtnOpuConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuConnIfBasicIfIndex.setStatus(_B)
_IfOtnOpuTxSignalStatus_Type=SignalStatusWithNA
_IfOtnOpuTxSignalStatus_Object=MibTableColumn
ifOtnOpuTxSignalStatus=_IfOtnOpuTxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,4),_IfOtnOpuTxSignalStatus_Type())
ifOtnOpuTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuTxSignalStatus.setStatus(_B)
_IfOtnOpuRxSignalStatus_Type=SignalStatusWithNA
_IfOtnOpuRxSignalStatus_Object=MibTableColumn
ifOtnOpuRxSignalStatus=_IfOtnOpuRxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,5),_IfOtnOpuRxSignalStatus_Type())
ifOtnOpuRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuRxSignalStatus.setStatus(_B)
_IfOtnOpuTxClientMaintenanceIndication_Type=FaultStatusWithNA
_IfOtnOpuTxClientMaintenanceIndication_Object=MibTableColumn
ifOtnOpuTxClientMaintenanceIndication=_IfOtnOpuTxClientMaintenanceIndication_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,6),_IfOtnOpuTxClientMaintenanceIndication_Type())
ifOtnOpuTxClientMaintenanceIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuTxClientMaintenanceIndication.setStatus(_B)
_IfOtnOpuTxClientSignalFail_Type=FaultStatusWithNA
_IfOtnOpuTxClientSignalFail_Object=MibTableColumn
ifOtnOpuTxClientSignalFail=_IfOtnOpuTxClientSignalFail_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,7),_IfOtnOpuTxClientSignalFail_Type())
ifOtnOpuTxClientSignalFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuTxClientSignalFail.setStatus(_B)
_IfOtnOpuRxPayloadMismatch_Type=FaultStatusWithNA
_IfOtnOpuRxPayloadMismatch_Object=MibTableColumn
ifOtnOpuRxPayloadMismatch=_IfOtnOpuRxPayloadMismatch_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,8),_IfOtnOpuRxPayloadMismatch_Type())
ifOtnOpuRxPayloadMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuRxPayloadMismatch.setStatus(_B)
_IfOtnOpuTxPayloadMismatch_Type=FaultStatusWithNA
_IfOtnOpuTxPayloadMismatch_Object=MibTableColumn
ifOtnOpuTxPayloadMismatch=_IfOtnOpuTxPayloadMismatch_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,9),_IfOtnOpuTxPayloadMismatch_Type())
ifOtnOpuTxPayloadMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuTxPayloadMismatch.setStatus(_B)
_IfOtnOpuLossOfOpuMultiFrameIdentifier_Type=FaultStatusWithNA
_IfOtnOpuLossOfOpuMultiFrameIdentifier_Object=MibTableColumn
ifOtnOpuLossOfOpuMultiFrameIdentifier=_IfOtnOpuLossOfOpuMultiFrameIdentifier_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,10),_IfOtnOpuLossOfOpuMultiFrameIdentifier_Type())
ifOtnOpuLossOfOpuMultiFrameIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuLossOfOpuMultiFrameIdentifier.setStatus(_B)
_IfOtnOpuRxClientMaintenanceIndication_Type=FaultStatusWithNA
_IfOtnOpuRxClientMaintenanceIndication_Object=MibTableColumn
ifOtnOpuRxClientMaintenanceIndication=_IfOtnOpuRxClientMaintenanceIndication_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,11),_IfOtnOpuRxClientMaintenanceIndication_Type())
ifOtnOpuRxClientMaintenanceIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuRxClientMaintenanceIndication.setStatus(_B)
_IfOtnOpuConnOduIndex_Type=Unsigned32WithNA
_IfOtnOpuConnOduIndex_Object=MibTableColumn
ifOtnOpuConnOduIndex=_IfOtnOpuConnOduIndex_Object((1,3,6,1,4,1,8708,2,50,2,4,1,1,12),_IfOtnOpuConnOduIndex_Type())
ifOtnOpuConnOduIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnOpuConnOduIndex.setStatus(_B)
_IfOtnTpList_ObjectIdentity=ObjectIdentity
ifOtnTpList=_IfOtnTpList_ObjectIdentity((1,3,6,1,4,1,8708,2,50,2,5))
_IfOtnTpTable_Object=MibTable
ifOtnTpTable=_IfOtnTpTable_Object((1,3,6,1,4,1,8708,2,50,2,5,1))
if mibBuilder.loadTexts:ifOtnTpTable.setStatus(_B)
_IfOtnTpEntry_Object=MibTableRow
ifOtnTpEntry=_IfOtnTpEntry_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1))
ifOtnTpEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:ifOtnTpEntry.setStatus(_B)
_IfOtnTpIndex_Type=Unsigned32
_IfOtnTpIndex_Object=MibTableColumn
ifOtnTpIndex=_IfOtnTpIndex_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,1),_IfOtnTpIndex_Type())
ifOtnTpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnTpIndex.setStatus(_B)
_IfOtnTpName_Type=MgmtNameString
_IfOtnTpName_Object=MibTableColumn
ifOtnTpName=_IfOtnTpName_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,2),_IfOtnTpName_Type())
ifOtnTpName.setMaxAccess(_E)
if mibBuilder.loadTexts:ifOtnTpName.setStatus(_B)
_IfOtnTpConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfOtnTpConnIfBasicIfIndex_Object=MibTableColumn
ifOtnTpConnIfBasicIfIndex=_IfOtnTpConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,3),_IfOtnTpConnIfBasicIfIndex_Type())
ifOtnTpConnIfBasicIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifOtnTpConnIfBasicIfIndex.setStatus(_B)
_IfOtnTpUsedTribSlots_Type=Unsigned32WithNA
_IfOtnTpUsedTribSlots_Object=MibTableColumn
ifOtnTpUsedTribSlots=_IfOtnTpUsedTribSlots_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,4),_IfOtnTpUsedTribSlots_Type())
ifOtnTpUsedTribSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnTpUsedTribSlots.setStatus(_B)
class _IfOtnTpTribPortId_Type(Unsigned32WithNA):defaultValue=2147483647
_IfOtnTpTribPortId_Type.__name__=_H
_IfOtnTpTribPortId_Object=MibTableColumn
ifOtnTpTribPortId=_IfOtnTpTribPortId_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,5),_IfOtnTpTribPortId_Type())
ifOtnTpTribPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:ifOtnTpTribPortId.setStatus(_B)
_IfOtnTpRxMultiplexStructureIdentifierMismatch_Type=FaultStatusWithNA
_IfOtnTpRxMultiplexStructureIdentifierMismatch_Object=MibTableColumn
ifOtnTpRxMultiplexStructureIdentifierMismatch=_IfOtnTpRxMultiplexStructureIdentifierMismatch_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,6),_IfOtnTpRxMultiplexStructureIdentifierMismatch_Type())
ifOtnTpRxMultiplexStructureIdentifierMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnTpRxMultiplexStructureIdentifierMismatch.setStatus(_B)
_IfOtnTpTxSignalStatus_Type=SignalStatusWithNA
_IfOtnTpTxSignalStatus_Object=MibTableColumn
ifOtnTpTxSignalStatus=_IfOtnTpTxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,7),_IfOtnTpTxSignalStatus_Type())
ifOtnTpTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnTpTxSignalStatus.setStatus(_B)
_IfOtnTpRxSignalStatus_Type=SignalStatusWithNA
_IfOtnTpRxSignalStatus_Object=MibTableColumn
ifOtnTpRxSignalStatus=_IfOtnTpRxSignalStatus_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,8),_IfOtnTpRxSignalStatus_Type())
ifOtnTpRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnTpRxSignalStatus.setStatus(_B)
class _IfOtnTpXcRefOduIndex_Type(Unsigned32WithNA):defaultValue=2147483647
_IfOtnTpXcRefOduIndex_Type.__name__=_H
_IfOtnTpXcRefOduIndex_Object=MibTableColumn
ifOtnTpXcRefOduIndex=_IfOtnTpXcRefOduIndex_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,9),_IfOtnTpXcRefOduIndex_Type())
ifOtnTpXcRefOduIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifOtnTpXcRefOduIndex.setStatus(_B)
class _IfOtnTpTribSlotMask_Type(DisplayString):defaultValue=OctetString('')
_IfOtnTpTribSlotMask_Type.__name__=_g
_IfOtnTpTribSlotMask_Object=MibTableColumn
ifOtnTpTribSlotMask=_IfOtnTpTribSlotMask_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,10),_IfOtnTpTribSlotMask_Type())
ifOtnTpTribSlotMask.setMaxAccess(_h)
if mibBuilder.loadTexts:ifOtnTpTribSlotMask.setStatus(_B)
class _IfOtnTpTribSlotView_Type(DisplayString):defaultValue=OctetString('')
_IfOtnTpTribSlotView_Type.__name__=_g
_IfOtnTpTribSlotView_Object=MibTableColumn
ifOtnTpTribSlotView=_IfOtnTpTribSlotView_Object((1,3,6,1,4,1,8708,2,50,2,5,1,1,11),_IfOtnTpTribSlotView_Type())
ifOtnTpTribSlotView.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtnTpTribSlotView.setStatus(_B)
ifOtnGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,1))
ifOtnGeneralGroupV1.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ifOtnGeneralGroupV1.setStatus(_D)
ifOtnOtuGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,2))
ifOtnOtuGroupV1.setObjects(*((_A,_I),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ifOtnOtuGroupV1.setStatus(_D)
ifOtnOduGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,3))
ifOtnOduGroupV1.setObjects(*((_A,_Q),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ifOtnOduGroupV1.setStatus(_D)
ifOtnOpuGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,4))
ifOtnOpuGroupV1.setObjects(*((_A,_F),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ifOtnOpuGroupV1.setStatus(_D)
ifOtnTpGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,5))
ifOtnTpGroupV1.setObjects(*((_A,_R),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:ifOtnTpGroupV1.setStatus(_B)
ifOtnOpuGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,6))
ifOtnOpuGroupV2.setObjects(*((_A,_F),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ifOtnOpuGroupV2.setStatus(_D)
ifOtnOduGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,7))
ifOtnOduGroupV2.setObjects(*((_A,_Q),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:ifOtnOduGroupV2.setStatus(_B)
ifOtnOtuGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,8))
ifOtnOtuGroupV2.setObjects(*((_A,_I),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ifOtnOtuGroupV2.setStatus(_D)
ifOtnOpuGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,9))
ifOtnOpuGroupV3.setObjects(*((_A,_F),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_A7)))
if mibBuilder.loadTexts:ifOtnOpuGroupV3.setStatus(_D)
ifOtnTpGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,10))
ifOtnTpGroupV2.setObjects(*((_A,_R),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ifOtnTpGroupV2.setStatus(_B)
ifOtnOtuGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,11))
ifOtnOtuGroupV3.setObjects(*((_A,_I),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_AF)))
if mibBuilder.loadTexts:ifOtnOtuGroupV3.setStatus(_B)
ifOtnGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,12))
ifOtnGeneralGroupV2.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:ifOtnGeneralGroupV2.setStatus(_B)
ifOtnOpuGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,50,1,1,13))
ifOtnOpuGroupV4.setObjects(*((_A,_F),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_A7),(_A,_AJ)))
if mibBuilder.loadTexts:ifOtnOpuGroupV4.setStatus(_B)
lumIfOtnComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,50,1,2,1))
lumIfOtnComplV1.setObjects(*((_A,_P),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:lumIfOtnComplV1.setStatus(_D)
lumIfOtnComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,50,1,2,2))
lumIfOtnComplV2.setObjects(*((_A,_P),(_A,_A8),(_A,_G),(_A,_AN),(_A,_A9)))
if mibBuilder.loadTexts:lumIfOtnComplV2.setStatus(_D)
lumIfOtnComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,50,1,2,3))
lumIfOtnComplV3.setObjects(*((_A,_P),(_A,_A8),(_A,_G),(_A,_b),(_A,_A9)))
if mibBuilder.loadTexts:lumIfOtnComplV3.setStatus(_D)
lumIfOtnComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,50,1,2,4))
lumIfOtnComplV4.setObjects(*((_A,_P),(_A,_c),(_A,_G),(_A,_b),(_A,_d)))
if mibBuilder.loadTexts:lumIfOtnComplV4.setStatus(_D)
lumIfOtnComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,50,1,2,5))
lumIfOtnComplV5.setObjects(*((_A,_AA),(_A,_c),(_A,_G),(_A,_b),(_A,_d)))
if mibBuilder.loadTexts:lumIfOtnComplV5.setStatus(_D)
lumIfOtnComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,50,1,2,6))
lumIfOtnComplV6.setObjects(*((_A,_AA),(_A,_c),(_A,_G),(_A,_AO),(_A,_d)))
if mibBuilder.loadTexts:lumIfOtnComplV6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfOtnMIBModule':lumIfOtnMIBModule,'lumIfOtnConfs':lumIfOtnConfs,'lumIfOtnGroups':lumIfOtnGroups,_P:ifOtnGeneralGroupV1,_AK:ifOtnOtuGroupV1,_AL:ifOtnOduGroupV1,_AM:ifOtnOpuGroupV1,_A9:ifOtnTpGroupV1,_AN:ifOtnOpuGroupV2,_G:ifOtnOduGroupV2,_A8:ifOtnOtuGroupV2,_b:ifOtnOpuGroupV3,_d:ifOtnTpGroupV2,_c:ifOtnOtuGroupV3,_AA:ifOtnGeneralGroupV2,_AO:ifOtnOpuGroupV4,'lumIfOtnCompl':lumIfOtnCompl,'lumIfOtnComplV1':lumIfOtnComplV1,'lumIfOtnComplV2':lumIfOtnComplV2,'lumIfOtnComplV3':lumIfOtnComplV3,'lumIfOtnComplV4':lumIfOtnComplV4,'lumIfOtnComplV5':lumIfOtnComplV5,'lumIfOtnComplV6':lumIfOtnComplV6,'lumIfOtnMIBObjects':lumIfOtnMIBObjects,'ifOtnGeneral':ifOtnGeneral,_i:ifOtnGeneralConfigLastChangeTime,_j:ifOtnGeneralStateLastChangeTime,_k:ifOtnGeneralIfOtnOtuTableSize,_l:ifOtnGeneralIfOtnOtuConfigLastChangeTime,_m:ifOtnGeneralIfOtnOtuStateLastChangeTime,_n:ifOtnGeneralIfOtnOduTableSize,_o:ifOtnGeneralIfOtnOduConfigLastChangeTime,_p:ifOtnGeneralIfOtnOduStateLastChangeTime,_q:ifOtnGeneralIfOtnOpuTableSize,_r:ifOtnGeneralIfOtnOpuConfigLastChangeTime,_s:ifOtnGeneralIfOtnOpuStateLastChangeTime,_AG:ifOtnGeneralIfOtnTpTableSize,_AH:ifOtnGeneralIfOtnTpConfigLastChangeTime,_AI:ifOtnGeneralIfOtnTpStateLastChangeTime,'ifOtnOtuList':ifOtnOtuList,'ifOtnOtuTable':ifOtnOtuTable,'ifOtnOtuEntry':ifOtnOtuEntry,_I:ifOtnOtuIndex,_S:ifOtnOtuName,_T:ifOtnOtuConnIfBasicIfIndex,_U:ifOtnOtuTxSignalStatus,_V:ifOtnOtuRxSignalStatus,_W:ifOtnOtuLossOfFrame,_X:ifOtnOtuRxAlarmIndicationSignal,_Y:ifOtnOtuLossOfMultiframe,_AF:ifOtnOtuUpPortId,'ifOtnOduList':ifOtnOduList,'ifOtnOduTable':ifOtnOduTable,'ifOtnOduEntry':ifOtnOduEntry,_Q:ifOtnOduIndex,_t:ifOtnOduName,_u:ifOtnOduConnIfBasicIfIndex,_v:ifOtnOduGcc1Terminated,_w:ifOtnOduGcc2Terminated,_x:ifOtnOduUsedTcms,_y:ifOtnOduTxSignalStatus,_z:ifOtnOduRxSignalStatus,_AB:ifOtnOduType,_AC:ifOtnOduParentOduIndex,'ifOtnOpuList':ifOtnOpuList,'ifOtnOpuTable':ifOtnOpuTable,'ifOtnOpuEntry':ifOtnOpuEntry,_F:ifOtnOpuIndex,_J:ifOtnOpuName,_K:ifOtnOpuConnIfBasicIfIndex,_L:ifOtnOpuTxSignalStatus,_M:ifOtnOpuRxSignalStatus,_N:ifOtnOpuTxClientMaintenanceIndication,_O:ifOtnOpuTxClientSignalFail,_Z:ifOtnOpuRxPayloadMismatch,_a:ifOtnOpuTxPayloadMismatch,_A7:ifOtnOpuLossOfOpuMultiFrameIdentifier,'ifOtnOpuRxClientMaintenanceIndication':ifOtnOpuRxClientMaintenanceIndication,_AJ:ifOtnOpuConnOduIndex,'ifOtnTpList':ifOtnTpList,'ifOtnTpTable':ifOtnTpTable,'ifOtnTpEntry':ifOtnTpEntry,_R:ifOtnTpIndex,_A0:ifOtnTpName,_A1:ifOtnTpConnIfBasicIfIndex,_A2:ifOtnTpUsedTribSlots,_A3:ifOtnTpTribPortId,_A4:ifOtnTpRxMultiplexStructureIdentifierMismatch,_A5:ifOtnTpTxSignalStatus,_A6:ifOtnTpRxSignalStatus,'ifOtnTpXcRefOduIndex':ifOtnTpXcRefOduIndex,_AD:ifOtnTpTribSlotMask,_AE:ifOtnTpTribSlotView})