_j='fsRstOldRoleType'
_i='fsRstPortRoleType'
_h='fsRstPktErrVal'
_g='fsRstPktErrType'
_f='fsRstPortMigrationType'
_e='fsRstOldDesignatedRoot'
_d='fsRstErrTrapType'
_c='fsRstGenTrapType'
_b='fsRstPortTrapIndex'
_a='disable'
_Z='enable'
_Y='timerExpiryEvent'
_X='bpduEvent'
_W='configurationEvent'
_V='learning'
_U='not-accessible'
_T='fsRstPort'
_S='disabled'
_R='dot1dStpVersion'
_Q='RSTP-MIB'
_P='dot1dStpPortState'
_O='dot1dStpDesignatedRoot'
_N='none'
_M='designatedPort'
_L='rootPort'
_K='backupPort'
_J='alternatePort'
_I='disabledPort'
_H='TruthValue'
_G='dot1dBaseBridgeAddress'
_F='SUPERMICRO-RSTP-MIB'
_E='BRIDGE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,dot1dBaseBridgeAddress,dot1dStpDesignatedRoot,dot1dStpPortState=mibBuilder.importSymbols(_E,'BridgeId',_G,_O,_P)
dot1dStpVersion,=mibBuilder.importSymbols(_Q,_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
futureRstMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,79))
if mibBuilder.loadTexts:futureRstMIB.setRevisions(('2012-09-05 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_S,2)))
_Dot1wFutureRst_ObjectIdentity=ObjectIdentity
dot1wFutureRst=_Dot1wFutureRst_ObjectIdentity((1,3,6,1,4,1,10876,101,1,79,1))
class _FsRstSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsRstSystemControl_Type.__name__=_C
_FsRstSystemControl_Object=MibScalar
fsRstSystemControl=_FsRstSystemControl_Object((1,3,6,1,4,1,10876,101,1,79,1,1),_FsRstSystemControl_Type())
fsRstSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstSystemControl.setStatus(_A)
_FsRstModuleStatus_Type=EnabledStatus
_FsRstModuleStatus_Object=MibScalar
fsRstModuleStatus=_FsRstModuleStatus_Object((1,3,6,1,4,1,10876,101,1,79,1,2),_FsRstModuleStatus_Type())
fsRstModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstModuleStatus.setStatus(_A)
class _FsRstTraceOption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsRstTraceOption_Type.__name__=_C
_FsRstTraceOption_Object=MibScalar
fsRstTraceOption=_FsRstTraceOption_Object((1,3,6,1,4,1,10876,101,1,79,1,3),_FsRstTraceOption_Type())
fsRstTraceOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstTraceOption.setStatus(_A)
class _FsRstDebugOption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_FsRstDebugOption_Type.__name__=_C
_FsRstDebugOption_Object=MibScalar
fsRstDebugOption=_FsRstDebugOption_Object((1,3,6,1,4,1,10876,101,1,79,1,4),_FsRstDebugOption_Type())
fsRstDebugOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstDebugOption.setStatus(_A)
_FsRstRstpUpCount_Type=Counter32
_FsRstRstpUpCount_Object=MibScalar
fsRstRstpUpCount=_FsRstRstpUpCount_Object((1,3,6,1,4,1,10876,101,1,79,1,5),_FsRstRstpUpCount_Type())
fsRstRstpUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstRstpUpCount.setStatus(_A)
_FsRstRstpDownCount_Type=Counter32
_FsRstRstpDownCount_Object=MibScalar
fsRstRstpDownCount=_FsRstRstpDownCount_Object((1,3,6,1,4,1,10876,101,1,79,1,6),_FsRstRstpDownCount_Type())
fsRstRstpDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstRstpDownCount.setStatus(_A)
_FsRstBufferFailureCount_Type=Counter32
_FsRstBufferFailureCount_Object=MibScalar
fsRstBufferFailureCount=_FsRstBufferFailureCount_Object((1,3,6,1,4,1,10876,101,1,79,1,7),_FsRstBufferFailureCount_Type())
fsRstBufferFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstBufferFailureCount.setStatus(_A)
_FsRstMemAllocFailureCount_Type=Counter32
_FsRstMemAllocFailureCount_Object=MibScalar
fsRstMemAllocFailureCount=_FsRstMemAllocFailureCount_Object((1,3,6,1,4,1,10876,101,1,79,1,8),_FsRstMemAllocFailureCount_Type())
fsRstMemAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstMemAllocFailureCount.setStatus(_A)
_FsRstNewRootIdCount_Type=Counter32
_FsRstNewRootIdCount_Object=MibScalar
fsRstNewRootIdCount=_FsRstNewRootIdCount_Object((1,3,6,1,4,1,10876,101,1,79,1,9),_FsRstNewRootIdCount_Type())
fsRstNewRootIdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstNewRootIdCount.setStatus(_A)
class _FsRstPortRoleSelSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('initbridge',0),('roleselection',1)))
_FsRstPortRoleSelSmState_Type.__name__=_C
_FsRstPortRoleSelSmState_Object=MibScalar
fsRstPortRoleSelSmState=_FsRstPortRoleSelSmState_Object((1,3,6,1,4,1,10876,101,1,79,1,10),_FsRstPortRoleSelSmState_Type())
fsRstPortRoleSelSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRoleSelSmState.setStatus(_A)
_FsRstOldDesignatedRoot_Type=BridgeId
_FsRstOldDesignatedRoot_Object=MibScalar
fsRstOldDesignatedRoot=_FsRstOldDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,79,1,11),_FsRstOldDesignatedRoot_Type())
fsRstOldDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstOldDesignatedRoot.setStatus(_A)
_FsRstPortExtTable_Object=MibTable
fsRstPortExtTable=_FsRstPortExtTable_Object((1,3,6,1,4,1,10876,101,1,79,1,12))
if mibBuilder.loadTexts:fsRstPortExtTable.setStatus(_A)
_FsRstPortExtEntry_Object=MibTableRow
fsRstPortExtEntry=_FsRstPortExtEntry_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1))
fsRstPortExtEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:fsRstPortExtEntry.setStatus(_A)
class _FsRstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsRstPort_Type.__name__=_C
_FsRstPort_Object=MibTableColumn
fsRstPort=_FsRstPort_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,1),_FsRstPort_Type())
fsRstPort.setMaxAccess(_U)
if mibBuilder.loadTexts:fsRstPort.setStatus(_A)
class _FsRstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4)))
_FsRstPortRole_Type.__name__=_C
_FsRstPortRole_Object=MibTableColumn
fsRstPortRole=_FsRstPortRole_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,2),_FsRstPortRole_Type())
fsRstPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRole.setStatus(_A)
class _FsRstPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2)))
_FsRstPortOperVersion_Type.__name__=_C
_FsRstPortOperVersion_Object=MibTableColumn
fsRstPortOperVersion=_FsRstPortOperVersion_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,3),_FsRstPortOperVersion_Type())
fsRstPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortOperVersion.setStatus(_A)
class _FsRstPortInfoSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,0),('aged',1),('update',2),('superior',3),('repeat',4),('notdesignated',5),('present',6),('receive',7),('inferiordesignated',8)))
_FsRstPortInfoSmState_Type.__name__=_C
_FsRstPortInfoSmState_Object=MibTableColumn
fsRstPortInfoSmState=_FsRstPortInfoSmState_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,4),_FsRstPortInfoSmState_Type())
fsRstPortInfoSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortInfoSmState.setStatus(_A)
class _FsRstPortMigSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('checkingrstp',0),('selectingstp',1),('sensing',2)))
_FsRstPortMigSmState_Type.__name__=_C
_FsRstPortMigSmState_Object=MibTableColumn
fsRstPortMigSmState=_FsRstPortMigSmState_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,5),_FsRstPortMigSmState_Type())
fsRstPortMigSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortMigSmState.setStatus(_A)
class _FsRstPortRoleTransSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('init',0),('disableport',1),('disabledport',2),('rootport',3),('designatedport',4),('backupport',5),('rootproposed',6),('rootagreed',7),('reroot',8),('rootforward',9),('rootlearn',10),('rerooted',11),('designatedpropose',12),('designatedsynced',13),('designatedretired',14),('designatedforward',15),('designatedlearn',16),('designatedlisten',17)))
_FsRstPortRoleTransSmState_Type.__name__=_C
_FsRstPortRoleTransSmState_Object=MibTableColumn
fsRstPortRoleTransSmState=_FsRstPortRoleTransSmState_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,6),_FsRstPortRoleTransSmState_Type())
fsRstPortRoleTransSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRoleTransSmState.setStatus(_A)
class _FsRstPortStateTransSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('discarding',0),(_V,1),('forwarding',2)))
_FsRstPortStateTransSmState_Type.__name__=_C
_FsRstPortStateTransSmState_Object=MibTableColumn
fsRstPortStateTransSmState=_FsRstPortStateTransSmState_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,7),_FsRstPortStateTransSmState_Type())
fsRstPortStateTransSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortStateTransSmState.setStatus(_A)
class _FsRstPortTopoChSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('inactive',0),(_V,1),('detected',2),('active',3),('notifiedtcn',4),('notifiedtc',5),('propagating',6),('acknowledged',7)))
_FsRstPortTopoChSmState_Type.__name__=_C
_FsRstPortTopoChSmState_Object=MibTableColumn
fsRstPortTopoChSmState=_FsRstPortTopoChSmState_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,8),_FsRstPortTopoChSmState_Type())
fsRstPortTopoChSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortTopoChSmState.setStatus(_A)
class _FsRstPortTxSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_FsRstPortTxSmState_Type.__name__=_C
_FsRstPortTxSmState_Object=MibTableColumn
fsRstPortTxSmState=_FsRstPortTxSmState_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,9),_FsRstPortTxSmState_Type())
fsRstPortTxSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortTxSmState.setStatus(_A)
_FsRstPortRxRstBpduCount_Type=Counter32
_FsRstPortRxRstBpduCount_Object=MibTableColumn
fsRstPortRxRstBpduCount=_FsRstPortRxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,10),_FsRstPortRxRstBpduCount_Type())
fsRstPortRxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRxRstBpduCount.setStatus(_A)
_FsRstPortRxConfigBpduCount_Type=Counter32
_FsRstPortRxConfigBpduCount_Object=MibTableColumn
fsRstPortRxConfigBpduCount=_FsRstPortRxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,11),_FsRstPortRxConfigBpduCount_Type())
fsRstPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRxConfigBpduCount.setStatus(_A)
_FsRstPortRxTcnBpduCount_Type=Counter32
_FsRstPortRxTcnBpduCount_Object=MibTableColumn
fsRstPortRxTcnBpduCount=_FsRstPortRxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,12),_FsRstPortRxTcnBpduCount_Type())
fsRstPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRxTcnBpduCount.setStatus(_A)
_FsRstPortTxRstBpduCount_Type=Counter32
_FsRstPortTxRstBpduCount_Object=MibTableColumn
fsRstPortTxRstBpduCount=_FsRstPortTxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,13),_FsRstPortTxRstBpduCount_Type())
fsRstPortTxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortTxRstBpduCount.setStatus(_A)
_FsRstPortTxConfigBpduCount_Type=Counter32
_FsRstPortTxConfigBpduCount_Object=MibTableColumn
fsRstPortTxConfigBpduCount=_FsRstPortTxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,14),_FsRstPortTxConfigBpduCount_Type())
fsRstPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortTxConfigBpduCount.setStatus(_A)
_FsRstPortTxTcnBpduCount_Type=Counter32
_FsRstPortTxTcnBpduCount_Object=MibTableColumn
fsRstPortTxTcnBpduCount=_FsRstPortTxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,15),_FsRstPortTxTcnBpduCount_Type())
fsRstPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortTxTcnBpduCount.setStatus(_A)
_FsRstPortInvalidRstBpduRxCount_Type=Counter32
_FsRstPortInvalidRstBpduRxCount_Object=MibTableColumn
fsRstPortInvalidRstBpduRxCount=_FsRstPortInvalidRstBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,16),_FsRstPortInvalidRstBpduRxCount_Type())
fsRstPortInvalidRstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortInvalidRstBpduRxCount.setStatus(_A)
_FsRstPortInvalidConfigBpduRxCount_Type=Counter32
_FsRstPortInvalidConfigBpduRxCount_Object=MibTableColumn
fsRstPortInvalidConfigBpduRxCount=_FsRstPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,17),_FsRstPortInvalidConfigBpduRxCount_Type())
fsRstPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortInvalidConfigBpduRxCount.setStatus(_A)
_FsRstPortInvalidTcnBpduRxCount_Type=Counter32
_FsRstPortInvalidTcnBpduRxCount_Object=MibTableColumn
fsRstPortInvalidTcnBpduRxCount=_FsRstPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,18),_FsRstPortInvalidTcnBpduRxCount_Type())
fsRstPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortInvalidTcnBpduRxCount.setStatus(_A)
_FsRstPortProtocolMigrationCount_Type=Counter32
_FsRstPortProtocolMigrationCount_Object=MibTableColumn
fsRstPortProtocolMigrationCount=_FsRstPortProtocolMigrationCount_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,19),_FsRstPortProtocolMigrationCount_Type())
fsRstPortProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortProtocolMigrationCount.setStatus(_A)
_FsRstPortEffectivePortState_Type=TruthValue
_FsRstPortEffectivePortState_Object=MibTableColumn
fsRstPortEffectivePortState=_FsRstPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,20),_FsRstPortEffectivePortState_Type())
fsRstPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortEffectivePortState.setStatus(_A)
_FsRstPortAutoEdge_Type=TruthValue
_FsRstPortAutoEdge_Object=MibTableColumn
fsRstPortAutoEdge=_FsRstPortAutoEdge_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,21),_FsRstPortAutoEdge_Type())
fsRstPortAutoEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortAutoEdge.setStatus(_A)
_FsRstPortRestrictedRole_Type=TruthValue
_FsRstPortRestrictedRole_Object=MibTableColumn
fsRstPortRestrictedRole=_FsRstPortRestrictedRole_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,22),_FsRstPortRestrictedRole_Type())
fsRstPortRestrictedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortRestrictedRole.setStatus(_A)
_FsRstPortRestrictedTCN_Type=TruthValue
_FsRstPortRestrictedTCN_Object=MibTableColumn
fsRstPortRestrictedTCN=_FsRstPortRestrictedTCN_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,23),_FsRstPortRestrictedTCN_Type())
fsRstPortRestrictedTCN.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortRestrictedTCN.setStatus(_A)
class _FsRstPortEnableBPDURx_Type(TruthValue):defaultValue=1
_FsRstPortEnableBPDURx_Type.__name__=_H
_FsRstPortEnableBPDURx_Object=MibTableColumn
fsRstPortEnableBPDURx=_FsRstPortEnableBPDURx_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,24),_FsRstPortEnableBPDURx_Type())
fsRstPortEnableBPDURx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortEnableBPDURx.setStatus(_A)
class _FsRstPortEnableBPDUTx_Type(TruthValue):defaultValue=1
_FsRstPortEnableBPDUTx_Type.__name__=_H
_FsRstPortEnableBPDUTx_Object=MibTableColumn
fsRstPortEnableBPDUTx=_FsRstPortEnableBPDUTx_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,25),_FsRstPortEnableBPDUTx_Type())
fsRstPortEnableBPDUTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortEnableBPDUTx.setStatus(_A)
_FsRstPortPseudoRootId_Type=BridgeId
_FsRstPortPseudoRootId_Object=MibTableColumn
fsRstPortPseudoRootId=_FsRstPortPseudoRootId_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,26),_FsRstPortPseudoRootId_Type())
fsRstPortPseudoRootId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortPseudoRootId.setStatus(_A)
class _FsRstPortIsL2Gp_Type(TruthValue):defaultValue=2
_FsRstPortIsL2Gp_Type.__name__=_H
_FsRstPortIsL2Gp_Object=MibTableColumn
fsRstPortIsL2Gp=_FsRstPortIsL2Gp_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,27),_FsRstPortIsL2Gp_Type())
fsRstPortIsL2Gp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortIsL2Gp.setStatus(_A)
class _FsRstPortLoopGuard_Type(TruthValue):defaultValue=2
_FsRstPortLoopGuard_Type.__name__=_H
_FsRstPortLoopGuard_Object=MibTableColumn
fsRstPortLoopGuard=_FsRstPortLoopGuard_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,28),_FsRstPortLoopGuard_Type())
fsRstPortLoopGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortLoopGuard.setStatus(_A)
class _FsRstPortRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_FsRstPortRcvdEvent_Type.__name__=_C
_FsRstPortRcvdEvent_Object=MibTableColumn
fsRstPortRcvdEvent=_FsRstPortRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,29),_FsRstPortRcvdEvent_Type())
fsRstPortRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRcvdEvent.setStatus(_A)
_FsRstPortRcvdEventSubType_Type=Integer32
_FsRstPortRcvdEventSubType_Object=MibTableColumn
fsRstPortRcvdEventSubType=_FsRstPortRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,30),_FsRstPortRcvdEventSubType_Type())
fsRstPortRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRcvdEventSubType.setStatus(_A)
_FsRstPortRcvdEventTimeStamp_Type=Unsigned32
_FsRstPortRcvdEventTimeStamp_Object=MibTableColumn
fsRstPortRcvdEventTimeStamp=_FsRstPortRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,31),_FsRstPortRcvdEventTimeStamp_Type())
fsRstPortRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRcvdEventTimeStamp.setStatus(_A)
_FsRstPortStateChangeTimeStamp_Type=Unsigned32
_FsRstPortStateChangeTimeStamp_Object=MibTableColumn
fsRstPortStateChangeTimeStamp=_FsRstPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,32),_FsRstPortStateChangeTimeStamp_Type())
fsRstPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortStateChangeTimeStamp.setStatus(_A)
_FsRstPortRowStatus_Type=RowStatus
_FsRstPortRowStatus_Object=MibTableColumn
fsRstPortRowStatus=_FsRstPortRowStatus_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,33),_FsRstPortRowStatus_Type())
fsRstPortRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsRstPortRowStatus.setStatus(_A)
class _FsRstPortBpduGuard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_Z,1),(_a,2)))
_FsRstPortBpduGuard_Type.__name__=_C
_FsRstPortBpduGuard_Object=MibTableColumn
fsRstPortBpduGuard=_FsRstPortBpduGuard_Object((1,3,6,1,4,1,10876,101,1,79,1,12,1,34),_FsRstPortBpduGuard_Type())
fsRstPortBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstPortBpduGuard.setStatus(_A)
class _FsRstDynamicPathcostCalculation_Type(TruthValue):defaultValue=2
_FsRstDynamicPathcostCalculation_Type.__name__=_H
_FsRstDynamicPathcostCalculation_Object=MibScalar
fsRstDynamicPathcostCalculation=_FsRstDynamicPathcostCalculation_Object((1,3,6,1,4,1,10876,101,1,79,1,13),_FsRstDynamicPathcostCalculation_Type())
fsRstDynamicPathcostCalculation.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstDynamicPathcostCalculation.setStatus(_A)
class _FsRstCalcPortPathCostOnSpeedChg_Type(TruthValue):defaultValue=2
_FsRstCalcPortPathCostOnSpeedChg_Type.__name__=_H
_FsRstCalcPortPathCostOnSpeedChg_Object=MibScalar
fsRstCalcPortPathCostOnSpeedChg=_FsRstCalcPortPathCostOnSpeedChg_Object((1,3,6,1,4,1,10876,101,1,79,1,14),_FsRstCalcPortPathCostOnSpeedChg_Type())
fsRstCalcPortPathCostOnSpeedChg.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstCalcPortPathCostOnSpeedChg.setStatus(_A)
class _FsRstRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_FsRstRcvdEvent_Type.__name__=_C
_FsRstRcvdEvent_Object=MibScalar
fsRstRcvdEvent=_FsRstRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,79,1,15),_FsRstRcvdEvent_Type())
fsRstRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstRcvdEvent.setStatus(_A)
_FsRstRcvdEventSubType_Type=Integer32
_FsRstRcvdEventSubType_Object=MibScalar
fsRstRcvdEventSubType=_FsRstRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,79,1,16),_FsRstRcvdEventSubType_Type())
fsRstRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstRcvdEventSubType.setStatus(_A)
_FsRstRcvdEventTimeStamp_Type=Unsigned32
_FsRstRcvdEventTimeStamp_Object=MibScalar
fsRstRcvdEventTimeStamp=_FsRstRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,79,1,17),_FsRstRcvdEventTimeStamp_Type())
fsRstRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstRcvdEventTimeStamp.setStatus(_A)
_FsRstRcvdPortStateChangeTimeStamp_Type=Unsigned32
_FsRstRcvdPortStateChangeTimeStamp_Object=MibScalar
fsRstRcvdPortStateChangeTimeStamp=_FsRstRcvdPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,79,1,18),_FsRstRcvdPortStateChangeTimeStamp_Type())
fsRstRcvdPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstRcvdPortStateChangeTimeStamp.setStatus(_A)
class _FsRstBpduGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_FsRstBpduGuard_Type.__name__=_C
_FsRstBpduGuard_Object=MibScalar
fsRstBpduGuard=_FsRstBpduGuard_Object((1,3,6,1,4,1,10876,101,1,79,1,19),_FsRstBpduGuard_Type())
fsRstBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstBpduGuard.setStatus(_A)
_Dot1wFsRstTrapsControl_ObjectIdentity=ObjectIdentity
dot1wFsRstTrapsControl=_Dot1wFsRstTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,79,2))
class _FsRstSetTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsRstSetTraps_Type.__name__=_C
_FsRstSetTraps_Object=MibScalar
fsRstSetTraps=_FsRstSetTraps_Object((1,3,6,1,4,1,10876,101,1,79,2,1),_FsRstSetTraps_Type())
fsRstSetTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRstSetTraps.setStatus(_A)
class _FsRstGenTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('up',1),('down',2)))
_FsRstGenTrapType_Type.__name__=_C
_FsRstGenTrapType_Object=MibScalar
fsRstGenTrapType=_FsRstGenTrapType_Object((1,3,6,1,4,1,10876,101,1,79,2,2),_FsRstGenTrapType_Type())
fsRstGenTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstGenTrapType.setStatus(_A)
class _FsRstErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('memfail',1),('bufffail',2)))
_FsRstErrTrapType_Type.__name__=_C
_FsRstErrTrapType_Object=MibScalar
fsRstErrTrapType=_FsRstErrTrapType_Object((1,3,6,1,4,1,10876,101,1,79,2,3),_FsRstErrTrapType_Type())
fsRstErrTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstErrTrapType.setStatus(_A)
_FsRstPortTrapNotificationTable_Object=MibTable
fsRstPortTrapNotificationTable=_FsRstPortTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,79,2,4))
if mibBuilder.loadTexts:fsRstPortTrapNotificationTable.setStatus(_A)
_FsRstPortTrapNotificationEntry_Object=MibTableRow
fsRstPortTrapNotificationEntry=_FsRstPortTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,79,2,4,1))
fsRstPortTrapNotificationEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:fsRstPortTrapNotificationEntry.setStatus(_A)
class _FsRstPortTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsRstPortTrapIndex_Type.__name__=_C
_FsRstPortTrapIndex_Object=MibTableColumn
fsRstPortTrapIndex=_FsRstPortTrapIndex_Object((1,3,6,1,4,1,10876,101,1,79,2,4,1,1),_FsRstPortTrapIndex_Type())
fsRstPortTrapIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:fsRstPortTrapIndex.setStatus(_A)
class _FsRstPortMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sendstp',0),('sendrstp',1)))
_FsRstPortMigrationType_Type.__name__=_C
_FsRstPortMigrationType_Object=MibTableColumn
fsRstPortMigrationType=_FsRstPortMigrationType_Object((1,3,6,1,4,1,10876,101,1,79,2,4,1,2),_FsRstPortMigrationType_Type())
fsRstPortMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortMigrationType.setStatus(_A)
class _FsRstPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7)))
_FsRstPktErrType_Type.__name__=_C
_FsRstPktErrType_Object=MibTableColumn
fsRstPktErrType=_FsRstPktErrType_Object((1,3,6,1,4,1,10876,101,1,79,2,4,1,3),_FsRstPktErrType_Type())
fsRstPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPktErrType.setStatus(_A)
_FsRstPktErrVal_Type=Integer32
_FsRstPktErrVal_Object=MibTableColumn
fsRstPktErrVal=_FsRstPktErrVal_Object((1,3,6,1,4,1,10876,101,1,79,2,4,1,4),_FsRstPktErrVal_Type())
fsRstPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPktErrVal.setStatus(_A)
class _FsRstPortRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4)))
_FsRstPortRoleType_Type.__name__=_C
_FsRstPortRoleType_Object=MibTableColumn
fsRstPortRoleType=_FsRstPortRoleType_Object((1,3,6,1,4,1,10876,101,1,79,2,4,1,5),_FsRstPortRoleType_Type())
fsRstPortRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstPortRoleType.setStatus(_A)
class _FsRstOldRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4)))
_FsRstOldRoleType_Type.__name__=_C
_FsRstOldRoleType_Object=MibTableColumn
fsRstOldRoleType=_FsRstOldRoleType_Object((1,3,6,1,4,1,10876,101,1,79,2,4,1,6),_FsRstOldRoleType_Type())
fsRstOldRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRstOldRoleType.setStatus(_A)
_Dot1wFutureRstTraps_ObjectIdentity=ObjectIdentity
dot1wFutureRstTraps=_Dot1wFutureRstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,79,3))
_FsRstTraps_ObjectIdentity=ObjectIdentity
fsRstTraps=_FsRstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,79,3,0))
fsRstGenTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,1))
fsRstGenTrap.setObjects(*((_E,_G),(_F,_c)))
if mibBuilder.loadTexts:fsRstGenTrap.setStatus(_A)
fsRstErrTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,2))
fsRstErrTrap.setObjects(*((_E,_G),(_F,_d)))
if mibBuilder.loadTexts:fsRstErrTrap.setStatus(_A)
fsRstNewRootTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,3))
fsRstNewRootTrap.setObjects(*((_E,_G),(_F,_e),(_E,_O)))
if mibBuilder.loadTexts:fsRstNewRootTrap.setStatus(_A)
fsRstTopologyChgTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,4))
fsRstTopologyChgTrap.setObjects((_E,_G))
if mibBuilder.loadTexts:fsRstTopologyChgTrap.setStatus(_A)
fsRstProtocolMigrationTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,5))
fsRstProtocolMigrationTrap.setObjects(*((_E,_G),(_Q,_R),(_F,_f)))
if mibBuilder.loadTexts:fsRstProtocolMigrationTrap.setStatus(_A)
fsRstInvalidBpduRxdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,6))
fsRstInvalidBpduRxdTrap.setObjects(*((_E,_G),(_F,_g),(_F,_h)))
if mibBuilder.loadTexts:fsRstInvalidBpduRxdTrap.setStatus(_A)
fsRstNewPortRoleTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,7))
fsRstNewPortRoleTrap.setObjects(*((_E,_G),(_F,_i),(_F,_j)))
if mibBuilder.loadTexts:fsRstNewPortRoleTrap.setStatus(_A)
fsRstHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,79,3,0,8))
fsRstHwFailureTrap.setObjects(*((_E,_G),(_E,_P)))
if mibBuilder.loadTexts:fsRstHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'EnabledStatus':EnabledStatus,'futureRstMIB':futureRstMIB,'dot1wFutureRst':dot1wFutureRst,'fsRstSystemControl':fsRstSystemControl,'fsRstModuleStatus':fsRstModuleStatus,'fsRstTraceOption':fsRstTraceOption,'fsRstDebugOption':fsRstDebugOption,'fsRstRstpUpCount':fsRstRstpUpCount,'fsRstRstpDownCount':fsRstRstpDownCount,'fsRstBufferFailureCount':fsRstBufferFailureCount,'fsRstMemAllocFailureCount':fsRstMemAllocFailureCount,'fsRstNewRootIdCount':fsRstNewRootIdCount,'fsRstPortRoleSelSmState':fsRstPortRoleSelSmState,_e:fsRstOldDesignatedRoot,'fsRstPortExtTable':fsRstPortExtTable,'fsRstPortExtEntry':fsRstPortExtEntry,_T:fsRstPort,'fsRstPortRole':fsRstPortRole,'fsRstPortOperVersion':fsRstPortOperVersion,'fsRstPortInfoSmState':fsRstPortInfoSmState,'fsRstPortMigSmState':fsRstPortMigSmState,'fsRstPortRoleTransSmState':fsRstPortRoleTransSmState,'fsRstPortStateTransSmState':fsRstPortStateTransSmState,'fsRstPortTopoChSmState':fsRstPortTopoChSmState,'fsRstPortTxSmState':fsRstPortTxSmState,'fsRstPortRxRstBpduCount':fsRstPortRxRstBpduCount,'fsRstPortRxConfigBpduCount':fsRstPortRxConfigBpduCount,'fsRstPortRxTcnBpduCount':fsRstPortRxTcnBpduCount,'fsRstPortTxRstBpduCount':fsRstPortTxRstBpduCount,'fsRstPortTxConfigBpduCount':fsRstPortTxConfigBpduCount,'fsRstPortTxTcnBpduCount':fsRstPortTxTcnBpduCount,'fsRstPortInvalidRstBpduRxCount':fsRstPortInvalidRstBpduRxCount,'fsRstPortInvalidConfigBpduRxCount':fsRstPortInvalidConfigBpduRxCount,'fsRstPortInvalidTcnBpduRxCount':fsRstPortInvalidTcnBpduRxCount,'fsRstPortProtocolMigrationCount':fsRstPortProtocolMigrationCount,'fsRstPortEffectivePortState':fsRstPortEffectivePortState,'fsRstPortAutoEdge':fsRstPortAutoEdge,'fsRstPortRestrictedRole':fsRstPortRestrictedRole,'fsRstPortRestrictedTCN':fsRstPortRestrictedTCN,'fsRstPortEnableBPDURx':fsRstPortEnableBPDURx,'fsRstPortEnableBPDUTx':fsRstPortEnableBPDUTx,'fsRstPortPseudoRootId':fsRstPortPseudoRootId,'fsRstPortIsL2Gp':fsRstPortIsL2Gp,'fsRstPortLoopGuard':fsRstPortLoopGuard,'fsRstPortRcvdEvent':fsRstPortRcvdEvent,'fsRstPortRcvdEventSubType':fsRstPortRcvdEventSubType,'fsRstPortRcvdEventTimeStamp':fsRstPortRcvdEventTimeStamp,'fsRstPortStateChangeTimeStamp':fsRstPortStateChangeTimeStamp,'fsRstPortRowStatus':fsRstPortRowStatus,'fsRstPortBpduGuard':fsRstPortBpduGuard,'fsRstDynamicPathcostCalculation':fsRstDynamicPathcostCalculation,'fsRstCalcPortPathCostOnSpeedChg':fsRstCalcPortPathCostOnSpeedChg,'fsRstRcvdEvent':fsRstRcvdEvent,'fsRstRcvdEventSubType':fsRstRcvdEventSubType,'fsRstRcvdEventTimeStamp':fsRstRcvdEventTimeStamp,'fsRstRcvdPortStateChangeTimeStamp':fsRstRcvdPortStateChangeTimeStamp,'fsRstBpduGuard':fsRstBpduGuard,'dot1wFsRstTrapsControl':dot1wFsRstTrapsControl,'fsRstSetTraps':fsRstSetTraps,_c:fsRstGenTrapType,_d:fsRstErrTrapType,'fsRstPortTrapNotificationTable':fsRstPortTrapNotificationTable,'fsRstPortTrapNotificationEntry':fsRstPortTrapNotificationEntry,_b:fsRstPortTrapIndex,_f:fsRstPortMigrationType,_g:fsRstPktErrType,_h:fsRstPktErrVal,_i:fsRstPortRoleType,_j:fsRstOldRoleType,'dot1wFutureRstTraps':dot1wFutureRstTraps,'fsRstTraps':fsRstTraps,'fsRstGenTrap':fsRstGenTrap,'fsRstErrTrap':fsRstErrTrap,'fsRstNewRootTrap':fsRstNewRootTrap,'fsRstTopologyChgTrap':fsRstTopologyChgTrap,'fsRstProtocolMigrationTrap':fsRstProtocolMigrationTrap,'fsRstInvalidBpduRxdTrap':fsRstInvalidBpduRxdTrap,'fsRstNewPortRoleTrap':fsRstNewPortRoleTrap,'fsRstHwFailureTrap':fsRstHwFailureTrap})