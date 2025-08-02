_AK='mbgRSC180TrapsGroup'
_AJ='mbgRSC180ObjectsGroup'
_AI='mbgTestNotificationTrap'
_AH='mbgHighTempTrap'
_AG='mbgPowerSupplyOKTrap'
_AF='mbgPowerSupplyFailureTrap'
_AE='mbgMasterclockSwitchoverTrap'
_AD='mbgLeapSecondAnnouncedTrap'
_AC='mbgSCUBootTrap'
_AB='mbgGPSAntennaReconnectTrap'
_AA='mbgGPSAntennaFaultyTrap'
_A9='mbgGPSReceiverNotSyncTrap'
_A8='mbgGPSReceiverNotRespondingTrap'
_A7='mbgGPSNavSolvedTrap'
_A6='mbgWarmBootTrap'
_A5='mbgColdBootTrap'
_A4='mbgSCUDum1'
_A3='mbgSCUAutoManual'
_A2='mbgSCUtimeDiff'
_A1='mbgSCUSupl4'
_A0='mbgSCUSupl3'
_z='mbgSCUSupl2'
_y='mbgSCUSupl1'
_x='mbgSCUInp2'
_w='mbgSCUInp1'
_v='mbgSCUOutp16'
_u='mbgSCUOutp15'
_t='mbgSCUOutp14'
_s='mbgSCUOutp13'
_r='mbgSCUOutp12'
_q='mbgSCUOutp11'
_p='mbgSCUOutp10'
_o='mbgSCUOutp9'
_n='mbgSCUOutp8'
_m='mbgSCUOutp7'
_l='mbgSCUOutp6'
_k='mbgSCUOutp5'
_j='mbgSCUOutp4'
_i='mbgSCUOutp3'
_h='mbgSCUOutp2'
_g='mbgSCUOutp1'
_f='mbgSCUTemp'
_e='mbgSCUPowerSupply2'
_d='mbgSCUPowerSupply1'
_c='mbgSCUACOMode'
_b='mbgSCUOutputStatus'
_a='mbgSCUSyncStatusClk2'
_Z='mbgSCUSyncStatusClk1'
_Y='mbgTrapIPAddress'
_X='mbgSCULocalRemote'
_W='mbgSCUMasterVal'
_V='mbgSCUFirmwareRev'
_U='mbgSCUSerialNo'
_T='mbgSCUType'
_S='mbgLeapSecond'
_R='mbgGPSNavSolved'
_Q='mbgGpsSatellitesInView'
_P='mbgGpsSatellitesGood'
_O='mbgGpsPosition'
_N='mbgGpsState'
_M='mbgClkMode'
_L='mbgClkFirmwareRev'
_K='mbgClkSerialNo'
_J='mbgClkType'
_I='notSync'
_H='MeinbergRefClockTyp'
_G='mbgClkTableIndex'
_F='read-write'
_E='notAvailable'
_D='Integer32'
_C='read-only'
_B='MBG-SNMP-RSC180-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mbgSnmpRoot,=mibBuilder.importSymbols('MBG-SNMP-ROOT-MIB','mbgSnmpRoot')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mbgRSC180=ModuleIdentity((1,3,6,1,4,1,5597,80))
if mibBuilder.loadTexts:mbgRSC180.setRevisions(('2012-01-25 00:00','2006-01-20 00:00'))
class MeinbergRefClockTyp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52)));namedValues=NamedValues(*((_E,0),('gps166',1),('gps167',2),('gps167SV',3),('gps167PC',4),('gps167PCI',5),('gps163',6),('gps168PCI',7),('gps161',8),('gps169PCI',9),('tcr167PCI',10),('gps164',11),('gps170PCI',12),('pzf511',13),('gps170',14),('tcr511',15),('am511',16),('msf511',17),('grc170',18),('gps170PEX',19),('gps162',20),('ptp270PEX',21),('frc511PEX',22),('gen170',23),('tcr170PEX',24),('wwvb511',25),('mbg170',26),('jjy511',27),('pzf600',28),('tcr600',29),('gps180',30),('gln170',31),('gps180PEX',32),('tcr180PEX',33),('pzf180PEX',34),('mbg180',35),('msf600',36),('wwvb600',37),('jjy600',38),('gps180HS',39),('gps180AMC',40),('esi180',41),('cpe180',42),('lno180',43),('grc180',44),('liu',45),('dcf600HS',46),('dcf600RS',47),('mri',48),('bpe',49),('gln180pex',50),('n2x',51),('rsc180',52)))
_MbgRefClock_ObjectIdentity=ObjectIdentity
mbgRefClock=_MbgRefClock_ObjectIdentity((1,3,6,1,4,1,5597,80,0))
_MbgRefClockStatus_ObjectIdentity=ObjectIdentity
mbgRefClockStatus=_MbgRefClockStatus_ObjectIdentity((1,3,6,1,4,1,5597,80,0,0))
_MbgRefClockTable_Object=MibTable
mbgRefClockTable=_MbgRefClockTable_Object((1,3,6,1,4,1,5597,80,0,0,1))
if mibBuilder.loadTexts:mbgRefClockTable.setStatus(_A)
_MbgRefClockTableEntry_Object=MibTableRow
mbgRefClockTableEntry=_MbgRefClockTableEntry_Object((1,3,6,1,4,1,5597,80,0,0,1,1))
mbgRefClockTableEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:mbgRefClockTableEntry.setStatus(_A)
_MbgClkTableIndex_Type=Unsigned32
_MbgClkTableIndex_Object=MibTableColumn
mbgClkTableIndex=_MbgClkTableIndex_Object((1,3,6,1,4,1,5597,80,0,0,1,1,1),_MbgClkTableIndex_Type())
mbgClkTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mbgClkTableIndex.setStatus(_A)
class _MbgClkType_Type(MeinbergRefClockTyp):defaultValue=0
_MbgClkType_Type.__name__=_H
_MbgClkType_Object=MibTableColumn
mbgClkType=_MbgClkType_Object((1,3,6,1,4,1,5597,80,0,0,1,1,2),_MbgClkType_Type())
mbgClkType.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgClkType.setStatus(_A)
_MbgClkSerialNo_Type=DisplayString
_MbgClkSerialNo_Object=MibTableColumn
mbgClkSerialNo=_MbgClkSerialNo_Object((1,3,6,1,4,1,5597,80,0,0,1,1,3),_MbgClkSerialNo_Type())
mbgClkSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgClkSerialNo.setStatus(_A)
_MbgClkFirmwareRev_Type=DisplayString
_MbgClkFirmwareRev_Object=MibTableColumn
mbgClkFirmwareRev=_MbgClkFirmwareRev_Object((1,3,6,1,4,1,5597,80,0,0,1,1,4),_MbgClkFirmwareRev_Type())
mbgClkFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgClkFirmwareRev.setStatus(_A)
class _MbgClkMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),('normalOperation',1),('trackingSearching',2),('antennaFaulty',3),('warmBoot',4),('coldBoot',5)))
_MbgClkMode_Type.__name__=_D
_MbgClkMode_Object=MibTableColumn
mbgClkMode=_MbgClkMode_Object((1,3,6,1,4,1,5597,80,0,0,1,1,5),_MbgClkMode_Type())
mbgClkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgClkMode.setStatus(_A)
class _MbgGpsState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('synchronized',1),('notSynchronized',2)))
_MbgGpsState_Type.__name__=_D
_MbgGpsState_Object=MibTableColumn
mbgGpsState=_MbgGpsState_Object((1,3,6,1,4,1,5597,80,0,0,1,1,6),_MbgGpsState_Type())
mbgGpsState.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGpsState.setStatus(_A)
_MbgGpsPosition_Type=DisplayString
_MbgGpsPosition_Object=MibTableColumn
mbgGpsPosition=_MbgGpsPosition_Object((1,3,6,1,4,1,5597,80,0,0,1,1,7),_MbgGpsPosition_Type())
mbgGpsPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGpsPosition.setStatus(_A)
_MbgGpsSatellitesGood_Type=Integer32
_MbgGpsSatellitesGood_Object=MibTableColumn
mbgGpsSatellitesGood=_MbgGpsSatellitesGood_Object((1,3,6,1,4,1,5597,80,0,0,1,1,8),_MbgGpsSatellitesGood_Type())
mbgGpsSatellitesGood.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGpsSatellitesGood.setStatus(_A)
_MbgGpsSatellitesInView_Type=Integer32
_MbgGpsSatellitesInView_Object=MibTableColumn
mbgGpsSatellitesInView=_MbgGpsSatellitesInView_Object((1,3,6,1,4,1,5597,80,0,0,1,1,9),_MbgGpsSatellitesInView_Type())
mbgGpsSatellitesInView.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGpsSatellitesInView.setStatus(_A)
class _MbgGPSNavSolved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_MbgGPSNavSolved_Type.__name__=_D
_MbgGPSNavSolved_Object=MibTableColumn
mbgGPSNavSolved=_MbgGPSNavSolved_Object((1,3,6,1,4,1,5597,80,0,0,1,1,10),_MbgGPSNavSolved_Type())
mbgGPSNavSolved.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGPSNavSolved.setStatus(_A)
_MbgLeapSecond_Type=DisplayString
_MbgLeapSecond_Object=MibTableColumn
mbgLeapSecond=_MbgLeapSecond_Object((1,3,6,1,4,1,5597,80,0,0,1,1,11),_MbgLeapSecond_Type())
mbgLeapSecond.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgLeapSecond.setStatus(_A)
_MbgSCU_ObjectIdentity=ObjectIdentity
mbgSCU=_MbgSCU_ObjectIdentity((1,3,6,1,4,1,5597,80,1))
_MbgSCUType_Type=MeinbergRefClockTyp
_MbgSCUType_Object=MibScalar
mbgSCUType=_MbgSCUType_Object((1,3,6,1,4,1,5597,80,1,1),_MbgSCUType_Type())
mbgSCUType.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUType.setStatus(_A)
_MbgSCUSerialNo_Type=DisplayString
_MbgSCUSerialNo_Object=MibScalar
mbgSCUSerialNo=_MbgSCUSerialNo_Object((1,3,6,1,4,1,5597,80,1,2),_MbgSCUSerialNo_Type())
mbgSCUSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSerialNo.setStatus(_A)
_MbgSCUFirmwareRev_Type=DisplayString
_MbgSCUFirmwareRev_Object=MibScalar
mbgSCUFirmwareRev=_MbgSCUFirmwareRev_Object((1,3,6,1,4,1,5597,80,1,3),_MbgSCUFirmwareRev_Type())
mbgSCUFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUFirmwareRev.setStatus(_A)
class _MbgSCUMasterVal_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noMaster',0),('clk1isMaster',1),('clk2isMaster',2)))
_MbgSCUMasterVal_Type.__name__=_D
_MbgSCUMasterVal_Object=MibScalar
mbgSCUMasterVal=_MbgSCUMasterVal_Object((1,3,6,1,4,1,5597,80,1,4),_MbgSCUMasterVal_Type())
mbgSCUMasterVal.setMaxAccess(_F)
if mibBuilder.loadTexts:mbgSCUMasterVal.setStatus(_A)
class _MbgSCULocalRemote_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('local',0),('remote',1)))
_MbgSCULocalRemote_Type.__name__=_D
_MbgSCULocalRemote_Object=MibScalar
mbgSCULocalRemote=_MbgSCULocalRemote_Object((1,3,6,1,4,1,5597,80,1,5),_MbgSCULocalRemote_Type())
mbgSCULocalRemote.setMaxAccess(_F)
if mibBuilder.loadTexts:mbgSCULocalRemote.setStatus(_A)
_MbgTrapIPAddress_Type=IpAddress
_MbgTrapIPAddress_Object=MibScalar
mbgTrapIPAddress=_MbgTrapIPAddress_Object((1,3,6,1,4,1,5597,80,1,6),_MbgTrapIPAddress_Type())
mbgTrapIPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:mbgTrapIPAddress.setStatus(_A)
class _MbgSCUSyncStatusClk1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('sync',1)))
_MbgSCUSyncStatusClk1_Type.__name__=_D
_MbgSCUSyncStatusClk1_Object=MibScalar
mbgSCUSyncStatusClk1=_MbgSCUSyncStatusClk1_Object((1,3,6,1,4,1,5597,80,1,7),_MbgSCUSyncStatusClk1_Type())
mbgSCUSyncStatusClk1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSyncStatusClk1.setStatus(_A)
class _MbgSCUSyncStatusClk2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('sync',1)))
_MbgSCUSyncStatusClk2_Type.__name__=_D
_MbgSCUSyncStatusClk2_Object=MibScalar
mbgSCUSyncStatusClk2=_MbgSCUSyncStatusClk2_Object((1,3,6,1,4,1,5597,80,1,8),_MbgSCUSyncStatusClk2_Type())
mbgSCUSyncStatusClk2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSyncStatusClk2.setStatus(_A)
class _MbgSCUOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('outputsDisabled',0),('outputsEnabled',1)))
_MbgSCUOutputStatus_Type.__name__=_D
_MbgSCUOutputStatus_Object=MibScalar
mbgSCUOutputStatus=_MbgSCUOutputStatus_Object((1,3,6,1,4,1,5597,80,1,9),_MbgSCUOutputStatus_Type())
mbgSCUOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutputStatus.setStatus(_A)
class _MbgSCUACOMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('acoModeOFF',0),('acoModeON',1)))
_MbgSCUACOMode_Type.__name__=_D
_MbgSCUACOMode_Object=MibScalar
mbgSCUACOMode=_MbgSCUACOMode_Object((1,3,6,1,4,1,5597,80,1,10),_MbgSCUACOMode_Type())
mbgSCUACOMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUACOMode.setStatus(_A)
class _MbgSCUPowerSupply1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notOK',0),('ok',1)))
_MbgSCUPowerSupply1_Type.__name__=_D
_MbgSCUPowerSupply1_Object=MibScalar
mbgSCUPowerSupply1=_MbgSCUPowerSupply1_Object((1,3,6,1,4,1,5597,80,1,11),_MbgSCUPowerSupply1_Type())
mbgSCUPowerSupply1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUPowerSupply1.setStatus(_A)
class _MbgSCUPowerSupply2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notOK',0),('ok',1)))
_MbgSCUPowerSupply2_Type.__name__=_D
_MbgSCUPowerSupply2_Object=MibScalar
mbgSCUPowerSupply2=_MbgSCUPowerSupply2_Object((1,3,6,1,4,1,5597,80,1,12),_MbgSCUPowerSupply2_Type())
mbgSCUPowerSupply2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUPowerSupply2.setStatus(_A)
_MbgSCUTemp_Type=DisplayString
_MbgSCUTemp_Object=MibScalar
mbgSCUTemp=_MbgSCUTemp_Object((1,3,6,1,4,1,5597,80,1,13),_MbgSCUTemp_Type())
mbgSCUTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUTemp.setStatus(_A)
_MbgSCUOutp1_Type=DisplayString
_MbgSCUOutp1_Object=MibScalar
mbgSCUOutp1=_MbgSCUOutp1_Object((1,3,6,1,4,1,5597,80,1,14),_MbgSCUOutp1_Type())
mbgSCUOutp1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp1.setStatus(_A)
_MbgSCUOutp2_Type=DisplayString
_MbgSCUOutp2_Object=MibScalar
mbgSCUOutp2=_MbgSCUOutp2_Object((1,3,6,1,4,1,5597,80,1,15),_MbgSCUOutp2_Type())
mbgSCUOutp2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp2.setStatus(_A)
_MbgSCUOutp3_Type=DisplayString
_MbgSCUOutp3_Object=MibScalar
mbgSCUOutp3=_MbgSCUOutp3_Object((1,3,6,1,4,1,5597,80,1,16),_MbgSCUOutp3_Type())
mbgSCUOutp3.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp3.setStatus(_A)
_MbgSCUOutp4_Type=DisplayString
_MbgSCUOutp4_Object=MibScalar
mbgSCUOutp4=_MbgSCUOutp4_Object((1,3,6,1,4,1,5597,80,1,17),_MbgSCUOutp4_Type())
mbgSCUOutp4.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp4.setStatus(_A)
_MbgSCUOutp5_Type=DisplayString
_MbgSCUOutp5_Object=MibScalar
mbgSCUOutp5=_MbgSCUOutp5_Object((1,3,6,1,4,1,5597,80,1,18),_MbgSCUOutp5_Type())
mbgSCUOutp5.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp5.setStatus(_A)
_MbgSCUOutp6_Type=DisplayString
_MbgSCUOutp6_Object=MibScalar
mbgSCUOutp6=_MbgSCUOutp6_Object((1,3,6,1,4,1,5597,80,1,19),_MbgSCUOutp6_Type())
mbgSCUOutp6.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp6.setStatus(_A)
_MbgSCUOutp7_Type=DisplayString
_MbgSCUOutp7_Object=MibScalar
mbgSCUOutp7=_MbgSCUOutp7_Object((1,3,6,1,4,1,5597,80,1,20),_MbgSCUOutp7_Type())
mbgSCUOutp7.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp7.setStatus(_A)
_MbgSCUOutp8_Type=DisplayString
_MbgSCUOutp8_Object=MibScalar
mbgSCUOutp8=_MbgSCUOutp8_Object((1,3,6,1,4,1,5597,80,1,21),_MbgSCUOutp8_Type())
mbgSCUOutp8.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp8.setStatus(_A)
_MbgSCUOutp9_Type=DisplayString
_MbgSCUOutp9_Object=MibScalar
mbgSCUOutp9=_MbgSCUOutp9_Object((1,3,6,1,4,1,5597,80,1,22),_MbgSCUOutp9_Type())
mbgSCUOutp9.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp9.setStatus(_A)
_MbgSCUOutp10_Type=DisplayString
_MbgSCUOutp10_Object=MibScalar
mbgSCUOutp10=_MbgSCUOutp10_Object((1,3,6,1,4,1,5597,80,1,23),_MbgSCUOutp10_Type())
mbgSCUOutp10.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp10.setStatus(_A)
_MbgSCUOutp11_Type=DisplayString
_MbgSCUOutp11_Object=MibScalar
mbgSCUOutp11=_MbgSCUOutp11_Object((1,3,6,1,4,1,5597,80,1,24),_MbgSCUOutp11_Type())
mbgSCUOutp11.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp11.setStatus(_A)
_MbgSCUOutp12_Type=DisplayString
_MbgSCUOutp12_Object=MibScalar
mbgSCUOutp12=_MbgSCUOutp12_Object((1,3,6,1,4,1,5597,80,1,25),_MbgSCUOutp12_Type())
mbgSCUOutp12.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp12.setStatus(_A)
_MbgSCUOutp13_Type=DisplayString
_MbgSCUOutp13_Object=MibScalar
mbgSCUOutp13=_MbgSCUOutp13_Object((1,3,6,1,4,1,5597,80,1,26),_MbgSCUOutp13_Type())
mbgSCUOutp13.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp13.setStatus(_A)
_MbgSCUOutp14_Type=DisplayString
_MbgSCUOutp14_Object=MibScalar
mbgSCUOutp14=_MbgSCUOutp14_Object((1,3,6,1,4,1,5597,80,1,27),_MbgSCUOutp14_Type())
mbgSCUOutp14.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp14.setStatus(_A)
_MbgSCUOutp15_Type=DisplayString
_MbgSCUOutp15_Object=MibScalar
mbgSCUOutp15=_MbgSCUOutp15_Object((1,3,6,1,4,1,5597,80,1,28),_MbgSCUOutp15_Type())
mbgSCUOutp15.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp15.setStatus(_A)
_MbgSCUOutp16_Type=DisplayString
_MbgSCUOutp16_Object=MibScalar
mbgSCUOutp16=_MbgSCUOutp16_Object((1,3,6,1,4,1,5597,80,1,29),_MbgSCUOutp16_Type())
mbgSCUOutp16.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUOutp16.setStatus(_A)
_MbgSCUInp1_Type=DisplayString
_MbgSCUInp1_Object=MibScalar
mbgSCUInp1=_MbgSCUInp1_Object((1,3,6,1,4,1,5597,80,1,30),_MbgSCUInp1_Type())
mbgSCUInp1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUInp1.setStatus(_A)
_MbgSCUInp2_Type=DisplayString
_MbgSCUInp2_Object=MibScalar
mbgSCUInp2=_MbgSCUInp2_Object((1,3,6,1,4,1,5597,80,1,31),_MbgSCUInp2_Type())
mbgSCUInp2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUInp2.setStatus(_A)
_MbgSCUSupl1_Type=DisplayString
_MbgSCUSupl1_Object=MibScalar
mbgSCUSupl1=_MbgSCUSupl1_Object((1,3,6,1,4,1,5597,80,1,32),_MbgSCUSupl1_Type())
mbgSCUSupl1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSupl1.setStatus(_A)
_MbgSCUSupl2_Type=DisplayString
_MbgSCUSupl2_Object=MibScalar
mbgSCUSupl2=_MbgSCUSupl2_Object((1,3,6,1,4,1,5597,80,1,33),_MbgSCUSupl2_Type())
mbgSCUSupl2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSupl2.setStatus(_A)
_MbgSCUSupl3_Type=DisplayString
_MbgSCUSupl3_Object=MibScalar
mbgSCUSupl3=_MbgSCUSupl3_Object((1,3,6,1,4,1,5597,80,1,34),_MbgSCUSupl3_Type())
mbgSCUSupl3.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSupl3.setStatus(_A)
_MbgSCUSupl4_Type=DisplayString
_MbgSCUSupl4_Object=MibScalar
mbgSCUSupl4=_MbgSCUSupl4_Object((1,3,6,1,4,1,5597,80,1,35),_MbgSCUSupl4_Type())
mbgSCUSupl4.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUSupl4.setStatus(_A)
_MbgSCUtimeDiff_Type=DisplayString
_MbgSCUtimeDiff_Object=MibScalar
mbgSCUtimeDiff=_MbgSCUtimeDiff_Object((1,3,6,1,4,1,5597,80,1,36),_MbgSCUtimeDiff_Type())
mbgSCUtimeDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUtimeDiff.setStatus(_A)
class _MbgSCUAutoManual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('manual',0),('auto',1)))
_MbgSCUAutoManual_Type.__name__=_D
_MbgSCUAutoManual_Object=MibScalar
mbgSCUAutoManual=_MbgSCUAutoManual_Object((1,3,6,1,4,1,5597,80,1,37),_MbgSCUAutoManual_Type())
mbgSCUAutoManual.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUAutoManual.setStatus(_A)
_MbgSCUDum1_Type=DisplayString
_MbgSCUDum1_Object=MibScalar
mbgSCUDum1=_MbgSCUDum1_Object((1,3,6,1,4,1,5597,80,1,38),_MbgSCUDum1_Type())
mbgSCUDum1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgSCUDum1.setStatus(_A)
_MbgTrapRoot_ObjectIdentity=ObjectIdentity
mbgTrapRoot=_MbgTrapRoot_ObjectIdentity((1,3,6,1,4,1,5597,80,2))
_MbgTraps_ObjectIdentity=ObjectIdentity
mbgTraps=_MbgTraps_ObjectIdentity((1,3,6,1,4,1,5597,80,2,0))
_MbgRSC180Conformance_ObjectIdentity=ObjectIdentity
mbgRSC180Conformance=_MbgRSC180Conformance_ObjectIdentity((1,3,6,1,4,1,5597,80,90))
_MbgRSC180Compliances_ObjectIdentity=ObjectIdentity
mbgRSC180Compliances=_MbgRSC180Compliances_ObjectIdentity((1,3,6,1,4,1,5597,80,90,1))
_MbgRSC180Groups_ObjectIdentity=ObjectIdentity
mbgRSC180Groups=_MbgRSC180Groups_ObjectIdentity((1,3,6,1,4,1,5597,80,90,2))
mbgRSC180ObjectsGroup=ObjectGroup((1,3,6,1,4,1,5597,80,90,2,1))
mbgRSC180ObjectsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:mbgRSC180ObjectsGroup.setStatus(_A)
mbgColdBootTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,1))
if mibBuilder.loadTexts:mbgColdBootTrap.setStatus(_A)
mbgWarmBootTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,2))
if mibBuilder.loadTexts:mbgWarmBootTrap.setStatus(_A)
mbgGPSNavSolvedTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,3))
if mibBuilder.loadTexts:mbgGPSNavSolvedTrap.setStatus(_A)
mbgGPSReceiverNotRespondingTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,4))
if mibBuilder.loadTexts:mbgGPSReceiverNotRespondingTrap.setStatus(_A)
mbgGPSReceiverNotSyncTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,5))
if mibBuilder.loadTexts:mbgGPSReceiverNotSyncTrap.setStatus(_A)
mbgGPSAntennaFaultyTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,6))
if mibBuilder.loadTexts:mbgGPSAntennaFaultyTrap.setStatus(_A)
mbgGPSAntennaReconnectTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,7))
if mibBuilder.loadTexts:mbgGPSAntennaReconnectTrap.setStatus(_A)
mbgSCUBootTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,8))
if mibBuilder.loadTexts:mbgSCUBootTrap.setStatus(_A)
mbgLeapSecondAnnouncedTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,9))
if mibBuilder.loadTexts:mbgLeapSecondAnnouncedTrap.setStatus(_A)
mbgMasterclockSwitchoverTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,10))
if mibBuilder.loadTexts:mbgMasterclockSwitchoverTrap.setStatus(_A)
mbgPowerSupplyFailureTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,11))
if mibBuilder.loadTexts:mbgPowerSupplyFailureTrap.setStatus(_A)
mbgPowerSupplyOKTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,12))
if mibBuilder.loadTexts:mbgPowerSupplyOKTrap.setStatus(_A)
mbgHighTempTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,13))
if mibBuilder.loadTexts:mbgHighTempTrap.setStatus(_A)
mbgTestNotificationTrap=NotificationType((1,3,6,1,4,1,5597,80,2,0,99))
if mibBuilder.loadTexts:mbgTestNotificationTrap.setStatus(_A)
mbgRSC180TrapsGroup=NotificationGroup((1,3,6,1,4,1,5597,80,90,2,2))
mbgRSC180TrapsGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:mbgRSC180TrapsGroup.setStatus(_A)
mbgRSC180Compliance=ModuleCompliance((1,3,6,1,4,1,5597,80,90,1,1))
mbgRSC180Compliance.setObjects(*((_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:mbgRSC180Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:MeinbergRefClockTyp,'mbgRSC180':mbgRSC180,'mbgRefClock':mbgRefClock,'mbgRefClockStatus':mbgRefClockStatus,'mbgRefClockTable':mbgRefClockTable,'mbgRefClockTableEntry':mbgRefClockTableEntry,_G:mbgClkTableIndex,_J:mbgClkType,_K:mbgClkSerialNo,_L:mbgClkFirmwareRev,_M:mbgClkMode,_N:mbgGpsState,_O:mbgGpsPosition,_P:mbgGpsSatellitesGood,_Q:mbgGpsSatellitesInView,_R:mbgGPSNavSolved,_S:mbgLeapSecond,'mbgSCU':mbgSCU,_T:mbgSCUType,_U:mbgSCUSerialNo,_V:mbgSCUFirmwareRev,_W:mbgSCUMasterVal,_X:mbgSCULocalRemote,_Y:mbgTrapIPAddress,_Z:mbgSCUSyncStatusClk1,_a:mbgSCUSyncStatusClk2,_b:mbgSCUOutputStatus,_c:mbgSCUACOMode,_d:mbgSCUPowerSupply1,_e:mbgSCUPowerSupply2,_f:mbgSCUTemp,_g:mbgSCUOutp1,_h:mbgSCUOutp2,_i:mbgSCUOutp3,_j:mbgSCUOutp4,_k:mbgSCUOutp5,_l:mbgSCUOutp6,_m:mbgSCUOutp7,_n:mbgSCUOutp8,_o:mbgSCUOutp9,_p:mbgSCUOutp10,_q:mbgSCUOutp11,_r:mbgSCUOutp12,_s:mbgSCUOutp13,_t:mbgSCUOutp14,_u:mbgSCUOutp15,_v:mbgSCUOutp16,_w:mbgSCUInp1,_x:mbgSCUInp2,_y:mbgSCUSupl1,_z:mbgSCUSupl2,_A0:mbgSCUSupl3,_A1:mbgSCUSupl4,_A2:mbgSCUtimeDiff,_A3:mbgSCUAutoManual,_A4:mbgSCUDum1,'mbgTrapRoot':mbgTrapRoot,'mbgTraps':mbgTraps,_A5:mbgColdBootTrap,_A6:mbgWarmBootTrap,_A7:mbgGPSNavSolvedTrap,_A8:mbgGPSReceiverNotRespondingTrap,_A9:mbgGPSReceiverNotSyncTrap,_AA:mbgGPSAntennaFaultyTrap,_AB:mbgGPSAntennaReconnectTrap,_AC:mbgSCUBootTrap,_AD:mbgLeapSecondAnnouncedTrap,_AE:mbgMasterclockSwitchoverTrap,_AF:mbgPowerSupplyFailureTrap,_AG:mbgPowerSupplyOKTrap,_AH:mbgHighTempTrap,_AI:mbgTestNotificationTrap,'mbgRSC180Conformance':mbgRSC180Conformance,'mbgRSC180Compliances':mbgRSC180Compliances,'mbgRSC180Compliance':mbgRSC180Compliance,'mbgRSC180Groups':mbgRSC180Groups,_AJ:mbgRSC180ObjectsGroup,_AK:mbgRSC180TrapsGroup})