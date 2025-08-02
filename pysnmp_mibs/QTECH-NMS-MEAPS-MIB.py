_V='nmsMEAPSRingState'
_U='nmsMEAPSRingNodeType'
_T='nmsMEAPSRingPort'
_S='nmsMEAPSRingPortRingID'
_R='read-create'
_Q='running'
_P='nmsMEAPSDomainID'
_O='link-up'
_N='link-down'
_M='edgepreforwarding'
_L='blocking'
_K='preforwarding'
_J='forwarding'
_I='nmsMEAPSRingID'
_H='enabled'
_G='disabled'
_F='unknown'
_E='QTECH-NMS-MEAPS-MIB'
_D='read-write'
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
_NmsMEAPS_ObjectIdentity=ObjectIdentity
nmsMEAPS=_NmsMEAPS_ObjectIdentity((1,3,6,1,4,1,34751,2,234))
_NmsMEAPSDomains_Type=Integer32
_NmsMEAPSDomains_Object=MibScalar
nmsMEAPSDomains=_NmsMEAPSDomains_Object((1,3,6,1,4,1,34751,2,234,1),_NmsMEAPSDomains_Type())
nmsMEAPSDomains.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSDomains.setStatus(_A)
_NmsMEAPSPduRx_Type=Integer32
_NmsMEAPSPduRx_Object=MibScalar
nmsMEAPSPduRx=_NmsMEAPSPduRx_Object((1,3,6,1,4,1,34751,2,234,2),_NmsMEAPSPduRx_Type())
nmsMEAPSPduRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSPduRx.setStatus(_A)
_NmsMEAPSPduTx_Type=Integer32
_NmsMEAPSPduTx_Object=MibScalar
nmsMEAPSPduTx=_NmsMEAPSPduTx_Object((1,3,6,1,4,1,34751,2,234,3),_NmsMEAPSPduTx_Type())
nmsMEAPSPduTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSPduTx.setStatus(_A)
_NmsMEAPSDomainTable_Object=MibTable
nmsMEAPSDomainTable=_NmsMEAPSDomainTable_Object((1,3,6,1,4,1,34751,2,234,4))
if mibBuilder.loadTexts:nmsMEAPSDomainTable.setStatus(_A)
_NmsMEAPSDomainTableEntry_Object=MibTableRow
nmsMEAPSDomainTableEntry=_NmsMEAPSDomainTableEntry_Object((1,3,6,1,4,1,34751,2,234,4,1))
nmsMEAPSDomainTableEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:nmsMEAPSDomainTableEntry.setStatus(_A)
_NmsMEAPSDomainID_Type=Integer32
_NmsMEAPSDomainID_Object=MibTableColumn
nmsMEAPSDomainID=_NmsMEAPSDomainID_Object((1,3,6,1,4,1,34751,2,234,4,1,1),_NmsMEAPSDomainID_Type())
nmsMEAPSDomainID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSDomainID.setStatus(_A)
_NmsMEAPSRings_Type=Integer32
_NmsMEAPSRings_Object=MibTableColumn
nmsMEAPSRings=_NmsMEAPSRings_Object((1,3,6,1,4,1,34751,2,234,4,1,2),_NmsMEAPSRings_Type())
nmsMEAPSRings.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRings.setStatus(_A)
class _NmsMEAPSRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_Q,2)))
_NmsMEAPSRowStatus_Type.__name__=_C
_NmsMEAPSRowStatus_Object=MibTableColumn
nmsMEAPSRowStatus=_NmsMEAPSRowStatus_Object((1,3,6,1,4,1,34751,2,234,4,1,3),_NmsMEAPSRowStatus_Type())
nmsMEAPSRowStatus.setMaxAccess(_R)
if mibBuilder.loadTexts:nmsMEAPSRowStatus.setStatus(_A)
_NmsMEAPSRingTable_Object=MibTable
nmsMEAPSRingTable=_NmsMEAPSRingTable_Object((1,3,6,1,4,1,34751,2,234,5))
if mibBuilder.loadTexts:nmsMEAPSRingTable.setStatus(_A)
_NmsMEAPSRingTableEntry_Object=MibTableRow
nmsMEAPSRingTableEntry=_NmsMEAPSRingTableEntry_Object((1,3,6,1,4,1,34751,2,234,5,1))
nmsMEAPSRingTableEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:nmsMEAPSRingTableEntry.setStatus(_A)
_NmsMEAPSRingID_Type=Integer32
_NmsMEAPSRingID_Object=MibTableColumn
nmsMEAPSRingID=_NmsMEAPSRingID_Object((1,3,6,1,4,1,34751,2,234,5,1,1),_NmsMEAPSRingID_Type())
nmsMEAPSRingID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingID.setStatus(_A)
class _NmsMEAPSRingLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('majorRing',1),('subRing',2)))
_NmsMEAPSRingLevel_Type.__name__=_C
_NmsMEAPSRingLevel_Object=MibTableColumn
nmsMEAPSRingLevel=_NmsMEAPSRingLevel_Object((1,3,6,1,4,1,34751,2,234,5,1,2),_NmsMEAPSRingLevel_Type())
nmsMEAPSRingLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingLevel.setStatus(_A)
class _NmsMEAPSRingNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),('masterNode',1),('transitNode',2),('edgeNode',3),('assistantNode',4)))
_NmsMEAPSRingNodeType_Type.__name__=_C
_NmsMEAPSRingNodeType_Object=MibTableColumn
nmsMEAPSRingNodeType=_NmsMEAPSRingNodeType_Object((1,3,6,1,4,1,34751,2,234,5,1,3),_NmsMEAPSRingNodeType_Type())
nmsMEAPSRingNodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingNodeType.setStatus(_A)
_NmsMEAPSRingControlVlanMajor_Type=Integer32
_NmsMEAPSRingControlVlanMajor_Object=MibTableColumn
nmsMEAPSRingControlVlanMajor=_NmsMEAPSRingControlVlanMajor_Object((1,3,6,1,4,1,34751,2,234,5,1,4),_NmsMEAPSRingControlVlanMajor_Type())
nmsMEAPSRingControlVlanMajor.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingControlVlanMajor.setStatus(_A)
_NmsMEAPSRingControlVlanSub_Type=Integer32
_NmsMEAPSRingControlVlanSub_Object=MibTableColumn
nmsMEAPSRingControlVlanSub=_NmsMEAPSRingControlVlanSub_Object((1,3,6,1,4,1,34751,2,234,5,1,5),_NmsMEAPSRingControlVlanSub_Type())
nmsMEAPSRingControlVlanSub.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingControlVlanSub.setStatus(_A)
_NmsMEAPSRingPorts_Type=Integer32
_NmsMEAPSRingPorts_Object=MibTableColumn
nmsMEAPSRingPorts=_NmsMEAPSRingPorts_Object((1,3,6,1,4,1,34751,2,234,5,1,6),_NmsMEAPSRingPorts_Type())
nmsMEAPSRingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPorts.setStatus(_A)
class _NmsMEAPSRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('complete',1),('ringFault',2)))
_NmsMEAPSRingState_Type.__name__=_C
_NmsMEAPSRingState_Object=MibTableColumn
nmsMEAPSRingState=_NmsMEAPSRingState_Object((1,3,6,1,4,1,34751,2,234,5,1,7),_NmsMEAPSRingState_Type())
nmsMEAPSRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingState.setStatus(_A)
class _NmsMEAPSRingHealthCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_NmsMEAPSRingHealthCheck_Type.__name__=_C
_NmsMEAPSRingHealthCheck_Object=MibTableColumn
nmsMEAPSRingHealthCheck=_NmsMEAPSRingHealthCheck_Object((1,3,6,1,4,1,34751,2,234,5,1,8),_NmsMEAPSRingHealthCheck_Type())
nmsMEAPSRingHealthCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingHealthCheck.setStatus(_A)
_NmsMEAPSRingHelloTime_Type=Integer32
_NmsMEAPSRingHelloTime_Object=MibTableColumn
nmsMEAPSRingHelloTime=_NmsMEAPSRingHelloTime_Object((1,3,6,1,4,1,34751,2,234,5,1,9),_NmsMEAPSRingHelloTime_Type())
nmsMEAPSRingHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingHelloTime.setStatus(_A)
_NmsMEAPSRingFailTime_Type=Integer32
_NmsMEAPSRingFailTime_Object=MibTableColumn
nmsMEAPSRingFailTime=_NmsMEAPSRingFailTime_Object((1,3,6,1,4,1,34751,2,234,5,1,10),_NmsMEAPSRingFailTime_Type())
nmsMEAPSRingFailTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingFailTime.setStatus(_A)
_NmsMEAPSRingPreforwardTime_Type=Integer32
_NmsMEAPSRingPreforwardTime_Object=MibTableColumn
nmsMEAPSRingPreforwardTime=_NmsMEAPSRingPreforwardTime_Object((1,3,6,1,4,1,34751,2,234,5,1,11),_NmsMEAPSRingPreforwardTime_Type())
nmsMEAPSRingPreforwardTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingPreforwardTime.setStatus(_A)
_NmsMEAPSRingEdgeHelloTime_Type=Integer32
_NmsMEAPSRingEdgeHelloTime_Object=MibTableColumn
nmsMEAPSRingEdgeHelloTime=_NmsMEAPSRingEdgeHelloTime_Object((1,3,6,1,4,1,34751,2,234,5,1,12),_NmsMEAPSRingEdgeHelloTime_Type())
nmsMEAPSRingEdgeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingEdgeHelloTime.setStatus(_A)
_NmsMEAPSRingEdgeFailTime_Type=Integer32
_NmsMEAPSRingEdgeFailTime_Object=MibTableColumn
nmsMEAPSRingEdgeFailTime=_NmsMEAPSRingEdgeFailTime_Object((1,3,6,1,4,1,34751,2,234,5,1,13),_NmsMEAPSRingEdgeFailTime_Type())
nmsMEAPSRingEdgeFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingEdgeFailTime.setStatus(_A)
class _NmsMEAPSRingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_Q,2)))
_NmsMEAPSRingAdminStatus_Type.__name__=_C
_NmsMEAPSRingAdminStatus_Object=MibTableColumn
nmsMEAPSRingAdminStatus=_NmsMEAPSRingAdminStatus_Object((1,3,6,1,4,1,34751,2,234,5,1,14),_NmsMEAPSRingAdminStatus_Type())
nmsMEAPSRingAdminStatus.setMaxAccess(_R)
if mibBuilder.loadTexts:nmsMEAPSRingAdminStatus.setStatus(_A)
_NmsMEAPSRingPrimaryPort_Type=Integer32
_NmsMEAPSRingPrimaryPort_Object=MibTableColumn
nmsMEAPSRingPrimaryPort=_NmsMEAPSRingPrimaryPort_Object((1,3,6,1,4,1,34751,2,234,5,1,15),_NmsMEAPSRingPrimaryPort_Type())
nmsMEAPSRingPrimaryPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingPrimaryPort.setStatus(_A)
class _NmsMEAPSRingPrimaryPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_J,1),(_K,2),(_L,3),(_M,4)))
_NmsMEAPSRingPrimaryPortState_Type.__name__=_C
_NmsMEAPSRingPrimaryPortState_Object=MibTableColumn
nmsMEAPSRingPrimaryPortState=_NmsMEAPSRingPrimaryPortState_Object((1,3,6,1,4,1,34751,2,234,5,1,16),_NmsMEAPSRingPrimaryPortState_Type())
nmsMEAPSRingPrimaryPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPrimaryPortState.setStatus(_A)
class _NmsMEAPSRingPrimaryPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NmsMEAPSRingPrimaryPortStatus_Type.__name__=_C
_NmsMEAPSRingPrimaryPortStatus_Object=MibTableColumn
nmsMEAPSRingPrimaryPortStatus=_NmsMEAPSRingPrimaryPortStatus_Object((1,3,6,1,4,1,34751,2,234,5,1,17),_NmsMEAPSRingPrimaryPortStatus_Type())
nmsMEAPSRingPrimaryPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPrimaryPortStatus.setStatus(_A)
_NmsMEAPSRingSecondaryPort_Type=Integer32
_NmsMEAPSRingSecondaryPort_Object=MibTableColumn
nmsMEAPSRingSecondaryPort=_NmsMEAPSRingSecondaryPort_Object((1,3,6,1,4,1,34751,2,234,5,1,18),_NmsMEAPSRingSecondaryPort_Type())
nmsMEAPSRingSecondaryPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsMEAPSRingSecondaryPort.setStatus(_A)
class _NmsMEAPSRingSecondaryPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_J,1),(_K,2),(_L,3),(_M,4)))
_NmsMEAPSRingSecondaryPortState_Type.__name__=_C
_NmsMEAPSRingSecondaryPortState_Object=MibTableColumn
nmsMEAPSRingSecondaryPortState=_NmsMEAPSRingSecondaryPortState_Object((1,3,6,1,4,1,34751,2,234,5,1,19),_NmsMEAPSRingSecondaryPortState_Type())
nmsMEAPSRingSecondaryPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingSecondaryPortState.setStatus(_A)
class _NmsMEAPSRingSecondaryPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NmsMEAPSRingSecondaryPortStatus_Type.__name__=_C
_NmsMEAPSRingSecondaryPortStatus_Object=MibTableColumn
nmsMEAPSRingSecondaryPortStatus=_NmsMEAPSRingSecondaryPortStatus_Object((1,3,6,1,4,1,34751,2,234,5,1,20),_NmsMEAPSRingSecondaryPortStatus_Type())
nmsMEAPSRingSecondaryPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingSecondaryPortStatus.setStatus(_A)
_NmsMEAPSRingPortTable_Object=MibTable
nmsMEAPSRingPortTable=_NmsMEAPSRingPortTable_Object((1,3,6,1,4,1,34751,2,234,6))
if mibBuilder.loadTexts:nmsMEAPSRingPortTable.setStatus(_A)
_NmsMEAPSRingPortTableEntry_Object=MibTableRow
nmsMEAPSRingPortTableEntry=_NmsMEAPSRingPortTableEntry_Object((1,3,6,1,4,1,34751,2,234,6,1))
nmsMEAPSRingPortTableEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:nmsMEAPSRingPortTableEntry.setStatus(_A)
_NmsMEAPSRingPortRingID_Type=Integer32
_NmsMEAPSRingPortRingID_Object=MibTableColumn
nmsMEAPSRingPortRingID=_NmsMEAPSRingPortRingID_Object((1,3,6,1,4,1,34751,2,234,6,1,1),_NmsMEAPSRingPortRingID_Type())
nmsMEAPSRingPortRingID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPortRingID.setStatus(_A)
_NmsMEAPSRingPort_Type=Integer32
_NmsMEAPSRingPort_Object=MibTableColumn
nmsMEAPSRingPort=_NmsMEAPSRingPort_Object((1,3,6,1,4,1,34751,2,234,6,1,2),_NmsMEAPSRingPort_Type())
nmsMEAPSRingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPort.setStatus(_A)
class _NmsMEAPSRingPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),('primaryPort',1),('secondaryPort',2),('transitPort',3),('commonPort',4),('edgePort',5)))
_NmsMEAPSRingPortType_Type.__name__=_C
_NmsMEAPSRingPortType_Object=MibTableColumn
nmsMEAPSRingPortType=_NmsMEAPSRingPortType_Object((1,3,6,1,4,1,34751,2,234,6,1,3),_NmsMEAPSRingPortType_Type())
nmsMEAPSRingPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPortType.setStatus(_A)
class _NmsMEAPSRingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_J,1),(_K,2),(_L,3),(_M,4)))
_NmsMEAPSRingPortState_Type.__name__=_C
_NmsMEAPSRingPortState_Object=MibTableColumn
nmsMEAPSRingPortState=_NmsMEAPSRingPortState_Object((1,3,6,1,4,1,34751,2,234,6,1,4),_NmsMEAPSRingPortState_Type())
nmsMEAPSRingPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPortState.setStatus(_A)
_NmsMEAPSRingPortForwards_Type=Integer32
_NmsMEAPSRingPortForwards_Object=MibTableColumn
nmsMEAPSRingPortForwards=_NmsMEAPSRingPortForwards_Object((1,3,6,1,4,1,34751,2,234,6,1,5),_NmsMEAPSRingPortForwards_Type())
nmsMEAPSRingPortForwards.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPortForwards.setStatus(_A)
_NmsMEAPSRingPortRx_Type=Integer32
_NmsMEAPSRingPortRx_Object=MibTableColumn
nmsMEAPSRingPortRx=_NmsMEAPSRingPortRx_Object((1,3,6,1,4,1,34751,2,234,6,1,6),_NmsMEAPSRingPortRx_Type())
nmsMEAPSRingPortRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPortRx.setStatus(_A)
_NmsMEAPSRingPortTx_Type=Integer32
_NmsMEAPSRingPortTx_Object=MibTableColumn
nmsMEAPSRingPortTx=_NmsMEAPSRingPortTx_Object((1,3,6,1,4,1,34751,2,234,6,1,7),_NmsMEAPSRingPortTx_Type())
nmsMEAPSRingPortTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPortTx.setStatus(_A)
class _NmsMEAPSRingPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NmsMEAPSRingPortStatus_Type.__name__=_C
_NmsMEAPSRingPortStatus_Object=MibTableColumn
nmsMEAPSRingPortStatus=_NmsMEAPSRingPortStatus_Object((1,3,6,1,4,1,34751,2,234,6,1,8),_NmsMEAPSRingPortStatus_Type())
nmsMEAPSRingPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsMEAPSRingPortStatus.setStatus(_A)
_NmsMEAPSRingNotifications_ObjectIdentity=ObjectIdentity
nmsMEAPSRingNotifications=_NmsMEAPSRingNotifications_ObjectIdentity((1,3,6,1,4,1,34751,2,234,7))
nmsMEAPSRingNotification=NotificationType((1,3,6,1,4,1,34751,2,234,7,1))
nmsMEAPSRingNotification.setObjects(*((_E,_I),(_E,_U),(_E,_V)))
if mibBuilder.loadTexts:nmsMEAPSRingNotification.setStatus('current')
mibBuilder.exportSymbols(_E,**{'nmsMEAPS':nmsMEAPS,'nmsMEAPSDomains':nmsMEAPSDomains,'nmsMEAPSPduRx':nmsMEAPSPduRx,'nmsMEAPSPduTx':nmsMEAPSPduTx,'nmsMEAPSDomainTable':nmsMEAPSDomainTable,'nmsMEAPSDomainTableEntry':nmsMEAPSDomainTableEntry,_P:nmsMEAPSDomainID,'nmsMEAPSRings':nmsMEAPSRings,'nmsMEAPSRowStatus':nmsMEAPSRowStatus,'nmsMEAPSRingTable':nmsMEAPSRingTable,'nmsMEAPSRingTableEntry':nmsMEAPSRingTableEntry,_I:nmsMEAPSRingID,'nmsMEAPSRingLevel':nmsMEAPSRingLevel,_U:nmsMEAPSRingNodeType,'nmsMEAPSRingControlVlanMajor':nmsMEAPSRingControlVlanMajor,'nmsMEAPSRingControlVlanSub':nmsMEAPSRingControlVlanSub,'nmsMEAPSRingPorts':nmsMEAPSRingPorts,_V:nmsMEAPSRingState,'nmsMEAPSRingHealthCheck':nmsMEAPSRingHealthCheck,'nmsMEAPSRingHelloTime':nmsMEAPSRingHelloTime,'nmsMEAPSRingFailTime':nmsMEAPSRingFailTime,'nmsMEAPSRingPreforwardTime':nmsMEAPSRingPreforwardTime,'nmsMEAPSRingEdgeHelloTime':nmsMEAPSRingEdgeHelloTime,'nmsMEAPSRingEdgeFailTime':nmsMEAPSRingEdgeFailTime,'nmsMEAPSRingAdminStatus':nmsMEAPSRingAdminStatus,'nmsMEAPSRingPrimaryPort':nmsMEAPSRingPrimaryPort,'nmsMEAPSRingPrimaryPortState':nmsMEAPSRingPrimaryPortState,'nmsMEAPSRingPrimaryPortStatus':nmsMEAPSRingPrimaryPortStatus,'nmsMEAPSRingSecondaryPort':nmsMEAPSRingSecondaryPort,'nmsMEAPSRingSecondaryPortState':nmsMEAPSRingSecondaryPortState,'nmsMEAPSRingSecondaryPortStatus':nmsMEAPSRingSecondaryPortStatus,'nmsMEAPSRingPortTable':nmsMEAPSRingPortTable,'nmsMEAPSRingPortTableEntry':nmsMEAPSRingPortTableEntry,_S:nmsMEAPSRingPortRingID,_T:nmsMEAPSRingPort,'nmsMEAPSRingPortType':nmsMEAPSRingPortType,'nmsMEAPSRingPortState':nmsMEAPSRingPortState,'nmsMEAPSRingPortForwards':nmsMEAPSRingPortForwards,'nmsMEAPSRingPortRx':nmsMEAPSRingPortRx,'nmsMEAPSRingPortTx':nmsMEAPSRingPortTx,'nmsMEAPSRingPortStatus':nmsMEAPSRingPortStatus,'nmsMEAPSRingNotifications':nmsMEAPSRingNotifications,'nmsMEAPSRingNotification':nmsMEAPSRingNotification})