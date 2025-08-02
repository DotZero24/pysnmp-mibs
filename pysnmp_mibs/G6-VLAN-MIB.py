_X='mvrpStatusPortIndex'
_W='portStatusPortIndex'
_V='statusVlanIndex'
_U='fabricAttachPortConfigPortIndex'
_T='mvrpPortConfigPortIndex'
_S='filterConfigIndex'
_R='portConfigPortIndex'
_Q='vlanIdConfigIndex'
_P='priority7'
_O='priority6'
_N='priority5'
_M='priority4'
_L='priority3'
_K='priority2'
_J='priority1'
_I='priority0'
_H='not-accessible'
_G='G6-VLAN-MIB'
_F='enabled'
_E='disabled'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,82))
class _VlanEnableVlanFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_VlanEnableVlanFiltering_Type.__name__=_B
_VlanEnableVlanFiltering_Object=MibScalar
vlanEnableVlanFiltering=_VlanEnableVlanFiltering_Object((1,3,6,1,4,1,3181,10,6,2,82,1),_VlanEnableVlanFiltering_Type())
vlanEnableVlanFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanEnableVlanFiltering.setStatus(_A)
_VlanIdConfigTable_Object=MibTable
vlanIdConfigTable=_VlanIdConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,82,2))
if mibBuilder.loadTexts:vlanIdConfigTable.setStatus(_A)
_VlanIdConfigEntry_Object=MibTableRow
vlanIdConfigEntry=_VlanIdConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1))
vlanIdConfigEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:vlanIdConfigEntry.setStatus(_A)
class _VlanIdConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_VlanIdConfigIndex_Type.__name__=_B
_VlanIdConfigIndex_Object=MibTableColumn
vlanIdConfigIndex=_VlanIdConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1,1),_VlanIdConfigIndex_Type())
vlanIdConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:vlanIdConfigIndex.setStatus(_A)
class _VlanIdConfigManagementVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanIdConfigManagementVlanId_Type.__name__=_B
_VlanIdConfigManagementVlanId_Object=MibTableColumn
vlanIdConfigManagementVlanId=_VlanIdConfigManagementVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1,2),_VlanIdConfigManagementVlanId_Type())
vlanIdConfigManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanIdConfigManagementVlanId.setStatus(_A)
class _VlanIdConfigManagementPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_VlanIdConfigManagementPriority_Type.__name__=_B
_VlanIdConfigManagementPriority_Object=MibTableColumn
vlanIdConfigManagementPriority=_VlanIdConfigManagementPriority_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1,3),_VlanIdConfigManagementPriority_Type())
vlanIdConfigManagementPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanIdConfigManagementPriority.setStatus(_A)
class _VlanIdConfigVoiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanIdConfigVoiceVlanId_Type.__name__=_B
_VlanIdConfigVoiceVlanId_Object=MibTableColumn
vlanIdConfigVoiceVlanId=_VlanIdConfigVoiceVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1,4),_VlanIdConfigVoiceVlanId_Type())
vlanIdConfigVoiceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanIdConfigVoiceVlanId.setStatus(_A)
class _VlanIdConfigRstpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanIdConfigRstpVlanId_Type.__name__=_B
_VlanIdConfigRstpVlanId_Object=MibTableColumn
vlanIdConfigRstpVlanId=_VlanIdConfigRstpVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1,5),_VlanIdConfigRstpVlanId_Type())
vlanIdConfigRstpVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanIdConfigRstpVlanId.setStatus(_A)
class _VlanIdConfigUnauthorizedVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanIdConfigUnauthorizedVlanId_Type.__name__=_B
_VlanIdConfigUnauthorizedVlanId_Object=MibTableColumn
vlanIdConfigUnauthorizedVlanId=_VlanIdConfigUnauthorizedVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1,6),_VlanIdConfigUnauthorizedVlanId_Type())
vlanIdConfigUnauthorizedVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanIdConfigUnauthorizedVlanId.setStatus(_A)
class _VlanIdConfigSmartofficeVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanIdConfigSmartofficeVlanId_Type.__name__=_B
_VlanIdConfigSmartofficeVlanId_Object=MibTableColumn
vlanIdConfigSmartofficeVlanId=_VlanIdConfigSmartofficeVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,2,1,7),_VlanIdConfigSmartofficeVlanId_Type())
vlanIdConfigSmartofficeVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanIdConfigSmartofficeVlanId.setStatus(_A)
_PortConfigTable_Object=MibTable
portConfigTable=_PortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,82,3))
if mibBuilder.loadTexts:portConfigTable.setStatus(_A)
_PortConfigEntry_Object=MibTableRow
portConfigEntry=_PortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1))
portConfigEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:portConfigEntry.setStatus(_A)
class _PortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortConfigPortIndex_Type.__name__=_B
_PortConfigPortIndex_Object=MibTableColumn
portConfigPortIndex=_PortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,1),_PortConfigPortIndex_Type())
portConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portConfigPortIndex.setStatus(_A)
class _PortConfigVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('access',0),('hybrid',1),('trunk',2),('qInQCustomer',3),('qInQProvider',4)))
_PortConfigVlanMode_Type.__name__=_B
_PortConfigVlanMode_Object=MibTableColumn
portConfigVlanMode=_PortConfigVlanMode_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,2),_PortConfigVlanMode_Type())
portConfigVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigVlanMode.setStatus(_A)
class _PortConfigDefaultVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortConfigDefaultVlanId_Type.__name__=_B
_PortConfigDefaultVlanId_Object=MibTableColumn
portConfigDefaultVlanId=_PortConfigDefaultVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,3),_PortConfigDefaultVlanId_Type())
portConfigDefaultVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigDefaultVlanId.setStatus(_A)
class _PortConfigForceDefaultVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortConfigForceDefaultVlanId_Type.__name__=_B
_PortConfigForceDefaultVlanId_Object=MibTableColumn
portConfigForceDefaultVlanId=_PortConfigForceDefaultVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,4),_PortConfigForceDefaultVlanId_Type())
portConfigForceDefaultVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigForceDefaultVlanId.setStatus(_A)
class _PortConfigDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_PortConfigDefaultPriority_Type.__name__=_B
_PortConfigDefaultPriority_Object=MibTableColumn
portConfigDefaultPriority=_PortConfigDefaultPriority_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,5),_PortConfigDefaultPriority_Type())
portConfigDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigDefaultPriority.setStatus(_A)
class _PortConfigPriorityOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PortConfigPriorityOverride_Type.__name__=_B
_PortConfigPriorityOverride_Object=MibTableColumn
portConfigPriorityOverride=_PortConfigPriorityOverride_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,6),_PortConfigPriorityOverride_Type())
portConfigPriorityOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigPriorityOverride.setStatus(_A)
class _PortConfigUnauthorizedVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortConfigUnauthorizedVlanId_Type.__name__=_B
_PortConfigUnauthorizedVlanId_Object=MibTableColumn
portConfigUnauthorizedVlanId=_PortConfigUnauthorizedVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,7),_PortConfigUnauthorizedVlanId_Type())
portConfigUnauthorizedVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigUnauthorizedVlanId.setStatus(_A)
class _PortConfigFallbackVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortConfigFallbackVlanId_Type.__name__=_B
_PortConfigFallbackVlanId_Object=MibTableColumn
portConfigFallbackVlanId=_PortConfigFallbackVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,8),_PortConfigFallbackVlanId_Type())
portConfigFallbackVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigFallbackVlanId.setStatus(_A)
class _PortConfigQInQEthertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ox88a8',0),('ox9100',1),('ox9200',2),('ox8100',3)))
_PortConfigQInQEthertype_Type.__name__=_B
_PortConfigQInQEthertype_Object=MibTableColumn
portConfigQInQEthertype=_PortConfigQInQEthertype_Object((1,3,6,1,4,1,3181,10,6,2,82,3,1,9),_PortConfigQInQEthertype_Type())
portConfigQInQEthertype.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigQInQEthertype.setStatus(_A)
_FilterConfigTable_Object=MibTable
filterConfigTable=_FilterConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,82,4))
if mibBuilder.loadTexts:filterConfigTable.setStatus(_A)
_FilterConfigEntry_Object=MibTableRow
filterConfigEntry=_FilterConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1))
filterConfigEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:filterConfigEntry.setStatus(_A)
class _FilterConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FilterConfigIndex_Type.__name__=_B
_FilterConfigIndex_Object=MibTableColumn
filterConfigIndex=_FilterConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,1),_FilterConfigIndex_Type())
filterConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:filterConfigIndex.setStatus(_A)
_FilterConfigVlanId_Type=DisplayString
_FilterConfigVlanId_Object=MibTableColumn
filterConfigVlanId=_FilterConfigVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,2),_FilterConfigVlanId_Type())
filterConfigVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigVlanId.setStatus(_A)
class _FilterConfigEntryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FilterConfigEntryMode_Type.__name__=_B
_FilterConfigEntryMode_Object=MibTableColumn
filterConfigEntryMode=_FilterConfigEntryMode_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,3),_FilterConfigEntryMode_Type())
filterConfigEntryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigEntryMode.setStatus(_A)
_FilterConfigAlias_Type=DisplayString
_FilterConfigAlias_Object=MibTableColumn
filterConfigAlias=_FilterConfigAlias_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,4),_FilterConfigAlias_Type())
filterConfigAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigAlias.setStatus(_A)
class _FilterConfigMstpGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FilterConfigMstpGroup_Type.__name__=_B
_FilterConfigMstpGroup_Object=MibTableColumn
filterConfigMstpGroup=_FilterConfigMstpGroup_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,5),_FilterConfigMstpGroup_Type())
filterConfigMstpGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigMstpGroup.setStatus(_A)
_FilterConfigFabricAttachISid_Type=Unsigned32
_FilterConfigFabricAttachISid_Object=MibTableColumn
filterConfigFabricAttachISid=_FilterConfigFabricAttachISid_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,6),_FilterConfigFabricAttachISid_Type())
filterConfigFabricAttachISid.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigFabricAttachISid.setStatus(_A)
_FilterConfigPortMembers_Type=Integer32
_FilterConfigPortMembers_Object=MibTableColumn
filterConfigPortMembers=_FilterConfigPortMembers_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,7),_FilterConfigPortMembers_Type())
filterConfigPortMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigPortMembers.setStatus(_A)
class _FilterConfigManagementMembers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('cpu1',1),('cpu2',2),('all',3)))
_FilterConfigManagementMembers_Type.__name__=_B
_FilterConfigManagementMembers_Object=MibTableColumn
filterConfigManagementMembers=_FilterConfigManagementMembers_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,8),_FilterConfigManagementMembers_Type())
filterConfigManagementMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigManagementMembers.setStatus(_A)
class _FilterConfigPriorityOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FilterConfigPriorityOverride_Type.__name__=_B
_FilterConfigPriorityOverride_Object=MibTableColumn
filterConfigPriorityOverride=_FilterConfigPriorityOverride_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,9),_FilterConfigPriorityOverride_Type())
filterConfigPriorityOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigPriorityOverride.setStatus(_A)
class _FilterConfigNewPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_FilterConfigNewPriority_Type.__name__=_B
_FilterConfigNewPriority_Object=MibTableColumn
filterConfigNewPriority=_FilterConfigNewPriority_Object((1,3,6,1,4,1,3181,10,6,2,82,4,1,10),_FilterConfigNewPriority_Type())
filterConfigNewPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:filterConfigNewPriority.setStatus(_A)
class _VlanEnableMvrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_VlanEnableMvrp_Type.__name__=_B
_VlanEnableMvrp_Object=MibScalar
vlanEnableMvrp=_VlanEnableMvrp_Object((1,3,6,1,4,1,3181,10,6,2,82,5),_VlanEnableMvrp_Type())
vlanEnableMvrp.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanEnableMvrp.setStatus(_A)
_MvrpPortConfigTable_Object=MibTable
mvrpPortConfigTable=_MvrpPortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,82,6))
if mibBuilder.loadTexts:mvrpPortConfigTable.setStatus(_A)
_MvrpPortConfigEntry_Object=MibTableRow
mvrpPortConfigEntry=_MvrpPortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,6,1))
mvrpPortConfigEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:mvrpPortConfigEntry.setStatus(_A)
class _MvrpPortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_MvrpPortConfigPortIndex_Type.__name__=_B
_MvrpPortConfigPortIndex_Object=MibTableColumn
mvrpPortConfigPortIndex=_MvrpPortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,6,1,1),_MvrpPortConfigPortIndex_Type())
mvrpPortConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mvrpPortConfigPortIndex.setStatus(_A)
class _MvrpPortConfigEnableMvrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MvrpPortConfigEnableMvrp_Type.__name__=_B
_MvrpPortConfigEnableMvrp_Object=MibTableColumn
mvrpPortConfigEnableMvrp=_MvrpPortConfigEnableMvrp_Object((1,3,6,1,4,1,3181,10,6,2,82,6,1,2),_MvrpPortConfigEnableMvrp_Type())
mvrpPortConfigEnableMvrp.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrpPortConfigEnableMvrp.setStatus(_A)
class _MvrpPortConfigRegistrationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('fixed',1),('forbidden',2)))
_MvrpPortConfigRegistrationMode_Type.__name__=_B
_MvrpPortConfigRegistrationMode_Object=MibTableColumn
mvrpPortConfigRegistrationMode=_MvrpPortConfigRegistrationMode_Object((1,3,6,1,4,1,3181,10,6,2,82,6,1,3),_MvrpPortConfigRegistrationMode_Type())
mvrpPortConfigRegistrationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrpPortConfigRegistrationMode.setStatus(_A)
_MvrpPortConfigJoinTimer_Type=Unsigned32
_MvrpPortConfigJoinTimer_Object=MibTableColumn
mvrpPortConfigJoinTimer=_MvrpPortConfigJoinTimer_Object((1,3,6,1,4,1,3181,10,6,2,82,6,1,4),_MvrpPortConfigJoinTimer_Type())
mvrpPortConfigJoinTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrpPortConfigJoinTimer.setStatus(_A)
_MvrpPortConfigLeaveTimer_Type=Unsigned32
_MvrpPortConfigLeaveTimer_Object=MibTableColumn
mvrpPortConfigLeaveTimer=_MvrpPortConfigLeaveTimer_Object((1,3,6,1,4,1,3181,10,6,2,82,6,1,5),_MvrpPortConfigLeaveTimer_Type())
mvrpPortConfigLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrpPortConfigLeaveTimer.setStatus(_A)
_MvrpPortConfigLeaveallTimer_Type=Unsigned32
_MvrpPortConfigLeaveallTimer_Object=MibTableColumn
mvrpPortConfigLeaveallTimer=_MvrpPortConfigLeaveallTimer_Object((1,3,6,1,4,1,3181,10,6,2,82,6,1,6),_MvrpPortConfigLeaveallTimer_Type())
mvrpPortConfigLeaveallTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrpPortConfigLeaveallTimer.setStatus(_A)
_FabricAttachPortConfigTable_Object=MibTable
fabricAttachPortConfigTable=_FabricAttachPortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,82,7))
if mibBuilder.loadTexts:fabricAttachPortConfigTable.setStatus(_A)
_FabricAttachPortConfigEntry_Object=MibTableRow
fabricAttachPortConfigEntry=_FabricAttachPortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,7,1))
fabricAttachPortConfigEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:fabricAttachPortConfigEntry.setStatus(_A)
class _FabricAttachPortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_FabricAttachPortConfigPortIndex_Type.__name__=_B
_FabricAttachPortConfigPortIndex_Object=MibTableColumn
fabricAttachPortConfigPortIndex=_FabricAttachPortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,7,1,1),_FabricAttachPortConfigPortIndex_Type())
fabricAttachPortConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fabricAttachPortConfigPortIndex.setStatus(_A)
class _FabricAttachPortConfigEnableFabricAttach_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FabricAttachPortConfigEnableFabricAttach_Type.__name__=_B
_FabricAttachPortConfigEnableFabricAttach_Object=MibTableColumn
fabricAttachPortConfigEnableFabricAttach=_FabricAttachPortConfigEnableFabricAttach_Object((1,3,6,1,4,1,3181,10,6,2,82,7,1,2),_FabricAttachPortConfigEnableFabricAttach_Type())
fabricAttachPortConfigEnableFabricAttach.setMaxAccess(_C)
if mibBuilder.loadTexts:fabricAttachPortConfigEnableFabricAttach.setStatus(_A)
class _FabricAttachPortConfigMsgAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FabricAttachPortConfigMsgAuthentication_Type.__name__=_B
_FabricAttachPortConfigMsgAuthentication_Object=MibTableColumn
fabricAttachPortConfigMsgAuthentication=_FabricAttachPortConfigMsgAuthentication_Object((1,3,6,1,4,1,3181,10,6,2,82,7,1,3),_FabricAttachPortConfigMsgAuthentication_Type())
fabricAttachPortConfigMsgAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:fabricAttachPortConfigMsgAuthentication.setStatus(_A)
_FabricAttachPortConfigEnterFaAuthKey_Type=DisplayString
_FabricAttachPortConfigEnterFaAuthKey_Object=MibTableColumn
fabricAttachPortConfigEnterFaAuthKey=_FabricAttachPortConfigEnterFaAuthKey_Object((1,3,6,1,4,1,3181,10,6,2,82,7,1,4),_FabricAttachPortConfigEnterFaAuthKey_Type())
fabricAttachPortConfigEnterFaAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:fabricAttachPortConfigEnterFaAuthKey.setStatus(_A)
_FabricAttachPortConfigEncryptedFaAuthKey_Type=DisplayString
_FabricAttachPortConfigEncryptedFaAuthKey_Object=MibTableColumn
fabricAttachPortConfigEncryptedFaAuthKey=_FabricAttachPortConfigEncryptedFaAuthKey_Object((1,3,6,1,4,1,3181,10,6,2,82,7,1,5),_FabricAttachPortConfigEncryptedFaAuthKey_Type())
fabricAttachPortConfigEncryptedFaAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:fabricAttachPortConfigEncryptedFaAuthKey.setStatus(_A)
class _VlanNumberOfEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanNumberOfEntries_Type.__name__=_B
_VlanNumberOfEntries_Object=MibScalar
vlanNumberOfEntries=_VlanNumberOfEntries_Object((1,3,6,1,4,1,3181,10,6,2,82,100),_VlanNumberOfEntries_Type())
vlanNumberOfEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNumberOfEntries.setStatus(_A)
_StatusTable_Object=MibTable
statusTable=_StatusTable_Object((1,3,6,1,4,1,3181,10,6,2,82,101))
if mibBuilder.loadTexts:statusTable.setStatus(_A)
_StatusEntry_Object=MibTableRow
statusEntry=_StatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1))
statusEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:statusEntry.setStatus(_A)
class _StatusVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StatusVlanIndex_Type.__name__=_B
_StatusVlanIndex_Object=MibTableColumn
statusVlanIndex=_StatusVlanIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,1),_StatusVlanIndex_Type())
statusVlanIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:statusVlanIndex.setStatus(_A)
class _StatusVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StatusVlanId_Type.__name__=_B
_StatusVlanId_Object=MibTableColumn
statusVlanId=_StatusVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,2),_StatusVlanId_Type())
statusVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:statusVlanId.setStatus(_A)
_StatusTimeMark_Type=Unsigned32
_StatusTimeMark_Object=MibTableColumn
statusTimeMark=_StatusTimeMark_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,3),_StatusTimeMark_Type())
statusTimeMark.setMaxAccess(_D)
if mibBuilder.loadTexts:statusTimeMark.setStatus(_A)
_StatusAlias_Type=DisplayString
_StatusAlias_Object=MibTableColumn
statusAlias=_StatusAlias_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,4),_StatusAlias_Type())
statusAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:statusAlias.setStatus(_A)
_StatusPortMembers_Type=Integer32
_StatusPortMembers_Object=MibTableColumn
statusPortMembers=_StatusPortMembers_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,5),_StatusPortMembers_Type())
statusPortMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:statusPortMembers.setStatus(_A)
_StatusFilterDatabase_Type=Unsigned32
_StatusFilterDatabase_Object=MibTableColumn
statusFilterDatabase=_StatusFilterDatabase_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,6),_StatusFilterDatabase_Type())
statusFilterDatabase.setMaxAccess(_D)
if mibBuilder.loadTexts:statusFilterDatabase.setStatus(_A)
_StatusEgressPorts_Type=Integer32
_StatusEgressPorts_Object=MibTableColumn
statusEgressPorts=_StatusEgressPorts_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,7),_StatusEgressPorts_Type())
statusEgressPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:statusEgressPorts.setStatus(_A)
_StatusUntaggedPorts_Type=Integer32
_StatusUntaggedPorts_Object=MibTableColumn
statusUntaggedPorts=_StatusUntaggedPorts_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,8),_StatusUntaggedPorts_Type())
statusUntaggedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:statusUntaggedPorts.setStatus(_A)
class _StatusFabricAttachState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('active',1),('rejected',2)))
_StatusFabricAttachState_Type.__name__=_B
_StatusFabricAttachState_Object=MibTableColumn
statusFabricAttachState=_StatusFabricAttachState_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,9),_StatusFabricAttachState_Type())
statusFabricAttachState.setMaxAccess(_D)
if mibBuilder.loadTexts:statusFabricAttachState.setStatus(_A)
class _StatusCreationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('filterTable',0),('pacc',1),('mvrp',2)))
_StatusCreationMode_Type.__name__=_B
_StatusCreationMode_Object=MibTableColumn
statusCreationMode=_StatusCreationMode_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,10),_StatusCreationMode_Type())
statusCreationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:statusCreationMode.setStatus(_A)
_StatusCreationTime_Type=Counter32
_StatusCreationTime_Object=MibTableColumn
statusCreationTime=_StatusCreationTime_Object((1,3,6,1,4,1,3181,10,6,2,82,101,1,11),_StatusCreationTime_Type())
statusCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:statusCreationTime.setStatus(_A)
_PortStatusTable_Object=MibTable
portStatusTable=_PortStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,82,102))
if mibBuilder.loadTexts:portStatusTable.setStatus(_A)
_PortStatusEntry_Object=MibTableRow
portStatusEntry=_PortStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,102,1))
portStatusEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:portStatusEntry.setStatus(_A)
class _PortStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortStatusPortIndex_Type.__name__=_B
_PortStatusPortIndex_Object=MibTableColumn
portStatusPortIndex=_PortStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,102,1,1),_PortStatusPortIndex_Type())
portStatusPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portStatusPortIndex.setStatus(_A)
_PortStatusAssignedVlanIds_Type=DisplayString
_PortStatusAssignedVlanIds_Object=MibTableColumn
portStatusAssignedVlanIds=_PortStatusAssignedVlanIds_Object((1,3,6,1,4,1,3181,10,6,2,82,102,1,2),_PortStatusAssignedVlanIds_Type())
portStatusAssignedVlanIds.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusAssignedVlanIds.setStatus(_A)
class _PortStatusDynamicDefaultVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortStatusDynamicDefaultVlanId_Type.__name__=_B
_PortStatusDynamicDefaultVlanId_Object=MibTableColumn
portStatusDynamicDefaultVlanId=_PortStatusDynamicDefaultVlanId_Object((1,3,6,1,4,1,3181,10,6,2,82,102,1,3),_PortStatusDynamicDefaultVlanId_Type())
portStatusDynamicDefaultVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusDynamicDefaultVlanId.setStatus(_A)
class _PortStatusLastUpdateMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('config',0),('viaMacTable',1),('macViaRadius',2),('ms8021xViaRadius',3)))
_PortStatusLastUpdateMethod_Type.__name__=_B
_PortStatusLastUpdateMethod_Object=MibTableColumn
portStatusLastUpdateMethod=_PortStatusLastUpdateMethod_Object((1,3,6,1,4,1,3181,10,6,2,82,102,1,4),_PortStatusLastUpdateMethod_Type())
portStatusLastUpdateMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusLastUpdateMethod.setStatus(_A)
_PortStatusLastUpdatingMac_Type=MacAddress
_PortStatusLastUpdatingMac_Object=MibTableColumn
portStatusLastUpdatingMac=_PortStatusLastUpdatingMac_Object((1,3,6,1,4,1,3181,10,6,2,82,102,1,5),_PortStatusLastUpdatingMac_Type())
portStatusLastUpdatingMac.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusLastUpdatingMac.setStatus(_A)
_PortStatusLastUpdateTime_Type=Counter32
_PortStatusLastUpdateTime_Object=MibTableColumn
portStatusLastUpdateTime=_PortStatusLastUpdateTime_Object((1,3,6,1,4,1,3181,10,6,2,82,102,1,6),_PortStatusLastUpdateTime_Type())
portStatusLastUpdateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusLastUpdateTime.setStatus(_A)
_MvrpStatusTable_Object=MibTable
mvrpStatusTable=_MvrpStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,82,103))
if mibBuilder.loadTexts:mvrpStatusTable.setStatus(_A)
_MvrpStatusEntry_Object=MibTableRow
mvrpStatusEntry=_MvrpStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,82,103,1))
mvrpStatusEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:mvrpStatusEntry.setStatus(_A)
class _MvrpStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_MvrpStatusPortIndex_Type.__name__=_B
_MvrpStatusPortIndex_Object=MibTableColumn
mvrpStatusPortIndex=_MvrpStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,82,103,1,1),_MvrpStatusPortIndex_Type())
mvrpStatusPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mvrpStatusPortIndex.setStatus(_A)
_MvrpStatusLastSourceMac_Type=MacAddress
_MvrpStatusLastSourceMac_Object=MibTableColumn
mvrpStatusLastSourceMac=_MvrpStatusLastSourceMac_Object((1,3,6,1,4,1,3181,10,6,2,82,103,1,2),_MvrpStatusLastSourceMac_Type())
mvrpStatusLastSourceMac.setMaxAccess(_D)
if mibBuilder.loadTexts:mvrpStatusLastSourceMac.setStatus(_A)
_MvrpStatusFailedRegistrations_Type=Unsigned32
_MvrpStatusFailedRegistrations_Object=MibTableColumn
mvrpStatusFailedRegistrations=_MvrpStatusFailedRegistrations_Object((1,3,6,1,4,1,3181,10,6,2,82,103,1,3),_MvrpStatusFailedRegistrations_Type())
mvrpStatusFailedRegistrations.setMaxAccess(_D)
if mibBuilder.loadTexts:mvrpStatusFailedRegistrations.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'protocol':protocol,'vlan':vlan,'vlanEnableVlanFiltering':vlanEnableVlanFiltering,'vlanIdConfigTable':vlanIdConfigTable,'vlanIdConfigEntry':vlanIdConfigEntry,_Q:vlanIdConfigIndex,'vlanIdConfigManagementVlanId':vlanIdConfigManagementVlanId,'vlanIdConfigManagementPriority':vlanIdConfigManagementPriority,'vlanIdConfigVoiceVlanId':vlanIdConfigVoiceVlanId,'vlanIdConfigRstpVlanId':vlanIdConfigRstpVlanId,'vlanIdConfigUnauthorizedVlanId':vlanIdConfigUnauthorizedVlanId,'vlanIdConfigSmartofficeVlanId':vlanIdConfigSmartofficeVlanId,'portConfigTable':portConfigTable,'portConfigEntry':portConfigEntry,_R:portConfigPortIndex,'portConfigVlanMode':portConfigVlanMode,'portConfigDefaultVlanId':portConfigDefaultVlanId,'portConfigForceDefaultVlanId':portConfigForceDefaultVlanId,'portConfigDefaultPriority':portConfigDefaultPriority,'portConfigPriorityOverride':portConfigPriorityOverride,'portConfigUnauthorizedVlanId':portConfigUnauthorizedVlanId,'portConfigFallbackVlanId':portConfigFallbackVlanId,'portConfigQInQEthertype':portConfigQInQEthertype,'filterConfigTable':filterConfigTable,'filterConfigEntry':filterConfigEntry,_S:filterConfigIndex,'filterConfigVlanId':filterConfigVlanId,'filterConfigEntryMode':filterConfigEntryMode,'filterConfigAlias':filterConfigAlias,'filterConfigMstpGroup':filterConfigMstpGroup,'filterConfigFabricAttachISid':filterConfigFabricAttachISid,'filterConfigPortMembers':filterConfigPortMembers,'filterConfigManagementMembers':filterConfigManagementMembers,'filterConfigPriorityOverride':filterConfigPriorityOverride,'filterConfigNewPriority':filterConfigNewPriority,'vlanEnableMvrp':vlanEnableMvrp,'mvrpPortConfigTable':mvrpPortConfigTable,'mvrpPortConfigEntry':mvrpPortConfigEntry,_T:mvrpPortConfigPortIndex,'mvrpPortConfigEnableMvrp':mvrpPortConfigEnableMvrp,'mvrpPortConfigRegistrationMode':mvrpPortConfigRegistrationMode,'mvrpPortConfigJoinTimer':mvrpPortConfigJoinTimer,'mvrpPortConfigLeaveTimer':mvrpPortConfigLeaveTimer,'mvrpPortConfigLeaveallTimer':mvrpPortConfigLeaveallTimer,'fabricAttachPortConfigTable':fabricAttachPortConfigTable,'fabricAttachPortConfigEntry':fabricAttachPortConfigEntry,_U:fabricAttachPortConfigPortIndex,'fabricAttachPortConfigEnableFabricAttach':fabricAttachPortConfigEnableFabricAttach,'fabricAttachPortConfigMsgAuthentication':fabricAttachPortConfigMsgAuthentication,'fabricAttachPortConfigEnterFaAuthKey':fabricAttachPortConfigEnterFaAuthKey,'fabricAttachPortConfigEncryptedFaAuthKey':fabricAttachPortConfigEncryptedFaAuthKey,'vlanNumberOfEntries':vlanNumberOfEntries,'statusTable':statusTable,'statusEntry':statusEntry,_V:statusVlanIndex,'statusVlanId':statusVlanId,'statusTimeMark':statusTimeMark,'statusAlias':statusAlias,'statusPortMembers':statusPortMembers,'statusFilterDatabase':statusFilterDatabase,'statusEgressPorts':statusEgressPorts,'statusUntaggedPorts':statusUntaggedPorts,'statusFabricAttachState':statusFabricAttachState,'statusCreationMode':statusCreationMode,'statusCreationTime':statusCreationTime,'portStatusTable':portStatusTable,'portStatusEntry':portStatusEntry,_W:portStatusPortIndex,'portStatusAssignedVlanIds':portStatusAssignedVlanIds,'portStatusDynamicDefaultVlanId':portStatusDynamicDefaultVlanId,'portStatusLastUpdateMethod':portStatusLastUpdateMethod,'portStatusLastUpdatingMac':portStatusLastUpdatingMac,'portStatusLastUpdateTime':portStatusLastUpdateTime,'mvrpStatusTable':mvrpStatusTable,'mvrpStatusEntry':mvrpStatusEntry,_X:mvrpStatusPortIndex,'mvrpStatusLastSourceMac':mvrpStatusLastSourceMac,'mvrpStatusFailedRegistrations':mvrpStatusFailedRegistrations})