_R='fsIcchPeerNodeState'
_Q='fsIcchPeerNodeIpAddress'
_P='fsIcclSessionVlan'
_O='fsIcclSessionSubnetMask'
_N='fsIcclSessionIpAddress'
_M='fsIcclSessionInterface'
_L='fsIcclSessionNodeState'
_K='DisplayString'
_J='Integer32'
_I='VlanId'
_H='fsIcclSessionInstanceId'
_G='TruthValue'
_F='IpAddress'
_E='Unsigned32'
_D='read-only'
_C='ARICENT-ICCH-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_I)
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,_F,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention',_G)
fsIcchMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,94))
if mibBuilder.loadTexts:fsIcchMIB.setRevisions(('2014-12-11 00:00',))
class FsIcchState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('init',0),('master',1),('slave',2)))
_FsIcch_ObjectIdentity=ObjectIdentity
fsIcch=_FsIcch_ObjectIdentity((1,3,6,1,4,1,29601,2,94,1))
class _FsIcchTrcLevel_Type(Unsigned32):defaultValue=0
_FsIcchTrcLevel_Type.__name__=_E
_FsIcchTrcLevel_Object=MibScalar
fsIcchTrcLevel=_FsIcchTrcLevel_Object((1,3,6,1,4,1,29601,2,94,1,1),_FsIcchTrcLevel_Type())
fsIcchTrcLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcchTrcLevel.setStatus(_A)
class _FsIcchStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsIcchStatsEnable_Type.__name__=_J
_FsIcchStatsEnable_Object=MibScalar
fsIcchStatsEnable=_FsIcchStatsEnable_Object((1,3,6,1,4,1,29601,2,94,1,2),_FsIcchStatsEnable_Type())
fsIcchStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcchStatsEnable.setStatus(_A)
class _FsIcchClearStats_Type(TruthValue):defaultValue=2
_FsIcchClearStats_Type.__name__=_G
_FsIcchClearStats_Object=MibScalar
fsIcchClearStats=_FsIcchClearStats_Object((1,3,6,1,4,1,29601,2,94,1,3),_FsIcchClearStats_Type())
fsIcchClearStats.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcchClearStats.setStatus(_A)
class _FsIcchEnableProtoSync_Type(Unsigned32):defaultValue=0
_FsIcchEnableProtoSync_Type.__name__=_E
_FsIcchEnableProtoSync_Object=MibScalar
fsIcchEnableProtoSync=_FsIcchEnableProtoSync_Object((1,3,6,1,4,1,29601,2,94,1,4),_FsIcchEnableProtoSync_Type())
fsIcchEnableProtoSync.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcchEnableProtoSync.setStatus(_A)
class _FsIcchFetchRemoteFdb_Type(TruthValue):defaultValue=2
_FsIcchFetchRemoteFdb_Type.__name__=_G
_FsIcchFetchRemoteFdb_Object=MibScalar
fsIcchFetchRemoteFdb=_FsIcchFetchRemoteFdb_Object((1,3,6,1,4,1,29601,2,94,1,5),_FsIcchFetchRemoteFdb_Type())
fsIcchFetchRemoteFdb.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcchFetchRemoteFdb.setStatus(_A)
_FsIcchPeerNodeIpAddress_Type=IpAddress
_FsIcchPeerNodeIpAddress_Object=MibScalar
fsIcchPeerNodeIpAddress=_FsIcchPeerNodeIpAddress_Object((1,3,6,1,4,1,29601,2,94,1,6),_FsIcchPeerNodeIpAddress_Type())
fsIcchPeerNodeIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcchPeerNodeIpAddress.setStatus(_A)
_FsIcchPeerNodeState_Type=FsIcchState
_FsIcchPeerNodeState_Object=MibScalar
fsIcchPeerNodeState=_FsIcchPeerNodeState_Object((1,3,6,1,4,1,29601,2,94,1,7),_FsIcchPeerNodeState_Type())
fsIcchPeerNodeState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcchPeerNodeState.setStatus(_A)
_FsIcchStatistics_ObjectIdentity=ObjectIdentity
fsIcchStatistics=_FsIcchStatistics_ObjectIdentity((1,3,6,1,4,1,29601,2,94,2))
_FsIcchStatsSyncMsgTxCount_Type=ZeroBasedCounter32
_FsIcchStatsSyncMsgTxCount_Object=MibScalar
fsIcchStatsSyncMsgTxCount=_FsIcchStatsSyncMsgTxCount_Object((1,3,6,1,4,1,29601,2,94,2,1),_FsIcchStatsSyncMsgTxCount_Type())
fsIcchStatsSyncMsgTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcchStatsSyncMsgTxCount.setStatus(_A)
_FsIcchStatsSyncMsgTxFailedCount_Type=ZeroBasedCounter32
_FsIcchStatsSyncMsgTxFailedCount_Object=MibScalar
fsIcchStatsSyncMsgTxFailedCount=_FsIcchStatsSyncMsgTxFailedCount_Object((1,3,6,1,4,1,29601,2,94,2,2),_FsIcchStatsSyncMsgTxFailedCount_Type())
fsIcchStatsSyncMsgTxFailedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcchStatsSyncMsgTxFailedCount.setStatus(_A)
_FsIcchStatsSyncMsgRxCount_Type=ZeroBasedCounter32
_FsIcchStatsSyncMsgRxCount_Object=MibScalar
fsIcchStatsSyncMsgRxCount=_FsIcchStatsSyncMsgRxCount_Object((1,3,6,1,4,1,29601,2,94,2,3),_FsIcchStatsSyncMsgRxCount_Type())
fsIcchStatsSyncMsgRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcchStatsSyncMsgRxCount.setStatus(_A)
_FsIcchStatsSyncMsgProcCount_Type=ZeroBasedCounter32
_FsIcchStatsSyncMsgProcCount_Object=MibScalar
fsIcchStatsSyncMsgProcCount=_FsIcchStatsSyncMsgProcCount_Object((1,3,6,1,4,1,29601,2,94,2,4),_FsIcchStatsSyncMsgProcCount_Type())
fsIcchStatsSyncMsgProcCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcchStatsSyncMsgProcCount.setStatus(_A)
_FsIcchStatsSyncMsgMissedCount_Type=ZeroBasedCounter32
_FsIcchStatsSyncMsgMissedCount_Object=MibScalar
fsIcchStatsSyncMsgMissedCount=_FsIcchStatsSyncMsgMissedCount_Object((1,3,6,1,4,1,29601,2,94,2,5),_FsIcchStatsSyncMsgMissedCount_Type())
fsIcchStatsSyncMsgMissedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcchStatsSyncMsgMissedCount.setStatus(_A)
_FsIcchNotification_ObjectIdentity=ObjectIdentity
fsIcchNotification=_FsIcchNotification_ObjectIdentity((1,3,6,1,4,1,29601,2,94,3))
_FsIcchTrap_ObjectIdentity=ObjectIdentity
fsIcchTrap=_FsIcchTrap_ObjectIdentity((1,3,6,1,4,1,29601,2,94,3,0))
_FsIcclSession_ObjectIdentity=ObjectIdentity
fsIcclSession=_FsIcclSession_ObjectIdentity((1,3,6,1,4,1,29601,2,94,4))
_FsIcclSessionTable_Object=MibTable
fsIcclSessionTable=_FsIcclSessionTable_Object((1,3,6,1,4,1,29601,2,94,4,1))
if mibBuilder.loadTexts:fsIcclSessionTable.setStatus(_A)
_FsIcclSessionEntry_Object=MibTableRow
fsIcclSessionEntry=_FsIcclSessionEntry_Object((1,3,6,1,4,1,29601,2,94,4,1,1))
fsIcclSessionEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:fsIcclSessionEntry.setStatus(_A)
class _FsIcclSessionInstanceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsIcclSessionInstanceId_Type.__name__=_E
_FsIcclSessionInstanceId_Object=MibTableColumn
fsIcclSessionInstanceId=_FsIcclSessionInstanceId_Object((1,3,6,1,4,1,29601,2,94,4,1,1,1),_FsIcclSessionInstanceId_Type())
fsIcclSessionInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsIcclSessionInstanceId.setStatus(_A)
class _FsIcclSessionInterface_Type(DisplayString):defaultValue=OctetString('po4094')
_FsIcclSessionInterface_Type.__name__=_K
_FsIcclSessionInterface_Object=MibTableColumn
fsIcclSessionInterface=_FsIcclSessionInterface_Object((1,3,6,1,4,1,29601,2,94,4,1,1,2),_FsIcclSessionInterface_Type())
fsIcclSessionInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcclSessionInterface.setStatus(_A)
class _FsIcclSessionIpAddress_Type(IpAddress):defaultHexValue='A9FE0101'
_FsIcclSessionIpAddress_Type.__name__=_F
_FsIcclSessionIpAddress_Object=MibTableColumn
fsIcclSessionIpAddress=_FsIcclSessionIpAddress_Object((1,3,6,1,4,1,29601,2,94,4,1,1,3),_FsIcclSessionIpAddress_Type())
fsIcclSessionIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcclSessionIpAddress.setStatus(_A)
class _FsIcclSessionSubnetMask_Type(IpAddress):defaultHexValue='FF000000'
_FsIcclSessionSubnetMask_Type.__name__=_F
_FsIcclSessionSubnetMask_Object=MibTableColumn
fsIcclSessionSubnetMask=_FsIcclSessionSubnetMask_Object((1,3,6,1,4,1,29601,2,94,4,1,1,4),_FsIcclSessionSubnetMask_Type())
fsIcclSessionSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcclSessionSubnetMask.setStatus(_A)
class _FsIcclSessionVlan_Type(VlanId):defaultValue=4094
_FsIcclSessionVlan_Type.__name__=_I
_FsIcclSessionVlan_Object=MibTableColumn
fsIcclSessionVlan=_FsIcclSessionVlan_Object((1,3,6,1,4,1,29601,2,94,4,1,1,5),_FsIcclSessionVlan_Type())
fsIcclSessionVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcclSessionVlan.setStatus(_A)
_FsIcclSessionNodeState_Type=FsIcchState
_FsIcclSessionNodeState_Object=MibTableColumn
fsIcclSessionNodeState=_FsIcclSessionNodeState_Object((1,3,6,1,4,1,29601,2,94,4,1,1,6),_FsIcclSessionNodeState_Type())
fsIcclSessionNodeState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIcclSessionNodeState.setStatus(_A)
_FsIcclSessionRowStatus_Type=RowStatus
_FsIcclSessionRowStatus_Object=MibTableColumn
fsIcclSessionRowStatus=_FsIcclSessionRowStatus_Object((1,3,6,1,4,1,29601,2,94,4,1,1,7),_FsIcclSessionRowStatus_Type())
fsIcclSessionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIcclSessionRowStatus.setStatus(_A)
fsIcchTrapNodeStatusChange=NotificationType((1,3,6,1,4,1,29601,2,94,3,0,1))
fsIcchTrapNodeStatusChange.setObjects(*((_C,_L),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P)))
if mibBuilder.loadTexts:fsIcchTrapNodeStatusChange.setStatus(_A)
fsIcchTrapPeerNodeStatusChange=NotificationType((1,3,6,1,4,1,29601,2,94,3,0,2))
fsIcchTrapPeerNodeStatusChange.setObjects(*((_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:fsIcchTrapPeerNodeStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FsIcchState':FsIcchState,'fsIcchMIB':fsIcchMIB,'fsIcch':fsIcch,'fsIcchTrcLevel':fsIcchTrcLevel,'fsIcchStatsEnable':fsIcchStatsEnable,'fsIcchClearStats':fsIcchClearStats,'fsIcchEnableProtoSync':fsIcchEnableProtoSync,'fsIcchFetchRemoteFdb':fsIcchFetchRemoteFdb,_Q:fsIcchPeerNodeIpAddress,_R:fsIcchPeerNodeState,'fsIcchStatistics':fsIcchStatistics,'fsIcchStatsSyncMsgTxCount':fsIcchStatsSyncMsgTxCount,'fsIcchStatsSyncMsgTxFailedCount':fsIcchStatsSyncMsgTxFailedCount,'fsIcchStatsSyncMsgRxCount':fsIcchStatsSyncMsgRxCount,'fsIcchStatsSyncMsgProcCount':fsIcchStatsSyncMsgProcCount,'fsIcchStatsSyncMsgMissedCount':fsIcchStatsSyncMsgMissedCount,'fsIcchNotification':fsIcchNotification,'fsIcchTrap':fsIcchTrap,'fsIcchTrapNodeStatusChange':fsIcchTrapNodeStatusChange,'fsIcchTrapPeerNodeStatusChange':fsIcchTrapPeerNodeStatusChange,'fsIcclSession':fsIcclSession,'fsIcclSessionTable':fsIcclSessionTable,'fsIcclSessionEntry':fsIcclSessionEntry,_H:fsIcclSessionInstanceId,_M:fsIcclSessionInterface,_N:fsIcclSessionIpAddress,_O:fsIcclSessionSubnetMask,_P:fsIcclSessionVlan,_L:fsIcclSessionNodeState,'fsIcclSessionRowStatus':fsIcclSessionRowStatus})