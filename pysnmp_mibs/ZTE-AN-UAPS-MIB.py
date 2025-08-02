_R='zxAnUapsGroupIndex'
_Q='not-accessible'
_P='DisplayString'
_O='zxAnUapsSecondaryPortList'
_N='zxAnUapsPrimaryPortList'
_M='zxAnUapsGroupName'
_L='zxAnUapsSwapReason'
_K='zxAnUapsPortWorkingStatus'
_J='forceSwap'
_I='failoverByIpLinkDown'
_H='failoverByPhyLinkDown'
_G='failback'
_F='Bits'
_E='read-only'
_D='ZTE-AN-UAPS-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_P,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ZxAnPortList,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnPortList','zxAn')
zxAnUapsMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,7))
_ZxAnUapsObjects_ObjectIdentity=ObjectIdentity
zxAnUapsObjects=_ZxAnUapsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,7,1))
class _ZxAnUapsCapability_Type(Bits):namedValues=NamedValues(*(('ipLinkChk',0),('protectionTime',1),('supportSlaveSlotPorts',2)))
_ZxAnUapsCapability_Type.__name__=_F
_ZxAnUapsCapability_Object=MibScalar
zxAnUapsCapability=_ZxAnUapsCapability_Object((1,3,6,1,4,1,3902,1015,7,1,1),_ZxAnUapsCapability_Type())
zxAnUapsCapability.setMaxAccess(_Q)
if mibBuilder.loadTexts:zxAnUapsCapability.setStatus(_A)
_ZxAnUapsGroupTable_Object=MibTable
zxAnUapsGroupTable=_ZxAnUapsGroupTable_Object((1,3,6,1,4,1,3902,1015,7,1,2))
if mibBuilder.loadTexts:zxAnUapsGroupTable.setStatus(_A)
_ZxAnUapsGroupEntry_Object=MibTableRow
zxAnUapsGroupEntry=_ZxAnUapsGroupEntry_Object((1,3,6,1,4,1,3902,1015,7,1,2,1))
zxAnUapsGroupEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:zxAnUapsGroupEntry.setStatus(_A)
class _ZxAnUapsGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ZxAnUapsGroupIndex_Type.__name__=_C
_ZxAnUapsGroupIndex_Object=MibTableColumn
zxAnUapsGroupIndex=_ZxAnUapsGroupIndex_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,1),_ZxAnUapsGroupIndex_Type())
zxAnUapsGroupIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:zxAnUapsGroupIndex.setStatus(_A)
class _ZxAnUapsGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnUapsGroupName_Type.__name__=_P
_ZxAnUapsGroupName_Object=MibTableColumn
zxAnUapsGroupName=_ZxAnUapsGroupName_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,2),_ZxAnUapsGroupName_Type())
zxAnUapsGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsGroupName.setStatus(_A)
_ZxAnUapsPrimaryPortList_Type=ObjectIdentifier
_ZxAnUapsPrimaryPortList_Object=MibTableColumn
zxAnUapsPrimaryPortList=_ZxAnUapsPrimaryPortList_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,3),_ZxAnUapsPrimaryPortList_Type())
zxAnUapsPrimaryPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsPrimaryPortList.setStatus(_A)
_ZxAnUapsSecondaryPortList_Type=ObjectIdentifier
_ZxAnUapsSecondaryPortList_Object=MibTableColumn
zxAnUapsSecondaryPortList=_ZxAnUapsSecondaryPortList_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,4),_ZxAnUapsSecondaryPortList_Type())
zxAnUapsSecondaryPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsSecondaryPortList.setStatus(_A)
_ZxAnUapsAutoFailbackEnable_Type=Integer32
_ZxAnUapsAutoFailbackEnable_Object=MibTableColumn
zxAnUapsAutoFailbackEnable=_ZxAnUapsAutoFailbackEnable_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,5),_ZxAnUapsAutoFailbackEnable_Type())
zxAnUapsAutoFailbackEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsAutoFailbackEnable.setStatus(_A)
_ZxAnUapsNextHopIp_Type=IpAddress
_ZxAnUapsNextHopIp_Object=MibTableColumn
zxAnUapsNextHopIp=_ZxAnUapsNextHopIp_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,6),_ZxAnUapsNextHopIp_Type())
zxAnUapsNextHopIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsNextHopIp.setStatus(_A)
class _ZxAnUapsIpLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('defaulIpLink',1),('serviceIpLink',2)))
_ZxAnUapsIpLinkType_Type.__name__=_C
_ZxAnUapsIpLinkType_Object=MibTableColumn
zxAnUapsIpLinkType=_ZxAnUapsIpLinkType_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,7),_ZxAnUapsIpLinkType_Type())
zxAnUapsIpLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsIpLinkType.setStatus(_A)
class _ZxAnUapsIpLinkChkRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZxAnUapsIpLinkChkRetries_Type.__name__=_C
_ZxAnUapsIpLinkChkRetries_Object=MibTableColumn
zxAnUapsIpLinkChkRetries=_ZxAnUapsIpLinkChkRetries_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,8),_ZxAnUapsIpLinkChkRetries_Type())
zxAnUapsIpLinkChkRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsIpLinkChkRetries.setStatus(_A)
class _ZxAnUapsIpLinkChkTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZxAnUapsIpLinkChkTimeout_Type.__name__=_C
_ZxAnUapsIpLinkChkTimeout_Object=MibTableColumn
zxAnUapsIpLinkChkTimeout=_ZxAnUapsIpLinkChkTimeout_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,9),_ZxAnUapsIpLinkChkTimeout_Type())
zxAnUapsIpLinkChkTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsIpLinkChkTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnUapsIpLinkChkTimeout.setUnits('sec')
class _ZxAnUapsIpLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('unknown',4)))
_ZxAnUapsIpLinkStatus_Type.__name__=_C
_ZxAnUapsIpLinkStatus_Object=MibTableColumn
zxAnUapsIpLinkStatus=_ZxAnUapsIpLinkStatus_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,10),_ZxAnUapsIpLinkStatus_Type())
zxAnUapsIpLinkStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnUapsIpLinkStatus.setStatus(_A)
_ZxAnUapsForceSwap_Type=Integer32
_ZxAnUapsForceSwap_Object=MibTableColumn
zxAnUapsForceSwap=_ZxAnUapsForceSwap_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,11),_ZxAnUapsForceSwap_Type())
zxAnUapsForceSwap.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsForceSwap.setStatus(_A)
class _ZxAnUapsPortWorkingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryPortInWorking',1),('secondaryPortInWorking',2)))
_ZxAnUapsPortWorkingStatus_Type.__name__=_C
_ZxAnUapsPortWorkingStatus_Object=MibTableColumn
zxAnUapsPortWorkingStatus=_ZxAnUapsPortWorkingStatus_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,12),_ZxAnUapsPortWorkingStatus_Type())
zxAnUapsPortWorkingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnUapsPortWorkingStatus.setStatus(_A)
class _ZxAnUapsSwapReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3)))
_ZxAnUapsSwapReason_Type.__name__=_C
_ZxAnUapsSwapReason_Object=MibTableColumn
zxAnUapsSwapReason=_ZxAnUapsSwapReason_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,13),_ZxAnUapsSwapReason_Type())
zxAnUapsSwapReason.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnUapsSwapReason.setStatus(_A)
class _ZxAnUapsSupportSlaveSlotPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('csc',2)))
_ZxAnUapsSupportSlaveSlotPorts_Type.__name__=_C
_ZxAnUapsSupportSlaveSlotPorts_Object=MibTableColumn
zxAnUapsSupportSlaveSlotPorts=_ZxAnUapsSupportSlaveSlotPorts_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,14),_ZxAnUapsSupportSlaveSlotPorts_Type())
zxAnUapsSupportSlaveSlotPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsSupportSlaveSlotPorts.setStatus(_A)
class _ZxAnUapsProtectionTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_ZxAnUapsProtectionTime_Type.__name__=_C
_ZxAnUapsProtectionTime_Object=MibTableColumn
zxAnUapsProtectionTime=_ZxAnUapsProtectionTime_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,15),_ZxAnUapsProtectionTime_Type())
zxAnUapsProtectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsProtectionTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnUapsProtectionTime.setUnits('second')
_ZxAnUapsIsInPrtctTime_Type=TruthValue
_ZxAnUapsIsInPrtctTime_Object=MibTableColumn
zxAnUapsIsInPrtctTime=_ZxAnUapsIsInPrtctTime_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,16),_ZxAnUapsIsInPrtctTime_Type())
zxAnUapsIsInPrtctTime.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnUapsIsInPrtctTime.setStatus(_A)
class _ZxAnUapsSwapRequestInCache_Type(Bits):namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3)))
_ZxAnUapsSwapRequestInCache_Type.__name__=_F
_ZxAnUapsSwapRequestInCache_Object=MibTableColumn
zxAnUapsSwapRequestInCache=_ZxAnUapsSwapRequestInCache_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,17),_ZxAnUapsSwapRequestInCache_Type())
zxAnUapsSwapRequestInCache.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnUapsSwapRequestInCache.setStatus(_A)
class _ZxAnUapsSwapLastRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3)))
_ZxAnUapsSwapLastRequest_Type.__name__=_C
_ZxAnUapsSwapLastRequest_Object=MibTableColumn
zxAnUapsSwapLastRequest=_ZxAnUapsSwapLastRequest_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,18),_ZxAnUapsSwapLastRequest_Type())
zxAnUapsSwapLastRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnUapsSwapLastRequest.setStatus(_A)
class _ZxAnUapsSwapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('common',1),('trunk',2),('upPortNum',3)))
_ZxAnUapsSwapMode_Type.__name__=_C
_ZxAnUapsSwapMode_Object=MibTableColumn
zxAnUapsSwapMode=_ZxAnUapsSwapMode_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,19),_ZxAnUapsSwapMode_Type())
zxAnUapsSwapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsSwapMode.setStatus(_A)
class _ZxAnUapsSecondaryPortLighting_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnUapsSecondaryPortLighting_Type.__name__=_C
_ZxAnUapsSecondaryPortLighting_Object=MibTableColumn
zxAnUapsSecondaryPortLighting=_ZxAnUapsSecondaryPortLighting_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,20),_ZxAnUapsSecondaryPortLighting_Type())
zxAnUapsSecondaryPortLighting.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsSecondaryPortLighting.setStatus(_A)
_ZxAnUapsGroupRowStatus_Type=RowStatus
_ZxAnUapsGroupRowStatus_Object=MibTableColumn
zxAnUapsGroupRowStatus=_ZxAnUapsGroupRowStatus_Object((1,3,6,1,4,1,3902,1015,7,1,2,1,25),_ZxAnUapsGroupRowStatus_Type())
zxAnUapsGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnUapsGroupRowStatus.setStatus(_A)
_ZxAnUapsTraps_ObjectIdentity=ObjectIdentity
zxAnUapsTraps=_ZxAnUapsTraps_ObjectIdentity((1,3,6,1,4,1,3902,1015,7,2))
zxAnUapsSwappedTrap=NotificationType((1,3,6,1,4,1,3902,1015,7,2,1))
zxAnUapsSwappedTrap.setObjects(*((_D,_K),(_D,_L),(_D,_M),(_D,_N),(_D,_O)))
if mibBuilder.loadTexts:zxAnUapsSwappedTrap.setStatus(_A)
zxAnUapsSwappedAlm=NotificationType((1,3,6,1,4,1,3902,1015,7,2,2))
zxAnUapsSwappedAlm.setObjects(*((_D,_K),(_D,_L),(_D,_M),(_D,_N),(_D,_O)))
if mibBuilder.loadTexts:zxAnUapsSwappedAlm.setStatus(_A)
zxAnUapsSwappedClr=NotificationType((1,3,6,1,4,1,3902,1015,7,2,3))
if mibBuilder.loadTexts:zxAnUapsSwappedClr.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnUapsMib':zxAnUapsMib,'zxAnUapsObjects':zxAnUapsObjects,'zxAnUapsCapability':zxAnUapsCapability,'zxAnUapsGroupTable':zxAnUapsGroupTable,'zxAnUapsGroupEntry':zxAnUapsGroupEntry,_R:zxAnUapsGroupIndex,_M:zxAnUapsGroupName,_N:zxAnUapsPrimaryPortList,_O:zxAnUapsSecondaryPortList,'zxAnUapsAutoFailbackEnable':zxAnUapsAutoFailbackEnable,'zxAnUapsNextHopIp':zxAnUapsNextHopIp,'zxAnUapsIpLinkType':zxAnUapsIpLinkType,'zxAnUapsIpLinkChkRetries':zxAnUapsIpLinkChkRetries,'zxAnUapsIpLinkChkTimeout':zxAnUapsIpLinkChkTimeout,'zxAnUapsIpLinkStatus':zxAnUapsIpLinkStatus,'zxAnUapsForceSwap':zxAnUapsForceSwap,_K:zxAnUapsPortWorkingStatus,_L:zxAnUapsSwapReason,'zxAnUapsSupportSlaveSlotPorts':zxAnUapsSupportSlaveSlotPorts,'zxAnUapsProtectionTime':zxAnUapsProtectionTime,'zxAnUapsIsInPrtctTime':zxAnUapsIsInPrtctTime,'zxAnUapsSwapRequestInCache':zxAnUapsSwapRequestInCache,'zxAnUapsSwapLastRequest':zxAnUapsSwapLastRequest,'zxAnUapsSwapMode':zxAnUapsSwapMode,'zxAnUapsSecondaryPortLighting':zxAnUapsSecondaryPortLighting,'zxAnUapsGroupRowStatus':zxAnUapsGroupRowStatus,'zxAnUapsTraps':zxAnUapsTraps,'zxAnUapsSwappedTrap':zxAnUapsSwappedTrap,'zxAnUapsSwappedAlm':zxAnUapsSwappedAlm,'zxAnUapsSwappedClr':zxAnUapsSwappedClr})