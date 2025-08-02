_U='nnRstPortNotificationMigrationType'
_T='nnRstDot1dStpVersion'
_S='nnRstDot1wOldDesignatedRoot'
_R='nnRstErrNotificationType'
_Q='nnRstGenNotificationType'
_P='nnRstPortNotificationIndex'
_O='sendstp'
_N='sendrstp'
_M='not-accessible'
_L='nnRstDot1wPort'
_K='stpCompatible'
_J='dot1dStpPort'
_I='dot1dStpDesignatedRoot'
_H='init'
_G='dot1dBaseBridgeAddress'
_F='NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB'
_E='read-write'
_D='BRIDGE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,dot1dBaseBridgeAddress,dot1dStpDesignatedRoot,dot1dStpPort=mibBuilder.importSymbols(_D,'BridgeId','Timeout',_G,_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
nnRapidSpanningTreeMib=ModuleIdentity((1,3,6,1,4,1,45,5,4))
if mibBuilder.loadTexts:nnRapidSpanningTreeMib.setRevisions(('2014-07-29 00:00','2004-02-24 00:00'))
_NnRstNotifications_ObjectIdentity=ObjectIdentity
nnRstNotifications=_NnRstNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,4,0))
_NnRstObjects_ObjectIdentity=ObjectIdentity
nnRstObjects=_NnRstObjects_ObjectIdentity((1,3,6,1,4,1,45,5,4,1))
_NnRstDot1d_ObjectIdentity=ObjectIdentity
nnRstDot1d=_NnRstDot1d_ObjectIdentity((1,3,6,1,4,1,45,5,4,1,1))
_NnRstDot1dScalars_ObjectIdentity=ObjectIdentity
nnRstDot1dScalars=_NnRstDot1dScalars_ObjectIdentity((1,3,6,1,4,1,45,5,4,1,1,1))
class _NnRstDot1dStpVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_K,0),('rstp',2)))
_NnRstDot1dStpVersion_Type.__name__=_C
_NnRstDot1dStpVersion_Object=MibScalar
nnRstDot1dStpVersion=_NnRstDot1dStpVersion_Object((1,3,6,1,4,1,45,5,4,1,1,1,1),_NnRstDot1dStpVersion_Type())
nnRstDot1dStpVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstDot1dStpVersion.setStatus(_A)
class _NnRstDot1dStpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NnRstDot1dStpTxHoldCount_Type.__name__=_C
_NnRstDot1dStpTxHoldCount_Object=MibScalar
nnRstDot1dStpTxHoldCount=_NnRstDot1dStpTxHoldCount_Object((1,3,6,1,4,1,45,5,4,1,1,1,2),_NnRstDot1dStpTxHoldCount_Type())
nnRstDot1dStpTxHoldCount.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstDot1dStpTxHoldCount.setStatus(_A)
class _NnRstDot1dStpPathCostDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_NnRstDot1dStpPathCostDefault_Type.__name__=_C
_NnRstDot1dStpPathCostDefault_Object=MibScalar
nnRstDot1dStpPathCostDefault=_NnRstDot1dStpPathCostDefault_Object((1,3,6,1,4,1,45,5,4,1,1,1,3),_NnRstDot1dStpPathCostDefault_Type())
nnRstDot1dStpPathCostDefault.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstDot1dStpPathCostDefault.setStatus(_A)
_NnRstDot1dStpPortTable_Object=MibTable
nnRstDot1dStpPortTable=_NnRstDot1dStpPortTable_Object((1,3,6,1,4,1,45,5,4,1,1,2))
if mibBuilder.loadTexts:nnRstDot1dStpPortTable.setStatus(_A)
_NnRstDot1dStpPortEntry_Object=MibTableRow
nnRstDot1dStpPortEntry=_NnRstDot1dStpPortEntry_Object((1,3,6,1,4,1,45,5,4,1,1,2,1))
nnRstDot1dStpPortEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:nnRstDot1dStpPortEntry.setStatus(_A)
_NnRstDot1dStpPortProtocolMigration_Type=TruthValue
_NnRstDot1dStpPortProtocolMigration_Object=MibTableColumn
nnRstDot1dStpPortProtocolMigration=_NnRstDot1dStpPortProtocolMigration_Object((1,3,6,1,4,1,45,5,4,1,1,2,1,1),_NnRstDot1dStpPortProtocolMigration_Type())
nnRstDot1dStpPortProtocolMigration.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstDot1dStpPortProtocolMigration.setStatus(_A)
_NnRstDot1dStpPortAdminEdgePort_Type=TruthValue
_NnRstDot1dStpPortAdminEdgePort_Object=MibTableColumn
nnRstDot1dStpPortAdminEdgePort=_NnRstDot1dStpPortAdminEdgePort_Object((1,3,6,1,4,1,45,5,4,1,1,2,1,2),_NnRstDot1dStpPortAdminEdgePort_Type())
nnRstDot1dStpPortAdminEdgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstDot1dStpPortAdminEdgePort.setStatus(_A)
_NnRstDot1dStpPortOperEdgePort_Type=TruthValue
_NnRstDot1dStpPortOperEdgePort_Object=MibTableColumn
nnRstDot1dStpPortOperEdgePort=_NnRstDot1dStpPortOperEdgePort_Object((1,3,6,1,4,1,45,5,4,1,1,2,1,3),_NnRstDot1dStpPortOperEdgePort_Type())
nnRstDot1dStpPortOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1dStpPortOperEdgePort.setStatus(_A)
class _NnRstDot1dStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_NnRstDot1dStpPortAdminPointToPoint_Type.__name__=_C
_NnRstDot1dStpPortAdminPointToPoint_Object=MibTableColumn
nnRstDot1dStpPortAdminPointToPoint=_NnRstDot1dStpPortAdminPointToPoint_Object((1,3,6,1,4,1,45,5,4,1,1,2,1,4),_NnRstDot1dStpPortAdminPointToPoint_Type())
nnRstDot1dStpPortAdminPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstDot1dStpPortAdminPointToPoint.setStatus(_A)
_NnRstDot1dStpPortOperPointToPoint_Type=TruthValue
_NnRstDot1dStpPortOperPointToPoint_Object=MibTableColumn
nnRstDot1dStpPortOperPointToPoint=_NnRstDot1dStpPortOperPointToPoint_Object((1,3,6,1,4,1,45,5,4,1,1,2,1,5),_NnRstDot1dStpPortOperPointToPoint_Type())
nnRstDot1dStpPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1dStpPortOperPointToPoint.setStatus(_A)
_NnRstDot1dStpPortParticipating_Type=TruthValue
_NnRstDot1dStpPortParticipating_Object=MibTableColumn
nnRstDot1dStpPortParticipating=_NnRstDot1dStpPortParticipating_Object((1,3,6,1,4,1,45,5,4,1,1,2,1,6),_NnRstDot1dStpPortParticipating_Type())
nnRstDot1dStpPortParticipating.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstDot1dStpPortParticipating.setStatus(_A)
_NnRstDot1w_ObjectIdentity=ObjectIdentity
nnRstDot1w=_NnRstDot1w_ObjectIdentity((1,3,6,1,4,1,45,5,4,1,2))
_NnRstDot1wScalars_ObjectIdentity=ObjectIdentity
nnRstDot1wScalars=_NnRstDot1wScalars_ObjectIdentity((1,3,6,1,4,1,45,5,4,1,2,1))
_NnRstDot1wRstpUpCount_Type=Counter32
_NnRstDot1wRstpUpCount_Object=MibScalar
nnRstDot1wRstpUpCount=_NnRstDot1wRstpUpCount_Object((1,3,6,1,4,1,45,5,4,1,2,1,1),_NnRstDot1wRstpUpCount_Type())
nnRstDot1wRstpUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wRstpUpCount.setStatus(_A)
_NnRstDot1wRstpDownCount_Type=Counter32
_NnRstDot1wRstpDownCount_Object=MibScalar
nnRstDot1wRstpDownCount=_NnRstDot1wRstpDownCount_Object((1,3,6,1,4,1,45,5,4,1,2,1,2),_NnRstDot1wRstpDownCount_Type())
nnRstDot1wRstpDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wRstpDownCount.setStatus(_A)
_NnRstDot1wNewRootIdCount_Type=Counter32
_NnRstDot1wNewRootIdCount_Object=MibScalar
nnRstDot1wNewRootIdCount=_NnRstDot1wNewRootIdCount_Object((1,3,6,1,4,1,45,5,4,1,2,1,3),_NnRstDot1wNewRootIdCount_Type())
nnRstDot1wNewRootIdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wNewRootIdCount.setStatus(_A)
class _NnRstDot1wPortRoleSelSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('initbridge',0),('roleselection',1)))
_NnRstDot1wPortRoleSelSmState_Type.__name__=_C
_NnRstDot1wPortRoleSelSmState_Object=MibScalar
nnRstDot1wPortRoleSelSmState=_NnRstDot1wPortRoleSelSmState_Object((1,3,6,1,4,1,45,5,4,1,2,1,4),_NnRstDot1wPortRoleSelSmState_Type())
nnRstDot1wPortRoleSelSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortRoleSelSmState.setStatus(_A)
_NnRstDot1wOldDesignatedRoot_Type=BridgeId
_NnRstDot1wOldDesignatedRoot_Object=MibScalar
nnRstDot1wOldDesignatedRoot=_NnRstDot1wOldDesignatedRoot_Object((1,3,6,1,4,1,45,5,4,1,2,1,5),_NnRstDot1wOldDesignatedRoot_Type())
nnRstDot1wOldDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wOldDesignatedRoot.setStatus(_A)
_NnRstDot1wPortTable_Object=MibTable
nnRstDot1wPortTable=_NnRstDot1wPortTable_Object((1,3,6,1,4,1,45,5,4,1,2,2))
if mibBuilder.loadTexts:nnRstDot1wPortTable.setStatus(_A)
_NnRstDot1wPortEntry_Object=MibTableRow
nnRstDot1wPortEntry=_NnRstDot1wPortEntry_Object((1,3,6,1,4,1,45,5,4,1,2,2,1))
nnRstDot1wPortEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:nnRstDot1wPortEntry.setStatus(_A)
class _NnRstDot1wPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_NnRstDot1wPort_Type.__name__=_C
_NnRstDot1wPort_Object=MibTableColumn
nnRstDot1wPort=_NnRstDot1wPort_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,1),_NnRstDot1wPort_Type())
nnRstDot1wPort.setMaxAccess(_M)
if mibBuilder.loadTexts:nnRstDot1wPort.setStatus(_A)
class _NnRstDot1wPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('disabledPort',0),('alternatePort',1),('backupPort',2),('rootPort',3),('designatedPort',4)))
_NnRstDot1wPortRole_Type.__name__=_C
_NnRstDot1wPortRole_Object=MibTableColumn
nnRstDot1wPortRole=_NnRstDot1wPortRole_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,2),_NnRstDot1wPortRole_Type())
nnRstDot1wPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortRole.setStatus(_A)
class _NnRstDot1wPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_K,0),('rstp',2)))
_NnRstDot1wPortOperVersion_Type.__name__=_C
_NnRstDot1wPortOperVersion_Object=MibTableColumn
nnRstDot1wPortOperVersion=_NnRstDot1wPortOperVersion_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,3),_NnRstDot1wPortOperVersion_Type())
nnRstDot1wPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortOperVersion.setStatus(_A)
class _NnRstDot1wPortInfoSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disabled',0),('aged',1),('update',2),('superior',3),('repeat',4),('agreement',5),('present',6),('receive',7)))
_NnRstDot1wPortInfoSmState_Type.__name__=_C
_NnRstDot1wPortInfoSmState_Object=MibTableColumn
nnRstDot1wPortInfoSmState=_NnRstDot1wPortInfoSmState_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,4),_NnRstDot1wPortInfoSmState_Type())
nnRstDot1wPortInfoSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortInfoSmState.setStatus(_A)
class _NnRstDot1wPortMigSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),(_N,1),('sendingrstp',2),(_O,3),('sendingstp',4)))
_NnRstDot1wPortMigSmState_Type.__name__=_C
_NnRstDot1wPortMigSmState_Object=MibTableColumn
nnRstDot1wPortMigSmState=_NnRstDot1wPortMigSmState_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,5),_NnRstDot1wPortMigSmState_Type())
nnRstDot1wPortMigSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortMigSmState.setStatus(_A)
class _NnRstDot1wPortRoleTransSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_H,0),('blockport',1),('blockedport',2),('rootport',3),('designatedport',4),('backupport',5),('rootproposed',6),('rootagreed',7),('reroot',8),('rootforward',9),('rootlearn',10),('rerooted',11),('designatedpropose',12),('designatedsynced',13),('designatedretired',14),('designatedforward',15),('designatedlearn',16),('designatedlisten',17)))
_NnRstDot1wPortRoleTransSmState_Type.__name__=_C
_NnRstDot1wPortRoleTransSmState_Object=MibTableColumn
nnRstDot1wPortRoleTransSmState=_NnRstDot1wPortRoleTransSmState_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,6),_NnRstDot1wPortRoleTransSmState_Type())
nnRstDot1wPortRoleTransSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortRoleTransSmState.setStatus(_A)
class _NnRstDot1wPortStateTransSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('discarding',0),('learning',1),('forwarding',2)))
_NnRstDot1wPortStateTransSmState_Type.__name__=_C
_NnRstDot1wPortStateTransSmState_Object=MibTableColumn
nnRstDot1wPortStateTransSmState=_NnRstDot1wPortStateTransSmState_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,7),_NnRstDot1wPortStateTransSmState_Type())
nnRstDot1wPortStateTransSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortStateTransSmState.setStatus(_A)
class _NnRstDot1wPortTopoChSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,0),('inactive',1),('active',2),('detected',3),('notifiedtcn',4),('notifiedtc',5),('propagating',6),('acknowledged',7)))
_NnRstDot1wPortTopoChSmState_Type.__name__=_C
_NnRstDot1wPortTopoChSmState_Object=MibTableColumn
nnRstDot1wPortTopoChSmState=_NnRstDot1wPortTopoChSmState_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,8),_NnRstDot1wPortTopoChSmState_Type())
nnRstDot1wPortTopoChSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortTopoChSmState.setStatus(_A)
class _NnRstDot1wPortTxSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_NnRstDot1wPortTxSmState_Type.__name__=_C
_NnRstDot1wPortTxSmState_Object=MibTableColumn
nnRstDot1wPortTxSmState=_NnRstDot1wPortTxSmState_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,9),_NnRstDot1wPortTxSmState_Type())
nnRstDot1wPortTxSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortTxSmState.setStatus(_A)
_NnRstDot1wPortRxRstBpduCount_Type=Counter32
_NnRstDot1wPortRxRstBpduCount_Object=MibTableColumn
nnRstDot1wPortRxRstBpduCount=_NnRstDot1wPortRxRstBpduCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,10),_NnRstDot1wPortRxRstBpduCount_Type())
nnRstDot1wPortRxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortRxRstBpduCount.setStatus(_A)
_NnRstDot1wPortRxConfigBpduCount_Type=Counter32
_NnRstDot1wPortRxConfigBpduCount_Object=MibTableColumn
nnRstDot1wPortRxConfigBpduCount=_NnRstDot1wPortRxConfigBpduCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,11),_NnRstDot1wPortRxConfigBpduCount_Type())
nnRstDot1wPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortRxConfigBpduCount.setStatus(_A)
_NnRstDot1wPortRxTcnBpduCount_Type=Counter32
_NnRstDot1wPortRxTcnBpduCount_Object=MibTableColumn
nnRstDot1wPortRxTcnBpduCount=_NnRstDot1wPortRxTcnBpduCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,12),_NnRstDot1wPortRxTcnBpduCount_Type())
nnRstDot1wPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortRxTcnBpduCount.setStatus(_A)
_NnRstDot1wPortTxRstBpduCount_Type=Counter32
_NnRstDot1wPortTxRstBpduCount_Object=MibTableColumn
nnRstDot1wPortTxRstBpduCount=_NnRstDot1wPortTxRstBpduCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,13),_NnRstDot1wPortTxRstBpduCount_Type())
nnRstDot1wPortTxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortTxRstBpduCount.setStatus(_A)
_NnRstDot1wPortTxConfigBpduCount_Type=Counter32
_NnRstDot1wPortTxConfigBpduCount_Object=MibTableColumn
nnRstDot1wPortTxConfigBpduCount=_NnRstDot1wPortTxConfigBpduCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,14),_NnRstDot1wPortTxConfigBpduCount_Type())
nnRstDot1wPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortTxConfigBpduCount.setStatus(_A)
_NnRstDot1wPortTxTcnBpduCount_Type=Counter32
_NnRstDot1wPortTxTcnBpduCount_Object=MibTableColumn
nnRstDot1wPortTxTcnBpduCount=_NnRstDot1wPortTxTcnBpduCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,15),_NnRstDot1wPortTxTcnBpduCount_Type())
nnRstDot1wPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortTxTcnBpduCount.setStatus(_A)
_NnRstDot1wPortInvalidRstBpduRxCount_Type=Counter32
_NnRstDot1wPortInvalidRstBpduRxCount_Object=MibTableColumn
nnRstDot1wPortInvalidRstBpduRxCount=_NnRstDot1wPortInvalidRstBpduRxCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,16),_NnRstDot1wPortInvalidRstBpduRxCount_Type())
nnRstDot1wPortInvalidRstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortInvalidRstBpduRxCount.setStatus(_A)
_NnRstDot1wPortInvalidConfigBpduRxCount_Type=Counter32
_NnRstDot1wPortInvalidConfigBpduRxCount_Object=MibTableColumn
nnRstDot1wPortInvalidConfigBpduRxCount=_NnRstDot1wPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,17),_NnRstDot1wPortInvalidConfigBpduRxCount_Type())
nnRstDot1wPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortInvalidConfigBpduRxCount.setStatus(_A)
_NnRstDot1wPortInvalidTcnBpduRxCount_Type=Counter32
_NnRstDot1wPortInvalidTcnBpduRxCount_Object=MibTableColumn
nnRstDot1wPortInvalidTcnBpduRxCount=_NnRstDot1wPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,18),_NnRstDot1wPortInvalidTcnBpduRxCount_Type())
nnRstDot1wPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortInvalidTcnBpduRxCount.setStatus(_A)
_NnRstDot1wPortProtocolMigrationCount_Type=Counter32
_NnRstDot1wPortProtocolMigrationCount_Object=MibTableColumn
nnRstDot1wPortProtocolMigrationCount=_NnRstDot1wPortProtocolMigrationCount_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,19),_NnRstDot1wPortProtocolMigrationCount_Type())
nnRstDot1wPortProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortProtocolMigrationCount.setStatus(_A)
_NnRstDot1wPortEffectivePortState_Type=TruthValue
_NnRstDot1wPortEffectivePortState_Object=MibTableColumn
nnRstDot1wPortEffectivePortState=_NnRstDot1wPortEffectivePortState_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,20),_NnRstDot1wPortEffectivePortState_Type())
nnRstDot1wPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortEffectivePortState.setStatus(_A)
_NnRstDot1wPortForwardTransitions_Type=Counter32
_NnRstDot1wPortForwardTransitions_Object=MibTableColumn
nnRstDot1wPortForwardTransitions=_NnRstDot1wPortForwardTransitions_Object((1,3,6,1,4,1,45,5,4,1,2,2,1,21),_NnRstDot1wPortForwardTransitions_Type())
nnRstDot1wPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstDot1wPortForwardTransitions.setStatus(_A)
_NnRstNotificationControl_ObjectIdentity=ObjectIdentity
nnRstNotificationControl=_NnRstNotificationControl_ObjectIdentity((1,3,6,1,4,1,45,5,4,1,3))
_NnRstNotificationControlScalars_ObjectIdentity=ObjectIdentity
nnRstNotificationControlScalars=_NnRstNotificationControlScalars_ObjectIdentity((1,3,6,1,4,1,45,5,4,1,3,1))
class _NnRstSetNotifications_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NnRstSetNotifications_Type.__name__=_C
_NnRstSetNotifications_Object=MibScalar
nnRstSetNotifications=_NnRstSetNotifications_Object((1,3,6,1,4,1,45,5,4,1,3,1,1),_NnRstSetNotifications_Type())
nnRstSetNotifications.setMaxAccess(_E)
if mibBuilder.loadTexts:nnRstSetNotifications.setStatus(_A)
class _NnRstGenNotificationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('up',1),('down',2)))
_NnRstGenNotificationType_Type.__name__=_C
_NnRstGenNotificationType_Object=MibScalar
nnRstGenNotificationType=_NnRstGenNotificationType_Object((1,3,6,1,4,1,45,5,4,1,3,1,2),_NnRstGenNotificationType_Type())
nnRstGenNotificationType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstGenNotificationType.setStatus(_A)
class _NnRstErrNotificationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('memfail',1),('bufffail',2)))
_NnRstErrNotificationType_Type.__name__=_C
_NnRstErrNotificationType_Object=MibScalar
nnRstErrNotificationType=_NnRstErrNotificationType_Object((1,3,6,1,4,1,45,5,4,1,3,1,3),_NnRstErrNotificationType_Type())
nnRstErrNotificationType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstErrNotificationType.setStatus(_A)
_NnRstPortNotificationTable_Object=MibTable
nnRstPortNotificationTable=_NnRstPortNotificationTable_Object((1,3,6,1,4,1,45,5,4,1,3,2))
if mibBuilder.loadTexts:nnRstPortNotificationTable.setStatus(_A)
_NnRstPortNotificationEntry_Object=MibTableRow
nnRstPortNotificationEntry=_NnRstPortNotificationEntry_Object((1,3,6,1,4,1,45,5,4,1,3,2,1))
nnRstPortNotificationEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:nnRstPortNotificationEntry.setStatus(_A)
class _NnRstPortNotificationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_NnRstPortNotificationIndex_Type.__name__=_C
_NnRstPortNotificationIndex_Object=MibTableColumn
nnRstPortNotificationIndex=_NnRstPortNotificationIndex_Object((1,3,6,1,4,1,45,5,4,1,3,2,1,1),_NnRstPortNotificationIndex_Type())
nnRstPortNotificationIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:nnRstPortNotificationIndex.setStatus(_A)
class _NnRstPortNotificationMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_N,1)))
_NnRstPortNotificationMigrationType_Type.__name__=_C
_NnRstPortNotificationMigrationType_Object=MibTableColumn
nnRstPortNotificationMigrationType=_NnRstPortNotificationMigrationType_Object((1,3,6,1,4,1,45,5,4,1,3,2,1,2),_NnRstPortNotificationMigrationType_Type())
nnRstPortNotificationMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstPortNotificationMigrationType.setStatus(_A)
class _NnRstPortNotificationPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7)))
_NnRstPortNotificationPktErrType_Type.__name__=_C
_NnRstPortNotificationPktErrType_Object=MibTableColumn
nnRstPortNotificationPktErrType=_NnRstPortNotificationPktErrType_Object((1,3,6,1,4,1,45,5,4,1,3,2,1,3),_NnRstPortNotificationPktErrType_Type())
nnRstPortNotificationPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstPortNotificationPktErrType.setStatus(_A)
_NnRstPortNotificationPktErrVal_Type=Integer32
_NnRstPortNotificationPktErrVal_Object=MibTableColumn
nnRstPortNotificationPktErrVal=_NnRstPortNotificationPktErrVal_Object((1,3,6,1,4,1,45,5,4,1,3,2,1,4),_NnRstPortNotificationPktErrVal_Type())
nnRstPortNotificationPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:nnRstPortNotificationPktErrVal.setStatus(_A)
nnRstGeneralEvent=NotificationType((1,3,6,1,4,1,45,5,4,0,1))
nnRstGeneralEvent.setObjects(*((_D,_G),(_F,_Q)))
if mibBuilder.loadTexts:nnRstGeneralEvent.setStatus(_A)
nnRstErrorEvent=NotificationType((1,3,6,1,4,1,45,5,4,0,2))
nnRstErrorEvent.setObjects(*((_D,_G),(_F,_R)))
if mibBuilder.loadTexts:nnRstErrorEvent.setStatus(_A)
nnRstNewRoot=NotificationType((1,3,6,1,4,1,45,5,4,0,3))
nnRstNewRoot.setObjects(*((_D,_G),(_F,_S),(_D,_I)))
if mibBuilder.loadTexts:nnRstNewRoot.setStatus(_A)
nnRstTopologyChange=NotificationType((1,3,6,1,4,1,45,5,4,0,4))
nnRstTopologyChange.setObjects((_D,_G))
if mibBuilder.loadTexts:nnRstTopologyChange.setStatus(_A)
nnRstProtocolMigration=NotificationType((1,3,6,1,4,1,45,5,4,0,5))
nnRstProtocolMigration.setObjects(*((_D,_G),(_F,_T),(_F,_U)))
if mibBuilder.loadTexts:nnRstProtocolMigration.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'nnRapidSpanningTreeMib':nnRapidSpanningTreeMib,'nnRstNotifications':nnRstNotifications,'nnRstGeneralEvent':nnRstGeneralEvent,'nnRstErrorEvent':nnRstErrorEvent,'nnRstNewRoot':nnRstNewRoot,'nnRstTopologyChange':nnRstTopologyChange,'nnRstProtocolMigration':nnRstProtocolMigration,'nnRstObjects':nnRstObjects,'nnRstDot1d':nnRstDot1d,'nnRstDot1dScalars':nnRstDot1dScalars,_T:nnRstDot1dStpVersion,'nnRstDot1dStpTxHoldCount':nnRstDot1dStpTxHoldCount,'nnRstDot1dStpPathCostDefault':nnRstDot1dStpPathCostDefault,'nnRstDot1dStpPortTable':nnRstDot1dStpPortTable,'nnRstDot1dStpPortEntry':nnRstDot1dStpPortEntry,'nnRstDot1dStpPortProtocolMigration':nnRstDot1dStpPortProtocolMigration,'nnRstDot1dStpPortAdminEdgePort':nnRstDot1dStpPortAdminEdgePort,'nnRstDot1dStpPortOperEdgePort':nnRstDot1dStpPortOperEdgePort,'nnRstDot1dStpPortAdminPointToPoint':nnRstDot1dStpPortAdminPointToPoint,'nnRstDot1dStpPortOperPointToPoint':nnRstDot1dStpPortOperPointToPoint,'nnRstDot1dStpPortParticipating':nnRstDot1dStpPortParticipating,'nnRstDot1w':nnRstDot1w,'nnRstDot1wScalars':nnRstDot1wScalars,'nnRstDot1wRstpUpCount':nnRstDot1wRstpUpCount,'nnRstDot1wRstpDownCount':nnRstDot1wRstpDownCount,'nnRstDot1wNewRootIdCount':nnRstDot1wNewRootIdCount,'nnRstDot1wPortRoleSelSmState':nnRstDot1wPortRoleSelSmState,_S:nnRstDot1wOldDesignatedRoot,'nnRstDot1wPortTable':nnRstDot1wPortTable,'nnRstDot1wPortEntry':nnRstDot1wPortEntry,_L:nnRstDot1wPort,'nnRstDot1wPortRole':nnRstDot1wPortRole,'nnRstDot1wPortOperVersion':nnRstDot1wPortOperVersion,'nnRstDot1wPortInfoSmState':nnRstDot1wPortInfoSmState,'nnRstDot1wPortMigSmState':nnRstDot1wPortMigSmState,'nnRstDot1wPortRoleTransSmState':nnRstDot1wPortRoleTransSmState,'nnRstDot1wPortStateTransSmState':nnRstDot1wPortStateTransSmState,'nnRstDot1wPortTopoChSmState':nnRstDot1wPortTopoChSmState,'nnRstDot1wPortTxSmState':nnRstDot1wPortTxSmState,'nnRstDot1wPortRxRstBpduCount':nnRstDot1wPortRxRstBpduCount,'nnRstDot1wPortRxConfigBpduCount':nnRstDot1wPortRxConfigBpduCount,'nnRstDot1wPortRxTcnBpduCount':nnRstDot1wPortRxTcnBpduCount,'nnRstDot1wPortTxRstBpduCount':nnRstDot1wPortTxRstBpduCount,'nnRstDot1wPortTxConfigBpduCount':nnRstDot1wPortTxConfigBpduCount,'nnRstDot1wPortTxTcnBpduCount':nnRstDot1wPortTxTcnBpduCount,'nnRstDot1wPortInvalidRstBpduRxCount':nnRstDot1wPortInvalidRstBpduRxCount,'nnRstDot1wPortInvalidConfigBpduRxCount':nnRstDot1wPortInvalidConfigBpduRxCount,'nnRstDot1wPortInvalidTcnBpduRxCount':nnRstDot1wPortInvalidTcnBpduRxCount,'nnRstDot1wPortProtocolMigrationCount':nnRstDot1wPortProtocolMigrationCount,'nnRstDot1wPortEffectivePortState':nnRstDot1wPortEffectivePortState,'nnRstDot1wPortForwardTransitions':nnRstDot1wPortForwardTransitions,'nnRstNotificationControl':nnRstNotificationControl,'nnRstNotificationControlScalars':nnRstNotificationControlScalars,'nnRstSetNotifications':nnRstSetNotifications,_Q:nnRstGenNotificationType,_R:nnRstErrNotificationType,'nnRstPortNotificationTable':nnRstPortNotificationTable,'nnRstPortNotificationEntry':nnRstPortNotificationEntry,_P:nnRstPortNotificationIndex,_U:nnRstPortNotificationMigrationType,'nnRstPortNotificationPktErrType':nnRstPortNotificationPktErrType,'nnRstPortNotificationPktErrVal':nnRstPortNotificationPktErrVal})