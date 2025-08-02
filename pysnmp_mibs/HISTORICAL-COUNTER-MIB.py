_G='swHistoryCntPort'
_F='Integer32'
_E='swHistoryCntType'
_D='swHistoryCntTime'
_C='HISTORICAL-COUNTER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
swHistoryCntMIB=ModuleIdentity((1,3,6,1,4,1,171,12,66))
_SwHistoryCntCtrl_ObjectIdentity=ObjectIdentity
swHistoryCntCtrl=_SwHistoryCntCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,66,1))
_SwHistoryCntInfo_ObjectIdentity=ObjectIdentity
swHistoryCntInfo=_SwHistoryCntInfo_ObjectIdentity((1,3,6,1,4,1,171,12,66,2))
_SwHistoricalCounter_ObjectIdentity=ObjectIdentity
swHistoricalCounter=_SwHistoricalCounter_ObjectIdentity((1,3,6,1,4,1,171,12,66,2,1))
_SwHistoryCntPktTable_Object=MibTable
swHistoryCntPktTable=_SwHistoryCntPktTable_Object((1,3,6,1,4,1,171,12,66,2,1,1))
if mibBuilder.loadTexts:swHistoryCntPktTable.setStatus(_A)
_SwHistoryCntPktEntry_Object=MibTableRow
swHistoryCntPktEntry=_SwHistoryCntPktEntry_Object((1,3,6,1,4,1,171,12,66,2,1,1,1))
swHistoryCntPktEntry.setIndexNames((0,_C,_G),(0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:swHistoryCntPktEntry.setStatus(_A)
_SwHistoryCntPort_Type=Integer32
_SwHistoryCntPort_Object=MibTableColumn
swHistoryCntPort=_SwHistoryCntPort_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,1),_SwHistoryCntPort_Type())
swHistoryCntPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntPort.setStatus(_A)
class _SwHistoryCntTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteen-minute',1),('one-day',2)))
_SwHistoryCntTime_Type.__name__=_F
_SwHistoryCntTime_Object=MibTableColumn
swHistoryCntTime=_SwHistoryCntTime_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,2),_SwHistoryCntTime_Type())
swHistoryCntTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntTime.setStatus(_A)
class _SwHistoryCntType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('slot1',1),('slot2',2),('slot3',3),('slot4',4),('slot5',5)))
_SwHistoryCntType_Type.__name__=_F
_SwHistoryCntType_Object=MibTableColumn
swHistoryCntType=_SwHistoryCntType_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,3),_SwHistoryCntType_Type())
swHistoryCntType.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntType.setStatus(_A)
_SwHistoryCntPktsTx_Type=Counter64
_SwHistoryCntPktsTx_Object=MibTableColumn
swHistoryCntPktsTx=_SwHistoryCntPktsTx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,4),_SwHistoryCntPktsTx_Type())
swHistoryCntPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntPktsTx.setStatus(_A)
_SwHistoryCntBytesTx_Type=Counter64
_SwHistoryCntBytesTx_Object=MibTableColumn
swHistoryCntBytesTx=_SwHistoryCntBytesTx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,5),_SwHistoryCntBytesTx_Type())
swHistoryCntBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntBytesTx.setStatus(_A)
_SwHistoryCntPktsRx_Type=Counter64
_SwHistoryCntPktsRx_Object=MibTableColumn
swHistoryCntPktsRx=_SwHistoryCntPktsRx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,6),_SwHistoryCntPktsRx_Type())
swHistoryCntPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntPktsRx.setStatus(_A)
_SwHistoryCntBytesRx_Type=Counter64
_SwHistoryCntBytesRx_Object=MibTableColumn
swHistoryCntBytesRx=_SwHistoryCntBytesRx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,7),_SwHistoryCntBytesRx_Type())
swHistoryCntBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntBytesRx.setStatus(_A)
_SwHistoryCnt64Rx_Type=Counter64
_SwHistoryCnt64Rx_Object=MibTableColumn
swHistoryCnt64Rx=_SwHistoryCnt64Rx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,8),_SwHistoryCnt64Rx_Type())
swHistoryCnt64Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCnt64Rx.setStatus(_A)
_SwHistoryCnt65to127Rx_Type=Counter64
_SwHistoryCnt65to127Rx_Object=MibTableColumn
swHistoryCnt65to127Rx=_SwHistoryCnt65to127Rx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,9),_SwHistoryCnt65to127Rx_Type())
swHistoryCnt65to127Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCnt65to127Rx.setStatus(_A)
_SwHistoryCnt128to255Rx_Type=Counter64
_SwHistoryCnt128to255Rx_Object=MibTableColumn
swHistoryCnt128to255Rx=_SwHistoryCnt128to255Rx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,10),_SwHistoryCnt128to255Rx_Type())
swHistoryCnt128to255Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCnt128to255Rx.setStatus(_A)
_SwHistoryCnt256to511Rx_Type=Counter64
_SwHistoryCnt256to511Rx_Object=MibTableColumn
swHistoryCnt256to511Rx=_SwHistoryCnt256to511Rx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,11),_SwHistoryCnt256to511Rx_Type())
swHistoryCnt256to511Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCnt256to511Rx.setStatus(_A)
_SwHistoryCnt512to1023Rx_Type=Counter64
_SwHistoryCnt512to1023Rx_Object=MibTableColumn
swHistoryCnt512to1023Rx=_SwHistoryCnt512to1023Rx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,12),_SwHistoryCnt512to1023Rx_Type())
swHistoryCnt512to1023Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCnt512to1023Rx.setStatus(_A)
_SwHistoryCnt1024to1518Rx_Type=Counter64
_SwHistoryCnt1024to1518Rx_Object=MibTableColumn
swHistoryCnt1024to1518Rx=_SwHistoryCnt1024to1518Rx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,13),_SwHistoryCnt1024to1518Rx_Type())
swHistoryCnt1024to1518Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCnt1024to1518Rx.setStatus(_A)
_SwHistoryCntUnicastRx_Type=Counter64
_SwHistoryCntUnicastRx_Object=MibTableColumn
swHistoryCntUnicastRx=_SwHistoryCntUnicastRx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,14),_SwHistoryCntUnicastRx_Type())
swHistoryCntUnicastRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntUnicastRx.setStatus(_A)
_SwHistoryCntMulticastRx_Type=Counter64
_SwHistoryCntMulticastRx_Object=MibTableColumn
swHistoryCntMulticastRx=_SwHistoryCntMulticastRx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,15),_SwHistoryCntMulticastRx_Type())
swHistoryCntMulticastRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntMulticastRx.setStatus(_A)
_SwHistoryCntBroadcastRx_Type=Counter64
_SwHistoryCntBroadcastRx_Object=MibTableColumn
swHistoryCntBroadcastRx=_SwHistoryCntBroadcastRx_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,16),_SwHistoryCntBroadcastRx_Type())
swHistoryCntBroadcastRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntBroadcastRx.setStatus(_A)
_SwHistoryCntStartTime_Type=DateAndTime
_SwHistoryCntStartTime_Object=MibTableColumn
swHistoryCntStartTime=_SwHistoryCntStartTime_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,17),_SwHistoryCntStartTime_Type())
swHistoryCntStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntStartTime.setStatus(_A)
_SwHistoryCntEndTime_Type=DateAndTime
_SwHistoryCntEndTime_Object=MibTableColumn
swHistoryCntEndTime=_SwHistoryCntEndTime_Object((1,3,6,1,4,1,171,12,66,2,1,1,1,18),_SwHistoryCntEndTime_Type())
swHistoryCntEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntEndTime.setStatus(_A)
_SwHistoryCntErrTable_Object=MibTable
swHistoryCntErrTable=_SwHistoryCntErrTable_Object((1,3,6,1,4,1,171,12,66,2,1,2))
if mibBuilder.loadTexts:swHistoryCntErrTable.setStatus(_A)
_SwHistoryCntErrEntry_Object=MibTableRow
swHistoryCntErrEntry=_SwHistoryCntErrEntry_Object((1,3,6,1,4,1,171,12,66,2,1,2,1))
swHistoryCntErrEntry.setIndexNames((0,_C,_G),(0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:swHistoryCntErrEntry.setStatus(_A)
_SwHistoryCntFragmentRx_Type=Counter64
_SwHistoryCntFragmentRx_Object=MibTableColumn
swHistoryCntFragmentRx=_SwHistoryCntFragmentRx_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,1),_SwHistoryCntFragmentRx_Type())
swHistoryCntFragmentRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntFragmentRx.setStatus(_A)
_SwHistoryCntJabberPktsRx_Type=Counter64
_SwHistoryCntJabberPktsRx_Object=MibTableColumn
swHistoryCntJabberPktsRx=_SwHistoryCntJabberPktsRx_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,2),_SwHistoryCntJabberPktsRx_Type())
swHistoryCntJabberPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntJabberPktsRx.setStatus(_A)
_SwHistoryCntOversizePktsRx_Type=Counter64
_SwHistoryCntOversizePktsRx_Object=MibTableColumn
swHistoryCntOversizePktsRx=_SwHistoryCntOversizePktsRx_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,3),_SwHistoryCntOversizePktsRx_Type())
swHistoryCntOversizePktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntOversizePktsRx.setStatus(_A)
_SwHistoryCntUndersizePktsRx_Type=Counter64
_SwHistoryCntUndersizePktsRx_Object=MibTableColumn
swHistoryCntUndersizePktsRx=_SwHistoryCntUndersizePktsRx_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,4),_SwHistoryCntUndersizePktsRx_Type())
swHistoryCntUndersizePktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntUndersizePktsRx.setStatus(_A)
_SwHistoryCntAlignmentErrorsRx_Type=Counter64
_SwHistoryCntAlignmentErrorsRx_Object=MibTableColumn
swHistoryCntAlignmentErrorsRx=_SwHistoryCntAlignmentErrorsRx_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,5),_SwHistoryCntAlignmentErrorsRx_Type())
swHistoryCntAlignmentErrorsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntAlignmentErrorsRx.setStatus(_A)
_SwHistoryCntUnknownCtrlPktsRx_Type=Counter64
_SwHistoryCntUnknownCtrlPktsRx_Object=MibTableColumn
swHistoryCntUnknownCtrlPktsRx=_SwHistoryCntUnknownCtrlPktsRx_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,6),_SwHistoryCntUnknownCtrlPktsRx_Type())
swHistoryCntUnknownCtrlPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntUnknownCtrlPktsRx.setStatus(_A)
_SwHistoryCntCollisionTx_Type=Counter64
_SwHistoryCntCollisionTx_Object=MibTableColumn
swHistoryCntCollisionTx=_SwHistoryCntCollisionTx_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,7),_SwHistoryCntCollisionTx_Type())
swHistoryCntCollisionTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntCollisionTx.setStatus(_A)
_SwHistoryCntDropedPkts_Type=Counter64
_SwHistoryCntDropedPkts_Object=MibTableColumn
swHistoryCntDropedPkts=_SwHistoryCntDropedPkts_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,8),_SwHistoryCntDropedPkts_Type())
swHistoryCntDropedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntDropedPkts.setStatus(_A)
_SwHistoryCntErrStartTime_Type=DateAndTime
_SwHistoryCntErrStartTime_Object=MibTableColumn
swHistoryCntErrStartTime=_SwHistoryCntErrStartTime_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,9),_SwHistoryCntErrStartTime_Type())
swHistoryCntErrStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntErrStartTime.setStatus(_A)
_SwHistoryCntErrEndTime_Type=DateAndTime
_SwHistoryCntErrEndTime_Object=MibTableColumn
swHistoryCntErrEndTime=_SwHistoryCntErrEndTime_Object((1,3,6,1,4,1,171,12,66,2,1,2,1,10),_SwHistoryCntErrEndTime_Type())
swHistoryCntErrEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryCntErrEndTime.setStatus(_A)
_SwHistoricalUtilization_ObjectIdentity=ObjectIdentity
swHistoricalUtilization=_SwHistoricalUtilization_ObjectIdentity((1,3,6,1,4,1,171,12,66,2,2))
_SwHistoryUtilTable_Object=MibTable
swHistoryUtilTable=_SwHistoryUtilTable_Object((1,3,6,1,4,1,171,12,66,2,2,1))
if mibBuilder.loadTexts:swHistoryUtilTable.setStatus(_A)
_SwHistoryUtilEntry_Object=MibTableRow
swHistoryUtilEntry=_SwHistoryUtilEntry_Object((1,3,6,1,4,1,171,12,66,2,2,1,1))
swHistoryUtilEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:swHistoryUtilEntry.setStatus(_A)
_SwHistoryUtilCPU_Type=Integer32
_SwHistoryUtilCPU_Object=MibTableColumn
swHistoryUtilCPU=_SwHistoryUtilCPU_Object((1,3,6,1,4,1,171,12,66,2,2,1,1,1),_SwHistoryUtilCPU_Type())
swHistoryUtilCPU.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryUtilCPU.setStatus(_A)
_SwHistoryUtilMemory_Type=Integer32
_SwHistoryUtilMemory_Object=MibTableColumn
swHistoryUtilMemory=_SwHistoryUtilMemory_Object((1,3,6,1,4,1,171,12,66,2,2,1,1,2),_SwHistoryUtilMemory_Type())
swHistoryUtilMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryUtilMemory.setStatus(_A)
_SwHistoryUtilStartTime_Type=DateAndTime
_SwHistoryUtilStartTime_Object=MibTableColumn
swHistoryUtilStartTime=_SwHistoryUtilStartTime_Object((1,3,6,1,4,1,171,12,66,2,2,1,1,3),_SwHistoryUtilStartTime_Type())
swHistoryUtilStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryUtilStartTime.setStatus(_A)
_SwHistoryUtilEndTime_Type=DateAndTime
_SwHistoryUtilEndTime_Object=MibTableColumn
swHistoryUtilEndTime=_SwHistoryUtilEndTime_Object((1,3,6,1,4,1,171,12,66,2,2,1,1,4),_SwHistoryUtilEndTime_Type())
swHistoryUtilEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swHistoryUtilEndTime.setStatus(_A)
_SwHistoryCntMgmt_ObjectIdentity=ObjectIdentity
swHistoryCntMgmt=_SwHistoryCntMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,66,3))
mibBuilder.exportSymbols(_C,**{'swHistoryCntMIB':swHistoryCntMIB,'swHistoryCntCtrl':swHistoryCntCtrl,'swHistoryCntInfo':swHistoryCntInfo,'swHistoricalCounter':swHistoricalCounter,'swHistoryCntPktTable':swHistoryCntPktTable,'swHistoryCntPktEntry':swHistoryCntPktEntry,_G:swHistoryCntPort,_D:swHistoryCntTime,_E:swHistoryCntType,'swHistoryCntPktsTx':swHistoryCntPktsTx,'swHistoryCntBytesTx':swHistoryCntBytesTx,'swHistoryCntPktsRx':swHistoryCntPktsRx,'swHistoryCntBytesRx':swHistoryCntBytesRx,'swHistoryCnt64Rx':swHistoryCnt64Rx,'swHistoryCnt65to127Rx':swHistoryCnt65to127Rx,'swHistoryCnt128to255Rx':swHistoryCnt128to255Rx,'swHistoryCnt256to511Rx':swHistoryCnt256to511Rx,'swHistoryCnt512to1023Rx':swHistoryCnt512to1023Rx,'swHistoryCnt1024to1518Rx':swHistoryCnt1024to1518Rx,'swHistoryCntUnicastRx':swHistoryCntUnicastRx,'swHistoryCntMulticastRx':swHistoryCntMulticastRx,'swHistoryCntBroadcastRx':swHistoryCntBroadcastRx,'swHistoryCntStartTime':swHistoryCntStartTime,'swHistoryCntEndTime':swHistoryCntEndTime,'swHistoryCntErrTable':swHistoryCntErrTable,'swHistoryCntErrEntry':swHistoryCntErrEntry,'swHistoryCntFragmentRx':swHistoryCntFragmentRx,'swHistoryCntJabberPktsRx':swHistoryCntJabberPktsRx,'swHistoryCntOversizePktsRx':swHistoryCntOversizePktsRx,'swHistoryCntUndersizePktsRx':swHistoryCntUndersizePktsRx,'swHistoryCntAlignmentErrorsRx':swHistoryCntAlignmentErrorsRx,'swHistoryCntUnknownCtrlPktsRx':swHistoryCntUnknownCtrlPktsRx,'swHistoryCntCollisionTx':swHistoryCntCollisionTx,'swHistoryCntDropedPkts':swHistoryCntDropedPkts,'swHistoryCntErrStartTime':swHistoryCntErrStartTime,'swHistoryCntErrEndTime':swHistoryCntErrEndTime,'swHistoricalUtilization':swHistoricalUtilization,'swHistoryUtilTable':swHistoryUtilTable,'swHistoryUtilEntry':swHistoryUtilEntry,'swHistoryUtilCPU':swHistoryUtilCPU,'swHistoryUtilMemory':swHistoryUtilMemory,'swHistoryUtilStartTime':swHistoryUtilStartTime,'swHistoryUtilEndTime':swHistoryUtilEndTime,'swHistoryCntMgmt':swHistoryCntMgmt})