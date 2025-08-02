_AR='cisco6400RedundantGroup2'
_AQ='cisco6400RedundantGroup'
_AP='c64ChassisAlarmACOStatus'
_AO='c64ChassisAlarmSeverity'
_AN='c64ChassisAlarmType'
_AM='c64ChassisAlarmSource'
_AL='c64ChassisTempThresholdAdmin'
_AK='c64ChassisTempCoreMajorThreshold'
_AJ='c64ChassisTempCoreMinorThreshold'
_AI='c64ChassisTempIntakeMajorThreshold'
_AH='c64ChassisTempIntakeMinorThreshold'
_AG='c64ChassisClearAlarms'
_AF='c64SubSlotConfigPrefIndex'
_AE='c64SlotConfigPrefIndex'
_AD='c64PortConfigPort2Index'
_AC='c64PortConfigSubModule2Index'
_AB='c64PortConfigModule2Index'
_AA='c64PortConfigPort1Index'
_A9='c64PortConfigSubModule1Index'
_A8='c64PortConfigModule1Index'
_A7='c64SubSlotConfigSubModule2Index'
_A6='c64SubSlotConfigModule2Index'
_A5='c64SubSlotConfigSubModule1Index'
_A4='c64SubSlotConfigModule1Index'
_A3='c64SlotConfigModule2Index'
_A2='c64SlotConfigModule1Index'
_A1='cisco6400ChassisMIBGroup'
_A0='c64ChassisFacilityAlarmStatus'
_z='c64SonetAPSChannelStatus'
_y='c64SonetAPSProtectPortStatus'
_x='c64SonetAPSProtectPathFEBE'
_w='c64SonetAPSProtectPathBIPE'
_v='c64SonetAPSProtectLineFEBE'
_u='c64SonetAPSProtectLineBIPE'
_t='c64SonetAPSProtectSectionBIPE'
_s='c64SonetAPSProtectPathStatus'
_r='c64SonetAPSProtectLineStatus'
_q='c64SonetAPSProtectSectionStatus'
_p='c64SonetAPSWorkPortStatus'
_o='c64SonetAPSWorkPathFEBE'
_n='c64SonetAPSWorkPathBIPE'
_m='c64SonetAPSWorkLineFEBE'
_l='c64SonetAPSWorkLineBIPE'
_k='c64SonetAPSWorkSectionBIPE'
_j='c64SonetAPSWorkPathStatus'
_i='c64SonetAPSWorkLineStatus'
_h='c64SonetAPSWorkSectionStatus'
_g='c64SonetAPSSFBERThreshold'
_f='c64SonetAPSSwitchCmd'
_e='c64SonetAPSBERThreshold'
_d='c64SonetAPSMode'
_c='c64PortConfigStatus'
_b='c64PortSwitchOver'
_a='c64PortConfigPrefIndex'
_Z='c64Port2Name'
_Y='c64Port1Name'
_X='c64SubSlotConfigStatus'
_W='c64SubSlotSwitchOver'
_V='c64SubSlot2Name'
_U='c64SubSlot1Name'
_T='c64SlotConfigStatus'
_S='c64SlotSwitchOver'
_R='c64Slot2Name'
_Q='c64Slot1Name'
_P='c64MainCPUSwitchOver'
_O='c64MainCPUConfigAutoSync'
_N='c64ChassisAlarmIndex'
_M='c64SubSlotRedundantIndex'
_L='ifIndex'
_K='IF-MIB'
_J='deprecated'
_I='forceOver'
_H='ok'
_G='read-write'
_F='read-create'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='current'
_A='CISCO-6400-CHASSIS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
cisco6400ChassisMIB=ModuleIdentity((1,3,6,1,4,1,9,10,27))
if mibBuilder.loadTexts:cisco6400ChassisMIB.setRevisions(('2001-10-22 00:00','2001-05-10 12:34','2000-09-25 12:34','1999-03-22 00:00','1998-08-05 00:00','1997-12-10 00:00'))
class APSEventStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('good',1),('noHardware',2),('doNotRevert',3),('manualSwitch',4),('signgalDegrade',5),('forceSwitch',6),('lockOut',7),('adminDown',8)))
_Cisco6400ChassisMIBObjects_ObjectIdentity=ObjectIdentity
cisco6400ChassisMIBObjects=_Cisco6400ChassisMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,27,1))
_C64RedundantGroup_ObjectIdentity=ObjectIdentity
c64RedundantGroup=_C64RedundantGroup_ObjectIdentity((1,3,6,1,4,1,9,10,27,1,1))
class _C64MainCPUConfigAutoSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_C64MainCPUConfigAutoSync_Type.__name__=_C
_C64MainCPUConfigAutoSync_Object=MibScalar
c64MainCPUConfigAutoSync=_C64MainCPUConfigAutoSync_Object((1,3,6,1,4,1,9,10,27,1,1,1),_C64MainCPUConfigAutoSync_Type())
c64MainCPUConfigAutoSync.setMaxAccess(_G)
if mibBuilder.loadTexts:c64MainCPUConfigAutoSync.setStatus(_B)
class _C64MainCPUSwitchOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_C64MainCPUSwitchOver_Type.__name__=_C
_C64MainCPUSwitchOver_Object=MibScalar
c64MainCPUSwitchOver=_C64MainCPUSwitchOver_Object((1,3,6,1,4,1,9,10,27,1,1,2),_C64MainCPUSwitchOver_Type())
c64MainCPUSwitchOver.setMaxAccess(_G)
if mibBuilder.loadTexts:c64MainCPUSwitchOver.setStatus(_B)
_C64SlotConfigTable_Object=MibTable
c64SlotConfigTable=_C64SlotConfigTable_Object((1,3,6,1,4,1,9,10,27,1,1,3))
if mibBuilder.loadTexts:c64SlotConfigTable.setStatus(_B)
_C64SlotConfigEntry_Object=MibTableRow
c64SlotConfigEntry=_C64SlotConfigEntry_Object((1,3,6,1,4,1,9,10,27,1,1,3,1))
c64SlotConfigEntry.setIndexNames((0,_A,_A2),(0,_A,_A3))
if mibBuilder.loadTexts:c64SlotConfigEntry.setStatus(_B)
class _C64SlotConfigModule1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_C64SlotConfigModule1Index_Type.__name__=_C
_C64SlotConfigModule1Index_Object=MibTableColumn
c64SlotConfigModule1Index=_C64SlotConfigModule1Index_Object((1,3,6,1,4,1,9,10,27,1,1,3,1,1),_C64SlotConfigModule1Index_Type())
c64SlotConfigModule1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64SlotConfigModule1Index.setStatus(_B)
class _C64SlotConfigModule2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_C64SlotConfigModule2Index_Type.__name__=_C
_C64SlotConfigModule2Index_Object=MibTableColumn
c64SlotConfigModule2Index=_C64SlotConfigModule2Index_Object((1,3,6,1,4,1,9,10,27,1,1,3,1,2),_C64SlotConfigModule2Index_Type())
c64SlotConfigModule2Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64SlotConfigModule2Index.setStatus(_B)
_C64Slot1Name_Type=DisplayString
_C64Slot1Name_Object=MibTableColumn
c64Slot1Name=_C64Slot1Name_Object((1,3,6,1,4,1,9,10,27,1,1,3,1,3),_C64Slot1Name_Type())
c64Slot1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:c64Slot1Name.setStatus(_B)
_C64Slot2Name_Type=DisplayString
_C64Slot2Name_Object=MibTableColumn
c64Slot2Name=_C64Slot2Name_Object((1,3,6,1,4,1,9,10,27,1,1,3,1,4),_C64Slot2Name_Type())
c64Slot2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:c64Slot2Name.setStatus(_B)
class _C64SlotConfigPrefIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primarySlot',1),('secondarySlot',2)))
_C64SlotConfigPrefIndex_Type.__name__=_C
_C64SlotConfigPrefIndex_Object=MibTableColumn
c64SlotConfigPrefIndex=_C64SlotConfigPrefIndex_Object((1,3,6,1,4,1,9,10,27,1,1,3,1,5),_C64SlotConfigPrefIndex_Type())
c64SlotConfigPrefIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SlotConfigPrefIndex.setStatus(_J)
class _C64SlotSwitchOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_C64SlotSwitchOver_Type.__name__=_C
_C64SlotSwitchOver_Object=MibTableColumn
c64SlotSwitchOver=_C64SlotSwitchOver_Object((1,3,6,1,4,1,9,10,27,1,1,3,1,6),_C64SlotSwitchOver_Type())
c64SlotSwitchOver.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SlotSwitchOver.setStatus(_B)
_C64SlotConfigStatus_Type=RowStatus
_C64SlotConfigStatus_Object=MibTableColumn
c64SlotConfigStatus=_C64SlotConfigStatus_Object((1,3,6,1,4,1,9,10,27,1,1,3,1,7),_C64SlotConfigStatus_Type())
c64SlotConfigStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SlotConfigStatus.setStatus(_B)
_C64SubSlotConfigTable_Object=MibTable
c64SubSlotConfigTable=_C64SubSlotConfigTable_Object((1,3,6,1,4,1,9,10,27,1,1,5))
if mibBuilder.loadTexts:c64SubSlotConfigTable.setStatus(_B)
_C64SubSlotConfigEntry_Object=MibTableRow
c64SubSlotConfigEntry=_C64SubSlotConfigEntry_Object((1,3,6,1,4,1,9,10,27,1,1,5,1))
c64SubSlotConfigEntry.setIndexNames((0,_A,_A4),(0,_A,_A5),(0,_A,_A6),(0,_A,_A7),(0,_A,_M))
if mibBuilder.loadTexts:c64SubSlotConfigEntry.setStatus(_B)
class _C64SubSlotRedundantIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64SubSlotRedundantIndex_Type.__name__=_C
_C64SubSlotRedundantIndex_Object=MibTableColumn
c64SubSlotRedundantIndex=_C64SubSlotRedundantIndex_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,1),_C64SubSlotRedundantIndex_Type())
c64SubSlotRedundantIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:c64SubSlotRedundantIndex.setStatus(_B)
class _C64SubSlotConfigModule1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_C64SubSlotConfigModule1Index_Type.__name__=_C
_C64SubSlotConfigModule1Index_Object=MibTableColumn
c64SubSlotConfigModule1Index=_C64SubSlotConfigModule1Index_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,2),_C64SubSlotConfigModule1Index_Type())
c64SubSlotConfigModule1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64SubSlotConfigModule1Index.setStatus(_B)
class _C64SubSlotConfigSubModule1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_C64SubSlotConfigSubModule1Index_Type.__name__=_C
_C64SubSlotConfigSubModule1Index_Object=MibTableColumn
c64SubSlotConfigSubModule1Index=_C64SubSlotConfigSubModule1Index_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,3),_C64SubSlotConfigSubModule1Index_Type())
c64SubSlotConfigSubModule1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64SubSlotConfigSubModule1Index.setStatus(_B)
class _C64SubSlotConfigModule2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_C64SubSlotConfigModule2Index_Type.__name__=_C
_C64SubSlotConfigModule2Index_Object=MibTableColumn
c64SubSlotConfigModule2Index=_C64SubSlotConfigModule2Index_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,4),_C64SubSlotConfigModule2Index_Type())
c64SubSlotConfigModule2Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64SubSlotConfigModule2Index.setStatus(_B)
class _C64SubSlotConfigSubModule2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_C64SubSlotConfigSubModule2Index_Type.__name__=_C
_C64SubSlotConfigSubModule2Index_Object=MibTableColumn
c64SubSlotConfigSubModule2Index=_C64SubSlotConfigSubModule2Index_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,5),_C64SubSlotConfigSubModule2Index_Type())
c64SubSlotConfigSubModule2Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64SubSlotConfigSubModule2Index.setStatus(_B)
_C64SubSlot1Name_Type=DisplayString
_C64SubSlot1Name_Object=MibTableColumn
c64SubSlot1Name=_C64SubSlot1Name_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,6),_C64SubSlot1Name_Type())
c64SubSlot1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SubSlot1Name.setStatus(_B)
_C64SubSlot2Name_Type=DisplayString
_C64SubSlot2Name_Object=MibTableColumn
c64SubSlot2Name=_C64SubSlot2Name_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,7),_C64SubSlot2Name_Type())
c64SubSlot2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SubSlot2Name.setStatus(_B)
class _C64SubSlotConfigPrefIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primarySubslot',1),('secondarySubslot',2)))
_C64SubSlotConfigPrefIndex_Type.__name__=_C
_C64SubSlotConfigPrefIndex_Object=MibTableColumn
c64SubSlotConfigPrefIndex=_C64SubSlotConfigPrefIndex_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,8),_C64SubSlotConfigPrefIndex_Type())
c64SubSlotConfigPrefIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SubSlotConfigPrefIndex.setStatus(_J)
class _C64SubSlotSwitchOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_C64SubSlotSwitchOver_Type.__name__=_C
_C64SubSlotSwitchOver_Object=MibTableColumn
c64SubSlotSwitchOver=_C64SubSlotSwitchOver_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,9),_C64SubSlotSwitchOver_Type())
c64SubSlotSwitchOver.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SubSlotSwitchOver.setStatus(_B)
_C64SubSlotConfigStatus_Type=RowStatus
_C64SubSlotConfigStatus_Object=MibTableColumn
c64SubSlotConfigStatus=_C64SubSlotConfigStatus_Object((1,3,6,1,4,1,9,10,27,1,1,5,1,10),_C64SubSlotConfigStatus_Type())
c64SubSlotConfigStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SubSlotConfigStatus.setStatus(_B)
_C64PortConfigTable_Object=MibTable
c64PortConfigTable=_C64PortConfigTable_Object((1,3,6,1,4,1,9,10,27,1,1,6))
if mibBuilder.loadTexts:c64PortConfigTable.setStatus(_B)
_C64PortConfigEntry_Object=MibTableRow
c64PortConfigEntry=_C64PortConfigEntry_Object((1,3,6,1,4,1,9,10,27,1,1,6,1))
c64PortConfigEntry.setIndexNames((0,_A,_A8),(0,_A,_A9),(0,_A,_AA),(0,_A,_AB),(0,_A,_AC),(0,_A,_AD),(0,_A,_M))
if mibBuilder.loadTexts:c64PortConfigEntry.setStatus(_B)
class _C64PortConfigModule1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_C64PortConfigModule1Index_Type.__name__=_C
_C64PortConfigModule1Index_Object=MibTableColumn
c64PortConfigModule1Index=_C64PortConfigModule1Index_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,1),_C64PortConfigModule1Index_Type())
c64PortConfigModule1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64PortConfigModule1Index.setStatus(_B)
class _C64PortConfigSubModule1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_C64PortConfigSubModule1Index_Type.__name__=_C
_C64PortConfigSubModule1Index_Object=MibTableColumn
c64PortConfigSubModule1Index=_C64PortConfigSubModule1Index_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,2),_C64PortConfigSubModule1Index_Type())
c64PortConfigSubModule1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64PortConfigSubModule1Index.setStatus(_B)
class _C64PortConfigPort1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_C64PortConfigPort1Index_Type.__name__=_C
_C64PortConfigPort1Index_Object=MibTableColumn
c64PortConfigPort1Index=_C64PortConfigPort1Index_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,3),_C64PortConfigPort1Index_Type())
c64PortConfigPort1Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64PortConfigPort1Index.setStatus(_B)
class _C64PortConfigModule2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_C64PortConfigModule2Index_Type.__name__=_C
_C64PortConfigModule2Index_Object=MibTableColumn
c64PortConfigModule2Index=_C64PortConfigModule2Index_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,4),_C64PortConfigModule2Index_Type())
c64PortConfigModule2Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64PortConfigModule2Index.setStatus(_B)
class _C64PortConfigSubModule2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_C64PortConfigSubModule2Index_Type.__name__=_C
_C64PortConfigSubModule2Index_Object=MibTableColumn
c64PortConfigSubModule2Index=_C64PortConfigSubModule2Index_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,5),_C64PortConfigSubModule2Index_Type())
c64PortConfigSubModule2Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64PortConfigSubModule2Index.setStatus(_B)
class _C64PortConfigPort2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_C64PortConfigPort2Index_Type.__name__=_C
_C64PortConfigPort2Index_Object=MibTableColumn
c64PortConfigPort2Index=_C64PortConfigPort2Index_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,6),_C64PortConfigPort2Index_Type())
c64PortConfigPort2Index.setMaxAccess(_E)
if mibBuilder.loadTexts:c64PortConfigPort2Index.setStatus(_B)
_C64Port1Name_Type=DisplayString
_C64Port1Name_Object=MibTableColumn
c64Port1Name=_C64Port1Name_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,7),_C64Port1Name_Type())
c64Port1Name.setMaxAccess(_D)
if mibBuilder.loadTexts:c64Port1Name.setStatus(_B)
_C64Port2Name_Type=DisplayString
_C64Port2Name_Object=MibTableColumn
c64Port2Name=_C64Port2Name_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,8),_C64Port2Name_Type())
c64Port2Name.setMaxAccess(_D)
if mibBuilder.loadTexts:c64Port2Name.setStatus(_B)
class _C64PortConfigPrefIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryPort',1),('secondaryPort',2)))
_C64PortConfigPrefIndex_Type.__name__=_C
_C64PortConfigPrefIndex_Object=MibTableColumn
c64PortConfigPrefIndex=_C64PortConfigPrefIndex_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,9),_C64PortConfigPrefIndex_Type())
c64PortConfigPrefIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:c64PortConfigPrefIndex.setStatus(_B)
class _C64PortSwitchOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_C64PortSwitchOver_Type.__name__=_C
_C64PortSwitchOver_Object=MibTableColumn
c64PortSwitchOver=_C64PortSwitchOver_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,10),_C64PortSwitchOver_Type())
c64PortSwitchOver.setMaxAccess(_F)
if mibBuilder.loadTexts:c64PortSwitchOver.setStatus(_B)
_C64PortConfigStatus_Type=RowStatus
_C64PortConfigStatus_Object=MibTableColumn
c64PortConfigStatus=_C64PortConfigStatus_Object((1,3,6,1,4,1,9,10,27,1,1,6,1,11),_C64PortConfigStatus_Type())
c64PortConfigStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:c64PortConfigStatus.setStatus(_B)
_C64SonetAPSConfigTable_Object=MibTable
c64SonetAPSConfigTable=_C64SonetAPSConfigTable_Object((1,3,6,1,4,1,9,10,27,1,1,7))
if mibBuilder.loadTexts:c64SonetAPSConfigTable.setStatus(_B)
_C64SonetAPSConfigEntry_Object=MibTableRow
c64SonetAPSConfigEntry=_C64SonetAPSConfigEntry_Object((1,3,6,1,4,1,9,10,27,1,1,7,1))
c64SonetAPSConfigEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:c64SonetAPSConfigEntry.setStatus(_B)
class _C64SonetAPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('linear',1),('yCable',2),('disable',3)))
_C64SonetAPSMode_Type.__name__=_C
_C64SonetAPSMode_Object=MibTableColumn
c64SonetAPSMode=_C64SonetAPSMode_Object((1,3,6,1,4,1,9,10,27,1,1,7,1,1),_C64SonetAPSMode_Type())
c64SonetAPSMode.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SonetAPSMode.setStatus(_B)
class _C64SonetAPSBERThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150000))
_C64SonetAPSBERThreshold_Type.__name__=_C
_C64SonetAPSBERThreshold_Object=MibTableColumn
c64SonetAPSBERThreshold=_C64SonetAPSBERThreshold_Object((1,3,6,1,4,1,9,10,27,1,1,7,1,2),_C64SonetAPSBERThreshold_Type())
c64SonetAPSBERThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SonetAPSBERThreshold.setStatus(_B)
class _C64SonetAPSSwitchCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lockOut',1),('forceWorking',2),('forceProtect',3),('manualWorking',4),('manualProtect',5),('clear',6)))
_C64SonetAPSSwitchCmd_Type.__name__=_C
_C64SonetAPSSwitchCmd_Object=MibTableColumn
c64SonetAPSSwitchCmd=_C64SonetAPSSwitchCmd_Object((1,3,6,1,4,1,9,10,27,1,1,7,1,3),_C64SonetAPSSwitchCmd_Type())
c64SonetAPSSwitchCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SonetAPSSwitchCmd.setStatus(_B)
class _C64SonetAPSSFBERThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_C64SonetAPSSFBERThreshold_Type.__name__=_C
_C64SonetAPSSFBERThreshold_Object=MibTableColumn
c64SonetAPSSFBERThreshold=_C64SonetAPSSFBERThreshold_Object((1,3,6,1,4,1,9,10,27,1,1,7,1,4),_C64SonetAPSSFBERThreshold_Type())
c64SonetAPSSFBERThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:c64SonetAPSSFBERThreshold.setStatus(_B)
_C64SonetAPSStatsTable_Object=MibTable
c64SonetAPSStatsTable=_C64SonetAPSStatsTable_Object((1,3,6,1,4,1,9,10,27,1,1,8))
if mibBuilder.loadTexts:c64SonetAPSStatsTable.setStatus(_B)
_C64SonetAPSStatsEntry_Object=MibTableRow
c64SonetAPSStatsEntry=_C64SonetAPSStatsEntry_Object((1,3,6,1,4,1,9,10,27,1,1,8,1))
c64SonetAPSStatsEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:c64SonetAPSStatsEntry.setStatus(_B)
class _C64SonetAPSWorkSectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64SonetAPSWorkSectionStatus_Type.__name__=_C
_C64SonetAPSWorkSectionStatus_Object=MibTableColumn
c64SonetAPSWorkSectionStatus=_C64SonetAPSWorkSectionStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,1),_C64SonetAPSWorkSectionStatus_Type())
c64SonetAPSWorkSectionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkSectionStatus.setStatus(_B)
class _C64SonetAPSWorkLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64SonetAPSWorkLineStatus_Type.__name__=_C
_C64SonetAPSWorkLineStatus_Object=MibTableColumn
c64SonetAPSWorkLineStatus=_C64SonetAPSWorkLineStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,2),_C64SonetAPSWorkLineStatus_Type())
c64SonetAPSWorkLineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkLineStatus.setStatus(_B)
class _C64SonetAPSWorkPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64SonetAPSWorkPathStatus_Type.__name__=_C
_C64SonetAPSWorkPathStatus_Object=MibTableColumn
c64SonetAPSWorkPathStatus=_C64SonetAPSWorkPathStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,3),_C64SonetAPSWorkPathStatus_Type())
c64SonetAPSWorkPathStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkPathStatus.setStatus(_B)
_C64SonetAPSWorkSectionBIPE_Type=Counter32
_C64SonetAPSWorkSectionBIPE_Object=MibTableColumn
c64SonetAPSWorkSectionBIPE=_C64SonetAPSWorkSectionBIPE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,4),_C64SonetAPSWorkSectionBIPE_Type())
c64SonetAPSWorkSectionBIPE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkSectionBIPE.setStatus(_B)
_C64SonetAPSWorkLineBIPE_Type=Counter32
_C64SonetAPSWorkLineBIPE_Object=MibTableColumn
c64SonetAPSWorkLineBIPE=_C64SonetAPSWorkLineBIPE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,5),_C64SonetAPSWorkLineBIPE_Type())
c64SonetAPSWorkLineBIPE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkLineBIPE.setStatus(_B)
_C64SonetAPSWorkLineFEBE_Type=Counter32
_C64SonetAPSWorkLineFEBE_Object=MibTableColumn
c64SonetAPSWorkLineFEBE=_C64SonetAPSWorkLineFEBE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,6),_C64SonetAPSWorkLineFEBE_Type())
c64SonetAPSWorkLineFEBE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkLineFEBE.setStatus(_B)
_C64SonetAPSWorkPathBIPE_Type=Counter32
_C64SonetAPSWorkPathBIPE_Object=MibTableColumn
c64SonetAPSWorkPathBIPE=_C64SonetAPSWorkPathBIPE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,7),_C64SonetAPSWorkPathBIPE_Type())
c64SonetAPSWorkPathBIPE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkPathBIPE.setStatus(_B)
_C64SonetAPSWorkPathFEBE_Type=Counter32
_C64SonetAPSWorkPathFEBE_Object=MibTableColumn
c64SonetAPSWorkPathFEBE=_C64SonetAPSWorkPathFEBE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,8),_C64SonetAPSWorkPathFEBE_Type())
c64SonetAPSWorkPathFEBE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkPathFEBE.setStatus(_B)
_C64SonetAPSWorkPortStatus_Type=APSEventStatus
_C64SonetAPSWorkPortStatus_Object=MibTableColumn
c64SonetAPSWorkPortStatus=_C64SonetAPSWorkPortStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,9),_C64SonetAPSWorkPortStatus_Type())
c64SonetAPSWorkPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSWorkPortStatus.setStatus(_B)
class _C64SonetAPSProtectSectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64SonetAPSProtectSectionStatus_Type.__name__=_C
_C64SonetAPSProtectSectionStatus_Object=MibTableColumn
c64SonetAPSProtectSectionStatus=_C64SonetAPSProtectSectionStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,10),_C64SonetAPSProtectSectionStatus_Type())
c64SonetAPSProtectSectionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectSectionStatus.setStatus(_B)
class _C64SonetAPSProtectLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64SonetAPSProtectLineStatus_Type.__name__=_C
_C64SonetAPSProtectLineStatus_Object=MibTableColumn
c64SonetAPSProtectLineStatus=_C64SonetAPSProtectLineStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,11),_C64SonetAPSProtectLineStatus_Type())
c64SonetAPSProtectLineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectLineStatus.setStatus(_B)
class _C64SonetAPSProtectPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64SonetAPSProtectPathStatus_Type.__name__=_C
_C64SonetAPSProtectPathStatus_Object=MibTableColumn
c64SonetAPSProtectPathStatus=_C64SonetAPSProtectPathStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,12),_C64SonetAPSProtectPathStatus_Type())
c64SonetAPSProtectPathStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectPathStatus.setStatus(_B)
_C64SonetAPSProtectSectionBIPE_Type=Counter32
_C64SonetAPSProtectSectionBIPE_Object=MibTableColumn
c64SonetAPSProtectSectionBIPE=_C64SonetAPSProtectSectionBIPE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,13),_C64SonetAPSProtectSectionBIPE_Type())
c64SonetAPSProtectSectionBIPE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectSectionBIPE.setStatus(_B)
_C64SonetAPSProtectLineBIPE_Type=Counter32
_C64SonetAPSProtectLineBIPE_Object=MibTableColumn
c64SonetAPSProtectLineBIPE=_C64SonetAPSProtectLineBIPE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,14),_C64SonetAPSProtectLineBIPE_Type())
c64SonetAPSProtectLineBIPE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectLineBIPE.setStatus(_B)
_C64SonetAPSProtectLineFEBE_Type=Counter32
_C64SonetAPSProtectLineFEBE_Object=MibTableColumn
c64SonetAPSProtectLineFEBE=_C64SonetAPSProtectLineFEBE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,15),_C64SonetAPSProtectLineFEBE_Type())
c64SonetAPSProtectLineFEBE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectLineFEBE.setStatus(_B)
_C64SonetAPSProtectPathBIPE_Type=Counter32
_C64SonetAPSProtectPathBIPE_Object=MibTableColumn
c64SonetAPSProtectPathBIPE=_C64SonetAPSProtectPathBIPE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,16),_C64SonetAPSProtectPathBIPE_Type())
c64SonetAPSProtectPathBIPE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectPathBIPE.setStatus(_B)
_C64SonetAPSProtectPathFEBE_Type=Counter32
_C64SonetAPSProtectPathFEBE_Object=MibTableColumn
c64SonetAPSProtectPathFEBE=_C64SonetAPSProtectPathFEBE_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,17),_C64SonetAPSProtectPathFEBE_Type())
c64SonetAPSProtectPathFEBE.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectPathFEBE.setStatus(_B)
_C64SonetAPSProtectPortStatus_Type=APSEventStatus
_C64SonetAPSProtectPortStatus_Object=MibTableColumn
c64SonetAPSProtectPortStatus=_C64SonetAPSProtectPortStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,18),_C64SonetAPSProtectPortStatus_Type())
c64SonetAPSProtectPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSProtectPortStatus.setStatus(_B)
_C64SonetAPSChannelStatus_Type=APSEventStatus
_C64SonetAPSChannelStatus_Object=MibTableColumn
c64SonetAPSChannelStatus=_C64SonetAPSChannelStatus_Object((1,3,6,1,4,1,9,10,27,1,1,8,1,19),_C64SonetAPSChannelStatus_Type())
c64SonetAPSChannelStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64SonetAPSChannelStatus.setStatus(_B)
_C64ChassisGroup_ObjectIdentity=ObjectIdentity
c64ChassisGroup=_C64ChassisGroup_ObjectIdentity((1,3,6,1,4,1,9,10,27,1,2))
_C64TelcoAlarmMgmt_ObjectIdentity=ObjectIdentity
c64TelcoAlarmMgmt=_C64TelcoAlarmMgmt_ObjectIdentity((1,3,6,1,4,1,9,10,27,1,2,1))
class _C64ChassisFacilityAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_C64ChassisFacilityAlarmStatus_Type.__name__=_C
_C64ChassisFacilityAlarmStatus_Object=MibScalar
c64ChassisFacilityAlarmStatus=_C64ChassisFacilityAlarmStatus_Object((1,3,6,1,4,1,9,10,27,1,2,1,1),_C64ChassisFacilityAlarmStatus_Type())
c64ChassisFacilityAlarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64ChassisFacilityAlarmStatus.setStatus(_B)
class _C64ChassisClearAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('done',0),('all',1),('minor',2),('major',3),('critical',4)))
_C64ChassisClearAlarms_Type.__name__=_C
_C64ChassisClearAlarms_Object=MibScalar
c64ChassisClearAlarms=_C64ChassisClearAlarms_Object((1,3,6,1,4,1,9,10,27,1,2,1,2),_C64ChassisClearAlarms_Type())
c64ChassisClearAlarms.setMaxAccess(_G)
if mibBuilder.loadTexts:c64ChassisClearAlarms.setStatus(_B)
class _C64ChassisTempIntakeMinorThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,57))
_C64ChassisTempIntakeMinorThreshold_Type.__name__=_C
_C64ChassisTempIntakeMinorThreshold_Object=MibScalar
c64ChassisTempIntakeMinorThreshold=_C64ChassisTempIntakeMinorThreshold_Object((1,3,6,1,4,1,9,10,27,1,2,1,3),_C64ChassisTempIntakeMinorThreshold_Type())
c64ChassisTempIntakeMinorThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:c64ChassisTempIntakeMinorThreshold.setStatus(_B)
class _C64ChassisTempIntakeMajorThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,57))
_C64ChassisTempIntakeMajorThreshold_Type.__name__=_C
_C64ChassisTempIntakeMajorThreshold_Object=MibScalar
c64ChassisTempIntakeMajorThreshold=_C64ChassisTempIntakeMajorThreshold_Object((1,3,6,1,4,1,9,10,27,1,2,1,4),_C64ChassisTempIntakeMajorThreshold_Type())
c64ChassisTempIntakeMajorThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:c64ChassisTempIntakeMajorThreshold.setStatus(_B)
class _C64ChassisTempCoreMinorThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,60))
_C64ChassisTempCoreMinorThreshold_Type.__name__=_C
_C64ChassisTempCoreMinorThreshold_Object=MibScalar
c64ChassisTempCoreMinorThreshold=_C64ChassisTempCoreMinorThreshold_Object((1,3,6,1,4,1,9,10,27,1,2,1,5),_C64ChassisTempCoreMinorThreshold_Type())
c64ChassisTempCoreMinorThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:c64ChassisTempCoreMinorThreshold.setStatus(_B)
class _C64ChassisTempCoreMajorThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,60))
_C64ChassisTempCoreMajorThreshold_Type.__name__=_C
_C64ChassisTempCoreMajorThreshold_Object=MibScalar
c64ChassisTempCoreMajorThreshold=_C64ChassisTempCoreMajorThreshold_Object((1,3,6,1,4,1,9,10,27,1,2,1,6),_C64ChassisTempCoreMajorThreshold_Type())
c64ChassisTempCoreMajorThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:c64ChassisTempCoreMajorThreshold.setStatus(_B)
class _C64ChassisTempThresholdAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_C64ChassisTempThresholdAdmin_Type.__name__=_C
_C64ChassisTempThresholdAdmin_Object=MibScalar
c64ChassisTempThresholdAdmin=_C64ChassisTempThresholdAdmin_Object((1,3,6,1,4,1,9,10,27,1,2,1,7),_C64ChassisTempThresholdAdmin_Type())
c64ChassisTempThresholdAdmin.setMaxAccess(_G)
if mibBuilder.loadTexts:c64ChassisTempThresholdAdmin.setStatus(_B)
_C64ChassisAlarmTable_Object=MibTable
c64ChassisAlarmTable=_C64ChassisAlarmTable_Object((1,3,6,1,4,1,9,10,27,1,2,2))
if mibBuilder.loadTexts:c64ChassisAlarmTable.setStatus(_B)
_C64ChassisAlarmEntry_Object=MibTableRow
c64ChassisAlarmEntry=_C64ChassisAlarmEntry_Object((1,3,6,1,4,1,9,10,27,1,2,2,1))
c64ChassisAlarmEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:c64ChassisAlarmEntry.setStatus(_B)
class _C64ChassisAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_C64ChassisAlarmIndex_Type.__name__=_C
_C64ChassisAlarmIndex_Object=MibTableColumn
c64ChassisAlarmIndex=_C64ChassisAlarmIndex_Object((1,3,6,1,4,1,9,10,27,1,2,2,1,1),_C64ChassisAlarmIndex_Type())
c64ChassisAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:c64ChassisAlarmIndex.setStatus(_B)
_C64ChassisAlarmSource_Type=DisplayString
_C64ChassisAlarmSource_Object=MibTableColumn
c64ChassisAlarmSource=_C64ChassisAlarmSource_Object((1,3,6,1,4,1,9,10,27,1,2,2,1,2),_C64ChassisAlarmSource_Type())
c64ChassisAlarmSource.setMaxAccess(_D)
if mibBuilder.loadTexts:c64ChassisAlarmSource.setStatus(_B)
class _C64ChassisAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('coreTemp',1),('inletTemp',2),('totalFanFail',3),('partialFanFail',4),('fanMissing',5),('pem0Fail',6),('pem1Fail',7),('sonetLineFail',8),('cardOIRAlarm',9),('cardFail',10),('cardPartialFail',11),('linkDownAlarm',12),('networkClockAlarm',13),('nrpSARFail',14),('nrpPAMDataError',15),('diskAlarm',16),('imageAlarm',17),('nrpBootUpAlarm',18),('nrpSwitchoverAlarm',19),('nrpSecondaryFailureAlarm',20),('nrpSecondaryRemovedAlarm',21),('nrpMismatchAlarm',22)))
_C64ChassisAlarmType_Type.__name__=_C
_C64ChassisAlarmType_Object=MibTableColumn
c64ChassisAlarmType=_C64ChassisAlarmType_Object((1,3,6,1,4,1,9,10,27,1,2,2,1,3),_C64ChassisAlarmType_Type())
c64ChassisAlarmType.setMaxAccess(_D)
if mibBuilder.loadTexts:c64ChassisAlarmType.setStatus(_B)
class _C64ChassisAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minor',1),('major',2),('critical',3)))
_C64ChassisAlarmSeverity_Type.__name__=_C
_C64ChassisAlarmSeverity_Object=MibTableColumn
c64ChassisAlarmSeverity=_C64ChassisAlarmSeverity_Object((1,3,6,1,4,1,9,10,27,1,2,2,1,4),_C64ChassisAlarmSeverity_Type())
c64ChassisAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:c64ChassisAlarmSeverity.setStatus(_B)
class _C64ChassisAlarmACOStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('cutoff',2)))
_C64ChassisAlarmACOStatus_Type.__name__=_C
_C64ChassisAlarmACOStatus_Object=MibTableColumn
c64ChassisAlarmACOStatus=_C64ChassisAlarmACOStatus_Object((1,3,6,1,4,1,9,10,27,1,2,2,1,5),_C64ChassisAlarmACOStatus_Type())
c64ChassisAlarmACOStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:c64ChassisAlarmACOStatus.setStatus(_B)
_Cisco6400ChassisMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cisco6400ChassisMIBNotificationPrefix=_Cisco6400ChassisMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,27,2))
_Cisco6400ChassisMIBNotification_ObjectIdentity=ObjectIdentity
cisco6400ChassisMIBNotification=_Cisco6400ChassisMIBNotification_ObjectIdentity((1,3,6,1,4,1,9,10,27,2,0))
_Cisco6400ChassisMIBConformance_ObjectIdentity=ObjectIdentity
cisco6400ChassisMIBConformance=_Cisco6400ChassisMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,27,3))
_Cisco6400ChassisMIBCompliances_ObjectIdentity=ObjectIdentity
cisco6400ChassisMIBCompliances=_Cisco6400ChassisMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,27,3,1))
_Cisco6400ChassisMIBGroups_ObjectIdentity=ObjectIdentity
cisco6400ChassisMIBGroups=_Cisco6400ChassisMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,27,3,2))
cisco6400RedundantGroup=ObjectGroup((1,3,6,1,4,1,9,10,27,3,2,1))
cisco6400RedundantGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_AE),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_AF),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:cisco6400RedundantGroup.setStatus(_J)
cisco6400ChassisMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,27,3,2,2))
cisco6400ChassisMIBGroup.setObjects(*((_A,_A0),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_N),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:cisco6400ChassisMIBGroup.setStatus(_B)
cisco6400RedundantGroup2=ObjectGroup((1,3,6,1,4,1,9,10,27,3,2,3))
cisco6400RedundantGroup2.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:cisco6400RedundantGroup2.setStatus(_B)
cisco6400ChassisFailureNotification=NotificationType((1,3,6,1,4,1,9,10,27,2,0,1))
cisco6400ChassisFailureNotification.setObjects((_A,_A0))
if mibBuilder.loadTexts:cisco6400ChassisFailureNotification.setStatus(_B)
cisco6400ChassisMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,27,3,1,1))
cisco6400ChassisMIBCompliance.setObjects(*((_A,_AQ),(_A,_A1)))
if mibBuilder.loadTexts:cisco6400ChassisMIBCompliance.setStatus(_J)
cisco6400ChassisMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,27,3,1,2))
cisco6400ChassisMIBCompliance2.setObjects(*((_A,_AR),(_A,_A1)))
if mibBuilder.loadTexts:cisco6400ChassisMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'APSEventStatus':APSEventStatus,'cisco6400ChassisMIB':cisco6400ChassisMIB,'cisco6400ChassisMIBObjects':cisco6400ChassisMIBObjects,'c64RedundantGroup':c64RedundantGroup,_O:c64MainCPUConfigAutoSync,_P:c64MainCPUSwitchOver,'c64SlotConfigTable':c64SlotConfigTable,'c64SlotConfigEntry':c64SlotConfigEntry,_A2:c64SlotConfigModule1Index,_A3:c64SlotConfigModule2Index,_Q:c64Slot1Name,_R:c64Slot2Name,_AE:c64SlotConfigPrefIndex,_S:c64SlotSwitchOver,_T:c64SlotConfigStatus,'c64SubSlotConfigTable':c64SubSlotConfigTable,'c64SubSlotConfigEntry':c64SubSlotConfigEntry,_M:c64SubSlotRedundantIndex,_A4:c64SubSlotConfigModule1Index,_A5:c64SubSlotConfigSubModule1Index,_A6:c64SubSlotConfigModule2Index,_A7:c64SubSlotConfigSubModule2Index,_U:c64SubSlot1Name,_V:c64SubSlot2Name,_AF:c64SubSlotConfigPrefIndex,_W:c64SubSlotSwitchOver,_X:c64SubSlotConfigStatus,'c64PortConfigTable':c64PortConfigTable,'c64PortConfigEntry':c64PortConfigEntry,_A8:c64PortConfigModule1Index,_A9:c64PortConfigSubModule1Index,_AA:c64PortConfigPort1Index,_AB:c64PortConfigModule2Index,_AC:c64PortConfigSubModule2Index,_AD:c64PortConfigPort2Index,_Y:c64Port1Name,_Z:c64Port2Name,_a:c64PortConfigPrefIndex,_b:c64PortSwitchOver,_c:c64PortConfigStatus,'c64SonetAPSConfigTable':c64SonetAPSConfigTable,'c64SonetAPSConfigEntry':c64SonetAPSConfigEntry,_d:c64SonetAPSMode,_e:c64SonetAPSBERThreshold,_f:c64SonetAPSSwitchCmd,_g:c64SonetAPSSFBERThreshold,'c64SonetAPSStatsTable':c64SonetAPSStatsTable,'c64SonetAPSStatsEntry':c64SonetAPSStatsEntry,_h:c64SonetAPSWorkSectionStatus,_i:c64SonetAPSWorkLineStatus,_j:c64SonetAPSWorkPathStatus,_k:c64SonetAPSWorkSectionBIPE,_l:c64SonetAPSWorkLineBIPE,_m:c64SonetAPSWorkLineFEBE,_n:c64SonetAPSWorkPathBIPE,_o:c64SonetAPSWorkPathFEBE,_p:c64SonetAPSWorkPortStatus,_q:c64SonetAPSProtectSectionStatus,_r:c64SonetAPSProtectLineStatus,_s:c64SonetAPSProtectPathStatus,_t:c64SonetAPSProtectSectionBIPE,_u:c64SonetAPSProtectLineBIPE,_v:c64SonetAPSProtectLineFEBE,_w:c64SonetAPSProtectPathBIPE,_x:c64SonetAPSProtectPathFEBE,_y:c64SonetAPSProtectPortStatus,_z:c64SonetAPSChannelStatus,'c64ChassisGroup':c64ChassisGroup,'c64TelcoAlarmMgmt':c64TelcoAlarmMgmt,_A0:c64ChassisFacilityAlarmStatus,_AG:c64ChassisClearAlarms,_AH:c64ChassisTempIntakeMinorThreshold,_AI:c64ChassisTempIntakeMajorThreshold,_AJ:c64ChassisTempCoreMinorThreshold,_AK:c64ChassisTempCoreMajorThreshold,_AL:c64ChassisTempThresholdAdmin,'c64ChassisAlarmTable':c64ChassisAlarmTable,'c64ChassisAlarmEntry':c64ChassisAlarmEntry,_N:c64ChassisAlarmIndex,_AM:c64ChassisAlarmSource,_AN:c64ChassisAlarmType,_AO:c64ChassisAlarmSeverity,_AP:c64ChassisAlarmACOStatus,'cisco6400ChassisMIBNotificationPrefix':cisco6400ChassisMIBNotificationPrefix,'cisco6400ChassisMIBNotification':cisco6400ChassisMIBNotification,'cisco6400ChassisFailureNotification':cisco6400ChassisFailureNotification,'cisco6400ChassisMIBConformance':cisco6400ChassisMIBConformance,'cisco6400ChassisMIBCompliances':cisco6400ChassisMIBCompliances,'cisco6400ChassisMIBCompliance':cisco6400ChassisMIBCompliance,'cisco6400ChassisMIBCompliance2':cisco6400ChassisMIBCompliance2,'cisco6400ChassisMIBGroups':cisco6400ChassisMIBGroups,_AQ:cisco6400RedundantGroup,_A1:cisco6400ChassisMIBGroup,_AR:cisco6400RedundantGroup2})