_N='a3ComDot1qTpGroupAddress'
_M='a3ComUserPriority'
_L='useDefault'
_K='a3ComDot1qVlanId'
_J='not-accessible'
_I='dot1dBasePort'
_H='BRIDGE-MIB'
_G='A3COM00xx-BRIDGE-EXT-MIB'
_F='read-only'
_E='disabled'
_D='enabled'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
a3ComBridgeExt,=mibBuilder.importSymbols('A3COM0004-GENERIC','a3ComBridgeExt')
MacAddress,Timeout,dot1dBasePort=mibBuilder.importSymbols(_H,'MacAddress','Timeout',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class PortList(OctetString):0
_A3ComDot1dExtended_ObjectIdentity=ObjectIdentity
a3ComDot1dExtended=_A3ComDot1dExtended_ObjectIdentity((1,3,6,1,4,1,43,10,36,1))
_A3ComDot1dExtBase_ObjectIdentity=ObjectIdentity
a3ComDot1dExtBase=_A3ComDot1dExtBase_ObjectIdentity((1,3,6,1,4,1,43,10,36,1,1))
class _A3ComDot1dGmrpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_A3ComDot1dGmrpAdminStatus_Type.__name__=_B
_A3ComDot1dGmrpAdminStatus_Object=MibScalar
a3ComDot1dGmrpAdminStatus=_A3ComDot1dGmrpAdminStatus_Object((1,3,6,1,4,1,43,10,36,1,1,1),_A3ComDot1dGmrpAdminStatus_Type())
a3ComDot1dGmrpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDot1dGmrpAdminStatus.setStatus(_A)
class _A3ComDot1dGvrpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_A3ComDot1dGvrpAdminStatus_Type.__name__=_B
_A3ComDot1dGvrpAdminStatus_Object=MibScalar
a3ComDot1dGvrpAdminStatus=_A3ComDot1dGvrpAdminStatus_Object((1,3,6,1,4,1,43,10,36,1,1,2),_A3ComDot1dGvrpAdminStatus_Type())
a3ComDot1dGvrpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDot1dGvrpAdminStatus.setStatus(_A)
_A3ComGarpJoinTime_Type=Timeout
_A3ComGarpJoinTime_Object=MibScalar
a3ComGarpJoinTime=_A3ComGarpJoinTime_Object((1,3,6,1,4,1,43,10,36,1,1,3),_A3ComGarpJoinTime_Type())
a3ComGarpJoinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComGarpJoinTime.setStatus(_A)
_A3ComGarpLeaveTime_Type=Timeout
_A3ComGarpLeaveTime_Object=MibScalar
a3ComGarpLeaveTime=_A3ComGarpLeaveTime_Object((1,3,6,1,4,1,43,10,36,1,1,4),_A3ComGarpLeaveTime_Type())
a3ComGarpLeaveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComGarpLeaveTime.setStatus(_A)
_A3ComGarpLeaveAllTime_Type=Timeout
_A3ComGarpLeaveAllTime_Object=MibScalar
a3ComGarpLeaveAllTime=_A3ComGarpLeaveAllTime_Object((1,3,6,1,4,1,43,10,36,1,1,5),_A3ComGarpLeaveAllTime_Type())
a3ComGarpLeaveAllTime.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComGarpLeaveAllTime.setStatus(_A)
class _A3ComSingleFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_A3ComSingleFdbStatus_Type.__name__=_B
_A3ComSingleFdbStatus_Object=MibScalar
a3ComSingleFdbStatus=_A3ComSingleFdbStatus_Object((1,3,6,1,4,1,43,10,36,1,1,6),_A3ComSingleFdbStatus_Type())
a3ComSingleFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComSingleFdbStatus.setStatus(_A)
_A3ComDot1dGarp_ObjectIdentity=ObjectIdentity
a3ComDot1dGarp=_A3ComDot1dGarp_ObjectIdentity((1,3,6,1,4,1,43,10,36,1,2))
_A3ComPortGarpTable_Object=MibTable
a3ComPortGarpTable=_A3ComPortGarpTable_Object((1,3,6,1,4,1,43,10,36,1,2,1))
if mibBuilder.loadTexts:a3ComPortGarpTable.setStatus(_A)
_A3ComPortGarpEntry_Object=MibTableRow
a3ComPortGarpEntry=_A3ComPortGarpEntry_Object((1,3,6,1,4,1,43,10,36,1,2,1,1))
a3ComPortGarpEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:a3ComPortGarpEntry.setStatus(_A)
class _A3ComPortGmrpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_L,3)))
_A3ComPortGmrpAdminStatus_Type.__name__=_B
_A3ComPortGmrpAdminStatus_Object=MibTableColumn
a3ComPortGmrpAdminStatus=_A3ComPortGmrpAdminStatus_Object((1,3,6,1,4,1,43,10,36,1,2,1,1,1),_A3ComPortGmrpAdminStatus_Type())
a3ComPortGmrpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComPortGmrpAdminStatus.setStatus(_A)
class _A3ComPortGmrpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_A3ComPortGmrpOperStatus_Type.__name__=_B
_A3ComPortGmrpOperStatus_Object=MibTableColumn
a3ComPortGmrpOperStatus=_A3ComPortGmrpOperStatus_Object((1,3,6,1,4,1,43,10,36,1,2,1,1,2),_A3ComPortGmrpOperStatus_Type())
a3ComPortGmrpOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComPortGmrpOperStatus.setStatus(_A)
class _A3ComPortGvrpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_L,3)))
_A3ComPortGvrpAdminStatus_Type.__name__=_B
_A3ComPortGvrpAdminStatus_Object=MibTableColumn
a3ComPortGvrpAdminStatus=_A3ComPortGvrpAdminStatus_Object((1,3,6,1,4,1,43,10,36,1,2,1,1,3),_A3ComPortGvrpAdminStatus_Type())
a3ComPortGvrpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComPortGvrpAdminStatus.setStatus(_A)
class _A3ComPortGvrpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_A3ComPortGvrpOperStatus_Type.__name__=_B
_A3ComPortGvrpOperStatus_Object=MibTableColumn
a3ComPortGvrpOperStatus=_A3ComPortGvrpOperStatus_Object((1,3,6,1,4,1,43,10,36,1,2,1,1,4),_A3ComPortGvrpOperStatus_Type())
a3ComPortGvrpOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComPortGvrpOperStatus.setStatus(_A)
_A3ComPriority_ObjectIdentity=ObjectIdentity
a3ComPriority=_A3ComPriority_ObjectIdentity((1,3,6,1,4,1,43,10,36,1,3))
_A3ComBridgePriorityTable_Object=MibTable
a3ComBridgePriorityTable=_A3ComBridgePriorityTable_Object((1,3,6,1,4,1,43,10,36,1,3,1))
if mibBuilder.loadTexts:a3ComBridgePriorityTable.setStatus(_A)
_A3ComBridgePriorityEntry_Object=MibTableRow
a3ComBridgePriorityEntry=_A3ComBridgePriorityEntry_Object((1,3,6,1,4,1,43,10,36,1,3,1,1))
a3ComBridgePriorityEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:a3ComBridgePriorityEntry.setStatus(_A)
class _A3ComUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_A3ComUserPriority_Type.__name__=_B
_A3ComUserPriority_Object=MibTableColumn
a3ComUserPriority=_A3ComUserPriority_Object((1,3,6,1,4,1,43,10,36,1,3,1,1,1),_A3ComUserPriority_Type())
a3ComUserPriority.setMaxAccess(_J)
if mibBuilder.loadTexts:a3ComUserPriority.setStatus(_A)
class _A3ComBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_A3ComBridgePriority_Type.__name__=_B
_A3ComBridgePriority_Object=MibTableColumn
a3ComBridgePriority=_A3ComBridgePriority_Object((1,3,6,1,4,1,43,10,36,1,3,1,1,2),_A3ComBridgePriority_Type())
a3ComBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComBridgePriority.setStatus(_A)
_A3ComNeighbour_ObjectIdentity=ObjectIdentity
a3ComNeighbour=_A3ComNeighbour_ObjectIdentity((1,3,6,1,4,1,43,10,36,1,4))
_A3ComPortNeighbourTable_Object=MibTable
a3ComPortNeighbourTable=_A3ComPortNeighbourTable_Object((1,3,6,1,4,1,43,10,36,1,4,1))
if mibBuilder.loadTexts:a3ComPortNeighbourTable.setStatus(_A)
_A3ComPortNeighbourEntry_Object=MibTableRow
a3ComPortNeighbourEntry=_A3ComPortNeighbourEntry_Object((1,3,6,1,4,1,43,10,36,1,4,1,1))
a3ComPortNeighbourEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:a3ComPortNeighbourEntry.setStatus(_A)
class _A3ComPortForwardUnknownVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_A3ComPortForwardUnknownVlans_Type.__name__=_B
_A3ComPortForwardUnknownVlans_Object=MibTableColumn
a3ComPortForwardUnknownVlans=_A3ComPortForwardUnknownVlans_Object((1,3,6,1,4,1,43,10,36,1,4,1,1,1),_A3ComPortForwardUnknownVlans_Type())
a3ComPortForwardUnknownVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComPortForwardUnknownVlans.setStatus(_A)
_A3ComDot1qVlan_ObjectIdentity=ObjectIdentity
a3ComDot1qVlan=_A3ComDot1qVlan_ObjectIdentity((1,3,6,1,4,1,43,10,36,2))
_A3ComDot1qVlanStaticTable_Object=MibTable
a3ComDot1qVlanStaticTable=_A3ComDot1qVlanStaticTable_Object((1,3,6,1,4,1,43,10,36,2,1))
if mibBuilder.loadTexts:a3ComDot1qVlanStaticTable.setStatus(_A)
_A3ComDot1qVlanStaticEntry_Object=MibTableRow
a3ComDot1qVlanStaticEntry=_A3ComDot1qVlanStaticEntry_Object((1,3,6,1,4,1,43,10,36,2,1,1))
a3ComDot1qVlanStaticEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:a3ComDot1qVlanStaticEntry.setStatus(_A)
class _A3ComDot1qVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_A3ComDot1qVlanId_Type.__name__=_B
_A3ComDot1qVlanId_Object=MibTableColumn
a3ComDot1qVlanId=_A3ComDot1qVlanId_Object((1,3,6,1,4,1,43,10,36,2,1,1,1),_A3ComDot1qVlanId_Type())
a3ComDot1qVlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:a3ComDot1qVlanId.setStatus(_A)
_A3ComDot1qVlanForbiddenPorts_Type=PortList
_A3ComDot1qVlanForbiddenPorts_Object=MibTableColumn
a3ComDot1qVlanForbiddenPorts=_A3ComDot1qVlanForbiddenPorts_Object((1,3,6,1,4,1,43,10,36,2,1,1,2),_A3ComDot1qVlanForbiddenPorts_Type())
a3ComDot1qVlanForbiddenPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComDot1qVlanForbiddenPorts.setStatus(_A)
_A3ComDot1qTpGroupTable_Object=MibTable
a3ComDot1qTpGroupTable=_A3ComDot1qTpGroupTable_Object((1,3,6,1,4,1,43,10,36,2,2))
if mibBuilder.loadTexts:a3ComDot1qTpGroupTable.setStatus(_A)
_A3ComDot1qTpGroupEntry_Object=MibTableRow
a3ComDot1qTpGroupEntry=_A3ComDot1qTpGroupEntry_Object((1,3,6,1,4,1,43,10,36,2,2,1))
a3ComDot1qTpGroupEntry.setIndexNames((0,_G,_K),(0,_G,_N))
if mibBuilder.loadTexts:a3ComDot1qTpGroupEntry.setStatus(_A)
_A3ComDot1qTpGroupAddress_Type=MacAddress
_A3ComDot1qTpGroupAddress_Object=MibTableColumn
a3ComDot1qTpGroupAddress=_A3ComDot1qTpGroupAddress_Object((1,3,6,1,4,1,43,10,36,2,2,1,1),_A3ComDot1qTpGroupAddress_Type())
a3ComDot1qTpGroupAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:a3ComDot1qTpGroupAddress.setStatus(_A)
_A3ComDot1qTpGroupAllowedToGoTo_Type=PortList
_A3ComDot1qTpGroupAllowedToGoTo_Object=MibTableColumn
a3ComDot1qTpGroupAllowedToGoTo=_A3ComDot1qTpGroupAllowedToGoTo_Object((1,3,6,1,4,1,43,10,36,2,2,1,2),_A3ComDot1qTpGroupAllowedToGoTo_Type())
a3ComDot1qTpGroupAllowedToGoTo.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComDot1qTpGroupAllowedToGoTo.setStatus(_A)
_A3ComDot1qTpGroupGmrp_Type=PortList
_A3ComDot1qTpGroupGmrp_Object=MibTableColumn
a3ComDot1qTpGroupGmrp=_A3ComDot1qTpGroupGmrp_Object((1,3,6,1,4,1,43,10,36,2,2,1,3),_A3ComDot1qTpGroupGmrp_Type())
a3ComDot1qTpGroupGmrp.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComDot1qTpGroupGmrp.setStatus(_A)
_A3ComDot1qTpGroupIgmp_Type=PortList
_A3ComDot1qTpGroupIgmp_Object=MibTableColumn
a3ComDot1qTpGroupIgmp=_A3ComDot1qTpGroupIgmp_Object((1,3,6,1,4,1,43,10,36,2,2,1,4),_A3ComDot1qTpGroupIgmp_Type())
a3ComDot1qTpGroupIgmp.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComDot1qTpGroupIgmp.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'PortList':PortList,'a3ComDot1dExtended':a3ComDot1dExtended,'a3ComDot1dExtBase':a3ComDot1dExtBase,'a3ComDot1dGmrpAdminStatus':a3ComDot1dGmrpAdminStatus,'a3ComDot1dGvrpAdminStatus':a3ComDot1dGvrpAdminStatus,'a3ComGarpJoinTime':a3ComGarpJoinTime,'a3ComGarpLeaveTime':a3ComGarpLeaveTime,'a3ComGarpLeaveAllTime':a3ComGarpLeaveAllTime,'a3ComSingleFdbStatus':a3ComSingleFdbStatus,'a3ComDot1dGarp':a3ComDot1dGarp,'a3ComPortGarpTable':a3ComPortGarpTable,'a3ComPortGarpEntry':a3ComPortGarpEntry,'a3ComPortGmrpAdminStatus':a3ComPortGmrpAdminStatus,'a3ComPortGmrpOperStatus':a3ComPortGmrpOperStatus,'a3ComPortGvrpAdminStatus':a3ComPortGvrpAdminStatus,'a3ComPortGvrpOperStatus':a3ComPortGvrpOperStatus,'a3ComPriority':a3ComPriority,'a3ComBridgePriorityTable':a3ComBridgePriorityTable,'a3ComBridgePriorityEntry':a3ComBridgePriorityEntry,_M:a3ComUserPriority,'a3ComBridgePriority':a3ComBridgePriority,'a3ComNeighbour':a3ComNeighbour,'a3ComPortNeighbourTable':a3ComPortNeighbourTable,'a3ComPortNeighbourEntry':a3ComPortNeighbourEntry,'a3ComPortForwardUnknownVlans':a3ComPortForwardUnknownVlans,'a3ComDot1qVlan':a3ComDot1qVlan,'a3ComDot1qVlanStaticTable':a3ComDot1qVlanStaticTable,'a3ComDot1qVlanStaticEntry':a3ComDot1qVlanStaticEntry,_K:a3ComDot1qVlanId,'a3ComDot1qVlanForbiddenPorts':a3ComDot1qVlanForbiddenPorts,'a3ComDot1qTpGroupTable':a3ComDot1qTpGroupTable,'a3ComDot1qTpGroupEntry':a3ComDot1qTpGroupEntry,_N:a3ComDot1qTpGroupAddress,'a3ComDot1qTpGroupAllowedToGoTo':a3ComDot1qTpGroupAllowedToGoTo,'a3ComDot1qTpGroupGmrp':a3ComDot1qTpGroupGmrp,'a3ComDot1qTpGroupIgmp':a3ComDot1qTpGroupIgmp})