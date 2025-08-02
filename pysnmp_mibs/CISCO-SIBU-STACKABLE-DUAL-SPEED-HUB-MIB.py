_z='ciscoSibuStackableDualSpeedHubSwitchPortGroup'
_y='ciscoSibuStackableDualSpeedHubRepeaterPortGroup'
_x='ciscoSibuStackableDualSpeedHubGroup'
_w='cssSwitchPortSpeedStatus'
_v='cssSwitchPortSpeedAdmin'
_u='cssSwitchPortDuplexStatus'
_t='cssSwitchPortDuplexAdmin'
_s='cssSwitchPortState'
_r='cssSwitchPortControllerRevision'
_q='cssSwitchPortType'
_p='cssSwitchPortName'
_o='cssRepeaterPortSpeedStatus'
_n='cssRepeaterPortSpeedAdmin'
_m='cssRepeaterPortControllerRevision'
_l='cssRepeaterPortName'
_k='cssGroupIsolatedState'
_j='cssGroupConfigDefaultReset'
_i='cssGroupReset'
_h='cssGroupRedundantPowerState'
_g='cssGroupInternalPowerState'
_f='cssGroupAgentPhysAddress'
_e='cssGroupAgentStatus'
_d='cssGroupAgentFirmwareVersion'
_c='cssGroupAgentBootVersion'
_b='cssGroupBoardRevision'
_a='cssGroupSerialNo'
_Z='cssGroupType'
_Y='cssGroupID'
_X='cssSystemLinkTraps'
_W='halfDuplex'
_V='fullDuplex'
_U='noLink'
_T='noReset'
_S='disabled'
_R='enabled'
_Q='rptrPortIndex'
_P='rptrPortGroupIndex'
_O='cssSwitchPortLinkStatus'
_N='cssRepeaterPortLinkStatus'
_M='cssSwitchPortPortID'
_L='cssSwitchPortModuleID'
_K='autoNegotiate'
_J='rptrGroupIndex'
_I='oneHundredMbps'
_H='tenMbps'
_G='SNMP-REPEATER-MIB'
_F='DisplayString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
rptrGroupIndex,rptrPortGroupIndex,rptrPortIndex=mibBuilder.importSymbols(_G,_J,_P,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ciscoSibuStackableDualSpeedHubMIB=ModuleIdentity((1,3,6,1,4,1,9,10,44))
if mibBuilder.loadTexts:ciscoSibuStackableDualSpeedHubMIB.setRevisions(('1998-10-23 00:00',))
class HubNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoSibuStackableDualSpeedHubMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBObjects=_CiscoSibuStackableDualSpeedHubMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,44,1))
_CssSystem_ObjectIdentity=ObjectIdentity
cssSystem=_CssSystem_ObjectIdentity((1,3,6,1,4,1,9,10,44,1,1))
class _CssSystemLinkTraps_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_CssSystemLinkTraps_Type.__name__=_C
_CssSystemLinkTraps_Object=MibScalar
cssSystemLinkTraps=_CssSystemLinkTraps_Object((1,3,6,1,4,1,9,10,44,1,1,1),_CssSystemLinkTraps_Type())
cssSystemLinkTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:cssSystemLinkTraps.setStatus(_A)
_CssGroup_ObjectIdentity=ObjectIdentity
cssGroup=_CssGroup_ObjectIdentity((1,3,6,1,4,1,9,10,44,1,2))
_CssGroupTable_Object=MibTable
cssGroupTable=_CssGroupTable_Object((1,3,6,1,4,1,9,10,44,1,2,1))
if mibBuilder.loadTexts:cssGroupTable.setStatus(_A)
_CssGroupEntry_Object=MibTableRow
cssGroupEntry=_CssGroupEntry_Object((1,3,6,1,4,1,9,10,44,1,2,1,1))
cssGroupEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:cssGroupEntry.setStatus(_A)
_CssGroupID_Type=HubNumber
_CssGroupID_Object=MibTableColumn
cssGroupID=_CssGroupID_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,1),_CssGroupID_Type())
cssGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupID.setStatus(_A)
class _CssGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cisco1538MDS',1),('cisco1538UDS',2),('wsC412M',3),('wsC412',4),('wsC424M',5),('wsC424',6)))
_CssGroupType_Type.__name__=_C
_CssGroupType_Object=MibTableColumn
cssGroupType=_CssGroupType_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,2),_CssGroupType_Type())
cssGroupType.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupType.setStatus(_A)
class _CssGroupSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CssGroupSerialNo_Type.__name__=_F
_CssGroupSerialNo_Object=MibTableColumn
cssGroupSerialNo=_CssGroupSerialNo_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,4),_CssGroupSerialNo_Type())
cssGroupSerialNo.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupSerialNo.setStatus(_A)
class _CssGroupBoardRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CssGroupBoardRevision_Type.__name__=_C
_CssGroupBoardRevision_Object=MibTableColumn
cssGroupBoardRevision=_CssGroupBoardRevision_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,5),_CssGroupBoardRevision_Type())
cssGroupBoardRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupBoardRevision.setStatus(_A)
class _CssGroupAgentBootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CssGroupAgentBootVersion_Type.__name__=_F
_CssGroupAgentBootVersion_Object=MibTableColumn
cssGroupAgentBootVersion=_CssGroupAgentBootVersion_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,6),_CssGroupAgentBootVersion_Type())
cssGroupAgentBootVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupAgentBootVersion.setStatus(_A)
class _CssGroupAgentFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CssGroupAgentFirmwareVersion_Type.__name__=_F
_CssGroupAgentFirmwareVersion_Object=MibTableColumn
cssGroupAgentFirmwareVersion=_CssGroupAgentFirmwareVersion_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,7),_CssGroupAgentFirmwareVersion_Type())
cssGroupAgentFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupAgentFirmwareVersion.setStatus(_A)
class _CssGroupAgentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPresent',1),('primary',2),('backup',3)))
_CssGroupAgentStatus_Type.__name__=_C
_CssGroupAgentStatus_Object=MibTableColumn
cssGroupAgentStatus=_CssGroupAgentStatus_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,8),_CssGroupAgentStatus_Type())
cssGroupAgentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupAgentStatus.setStatus(_A)
_CssGroupAgentPhysAddress_Type=PhysAddress
_CssGroupAgentPhysAddress_Object=MibTableColumn
cssGroupAgentPhysAddress=_CssGroupAgentPhysAddress_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,9),_CssGroupAgentPhysAddress_Type())
cssGroupAgentPhysAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupAgentPhysAddress.setStatus(_A)
class _CssGroupInternalPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_CssGroupInternalPowerState_Type.__name__=_C
_CssGroupInternalPowerState_Object=MibTableColumn
cssGroupInternalPowerState=_CssGroupInternalPowerState_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,12),_CssGroupInternalPowerState_Type())
cssGroupInternalPowerState.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupInternalPowerState.setStatus(_A)
class _CssGroupRedundantPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('healthy',2),('faulty',3)))
_CssGroupRedundantPowerState_Type.__name__=_C
_CssGroupRedundantPowerState_Object=MibTableColumn
cssGroupRedundantPowerState=_CssGroupRedundantPowerState_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,13),_CssGroupRedundantPowerState_Type())
cssGroupRedundantPowerState.setMaxAccess(_D)
if mibBuilder.loadTexts:cssGroupRedundantPowerState.setStatus(_A)
class _CssGroupReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('reset',2)))
_CssGroupReset_Type.__name__=_C
_CssGroupReset_Object=MibTableColumn
cssGroupReset=_CssGroupReset_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,14),_CssGroupReset_Type())
cssGroupReset.setMaxAccess(_E)
if mibBuilder.loadTexts:cssGroupReset.setStatus(_A)
class _CssGroupConfigDefaultReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('reset',2)))
_CssGroupConfigDefaultReset_Type.__name__=_C
_CssGroupConfigDefaultReset_Object=MibTableColumn
cssGroupConfigDefaultReset=_CssGroupConfigDefaultReset_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,15),_CssGroupConfigDefaultReset_Type())
cssGroupConfigDefaultReset.setMaxAccess(_E)
if mibBuilder.loadTexts:cssGroupConfigDefaultReset.setStatus(_A)
class _CssGroupIsolatedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('isolated',1),('attached',2)))
_CssGroupIsolatedState_Type.__name__=_C
_CssGroupIsolatedState_Object=MibTableColumn
cssGroupIsolatedState=_CssGroupIsolatedState_Object((1,3,6,1,4,1,9,10,44,1,2,1,1,16),_CssGroupIsolatedState_Type())
cssGroupIsolatedState.setMaxAccess(_E)
if mibBuilder.loadTexts:cssGroupIsolatedState.setStatus(_A)
_CssRepeaterPort_ObjectIdentity=ObjectIdentity
cssRepeaterPort=_CssRepeaterPort_ObjectIdentity((1,3,6,1,4,1,9,10,44,1,3))
_CssRepeaterPortTable_Object=MibTable
cssRepeaterPortTable=_CssRepeaterPortTable_Object((1,3,6,1,4,1,9,10,44,1,3,1))
if mibBuilder.loadTexts:cssRepeaterPortTable.setStatus(_A)
_CssRepeaterPortEntry_Object=MibTableRow
cssRepeaterPortEntry=_CssRepeaterPortEntry_Object((1,3,6,1,4,1,9,10,44,1,3,1,1))
cssRepeaterPortEntry.setIndexNames((0,_G,_P),(0,_G,_Q))
if mibBuilder.loadTexts:cssRepeaterPortEntry.setStatus(_A)
class _CssRepeaterPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CssRepeaterPortName_Type.__name__=_F
_CssRepeaterPortName_Object=MibTableColumn
cssRepeaterPortName=_CssRepeaterPortName_Object((1,3,6,1,4,1,9,10,44,1,3,1,1,1),_CssRepeaterPortName_Type())
cssRepeaterPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:cssRepeaterPortName.setStatus(_A)
class _CssRepeaterPortControllerRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CssRepeaterPortControllerRevision_Type.__name__=_C
_CssRepeaterPortControllerRevision_Object=MibTableColumn
cssRepeaterPortControllerRevision=_CssRepeaterPortControllerRevision_Object((1,3,6,1,4,1,9,10,44,1,3,1,1,2),_CssRepeaterPortControllerRevision_Type())
cssRepeaterPortControllerRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:cssRepeaterPortControllerRevision.setStatus(_A)
class _CssRepeaterPortSpeedAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_K,3)))
_CssRepeaterPortSpeedAdmin_Type.__name__=_C
_CssRepeaterPortSpeedAdmin_Object=MibTableColumn
cssRepeaterPortSpeedAdmin=_CssRepeaterPortSpeedAdmin_Object((1,3,6,1,4,1,9,10,44,1,3,1,1,3),_CssRepeaterPortSpeedAdmin_Type())
cssRepeaterPortSpeedAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:cssRepeaterPortSpeedAdmin.setStatus(_A)
class _CssRepeaterPortSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_CssRepeaterPortSpeedStatus_Type.__name__=_C
_CssRepeaterPortSpeedStatus_Object=MibTableColumn
cssRepeaterPortSpeedStatus=_CssRepeaterPortSpeedStatus_Object((1,3,6,1,4,1,9,10,44,1,3,1,1,4),_CssRepeaterPortSpeedStatus_Type())
cssRepeaterPortSpeedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cssRepeaterPortSpeedStatus.setStatus(_A)
class _CssRepeaterPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link',1),(_U,2)))
_CssRepeaterPortLinkStatus_Type.__name__=_C
_CssRepeaterPortLinkStatus_Object=MibTableColumn
cssRepeaterPortLinkStatus=_CssRepeaterPortLinkStatus_Object((1,3,6,1,4,1,9,10,44,1,3,1,1,5),_CssRepeaterPortLinkStatus_Type())
cssRepeaterPortLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cssRepeaterPortLinkStatus.setStatus(_A)
_CssSwitchPort_ObjectIdentity=ObjectIdentity
cssSwitchPort=_CssSwitchPort_ObjectIdentity((1,3,6,1,4,1,9,10,44,1,4))
_CssSwitchPortTable_Object=MibTable
cssSwitchPortTable=_CssSwitchPortTable_Object((1,3,6,1,4,1,9,10,44,1,4,1))
if mibBuilder.loadTexts:cssSwitchPortTable.setStatus(_A)
_CssSwitchPortEntry_Object=MibTableRow
cssSwitchPortEntry=_CssSwitchPortEntry_Object((1,3,6,1,4,1,9,10,44,1,4,1,1))
cssSwitchPortEntry.setIndexNames((0,_G,_J),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:cssSwitchPortEntry.setStatus(_A)
class _CssSwitchPortModuleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CssSwitchPortModuleID_Type.__name__=_C
_CssSwitchPortModuleID_Object=MibTableColumn
cssSwitchPortModuleID=_CssSwitchPortModuleID_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,1),_CssSwitchPortModuleID_Type())
cssSwitchPortModuleID.setMaxAccess(_D)
if mibBuilder.loadTexts:cssSwitchPortModuleID.setStatus(_A)
class _CssSwitchPortPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CssSwitchPortPortID_Type.__name__=_C
_CssSwitchPortPortID_Object=MibTableColumn
cssSwitchPortPortID=_CssSwitchPortPortID_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,2),_CssSwitchPortPortID_Type())
cssSwitchPortPortID.setMaxAccess(_D)
if mibBuilder.loadTexts:cssSwitchPortPortID.setStatus(_A)
class _CssSwitchPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CssSwitchPortName_Type.__name__=_F
_CssSwitchPortName_Object=MibTableColumn
cssSwitchPortName=_CssSwitchPortName_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,3),_CssSwitchPortName_Type())
cssSwitchPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:cssSwitchPortName.setStatus(_A)
class _CssSwitchPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wsX4001',1),('wsX4002',2)))
_CssSwitchPortType_Type.__name__=_C
_CssSwitchPortType_Object=MibTableColumn
cssSwitchPortType=_CssSwitchPortType_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,4),_CssSwitchPortType_Type())
cssSwitchPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:cssSwitchPortType.setStatus(_A)
class _CssSwitchPortControllerRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CssSwitchPortControllerRevision_Type.__name__=_C
_CssSwitchPortControllerRevision_Object=MibTableColumn
cssSwitchPortControllerRevision=_CssSwitchPortControllerRevision_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,5),_CssSwitchPortControllerRevision_Type())
cssSwitchPortControllerRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:cssSwitchPortControllerRevision.setStatus(_A)
class _CssSwitchPortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_CssSwitchPortState_Type.__name__=_C
_CssSwitchPortState_Object=MibTableColumn
cssSwitchPortState=_CssSwitchPortState_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,6),_CssSwitchPortState_Type())
cssSwitchPortState.setMaxAccess(_E)
if mibBuilder.loadTexts:cssSwitchPortState.setStatus(_A)
class _CssSwitchPortDuplexAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),(_K,3)))
_CssSwitchPortDuplexAdmin_Type.__name__=_C
_CssSwitchPortDuplexAdmin_Object=MibTableColumn
cssSwitchPortDuplexAdmin=_CssSwitchPortDuplexAdmin_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,7),_CssSwitchPortDuplexAdmin_Type())
cssSwitchPortDuplexAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:cssSwitchPortDuplexAdmin.setStatus(_A)
class _CssSwitchPortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_CssSwitchPortDuplexStatus_Type.__name__=_C
_CssSwitchPortDuplexStatus_Object=MibTableColumn
cssSwitchPortDuplexStatus=_CssSwitchPortDuplexStatus_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,8),_CssSwitchPortDuplexStatus_Type())
cssSwitchPortDuplexStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cssSwitchPortDuplexStatus.setStatus(_A)
class _CssSwitchPortSpeedAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_K,3)))
_CssSwitchPortSpeedAdmin_Type.__name__=_C
_CssSwitchPortSpeedAdmin_Object=MibTableColumn
cssSwitchPortSpeedAdmin=_CssSwitchPortSpeedAdmin_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,9),_CssSwitchPortSpeedAdmin_Type())
cssSwitchPortSpeedAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:cssSwitchPortSpeedAdmin.setStatus(_A)
class _CssSwitchPortSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_CssSwitchPortSpeedStatus_Type.__name__=_C
_CssSwitchPortSpeedStatus_Object=MibTableColumn
cssSwitchPortSpeedStatus=_CssSwitchPortSpeedStatus_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,10),_CssSwitchPortSpeedStatus_Type())
cssSwitchPortSpeedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cssSwitchPortSpeedStatus.setStatus(_A)
class _CssSwitchPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link',1),(_U,2)))
_CssSwitchPortLinkStatus_Type.__name__=_C
_CssSwitchPortLinkStatus_Object=MibTableColumn
cssSwitchPortLinkStatus=_CssSwitchPortLinkStatus_Object((1,3,6,1,4,1,9,10,44,1,4,1,1,11),_CssSwitchPortLinkStatus_Type())
cssSwitchPortLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cssSwitchPortLinkStatus.setStatus(_A)
_CiscoSibuStackableDualSpeedHubNotifications_ObjectIdentity=ObjectIdentity
ciscoSibuStackableDualSpeedHubNotifications=_CiscoSibuStackableDualSpeedHubNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,44,2))
_CiscoSibuStackableDualSpeedHubNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoSibuStackableDualSpeedHubNotificationsPrefix=_CiscoSibuStackableDualSpeedHubNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,44,2,0))
_CiscoSibuStackableDualSpeedHubMIBComformance_ObjectIdentity=ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBComformance=_CiscoSibuStackableDualSpeedHubMIBComformance_ObjectIdentity((1,3,6,1,4,1,9,10,44,3))
_CiscoSibuStackableDualSpeedHubMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBCompliances=_CiscoSibuStackableDualSpeedHubMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,44,3,1))
_CiscoSibuStackableDualSpeedHubMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSibuStackableDualSpeedHubMIBGroups=_CiscoSibuStackableDualSpeedHubMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,44,3,2))
ciscoSibuStackableDualSpeedHubGroup=ObjectGroup((1,3,6,1,4,1,9,10,44,3,2,1))
ciscoSibuStackableDualSpeedHubGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoSibuStackableDualSpeedHubGroup.setStatus(_A)
ciscoSibuStackableDualSpeedHubRepeaterPortGroup=ObjectGroup((1,3,6,1,4,1,9,10,44,3,2,2))
ciscoSibuStackableDualSpeedHubRepeaterPortGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_N)))
if mibBuilder.loadTexts:ciscoSibuStackableDualSpeedHubRepeaterPortGroup.setStatus(_A)
ciscoSibuStackableDualSpeedHubSwitchPortGroup=ObjectGroup((1,3,6,1,4,1,9,10,44,3,2,3))
ciscoSibuStackableDualSpeedHubSwitchPortGroup.setObjects(*((_B,_L),(_B,_M),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_O)))
if mibBuilder.loadTexts:ciscoSibuStackableDualSpeedHubSwitchPortGroup.setStatus(_A)
ciscoSibuStackableDualSpeedHubRptrPortLinkChange=NotificationType((1,3,6,1,4,1,9,10,44,2,0,1))
ciscoSibuStackableDualSpeedHubRptrPortLinkChange.setObjects((_B,_N))
if mibBuilder.loadTexts:ciscoSibuStackableDualSpeedHubRptrPortLinkChange.setStatus(_A)
ciscoSibuStackableDualSpeedHubSwitchPortLinkChange=NotificationType((1,3,6,1,4,1,9,10,44,2,0,2))
ciscoSibuStackableDualSpeedHubSwitchPortLinkChange.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoSibuStackableDualSpeedHubSwitchPortLinkChange.setStatus(_A)
ciscoSibuStackableDualSpeedHubCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,44,3,1,1))
ciscoSibuStackableDualSpeedHubCompliance.setObjects(*((_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ciscoSibuStackableDualSpeedHubCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HubNumber':HubNumber,'ciscoSibuStackableDualSpeedHubMIB':ciscoSibuStackableDualSpeedHubMIB,'ciscoSibuStackableDualSpeedHubMIBObjects':ciscoSibuStackableDualSpeedHubMIBObjects,'cssSystem':cssSystem,_X:cssSystemLinkTraps,'cssGroup':cssGroup,'cssGroupTable':cssGroupTable,'cssGroupEntry':cssGroupEntry,_Y:cssGroupID,_Z:cssGroupType,_a:cssGroupSerialNo,_b:cssGroupBoardRevision,_c:cssGroupAgentBootVersion,_d:cssGroupAgentFirmwareVersion,_e:cssGroupAgentStatus,_f:cssGroupAgentPhysAddress,_g:cssGroupInternalPowerState,_h:cssGroupRedundantPowerState,_i:cssGroupReset,_j:cssGroupConfigDefaultReset,_k:cssGroupIsolatedState,'cssRepeaterPort':cssRepeaterPort,'cssRepeaterPortTable':cssRepeaterPortTable,'cssRepeaterPortEntry':cssRepeaterPortEntry,_l:cssRepeaterPortName,_m:cssRepeaterPortControllerRevision,_n:cssRepeaterPortSpeedAdmin,_o:cssRepeaterPortSpeedStatus,_N:cssRepeaterPortLinkStatus,'cssSwitchPort':cssSwitchPort,'cssSwitchPortTable':cssSwitchPortTable,'cssSwitchPortEntry':cssSwitchPortEntry,_L:cssSwitchPortModuleID,_M:cssSwitchPortPortID,_p:cssSwitchPortName,_q:cssSwitchPortType,_r:cssSwitchPortControllerRevision,_s:cssSwitchPortState,_t:cssSwitchPortDuplexAdmin,_u:cssSwitchPortDuplexStatus,_v:cssSwitchPortSpeedAdmin,_w:cssSwitchPortSpeedStatus,_O:cssSwitchPortLinkStatus,'ciscoSibuStackableDualSpeedHubNotifications':ciscoSibuStackableDualSpeedHubNotifications,'ciscoSibuStackableDualSpeedHubNotificationsPrefix':ciscoSibuStackableDualSpeedHubNotificationsPrefix,'ciscoSibuStackableDualSpeedHubRptrPortLinkChange':ciscoSibuStackableDualSpeedHubRptrPortLinkChange,'ciscoSibuStackableDualSpeedHubSwitchPortLinkChange':ciscoSibuStackableDualSpeedHubSwitchPortLinkChange,'ciscoSibuStackableDualSpeedHubMIBComformance':ciscoSibuStackableDualSpeedHubMIBComformance,'ciscoSibuStackableDualSpeedHubMIBCompliances':ciscoSibuStackableDualSpeedHubMIBCompliances,'ciscoSibuStackableDualSpeedHubCompliance':ciscoSibuStackableDualSpeedHubCompliance,'ciscoSibuStackableDualSpeedHubMIBGroups':ciscoSibuStackableDualSpeedHubMIBGroups,_x:ciscoSibuStackableDualSpeedHubGroup,_y:ciscoSibuStackableDualSpeedHubRepeaterPortGroup,_z:ciscoSibuStackableDualSpeedHubSwitchPortGroup})