_O='ipadOSPFVlinkIndex'
_N='ipadOSPFAreaIndex'
_M='ipadRIPNeighborIndex'
_L='ipadRIPStaticRouteIndex'
_K='ipadRIPStaticARPIndex'
_J='ipadCircuitIndex'
_I='addnew'
_H='read-only'
_G='IPAD-ROUTER-MIB'
_F='enabled'
_E='disabled'
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
ipadRouter=ModuleIdentity((1,3,6,1,4,1,321,100,1,13))
_IpadCircuitParms_ObjectIdentity=ObjectIdentity
ipadCircuitParms=_IpadCircuitParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,13,1))
_IpadCircuitTable_Object=MibTable
ipadCircuitTable=_IpadCircuitTable_Object((1,3,6,1,4,1,321,100,1,13,1,1))
if mibBuilder.loadTexts:ipadCircuitTable.setStatus(_A)
_IpadCircuitTableEntry_Object=MibTableRow
ipadCircuitTableEntry=_IpadCircuitTableEntry_Object((1,3,6,1,4,1,321,100,1,13,1,1,1))
ipadCircuitTableEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:ipadCircuitTableEntry.setStatus(_A)
_IpadCircuitIndex_Type=Integer32
_IpadCircuitIndex_Object=MibTableColumn
ipadCircuitIndex=_IpadCircuitIndex_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,1),_IpadCircuitIndex_Type())
ipadCircuitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipadCircuitIndex.setStatus(_A)
_IpadCircuitEndpoint_Type=DisplayString
_IpadCircuitEndpoint_Object=MibTableColumn
ipadCircuitEndpoint=_IpadCircuitEndpoint_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,2),_IpadCircuitEndpoint_Type())
ipadCircuitEndpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitEndpoint.setStatus(_A)
_IpadCircuitIpAddress_Type=IpAddress
_IpadCircuitIpAddress_Object=MibTableColumn
ipadCircuitIpAddress=_IpadCircuitIpAddress_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,3),_IpadCircuitIpAddress_Type())
ipadCircuitIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitIpAddress.setStatus(_A)
_IpadCircuitIpMask_Type=IpAddress
_IpadCircuitIpMask_Object=MibTableColumn
ipadCircuitIpMask=_IpadCircuitIpMask_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,4),_IpadCircuitIpMask_Type())
ipadCircuitIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitIpMask.setStatus(_A)
class _IpadCircuitMaxTransmitUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpadCircuitMaxTransmitUnit_Type.__name__=_C
_IpadCircuitMaxTransmitUnit_Object=MibTableColumn
ipadCircuitMaxTransmitUnit=_IpadCircuitMaxTransmitUnit_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,5),_IpadCircuitMaxTransmitUnit_Type())
ipadCircuitMaxTransmitUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitMaxTransmitUnit.setStatus(_A)
class _IpadCircuitCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpadCircuitCost_Type.__name__=_C
_IpadCircuitCost_Object=MibTableColumn
ipadCircuitCost=_IpadCircuitCost_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,6),_IpadCircuitCost_Type())
ipadCircuitCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitCost.setStatus(_A)
class _IpadCircuitEnableRIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),('talkOnly',4),('listenOnly',5)))
_IpadCircuitEnableRIP_Type.__name__=_C
_IpadCircuitEnableRIP_Object=MibTableColumn
ipadCircuitEnableRIP=_IpadCircuitEnableRIP_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,7),_IpadCircuitEnableRIP_Type())
ipadCircuitEnableRIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitEnableRIP.setStatus(_A)
class _IpadCircuitEnableOSPF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadCircuitEnableOSPF_Type.__name__=_C
_IpadCircuitEnableOSPF_Object=MibTableColumn
ipadCircuitEnableOSPF=_IpadCircuitEnableOSPF_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,8),_IpadCircuitEnableOSPF_Type())
ipadCircuitEnableOSPF.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitEnableOSPF.setStatus(_A)
class _IpadCircuitEnableMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadCircuitEnableMulticast_Type.__name__=_C
_IpadCircuitEnableMulticast_Object=MibTableColumn
ipadCircuitEnableMulticast=_IpadCircuitEnableMulticast_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,9),_IpadCircuitEnableMulticast_Type())
ipadCircuitEnableMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitEnableMulticast.setStatus(_A)
class _IpadCircuitOSPFArea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_IpadCircuitOSPFArea_Type.__name__=_C
_IpadCircuitOSPFArea_Object=MibTableColumn
ipadCircuitOSPFArea=_IpadCircuitOSPFArea_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,10),_IpadCircuitOSPFArea_Type())
ipadCircuitOSPFArea.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitOSPFArea.setStatus(_A)
class _IpadCircuitOSPFLSATimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_IpadCircuitOSPFLSATimer_Type.__name__=_C
_IpadCircuitOSPFLSATimer_Object=MibTableColumn
ipadCircuitOSPFLSATimer=_IpadCircuitOSPFLSATimer_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,11),_IpadCircuitOSPFLSATimer_Type())
ipadCircuitOSPFLSATimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitOSPFLSATimer.setStatus(_A)
class _IpadCircuitOSPFLSUDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_IpadCircuitOSPFLSUDelay_Type.__name__=_C
_IpadCircuitOSPFLSUDelay_Object=MibTableColumn
ipadCircuitOSPFLSUDelay=_IpadCircuitOSPFLSUDelay_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,12),_IpadCircuitOSPFLSUDelay_Type())
ipadCircuitOSPFLSUDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitOSPFLSUDelay.setStatus(_A)
class _IpadCircuitOSPFRouterPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpadCircuitOSPFRouterPriority_Type.__name__=_C
_IpadCircuitOSPFRouterPriority_Object=MibTableColumn
ipadCircuitOSPFRouterPriority=_IpadCircuitOSPFRouterPriority_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,13),_IpadCircuitOSPFRouterPriority_Type())
ipadCircuitOSPFRouterPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitOSPFRouterPriority.setStatus(_A)
class _IpadCircuitOSPFHelloInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpadCircuitOSPFHelloInterval_Type.__name__=_C
_IpadCircuitOSPFHelloInterval_Object=MibTableColumn
ipadCircuitOSPFHelloInterval=_IpadCircuitOSPFHelloInterval_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,14),_IpadCircuitOSPFHelloInterval_Type())
ipadCircuitOSPFHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitOSPFHelloInterval.setStatus(_A)
class _IpadCircuitOSPFDeadInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpadCircuitOSPFDeadInterval_Type.__name__=_C
_IpadCircuitOSPFDeadInterval_Object=MibTableColumn
ipadCircuitOSPFDeadInterval=_IpadCircuitOSPFDeadInterval_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,15),_IpadCircuitOSPFDeadInterval_Type())
ipadCircuitOSPFDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitOSPFDeadInterval.setStatus(_A)
_IpadCircuitOSPFAuthKey_Type=DisplayString
_IpadCircuitOSPFAuthKey_Object=MibTableColumn
ipadCircuitOSPFAuthKey=_IpadCircuitOSPFAuthKey_Object((1,3,6,1,4,1,321,100,1,13,1,1,1,16),_IpadCircuitOSPFAuthKey_Type())
ipadCircuitOSPFAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitOSPFAuthKey.setStatus(_A)
class _IpadCircuitAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadCircuitAdd_Type.__name__=_C
_IpadCircuitAdd_Object=MibScalar
ipadCircuitAdd=_IpadCircuitAdd_Object((1,3,6,1,4,1,321,100,1,13,1,2),_IpadCircuitAdd_Type())
ipadCircuitAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitAdd.setStatus(_A)
_IpadCircuitDelete_Type=Integer32
_IpadCircuitDelete_Object=MibScalar
ipadCircuitDelete=_IpadCircuitDelete_Object((1,3,6,1,4,1,321,100,1,13,1,3),_IpadCircuitDelete_Type())
ipadCircuitDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadCircuitDelete.setStatus(_A)
_IpadRIPParms_ObjectIdentity=ObjectIdentity
ipadRIPParms=_IpadRIPParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,13,2))
class _IpadRIPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_E,2),('enabledRIP1',3),('enabledRIP2',4)))
_IpadRIPEnable_Type.__name__=_C
_IpadRIPEnable_Object=MibScalar
ipadRIPEnable=_IpadRIPEnable_Object((1,3,6,1,4,1,321,100,1,13,2,1),_IpadRIPEnable_Type())
ipadRIPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPEnable.setStatus(_A)
class _IpadRIPTrustNeighbors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadRIPTrustNeighbors_Type.__name__=_C
_IpadRIPTrustNeighbors_Object=MibScalar
ipadRIPTrustNeighbors=_IpadRIPTrustNeighbors_Object((1,3,6,1,4,1,321,100,1,13,2,2),_IpadRIPTrustNeighbors_Type())
ipadRIPTrustNeighbors.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPTrustNeighbors.setStatus(_A)
class _IpadRIPInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpadRIPInterval_Type.__name__=_C
_IpadRIPInterval_Object=MibScalar
ipadRIPInterval=_IpadRIPInterval_Object((1,3,6,1,4,1,321,100,1,13,2,3),_IpadRIPInterval_Type())
ipadRIPInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPInterval.setStatus(_A)
class _IpadRIPDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpadRIPDomain_Type.__name__=_C
_IpadRIPDomain_Object=MibScalar
ipadRIPDomain=_IpadRIPDomain_Object((1,3,6,1,4,1,321,100,1,13,2,4),_IpadRIPDomain_Type())
ipadRIPDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPDomain.setStatus(_A)
_IpadRIPStaticARPTable_Object=MibTable
ipadRIPStaticARPTable=_IpadRIPStaticARPTable_Object((1,3,6,1,4,1,321,100,1,13,2,5))
if mibBuilder.loadTexts:ipadRIPStaticARPTable.setStatus(_A)
_IpadRIPStaticARPTableEntry_Object=MibTableRow
ipadRIPStaticARPTableEntry=_IpadRIPStaticARPTableEntry_Object((1,3,6,1,4,1,321,100,1,13,2,5,1))
ipadRIPStaticARPTableEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:ipadRIPStaticARPTableEntry.setStatus(_A)
_IpadRIPStaticARPIndex_Type=Integer32
_IpadRIPStaticARPIndex_Object=MibTableColumn
ipadRIPStaticARPIndex=_IpadRIPStaticARPIndex_Object((1,3,6,1,4,1,321,100,1,13,2,5,1,1),_IpadRIPStaticARPIndex_Type())
ipadRIPStaticARPIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipadRIPStaticARPIndex.setStatus(_A)
_IpadRIPStaticARPEndpoint_Type=DisplayString
_IpadRIPStaticARPEndpoint_Object=MibTableColumn
ipadRIPStaticARPEndpoint=_IpadRIPStaticARPEndpoint_Object((1,3,6,1,4,1,321,100,1,13,2,5,1,2),_IpadRIPStaticARPEndpoint_Type())
ipadRIPStaticARPEndpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticARPEndpoint.setStatus(_A)
_IpadRIPStaticARPIpAddress_Type=IpAddress
_IpadRIPStaticARPIpAddress_Object=MibTableColumn
ipadRIPStaticARPIpAddress=_IpadRIPStaticARPIpAddress_Object((1,3,6,1,4,1,321,100,1,13,2,5,1,3),_IpadRIPStaticARPIpAddress_Type())
ipadRIPStaticARPIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticARPIpAddress.setStatus(_A)
_IpadRIPStaticARPMacAddress_Type=DisplayString
_IpadRIPStaticARPMacAddress_Object=MibTableColumn
ipadRIPStaticARPMacAddress=_IpadRIPStaticARPMacAddress_Object((1,3,6,1,4,1,321,100,1,13,2,5,1,4),_IpadRIPStaticARPMacAddress_Type())
ipadRIPStaticARPMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticARPMacAddress.setStatus(_A)
_IpadRIPStaticARPDLCIAddress_Type=Integer32
_IpadRIPStaticARPDLCIAddress_Object=MibTableColumn
ipadRIPStaticARPDLCIAddress=_IpadRIPStaticARPDLCIAddress_Object((1,3,6,1,4,1,321,100,1,13,2,5,1,5),_IpadRIPStaticARPDLCIAddress_Type())
ipadRIPStaticARPDLCIAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticARPDLCIAddress.setStatus(_A)
class _IpadRIPStaticARPEnableARP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadRIPStaticARPEnableARP_Type.__name__=_C
_IpadRIPStaticARPEnableARP_Object=MibTableColumn
ipadRIPStaticARPEnableARP=_IpadRIPStaticARPEnableARP_Object((1,3,6,1,4,1,321,100,1,13,2,5,1,6),_IpadRIPStaticARPEnableARP_Type())
ipadRIPStaticARPEnableARP.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticARPEnableARP.setStatus(_A)
class _IpadRIPStaticARPAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadRIPStaticARPAdd_Type.__name__=_C
_IpadRIPStaticARPAdd_Object=MibScalar
ipadRIPStaticARPAdd=_IpadRIPStaticARPAdd_Object((1,3,6,1,4,1,321,100,1,13,2,6),_IpadRIPStaticARPAdd_Type())
ipadRIPStaticARPAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticARPAdd.setStatus(_A)
_IpadRIPStaticARPDelete_Type=Integer32
_IpadRIPStaticARPDelete_Object=MibScalar
ipadRIPStaticARPDelete=_IpadRIPStaticARPDelete_Object((1,3,6,1,4,1,321,100,1,13,2,7),_IpadRIPStaticARPDelete_Type())
ipadRIPStaticARPDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticARPDelete.setStatus(_A)
_IpadRIPStaticRouteTable_Object=MibTable
ipadRIPStaticRouteTable=_IpadRIPStaticRouteTable_Object((1,3,6,1,4,1,321,100,1,13,2,8))
if mibBuilder.loadTexts:ipadRIPStaticRouteTable.setStatus(_A)
_IpadRIPStaticRouteTableEntry_Object=MibTableRow
ipadRIPStaticRouteTableEntry=_IpadRIPStaticRouteTableEntry_Object((1,3,6,1,4,1,321,100,1,13,2,8,1))
ipadRIPStaticRouteTableEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:ipadRIPStaticRouteTableEntry.setStatus(_A)
_IpadRIPStaticRouteIndex_Type=Integer32
_IpadRIPStaticRouteIndex_Object=MibTableColumn
ipadRIPStaticRouteIndex=_IpadRIPStaticRouteIndex_Object((1,3,6,1,4,1,321,100,1,13,2,8,1,1),_IpadRIPStaticRouteIndex_Type())
ipadRIPStaticRouteIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipadRIPStaticRouteIndex.setStatus(_A)
_IpadRIPStaticRouteEndpoint_Type=DisplayString
_IpadRIPStaticRouteEndpoint_Object=MibTableColumn
ipadRIPStaticRouteEndpoint=_IpadRIPStaticRouteEndpoint_Object((1,3,6,1,4,1,321,100,1,13,2,8,1,2),_IpadRIPStaticRouteEndpoint_Type())
ipadRIPStaticRouteEndpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteEndpoint.setStatus(_A)
_IpadRIPStaticRouteTargetIpAddress_Type=IpAddress
_IpadRIPStaticRouteTargetIpAddress_Object=MibTableColumn
ipadRIPStaticRouteTargetIpAddress=_IpadRIPStaticRouteTargetIpAddress_Object((1,3,6,1,4,1,321,100,1,13,2,8,1,3),_IpadRIPStaticRouteTargetIpAddress_Type())
ipadRIPStaticRouteTargetIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteTargetIpAddress.setStatus(_A)
_IpadRIPStaticRouteTargetIpMask_Type=IpAddress
_IpadRIPStaticRouteTargetIpMask_Object=MibTableColumn
ipadRIPStaticRouteTargetIpMask=_IpadRIPStaticRouteTargetIpMask_Object((1,3,6,1,4,1,321,100,1,13,2,8,1,4),_IpadRIPStaticRouteTargetIpMask_Type())
ipadRIPStaticRouteTargetIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteTargetIpMask.setStatus(_A)
_IpadRIPStaticRouteNextHopIpAddress_Type=IpAddress
_IpadRIPStaticRouteNextHopIpAddress_Object=MibTableColumn
ipadRIPStaticRouteNextHopIpAddress=_IpadRIPStaticRouteNextHopIpAddress_Object((1,3,6,1,4,1,321,100,1,13,2,8,1,5),_IpadRIPStaticRouteNextHopIpAddress_Type())
ipadRIPStaticRouteNextHopIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteNextHopIpAddress.setStatus(_A)
class _IpadRIPStaticRouteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpadRIPStaticRouteCost_Type.__name__=_C
_IpadRIPStaticRouteCost_Object=MibTableColumn
ipadRIPStaticRouteCost=_IpadRIPStaticRouteCost_Object((1,3,6,1,4,1,321,100,1,13,2,8,1,6),_IpadRIPStaticRouteCost_Type())
ipadRIPStaticRouteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteCost.setStatus(_A)
class _IpadRIPStaticRouteEnableRouter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('disable',2),('enable',3),('enableAndAdvertize',4)))
_IpadRIPStaticRouteEnableRouter_Type.__name__=_C
_IpadRIPStaticRouteEnableRouter_Object=MibTableColumn
ipadRIPStaticRouteEnableRouter=_IpadRIPStaticRouteEnableRouter_Object((1,3,6,1,4,1,321,100,1,13,2,8,1,7),_IpadRIPStaticRouteEnableRouter_Type())
ipadRIPStaticRouteEnableRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteEnableRouter.setStatus(_A)
class _IpadRIPStaticRouteAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadRIPStaticRouteAdd_Type.__name__=_C
_IpadRIPStaticRouteAdd_Object=MibScalar
ipadRIPStaticRouteAdd=_IpadRIPStaticRouteAdd_Object((1,3,6,1,4,1,321,100,1,13,2,9),_IpadRIPStaticRouteAdd_Type())
ipadRIPStaticRouteAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteAdd.setStatus(_A)
_IpadRIPStaticRouteDelete_Type=Integer32
_IpadRIPStaticRouteDelete_Object=MibScalar
ipadRIPStaticRouteDelete=_IpadRIPStaticRouteDelete_Object((1,3,6,1,4,1,321,100,1,13,2,10),_IpadRIPStaticRouteDelete_Type())
ipadRIPStaticRouteDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPStaticRouteDelete.setStatus(_A)
_IpadRIPNeighborTable_Object=MibTable
ipadRIPNeighborTable=_IpadRIPNeighborTable_Object((1,3,6,1,4,1,321,100,1,13,2,11))
if mibBuilder.loadTexts:ipadRIPNeighborTable.setStatus(_A)
_IpadRIPNeighborTableEntry_Object=MibTableRow
ipadRIPNeighborTableEntry=_IpadRIPNeighborTableEntry_Object((1,3,6,1,4,1,321,100,1,13,2,11,1))
ipadRIPNeighborTableEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:ipadRIPNeighborTableEntry.setStatus(_A)
_IpadRIPNeighborIndex_Type=Integer32
_IpadRIPNeighborIndex_Object=MibTableColumn
ipadRIPNeighborIndex=_IpadRIPNeighborIndex_Object((1,3,6,1,4,1,321,100,1,13,2,11,1,1),_IpadRIPNeighborIndex_Type())
ipadRIPNeighborIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipadRIPNeighborIndex.setStatus(_A)
_IpadRIPNeighborAddress_Type=IpAddress
_IpadRIPNeighborAddress_Object=MibTableColumn
ipadRIPNeighborAddress=_IpadRIPNeighborAddress_Object((1,3,6,1,4,1,321,100,1,13,2,11,1,2),_IpadRIPNeighborAddress_Type())
ipadRIPNeighborAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:ipadRIPNeighborAddress.setStatus(_A)
_IpadRIPNeighborAdd_Type=IpAddress
_IpadRIPNeighborAdd_Object=MibScalar
ipadRIPNeighborAdd=_IpadRIPNeighborAdd_Object((1,3,6,1,4,1,321,100,1,13,2,12),_IpadRIPNeighborAdd_Type())
ipadRIPNeighborAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPNeighborAdd.setStatus(_A)
_IpadRIPNeighborDelete_Type=IpAddress
_IpadRIPNeighborDelete_Object=MibScalar
ipadRIPNeighborDelete=_IpadRIPNeighborDelete_Object((1,3,6,1,4,1,321,100,1,13,2,13),_IpadRIPNeighborDelete_Type())
ipadRIPNeighborDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadRIPNeighborDelete.setStatus(_A)
_IpadOSPFParms_ObjectIdentity=ObjectIdentity
ipadOSPFParms=_IpadOSPFParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,13,3))
class _IpadOSPFEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadOSPFEnable_Type.__name__=_C
_IpadOSPFEnable_Object=MibScalar
ipadOSPFEnable=_IpadOSPFEnable_Object((1,3,6,1,4,1,321,100,1,13,3,1),_IpadOSPFEnable_Type())
ipadOSPFEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFEnable.setStatus(_A)
_IpadOSPFRouterID_Type=IpAddress
_IpadOSPFRouterID_Object=MibScalar
ipadOSPFRouterID=_IpadOSPFRouterID_Object((1,3,6,1,4,1,321,100,1,13,3,2),_IpadOSPFRouterID_Type())
ipadOSPFRouterID.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFRouterID.setStatus(_A)
_IpadOSPFAreaTable_Object=MibTable
ipadOSPFAreaTable=_IpadOSPFAreaTable_Object((1,3,6,1,4,1,321,100,1,13,3,3))
if mibBuilder.loadTexts:ipadOSPFAreaTable.setStatus(_A)
_IpadOSPFAreaTableEntry_Object=MibTableRow
ipadOSPFAreaTableEntry=_IpadOSPFAreaTableEntry_Object((1,3,6,1,4,1,321,100,1,13,3,3,1))
ipadOSPFAreaTableEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:ipadOSPFAreaTableEntry.setStatus(_A)
_IpadOSPFAreaIndex_Type=Integer32
_IpadOSPFAreaIndex_Object=MibTableColumn
ipadOSPFAreaIndex=_IpadOSPFAreaIndex_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,1),_IpadOSPFAreaIndex_Type())
ipadOSPFAreaIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipadOSPFAreaIndex.setStatus(_A)
_IpadOSPFAreaID_Type=IpAddress
_IpadOSPFAreaID_Object=MibTableColumn
ipadOSPFAreaID=_IpadOSPFAreaID_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,2),_IpadOSPFAreaID_Type())
ipadOSPFAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaID.setStatus(_A)
class _IpadOSPFAreaEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadOSPFAreaEnable_Type.__name__=_C
_IpadOSPFAreaEnable_Object=MibTableColumn
ipadOSPFAreaEnable=_IpadOSPFAreaEnable_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,3),_IpadOSPFAreaEnable_Type())
ipadOSPFAreaEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaEnable.setStatus(_A)
class _IpadOSPFAreaAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('simple',2)))
_IpadOSPFAreaAuthType_Type.__name__=_C
_IpadOSPFAreaAuthType_Object=MibTableColumn
ipadOSPFAreaAuthType=_IpadOSPFAreaAuthType_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,4),_IpadOSPFAreaAuthType_Type())
ipadOSPFAreaAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaAuthType.setStatus(_A)
class _IpadOSPFAreaStub_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('no',2),('yes',3)))
_IpadOSPFAreaStub_Type.__name__=_C
_IpadOSPFAreaStub_Object=MibTableColumn
ipadOSPFAreaStub=_IpadOSPFAreaStub_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,5),_IpadOSPFAreaStub_Type())
ipadOSPFAreaStub.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaStub.setStatus(_A)
_IpadOSPFAreaAddrSummary_Type=IpAddress
_IpadOSPFAreaAddrSummary_Object=MibTableColumn
ipadOSPFAreaAddrSummary=_IpadOSPFAreaAddrSummary_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,6),_IpadOSPFAreaAddrSummary_Type())
ipadOSPFAreaAddrSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaAddrSummary.setStatus(_A)
_IpadOSPFAreaMaskSummary_Type=IpAddress
_IpadOSPFAreaMaskSummary_Object=MibTableColumn
ipadOSPFAreaMaskSummary=_IpadOSPFAreaMaskSummary_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,7),_IpadOSPFAreaMaskSummary_Type())
ipadOSPFAreaMaskSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaMaskSummary.setStatus(_A)
class _IpadOSPFAreaAdvertise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadOSPFAreaAdvertise_Type.__name__=_C
_IpadOSPFAreaAdvertise_Object=MibTableColumn
ipadOSPFAreaAdvertise=_IpadOSPFAreaAdvertise_Object((1,3,6,1,4,1,321,100,1,13,3,3,1,8),_IpadOSPFAreaAdvertise_Type())
ipadOSPFAreaAdvertise.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaAdvertise.setStatus(_A)
class _IpadOSPFAreaAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadOSPFAreaAdd_Type.__name__=_C
_IpadOSPFAreaAdd_Object=MibScalar
ipadOSPFAreaAdd=_IpadOSPFAreaAdd_Object((1,3,6,1,4,1,321,100,1,13,3,4),_IpadOSPFAreaAdd_Type())
ipadOSPFAreaAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaAdd.setStatus(_A)
_IpadOSPFAreaDelete_Type=Integer32
_IpadOSPFAreaDelete_Object=MibScalar
ipadOSPFAreaDelete=_IpadOSPFAreaDelete_Object((1,3,6,1,4,1,321,100,1,13,3,5),_IpadOSPFAreaDelete_Type())
ipadOSPFAreaDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFAreaDelete.setStatus(_A)
_IpadOSPFVlinkTable_Object=MibTable
ipadOSPFVlinkTable=_IpadOSPFVlinkTable_Object((1,3,6,1,4,1,321,100,1,13,3,6))
if mibBuilder.loadTexts:ipadOSPFVlinkTable.setStatus(_A)
_IpadOSPFVlinkTableEntry_Object=MibTableRow
ipadOSPFVlinkTableEntry=_IpadOSPFVlinkTableEntry_Object((1,3,6,1,4,1,321,100,1,13,3,6,1))
ipadOSPFVlinkTableEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:ipadOSPFVlinkTableEntry.setStatus(_A)
_IpadOSPFVlinkIndex_Type=Integer32
_IpadOSPFVlinkIndex_Object=MibTableColumn
ipadOSPFVlinkIndex=_IpadOSPFVlinkIndex_Object((1,3,6,1,4,1,321,100,1,13,3,6,1,1),_IpadOSPFVlinkIndex_Type())
ipadOSPFVlinkIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipadOSPFVlinkIndex.setStatus(_A)
class _IpadOSPFVlinkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_IpadOSPFVlinkEnable_Type.__name__=_C
_IpadOSPFVlinkEnable_Object=MibTableColumn
ipadOSPFVlinkEnable=_IpadOSPFVlinkEnable_Object((1,3,6,1,4,1,321,100,1,13,3,6,1,2),_IpadOSPFVlinkEnable_Type())
ipadOSPFVlinkEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFVlinkEnable.setStatus(_A)
_IpadOSPFVlinkTransitAreaID_Type=IpAddress
_IpadOSPFVlinkTransitAreaID_Object=MibTableColumn
ipadOSPFVlinkTransitAreaID=_IpadOSPFVlinkTransitAreaID_Object((1,3,6,1,4,1,321,100,1,13,3,6,1,3),_IpadOSPFVlinkTransitAreaID_Type())
ipadOSPFVlinkTransitAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFVlinkTransitAreaID.setStatus(_A)
_IpadOSPFVlinkAreaBorderRouterID_Type=IpAddress
_IpadOSPFVlinkAreaBorderRouterID_Object=MibTableColumn
ipadOSPFVlinkAreaBorderRouterID=_IpadOSPFVlinkAreaBorderRouterID_Object((1,3,6,1,4,1,321,100,1,13,3,6,1,4),_IpadOSPFVlinkAreaBorderRouterID_Type())
ipadOSPFVlinkAreaBorderRouterID.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFVlinkAreaBorderRouterID.setStatus(_A)
class _IpadOSPFVlinkAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadOSPFVlinkAdd_Type.__name__=_C
_IpadOSPFVlinkAdd_Object=MibScalar
ipadOSPFVlinkAdd=_IpadOSPFVlinkAdd_Object((1,3,6,1,4,1,321,100,1,13,3,7),_IpadOSPFVlinkAdd_Type())
ipadOSPFVlinkAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFVlinkAdd.setStatus(_A)
_IpadOSPFVlinkDelete_Type=Integer32
_IpadOSPFVlinkDelete_Object=MibScalar
ipadOSPFVlinkDelete=_IpadOSPFVlinkDelete_Object((1,3,6,1,4,1,321,100,1,13,3,8),_IpadOSPFVlinkDelete_Type())
ipadOSPFVlinkDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadOSPFVlinkDelete.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ipadRouter':ipadRouter,'ipadCircuitParms':ipadCircuitParms,'ipadCircuitTable':ipadCircuitTable,'ipadCircuitTableEntry':ipadCircuitTableEntry,_J:ipadCircuitIndex,'ipadCircuitEndpoint':ipadCircuitEndpoint,'ipadCircuitIpAddress':ipadCircuitIpAddress,'ipadCircuitIpMask':ipadCircuitIpMask,'ipadCircuitMaxTransmitUnit':ipadCircuitMaxTransmitUnit,'ipadCircuitCost':ipadCircuitCost,'ipadCircuitEnableRIP':ipadCircuitEnableRIP,'ipadCircuitEnableOSPF':ipadCircuitEnableOSPF,'ipadCircuitEnableMulticast':ipadCircuitEnableMulticast,'ipadCircuitOSPFArea':ipadCircuitOSPFArea,'ipadCircuitOSPFLSATimer':ipadCircuitOSPFLSATimer,'ipadCircuitOSPFLSUDelay':ipadCircuitOSPFLSUDelay,'ipadCircuitOSPFRouterPriority':ipadCircuitOSPFRouterPriority,'ipadCircuitOSPFHelloInterval':ipadCircuitOSPFHelloInterval,'ipadCircuitOSPFDeadInterval':ipadCircuitOSPFDeadInterval,'ipadCircuitOSPFAuthKey':ipadCircuitOSPFAuthKey,'ipadCircuitAdd':ipadCircuitAdd,'ipadCircuitDelete':ipadCircuitDelete,'ipadRIPParms':ipadRIPParms,'ipadRIPEnable':ipadRIPEnable,'ipadRIPTrustNeighbors':ipadRIPTrustNeighbors,'ipadRIPInterval':ipadRIPInterval,'ipadRIPDomain':ipadRIPDomain,'ipadRIPStaticARPTable':ipadRIPStaticARPTable,'ipadRIPStaticARPTableEntry':ipadRIPStaticARPTableEntry,_K:ipadRIPStaticARPIndex,'ipadRIPStaticARPEndpoint':ipadRIPStaticARPEndpoint,'ipadRIPStaticARPIpAddress':ipadRIPStaticARPIpAddress,'ipadRIPStaticARPMacAddress':ipadRIPStaticARPMacAddress,'ipadRIPStaticARPDLCIAddress':ipadRIPStaticARPDLCIAddress,'ipadRIPStaticARPEnableARP':ipadRIPStaticARPEnableARP,'ipadRIPStaticARPAdd':ipadRIPStaticARPAdd,'ipadRIPStaticARPDelete':ipadRIPStaticARPDelete,'ipadRIPStaticRouteTable':ipadRIPStaticRouteTable,'ipadRIPStaticRouteTableEntry':ipadRIPStaticRouteTableEntry,_L:ipadRIPStaticRouteIndex,'ipadRIPStaticRouteEndpoint':ipadRIPStaticRouteEndpoint,'ipadRIPStaticRouteTargetIpAddress':ipadRIPStaticRouteTargetIpAddress,'ipadRIPStaticRouteTargetIpMask':ipadRIPStaticRouteTargetIpMask,'ipadRIPStaticRouteNextHopIpAddress':ipadRIPStaticRouteNextHopIpAddress,'ipadRIPStaticRouteCost':ipadRIPStaticRouteCost,'ipadRIPStaticRouteEnableRouter':ipadRIPStaticRouteEnableRouter,'ipadRIPStaticRouteAdd':ipadRIPStaticRouteAdd,'ipadRIPStaticRouteDelete':ipadRIPStaticRouteDelete,'ipadRIPNeighborTable':ipadRIPNeighborTable,'ipadRIPNeighborTableEntry':ipadRIPNeighborTableEntry,_M:ipadRIPNeighborIndex,'ipadRIPNeighborAddress':ipadRIPNeighborAddress,'ipadRIPNeighborAdd':ipadRIPNeighborAdd,'ipadRIPNeighborDelete':ipadRIPNeighborDelete,'ipadOSPFParms':ipadOSPFParms,'ipadOSPFEnable':ipadOSPFEnable,'ipadOSPFRouterID':ipadOSPFRouterID,'ipadOSPFAreaTable':ipadOSPFAreaTable,'ipadOSPFAreaTableEntry':ipadOSPFAreaTableEntry,_N:ipadOSPFAreaIndex,'ipadOSPFAreaID':ipadOSPFAreaID,'ipadOSPFAreaEnable':ipadOSPFAreaEnable,'ipadOSPFAreaAuthType':ipadOSPFAreaAuthType,'ipadOSPFAreaStub':ipadOSPFAreaStub,'ipadOSPFAreaAddrSummary':ipadOSPFAreaAddrSummary,'ipadOSPFAreaMaskSummary':ipadOSPFAreaMaskSummary,'ipadOSPFAreaAdvertise':ipadOSPFAreaAdvertise,'ipadOSPFAreaAdd':ipadOSPFAreaAdd,'ipadOSPFAreaDelete':ipadOSPFAreaDelete,'ipadOSPFVlinkTable':ipadOSPFVlinkTable,'ipadOSPFVlinkTableEntry':ipadOSPFVlinkTableEntry,_O:ipadOSPFVlinkIndex,'ipadOSPFVlinkEnable':ipadOSPFVlinkEnable,'ipadOSPFVlinkTransitAreaID':ipadOSPFVlinkTransitAreaID,'ipadOSPFVlinkAreaBorderRouterID':ipadOSPFVlinkAreaBorderRouterID,'ipadOSPFVlinkAdd':ipadOSPFVlinkAdd,'ipadOSPFVlinkDelete':ipadOSPFVlinkDelete})