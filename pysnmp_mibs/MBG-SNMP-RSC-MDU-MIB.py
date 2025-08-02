_f='mbgRSC180TrapsGroup'
_e='mbgRSC180ObjectsGroup'
_d='mbgTestNotificationTrap'
_c='mbgHighTempTrap'
_b='mbgPowerSupplyOKTrap'
_a='mbgPowerSupplyFailureTrap'
_Z='mbgMasterclockSwitchoverTrap'
_Y='mbgLeapSecondAnnouncedTrap'
_X='mbgSCUBootTrap'
_W='mbgGPSAntennaReconnectTrap'
_V='mbgGPSAntennaFaultyTrap'
_U='mbgGPSReceiverNotSyncTrap'
_T='mbgGPSReceiverNotRespondingTrap'
_S='mbgGPSNavSolvedTrap'
_R='mbgWarmBootTrap'
_Q='mbgColdBootTrap'
_P='mbgTrapIPAddress'
_O='mbgGpsState'
_N='mbgClkFirmwareRev'
_M='mbgClkSerialNo'
_L='mbgClkType'
_K='notSync'
_J='MeinbergRefClockTyp'
_I='mbgClkTableIndex'
_H='notAvailable'
_G='read-write'
_F='ok'
_E='notOK'
_D='Integer32'
_C='read-only'
_B='MBG-SNMP-RSC-MDU-MIB'
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
if mibBuilder.loadTexts:mbgRSC180.setRevisions(('2017-03-28 00:00','2006-01-20 00:00'))
class MeinbergRefClockTyp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87)));namedValues=NamedValues(*((_H,0),('gps166',1),('gps167',2),('gps167SV',3),('gps167PC',4),('gps167PCI',5),('gps163',6),('gps168PCI',7),('gps161',8),('gps169PCI',9),('tcr167PCI',10),('gps164',11),('gps170PCI',12),('pzf511',13),('gps170',14),('tcr511',15),('am511',16),('msf511',17),('grc170',18),('gps170PEX',19),('gps162',20),('ptp270PEX',21),('frc511PEX',22),('gen170',23),('tcr170PEX',24),('wwvb511',25),('mbg170',26),('jjy511',27),('pzf600',28),('tcr600',29),('gps180',30),('gln170',31),('gps180PEX',32),('tcr180PEX',33),('pzf180PEX',34),('mbg180',35),('msf600',36),('wwvb600',37),('jjy600',38),('gps180HS',39),('gps180AMC',40),('esi180',41),('cpe180',42),('lno180',43),('grc180',44),('liu',45),('dcf600HS',46),('dcf600RS',47),('mri',48),('bpe',49),('gln180pex',50),('n2x',51),('rsc180',52),('lne_gb',53),('Ppg180',54),('scg',55),('mdu300',56),('sdi',57),('fdm180',58),('spt',59),('pzf180',60),('rel1000',61),('hps100',62),('vsg180',63),('msf180',64),('wwvb180',65),('cpc180',66),('ctc100',67),('tcr180',68),('lue180',69),('cpc_01',70),('tsu_01',71),('cmc_01',72),('scu_01',73),('fcu_01',74),('csm100',75),('lne180sfp',76),('gts180',77),('gps180csm',78),('grc181',79),('n2x180',80),('grc181PEX',81),('mdu180',82),('mdu312',83),('gps165',84),('gns181_uc',85),('psx_4ge',86),('rsc180rdu',87)))
_MbgRefClock_ObjectIdentity=ObjectIdentity
mbgRefClock=_MbgRefClock_ObjectIdentity((1,3,6,1,4,1,5597,80,0))
_MbgRefClockStatus_ObjectIdentity=ObjectIdentity
mbgRefClockStatus=_MbgRefClockStatus_ObjectIdentity((1,3,6,1,4,1,5597,80,0,0))
_MbgRefClockTable_Object=MibTable
mbgRefClockTable=_MbgRefClockTable_Object((1,3,6,1,4,1,5597,80,0,0,1))
if mibBuilder.loadTexts:mbgRefClockTable.setStatus(_A)
_MbgRefClockTableEntry_Object=MibTableRow
mbgRefClockTableEntry=_MbgRefClockTableEntry_Object((1,3,6,1,4,1,5597,80,0,0,1,1))
mbgRefClockTableEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:mbgRefClockTableEntry.setStatus(_A)
_MbgClkTableIndex_Type=Unsigned32
_MbgClkTableIndex_Object=MibTableColumn
mbgClkTableIndex=_MbgClkTableIndex_Object((1,3,6,1,4,1,5597,80,0,0,1,1,1),_MbgClkTableIndex_Type())
mbgClkTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mbgClkTableIndex.setStatus(_A)
class _MbgClkType_Type(MeinbergRefClockTyp):defaultValue=0
_MbgClkType_Type.__name__=_J
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
class _MbgGpsState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('synchronized',1),('notSynchronized',2)))
_MbgGpsState_Type.__name__=_D
_MbgGpsState_Object=MibTableColumn
mbgGpsState=_MbgGpsState_Object((1,3,6,1,4,1,5597,80,0,0,1,1,5),_MbgGpsState_Type())
mbgGpsState.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgGpsState.setStatus(_A)
_MbgMDU_ObjectIdentity=ObjectIdentity
mbgMDU=_MbgMDU_ObjectIdentity((1,3,6,1,4,1,5597,80,1))
_MbgMDUType_Type=MeinbergRefClockTyp
_MbgMDUType_Object=MibScalar
mbgMDUType=_MbgMDUType_Object((1,3,6,1,4,1,5597,80,1,1),_MbgMDUType_Type())
mbgMDUType.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUType.setStatus(_A)
_MbgMDUSerialNo_Type=DisplayString
_MbgMDUSerialNo_Object=MibScalar
mbgMDUSerialNo=_MbgMDUSerialNo_Object((1,3,6,1,4,1,5597,80,1,2),_MbgMDUSerialNo_Type())
mbgMDUSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSerialNo.setStatus(_A)
_MbgMDUFirmwareRev_Type=DisplayString
_MbgMDUFirmwareRev_Object=MibScalar
mbgMDUFirmwareRev=_MbgMDUFirmwareRev_Object((1,3,6,1,4,1,5597,80,1,3),_MbgMDUFirmwareRev_Type())
mbgMDUFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUFirmwareRev.setStatus(_A)
class _MbgMDUMasterVal_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noMaster',0),('clk1isMaster',1),('clk2isMaster',2)))
_MbgMDUMasterVal_Type.__name__=_D
_MbgMDUMasterVal_Object=MibScalar
mbgMDUMasterVal=_MbgMDUMasterVal_Object((1,3,6,1,4,1,5597,80,1,4),_MbgMDUMasterVal_Type())
mbgMDUMasterVal.setMaxAccess(_G)
if mibBuilder.loadTexts:mbgMDUMasterVal.setStatus(_A)
class _MbgMDULocalRemote_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('local',0),('remote',1)))
_MbgMDULocalRemote_Type.__name__=_D
_MbgMDULocalRemote_Object=MibScalar
mbgMDULocalRemote=_MbgMDULocalRemote_Object((1,3,6,1,4,1,5597,80,1,5),_MbgMDULocalRemote_Type())
mbgMDULocalRemote.setMaxAccess(_G)
if mibBuilder.loadTexts:mbgMDULocalRemote.setStatus(_A)
_MbgTrapIPAddress_Type=IpAddress
_MbgTrapIPAddress_Object=MibScalar
mbgTrapIPAddress=_MbgTrapIPAddress_Object((1,3,6,1,4,1,5597,80,1,6),_MbgTrapIPAddress_Type())
mbgTrapIPAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:mbgTrapIPAddress.setStatus(_A)
class _MbgMDUSyncStatusClk1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('sync',1)))
_MbgMDUSyncStatusClk1_Type.__name__=_D
_MbgMDUSyncStatusClk1_Object=MibScalar
mbgMDUSyncStatusClk1=_MbgMDUSyncStatusClk1_Object((1,3,6,1,4,1,5597,80,1,7),_MbgMDUSyncStatusClk1_Type())
mbgMDUSyncStatusClk1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSyncStatusClk1.setStatus(_A)
class _MbgMDUSyncStatusClk2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('sync',1)))
_MbgMDUSyncStatusClk2_Type.__name__=_D
_MbgMDUSyncStatusClk2_Object=MibScalar
mbgMDUSyncStatusClk2=_MbgMDUSyncStatusClk2_Object((1,3,6,1,4,1,5597,80,1,8),_MbgMDUSyncStatusClk2_Type())
mbgMDUSyncStatusClk2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSyncStatusClk2.setStatus(_A)
class _MbgMDUOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('outputsDisabled',0),('outputsEnabled',1)))
_MbgMDUOutputStatus_Type.__name__=_D
_MbgMDUOutputStatus_Object=MibScalar
mbgMDUOutputStatus=_MbgMDUOutputStatus_Object((1,3,6,1,4,1,5597,80,1,9),_MbgMDUOutputStatus_Type())
mbgMDUOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUOutputStatus.setStatus(_A)
class _MbgMDUACOMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('acoModeOFF',0),('acoModeON',1)))
_MbgMDUACOMode_Type.__name__=_D
_MbgMDUACOMode_Object=MibScalar
mbgMDUACOMode=_MbgMDUACOMode_Object((1,3,6,1,4,1,5597,80,1,10),_MbgMDUACOMode_Type())
mbgMDUACOMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUACOMode.setStatus(_A)
class _MbgMDUPowerSupply1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MbgMDUPowerSupply1_Type.__name__=_D
_MbgMDUPowerSupply1_Object=MibScalar
mbgMDUPowerSupply1=_MbgMDUPowerSupply1_Object((1,3,6,1,4,1,5597,80,1,11),_MbgMDUPowerSupply1_Type())
mbgMDUPowerSupply1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUPowerSupply1.setStatus(_A)
class _MbgMDUPowerSupply2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MbgMDUPowerSupply2_Type.__name__=_D
_MbgMDUPowerSupply2_Object=MibScalar
mbgMDUPowerSupply2=_MbgMDUPowerSupply2_Object((1,3,6,1,4,1,5597,80,1,12),_MbgMDUPowerSupply2_Type())
mbgMDUPowerSupply2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUPowerSupply2.setStatus(_A)
class _MbgMDUPowerSupply3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MbgMDUPowerSupply3_Type.__name__=_D
_MbgMDUPowerSupply3_Object=MibScalar
mbgMDUPowerSupply3=_MbgMDUPowerSupply3_Object((1,3,6,1,4,1,5597,80,1,13),_MbgMDUPowerSupply3_Type())
mbgMDUPowerSupply3.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUPowerSupply3.setStatus(_A)
class _MbgMDUPowerSupply4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MbgMDUPowerSupply4_Type.__name__=_D
_MbgMDUPowerSupply4_Object=MibScalar
mbgMDUPowerSupply4=_MbgMDUPowerSupply4_Object((1,3,6,1,4,1,5597,80,1,14),_MbgMDUPowerSupply4_Type())
mbgMDUPowerSupply4.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUPowerSupply4.setStatus(_A)
_MbgMDUTemp_Type=DisplayString
_MbgMDUTemp_Object=MibScalar
mbgMDUTemp=_MbgMDUTemp_Object((1,3,6,1,4,1,5597,80,1,15),_MbgMDUTemp_Type())
mbgMDUTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUTemp.setStatus(_A)
_MbgMDUSlot1_Type=DisplayString
_MbgMDUSlot1_Object=MibScalar
mbgMDUSlot1=_MbgMDUSlot1_Object((1,3,6,1,4,1,5597,80,1,16),_MbgMDUSlot1_Type())
mbgMDUSlot1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot1.setStatus(_A)
_MbgMDUSlot2_Type=DisplayString
_MbgMDUSlot2_Object=MibScalar
mbgMDUSlot2=_MbgMDUSlot2_Object((1,3,6,1,4,1,5597,80,1,17),_MbgMDUSlot2_Type())
mbgMDUSlot2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot2.setStatus(_A)
_MbgMDUSlot3_Type=DisplayString
_MbgMDUSlot3_Object=MibScalar
mbgMDUSlot3=_MbgMDUSlot3_Object((1,3,6,1,4,1,5597,80,1,18),_MbgMDUSlot3_Type())
mbgMDUSlot3.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot3.setStatus(_A)
_MbgMDUSlot4_Type=DisplayString
_MbgMDUSlot4_Object=MibScalar
mbgMDUSlot4=_MbgMDUSlot4_Object((1,3,6,1,4,1,5597,80,1,19),_MbgMDUSlot4_Type())
mbgMDUSlot4.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot4.setStatus(_A)
_MbgMDUSlot5_Type=DisplayString
_MbgMDUSlot5_Object=MibScalar
mbgMDUSlot5=_MbgMDUSlot5_Object((1,3,6,1,4,1,5597,80,1,20),_MbgMDUSlot5_Type())
mbgMDUSlot5.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot5.setStatus(_A)
_MbgMDUSlot6_Type=DisplayString
_MbgMDUSlot6_Object=MibScalar
mbgMDUSlot6=_MbgMDUSlot6_Object((1,3,6,1,4,1,5597,80,1,21),_MbgMDUSlot6_Type())
mbgMDUSlot6.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot6.setStatus(_A)
_MbgMDUSlot7_Type=DisplayString
_MbgMDUSlot7_Object=MibScalar
mbgMDUSlot7=_MbgMDUSlot7_Object((1,3,6,1,4,1,5597,80,1,22),_MbgMDUSlot7_Type())
mbgMDUSlot7.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot7.setStatus(_A)
_MbgMDUSlot8_Type=DisplayString
_MbgMDUSlot8_Object=MibScalar
mbgMDUSlot8=_MbgMDUSlot8_Object((1,3,6,1,4,1,5597,80,1,23),_MbgMDUSlot8_Type())
mbgMDUSlot8.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot8.setStatus(_A)
_MbgMDUSlot9_Type=DisplayString
_MbgMDUSlot9_Object=MibScalar
mbgMDUSlot9=_MbgMDUSlot9_Object((1,3,6,1,4,1,5597,80,1,24),_MbgMDUSlot9_Type())
mbgMDUSlot9.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot9.setStatus(_A)
_MbgMDUSlot10_Type=DisplayString
_MbgMDUSlot10_Object=MibScalar
mbgMDUSlot10=_MbgMDUSlot10_Object((1,3,6,1,4,1,5597,80,1,25),_MbgMDUSlot10_Type())
mbgMDUSlot10.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot10.setStatus(_A)
_MbgMDUSlot11_Type=DisplayString
_MbgMDUSlot11_Object=MibScalar
mbgMDUSlot11=_MbgMDUSlot11_Object((1,3,6,1,4,1,5597,80,1,26),_MbgMDUSlot11_Type())
mbgMDUSlot11.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot11.setStatus(_A)
_MbgMDUSlot12_Type=DisplayString
_MbgMDUSlot12_Object=MibScalar
mbgMDUSlot12=_MbgMDUSlot12_Object((1,3,6,1,4,1,5597,80,1,27),_MbgMDUSlot12_Type())
mbgMDUSlot12.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot12.setStatus(_A)
_MbgMDUSlot13_Type=DisplayString
_MbgMDUSlot13_Object=MibScalar
mbgMDUSlot13=_MbgMDUSlot13_Object((1,3,6,1,4,1,5597,80,1,28),_MbgMDUSlot13_Type())
mbgMDUSlot13.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot13.setStatus(_A)
_MbgMDUSlot14_Type=DisplayString
_MbgMDUSlot14_Object=MibScalar
mbgMDUSlot14=_MbgMDUSlot14_Object((1,3,6,1,4,1,5597,80,1,29),_MbgMDUSlot14_Type())
mbgMDUSlot14.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUSlot14.setStatus(_A)
_MbgMDUClk1_Type=DisplayString
_MbgMDUClk1_Object=MibScalar
mbgMDUClk1=_MbgMDUClk1_Object((1,3,6,1,4,1,5597,80,1,30),_MbgMDUClk1_Type())
mbgMDUClk1.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUClk1.setStatus(_A)
_MbgMDUClk2_Type=DisplayString
_MbgMDUClk2_Object=MibScalar
mbgMDUClk2=_MbgMDUClk2_Object((1,3,6,1,4,1,5597,80,1,31),_MbgMDUClk2_Type())
mbgMDUClk2.setMaxAccess(_C)
if mibBuilder.loadTexts:mbgMDUClk2.setStatus(_A)
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
mbgRSC180ObjectsGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,'mbgClkMode'),(_B,_O),(_B,'mbgGpsPosition'),(_B,'mbgGpsSatellitesGood'),(_B,'mbgGpsSatellitesInView'),(_B,'mbgGPSNavSolved'),(_B,'mbgLeapSecond'),(_B,'mbgSCUType'),(_B,'mbgSCUSerialNo'),(_B,'mbgSCUFirmwareRev'),(_B,'mbgSCUMasterVal'),(_B,'mbgSCULocalRemote'),(_B,_P),(_B,'mbgSCUSyncStatusClk1'),(_B,'mbgSCUSyncStatusClk2'),(_B,'mbgSCUOutputStatus'),(_B,'mbgSCUACOMode'),(_B,'mbgSCUPowerSupply1'),(_B,'mbgSCUPowerSupply2'),(_B,'mbgSCUTemp')))
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
mbgRSC180TrapsGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:mbgRSC180TrapsGroup.setStatus(_A)
mbgRSC180Compliance=ModuleCompliance((1,3,6,1,4,1,5597,80,90,1,1))
mbgRSC180Compliance.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:mbgRSC180Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:MeinbergRefClockTyp,'mbgRSC180':mbgRSC180,'mbgRefClock':mbgRefClock,'mbgRefClockStatus':mbgRefClockStatus,'mbgRefClockTable':mbgRefClockTable,'mbgRefClockTableEntry':mbgRefClockTableEntry,_I:mbgClkTableIndex,_L:mbgClkType,_M:mbgClkSerialNo,_N:mbgClkFirmwareRev,_O:mbgGpsState,'mbgMDU':mbgMDU,'mbgMDUType':mbgMDUType,'mbgMDUSerialNo':mbgMDUSerialNo,'mbgMDUFirmwareRev':mbgMDUFirmwareRev,'mbgMDUMasterVal':mbgMDUMasterVal,'mbgMDULocalRemote':mbgMDULocalRemote,_P:mbgTrapIPAddress,'mbgMDUSyncStatusClk1':mbgMDUSyncStatusClk1,'mbgMDUSyncStatusClk2':mbgMDUSyncStatusClk2,'mbgMDUOutputStatus':mbgMDUOutputStatus,'mbgMDUACOMode':mbgMDUACOMode,'mbgMDUPowerSupply1':mbgMDUPowerSupply1,'mbgMDUPowerSupply2':mbgMDUPowerSupply2,'mbgMDUPowerSupply3':mbgMDUPowerSupply3,'mbgMDUPowerSupply4':mbgMDUPowerSupply4,'mbgMDUTemp':mbgMDUTemp,'mbgMDUSlot1':mbgMDUSlot1,'mbgMDUSlot2':mbgMDUSlot2,'mbgMDUSlot3':mbgMDUSlot3,'mbgMDUSlot4':mbgMDUSlot4,'mbgMDUSlot5':mbgMDUSlot5,'mbgMDUSlot6':mbgMDUSlot6,'mbgMDUSlot7':mbgMDUSlot7,'mbgMDUSlot8':mbgMDUSlot8,'mbgMDUSlot9':mbgMDUSlot9,'mbgMDUSlot10':mbgMDUSlot10,'mbgMDUSlot11':mbgMDUSlot11,'mbgMDUSlot12':mbgMDUSlot12,'mbgMDUSlot13':mbgMDUSlot13,'mbgMDUSlot14':mbgMDUSlot14,'mbgMDUClk1':mbgMDUClk1,'mbgMDUClk2':mbgMDUClk2,'mbgTrapRoot':mbgTrapRoot,'mbgTraps':mbgTraps,_Q:mbgColdBootTrap,_R:mbgWarmBootTrap,_S:mbgGPSNavSolvedTrap,_T:mbgGPSReceiverNotRespondingTrap,_U:mbgGPSReceiverNotSyncTrap,_V:mbgGPSAntennaFaultyTrap,_W:mbgGPSAntennaReconnectTrap,_X:mbgSCUBootTrap,_Y:mbgLeapSecondAnnouncedTrap,_Z:mbgMasterclockSwitchoverTrap,_a:mbgPowerSupplyFailureTrap,_b:mbgPowerSupplyOKTrap,_c:mbgHighTempTrap,_d:mbgTestNotificationTrap,'mbgRSC180Conformance':mbgRSC180Conformance,'mbgRSC180Compliances':mbgRSC180Compliances,'mbgRSC180Compliance':mbgRSC180Compliance,'mbgRSC180Groups':mbgRSC180Groups,_e:mbgRSC180ObjectsGroup,_f:mbgRSC180TrapsGroup})