_Ac='atiStkSwPortLoopDetectCurrentAction'
_Ab='atiStkSwPortLoopDetectCurrentVlanId'
_Aa='atiStkSwSysNumOfModuleInStack'
_AZ='atiStkSwPortStormDetectCurrentLowAction'
_AY='atiStkSwPortStormDetectCurrentHighAction'
_AX='atiStkSwSysTemperatureLimitValue'
_AW='atiStkSwTrapVarMgmtIpAddr'
_AV='atiStkSwTrapVarMgmtType'
_AU='atiStkSwSysDCState'
_AT='atiStkSwSysRPSState'
_AS='atiStkSwSysRPSPresent'
_AR='atiStkSwIntruderAttackMacAddr'
_AQ='atiStkSwIntruderAttackVlanId'
_AP='atiStkSwACLId'
_AO='atiStkSwACLModuleId'
_AN='atiStkSwStaticTrunkIndex'
_AM='atiStkSwStaticTrunkModuleId'
_AL='atiStkSwQoSGroupPortCoSPriorityPortId'
_AK='atiStkSwQoSGroupPortCoSPriorityModuleId'
_AJ='atiStkSwQosPolicyId'
_AI='atiStkSwQosPolicyModuleId'
_AH='atiStkSwQosTrafficClassId'
_AG='atiStkSwQosTrafficClassModuleId'
_AF='atiStkSwQosFlowGrpId'
_AE='atiStkSwQosFlowGrpModuleId'
_AD='atiStkSwQoSGroupQueue'
_AC='egress-queue-7'
_AB='egress-queue-6'
_AA='egress-queue-5'
_A9='egress-queue-4'
_A8='egress-queue-3'
_A7='egress-queue-2'
_A6='egress-queue-1'
_A5='egress-queue-0'
_A4='atiStkSwQoSGroupCoSPriority'
_A3='atiStkSwStaticMacAddrVlanId'
_A2='atiStkSwStaticMacAddress'
_A1='atiStkSwGVRPCountersModuleId'
_A0='atiStkSwGVRPPortConfigPortId'
_z='atiStkSwGVRPPortConfigModuleId'
_y='atiStkSwMacAddrVlanId'
_x='atiStkSwMacAddress'
_w='atiStkSwVlanId'
_v='locked'
_u='secured'
_t='limited'
_s='automatic'
_r='telnet'
_q='atiStkSwSysMgmtACLConfigId'
_p='atiStkSwSysMgmtACLConfigModuleId'
_o='atiStkSwMemoryComBuffersModuleId'
_n='atiStkSwMemoryPoolIndex'
_m='atiStkSwMemoryPoolModuleId'
_l='atiStkSwMemoryInfoModuleId'
_k='atiStkSwCPUInfoModuleId'
_j='atiStkSwVoltageInfoIndex'
_i='atiStkSwVoltageInfoModuleId'
_h='atiStkSwFanInfoFanId'
_g='atiStkSwFanInfoModuleId'
_f='atiStkSwTemperatureInfoModuleId'
_e='atiStkSwSysUplinkPortId'
_d='atiStkSwSysUplinkModuleId'
_c='notPresent'
_b='broadcast-discard'
_a='linkdown'
_Z='port-disabled'
_Y='detected'
_X='inactive'
_W='atiStkSwPortDOSAttackType'
_V='enable'
_U='disable'
_T='other'
_S='normal'
_R='blocking'
_Q='read-create'
_P='none'
_O='obsolete'
_N='unknown'
_M='enabled'
_L='atiStkSwSysModuleId'
_K='no'
_J='yes'
_I='disabled'
_H='atiStkSwPortId'
_G='atiStkSwModuleId'
_F='DisplayString'
_E='AtiStackSwitch9424-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
alliedTelesyn=ModuleIdentity((1,3,6,1,4,1,207))
class AtiProductType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23)));namedValues=NamedValues(*((_T,1),('at8324',2),('at8316F-MT',3),('at8316F-VF',4),('at8316F-SC',5),('at8524M',6),('at8550GB',7),('at8516F',8),('at8550SP',9),('at9424T-SP',10),('at9424T-GB',11),('at9408LC-SP',12),('at8524-POE',13),('at9424Ti-SP',14),('at9448Ts-XP',15),('at9448Ts',16),('at9448T-SP',17),('at9424Ts-XP',18),('at9424Ts',19),('at9424T',21),('at9424T-POE',22),('at9424TL',23)))
class AtiPortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_T,1),(_c,2),('mgmt',3),('tenBaseT',4),('hundredBaseT',5),('hundredBaseFX-VF',6),('hundredBaseFX-MT',7),('hundredBaseFX-SC',8),('hundredBaseFX-LC',9),('thousandBaseT',10),('gigabit',11),('gigabitSX',12),('gigabitSX-SC',13),('gigabitSX-MT',14),('gigabitSX-VF',15),('gigabitSX-LC',16),('gigabitLX',17),('gigabitLX-SC',18),('gigabitLX-MT',19),('gigabitLX-VF',20),('gigabitLX-LC',21),('sm15',22),('ten-gigabit',23)))
class AtiUplinkType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_c,1),(_T,2),('applique-at-45-sc-sm',3),('applique-at-45-sc',4),('applique-at-45-mt',5),('applique-at-46',6),('applique-at-47',7),('sfp',8),('gbic',9),('xfp',10)))
_AtiProduct_ObjectIdentity=ObjectIdentity
atiProduct=_AtiProduct_ObjectIdentity((1,3,6,1,4,1,207,1))
_Swhub_ObjectIdentity=ObjectIdentity
swhub=_Swhub_ObjectIdentity((1,3,6,1,4,1,207,1,4))
_At_8324_ObjectIdentity=ObjectIdentity
at_8324=_At_8324_ObjectIdentity((1,3,6,1,4,1,207,1,4,37))
_At_8316F_ObjectIdentity=ObjectIdentity
at_8316F=_At_8316F_ObjectIdentity((1,3,6,1,4,1,207,1,4,77))
_At_8524M_ObjectIdentity=ObjectIdentity
at_8524M=_At_8524M_ObjectIdentity((1,3,6,1,4,1,207,1,4,98))
_At_8550GB_ObjectIdentity=ObjectIdentity
at_8550GB=_At_8550GB_ObjectIdentity((1,3,6,1,4,1,207,1,4,99))
_At_8516F_ObjectIdentity=ObjectIdentity
at_8516F=_At_8516F_ObjectIdentity((1,3,6,1,4,1,207,1,4,100))
_At_8550SP_ObjectIdentity=ObjectIdentity
at_8550SP=_At_8550SP_ObjectIdentity((1,3,6,1,4,1,207,1,4,104))
_At_9424T_SP_ObjectIdentity=ObjectIdentity
at_9424T_SP=_At_9424T_SP_ObjectIdentity((1,3,6,1,4,1,207,1,4,105))
_At_9424T_GB_ObjectIdentity=ObjectIdentity
at_9424T_GB=_At_9424T_GB_ObjectIdentity((1,3,6,1,4,1,207,1,4,112))
_At_8524POE_ObjectIdentity=ObjectIdentity
at_8524POE=_At_8524POE_ObjectIdentity((1,3,6,1,4,1,207,1,4,113))
_At_9408LC_SP_ObjectIdentity=ObjectIdentity
at_9408LC_SP=_At_9408LC_SP_ObjectIdentity((1,3,6,1,4,1,207,1,4,117))
_At_9424Ti_SP_ObjectIdentity=ObjectIdentity
at_9424Ti_SP=_At_9424Ti_SP_ObjectIdentity((1,3,6,1,4,1,207,1,4,118))
_At_9448Ts_XP_ObjectIdentity=ObjectIdentity
at_9448Ts_XP=_At_9448Ts_XP_ObjectIdentity((1,3,6,1,4,1,207,1,4,119))
_At_9448Ts_ObjectIdentity=ObjectIdentity
at_9448Ts=_At_9448Ts_ObjectIdentity((1,3,6,1,4,1,207,1,4,130))
_At_9448T_SP_ObjectIdentity=ObjectIdentity
at_9448T_SP=_At_9448T_SP_ObjectIdentity((1,3,6,1,4,1,207,1,4,131))
_At_9424Ts_XP_ObjectIdentity=ObjectIdentity
at_9424Ts_XP=_At_9424Ts_XP_ObjectIdentity((1,3,6,1,4,1,207,1,4,132))
_At_9424Ts_ObjectIdentity=ObjectIdentity
at_9424Ts=_At_9424Ts_ObjectIdentity((1,3,6,1,4,1,207,1,4,133))
_At_9424T_ObjectIdentity=ObjectIdentity
at_9424T=_At_9424T_ObjectIdentity((1,3,6,1,4,1,207,1,4,146))
_At_9424TPOE_ObjectIdentity=ObjectIdentity
at_9424TPOE=_At_9424TPOE_ObjectIdentity((1,3,6,1,4,1,207,1,4,152))
_At_9424TL_ObjectIdentity=ObjectIdentity
at_9424TL=_At_9424TL_ObjectIdentity((1,3,6,1,4,1,207,1,4,153))
_MibObject_ObjectIdentity=ObjectIdentity
mibObject=_MibObject_ObjectIdentity((1,3,6,1,4,1,207,8))
_AtiStkSwMib_ObjectIdentity=ObjectIdentity
atiStkSwMib=_AtiStkSwMib_ObjectIdentity((1,3,6,1,4,1,207,8,17))
_AtiStkSwSysGroup_ObjectIdentity=ObjectIdentity
atiStkSwSysGroup=_AtiStkSwSysGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,1))
_AtiStkSwSysConfig_ObjectIdentity=ObjectIdentity
atiStkSwSysConfig=_AtiStkSwSysConfig_ObjectIdentity((1,3,6,1,4,1,207,8,17,1,1))
class _AtiStkSwSysReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no-reset',1),('reset',2)))
_AtiStkSwSysReset_Type.__name__=_D
_AtiStkSwSysReset_Object=MibScalar
atiStkSwSysReset=_AtiStkSwSysReset_Object((1,3,6,1,4,1,207,8,17,1,1,1),_AtiStkSwSysReset_Type())
atiStkSwSysReset.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysReset.setStatus(_A)
_AtiStkSwSysIpAddress_Type=IpAddress
_AtiStkSwSysIpAddress_Object=MibScalar
atiStkSwSysIpAddress=_AtiStkSwSysIpAddress_Object((1,3,6,1,4,1,207,8,17,1,1,2),_AtiStkSwSysIpAddress_Type())
atiStkSwSysIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysIpAddress.setStatus(_A)
_AtiStkSwSysSubnetMask_Type=IpAddress
_AtiStkSwSysSubnetMask_Object=MibScalar
atiStkSwSysSubnetMask=_AtiStkSwSysSubnetMask_Object((1,3,6,1,4,1,207,8,17,1,1,3),_AtiStkSwSysSubnetMask_Type())
atiStkSwSysSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSubnetMask.setStatus(_A)
_AtiStkSwSysGateway_Type=IpAddress
_AtiStkSwSysGateway_Object=MibScalar
atiStkSwSysGateway=_AtiStkSwSysGateway_Object((1,3,6,1,4,1,207,8,17,1,1,4),_AtiStkSwSysGateway_Type())
atiStkSwSysGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysGateway.setStatus(_A)
class _AtiStkSwSysIpAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fromDhcp',1),('fromBootp',2),('static',3)))
_AtiStkSwSysIpAddressStatus_Type.__name__=_D
_AtiStkSwSysIpAddressStatus_Object=MibScalar
atiStkSwSysIpAddressStatus=_AtiStkSwSysIpAddressStatus_Object((1,3,6,1,4,1,207,8,17,1,1,5),_AtiStkSwSysIpAddressStatus_Type())
atiStkSwSysIpAddressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysIpAddressStatus.setStatus(_A)
_AtiStkSwSysDnsServer_Type=IpAddress
_AtiStkSwSysDnsServer_Object=MibScalar
atiStkSwSysDnsServer=_AtiStkSwSysDnsServer_Object((1,3,6,1,4,1,207,8,17,1,1,6),_AtiStkSwSysDnsServer_Type())
atiStkSwSysDnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysDnsServer.setStatus(_A)
_AtiStkSwSysDefaultDomainName_Type=DisplayString
_AtiStkSwSysDefaultDomainName_Object=MibScalar
atiStkSwSysDefaultDomainName=_AtiStkSwSysDefaultDomainName_Object((1,3,6,1,4,1,207,8,17,1,1,7),_AtiStkSwSysDefaultDomainName_Type())
atiStkSwSysDefaultDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysDefaultDomainName.setStatus(_A)
_AtiStkSwSysNumberOfModules_Type=Integer32
_AtiStkSwSysNumberOfModules_Object=MibScalar
atiStkSwSysNumberOfModules=_AtiStkSwSysNumberOfModules_Object((1,3,6,1,4,1,207,8,17,1,1,8),_AtiStkSwSysNumberOfModules_Type())
atiStkSwSysNumberOfModules.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysNumberOfModules.setStatus(_A)
class _AtiStkSwSysSpanningTreeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_AtiStkSwSysSpanningTreeStatus_Type.__name__=_D
_AtiStkSwSysSpanningTreeStatus_Object=MibScalar
atiStkSwSysSpanningTreeStatus=_AtiStkSwSysSpanningTreeStatus_Object((1,3,6,1,4,1,207,8,17,1,1,9),_AtiStkSwSysSpanningTreeStatus_Type())
atiStkSwSysSpanningTreeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSpanningTreeStatus.setStatus(_A)
class _AtiStkSwSysSpanningTreeVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rstp',1),('stp',2),('mstp',3)))
_AtiStkSwSysSpanningTreeVersion_Type.__name__=_D
_AtiStkSwSysSpanningTreeVersion_Object=MibScalar
atiStkSwSysSpanningTreeVersion=_AtiStkSwSysSpanningTreeVersion_Object((1,3,6,1,4,1,207,8,17,1,1,10),_AtiStkSwSysSpanningTreeVersion_Type())
atiStkSwSysSpanningTreeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSpanningTreeVersion.setStatus(_A)
class _AtiStkSwSysAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('saveConfig',1),('reset',2),('defaultConfig',3)))
_AtiStkSwSysAction_Type.__name__=_D
_AtiStkSwSysAction_Object=MibScalar
atiStkSwSysAction=_AtiStkSwSysAction_Object((1,3,6,1,4,1,207,8,17,1,1,11),_AtiStkSwSysAction_Type())
atiStkSwSysAction.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysAction.setStatus(_A)
class _AtiStkSwSysNumOfModuleInStack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwSysNumOfModuleInStack_Type.__name__=_D
_AtiStkSwSysNumOfModuleInStack_Object=MibScalar
atiStkSwSysNumOfModuleInStack=_AtiStkSwSysNumOfModuleInStack_Object((1,3,6,1,4,1,207,8,17,1,1,12),_AtiStkSwSysNumOfModuleInStack_Type())
atiStkSwSysNumOfModuleInStack.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysNumOfModuleInStack.setStatus(_A)
_AtiStkSwSysNwMgmt_ObjectIdentity=ObjectIdentity
atiStkSwSysNwMgmt=_AtiStkSwSysNwMgmt_ObjectIdentity((1,3,6,1,4,1,207,8,17,1,2))
_AtiStkSwSysTrapRecv1_Type=IpAddress
_AtiStkSwSysTrapRecv1_Object=MibScalar
atiStkSwSysTrapRecv1=_AtiStkSwSysTrapRecv1_Object((1,3,6,1,4,1,207,8,17,1,2,1),_AtiStkSwSysTrapRecv1_Type())
atiStkSwSysTrapRecv1.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysTrapRecv1.setStatus(_O)
_AtiStkSwSysTrapRecv2_Type=IpAddress
_AtiStkSwSysTrapRecv2_Object=MibScalar
atiStkSwSysTrapRecv2=_AtiStkSwSysTrapRecv2_Object((1,3,6,1,4,1,207,8,17,1,2,2),_AtiStkSwSysTrapRecv2_Type())
atiStkSwSysTrapRecv2.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysTrapRecv2.setStatus(_O)
_AtiStkSwSysTrapRecv3_Type=IpAddress
_AtiStkSwSysTrapRecv3_Object=MibScalar
atiStkSwSysTrapRecv3=_AtiStkSwSysTrapRecv3_Object((1,3,6,1,4,1,207,8,17,1,2,3),_AtiStkSwSysTrapRecv3_Type())
atiStkSwSysTrapRecv3.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysTrapRecv3.setStatus(_O)
_AtiStkSwSysTrapRecv4_Type=IpAddress
_AtiStkSwSysTrapRecv4_Object=MibScalar
atiStkSwSysTrapRecv4=_AtiStkSwSysTrapRecv4_Object((1,3,6,1,4,1,207,8,17,1,2,4),_AtiStkSwSysTrapRecv4_Type())
atiStkSwSysTrapRecv4.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysTrapRecv4.setStatus(_O)
_AtiStkSwSysProductInfoTable_Object=MibTable
atiStkSwSysProductInfoTable=_AtiStkSwSysProductInfoTable_Object((1,3,6,1,4,1,207,8,17,1,3))
if mibBuilder.loadTexts:atiStkSwSysProductInfoTable.setStatus(_A)
_AtiStkSwSysProductInfoEntry_Object=MibTableRow
atiStkSwSysProductInfoEntry=_AtiStkSwSysProductInfoEntry_Object((1,3,6,1,4,1,207,8,17,1,3,1))
atiStkSwSysProductInfoEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:atiStkSwSysProductInfoEntry.setStatus(_A)
class _AtiStkSwSysModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwSysModuleId_Type.__name__=_D
_AtiStkSwSysModuleId_Object=MibTableColumn
atiStkSwSysModuleId=_AtiStkSwSysModuleId_Object((1,3,6,1,4,1,207,8,17,1,3,1,1),_AtiStkSwSysModuleId_Type())
atiStkSwSysModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysModuleId.setStatus(_A)
_AtiStkSwSysProductType_Type=AtiProductType
_AtiStkSwSysProductType_Object=MibTableColumn
atiStkSwSysProductType=_AtiStkSwSysProductType_Object((1,3,6,1,4,1,207,8,17,1,3,1,2),_AtiStkSwSysProductType_Type())
atiStkSwSysProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysProductType.setStatus(_A)
_AtiStkSwSysMacAddress_Type=MacAddress
_AtiStkSwSysMacAddress_Object=MibTableColumn
atiStkSwSysMacAddress=_AtiStkSwSysMacAddress_Object((1,3,6,1,4,1,207,8,17,1,3,1,3),_AtiStkSwSysMacAddress_Type())
atiStkSwSysMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysMacAddress.setStatus(_A)
class _AtiStkSwSysSwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysSwName_Type.__name__=_F
_AtiStkSwSysSwName_Object=MibTableColumn
atiStkSwSysSwName=_AtiStkSwSysSwName_Object((1,3,6,1,4,1,207,8,17,1,3,1,4),_AtiStkSwSysSwName_Type())
atiStkSwSysSwName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysSwName.setStatus(_A)
class _AtiStkSwSysSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysSwVersion_Type.__name__=_F
_AtiStkSwSysSwVersion_Object=MibTableColumn
atiStkSwSysSwVersion=_AtiStkSwSysSwVersion_Object((1,3,6,1,4,1,207,8,17,1,3,1,5),_AtiStkSwSysSwVersion_Type())
atiStkSwSysSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysSwVersion.setStatus(_A)
class _AtiStkSwSysHwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysHwName_Type.__name__=_F
_AtiStkSwSysHwName_Object=MibTableColumn
atiStkSwSysHwName=_AtiStkSwSysHwName_Object((1,3,6,1,4,1,207,8,17,1,3,1,6),_AtiStkSwSysHwName_Type())
atiStkSwSysHwName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysHwName.setStatus(_A)
class _AtiStkSwSysHwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysHwRevision_Type.__name__=_F
_AtiStkSwSysHwRevision_Object=MibTableColumn
atiStkSwSysHwRevision=_AtiStkSwSysHwRevision_Object((1,3,6,1,4,1,207,8,17,1,3,1,7),_AtiStkSwSysHwRevision_Type())
atiStkSwSysHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysHwRevision.setStatus(_A)
class _AtiStkSwSysSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysSerialNumber_Type.__name__=_F
_AtiStkSwSysSerialNumber_Object=MibTableColumn
atiStkSwSysSerialNumber=_AtiStkSwSysSerialNumber_Object((1,3,6,1,4,1,207,8,17,1,3,1,8),_AtiStkSwSysSerialNumber_Type())
atiStkSwSysSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysSerialNumber.setStatus(_A)
_AtiStkSwSysTotalPortCount_Type=Integer32
_AtiStkSwSysTotalPortCount_Object=MibTableColumn
atiStkSwSysTotalPortCount=_AtiStkSwSysTotalPortCount_Object((1,3,6,1,4,1,207,8,17,1,3,1,9),_AtiStkSwSysTotalPortCount_Type())
atiStkSwSysTotalPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysTotalPortCount.setStatus(_A)
_AtiStkSwSysBasePortType_Type=AtiPortType
_AtiStkSwSysBasePortType_Object=MibTableColumn
atiStkSwSysBasePortType=_AtiStkSwSysBasePortType_Object((1,3,6,1,4,1,207,8,17,1,3,1,10),_AtiStkSwSysBasePortType_Type())
atiStkSwSysBasePortType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysBasePortType.setStatus(_A)
_AtiStkSwSysBasePortCount_Type=Integer32
_AtiStkSwSysBasePortCount_Object=MibTableColumn
atiStkSwSysBasePortCount=_AtiStkSwSysBasePortCount_Object((1,3,6,1,4,1,207,8,17,1,3,1,11),_AtiStkSwSysBasePortCount_Type())
atiStkSwSysBasePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysBasePortCount.setStatus(_A)
class _AtiStkSwSysUplinkAModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysUplinkAModelName_Type.__name__=_F
_AtiStkSwSysUplinkAModelName_Object=MibTableColumn
atiStkSwSysUplinkAModelName=_AtiStkSwSysUplinkAModelName_Object((1,3,6,1,4,1,207,8,17,1,3,1,12),_AtiStkSwSysUplinkAModelName_Type())
atiStkSwSysUplinkAModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkAModelName.setStatus(_A)
_AtiStkSwSysUplinkAPortType_Type=AtiPortType
_AtiStkSwSysUplinkAPortType_Object=MibTableColumn
atiStkSwSysUplinkAPortType=_AtiStkSwSysUplinkAPortType_Object((1,3,6,1,4,1,207,8,17,1,3,1,13),_AtiStkSwSysUplinkAPortType_Type())
atiStkSwSysUplinkAPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkAPortType.setStatus(_A)
_AtiStkSwSysUplinkAPortCount_Type=Integer32
_AtiStkSwSysUplinkAPortCount_Object=MibTableColumn
atiStkSwSysUplinkAPortCount=_AtiStkSwSysUplinkAPortCount_Object((1,3,6,1,4,1,207,8,17,1,3,1,14),_AtiStkSwSysUplinkAPortCount_Type())
atiStkSwSysUplinkAPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkAPortCount.setStatus(_A)
_AtiStkSwSysUplinkAPortIdBase_Type=Integer32
_AtiStkSwSysUplinkAPortIdBase_Object=MibTableColumn
atiStkSwSysUplinkAPortIdBase=_AtiStkSwSysUplinkAPortIdBase_Object((1,3,6,1,4,1,207,8,17,1,3,1,15),_AtiStkSwSysUplinkAPortIdBase_Type())
atiStkSwSysUplinkAPortIdBase.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkAPortIdBase.setStatus(_A)
_AtiStkSwSysUplinkAPortIdLimit_Type=Integer32
_AtiStkSwSysUplinkAPortIdLimit_Object=MibTableColumn
atiStkSwSysUplinkAPortIdLimit=_AtiStkSwSysUplinkAPortIdLimit_Object((1,3,6,1,4,1,207,8,17,1,3,1,16),_AtiStkSwSysUplinkAPortIdLimit_Type())
atiStkSwSysUplinkAPortIdLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkAPortIdLimit.setStatus(_A)
class _AtiStkSwSysUplinkBModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysUplinkBModelName_Type.__name__=_F
_AtiStkSwSysUplinkBModelName_Object=MibTableColumn
atiStkSwSysUplinkBModelName=_AtiStkSwSysUplinkBModelName_Object((1,3,6,1,4,1,207,8,17,1,3,1,17),_AtiStkSwSysUplinkBModelName_Type())
atiStkSwSysUplinkBModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkBModelName.setStatus(_A)
_AtiStkSwSysUplinkBPortType_Type=AtiPortType
_AtiStkSwSysUplinkBPortType_Object=MibTableColumn
atiStkSwSysUplinkBPortType=_AtiStkSwSysUplinkBPortType_Object((1,3,6,1,4,1,207,8,17,1,3,1,18),_AtiStkSwSysUplinkBPortType_Type())
atiStkSwSysUplinkBPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkBPortType.setStatus(_A)
_AtiStkSwSysUplinkBPortCount_Type=Integer32
_AtiStkSwSysUplinkBPortCount_Object=MibTableColumn
atiStkSwSysUplinkBPortCount=_AtiStkSwSysUplinkBPortCount_Object((1,3,6,1,4,1,207,8,17,1,3,1,19),_AtiStkSwSysUplinkBPortCount_Type())
atiStkSwSysUplinkBPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkBPortCount.setStatus(_A)
_AtiStkSwSysUplinkBPortIdBase_Type=Integer32
_AtiStkSwSysUplinkBPortIdBase_Object=MibTableColumn
atiStkSwSysUplinkBPortIdBase=_AtiStkSwSysUplinkBPortIdBase_Object((1,3,6,1,4,1,207,8,17,1,3,1,20),_AtiStkSwSysUplinkBPortIdBase_Type())
atiStkSwSysUplinkBPortIdBase.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkBPortIdBase.setStatus(_A)
_AtiStkSwSysUplinkBPortIdLimit_Type=Integer32
_AtiStkSwSysUplinkBPortIdLimit_Object=MibTableColumn
atiStkSwSysUplinkBPortIdLimit=_AtiStkSwSysUplinkBPortIdLimit_Object((1,3,6,1,4,1,207,8,17,1,3,1,21),_AtiStkSwSysUplinkBPortIdLimit_Type())
atiStkSwSysUplinkBPortIdLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkBPortIdLimit.setStatus(_A)
class _AtiStkSwSysRPSPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnected',2)))
_AtiStkSwSysRPSPresent_Type.__name__=_D
_AtiStkSwSysRPSPresent_Object=MibTableColumn
atiStkSwSysRPSPresent=_AtiStkSwSysRPSPresent_Object((1,3,6,1,4,1,207,8,17,1,3,1,22),_AtiStkSwSysRPSPresent_Type())
atiStkSwSysRPSPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysRPSPresent.setStatus(_A)
class _AtiStkSwSysRPSState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AtiStkSwSysRPSState_Type.__name__=_D
_AtiStkSwSysRPSState_Object=MibTableColumn
atiStkSwSysRPSState=_AtiStkSwSysRPSState_Object((1,3,6,1,4,1,207,8,17,1,3,1,23),_AtiStkSwSysRPSState_Type())
atiStkSwSysRPSState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysRPSState.setStatus(_A)
class _AtiStkSwSysDCState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AtiStkSwSysDCState_Type.__name__=_D
_AtiStkSwSysDCState_Object=MibTableColumn
atiStkSwSysDCState=_AtiStkSwSysDCState_Object((1,3,6,1,4,1,207,8,17,1,3,1,24),_AtiStkSwSysDCState_Type())
atiStkSwSysDCState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysDCState.setStatus(_A)
_AtiStkSwSysTemperatureLimitValue_Type=Integer32
_AtiStkSwSysTemperatureLimitValue_Object=MibTableColumn
atiStkSwSysTemperatureLimitValue=_AtiStkSwSysTemperatureLimitValue_Object((1,3,6,1,4,1,207,8,17,1,3,1,25),_AtiStkSwSysTemperatureLimitValue_Type())
atiStkSwSysTemperatureLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysTemperatureLimitValue.setStatus(_A)
_AtiStkSwSysUplinkInfoTable_Object=MibTable
atiStkSwSysUplinkInfoTable=_AtiStkSwSysUplinkInfoTable_Object((1,3,6,1,4,1,207,8,17,1,4))
if mibBuilder.loadTexts:atiStkSwSysUplinkInfoTable.setStatus(_A)
_AtiStkSwSysUplinkInfoEntry_Object=MibTableRow
atiStkSwSysUplinkInfoEntry=_AtiStkSwSysUplinkInfoEntry_Object((1,3,6,1,4,1,207,8,17,1,4,1))
atiStkSwSysUplinkInfoEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:atiStkSwSysUplinkInfoEntry.setStatus(_A)
class _AtiStkSwSysUplinkModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwSysUplinkModuleId_Type.__name__=_D
_AtiStkSwSysUplinkModuleId_Object=MibTableColumn
atiStkSwSysUplinkModuleId=_AtiStkSwSysUplinkModuleId_Object((1,3,6,1,4,1,207,8,17,1,4,1,1),_AtiStkSwSysUplinkModuleId_Type())
atiStkSwSysUplinkModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkModuleId.setStatus(_A)
class _AtiStkSwSysUplinkPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_AtiStkSwSysUplinkPortId_Type.__name__=_D
_AtiStkSwSysUplinkPortId_Object=MibTableColumn
atiStkSwSysUplinkPortId=_AtiStkSwSysUplinkPortId_Object((1,3,6,1,4,1,207,8,17,1,4,1,2),_AtiStkSwSysUplinkPortId_Type())
atiStkSwSysUplinkPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkPortId.setStatus(_A)
class _AtiStkSwSysUplinkSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('pluggable',2)))
_AtiStkSwSysUplinkSetup_Type.__name__=_D
_AtiStkSwSysUplinkSetup_Object=MibTableColumn
atiStkSwSysUplinkSetup=_AtiStkSwSysUplinkSetup_Object((1,3,6,1,4,1,207,8,17,1,4,1,3),_AtiStkSwSysUplinkSetup_Type())
atiStkSwSysUplinkSetup.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkSetup.setStatus(_A)
_AtiStkSwSysUplinkType_Type=AtiUplinkType
_AtiStkSwSysUplinkType_Object=MibTableColumn
atiStkSwSysUplinkType=_AtiStkSwSysUplinkType_Object((1,3,6,1,4,1,207,8,17,1,4,1,4),_AtiStkSwSysUplinkType_Type())
atiStkSwSysUplinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkType.setStatus(_A)
class _AtiStkSwSysUplinkDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwSysUplinkDetails_Type.__name__=_F
_AtiStkSwSysUplinkDetails_Object=MibTableColumn
atiStkSwSysUplinkDetails=_AtiStkSwSysUplinkDetails_Object((1,3,6,1,4,1,207,8,17,1,4,1,5),_AtiStkSwSysUplinkDetails_Type())
atiStkSwSysUplinkDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkDetails.setStatus(_A)
_AtiStkSwSysUplinkPortType_Type=AtiPortType
_AtiStkSwSysUplinkPortType_Object=MibTableColumn
atiStkSwSysUplinkPortType=_AtiStkSwSysUplinkPortType_Object((1,3,6,1,4,1,207,8,17,1,4,1,6),_AtiStkSwSysUplinkPortType_Type())
atiStkSwSysUplinkPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysUplinkPortType.setStatus(_A)
_AtiStkSwSysSystemTimeConfig_ObjectIdentity=ObjectIdentity
atiStkSwSysSystemTimeConfig=_AtiStkSwSysSystemTimeConfig_ObjectIdentity((1,3,6,1,4,1,207,8,17,1,5))
class _AtiStkSwSysCurrentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AtiStkSwSysCurrentTime_Type.__name__=_F
_AtiStkSwSysCurrentTime_Object=MibScalar
atiStkSwSysCurrentTime=_AtiStkSwSysCurrentTime_Object((1,3,6,1,4,1,207,8,17,1,5,1),_AtiStkSwSysCurrentTime_Type())
atiStkSwSysCurrentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysCurrentTime.setStatus(_A)
class _AtiStkSwSysCurrentDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AtiStkSwSysCurrentDate_Type.__name__=_F
_AtiStkSwSysCurrentDate_Object=MibScalar
atiStkSwSysCurrentDate=_AtiStkSwSysCurrentDate_Object((1,3,6,1,4,1,207,8,17,1,5,2),_AtiStkSwSysCurrentDate_Type())
atiStkSwSysCurrentDate.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysCurrentDate.setStatus(_A)
class _AtiStkSwSysSNTPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_M,2)))
_AtiStkSwSysSNTPStatus_Type.__name__=_D
_AtiStkSwSysSNTPStatus_Object=MibScalar
atiStkSwSysSNTPStatus=_AtiStkSwSysSNTPStatus_Object((1,3,6,1,4,1,207,8,17,1,5,3),_AtiStkSwSysSNTPStatus_Type())
atiStkSwSysSNTPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSNTPStatus.setStatus(_A)
_AtiStkSwSysSNTPServerIPAddress_Type=IpAddress
_AtiStkSwSysSNTPServerIPAddress_Object=MibScalar
atiStkSwSysSNTPServerIPAddress=_AtiStkSwSysSNTPServerIPAddress_Object((1,3,6,1,4,1,207,8,17,1,5,4),_AtiStkSwSysSNTPServerIPAddress_Type())
atiStkSwSysSNTPServerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSNTPServerIPAddress.setStatus(_A)
class _AtiStkSwSysSNTPUTCOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_AtiStkSwSysSNTPUTCOffset_Type.__name__=_D
_AtiStkSwSysSNTPUTCOffset_Object=MibScalar
atiStkSwSysSNTPUTCOffset=_AtiStkSwSysSNTPUTCOffset_Object((1,3,6,1,4,1,207,8,17,1,5,5),_AtiStkSwSysSNTPUTCOffset_Type())
atiStkSwSysSNTPUTCOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSNTPUTCOffset.setStatus(_A)
class _AtiStkSwSysSNTPDSTStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_M,2)))
_AtiStkSwSysSNTPDSTStatus_Type.__name__=_D
_AtiStkSwSysSNTPDSTStatus_Object=MibScalar
atiStkSwSysSNTPDSTStatus=_AtiStkSwSysSNTPDSTStatus_Object((1,3,6,1,4,1,207,8,17,1,5,6),_AtiStkSwSysSNTPDSTStatus_Type())
atiStkSwSysSNTPDSTStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSNTPDSTStatus.setStatus(_A)
class _AtiStkSwSysSNTPPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,1200))
_AtiStkSwSysSNTPPollingInterval_Type.__name__=_D
_AtiStkSwSysSNTPPollingInterval_Object=MibScalar
atiStkSwSysSNTPPollingInterval=_AtiStkSwSysSNTPPollingInterval_Object((1,3,6,1,4,1,207,8,17,1,5,7),_AtiStkSwSysSNTPPollingInterval_Type())
atiStkSwSysSNTPPollingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysSNTPPollingInterval.setStatus(_A)
_AtiStkSwSysSNTPLastDelta_Type=Integer32
_AtiStkSwSysSNTPLastDelta_Object=MibScalar
atiStkSwSysSNTPLastDelta=_AtiStkSwSysSNTPLastDelta_Object((1,3,6,1,4,1,207,8,17,1,5,8),_AtiStkSwSysSNTPLastDelta_Type())
atiStkSwSysSNTPLastDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysSNTPLastDelta.setStatus(_A)
_AtiStkSwSysInfoGroup_ObjectIdentity=ObjectIdentity
atiStkSwSysInfoGroup=_AtiStkSwSysInfoGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,1,6))
_AtiStkSwTemperatureInfoTable_Object=MibTable
atiStkSwTemperatureInfoTable=_AtiStkSwTemperatureInfoTable_Object((1,3,6,1,4,1,207,8,17,1,6,1))
if mibBuilder.loadTexts:atiStkSwTemperatureInfoTable.setStatus(_A)
_AtiStkSwTemperatureInfoEntry_Object=MibTableRow
atiStkSwTemperatureInfoEntry=_AtiStkSwTemperatureInfoEntry_Object((1,3,6,1,4,1,207,8,17,1,6,1,1))
atiStkSwTemperatureInfoEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:atiStkSwTemperatureInfoEntry.setStatus(_A)
class _AtiStkSwTemperatureInfoModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwTemperatureInfoModuleId_Type.__name__=_D
_AtiStkSwTemperatureInfoModuleId_Object=MibTableColumn
atiStkSwTemperatureInfoModuleId=_AtiStkSwTemperatureInfoModuleId_Object((1,3,6,1,4,1,207,8,17,1,6,1,1,1),_AtiStkSwTemperatureInfoModuleId_Type())
atiStkSwTemperatureInfoModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwTemperatureInfoModuleId.setStatus(_A)
class _AtiStkSwTemperatureInfoTemperature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_AtiStkSwTemperatureInfoTemperature_Type.__name__=_F
_AtiStkSwTemperatureInfoTemperature_Object=MibTableColumn
atiStkSwTemperatureInfoTemperature=_AtiStkSwTemperatureInfoTemperature_Object((1,3,6,1,4,1,207,8,17,1,6,1,1,2),_AtiStkSwTemperatureInfoTemperature_Type())
atiStkSwTemperatureInfoTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwTemperatureInfoTemperature.setStatus(_A)
_AtiStkSwFanInfoTable_Object=MibTable
atiStkSwFanInfoTable=_AtiStkSwFanInfoTable_Object((1,3,6,1,4,1,207,8,17,1,6,2))
if mibBuilder.loadTexts:atiStkSwFanInfoTable.setStatus(_A)
_AtiStkSwFanInfoEntry_Object=MibTableRow
atiStkSwFanInfoEntry=_AtiStkSwFanInfoEntry_Object((1,3,6,1,4,1,207,8,17,1,6,2,1))
atiStkSwFanInfoEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:atiStkSwFanInfoEntry.setStatus(_A)
class _AtiStkSwFanInfoModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwFanInfoModuleId_Type.__name__=_D
_AtiStkSwFanInfoModuleId_Object=MibTableColumn
atiStkSwFanInfoModuleId=_AtiStkSwFanInfoModuleId_Object((1,3,6,1,4,1,207,8,17,1,6,2,1,1),_AtiStkSwFanInfoModuleId_Type())
atiStkSwFanInfoModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwFanInfoModuleId.setStatus(_A)
class _AtiStkSwFanInfoFanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwFanInfoFanId_Type.__name__=_D
_AtiStkSwFanInfoFanId_Object=MibTableColumn
atiStkSwFanInfoFanId=_AtiStkSwFanInfoFanId_Object((1,3,6,1,4,1,207,8,17,1,6,2,1,2),_AtiStkSwFanInfoFanId_Type())
atiStkSwFanInfoFanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwFanInfoFanId.setStatus(_A)
class _AtiStkSwFanInfoState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_AtiStkSwFanInfoState_Type.__name__=_F
_AtiStkSwFanInfoState_Object=MibTableColumn
atiStkSwFanInfoState=_AtiStkSwFanInfoState_Object((1,3,6,1,4,1,207,8,17,1,6,2,1,3),_AtiStkSwFanInfoState_Type())
atiStkSwFanInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwFanInfoState.setStatus(_A)
class _AtiStkSwFanInfoSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_AtiStkSwFanInfoSpeed_Type.__name__=_F
_AtiStkSwFanInfoSpeed_Object=MibTableColumn
atiStkSwFanInfoSpeed=_AtiStkSwFanInfoSpeed_Object((1,3,6,1,4,1,207,8,17,1,6,2,1,4),_AtiStkSwFanInfoSpeed_Type())
atiStkSwFanInfoSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwFanInfoSpeed.setStatus(_A)
_AtiStkSwVoltageInfoTable_Object=MibTable
atiStkSwVoltageInfoTable=_AtiStkSwVoltageInfoTable_Object((1,3,6,1,4,1,207,8,17,1,6,3))
if mibBuilder.loadTexts:atiStkSwVoltageInfoTable.setStatus(_A)
_AtiStkSwVoltageInfoEntry_Object=MibTableRow
atiStkSwVoltageInfoEntry=_AtiStkSwVoltageInfoEntry_Object((1,3,6,1,4,1,207,8,17,1,6,3,1))
atiStkSwVoltageInfoEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:atiStkSwVoltageInfoEntry.setStatus(_A)
class _AtiStkSwVoltageInfoModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwVoltageInfoModuleId_Type.__name__=_D
_AtiStkSwVoltageInfoModuleId_Object=MibTableColumn
atiStkSwVoltageInfoModuleId=_AtiStkSwVoltageInfoModuleId_Object((1,3,6,1,4,1,207,8,17,1,6,3,1,1),_AtiStkSwVoltageInfoModuleId_Type())
atiStkSwVoltageInfoModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwVoltageInfoModuleId.setStatus(_A)
class _AtiStkSwVoltageInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AtiStkSwVoltageInfoIndex_Type.__name__=_D
_AtiStkSwVoltageInfoIndex_Object=MibTableColumn
atiStkSwVoltageInfoIndex=_AtiStkSwVoltageInfoIndex_Object((1,3,6,1,4,1,207,8,17,1,6,3,1,2),_AtiStkSwVoltageInfoIndex_Type())
atiStkSwVoltageInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwVoltageInfoIndex.setStatus(_A)
class _AtiStkSwVoltageInfoLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AtiStkSwVoltageInfoLevel_Type.__name__=_F
_AtiStkSwVoltageInfoLevel_Object=MibTableColumn
atiStkSwVoltageInfoLevel=_AtiStkSwVoltageInfoLevel_Object((1,3,6,1,4,1,207,8,17,1,6,3,1,3),_AtiStkSwVoltageInfoLevel_Type())
atiStkSwVoltageInfoLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwVoltageInfoLevel.setStatus(_A)
class _AtiStkSwVoltageInfoMeasured_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AtiStkSwVoltageInfoMeasured_Type.__name__=_F
_AtiStkSwVoltageInfoMeasured_Object=MibTableColumn
atiStkSwVoltageInfoMeasured=_AtiStkSwVoltageInfoMeasured_Object((1,3,6,1,4,1,207,8,17,1,6,3,1,4),_AtiStkSwVoltageInfoMeasured_Type())
atiStkSwVoltageInfoMeasured.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwVoltageInfoMeasured.setStatus(_A)
_AtiStkSwCPUInfoTable_Object=MibTable
atiStkSwCPUInfoTable=_AtiStkSwCPUInfoTable_Object((1,3,6,1,4,1,207,8,17,1,6,4))
if mibBuilder.loadTexts:atiStkSwCPUInfoTable.setStatus(_A)
_AtiStkSwCPUInfoEntry_Object=MibTableRow
atiStkSwCPUInfoEntry=_AtiStkSwCPUInfoEntry_Object((1,3,6,1,4,1,207,8,17,1,6,4,1))
atiStkSwCPUInfoEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:atiStkSwCPUInfoEntry.setStatus(_A)
class _AtiStkSwCPUInfoModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwCPUInfoModuleId_Type.__name__=_D
_AtiStkSwCPUInfoModuleId_Object=MibTableColumn
atiStkSwCPUInfoModuleId=_AtiStkSwCPUInfoModuleId_Object((1,3,6,1,4,1,207,8,17,1,6,4,1,1),_AtiStkSwCPUInfoModuleId_Type())
atiStkSwCPUInfoModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwCPUInfoModuleId.setStatus(_A)
class _AtiStkSwCPUInfoAvgLastMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AtiStkSwCPUInfoAvgLastMinute_Type.__name__=_D
_AtiStkSwCPUInfoAvgLastMinute_Object=MibTableColumn
atiStkSwCPUInfoAvgLastMinute=_AtiStkSwCPUInfoAvgLastMinute_Object((1,3,6,1,4,1,207,8,17,1,6,4,1,2),_AtiStkSwCPUInfoAvgLastMinute_Type())
atiStkSwCPUInfoAvgLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwCPUInfoAvgLastMinute.setStatus(_A)
class _AtiStkSwCPUInfoAvgLast20Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AtiStkSwCPUInfoAvgLast20Seconds_Type.__name__=_D
_AtiStkSwCPUInfoAvgLast20Seconds_Object=MibTableColumn
atiStkSwCPUInfoAvgLast20Seconds=_AtiStkSwCPUInfoAvgLast20Seconds_Object((1,3,6,1,4,1,207,8,17,1,6,4,1,3),_AtiStkSwCPUInfoAvgLast20Seconds_Type())
atiStkSwCPUInfoAvgLast20Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwCPUInfoAvgLast20Seconds.setStatus(_A)
class _AtiStkSwCPUInfoAvgSecond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AtiStkSwCPUInfoAvgSecond_Type.__name__=_D
_AtiStkSwCPUInfoAvgSecond_Object=MibTableColumn
atiStkSwCPUInfoAvgSecond=_AtiStkSwCPUInfoAvgSecond_Object((1,3,6,1,4,1,207,8,17,1,6,4,1,4),_AtiStkSwCPUInfoAvgSecond_Type())
atiStkSwCPUInfoAvgSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwCPUInfoAvgSecond.setStatus(_A)
_AtiStkSwMemoryGroup_ObjectIdentity=ObjectIdentity
atiStkSwMemoryGroup=_AtiStkSwMemoryGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,1,6,5))
_AtiStkSwMemoryInfoTable_Object=MibTable
atiStkSwMemoryInfoTable=_AtiStkSwMemoryInfoTable_Object((1,3,6,1,4,1,207,8,17,1,6,5,1))
if mibBuilder.loadTexts:atiStkSwMemoryInfoTable.setStatus(_A)
_AtiStkSwMemoryInfoEntry_Object=MibTableRow
atiStkSwMemoryInfoEntry=_AtiStkSwMemoryInfoEntry_Object((1,3,6,1,4,1,207,8,17,1,6,5,1,1))
atiStkSwMemoryInfoEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:atiStkSwMemoryInfoEntry.setStatus(_A)
_AtiStkSwMemoryInfoModuleId_Type=Integer32
_AtiStkSwMemoryInfoModuleId_Object=MibTableColumn
atiStkSwMemoryInfoModuleId=_AtiStkSwMemoryInfoModuleId_Object((1,3,6,1,4,1,207,8,17,1,6,5,1,1,1),_AtiStkSwMemoryInfoModuleId_Type())
atiStkSwMemoryInfoModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryInfoModuleId.setStatus(_A)
_AtiStkSwMemoryInfoTotalBuffers_Type=Integer32
_AtiStkSwMemoryInfoTotalBuffers_Object=MibTableColumn
atiStkSwMemoryInfoTotalBuffers=_AtiStkSwMemoryInfoTotalBuffers_Object((1,3,6,1,4,1,207,8,17,1,6,5,1,1,2),_AtiStkSwMemoryInfoTotalBuffers_Type())
atiStkSwMemoryInfoTotalBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryInfoTotalBuffers.setStatus(_A)
_AtiStkSwMemoryPoolTable_Object=MibTable
atiStkSwMemoryPoolTable=_AtiStkSwMemoryPoolTable_Object((1,3,6,1,4,1,207,8,17,1,6,5,2))
if mibBuilder.loadTexts:atiStkSwMemoryPoolTable.setStatus(_A)
_AtiStkSwMemoryPoolEntry_Object=MibTableRow
atiStkSwMemoryPoolEntry=_AtiStkSwMemoryPoolEntry_Object((1,3,6,1,4,1,207,8,17,1,6,5,2,1))
atiStkSwMemoryPoolEntry.setIndexNames((0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:atiStkSwMemoryPoolEntry.setStatus(_A)
_AtiStkSwMemoryPoolModuleId_Type=Integer32
_AtiStkSwMemoryPoolModuleId_Object=MibTableColumn
atiStkSwMemoryPoolModuleId=_AtiStkSwMemoryPoolModuleId_Object((1,3,6,1,4,1,207,8,17,1,6,5,2,1,1),_AtiStkSwMemoryPoolModuleId_Type())
atiStkSwMemoryPoolModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryPoolModuleId.setStatus(_A)
_AtiStkSwMemoryPoolIndex_Type=Integer32
_AtiStkSwMemoryPoolIndex_Object=MibTableColumn
atiStkSwMemoryPoolIndex=_AtiStkSwMemoryPoolIndex_Object((1,3,6,1,4,1,207,8,17,1,6,5,2,1,2),_AtiStkSwMemoryPoolIndex_Type())
atiStkSwMemoryPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryPoolIndex.setStatus(_A)
_AtiStkSwMemoryPoolName_Type=DisplayString
_AtiStkSwMemoryPoolName_Object=MibTableColumn
atiStkSwMemoryPoolName=_AtiStkSwMemoryPoolName_Object((1,3,6,1,4,1,207,8,17,1,6,5,2,1,3),_AtiStkSwMemoryPoolName_Type())
atiStkSwMemoryPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryPoolName.setStatus(_A)
_AtiStkSwMemoryPoolTotal_Type=Integer32
_AtiStkSwMemoryPoolTotal_Object=MibTableColumn
atiStkSwMemoryPoolTotal=_AtiStkSwMemoryPoolTotal_Object((1,3,6,1,4,1,207,8,17,1,6,5,2,1,4),_AtiStkSwMemoryPoolTotal_Type())
atiStkSwMemoryPoolTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryPoolTotal.setStatus(_A)
_AtiStkSwMemoryPoolFree_Type=Integer32
_AtiStkSwMemoryPoolFree_Object=MibTableColumn
atiStkSwMemoryPoolFree=_AtiStkSwMemoryPoolFree_Object((1,3,6,1,4,1,207,8,17,1,6,5,2,1,5),_AtiStkSwMemoryPoolFree_Type())
atiStkSwMemoryPoolFree.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryPoolFree.setStatus(_A)
_AtiStkSwMemoryComBuffersTable_Object=MibTable
atiStkSwMemoryComBuffersTable=_AtiStkSwMemoryComBuffersTable_Object((1,3,6,1,4,1,207,8,17,1,6,5,3))
if mibBuilder.loadTexts:atiStkSwMemoryComBuffersTable.setStatus(_A)
_AtiStkSwMemoryComBuffersEntry_Object=MibTableRow
atiStkSwMemoryComBuffersEntry=_AtiStkSwMemoryComBuffersEntry_Object((1,3,6,1,4,1,207,8,17,1,6,5,3,1))
atiStkSwMemoryComBuffersEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:atiStkSwMemoryComBuffersEntry.setStatus(_A)
_AtiStkSwMemoryComBuffersModuleId_Type=Integer32
_AtiStkSwMemoryComBuffersModuleId_Object=MibTableColumn
atiStkSwMemoryComBuffersModuleId=_AtiStkSwMemoryComBuffersModuleId_Object((1,3,6,1,4,1,207,8,17,1,6,5,3,1,1),_AtiStkSwMemoryComBuffersModuleId_Type())
atiStkSwMemoryComBuffersModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryComBuffersModuleId.setStatus(_A)
_AtiStkSwMemoryTotalComBuffers_Type=Integer32
_AtiStkSwMemoryTotalComBuffers_Object=MibTableColumn
atiStkSwMemoryTotalComBuffers=_AtiStkSwMemoryTotalComBuffers_Object((1,3,6,1,4,1,207,8,17,1,6,5,3,1,2),_AtiStkSwMemoryTotalComBuffers_Type())
atiStkSwMemoryTotalComBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryTotalComBuffers.setStatus(_A)
_AtiStkSwMemoryFreeComBuffers_Type=Integer32
_AtiStkSwMemoryFreeComBuffers_Object=MibTableColumn
atiStkSwMemoryFreeComBuffers=_AtiStkSwMemoryFreeComBuffers_Object((1,3,6,1,4,1,207,8,17,1,6,5,3,1,3),_AtiStkSwMemoryFreeComBuffers_Type())
atiStkSwMemoryFreeComBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMemoryFreeComBuffers.setStatus(_A)
_AtiStkSwSysMgmtACLGroup_ObjectIdentity=ObjectIdentity
atiStkSwSysMgmtACLGroup=_AtiStkSwSysMgmtACLGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,1,7))
class _AtiStkSwSysMgmtACLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_I,2)))
_AtiStkSwSysMgmtACLStatus_Type.__name__=_D
_AtiStkSwSysMgmtACLStatus_Object=MibScalar
atiStkSwSysMgmtACLStatus=_AtiStkSwSysMgmtACLStatus_Object((1,3,6,1,4,1,207,8,17,1,7,1),_AtiStkSwSysMgmtACLStatus_Type())
atiStkSwSysMgmtACLStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysMgmtACLStatus.setStatus(_A)
_AtiStkSwSysMgmtACLConfigTable_Object=MibTable
atiStkSwSysMgmtACLConfigTable=_AtiStkSwSysMgmtACLConfigTable_Object((1,3,6,1,4,1,207,8,17,1,7,2))
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigTable.setStatus(_A)
_AtiStkSwSysMgmtACLConfigEntry_Object=MibTableRow
atiStkSwSysMgmtACLConfigEntry=_AtiStkSwSysMgmtACLConfigEntry_Object((1,3,6,1,4,1,207,8,17,1,7,2,1))
atiStkSwSysMgmtACLConfigEntry.setIndexNames((0,_E,_p),(0,_E,_q))
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigEntry.setStatus(_A)
class _AtiStkSwSysMgmtACLConfigModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwSysMgmtACLConfigModuleId_Type.__name__=_D
_AtiStkSwSysMgmtACLConfigModuleId_Object=MibTableColumn
atiStkSwSysMgmtACLConfigModuleId=_AtiStkSwSysMgmtACLConfigModuleId_Object((1,3,6,1,4,1,207,8,17,1,7,2,1,1),_AtiStkSwSysMgmtACLConfigModuleId_Type())
atiStkSwSysMgmtACLConfigModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigModuleId.setStatus(_A)
class _AtiStkSwSysMgmtACLConfigId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_AtiStkSwSysMgmtACLConfigId_Type.__name__=_D
_AtiStkSwSysMgmtACLConfigId_Object=MibTableColumn
atiStkSwSysMgmtACLConfigId=_AtiStkSwSysMgmtACLConfigId_Object((1,3,6,1,4,1,207,8,17,1,7,2,1,2),_AtiStkSwSysMgmtACLConfigId_Type())
atiStkSwSysMgmtACLConfigId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigId.setStatus(_A)
_AtiStkSwSysMgmtACLConfigIpAddr_Type=IpAddress
_AtiStkSwSysMgmtACLConfigIpAddr_Object=MibTableColumn
atiStkSwSysMgmtACLConfigIpAddr=_AtiStkSwSysMgmtACLConfigIpAddr_Object((1,3,6,1,4,1,207,8,17,1,7,2,1,3),_AtiStkSwSysMgmtACLConfigIpAddr_Type())
atiStkSwSysMgmtACLConfigIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigIpAddr.setStatus(_A)
_AtiStkSwSysMgmtACLConfigMask_Type=IpAddress
_AtiStkSwSysMgmtACLConfigMask_Object=MibTableColumn
atiStkSwSysMgmtACLConfigMask=_AtiStkSwSysMgmtACLConfigMask_Object((1,3,6,1,4,1,207,8,17,1,7,2,1,4),_AtiStkSwSysMgmtACLConfigMask_Type())
atiStkSwSysMgmtACLConfigMask.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigMask.setStatus(_A)
class _AtiStkSwSysMgmtACLConfigApplication_Type(Bits):namedValues=NamedValues(*((_r,0),('web',1),('ping',2)))
_AtiStkSwSysMgmtACLConfigApplication_Type.__name__='Bits'
_AtiStkSwSysMgmtACLConfigApplication_Object=MibTableColumn
atiStkSwSysMgmtACLConfigApplication=_AtiStkSwSysMgmtACLConfigApplication_Object((1,3,6,1,4,1,207,8,17,1,7,2,1,5),_AtiStkSwSysMgmtACLConfigApplication_Type())
atiStkSwSysMgmtACLConfigApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigApplication.setStatus(_A)
_AtiStkSwSysMgmtACLConfigRowStatus_Type=RowStatus
_AtiStkSwSysMgmtACLConfigRowStatus_Object=MibTableColumn
atiStkSwSysMgmtACLConfigRowStatus=_AtiStkSwSysMgmtACLConfigRowStatus_Object((1,3,6,1,4,1,207,8,17,1,7,2,1,6),_AtiStkSwSysMgmtACLConfigRowStatus_Type())
atiStkSwSysMgmtACLConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwSysMgmtACLConfigRowStatus.setStatus(_A)
_AtiStkSwPortGroup_ObjectIdentity=ObjectIdentity
atiStkSwPortGroup=_AtiStkSwPortGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,2))
_AtiStkSwPortConfigTable_Object=MibTable
atiStkSwPortConfigTable=_AtiStkSwPortConfigTable_Object((1,3,6,1,4,1,207,8,17,2,1))
if mibBuilder.loadTexts:atiStkSwPortConfigTable.setStatus(_A)
_AtiStkSwPortConfigEntry_Object=MibTableRow
atiStkSwPortConfigEntry=_AtiStkSwPortConfigEntry_Object((1,3,6,1,4,1,207,8,17,2,1,1))
atiStkSwPortConfigEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkSwPortConfigEntry.setStatus(_A)
class _AtiStkSwModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwModuleId_Type.__name__=_D
_AtiStkSwModuleId_Object=MibTableColumn
atiStkSwModuleId=_AtiStkSwModuleId_Object((1,3,6,1,4,1,207,8,17,2,1,1,1),_AtiStkSwModuleId_Type())
atiStkSwModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwModuleId.setStatus(_A)
class _AtiStkSwPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_AtiStkSwPortId_Type.__name__=_D
_AtiStkSwPortId_Object=MibTableColumn
atiStkSwPortId=_AtiStkSwPortId_Object((1,3,6,1,4,1,207,8,17,2,1,1,2),_AtiStkSwPortId_Type())
atiStkSwPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortId.setStatus(_A)
class _AtiStkSwPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_AtiStkSwPortName_Type.__name__=_F
_AtiStkSwPortName_Object=MibTableColumn
atiStkSwPortName=_AtiStkSwPortName_Object((1,3,6,1,4,1,207,8,17,2,1,1,3),_AtiStkSwPortName_Type())
atiStkSwPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortName.setStatus(_A)
class _AtiStkSwPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_I,2)))
_AtiStkSwPortState_Type.__name__=_D
_AtiStkSwPortState_Object=MibTableColumn
atiStkSwPortState=_AtiStkSwPortState_Object((1,3,6,1,4,1,207,8,17,2,1,1,4),_AtiStkSwPortState_Type())
atiStkSwPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortState.setStatus(_A)
class _AtiStkSwPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_AtiStkSwPortLinkState_Type.__name__=_D
_AtiStkSwPortLinkState_Object=MibTableColumn
atiStkSwPortLinkState=_AtiStkSwPortLinkState_Object((1,3,6,1,4,1,207,8,17,2,1,1,5),_AtiStkSwPortLinkState_Type())
atiStkSwPortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortLinkState.setStatus(_A)
class _AtiStkSwPortNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('autosense',1),('forceHalfDuplex-10M',2),('forceHalfDuplex-100M',3),('forceHalfDuplex-1G',4),('forceFullDuplex-10M',5),('forceFullDuplex-100M',6),('forceFullDuplex-1G',7),('autoHalfDuplex-10M',8),('autoHalfDuplex-100M',9),('autoFullDuplex-10M',10),('autoFullDuplex-100M',11)))
_AtiStkSwPortNegotiation_Type.__name__=_D
_AtiStkSwPortNegotiation_Object=MibTableColumn
atiStkSwPortNegotiation=_AtiStkSwPortNegotiation_Object((1,3,6,1,4,1,207,8,17,2,1,1,6),_AtiStkSwPortNegotiation_Type())
atiStkSwPortNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortNegotiation.setStatus(_A)
class _AtiStkSwPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('speed-10M',2),('speed-100M',3),('speed-1G',4)))
_AtiStkSwPortSpeed_Type.__name__=_D
_AtiStkSwPortSpeed_Object=MibTableColumn
atiStkSwPortSpeed=_AtiStkSwPortSpeed_Object((1,3,6,1,4,1,207,8,17,2,1,1,7),_AtiStkSwPortSpeed_Type())
atiStkSwPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortSpeed.setStatus(_A)
class _AtiStkSwPortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('halfDuplex',2),('fullDuplex',3)))
_AtiStkSwPortDuplexStatus_Type.__name__=_D
_AtiStkSwPortDuplexStatus_Object=MibTableColumn
atiStkSwPortDuplexStatus=_AtiStkSwPortDuplexStatus_Object((1,3,6,1,4,1,207,8,17,2,1,1,8),_AtiStkSwPortDuplexStatus_Type())
atiStkSwPortDuplexStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortDuplexStatus.setStatus(_A)
class _AtiStkSwPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_U,2),(_V,3)))
_AtiStkSwPortFlowControl_Type.__name__=_D
_AtiStkSwPortFlowControl_Object=MibTableColumn
atiStkSwPortFlowControl=_AtiStkSwPortFlowControl_Object((1,3,6,1,4,1,207,8,17,2,1,1,9),_AtiStkSwPortFlowControl_Type())
atiStkSwPortFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortFlowControl.setStatus(_A)
class _AtiStkSwPortBackPressure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_U,2),(_V,3)))
_AtiStkSwPortBackPressure_Type.__name__=_D
_AtiStkSwPortBackPressure_Object=MibTableColumn
atiStkSwPortBackPressure=_AtiStkSwPortBackPressure_Object((1,3,6,1,4,1,207,8,17,2,1,1,10),_AtiStkSwPortBackPressure_Type())
atiStkSwPortBackPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortBackPressure.setStatus(_A)
class _AtiStkSwPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('use-vlan-priority',1),('override-and-use-low-priority',2),('override-and-use-high-priority',3)))
_AtiStkSwPortPriority_Type.__name__=_D
_AtiStkSwPortPriority_Object=MibTableColumn
atiStkSwPortPriority=_AtiStkSwPortPriority_Object((1,3,6,1,4,1,207,8,17,2,1,1,11),_AtiStkSwPortPriority_Type())
atiStkSwPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortPriority.setStatus(_A)
class _AtiStkSwPortBroadcastProcessing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard-broadcasts',1),('do-not-discard-broadcasts',2)))
_AtiStkSwPortBroadcastProcessing_Type.__name__=_D
_AtiStkSwPortBroadcastProcessing_Object=MibTableColumn
atiStkSwPortBroadcastProcessing=_AtiStkSwPortBroadcastProcessing_Object((1,3,6,1,4,1,207,8,17,2,1,1,12),_AtiStkSwPortBroadcastProcessing_Type())
atiStkSwPortBroadcastProcessing.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortBroadcastProcessing.setStatus(_A)
class _AtiStkSwPortMDIO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mdi',1),('mdix',2),('auto-mdix',3)))
_AtiStkSwPortMDIO_Type.__name__=_D
_AtiStkSwPortMDIO_Object=MibTableColumn
atiStkSwPortMDIO=_AtiStkSwPortMDIO_Object((1,3,6,1,4,1,207,8,17,2,1,1,13),_AtiStkSwPortMDIO_Type())
atiStkSwPortMDIO.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMDIO.setStatus(_A)
class _AtiStkSwPortHOLLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_AtiStkSwPortHOLLimit_Type.__name__=_D
_AtiStkSwPortHOLLimit_Object=MibTableColumn
atiStkSwPortHOLLimit=_AtiStkSwPortHOLLimit_Object((1,3,6,1,4,1,207,8,17,2,1,1,14),_AtiStkSwPortHOLLimit_Type())
atiStkSwPortHOLLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortHOLLimit.setStatus(_A)
class _AtiStkSwPortBackPressureLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,57344))
_AtiStkSwPortBackPressureLimit_Type.__name__=_D
_AtiStkSwPortBackPressureLimit_Object=MibTableColumn
atiStkSwPortBackPressureLimit=_AtiStkSwPortBackPressureLimit_Object((1,3,6,1,4,1,207,8,17,2,1,1,15),_AtiStkSwPortBackPressureLimit_Type())
atiStkSwPortBackPressureLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortBackPressureLimit.setStatus(_A)
class _AtiStkSwPortSTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_I,2),(_R,3),('listening',4),('learning',5),('forwarding',6)))
_AtiStkSwPortSTPState_Type.__name__=_D
_AtiStkSwPortSTPState_Object=MibTableColumn
atiStkSwPortSTPState=_AtiStkSwPortSTPState_Object((1,3,6,1,4,1,207,8,17,2,1,1,16),_AtiStkSwPortSTPState_Type())
atiStkSwPortSTPState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortSTPState.setStatus(_A)
_AtiStkSwPortMirroringConfig_ObjectIdentity=ObjectIdentity
atiStkSwPortMirroringConfig=_AtiStkSwPortMirroringConfig_ObjectIdentity((1,3,6,1,4,1,207,8,17,2,2))
class _AtiStkSwPortMirroringState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('l2-enabled',2)))
_AtiStkSwPortMirroringState_Type.__name__=_D
_AtiStkSwPortMirroringState_Object=MibScalar
atiStkSwPortMirroringState=_AtiStkSwPortMirroringState_Object((1,3,6,1,4,1,207,8,17,2,2,1),_AtiStkSwPortMirroringState_Type())
atiStkSwPortMirroringState.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMirroringState.setStatus(_A)
class _AtiStkSwPortMirroringSourceModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwPortMirroringSourceModuleId_Type.__name__=_D
_AtiStkSwPortMirroringSourceModuleId_Object=MibScalar
atiStkSwPortMirroringSourceModuleId=_AtiStkSwPortMirroringSourceModuleId_Object((1,3,6,1,4,1,207,8,17,2,2,2),_AtiStkSwPortMirroringSourceModuleId_Type())
atiStkSwPortMirroringSourceModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMirroringSourceModuleId.setStatus(_A)
_AtiStkSwPortMirroringSourcePortId_Type=Integer32
_AtiStkSwPortMirroringSourcePortId_Object=MibScalar
atiStkSwPortMirroringSourcePortId=_AtiStkSwPortMirroringSourcePortId_Object((1,3,6,1,4,1,207,8,17,2,2,3),_AtiStkSwPortMirroringSourcePortId_Type())
atiStkSwPortMirroringSourcePortId.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMirroringSourcePortId.setStatus(_A)
class _AtiStkSwPortMirroringDestinationModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwPortMirroringDestinationModuleId_Type.__name__=_D
_AtiStkSwPortMirroringDestinationModuleId_Object=MibScalar
atiStkSwPortMirroringDestinationModuleId=_AtiStkSwPortMirroringDestinationModuleId_Object((1,3,6,1,4,1,207,8,17,2,2,4),_AtiStkSwPortMirroringDestinationModuleId_Type())
atiStkSwPortMirroringDestinationModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMirroringDestinationModuleId.setStatus(_A)
_AtiStkSwPortMirroringDestinationPortId_Type=Integer32
_AtiStkSwPortMirroringDestinationPortId_Object=MibScalar
atiStkSwPortMirroringDestinationPortId=_AtiStkSwPortMirroringDestinationPortId_Object((1,3,6,1,4,1,207,8,17,2,2,5),_AtiStkSwPortMirroringDestinationPortId_Type())
atiStkSwPortMirroringDestinationPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMirroringDestinationPortId.setStatus(_A)
_AtiStkSwPortMirroringSourceRxList_Type=DisplayString
_AtiStkSwPortMirroringSourceRxList_Object=MibScalar
atiStkSwPortMirroringSourceRxList=_AtiStkSwPortMirroringSourceRxList_Object((1,3,6,1,4,1,207,8,17,2,2,6),_AtiStkSwPortMirroringSourceRxList_Type())
atiStkSwPortMirroringSourceRxList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMirroringSourceRxList.setStatus(_A)
_AtiStkSwPortMirroringSourceTxList_Type=DisplayString
_AtiStkSwPortMirroringSourceTxList_Object=MibScalar
atiStkSwPortMirroringSourceTxList=_AtiStkSwPortMirroringSourceTxList_Object((1,3,6,1,4,1,207,8,17,2,2,7),_AtiStkSwPortMirroringSourceTxList_Type())
atiStkSwPortMirroringSourceTxList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortMirroringSourceTxList.setStatus(_A)
_AtiStkSwPortSecurityConfig_ObjectIdentity=ObjectIdentity
atiStkSwPortSecurityConfig=_AtiStkSwPortSecurityConfig_ObjectIdentity((1,3,6,1,4,1,207,8,17,2,3))
class _AtiStkSwPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_s,1),(_t,2),(_u,3),(_v,4)))
_AtiStkSwPortSecurityMode_Type.__name__=_D
_AtiStkSwPortSecurityMode_Object=MibScalar
atiStkSwPortSecurityMode=_AtiStkSwPortSecurityMode_Object((1,3,6,1,4,1,207,8,17,2,3,1),_AtiStkSwPortSecurityMode_Type())
atiStkSwPortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortSecurityMode.setStatus(_A)
_AtiStkSwPortIntrusionDetectionTable_Object=MibTable
atiStkSwPortIntrusionDetectionTable=_AtiStkSwPortIntrusionDetectionTable_Object((1,3,6,1,4,1,207,8,17,2,4))
if mibBuilder.loadTexts:atiStkSwPortIntrusionDetectionTable.setStatus(_A)
_AtiStkSwPortIntrusionDetectionEntry_Object=MibTableRow
atiStkSwPortIntrusionDetectionEntry=_AtiStkSwPortIntrusionDetectionEntry_Object((1,3,6,1,4,1,207,8,17,2,4,1))
atiStkSwPortIntrusionDetectionEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:atiStkSwPortIntrusionDetectionEntry.setStatus(_A)
class _AtiStkSwPortIntrusionDetectionAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('do-nothing',1),('send-trap-only',2),('disable-port-and-send-trap',3)))
_AtiStkSwPortIntrusionDetectionAction_Type.__name__=_D
_AtiStkSwPortIntrusionDetectionAction_Object=MibTableColumn
atiStkSwPortIntrusionDetectionAction=_AtiStkSwPortIntrusionDetectionAction_Object((1,3,6,1,4,1,207,8,17,2,4,1,1),_AtiStkSwPortIntrusionDetectionAction_Type())
atiStkSwPortIntrusionDetectionAction.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortIntrusionDetectionAction.setStatus(_A)
_AtiStkSwPortIntrusionDetectionPortList_Type=DisplayString
_AtiStkSwPortIntrusionDetectionPortList_Object=MibTableColumn
atiStkSwPortIntrusionDetectionPortList=_AtiStkSwPortIntrusionDetectionPortList_Object((1,3,6,1,4,1,207,8,17,2,4,1,2),_AtiStkSwPortIntrusionDetectionPortList_Type())
atiStkSwPortIntrusionDetectionPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortIntrusionDetectionPortList.setStatus(_A)
_AtiStkPortSecurityConfigTable_Object=MibTable
atiStkPortSecurityConfigTable=_AtiStkPortSecurityConfigTable_Object((1,3,6,1,4,1,207,8,17,2,5))
if mibBuilder.loadTexts:atiStkPortSecurityConfigTable.setStatus(_A)
_AtiStkPortSecurityConfigEntry_Object=MibTableRow
atiStkPortSecurityConfigEntry=_AtiStkPortSecurityConfigEntry_Object((1,3,6,1,4,1,207,8,17,2,5,1))
atiStkPortSecurityConfigEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkPortSecurityConfigEntry.setStatus(_A)
class _AtiStkPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_s,1),(_t,2),(_u,3),(_v,4)))
_AtiStkPortSecurityMode_Type.__name__=_D
_AtiStkPortSecurityMode_Object=MibTableColumn
atiStkPortSecurityMode=_AtiStkPortSecurityMode_Object((1,3,6,1,4,1,207,8,17,2,5,1,1),_AtiStkPortSecurityMode_Type())
atiStkPortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkPortSecurityMode.setStatus(_A)
class _AtiStkPortSecurityThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_AtiStkPortSecurityThreshold_Type.__name__=_D
_AtiStkPortSecurityThreshold_Object=MibTableColumn
atiStkPortSecurityThreshold=_AtiStkPortSecurityThreshold_Object((1,3,6,1,4,1,207,8,17,2,5,1,2),_AtiStkPortSecurityThreshold_Type())
atiStkPortSecurityThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkPortSecurityThreshold.setStatus(_A)
class _AtiStkPortIntrusionAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discard',1),('send-trap',2),('disable-port',3)))
_AtiStkPortIntrusionAction_Type.__name__=_D
_AtiStkPortIntrusionAction_Object=MibTableColumn
atiStkPortIntrusionAction=_AtiStkPortIntrusionAction_Object((1,3,6,1,4,1,207,8,17,2,5,1,3),_AtiStkPortIntrusionAction_Type())
atiStkPortIntrusionAction.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkPortIntrusionAction.setStatus(_A)
class _AtiStkPortIntrusionActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_I,2)))
_AtiStkPortIntrusionActionStatus_Type.__name__=_D
_AtiStkPortIntrusionActionStatus_Object=MibTableColumn
atiStkPortIntrusionActionStatus=_AtiStkPortIntrusionActionStatus_Object((1,3,6,1,4,1,207,8,17,2,5,1,4),_AtiStkPortIntrusionActionStatus_Type())
atiStkPortIntrusionActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkPortIntrusionActionStatus.setStatus(_A)
_AtiStkDOSConfig_ObjectIdentity=ObjectIdentity
atiStkDOSConfig=_AtiStkDOSConfig_ObjectIdentity((1,3,6,1,4,1,207,8,17,2,6))
_AtiStkDOSConfigLANIpAddress_Type=IpAddress
_AtiStkDOSConfigLANIpAddress_Object=MibScalar
atiStkDOSConfigLANIpAddress=_AtiStkDOSConfigLANIpAddress_Object((1,3,6,1,4,1,207,8,17,2,6,1),_AtiStkDOSConfigLANIpAddress_Type())
atiStkDOSConfigLANIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkDOSConfigLANIpAddress.setStatus(_A)
_AtiStkDOSConfigLANSubnetMask_Type=IpAddress
_AtiStkDOSConfigLANSubnetMask_Object=MibScalar
atiStkDOSConfigLANSubnetMask=_AtiStkDOSConfigLANSubnetMask_Object((1,3,6,1,4,1,207,8,17,2,6,2),_AtiStkDOSConfigLANSubnetMask_Type())
atiStkDOSConfigLANSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkDOSConfigLANSubnetMask.setStatus(_A)
_AtiStkPortDOSAttackConfigTable_Object=MibTable
atiStkPortDOSAttackConfigTable=_AtiStkPortDOSAttackConfigTable_Object((1,3,6,1,4,1,207,8,17,2,6,3))
if mibBuilder.loadTexts:atiStkPortDOSAttackConfigTable.setStatus(_A)
_AtiStkPortDOSAttackConfigEntry_Object=MibTableRow
atiStkPortDOSAttackConfigEntry=_AtiStkPortDOSAttackConfigEntry_Object((1,3,6,1,4,1,207,8,17,2,6,3,1))
atiStkPortDOSAttackConfigEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_W))
if mibBuilder.loadTexts:atiStkPortDOSAttackConfigEntry.setStatus(_A)
class _AtiStkSwPortDOSAttackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('syn-flood',1),('smurf',2),('land',3),('ip-option',4),('teardrop',5),('ping-of-death',6)))
_AtiStkSwPortDOSAttackType_Type.__name__=_D
_AtiStkSwPortDOSAttackType_Object=MibTableColumn
atiStkSwPortDOSAttackType=_AtiStkSwPortDOSAttackType_Object((1,3,6,1,4,1,207,8,17,2,6,3,1,1),_AtiStkSwPortDOSAttackType_Type())
atiStkSwPortDOSAttackType.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortDOSAttackType.setStatus(_A)
class _AtiStkSwPortDOSAttackActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_I,2)))
_AtiStkSwPortDOSAttackActionStatus_Type.__name__=_D
_AtiStkSwPortDOSAttackActionStatus_Object=MibTableColumn
atiStkSwPortDOSAttackActionStatus=_AtiStkSwPortDOSAttackActionStatus_Object((1,3,6,1,4,1,207,8,17,2,6,3,1,2),_AtiStkSwPortDOSAttackActionStatus_Type())
atiStkSwPortDOSAttackActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortDOSAttackActionStatus.setStatus(_A)
_AtiStkSwPortDOSAttackMirrorPort_Type=Integer32
_AtiStkSwPortDOSAttackMirrorPort_Object=MibTableColumn
atiStkSwPortDOSAttackMirrorPort=_AtiStkSwPortDOSAttackMirrorPort_Object((1,3,6,1,4,1,207,8,17,2,6,3,1,3),_AtiStkSwPortDOSAttackMirrorPort_Type())
atiStkSwPortDOSAttackMirrorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortDOSAttackMirrorPort.setStatus(_O)
class _AtiStkSwPortDOSAttackMirrorPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_I,2)))
_AtiStkSwPortDOSAttackMirrorPortStatus_Type.__name__=_D
_AtiStkSwPortDOSAttackMirrorPortStatus_Object=MibTableColumn
atiStkSwPortDOSAttackMirrorPortStatus=_AtiStkSwPortDOSAttackMirrorPortStatus_Object((1,3,6,1,4,1,207,8,17,2,6,3,1,4),_AtiStkSwPortDOSAttackMirrorPortStatus_Type())
atiStkSwPortDOSAttackMirrorPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwPortDOSAttackMirrorPortStatus.setStatus(_A)
_AtiStkSwIntrusionAttackTable_Object=MibTable
atiStkSwIntrusionAttackTable=_AtiStkSwIntrusionAttackTable_Object((1,3,6,1,4,1,207,8,17,2,7))
if mibBuilder.loadTexts:atiStkSwIntrusionAttackTable.setStatus(_A)
_AtiStkSwIntrusionAttackEntry_Object=MibTableRow
atiStkSwIntrusionAttackEntry=_AtiStkSwIntrusionAttackEntry_Object((1,3,6,1,4,1,207,8,17,2,7,1))
atiStkSwIntrusionAttackEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkSwIntrusionAttackEntry.setStatus(_A)
_AtiStkSwIntruderAttackVlanId_Type=Integer32
_AtiStkSwIntruderAttackVlanId_Object=MibTableColumn
atiStkSwIntruderAttackVlanId=_AtiStkSwIntruderAttackVlanId_Object((1,3,6,1,4,1,207,8,17,2,7,1,1),_AtiStkSwIntruderAttackVlanId_Type())
atiStkSwIntruderAttackVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwIntruderAttackVlanId.setStatus(_A)
_AtiStkSwIntruderAttackMacAddr_Type=MacAddress
_AtiStkSwIntruderAttackMacAddr_Object=MibTableColumn
atiStkSwIntruderAttackMacAddr=_AtiStkSwIntruderAttackMacAddr_Object((1,3,6,1,4,1,207,8,17,2,7,1,2),_AtiStkSwIntruderAttackMacAddr_Type())
atiStkSwIntruderAttackMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwIntruderAttackMacAddr.setStatus(_A)
_AtiStkSwPortStormDetectCurrentTable_Object=MibTable
atiStkSwPortStormDetectCurrentTable=_AtiStkSwPortStormDetectCurrentTable_Object((1,3,6,1,4,1,207,8,17,2,8))
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentTable.setStatus(_A)
_AtiStkSwPortStormDetectCurrentEntry_Object=MibTableRow
atiStkSwPortStormDetectCurrentEntry=_AtiStkSwPortStormDetectCurrentEntry_Object((1,3,6,1,4,1,207,8,17,2,8,1))
atiStkSwPortStormDetectCurrentEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentEntry.setStatus(_A)
class _AtiStkSwPortStormDetectCurrentHighStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_S,2),(_Y,3),(_R,4)))
_AtiStkSwPortStormDetectCurrentHighStatus_Type.__name__=_D
_AtiStkSwPortStormDetectCurrentHighStatus_Object=MibTableColumn
atiStkSwPortStormDetectCurrentHighStatus=_AtiStkSwPortStormDetectCurrentHighStatus_Object((1,3,6,1,4,1,207,8,17,2,8,1,1),_AtiStkSwPortStormDetectCurrentHighStatus_Type())
atiStkSwPortStormDetectCurrentHighStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentHighStatus.setStatus(_A)
class _AtiStkSwPortStormDetectCurrentHighAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_P,2),(_Z,3),(_a,4),(_b,5)))
_AtiStkSwPortStormDetectCurrentHighAction_Type.__name__=_D
_AtiStkSwPortStormDetectCurrentHighAction_Object=MibTableColumn
atiStkSwPortStormDetectCurrentHighAction=_AtiStkSwPortStormDetectCurrentHighAction_Object((1,3,6,1,4,1,207,8,17,2,8,1,2),_AtiStkSwPortStormDetectCurrentHighAction_Type())
atiStkSwPortStormDetectCurrentHighAction.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentHighAction.setStatus(_A)
_AtiStkSwPortStormDetectCurrentHighExpiry_Type=Integer32
_AtiStkSwPortStormDetectCurrentHighExpiry_Object=MibTableColumn
atiStkSwPortStormDetectCurrentHighExpiry=_AtiStkSwPortStormDetectCurrentHighExpiry_Object((1,3,6,1,4,1,207,8,17,2,8,1,3),_AtiStkSwPortStormDetectCurrentHighExpiry_Type())
atiStkSwPortStormDetectCurrentHighExpiry.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentHighExpiry.setStatus(_A)
class _AtiStkSwPortStormDetectCurrentLowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_S,2),(_Y,3),(_R,4)))
_AtiStkSwPortStormDetectCurrentLowStatus_Type.__name__=_D
_AtiStkSwPortStormDetectCurrentLowStatus_Object=MibTableColumn
atiStkSwPortStormDetectCurrentLowStatus=_AtiStkSwPortStormDetectCurrentLowStatus_Object((1,3,6,1,4,1,207,8,17,2,8,1,4),_AtiStkSwPortStormDetectCurrentLowStatus_Type())
atiStkSwPortStormDetectCurrentLowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentLowStatus.setStatus(_A)
class _AtiStkSwPortStormDetectCurrentLowAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_P,2),(_Z,3),(_a,4),(_b,5)))
_AtiStkSwPortStormDetectCurrentLowAction_Type.__name__=_D
_AtiStkSwPortStormDetectCurrentLowAction_Object=MibTableColumn
atiStkSwPortStormDetectCurrentLowAction=_AtiStkSwPortStormDetectCurrentLowAction_Object((1,3,6,1,4,1,207,8,17,2,8,1,5),_AtiStkSwPortStormDetectCurrentLowAction_Type())
atiStkSwPortStormDetectCurrentLowAction.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentLowAction.setStatus(_A)
_AtiStkSwPortStormDetectCurrentLowExpiry_Type=Integer32
_AtiStkSwPortStormDetectCurrentLowExpiry_Object=MibTableColumn
atiStkSwPortStormDetectCurrentLowExpiry=_AtiStkSwPortStormDetectCurrentLowExpiry_Object((1,3,6,1,4,1,207,8,17,2,8,1,6),_AtiStkSwPortStormDetectCurrentLowExpiry_Type())
atiStkSwPortStormDetectCurrentLowExpiry.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortStormDetectCurrentLowExpiry.setStatus(_A)
_AtiStkSwPortLoopDetectCurrentTable_Object=MibTable
atiStkSwPortLoopDetectCurrentTable=_AtiStkSwPortLoopDetectCurrentTable_Object((1,3,6,1,4,1,207,8,17,2,9))
if mibBuilder.loadTexts:atiStkSwPortLoopDetectCurrentTable.setStatus(_A)
_AtiStkSwPortLoopDetectCurrentEntry_Object=MibTableRow
atiStkSwPortLoopDetectCurrentEntry=_AtiStkSwPortLoopDetectCurrentEntry_Object((1,3,6,1,4,1,207,8,17,2,9,1))
atiStkSwPortLoopDetectCurrentEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkSwPortLoopDetectCurrentEntry.setStatus(_A)
class _AtiStkSwPortLoopDetectCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_S,2),(_Y,3),(_R,4)))
_AtiStkSwPortLoopDetectCurrentStatus_Type.__name__=_D
_AtiStkSwPortLoopDetectCurrentStatus_Object=MibTableColumn
atiStkSwPortLoopDetectCurrentStatus=_AtiStkSwPortLoopDetectCurrentStatus_Object((1,3,6,1,4,1,207,8,17,2,9,1,1),_AtiStkSwPortLoopDetectCurrentStatus_Type())
atiStkSwPortLoopDetectCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortLoopDetectCurrentStatus.setStatus(_A)
class _AtiStkSwPortLoopDetectCurrentAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_P,2),(_Z,3),(_a,4),(_b,5)))
_AtiStkSwPortLoopDetectCurrentAction_Type.__name__=_D
_AtiStkSwPortLoopDetectCurrentAction_Object=MibTableColumn
atiStkSwPortLoopDetectCurrentAction=_AtiStkSwPortLoopDetectCurrentAction_Object((1,3,6,1,4,1,207,8,17,2,9,1,2),_AtiStkSwPortLoopDetectCurrentAction_Type())
atiStkSwPortLoopDetectCurrentAction.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortLoopDetectCurrentAction.setStatus(_A)
_AtiStkSwPortLoopDetectCurrentExpiry_Type=Integer32
_AtiStkSwPortLoopDetectCurrentExpiry_Object=MibTableColumn
atiStkSwPortLoopDetectCurrentExpiry=_AtiStkSwPortLoopDetectCurrentExpiry_Object((1,3,6,1,4,1,207,8,17,2,9,1,3),_AtiStkSwPortLoopDetectCurrentExpiry_Type())
atiStkSwPortLoopDetectCurrentExpiry.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortLoopDetectCurrentExpiry.setStatus(_A)
_AtiStkSwPortLoopDetectCurrentVlanId_Type=Integer32
_AtiStkSwPortLoopDetectCurrentVlanId_Object=MibTableColumn
atiStkSwPortLoopDetectCurrentVlanId=_AtiStkSwPortLoopDetectCurrentVlanId_Object((1,3,6,1,4,1,207,8,17,2,9,1,4),_AtiStkSwPortLoopDetectCurrentVlanId_Type())
atiStkSwPortLoopDetectCurrentVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortLoopDetectCurrentVlanId.setStatus(_A)
_AtiStkSwVlanGroup_ObjectIdentity=ObjectIdentity
atiStkSwVlanGroup=_AtiStkSwVlanGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,3))
_AtiStkSwVlanConfigTable_Object=MibTable
atiStkSwVlanConfigTable=_AtiStkSwVlanConfigTable_Object((1,3,6,1,4,1,207,8,17,3,1))
if mibBuilder.loadTexts:atiStkSwVlanConfigTable.setStatus(_A)
_AtiStkSwVlanConfigEntry_Object=MibTableRow
atiStkSwVlanConfigEntry=_AtiStkSwVlanConfigEntry_Object((1,3,6,1,4,1,207,8,17,3,1,1))
atiStkSwVlanConfigEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:atiStkSwVlanConfigEntry.setStatus(_A)
class _AtiStkSwVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AtiStkSwVlanId_Type.__name__=_D
_AtiStkSwVlanId_Object=MibTableColumn
atiStkSwVlanId=_AtiStkSwVlanId_Object((1,3,6,1,4,1,207,8,17,3,1,1,1),_AtiStkSwVlanId_Type())
atiStkSwVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwVlanId.setStatus(_A)
class _AtiStkSwVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_AtiStkSwVlanName_Type.__name__=_F
_AtiStkSwVlanName_Object=MibTableColumn
atiStkSwVlanName=_AtiStkSwVlanName_Object((1,3,6,1,4,1,207,8,17,3,1,1,2),_AtiStkSwVlanName_Type())
atiStkSwVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanName.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule1_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule1_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule1=_AtiStkSwVlanTaggedPortListModule1_Object((1,3,6,1,4,1,207,8,17,3,1,1,3),_AtiStkSwVlanTaggedPortListModule1_Type())
atiStkSwVlanTaggedPortListModule1.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule1.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule1_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule1_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule1=_AtiStkSwVlanUntaggedPortListModule1_Object((1,3,6,1,4,1,207,8,17,3,1,1,4),_AtiStkSwVlanUntaggedPortListModule1_Type())
atiStkSwVlanUntaggedPortListModule1.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule1.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule2_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule2_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule2=_AtiStkSwVlanTaggedPortListModule2_Object((1,3,6,1,4,1,207,8,17,3,1,1,5),_AtiStkSwVlanTaggedPortListModule2_Type())
atiStkSwVlanTaggedPortListModule2.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule2.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule2_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule2_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule2=_AtiStkSwVlanUntaggedPortListModule2_Object((1,3,6,1,4,1,207,8,17,3,1,1,6),_AtiStkSwVlanUntaggedPortListModule2_Type())
atiStkSwVlanUntaggedPortListModule2.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule2.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule3_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule3_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule3=_AtiStkSwVlanTaggedPortListModule3_Object((1,3,6,1,4,1,207,8,17,3,1,1,7),_AtiStkSwVlanTaggedPortListModule3_Type())
atiStkSwVlanTaggedPortListModule3.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule3.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule3_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule3_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule3=_AtiStkSwVlanUntaggedPortListModule3_Object((1,3,6,1,4,1,207,8,17,3,1,1,8),_AtiStkSwVlanUntaggedPortListModule3_Type())
atiStkSwVlanUntaggedPortListModule3.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule3.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule4_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule4_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule4=_AtiStkSwVlanTaggedPortListModule4_Object((1,3,6,1,4,1,207,8,17,3,1,1,9),_AtiStkSwVlanTaggedPortListModule4_Type())
atiStkSwVlanTaggedPortListModule4.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule4.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule4_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule4_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule4=_AtiStkSwVlanUntaggedPortListModule4_Object((1,3,6,1,4,1,207,8,17,3,1,1,10),_AtiStkSwVlanUntaggedPortListModule4_Type())
atiStkSwVlanUntaggedPortListModule4.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule4.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule5_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule5_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule5=_AtiStkSwVlanTaggedPortListModule5_Object((1,3,6,1,4,1,207,8,17,3,1,1,11),_AtiStkSwVlanTaggedPortListModule5_Type())
atiStkSwVlanTaggedPortListModule5.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule5.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule5_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule5_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule5=_AtiStkSwVlanUntaggedPortListModule5_Object((1,3,6,1,4,1,207,8,17,3,1,1,12),_AtiStkSwVlanUntaggedPortListModule5_Type())
atiStkSwVlanUntaggedPortListModule5.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule5.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule6_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule6_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule6=_AtiStkSwVlanTaggedPortListModule6_Object((1,3,6,1,4,1,207,8,17,3,1,1,13),_AtiStkSwVlanTaggedPortListModule6_Type())
atiStkSwVlanTaggedPortListModule6.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule6.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule6_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule6_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule6=_AtiStkSwVlanUntaggedPortListModule6_Object((1,3,6,1,4,1,207,8,17,3,1,1,14),_AtiStkSwVlanUntaggedPortListModule6_Type())
atiStkSwVlanUntaggedPortListModule6.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule6.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule7_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule7_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule7=_AtiStkSwVlanTaggedPortListModule7_Object((1,3,6,1,4,1,207,8,17,3,1,1,15),_AtiStkSwVlanTaggedPortListModule7_Type())
atiStkSwVlanTaggedPortListModule7.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule7.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule7_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule7_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule7=_AtiStkSwVlanUntaggedPortListModule7_Object((1,3,6,1,4,1,207,8,17,3,1,1,16),_AtiStkSwVlanUntaggedPortListModule7_Type())
atiStkSwVlanUntaggedPortListModule7.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule7.setStatus(_A)
_AtiStkSwVlanTaggedPortListModule8_Type=DisplayString
_AtiStkSwVlanTaggedPortListModule8_Object=MibTableColumn
atiStkSwVlanTaggedPortListModule8=_AtiStkSwVlanTaggedPortListModule8_Object((1,3,6,1,4,1,207,8,17,3,1,1,17),_AtiStkSwVlanTaggedPortListModule8_Type())
atiStkSwVlanTaggedPortListModule8.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanTaggedPortListModule8.setStatus(_A)
_AtiStkSwVlanUntaggedPortListModule8_Type=DisplayString
_AtiStkSwVlanUntaggedPortListModule8_Object=MibTableColumn
atiStkSwVlanUntaggedPortListModule8=_AtiStkSwVlanUntaggedPortListModule8_Object((1,3,6,1,4,1,207,8,17,3,1,1,18),_AtiStkSwVlanUntaggedPortListModule8_Type())
atiStkSwVlanUntaggedPortListModule8.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUntaggedPortListModule8.setStatus(_A)
_AtiStkSwVlanConfigEntryStatus_Type=RowStatus
_AtiStkSwVlanConfigEntryStatus_Object=MibTableColumn
atiStkSwVlanConfigEntryStatus=_AtiStkSwVlanConfigEntryStatus_Object((1,3,6,1,4,1,207,8,17,3,1,1,19),_AtiStkSwVlanConfigEntryStatus_Type())
atiStkSwVlanConfigEntryStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:atiStkSwVlanConfigEntryStatus.setStatus(_A)
_AtiStkSwVlanActualUntaggedPortListModule1_Type=DisplayString
_AtiStkSwVlanActualUntaggedPortListModule1_Object=MibTableColumn
atiStkSwVlanActualUntaggedPortListModule1=_AtiStkSwVlanActualUntaggedPortListModule1_Object((1,3,6,1,4,1,207,8,17,3,1,1,20),_AtiStkSwVlanActualUntaggedPortListModule1_Type())
atiStkSwVlanActualUntaggedPortListModule1.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwVlanActualUntaggedPortListModule1.setStatus(_A)
_AtiStkSwPort2VlanTable_Object=MibTable
atiStkSwPort2VlanTable=_AtiStkSwPort2VlanTable_Object((1,3,6,1,4,1,207,8,17,3,2))
if mibBuilder.loadTexts:atiStkSwPort2VlanTable.setStatus(_A)
_AtiStkSwPort2VlanEntry_Object=MibTableRow
atiStkSwPort2VlanEntry=_AtiStkSwPort2VlanEntry_Object((1,3,6,1,4,1,207,8,17,3,2,1))
atiStkSwPort2VlanEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkSwPort2VlanEntry.setStatus(_A)
_AtiStkSwPortVlanId_Type=Integer32
_AtiStkSwPortVlanId_Object=MibTableColumn
atiStkSwPortVlanId=_AtiStkSwPortVlanId_Object((1,3,6,1,4,1,207,8,17,3,2,1,1),_AtiStkSwPortVlanId_Type())
atiStkSwPortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortVlanId.setStatus(_A)
class _AtiStkSwPortVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_AtiStkSwPortVlanName_Type.__name__=_F
_AtiStkSwPortVlanName_Object=MibTableColumn
atiStkSwPortVlanName=_AtiStkSwPortVlanName_Object((1,3,6,1,4,1,207,8,17,3,2,1,2),_AtiStkSwPortVlanName_Type())
atiStkSwPortVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwPortVlanName.setStatus(_A)
_AtiStkSwMacAddr2VlanTable_Object=MibTable
atiStkSwMacAddr2VlanTable=_AtiStkSwMacAddr2VlanTable_Object((1,3,6,1,4,1,207,8,17,3,3))
if mibBuilder.loadTexts:atiStkSwMacAddr2VlanTable.setStatus(_A)
_AtiStkSwMacAddr2VlanEntry_Object=MibTableRow
atiStkSwMacAddr2VlanEntry=_AtiStkSwMacAddr2VlanEntry_Object((1,3,6,1,4,1,207,8,17,3,3,1))
atiStkSwMacAddr2VlanEntry.setIndexNames((0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:atiStkSwMacAddr2VlanEntry.setStatus(_A)
_AtiStkSwMacAddress_Type=MacAddress
_AtiStkSwMacAddress_Object=MibTableColumn
atiStkSwMacAddress=_AtiStkSwMacAddress_Object((1,3,6,1,4,1,207,8,17,3,3,1,1),_AtiStkSwMacAddress_Type())
atiStkSwMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMacAddress.setStatus(_A)
class _AtiStkSwMacAddrVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AtiStkSwMacAddrVlanId_Type.__name__=_D
_AtiStkSwMacAddrVlanId_Object=MibTableColumn
atiStkSwMacAddrVlanId=_AtiStkSwMacAddrVlanId_Object((1,3,6,1,4,1,207,8,17,3,3,1,2),_AtiStkSwMacAddrVlanId_Type())
atiStkSwMacAddrVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMacAddrVlanId.setStatus(_A)
class _AtiStkSwMacAddrVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_AtiStkSwMacAddrVlanName_Type.__name__=_F
_AtiStkSwMacAddrVlanName_Object=MibTableColumn
atiStkSwMacAddrVlanName=_AtiStkSwMacAddrVlanName_Object((1,3,6,1,4,1,207,8,17,3,3,1,3),_AtiStkSwMacAddrVlanName_Type())
atiStkSwMacAddrVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMacAddrVlanName.setStatus(_A)
class _AtiStkSwMacAddrModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwMacAddrModuleId_Type.__name__=_D
_AtiStkSwMacAddrModuleId_Object=MibTableColumn
atiStkSwMacAddrModuleId=_AtiStkSwMacAddrModuleId_Object((1,3,6,1,4,1,207,8,17,3,3,1,4),_AtiStkSwMacAddrModuleId_Type())
atiStkSwMacAddrModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMacAddrModuleId.setStatus(_A)
_AtiStkSwMacAddrPortId_Type=Integer32
_AtiStkSwMacAddrPortId_Object=MibTableColumn
atiStkSwMacAddrPortId=_AtiStkSwMacAddrPortId_Object((1,3,6,1,4,1,207,8,17,3,3,1,5),_AtiStkSwMacAddrPortId_Type())
atiStkSwMacAddrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMacAddrPortId.setStatus(_A)
class _AtiStkSwMacAddrPortList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwMacAddrPortList_Type.__name__=_F
_AtiStkSwMacAddrPortList_Object=MibTableColumn
atiStkSwMacAddrPortList=_AtiStkSwMacAddrPortList_Object((1,3,6,1,4,1,207,8,17,3,3,1,6),_AtiStkSwMacAddrPortList_Type())
atiStkSwMacAddrPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwMacAddrPortList.setStatus(_A)
class _AtiStkSwVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user-configured',1),('multiple',2),('multiple-802-1Q',3)))
_AtiStkSwVlanMode_Type.__name__=_D
_AtiStkSwVlanMode_Object=MibScalar
atiStkSwVlanMode=_AtiStkSwVlanMode_Object((1,3,6,1,4,1,207,8,17,3,4),_AtiStkSwVlanMode_Type())
atiStkSwVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanMode.setStatus(_A)
_AtiStkSwVlanUplinkVlanPort_Type=Integer32
_AtiStkSwVlanUplinkVlanPort_Object=MibScalar
atiStkSwVlanUplinkVlanPort=_AtiStkSwVlanUplinkVlanPort_Object((1,3,6,1,4,1,207,8,17,3,5),_AtiStkSwVlanUplinkVlanPort_Type())
atiStkSwVlanUplinkVlanPort.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwVlanUplinkVlanPort.setStatus(_A)
_AtiStkSwGVRPConfig_ObjectIdentity=ObjectIdentity
atiStkSwGVRPConfig=_AtiStkSwGVRPConfig_ObjectIdentity((1,3,6,1,4,1,207,8,17,3,6))
class _AtiStkSwGVRPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_I,2)))
_AtiStkSwGVRPStatus_Type.__name__=_D
_AtiStkSwGVRPStatus_Object=MibScalar
atiStkSwGVRPStatus=_AtiStkSwGVRPStatus_Object((1,3,6,1,4,1,207,8,17,3,6,1),_AtiStkSwGVRPStatus_Type())
atiStkSwGVRPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwGVRPStatus.setStatus(_A)
class _AtiStkSwGVRPGIPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_I,2)))
_AtiStkSwGVRPGIPStatus_Type.__name__=_D
_AtiStkSwGVRPGIPStatus_Object=MibScalar
atiStkSwGVRPGIPStatus=_AtiStkSwGVRPGIPStatus_Object((1,3,6,1,4,1,207,8,17,3,6,2),_AtiStkSwGVRPGIPStatus_Type())
atiStkSwGVRPGIPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwGVRPGIPStatus.setStatus(_A)
class _AtiStkSwGVRPJoinTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60))
_AtiStkSwGVRPJoinTimer_Type.__name__=_D
_AtiStkSwGVRPJoinTimer_Object=MibScalar
atiStkSwGVRPJoinTimer=_AtiStkSwGVRPJoinTimer_Object((1,3,6,1,4,1,207,8,17,3,6,3),_AtiStkSwGVRPJoinTimer_Type())
atiStkSwGVRPJoinTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwGVRPJoinTimer.setStatus(_A)
class _AtiStkSwGVRPLeaveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,180))
_AtiStkSwGVRPLeaveTimer_Type.__name__=_D
_AtiStkSwGVRPLeaveTimer_Object=MibScalar
atiStkSwGVRPLeaveTimer=_AtiStkSwGVRPLeaveTimer_Object((1,3,6,1,4,1,207,8,17,3,6,4),_AtiStkSwGVRPLeaveTimer_Type())
atiStkSwGVRPLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwGVRPLeaveTimer.setStatus(_A)
class _AtiStkSwGVRPLeaveAllTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,3000))
_AtiStkSwGVRPLeaveAllTimer_Type.__name__=_D
_AtiStkSwGVRPLeaveAllTimer_Object=MibScalar
atiStkSwGVRPLeaveAllTimer=_AtiStkSwGVRPLeaveAllTimer_Object((1,3,6,1,4,1,207,8,17,3,6,5),_AtiStkSwGVRPLeaveAllTimer_Type())
atiStkSwGVRPLeaveAllTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwGVRPLeaveAllTimer.setStatus(_A)
_AtiStkSwGVRPPortConfigTable_Object=MibTable
atiStkSwGVRPPortConfigTable=_AtiStkSwGVRPPortConfigTable_Object((1,3,6,1,4,1,207,8,17,3,7))
if mibBuilder.loadTexts:atiStkSwGVRPPortConfigTable.setStatus(_A)
_AtiStkSwGVRPPortConfigEntry_Object=MibTableRow
atiStkSwGVRPPortConfigEntry=_AtiStkSwGVRPPortConfigEntry_Object((1,3,6,1,4,1,207,8,17,3,7,1))
atiStkSwGVRPPortConfigEntry.setIndexNames((0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:atiStkSwGVRPPortConfigEntry.setStatus(_A)
class _AtiStkSwGVRPPortConfigModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwGVRPPortConfigModuleId_Type.__name__=_D
_AtiStkSwGVRPPortConfigModuleId_Object=MibTableColumn
atiStkSwGVRPPortConfigModuleId=_AtiStkSwGVRPPortConfigModuleId_Object((1,3,6,1,4,1,207,8,17,3,7,1,1),_AtiStkSwGVRPPortConfigModuleId_Type())
atiStkSwGVRPPortConfigModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPPortConfigModuleId.setStatus(_A)
class _AtiStkSwGVRPPortConfigPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_AtiStkSwGVRPPortConfigPortId_Type.__name__=_D
_AtiStkSwGVRPPortConfigPortId_Object=MibTableColumn
atiStkSwGVRPPortConfigPortId=_AtiStkSwGVRPPortConfigPortId_Object((1,3,6,1,4,1,207,8,17,3,7,1,2),_AtiStkSwGVRPPortConfigPortId_Type())
atiStkSwGVRPPortConfigPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPPortConfigPortId.setStatus(_A)
class _AtiStkSwGVRPPortConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_S,2)))
_AtiStkSwGVRPPortConfigStatus_Type.__name__=_D
_AtiStkSwGVRPPortConfigStatus_Object=MibTableColumn
atiStkSwGVRPPortConfigStatus=_AtiStkSwGVRPPortConfigStatus_Object((1,3,6,1,4,1,207,8,17,3,7,1,3),_AtiStkSwGVRPPortConfigStatus_Type())
atiStkSwGVRPPortConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwGVRPPortConfigStatus.setStatus(_A)
_AtiStkSwGVRPCountersTable_Object=MibTable
atiStkSwGVRPCountersTable=_AtiStkSwGVRPCountersTable_Object((1,3,6,1,4,1,207,8,17,3,8))
if mibBuilder.loadTexts:atiStkSwGVRPCountersTable.setStatus(_A)
_AtiStkSwGVRPCountersEntry_Object=MibTableRow
atiStkSwGVRPCountersEntry=_AtiStkSwGVRPCountersEntry_Object((1,3,6,1,4,1,207,8,17,3,8,1))
atiStkSwGVRPCountersEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:atiStkSwGVRPCountersEntry.setStatus(_A)
class _AtiStkSwGVRPCountersModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwGVRPCountersModuleId_Type.__name__=_D
_AtiStkSwGVRPCountersModuleId_Object=MibTableColumn
atiStkSwGVRPCountersModuleId=_AtiStkSwGVRPCountersModuleId_Object((1,3,6,1,4,1,207,8,17,3,8,1,1),_AtiStkSwGVRPCountersModuleId_Type())
atiStkSwGVRPCountersModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersModuleId.setStatus(_A)
_AtiStkSwGVRPCountersGARPRxPkt_Type=Counter32
_AtiStkSwGVRPCountersGARPRxPkt_Object=MibTableColumn
atiStkSwGVRPCountersGARPRxPkt=_AtiStkSwGVRPCountersGARPRxPkt_Object((1,3,6,1,4,1,207,8,17,3,8,1,2),_AtiStkSwGVRPCountersGARPRxPkt_Type())
atiStkSwGVRPCountersGARPRxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersGARPRxPkt.setStatus(_A)
_AtiStkSwGVRPCountersInvalidGARPRxPkt_Type=Counter32
_AtiStkSwGVRPCountersInvalidGARPRxPkt_Object=MibTableColumn
atiStkSwGVRPCountersInvalidGARPRxPkt=_AtiStkSwGVRPCountersInvalidGARPRxPkt_Object((1,3,6,1,4,1,207,8,17,3,8,1,3),_AtiStkSwGVRPCountersInvalidGARPRxPkt_Type())
atiStkSwGVRPCountersInvalidGARPRxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersInvalidGARPRxPkt.setStatus(_A)
_AtiStkSwGVRPCountersGARPTxPkt_Type=Counter32
_AtiStkSwGVRPCountersGARPTxPkt_Object=MibTableColumn
atiStkSwGVRPCountersGARPTxPkt=_AtiStkSwGVRPCountersGARPTxPkt_Object((1,3,6,1,4,1,207,8,17,3,8,1,4),_AtiStkSwGVRPCountersGARPTxPkt_Type())
atiStkSwGVRPCountersGARPTxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersGARPTxPkt.setStatus(_A)
_AtiStkSwGVRPCountersGARPTxDisabled_Type=Counter32
_AtiStkSwGVRPCountersGARPTxDisabled_Object=MibTableColumn
atiStkSwGVRPCountersGARPTxDisabled=_AtiStkSwGVRPCountersGARPTxDisabled_Object((1,3,6,1,4,1,207,8,17,3,8,1,5),_AtiStkSwGVRPCountersGARPTxDisabled_Type())
atiStkSwGVRPCountersGARPTxDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersGARPTxDisabled.setStatus(_A)
_AtiStkSwGVRPCountersPortNotSending_Type=Counter32
_AtiStkSwGVRPCountersPortNotSending_Object=MibTableColumn
atiStkSwGVRPCountersPortNotSending=_AtiStkSwGVRPCountersPortNotSending_Object((1,3,6,1,4,1,207,8,17,3,8,1,6),_AtiStkSwGVRPCountersPortNotSending_Type())
atiStkSwGVRPCountersPortNotSending.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersPortNotSending.setStatus(_A)
_AtiStkSwGVRPCountersGARPDisabled_Type=Counter32
_AtiStkSwGVRPCountersGARPDisabled_Object=MibTableColumn
atiStkSwGVRPCountersGARPDisabled=_AtiStkSwGVRPCountersGARPDisabled_Object((1,3,6,1,4,1,207,8,17,3,8,1,7),_AtiStkSwGVRPCountersGARPDisabled_Type())
atiStkSwGVRPCountersGARPDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersGARPDisabled.setStatus(_A)
_AtiStkSwGVRPCountersPortNotListening_Type=Counter32
_AtiStkSwGVRPCountersPortNotListening_Object=MibTableColumn
atiStkSwGVRPCountersPortNotListening=_AtiStkSwGVRPCountersPortNotListening_Object((1,3,6,1,4,1,207,8,17,3,8,1,8),_AtiStkSwGVRPCountersPortNotListening_Type())
atiStkSwGVRPCountersPortNotListening.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersPortNotListening.setStatus(_A)
_AtiStkSwGVRPCountersInvalidPort_Type=Counter32
_AtiStkSwGVRPCountersInvalidPort_Object=MibTableColumn
atiStkSwGVRPCountersInvalidPort=_AtiStkSwGVRPCountersInvalidPort_Object((1,3,6,1,4,1,207,8,17,3,8,1,9),_AtiStkSwGVRPCountersInvalidPort_Type())
atiStkSwGVRPCountersInvalidPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersInvalidPort.setStatus(_A)
_AtiStkSwGVRPCountersInvalidProtocol_Type=Counter32
_AtiStkSwGVRPCountersInvalidProtocol_Object=MibTableColumn
atiStkSwGVRPCountersInvalidProtocol=_AtiStkSwGVRPCountersInvalidProtocol_Object((1,3,6,1,4,1,207,8,17,3,8,1,10),_AtiStkSwGVRPCountersInvalidProtocol_Type())
atiStkSwGVRPCountersInvalidProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersInvalidProtocol.setStatus(_A)
_AtiStkSwGVRPCountersInvalidFormat_Type=Counter32
_AtiStkSwGVRPCountersInvalidFormat_Object=MibTableColumn
atiStkSwGVRPCountersInvalidFormat=_AtiStkSwGVRPCountersInvalidFormat_Object((1,3,6,1,4,1,207,8,17,3,8,1,11),_AtiStkSwGVRPCountersInvalidFormat_Type())
atiStkSwGVRPCountersInvalidFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersInvalidFormat.setStatus(_A)
_AtiStkSwGVRPCountersDatabaseFull_Type=Counter32
_AtiStkSwGVRPCountersDatabaseFull_Object=MibTableColumn
atiStkSwGVRPCountersDatabaseFull=_AtiStkSwGVRPCountersDatabaseFull_Object((1,3,6,1,4,1,207,8,17,3,8,1,12),_AtiStkSwGVRPCountersDatabaseFull_Type())
atiStkSwGVRPCountersDatabaseFull.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersDatabaseFull.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgLeaveAll_Type=Counter32
_AtiStkSwGVRPCountersRxMsgLeaveAll_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgLeaveAll=_AtiStkSwGVRPCountersRxMsgLeaveAll_Object((1,3,6,1,4,1,207,8,17,3,8,1,13),_AtiStkSwGVRPCountersRxMsgLeaveAll_Type())
atiStkSwGVRPCountersRxMsgLeaveAll.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgLeaveAll.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgJoinEmpty_Type=Counter32
_AtiStkSwGVRPCountersRxMsgJoinEmpty_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgJoinEmpty=_AtiStkSwGVRPCountersRxMsgJoinEmpty_Object((1,3,6,1,4,1,207,8,17,3,8,1,14),_AtiStkSwGVRPCountersRxMsgJoinEmpty_Type())
atiStkSwGVRPCountersRxMsgJoinEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgJoinEmpty.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgJoinIn_Type=Counter32
_AtiStkSwGVRPCountersRxMsgJoinIn_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgJoinIn=_AtiStkSwGVRPCountersRxMsgJoinIn_Object((1,3,6,1,4,1,207,8,17,3,8,1,15),_AtiStkSwGVRPCountersRxMsgJoinIn_Type())
atiStkSwGVRPCountersRxMsgJoinIn.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgJoinIn.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgLeaveEmpty_Type=Counter32
_AtiStkSwGVRPCountersRxMsgLeaveEmpty_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgLeaveEmpty=_AtiStkSwGVRPCountersRxMsgLeaveEmpty_Object((1,3,6,1,4,1,207,8,17,3,8,1,16),_AtiStkSwGVRPCountersRxMsgLeaveEmpty_Type())
atiStkSwGVRPCountersRxMsgLeaveEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgLeaveEmpty.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgLeaveIn_Type=Counter32
_AtiStkSwGVRPCountersRxMsgLeaveIn_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgLeaveIn=_AtiStkSwGVRPCountersRxMsgLeaveIn_Object((1,3,6,1,4,1,207,8,17,3,8,1,17),_AtiStkSwGVRPCountersRxMsgLeaveIn_Type())
atiStkSwGVRPCountersRxMsgLeaveIn.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgLeaveIn.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgEmpty_Type=Counter32
_AtiStkSwGVRPCountersRxMsgEmpty_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgEmpty=_AtiStkSwGVRPCountersRxMsgEmpty_Object((1,3,6,1,4,1,207,8,17,3,8,1,18),_AtiStkSwGVRPCountersRxMsgEmpty_Type())
atiStkSwGVRPCountersRxMsgEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgEmpty.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgBadMsg_Type=Counter32
_AtiStkSwGVRPCountersRxMsgBadMsg_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgBadMsg=_AtiStkSwGVRPCountersRxMsgBadMsg_Object((1,3,6,1,4,1,207,8,17,3,8,1,19),_AtiStkSwGVRPCountersRxMsgBadMsg_Type())
atiStkSwGVRPCountersRxMsgBadMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgBadMsg.setStatus(_A)
_AtiStkSwGVRPCountersRxMsgBadAttribute_Type=Counter32
_AtiStkSwGVRPCountersRxMsgBadAttribute_Object=MibTableColumn
atiStkSwGVRPCountersRxMsgBadAttribute=_AtiStkSwGVRPCountersRxMsgBadAttribute_Object((1,3,6,1,4,1,207,8,17,3,8,1,20),_AtiStkSwGVRPCountersRxMsgBadAttribute_Type())
atiStkSwGVRPCountersRxMsgBadAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersRxMsgBadAttribute.setStatus(_A)
_AtiStkSwGVRPCountersTxMsgLeaveAll_Type=Counter32
_AtiStkSwGVRPCountersTxMsgLeaveAll_Object=MibTableColumn
atiStkSwGVRPCountersTxMsgLeaveAll=_AtiStkSwGVRPCountersTxMsgLeaveAll_Object((1,3,6,1,4,1,207,8,17,3,8,1,21),_AtiStkSwGVRPCountersTxMsgLeaveAll_Type())
atiStkSwGVRPCountersTxMsgLeaveAll.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersTxMsgLeaveAll.setStatus(_A)
_AtiStkSwGVRPCountersTxMsgJoinEmpty_Type=Counter32
_AtiStkSwGVRPCountersTxMsgJoinEmpty_Object=MibTableColumn
atiStkSwGVRPCountersTxMsgJoinEmpty=_AtiStkSwGVRPCountersTxMsgJoinEmpty_Object((1,3,6,1,4,1,207,8,17,3,8,1,22),_AtiStkSwGVRPCountersTxMsgJoinEmpty_Type())
atiStkSwGVRPCountersTxMsgJoinEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersTxMsgJoinEmpty.setStatus(_A)
_AtiStkSwGVRPCountersTxMsgJoinIn_Type=Counter32
_AtiStkSwGVRPCountersTxMsgJoinIn_Object=MibTableColumn
atiStkSwGVRPCountersTxMsgJoinIn=_AtiStkSwGVRPCountersTxMsgJoinIn_Object((1,3,6,1,4,1,207,8,17,3,8,1,23),_AtiStkSwGVRPCountersTxMsgJoinIn_Type())
atiStkSwGVRPCountersTxMsgJoinIn.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersTxMsgJoinIn.setStatus(_A)
_AtiStkSwGVRPCountersTxMsgLeaveEmpty_Type=Counter32
_AtiStkSwGVRPCountersTxMsgLeaveEmpty_Object=MibTableColumn
atiStkSwGVRPCountersTxMsgLeaveEmpty=_AtiStkSwGVRPCountersTxMsgLeaveEmpty_Object((1,3,6,1,4,1,207,8,17,3,8,1,24),_AtiStkSwGVRPCountersTxMsgLeaveEmpty_Type())
atiStkSwGVRPCountersTxMsgLeaveEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersTxMsgLeaveEmpty.setStatus(_A)
_AtiStkSwGVRPCountersTxMsgLeaveIn_Type=Counter32
_AtiStkSwGVRPCountersTxMsgLeaveIn_Object=MibTableColumn
atiStkSwGVRPCountersTxMsgLeaveIn=_AtiStkSwGVRPCountersTxMsgLeaveIn_Object((1,3,6,1,4,1,207,8,17,3,8,1,25),_AtiStkSwGVRPCountersTxMsgLeaveIn_Type())
atiStkSwGVRPCountersTxMsgLeaveIn.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersTxMsgLeaveIn.setStatus(_A)
_AtiStkSwGVRPCountersTxMsgEmpty_Type=Counter32
_AtiStkSwGVRPCountersTxMsgEmpty_Object=MibTableColumn
atiStkSwGVRPCountersTxMsgEmpty=_AtiStkSwGVRPCountersTxMsgEmpty_Object((1,3,6,1,4,1,207,8,17,3,8,1,26),_AtiStkSwGVRPCountersTxMsgEmpty_Type())
atiStkSwGVRPCountersTxMsgEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwGVRPCountersTxMsgEmpty.setStatus(_A)
_AtiStkSwMacAddrGroup_ObjectIdentity=ObjectIdentity
atiStkSwMacAddrGroup=_AtiStkSwMacAddrGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,4))
_AtiStkSwStaticMacAddrTable_Object=MibTable
atiStkSwStaticMacAddrTable=_AtiStkSwStaticMacAddrTable_Object((1,3,6,1,4,1,207,8,17,4,1))
if mibBuilder.loadTexts:atiStkSwStaticMacAddrTable.setStatus(_A)
_AtiStkSwStaticMacAddrEntry_Object=MibTableRow
atiStkSwStaticMacAddrEntry=_AtiStkSwStaticMacAddrEntry_Object((1,3,6,1,4,1,207,8,17,4,1,1))
atiStkSwStaticMacAddrEntry.setIndexNames((0,_E,_A2),(0,_E,_A3))
if mibBuilder.loadTexts:atiStkSwStaticMacAddrEntry.setStatus(_A)
_AtiStkSwStaticMacAddress_Type=MacAddress
_AtiStkSwStaticMacAddress_Object=MibTableColumn
atiStkSwStaticMacAddress=_AtiStkSwStaticMacAddress_Object((1,3,6,1,4,1,207,8,17,4,1,1,1),_AtiStkSwStaticMacAddress_Type())
atiStkSwStaticMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwStaticMacAddress.setStatus(_A)
class _AtiStkSwStaticMacAddrVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AtiStkSwStaticMacAddrVlanId_Type.__name__=_D
_AtiStkSwStaticMacAddrVlanId_Object=MibTableColumn
atiStkSwStaticMacAddrVlanId=_AtiStkSwStaticMacAddrVlanId_Object((1,3,6,1,4,1,207,8,17,4,1,1,2),_AtiStkSwStaticMacAddrVlanId_Type())
atiStkSwStaticMacAddrVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwStaticMacAddrVlanId.setStatus(_A)
class _AtiStkSwStaticMacAddrModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwStaticMacAddrModuleId_Type.__name__=_D
_AtiStkSwStaticMacAddrModuleId_Object=MibTableColumn
atiStkSwStaticMacAddrModuleId=_AtiStkSwStaticMacAddrModuleId_Object((1,3,6,1,4,1,207,8,17,4,1,1,3),_AtiStkSwStaticMacAddrModuleId_Type())
atiStkSwStaticMacAddrModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwStaticMacAddrModuleId.setStatus(_A)
_AtiStkSwStaticMacAddrPortId_Type=Integer32
_AtiStkSwStaticMacAddrPortId_Object=MibTableColumn
atiStkSwStaticMacAddrPortId=_AtiStkSwStaticMacAddrPortId_Object((1,3,6,1,4,1,207,8,17,4,1,1,4),_AtiStkSwStaticMacAddrPortId_Type())
atiStkSwStaticMacAddrPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwStaticMacAddrPortId.setStatus(_A)
class _AtiStkSwStaticMacAddrPortList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiStkSwStaticMacAddrPortList_Type.__name__=_F
_AtiStkSwStaticMacAddrPortList_Object=MibTableColumn
atiStkSwStaticMacAddrPortList=_AtiStkSwStaticMacAddrPortList_Object((1,3,6,1,4,1,207,8,17,4,1,1,5),_AtiStkSwStaticMacAddrPortList_Type())
atiStkSwStaticMacAddrPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwStaticMacAddrPortList.setStatus(_A)
_AtiStkSwStaticMacAddrEntryStatus_Type=RowStatus
_AtiStkSwStaticMacAddrEntryStatus_Object=MibTableColumn
atiStkSwStaticMacAddrEntryStatus=_AtiStkSwStaticMacAddrEntryStatus_Object((1,3,6,1,4,1,207,8,17,4,1,1,6),_AtiStkSwStaticMacAddrEntryStatus_Type())
atiStkSwStaticMacAddrEntryStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:atiStkSwStaticMacAddrEntryStatus.setStatus(_A)
_AtiStkSwEthStatsGroup_ObjectIdentity=ObjectIdentity
atiStkSwEthStatsGroup=_AtiStkSwEthStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,5))
_AtiStkSwEthModuleMonTable_Object=MibTable
atiStkSwEthModuleMonTable=_AtiStkSwEthModuleMonTable_Object((1,3,6,1,4,1,207,8,17,5,1))
if mibBuilder.loadTexts:atiStkSwEthModuleMonTable.setStatus(_A)
_AtiStkSwEthModuleMonEntry_Object=MibTableRow
atiStkSwEthModuleMonEntry=_AtiStkSwEthModuleMonEntry_Object((1,3,6,1,4,1,207,8,17,5,1,1))
atiStkSwEthModuleMonEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:atiStkSwEthModuleMonEntry.setStatus(_A)
_AtiStkSwEthModuleMonTxGoodFrames_Type=Counter64
_AtiStkSwEthModuleMonTxGoodFrames_Object=MibTableColumn
atiStkSwEthModuleMonTxGoodFrames=_AtiStkSwEthModuleMonTxGoodFrames_Object((1,3,6,1,4,1,207,8,17,5,1,1,1),_AtiStkSwEthModuleMonTxGoodFrames_Type())
atiStkSwEthModuleMonTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleMonTxGoodFrames.setStatus(_A)
_AtiStkSwEthModuleMonRxGoodFrames_Type=Counter64
_AtiStkSwEthModuleMonRxGoodFrames_Object=MibTableColumn
atiStkSwEthModuleMonRxGoodFrames=_AtiStkSwEthModuleMonRxGoodFrames_Object((1,3,6,1,4,1,207,8,17,5,1,1,2),_AtiStkSwEthModuleMonRxGoodFrames_Type())
atiStkSwEthModuleMonRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleMonRxGoodFrames.setStatus(_A)
_AtiStkSwEthModuleMonTxTotalBytes_Type=Counter64
_AtiStkSwEthModuleMonTxTotalBytes_Object=MibTableColumn
atiStkSwEthModuleMonTxTotalBytes=_AtiStkSwEthModuleMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,17,5,1,1,3),_AtiStkSwEthModuleMonTxTotalBytes_Type())
atiStkSwEthModuleMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleMonTxTotalBytes.setStatus(_A)
_AtiStkSwEthModuleMonTxBroadcastFrames_Type=Counter64
_AtiStkSwEthModuleMonTxBroadcastFrames_Object=MibTableColumn
atiStkSwEthModuleMonTxBroadcastFrames=_AtiStkSwEthModuleMonTxBroadcastFrames_Object((1,3,6,1,4,1,207,8,17,5,1,1,4),_AtiStkSwEthModuleMonTxBroadcastFrames_Type())
atiStkSwEthModuleMonTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleMonTxBroadcastFrames.setStatus(_A)
_AtiStkSwEthModuleMonTxMulticastFrames_Type=Counter64
_AtiStkSwEthModuleMonTxMulticastFrames_Object=MibTableColumn
atiStkSwEthModuleMonTxMulticastFrames=_AtiStkSwEthModuleMonTxMulticastFrames_Object((1,3,6,1,4,1,207,8,17,5,1,1,5),_AtiStkSwEthModuleMonTxMulticastFrames_Type())
atiStkSwEthModuleMonTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleMonTxMulticastFrames.setStatus(_A)
_AtiStkSwEthModuleMonRxOverrunFrames_Type=Counter64
_AtiStkSwEthModuleMonRxOverrunFrames_Object=MibTableColumn
atiStkSwEthModuleMonRxOverrunFrames=_AtiStkSwEthModuleMonRxOverrunFrames_Object((1,3,6,1,4,1,207,8,17,5,1,1,6),_AtiStkSwEthModuleMonRxOverrunFrames_Type())
atiStkSwEthModuleMonRxOverrunFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleMonRxOverrunFrames.setStatus(_A)
_AtiStkSwEthModuleErrTable_Object=MibTable
atiStkSwEthModuleErrTable=_AtiStkSwEthModuleErrTable_Object((1,3,6,1,4,1,207,8,17,5,2))
if mibBuilder.loadTexts:atiStkSwEthModuleErrTable.setStatus(_A)
_AtiStkSwEthModuleErrEntry_Object=MibTableRow
atiStkSwEthModuleErrEntry=_AtiStkSwEthModuleErrEntry_Object((1,3,6,1,4,1,207,8,17,5,2,1))
atiStkSwEthModuleErrEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:atiStkSwEthModuleErrEntry.setStatus(_A)
_AtiStkSwEthModuleErrRxCRC_Type=Counter64
_AtiStkSwEthModuleErrRxCRC_Object=MibTableColumn
atiStkSwEthModuleErrRxCRC=_AtiStkSwEthModuleErrRxCRC_Object((1,3,6,1,4,1,207,8,17,5,2,1,1),_AtiStkSwEthModuleErrRxCRC_Type())
atiStkSwEthModuleErrRxCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleErrRxCRC.setStatus(_A)
_AtiStkSwEthModuleErrRxBadFrames_Type=Counter64
_AtiStkSwEthModuleErrRxBadFrames_Object=MibTableColumn
atiStkSwEthModuleErrRxBadFrames=_AtiStkSwEthModuleErrRxBadFrames_Object((1,3,6,1,4,1,207,8,17,5,2,1,2),_AtiStkSwEthModuleErrRxBadFrames_Type())
atiStkSwEthModuleErrRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleErrRxBadFrames.setStatus(_A)
_AtiStkSwEthModuleErrCollisions_Type=Counter64
_AtiStkSwEthModuleErrCollisions_Object=MibTableColumn
atiStkSwEthModuleErrCollisions=_AtiStkSwEthModuleErrCollisions_Object((1,3,6,1,4,1,207,8,17,5,2,1,3),_AtiStkSwEthModuleErrCollisions_Type())
atiStkSwEthModuleErrCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthModuleErrCollisions.setStatus(_A)
_AtiStkSwEthPortMonTable_Object=MibTable
atiStkSwEthPortMonTable=_AtiStkSwEthPortMonTable_Object((1,3,6,1,4,1,207,8,17,5,3))
if mibBuilder.loadTexts:atiStkSwEthPortMonTable.setStatus(_A)
_AtiStkSwEthPortMonEntry_Object=MibTableRow
atiStkSwEthPortMonEntry=_AtiStkSwEthPortMonEntry_Object((1,3,6,1,4,1,207,8,17,5,3,1))
atiStkSwEthPortMonEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkSwEthPortMonEntry.setStatus(_A)
_AtiStkSwEthPortMonTxGoodFrames_Type=Counter64
_AtiStkSwEthPortMonTxGoodFrames_Object=MibTableColumn
atiStkSwEthPortMonTxGoodFrames=_AtiStkSwEthPortMonTxGoodFrames_Object((1,3,6,1,4,1,207,8,17,5,3,1,1),_AtiStkSwEthPortMonTxGoodFrames_Type())
atiStkSwEthPortMonTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortMonTxGoodFrames.setStatus(_A)
_AtiStkSwEthPortMonRxGoodFrames_Type=Counter64
_AtiStkSwEthPortMonRxGoodFrames_Object=MibTableColumn
atiStkSwEthPortMonRxGoodFrames=_AtiStkSwEthPortMonRxGoodFrames_Object((1,3,6,1,4,1,207,8,17,5,3,1,2),_AtiStkSwEthPortMonRxGoodFrames_Type())
atiStkSwEthPortMonRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortMonRxGoodFrames.setStatus(_A)
_AtiStkSwEthPortMonTxTotalBytes_Type=Counter64
_AtiStkSwEthPortMonTxTotalBytes_Object=MibTableColumn
atiStkSwEthPortMonTxTotalBytes=_AtiStkSwEthPortMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,17,5,3,1,3),_AtiStkSwEthPortMonTxTotalBytes_Type())
atiStkSwEthPortMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortMonTxTotalBytes.setStatus(_A)
_AtiStkSwEthPortMonTxBroadcastFrames_Type=Counter64
_AtiStkSwEthPortMonTxBroadcastFrames_Object=MibTableColumn
atiStkSwEthPortMonTxBroadcastFrames=_AtiStkSwEthPortMonTxBroadcastFrames_Object((1,3,6,1,4,1,207,8,17,5,3,1,4),_AtiStkSwEthPortMonTxBroadcastFrames_Type())
atiStkSwEthPortMonTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortMonTxBroadcastFrames.setStatus(_A)
_AtiStkSwEthPortMonTxMulticastFrames_Type=Counter64
_AtiStkSwEthPortMonTxMulticastFrames_Object=MibTableColumn
atiStkSwEthPortMonTxMulticastFrames=_AtiStkSwEthPortMonTxMulticastFrames_Object((1,3,6,1,4,1,207,8,17,5,3,1,5),_AtiStkSwEthPortMonTxMulticastFrames_Type())
atiStkSwEthPortMonTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortMonTxMulticastFrames.setStatus(_A)
_AtiStkSwEthPortMonRxOverrunFrames_Type=Counter64
_AtiStkSwEthPortMonRxOverrunFrames_Object=MibTableColumn
atiStkSwEthPortMonRxOverrunFrames=_AtiStkSwEthPortMonRxOverrunFrames_Object((1,3,6,1,4,1,207,8,17,5,3,1,6),_AtiStkSwEthPortMonRxOverrunFrames_Type())
atiStkSwEthPortMonRxOverrunFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortMonRxOverrunFrames.setStatus(_A)
_AtiStkSwEthPortErrTable_Object=MibTable
atiStkSwEthPortErrTable=_AtiStkSwEthPortErrTable_Object((1,3,6,1,4,1,207,8,17,5,4))
if mibBuilder.loadTexts:atiStkSwEthPortErrTable.setStatus(_A)
_AtiStkSwEthPortErrEntry_Object=MibTableRow
atiStkSwEthPortErrEntry=_AtiStkSwEthPortErrEntry_Object((1,3,6,1,4,1,207,8,17,5,4,1))
atiStkSwEthPortErrEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:atiStkSwEthPortErrEntry.setStatus(_A)
_AtiStkSwEthPortErrRxBadFrames_Type=Counter64
_AtiStkSwEthPortErrRxBadFrames_Object=MibTableColumn
atiStkSwEthPortErrRxBadFrames=_AtiStkSwEthPortErrRxBadFrames_Object((1,3,6,1,4,1,207,8,17,5,4,1,1),_AtiStkSwEthPortErrRxBadFrames_Type())
atiStkSwEthPortErrRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortErrRxBadFrames.setStatus(_A)
_AtiStkSwEthPortErrCollisions_Type=Counter64
_AtiStkSwEthPortErrCollisions_Object=MibTableColumn
atiStkSwEthPortErrCollisions=_AtiStkSwEthPortErrCollisions_Object((1,3,6,1,4,1,207,8,17,5,4,1,2),_AtiStkSwEthPortErrCollisions_Type())
atiStkSwEthPortErrCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwEthPortErrCollisions.setStatus(_A)
_AtiStkSwTrapsGroup_ObjectIdentity=ObjectIdentity
atiStkSwTrapsGroup=_AtiStkSwTrapsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,6))
class _AtiStkSwTrapVarMgmtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notrap',1),('ssh',2),(_r,3),('web',4)))
_AtiStkSwTrapVarMgmtType_Type.__name__=_D
_AtiStkSwTrapVarMgmtType_Object=MibScalar
atiStkSwTrapVarMgmtType=_AtiStkSwTrapVarMgmtType_Object((1,3,6,1,4,1,207,8,17,6,8),_AtiStkSwTrapVarMgmtType_Type())
atiStkSwTrapVarMgmtType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwTrapVarMgmtType.setStatus(_A)
_AtiStkSwTrapVarMgmtIpAddr_Type=IpAddress
_AtiStkSwTrapVarMgmtIpAddr_Object=MibScalar
atiStkSwTrapVarMgmtIpAddr=_AtiStkSwTrapVarMgmtIpAddr_Object((1,3,6,1,4,1,207,8,17,6,9),_AtiStkSwTrapVarMgmtIpAddr_Type())
atiStkSwTrapVarMgmtIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwTrapVarMgmtIpAddr.setStatus(_A)
_AtiStkSwQoSGroup_ObjectIdentity=ObjectIdentity
atiStkSwQoSGroup=_AtiStkSwQoSGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,7))
_AtiStkSwQoSGroupNumberOfQueues_Type=Integer32
_AtiStkSwQoSGroupNumberOfQueues_Object=MibScalar
atiStkSwQoSGroupNumberOfQueues=_AtiStkSwQoSGroupNumberOfQueues_Object((1,3,6,1,4,1,207,8,17,7,1),_AtiStkSwQoSGroupNumberOfQueues_Type())
atiStkSwQoSGroupNumberOfQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQoSGroupNumberOfQueues.setStatus(_A)
class _AtiStkSwQoSGroupSchedulingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict-priority',1),('weighted-round-robin',2)))
_AtiStkSwQoSGroupSchedulingMode_Type.__name__=_D
_AtiStkSwQoSGroupSchedulingMode_Object=MibScalar
atiStkSwQoSGroupSchedulingMode=_AtiStkSwQoSGroupSchedulingMode_Object((1,3,6,1,4,1,207,8,17,7,2),_AtiStkSwQoSGroupSchedulingMode_Type())
atiStkSwQoSGroupSchedulingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQoSGroupSchedulingMode.setStatus(_A)
_AtiStkSwQoSGroupCoSToQueueTable_Object=MibTable
atiStkSwQoSGroupCoSToQueueTable=_AtiStkSwQoSGroupCoSToQueueTable_Object((1,3,6,1,4,1,207,8,17,7,3))
if mibBuilder.loadTexts:atiStkSwQoSGroupCoSToQueueTable.setStatus(_A)
_AtiStkSwQoSGroupCoSToQueueEntry_Object=MibTableRow
atiStkSwQoSGroupCoSToQueueEntry=_AtiStkSwQoSGroupCoSToQueueEntry_Object((1,3,6,1,4,1,207,8,17,7,3,1))
atiStkSwQoSGroupCoSToQueueEntry.setIndexNames((0,_E,_A4))
if mibBuilder.loadTexts:atiStkSwQoSGroupCoSToQueueEntry.setStatus(_A)
class _AtiStkSwQoSGroupCoSPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cos-priority-0',1),('cos-priority-1',2),('cos-priority-2',3),('cos-priority-3',4),('cos-priority-4',5),('cos-priority-5',6),('cos-priority-6',7),('cos-priority-7',8)))
_AtiStkSwQoSGroupCoSPriority_Type.__name__=_D
_AtiStkSwQoSGroupCoSPriority_Object=MibTableColumn
atiStkSwQoSGroupCoSPriority=_AtiStkSwQoSGroupCoSPriority_Object((1,3,6,1,4,1,207,8,17,7,3,1,1),_AtiStkSwQoSGroupCoSPriority_Type())
atiStkSwQoSGroupCoSPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQoSGroupCoSPriority.setStatus(_A)
class _AtiStkSwQoSGroupCoSQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_A5,1),(_A6,2),(_A7,3),(_A8,4),(_A9,5),(_AA,6),(_AB,7),(_AC,8)))
_AtiStkSwQoSGroupCoSQueue_Type.__name__=_D
_AtiStkSwQoSGroupCoSQueue_Object=MibTableColumn
atiStkSwQoSGroupCoSQueue=_AtiStkSwQoSGroupCoSQueue_Object((1,3,6,1,4,1,207,8,17,7,3,1,2),_AtiStkSwQoSGroupCoSQueue_Type())
atiStkSwQoSGroupCoSQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQoSGroupCoSQueue.setStatus(_A)
_AtiStkSwQoSGroupQueueToWeightTable_Object=MibTable
atiStkSwQoSGroupQueueToWeightTable=_AtiStkSwQoSGroupQueueToWeightTable_Object((1,3,6,1,4,1,207,8,17,7,4))
if mibBuilder.loadTexts:atiStkSwQoSGroupQueueToWeightTable.setStatus(_A)
_AtiStkSwQoSGroupQueueToWeightEntry_Object=MibTableRow
atiStkSwQoSGroupQueueToWeightEntry=_AtiStkSwQoSGroupQueueToWeightEntry_Object((1,3,6,1,4,1,207,8,17,7,4,1))
atiStkSwQoSGroupQueueToWeightEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:atiStkSwQoSGroupQueueToWeightEntry.setStatus(_A)
class _AtiStkSwQoSGroupQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_A5,1),(_A6,2),(_A7,3),(_A8,4),(_A9,5),(_AA,6),(_AB,7),(_AC,8)))
_AtiStkSwQoSGroupQueue_Type.__name__=_D
_AtiStkSwQoSGroupQueue_Object=MibTableColumn
atiStkSwQoSGroupQueue=_AtiStkSwQoSGroupQueue_Object((1,3,6,1,4,1,207,8,17,7,4,1,1),_AtiStkSwQoSGroupQueue_Type())
atiStkSwQoSGroupQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQoSGroupQueue.setStatus(_A)
class _AtiStkSwQoSGroupQueueWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_AtiStkSwQoSGroupQueueWeight_Type.__name__=_D
_AtiStkSwQoSGroupQueueWeight_Object=MibTableColumn
atiStkSwQoSGroupQueueWeight=_AtiStkSwQoSGroupQueueWeight_Object((1,3,6,1,4,1,207,8,17,7,4,1,2),_AtiStkSwQoSGroupQueueWeight_Type())
atiStkSwQoSGroupQueueWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQoSGroupQueueWeight.setStatus(_A)
_AtiStkSwQosFlowGrpTable_Object=MibTable
atiStkSwQosFlowGrpTable=_AtiStkSwQosFlowGrpTable_Object((1,3,6,1,4,1,207,8,17,7,5))
if mibBuilder.loadTexts:atiStkSwQosFlowGrpTable.setStatus(_A)
_AtiStkSwQosFlowGrpEntry_Object=MibTableRow
atiStkSwQosFlowGrpEntry=_AtiStkSwQosFlowGrpEntry_Object((1,3,6,1,4,1,207,8,17,7,5,1))
atiStkSwQosFlowGrpEntry.setIndexNames((0,_E,_AE),(0,_E,_AF))
if mibBuilder.loadTexts:atiStkSwQosFlowGrpEntry.setStatus(_A)
class _AtiStkSwQosFlowGrpModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwQosFlowGrpModuleId_Type.__name__=_D
_AtiStkSwQosFlowGrpModuleId_Object=MibTableColumn
atiStkSwQosFlowGrpModuleId=_AtiStkSwQosFlowGrpModuleId_Object((1,3,6,1,4,1,207,8,17,7,5,1,1),_AtiStkSwQosFlowGrpModuleId_Type())
atiStkSwQosFlowGrpModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpModuleId.setStatus(_A)
class _AtiStkSwQosFlowGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_AtiStkSwQosFlowGrpId_Type.__name__=_D
_AtiStkSwQosFlowGrpId_Object=MibTableColumn
atiStkSwQosFlowGrpId=_AtiStkSwQosFlowGrpId_Object((1,3,6,1,4,1,207,8,17,7,5,1,2),_AtiStkSwQosFlowGrpId_Type())
atiStkSwQosFlowGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpId.setStatus(_A)
class _AtiStkSwQosFlowGrpDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AtiStkSwQosFlowGrpDescription_Type.__name__=_F
_AtiStkSwQosFlowGrpDescription_Object=MibTableColumn
atiStkSwQosFlowGrpDescription=_AtiStkSwQosFlowGrpDescription_Object((1,3,6,1,4,1,207,8,17,7,5,1,3),_AtiStkSwQosFlowGrpDescription_Type())
atiStkSwQosFlowGrpDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpDescription.setStatus(_A)
class _AtiStkSwQosFlowGrpDSCPValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AtiStkSwQosFlowGrpDSCPValue_Type.__name__=_F
_AtiStkSwQosFlowGrpDSCPValue_Object=MibTableColumn
atiStkSwQosFlowGrpDSCPValue=_AtiStkSwQosFlowGrpDSCPValue_Object((1,3,6,1,4,1,207,8,17,7,5,1,4),_AtiStkSwQosFlowGrpDSCPValue_Type())
atiStkSwQosFlowGrpDSCPValue.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpDSCPValue.setStatus(_A)
class _AtiStkSwQosFlowGrpPriority_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_AtiStkSwQosFlowGrpPriority_Type.__name__=_F
_AtiStkSwQosFlowGrpPriority_Object=MibTableColumn
atiStkSwQosFlowGrpPriority=_AtiStkSwQosFlowGrpPriority_Object((1,3,6,1,4,1,207,8,17,7,5,1,5),_AtiStkSwQosFlowGrpPriority_Type())
atiStkSwQosFlowGrpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpPriority.setStatus(_A)
class _AtiStkSwQosFlowGrpRemarkPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosFlowGrpRemarkPriority_Type.__name__=_D
_AtiStkSwQosFlowGrpRemarkPriority_Object=MibTableColumn
atiStkSwQosFlowGrpRemarkPriority=_AtiStkSwQosFlowGrpRemarkPriority_Object((1,3,6,1,4,1,207,8,17,7,5,1,6),_AtiStkSwQosFlowGrpRemarkPriority_Type())
atiStkSwQosFlowGrpRemarkPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpRemarkPriority.setStatus(_A)
class _AtiStkSwQosFlowGrpTos_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_AtiStkSwQosFlowGrpTos_Type.__name__=_F
_AtiStkSwQosFlowGrpTos_Object=MibTableColumn
atiStkSwQosFlowGrpTos=_AtiStkSwQosFlowGrpTos_Object((1,3,6,1,4,1,207,8,17,7,5,1,7),_AtiStkSwQosFlowGrpTos_Type())
atiStkSwQosFlowGrpTos.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpTos.setStatus(_A)
class _AtiStkSwQosFlowGrpTosToPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosFlowGrpTosToPriority_Type.__name__=_D
_AtiStkSwQosFlowGrpTosToPriority_Object=MibTableColumn
atiStkSwQosFlowGrpTosToPriority=_AtiStkSwQosFlowGrpTosToPriority_Object((1,3,6,1,4,1,207,8,17,7,5,1,8),_AtiStkSwQosFlowGrpTosToPriority_Type())
atiStkSwQosFlowGrpTosToPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpTosToPriority.setStatus(_A)
class _AtiStkSwQosFlowGrpPriorityToTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosFlowGrpPriorityToTos_Type.__name__=_D
_AtiStkSwQosFlowGrpPriorityToTos_Object=MibTableColumn
atiStkSwQosFlowGrpPriorityToTos=_AtiStkSwQosFlowGrpPriorityToTos_Object((1,3,6,1,4,1,207,8,17,7,5,1,9),_AtiStkSwQosFlowGrpPriorityToTos_Type())
atiStkSwQosFlowGrpPriorityToTos.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpPriorityToTos.setStatus(_A)
_AtiStkSwQosFlowGrpClassifierList_Type=DisplayString
_AtiStkSwQosFlowGrpClassifierList_Object=MibTableColumn
atiStkSwQosFlowGrpClassifierList=_AtiStkSwQosFlowGrpClassifierList_Object((1,3,6,1,4,1,207,8,17,7,5,1,10),_AtiStkSwQosFlowGrpClassifierList_Type())
atiStkSwQosFlowGrpClassifierList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpClassifierList.setStatus(_A)
_AtiStkSwQosFlowGrpRowStatus_Type=RowStatus
_AtiStkSwQosFlowGrpRowStatus_Object=MibTableColumn
atiStkSwQosFlowGrpRowStatus=_AtiStkSwQosFlowGrpRowStatus_Object((1,3,6,1,4,1,207,8,17,7,5,1,11),_AtiStkSwQosFlowGrpRowStatus_Type())
atiStkSwQosFlowGrpRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:atiStkSwQosFlowGrpRowStatus.setStatus(_A)
_AtiStkSwQosTrafficClassTable_Object=MibTable
atiStkSwQosTrafficClassTable=_AtiStkSwQosTrafficClassTable_Object((1,3,6,1,4,1,207,8,17,7,6))
if mibBuilder.loadTexts:atiStkSwQosTrafficClassTable.setStatus(_A)
_AtiStkSwQosTrafficClassEntry_Object=MibTableRow
atiStkSwQosTrafficClassEntry=_AtiStkSwQosTrafficClassEntry_Object((1,3,6,1,4,1,207,8,17,7,6,1))
atiStkSwQosTrafficClassEntry.setIndexNames((0,_E,_AG),(0,_E,_AH))
if mibBuilder.loadTexts:atiStkSwQosTrafficClassEntry.setStatus(_A)
class _AtiStkSwQosTrafficClassModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwQosTrafficClassModuleId_Type.__name__=_D
_AtiStkSwQosTrafficClassModuleId_Object=MibTableColumn
atiStkSwQosTrafficClassModuleId=_AtiStkSwQosTrafficClassModuleId_Object((1,3,6,1,4,1,207,8,17,7,6,1,1),_AtiStkSwQosTrafficClassModuleId_Type())
atiStkSwQosTrafficClassModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassModuleId.setStatus(_A)
class _AtiStkSwQosTrafficClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_AtiStkSwQosTrafficClassId_Type.__name__=_D
_AtiStkSwQosTrafficClassId_Object=MibTableColumn
atiStkSwQosTrafficClassId=_AtiStkSwQosTrafficClassId_Object((1,3,6,1,4,1,207,8,17,7,6,1,2),_AtiStkSwQosTrafficClassId_Type())
atiStkSwQosTrafficClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassId.setStatus(_A)
class _AtiStkSwQosTrafficClassDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AtiStkSwQosTrafficClassDescription_Type.__name__=_F
_AtiStkSwQosTrafficClassDescription_Object=MibTableColumn
atiStkSwQosTrafficClassDescription=_AtiStkSwQosTrafficClassDescription_Object((1,3,6,1,4,1,207,8,17,7,6,1,3),_AtiStkSwQosTrafficClassDescription_Type())
atiStkSwQosTrafficClassDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassDescription.setStatus(_A)
class _AtiStkSwQosTrafficClassExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('remark',2)))
_AtiStkSwQosTrafficClassExceedAction_Type.__name__=_D
_AtiStkSwQosTrafficClassExceedAction_Object=MibTableColumn
atiStkSwQosTrafficClassExceedAction=_AtiStkSwQosTrafficClassExceedAction_Object((1,3,6,1,4,1,207,8,17,7,6,1,4),_AtiStkSwQosTrafficClassExceedAction_Type())
atiStkSwQosTrafficClassExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassExceedAction.setStatus(_A)
class _AtiStkSwQosTrafficClassExceedRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AtiStkSwQosTrafficClassExceedRemarkValue_Type.__name__=_D
_AtiStkSwQosTrafficClassExceedRemarkValue_Object=MibTableColumn
atiStkSwQosTrafficClassExceedRemarkValue=_AtiStkSwQosTrafficClassExceedRemarkValue_Object((1,3,6,1,4,1,207,8,17,7,6,1,5),_AtiStkSwQosTrafficClassExceedRemarkValue_Type())
atiStkSwQosTrafficClassExceedRemarkValue.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassExceedRemarkValue.setStatus(_A)
class _AtiStkSwQosTrafficClassDSCPValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AtiStkSwQosTrafficClassDSCPValue_Type.__name__=_F
_AtiStkSwQosTrafficClassDSCPValue_Object=MibTableColumn
atiStkSwQosTrafficClassDSCPValue=_AtiStkSwQosTrafficClassDSCPValue_Object((1,3,6,1,4,1,207,8,17,7,6,1,6),_AtiStkSwQosTrafficClassDSCPValue_Type())
atiStkSwQosTrafficClassDSCPValue.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassDSCPValue.setStatus(_A)
class _AtiStkSwQosTrafficClassMaxBandwidth_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_AtiStkSwQosTrafficClassMaxBandwidth_Type.__name__=_F
_AtiStkSwQosTrafficClassMaxBandwidth_Object=MibTableColumn
atiStkSwQosTrafficClassMaxBandwidth=_AtiStkSwQosTrafficClassMaxBandwidth_Object((1,3,6,1,4,1,207,8,17,7,6,1,7),_AtiStkSwQosTrafficClassMaxBandwidth_Type())
atiStkSwQosTrafficClassMaxBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassMaxBandwidth.setStatus(_A)
class _AtiStkSwQosTrafficClassBurstSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_AtiStkSwQosTrafficClassBurstSize_Type.__name__=_F
_AtiStkSwQosTrafficClassBurstSize_Object=MibTableColumn
atiStkSwQosTrafficClassBurstSize=_AtiStkSwQosTrafficClassBurstSize_Object((1,3,6,1,4,1,207,8,17,7,6,1,8),_AtiStkSwQosTrafficClassBurstSize_Type())
atiStkSwQosTrafficClassBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassBurstSize.setStatus(_A)
class _AtiStkSwQosTrafficClassPriority_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AtiStkSwQosTrafficClassPriority_Type.__name__=_F
_AtiStkSwQosTrafficClassPriority_Object=MibTableColumn
atiStkSwQosTrafficClassPriority=_AtiStkSwQosTrafficClassPriority_Object((1,3,6,1,4,1,207,8,17,7,6,1,9),_AtiStkSwQosTrafficClassPriority_Type())
atiStkSwQosTrafficClassPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassPriority.setStatus(_A)
class _AtiStkSwQosTrafficClassRemarkPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosTrafficClassRemarkPriority_Type.__name__=_D
_AtiStkSwQosTrafficClassRemarkPriority_Object=MibTableColumn
atiStkSwQosTrafficClassRemarkPriority=_AtiStkSwQosTrafficClassRemarkPriority_Object((1,3,6,1,4,1,207,8,17,7,6,1,10),_AtiStkSwQosTrafficClassRemarkPriority_Type())
atiStkSwQosTrafficClassRemarkPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassRemarkPriority.setStatus(_A)
class _AtiStkSwQosTrafficClassToS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AtiStkSwQosTrafficClassToS_Type.__name__=_F
_AtiStkSwQosTrafficClassToS_Object=MibTableColumn
atiStkSwQosTrafficClassToS=_AtiStkSwQosTrafficClassToS_Object((1,3,6,1,4,1,207,8,17,7,6,1,11),_AtiStkSwQosTrafficClassToS_Type())
atiStkSwQosTrafficClassToS.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassToS.setStatus(_A)
class _AtiStkSwQosTrafficClassMoveToSToPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosTrafficClassMoveToSToPriority_Type.__name__=_D
_AtiStkSwQosTrafficClassMoveToSToPriority_Object=MibTableColumn
atiStkSwQosTrafficClassMoveToSToPriority=_AtiStkSwQosTrafficClassMoveToSToPriority_Object((1,3,6,1,4,1,207,8,17,7,6,1,12),_AtiStkSwQosTrafficClassMoveToSToPriority_Type())
atiStkSwQosTrafficClassMoveToSToPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassMoveToSToPriority.setStatus(_A)
class _AtiStkSwQosTrafficClassMovePriorityToToS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosTrafficClassMovePriorityToToS_Type.__name__=_D
_AtiStkSwQosTrafficClassMovePriorityToToS_Object=MibTableColumn
atiStkSwQosTrafficClassMovePriorityToToS=_AtiStkSwQosTrafficClassMovePriorityToToS_Object((1,3,6,1,4,1,207,8,17,7,6,1,13),_AtiStkSwQosTrafficClassMovePriorityToToS_Type())
atiStkSwQosTrafficClassMovePriorityToToS.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassMovePriorityToToS.setStatus(_A)
_AtiStkSwQosTrafficClassFlowGroupList_Type=DisplayString
_AtiStkSwQosTrafficClassFlowGroupList_Object=MibTableColumn
atiStkSwQosTrafficClassFlowGroupList=_AtiStkSwQosTrafficClassFlowGroupList_Object((1,3,6,1,4,1,207,8,17,7,6,1,14),_AtiStkSwQosTrafficClassFlowGroupList_Type())
atiStkSwQosTrafficClassFlowGroupList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassFlowGroupList.setStatus(_A)
_AtiStkSwQosTrafficClassRowStatus_Type=RowStatus
_AtiStkSwQosTrafficClassRowStatus_Object=MibTableColumn
atiStkSwQosTrafficClassRowStatus=_AtiStkSwQosTrafficClassRowStatus_Object((1,3,6,1,4,1,207,8,17,7,6,1,15),_AtiStkSwQosTrafficClassRowStatus_Type())
atiStkSwQosTrafficClassRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:atiStkSwQosTrafficClassRowStatus.setStatus(_A)
_AtiStkSwQosPolicyTable_Object=MibTable
atiStkSwQosPolicyTable=_AtiStkSwQosPolicyTable_Object((1,3,6,1,4,1,207,8,17,7,7))
if mibBuilder.loadTexts:atiStkSwQosPolicyTable.setStatus(_A)
_AtiStkSwQosPolicyEntry_Object=MibTableRow
atiStkSwQosPolicyEntry=_AtiStkSwQosPolicyEntry_Object((1,3,6,1,4,1,207,8,17,7,7,1))
atiStkSwQosPolicyEntry.setIndexNames((0,_E,_AI),(0,_E,_AJ))
if mibBuilder.loadTexts:atiStkSwQosPolicyEntry.setStatus(_A)
class _AtiStkSwQosPolicyModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwQosPolicyModuleId_Type.__name__=_D
_AtiStkSwQosPolicyModuleId_Object=MibTableColumn
atiStkSwQosPolicyModuleId=_AtiStkSwQosPolicyModuleId_Object((1,3,6,1,4,1,207,8,17,7,7,1,1),_AtiStkSwQosPolicyModuleId_Type())
atiStkSwQosPolicyModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQosPolicyModuleId.setStatus(_A)
class _AtiStkSwQosPolicyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_AtiStkSwQosPolicyId_Type.__name__=_D
_AtiStkSwQosPolicyId_Object=MibTableColumn
atiStkSwQosPolicyId=_AtiStkSwQosPolicyId_Object((1,3,6,1,4,1,207,8,17,7,7,1,2),_AtiStkSwQosPolicyId_Type())
atiStkSwQosPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQosPolicyId.setStatus(_A)
class _AtiStkSwQosPolicyDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AtiStkSwQosPolicyDescription_Type.__name__=_F
_AtiStkSwQosPolicyDescription_Object=MibTableColumn
atiStkSwQosPolicyDescription=_AtiStkSwQosPolicyDescription_Object((1,3,6,1,4,1,207,8,17,7,7,1,3),_AtiStkSwQosPolicyDescription_Type())
atiStkSwQosPolicyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyDescription.setStatus(_A)
class _AtiStkSwQosPolicyRemarkDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('all',1),(_P,2)))
_AtiStkSwQosPolicyRemarkDSCP_Type.__name__=_D
_AtiStkSwQosPolicyRemarkDSCP_Object=MibTableColumn
atiStkSwQosPolicyRemarkDSCP=_AtiStkSwQosPolicyRemarkDSCP_Object((1,3,6,1,4,1,207,8,17,7,7,1,4),_AtiStkSwQosPolicyRemarkDSCP_Type())
atiStkSwQosPolicyRemarkDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyRemarkDSCP.setStatus(_A)
class _AtiStkSwQosPolicyDSCPValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AtiStkSwQosPolicyDSCPValue_Type.__name__=_F
_AtiStkSwQosPolicyDSCPValue_Object=MibTableColumn
atiStkSwQosPolicyDSCPValue=_AtiStkSwQosPolicyDSCPValue_Object((1,3,6,1,4,1,207,8,17,7,7,1,5),_AtiStkSwQosPolicyDSCPValue_Type())
atiStkSwQosPolicyDSCPValue.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyDSCPValue.setStatus(_A)
class _AtiStkSwQosPolicyToS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AtiStkSwQosPolicyToS_Type.__name__=_F
_AtiStkSwQosPolicyToS_Object=MibTableColumn
atiStkSwQosPolicyToS=_AtiStkSwQosPolicyToS_Object((1,3,6,1,4,1,207,8,17,7,7,1,6),_AtiStkSwQosPolicyToS_Type())
atiStkSwQosPolicyToS.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyToS.setStatus(_A)
class _AtiStkSwQosPolicyMoveToSToPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosPolicyMoveToSToPriority_Type.__name__=_D
_AtiStkSwQosPolicyMoveToSToPriority_Object=MibTableColumn
atiStkSwQosPolicyMoveToSToPriority=_AtiStkSwQosPolicyMoveToSToPriority_Object((1,3,6,1,4,1,207,8,17,7,7,1,7),_AtiStkSwQosPolicyMoveToSToPriority_Type())
atiStkSwQosPolicyMoveToSToPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyMoveToSToPriority.setStatus(_A)
class _AtiStkSwQosPolicyMovePriorityToToS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosPolicyMovePriorityToToS_Type.__name__=_D
_AtiStkSwQosPolicyMovePriorityToToS_Object=MibTableColumn
atiStkSwQosPolicyMovePriorityToToS=_AtiStkSwQosPolicyMovePriorityToToS_Object((1,3,6,1,4,1,207,8,17,7,7,1,8),_AtiStkSwQosPolicyMovePriorityToToS_Type())
atiStkSwQosPolicyMovePriorityToToS.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyMovePriorityToToS.setStatus(_A)
class _AtiStkSwQosPolicySendToMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQosPolicySendToMirrorPort_Type.__name__=_D
_AtiStkSwQosPolicySendToMirrorPort_Object=MibTableColumn
atiStkSwQosPolicySendToMirrorPort=_AtiStkSwQosPolicySendToMirrorPort_Object((1,3,6,1,4,1,207,8,17,7,7,1,9),_AtiStkSwQosPolicySendToMirrorPort_Type())
atiStkSwQosPolicySendToMirrorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicySendToMirrorPort.setStatus(_A)
_AtiStkSwQosPolicyTrafficClassList_Type=DisplayString
_AtiStkSwQosPolicyTrafficClassList_Object=MibTableColumn
atiStkSwQosPolicyTrafficClassList=_AtiStkSwQosPolicyTrafficClassList_Object((1,3,6,1,4,1,207,8,17,7,7,1,10),_AtiStkSwQosPolicyTrafficClassList_Type())
atiStkSwQosPolicyTrafficClassList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyTrafficClassList.setStatus(_A)
_AtiStkSwQosPolicyRedirectPort_Type=DisplayString
_AtiStkSwQosPolicyRedirectPort_Object=MibTableColumn
atiStkSwQosPolicyRedirectPort=_AtiStkSwQosPolicyRedirectPort_Object((1,3,6,1,4,1,207,8,17,7,7,1,11),_AtiStkSwQosPolicyRedirectPort_Type())
atiStkSwQosPolicyRedirectPort.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyRedirectPort.setStatus(_A)
_AtiStkSwQosPolicyIngressPortList_Type=DisplayString
_AtiStkSwQosPolicyIngressPortList_Object=MibTableColumn
atiStkSwQosPolicyIngressPortList=_AtiStkSwQosPolicyIngressPortList_Object((1,3,6,1,4,1,207,8,17,7,7,1,12),_AtiStkSwQosPolicyIngressPortList_Type())
atiStkSwQosPolicyIngressPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyIngressPortList.setStatus(_A)
_AtiStkSwQosPolicyEgressPortList_Type=DisplayString
_AtiStkSwQosPolicyEgressPortList_Object=MibTableColumn
atiStkSwQosPolicyEgressPortList=_AtiStkSwQosPolicyEgressPortList_Object((1,3,6,1,4,1,207,8,17,7,7,1,13),_AtiStkSwQosPolicyEgressPortList_Type())
atiStkSwQosPolicyEgressPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQosPolicyEgressPortList.setStatus(_A)
_AtiStkSwQosPolicyRowStatus_Type=RowStatus
_AtiStkSwQosPolicyRowStatus_Object=MibTableColumn
atiStkSwQosPolicyRowStatus=_AtiStkSwQosPolicyRowStatus_Object((1,3,6,1,4,1,207,8,17,7,7,1,14),_AtiStkSwQosPolicyRowStatus_Type())
atiStkSwQosPolicyRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:atiStkSwQosPolicyRowStatus.setStatus(_A)
_AtiStkSwQoSGroupPortCoSPriorityTable_Object=MibTable
atiStkSwQoSGroupPortCoSPriorityTable=_AtiStkSwQoSGroupPortCoSPriorityTable_Object((1,3,6,1,4,1,207,8,17,7,8))
if mibBuilder.loadTexts:atiStkSwQoSGroupPortCoSPriorityTable.setStatus(_A)
_AtiStkSwQoSGroupPortCoSPriorityEntry_Object=MibTableRow
atiStkSwQoSGroupPortCoSPriorityEntry=_AtiStkSwQoSGroupPortCoSPriorityEntry_Object((1,3,6,1,4,1,207,8,17,7,8,1))
atiStkSwQoSGroupPortCoSPriorityEntry.setIndexNames((0,_E,_AK),(0,_E,_AL))
if mibBuilder.loadTexts:atiStkSwQoSGroupPortCoSPriorityEntry.setStatus(_A)
class _AtiStkSwQoSGroupPortCoSPriorityModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwQoSGroupPortCoSPriorityModuleId_Type.__name__=_D
_AtiStkSwQoSGroupPortCoSPriorityModuleId_Object=MibTableColumn
atiStkSwQoSGroupPortCoSPriorityModuleId=_AtiStkSwQoSGroupPortCoSPriorityModuleId_Object((1,3,6,1,4,1,207,8,17,7,8,1,1),_AtiStkSwQoSGroupPortCoSPriorityModuleId_Type())
atiStkSwQoSGroupPortCoSPriorityModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQoSGroupPortCoSPriorityModuleId.setStatus(_A)
_AtiStkSwQoSGroupPortCoSPriorityPortId_Type=Integer32
_AtiStkSwQoSGroupPortCoSPriorityPortId_Object=MibTableColumn
atiStkSwQoSGroupPortCoSPriorityPortId=_AtiStkSwQoSGroupPortCoSPriorityPortId_Object((1,3,6,1,4,1,207,8,17,7,8,1,2),_AtiStkSwQoSGroupPortCoSPriorityPortId_Type())
atiStkSwQoSGroupPortCoSPriorityPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwQoSGroupPortCoSPriorityPortId.setStatus(_A)
class _AtiStkSwQoSGroupPortCoSPriorityPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AtiStkSwQoSGroupPortCoSPriorityPriority_Type.__name__=_D
_AtiStkSwQoSGroupPortCoSPriorityPriority_Object=MibTableColumn
atiStkSwQoSGroupPortCoSPriorityPriority=_AtiStkSwQoSGroupPortCoSPriorityPriority_Object((1,3,6,1,4,1,207,8,17,7,8,1,3),_AtiStkSwQoSGroupPortCoSPriorityPriority_Type())
atiStkSwQoSGroupPortCoSPriorityPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQoSGroupPortCoSPriorityPriority.setStatus(_A)
class _AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Type.__name__=_D
_AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Object=MibTableColumn
atiStkSwQoSGroupPortCoSPriorityOverridePriority=_AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Object((1,3,6,1,4,1,207,8,17,7,8,1,4),_AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Type())
atiStkSwQoSGroupPortCoSPriorityOverridePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwQoSGroupPortCoSPriorityOverridePriority.setStatus(_A)
_AtiStkSwTrunkGroup_ObjectIdentity=ObjectIdentity
atiStkSwTrunkGroup=_AtiStkSwTrunkGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,8))
_AtiStkSwStaticTrunkTable_Object=MibTable
atiStkSwStaticTrunkTable=_AtiStkSwStaticTrunkTable_Object((1,3,6,1,4,1,207,8,17,8,1))
if mibBuilder.loadTexts:atiStkSwStaticTrunkTable.setStatus(_A)
_AtiStkSwStaticTrunkEntry_Object=MibTableRow
atiStkSwStaticTrunkEntry=_AtiStkSwStaticTrunkEntry_Object((1,3,6,1,4,1,207,8,17,8,1,1))
atiStkSwStaticTrunkEntry.setIndexNames((0,_E,_AM),(0,_E,_AN))
if mibBuilder.loadTexts:atiStkSwStaticTrunkEntry.setStatus(_A)
class _AtiStkSwStaticTrunkModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwStaticTrunkModuleId_Type.__name__=_D
_AtiStkSwStaticTrunkModuleId_Object=MibTableColumn
atiStkSwStaticTrunkModuleId=_AtiStkSwStaticTrunkModuleId_Object((1,3,6,1,4,1,207,8,17,8,1,1,1),_AtiStkSwStaticTrunkModuleId_Type())
atiStkSwStaticTrunkModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwStaticTrunkModuleId.setStatus(_A)
_AtiStkSwStaticTrunkIndex_Type=Integer32
_AtiStkSwStaticTrunkIndex_Object=MibTableColumn
atiStkSwStaticTrunkIndex=_AtiStkSwStaticTrunkIndex_Object((1,3,6,1,4,1,207,8,17,8,1,1,2),_AtiStkSwStaticTrunkIndex_Type())
atiStkSwStaticTrunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwStaticTrunkIndex.setStatus(_A)
_AtiStkSwStaticTrunkId_Type=Integer32
_AtiStkSwStaticTrunkId_Object=MibTableColumn
atiStkSwStaticTrunkId=_AtiStkSwStaticTrunkId_Object((1,3,6,1,4,1,207,8,17,8,1,1,3),_AtiStkSwStaticTrunkId_Type())
atiStkSwStaticTrunkId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwStaticTrunkId.setStatus(_A)
class _AtiStkSwStaticTrunkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AtiStkSwStaticTrunkName_Type.__name__=_F
_AtiStkSwStaticTrunkName_Object=MibTableColumn
atiStkSwStaticTrunkName=_AtiStkSwStaticTrunkName_Object((1,3,6,1,4,1,207,8,17,8,1,1,4),_AtiStkSwStaticTrunkName_Type())
atiStkSwStaticTrunkName.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwStaticTrunkName.setStatus(_A)
class _AtiStkSwStaticTrunkMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('srcIp',1),('dstIp',2),('src-dstIp',3),('srcMac',4),('dstMac',5),('src-dstMac',6)))
_AtiStkSwStaticTrunkMethod_Type.__name__=_D
_AtiStkSwStaticTrunkMethod_Object=MibTableColumn
atiStkSwStaticTrunkMethod=_AtiStkSwStaticTrunkMethod_Object((1,3,6,1,4,1,207,8,17,8,1,1,5),_AtiStkSwStaticTrunkMethod_Type())
atiStkSwStaticTrunkMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwStaticTrunkMethod.setStatus(_A)
_AtiStkSwStaticTrunkPortList_Type=DisplayString
_AtiStkSwStaticTrunkPortList_Object=MibTableColumn
atiStkSwStaticTrunkPortList=_AtiStkSwStaticTrunkPortList_Object((1,3,6,1,4,1,207,8,17,8,1,1,6),_AtiStkSwStaticTrunkPortList_Type())
atiStkSwStaticTrunkPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwStaticTrunkPortList.setStatus(_A)
class _AtiStkSwStaticTrunkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AtiStkSwStaticTrunkStatus_Type.__name__=_D
_AtiStkSwStaticTrunkStatus_Object=MibTableColumn
atiStkSwStaticTrunkStatus=_AtiStkSwStaticTrunkStatus_Object((1,3,6,1,4,1,207,8,17,8,1,1,7),_AtiStkSwStaticTrunkStatus_Type())
atiStkSwStaticTrunkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwStaticTrunkStatus.setStatus(_A)
_AtiStkSwStaticTrunkRowStatus_Type=RowStatus
_AtiStkSwStaticTrunkRowStatus_Object=MibTableColumn
atiStkSwStaticTrunkRowStatus=_AtiStkSwStaticTrunkRowStatus_Object((1,3,6,1,4,1,207,8,17,8,1,1,8),_AtiStkSwStaticTrunkRowStatus_Type())
atiStkSwStaticTrunkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwStaticTrunkRowStatus.setStatus(_A)
_AtiStkSwACLGroup_ObjectIdentity=ObjectIdentity
atiStkSwACLGroup=_AtiStkSwACLGroup_ObjectIdentity((1,3,6,1,4,1,207,8,17,9))
_AtiStkSwACLConfigTable_Object=MibTable
atiStkSwACLConfigTable=_AtiStkSwACLConfigTable_Object((1,3,6,1,4,1,207,8,17,9,1))
if mibBuilder.loadTexts:atiStkSwACLConfigTable.setStatus(_A)
_AtiStkSwACLConfigEntry_Object=MibTableRow
atiStkSwACLConfigEntry=_AtiStkSwACLConfigEntry_Object((1,3,6,1,4,1,207,8,17,9,1,1))
atiStkSwACLConfigEntry.setIndexNames((0,_E,_AO),(0,_E,_AP))
if mibBuilder.loadTexts:atiStkSwACLConfigEntry.setStatus(_A)
class _AtiStkSwACLModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AtiStkSwACLModuleId_Type.__name__=_D
_AtiStkSwACLModuleId_Object=MibTableColumn
atiStkSwACLModuleId=_AtiStkSwACLModuleId_Object((1,3,6,1,4,1,207,8,17,9,1,1,1),_AtiStkSwACLModuleId_Type())
atiStkSwACLModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwACLModuleId.setStatus(_A)
class _AtiStkSwACLId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtiStkSwACLId_Type.__name__=_D
_AtiStkSwACLId_Object=MibTableColumn
atiStkSwACLId=_AtiStkSwACLId_Object((1,3,6,1,4,1,207,8,17,9,1,1,2),_AtiStkSwACLId_Type())
atiStkSwACLId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiStkSwACLId.setStatus(_A)
class _AtiStkSwACLDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AtiStkSwACLDescription_Type.__name__=_F
_AtiStkSwACLDescription_Object=MibTableColumn
atiStkSwACLDescription=_AtiStkSwACLDescription_Object((1,3,6,1,4,1,207,8,17,9,1,1,3),_AtiStkSwACLDescription_Type())
atiStkSwACLDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwACLDescription.setStatus(_A)
class _AtiStkSwACLAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('permit',2)))
_AtiStkSwACLAction_Type.__name__=_D
_AtiStkSwACLAction_Object=MibTableColumn
atiStkSwACLAction=_AtiStkSwACLAction_Object((1,3,6,1,4,1,207,8,17,9,1,1,4),_AtiStkSwACLAction_Type())
atiStkSwACLAction.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwACLAction.setStatus(_A)
_AtiStkSwACLClassifierList_Type=DisplayString
_AtiStkSwACLClassifierList_Object=MibTableColumn
atiStkSwACLClassifierList=_AtiStkSwACLClassifierList_Object((1,3,6,1,4,1,207,8,17,9,1,1,5),_AtiStkSwACLClassifierList_Type())
atiStkSwACLClassifierList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwACLClassifierList.setStatus(_A)
_AtiStkSwACLPortList_Type=DisplayString
_AtiStkSwACLPortList_Object=MibTableColumn
atiStkSwACLPortList=_AtiStkSwACLPortList_Object((1,3,6,1,4,1,207,8,17,9,1,1,6),_AtiStkSwACLPortList_Type())
atiStkSwACLPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwACLPortList.setStatus(_A)
_AtiStkSwACLRowStatus_Type=RowStatus
_AtiStkSwACLRowStatus_Object=MibTableColumn
atiStkSwACLRowStatus=_AtiStkSwACLRowStatus_Object((1,3,6,1,4,1,207,8,17,9,1,1,7),_AtiStkSwACLRowStatus_Type())
atiStkSwACLRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atiStkSwACLRowStatus.setStatus(_A)
atiStkSwFanStopTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,1))
atiStkSwFanStopTrap.setObjects((_E,_L))
if mibBuilder.loadTexts:atiStkSwFanStopTrap.setStatus(_A)
atiStkSwTemperatureAbnormalTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,2))
atiStkSwTemperatureAbnormalTrap.setObjects((_E,_L))
if mibBuilder.loadTexts:atiStkSwTemperatureAbnormalTrap.setStatus(_O)
atiStkSwIntrusionDetectionTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,3))
atiStkSwIntrusionDetectionTrap.setObjects(*((_E,_G),(_E,_H),(_E,_AQ),(_E,_AR)))
if mibBuilder.loadTexts:atiStkSwIntrusionDetectionTrap.setStatus(_A)
atiStkSwDOSTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,4))
atiStkSwDOSTrap.setObjects(*((_E,_G),(_E,_H),(_E,_W)))
if mibBuilder.loadTexts:atiStkSwDOSTrap.setStatus(_A)
atiStkSwSTPPortStateChangeTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,5))
atiStkSwSTPPortStateChangeTrap.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:atiStkSwSTPPortStateChangeTrap.setStatus(_A)
atiStkSwSTPTrunkStateChangeTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,6))
atiStkSwSTPTrunkStateChangeTrap.setObjects((_E,_L))
if mibBuilder.loadTexts:atiStkSwSTPTrunkStateChangeTrap.setStatus(_A)
atiStkSwSysRPSStateChangedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,7))
atiStkSwSysRPSStateChangedTrap.setObjects(*((_E,_L),(_E,_AS),(_E,_AT),(_E,_AU)))
if mibBuilder.loadTexts:atiStkSwSysRPSStateChangedTrap.setStatus(_A)
atiStkSwMgmtDisabledTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,15))
atiStkSwMgmtDisabledTrap.setObjects(*((_E,_AV),(_E,_AW)))
if mibBuilder.loadTexts:atiStkSwMgmtDisabledTrap.setStatus(_A)
atiStkSwTemperatureLimitTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,16))
atiStkSwTemperatureLimitTrap.setObjects(*((_E,_L),(_E,_AX)))
if mibBuilder.loadTexts:atiStkSwTemperatureLimitTrap.setStatus(_A)
atiStkSwFanOkTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,17))
atiStkSwFanOkTrap.setObjects((_E,_L))
if mibBuilder.loadTexts:atiStkSwFanOkTrap.setStatus(_A)
atiStkSwTemperatureNormalTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,18))
atiStkSwTemperatureNormalTrap.setObjects((_E,_L))
if mibBuilder.loadTexts:atiStkSwTemperatureNormalTrap.setStatus(_A)
atiStkSwHighRateStormDetectedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,19))
atiStkSwHighRateStormDetectedTrap.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:atiStkSwHighRateStormDetectedTrap.setStatus(_A)
atiStkSwWarningHighRateStormBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,20))
atiStkSwWarningHighRateStormBlockedTrap.setObjects(*((_E,_G),(_E,_H),(_E,_AY)))
if mibBuilder.loadTexts:atiStkSwWarningHighRateStormBlockedTrap.setStatus(_A)
atiStkSwRecoverHighRateStormBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,21))
atiStkSwRecoverHighRateStormBlockedTrap.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:atiStkSwRecoverHighRateStormBlockedTrap.setStatus(_A)
atiStkSwLowRateStormDetectedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,22))
atiStkSwLowRateStormDetectedTrap.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:atiStkSwLowRateStormDetectedTrap.setStatus(_A)
atiStkSwWarningLowRateStormBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,23))
atiStkSwWarningLowRateStormBlockedTrap.setObjects(*((_E,_G),(_E,_H),(_E,_AZ)))
if mibBuilder.loadTexts:atiStkSwWarningLowRateStormBlockedTrap.setStatus(_A)
atiStkSwRecoverLowRateStormBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,24))
atiStkSwRecoverLowRateStormBlockedTrap.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:atiStkSwRecoverLowRateStormBlockedTrap.setStatus(_A)
atiStkSwStackTopologyChangeTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,25))
atiStkSwStackTopologyChangeTrap.setObjects((_E,_Aa))
if mibBuilder.loadTexts:atiStkSwStackTopologyChangeTrap.setStatus(_A)
atiStkSwBPDUGuardIsTriggeredTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,26))
atiStkSwBPDUGuardIsTriggeredTrap.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:atiStkSwBPDUGuardIsTriggeredTrap.setStatus(_A)
atiStkSwLoopDetectedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,27))
atiStkSwLoopDetectedTrap.setObjects(*((_E,_G),(_E,_H),(_E,_Ab)))
if mibBuilder.loadTexts:atiStkSwLoopDetectedTrap.setStatus(_A)
atiStkSwWarningLoopBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,28))
atiStkSwWarningLoopBlockedTrap.setObjects(*((_E,_G),(_E,_H),(_E,_Ac)))
if mibBuilder.loadTexts:atiStkSwWarningLoopBlockedTrap.setStatus(_A)
atiStkSwRecoverLoopBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,17,6,29))
atiStkSwRecoverLoopBlockedTrap.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:atiStkSwRecoverLoopBlockedTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'AtiProductType':AtiProductType,'AtiPortType':AtiPortType,'AtiUplinkType':AtiUplinkType,'alliedTelesyn':alliedTelesyn,'atiProduct':atiProduct,'swhub':swhub,'at-8324':at_8324,'at-8316F':at_8316F,'at-8524M':at_8524M,'at-8550GB':at_8550GB,'at-8516F':at_8516F,'at-8550SP':at_8550SP,'at-9424T-SP':at_9424T_SP,'at-9424T-GB':at_9424T_GB,'at-8524POE':at_8524POE,'at-9408LC-SP':at_9408LC_SP,'at-9424Ti-SP':at_9424Ti_SP,'at-9448Ts-XP':at_9448Ts_XP,'at-9448Ts':at_9448Ts,'at-9448T-SP':at_9448T_SP,'at-9424Ts-XP':at_9424Ts_XP,'at-9424Ts':at_9424Ts,'at-9424T':at_9424T,'at-9424TPOE':at_9424TPOE,'at-9424TL':at_9424TL,'mibObject':mibObject,'atiStkSwMib':atiStkSwMib,'atiStkSwSysGroup':atiStkSwSysGroup,'atiStkSwSysConfig':atiStkSwSysConfig,'atiStkSwSysReset':atiStkSwSysReset,'atiStkSwSysIpAddress':atiStkSwSysIpAddress,'atiStkSwSysSubnetMask':atiStkSwSysSubnetMask,'atiStkSwSysGateway':atiStkSwSysGateway,'atiStkSwSysIpAddressStatus':atiStkSwSysIpAddressStatus,'atiStkSwSysDnsServer':atiStkSwSysDnsServer,'atiStkSwSysDefaultDomainName':atiStkSwSysDefaultDomainName,'atiStkSwSysNumberOfModules':atiStkSwSysNumberOfModules,'atiStkSwSysSpanningTreeStatus':atiStkSwSysSpanningTreeStatus,'atiStkSwSysSpanningTreeVersion':atiStkSwSysSpanningTreeVersion,'atiStkSwSysAction':atiStkSwSysAction,_Aa:atiStkSwSysNumOfModuleInStack,'atiStkSwSysNwMgmt':atiStkSwSysNwMgmt,'atiStkSwSysTrapRecv1':atiStkSwSysTrapRecv1,'atiStkSwSysTrapRecv2':atiStkSwSysTrapRecv2,'atiStkSwSysTrapRecv3':atiStkSwSysTrapRecv3,'atiStkSwSysTrapRecv4':atiStkSwSysTrapRecv4,'atiStkSwSysProductInfoTable':atiStkSwSysProductInfoTable,'atiStkSwSysProductInfoEntry':atiStkSwSysProductInfoEntry,_L:atiStkSwSysModuleId,'atiStkSwSysProductType':atiStkSwSysProductType,'atiStkSwSysMacAddress':atiStkSwSysMacAddress,'atiStkSwSysSwName':atiStkSwSysSwName,'atiStkSwSysSwVersion':atiStkSwSysSwVersion,'atiStkSwSysHwName':atiStkSwSysHwName,'atiStkSwSysHwRevision':atiStkSwSysHwRevision,'atiStkSwSysSerialNumber':atiStkSwSysSerialNumber,'atiStkSwSysTotalPortCount':atiStkSwSysTotalPortCount,'atiStkSwSysBasePortType':atiStkSwSysBasePortType,'atiStkSwSysBasePortCount':atiStkSwSysBasePortCount,'atiStkSwSysUplinkAModelName':atiStkSwSysUplinkAModelName,'atiStkSwSysUplinkAPortType':atiStkSwSysUplinkAPortType,'atiStkSwSysUplinkAPortCount':atiStkSwSysUplinkAPortCount,'atiStkSwSysUplinkAPortIdBase':atiStkSwSysUplinkAPortIdBase,'atiStkSwSysUplinkAPortIdLimit':atiStkSwSysUplinkAPortIdLimit,'atiStkSwSysUplinkBModelName':atiStkSwSysUplinkBModelName,'atiStkSwSysUplinkBPortType':atiStkSwSysUplinkBPortType,'atiStkSwSysUplinkBPortCount':atiStkSwSysUplinkBPortCount,'atiStkSwSysUplinkBPortIdBase':atiStkSwSysUplinkBPortIdBase,'atiStkSwSysUplinkBPortIdLimit':atiStkSwSysUplinkBPortIdLimit,_AS:atiStkSwSysRPSPresent,_AT:atiStkSwSysRPSState,_AU:atiStkSwSysDCState,_AX:atiStkSwSysTemperatureLimitValue,'atiStkSwSysUplinkInfoTable':atiStkSwSysUplinkInfoTable,'atiStkSwSysUplinkInfoEntry':atiStkSwSysUplinkInfoEntry,_d:atiStkSwSysUplinkModuleId,_e:atiStkSwSysUplinkPortId,'atiStkSwSysUplinkSetup':atiStkSwSysUplinkSetup,'atiStkSwSysUplinkType':atiStkSwSysUplinkType,'atiStkSwSysUplinkDetails':atiStkSwSysUplinkDetails,'atiStkSwSysUplinkPortType':atiStkSwSysUplinkPortType,'atiStkSwSysSystemTimeConfig':atiStkSwSysSystemTimeConfig,'atiStkSwSysCurrentTime':atiStkSwSysCurrentTime,'atiStkSwSysCurrentDate':atiStkSwSysCurrentDate,'atiStkSwSysSNTPStatus':atiStkSwSysSNTPStatus,'atiStkSwSysSNTPServerIPAddress':atiStkSwSysSNTPServerIPAddress,'atiStkSwSysSNTPUTCOffset':atiStkSwSysSNTPUTCOffset,'atiStkSwSysSNTPDSTStatus':atiStkSwSysSNTPDSTStatus,'atiStkSwSysSNTPPollingInterval':atiStkSwSysSNTPPollingInterval,'atiStkSwSysSNTPLastDelta':atiStkSwSysSNTPLastDelta,'atiStkSwSysInfoGroup':atiStkSwSysInfoGroup,'atiStkSwTemperatureInfoTable':atiStkSwTemperatureInfoTable,'atiStkSwTemperatureInfoEntry':atiStkSwTemperatureInfoEntry,_f:atiStkSwTemperatureInfoModuleId,'atiStkSwTemperatureInfoTemperature':atiStkSwTemperatureInfoTemperature,'atiStkSwFanInfoTable':atiStkSwFanInfoTable,'atiStkSwFanInfoEntry':atiStkSwFanInfoEntry,_g:atiStkSwFanInfoModuleId,_h:atiStkSwFanInfoFanId,'atiStkSwFanInfoState':atiStkSwFanInfoState,'atiStkSwFanInfoSpeed':atiStkSwFanInfoSpeed,'atiStkSwVoltageInfoTable':atiStkSwVoltageInfoTable,'atiStkSwVoltageInfoEntry':atiStkSwVoltageInfoEntry,_i:atiStkSwVoltageInfoModuleId,_j:atiStkSwVoltageInfoIndex,'atiStkSwVoltageInfoLevel':atiStkSwVoltageInfoLevel,'atiStkSwVoltageInfoMeasured':atiStkSwVoltageInfoMeasured,'atiStkSwCPUInfoTable':atiStkSwCPUInfoTable,'atiStkSwCPUInfoEntry':atiStkSwCPUInfoEntry,_k:atiStkSwCPUInfoModuleId,'atiStkSwCPUInfoAvgLastMinute':atiStkSwCPUInfoAvgLastMinute,'atiStkSwCPUInfoAvgLast20Seconds':atiStkSwCPUInfoAvgLast20Seconds,'atiStkSwCPUInfoAvgSecond':atiStkSwCPUInfoAvgSecond,'atiStkSwMemoryGroup':atiStkSwMemoryGroup,'atiStkSwMemoryInfoTable':atiStkSwMemoryInfoTable,'atiStkSwMemoryInfoEntry':atiStkSwMemoryInfoEntry,_l:atiStkSwMemoryInfoModuleId,'atiStkSwMemoryInfoTotalBuffers':atiStkSwMemoryInfoTotalBuffers,'atiStkSwMemoryPoolTable':atiStkSwMemoryPoolTable,'atiStkSwMemoryPoolEntry':atiStkSwMemoryPoolEntry,_m:atiStkSwMemoryPoolModuleId,_n:atiStkSwMemoryPoolIndex,'atiStkSwMemoryPoolName':atiStkSwMemoryPoolName,'atiStkSwMemoryPoolTotal':atiStkSwMemoryPoolTotal,'atiStkSwMemoryPoolFree':atiStkSwMemoryPoolFree,'atiStkSwMemoryComBuffersTable':atiStkSwMemoryComBuffersTable,'atiStkSwMemoryComBuffersEntry':atiStkSwMemoryComBuffersEntry,_o:atiStkSwMemoryComBuffersModuleId,'atiStkSwMemoryTotalComBuffers':atiStkSwMemoryTotalComBuffers,'atiStkSwMemoryFreeComBuffers':atiStkSwMemoryFreeComBuffers,'atiStkSwSysMgmtACLGroup':atiStkSwSysMgmtACLGroup,'atiStkSwSysMgmtACLStatus':atiStkSwSysMgmtACLStatus,'atiStkSwSysMgmtACLConfigTable':atiStkSwSysMgmtACLConfigTable,'atiStkSwSysMgmtACLConfigEntry':atiStkSwSysMgmtACLConfigEntry,_p:atiStkSwSysMgmtACLConfigModuleId,_q:atiStkSwSysMgmtACLConfigId,'atiStkSwSysMgmtACLConfigIpAddr':atiStkSwSysMgmtACLConfigIpAddr,'atiStkSwSysMgmtACLConfigMask':atiStkSwSysMgmtACLConfigMask,'atiStkSwSysMgmtACLConfigApplication':atiStkSwSysMgmtACLConfigApplication,'atiStkSwSysMgmtACLConfigRowStatus':atiStkSwSysMgmtACLConfigRowStatus,'atiStkSwPortGroup':atiStkSwPortGroup,'atiStkSwPortConfigTable':atiStkSwPortConfigTable,'atiStkSwPortConfigEntry':atiStkSwPortConfigEntry,_G:atiStkSwModuleId,_H:atiStkSwPortId,'atiStkSwPortName':atiStkSwPortName,'atiStkSwPortState':atiStkSwPortState,'atiStkSwPortLinkState':atiStkSwPortLinkState,'atiStkSwPortNegotiation':atiStkSwPortNegotiation,'atiStkSwPortSpeed':atiStkSwPortSpeed,'atiStkSwPortDuplexStatus':atiStkSwPortDuplexStatus,'atiStkSwPortFlowControl':atiStkSwPortFlowControl,'atiStkSwPortBackPressure':atiStkSwPortBackPressure,'atiStkSwPortPriority':atiStkSwPortPriority,'atiStkSwPortBroadcastProcessing':atiStkSwPortBroadcastProcessing,'atiStkSwPortMDIO':atiStkSwPortMDIO,'atiStkSwPortHOLLimit':atiStkSwPortHOLLimit,'atiStkSwPortBackPressureLimit':atiStkSwPortBackPressureLimit,'atiStkSwPortSTPState':atiStkSwPortSTPState,'atiStkSwPortMirroringConfig':atiStkSwPortMirroringConfig,'atiStkSwPortMirroringState':atiStkSwPortMirroringState,'atiStkSwPortMirroringSourceModuleId':atiStkSwPortMirroringSourceModuleId,'atiStkSwPortMirroringSourcePortId':atiStkSwPortMirroringSourcePortId,'atiStkSwPortMirroringDestinationModuleId':atiStkSwPortMirroringDestinationModuleId,'atiStkSwPortMirroringDestinationPortId':atiStkSwPortMirroringDestinationPortId,'atiStkSwPortMirroringSourceRxList':atiStkSwPortMirroringSourceRxList,'atiStkSwPortMirroringSourceTxList':atiStkSwPortMirroringSourceTxList,'atiStkSwPortSecurityConfig':atiStkSwPortSecurityConfig,'atiStkSwPortSecurityMode':atiStkSwPortSecurityMode,'atiStkSwPortIntrusionDetectionTable':atiStkSwPortIntrusionDetectionTable,'atiStkSwPortIntrusionDetectionEntry':atiStkSwPortIntrusionDetectionEntry,'atiStkSwPortIntrusionDetectionAction':atiStkSwPortIntrusionDetectionAction,'atiStkSwPortIntrusionDetectionPortList':atiStkSwPortIntrusionDetectionPortList,'atiStkPortSecurityConfigTable':atiStkPortSecurityConfigTable,'atiStkPortSecurityConfigEntry':atiStkPortSecurityConfigEntry,'atiStkPortSecurityMode':atiStkPortSecurityMode,'atiStkPortSecurityThreshold':atiStkPortSecurityThreshold,'atiStkPortIntrusionAction':atiStkPortIntrusionAction,'atiStkPortIntrusionActionStatus':atiStkPortIntrusionActionStatus,'atiStkDOSConfig':atiStkDOSConfig,'atiStkDOSConfigLANIpAddress':atiStkDOSConfigLANIpAddress,'atiStkDOSConfigLANSubnetMask':atiStkDOSConfigLANSubnetMask,'atiStkPortDOSAttackConfigTable':atiStkPortDOSAttackConfigTable,'atiStkPortDOSAttackConfigEntry':atiStkPortDOSAttackConfigEntry,_W:atiStkSwPortDOSAttackType,'atiStkSwPortDOSAttackActionStatus':atiStkSwPortDOSAttackActionStatus,'atiStkSwPortDOSAttackMirrorPort':atiStkSwPortDOSAttackMirrorPort,'atiStkSwPortDOSAttackMirrorPortStatus':atiStkSwPortDOSAttackMirrorPortStatus,'atiStkSwIntrusionAttackTable':atiStkSwIntrusionAttackTable,'atiStkSwIntrusionAttackEntry':atiStkSwIntrusionAttackEntry,_AQ:atiStkSwIntruderAttackVlanId,_AR:atiStkSwIntruderAttackMacAddr,'atiStkSwPortStormDetectCurrentTable':atiStkSwPortStormDetectCurrentTable,'atiStkSwPortStormDetectCurrentEntry':atiStkSwPortStormDetectCurrentEntry,'atiStkSwPortStormDetectCurrentHighStatus':atiStkSwPortStormDetectCurrentHighStatus,_AY:atiStkSwPortStormDetectCurrentHighAction,'atiStkSwPortStormDetectCurrentHighExpiry':atiStkSwPortStormDetectCurrentHighExpiry,'atiStkSwPortStormDetectCurrentLowStatus':atiStkSwPortStormDetectCurrentLowStatus,_AZ:atiStkSwPortStormDetectCurrentLowAction,'atiStkSwPortStormDetectCurrentLowExpiry':atiStkSwPortStormDetectCurrentLowExpiry,'atiStkSwPortLoopDetectCurrentTable':atiStkSwPortLoopDetectCurrentTable,'atiStkSwPortLoopDetectCurrentEntry':atiStkSwPortLoopDetectCurrentEntry,'atiStkSwPortLoopDetectCurrentStatus':atiStkSwPortLoopDetectCurrentStatus,_Ac:atiStkSwPortLoopDetectCurrentAction,'atiStkSwPortLoopDetectCurrentExpiry':atiStkSwPortLoopDetectCurrentExpiry,_Ab:atiStkSwPortLoopDetectCurrentVlanId,'atiStkSwVlanGroup':atiStkSwVlanGroup,'atiStkSwVlanConfigTable':atiStkSwVlanConfigTable,'atiStkSwVlanConfigEntry':atiStkSwVlanConfigEntry,_w:atiStkSwVlanId,'atiStkSwVlanName':atiStkSwVlanName,'atiStkSwVlanTaggedPortListModule1':atiStkSwVlanTaggedPortListModule1,'atiStkSwVlanUntaggedPortListModule1':atiStkSwVlanUntaggedPortListModule1,'atiStkSwVlanTaggedPortListModule2':atiStkSwVlanTaggedPortListModule2,'atiStkSwVlanUntaggedPortListModule2':atiStkSwVlanUntaggedPortListModule2,'atiStkSwVlanTaggedPortListModule3':atiStkSwVlanTaggedPortListModule3,'atiStkSwVlanUntaggedPortListModule3':atiStkSwVlanUntaggedPortListModule3,'atiStkSwVlanTaggedPortListModule4':atiStkSwVlanTaggedPortListModule4,'atiStkSwVlanUntaggedPortListModule4':atiStkSwVlanUntaggedPortListModule4,'atiStkSwVlanTaggedPortListModule5':atiStkSwVlanTaggedPortListModule5,'atiStkSwVlanUntaggedPortListModule5':atiStkSwVlanUntaggedPortListModule5,'atiStkSwVlanTaggedPortListModule6':atiStkSwVlanTaggedPortListModule6,'atiStkSwVlanUntaggedPortListModule6':atiStkSwVlanUntaggedPortListModule6,'atiStkSwVlanTaggedPortListModule7':atiStkSwVlanTaggedPortListModule7,'atiStkSwVlanUntaggedPortListModule7':atiStkSwVlanUntaggedPortListModule7,'atiStkSwVlanTaggedPortListModule8':atiStkSwVlanTaggedPortListModule8,'atiStkSwVlanUntaggedPortListModule8':atiStkSwVlanUntaggedPortListModule8,'atiStkSwVlanConfigEntryStatus':atiStkSwVlanConfigEntryStatus,'atiStkSwVlanActualUntaggedPortListModule1':atiStkSwVlanActualUntaggedPortListModule1,'atiStkSwPort2VlanTable':atiStkSwPort2VlanTable,'atiStkSwPort2VlanEntry':atiStkSwPort2VlanEntry,'atiStkSwPortVlanId':atiStkSwPortVlanId,'atiStkSwPortVlanName':atiStkSwPortVlanName,'atiStkSwMacAddr2VlanTable':atiStkSwMacAddr2VlanTable,'atiStkSwMacAddr2VlanEntry':atiStkSwMacAddr2VlanEntry,_x:atiStkSwMacAddress,_y:atiStkSwMacAddrVlanId,'atiStkSwMacAddrVlanName':atiStkSwMacAddrVlanName,'atiStkSwMacAddrModuleId':atiStkSwMacAddrModuleId,'atiStkSwMacAddrPortId':atiStkSwMacAddrPortId,'atiStkSwMacAddrPortList':atiStkSwMacAddrPortList,'atiStkSwVlanMode':atiStkSwVlanMode,'atiStkSwVlanUplinkVlanPort':atiStkSwVlanUplinkVlanPort,'atiStkSwGVRPConfig':atiStkSwGVRPConfig,'atiStkSwGVRPStatus':atiStkSwGVRPStatus,'atiStkSwGVRPGIPStatus':atiStkSwGVRPGIPStatus,'atiStkSwGVRPJoinTimer':atiStkSwGVRPJoinTimer,'atiStkSwGVRPLeaveTimer':atiStkSwGVRPLeaveTimer,'atiStkSwGVRPLeaveAllTimer':atiStkSwGVRPLeaveAllTimer,'atiStkSwGVRPPortConfigTable':atiStkSwGVRPPortConfigTable,'atiStkSwGVRPPortConfigEntry':atiStkSwGVRPPortConfigEntry,_z:atiStkSwGVRPPortConfigModuleId,_A0:atiStkSwGVRPPortConfigPortId,'atiStkSwGVRPPortConfigStatus':atiStkSwGVRPPortConfigStatus,'atiStkSwGVRPCountersTable':atiStkSwGVRPCountersTable,'atiStkSwGVRPCountersEntry':atiStkSwGVRPCountersEntry,_A1:atiStkSwGVRPCountersModuleId,'atiStkSwGVRPCountersGARPRxPkt':atiStkSwGVRPCountersGARPRxPkt,'atiStkSwGVRPCountersInvalidGARPRxPkt':atiStkSwGVRPCountersInvalidGARPRxPkt,'atiStkSwGVRPCountersGARPTxPkt':atiStkSwGVRPCountersGARPTxPkt,'atiStkSwGVRPCountersGARPTxDisabled':atiStkSwGVRPCountersGARPTxDisabled,'atiStkSwGVRPCountersPortNotSending':atiStkSwGVRPCountersPortNotSending,'atiStkSwGVRPCountersGARPDisabled':atiStkSwGVRPCountersGARPDisabled,'atiStkSwGVRPCountersPortNotListening':atiStkSwGVRPCountersPortNotListening,'atiStkSwGVRPCountersInvalidPort':atiStkSwGVRPCountersInvalidPort,'atiStkSwGVRPCountersInvalidProtocol':atiStkSwGVRPCountersInvalidProtocol,'atiStkSwGVRPCountersInvalidFormat':atiStkSwGVRPCountersInvalidFormat,'atiStkSwGVRPCountersDatabaseFull':atiStkSwGVRPCountersDatabaseFull,'atiStkSwGVRPCountersRxMsgLeaveAll':atiStkSwGVRPCountersRxMsgLeaveAll,'atiStkSwGVRPCountersRxMsgJoinEmpty':atiStkSwGVRPCountersRxMsgJoinEmpty,'atiStkSwGVRPCountersRxMsgJoinIn':atiStkSwGVRPCountersRxMsgJoinIn,'atiStkSwGVRPCountersRxMsgLeaveEmpty':atiStkSwGVRPCountersRxMsgLeaveEmpty,'atiStkSwGVRPCountersRxMsgLeaveIn':atiStkSwGVRPCountersRxMsgLeaveIn,'atiStkSwGVRPCountersRxMsgEmpty':atiStkSwGVRPCountersRxMsgEmpty,'atiStkSwGVRPCountersRxMsgBadMsg':atiStkSwGVRPCountersRxMsgBadMsg,'atiStkSwGVRPCountersRxMsgBadAttribute':atiStkSwGVRPCountersRxMsgBadAttribute,'atiStkSwGVRPCountersTxMsgLeaveAll':atiStkSwGVRPCountersTxMsgLeaveAll,'atiStkSwGVRPCountersTxMsgJoinEmpty':atiStkSwGVRPCountersTxMsgJoinEmpty,'atiStkSwGVRPCountersTxMsgJoinIn':atiStkSwGVRPCountersTxMsgJoinIn,'atiStkSwGVRPCountersTxMsgLeaveEmpty':atiStkSwGVRPCountersTxMsgLeaveEmpty,'atiStkSwGVRPCountersTxMsgLeaveIn':atiStkSwGVRPCountersTxMsgLeaveIn,'atiStkSwGVRPCountersTxMsgEmpty':atiStkSwGVRPCountersTxMsgEmpty,'atiStkSwMacAddrGroup':atiStkSwMacAddrGroup,'atiStkSwStaticMacAddrTable':atiStkSwStaticMacAddrTable,'atiStkSwStaticMacAddrEntry':atiStkSwStaticMacAddrEntry,_A2:atiStkSwStaticMacAddress,_A3:atiStkSwStaticMacAddrVlanId,'atiStkSwStaticMacAddrModuleId':atiStkSwStaticMacAddrModuleId,'atiStkSwStaticMacAddrPortId':atiStkSwStaticMacAddrPortId,'atiStkSwStaticMacAddrPortList':atiStkSwStaticMacAddrPortList,'atiStkSwStaticMacAddrEntryStatus':atiStkSwStaticMacAddrEntryStatus,'atiStkSwEthStatsGroup':atiStkSwEthStatsGroup,'atiStkSwEthModuleMonTable':atiStkSwEthModuleMonTable,'atiStkSwEthModuleMonEntry':atiStkSwEthModuleMonEntry,'atiStkSwEthModuleMonTxGoodFrames':atiStkSwEthModuleMonTxGoodFrames,'atiStkSwEthModuleMonRxGoodFrames':atiStkSwEthModuleMonRxGoodFrames,'atiStkSwEthModuleMonTxTotalBytes':atiStkSwEthModuleMonTxTotalBytes,'atiStkSwEthModuleMonTxBroadcastFrames':atiStkSwEthModuleMonTxBroadcastFrames,'atiStkSwEthModuleMonTxMulticastFrames':atiStkSwEthModuleMonTxMulticastFrames,'atiStkSwEthModuleMonRxOverrunFrames':atiStkSwEthModuleMonRxOverrunFrames,'atiStkSwEthModuleErrTable':atiStkSwEthModuleErrTable,'atiStkSwEthModuleErrEntry':atiStkSwEthModuleErrEntry,'atiStkSwEthModuleErrRxCRC':atiStkSwEthModuleErrRxCRC,'atiStkSwEthModuleErrRxBadFrames':atiStkSwEthModuleErrRxBadFrames,'atiStkSwEthModuleErrCollisions':atiStkSwEthModuleErrCollisions,'atiStkSwEthPortMonTable':atiStkSwEthPortMonTable,'atiStkSwEthPortMonEntry':atiStkSwEthPortMonEntry,'atiStkSwEthPortMonTxGoodFrames':atiStkSwEthPortMonTxGoodFrames,'atiStkSwEthPortMonRxGoodFrames':atiStkSwEthPortMonRxGoodFrames,'atiStkSwEthPortMonTxTotalBytes':atiStkSwEthPortMonTxTotalBytes,'atiStkSwEthPortMonTxBroadcastFrames':atiStkSwEthPortMonTxBroadcastFrames,'atiStkSwEthPortMonTxMulticastFrames':atiStkSwEthPortMonTxMulticastFrames,'atiStkSwEthPortMonRxOverrunFrames':atiStkSwEthPortMonRxOverrunFrames,'atiStkSwEthPortErrTable':atiStkSwEthPortErrTable,'atiStkSwEthPortErrEntry':atiStkSwEthPortErrEntry,'atiStkSwEthPortErrRxBadFrames':atiStkSwEthPortErrRxBadFrames,'atiStkSwEthPortErrCollisions':atiStkSwEthPortErrCollisions,'atiStkSwTrapsGroup':atiStkSwTrapsGroup,'atiStkSwFanStopTrap':atiStkSwFanStopTrap,'atiStkSwTemperatureAbnormalTrap':atiStkSwTemperatureAbnormalTrap,'atiStkSwIntrusionDetectionTrap':atiStkSwIntrusionDetectionTrap,'atiStkSwDOSTrap':atiStkSwDOSTrap,'atiStkSwSTPPortStateChangeTrap':atiStkSwSTPPortStateChangeTrap,'atiStkSwSTPTrunkStateChangeTrap':atiStkSwSTPTrunkStateChangeTrap,'atiStkSwSysRPSStateChangedTrap':atiStkSwSysRPSStateChangedTrap,_AV:atiStkSwTrapVarMgmtType,_AW:atiStkSwTrapVarMgmtIpAddr,'atiStkSwMgmtDisabledTrap':atiStkSwMgmtDisabledTrap,'atiStkSwTemperatureLimitTrap':atiStkSwTemperatureLimitTrap,'atiStkSwFanOkTrap':atiStkSwFanOkTrap,'atiStkSwTemperatureNormalTrap':atiStkSwTemperatureNormalTrap,'atiStkSwHighRateStormDetectedTrap':atiStkSwHighRateStormDetectedTrap,'atiStkSwWarningHighRateStormBlockedTrap':atiStkSwWarningHighRateStormBlockedTrap,'atiStkSwRecoverHighRateStormBlockedTrap':atiStkSwRecoverHighRateStormBlockedTrap,'atiStkSwLowRateStormDetectedTrap':atiStkSwLowRateStormDetectedTrap,'atiStkSwWarningLowRateStormBlockedTrap':atiStkSwWarningLowRateStormBlockedTrap,'atiStkSwRecoverLowRateStormBlockedTrap':atiStkSwRecoverLowRateStormBlockedTrap,'atiStkSwStackTopologyChangeTrap':atiStkSwStackTopologyChangeTrap,'atiStkSwBPDUGuardIsTriggeredTrap':atiStkSwBPDUGuardIsTriggeredTrap,'atiStkSwLoopDetectedTrap':atiStkSwLoopDetectedTrap,'atiStkSwWarningLoopBlockedTrap':atiStkSwWarningLoopBlockedTrap,'atiStkSwRecoverLoopBlockedTrap':atiStkSwRecoverLoopBlockedTrap,'atiStkSwQoSGroup':atiStkSwQoSGroup,'atiStkSwQoSGroupNumberOfQueues':atiStkSwQoSGroupNumberOfQueues,'atiStkSwQoSGroupSchedulingMode':atiStkSwQoSGroupSchedulingMode,'atiStkSwQoSGroupCoSToQueueTable':atiStkSwQoSGroupCoSToQueueTable,'atiStkSwQoSGroupCoSToQueueEntry':atiStkSwQoSGroupCoSToQueueEntry,_A4:atiStkSwQoSGroupCoSPriority,'atiStkSwQoSGroupCoSQueue':atiStkSwQoSGroupCoSQueue,'atiStkSwQoSGroupQueueToWeightTable':atiStkSwQoSGroupQueueToWeightTable,'atiStkSwQoSGroupQueueToWeightEntry':atiStkSwQoSGroupQueueToWeightEntry,_AD:atiStkSwQoSGroupQueue,'atiStkSwQoSGroupQueueWeight':atiStkSwQoSGroupQueueWeight,'atiStkSwQosFlowGrpTable':atiStkSwQosFlowGrpTable,'atiStkSwQosFlowGrpEntry':atiStkSwQosFlowGrpEntry,_AE:atiStkSwQosFlowGrpModuleId,_AF:atiStkSwQosFlowGrpId,'atiStkSwQosFlowGrpDescription':atiStkSwQosFlowGrpDescription,'atiStkSwQosFlowGrpDSCPValue':atiStkSwQosFlowGrpDSCPValue,'atiStkSwQosFlowGrpPriority':atiStkSwQosFlowGrpPriority,'atiStkSwQosFlowGrpRemarkPriority':atiStkSwQosFlowGrpRemarkPriority,'atiStkSwQosFlowGrpTos':atiStkSwQosFlowGrpTos,'atiStkSwQosFlowGrpTosToPriority':atiStkSwQosFlowGrpTosToPriority,'atiStkSwQosFlowGrpPriorityToTos':atiStkSwQosFlowGrpPriorityToTos,'atiStkSwQosFlowGrpClassifierList':atiStkSwQosFlowGrpClassifierList,'atiStkSwQosFlowGrpRowStatus':atiStkSwQosFlowGrpRowStatus,'atiStkSwQosTrafficClassTable':atiStkSwQosTrafficClassTable,'atiStkSwQosTrafficClassEntry':atiStkSwQosTrafficClassEntry,_AG:atiStkSwQosTrafficClassModuleId,_AH:atiStkSwQosTrafficClassId,'atiStkSwQosTrafficClassDescription':atiStkSwQosTrafficClassDescription,'atiStkSwQosTrafficClassExceedAction':atiStkSwQosTrafficClassExceedAction,'atiStkSwQosTrafficClassExceedRemarkValue':atiStkSwQosTrafficClassExceedRemarkValue,'atiStkSwQosTrafficClassDSCPValue':atiStkSwQosTrafficClassDSCPValue,'atiStkSwQosTrafficClassMaxBandwidth':atiStkSwQosTrafficClassMaxBandwidth,'atiStkSwQosTrafficClassBurstSize':atiStkSwQosTrafficClassBurstSize,'atiStkSwQosTrafficClassPriority':atiStkSwQosTrafficClassPriority,'atiStkSwQosTrafficClassRemarkPriority':atiStkSwQosTrafficClassRemarkPriority,'atiStkSwQosTrafficClassToS':atiStkSwQosTrafficClassToS,'atiStkSwQosTrafficClassMoveToSToPriority':atiStkSwQosTrafficClassMoveToSToPriority,'atiStkSwQosTrafficClassMovePriorityToToS':atiStkSwQosTrafficClassMovePriorityToToS,'atiStkSwQosTrafficClassFlowGroupList':atiStkSwQosTrafficClassFlowGroupList,'atiStkSwQosTrafficClassRowStatus':atiStkSwQosTrafficClassRowStatus,'atiStkSwQosPolicyTable':atiStkSwQosPolicyTable,'atiStkSwQosPolicyEntry':atiStkSwQosPolicyEntry,_AI:atiStkSwQosPolicyModuleId,_AJ:atiStkSwQosPolicyId,'atiStkSwQosPolicyDescription':atiStkSwQosPolicyDescription,'atiStkSwQosPolicyRemarkDSCP':atiStkSwQosPolicyRemarkDSCP,'atiStkSwQosPolicyDSCPValue':atiStkSwQosPolicyDSCPValue,'atiStkSwQosPolicyToS':atiStkSwQosPolicyToS,'atiStkSwQosPolicyMoveToSToPriority':atiStkSwQosPolicyMoveToSToPriority,'atiStkSwQosPolicyMovePriorityToToS':atiStkSwQosPolicyMovePriorityToToS,'atiStkSwQosPolicySendToMirrorPort':atiStkSwQosPolicySendToMirrorPort,'atiStkSwQosPolicyTrafficClassList':atiStkSwQosPolicyTrafficClassList,'atiStkSwQosPolicyRedirectPort':atiStkSwQosPolicyRedirectPort,'atiStkSwQosPolicyIngressPortList':atiStkSwQosPolicyIngressPortList,'atiStkSwQosPolicyEgressPortList':atiStkSwQosPolicyEgressPortList,'atiStkSwQosPolicyRowStatus':atiStkSwQosPolicyRowStatus,'atiStkSwQoSGroupPortCoSPriorityTable':atiStkSwQoSGroupPortCoSPriorityTable,'atiStkSwQoSGroupPortCoSPriorityEntry':atiStkSwQoSGroupPortCoSPriorityEntry,_AK:atiStkSwQoSGroupPortCoSPriorityModuleId,_AL:atiStkSwQoSGroupPortCoSPriorityPortId,'atiStkSwQoSGroupPortCoSPriorityPriority':atiStkSwQoSGroupPortCoSPriorityPriority,'atiStkSwQoSGroupPortCoSPriorityOverridePriority':atiStkSwQoSGroupPortCoSPriorityOverridePriority,'atiStkSwTrunkGroup':atiStkSwTrunkGroup,'atiStkSwStaticTrunkTable':atiStkSwStaticTrunkTable,'atiStkSwStaticTrunkEntry':atiStkSwStaticTrunkEntry,_AM:atiStkSwStaticTrunkModuleId,_AN:atiStkSwStaticTrunkIndex,'atiStkSwStaticTrunkId':atiStkSwStaticTrunkId,'atiStkSwStaticTrunkName':atiStkSwStaticTrunkName,'atiStkSwStaticTrunkMethod':atiStkSwStaticTrunkMethod,'atiStkSwStaticTrunkPortList':atiStkSwStaticTrunkPortList,'atiStkSwStaticTrunkStatus':atiStkSwStaticTrunkStatus,'atiStkSwStaticTrunkRowStatus':atiStkSwStaticTrunkRowStatus,'atiStkSwACLGroup':atiStkSwACLGroup,'atiStkSwACLConfigTable':atiStkSwACLConfigTable,'atiStkSwACLConfigEntry':atiStkSwACLConfigEntry,_AO:atiStkSwACLModuleId,_AP:atiStkSwACLId,'atiStkSwACLDescription':atiStkSwACLDescription,'atiStkSwACLAction':atiStkSwACLAction,'atiStkSwACLClassifierList':atiStkSwACLClassifierList,'atiStkSwACLPortList':atiStkSwACLPortList,'atiStkSwACLRowStatus':atiStkSwACLRowStatus})