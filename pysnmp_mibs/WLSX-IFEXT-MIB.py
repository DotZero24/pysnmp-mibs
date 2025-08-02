_S='ifExtNPortNumber'
_R='ifExtNModuleNumber'
_Q='ifExtNSlotNumber'
_P='testing'
_O='ifExtPortNumber'
_N='ifExtSlotNumber'
_M='ifIndex'
_L='IF-MIB'
_K='Integer32'
_J='OctetString'
_I='ifExtVlanId'
_H='not-accessible'
_G='WLSX-IFEXT-MIB'
_F='DisplayString'
_E='read-create'
_D='read-only'
_C='deprecated'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ArubaDot1dState,ArubaEnableValue,ArubaIfType,ArubaOperStateValue,ArubaPoeState,ArubaPortDuplex,ArubaPortMode,ArubaPortSpeed,ArubaPortType,ArubaVlanValidRange=mibBuilder.importSymbols('ARUBA-TC','ArubaDot1dState','ArubaEnableValue','ArubaIfType','ArubaOperStateValue','ArubaPoeState','ArubaPortDuplex','ArubaPortMode','ArubaPortSpeed','ArubaPortType','ArubaVlanValidRange')
ifIndex,=mibBuilder.importSymbols(_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxIfExtMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,3))
if mibBuilder.loadTexts:wlsxIfExtMIB.setRevisions(('2020-08-14 17:45','1910-01-26 18:06'))
_WlsxIfExtGroup_ObjectIdentity=ObjectIdentity
wlsxIfExtGroup=_WlsxIfExtGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,3,1))
_WlsxIfExtPortTable_Object=MibTable
wlsxIfExtPortTable=_WlsxIfExtPortTable_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1))
if mibBuilder.loadTexts:wlsxIfExtPortTable.setStatus(_C)
_WlsxIfExtPortEntry_Object=MibTableRow
wlsxIfExtPortEntry=_WlsxIfExtPortEntry_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1))
wlsxIfExtPortEntry.setIndexNames((0,_G,_N),(0,_G,_O))
if mibBuilder.loadTexts:wlsxIfExtPortEntry.setStatus(_C)
_IfExtSlotNumber_Type=Integer32
_IfExtSlotNumber_Object=MibTableColumn
ifExtSlotNumber=_IfExtSlotNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,1),_IfExtSlotNumber_Type())
ifExtSlotNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtSlotNumber.setStatus(_C)
_IfExtPortNumber_Type=Integer32
_IfExtPortNumber_Object=MibTableColumn
ifExtPortNumber=_IfExtPortNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,2),_IfExtPortNumber_Type())
ifExtPortNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtPortNumber.setStatus(_C)
_IfExtPortIfIndex_Type=Integer32
_IfExtPortIfIndex_Object=MibTableColumn
ifExtPortIfIndex=_IfExtPortIfIndex_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,3),_IfExtPortIfIndex_Type())
ifExtPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtPortIfIndex.setStatus(_C)
_IfExtAdminState_Type=ArubaEnableValue
_IfExtAdminState_Object=MibTableColumn
ifExtAdminState=_IfExtAdminState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,4),_IfExtAdminState_Type())
ifExtAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtAdminState.setStatus(_C)
class _IfExtOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_P,3)))
_IfExtOperState_Type.__name__=_K
_IfExtOperState_Object=MibTableColumn
ifExtOperState=_IfExtOperState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,5),_IfExtOperState_Type())
ifExtOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtOperState.setStatus(_C)
_IfExtPoeState_Type=ArubaPoeState
_IfExtPoeState_Object=MibTableColumn
ifExtPoeState=_IfExtPoeState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,6),_IfExtPoeState_Type())
ifExtPoeState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtPoeState.setStatus(_C)
_IfExtIsTrusted_Type=TruthValue
_IfExtIsTrusted_Object=MibTableColumn
ifExtIsTrusted=_IfExtIsTrusted_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,7),_IfExtIsTrusted_Type())
ifExtIsTrusted.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtIsTrusted.setStatus(_C)
_IfExtDot1DState_Type=ArubaDot1dState
_IfExtDot1DState_Object=MibTableColumn
ifExtDot1DState=_IfExtDot1DState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,8),_IfExtDot1DState_Type())
ifExtDot1DState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtDot1DState.setStatus(_C)
_IfExtMode_Type=ArubaPortMode
_IfExtMode_Object=MibTableColumn
ifExtMode=_IfExtMode_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,9),_IfExtMode_Type())
ifExtMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtMode.setStatus(_C)
_IfExtAccessVlanId_Type=ArubaVlanValidRange
_IfExtAccessVlanId_Object=MibTableColumn
ifExtAccessVlanId=_IfExtAccessVlanId_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,10),_IfExtAccessVlanId_Type())
ifExtAccessVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtAccessVlanId.setStatus(_C)
_IfExtTrunkNativeVlanId_Type=ArubaVlanValidRange
_IfExtTrunkNativeVlanId_Object=MibTableColumn
ifExtTrunkNativeVlanId=_IfExtTrunkNativeVlanId_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,11),_IfExtTrunkNativeVlanId_Type())
ifExtTrunkNativeVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtTrunkNativeVlanId.setStatus(_C)
_IfExtTrunkIsAllowedAll_Type=TruthValue
_IfExtTrunkIsAllowedAll_Object=MibTableColumn
ifExtTrunkIsAllowedAll=_IfExtTrunkIsAllowedAll_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,12),_IfExtTrunkIsAllowedAll_Type())
ifExtTrunkIsAllowedAll.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtTrunkIsAllowedAll.setStatus(_C)
class _IfExtTrunkAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_IfExtTrunkAllowedVlanList_Type.__name__=_J
_IfExtTrunkAllowedVlanList_Object=MibTableColumn
ifExtTrunkAllowedVlanList=_IfExtTrunkAllowedVlanList_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,13),_IfExtTrunkAllowedVlanList_Type())
ifExtTrunkAllowedVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtTrunkAllowedVlanList.setStatus(_C)
class _IfExtIngressACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtIngressACLName_Type.__name__=_F
_IfExtIngressACLName_Object=MibTableColumn
ifExtIngressACLName=_IfExtIngressACLName_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,14),_IfExtIngressACLName_Type())
ifExtIngressACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtIngressACLName.setStatus(_C)
class _IfExtEgressACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtEgressACLName_Type.__name__=_F
_IfExtEgressACLName_Object=MibTableColumn
ifExtEgressACLName=_IfExtEgressACLName_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,15),_IfExtEgressACLName_Type())
ifExtEgressACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtEgressACLName.setStatus(_C)
class _IfExtSessionACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtSessionACLName_Type.__name__=_F
_IfExtSessionACLName_Object=MibTableColumn
ifExtSessionACLName=_IfExtSessionACLName_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,16),_IfExtSessionACLName_Type())
ifExtSessionACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtSessionACLName.setStatus(_C)
_IfExtXsecVlan_Type=ArubaVlanValidRange
_IfExtXsecVlan_Object=MibTableColumn
ifExtXsecVlan=_IfExtXsecVlan_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,17),_IfExtXsecVlan_Type())
ifExtXsecVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtXsecVlan.setStatus(_C)
_IfExtIsMonitoring_Type=TruthValue
_IfExtIsMonitoring_Object=MibTableColumn
ifExtIsMonitoring=_IfExtIsMonitoring_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,18),_IfExtIsMonitoring_Type())
ifExtIsMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtIsMonitoring.setStatus(_C)
_IfExtIsMux_Type=TruthValue
_IfExtIsMux_Object=MibTableColumn
ifExtIsMux=_IfExtIsMux_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,19),_IfExtIsMux_Type())
ifExtIsMux.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtIsMux.setStatus(_C)
_IfExtUserSlotNumber_Type=Integer32
_IfExtUserSlotNumber_Object=MibTableColumn
ifExtUserSlotNumber=_IfExtUserSlotNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,20),_IfExtUserSlotNumber_Type())
ifExtUserSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtUserSlotNumber.setStatus(_C)
_IfExtUserPortNumber_Type=Integer32
_IfExtUserPortNumber_Object=MibTableColumn
ifExtUserPortNumber=_IfExtUserPortNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,21),_IfExtUserPortNumber_Type())
ifExtUserPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtUserPortNumber.setStatus(_C)
_IfExtPortSpeed_Type=ArubaPortSpeed
_IfExtPortSpeed_Object=MibTableColumn
ifExtPortSpeed=_IfExtPortSpeed_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,22),_IfExtPortSpeed_Type())
ifExtPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtPortSpeed.setStatus(_C)
_IfExtPortDuplex_Type=ArubaPortDuplex
_IfExtPortDuplex_Object=MibTableColumn
ifExtPortDuplex=_IfExtPortDuplex_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,23),_IfExtPortDuplex_Type())
ifExtPortDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtPortDuplex.setStatus(_C)
_IfExtPortType_Type=ArubaPortType
_IfExtPortType_Object=MibTableColumn
ifExtPortType=_IfExtPortType_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,24),_IfExtPortType_Type())
ifExtPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtPortType.setStatus(_C)
_IfExtDescr_Type=DisplayString
_IfExtDescr_Object=MibTableColumn
ifExtDescr=_IfExtDescr_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,25),_IfExtDescr_Type())
ifExtDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtDescr.setStatus(_C)
_IfExtUserModuleNumber_Type=Integer32
_IfExtUserModuleNumber_Object=MibTableColumn
ifExtUserModuleNumber=_IfExtUserModuleNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,1,1,26),_IfExtUserModuleNumber_Type())
ifExtUserModuleNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtUserModuleNumber.setStatus(_C)
_WlsxIfExtVlanTable_Object=MibTable
wlsxIfExtVlanTable=_WlsxIfExtVlanTable_Object((1,3,6,1,4,1,14823,2,2,1,3,1,2))
if mibBuilder.loadTexts:wlsxIfExtVlanTable.setStatus(_A)
_WlsxIfExtVlanEntry_Object=MibTableRow
wlsxIfExtVlanEntry=_WlsxIfExtVlanEntry_Object((1,3,6,1,4,1,14823,2,2,1,3,1,2,1))
wlsxIfExtVlanEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:wlsxIfExtVlanEntry.setStatus(_A)
_IfExtVlanId_Type=ArubaVlanValidRange
_IfExtVlanId_Object=MibTableColumn
ifExtVlanId=_IfExtVlanId_Object((1,3,6,1,4,1,14823,2,2,1,3,1,2,1,1),_IfExtVlanId_Type())
ifExtVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtVlanId.setStatus(_A)
class _IfExtVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtVlanName_Type.__name__=_F
_IfExtVlanName_Object=MibTableColumn
ifExtVlanName=_IfExtVlanName_Object((1,3,6,1,4,1,14823,2,2,1,3,1,2,1,2),_IfExtVlanName_Type())
ifExtVlanName.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanName.setStatus(_A)
_IfExtVlanStatus_Type=RowStatus
_IfExtVlanStatus_Object=MibTableColumn
ifExtVlanStatus=_IfExtVlanStatus_Object((1,3,6,1,4,1,14823,2,2,1,3,1,2,1,3),_IfExtVlanStatus_Type())
ifExtVlanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanStatus.setStatus(_A)
_WlsxIfExtVlanMemberTable_Object=MibTable
wlsxIfExtVlanMemberTable=_WlsxIfExtVlanMemberTable_Object((1,3,6,1,4,1,14823,2,2,1,3,1,3))
if mibBuilder.loadTexts:wlsxIfExtVlanMemberTable.setStatus(_A)
_WlsxIfExtVlanMemberEntry_Object=MibTableRow
wlsxIfExtVlanMemberEntry=_WlsxIfExtVlanMemberEntry_Object((1,3,6,1,4,1,14823,2,2,1,3,1,3,1))
wlsxIfExtVlanMemberEntry.setIndexNames((0,_G,_I),(0,_L,_M))
if mibBuilder.loadTexts:wlsxIfExtVlanMemberEntry.setStatus(_A)
_IfExtVlanMemberStatus_Type=RowStatus
_IfExtVlanMemberStatus_Object=MibTableColumn
ifExtVlanMemberStatus=_IfExtVlanMemberStatus_Object((1,3,6,1,4,1,14823,2,2,1,3,1,3,1,1),_IfExtVlanMemberStatus_Type())
ifExtVlanMemberStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanMemberStatus.setStatus(_A)
_IfExtVlanMemberSlot_Type=Integer32
_IfExtVlanMemberSlot_Object=MibTableColumn
ifExtVlanMemberSlot=_IfExtVlanMemberSlot_Object((1,3,6,1,4,1,14823,2,2,1,3,1,3,1,2),_IfExtVlanMemberSlot_Type())
ifExtVlanMemberSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtVlanMemberSlot.setStatus(_A)
_IfExtVlanMemberPort_Type=Integer32
_IfExtVlanMemberPort_Object=MibTableColumn
ifExtVlanMemberPort=_IfExtVlanMemberPort_Object((1,3,6,1,4,1,14823,2,2,1,3,1,3,1,3),_IfExtVlanMemberPort_Type())
ifExtVlanMemberPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtVlanMemberPort.setStatus(_A)
_IfExtVlanMemberType_Type=ArubaIfType
_IfExtVlanMemberType_Object=MibTableColumn
ifExtVlanMemberType=_IfExtVlanMemberType_Object((1,3,6,1,4,1,14823,2,2,1,3,1,3,1,4),_IfExtVlanMemberType_Type())
ifExtVlanMemberType.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtVlanMemberType.setStatus(_A)
_WlsxIfExtVlanInterfaceTable_Object=MibTable
wlsxIfExtVlanInterfaceTable=_WlsxIfExtVlanInterfaceTable_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4))
if mibBuilder.loadTexts:wlsxIfExtVlanInterfaceTable.setStatus(_A)
_WlsxIfExtVlanInterfaceEntry_Object=MibTableRow
wlsxIfExtVlanInterfaceEntry=_WlsxIfExtVlanInterfaceEntry_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1))
wlsxIfExtVlanInterfaceEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:wlsxIfExtVlanInterfaceEntry.setStatus(_A)
_IfExtVlanInterfaceIfIndex_Type=Integer32
_IfExtVlanInterfaceIfIndex_Object=MibTableColumn
ifExtVlanInterfaceIfIndex=_IfExtVlanInterfaceIfIndex_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,1),_IfExtVlanInterfaceIfIndex_Type())
ifExtVlanInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceIfIndex.setStatus(_A)
class _IfExtVlanInterfaceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtVlanInterfaceDescription_Type.__name__=_F
_IfExtVlanInterfaceDescription_Object=MibTableColumn
ifExtVlanInterfaceDescription=_IfExtVlanInterfaceDescription_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,2),_IfExtVlanInterfaceDescription_Type())
ifExtVlanInterfaceDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceDescription.setStatus(_A)
class _IfExtVlanInterfaceBWContract_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtVlanInterfaceBWContract_Type.__name__=_F
_IfExtVlanInterfaceBWContract_Object=MibTableColumn
ifExtVlanInterfaceBWContract=_IfExtVlanInterfaceBWContract_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,3),_IfExtVlanInterfaceBWContract_Type())
ifExtVlanInterfaceBWContract.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceBWContract.setStatus(_A)
_IfExtVlanInterfaceAdminState_Type=ArubaEnableValue
_IfExtVlanInterfaceAdminState_Object=MibTableColumn
ifExtVlanInterfaceAdminState=_IfExtVlanInterfaceAdminState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,4),_IfExtVlanInterfaceAdminState_Type())
ifExtVlanInterfaceAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceAdminState.setStatus(_A)
_IfExtVlanInterfaceOperState_Type=ArubaOperStateValue
_IfExtVlanInterfaceOperState_Object=MibTableColumn
ifExtVlanInterfaceOperState=_IfExtVlanInterfaceOperState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,5),_IfExtVlanInterfaceOperState_Type())
ifExtVlanInterfaceOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceOperState.setStatus(_A)
_IfExtVlanInterfaceIpAddress_Type=IpAddress
_IfExtVlanInterfaceIpAddress_Object=MibTableColumn
ifExtVlanInterfaceIpAddress=_IfExtVlanInterfaceIpAddress_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,6),_IfExtVlanInterfaceIpAddress_Type())
ifExtVlanInterfaceIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceIpAddress.setStatus(_A)
_IfExtVlanInterfaceIpMask_Type=IpAddress
_IfExtVlanInterfaceIpMask_Object=MibTableColumn
ifExtVlanInterfaceIpMask=_IfExtVlanInterfaceIpMask_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,7),_IfExtVlanInterfaceIpMask_Type())
ifExtVlanInterfaceIpMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceIpMask.setStatus(_A)
_IfExtVlanInterfaceIsLocalArp_Type=ArubaEnableValue
_IfExtVlanInterfaceIsLocalArp_Object=MibTableColumn
ifExtVlanInterfaceIsLocalArp=_IfExtVlanInterfaceIsLocalArp_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,8),_IfExtVlanInterfaceIsLocalArp_Type())
ifExtVlanInterfaceIsLocalArp.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceIsLocalArp.setStatus(_A)
_IfExtVlanInterfaceStatus_Type=RowStatus
_IfExtVlanInterfaceStatus_Object=MibTableColumn
ifExtVlanInterfaceStatus=_IfExtVlanInterfaceStatus_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,9),_IfExtVlanInterfaceStatus_Type())
ifExtVlanInterfaceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceStatus.setStatus(_A)
_IfExtVlanInterfaceIpRouting_Type=ArubaEnableValue
_IfExtVlanInterfaceIpRouting_Object=MibTableColumn
ifExtVlanInterfaceIpRouting=_IfExtVlanInterfaceIpRouting_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,10),_IfExtVlanInterfaceIpRouting_Type())
ifExtVlanInterfaceIpRouting.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceIpRouting.setStatus(_A)
_IfExtVlanInterfaceIpNatInside_Type=ArubaEnableValue
_IfExtVlanInterfaceIpNatInside_Object=MibTableColumn
ifExtVlanInterfaceIpNatInside=_IfExtVlanInterfaceIpNatInside_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,11),_IfExtVlanInterfaceIpNatInside_Type())
ifExtVlanInterfaceIpNatInside.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceIpNatInside.setStatus(_A)
_IfExtVlanInterfaceIpIgmpSnooping_Type=ArubaEnableValue
_IfExtVlanInterfaceIpIgmpSnooping_Object=MibTableColumn
ifExtVlanInterfaceIpIgmpSnooping=_IfExtVlanInterfaceIpIgmpSnooping_Object((1,3,6,1,4,1,14823,2,2,1,3,1,4,1,12),_IfExtVlanInterfaceIpIgmpSnooping_Type())
ifExtVlanInterfaceIpIgmpSnooping.setMaxAccess(_E)
if mibBuilder.loadTexts:ifExtVlanInterfaceIpIgmpSnooping.setStatus(_A)
_WlsxIfExtNPortTable_Object=MibTable
wlsxIfExtNPortTable=_WlsxIfExtNPortTable_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5))
if mibBuilder.loadTexts:wlsxIfExtNPortTable.setStatus(_A)
_WlsxIfExtNPortEntry_Object=MibTableRow
wlsxIfExtNPortEntry=_WlsxIfExtNPortEntry_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1))
wlsxIfExtNPortEntry.setIndexNames((0,_G,_Q),(0,_G,_R),(0,_G,_S))
if mibBuilder.loadTexts:wlsxIfExtNPortEntry.setStatus(_A)
_IfExtNSlotNumber_Type=Integer32
_IfExtNSlotNumber_Object=MibTableColumn
ifExtNSlotNumber=_IfExtNSlotNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,1),_IfExtNSlotNumber_Type())
ifExtNSlotNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtNSlotNumber.setStatus(_A)
_IfExtNModuleNumber_Type=Integer32
_IfExtNModuleNumber_Object=MibTableColumn
ifExtNModuleNumber=_IfExtNModuleNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,2),_IfExtNModuleNumber_Type())
ifExtNModuleNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtNModuleNumber.setStatus(_A)
_IfExtNPortNumber_Type=Integer32
_IfExtNPortNumber_Object=MibTableColumn
ifExtNPortNumber=_IfExtNPortNumber_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,3),_IfExtNPortNumber_Type())
ifExtNPortNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:ifExtNPortNumber.setStatus(_A)
_IfExtNPortIfIndex_Type=Integer32
_IfExtNPortIfIndex_Object=MibTableColumn
ifExtNPortIfIndex=_IfExtNPortIfIndex_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,4),_IfExtNPortIfIndex_Type())
ifExtNPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtNPortIfIndex.setStatus(_A)
_IfExtNAdminState_Type=ArubaEnableValue
_IfExtNAdminState_Object=MibTableColumn
ifExtNAdminState=_IfExtNAdminState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,5),_IfExtNAdminState_Type())
ifExtNAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNAdminState.setStatus(_A)
class _IfExtNOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_P,3)))
_IfExtNOperState_Type.__name__=_K
_IfExtNOperState_Object=MibTableColumn
ifExtNOperState=_IfExtNOperState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,6),_IfExtNOperState_Type())
ifExtNOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtNOperState.setStatus(_A)
_IfExtNPoeState_Type=ArubaPoeState
_IfExtNPoeState_Object=MibTableColumn
ifExtNPoeState=_IfExtNPoeState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,7),_IfExtNPoeState_Type())
ifExtNPoeState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNPoeState.setStatus(_A)
_IfExtNIsTrusted_Type=TruthValue
_IfExtNIsTrusted_Object=MibTableColumn
ifExtNIsTrusted=_IfExtNIsTrusted_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,8),_IfExtNIsTrusted_Type())
ifExtNIsTrusted.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNIsTrusted.setStatus(_A)
_IfExtNDot1DState_Type=ArubaDot1dState
_IfExtNDot1DState_Object=MibTableColumn
ifExtNDot1DState=_IfExtNDot1DState_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,9),_IfExtNDot1DState_Type())
ifExtNDot1DState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNDot1DState.setStatus(_A)
_IfExtNMode_Type=ArubaPortMode
_IfExtNMode_Object=MibTableColumn
ifExtNMode=_IfExtNMode_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,10),_IfExtNMode_Type())
ifExtNMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNMode.setStatus(_A)
_IfExtNAccessVlanId_Type=ArubaVlanValidRange
_IfExtNAccessVlanId_Object=MibTableColumn
ifExtNAccessVlanId=_IfExtNAccessVlanId_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,11),_IfExtNAccessVlanId_Type())
ifExtNAccessVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNAccessVlanId.setStatus(_A)
_IfExtNTrunkNativeVlanId_Type=ArubaVlanValidRange
_IfExtNTrunkNativeVlanId_Object=MibTableColumn
ifExtNTrunkNativeVlanId=_IfExtNTrunkNativeVlanId_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,12),_IfExtNTrunkNativeVlanId_Type())
ifExtNTrunkNativeVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNTrunkNativeVlanId.setStatus(_A)
_IfExtNTrunkIsAllowedAll_Type=TruthValue
_IfExtNTrunkIsAllowedAll_Object=MibTableColumn
ifExtNTrunkIsAllowedAll=_IfExtNTrunkIsAllowedAll_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,13),_IfExtNTrunkIsAllowedAll_Type())
ifExtNTrunkIsAllowedAll.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNTrunkIsAllowedAll.setStatus(_A)
class _IfExtNTrunkAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_IfExtNTrunkAllowedVlanList_Type.__name__=_J
_IfExtNTrunkAllowedVlanList_Object=MibTableColumn
ifExtNTrunkAllowedVlanList=_IfExtNTrunkAllowedVlanList_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,14),_IfExtNTrunkAllowedVlanList_Type())
ifExtNTrunkAllowedVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNTrunkAllowedVlanList.setStatus(_A)
class _IfExtNIngressACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtNIngressACLName_Type.__name__=_F
_IfExtNIngressACLName_Object=MibTableColumn
ifExtNIngressACLName=_IfExtNIngressACLName_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,15),_IfExtNIngressACLName_Type())
ifExtNIngressACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNIngressACLName.setStatus(_A)
class _IfExtNEgressACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtNEgressACLName_Type.__name__=_F
_IfExtNEgressACLName_Object=MibTableColumn
ifExtNEgressACLName=_IfExtNEgressACLName_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,16),_IfExtNEgressACLName_Type())
ifExtNEgressACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNEgressACLName.setStatus(_A)
class _IfExtNSessionACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IfExtNSessionACLName_Type.__name__=_F
_IfExtNSessionACLName_Object=MibTableColumn
ifExtNSessionACLName=_IfExtNSessionACLName_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,17),_IfExtNSessionACLName_Type())
ifExtNSessionACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNSessionACLName.setStatus(_A)
_IfExtNXsecVlan_Type=ArubaVlanValidRange
_IfExtNXsecVlan_Object=MibTableColumn
ifExtNXsecVlan=_IfExtNXsecVlan_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,18),_IfExtNXsecVlan_Type())
ifExtNXsecVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNXsecVlan.setStatus(_A)
_IfExtNIsMonitoring_Type=TruthValue
_IfExtNIsMonitoring_Object=MibTableColumn
ifExtNIsMonitoring=_IfExtNIsMonitoring_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,19),_IfExtNIsMonitoring_Type())
ifExtNIsMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNIsMonitoring.setStatus(_A)
_IfExtNIsMux_Type=TruthValue
_IfExtNIsMux_Object=MibTableColumn
ifExtNIsMux=_IfExtNIsMux_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,20),_IfExtNIsMux_Type())
ifExtNIsMux.setMaxAccess(_B)
if mibBuilder.loadTexts:ifExtNIsMux.setStatus(_A)
_IfExtNPortSpeed_Type=ArubaPortSpeed
_IfExtNPortSpeed_Object=MibTableColumn
ifExtNPortSpeed=_IfExtNPortSpeed_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,21),_IfExtNPortSpeed_Type())
ifExtNPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtNPortSpeed.setStatus(_A)
_IfExtNPortDuplex_Type=ArubaPortDuplex
_IfExtNPortDuplex_Object=MibTableColumn
ifExtNPortDuplex=_IfExtNPortDuplex_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,22),_IfExtNPortDuplex_Type())
ifExtNPortDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtNPortDuplex.setStatus(_A)
_IfExtNPortType_Type=ArubaPortType
_IfExtNPortType_Object=MibTableColumn
ifExtNPortType=_IfExtNPortType_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,23),_IfExtNPortType_Type())
ifExtNPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtNPortType.setStatus(_A)
_IfExtNDescr_Type=DisplayString
_IfExtNDescr_Object=MibTableColumn
ifExtNDescr=_IfExtNDescr_Object((1,3,6,1,4,1,14823,2,2,1,3,1,5,1,24),_IfExtNDescr_Type())
ifExtNDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:ifExtNDescr.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'wlsxIfExtMIB':wlsxIfExtMIB,'wlsxIfExtGroup':wlsxIfExtGroup,'wlsxIfExtPortTable':wlsxIfExtPortTable,'wlsxIfExtPortEntry':wlsxIfExtPortEntry,_N:ifExtSlotNumber,_O:ifExtPortNumber,'ifExtPortIfIndex':ifExtPortIfIndex,'ifExtAdminState':ifExtAdminState,'ifExtOperState':ifExtOperState,'ifExtPoeState':ifExtPoeState,'ifExtIsTrusted':ifExtIsTrusted,'ifExtDot1DState':ifExtDot1DState,'ifExtMode':ifExtMode,'ifExtAccessVlanId':ifExtAccessVlanId,'ifExtTrunkNativeVlanId':ifExtTrunkNativeVlanId,'ifExtTrunkIsAllowedAll':ifExtTrunkIsAllowedAll,'ifExtTrunkAllowedVlanList':ifExtTrunkAllowedVlanList,'ifExtIngressACLName':ifExtIngressACLName,'ifExtEgressACLName':ifExtEgressACLName,'ifExtSessionACLName':ifExtSessionACLName,'ifExtXsecVlan':ifExtXsecVlan,'ifExtIsMonitoring':ifExtIsMonitoring,'ifExtIsMux':ifExtIsMux,'ifExtUserSlotNumber':ifExtUserSlotNumber,'ifExtUserPortNumber':ifExtUserPortNumber,'ifExtPortSpeed':ifExtPortSpeed,'ifExtPortDuplex':ifExtPortDuplex,'ifExtPortType':ifExtPortType,'ifExtDescr':ifExtDescr,'ifExtUserModuleNumber':ifExtUserModuleNumber,'wlsxIfExtVlanTable':wlsxIfExtVlanTable,'wlsxIfExtVlanEntry':wlsxIfExtVlanEntry,_I:ifExtVlanId,'ifExtVlanName':ifExtVlanName,'ifExtVlanStatus':ifExtVlanStatus,'wlsxIfExtVlanMemberTable':wlsxIfExtVlanMemberTable,'wlsxIfExtVlanMemberEntry':wlsxIfExtVlanMemberEntry,'ifExtVlanMemberStatus':ifExtVlanMemberStatus,'ifExtVlanMemberSlot':ifExtVlanMemberSlot,'ifExtVlanMemberPort':ifExtVlanMemberPort,'ifExtVlanMemberType':ifExtVlanMemberType,'wlsxIfExtVlanInterfaceTable':wlsxIfExtVlanInterfaceTable,'wlsxIfExtVlanInterfaceEntry':wlsxIfExtVlanInterfaceEntry,'ifExtVlanInterfaceIfIndex':ifExtVlanInterfaceIfIndex,'ifExtVlanInterfaceDescription':ifExtVlanInterfaceDescription,'ifExtVlanInterfaceBWContract':ifExtVlanInterfaceBWContract,'ifExtVlanInterfaceAdminState':ifExtVlanInterfaceAdminState,'ifExtVlanInterfaceOperState':ifExtVlanInterfaceOperState,'ifExtVlanInterfaceIpAddress':ifExtVlanInterfaceIpAddress,'ifExtVlanInterfaceIpMask':ifExtVlanInterfaceIpMask,'ifExtVlanInterfaceIsLocalArp':ifExtVlanInterfaceIsLocalArp,'ifExtVlanInterfaceStatus':ifExtVlanInterfaceStatus,'ifExtVlanInterfaceIpRouting':ifExtVlanInterfaceIpRouting,'ifExtVlanInterfaceIpNatInside':ifExtVlanInterfaceIpNatInside,'ifExtVlanInterfaceIpIgmpSnooping':ifExtVlanInterfaceIpIgmpSnooping,'wlsxIfExtNPortTable':wlsxIfExtNPortTable,'wlsxIfExtNPortEntry':wlsxIfExtNPortEntry,_Q:ifExtNSlotNumber,_R:ifExtNModuleNumber,_S:ifExtNPortNumber,'ifExtNPortIfIndex':ifExtNPortIfIndex,'ifExtNAdminState':ifExtNAdminState,'ifExtNOperState':ifExtNOperState,'ifExtNPoeState':ifExtNPoeState,'ifExtNIsTrusted':ifExtNIsTrusted,'ifExtNDot1DState':ifExtNDot1DState,'ifExtNMode':ifExtNMode,'ifExtNAccessVlanId':ifExtNAccessVlanId,'ifExtNTrunkNativeVlanId':ifExtNTrunkNativeVlanId,'ifExtNTrunkIsAllowedAll':ifExtNTrunkIsAllowedAll,'ifExtNTrunkAllowedVlanList':ifExtNTrunkAllowedVlanList,'ifExtNIngressACLName':ifExtNIngressACLName,'ifExtNEgressACLName':ifExtNEgressACLName,'ifExtNSessionACLName':ifExtNSessionACLName,'ifExtNXsecVlan':ifExtNXsecVlan,'ifExtNIsMonitoring':ifExtNIsMonitoring,'ifExtNIsMux':ifExtNIsMux,'ifExtNPortSpeed':ifExtNPortSpeed,'ifExtNPortDuplex':ifExtNPortDuplex,'ifExtNPortType':ifExtNPortType,'ifExtNDescr':ifExtNDescr})