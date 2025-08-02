_AH='hpStackConfigScalarGroup1'
_AG='hpStackNotificationsGroup'
_AF='hpStackTopoChange'
_AE='hpStackActiveMemberCount'
_AD='hpStackMemberCount'
_AC='hpStackPortAdminStatus'
_AB='hpStackPortCost'
_AA='hpStackMemberBootImage'
_A9='hpStackMemberOsVersion'
_A8='hpStackMemberBootRomVersion'
_A7='hpStackMemberFreeMemory'
_A6='hpStackMemberTotalMemory'
_A5='hpStackMemberCpuUtil'
_A4='hpStackMemberSerialNum'
_A3='hpStackMemberSysOid'
_A2='hpStackMemberUpTime'
_A1='hpStackMemberProductName'
_A0='hpStackMemberEntPhysicalIndex'
_z='hpStackMemberEntryStatus'
_y='hpStackMemberAdminPriority'
_x='hpStackMemberReboot'
_w='hpStackMemberShutdown'
_v='hpStackMemberMacAddr'
_u='hpStackMemberProductId'
_t='frontPlane'
_s='backPlane'
_r='hpStackPortType'
_q='hpStackPortId'
_p='hpStackSequenceNum'
_o='disabled'
_n='hpSwitchBaseMACAddress'
_m='NETSWITCH-MIB'
_l='hpStackNotificationsGroup1'
_k='hpStackConfigScalarGroup'
_j='hpStackMergeSuccess'
_i='hpStackMergeFailed'
_h='hpStackMemberStatusChange'
_g='hpStackMemberChange'
_f='hpStackCommanderChange'
_e='hpStackPortChange'
_d='hpStackPortTypeForTrap'
_c='hpStackPortIdForTrap'
_b='hpStackPortNeighbor'
_a='hpStackPortOperStatus'
_Z='hpStackSplitPolicy'
_Y='hpStackSwitchPreferredMemberId'
_X='hpStackSwitchPreferredPriority'
_W='hpStackSwitchAdminStatus'
_V='hpStackTrapEnable'
_U='hpStackSetStacking'
_T='hpStackOperStatus'
_S='accessible-for-notify'
_R='hpStackMemberId'
_Q='disable'
_P='enable'
_O='hpStackPortGroup'
_N='hpStackMemberGroup'
_M='deprecated'
_L='hpStackTopology'
_K='not-accessible'
_J='OctetString'
_I='hpStackId'
_H='read-create'
_G='hpStackMemberState'
_F='read-write'
_E='hpStackMemberIdForTrap'
_D='read-only'
_C='Integer32'
_B='current'
_A='HP-STACK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
hpSwitchBaseMACAddress,=mibBuilder.importSymbols(_m,_n)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpStackMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,69))
if mibBuilder.loadTexts:hpStackMIB.setRevisions(('2021-01-22 00:00','2020-09-29 00:00','2020-09-21 00:00','2010-01-03 00:00'))
_HpStackNotifications_ObjectIdentity=ObjectIdentity
hpStackNotifications=_HpStackNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,69,0))
_HpStackObjects_ObjectIdentity=ObjectIdentity
hpStackObjects=_HpStackObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,69,1))
_HpStackConfig_ObjectIdentity=ObjectIdentity
hpStackConfig=_HpStackConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1))
class _HpStackId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpStackId_Type.__name__=_J
_HpStackId_Object=MibScalar
hpStackId=_HpStackId_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,1),_HpStackId_Type())
hpStackId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackId.setStatus(_B)
class _HpStackOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unAvailable',0),(_o,1),('active',2),('fragmentInactive',3),('fragmentActive',4)))
_HpStackOperStatus_Type.__name__=_C
_HpStackOperStatus_Object=MibScalar
hpStackOperStatus=_HpStackOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,2),_HpStackOperStatus_Type())
hpStackOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackOperStatus.setStatus(_B)
_HpStackSetStacking_Type=TruthValue
_HpStackSetStacking_Object=MibScalar
hpStackSetStacking=_HpStackSetStacking_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,3),_HpStackSetStacking_Type())
hpStackSetStacking.setMaxAccess(_F)
if mibBuilder.loadTexts:hpStackSetStacking.setStatus(_B)
class _HpStackTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unKnown',0),('chain',1),('ring',2),('mesh',3),('partialMesh',4)))
_HpStackTopology_Type.__name__=_C
_HpStackTopology_Object=MibScalar
hpStackTopology=_HpStackTopology_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,4),_HpStackTopology_Type())
hpStackTopology.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackTopology.setStatus(_B)
class _HpStackTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpStackTrapEnable_Type.__name__=_C
_HpStackTrapEnable_Object=MibScalar
hpStackTrapEnable=_HpStackTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,5),_HpStackTrapEnable_Type())
hpStackTrapEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpStackTrapEnable.setStatus(_B)
class _HpStackSplitPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneFragmentUp',1),('allFragmentsUp',2)))
_HpStackSplitPolicy_Type.__name__=_C
_HpStackSplitPolicy_Object=MibScalar
hpStackSplitPolicy=_HpStackSplitPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,6),_HpStackSplitPolicy_Type())
hpStackSplitPolicy.setMaxAccess(_F)
if mibBuilder.loadTexts:hpStackSplitPolicy.setStatus(_B)
class _HpStackMemberCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpStackMemberCount_Type.__name__=_C
_HpStackMemberCount_Object=MibScalar
hpStackMemberCount=_HpStackMemberCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,7),_HpStackMemberCount_Type())
hpStackMemberCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberCount.setStatus(_B)
class _HpStackActiveMemberCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpStackActiveMemberCount_Type.__name__=_C
_HpStackActiveMemberCount_Object=MibScalar
hpStackActiveMemberCount=_HpStackActiveMemberCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,1,8),_HpStackActiveMemberCount_Type())
hpStackActiveMemberCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackActiveMemberCount.setStatus(_B)
_HpStackConfigTable_Object=MibTable
hpStackConfigTable=_HpStackConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,2))
if mibBuilder.loadTexts:hpStackConfigTable.setStatus(_B)
_HpStackConfigEntry_Object=MibTableRow
hpStackConfigEntry=_HpStackConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,2,1))
hpStackConfigEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:hpStackConfigEntry.setStatus(_B)
class _HpStackSequenceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpStackSequenceNum_Type.__name__=_C
_HpStackSequenceNum_Object=MibTableColumn
hpStackSequenceNum=_HpStackSequenceNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,2,1,1),_HpStackSequenceNum_Type())
hpStackSequenceNum.setMaxAccess(_K)
if mibBuilder.loadTexts:hpStackSequenceNum.setStatus(_B)
class _HpStackSwitchAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpStackSwitchAdminStatus_Type.__name__=_C
_HpStackSwitchAdminStatus_Object=MibTableColumn
hpStackSwitchAdminStatus=_HpStackSwitchAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,2,1,2),_HpStackSwitchAdminStatus_Type())
hpStackSwitchAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpStackSwitchAdminStatus.setStatus(_B)
class _HpStackSwitchPreferredPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpStackSwitchPreferredPriority_Type.__name__=_C
_HpStackSwitchPreferredPriority_Object=MibTableColumn
hpStackSwitchPreferredPriority=_HpStackSwitchPreferredPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,2,1,3),_HpStackSwitchPreferredPriority_Type())
hpStackSwitchPreferredPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:hpStackSwitchPreferredPriority.setStatus(_B)
class _HpStackSwitchPreferredMemberId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpStackSwitchPreferredMemberId_Type.__name__=_C
_HpStackSwitchPreferredMemberId_Object=MibTableColumn
hpStackSwitchPreferredMemberId=_HpStackSwitchPreferredMemberId_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,2,1,4),_HpStackSwitchPreferredMemberId_Type())
hpStackSwitchPreferredMemberId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpStackSwitchPreferredMemberId.setStatus(_B)
_HpStackMemberTable_Object=MibTable
hpStackMemberTable=_HpStackMemberTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3))
if mibBuilder.loadTexts:hpStackMemberTable.setStatus(_B)
_HpStackMemberEntry_Object=MibTableRow
hpStackMemberEntry=_HpStackMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1))
hpStackMemberEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:hpStackMemberEntry.setStatus(_B)
class _HpStackMemberId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpStackMemberId_Type.__name__=_C
_HpStackMemberId_Object=MibTableColumn
hpStackMemberId=_HpStackMemberId_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,1),_HpStackMemberId_Type())
hpStackMemberId.setMaxAccess(_K)
if mibBuilder.loadTexts:hpStackMemberId.setStatus(_B)
_HpStackMemberProductId_Type=DisplayString
_HpStackMemberProductId_Object=MibTableColumn
hpStackMemberProductId=_HpStackMemberProductId_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,2),_HpStackMemberProductId_Type())
hpStackMemberProductId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpStackMemberProductId.setStatus(_B)
class _HpStackMemberMacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_HpStackMemberMacAddr_Type.__name__=_J
_HpStackMemberMacAddr_Object=MibTableColumn
hpStackMemberMacAddr=_HpStackMemberMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,3),_HpStackMemberMacAddr_Type())
hpStackMemberMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hpStackMemberMacAddr.setStatus(_B)
_HpStackMemberShutdown_Type=TruthValue
_HpStackMemberShutdown_Object=MibTableColumn
hpStackMemberShutdown=_HpStackMemberShutdown_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,4),_HpStackMemberShutdown_Type())
hpStackMemberShutdown.setMaxAccess(_H)
if mibBuilder.loadTexts:hpStackMemberShutdown.setStatus(_B)
_HpStackMemberReboot_Type=TruthValue
_HpStackMemberReboot_Object=MibTableColumn
hpStackMemberReboot=_HpStackMemberReboot_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,5),_HpStackMemberReboot_Type())
hpStackMemberReboot.setMaxAccess(_H)
if mibBuilder.loadTexts:hpStackMemberReboot.setStatus(_B)
class _HpStackMemberAdminPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpStackMemberAdminPriority_Type.__name__=_C
_HpStackMemberAdminPriority_Object=MibTableColumn
hpStackMemberAdminPriority=_HpStackMemberAdminPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,6),_HpStackMemberAdminPriority_Type())
hpStackMemberAdminPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:hpStackMemberAdminPriority.setStatus(_B)
_HpStackMemberEntryStatus_Type=RowStatus
_HpStackMemberEntryStatus_Object=MibTableColumn
hpStackMemberEntryStatus=_HpStackMemberEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,7),_HpStackMemberEntryStatus_Type())
hpStackMemberEntryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpStackMemberEntryStatus.setStatus(_B)
_HpStackMemberEntPhysicalIndex_Type=PhysicalIndex
_HpStackMemberEntPhysicalIndex_Object=MibTableColumn
hpStackMemberEntPhysicalIndex=_HpStackMemberEntPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,8),_HpStackMemberEntPhysicalIndex_Type())
hpStackMemberEntPhysicalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberEntPhysicalIndex.setStatus(_B)
class _HpStackMemberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('unusedId',0),('missing',1),('provision',2),('commander',3),('standby',4),('member',5),('shutdown',6),('booting',7),('communicationFailure',8),('incompatibleOs',9),('unknownState',10),('standbyBooting',11)))
_HpStackMemberState_Type.__name__=_C
_HpStackMemberState_Object=MibTableColumn
hpStackMemberState=_HpStackMemberState_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,9),_HpStackMemberState_Type())
hpStackMemberState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberState.setStatus(_B)
_HpStackMemberProductName_Type=SnmpAdminString
_HpStackMemberProductName_Object=MibTableColumn
hpStackMemberProductName=_HpStackMemberProductName_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,10),_HpStackMemberProductName_Type())
hpStackMemberProductName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberProductName.setStatus(_B)
_HpStackMemberUpTime_Type=TimeTicks
_HpStackMemberUpTime_Object=MibTableColumn
hpStackMemberUpTime=_HpStackMemberUpTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,11),_HpStackMemberUpTime_Type())
hpStackMemberUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberUpTime.setStatus(_B)
_HpStackMemberSysOid_Type=ObjectIdentifier
_HpStackMemberSysOid_Object=MibTableColumn
hpStackMemberSysOid=_HpStackMemberSysOid_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,12),_HpStackMemberSysOid_Type())
hpStackMemberSysOid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberSysOid.setStatus(_B)
_HpStackMemberIdForTrap_Type=Integer32
_HpStackMemberIdForTrap_Object=MibTableColumn
hpStackMemberIdForTrap=_HpStackMemberIdForTrap_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,13),_HpStackMemberIdForTrap_Type())
hpStackMemberIdForTrap.setMaxAccess(_S)
if mibBuilder.loadTexts:hpStackMemberIdForTrap.setStatus(_B)
_HpStackMemberSerialNum_Type=DisplayString
_HpStackMemberSerialNum_Object=MibTableColumn
hpStackMemberSerialNum=_HpStackMemberSerialNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,14),_HpStackMemberSerialNum_Type())
hpStackMemberSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberSerialNum.setStatus(_B)
_HpStackMemberCpuUtil_Type=Integer32
_HpStackMemberCpuUtil_Object=MibTableColumn
hpStackMemberCpuUtil=_HpStackMemberCpuUtil_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,15),_HpStackMemberCpuUtil_Type())
hpStackMemberCpuUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberCpuUtil.setStatus(_B)
_HpStackMemberTotalMemory_Type=Integer32
_HpStackMemberTotalMemory_Object=MibTableColumn
hpStackMemberTotalMemory=_HpStackMemberTotalMemory_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,16),_HpStackMemberTotalMemory_Type())
hpStackMemberTotalMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberTotalMemory.setStatus(_B)
_HpStackMemberFreeMemory_Type=Integer32
_HpStackMemberFreeMemory_Object=MibTableColumn
hpStackMemberFreeMemory=_HpStackMemberFreeMemory_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,17),_HpStackMemberFreeMemory_Type())
hpStackMemberFreeMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberFreeMemory.setStatus(_B)
_HpStackMemberBootRomVersion_Type=DisplayString
_HpStackMemberBootRomVersion_Object=MibTableColumn
hpStackMemberBootRomVersion=_HpStackMemberBootRomVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,18),_HpStackMemberBootRomVersion_Type())
hpStackMemberBootRomVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberBootRomVersion.setStatus(_B)
_HpStackMemberOsVersion_Type=DisplayString
_HpStackMemberOsVersion_Object=MibTableColumn
hpStackMemberOsVersion=_HpStackMemberOsVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,19),_HpStackMemberOsVersion_Type())
hpStackMemberOsVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberOsVersion.setStatus(_B)
class _HpStackMemberBootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_HpStackMemberBootImage_Type.__name__=_C
_HpStackMemberBootImage_Object=MibTableColumn
hpStackMemberBootImage=_HpStackMemberBootImage_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,3,1,20),_HpStackMemberBootImage_Type())
hpStackMemberBootImage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackMemberBootImage.setStatus(_B)
_HpStackPortTable_Object=MibTable
hpStackPortTable=_HpStackPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5))
if mibBuilder.loadTexts:hpStackPortTable.setStatus(_B)
_HpStackPortEntry_Object=MibTableRow
hpStackPortEntry=_HpStackPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1))
hpStackPortEntry.setIndexNames((0,_A,_R),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:hpStackPortEntry.setStatus(_B)
class _HpStackPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpStackPortId_Type.__name__=_C
_HpStackPortId_Object=MibTableColumn
hpStackPortId=_HpStackPortId_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,1),_HpStackPortId_Type())
hpStackPortId.setMaxAccess(_K)
if mibBuilder.loadTexts:hpStackPortId.setStatus(_B)
class _HpStackPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_t,2)))
_HpStackPortType_Type.__name__=_C
_HpStackPortType_Object=MibTableColumn
hpStackPortType=_HpStackPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,2),_HpStackPortType_Type())
hpStackPortType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpStackPortType.setStatus(_B)
class _HpStackPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),(_o,3),('blocked',4)))
_HpStackPortOperStatus_Type.__name__=_C
_HpStackPortOperStatus_Object=MibTableColumn
hpStackPortOperStatus=_HpStackPortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,3),_HpStackPortOperStatus_Type())
hpStackPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackPortOperStatus.setStatus(_B)
class _HpStackPortNeighbor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpStackPortNeighbor_Type.__name__=_J
_HpStackPortNeighbor_Object=MibTableColumn
hpStackPortNeighbor=_HpStackPortNeighbor_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,4),_HpStackPortNeighbor_Type())
hpStackPortNeighbor.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackPortNeighbor.setStatus(_B)
_HpStackPortCost_Type=Integer32
_HpStackPortCost_Object=MibTableColumn
hpStackPortCost=_HpStackPortCost_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,5),_HpStackPortCost_Type())
hpStackPortCost.setMaxAccess(_D)
if mibBuilder.loadTexts:hpStackPortCost.setStatus(_B)
_HpStackPortIdForTrap_Type=Integer32
_HpStackPortIdForTrap_Object=MibTableColumn
hpStackPortIdForTrap=_HpStackPortIdForTrap_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,6),_HpStackPortIdForTrap_Type())
hpStackPortIdForTrap.setMaxAccess(_S)
if mibBuilder.loadTexts:hpStackPortIdForTrap.setStatus(_B)
class _HpStackPortTypeForTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_t,2)))
_HpStackPortTypeForTrap_Type.__name__=_C
_HpStackPortTypeForTrap_Object=MibTableColumn
hpStackPortTypeForTrap=_HpStackPortTypeForTrap_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,7),_HpStackPortTypeForTrap_Type())
hpStackPortTypeForTrap.setMaxAccess(_S)
if mibBuilder.loadTexts:hpStackPortTypeForTrap.setStatus(_B)
class _HpStackPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpStackPortAdminStatus_Type.__name__=_C
_HpStackPortAdminStatus_Object=MibTableColumn
hpStackPortAdminStatus=_HpStackPortAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,69,1,5,1,8),_HpStackPortAdminStatus_Type())
hpStackPortAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpStackPortAdminStatus.setStatus(_B)
_HpStackConformance_ObjectIdentity=ObjectIdentity
hpStackConformance=_HpStackConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,69,2))
_HpStackCompliances_ObjectIdentity=ObjectIdentity
hpStackCompliances=_HpStackCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,69,2,1))
_HpStackGroups_ObjectIdentity=ObjectIdentity
hpStackGroups=_HpStackGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,69,2,2))
hpStackConfigScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,69,2,2,1))
hpStackConfigScalarGroup.setObjects(*((_A,_I),(_A,_T),(_A,_U),(_A,_L),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hpStackConfigScalarGroup.setStatus(_M)
hpStackMemberGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,69,2,2,2))
hpStackMemberGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_G),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_E),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:hpStackMemberGroup.setStatus(_B)
hpStackPortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,69,2,2,3))
hpStackPortGroup.setObjects(*((_A,_a),(_A,_b),(_A,_AB),(_A,_c),(_A,_d),(_A,_AC)))
if mibBuilder.loadTexts:hpStackPortGroup.setStatus(_B)
hpStackConfigScalarGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,69,2,2,6))
hpStackConfigScalarGroup1.setObjects(*((_A,_I),(_A,_T),(_A,_U),(_A,_L),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:hpStackConfigScalarGroup1.setStatus(_B)
hpStackPortChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,69,0,1))
hpStackPortChange.setObjects(*((_A,_E),(_A,_c),(_A,_d),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hpStackPortChange.setStatus(_B)
hpStackCommanderChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,69,0,2))
hpStackCommanderChange.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpStackCommanderChange.setStatus(_B)
hpStackMemberChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,69,0,3))
hpStackMemberChange.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpStackMemberChange.setStatus(_B)
hpStackMemberStatusChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,69,0,4))
hpStackMemberStatusChange.setObjects(*((_A,_E),(_m,_n),(_A,_G)))
if mibBuilder.loadTexts:hpStackMemberStatusChange.setStatus(_B)
hpStackMergeFailed=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,69,0,5))
hpStackMergeFailed.setObjects(*((_A,_E),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:hpStackMergeFailed.setStatus(_B)
hpStackMergeSuccess=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,69,0,6))
hpStackMergeSuccess.setObjects(*((_A,_E),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:hpStackMergeSuccess.setStatus(_B)
hpStackTopoChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,69,0,7))
hpStackTopoChange.setObjects(*((_A,_E),(_A,_L)))
if mibBuilder.loadTexts:hpStackTopoChange.setStatus(_B)
hpStackNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,69,2,2,4))
hpStackNotificationsGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:hpStackNotificationsGroup.setStatus(_M)
hpStackNotificationsGroup1=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,69,2,2,5))
hpStackNotificationsGroup1.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_AF)))
if mibBuilder.loadTexts:hpStackNotificationsGroup1.setStatus(_B)
hpStackCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,69,2,1,1))
hpStackCompliance.setObjects(*((_A,_k),(_A,_N),(_A,_O),(_A,_AG)))
if mibBuilder.loadTexts:hpStackCompliance.setStatus(_M)
hpStackCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,69,2,1,2))
hpStackCompliance1.setObjects(*((_A,_k),(_A,_N),(_A,_O),(_A,_l)))
if mibBuilder.loadTexts:hpStackCompliance1.setStatus(_M)
hpStackCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,69,2,1,3))
hpStackCompliance2.setObjects(*((_A,_AH),(_A,_N),(_A,_O),(_A,_l)))
if mibBuilder.loadTexts:hpStackCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpStackMIB':hpStackMIB,'hpStackNotifications':hpStackNotifications,_e:hpStackPortChange,_f:hpStackCommanderChange,_g:hpStackMemberChange,_h:hpStackMemberStatusChange,_i:hpStackMergeFailed,_j:hpStackMergeSuccess,_AF:hpStackTopoChange,'hpStackObjects':hpStackObjects,'hpStackConfig':hpStackConfig,_I:hpStackId,_T:hpStackOperStatus,_U:hpStackSetStacking,_L:hpStackTopology,_V:hpStackTrapEnable,_Z:hpStackSplitPolicy,_AD:hpStackMemberCount,_AE:hpStackActiveMemberCount,'hpStackConfigTable':hpStackConfigTable,'hpStackConfigEntry':hpStackConfigEntry,_p:hpStackSequenceNum,_W:hpStackSwitchAdminStatus,_X:hpStackSwitchPreferredPriority,_Y:hpStackSwitchPreferredMemberId,'hpStackMemberTable':hpStackMemberTable,'hpStackMemberEntry':hpStackMemberEntry,_R:hpStackMemberId,_u:hpStackMemberProductId,_v:hpStackMemberMacAddr,_w:hpStackMemberShutdown,_x:hpStackMemberReboot,_y:hpStackMemberAdminPriority,_z:hpStackMemberEntryStatus,_A0:hpStackMemberEntPhysicalIndex,_G:hpStackMemberState,_A1:hpStackMemberProductName,_A2:hpStackMemberUpTime,_A3:hpStackMemberSysOid,_E:hpStackMemberIdForTrap,_A4:hpStackMemberSerialNum,_A5:hpStackMemberCpuUtil,_A6:hpStackMemberTotalMemory,_A7:hpStackMemberFreeMemory,_A8:hpStackMemberBootRomVersion,_A9:hpStackMemberOsVersion,_AA:hpStackMemberBootImage,'hpStackPortTable':hpStackPortTable,'hpStackPortEntry':hpStackPortEntry,_q:hpStackPortId,_r:hpStackPortType,_a:hpStackPortOperStatus,_b:hpStackPortNeighbor,_AB:hpStackPortCost,_c:hpStackPortIdForTrap,_d:hpStackPortTypeForTrap,_AC:hpStackPortAdminStatus,'hpStackConformance':hpStackConformance,'hpStackCompliances':hpStackCompliances,'hpStackCompliance':hpStackCompliance,'hpStackCompliance1':hpStackCompliance1,'hpStackCompliance2':hpStackCompliance2,'hpStackGroups':hpStackGroups,_k:hpStackConfigScalarGroup,_N:hpStackMemberGroup,_O:hpStackPortGroup,_AG:hpStackNotificationsGroup,_l:hpStackNotificationsGroup1,_AH:hpStackConfigScalarGroup1})