_U='posPosConnectState'
_T='posAppState'
_S='posPadIfIndex'
_R='counting'
_Q='posAsyAppIfIndex'
_P='posMapDes'
_O='OctetString'
_N='enable'
_M='disable'
_L='posFCMIfIndex'
_K='posPosId'
_J='open'
_I='close'
_H='posAppId'
_G='read-write'
_F='Counter32'
_E='read-create'
_D='HUAWEI-POS-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huawei,mlsr=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','huawei','mlsr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_F,'Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
pos=ModuleIdentity((1,3,6,1,4,1,2011,2,33,8))
if mibBuilder.loadTexts:pos.setRevisions(('2004-10-12 00:00','2004-07-02 00:00'))
_PosAppTable_Object=MibTable
posAppTable=_PosAppTable_Object((1,3,6,1,4,1,2011,2,33,8,1))
if mibBuilder.loadTexts:posAppTable.setStatus(_A)
_PosAppEntry_Object=MibTableRow
posAppEntry=_PosAppEntry_Object((1,3,6,1,4,1,2011,2,33,8,1,1))
posAppEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:posAppEntry.setStatus(_A)
class _PosAppId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PosAppId_Type.__name__=_B
_PosAppId_Object=MibTableColumn
posAppId=_PosAppId_Object((1,3,6,1,4,1,2011,2,33,8,1,1,1),_PosAppId_Type())
posAppId.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppId.setStatus(_A)
class _PosAppConnectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('flow',2),('pad',3)))
_PosAppConnectMode_Type.__name__=_B
_PosAppConnectMode_Object=MibTableColumn
posAppConnectMode=_PosAppConnectMode_Object((1,3,6,1,4,1,2011,2,33,8,1,1,2),_PosAppConnectMode_Type())
posAppConnectMode.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppConnectMode.setStatus(_A)
class _PosAppState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noset',1),('down',2),('up',3),('ok',4),('kept',5),('linking',6),('linked',7)))
_PosAppState_Type.__name__=_B
_PosAppState_Object=MibTableColumn
posAppState=_PosAppState_Object((1,3,6,1,4,1,2011,2,33,8,1,1,3),_PosAppState_Type())
posAppState.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppState.setStatus(_A)
class _PosAppIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PosAppIfIndex_Type.__name__=_B
_PosAppIfIndex_Object=MibTableColumn
posAppIfIndex=_PosAppIfIndex_Object((1,3,6,1,4,1,2011,2,33,8,1,1,4),_PosAppIfIndex_Type())
posAppIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppIfIndex.setStatus(_A)
_PosAppHostIP_Type=IpAddress
_PosAppHostIP_Object=MibTableColumn
posAppHostIP=_PosAppHostIP_Object((1,3,6,1,4,1,2011,2,33,8,1,1,5),_PosAppHostIP_Type())
posAppHostIP.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppHostIP.setStatus(_A)
class _PosAppPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PosAppPort_Type.__name__=_B
_PosAppPort_Object=MibTableColumn
posAppPort=_PosAppPort_Object((1,3,6,1,4,1,2011,2,33,8,1,1,6),_PosAppPort_Type())
posAppPort.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppPort.setStatus(_A)
_PosAppSourceIp_Type=IpAddress
_PosAppSourceIp_Object=MibTableColumn
posAppSourceIp=_PosAppSourceIp_Object((1,3,6,1,4,1,2011,2,33,8,1,1,7),_PosAppSourceIp_Type())
posAppSourceIp.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppSourceIp.setStatus(_A)
class _PosAppRecvPacCounter_Type(Counter32):defaultValue=0
_PosAppRecvPacCounter_Type.__name__=_F
_PosAppRecvPacCounter_Object=MibTableColumn
posAppRecvPacCounter=_PosAppRecvPacCounter_Object((1,3,6,1,4,1,2011,2,33,8,1,1,8),_PosAppRecvPacCounter_Type())
posAppRecvPacCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppRecvPacCounter.setStatus(_A)
class _PosAppErrPacCounter_Type(Counter32):defaultValue=0
_PosAppErrPacCounter_Type.__name__=_F
_PosAppErrPacCounter_Object=MibTableColumn
posAppErrPacCounter=_PosAppErrPacCounter_Object((1,3,6,1,4,1,2011,2,33,8,1,1,9),_PosAppErrPacCounter_Type())
posAppErrPacCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppErrPacCounter.setStatus(_A)
class _PosAppDistrErrCounter_Type(Counter32):defaultValue=0
_PosAppDistrErrCounter_Type.__name__=_F
_PosAppDistrErrCounter_Object=MibTableColumn
posAppDistrErrCounter=_PosAppDistrErrCounter_Object((1,3,6,1,4,1,2011,2,33,8,1,1,10),_PosAppDistrErrCounter_Type())
posAppDistrErrCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppDistrErrCounter.setStatus(_A)
class _PosAppBuffedCounter_Type(Counter32):defaultValue=0
_PosAppBuffedCounter_Type.__name__=_F
_PosAppBuffedCounter_Object=MibTableColumn
posAppBuffedCounter=_PosAppBuffedCounter_Object((1,3,6,1,4,1,2011,2,33,8,1,1,11),_PosAppBuffedCounter_Type())
posAppBuffedCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppBuffedCounter.setStatus(_A)
class _PosAppDiscardedCounter_Type(Counter32):defaultValue=0
_PosAppDiscardedCounter_Type.__name__=_F
_PosAppDiscardedCounter_Object=MibTableColumn
posAppDiscardedCounter=_PosAppDiscardedCounter_Object((1,3,6,1,4,1,2011,2,33,8,1,1,12),_PosAppDiscardedCounter_Type())
posAppDiscardedCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppDiscardedCounter.setStatus(_A)
class _PosAppDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_PosAppDebug_Type.__name__=_B
_PosAppDebug_Object=MibTableColumn
posAppDebug=_PosAppDebug_Object((1,3,6,1,4,1,2011,2,33,8,1,1,13),_PosAppDebug_Type())
posAppDebug.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppDebug.setStatus(_A)
_PosAppRowStatus_Type=RowStatus
_PosAppRowStatus_Object=MibTableColumn
posAppRowStatus=_PosAppRowStatus_Object((1,3,6,1,4,1,2011,2,33,8,1,1,14),_PosAppRowStatus_Type())
posAppRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppRowStatus.setStatus(_A)
class _PosAppX121Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_PosAppX121Addr_Type.__name__=_O
_PosAppX121Addr_Object=MibTableColumn
posAppX121Addr=_PosAppX121Addr_Object((1,3,6,1,4,1,2011,2,33,8,1,1,15),_PosAppX121Addr_Type())
posAppX121Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:posAppX121Addr.setStatus(_A)
_PosInterTable_Object=MibTable
posInterTable=_PosInterTable_Object((1,3,6,1,4,1,2011,2,33,8,2))
if mibBuilder.loadTexts:posInterTable.setStatus(_A)
_PosInterEntry_Object=MibTableRow
posInterEntry=_PosInterEntry_Object((1,3,6,1,4,1,2011,2,33,8,2,1))
posInterEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:posInterEntry.setStatus(_A)
class _PosPosId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PosPosId_Type.__name__=_B
_PosPosId_Object=MibTableColumn
posPosId=_PosPosId_Object((1,3,6,1,4,1,2011,2,33,8,2,1,1),_PosPosId_Type())
posPosId.setMaxAccess(_C)
if mibBuilder.loadTexts:posPosId.setStatus(_A)
class _PosPosIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PosPosIfIndex_Type.__name__=_B
_PosPosIfIndex_Object=MibTableColumn
posPosIfIndex=_PosPosIfIndex_Object((1,3,6,1,4,1,2011,2,33,8,2,1,2),_PosPosIfIndex_Type())
posPosIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:posPosIfIndex.setStatus(_A)
class _PosPosConnectState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noset',1),('down',2),('up',3),('ok',4)))
_PosPosConnectState_Type.__name__=_B
_PosPosConnectState_Object=MibTableColumn
posPosConnectState=_PosPosConnectState_Object((1,3,6,1,4,1,2011,2,33,8,2,1,3),_PosPosConnectState_Type())
posPosConnectState.setMaxAccess(_C)
if mibBuilder.loadTexts:posPosConnectState.setStatus(_A)
class _PosPosRecvPacCounter_Type(Counter32):defaultValue=0
_PosPosRecvPacCounter_Type.__name__=_F
_PosPosRecvPacCounter_Object=MibTableColumn
posPosRecvPacCounter=_PosPosRecvPacCounter_Object((1,3,6,1,4,1,2011,2,33,8,2,1,4),_PosPosRecvPacCounter_Type())
posPosRecvPacCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posPosRecvPacCounter.setStatus(_A)
class _PosPosErrPacCounter_Type(Counter32):defaultValue=0
_PosPosErrPacCounter_Type.__name__=_F
_PosPosErrPacCounter_Object=MibTableColumn
posPosErrPacCounter=_PosPosErrPacCounter_Object((1,3,6,1,4,1,2011,2,33,8,2,1,5),_PosPosErrPacCounter_Type())
posPosErrPacCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posPosErrPacCounter.setStatus(_A)
class _PosPosMapErrCounter_Type(Counter32):defaultValue=0
_PosPosMapErrCounter_Type.__name__=_F
_PosPosMapErrCounter_Object=MibTableColumn
posPosMapErrCounter=_PosPosMapErrCounter_Object((1,3,6,1,4,1,2011,2,33,8,2,1,6),_PosPosMapErrCounter_Type())
posPosMapErrCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posPosMapErrCounter.setStatus(_A)
class _PosPosBuffedCounter_Type(Counter32):defaultValue=0
_PosPosBuffedCounter_Type.__name__=_F
_PosPosBuffedCounter_Object=MibTableColumn
posPosBuffedCounter=_PosPosBuffedCounter_Object((1,3,6,1,4,1,2011,2,33,8,2,1,7),_PosPosBuffedCounter_Type())
posPosBuffedCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posPosBuffedCounter.setStatus(_A)
class _PosPosDiscardedCounter_Type(Counter32):defaultValue=0
_PosPosDiscardedCounter_Type.__name__=_F
_PosPosDiscardedCounter_Object=MibTableColumn
posPosDiscardedCounter=_PosPosDiscardedCounter_Object((1,3,6,1,4,1,2011,2,33,8,2,1,8),_PosPosDiscardedCounter_Type())
posPosDiscardedCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posPosDiscardedCounter.setStatus(_A)
class _PosPosInterDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_PosPosInterDebug_Type.__name__=_B
_PosPosInterDebug_Object=MibTableColumn
posPosInterDebug=_PosPosInterDebug_Object((1,3,6,1,4,1,2011,2,33,8,2,1,9),_PosPosInterDebug_Type())
posPosInterDebug.setMaxAccess(_E)
if mibBuilder.loadTexts:posPosInterDebug.setStatus(_A)
_PosPosInterRowStatus_Type=RowStatus
_PosPosInterRowStatus_Object=MibTableColumn
posPosInterRowStatus=_PosPosInterRowStatus_Object((1,3,6,1,4,1,2011,2,33,8,2,1,10),_PosPosInterRowStatus_Type())
posPosInterRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:posPosInterRowStatus.setStatus(_A)
class _PosPosInterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fcm',1),('asy',2),('pad-client',3),('pad-server',4)))
_PosPosInterType_Type.__name__=_B
_PosPosInterType_Object=MibTableColumn
posPosInterType=_PosPosInterType_Object((1,3,6,1,4,1,2011,2,33,8,2,1,11),_PosPosInterType_Type())
posPosInterType.setMaxAccess(_E)
if mibBuilder.loadTexts:posPosInterType.setStatus(_A)
_PosMapTable_Object=MibTable
posMapTable=_PosMapTable_Object((1,3,6,1,4,1,2011,2,33,8,3))
if mibBuilder.loadTexts:posMapTable.setStatus(_A)
_PosMapEntry_Object=MibTableRow
posMapEntry=_PosMapEntry_Object((1,3,6,1,4,1,2011,2,33,8,3,1))
posMapEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:posMapEntry.setStatus(_A)
class _PosMapDes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_PosMapDes_Type.__name__=_B
_PosMapDes_Object=MibTableColumn
posMapDes=_PosMapDes_Object((1,3,6,1,4,1,2011,2,33,8,3,1,1),_PosMapDes_Type())
posMapDes.setMaxAccess(_E)
if mibBuilder.loadTexts:posMapDes.setStatus(_A)
class _PosMapAppNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PosMapAppNumber_Type.__name__=_B
_PosMapAppNumber_Object=MibTableColumn
posMapAppNumber=_PosMapAppNumber_Object((1,3,6,1,4,1,2011,2,33,8,3,1,2),_PosMapAppNumber_Type())
posMapAppNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:posMapAppNumber.setStatus(_A)
_PosMapRowStatus_Type=RowStatus
_PosMapRowStatus_Object=MibTableColumn
posMapRowStatus=_PosMapRowStatus_Object((1,3,6,1,4,1,2011,2,33,8,3,1,3),_PosMapRowStatus_Type())
posMapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:posMapRowStatus.setStatus(_A)
_PosAsyAppTable_Object=MibTable
posAsyAppTable=_PosAsyAppTable_Object((1,3,6,1,4,1,2011,2,33,8,4))
if mibBuilder.loadTexts:posAsyAppTable.setStatus(_A)
_PosAsyAppEntry_Object=MibTableRow
posAsyAppEntry=_PosAsyAppEntry_Object((1,3,6,1,4,1,2011,2,33,8,4,1))
posAsyAppEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:posAsyAppEntry.setStatus(_A)
class _PosAsyAppIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PosAsyAppIfIndex_Type.__name__=_B
_PosAsyAppIfIndex_Object=MibTableColumn
posAsyAppIfIndex=_PosAsyAppIfIndex_Object((1,3,6,1,4,1,2011,2,33,8,4,1,1),_PosAsyAppIfIndex_Type())
posAsyAppIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:posAsyAppIfIndex.setStatus(_A)
_PosAsyAppRowStatus_Type=RowStatus
_PosAsyAppRowStatus_Object=MibTableColumn
posAsyAppRowStatus=_PosAsyAppRowStatus_Object((1,3,6,1,4,1,2011,2,33,8,4,1,2),_PosAsyAppRowStatus_Type())
posAsyAppRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:posAsyAppRowStatus.setStatus(_A)
_PosFCMTable_Object=MibTable
posFCMTable=_PosFCMTable_Object((1,3,6,1,4,1,2011,2,33,8,5))
if mibBuilder.loadTexts:posFCMTable.setStatus(_A)
_PosFCMEntry_Object=MibTableRow
posFCMEntry=_PosFCMEntry_Object((1,3,6,1,4,1,2011,2,33,8,5,1))
posFCMEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:posFCMEntry.setStatus(_A)
class _PosFCMIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PosFCMIfIndex_Type.__name__=_B
_PosFCMIfIndex_Object=MibTableColumn
posFCMIfIndex=_PosFCMIfIndex_Object((1,3,6,1,4,1,2011,2,33,8,5,1,1),_PosFCMIfIndex_Type())
posFCMIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:posFCMIfIndex.setStatus(_A)
class _PosFCMTimeoutCounter_Type(Counter32):defaultValue=0
_PosFCMTimeoutCounter_Type.__name__=_F
_PosFCMTimeoutCounter_Object=MibTableColumn
posFCMTimeoutCounter=_PosFCMTimeoutCounter_Object((1,3,6,1,4,1,2011,2,33,8,5,1,3),_PosFCMTimeoutCounter_Type())
posFCMTimeoutCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posFCMTimeoutCounter.setStatus(_A)
class _PosFCMConnectFailCounter_Type(Counter32):defaultValue=0
_PosFCMConnectFailCounter_Type.__name__=_F
_PosFCMConnectFailCounter_Object=MibTableColumn
posFCMConnectFailCounter=_PosFCMConnectFailCounter_Object((1,3,6,1,4,1,2011,2,33,8,5,1,4),_PosFCMConnectFailCounter_Type())
posFCMConnectFailCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:posFCMConnectFailCounter.setStatus(_A)
class _PosAppSum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_PosAppSum_Type.__name__=_B
_PosAppSum_Object=MibScalar
posAppSum=_PosAppSum_Object((1,3,6,1,4,1,2011,2,33,8,6),_PosAppSum_Type())
posAppSum.setMaxAccess(_C)
if mibBuilder.loadTexts:posAppSum.setStatus(_A)
class _PosInterSum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_PosInterSum_Type.__name__=_B
_PosInterSum_Object=MibScalar
posInterSum=_PosInterSum_Object((1,3,6,1,4,1,2011,2,33,8,7),_PosInterSum_Type())
posInterSum.setMaxAccess(_C)
if mibBuilder.loadTexts:posInterSum.setStatus(_A)
class _PosEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_PosEnable_Type.__name__=_B
_PosEnable_Object=MibScalar
posEnable=_PosEnable_Object((1,3,6,1,4,1,2011,2,33,8,8),_PosEnable_Type())
posEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:posEnable.setStatus(_A)
class _PosAppDebugAll_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_PosAppDebugAll_Type.__name__=_B
_PosAppDebugAll_Object=MibScalar
posAppDebugAll=_PosAppDebugAll_Object((1,3,6,1,4,1,2011,2,33,8,9),_PosAppDebugAll_Type())
posAppDebugAll.setMaxAccess(_G)
if mibBuilder.loadTexts:posAppDebugAll.setStatus(_A)
class _PosPosDebugAll_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_PosPosDebugAll_Type.__name__=_B
_PosPosDebugAll_Object=MibScalar
posPosDebugAll=_PosPosDebugAll_Object((1,3,6,1,4,1,2011,2,33,8,10),_PosPosDebugAll_Type())
posPosDebugAll.setMaxAccess(_G)
if mibBuilder.loadTexts:posPosDebugAll.setStatus(_A)
class _PosClearPacCounter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_R,2)))
_PosClearPacCounter_Type.__name__=_B
_PosClearPacCounter_Object=MibScalar
posClearPacCounter=_PosClearPacCounter_Object((1,3,6,1,4,1,2011,2,33,8,11),_PosClearPacCounter_Type())
posClearPacCounter.setMaxAccess(_G)
if mibBuilder.loadTexts:posClearPacCounter.setStatus(_A)
class _PosClearFCMCounter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_R,2)))
_PosClearFCMCounter_Type.__name__=_B
_PosClearFCMCounter_Object=MibScalar
posClearFCMCounter=_PosClearFCMCounter_Object((1,3,6,1,4,1,2011,2,33,8,12),_PosClearFCMCounter_Type())
posClearFCMCounter.setMaxAccess(_G)
if mibBuilder.loadTexts:posClearFCMCounter.setStatus(_A)
class _PosEnableTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_PosEnableTrap_Type.__name__=_B
_PosEnableTrap_Object=MibScalar
posEnableTrap=_PosEnableTrap_Object((1,3,6,1,4,1,2011,2,33,8,13),_PosEnableTrap_Type())
posEnableTrap.setMaxAccess(_G)
if mibBuilder.loadTexts:posEnableTrap.setStatus(_A)
class _PosFCMAnswerTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2000))
_PosFCMAnswerTime_Type.__name__=_B
_PosFCMAnswerTime_Object=MibScalar
posFCMAnswerTime=_PosFCMAnswerTime_Object((1,3,6,1,4,1,2011,2,33,8,14),_PosFCMAnswerTime_Type())
posFCMAnswerTime.setMaxAccess(_G)
if mibBuilder.loadTexts:posFCMAnswerTime.setStatus(_A)
class _PosFCMTradeTime_Type(Integer32):defaultValue=60000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30000,1200000))
_PosFCMTradeTime_Type.__name__=_B
_PosFCMTradeTime_Object=MibScalar
posFCMTradeTime=_PosFCMTradeTime_Object((1,3,6,1,4,1,2011,2,33,8,15),_PosFCMTradeTime_Type())
posFCMTradeTime.setMaxAccess(_G)
if mibBuilder.loadTexts:posFCMTradeTime.setStatus(_A)
class _PosFCMPacketInterval_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3500,10000))
_PosFCMPacketInterval_Type.__name__=_B
_PosFCMPacketInterval_Object=MibScalar
posFCMPacketInterval=_PosFCMPacketInterval_Object((1,3,6,1,4,1,2011,2,33,8,16),_PosFCMPacketInterval_Type())
posFCMPacketInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:posFCMPacketInterval.setStatus(_A)
_PosTrap_ObjectIdentity=ObjectIdentity
posTrap=_PosTrap_ObjectIdentity((1,3,6,1,4,1,2011,2,33,8,17))
class _PosPadWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_PosPadWaitTime_Type.__name__=_B
_PosPadWaitTime_Object=MibScalar
posPadWaitTime=_PosPadWaitTime_Object((1,3,6,1,4,1,2011,2,33,8,18),_PosPadWaitTime_Type())
posPadWaitTime.setMaxAccess(_G)
if mibBuilder.loadTexts:posPadWaitTime.setStatus(_A)
class _PosPadIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_PosPadIdleTimeout_Type.__name__=_B
_PosPadIdleTimeout_Object=MibScalar
posPadIdleTimeout=_PosPadIdleTimeout_Object((1,3,6,1,4,1,2011,2,33,8,19),_PosPadIdleTimeout_Type())
posPadIdleTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:posPadIdleTimeout.setStatus(_A)
class _PosPadPacType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('syn',1),('asy',2)))
_PosPadPacType_Type.__name__=_B
_PosPadPacType_Object=MibScalar
posPadPacType=_PosPadPacType_Object((1,3,6,1,4,1,2011,2,33,8,20),_PosPadPacType_Type())
posPadPacType.setMaxAccess(_G)
if mibBuilder.loadTexts:posPadPacType.setStatus(_A)
class _PosPadCheckSChar_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_PosPadCheckSChar_Type.__name__=_B
_PosPadCheckSChar_Object=MibScalar
posPadCheckSChar=_PosPadCheckSChar_Object((1,3,6,1,4,1,2011,2,33,8,21),_PosPadCheckSChar_Type())
posPadCheckSChar.setMaxAccess(_G)
if mibBuilder.loadTexts:posPadCheckSChar.setStatus(_A)
_PosPadTable_Object=MibTable
posPadTable=_PosPadTable_Object((1,3,6,1,4,1,2011,2,33,8,22))
if mibBuilder.loadTexts:posPadTable.setStatus(_A)
_PosPadEntry_Object=MibTableRow
posPadEntry=_PosPadEntry_Object((1,3,6,1,4,1,2011,2,33,8,22,1))
posPadEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:posPadEntry.setStatus(_A)
class _PosPadIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PosPadIfIndex_Type.__name__=_B
_PosPadIfIndex_Object=MibTableColumn
posPadIfIndex=_PosPadIfIndex_Object((1,3,6,1,4,1,2011,2,33,8,22,1,1),_PosPadIfIndex_Type())
posPadIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:posPadIfIndex.setStatus(_A)
_PosPadRowStatus_Type=RowStatus
_PosPadRowStatus_Object=MibTableColumn
posPadRowStatus=_PosPadRowStatus_Object((1,3,6,1,4,1,2011,2,33,8,22,1,2),_PosPadRowStatus_Type())
posPadRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:posPadRowStatus.setStatus(_A)
posAppNotReadyTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,1))
posAppNotReadyTrap.setObjects((_D,_H))
if mibBuilder.loadTexts:posAppNotReadyTrap.setStatus(_A)
posAppConnectFailTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,2))
posAppConnectFailTrap.setObjects((_D,_H))
if mibBuilder.loadTexts:posAppConnectFailTrap.setStatus(_A)
posAppStateChangeTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,3))
posAppStateChangeTrap.setObjects(*((_D,_H),(_D,_T)))
if mibBuilder.loadTexts:posAppStateChangeTrap.setStatus(_A)
posAppNotConfigedTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,4))
posAppNotConfigedTrap.setObjects((_D,_H))
if mibBuilder.loadTexts:posAppNotConfigedTrap.setStatus(_A)
posAppBuffOverFlowTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,5))
posAppBuffOverFlowTrap.setObjects((_D,_H))
if mibBuilder.loadTexts:posAppBuffOverFlowTrap.setStatus(_A)
posAppDebugOpenTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,6))
posAppDebugOpenTrap.setObjects((_D,_H))
if mibBuilder.loadTexts:posAppDebugOpenTrap.setStatus(_A)
posAppDebugAllOpenTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,7))
if mibBuilder.loadTexts:posAppDebugAllOpenTrap.setStatus(_A)
posInterBuffOverFlowTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,8))
if mibBuilder.loadTexts:posInterBuffOverFlowTrap.setStatus(_A)
posInterStateChangeTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,9))
posInterStateChangeTrap.setObjects(*((_D,_K),(_D,_U)))
if mibBuilder.loadTexts:posInterStateChangeTrap.setStatus(_A)
posInterDebugOpenTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,10))
posInterDebugOpenTrap.setObjects((_D,_K))
if mibBuilder.loadTexts:posInterDebugOpenTrap.setStatus(_A)
posInterDebugAllOpenTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,11))
if mibBuilder.loadTexts:posInterDebugAllOpenTrap.setStatus(_A)
posFCMTimeoutTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,12))
posFCMTimeoutTrap.setObjects((_D,_L))
if mibBuilder.loadTexts:posFCMTimeoutTrap.setStatus(_A)
posFCMConnectFailTrap=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,13))
posFCMConnectFailTrap.setObjects((_D,_L))
if mibBuilder.loadTexts:posFCMConnectFailTrap.setStatus(_A)
posClearPacketCounter=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,14))
if mibBuilder.loadTexts:posClearPacketCounter.setStatus(_A)
posClearFcmCounter=NotificationType((1,3,6,1,4,1,2011,2,33,8,17,15))
if mibBuilder.loadTexts:posClearFcmCounter.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'pos':pos,'posAppTable':posAppTable,'posAppEntry':posAppEntry,_H:posAppId,'posAppConnectMode':posAppConnectMode,_T:posAppState,'posAppIfIndex':posAppIfIndex,'posAppHostIP':posAppHostIP,'posAppPort':posAppPort,'posAppSourceIp':posAppSourceIp,'posAppRecvPacCounter':posAppRecvPacCounter,'posAppErrPacCounter':posAppErrPacCounter,'posAppDistrErrCounter':posAppDistrErrCounter,'posAppBuffedCounter':posAppBuffedCounter,'posAppDiscardedCounter':posAppDiscardedCounter,'posAppDebug':posAppDebug,'posAppRowStatus':posAppRowStatus,'posAppX121Addr':posAppX121Addr,'posInterTable':posInterTable,'posInterEntry':posInterEntry,_K:posPosId,'posPosIfIndex':posPosIfIndex,_U:posPosConnectState,'posPosRecvPacCounter':posPosRecvPacCounter,'posPosErrPacCounter':posPosErrPacCounter,'posPosMapErrCounter':posPosMapErrCounter,'posPosBuffedCounter':posPosBuffedCounter,'posPosDiscardedCounter':posPosDiscardedCounter,'posPosInterDebug':posPosInterDebug,'posPosInterRowStatus':posPosInterRowStatus,'posPosInterType':posPosInterType,'posMapTable':posMapTable,'posMapEntry':posMapEntry,_P:posMapDes,'posMapAppNumber':posMapAppNumber,'posMapRowStatus':posMapRowStatus,'posAsyAppTable':posAsyAppTable,'posAsyAppEntry':posAsyAppEntry,_Q:posAsyAppIfIndex,'posAsyAppRowStatus':posAsyAppRowStatus,'posFCMTable':posFCMTable,'posFCMEntry':posFCMEntry,_L:posFCMIfIndex,'posFCMTimeoutCounter':posFCMTimeoutCounter,'posFCMConnectFailCounter':posFCMConnectFailCounter,'posAppSum':posAppSum,'posInterSum':posInterSum,'posEnable':posEnable,'posAppDebugAll':posAppDebugAll,'posPosDebugAll':posPosDebugAll,'posClearPacCounter':posClearPacCounter,'posClearFCMCounter':posClearFCMCounter,'posEnableTrap':posEnableTrap,'posFCMAnswerTime':posFCMAnswerTime,'posFCMTradeTime':posFCMTradeTime,'posFCMPacketInterval':posFCMPacketInterval,'posTrap':posTrap,'posAppNotReadyTrap':posAppNotReadyTrap,'posAppConnectFailTrap':posAppConnectFailTrap,'posAppStateChangeTrap':posAppStateChangeTrap,'posAppNotConfigedTrap':posAppNotConfigedTrap,'posAppBuffOverFlowTrap':posAppBuffOverFlowTrap,'posAppDebugOpenTrap':posAppDebugOpenTrap,'posAppDebugAllOpenTrap':posAppDebugAllOpenTrap,'posInterBuffOverFlowTrap':posInterBuffOverFlowTrap,'posInterStateChangeTrap':posInterStateChangeTrap,'posInterDebugOpenTrap':posInterDebugOpenTrap,'posInterDebugAllOpenTrap':posInterDebugAllOpenTrap,'posFCMTimeoutTrap':posFCMTimeoutTrap,'posFCMConnectFailTrap':posFCMConnectFailTrap,'posClearPacketCounter':posClearPacketCounter,'posClearFcmCounter':posClearFcmCounter,'posPadWaitTime':posPadWaitTime,'posPadIdleTimeout':posPadIdleTimeout,'posPadPacType':posPadPacType,'posPadCheckSChar':posPadCheckSChar,'posPadTable':posPadTable,'posPadEntry':posPadEntry,_S:posPadIfIndex,'posPadRowStatus':posPadRowStatus})