_Z='vlanAMRRulesRule'
_Y='vlanTestAPIOutputIndex'
_X='vlanPortPortNum'
_W='vlanSystemSwitchInstance'
_V='invalid-config'
_U='vlanNameIndex'
_T='vlanNameNHash'
_S='locked'
_R='decNET'
_Q='appleTalk'
_P='netBIOS'
_O='disable-vlan'
_N='enable-vlan'
_M='delete-vlan'
_L='add-vlan'
_K='normal'
_J='open'
_I='secure'
_H='CTRON-SFPS-VLAN-MIB'
_G='disabled'
_F='enabled'
_E='read-write'
_D='other'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vlanAMRRules,vlanAMRStats,vlanAMRSubnets,vlanAPI,vlanCountAPI,vlanName,vlanPort,vlanSystem,vlanTestAPI=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','vlanAMRRules','vlanAMRStats','vlanAMRSubnets','vlanAPI','vlanCountAPI','vlanName','vlanPort','vlanSystem','vlanTestAPI')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class VlanSwitchInstance(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class HexInteger(Integer32):0
class SfpsSwitchPort(Integer32):0
class _SfpsVAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_D,1),(_L,2),(_M,3),(_N,4),(_O,5),('map-port',6),('unmap-port',7),('enable-port',8),('disable-port',9),('map-user',10),('unmap-user',11),('tap-vlan',12),('untap-vlan',13),('auto-register',14),('auto-unregister',15)))
_SfpsVAPIVerb_Type.__name__=_C
_SfpsVAPIVerb_Object=MibScalar
sfpsVAPIVerb=_SfpsVAPIVerb_Object((1,3,6,1,4,1,52,4,2,12,1,1,1),_SfpsVAPIVerb_Type())
sfpsVAPIVerb.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIVerb.setStatus(_A)
_SfpsVAPIInPort_Type=SfpsSwitchPort
_SfpsVAPIInPort_Object=MibScalar
sfpsVAPIInPort=_SfpsVAPIInPort_Object((1,3,6,1,4,1,52,4,2,12,1,1,2),_SfpsVAPIInPort_Type())
sfpsVAPIInPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIInPort.setStatus(_A)
_SfpsVAPIVlanName_Type=DisplayString
_SfpsVAPIVlanName_Object=MibScalar
sfpsVAPIVlanName=_SfpsVAPIVlanName_Object((1,3,6,1,4,1,52,4,2,12,1,1,3),_SfpsVAPIVlanName_Type())
sfpsVAPIVlanName.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIVlanName.setStatus(_A)
_SfpsVAPIOutPort_Type=SfpsSwitchPort
_SfpsVAPIOutPort_Object=MibScalar
sfpsVAPIOutPort=_SfpsVAPIOutPort_Object((1,3,6,1,4,1,52,4,2,12,1,1,4),_SfpsVAPIOutPort_Type())
sfpsVAPIOutPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIOutPort.setStatus(_A)
_SfpsVAPIUserMAC_Type=SfpsAddress
_SfpsVAPIUserMAC_Object=MibScalar
sfpsVAPIUserMAC=_SfpsVAPIUserMAC_Object((1,3,6,1,4,1,52,4,2,12,1,1,5),_SfpsVAPIUserMAC_Type())
sfpsVAPIUserMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIUserMAC.setStatus(_A)
class _SfpsVAPIUserAliasTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('aoMacDx',1),('aoIpxSap',2),('aoIpxRIP',3),('aoInetYP',4),('aoInetUDP',5),('aoIpxIpx',6),('aoInetIP',7),('aoInetRPC',8),('aoInetRIP',9),('aoMacDXMcast',10),('aoAtDDP',11),('aoEmpty',12),('aoVlan',13),('aoHostName',14),('aoNetBiosName',15),('aoInetIPMask',16)))
_SfpsVAPIUserAliasTag_Type.__name__=_C
_SfpsVAPIUserAliasTag_Object=MibScalar
sfpsVAPIUserAliasTag=_SfpsVAPIUserAliasTag_Object((1,3,6,1,4,1,52,4,2,12,1,1,6),_SfpsVAPIUserAliasTag_Type())
sfpsVAPIUserAliasTag.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIUserAliasTag.setStatus(_A)
_SfpsVAPIUserAlias_Type=DisplayString
_SfpsVAPIUserAlias_Object=MibScalar
sfpsVAPIUserAlias=_SfpsVAPIUserAlias_Object((1,3,6,1,4,1,52,4,2,12,1,1,7),_SfpsVAPIUserAlias_Type())
sfpsVAPIUserAlias.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIUserAlias.setStatus(_A)
class _SfpsVAPIAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_SfpsVAPIAdminStatus_Type.__name__=_C
_SfpsVAPIAdminStatus_Object=MibScalar
sfpsVAPIAdminStatus=_SfpsVAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,12,1,1,8),_SfpsVAPIAdminStatus_Type())
sfpsVAPIAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIAdminStatus.setStatus(_A)
class _SfpsVAPIAutoRegisterRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,1),('ether-type',2),('ip-subnet',3),(_P,4),('ipx-Server',5),(_Q,6),(_R,7),('vines',8),('bpdu',9)))
_SfpsVAPIAutoRegisterRule_Type.__name__=_C
_SfpsVAPIAutoRegisterRule_Object=MibScalar
sfpsVAPIAutoRegisterRule=_SfpsVAPIAutoRegisterRule_Object((1,3,6,1,4,1,52,4,2,12,1,1,9),_SfpsVAPIAutoRegisterRule_Type())
sfpsVAPIAutoRegisterRule.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIAutoRegisterRule.setStatus(_A)
_SfpsVAPIAutoRegMask_Type=IpAddress
_SfpsVAPIAutoRegMask_Object=MibScalar
sfpsVAPIAutoRegMask=_SfpsVAPIAutoRegMask_Object((1,3,6,1,4,1,52,4,2,12,1,1,10),_SfpsVAPIAutoRegMask_Type())
sfpsVAPIAutoRegMask.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIAutoRegMask.setStatus(_A)
_SfpsVAPIAutoRegValue_Type=IpAddress
_SfpsVAPIAutoRegValue_Object=MibScalar
sfpsVAPIAutoRegValue=_SfpsVAPIAutoRegValue_Object((1,3,6,1,4,1,52,4,2,12,1,1,11),_SfpsVAPIAutoRegValue_Type())
sfpsVAPIAutoRegValue.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIAutoRegValue.setStatus(_A)
class _SfpsVAPIUnicastPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_I,3)))
_SfpsVAPIUnicastPolicy_Type.__name__=_C
_SfpsVAPIUnicastPolicy_Object=MibScalar
sfpsVAPIUnicastPolicy=_SfpsVAPIUnicastPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,1,12),_SfpsVAPIUnicastPolicy_Type())
sfpsVAPIUnicastPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIUnicastPolicy.setStatus(_A)
class _SfpsVAPIPortPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_K,2),(_S,3)))
_SfpsVAPIPortPolicy_Type.__name__=_C
_SfpsVAPIPortPolicy_Object=MibScalar
sfpsVAPIPortPolicy=_SfpsVAPIPortPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,1,13),_SfpsVAPIPortPolicy_Type())
sfpsVAPIPortPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIPortPolicy.setStatus(_A)
class _SfpsVAPIFloodPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('flooding-on',2),('flooding-off',3)))
_SfpsVAPIFloodPolicy_Type.__name__=_C
_SfpsVAPIFloodPolicy_Object=MibScalar
sfpsVAPIFloodPolicy=_SfpsVAPIFloodPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,1,14),_SfpsVAPIFloodPolicy_Type())
sfpsVAPIFloodPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIFloodPolicy.setStatus(_A)
class _SfpsVAPIRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('router-port',2),('no-router',3)))
_SfpsVAPIRouterPort_Type.__name__=_C
_SfpsVAPIRouterPort_Object=MibScalar
sfpsVAPIRouterPort=_SfpsVAPIRouterPort_Object((1,3,6,1,4,1,52,4,2,12,1,1,15),_SfpsVAPIRouterPort_Type())
sfpsVAPIRouterPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIRouterPort.setStatus(_A)
_SfpsVAPIVlanId_Type=Integer32
_SfpsVAPIVlanId_Object=MibScalar
sfpsVAPIVlanId=_SfpsVAPIVlanId_Object((1,3,6,1,4,1,52,4,2,12,1,1,16),_SfpsVAPIVlanId_Type())
sfpsVAPIVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIVlanId.setStatus(_A)
_SfpsVAPINvramId_Type=Integer32
_SfpsVAPINvramId_Object=MibScalar
sfpsVAPINvramId=_SfpsVAPINvramId_Object((1,3,6,1,4,1,52,4,2,12,1,1,17),_SfpsVAPINvramId_Type())
sfpsVAPINvramId.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPINvramId.setStatus(_A)
_SfpsVAPIRelayAgent_Type=IpAddress
_SfpsVAPIRelayAgent_Object=MibScalar
sfpsVAPIRelayAgent=_SfpsVAPIRelayAgent_Object((1,3,6,1,4,1,52,4,2,12,1,1,18),_SfpsVAPIRelayAgent_Type())
sfpsVAPIRelayAgent.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPIRelayAgent.setStatus(_A)
class _SfpsVAPILayer3Learning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('learning-enabled',2),('learning-disabled',3)))
_SfpsVAPILayer3Learning_Type.__name__=_C
_SfpsVAPILayer3Learning_Object=MibScalar
sfpsVAPILayer3Learning=_SfpsVAPILayer3Learning_Object((1,3,6,1,4,1,52,4,2,12,1,1,19),_SfpsVAPILayer3Learning_Type())
sfpsVAPILayer3Learning.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVAPILayer3Learning.setStatus(_A)
_VlanNameTable_Object=MibTable
vlanNameTable=_VlanNameTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1))
if mibBuilder.loadTexts:vlanNameTable.setStatus(_A)
_VlanNameEntry_Object=MibTableRow
vlanNameEntry=_VlanNameEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1))
vlanNameEntry.setIndexNames((0,_H,_T),(0,_H,_U))
if mibBuilder.loadTexts:vlanNameEntry.setStatus(_A)
_VlanNameNHash_Type=HexInteger
_VlanNameNHash_Object=MibTableColumn
vlanNameNHash=_VlanNameNHash_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,1),_VlanNameNHash_Type())
vlanNameNHash.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameNHash.setStatus(_A)
_VlanNameIndex_Type=Integer32
_VlanNameIndex_Object=MibTableColumn
vlanNameIndex=_VlanNameIndex_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,2),_VlanNameIndex_Type())
vlanNameIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameIndex.setStatus(_A)
_VlanNameVlanName_Type=DisplayString
_VlanNameVlanName_Object=MibTableColumn
vlanNameVlanName=_VlanNameVlanName_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,3),_VlanNameVlanName_Type())
vlanNameVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameVlanName.setStatus(_A)
class _VlanNameAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_VlanNameAdminStatus_Type.__name__=_C
_VlanNameAdminStatus_Object=MibTableColumn
vlanNameAdminStatus=_VlanNameAdminStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,4),_VlanNameAdminStatus_Type())
vlanNameAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameAdminStatus.setStatus(_A)
class _VlanNameOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3),('shutdown-pending',4),('startup-pending',5),(_V,6),('testing',7)))
_VlanNameOperStatus_Type.__name__=_C
_VlanNameOperStatus_Object=MibTableColumn
vlanNameOperStatus=_VlanNameOperStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,5),_VlanNameOperStatus_Type())
vlanNameOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameOperStatus.setStatus(_A)
class _VlanNameUniPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_I,3)))
_VlanNameUniPolicy_Type.__name__=_C
_VlanNameUniPolicy_Object=MibTableColumn
vlanNameUniPolicy=_VlanNameUniPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,6),_VlanNameUniPolicy_Type())
vlanNameUniPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameUniPolicy.setStatus(_A)
class _VlanNameFloodPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('flood-off',2),('flood-on',3)))
_VlanNameFloodPolicy_Type.__name__=_C
_VlanNameFloodPolicy_Object=MibTableColumn
vlanNameFloodPolicy=_VlanNameFloodPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,7),_VlanNameFloodPolicy_Type())
vlanNameFloodPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameFloodPolicy.setStatus(_A)
_VlanNameStatusTime_Type=TimeTicks
_VlanNameStatusTime_Object=MibTableColumn
vlanNameStatusTime=_VlanNameStatusTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,8),_VlanNameStatusTime_Type())
vlanNameStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameStatusTime.setStatus(_A)
_VlanNameNumUsers_Type=DisplayString
_VlanNameNumUsers_Object=MibTableColumn
vlanNameNumUsers=_VlanNameNumUsers_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,9),_VlanNameNumUsers_Type())
vlanNameNumUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameNumUsers.setStatus(_A)
_VlanNameEnabledPorts_Type=DisplayString
_VlanNameEnabledPorts_Object=MibTableColumn
vlanNameEnabledPorts=_VlanNameEnabledPorts_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,10),_VlanNameEnabledPorts_Type())
vlanNameEnabledPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameEnabledPorts.setStatus(_A)
_VlanNameMappedPorts_Type=DisplayString
_VlanNameMappedPorts_Object=MibTableColumn
vlanNameMappedPorts=_VlanNameMappedPorts_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,11),_VlanNameMappedPorts_Type())
vlanNameMappedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameMappedPorts.setStatus(_A)
_VlanNameVlanRule_Type=Integer32
_VlanNameVlanRule_Object=MibTableColumn
vlanNameVlanRule=_VlanNameVlanRule_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,12),_VlanNameVlanRule_Type())
vlanNameVlanRule.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameVlanRule.setStatus(_A)
_VlanNameFloodPorts_Type=DisplayString
_VlanNameFloodPorts_Object=MibTableColumn
vlanNameFloodPorts=_VlanNameFloodPorts_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,13),_VlanNameFloodPorts_Type())
vlanNameFloodPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameFloodPorts.setStatus(_A)
_VlanNameVlanId_Type=Integer32
_VlanNameVlanId_Object=MibTableColumn
vlanNameVlanId=_VlanNameVlanId_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,14),_VlanNameVlanId_Type())
vlanNameVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameVlanId.setStatus(_A)
_VlanNameRelayAgent_Type=IpAddress
_VlanNameRelayAgent_Object=MibTableColumn
vlanNameRelayAgent=_VlanNameRelayAgent_Object((1,3,6,1,4,1,52,4,2,12,1,2,1,1,1,15),_VlanNameRelayAgent_Type())
vlanNameRelayAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNameRelayAgent.setStatus(_A)
_VlanSystemTable_Object=MibTable
vlanSystemTable=_VlanSystemTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1))
if mibBuilder.loadTexts:vlanSystemTable.setStatus(_A)
_VlanSystemEntry_Object=MibTableRow
vlanSystemEntry=_VlanSystemEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1))
vlanSystemEntry.setIndexNames((0,_H,_W))
if mibBuilder.loadTexts:vlanSystemEntry.setStatus(_A)
_VlanSystemSwitchInstance_Type=VlanSwitchInstance
_VlanSystemSwitchInstance_Object=MibTableColumn
vlanSystemSwitchInstance=_VlanSystemSwitchInstance_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,1),_VlanSystemSwitchInstance_Type())
vlanSystemSwitchInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemSwitchInstance.setStatus(_A)
class _VlanSystemAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_VlanSystemAdminStatus_Type.__name__=_C
_VlanSystemAdminStatus_Object=MibTableColumn
vlanSystemAdminStatus=_VlanSystemAdminStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,2),_VlanSystemAdminStatus_Type())
vlanSystemAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSystemAdminStatus.setStatus(_A)
class _VlanSystemAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('reset',2)))
_VlanSystemAdminReset_Type.__name__=_C
_VlanSystemAdminReset_Object=MibTableColumn
vlanSystemAdminReset=_VlanSystemAdminReset_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,3),_VlanSystemAdminReset_Type())
vlanSystemAdminReset.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSystemAdminReset.setStatus(_A)
class _VlanSystemOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3),('pending-disable',4),('pending-enable',5),(_V,6)))
_VlanSystemOperStatus_Type.__name__=_C
_VlanSystemOperStatus_Object=MibTableColumn
vlanSystemOperStatus=_VlanSystemOperStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,4),_VlanSystemOperStatus_Type())
vlanSystemOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemOperStatus.setStatus(_A)
_VlanSystemOperTime_Type=TimeTicks
_VlanSystemOperTime_Object=MibTableColumn
vlanSystemOperTime=_VlanSystemOperTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,5),_VlanSystemOperTime_Type())
vlanSystemOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemOperTime.setStatus(_A)
_VlanSystemLastChange_Type=TimeTicks
_VlanSystemLastChange_Object=MibTableColumn
vlanSystemLastChange=_VlanSystemLastChange_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,6),_VlanSystemLastChange_Type())
vlanSystemLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemLastChange.setStatus(_A)
_VlanSystemVersion_Type=DisplayString
_VlanSystemVersion_Object=MibTableColumn
vlanSystemVersion=_VlanSystemVersion_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,7),_VlanSystemVersion_Type())
vlanSystemVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemVersion.setStatus(_A)
_VlanSystemMibRev_Type=DisplayString
_VlanSystemMibRev_Object=MibTableColumn
vlanSystemMibRev=_VlanSystemMibRev_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,8),_VlanSystemMibRev_Type())
vlanSystemMibRev.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemMibRev.setStatus(_A)
_VlanSystemAgentIP_Type=IpAddress
_VlanSystemAgentIP_Object=MibTableColumn
vlanSystemAgentIP=_VlanSystemAgentIP_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,9),_VlanSystemAgentIP_Type())
vlanSystemAgentIP.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSystemAgentIP.setStatus(_A)
_VlanSystemDomainName_Type=DisplayString
_VlanSystemDomainName_Object=MibTableColumn
vlanSystemDomainName=_VlanSystemDomainName_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,10),_VlanSystemDomainName_Type())
vlanSystemDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanSystemDomainName.setStatus(_A)
_VlanSystemPollCount_Type=Integer32
_VlanSystemPollCount_Object=MibTableColumn
vlanSystemPollCount=_VlanSystemPollCount_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,11),_VlanSystemPollCount_Type())
vlanSystemPollCount.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemPollCount.setStatus(_A)
_VlanSystemFirstPollTime_Type=TimeTicks
_VlanSystemFirstPollTime_Object=MibTableColumn
vlanSystemFirstPollTime=_VlanSystemFirstPollTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,12),_VlanSystemFirstPollTime_Type())
vlanSystemFirstPollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemFirstPollTime.setStatus(_A)
_VlanSystemLastPollTime_Type=TimeTicks
_VlanSystemLastPollTime_Object=MibTableColumn
vlanSystemLastPollTime=_VlanSystemLastPollTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,13),_VlanSystemLastPollTime_Type())
vlanSystemLastPollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemLastPollTime.setStatus(_A)
_VlanSystemPriorPollTime_Type=TimeTicks
_VlanSystemPriorPollTime_Object=MibTableColumn
vlanSystemPriorPollTime=_VlanSystemPriorPollTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,14),_VlanSystemPriorPollTime_Type())
vlanSystemPriorPollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemPriorPollTime.setStatus(_A)
_VlanSystemDeltaPollTime_Type=TimeTicks
_VlanSystemDeltaPollTime_Object=MibTableColumn
vlanSystemDeltaPollTime=_VlanSystemDeltaPollTime_Object((1,3,6,1,4,1,52,4,2,12,1,2,5,1,1,15),_VlanSystemDeltaPollTime_Type())
vlanSystemDeltaPollTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSystemDeltaPollTime.setStatus(_A)
_VlanPortTable_Object=MibTable
vlanPortTable=_VlanPortTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1))
if mibBuilder.loadTexts:vlanPortTable.setStatus(_A)
_VlanPortEntry_Object=MibTableRow
vlanPortEntry=_VlanPortEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1))
vlanPortEntry.setIndexNames((0,_H,_X))
if mibBuilder.loadTexts:vlanPortEntry.setStatus(_A)
_VlanPortPortNum_Type=Integer32
_VlanPortPortNum_Object=MibTableColumn
vlanPortPortNum=_VlanPortPortNum_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,1),_VlanPortPortNum_Type())
vlanPortPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortPortNum.setStatus(_A)
class _VlanPortPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_VlanPortPortStatus_Type.__name__=_C
_VlanPortPortStatus_Object=MibTableColumn
vlanPortPortStatus=_VlanPortPortStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,2),_VlanPortPortStatus_Type())
vlanPortPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortPortStatus.setStatus(_A)
class _VlanPortPortPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_K,2),(_S,3)))
_VlanPortPortPolicy_Type.__name__=_C
_VlanPortPortPolicy_Object=MibTableColumn
vlanPortPortPolicy=_VlanPortPortPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,3),_VlanPortPortPolicy_Type())
vlanPortPortPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortPortPolicy.setStatus(_A)
_VlanPortVlanName_Type=DisplayString
_VlanPortVlanName_Object=MibTableColumn
vlanPortVlanName=_VlanPortVlanName_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,4),_VlanPortVlanName_Type())
vlanPortVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortVlanName.setStatus(_A)
class _VlanPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_VlanPortAdminStatus_Type.__name__=_C
_VlanPortAdminStatus_Object=MibTableColumn
vlanPortAdminStatus=_VlanPortAdminStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,5),_VlanPortAdminStatus_Type())
vlanPortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortAdminStatus.setStatus(_A)
class _VlanPortUniPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_J,2),(_I,3)))
_VlanPortUniPolicy_Type.__name__=_C
_VlanPortUniPolicy_Object=MibTableColumn
vlanPortUniPolicy=_VlanPortUniPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,6),_VlanPortUniPolicy_Type())
vlanPortUniPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortUniPolicy.setStatus(_A)
class _VlanPortFloodPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('floodOn',2),('floodOff',3)))
_VlanPortFloodPolicy_Type.__name__=_C
_VlanPortFloodPolicy_Object=MibTableColumn
vlanPortFloodPolicy=_VlanPortFloodPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,7),_VlanPortFloodPolicy_Type())
vlanPortFloodPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortFloodPolicy.setStatus(_A)
class _VlanPortRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('routerPort',2),('noRouter',3)))
_VlanPortRouterPort_Type.__name__=_C
_VlanPortRouterPort_Object=MibTableColumn
vlanPortRouterPort=_VlanPortRouterPort_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,8),_VlanPortRouterPort_Type())
vlanPortRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortRouterPort.setStatus(_A)
_VlanPortVlanId_Type=Integer32
_VlanPortVlanId_Object=MibTableColumn
vlanPortVlanId=_VlanPortVlanId_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,9),_VlanPortVlanId_Type())
vlanPortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortVlanId.setStatus(_A)
_VlanPortRelayAgent_Type=IpAddress
_VlanPortRelayAgent_Object=MibTableColumn
vlanPortRelayAgent=_VlanPortRelayAgent_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,10),_VlanPortRelayAgent_Type())
vlanPortRelayAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortRelayAgent.setStatus(_A)
class _VlanPortLayer3Learning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_F,2),('disabed',3)))
_VlanPortLayer3Learning_Type.__name__=_C
_VlanPortLayer3Learning_Object=MibTableColumn
vlanPortLayer3Learning=_VlanPortLayer3Learning_Object((1,3,6,1,4,1,52,4,2,12,1,2,6,1,1,11),_VlanPortLayer3Learning_Type())
vlanPortLayer3Learning.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortLayer3Learning.setStatus(_A)
class _VlanTestAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_D,1),(_L,2),(_M,3),(_N,4),(_O,5),('open-vlan',6),('secure-vlan',7),('enable-vlan-port',8),('disable-vlan-port',9),('map-vlan-port',10),('unmap-vlan-port',11),('tap-vlan-port',12),('untap-vlan-port',13),('get-vlan-info',14),('get-port-info',15),('fill-table',16),('empty-table',17)))
_VlanTestAPIVerb_Type.__name__=_C
_VlanTestAPIVerb_Object=MibScalar
vlanTestAPIVerb=_VlanTestAPIVerb_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,1),_VlanTestAPIVerb_Type())
vlanTestAPIVerb.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanTestAPIVerb.setStatus(_A)
_VlanTestAPIVlanName_Type=DisplayString
_VlanTestAPIVlanName_Object=MibScalar
vlanTestAPIVlanName=_VlanTestAPIVlanName_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,2),_VlanTestAPIVlanName_Type())
vlanTestAPIVlanName.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanTestAPIVlanName.setStatus(_A)
_VlanTestAPIPort_Type=Integer32
_VlanTestAPIPort_Object=MibScalar
vlanTestAPIPort=_VlanTestAPIPort_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,3),_VlanTestAPIPort_Type())
vlanTestAPIPort.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanTestAPIPort.setStatus(_A)
_VlanTestAPIOutputTable_Object=MibTable
vlanTestAPIOutputTable=_VlanTestAPIOutputTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4))
if mibBuilder.loadTexts:vlanTestAPIOutputTable.setStatus(_A)
_VlanTestAPIOutputEntry_Object=MibTableRow
vlanTestAPIOutputEntry=_VlanTestAPIOutputEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1))
vlanTestAPIOutputEntry.setIndexNames((0,_H,_Y))
if mibBuilder.loadTexts:vlanTestAPIOutputEntry.setStatus(_A)
_VlanTestAPIOutputIndex_Type=Integer32
_VlanTestAPIOutputIndex_Object=MibTableColumn
vlanTestAPIOutputIndex=_VlanTestAPIOutputIndex_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,1),_VlanTestAPIOutputIndex_Type())
vlanTestAPIOutputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputIndex.setStatus(_A)
_VlanTestAPIOutputVlanName_Type=DisplayString
_VlanTestAPIOutputVlanName_Object=MibTableColumn
vlanTestAPIOutputVlanName=_VlanTestAPIOutputVlanName_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,2),_VlanTestAPIOutputVlanName_Type())
vlanTestAPIOutputVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputVlanName.setStatus(_A)
_VlanTestAPIOutputUserCnt_Type=Integer32
_VlanTestAPIOutputUserCnt_Object=MibTableColumn
vlanTestAPIOutputUserCnt=_VlanTestAPIOutputUserCnt_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,3),_VlanTestAPIOutputUserCnt_Type())
vlanTestAPIOutputUserCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputUserCnt.setStatus(_A)
class _VlanTestAPIOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_VlanTestAPIOutputStatus_Type.__name__=_C
_VlanTestAPIOutputStatus_Object=MibTableColumn
vlanTestAPIOutputStatus=_VlanTestAPIOutputStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,4),_VlanTestAPIOutputStatus_Type())
vlanTestAPIOutputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputStatus.setStatus(_A)
class _VlanTestAPIOutputPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_K,2),(_I,3)))
_VlanTestAPIOutputPolicy_Type.__name__=_C
_VlanTestAPIOutputPolicy_Object=MibTableColumn
vlanTestAPIOutputPolicy=_VlanTestAPIOutputPolicy_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,5),_VlanTestAPIOutputPolicy_Type())
vlanTestAPIOutputPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputPolicy.setStatus(_A)
_VlanTestAPIOutputPort_Type=Integer32
_VlanTestAPIOutputPort_Object=MibTableColumn
vlanTestAPIOutputPort=_VlanTestAPIOutputPort_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,6),_VlanTestAPIOutputPort_Type())
vlanTestAPIOutputPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputPort.setStatus(_A)
class _VlanTestAPIOutputMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('unmapped',2),('mapped',3)))
_VlanTestAPIOutputMap_Type.__name__=_C
_VlanTestAPIOutputMap_Object=MibTableColumn
vlanTestAPIOutputMap=_VlanTestAPIOutputMap_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,7),_VlanTestAPIOutputMap_Type())
vlanTestAPIOutputMap.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputMap.setStatus(_A)
class _VlanTestAPIOutputAble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_F,3)))
_VlanTestAPIOutputAble_Type.__name__=_C
_VlanTestAPIOutputAble_Object=MibTableColumn
vlanTestAPIOutputAble=_VlanTestAPIOutputAble_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,8),_VlanTestAPIOutputAble_Type())
vlanTestAPIOutputAble.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputAble.setStatus(_A)
class _VlanTestAPIOutputTap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('untapped',2),('tapped',3)))
_VlanTestAPIOutputTap_Type.__name__=_C
_VlanTestAPIOutputTap_Object=MibTableColumn
vlanTestAPIOutputTap=_VlanTestAPIOutputTap_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,9),_VlanTestAPIOutputTap_Type())
vlanTestAPIOutputTap.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputTap.setStatus(_A)
_VlanTestAPIOutputVlanId_Type=Integer32
_VlanTestAPIOutputVlanId_Object=MibTableColumn
vlanTestAPIOutputVlanId=_VlanTestAPIOutputVlanId_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,4,1,10),_VlanTestAPIOutputVlanId_Type())
vlanTestAPIOutputVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTestAPIOutputVlanId.setStatus(_A)
_VlanTestAPIVlanId_Type=Integer32
_VlanTestAPIVlanId_Object=MibScalar
vlanTestAPIVlanId=_VlanTestAPIVlanId_Object((1,3,6,1,4,1,52,4,2,12,1,2,9,5),_VlanTestAPIVlanId_Type())
vlanTestAPIVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanTestAPIVlanId.setStatus(_A)
_VlanCountAPITotal_Type=Integer32
_VlanCountAPITotal_Object=MibScalar
vlanCountAPITotal=_VlanCountAPITotal_Object((1,3,6,1,4,1,52,4,2,12,1,2,10,1,1),_VlanCountAPITotal_Type())
vlanCountAPITotal.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCountAPITotal.setStatus(_A)
_VlanCountAPIAdmin_Type=Integer32
_VlanCountAPIAdmin_Object=MibScalar
vlanCountAPIAdmin=_VlanCountAPIAdmin_Object((1,3,6,1,4,1,52,4,2,12,1,2,10,1,2),_VlanCountAPIAdmin_Type())
vlanCountAPIAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCountAPIAdmin.setStatus(_A)
_VlanCountAPIAutoreg_Type=Integer32
_VlanCountAPIAutoreg_Object=MibScalar
vlanCountAPIAutoreg=_VlanCountAPIAutoreg_Object((1,3,6,1,4,1,52,4,2,12,1,2,10,1,3),_VlanCountAPIAutoreg_Type())
vlanCountAPIAutoreg.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCountAPIAutoreg.setStatus(_A)
_VlanAMRRulesTable_Object=MibTable
vlanAMRRulesTable=_VlanAMRRulesTable_Object((1,3,6,1,4,1,52,4,2,12,3,6,1))
if mibBuilder.loadTexts:vlanAMRRulesTable.setStatus(_A)
_VlanAMRRulesEntry_Object=MibTableRow
vlanAMRRulesEntry=_VlanAMRRulesEntry_Object((1,3,6,1,4,1,52,4,2,12,3,6,1,1))
vlanAMRRulesEntry.setIndexNames((0,_H,_Z))
if mibBuilder.loadTexts:vlanAMRRulesEntry.setStatus(_A)
class _VlanAMRRulesRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,1),('etherType',2),('ipSubNet',3),(_P,4),('ipxServer',5),(_Q,6),(_R,7),('vines',8),('bpdu',9)))
_VlanAMRRulesRule_Type.__name__=_C
_VlanAMRRulesRule_Object=MibTableColumn
vlanAMRRulesRule=_VlanAMRRulesRule_Object((1,3,6,1,4,1,52,4,2,12,3,6,1,1,1),_VlanAMRRulesRule_Type())
vlanAMRRulesRule.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAMRRulesRule.setStatus(_A)
class _VlanAMRRulesStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('on',1))
_VlanAMRRulesStatus_Type.__name__=_C
_VlanAMRRulesStatus_Object=MibTableColumn
vlanAMRRulesStatus=_VlanAMRRulesStatus_Object((1,3,6,1,4,1,52,4,2,12,3,6,1,1,2),_VlanAMRRulesStatus_Type())
vlanAMRRulesStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAMRRulesStatus.setStatus(_A)
_VlanAMRSubnetsPrefix_Type=IpAddress
_VlanAMRSubnetsPrefix_Object=MibScalar
vlanAMRSubnetsPrefix=_VlanAMRSubnetsPrefix_Object((1,3,6,1,4,1,52,4,2,12,3,7,1),_VlanAMRSubnetsPrefix_Type())
vlanAMRSubnetsPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAMRSubnetsPrefix.setStatus(_A)
_VlanAMRSubnetsMask_Type=IpAddress
_VlanAMRSubnetsMask_Object=MibScalar
vlanAMRSubnetsMask=_VlanAMRSubnetsMask_Object((1,3,6,1,4,1,52,4,2,12,3,7,2),_VlanAMRSubnetsMask_Type())
vlanAMRSubnetsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAMRSubnetsMask.setStatus(_A)
_VlanAMRStatsNumRulesEnabled_Type=Integer32
_VlanAMRStatsNumRulesEnabled_Object=MibScalar
vlanAMRStatsNumRulesEnabled=_VlanAMRStatsNumRulesEnabled_Object((1,3,6,1,4,1,52,4,2,12,3,8,1),_VlanAMRStatsNumRulesEnabled_Type())
vlanAMRStatsNumRulesEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAMRStatsNumRulesEnabled.setStatus(_A)
_VlanAMRStatsSingleMask_Type=IpAddress
_VlanAMRStatsSingleMask_Object=MibScalar
vlanAMRStatsSingleMask=_VlanAMRStatsSingleMask_Object((1,3,6,1,4,1,52,4,2,12,3,8,2),_VlanAMRStatsSingleMask_Type())
vlanAMRStatsSingleMask.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAMRStatsSingleMask.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'VlanSwitchInstance':VlanSwitchInstance,'SfpsAddress':SfpsAddress,'HexInteger':HexInteger,'SfpsSwitchPort':SfpsSwitchPort,'sfpsVAPIVerb':sfpsVAPIVerb,'sfpsVAPIInPort':sfpsVAPIInPort,'sfpsVAPIVlanName':sfpsVAPIVlanName,'sfpsVAPIOutPort':sfpsVAPIOutPort,'sfpsVAPIUserMAC':sfpsVAPIUserMAC,'sfpsVAPIUserAliasTag':sfpsVAPIUserAliasTag,'sfpsVAPIUserAlias':sfpsVAPIUserAlias,'sfpsVAPIAdminStatus':sfpsVAPIAdminStatus,'sfpsVAPIAutoRegisterRule':sfpsVAPIAutoRegisterRule,'sfpsVAPIAutoRegMask':sfpsVAPIAutoRegMask,'sfpsVAPIAutoRegValue':sfpsVAPIAutoRegValue,'sfpsVAPIUnicastPolicy':sfpsVAPIUnicastPolicy,'sfpsVAPIPortPolicy':sfpsVAPIPortPolicy,'sfpsVAPIFloodPolicy':sfpsVAPIFloodPolicy,'sfpsVAPIRouterPort':sfpsVAPIRouterPort,'sfpsVAPIVlanId':sfpsVAPIVlanId,'sfpsVAPINvramId':sfpsVAPINvramId,'sfpsVAPIRelayAgent':sfpsVAPIRelayAgent,'sfpsVAPILayer3Learning':sfpsVAPILayer3Learning,'vlanNameTable':vlanNameTable,'vlanNameEntry':vlanNameEntry,_T:vlanNameNHash,_U:vlanNameIndex,'vlanNameVlanName':vlanNameVlanName,'vlanNameAdminStatus':vlanNameAdminStatus,'vlanNameOperStatus':vlanNameOperStatus,'vlanNameUniPolicy':vlanNameUniPolicy,'vlanNameFloodPolicy':vlanNameFloodPolicy,'vlanNameStatusTime':vlanNameStatusTime,'vlanNameNumUsers':vlanNameNumUsers,'vlanNameEnabledPorts':vlanNameEnabledPorts,'vlanNameMappedPorts':vlanNameMappedPorts,'vlanNameVlanRule':vlanNameVlanRule,'vlanNameFloodPorts':vlanNameFloodPorts,'vlanNameVlanId':vlanNameVlanId,'vlanNameRelayAgent':vlanNameRelayAgent,'vlanSystemTable':vlanSystemTable,'vlanSystemEntry':vlanSystemEntry,_W:vlanSystemSwitchInstance,'vlanSystemAdminStatus':vlanSystemAdminStatus,'vlanSystemAdminReset':vlanSystemAdminReset,'vlanSystemOperStatus':vlanSystemOperStatus,'vlanSystemOperTime':vlanSystemOperTime,'vlanSystemLastChange':vlanSystemLastChange,'vlanSystemVersion':vlanSystemVersion,'vlanSystemMibRev':vlanSystemMibRev,'vlanSystemAgentIP':vlanSystemAgentIP,'vlanSystemDomainName':vlanSystemDomainName,'vlanSystemPollCount':vlanSystemPollCount,'vlanSystemFirstPollTime':vlanSystemFirstPollTime,'vlanSystemLastPollTime':vlanSystemLastPollTime,'vlanSystemPriorPollTime':vlanSystemPriorPollTime,'vlanSystemDeltaPollTime':vlanSystemDeltaPollTime,'vlanPortTable':vlanPortTable,'vlanPortEntry':vlanPortEntry,_X:vlanPortPortNum,'vlanPortPortStatus':vlanPortPortStatus,'vlanPortPortPolicy':vlanPortPortPolicy,'vlanPortVlanName':vlanPortVlanName,'vlanPortAdminStatus':vlanPortAdminStatus,'vlanPortUniPolicy':vlanPortUniPolicy,'vlanPortFloodPolicy':vlanPortFloodPolicy,'vlanPortRouterPort':vlanPortRouterPort,'vlanPortVlanId':vlanPortVlanId,'vlanPortRelayAgent':vlanPortRelayAgent,'vlanPortLayer3Learning':vlanPortLayer3Learning,'vlanTestAPIVerb':vlanTestAPIVerb,'vlanTestAPIVlanName':vlanTestAPIVlanName,'vlanTestAPIPort':vlanTestAPIPort,'vlanTestAPIOutputTable':vlanTestAPIOutputTable,'vlanTestAPIOutputEntry':vlanTestAPIOutputEntry,_Y:vlanTestAPIOutputIndex,'vlanTestAPIOutputVlanName':vlanTestAPIOutputVlanName,'vlanTestAPIOutputUserCnt':vlanTestAPIOutputUserCnt,'vlanTestAPIOutputStatus':vlanTestAPIOutputStatus,'vlanTestAPIOutputPolicy':vlanTestAPIOutputPolicy,'vlanTestAPIOutputPort':vlanTestAPIOutputPort,'vlanTestAPIOutputMap':vlanTestAPIOutputMap,'vlanTestAPIOutputAble':vlanTestAPIOutputAble,'vlanTestAPIOutputTap':vlanTestAPIOutputTap,'vlanTestAPIOutputVlanId':vlanTestAPIOutputVlanId,'vlanTestAPIVlanId':vlanTestAPIVlanId,'vlanCountAPITotal':vlanCountAPITotal,'vlanCountAPIAdmin':vlanCountAPIAdmin,'vlanCountAPIAutoreg':vlanCountAPIAutoreg,'vlanAMRRulesTable':vlanAMRRulesTable,'vlanAMRRulesEntry':vlanAMRRulesEntry,_Z:vlanAMRRulesRule,'vlanAMRRulesStatus':vlanAMRRulesStatus,'vlanAMRSubnetsPrefix':vlanAMRSubnetsPrefix,'vlanAMRSubnetsMask':vlanAMRSubnetsMask,'vlanAMRStatsNumRulesEnabled':vlanAMRStatsNumRulesEnabled,'vlanAMRStatsSingleMask':vlanAMRStatsSingleMask})