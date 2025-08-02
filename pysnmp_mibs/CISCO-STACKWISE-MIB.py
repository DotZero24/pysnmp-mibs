_Ag='cswDistrStackPhyPortStatusGroup'
_Af='cswDistrStackLinkStatusGroup'
_Ae='cswStatusGroupRev2'
_Ad='cswStatusGroup'
_Ac='cswStackMemberToBeReloadedForUpgrade'
_Ab='cswStackPowerSSLS'
_Aa='cswStackPowerSRLS'
_AZ='cswStackPowerILS'
_AY='cswStackPowerGLS'
_AX='cswStackPowerUnderVoltage'
_AW='cswStackPowerPriorityConflict'
_AV='cswStackPowerInsufficientPower'
_AU='cswStackPowerUnbalancedPowerSupplies'
_AT='cswStackPowerUnderBudget'
_AS='cswStackPowerInvalidOutputCurrent'
_AR='cswStackPowerInvalidInputCurrent'
_AQ='cscwStackPowerBudgetWarrning'
_AP='cswStackPowerInvalidTopology'
_AO='cswStackPowerVersionMismatch'
_AN='cswStackPowerPortOperStatusChanged'
_AM='cswStackPowerPortLinkStatusChanged'
_AL='cswStackMemberRemoved'
_AK='cswStackNewMember'
_AJ='cswStackRingRedundant'
_AI='cswStackMismatch'
_AH='cswStackNewMaster'
_AG='cswStackPortChange'
_AF='cswDistrStackPhyPortNbrsw'
_AE='cswDistrStackPhyPortNbr'
_AD='cswDistrStackPhyPortOperStatus'
_AC='cswDistrStackPhyPort'
_AB='cswDistrStackLinkBundleOperStatus'
_AA='cswStackBandWidth'
_A9='cswStackType'
_A8='cswStackDomainNum'
_A7='cswSwitchPowerAllocated'
_A6='cswEnableIndividualStackNotifications'
_A5='cswStackPowerPortNeighborSwitchNum'
_A4='cswStackPowerPortNeighborMacAddress'
_A3='cswSwitchPoeDevicesHighPriority'
_A2='cswSwitchPoeDevicesLowPriority'
_A1='cswSwitchSystemPowerPriority'
_A0='cswSwitchPowerCommited'
_z='cswSwitchPowerBudget'
_y='cswStackPowerNumMembers'
_x='cswStackPowerMasterSwitchNum'
_w='cswStackPowerMasterMacAddress'
_v='cswStackPowerMode'
_u='cswStackPortNeighbor'
_t='cswEnableStackNotifications'
_s='cswStackPowerPortIndex'
_r='cswStackPowerStackNumber'
_q='Unsigned32'
_p='cswStackPowerAllocatedGroup'
_o='cswStackPowerPortLinkStatus'
_n='cswStackPowerPortOperStatus'
_m='cswStackPowerType'
_l='cswStackPortOperStatus'
_k='cswSwitchSoftwareImage'
_j='not-accessible'
_i='cswDSLindex'
_h='Watts'
_g='cswNotificationGroupSup1'
_f='cswStatusGroupRev1'
_e='cswStackPowerPortOverCurrentThreshold'
_d='cswSwitchMacAddress'
_c='cswSwitchHwPriority'
_b='cswSwitchSwPriority'
_a='cswSwitchRole'
_Z='cswSwitchNumNextReload'
_Y='cswMaxSwitchConfigPriority'
_X='cswMaxSwitchNum'
_W='down'
_V='up'
_U='ifIndex'
_T='IF-MIB'
_S='cswStackPowerNotificationGroup'
_R='cswStackPowerPortStatusGroup'
_Q='cswStackPowerSwitchStatusGroup'
_P='cswStackPowerStatusGroup'
_O='cswStackPowerEnableNotificationGroup'
_N='cswStackPowerName'
_M='cswSwitchState'
_L='cswRingRedundant'
_K='entPhysicalIndex'
_J='ENTITY-MIB'
_I='cswNotificationGroup'
_H='cswStackPowerPortName'
_G='deprecated'
_F='Integer32'
_E='read-write'
_D='cswSwitchNumCurrent'
_C='read-only'
_B='current'
_A='CISCO-STACKWISE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
entPhysicalIndex,=mibBuilder.importSymbols(_J,_K)
ifIndex,=mibBuilder.importSymbols(_T,_U)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_q,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ciscoStackWiseMIB=ModuleIdentity((1,3,6,1,4,1,9,9,500))
if mibBuilder.loadTexts:ciscoStackWiseMIB.setRevisions(('2016-04-16 00:00','2015-11-24 00:00','2011-12-12 00:00','2010-02-01 00:00','2008-06-10 00:00','2005-10-12 00:00'))
class CswPowerStackMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('powerSharing',1),('redundant',2),('powerSharingStrict',3),('redundantStrict',4)))
class CswPowerStackType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ring',1),('star',2)))
class CswSwitchNumber(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CswSwitchNumberOrZero(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class CswSwitchPriority(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiscoStackWiseMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoStackWiseMIBNotifs=_CiscoStackWiseMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,500,0))
_CswMIBNotifications_ObjectIdentity=ObjectIdentity
cswMIBNotifications=_CswMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,500,0,0))
_CiscoStackWiseMIBObjects_ObjectIdentity=ObjectIdentity
ciscoStackWiseMIBObjects=_CiscoStackWiseMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,500,1))
_CswGlobals_ObjectIdentity=ObjectIdentity
cswGlobals=_CswGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,500,1,1))
_CswMaxSwitchNum_Type=CswSwitchNumber
_CswMaxSwitchNum_Object=MibScalar
cswMaxSwitchNum=_CswMaxSwitchNum_Object((1,3,6,1,4,1,9,9,500,1,1,1),_CswMaxSwitchNum_Type())
cswMaxSwitchNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cswMaxSwitchNum.setStatus(_B)
_CswMaxSwitchConfigPriority_Type=CswSwitchPriority
_CswMaxSwitchConfigPriority_Object=MibScalar
cswMaxSwitchConfigPriority=_CswMaxSwitchConfigPriority_Object((1,3,6,1,4,1,9,9,500,1,1,2),_CswMaxSwitchConfigPriority_Type())
cswMaxSwitchConfigPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cswMaxSwitchConfigPriority.setStatus(_B)
_CswRingRedundant_Type=TruthValue
_CswRingRedundant_Object=MibScalar
cswRingRedundant=_CswRingRedundant_Object((1,3,6,1,4,1,9,9,500,1,1,3),_CswRingRedundant_Type())
cswRingRedundant.setMaxAccess(_C)
if mibBuilder.loadTexts:cswRingRedundant.setStatus(_B)
_CswEnableStackNotifications_Type=TruthValue
_CswEnableStackNotifications_Object=MibScalar
cswEnableStackNotifications=_CswEnableStackNotifications_Object((1,3,6,1,4,1,9,9,500,1,1,4),_CswEnableStackNotifications_Type())
cswEnableStackNotifications.setMaxAccess(_E)
if mibBuilder.loadTexts:cswEnableStackNotifications.setStatus(_G)
class _CswEnableIndividualStackNotifications_Type(Bits):namedValues=NamedValues(*(('stackPortChange',0),('stackNewMaster',1),('stackMismatch',2),('stackRingRedundant',3),('stackNewMember',4),('stackMemberRemoved',5),('stackPowerLinkStatusChanged',6),('stackPowerPortOperStatusChanged',7),('stackPowerVersionMismatch',8),('stackPowerInvalidTopology',9),('stackPowerBudgetWarning',10),('stackPowerInvalidInputCurrent',11),('stackPowerInvalidOutputCurrent',12),('stackPowerUnderBudget',13),('stackPowerUnbalancedPowerSupplies',14),('stackPowerInsufficientPower',15),('stackPowerPriorityConflict',16),('stackPowerUnderVoltage',17),('stackPowerGLS',18),('stackPowerILS',19),('stackPowerSRLS',20),('stackPowerSSLS',21),('stackMemberToBeReloadedForUpgrade',22)))
_CswEnableIndividualStackNotifications_Type.__name__='Bits'
_CswEnableIndividualStackNotifications_Object=MibScalar
cswEnableIndividualStackNotifications=_CswEnableIndividualStackNotifications_Object((1,3,6,1,4,1,9,9,500,1,1,5),_CswEnableIndividualStackNotifications_Type())
cswEnableIndividualStackNotifications.setMaxAccess(_E)
if mibBuilder.loadTexts:cswEnableIndividualStackNotifications.setStatus(_B)
_CswStackDomainNum_Type=Unsigned32
_CswStackDomainNum_Object=MibScalar
cswStackDomainNum=_CswStackDomainNum_Object((1,3,6,1,4,1,9,9,500,1,1,6),_CswStackDomainNum_Type())
cswStackDomainNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackDomainNum.setStatus(_B)
_CswStackType_Type=Unsigned32
_CswStackType_Object=MibScalar
cswStackType=_CswStackType_Object((1,3,6,1,4,1,9,9,500,1,1,7),_CswStackType_Type())
cswStackType.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackType.setStatus(_B)
_CswStackBandWidth_Type=Unsigned32
_CswStackBandWidth_Object=MibScalar
cswStackBandWidth=_CswStackBandWidth_Object((1,3,6,1,4,1,9,9,500,1,1,8),_CswStackBandWidth_Type())
cswStackBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackBandWidth.setStatus(_B)
_CswStackInfo_ObjectIdentity=ObjectIdentity
cswStackInfo=_CswStackInfo_ObjectIdentity((1,3,6,1,4,1,9,9,500,1,2))
_CswSwitchInfoTable_Object=MibTable
cswSwitchInfoTable=_CswSwitchInfoTable_Object((1,3,6,1,4,1,9,9,500,1,2,1))
if mibBuilder.loadTexts:cswSwitchInfoTable.setStatus(_B)
_CswSwitchInfoEntry_Object=MibTableRow
cswSwitchInfoEntry=_CswSwitchInfoEntry_Object((1,3,6,1,4,1,9,9,500,1,2,1,1))
cswSwitchInfoEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cswSwitchInfoEntry.setStatus(_B)
_CswSwitchNumCurrent_Type=CswSwitchNumber
_CswSwitchNumCurrent_Object=MibTableColumn
cswSwitchNumCurrent=_CswSwitchNumCurrent_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,1),_CswSwitchNumCurrent_Type())
cswSwitchNumCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchNumCurrent.setStatus(_B)
_CswSwitchNumNextReload_Type=CswSwitchNumberOrZero
_CswSwitchNumNextReload_Object=MibTableColumn
cswSwitchNumNextReload=_CswSwitchNumNextReload_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,2),_CswSwitchNumNextReload_Type())
cswSwitchNumNextReload.setMaxAccess(_E)
if mibBuilder.loadTexts:cswSwitchNumNextReload.setStatus(_B)
class _CswSwitchRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('master',1),('member',2),('notMember',3),('standby',4)))
_CswSwitchRole_Type.__name__=_F
_CswSwitchRole_Object=MibTableColumn
cswSwitchRole=_CswSwitchRole_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,3),_CswSwitchRole_Type())
cswSwitchRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchRole.setStatus(_B)
_CswSwitchSwPriority_Type=CswSwitchPriority
_CswSwitchSwPriority_Object=MibTableColumn
cswSwitchSwPriority=_CswSwitchSwPriority_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,4),_CswSwitchSwPriority_Type())
cswSwitchSwPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cswSwitchSwPriority.setStatus(_B)
_CswSwitchHwPriority_Type=CswSwitchPriority
_CswSwitchHwPriority_Object=MibTableColumn
cswSwitchHwPriority=_CswSwitchHwPriority_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,5),_CswSwitchHwPriority_Type())
cswSwitchHwPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchHwPriority.setStatus(_B)
class _CswSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('waiting',1),('progressing',2),('added',3),('ready',4),('sdmMismatch',5),('verMismatch',6),('featureMismatch',7),('newMasterInit',8),('provisioned',9),('invalid',10),('removed',11)))
_CswSwitchState_Type.__name__=_F
_CswSwitchState_Object=MibTableColumn
cswSwitchState=_CswSwitchState_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,6),_CswSwitchState_Type())
cswSwitchState.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchState.setStatus(_B)
_CswSwitchMacAddress_Type=MacAddress
_CswSwitchMacAddress_Object=MibTableColumn
cswSwitchMacAddress=_CswSwitchMacAddress_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,7),_CswSwitchMacAddress_Type())
cswSwitchMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchMacAddress.setStatus(_B)
_CswSwitchSoftwareImage_Type=SnmpAdminString
_CswSwitchSoftwareImage_Object=MibTableColumn
cswSwitchSoftwareImage=_CswSwitchSoftwareImage_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,8),_CswSwitchSoftwareImage_Type())
cswSwitchSoftwareImage.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchSoftwareImage.setStatus(_B)
_CswSwitchPowerBudget_Type=Unsigned32
_CswSwitchPowerBudget_Object=MibTableColumn
cswSwitchPowerBudget=_CswSwitchPowerBudget_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,9),_CswSwitchPowerBudget_Type())
cswSwitchPowerBudget.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchPowerBudget.setStatus(_B)
if mibBuilder.loadTexts:cswSwitchPowerBudget.setUnits(_h)
_CswSwitchPowerCommited_Type=Unsigned32
_CswSwitchPowerCommited_Object=MibTableColumn
cswSwitchPowerCommited=_CswSwitchPowerCommited_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,10),_CswSwitchPowerCommited_Type())
cswSwitchPowerCommited.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchPowerCommited.setStatus(_B)
if mibBuilder.loadTexts:cswSwitchPowerCommited.setUnits(_h)
_CswSwitchSystemPowerPriority_Type=Unsigned32
_CswSwitchSystemPowerPriority_Object=MibTableColumn
cswSwitchSystemPowerPriority=_CswSwitchSystemPowerPriority_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,11),_CswSwitchSystemPowerPriority_Type())
cswSwitchSystemPowerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cswSwitchSystemPowerPriority.setStatus(_B)
_CswSwitchPoeDevicesLowPriority_Type=Unsigned32
_CswSwitchPoeDevicesLowPriority_Object=MibTableColumn
cswSwitchPoeDevicesLowPriority=_CswSwitchPoeDevicesLowPriority_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,12),_CswSwitchPoeDevicesLowPriority_Type())
cswSwitchPoeDevicesLowPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cswSwitchPoeDevicesLowPriority.setStatus(_B)
_CswSwitchPoeDevicesHighPriority_Type=Unsigned32
_CswSwitchPoeDevicesHighPriority_Object=MibTableColumn
cswSwitchPoeDevicesHighPriority=_CswSwitchPoeDevicesHighPriority_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,13),_CswSwitchPoeDevicesHighPriority_Type())
cswSwitchPoeDevicesHighPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cswSwitchPoeDevicesHighPriority.setStatus(_B)
_CswSwitchPowerAllocated_Type=Unsigned32
_CswSwitchPowerAllocated_Object=MibTableColumn
cswSwitchPowerAllocated=_CswSwitchPowerAllocated_Object((1,3,6,1,4,1,9,9,500,1,2,1,1,14),_CswSwitchPowerAllocated_Type())
cswSwitchPowerAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:cswSwitchPowerAllocated.setStatus(_B)
if mibBuilder.loadTexts:cswSwitchPowerAllocated.setUnits(_h)
_CswStackPortInfoTable_Object=MibTable
cswStackPortInfoTable=_CswStackPortInfoTable_Object((1,3,6,1,4,1,9,9,500,1,2,2))
if mibBuilder.loadTexts:cswStackPortInfoTable.setStatus(_B)
_CswStackPortInfoEntry_Object=MibTableRow
cswStackPortInfoEntry=_CswStackPortInfoEntry_Object((1,3,6,1,4,1,9,9,500,1,2,2,1))
cswStackPortInfoEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:cswStackPortInfoEntry.setStatus(_B)
class _CswStackPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),('forcedDown',3)))
_CswStackPortOperStatus_Type.__name__=_F
_CswStackPortOperStatus_Object=MibTableColumn
cswStackPortOperStatus=_CswStackPortOperStatus_Object((1,3,6,1,4,1,9,9,500,1,2,2,1,1),_CswStackPortOperStatus_Type())
cswStackPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPortOperStatus.setStatus(_B)
_CswStackPortNeighbor_Type=EntPhysicalIndexOrZero
_CswStackPortNeighbor_Object=MibTableColumn
cswStackPortNeighbor=_CswStackPortNeighbor_Object((1,3,6,1,4,1,9,9,500,1,2,2,1,2),_CswStackPortNeighbor_Type())
cswStackPortNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPortNeighbor.setStatus(_B)
_CswDistrStackLinkInfoTable_Object=MibTable
cswDistrStackLinkInfoTable=_CswDistrStackLinkInfoTable_Object((1,3,6,1,4,1,9,9,500,1,2,3))
if mibBuilder.loadTexts:cswDistrStackLinkInfoTable.setStatus(_B)
_CswDistrStackLinkInfoEntry_Object=MibTableRow
cswDistrStackLinkInfoEntry=_CswDistrStackLinkInfoEntry_Object((1,3,6,1,4,1,9,9,500,1,2,3,1))
cswDistrStackLinkInfoEntry.setIndexNames((0,_J,_K),(0,_A,_i))
if mibBuilder.loadTexts:cswDistrStackLinkInfoEntry.setStatus(_B)
class _CswDSLindex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CswDSLindex_Type.__name__=_q
_CswDSLindex_Object=MibTableColumn
cswDSLindex=_CswDSLindex_Object((1,3,6,1,4,1,9,9,500,1,2,3,1,1),_CswDSLindex_Type())
cswDSLindex.setMaxAccess(_j)
if mibBuilder.loadTexts:cswDSLindex.setStatus(_B)
class _CswDistrStackLinkBundleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_CswDistrStackLinkBundleOperStatus_Type.__name__=_F
_CswDistrStackLinkBundleOperStatus_Object=MibTableColumn
cswDistrStackLinkBundleOperStatus=_CswDistrStackLinkBundleOperStatus_Object((1,3,6,1,4,1,9,9,500,1,2,3,1,2),_CswDistrStackLinkBundleOperStatus_Type())
cswDistrStackLinkBundleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cswDistrStackLinkBundleOperStatus.setStatus(_B)
_CswDistrStackPhyPortInfoTable_Object=MibTable
cswDistrStackPhyPortInfoTable=_CswDistrStackPhyPortInfoTable_Object((1,3,6,1,4,1,9,9,500,1,2,4))
if mibBuilder.loadTexts:cswDistrStackPhyPortInfoTable.setStatus(_B)
_CswDistrStackPhyPortInfoEntry_Object=MibTableRow
cswDistrStackPhyPortInfoEntry=_CswDistrStackPhyPortInfoEntry_Object((1,3,6,1,4,1,9,9,500,1,2,4,1))
cswDistrStackPhyPortInfoEntry.setIndexNames((0,_J,_K),(0,_A,_i),(0,_T,_U))
if mibBuilder.loadTexts:cswDistrStackPhyPortInfoEntry.setStatus(_B)
_CswDistrStackPhyPort_Type=SnmpAdminString
_CswDistrStackPhyPort_Object=MibTableColumn
cswDistrStackPhyPort=_CswDistrStackPhyPort_Object((1,3,6,1,4,1,9,9,500,1,2,4,1,1),_CswDistrStackPhyPort_Type())
cswDistrStackPhyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cswDistrStackPhyPort.setStatus(_B)
class _CswDistrStackPhyPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_CswDistrStackPhyPortOperStatus_Type.__name__=_F
_CswDistrStackPhyPortOperStatus_Object=MibTableColumn
cswDistrStackPhyPortOperStatus=_CswDistrStackPhyPortOperStatus_Object((1,3,6,1,4,1,9,9,500,1,2,4,1,2),_CswDistrStackPhyPortOperStatus_Type())
cswDistrStackPhyPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cswDistrStackPhyPortOperStatus.setStatus(_B)
_CswDistrStackPhyPortNbr_Type=SnmpAdminString
_CswDistrStackPhyPortNbr_Object=MibTableColumn
cswDistrStackPhyPortNbr=_CswDistrStackPhyPortNbr_Object((1,3,6,1,4,1,9,9,500,1,2,4,1,3),_CswDistrStackPhyPortNbr_Type())
cswDistrStackPhyPortNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:cswDistrStackPhyPortNbr.setStatus(_B)
_CswDistrStackPhyPortNbrsw_Type=EntPhysicalIndexOrZero
_CswDistrStackPhyPortNbrsw_Object=MibTableColumn
cswDistrStackPhyPortNbrsw=_CswDistrStackPhyPortNbrsw_Object((1,3,6,1,4,1,9,9,500,1,2,4,1,4),_CswDistrStackPhyPortNbrsw_Type())
cswDistrStackPhyPortNbrsw.setMaxAccess(_C)
if mibBuilder.loadTexts:cswDistrStackPhyPortNbrsw.setStatus(_B)
_CswStackPowerInfo_ObjectIdentity=ObjectIdentity
cswStackPowerInfo=_CswStackPowerInfo_ObjectIdentity((1,3,6,1,4,1,9,9,500,1,3))
_CswStackPowerInfoTable_Object=MibTable
cswStackPowerInfoTable=_CswStackPowerInfoTable_Object((1,3,6,1,4,1,9,9,500,1,3,1))
if mibBuilder.loadTexts:cswStackPowerInfoTable.setStatus(_B)
_CswStackPowerInfoEntry_Object=MibTableRow
cswStackPowerInfoEntry=_CswStackPowerInfoEntry_Object((1,3,6,1,4,1,9,9,500,1,3,1,1))
cswStackPowerInfoEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:cswStackPowerInfoEntry.setStatus(_B)
_CswStackPowerStackNumber_Type=Unsigned32
_CswStackPowerStackNumber_Object=MibTableColumn
cswStackPowerStackNumber=_CswStackPowerStackNumber_Object((1,3,6,1,4,1,9,9,500,1,3,1,1,1),_CswStackPowerStackNumber_Type())
cswStackPowerStackNumber.setMaxAccess(_j)
if mibBuilder.loadTexts:cswStackPowerStackNumber.setStatus(_B)
_CswStackPowerMode_Type=CswPowerStackMode
_CswStackPowerMode_Object=MibTableColumn
cswStackPowerMode=_CswStackPowerMode_Object((1,3,6,1,4,1,9,9,500,1,3,1,1,2),_CswStackPowerMode_Type())
cswStackPowerMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cswStackPowerMode.setStatus(_B)
_CswStackPowerMasterMacAddress_Type=MacAddress
_CswStackPowerMasterMacAddress_Object=MibTableColumn
cswStackPowerMasterMacAddress=_CswStackPowerMasterMacAddress_Object((1,3,6,1,4,1,9,9,500,1,3,1,1,3),_CswStackPowerMasterMacAddress_Type())
cswStackPowerMasterMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerMasterMacAddress.setStatus(_B)
_CswStackPowerMasterSwitchNum_Type=Unsigned32
_CswStackPowerMasterSwitchNum_Object=MibTableColumn
cswStackPowerMasterSwitchNum=_CswStackPowerMasterSwitchNum_Object((1,3,6,1,4,1,9,9,500,1,3,1,1,4),_CswStackPowerMasterSwitchNum_Type())
cswStackPowerMasterSwitchNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerMasterSwitchNum.setStatus(_B)
_CswStackPowerNumMembers_Type=Unsigned32
_CswStackPowerNumMembers_Object=MibTableColumn
cswStackPowerNumMembers=_CswStackPowerNumMembers_Object((1,3,6,1,4,1,9,9,500,1,3,1,1,5),_CswStackPowerNumMembers_Type())
cswStackPowerNumMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerNumMembers.setStatus(_B)
_CswStackPowerType_Type=CswPowerStackType
_CswStackPowerType_Object=MibTableColumn
cswStackPowerType=_CswStackPowerType_Object((1,3,6,1,4,1,9,9,500,1,3,1,1,6),_CswStackPowerType_Type())
cswStackPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerType.setStatus(_B)
_CswStackPowerName_Type=SnmpAdminString
_CswStackPowerName_Object=MibTableColumn
cswStackPowerName=_CswStackPowerName_Object((1,3,6,1,4,1,9,9,500,1,3,1,1,7),_CswStackPowerName_Type())
cswStackPowerName.setMaxAccess(_E)
if mibBuilder.loadTexts:cswStackPowerName.setStatus(_B)
_CswStackPowerPortInfoTable_Object=MibTable
cswStackPowerPortInfoTable=_CswStackPowerPortInfoTable_Object((1,3,6,1,4,1,9,9,500,1,3,2))
if mibBuilder.loadTexts:cswStackPowerPortInfoTable.setStatus(_B)
_CswStackPowerPortInfoEntry_Object=MibTableRow
cswStackPowerPortInfoEntry=_CswStackPowerPortInfoEntry_Object((1,3,6,1,4,1,9,9,500,1,3,2,1))
cswStackPowerPortInfoEntry.setIndexNames((0,_J,_K),(0,_A,_s))
if mibBuilder.loadTexts:cswStackPowerPortInfoEntry.setStatus(_B)
_CswStackPowerPortIndex_Type=Unsigned32
_CswStackPowerPortIndex_Object=MibTableColumn
cswStackPowerPortIndex=_CswStackPowerPortIndex_Object((1,3,6,1,4,1,9,9,500,1,3,2,1,1),_CswStackPowerPortIndex_Type())
cswStackPowerPortIndex.setMaxAccess(_j)
if mibBuilder.loadTexts:cswStackPowerPortIndex.setStatus(_B)
class _CswStackPowerPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CswStackPowerPortOperStatus_Type.__name__=_F
_CswStackPowerPortOperStatus_Object=MibTableColumn
cswStackPowerPortOperStatus=_CswStackPowerPortOperStatus_Object((1,3,6,1,4,1,9,9,500,1,3,2,1,2),_CswStackPowerPortOperStatus_Type())
cswStackPowerPortOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cswStackPowerPortOperStatus.setStatus(_B)
_CswStackPowerPortNeighborMacAddress_Type=MacAddress
_CswStackPowerPortNeighborMacAddress_Object=MibTableColumn
cswStackPowerPortNeighborMacAddress=_CswStackPowerPortNeighborMacAddress_Object((1,3,6,1,4,1,9,9,500,1,3,2,1,3),_CswStackPowerPortNeighborMacAddress_Type())
cswStackPowerPortNeighborMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerPortNeighborMacAddress.setStatus(_B)
_CswStackPowerPortNeighborSwitchNum_Type=CswSwitchNumberOrZero
_CswStackPowerPortNeighborSwitchNum_Object=MibTableColumn
cswStackPowerPortNeighborSwitchNum=_CswStackPowerPortNeighborSwitchNum_Object((1,3,6,1,4,1,9,9,500,1,3,2,1,4),_CswStackPowerPortNeighborSwitchNum_Type())
cswStackPowerPortNeighborSwitchNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerPortNeighborSwitchNum.setStatus(_B)
class _CswStackPowerPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_CswStackPowerPortLinkStatus_Type.__name__=_F
_CswStackPowerPortLinkStatus_Object=MibTableColumn
cswStackPowerPortLinkStatus=_CswStackPowerPortLinkStatus_Object((1,3,6,1,4,1,9,9,500,1,3,2,1,5),_CswStackPowerPortLinkStatus_Type())
cswStackPowerPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerPortLinkStatus.setStatus(_B)
_CswStackPowerPortOverCurrentThreshold_Type=Unsigned32
_CswStackPowerPortOverCurrentThreshold_Object=MibTableColumn
cswStackPowerPortOverCurrentThreshold=_CswStackPowerPortOverCurrentThreshold_Object((1,3,6,1,4,1,9,9,500,1,3,2,1,6),_CswStackPowerPortOverCurrentThreshold_Type())
cswStackPowerPortOverCurrentThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cswStackPowerPortOverCurrentThreshold.setStatus(_B)
if mibBuilder.loadTexts:cswStackPowerPortOverCurrentThreshold.setUnits('Amperes')
_CswStackPowerPortName_Type=SnmpAdminString
_CswStackPowerPortName_Object=MibTableColumn
cswStackPowerPortName=_CswStackPowerPortName_Object((1,3,6,1,4,1,9,9,500,1,3,2,1,7),_CswStackPowerPortName_Type())
cswStackPowerPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:cswStackPowerPortName.setStatus(_B)
_CiscoStackWiseMIBConform_ObjectIdentity=ObjectIdentity
ciscoStackWiseMIBConform=_CiscoStackWiseMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,500,2))
_CswStackWiseMIBCompliances_ObjectIdentity=ObjectIdentity
cswStackWiseMIBCompliances=_CswStackWiseMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,500,2,1))
_CswStackWiseMIBGroups_ObjectIdentity=ObjectIdentity
cswStackWiseMIBGroups=_CswStackWiseMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,500,2,2))
cswStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,1))
cswStatusGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_L),(_A,_t),(_A,_D),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_M),(_A,_d),(_A,_k),(_A,_l),(_A,_u),(_A,_m)))
if mibBuilder.loadTexts:cswStatusGroup.setStatus(_G)
cswStatusGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,3))
cswStatusGroupRev1.setObjects(*((_A,_X),(_A,_Y),(_A,_L),(_A,_D),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_M),(_A,_d),(_A,_k)))
if mibBuilder.loadTexts:cswStatusGroupRev1.setStatus(_B)
cswStackPowerStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,4))
cswStackPowerStatusGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_m),(_A,_N)))
if mibBuilder.loadTexts:cswStackPowerStatusGroup.setStatus(_B)
cswStackPowerSwitchStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,5))
cswStackPowerSwitchStatusGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:cswStackPowerSwitchStatusGroup.setStatus(_B)
cswStackPowerPortStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,6))
cswStackPowerPortStatusGroup.setObjects(*((_A,_n),(_A,_A4),(_A,_A5),(_A,_o),(_A,_e),(_A,_H)))
if mibBuilder.loadTexts:cswStackPowerPortStatusGroup.setStatus(_B)
cswStackPowerEnableNotificationGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,8))
cswStackPowerEnableNotificationGroup.setObjects((_A,_A6))
if mibBuilder.loadTexts:cswStackPowerEnableNotificationGroup.setStatus(_B)
cswStackPowerAllocatedGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,10))
cswStackPowerAllocatedGroup.setObjects((_A,_A7))
if mibBuilder.loadTexts:cswStackPowerAllocatedGroup.setStatus(_B)
cswStatusGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,11))
cswStatusGroupRev2.setObjects(*((_A,_X),(_A,_Y),(_A,_L),(_A,_D),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_M),(_A,_d),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:cswStatusGroupRev2.setStatus(_B)
cswDistrStackLinkStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,12))
cswDistrStackLinkStatusGroup.setObjects((_A,_AB))
if mibBuilder.loadTexts:cswDistrStackLinkStatusGroup.setStatus(_B)
cswDistrStackPhyPortStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,500,2,2,13))
cswDistrStackPhyPortStatusGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:cswDistrStackPhyPortStatusGroup.setStatus(_B)
cswStackPortChange=NotificationType((1,3,6,1,4,1,9,9,500,0,0,1))
cswStackPortChange.setObjects(*((_T,_U),(_A,_l),(_A,_D)))
if mibBuilder.loadTexts:cswStackPortChange.setStatus(_B)
cswStackNewMaster=NotificationType((1,3,6,1,4,1,9,9,500,0,0,2))
cswStackNewMaster.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackNewMaster.setStatus(_B)
cswStackMismatch=NotificationType((1,3,6,1,4,1,9,9,500,0,0,3))
cswStackMismatch.setObjects(*((_A,_M),(_A,_D)))
if mibBuilder.loadTexts:cswStackMismatch.setStatus(_B)
cswStackRingRedundant=NotificationType((1,3,6,1,4,1,9,9,500,0,0,4))
cswStackRingRedundant.setObjects((_A,_L))
if mibBuilder.loadTexts:cswStackRingRedundant.setStatus(_B)
cswStackNewMember=NotificationType((1,3,6,1,4,1,9,9,500,0,0,5))
cswStackNewMember.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackNewMember.setStatus(_B)
cswStackMemberRemoved=NotificationType((1,3,6,1,4,1,9,9,500,0,0,6))
cswStackMemberRemoved.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackMemberRemoved.setStatus(_B)
cswStackPowerPortLinkStatusChanged=NotificationType((1,3,6,1,4,1,9,9,500,0,0,7))
cswStackPowerPortLinkStatusChanged.setObjects(*((_A,_o),(_A,_D),(_A,_H)))
if mibBuilder.loadTexts:cswStackPowerPortLinkStatusChanged.setStatus(_B)
cswStackPowerPortOperStatusChanged=NotificationType((1,3,6,1,4,1,9,9,500,0,0,8))
cswStackPowerPortOperStatusChanged.setObjects(*((_A,_D),(_A,_n),(_A,_H)))
if mibBuilder.loadTexts:cswStackPowerPortOperStatusChanged.setStatus(_B)
cswStackPowerVersionMismatch=NotificationType((1,3,6,1,4,1,9,9,500,0,0,9))
cswStackPowerVersionMismatch.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerVersionMismatch.setStatus(_B)
cswStackPowerInvalidTopology=NotificationType((1,3,6,1,4,1,9,9,500,0,0,10))
cswStackPowerInvalidTopology.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerInvalidTopology.setStatus(_B)
cscwStackPowerBudgetWarrning=NotificationType((1,3,6,1,4,1,9,9,500,0,0,11))
cscwStackPowerBudgetWarrning.setObjects((_A,_D))
if mibBuilder.loadTexts:cscwStackPowerBudgetWarrning.setStatus(_B)
cswStackPowerInvalidInputCurrent=NotificationType((1,3,6,1,4,1,9,9,500,0,0,12))
cswStackPowerInvalidInputCurrent.setObjects(*((_A,_D),(_A,_e),(_A,_H)))
if mibBuilder.loadTexts:cswStackPowerInvalidInputCurrent.setStatus(_B)
cswStackPowerInvalidOutputCurrent=NotificationType((1,3,6,1,4,1,9,9,500,0,0,13))
cswStackPowerInvalidOutputCurrent.setObjects(*((_A,_D),(_A,_e),(_A,_H)))
if mibBuilder.loadTexts:cswStackPowerInvalidOutputCurrent.setStatus(_B)
cswStackPowerUnderBudget=NotificationType((1,3,6,1,4,1,9,9,500,0,0,14))
cswStackPowerUnderBudget.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerUnderBudget.setStatus(_B)
cswStackPowerUnbalancedPowerSupplies=NotificationType((1,3,6,1,4,1,9,9,500,0,0,15))
cswStackPowerUnbalancedPowerSupplies.setObjects((_A,_N))
if mibBuilder.loadTexts:cswStackPowerUnbalancedPowerSupplies.setStatus(_B)
cswStackPowerInsufficientPower=NotificationType((1,3,6,1,4,1,9,9,500,0,0,16))
cswStackPowerInsufficientPower.setObjects((_A,_N))
if mibBuilder.loadTexts:cswStackPowerInsufficientPower.setStatus(_B)
cswStackPowerPriorityConflict=NotificationType((1,3,6,1,4,1,9,9,500,0,0,17))
cswStackPowerPriorityConflict.setObjects((_A,_N))
if mibBuilder.loadTexts:cswStackPowerPriorityConflict.setStatus(_B)
cswStackPowerUnderVoltage=NotificationType((1,3,6,1,4,1,9,9,500,0,0,18))
cswStackPowerUnderVoltage.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerUnderVoltage.setStatus(_B)
cswStackPowerGLS=NotificationType((1,3,6,1,4,1,9,9,500,0,0,19))
cswStackPowerGLS.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerGLS.setStatus(_B)
cswStackPowerILS=NotificationType((1,3,6,1,4,1,9,9,500,0,0,20))
cswStackPowerILS.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerILS.setStatus(_B)
cswStackPowerSRLS=NotificationType((1,3,6,1,4,1,9,9,500,0,0,21))
cswStackPowerSRLS.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerSRLS.setStatus(_B)
cswStackPowerSSLS=NotificationType((1,3,6,1,4,1,9,9,500,0,0,22))
cswStackPowerSSLS.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackPowerSSLS.setStatus(_B)
cswStackMemberToBeReloadedForUpgrade=NotificationType((1,3,6,1,4,1,9,9,500,0,0,23))
cswStackMemberToBeReloadedForUpgrade.setObjects((_A,_D))
if mibBuilder.loadTexts:cswStackMemberToBeReloadedForUpgrade.setStatus(_B)
cswNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,500,2,2,2))
cswNotificationGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:cswNotificationGroup.setStatus(_B)
cswStackPowerNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,500,2,2,7))
cswStackPowerNotificationGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:cswStackPowerNotificationGroup.setStatus(_B)
cswNotificationGroupSup1=NotificationGroup((1,3,6,1,4,1,9,9,500,2,2,9))
cswNotificationGroupSup1.setObjects((_A,_Ac))
if mibBuilder.loadTexts:cswNotificationGroupSup1.setStatus(_B)
cswStackWiseMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,500,2,1,1))
cswStackWiseMIBCompliance.setObjects(*((_A,_Ad),(_A,_I)))
if mibBuilder.loadTexts:cswStackWiseMIBCompliance.setStatus(_G)
cswStackWiseMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,500,2,1,2))
cswStackWiseMIBComplianceRev1.setObjects(*((_A,_I),(_A,_f),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cswStackWiseMIBComplianceRev1.setStatus(_G)
cswStackWiseMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,500,2,1,3))
cswStackWiseMIBComplianceRev2.setObjects(*((_A,_I),(_A,_g),(_A,_f),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cswStackWiseMIBComplianceRev2.setStatus(_G)
cswStackWiseMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,500,2,1,4))
cswStackWiseMIBComplianceRev3.setObjects(*((_A,_I),(_A,_g),(_A,_f),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_p)))
if mibBuilder.loadTexts:cswStackWiseMIBComplianceRev3.setStatus(_G)
cswStackWiseMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,500,2,1,5))
cswStackWiseMIBComplianceRev4.setObjects(*((_A,_I),(_A,_g),(_A,_Ae),(_A,_O),(_A,_Af),(_A,_Ag),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_p)))
if mibBuilder.loadTexts:cswStackWiseMIBComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CswPowerStackMode':CswPowerStackMode,'CswPowerStackType':CswPowerStackType,'CswSwitchNumber':CswSwitchNumber,'CswSwitchNumberOrZero':CswSwitchNumberOrZero,'CswSwitchPriority':CswSwitchPriority,'ciscoStackWiseMIB':ciscoStackWiseMIB,'ciscoStackWiseMIBNotifs':ciscoStackWiseMIBNotifs,'cswMIBNotifications':cswMIBNotifications,_AG:cswStackPortChange,_AH:cswStackNewMaster,_AI:cswStackMismatch,_AJ:cswStackRingRedundant,_AK:cswStackNewMember,_AL:cswStackMemberRemoved,_AM:cswStackPowerPortLinkStatusChanged,_AN:cswStackPowerPortOperStatusChanged,_AO:cswStackPowerVersionMismatch,_AP:cswStackPowerInvalidTopology,_AQ:cscwStackPowerBudgetWarrning,_AR:cswStackPowerInvalidInputCurrent,_AS:cswStackPowerInvalidOutputCurrent,_AT:cswStackPowerUnderBudget,_AU:cswStackPowerUnbalancedPowerSupplies,_AV:cswStackPowerInsufficientPower,_AW:cswStackPowerPriorityConflict,_AX:cswStackPowerUnderVoltage,_AY:cswStackPowerGLS,_AZ:cswStackPowerILS,_Aa:cswStackPowerSRLS,_Ab:cswStackPowerSSLS,_Ac:cswStackMemberToBeReloadedForUpgrade,'ciscoStackWiseMIBObjects':ciscoStackWiseMIBObjects,'cswGlobals':cswGlobals,_X:cswMaxSwitchNum,_Y:cswMaxSwitchConfigPriority,_L:cswRingRedundant,_t:cswEnableStackNotifications,_A6:cswEnableIndividualStackNotifications,_A8:cswStackDomainNum,_A9:cswStackType,_AA:cswStackBandWidth,'cswStackInfo':cswStackInfo,'cswSwitchInfoTable':cswSwitchInfoTable,'cswSwitchInfoEntry':cswSwitchInfoEntry,_D:cswSwitchNumCurrent,_Z:cswSwitchNumNextReload,_a:cswSwitchRole,_b:cswSwitchSwPriority,_c:cswSwitchHwPriority,_M:cswSwitchState,_d:cswSwitchMacAddress,_k:cswSwitchSoftwareImage,_z:cswSwitchPowerBudget,_A0:cswSwitchPowerCommited,_A1:cswSwitchSystemPowerPriority,_A2:cswSwitchPoeDevicesLowPriority,_A3:cswSwitchPoeDevicesHighPriority,_A7:cswSwitchPowerAllocated,'cswStackPortInfoTable':cswStackPortInfoTable,'cswStackPortInfoEntry':cswStackPortInfoEntry,_l:cswStackPortOperStatus,_u:cswStackPortNeighbor,'cswDistrStackLinkInfoTable':cswDistrStackLinkInfoTable,'cswDistrStackLinkInfoEntry':cswDistrStackLinkInfoEntry,_i:cswDSLindex,_AB:cswDistrStackLinkBundleOperStatus,'cswDistrStackPhyPortInfoTable':cswDistrStackPhyPortInfoTable,'cswDistrStackPhyPortInfoEntry':cswDistrStackPhyPortInfoEntry,_AC:cswDistrStackPhyPort,_AD:cswDistrStackPhyPortOperStatus,_AE:cswDistrStackPhyPortNbr,_AF:cswDistrStackPhyPortNbrsw,'cswStackPowerInfo':cswStackPowerInfo,'cswStackPowerInfoTable':cswStackPowerInfoTable,'cswStackPowerInfoEntry':cswStackPowerInfoEntry,_r:cswStackPowerStackNumber,_v:cswStackPowerMode,_w:cswStackPowerMasterMacAddress,_x:cswStackPowerMasterSwitchNum,_y:cswStackPowerNumMembers,_m:cswStackPowerType,_N:cswStackPowerName,'cswStackPowerPortInfoTable':cswStackPowerPortInfoTable,'cswStackPowerPortInfoEntry':cswStackPowerPortInfoEntry,_s:cswStackPowerPortIndex,_n:cswStackPowerPortOperStatus,_A4:cswStackPowerPortNeighborMacAddress,_A5:cswStackPowerPortNeighborSwitchNum,_o:cswStackPowerPortLinkStatus,_e:cswStackPowerPortOverCurrentThreshold,_H:cswStackPowerPortName,'ciscoStackWiseMIBConform':ciscoStackWiseMIBConform,'cswStackWiseMIBCompliances':cswStackWiseMIBCompliances,'cswStackWiseMIBCompliance':cswStackWiseMIBCompliance,'cswStackWiseMIBComplianceRev1':cswStackWiseMIBComplianceRev1,'cswStackWiseMIBComplianceRev2':cswStackWiseMIBComplianceRev2,'cswStackWiseMIBComplianceRev3':cswStackWiseMIBComplianceRev3,'cswStackWiseMIBComplianceRev4':cswStackWiseMIBComplianceRev4,'cswStackWiseMIBGroups':cswStackWiseMIBGroups,_Ad:cswStatusGroup,_I:cswNotificationGroup,_f:cswStatusGroupRev1,_P:cswStackPowerStatusGroup,_Q:cswStackPowerSwitchStatusGroup,_R:cswStackPowerPortStatusGroup,_S:cswStackPowerNotificationGroup,_O:cswStackPowerEnableNotificationGroup,_g:cswNotificationGroupSup1,_p:cswStackPowerAllocatedGroup,_Ae:cswStatusGroupRev2,_Af:cswDistrStackLinkStatusGroup,_Ag:cswDistrStackPhyPortStatusGroup})