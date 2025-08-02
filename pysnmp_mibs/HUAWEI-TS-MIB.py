_T='tsAsyModeTtyVtyState'
_S='tsAppTtyServerState'
_R='tsTtyManageUnixIndex'
_Q='tsTtyID'
_P='DisplayString'
_O='NotificationType'
_N='none'
_M='tsAsyModeTtyVtyID'
_L='tsAsyModeTtyID'
_K='clear'
_J='tsAppID'
_I='write-only'
_H='current'
_G='disable'
_F='enable'
_E='HUAWEI-TS-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huawei,mlsr=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','huawei','mlsr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_O,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_O,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention')
class EntryStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_TerminalServer_ObjectIdentity=ObjectIdentity
terminalServer=_TerminalServer_ObjectIdentity((1,3,6,1,4,1,2011,2,33,1))
_TsAppTable_Object=MibTable
tsAppTable=_TsAppTable_Object((1,3,6,1,4,1,2011,2,33,1,1))
if mibBuilder.loadTexts:tsAppTable.setStatus(_A)
_TsAppEntry_Object=MibTableRow
tsAppEntry=_TsAppEntry_Object((1,3,6,1,4,1,2011,2,33,1,1,1))
tsAppEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:tsAppEntry.setStatus(_A)
class _TsAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,515))
_TsAppID_Type.__name__=_B
_TsAppID_Object=MibTableColumn
tsAppID=_TsAppID_Object((1,3,6,1,4,1,2011,2,33,1,1,1,1),_TsAppID_Type())
tsAppID.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppID.setStatus(_A)
_TsAppIPAddress_Type=IpAddress
_TsAppIPAddress_Object=MibTableColumn
tsAppIPAddress=_TsAppIPAddress_Object((1,3,6,1,4,1,2011,2,33,1,1,1,2),_TsAppIPAddress_Type())
tsAppIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAppIPAddress.setStatus(_A)
class _TsAppPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1025,65535))
_TsAppPort_Type.__name__=_B
_TsAppPort_Object=MibTableColumn
tsAppPort=_TsAppPort_Object((1,3,6,1,4,1,2011,2,33,1,1,1,3),_TsAppPort_Type())
tsAppPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAppPort.setStatus(_A)
class _TsAppType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('special',2)))
_TsAppType_Type.__name__=_B
_TsAppType_Object=MibTableColumn
tsAppType=_TsAppType_Object((1,3,6,1,4,1,2011,2,33,1,1,1,4),_TsAppType_Type())
tsAppType.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAppType.setStatus(_A)
class _TsAppName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_TsAppName_Type.__name__=_P
_TsAppName_Object=MibTableColumn
tsAppName=_TsAppName_Object((1,3,6,1,4,1,2011,2,33,1,1,1,5),_TsAppName_Type())
tsAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAppName.setStatus(_A)
_TsAppSourceIP_Type=IpAddress
_TsAppSourceIP_Object=MibTableColumn
tsAppSourceIP=_TsAppSourceIP_Object((1,3,6,1,4,1,2011,2,33,1,1,1,6),_TsAppSourceIP_Type())
tsAppSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAppSourceIP.setStatus(_A)
class _TsAppLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535),ValueRangeConstraint(0,0))
_TsAppLocalPort_Type.__name__=_B
_TsAppLocalPort_Object=MibTableColumn
tsAppLocalPort=_TsAppLocalPort_Object((1,3,6,1,4,1,2011,2,33,1,1,1,7),_TsAppLocalPort_Type())
tsAppLocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppLocalPort.setStatus(_A)
class _TsAppTtyServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noset',1),('kept',2),('linking',3),('linked',4),('removed',5),('overcast',6)))
_TsAppTtyServerState_Type.__name__=_B
_TsAppTtyServerState_Object=MibTableColumn
tsAppTtyServerState=_TsAppTtyServerState_Object((1,3,6,1,4,1,2011,2,33,1,1,1,8),_TsAppTtyServerState_Type())
tsAppTtyServerState.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppTtyServerState.setStatus(_A)
_TsAppSocketRecvBufSize_Type=Integer32
_TsAppSocketRecvBufSize_Object=MibTableColumn
tsAppSocketRecvBufSize=_TsAppSocketRecvBufSize_Object((1,3,6,1,4,1,2011,2,33,1,1,1,9),_TsAppSocketRecvBufSize_Type())
tsAppSocketRecvBufSize.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppSocketRecvBufSize.setStatus(_A)
_TsAppSocketSendBufSize_Type=Integer32
_TsAppSocketSendBufSize_Object=MibTableColumn
tsAppSocketSendBufSize=_TsAppSocketSendBufSize_Object((1,3,6,1,4,1,2011,2,33,1,1,1,10),_TsAppSocketSendBufSize_Type())
tsAppSocketSendBufSize.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppSocketSendBufSize.setStatus(_A)
_TsAppSockRecvByte_Type=Integer32
_TsAppSockRecvByte_Object=MibTableColumn
tsAppSockRecvByte=_TsAppSockRecvByte_Object((1,3,6,1,4,1,2011,2,33,1,1,1,11),_TsAppSockRecvByte_Type())
tsAppSockRecvByte.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppSockRecvByte.setStatus(_A)
_TsAppSockSendByte_Type=Integer32
_TsAppSockSendByte_Object=MibTableColumn
tsAppSockSendByte=_TsAppSockSendByte_Object((1,3,6,1,4,1,2011,2,33,1,1,1,12),_TsAppSockSendByte_Type())
tsAppSockSendByte.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppSockSendByte.setStatus(_A)
_TsAppLastRecvTime_Type=DisplayString
_TsAppLastRecvTime_Object=MibTableColumn
tsAppLastRecvTime=_TsAppLastRecvTime_Object((1,3,6,1,4,1,2011,2,33,1,1,1,13),_TsAppLastRecvTime_Type())
tsAppLastRecvTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppLastRecvTime.setStatus(_A)
_TsAppLastSendTime_Type=DisplayString
_TsAppLastSendTime_Object=MibTableColumn
tsAppLastSendTime=_TsAppLastSendTime_Object((1,3,6,1,4,1,2011,2,33,1,1,1,14),_TsAppLastSendTime_Type())
tsAppLastSendTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppLastSendTime.setStatus(_A)
class _TsAppClearStatistic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_TsAppClearStatistic_Type.__name__=_B
_TsAppClearStatistic_Object=MibTableColumn
tsAppClearStatistic=_TsAppClearStatistic_Object((1,3,6,1,4,1,2011,2,33,1,1,1,15),_TsAppClearStatistic_Type())
tsAppClearStatistic.setMaxAccess(_I)
if mibBuilder.loadTexts:tsAppClearStatistic.setStatus(_A)
class _TsAppUnixIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_TsAppUnixIndex_Type.__name__=_B
_TsAppUnixIndex_Object=MibTableColumn
tsAppUnixIndex=_TsAppUnixIndex_Object((1,3,6,1,4,1,2011,2,33,1,1,1,16),_TsAppUnixIndex_Type())
tsAppUnixIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAppUnixIndex.setStatus(_A)
_TsAppStatus_Type=EntryStatus
_TsAppStatus_Object=MibTableColumn
tsAppStatus=_TsAppStatus_Object((1,3,6,1,4,1,2011,2,33,1,1,1,17),_TsAppStatus_Type())
tsAppStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAppStatus.setStatus(_A)
_TsAsyModeTtyTable_Object=MibTable
tsAsyModeTtyTable=_TsAsyModeTtyTable_Object((1,3,6,1,4,1,2011,2,33,1,2))
if mibBuilder.loadTexts:tsAsyModeTtyTable.setStatus(_A)
_TsAsyModeTtyEntry_Object=MibTableRow
tsAsyModeTtyEntry=_TsAsyModeTtyEntry_Object((1,3,6,1,4,1,2011,2,33,1,2,1))
tsAsyModeTtyEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:tsAsyModeTtyEntry.setStatus(_A)
class _TsAsyModeTtyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TsAsyModeTtyID_Type.__name__=_B
_TsAsyModeTtyID_Object=MibTableColumn
tsAsyModeTtyID=_TsAsyModeTtyID_Object((1,3,6,1,4,1,2011,2,33,1,2,1,1),_TsAsyModeTtyID_Type())
tsAsyModeTtyID.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAsyModeTtyID.setStatus(_A)
class _TsAsyModeTtyVtyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_TsAsyModeTtyVtyID_Type.__name__=_B
_TsAsyModeTtyVtyID_Object=MibTableColumn
tsAsyModeTtyVtyID=_TsAsyModeTtyVtyID_Object((1,3,6,1,4,1,2011,2,33,1,2,1,2),_TsAsyModeTtyVtyID_Type())
tsAsyModeTtyVtyID.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAsyModeTtyVtyID.setStatus(_A)
_TsAsyModeTtyIFIndex_Type=Integer32
_TsAsyModeTtyIFIndex_Object=MibTableColumn
tsAsyModeTtyIFIndex=_TsAsyModeTtyIFIndex_Object((1,3,6,1,4,1,2011,2,33,1,2,1,3),_TsAsyModeTtyIFIndex_Type())
tsAsyModeTtyIFIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAsyModeTtyIFIndex.setStatus(_A)
class _TsAsyModeTtyAppID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,515))
_TsAsyModeTtyAppID_Type.__name__=_B
_TsAsyModeTtyAppID_Object=MibTableColumn
tsAsyModeTtyAppID=_TsAsyModeTtyAppID_Object((1,3,6,1,4,1,2011,2,33,1,2,1,4),_TsAsyModeTtyAppID_Type())
tsAsyModeTtyAppID.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAsyModeTtyAppID.setStatus(_A)
class _TsAsyModeTtyDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('disconnect',1))
_TsAsyModeTtyDisconnect_Type.__name__=_B
_TsAsyModeTtyDisconnect_Object=MibTableColumn
tsAsyModeTtyDisconnect=_TsAsyModeTtyDisconnect_Object((1,3,6,1,4,1,2011,2,33,1,2,1,5),_TsAsyModeTtyDisconnect_Type())
tsAsyModeTtyDisconnect.setMaxAccess(_I)
if mibBuilder.loadTexts:tsAsyModeTtyDisconnect.setStatus(_A)
class _TsAsyModeTtyVtyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('down',1),('up',2),('waitaaa',3),('ok',4),('menu',5)))
_TsAsyModeTtyVtyState_Type.__name__=_B
_TsAsyModeTtyVtyState_Object=MibTableColumn
tsAsyModeTtyVtyState=_TsAsyModeTtyVtyState_Object((1,3,6,1,4,1,2011,2,33,1,2,1,6),_TsAsyModeTtyVtyState_Type())
tsAsyModeTtyVtyState.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAsyModeTtyVtyState.setStatus(_A)
class _TsAsyModeTtyFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_TsAsyModeTtyFlowCtrlState_Type.__name__=_B
_TsAsyModeTtyFlowCtrlState_Object=MibTableColumn
tsAsyModeTtyFlowCtrlState=_TsAsyModeTtyFlowCtrlState_Object((1,3,6,1,4,1,2011,2,33,1,2,1,7),_TsAsyModeTtyFlowCtrlState_Type())
tsAsyModeTtyFlowCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:tsAsyModeTtyFlowCtrlState.setStatus(_A)
_TsAsyModeTtyStatus_Type=EntryStatus
_TsAsyModeTtyStatus_Object=MibTableColumn
tsAsyModeTtyStatus=_TsAsyModeTtyStatus_Object((1,3,6,1,4,1,2011,2,33,1,2,1,8),_TsAsyModeTtyStatus_Type())
tsAsyModeTtyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tsAsyModeTtyStatus.setStatus(_A)
_TsTtyTable_Object=MibTable
tsTtyTable=_TsTtyTable_Object((1,3,6,1,4,1,2011,2,33,1,3))
if mibBuilder.loadTexts:tsTtyTable.setStatus(_A)
_TsTtyEntry_Object=MibTableRow
tsTtyEntry=_TsTtyEntry_Object((1,3,6,1,4,1,2011,2,33,1,3,1))
tsTtyEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:tsTtyEntry.setStatus(_A)
class _TsTtyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TsTtyID_Type.__name__=_B
_TsTtyID_Object=MibTableColumn
tsTtyID=_TsTtyID_Object((1,3,6,1,4,1,2011,2,33,1,3,1,1),_TsTtyID_Type())
tsTtyID.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyID.setStatus(_A)
class _TsTtyBufferSize_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,204800))
_TsTtyBufferSize_Type.__name__=_B
_TsTtyBufferSize_Object=MibTableColumn
tsTtyBufferSize=_TsTtyBufferSize_Object((1,3,6,1,4,1,2011,2,33,1,3,1,2),_TsTtyBufferSize_Type())
tsTtyBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyBufferSize.setStatus(_A)
class _TsTtyAutoLink_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,3600))
_TsTtyAutoLink_Type.__name__=_B
_TsTtyAutoLink_Object=MibTableColumn
tsTtyAutoLink=_TsTtyAutoLink_Object((1,3,6,1,4,1,2011,2,33,1,3,1,3),_TsTtyAutoLink_Type())
tsTtyAutoLink.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyAutoLink.setStatus(_A)
class _TsTtyCloseLink_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,3600))
_TsTtyCloseLink_Type.__name__=_B
_TsTtyCloseLink_Object=MibTableColumn
tsTtyCloseLink=_TsTtyCloseLink_Object((1,3,6,1,4,1,2011,2,33,1,3,1,4),_TsTtyCloseLink_Type())
tsTtyCloseLink.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyCloseLink.setStatus(_A)
class _TsTtyConnPrint_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('english',1),('chinese',2),(_N,3)))
_TsTtyConnPrint_Type.__name__=_B
_TsTtyConnPrint_Object=MibTableColumn
tsTtyConnPrint=_TsTtyConnPrint_Object((1,3,6,1,4,1,2011,2,33,1,3,1,5),_TsTtyConnPrint_Type())
tsTtyConnPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyConnPrint.setStatus(_A)
class _TsTtyDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1200))
_TsTtyDelay_Type.__name__=_B
_TsTtyDelay_Object=MibTableColumn
tsTtyDelay=_TsTtyDelay_Object((1,3,6,1,4,1,2011,2,33,1,3,1,6),_TsTtyDelay_Type())
tsTtyDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyDelay.setStatus(_A)
class _TsTtyLogoPrint_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsTtyLogoPrint_Type.__name__=_B
_TsTtyLogoPrint_Object=MibTableColumn
tsTtyLogoPrint=_TsTtyLogoPrint_Object((1,3,6,1,4,1,2011,2,33,1,3,1,7),_TsTtyLogoPrint_Type())
tsTtyLogoPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyLogoPrint.setStatus(_A)
class _TsTtyMenuKey1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyMenuKey1_Type.__name__=_B
_TsTtyMenuKey1_Object=MibTableColumn
tsTtyMenuKey1=_TsTtyMenuKey1_Object((1,3,6,1,4,1,2011,2,33,1,3,1,8),_TsTtyMenuKey1_Type())
tsTtyMenuKey1.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyMenuKey1.setStatus(_A)
class _TsTtyMenuKey2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyMenuKey2_Type.__name__=_B
_TsTtyMenuKey2_Object=MibTableColumn
tsTtyMenuKey2=_TsTtyMenuKey2_Object((1,3,6,1,4,1,2011,2,33,1,3,1,9),_TsTtyMenuKey2_Type())
tsTtyMenuKey2.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyMenuKey2.setStatus(_A)
class _TsTtyMenuKey3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyMenuKey3_Type.__name__=_B
_TsTtyMenuKey3_Object=MibTableColumn
tsTtyMenuKey3=_TsTtyMenuKey3_Object((1,3,6,1,4,1,2011,2,33,1,3,1,10),_TsTtyMenuKey3_Type())
tsTtyMenuKey3.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyMenuKey3.setStatus(_A)
class _TsTtyReadBlock_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('noSet',2)))
_TsTtyReadBlock_Type.__name__=_B
_TsTtyReadBlock_Object=MibTableColumn
tsTtyReadBlock=_TsTtyReadBlock_Object((1,3,6,1,4,1,2011,2,33,1,3,1,11),_TsTtyReadBlock_Type())
tsTtyReadBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyReadBlock.setStatus(_A)
class _TsTtyRedrawkey1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyRedrawkey1_Type.__name__=_B
_TsTtyRedrawkey1_Object=MibTableColumn
tsTtyRedrawkey1=_TsTtyRedrawkey1_Object((1,3,6,1,4,1,2011,2,33,1,3,1,12),_TsTtyRedrawkey1_Type())
tsTtyRedrawkey1.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyRedrawkey1.setStatus(_A)
class _TsTtyRedrawkey2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyRedrawkey2_Type.__name__=_B
_TsTtyRedrawkey2_Object=MibTableColumn
tsTtyRedrawkey2=_TsTtyRedrawkey2_Object((1,3,6,1,4,1,2011,2,33,1,3,1,13),_TsTtyRedrawkey2_Type())
tsTtyRedrawkey2.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyRedrawkey2.setStatus(_A)
class _TsTtyRedrawkey3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyRedrawkey3_Type.__name__=_B
_TsTtyRedrawkey3_Object=MibTableColumn
tsTtyRedrawkey3=_TsTtyRedrawkey3_Object((1,3,6,1,4,1,2011,2,33,1,3,1,14),_TsTtyRedrawkey3_Type())
tsTtyRedrawkey3.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyRedrawkey3.setStatus(_A)
class _TsTtyResetKey1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyResetKey1_Type.__name__=_B
_TsTtyResetKey1_Object=MibTableColumn
tsTtyResetKey1=_TsTtyResetKey1_Object((1,3,6,1,4,1,2011,2,33,1,3,1,15),_TsTtyResetKey1_Type())
tsTtyResetKey1.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyResetKey1.setStatus(_A)
class _TsTtyResetKey2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyResetKey2_Type.__name__=_B
_TsTtyResetKey2_Object=MibTableColumn
tsTtyResetKey2=_TsTtyResetKey2_Object((1,3,6,1,4,1,2011,2,33,1,3,1,16),_TsTtyResetKey2_Type())
tsTtyResetKey2.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyResetKey2.setStatus(_A)
class _TsTtyResetKey3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyResetKey3_Type.__name__=_B
_TsTtyResetKey3_Object=MibTableColumn
tsTtyResetKey3=_TsTtyResetKey3_Object((1,3,6,1,4,1,2011,2,33,1,3,1,17),_TsTtyResetKey3_Type())
tsTtyResetKey3.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyResetKey3.setStatus(_A)
class _TsTtyTcpNoDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsTtyTcpNoDelay_Type.__name__=_B
_TsTtyTcpNoDelay_Object=MibTableColumn
tsTtyTcpNoDelay=_TsTtyTcpNoDelay_Object((1,3,6,1,4,1,2011,2,33,1,3,1,18),_TsTtyTcpNoDelay_Type())
tsTtyTcpNoDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyTcpNoDelay.setStatus(_A)
class _TsTtyTcpRecvBufferSize_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16384))
_TsTtyTcpRecvBufferSize_Type.__name__=_B
_TsTtyTcpRecvBufferSize_Object=MibTableColumn
tsTtyTcpRecvBufferSize=_TsTtyTcpRecvBufferSize_Object((1,3,6,1,4,1,2011,2,33,1,3,1,19),_TsTtyTcpRecvBufferSize_Type())
tsTtyTcpRecvBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyTcpRecvBufferSize.setStatus(_A)
class _TsTtyTcpSendBufferSize_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16384))
_TsTtyTcpSendBufferSize_Type.__name__=_B
_TsTtyTcpSendBufferSize_Object=MibTableColumn
tsTtyTcpSendBufferSize=_TsTtyTcpSendBufferSize_Object((1,3,6,1,4,1,2011,2,33,1,3,1,20),_TsTtyTcpSendBufferSize_Type())
tsTtyTcpSendBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyTcpSendBufferSize.setStatus(_A)
class _TsTtyTestKey1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyTestKey1_Type.__name__=_B
_TsTtyTestKey1_Object=MibTableColumn
tsTtyTestKey1=_TsTtyTestKey1_Object((1,3,6,1,4,1,2011,2,33,1,3,1,21),_TsTtyTestKey1_Type())
tsTtyTestKey1.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyTestKey1.setStatus(_A)
class _TsTtyTestKey2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyTestKey2_Type.__name__=_B
_TsTtyTestKey2_Object=MibTableColumn
tsTtyTestKey2=_TsTtyTestKey2_Object((1,3,6,1,4,1,2011,2,33,1,3,1,22),_TsTtyTestKey2_Type())
tsTtyTestKey2.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyTestKey2.setStatus(_A)
class _TsTtyTestKey3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_TsTtyTestKey3_Type.__name__=_B
_TsTtyTestKey3_Object=MibTableColumn
tsTtyTestKey3=_TsTtyTestKey3_Object((1,3,6,1,4,1,2011,2,33,1,3,1,23),_TsTtyTestKey3_Type())
tsTtyTestKey3.setMaxAccess(_C)
if mibBuilder.loadTexts:tsTtyTestKey3.setStatus(_A)
class _TsTtyBufferRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TsTtyBufferRate_Type.__name__=_B
_TsTtyBufferRate_Object=MibTableColumn
tsTtyBufferRate=_TsTtyBufferRate_Object((1,3,6,1,4,1,2011,2,33,1,3,1,24),_TsTtyBufferRate_Type())
tsTtyBufferRate.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyBufferRate.setStatus(_A)
_TsTtyRecvBytes_Type=Integer32
_TsTtyRecvBytes_Object=MibTableColumn
tsTtyRecvBytes=_TsTtyRecvBytes_Object((1,3,6,1,4,1,2011,2,33,1,3,1,25),_TsTtyRecvBytes_Type())
tsTtyRecvBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyRecvBytes.setStatus(_A)
_TsTtySendBytes_Type=Integer32
_TsTtySendBytes_Object=MibTableColumn
tsTtySendBytes=_TsTtySendBytes_Object((1,3,6,1,4,1,2011,2,33,1,3,1,26),_TsTtySendBytes_Type())
tsTtySendBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtySendBytes.setStatus(_A)
_TsTtyLastRecvTime_Type=DisplayString
_TsTtyLastRecvTime_Object=MibTableColumn
tsTtyLastRecvTime=_TsTtyLastRecvTime_Object((1,3,6,1,4,1,2011,2,33,1,3,1,27),_TsTtyLastRecvTime_Type())
tsTtyLastRecvTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyLastRecvTime.setStatus(_A)
_TsTtyLastSendTime_Type=DisplayString
_TsTtyLastSendTime_Object=MibTableColumn
tsTtyLastSendTime=_TsTtyLastSendTime_Object((1,3,6,1,4,1,2011,2,33,1,3,1,28),_TsTtyLastSendTime_Type())
tsTtyLastSendTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyLastSendTime.setStatus(_A)
_TsTtyCurrentVtyID_Type=Integer32
_TsTtyCurrentVtyID_Object=MibTableColumn
tsTtyCurrentVtyID=_TsTtyCurrentVtyID_Object((1,3,6,1,4,1,2011,2,33,1,3,1,29),_TsTtyCurrentVtyID_Type())
tsTtyCurrentVtyID.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyCurrentVtyID.setStatus(_A)
_TsTtyCurrentVtyRecv_Type=Integer32
_TsTtyCurrentVtyRecv_Object=MibTableColumn
tsTtyCurrentVtyRecv=_TsTtyCurrentVtyRecv_Object((1,3,6,1,4,1,2011,2,33,1,3,1,30),_TsTtyCurrentVtyRecv_Type())
tsTtyCurrentVtyRecv.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyCurrentVtyRecv.setStatus(_A)
_TsTtyCurrentVtySend_Type=Integer32
_TsTtyCurrentVtySend_Object=MibTableColumn
tsTtyCurrentVtySend=_TsTtyCurrentVtySend_Object((1,3,6,1,4,1,2011,2,33,1,3,1,31),_TsTtyCurrentVtySend_Type())
tsTtyCurrentVtySend.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyCurrentVtySend.setStatus(_A)
_TsTtyCurrentAppID_Type=Integer32
_TsTtyCurrentAppID_Object=MibTableColumn
tsTtyCurrentAppID=_TsTtyCurrentAppID_Object((1,3,6,1,4,1,2011,2,33,1,3,1,32),_TsTtyCurrentAppID_Type())
tsTtyCurrentAppID.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyCurrentAppID.setStatus(_A)
_TsTtyCurrentAppRecv_Type=Integer32
_TsTtyCurrentAppRecv_Object=MibTableColumn
tsTtyCurrentAppRecv=_TsTtyCurrentAppRecv_Object((1,3,6,1,4,1,2011,2,33,1,3,1,33),_TsTtyCurrentAppRecv_Type())
tsTtyCurrentAppRecv.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyCurrentAppRecv.setStatus(_A)
_TsTtyCurrentAppSend_Type=Integer32
_TsTtyCurrentAppSend_Object=MibTableColumn
tsTtyCurrentAppSend=_TsTtyCurrentAppSend_Object((1,3,6,1,4,1,2011,2,33,1,3,1,34),_TsTtyCurrentAppSend_Type())
tsTtyCurrentAppSend.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyCurrentAppSend.setStatus(_A)
class _TsTtyClearStatistic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_TsTtyClearStatistic_Type.__name__=_B
_TsTtyClearStatistic_Object=MibTableColumn
tsTtyClearStatistic=_TsTtyClearStatistic_Object((1,3,6,1,4,1,2011,2,33,1,3,1,35),_TsTtyClearStatistic_Type())
tsTtyClearStatistic.setMaxAccess(_I)
if mibBuilder.loadTexts:tsTtyClearStatistic.setStatus(_A)
class _TsDebugTtyAll_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsDebugTtyAll_Type.__name__=_B
_TsDebugTtyAll_Object=MibTableColumn
tsDebugTtyAll=_TsDebugTtyAll_Object((1,3,6,1,4,1,2011,2,33,1,3,1,36),_TsDebugTtyAll_Type())
tsDebugTtyAll.setMaxAccess(_C)
if mibBuilder.loadTexts:tsDebugTtyAll.setStatus(_A)
class _TsDebugTtyBrief_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsDebugTtyBrief_Type.__name__=_B
_TsDebugTtyBrief_Object=MibTableColumn
tsDebugTtyBrief=_TsDebugTtyBrief_Object((1,3,6,1,4,1,2011,2,33,1,3,1,37),_TsDebugTtyBrief_Type())
tsDebugTtyBrief.setMaxAccess(_C)
if mibBuilder.loadTexts:tsDebugTtyBrief.setStatus(_A)
class _TsDebugTtySock_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('recv',2),('send',3),(_N,4)))
_TsDebugTtySock_Type.__name__=_B
_TsDebugTtySock_Object=MibTableColumn
tsDebugTtySock=_TsDebugTtySock_Object((1,3,6,1,4,1,2011,2,33,1,3,1,38),_TsDebugTtySock_Type())
tsDebugTtySock.setMaxAccess(_C)
if mibBuilder.loadTexts:tsDebugTtySock.setStatus(_A)
class _TsDebugTtyTimeStamp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsDebugTtyTimeStamp_Type.__name__=_B
_TsDebugTtyTimeStamp_Object=MibTableColumn
tsDebugTtyTimeStamp=_TsDebugTtyTimeStamp_Object((1,3,6,1,4,1,2011,2,33,1,3,1,39),_TsDebugTtyTimeStamp_Type())
tsDebugTtyTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tsDebugTtyTimeStamp.setStatus(_A)
class _TsDebugTtyTty_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('recv',2),('send',3),(_N,4)))
_TsDebugTtyTty_Type.__name__=_B
_TsDebugTtyTty_Object=MibTableColumn
tsDebugTtyTty=_TsDebugTtyTty_Object((1,3,6,1,4,1,2011,2,33,1,3,1,40),_TsDebugTtyTty_Type())
tsDebugTtyTty.setMaxAccess(_C)
if mibBuilder.loadTexts:tsDebugTtyTty.setStatus(_A)
_TsTtyManageTable_Object=MibTable
tsTtyManageTable=_TsTtyManageTable_Object((1,3,6,1,4,1,2011,2,33,1,4))
if mibBuilder.loadTexts:tsTtyManageTable.setStatus(_A)
_TsTtyManageEntry_Object=MibTableRow
tsTtyManageEntry=_TsTtyManageEntry_Object((1,3,6,1,4,1,2011,2,33,1,4,1))
tsTtyManageEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:tsTtyManageEntry.setStatus(_A)
class _TsTtyManageUnixIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_TsTtyManageUnixIndex_Type.__name__=_B
_TsTtyManageUnixIndex_Object=MibTableColumn
tsTtyManageUnixIndex=_TsTtyManageUnixIndex_Object((1,3,6,1,4,1,2011,2,33,1,4,1,1),_TsTtyManageUnixIndex_Type())
tsTtyManageUnixIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyManageUnixIndex.setStatus(_A)
_TsTtyManageUnixSockid_Type=Integer32
_TsTtyManageUnixSockid_Object=MibTableColumn
tsTtyManageUnixSockid=_TsTtyManageUnixSockid_Object((1,3,6,1,4,1,2011,2,33,1,4,1,2),_TsTtyManageUnixSockid_Type())
tsTtyManageUnixSockid.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyManageUnixSockid.setStatus(_A)
_TsTtyManageLocalIP_Type=IpAddress
_TsTtyManageLocalIP_Object=MibTableColumn
tsTtyManageLocalIP=_TsTtyManageLocalIP_Object((1,3,6,1,4,1,2011,2,33,1,4,1,3),_TsTtyManageLocalIP_Type())
tsTtyManageLocalIP.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyManageLocalIP.setStatus(_A)
_TsTtyManageItemNum_Type=Integer32
_TsTtyManageItemNum_Object=MibTableColumn
tsTtyManageItemNum=_TsTtyManageItemNum_Object((1,3,6,1,4,1,2011,2,33,1,4,1,4),_TsTtyManageItemNum_Type())
tsTtyManageItemNum.setMaxAccess(_D)
if mibBuilder.loadTexts:tsTtyManageItemNum.setStatus(_A)
class _TsEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsEnable_Type.__name__=_B
_TsEnable_Object=MibScalar
tsEnable=_TsEnable_Object((1,3,6,1,4,1,2011,2,33,1,5),_TsEnable_Type())
tsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tsEnable.setStatus(_A)
class _TsEnableTrap_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsEnableTrap_Type.__name__=_B
_TsEnableTrap_Object=MibScalar
tsEnableTrap=_TsEnableTrap_Object((1,3,6,1,4,1,2011,2,33,1,6),_TsEnableTrap_Type())
tsEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:tsEnableTrap.setStatus(_A)
class _TsClearTtyAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_TsClearTtyAll_Type.__name__=_B
_TsClearTtyAll_Object=MibScalar
tsClearTtyAll=_TsClearTtyAll_Object((1,3,6,1,4,1,2011,2,33,1,7),_TsClearTtyAll_Type())
tsClearTtyAll.setMaxAccess(_I)
if mibBuilder.loadTexts:tsClearTtyAll.setStatus(_A)
class _TsLoginTty_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsLoginTty_Type.__name__=_B
_TsLoginTty_Object=MibScalar
tsLoginTty=_TsLoginTty_Object((1,3,6,1,4,1,2011,2,33,1,8),_TsLoginTty_Type())
tsLoginTty.setMaxAccess(_C)
if mibBuilder.loadTexts:tsLoginTty.setStatus('obsolete')
_TsDebugTtyGroup_ObjectIdentity=ObjectIdentity
tsDebugTtyGroup=_TsDebugTtyGroup_ObjectIdentity((1,3,6,1,4,1,2011,2,33,1,9))
class _TsDebugTtyError_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsDebugTtyError_Type.__name__=_B
_TsDebugTtyError_Object=MibScalar
tsDebugTtyError=_TsDebugTtyError_Object((1,3,6,1,4,1,2011,2,33,1,9,1),_TsDebugTtyError_Type())
tsDebugTtyError.setMaxAccess(_C)
if mibBuilder.loadTexts:tsDebugTtyError.setStatus(_A)
class _TsDebugTtyManage_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TsDebugTtyManage_Type.__name__=_B
_TsDebugTtyManage_Object=MibScalar
tsDebugTtyManage=_TsDebugTtyManage_Object((1,3,6,1,4,1,2011,2,33,1,9,2),_TsDebugTtyManage_Type())
tsDebugTtyManage.setMaxAccess(_C)
if mibBuilder.loadTexts:tsDebugTtyManage.setStatus(_A)
_TsTrap_ObjectIdentity=ObjectIdentity
tsTrap=_TsTrap_ObjectIdentity((1,3,6,1,4,1,2011,2,33,1,10))
tsAppStatusTrap=NotificationType((1,3,6,1,4,1,2011,2,33,1,10,1))
tsAppStatusTrap.setObjects(*((_E,_J),(_E,_S)))
if mibBuilder.loadTexts:tsAppStatusTrap.setStatus(_H)
tsTtyStatusTrap=NotificationType((1,3,6,1,4,1,2011,2,33,1,10,2))
tsTtyStatusTrap.setObjects(*((_E,_L),(_E,_M),(_E,_T)))
if mibBuilder.loadTexts:tsTtyStatusTrap.setStatus(_H)
tsExceptionTrap=NotificationType((1,3,6,1,4,1,2011,2,33,1,10,3))
if mibBuilder.loadTexts:tsExceptionTrap.setStatus(_H)
tsClearSuccessTrap=NotificationType((1,3,6,1,4,1,2011,2,33,1,10,4))
if mibBuilder.loadTexts:tsClearSuccessTrap.setStatus(_H)
tsDisconnectSuccessTrap=NotificationType((1,3,6,1,4,1,2011,2,33,1,10,5))
if mibBuilder.loadTexts:tsDisconnectSuccessTrap.setStatus(_H)
mibBuilder.exportSymbols(_E,**{'EntryStatus':EntryStatus,'terminalServer':terminalServer,'tsAppTable':tsAppTable,'tsAppEntry':tsAppEntry,_J:tsAppID,'tsAppIPAddress':tsAppIPAddress,'tsAppPort':tsAppPort,'tsAppType':tsAppType,'tsAppName':tsAppName,'tsAppSourceIP':tsAppSourceIP,'tsAppLocalPort':tsAppLocalPort,_S:tsAppTtyServerState,'tsAppSocketRecvBufSize':tsAppSocketRecvBufSize,'tsAppSocketSendBufSize':tsAppSocketSendBufSize,'tsAppSockRecvByte':tsAppSockRecvByte,'tsAppSockSendByte':tsAppSockSendByte,'tsAppLastRecvTime':tsAppLastRecvTime,'tsAppLastSendTime':tsAppLastSendTime,'tsAppClearStatistic':tsAppClearStatistic,'tsAppUnixIndex':tsAppUnixIndex,'tsAppStatus':tsAppStatus,'tsAsyModeTtyTable':tsAsyModeTtyTable,'tsAsyModeTtyEntry':tsAsyModeTtyEntry,_L:tsAsyModeTtyID,_M:tsAsyModeTtyVtyID,'tsAsyModeTtyIFIndex':tsAsyModeTtyIFIndex,'tsAsyModeTtyAppID':tsAsyModeTtyAppID,'tsAsyModeTtyDisconnect':tsAsyModeTtyDisconnect,_T:tsAsyModeTtyVtyState,'tsAsyModeTtyFlowCtrlState':tsAsyModeTtyFlowCtrlState,'tsAsyModeTtyStatus':tsAsyModeTtyStatus,'tsTtyTable':tsTtyTable,'tsTtyEntry':tsTtyEntry,_Q:tsTtyID,'tsTtyBufferSize':tsTtyBufferSize,'tsTtyAutoLink':tsTtyAutoLink,'tsTtyCloseLink':tsTtyCloseLink,'tsTtyConnPrint':tsTtyConnPrint,'tsTtyDelay':tsTtyDelay,'tsTtyLogoPrint':tsTtyLogoPrint,'tsTtyMenuKey1':tsTtyMenuKey1,'tsTtyMenuKey2':tsTtyMenuKey2,'tsTtyMenuKey3':tsTtyMenuKey3,'tsTtyReadBlock':tsTtyReadBlock,'tsTtyRedrawkey1':tsTtyRedrawkey1,'tsTtyRedrawkey2':tsTtyRedrawkey2,'tsTtyRedrawkey3':tsTtyRedrawkey3,'tsTtyResetKey1':tsTtyResetKey1,'tsTtyResetKey2':tsTtyResetKey2,'tsTtyResetKey3':tsTtyResetKey3,'tsTtyTcpNoDelay':tsTtyTcpNoDelay,'tsTtyTcpRecvBufferSize':tsTtyTcpRecvBufferSize,'tsTtyTcpSendBufferSize':tsTtyTcpSendBufferSize,'tsTtyTestKey1':tsTtyTestKey1,'tsTtyTestKey2':tsTtyTestKey2,'tsTtyTestKey3':tsTtyTestKey3,'tsTtyBufferRate':tsTtyBufferRate,'tsTtyRecvBytes':tsTtyRecvBytes,'tsTtySendBytes':tsTtySendBytes,'tsTtyLastRecvTime':tsTtyLastRecvTime,'tsTtyLastSendTime':tsTtyLastSendTime,'tsTtyCurrentVtyID':tsTtyCurrentVtyID,'tsTtyCurrentVtyRecv':tsTtyCurrentVtyRecv,'tsTtyCurrentVtySend':tsTtyCurrentVtySend,'tsTtyCurrentAppID':tsTtyCurrentAppID,'tsTtyCurrentAppRecv':tsTtyCurrentAppRecv,'tsTtyCurrentAppSend':tsTtyCurrentAppSend,'tsTtyClearStatistic':tsTtyClearStatistic,'tsDebugTtyAll':tsDebugTtyAll,'tsDebugTtyBrief':tsDebugTtyBrief,'tsDebugTtySock':tsDebugTtySock,'tsDebugTtyTimeStamp':tsDebugTtyTimeStamp,'tsDebugTtyTty':tsDebugTtyTty,'tsTtyManageTable':tsTtyManageTable,'tsTtyManageEntry':tsTtyManageEntry,_R:tsTtyManageUnixIndex,'tsTtyManageUnixSockid':tsTtyManageUnixSockid,'tsTtyManageLocalIP':tsTtyManageLocalIP,'tsTtyManageItemNum':tsTtyManageItemNum,'tsEnable':tsEnable,'tsEnableTrap':tsEnableTrap,'tsClearTtyAll':tsClearTtyAll,'tsLoginTty':tsLoginTty,'tsDebugTtyGroup':tsDebugTtyGroup,'tsDebugTtyError':tsDebugTtyError,'tsDebugTtyManage':tsDebugTtyManage,'tsTrap':tsTrap,'tsAppStatusTrap':tsAppStatusTrap,'tsTtyStatusTrap':tsTtyStatusTrap,'tsExceptionTrap':tsExceptionTrap,'tsClearSuccessTrap':tsClearSuccessTrap,'tsDisconnectSuccessTrap':tsDisconnectSuccessTrap})