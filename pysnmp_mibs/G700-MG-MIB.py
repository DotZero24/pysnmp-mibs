_AQ='cmgFipsErrorType'
_AP='cmgEtrModule'
_AO='cmgCcRelay'
_AN='cmgCcPort'
_AM='cmgCcModule'
_AL='cmgTrapManagerAddress'
_AK='cmgDSPCoreCoreId'
_AJ='controlledLoadService'
_AI='guaranteedService'
_AH='cmgExpansionSlot'
_AG='notSupported'
_AF='cmgAnalogPort'
_AE='cmgAnalogSlot'
_AD='genOpLastWarningDisplay'
_AC='cmgActiveControllerInetAddress'
_AB='cmgActiveControllerInetAddressType'
_AA='cmgVoipCurrentIpAddress'
_A9='cmgVoipAverageOccupancy'
_A8='cmgVoipTotalChannels'
_A7='cmgVoipChannelsInUse'
_A6='cmgActiveControllerAddress'
_A5='cmgModuleName'
_A4='cmgModuleType'
_A3='cmgPower8260'
_A2='cmgPowerDsp'
_A1='cmgPowerVoipComplex'
_A0='cmgPowerMediaModules'
_z='cmgPowerMgProcessor'
_y='cmgDspTempWarningThresh'
_x='cmgCpuTempWarningThresh'
_w='cmgVoipSlot'
_v='remote'
_u='cmgProductId'
_t='cmgDspTempShutdownThresh'
_s='cmgDspTemp'
_r='cmgCpuTempShutdownThresh'
_q='cmgCpuTemp'
_p='read-create'
_o='local'
_n='auto'
_m='cmgDsuPort'
_l='cmgDsuSlot'
_k='unknown'
_j='cmgModuleSlot'
_i='genOpLastFailureIndex'
_h='cmgTrapInUseTimeslots'
_g='cmgTrapAvailableTimeslots'
_f='cmgUseDhcpForMgcList'
_e='genAppFileVersionNumber'
_d='genAppFileName'
_c='genAppFileId'
_b='inactive'
_a='cmgTrapModule'
_Z='cmgActiveClockSource'
_Y='cmgSecondaryClockSource'
_X='cmgPrimaryClockSource'
_W='active'
_V='cmgModuleFaultMask'
_U='accessible-for-notify'
_T='cmgTrapSeverity'
_S='cmgVoipFaultMask'
_R='disabled'
_Q='enabled'
_P='OctetString'
_O='LOAD-MIB'
_N='on'
_M='off'
_L='cmgMgpFaultMask'
_K='cmgHardwareFaultMask'
_J='DisplayString'
_I='obsolete'
_H='read-write'
_G='cmgTrapLocation'
_F='cmgTrapOnBoard'
_E='cmgTrapSubsystem'
_D='Integer32'
_C='read-only'
_B='current'
_A='G700-MG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
genAppFileId,genAppFileName,genAppFileVersionNumber,genOpLastFailureIndex,genOpLastWarningDisplay=mibBuilder.importSymbols(_O,_c,_d,_e,_i,_AD)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
cmgmib=ModuleIdentity((1,3,6,1,4,1,6889,2,9,1))
if mibBuilder.loadTexts:cmgmib.setRevisions(('2015-03-23 06:00',))
class CmgItuPerceivedSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6)))
class CmgModuleSlot(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_Avaya_ObjectIdentity=ObjectIdentity
avaya=_Avaya_ObjectIdentity((1,3,6,1,4,1,6889))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,6889,1))
_G700MediaGateway_ObjectIdentity=ObjectIdentity
g700MediaGateway=_G700MediaGateway_ObjectIdentity((1,3,6,1,4,1,6889,1,9))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,6889,2))
_G700MediaGatewayMIB_ObjectIdentity=ObjectIdentity
g700MediaGatewayMIB=_G700MediaGatewayMIB_ObjectIdentity((1,3,6,1,4,1,6889,2,9))
_CmgChassis_ObjectIdentity=ObjectIdentity
cmgChassis=_CmgChassis_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,1))
class _CmgHWType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10,28,29,30,31,32,33,34,35,37,41)));namedValues=NamedValues(*(('media-gateway',1),('g350',2),('avayaG250',3),('avayaG250-BRI',4),('avayaG250-DS1',5),('avayaG250-DCP',6),('avayaG450',7),('avayaG250-A14',8),('avayaTGM550',10),('avayaCommunicationManagerBranchEditioni120',28),('avayaCommunicationManagerBranchEditioni40-Analog',29),('avayaCommunicationManagerBranchEditioni40-BRI',30),('avayaCommunicationManagerBranchEditioni40-DS1',31),('avayaCommunicationManagerBranchEditioni40-DCP',32),('avayaTRM480',33),('avayaCommunicationManagerBranchEditioni40-A14',34),('avayaCommunicationManagerBranchEditionG450',35),('avayaCommunicationManagerBranchEditionG430',37),('avayaG430',41)))
_CmgHWType_Type.__name__=_D
_CmgHWType_Object=MibScalar
cmgHWType=_CmgHWType_Object((1,3,6,1,4,1,6889,2,9,1,1,1),_CmgHWType_Type())
cmgHWType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgHWType.setStatus(_B)
class _CmgModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CmgModelNumber_Type.__name__=_J
_CmgModelNumber_Object=MibScalar
cmgModelNumber=_CmgModelNumber_Object((1,3,6,1,4,1,6889,2,9,1,1,2),_CmgModelNumber_Type())
cmgModelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModelNumber.setStatus(_B)
class _CmgDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmgDescription_Type.__name__=_J
_CmgDescription_Object=MibScalar
cmgDescription=_CmgDescription_Object((1,3,6,1,4,1,6889,2,9,1,1,3),_CmgDescription_Type())
cmgDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDescription.setStatus(_B)
class _CmgSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CmgSerialNumber_Type.__name__=_J
_CmgSerialNumber_Object=MibScalar
cmgSerialNumber=_CmgSerialNumber_Object((1,3,6,1,4,1,6889,2,9,1,1,4),_CmgSerialNumber_Type())
cmgSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgSerialNumber.setStatus(_B)
class _CmgHWVintage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CmgHWVintage_Type.__name__=_J
_CmgHWVintage_Object=MibScalar
cmgHWVintage=_CmgHWVintage_Object((1,3,6,1,4,1,6889,2,9,1,1,5),_CmgHWVintage_Type())
cmgHWVintage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgHWVintage.setStatus(_B)
class _CmgHWSuffix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CmgHWSuffix_Type.__name__=_J
_CmgHWSuffix_Object=MibScalar
cmgHWSuffix=_CmgHWSuffix_Object((1,3,6,1,4,1,6889,2,9,1,1,6),_CmgHWSuffix_Type())
cmgHWSuffix.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgHWSuffix.setStatus(_B)
class _CmgStackPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CmgStackPosition_Type.__name__=_D
_CmgStackPosition_Object=MibScalar
cmgStackPosition=_CmgStackPosition_Object((1,3,6,1,4,1,6889,2,9,1,1,7),_CmgStackPosition_Type())
cmgStackPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgStackPosition.setStatus(_B)
class _CmgModuleList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_CmgModuleList_Type.__name__=_P
_CmgModuleList_Object=MibScalar
cmgModuleList=_CmgModuleList_Object((1,3,6,1,4,1,6889,2,9,1,1,8),_CmgModuleList_Type())
cmgModuleList.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleList.setStatus(_B)
class _CmgReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgReset_Type.__name__=_D
_CmgReset_Object=MibScalar
cmgReset=_CmgReset_Object((1,3,6,1,4,1,6889,2,9,1,1,9),_CmgReset_Type())
cmgReset.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgReset.setStatus(_B)
_CmgHardware_ObjectIdentity=ObjectIdentity
cmgHardware=_CmgHardware_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,1,10))
_CmgCpuTemp_Type=Integer32
_CmgCpuTemp_Object=MibScalar
cmgCpuTemp=_CmgCpuTemp_Object((1,3,6,1,4,1,6889,2,9,1,1,10,1),_CmgCpuTemp_Type())
cmgCpuTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCpuTemp.setStatus(_B)
_CmgCpuTempWarningThresh_Type=Integer32
_CmgCpuTempWarningThresh_Object=MibScalar
cmgCpuTempWarningThresh=_CmgCpuTempWarningThresh_Object((1,3,6,1,4,1,6889,2,9,1,1,10,2),_CmgCpuTempWarningThresh_Type())
cmgCpuTempWarningThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCpuTempWarningThresh.setStatus(_B)
_CmgCpuTempShutdownThresh_Type=Integer32
_CmgCpuTempShutdownThresh_Object=MibScalar
cmgCpuTempShutdownThresh=_CmgCpuTempShutdownThresh_Object((1,3,6,1,4,1,6889,2,9,1,1,10,3),_CmgCpuTempShutdownThresh_Type())
cmgCpuTempShutdownThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCpuTempShutdownThresh.setStatus(_B)
_CmgDspTemp_Type=Integer32
_CmgDspTemp_Object=MibScalar
cmgDspTemp=_CmgDspTemp_Object((1,3,6,1,4,1,6889,2,9,1,1,10,4),_CmgDspTemp_Type())
cmgDspTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDspTemp.setStatus(_B)
_CmgDspTempWarningThresh_Type=Integer32
_CmgDspTempWarningThresh_Object=MibScalar
cmgDspTempWarningThresh=_CmgDspTempWarningThresh_Object((1,3,6,1,4,1,6889,2,9,1,1,10,5),_CmgDspTempWarningThresh_Type())
cmgDspTempWarningThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDspTempWarningThresh.setStatus(_B)
_CmgDspTempShutdownThresh_Type=Integer32
_CmgDspTempShutdownThresh_Object=MibScalar
cmgDspTempShutdownThresh=_CmgDspTempShutdownThresh_Object((1,3,6,1,4,1,6889,2,9,1,1,10,6),_CmgDspTempShutdownThresh_Type())
cmgDspTempShutdownThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDspTempShutdownThresh.setStatus(_B)
_CmgPowerMgProcessor_Type=Integer32
_CmgPowerMgProcessor_Object=MibScalar
cmgPowerMgProcessor=_CmgPowerMgProcessor_Object((1,3,6,1,4,1,6889,2,9,1,1,10,7),_CmgPowerMgProcessor_Type())
cmgPowerMgProcessor.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgPowerMgProcessor.setStatus(_B)
_CmgPowerMediaModules_Type=Integer32
_CmgPowerMediaModules_Object=MibScalar
cmgPowerMediaModules=_CmgPowerMediaModules_Object((1,3,6,1,4,1,6889,2,9,1,1,10,8),_CmgPowerMediaModules_Type())
cmgPowerMediaModules.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgPowerMediaModules.setStatus(_B)
_CmgPowerVoipComplex_Type=Integer32
_CmgPowerVoipComplex_Object=MibScalar
cmgPowerVoipComplex=_CmgPowerVoipComplex_Object((1,3,6,1,4,1,6889,2,9,1,1,10,9),_CmgPowerVoipComplex_Type())
cmgPowerVoipComplex.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgPowerVoipComplex.setStatus(_B)
_CmgPowerDsp_Type=Integer32
_CmgPowerDsp_Object=MibScalar
cmgPowerDsp=_CmgPowerDsp_Object((1,3,6,1,4,1,6889,2,9,1,1,10,10),_CmgPowerDsp_Type())
cmgPowerDsp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgPowerDsp.setStatus(_B)
_CmgPower8260_Type=Integer32
_CmgPower8260_Object=MibScalar
cmgPower8260=_CmgPower8260_Object((1,3,6,1,4,1,6889,2,9,1,1,10,11),_CmgPower8260_Type())
cmgPower8260.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgPower8260.setStatus(_B)
class _CmgHardwareFaultMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_CmgHardwareFaultMask_Type.__name__=_P
_CmgHardwareFaultMask_Object=MibScalar
cmgHardwareFaultMask=_CmgHardwareFaultMask_Object((1,3,6,1,4,1,6889,2,9,1,1,10,12),_CmgHardwareFaultMask_Type())
cmgHardwareFaultMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgHardwareFaultMask.setStatus(_B)
class _CmgHardwareStatusMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CmgHardwareStatusMask_Type.__name__=_P
_CmgHardwareStatusMask_Object=MibScalar
cmgHardwareStatusMask=_CmgHardwareStatusMask_Object((1,3,6,1,4,1,6889,2,9,1,1,10,13),_CmgHardwareStatusMask_Type())
cmgHardwareStatusMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgHardwareStatusMask.setStatus(_B)
class _CmgHardwareFanLowSpeedLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CmgHardwareFanLowSpeedLevel_Type.__name__=_D
_CmgHardwareFanLowSpeedLevel_Object=MibScalar
cmgHardwareFanLowSpeedLevel=_CmgHardwareFanLowSpeedLevel_Object((1,3,6,1,4,1,6889,2,9,1,1,10,14),_CmgHardwareFanLowSpeedLevel_Type())
cmgHardwareFanLowSpeedLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgHardwareFanLowSpeedLevel.setStatus(_B)
_CmgModules_ObjectIdentity=ObjectIdentity
cmgModules=_CmgModules_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,1,11))
_CmgModuleTable_Object=MibTable
cmgModuleTable=_CmgModuleTable_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1))
if mibBuilder.loadTexts:cmgModuleTable.setStatus(_B)
_CmgModuleEntry_Object=MibTableRow
cmgModuleEntry=_CmgModuleEntry_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1))
cmgModuleEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:cmgModuleEntry.setStatus(_B)
class _CmgModuleSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_CmgModuleSlot_Type.__name__=_D
_CmgModuleSlot_Object=MibTableColumn
cmgModuleSlot=_CmgModuleSlot_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,1),_CmgModuleSlot_Type())
cmgModuleSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleSlot.setStatus(_B)
class _CmgModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32,33,34,40,41,42,43,44,45,46,47,48,49,50,51,52,253,255)));namedValues=NamedValues(*(('t1e1-voip',1),('bri',2),('dcp',3),('analog',4),('t1e1',5),('voip',6),('icc',7),('fxo4fxs4',9),('bri2',10),('ds1wan',11),('uspwan',12),('dcp24hd',13),('poe24',14),('g350intana',16),('dcp24',17),('fxs24',18),('g250-int-analog-2L4T',19),('g250-int-analog-2L1T',20),('g250-int-BRI',21),('poe40',22),('g250-int-12pDCP',23),('g250-int-DS1',24),('poe24cr',25),('poe8',26),('g250-int-analog-6L8T',29),('tgm550-int-analog-2L2T',30),('tim514',31),('tim510',32),('tim521',33),('avayaAM110ApplicationModule',34),('g450Mainboard',40),('tim508',41),('tim516',42),('tim518',43),('i120-intana',44),('i40-int-analog-2L4T',45),('i40-int-analog-2L1T',46),('i40-int-BRI',47),('i40-int-DS1',48),('i40-A14-int-analog-6L8T',49),('avayaCommunicationManagerBranchEditionG450Mainboard',50),('g430Mainboard',51),('bri8',52),('invalid',253),(_k,255)))
_CmgModuleType_Type.__name__=_D
_CmgModuleType_Object=MibTableColumn
cmgModuleType=_CmgModuleType_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,2),_CmgModuleType_Type())
cmgModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleType.setStatus(_B)
class _CmgModuleDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmgModuleDescription_Type.__name__=_J
_CmgModuleDescription_Object=MibTableColumn
cmgModuleDescription=_CmgModuleDescription_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,3),_CmgModuleDescription_Type())
cmgModuleDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleDescription.setStatus(_B)
class _CmgModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmgModuleName_Type.__name__=_J
_CmgModuleName_Object=MibTableColumn
cmgModuleName=_CmgModuleName_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,4),_CmgModuleName_Type())
cmgModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleName.setStatus(_B)
class _CmgModuleSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CmgModuleSerialNumber_Type.__name__=_J
_CmgModuleSerialNumber_Object=MibTableColumn
cmgModuleSerialNumber=_CmgModuleSerialNumber_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,5),_CmgModuleSerialNumber_Type())
cmgModuleSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleSerialNumber.setStatus(_B)
class _CmgModuleHWVintage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CmgModuleHWVintage_Type.__name__=_J
_CmgModuleHWVintage_Object=MibTableColumn
cmgModuleHWVintage=_CmgModuleHWVintage_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,6),_CmgModuleHWVintage_Type())
cmgModuleHWVintage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleHWVintage.setStatus(_B)
class _CmgModuleHWSuffix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CmgModuleHWSuffix_Type.__name__=_J
_CmgModuleHWSuffix_Object=MibTableColumn
cmgModuleHWSuffix=_CmgModuleHWSuffix_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,7),_CmgModuleHWSuffix_Type())
cmgModuleHWSuffix.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleHWSuffix.setStatus(_B)
class _CmgModuleFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmgModuleFWVersion_Type.__name__=_J
_CmgModuleFWVersion_Object=MibTableColumn
cmgModuleFWVersion=_CmgModuleFWVersion_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,8),_CmgModuleFWVersion_Type())
cmgModuleFWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleFWVersion.setStatus(_B)
class _CmgModuleNumberOfPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CmgModuleNumberOfPorts_Type.__name__=_D
_CmgModuleNumberOfPorts_Object=MibTableColumn
cmgModuleNumberOfPorts=_CmgModuleNumberOfPorts_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,9),_CmgModuleNumberOfPorts_Type())
cmgModuleNumberOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleNumberOfPorts.setStatus(_B)
class _CmgModuleFaultMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CmgModuleFaultMask_Type.__name__=_P
_CmgModuleFaultMask_Object=MibTableColumn
cmgModuleFaultMask=_CmgModuleFaultMask_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,10),_CmgModuleFaultMask_Type())
cmgModuleFaultMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleFaultMask.setStatus(_B)
class _CmgModuleStatusMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CmgModuleStatusMask_Type.__name__=_P
_CmgModuleStatusMask_Object=MibTableColumn
cmgModuleStatusMask=_CmgModuleStatusMask_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,11),_CmgModuleStatusMask_Type())
cmgModuleStatusMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleStatusMask.setStatus(_B)
class _CmgModuleReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgModuleReset_Type.__name__=_D
_CmgModuleReset_Object=MibTableColumn
cmgModuleReset=_CmgModuleReset_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,12),_CmgModuleReset_Type())
cmgModuleReset.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgModuleReset.setStatus(_B)
class _CmgModuleNumberOfChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CmgModuleNumberOfChannels_Type.__name__=_D
_CmgModuleNumberOfChannels_Object=MibTableColumn
cmgModuleNumberOfChannels=_CmgModuleNumberOfChannels_Object((1,3,6,1,4,1,6889,2,9,1,1,11,1,1,13),_CmgModuleNumberOfChannels_Type())
cmgModuleNumberOfChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgModuleNumberOfChannels.setStatus(_B)
_CmgDsu_ObjectIdentity=ObjectIdentity
cmgDsu=_CmgDsu_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,1,11,2))
_CmgDsuConfigTable_Object=MibTable
cmgDsuConfigTable=_CmgDsuConfigTable_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1))
if mibBuilder.loadTexts:cmgDsuConfigTable.setStatus(_I)
_CmgDsuConfigEntry_Object=MibTableRow
cmgDsuConfigEntry=_CmgDsuConfigEntry_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1))
cmgDsuConfigEntry.setIndexNames((0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:cmgDsuConfigEntry.setStatus(_I)
class _CmgDsuSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CmgDsuSlot_Type.__name__=_D
_CmgDsuSlot_Object=MibTableColumn
cmgDsuSlot=_CmgDsuSlot_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,1),_CmgDsuSlot_Type())
cmgDsuSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuSlot.setStatus(_I)
class _CmgDsuPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CmgDsuPort_Type.__name__=_D
_CmgDsuPort_Object=MibTableColumn
cmgDsuPort=_CmgDsuPort_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,2),_CmgDsuPort_Type())
cmgDsuPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuPort.setStatus(_I)
class _CmgDsuPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgDsuPortEnable_Type.__name__=_D
_CmgDsuPortEnable_Object=MibTableColumn
cmgDsuPortEnable=_CmgDsuPortEnable_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,3),_CmgDsuPortEnable_Type())
cmgDsuPortEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuPortEnable.setStatus(_I)
class _CmgDsuDataFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rate56Kbps',1),('rate64KbpsClear',2)))
_CmgDsuDataFormat_Type.__name__=_D
_CmgDsuDataFormat_Object=MibTableColumn
cmgDsuDataFormat=_CmgDsuDataFormat_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,4),_CmgDsuDataFormat_Type())
cmgDsuDataFormat.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuDataFormat.setStatus(_I)
class _CmgDsuFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dtr-rts',1),('dtr',2),('rts',3),('disable',4)))
_CmgDsuFlowControl_Type.__name__=_D
_CmgDsuFlowControl_Object=MibTableColumn
cmgDsuFlowControl=_CmgDsuFlowControl_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,5),_CmgDsuFlowControl_Type())
cmgDsuFlowControl.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuFlowControl.setStatus(_I)
class _CmgDsuYellowAlarmAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('halt',2)))
_CmgDsuYellowAlarmAction_Type.__name__=_D
_CmgDsuYellowAlarmAction_Object=MibTableColumn
cmgDsuYellowAlarmAction=_CmgDsuYellowAlarmAction_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,6),_CmgDsuYellowAlarmAction_Type())
cmgDsuYellowAlarmAction.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuYellowAlarmAction.setStatus(_I)
class _CmgDsuReceiveClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_CmgDsuReceiveClock_Type.__name__=_D
_CmgDsuReceiveClock_Object=MibTableColumn
cmgDsuReceiveClock=_CmgDsuReceiveClock_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,7),_CmgDsuReceiveClock_Type())
cmgDsuReceiveClock.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuReceiveClock.setStatus(_I)
class _CmgDsuInvertTxC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgDsuInvertTxC_Type.__name__=_D
_CmgDsuInvertTxC_Object=MibTableColumn
cmgDsuInvertTxC=_CmgDsuInvertTxC_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,8),_CmgDsuInvertTxC_Type())
cmgDsuInvertTxC.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuInvertTxC.setStatus(_I)
class _CmgDsuInvertRxC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgDsuInvertRxC_Type.__name__=_D
_CmgDsuInvertRxC_Object=MibTableColumn
cmgDsuInvertRxC=_CmgDsuInvertRxC_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,9),_CmgDsuInvertRxC_Type())
cmgDsuInvertRxC.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuInvertRxC.setStatus(_I)
class _CmgDsuInvertTxD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgDsuInvertTxD_Type.__name__=_D
_CmgDsuInvertTxD_Object=MibTableColumn
cmgDsuInvertTxD=_CmgDsuInvertTxD_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,10),_CmgDsuInvertTxD_Type())
cmgDsuInvertTxD.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuInvertTxD.setStatus(_I)
class _CmgDsuInvertRxD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgDsuInvertRxD_Type.__name__=_D
_CmgDsuInvertRxD_Object=MibTableColumn
cmgDsuInvertRxD=_CmgDsuInvertRxD_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,11),_CmgDsuInvertRxD_Type())
cmgDsuInvertRxD.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuInvertRxD.setStatus(_I)
class _CmgDsuPortInitiatedLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('disallow',2)))
_CmgDsuPortInitiatedLoopback_Type.__name__=_D
_CmgDsuPortInitiatedLoopback_Object=MibTableColumn
cmgDsuPortInitiatedLoopback=_CmgDsuPortInitiatedLoopback_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,12),_CmgDsuPortInitiatedLoopback_Type())
cmgDsuPortInitiatedLoopback.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuPortInitiatedLoopback.setStatus(_I)
class _CmgDsuNetworkInitiatedLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('disallow',2)))
_CmgDsuNetworkInitiatedLoopback_Type.__name__=_D
_CmgDsuNetworkInitiatedLoopback_Object=MibTableColumn
cmgDsuNetworkInitiatedLoopback=_CmgDsuNetworkInitiatedLoopback_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,13),_CmgDsuNetworkInitiatedLoopback_Type())
cmgDsuNetworkInitiatedLoopback.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuNetworkInitiatedLoopback.setStatus(_I)
class _CmgDsuChannelAssignments_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CmgDsuChannelAssignments_Type.__name__=_P
_CmgDsuChannelAssignments_Object=MibTableColumn
cmgDsuChannelAssignments=_CmgDsuChannelAssignments_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,14),_CmgDsuChannelAssignments_Type())
cmgDsuChannelAssignments.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuChannelAssignments.setStatus(_I)
class _CmgDsuDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CmgDsuDataRate_Type.__name__=_D
_CmgDsuDataRate_Object=MibTableColumn
cmgDsuDataRate=_CmgDsuDataRate_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,1,1,15),_CmgDsuDataRate_Type())
cmgDsuDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuDataRate.setStatus(_I)
_CmgDsuPortStatusTable_Object=MibTable
cmgDsuPortStatusTable=_CmgDsuPortStatusTable_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2))
if mibBuilder.loadTexts:cmgDsuPortStatusTable.setStatus(_I)
_CmgDsuPortStatusEntry_Object=MibTableRow
cmgDsuPortStatusEntry=_CmgDsuPortStatusEntry_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1))
cmgDsuPortStatusEntry.setIndexNames((0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:cmgDsuPortStatusEntry.setStatus(_I)
class _CmgDsuRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuRTS_Type.__name__=_D
_CmgDsuRTS_Object=MibTableColumn
cmgDsuRTS=_CmgDsuRTS_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,1),_CmgDsuRTS_Type())
cmgDsuRTS.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuRTS.setStatus(_I)
class _CmgDsuDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuDTR_Type.__name__=_D
_CmgDsuDTR_Object=MibTableColumn
cmgDsuDTR=_CmgDsuDTR_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,2),_CmgDsuDTR_Type())
cmgDsuDTR.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuDTR.setStatus(_I)
class _CmgDsuLL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuLL_Type.__name__=_D
_CmgDsuLL_Object=MibTableColumn
cmgDsuLL=_CmgDsuLL_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,3),_CmgDsuLL_Type())
cmgDsuLL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuLL.setStatus(_I)
class _CmgDsuRL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuRL_Type.__name__=_D
_CmgDsuRL_Object=MibTableColumn
cmgDsuRL=_CmgDsuRL_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,4),_CmgDsuRL_Type())
cmgDsuRL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuRL.setStatus(_I)
class _CmgDsuRLSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuRLSD_Type.__name__=_D
_CmgDsuRLSD_Object=MibTableColumn
cmgDsuRLSD=_CmgDsuRLSD_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,5),_CmgDsuRLSD_Type())
cmgDsuRLSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuRLSD.setStatus(_I)
class _CmgDsuCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuCTS_Type.__name__=_D
_CmgDsuCTS_Object=MibTableColumn
cmgDsuCTS=_CmgDsuCTS_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,6),_CmgDsuCTS_Type())
cmgDsuCTS.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuCTS.setStatus(_I)
class _CmgDsuDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuDSR_Type.__name__=_D
_CmgDsuDSR_Object=MibTableColumn
cmgDsuDSR=_CmgDsuDSR_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,7),_CmgDsuDSR_Type())
cmgDsuDSR.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuDSR.setStatus(_I)
class _CmgDsuRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuRing_Type.__name__=_D
_CmgDsuRing_Object=MibTableColumn
cmgDsuRing=_CmgDsuRing_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,8),_CmgDsuRing_Type())
cmgDsuRing.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuRing.setStatus(_I)
class _CmgDsuTestMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuTestMode_Type.__name__=_D
_CmgDsuTestMode_Object=MibTableColumn
cmgDsuTestMode=_CmgDsuTestMode_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,9),_CmgDsuTestMode_Type())
cmgDsuTestMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuTestMode.setStatus(_I)
class _CmgDsuTxD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mark',1),('space',2),('cycling',3)))
_CmgDsuTxD_Type.__name__=_D
_CmgDsuTxD_Object=MibTableColumn
cmgDsuTxD=_CmgDsuTxD_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,10),_CmgDsuTxD_Type())
cmgDsuTxD.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuTxD.setStatus(_I)
class _CmgDsuRxD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mark',1),('space',2),('cycling',3)))
_CmgDsuRxD_Type.__name__=_D
_CmgDsuRxD_Object=MibTableColumn
cmgDsuRxD=_CmgDsuRxD_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,11),_CmgDsuRxD_Type())
cmgDsuRxD.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuRxD.setStatus(_I)
class _CmgDsuFaultMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CmgDsuFaultMask_Type.__name__=_P
_CmgDsuFaultMask_Object=MibTableColumn
cmgDsuFaultMask=_CmgDsuFaultMask_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,12),_CmgDsuFaultMask_Type())
cmgDsuFaultMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuFaultMask.setStatus(_I)
class _CmgDsuStatusMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CmgDsuStatusMask_Type.__name__=_P
_CmgDsuStatusMask_Object=MibTableColumn
cmgDsuStatusMask=_CmgDsuStatusMask_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,2,1,13),_CmgDsuStatusMask_Type())
cmgDsuStatusMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuStatusMask.setStatus(_I)
_CmgDsuTestTable_Object=MibTable
cmgDsuTestTable=_CmgDsuTestTable_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3))
if mibBuilder.loadTexts:cmgDsuTestTable.setStatus(_I)
_CmgDsuTestEntry_Object=MibTableRow
cmgDsuTestEntry=_CmgDsuTestEntry_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1))
cmgDsuTestEntry.setIndexNames((0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:cmgDsuTestEntry.setStatus(_I)
class _CmgDsuLoopbackPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('allZeroes',1),('allOnes',2),('oneZeroOne',3),('oneIn5',4),('oneIn8',5),('threeIn24',6),('qrs',7),('qrs511',8),('qrs2047',9),('none',255)))
_CmgDsuLoopbackPattern_Type.__name__=_D
_CmgDsuLoopbackPattern_Object=MibTableColumn
cmgDsuLoopbackPattern=_CmgDsuLoopbackPattern_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1,1),_CmgDsuLoopbackPattern_Type())
cmgDsuLoopbackPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuLoopbackPattern.setStatus(_I)
class _CmgDsuLocalDteLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_b,2)))
_CmgDsuLocalDteLoopback_Type.__name__=_D
_CmgDsuLocalDteLoopback_Object=MibTableColumn
cmgDsuLocalDteLoopback=_CmgDsuLocalDteLoopback_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1,2),_CmgDsuLocalDteLoopback_Type())
cmgDsuLocalDteLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuLocalDteLoopback.setStatus(_I)
class _CmgDsuNearEndDataChannelLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_b,2)))
_CmgDsuNearEndDataChannelLoopback_Type.__name__=_D
_CmgDsuNearEndDataChannelLoopback_Object=MibTableColumn
cmgDsuNearEndDataChannelLoopback=_CmgDsuNearEndDataChannelLoopback_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1,3),_CmgDsuNearEndDataChannelLoopback_Type())
cmgDsuNearEndDataChannelLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuNearEndDataChannelLoopback.setStatus(_I)
class _CmgDsuFarEndDataChannelLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_b,2)))
_CmgDsuFarEndDataChannelLoopback_Type.__name__=_D
_CmgDsuFarEndDataChannelLoopback_Object=MibTableColumn
cmgDsuFarEndDataChannelLoopback=_CmgDsuFarEndDataChannelLoopback_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1,4),_CmgDsuFarEndDataChannelLoopback_Type())
cmgDsuFarEndDataChannelLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuFarEndDataChannelLoopback.setStatus(_I)
class _CmgDsuRemoteLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_b,2)))
_CmgDsuRemoteLoopback_Type.__name__=_D
_CmgDsuRemoteLoopback_Object=MibTableColumn
cmgDsuRemoteLoopback=_CmgDsuRemoteLoopback_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1,5),_CmgDsuRemoteLoopback_Type())
cmgDsuRemoteLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuRemoteLoopback.setStatus(_I)
class _CmgDsuDataTerminalLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_b,2)))
_CmgDsuDataTerminalLoopback_Type.__name__=_D
_CmgDsuDataTerminalLoopback_Object=MibTableColumn
cmgDsuDataTerminalLoopback=_CmgDsuDataTerminalLoopback_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1,6),_CmgDsuDataTerminalLoopback_Type())
cmgDsuDataTerminalLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDsuDataTerminalLoopback.setStatus(_I)
class _CmgDsuReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDsuReset_Type.__name__=_D
_CmgDsuReset_Object=MibTableColumn
cmgDsuReset=_CmgDsuReset_Object((1,3,6,1,4,1,6889,2,9,1,1,11,2,3,1,7),_CmgDsuReset_Type())
cmgDsuReset.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDsuReset.setStatus(_I)
_CmgAnalogPorts_ObjectIdentity=ObjectIdentity
cmgAnalogPorts=_CmgAnalogPorts_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,1,12))
_CmgAnalogPortTable_Object=MibTable
cmgAnalogPortTable=_CmgAnalogPortTable_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1))
if mibBuilder.loadTexts:cmgAnalogPortTable.setStatus(_B)
_CmgAnalogPortEntry_Object=MibTableRow
cmgAnalogPortEntry=_CmgAnalogPortEntry_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1))
cmgAnalogPortEntry.setIndexNames((0,_A,_AE),(0,_A,_AF))
if mibBuilder.loadTexts:cmgAnalogPortEntry.setStatus(_B)
class _CmgAnalogSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_CmgAnalogSlot_Type.__name__=_D
_CmgAnalogSlot_Object=MibTableColumn
cmgAnalogSlot=_CmgAnalogSlot_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,1),_CmgAnalogSlot_Type())
cmgAnalogSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgAnalogSlot.setStatus(_B)
class _CmgAnalogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_CmgAnalogPort_Type.__name__=_D
_CmgAnalogPort_Object=MibTableColumn
cmgAnalogPort=_CmgAnalogPort_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,2),_CmgAnalogPort_Type())
cmgAnalogPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgAnalogPort.setStatus(_B)
class _CmgAnalogEchoCancellerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_n,0),(_N,1),(_M,2),('fixedOn',3),(_AG,4)))
_CmgAnalogEchoCancellerControl_Type.__name__=_D
_CmgAnalogEchoCancellerControl_Object=MibTableColumn
cmgAnalogEchoCancellerControl=_CmgAnalogEchoCancellerControl_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,3),_CmgAnalogEchoCancellerControl_Type())
cmgAnalogEchoCancellerControl.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgAnalogEchoCancellerControl.setStatus(_B)
class _CmgAnalogEchoCancellerConfig1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CmgAnalogEchoCancellerConfig1_Type.__name__=_D
_CmgAnalogEchoCancellerConfig1_Object=MibTableColumn
cmgAnalogEchoCancellerConfig1=_CmgAnalogEchoCancellerConfig1_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,4),_CmgAnalogEchoCancellerConfig1_Type())
cmgAnalogEchoCancellerConfig1.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgAnalogEchoCancellerConfig1.setStatus(_B)
class _CmgAnalogEchoCancellerConfig2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CmgAnalogEchoCancellerConfig2_Type.__name__=_D
_CmgAnalogEchoCancellerConfig2_Object=MibTableColumn
cmgAnalogEchoCancellerConfig2=_CmgAnalogEchoCancellerConfig2_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,5),_CmgAnalogEchoCancellerConfig2_Type())
cmgAnalogEchoCancellerConfig2.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgAnalogEchoCancellerConfig2.setStatus(_B)
class _CmgAnalogBalance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CmgAnalogBalance_Type.__name__=_D
_CmgAnalogBalance_Object=MibTableColumn
cmgAnalogBalance=_CmgAnalogBalance_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,6),_CmgAnalogBalance_Type())
cmgAnalogBalance.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgAnalogBalance.setStatus(_B)
class _CmgAnalogReceiveGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-600,300))
_CmgAnalogReceiveGain_Type.__name__=_D
_CmgAnalogReceiveGain_Object=MibTableColumn
cmgAnalogReceiveGain=_CmgAnalogReceiveGain_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,7),_CmgAnalogReceiveGain_Type())
cmgAnalogReceiveGain.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgAnalogReceiveGain.setStatus(_B)
class _CmgAnalogTransmitGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-600,300))
_CmgAnalogTransmitGain_Type.__name__=_D
_CmgAnalogTransmitGain_Object=MibTableColumn
cmgAnalogTransmitGain=_CmgAnalogTransmitGain_Object((1,3,6,1,4,1,6889,2,9,1,1,12,1,1,8),_CmgAnalogTransmitGain_Type())
cmgAnalogTransmitGain.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgAnalogTransmitGain.setStatus(_B)
_CmgExpansionUnits_ObjectIdentity=ObjectIdentity
cmgExpansionUnits=_CmgExpansionUnits_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,1,13))
_CmgExpansionUnitsTable_Object=MibTable
cmgExpansionUnitsTable=_CmgExpansionUnitsTable_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1))
if mibBuilder.loadTexts:cmgExpansionUnitsTable.setStatus(_B)
_CmgExpansions_Object=MibTableRow
cmgExpansions=_CmgExpansions_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1))
cmgExpansions.setIndexNames((0,_A,_AH))
if mibBuilder.loadTexts:cmgExpansions.setStatus(_B)
class _CmgExpansionSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CmgExpansionSlot_Type.__name__=_D
_CmgExpansionSlot_Object=MibTableColumn
cmgExpansionSlot=_CmgExpansionSlot_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,1),_CmgExpansionSlot_Type())
cmgExpansionSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgExpansionSlot.setStatus(_B)
class _CmgExpansionModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CmgExpansionModelNumber_Type.__name__=_J
_CmgExpansionModelNumber_Object=MibTableColumn
cmgExpansionModelNumber=_CmgExpansionModelNumber_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,2),_CmgExpansionModelNumber_Type())
cmgExpansionModelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgExpansionModelNumber.setStatus(_B)
class _CmgExpansionDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmgExpansionDescription_Type.__name__=_J
_CmgExpansionDescription_Object=MibTableColumn
cmgExpansionDescription=_CmgExpansionDescription_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,3),_CmgExpansionDescription_Type())
cmgExpansionDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgExpansionDescription.setStatus(_B)
class _CmgExpansionSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CmgExpansionSerialNumber_Type.__name__=_J
_CmgExpansionSerialNumber_Object=MibTableColumn
cmgExpansionSerialNumber=_CmgExpansionSerialNumber_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,4),_CmgExpansionSerialNumber_Type())
cmgExpansionSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgExpansionSerialNumber.setStatus(_B)
class _CmgExpansionHWVintage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CmgExpansionHWVintage_Type.__name__=_J
_CmgExpansionHWVintage_Object=MibTableColumn
cmgExpansionHWVintage=_CmgExpansionHWVintage_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,5),_CmgExpansionHWVintage_Type())
cmgExpansionHWVintage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgExpansionHWVintage.setStatus(_B)
class _CmgExpansionHWSuffix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CmgExpansionHWSuffix_Type.__name__=_J
_CmgExpansionHWSuffix_Object=MibTableColumn
cmgExpansionHWSuffix=_CmgExpansionHWSuffix_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,6),_CmgExpansionHWSuffix_Type())
cmgExpansionHWSuffix.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgExpansionHWSuffix.setStatus(_B)
class _CmgExpansionDemandTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgExpansionDemandTest_Type.__name__=_D
_CmgExpansionDemandTest_Object=MibTableColumn
cmgExpansionDemandTest=_CmgExpansionDemandTest_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,7),_CmgExpansionDemandTest_Type())
cmgExpansionDemandTest.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgExpansionDemandTest.setStatus(_B)
class _CmgExpansionDemandTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*(('fail',1),('pass',255)))
_CmgExpansionDemandTestResult_Type.__name__=_D
_CmgExpansionDemandTestResult_Object=MibTableColumn
cmgExpansionDemandTestResult=_CmgExpansionDemandTestResult_Object((1,3,6,1,4,1,6889,2,9,1,1,13,1,1,8),_CmgExpansionDemandTestResult_Type())
cmgExpansionDemandTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgExpansionDemandTestResult.setStatus(_B)
class _CmgTimeslotMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgTimeslotMonitoring_Type.__name__=_D
_CmgTimeslotMonitoring_Object=MibScalar
cmgTimeslotMonitoring=_CmgTimeslotMonitoring_Object((1,3,6,1,4,1,6889,2,9,1,1,14),_CmgTimeslotMonitoring_Type())
cmgTimeslotMonitoring.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgTimeslotMonitoring.setStatus(_B)
class _CmgTimeslotUpperThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CmgTimeslotUpperThreshold_Type.__name__=_D
_CmgTimeslotUpperThreshold_Object=MibScalar
cmgTimeslotUpperThreshold=_CmgTimeslotUpperThreshold_Object((1,3,6,1,4,1,6889,2,9,1,1,15),_CmgTimeslotUpperThreshold_Type())
cmgTimeslotUpperThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgTimeslotUpperThreshold.setStatus(_B)
class _CmgTimeslotLowerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_CmgTimeslotLowerThreshold_Type.__name__=_D
_CmgTimeslotLowerThreshold_Object=MibScalar
cmgTimeslotLowerThreshold=_CmgTimeslotLowerThreshold_Object((1,3,6,1,4,1,6889,2,9,1,1,16),_CmgTimeslotLowerThreshold_Type())
cmgTimeslotLowerThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgTimeslotLowerThreshold.setStatus(_B)
_CmgProcessor_ObjectIdentity=ObjectIdentity
cmgProcessor=_CmgProcessor_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,2))
_CmgProcessorConfig_ObjectIdentity=ObjectIdentity
cmgProcessorConfig=_CmgProcessorConfig_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,2,1))
class _CmgGatewayNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_CmgGatewayNumber_Type.__name__=_J
_CmgGatewayNumber_Object=MibScalar
cmgGatewayNumber=_CmgGatewayNumber_Object((1,3,6,1,4,1,6889,2,9,1,2,1,1),_CmgGatewayNumber_Type())
cmgGatewayNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgGatewayNumber.setStatus(_B)
class _CmgMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CmgMACAddress_Type.__name__=_P
_CmgMACAddress_Object=MibScalar
cmgMACAddress=_CmgMACAddress_Object((1,3,6,1,4,1,6889,2,9,1,2,1,2),_CmgMACAddress_Type())
cmgMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgMACAddress.setStatus(_B)
class _CmgFWVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CmgFWVersion_Type.__name__=_P
_CmgFWVersion_Object=MibScalar
cmgFWVersion=_CmgFWVersion_Object((1,3,6,1,4,1,6889,2,9,1,2,1,3),_CmgFWVersion_Type())
cmgFWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgFWVersion.setStatus(_B)
_CmgCurrentIpAddress_Type=IpAddress
_CmgCurrentIpAddress_Object=MibScalar
cmgCurrentIpAddress=_CmgCurrentIpAddress_Object((1,3,6,1,4,1,6889,2,9,1,2,1,4),_CmgCurrentIpAddress_Type())
cmgCurrentIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCurrentIpAddress.setStatus(_B)
class _CmgUseDhcpForIpAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgUseDhcpForIpAddress_Type.__name__=_D
_CmgUseDhcpForIpAddress_Object=MibScalar
cmgUseDhcpForIpAddress=_CmgUseDhcpForIpAddress_Object((1,3,6,1,4,1,6889,2,9,1,2,1,7),_CmgUseDhcpForIpAddress_Type())
cmgUseDhcpForIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgUseDhcpForIpAddress.setStatus(_B)
class _CmgUseDhcpForVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgUseDhcpForVlan_Type.__name__=_D
_CmgUseDhcpForVlan_Object=MibScalar
cmgUseDhcpForVlan=_CmgUseDhcpForVlan_Object((1,3,6,1,4,1,6889,2,9,1,2,1,8),_CmgUseDhcpForVlan_Type())
cmgUseDhcpForVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgUseDhcpForVlan.setStatus(_B)
class _CmgDhcpSson_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,254))
_CmgDhcpSson_Type.__name__=_D
_CmgDhcpSson_Object=MibScalar
cmgDhcpSson=_CmgDhcpSson_Object((1,3,6,1,4,1,6889,2,9,1,2,1,9),_CmgDhcpSson_Type())
cmgDhcpSson.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDhcpSson.setStatus(_B)
_CmgStaticIpAddress_Type=IpAddress
_CmgStaticIpAddress_Object=MibScalar
cmgStaticIpAddress=_CmgStaticIpAddress_Object((1,3,6,1,4,1,6889,2,9,1,2,1,10),_CmgStaticIpAddress_Type())
cmgStaticIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgStaticIpAddress.setStatus(_B)
class _CmgDnsServerList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CmgDnsServerList_Type.__name__=_J
_CmgDnsServerList_Object=MibScalar
cmgDnsServerList=_CmgDnsServerList_Object((1,3,6,1,4,1,6889,2,9,1,2,1,13),_CmgDnsServerList_Type())
cmgDnsServerList.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDnsServerList.setStatus(_B)
class _CmgDnsHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmgDnsHostname_Type.__name__=_J
_CmgDnsHostname_Object=MibScalar
cmgDnsHostname=_CmgDnsHostname_Object((1,3,6,1,4,1,6889,2,9,1,2,1,14),_CmgDnsHostname_Type())
cmgDnsHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDnsHostname.setStatus(_B)
class _CmgMgpFaultMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_CmgMgpFaultMask_Type.__name__=_P
_CmgMgpFaultMask_Object=MibScalar
cmgMgpFaultMask=_CmgMgpFaultMask_Object((1,3,6,1,4,1,6889,2,9,1,2,1,15),_CmgMgpFaultMask_Type())
cmgMgpFaultMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgMgpFaultMask.setStatus(_B)
_CmgCurrentInetAddressType_Type=InetAddressType
_CmgCurrentInetAddressType_Object=MibScalar
cmgCurrentInetAddressType=_CmgCurrentInetAddressType_Object((1,3,6,1,4,1,6889,2,9,1,2,1,16),_CmgCurrentInetAddressType_Type())
cmgCurrentInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCurrentInetAddressType.setStatus(_B)
_CmgCurrentInetAddress_Type=InetAddress
_CmgCurrentInetAddress_Object=MibScalar
cmgCurrentInetAddress=_CmgCurrentInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,2,1,17),_CmgCurrentInetAddress_Type())
cmgCurrentInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCurrentInetAddress.setStatus(_B)
_CmgProcessorQos_ObjectIdentity=ObjectIdentity
cmgProcessorQos=_CmgProcessorQos_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,2,2))
class _CmgQosControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_v,2)))
_CmgQosControl_Type.__name__=_D
_CmgQosControl_Object=MibScalar
cmgQosControl=_CmgQosControl_Object((1,3,6,1,4,1,6889,2,9,1,2,2,1),_CmgQosControl_Type())
cmgQosControl.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgQosControl.setStatus(_B)
class _CmgRemoteSigDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CmgRemoteSigDscp_Type.__name__=_D
_CmgRemoteSigDscp_Object=MibScalar
cmgRemoteSigDscp=_CmgRemoteSigDscp_Object((1,3,6,1,4,1,6889,2,9,1,2,2,2),_CmgRemoteSigDscp_Type())
cmgRemoteSigDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgRemoteSigDscp.setStatus(_B)
class _CmgRemoteSig802Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CmgRemoteSig802Priority_Type.__name__=_D
_CmgRemoteSig802Priority_Object=MibScalar
cmgRemoteSig802Priority=_CmgRemoteSig802Priority_Object((1,3,6,1,4,1,6889,2,9,1,2,2,3),_CmgRemoteSig802Priority_Type())
cmgRemoteSig802Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgRemoteSig802Priority.setStatus(_B)
class _CmgLocalSigDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CmgLocalSigDscp_Type.__name__=_D
_CmgLocalSigDscp_Object=MibScalar
cmgLocalSigDscp=_CmgLocalSigDscp_Object((1,3,6,1,4,1,6889,2,9,1,2,2,4),_CmgLocalSigDscp_Type())
cmgLocalSigDscp.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgLocalSigDscp.setStatus(_B)
class _CmgLocalSig802Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CmgLocalSig802Priority_Type.__name__=_D
_CmgLocalSig802Priority_Object=MibScalar
cmgLocalSig802Priority=_CmgLocalSig802Priority_Object((1,3,6,1,4,1,6889,2,9,1,2,2,5),_CmgLocalSig802Priority_Type())
cmgLocalSig802Priority.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgLocalSig802Priority.setStatus(_B)
class _CmgStatic802Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4090))
_CmgStatic802Vlan_Type.__name__=_D
_CmgStatic802Vlan_Object=MibScalar
cmgStatic802Vlan=_CmgStatic802Vlan_Object((1,3,6,1,4,1,6889,2,9,1,2,2,6),_CmgStatic802Vlan_Type())
cmgStatic802Vlan.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgStatic802Vlan.setStatus(_B)
class _CmgCurrent802Vlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4090))
_CmgCurrent802Vlan_Type.__name__=_D
_CmgCurrent802Vlan_Object=MibScalar
cmgCurrent802Vlan=_CmgCurrent802Vlan_Object((1,3,6,1,4,1,6889,2,9,1,2,2,7),_CmgCurrent802Vlan_Type())
cmgCurrent802Vlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCurrent802Vlan.setStatus(_B)
_CmgProcessorClock_ObjectIdentity=ObjectIdentity
cmgProcessorClock=_CmgProcessorClock_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,2,3))
class _CmgPrimaryClockSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,21))
_CmgPrimaryClockSource_Type.__name__=_J
_CmgPrimaryClockSource_Object=MibScalar
cmgPrimaryClockSource=_CmgPrimaryClockSource_Object((1,3,6,1,4,1,6889,2,9,1,2,3,1),_CmgPrimaryClockSource_Type())
cmgPrimaryClockSource.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgPrimaryClockSource.setStatus(_B)
class _CmgSecondaryClockSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,21))
_CmgSecondaryClockSource_Type.__name__=_J
_CmgSecondaryClockSource_Object=MibScalar
cmgSecondaryClockSource=_CmgSecondaryClockSource_Object((1,3,6,1,4,1,6889,2,9,1,2,3,2),_CmgSecondaryClockSource_Type())
cmgSecondaryClockSource.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgSecondaryClockSource.setStatus(_B)
class _CmgActiveClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),(_o,3)))
_CmgActiveClockSource_Type.__name__=_D
_CmgActiveClockSource_Object=MibScalar
cmgActiveClockSource=_CmgActiveClockSource_Object((1,3,6,1,4,1,6889,2,9,1,2,3,3),_CmgActiveClockSource_Type())
cmgActiveClockSource.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgActiveClockSource.setStatus(_B)
class _CmgClockSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgClockSwitching_Type.__name__=_D
_CmgClockSwitching_Object=MibScalar
cmgClockSwitching=_CmgClockSwitching_Object((1,3,6,1,4,1,6889,2,9,1,2,3,4),_CmgClockSwitching_Type())
cmgClockSwitching.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgClockSwitching.setStatus(_B)
class _CmgClockSourceControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_v,2)))
_CmgClockSourceControl_Type.__name__=_D
_CmgClockSourceControl_Object=MibScalar
cmgClockSourceControl=_CmgClockSourceControl_Object((1,3,6,1,4,1,6889,2,9,1,2,3,5),_CmgClockSourceControl_Type())
cmgClockSourceControl.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgClockSourceControl.setStatus(_B)
_CmgControllers_ObjectIdentity=ObjectIdentity
cmgControllers=_CmgControllers_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,3))
class _CmgRegistrationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('registered',1),('notRegistered',2)))
_CmgRegistrationState_Type.__name__=_D
_CmgRegistrationState_Object=MibScalar
cmgRegistrationState=_CmgRegistrationState_Object((1,3,6,1,4,1,6889,2,9,1,3,1),_CmgRegistrationState_Type())
cmgRegistrationState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgRegistrationState.setStatus(_B)
_CmgActiveControllerAddress_Type=IpAddress
_CmgActiveControllerAddress_Object=MibScalar
cmgActiveControllerAddress=_CmgActiveControllerAddress_Object((1,3,6,1,4,1,6889,2,9,1,3,2),_CmgActiveControllerAddress_Type())
cmgActiveControllerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgActiveControllerAddress.setStatus(_B)
class _CmgH248LinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CmgH248LinkStatus_Type.__name__=_D
_CmgH248LinkStatus_Object=MibScalar
cmgH248LinkStatus=_CmgH248LinkStatus_Object((1,3,6,1,4,1,6889,2,9,1,3,3),_CmgH248LinkStatus_Type())
cmgH248LinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgH248LinkStatus.setStatus(_B)
_CmgH248LinkErrorCode_Type=Integer32
_CmgH248LinkErrorCode_Object=MibScalar
cmgH248LinkErrorCode=_CmgH248LinkErrorCode_Object((1,3,6,1,4,1,6889,2,9,1,3,4),_CmgH248LinkErrorCode_Type())
cmgH248LinkErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgH248LinkErrorCode.setStatus(_B)
class _CmgUseDhcpForMgcList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgUseDhcpForMgcList_Type.__name__=_D
_CmgUseDhcpForMgcList_Object=MibScalar
cmgUseDhcpForMgcList=_CmgUseDhcpForMgcList_Object((1,3,6,1,4,1,6889,2,9,1,3,5),_CmgUseDhcpForMgcList_Type())
cmgUseDhcpForMgcList.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgUseDhcpForMgcList.setStatus(_B)
class _CmgStaticControllerHosts_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CmgStaticControllerHosts_Type.__name__=_J
_CmgStaticControllerHosts_Object=MibScalar
cmgStaticControllerHosts=_CmgStaticControllerHosts_Object((1,3,6,1,4,1,6889,2,9,1,3,6),_CmgStaticControllerHosts_Type())
cmgStaticControllerHosts.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgStaticControllerHosts.setStatus(_B)
class _CmgDhcpControllerHosts_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmgDhcpControllerHosts_Type.__name__=_J
_CmgDhcpControllerHosts_Object=MibScalar
cmgDhcpControllerHosts=_CmgDhcpControllerHosts_Object((1,3,6,1,4,1,6889,2,9,1,3,7),_CmgDhcpControllerHosts_Type())
cmgDhcpControllerHosts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDhcpControllerHosts.setStatus(_B)
class _CmgPrimarySearchTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,59))
_CmgPrimarySearchTime_Type.__name__=_D
_CmgPrimarySearchTime_Object=MibScalar
cmgPrimarySearchTime=_CmgPrimarySearchTime_Object((1,3,6,1,4,1,6889,2,9,1,3,8),_CmgPrimarySearchTime_Type())
cmgPrimarySearchTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgPrimarySearchTime.setStatus(_B)
class _CmgTotalSearchTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,60))
_CmgTotalSearchTime_Type.__name__=_D
_CmgTotalSearchTime_Object=MibScalar
cmgTotalSearchTime=_CmgTotalSearchTime_Object((1,3,6,1,4,1,6889,2,9,1,3,9),_CmgTotalSearchTime_Type())
cmgTotalSearchTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgTotalSearchTime.setStatus(_B)
class _CmgTransitionPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CmgTransitionPoint_Type.__name__=_D
_CmgTransitionPoint_Object=MibScalar
cmgTransitionPoint=_CmgTransitionPoint_Object((1,3,6,1,4,1,6889,2,9,1,3,10),_CmgTransitionPoint_Type())
cmgTransitionPoint.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgTransitionPoint.setStatus(_B)
class _CmgActiveControllerSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CmgActiveControllerSoftwareVersion_Type.__name__=_J
_CmgActiveControllerSoftwareVersion_Object=MibScalar
cmgActiveControllerSoftwareVersion=_CmgActiveControllerSoftwareVersion_Object((1,3,6,1,4,1,6889,2,9,1,3,11),_CmgActiveControllerSoftwareVersion_Type())
cmgActiveControllerSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgActiveControllerSoftwareVersion.setStatus(_B)
_CmgActiveControllerInetAddressType_Type=InetAddressType
_CmgActiveControllerInetAddressType_Object=MibScalar
cmgActiveControllerInetAddressType=_CmgActiveControllerInetAddressType_Object((1,3,6,1,4,1,6889,2,9,1,3,12),_CmgActiveControllerInetAddressType_Type())
cmgActiveControllerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgActiveControllerInetAddressType.setStatus(_B)
_CmgActiveControllerInetAddress_Type=InetAddress
_CmgActiveControllerInetAddress_Object=MibScalar
cmgActiveControllerInetAddress=_CmgActiveControllerInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,3,13),_CmgActiveControllerInetAddress_Type())
cmgActiveControllerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgActiveControllerInetAddress.setStatus(_B)
_CmgVoip_ObjectIdentity=ObjectIdentity
cmgVoip=_CmgVoip_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4))
class _CmgVoipEngineUseDhcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgVoipEngineUseDhcp_Type.__name__=_D
_CmgVoipEngineUseDhcp_Object=MibScalar
cmgVoipEngineUseDhcp=_CmgVoipEngineUseDhcp_Object((1,3,6,1,4,1,6889,2,9,1,4,1),_CmgVoipEngineUseDhcp_Type())
cmgVoipEngineUseDhcp.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipEngineUseDhcp.setStatus(_B)
class _CmgVoipQosControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_v,2)))
_CmgVoipQosControl_Type.__name__=_D
_CmgVoipQosControl_Object=MibScalar
cmgVoipQosControl=_CmgVoipQosControl_Object((1,3,6,1,4,1,6889,2,9,1,4,2),_CmgVoipQosControl_Type())
cmgVoipQosControl.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipQosControl.setStatus(_B)
_CmgVoipRemoteParameters_ObjectIdentity=ObjectIdentity
cmgVoipRemoteParameters=_CmgVoipRemoteParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,3))
_CmgVoipRemoteQosParameters_ObjectIdentity=ObjectIdentity
cmgVoipRemoteQosParameters=_CmgVoipRemoteQosParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,3,1))
class _CmgVoipRemoteBbeDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CmgVoipRemoteBbeDscp_Type.__name__=_D
_CmgVoipRemoteBbeDscp_Object=MibScalar
cmgVoipRemoteBbeDscp=_CmgVoipRemoteBbeDscp_Object((1,3,6,1,4,1,6889,2,9,1,4,3,1,1),_CmgVoipRemoteBbeDscp_Type())
cmgVoipRemoteBbeDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteBbeDscp.setStatus(_B)
class _CmgVoipRemoteEfDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CmgVoipRemoteEfDscp_Type.__name__=_D
_CmgVoipRemoteEfDscp_Object=MibScalar
cmgVoipRemoteEfDscp=_CmgVoipRemoteEfDscp_Object((1,3,6,1,4,1,6889,2,9,1,4,3,1,2),_CmgVoipRemoteEfDscp_Type())
cmgVoipRemoteEfDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteEfDscp.setStatus(_B)
class _CmgVoipRemote802Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CmgVoipRemote802Priority_Type.__name__=_D
_CmgVoipRemote802Priority_Object=MibScalar
cmgVoipRemote802Priority=_CmgVoipRemote802Priority_Object((1,3,6,1,4,1,6889,2,9,1,4,3,1,3),_CmgVoipRemote802Priority_Type())
cmgVoipRemote802Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemote802Priority.setStatus(_B)
class _CmgVoipRemoteMinRtpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65533))
_CmgVoipRemoteMinRtpPort_Type.__name__=_D
_CmgVoipRemoteMinRtpPort_Object=MibScalar
cmgVoipRemoteMinRtpPort=_CmgVoipRemoteMinRtpPort_Object((1,3,6,1,4,1,6889,2,9,1,4,3,1,4),_CmgVoipRemoteMinRtpPort_Type())
cmgVoipRemoteMinRtpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteMinRtpPort.setStatus(_B)
class _CmgVoipRemoteMaxRtpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65535))
_CmgVoipRemoteMaxRtpPort_Type.__name__=_D
_CmgVoipRemoteMaxRtpPort_Object=MibScalar
cmgVoipRemoteMaxRtpPort=_CmgVoipRemoteMaxRtpPort_Object((1,3,6,1,4,1,6889,2,9,1,4,3,1,5),_CmgVoipRemoteMaxRtpPort_Type())
cmgVoipRemoteMaxRtpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteMaxRtpPort.setStatus(_B)
_CmgVoipRemoteRtcpParameters_ObjectIdentity=ObjectIdentity
cmgVoipRemoteRtcpParameters=_CmgVoipRemoteRtcpParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,3,2))
class _CmgVoipRemoteRtcpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgVoipRemoteRtcpEnabled_Type.__name__=_D
_CmgVoipRemoteRtcpEnabled_Object=MibScalar
cmgVoipRemoteRtcpEnabled=_CmgVoipRemoteRtcpEnabled_Object((1,3,6,1,4,1,6889,2,9,1,4,3,2,1),_CmgVoipRemoteRtcpEnabled_Type())
cmgVoipRemoteRtcpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRtcpEnabled.setStatus(_B)
_CmgVoipRemoteRtcpMonitorIpAddress_Type=IpAddress
_CmgVoipRemoteRtcpMonitorIpAddress_Object=MibScalar
cmgVoipRemoteRtcpMonitorIpAddress=_CmgVoipRemoteRtcpMonitorIpAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,3,2,2),_CmgVoipRemoteRtcpMonitorIpAddress_Type())
cmgVoipRemoteRtcpMonitorIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRtcpMonitorIpAddress.setStatus(_B)
class _CmgVoipRemoteRtcpMonitorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmgVoipRemoteRtcpMonitorPort_Type.__name__=_D
_CmgVoipRemoteRtcpMonitorPort_Object=MibScalar
cmgVoipRemoteRtcpMonitorPort=_CmgVoipRemoteRtcpMonitorPort_Object((1,3,6,1,4,1,6889,2,9,1,4,3,2,3),_CmgVoipRemoteRtcpMonitorPort_Type())
cmgVoipRemoteRtcpMonitorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRtcpMonitorPort.setStatus(_B)
class _CmgVoipRemoteRtcpReportPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_CmgVoipRemoteRtcpReportPeriod_Type.__name__=_D
_CmgVoipRemoteRtcpReportPeriod_Object=MibScalar
cmgVoipRemoteRtcpReportPeriod=_CmgVoipRemoteRtcpReportPeriod_Object((1,3,6,1,4,1,6889,2,9,1,4,3,2,4),_CmgVoipRemoteRtcpReportPeriod_Type())
cmgVoipRemoteRtcpReportPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRtcpReportPeriod.setStatus(_B)
_CmgVoipRemoteRtcpMonitorInetAddressType_Type=InetAddressType
_CmgVoipRemoteRtcpMonitorInetAddressType_Object=MibScalar
cmgVoipRemoteRtcpMonitorInetAddressType=_CmgVoipRemoteRtcpMonitorInetAddressType_Object((1,3,6,1,4,1,6889,2,9,1,4,3,2,5),_CmgVoipRemoteRtcpMonitorInetAddressType_Type())
cmgVoipRemoteRtcpMonitorInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRtcpMonitorInetAddressType.setStatus(_B)
_CmgVoipRemoteRtcpMonitorInetAddress_Type=InetAddress
_CmgVoipRemoteRtcpMonitorInetAddress_Object=MibScalar
cmgVoipRemoteRtcpMonitorInetAddress=_CmgVoipRemoteRtcpMonitorInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,3,2,6),_CmgVoipRemoteRtcpMonitorInetAddress_Type())
cmgVoipRemoteRtcpMonitorInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRtcpMonitorInetAddress.setStatus(_B)
class _CmgVoipRemoteRtcpMonitorPortInetAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmgVoipRemoteRtcpMonitorPortInetAddress_Type.__name__=_D
_CmgVoipRemoteRtcpMonitorPortInetAddress_Object=MibScalar
cmgVoipRemoteRtcpMonitorPortInetAddress=_CmgVoipRemoteRtcpMonitorPortInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,3,2,7),_CmgVoipRemoteRtcpMonitorPortInetAddress_Type())
cmgVoipRemoteRtcpMonitorPortInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRtcpMonitorPortInetAddress.setStatus(_B)
_CmgVoipRemoteRsvpParameters_ObjectIdentity=ObjectIdentity
cmgVoipRemoteRsvpParameters=_CmgVoipRemoteRsvpParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,3,3))
class _CmgVoipRemoteRsvpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgVoipRemoteRsvpEnabled_Type.__name__=_D
_CmgVoipRemoteRsvpEnabled_Object=MibScalar
cmgVoipRemoteRsvpEnabled=_CmgVoipRemoteRsvpEnabled_Object((1,3,6,1,4,1,6889,2,9,1,4,3,3,1),_CmgVoipRemoteRsvpEnabled_Type())
cmgVoipRemoteRsvpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRsvpEnabled.setStatus(_B)
class _CmgVoipRemoteRetryOnFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgVoipRemoteRetryOnFailure_Type.__name__=_D
_CmgVoipRemoteRetryOnFailure_Object=MibScalar
cmgVoipRemoteRetryOnFailure=_CmgVoipRemoteRetryOnFailure_Object((1,3,6,1,4,1,6889,2,9,1,4,3,3,2),_CmgVoipRemoteRetryOnFailure_Type())
cmgVoipRemoteRetryOnFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRetryOnFailure.setStatus(_B)
class _CmgVoipRemoteRetryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_CmgVoipRemoteRetryDelay_Type.__name__=_D
_CmgVoipRemoteRetryDelay_Object=MibScalar
cmgVoipRemoteRetryDelay=_CmgVoipRemoteRetryDelay_Object((1,3,6,1,4,1,6889,2,9,1,4,3,3,3),_CmgVoipRemoteRetryDelay_Type())
cmgVoipRemoteRetryDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRetryDelay.setStatus(_B)
class _CmgVoipRemoteRsvpProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AI,1),(_AJ,2)))
_CmgVoipRemoteRsvpProfile_Type.__name__=_D
_CmgVoipRemoteRsvpProfile_Object=MibScalar
cmgVoipRemoteRsvpProfile=_CmgVoipRemoteRsvpProfile_Object((1,3,6,1,4,1,6889,2,9,1,4,3,3,4),_CmgVoipRemoteRsvpProfile_Type())
cmgVoipRemoteRsvpProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipRemoteRsvpProfile.setStatus(_B)
_CmgVoipLocalParameters_ObjectIdentity=ObjectIdentity
cmgVoipLocalParameters=_CmgVoipLocalParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,4))
_CmgVoipLocalQosParameters_ObjectIdentity=ObjectIdentity
cmgVoipLocalQosParameters=_CmgVoipLocalQosParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,4,1))
class _CmgVoipLocalBbeDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CmgVoipLocalBbeDscp_Type.__name__=_D
_CmgVoipLocalBbeDscp_Object=MibScalar
cmgVoipLocalBbeDscp=_CmgVoipLocalBbeDscp_Object((1,3,6,1,4,1,6889,2,9,1,4,4,1,1),_CmgVoipLocalBbeDscp_Type())
cmgVoipLocalBbeDscp.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalBbeDscp.setStatus(_B)
class _CmgVoipLocalEfDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CmgVoipLocalEfDscp_Type.__name__=_D
_CmgVoipLocalEfDscp_Object=MibScalar
cmgVoipLocalEfDscp=_CmgVoipLocalEfDscp_Object((1,3,6,1,4,1,6889,2,9,1,4,4,1,2),_CmgVoipLocalEfDscp_Type())
cmgVoipLocalEfDscp.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalEfDscp.setStatus(_B)
class _CmgVoipLocal802Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CmgVoipLocal802Priority_Type.__name__=_D
_CmgVoipLocal802Priority_Object=MibScalar
cmgVoipLocal802Priority=_CmgVoipLocal802Priority_Object((1,3,6,1,4,1,6889,2,9,1,4,4,1,3),_CmgVoipLocal802Priority_Type())
cmgVoipLocal802Priority.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocal802Priority.setStatus(_B)
class _CmgVoipLocalMinRtpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65533))
_CmgVoipLocalMinRtpPort_Type.__name__=_D
_CmgVoipLocalMinRtpPort_Object=MibScalar
cmgVoipLocalMinRtpPort=_CmgVoipLocalMinRtpPort_Object((1,3,6,1,4,1,6889,2,9,1,4,4,1,4),_CmgVoipLocalMinRtpPort_Type())
cmgVoipLocalMinRtpPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalMinRtpPort.setStatus(_B)
class _CmgVoipLocalMaxRtpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65535))
_CmgVoipLocalMaxRtpPort_Type.__name__=_D
_CmgVoipLocalMaxRtpPort_Object=MibScalar
cmgVoipLocalMaxRtpPort=_CmgVoipLocalMaxRtpPort_Object((1,3,6,1,4,1,6889,2,9,1,4,4,1,5),_CmgVoipLocalMaxRtpPort_Type())
cmgVoipLocalMaxRtpPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalMaxRtpPort.setStatus(_B)
_CmgVoipLocalRtcpParameters_ObjectIdentity=ObjectIdentity
cmgVoipLocalRtcpParameters=_CmgVoipLocalRtcpParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,4,2))
class _CmgVoipLocalRtcpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgVoipLocalRtcpEnabled_Type.__name__=_D
_CmgVoipLocalRtcpEnabled_Object=MibScalar
cmgVoipLocalRtcpEnabled=_CmgVoipLocalRtcpEnabled_Object((1,3,6,1,4,1,6889,2,9,1,4,4,2,1),_CmgVoipLocalRtcpEnabled_Type())
cmgVoipLocalRtcpEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRtcpEnabled.setStatus(_B)
_CmgVoipLocalRtcpMonitorIpAddress_Type=IpAddress
_CmgVoipLocalRtcpMonitorIpAddress_Object=MibScalar
cmgVoipLocalRtcpMonitorIpAddress=_CmgVoipLocalRtcpMonitorIpAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,4,2,2),_CmgVoipLocalRtcpMonitorIpAddress_Type())
cmgVoipLocalRtcpMonitorIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRtcpMonitorIpAddress.setStatus(_B)
class _CmgVoipLocalRtcpMonitorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmgVoipLocalRtcpMonitorPort_Type.__name__=_D
_CmgVoipLocalRtcpMonitorPort_Object=MibScalar
cmgVoipLocalRtcpMonitorPort=_CmgVoipLocalRtcpMonitorPort_Object((1,3,6,1,4,1,6889,2,9,1,4,4,2,3),_CmgVoipLocalRtcpMonitorPort_Type())
cmgVoipLocalRtcpMonitorPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRtcpMonitorPort.setStatus(_B)
class _CmgVoipLocalRtcpReportPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_CmgVoipLocalRtcpReportPeriod_Type.__name__=_D
_CmgVoipLocalRtcpReportPeriod_Object=MibScalar
cmgVoipLocalRtcpReportPeriod=_CmgVoipLocalRtcpReportPeriod_Object((1,3,6,1,4,1,6889,2,9,1,4,4,2,4),_CmgVoipLocalRtcpReportPeriod_Type())
cmgVoipLocalRtcpReportPeriod.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRtcpReportPeriod.setStatus(_B)
_CmgVoipLocalRtcpMonitorInetAddressType_Type=InetAddressType
_CmgVoipLocalRtcpMonitorInetAddressType_Object=MibScalar
cmgVoipLocalRtcpMonitorInetAddressType=_CmgVoipLocalRtcpMonitorInetAddressType_Object((1,3,6,1,4,1,6889,2,9,1,4,4,2,5),_CmgVoipLocalRtcpMonitorInetAddressType_Type())
cmgVoipLocalRtcpMonitorInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipLocalRtcpMonitorInetAddressType.setStatus(_B)
_CmgVoipLocalRtcpMonitorInetAddress_Type=InetAddress
_CmgVoipLocalRtcpMonitorInetAddress_Object=MibScalar
cmgVoipLocalRtcpMonitorInetAddress=_CmgVoipLocalRtcpMonitorInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,4,2,6),_CmgVoipLocalRtcpMonitorInetAddress_Type())
cmgVoipLocalRtcpMonitorInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipLocalRtcpMonitorInetAddress.setStatus(_B)
class _CmgVoipLocalRtcpMonitorPortInetAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmgVoipLocalRtcpMonitorPortInetAddress_Type.__name__=_D
_CmgVoipLocalRtcpMonitorPortInetAddress_Object=MibScalar
cmgVoipLocalRtcpMonitorPortInetAddress=_CmgVoipLocalRtcpMonitorPortInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,4,2,7),_CmgVoipLocalRtcpMonitorPortInetAddress_Type())
cmgVoipLocalRtcpMonitorPortInetAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRtcpMonitorPortInetAddress.setStatus(_B)
_CmgVoipLocalRsvpParameters_ObjectIdentity=ObjectIdentity
cmgVoipLocalRsvpParameters=_CmgVoipLocalRsvpParameters_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,4,4,3))
class _CmgVoipLocalRsvpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgVoipLocalRsvpEnabled_Type.__name__=_D
_CmgVoipLocalRsvpEnabled_Object=MibScalar
cmgVoipLocalRsvpEnabled=_CmgVoipLocalRsvpEnabled_Object((1,3,6,1,4,1,6889,2,9,1,4,4,3,1),_CmgVoipLocalRsvpEnabled_Type())
cmgVoipLocalRsvpEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRsvpEnabled.setStatus(_B)
class _CmgVoipLocalRetryOnFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CmgVoipLocalRetryOnFailure_Type.__name__=_D
_CmgVoipLocalRetryOnFailure_Object=MibScalar
cmgVoipLocalRetryOnFailure=_CmgVoipLocalRetryOnFailure_Object((1,3,6,1,4,1,6889,2,9,1,4,4,3,2),_CmgVoipLocalRetryOnFailure_Type())
cmgVoipLocalRetryOnFailure.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRetryOnFailure.setStatus(_B)
class _CmgVoipLocalRetryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_CmgVoipLocalRetryDelay_Type.__name__=_D
_CmgVoipLocalRetryDelay_Object=MibScalar
cmgVoipLocalRetryDelay=_CmgVoipLocalRetryDelay_Object((1,3,6,1,4,1,6889,2,9,1,4,4,3,3),_CmgVoipLocalRetryDelay_Type())
cmgVoipLocalRetryDelay.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRetryDelay.setStatus(_B)
class _CmgVoipLocalRsvpProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AI,1),(_AJ,2)))
_CmgVoipLocalRsvpProfile_Type.__name__=_D
_CmgVoipLocalRsvpProfile_Object=MibScalar
cmgVoipLocalRsvpProfile=_CmgVoipLocalRsvpProfile_Object((1,3,6,1,4,1,6889,2,9,1,4,4,3,4),_CmgVoipLocalRsvpProfile_Type())
cmgVoipLocalRsvpProfile.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipLocalRsvpProfile.setStatus(_B)
_CmgVoipEngineTable_Object=MibTable
cmgVoipEngineTable=_CmgVoipEngineTable_Object((1,3,6,1,4,1,6889,2,9,1,4,5))
if mibBuilder.loadTexts:cmgVoipEngineTable.setStatus(_B)
_CmgVoipEngineEntry_Object=MibTableRow
cmgVoipEngineEntry=_CmgVoipEngineEntry_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1))
cmgVoipEngineEntry.setIndexNames((0,_A,_w))
if mibBuilder.loadTexts:cmgVoipEngineEntry.setStatus(_B)
class _CmgVoipSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,104))
_CmgVoipSlot_Type.__name__=_D
_CmgVoipSlot_Object=MibTableColumn
cmgVoipSlot=_CmgVoipSlot_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,1),_CmgVoipSlot_Type())
cmgVoipSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipSlot.setStatus(_B)
class _CmgVoipMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CmgVoipMACAddress_Type.__name__=_P
_CmgVoipMACAddress_Object=MibTableColumn
cmgVoipMACAddress=_CmgVoipMACAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,2),_CmgVoipMACAddress_Type())
cmgVoipMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipMACAddress.setStatus(_B)
_CmgVoipStaticIpAddress_Type=IpAddress
_CmgVoipStaticIpAddress_Object=MibTableColumn
cmgVoipStaticIpAddress=_CmgVoipStaticIpAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,3),_CmgVoipStaticIpAddress_Type())
cmgVoipStaticIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipStaticIpAddress.setStatus(_B)
_CmgVoipCurrentIpAddress_Type=IpAddress
_CmgVoipCurrentIpAddress_Object=MibTableColumn
cmgVoipCurrentIpAddress=_CmgVoipCurrentIpAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,4),_CmgVoipCurrentIpAddress_Type())
cmgVoipCurrentIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipCurrentIpAddress.setStatus(_B)
_CmgVoipJitterBufferSize_Type=Integer32
_CmgVoipJitterBufferSize_Object=MibTableColumn
cmgVoipJitterBufferSize=_CmgVoipJitterBufferSize_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,5),_CmgVoipJitterBufferSize_Type())
cmgVoipJitterBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipJitterBufferSize.setStatus(_B)
_CmgVoipTotalChannels_Type=Integer32
_CmgVoipTotalChannels_Object=MibTableColumn
cmgVoipTotalChannels=_CmgVoipTotalChannels_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,6),_CmgVoipTotalChannels_Type())
cmgVoipTotalChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipTotalChannels.setStatus(_B)
_CmgVoipChannelsInUse_Type=Integer32
_CmgVoipChannelsInUse_Object=MibTableColumn
cmgVoipChannelsInUse=_CmgVoipChannelsInUse_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,7),_CmgVoipChannelsInUse_Type())
cmgVoipChannelsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipChannelsInUse.setStatus(_B)
class _CmgVoipAverageOccupancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CmgVoipAverageOccupancy_Type.__name__=_D
_CmgVoipAverageOccupancy_Object=MibTableColumn
cmgVoipAverageOccupancy=_CmgVoipAverageOccupancy_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,8),_CmgVoipAverageOccupancy_Type())
cmgVoipAverageOccupancy.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipAverageOccupancy.setStatus(_B)
class _CmgVoipHyperactivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('normal',1),('hyperactive',2),(_k,255)))
_CmgVoipHyperactivity_Type.__name__=_D
_CmgVoipHyperactivity_Object=MibTableColumn
cmgVoipHyperactivity=_CmgVoipHyperactivity_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,9),_CmgVoipHyperactivity_Type())
cmgVoipHyperactivity.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipHyperactivity.setStatus(_B)
class _CmgVoipAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('busy-out',1),('release',2),('camp-on',3),(_k,255)))
_CmgVoipAdminState_Type.__name__=_D
_CmgVoipAdminState_Object=MibTableColumn
cmgVoipAdminState=_CmgVoipAdminState_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,10),_CmgVoipAdminState_Type())
cmgVoipAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipAdminState.setStatus(_B)
class _CmgVoipDspFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CmgVoipDspFWVersion_Type.__name__=_J
_CmgVoipDspFWVersion_Object=MibTableColumn
cmgVoipDspFWVersion=_CmgVoipDspFWVersion_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,11),_CmgVoipDspFWVersion_Type())
cmgVoipDspFWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipDspFWVersion.setStatus(_B)
class _CmgVoipDspStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('inUse',2),('fault',3)))
_CmgVoipDspStatus_Type.__name__=_D
_CmgVoipDspStatus_Object=MibTableColumn
cmgVoipDspStatus=_CmgVoipDspStatus_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,12),_CmgVoipDspStatus_Type())
cmgVoipDspStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipDspStatus.setStatus(_B)
class _CmgVoipEngineReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgVoipEngineReset_Type.__name__=_D
_CmgVoipEngineReset_Object=MibTableColumn
cmgVoipEngineReset=_CmgVoipEngineReset_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,13),_CmgVoipEngineReset_Type())
cmgVoipEngineReset.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipEngineReset.setStatus(_B)
class _CmgVoipFaultMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CmgVoipFaultMask_Type.__name__=_P
_CmgVoipFaultMask_Object=MibTableColumn
cmgVoipFaultMask=_CmgVoipFaultMask_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,14),_CmgVoipFaultMask_Type())
cmgVoipFaultMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipFaultMask.setStatus(_B)
_CmgVoipStaticInetAddressType_Type=InetAddressType
_CmgVoipStaticInetAddressType_Object=MibTableColumn
cmgVoipStaticInetAddressType=_CmgVoipStaticInetAddressType_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,15),_CmgVoipStaticInetAddressType_Type())
cmgVoipStaticInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipStaticInetAddressType.setStatus(_B)
_CmgVoipStaticInetAddress_Type=InetAddress
_CmgVoipStaticInetAddress_Object=MibTableColumn
cmgVoipStaticInetAddress=_CmgVoipStaticInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,16),_CmgVoipStaticInetAddress_Type())
cmgVoipStaticInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipStaticInetAddress.setStatus(_B)
_CmgVoipCurrentInetAddressType_Type=InetAddressType
_CmgVoipCurrentInetAddressType_Object=MibTableColumn
cmgVoipCurrentInetAddressType=_CmgVoipCurrentInetAddressType_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,17),_CmgVoipCurrentInetAddressType_Type())
cmgVoipCurrentInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipCurrentInetAddressType.setStatus(_B)
_CmgVoipCurrentInetAddress_Type=InetAddress
_CmgVoipCurrentInetAddress_Object=MibTableColumn
cmgVoipCurrentInetAddress=_CmgVoipCurrentInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,4,5,1,18),_CmgVoipCurrentInetAddress_Type())
cmgVoipCurrentInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipCurrentInetAddress.setStatus(_B)
_CmgVoipDSPCoreTable_Object=MibTable
cmgVoipDSPCoreTable=_CmgVoipDSPCoreTable_Object((1,3,6,1,4,1,6889,2,9,1,4,6))
if mibBuilder.loadTexts:cmgVoipDSPCoreTable.setStatus(_B)
_CmgVoipDSPCoreEntry_Object=MibTableRow
cmgVoipDSPCoreEntry=_CmgVoipDSPCoreEntry_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1))
cmgVoipDSPCoreEntry.setIndexNames((0,_A,_w),(0,_A,_AK))
if mibBuilder.loadTexts:cmgVoipDSPCoreEntry.setStatus(_B)
class _CmgDSPCoreCoreId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CmgDSPCoreCoreId_Type.__name__=_D
_CmgDSPCoreCoreId_Object=MibTableColumn
cmgDSPCoreCoreId=_CmgDSPCoreCoreId_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1,1),_CmgDSPCoreCoreId_Type())
cmgDSPCoreCoreId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDSPCoreCoreId.setStatus(_B)
class _CmgDSPCoreTotalChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CmgDSPCoreTotalChannels_Type.__name__=_D
_CmgDSPCoreTotalChannels_Object=MibTableColumn
cmgDSPCoreTotalChannels=_CmgDSPCoreTotalChannels_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1,2),_CmgDSPCoreTotalChannels_Type())
cmgDSPCoreTotalChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDSPCoreTotalChannels.setStatus(_B)
class _CmgDSPCoreChannelsInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CmgDSPCoreChannelsInUse_Type.__name__=_D
_CmgDSPCoreChannelsInUse_Object=MibTableColumn
cmgDSPCoreChannelsInUse=_CmgDSPCoreChannelsInUse_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1,3),_CmgDSPCoreChannelsInUse_Type())
cmgDSPCoreChannelsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDSPCoreChannelsInUse.setStatus(_B)
class _CmgDSPCoreAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('busy-out',1),('release',2),('camp-on',3),(_k,255)))
_CmgDSPCoreAdminState_Type.__name__=_D
_CmgDSPCoreAdminState_Object=MibTableColumn
cmgDSPCoreAdminState=_CmgDSPCoreAdminState_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1,4),_CmgDSPCoreAdminState_Type())
cmgDSPCoreAdminState.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDSPCoreAdminState.setStatus(_B)
class _CmgDSPCoreStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('inUse',2),('fault',3)))
_CmgDSPCoreStatus_Type.__name__=_D
_CmgDSPCoreStatus_Object=MibTableColumn
cmgDSPCoreStatus=_CmgDSPCoreStatus_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1,5),_CmgDSPCoreStatus_Type())
cmgDSPCoreStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDSPCoreStatus.setStatus(_B)
class _CmgDSPCoreDemandTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgDSPCoreDemandTest_Type.__name__=_D
_CmgDSPCoreDemandTest_Object=MibTableColumn
cmgDSPCoreDemandTest=_CmgDSPCoreDemandTest_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1,6),_CmgDSPCoreDemandTest_Type())
cmgDSPCoreDemandTest.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgDSPCoreDemandTest.setStatus(_B)
class _CmgDSPCoreDemandTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*(('errorCode1',1),('errorCode2',2),('errorCode3',3),('errorCode4',4),('errorCode5',5),('errorCode6',6),('notResponding',7),('pass',255)))
_CmgDSPCoreDemandTestResult_Type.__name__=_D
_CmgDSPCoreDemandTestResult_Object=MibTableColumn
cmgDSPCoreDemandTestResult=_CmgDSPCoreDemandTestResult_Object((1,3,6,1,4,1,6889,2,9,1,4,6,1,7),_CmgDSPCoreDemandTestResult_Type())
cmgDSPCoreDemandTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDSPCoreDemandTestResult.setStatus(_B)
class _CmgVoipEchoCancellerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_n,0),(_N,1),(_M,2),('fixedOn',3)))
_CmgVoipEchoCancellerControl_Type.__name__=_D
_CmgVoipEchoCancellerControl_Object=MibScalar
cmgVoipEchoCancellerControl=_CmgVoipEchoCancellerControl_Object((1,3,6,1,4,1,6889,2,9,1,4,7),_CmgVoipEchoCancellerControl_Type())
cmgVoipEchoCancellerControl.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipEchoCancellerControl.setStatus(_B)
class _CmgVoipEchoCancellerConfig1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CmgVoipEchoCancellerConfig1_Type.__name__=_D
_CmgVoipEchoCancellerConfig1_Object=MibScalar
cmgVoipEchoCancellerConfig1=_CmgVoipEchoCancellerConfig1_Object((1,3,6,1,4,1,6889,2,9,1,4,8),_CmgVoipEchoCancellerConfig1_Type())
cmgVoipEchoCancellerConfig1.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipEchoCancellerConfig1.setStatus(_B)
class _CmgVoipEchoCancellerConfig2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CmgVoipEchoCancellerConfig2_Type.__name__=_D
_CmgVoipEchoCancellerConfig2_Object=MibScalar
cmgVoipEchoCancellerConfig2=_CmgVoipEchoCancellerConfig2_Object((1,3,6,1,4,1,6889,2,9,1,4,9),_CmgVoipEchoCancellerConfig2_Type())
cmgVoipEchoCancellerConfig2.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgVoipEchoCancellerConfig2.setStatus(_B)
_CmgVoipTotalChannelsEnforcedByCM_Type=Integer32
_CmgVoipTotalChannelsEnforcedByCM_Object=MibScalar
cmgVoipTotalChannelsEnforcedByCM=_CmgVoipTotalChannelsEnforcedByCM_Object((1,3,6,1,4,1,6889,2,9,1,4,10),_CmgVoipTotalChannelsEnforcedByCM_Type())
cmgVoipTotalChannelsEnforcedByCM.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgVoipTotalChannelsEnforcedByCM.setStatus(_B)
_CmgTraps_ObjectIdentity=ObjectIdentity
cmgTraps=_CmgTraps_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,5))
_CmgTrapManagerTable_Object=MibTable
cmgTrapManagerTable=_CmgTrapManagerTable_Object((1,3,6,1,4,1,6889,2,9,1,5,1))
if mibBuilder.loadTexts:cmgTrapManagerTable.setStatus(_B)
_CmgTrapManagerEntry_Object=MibTableRow
cmgTrapManagerEntry=_CmgTrapManagerEntry_Object((1,3,6,1,4,1,6889,2,9,1,5,1,1))
cmgTrapManagerEntry.setIndexNames((0,_A,_AL))
if mibBuilder.loadTexts:cmgTrapManagerEntry.setStatus(_B)
_CmgTrapManagerAddress_Type=IpAddress
_CmgTrapManagerAddress_Object=MibTableColumn
cmgTrapManagerAddress=_CmgTrapManagerAddress_Object((1,3,6,1,4,1,6889,2,9,1,5,1,1,1),_CmgTrapManagerAddress_Type())
cmgTrapManagerAddress.setMaxAccess(_p)
if mibBuilder.loadTexts:cmgTrapManagerAddress.setStatus(_B)
class _CmgTrapManagerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_b,2)))
_CmgTrapManagerControl_Type.__name__=_D
_CmgTrapManagerControl_Object=MibTableColumn
cmgTrapManagerControl=_CmgTrapManagerControl_Object((1,3,6,1,4,1,6889,2,9,1,5,1,1,3),_CmgTrapManagerControl_Type())
cmgTrapManagerControl.setMaxAccess(_p)
if mibBuilder.loadTexts:cmgTrapManagerControl.setStatus(_B)
_CmgTrapManagerMask_Type=Integer32
_CmgTrapManagerMask_Object=MibTableColumn
cmgTrapManagerMask=_CmgTrapManagerMask_Object((1,3,6,1,4,1,6889,2,9,1,5,1,1,4),_CmgTrapManagerMask_Type())
cmgTrapManagerMask.setMaxAccess(_p)
if mibBuilder.loadTexts:cmgTrapManagerMask.setStatus(_B)
_CmgTrapManagerRowStatus_Type=RowStatus
_CmgTrapManagerRowStatus_Object=MibTableColumn
cmgTrapManagerRowStatus=_CmgTrapManagerRowStatus_Object((1,3,6,1,4,1,6889,2,9,1,5,1,1,5),_CmgTrapManagerRowStatus_Type())
cmgTrapManagerRowStatus.setMaxAccess(_p)
if mibBuilder.loadTexts:cmgTrapManagerRowStatus.setStatus(_B)
_CmgTrapDefinitions_ObjectIdentity=ObjectIdentity
cmgTrapDefinitions=_CmgTrapDefinitions_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,5,2))
_CmgTrapVariables_ObjectIdentity=ObjectIdentity
cmgTrapVariables=_CmgTrapVariables_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,5,2,1))
class _CmgTrapLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CmgTrapLocation_Type.__name__=_J
_CmgTrapLocation_Object=MibScalar
cmgTrapLocation=_CmgTrapLocation_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,1),_CmgTrapLocation_Type())
cmgTrapLocation.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgTrapLocation.setStatus(_B)
class _CmgTrapOnBoard_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CmgTrapOnBoard_Type.__name__=_J
_CmgTrapOnBoard_Object=MibScalar
cmgTrapOnBoard=_CmgTrapOnBoard_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,2),_CmgTrapOnBoard_Type())
cmgTrapOnBoard.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgTrapOnBoard.setStatus(_B)
class _CmgTrapSubsystem_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CmgTrapSubsystem_Type.__name__=_J
_CmgTrapSubsystem_Object=MibScalar
cmgTrapSubsystem=_CmgTrapSubsystem_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,3),_CmgTrapSubsystem_Type())
cmgTrapSubsystem.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgTrapSubsystem.setStatus(_B)
class _CmgTrapOnIccMissing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_CmgTrapOnIccMissing_Type.__name__=_D
_CmgTrapOnIccMissing_Object=MibScalar
cmgTrapOnIccMissing=_CmgTrapOnIccMissing_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,4),_CmgTrapOnIccMissing_Type())
cmgTrapOnIccMissing.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgTrapOnIccMissing.setStatus(_B)
class _CmgTrapModule_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmgTrapModule_Type.__name__=_J
_CmgTrapModule_Object=MibScalar
cmgTrapModule=_CmgTrapModule_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,5),_CmgTrapModule_Type())
cmgTrapModule.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgTrapModule.setStatus(_B)
_CmgTrapSeverity_Type=CmgItuPerceivedSeverity
_CmgTrapSeverity_Object=MibScalar
cmgTrapSeverity=_CmgTrapSeverity_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,6),_CmgTrapSeverity_Type())
cmgTrapSeverity.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgTrapSeverity.setStatus(_B)
class _CmgProductId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CmgProductId_Type.__name__=_J
_CmgProductId_Object=MibScalar
cmgProductId=_CmgProductId_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,7),_CmgProductId_Type())
cmgProductId.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgProductId.setStatus(_B)
_CmgTrapAvailableTimeslots_Type=Integer32
_CmgTrapAvailableTimeslots_Object=MibScalar
cmgTrapAvailableTimeslots=_CmgTrapAvailableTimeslots_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,8),_CmgTrapAvailableTimeslots_Type())
cmgTrapAvailableTimeslots.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgTrapAvailableTimeslots.setStatus(_B)
_CmgTrapInUseTimeslots_Type=Integer32
_CmgTrapInUseTimeslots_Object=MibScalar
cmgTrapInUseTimeslots=_CmgTrapInUseTimeslots_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,9),_CmgTrapInUseTimeslots_Type())
cmgTrapInUseTimeslots.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgTrapInUseTimeslots.setStatus(_B)
class _CmgFipsErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cryptoTestError',1),('prngFailure',2),('hashIntegrity',3)))
_CmgFipsErrorType_Type.__name__=_D
_CmgFipsErrorType_Object=MibScalar
cmgFipsErrorType=_CmgFipsErrorType_Object((1,3,6,1,4,1,6889,2,9,1,5,2,1,10),_CmgFipsErrorType_Type())
cmgFipsErrorType.setMaxAccess(_U)
if mibBuilder.loadTexts:cmgFipsErrorType.setStatus(_B)
_CmgTrapTypes_ObjectIdentity=ObjectIdentity
cmgTrapTypes=_CmgTrapTypes_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,5,2,2))
_CmgTrapV3separator_ObjectIdentity=ObjectIdentity
cmgTrapV3separator=_CmgTrapV3separator_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,5,2,2,0))
_CmgContactClosures_ObjectIdentity=ObjectIdentity
cmgContactClosures=_CmgContactClosures_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,6))
_CmgContactClosuresTable_Object=MibTable
cmgContactClosuresTable=_CmgContactClosuresTable_Object((1,3,6,1,4,1,6889,2,9,1,6,1))
if mibBuilder.loadTexts:cmgContactClosuresTable.setStatus(_B)
_CmgContactClosuresEntry_Object=MibTableRow
cmgContactClosuresEntry=_CmgContactClosuresEntry_Object((1,3,6,1,4,1,6889,2,9,1,6,1,1))
cmgContactClosuresEntry.setIndexNames((0,_A,_AM),(0,_A,_AN),(0,_A,_AO))
if mibBuilder.loadTexts:cmgContactClosuresEntry.setStatus(_B)
class _CmgCcModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10))
_CmgCcModule_Type.__name__=_D
_CmgCcModule_Object=MibTableColumn
cmgCcModule=_CmgCcModule_Object((1,3,6,1,4,1,6889,2,9,1,6,1,1,1),_CmgCcModule_Type())
cmgCcModule.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCcModule.setStatus(_B)
class _CmgCcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CmgCcPort_Type.__name__=_D
_CmgCcPort_Object=MibTableColumn
cmgCcPort=_CmgCcPort_Object((1,3,6,1,4,1,6889,2,9,1,6,1,1,2),_CmgCcPort_Type())
cmgCcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCcPort.setStatus(_B)
class _CmgCcRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CmgCcRelay_Type.__name__=_D
_CmgCcRelay_Object=MibTableColumn
cmgCcRelay=_CmgCcRelay_Object((1,3,6,1,4,1,6889,2,9,1,6,1,1,3),_CmgCcRelay_Type())
cmgCcRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCcRelay.setStatus(_B)
class _CmgCcAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),('manualTrigger',2),('manualOff',3)))
_CmgCcAdminState_Type.__name__=_D
_CmgCcAdminState_Object=MibTableColumn
cmgCcAdminState=_CmgCcAdminState_Object((1,3,6,1,4,1,6889,2,9,1,6,1,1,4),_CmgCcAdminState_Type())
cmgCcAdminState.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgCcAdminState.setStatus(_B)
class _CmgCcPulseDuration_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CmgCcPulseDuration_Type.__name__=_D
_CmgCcPulseDuration_Object=MibTableColumn
cmgCcPulseDuration=_CmgCcPulseDuration_Object((1,3,6,1,4,1,6889,2,9,1,6,1,1,5),_CmgCcPulseDuration_Type())
cmgCcPulseDuration.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgCcPulseDuration.setStatus(_B)
class _CmgCcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('triggered',1),(_M,2)))
_CmgCcStatus_Type.__name__=_D
_CmgCcStatus_Object=MibTableColumn
cmgCcStatus=_CmgCcStatus_Object((1,3,6,1,4,1,6889,2,9,1,6,1,1,6),_CmgCcStatus_Type())
cmgCcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgCcStatus.setStatus(_B)
_CmgETR_ObjectIdentity=ObjectIdentity
cmgETR=_CmgETR_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,7))
_CmgETRTable_Object=MibTable
cmgETRTable=_CmgETRTable_Object((1,3,6,1,4,1,6889,2,9,1,7,1))
if mibBuilder.loadTexts:cmgETRTable.setStatus(_B)
_CmgETREntry_Object=MibTableRow
cmgETREntry=_CmgETREntry_Object((1,3,6,1,4,1,6889,2,9,1,7,1,1))
cmgETREntry.setIndexNames((0,_A,_AP))
if mibBuilder.loadTexts:cmgETREntry.setStatus(_B)
class _CmgEtrModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CmgEtrModule_Type.__name__=_D
_CmgEtrModule_Object=MibTableColumn
cmgEtrModule=_CmgEtrModule_Object((1,3,6,1,4,1,6889,2,9,1,7,1,1,1),_CmgEtrModule_Type())
cmgEtrModule.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgEtrModule.setStatus(_B)
class _CmgEtrAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_N,2),(_M,3)))
_CmgEtrAdminState_Type.__name__=_D
_CmgEtrAdminState_Object=MibTableColumn
cmgEtrAdminState=_CmgEtrAdminState_Object((1,3,6,1,4,1,6889,2,9,1,7,1,1,2),_CmgEtrAdminState_Type())
cmgEtrAdminState.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgEtrAdminState.setStatus(_B)
class _CmgEtrNumberOfPairs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CmgEtrNumberOfPairs_Type.__name__=_D
_CmgEtrNumberOfPairs_Object=MibTableColumn
cmgEtrNumberOfPairs=_CmgEtrNumberOfPairs_Object((1,3,6,1,4,1,6889,2,9,1,7,1,1,3),_CmgEtrNumberOfPairs_Type())
cmgEtrNumberOfPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgEtrNumberOfPairs.setStatus(_B)
class _CmgEtrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_CmgEtrStatus_Type.__name__=_D
_CmgEtrStatus_Object=MibTableColumn
cmgEtrStatus=_CmgEtrStatus_Object((1,3,6,1,4,1,6889,2,9,1,7,1,1,4),_CmgEtrStatus_Type())
cmgEtrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgEtrStatus.setStatus(_B)
class _CmgEtrCurrentLoopDetect_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CmgEtrCurrentLoopDetect_Type.__name__=_P
_CmgEtrCurrentLoopDetect_Object=MibTableColumn
cmgEtrCurrentLoopDetect=_CmgEtrCurrentLoopDetect_Object((1,3,6,1,4,1,6889,2,9,1,7,1,1,5),_CmgEtrCurrentLoopDetect_Type())
cmgEtrCurrentLoopDetect.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgEtrCurrentLoopDetect.setStatus(_B)
_CmgDynamicCAC_ObjectIdentity=ObjectIdentity
cmgDynamicCAC=_CmgDynamicCAC_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,8))
class _CmgDynCacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_W,1),('notConfigured',2),('notArmed',3),('armedNotConfigured',4),(_AG,255)))
_CmgDynCacStatus_Type.__name__=_D
_CmgDynCacStatus_Object=MibScalar
cmgDynCacStatus=_CmgDynCacStatus_Object((1,3,6,1,4,1,6889,2,9,1,8,1),_CmgDynCacStatus_Type())
cmgDynCacStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDynCacStatus.setStatus(_B)
_CmgDynCacRBBL_Type=Integer32
_CmgDynCacRBBL_Object=MibScalar
cmgDynCacRBBL=_CmgDynCacRBBL_Object((1,3,6,1,4,1,6889,2,9,1,8,2),_CmgDynCacRBBL_Type())
cmgDynCacRBBL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDynCacRBBL.setStatus(_B)
_CmgDynCacLastUpdate_Type=TimeTicks
_CmgDynCacLastUpdate_Object=MibScalar
cmgDynCacLastUpdate=_CmgDynCacLastUpdate_Object((1,3,6,1,4,1,6889,2,9,1,8,3),_CmgDynCacLastUpdate_Type())
cmgDynCacLastUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgDynCacLastUpdate.setStatus(_B)
_CmgSLAMonitor_ObjectIdentity=ObjectIdentity
cmgSLAMonitor=_CmgSLAMonitor_ObjectIdentity((1,3,6,1,4,1,6889,2,9,1,9))
class _CmgSLAMonitorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_Q,1)))
_CmgSLAMonitorState_Type.__name__=_D
_CmgSLAMonitorState_Object=MibScalar
cmgSLAMonitorState=_CmgSLAMonitorState_Object((1,3,6,1,4,1,6889,2,9,1,9,1),_CmgSLAMonitorState_Type())
cmgSLAMonitorState.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgSLAMonitorState.setStatus(_B)
_CmgSLAMonitorServerInetAddressType_Type=InetAddressType
_CmgSLAMonitorServerInetAddressType_Object=MibScalar
cmgSLAMonitorServerInetAddressType=_CmgSLAMonitorServerInetAddressType_Object((1,3,6,1,4,1,6889,2,9,1,9,2),_CmgSLAMonitorServerInetAddressType_Type())
cmgSLAMonitorServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgSLAMonitorServerInetAddressType.setStatus(_B)
_CmgSLAMonitorServerInetAddress_Type=InetAddress
_CmgSLAMonitorServerInetAddress_Object=MibScalar
cmgSLAMonitorServerInetAddress=_CmgSLAMonitorServerInetAddress_Object((1,3,6,1,4,1,6889,2,9,1,9,3),_CmgSLAMonitorServerInetAddress_Type())
cmgSLAMonitorServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgSLAMonitorServerInetAddress.setStatus(_B)
class _CmgSLAMonitorServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmgSLAMonitorServerPort_Type.__name__=_D
_CmgSLAMonitorServerPort_Object=MibScalar
cmgSLAMonitorServerPort=_CmgSLAMonitorServerPort_Object((1,3,6,1,4,1,6889,2,9,1,9,4),_CmgSLAMonitorServerPort_Type())
cmgSLAMonitorServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgSLAMonitorServerPort.setStatus(_B)
class _CmgSLAMonitorPacketCaptureMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('withoutPayload',1),('all',2)))
_CmgSLAMonitorPacketCaptureMode_Type.__name__=_D
_CmgSLAMonitorPacketCaptureMode_Object=MibScalar
cmgSLAMonitorPacketCaptureMode=_CmgSLAMonitorPacketCaptureMode_Object((1,3,6,1,4,1,6889,2,9,1,9,10),_CmgSLAMonitorPacketCaptureMode_Type())
cmgSLAMonitorPacketCaptureMode.setMaxAccess(_H)
if mibBuilder.loadTexts:cmgSLAMonitorPacketCaptureMode.setStatus(_B)
class _CmgSLAMonitorVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmgSLAMonitorVersion_Type.__name__=_J
_CmgSLAMonitorVersion_Object=MibScalar
cmgSLAMonitorVersion=_CmgSLAMonitorVersion_Object((1,3,6,1,4,1,6889,2,9,1,9,99),_CmgSLAMonitorVersion_Type())
cmgSLAMonitorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgSLAMonitorVersion.setStatus(_B)
cmgMultipleFanFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,2))
cmgMultipleFanFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgMultipleFanFault.setStatus(_B)
cmgMultipleFanClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,3))
cmgMultipleFanClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgMultipleFanClear.setStatus(_B)
cmgPsuFanBriefFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,4))
cmgPsuFanBriefFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgPsuFanBriefFault.setStatus(_B)
cmgPsuFanBriefClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,5))
cmgPsuFanBriefClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgPsuFanBriefClear.setStatus(_B)
cmgPsuFanProlongedFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,6))
cmgPsuFanProlongedFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgPsuFanProlongedFault.setStatus(_B)
cmgPsuFanProlongedClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,7))
cmgPsuFanProlongedClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgPsuFanProlongedClear.setStatus(_B)
cmgCpuTempWarningFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,10))
cmgCpuTempWarningFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_q),(_A,_x),(_A,_r)))
if mibBuilder.loadTexts:cmgCpuTempWarningFault.setStatus(_B)
cmgCpuTempWarningClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,11))
cmgCpuTempWarningClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_q),(_A,_x),(_A,_r)))
if mibBuilder.loadTexts:cmgCpuTempWarningClear.setStatus(_B)
cmgDspTempWarningFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,12))
cmgDspTempWarningFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_s),(_A,_y),(_A,_t)))
if mibBuilder.loadTexts:cmgDspTempWarningFault.setStatus(_B)
cmgDspTempWarningClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,13))
cmgDspTempWarningClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_s),(_A,_y),(_A,_t)))
if mibBuilder.loadTexts:cmgDspTempWarningClear.setStatus(_B)
cmgTempShutdownFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,14))
cmgTempShutdownFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:cmgTempShutdownFault.setStatus(_B)
cmgMgpPowerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,16))
cmgMgpPowerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_z)))
if mibBuilder.loadTexts:cmgMgpPowerFault.setStatus(_B)
cmgMgpPowerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,17))
cmgMgpPowerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_z)))
if mibBuilder.loadTexts:cmgMgpPowerClear.setStatus(_B)
cmgMediaModulePowerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,18))
cmgMediaModulePowerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A0)))
if mibBuilder.loadTexts:cmgMediaModulePowerFault.setStatus(_B)
cmgMediaModulePowerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,19))
cmgMediaModulePowerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A0)))
if mibBuilder.loadTexts:cmgMediaModulePowerClear.setStatus(_B)
cmgVoipPowerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,20))
cmgVoipPowerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A1)))
if mibBuilder.loadTexts:cmgVoipPowerFault.setStatus(_B)
cmgVoipPowerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,21))
cmgVoipPowerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A1)))
if mibBuilder.loadTexts:cmgVoipPowerClear.setStatus(_B)
cmgDspPowerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,22))
cmgDspPowerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A2)))
if mibBuilder.loadTexts:cmgDspPowerFault.setStatus(_B)
cmgDspPowerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,23))
cmgDspPowerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A2)))
if mibBuilder.loadTexts:cmgDspPowerClear.setStatus(_B)
cmg8260PowerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,24))
cmg8260PowerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A3)))
if mibBuilder.loadTexts:cmg8260PowerFault.setStatus(_B)
cmg8260PowerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,25))
cmg8260PowerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_A3)))
if mibBuilder.loadTexts:cmg8260PowerClear.setStatus(_B)
cmgAuxPowerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,26))
cmgAuxPowerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgAuxPowerFault.setStatus(_B)
cmgAuxPowerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,27))
cmgAuxPowerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgAuxPowerClear.setStatus(_B)
cmgFanPowerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,28))
cmgFanPowerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgFanPowerFault.setStatus(_B)
cmgFanPowerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,29))
cmgFanPowerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:cmgFanPowerClear.setStatus(_B)
cmgSyncSignalFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,30))
cmgSyncSignalFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cmgSyncSignalFault.setStatus(_B)
cmgSyncSignalClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,31))
cmgSyncSignalClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cmgSyncSignalClear.setStatus(_B)
cmgVoipHardwareFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,32))
cmgVoipHardwareFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:cmgVoipHardwareFault.setStatus(_B)
cmgVoipHardwareClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,33))
cmgVoipHardwareClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:cmgVoipHardwareClear.setStatus(_B)
cmgSyncSignalWarn=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,34))
cmgSyncSignalWarn.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cmgSyncSignalWarn.setStatus(_B)
cmgSyncWarnClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,35))
cmgSyncWarnClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cmgSyncWarnClear.setStatus(_B)
cmgSyncSignalExcess=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,36))
cmgSyncSignalExcess.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cmgSyncSignalExcess.setStatus(_B)
cmgSyncExcessClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,37))
cmgSyncExcessClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cmgSyncExcessClear.setStatus(_B)
cmgVoipCoreFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,38))
cmgVoipCoreFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:cmgVoipCoreFault.setStatus(_B)
cmgVoipCoreClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,39))
cmgVoipCoreClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:cmgVoipCoreClear.setStatus(_B)
cmgModuleRemove=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,50))
cmgModuleRemove.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_a)))
if mibBuilder.loadTexts:cmgModuleRemove.setStatus(_B)
cmgModuleInsertFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,52))
cmgModuleInsertFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_V),(_A,_a)))
if mibBuilder.loadTexts:cmgModuleInsertFault.setStatus(_B)
cmgModuleInsertSuccess=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,53))
cmgModuleInsertSuccess.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_a)))
if mibBuilder.loadTexts:cmgModuleInsertSuccess.setStatus(_B)
cmgMgBusyout=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,54))
cmgMgBusyout.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgMgBusyout.setStatus(_B)
cmgMgRelease=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,55))
cmgMgRelease.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgMgRelease.setStatus(_B)
cmgUnsupportedMmEnrolement=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,56))
cmgUnsupportedMmEnrolement.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_j),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cmgUnsupportedMmEnrolement.setStatus(_B)
cmgDataModuleAwohConflict=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,57))
cmgDataModuleAwohConflict.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_j),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cmgDataModuleAwohConflict.setStatus(_B)
cmgFirmwareDownloadBegun=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,70))
cmgFirmwareDownloadBegun.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_O,_c),(_O,_d),(_O,_e),(_A,_u),(_A,_T)))
if mibBuilder.loadTexts:cmgFirmwareDownloadBegun.setStatus(_B)
cmgFirmwareDownloadSuccess=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,71))
cmgFirmwareDownloadSuccess.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_O,_c),(_O,_d),(_O,_e)))
if mibBuilder.loadTexts:cmgFirmwareDownloadSuccess.setStatus(_B)
cmgRegistrationSuccess=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,73))
cmgRegistrationSuccess.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_A6)))
if mibBuilder.loadTexts:cmgRegistrationSuccess.setStatus(_B)
cmgMgManualReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,74))
cmgMgManualReset.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgMgManualReset.setStatus(_B)
cmgModuleManualReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,75))
cmgModuleManualReset.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgModuleManualReset.setStatus(_B)
cmgVoipManualReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,76))
cmgVoipManualReset.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgVoipManualReset.setStatus(_B)
cmgDsuManualReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,77))
cmgDsuManualReset.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuManualReset.setStatus(_I)
cmgConfigUploadBegun=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,78))
cmgConfigUploadBegun.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgConfigUploadBegun.setStatus(_B)
cmgConfigUploadSuccess=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,79))
cmgConfigUploadSuccess.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgConfigUploadSuccess.setStatus(_B)
cmgMemoryFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,90))
cmgMemoryFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgMemoryFault.setStatus(_B)
cmgMemoryClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,91))
cmgMemoryClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgMemoryClear.setStatus(_B)
cmgDhcpRequestFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,92))
cmgDhcpRequestFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgDhcpRequestFault.setStatus(_B)
cmgDhcpRequestClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,93))
cmgDhcpRequestClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgDhcpRequestClear.setStatus(_B)
cmgFirmwareDownloadFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,94))
cmgFirmwareDownloadFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_O,_c),(_O,_d),(_O,_e),(_O,_i)))
if mibBuilder.loadTexts:cmgFirmwareDownloadFault.setStatus(_B)
cmgProcessRestart=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,96))
cmgProcessRestart.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgProcessRestart.setStatus(_B)
cmgProcessRestartClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,97))
cmgProcessRestartClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgProcessRestartClear.setStatus(_B)
cmgIccMissingFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,98))
cmgIccMissingFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgIccMissingFault.setStatus(_B)
cmgIccMissingClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,99))
cmgIccMissingClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgIccMissingClear.setStatus(_B)
cmgIccAutoReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,100))
cmgIccAutoReset.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgIccAutoReset.setStatus(_B)
cmgIccAutoResetClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,101))
cmgIccAutoResetClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgIccAutoResetClear.setStatus(_B)
cmgPrimaryControllerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,102))
cmgPrimaryControllerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_A,_f)))
if mibBuilder.loadTexts:cmgPrimaryControllerFault.setStatus(_B)
cmgPrimaryControllerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,103))
cmgPrimaryControllerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_A,_f)))
if mibBuilder.loadTexts:cmgPrimaryControllerClear.setStatus(_B)
cmgNoControllerFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,104))
cmgNoControllerFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_A,_f)))
if mibBuilder.loadTexts:cmgNoControllerFault.setStatus(_B)
cmgNoControllerClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,105))
cmgNoControllerClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_A,_f)))
if mibBuilder.loadTexts:cmgNoControllerClear.setStatus(_B)
cmgRegistrationFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,106))
cmgRegistrationFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_A,_A6)))
if mibBuilder.loadTexts:cmgRegistrationFault.setStatus(_B)
cmgH248LinkDown=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,108))
cmgH248LinkDown.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgH248LinkDown.setStatus(_B)
cmgH248LinkUp=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,109))
cmgH248LinkUp.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgH248LinkUp.setStatus(_B)
cmgTestFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,110))
cmgTestFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgTestFault.setStatus(_B)
cmgTestClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,111))
cmgTestClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgTestClear.setStatus(_B)
cmgTestThresholdFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,112))
cmgTestThresholdFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgTestThresholdFault.setStatus(_B)
cmgTestThresholdClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,113))
cmgTestThresholdClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgTestThresholdClear.setStatus(_B)
cmgMgAutoReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,114))
cmgMgAutoReset.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:cmgMgAutoReset.setStatus(_B)
cmgModuleAutoReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,116))
cmgModuleAutoReset.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_V)))
if mibBuilder.loadTexts:cmgModuleAutoReset.setStatus(_B)
cmgModuleAutoResetClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,117))
cmgModuleAutoResetClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_V)))
if mibBuilder.loadTexts:cmgModuleAutoResetClear.setStatus(_B)
cmgModulePostFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,118))
cmgModulePostFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_V)))
if mibBuilder.loadTexts:cmgModulePostFault.setStatus(_B)
cmgModulePostClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,119))
cmgModulePostClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_V)))
if mibBuilder.loadTexts:cmgModulePostClear.setStatus(_B)
cmgModuleParameterFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,120))
cmgModuleParameterFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_V)))
if mibBuilder.loadTexts:cmgModuleParameterFault.setStatus(_B)
cmgModuleParameterClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,121))
cmgModuleParameterClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_V)))
if mibBuilder.loadTexts:cmgModuleParameterClear.setStatus(_B)
cmgConfigUploadFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,122))
cmgConfigUploadFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_O,_i)))
if mibBuilder.loadTexts:cmgConfigUploadFault.setStatus(_B)
cmgVoipOccFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,124))
cmgVoipOccFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:cmgVoipOccFault.setStatus(_B)
cmgVoipOccClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,125))
cmgVoipOccClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:cmgVoipOccClear.setStatus(_B)
cmgVoipAvgOccFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,126))
cmgVoipAvgOccFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S),(_A,_A9)))
if mibBuilder.loadTexts:cmgVoipAvgOccFault.setStatus(_B)
cmgVoipAvgOccClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,127))
cmgVoipAvgOccClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S),(_A,_A9)))
if mibBuilder.loadTexts:cmgVoipAvgOccClear.setStatus(_B)
cmgVoipAutoReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,128))
cmgVoipAutoReset.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:cmgVoipAutoReset.setStatus(_B)
cmgVoipAutoResetClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,129))
cmgVoipAutoResetClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:cmgVoipAutoResetClear.setStatus(_B)
cmgDsuFpgaConfigureFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,130))
cmgDsuFpgaConfigureFault.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuFpgaConfigureFault.setStatus(_I)
cmgDsuFpgaConfigureClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,131))
cmgDsuFpgaConfigureClear.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuFpgaConfigureClear.setStatus(_I)
cmgDsuAutoReset=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,132))
cmgDsuAutoReset.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuAutoReset.setStatus(_I)
cmgDsuAutoResetClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,133))
cmgDsuAutoResetClear.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuAutoResetClear.setStatus(_I)
cmgDsuDteDtrFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,134))
cmgDsuDteDtrFault.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuDteDtrFault.setStatus(_I)
cmgDsuDteDtrClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,135))
cmgDsuDteDtrClear.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuDteDtrClear.setStatus(_I)
cmgDsuDteRtsFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,136))
cmgDsuDteRtsFault.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuDteRtsFault.setStatus(_I)
cmgDsuDteRtsClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,137))
cmgDsuDteRtsClear.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuDteRtsClear.setStatus(_I)
cmgDsuTxDFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,138))
cmgDsuTxDFault.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuTxDFault.setStatus(_I)
cmgDsuTxDClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,139))
cmgDsuTxDClear.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuTxDClear.setStatus(_I)
cmgDsuRxDFailure=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,140))
cmgDsuRxDFailure.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuRxDFailure.setStatus(_I)
cmgDsuRxDClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,141))
cmgDsuRxDClear.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgDsuRxDClear.setStatus(_I)
cmgVoipIpConfigFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,142))
cmgVoipIpConfigFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S),(_A,_AA)))
if mibBuilder.loadTexts:cmgVoipIpConfigFault.setStatus(_B)
cmgVoipIpConfigClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,143))
cmgVoipIpConfigClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_S),(_A,_AA)))
if mibBuilder.loadTexts:cmgVoipIpConfigClear.setStatus(_B)
cmgConfigDownloadFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,144))
cmgConfigDownloadFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_O,_i)))
if mibBuilder.loadTexts:cmgConfigDownloadFault.setStatus(_B)
cmgConfigDownloadBegun=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,145))
cmgConfigDownloadBegun.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgConfigDownloadBegun.setStatus(_B)
cmgConfigDownloadSuccess=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,146))
cmgConfigDownloadSuccess.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cmgConfigDownloadSuccess.setStatus(_B)
cmgTimeslotOccupancyFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,147))
cmgTimeslotOccupancyFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cmgTimeslotOccupancyFault.setStatus(_B)
cmgTimeslotOccupancyClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,148))
cmgTimeslotOccupancyClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cmgTimeslotOccupancyClear.setStatus(_B)
cmgTimeslotAvailabilityFault=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,149))
cmgTimeslotAvailabilityFault.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cmgTimeslotAvailabilityFault.setStatus(_B)
cmgTimeslotAvailabilityClear=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,150))
cmgTimeslotAvailabilityClear.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cmgTimeslotAvailabilityClear.setStatus(_B)
cmgRegistrationSuccessInetAddress=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,151))
cmgRegistrationSuccessInetAddress.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_AB),(_A,_AC),(_A,_u),(_A,_T)))
if mibBuilder.loadTexts:cmgRegistrationSuccessInetAddress.setStatus(_B)
cmgRegistrationFaultInetAddress=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,152))
cmgRegistrationFaultInetAddress.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_A,_AB),(_A,_AC),(_A,_u),(_A,_T)))
if mibBuilder.loadTexts:cmgRegistrationFaultInetAddress.setStatus(_B)
cmgDs1Layer2Down=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,153))
cmgDs1Layer2Down.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_a)))
if mibBuilder.loadTexts:cmgDs1Layer2Down.setStatus(_B)
cmgDs1Layer2Up=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,154))
cmgDs1Layer2Up.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_a)))
if mibBuilder.loadTexts:cmgDs1Layer2Up.setStatus(_B)
cmgFipsErrorMode=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,155))
cmgFipsErrorMode.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_a),(_A,_AQ),(_A,_T)))
if mibBuilder.loadTexts:cmgFipsErrorMode.setStatus(_B)
cmgCertErrorCertRevoked=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,156))
cmgCertErrorCertRevoked.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:cmgCertErrorCertRevoked.setStatus(_B)
cmgCrlAccessDenied=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,157))
cmgCrlAccessDenied.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:cmgCrlAccessDenied.setStatus(_B)
cmgCrlFileSize=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,158))
cmgCrlFileSize.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:cmgCrlFileSize.setStatus(_B)
cmgCertErrorCertExpired=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,159))
cmgCertErrorCertExpired.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:cmgCertErrorCertExpired.setStatus(_B)
cmgCertErrorNearExpiry=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,160))
cmgCertErrorNearExpiry.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:cmgCertErrorNearExpiry.setStatus(_B)
cmgCertErrorIdAuthentication=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,161))
cmgCertErrorIdAuthentication.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:cmgCertErrorIdAuthentication.setStatus(_B)
cmgOcspAccessDenied=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,0,162))
cmgOcspAccessDenied.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:cmgOcspAccessDenied.setStatus(_B)
cmgFirmwareDownloadWarning=NotificationType((1,3,6,1,4,1,6889,2,9,1,5,2,2,95))
cmgFirmwareDownloadWarning.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_O,_c),(_O,_d),(_O,_e),(_O,_AD)))
if mibBuilder.loadTexts:cmgFirmwareDownloadWarning.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CmgItuPerceivedSeverity':CmgItuPerceivedSeverity,'CmgModuleSlot':CmgModuleSlot,'avaya':avaya,'products':products,'g700MediaGateway':g700MediaGateway,'mibs':mibs,'g700MediaGatewayMIB':g700MediaGatewayMIB,'cmgmib':cmgmib,'cmgChassis':cmgChassis,'cmgHWType':cmgHWType,'cmgModelNumber':cmgModelNumber,'cmgDescription':cmgDescription,'cmgSerialNumber':cmgSerialNumber,'cmgHWVintage':cmgHWVintage,'cmgHWSuffix':cmgHWSuffix,'cmgStackPosition':cmgStackPosition,'cmgModuleList':cmgModuleList,'cmgReset':cmgReset,'cmgHardware':cmgHardware,_q:cmgCpuTemp,_x:cmgCpuTempWarningThresh,_r:cmgCpuTempShutdownThresh,_s:cmgDspTemp,_y:cmgDspTempWarningThresh,_t:cmgDspTempShutdownThresh,_z:cmgPowerMgProcessor,_A0:cmgPowerMediaModules,_A1:cmgPowerVoipComplex,_A2:cmgPowerDsp,_A3:cmgPower8260,_K:cmgHardwareFaultMask,'cmgHardwareStatusMask':cmgHardwareStatusMask,'cmgHardwareFanLowSpeedLevel':cmgHardwareFanLowSpeedLevel,'cmgModules':cmgModules,'cmgModuleTable':cmgModuleTable,'cmgModuleEntry':cmgModuleEntry,_j:cmgModuleSlot,_A4:cmgModuleType,'cmgModuleDescription':cmgModuleDescription,_A5:cmgModuleName,'cmgModuleSerialNumber':cmgModuleSerialNumber,'cmgModuleHWVintage':cmgModuleHWVintage,'cmgModuleHWSuffix':cmgModuleHWSuffix,'cmgModuleFWVersion':cmgModuleFWVersion,'cmgModuleNumberOfPorts':cmgModuleNumberOfPorts,_V:cmgModuleFaultMask,'cmgModuleStatusMask':cmgModuleStatusMask,'cmgModuleReset':cmgModuleReset,'cmgModuleNumberOfChannels':cmgModuleNumberOfChannels,'cmgDsu':cmgDsu,'cmgDsuConfigTable':cmgDsuConfigTable,'cmgDsuConfigEntry':cmgDsuConfigEntry,_l:cmgDsuSlot,_m:cmgDsuPort,'cmgDsuPortEnable':cmgDsuPortEnable,'cmgDsuDataFormat':cmgDsuDataFormat,'cmgDsuFlowControl':cmgDsuFlowControl,'cmgDsuYellowAlarmAction':cmgDsuYellowAlarmAction,'cmgDsuReceiveClock':cmgDsuReceiveClock,'cmgDsuInvertTxC':cmgDsuInvertTxC,'cmgDsuInvertRxC':cmgDsuInvertRxC,'cmgDsuInvertTxD':cmgDsuInvertTxD,'cmgDsuInvertRxD':cmgDsuInvertRxD,'cmgDsuPortInitiatedLoopback':cmgDsuPortInitiatedLoopback,'cmgDsuNetworkInitiatedLoopback':cmgDsuNetworkInitiatedLoopback,'cmgDsuChannelAssignments':cmgDsuChannelAssignments,'cmgDsuDataRate':cmgDsuDataRate,'cmgDsuPortStatusTable':cmgDsuPortStatusTable,'cmgDsuPortStatusEntry':cmgDsuPortStatusEntry,'cmgDsuRTS':cmgDsuRTS,'cmgDsuDTR':cmgDsuDTR,'cmgDsuLL':cmgDsuLL,'cmgDsuRL':cmgDsuRL,'cmgDsuRLSD':cmgDsuRLSD,'cmgDsuCTS':cmgDsuCTS,'cmgDsuDSR':cmgDsuDSR,'cmgDsuRing':cmgDsuRing,'cmgDsuTestMode':cmgDsuTestMode,'cmgDsuTxD':cmgDsuTxD,'cmgDsuRxD':cmgDsuRxD,'cmgDsuFaultMask':cmgDsuFaultMask,'cmgDsuStatusMask':cmgDsuStatusMask,'cmgDsuTestTable':cmgDsuTestTable,'cmgDsuTestEntry':cmgDsuTestEntry,'cmgDsuLoopbackPattern':cmgDsuLoopbackPattern,'cmgDsuLocalDteLoopback':cmgDsuLocalDteLoopback,'cmgDsuNearEndDataChannelLoopback':cmgDsuNearEndDataChannelLoopback,'cmgDsuFarEndDataChannelLoopback':cmgDsuFarEndDataChannelLoopback,'cmgDsuRemoteLoopback':cmgDsuRemoteLoopback,'cmgDsuDataTerminalLoopback':cmgDsuDataTerminalLoopback,'cmgDsuReset':cmgDsuReset,'cmgAnalogPorts':cmgAnalogPorts,'cmgAnalogPortTable':cmgAnalogPortTable,'cmgAnalogPortEntry':cmgAnalogPortEntry,_AE:cmgAnalogSlot,_AF:cmgAnalogPort,'cmgAnalogEchoCancellerControl':cmgAnalogEchoCancellerControl,'cmgAnalogEchoCancellerConfig1':cmgAnalogEchoCancellerConfig1,'cmgAnalogEchoCancellerConfig2':cmgAnalogEchoCancellerConfig2,'cmgAnalogBalance':cmgAnalogBalance,'cmgAnalogReceiveGain':cmgAnalogReceiveGain,'cmgAnalogTransmitGain':cmgAnalogTransmitGain,'cmgExpansionUnits':cmgExpansionUnits,'cmgExpansionUnitsTable':cmgExpansionUnitsTable,'cmgExpansions':cmgExpansions,_AH:cmgExpansionSlot,'cmgExpansionModelNumber':cmgExpansionModelNumber,'cmgExpansionDescription':cmgExpansionDescription,'cmgExpansionSerialNumber':cmgExpansionSerialNumber,'cmgExpansionHWVintage':cmgExpansionHWVintage,'cmgExpansionHWSuffix':cmgExpansionHWSuffix,'cmgExpansionDemandTest':cmgExpansionDemandTest,'cmgExpansionDemandTestResult':cmgExpansionDemandTestResult,'cmgTimeslotMonitoring':cmgTimeslotMonitoring,'cmgTimeslotUpperThreshold':cmgTimeslotUpperThreshold,'cmgTimeslotLowerThreshold':cmgTimeslotLowerThreshold,'cmgProcessor':cmgProcessor,'cmgProcessorConfig':cmgProcessorConfig,'cmgGatewayNumber':cmgGatewayNumber,'cmgMACAddress':cmgMACAddress,'cmgFWVersion':cmgFWVersion,'cmgCurrentIpAddress':cmgCurrentIpAddress,'cmgUseDhcpForIpAddress':cmgUseDhcpForIpAddress,'cmgUseDhcpForVlan':cmgUseDhcpForVlan,'cmgDhcpSson':cmgDhcpSson,'cmgStaticIpAddress':cmgStaticIpAddress,'cmgDnsServerList':cmgDnsServerList,'cmgDnsHostname':cmgDnsHostname,_L:cmgMgpFaultMask,'cmgCurrentInetAddressType':cmgCurrentInetAddressType,'cmgCurrentInetAddress':cmgCurrentInetAddress,'cmgProcessorQos':cmgProcessorQos,'cmgQosControl':cmgQosControl,'cmgRemoteSigDscp':cmgRemoteSigDscp,'cmgRemoteSig802Priority':cmgRemoteSig802Priority,'cmgLocalSigDscp':cmgLocalSigDscp,'cmgLocalSig802Priority':cmgLocalSig802Priority,'cmgStatic802Vlan':cmgStatic802Vlan,'cmgCurrent802Vlan':cmgCurrent802Vlan,'cmgProcessorClock':cmgProcessorClock,_X:cmgPrimaryClockSource,_Y:cmgSecondaryClockSource,_Z:cmgActiveClockSource,'cmgClockSwitching':cmgClockSwitching,'cmgClockSourceControl':cmgClockSourceControl,'cmgControllers':cmgControllers,'cmgRegistrationState':cmgRegistrationState,_A6:cmgActiveControllerAddress,'cmgH248LinkStatus':cmgH248LinkStatus,'cmgH248LinkErrorCode':cmgH248LinkErrorCode,_f:cmgUseDhcpForMgcList,'cmgStaticControllerHosts':cmgStaticControllerHosts,'cmgDhcpControllerHosts':cmgDhcpControllerHosts,'cmgPrimarySearchTime':cmgPrimarySearchTime,'cmgTotalSearchTime':cmgTotalSearchTime,'cmgTransitionPoint':cmgTransitionPoint,'cmgActiveControllerSoftwareVersion':cmgActiveControllerSoftwareVersion,_AB:cmgActiveControllerInetAddressType,_AC:cmgActiveControllerInetAddress,'cmgVoip':cmgVoip,'cmgVoipEngineUseDhcp':cmgVoipEngineUseDhcp,'cmgVoipQosControl':cmgVoipQosControl,'cmgVoipRemoteParameters':cmgVoipRemoteParameters,'cmgVoipRemoteQosParameters':cmgVoipRemoteQosParameters,'cmgVoipRemoteBbeDscp':cmgVoipRemoteBbeDscp,'cmgVoipRemoteEfDscp':cmgVoipRemoteEfDscp,'cmgVoipRemote802Priority':cmgVoipRemote802Priority,'cmgVoipRemoteMinRtpPort':cmgVoipRemoteMinRtpPort,'cmgVoipRemoteMaxRtpPort':cmgVoipRemoteMaxRtpPort,'cmgVoipRemoteRtcpParameters':cmgVoipRemoteRtcpParameters,'cmgVoipRemoteRtcpEnabled':cmgVoipRemoteRtcpEnabled,'cmgVoipRemoteRtcpMonitorIpAddress':cmgVoipRemoteRtcpMonitorIpAddress,'cmgVoipRemoteRtcpMonitorPort':cmgVoipRemoteRtcpMonitorPort,'cmgVoipRemoteRtcpReportPeriod':cmgVoipRemoteRtcpReportPeriod,'cmgVoipRemoteRtcpMonitorInetAddressType':cmgVoipRemoteRtcpMonitorInetAddressType,'cmgVoipRemoteRtcpMonitorInetAddress':cmgVoipRemoteRtcpMonitorInetAddress,'cmgVoipRemoteRtcpMonitorPortInetAddress':cmgVoipRemoteRtcpMonitorPortInetAddress,'cmgVoipRemoteRsvpParameters':cmgVoipRemoteRsvpParameters,'cmgVoipRemoteRsvpEnabled':cmgVoipRemoteRsvpEnabled,'cmgVoipRemoteRetryOnFailure':cmgVoipRemoteRetryOnFailure,'cmgVoipRemoteRetryDelay':cmgVoipRemoteRetryDelay,'cmgVoipRemoteRsvpProfile':cmgVoipRemoteRsvpProfile,'cmgVoipLocalParameters':cmgVoipLocalParameters,'cmgVoipLocalQosParameters':cmgVoipLocalQosParameters,'cmgVoipLocalBbeDscp':cmgVoipLocalBbeDscp,'cmgVoipLocalEfDscp':cmgVoipLocalEfDscp,'cmgVoipLocal802Priority':cmgVoipLocal802Priority,'cmgVoipLocalMinRtpPort':cmgVoipLocalMinRtpPort,'cmgVoipLocalMaxRtpPort':cmgVoipLocalMaxRtpPort,'cmgVoipLocalRtcpParameters':cmgVoipLocalRtcpParameters,'cmgVoipLocalRtcpEnabled':cmgVoipLocalRtcpEnabled,'cmgVoipLocalRtcpMonitorIpAddress':cmgVoipLocalRtcpMonitorIpAddress,'cmgVoipLocalRtcpMonitorPort':cmgVoipLocalRtcpMonitorPort,'cmgVoipLocalRtcpReportPeriod':cmgVoipLocalRtcpReportPeriod,'cmgVoipLocalRtcpMonitorInetAddressType':cmgVoipLocalRtcpMonitorInetAddressType,'cmgVoipLocalRtcpMonitorInetAddress':cmgVoipLocalRtcpMonitorInetAddress,'cmgVoipLocalRtcpMonitorPortInetAddress':cmgVoipLocalRtcpMonitorPortInetAddress,'cmgVoipLocalRsvpParameters':cmgVoipLocalRsvpParameters,'cmgVoipLocalRsvpEnabled':cmgVoipLocalRsvpEnabled,'cmgVoipLocalRetryOnFailure':cmgVoipLocalRetryOnFailure,'cmgVoipLocalRetryDelay':cmgVoipLocalRetryDelay,'cmgVoipLocalRsvpProfile':cmgVoipLocalRsvpProfile,'cmgVoipEngineTable':cmgVoipEngineTable,'cmgVoipEngineEntry':cmgVoipEngineEntry,_w:cmgVoipSlot,'cmgVoipMACAddress':cmgVoipMACAddress,'cmgVoipStaticIpAddress':cmgVoipStaticIpAddress,_AA:cmgVoipCurrentIpAddress,'cmgVoipJitterBufferSize':cmgVoipJitterBufferSize,_A8:cmgVoipTotalChannels,_A7:cmgVoipChannelsInUse,_A9:cmgVoipAverageOccupancy,'cmgVoipHyperactivity':cmgVoipHyperactivity,'cmgVoipAdminState':cmgVoipAdminState,'cmgVoipDspFWVersion':cmgVoipDspFWVersion,'cmgVoipDspStatus':cmgVoipDspStatus,'cmgVoipEngineReset':cmgVoipEngineReset,_S:cmgVoipFaultMask,'cmgVoipStaticInetAddressType':cmgVoipStaticInetAddressType,'cmgVoipStaticInetAddress':cmgVoipStaticInetAddress,'cmgVoipCurrentInetAddressType':cmgVoipCurrentInetAddressType,'cmgVoipCurrentInetAddress':cmgVoipCurrentInetAddress,'cmgVoipDSPCoreTable':cmgVoipDSPCoreTable,'cmgVoipDSPCoreEntry':cmgVoipDSPCoreEntry,_AK:cmgDSPCoreCoreId,'cmgDSPCoreTotalChannels':cmgDSPCoreTotalChannels,'cmgDSPCoreChannelsInUse':cmgDSPCoreChannelsInUse,'cmgDSPCoreAdminState':cmgDSPCoreAdminState,'cmgDSPCoreStatus':cmgDSPCoreStatus,'cmgDSPCoreDemandTest':cmgDSPCoreDemandTest,'cmgDSPCoreDemandTestResult':cmgDSPCoreDemandTestResult,'cmgVoipEchoCancellerControl':cmgVoipEchoCancellerControl,'cmgVoipEchoCancellerConfig1':cmgVoipEchoCancellerConfig1,'cmgVoipEchoCancellerConfig2':cmgVoipEchoCancellerConfig2,'cmgVoipTotalChannelsEnforcedByCM':cmgVoipTotalChannelsEnforcedByCM,'cmgTraps':cmgTraps,'cmgTrapManagerTable':cmgTrapManagerTable,'cmgTrapManagerEntry':cmgTrapManagerEntry,_AL:cmgTrapManagerAddress,'cmgTrapManagerControl':cmgTrapManagerControl,'cmgTrapManagerMask':cmgTrapManagerMask,'cmgTrapManagerRowStatus':cmgTrapManagerRowStatus,'cmgTrapDefinitions':cmgTrapDefinitions,'cmgTrapVariables':cmgTrapVariables,_G:cmgTrapLocation,_F:cmgTrapOnBoard,_E:cmgTrapSubsystem,'cmgTrapOnIccMissing':cmgTrapOnIccMissing,_a:cmgTrapModule,_T:cmgTrapSeverity,_u:cmgProductId,_g:cmgTrapAvailableTimeslots,_h:cmgTrapInUseTimeslots,_AQ:cmgFipsErrorType,'cmgTrapTypes':cmgTrapTypes,'cmgTrapV3separator':cmgTrapV3separator,'cmgMultipleFanFault':cmgMultipleFanFault,'cmgMultipleFanClear':cmgMultipleFanClear,'cmgPsuFanBriefFault':cmgPsuFanBriefFault,'cmgPsuFanBriefClear':cmgPsuFanBriefClear,'cmgPsuFanProlongedFault':cmgPsuFanProlongedFault,'cmgPsuFanProlongedClear':cmgPsuFanProlongedClear,'cmgCpuTempWarningFault':cmgCpuTempWarningFault,'cmgCpuTempWarningClear':cmgCpuTempWarningClear,'cmgDspTempWarningFault':cmgDspTempWarningFault,'cmgDspTempWarningClear':cmgDspTempWarningClear,'cmgTempShutdownFault':cmgTempShutdownFault,'cmgMgpPowerFault':cmgMgpPowerFault,'cmgMgpPowerClear':cmgMgpPowerClear,'cmgMediaModulePowerFault':cmgMediaModulePowerFault,'cmgMediaModulePowerClear':cmgMediaModulePowerClear,'cmgVoipPowerFault':cmgVoipPowerFault,'cmgVoipPowerClear':cmgVoipPowerClear,'cmgDspPowerFault':cmgDspPowerFault,'cmgDspPowerClear':cmgDspPowerClear,'cmg8260PowerFault':cmg8260PowerFault,'cmg8260PowerClear':cmg8260PowerClear,'cmgAuxPowerFault':cmgAuxPowerFault,'cmgAuxPowerClear':cmgAuxPowerClear,'cmgFanPowerFault':cmgFanPowerFault,'cmgFanPowerClear':cmgFanPowerClear,'cmgSyncSignalFault':cmgSyncSignalFault,'cmgSyncSignalClear':cmgSyncSignalClear,'cmgVoipHardwareFault':cmgVoipHardwareFault,'cmgVoipHardwareClear':cmgVoipHardwareClear,'cmgSyncSignalWarn':cmgSyncSignalWarn,'cmgSyncWarnClear':cmgSyncWarnClear,'cmgSyncSignalExcess':cmgSyncSignalExcess,'cmgSyncExcessClear':cmgSyncExcessClear,'cmgVoipCoreFault':cmgVoipCoreFault,'cmgVoipCoreClear':cmgVoipCoreClear,'cmgModuleRemove':cmgModuleRemove,'cmgModuleInsertFault':cmgModuleInsertFault,'cmgModuleInsertSuccess':cmgModuleInsertSuccess,'cmgMgBusyout':cmgMgBusyout,'cmgMgRelease':cmgMgRelease,'cmgUnsupportedMmEnrolement':cmgUnsupportedMmEnrolement,'cmgDataModuleAwohConflict':cmgDataModuleAwohConflict,'cmgFirmwareDownloadBegun':cmgFirmwareDownloadBegun,'cmgFirmwareDownloadSuccess':cmgFirmwareDownloadSuccess,'cmgRegistrationSuccess':cmgRegistrationSuccess,'cmgMgManualReset':cmgMgManualReset,'cmgModuleManualReset':cmgModuleManualReset,'cmgVoipManualReset':cmgVoipManualReset,'cmgDsuManualReset':cmgDsuManualReset,'cmgConfigUploadBegun':cmgConfigUploadBegun,'cmgConfigUploadSuccess':cmgConfigUploadSuccess,'cmgMemoryFault':cmgMemoryFault,'cmgMemoryClear':cmgMemoryClear,'cmgDhcpRequestFault':cmgDhcpRequestFault,'cmgDhcpRequestClear':cmgDhcpRequestClear,'cmgFirmwareDownloadFault':cmgFirmwareDownloadFault,'cmgProcessRestart':cmgProcessRestart,'cmgProcessRestartClear':cmgProcessRestartClear,'cmgIccMissingFault':cmgIccMissingFault,'cmgIccMissingClear':cmgIccMissingClear,'cmgIccAutoReset':cmgIccAutoReset,'cmgIccAutoResetClear':cmgIccAutoResetClear,'cmgPrimaryControllerFault':cmgPrimaryControllerFault,'cmgPrimaryControllerClear':cmgPrimaryControllerClear,'cmgNoControllerFault':cmgNoControllerFault,'cmgNoControllerClear':cmgNoControllerClear,'cmgRegistrationFault':cmgRegistrationFault,'cmgH248LinkDown':cmgH248LinkDown,'cmgH248LinkUp':cmgH248LinkUp,'cmgTestFault':cmgTestFault,'cmgTestClear':cmgTestClear,'cmgTestThresholdFault':cmgTestThresholdFault,'cmgTestThresholdClear':cmgTestThresholdClear,'cmgMgAutoReset':cmgMgAutoReset,'cmgModuleAutoReset':cmgModuleAutoReset,'cmgModuleAutoResetClear':cmgModuleAutoResetClear,'cmgModulePostFault':cmgModulePostFault,'cmgModulePostClear':cmgModulePostClear,'cmgModuleParameterFault':cmgModuleParameterFault,'cmgModuleParameterClear':cmgModuleParameterClear,'cmgConfigUploadFault':cmgConfigUploadFault,'cmgVoipOccFault':cmgVoipOccFault,'cmgVoipOccClear':cmgVoipOccClear,'cmgVoipAvgOccFault':cmgVoipAvgOccFault,'cmgVoipAvgOccClear':cmgVoipAvgOccClear,'cmgVoipAutoReset':cmgVoipAutoReset,'cmgVoipAutoResetClear':cmgVoipAutoResetClear,'cmgDsuFpgaConfigureFault':cmgDsuFpgaConfigureFault,'cmgDsuFpgaConfigureClear':cmgDsuFpgaConfigureClear,'cmgDsuAutoReset':cmgDsuAutoReset,'cmgDsuAutoResetClear':cmgDsuAutoResetClear,'cmgDsuDteDtrFault':cmgDsuDteDtrFault,'cmgDsuDteDtrClear':cmgDsuDteDtrClear,'cmgDsuDteRtsFault':cmgDsuDteRtsFault,'cmgDsuDteRtsClear':cmgDsuDteRtsClear,'cmgDsuTxDFault':cmgDsuTxDFault,'cmgDsuTxDClear':cmgDsuTxDClear,'cmgDsuRxDFailure':cmgDsuRxDFailure,'cmgDsuRxDClear':cmgDsuRxDClear,'cmgVoipIpConfigFault':cmgVoipIpConfigFault,'cmgVoipIpConfigClear':cmgVoipIpConfigClear,'cmgConfigDownloadFault':cmgConfigDownloadFault,'cmgConfigDownloadBegun':cmgConfigDownloadBegun,'cmgConfigDownloadSuccess':cmgConfigDownloadSuccess,'cmgTimeslotOccupancyFault':cmgTimeslotOccupancyFault,'cmgTimeslotOccupancyClear':cmgTimeslotOccupancyClear,'cmgTimeslotAvailabilityFault':cmgTimeslotAvailabilityFault,'cmgTimeslotAvailabilityClear':cmgTimeslotAvailabilityClear,'cmgRegistrationSuccessInetAddress':cmgRegistrationSuccessInetAddress,'cmgRegistrationFaultInetAddress':cmgRegistrationFaultInetAddress,'cmgDs1Layer2Down':cmgDs1Layer2Down,'cmgDs1Layer2Up':cmgDs1Layer2Up,'cmgFipsErrorMode':cmgFipsErrorMode,'cmgCertErrorCertRevoked':cmgCertErrorCertRevoked,'cmgCrlAccessDenied':cmgCrlAccessDenied,'cmgCrlFileSize':cmgCrlFileSize,'cmgCertErrorCertExpired':cmgCertErrorCertExpired,'cmgCertErrorNearExpiry':cmgCertErrorNearExpiry,'cmgCertErrorIdAuthentication':cmgCertErrorIdAuthentication,'cmgOcspAccessDenied':cmgOcspAccessDenied,'cmgFirmwareDownloadWarning':cmgFirmwareDownloadWarning,'cmgContactClosures':cmgContactClosures,'cmgContactClosuresTable':cmgContactClosuresTable,'cmgContactClosuresEntry':cmgContactClosuresEntry,_AM:cmgCcModule,_AN:cmgCcPort,_AO:cmgCcRelay,'cmgCcAdminState':cmgCcAdminState,'cmgCcPulseDuration':cmgCcPulseDuration,'cmgCcStatus':cmgCcStatus,'cmgETR':cmgETR,'cmgETRTable':cmgETRTable,'cmgETREntry':cmgETREntry,_AP:cmgEtrModule,'cmgEtrAdminState':cmgEtrAdminState,'cmgEtrNumberOfPairs':cmgEtrNumberOfPairs,'cmgEtrStatus':cmgEtrStatus,'cmgEtrCurrentLoopDetect':cmgEtrCurrentLoopDetect,'cmgDynamicCAC':cmgDynamicCAC,'cmgDynCacStatus':cmgDynCacStatus,'cmgDynCacRBBL':cmgDynCacRBBL,'cmgDynCacLastUpdate':cmgDynCacLastUpdate,'cmgSLAMonitor':cmgSLAMonitor,'cmgSLAMonitorState':cmgSLAMonitorState,'cmgSLAMonitorServerInetAddressType':cmgSLAMonitorServerInetAddressType,'cmgSLAMonitorServerInetAddress':cmgSLAMonitorServerInetAddress,'cmgSLAMonitorServerPort':cmgSLAMonitorServerPort,'cmgSLAMonitorPacketCaptureMode':cmgSLAMonitorPacketCaptureMode,'cmgSLAMonitorVersion':cmgSLAMonitorVersion})