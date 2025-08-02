_n='cnAutoAttachRemoteElemMgmtOid'
_m='cnAutoAttachRemoteElemSysDescr'
_l='accessible-for-notify'
_k='cnAutoAttachMacListFileName'
_j='cambium'
_i='cnAutoAttachNbrClassIdentifier'
_h='cnAutoAttachNbrClassType'
_g='cnAutoAttachCondensedNbrIfIndex'
_f='cnAutoAttachScriptName'
_e='cnAutoAttachPolicyName'
_d='hybrid'
_c='access'
_b='cnAutoAttachActionName'
_a='macFullAddress'
_Z='lldpPortDescription'
_Y='lldpPortId'
_X='lldpChassisId'
_W='lldpCapabilities'
_V='lldpAny'
_U='cnAutoAttachRuleName'
_T='cnAutoAttachPortIfIndex'
_S='cnAutoAttachPortActivePolicyName'
_R='macOui'
_Q='lldpSystemDescription'
_P='lldpSystemName'
_O='TruthValue'
_N='ifIndex'
_M='IF-MIB'
_L='OctetString'
_K='not-accessible'
_J='none'
_I='CAMBIUM-NETWORKS-AUTO-ATTACH-MIB'
_H='enabled'
_G='disabled'
_F='read-write'
_E='read-only'
_D='SnmpAdminString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_M,_N)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention',_O)
cnAutoAttachMib=ModuleIdentity((1,3,6,1,4,1,17713,24,1))
if mibBuilder.loadTexts:cnAutoAttachMib.setRevisions(('2022-09-21 00:00','2021-12-10 00:00','2021-09-29 00:00','2021-02-11 00:00','2021-01-19 00:00','2020-10-12 00:00','2020-06-05 00:00','2019-10-10 00:00','2019-09-10 00:00','2019-06-26 00:00','2019-01-23 00:00','2018-10-23 00:00'))
_Cambium_ObjectIdentity=ObjectIdentity
cambium=_Cambium_ObjectIdentity((1,3,6,1,4,1,17713))
_CnMatrix_ObjectIdentity=ObjectIdentity
cnMatrix=_CnMatrix_ObjectIdentity((1,3,6,1,4,1,17713,24))
_CnAutoAttachNotifications_ObjectIdentity=ObjectIdentity
cnAutoAttachNotifications=_CnAutoAttachNotifications_ObjectIdentity((1,3,6,1,4,1,17713,24,1,0))
_CnAutoAttachObjects_ObjectIdentity=ObjectIdentity
cnAutoAttachObjects=_CnAutoAttachObjects_ObjectIdentity((1,3,6,1,4,1,17713,24,1,1))
class _CnAutoAttachService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachService_Type.__name__=_C
_CnAutoAttachService_Object=MibScalar
cnAutoAttachService=_CnAutoAttachService_Object((1,3,6,1,4,1,17713,24,1,1,1),_CnAutoAttachService_Type())
cnAutoAttachService.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachService.setStatus(_A)
class _CnAutoAttachDataDiffAllowed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CnAutoAttachDataDiffAllowed_Type.__name__=_C
_CnAutoAttachDataDiffAllowed_Object=MibScalar
cnAutoAttachDataDiffAllowed=_CnAutoAttachDataDiffAllowed_Object((1,3,6,1,4,1,17713,24,1,1,2),_CnAutoAttachDataDiffAllowed_Type())
cnAutoAttachDataDiffAllowed.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachDataDiffAllowed.setStatus(_A)
class _CnAutoAttachDeviceDataCompare_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('caseSensitive',1),('caseInsensitive',2)))
_CnAutoAttachDeviceDataCompare_Type.__name__=_C
_CnAutoAttachDeviceDataCompare_Object=MibScalar
cnAutoAttachDeviceDataCompare=_CnAutoAttachDeviceDataCompare_Object((1,3,6,1,4,1,17713,24,1,1,3),_CnAutoAttachDeviceDataCompare_Type())
cnAutoAttachDeviceDataCompare.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachDeviceDataCompare.setStatus(_A)
class _CnAutoAttachClearPolicyStats_Type(TruthValue):defaultValue=2
_CnAutoAttachClearPolicyStats_Type.__name__=_O
_CnAutoAttachClearPolicyStats_Object=MibScalar
cnAutoAttachClearPolicyStats=_CnAutoAttachClearPolicyStats_Object((1,3,6,1,4,1,17713,24,1,1,4),_CnAutoAttachClearPolicyStats_Type())
cnAutoAttachClearPolicyStats.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachClearPolicyStats.setStatus(_A)
class _CnAutoAttachClearInterfaceStats_Type(TruthValue):defaultValue=2
_CnAutoAttachClearInterfaceStats_Type.__name__=_O
_CnAutoAttachClearInterfaceStats_Object=MibScalar
cnAutoAttachClearInterfaceStats=_CnAutoAttachClearInterfaceStats_Object((1,3,6,1,4,1,17713,24,1,1,5),_CnAutoAttachClearInterfaceStats_Type())
cnAutoAttachClearInterfaceStats.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachClearInterfaceStats.setStatus(_A)
class _CnAutoAttachUpdatePortDesc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('pbaPolicyName',2),(_P,3),(_Q,4)))
_CnAutoAttachUpdatePortDesc_Type.__name__=_C
_CnAutoAttachUpdatePortDesc_Object=MibScalar
cnAutoAttachUpdatePortDesc=_CnAutoAttachUpdatePortDesc_Object((1,3,6,1,4,1,17713,24,1,1,6),_CnAutoAttachUpdatePortDesc_Type())
cnAutoAttachUpdatePortDesc.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachUpdatePortDesc.setStatus(_A)
class _CnAutoAttachRestrictedMacMatch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachRestrictedMacMatch_Type.__name__=_C
_CnAutoAttachRestrictedMacMatch_Object=MibScalar
cnAutoAttachRestrictedMacMatch=_CnAutoAttachRestrictedMacMatch_Object((1,3,6,1,4,1,17713,24,1,1,7),_CnAutoAttachRestrictedMacMatch_Type())
cnAutoAttachRestrictedMacMatch.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachRestrictedMacMatch.setStatus(_A)
class _CnAutoAttachActivePolicyReorder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachActivePolicyReorder_Type.__name__=_C
_CnAutoAttachActivePolicyReorder_Object=MibScalar
cnAutoAttachActivePolicyReorder=_CnAutoAttachActivePolicyReorder_Object((1,3,6,1,4,1,17713,24,1,1,8),_CnAutoAttachActivePolicyReorder_Type())
cnAutoAttachActivePolicyReorder.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachActivePolicyReorder.setStatus(_A)
class _CnAutoAttachMacPolicyAging_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachMacPolicyAging_Type.__name__=_C
_CnAutoAttachMacPolicyAging_Object=MibScalar
cnAutoAttachMacPolicyAging=_CnAutoAttachMacPolicyAging_Object((1,3,6,1,4,1,17713,24,1,1,9),_CnAutoAttachMacPolicyAging_Type())
cnAutoAttachMacPolicyAging.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachMacPolicyAging.setStatus(_A)
_CnAutoAttachPortTable_Object=MibTable
cnAutoAttachPortTable=_CnAutoAttachPortTable_Object((1,3,6,1,4,1,17713,24,1,1,10))
if mibBuilder.loadTexts:cnAutoAttachPortTable.setStatus(_A)
_CnAutoAttachPortEntry_Object=MibTableRow
cnAutoAttachPortEntry=_CnAutoAttachPortEntry_Object((1,3,6,1,4,1,17713,24,1,1,10,1))
cnAutoAttachPortEntry.setIndexNames((0,_I,_T))
if mibBuilder.loadTexts:cnAutoAttachPortEntry.setStatus(_A)
class _CnAutoAttachPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CnAutoAttachPortIfIndex_Type.__name__=_C
_CnAutoAttachPortIfIndex_Object=MibTableColumn
cnAutoAttachPortIfIndex=_CnAutoAttachPortIfIndex_Object((1,3,6,1,4,1,17713,24,1,1,10,1,1),_CnAutoAttachPortIfIndex_Type())
cnAutoAttachPortIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachPortIfIndex.setStatus(_A)
class _CnAutoAttachPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachPortState_Type.__name__=_C
_CnAutoAttachPortState_Object=MibTableColumn
cnAutoAttachPortState=_CnAutoAttachPortState_Object((1,3,6,1,4,1,17713,24,1,1,10,1,2),_CnAutoAttachPortState_Type())
cnAutoAttachPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPortState.setStatus(_A)
class _CnAutoAttachPortMsgAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachPortMsgAuthStatus_Type.__name__=_C
_CnAutoAttachPortMsgAuthStatus_Object=MibTableColumn
cnAutoAttachPortMsgAuthStatus=_CnAutoAttachPortMsgAuthStatus_Object((1,3,6,1,4,1,17713,24,1,1,10,1,3),_CnAutoAttachPortMsgAuthStatus_Type())
cnAutoAttachPortMsgAuthStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPortMsgAuthStatus.setStatus(_A)
class _CnAutoAttachPortMsgAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnAutoAttachPortMsgAuthKey_Type.__name__=_L
_CnAutoAttachPortMsgAuthKey_Object=MibTableColumn
cnAutoAttachPortMsgAuthKey=_CnAutoAttachPortMsgAuthKey_Object((1,3,6,1,4,1,17713,24,1,1,10,1,4),_CnAutoAttachPortMsgAuthKey_Type())
cnAutoAttachPortMsgAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPortMsgAuthKey.setStatus(_A)
class _CnAutoAttachPortActivePolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CnAutoAttachPortActivePolicyName_Type.__name__=_D
_CnAutoAttachPortActivePolicyName_Object=MibTableColumn
cnAutoAttachPortActivePolicyName=_CnAutoAttachPortActivePolicyName_Object((1,3,6,1,4,1,17713,24,1,1,10,1,5),_CnAutoAttachPortActivePolicyName_Type())
cnAutoAttachPortActivePolicyName.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortActivePolicyName.setStatus(_A)
_CnAutoAttachPortPolicyApplied_Type=Counter32
_CnAutoAttachPortPolicyApplied_Object=MibTableColumn
cnAutoAttachPortPolicyApplied=_CnAutoAttachPortPolicyApplied_Object((1,3,6,1,4,1,17713,24,1,1,10,1,6),_CnAutoAttachPortPolicyApplied_Type())
cnAutoAttachPortPolicyApplied.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortPolicyApplied.setStatus(_A)
_CnAutoAttachPortPolicyExpired_Type=Counter32
_CnAutoAttachPortPolicyExpired_Object=MibTableColumn
cnAutoAttachPortPolicyExpired=_CnAutoAttachPortPolicyExpired_Object((1,3,6,1,4,1,17713,24,1,1,10,1,7),_CnAutoAttachPortPolicyExpired_Type())
cnAutoAttachPortPolicyExpired.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortPolicyExpired.setStatus(_A)
_CnAutoAttachPortPolicyErrors_Type=Counter32
_CnAutoAttachPortPolicyErrors_Object=MibTableColumn
cnAutoAttachPortPolicyErrors=_CnAutoAttachPortPolicyErrors_Object((1,3,6,1,4,1,17713,24,1,1,10,1,8),_CnAutoAttachPortPolicyErrors_Type())
cnAutoAttachPortPolicyErrors.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortPolicyErrors.setStatus(_A)
_CnAutoAttachPortRowStatus_Type=RowStatus
_CnAutoAttachPortRowStatus_Object=MibTableColumn
cnAutoAttachPortRowStatus=_CnAutoAttachPortRowStatus_Object((1,3,6,1,4,1,17713,24,1,1,10,1,9),_CnAutoAttachPortRowStatus_Type())
cnAutoAttachPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPortRowStatus.setStatus(_A)
class _CnAutoAttachPortTlvTxEnable_Type(Bits):namedValues=NamedValues(*(('pbaAuthenticationTlv',0),('pbaDeviceSettingsTlv',1)))
_CnAutoAttachPortTlvTxEnable_Type.__name__='Bits'
_CnAutoAttachPortTlvTxEnable_Object=MibTableColumn
cnAutoAttachPortTlvTxEnable=_CnAutoAttachPortTlvTxEnable_Object((1,3,6,1,4,1,17713,24,1,1,10,1,10),_CnAutoAttachPortTlvTxEnable_Type())
cnAutoAttachPortTlvTxEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPortTlvTxEnable.setStatus(_A)
_CnAutoAttachPortDevSettingsTlvReceived_Type=Counter32
_CnAutoAttachPortDevSettingsTlvReceived_Object=MibTableColumn
cnAutoAttachPortDevSettingsTlvReceived=_CnAutoAttachPortDevSettingsTlvReceived_Object((1,3,6,1,4,1,17713,24,1,1,10,1,11),_CnAutoAttachPortDevSettingsTlvReceived_Type())
cnAutoAttachPortDevSettingsTlvReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortDevSettingsTlvReceived.setStatus(_A)
_CnAutoAttachPortDevSettingsTlvProcessed_Type=Counter32
_CnAutoAttachPortDevSettingsTlvProcessed_Object=MibTableColumn
cnAutoAttachPortDevSettingsTlvProcessed=_CnAutoAttachPortDevSettingsTlvProcessed_Object((1,3,6,1,4,1,17713,24,1,1,10,1,12),_CnAutoAttachPortDevSettingsTlvProcessed_Type())
cnAutoAttachPortDevSettingsTlvProcessed.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortDevSettingsTlvProcessed.setStatus(_A)
_CnAutoAttachPortDevSettingsTlvAuthFails_Type=Counter32
_CnAutoAttachPortDevSettingsTlvAuthFails_Object=MibTableColumn
cnAutoAttachPortDevSettingsTlvAuthFails=_CnAutoAttachPortDevSettingsTlvAuthFails_Object((1,3,6,1,4,1,17713,24,1,1,10,1,13),_CnAutoAttachPortDevSettingsTlvAuthFails_Type())
cnAutoAttachPortDevSettingsTlvAuthFails.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortDevSettingsTlvAuthFails.setStatus(_A)
class _CnAutoAttachPortPrevPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CnAutoAttachPortPrevPolicyName_Type.__name__=_D
_CnAutoAttachPortPrevPolicyName_Object=MibTableColumn
cnAutoAttachPortPrevPolicyName=_CnAutoAttachPortPrevPolicyName_Object((1,3,6,1,4,1,17713,24,1,1,10,1,14),_CnAutoAttachPortPrevPolicyName_Type())
cnAutoAttachPortPrevPolicyName.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPortPrevPolicyName.setStatus(_A)
_CnAutoAttachRuleTable_Object=MibTable
cnAutoAttachRuleTable=_CnAutoAttachRuleTable_Object((1,3,6,1,4,1,17713,24,1,1,11))
if mibBuilder.loadTexts:cnAutoAttachRuleTable.setStatus(_A)
_CnAutoAttachRuleEntry_Object=MibTableRow
cnAutoAttachRuleEntry=_CnAutoAttachRuleEntry_Object((1,3,6,1,4,1,17713,24,1,1,11,1))
cnAutoAttachRuleEntry.setIndexNames((0,_I,_U))
if mibBuilder.loadTexts:cnAutoAttachRuleEntry.setStatus(_A)
class _CnAutoAttachRuleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnAutoAttachRuleName_Type.__name__=_D
_CnAutoAttachRuleName_Object=MibTableColumn
cnAutoAttachRuleName=_CnAutoAttachRuleName_Object((1,3,6,1,4,1,17713,24,1,1,11,1,1),_CnAutoAttachRuleName_Type())
cnAutoAttachRuleName.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachRuleName.setStatus(_A)
class _CnAutoAttachRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_J,1),(_V,2),(_W,3),(_P,4),(_Q,5),(_X,6),(_Y,7),(_Z,8),(_R,9),(_a,10),('macAddressRange',11),('lldpIpv4MgmtAddress',12),('autoVlan',13),('defaultAnyMac',14),('ifc8021x',15),('autoVoip',16),('macList',17)))
_CnAutoAttachRuleType_Type.__name__=_C
_CnAutoAttachRuleType_Object=MibTableColumn
cnAutoAttachRuleType=_CnAutoAttachRuleType_Object((1,3,6,1,4,1,17713,24,1,1,11,1,2),_CnAutoAttachRuleType_Type())
cnAutoAttachRuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachRuleType.setStatus(_A)
class _CnAutoAttachRuleDeviceData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_CnAutoAttachRuleDeviceData_Type.__name__=_D
_CnAutoAttachRuleDeviceData_Object=MibTableColumn
cnAutoAttachRuleDeviceData=_CnAutoAttachRuleDeviceData_Object((1,3,6,1,4,1,17713,24,1,1,11,1,3),_CnAutoAttachRuleDeviceData_Type())
cnAutoAttachRuleDeviceData.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachRuleDeviceData.setStatus(_A)
_CnAutoAttachRuleRowStatus_Type=RowStatus
_CnAutoAttachRuleRowStatus_Object=MibTableColumn
cnAutoAttachRuleRowStatus=_CnAutoAttachRuleRowStatus_Object((1,3,6,1,4,1,17713,24,1,1,11,1,4),_CnAutoAttachRuleRowStatus_Type())
cnAutoAttachRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachRuleRowStatus.setStatus(_A)
class _CnAutoAttachRuleListName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnAutoAttachRuleListName_Type.__name__=_D
_CnAutoAttachRuleListName_Object=MibTableColumn
cnAutoAttachRuleListName=_CnAutoAttachRuleListName_Object((1,3,6,1,4,1,17713,24,1,1,11,1,5),_CnAutoAttachRuleListName_Type())
cnAutoAttachRuleListName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachRuleListName.setStatus(_A)
class _CnAutoAttachRuleDataFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CnAutoAttachRuleDataFileName_Type.__name__=_D
_CnAutoAttachRuleDataFileName_Object=MibTableColumn
cnAutoAttachRuleDataFileName=_CnAutoAttachRuleDataFileName_Object((1,3,6,1,4,1,17713,24,1,1,11,1,6),_CnAutoAttachRuleDataFileName_Type())
cnAutoAttachRuleDataFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachRuleDataFileName.setStatus(_A)
_CnAutoAttachActionTable_Object=MibTable
cnAutoAttachActionTable=_CnAutoAttachActionTable_Object((1,3,6,1,4,1,17713,24,1,1,12))
if mibBuilder.loadTexts:cnAutoAttachActionTable.setStatus(_A)
_CnAutoAttachActionEntry_Object=MibTableRow
cnAutoAttachActionEntry=_CnAutoAttachActionEntry_Object((1,3,6,1,4,1,17713,24,1,1,12,1))
cnAutoAttachActionEntry.setIndexNames((0,_I,_b))
if mibBuilder.loadTexts:cnAutoAttachActionEntry.setStatus(_A)
class _CnAutoAttachActionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65))
_CnAutoAttachActionName_Type.__name__=_D
_CnAutoAttachActionName_Object=MibTableColumn
cnAutoAttachActionName=_CnAutoAttachActionName_Object((1,3,6,1,4,1,17713,24,1,1,12,1,1),_CnAutoAttachActionName_Type())
cnAutoAttachActionName.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachActionName.setStatus(_A)
class _CnAutoAttachActionVlanData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CnAutoAttachActionVlanData_Type.__name__=_D
_CnAutoAttachActionVlanData_Object=MibTableColumn
cnAutoAttachActionVlanData=_CnAutoAttachActionVlanData_Object((1,3,6,1,4,1,17713,24,1,1,12,1,2),_CnAutoAttachActionVlanData_Type())
cnAutoAttachActionVlanData.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionVlanData.setStatus(_A)
class _CnAutoAttachActionPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CnAutoAttachActionPvid_Type.__name__=_C
_CnAutoAttachActionPvid_Object=MibTableColumn
cnAutoAttachActionPvid=_CnAutoAttachActionPvid_Object((1,3,6,1,4,1,17713,24,1,1,12,1,3),_CnAutoAttachActionPvid_Type())
cnAutoAttachActionPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionPvid.setStatus(_A)
class _CnAutoAttachActionPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_c,2),('trunk',3),(_d,4)))
_CnAutoAttachActionPortMode_Type.__name__=_C
_CnAutoAttachActionPortMode_Object=MibTableColumn
cnAutoAttachActionPortMode=_CnAutoAttachActionPortMode_Object((1,3,6,1,4,1,17713,24,1,1,12,1,4),_CnAutoAttachActionPortMode_Type())
cnAutoAttachActionPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionPortMode.setStatus(_A)
_CnAutoAttachActionRowStatus_Type=RowStatus
_CnAutoAttachActionRowStatus_Object=MibTableColumn
cnAutoAttachActionRowStatus=_CnAutoAttachActionRowStatus_Object((1,3,6,1,4,1,17713,24,1,1,12,1,5),_CnAutoAttachActionRowStatus_Type())
cnAutoAttachActionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionRowStatus.setStatus(_A)
class _CnAutoAttachActionUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CnAutoAttachActionUserPriority_Type.__name__=_C
_CnAutoAttachActionUserPriority_Object=MibTableColumn
cnAutoAttachActionUserPriority=_CnAutoAttachActionUserPriority_Object((1,3,6,1,4,1,17713,24,1,1,12,1,6),_CnAutoAttachActionUserPriority_Type())
cnAutoAttachActionUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionUserPriority.setStatus(_A)
class _CnAutoAttachActionQosTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('untrusted',2),('dot1p',3),('dscp',4)))
_CnAutoAttachActionQosTrust_Type.__name__=_C
_CnAutoAttachActionQosTrust_Object=MibTableColumn
cnAutoAttachActionQosTrust=_CnAutoAttachActionQosTrust_Object((1,3,6,1,4,1,17713,24,1,1,12,1,7),_CnAutoAttachActionQosTrust_Type())
cnAutoAttachActionQosTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionQosTrust.setStatus(_A)
class _CnAutoAttachActionUplinkData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CnAutoAttachActionUplinkData_Type.__name__=_D
_CnAutoAttachActionUplinkData_Object=MibTableColumn
cnAutoAttachActionUplinkData=_CnAutoAttachActionUplinkData_Object((1,3,6,1,4,1,17713,24,1,1,12,1,8),_CnAutoAttachActionUplinkData_Type())
cnAutoAttachActionUplinkData.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionUplinkData.setStatus(_A)
class _CnAutoAttachActionPoePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('critical',2),('high',3),('low',4)))
_CnAutoAttachActionPoePriority_Type.__name__=_C
_CnAutoAttachActionPoePriority_Object=MibTableColumn
cnAutoAttachActionPoePriority=_CnAutoAttachActionPoePriority_Object((1,3,6,1,4,1,17713,24,1,1,12,1,9),_CnAutoAttachActionPoePriority_Type())
cnAutoAttachActionPoePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionPoePriority.setStatus(_A)
class _CnAutoAttachActionPvidUpdateReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachActionPvidUpdateReset_Type.__name__=_C
_CnAutoAttachActionPvidUpdateReset_Object=MibTableColumn
cnAutoAttachActionPvidUpdateReset=_CnAutoAttachActionPvidUpdateReset_Object((1,3,6,1,4,1,17713,24,1,1,12,1,10),_CnAutoAttachActionPvidUpdateReset_Type())
cnAutoAttachActionPvidUpdateReset.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionPvidUpdateReset.setStatus(_A)
class _CnAutoAttachActionProtectedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_G,3)))
_CnAutoAttachActionProtectedPort_Type.__name__=_C
_CnAutoAttachActionProtectedPort_Object=MibTableColumn
cnAutoAttachActionProtectedPort=_CnAutoAttachActionProtectedPort_Object((1,3,6,1,4,1,17713,24,1,1,12,1,11),_CnAutoAttachActionProtectedPort_Type())
cnAutoAttachActionProtectedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionProtectedPort.setStatus(_A)
class _CnAutoAttachActionCambiumSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_G,3)))
_CnAutoAttachActionCambiumSync_Type.__name__=_C
_CnAutoAttachActionCambiumSync_Object=MibTableColumn
cnAutoAttachActionCambiumSync=_CnAutoAttachActionCambiumSync_Object((1,3,6,1,4,1,17713,24,1,1,12,1,12),_CnAutoAttachActionCambiumSync_Type())
cnAutoAttachActionCambiumSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionCambiumSync.setStatus(_A)
class _CnAutoAttachActionPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_J,1),('negotiated10Mbps',2),('negotiated100Mbps',3),('negotiated1Gbps',4),('negotiated2500Mbps',5),('forced10Mbps',6),('forced100Mbps',7),('forced1Gbps',8),('forced2500Mbps',9)))
_CnAutoAttachActionPortSpeed_Type.__name__=_C
_CnAutoAttachActionPortSpeed_Object=MibTableColumn
cnAutoAttachActionPortSpeed=_CnAutoAttachActionPortSpeed_Object((1,3,6,1,4,1,17713,24,1,1,12,1,13),_CnAutoAttachActionPortSpeed_Type())
cnAutoAttachActionPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionPortSpeed.setStatus(_A)
class _CnAutoAttachActionPortAdr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_G,3)))
_CnAutoAttachActionPortAdr_Type.__name__=_C
_CnAutoAttachActionPortAdr_Object=MibTableColumn
cnAutoAttachActionPortAdr=_CnAutoAttachActionPortAdr_Object((1,3,6,1,4,1,17713,24,1,1,12,1,14),_CnAutoAttachActionPortAdr_Type())
cnAutoAttachActionPortAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionPortAdr.setStatus(_A)
class _CnAutoAttachActionAutoVoip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachActionAutoVoip_Type.__name__=_C
_CnAutoAttachActionAutoVoip_Object=MibTableColumn
cnAutoAttachActionAutoVoip=_CnAutoAttachActionAutoVoip_Object((1,3,6,1,4,1,17713,24,1,1,12,1,15),_CnAutoAttachActionAutoVoip_Type())
cnAutoAttachActionAutoVoip.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachActionAutoVoip.setStatus(_A)
_CnAutoAttachPolicyTable_Object=MibTable
cnAutoAttachPolicyTable=_CnAutoAttachPolicyTable_Object((1,3,6,1,4,1,17713,24,1,1,13))
if mibBuilder.loadTexts:cnAutoAttachPolicyTable.setStatus(_A)
_CnAutoAttachPolicyEntry_Object=MibTableRow
cnAutoAttachPolicyEntry=_CnAutoAttachPolicyEntry_Object((1,3,6,1,4,1,17713,24,1,1,13,1))
cnAutoAttachPolicyEntry.setIndexNames((0,_I,_e))
if mibBuilder.loadTexts:cnAutoAttachPolicyEntry.setStatus(_A)
class _CnAutoAttachPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnAutoAttachPolicyName_Type.__name__=_D
_CnAutoAttachPolicyName_Object=MibTableColumn
cnAutoAttachPolicyName=_CnAutoAttachPolicyName_Object((1,3,6,1,4,1,17713,24,1,1,13,1,1),_CnAutoAttachPolicyName_Type())
cnAutoAttachPolicyName.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachPolicyName.setStatus(_A)
class _CnAutoAttachPolicyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachPolicyStatus_Type.__name__=_C
_CnAutoAttachPolicyStatus_Object=MibTableColumn
cnAutoAttachPolicyStatus=_CnAutoAttachPolicyStatus_Object((1,3,6,1,4,1,17713,24,1,1,13,1,2),_CnAutoAttachPolicyStatus_Type())
cnAutoAttachPolicyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyStatus.setStatus(_A)
class _CnAutoAttachPolicyPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CnAutoAttachPolicyPrecedence_Type.__name__=_C
_CnAutoAttachPolicyPrecedence_Object=MibTableColumn
cnAutoAttachPolicyPrecedence=_CnAutoAttachPolicyPrecedence_Object((1,3,6,1,4,1,17713,24,1,1,13,1,3),_CnAutoAttachPolicyPrecedence_Type())
cnAutoAttachPolicyPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyPrecedence.setStatus(_A)
class _CnAutoAttachPolicyRuleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnAutoAttachPolicyRuleName_Type.__name__=_D
_CnAutoAttachPolicyRuleName_Object=MibTableColumn
cnAutoAttachPolicyRuleName=_CnAutoAttachPolicyRuleName_Object((1,3,6,1,4,1,17713,24,1,1,13,1,4),_CnAutoAttachPolicyRuleName_Type())
cnAutoAttachPolicyRuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyRuleName.setStatus(_A)
class _CnAutoAttachPolicyRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_J,1),(_V,2),(_W,3),(_P,4),(_Q,5),(_X,6),(_Y,7),(_Z,8),(_R,9),(_a,10)))
_CnAutoAttachPolicyRuleType_Type.__name__=_C
_CnAutoAttachPolicyRuleType_Object=MibTableColumn
cnAutoAttachPolicyRuleType=_CnAutoAttachPolicyRuleType_Object((1,3,6,1,4,1,17713,24,1,1,13,1,5),_CnAutoAttachPolicyRuleType_Type())
cnAutoAttachPolicyRuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyRuleType.setStatus(_A)
class _CnAutoAttachPolicyRuleDeviceData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_CnAutoAttachPolicyRuleDeviceData_Type.__name__=_D
_CnAutoAttachPolicyRuleDeviceData_Object=MibTableColumn
cnAutoAttachPolicyRuleDeviceData=_CnAutoAttachPolicyRuleDeviceData_Object((1,3,6,1,4,1,17713,24,1,1,13,1,6),_CnAutoAttachPolicyRuleDeviceData_Type())
cnAutoAttachPolicyRuleDeviceData.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyRuleDeviceData.setStatus(_A)
class _CnAutoAttachPolicyActionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnAutoAttachPolicyActionName_Type.__name__=_D
_CnAutoAttachPolicyActionName_Object=MibTableColumn
cnAutoAttachPolicyActionName=_CnAutoAttachPolicyActionName_Object((1,3,6,1,4,1,17713,24,1,1,13,1,7),_CnAutoAttachPolicyActionName_Type())
cnAutoAttachPolicyActionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyActionName.setStatus(_A)
class _CnAutoAttachPolicyActionVlanData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CnAutoAttachPolicyActionVlanData_Type.__name__=_D
_CnAutoAttachPolicyActionVlanData_Object=MibTableColumn
cnAutoAttachPolicyActionVlanData=_CnAutoAttachPolicyActionVlanData_Object((1,3,6,1,4,1,17713,24,1,1,13,1,8),_CnAutoAttachPolicyActionVlanData_Type())
cnAutoAttachPolicyActionVlanData.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyActionVlanData.setStatus(_A)
class _CnAutoAttachPolicyActionPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CnAutoAttachPolicyActionPvid_Type.__name__=_C
_CnAutoAttachPolicyActionPvid_Object=MibTableColumn
cnAutoAttachPolicyActionPvid=_CnAutoAttachPolicyActionPvid_Object((1,3,6,1,4,1,17713,24,1,1,13,1,9),_CnAutoAttachPolicyActionPvid_Type())
cnAutoAttachPolicyActionPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyActionPvid.setStatus(_A)
class _CnAutoAttachPolicyActionPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_c,2),('trunk',3),(_d,4)))
_CnAutoAttachPolicyActionPortMode_Type.__name__=_C
_CnAutoAttachPolicyActionPortMode_Object=MibTableColumn
cnAutoAttachPolicyActionPortMode=_CnAutoAttachPolicyActionPortMode_Object((1,3,6,1,4,1,17713,24,1,1,13,1,10),_CnAutoAttachPolicyActionPortMode_Type())
cnAutoAttachPolicyActionPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyActionPortMode.setStatus(_A)
_CnAutoAttachPolicyApplied_Type=Counter32
_CnAutoAttachPolicyApplied_Object=MibTableColumn
cnAutoAttachPolicyApplied=_CnAutoAttachPolicyApplied_Object((1,3,6,1,4,1,17713,24,1,1,13,1,11),_CnAutoAttachPolicyApplied_Type())
cnAutoAttachPolicyApplied.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPolicyApplied.setStatus(_A)
_CnAutoAttachPolicyExpired_Type=Counter32
_CnAutoAttachPolicyExpired_Object=MibTableColumn
cnAutoAttachPolicyExpired=_CnAutoAttachPolicyExpired_Object((1,3,6,1,4,1,17713,24,1,1,13,1,12),_CnAutoAttachPolicyExpired_Type())
cnAutoAttachPolicyExpired.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPolicyExpired.setStatus(_A)
_CnAutoAttachPolicyErrors_Type=Counter32
_CnAutoAttachPolicyErrors_Object=MibTableColumn
cnAutoAttachPolicyErrors=_CnAutoAttachPolicyErrors_Object((1,3,6,1,4,1,17713,24,1,1,13,1,13),_CnAutoAttachPolicyErrors_Type())
cnAutoAttachPolicyErrors.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachPolicyErrors.setStatus(_A)
_CnAutoAttachPolicyRowStatus_Type=RowStatus
_CnAutoAttachPolicyRowStatus_Object=MibTableColumn
cnAutoAttachPolicyRowStatus=_CnAutoAttachPolicyRowStatus_Object((1,3,6,1,4,1,17713,24,1,1,13,1,14),_CnAutoAttachPolicyRowStatus_Type())
cnAutoAttachPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyRowStatus.setStatus(_A)
class _CnAutoAttachPolicyPortList_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_CnAutoAttachPolicyPortList_Type.__name__=_D
_CnAutoAttachPolicyPortList_Object=MibTableColumn
cnAutoAttachPolicyPortList=_CnAutoAttachPolicyPortList_Object((1,3,6,1,4,1,17713,24,1,1,13,1,15),_CnAutoAttachPolicyPortList_Type())
cnAutoAttachPolicyPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachPolicyPortList.setStatus(_A)
_CnAutoAttachScriptTable_Object=MibTable
cnAutoAttachScriptTable=_CnAutoAttachScriptTable_Object((1,3,6,1,4,1,17713,24,1,1,14))
if mibBuilder.loadTexts:cnAutoAttachScriptTable.setStatus(_A)
_CnAutoAttachScriptEntry_Object=MibTableRow
cnAutoAttachScriptEntry=_CnAutoAttachScriptEntry_Object((1,3,6,1,4,1,17713,24,1,1,14,1))
cnAutoAttachScriptEntry.setIndexNames((0,_I,_f))
if mibBuilder.loadTexts:cnAutoAttachScriptEntry.setStatus(_A)
class _CnAutoAttachScriptName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnAutoAttachScriptName_Type.__name__=_D
_CnAutoAttachScriptName_Object=MibTableColumn
cnAutoAttachScriptName=_CnAutoAttachScriptName_Object((1,3,6,1,4,1,17713,24,1,1,14,1,1),_CnAutoAttachScriptName_Type())
cnAutoAttachScriptName.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachScriptName.setStatus(_A)
class _CnAutoAttachScriptActionVlanData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CnAutoAttachScriptActionVlanData_Type.__name__=_D
_CnAutoAttachScriptActionVlanData_Object=MibTableColumn
cnAutoAttachScriptActionVlanData=_CnAutoAttachScriptActionVlanData_Object((1,3,6,1,4,1,17713,24,1,1,14,1,2),_CnAutoAttachScriptActionVlanData_Type())
cnAutoAttachScriptActionVlanData.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachScriptActionVlanData.setStatus(_A)
class _CnAutoAttachScriptActionPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CnAutoAttachScriptActionPvid_Type.__name__=_C
_CnAutoAttachScriptActionPvid_Object=MibTableColumn
cnAutoAttachScriptActionPvid=_CnAutoAttachScriptActionPvid_Object((1,3,6,1,4,1,17713,24,1,1,14,1,3),_CnAutoAttachScriptActionPvid_Type())
cnAutoAttachScriptActionPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachScriptActionPvid.setStatus(_A)
_CnAutoAttachScriptRowStatus_Type=RowStatus
_CnAutoAttachScriptRowStatus_Object=MibTableColumn
cnAutoAttachScriptRowStatus=_CnAutoAttachScriptRowStatus_Object((1,3,6,1,4,1,17713,24,1,1,14,1,4),_CnAutoAttachScriptRowStatus_Type())
cnAutoAttachScriptRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachScriptRowStatus.setStatus(_A)
_CnAutoAttachCondensedNbrTable_Object=MibTable
cnAutoAttachCondensedNbrTable=_CnAutoAttachCondensedNbrTable_Object((1,3,6,1,4,1,17713,24,1,1,15))
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrTable.setStatus(_A)
_CnAutoAttachCondensedNbrEntry_Object=MibTableRow
cnAutoAttachCondensedNbrEntry=_CnAutoAttachCondensedNbrEntry_Object((1,3,6,1,4,1,17713,24,1,1,15,1))
cnAutoAttachCondensedNbrEntry.setIndexNames((0,_I,_g))
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrEntry.setStatus(_A)
class _CnAutoAttachCondensedNbrIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CnAutoAttachCondensedNbrIfIndex_Type.__name__=_C
_CnAutoAttachCondensedNbrIfIndex_Object=MibTableColumn
cnAutoAttachCondensedNbrIfIndex=_CnAutoAttachCondensedNbrIfIndex_Object((1,3,6,1,4,1,17713,24,1,1,15,1,1),_CnAutoAttachCondensedNbrIfIndex_Type())
cnAutoAttachCondensedNbrIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrIfIndex.setStatus(_A)
class _CnAutoAttachCondensedNbrName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CnAutoAttachCondensedNbrName_Type.__name__=_D
_CnAutoAttachCondensedNbrName_Object=MibTableColumn
cnAutoAttachCondensedNbrName=_CnAutoAttachCondensedNbrName_Object((1,3,6,1,4,1,17713,24,1,1,15,1,2),_CnAutoAttachCondensedNbrName_Type())
cnAutoAttachCondensedNbrName.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrName.setStatus(_A)
class _CnAutoAttachCondensedNbrLldpChassisId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CnAutoAttachCondensedNbrLldpChassisId_Type.__name__=_D
_CnAutoAttachCondensedNbrLldpChassisId_Object=MibTableColumn
cnAutoAttachCondensedNbrLldpChassisId=_CnAutoAttachCondensedNbrLldpChassisId_Object((1,3,6,1,4,1,17713,24,1,1,15,1,3),_CnAutoAttachCondensedNbrLldpChassisId_Type())
cnAutoAttachCondensedNbrLldpChassisId.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrLldpChassisId.setStatus(_A)
class _CnAutoAttachCondensedNbrLldpPortId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CnAutoAttachCondensedNbrLldpPortId_Type.__name__=_D
_CnAutoAttachCondensedNbrLldpPortId_Object=MibTableColumn
cnAutoAttachCondensedNbrLldpPortId=_CnAutoAttachCondensedNbrLldpPortId_Object((1,3,6,1,4,1,17713,24,1,1,15,1,4),_CnAutoAttachCondensedNbrLldpPortId_Type())
cnAutoAttachCondensedNbrLldpPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrLldpPortId.setStatus(_A)
class _CnAutoAttachCondensedNbrLldpSystemName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CnAutoAttachCondensedNbrLldpSystemName_Type.__name__=_D
_CnAutoAttachCondensedNbrLldpSystemName_Object=MibTableColumn
cnAutoAttachCondensedNbrLldpSystemName=_CnAutoAttachCondensedNbrLldpSystemName_Object((1,3,6,1,4,1,17713,24,1,1,15,1,5),_CnAutoAttachCondensedNbrLldpSystemName_Type())
cnAutoAttachCondensedNbrLldpSystemName.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrLldpSystemName.setStatus(_A)
class _CnAutoAttachCondensedNbrLldpSystemDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CnAutoAttachCondensedNbrLldpSystemDesc_Type.__name__=_D
_CnAutoAttachCondensedNbrLldpSystemDesc_Object=MibTableColumn
cnAutoAttachCondensedNbrLldpSystemDesc=_CnAutoAttachCondensedNbrLldpSystemDesc_Object((1,3,6,1,4,1,17713,24,1,1,15,1,6),_CnAutoAttachCondensedNbrLldpSystemDesc_Type())
cnAutoAttachCondensedNbrLldpSystemDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrLldpSystemDesc.setStatus(_A)
class _CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Type.__name__=_D
_CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Object=MibTableColumn
cnAutoAttachCondensedNbrLldpMgmtIpv4Addr=_CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Object((1,3,6,1,4,1,17713,24,1,1,15,1,7),_CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Type())
cnAutoAttachCondensedNbrLldpMgmtIpv4Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrLldpMgmtIpv4Addr.setStatus(_A)
class _CnAutoAttachCondensedNbrMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(17,17))
_CnAutoAttachCondensedNbrMacAddress_Type.__name__=_L
_CnAutoAttachCondensedNbrMacAddress_Object=MibTableColumn
cnAutoAttachCondensedNbrMacAddress=_CnAutoAttachCondensedNbrMacAddress_Object((1,3,6,1,4,1,17713,24,1,1,15,1,8),_CnAutoAttachCondensedNbrMacAddress_Type())
cnAutoAttachCondensedNbrMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrMacAddress.setStatus(_A)
class _CnAutoAttachCondensedNbrClassification_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CnAutoAttachCondensedNbrClassification_Type.__name__=_D
_CnAutoAttachCondensedNbrClassification_Object=MibTableColumn
cnAutoAttachCondensedNbrClassification=_CnAutoAttachCondensedNbrClassification_Object((1,3,6,1,4,1,17713,24,1,1,15,1,9),_CnAutoAttachCondensedNbrClassification_Type())
cnAutoAttachCondensedNbrClassification.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachCondensedNbrClassification.setStatus(_A)
class _CnAutoAttachGlobalUplinkData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CnAutoAttachGlobalUplinkData_Type.__name__=_D
_CnAutoAttachGlobalUplinkData_Object=MibScalar
cnAutoAttachGlobalUplinkData=_CnAutoAttachGlobalUplinkData_Object((1,3,6,1,4,1,17713,24,1,1,16),_CnAutoAttachGlobalUplinkData_Type())
cnAutoAttachGlobalUplinkData.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachGlobalUplinkData.setStatus(_A)
class _CnAutoAttachAutoVlanStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachAutoVlanStatus_Type.__name__=_C
_CnAutoAttachAutoVlanStatus_Object=MibScalar
cnAutoAttachAutoVlanStatus=_CnAutoAttachAutoVlanStatus_Object((1,3,6,1,4,1,17713,24,1,1,17),_CnAutoAttachAutoVlanStatus_Type())
cnAutoAttachAutoVlanStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachAutoVlanStatus.setStatus(_A)
_CnAutoAttachNbrClassTable_Object=MibTable
cnAutoAttachNbrClassTable=_CnAutoAttachNbrClassTable_Object((1,3,6,1,4,1,17713,24,1,1,18))
if mibBuilder.loadTexts:cnAutoAttachNbrClassTable.setStatus(_A)
_CnAutoAttachNbrClassEntry_Object=MibTableRow
cnAutoAttachNbrClassEntry=_CnAutoAttachNbrClassEntry_Object((1,3,6,1,4,1,17713,24,1,1,18,1))
cnAutoAttachNbrClassEntry.setIndexNames((0,_I,_h),(0,_I,_i))
if mibBuilder.loadTexts:cnAutoAttachNbrClassEntry.setStatus(_A)
class _CnAutoAttachNbrClassType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('bridge',2),('ap',3),('router',4),('phone',5),('radio',6),('camera',7),(_j,8),('cambiumCnMatrix',9),('cambiumCnPilot',10)))
_CnAutoAttachNbrClassType_Type.__name__=_C
_CnAutoAttachNbrClassType_Object=MibTableColumn
cnAutoAttachNbrClassType=_CnAutoAttachNbrClassType_Object((1,3,6,1,4,1,17713,24,1,1,18,1,1),_CnAutoAttachNbrClassType_Type())
cnAutoAttachNbrClassType.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachNbrClassType.setStatus(_A)
class _CnAutoAttachNbrClassIdentifier_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CnAutoAttachNbrClassIdentifier_Type.__name__=_D
_CnAutoAttachNbrClassIdentifier_Object=MibTableColumn
cnAutoAttachNbrClassIdentifier=_CnAutoAttachNbrClassIdentifier_Object((1,3,6,1,4,1,17713,24,1,1,18,1,2),_CnAutoAttachNbrClassIdentifier_Type())
cnAutoAttachNbrClassIdentifier.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachNbrClassIdentifier.setStatus(_A)
class _CnAutoAttachNbrClassIdentifierType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lldp',1),(_R,2),('macAddress',3)))
_CnAutoAttachNbrClassIdentifierType_Type.__name__=_C
_CnAutoAttachNbrClassIdentifierType_Object=MibTableColumn
cnAutoAttachNbrClassIdentifierType=_CnAutoAttachNbrClassIdentifierType_Object((1,3,6,1,4,1,17713,24,1,1,18,1,3),_CnAutoAttachNbrClassIdentifierType_Type())
cnAutoAttachNbrClassIdentifierType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachNbrClassIdentifierType.setStatus(_A)
_CnAutoAttachNbrClassStorageType_Type=StorageType
_CnAutoAttachNbrClassStorageType_Object=MibTableColumn
cnAutoAttachNbrClassStorageType=_CnAutoAttachNbrClassStorageType_Object((1,3,6,1,4,1,17713,24,1,1,18,1,4),_CnAutoAttachNbrClassStorageType_Type())
cnAutoAttachNbrClassStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachNbrClassStorageType.setStatus(_A)
_CnAutoAttachNbrClassRowStatus_Type=RowStatus
_CnAutoAttachNbrClassRowStatus_Object=MibTableColumn
cnAutoAttachNbrClassRowStatus=_CnAutoAttachNbrClassRowStatus_Object((1,3,6,1,4,1,17713,24,1,1,18,1,5),_CnAutoAttachNbrClassRowStatus_Type())
cnAutoAttachNbrClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachNbrClassRowStatus.setStatus(_A)
class _CnAutoAttachDeviceLocalization_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnAutoAttachDeviceLocalization_Type.__name__=_D
_CnAutoAttachDeviceLocalization_Object=MibScalar
cnAutoAttachDeviceLocalization=_CnAutoAttachDeviceLocalization_Object((1,3,6,1,4,1,17713,24,1,1,19),_CnAutoAttachDeviceLocalization_Type())
cnAutoAttachDeviceLocalization.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachDeviceLocalization.setStatus(_A)
_CnAutoAttachMacListFileTable_Object=MibTable
cnAutoAttachMacListFileTable=_CnAutoAttachMacListFileTable_Object((1,3,6,1,4,1,17713,24,1,1,20))
if mibBuilder.loadTexts:cnAutoAttachMacListFileTable.setStatus(_A)
_CnAutoAttachMacListFileEntry_Object=MibTableRow
cnAutoAttachMacListFileEntry=_CnAutoAttachMacListFileEntry_Object((1,3,6,1,4,1,17713,24,1,1,20,1))
cnAutoAttachMacListFileEntry.setIndexNames((0,_I,_k))
if mibBuilder.loadTexts:cnAutoAttachMacListFileEntry.setStatus(_A)
class _CnAutoAttachMacListFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CnAutoAttachMacListFileName_Type.__name__=_D
_CnAutoAttachMacListFileName_Object=MibTableColumn
cnAutoAttachMacListFileName=_CnAutoAttachMacListFileName_Object((1,3,6,1,4,1,17713,24,1,1,20,1,1),_CnAutoAttachMacListFileName_Type())
cnAutoAttachMacListFileName.setMaxAccess(_K)
if mibBuilder.loadTexts:cnAutoAttachMacListFileName.setStatus(_A)
class _CnAutoAttachMacListFileMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CnAutoAttachMacListFileMacCount_Type.__name__=_C
_CnAutoAttachMacListFileMacCount_Object=MibTableColumn
cnAutoAttachMacListFileMacCount=_CnAutoAttachMacListFileMacCount_Object((1,3,6,1,4,1,17713,24,1,1,20,1,2),_CnAutoAttachMacListFileMacCount_Type())
cnAutoAttachMacListFileMacCount.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachMacListFileMacCount.setStatus(_A)
class _CnAutoAttachMacListFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('pendingDownload',2),('downloading',3),('downloaded',4),('failedDownload',5)))
_CnAutoAttachMacListFileStatus_Type.__name__=_C
_CnAutoAttachMacListFileStatus_Object=MibTableColumn
cnAutoAttachMacListFileStatus=_CnAutoAttachMacListFileStatus_Object((1,3,6,1,4,1,17713,24,1,1,20,1,3),_CnAutoAttachMacListFileStatus_Type())
cnAutoAttachMacListFileStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnAutoAttachMacListFileStatus.setStatus(_A)
class _CnAutoAttachMacListFileRefresh_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_CnAutoAttachMacListFileRefresh_Type.__name__=_C
_CnAutoAttachMacListFileRefresh_Object=MibTableColumn
cnAutoAttachMacListFileRefresh=_CnAutoAttachMacListFileRefresh_Object((1,3,6,1,4,1,17713,24,1,1,20,1,4),_CnAutoAttachMacListFileRefresh_Type())
cnAutoAttachMacListFileRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachMacListFileRefresh.setStatus(_A)
_CnAutoAttachMacListFileRowStatus_Type=RowStatus
_CnAutoAttachMacListFileRowStatus_Object=MibTableColumn
cnAutoAttachMacListFileRowStatus=_CnAutoAttachMacListFileRowStatus_Object((1,3,6,1,4,1,17713,24,1,1,20,1,5),_CnAutoAttachMacListFileRowStatus_Type())
cnAutoAttachMacListFileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnAutoAttachMacListFileRowStatus.setStatus(_A)
class _CnAutoAttachFileDownloadType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('macListFile',1))
_CnAutoAttachFileDownloadType_Type.__name__=_C
_CnAutoAttachFileDownloadType_Object=MibScalar
cnAutoAttachFileDownloadType=_CnAutoAttachFileDownloadType_Object((1,3,6,1,4,1,17713,24,1,1,21),_CnAutoAttachFileDownloadType_Type())
cnAutoAttachFileDownloadType.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachFileDownloadType.setStatus(_A)
class _CnAutoAttachFileDownloadPath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CnAutoAttachFileDownloadPath_Type.__name__=_D
_CnAutoAttachFileDownloadPath_Object=MibScalar
cnAutoAttachFileDownloadPath=_CnAutoAttachFileDownloadPath_Object((1,3,6,1,4,1,17713,24,1,1,22),_CnAutoAttachFileDownloadPath_Type())
cnAutoAttachFileDownloadPath.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachFileDownloadPath.setStatus(_A)
class _CnAutoAttachFileDownloadTransferMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*(('tftp',1),('sftp',2),('scp',5)))
_CnAutoAttachFileDownloadTransferMode_Type.__name__=_C
_CnAutoAttachFileDownloadTransferMode_Object=MibScalar
cnAutoAttachFileDownloadTransferMode=_CnAutoAttachFileDownloadTransferMode_Object((1,3,6,1,4,1,17713,24,1,1,23),_CnAutoAttachFileDownloadTransferMode_Type())
cnAutoAttachFileDownloadTransferMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachFileDownloadTransferMode.setStatus(_A)
_CnAutoAttachFileDownloadFromIpAddrType_Type=InetAddressType
_CnAutoAttachFileDownloadFromIpAddrType_Object=MibScalar
cnAutoAttachFileDownloadFromIpAddrType=_CnAutoAttachFileDownloadFromIpAddrType_Object((1,3,6,1,4,1,17713,24,1,1,24),_CnAutoAttachFileDownloadFromIpAddrType_Type())
cnAutoAttachFileDownloadFromIpAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachFileDownloadFromIpAddrType.setStatus(_A)
_CnAutoAttachFileDownloadFromIpvx_Type=InetAddress
_CnAutoAttachFileDownloadFromIpvx_Object=MibScalar
cnAutoAttachFileDownloadFromIpvx=_CnAutoAttachFileDownloadFromIpvx_Object((1,3,6,1,4,1,17713,24,1,1,25),_CnAutoAttachFileDownloadFromIpvx_Type())
cnAutoAttachFileDownloadFromIpvx.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachFileDownloadFromIpvx.setStatus(_A)
class _CnAutoAttachFileDownloadUsername_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CnAutoAttachFileDownloadUsername_Type.__name__=_D
_CnAutoAttachFileDownloadUsername_Object=MibScalar
cnAutoAttachFileDownloadUsername=_CnAutoAttachFileDownloadUsername_Object((1,3,6,1,4,1,17713,24,1,1,26),_CnAutoAttachFileDownloadUsername_Type())
cnAutoAttachFileDownloadUsername.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachFileDownloadUsername.setStatus(_A)
class _CnAutoAttachFileDownloadPassword_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CnAutoAttachFileDownloadPassword_Type.__name__=_D
_CnAutoAttachFileDownloadPassword_Object=MibScalar
cnAutoAttachFileDownloadPassword=_CnAutoAttachFileDownloadPassword_Object((1,3,6,1,4,1,17713,24,1,1,27),_CnAutoAttachFileDownloadPassword_Type())
cnAutoAttachFileDownloadPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:cnAutoAttachFileDownloadPassword.setStatus(_A)
_CnAutoAttachNotifyObjects_ObjectIdentity=ObjectIdentity
cnAutoAttachNotifyObjects=_CnAutoAttachNotifyObjects_ObjectIdentity((1,3,6,1,4,1,17713,24,1,2))
class _CnAutoAttachRemoteElemSysDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CnAutoAttachRemoteElemSysDescr_Type.__name__=_D
_CnAutoAttachRemoteElemSysDescr_Object=MibScalar
cnAutoAttachRemoteElemSysDescr=_CnAutoAttachRemoteElemSysDescr_Object((1,3,6,1,4,1,17713,24,1,2,1),_CnAutoAttachRemoteElemSysDescr_Type())
cnAutoAttachRemoteElemSysDescr.setMaxAccess(_l)
if mibBuilder.loadTexts:cnAutoAttachRemoteElemSysDescr.setStatus(_A)
_CnAutoAttachRemoteElemMgmtOid_Type=ObjectIdentifier
_CnAutoAttachRemoteElemMgmtOid_Object=MibScalar
cnAutoAttachRemoteElemMgmtOid=_CnAutoAttachRemoteElemMgmtOid_Object((1,3,6,1,4,1,17713,24,1,2,2),_CnAutoAttachRemoteElemMgmtOid_Type())
cnAutoAttachRemoteElemMgmtOid.setMaxAccess(_l)
if mibBuilder.loadTexts:cnAutoAttachRemoteElemMgmtOid.setStatus(_A)
cnAutoAttachInterfacePolicyApplied=NotificationType((1,3,6,1,4,1,17713,24,1,0,1))
cnAutoAttachInterfacePolicyApplied.setObjects(*((_M,_N),(_I,_S),(_I,_m),(_I,_n)))
if mibBuilder.loadTexts:cnAutoAttachInterfacePolicyApplied.setStatus(_A)
cnAutoAttachInterfacePolicyExpired=NotificationType((1,3,6,1,4,1,17713,24,1,0,2))
cnAutoAttachInterfacePolicyExpired.setObjects(*((_M,_N),(_I,_S)))
if mibBuilder.loadTexts:cnAutoAttachInterfacePolicyExpired.setStatus(_A)
mibBuilder.exportSymbols(_I,**{_j:cambium,'cnMatrix':cnMatrix,'cnAutoAttachMib':cnAutoAttachMib,'cnAutoAttachNotifications':cnAutoAttachNotifications,'cnAutoAttachInterfacePolicyApplied':cnAutoAttachInterfacePolicyApplied,'cnAutoAttachInterfacePolicyExpired':cnAutoAttachInterfacePolicyExpired,'cnAutoAttachObjects':cnAutoAttachObjects,'cnAutoAttachService':cnAutoAttachService,'cnAutoAttachDataDiffAllowed':cnAutoAttachDataDiffAllowed,'cnAutoAttachDeviceDataCompare':cnAutoAttachDeviceDataCompare,'cnAutoAttachClearPolicyStats':cnAutoAttachClearPolicyStats,'cnAutoAttachClearInterfaceStats':cnAutoAttachClearInterfaceStats,'cnAutoAttachUpdatePortDesc':cnAutoAttachUpdatePortDesc,'cnAutoAttachRestrictedMacMatch':cnAutoAttachRestrictedMacMatch,'cnAutoAttachActivePolicyReorder':cnAutoAttachActivePolicyReorder,'cnAutoAttachMacPolicyAging':cnAutoAttachMacPolicyAging,'cnAutoAttachPortTable':cnAutoAttachPortTable,'cnAutoAttachPortEntry':cnAutoAttachPortEntry,_T:cnAutoAttachPortIfIndex,'cnAutoAttachPortState':cnAutoAttachPortState,'cnAutoAttachPortMsgAuthStatus':cnAutoAttachPortMsgAuthStatus,'cnAutoAttachPortMsgAuthKey':cnAutoAttachPortMsgAuthKey,_S:cnAutoAttachPortActivePolicyName,'cnAutoAttachPortPolicyApplied':cnAutoAttachPortPolicyApplied,'cnAutoAttachPortPolicyExpired':cnAutoAttachPortPolicyExpired,'cnAutoAttachPortPolicyErrors':cnAutoAttachPortPolicyErrors,'cnAutoAttachPortRowStatus':cnAutoAttachPortRowStatus,'cnAutoAttachPortTlvTxEnable':cnAutoAttachPortTlvTxEnable,'cnAutoAttachPortDevSettingsTlvReceived':cnAutoAttachPortDevSettingsTlvReceived,'cnAutoAttachPortDevSettingsTlvProcessed':cnAutoAttachPortDevSettingsTlvProcessed,'cnAutoAttachPortDevSettingsTlvAuthFails':cnAutoAttachPortDevSettingsTlvAuthFails,'cnAutoAttachPortPrevPolicyName':cnAutoAttachPortPrevPolicyName,'cnAutoAttachRuleTable':cnAutoAttachRuleTable,'cnAutoAttachRuleEntry':cnAutoAttachRuleEntry,_U:cnAutoAttachRuleName,'cnAutoAttachRuleType':cnAutoAttachRuleType,'cnAutoAttachRuleDeviceData':cnAutoAttachRuleDeviceData,'cnAutoAttachRuleRowStatus':cnAutoAttachRuleRowStatus,'cnAutoAttachRuleListName':cnAutoAttachRuleListName,'cnAutoAttachRuleDataFileName':cnAutoAttachRuleDataFileName,'cnAutoAttachActionTable':cnAutoAttachActionTable,'cnAutoAttachActionEntry':cnAutoAttachActionEntry,_b:cnAutoAttachActionName,'cnAutoAttachActionVlanData':cnAutoAttachActionVlanData,'cnAutoAttachActionPvid':cnAutoAttachActionPvid,'cnAutoAttachActionPortMode':cnAutoAttachActionPortMode,'cnAutoAttachActionRowStatus':cnAutoAttachActionRowStatus,'cnAutoAttachActionUserPriority':cnAutoAttachActionUserPriority,'cnAutoAttachActionQosTrust':cnAutoAttachActionQosTrust,'cnAutoAttachActionUplinkData':cnAutoAttachActionUplinkData,'cnAutoAttachActionPoePriority':cnAutoAttachActionPoePriority,'cnAutoAttachActionPvidUpdateReset':cnAutoAttachActionPvidUpdateReset,'cnAutoAttachActionProtectedPort':cnAutoAttachActionProtectedPort,'cnAutoAttachActionCambiumSync':cnAutoAttachActionCambiumSync,'cnAutoAttachActionPortSpeed':cnAutoAttachActionPortSpeed,'cnAutoAttachActionPortAdr':cnAutoAttachActionPortAdr,'cnAutoAttachActionAutoVoip':cnAutoAttachActionAutoVoip,'cnAutoAttachPolicyTable':cnAutoAttachPolicyTable,'cnAutoAttachPolicyEntry':cnAutoAttachPolicyEntry,_e:cnAutoAttachPolicyName,'cnAutoAttachPolicyStatus':cnAutoAttachPolicyStatus,'cnAutoAttachPolicyPrecedence':cnAutoAttachPolicyPrecedence,'cnAutoAttachPolicyRuleName':cnAutoAttachPolicyRuleName,'cnAutoAttachPolicyRuleType':cnAutoAttachPolicyRuleType,'cnAutoAttachPolicyRuleDeviceData':cnAutoAttachPolicyRuleDeviceData,'cnAutoAttachPolicyActionName':cnAutoAttachPolicyActionName,'cnAutoAttachPolicyActionVlanData':cnAutoAttachPolicyActionVlanData,'cnAutoAttachPolicyActionPvid':cnAutoAttachPolicyActionPvid,'cnAutoAttachPolicyActionPortMode':cnAutoAttachPolicyActionPortMode,'cnAutoAttachPolicyApplied':cnAutoAttachPolicyApplied,'cnAutoAttachPolicyExpired':cnAutoAttachPolicyExpired,'cnAutoAttachPolicyErrors':cnAutoAttachPolicyErrors,'cnAutoAttachPolicyRowStatus':cnAutoAttachPolicyRowStatus,'cnAutoAttachPolicyPortList':cnAutoAttachPolicyPortList,'cnAutoAttachScriptTable':cnAutoAttachScriptTable,'cnAutoAttachScriptEntry':cnAutoAttachScriptEntry,_f:cnAutoAttachScriptName,'cnAutoAttachScriptActionVlanData':cnAutoAttachScriptActionVlanData,'cnAutoAttachScriptActionPvid':cnAutoAttachScriptActionPvid,'cnAutoAttachScriptRowStatus':cnAutoAttachScriptRowStatus,'cnAutoAttachCondensedNbrTable':cnAutoAttachCondensedNbrTable,'cnAutoAttachCondensedNbrEntry':cnAutoAttachCondensedNbrEntry,_g:cnAutoAttachCondensedNbrIfIndex,'cnAutoAttachCondensedNbrName':cnAutoAttachCondensedNbrName,'cnAutoAttachCondensedNbrLldpChassisId':cnAutoAttachCondensedNbrLldpChassisId,'cnAutoAttachCondensedNbrLldpPortId':cnAutoAttachCondensedNbrLldpPortId,'cnAutoAttachCondensedNbrLldpSystemName':cnAutoAttachCondensedNbrLldpSystemName,'cnAutoAttachCondensedNbrLldpSystemDesc':cnAutoAttachCondensedNbrLldpSystemDesc,'cnAutoAttachCondensedNbrLldpMgmtIpv4Addr':cnAutoAttachCondensedNbrLldpMgmtIpv4Addr,'cnAutoAttachCondensedNbrMacAddress':cnAutoAttachCondensedNbrMacAddress,'cnAutoAttachCondensedNbrClassification':cnAutoAttachCondensedNbrClassification,'cnAutoAttachGlobalUplinkData':cnAutoAttachGlobalUplinkData,'cnAutoAttachAutoVlanStatus':cnAutoAttachAutoVlanStatus,'cnAutoAttachNbrClassTable':cnAutoAttachNbrClassTable,'cnAutoAttachNbrClassEntry':cnAutoAttachNbrClassEntry,_h:cnAutoAttachNbrClassType,_i:cnAutoAttachNbrClassIdentifier,'cnAutoAttachNbrClassIdentifierType':cnAutoAttachNbrClassIdentifierType,'cnAutoAttachNbrClassStorageType':cnAutoAttachNbrClassStorageType,'cnAutoAttachNbrClassRowStatus':cnAutoAttachNbrClassRowStatus,'cnAutoAttachDeviceLocalization':cnAutoAttachDeviceLocalization,'cnAutoAttachMacListFileTable':cnAutoAttachMacListFileTable,'cnAutoAttachMacListFileEntry':cnAutoAttachMacListFileEntry,_k:cnAutoAttachMacListFileName,'cnAutoAttachMacListFileMacCount':cnAutoAttachMacListFileMacCount,'cnAutoAttachMacListFileStatus':cnAutoAttachMacListFileStatus,'cnAutoAttachMacListFileRefresh':cnAutoAttachMacListFileRefresh,'cnAutoAttachMacListFileRowStatus':cnAutoAttachMacListFileRowStatus,'cnAutoAttachFileDownloadType':cnAutoAttachFileDownloadType,'cnAutoAttachFileDownloadPath':cnAutoAttachFileDownloadPath,'cnAutoAttachFileDownloadTransferMode':cnAutoAttachFileDownloadTransferMode,'cnAutoAttachFileDownloadFromIpAddrType':cnAutoAttachFileDownloadFromIpAddrType,'cnAutoAttachFileDownloadFromIpvx':cnAutoAttachFileDownloadFromIpvx,'cnAutoAttachFileDownloadUsername':cnAutoAttachFileDownloadUsername,'cnAutoAttachFileDownloadPassword':cnAutoAttachFileDownloadPassword,'cnAutoAttachNotifyObjects':cnAutoAttachNotifyObjects,_m:cnAutoAttachRemoteElemSysDescr,_n:cnAutoAttachRemoteElemMgmtOid})