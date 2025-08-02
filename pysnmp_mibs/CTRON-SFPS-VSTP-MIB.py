_G='vlanSpanningTreeSwitchIndex'
_F='vlanSpanningTreePortPortNumber'
_E='Integer32'
_D='CTRON-SFPS-VSTP-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vlanSpanningTreePort,vlanSpanningTreeSwitch=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','vlanSpanningTreePort','vlanSpanningTreeSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsSwitchPort(Integer32):0
class HexInteger(Integer32):0
_VlanSpanningTreePortTable_Object=MibTable
vlanSpanningTreePortTable=_VlanSpanningTreePortTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1))
if mibBuilder.loadTexts:vlanSpanningTreePortTable.setStatus(_A)
_VlanSpanningTreePortEntry_Object=MibTableRow
vlanSpanningTreePortEntry=_VlanSpanningTreePortEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1))
vlanSpanningTreePortEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:vlanSpanningTreePortEntry.setStatus(_A)
_VlanSpanningTreePortPortNumber_Type=SfpsSwitchPort
_VlanSpanningTreePortPortNumber_Object=MibTableColumn
vlanSpanningTreePortPortNumber=_VlanSpanningTreePortPortNumber_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,1),_VlanSpanningTreePortPortNumber_Type())
vlanSpanningTreePortPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreePortPortNumber.setStatus(_A)
class _VlanSpanningTreePortPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('blocking',3),('listening',4),('learning',5),('forwarding',6),('broken',7)))
_VlanSpanningTreePortPortState_Type.__name__=_E
_VlanSpanningTreePortPortState_Object=MibTableColumn
vlanSpanningTreePortPortState=_VlanSpanningTreePortPortState_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,2),_VlanSpanningTreePortPortState_Type())
vlanSpanningTreePortPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreePortPortState.setStatus(_A)
_VlanSpanningTreePortPortIdentifier_Type=HexInteger
_VlanSpanningTreePortPortIdentifier_Object=MibTableColumn
vlanSpanningTreePortPortIdentifier=_VlanSpanningTreePortPortIdentifier_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,3),_VlanSpanningTreePortPortIdentifier_Type())
vlanSpanningTreePortPortIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreePortPortIdentifier.setStatus(_A)
_VlanSpanningTreePortPathCost_Type=Integer32
_VlanSpanningTreePortPathCost_Object=MibTableColumn
vlanSpanningTreePortPathCost=_VlanSpanningTreePortPathCost_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,4),_VlanSpanningTreePortPathCost_Type())
vlanSpanningTreePortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpanningTreePortPathCost.setStatus(_A)
_VlanSpanningTreePortDesignatedRoot_Type=OctetString
_VlanSpanningTreePortDesignatedRoot_Object=MibTableColumn
vlanSpanningTreePortDesignatedRoot=_VlanSpanningTreePortDesignatedRoot_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,5),_VlanSpanningTreePortDesignatedRoot_Type())
vlanSpanningTreePortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreePortDesignatedRoot.setStatus(_A)
_VlanSpanningTreePortDesignatedCost_Type=Integer32
_VlanSpanningTreePortDesignatedCost_Object=MibTableColumn
vlanSpanningTreePortDesignatedCost=_VlanSpanningTreePortDesignatedCost_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,6),_VlanSpanningTreePortDesignatedCost_Type())
vlanSpanningTreePortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreePortDesignatedCost.setStatus(_A)
_VlanSpanningTreePortDesignatedBridge_Type=OctetString
_VlanSpanningTreePortDesignatedBridge_Object=MibTableColumn
vlanSpanningTreePortDesignatedBridge=_VlanSpanningTreePortDesignatedBridge_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,7),_VlanSpanningTreePortDesignatedBridge_Type())
vlanSpanningTreePortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreePortDesignatedBridge.setStatus(_A)
_VlanSpanningTreePortDesignatedPort_Type=HexInteger
_VlanSpanningTreePortDesignatedPort_Object=MibTableColumn
vlanSpanningTreePortDesignatedPort=_VlanSpanningTreePortDesignatedPort_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,1,1,1,8),_VlanSpanningTreePortDesignatedPort_Type())
vlanSpanningTreePortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreePortDesignatedPort.setStatus(_A)
_VlanSpanningTreeSwitchTable_Object=MibTable
vlanSpanningTreeSwitchTable=_VlanSpanningTreeSwitchTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1))
if mibBuilder.loadTexts:vlanSpanningTreeSwitchTable.setStatus(_A)
_VlanSpanningTreeSwitchEntry_Object=MibTableRow
vlanSpanningTreeSwitchEntry=_VlanSpanningTreeSwitchEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1))
vlanSpanningTreeSwitchEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:vlanSpanningTreeSwitchEntry.setStatus(_A)
_VlanSpanningTreeSwitchIndex_Type=Integer32
_VlanSpanningTreeSwitchIndex_Object=MibTableColumn
vlanSpanningTreeSwitchIndex=_VlanSpanningTreeSwitchIndex_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,1),_VlanSpanningTreeSwitchIndex_Type())
vlanSpanningTreeSwitchIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchIndex.setStatus(_A)
_VlanSpanningTreeSwitchBridgePriority_Type=HexInteger
_VlanSpanningTreeSwitchBridgePriority_Object=MibTableColumn
vlanSpanningTreeSwitchBridgePriority=_VlanSpanningTreeSwitchBridgePriority_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,2),_VlanSpanningTreeSwitchBridgePriority_Type())
vlanSpanningTreeSwitchBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchBridgePriority.setStatus(_A)
_VlanSpanningTreeSwitchBridgeId_Type=OctetString
_VlanSpanningTreeSwitchBridgeId_Object=MibTableColumn
vlanSpanningTreeSwitchBridgeId=_VlanSpanningTreeSwitchBridgeId_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,3),_VlanSpanningTreeSwitchBridgeId_Type())
vlanSpanningTreeSwitchBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchBridgeId.setStatus(_A)
_VlanSpanningTreeSwitchDesignatedRoot_Type=OctetString
_VlanSpanningTreeSwitchDesignatedRoot_Object=MibTableColumn
vlanSpanningTreeSwitchDesignatedRoot=_VlanSpanningTreeSwitchDesignatedRoot_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,4),_VlanSpanningTreeSwitchDesignatedRoot_Type())
vlanSpanningTreeSwitchDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchDesignatedRoot.setStatus(_A)
_VlanSpanningTreeSwitchRootPathCost_Type=Integer32
_VlanSpanningTreeSwitchRootPathCost_Object=MibTableColumn
vlanSpanningTreeSwitchRootPathCost=_VlanSpanningTreeSwitchRootPathCost_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,5),_VlanSpanningTreeSwitchRootPathCost_Type())
vlanSpanningTreeSwitchRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchRootPathCost.setStatus(_A)
_VlanSpanningTreeSwitchOperTime_Type=TimeTicks
_VlanSpanningTreeSwitchOperTime_Object=MibTableColumn
vlanSpanningTreeSwitchOperTime=_VlanSpanningTreeSwitchOperTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,6),_VlanSpanningTreeSwitchOperTime_Type())
vlanSpanningTreeSwitchOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchOperTime.setStatus(_A)
_VlanSpanningTreeSwitchRootPort_Type=SfpsSwitchPort
_VlanSpanningTreeSwitchRootPort_Object=MibTableColumn
vlanSpanningTreeSwitchRootPort=_VlanSpanningTreeSwitchRootPort_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,7),_VlanSpanningTreeSwitchRootPort_Type())
vlanSpanningTreeSwitchRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchRootPort.setStatus(_A)
_VlanSpanningTreeSwitchRootPortTime_Type=TimeTicks
_VlanSpanningTreeSwitchRootPortTime_Object=MibTableColumn
vlanSpanningTreeSwitchRootPortTime=_VlanSpanningTreeSwitchRootPortTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,8),_VlanSpanningTreeSwitchRootPortTime_Type())
vlanSpanningTreeSwitchRootPortTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchRootPortTime.setStatus(_A)
_VlanSpanningTreeSwitchPrevRootPort_Type=SfpsSwitchPort
_VlanSpanningTreeSwitchPrevRootPort_Object=MibTableColumn
vlanSpanningTreeSwitchPrevRootPort=_VlanSpanningTreeSwitchPrevRootPort_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,9),_VlanSpanningTreeSwitchPrevRootPort_Type())
vlanSpanningTreeSwitchPrevRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchPrevRootPort.setStatus(_A)
_VlanSpanningTreeSwitchPrevRootPortTime_Type=TimeTicks
_VlanSpanningTreeSwitchPrevRootPortTime_Object=MibTableColumn
vlanSpanningTreeSwitchPrevRootPortTime=_VlanSpanningTreeSwitchPrevRootPortTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,10),_VlanSpanningTreeSwitchPrevRootPortTime_Type())
vlanSpanningTreeSwitchPrevRootPortTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchPrevRootPortTime.setStatus(_A)
_VlanSpanningTreeSwitchMaxAge_Type=Integer32
_VlanSpanningTreeSwitchMaxAge_Object=MibTableColumn
vlanSpanningTreeSwitchMaxAge=_VlanSpanningTreeSwitchMaxAge_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,11),_VlanSpanningTreeSwitchMaxAge_Type())
vlanSpanningTreeSwitchMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchMaxAge.setStatus(_A)
_VlanSpanningTreeSwitchHelloTime_Type=Integer32
_VlanSpanningTreeSwitchHelloTime_Object=MibTableColumn
vlanSpanningTreeSwitchHelloTime=_VlanSpanningTreeSwitchHelloTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,12),_VlanSpanningTreeSwitchHelloTime_Type())
vlanSpanningTreeSwitchHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchHelloTime.setStatus(_A)
_VlanSpanningTreeSwitchForwardDelay_Type=Integer32
_VlanSpanningTreeSwitchForwardDelay_Object=MibTableColumn
vlanSpanningTreeSwitchForwardDelay=_VlanSpanningTreeSwitchForwardDelay_Object((1,3,6,1,4,1,52,4,2,12,1,2,8,2,1,1,13),_VlanSpanningTreeSwitchForwardDelay_Type())
vlanSpanningTreeSwitchForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpanningTreeSwitchForwardDelay.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SfpsSwitchPort':SfpsSwitchPort,'HexInteger':HexInteger,'vlanSpanningTreePortTable':vlanSpanningTreePortTable,'vlanSpanningTreePortEntry':vlanSpanningTreePortEntry,_F:vlanSpanningTreePortPortNumber,'vlanSpanningTreePortPortState':vlanSpanningTreePortPortState,'vlanSpanningTreePortPortIdentifier':vlanSpanningTreePortPortIdentifier,'vlanSpanningTreePortPathCost':vlanSpanningTreePortPathCost,'vlanSpanningTreePortDesignatedRoot':vlanSpanningTreePortDesignatedRoot,'vlanSpanningTreePortDesignatedCost':vlanSpanningTreePortDesignatedCost,'vlanSpanningTreePortDesignatedBridge':vlanSpanningTreePortDesignatedBridge,'vlanSpanningTreePortDesignatedPort':vlanSpanningTreePortDesignatedPort,'vlanSpanningTreeSwitchTable':vlanSpanningTreeSwitchTable,'vlanSpanningTreeSwitchEntry':vlanSpanningTreeSwitchEntry,_G:vlanSpanningTreeSwitchIndex,'vlanSpanningTreeSwitchBridgePriority':vlanSpanningTreeSwitchBridgePriority,'vlanSpanningTreeSwitchBridgeId':vlanSpanningTreeSwitchBridgeId,'vlanSpanningTreeSwitchDesignatedRoot':vlanSpanningTreeSwitchDesignatedRoot,'vlanSpanningTreeSwitchRootPathCost':vlanSpanningTreeSwitchRootPathCost,'vlanSpanningTreeSwitchOperTime':vlanSpanningTreeSwitchOperTime,'vlanSpanningTreeSwitchRootPort':vlanSpanningTreeSwitchRootPort,'vlanSpanningTreeSwitchRootPortTime':vlanSpanningTreeSwitchRootPortTime,'vlanSpanningTreeSwitchPrevRootPort':vlanSpanningTreeSwitchPrevRootPort,'vlanSpanningTreeSwitchPrevRootPortTime':vlanSpanningTreeSwitchPrevRootPortTime,'vlanSpanningTreeSwitchMaxAge':vlanSpanningTreeSwitchMaxAge,'vlanSpanningTreeSwitchHelloTime':vlanSpanningTreeSwitchHelloTime,'vlanSpanningTreeSwitchForwardDelay':vlanSpanningTreeSwitchForwardDelay})