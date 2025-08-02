_R='nmsEAPSRingState'
_Q='nmsEAPSRingNodeType'
_P='nmsEAPSRingPort'
_O='nmsEAPSRingPortRingID'
_N='enabled'
_M='disabled'
_L='link-up'
_K='link-down'
_J='blocking'
_I='preforwarding'
_H='forwarding'
_G='nmsEAPSRingID'
_F='unknown'
_E='read-write'
_D='QTECH-NMS-EAPS-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmslocal,=mibBuilder.importSymbols('QTECH-NMS-SMI','nmslocal')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_NmsEAPS_ObjectIdentity=ObjectIdentity
nmsEAPS=_NmsEAPS_ObjectIdentity((1,3,6,1,4,1,34751,2,230))
_NmsEAPSRings_Type=Integer32
_NmsEAPSRings_Object=MibScalar
nmsEAPSRings=_NmsEAPSRings_Object((1,3,6,1,4,1,34751,2,230,1),_NmsEAPSRings_Type())
nmsEAPSRings.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRings.setStatus(_A)
_NmsEAPSPduRx_Type=Integer32
_NmsEAPSPduRx_Object=MibScalar
nmsEAPSPduRx=_NmsEAPSPduRx_Object((1,3,6,1,4,1,34751,2,230,2),_NmsEAPSPduRx_Type())
nmsEAPSPduRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSPduRx.setStatus(_A)
_NmsEAPSPduTx_Type=Integer32
_NmsEAPSPduTx_Object=MibScalar
nmsEAPSPduTx=_NmsEAPSPduTx_Object((1,3,6,1,4,1,34751,2,230,3),_NmsEAPSPduTx_Type())
nmsEAPSPduTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSPduTx.setStatus(_A)
_NmsEAPSRingTable_Object=MibTable
nmsEAPSRingTable=_NmsEAPSRingTable_Object((1,3,6,1,4,1,34751,2,230,4))
if mibBuilder.loadTexts:nmsEAPSRingTable.setStatus(_A)
_NmsEAPSRingTableEntry_Object=MibTableRow
nmsEAPSRingTableEntry=_NmsEAPSRingTableEntry_Object((1,3,6,1,4,1,34751,2,230,4,1))
nmsEAPSRingTableEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:nmsEAPSRingTableEntry.setStatus(_A)
_NmsEAPSRingID_Type=Integer32
_NmsEAPSRingID_Object=MibTableColumn
nmsEAPSRingID=_NmsEAPSRingID_Object((1,3,6,1,4,1,34751,2,230,4,1,1),_NmsEAPSRingID_Type())
nmsEAPSRingID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingID.setStatus(_A)
class _NmsEAPSRingNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('masterNode',1),('transitNode',2)))
_NmsEAPSRingNodeType_Type.__name__=_C
_NmsEAPSRingNodeType_Object=MibTableColumn
nmsEAPSRingNodeType=_NmsEAPSRingNodeType_Object((1,3,6,1,4,1,34751,2,230,4,1,2),_NmsEAPSRingNodeType_Type())
nmsEAPSRingNodeType.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsEAPSRingNodeType.setStatus(_A)
_NmsEAPSRingControlVlan_Type=Integer32
_NmsEAPSRingControlVlan_Object=MibTableColumn
nmsEAPSRingControlVlan=_NmsEAPSRingControlVlan_Object((1,3,6,1,4,1,34751,2,230,4,1,3),_NmsEAPSRingControlVlan_Type())
nmsEAPSRingControlVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsEAPSRingControlVlan.setStatus(_A)
_NmsEAPSRingPorts_Type=Integer32
_NmsEAPSRingPorts_Object=MibTableColumn
nmsEAPSRingPorts=_NmsEAPSRingPorts_Object((1,3,6,1,4,1,34751,2,230,4,1,4),_NmsEAPSRingPorts_Type())
nmsEAPSRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPorts.setStatus(_A)
class _NmsEAPSRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('complete',1),('ringFault',2)))
_NmsEAPSRingState_Type.__name__=_C
_NmsEAPSRingState_Object=MibTableColumn
nmsEAPSRingState=_NmsEAPSRingState_Object((1,3,6,1,4,1,34751,2,230,4,1,5),_NmsEAPSRingState_Type())
nmsEAPSRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingState.setStatus(_A)
class _NmsEAPSRingHealthCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_NmsEAPSRingHealthCheck_Type.__name__=_C
_NmsEAPSRingHealthCheck_Object=MibTableColumn
nmsEAPSRingHealthCheck=_NmsEAPSRingHealthCheck_Object((1,3,6,1,4,1,34751,2,230,4,1,6),_NmsEAPSRingHealthCheck_Type())
nmsEAPSRingHealthCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingHealthCheck.setStatus(_A)
_NmsEAPSRingHelloTime_Type=Integer32
_NmsEAPSRingHelloTime_Object=MibTableColumn
nmsEAPSRingHelloTime=_NmsEAPSRingHelloTime_Object((1,3,6,1,4,1,34751,2,230,4,1,7),_NmsEAPSRingHelloTime_Type())
nmsEAPSRingHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsEAPSRingHelloTime.setStatus(_A)
_NmsEAPSRingFailTime_Type=Integer32
_NmsEAPSRingFailTime_Object=MibTableColumn
nmsEAPSRingFailTime=_NmsEAPSRingFailTime_Object((1,3,6,1,4,1,34751,2,230,4,1,8),_NmsEAPSRingFailTime_Type())
nmsEAPSRingFailTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsEAPSRingFailTime.setStatus(_A)
_NmsEAPSRingPreforwardTime_Type=Integer32
_NmsEAPSRingPreforwardTime_Object=MibTableColumn
nmsEAPSRingPreforwardTime=_NmsEAPSRingPreforwardTime_Object((1,3,6,1,4,1,34751,2,230,4,1,9),_NmsEAPSRingPreforwardTime_Type())
nmsEAPSRingPreforwardTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsEAPSRingPreforwardTime.setStatus(_A)
class _NmsEAPSRingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),('running',2)))
_NmsEAPSRingAdminStatus_Type.__name__=_C
_NmsEAPSRingAdminStatus_Object=MibTableColumn
nmsEAPSRingAdminStatus=_NmsEAPSRingAdminStatus_Object((1,3,6,1,4,1,34751,2,230,4,1,10),_NmsEAPSRingAdminStatus_Type())
nmsEAPSRingAdminStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:nmsEAPSRingAdminStatus.setStatus(_A)
_NmsEAPSRingPrimaryPort_Type=Integer32
_NmsEAPSRingPrimaryPort_Object=MibTableColumn
nmsEAPSRingPrimaryPort=_NmsEAPSRingPrimaryPort_Object((1,3,6,1,4,1,34751,2,230,4,1,11),_NmsEAPSRingPrimaryPort_Type())
nmsEAPSRingPrimaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsEAPSRingPrimaryPort.setStatus(_A)
class _NmsEAPSRingPrimaryPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2),(_J,3)))
_NmsEAPSRingPrimaryPortState_Type.__name__=_C
_NmsEAPSRingPrimaryPortState_Object=MibTableColumn
nmsEAPSRingPrimaryPortState=_NmsEAPSRingPrimaryPortState_Object((1,3,6,1,4,1,34751,2,230,4,1,12),_NmsEAPSRingPrimaryPortState_Type())
nmsEAPSRingPrimaryPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPrimaryPortState.setStatus(_A)
class _NmsEAPSRingPrimaryPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_NmsEAPSRingPrimaryPortStatus_Type.__name__=_C
_NmsEAPSRingPrimaryPortStatus_Object=MibTableColumn
nmsEAPSRingPrimaryPortStatus=_NmsEAPSRingPrimaryPortStatus_Object((1,3,6,1,4,1,34751,2,230,4,1,13),_NmsEAPSRingPrimaryPortStatus_Type())
nmsEAPSRingPrimaryPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPrimaryPortStatus.setStatus(_A)
_NmsEAPSRingSecondaryPort_Type=Integer32
_NmsEAPSRingSecondaryPort_Object=MibTableColumn
nmsEAPSRingSecondaryPort=_NmsEAPSRingSecondaryPort_Object((1,3,6,1,4,1,34751,2,230,4,1,14),_NmsEAPSRingSecondaryPort_Type())
nmsEAPSRingSecondaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:nmsEAPSRingSecondaryPort.setStatus(_A)
class _NmsEAPSRingSecondaryPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2),(_J,3)))
_NmsEAPSRingSecondaryPortState_Type.__name__=_C
_NmsEAPSRingSecondaryPortState_Object=MibTableColumn
nmsEAPSRingSecondaryPortState=_NmsEAPSRingSecondaryPortState_Object((1,3,6,1,4,1,34751,2,230,4,1,15),_NmsEAPSRingSecondaryPortState_Type())
nmsEAPSRingSecondaryPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingSecondaryPortState.setStatus(_A)
class _NmsEAPSRingSecondaryPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_NmsEAPSRingSecondaryPortStatus_Type.__name__=_C
_NmsEAPSRingSecondaryPortStatus_Object=MibTableColumn
nmsEAPSRingSecondaryPortStatus=_NmsEAPSRingSecondaryPortStatus_Object((1,3,6,1,4,1,34751,2,230,4,1,16),_NmsEAPSRingSecondaryPortStatus_Type())
nmsEAPSRingSecondaryPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingSecondaryPortStatus.setStatus(_A)
_NmsEAPSRingPortTable_Object=MibTable
nmsEAPSRingPortTable=_NmsEAPSRingPortTable_Object((1,3,6,1,4,1,34751,2,230,5))
if mibBuilder.loadTexts:nmsEAPSRingPortTable.setStatus(_A)
_NmsEAPSRingPortTableEntry_Object=MibTableRow
nmsEAPSRingPortTableEntry=_NmsEAPSRingPortTableEntry_Object((1,3,6,1,4,1,34751,2,230,5,1))
nmsEAPSRingPortTableEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:nmsEAPSRingPortTableEntry.setStatus(_A)
_NmsEAPSRingPortRingID_Type=Integer32
_NmsEAPSRingPortRingID_Object=MibTableColumn
nmsEAPSRingPortRingID=_NmsEAPSRingPortRingID_Object((1,3,6,1,4,1,34751,2,230,5,1,1),_NmsEAPSRingPortRingID_Type())
nmsEAPSRingPortRingID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPortRingID.setStatus(_A)
_NmsEAPSRingPort_Type=Integer32
_NmsEAPSRingPort_Object=MibTableColumn
nmsEAPSRingPort=_NmsEAPSRingPort_Object((1,3,6,1,4,1,34751,2,230,5,1,2),_NmsEAPSRingPort_Type())
nmsEAPSRingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPort.setStatus(_A)
class _NmsEAPSRingPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('primaryPort',1),('secondaryPort',2),('transitPort',3)))
_NmsEAPSRingPortType_Type.__name__=_C
_NmsEAPSRingPortType_Object=MibTableColumn
nmsEAPSRingPortType=_NmsEAPSRingPortType_Object((1,3,6,1,4,1,34751,2,230,5,1,3),_NmsEAPSRingPortType_Type())
nmsEAPSRingPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPortType.setStatus(_A)
class _NmsEAPSRingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2),(_J,3)))
_NmsEAPSRingPortState_Type.__name__=_C
_NmsEAPSRingPortState_Object=MibTableColumn
nmsEAPSRingPortState=_NmsEAPSRingPortState_Object((1,3,6,1,4,1,34751,2,230,5,1,4),_NmsEAPSRingPortState_Type())
nmsEAPSRingPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPortState.setStatus(_A)
_NmsEAPSRingPortForwards_Type=Integer32
_NmsEAPSRingPortForwards_Object=MibTableColumn
nmsEAPSRingPortForwards=_NmsEAPSRingPortForwards_Object((1,3,6,1,4,1,34751,2,230,5,1,5),_NmsEAPSRingPortForwards_Type())
nmsEAPSRingPortForwards.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPortForwards.setStatus(_A)
_NmsEAPSRingPortRx_Type=Integer32
_NmsEAPSRingPortRx_Object=MibTableColumn
nmsEAPSRingPortRx=_NmsEAPSRingPortRx_Object((1,3,6,1,4,1,34751,2,230,5,1,6),_NmsEAPSRingPortRx_Type())
nmsEAPSRingPortRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPortRx.setStatus(_A)
_NmsEAPSRingPortTx_Type=Integer32
_NmsEAPSRingPortTx_Object=MibTableColumn
nmsEAPSRingPortTx=_NmsEAPSRingPortTx_Object((1,3,6,1,4,1,34751,2,230,5,1,7),_NmsEAPSRingPortTx_Type())
nmsEAPSRingPortTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPortTx.setStatus(_A)
class _NmsEAPSRingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_NmsEAPSRingPortStatus_Type.__name__=_C
_NmsEAPSRingPortStatus_Object=MibTableColumn
nmsEAPSRingPortStatus=_NmsEAPSRingPortStatus_Object((1,3,6,1,4,1,34751,2,230,5,1,8),_NmsEAPSRingPortStatus_Type())
nmsEAPSRingPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsEAPSRingPortStatus.setStatus(_A)
_NmsEAPSRingNotifications_ObjectIdentity=ObjectIdentity
nmsEAPSRingNotifications=_NmsEAPSRingNotifications_ObjectIdentity((1,3,6,1,4,1,34751,2,230,6))
nmsEAPSRingNotification=NotificationType((1,3,6,1,4,1,34751,2,230,6,1))
nmsEAPSRingNotification.setObjects(*((_D,_G),(_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:nmsEAPSRingNotification.setStatus('current')
mibBuilder.exportSymbols(_D,**{'nmsEAPS':nmsEAPS,'nmsEAPSRings':nmsEAPSRings,'nmsEAPSPduRx':nmsEAPSPduRx,'nmsEAPSPduTx':nmsEAPSPduTx,'nmsEAPSRingTable':nmsEAPSRingTable,'nmsEAPSRingTableEntry':nmsEAPSRingTableEntry,_G:nmsEAPSRingID,_Q:nmsEAPSRingNodeType,'nmsEAPSRingControlVlan':nmsEAPSRingControlVlan,'nmsEAPSRingPorts':nmsEAPSRingPorts,_R:nmsEAPSRingState,'nmsEAPSRingHealthCheck':nmsEAPSRingHealthCheck,'nmsEAPSRingHelloTime':nmsEAPSRingHelloTime,'nmsEAPSRingFailTime':nmsEAPSRingFailTime,'nmsEAPSRingPreforwardTime':nmsEAPSRingPreforwardTime,'nmsEAPSRingAdminStatus':nmsEAPSRingAdminStatus,'nmsEAPSRingPrimaryPort':nmsEAPSRingPrimaryPort,'nmsEAPSRingPrimaryPortState':nmsEAPSRingPrimaryPortState,'nmsEAPSRingPrimaryPortStatus':nmsEAPSRingPrimaryPortStatus,'nmsEAPSRingSecondaryPort':nmsEAPSRingSecondaryPort,'nmsEAPSRingSecondaryPortState':nmsEAPSRingSecondaryPortState,'nmsEAPSRingSecondaryPortStatus':nmsEAPSRingSecondaryPortStatus,'nmsEAPSRingPortTable':nmsEAPSRingPortTable,'nmsEAPSRingPortTableEntry':nmsEAPSRingPortTableEntry,_O:nmsEAPSRingPortRingID,_P:nmsEAPSRingPort,'nmsEAPSRingPortType':nmsEAPSRingPortType,'nmsEAPSRingPortState':nmsEAPSRingPortState,'nmsEAPSRingPortForwards':nmsEAPSRingPortForwards,'nmsEAPSRingPortRx':nmsEAPSRingPortRx,'nmsEAPSRingPortTx':nmsEAPSRingPortTx,'nmsEAPSRingPortStatus':nmsEAPSRingPortStatus,'nmsEAPSRingNotifications':nmsEAPSRingNotifications,'nmsEAPSRingNotification':nmsEAPSRingNotification})