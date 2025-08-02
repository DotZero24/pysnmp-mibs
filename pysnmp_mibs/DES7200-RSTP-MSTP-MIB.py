_AG='mstpMstiPortGroup'
_AF='mstpMstiBridgeGroup'
_AE='mstpBridgeRegionGroup'
_AD='rstpPortGroup'
_AC='rstpBridgeGroup'
_AB='myStpPortMstiPortForwardTransitions'
_AA='myStpPortMstiPortRole'
_A9='myStpPortMstiDesignatedPort'
_A8='myStpPortMstiDesignatedBridge'
_A7='myStpPortMstiDesignatedCost'
_A6='myStpPortMstiDesignatedRoot'
_A5='myStpPortMstiPriority'
_A4='myStpPortMstiOperPathCost'
_A3='myStpPortMstiAdminPathCost'
_A2='myStpPortMstiState'
_A1='myStpMstiInstanceEntryStatus'
_A0='myStpMstiRootPort'
_z='myStpMstiRootCost'
_y='myStpMstiDesignatedRoot'
_x='myStpMstiTopChanges'
_w='myStpMstiTimeSinceTopologyChange'
_v='myStpMstiPriority'
_u='myStpMstiInstanceRemainingHopCount'
_t='myStpMstiInstanceVlansGetMapped'
_s='myStpMstiInstanceVlansDeleteMapped'
_r='myStpMstiInstanceVlansAddMapped'
_q='myStpMstiMaxHopNumber'
_p='myStpMstiRegionRevision'
_o='myStpMstiRegionName'
_n='myStpMstiMaxInstanceNumber'
_m='myStpCistPathCost'
_l='myStpCistRegionRoot'
_k='myStpPortBpduFilter'
_j='myStpPortBpduGuard'
_i='myStpPortOperPointToPoint'
_h='myStpPortAdminPointToPoint'
_g='myStpPortOperEdgePort'
_f='myStpPortAdminEdgePort'
_e='myStpPortProtocolMigration'
_d='myStpPathCostDefault'
_c='myStpBpduFilter'
_b='myStpBpduGuard'
_a='myStpTxHoldCount'
_Z='myStpVersion'
_Y='myStpPortRole'
_X='myStpPortOperPathCost'
_W='myStpPortAdminPathCost'
_V='mySysStpReset'
_U='mySysStpStatus'
_T='masterPort'
_S='designatedPort'
_R='rootPort'
_Q='backupPort'
_P='alternatePort'
_O='disabledPort'
_N='DisplayString'
_M='EnabledStatus'
_L='rstpDefaultPathCostGroup'
_K='myStpPortMstiIndex'
_J='myRstpExtPortIfIndex'
_I='myStpPortIfIndex'
_H='myStpMstiInstanceIndex'
_G='mandatory'
_F='OctetString'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='DES7200-RSTP-MSTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,dot1dBridge,dot1dStp,dot1dStpPortEntry=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId','dot1dBridge','dot1dStp','dot1dStpPortEntry')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_M)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myStpMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,16))
if mibBuilder.loadTexts:myStpMIB.setRevisions(('2002-03-20 00:00',))
_MyStpMIBObjects_ObjectIdentity=ObjectIdentity
myStpMIBObjects=_MyStpMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,1))
class _MySysStpStatus_Type(EnabledStatus):defaultValue=2
_MySysStpStatus_Type.__name__=_M
_MySysStpStatus_Object=MibScalar
mySysStpStatus=_MySysStpStatus_Object((1,3,6,1,4,1,171,10,97,2,16,1,1),_MySysStpStatus_Type())
mySysStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mySysStpStatus.setStatus(_A)
_MySysStpReset_Type=Integer32
_MySysStpReset_Object=MibScalar
mySysStpReset=_MySysStpReset_Object((1,3,6,1,4,1,171,10,97,2,16,1,2),_MySysStpReset_Type())
mySysStpReset.setMaxAccess(_D)
if mibBuilder.loadTexts:mySysStpReset.setStatus(_A)
_MyStpExtPortTable_Object=MibTable
myStpExtPortTable=_MyStpExtPortTable_Object((1,3,6,1,4,1,171,10,97,2,16,1,3))
if mibBuilder.loadTexts:myStpExtPortTable.setStatus(_A)
_MyStpExtPortEntry_Object=MibTableRow
myStpExtPortEntry=_MyStpExtPortEntry_Object((1,3,6,1,4,1,171,10,97,2,16,1,3,1))
myStpExtPortEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:myStpExtPortEntry.setStatus(_A)
_MyStpPortIfIndex_Type=IfIndex
_MyStpPortIfIndex_Object=MibTableColumn
myStpPortIfIndex=_MyStpPortIfIndex_Object((1,3,6,1,4,1,171,10,97,2,16,1,3,1,1),_MyStpPortIfIndex_Type())
myStpPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortIfIndex.setStatus(_A)
class _MyStpPortAdminPathCost_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_MyStpPortAdminPathCost_Type.__name__=_E
_MyStpPortAdminPathCost_Object=MibTableColumn
myStpPortAdminPathCost=_MyStpPortAdminPathCost_Object((1,3,6,1,4,1,171,10,97,2,16,1,3,1,2),_MyStpPortAdminPathCost_Type())
myStpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortAdminPathCost.setStatus(_A)
class _MyStpPortOperPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_MyStpPortOperPathCost_Type.__name__=_E
_MyStpPortOperPathCost_Object=MibTableColumn
myStpPortOperPathCost=_MyStpPortOperPathCost_Object((1,3,6,1,4,1,171,10,97,2,16,1,3,1,3),_MyStpPortOperPathCost_Type())
myStpPortOperPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortOperPathCost.setStatus(_A)
class _MyStpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_MyStpPortRole_Type.__name__=_E
_MyStpPortRole_Object=MibTableColumn
myStpPortRole=_MyStpPortRole_Object((1,3,6,1,4,1,171,10,97,2,16,1,3,1,4),_MyStpPortRole_Type())
myStpPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortRole.setStatus(_A)
_MyRstpMIBObjects_ObjectIdentity=ObjectIdentity
myRstpMIBObjects=_MyRstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,2))
class _MyStpVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2),('mstp',3)))
_MyStpVersion_Type.__name__=_E
_MyStpVersion_Object=MibScalar
myStpVersion=_MyStpVersion_Object((1,3,6,1,4,1,171,10,97,2,16,2,1),_MyStpVersion_Type())
myStpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpVersion.setStatus(_A)
class _MyStpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MyStpTxHoldCount_Type.__name__=_E
_MyStpTxHoldCount_Object=MibScalar
myStpTxHoldCount=_MyStpTxHoldCount_Object((1,3,6,1,4,1,171,10,97,2,16,2,2),_MyStpTxHoldCount_Type())
myStpTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpTxHoldCount.setStatus(_A)
class _MyStpPathCostDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_MyStpPathCostDefault_Type.__name__=_E
_MyStpPathCostDefault_Object=MibScalar
myStpPathCostDefault=_MyStpPathCostDefault_Object((1,3,6,1,4,1,171,10,97,2,16,2,3),_MyStpPathCostDefault_Type())
myStpPathCostDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPathCostDefault.setStatus(_A)
_MyRstpExtPortTable_Object=MibTable
myRstpExtPortTable=_MyRstpExtPortTable_Object((1,3,6,1,4,1,171,10,97,2,16,2,4))
if mibBuilder.loadTexts:myRstpExtPortTable.setStatus(_A)
_MyRstpExtPortEntry_Object=MibTableRow
myRstpExtPortEntry=_MyRstpExtPortEntry_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1))
myRstpExtPortEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:myRstpExtPortEntry.setStatus(_A)
_MyRstpExtPortIfIndex_Type=IfIndex
_MyRstpExtPortIfIndex_Object=MibTableColumn
myRstpExtPortIfIndex=_MyRstpExtPortIfIndex_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,1),_MyRstpExtPortIfIndex_Type())
myRstpExtPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myRstpExtPortIfIndex.setStatus(_A)
_MyStpPortProtocolMigration_Type=TruthValue
_MyStpPortProtocolMigration_Object=MibTableColumn
myStpPortProtocolMigration=_MyStpPortProtocolMigration_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,2),_MyStpPortProtocolMigration_Type())
myStpPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortProtocolMigration.setStatus(_A)
_MyStpPortAdminEdgePort_Type=TruthValue
_MyStpPortAdminEdgePort_Object=MibTableColumn
myStpPortAdminEdgePort=_MyStpPortAdminEdgePort_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,3),_MyStpPortAdminEdgePort_Type())
myStpPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortAdminEdgePort.setStatus(_A)
_MyStpPortOperEdgePort_Type=TruthValue
_MyStpPortOperEdgePort_Object=MibTableColumn
myStpPortOperEdgePort=_MyStpPortOperEdgePort_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,4),_MyStpPortOperEdgePort_Type())
myStpPortOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortOperEdgePort.setStatus(_A)
class _MyStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_MyStpPortAdminPointToPoint_Type.__name__=_E
_MyStpPortAdminPointToPoint_Object=MibTableColumn
myStpPortAdminPointToPoint=_MyStpPortAdminPointToPoint_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,5),_MyStpPortAdminPointToPoint_Type())
myStpPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortAdminPointToPoint.setStatus(_A)
_MyStpPortOperPointToPoint_Type=TruthValue
_MyStpPortOperPointToPoint_Object=MibTableColumn
myStpPortOperPointToPoint=_MyStpPortOperPointToPoint_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,6),_MyStpPortOperPointToPoint_Type())
myStpPortOperPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortOperPointToPoint.setStatus(_A)
_MyStpPortBpduGuard_Type=EnabledStatus
_MyStpPortBpduGuard_Object=MibTableColumn
myStpPortBpduGuard=_MyStpPortBpduGuard_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,7),_MyStpPortBpduGuard_Type())
myStpPortBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortBpduGuard.setStatus(_A)
_MyStpPortBpduFilter_Type=EnabledStatus
_MyStpPortBpduFilter_Object=MibTableColumn
myStpPortBpduFilter=_MyStpPortBpduFilter_Object((1,3,6,1,4,1,171,10,97,2,16,2,4,1,8),_MyStpPortBpduFilter_Type())
myStpPortBpduFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortBpduFilter.setStatus(_A)
_MyStpBpduGuard_Type=EnabledStatus
_MyStpBpduGuard_Object=MibScalar
myStpBpduGuard=_MyStpBpduGuard_Object((1,3,6,1,4,1,171,10,97,2,16,2,5),_MyStpBpduGuard_Type())
myStpBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpBpduGuard.setStatus(_A)
_MyStpBpduFilter_Type=EnabledStatus
_MyStpBpduFilter_Object=MibScalar
myStpBpduFilter=_MyStpBpduFilter_Object((1,3,6,1,4,1,171,10,97,2,16,2,6),_MyStpBpduFilter_Type())
myStpBpduFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpBpduFilter.setStatus(_A)
_MyStpCistRegionRoot_Type=BridgeId
_MyStpCistRegionRoot_Object=MibScalar
myStpCistRegionRoot=_MyStpCistRegionRoot_Object((1,3,6,1,4,1,171,10,97,2,16,2,7),_MyStpCistRegionRoot_Type())
myStpCistRegionRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpCistRegionRoot.setStatus(_G)
_MyStpCistPathCost_Type=Integer32
_MyStpCistPathCost_Object=MibScalar
myStpCistPathCost=_MyStpCistPathCost_Object((1,3,6,1,4,1,171,10,97,2,16,2,8),_MyStpCistPathCost_Type())
myStpCistPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpCistPathCost.setStatus(_G)
_MyMstpMIBObjects_ObjectIdentity=ObjectIdentity
myMstpMIBObjects=_MyMstpMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,3))
_MyStpMstiMaxInstanceNumber_Type=Integer32
_MyStpMstiMaxInstanceNumber_Object=MibScalar
myStpMstiMaxInstanceNumber=_MyStpMstiMaxInstanceNumber_Object((1,3,6,1,4,1,171,10,97,2,16,3,1),_MyStpMstiMaxInstanceNumber_Type())
myStpMstiMaxInstanceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiMaxInstanceNumber.setStatus(_A)
class _MyStpMstiRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyStpMstiRegionName_Type.__name__=_N
_MyStpMstiRegionName_Object=MibScalar
myStpMstiRegionName=_MyStpMstiRegionName_Object((1,3,6,1,4,1,171,10,97,2,16,3,2),_MyStpMstiRegionName_Type())
myStpMstiRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpMstiRegionName.setStatus(_A)
class _MyStpMstiRegionRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyStpMstiRegionRevision_Type.__name__=_E
_MyStpMstiRegionRevision_Object=MibScalar
myStpMstiRegionRevision=_MyStpMstiRegionRevision_Object((1,3,6,1,4,1,171,10,97,2,16,3,3),_MyStpMstiRegionRevision_Type())
myStpMstiRegionRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpMstiRegionRevision.setStatus(_A)
class _MyStpMstiMaxHopNumber_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_MyStpMstiMaxHopNumber_Type.__name__=_E
_MyStpMstiMaxHopNumber_Object=MibScalar
myStpMstiMaxHopNumber=_MyStpMstiMaxHopNumber_Object((1,3,6,1,4,1,171,10,97,2,16,3,4),_MyStpMstiMaxHopNumber_Type())
myStpMstiMaxHopNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpMstiMaxHopNumber.setStatus(_A)
_MyStpMstiInstanceTable_Object=MibTable
myStpMstiInstanceTable=_MyStpMstiInstanceTable_Object((1,3,6,1,4,1,171,10,97,2,16,3,5))
if mibBuilder.loadTexts:myStpMstiInstanceTable.setStatus(_A)
_MyStpMstiInstanceEntry_Object=MibTableRow
myStpMstiInstanceEntry=_MyStpMstiInstanceEntry_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1))
myStpMstiInstanceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:myStpMstiInstanceEntry.setStatus(_A)
class _MyStpMstiInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_MyStpMstiInstanceIndex_Type.__name__=_E
_MyStpMstiInstanceIndex_Object=MibTableColumn
myStpMstiInstanceIndex=_MyStpMstiInstanceIndex_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,1),_MyStpMstiInstanceIndex_Type())
myStpMstiInstanceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiInstanceIndex.setStatus(_A)
class _MyStpMstiInstanceVlansAddMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_MyStpMstiInstanceVlansAddMapped_Type.__name__=_F
_MyStpMstiInstanceVlansAddMapped_Object=MibTableColumn
myStpMstiInstanceVlansAddMapped=_MyStpMstiInstanceVlansAddMapped_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,2),_MyStpMstiInstanceVlansAddMapped_Type())
myStpMstiInstanceVlansAddMapped.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpMstiInstanceVlansAddMapped.setStatus(_A)
class _MyStpMstiInstanceVlansDeleteMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_MyStpMstiInstanceVlansDeleteMapped_Type.__name__=_F
_MyStpMstiInstanceVlansDeleteMapped_Object=MibTableColumn
myStpMstiInstanceVlansDeleteMapped=_MyStpMstiInstanceVlansDeleteMapped_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,3),_MyStpMstiInstanceVlansDeleteMapped_Type())
myStpMstiInstanceVlansDeleteMapped.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpMstiInstanceVlansDeleteMapped.setStatus(_A)
class _MyStpMstiInstanceVlansGetMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_MyStpMstiInstanceVlansGetMapped_Type.__name__=_F
_MyStpMstiInstanceVlansGetMapped_Object=MibTableColumn
myStpMstiInstanceVlansGetMapped=_MyStpMstiInstanceVlansGetMapped_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,4),_MyStpMstiInstanceVlansGetMapped_Type())
myStpMstiInstanceVlansGetMapped.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiInstanceVlansGetMapped.setStatus(_A)
class _MyStpMstiInstanceRemainingHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_MyStpMstiInstanceRemainingHopCount_Type.__name__=_E
_MyStpMstiInstanceRemainingHopCount_Object=MibTableColumn
myStpMstiInstanceRemainingHopCount=_MyStpMstiInstanceRemainingHopCount_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,5),_MyStpMstiInstanceRemainingHopCount_Type())
myStpMstiInstanceRemainingHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiInstanceRemainingHopCount.setStatus(_A)
class _MyStpMstiPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyStpMstiPriority_Type.__name__=_E
_MyStpMstiPriority_Object=MibTableColumn
myStpMstiPriority=_MyStpMstiPriority_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,6),_MyStpMstiPriority_Type())
myStpMstiPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpMstiPriority.setStatus(_A)
_MyStpMstiTimeSinceTopologyChange_Type=TimeTicks
_MyStpMstiTimeSinceTopologyChange_Object=MibTableColumn
myStpMstiTimeSinceTopologyChange=_MyStpMstiTimeSinceTopologyChange_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,7),_MyStpMstiTimeSinceTopologyChange_Type())
myStpMstiTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiTimeSinceTopologyChange.setStatus(_A)
_MyStpMstiTopChanges_Type=Integer32
_MyStpMstiTopChanges_Object=MibTableColumn
myStpMstiTopChanges=_MyStpMstiTopChanges_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,8),_MyStpMstiTopChanges_Type())
myStpMstiTopChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiTopChanges.setStatus(_A)
_MyStpMstiDesignatedRoot_Type=BridgeId
_MyStpMstiDesignatedRoot_Object=MibTableColumn
myStpMstiDesignatedRoot=_MyStpMstiDesignatedRoot_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,9),_MyStpMstiDesignatedRoot_Type())
myStpMstiDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiDesignatedRoot.setStatus(_A)
_MyStpMstiRootCost_Type=Integer32
_MyStpMstiRootCost_Object=MibTableColumn
myStpMstiRootCost=_MyStpMstiRootCost_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,10),_MyStpMstiRootCost_Type())
myStpMstiRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiRootCost.setStatus(_A)
_MyStpMstiRootPort_Type=Integer32
_MyStpMstiRootPort_Object=MibTableColumn
myStpMstiRootPort=_MyStpMstiRootPort_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,11),_MyStpMstiRootPort_Type())
myStpMstiRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpMstiRootPort.setStatus(_A)
_MyStpMstiInstanceEntryStatus_Type=ConfigStatus
_MyStpMstiInstanceEntryStatus_Object=MibTableColumn
myStpMstiInstanceEntryStatus=_MyStpMstiInstanceEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,16,3,5,1,12),_MyStpMstiInstanceEntryStatus_Type())
myStpMstiInstanceEntryStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myStpMstiInstanceEntryStatus.setStatus(_A)
_MyStpPortMstiInstanceTable_Object=MibTable
myStpPortMstiInstanceTable=_MyStpPortMstiInstanceTable_Object((1,3,6,1,4,1,171,10,97,2,16,3,6))
if mibBuilder.loadTexts:myStpPortMstiInstanceTable.setStatus(_A)
_MyStpPortMstiInstanceEntry_Object=MibTableRow
myStpPortMstiInstanceEntry=_MyStpPortMstiInstanceEntry_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1))
myStpPortMstiInstanceEntry.setIndexNames((0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:myStpPortMstiInstanceEntry.setStatus(_A)
_MyStpPortMstiIndex_Type=Integer32
_MyStpPortMstiIndex_Object=MibTableColumn
myStpPortMstiIndex=_MyStpPortMstiIndex_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,1),_MyStpPortMstiIndex_Type())
myStpPortMstiIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:myStpPortMstiIndex.setStatus(_A)
class _MyStpPortMstiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6),('discard',7)))
_MyStpPortMstiState_Type.__name__=_E
_MyStpPortMstiState_Object=MibTableColumn
myStpPortMstiState=_MyStpPortMstiState_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,2),_MyStpPortMstiState_Type())
myStpPortMstiState.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiState.setStatus(_A)
_MyStpPortMstiAdminPathCost_Type=Integer32
_MyStpPortMstiAdminPathCost_Object=MibTableColumn
myStpPortMstiAdminPathCost=_MyStpPortMstiAdminPathCost_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,3),_MyStpPortMstiAdminPathCost_Type())
myStpPortMstiAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortMstiAdminPathCost.setStatus(_A)
_MyStpPortMstiOperPathCost_Type=Counter32
_MyStpPortMstiOperPathCost_Object=MibTableColumn
myStpPortMstiOperPathCost=_MyStpPortMstiOperPathCost_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,4),_MyStpPortMstiOperPathCost_Type())
myStpPortMstiOperPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiOperPathCost.setStatus(_A)
class _MyStpPortMstiPriority_Type(Integer32):defaultValue=128
_MyStpPortMstiPriority_Type.__name__=_E
_MyStpPortMstiPriority_Object=MibTableColumn
myStpPortMstiPriority=_MyStpPortMstiPriority_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,5),_MyStpPortMstiPriority_Type())
myStpPortMstiPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpPortMstiPriority.setStatus(_A)
_MyStpPortMstiDesignatedRoot_Type=BridgeId
_MyStpPortMstiDesignatedRoot_Object=MibTableColumn
myStpPortMstiDesignatedRoot=_MyStpPortMstiDesignatedRoot_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,6),_MyStpPortMstiDesignatedRoot_Type())
myStpPortMstiDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiDesignatedRoot.setStatus(_A)
_MyStpPortMstiDesignatedCost_Type=Integer32
_MyStpPortMstiDesignatedCost_Object=MibTableColumn
myStpPortMstiDesignatedCost=_MyStpPortMstiDesignatedCost_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,7),_MyStpPortMstiDesignatedCost_Type())
myStpPortMstiDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiDesignatedCost.setStatus(_A)
_MyStpPortMstiDesignatedBridge_Type=BridgeId
_MyStpPortMstiDesignatedBridge_Object=MibTableColumn
myStpPortMstiDesignatedBridge=_MyStpPortMstiDesignatedBridge_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,8),_MyStpPortMstiDesignatedBridge_Type())
myStpPortMstiDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiDesignatedBridge.setStatus(_A)
class _MyStpPortMstiDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MyStpPortMstiDesignatedPort_Type.__name__=_F
_MyStpPortMstiDesignatedPort_Object=MibTableColumn
myStpPortMstiDesignatedPort=_MyStpPortMstiDesignatedPort_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,9),_MyStpPortMstiDesignatedPort_Type())
myStpPortMstiDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiDesignatedPort.setStatus(_A)
class _MyStpPortMstiPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_MyStpPortMstiPortRole_Type.__name__=_E
_MyStpPortMstiPortRole_Object=MibTableColumn
myStpPortMstiPortRole=_MyStpPortMstiPortRole_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,10),_MyStpPortMstiPortRole_Type())
myStpPortMstiPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiPortRole.setStatus(_A)
_MyStpPortMstiPortForwardTransitions_Type=Integer32
_MyStpPortMstiPortForwardTransitions_Object=MibTableColumn
myStpPortMstiPortForwardTransitions=_MyStpPortMstiPortForwardTransitions_Object((1,3,6,1,4,1,171,10,97,2,16,3,6,1,11),_MyStpPortMstiPortForwardTransitions_Type())
myStpPortMstiPortForwardTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpPortMstiPortForwardTransitions.setStatus(_A)
_MyStpMstiReset_Type=Integer32
_MyStpMstiReset_Object=MibScalar
myStpMstiReset=_MyStpMstiReset_Object((1,3,6,1,4,1,171,10,97,2,16,3,7),_MyStpMstiReset_Type())
myStpMstiReset.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpMstiReset.setStatus(_A)
_MyStpCistVlansAddMapped_Type=OctetString
_MyStpCistVlansAddMapped_Object=MibScalar
myStpCistVlansAddMapped=_MyStpCistVlansAddMapped_Object((1,3,6,1,4,1,171,10,97,2,16,3,8),_MyStpCistVlansAddMapped_Type())
myStpCistVlansAddMapped.setMaxAccess(_D)
if mibBuilder.loadTexts:myStpCistVlansAddMapped.setStatus(_G)
_MyStpCistVlansGetMapped_Type=OctetString
_MyStpCistVlansGetMapped_Object=MibScalar
myStpCistVlansGetMapped=_MyStpCistVlansGetMapped_Object((1,3,6,1,4,1,171,10,97,2,16,3,9),_MyStpCistVlansGetMapped_Type())
myStpCistVlansGetMapped.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpCistVlansGetMapped.setStatus(_G)
_MyStpCistRemainingHopCount_Type=Integer32
_MyStpCistRemainingHopCount_Object=MibScalar
myStpCistRemainingHopCount=_MyStpCistRemainingHopCount_Object((1,3,6,1,4,1,171,10,97,2,16,3,10),_MyStpCistRemainingHopCount_Type())
myStpCistRemainingHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:myStpCistRemainingHopCount.setStatus(_G)
_StpExternConformance_ObjectIdentity=ObjectIdentity
stpExternConformance=_StpExternConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,4))
_StpExternGroups_ObjectIdentity=ObjectIdentity
stpExternGroups=_StpExternGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,4,1))
_RstpConformance_ObjectIdentity=ObjectIdentity
rstpConformance=_RstpConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,5))
_RstpGroups_ObjectIdentity=ObjectIdentity
rstpGroups=_RstpGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,5,1))
_RstpCompliances_ObjectIdentity=ObjectIdentity
rstpCompliances=_RstpCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,5,2))
_MstpConformance_ObjectIdentity=ObjectIdentity
mstpConformance=_MstpConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,6))
_MstpGroups_ObjectIdentity=ObjectIdentity
mstpGroups=_MstpGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,6,1))
_MstpCompliances_ObjectIdentity=ObjectIdentity
mstpCompliances=_MstpCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,16,6,2))
stpExternGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,16,4,1,1))
stpExternGroup.setObjects(*((_B,_U),(_B,_V),(_B,_I),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:stpExternGroup.setStatus(_A)
rstpBridgeGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,16,5,1,1))
rstpBridgeGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:rstpBridgeGroup.setStatus(_A)
rstpDefaultPathCostGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,16,5,1,2))
rstpDefaultPathCostGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:rstpDefaultPathCostGroup.setStatus(_A)
rstpPortGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,16,5,1,3))
rstpPortGroup.setObjects(*((_B,_J),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:rstpPortGroup.setStatus(_A)
mstpBridgeRegionGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,16,6,1,1))
mstpBridgeRegionGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:mstpBridgeRegionGroup.setStatus(_A)
mstpMstiBridgeGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,16,6,1,2))
mstpMstiBridgeGroup.setObjects(*((_B,_H),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:mstpMstiBridgeGroup.setStatus(_A)
mstpMstiPortGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,16,6,1,3))
mstpMstiPortGroup.setObjects(*((_B,_K),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:mstpMstiPortGroup.setStatus(_A)
rstpCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,16,5,2,1))
rstpCompliance.setObjects(*((_B,_AC),(_B,_L),(_B,_AD),(_B,_L)))
if mibBuilder.loadTexts:rstpCompliance.setStatus(_A)
mstpCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,16,6,2,1))
mstpCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:mstpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myStpMIB':myStpMIB,'myStpMIBObjects':myStpMIBObjects,_U:mySysStpStatus,_V:mySysStpReset,'myStpExtPortTable':myStpExtPortTable,'myStpExtPortEntry':myStpExtPortEntry,_I:myStpPortIfIndex,_W:myStpPortAdminPathCost,_X:myStpPortOperPathCost,_Y:myStpPortRole,'myRstpMIBObjects':myRstpMIBObjects,_Z:myStpVersion,_a:myStpTxHoldCount,_d:myStpPathCostDefault,'myRstpExtPortTable':myRstpExtPortTable,'myRstpExtPortEntry':myRstpExtPortEntry,_J:myRstpExtPortIfIndex,_e:myStpPortProtocolMigration,_f:myStpPortAdminEdgePort,_g:myStpPortOperEdgePort,_h:myStpPortAdminPointToPoint,_i:myStpPortOperPointToPoint,_j:myStpPortBpduGuard,_k:myStpPortBpduFilter,_b:myStpBpduGuard,_c:myStpBpduFilter,_l:myStpCistRegionRoot,_m:myStpCistPathCost,'myMstpMIBObjects':myMstpMIBObjects,_n:myStpMstiMaxInstanceNumber,_o:myStpMstiRegionName,_p:myStpMstiRegionRevision,_q:myStpMstiMaxHopNumber,'myStpMstiInstanceTable':myStpMstiInstanceTable,'myStpMstiInstanceEntry':myStpMstiInstanceEntry,_H:myStpMstiInstanceIndex,_r:myStpMstiInstanceVlansAddMapped,_s:myStpMstiInstanceVlansDeleteMapped,_t:myStpMstiInstanceVlansGetMapped,_u:myStpMstiInstanceRemainingHopCount,_v:myStpMstiPriority,_w:myStpMstiTimeSinceTopologyChange,_x:myStpMstiTopChanges,_y:myStpMstiDesignatedRoot,_z:myStpMstiRootCost,_A0:myStpMstiRootPort,_A1:myStpMstiInstanceEntryStatus,'myStpPortMstiInstanceTable':myStpPortMstiInstanceTable,'myStpPortMstiInstanceEntry':myStpPortMstiInstanceEntry,_K:myStpPortMstiIndex,_A2:myStpPortMstiState,_A3:myStpPortMstiAdminPathCost,_A4:myStpPortMstiOperPathCost,_A5:myStpPortMstiPriority,_A6:myStpPortMstiDesignatedRoot,_A7:myStpPortMstiDesignatedCost,_A8:myStpPortMstiDesignatedBridge,_A9:myStpPortMstiDesignatedPort,_AA:myStpPortMstiPortRole,_AB:myStpPortMstiPortForwardTransitions,'myStpMstiReset':myStpMstiReset,'myStpCistVlansAddMapped':myStpCistVlansAddMapped,'myStpCistVlansGetMapped':myStpCistVlansGetMapped,'myStpCistRemainingHopCount':myStpCistRemainingHopCount,'stpExternConformance':stpExternConformance,'stpExternGroups':stpExternGroups,'stpExternGroup':stpExternGroup,'rstpConformance':rstpConformance,'rstpGroups':rstpGroups,_AC:rstpBridgeGroup,_L:rstpDefaultPathCostGroup,_AD:rstpPortGroup,'rstpCompliances':rstpCompliances,'rstpCompliance':rstpCompliance,'mstpConformance':mstpConformance,'mstpGroups':mstpGroups,_AE:mstpBridgeRegionGroup,_AF:mstpMstiBridgeGroup,_AG:mstpMstiPortGroup,'mstpCompliances':mstpCompliances,'mstpCompliance':mstpCompliance})