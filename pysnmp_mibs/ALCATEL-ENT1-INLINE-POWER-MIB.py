_AF='pethMainPowerUsageNIFailNotification'
_AE='alaPethPwrSupplyNotSupportedTrap'
_AD='alaPethPwrSupplyConflictTrap'
_AC='alaPethUpdateErrorString'
_AB='alaPethUpdateErrorCode'
_AA='alaPethUpdateStatus'
_A9='alaPethUpdateAction'
_A8='alaPethUpdateFilename'
_A7='alaPethUpdatePortGroupIndex'
_A6='alaPethPowerSlotRowStatus'
_A5='alaPethPowerSlotPolicyName'
_A4='alaPethPowerPortRowStatus'
_A3='alaPethPowerPortPolicyName'
_A2='alaPethPowerPolicyRowStatus'
_A1='alaPethPowerRuleAtTime'
_A0='alaPethPowerRuleRowStatus'
_z='alaPethPowerRuleTimezone'
_y='alaPethPowerRuleMonths'
_x='alaPethPowerRuleDaysOfMonth'
_w='alaPethPowerRuleDaysOfWeek'
_v='alaPethPowerRuleAtMinute'
_u='alaPethPowerRulePowerStatus'
_t='alaPethPowerRuleAdminStatus'
_s='alaPethMainChassisDynamicPowerManagement'
_r='alaPethMainPseClassDetection'
_q='alaPethMainPseComboPort'
_p='alaPethMainPsePriority'
_o='alaPethMainPseCapacitorDetect'
_n='alaPethMainPsePriorityDisconnect'
_m='alaPethMainPseAdminStatus'
_l='alaPethPsePortPowerClass'
_k='alaPethPsePortPowerStatus'
_j='alaPethPsePortPowerActual'
_i='alaPethPsePortPowerMaximum'
_h='alaPethMainPseEntry'
_g='alaPethPsePortEntry'
_f='alaPethPowerPolicyName'
_e='minutes'
_d='not-accessible'
_c='alaPethMainChassisId'
_b='pethMainPsePower'
_a='pethTrapsGroup'
_Z='alaPethUpdateGroup'
_Y='alaPethPowerSlotGroup'
_X='alaPethPowerPortGroup'
_W='alaPethPowerPolicyGroup'
_V='alaPethPowerRuleGroup'
_U='alaPethMainChassisGroup'
_T='alaPethMainPseGroup'
_S='alaPethPsePortGroup'
_R='alaPethMainChassisAvailableReservePower'
_Q='alaPethMainChassisNumberOfPowerSupply'
_P='alaPethMainChassisPowerRedundancy'
_O='alaPethMainPseMaxPower'
_N='pethPsePortIndex'
_M='alaPethPowerRuleName'
_L='Bits'
_K='disable'
_J='enable'
_I='pethPsePortGroupIndex'
_H='SnmpAdminString'
_G='read-only'
_F='POWER-ETHERNET-MIB'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='current'
_A='ALCATEL-ENT1-INLINE-POWER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1InLinePower,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1InLinePower')
pethMainPseEntry,pethMainPsePower,pethPsePortEntry,pethPsePortGroupIndex,pethPsePortIndex=mibBuilder.importSymbols(_F,'pethMainPseEntry',_b,'pethPsePortEntry',_I,_N)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1INLINEPOWERMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,27,1))
if mibBuilder.loadTexts:alcatelIND1INLINEPOWERMIB.setRevisions(('2007-04-03 00:00',))
_AlaPethNotificationObjects_ObjectIdentity=ObjectIdentity
alaPethNotificationObjects=_AlaPethNotificationObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,27,1,0))
_AlaPethObjects_ObjectIdentity=ObjectIdentity
alaPethObjects=_AlaPethObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,27,1,1))
_AlaPethPsePortTable_Object=MibTable
alaPethPsePortTable=_AlaPethPsePortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,1))
if mibBuilder.loadTexts:alaPethPsePortTable.setStatus(_B)
_AlaPethPsePortEntry_Object=MibTableRow
alaPethPsePortEntry=_AlaPethPsePortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,1,1))
if mibBuilder.loadTexts:alaPethPsePortEntry.setStatus(_B)
class _AlaPethPsePortPowerMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3000,60000))
_AlaPethPsePortPowerMaximum_Type.__name__=_C
_AlaPethPsePortPowerMaximum_Object=MibTableColumn
alaPethPsePortPowerMaximum=_AlaPethPsePortPowerMaximum_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,1,1,1),_AlaPethPsePortPowerMaximum_Type())
alaPethPsePortPowerMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethPsePortPowerMaximum.setStatus(_B)
class _AlaPethPsePortPowerActual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_AlaPethPsePortPowerActual_Type.__name__=_C
_AlaPethPsePortPowerActual_Object=MibTableColumn
alaPethPsePortPowerActual=_AlaPethPsePortPowerActual_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,1,1,2),_AlaPethPsePortPowerActual_Type())
alaPethPsePortPowerActual.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethPsePortPowerActual.setStatus(_B)
class _AlaPethPsePortPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerOn',1),('powerOff',2)))
_AlaPethPsePortPowerStatus_Type.__name__=_C
_AlaPethPsePortPowerStatus_Object=MibTableColumn
alaPethPsePortPowerStatus=_AlaPethPsePortPowerStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,1,1,3),_AlaPethPsePortPowerStatus_Type())
alaPethPsePortPowerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethPsePortPowerStatus.setStatus(_B)
class _AlaPethPsePortPowerClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('class0',0),('class1',1),('class2',2),('class3',3),('class4',4),('class5',5)))
_AlaPethPsePortPowerClass_Type.__name__=_C
_AlaPethPsePortPowerClass_Object=MibTableColumn
alaPethPsePortPowerClass=_AlaPethPsePortPowerClass_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,1,1,4),_AlaPethPsePortPowerClass_Type())
alaPethPsePortPowerClass.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethPsePortPowerClass.setStatus(_B)
_AlaPethMainPseTable_Object=MibTable
alaPethMainPseTable=_AlaPethMainPseTable_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2))
if mibBuilder.loadTexts:alaPethMainPseTable.setStatus(_B)
_AlaPethMainPseEntry_Object=MibTableRow
alaPethMainPseEntry=_AlaPethMainPseEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1))
if mibBuilder.loadTexts:alaPethMainPseEntry.setStatus(_B)
class _AlaPethMainPseAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_AlaPethMainPseAdminStatus_Type.__name__=_C
_AlaPethMainPseAdminStatus_Object=MibTableColumn
alaPethMainPseAdminStatus=_AlaPethMainPseAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1,1),_AlaPethMainPseAdminStatus_Type())
alaPethMainPseAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainPseAdminStatus.setStatus(_B)
class _AlaPethMainPseMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(37,1500))
_AlaPethMainPseMaxPower_Type.__name__=_C
_AlaPethMainPseMaxPower_Object=MibTableColumn
alaPethMainPseMaxPower=_AlaPethMainPseMaxPower_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1,2),_AlaPethMainPseMaxPower_Type())
alaPethMainPseMaxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainPseMaxPower.setStatus(_B)
if mibBuilder.loadTexts:alaPethMainPseMaxPower.setUnits('Watts')
class _AlaPethMainPsePriorityDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AlaPethMainPsePriorityDisconnect_Type.__name__=_C
_AlaPethMainPsePriorityDisconnect_Object=MibTableColumn
alaPethMainPsePriorityDisconnect=_AlaPethMainPsePriorityDisconnect_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1,3),_AlaPethMainPsePriorityDisconnect_Type())
alaPethMainPsePriorityDisconnect.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainPsePriorityDisconnect.setStatus(_B)
class _AlaPethMainPseCapacitorDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AlaPethMainPseCapacitorDetect_Type.__name__=_C
_AlaPethMainPseCapacitorDetect_Object=MibTableColumn
alaPethMainPseCapacitorDetect=_AlaPethMainPseCapacitorDetect_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1,4),_AlaPethMainPseCapacitorDetect_Type())
alaPethMainPseCapacitorDetect.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainPseCapacitorDetect.setStatus(_B)
class _AlaPethMainPsePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_AlaPethMainPsePriority_Type.__name__=_C
_AlaPethMainPsePriority_Object=MibTableColumn
alaPethMainPsePriority=_AlaPethMainPsePriority_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1,5),_AlaPethMainPsePriority_Type())
alaPethMainPsePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainPsePriority.setStatus(_B)
class _AlaPethMainPseComboPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AlaPethMainPseComboPort_Type.__name__=_C
_AlaPethMainPseComboPort_Object=MibTableColumn
alaPethMainPseComboPort=_AlaPethMainPseComboPort_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1,6),_AlaPethMainPseComboPort_Type())
alaPethMainPseComboPort.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainPseComboPort.setStatus(_B)
class _AlaPethMainPseClassDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AlaPethMainPseClassDetection_Type.__name__=_C
_AlaPethMainPseClassDetection_Object=MibTableColumn
alaPethMainPseClassDetection=_AlaPethMainPseClassDetection_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,2,1,7),_AlaPethMainPseClassDetection_Type())
alaPethMainPseClassDetection.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainPseClassDetection.setStatus(_B)
_AlaPethMainChassisTable_Object=MibTable
alaPethMainChassisTable=_AlaPethMainChassisTable_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,3))
if mibBuilder.loadTexts:alaPethMainChassisTable.setStatus(_B)
_AlaPethMainChassisEntry_Object=MibTableRow
alaPethMainChassisEntry=_AlaPethMainChassisEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,3,1))
alaPethMainChassisEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:alaPethMainChassisEntry.setStatus(_B)
class _AlaPethMainChassisId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AlaPethMainChassisId_Type.__name__=_C
_AlaPethMainChassisId_Object=MibTableColumn
alaPethMainChassisId=_AlaPethMainChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,3,1,1),_AlaPethMainChassisId_Type())
alaPethMainChassisId.setMaxAccess(_d)
if mibBuilder.loadTexts:alaPethMainChassisId.setStatus(_B)
class _AlaPethMainChassisPowerRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AlaPethMainChassisPowerRedundancy_Type.__name__=_C
_AlaPethMainChassisPowerRedundancy_Object=MibTableColumn
alaPethMainChassisPowerRedundancy=_AlaPethMainChassisPowerRedundancy_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,3,1,2),_AlaPethMainChassisPowerRedundancy_Type())
alaPethMainChassisPowerRedundancy.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainChassisPowerRedundancy.setStatus(_B)
class _AlaPethMainChassisDynamicPowerManagement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AlaPethMainChassisDynamicPowerManagement_Type.__name__=_C
_AlaPethMainChassisDynamicPowerManagement_Object=MibTableColumn
alaPethMainChassisDynamicPowerManagement=_AlaPethMainChassisDynamicPowerManagement_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,3,1,3),_AlaPethMainChassisDynamicPowerManagement_Type())
alaPethMainChassisDynamicPowerManagement.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethMainChassisDynamicPowerManagement.setStatus(_B)
class _AlaPethMainChassisNumberOfPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AlaPethMainChassisNumberOfPowerSupply_Type.__name__=_C
_AlaPethMainChassisNumberOfPowerSupply_Object=MibTableColumn
alaPethMainChassisNumberOfPowerSupply=_AlaPethMainChassisNumberOfPowerSupply_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,3,1,4),_AlaPethMainChassisNumberOfPowerSupply_Type())
alaPethMainChassisNumberOfPowerSupply.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethMainChassisNumberOfPowerSupply.setStatus(_B)
if mibBuilder.loadTexts:alaPethMainChassisNumberOfPowerSupply.setUnits('scaler')
_AlaPethMainChassisAvailableReservePower_Type=Integer32
_AlaPethMainChassisAvailableReservePower_Object=MibTableColumn
alaPethMainChassisAvailableReservePower=_AlaPethMainChassisAvailableReservePower_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,3,1,5),_AlaPethMainChassisAvailableReservePower_Type())
alaPethMainChassisAvailableReservePower.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethMainChassisAvailableReservePower.setStatus(_B)
if mibBuilder.loadTexts:alaPethMainChassisAvailableReservePower.setUnits('watts')
_AlaPethPowerRuleTable_Object=MibTable
alaPethPowerRuleTable=_AlaPethPowerRuleTable_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4))
if mibBuilder.loadTexts:alaPethPowerRuleTable.setStatus(_B)
_AlaPethPowerRuleEntry_Object=MibTableRow
alaPethPowerRuleEntry=_AlaPethPowerRuleEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1))
alaPethPowerRuleEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:alaPethPowerRuleEntry.setStatus(_B)
class _AlaPethPowerRuleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaPethPowerRuleName_Type.__name__=_H
_AlaPethPowerRuleName_Object=MibTableColumn
alaPethPowerRuleName=_AlaPethPowerRuleName_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,1),_AlaPethPowerRuleName_Type())
alaPethPowerRuleName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleName.setStatus(_B)
class _AlaPethPowerRuleAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaPethPowerRuleAdminStatus_Type.__name__=_C
_AlaPethPowerRuleAdminStatus_Object=MibTableColumn
alaPethPowerRuleAdminStatus=_AlaPethPowerRuleAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,2),_AlaPethPowerRuleAdminStatus_Type())
alaPethPowerRuleAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleAdminStatus.setStatus(_B)
class _AlaPethPowerRulePowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_AlaPethPowerRulePowerStatus_Type.__name__=_C
_AlaPethPowerRulePowerStatus_Object=MibTableColumn
alaPethPowerRulePowerStatus=_AlaPethPowerRulePowerStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,3),_AlaPethPowerRulePowerStatus_Type())
alaPethPowerRulePowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRulePowerStatus.setStatus(_B)
class _AlaPethPowerRuleAtMinute_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,59))
_AlaPethPowerRuleAtMinute_Type.__name__=_C
_AlaPethPowerRuleAtMinute_Object=MibTableColumn
alaPethPowerRuleAtMinute=_AlaPethPowerRuleAtMinute_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,4),_AlaPethPowerRuleAtMinute_Type())
alaPethPowerRuleAtMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleAtMinute.setStatus(_B)
if mibBuilder.loadTexts:alaPethPowerRuleAtMinute.setUnits(_e)
class _AlaPethPowerRuleAtTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1439))
_AlaPethPowerRuleAtTime_Type.__name__=_C
_AlaPethPowerRuleAtTime_Object=MibTableColumn
alaPethPowerRuleAtTime=_AlaPethPowerRuleAtTime_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,5),_AlaPethPowerRuleAtTime_Type())
alaPethPowerRuleAtTime.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleAtTime.setStatus(_B)
if mibBuilder.loadTexts:alaPethPowerRuleAtTime.setUnits(_e)
class _AlaPethPowerRuleDaysOfWeek_Type(Bits):defaultBinValue='1111111';namedValues=NamedValues(*(('sun',0),('mon',1),('tue',2),('wed',3),('thu',4),('fri',5),('sat',6)))
_AlaPethPowerRuleDaysOfWeek_Type.__name__=_L
_AlaPethPowerRuleDaysOfWeek_Object=MibTableColumn
alaPethPowerRuleDaysOfWeek=_AlaPethPowerRuleDaysOfWeek_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,6),_AlaPethPowerRuleDaysOfWeek_Type())
alaPethPowerRuleDaysOfWeek.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleDaysOfWeek.setStatus(_B)
class _AlaPethPowerRuleDaysOfMonth_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('d1',0),('d2',1),('d3',2),('d4',3),('d5',4),('d6',5),('d7',6),('d8',7),('d9',8),('d10',9),('d11',10),('d12',11),('d13',12),('d14',13),('d15',14),('d16',15),('d17',16),('d18',17),('d19',18),('d20',19),('d21',20),('d22',21),('d23',22),('d24',23),('d25',24),('d26',25),('d27',26),('d28',27),('d29',28),('d30',29),('d31',30)))
_AlaPethPowerRuleDaysOfMonth_Type.__name__=_L
_AlaPethPowerRuleDaysOfMonth_Object=MibTableColumn
alaPethPowerRuleDaysOfMonth=_AlaPethPowerRuleDaysOfMonth_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,7),_AlaPethPowerRuleDaysOfMonth_Type())
alaPethPowerRuleDaysOfMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleDaysOfMonth.setStatus(_B)
class _AlaPethPowerRuleMonths_Type(Bits):defaultBinValue='111111111111';namedValues=NamedValues(*(('jan',0),('feb',1),('mar',2),('apr',3),('may',4),('jun',5),('jul',6),('aug',7),('sep',8),('oct',9),('nov',10),('dec',11)))
_AlaPethPowerRuleMonths_Type.__name__=_L
_AlaPethPowerRuleMonths_Object=MibTableColumn
alaPethPowerRuleMonths=_AlaPethPowerRuleMonths_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,8),_AlaPethPowerRuleMonths_Type())
alaPethPowerRuleMonths.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleMonths.setStatus(_B)
class _AlaPethPowerRuleTimezone_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('localServer',1),('originatorServer',2),('utc',3)))
_AlaPethPowerRuleTimezone_Type.__name__=_C
_AlaPethPowerRuleTimezone_Object=MibTableColumn
alaPethPowerRuleTimezone=_AlaPethPowerRuleTimezone_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,9),_AlaPethPowerRuleTimezone_Type())
alaPethPowerRuleTimezone.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleTimezone.setStatus(_B)
_AlaPethPowerRuleRowStatus_Type=RowStatus
_AlaPethPowerRuleRowStatus_Object=MibTableColumn
alaPethPowerRuleRowStatus=_AlaPethPowerRuleRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,4,1,10),_AlaPethPowerRuleRowStatus_Type())
alaPethPowerRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerRuleRowStatus.setStatus(_B)
_AlaPethPowerPolicyTable_Object=MibTable
alaPethPowerPolicyTable=_AlaPethPowerPolicyTable_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,5))
if mibBuilder.loadTexts:alaPethPowerPolicyTable.setStatus(_B)
_AlaPethPowerPolicyEntry_Object=MibTableRow
alaPethPowerPolicyEntry=_AlaPethPowerPolicyEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,5,1))
alaPethPowerPolicyEntry.setIndexNames((0,_A,_f),(0,_A,_M))
if mibBuilder.loadTexts:alaPethPowerPolicyEntry.setStatus(_B)
class _AlaPethPowerPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaPethPowerPolicyName_Type.__name__=_H
_AlaPethPowerPolicyName_Object=MibTableColumn
alaPethPowerPolicyName=_AlaPethPowerPolicyName_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,5,1,1),_AlaPethPowerPolicyName_Type())
alaPethPowerPolicyName.setMaxAccess(_d)
if mibBuilder.loadTexts:alaPethPowerPolicyName.setStatus(_B)
_AlaPethPowerPolicyRowStatus_Type=RowStatus
_AlaPethPowerPolicyRowStatus_Object=MibTableColumn
alaPethPowerPolicyRowStatus=_AlaPethPowerPolicyRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,5,1,2),_AlaPethPowerPolicyRowStatus_Type())
alaPethPowerPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerPolicyRowStatus.setStatus(_B)
_AlaPethPowerPortTable_Object=MibTable
alaPethPowerPortTable=_AlaPethPowerPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,6))
if mibBuilder.loadTexts:alaPethPowerPortTable.setStatus(_B)
_AlaPethPowerPortEntry_Object=MibTableRow
alaPethPowerPortEntry=_AlaPethPowerPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,6,1))
alaPethPowerPortEntry.setIndexNames((0,_F,_I),(0,_F,_N))
if mibBuilder.loadTexts:alaPethPowerPortEntry.setStatus(_B)
class _AlaPethPowerPortPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaPethPowerPortPolicyName_Type.__name__=_H
_AlaPethPowerPortPolicyName_Object=MibTableColumn
alaPethPowerPortPolicyName=_AlaPethPowerPortPolicyName_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,6,1,1),_AlaPethPowerPortPolicyName_Type())
alaPethPowerPortPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerPortPolicyName.setStatus(_B)
_AlaPethPowerPortRowStatus_Type=RowStatus
_AlaPethPowerPortRowStatus_Object=MibTableColumn
alaPethPowerPortRowStatus=_AlaPethPowerPortRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,6,1,2),_AlaPethPowerPortRowStatus_Type())
alaPethPowerPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerPortRowStatus.setStatus(_B)
_AlaPethPowerSlotTable_Object=MibTable
alaPethPowerSlotTable=_AlaPethPowerSlotTable_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,7))
if mibBuilder.loadTexts:alaPethPowerSlotTable.setStatus(_B)
_AlaPethPowerSlotEntry_Object=MibTableRow
alaPethPowerSlotEntry=_AlaPethPowerSlotEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,7,1))
alaPethPowerSlotEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:alaPethPowerSlotEntry.setStatus(_B)
class _AlaPethPowerSlotPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaPethPowerSlotPolicyName_Type.__name__=_H
_AlaPethPowerSlotPolicyName_Object=MibTableColumn
alaPethPowerSlotPolicyName=_AlaPethPowerSlotPolicyName_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,7,1,1),_AlaPethPowerSlotPolicyName_Type())
alaPethPowerSlotPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerSlotPolicyName.setStatus(_B)
_AlaPethPowerSlotRowStatus_Type=RowStatus
_AlaPethPowerSlotRowStatus_Object=MibTableColumn
alaPethPowerSlotRowStatus=_AlaPethPowerSlotRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,7,1,2),_AlaPethPowerSlotRowStatus_Type())
alaPethPowerSlotRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPowerSlotRowStatus.setStatus(_B)
_AlaPethUpdate_ObjectIdentity=ObjectIdentity
alaPethUpdate=_AlaPethUpdate_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,8))
class _AlaPethUpdatePortGroupIndex_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_AlaPethUpdatePortGroupIndex_Type.__name__=_C
_AlaPethUpdatePortGroupIndex_Object=MibScalar
alaPethUpdatePortGroupIndex=_AlaPethUpdatePortGroupIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,8,1),_AlaPethUpdatePortGroupIndex_Type())
alaPethUpdatePortGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethUpdatePortGroupIndex.setStatus(_B)
class _AlaPethUpdateFilename_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaPethUpdateFilename_Type.__name__=_H
_AlaPethUpdateFilename_Object=MibScalar
alaPethUpdateFilename=_AlaPethUpdateFilename_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,8,2),_AlaPethUpdateFilename_Type())
alaPethUpdateFilename.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethUpdateFilename.setStatus(_B)
class _AlaPethUpdateAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('doUpdate',2)))
_AlaPethUpdateAction_Type.__name__=_C
_AlaPethUpdateAction_Object=MibScalar
alaPethUpdateAction=_AlaPethUpdateAction_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,8,3),_AlaPethUpdateAction_Type())
alaPethUpdateAction.setMaxAccess(_E)
if mibBuilder.loadTexts:alaPethUpdateAction.setStatus(_B)
class _AlaPethUpdateStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inProgress',1),('doneOk',2),('doneNotOk',3),('noOp',4)))
_AlaPethUpdateStatus_Type.__name__=_C
_AlaPethUpdateStatus_Object=MibScalar
alaPethUpdateStatus=_AlaPethUpdateStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,8,4),_AlaPethUpdateStatus_Type())
alaPethUpdateStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethUpdateStatus.setStatus(_B)
class _AlaPethUpdateErrorCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('noError',1),('notAllSlotsUpdated',2),('noUpdateStatusErr',3),('programmingImageBadErr',4),('programmingFailed',5),('controllerFileChecksumErr',6),('controllerFileReadErr',7),('controllerFileStatusErr',8),('controllerFileWriteErr',9),('dataErr',10),('dataConflictErr',11),('invalidResponseErr',12),('programUndefinedErr',13)))
_AlaPethUpdateErrorCode_Type.__name__=_C
_AlaPethUpdateErrorCode_Object=MibScalar
alaPethUpdateErrorCode=_AlaPethUpdateErrorCode_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,8,5),_AlaPethUpdateErrorCode_Type())
alaPethUpdateErrorCode.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethUpdateErrorCode.setStatus(_B)
class _AlaPethUpdateErrorString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPethUpdateErrorString_Type.__name__=_H
_AlaPethUpdateErrorString_Object=MibScalar
alaPethUpdateErrorString=_AlaPethUpdateErrorString_Object((1,3,6,1,4,1,6486,801,1,2,1,27,1,1,8,6),_AlaPethUpdateErrorString_Type())
alaPethUpdateErrorString.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPethUpdateErrorString.setStatus(_B)
_AlaPethConformance_ObjectIdentity=ObjectIdentity
alaPethConformance=_AlaPethConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,27,1,2))
_AlaPethCompliances_ObjectIdentity=ObjectIdentity
alaPethCompliances=_AlaPethCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,1))
_AlaPethGroups_ObjectIdentity=ObjectIdentity
alaPethGroups=_AlaPethGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2))
pethPsePortEntry.registerAugmentions((_A,_g))
alaPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_A,_h))
alaPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
alaPethPsePortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,1))
alaPethPsePortGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:alaPethPsePortGroup.setStatus(_B)
alaPethMainPseGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,2))
alaPethMainPseGroup.setObjects(*((_A,_m),(_A,_O),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:alaPethMainPseGroup.setStatus(_B)
alaPethMainChassisGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,3))
alaPethMainChassisGroup.setObjects(*((_A,_P),(_A,_s),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:alaPethMainChassisGroup.setStatus(_B)
alaPethPowerRuleGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,4))
alaPethPowerRuleGroup.setObjects(*((_A,_M),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:alaPethPowerRuleGroup.setStatus(_B)
alaPethPowerPolicyGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,5))
alaPethPowerPolicyGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:alaPethPowerPolicyGroup.setStatus(_B)
alaPethPowerPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,6))
alaPethPowerPortGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:alaPethPowerPortGroup.setStatus(_B)
alaPethPowerSlotGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,7))
alaPethPowerSlotGroup.setObjects(*((_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:alaPethPowerSlotGroup.setStatus(_B)
alaPethUpdateGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,8))
alaPethUpdateGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:alaPethUpdateGroup.setStatus(_B)
alaPethPwrSupplyConflictTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,27,1,0,1))
alaPethPwrSupplyConflictTrap.setObjects((_F,_I))
if mibBuilder.loadTexts:alaPethPwrSupplyConflictTrap.setStatus(_B)
alaPethPwrSupplyNotSupportedTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,27,1,0,2))
alaPethPwrSupplyNotSupportedTrap.setObjects(*((_F,_I),(_F,_N)))
if mibBuilder.loadTexts:alaPethPwrSupplyNotSupportedTrap.setStatus(_B)
pethMainPowerUsageNIFailNotification=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,27,1,0,3))
pethMainPowerUsageNIFailNotification.setObjects(*((_F,_I),(_A,_Q),(_A,_P),(_F,_b),(_A,_O),(_A,_R)))
if mibBuilder.loadTexts:pethMainPowerUsageNIFailNotification.setStatus(_B)
pethTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,2,9))
pethTrapsGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:pethTrapsGroup.setStatus(_B)
alaPethCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,1,1))
alaPethCompliance.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:alaPethCompliance.setStatus(_B)
alaPethPseCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,27,1,2,1,2))
alaPethPseCompliance.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:alaPethPseCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1INLINEPOWERMIB':alcatelIND1INLINEPOWERMIB,'alaPethNotificationObjects':alaPethNotificationObjects,_AD:alaPethPwrSupplyConflictTrap,_AE:alaPethPwrSupplyNotSupportedTrap,_AF:pethMainPowerUsageNIFailNotification,'alaPethObjects':alaPethObjects,'alaPethPsePortTable':alaPethPsePortTable,_g:alaPethPsePortEntry,_i:alaPethPsePortPowerMaximum,_j:alaPethPsePortPowerActual,_k:alaPethPsePortPowerStatus,_l:alaPethPsePortPowerClass,'alaPethMainPseTable':alaPethMainPseTable,_h:alaPethMainPseEntry,_m:alaPethMainPseAdminStatus,_O:alaPethMainPseMaxPower,_n:alaPethMainPsePriorityDisconnect,_o:alaPethMainPseCapacitorDetect,_p:alaPethMainPsePriority,_q:alaPethMainPseComboPort,_r:alaPethMainPseClassDetection,'alaPethMainChassisTable':alaPethMainChassisTable,'alaPethMainChassisEntry':alaPethMainChassisEntry,_c:alaPethMainChassisId,_P:alaPethMainChassisPowerRedundancy,_s:alaPethMainChassisDynamicPowerManagement,_Q:alaPethMainChassisNumberOfPowerSupply,_R:alaPethMainChassisAvailableReservePower,'alaPethPowerRuleTable':alaPethPowerRuleTable,'alaPethPowerRuleEntry':alaPethPowerRuleEntry,_M:alaPethPowerRuleName,_t:alaPethPowerRuleAdminStatus,_u:alaPethPowerRulePowerStatus,_v:alaPethPowerRuleAtMinute,_A1:alaPethPowerRuleAtTime,_w:alaPethPowerRuleDaysOfWeek,_x:alaPethPowerRuleDaysOfMonth,_y:alaPethPowerRuleMonths,_z:alaPethPowerRuleTimezone,_A0:alaPethPowerRuleRowStatus,'alaPethPowerPolicyTable':alaPethPowerPolicyTable,'alaPethPowerPolicyEntry':alaPethPowerPolicyEntry,_f:alaPethPowerPolicyName,_A2:alaPethPowerPolicyRowStatus,'alaPethPowerPortTable':alaPethPowerPortTable,'alaPethPowerPortEntry':alaPethPowerPortEntry,_A3:alaPethPowerPortPolicyName,_A4:alaPethPowerPortRowStatus,'alaPethPowerSlotTable':alaPethPowerSlotTable,'alaPethPowerSlotEntry':alaPethPowerSlotEntry,_A5:alaPethPowerSlotPolicyName,_A6:alaPethPowerSlotRowStatus,'alaPethUpdate':alaPethUpdate,_A7:alaPethUpdatePortGroupIndex,_A8:alaPethUpdateFilename,_A9:alaPethUpdateAction,_AA:alaPethUpdateStatus,_AB:alaPethUpdateErrorCode,_AC:alaPethUpdateErrorString,'alaPethConformance':alaPethConformance,'alaPethCompliances':alaPethCompliances,'alaPethCompliance':alaPethCompliance,'alaPethPseCompliance':alaPethPseCompliance,'alaPethGroups':alaPethGroups,_S:alaPethPsePortGroup,_T:alaPethMainPseGroup,_U:alaPethMainChassisGroup,_V:alaPethPowerRuleGroup,_W:alaPethPowerPolicyGroup,_X:alaPethPowerPortGroup,_Y:alaPethPowerSlotGroup,_Z:alaPethUpdateGroup,_a:pethTrapsGroup})