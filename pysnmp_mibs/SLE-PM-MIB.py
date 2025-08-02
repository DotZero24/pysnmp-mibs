_b='slePmHistoryControlReqResult'
_a='slePmHistoryControlTimeStamp'
_Z='slePmHistoryControlRequest'
_Y='slePmCurrentControlReqResult'
_X='slePmCurrentControlTimeStamp'
_W='slePmCurrentControlRequest'
_V='slePmConfigControlTh1Day'
_U='slePmConfigControlTh15Min'
_T='slePmConfigControlTcaEnable'
_S='slePmHistoryIndex'
_R='slePmHistoryTerm'
_Q='slePmHistorySeqId'
_P='slePmCurrentTerm'
_O='slePmCurrentSeqId'
_N='tcaOccur'
_M='tcaNormal'
_L='slePmConfigSeqId'
_K='OctetString'
_J='slePmConfigControlSeqId'
_I='slePmConfigControlReqResult'
_H='slePmConfigControlTimeStamp'
_G='slePmConfigControlRequest'
_F='slePmNeId'
_E='Integer32'
_D='read-write'
_C='SLE-PM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','zeroDotZero')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
slePmMgr=ModuleIdentity((1,3,6,1,4,1,6296,101,94))
if mibBuilder.loadTexts:slePmMgr.setRevisions(('2015-11-30 00:00',))
class PmClassId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class PmId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class PmSrc(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(68,68));fixedLength=68
class PmTcaState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
class PmDateTime(TextualConvention,Unsigned32):status=_A
class _SlePmNeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SlePmNeId_Type.__name__=_K
_SlePmNeId_Object=MibScalar
slePmNeId=_SlePmNeId_Object((1,3,6,1,4,1,6296,101,94,1),_SlePmNeId_Type())
slePmNeId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmNeId.setStatus(_A)
_SlePmConfigBase_ObjectIdentity=ObjectIdentity
slePmConfigBase=_SlePmConfigBase_ObjectIdentity((1,3,6,1,4,1,6296,101,94,2))
_SlePmConfigTable_Object=MibTable
slePmConfigTable=_SlePmConfigTable_Object((1,3,6,1,4,1,6296,101,94,2,1))
if mibBuilder.loadTexts:slePmConfigTable.setStatus(_A)
_SlePmConfigEntry_Object=MibTableRow
slePmConfigEntry=_SlePmConfigEntry_Object((1,3,6,1,4,1,6296,101,94,2,1,1))
slePmConfigEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:slePmConfigEntry.setStatus(_A)
class _SlePmConfigSeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SlePmConfigSeqId_Type.__name__=_E
_SlePmConfigSeqId_Object=MibTableColumn
slePmConfigSeqId=_SlePmConfigSeqId_Object((1,3,6,1,4,1,6296,101,94,2,1,1,1),_SlePmConfigSeqId_Type())
slePmConfigSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigSeqId.setStatus(_A)
_SlePmConfigClassId_Type=PmClassId
_SlePmConfigClassId_Object=MibTableColumn
slePmConfigClassId=_SlePmConfigClassId_Object((1,3,6,1,4,1,6296,101,94,2,1,1,2),_SlePmConfigClassId_Type())
slePmConfigClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigClassId.setStatus(_A)
_SlePmConfigPmId_Type=PmId
_SlePmConfigPmId_Object=MibTableColumn
slePmConfigPmId=_SlePmConfigPmId_Object((1,3,6,1,4,1,6296,101,94,2,1,1,3),_SlePmConfigPmId_Type())
slePmConfigPmId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigPmId.setStatus(_A)
_SlePmConfigSource_Type=PmSrc
_SlePmConfigSource_Object=MibTableColumn
slePmConfigSource=_SlePmConfigSource_Object((1,3,6,1,4,1,6296,101,94,2,1,1,4),_SlePmConfigSource_Type())
slePmConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigSource.setStatus(_A)
class _SlePmConfigTcaStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SlePmConfigTcaStat_Type.__name__=_E
_SlePmConfigTcaStat_Object=MibTableColumn
slePmConfigTcaStat=_SlePmConfigTcaStat_Object((1,3,6,1,4,1,6296,101,94,2,1,1,5),_SlePmConfigTcaStat_Type())
slePmConfigTcaStat.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigTcaStat.setStatus(_A)
_SlePmConfigTcaEnable_Type=PmTcaState
_SlePmConfigTcaEnable_Object=MibTableColumn
slePmConfigTcaEnable=_SlePmConfigTcaEnable_Object((1,3,6,1,4,1,6296,101,94,2,1,1,6),_SlePmConfigTcaEnable_Type())
slePmConfigTcaEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigTcaEnable.setStatus(_A)
_SlePmConfigTh15Min_Type=Counter64
_SlePmConfigTh15Min_Object=MibTableColumn
slePmConfigTh15Min=_SlePmConfigTh15Min_Object((1,3,6,1,4,1,6296,101,94,2,1,1,7),_SlePmConfigTh15Min_Type())
slePmConfigTh15Min.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigTh15Min.setStatus(_A)
_SlePmConfigTh1Day_Type=Counter64
_SlePmConfigTh1Day_Object=MibTableColumn
slePmConfigTh1Day=_SlePmConfigTh1Day_Object((1,3,6,1,4,1,6296,101,94,2,1,1,8),_SlePmConfigTh1Day_Type())
slePmConfigTh1Day.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmConfigTh1Day.setStatus(_A)
_SlePmConfigControl_ObjectIdentity=ObjectIdentity
slePmConfigControl=_SlePmConfigControl_ObjectIdentity((1,3,6,1,4,1,6296,101,94,2,2))
class _SlePmConfigControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('setPmConfigTcaEnable',1),('setPmConfigTh15Min',2),('setPmConfigTh1Day',3)))
_SlePmConfigControlRequest_Type.__name__=_E
_SlePmConfigControlRequest_Object=MibScalar
slePmConfigControlRequest=_SlePmConfigControlRequest_Object((1,3,6,1,4,1,6296,101,94,2,2,1),_SlePmConfigControlRequest_Type())
slePmConfigControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmConfigControlRequest.setStatus(_A)
_SlePmConfigControlStatus_Type=SleControlStatusType
_SlePmConfigControlStatus_Object=MibScalar
slePmConfigControlStatus=_SlePmConfigControlStatus_Object((1,3,6,1,4,1,6296,101,94,2,2,2),_SlePmConfigControlStatus_Type())
slePmConfigControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigControlStatus.setStatus(_A)
_SlePmConfigControlTimer_Type=Gauge32
_SlePmConfigControlTimer_Object=MibScalar
slePmConfigControlTimer=_SlePmConfigControlTimer_Object((1,3,6,1,4,1,6296,101,94,2,2,3),_SlePmConfigControlTimer_Type())
slePmConfigControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmConfigControlTimer.setStatus(_A)
_SlePmConfigControlTimeStamp_Type=TimeTicks
_SlePmConfigControlTimeStamp_Object=MibScalar
slePmConfigControlTimeStamp=_SlePmConfigControlTimeStamp_Object((1,3,6,1,4,1,6296,101,94,2,2,4),_SlePmConfigControlTimeStamp_Type())
slePmConfigControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigControlTimeStamp.setStatus(_A)
_SlePmConfigControlReqResult_Type=SleControlRequestResultType
_SlePmConfigControlReqResult_Object=MibScalar
slePmConfigControlReqResult=_SlePmConfigControlReqResult_Object((1,3,6,1,4,1,6296,101,94,2,2,5),_SlePmConfigControlReqResult_Type())
slePmConfigControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmConfigControlReqResult.setStatus(_A)
_SlePmConfigControlSeqId_Type=Integer32
_SlePmConfigControlSeqId_Object=MibScalar
slePmConfigControlSeqId=_SlePmConfigControlSeqId_Object((1,3,6,1,4,1,6296,101,94,2,2,6),_SlePmConfigControlSeqId_Type())
slePmConfigControlSeqId.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmConfigControlSeqId.setStatus(_A)
_SlePmConfigControlTcaEnable_Type=PmTcaState
_SlePmConfigControlTcaEnable_Object=MibScalar
slePmConfigControlTcaEnable=_SlePmConfigControlTcaEnable_Object((1,3,6,1,4,1,6296,101,94,2,2,7),_SlePmConfigControlTcaEnable_Type())
slePmConfigControlTcaEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmConfigControlTcaEnable.setStatus(_A)
_SlePmConfigControlTh15Min_Type=Counter64
_SlePmConfigControlTh15Min_Object=MibScalar
slePmConfigControlTh15Min=_SlePmConfigControlTh15Min_Object((1,3,6,1,4,1,6296,101,94,2,2,8),_SlePmConfigControlTh15Min_Type())
slePmConfigControlTh15Min.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmConfigControlTh15Min.setStatus(_A)
_SlePmConfigControlTh1Day_Type=Counter64
_SlePmConfigControlTh1Day_Object=MibScalar
slePmConfigControlTh1Day=_SlePmConfigControlTh1Day_Object((1,3,6,1,4,1,6296,101,94,2,2,9),_SlePmConfigControlTh1Day_Type())
slePmConfigControlTh1Day.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmConfigControlTh1Day.setStatus(_A)
_SlePmConfigNotification_ObjectIdentity=ObjectIdentity
slePmConfigNotification=_SlePmConfigNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,94,2,3))
_SlePmCurrentBase_ObjectIdentity=ObjectIdentity
slePmCurrentBase=_SlePmCurrentBase_ObjectIdentity((1,3,6,1,4,1,6296,101,94,3))
_SlePmCurrentTable_Object=MibTable
slePmCurrentTable=_SlePmCurrentTable_Object((1,3,6,1,4,1,6296,101,94,3,1))
if mibBuilder.loadTexts:slePmCurrentTable.setStatus(_A)
_SlePmCurrentEntry_Object=MibTableRow
slePmCurrentEntry=_SlePmCurrentEntry_Object((1,3,6,1,4,1,6296,101,94,3,1,1))
slePmCurrentEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:slePmCurrentEntry.setStatus(_A)
class _SlePmCurrentSeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SlePmCurrentSeqId_Type.__name__=_E
_SlePmCurrentSeqId_Object=MibTableColumn
slePmCurrentSeqId=_SlePmCurrentSeqId_Object((1,3,6,1,4,1,6296,101,94,3,1,1,1),_SlePmCurrentSeqId_Type())
slePmCurrentSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentSeqId.setStatus(_A)
_SlePmCurrentClassId_Type=PmClassId
_SlePmCurrentClassId_Object=MibTableColumn
slePmCurrentClassId=_SlePmCurrentClassId_Object((1,3,6,1,4,1,6296,101,94,3,1,1,2),_SlePmCurrentClassId_Type())
slePmCurrentClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentClassId.setStatus(_A)
_SlePmCurrentPmId_Type=PmId
_SlePmCurrentPmId_Object=MibTableColumn
slePmCurrentPmId=_SlePmCurrentPmId_Object((1,3,6,1,4,1,6296,101,94,3,1,1,3),_SlePmCurrentPmId_Type())
slePmCurrentPmId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentPmId.setStatus(_A)
_SlePmCurrentSource_Type=PmSrc
_SlePmCurrentSource_Object=MibTableColumn
slePmCurrentSource=_SlePmCurrentSource_Object((1,3,6,1,4,1,6296,101,94,3,1,1,4),_SlePmCurrentSource_Type())
slePmCurrentSource.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentSource.setStatus(_A)
class _SlePmCurrentTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('min15',1),('day1',2)))
_SlePmCurrentTerm_Type.__name__=_E
_SlePmCurrentTerm_Object=MibTableColumn
slePmCurrentTerm=_SlePmCurrentTerm_Object((1,3,6,1,4,1,6296,101,94,3,1,1,5),_SlePmCurrentTerm_Type())
slePmCurrentTerm.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmCurrentTerm.setStatus(_A)
_SlePmCurrentPmCount_Type=Counter64
_SlePmCurrentPmCount_Object=MibTableColumn
slePmCurrentPmCount=_SlePmCurrentPmCount_Object((1,3,6,1,4,1,6296,101,94,3,1,1,6),_SlePmCurrentPmCount_Type())
slePmCurrentPmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentPmCount.setStatus(_A)
_SlePmCurrentAccSecond_Type=Counter32
_SlePmCurrentAccSecond_Object=MibTableColumn
slePmCurrentAccSecond=_SlePmCurrentAccSecond_Object((1,3,6,1,4,1,6296,101,94,3,1,1,7),_SlePmCurrentAccSecond_Type())
slePmCurrentAccSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentAccSecond.setStatus(_A)
class _SlePmCurrentTcaStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SlePmCurrentTcaStat_Type.__name__=_E
_SlePmCurrentTcaStat_Object=MibTableColumn
slePmCurrentTcaStat=_SlePmCurrentTcaStat_Object((1,3,6,1,4,1,6296,101,94,3,1,1,8),_SlePmCurrentTcaStat_Type())
slePmCurrentTcaStat.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentTcaStat.setStatus(_A)
_SlePmCurrentTcaTime_Type=TimeTicks
_SlePmCurrentTcaTime_Object=MibTableColumn
slePmCurrentTcaTime=_SlePmCurrentTcaTime_Object((1,3,6,1,4,1,6296,101,94,3,1,1,9),_SlePmCurrentTcaTime_Type())
slePmCurrentTcaTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentTcaTime.setStatus(_A)
_SlePmCurrentControl_ObjectIdentity=ObjectIdentity
slePmCurrentControl=_SlePmCurrentControl_ObjectIdentity((1,3,6,1,4,1,6296,101,94,3,2))
class _SlePmCurrentControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clearCurrentPm',1),('clearCurrentTca',2)))
_SlePmCurrentControlRequest_Type.__name__=_E
_SlePmCurrentControlRequest_Object=MibScalar
slePmCurrentControlRequest=_SlePmCurrentControlRequest_Object((1,3,6,1,4,1,6296,101,94,3,2,1),_SlePmCurrentControlRequest_Type())
slePmCurrentControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmCurrentControlRequest.setStatus(_A)
_SlePmCurrentControlStatus_Type=SleControlStatusType
_SlePmCurrentControlStatus_Object=MibScalar
slePmCurrentControlStatus=_SlePmCurrentControlStatus_Object((1,3,6,1,4,1,6296,101,94,3,2,2),_SlePmCurrentControlStatus_Type())
slePmCurrentControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentControlStatus.setStatus(_A)
_SlePmCurrentControlTimer_Type=Gauge32
_SlePmCurrentControlTimer_Object=MibScalar
slePmCurrentControlTimer=_SlePmCurrentControlTimer_Object((1,3,6,1,4,1,6296,101,94,3,2,3),_SlePmCurrentControlTimer_Type())
slePmCurrentControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmCurrentControlTimer.setStatus(_A)
_SlePmCurrentControlTimeStamp_Type=TimeTicks
_SlePmCurrentControlTimeStamp_Object=MibScalar
slePmCurrentControlTimeStamp=_SlePmCurrentControlTimeStamp_Object((1,3,6,1,4,1,6296,101,94,3,2,4),_SlePmCurrentControlTimeStamp_Type())
slePmCurrentControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentControlTimeStamp.setStatus(_A)
_SlePmCurrentControlReqResult_Type=SleControlRequestResultType
_SlePmCurrentControlReqResult_Object=MibScalar
slePmCurrentControlReqResult=_SlePmCurrentControlReqResult_Object((1,3,6,1,4,1,6296,101,94,3,2,5),_SlePmCurrentControlReqResult_Type())
slePmCurrentControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmCurrentControlReqResult.setStatus(_A)
_SlePmCurrentNotification_ObjectIdentity=ObjectIdentity
slePmCurrentNotification=_SlePmCurrentNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,94,3,3))
_SlePMHistoryBase_ObjectIdentity=ObjectIdentity
slePMHistoryBase=_SlePMHistoryBase_ObjectIdentity((1,3,6,1,4,1,6296,101,94,4))
_SlePmHistoryTable_Object=MibTable
slePmHistoryTable=_SlePmHistoryTable_Object((1,3,6,1,4,1,6296,101,94,4,1))
if mibBuilder.loadTexts:slePmHistoryTable.setStatus(_A)
_SlePmHistoryEntry_Object=MibTableRow
slePmHistoryEntry=_SlePmHistoryEntry_Object((1,3,6,1,4,1,6296,101,94,4,1,1))
slePmHistoryEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:slePmHistoryEntry.setStatus(_A)
class _SlePmHistorySeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SlePmHistorySeqId_Type.__name__=_E
_SlePmHistorySeqId_Object=MibTableColumn
slePmHistorySeqId=_SlePmHistorySeqId_Object((1,3,6,1,4,1,6296,101,94,4,1,1,1),_SlePmHistorySeqId_Type())
slePmHistorySeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistorySeqId.setStatus(_A)
_SlePmHistoryClassId_Type=PmClassId
_SlePmHistoryClassId_Object=MibTableColumn
slePmHistoryClassId=_SlePmHistoryClassId_Object((1,3,6,1,4,1,6296,101,94,4,1,1,2),_SlePmHistoryClassId_Type())
slePmHistoryClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryClassId.setStatus(_A)
_SlePmHistoryPmId_Type=PmId
_SlePmHistoryPmId_Object=MibTableColumn
slePmHistoryPmId=_SlePmHistoryPmId_Object((1,3,6,1,4,1,6296,101,94,4,1,1,3),_SlePmHistoryPmId_Type())
slePmHistoryPmId.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryPmId.setStatus(_A)
_SlePmHistoryPmSource_Type=PmSrc
_SlePmHistoryPmSource_Object=MibTableColumn
slePmHistoryPmSource=_SlePmHistoryPmSource_Object((1,3,6,1,4,1,6296,101,94,4,1,1,4),_SlePmHistoryPmSource_Type())
slePmHistoryPmSource.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryPmSource.setStatus(_A)
class _SlePmHistoryTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('min15',1),('day1',2)))
_SlePmHistoryTerm_Type.__name__=_E
_SlePmHistoryTerm_Object=MibTableColumn
slePmHistoryTerm=_SlePmHistoryTerm_Object((1,3,6,1,4,1,6296,101,94,4,1,1,5),_SlePmHistoryTerm_Type())
slePmHistoryTerm.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryTerm.setStatus(_A)
class _SlePmHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_SlePmHistoryIndex_Type.__name__=_E
_SlePmHistoryIndex_Object=MibTableColumn
slePmHistoryIndex=_SlePmHistoryIndex_Object((1,3,6,1,4,1,6296,101,94,4,1,1,6),_SlePmHistoryIndex_Type())
slePmHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryIndex.setStatus(_A)
_SlePmHistoryPmCount_Type=Counter64
_SlePmHistoryPmCount_Object=MibTableColumn
slePmHistoryPmCount=_SlePmHistoryPmCount_Object((1,3,6,1,4,1,6296,101,94,4,1,1,7),_SlePmHistoryPmCount_Type())
slePmHistoryPmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryPmCount.setStatus(_A)
_SlePmHistoryAccCount_Type=Counter32
_SlePmHistoryAccCount_Object=MibTableColumn
slePmHistoryAccCount=_SlePmHistoryAccCount_Object((1,3,6,1,4,1,6296,101,94,4,1,1,8),_SlePmHistoryAccCount_Type())
slePmHistoryAccCount.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmHistoryAccCount.setStatus(_A)
_SlePmHistoryStartTime_Type=TimeTicks
_SlePmHistoryStartTime_Object=MibTableColumn
slePmHistoryStartTime=_SlePmHistoryStartTime_Object((1,3,6,1,4,1,6296,101,94,4,1,1,9),_SlePmHistoryStartTime_Type())
slePmHistoryStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryStartTime.setStatus(_A)
_SlePmHistoryControl_ObjectIdentity=ObjectIdentity
slePmHistoryControl=_SlePmHistoryControl_ObjectIdentity((1,3,6,1,4,1,6296,101,94,4,2))
class _SlePmHistoryControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearPmHistory',1))
_SlePmHistoryControlRequest_Type.__name__=_E
_SlePmHistoryControlRequest_Object=MibScalar
slePmHistoryControlRequest=_SlePmHistoryControlRequest_Object((1,3,6,1,4,1,6296,101,94,4,2,1),_SlePmHistoryControlRequest_Type())
slePmHistoryControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmHistoryControlRequest.setStatus(_A)
_SlePmHistoryControlStatus_Type=SleControlStatusType
_SlePmHistoryControlStatus_Object=MibScalar
slePmHistoryControlStatus=_SlePmHistoryControlStatus_Object((1,3,6,1,4,1,6296,101,94,4,2,2),_SlePmHistoryControlStatus_Type())
slePmHistoryControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryControlStatus.setStatus(_A)
_SlePmHistoryControlTimer_Type=Gauge32
_SlePmHistoryControlTimer_Object=MibScalar
slePmHistoryControlTimer=_SlePmHistoryControlTimer_Object((1,3,6,1,4,1,6296,101,94,4,2,3),_SlePmHistoryControlTimer_Type())
slePmHistoryControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:slePmHistoryControlTimer.setStatus(_A)
_SlePmHistoryControlTimeStamp_Type=TimeTicks
_SlePmHistoryControlTimeStamp_Object=MibScalar
slePmHistoryControlTimeStamp=_SlePmHistoryControlTimeStamp_Object((1,3,6,1,4,1,6296,101,94,4,2,4),_SlePmHistoryControlTimeStamp_Type())
slePmHistoryControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryControlTimeStamp.setStatus(_A)
_SlePmHistoryControlReqResult_Type=SleControlRequestResultType
_SlePmHistoryControlReqResult_Object=MibScalar
slePmHistoryControlReqResult=_SlePmHistoryControlReqResult_Object((1,3,6,1,4,1,6296,101,94,4,2,5),_SlePmHistoryControlReqResult_Type())
slePmHistoryControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:slePmHistoryControlReqResult.setStatus(_A)
_SlePmHistoryNotification_ObjectIdentity=ObjectIdentity
slePmHistoryNotification=_SlePmHistoryNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,94,4,3))
slePmConfigTcaEnableChanged=NotificationType((1,3,6,1,4,1,6296,101,94,2,3,1))
slePmConfigTcaEnableChanged.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_T)))
if mibBuilder.loadTexts:slePmConfigTcaEnableChanged.setStatus(_A)
slePmConfigTh15MinChanged=NotificationType((1,3,6,1,4,1,6296,101,94,2,3,2))
slePmConfigTh15MinChanged.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_U)))
if mibBuilder.loadTexts:slePmConfigTh15MinChanged.setStatus(_A)
slePmConfigTh1DayChanged=NotificationType((1,3,6,1,4,1,6296,101,94,2,3,3))
slePmConfigTh1DayChanged.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_V)))
if mibBuilder.loadTexts:slePmConfigTh1DayChanged.setStatus(_A)
slePmCurrentPmCleared=NotificationType((1,3,6,1,4,1,6296,101,94,3,3,1))
slePmCurrentPmCleared.setObjects(*((_C,_F),(_C,_W),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:slePmCurrentPmCleared.setStatus(_A)
slePmHistoryPmCleared=NotificationType((1,3,6,1,4,1,6296,101,94,4,3,1))
slePmHistoryPmCleared.setObjects(*((_C,_F),(_C,_Z),(_C,_a),(_C,_b)))
if mibBuilder.loadTexts:slePmHistoryPmCleared.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PmClassId':PmClassId,'PmId':PmId,'PmSrc':PmSrc,'PmTcaState':PmTcaState,'PmDateTime':PmDateTime,'slePmMgr':slePmMgr,_F:slePmNeId,'slePmConfigBase':slePmConfigBase,'slePmConfigTable':slePmConfigTable,'slePmConfigEntry':slePmConfigEntry,_L:slePmConfigSeqId,'slePmConfigClassId':slePmConfigClassId,'slePmConfigPmId':slePmConfigPmId,'slePmConfigSource':slePmConfigSource,'slePmConfigTcaStat':slePmConfigTcaStat,'slePmConfigTcaEnable':slePmConfigTcaEnable,'slePmConfigTh15Min':slePmConfigTh15Min,'slePmConfigTh1Day':slePmConfigTh1Day,'slePmConfigControl':slePmConfigControl,_G:slePmConfigControlRequest,'slePmConfigControlStatus':slePmConfigControlStatus,'slePmConfigControlTimer':slePmConfigControlTimer,_H:slePmConfigControlTimeStamp,_I:slePmConfigControlReqResult,_J:slePmConfigControlSeqId,_T:slePmConfigControlTcaEnable,_U:slePmConfigControlTh15Min,_V:slePmConfigControlTh1Day,'slePmConfigNotification':slePmConfigNotification,'slePmConfigTcaEnableChanged':slePmConfigTcaEnableChanged,'slePmConfigTh15MinChanged':slePmConfigTh15MinChanged,'slePmConfigTh1DayChanged':slePmConfigTh1DayChanged,'slePmCurrentBase':slePmCurrentBase,'slePmCurrentTable':slePmCurrentTable,'slePmCurrentEntry':slePmCurrentEntry,_O:slePmCurrentSeqId,'slePmCurrentClassId':slePmCurrentClassId,'slePmCurrentPmId':slePmCurrentPmId,'slePmCurrentSource':slePmCurrentSource,_P:slePmCurrentTerm,'slePmCurrentPmCount':slePmCurrentPmCount,'slePmCurrentAccSecond':slePmCurrentAccSecond,'slePmCurrentTcaStat':slePmCurrentTcaStat,'slePmCurrentTcaTime':slePmCurrentTcaTime,'slePmCurrentControl':slePmCurrentControl,_W:slePmCurrentControlRequest,'slePmCurrentControlStatus':slePmCurrentControlStatus,'slePmCurrentControlTimer':slePmCurrentControlTimer,_X:slePmCurrentControlTimeStamp,_Y:slePmCurrentControlReqResult,'slePmCurrentNotification':slePmCurrentNotification,'slePmCurrentPmCleared':slePmCurrentPmCleared,'slePMHistoryBase':slePMHistoryBase,'slePmHistoryTable':slePmHistoryTable,'slePmHistoryEntry':slePmHistoryEntry,_Q:slePmHistorySeqId,'slePmHistoryClassId':slePmHistoryClassId,'slePmHistoryPmId':slePmHistoryPmId,'slePmHistoryPmSource':slePmHistoryPmSource,_R:slePmHistoryTerm,_S:slePmHistoryIndex,'slePmHistoryPmCount':slePmHistoryPmCount,'slePmHistoryAccCount':slePmHistoryAccCount,'slePmHistoryStartTime':slePmHistoryStartTime,'slePmHistoryControl':slePmHistoryControl,_Z:slePmHistoryControlRequest,'slePmHistoryControlStatus':slePmHistoryControlStatus,'slePmHistoryControlTimer':slePmHistoryControlTimer,_a:slePmHistoryControlTimeStamp,_b:slePmHistoryControlReqResult,'slePmHistoryNotification':slePmHistoryNotification,'slePmHistoryPmCleared':slePmHistoryPmCleared})