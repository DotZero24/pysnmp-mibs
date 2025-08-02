_AG='mstpMstiPortGroup'
_AF='mstpMstiBridgeGroup'
_AE='mstpBridgeRegionGroup'
_AD='rstpPortGroup'
_AC='rstpBridgeGroup'
_AB='qtechStpPortMstiPortForwardTransitions'
_AA='qtechStpPortMstiPortRole'
_A9='qtechStpPortMstiDesignatedPort'
_A8='qtechStpPortMstiDesignatedBridge'
_A7='qtechStpPortMstiDesignatedCost'
_A6='qtechStpPortMstiDesignatedRoot'
_A5='qtechStpPortMstiPriority'
_A4='qtechStpPortMstiOperPathCost'
_A3='qtechStpPortMstiAdminPathCost'
_A2='qtechStpPortMstiState'
_A1='qtechStpMstiInstanceEntryStatus'
_A0='qtechStpMstiRootPort'
_z='qtechStpMstiRootCost'
_y='qtechStpMstiDesignatedRoot'
_x='qtechStpMstiTopChanges'
_w='qtechStpMstiTimeSinceTopologyChange'
_v='qtechStpMstiPriority'
_u='qtechStpMstiInstanceRemainingHopCount'
_t='qtechStpMstiInstanceVlansGetMapped'
_s='qtechStpMstiInstanceVlansDeleteMapped'
_r='qtechStpMstiInstanceVlansAddMapped'
_q='qtechStpMstiMaxHopNumber'
_p='qtechStpMstiRegionRevision'
_o='qtechStpMstiRegionName'
_n='qtechStpMstiMaxInstanceNumber'
_m='qtechStpCistPathCost'
_l='qtechStpCistRegionRoot'
_k='qtechStpPortBpduFilter'
_j='qtechStpPortBpduGuard'
_i='qtechStpPortOperPointToPoint'
_h='qtechStpPortAdminPointToPoint'
_g='qtechStpPortOperEdgePort'
_f='qtechStpPortAdminEdgePort'
_e='qtechStpPortProtocolMigration'
_d='qtechStpPathCostDefault'
_c='qtechStpBpduFilter'
_b='qtechStpBpduGuard'
_a='qtechStpTxHoldCount'
_Z='qtechStpVersion'
_Y='qtechStpPortRole'
_X='qtechStpPortOperPathCost'
_W='qtechStpPortAdminPathCost'
_V='qtechSysStpReset'
_U='qtechSysStpStatus'
_T='qtechStpPortMstiIndex'
_S='masterPort'
_R='designatedPort'
_Q='rootPort'
_P='backupPort'
_O='alternatePort'
_N='disabledPort'
_M='DisplayString'
_L='EnabledStatus'
_K='rstpDefaultPathCostGroup'
_J='qtechRstpExtPortIfIndex'
_I='qtechStpPortIfIndex'
_H='read-create'
_G='qtechStpMstiInstanceIndex'
_F='OctetString'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='QTECH-RSTP-MSTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_L)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention','TruthValue')
qtechStpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,16))
if mibBuilder.loadTexts:qtechStpMIB.setRevisions(('2002-03-20 00:00',))
_QtechStpMIBObjects_ObjectIdentity=ObjectIdentity
qtechStpMIBObjects=_QtechStpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,1))
class _QtechSysStpStatus_Type(EnabledStatus):defaultValue=2
_QtechSysStpStatus_Type.__name__=_L
_QtechSysStpStatus_Object=MibScalar
qtechSysStpStatus=_QtechSysStpStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,1),_QtechSysStpStatus_Type())
qtechSysStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSysStpStatus.setStatus(_A)
_QtechSysStpReset_Type=Integer32
_QtechSysStpReset_Object=MibScalar
qtechSysStpReset=_QtechSysStpReset_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,2),_QtechSysStpReset_Type())
qtechSysStpReset.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSysStpReset.setStatus(_A)
_QtechStpExtPortTable_Object=MibTable
qtechStpExtPortTable=_QtechStpExtPortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,3))
if mibBuilder.loadTexts:qtechStpExtPortTable.setStatus(_A)
_QtechStpExtPortEntry_Object=MibTableRow
qtechStpExtPortEntry=_QtechStpExtPortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,3,1))
qtechStpExtPortEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechStpExtPortEntry.setStatus(_A)
_QtechStpPortIfIndex_Type=IfIndex
_QtechStpPortIfIndex_Object=MibTableColumn
qtechStpPortIfIndex=_QtechStpPortIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,3,1,1),_QtechStpPortIfIndex_Type())
qtechStpPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortIfIndex.setStatus(_A)
class _QtechStpPortAdminPathCost_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_QtechStpPortAdminPathCost_Type.__name__=_E
_QtechStpPortAdminPathCost_Object=MibTableColumn
qtechStpPortAdminPathCost=_QtechStpPortAdminPathCost_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,3,1,2),_QtechStpPortAdminPathCost_Type())
qtechStpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortAdminPathCost.setStatus(_A)
class _QtechStpPortOperPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_QtechStpPortOperPathCost_Type.__name__=_E
_QtechStpPortOperPathCost_Object=MibTableColumn
qtechStpPortOperPathCost=_QtechStpPortOperPathCost_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,3,1,3),_QtechStpPortOperPathCost_Type())
qtechStpPortOperPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortOperPathCost.setStatus(_A)
class _QtechStpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_QtechStpPortRole_Type.__name__=_E
_QtechStpPortRole_Object=MibTableColumn
qtechStpPortRole=_QtechStpPortRole_Object((1,3,6,1,4,1,27514,1,1,10,2,16,1,3,1,4),_QtechStpPortRole_Type())
qtechStpPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortRole.setStatus(_A)
_QtechRstpMIBObjects_ObjectIdentity=ObjectIdentity
qtechRstpMIBObjects=_QtechRstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,2))
class _QtechStpVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2),('mstp',3)))
_QtechStpVersion_Type.__name__=_E
_QtechStpVersion_Object=MibScalar
qtechStpVersion=_QtechStpVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,1),_QtechStpVersion_Type())
qtechStpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpVersion.setStatus(_A)
class _QtechStpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_QtechStpTxHoldCount_Type.__name__=_E
_QtechStpTxHoldCount_Object=MibScalar
qtechStpTxHoldCount=_QtechStpTxHoldCount_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,2),_QtechStpTxHoldCount_Type())
qtechStpTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpTxHoldCount.setStatus(_A)
class _QtechStpPathCostDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_QtechStpPathCostDefault_Type.__name__=_E
_QtechStpPathCostDefault_Object=MibScalar
qtechStpPathCostDefault=_QtechStpPathCostDefault_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,3),_QtechStpPathCostDefault_Type())
qtechStpPathCostDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPathCostDefault.setStatus(_A)
_QtechRstpExtPortTable_Object=MibTable
qtechRstpExtPortTable=_QtechRstpExtPortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4))
if mibBuilder.loadTexts:qtechRstpExtPortTable.setStatus(_A)
_QtechRstpExtPortEntry_Object=MibTableRow
qtechRstpExtPortEntry=_QtechRstpExtPortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1))
qtechRstpExtPortEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechRstpExtPortEntry.setStatus(_A)
_QtechRstpExtPortIfIndex_Type=IfIndex
_QtechRstpExtPortIfIndex_Object=MibTableColumn
qtechRstpExtPortIfIndex=_QtechRstpExtPortIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,1),_QtechRstpExtPortIfIndex_Type())
qtechRstpExtPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRstpExtPortIfIndex.setStatus(_A)
_QtechStpPortProtocolMigration_Type=TruthValue
_QtechStpPortProtocolMigration_Object=MibTableColumn
qtechStpPortProtocolMigration=_QtechStpPortProtocolMigration_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,2),_QtechStpPortProtocolMigration_Type())
qtechStpPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortProtocolMigration.setStatus(_A)
_QtechStpPortAdminEdgePort_Type=TruthValue
_QtechStpPortAdminEdgePort_Object=MibTableColumn
qtechStpPortAdminEdgePort=_QtechStpPortAdminEdgePort_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,3),_QtechStpPortAdminEdgePort_Type())
qtechStpPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortAdminEdgePort.setStatus(_A)
_QtechStpPortOperEdgePort_Type=TruthValue
_QtechStpPortOperEdgePort_Object=MibTableColumn
qtechStpPortOperEdgePort=_QtechStpPortOperEdgePort_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,4),_QtechStpPortOperEdgePort_Type())
qtechStpPortOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortOperEdgePort.setStatus(_A)
class _QtechStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_QtechStpPortAdminPointToPoint_Type.__name__=_E
_QtechStpPortAdminPointToPoint_Object=MibTableColumn
qtechStpPortAdminPointToPoint=_QtechStpPortAdminPointToPoint_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,5),_QtechStpPortAdminPointToPoint_Type())
qtechStpPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortAdminPointToPoint.setStatus(_A)
_QtechStpPortOperPointToPoint_Type=TruthValue
_QtechStpPortOperPointToPoint_Object=MibTableColumn
qtechStpPortOperPointToPoint=_QtechStpPortOperPointToPoint_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,6),_QtechStpPortOperPointToPoint_Type())
qtechStpPortOperPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortOperPointToPoint.setStatus(_A)
_QtechStpPortBpduGuard_Type=EnabledStatus
_QtechStpPortBpduGuard_Object=MibTableColumn
qtechStpPortBpduGuard=_QtechStpPortBpduGuard_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,7),_QtechStpPortBpduGuard_Type())
qtechStpPortBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortBpduGuard.setStatus(_A)
_QtechStpPortBpduFilter_Type=EnabledStatus
_QtechStpPortBpduFilter_Object=MibTableColumn
qtechStpPortBpduFilter=_QtechStpPortBpduFilter_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,4,1,8),_QtechStpPortBpduFilter_Type())
qtechStpPortBpduFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortBpduFilter.setStatus(_A)
_QtechStpBpduGuard_Type=EnabledStatus
_QtechStpBpduGuard_Object=MibScalar
qtechStpBpduGuard=_QtechStpBpduGuard_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,5),_QtechStpBpduGuard_Type())
qtechStpBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpBpduGuard.setStatus(_A)
_QtechStpBpduFilter_Type=EnabledStatus
_QtechStpBpduFilter_Object=MibScalar
qtechStpBpduFilter=_QtechStpBpduFilter_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,6),_QtechStpBpduFilter_Type())
qtechStpBpduFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpBpduFilter.setStatus(_A)
_QtechStpCistRegionRoot_Type=BridgeId
_QtechStpCistRegionRoot_Object=MibScalar
qtechStpCistRegionRoot=_QtechStpCistRegionRoot_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,7),_QtechStpCistRegionRoot_Type())
qtechStpCistRegionRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpCistRegionRoot.setStatus(_A)
_QtechStpCistPathCost_Type=Integer32
_QtechStpCistPathCost_Object=MibScalar
qtechStpCistPathCost=_QtechStpCistPathCost_Object((1,3,6,1,4,1,27514,1,1,10,2,16,2,8),_QtechStpCistPathCost_Type())
qtechStpCistPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpCistPathCost.setStatus(_A)
_QtechMstpMIBObjects_ObjectIdentity=ObjectIdentity
qtechMstpMIBObjects=_QtechMstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,3))
_QtechStpMstiMaxInstanceNumber_Type=Integer32
_QtechStpMstiMaxInstanceNumber_Object=MibScalar
qtechStpMstiMaxInstanceNumber=_QtechStpMstiMaxInstanceNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,1),_QtechStpMstiMaxInstanceNumber_Type())
qtechStpMstiMaxInstanceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiMaxInstanceNumber.setStatus(_A)
class _QtechStpMstiRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechStpMstiRegionName_Type.__name__=_M
_QtechStpMstiRegionName_Object=MibScalar
qtechStpMstiRegionName=_QtechStpMstiRegionName_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,2),_QtechStpMstiRegionName_Type())
qtechStpMstiRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpMstiRegionName.setStatus(_A)
class _QtechStpMstiRegionRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechStpMstiRegionRevision_Type.__name__=_E
_QtechStpMstiRegionRevision_Object=MibScalar
qtechStpMstiRegionRevision=_QtechStpMstiRegionRevision_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,3),_QtechStpMstiRegionRevision_Type())
qtechStpMstiRegionRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpMstiRegionRevision.setStatus(_A)
class _QtechStpMstiMaxHopNumber_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_QtechStpMstiMaxHopNumber_Type.__name__=_E
_QtechStpMstiMaxHopNumber_Object=MibScalar
qtechStpMstiMaxHopNumber=_QtechStpMstiMaxHopNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,4),_QtechStpMstiMaxHopNumber_Type())
qtechStpMstiMaxHopNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpMstiMaxHopNumber.setStatus(_A)
_QtechStpMstiInstanceTable_Object=MibTable
qtechStpMstiInstanceTable=_QtechStpMstiInstanceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5))
if mibBuilder.loadTexts:qtechStpMstiInstanceTable.setStatus(_A)
_QtechStpMstiInstanceEntry_Object=MibTableRow
qtechStpMstiInstanceEntry=_QtechStpMstiInstanceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1))
qtechStpMstiInstanceEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechStpMstiInstanceEntry.setStatus(_A)
class _QtechStpMstiInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_QtechStpMstiInstanceIndex_Type.__name__=_E
_QtechStpMstiInstanceIndex_Object=MibTableColumn
qtechStpMstiInstanceIndex=_QtechStpMstiInstanceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,1),_QtechStpMstiInstanceIndex_Type())
qtechStpMstiInstanceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiInstanceIndex.setStatus(_A)
class _QtechStpMstiInstanceVlansAddMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_QtechStpMstiInstanceVlansAddMapped_Type.__name__=_F
_QtechStpMstiInstanceVlansAddMapped_Object=MibTableColumn
qtechStpMstiInstanceVlansAddMapped=_QtechStpMstiInstanceVlansAddMapped_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,2),_QtechStpMstiInstanceVlansAddMapped_Type())
qtechStpMstiInstanceVlansAddMapped.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechStpMstiInstanceVlansAddMapped.setStatus(_A)
class _QtechStpMstiInstanceVlansDeleteMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_QtechStpMstiInstanceVlansDeleteMapped_Type.__name__=_F
_QtechStpMstiInstanceVlansDeleteMapped_Object=MibTableColumn
qtechStpMstiInstanceVlansDeleteMapped=_QtechStpMstiInstanceVlansDeleteMapped_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,3),_QtechStpMstiInstanceVlansDeleteMapped_Type())
qtechStpMstiInstanceVlansDeleteMapped.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechStpMstiInstanceVlansDeleteMapped.setStatus(_A)
class _QtechStpMstiInstanceVlansGetMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_QtechStpMstiInstanceVlansGetMapped_Type.__name__=_F
_QtechStpMstiInstanceVlansGetMapped_Object=MibTableColumn
qtechStpMstiInstanceVlansGetMapped=_QtechStpMstiInstanceVlansGetMapped_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,4),_QtechStpMstiInstanceVlansGetMapped_Type())
qtechStpMstiInstanceVlansGetMapped.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiInstanceVlansGetMapped.setStatus(_A)
class _QtechStpMstiInstanceRemainingHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_QtechStpMstiInstanceRemainingHopCount_Type.__name__=_E
_QtechStpMstiInstanceRemainingHopCount_Object=MibTableColumn
qtechStpMstiInstanceRemainingHopCount=_QtechStpMstiInstanceRemainingHopCount_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,5),_QtechStpMstiInstanceRemainingHopCount_Type())
qtechStpMstiInstanceRemainingHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiInstanceRemainingHopCount.setStatus(_A)
class _QtechStpMstiPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechStpMstiPriority_Type.__name__=_E
_QtechStpMstiPriority_Object=MibTableColumn
qtechStpMstiPriority=_QtechStpMstiPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,6),_QtechStpMstiPriority_Type())
qtechStpMstiPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechStpMstiPriority.setStatus(_A)
_QtechStpMstiTimeSinceTopologyChange_Type=TimeTicks
_QtechStpMstiTimeSinceTopologyChange_Object=MibTableColumn
qtechStpMstiTimeSinceTopologyChange=_QtechStpMstiTimeSinceTopologyChange_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,7),_QtechStpMstiTimeSinceTopologyChange_Type())
qtechStpMstiTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiTimeSinceTopologyChange.setStatus(_A)
_QtechStpMstiTopChanges_Type=Integer32
_QtechStpMstiTopChanges_Object=MibTableColumn
qtechStpMstiTopChanges=_QtechStpMstiTopChanges_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,8),_QtechStpMstiTopChanges_Type())
qtechStpMstiTopChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiTopChanges.setStatus(_A)
_QtechStpMstiDesignatedRoot_Type=BridgeId
_QtechStpMstiDesignatedRoot_Object=MibTableColumn
qtechStpMstiDesignatedRoot=_QtechStpMstiDesignatedRoot_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,9),_QtechStpMstiDesignatedRoot_Type())
qtechStpMstiDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiDesignatedRoot.setStatus(_A)
_QtechStpMstiRootCost_Type=Integer32
_QtechStpMstiRootCost_Object=MibTableColumn
qtechStpMstiRootCost=_QtechStpMstiRootCost_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,10),_QtechStpMstiRootCost_Type())
qtechStpMstiRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiRootCost.setStatus(_A)
_QtechStpMstiRootPort_Type=Integer32
_QtechStpMstiRootPort_Object=MibTableColumn
qtechStpMstiRootPort=_QtechStpMstiRootPort_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,11),_QtechStpMstiRootPort_Type())
qtechStpMstiRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpMstiRootPort.setStatus(_A)
_QtechStpMstiInstanceEntryStatus_Type=ConfigStatus
_QtechStpMstiInstanceEntryStatus_Object=MibTableColumn
qtechStpMstiInstanceEntryStatus=_QtechStpMstiInstanceEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,5,1,12),_QtechStpMstiInstanceEntryStatus_Type())
qtechStpMstiInstanceEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechStpMstiInstanceEntryStatus.setStatus(_A)
_QtechStpPortMstiInstanceTable_Object=MibTable
qtechStpPortMstiInstanceTable=_QtechStpPortMstiInstanceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6))
if mibBuilder.loadTexts:qtechStpPortMstiInstanceTable.setStatus(_A)
_QtechStpPortMstiInstanceEntry_Object=MibTableRow
qtechStpPortMstiInstanceEntry=_QtechStpPortMstiInstanceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1))
qtechStpPortMstiInstanceEntry.setIndexNames((0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:qtechStpPortMstiInstanceEntry.setStatus(_A)
_QtechStpPortMstiIndex_Type=Integer32
_QtechStpPortMstiIndex_Object=MibTableColumn
qtechStpPortMstiIndex=_QtechStpPortMstiIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,1),_QtechStpPortMstiIndex_Type())
qtechStpPortMstiIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechStpPortMstiIndex.setStatus(_A)
class _QtechStpPortMstiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6),('discard',7)))
_QtechStpPortMstiState_Type.__name__=_E
_QtechStpPortMstiState_Object=MibTableColumn
qtechStpPortMstiState=_QtechStpPortMstiState_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,2),_QtechStpPortMstiState_Type())
qtechStpPortMstiState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiState.setStatus(_A)
_QtechStpPortMstiAdminPathCost_Type=Integer32
_QtechStpPortMstiAdminPathCost_Object=MibTableColumn
qtechStpPortMstiAdminPathCost=_QtechStpPortMstiAdminPathCost_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,3),_QtechStpPortMstiAdminPathCost_Type())
qtechStpPortMstiAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortMstiAdminPathCost.setStatus(_A)
_QtechStpPortMstiOperPathCost_Type=Counter32
_QtechStpPortMstiOperPathCost_Object=MibTableColumn
qtechStpPortMstiOperPathCost=_QtechStpPortMstiOperPathCost_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,4),_QtechStpPortMstiOperPathCost_Type())
qtechStpPortMstiOperPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiOperPathCost.setStatus(_A)
class _QtechStpPortMstiPriority_Type(Integer32):defaultValue=128
_QtechStpPortMstiPriority_Type.__name__=_E
_QtechStpPortMstiPriority_Object=MibTableColumn
qtechStpPortMstiPriority=_QtechStpPortMstiPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,5),_QtechStpPortMstiPriority_Type())
qtechStpPortMstiPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpPortMstiPriority.setStatus(_A)
_QtechStpPortMstiDesignatedRoot_Type=BridgeId
_QtechStpPortMstiDesignatedRoot_Object=MibTableColumn
qtechStpPortMstiDesignatedRoot=_QtechStpPortMstiDesignatedRoot_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,6),_QtechStpPortMstiDesignatedRoot_Type())
qtechStpPortMstiDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiDesignatedRoot.setStatus(_A)
_QtechStpPortMstiDesignatedCost_Type=Integer32
_QtechStpPortMstiDesignatedCost_Object=MibTableColumn
qtechStpPortMstiDesignatedCost=_QtechStpPortMstiDesignatedCost_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,7),_QtechStpPortMstiDesignatedCost_Type())
qtechStpPortMstiDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiDesignatedCost.setStatus(_A)
_QtechStpPortMstiDesignatedBridge_Type=BridgeId
_QtechStpPortMstiDesignatedBridge_Object=MibTableColumn
qtechStpPortMstiDesignatedBridge=_QtechStpPortMstiDesignatedBridge_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,8),_QtechStpPortMstiDesignatedBridge_Type())
qtechStpPortMstiDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiDesignatedBridge.setStatus(_A)
class _QtechStpPortMstiDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_QtechStpPortMstiDesignatedPort_Type.__name__=_F
_QtechStpPortMstiDesignatedPort_Object=MibTableColumn
qtechStpPortMstiDesignatedPort=_QtechStpPortMstiDesignatedPort_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,9),_QtechStpPortMstiDesignatedPort_Type())
qtechStpPortMstiDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiDesignatedPort.setStatus(_A)
class _QtechStpPortMstiPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_QtechStpPortMstiPortRole_Type.__name__=_E
_QtechStpPortMstiPortRole_Object=MibTableColumn
qtechStpPortMstiPortRole=_QtechStpPortMstiPortRole_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,10),_QtechStpPortMstiPortRole_Type())
qtechStpPortMstiPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiPortRole.setStatus(_A)
_QtechStpPortMstiPortForwardTransitions_Type=Integer32
_QtechStpPortMstiPortForwardTransitions_Object=MibTableColumn
qtechStpPortMstiPortForwardTransitions=_QtechStpPortMstiPortForwardTransitions_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,6,1,11),_QtechStpPortMstiPortForwardTransitions_Type())
qtechStpPortMstiPortForwardTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpPortMstiPortForwardTransitions.setStatus(_A)
_QtechStpMstiReset_Type=Integer32
_QtechStpMstiReset_Object=MibScalar
qtechStpMstiReset=_QtechStpMstiReset_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,7),_QtechStpMstiReset_Type())
qtechStpMstiReset.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpMstiReset.setStatus(_A)
_QtechStpCistVlansAddMapped_Type=OctetString
_QtechStpCistVlansAddMapped_Object=MibScalar
qtechStpCistVlansAddMapped=_QtechStpCistVlansAddMapped_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,8),_QtechStpCistVlansAddMapped_Type())
qtechStpCistVlansAddMapped.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStpCistVlansAddMapped.setStatus(_A)
_QtechStpCistVlansGetMapped_Type=OctetString
_QtechStpCistVlansGetMapped_Object=MibScalar
qtechStpCistVlansGetMapped=_QtechStpCistVlansGetMapped_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,9),_QtechStpCistVlansGetMapped_Type())
qtechStpCistVlansGetMapped.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpCistVlansGetMapped.setStatus(_A)
_QtechStpCistRemainingHopCount_Type=Integer32
_QtechStpCistRemainingHopCount_Object=MibScalar
qtechStpCistRemainingHopCount=_QtechStpCistRemainingHopCount_Object((1,3,6,1,4,1,27514,1,1,10,2,16,3,10),_QtechStpCistRemainingHopCount_Type())
qtechStpCistRemainingHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStpCistRemainingHopCount.setStatus(_A)
_StpExternConformance_ObjectIdentity=ObjectIdentity
stpExternConformance=_StpExternConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,4))
_StpExternGroups_ObjectIdentity=ObjectIdentity
stpExternGroups=_StpExternGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,4,1))
_RstpConformance_ObjectIdentity=ObjectIdentity
rstpConformance=_RstpConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,5))
_RstpGroups_ObjectIdentity=ObjectIdentity
rstpGroups=_RstpGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,5,1))
_RstpCompliances_ObjectIdentity=ObjectIdentity
rstpCompliances=_RstpCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,5,2))
_MstpConformance_ObjectIdentity=ObjectIdentity
mstpConformance=_MstpConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,6))
_MstpGroups_ObjectIdentity=ObjectIdentity
mstpGroups=_MstpGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,6,1))
_MstpCompliances_ObjectIdentity=ObjectIdentity
mstpCompliances=_MstpCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,16,6,2))
stpExternGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,16,4,1,1))
stpExternGroup.setObjects(*((_B,_U),(_B,_V),(_B,_I),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:stpExternGroup.setStatus(_A)
rstpBridgeGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,16,5,1,1))
rstpBridgeGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:rstpBridgeGroup.setStatus(_A)
rstpDefaultPathCostGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,16,5,1,2))
rstpDefaultPathCostGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:rstpDefaultPathCostGroup.setStatus(_A)
rstpPortGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,16,5,1,3))
rstpPortGroup.setObjects(*((_B,_J),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:rstpPortGroup.setStatus(_A)
mstpBridgeRegionGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,16,6,1,1))
mstpBridgeRegionGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:mstpBridgeRegionGroup.setStatus(_A)
mstpMstiBridgeGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,16,6,1,2))
mstpMstiBridgeGroup.setObjects(*((_B,_G),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:mstpMstiBridgeGroup.setStatus(_A)
mstpMstiPortGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,16,6,1,3))
mstpMstiPortGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:mstpMstiPortGroup.setStatus(_A)
rstpCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,16,5,2,1))
rstpCompliance.setObjects(*((_B,_AC),(_B,_K),(_B,_AD),(_B,_K)))
if mibBuilder.loadTexts:rstpCompliance.setStatus(_A)
mstpCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,16,6,2,1))
mstpCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:mstpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechStpMIB':qtechStpMIB,'qtechStpMIBObjects':qtechStpMIBObjects,_U:qtechSysStpStatus,_V:qtechSysStpReset,'qtechStpExtPortTable':qtechStpExtPortTable,'qtechStpExtPortEntry':qtechStpExtPortEntry,_I:qtechStpPortIfIndex,_W:qtechStpPortAdminPathCost,_X:qtechStpPortOperPathCost,_Y:qtechStpPortRole,'qtechRstpMIBObjects':qtechRstpMIBObjects,_Z:qtechStpVersion,_a:qtechStpTxHoldCount,_d:qtechStpPathCostDefault,'qtechRstpExtPortTable':qtechRstpExtPortTable,'qtechRstpExtPortEntry':qtechRstpExtPortEntry,_J:qtechRstpExtPortIfIndex,_e:qtechStpPortProtocolMigration,_f:qtechStpPortAdminEdgePort,_g:qtechStpPortOperEdgePort,_h:qtechStpPortAdminPointToPoint,_i:qtechStpPortOperPointToPoint,_j:qtechStpPortBpduGuard,_k:qtechStpPortBpduFilter,_b:qtechStpBpduGuard,_c:qtechStpBpduFilter,_l:qtechStpCistRegionRoot,_m:qtechStpCistPathCost,'qtechMstpMIBObjects':qtechMstpMIBObjects,_n:qtechStpMstiMaxInstanceNumber,_o:qtechStpMstiRegionName,_p:qtechStpMstiRegionRevision,_q:qtechStpMstiMaxHopNumber,'qtechStpMstiInstanceTable':qtechStpMstiInstanceTable,'qtechStpMstiInstanceEntry':qtechStpMstiInstanceEntry,_G:qtechStpMstiInstanceIndex,_r:qtechStpMstiInstanceVlansAddMapped,_s:qtechStpMstiInstanceVlansDeleteMapped,_t:qtechStpMstiInstanceVlansGetMapped,_u:qtechStpMstiInstanceRemainingHopCount,_v:qtechStpMstiPriority,_w:qtechStpMstiTimeSinceTopologyChange,_x:qtechStpMstiTopChanges,_y:qtechStpMstiDesignatedRoot,_z:qtechStpMstiRootCost,_A0:qtechStpMstiRootPort,_A1:qtechStpMstiInstanceEntryStatus,'qtechStpPortMstiInstanceTable':qtechStpPortMstiInstanceTable,'qtechStpPortMstiInstanceEntry':qtechStpPortMstiInstanceEntry,_T:qtechStpPortMstiIndex,_A2:qtechStpPortMstiState,_A3:qtechStpPortMstiAdminPathCost,_A4:qtechStpPortMstiOperPathCost,_A5:qtechStpPortMstiPriority,_A6:qtechStpPortMstiDesignatedRoot,_A7:qtechStpPortMstiDesignatedCost,_A8:qtechStpPortMstiDesignatedBridge,_A9:qtechStpPortMstiDesignatedPort,_AA:qtechStpPortMstiPortRole,_AB:qtechStpPortMstiPortForwardTransitions,'qtechStpMstiReset':qtechStpMstiReset,'qtechStpCistVlansAddMapped':qtechStpCistVlansAddMapped,'qtechStpCistVlansGetMapped':qtechStpCistVlansGetMapped,'qtechStpCistRemainingHopCount':qtechStpCistRemainingHopCount,'stpExternConformance':stpExternConformance,'stpExternGroups':stpExternGroups,'stpExternGroup':stpExternGroup,'rstpConformance':rstpConformance,'rstpGroups':rstpGroups,_AC:rstpBridgeGroup,_K:rstpDefaultPathCostGroup,_AD:rstpPortGroup,'rstpCompliances':rstpCompliances,'rstpCompliance':rstpCompliance,'mstpConformance':mstpConformance,'mstpGroups':mstpGroups,_AE:mstpBridgeRegionGroup,_AF:mstpMstiBridgeGroup,_AG:mstpMstiPortGroup,'mstpCompliances':mstpCompliances,'mstpCompliance':mstpCompliance})