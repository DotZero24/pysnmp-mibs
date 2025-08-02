_V='nmsERPSRingState'
_U='current'
_T='nmsERPSRingPort'
_S='nmsERPSRingPortRingID'
_R='nmsERPSRingRole'
_Q='nmsERPSRingNodeID'
_P='link-up'
_O='link-down'
_N='forwarding'
_M='blocking'
_L='read-create'
_K='enabled'
_J='disabled'
_I='nmsERPSRingID'
_H='DisplayString'
_G='rpl'
_F='ring-port'
_E='read-write'
_D='NMS-ERPS-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmslocal,=mibBuilder.importSymbols('NMS-SMI','nmslocal')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_NmsERPS_ObjectIdentity=ObjectIdentity
nmsERPS=_NmsERPS_ObjectIdentity((1,3,6,1,4,1,3320,2,231))
_NmsERPSRings_Type=Integer32
_NmsERPSRings_Object=MibScalar
nmsERPSRings=_NmsERPSRings_Object((1,3,6,1,4,1,3320,2,231,1),_NmsERPSRings_Type())
nmsERPSRings.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRings.setStatus(_A)
class _NmsERPSInconsistenceCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_NmsERPSInconsistenceCheck_Type.__name__=_C
_NmsERPSInconsistenceCheck_Object=MibScalar
nmsERPSInconsistenceCheck=_NmsERPSInconsistenceCheck_Object((1,3,6,1,4,1,3320,2,231,2),_NmsERPSInconsistenceCheck_Type())
nmsERPSInconsistenceCheck.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSInconsistenceCheck.setStatus(_A)
_NmsERPSPduRx_Type=Integer32
_NmsERPSPduRx_Object=MibScalar
nmsERPSPduRx=_NmsERPSPduRx_Object((1,3,6,1,4,1,3320,2,231,3),_NmsERPSPduRx_Type())
nmsERPSPduRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSPduRx.setStatus(_A)
_NmsERPSPduRxDropped_Type=Integer32
_NmsERPSPduRxDropped_Object=MibScalar
nmsERPSPduRxDropped=_NmsERPSPduRxDropped_Object((1,3,6,1,4,1,3320,2,231,4),_NmsERPSPduRxDropped_Type())
nmsERPSPduRxDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSPduRxDropped.setStatus(_A)
_NmsERPSPduTx_Type=Integer32
_NmsERPSPduTx_Object=MibScalar
nmsERPSPduTx=_NmsERPSPduTx_Object((1,3,6,1,4,1,3320,2,231,5),_NmsERPSPduTx_Type())
nmsERPSPduTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSPduTx.setStatus(_A)
_NmsERPSRingTable_Object=MibTable
nmsERPSRingTable=_NmsERPSRingTable_Object((1,3,6,1,4,1,3320,2,231,6))
if mibBuilder.loadTexts:nmsERPSRingTable.setStatus(_A)
_NmsERPSRingTableEntry_Object=MibTableRow
nmsERPSRingTableEntry=_NmsERPSRingTableEntry_Object((1,3,6,1,4,1,3320,2,231,6,1))
nmsERPSRingTableEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:nmsERPSRingTableEntry.setStatus(_A)
_NmsERPSRingID_Type=Integer32
_NmsERPSRingID_Object=MibTableColumn
nmsERPSRingID=_NmsERPSRingID_Object((1,3,6,1,4,1,3320,2,231,6,1,1),_NmsERPSRingID_Type())
nmsERPSRingID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingID.setStatus(_A)
class _NmsERPSRingNodeID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NmsERPSRingNodeID_Type.__name__=_H
_NmsERPSRingNodeID_Object=MibTableColumn
nmsERPSRingNodeID=_NmsERPSRingNodeID_Object((1,3,6,1,4,1,3320,2,231,6,1,2),_NmsERPSRingNodeID_Type())
nmsERPSRingNodeID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingNodeID.setStatus(_A)
_NmsERPSRingPorts_Type=Integer32
_NmsERPSRingPorts_Object=MibTableColumn
nmsERPSRingPorts=_NmsERPSRingPorts_Object((1,3,6,1,4,1,3320,2,231,6,1,3),_NmsERPSRingPorts_Type())
nmsERPSRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPorts.setStatus(_A)
class _NmsERPSRingRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notRplOwner',0),('rplOwner',1)))
_NmsERPSRingRole_Type.__name__=_C
_NmsERPSRingRole_Object=MibTableColumn
nmsERPSRingRole=_NmsERPSRingRole_Object((1,3,6,1,4,1,3320,2,231,6,1,4),_NmsERPSRingRole_Type())
nmsERPSRingRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingRole.setStatus(_A)
class _NmsERPSRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('protection',1)))
_NmsERPSRingState_Type.__name__=_C
_NmsERPSRingState_Object=MibTableColumn
nmsERPSRingState=_NmsERPSRingState_Object((1,3,6,1,4,1,3320,2,231,6,1,5),_NmsERPSRingState_Type())
nmsERPSRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingState.setStatus(_A)
class _NmsERPSRingWTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notWaitToRestore',0),('waitToRestore',1)))
_NmsERPSRingWTR_Type.__name__=_C
_NmsERPSRingWTR_Object=MibTableColumn
nmsERPSRingWTR=_NmsERPSRingWTR_Object((1,3,6,1,4,1,3320,2,231,6,1,6),_NmsERPSRingWTR_Type())
nmsERPSRingWTR.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingWTR.setStatus(_A)
_NmsERPSRingWtrWhile_Type=Integer32
_NmsERPSRingWtrWhile_Object=MibTableColumn
nmsERPSRingWtrWhile=_NmsERPSRingWtrWhile_Object((1,3,6,1,4,1,3320,2,231,6,1,7),_NmsERPSRingWtrWhile_Type())
nmsERPSRingWtrWhile.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingWtrWhile.setStatus(_A)
class _NmsERPSRingSignalFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noSignalFail',0),('signalFail',1)))
_NmsERPSRingSignalFail_Type.__name__=_C
_NmsERPSRingSignalFail_Object=MibTableColumn
nmsERPSRingSignalFail=_NmsERPSRingSignalFail_Object((1,3,6,1,4,1,3320,2,231,6,1,8),_NmsERPSRingSignalFail_Type())
nmsERPSRingSignalFail.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingSignalFail.setStatus(_A)
class _NmsERPSRingSending_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NmsERPSRingSending_Type.__name__=_H
_NmsERPSRingSending_Object=MibTableColumn
nmsERPSRingSending=_NmsERPSRingSending_Object((1,3,6,1,4,1,3320,2,231,6,1,9),_NmsERPSRingSending_Type())
nmsERPSRingSending.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingSending.setStatus(_A)
class _NmsERPSRingRplOwnerID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NmsERPSRingRplOwnerID_Type.__name__=_H
_NmsERPSRingRplOwnerID_Object=MibTableColumn
nmsERPSRingRplOwnerID=_NmsERPSRingRplOwnerID_Object((1,3,6,1,4,1,3320,2,231,6,1,10),_NmsERPSRingRplOwnerID_Type())
nmsERPSRingRplOwnerID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingRplOwnerID.setStatus(_A)
class _NmsERPSRingRplOwnerMAC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NmsERPSRingRplOwnerMAC_Type.__name__=_H
_NmsERPSRingRplOwnerMAC_Object=MibTableColumn
nmsERPSRingRplOwnerMAC=_NmsERPSRingRplOwnerMAC_Object((1,3,6,1,4,1,3320,2,231,6,1,11),_NmsERPSRingRplOwnerMAC_Type())
nmsERPSRingRplOwnerMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingRplOwnerMAC.setStatus(_A)
class _NmsERPSRingDiscovering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notDiscovering',0),('discovering',1),(_J,2),(_K,3)))
_NmsERPSRingDiscovering_Type.__name__=_C
_NmsERPSRingDiscovering_Object=MibTableColumn
nmsERPSRingDiscovering=_NmsERPSRingDiscovering_Object((1,3,6,1,4,1,3320,2,231,6,1,12),_NmsERPSRingDiscovering_Type())
nmsERPSRingDiscovering.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingDiscovering.setStatus(_A)
_NmsERPSRingDiscoverWhile_Type=Integer32
_NmsERPSRingDiscoverWhile_Object=MibTableColumn
nmsERPSRingDiscoverWhile=_NmsERPSRingDiscoverWhile_Object((1,3,6,1,4,1,3320,2,231,6,1,13),_NmsERPSRingDiscoverWhile_Type())
nmsERPSRingDiscoverWhile.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingDiscoverWhile.setStatus(_A)
_NmsERPSRingPriorityValue_Type=Integer32
_NmsERPSRingPriorityValue_Object=MibTableColumn
nmsERPSRingPriorityValue=_NmsERPSRingPriorityValue_Object((1,3,6,1,4,1,3320,2,231,6,1,14),_NmsERPSRingPriorityValue_Type())
nmsERPSRingPriorityValue.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingPriorityValue.setStatus(_A)
_NmsERPSRingWtrTime_Type=Integer32
_NmsERPSRingWtrTime_Object=MibTableColumn
nmsERPSRingWtrTime=_NmsERPSRingWtrTime_Object((1,3,6,1,4,1,3320,2,231,6,1,15),_NmsERPSRingWtrTime_Type())
nmsERPSRingWtrTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingWtrTime.setStatus(_A)
_NmsERPSRingGuardTime_Type=Integer32
_NmsERPSRingGuardTime_Object=MibTableColumn
nmsERPSRingGuardTime=_NmsERPSRingGuardTime_Object((1,3,6,1,4,1,3320,2,231,6,1,16),_NmsERPSRingGuardTime_Type())
nmsERPSRingGuardTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingGuardTime.setStatus(_A)
_NmsERPSRingSendTime_Type=Integer32
_NmsERPSRingSendTime_Object=MibTableColumn
nmsERPSRingSendTime=_NmsERPSRingSendTime_Object((1,3,6,1,4,1,3320,2,231,6,1,17),_NmsERPSRingSendTime_Type())
nmsERPSRingSendTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingSendTime.setStatus(_A)
_NmsERPSRingDiscoveryTime_Type=Integer32
_NmsERPSRingDiscoveryTime_Object=MibTableColumn
nmsERPSRingDiscoveryTime=_NmsERPSRingDiscoveryTime_Object((1,3,6,1,4,1,3320,2,231,6,1,18),_NmsERPSRingDiscoveryTime_Type())
nmsERPSRingDiscoveryTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingDiscoveryTime.setStatus(_A)
_NmsERPSRingDpduInterval_Type=Integer32
_NmsERPSRingDpduInterval_Object=MibTableColumn
nmsERPSRingDpduInterval=_NmsERPSRingDpduInterval_Object((1,3,6,1,4,1,3320,2,231,6,1,19),_NmsERPSRingDpduInterval_Type())
nmsERPSRingDpduInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingDpduInterval.setStatus(_A)
_NmsERPSRingDiscoveryCount_Type=Integer32
_NmsERPSRingDiscoveryCount_Object=MibTableColumn
nmsERPSRingDiscoveryCount=_NmsERPSRingDiscoveryCount_Object((1,3,6,1,4,1,3320,2,231,6,1,20),_NmsERPSRingDiscoveryCount_Type())
nmsERPSRingDiscoveryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingDiscoveryCount.setStatus(_A)
_NmsERPSRingDiscoveryLastDuration_Type=Integer32
_NmsERPSRingDiscoveryLastDuration_Object=MibTableColumn
nmsERPSRingDiscoveryLastDuration=_NmsERPSRingDiscoveryLastDuration_Object((1,3,6,1,4,1,3320,2,231,6,1,21),_NmsERPSRingDiscoveryLastDuration_Type())
nmsERPSRingDiscoveryLastDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingDiscoveryLastDuration.setStatus(_A)
_NmsERPSRingDiscoveryLastElapsed_Type=Integer32
_NmsERPSRingDiscoveryLastElapsed_Object=MibTableColumn
nmsERPSRingDiscoveryLastElapsed=_NmsERPSRingDiscoveryLastElapsed_Object((1,3,6,1,4,1,3320,2,231,6,1,22),_NmsERPSRingDiscoveryLastElapsed_Type())
nmsERPSRingDiscoveryLastElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingDiscoveryLastElapsed.setStatus(_A)
class _NmsERPSRingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_NmsERPSRingAdminStatus_Type.__name__=_C
_NmsERPSRingAdminStatus_Object=MibTableColumn
nmsERPSRingAdminStatus=_NmsERPSRingAdminStatus_Object((1,3,6,1,4,1,3320,2,231,6,1,23),_NmsERPSRingAdminStatus_Type())
nmsERPSRingAdminStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:nmsERPSRingAdminStatus.setStatus(_A)
_NmsERPSRingPort1_Type=Integer32
_NmsERPSRingPort1_Object=MibTableColumn
nmsERPSRingPort1=_NmsERPSRingPort1_Object((1,3,6,1,4,1,3320,2,231,6,1,24),_NmsERPSRingPort1_Type())
nmsERPSRingPort1.setMaxAccess(_L)
if mibBuilder.loadTexts:nmsERPSRingPort1.setStatus(_A)
class _NmsERPSRingPort1AdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NmsERPSRingPort1AdminType_Type.__name__=_C
_NmsERPSRingPort1AdminType_Object=MibTableColumn
nmsERPSRingPort1AdminType=_NmsERPSRingPort1AdminType_Object((1,3,6,1,4,1,3320,2,231,6,1,25),_NmsERPSRingPort1AdminType_Type())
nmsERPSRingPort1AdminType.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingPort1AdminType.setStatus(_A)
class _NmsERPSRingPort1OperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NmsERPSRingPort1OperType_Type.__name__=_C
_NmsERPSRingPort1OperType_Object=MibTableColumn
nmsERPSRingPort1OperType=_NmsERPSRingPort1OperType_Object((1,3,6,1,4,1,3320,2,231,6,1,26),_NmsERPSRingPort1OperType_Type())
nmsERPSRingPort1OperType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPort1OperType.setStatus(_A)
class _NmsERPSRingPort1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_NmsERPSRingPort1State_Type.__name__=_C
_NmsERPSRingPort1State_Object=MibTableColumn
nmsERPSRingPort1State=_NmsERPSRingPort1State_Object((1,3,6,1,4,1,3320,2,231,6,1,27),_NmsERPSRingPort1State_Type())
nmsERPSRingPort1State.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPort1State.setStatus(_A)
class _NmsERPSRingPort1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_NmsERPSRingPort1Status_Type.__name__=_C
_NmsERPSRingPort1Status_Object=MibTableColumn
nmsERPSRingPort1Status=_NmsERPSRingPort1Status_Object((1,3,6,1,4,1,3320,2,231,6,1,28),_NmsERPSRingPort1Status_Type())
nmsERPSRingPort1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPort1Status.setStatus(_A)
_NmsERPSRingPort2_Type=Integer32
_NmsERPSRingPort2_Object=MibTableColumn
nmsERPSRingPort2=_NmsERPSRingPort2_Object((1,3,6,1,4,1,3320,2,231,6,1,29),_NmsERPSRingPort2_Type())
nmsERPSRingPort2.setMaxAccess(_L)
if mibBuilder.loadTexts:nmsERPSRingPort2.setStatus(_A)
class _NmsERPSRingPort2AdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NmsERPSRingPort2AdminType_Type.__name__=_C
_NmsERPSRingPort2AdminType_Object=MibTableColumn
nmsERPSRingPort2AdminType=_NmsERPSRingPort2AdminType_Object((1,3,6,1,4,1,3320,2,231,6,1,30),_NmsERPSRingPort2AdminType_Type())
nmsERPSRingPort2AdminType.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsERPSRingPort2AdminType.setStatus(_A)
class _NmsERPSRingPort2OperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NmsERPSRingPort2OperType_Type.__name__=_C
_NmsERPSRingPort2OperType_Object=MibTableColumn
nmsERPSRingPort2OperType=_NmsERPSRingPort2OperType_Object((1,3,6,1,4,1,3320,2,231,6,1,31),_NmsERPSRingPort2OperType_Type())
nmsERPSRingPort2OperType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPort2OperType.setStatus(_A)
class _NmsERPSRingPort2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_NmsERPSRingPort2State_Type.__name__=_C
_NmsERPSRingPort2State_Object=MibTableColumn
nmsERPSRingPort2State=_NmsERPSRingPort2State_Object((1,3,6,1,4,1,3320,2,231,6,1,32),_NmsERPSRingPort2State_Type())
nmsERPSRingPort2State.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPort2State.setStatus(_A)
class _NmsERPSRingPort2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_NmsERPSRingPort2Status_Type.__name__=_C
_NmsERPSRingPort2Status_Object=MibTableColumn
nmsERPSRingPort2Status=_NmsERPSRingPort2Status_Object((1,3,6,1,4,1,3320,2,231,6,1,33),_NmsERPSRingPort2Status_Type())
nmsERPSRingPort2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPort2Status.setStatus(_A)
_NmsERPSRingPortTable_Object=MibTable
nmsERPSRingPortTable=_NmsERPSRingPortTable_Object((1,3,6,1,4,1,3320,2,231,7))
if mibBuilder.loadTexts:nmsERPSRingPortTable.setStatus(_A)
_NmsERPSRingPortTableEntry_Object=MibTableRow
nmsERPSRingPortTableEntry=_NmsERPSRingPortTableEntry_Object((1,3,6,1,4,1,3320,2,231,7,1))
nmsERPSRingPortTableEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:nmsERPSRingPortTableEntry.setStatus(_A)
_NmsERPSRingPortRingID_Type=Integer32
_NmsERPSRingPortRingID_Object=MibTableColumn
nmsERPSRingPortRingID=_NmsERPSRingPortRingID_Object((1,3,6,1,4,1,3320,2,231,7,1,1),_NmsERPSRingPortRingID_Type())
nmsERPSRingPortRingID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortRingID.setStatus(_A)
_NmsERPSRingPort_Type=Integer32
_NmsERPSRingPort_Object=MibTableColumn
nmsERPSRingPort=_NmsERPSRingPort_Object((1,3,6,1,4,1,3320,2,231,7,1,2),_NmsERPSRingPort_Type())
nmsERPSRingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPort.setStatus(_A)
class _NmsERPSRingPortAdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NmsERPSRingPortAdminType_Type.__name__=_C
_NmsERPSRingPortAdminType_Object=MibTableColumn
nmsERPSRingPortAdminType=_NmsERPSRingPortAdminType_Object((1,3,6,1,4,1,3320,2,231,7,1,3),_NmsERPSRingPortAdminType_Type())
nmsERPSRingPortAdminType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortAdminType.setStatus(_A)
class _NmsERPSRingPortOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NmsERPSRingPortOperType_Type.__name__=_C
_NmsERPSRingPortOperType_Object=MibTableColumn
nmsERPSRingPortOperType=_NmsERPSRingPortOperType_Object((1,3,6,1,4,1,3320,2,231,7,1,4),_NmsERPSRingPortOperType_Type())
nmsERPSRingPortOperType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortOperType.setStatus(_A)
class _NmsERPSRingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_NmsERPSRingPortState_Type.__name__=_C
_NmsERPSRingPortState_Object=MibTableColumn
nmsERPSRingPortState=_NmsERPSRingPortState_Object((1,3,6,1,4,1,3320,2,231,7,1,5),_NmsERPSRingPortState_Type())
nmsERPSRingPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortState.setStatus(_A)
class _NmsERPSRingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_NmsERPSRingPortStatus_Type.__name__=_C
_NmsERPSRingPortStatus_Object=MibTableColumn
nmsERPSRingPortStatus=_NmsERPSRingPortStatus_Object((1,3,6,1,4,1,3320,2,231,7,1,6),_NmsERPSRingPortStatus_Type())
nmsERPSRingPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortStatus.setStatus(_A)
_NmsERPSRingPortForwards_Type=Integer32
_NmsERPSRingPortForwards_Object=MibTableColumn
nmsERPSRingPortForwards=_NmsERPSRingPortForwards_Object((1,3,6,1,4,1,3320,2,231,7,1,7),_NmsERPSRingPortForwards_Type())
nmsERPSRingPortForwards.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortForwards.setStatus(_A)
_NmsERPSRingPortForwardLastElapsed_Type=Integer32
_NmsERPSRingPortForwardLastElapsed_Object=MibTableColumn
nmsERPSRingPortForwardLastElapsed=_NmsERPSRingPortForwardLastElapsed_Object((1,3,6,1,4,1,3320,2,231,7,1,8),_NmsERPSRingPortForwardLastElapsed_Type())
nmsERPSRingPortForwardLastElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortForwardLastElapsed.setStatus(_A)
_NmsERPSRingPortRx_Type=Integer32
_NmsERPSRingPortRx_Object=MibTableColumn
nmsERPSRingPortRx=_NmsERPSRingPortRx_Object((1,3,6,1,4,1,3320,2,231,7,1,9),_NmsERPSRingPortRx_Type())
nmsERPSRingPortRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortRx.setStatus(_A)
_NmsERPSRingPortTx_Type=Integer32
_NmsERPSRingPortTx_Object=MibTableColumn
nmsERPSRingPortTx=_NmsERPSRingPortTx_Object((1,3,6,1,4,1,3320,2,231,7,1,10),_NmsERPSRingPortTx_Type())
nmsERPSRingPortTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsERPSRingPortTx.setStatus(_A)
_NmsERPSRingNotifications_ObjectIdentity=ObjectIdentity
nmsERPSRingNotifications=_NmsERPSRingNotifications_ObjectIdentity((1,3,6,1,4,1,3320,2,231,8))
nmsERPSRingRoleChange=NotificationType((1,3,6,1,4,1,3320,2,231,8,1))
nmsERPSRingRoleChange.setObjects(*((_D,_I),(_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:nmsERPSRingRoleChange.setStatus(_U)
nmsERPSRingStateChange=NotificationType((1,3,6,1,4,1,3320,2,231,8,2))
nmsERPSRingStateChange.setObjects(*((_D,_I),(_D,_Q),(_D,_R),(_D,_V)))
if mibBuilder.loadTexts:nmsERPSRingStateChange.setStatus(_U)
mibBuilder.exportSymbols(_D,**{'nmsERPS':nmsERPS,'nmsERPSRings':nmsERPSRings,'nmsERPSInconsistenceCheck':nmsERPSInconsistenceCheck,'nmsERPSPduRx':nmsERPSPduRx,'nmsERPSPduRxDropped':nmsERPSPduRxDropped,'nmsERPSPduTx':nmsERPSPduTx,'nmsERPSRingTable':nmsERPSRingTable,'nmsERPSRingTableEntry':nmsERPSRingTableEntry,_I:nmsERPSRingID,_Q:nmsERPSRingNodeID,'nmsERPSRingPorts':nmsERPSRingPorts,_R:nmsERPSRingRole,_V:nmsERPSRingState,'nmsERPSRingWTR':nmsERPSRingWTR,'nmsERPSRingWtrWhile':nmsERPSRingWtrWhile,'nmsERPSRingSignalFail':nmsERPSRingSignalFail,'nmsERPSRingSending':nmsERPSRingSending,'nmsERPSRingRplOwnerID':nmsERPSRingRplOwnerID,'nmsERPSRingRplOwnerMAC':nmsERPSRingRplOwnerMAC,'nmsERPSRingDiscovering':nmsERPSRingDiscovering,'nmsERPSRingDiscoverWhile':nmsERPSRingDiscoverWhile,'nmsERPSRingPriorityValue':nmsERPSRingPriorityValue,'nmsERPSRingWtrTime':nmsERPSRingWtrTime,'nmsERPSRingGuardTime':nmsERPSRingGuardTime,'nmsERPSRingSendTime':nmsERPSRingSendTime,'nmsERPSRingDiscoveryTime':nmsERPSRingDiscoveryTime,'nmsERPSRingDpduInterval':nmsERPSRingDpduInterval,'nmsERPSRingDiscoveryCount':nmsERPSRingDiscoveryCount,'nmsERPSRingDiscoveryLastDuration':nmsERPSRingDiscoveryLastDuration,'nmsERPSRingDiscoveryLastElapsed':nmsERPSRingDiscoveryLastElapsed,'nmsERPSRingAdminStatus':nmsERPSRingAdminStatus,'nmsERPSRingPort1':nmsERPSRingPort1,'nmsERPSRingPort1AdminType':nmsERPSRingPort1AdminType,'nmsERPSRingPort1OperType':nmsERPSRingPort1OperType,'nmsERPSRingPort1State':nmsERPSRingPort1State,'nmsERPSRingPort1Status':nmsERPSRingPort1Status,'nmsERPSRingPort2':nmsERPSRingPort2,'nmsERPSRingPort2AdminType':nmsERPSRingPort2AdminType,'nmsERPSRingPort2OperType':nmsERPSRingPort2OperType,'nmsERPSRingPort2State':nmsERPSRingPort2State,'nmsERPSRingPort2Status':nmsERPSRingPort2Status,'nmsERPSRingPortTable':nmsERPSRingPortTable,'nmsERPSRingPortTableEntry':nmsERPSRingPortTableEntry,_S:nmsERPSRingPortRingID,_T:nmsERPSRingPort,'nmsERPSRingPortAdminType':nmsERPSRingPortAdminType,'nmsERPSRingPortOperType':nmsERPSRingPortOperType,'nmsERPSRingPortState':nmsERPSRingPortState,'nmsERPSRingPortStatus':nmsERPSRingPortStatus,'nmsERPSRingPortForwards':nmsERPSRingPortForwards,'nmsERPSRingPortForwardLastElapsed':nmsERPSRingPortForwardLastElapsed,'nmsERPSRingPortRx':nmsERPSRingPortRx,'nmsERPSRingPortTx':nmsERPSRingPortTx,'nmsERPSRingNotifications':nmsERPSRingNotifications,'nmsERPSRingRoleChange':nmsERPSRingRoleChange,'nmsERPSRingStateChange':nmsERPSRingStateChange})