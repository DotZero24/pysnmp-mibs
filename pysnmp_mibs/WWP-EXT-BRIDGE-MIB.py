_N='wwpVlanXEntry'
_M='PortList'
_L='wwpVlanId'
_K='enable'
_J='disable'
_I='wwpPortId'
_H='auto'
_G='TruthValue'
_F='DisplayString'
_E='WWP-EXT-BRIDGE-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpExtBridgeMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,4))
if mibBuilder.loadTexts:wwpExtBridgeMIB.setRevisions(('2005-11-23 09:00','2001-04-03 17:00'))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpExtBridgeMIBObjects_ObjectIdentity=ObjectIdentity
wwpExtBridgeMIBObjects=_WwpExtBridgeMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,4,1))
_WwpPort_ObjectIdentity=ObjectIdentity
wwpPort=_WwpPort_ObjectIdentity((1,3,6,1,4,1,6141,2,4,1,1))
_WwpPortTable_Object=MibTable
wwpPortTable=_WwpPortTable_Object((1,3,6,1,4,1,6141,2,4,1,1,1))
if mibBuilder.loadTexts:wwpPortTable.setStatus(_A)
_WwpPortEntry_Object=MibTableRow
wwpPortEntry=_WwpPortEntry_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1))
wwpPortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wwpPortEntry.setStatus(_A)
class _WwpPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpPortId_Type.__name__=_B
_WwpPortId_Object=MibTableColumn
wwpPortId=_WwpPortId_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,1),_WwpPortId_Type())
wwpPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPortId.setStatus(_A)
class _WwpPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lx',1),('fastEth',2),('voip',3),('sx',4),('hundredFx',5),('unknown',6)))
_WwpPortType_Type.__name__=_B
_WwpPortType_Object=MibTableColumn
wwpPortType=_WwpPortType_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,2),_WwpPortType_Type())
wwpPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPortType.setStatus(_A)
class _WwpPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpPortName_Type.__name__=_F
_WwpPortName_Object=MibTableColumn
wwpPortName=_WwpPortName_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,3),_WwpPortName_Type())
wwpPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortName.setStatus(_A)
_WwpPortPhysAddr_Type=MacAddress
_WwpPortPhysAddr_Object=MibTableColumn
wwpPortPhysAddr=_WwpPortPhysAddr_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,4),_WwpPortPhysAddr_Type())
wwpPortPhysAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPortPhysAddr.setStatus(_A)
_WwpPortAutoNeg_Type=TruthValue
_WwpPortAutoNeg_Object=MibTableColumn
wwpPortAutoNeg=_WwpPortAutoNeg_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,5),_WwpPortAutoNeg_Type())
wwpPortAutoNeg.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortAutoNeg.setStatus(_A)
class _WwpPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_WwpPortAdminStatus_Type.__name__=_B
_WwpPortAdminStatus_Object=MibTableColumn
wwpPortAdminStatus=_WwpPortAdminStatus_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,6),_WwpPortAdminStatus_Type())
wwpPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortAdminStatus.setStatus(_A)
class _WwpPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_WwpPortOperStatus_Type.__name__=_B
_WwpPortOperStatus_Object=MibTableColumn
wwpPortOperStatus=_WwpPortOperStatus_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,7),_WwpPortOperStatus_Type())
wwpPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPortOperStatus.setStatus(_A)
class _WwpPortAdminSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tenMb',1),('hundredMb',2),('gig',3),(_H,4)))
_WwpPortAdminSpeed_Type.__name__=_B
_WwpPortAdminSpeed_Object=MibTableColumn
wwpPortAdminSpeed=_WwpPortAdminSpeed_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,8),_WwpPortAdminSpeed_Type())
wwpPortAdminSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortAdminSpeed.setStatus(_A)
_WwpPortOperSpeed_Type=Integer32
_WwpPortOperSpeed_Object=MibTableColumn
wwpPortOperSpeed=_WwpPortOperSpeed_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,9),_WwpPortOperSpeed_Type())
wwpPortOperSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPortOperSpeed.setStatus(_A)
class _WwpPortAdminDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('half',1),('full',2),(_H,3)))
_WwpPortAdminDuplex_Type.__name__=_B
_WwpPortAdminDuplex_Object=MibTableColumn
wwpPortAdminDuplex=_WwpPortAdminDuplex_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,10),_WwpPortAdminDuplex_Type())
wwpPortAdminDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortAdminDuplex.setStatus(_A)
class _WwpPortOperDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('half',1),('full',2),(_H,3)))
_WwpPortOperDuplex_Type.__name__=_B
_WwpPortOperDuplex_Object=MibTableColumn
wwpPortOperDuplex=_WwpPortOperDuplex_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,11),_WwpPortOperDuplex_Type())
wwpPortOperDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPortOperDuplex.setStatus(_A)
class _WwpPortAdminFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_WwpPortAdminFlowCtrl_Type.__name__=_B
_WwpPortAdminFlowCtrl_Object=MibTableColumn
wwpPortAdminFlowCtrl=_WwpPortAdminFlowCtrl_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,12),_WwpPortAdminFlowCtrl_Type())
wwpPortAdminFlowCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortAdminFlowCtrl.setStatus(_A)
class _WwpPortOperFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_WwpPortOperFlowCtrl_Type.__name__=_B
_WwpPortOperFlowCtrl_Object=MibTableColumn
wwpPortOperFlowCtrl=_WwpPortOperFlowCtrl_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,13),_WwpPortOperFlowCtrl_Type())
wwpPortOperFlowCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPortOperFlowCtrl.setStatus(_A)
class _WwpPortTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untagged',0),('tagged',1)))
_WwpPortTagged_Type.__name__=_B
_WwpPortTagged_Object=MibTableColumn
wwpPortTagged=_WwpPortTagged_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,14),_WwpPortTagged_Type())
wwpPortTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortTagged.setStatus(_A)
class _WwpPortUntaggedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('p0',0),('p1',1),('p2',2),('p3',3),('p4',4),('p5',5),('p6',6),('p7',7)))
_WwpPortUntaggedPriority_Type.__name__=_B
_WwpPortUntaggedPriority_Object=MibTableColumn
wwpPortUntaggedPriority=_WwpPortUntaggedPriority_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,15),_WwpPortUntaggedPriority_Type())
wwpPortUntaggedPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortUntaggedPriority.setStatus(_A)
class _WwpPortMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1522,9126))
_WwpPortMaxFrameSize_Type.__name__=_B
_WwpPortMaxFrameSize_Object=MibTableColumn
wwpPortMaxFrameSize=_WwpPortMaxFrameSize_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,16),_WwpPortMaxFrameSize_Type())
wwpPortMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortMaxFrameSize.setStatus(_A)
class _WwpPortIngressFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_WwpPortIngressFiltering_Type.__name__=_B
_WwpPortIngressFiltering_Object=MibTableColumn
wwpPortIngressFiltering=_WwpPortIngressFiltering_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,17),_WwpPortIngressFiltering_Type())
wwpPortIngressFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortIngressFiltering.setStatus(_A)
class _WwpPortRateLimitState_Type(TruthValue):defaultValue=2
_WwpPortRateLimitState_Type.__name__=_G
_WwpPortRateLimitState_Object=MibTableColumn
wwpPortRateLimitState=_WwpPortRateLimitState_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,18),_WwpPortRateLimitState_Type())
wwpPortRateLimitState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortRateLimitState.setStatus(_A)
class _WwpPortRateLimitValue_Type(Integer32):defaultValue=10000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpPortRateLimitValue_Type.__name__=_B
_WwpPortRateLimitValue_Object=MibTableColumn
wwpPortRateLimitValue=_WwpPortRateLimitValue_Object((1,3,6,1,4,1,6141,2,4,1,1,1,1,19),_WwpPortRateLimitValue_Type())
wwpPortRateLimitValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpPortRateLimitValue.setStatus(_A)
if mibBuilder.loadTexts:wwpPortRateLimitValue.setUnits('Bits per second')
class _WwpLocalMgmtPortEnable_Type(TruthValue):defaultValue=1
_WwpLocalMgmtPortEnable_Type.__name__=_G
_WwpLocalMgmtPortEnable_Object=MibScalar
wwpLocalMgmtPortEnable=_WwpLocalMgmtPortEnable_Object((1,3,6,1,4,1,6141,2,4,1,1,2),_WwpLocalMgmtPortEnable_Type())
wwpLocalMgmtPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLocalMgmtPortEnable.setStatus('deprecated')
_WwpVlan_ObjectIdentity=ObjectIdentity
wwpVlan=_WwpVlan_ObjectIdentity((1,3,6,1,4,1,6141,2,4,1,2))
class _WwpVlanVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('version1',1))
_WwpVlanVersionNumber_Type.__name__=_B
_WwpVlanVersionNumber_Object=MibScalar
wwpVlanVersionNumber=_WwpVlanVersionNumber_Object((1,3,6,1,4,1,6141,2,4,1,2,1),_WwpVlanVersionNumber_Type())
wwpVlanVersionNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVlanVersionNumber.setStatus(_A)
_WwpMaxVlanId_Type=VlanId
_WwpMaxVlanId_Object=MibScalar
wwpMaxVlanId=_WwpMaxVlanId_Object((1,3,6,1,4,1,6141,2,4,1,2,2),_WwpMaxVlanId_Type())
wwpMaxVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpMaxVlanId.setStatus(_A)
_WwpMaxSupportedVlans_Type=Unsigned32
_WwpMaxSupportedVlans_Object=MibScalar
wwpMaxSupportedVlans=_WwpMaxSupportedVlans_Object((1,3,6,1,4,1,6141,2,4,1,2,3),_WwpMaxSupportedVlans_Type())
wwpMaxSupportedVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpMaxSupportedVlans.setStatus(_A)
_WwpNumVlans_Type=Unsigned32
_WwpNumVlans_Object=MibScalar
wwpNumVlans=_WwpNumVlans_Object((1,3,6,1,4,1,6141,2,4,1,2,4),_WwpNumVlans_Type())
wwpNumVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpNumVlans.setStatus(_A)
_WwpVlanTable_Object=MibTable
wwpVlanTable=_WwpVlanTable_Object((1,3,6,1,4,1,6141,2,4,1,2,5))
if mibBuilder.loadTexts:wwpVlanTable.setStatus(_A)
_WwpVlanEntry_Object=MibTableRow
wwpVlanEntry=_WwpVlanEntry_Object((1,3,6,1,4,1,6141,2,4,1,2,5,1))
wwpVlanEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:wwpVlanEntry.setStatus(_A)
_WwpVlanId_Type=VlanId
_WwpVlanId_Object=MibTableColumn
wwpVlanId=_WwpVlanId_Object((1,3,6,1,4,1,6141,2,4,1,2,5,1,1),_WwpVlanId_Type())
wwpVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVlanId.setStatus(_A)
class _WwpVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpVlanName_Type.__name__=_F
_WwpVlanName_Object=MibTableColumn
wwpVlanName=_WwpVlanName_Object((1,3,6,1,4,1,6141,2,4,1,2,5,1,2),_WwpVlanName_Type())
wwpVlanName.setMaxAccess('read-create')
if mibBuilder.loadTexts:wwpVlanName.setStatus(_A)
class _WwpVlanCurrentEgressPorts_Type(PortList):defaultHexValue='0000'
_WwpVlanCurrentEgressPorts_Type.__name__=_M
_WwpVlanCurrentEgressPorts_Object=MibTableColumn
wwpVlanCurrentEgressPorts=_WwpVlanCurrentEgressPorts_Object((1,3,6,1,4,1,6141,2,4,1,2,5,1,3),_WwpVlanCurrentEgressPorts_Type())
wwpVlanCurrentEgressPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpVlanCurrentEgressPorts.setStatus(_A)
_WwpVlanCurrentUntaggedPorts_Type=PortList
_WwpVlanCurrentUntaggedPorts_Object=MibTableColumn
wwpVlanCurrentUntaggedPorts=_WwpVlanCurrentUntaggedPorts_Object((1,3,6,1,4,1,6141,2,4,1,2,5,1,4),_WwpVlanCurrentUntaggedPorts_Type())
wwpVlanCurrentUntaggedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpVlanCurrentUntaggedPorts.setStatus(_A)
class _WwpVlanMgmtStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notMgmtVlan',0),('remoteMgmtVlan',1),('localMgmtVlan',2)))
_WwpVlanMgmtStatus_Type.__name__=_B
_WwpVlanMgmtStatus_Object=MibTableColumn
wwpVlanMgmtStatus=_WwpVlanMgmtStatus_Object((1,3,6,1,4,1,6141,2,4,1,2,5,1,5),_WwpVlanMgmtStatus_Type())
wwpVlanMgmtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpVlanMgmtStatus.setStatus(_A)
_WwpVlanRowStatus_Type=RowStatus
_WwpVlanRowStatus_Object=MibTableColumn
wwpVlanRowStatus=_WwpVlanRowStatus_Object((1,3,6,1,4,1,6141,2,4,1,2,5,1,6),_WwpVlanRowStatus_Type())
wwpVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpVlanRowStatus.setStatus(_A)
_WwpVlanXTable_Object=MibTable
wwpVlanXTable=_WwpVlanXTable_Object((1,3,6,1,4,1,6141,2,4,1,2,6))
if mibBuilder.loadTexts:wwpVlanXTable.setStatus(_A)
_WwpVlanXEntry_Object=MibTableRow
wwpVlanXEntry=_WwpVlanXEntry_Object((1,3,6,1,4,1,6141,2,4,1,2,6,1))
if mibBuilder.loadTexts:wwpVlanXEntry.setStatus(_A)
class _WwpVlanTunnel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_WwpVlanTunnel_Type.__name__=_B
_WwpVlanTunnel_Object=MibTableColumn
wwpVlanTunnel=_WwpVlanTunnel_Object((1,3,6,1,4,1,6141,2,4,1,2,6,1,1),_WwpVlanTunnel_Type())
wwpVlanTunnel.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpVlanTunnel.setStatus(_A)
_WwpExtBridgeMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpExtBridgeMIBNotificationPrefix=_WwpExtBridgeMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,4,2))
_WwpExtBridgeMIBNotifications_ObjectIdentity=ObjectIdentity
wwpExtBridgeMIBNotifications=_WwpExtBridgeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,4,2,0))
_WwpExtBridgeMIBConformance_ObjectIdentity=ObjectIdentity
wwpExtBridgeMIBConformance=_WwpExtBridgeMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,4,3))
_WwpExtBridgeMIBCompliances_ObjectIdentity=ObjectIdentity
wwpExtBridgeMIBCompliances=_WwpExtBridgeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,4,3,1))
_WwpExtBridgeMIBGroups_ObjectIdentity=ObjectIdentity
wwpExtBridgeMIBGroups=_WwpExtBridgeMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,4,3,2))
wwpVlanEntry.registerAugmentions((_E,_N))
wwpVlanXEntry.setIndexNames(*wwpVlanEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_M:PortList,'VlanId':VlanId,'wwpExtBridgeMIB':wwpExtBridgeMIB,'wwpExtBridgeMIBObjects':wwpExtBridgeMIBObjects,'wwpPort':wwpPort,'wwpPortTable':wwpPortTable,'wwpPortEntry':wwpPortEntry,_I:wwpPortId,'wwpPortType':wwpPortType,'wwpPortName':wwpPortName,'wwpPortPhysAddr':wwpPortPhysAddr,'wwpPortAutoNeg':wwpPortAutoNeg,'wwpPortAdminStatus':wwpPortAdminStatus,'wwpPortOperStatus':wwpPortOperStatus,'wwpPortAdminSpeed':wwpPortAdminSpeed,'wwpPortOperSpeed':wwpPortOperSpeed,'wwpPortAdminDuplex':wwpPortAdminDuplex,'wwpPortOperDuplex':wwpPortOperDuplex,'wwpPortAdminFlowCtrl':wwpPortAdminFlowCtrl,'wwpPortOperFlowCtrl':wwpPortOperFlowCtrl,'wwpPortTagged':wwpPortTagged,'wwpPortUntaggedPriority':wwpPortUntaggedPriority,'wwpPortMaxFrameSize':wwpPortMaxFrameSize,'wwpPortIngressFiltering':wwpPortIngressFiltering,'wwpPortRateLimitState':wwpPortRateLimitState,'wwpPortRateLimitValue':wwpPortRateLimitValue,'wwpLocalMgmtPortEnable':wwpLocalMgmtPortEnable,'wwpVlan':wwpVlan,'wwpVlanVersionNumber':wwpVlanVersionNumber,'wwpMaxVlanId':wwpMaxVlanId,'wwpMaxSupportedVlans':wwpMaxSupportedVlans,'wwpNumVlans':wwpNumVlans,'wwpVlanTable':wwpVlanTable,'wwpVlanEntry':wwpVlanEntry,_L:wwpVlanId,'wwpVlanName':wwpVlanName,'wwpVlanCurrentEgressPorts':wwpVlanCurrentEgressPorts,'wwpVlanCurrentUntaggedPorts':wwpVlanCurrentUntaggedPorts,'wwpVlanMgmtStatus':wwpVlanMgmtStatus,'wwpVlanRowStatus':wwpVlanRowStatus,'wwpVlanXTable':wwpVlanXTable,_N:wwpVlanXEntry,'wwpVlanTunnel':wwpVlanTunnel,'wwpExtBridgeMIBNotificationPrefix':wwpExtBridgeMIBNotificationPrefix,'wwpExtBridgeMIBNotifications':wwpExtBridgeMIBNotifications,'wwpExtBridgeMIBConformance':wwpExtBridgeMIBConformance,'wwpExtBridgeMIBCompliances':wwpExtBridgeMIBCompliances,'wwpExtBridgeMIBGroups':wwpExtBridgeMIBGroups})