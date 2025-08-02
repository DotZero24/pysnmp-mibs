_AG='mstpMstiPortGroup'
_AF='mstpMstiBridgeGroup'
_AE='mstpBridgeRegionGroup'
_AD='rstpPortGroup'
_AC='rstpBridgeGroup'
_AB='fsStpPortMstiPortForwardTransitions'
_AA='fsStpPortMstiPortRole'
_A9='fsStpPortMstiDesignatedPort'
_A8='fsStpPortMstiDesignatedBridge'
_A7='fsStpPortMstiDesignatedCost'
_A6='fsStpPortMstiDesignatedRoot'
_A5='fsStpPortMstiPriority'
_A4='fsStpPortMstiOperPathCost'
_A3='fsStpPortMstiAdminPathCost'
_A2='fsStpPortMstiState'
_A1='fsStpMstiInstanceEntryStatus'
_A0='fsStpMstiRootPort'
_z='fsStpMstiRootCost'
_y='fsStpMstiDesignatedRoot'
_x='fsStpMstiTopChanges'
_w='fsStpMstiTimeSinceTopologyChange'
_v='fsStpMstiPriority'
_u='fsStpMstiInstanceRemainingHopCount'
_t='fsStpMstiInstanceVlansGetMapped'
_s='fsStpMstiInstanceVlansDeleteMapped'
_r='fsStpMstiInstanceVlansAddMapped'
_q='fsStpMstiMaxHopNumber'
_p='fsStpMstiRegionRevision'
_o='fsStpMstiRegionName'
_n='fsStpMstiMaxInstanceNumber'
_m='fsStpCistPathCost'
_l='fsStpCistRegionRoot'
_k='fsStpPortBpduFilter'
_j='fsStpPortBpduGuard'
_i='fsStpPortOperPointToPoint'
_h='fsStpPortAdminPointToPoint'
_g='fsStpPortOperEdgePort'
_f='fsStpPortAdminEdgePort'
_e='fsStpPortProtocolMigration'
_d='fsStpPathCostDefault'
_c='fsStpBpduFilter'
_b='fsStpBpduGuard'
_a='fsStpTxHoldCount'
_Z='fsStpVersion'
_Y='fsStpPortRole'
_X='fsStpPortOperPathCost'
_W='fsStpPortAdminPathCost'
_V='fsSysStpReset'
_U='fsSysStpStatus'
_T='fsStpPortMstiIndex'
_S='masterPort'
_R='designatedPort'
_Q='rootPort'
_P='backupPort'
_O='alternatePort'
_N='disabledPort'
_M='DisplayString'
_L='EnabledStatus'
_K='rstpDefaultPathCostGroup'
_J='fsRstpExtPortIfIndex'
_I='fsStpPortIfIndex'
_H='read-create'
_G='fsStpMstiInstanceIndex'
_F='OctetString'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='FS-RSTP-MSTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention','TruthValue')
fsStpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,16))
if mibBuilder.loadTexts:fsStpMIB.setRevisions(('2002-03-20 00:00',))
_FsStpMIBObjects_ObjectIdentity=ObjectIdentity
fsStpMIBObjects=_FsStpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,1))
class _FsSysStpStatus_Type(EnabledStatus):defaultValue=2
_FsSysStpStatus_Type.__name__=_L
_FsSysStpStatus_Object=MibScalar
fsSysStpStatus=_FsSysStpStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,1),_FsSysStpStatus_Type())
fsSysStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSysStpStatus.setStatus(_A)
_FsSysStpReset_Type=Integer32
_FsSysStpReset_Object=MibScalar
fsSysStpReset=_FsSysStpReset_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,2),_FsSysStpReset_Type())
fsSysStpReset.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSysStpReset.setStatus(_A)
_FsStpExtPortTable_Object=MibTable
fsStpExtPortTable=_FsStpExtPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,3))
if mibBuilder.loadTexts:fsStpExtPortTable.setStatus(_A)
_FsStpExtPortEntry_Object=MibTableRow
fsStpExtPortEntry=_FsStpExtPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,3,1))
fsStpExtPortEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:fsStpExtPortEntry.setStatus(_A)
_FsStpPortIfIndex_Type=IfIndex
_FsStpPortIfIndex_Object=MibTableColumn
fsStpPortIfIndex=_FsStpPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,3,1,1),_FsStpPortIfIndex_Type())
fsStpPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortIfIndex.setStatus(_A)
class _FsStpPortAdminPathCost_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsStpPortAdminPathCost_Type.__name__=_E
_FsStpPortAdminPathCost_Object=MibTableColumn
fsStpPortAdminPathCost=_FsStpPortAdminPathCost_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,3,1,2),_FsStpPortAdminPathCost_Type())
fsStpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortAdminPathCost.setStatus(_A)
class _FsStpPortOperPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsStpPortOperPathCost_Type.__name__=_E
_FsStpPortOperPathCost_Object=MibTableColumn
fsStpPortOperPathCost=_FsStpPortOperPathCost_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,3,1,3),_FsStpPortOperPathCost_Type())
fsStpPortOperPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortOperPathCost.setStatus(_A)
class _FsStpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_FsStpPortRole_Type.__name__=_E
_FsStpPortRole_Object=MibTableColumn
fsStpPortRole=_FsStpPortRole_Object((1,3,6,1,4,1,52642,1,1,10,2,16,1,3,1,4),_FsStpPortRole_Type())
fsStpPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortRole.setStatus(_A)
_FsRstpMIBObjects_ObjectIdentity=ObjectIdentity
fsRstpMIBObjects=_FsRstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,2))
class _FsStpVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2),('mstp',3)))
_FsStpVersion_Type.__name__=_E
_FsStpVersion_Object=MibScalar
fsStpVersion=_FsStpVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,1),_FsStpVersion_Type())
fsStpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpVersion.setStatus(_A)
class _FsStpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsStpTxHoldCount_Type.__name__=_E
_FsStpTxHoldCount_Object=MibScalar
fsStpTxHoldCount=_FsStpTxHoldCount_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,2),_FsStpTxHoldCount_Type())
fsStpTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpTxHoldCount.setStatus(_A)
class _FsStpPathCostDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_FsStpPathCostDefault_Type.__name__=_E
_FsStpPathCostDefault_Object=MibScalar
fsStpPathCostDefault=_FsStpPathCostDefault_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,3),_FsStpPathCostDefault_Type())
fsStpPathCostDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPathCostDefault.setStatus(_A)
_FsRstpExtPortTable_Object=MibTable
fsRstpExtPortTable=_FsRstpExtPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4))
if mibBuilder.loadTexts:fsRstpExtPortTable.setStatus(_A)
_FsRstpExtPortEntry_Object=MibTableRow
fsRstpExtPortEntry=_FsRstpExtPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1))
fsRstpExtPortEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsRstpExtPortEntry.setStatus(_A)
_FsRstpExtPortIfIndex_Type=IfIndex
_FsRstpExtPortIfIndex_Object=MibTableColumn
fsRstpExtPortIfIndex=_FsRstpExtPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,1),_FsRstpExtPortIfIndex_Type())
fsRstpExtPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRstpExtPortIfIndex.setStatus(_A)
_FsStpPortProtocolMigration_Type=TruthValue
_FsStpPortProtocolMigration_Object=MibTableColumn
fsStpPortProtocolMigration=_FsStpPortProtocolMigration_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,2),_FsStpPortProtocolMigration_Type())
fsStpPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortProtocolMigration.setStatus(_A)
_FsStpPortAdminEdgePort_Type=TruthValue
_FsStpPortAdminEdgePort_Object=MibTableColumn
fsStpPortAdminEdgePort=_FsStpPortAdminEdgePort_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,3),_FsStpPortAdminEdgePort_Type())
fsStpPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortAdminEdgePort.setStatus(_A)
_FsStpPortOperEdgePort_Type=TruthValue
_FsStpPortOperEdgePort_Object=MibTableColumn
fsStpPortOperEdgePort=_FsStpPortOperEdgePort_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,4),_FsStpPortOperEdgePort_Type())
fsStpPortOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortOperEdgePort.setStatus(_A)
class _FsStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_FsStpPortAdminPointToPoint_Type.__name__=_E
_FsStpPortAdminPointToPoint_Object=MibTableColumn
fsStpPortAdminPointToPoint=_FsStpPortAdminPointToPoint_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,5),_FsStpPortAdminPointToPoint_Type())
fsStpPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortAdminPointToPoint.setStatus(_A)
_FsStpPortOperPointToPoint_Type=TruthValue
_FsStpPortOperPointToPoint_Object=MibTableColumn
fsStpPortOperPointToPoint=_FsStpPortOperPointToPoint_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,6),_FsStpPortOperPointToPoint_Type())
fsStpPortOperPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortOperPointToPoint.setStatus(_A)
_FsStpPortBpduGuard_Type=EnabledStatus
_FsStpPortBpduGuard_Object=MibTableColumn
fsStpPortBpduGuard=_FsStpPortBpduGuard_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,7),_FsStpPortBpduGuard_Type())
fsStpPortBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortBpduGuard.setStatus(_A)
_FsStpPortBpduFilter_Type=EnabledStatus
_FsStpPortBpduFilter_Object=MibTableColumn
fsStpPortBpduFilter=_FsStpPortBpduFilter_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,4,1,8),_FsStpPortBpduFilter_Type())
fsStpPortBpduFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortBpduFilter.setStatus(_A)
_FsStpBpduGuard_Type=EnabledStatus
_FsStpBpduGuard_Object=MibScalar
fsStpBpduGuard=_FsStpBpduGuard_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,5),_FsStpBpduGuard_Type())
fsStpBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpBpduGuard.setStatus(_A)
_FsStpBpduFilter_Type=EnabledStatus
_FsStpBpduFilter_Object=MibScalar
fsStpBpduFilter=_FsStpBpduFilter_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,6),_FsStpBpduFilter_Type())
fsStpBpduFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpBpduFilter.setStatus(_A)
_FsStpCistRegionRoot_Type=BridgeId
_FsStpCistRegionRoot_Object=MibScalar
fsStpCistRegionRoot=_FsStpCistRegionRoot_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,7),_FsStpCistRegionRoot_Type())
fsStpCistRegionRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpCistRegionRoot.setStatus(_A)
_FsStpCistPathCost_Type=Integer32
_FsStpCistPathCost_Object=MibScalar
fsStpCistPathCost=_FsStpCistPathCost_Object((1,3,6,1,4,1,52642,1,1,10,2,16,2,8),_FsStpCistPathCost_Type())
fsStpCistPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpCistPathCost.setStatus(_A)
_FsMstpMIBObjects_ObjectIdentity=ObjectIdentity
fsMstpMIBObjects=_FsMstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,3))
_FsStpMstiMaxInstanceNumber_Type=Integer32
_FsStpMstiMaxInstanceNumber_Object=MibScalar
fsStpMstiMaxInstanceNumber=_FsStpMstiMaxInstanceNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,1),_FsStpMstiMaxInstanceNumber_Type())
fsStpMstiMaxInstanceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiMaxInstanceNumber.setStatus(_A)
class _FsStpMstiRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsStpMstiRegionName_Type.__name__=_M
_FsStpMstiRegionName_Object=MibScalar
fsStpMstiRegionName=_FsStpMstiRegionName_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,2),_FsStpMstiRegionName_Type())
fsStpMstiRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpMstiRegionName.setStatus(_A)
class _FsStpMstiRegionRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsStpMstiRegionRevision_Type.__name__=_E
_FsStpMstiRegionRevision_Object=MibScalar
fsStpMstiRegionRevision=_FsStpMstiRegionRevision_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,3),_FsStpMstiRegionRevision_Type())
fsStpMstiRegionRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpMstiRegionRevision.setStatus(_A)
class _FsStpMstiMaxHopNumber_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_FsStpMstiMaxHopNumber_Type.__name__=_E
_FsStpMstiMaxHopNumber_Object=MibScalar
fsStpMstiMaxHopNumber=_FsStpMstiMaxHopNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,4),_FsStpMstiMaxHopNumber_Type())
fsStpMstiMaxHopNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpMstiMaxHopNumber.setStatus(_A)
_FsStpMstiInstanceTable_Object=MibTable
fsStpMstiInstanceTable=_FsStpMstiInstanceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5))
if mibBuilder.loadTexts:fsStpMstiInstanceTable.setStatus(_A)
_FsStpMstiInstanceEntry_Object=MibTableRow
fsStpMstiInstanceEntry=_FsStpMstiInstanceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1))
fsStpMstiInstanceEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsStpMstiInstanceEntry.setStatus(_A)
class _FsStpMstiInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_FsStpMstiInstanceIndex_Type.__name__=_E
_FsStpMstiInstanceIndex_Object=MibTableColumn
fsStpMstiInstanceIndex=_FsStpMstiInstanceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,1),_FsStpMstiInstanceIndex_Type())
fsStpMstiInstanceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiInstanceIndex.setStatus(_A)
class _FsStpMstiInstanceVlansAddMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_FsStpMstiInstanceVlansAddMapped_Type.__name__=_F
_FsStpMstiInstanceVlansAddMapped_Object=MibTableColumn
fsStpMstiInstanceVlansAddMapped=_FsStpMstiInstanceVlansAddMapped_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,2),_FsStpMstiInstanceVlansAddMapped_Type())
fsStpMstiInstanceVlansAddMapped.setMaxAccess(_H)
if mibBuilder.loadTexts:fsStpMstiInstanceVlansAddMapped.setStatus(_A)
class _FsStpMstiInstanceVlansDeleteMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_FsStpMstiInstanceVlansDeleteMapped_Type.__name__=_F
_FsStpMstiInstanceVlansDeleteMapped_Object=MibTableColumn
fsStpMstiInstanceVlansDeleteMapped=_FsStpMstiInstanceVlansDeleteMapped_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,3),_FsStpMstiInstanceVlansDeleteMapped_Type())
fsStpMstiInstanceVlansDeleteMapped.setMaxAccess(_H)
if mibBuilder.loadTexts:fsStpMstiInstanceVlansDeleteMapped.setStatus(_A)
class _FsStpMstiInstanceVlansGetMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_FsStpMstiInstanceVlansGetMapped_Type.__name__=_F
_FsStpMstiInstanceVlansGetMapped_Object=MibTableColumn
fsStpMstiInstanceVlansGetMapped=_FsStpMstiInstanceVlansGetMapped_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,4),_FsStpMstiInstanceVlansGetMapped_Type())
fsStpMstiInstanceVlansGetMapped.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiInstanceVlansGetMapped.setStatus(_A)
class _FsStpMstiInstanceRemainingHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_FsStpMstiInstanceRemainingHopCount_Type.__name__=_E
_FsStpMstiInstanceRemainingHopCount_Object=MibTableColumn
fsStpMstiInstanceRemainingHopCount=_FsStpMstiInstanceRemainingHopCount_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,5),_FsStpMstiInstanceRemainingHopCount_Type())
fsStpMstiInstanceRemainingHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiInstanceRemainingHopCount.setStatus(_A)
class _FsStpMstiPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsStpMstiPriority_Type.__name__=_E
_FsStpMstiPriority_Object=MibTableColumn
fsStpMstiPriority=_FsStpMstiPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,6),_FsStpMstiPriority_Type())
fsStpMstiPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:fsStpMstiPriority.setStatus(_A)
_FsStpMstiTimeSinceTopologyChange_Type=TimeTicks
_FsStpMstiTimeSinceTopologyChange_Object=MibTableColumn
fsStpMstiTimeSinceTopologyChange=_FsStpMstiTimeSinceTopologyChange_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,7),_FsStpMstiTimeSinceTopologyChange_Type())
fsStpMstiTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiTimeSinceTopologyChange.setStatus(_A)
_FsStpMstiTopChanges_Type=Integer32
_FsStpMstiTopChanges_Object=MibTableColumn
fsStpMstiTopChanges=_FsStpMstiTopChanges_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,8),_FsStpMstiTopChanges_Type())
fsStpMstiTopChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiTopChanges.setStatus(_A)
_FsStpMstiDesignatedRoot_Type=BridgeId
_FsStpMstiDesignatedRoot_Object=MibTableColumn
fsStpMstiDesignatedRoot=_FsStpMstiDesignatedRoot_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,9),_FsStpMstiDesignatedRoot_Type())
fsStpMstiDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiDesignatedRoot.setStatus(_A)
_FsStpMstiRootCost_Type=Integer32
_FsStpMstiRootCost_Object=MibTableColumn
fsStpMstiRootCost=_FsStpMstiRootCost_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,10),_FsStpMstiRootCost_Type())
fsStpMstiRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiRootCost.setStatus(_A)
_FsStpMstiRootPort_Type=Integer32
_FsStpMstiRootPort_Object=MibTableColumn
fsStpMstiRootPort=_FsStpMstiRootPort_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,11),_FsStpMstiRootPort_Type())
fsStpMstiRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpMstiRootPort.setStatus(_A)
_FsStpMstiInstanceEntryStatus_Type=ConfigStatus
_FsStpMstiInstanceEntryStatus_Object=MibTableColumn
fsStpMstiInstanceEntryStatus=_FsStpMstiInstanceEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,5,1,12),_FsStpMstiInstanceEntryStatus_Type())
fsStpMstiInstanceEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsStpMstiInstanceEntryStatus.setStatus(_A)
_FsStpPortMstiInstanceTable_Object=MibTable
fsStpPortMstiInstanceTable=_FsStpPortMstiInstanceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6))
if mibBuilder.loadTexts:fsStpPortMstiInstanceTable.setStatus(_A)
_FsStpPortMstiInstanceEntry_Object=MibTableRow
fsStpPortMstiInstanceEntry=_FsStpPortMstiInstanceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1))
fsStpPortMstiInstanceEntry.setIndexNames((0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:fsStpPortMstiInstanceEntry.setStatus(_A)
_FsStpPortMstiIndex_Type=Integer32
_FsStpPortMstiIndex_Object=MibTableColumn
fsStpPortMstiIndex=_FsStpPortMstiIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,1),_FsStpPortMstiIndex_Type())
fsStpPortMstiIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsStpPortMstiIndex.setStatus(_A)
class _FsStpPortMstiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6),('discard',7)))
_FsStpPortMstiState_Type.__name__=_E
_FsStpPortMstiState_Object=MibTableColumn
fsStpPortMstiState=_FsStpPortMstiState_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,2),_FsStpPortMstiState_Type())
fsStpPortMstiState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiState.setStatus(_A)
_FsStpPortMstiAdminPathCost_Type=Integer32
_FsStpPortMstiAdminPathCost_Object=MibTableColumn
fsStpPortMstiAdminPathCost=_FsStpPortMstiAdminPathCost_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,3),_FsStpPortMstiAdminPathCost_Type())
fsStpPortMstiAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortMstiAdminPathCost.setStatus(_A)
_FsStpPortMstiOperPathCost_Type=Counter32
_FsStpPortMstiOperPathCost_Object=MibTableColumn
fsStpPortMstiOperPathCost=_FsStpPortMstiOperPathCost_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,4),_FsStpPortMstiOperPathCost_Type())
fsStpPortMstiOperPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiOperPathCost.setStatus(_A)
class _FsStpPortMstiPriority_Type(Integer32):defaultValue=128
_FsStpPortMstiPriority_Type.__name__=_E
_FsStpPortMstiPriority_Object=MibTableColumn
fsStpPortMstiPriority=_FsStpPortMstiPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,5),_FsStpPortMstiPriority_Type())
fsStpPortMstiPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpPortMstiPriority.setStatus(_A)
_FsStpPortMstiDesignatedRoot_Type=BridgeId
_FsStpPortMstiDesignatedRoot_Object=MibTableColumn
fsStpPortMstiDesignatedRoot=_FsStpPortMstiDesignatedRoot_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,6),_FsStpPortMstiDesignatedRoot_Type())
fsStpPortMstiDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiDesignatedRoot.setStatus(_A)
_FsStpPortMstiDesignatedCost_Type=Integer32
_FsStpPortMstiDesignatedCost_Object=MibTableColumn
fsStpPortMstiDesignatedCost=_FsStpPortMstiDesignatedCost_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,7),_FsStpPortMstiDesignatedCost_Type())
fsStpPortMstiDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiDesignatedCost.setStatus(_A)
_FsStpPortMstiDesignatedBridge_Type=BridgeId
_FsStpPortMstiDesignatedBridge_Object=MibTableColumn
fsStpPortMstiDesignatedBridge=_FsStpPortMstiDesignatedBridge_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,8),_FsStpPortMstiDesignatedBridge_Type())
fsStpPortMstiDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiDesignatedBridge.setStatus(_A)
class _FsStpPortMstiDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsStpPortMstiDesignatedPort_Type.__name__=_F
_FsStpPortMstiDesignatedPort_Object=MibTableColumn
fsStpPortMstiDesignatedPort=_FsStpPortMstiDesignatedPort_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,9),_FsStpPortMstiDesignatedPort_Type())
fsStpPortMstiDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiDesignatedPort.setStatus(_A)
class _FsStpPortMstiPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_FsStpPortMstiPortRole_Type.__name__=_E
_FsStpPortMstiPortRole_Object=MibTableColumn
fsStpPortMstiPortRole=_FsStpPortMstiPortRole_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,10),_FsStpPortMstiPortRole_Type())
fsStpPortMstiPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiPortRole.setStatus(_A)
_FsStpPortMstiPortForwardTransitions_Type=Integer32
_FsStpPortMstiPortForwardTransitions_Object=MibTableColumn
fsStpPortMstiPortForwardTransitions=_FsStpPortMstiPortForwardTransitions_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,6,1,11),_FsStpPortMstiPortForwardTransitions_Type())
fsStpPortMstiPortForwardTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpPortMstiPortForwardTransitions.setStatus(_A)
_FsStpMstiReset_Type=Integer32
_FsStpMstiReset_Object=MibScalar
fsStpMstiReset=_FsStpMstiReset_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,7),_FsStpMstiReset_Type())
fsStpMstiReset.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpMstiReset.setStatus(_A)
_FsStpCistVlansAddMapped_Type=OctetString
_FsStpCistVlansAddMapped_Object=MibScalar
fsStpCistVlansAddMapped=_FsStpCistVlansAddMapped_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,8),_FsStpCistVlansAddMapped_Type())
fsStpCistVlansAddMapped.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStpCistVlansAddMapped.setStatus(_A)
_FsStpCistVlansGetMapped_Type=OctetString
_FsStpCistVlansGetMapped_Object=MibScalar
fsStpCistVlansGetMapped=_FsStpCistVlansGetMapped_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,9),_FsStpCistVlansGetMapped_Type())
fsStpCistVlansGetMapped.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpCistVlansGetMapped.setStatus(_A)
_FsStpCistRemainingHopCount_Type=Integer32
_FsStpCistRemainingHopCount_Object=MibScalar
fsStpCistRemainingHopCount=_FsStpCistRemainingHopCount_Object((1,3,6,1,4,1,52642,1,1,10,2,16,3,10),_FsStpCistRemainingHopCount_Type())
fsStpCistRemainingHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStpCistRemainingHopCount.setStatus(_A)
_StpExternConformance_ObjectIdentity=ObjectIdentity
stpExternConformance=_StpExternConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,4))
_StpExternGroups_ObjectIdentity=ObjectIdentity
stpExternGroups=_StpExternGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,4,1))
_RstpConformance_ObjectIdentity=ObjectIdentity
rstpConformance=_RstpConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,5))
_RstpGroups_ObjectIdentity=ObjectIdentity
rstpGroups=_RstpGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,5,1))
_RstpCompliances_ObjectIdentity=ObjectIdentity
rstpCompliances=_RstpCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,5,2))
_MstpConformance_ObjectIdentity=ObjectIdentity
mstpConformance=_MstpConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,6))
_MstpGroups_ObjectIdentity=ObjectIdentity
mstpGroups=_MstpGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,6,1))
_MstpCompliances_ObjectIdentity=ObjectIdentity
mstpCompliances=_MstpCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,16,6,2))
stpExternGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,16,4,1,1))
stpExternGroup.setObjects(*((_B,_U),(_B,_V),(_B,_I),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:stpExternGroup.setStatus(_A)
rstpBridgeGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,16,5,1,1))
rstpBridgeGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:rstpBridgeGroup.setStatus(_A)
rstpDefaultPathCostGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,16,5,1,2))
rstpDefaultPathCostGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:rstpDefaultPathCostGroup.setStatus(_A)
rstpPortGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,16,5,1,3))
rstpPortGroup.setObjects(*((_B,_J),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:rstpPortGroup.setStatus(_A)
mstpBridgeRegionGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,16,6,1,1))
mstpBridgeRegionGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:mstpBridgeRegionGroup.setStatus(_A)
mstpMstiBridgeGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,16,6,1,2))
mstpMstiBridgeGroup.setObjects(*((_B,_G),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:mstpMstiBridgeGroup.setStatus(_A)
mstpMstiPortGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,16,6,1,3))
mstpMstiPortGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:mstpMstiPortGroup.setStatus(_A)
rstpCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,16,5,2,1))
rstpCompliance.setObjects(*((_B,_AC),(_B,_K),(_B,_AD),(_B,_K)))
if mibBuilder.loadTexts:rstpCompliance.setStatus(_A)
mstpCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,16,6,2,1))
mstpCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:mstpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsStpMIB':fsStpMIB,'fsStpMIBObjects':fsStpMIBObjects,_U:fsSysStpStatus,_V:fsSysStpReset,'fsStpExtPortTable':fsStpExtPortTable,'fsStpExtPortEntry':fsStpExtPortEntry,_I:fsStpPortIfIndex,_W:fsStpPortAdminPathCost,_X:fsStpPortOperPathCost,_Y:fsStpPortRole,'fsRstpMIBObjects':fsRstpMIBObjects,_Z:fsStpVersion,_a:fsStpTxHoldCount,_d:fsStpPathCostDefault,'fsRstpExtPortTable':fsRstpExtPortTable,'fsRstpExtPortEntry':fsRstpExtPortEntry,_J:fsRstpExtPortIfIndex,_e:fsStpPortProtocolMigration,_f:fsStpPortAdminEdgePort,_g:fsStpPortOperEdgePort,_h:fsStpPortAdminPointToPoint,_i:fsStpPortOperPointToPoint,_j:fsStpPortBpduGuard,_k:fsStpPortBpduFilter,_b:fsStpBpduGuard,_c:fsStpBpduFilter,_l:fsStpCistRegionRoot,_m:fsStpCistPathCost,'fsMstpMIBObjects':fsMstpMIBObjects,_n:fsStpMstiMaxInstanceNumber,_o:fsStpMstiRegionName,_p:fsStpMstiRegionRevision,_q:fsStpMstiMaxHopNumber,'fsStpMstiInstanceTable':fsStpMstiInstanceTable,'fsStpMstiInstanceEntry':fsStpMstiInstanceEntry,_G:fsStpMstiInstanceIndex,_r:fsStpMstiInstanceVlansAddMapped,_s:fsStpMstiInstanceVlansDeleteMapped,_t:fsStpMstiInstanceVlansGetMapped,_u:fsStpMstiInstanceRemainingHopCount,_v:fsStpMstiPriority,_w:fsStpMstiTimeSinceTopologyChange,_x:fsStpMstiTopChanges,_y:fsStpMstiDesignatedRoot,_z:fsStpMstiRootCost,_A0:fsStpMstiRootPort,_A1:fsStpMstiInstanceEntryStatus,'fsStpPortMstiInstanceTable':fsStpPortMstiInstanceTable,'fsStpPortMstiInstanceEntry':fsStpPortMstiInstanceEntry,_T:fsStpPortMstiIndex,_A2:fsStpPortMstiState,_A3:fsStpPortMstiAdminPathCost,_A4:fsStpPortMstiOperPathCost,_A5:fsStpPortMstiPriority,_A6:fsStpPortMstiDesignatedRoot,_A7:fsStpPortMstiDesignatedCost,_A8:fsStpPortMstiDesignatedBridge,_A9:fsStpPortMstiDesignatedPort,_AA:fsStpPortMstiPortRole,_AB:fsStpPortMstiPortForwardTransitions,'fsStpMstiReset':fsStpMstiReset,'fsStpCistVlansAddMapped':fsStpCistVlansAddMapped,'fsStpCistVlansGetMapped':fsStpCistVlansGetMapped,'fsStpCistRemainingHopCount':fsStpCistRemainingHopCount,'stpExternConformance':stpExternConformance,'stpExternGroups':stpExternGroups,'stpExternGroup':stpExternGroup,'rstpConformance':rstpConformance,'rstpGroups':rstpGroups,_AC:rstpBridgeGroup,_K:rstpDefaultPathCostGroup,_AD:rstpPortGroup,'rstpCompliances':rstpCompliances,'rstpCompliance':rstpCompliance,'mstpConformance':mstpConformance,'mstpGroups':mstpGroups,_AE:mstpBridgeRegionGroup,_AF:mstpMstiBridgeGroup,_AG:mstpMstiPortGroup,'mstpCompliances':mstpCompliances,'mstpCompliance':mstpCompliance})