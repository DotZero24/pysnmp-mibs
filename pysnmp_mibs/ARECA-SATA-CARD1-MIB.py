_R='eventNumber'
_Q='volNumber'
_P='raidNumber'
_O='hddSlots'
_N='hwControllerBoardTempIndex'
_M='hwControllerBoardFanIndex'
_L='hwControllerBoardVolIndex'
_K='hwControllerBoardPowerIndex'
_J='NotificationType'
_I='enabled'
_H='disabled'
_G='s512K'
_F='s32K'
_E='Integer32'
_D='read-only'
_C='mandatory'
_B='eventString'
_A='ARECA-SATA-CARD1-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Areca_ObjectIdentity=ObjectIdentity
areca=_Areca_ObjectIdentity((1,3,6,1,4,1,18928))
_ArecaGroup1_ObjectIdentity=ObjectIdentity
arecaGroup1=_ArecaGroup1_ObjectIdentity((1,3,6,1,4,1,18928,1))
_SataRaidCard1_ObjectIdentity=ObjectIdentity
sataRaidCard1=_SataRaidCard1_ObjectIdentity((1,3,6,1,4,1,18928,1,1))
_SystemInformation_ObjectIdentity=ObjectIdentity
systemInformation=_SystemInformation_ObjectIdentity((1,3,6,1,4,1,18928,1,1,1))
_SiVendor_Type=OctetString
_SiVendor_Object=MibScalar
siVendor=_SiVendor_Object((1,3,6,1,4,1,18928,1,1,1,1),_SiVendor_Type())
siVendor.setMaxAccess(_D)
if mibBuilder.loadTexts:siVendor.setStatus(_C)
_SiModel_Type=OctetString
_SiModel_Object=MibScalar
siModel=_SiModel_Object((1,3,6,1,4,1,18928,1,1,1,2),_SiModel_Type())
siModel.setMaxAccess(_D)
if mibBuilder.loadTexts:siModel.setStatus(_C)
_SiSerial_Type=OctetString
_SiSerial_Object=MibScalar
siSerial=_SiSerial_Object((1,3,6,1,4,1,18928,1,1,1,3),_SiSerial_Type())
siSerial.setMaxAccess(_D)
if mibBuilder.loadTexts:siSerial.setStatus(_C)
_SiFirmVer_Type=OctetString
_SiFirmVer_Object=MibScalar
siFirmVer=_SiFirmVer_Object((1,3,6,1,4,1,18928,1,1,1,4),_SiFirmVer_Type())
siFirmVer.setMaxAccess(_D)
if mibBuilder.loadTexts:siFirmVer.setStatus(_C)
_SiBootVer_Type=OctetString
_SiBootVer_Object=MibScalar
siBootVer=_SiBootVer_Object((1,3,6,1,4,1,18928,1,1,1,5),_SiBootVer_Type())
siBootVer.setMaxAccess(_D)
if mibBuilder.loadTexts:siBootVer.setStatus(_C)
_SiMbrVer_Type=OctetString
_SiMbrVer_Object=MibScalar
siMbrVer=_SiMbrVer_Object((1,3,6,1,4,1,18928,1,1,1,6),_SiMbrVer_Type())
siMbrVer.setMaxAccess(_D)
if mibBuilder.loadTexts:siMbrVer.setStatus(_C)
_SiProcessor_Type=OctetString
_SiProcessor_Object=MibScalar
siProcessor=_SiProcessor_Object((1,3,6,1,4,1,18928,1,1,1,7),_SiProcessor_Type())
siProcessor.setMaxAccess(_D)
if mibBuilder.loadTexts:siProcessor.setStatus(_C)
_SiCpuSpeed_Type=Integer32
_SiCpuSpeed_Object=MibScalar
siCpuSpeed=_SiCpuSpeed_Object((1,3,6,1,4,1,18928,1,1,1,8),_SiCpuSpeed_Type())
siCpuSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:siCpuSpeed.setStatus(_C)
class _SiICache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32768,524288)));namedValues=NamedValues(*((_F,32768),(_G,524288)))
_SiICache_Type.__name__=_E
_SiICache_Object=MibScalar
siICache=_SiICache_Object((1,3,6,1,4,1,18928,1,1,1,9),_SiICache_Type())
siICache.setMaxAccess(_D)
if mibBuilder.loadTexts:siICache.setStatus(_C)
class _SiDCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32768,524288)));namedValues=NamedValues(*((_F,32768),(_G,524288)))
_SiDCache_Type.__name__=_E
_SiDCache_Object=MibScalar
siDCache=_SiDCache_Object((1,3,6,1,4,1,18928,1,1,1,10),_SiDCache_Type())
siDCache.setMaxAccess(_D)
if mibBuilder.loadTexts:siDCache.setStatus(_C)
class _SiSCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32768,524288)));namedValues=NamedValues(*((_F,32768),(_G,524288)))
_SiSCache_Type.__name__=_E
_SiSCache_Object=MibScalar
siSCache=_SiSCache_Object((1,3,6,1,4,1,18928,1,1,1,11),_SiSCache_Type())
siSCache.setMaxAccess(_D)
if mibBuilder.loadTexts:siSCache.setStatus(_C)
_SiMemory_Type=Integer32
_SiMemory_Object=MibScalar
siMemory=_SiMemory_Object((1,3,6,1,4,1,18928,1,1,1,12),_SiMemory_Type())
siMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:siMemory.setStatus(_C)
_SiMemSpeed_Type=Integer32
_SiMemSpeed_Object=MibScalar
siMemSpeed=_SiMemSpeed_Object((1,3,6,1,4,1,18928,1,1,1,13),_SiMemSpeed_Type())
siMemSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:siMemSpeed.setStatus(_C)
class _SiEcc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_SiEcc_Type.__name__=_E
_SiEcc_Object=MibScalar
siEcc=_SiEcc_Object((1,3,6,1,4,1,18928,1,1,1,14),_SiEcc_Type())
siEcc.setMaxAccess(_D)
if mibBuilder.loadTexts:siEcc.setStatus(_C)
_SiHosts_Type=Integer32
_SiHosts_Object=MibScalar
siHosts=_SiHosts_Object((1,3,6,1,4,1,18928,1,1,1,15),_SiHosts_Type())
siHosts.setMaxAccess(_D)
if mibBuilder.loadTexts:siHosts.setStatus(_C)
_SiHddSlots_Type=Integer32
_SiHddSlots_Object=MibScalar
siHddSlots=_SiHddSlots_Object((1,3,6,1,4,1,18928,1,1,1,16),_SiHddSlots_Type())
siHddSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:siHddSlots.setStatus(_C)
_SiRaidSets_Type=Integer32
_SiRaidSets_Object=MibScalar
siRaidSets=_SiRaidSets_Object((1,3,6,1,4,1,18928,1,1,1,17),_SiRaidSets_Type())
siRaidSets.setMaxAccess(_D)
if mibBuilder.loadTexts:siRaidSets.setStatus(_C)
_SiVolumeSets_Type=Integer32
_SiVolumeSets_Object=MibScalar
siVolumeSets=_SiVolumeSets_Object((1,3,6,1,4,1,18928,1,1,1,18),_SiVolumeSets_Type())
siVolumeSets.setMaxAccess(_D)
if mibBuilder.loadTexts:siVolumeSets.setStatus(_C)
_SiEvents_Type=Integer32
_SiEvents_Object=MibScalar
siEvents=_SiEvents_Object((1,3,6,1,4,1,18928,1,1,1,19),_SiEvents_Type())
siEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:siEvents.setStatus(_C)
_SiFans_Type=Integer32
_SiFans_Object=MibScalar
siFans=_SiFans_Object((1,3,6,1,4,1,18928,1,1,1,20),_SiFans_Type())
siFans.setMaxAccess(_D)
if mibBuilder.loadTexts:siFans.setStatus(_C)
_SiPowers_Type=Integer32
_SiPowers_Object=MibScalar
siPowers=_SiPowers_Object((1,3,6,1,4,1,18928,1,1,1,21),_SiPowers_Type())
siPowers.setMaxAccess(_D)
if mibBuilder.loadTexts:siPowers.setStatus(_C)
class _SiRaid6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_SiRaid6_Type.__name__=_E
_SiRaid6_Object=MibScalar
siRaid6=_SiRaid6_Object((1,3,6,1,4,1,18928,1,1,1,22),_SiRaid6_Type())
siRaid6.setMaxAccess(_D)
if mibBuilder.loadTexts:siRaid6.setStatus(_C)
class _SiDhcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SiDhcp_Type.__name__=_E
_SiDhcp_Object=MibScalar
siDhcp=_SiDhcp_Object((1,3,6,1,4,1,18928,1,1,1,23),_SiDhcp_Type())
siDhcp.setMaxAccess(_D)
if mibBuilder.loadTexts:siDhcp.setStatus(_C)
class _SiBeeper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SiBeeper_Type.__name__=_E
_SiBeeper_Object=MibScalar
siBeeper=_SiBeeper_Object((1,3,6,1,4,1,18928,1,1,1,24),_SiBeeper_Type())
siBeeper.setMaxAccess(_D)
if mibBuilder.loadTexts:siBeeper.setStatus(_C)
class _SiUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('jbod',1)))
_SiUsage_Type.__name__=_E
_SiUsage_Object=MibScalar
siUsage=_SiUsage_Object((1,3,6,1,4,1,18928,1,1,1,25),_SiUsage_Type())
siUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:siUsage.setStatus(_C)
class _SiMaxATA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(33,66,100,133,150)));namedValues=NamedValues(*(('ata33',33),('ata66',66),('ata100',100),('ata133',133),('serialATA',150)))
_SiMaxATA_Type.__name__=_E
_SiMaxATA_Object=MibScalar
siMaxATA=_SiMaxATA_Object((1,3,6,1,4,1,18928,1,1,1,26),_SiMaxATA_Type())
siMaxATA.setMaxAccess(_D)
if mibBuilder.loadTexts:siMaxATA.setStatus(_C)
_SiRebuildRate_Type=Integer32
_SiRebuildRate_Object=MibScalar
siRebuildRate=_SiRebuildRate_Object((1,3,6,1,4,1,18928,1,1,1,27),_SiRebuildRate_Type())
siRebuildRate.setMaxAccess(_D)
if mibBuilder.loadTexts:siRebuildRate.setStatus(_C)
class _SiBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1200,2400,4800,9600,19200,38400,57600,115200)));namedValues=NamedValues(*(('s1200bps',1200),('s2400bps',2400),('s4800bps',4800),('s9600bps',9600),('s19200bps',19200),('s38400bps',38400),('s57600bps',57600),('s115200bps',115200)))
_SiBaudRate_Type.__name__=_E
_SiBaudRate_Object=MibScalar
siBaudRate=_SiBaudRate_Object((1,3,6,1,4,1,18928,1,1,1,28),_SiBaudRate_Type())
siBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:siBaudRate.setStatus(_C)
_HwMonitor_ObjectIdentity=ObjectIdentity
hwMonitor=_HwMonitor_ObjectIdentity((1,3,6,1,4,1,18928,1,1,2))
_HwControllerBoardInstalled_Type=Integer32
_HwControllerBoardInstalled_Object=MibScalar
hwControllerBoardInstalled=_HwControllerBoardInstalled_Object((1,3,6,1,4,1,18928,1,1,2,1),_HwControllerBoardInstalled_Type())
hwControllerBoardInstalled.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardInstalled.setStatus(_C)
_HwControllerBoardDescription_Type=OctetString
_HwControllerBoardDescription_Object=MibScalar
hwControllerBoardDescription=_HwControllerBoardDescription_Object((1,3,6,1,4,1,18928,1,1,2,2),_HwControllerBoardDescription_Type())
hwControllerBoardDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardDescription.setStatus(_C)
_HwControllerBoardNumberOfPower_Type=Integer32
_HwControllerBoardNumberOfPower_Object=MibScalar
hwControllerBoardNumberOfPower=_HwControllerBoardNumberOfPower_Object((1,3,6,1,4,1,18928,1,1,2,3),_HwControllerBoardNumberOfPower_Type())
hwControllerBoardNumberOfPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardNumberOfPower.setStatus(_C)
_HwControllerBoardNumberOfVol_Type=Integer32
_HwControllerBoardNumberOfVol_Object=MibScalar
hwControllerBoardNumberOfVol=_HwControllerBoardNumberOfVol_Object((1,3,6,1,4,1,18928,1,1,2,4),_HwControllerBoardNumberOfVol_Type())
hwControllerBoardNumberOfVol.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardNumberOfVol.setStatus(_C)
_HwControllerBoardNumberOfFan_Type=Integer32
_HwControllerBoardNumberOfFan_Object=MibScalar
hwControllerBoardNumberOfFan=_HwControllerBoardNumberOfFan_Object((1,3,6,1,4,1,18928,1,1,2,5),_HwControllerBoardNumberOfFan_Type())
hwControllerBoardNumberOfFan.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardNumberOfFan.setStatus(_C)
_HwControllerBoardNumberOfTemp_Type=Integer32
_HwControllerBoardNumberOfTemp_Object=MibScalar
hwControllerBoardNumberOfTemp=_HwControllerBoardNumberOfTemp_Object((1,3,6,1,4,1,18928,1,1,2,6),_HwControllerBoardNumberOfTemp_Type())
hwControllerBoardNumberOfTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardNumberOfTemp.setStatus(_C)
_HwControllerBoardPowerTable_Object=MibTable
hwControllerBoardPowerTable=_HwControllerBoardPowerTable_Object((1,3,6,1,4,1,18928,1,1,2,7))
if mibBuilder.loadTexts:hwControllerBoardPowerTable.setStatus(_C)
_HwControllerBoardPowerEntry_Object=MibTableRow
hwControllerBoardPowerEntry=_HwControllerBoardPowerEntry_Object((1,3,6,1,4,1,18928,1,1,2,7,1))
hwControllerBoardPowerEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:hwControllerBoardPowerEntry.setStatus(_C)
_HwControllerBoardPowerIndex_Type=Integer32
_HwControllerBoardPowerIndex_Object=MibTableColumn
hwControllerBoardPowerIndex=_HwControllerBoardPowerIndex_Object((1,3,6,1,4,1,18928,1,1,2,7,1,1),_HwControllerBoardPowerIndex_Type())
hwControllerBoardPowerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardPowerIndex.setStatus(_C)
_HwControllerBoardPowerDesc_Type=OctetString
_HwControllerBoardPowerDesc_Object=MibTableColumn
hwControllerBoardPowerDesc=_HwControllerBoardPowerDesc_Object((1,3,6,1,4,1,18928,1,1,2,7,1,2),_HwControllerBoardPowerDesc_Type())
hwControllerBoardPowerDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardPowerDesc.setStatus(_C)
class _HwControllerBoardPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('failed',0),('ok',1)))
_HwControllerBoardPowerState_Type.__name__=_E
_HwControllerBoardPowerState_Object=MibTableColumn
hwControllerBoardPowerState=_HwControllerBoardPowerState_Object((1,3,6,1,4,1,18928,1,1,2,7,1,3),_HwControllerBoardPowerState_Type())
hwControllerBoardPowerState.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardPowerState.setStatus(_C)
_HwControllerBoardVolTable_Object=MibTable
hwControllerBoardVolTable=_HwControllerBoardVolTable_Object((1,3,6,1,4,1,18928,1,1,2,8))
if mibBuilder.loadTexts:hwControllerBoardVolTable.setStatus(_C)
_HwControllerBoardVolEntry_Object=MibTableRow
hwControllerBoardVolEntry=_HwControllerBoardVolEntry_Object((1,3,6,1,4,1,18928,1,1,2,8,1))
hwControllerBoardVolEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:hwControllerBoardVolEntry.setStatus(_C)
_HwControllerBoardVolIndex_Type=Integer32
_HwControllerBoardVolIndex_Object=MibTableColumn
hwControllerBoardVolIndex=_HwControllerBoardVolIndex_Object((1,3,6,1,4,1,18928,1,1,2,8,1,1),_HwControllerBoardVolIndex_Type())
hwControllerBoardVolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardVolIndex.setStatus(_C)
_HwControllerBoardVolDesc_Type=OctetString
_HwControllerBoardVolDesc_Object=MibTableColumn
hwControllerBoardVolDesc=_HwControllerBoardVolDesc_Object((1,3,6,1,4,1,18928,1,1,2,8,1,2),_HwControllerBoardVolDesc_Type())
hwControllerBoardVolDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardVolDesc.setStatus(_C)
_HwControllerBoardVolValue_Type=Integer32
_HwControllerBoardVolValue_Object=MibTableColumn
hwControllerBoardVolValue=_HwControllerBoardVolValue_Object((1,3,6,1,4,1,18928,1,1,2,8,1,3),_HwControllerBoardVolValue_Type())
hwControllerBoardVolValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardVolValue.setStatus(_C)
_HwControllerBoardFanTable_Object=MibTable
hwControllerBoardFanTable=_HwControllerBoardFanTable_Object((1,3,6,1,4,1,18928,1,1,2,9))
if mibBuilder.loadTexts:hwControllerBoardFanTable.setStatus(_C)
_HwControllerBoardFanEntry_Object=MibTableRow
hwControllerBoardFanEntry=_HwControllerBoardFanEntry_Object((1,3,6,1,4,1,18928,1,1,2,9,1))
hwControllerBoardFanEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:hwControllerBoardFanEntry.setStatus(_C)
_HwControllerBoardFanIndex_Type=Integer32
_HwControllerBoardFanIndex_Object=MibTableColumn
hwControllerBoardFanIndex=_HwControllerBoardFanIndex_Object((1,3,6,1,4,1,18928,1,1,2,9,1,1),_HwControllerBoardFanIndex_Type())
hwControllerBoardFanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardFanIndex.setStatus(_C)
_HwControllerBoardFanDesc_Type=OctetString
_HwControllerBoardFanDesc_Object=MibTableColumn
hwControllerBoardFanDesc=_HwControllerBoardFanDesc_Object((1,3,6,1,4,1,18928,1,1,2,9,1,2),_HwControllerBoardFanDesc_Type())
hwControllerBoardFanDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardFanDesc.setStatus(_C)
_HwControllerBoardFanSpeed_Type=Integer32
_HwControllerBoardFanSpeed_Object=MibTableColumn
hwControllerBoardFanSpeed=_HwControllerBoardFanSpeed_Object((1,3,6,1,4,1,18928,1,1,2,9,1,3),_HwControllerBoardFanSpeed_Type())
hwControllerBoardFanSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardFanSpeed.setStatus(_C)
_HwControllerBoardTempTable_Object=MibTable
hwControllerBoardTempTable=_HwControllerBoardTempTable_Object((1,3,6,1,4,1,18928,1,1,2,10))
if mibBuilder.loadTexts:hwControllerBoardTempTable.setStatus(_C)
_HwControllerBoardTempEntry_Object=MibTableRow
hwControllerBoardTempEntry=_HwControllerBoardTempEntry_Object((1,3,6,1,4,1,18928,1,1,2,10,1))
hwControllerBoardTempEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:hwControllerBoardTempEntry.setStatus(_C)
_HwControllerBoardTempIndex_Type=Integer32
_HwControllerBoardTempIndex_Object=MibTableColumn
hwControllerBoardTempIndex=_HwControllerBoardTempIndex_Object((1,3,6,1,4,1,18928,1,1,2,10,1,1),_HwControllerBoardTempIndex_Type())
hwControllerBoardTempIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardTempIndex.setStatus(_C)
_HwControllerBoardTempDesc_Type=OctetString
_HwControllerBoardTempDesc_Object=MibTableColumn
hwControllerBoardTempDesc=_HwControllerBoardTempDesc_Object((1,3,6,1,4,1,18928,1,1,2,10,1,2),_HwControllerBoardTempDesc_Type())
hwControllerBoardTempDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardTempDesc.setStatus(_C)
class _HwControllerBoardTempValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-128));namedValues=NamedValues(('na',-128))
_HwControllerBoardTempValue_Type.__name__=_E
_HwControllerBoardTempValue_Object=MibTableColumn
hwControllerBoardTempValue=_HwControllerBoardTempValue_Object((1,3,6,1,4,1,18928,1,1,2,10,1,3),_HwControllerBoardTempValue_Type())
hwControllerBoardTempValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hwControllerBoardTempValue.setStatus(_C)
_HddInformation_ObjectIdentity=ObjectIdentity
hddInformation=_HddInformation_ObjectIdentity((1,3,6,1,4,1,18928,1,1,3))
_HddInfoTable_Object=MibTable
hddInfoTable=_HddInfoTable_Object((1,3,6,1,4,1,18928,1,1,3,1))
if mibBuilder.loadTexts:hddInfoTable.setStatus(_C)
_HddInfoEntry_Object=MibTableRow
hddInfoEntry=_HddInfoEntry_Object((1,3,6,1,4,1,18928,1,1,3,1,1))
hddInfoEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:hddInfoEntry.setStatus(_C)
_HddSlots_Type=Integer32
_HddSlots_Object=MibTableColumn
hddSlots=_HddSlots_Object((1,3,6,1,4,1,18928,1,1,3,1,1,1),_HddSlots_Type())
hddSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:hddSlots.setStatus(_C)
_HddName_Type=OctetString
_HddName_Object=MibTableColumn
hddName=_HddName_Object((1,3,6,1,4,1,18928,1,1,3,1,1,2),_HddName_Type())
hddName.setMaxAccess(_D)
if mibBuilder.loadTexts:hddName.setStatus(_C)
_HddSerial_Type=OctetString
_HddSerial_Object=MibTableColumn
hddSerial=_HddSerial_Object((1,3,6,1,4,1,18928,1,1,3,1,1,3),_HddSerial_Type())
hddSerial.setMaxAccess(_D)
if mibBuilder.loadTexts:hddSerial.setStatus(_C)
_HddFirmVer_Type=OctetString
_HddFirmVer_Object=MibTableColumn
hddFirmVer=_HddFirmVer_Object((1,3,6,1,4,1,18928,1,1,3,1,1,4),_HddFirmVer_Type())
hddFirmVer.setMaxAccess(_D)
if mibBuilder.loadTexts:hddFirmVer.setStatus(_C)
_HddCapacity_Type=Integer32
_HddCapacity_Object=MibTableColumn
hddCapacity=_HddCapacity_Object((1,3,6,1,4,1,18928,1,1,3,1,1,5),_HddCapacity_Type())
hddCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:hddCapacity.setStatus(_C)
_HddPio_Type=Integer32
_HddPio_Object=MibTableColumn
hddPio=_HddPio_Object((1,3,6,1,4,1,18928,1,1,3,1,1,6),_HddPio_Type())
hddPio.setMaxAccess(_D)
if mibBuilder.loadTexts:hddPio.setStatus(_C)
_HddCudma_Type=Integer32
_HddCudma_Object=MibTableColumn
hddCudma=_HddCudma_Object((1,3,6,1,4,1,18928,1,1,3,1,1,7),_HddCudma_Type())
hddCudma.setMaxAccess(_D)
if mibBuilder.loadTexts:hddCudma.setStatus(_C)
_HddSudma_Type=Integer32
_HddSudma_Object=MibTableColumn
hddSudma=_HddSudma_Object((1,3,6,1,4,1,18928,1,1,3,1,1,8),_HddSudma_Type())
hddSudma.setMaxAccess(_D)
if mibBuilder.loadTexts:hddSudma.setStatus(_C)
_HddState_Type=OctetString
_HddState_Object=MibTableColumn
hddState=_HddState_Object((1,3,6,1,4,1,18928,1,1,3,1,1,9),_HddState_Type())
hddState.setMaxAccess(_D)
if mibBuilder.loadTexts:hddState.setStatus(_C)
_RaidsetInformation_ObjectIdentity=ObjectIdentity
raidsetInformation=_RaidsetInformation_ObjectIdentity((1,3,6,1,4,1,18928,1,1,4))
_RaidInfoTable_Object=MibTable
raidInfoTable=_RaidInfoTable_Object((1,3,6,1,4,1,18928,1,1,4,1))
if mibBuilder.loadTexts:raidInfoTable.setStatus(_C)
_RaidInfoEntry_Object=MibTableRow
raidInfoEntry=_RaidInfoEntry_Object((1,3,6,1,4,1,18928,1,1,4,1,1))
raidInfoEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:raidInfoEntry.setStatus(_C)
_RaidNumber_Type=Integer32
_RaidNumber_Object=MibTableColumn
raidNumber=_RaidNumber_Object((1,3,6,1,4,1,18928,1,1,4,1,1,1),_RaidNumber_Type())
raidNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:raidNumber.setStatus(_C)
_RaidName_Type=OctetString
_RaidName_Object=MibTableColumn
raidName=_RaidName_Object((1,3,6,1,4,1,18928,1,1,4,1,1,2),_RaidName_Type())
raidName.setMaxAccess(_D)
if mibBuilder.loadTexts:raidName.setStatus(_C)
_RaidDisks_Type=Integer32
_RaidDisks_Object=MibTableColumn
raidDisks=_RaidDisks_Object((1,3,6,1,4,1,18928,1,1,4,1,1,3),_RaidDisks_Type())
raidDisks.setMaxAccess(_D)
if mibBuilder.loadTexts:raidDisks.setStatus(_C)
_RaidState_Type=OctetString
_RaidState_Object=MibTableColumn
raidState=_RaidState_Object((1,3,6,1,4,1,18928,1,1,4,1,1,4),_RaidState_Type())
raidState.setMaxAccess(_D)
if mibBuilder.loadTexts:raidState.setStatus(_C)
_RaidTotalCapacity_Type=Integer32
_RaidTotalCapacity_Object=MibTableColumn
raidTotalCapacity=_RaidTotalCapacity_Object((1,3,6,1,4,1,18928,1,1,4,1,1,5),_RaidTotalCapacity_Type())
raidTotalCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:raidTotalCapacity.setStatus(_C)
_RaidFreeCapacity_Type=Integer32
_RaidFreeCapacity_Object=MibTableColumn
raidFreeCapacity=_RaidFreeCapacity_Object((1,3,6,1,4,1,18928,1,1,4,1,1,6),_RaidFreeCapacity_Type())
raidFreeCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:raidFreeCapacity.setStatus(_C)
_RaidMemberDiskCapacity_Type=Integer32
_RaidMemberDiskCapacity_Object=MibTableColumn
raidMemberDiskCapacity=_RaidMemberDiskCapacity_Object((1,3,6,1,4,1,18928,1,1,4,1,1,7),_RaidMemberDiskCapacity_Type())
raidMemberDiskCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:raidMemberDiskCapacity.setStatus(_C)
_RaidMemberDiskChannels_Type=OctetString
_RaidMemberDiskChannels_Object=MibTableColumn
raidMemberDiskChannels=_RaidMemberDiskChannels_Object((1,3,6,1,4,1,18928,1,1,4,1,1,8),_RaidMemberDiskChannels_Type())
raidMemberDiskChannels.setMaxAccess(_D)
if mibBuilder.loadTexts:raidMemberDiskChannels.setStatus(_C)
_VolumesetInformation_ObjectIdentity=ObjectIdentity
volumesetInformation=_VolumesetInformation_ObjectIdentity((1,3,6,1,4,1,18928,1,1,5))
_VolInfoTable_Object=MibTable
volInfoTable=_VolInfoTable_Object((1,3,6,1,4,1,18928,1,1,5,1))
if mibBuilder.loadTexts:volInfoTable.setStatus(_C)
_VolInfoEntry_Object=MibTableRow
volInfoEntry=_VolInfoEntry_Object((1,3,6,1,4,1,18928,1,1,5,1,1))
volInfoEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:volInfoEntry.setStatus(_C)
_VolNumber_Type=Integer32
_VolNumber_Object=MibTableColumn
volNumber=_VolNumber_Object((1,3,6,1,4,1,18928,1,1,5,1,1,1),_VolNumber_Type())
volNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:volNumber.setStatus(_C)
_VolName_Type=OctetString
_VolName_Object=MibTableColumn
volName=_VolName_Object((1,3,6,1,4,1,18928,1,1,5,1,1,2),_VolName_Type())
volName.setMaxAccess(_D)
if mibBuilder.loadTexts:volName.setStatus(_C)
_VolRaidName_Type=OctetString
_VolRaidName_Object=MibTableColumn
volRaidName=_VolRaidName_Object((1,3,6,1,4,1,18928,1,1,5,1,1,3),_VolRaidName_Type())
volRaidName.setMaxAccess(_D)
if mibBuilder.loadTexts:volRaidName.setStatus(_C)
_VolCapacity_Type=Integer32
_VolCapacity_Object=MibTableColumn
volCapacity=_VolCapacity_Object((1,3,6,1,4,1,18928,1,1,5,1,1,4),_VolCapacity_Type())
volCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:volCapacity.setStatus(_C)
_VolState_Type=OctetString
_VolState_Object=MibTableColumn
volState=_VolState_Object((1,3,6,1,4,1,18928,1,1,5,1,1,5),_VolState_Type())
volState.setMaxAccess(_D)
if mibBuilder.loadTexts:volState.setStatus(_C)
_VolProgress_Type=Integer32
_VolProgress_Object=MibTableColumn
volProgress=_VolProgress_Object((1,3,6,1,4,1,18928,1,1,5,1,1,6),_VolProgress_Type())
volProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:volProgress.setStatus(_C)
_VolCluster_Type=Integer32
_VolCluster_Object=MibTableColumn
volCluster=_VolCluster_Object((1,3,6,1,4,1,18928,1,1,5,1,1,7),_VolCluster_Type())
volCluster.setMaxAccess(_D)
if mibBuilder.loadTexts:volCluster.setStatus(_C)
_VolChannel_Type=Integer32
_VolChannel_Object=MibTableColumn
volChannel=_VolChannel_Object((1,3,6,1,4,1,18928,1,1,5,1,1,8),_VolChannel_Type())
volChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:volChannel.setStatus(_C)
_VolSCSIID_Type=Integer32
_VolSCSIID_Object=MibTableColumn
volSCSIID=_VolSCSIID_Object((1,3,6,1,4,1,18928,1,1,5,1,1,9),_VolSCSIID_Type())
volSCSIID.setMaxAccess(_D)
if mibBuilder.loadTexts:volSCSIID.setStatus(_C)
_VolSCSILUN_Type=Integer32
_VolSCSILUN_Object=MibTableColumn
volSCSILUN=_VolSCSILUN_Object((1,3,6,1,4,1,18928,1,1,5,1,1,10),_VolSCSILUN_Type())
volSCSILUN.setMaxAccess(_D)
if mibBuilder.loadTexts:volSCSILUN.setStatus(_C)
_VolRaidLevel_Type=Integer32
_VolRaidLevel_Object=MibTableColumn
volRaidLevel=_VolRaidLevel_Object((1,3,6,1,4,1,18928,1,1,5,1,1,11),_VolRaidLevel_Type())
volRaidLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:volRaidLevel.setStatus(_C)
class _VolStripes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4096,8192,16384,32768,65536,131072)));namedValues=NamedValues(*(('s4K',4096),('s8K',8192),('s16K',16384),(_F,32768),('s64K',65536),('s128K',131072)))
_VolStripes_Type.__name__=_E
_VolStripes_Object=MibTableColumn
volStripes=_VolStripes_Object((1,3,6,1,4,1,18928,1,1,5,1,1,12),_VolStripes_Type())
volStripes.setMaxAccess(_D)
if mibBuilder.loadTexts:volStripes.setStatus(_C)
_VolDisks_Type=Integer32
_VolDisks_Object=MibTableColumn
volDisks=_VolDisks_Object((1,3,6,1,4,1,18928,1,1,5,1,1,13),_VolDisks_Type())
volDisks.setMaxAccess(_D)
if mibBuilder.loadTexts:volDisks.setStatus(_C)
class _VolCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('write-through',0),('write-back',1)))
_VolCache_Type.__name__=_E
_VolCache_Object=MibTableColumn
volCache=_VolCache_Object((1,3,6,1,4,1,18928,1,1,5,1,1,14),_VolCache_Type())
volCache.setMaxAccess(_D)
if mibBuilder.loadTexts:volCache.setStatus(_C)
class _VolTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_VolTag_Type.__name__=_E
_VolTag_Object=MibTableColumn
volTag=_VolTag_Object((1,3,6,1,4,1,18928,1,1,5,1,1,15),_VolTag_Type())
volTag.setMaxAccess(_D)
if mibBuilder.loadTexts:volTag.setStatus(_C)
_VolMaxSpeed_Type=OctetString
_VolMaxSpeed_Object=MibTableColumn
volMaxSpeed=_VolMaxSpeed_Object((1,3,6,1,4,1,18928,1,1,5,1,1,16),_VolMaxSpeed_Type())
volMaxSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:volMaxSpeed.setStatus(_C)
_VolCurrentSpeed_Type=OctetString
_VolCurrentSpeed_Object=MibTableColumn
volCurrentSpeed=_VolCurrentSpeed_Object((1,3,6,1,4,1,18928,1,1,5,1,1,17),_VolCurrentSpeed_Type())
volCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:volCurrentSpeed.setStatus(_C)
_EventInformation_ObjectIdentity=ObjectIdentity
eventInformation=_EventInformation_ObjectIdentity((1,3,6,1,4,1,18928,1,1,6))
_EventInfoTable_Object=MibTable
eventInfoTable=_EventInfoTable_Object((1,3,6,1,4,1,18928,1,1,6,1))
if mibBuilder.loadTexts:eventInfoTable.setStatus(_C)
_EventInfoEntry_Object=MibTableRow
eventInfoEntry=_EventInfoEntry_Object((1,3,6,1,4,1,18928,1,1,6,1,1))
eventInfoEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:eventInfoEntry.setStatus(_C)
_EventNumber_Type=Integer32
_EventNumber_Object=MibTableColumn
eventNumber=_EventNumber_Object((1,3,6,1,4,1,18928,1,1,6,1,1,1),_EventNumber_Type())
eventNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:eventNumber.setStatus(_C)
_EventString_Type=OctetString
_EventString_Object=MibTableColumn
eventString=_EventString_Object((1,3,6,1,4,1,18928,1,1,6,1,1,2),_EventString_Type())
eventString.setMaxAccess(_D)
if mibBuilder.loadTexts:eventString.setStatus(_C)
_RaidSubSysTraps_ObjectIdentity=ObjectIdentity
raidSubSysTraps=_RaidSubSysTraps_ObjectIdentity((1,3,6,1,4,1,18928,1,1,7))
rsCreate=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,128))
rsCreate.setObjects((_A,_B))
if mibBuilder.loadTexts:rsCreate.setStatus('')
rsDelete=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,129))
rsDelete.setObjects((_A,_B))
if mibBuilder.loadTexts:rsDelete.setStatus('')
rsExpand=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,130))
rsExpand.setObjects((_A,_B))
if mibBuilder.loadTexts:rsExpand.setStatus('')
rsRebuild=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,131))
rsRebuild.setObjects((_A,_B))
if mibBuilder.loadTexts:rsRebuild.setStatus('')
rsDegraded=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,132))
rsDegraded.setObjects((_A,_B))
if mibBuilder.loadTexts:rsDegraded.setStatus('')
rsNoEvent=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,133))
rsNoEvent.setObjects((_A,_B))
if mibBuilder.loadTexts:rsNoEvent.setStatus('')
vsInitializing=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,256))
vsInitializing.setObjects((_A,_B))
if mibBuilder.loadTexts:vsInitializing.setStatus('')
vsRebuilding=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,257))
vsRebuilding.setObjects((_A,_B))
if mibBuilder.loadTexts:vsRebuilding.setStatus('')
vsMigrating=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,258))
vsMigrating.setObjects((_A,_B))
if mibBuilder.loadTexts:vsMigrating.setStatus('')
vsChecking=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,259))
vsChecking.setObjects((_A,_B))
if mibBuilder.loadTexts:vsChecking.setStatus('')
vsCompleteInit=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,260))
vsCompleteInit.setObjects((_A,_B))
if mibBuilder.loadTexts:vsCompleteInit.setStatus('')
vsCompleteRebuild=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,261))
vsCompleteRebuild.setObjects((_A,_B))
if mibBuilder.loadTexts:vsCompleteRebuild.setStatus('')
vsCompleteMigrating=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,262))
vsCompleteMigrating.setObjects((_A,_B))
if mibBuilder.loadTexts:vsCompleteMigrating.setStatus('')
vsCompleteChecking=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,263))
vsCompleteChecking.setObjects((_A,_B))
if mibBuilder.loadTexts:vsCompleteChecking.setStatus('')
vsCreate=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,264))
vsCreate.setObjects((_A,_B))
if mibBuilder.loadTexts:vsCreate.setStatus('')
vsDelete=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,265))
vsDelete.setObjects((_A,_B))
if mibBuilder.loadTexts:vsDelete.setStatus('')
vsModify=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,266))
vsModify.setObjects((_A,_B))
if mibBuilder.loadTexts:vsModify.setStatus('')
vsDegraded=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,267))
vsDegraded.setObjects((_A,_B))
if mibBuilder.loadTexts:vsDegraded.setStatus('')
vsFailed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,268))
vsFailed.setObjects((_A,_B))
if mibBuilder.loadTexts:vsFailed.setStatus('')
vsRevived=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,269))
vsRevived.setObjects((_A,_B))
if mibBuilder.loadTexts:vsRevived.setStatus('')
vsTotals=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,270))
vsTotals.setObjects((_A,_B))
if mibBuilder.loadTexts:vsTotals.setStatus('')
pdAdded=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,384))
pdAdded.setObjects((_A,_B))
if mibBuilder.loadTexts:pdAdded.setStatus('')
pdRemoved=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,385))
pdRemoved.setObjects((_A,_B))
if mibBuilder.loadTexts:pdRemoved.setStatus('')
pdReadError=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,386))
pdReadError.setObjects((_A,_B))
if mibBuilder.loadTexts:pdReadError.setStatus('')
pdWriteError=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,387))
pdWriteError.setObjects((_A,_B))
if mibBuilder.loadTexts:pdWriteError.setStatus('')
pdAtaEccError=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,388))
pdAtaEccError.setObjects((_A,_B))
if mibBuilder.loadTexts:pdAtaEccError.setStatus('')
pdAtaChangeMode=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,389))
pdAtaChangeMode.setObjects((_A,_B))
if mibBuilder.loadTexts:pdAtaChangeMode.setStatus('')
pdTimeOut=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,390))
pdTimeOut.setObjects((_A,_B))
if mibBuilder.loadTexts:pdTimeOut.setStatus('')
pdMarkFailed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,391))
pdMarkFailed.setObjects((_A,_B))
if mibBuilder.loadTexts:pdMarkFailed.setStatus('')
pdPciError=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,392))
pdPciError.setObjects((_A,_B))
if mibBuilder.loadTexts:pdPciError.setStatus('')
pdSmartFailed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,393))
pdSmartFailed.setObjects((_A,_B))
if mibBuilder.loadTexts:pdSmartFailed.setStatus('')
pdCreatePass=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,394))
pdCreatePass.setObjects((_A,_B))
if mibBuilder.loadTexts:pdCreatePass.setStatus('')
pdModifyPass=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,395))
pdModifyPass.setObjects((_A,_B))
if mibBuilder.loadTexts:pdModifyPass.setStatus('')
pdDeletePass=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,396))
pdDeletePass.setObjects((_A,_B))
if mibBuilder.loadTexts:pdDeletePass.setStatus('')
pdTotals=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,397))
pdTotals.setObjects((_A,_B))
if mibBuilder.loadTexts:pdTotals.setStatus('')
scsiReset=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,512))
scsiReset.setObjects((_A,_B))
if mibBuilder.loadTexts:scsiReset.setStatus('')
scsiParity=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,513))
scsiParity.setObjects((_A,_B))
if mibBuilder.loadTexts:scsiParity.setStatus('')
scsiModeChange=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,514))
scsiModeChange.setObjects((_A,_B))
if mibBuilder.loadTexts:scsiModeChange.setStatus('')
scsiTotals=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,515))
scsiTotals.setObjects((_A,_B))
if mibBuilder.loadTexts:scsiTotals.setStatus('')
hwSdram1BitEcc=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,640))
hwSdram1BitEcc.setObjects((_A,_B))
if mibBuilder.loadTexts:hwSdram1BitEcc.setStatus('')
hwSdramMultiBitEcc=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,641))
hwSdramMultiBitEcc.setObjects((_A,_B))
if mibBuilder.loadTexts:hwSdramMultiBitEcc.setStatus('')
hwTempController=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,642))
hwTempController.setObjects((_A,_B))
if mibBuilder.loadTexts:hwTempController.setStatus('')
hwTempBackplane=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,643))
hwTempBackplane.setObjects((_A,_B))
if mibBuilder.loadTexts:hwTempBackplane.setStatus('')
hwVoltage15=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,644))
hwVoltage15.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage15.setStatus('')
hwVoltage3=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,645))
hwVoltage3.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage3.setStatus('')
hwVoltage5=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,646))
hwVoltage5.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage5.setStatus('')
hwVoltage12=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,647))
hwVoltage12.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage12.setStatus('')
hwVoltage13=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,648))
hwVoltage13.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage13.setStatus('')
hwVoltage25=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,649))
hwVoltage25.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage25.setStatus('')
hwVoltage125=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,650))
hwVoltage125.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage125.setStatus('')
hwPower1Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,651))
hwPower1Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower1Failed.setStatus('')
hwFan1Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,652))
hwFan1Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan1Failed.setStatus('')
hwPower2Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,653))
hwPower2Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower2Failed.setStatus('')
hwFan2Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,654))
hwFan2Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan2Failed.setStatus('')
hwPower3Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,655))
hwPower3Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower3Failed.setStatus('')
hwFan3Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,656))
hwFan3Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan3Failed.setStatus('')
hwPower4Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,657))
hwPower4Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower4Failed.setStatus('')
hwFan4Failed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,658))
hwFan4Failed.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan4Failed.setStatus('')
hwUpsPowerLoss=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,659))
hwUpsPowerLoss.setObjects((_A,_B))
if mibBuilder.loadTexts:hwUpsPowerLoss.setStatus('')
hwTempControllerR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,660))
hwTempControllerR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwTempControllerR.setStatus('')
hwTempBackplaneR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,661))
hwTempBackplaneR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwTempBackplaneR.setStatus('')
hwVoltage15R=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,662))
hwVoltage15R.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage15R.setStatus('')
hwVoltage3R=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,663))
hwVoltage3R.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage3R.setStatus('')
hwVoltage5R=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,664))
hwVoltage5R.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage5R.setStatus('')
hwVoltage12R=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,665))
hwVoltage12R.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage12R.setStatus('')
hwVoltage13R=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,666))
hwVoltage13R.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage13R.setStatus('')
hwVoltage25R=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,667))
hwVoltage25R.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage25R.setStatus('')
hwVoltage125R=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,668))
hwVoltage125R.setObjects((_A,_B))
if mibBuilder.loadTexts:hwVoltage125R.setStatus('')
hwPower1FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,669))
hwPower1FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower1FailedR.setStatus('')
hwFan1FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,670))
hwFan1FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan1FailedR.setStatus('')
hwPower2FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,671))
hwPower2FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower2FailedR.setStatus('')
hwFan2FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,672))
hwFan2FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan2FailedR.setStatus('')
hwPower3FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,673))
hwPower3FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower3FailedR.setStatus('')
hwFan3FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,674))
hwFan3FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan3FailedR.setStatus('')
hwPower4FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,675))
hwPower4FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwPower4FailedR.setStatus('')
hwFan4FailedR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,676))
hwFan4FailedR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwFan4FailedR.setStatus('')
hwUPSPowerR=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,677))
hwUPSPowerR.setObjects((_A,_B))
if mibBuilder.loadTexts:hwUPSPowerR.setStatus('')
hwSystemRestarted=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,678))
hwSystemRestarted.setObjects((_A,_B))
if mibBuilder.loadTexts:hwSystemRestarted.setStatus('')
hwTest=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,679))
hwTest.setObjects((_A,_B))
if mibBuilder.loadTexts:hwTest.setStatus('')
hwSystemRecovered=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,680))
hwSystemRecovered.setObjects((_A,_B))
if mibBuilder.loadTexts:hwSystemRecovered.setStatus('')
ghmRecover=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,768))
ghmRecover.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmRecover.setStatus('')
ghmOverTemp=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,769))
ghmOverTemp.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmOverTemp.setStatus('')
ghmFailed=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,770))
ghmFailed.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmFailed.setStatus('')
ghmUnderVoltage=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,771))
ghmUnderVoltage.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmUnderVoltage.setStatus('')
ghmOverVoltage=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,772))
ghmOverVoltage.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmOverVoltage.setStatus('')
ghmDiscovered=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,773))
ghmDiscovered.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmDiscovered.setStatus('')
ghmLostMig=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,774))
ghmLostMig.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmLostMig.setStatus('')
ghmRestartLBA=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,775))
ghmRestartLBA.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmRestartLBA.setStatus('')
ghmHTTPLogin=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,776))
ghmHTTPLogin.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmHTTPLogin.setStatus('')
ghmTelnetLogin=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,777))
ghmTelnetLogin.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmTelnetLogin.setStatus('')
ghmVt100Login=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,778))
ghmVt100Login.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmVt100Login.setStatus('')
ghmGUILogin=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,779))
ghmGUILogin.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmGUILogin.setStatus('')
ghmFCLinkUp=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,780))
ghmFCLinkUp.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmFCLinkUp.setStatus('')
ghmFCLinkDown=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,781))
ghmFCLinkDown.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmFCLinkDown.setStatus('')
ghm16BytesCDB=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,782))
ghm16BytesCDB.setObjects((_A,_B))
if mibBuilder.loadTexts:ghm16BytesCDB.setStatus('')
ghmInitLBA=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,783))
ghmInitLBA.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmInitLBA.setStatus('')
ghmRebuildLBA=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,784))
ghmRebuildLBA.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmRebuildLBA.setStatus('')
ghmMigrateLBA=NotificationType((1,3,6,1,4,1,18928,1,1,7,0,785))
ghmMigrateLBA.setObjects((_A,_B))
if mibBuilder.loadTexts:ghmMigrateLBA.setStatus('')
mibBuilder.exportSymbols(_A,**{'areca':areca,'arecaGroup1':arecaGroup1,'sataRaidCard1':sataRaidCard1,'systemInformation':systemInformation,'siVendor':siVendor,'siModel':siModel,'siSerial':siSerial,'siFirmVer':siFirmVer,'siBootVer':siBootVer,'siMbrVer':siMbrVer,'siProcessor':siProcessor,'siCpuSpeed':siCpuSpeed,'siICache':siICache,'siDCache':siDCache,'siSCache':siSCache,'siMemory':siMemory,'siMemSpeed':siMemSpeed,'siEcc':siEcc,'siHosts':siHosts,'siHddSlots':siHddSlots,'siRaidSets':siRaidSets,'siVolumeSets':siVolumeSets,'siEvents':siEvents,'siFans':siFans,'siPowers':siPowers,'siRaid6':siRaid6,'siDhcp':siDhcp,'siBeeper':siBeeper,'siUsage':siUsage,'siMaxATA':siMaxATA,'siRebuildRate':siRebuildRate,'siBaudRate':siBaudRate,'hwMonitor':hwMonitor,'hwControllerBoardInstalled':hwControllerBoardInstalled,'hwControllerBoardDescription':hwControllerBoardDescription,'hwControllerBoardNumberOfPower':hwControllerBoardNumberOfPower,'hwControllerBoardNumberOfVol':hwControllerBoardNumberOfVol,'hwControllerBoardNumberOfFan':hwControllerBoardNumberOfFan,'hwControllerBoardNumberOfTemp':hwControllerBoardNumberOfTemp,'hwControllerBoardPowerTable':hwControllerBoardPowerTable,'hwControllerBoardPowerEntry':hwControllerBoardPowerEntry,_K:hwControllerBoardPowerIndex,'hwControllerBoardPowerDesc':hwControllerBoardPowerDesc,'hwControllerBoardPowerState':hwControllerBoardPowerState,'hwControllerBoardVolTable':hwControllerBoardVolTable,'hwControllerBoardVolEntry':hwControllerBoardVolEntry,_L:hwControllerBoardVolIndex,'hwControllerBoardVolDesc':hwControllerBoardVolDesc,'hwControllerBoardVolValue':hwControllerBoardVolValue,'hwControllerBoardFanTable':hwControllerBoardFanTable,'hwControllerBoardFanEntry':hwControllerBoardFanEntry,_M:hwControllerBoardFanIndex,'hwControllerBoardFanDesc':hwControllerBoardFanDesc,'hwControllerBoardFanSpeed':hwControllerBoardFanSpeed,'hwControllerBoardTempTable':hwControllerBoardTempTable,'hwControllerBoardTempEntry':hwControllerBoardTempEntry,_N:hwControllerBoardTempIndex,'hwControllerBoardTempDesc':hwControllerBoardTempDesc,'hwControllerBoardTempValue':hwControllerBoardTempValue,'hddInformation':hddInformation,'hddInfoTable':hddInfoTable,'hddInfoEntry':hddInfoEntry,_O:hddSlots,'hddName':hddName,'hddSerial':hddSerial,'hddFirmVer':hddFirmVer,'hddCapacity':hddCapacity,'hddPio':hddPio,'hddCudma':hddCudma,'hddSudma':hddSudma,'hddState':hddState,'raidsetInformation':raidsetInformation,'raidInfoTable':raidInfoTable,'raidInfoEntry':raidInfoEntry,_P:raidNumber,'raidName':raidName,'raidDisks':raidDisks,'raidState':raidState,'raidTotalCapacity':raidTotalCapacity,'raidFreeCapacity':raidFreeCapacity,'raidMemberDiskCapacity':raidMemberDiskCapacity,'raidMemberDiskChannels':raidMemberDiskChannels,'volumesetInformation':volumesetInformation,'volInfoTable':volInfoTable,'volInfoEntry':volInfoEntry,_Q:volNumber,'volName':volName,'volRaidName':volRaidName,'volCapacity':volCapacity,'volState':volState,'volProgress':volProgress,'volCluster':volCluster,'volChannel':volChannel,'volSCSIID':volSCSIID,'volSCSILUN':volSCSILUN,'volRaidLevel':volRaidLevel,'volStripes':volStripes,'volDisks':volDisks,'volCache':volCache,'volTag':volTag,'volMaxSpeed':volMaxSpeed,'volCurrentSpeed':volCurrentSpeed,'eventInformation':eventInformation,'eventInfoTable':eventInfoTable,'eventInfoEntry':eventInfoEntry,_R:eventNumber,_B:eventString,'raidSubSysTraps':raidSubSysTraps,'rsCreate':rsCreate,'rsDelete':rsDelete,'rsExpand':rsExpand,'rsRebuild':rsRebuild,'rsDegraded':rsDegraded,'rsNoEvent':rsNoEvent,'vsInitializing':vsInitializing,'vsRebuilding':vsRebuilding,'vsMigrating':vsMigrating,'vsChecking':vsChecking,'vsCompleteInit':vsCompleteInit,'vsCompleteRebuild':vsCompleteRebuild,'vsCompleteMigrating':vsCompleteMigrating,'vsCompleteChecking':vsCompleteChecking,'vsCreate':vsCreate,'vsDelete':vsDelete,'vsModify':vsModify,'vsDegraded':vsDegraded,'vsFailed':vsFailed,'vsRevived':vsRevived,'vsTotals':vsTotals,'pdAdded':pdAdded,'pdRemoved':pdRemoved,'pdReadError':pdReadError,'pdWriteError':pdWriteError,'pdAtaEccError':pdAtaEccError,'pdAtaChangeMode':pdAtaChangeMode,'pdTimeOut':pdTimeOut,'pdMarkFailed':pdMarkFailed,'pdPciError':pdPciError,'pdSmartFailed':pdSmartFailed,'pdCreatePass':pdCreatePass,'pdModifyPass':pdModifyPass,'pdDeletePass':pdDeletePass,'pdTotals':pdTotals,'scsiReset':scsiReset,'scsiParity':scsiParity,'scsiModeChange':scsiModeChange,'scsiTotals':scsiTotals,'hwSdram1BitEcc':hwSdram1BitEcc,'hwSdramMultiBitEcc':hwSdramMultiBitEcc,'hwTempController':hwTempController,'hwTempBackplane':hwTempBackplane,'hwVoltage15':hwVoltage15,'hwVoltage3':hwVoltage3,'hwVoltage5':hwVoltage5,'hwVoltage12':hwVoltage12,'hwVoltage13':hwVoltage13,'hwVoltage25':hwVoltage25,'hwVoltage125':hwVoltage125,'hwPower1Failed':hwPower1Failed,'hwFan1Failed':hwFan1Failed,'hwPower2Failed':hwPower2Failed,'hwFan2Failed':hwFan2Failed,'hwPower3Failed':hwPower3Failed,'hwFan3Failed':hwFan3Failed,'hwPower4Failed':hwPower4Failed,'hwFan4Failed':hwFan4Failed,'hwUpsPowerLoss':hwUpsPowerLoss,'hwTempControllerR':hwTempControllerR,'hwTempBackplaneR':hwTempBackplaneR,'hwVoltage15R':hwVoltage15R,'hwVoltage3R':hwVoltage3R,'hwVoltage5R':hwVoltage5R,'hwVoltage12R':hwVoltage12R,'hwVoltage13R':hwVoltage13R,'hwVoltage25R':hwVoltage25R,'hwVoltage125R':hwVoltage125R,'hwPower1FailedR':hwPower1FailedR,'hwFan1FailedR':hwFan1FailedR,'hwPower2FailedR':hwPower2FailedR,'hwFan2FailedR':hwFan2FailedR,'hwPower3FailedR':hwPower3FailedR,'hwFan3FailedR':hwFan3FailedR,'hwPower4FailedR':hwPower4FailedR,'hwFan4FailedR':hwFan4FailedR,'hwUPSPowerR':hwUPSPowerR,'hwSystemRestarted':hwSystemRestarted,'hwTest':hwTest,'hwSystemRecovered':hwSystemRecovered,'ghmRecover':ghmRecover,'ghmOverTemp':ghmOverTemp,'ghmFailed':ghmFailed,'ghmUnderVoltage':ghmUnderVoltage,'ghmOverVoltage':ghmOverVoltage,'ghmDiscovered':ghmDiscovered,'ghmLostMig':ghmLostMig,'ghmRestartLBA':ghmRestartLBA,'ghmHTTPLogin':ghmHTTPLogin,'ghmTelnetLogin':ghmTelnetLogin,'ghmVt100Login':ghmVt100Login,'ghmGUILogin':ghmGUILogin,'ghmFCLinkUp':ghmFCLinkUp,'ghmFCLinkDown':ghmFCLinkDown,'ghm16BytesCDB':ghm16BytesCDB,'ghmInitLBA':ghmInitLBA,'ghmRebuildLBA':ghmRebuildLBA,'ghmMigrateLBA':ghmMigrateLBA})