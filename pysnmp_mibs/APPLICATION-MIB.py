_BU='applicationRunGroup'
_BT='applicationHistoryGroup'
_BS='applicationMonitorGroup'
_BR='applElmtRunControlTerminate'
_BQ='applElmtRunControlReconfigure'
_BP='applElmtRunControlSuspend'
_BO='applElmtRunStatusLastErrorTime'
_BN='applElmtRunStatusLastErrorMsg'
_BM='applElmtRunStatusOpenFiles'
_BL='applElmtRunStatusOpenConnections'
_BK='applElmtRunStatusHeapUsage'
_BJ='applElmtRunStatusSuspended'
_BI='applPastTransStreamInvokes'
_BH='applPastTransStreamPerforms'
_BG='applPastTransKindBytes'
_BF='applPastTransKindTrans'
_BE='applPastTransFlowBytes'
_BD='applPastTransFlowTrans'
_BC='applPastTransKindTime'
_BB='applPastTransKindBytesLow'
_BA='applPastTransKindTransLow'
_B9='applPastTransFlowTime'
_B8='applPastTransFlowBytesLow'
_B7='applPastTransFlowTransLow'
_B6='applPastTransStreamPrfRspTimes'
_B5='applPastTransStreamPrfCumTimes'
_B4='applPastTransStreamPerformsLow'
_B3='applPastTransStreamInvRspTimes'
_B2='applPastTransStreamInvCumTimes'
_B1='applPastTransStreamInvokesLow'
_B0='applPastTransStreamUnitOfWork'
_A_='applPastTransStreamDescr'
_Az='applPastChannelBytesWritten'
_Ay='applPastChannelWriteRequests'
_Ax='applPastChannelBytesRead'
_Aw='applPastChannelReadRequests'
_Av='applPastConApplication'
_Au='applPastConFarEndpoint'
_At='applPastConFarEndAddr'
_As='applPastConNearEndpoint'
_Ar='applPastConNearEndAddr'
_Aq='applPastConTransport'
_Ap='applPastFileMode'
_Ao='applPastFileSizeLow'
_An='applPastFileSizeHigh'
_Am='applPastFileName'
_Al='applPastChannelLastWriteTime'
_Ak='applPastChannelBytesWritLow'
_Aj='applPastChannelWriteFailures'
_Ai='applPastChannelWriteReqsLow'
_Ah='applPastChannelLastReadTime'
_Ag='applPastChannelBytesReadLow'
_Af='applPastChannelReadFailures'
_Ae='applPastChannelReadReqsLow'
_Ad='applPastChannelCloseTime'
_Ac='applPastChannelOpenTime'
_Ab='applPastChannelControlRemItems'
_Aa='applPastChannelControlTimeLimit'
_AZ='applPastChannelControlMaxRows'
_AY='applPastChannelControlCollect'
_AX='applTransactKindBytes'
_AW='applTransactKindTrans'
_AV='applTransactFlowBytes'
_AU='applTransactFlowTrans'
_AT='applTransactStreamPerforms'
_AS='applTransactStreamInvokes'
_AR='applTransactKindTime'
_AQ='applTransactKindBytesLow'
_AP='applTransactKindTransLow'
_AO='applTransactFlowTime'
_AN='applTransactFlowBytesLow'
_AM='applTransactFlowTransLow'
_AL='applTransactStreamPrfRspTimes'
_AK='applTransactStreamPrfCumTimes'
_AJ='applTransactStreamPerformsLow'
_AI='applTransactStreamInvRspTimes'
_AH='applTransactStreamInvCumTimes'
_AG='applTransactStreamInvokesLow'
_AF='applTransactStreamUnitOfWork'
_AE='applTransactStreamDescr'
_AD='applOpenChannelBytesWritten'
_AC='applOpenChannelWriteRequests'
_AB='applOpenChannelBytesRead'
_AA='applOpenChannelReadRequests'
_A9='applOpenConnectionApplication'
_A8='applOpenConnectionFarEndpoint'
_A7='applOpenConnectionFarEndAddr'
_A6='applOpenConnectionNearEndpoint'
_A5='applOpenConnectionNearEndAddr'
_A4='applOpenConnectionTransport'
_A3='applOpenFileMode'
_A2='applOpenFileSizeLow'
_A1='applOpenFileSizeHigh'
_A0='applOpenFileName'
_z='applOpenChannelLastWriteTime'
_y='applOpenChannelBytesWrittenLow'
_x='applOpenChannelWriteFailures'
_w='applOpenChannelWriteRequestsLow'
_v='applOpenChannelLastReadTime'
_u='applOpenChannelBytesReadLow'
_t='applOpenChannelReadFailures'
_s='applOpenChannelReadRequestsLow'
_r='applOpenChannelOpenTime'
_q='applSrvInstQual'
_p='applPastTransKind'
_o='channel history entries'
_n='applTransactKind'
_m='response'
_l='request'
_k='receive'
_j='transmit'
_i='readWrite'
_h='2^32 byte blocks'
_g='failed write requests'
_f='failed read requests'
_e='applPastTransFlowReqRsp'
_d='applPastTransFlowDirection'
_c='applTransactFlowReqRsp'
_b='applTransactFlowDirection'
_a='applSrvInstance'
_Z='TruthValue'
_Y='TDomain'
_X='write requests'
_W='read requests'
_V='applSrvName'
_U='ApplTAddress'
_T='applSrvIndex'
_S='sysApplElmtRunIndex'
_R='SYSAPPL-MIB'
_Q='read-write'
_P='applPastChannelIndex'
_O='applOpenChannelIndex'
_N='Unsigned32'
_M='milliseconds'
_L='0000000000000000'
_K='Integer32'
_J='not-accessible'
_I='DateAndTime'
_H='applElmtOrSvcId'
_G='applElmtOrSvc'
_F='SnmpAdminString'
_E='transactions'
_D='bytes'
_C='read-only'
_B='APPLICATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso','mib-2','zeroDotZero')
DateAndTime,DisplayString,PhysAddress,TDomain,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'DisplayString','PhysAddress',_Y,'TextualConvention','TestAndIncr','TimeStamp',_Z)
LongUtf8String,sysApplElmtRunIndex=mibBuilder.importSymbols(_R,'LongUtf8String',_S)
applicationMib=ModuleIdentity((1,3,6,1,2,1,62))
class Unsigned64TC(TextualConvention,Counter64):status=_A
class ApplTAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApplicationMibObjects_ObjectIdentity=ObjectIdentity
applicationMibObjects=_ApplicationMibObjects_ObjectIdentity((1,3,6,1,2,1,62,1))
_ApplServiceGroup_ObjectIdentity=ObjectIdentity
applServiceGroup=_ApplServiceGroup_ObjectIdentity((1,3,6,1,2,1,62,1,1))
_ApplSrvNameToSrvInstTable_Object=MibTable
applSrvNameToSrvInstTable=_ApplSrvNameToSrvInstTable_Object((1,3,6,1,2,1,62,1,1,1))
if mibBuilder.loadTexts:applSrvNameToSrvInstTable.setStatus(_A)
_ApplSrvNameToSrvInstEntry_Object=MibTableRow
applSrvNameToSrvInstEntry=_ApplSrvNameToSrvInstEntry_Object((1,3,6,1,2,1,62,1,1,1,1))
applSrvNameToSrvInstEntry.setIndexNames((0,_B,_V),(0,_B,_T))
if mibBuilder.loadTexts:applSrvNameToSrvInstEntry.setStatus(_A)
_ApplSrvInstQual_Type=SnmpAdminString
_ApplSrvInstQual_Object=MibTableColumn
applSrvInstQual=_ApplSrvInstQual_Object((1,3,6,1,2,1,62,1,1,1,1,1),_ApplSrvInstQual_Type())
applSrvInstQual.setMaxAccess(_C)
if mibBuilder.loadTexts:applSrvInstQual.setStatus(_A)
_ApplSrvInstToSrvNameTable_Object=MibTable
applSrvInstToSrvNameTable=_ApplSrvInstToSrvNameTable_Object((1,3,6,1,2,1,62,1,1,2))
if mibBuilder.loadTexts:applSrvInstToSrvNameTable.setStatus(_A)
_ApplSrvInstToSrvNameEntry_Object=MibTableRow
applSrvInstToSrvNameEntry=_ApplSrvInstToSrvNameEntry_Object((1,3,6,1,2,1,62,1,1,2,1))
applSrvInstToSrvNameEntry.setIndexNames((0,_B,_T),(0,_B,_V))
if mibBuilder.loadTexts:applSrvInstToSrvNameEntry.setStatus(_A)
_ApplSrvName_Type=SnmpAdminString
_ApplSrvName_Object=MibTableColumn
applSrvName=_ApplSrvName_Object((1,3,6,1,2,1,62,1,1,2,1,1),_ApplSrvName_Type())
applSrvName.setMaxAccess(_C)
if mibBuilder.loadTexts:applSrvName.setStatus(_A)
_ApplSrvInstToRunApplElmtTable_Object=MibTable
applSrvInstToRunApplElmtTable=_ApplSrvInstToRunApplElmtTable_Object((1,3,6,1,2,1,62,1,1,3))
if mibBuilder.loadTexts:applSrvInstToRunApplElmtTable.setStatus(_A)
_ApplSrvInstToRunApplElmtEntry_Object=MibTableRow
applSrvInstToRunApplElmtEntry=_ApplSrvInstToRunApplElmtEntry_Object((1,3,6,1,2,1,62,1,1,3,1))
applSrvInstToRunApplElmtEntry.setIndexNames((0,_B,_T),(0,_R,_S))
if mibBuilder.loadTexts:applSrvInstToRunApplElmtEntry.setStatus(_A)
class _ApplSrvIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApplSrvIndex_Type.__name__=_N
_ApplSrvIndex_Object=MibTableColumn
applSrvIndex=_ApplSrvIndex_Object((1,3,6,1,2,1,62,1,1,3,1,1),_ApplSrvIndex_Type())
applSrvIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:applSrvIndex.setStatus(_A)
_ApplRunApplElmtToSrvInstTable_Object=MibTable
applRunApplElmtToSrvInstTable=_ApplRunApplElmtToSrvInstTable_Object((1,3,6,1,2,1,62,1,1,4))
if mibBuilder.loadTexts:applRunApplElmtToSrvInstTable.setStatus(_A)
_ApplRunApplElmtToSrvInstEntry_Object=MibTableRow
applRunApplElmtToSrvInstEntry=_ApplRunApplElmtToSrvInstEntry_Object((1,3,6,1,2,1,62,1,1,4,1))
applRunApplElmtToSrvInstEntry.setIndexNames((0,_R,_S),(0,_B,_a))
if mibBuilder.loadTexts:applRunApplElmtToSrvInstEntry.setStatus(_A)
class _ApplSrvInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApplSrvInstance_Type.__name__=_N
_ApplSrvInstance_Object=MibTableColumn
applSrvInstance=_ApplSrvInstance_Object((1,3,6,1,2,1,62,1,1,4,1,1),_ApplSrvInstance_Type())
applSrvInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:applSrvInstance.setStatus(_A)
_ApplChannelGroup_ObjectIdentity=ObjectIdentity
applChannelGroup=_ApplChannelGroup_ObjectIdentity((1,3,6,1,2,1,62,1,2))
_ApplOpenChannelTable_Object=MibTable
applOpenChannelTable=_ApplOpenChannelTable_Object((1,3,6,1,2,1,62,1,2,1))
if mibBuilder.loadTexts:applOpenChannelTable.setStatus(_A)
_ApplOpenChannelEntry_Object=MibTableRow
applOpenChannelEntry=_ApplOpenChannelEntry_Object((1,3,6,1,2,1,62,1,2,1,1))
applOpenChannelEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_O))
if mibBuilder.loadTexts:applOpenChannelEntry.setStatus(_A)
class _ApplElmtOrSvc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('service',1),('element',2)))
_ApplElmtOrSvc_Type.__name__=_K
_ApplElmtOrSvc_Object=MibTableColumn
applElmtOrSvc=_ApplElmtOrSvc_Object((1,3,6,1,2,1,62,1,2,1,1,1),_ApplElmtOrSvc_Type())
applElmtOrSvc.setMaxAccess(_J)
if mibBuilder.loadTexts:applElmtOrSvc.setStatus(_A)
class _ApplElmtOrSvcId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApplElmtOrSvcId_Type.__name__=_N
_ApplElmtOrSvcId_Object=MibTableColumn
applElmtOrSvcId=_ApplElmtOrSvcId_Object((1,3,6,1,2,1,62,1,2,1,1,2),_ApplElmtOrSvcId_Type())
applElmtOrSvcId.setMaxAccess(_J)
if mibBuilder.loadTexts:applElmtOrSvcId.setStatus(_A)
_ApplOpenChannelIndex_Type=Unsigned32
_ApplOpenChannelIndex_Object=MibTableColumn
applOpenChannelIndex=_ApplOpenChannelIndex_Object((1,3,6,1,2,1,62,1,2,1,1,3),_ApplOpenChannelIndex_Type())
applOpenChannelIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:applOpenChannelIndex.setStatus(_A)
_ApplOpenChannelOpenTime_Type=TimeStamp
_ApplOpenChannelOpenTime_Object=MibTableColumn
applOpenChannelOpenTime=_ApplOpenChannelOpenTime_Object((1,3,6,1,2,1,62,1,2,1,1,4),_ApplOpenChannelOpenTime_Type())
applOpenChannelOpenTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelOpenTime.setStatus(_A)
_ApplOpenChannelReadRequests_Type=Counter64
_ApplOpenChannelReadRequests_Object=MibTableColumn
applOpenChannelReadRequests=_ApplOpenChannelReadRequests_Object((1,3,6,1,2,1,62,1,2,1,1,5),_ApplOpenChannelReadRequests_Type())
applOpenChannelReadRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelReadRequests.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelReadRequests.setUnits(_W)
_ApplOpenChannelReadRequestsLow_Type=Counter32
_ApplOpenChannelReadRequestsLow_Object=MibTableColumn
applOpenChannelReadRequestsLow=_ApplOpenChannelReadRequestsLow_Object((1,3,6,1,2,1,62,1,2,1,1,6),_ApplOpenChannelReadRequestsLow_Type())
applOpenChannelReadRequestsLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelReadRequestsLow.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelReadRequestsLow.setUnits(_W)
_ApplOpenChannelReadFailures_Type=Counter32
_ApplOpenChannelReadFailures_Object=MibTableColumn
applOpenChannelReadFailures=_ApplOpenChannelReadFailures_Object((1,3,6,1,2,1,62,1,2,1,1,7),_ApplOpenChannelReadFailures_Type())
applOpenChannelReadFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelReadFailures.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelReadFailures.setUnits(_f)
_ApplOpenChannelBytesRead_Type=Counter64
_ApplOpenChannelBytesRead_Object=MibTableColumn
applOpenChannelBytesRead=_ApplOpenChannelBytesRead_Object((1,3,6,1,2,1,62,1,2,1,1,8),_ApplOpenChannelBytesRead_Type())
applOpenChannelBytesRead.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelBytesRead.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelBytesRead.setUnits(_D)
_ApplOpenChannelBytesReadLow_Type=Counter32
_ApplOpenChannelBytesReadLow_Object=MibTableColumn
applOpenChannelBytesReadLow=_ApplOpenChannelBytesReadLow_Object((1,3,6,1,2,1,62,1,2,1,1,9),_ApplOpenChannelBytesReadLow_Type())
applOpenChannelBytesReadLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelBytesReadLow.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelBytesReadLow.setUnits(_D)
class _ApplOpenChannelLastReadTime_Type(DateAndTime):defaultHexValue=_L
_ApplOpenChannelLastReadTime_Type.__name__=_I
_ApplOpenChannelLastReadTime_Object=MibTableColumn
applOpenChannelLastReadTime=_ApplOpenChannelLastReadTime_Object((1,3,6,1,2,1,62,1,2,1,1,10),_ApplOpenChannelLastReadTime_Type())
applOpenChannelLastReadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelLastReadTime.setStatus(_A)
_ApplOpenChannelWriteRequests_Type=Counter64
_ApplOpenChannelWriteRequests_Object=MibTableColumn
applOpenChannelWriteRequests=_ApplOpenChannelWriteRequests_Object((1,3,6,1,2,1,62,1,2,1,1,11),_ApplOpenChannelWriteRequests_Type())
applOpenChannelWriteRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelWriteRequests.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelWriteRequests.setUnits(_X)
_ApplOpenChannelWriteRequestsLow_Type=Counter32
_ApplOpenChannelWriteRequestsLow_Object=MibTableColumn
applOpenChannelWriteRequestsLow=_ApplOpenChannelWriteRequestsLow_Object((1,3,6,1,2,1,62,1,2,1,1,12),_ApplOpenChannelWriteRequestsLow_Type())
applOpenChannelWriteRequestsLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelWriteRequestsLow.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelWriteRequestsLow.setUnits(_X)
_ApplOpenChannelWriteFailures_Type=Counter32
_ApplOpenChannelWriteFailures_Object=MibTableColumn
applOpenChannelWriteFailures=_ApplOpenChannelWriteFailures_Object((1,3,6,1,2,1,62,1,2,1,1,13),_ApplOpenChannelWriteFailures_Type())
applOpenChannelWriteFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelWriteFailures.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelWriteFailures.setUnits(_g)
_ApplOpenChannelBytesWritten_Type=Counter64
_ApplOpenChannelBytesWritten_Object=MibTableColumn
applOpenChannelBytesWritten=_ApplOpenChannelBytesWritten_Object((1,3,6,1,2,1,62,1,2,1,1,14),_ApplOpenChannelBytesWritten_Type())
applOpenChannelBytesWritten.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelBytesWritten.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelBytesWritten.setUnits(_D)
_ApplOpenChannelBytesWrittenLow_Type=Counter32
_ApplOpenChannelBytesWrittenLow_Object=MibTableColumn
applOpenChannelBytesWrittenLow=_ApplOpenChannelBytesWrittenLow_Object((1,3,6,1,2,1,62,1,2,1,1,15),_ApplOpenChannelBytesWrittenLow_Type())
applOpenChannelBytesWrittenLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelBytesWrittenLow.setStatus(_A)
if mibBuilder.loadTexts:applOpenChannelBytesWrittenLow.setUnits(_D)
class _ApplOpenChannelLastWriteTime_Type(DateAndTime):defaultHexValue=_L
_ApplOpenChannelLastWriteTime_Type.__name__=_I
_ApplOpenChannelLastWriteTime_Object=MibTableColumn
applOpenChannelLastWriteTime=_ApplOpenChannelLastWriteTime_Object((1,3,6,1,2,1,62,1,2,1,1,16),_ApplOpenChannelLastWriteTime_Type())
applOpenChannelLastWriteTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenChannelLastWriteTime.setStatus(_A)
_ApplOpenFileTable_Object=MibTable
applOpenFileTable=_ApplOpenFileTable_Object((1,3,6,1,2,1,62,1,2,2))
if mibBuilder.loadTexts:applOpenFileTable.setStatus(_A)
_ApplOpenFileEntry_Object=MibTableRow
applOpenFileEntry=_ApplOpenFileEntry_Object((1,3,6,1,2,1,62,1,2,2,1))
applOpenFileEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_O))
if mibBuilder.loadTexts:applOpenFileEntry.setStatus(_A)
_ApplOpenFileName_Type=LongUtf8String
_ApplOpenFileName_Object=MibTableColumn
applOpenFileName=_ApplOpenFileName_Object((1,3,6,1,2,1,62,1,2,2,1,1),_ApplOpenFileName_Type())
applOpenFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenFileName.setStatus(_A)
_ApplOpenFileSizeHigh_Type=Unsigned32
_ApplOpenFileSizeHigh_Object=MibTableColumn
applOpenFileSizeHigh=_ApplOpenFileSizeHigh_Object((1,3,6,1,2,1,62,1,2,2,1,2),_ApplOpenFileSizeHigh_Type())
applOpenFileSizeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenFileSizeHigh.setStatus(_A)
if mibBuilder.loadTexts:applOpenFileSizeHigh.setUnits(_h)
_ApplOpenFileSizeLow_Type=Unsigned32
_ApplOpenFileSizeLow_Object=MibTableColumn
applOpenFileSizeLow=_ApplOpenFileSizeLow_Object((1,3,6,1,2,1,62,1,2,2,1,3),_ApplOpenFileSizeLow_Type())
applOpenFileSizeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenFileSizeLow.setStatus(_A)
if mibBuilder.loadTexts:applOpenFileSizeLow.setUnits(_D)
class _ApplOpenFileMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('read',1),('write',2),(_i,3)))
_ApplOpenFileMode_Type.__name__=_K
_ApplOpenFileMode_Object=MibTableColumn
applOpenFileMode=_ApplOpenFileMode_Object((1,3,6,1,2,1,62,1,2,2,1,4),_ApplOpenFileMode_Type())
applOpenFileMode.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenFileMode.setStatus(_A)
_ApplOpenConnectionTable_Object=MibTable
applOpenConnectionTable=_ApplOpenConnectionTable_Object((1,3,6,1,2,1,62,1,2,3))
if mibBuilder.loadTexts:applOpenConnectionTable.setStatus(_A)
_ApplOpenConnectionEntry_Object=MibTableRow
applOpenConnectionEntry=_ApplOpenConnectionEntry_Object((1,3,6,1,2,1,62,1,2,3,1))
applOpenConnectionEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_O))
if mibBuilder.loadTexts:applOpenConnectionEntry.setStatus(_A)
class _ApplOpenConnectionTransport_Type(TDomain):defaultValue=0,0
_ApplOpenConnectionTransport_Type.__name__=_Y
_ApplOpenConnectionTransport_Object=MibTableColumn
applOpenConnectionTransport=_ApplOpenConnectionTransport_Object((1,3,6,1,2,1,62,1,2,3,1,1),_ApplOpenConnectionTransport_Type())
applOpenConnectionTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenConnectionTransport.setStatus(_A)
class _ApplOpenConnectionNearEndAddr_Type(ApplTAddress):defaultValue=OctetString('')
_ApplOpenConnectionNearEndAddr_Type.__name__=_U
_ApplOpenConnectionNearEndAddr_Object=MibTableColumn
applOpenConnectionNearEndAddr=_ApplOpenConnectionNearEndAddr_Object((1,3,6,1,2,1,62,1,2,3,1,2),_ApplOpenConnectionNearEndAddr_Type())
applOpenConnectionNearEndAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenConnectionNearEndAddr.setStatus(_A)
class _ApplOpenConnectionNearEndpoint_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplOpenConnectionNearEndpoint_Type.__name__=_F
_ApplOpenConnectionNearEndpoint_Object=MibTableColumn
applOpenConnectionNearEndpoint=_ApplOpenConnectionNearEndpoint_Object((1,3,6,1,2,1,62,1,2,3,1,3),_ApplOpenConnectionNearEndpoint_Type())
applOpenConnectionNearEndpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenConnectionNearEndpoint.setStatus(_A)
class _ApplOpenConnectionFarEndAddr_Type(ApplTAddress):defaultValue=OctetString('')
_ApplOpenConnectionFarEndAddr_Type.__name__=_U
_ApplOpenConnectionFarEndAddr_Object=MibTableColumn
applOpenConnectionFarEndAddr=_ApplOpenConnectionFarEndAddr_Object((1,3,6,1,2,1,62,1,2,3,1,4),_ApplOpenConnectionFarEndAddr_Type())
applOpenConnectionFarEndAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenConnectionFarEndAddr.setStatus(_A)
class _ApplOpenConnectionFarEndpoint_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplOpenConnectionFarEndpoint_Type.__name__=_F
_ApplOpenConnectionFarEndpoint_Object=MibTableColumn
applOpenConnectionFarEndpoint=_ApplOpenConnectionFarEndpoint_Object((1,3,6,1,2,1,62,1,2,3,1,5),_ApplOpenConnectionFarEndpoint_Type())
applOpenConnectionFarEndpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenConnectionFarEndpoint.setStatus(_A)
class _ApplOpenConnectionApplication_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplOpenConnectionApplication_Type.__name__=_F
_ApplOpenConnectionApplication_Object=MibTableColumn
applOpenConnectionApplication=_ApplOpenConnectionApplication_Object((1,3,6,1,2,1,62,1,2,3,1,6),_ApplOpenConnectionApplication_Type())
applOpenConnectionApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:applOpenConnectionApplication.setStatus(_A)
_ApplTransactionStreamTable_Object=MibTable
applTransactionStreamTable=_ApplTransactionStreamTable_Object((1,3,6,1,2,1,62,1,2,4))
if mibBuilder.loadTexts:applTransactionStreamTable.setStatus(_A)
_ApplTransactionStreamEntry_Object=MibTableRow
applTransactionStreamEntry=_ApplTransactionStreamEntry_Object((1,3,6,1,2,1,62,1,2,4,1))
applTransactionStreamEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_O))
if mibBuilder.loadTexts:applTransactionStreamEntry.setStatus(_A)
class _ApplTransactStreamDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplTransactStreamDescr_Type.__name__=_F
_ApplTransactStreamDescr_Object=MibTableColumn
applTransactStreamDescr=_ApplTransactStreamDescr_Object((1,3,6,1,2,1,62,1,2,4,1,1),_ApplTransactStreamDescr_Type())
applTransactStreamDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamDescr.setStatus(_A)
class _ApplTransactStreamUnitOfWork_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplTransactStreamUnitOfWork_Type.__name__=_F
_ApplTransactStreamUnitOfWork_Object=MibTableColumn
applTransactStreamUnitOfWork=_ApplTransactStreamUnitOfWork_Object((1,3,6,1,2,1,62,1,2,4,1,2),_ApplTransactStreamUnitOfWork_Type())
applTransactStreamUnitOfWork.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamUnitOfWork.setStatus(_A)
_ApplTransactStreamInvokes_Type=Counter64
_ApplTransactStreamInvokes_Object=MibTableColumn
applTransactStreamInvokes=_ApplTransactStreamInvokes_Object((1,3,6,1,2,1,62,1,2,4,1,3),_ApplTransactStreamInvokes_Type())
applTransactStreamInvokes.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamInvokes.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamInvokes.setUnits(_E)
_ApplTransactStreamInvokesLow_Type=Counter32
_ApplTransactStreamInvokesLow_Object=MibTableColumn
applTransactStreamInvokesLow=_ApplTransactStreamInvokesLow_Object((1,3,6,1,2,1,62,1,2,4,1,4),_ApplTransactStreamInvokesLow_Type())
applTransactStreamInvokesLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamInvokesLow.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamInvokesLow.setUnits(_E)
_ApplTransactStreamInvCumTimes_Type=Counter32
_ApplTransactStreamInvCumTimes_Object=MibTableColumn
applTransactStreamInvCumTimes=_ApplTransactStreamInvCumTimes_Object((1,3,6,1,2,1,62,1,2,4,1,5),_ApplTransactStreamInvCumTimes_Type())
applTransactStreamInvCumTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamInvCumTimes.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamInvCumTimes.setUnits(_M)
_ApplTransactStreamInvRspTimes_Type=Counter32
_ApplTransactStreamInvRspTimes_Object=MibTableColumn
applTransactStreamInvRspTimes=_ApplTransactStreamInvRspTimes_Object((1,3,6,1,2,1,62,1,2,4,1,6),_ApplTransactStreamInvRspTimes_Type())
applTransactStreamInvRspTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamInvRspTimes.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamInvRspTimes.setUnits(_M)
_ApplTransactStreamPerforms_Type=Counter64
_ApplTransactStreamPerforms_Object=MibTableColumn
applTransactStreamPerforms=_ApplTransactStreamPerforms_Object((1,3,6,1,2,1,62,1,2,4,1,7),_ApplTransactStreamPerforms_Type())
applTransactStreamPerforms.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamPerforms.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamPerforms.setUnits(_E)
_ApplTransactStreamPerformsLow_Type=Counter32
_ApplTransactStreamPerformsLow_Object=MibTableColumn
applTransactStreamPerformsLow=_ApplTransactStreamPerformsLow_Object((1,3,6,1,2,1,62,1,2,4,1,8),_ApplTransactStreamPerformsLow_Type())
applTransactStreamPerformsLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamPerformsLow.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamPerformsLow.setUnits(_E)
_ApplTransactStreamPrfCumTimes_Type=Counter32
_ApplTransactStreamPrfCumTimes_Object=MibTableColumn
applTransactStreamPrfCumTimes=_ApplTransactStreamPrfCumTimes_Object((1,3,6,1,2,1,62,1,2,4,1,9),_ApplTransactStreamPrfCumTimes_Type())
applTransactStreamPrfCumTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamPrfCumTimes.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamPrfCumTimes.setUnits(_M)
_ApplTransactStreamPrfRspTimes_Type=Counter32
_ApplTransactStreamPrfRspTimes_Object=MibTableColumn
applTransactStreamPrfRspTimes=_ApplTransactStreamPrfRspTimes_Object((1,3,6,1,2,1,62,1,2,4,1,10),_ApplTransactStreamPrfRspTimes_Type())
applTransactStreamPrfRspTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactStreamPrfRspTimes.setStatus(_A)
if mibBuilder.loadTexts:applTransactStreamPrfRspTimes.setUnits(_M)
_ApplTransactFlowTable_Object=MibTable
applTransactFlowTable=_ApplTransactFlowTable_Object((1,3,6,1,2,1,62,1,2,5))
if mibBuilder.loadTexts:applTransactFlowTable.setStatus(_A)
_ApplTransactFlowEntry_Object=MibTableRow
applTransactFlowEntry=_ApplTransactFlowEntry_Object((1,3,6,1,2,1,62,1,2,5,1))
applTransactFlowEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_O),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:applTransactFlowEntry.setStatus(_A)
class _ApplTransactFlowDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_ApplTransactFlowDirection_Type.__name__=_K
_ApplTransactFlowDirection_Object=MibTableColumn
applTransactFlowDirection=_ApplTransactFlowDirection_Object((1,3,6,1,2,1,62,1,2,5,1,1),_ApplTransactFlowDirection_Type())
applTransactFlowDirection.setMaxAccess(_J)
if mibBuilder.loadTexts:applTransactFlowDirection.setStatus(_A)
class _ApplTransactFlowReqRsp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_ApplTransactFlowReqRsp_Type.__name__=_K
_ApplTransactFlowReqRsp_Object=MibTableColumn
applTransactFlowReqRsp=_ApplTransactFlowReqRsp_Object((1,3,6,1,2,1,62,1,2,5,1,2),_ApplTransactFlowReqRsp_Type())
applTransactFlowReqRsp.setMaxAccess(_J)
if mibBuilder.loadTexts:applTransactFlowReqRsp.setStatus(_A)
_ApplTransactFlowTrans_Type=Counter64
_ApplTransactFlowTrans_Object=MibTableColumn
applTransactFlowTrans=_ApplTransactFlowTrans_Object((1,3,6,1,2,1,62,1,2,5,1,3),_ApplTransactFlowTrans_Type())
applTransactFlowTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactFlowTrans.setStatus(_A)
if mibBuilder.loadTexts:applTransactFlowTrans.setUnits(_E)
_ApplTransactFlowTransLow_Type=Counter32
_ApplTransactFlowTransLow_Object=MibTableColumn
applTransactFlowTransLow=_ApplTransactFlowTransLow_Object((1,3,6,1,2,1,62,1,2,5,1,4),_ApplTransactFlowTransLow_Type())
applTransactFlowTransLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactFlowTransLow.setStatus(_A)
if mibBuilder.loadTexts:applTransactFlowTransLow.setUnits(_E)
_ApplTransactFlowBytes_Type=Counter64
_ApplTransactFlowBytes_Object=MibTableColumn
applTransactFlowBytes=_ApplTransactFlowBytes_Object((1,3,6,1,2,1,62,1,2,5,1,5),_ApplTransactFlowBytes_Type())
applTransactFlowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactFlowBytes.setStatus(_A)
if mibBuilder.loadTexts:applTransactFlowBytes.setUnits(_D)
_ApplTransactFlowBytesLow_Type=Counter32
_ApplTransactFlowBytesLow_Object=MibTableColumn
applTransactFlowBytesLow=_ApplTransactFlowBytesLow_Object((1,3,6,1,2,1,62,1,2,5,1,6),_ApplTransactFlowBytesLow_Type())
applTransactFlowBytesLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactFlowBytesLow.setStatus(_A)
if mibBuilder.loadTexts:applTransactFlowBytesLow.setUnits(_D)
class _ApplTransactFlowTime_Type(DateAndTime):defaultHexValue=_L
_ApplTransactFlowTime_Type.__name__=_I
_ApplTransactFlowTime_Object=MibTableColumn
applTransactFlowTime=_ApplTransactFlowTime_Object((1,3,6,1,2,1,62,1,2,5,1,7),_ApplTransactFlowTime_Type())
applTransactFlowTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactFlowTime.setStatus(_A)
_ApplTransactKindTable_Object=MibTable
applTransactKindTable=_ApplTransactKindTable_Object((1,3,6,1,2,1,62,1,2,6))
if mibBuilder.loadTexts:applTransactKindTable.setStatus(_A)
_ApplTransactKindEntry_Object=MibTableRow
applTransactKindEntry=_ApplTransactKindEntry_Object((1,3,6,1,2,1,62,1,2,6,1))
applTransactKindEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_O),(0,_B,_b),(0,_B,_c),(0,_B,_n))
if mibBuilder.loadTexts:applTransactKindEntry.setStatus(_A)
class _ApplTransactKind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApplTransactKind_Type.__name__=_F
_ApplTransactKind_Object=MibTableColumn
applTransactKind=_ApplTransactKind_Object((1,3,6,1,2,1,62,1,2,6,1,1),_ApplTransactKind_Type())
applTransactKind.setMaxAccess(_J)
if mibBuilder.loadTexts:applTransactKind.setStatus(_A)
_ApplTransactKindTrans_Type=Counter64
_ApplTransactKindTrans_Object=MibTableColumn
applTransactKindTrans=_ApplTransactKindTrans_Object((1,3,6,1,2,1,62,1,2,6,1,2),_ApplTransactKindTrans_Type())
applTransactKindTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactKindTrans.setStatus(_A)
if mibBuilder.loadTexts:applTransactKindTrans.setUnits(_E)
_ApplTransactKindTransLow_Type=Counter32
_ApplTransactKindTransLow_Object=MibTableColumn
applTransactKindTransLow=_ApplTransactKindTransLow_Object((1,3,6,1,2,1,62,1,2,6,1,3),_ApplTransactKindTransLow_Type())
applTransactKindTransLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactKindTransLow.setStatus(_A)
if mibBuilder.loadTexts:applTransactKindTransLow.setUnits(_E)
_ApplTransactKindBytes_Type=Counter64
_ApplTransactKindBytes_Object=MibTableColumn
applTransactKindBytes=_ApplTransactKindBytes_Object((1,3,6,1,2,1,62,1,2,6,1,4),_ApplTransactKindBytes_Type())
applTransactKindBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactKindBytes.setStatus(_A)
if mibBuilder.loadTexts:applTransactKindBytes.setUnits(_D)
_ApplTransactKindBytesLow_Type=Counter32
_ApplTransactKindBytesLow_Object=MibTableColumn
applTransactKindBytesLow=_ApplTransactKindBytesLow_Object((1,3,6,1,2,1,62,1,2,6,1,5),_ApplTransactKindBytesLow_Type())
applTransactKindBytesLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactKindBytesLow.setStatus(_A)
if mibBuilder.loadTexts:applTransactKindBytesLow.setUnits(_D)
class _ApplTransactKindTime_Type(DateAndTime):defaultHexValue=_L
_ApplTransactKindTime_Type.__name__=_I
_ApplTransactKindTime_Object=MibTableColumn
applTransactKindTime=_ApplTransactKindTime_Object((1,3,6,1,2,1,62,1,2,6,1,6),_ApplTransactKindTime_Type())
applTransactKindTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applTransactKindTime.setStatus(_A)
_ApplPastChannelGroup_ObjectIdentity=ObjectIdentity
applPastChannelGroup=_ApplPastChannelGroup_ObjectIdentity((1,3,6,1,2,1,62,1,3))
_ApplPastChannelControlTable_Object=MibTable
applPastChannelControlTable=_ApplPastChannelControlTable_Object((1,3,6,1,2,1,62,1,3,1))
if mibBuilder.loadTexts:applPastChannelControlTable.setStatus(_A)
_ApplPastChannelControlEntry_Object=MibTableRow
applPastChannelControlEntry=_ApplPastChannelControlEntry_Object((1,3,6,1,2,1,62,1,3,1,1))
applPastChannelControlEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:applPastChannelControlEntry.setStatus(_A)
class _ApplPastChannelControlCollect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('frozen',2),('disabled',3)))
_ApplPastChannelControlCollect_Type.__name__=_K
_ApplPastChannelControlCollect_Object=MibTableColumn
applPastChannelControlCollect=_ApplPastChannelControlCollect_Object((1,3,6,1,2,1,62,1,3,1,1,1),_ApplPastChannelControlCollect_Type())
applPastChannelControlCollect.setMaxAccess(_Q)
if mibBuilder.loadTexts:applPastChannelControlCollect.setStatus(_A)
class _ApplPastChannelControlMaxRows_Type(Unsigned32):defaultValue=500
_ApplPastChannelControlMaxRows_Type.__name__=_N
_ApplPastChannelControlMaxRows_Object=MibTableColumn
applPastChannelControlMaxRows=_ApplPastChannelControlMaxRows_Object((1,3,6,1,2,1,62,1,3,1,1,2),_ApplPastChannelControlMaxRows_Type())
applPastChannelControlMaxRows.setMaxAccess(_Q)
if mibBuilder.loadTexts:applPastChannelControlMaxRows.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelControlMaxRows.setUnits(_o)
class _ApplPastChannelControlTimeLimit_Type(Unsigned32):defaultValue=7200
_ApplPastChannelControlTimeLimit_Type.__name__=_N
_ApplPastChannelControlTimeLimit_Object=MibTableColumn
applPastChannelControlTimeLimit=_ApplPastChannelControlTimeLimit_Object((1,3,6,1,2,1,62,1,3,1,1,3),_ApplPastChannelControlTimeLimit_Type())
applPastChannelControlTimeLimit.setMaxAccess(_Q)
if mibBuilder.loadTexts:applPastChannelControlTimeLimit.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelControlTimeLimit.setUnits('seconds')
_ApplPastChannelControlRemItems_Type=Counter32
_ApplPastChannelControlRemItems_Object=MibTableColumn
applPastChannelControlRemItems=_ApplPastChannelControlRemItems_Object((1,3,6,1,2,1,62,1,3,1,1,4),_ApplPastChannelControlRemItems_Type())
applPastChannelControlRemItems.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelControlRemItems.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelControlRemItems.setUnits(_o)
_ApplPastChannelTable_Object=MibTable
applPastChannelTable=_ApplPastChannelTable_Object((1,3,6,1,2,1,62,1,3,2))
if mibBuilder.loadTexts:applPastChannelTable.setStatus(_A)
_ApplPastChannelEntry_Object=MibTableRow
applPastChannelEntry=_ApplPastChannelEntry_Object((1,3,6,1,2,1,62,1,3,2,1))
applPastChannelEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_P))
if mibBuilder.loadTexts:applPastChannelEntry.setStatus(_A)
class _ApplPastChannelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ApplPastChannelIndex_Type.__name__=_N
_ApplPastChannelIndex_Object=MibTableColumn
applPastChannelIndex=_ApplPastChannelIndex_Object((1,3,6,1,2,1,62,1,3,2,1,1),_ApplPastChannelIndex_Type())
applPastChannelIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:applPastChannelIndex.setStatus(_A)
_ApplPastChannelOpenTime_Type=DateAndTime
_ApplPastChannelOpenTime_Object=MibTableColumn
applPastChannelOpenTime=_ApplPastChannelOpenTime_Object((1,3,6,1,2,1,62,1,3,2,1,2),_ApplPastChannelOpenTime_Type())
applPastChannelOpenTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelOpenTime.setStatus(_A)
_ApplPastChannelCloseTime_Type=DateAndTime
_ApplPastChannelCloseTime_Object=MibTableColumn
applPastChannelCloseTime=_ApplPastChannelCloseTime_Object((1,3,6,1,2,1,62,1,3,2,1,3),_ApplPastChannelCloseTime_Type())
applPastChannelCloseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelCloseTime.setStatus(_A)
_ApplPastChannelReadRequests_Type=Unsigned64TC
_ApplPastChannelReadRequests_Object=MibTableColumn
applPastChannelReadRequests=_ApplPastChannelReadRequests_Object((1,3,6,1,2,1,62,1,3,2,1,4),_ApplPastChannelReadRequests_Type())
applPastChannelReadRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelReadRequests.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelReadRequests.setUnits(_W)
_ApplPastChannelReadReqsLow_Type=Unsigned32
_ApplPastChannelReadReqsLow_Object=MibTableColumn
applPastChannelReadReqsLow=_ApplPastChannelReadReqsLow_Object((1,3,6,1,2,1,62,1,3,2,1,5),_ApplPastChannelReadReqsLow_Type())
applPastChannelReadReqsLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelReadReqsLow.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelReadReqsLow.setUnits(_W)
_ApplPastChannelReadFailures_Type=Unsigned32
_ApplPastChannelReadFailures_Object=MibTableColumn
applPastChannelReadFailures=_ApplPastChannelReadFailures_Object((1,3,6,1,2,1,62,1,3,2,1,6),_ApplPastChannelReadFailures_Type())
applPastChannelReadFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelReadFailures.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelReadFailures.setUnits(_f)
_ApplPastChannelBytesRead_Type=Unsigned64TC
_ApplPastChannelBytesRead_Object=MibTableColumn
applPastChannelBytesRead=_ApplPastChannelBytesRead_Object((1,3,6,1,2,1,62,1,3,2,1,7),_ApplPastChannelBytesRead_Type())
applPastChannelBytesRead.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelBytesRead.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelBytesRead.setUnits(_D)
_ApplPastChannelBytesReadLow_Type=Unsigned32
_ApplPastChannelBytesReadLow_Object=MibTableColumn
applPastChannelBytesReadLow=_ApplPastChannelBytesReadLow_Object((1,3,6,1,2,1,62,1,3,2,1,8),_ApplPastChannelBytesReadLow_Type())
applPastChannelBytesReadLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelBytesReadLow.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelBytesReadLow.setUnits(_D)
class _ApplPastChannelLastReadTime_Type(DateAndTime):defaultHexValue=_L
_ApplPastChannelLastReadTime_Type.__name__=_I
_ApplPastChannelLastReadTime_Object=MibTableColumn
applPastChannelLastReadTime=_ApplPastChannelLastReadTime_Object((1,3,6,1,2,1,62,1,3,2,1,9),_ApplPastChannelLastReadTime_Type())
applPastChannelLastReadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelLastReadTime.setStatus(_A)
_ApplPastChannelWriteRequests_Type=Unsigned64TC
_ApplPastChannelWriteRequests_Object=MibTableColumn
applPastChannelWriteRequests=_ApplPastChannelWriteRequests_Object((1,3,6,1,2,1,62,1,3,2,1,10),_ApplPastChannelWriteRequests_Type())
applPastChannelWriteRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelWriteRequests.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelWriteRequests.setUnits(_X)
_ApplPastChannelWriteReqsLow_Type=Unsigned32
_ApplPastChannelWriteReqsLow_Object=MibTableColumn
applPastChannelWriteReqsLow=_ApplPastChannelWriteReqsLow_Object((1,3,6,1,2,1,62,1,3,2,1,11),_ApplPastChannelWriteReqsLow_Type())
applPastChannelWriteReqsLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelWriteReqsLow.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelWriteReqsLow.setUnits(_X)
_ApplPastChannelWriteFailures_Type=Unsigned32
_ApplPastChannelWriteFailures_Object=MibTableColumn
applPastChannelWriteFailures=_ApplPastChannelWriteFailures_Object((1,3,6,1,2,1,62,1,3,2,1,12),_ApplPastChannelWriteFailures_Type())
applPastChannelWriteFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelWriteFailures.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelWriteFailures.setUnits(_g)
_ApplPastChannelBytesWritten_Type=Unsigned64TC
_ApplPastChannelBytesWritten_Object=MibTableColumn
applPastChannelBytesWritten=_ApplPastChannelBytesWritten_Object((1,3,6,1,2,1,62,1,3,2,1,13),_ApplPastChannelBytesWritten_Type())
applPastChannelBytesWritten.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelBytesWritten.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelBytesWritten.setUnits(_D)
_ApplPastChannelBytesWritLow_Type=Unsigned32
_ApplPastChannelBytesWritLow_Object=MibTableColumn
applPastChannelBytesWritLow=_ApplPastChannelBytesWritLow_Object((1,3,6,1,2,1,62,1,3,2,1,14),_ApplPastChannelBytesWritLow_Type())
applPastChannelBytesWritLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelBytesWritLow.setStatus(_A)
if mibBuilder.loadTexts:applPastChannelBytesWritLow.setUnits(_D)
class _ApplPastChannelLastWriteTime_Type(DateAndTime):defaultHexValue=_L
_ApplPastChannelLastWriteTime_Type.__name__=_I
_ApplPastChannelLastWriteTime_Object=MibTableColumn
applPastChannelLastWriteTime=_ApplPastChannelLastWriteTime_Object((1,3,6,1,2,1,62,1,3,2,1,15),_ApplPastChannelLastWriteTime_Type())
applPastChannelLastWriteTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastChannelLastWriteTime.setStatus(_A)
_ApplPastFileTable_Object=MibTable
applPastFileTable=_ApplPastFileTable_Object((1,3,6,1,2,1,62,1,3,3))
if mibBuilder.loadTexts:applPastFileTable.setStatus(_A)
_ApplPastFileEntry_Object=MibTableRow
applPastFileEntry=_ApplPastFileEntry_Object((1,3,6,1,2,1,62,1,3,3,1))
applPastFileEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_P))
if mibBuilder.loadTexts:applPastFileEntry.setStatus(_A)
_ApplPastFileName_Type=LongUtf8String
_ApplPastFileName_Object=MibTableColumn
applPastFileName=_ApplPastFileName_Object((1,3,6,1,2,1,62,1,3,3,1,1),_ApplPastFileName_Type())
applPastFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastFileName.setStatus(_A)
_ApplPastFileSizeHigh_Type=Unsigned32
_ApplPastFileSizeHigh_Object=MibTableColumn
applPastFileSizeHigh=_ApplPastFileSizeHigh_Object((1,3,6,1,2,1,62,1,3,3,1,2),_ApplPastFileSizeHigh_Type())
applPastFileSizeHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastFileSizeHigh.setStatus(_A)
if mibBuilder.loadTexts:applPastFileSizeHigh.setUnits(_h)
_ApplPastFileSizeLow_Type=Unsigned32
_ApplPastFileSizeLow_Object=MibTableColumn
applPastFileSizeLow=_ApplPastFileSizeLow_Object((1,3,6,1,2,1,62,1,3,3,1,3),_ApplPastFileSizeLow_Type())
applPastFileSizeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastFileSizeLow.setStatus(_A)
if mibBuilder.loadTexts:applPastFileSizeLow.setUnits(_D)
class _ApplPastFileMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('read',1),('write',2),(_i,3)))
_ApplPastFileMode_Type.__name__=_K
_ApplPastFileMode_Object=MibTableColumn
applPastFileMode=_ApplPastFileMode_Object((1,3,6,1,2,1,62,1,3,3,1,4),_ApplPastFileMode_Type())
applPastFileMode.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastFileMode.setStatus(_A)
_ApplPastConTable_Object=MibTable
applPastConTable=_ApplPastConTable_Object((1,3,6,1,2,1,62,1,3,4))
if mibBuilder.loadTexts:applPastConTable.setStatus(_A)
_ApplPastConEntry_Object=MibTableRow
applPastConEntry=_ApplPastConEntry_Object((1,3,6,1,2,1,62,1,3,4,1))
applPastConEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_P))
if mibBuilder.loadTexts:applPastConEntry.setStatus(_A)
class _ApplPastConTransport_Type(TDomain):defaultValue=0,0
_ApplPastConTransport_Type.__name__=_Y
_ApplPastConTransport_Object=MibTableColumn
applPastConTransport=_ApplPastConTransport_Object((1,3,6,1,2,1,62,1,3,4,1,1),_ApplPastConTransport_Type())
applPastConTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastConTransport.setStatus(_A)
class _ApplPastConNearEndAddr_Type(ApplTAddress):defaultValue=OctetString('')
_ApplPastConNearEndAddr_Type.__name__=_U
_ApplPastConNearEndAddr_Object=MibTableColumn
applPastConNearEndAddr=_ApplPastConNearEndAddr_Object((1,3,6,1,2,1,62,1,3,4,1,2),_ApplPastConNearEndAddr_Type())
applPastConNearEndAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastConNearEndAddr.setStatus(_A)
class _ApplPastConNearEndpoint_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplPastConNearEndpoint_Type.__name__=_F
_ApplPastConNearEndpoint_Object=MibTableColumn
applPastConNearEndpoint=_ApplPastConNearEndpoint_Object((1,3,6,1,2,1,62,1,3,4,1,3),_ApplPastConNearEndpoint_Type())
applPastConNearEndpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastConNearEndpoint.setStatus(_A)
class _ApplPastConFarEndAddr_Type(ApplTAddress):defaultValue=OctetString('')
_ApplPastConFarEndAddr_Type.__name__=_U
_ApplPastConFarEndAddr_Object=MibTableColumn
applPastConFarEndAddr=_ApplPastConFarEndAddr_Object((1,3,6,1,2,1,62,1,3,4,1,4),_ApplPastConFarEndAddr_Type())
applPastConFarEndAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastConFarEndAddr.setStatus(_A)
class _ApplPastConFarEndpoint_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplPastConFarEndpoint_Type.__name__=_F
_ApplPastConFarEndpoint_Object=MibTableColumn
applPastConFarEndpoint=_ApplPastConFarEndpoint_Object((1,3,6,1,2,1,62,1,3,4,1,5),_ApplPastConFarEndpoint_Type())
applPastConFarEndpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastConFarEndpoint.setStatus(_A)
class _ApplPastConApplication_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplPastConApplication_Type.__name__=_F
_ApplPastConApplication_Object=MibTableColumn
applPastConApplication=_ApplPastConApplication_Object((1,3,6,1,2,1,62,1,3,4,1,6),_ApplPastConApplication_Type())
applPastConApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastConApplication.setStatus(_A)
_ApplPastTransStreamTable_Object=MibTable
applPastTransStreamTable=_ApplPastTransStreamTable_Object((1,3,6,1,2,1,62,1,3,5))
if mibBuilder.loadTexts:applPastTransStreamTable.setStatus(_A)
_ApplPastTransStreamEntry_Object=MibTableRow
applPastTransStreamEntry=_ApplPastTransStreamEntry_Object((1,3,6,1,2,1,62,1,3,5,1))
applPastTransStreamEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_P))
if mibBuilder.loadTexts:applPastTransStreamEntry.setStatus(_A)
class _ApplPastTransStreamDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplPastTransStreamDescr_Type.__name__=_F
_ApplPastTransStreamDescr_Object=MibTableColumn
applPastTransStreamDescr=_ApplPastTransStreamDescr_Object((1,3,6,1,2,1,62,1,3,5,1,1),_ApplPastTransStreamDescr_Type())
applPastTransStreamDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamDescr.setStatus(_A)
class _ApplPastTransStreamUnitOfWork_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplPastTransStreamUnitOfWork_Type.__name__=_F
_ApplPastTransStreamUnitOfWork_Object=MibTableColumn
applPastTransStreamUnitOfWork=_ApplPastTransStreamUnitOfWork_Object((1,3,6,1,2,1,62,1,3,5,1,2),_ApplPastTransStreamUnitOfWork_Type())
applPastTransStreamUnitOfWork.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamUnitOfWork.setStatus(_A)
_ApplPastTransStreamInvokes_Type=Unsigned64TC
_ApplPastTransStreamInvokes_Object=MibTableColumn
applPastTransStreamInvokes=_ApplPastTransStreamInvokes_Object((1,3,6,1,2,1,62,1,3,5,1,3),_ApplPastTransStreamInvokes_Type())
applPastTransStreamInvokes.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamInvokes.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamInvokes.setUnits(_E)
_ApplPastTransStreamInvokesLow_Type=Unsigned32
_ApplPastTransStreamInvokesLow_Object=MibTableColumn
applPastTransStreamInvokesLow=_ApplPastTransStreamInvokesLow_Object((1,3,6,1,2,1,62,1,3,5,1,4),_ApplPastTransStreamInvokesLow_Type())
applPastTransStreamInvokesLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamInvokesLow.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamInvokesLow.setUnits(_E)
_ApplPastTransStreamInvCumTimes_Type=Unsigned32
_ApplPastTransStreamInvCumTimes_Object=MibTableColumn
applPastTransStreamInvCumTimes=_ApplPastTransStreamInvCumTimes_Object((1,3,6,1,2,1,62,1,3,5,1,5),_ApplPastTransStreamInvCumTimes_Type())
applPastTransStreamInvCumTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamInvCumTimes.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamInvCumTimes.setUnits(_M)
_ApplPastTransStreamInvRspTimes_Type=Unsigned32
_ApplPastTransStreamInvRspTimes_Object=MibTableColumn
applPastTransStreamInvRspTimes=_ApplPastTransStreamInvRspTimes_Object((1,3,6,1,2,1,62,1,3,5,1,6),_ApplPastTransStreamInvRspTimes_Type())
applPastTransStreamInvRspTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamInvRspTimes.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamInvRspTimes.setUnits(_M)
_ApplPastTransStreamPerforms_Type=Unsigned64TC
_ApplPastTransStreamPerforms_Object=MibTableColumn
applPastTransStreamPerforms=_ApplPastTransStreamPerforms_Object((1,3,6,1,2,1,62,1,3,5,1,7),_ApplPastTransStreamPerforms_Type())
applPastTransStreamPerforms.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamPerforms.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamPerforms.setUnits(_E)
_ApplPastTransStreamPerformsLow_Type=Unsigned32
_ApplPastTransStreamPerformsLow_Object=MibTableColumn
applPastTransStreamPerformsLow=_ApplPastTransStreamPerformsLow_Object((1,3,6,1,2,1,62,1,3,5,1,8),_ApplPastTransStreamPerformsLow_Type())
applPastTransStreamPerformsLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamPerformsLow.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamPerformsLow.setUnits(_E)
_ApplPastTransStreamPrfCumTimes_Type=Unsigned32
_ApplPastTransStreamPrfCumTimes_Object=MibTableColumn
applPastTransStreamPrfCumTimes=_ApplPastTransStreamPrfCumTimes_Object((1,3,6,1,2,1,62,1,3,5,1,9),_ApplPastTransStreamPrfCumTimes_Type())
applPastTransStreamPrfCumTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamPrfCumTimes.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamPrfCumTimes.setUnits(_M)
_ApplPastTransStreamPrfRspTimes_Type=Unsigned32
_ApplPastTransStreamPrfRspTimes_Object=MibTableColumn
applPastTransStreamPrfRspTimes=_ApplPastTransStreamPrfRspTimes_Object((1,3,6,1,2,1,62,1,3,5,1,10),_ApplPastTransStreamPrfRspTimes_Type())
applPastTransStreamPrfRspTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransStreamPrfRspTimes.setStatus(_A)
if mibBuilder.loadTexts:applPastTransStreamPrfRspTimes.setUnits(_M)
_ApplPastTransFlowTable_Object=MibTable
applPastTransFlowTable=_ApplPastTransFlowTable_Object((1,3,6,1,2,1,62,1,3,6))
if mibBuilder.loadTexts:applPastTransFlowTable.setStatus(_A)
_ApplPastTransFlowEntry_Object=MibTableRow
applPastTransFlowEntry=_ApplPastTransFlowEntry_Object((1,3,6,1,2,1,62,1,3,6,1))
applPastTransFlowEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_P),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:applPastTransFlowEntry.setStatus(_A)
class _ApplPastTransFlowDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_ApplPastTransFlowDirection_Type.__name__=_K
_ApplPastTransFlowDirection_Object=MibTableColumn
applPastTransFlowDirection=_ApplPastTransFlowDirection_Object((1,3,6,1,2,1,62,1,3,6,1,1),_ApplPastTransFlowDirection_Type())
applPastTransFlowDirection.setMaxAccess(_J)
if mibBuilder.loadTexts:applPastTransFlowDirection.setStatus(_A)
class _ApplPastTransFlowReqRsp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_ApplPastTransFlowReqRsp_Type.__name__=_K
_ApplPastTransFlowReqRsp_Object=MibTableColumn
applPastTransFlowReqRsp=_ApplPastTransFlowReqRsp_Object((1,3,6,1,2,1,62,1,3,6,1,2),_ApplPastTransFlowReqRsp_Type())
applPastTransFlowReqRsp.setMaxAccess(_J)
if mibBuilder.loadTexts:applPastTransFlowReqRsp.setStatus(_A)
_ApplPastTransFlowTrans_Type=Unsigned64TC
_ApplPastTransFlowTrans_Object=MibTableColumn
applPastTransFlowTrans=_ApplPastTransFlowTrans_Object((1,3,6,1,2,1,62,1,3,6,1,3),_ApplPastTransFlowTrans_Type())
applPastTransFlowTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransFlowTrans.setStatus(_A)
if mibBuilder.loadTexts:applPastTransFlowTrans.setUnits(_E)
_ApplPastTransFlowTransLow_Type=Unsigned32
_ApplPastTransFlowTransLow_Object=MibTableColumn
applPastTransFlowTransLow=_ApplPastTransFlowTransLow_Object((1,3,6,1,2,1,62,1,3,6,1,4),_ApplPastTransFlowTransLow_Type())
applPastTransFlowTransLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransFlowTransLow.setStatus(_A)
if mibBuilder.loadTexts:applPastTransFlowTransLow.setUnits(_E)
_ApplPastTransFlowBytes_Type=Unsigned64TC
_ApplPastTransFlowBytes_Object=MibTableColumn
applPastTransFlowBytes=_ApplPastTransFlowBytes_Object((1,3,6,1,2,1,62,1,3,6,1,5),_ApplPastTransFlowBytes_Type())
applPastTransFlowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransFlowBytes.setStatus(_A)
if mibBuilder.loadTexts:applPastTransFlowBytes.setUnits(_D)
_ApplPastTransFlowBytesLow_Type=Unsigned32
_ApplPastTransFlowBytesLow_Object=MibTableColumn
applPastTransFlowBytesLow=_ApplPastTransFlowBytesLow_Object((1,3,6,1,2,1,62,1,3,6,1,6),_ApplPastTransFlowBytesLow_Type())
applPastTransFlowBytesLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransFlowBytesLow.setStatus(_A)
if mibBuilder.loadTexts:applPastTransFlowBytesLow.setUnits(_D)
class _ApplPastTransFlowTime_Type(DateAndTime):defaultHexValue=_L
_ApplPastTransFlowTime_Type.__name__=_I
_ApplPastTransFlowTime_Object=MibTableColumn
applPastTransFlowTime=_ApplPastTransFlowTime_Object((1,3,6,1,2,1,62,1,3,6,1,7),_ApplPastTransFlowTime_Type())
applPastTransFlowTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransFlowTime.setStatus(_A)
_ApplPastTransKindTable_Object=MibTable
applPastTransKindTable=_ApplPastTransKindTable_Object((1,3,6,1,2,1,62,1,3,7))
if mibBuilder.loadTexts:applPastTransKindTable.setStatus(_A)
_ApplPastTransKindEntry_Object=MibTableRow
applPastTransKindEntry=_ApplPastTransKindEntry_Object((1,3,6,1,2,1,62,1,3,7,1))
applPastTransKindEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_P),(0,_B,_d),(0,_B,_e),(0,_B,_p))
if mibBuilder.loadTexts:applPastTransKindEntry.setStatus(_A)
class _ApplPastTransKind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApplPastTransKind_Type.__name__=_F
_ApplPastTransKind_Object=MibTableColumn
applPastTransKind=_ApplPastTransKind_Object((1,3,6,1,2,1,62,1,3,7,1,1),_ApplPastTransKind_Type())
applPastTransKind.setMaxAccess(_J)
if mibBuilder.loadTexts:applPastTransKind.setStatus(_A)
_ApplPastTransKindTrans_Type=Unsigned64TC
_ApplPastTransKindTrans_Object=MibTableColumn
applPastTransKindTrans=_ApplPastTransKindTrans_Object((1,3,6,1,2,1,62,1,3,7,1,2),_ApplPastTransKindTrans_Type())
applPastTransKindTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransKindTrans.setStatus(_A)
if mibBuilder.loadTexts:applPastTransKindTrans.setUnits(_E)
_ApplPastTransKindTransLow_Type=Unsigned32
_ApplPastTransKindTransLow_Object=MibTableColumn
applPastTransKindTransLow=_ApplPastTransKindTransLow_Object((1,3,6,1,2,1,62,1,3,7,1,3),_ApplPastTransKindTransLow_Type())
applPastTransKindTransLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransKindTransLow.setStatus(_A)
if mibBuilder.loadTexts:applPastTransKindTransLow.setUnits(_E)
_ApplPastTransKindBytes_Type=Unsigned64TC
_ApplPastTransKindBytes_Object=MibTableColumn
applPastTransKindBytes=_ApplPastTransKindBytes_Object((1,3,6,1,2,1,62,1,3,7,1,4),_ApplPastTransKindBytes_Type())
applPastTransKindBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransKindBytes.setStatus(_A)
if mibBuilder.loadTexts:applPastTransKindBytes.setUnits(_D)
_ApplPastTransKindBytesLow_Type=Unsigned32
_ApplPastTransKindBytesLow_Object=MibTableColumn
applPastTransKindBytesLow=_ApplPastTransKindBytesLow_Object((1,3,6,1,2,1,62,1,3,7,1,5),_ApplPastTransKindBytesLow_Type())
applPastTransKindBytesLow.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransKindBytesLow.setStatus(_A)
if mibBuilder.loadTexts:applPastTransKindBytesLow.setUnits(_D)
class _ApplPastTransKindTime_Type(DateAndTime):defaultHexValue=_L
_ApplPastTransKindTime_Type.__name__=_I
_ApplPastTransKindTime_Object=MibTableColumn
applPastTransKindTime=_ApplPastTransKindTime_Object((1,3,6,1,2,1,62,1,3,7,1,6),_ApplPastTransKindTime_Type())
applPastTransKindTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applPastTransKindTime.setStatus(_A)
_ApplElmtRunControlGroup_ObjectIdentity=ObjectIdentity
applElmtRunControlGroup=_ApplElmtRunControlGroup_ObjectIdentity((1,3,6,1,2,1,62,1,4))
_ApplElmtRunStatusTable_Object=MibTable
applElmtRunStatusTable=_ApplElmtRunStatusTable_Object((1,3,6,1,2,1,62,1,4,1))
if mibBuilder.loadTexts:applElmtRunStatusTable.setStatus(_A)
_ApplElmtRunStatusEntry_Object=MibTableRow
applElmtRunStatusEntry=_ApplElmtRunStatusEntry_Object((1,3,6,1,2,1,62,1,4,1,1))
applElmtRunStatusEntry.setIndexNames((0,_R,_S))
if mibBuilder.loadTexts:applElmtRunStatusEntry.setStatus(_A)
_ApplElmtRunStatusSuspended_Type=TruthValue
_ApplElmtRunStatusSuspended_Object=MibTableColumn
applElmtRunStatusSuspended=_ApplElmtRunStatusSuspended_Object((1,3,6,1,2,1,62,1,4,1,1,1),_ApplElmtRunStatusSuspended_Type())
applElmtRunStatusSuspended.setMaxAccess(_C)
if mibBuilder.loadTexts:applElmtRunStatusSuspended.setStatus(_A)
_ApplElmtRunStatusHeapUsage_Type=Unsigned32
_ApplElmtRunStatusHeapUsage_Object=MibTableColumn
applElmtRunStatusHeapUsage=_ApplElmtRunStatusHeapUsage_Object((1,3,6,1,2,1,62,1,4,1,1,2),_ApplElmtRunStatusHeapUsage_Type())
applElmtRunStatusHeapUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:applElmtRunStatusHeapUsage.setStatus(_A)
if mibBuilder.loadTexts:applElmtRunStatusHeapUsage.setUnits(_D)
_ApplElmtRunStatusOpenConnections_Type=Unsigned32
_ApplElmtRunStatusOpenConnections_Object=MibTableColumn
applElmtRunStatusOpenConnections=_ApplElmtRunStatusOpenConnections_Object((1,3,6,1,2,1,62,1,4,1,1,3),_ApplElmtRunStatusOpenConnections_Type())
applElmtRunStatusOpenConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:applElmtRunStatusOpenConnections.setStatus(_A)
if mibBuilder.loadTexts:applElmtRunStatusOpenConnections.setUnits('connections')
_ApplElmtRunStatusOpenFiles_Type=Gauge32
_ApplElmtRunStatusOpenFiles_Object=MibTableColumn
applElmtRunStatusOpenFiles=_ApplElmtRunStatusOpenFiles_Object((1,3,6,1,2,1,62,1,4,1,1,4),_ApplElmtRunStatusOpenFiles_Type())
applElmtRunStatusOpenFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:applElmtRunStatusOpenFiles.setStatus(_A)
if mibBuilder.loadTexts:applElmtRunStatusOpenFiles.setUnits('files')
class _ApplElmtRunStatusLastErrorMsg_Type(SnmpAdminString):defaultValue=OctetString('')
_ApplElmtRunStatusLastErrorMsg_Type.__name__=_F
_ApplElmtRunStatusLastErrorMsg_Object=MibTableColumn
applElmtRunStatusLastErrorMsg=_ApplElmtRunStatusLastErrorMsg_Object((1,3,6,1,2,1,62,1,4,1,1,5),_ApplElmtRunStatusLastErrorMsg_Type())
applElmtRunStatusLastErrorMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:applElmtRunStatusLastErrorMsg.setStatus(_A)
class _ApplElmtRunStatusLastErrorTime_Type(DateAndTime):defaultHexValue=_L
_ApplElmtRunStatusLastErrorTime_Type.__name__=_I
_ApplElmtRunStatusLastErrorTime_Object=MibTableColumn
applElmtRunStatusLastErrorTime=_ApplElmtRunStatusLastErrorTime_Object((1,3,6,1,2,1,62,1,4,1,1,6),_ApplElmtRunStatusLastErrorTime_Type())
applElmtRunStatusLastErrorTime.setMaxAccess(_C)
if mibBuilder.loadTexts:applElmtRunStatusLastErrorTime.setStatus(_A)
_ApplElmtRunControlTable_Object=MibTable
applElmtRunControlTable=_ApplElmtRunControlTable_Object((1,3,6,1,2,1,62,1,4,2))
if mibBuilder.loadTexts:applElmtRunControlTable.setStatus(_A)
_ApplElmtRunControlEntry_Object=MibTableRow
applElmtRunControlEntry=_ApplElmtRunControlEntry_Object((1,3,6,1,2,1,62,1,4,2,1))
applElmtRunControlEntry.setIndexNames((0,_R,_S))
if mibBuilder.loadTexts:applElmtRunControlEntry.setStatus(_A)
class _ApplElmtRunControlSuspend_Type(TruthValue):defaultValue=2
_ApplElmtRunControlSuspend_Type.__name__=_Z
_ApplElmtRunControlSuspend_Object=MibTableColumn
applElmtRunControlSuspend=_ApplElmtRunControlSuspend_Object((1,3,6,1,2,1,62,1,4,2,1,1),_ApplElmtRunControlSuspend_Type())
applElmtRunControlSuspend.setMaxAccess(_Q)
if mibBuilder.loadTexts:applElmtRunControlSuspend.setStatus(_A)
_ApplElmtRunControlReconfigure_Type=TestAndIncr
_ApplElmtRunControlReconfigure_Object=MibTableColumn
applElmtRunControlReconfigure=_ApplElmtRunControlReconfigure_Object((1,3,6,1,2,1,62,1,4,2,1,2),_ApplElmtRunControlReconfigure_Type())
applElmtRunControlReconfigure.setMaxAccess(_Q)
if mibBuilder.loadTexts:applElmtRunControlReconfigure.setStatus(_A)
class _ApplElmtRunControlTerminate_Type(TruthValue):defaultValue=2
_ApplElmtRunControlTerminate_Type.__name__=_Z
_ApplElmtRunControlTerminate_Object=MibTableColumn
applElmtRunControlTerminate=_ApplElmtRunControlTerminate_Object((1,3,6,1,2,1,62,1,4,2,1,3),_ApplElmtRunControlTerminate_Type())
applElmtRunControlTerminate.setMaxAccess(_Q)
if mibBuilder.loadTexts:applElmtRunControlTerminate.setStatus(_A)
_ApplicationMibConformance_ObjectIdentity=ObjectIdentity
applicationMibConformance=_ApplicationMibConformance_ObjectIdentity((1,3,6,1,2,1,62,2))
_ApplicationMibGroups_ObjectIdentity=ObjectIdentity
applicationMibGroups=_ApplicationMibGroups_ObjectIdentity((1,3,6,1,2,1,62,2,1))
applicationMonitorGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,1))
applicationMonitorGroup.setObjects(*((_B,_q),(_B,_V),(_B,_T),(_B,_a),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:applicationMonitorGroup.setStatus(_A)
applicationFastMonitorGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,2))
applicationFastMonitorGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:applicationFastMonitorGroup.setStatus(_A)
applicationTransactGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,3))
applicationTransactGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:applicationTransactGroup.setStatus(_A)
applicationFastTransactGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,4))
applicationFastTransactGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:applicationFastTransactGroup.setStatus(_A)
applicationHistoryGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,5))
applicationHistoryGroup.setObjects(*((_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:applicationHistoryGroup.setStatus(_A)
applicationFastHistoryGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,6))
applicationFastHistoryGroup.setObjects(*((_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az)))
if mibBuilder.loadTexts:applicationFastHistoryGroup.setStatus(_A)
applicationTransHistoryGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,7))
applicationTransHistoryGroup.setObjects(*((_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC)))
if mibBuilder.loadTexts:applicationTransHistoryGroup.setStatus(_A)
applicationFastTransHistoryGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,8))
applicationFastTransHistoryGroup.setObjects(*((_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI)))
if mibBuilder.loadTexts:applicationFastTransHistoryGroup.setStatus(_A)
applicationRunGroup=ObjectGroup((1,3,6,1,2,1,62,2,1,9))
applicationRunGroup.setObjects(*((_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR)))
if mibBuilder.loadTexts:applicationRunGroup.setStatus(_A)
applicationMibCompliance=ModuleCompliance((1,3,6,1,2,1,62,2,2))
applicationMibCompliance.setObjects(*((_B,_BS),(_B,_BT),(_B,_BU)))
if mibBuilder.loadTexts:applicationMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Unsigned64TC':Unsigned64TC,_U:ApplTAddress,'applicationMib':applicationMib,'applicationMibObjects':applicationMibObjects,'applServiceGroup':applServiceGroup,'applSrvNameToSrvInstTable':applSrvNameToSrvInstTable,'applSrvNameToSrvInstEntry':applSrvNameToSrvInstEntry,_q:applSrvInstQual,'applSrvInstToSrvNameTable':applSrvInstToSrvNameTable,'applSrvInstToSrvNameEntry':applSrvInstToSrvNameEntry,_V:applSrvName,'applSrvInstToRunApplElmtTable':applSrvInstToRunApplElmtTable,'applSrvInstToRunApplElmtEntry':applSrvInstToRunApplElmtEntry,_T:applSrvIndex,'applRunApplElmtToSrvInstTable':applRunApplElmtToSrvInstTable,'applRunApplElmtToSrvInstEntry':applRunApplElmtToSrvInstEntry,_a:applSrvInstance,'applChannelGroup':applChannelGroup,'applOpenChannelTable':applOpenChannelTable,'applOpenChannelEntry':applOpenChannelEntry,_G:applElmtOrSvc,_H:applElmtOrSvcId,_O:applOpenChannelIndex,_r:applOpenChannelOpenTime,_AA:applOpenChannelReadRequests,_s:applOpenChannelReadRequestsLow,_t:applOpenChannelReadFailures,_AB:applOpenChannelBytesRead,_u:applOpenChannelBytesReadLow,_v:applOpenChannelLastReadTime,_AC:applOpenChannelWriteRequests,_w:applOpenChannelWriteRequestsLow,_x:applOpenChannelWriteFailures,_AD:applOpenChannelBytesWritten,_y:applOpenChannelBytesWrittenLow,_z:applOpenChannelLastWriteTime,'applOpenFileTable':applOpenFileTable,'applOpenFileEntry':applOpenFileEntry,_A0:applOpenFileName,_A1:applOpenFileSizeHigh,_A2:applOpenFileSizeLow,_A3:applOpenFileMode,'applOpenConnectionTable':applOpenConnectionTable,'applOpenConnectionEntry':applOpenConnectionEntry,_A4:applOpenConnectionTransport,_A5:applOpenConnectionNearEndAddr,_A6:applOpenConnectionNearEndpoint,_A7:applOpenConnectionFarEndAddr,_A8:applOpenConnectionFarEndpoint,_A9:applOpenConnectionApplication,'applTransactionStreamTable':applTransactionStreamTable,'applTransactionStreamEntry':applTransactionStreamEntry,_AE:applTransactStreamDescr,_AF:applTransactStreamUnitOfWork,_AS:applTransactStreamInvokes,_AG:applTransactStreamInvokesLow,_AH:applTransactStreamInvCumTimes,_AI:applTransactStreamInvRspTimes,_AT:applTransactStreamPerforms,_AJ:applTransactStreamPerformsLow,_AK:applTransactStreamPrfCumTimes,_AL:applTransactStreamPrfRspTimes,'applTransactFlowTable':applTransactFlowTable,'applTransactFlowEntry':applTransactFlowEntry,_b:applTransactFlowDirection,_c:applTransactFlowReqRsp,_AU:applTransactFlowTrans,_AM:applTransactFlowTransLow,_AV:applTransactFlowBytes,_AN:applTransactFlowBytesLow,_AO:applTransactFlowTime,'applTransactKindTable':applTransactKindTable,'applTransactKindEntry':applTransactKindEntry,_n:applTransactKind,_AW:applTransactKindTrans,_AP:applTransactKindTransLow,_AX:applTransactKindBytes,_AQ:applTransactKindBytesLow,_AR:applTransactKindTime,'applPastChannelGroup':applPastChannelGroup,'applPastChannelControlTable':applPastChannelControlTable,'applPastChannelControlEntry':applPastChannelControlEntry,_AY:applPastChannelControlCollect,_AZ:applPastChannelControlMaxRows,_Aa:applPastChannelControlTimeLimit,_Ab:applPastChannelControlRemItems,'applPastChannelTable':applPastChannelTable,'applPastChannelEntry':applPastChannelEntry,_P:applPastChannelIndex,_Ac:applPastChannelOpenTime,_Ad:applPastChannelCloseTime,_Aw:applPastChannelReadRequests,_Ae:applPastChannelReadReqsLow,_Af:applPastChannelReadFailures,_Ax:applPastChannelBytesRead,_Ag:applPastChannelBytesReadLow,_Ah:applPastChannelLastReadTime,_Ay:applPastChannelWriteRequests,_Ai:applPastChannelWriteReqsLow,_Aj:applPastChannelWriteFailures,_Az:applPastChannelBytesWritten,_Ak:applPastChannelBytesWritLow,_Al:applPastChannelLastWriteTime,'applPastFileTable':applPastFileTable,'applPastFileEntry':applPastFileEntry,_Am:applPastFileName,_An:applPastFileSizeHigh,_Ao:applPastFileSizeLow,_Ap:applPastFileMode,'applPastConTable':applPastConTable,'applPastConEntry':applPastConEntry,_Aq:applPastConTransport,_Ar:applPastConNearEndAddr,_As:applPastConNearEndpoint,_At:applPastConFarEndAddr,_Au:applPastConFarEndpoint,_Av:applPastConApplication,'applPastTransStreamTable':applPastTransStreamTable,'applPastTransStreamEntry':applPastTransStreamEntry,_A_:applPastTransStreamDescr,_B0:applPastTransStreamUnitOfWork,_BI:applPastTransStreamInvokes,_B1:applPastTransStreamInvokesLow,_B2:applPastTransStreamInvCumTimes,_B3:applPastTransStreamInvRspTimes,_BH:applPastTransStreamPerforms,_B4:applPastTransStreamPerformsLow,_B5:applPastTransStreamPrfCumTimes,_B6:applPastTransStreamPrfRspTimes,'applPastTransFlowTable':applPastTransFlowTable,'applPastTransFlowEntry':applPastTransFlowEntry,_d:applPastTransFlowDirection,_e:applPastTransFlowReqRsp,_BD:applPastTransFlowTrans,_B7:applPastTransFlowTransLow,_BE:applPastTransFlowBytes,_B8:applPastTransFlowBytesLow,_B9:applPastTransFlowTime,'applPastTransKindTable':applPastTransKindTable,'applPastTransKindEntry':applPastTransKindEntry,_p:applPastTransKind,_BF:applPastTransKindTrans,_BA:applPastTransKindTransLow,_BG:applPastTransKindBytes,_BB:applPastTransKindBytesLow,_BC:applPastTransKindTime,'applElmtRunControlGroup':applElmtRunControlGroup,'applElmtRunStatusTable':applElmtRunStatusTable,'applElmtRunStatusEntry':applElmtRunStatusEntry,_BJ:applElmtRunStatusSuspended,_BK:applElmtRunStatusHeapUsage,_BL:applElmtRunStatusOpenConnections,_BM:applElmtRunStatusOpenFiles,_BN:applElmtRunStatusLastErrorMsg,_BO:applElmtRunStatusLastErrorTime,'applElmtRunControlTable':applElmtRunControlTable,'applElmtRunControlEntry':applElmtRunControlEntry,_BP:applElmtRunControlSuspend,_BQ:applElmtRunControlReconfigure,_BR:applElmtRunControlTerminate,'applicationMibConformance':applicationMibConformance,'applicationMibGroups':applicationMibGroups,_BS:applicationMonitorGroup,'applicationFastMonitorGroup':applicationFastMonitorGroup,'applicationTransactGroup':applicationTransactGroup,'applicationFastTransactGroup':applicationFastTransactGroup,_BT:applicationHistoryGroup,'applicationFastHistoryGroup':applicationFastHistoryGroup,'applicationTransHistoryGroup':applicationTransHistoryGroup,'applicationFastTransHistoryGroup':applicationFastTransHistoryGroup,_BU:applicationRunGroup,'applicationMibCompliance':applicationMibCompliance})