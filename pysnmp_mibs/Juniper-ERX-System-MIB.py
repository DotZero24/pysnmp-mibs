_B9='juniERXSysGeneralGroup3'
_B8='juniERXSysNotifyGroup2'
_B7='juniERXSysGroup'
_B6='juniERXSysTempProtectionStatusChange'
_B5='juniERXSysGeneralTrapEnable'
_B4='juniERXSysTempProtectionHoldOffTime'
_B3='juniERXSysTimingStatus'
_B2='juniERXSysTimingSourceLine'
_B1='juniERXSysTimingSourceIfIndex'
_B0='juniERXSysTimingSourceType'
_A_='juniERXSysTimingDisableAutoUpgrade'
_Az='juniERXSysOperTimingSource'
_Ay='juniERXSysAdminTimingSource'
_Ax='juniERXSysSlotIoaAssemblyRev'
_Aw='juniERXSysSlotIoaAssemblyPartNumber'
_Av='juniERXSysSlotIoaSerialNumber'
_Au='juniERXSysSlotAssemblyRev'
_At='juniERXSysSlotAssemblyPartNumber'
_As='juniERXSysSlotSerialNumber'
_Ar='juniERXSysSubsystemIndex'
_Aq='juniERXSysTempIndex'
_Ap='juniERXSysPowerIndex'
_Ao='juniERXSysPortIndex'
_An='noBootBackup'
_Am='noOperation'
_Al='JuniTimingSourceLineType'
_Ak='juniERXSysTimingSelectorIndex'
_Aj='factoryDefaults'
_Ai='immediate'
_Ah='juniERXSysNotifyGroup3'
_Ag='juniERXSysTemperatureGroup2'
_Af='juniERXSysGeneralGroup2'
_Ae='juniERXSysGeneralGroup'
_Ad='juniERXSysAbatedMemUtil'
_Ac='juniERXSysHighMemUtil'
_Ab='juniERXSysTempProtectionHoldOffTimeRemaining'
_Aa='juniERXSysTempProtectionStatus'
_AZ='juniERXSysMemUtilTrapEnable'
_AY='juniERXSysSubsystemBootBackupReleaseFile'
_AX='juniERXSysSubsystemBootReleaseFile'
_AW='juniERXSysSubsystemControl'
_AV='juniERXSysSubsystemName'
_AU='juniERXSysPowerDescr'
_AT='juniERXSysPortIfIndex'
_AS='juniERXSysPortType'
_AR='juniERXSysPortDescr'
_AQ='juniERXSysSlotBootBackupReleaseFile'
_AP='juniERXSysSlotBootReleaseFile'
_AO='juniERXSysSlotRedundancyRevertTime'
_AN='juniERXSysSlotRevertControl'
_AM='juniERXSysSlotRedundancyGroupId'
_AL='juniERXSysSlotRedundancyLockout'
_AK='juniERXSysSlotLastChange'
_AJ='juniERXSysSlotPortCount'
_AI='juniERXSysSlotIoaPresent'
_AH='juniERXSysSlotMemUtilPct'
_AG='juniERXSysSlotCpuUtilPct'
_AF='juniERXSysSlotControl'
_AE='juniERXSysSlotExpectedCardType'
_AD='juniERXSysSlotRev'
_AC='juniERXSysSlotCount'
_AB='juniERXSysNvsUtilPct'
_AA='juniERXSysNvsCapacity'
_A9='juniERXSysNvsStatus'
_A8='juniERXSysFabricRev'
_A7='juniERXSysFabricSpeed'
_A6='failed'
_A5='Unsigned32'
_A4='juniERXSysTemperatureGroup'
_A3='juniERXSysNotifyGroup'
_A2='juniERXSysTempStatusChange'
_A1='juniERXSysTempFanStatusChange'
_A0='juniERXSysPowerStatusChange'
_z='juniERXSysSlotOperStatusChange'
_y='juniERXSysTempValue'
_x='juniERXSysTempDescr'
_w='juniERXSysPowerStatus'
_v='juniERXSysSlotAssociatedSlot'
_u='juniERXSysSlotSpareServer'
_t='juniERXSysSlotDisableReason'
_s='juniERXSysSlotOperStatus'
_r='juniERXSysSlotAdminStatus'
_q='juniERXSysSlotCurrentCardType'
_p='juniERXSysSlotDescr'
_o='juniERXSysSlotIndex'
_n='seconds'
_m='TruthValue'
_l='juniERXSysTimingGroup'
_k='juniERXSysAbatedMemUtilThreshold'
_j='juniERXSysHighMemUtilThreshold'
_i='juniERXSysMemCapacity'
_h='juniERXSysMemUtilPct'
_g='juniERXSysTempStatus'
_f='juniERXSysTempFanStatus'
_e='juniERXSysBootBackupConfigFile'
_d='juniERXSysBootBackupReleaseFile'
_c='juniERXSysBootConfigFile'
_b='juniERXSysBootReleaseFile'
_a='juniERXSysBootAutoRevertTimeTolerance'
_Z='juniERXSysBootAutoRevertCountTolerance'
_Y='juniERXSysBootAutoRevertControl'
_X='juniERXSysBootForceBackupControl'
_W='juniERXSysBootBackupConfigControl'
_V='juniERXSysBootConfigControl'
_U='juniERXSysRevertTimeOfDay'
_T='juniERXSysRevertControl'
_S='juniERXSysSwBuildDate'
_R='juniERXSysSwVersion'
_Q='juniERXSysChassisRev'
_P='unknown'
_O='juniERXSysSubsystemGroup'
_N='juniERXSysPowerGroup'
_M='juniERXSysPortGroup'
_L='juniERXSysSlotGroup'
_K='juniERXSysNvsGroup'
_J='juniERXSysFabricGroup'
_I='percent'
_H='not-accessible'
_G='obsolete'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='deprecated'
_A='Juniper-ERX-System-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC','JuniEnable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A5,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','TextualConvention',_m)
juniERXSysMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,17))
if mibBuilder.loadTexts:juniERXSysMIB.setRevisions(('2003-11-24 21:01','2003-11-24 14:26','2003-11-18 22:06','2002-10-14 17:40','2002-04-12 20:57','2001-05-21 19:27','2001-05-15 18:27','2000-04-25 18:44','2000-01-20 00:00','1999-02-10 00:00'))
class JuniTimingSelector(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
class JuniTimingSourceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('timingInterfaceIfIndex',1),('timingInternal',2),('timingLine',3)))
class JuniTimingSourceLineType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('timingSourceLineUndefined',0),('timingSourceLineE1PortA',1),('timingSourceLineE1PortB',2),('timingSourceLineT1PortA',3),('timingSourceLineT1PortB',4)))
class JuniSysCardType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*((_P,0),('srp',1),('ct3',2),('oc3',3),('ut3Atm',4),('ut3Frame',5),('ue3Atm',6),('ue3Frame',7),('ce1',8),('ct1',9),('dpfe',10),('oc12Pos',11),('oc12Atm',12),('oc3Pos',13),('oc3Atm',14),('ge',15),('fe8',16),('oc3oc12Pos',17),('oc3oc12Atm',18),('coc3oc12',19),('coc3',20),('coc12',21),('oc12Server',22),('hssi',23),('geFe',24),('ct3P12',25),('v35',26),('ut3f12',27),('ue3f12',28),('coc12F3',29),('coc3F3',30),('cocxF3',31),('vts',32),('oc48',33),('ut3Atm4',34),('hybrid',35),('oc3AtmGe',36),('oc3AtmPos',37),('ge2',38)))
_JuniERXSysTrap_ObjectIdentity=ObjectIdentity
juniERXSysTrap=_JuniERXSysTrap_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,0))
_JuniERXSysObjects_ObjectIdentity=ObjectIdentity
juniERXSysObjects=_JuniERXSysObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1))
_JuniERXSysGeneral_ObjectIdentity=ObjectIdentity
juniERXSysGeneral=_JuniERXSysGeneral_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,1))
class _JuniERXSysChassisRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysChassisRev_Type.__name__=_D
_JuniERXSysChassisRev_Object=MibScalar
juniERXSysChassisRev=_JuniERXSysChassisRev_Object((1,3,6,1,4,1,4874,2,2,17,1,1,1),_JuniERXSysChassisRev_Type())
juniERXSysChassisRev.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysChassisRev.setStatus(_B)
_JuniERXSysSwVersion_Type=DisplayString
_JuniERXSysSwVersion_Object=MibScalar
juniERXSysSwVersion=_JuniERXSysSwVersion_Object((1,3,6,1,4,1,4874,2,2,17,1,1,2),_JuniERXSysSwVersion_Type())
juniERXSysSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSwVersion.setStatus(_B)
_JuniERXSysSwBuildDate_Type=DisplayString
_JuniERXSysSwBuildDate_Object=MibScalar
juniERXSysSwBuildDate=_JuniERXSysSwBuildDate_Object((1,3,6,1,4,1,4874,2,2,17,1,1,3),_JuniERXSysSwBuildDate_Type())
juniERXSysSwBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSwBuildDate.setStatus(_B)
class _JuniERXSysRevertControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),(_Ai,1),('timeOfDay',2)))
_JuniERXSysRevertControl_Type.__name__=_D
_JuniERXSysRevertControl_Object=MibScalar
juniERXSysRevertControl=_JuniERXSysRevertControl_Object((1,3,6,1,4,1,4874,2,2,17,1,1,4),_JuniERXSysRevertControl_Type())
juniERXSysRevertControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysRevertControl.setStatus(_B)
class _JuniERXSysRevertTimeOfDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
_JuniERXSysRevertTimeOfDay_Type.__name__=_D
_JuniERXSysRevertTimeOfDay_Object=MibScalar
juniERXSysRevertTimeOfDay=_JuniERXSysRevertTimeOfDay_Object((1,3,6,1,4,1,4874,2,2,17,1,1,5),_JuniERXSysRevertTimeOfDay_Type())
juniERXSysRevertTimeOfDay.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysRevertTimeOfDay.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysRevertTimeOfDay.setUnits(_n)
class _JuniERXSysBootConfigControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('file',0),('fileOnce',1),(_Aj,2),('runningConfiguration',3)))
_JuniERXSysBootConfigControl_Type.__name__=_D
_JuniERXSysBootConfigControl_Object=MibScalar
juniERXSysBootConfigControl=_JuniERXSysBootConfigControl_Object((1,3,6,1,4,1,4874,2,2,17,1,1,6),_JuniERXSysBootConfigControl_Type())
juniERXSysBootConfigControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootConfigControl.setStatus(_B)
class _JuniERXSysBootBackupConfigControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('file',0),(_Aj,1),('none',2)))
_JuniERXSysBootBackupConfigControl_Type.__name__=_D
_JuniERXSysBootBackupConfigControl_Object=MibScalar
juniERXSysBootBackupConfigControl=_JuniERXSysBootBackupConfigControl_Object((1,3,6,1,4,1,4874,2,2,17,1,1,7),_JuniERXSysBootBackupConfigControl_Type())
juniERXSysBootBackupConfigControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootBackupConfigControl.setStatus(_B)
class _JuniERXSysBootForceBackupControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_JuniERXSysBootForceBackupControl_Type.__name__=_D
_JuniERXSysBootForceBackupControl_Object=MibScalar
juniERXSysBootForceBackupControl=_JuniERXSysBootForceBackupControl_Object((1,3,6,1,4,1,4874,2,2,17,1,1,8),_JuniERXSysBootForceBackupControl_Type())
juniERXSysBootForceBackupControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootForceBackupControl.setStatus(_B)
class _JuniERXSysBootAutoRevertControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),('never',1),('set',2)))
_JuniERXSysBootAutoRevertControl_Type.__name__=_D
_JuniERXSysBootAutoRevertControl_Object=MibScalar
juniERXSysBootAutoRevertControl=_JuniERXSysBootAutoRevertControl_Object((1,3,6,1,4,1,4874,2,2,17,1,1,9),_JuniERXSysBootAutoRevertControl_Type())
juniERXSysBootAutoRevertControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootAutoRevertControl.setStatus(_B)
class _JuniERXSysBootAutoRevertCountTolerance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_JuniERXSysBootAutoRevertCountTolerance_Type.__name__=_A5
_JuniERXSysBootAutoRevertCountTolerance_Object=MibScalar
juniERXSysBootAutoRevertCountTolerance=_JuniERXSysBootAutoRevertCountTolerance_Object((1,3,6,1,4,1,4874,2,2,17,1,1,10),_JuniERXSysBootAutoRevertCountTolerance_Type())
juniERXSysBootAutoRevertCountTolerance.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootAutoRevertCountTolerance.setStatus(_B)
class _JuniERXSysBootAutoRevertTimeTolerance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_JuniERXSysBootAutoRevertTimeTolerance_Type.__name__=_A5
_JuniERXSysBootAutoRevertTimeTolerance_Object=MibScalar
juniERXSysBootAutoRevertTimeTolerance=_JuniERXSysBootAutoRevertTimeTolerance_Object((1,3,6,1,4,1,4874,2,2,17,1,1,11),_JuniERXSysBootAutoRevertTimeTolerance_Type())
juniERXSysBootAutoRevertTimeTolerance.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootAutoRevertTimeTolerance.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysBootAutoRevertTimeTolerance.setUnits(_n)
class _JuniERXSysBootReleaseFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysBootReleaseFile_Type.__name__=_F
_JuniERXSysBootReleaseFile_Object=MibScalar
juniERXSysBootReleaseFile=_JuniERXSysBootReleaseFile_Object((1,3,6,1,4,1,4874,2,2,17,1,1,12),_JuniERXSysBootReleaseFile_Type())
juniERXSysBootReleaseFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootReleaseFile.setStatus(_B)
class _JuniERXSysBootConfigFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysBootConfigFile_Type.__name__=_F
_JuniERXSysBootConfigFile_Object=MibScalar
juniERXSysBootConfigFile=_JuniERXSysBootConfigFile_Object((1,3,6,1,4,1,4874,2,2,17,1,1,13),_JuniERXSysBootConfigFile_Type())
juniERXSysBootConfigFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootConfigFile.setStatus(_B)
class _JuniERXSysBootBackupReleaseFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysBootBackupReleaseFile_Type.__name__=_F
_JuniERXSysBootBackupReleaseFile_Object=MibScalar
juniERXSysBootBackupReleaseFile=_JuniERXSysBootBackupReleaseFile_Object((1,3,6,1,4,1,4874,2,2,17,1,1,14),_JuniERXSysBootBackupReleaseFile_Type())
juniERXSysBootBackupReleaseFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootBackupReleaseFile.setStatus(_B)
class _JuniERXSysBootBackupConfigFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysBootBackupConfigFile_Type.__name__=_F
_JuniERXSysBootBackupConfigFile_Object=MibScalar
juniERXSysBootBackupConfigFile=_JuniERXSysBootBackupConfigFile_Object((1,3,6,1,4,1,4874,2,2,17,1,1,15),_JuniERXSysBootBackupConfigFile_Type())
juniERXSysBootBackupConfigFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysBootBackupConfigFile.setStatus(_B)
_JuniERXSysAdminTimingSource_Type=JuniTimingSelector
_JuniERXSysAdminTimingSource_Object=MibScalar
juniERXSysAdminTimingSource=_JuniERXSysAdminTimingSource_Object((1,3,6,1,4,1,4874,2,2,17,1,1,16),_JuniERXSysAdminTimingSource_Type())
juniERXSysAdminTimingSource.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysAdminTimingSource.setStatus(_B)
_JuniERXSysOperTimingSource_Type=JuniTimingSelector
_JuniERXSysOperTimingSource_Object=MibScalar
juniERXSysOperTimingSource=_JuniERXSysOperTimingSource_Object((1,3,6,1,4,1,4874,2,2,17,1,1,17),_JuniERXSysOperTimingSource_Type())
juniERXSysOperTimingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysOperTimingSource.setStatus(_B)
class _JuniERXSysTimingDisableAutoUpgrade_Type(TruthValue):defaultValue=2
_JuniERXSysTimingDisableAutoUpgrade_Type.__name__=_m
_JuniERXSysTimingDisableAutoUpgrade_Object=MibScalar
juniERXSysTimingDisableAutoUpgrade=_JuniERXSysTimingDisableAutoUpgrade_Object((1,3,6,1,4,1,4874,2,2,17,1,1,18),_JuniERXSysTimingDisableAutoUpgrade_Type())
juniERXSysTimingDisableAutoUpgrade.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysTimingDisableAutoUpgrade.setStatus(_B)
_JuniERXSysTimingSelectorTable_Object=MibTable
juniERXSysTimingSelectorTable=_JuniERXSysTimingSelectorTable_Object((1,3,6,1,4,1,4874,2,2,17,1,1,19))
if mibBuilder.loadTexts:juniERXSysTimingSelectorTable.setStatus(_B)
_JuniERXSysTimingSelectorEntry_Object=MibTableRow
juniERXSysTimingSelectorEntry=_JuniERXSysTimingSelectorEntry_Object((1,3,6,1,4,1,4874,2,2,17,1,1,19,1))
juniERXSysTimingSelectorEntry.setIndexNames((0,_A,_Ak))
if mibBuilder.loadTexts:juniERXSysTimingSelectorEntry.setStatus(_B)
_JuniERXSysTimingSelectorIndex_Type=JuniTimingSelector
_JuniERXSysTimingSelectorIndex_Object=MibTableColumn
juniERXSysTimingSelectorIndex=_JuniERXSysTimingSelectorIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,1,19,1,1),_JuniERXSysTimingSelectorIndex_Type())
juniERXSysTimingSelectorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniERXSysTimingSelectorIndex.setStatus(_B)
_JuniERXSysTimingSourceType_Type=JuniTimingSourceType
_JuniERXSysTimingSourceType_Object=MibTableColumn
juniERXSysTimingSourceType=_JuniERXSysTimingSourceType_Object((1,3,6,1,4,1,4874,2,2,17,1,1,19,1,2),_JuniERXSysTimingSourceType_Type())
juniERXSysTimingSourceType.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysTimingSourceType.setStatus(_B)
_JuniERXSysTimingSourceIfIndex_Type=InterfaceIndexOrZero
_JuniERXSysTimingSourceIfIndex_Object=MibTableColumn
juniERXSysTimingSourceIfIndex=_JuniERXSysTimingSourceIfIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,1,19,1,3),_JuniERXSysTimingSourceIfIndex_Type())
juniERXSysTimingSourceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysTimingSourceIfIndex.setStatus(_B)
class _JuniERXSysTimingSourceLine_Type(JuniTimingSourceLineType):defaultValue=0
_JuniERXSysTimingSourceLine_Type.__name__=_Al
_JuniERXSysTimingSourceLine_Object=MibTableColumn
juniERXSysTimingSourceLine=_JuniERXSysTimingSourceLine_Object((1,3,6,1,4,1,4874,2,2,17,1,1,19,1,4),_JuniERXSysTimingSourceLine_Type())
juniERXSysTimingSourceLine.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysTimingSourceLine.setStatus(_B)
class _JuniERXSysTimingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('timingStatusOk',1),('timingStatusError',2),('timingStatusUnknown',3)))
_JuniERXSysTimingStatus_Type.__name__=_D
_JuniERXSysTimingStatus_Object=MibTableColumn
juniERXSysTimingStatus=_JuniERXSysTimingStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,1,19,1,5),_JuniERXSysTimingStatus_Type())
juniERXSysTimingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTimingStatus.setStatus(_B)
class _JuniERXSysMemUtilPct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_JuniERXSysMemUtilPct_Type.__name__=_D
_JuniERXSysMemUtilPct_Object=MibScalar
juniERXSysMemUtilPct=_JuniERXSysMemUtilPct_Object((1,3,6,1,4,1,4874,2,2,17,1,1,20),_JuniERXSysMemUtilPct_Type())
juniERXSysMemUtilPct.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysMemUtilPct.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysMemUtilPct.setUnits(_I)
_JuniERXSysMemCapacity_Type=Integer32
_JuniERXSysMemCapacity_Object=MibScalar
juniERXSysMemCapacity=_JuniERXSysMemCapacity_Object((1,3,6,1,4,1,4874,2,2,17,1,1,21),_JuniERXSysMemCapacity_Type())
juniERXSysMemCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysMemCapacity.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysMemCapacity.setUnits('bytes')
class _JuniERXSysHighMemUtilThreshold_Type(Integer32):defaultValue=85;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_JuniERXSysHighMemUtilThreshold_Type.__name__=_D
_JuniERXSysHighMemUtilThreshold_Object=MibScalar
juniERXSysHighMemUtilThreshold=_JuniERXSysHighMemUtilThreshold_Object((1,3,6,1,4,1,4874,2,2,17,1,1,22),_JuniERXSysHighMemUtilThreshold_Type())
juniERXSysHighMemUtilThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysHighMemUtilThreshold.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysHighMemUtilThreshold.setUnits(_I)
class _JuniERXSysAbatedMemUtilThreshold_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_JuniERXSysAbatedMemUtilThreshold_Type.__name__=_D
_JuniERXSysAbatedMemUtilThreshold_Object=MibScalar
juniERXSysAbatedMemUtilThreshold=_JuniERXSysAbatedMemUtilThreshold_Object((1,3,6,1,4,1,4874,2,2,17,1,1,23),_JuniERXSysAbatedMemUtilThreshold_Type())
juniERXSysAbatedMemUtilThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysAbatedMemUtilThreshold.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysAbatedMemUtilThreshold.setUnits(_I)
class _JuniERXSysMemUtilTrapEnable_Type(TruthValue):defaultValue=2
_JuniERXSysMemUtilTrapEnable_Type.__name__=_m
_JuniERXSysMemUtilTrapEnable_Object=MibScalar
juniERXSysMemUtilTrapEnable=_JuniERXSysMemUtilTrapEnable_Object((1,3,6,1,4,1,4874,2,2,17,1,1,24),_JuniERXSysMemUtilTrapEnable_Type())
juniERXSysMemUtilTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysMemUtilTrapEnable.setStatus(_B)
class _JuniERXSysGeneralTrapEnable_Type(TruthValue):defaultValue=2
_JuniERXSysGeneralTrapEnable_Type.__name__=_m
_JuniERXSysGeneralTrapEnable_Object=MibScalar
juniERXSysGeneralTrapEnable=_JuniERXSysGeneralTrapEnable_Object((1,3,6,1,4,1,4874,2,2,17,1,1,25),_JuniERXSysGeneralTrapEnable_Type())
juniERXSysGeneralTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysGeneralTrapEnable.setStatus(_B)
_JuniERXSysFabric_ObjectIdentity=ObjectIdentity
juniERXSysFabric=_JuniERXSysFabric_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,2))
_JuniERXSysFabricSpeed_Type=Integer32
_JuniERXSysFabricSpeed_Object=MibScalar
juniERXSysFabricSpeed=_JuniERXSysFabricSpeed_Object((1,3,6,1,4,1,4874,2,2,17,1,2,1),_JuniERXSysFabricSpeed_Type())
juniERXSysFabricSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysFabricSpeed.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysFabricSpeed.setUnits('gigabits per second')
class _JuniERXSysFabricRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysFabricRev_Type.__name__=_D
_JuniERXSysFabricRev_Object=MibScalar
juniERXSysFabricRev=_JuniERXSysFabricRev_Object((1,3,6,1,4,1,4874,2,2,17,1,2,2),_JuniERXSysFabricRev_Type())
juniERXSysFabricRev.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysFabricRev.setStatus(_B)
_JuniERXSysNvs_ObjectIdentity=ObjectIdentity
juniERXSysNvs=_JuniERXSysNvs_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,3))
class _JuniERXSysNvsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('notPresent',0),('writeProtected',1),('volumeError',2),('nearCapacity',3),('ok',4),('nearConfigCapacity',5)))
_JuniERXSysNvsStatus_Type.__name__=_D
_JuniERXSysNvsStatus_Object=MibScalar
juniERXSysNvsStatus=_JuniERXSysNvsStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,3,1),_JuniERXSysNvsStatus_Type())
juniERXSysNvsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysNvsStatus.setStatus(_B)
_JuniERXSysNvsCapacity_Type=Integer32
_JuniERXSysNvsCapacity_Object=MibScalar
juniERXSysNvsCapacity=_JuniERXSysNvsCapacity_Object((1,3,6,1,4,1,4874,2,2,17,1,3,2),_JuniERXSysNvsCapacity_Type())
juniERXSysNvsCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysNvsCapacity.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysNvsCapacity.setUnits('megabytes')
class _JuniERXSysNvsUtilPct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_JuniERXSysNvsUtilPct_Type.__name__=_D
_JuniERXSysNvsUtilPct_Object=MibScalar
juniERXSysNvsUtilPct=_JuniERXSysNvsUtilPct_Object((1,3,6,1,4,1,4874,2,2,17,1,3,3),_JuniERXSysNvsUtilPct_Type())
juniERXSysNvsUtilPct.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysNvsUtilPct.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysNvsUtilPct.setUnits(_I)
_JuniERXSysSlot_ObjectIdentity=ObjectIdentity
juniERXSysSlot=_JuniERXSysSlot_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,4))
_JuniERXSysSlotCount_Type=Integer32
_JuniERXSysSlotCount_Object=MibScalar
juniERXSysSlotCount=_JuniERXSysSlotCount_Object((1,3,6,1,4,1,4874,2,2,17,1,4,1),_JuniERXSysSlotCount_Type())
juniERXSysSlotCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotCount.setStatus(_B)
_JuniERXSysSlotTable_Object=MibTable
juniERXSysSlotTable=_JuniERXSysSlotTable_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2))
if mibBuilder.loadTexts:juniERXSysSlotTable.setStatus(_B)
_JuniERXSysSlotEntry_Object=MibTableRow
juniERXSysSlotEntry=_JuniERXSysSlotEntry_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1))
juniERXSysSlotEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:juniERXSysSlotEntry.setStatus(_B)
class _JuniERXSysSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysSlotIndex_Type.__name__=_D
_JuniERXSysSlotIndex_Object=MibTableColumn
juniERXSysSlotIndex=_JuniERXSysSlotIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,1),_JuniERXSysSlotIndex_Type())
juniERXSysSlotIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniERXSysSlotIndex.setStatus(_B)
class _JuniERXSysSlotDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JuniERXSysSlotDescr_Type.__name__=_F
_JuniERXSysSlotDescr_Object=MibTableColumn
juniERXSysSlotDescr=_JuniERXSysSlotDescr_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,2),_JuniERXSysSlotDescr_Type())
juniERXSysSlotDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotDescr.setStatus(_B)
_JuniERXSysSlotCurrentCardType_Type=JuniSysCardType
_JuniERXSysSlotCurrentCardType_Object=MibTableColumn
juniERXSysSlotCurrentCardType=_JuniERXSysSlotCurrentCardType_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,3),_JuniERXSysSlotCurrentCardType_Type())
juniERXSysSlotCurrentCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotCurrentCardType.setStatus(_B)
class _JuniERXSysSlotRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysSlotRev_Type.__name__=_D
_JuniERXSysSlotRev_Object=MibTableColumn
juniERXSysSlotRev=_JuniERXSysSlotRev_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,4),_JuniERXSysSlotRev_Type())
juniERXSysSlotRev.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotRev.setStatus(_B)
_JuniERXSysSlotAdminStatus_Type=JuniEnable
_JuniERXSysSlotAdminStatus_Object=MibTableColumn
juniERXSysSlotAdminStatus=_JuniERXSysSlotAdminStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,5),_JuniERXSysSlotAdminStatus_Type())
juniERXSysSlotAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSlotAdminStatus.setStatus(_B)
class _JuniERXSysSlotOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_P,0),('empty',1),('disabled',2),(_A6,3),('booting',4),('initializing',5),('online',6),('standby',7),('inactive',8)))
_JuniERXSysSlotOperStatus_Type.__name__=_D
_JuniERXSysSlotOperStatus_Object=MibTableColumn
juniERXSysSlotOperStatus=_JuniERXSysSlotOperStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,6),_JuniERXSysSlotOperStatus_Type())
juniERXSysSlotOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotOperStatus.setStatus(_B)
class _JuniERXSysSlotDisableReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('none',0),(_P,1),('assessing',2),('admin',3),('cardMismatch',4),('fabricLimit',5),('imageError',6)))
_JuniERXSysSlotDisableReason_Type.__name__=_D
_JuniERXSysSlotDisableReason_Object=MibTableColumn
juniERXSysSlotDisableReason=_JuniERXSysSlotDisableReason_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,7),_JuniERXSysSlotDisableReason_Type())
juniERXSysSlotDisableReason.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotDisableReason.setStatus(_B)
_JuniERXSysSlotExpectedCardType_Type=JuniSysCardType
_JuniERXSysSlotExpectedCardType_Object=MibTableColumn
juniERXSysSlotExpectedCardType=_JuniERXSysSlotExpectedCardType_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,8),_JuniERXSysSlotExpectedCardType_Type())
juniERXSysSlotExpectedCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotExpectedCardType.setStatus(_B)
class _JuniERXSysSlotControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_Am,0),('flush',1),('reset',2),('forceFailover',3),('noBoot',4),(_An,5)))
_JuniERXSysSlotControl_Type.__name__=_D
_JuniERXSysSlotControl_Object=MibTableColumn
juniERXSysSlotControl=_JuniERXSysSlotControl_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,9),_JuniERXSysSlotControl_Type())
juniERXSysSlotControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSlotControl.setStatus(_B)
class _JuniERXSysSlotCpuUtilPct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_JuniERXSysSlotCpuUtilPct_Type.__name__=_D
_JuniERXSysSlotCpuUtilPct_Object=MibTableColumn
juniERXSysSlotCpuUtilPct=_JuniERXSysSlotCpuUtilPct_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,10),_JuniERXSysSlotCpuUtilPct_Type())
juniERXSysSlotCpuUtilPct.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotCpuUtilPct.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysSlotCpuUtilPct.setUnits(_I)
class _JuniERXSysSlotMemUtilPct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_JuniERXSysSlotMemUtilPct_Type.__name__=_D
_JuniERXSysSlotMemUtilPct_Object=MibTableColumn
juniERXSysSlotMemUtilPct=_JuniERXSysSlotMemUtilPct_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,11),_JuniERXSysSlotMemUtilPct_Type())
juniERXSysSlotMemUtilPct.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotMemUtilPct.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysSlotMemUtilPct.setUnits(_I)
_JuniERXSysSlotIoaPresent_Type=TruthValue
_JuniERXSysSlotIoaPresent_Object=MibTableColumn
juniERXSysSlotIoaPresent=_JuniERXSysSlotIoaPresent_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,12),_JuniERXSysSlotIoaPresent_Type())
juniERXSysSlotIoaPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotIoaPresent.setStatus(_B)
_JuniERXSysSlotPortCount_Type=Integer32
_JuniERXSysSlotPortCount_Object=MibTableColumn
juniERXSysSlotPortCount=_JuniERXSysSlotPortCount_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,13),_JuniERXSysSlotPortCount_Type())
juniERXSysSlotPortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotPortCount.setStatus(_B)
_JuniERXSysSlotLastChange_Type=TimeTicks
_JuniERXSysSlotLastChange_Object=MibTableColumn
juniERXSysSlotLastChange=_JuniERXSysSlotLastChange_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,14),_JuniERXSysSlotLastChange_Type())
juniERXSysSlotLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotLastChange.setStatus(_B)
_JuniERXSysSlotRedundancyLockout_Type=JuniEnable
_JuniERXSysSlotRedundancyLockout_Object=MibTableColumn
juniERXSysSlotRedundancyLockout=_JuniERXSysSlotRedundancyLockout_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,15),_JuniERXSysSlotRedundancyLockout_Type())
juniERXSysSlotRedundancyLockout.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSlotRedundancyLockout.setStatus(_B)
_JuniERXSysSlotRedundancyGroupId_Type=Unsigned32
_JuniERXSysSlotRedundancyGroupId_Object=MibTableColumn
juniERXSysSlotRedundancyGroupId=_JuniERXSysSlotRedundancyGroupId_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,16),_JuniERXSysSlotRedundancyGroupId_Type())
juniERXSysSlotRedundancyGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotRedundancyGroupId.setStatus(_B)
_JuniERXSysSlotSpareServer_Type=TruthValue
_JuniERXSysSlotSpareServer_Object=MibTableColumn
juniERXSysSlotSpareServer=_JuniERXSysSlotSpareServer_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,17),_JuniERXSysSlotSpareServer_Type())
juniERXSysSlotSpareServer.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotSpareServer.setStatus(_B)
_JuniERXSysSlotAssociatedSlot_Type=Integer32
_JuniERXSysSlotAssociatedSlot_Object=MibTableColumn
juniERXSysSlotAssociatedSlot=_JuniERXSysSlotAssociatedSlot_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,18),_JuniERXSysSlotAssociatedSlot_Type())
juniERXSysSlotAssociatedSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotAssociatedSlot.setStatus(_B)
class _JuniERXSysSlotRevertControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),(_Ai,1),('timeAndDate',2)))
_JuniERXSysSlotRevertControl_Type.__name__=_D
_JuniERXSysSlotRevertControl_Object=MibTableColumn
juniERXSysSlotRevertControl=_JuniERXSysSlotRevertControl_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,19),_JuniERXSysSlotRevertControl_Type())
juniERXSysSlotRevertControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSlotRevertControl.setStatus(_B)
_JuniERXSysSlotRedundancyRevertTime_Type=DateAndTime
_JuniERXSysSlotRedundancyRevertTime_Object=MibTableColumn
juniERXSysSlotRedundancyRevertTime=_JuniERXSysSlotRedundancyRevertTime_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,20),_JuniERXSysSlotRedundancyRevertTime_Type())
juniERXSysSlotRedundancyRevertTime.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSlotRedundancyRevertTime.setStatus(_B)
class _JuniERXSysSlotBootReleaseFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysSlotBootReleaseFile_Type.__name__=_F
_JuniERXSysSlotBootReleaseFile_Object=MibTableColumn
juniERXSysSlotBootReleaseFile=_JuniERXSysSlotBootReleaseFile_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,21),_JuniERXSysSlotBootReleaseFile_Type())
juniERXSysSlotBootReleaseFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSlotBootReleaseFile.setStatus(_B)
class _JuniERXSysSlotBootBackupReleaseFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysSlotBootBackupReleaseFile_Type.__name__=_F
_JuniERXSysSlotBootBackupReleaseFile_Object=MibTableColumn
juniERXSysSlotBootBackupReleaseFile=_JuniERXSysSlotBootBackupReleaseFile_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,22),_JuniERXSysSlotBootBackupReleaseFile_Type())
juniERXSysSlotBootBackupReleaseFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSlotBootBackupReleaseFile.setStatus(_B)
class _JuniERXSysSlotSerialNumber_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniERXSysSlotSerialNumber_Type.__name__=_F
_JuniERXSysSlotSerialNumber_Object=MibTableColumn
juniERXSysSlotSerialNumber=_JuniERXSysSlotSerialNumber_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,23),_JuniERXSysSlotSerialNumber_Type())
juniERXSysSlotSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotSerialNumber.setStatus(_B)
class _JuniERXSysSlotAssemblyPartNumber_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniERXSysSlotAssemblyPartNumber_Type.__name__=_F
_JuniERXSysSlotAssemblyPartNumber_Object=MibTableColumn
juniERXSysSlotAssemblyPartNumber=_JuniERXSysSlotAssemblyPartNumber_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,24),_JuniERXSysSlotAssemblyPartNumber_Type())
juniERXSysSlotAssemblyPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotAssemblyPartNumber.setStatus(_B)
class _JuniERXSysSlotAssemblyRev_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_JuniERXSysSlotAssemblyRev_Type.__name__=_F
_JuniERXSysSlotAssemblyRev_Object=MibTableColumn
juniERXSysSlotAssemblyRev=_JuniERXSysSlotAssemblyRev_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,25),_JuniERXSysSlotAssemblyRev_Type())
juniERXSysSlotAssemblyRev.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotAssemblyRev.setStatus(_B)
class _JuniERXSysSlotIoaSerialNumber_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniERXSysSlotIoaSerialNumber_Type.__name__=_F
_JuniERXSysSlotIoaSerialNumber_Object=MibTableColumn
juniERXSysSlotIoaSerialNumber=_JuniERXSysSlotIoaSerialNumber_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,26),_JuniERXSysSlotIoaSerialNumber_Type())
juniERXSysSlotIoaSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotIoaSerialNumber.setStatus(_B)
class _JuniERXSysSlotIoaAssemblyPartNumber_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniERXSysSlotIoaAssemblyPartNumber_Type.__name__=_F
_JuniERXSysSlotIoaAssemblyPartNumber_Object=MibTableColumn
juniERXSysSlotIoaAssemblyPartNumber=_JuniERXSysSlotIoaAssemblyPartNumber_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,27),_JuniERXSysSlotIoaAssemblyPartNumber_Type())
juniERXSysSlotIoaAssemblyPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotIoaAssemblyPartNumber.setStatus(_B)
class _JuniERXSysSlotIoaAssemblyRev_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_JuniERXSysSlotIoaAssemblyRev_Type.__name__=_F
_JuniERXSysSlotIoaAssemblyRev_Object=MibTableColumn
juniERXSysSlotIoaAssemblyRev=_JuniERXSysSlotIoaAssemblyRev_Object((1,3,6,1,4,1,4874,2,2,17,1,4,2,1,28),_JuniERXSysSlotIoaAssemblyRev_Type())
juniERXSysSlotIoaAssemblyRev.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSlotIoaAssemblyRev.setStatus(_B)
_JuniERXSysPort_ObjectIdentity=ObjectIdentity
juniERXSysPort=_JuniERXSysPort_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,5))
_JuniERXSysPortTable_Object=MibTable
juniERXSysPortTable=_JuniERXSysPortTable_Object((1,3,6,1,4,1,4874,2,2,17,1,5,1))
if mibBuilder.loadTexts:juniERXSysPortTable.setStatus(_B)
_JuniERXSysPortEntry_Object=MibTableRow
juniERXSysPortEntry=_JuniERXSysPortEntry_Object((1,3,6,1,4,1,4874,2,2,17,1,5,1,1))
juniERXSysPortEntry.setIndexNames((0,_A,_o),(0,_A,_Ao))
if mibBuilder.loadTexts:juniERXSysPortEntry.setStatus(_B)
class _JuniERXSysPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysPortIndex_Type.__name__=_D
_JuniERXSysPortIndex_Object=MibTableColumn
juniERXSysPortIndex=_JuniERXSysPortIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,5,1,1,1),_JuniERXSysPortIndex_Type())
juniERXSysPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniERXSysPortIndex.setStatus(_B)
class _JuniERXSysPortDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JuniERXSysPortDescr_Type.__name__=_F
_JuniERXSysPortDescr_Object=MibTableColumn
juniERXSysPortDescr=_JuniERXSysPortDescr_Object((1,3,6,1,4,1,4874,2,2,17,1,5,1,1,2),_JuniERXSysPortDescr_Type())
juniERXSysPortDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysPortDescr.setStatus(_B)
class _JuniERXSysPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_P,0),('eth',1),('ct3',2),('oc3c',3),('ut3Atm',4),('ut3Frame',5),('ue3Atm',6),('ue3Frame',7),('ce1',8),('ct1',9),('oc12cPos',10),('oc12cAtm',11),('oc3cPos',12),('oc3cAtm',13),('coc3',14),('coc12',15),('server',16),('hssi',17),('v35',18),('oc48cPos',19)))
_JuniERXSysPortType_Type.__name__=_D
_JuniERXSysPortType_Object=MibTableColumn
juniERXSysPortType=_JuniERXSysPortType_Object((1,3,6,1,4,1,4874,2,2,17,1,5,1,1,3),_JuniERXSysPortType_Type())
juniERXSysPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysPortType.setStatus(_B)
_JuniERXSysPortIfIndex_Type=InterfaceIndexOrZero
_JuniERXSysPortIfIndex_Object=MibTableColumn
juniERXSysPortIfIndex=_JuniERXSysPortIfIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,5,1,1,4),_JuniERXSysPortIfIndex_Type())
juniERXSysPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysPortIfIndex.setStatus(_B)
_JuniERXSysPower_ObjectIdentity=ObjectIdentity
juniERXSysPower=_JuniERXSysPower_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,6))
_JuniERXSysPowerTable_Object=MibTable
juniERXSysPowerTable=_JuniERXSysPowerTable_Object((1,3,6,1,4,1,4874,2,2,17,1,6,1))
if mibBuilder.loadTexts:juniERXSysPowerTable.setStatus(_B)
_JuniERXSysPowerEntry_Object=MibTableRow
juniERXSysPowerEntry=_JuniERXSysPowerEntry_Object((1,3,6,1,4,1,4874,2,2,17,1,6,1,1))
juniERXSysPowerEntry.setIndexNames((0,_A,_Ap))
if mibBuilder.loadTexts:juniERXSysPowerEntry.setStatus(_B)
class _JuniERXSysPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysPowerIndex_Type.__name__=_D
_JuniERXSysPowerIndex_Object=MibTableColumn
juniERXSysPowerIndex=_JuniERXSysPowerIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,6,1,1,1),_JuniERXSysPowerIndex_Type())
juniERXSysPowerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniERXSysPowerIndex.setStatus(_B)
class _JuniERXSysPowerDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JuniERXSysPowerDescr_Type.__name__=_F
_JuniERXSysPowerDescr_Object=MibTableColumn
juniERXSysPowerDescr=_JuniERXSysPowerDescr_Object((1,3,6,1,4,1,4874,2,2,17,1,6,1,1,2),_JuniERXSysPowerDescr_Type())
juniERXSysPowerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysPowerDescr.setStatus(_B)
class _JuniERXSysPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_JuniERXSysPowerStatus_Type.__name__=_D
_JuniERXSysPowerStatus_Object=MibTableColumn
juniERXSysPowerStatus=_JuniERXSysPowerStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,6,1,1,3),_JuniERXSysPowerStatus_Type())
juniERXSysPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysPowerStatus.setStatus(_B)
_JuniERXSysTemperature_ObjectIdentity=ObjectIdentity
juniERXSysTemperature=_JuniERXSysTemperature_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,7))
class _JuniERXSysTempFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_A6,0),('ok',1),('warning',2)))
_JuniERXSysTempFanStatus_Type.__name__=_D
_JuniERXSysTempFanStatus_Object=MibScalar
juniERXSysTempFanStatus=_JuniERXSysTempFanStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,7,1),_JuniERXSysTempFanStatus_Type())
juniERXSysTempFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTempFanStatus.setStatus(_B)
_JuniERXSysTempTable_Object=MibTable
juniERXSysTempTable=_JuniERXSysTempTable_Object((1,3,6,1,4,1,4874,2,2,17,1,7,2))
if mibBuilder.loadTexts:juniERXSysTempTable.setStatus(_B)
_JuniERXSysTempEntry_Object=MibTableRow
juniERXSysTempEntry=_JuniERXSysTempEntry_Object((1,3,6,1,4,1,4874,2,2,17,1,7,2,1))
juniERXSysTempEntry.setIndexNames((0,_A,_o),(0,_A,_Aq))
if mibBuilder.loadTexts:juniERXSysTempEntry.setStatus(_B)
class _JuniERXSysTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysTempIndex_Type.__name__=_D
_JuniERXSysTempIndex_Object=MibTableColumn
juniERXSysTempIndex=_JuniERXSysTempIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,7,2,1,1),_JuniERXSysTempIndex_Type())
juniERXSysTempIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniERXSysTempIndex.setStatus(_B)
class _JuniERXSysTempDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JuniERXSysTempDescr_Type.__name__=_F
_JuniERXSysTempDescr_Object=MibTableColumn
juniERXSysTempDescr=_JuniERXSysTempDescr_Object((1,3,6,1,4,1,4874,2,2,17,1,7,2,1,2),_JuniERXSysTempDescr_Type())
juniERXSysTempDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTempDescr.setStatus(_B)
class _JuniERXSysTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_P,0),(_A6,1),('tooLow',2),('nominal',3),('tooHigh',4),('tooLowWarning',5),('tooHighWarning',6)))
_JuniERXSysTempStatus_Type.__name__=_D
_JuniERXSysTempStatus_Object=MibTableColumn
juniERXSysTempStatus=_JuniERXSysTempStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,7,2,1,3),_JuniERXSysTempStatus_Type())
juniERXSysTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTempStatus.setStatus(_B)
_JuniERXSysTempValue_Type=Integer32
_JuniERXSysTempValue_Object=MibTableColumn
juniERXSysTempValue=_JuniERXSysTempValue_Object((1,3,6,1,4,1,4874,2,2,17,1,7,2,1,4),_JuniERXSysTempValue_Type())
juniERXSysTempValue.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTempValue.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysTempValue.setUnits('degrees Celsius')
class _JuniERXSysTempProtectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('monitoring',1),('inHoldOff',2),('activatedHoldOffExpired',3),('activatedTempTooHigh',4)))
_JuniERXSysTempProtectionStatus_Type.__name__=_D
_JuniERXSysTempProtectionStatus_Object=MibScalar
juniERXSysTempProtectionStatus=_JuniERXSysTempProtectionStatus_Object((1,3,6,1,4,1,4874,2,2,17,1,7,3),_JuniERXSysTempProtectionStatus_Type())
juniERXSysTempProtectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTempProtectionStatus.setStatus(_B)
class _JuniERXSysTempProtectionHoldOffTime_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1200))
_JuniERXSysTempProtectionHoldOffTime_Type.__name__=_D
_JuniERXSysTempProtectionHoldOffTime_Object=MibScalar
juniERXSysTempProtectionHoldOffTime=_JuniERXSysTempProtectionHoldOffTime_Object((1,3,6,1,4,1,4874,2,2,17,1,7,4),_JuniERXSysTempProtectionHoldOffTime_Type())
juniERXSysTempProtectionHoldOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTempProtectionHoldOffTime.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysTempProtectionHoldOffTime.setUnits(_n)
class _JuniERXSysTempProtectionHoldOffTimeRemaining_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1200))
_JuniERXSysTempProtectionHoldOffTimeRemaining_Type.__name__=_D
_JuniERXSysTempProtectionHoldOffTimeRemaining_Object=MibScalar
juniERXSysTempProtectionHoldOffTimeRemaining=_JuniERXSysTempProtectionHoldOffTimeRemaining_Object((1,3,6,1,4,1,4874,2,2,17,1,7,5),_JuniERXSysTempProtectionHoldOffTimeRemaining_Type())
juniERXSysTempProtectionHoldOffTimeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysTempProtectionHoldOffTimeRemaining.setStatus(_B)
if mibBuilder.loadTexts:juniERXSysTempProtectionHoldOffTimeRemaining.setUnits(_n)
_JuniERXSysSubsystem_ObjectIdentity=ObjectIdentity
juniERXSysSubsystem=_JuniERXSysSubsystem_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,1,8))
_JuniERXSysSubsystemTable_Object=MibTable
juniERXSysSubsystemTable=_JuniERXSysSubsystemTable_Object((1,3,6,1,4,1,4874,2,2,17,1,8,1))
if mibBuilder.loadTexts:juniERXSysSubsystemTable.setStatus(_B)
_JuniERXSysSubsystemEntry_Object=MibTableRow
juniERXSysSubsystemEntry=_JuniERXSysSubsystemEntry_Object((1,3,6,1,4,1,4874,2,2,17,1,8,1,1))
juniERXSysSubsystemEntry.setIndexNames((0,_A,_Ar))
if mibBuilder.loadTexts:juniERXSysSubsystemEntry.setStatus(_B)
class _JuniERXSysSubsystemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniERXSysSubsystemIndex_Type.__name__=_D
_JuniERXSysSubsystemIndex_Object=MibTableColumn
juniERXSysSubsystemIndex=_JuniERXSysSubsystemIndex_Object((1,3,6,1,4,1,4874,2,2,17,1,8,1,1,1),_JuniERXSysSubsystemIndex_Type())
juniERXSysSubsystemIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniERXSysSubsystemIndex.setStatus(_B)
class _JuniERXSysSubsystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysSubsystemName_Type.__name__=_F
_JuniERXSysSubsystemName_Object=MibTableColumn
juniERXSysSubsystemName=_JuniERXSysSubsystemName_Object((1,3,6,1,4,1,4874,2,2,17,1,8,1,1,2),_JuniERXSysSubsystemName_Type())
juniERXSysSubsystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniERXSysSubsystemName.setStatus(_B)
class _JuniERXSysSubsystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Am,0),('noBoot',1),(_An,2)))
_JuniERXSysSubsystemControl_Type.__name__=_D
_JuniERXSysSubsystemControl_Object=MibTableColumn
juniERXSysSubsystemControl=_JuniERXSysSubsystemControl_Object((1,3,6,1,4,1,4874,2,2,17,1,8,1,1,3),_JuniERXSysSubsystemControl_Type())
juniERXSysSubsystemControl.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSubsystemControl.setStatus(_B)
class _JuniERXSysSubsystemBootReleaseFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysSubsystemBootReleaseFile_Type.__name__=_F
_JuniERXSysSubsystemBootReleaseFile_Object=MibTableColumn
juniERXSysSubsystemBootReleaseFile=_JuniERXSysSubsystemBootReleaseFile_Object((1,3,6,1,4,1,4874,2,2,17,1,8,1,1,4),_JuniERXSysSubsystemBootReleaseFile_Type())
juniERXSysSubsystemBootReleaseFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSubsystemBootReleaseFile.setStatus(_B)
class _JuniERXSysSubsystemBootBackupReleaseFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JuniERXSysSubsystemBootBackupReleaseFile_Type.__name__=_F
_JuniERXSysSubsystemBootBackupReleaseFile_Object=MibTableColumn
juniERXSysSubsystemBootBackupReleaseFile=_JuniERXSysSubsystemBootBackupReleaseFile_Object((1,3,6,1,4,1,4874,2,2,17,1,8,1,1,5),_JuniERXSysSubsystemBootBackupReleaseFile_Type())
juniERXSysSubsystemBootBackupReleaseFile.setMaxAccess(_E)
if mibBuilder.loadTexts:juniERXSysSubsystemBootBackupReleaseFile.setStatus(_B)
_JuniERXSysConformance_ObjectIdentity=ObjectIdentity
juniERXSysConformance=_JuniERXSysConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,2))
_JuniERXSysCompliances_ObjectIdentity=ObjectIdentity
juniERXSysCompliances=_JuniERXSysCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,2,1))
_JuniERXSysGroups_ObjectIdentity=ObjectIdentity
juniERXSysGroups=_JuniERXSysGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,17,2,2))
juniERXSysGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,1))
juniERXSysGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_p),(_A,_q),(_A,_AD),(_A,_r),(_A,_s),(_A,_t),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_u),(_A,_v),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_w),(_A,_f),(_A,_x),(_A,_g),(_A,_y),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:juniERXSysGroup.setStatus(_G)
juniERXSysGeneralGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,3))
juniERXSysGeneralGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:juniERXSysGeneralGroup.setStatus(_G)
juniERXSysFabricGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,4))
juniERXSysFabricGroup.setObjects(*((_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:juniERXSysFabricGroup.setStatus(_B)
juniERXSysNvsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,5))
juniERXSysNvsGroup.setObjects(*((_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:juniERXSysNvsGroup.setStatus(_B)
juniERXSysSlotGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,6))
juniERXSysSlotGroup.setObjects(*((_A,_AC),(_A,_p),(_A,_q),(_A,_AD),(_A,_r),(_A,_s),(_A,_t),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_u),(_A,_v),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:juniERXSysSlotGroup.setStatus(_B)
juniERXSysPortGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,7))
juniERXSysPortGroup.setObjects(*((_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:juniERXSysPortGroup.setStatus(_B)
juniERXSysPowerGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,8))
juniERXSysPowerGroup.setObjects(*((_A,_AU),(_A,_w)))
if mibBuilder.loadTexts:juniERXSysPowerGroup.setStatus(_B)
juniERXSysTemperatureGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,9))
juniERXSysTemperatureGroup.setObjects(*((_A,_f),(_A,_x),(_A,_g),(_A,_y)))
if mibBuilder.loadTexts:juniERXSysTemperatureGroup.setStatus(_G)
juniERXSysSubsystemGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,10))
juniERXSysSubsystemGroup.setObjects(*((_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:juniERXSysSubsystemGroup.setStatus(_B)
juniERXSysTimingGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,11))
juniERXSysTimingGroup.setObjects(*((_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3)))
if mibBuilder.loadTexts:juniERXSysTimingGroup.setStatus(_B)
juniERXSysGeneralGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,12))
juniERXSysGeneralGroup2.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_AZ)))
if mibBuilder.loadTexts:juniERXSysGeneralGroup2.setStatus(_G)
juniERXSysTemperatureGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,14))
juniERXSysTemperatureGroup2.setObjects(*((_A,_f),(_A,_x),(_A,_g),(_A,_y),(_A,_Aa),(_A,_B4),(_A,_Ab)))
if mibBuilder.loadTexts:juniERXSysTemperatureGroup2.setStatus(_B)
juniERXSysGeneralGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,17,2,2,16))
juniERXSysGeneralGroup3.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_AZ),(_A,_B5)))
if mibBuilder.loadTexts:juniERXSysGeneralGroup3.setStatus(_B)
juniERXSysSlotOperStatusChange=NotificationType((1,3,6,1,4,1,4874,2,2,17,0,1))
juniERXSysSlotOperStatusChange.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_p)))
if mibBuilder.loadTexts:juniERXSysSlotOperStatusChange.setStatus(_B)
juniERXSysPowerStatusChange=NotificationType((1,3,6,1,4,1,4874,2,2,17,0,2))
juniERXSysPowerStatusChange.setObjects((_A,_w))
if mibBuilder.loadTexts:juniERXSysPowerStatusChange.setStatus(_B)
juniERXSysTempFanStatusChange=NotificationType((1,3,6,1,4,1,4874,2,2,17,0,3))
juniERXSysTempFanStatusChange.setObjects((_A,_f))
if mibBuilder.loadTexts:juniERXSysTempFanStatusChange.setStatus(_B)
juniERXSysTempStatusChange=NotificationType((1,3,6,1,4,1,4874,2,2,17,0,4))
juniERXSysTempStatusChange.setObjects((_A,_g))
if mibBuilder.loadTexts:juniERXSysTempStatusChange.setStatus(_B)
juniERXSysHighMemUtil=NotificationType((1,3,6,1,4,1,4874,2,2,17,0,5))
juniERXSysHighMemUtil.setObjects(*((_A,_i),(_A,_h),(_A,_k),(_A,_j)))
if mibBuilder.loadTexts:juniERXSysHighMemUtil.setStatus(_B)
juniERXSysAbatedMemUtil=NotificationType((1,3,6,1,4,1,4874,2,2,17,0,6))
juniERXSysAbatedMemUtil.setObjects(*((_A,_i),(_A,_h),(_A,_k),(_A,_j)))
if mibBuilder.loadTexts:juniERXSysAbatedMemUtil.setStatus(_B)
juniERXSysTempProtectionStatusChange=NotificationType((1,3,6,1,4,1,4874,2,2,17,0,7))
juniERXSysTempProtectionStatusChange.setObjects(*((_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:juniERXSysTempProtectionStatusChange.setStatus(_B)
juniERXSysNotifyGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,17,2,2,2))
juniERXSysNotifyGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:juniERXSysNotifyGroup.setStatus(_G)
juniERXSysNotifyGroup2=NotificationGroup((1,3,6,1,4,1,4874,2,2,17,2,2,13))
juniERXSysNotifyGroup2.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:juniERXSysNotifyGroup2.setStatus(_G)
juniERXSysNotifyGroup3=NotificationGroup((1,3,6,1,4,1,4874,2,2,17,2,2,15))
juniERXSysNotifyGroup3.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_Ac),(_A,_Ad),(_A,_B6)))
if mibBuilder.loadTexts:juniERXSysNotifyGroup3.setStatus(_B)
juniERXSysCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,17,2,1,1))
juniERXSysCompliance.setObjects(*((_A,_B7),(_A,_A3)))
if mibBuilder.loadTexts:juniERXSysCompliance.setStatus(_G)
juniERXSysCompliance1=ModuleCompliance((1,3,6,1,4,1,4874,2,2,17,2,1,2))
juniERXSysCompliance1.setObjects(*((_A,_Ae),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_A4),(_A,_O),(_A,_A3)))
if mibBuilder.loadTexts:juniERXSysCompliance1.setStatus(_G)
juniERXSysCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,17,2,1,3))
juniERXSysCompliance2.setObjects(*((_A,_Ae),(_A,_l),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_A4),(_A,_O),(_A,_A3)))
if mibBuilder.loadTexts:juniERXSysCompliance2.setStatus(_G)
juniERXSysCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,17,2,1,4))
juniERXSysCompliance3.setObjects(*((_A,_Af),(_A,_l),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_A4),(_A,_O),(_A,_B8)))
if mibBuilder.loadTexts:juniERXSysCompliance3.setStatus(_G)
juniERXSysCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,17,2,1,5))
juniERXSysCompliance4.setObjects(*((_A,_Af),(_A,_l),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Ag),(_A,_O),(_A,_Ah)))
if mibBuilder.loadTexts:juniERXSysCompliance4.setStatus(_G)
juniERXSysCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,17,2,1,6))
juniERXSysCompliance5.setObjects(*((_A,_B9),(_A,_l),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Ag),(_A,_O),(_A,_Ah)))
if mibBuilder.loadTexts:juniERXSysCompliance5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniTimingSelector':JuniTimingSelector,'JuniTimingSourceType':JuniTimingSourceType,_Al:JuniTimingSourceLineType,'JuniSysCardType':JuniSysCardType,'juniERXSysMIB':juniERXSysMIB,'juniERXSysTrap':juniERXSysTrap,_z:juniERXSysSlotOperStatusChange,_A0:juniERXSysPowerStatusChange,_A1:juniERXSysTempFanStatusChange,_A2:juniERXSysTempStatusChange,_Ac:juniERXSysHighMemUtil,_Ad:juniERXSysAbatedMemUtil,_B6:juniERXSysTempProtectionStatusChange,'juniERXSysObjects':juniERXSysObjects,'juniERXSysGeneral':juniERXSysGeneral,_Q:juniERXSysChassisRev,_R:juniERXSysSwVersion,_S:juniERXSysSwBuildDate,_T:juniERXSysRevertControl,_U:juniERXSysRevertTimeOfDay,_V:juniERXSysBootConfigControl,_W:juniERXSysBootBackupConfigControl,_X:juniERXSysBootForceBackupControl,_Y:juniERXSysBootAutoRevertControl,_Z:juniERXSysBootAutoRevertCountTolerance,_a:juniERXSysBootAutoRevertTimeTolerance,_b:juniERXSysBootReleaseFile,_c:juniERXSysBootConfigFile,_d:juniERXSysBootBackupReleaseFile,_e:juniERXSysBootBackupConfigFile,_Ay:juniERXSysAdminTimingSource,_Az:juniERXSysOperTimingSource,_A_:juniERXSysTimingDisableAutoUpgrade,'juniERXSysTimingSelectorTable':juniERXSysTimingSelectorTable,'juniERXSysTimingSelectorEntry':juniERXSysTimingSelectorEntry,_Ak:juniERXSysTimingSelectorIndex,_B0:juniERXSysTimingSourceType,_B1:juniERXSysTimingSourceIfIndex,_B2:juniERXSysTimingSourceLine,_B3:juniERXSysTimingStatus,_h:juniERXSysMemUtilPct,_i:juniERXSysMemCapacity,_j:juniERXSysHighMemUtilThreshold,_k:juniERXSysAbatedMemUtilThreshold,_AZ:juniERXSysMemUtilTrapEnable,_B5:juniERXSysGeneralTrapEnable,'juniERXSysFabric':juniERXSysFabric,_A7:juniERXSysFabricSpeed,_A8:juniERXSysFabricRev,'juniERXSysNvs':juniERXSysNvs,_A9:juniERXSysNvsStatus,_AA:juniERXSysNvsCapacity,_AB:juniERXSysNvsUtilPct,'juniERXSysSlot':juniERXSysSlot,_AC:juniERXSysSlotCount,'juniERXSysSlotTable':juniERXSysSlotTable,'juniERXSysSlotEntry':juniERXSysSlotEntry,_o:juniERXSysSlotIndex,_p:juniERXSysSlotDescr,_q:juniERXSysSlotCurrentCardType,_AD:juniERXSysSlotRev,_r:juniERXSysSlotAdminStatus,_s:juniERXSysSlotOperStatus,_t:juniERXSysSlotDisableReason,_AE:juniERXSysSlotExpectedCardType,_AF:juniERXSysSlotControl,_AG:juniERXSysSlotCpuUtilPct,_AH:juniERXSysSlotMemUtilPct,_AI:juniERXSysSlotIoaPresent,_AJ:juniERXSysSlotPortCount,_AK:juniERXSysSlotLastChange,_AL:juniERXSysSlotRedundancyLockout,_AM:juniERXSysSlotRedundancyGroupId,_u:juniERXSysSlotSpareServer,_v:juniERXSysSlotAssociatedSlot,_AN:juniERXSysSlotRevertControl,_AO:juniERXSysSlotRedundancyRevertTime,_AP:juniERXSysSlotBootReleaseFile,_AQ:juniERXSysSlotBootBackupReleaseFile,_As:juniERXSysSlotSerialNumber,_At:juniERXSysSlotAssemblyPartNumber,_Au:juniERXSysSlotAssemblyRev,_Av:juniERXSysSlotIoaSerialNumber,_Aw:juniERXSysSlotIoaAssemblyPartNumber,_Ax:juniERXSysSlotIoaAssemblyRev,'juniERXSysPort':juniERXSysPort,'juniERXSysPortTable':juniERXSysPortTable,'juniERXSysPortEntry':juniERXSysPortEntry,_Ao:juniERXSysPortIndex,_AR:juniERXSysPortDescr,_AS:juniERXSysPortType,_AT:juniERXSysPortIfIndex,'juniERXSysPower':juniERXSysPower,'juniERXSysPowerTable':juniERXSysPowerTable,'juniERXSysPowerEntry':juniERXSysPowerEntry,_Ap:juniERXSysPowerIndex,_AU:juniERXSysPowerDescr,_w:juniERXSysPowerStatus,'juniERXSysTemperature':juniERXSysTemperature,_f:juniERXSysTempFanStatus,'juniERXSysTempTable':juniERXSysTempTable,'juniERXSysTempEntry':juniERXSysTempEntry,_Aq:juniERXSysTempIndex,_x:juniERXSysTempDescr,_g:juniERXSysTempStatus,_y:juniERXSysTempValue,_Aa:juniERXSysTempProtectionStatus,_B4:juniERXSysTempProtectionHoldOffTime,_Ab:juniERXSysTempProtectionHoldOffTimeRemaining,'juniERXSysSubsystem':juniERXSysSubsystem,'juniERXSysSubsystemTable':juniERXSysSubsystemTable,'juniERXSysSubsystemEntry':juniERXSysSubsystemEntry,_Ar:juniERXSysSubsystemIndex,_AV:juniERXSysSubsystemName,_AW:juniERXSysSubsystemControl,_AX:juniERXSysSubsystemBootReleaseFile,_AY:juniERXSysSubsystemBootBackupReleaseFile,'juniERXSysConformance':juniERXSysConformance,'juniERXSysCompliances':juniERXSysCompliances,'juniERXSysCompliance':juniERXSysCompliance,'juniERXSysCompliance1':juniERXSysCompliance1,'juniERXSysCompliance2':juniERXSysCompliance2,'juniERXSysCompliance3':juniERXSysCompliance3,'juniERXSysCompliance4':juniERXSysCompliance4,'juniERXSysCompliance5':juniERXSysCompliance5,'juniERXSysGroups':juniERXSysGroups,_B7:juniERXSysGroup,_A3:juniERXSysNotifyGroup,_Ae:juniERXSysGeneralGroup,_J:juniERXSysFabricGroup,_K:juniERXSysNvsGroup,_L:juniERXSysSlotGroup,_M:juniERXSysPortGroup,_N:juniERXSysPowerGroup,_A4:juniERXSysTemperatureGroup,_O:juniERXSysSubsystemGroup,_l:juniERXSysTimingGroup,_Af:juniERXSysGeneralGroup2,_B8:juniERXSysNotifyGroup2,_Ag:juniERXSysTemperatureGroup2,_Ah:juniERXSysNotifyGroup3,_B9:juniERXSysGeneralGroup3})