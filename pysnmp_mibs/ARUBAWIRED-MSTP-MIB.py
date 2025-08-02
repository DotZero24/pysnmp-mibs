_x='arubaWiredMstpGroup'
_w='arubaWiredMstpPortGroup'
_v='arubaWiredMstpNotificationGroup'
_u='arubaWiredMstpNotificationObjectGroup'
_t='arubaWiredMstpCISTTopologyChange'
_s='arubaWiredMstpInstanceTopologyChange'
_r='arubaWiredMstpCISTLoopGuardInconsistency'
_q='arubaWiredMstpInstanceLoopGuardInconsistency'
_p='arubaWiredMstpCISTRootGuardInconsistency'
_o='arubaWiredMstpInstanceRootGuardInconsistency'
_n='arubaWiredMstpCISTNewRoot'
_m='arubaWiredMstpInstanceNewRoot'
_l='arubaWiredMstpErrantBpduReceived'
_k='arubaWiredMstpBpduGuardTimeout'
_j='arubaWiredMstpPortRpvstFiltering'
_i='arubaWiredMstpPortRpvstProtection'
_h='arubaWiredMstpPortBpduProtection'
_g='arubaWiredMstpPortLoopGuard'
_f='arubaWiredMstpPortRootGuard'
_e='arubaWiredMstpPortRestrictedTcn'
_d='arubaWiredMstpPortBpduFiltering'
_c='arubaWiredMstpPortAutoEdge'
_b='arubaWiredMstpPortAdminPointToPoint'
_a='arubaWiredMstpPortAdminEdge'
_Z='PointToPoint'
_Y='arubaWiredMstpPortIndex'
_X='not-accessible'
_W='arubaWiredMstpId'
_V='arubaWiredMstpErrantBpduDetector'
_U='arubaWiredMstpPortInstanceState'
_T='arubaWiredMstpErrantBpduSrcMac'
_S='arubaWiredMstpPortErrantBpduRxCount'
_R='arubaWiredMstpRootBridgeChangeTimeStamp'
_Q='arubaWiredMstpNewRootBridgeID'
_P='arubaWiredMstpPreviousRootBridgeID'
_O='arubaWiredMstpTopoChangeTime'
_N='arubaWiredMstpNewPortRole'
_M='arubaWiredMstpOldPortRole'
_L='arubaWiredMstpPortDesignatedBridge'
_K='arubaWiredMstpSuperiorBpduSrcMac'
_J='arubaWiredMstpSuperiorBpduSrcPort'
_I='Integer32'
_H='arubaWiredMstpInstanceID'
_G='arubaWiredMstpPortName'
_F='DisplayString'
_E='TruthValue'
_D='read-write'
_C='accessible-for-notify'
_B='current'
_A='ARUBAWIRED-MSTP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','TextualConvention',_E)
arubaWiredMstpMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,13))
if mibBuilder.loadTexts:arubaWiredMstpMIB.setRevisions(('2020-06-12 00:00','2018-01-18 00:00'))
class PointToPoint(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceTrue',1),('forceFalse',2),('auto',3)))
_ArubaWiredMstpNotifications_ObjectIdentity=ObjectIdentity
arubaWiredMstpNotifications=_ArubaWiredMstpNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,13,0))
_ArubaWiredMstpObjects_ObjectIdentity=ObjectIdentity
arubaWiredMstpObjects=_ArubaWiredMstpObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,13,1))
_ArubaWiredMstpNotificationTable_Object=MibTable
arubaWiredMstpNotificationTable=_ArubaWiredMstpNotificationTable_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1))
if mibBuilder.loadTexts:arubaWiredMstpNotificationTable.setStatus(_B)
_ArubaWiredMstpNotificationEntry_Object=MibTableRow
arubaWiredMstpNotificationEntry=_ArubaWiredMstpNotificationEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1))
arubaWiredMstpNotificationEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:arubaWiredMstpNotificationEntry.setStatus(_B)
class _ArubaWiredMstpPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpPortName_Type.__name__=_F
_ArubaWiredMstpPortName_Object=MibTableColumn
arubaWiredMstpPortName=_ArubaWiredMstpPortName_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,1),_ArubaWiredMstpPortName_Type())
arubaWiredMstpPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpPortName.setStatus(_B)
class _ArubaWiredMstpInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65))
_ArubaWiredMstpInstanceID_Type.__name__=_I
_ArubaWiredMstpInstanceID_Object=MibTableColumn
arubaWiredMstpInstanceID=_ArubaWiredMstpInstanceID_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,2),_ArubaWiredMstpInstanceID_Type())
arubaWiredMstpInstanceID.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpInstanceID.setStatus(_B)
class _ArubaWiredMstpPortErrantBpduRxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ArubaWiredMstpPortErrantBpduRxCount_Type.__name__=_I
_ArubaWiredMstpPortErrantBpduRxCount_Object=MibTableColumn
arubaWiredMstpPortErrantBpduRxCount=_ArubaWiredMstpPortErrantBpduRxCount_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,3),_ArubaWiredMstpPortErrantBpduRxCount_Type())
arubaWiredMstpPortErrantBpduRxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpPortErrantBpduRxCount.setStatus(_B)
_ArubaWiredMstpErrantBpduSrcMac_Type=MacAddress
_ArubaWiredMstpErrantBpduSrcMac_Object=MibTableColumn
arubaWiredMstpErrantBpduSrcMac=_ArubaWiredMstpErrantBpduSrcMac_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,4),_ArubaWiredMstpErrantBpduSrcMac_Type())
arubaWiredMstpErrantBpduSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpErrantBpduSrcMac.setStatus(_B)
class _ArubaWiredMstpSuperiorBpduSrcPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpSuperiorBpduSrcPort_Type.__name__=_F
_ArubaWiredMstpSuperiorBpduSrcPort_Object=MibTableColumn
arubaWiredMstpSuperiorBpduSrcPort=_ArubaWiredMstpSuperiorBpduSrcPort_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,5),_ArubaWiredMstpSuperiorBpduSrcPort_Type())
arubaWiredMstpSuperiorBpduSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpSuperiorBpduSrcPort.setStatus(_B)
_ArubaWiredMstpSuperiorBpduSrcMac_Type=MacAddress
_ArubaWiredMstpSuperiorBpduSrcMac_Object=MibTableColumn
arubaWiredMstpSuperiorBpduSrcMac=_ArubaWiredMstpSuperiorBpduSrcMac_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,6),_ArubaWiredMstpSuperiorBpduSrcMac_Type())
arubaWiredMstpSuperiorBpduSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpSuperiorBpduSrcMac.setStatus(_B)
class _ArubaWiredMstpPortInstanceState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpPortInstanceState_Type.__name__=_F
_ArubaWiredMstpPortInstanceState_Object=MibTableColumn
arubaWiredMstpPortInstanceState=_ArubaWiredMstpPortInstanceState_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,7),_ArubaWiredMstpPortInstanceState_Type())
arubaWiredMstpPortInstanceState.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpPortInstanceState.setStatus(_B)
class _ArubaWiredMstpErrantBpduDetector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bpduFilter',1),('bpduProtection',2)))
_ArubaWiredMstpErrantBpduDetector_Type.__name__=_I
_ArubaWiredMstpErrantBpduDetector_Object=MibTableColumn
arubaWiredMstpErrantBpduDetector=_ArubaWiredMstpErrantBpduDetector_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,8),_ArubaWiredMstpErrantBpduDetector_Type())
arubaWiredMstpErrantBpduDetector.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpErrantBpduDetector.setStatus(_B)
class _ArubaWiredMstpPortDesignatedBridge_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpPortDesignatedBridge_Type.__name__=_F
_ArubaWiredMstpPortDesignatedBridge_Object=MibTableColumn
arubaWiredMstpPortDesignatedBridge=_ArubaWiredMstpPortDesignatedBridge_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,9),_ArubaWiredMstpPortDesignatedBridge_Type())
arubaWiredMstpPortDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpPortDesignatedBridge.setStatus(_B)
class _ArubaWiredMstpOldPortRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpOldPortRole_Type.__name__=_F
_ArubaWiredMstpOldPortRole_Object=MibTableColumn
arubaWiredMstpOldPortRole=_ArubaWiredMstpOldPortRole_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,10),_ArubaWiredMstpOldPortRole_Type())
arubaWiredMstpOldPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpOldPortRole.setStatus(_B)
class _ArubaWiredMstpNewPortRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpNewPortRole_Type.__name__=_F
_ArubaWiredMstpNewPortRole_Object=MibTableColumn
arubaWiredMstpNewPortRole=_ArubaWiredMstpNewPortRole_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,11),_ArubaWiredMstpNewPortRole_Type())
arubaWiredMstpNewPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpNewPortRole.setStatus(_B)
_ArubaWiredMstpTopoChangeTime_Type=DateAndTime
_ArubaWiredMstpTopoChangeTime_Object=MibTableColumn
arubaWiredMstpTopoChangeTime=_ArubaWiredMstpTopoChangeTime_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,12),_ArubaWiredMstpTopoChangeTime_Type())
arubaWiredMstpTopoChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpTopoChangeTime.setStatus(_B)
class _ArubaWiredMstpPreviousRootBridgeID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpPreviousRootBridgeID_Type.__name__=_F
_ArubaWiredMstpPreviousRootBridgeID_Object=MibTableColumn
arubaWiredMstpPreviousRootBridgeID=_ArubaWiredMstpPreviousRootBridgeID_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,13),_ArubaWiredMstpPreviousRootBridgeID_Type())
arubaWiredMstpPreviousRootBridgeID.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpPreviousRootBridgeID.setStatus(_B)
class _ArubaWiredMstpNewRootBridgeID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredMstpNewRootBridgeID_Type.__name__=_F
_ArubaWiredMstpNewRootBridgeID_Object=MibTableColumn
arubaWiredMstpNewRootBridgeID=_ArubaWiredMstpNewRootBridgeID_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,14),_ArubaWiredMstpNewRootBridgeID_Type())
arubaWiredMstpNewRootBridgeID.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpNewRootBridgeID.setStatus(_B)
_ArubaWiredMstpRootBridgeChangeTimeStamp_Type=DateAndTime
_ArubaWiredMstpRootBridgeChangeTimeStamp_Object=MibTableColumn
arubaWiredMstpRootBridgeChangeTimeStamp=_ArubaWiredMstpRootBridgeChangeTimeStamp_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,15),_ArubaWiredMstpRootBridgeChangeTimeStamp_Type())
arubaWiredMstpRootBridgeChangeTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMstpRootBridgeChangeTimeStamp.setStatus(_B)
class _ArubaWiredMstpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65))
_ArubaWiredMstpId_Type.__name__=_I
_ArubaWiredMstpId_Object=MibTableColumn
arubaWiredMstpId=_ArubaWiredMstpId_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,1,1,16),_ArubaWiredMstpId_Type())
arubaWiredMstpId.setMaxAccess(_X)
if mibBuilder.loadTexts:arubaWiredMstpId.setStatus(_B)
_ArubaWiredMstpPortTable_Object=MibTable
arubaWiredMstpPortTable=_ArubaWiredMstpPortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2))
if mibBuilder.loadTexts:arubaWiredMstpPortTable.setStatus(_B)
_ArubaWiredMstpPortEntry_Object=MibTableRow
arubaWiredMstpPortEntry=_ArubaWiredMstpPortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1))
arubaWiredMstpPortEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:arubaWiredMstpPortEntry.setStatus(_B)
_ArubaWiredMstpPortIndex_Type=InterfaceIndex
_ArubaWiredMstpPortIndex_Object=MibTableColumn
arubaWiredMstpPortIndex=_ArubaWiredMstpPortIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,1),_ArubaWiredMstpPortIndex_Type())
arubaWiredMstpPortIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:arubaWiredMstpPortIndex.setStatus(_B)
class _ArubaWiredMstpPortAdminEdge_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortAdminEdge_Type.__name__=_E
_ArubaWiredMstpPortAdminEdge_Object=MibTableColumn
arubaWiredMstpPortAdminEdge=_ArubaWiredMstpPortAdminEdge_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,2),_ArubaWiredMstpPortAdminEdge_Type())
arubaWiredMstpPortAdminEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortAdminEdge.setStatus(_B)
class _ArubaWiredMstpPortAdminPointToPoint_Type(PointToPoint):defaultValue=3
_ArubaWiredMstpPortAdminPointToPoint_Type.__name__=_Z
_ArubaWiredMstpPortAdminPointToPoint_Object=MibTableColumn
arubaWiredMstpPortAdminPointToPoint=_ArubaWiredMstpPortAdminPointToPoint_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,3),_ArubaWiredMstpPortAdminPointToPoint_Type())
arubaWiredMstpPortAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortAdminPointToPoint.setStatus(_B)
class _ArubaWiredMstpPortAutoEdge_Type(TruthValue):defaultValue=1
_ArubaWiredMstpPortAutoEdge_Type.__name__=_E
_ArubaWiredMstpPortAutoEdge_Object=MibTableColumn
arubaWiredMstpPortAutoEdge=_ArubaWiredMstpPortAutoEdge_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,4),_ArubaWiredMstpPortAutoEdge_Type())
arubaWiredMstpPortAutoEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortAutoEdge.setStatus(_B)
class _ArubaWiredMstpPortBpduFiltering_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortBpduFiltering_Type.__name__=_E
_ArubaWiredMstpPortBpduFiltering_Object=MibTableColumn
arubaWiredMstpPortBpduFiltering=_ArubaWiredMstpPortBpduFiltering_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,5),_ArubaWiredMstpPortBpduFiltering_Type())
arubaWiredMstpPortBpduFiltering.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortBpduFiltering.setStatus(_B)
class _ArubaWiredMstpPortRestrictedTcn_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortRestrictedTcn_Type.__name__=_E
_ArubaWiredMstpPortRestrictedTcn_Object=MibTableColumn
arubaWiredMstpPortRestrictedTcn=_ArubaWiredMstpPortRestrictedTcn_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,6),_ArubaWiredMstpPortRestrictedTcn_Type())
arubaWiredMstpPortRestrictedTcn.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortRestrictedTcn.setStatus(_B)
class _ArubaWiredMstpPortRootGuard_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortRootGuard_Type.__name__=_E
_ArubaWiredMstpPortRootGuard_Object=MibTableColumn
arubaWiredMstpPortRootGuard=_ArubaWiredMstpPortRootGuard_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,7),_ArubaWiredMstpPortRootGuard_Type())
arubaWiredMstpPortRootGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortRootGuard.setStatus(_B)
class _ArubaWiredMstpPortLoopGuard_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortLoopGuard_Type.__name__=_E
_ArubaWiredMstpPortLoopGuard_Object=MibTableColumn
arubaWiredMstpPortLoopGuard=_ArubaWiredMstpPortLoopGuard_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,8),_ArubaWiredMstpPortLoopGuard_Type())
arubaWiredMstpPortLoopGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortLoopGuard.setStatus(_B)
class _ArubaWiredMstpPortBpduProtection_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortBpduProtection_Type.__name__=_E
_ArubaWiredMstpPortBpduProtection_Object=MibTableColumn
arubaWiredMstpPortBpduProtection=_ArubaWiredMstpPortBpduProtection_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,9),_ArubaWiredMstpPortBpduProtection_Type())
arubaWiredMstpPortBpduProtection.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortBpduProtection.setStatus(_B)
class _ArubaWiredMstpPortRpvstProtection_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortRpvstProtection_Type.__name__=_E
_ArubaWiredMstpPortRpvstProtection_Object=MibTableColumn
arubaWiredMstpPortRpvstProtection=_ArubaWiredMstpPortRpvstProtection_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,10),_ArubaWiredMstpPortRpvstProtection_Type())
arubaWiredMstpPortRpvstProtection.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortRpvstProtection.setStatus(_B)
class _ArubaWiredMstpPortRpvstFiltering_Type(TruthValue):defaultValue=2
_ArubaWiredMstpPortRpvstFiltering_Type.__name__=_E
_ArubaWiredMstpPortRpvstFiltering_Object=MibTableColumn
arubaWiredMstpPortRpvstFiltering=_ArubaWiredMstpPortRpvstFiltering_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,2,1,11),_ArubaWiredMstpPortRpvstFiltering_Type())
arubaWiredMstpPortRpvstFiltering.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpPortRpvstFiltering.setStatus(_B)
_ArubaWiredMstpGeneralGroup_ObjectIdentity=ObjectIdentity
arubaWiredMstpGeneralGroup=_ArubaWiredMstpGeneralGroup_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,13,1,3))
_ArubaWiredMstpBpduGuardTimeout_Type=Integer32
_ArubaWiredMstpBpduGuardTimeout_Object=MibScalar
arubaWiredMstpBpduGuardTimeout=_ArubaWiredMstpBpduGuardTimeout_Object((1,3,6,1,4,1,47196,4,1,1,3,13,1,3,1),_ArubaWiredMstpBpduGuardTimeout_Type())
arubaWiredMstpBpduGuardTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredMstpBpduGuardTimeout.setStatus(_B)
_ArubaWiredMstpConformance_ObjectIdentity=ObjectIdentity
arubaWiredMstpConformance=_ArubaWiredMstpConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,13,2))
_ArubaWiredMstpGroups_ObjectIdentity=ObjectIdentity
arubaWiredMstpGroups=_ArubaWiredMstpGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,13,2,1))
_ArubaWiredMstpCompliances_ObjectIdentity=ObjectIdentity
arubaWiredMstpCompliances=_ArubaWiredMstpCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,13,2,2))
arubaWiredMstpNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,13,2,1,1))
arubaWiredMstpNotificationObjectGroup.setObjects(*((_A,_G),(_A,_H),(_A,_S),(_A,_T),(_A,_J),(_A,_K),(_A,_U),(_A,_V),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:arubaWiredMstpNotificationObjectGroup.setStatus(_B)
arubaWiredMstpPortGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,13,2,1,3))
arubaWiredMstpPortGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:arubaWiredMstpPortGroup.setStatus(_B)
arubaWiredMstpGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,13,2,1,4))
arubaWiredMstpGroup.setObjects((_A,_k))
if mibBuilder.loadTexts:arubaWiredMstpGroup.setStatus(_B)
arubaWiredMstpErrantBpduReceived=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,1))
arubaWiredMstpErrantBpduReceived.setObjects(*((_A,_G),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:arubaWiredMstpErrantBpduReceived.setStatus(_B)
arubaWiredMstpInstanceTopologyChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,2))
arubaWiredMstpInstanceTopologyChange.setObjects(*((_A,_G),(_A,_H),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:arubaWiredMstpInstanceTopologyChange.setStatus(_B)
arubaWiredMstpCISTTopologyChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,3))
arubaWiredMstpCISTTopologyChange.setObjects(*((_A,_G),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:arubaWiredMstpCISTTopologyChange.setStatus(_B)
arubaWiredMstpInstanceNewRoot=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,4))
arubaWiredMstpInstanceNewRoot.setObjects(*((_A,_H),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:arubaWiredMstpInstanceNewRoot.setStatus(_B)
arubaWiredMstpCISTNewRoot=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,5))
arubaWiredMstpCISTNewRoot.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:arubaWiredMstpCISTNewRoot.setStatus(_B)
arubaWiredMstpInstanceLoopGuardInconsistency=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,6))
arubaWiredMstpInstanceLoopGuardInconsistency.setObjects(*((_A,_G),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:arubaWiredMstpInstanceLoopGuardInconsistency.setStatus(_B)
arubaWiredMstpCISTLoopGuardInconsistency=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,7))
arubaWiredMstpCISTLoopGuardInconsistency.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:arubaWiredMstpCISTLoopGuardInconsistency.setStatus(_B)
arubaWiredMstpInstanceRootGuardInconsistency=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,8))
arubaWiredMstpInstanceRootGuardInconsistency.setObjects(*((_A,_G),(_A,_H),(_A,_K),(_A,_J)))
if mibBuilder.loadTexts:arubaWiredMstpInstanceRootGuardInconsistency.setStatus(_B)
arubaWiredMstpCISTRootGuardInconsistency=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,13,0,9))
arubaWiredMstpCISTRootGuardInconsistency.setObjects(*((_A,_G),(_A,_K),(_A,_J)))
if mibBuilder.loadTexts:arubaWiredMstpCISTRootGuardInconsistency.setStatus(_B)
arubaWiredMstpNotificationGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,13,2,1,2))
arubaWiredMstpNotificationGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:arubaWiredMstpNotificationGroup.setStatus(_B)
arubaWiredMstpNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,13,2,2,1))
arubaWiredMstpNotificationCompliance.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:arubaWiredMstpNotificationCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_Z:PointToPoint,'arubaWiredMstpMIB':arubaWiredMstpMIB,'arubaWiredMstpNotifications':arubaWiredMstpNotifications,_l:arubaWiredMstpErrantBpduReceived,_s:arubaWiredMstpInstanceTopologyChange,_t:arubaWiredMstpCISTTopologyChange,_m:arubaWiredMstpInstanceNewRoot,_n:arubaWiredMstpCISTNewRoot,_q:arubaWiredMstpInstanceLoopGuardInconsistency,_r:arubaWiredMstpCISTLoopGuardInconsistency,_o:arubaWiredMstpInstanceRootGuardInconsistency,_p:arubaWiredMstpCISTRootGuardInconsistency,'arubaWiredMstpObjects':arubaWiredMstpObjects,'arubaWiredMstpNotificationTable':arubaWiredMstpNotificationTable,'arubaWiredMstpNotificationEntry':arubaWiredMstpNotificationEntry,_G:arubaWiredMstpPortName,_H:arubaWiredMstpInstanceID,_S:arubaWiredMstpPortErrantBpduRxCount,_T:arubaWiredMstpErrantBpduSrcMac,_J:arubaWiredMstpSuperiorBpduSrcPort,_K:arubaWiredMstpSuperiorBpduSrcMac,_U:arubaWiredMstpPortInstanceState,_V:arubaWiredMstpErrantBpduDetector,_L:arubaWiredMstpPortDesignatedBridge,_M:arubaWiredMstpOldPortRole,_N:arubaWiredMstpNewPortRole,_O:arubaWiredMstpTopoChangeTime,_P:arubaWiredMstpPreviousRootBridgeID,_Q:arubaWiredMstpNewRootBridgeID,_R:arubaWiredMstpRootBridgeChangeTimeStamp,_W:arubaWiredMstpId,'arubaWiredMstpPortTable':arubaWiredMstpPortTable,'arubaWiredMstpPortEntry':arubaWiredMstpPortEntry,_Y:arubaWiredMstpPortIndex,_a:arubaWiredMstpPortAdminEdge,_b:arubaWiredMstpPortAdminPointToPoint,_c:arubaWiredMstpPortAutoEdge,_d:arubaWiredMstpPortBpduFiltering,_e:arubaWiredMstpPortRestrictedTcn,_f:arubaWiredMstpPortRootGuard,_g:arubaWiredMstpPortLoopGuard,_h:arubaWiredMstpPortBpduProtection,_i:arubaWiredMstpPortRpvstProtection,_j:arubaWiredMstpPortRpvstFiltering,'arubaWiredMstpGeneralGroup':arubaWiredMstpGeneralGroup,_k:arubaWiredMstpBpduGuardTimeout,'arubaWiredMstpConformance':arubaWiredMstpConformance,'arubaWiredMstpGroups':arubaWiredMstpGroups,_u:arubaWiredMstpNotificationObjectGroup,_v:arubaWiredMstpNotificationGroup,_w:arubaWiredMstpPortGroup,_x:arubaWiredMstpGroup,'arubaWiredMstpCompliances':arubaWiredMstpCompliances,'arubaWiredMstpNotificationCompliance':arubaWiredMstpNotificationCompliance})