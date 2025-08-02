_I='ipadBridgePortIndex'
_H='IPAD-BRIDGE-MIB'
_G='enable'
_F='disable'
_E='yes'
_D='other'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipad,=mibBuilder.importSymbols('IPADv2-MIB','ipad')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipadBridge=ModuleIdentity((1,3,6,1,4,1,321,100,1,28))
_IpadBridgeParms_ObjectIdentity=ObjectIdentity
ipadBridgeParms=_IpadBridgeParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,28,1))
_IpadBridgeManagementMacAddress_Type=OctetString
_IpadBridgeManagementMacAddress_Object=MibScalar
ipadBridgeManagementMacAddress=_IpadBridgeManagementMacAddress_Object((1,3,6,1,4,1,321,100,1,28,1,1),_IpadBridgeManagementMacAddress_Type())
ipadBridgeManagementMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgeManagementMacAddress.setStatus(_A)
class _IpadBridgeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3)))
_IpadBridgeEnable_Type.__name__=_C
_IpadBridgeEnable_Object=MibScalar
ipadBridgeEnable=_IpadBridgeEnable_Object((1,3,6,1,4,1,321,100,1,28,1,2),_IpadBridgeEnable_Type())
ipadBridgeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgeEnable.setStatus(_A)
class _IpadBridgePortAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('addnew',2)))
_IpadBridgePortAdd_Type.__name__=_C
_IpadBridgePortAdd_Object=MibScalar
ipadBridgePortAdd=_IpadBridgePortAdd_Object((1,3,6,1,4,1,321,100,1,28,1,3),_IpadBridgePortAdd_Type())
ipadBridgePortAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgePortAdd.setStatus(_A)
_IpadBridgePortDelete_Type=Integer32
_IpadBridgePortDelete_Object=MibScalar
ipadBridgePortDelete=_IpadBridgePortDelete_Object((1,3,6,1,4,1,321,100,1,28,1,4),_IpadBridgePortDelete_Type())
ipadBridgePortDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgePortDelete.setStatus(_A)
_IpadBridgePortTable_Object=MibTable
ipadBridgePortTable=_IpadBridgePortTable_Object((1,3,6,1,4,1,321,100,1,28,2))
if mibBuilder.loadTexts:ipadBridgePortTable.setStatus(_A)
_IpadBridgePortTableEntry_Object=MibTableRow
ipadBridgePortTableEntry=_IpadBridgePortTableEntry_Object((1,3,6,1,4,1,321,100,1,28,2,1))
ipadBridgePortTableEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ipadBridgePortTableEntry.setStatus(_A)
_IpadBridgePortIndex_Type=Integer32
_IpadBridgePortIndex_Object=MibTableColumn
ipadBridgePortIndex=_IpadBridgePortIndex_Object((1,3,6,1,4,1,321,100,1,28,2,1,1),_IpadBridgePortIndex_Type())
ipadBridgePortIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:ipadBridgePortIndex.setStatus(_A)
_IpadBridgePortEndpoint_Type=DisplayString
_IpadBridgePortEndpoint_Object=MibTableColumn
ipadBridgePortEndpoint=_IpadBridgePortEndpoint_Object((1,3,6,1,4,1,321,100,1,28,2,1,2),_IpadBridgePortEndpoint_Type())
ipadBridgePortEndpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgePortEndpoint.setStatus(_A)
class _IpadBridgePortBPDUOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_F,2),(_G,3)))
_IpadBridgePortBPDUOption_Type.__name__=_C
_IpadBridgePortBPDUOption_Object=MibTableColumn
ipadBridgePortBPDUOption=_IpadBridgePortBPDUOption_Object((1,3,6,1,4,1,321,100,1,28,2,1,3),_IpadBridgePortBPDUOption_Type())
ipadBridgePortBPDUOption.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgePortBPDUOption.setStatus(_A)
class _IpadBridgePortMulticastAddrDest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no',2),(_E,3)))
_IpadBridgePortMulticastAddrDest_Type.__name__=_C
_IpadBridgePortMulticastAddrDest_Object=MibTableColumn
ipadBridgePortMulticastAddrDest=_IpadBridgePortMulticastAddrDest_Object((1,3,6,1,4,1,321,100,1,28,2,1,4),_IpadBridgePortMulticastAddrDest_Type())
ipadBridgePortMulticastAddrDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgePortMulticastAddrDest.setStatus(_A)
class _IpadBridgePortBroadcastAddrDest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no',2),(_E,3)))
_IpadBridgePortBroadcastAddrDest_Type.__name__=_C
_IpadBridgePortBroadcastAddrDest_Object=MibTableColumn
ipadBridgePortBroadcastAddrDest=_IpadBridgePortBroadcastAddrDest_Object((1,3,6,1,4,1,321,100,1,28,2,1,5),_IpadBridgePortBroadcastAddrDest_Type())
ipadBridgePortBroadcastAddrDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgePortBroadcastAddrDest.setStatus(_A)
class _IpadBridgePortForwardIpFramesOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no',2),(_E,3)))
_IpadBridgePortForwardIpFramesOnly_Type.__name__=_C
_IpadBridgePortForwardIpFramesOnly_Object=MibTableColumn
ipadBridgePortForwardIpFramesOnly=_IpadBridgePortForwardIpFramesOnly_Object((1,3,6,1,4,1,321,100,1,28,2,1,6),_IpadBridgePortForwardIpFramesOnly_Type())
ipadBridgePortForwardIpFramesOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadBridgePortForwardIpFramesOnly.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'ipadBridge':ipadBridge,'ipadBridgeParms':ipadBridgeParms,'ipadBridgeManagementMacAddress':ipadBridgeManagementMacAddress,'ipadBridgeEnable':ipadBridgeEnable,'ipadBridgePortAdd':ipadBridgePortAdd,'ipadBridgePortDelete':ipadBridgePortDelete,'ipadBridgePortTable':ipadBridgePortTable,'ipadBridgePortTableEntry':ipadBridgePortTableEntry,_I:ipadBridgePortIndex,'ipadBridgePortEndpoint':ipadBridgePortEndpoint,'ipadBridgePortBPDUOption':ipadBridgePortBPDUOption,'ipadBridgePortMulticastAddrDest':ipadBridgePortMulticastAddrDest,'ipadBridgePortBroadcastAddrDest':ipadBridgePortBroadcastAddrDest,'ipadBridgePortForwardIpFramesOnly':ipadBridgePortForwardIpFramesOnly})