_Bi='trapSensorGroup'
_Bh='trapSystemWarningsUnits'
_Bg='trapCesopG704ClockSourceStatus'
_Bf='trapSyncSystemClockStatus'
_Be='trapEvcStatus'
_Bd='trapEvcName'
_Bc='trapCfmDefect'
_Bb='trapCfmVlan'
_Ba='trapCfmMepId'
_BZ='trapCfmMaName'
_BY='trapCfmMdName'
_BX='trapErpsStatus'
_BW='trapErpsDomainName'
_BV='trapErpsDomainId'
_BU='trapStandByMpuNsfId'
_BT='trapActiveMpuNsfId'
_BS='trapPanelStatus'
_BR='trapIdTunnelRSVP'
_BQ='trapStatusTunnelRSVP'
_BP='trapIpNeighborLDP'
_BO='trapIdLDP'
_BN='trapStatusLDP'
_BM='trapMulticastStormControlPPS'
_BL='trapMulticastStormControlStatus'
_BK='trapBroadcastStormControlPPS'
_BJ='trapBroadcastStormControlStatus'
_BI='trapCesopClockSourceStatus'
_BH='trapCesopClockAdapLinkQuality'
_BG='trapCesopBundleNextHopStatus'
_BF='trapCesopBundlePktMismatchStatus'
_BE='trapCesopBundleRemoteStatus'
_BD='trapCesopBundleLocalStatus'
_BC='trapCesopBundleRemoteTdmStatus'
_BB='trapCesopBundleLocalTdmStatus'
_BA='trapCesopTdmCrcStatus'
_B9='trapCesopTdmCasStatus'
_B8='trapCesopTdmRemoteStatus'
_B7='trapCesopTdmStatus'
_B6='trapBootloaderNew'
_B5='trapMacAddressMove'
_B4='trapStandbyMpuPresenceStatus'
_B3='swMpuModelId'
_B2='swMpuSerialNumber'
_B1='trapFansBoardPresenceStatus'
_B0='trapEapsStatus'
_A_='trapEapsDomainName'
_Az='trapEapsDomainId'
_Ay='trapDuplicatedIpMacAddress'
_Ax='trapDuplicatedIpAddress'
_Aw='trapDuplicatedIpVlan'
_Av='swIndivAlarmStatus'
_Au='swIndivPowerStatus'
_At='swIndivFanStatus'
_As='trapConfigSavePartition'
_Ar='trapSfpPresenceStatus'
_Aq='trapForbiddenAccessIp'
_Ap='trapForbiddenAccessMode'
_Ao='ddTransceiversIfIndex'
_An='queuePortQueueIndex'
_Am='queuePortIfIndex'
_Al='memStandbyUsageIndex'
_Ak='cpuStandbyUsageIndex'
_Aj='memActiveUsageIndex'
_Ai='cpuActiveUsageIndex'
_Ah='cfmProbeDmIndex'
_Ag='eapsInfoId'
_Af='filterCounterValueIndex'
_Ae='interfaceNumber'
_Ad='fileInfoFileIndex'
_Ac='fileInfoUnitID'
_Ab='sntpServerIp'
_Aa='remoteLogServerIp'
_AZ='ipFilterSSHMask'
_AY='ipFilterSSHAddress'
_AX='ipFilterTelnetMask'
_AW='ipFilterTelnetAddress'
_AV='ipFilterHTTPMask'
_AU='ipFilterHTTPAddress'
_AT='ipFilterSnmpMask'
_AS='ipFilterSnmpAddress'
_AR='radiusMultipleServerIndex'
_AQ='rlPortIndex'
_AP='trapDestAddress'
_AO='prioWrrTrafficClass'
_AN='vlanIndex'
_AM='bcastStormIfIndex'
_AL='igmpSnoopMulticastStaticIpAddress'
_AK='igmpSnoopMulticastStaticVlanIndex'
_AJ='igmpSnoopMulticastCurrentIpAddress'
_AI='igmpSnoopMulticastCurrentVlanIndex'
_AH='igmpSnoopRouterStaticVlanIndex'
_AG='igmpSnoopRouterCurrentVlanIndex'
_AF='mirrorSourcePort'
_AE='staPortIndex'
_AD='lacpPortIndex'
_AC='trunkIndex'
_AB='backPressure'
_AA='fullDuplex10000'
_A9='fullDuplex1000'
_A8='halfDuplex1000'
_A7='fullDuplex100'
_A6='halfDuplex100'
_A5='fullDuplex10'
_A4='halfDuplex10'
_A3='swSessionUnitIndex'
_A2='swIndivAlarmOutUnitIndex'
_A1='swMacAddrUnitIndex'
_A0='infNotAvailable'
_z='objectNonexistentInModel'
_y='mpu384'
_x='mpu192'
_w='master'
_v='OctetString'
_u='trapMemL3Free'
_t='trapLSTGroup'
_s='trapMemFree'
_r='trapFuseStatus'
_q='trapFuseId'
_p='swSerialNumber'
_o='trapLoginUserName'
_n='filterCounterInfoIndex'
_m='out-of-limits'
_l='failed'
_k='idle'
_j='present'
_i='absentee'
_h='dot3xFlowControlTx'
_g='dot3xFlowControlRx'
_f='dot3xFlowControlRxTx'
_e='swMpuIndex'
_d='activated'
_c='deactivated'
_b='swIndivAlarmIndex'
_a='swIndivAlarmUnitIndex'
_Z='swIndivFanIndex'
_Y='swIndivFanUnitIndex'
_X='swIndivPowerIndex'
_W='swIndivPowerUnitIndex'
_V='valid'
_U='EnabledStatus'
_T='trapTemperature'
_S='down'
_R='invalid'
_Q='fail'
_P='ok'
_O='disabled'
_N='enabled'
_M='swUnitIndex'
_L='read-create'
_K='DisplayString'
_J='not-accessible'
_I='portIndex'
_H='accessible-for-notify'
_G='trapDevLocalId'
_F='trapDevNo'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='DMswitch-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_v,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
datacomAccessDevicesMIBs,=mibBuilder.importSymbols('DATACOM-SMI','datacomAccessDevicesMIBs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_U)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dmSwitchMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,5,201))
class ValidStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_R,2)))
class KeySegment(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class StaPathCostMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_DmSwitchMIBObjects_ObjectIdentity=ObjectIdentity
dmSwitchMIBObjects=_DmSwitchMIBObjects_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1))
_SwitchMgt_ObjectIdentity=ObjectIdentity
switchMgt=_SwitchMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,1))
_SwitchNumber_Type=Integer32
_SwitchNumber_Object=MibScalar
switchNumber=_SwitchNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,1),_SwitchNumber_Type())
switchNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:switchNumber.setStatus(_A)
_SwitchInfoTable_Object=MibTable
switchInfoTable=_SwitchInfoTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2))
if mibBuilder.loadTexts:switchInfoTable.setStatus(_A)
_SwitchInfoEntry_Object=MibTableRow
switchInfoEntry=_SwitchInfoEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1))
switchInfoEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:switchInfoEntry.setStatus(_A)
_SwUnitIndex_Type=Integer32
_SwUnitIndex_Object=MibTableColumn
swUnitIndex=_SwUnitIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,1),_SwUnitIndex_Type())
swUnitIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swUnitIndex.setStatus(_A)
_SwHardwareVer_Type=Integer32
_SwHardwareVer_Object=MibTableColumn
swHardwareVer=_SwHardwareVer_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,2),_SwHardwareVer_Type())
swHardwareVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swHardwareVer.setStatus(_A)
class _SwBootLoaderVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBootLoaderVer_Type.__name__=_K
_SwBootLoaderVer_Object=MibTableColumn
swBootLoaderVer=_SwBootLoaderVer_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,3),_SwBootLoaderVer_Type())
swBootLoaderVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swBootLoaderVer.setStatus(_A)
class _SwFirmwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwFirmwareVer_Type.__name__=_K
_SwFirmwareVer_Object=MibTableColumn
swFirmwareVer=_SwFirmwareVer_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,4),_SwFirmwareVer_Type())
swFirmwareVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swFirmwareVer.setStatus(_A)
_SwPortNumber_Type=Integer32
_SwPortNumber_Object=MibTableColumn
swPortNumber=_SwPortNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,5),_SwPortNumber_Type())
swPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortNumber.setStatus(_A)
class _SwPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('internalPower',1),('redundantPower',2),('internalAndRedundantPower',3),('externalPower',4)))
_SwPowerStatus_Type.__name__=_C
_SwPowerStatus_Object=MibTableColumn
swPowerStatus=_SwPowerStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,6),_SwPowerStatus_Type())
swPowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swPowerStatus.setStatus(_A)
class _SwRoleInSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_w,1),('backupMaster',2),('slave',3)))
_SwRoleInSystem_Type.__name__=_C
_SwRoleInSystem_Object=MibTableColumn
swRoleInSystem=_SwRoleInSystem_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,7),_SwRoleInSystem_Type())
swRoleInSystem.setMaxAccess(_D)
if mibBuilder.loadTexts:swRoleInSystem.setStatus(_A)
class _SwSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwSerialNumber_Type.__name__=_K
_SwSerialNumber_Object=MibTableColumn
swSerialNumber=_SwSerialNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,8),_SwSerialNumber_Type())
swSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swSerialNumber.setStatus(_A)
class _SwProdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdName_Type.__name__=_K
_SwProdName_Object=MibTableColumn
swProdName=_SwProdName_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,9),_SwProdName_Type())
swProdName.setMaxAccess(_D)
if mibBuilder.loadTexts:swProdName.setStatus(_A)
class _SwProdModelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71)));namedValues=NamedValues(*(('dmSwitch2204G1',1),('dmSwitch2304G1',2),('dmSwitch3224F1',3),('dmSwitch3324F1',4),('dmSwitch3224F2',5),('dmSwitch3324F2',6),('dmSwitch3224F3',7),('dmSwitch3324F3',8),(_x,9),(_y,10),('eth12gx',11),('eth24gx',12),('eth1x10gx',13),('eth2x10gx',14),('eth12gxEth1x10gx',15),('eth24gt',16),('eth48gt',17),('eth24gxEth2x10gx',20),('eth48gx',21),('eth4x10gxhseries',22),('eth24gxEth2x10gxhseries',23),('eth48gxhseries',24),('eth24gxhseries',25),('eth2x10gxhseries',26),('eth10gx32xe1',27),('eth10gx4xstm1',28),('eth10gx2xstm4',29),('mpu512',30),('eth24gxlseries',31),('eth24gx4gx',32),('eth24gx2xx',33),('eth24gxs',34),('eth24gx2xxs',35),('eth24gx4xx',36),('eth20gt4gc',37),('eth20gt4gc2xx',38),('eth20gt4gcs',39),('eth20gt4gc2xxs',40),('eth20gt4gc4xx',41),('eth44gt4gc',42),('eth44gt4gc2xx',43),('eth44gt4gcs',44),('eth44gt4gc2xxs',45),('eth44gt4gc4xx',46),('eth44gt4gc2xs',47),('eth44gt4gc2xss',48),('eth44gt4gc4xs',49),('eth24gthseries',50),('eth48gthseries',51),('eth20gt4gc2xss',52),('eth20gx32xe1hseries',53),('eth20gx2x10gx32xe1hseries',54),('eth16gx2x10gx4xstm1hseries',55),('eth16gx4xstm1hseries',56),('eth24gx2x10gxeseries',57),('eth24gxeseries',58),('eth4x10gxeseries',59),('eth48gteseries',60),('mpu960',61),('eth44gt4gcsmplsdc',62),('eth44gt4gc2xxsmplsdc',63),('eth44gt4gc4xxmplsdc',64),('eth24gx2x10gxhseriesII',65),('eth20gt4gc4xs',66),('eth24gxhseriesII',67),('eth2x10gxhseriesII',68),('eth48gxhseriesII',69),('eth4x10gxhseriesII',70),('eth24gx4xs',71)))
_SwProdModelId_Type.__name__=_C
_SwProdModelId_Object=MibTableColumn
swProdModelId=_SwProdModelId_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,10),_SwProdModelId_Type())
swProdModelId.setMaxAccess(_D)
if mibBuilder.loadTexts:swProdModelId.setStatus(_A)
class _SwFirmwareReleaseDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwFirmwareReleaseDate_Type.__name__=_K
_SwFirmwareReleaseDate_Object=MibTableColumn
swFirmwareReleaseDate=_SwFirmwareReleaseDate_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,11),_SwFirmwareReleaseDate_Type())
swFirmwareReleaseDate.setMaxAccess(_D)
if mibBuilder.loadTexts:swFirmwareReleaseDate.setStatus(_A)
_SwTemperature_Type=Integer32
_SwTemperature_Object=MibTableColumn
swTemperature=_SwTemperature_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,12),_SwTemperature_Type())
swTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:swTemperature.setStatus(_A)
_SwG704IntfNumber_Type=Integer32
_SwG704IntfNumber_Object=MibTableColumn
swG704IntfNumber=_SwG704IntfNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,13),_SwG704IntfNumber_Type())
swG704IntfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swG704IntfNumber.setStatus(_A)
_SwE1cIntfNumber_Type=Integer32
_SwE1cIntfNumber_Object=MibTableColumn
swE1cIntfNumber=_SwE1cIntfNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,14),_SwE1cIntfNumber_Type())
swE1cIntfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swE1cIntfNumber.setStatus(_A)
_SwBundleIntfNumber_Type=Integer32
_SwBundleIntfNumber_Object=MibTableColumn
swBundleIntfNumber=_SwBundleIntfNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,15),_SwBundleIntfNumber_Type())
swBundleIntfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swBundleIntfNumber.setStatus(_A)
_SwPtpIntfNumber_Type=Integer32
_SwPtpIntfNumber_Object=MibTableColumn
swPtpIntfNumber=_SwPtpIntfNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,16),_SwPtpIntfNumber_Type())
swPtpIntfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swPtpIntfNumber.setStatus(_A)
_SwSdhIntfNumber_Type=Integer32
_SwSdhIntfNumber_Object=MibTableColumn
swSdhIntfNumber=_SwSdhIntfNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,17),_SwSdhIntfNumber_Type())
swSdhIntfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swSdhIntfNumber.setStatus(_A)
_SwVC4Number_Type=Integer32
_SwVC4Number_Object=MibTableColumn
swVC4Number=_SwVC4Number_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,18),_SwVC4Number_Type())
swVC4Number.setMaxAccess(_D)
if mibBuilder.loadTexts:swVC4Number.setStatus(_A)
_SwVC12Number_Type=Integer32
_SwVC12Number_Object=MibTableColumn
swVC12Number=_SwVC12Number_Object((1,3,6,1,4,1,3709,3,5,201,1,1,2,1,19),_SwVC12Number_Type())
swVC12Number.setMaxAccess(_D)
if mibBuilder.loadTexts:swVC12Number.setStatus(_A)
_SwitchProductId_ObjectIdentity=ObjectIdentity
switchProductId=_SwitchProductId_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,1,3))
class _SwProdManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdManufacturer_Type.__name__=_K
_SwProdManufacturer_Object=MibScalar
swProdManufacturer=_SwProdManufacturer_Object((1,3,6,1,4,1,3709,3,5,201,1,1,3,2),_SwProdManufacturer_Type())
swProdManufacturer.setMaxAccess(_D)
if mibBuilder.loadTexts:swProdManufacturer.setStatus(_A)
class _SwProdDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdDescription_Type.__name__=_K
_SwProdDescription_Object=MibScalar
swProdDescription=_SwProdDescription_Object((1,3,6,1,4,1,3709,3,5,201,1,1,3,3),_SwProdDescription_Type())
swProdDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:swProdDescription.setStatus(_A)
class _SwProdUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProdUrl_Type.__name__=_K
_SwProdUrl_Object=MibScalar
swProdUrl=_SwProdUrl_Object((1,3,6,1,4,1,3709,3,5,201,1,1,3,5),_SwProdUrl_Type())
swProdUrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swProdUrl.setStatus(_A)
_SwIdentifier_Type=Integer32
_SwIdentifier_Object=MibScalar
swIdentifier=_SwIdentifier_Object((1,3,6,1,4,1,3709,3,5,201,1,1,3,6),_SwIdentifier_Type())
swIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:swIdentifier.setStatus(_A)
class _SwVendorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,9,2000000254,2000000255)));namedValues=NamedValues(*(('datacom',1),('ieru',2),('asga',3),('parks',4),('digitel',5),('none',6),('elebra',7),('osp',9),(_z,2000000254),(_A0,2000000255)))
_SwVendorId_Type.__name__=_C
_SwVendorId_Object=MibScalar
swVendorId=_SwVendorId_Object((1,3,6,1,4,1,3709,3,5,201,1,1,3,7),_SwVendorId_Type())
swVendorId.setMaxAccess(_D)
if mibBuilder.loadTexts:swVendorId.setStatus('mandatory')
_SwitchIndivPowerTable_Object=MibTable
switchIndivPowerTable=_SwitchIndivPowerTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,4))
if mibBuilder.loadTexts:switchIndivPowerTable.setStatus(_A)
_SwitchIndivPowerEntry_Object=MibTableRow
switchIndivPowerEntry=_SwitchIndivPowerEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,4,1))
switchIndivPowerEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:switchIndivPowerEntry.setStatus(_A)
_SwIndivPowerUnitIndex_Type=Integer32
_SwIndivPowerUnitIndex_Object=MibTableColumn
swIndivPowerUnitIndex=_SwIndivPowerUnitIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,4,1,1),_SwIndivPowerUnitIndex_Type())
swIndivPowerUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivPowerUnitIndex.setStatus(_A)
class _SwIndivPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SwIndivPowerIndex_Type.__name__=_C
_SwIndivPowerIndex_Object=MibTableColumn
swIndivPowerIndex=_SwIndivPowerIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,4,1,2),_SwIndivPowerIndex_Type())
swIndivPowerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivPowerIndex.setStatus(_A)
class _SwIndivPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('red',1),('green',2),('notPresent',3)))
_SwIndivPowerStatus_Type.__name__=_C
_SwIndivPowerStatus_Object=MibTableColumn
swIndivPowerStatus=_SwIndivPowerStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,1,4,1,3),_SwIndivPowerStatus_Type())
swIndivPowerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivPowerStatus.setStatus(_A)
_SwitchIndivFanTable_Object=MibTable
switchIndivFanTable=_SwitchIndivFanTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,5))
if mibBuilder.loadTexts:switchIndivFanTable.setStatus(_A)
_SwitchIndivFanEntry_Object=MibTableRow
switchIndivFanEntry=_SwitchIndivFanEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,5,1))
switchIndivFanEntry.setIndexNames((0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:switchIndivFanEntry.setStatus(_A)
_SwIndivFanUnitIndex_Type=Integer32
_SwIndivFanUnitIndex_Object=MibTableColumn
swIndivFanUnitIndex=_SwIndivFanUnitIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,5,1,1),_SwIndivFanUnitIndex_Type())
swIndivFanUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivFanUnitIndex.setStatus(_A)
class _SwIndivFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SwIndivFanIndex_Type.__name__=_C
_SwIndivFanIndex_Object=MibTableColumn
swIndivFanIndex=_SwIndivFanIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,5,1,2),_SwIndivFanIndex_Type())
swIndivFanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivFanIndex.setStatus(_A)
class _SwIndivFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('red',1),('green',2)))
_SwIndivFanStatus_Type.__name__=_C
_SwIndivFanStatus_Object=MibTableColumn
swIndivFanStatus=_SwIndivFanStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,1,5,1,3),_SwIndivFanStatus_Type())
swIndivFanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivFanStatus.setStatus(_A)
_SwitchIndivAlarmTable_Object=MibTable
switchIndivAlarmTable=_SwitchIndivAlarmTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,6))
if mibBuilder.loadTexts:switchIndivAlarmTable.setStatus(_A)
_SwitchIndivAlarmEntry_Object=MibTableRow
switchIndivAlarmEntry=_SwitchIndivAlarmEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,6,1))
switchIndivAlarmEntry.setIndexNames((0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:switchIndivAlarmEntry.setStatus(_A)
_SwIndivAlarmUnitIndex_Type=Integer32
_SwIndivAlarmUnitIndex_Object=MibTableColumn
swIndivAlarmUnitIndex=_SwIndivAlarmUnitIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,6,1,1),_SwIndivAlarmUnitIndex_Type())
swIndivAlarmUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivAlarmUnitIndex.setStatus(_A)
class _SwIndivAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwIndivAlarmIndex_Type.__name__=_C
_SwIndivAlarmIndex_Object=MibTableColumn
swIndivAlarmIndex=_SwIndivAlarmIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,6,1,2),_SwIndivAlarmIndex_Type())
swIndivAlarmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivAlarmIndex.setStatus(_A)
class _SwIndivAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_SwIndivAlarmStatus_Type.__name__=_C
_SwIndivAlarmStatus_Object=MibTableColumn
swIndivAlarmStatus=_SwIndivAlarmStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,1,6,1,3),_SwIndivAlarmStatus_Type())
swIndivAlarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivAlarmStatus.setStatus(_A)
_SwitchResObj_Type=Integer32
_SwitchResObj_Object=MibScalar
switchResObj=_SwitchResObj_Object((1,3,6,1,4,1,3709,3,5,201,1,1,7),_SwitchResObj_Type())
switchResObj.setMaxAccess(_E)
if mibBuilder.loadTexts:switchResObj.setStatus(_A)
class _SwHashConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwHashConfig_Type.__name__=_K
_SwHashConfig_Object=MibScalar
swHashConfig=_SwHashConfig_Object((1,3,6,1,4,1,3709,3,5,201,1,1,8),_SwHashConfig_Type())
swHashConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:swHashConfig.setStatus(_A)
class _SwHashStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwHashStatus_Type.__name__=_K
_SwHashStatus_Object=MibScalar
swHashStatus=_SwHashStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,1,9),_SwHashStatus_Type())
swHashStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swHashStatus.setStatus(_A)
_SwCpuUsage_Type=Integer32
_SwCpuUsage_Object=MibScalar
swCpuUsage=_SwCpuUsage_Object((1,3,6,1,4,1,3709,3,5,201,1,1,10),_SwCpuUsage_Type())
swCpuUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:swCpuUsage.setStatus(_A)
_SwMemUsage_Type=Integer32
_SwMemUsage_Object=MibScalar
swMemUsage=_SwMemUsage_Object((1,3,6,1,4,1,3709,3,5,201,1,1,11),_SwMemUsage_Type())
swMemUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:swMemUsage.setStatus(_A)
_SwitchMacAddrUsageTable_Object=MibTable
switchMacAddrUsageTable=_SwitchMacAddrUsageTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,12))
if mibBuilder.loadTexts:switchMacAddrUsageTable.setStatus(_A)
_SwitchMacAddrUsageEntry_Object=MibTableRow
switchMacAddrUsageEntry=_SwitchMacAddrUsageEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,12,1))
switchMacAddrUsageEntry.setIndexNames((0,_B,_A1))
if mibBuilder.loadTexts:switchMacAddrUsageEntry.setStatus(_A)
_SwMacAddrUnitIndex_Type=Integer32
_SwMacAddrUnitIndex_Object=MibTableColumn
swMacAddrUnitIndex=_SwMacAddrUnitIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,12,1,1),_SwMacAddrUnitIndex_Type())
swMacAddrUnitIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swMacAddrUnitIndex.setStatus(_A)
_SwMacAddrUsageValue_Type=Integer32
_SwMacAddrUsageValue_Object=MibTableColumn
swMacAddrUsageValue=_SwMacAddrUsageValue_Object((1,3,6,1,4,1,3709,3,5,201,1,1,12,1,2),_SwMacAddrUsageValue_Type())
swMacAddrUsageValue.setMaxAccess(_D)
if mibBuilder.loadTexts:swMacAddrUsageValue.setStatus(_A)
_SwSlotNumber_Type=Integer32
_SwSlotNumber_Object=MibScalar
swSlotNumber=_SwSlotNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,13),_SwSlotNumber_Type())
swSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swSlotNumber.setStatus(_A)
_SwitchMpuTable_Object=MibTable
switchMpuTable=_SwitchMpuTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,14))
if mibBuilder.loadTexts:switchMpuTable.setStatus(_A)
_SwitchMpuEntry_Object=MibTableRow
switchMpuEntry=_SwitchMpuEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,14,1))
switchMpuEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:switchMpuEntry.setStatus(_A)
_SwMpuIndex_Type=Integer32
_SwMpuIndex_Object=MibTableColumn
swMpuIndex=_SwMpuIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,14,1,1),_SwMpuIndex_Type())
swMpuIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swMpuIndex.setStatus(_A)
class _SwMpuBootLoaderVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwMpuBootLoaderVer_Type.__name__=_K
_SwMpuBootLoaderVer_Object=MibTableColumn
swMpuBootLoaderVer=_SwMpuBootLoaderVer_Object((1,3,6,1,4,1,3709,3,5,201,1,1,14,1,2),_SwMpuBootLoaderVer_Type())
swMpuBootLoaderVer.setMaxAccess(_D)
if mibBuilder.loadTexts:swMpuBootLoaderVer.setStatus(_A)
class _SwMpuRoleInSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('standby',2)))
_SwMpuRoleInSystem_Type.__name__=_C
_SwMpuRoleInSystem_Object=MibTableColumn
swMpuRoleInSystem=_SwMpuRoleInSystem_Object((1,3,6,1,4,1,3709,3,5,201,1,1,14,1,3),_SwMpuRoleInSystem_Type())
swMpuRoleInSystem.setMaxAccess(_D)
if mibBuilder.loadTexts:swMpuRoleInSystem.setStatus(_A)
class _SwMpuSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SwMpuSerialNumber_Type.__name__=_K
_SwMpuSerialNumber_Object=MibTableColumn
swMpuSerialNumber=_SwMpuSerialNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,1,14,1,4),_SwMpuSerialNumber_Type())
swMpuSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:swMpuSerialNumber.setStatus(_A)
class _SwMpuModelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(9,10)));namedValues=NamedValues(*((_x,9),(_y,10)))
_SwMpuModelId_Type.__name__=_C
_SwMpuModelId_Object=MibTableColumn
swMpuModelId=_SwMpuModelId_Object((1,3,6,1,4,1,3709,3,5,201,1,1,14,1,5),_SwMpuModelId_Type())
swMpuModelId.setMaxAccess(_D)
if mibBuilder.loadTexts:swMpuModelId.setStatus(_A)
class _SwHashHardware_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwHashHardware_Type.__name__=_K
_SwHashHardware_Object=MibScalar
swHashHardware=_SwHashHardware_Object((1,3,6,1,4,1,3709,3,5,201,1,1,15),_SwHashHardware_Type())
swHashHardware.setMaxAccess(_D)
if mibBuilder.loadTexts:swHashHardware.setStatus(_A)
_SwitchIndivAlarmOutTable_Object=MibTable
switchIndivAlarmOutTable=_SwitchIndivAlarmOutTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,16))
if mibBuilder.loadTexts:switchIndivAlarmOutTable.setStatus(_A)
_SwitchIndivAlarmOutEntry_Object=MibTableRow
switchIndivAlarmOutEntry=_SwitchIndivAlarmOutEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,16,1))
switchIndivAlarmOutEntry.setIndexNames((0,_B,_A2))
if mibBuilder.loadTexts:switchIndivAlarmOutEntry.setStatus(_A)
_SwIndivAlarmOutUnitIndex_Type=Integer32
_SwIndivAlarmOutUnitIndex_Object=MibTableColumn
swIndivAlarmOutUnitIndex=_SwIndivAlarmOutUnitIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,16,1,1),_SwIndivAlarmOutUnitIndex_Type())
swIndivAlarmOutUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivAlarmOutUnitIndex.setStatus(_A)
class _SwIndivAlarmOutStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_SwIndivAlarmOutStatus_Type.__name__=_C
_SwIndivAlarmOutStatus_Object=MibTableColumn
swIndivAlarmOutStatus=_SwIndivAlarmOutStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,1,16,1,2),_SwIndivAlarmOutStatus_Type())
swIndivAlarmOutStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swIndivAlarmOutStatus.setStatus(_A)
class _SwChassisModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,2000000254,2000000255)));namedValues=NamedValues(*(('dmSwitch3000',1),('dmSwitch4001',2),('dmSwitch4001L',3),('dmSwitch4001S',4),('dmSwitch4004',5),('dmSwitch4008',6),('dmSwitch4008HighSpeed',7),('dmSwitch4001NewFan',8),('dmSwitch4100',9),(_z,2000000254),(_A0,2000000255)))
_SwChassisModel_Type.__name__=_C
_SwChassisModel_Object=MibScalar
swChassisModel=_SwChassisModel_Object((1,3,6,1,4,1,3709,3,5,201,1,1,17),_SwChassisModel_Type())
swChassisModel.setMaxAccess(_D)
if mibBuilder.loadTexts:swChassisModel.setStatus(_A)
_SwitchSessionTable_Object=MibTable
switchSessionTable=_SwitchSessionTable_Object((1,3,6,1,4,1,3709,3,5,201,1,1,18))
if mibBuilder.loadTexts:switchSessionTable.setStatus(_A)
_SwitchSessionEntry_Object=MibTableRow
switchSessionEntry=_SwitchSessionEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,1,18,1))
switchSessionEntry.setIndexNames((0,_B,_A3))
if mibBuilder.loadTexts:switchSessionEntry.setStatus(_A)
_SwSessionUnitIndex_Type=Integer32
_SwSessionUnitIndex_Object=MibTableColumn
swSessionUnitIndex=_SwSessionUnitIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,1,18,1,1),_SwSessionUnitIndex_Type())
swSessionUnitIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swSessionUnitIndex.setStatus(_A)
class _SwSessionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwSessionName_Type.__name__=_K
_SwSessionName_Object=MibTableColumn
swSessionName=_SwSessionName_Object((1,3,6,1,4,1,3709,3,5,201,1,1,18,1,2),_SwSessionName_Type())
swSessionName.setMaxAccess(_D)
if mibBuilder.loadTexts:swSessionName.setStatus(_A)
class _SwSessionUptime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwSessionUptime_Type.__name__=_K
_SwSessionUptime_Object=MibTableColumn
swSessionUptime=_SwSessionUptime_Object((1,3,6,1,4,1,3709,3,5,201,1,1,18,1,3),_SwSessionUptime_Type())
swSessionUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:swSessionUptime.setStatus(_A)
_SwSessionPid_Type=Integer32
_SwSessionPid_Object=MibTableColumn
swSessionPid=_SwSessionPid_Object((1,3,6,1,4,1,3709,3,5,201,1,1,18,1,4),_SwSessionPid_Type())
swSessionPid.setMaxAccess(_D)
if mibBuilder.loadTexts:swSessionPid.setStatus(_A)
class _SwSessionSrcIP_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwSessionSrcIP_Type.__name__=_K
_SwSessionSrcIP_Object=MibTableColumn
swSessionSrcIP=_SwSessionSrcIP_Object((1,3,6,1,4,1,3709,3,5,201,1,1,18,1,5),_SwSessionSrcIP_Type())
swSessionSrcIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swSessionSrcIP.setStatus(_A)
_PortMgt_ObjectIdentity=ObjectIdentity
portMgt=_PortMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,2))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1))
portEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PortName_Type.__name__=_K
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,2),_PortName_Type())
portName.setMaxAccess(_E)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),('hundredBaseTX',2),('hundredBaseFX',3),('thousandBaseSX',4),('thousandBaseLX',5),('thousandBaseT',6),('thousandBaseGBIC',7),('thousandBaseSfp',8),('hundredBaseFxScSingleMode',9),('hundredBaseFxScMultiMode',10),('tenG',11),('tenGSfp',12)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,3),_PortType_Type())
portType.setMaxAccess(_D)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSpeedDpxCfg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('reserved',1),(_A4,2),(_A5,3),(_A6,4),(_A7,5),(_A8,6),(_A9,7),(_AA,8)))
_PortSpeedDpxCfg_Type.__name__=_C
_PortSpeedDpxCfg_Object=MibTableColumn
portSpeedDpxCfg=_PortSpeedDpxCfg_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,4),_PortSpeedDpxCfg_Type())
portSpeedDpxCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:portSpeedDpxCfg.setStatus(_A)
class _PortFlowCtrlCfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_AB,3),(_f,4),(_g,5),(_h,6)))
_PortFlowCtrlCfg_Type.__name__=_C
_PortFlowCtrlCfg_Object=MibTableColumn
portFlowCtrlCfg=_PortFlowCtrlCfg_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,5),_PortFlowCtrlCfg_Type())
portFlowCtrlCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:portFlowCtrlCfg.setStatus(_A)
class _PortCapabilities_Type(Bits):namedValues=NamedValues(*(('portCap10half',0),('portCap10full',1),('portCap100half',2),('portCap100full',3),('portCap1000half',4),('portCap1000full',5),('portCap10000full',6),(_f,7),(_g,8),(_h,9)))
_PortCapabilities_Type.__name__='Bits'
_PortCapabilities_Object=MibTableColumn
portCapabilities=_PortCapabilities_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,6),_PortCapabilities_Type())
portCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:portCapabilities.setStatus(_A)
class _PortAutonegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_PortAutonegotiation_Type.__name__=_C
_PortAutonegotiation_Object=MibTableColumn
portAutonegotiation=_PortAutonegotiation_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,7),_PortAutonegotiation_Type())
portAutonegotiation.setMaxAccess(_E)
if mibBuilder.loadTexts:portAutonegotiation.setStatus(_A)
class _PortSpeedDpxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('error',1),(_A4,2),(_A5,3),(_A6,4),(_A7,5),(_A8,6),(_A9,7),(_AA,8),(_S,9)))
_PortSpeedDpxStatus_Type.__name__=_C
_PortSpeedDpxStatus_Object=MibTableColumn
portSpeedDpxStatus=_PortSpeedDpxStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,8),_PortSpeedDpxStatus_Type())
portSpeedDpxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portSpeedDpxStatus.setStatus(_A)
class _PortFlowCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('error',1),(_AB,2),(_f,3),(_g,4),(_h,5),('disable',6)))
_PortFlowCtrlStatus_Type.__name__=_C
_PortFlowCtrlStatus_Object=MibTableColumn
portFlowCtrlStatus=_PortFlowCtrlStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,9),_PortFlowCtrlStatus_Type())
portFlowCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portFlowCtrlStatus.setStatus(_A)
class _PortMdiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('normal',2),('xover',3)))
_PortMdiStatus_Type.__name__=_C
_PortMdiStatus_Object=MibTableColumn
portMdiStatus=_PortMdiStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,10),_PortMdiStatus_Type())
portMdiStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portMdiStatus.setStatus(_A)
_PortTrunkIndex_Type=Integer32
_PortTrunkIndex_Object=MibTableColumn
portTrunkIndex=_PortTrunkIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,2,1,1,11),_PortTrunkIndex_Type())
portTrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portTrunkIndex.setStatus(_A)
_TrunkMgt_ObjectIdentity=ObjectIdentity
trunkMgt=_TrunkMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,3))
_TrunkMaxId_Type=Integer32
_TrunkMaxId_Object=MibScalar
trunkMaxId=_TrunkMaxId_Object((1,3,6,1,4,1,3709,3,5,201,1,3,1),_TrunkMaxId_Type())
trunkMaxId.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkMaxId.setStatus(_A)
_TrunkValidNumber_Type=Integer32
_TrunkValidNumber_Object=MibScalar
trunkValidNumber=_TrunkValidNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,3,2),_TrunkValidNumber_Type())
trunkValidNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkValidNumber.setStatus(_A)
_TrunkTable_Object=MibTable
trunkTable=_TrunkTable_Object((1,3,6,1,4,1,3709,3,5,201,1,3,3))
if mibBuilder.loadTexts:trunkTable.setStatus(_A)
_TrunkEntry_Object=MibTableRow
trunkEntry=_TrunkEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,3,3,1))
trunkEntry.setIndexNames((0,_B,_AC))
if mibBuilder.loadTexts:trunkEntry.setStatus(_A)
_TrunkIndex_Type=Integer32
_TrunkIndex_Object=MibTableColumn
trunkIndex=_TrunkIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,3,3,1,1),_TrunkIndex_Type())
trunkIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:trunkIndex.setStatus(_A)
_TrunkPorts_Type=PortList
_TrunkPorts_Object=MibTableColumn
trunkPorts=_TrunkPorts_Object((1,3,6,1,4,1,3709,3,5,201,1,3,3,1,2),_TrunkPorts_Type())
trunkPorts.setMaxAccess(_L)
if mibBuilder.loadTexts:trunkPorts.setStatus(_A)
class _TrunkCreation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('lacp',2)))
_TrunkCreation_Type.__name__=_C
_TrunkCreation_Object=MibTableColumn
trunkCreation=_TrunkCreation_Object((1,3,6,1,4,1,3709,3,5,201,1,3,3,1,3),_TrunkCreation_Type())
trunkCreation.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkCreation.setStatus(_A)
class _TrunkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_R,2)))
_TrunkStatus_Type.__name__=_C
_TrunkStatus_Object=MibTableColumn
trunkStatus=_TrunkStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,3,3,1,4),_TrunkStatus_Type())
trunkStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:trunkStatus.setStatus(_A)
_LacpMgt_ObjectIdentity=ObjectIdentity
lacpMgt=_LacpMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,4))
_LacpPortTable_Object=MibTable
lacpPortTable=_LacpPortTable_Object((1,3,6,1,4,1,3709,3,5,201,1,4,1))
if mibBuilder.loadTexts:lacpPortTable.setStatus(_A)
_LacpPortEntry_Object=MibTableRow
lacpPortEntry=_LacpPortEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,4,1,1))
lacpPortEntry.setIndexNames((0,_B,_AD))
if mibBuilder.loadTexts:lacpPortEntry.setStatus(_A)
_LacpPortIndex_Type=Integer32
_LacpPortIndex_Object=MibTableColumn
lacpPortIndex=_LacpPortIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,4,1,1,1),_LacpPortIndex_Type())
lacpPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:lacpPortIndex.setStatus(_A)
class _LacpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_LacpPortStatus_Type.__name__=_C
_LacpPortStatus_Object=MibTableColumn
lacpPortStatus=_LacpPortStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,4,1,1,2),_LacpPortStatus_Type())
lacpPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lacpPortStatus.setStatus(_A)
_StaMgt_ObjectIdentity=ObjectIdentity
staMgt=_StaMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,5))
class _StaSystemStatus_Type(EnabledStatus):defaultValue=1
_StaSystemStatus_Type.__name__=_U
_StaSystemStatus_Object=MibScalar
staSystemStatus=_StaSystemStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,5,1),_StaSystemStatus_Type())
staSystemStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:staSystemStatus.setStatus(_A)
_StaPortTable_Object=MibTable
staPortTable=_StaPortTable_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2))
if mibBuilder.loadTexts:staPortTable.setStatus(_A)
_StaPortEntry_Object=MibTableRow
staPortEntry=_StaPortEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1))
staPortEntry.setIndexNames((0,_B,_AE))
if mibBuilder.loadTexts:staPortEntry.setStatus(_A)
_StaPortIndex_Type=Integer32
_StaPortIndex_Object=MibTableColumn
staPortIndex=_StaPortIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1,1),_StaPortIndex_Type())
staPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:staPortIndex.setStatus(_A)
_StaPortAdminEdgePort_Type=TruthValue
_StaPortAdminEdgePort_Object=MibTableColumn
staPortAdminEdgePort=_StaPortAdminEdgePort_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1,2),_StaPortAdminEdgePort_Type())
staPortAdminEdgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:staPortAdminEdgePort.setStatus(_A)
_StaPortOperEdgePort_Type=TruthValue
_StaPortOperEdgePort_Object=MibTableColumn
staPortOperEdgePort=_StaPortOperEdgePort_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1,3),_StaPortOperEdgePort_Type())
staPortOperEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortOperEdgePort.setStatus(_A)
class _StaPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_StaPortAdminPointToPoint_Type.__name__=_C
_StaPortAdminPointToPoint_Object=MibTableColumn
staPortAdminPointToPoint=_StaPortAdminPointToPoint_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1,4),_StaPortAdminPointToPoint_Type())
staPortAdminPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:staPortAdminPointToPoint.setStatus(_A)
_StaPortOperPointToPoint_Type=TruthValue
_StaPortOperPointToPoint_Object=MibTableColumn
staPortOperPointToPoint=_StaPortOperPointToPoint_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1,5),_StaPortOperPointToPoint_Type())
staPortOperPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:staPortOperPointToPoint.setStatus(_A)
class _StaPortLongPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_StaPortLongPathCost_Type.__name__=_C
_StaPortLongPathCost_Object=MibTableColumn
staPortLongPathCost=_StaPortLongPathCost_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1,6),_StaPortLongPathCost_Type())
staPortLongPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:staPortLongPathCost.setStatus(_A)
class _StaPortSystemStatus_Type(EnabledStatus):defaultValue=1
_StaPortSystemStatus_Type.__name__=_U
_StaPortSystemStatus_Object=MibTableColumn
staPortSystemStatus=_StaPortSystemStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,5,2,1,7),_StaPortSystemStatus_Type())
staPortSystemStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:staPortSystemStatus.setStatus(_A)
class _StaProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stp',1),('rstp',2),('mstp',3)))
_StaProtocolType_Type.__name__=_C
_StaProtocolType_Object=MibScalar
staProtocolType=_StaProtocolType_Object((1,3,6,1,4,1,3709,3,5,201,1,5,3),_StaProtocolType_Type())
staProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:staProtocolType.setStatus(_A)
_TftpMgt_ObjectIdentity=ObjectIdentity
tftpMgt=_TftpMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,6))
class _TftpFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TftpFile_Type.__name__=_K
_TftpFile_Object=MibScalar
tftpFile=_TftpFile_Object((1,3,6,1,4,1,3709,3,5,201,1,6,1),_TftpFile_Type())
tftpFile.setMaxAccess(_E)
if mibBuilder.loadTexts:tftpFile.setStatus(_A)
class _TftpFlashConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_TftpFlashConfig_Type.__name__=_C
_TftpFlashConfig_Object=MibScalar
tftpFlashConfig=_TftpFlashConfig_Object((1,3,6,1,4,1,3709,3,5,201,1,6,2),_TftpFlashConfig_Type())
tftpFlashConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:tftpFlashConfig.setStatus(_A)
_TftpServer_Type=IpAddress
_TftpServer_Object=MibScalar
tftpServer=_TftpServer_Object((1,3,6,1,4,1,3709,3,5,201,1,6,3),_TftpServer_Type())
tftpServer.setMaxAccess(_E)
if mibBuilder.loadTexts:tftpServer.setStatus(_A)
class _TftpAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('downloadToFlashConfig',1),('downloadToRunningConfig',2),('downloadToStartupConfig',3),('downloadToFirmware',4),('uploadFromFlashConfig',5),('uploadFromRunningConfig',6),('uploadFromStartupConfig',7),('notDownloading',8)))
_TftpAction_Type.__name__=_C
_TftpAction_Object=MibScalar
tftpAction=_TftpAction_Object((1,3,6,1,4,1,3709,3,5,201,1,6,4),_TftpAction_Type())
tftpAction.setMaxAccess(_E)
if mibBuilder.loadTexts:tftpAction.setStatus(_A)
_RestartMgt_ObjectIdentity=ObjectIdentity
restartMgt=_RestartMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,7))
class _RestartFirmware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RestartFirmware_Type.__name__=_C
_RestartFirmware_Object=MibScalar
restartFirmware=_RestartFirmware_Object((1,3,6,1,4,1,3709,3,5,201,1,7,1),_RestartFirmware_Type())
restartFirmware.setMaxAccess(_E)
if mibBuilder.loadTexts:restartFirmware.setStatus(_A)
class _RestartConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RestartConfig_Type.__name__=_C
_RestartConfig_Object=MibScalar
restartConfig=_RestartConfig_Object((1,3,6,1,4,1,3709,3,5,201,1,7,2),_RestartConfig_Type())
restartConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:restartConfig.setStatus(_A)
class _RestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('warmBoot',2),('coldBoot',3)))
_RestartControl_Type.__name__=_C
_RestartControl_Object=MibScalar
restartControl=_RestartControl_Object((1,3,6,1,4,1,3709,3,5,201,1,7,3),_RestartControl_Type())
restartControl.setMaxAccess(_E)
if mibBuilder.loadTexts:restartControl.setStatus(_A)
_MirrorMgt_ObjectIdentity=ObjectIdentity
mirrorMgt=_MirrorMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,8))
_MirrorDestinationPort_Type=Integer32
_MirrorDestinationPort_Object=MibScalar
mirrorDestinationPort=_MirrorDestinationPort_Object((1,3,6,1,4,1,3709,3,5,201,1,8,1),_MirrorDestinationPort_Type())
mirrorDestinationPort.setMaxAccess(_E)
if mibBuilder.loadTexts:mirrorDestinationPort.setStatus(_A)
_MirrorTable_Object=MibTable
mirrorTable=_MirrorTable_Object((1,3,6,1,4,1,3709,3,5,201,1,8,2))
if mibBuilder.loadTexts:mirrorTable.setStatus(_A)
_MirrorEntry_Object=MibTableRow
mirrorEntry=_MirrorEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,8,2,1))
mirrorEntry.setIndexNames((0,_B,_AF))
if mibBuilder.loadTexts:mirrorEntry.setStatus(_A)
_MirrorSourcePort_Type=Integer32
_MirrorSourcePort_Object=MibTableColumn
mirrorSourcePort=_MirrorSourcePort_Object((1,3,6,1,4,1,3709,3,5,201,1,8,2,1,1),_MirrorSourcePort_Type())
mirrorSourcePort.setMaxAccess(_J)
if mibBuilder.loadTexts:mirrorSourcePort.setStatus(_A)
class _MirrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rx',1),('tx',2),('all',3),('disable',4)))
_MirrorType_Type.__name__=_C
_MirrorType_Object=MibTableColumn
mirrorType=_MirrorType_Object((1,3,6,1,4,1,3709,3,5,201,1,8,2,1,2),_MirrorType_Type())
mirrorType.setMaxAccess(_L)
if mibBuilder.loadTexts:mirrorType.setStatus(_A)
_IgmpSnoopMgt_ObjectIdentity=ObjectIdentity
igmpSnoopMgt=_IgmpSnoopMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,9))
class _IgmpSnoopStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_IgmpSnoopStatus_Type.__name__=_C
_IgmpSnoopStatus_Object=MibScalar
igmpSnoopStatus=_IgmpSnoopStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,9,1),_IgmpSnoopStatus_Type())
igmpSnoopStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopStatus.setStatus(_A)
class _IgmpSnoopQuerier_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_IgmpSnoopQuerier_Type.__name__=_C
_IgmpSnoopQuerier_Object=MibScalar
igmpSnoopQuerier=_IgmpSnoopQuerier_Object((1,3,6,1,4,1,3709,3,5,201,1,9,2),_IgmpSnoopQuerier_Type())
igmpSnoopQuerier.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopQuerier.setStatus(_A)
class _IgmpSnoopQueryCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_IgmpSnoopQueryCount_Type.__name__=_C
_IgmpSnoopQueryCount_Object=MibScalar
igmpSnoopQueryCount=_IgmpSnoopQueryCount_Object((1,3,6,1,4,1,3709,3,5,201,1,9,3),_IgmpSnoopQueryCount_Type())
igmpSnoopQueryCount.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopQueryCount.setStatus(_A)
class _IgmpSnoopQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,125))
_IgmpSnoopQueryInterval_Type.__name__=_C
_IgmpSnoopQueryInterval_Object=MibScalar
igmpSnoopQueryInterval=_IgmpSnoopQueryInterval_Object((1,3,6,1,4,1,3709,3,5,201,1,9,4),_IgmpSnoopQueryInterval_Type())
igmpSnoopQueryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopQueryInterval.setStatus(_A)
class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,25))
_IgmpSnoopQueryMaxResponseTime_Type.__name__=_C
_IgmpSnoopQueryMaxResponseTime_Object=MibScalar
igmpSnoopQueryMaxResponseTime=_IgmpSnoopQueryMaxResponseTime_Object((1,3,6,1,4,1,3709,3,5,201,1,9,5),_IgmpSnoopQueryMaxResponseTime_Type())
igmpSnoopQueryMaxResponseTime.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopQueryMaxResponseTime.setStatus(_A)
class _IgmpSnoopQueryTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,500))
_IgmpSnoopQueryTimeout_Type.__name__=_C
_IgmpSnoopQueryTimeout_Object=MibScalar
igmpSnoopQueryTimeout=_IgmpSnoopQueryTimeout_Object((1,3,6,1,4,1,3709,3,5,201,1,9,6),_IgmpSnoopQueryTimeout_Type())
igmpSnoopQueryTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopQueryTimeout.setStatus(_A)
class _IgmpSnoopVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IgmpSnoopVersion_Type.__name__=_C
_IgmpSnoopVersion_Object=MibScalar
igmpSnoopVersion=_IgmpSnoopVersion_Object((1,3,6,1,4,1,3709,3,5,201,1,9,7),_IgmpSnoopVersion_Type())
igmpSnoopVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:igmpSnoopVersion.setStatus(_A)
_IgmpSnoopRouterCurrentTable_Object=MibTable
igmpSnoopRouterCurrentTable=_IgmpSnoopRouterCurrentTable_Object((1,3,6,1,4,1,3709,3,5,201,1,9,8))
if mibBuilder.loadTexts:igmpSnoopRouterCurrentTable.setStatus(_A)
_IgmpSnoopRouterCurrentEntry_Object=MibTableRow
igmpSnoopRouterCurrentEntry=_IgmpSnoopRouterCurrentEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,9,8,1))
igmpSnoopRouterCurrentEntry.setIndexNames((0,_B,_AG))
if mibBuilder.loadTexts:igmpSnoopRouterCurrentEntry.setStatus(_A)
_IgmpSnoopRouterCurrentVlanIndex_Type=Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object=MibTableColumn
igmpSnoopRouterCurrentVlanIndex=_IgmpSnoopRouterCurrentVlanIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,9,8,1,1),_IgmpSnoopRouterCurrentVlanIndex_Type())
igmpSnoopRouterCurrentVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentVlanIndex.setStatus(_A)
_IgmpSnoopRouterCurrentPorts_Type=PortList
_IgmpSnoopRouterCurrentPorts_Object=MibTableColumn
igmpSnoopRouterCurrentPorts=_IgmpSnoopRouterCurrentPorts_Object((1,3,6,1,4,1,3709,3,5,201,1,9,8,1,2),_IgmpSnoopRouterCurrentPorts_Type())
igmpSnoopRouterCurrentPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopRouterCurrentPorts.setStatus(_A)
_IgmpSnoopRouterStaticTable_Object=MibTable
igmpSnoopRouterStaticTable=_IgmpSnoopRouterStaticTable_Object((1,3,6,1,4,1,3709,3,5,201,1,9,9))
if mibBuilder.loadTexts:igmpSnoopRouterStaticTable.setStatus(_A)
_IgmpSnoopRouterStaticEntry_Object=MibTableRow
igmpSnoopRouterStaticEntry=_IgmpSnoopRouterStaticEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,9,9,1))
igmpSnoopRouterStaticEntry.setIndexNames((0,_B,_AH))
if mibBuilder.loadTexts:igmpSnoopRouterStaticEntry.setStatus(_A)
_IgmpSnoopRouterStaticVlanIndex_Type=Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object=MibTableColumn
igmpSnoopRouterStaticVlanIndex=_IgmpSnoopRouterStaticVlanIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,9,9,1,1),_IgmpSnoopRouterStaticVlanIndex_Type())
igmpSnoopRouterStaticVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpSnoopRouterStaticVlanIndex.setStatus(_A)
_IgmpSnoopRouterStaticPorts_Type=PortList
_IgmpSnoopRouterStaticPorts_Object=MibTableColumn
igmpSnoopRouterStaticPorts=_IgmpSnoopRouterStaticPorts_Object((1,3,6,1,4,1,3709,3,5,201,1,9,9,1,2),_IgmpSnoopRouterStaticPorts_Type())
igmpSnoopRouterStaticPorts.setMaxAccess(_L)
if mibBuilder.loadTexts:igmpSnoopRouterStaticPorts.setStatus(_A)
_IgmpSnoopMulticastCurrentTable_Object=MibTable
igmpSnoopMulticastCurrentTable=_IgmpSnoopMulticastCurrentTable_Object((1,3,6,1,4,1,3709,3,5,201,1,9,10))
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentTable.setStatus(_A)
_IgmpSnoopMulticastCurrentEntry_Object=MibTableRow
igmpSnoopMulticastCurrentEntry=_IgmpSnoopMulticastCurrentEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,9,10,1))
igmpSnoopMulticastCurrentEntry.setIndexNames((0,_B,_AI),(0,_B,_AJ))
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentEntry.setStatus(_A)
_IgmpSnoopMulticastCurrentVlanIndex_Type=Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object=MibTableColumn
igmpSnoopMulticastCurrentVlanIndex=_IgmpSnoopMulticastCurrentVlanIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,9,10,1,1),_IgmpSnoopMulticastCurrentVlanIndex_Type())
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentVlanIndex.setStatus(_A)
_IgmpSnoopMulticastCurrentIpAddress_Type=IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object=MibTableColumn
igmpSnoopMulticastCurrentIpAddress=_IgmpSnoopMulticastCurrentIpAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,9,10,1,2),_IgmpSnoopMulticastCurrentIpAddress_Type())
igmpSnoopMulticastCurrentIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentIpAddress.setStatus(_A)
_IgmpSnoopMulticastCurrentPorts_Type=PortList
_IgmpSnoopMulticastCurrentPorts_Object=MibTableColumn
igmpSnoopMulticastCurrentPorts=_IgmpSnoopMulticastCurrentPorts_Object((1,3,6,1,4,1,3709,3,5,201,1,9,10,1,3),_IgmpSnoopMulticastCurrentPorts_Type())
igmpSnoopMulticastCurrentPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpSnoopMulticastCurrentPorts.setStatus(_A)
_IgmpSnoopMulticastStaticTable_Object=MibTable
igmpSnoopMulticastStaticTable=_IgmpSnoopMulticastStaticTable_Object((1,3,6,1,4,1,3709,3,5,201,1,9,11))
if mibBuilder.loadTexts:igmpSnoopMulticastStaticTable.setStatus(_A)
_IgmpSnoopMulticastStaticEntry_Object=MibTableRow
igmpSnoopMulticastStaticEntry=_IgmpSnoopMulticastStaticEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,9,11,1))
igmpSnoopMulticastStaticEntry.setIndexNames((0,_B,_AK),(0,_B,_AL))
if mibBuilder.loadTexts:igmpSnoopMulticastStaticEntry.setStatus(_A)
_IgmpSnoopMulticastStaticVlanIndex_Type=Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object=MibTableColumn
igmpSnoopMulticastStaticVlanIndex=_IgmpSnoopMulticastStaticVlanIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,9,11,1,1),_IgmpSnoopMulticastStaticVlanIndex_Type())
igmpSnoopMulticastStaticVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticVlanIndex.setStatus(_A)
_IgmpSnoopMulticastStaticIpAddress_Type=IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object=MibTableColumn
igmpSnoopMulticastStaticIpAddress=_IgmpSnoopMulticastStaticIpAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,9,11,1,2),_IgmpSnoopMulticastStaticIpAddress_Type())
igmpSnoopMulticastStaticIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticIpAddress.setStatus(_A)
_IgmpSnoopMulticastStaticPorts_Type=PortList
_IgmpSnoopMulticastStaticPorts_Object=MibTableColumn
igmpSnoopMulticastStaticPorts=_IgmpSnoopMulticastStaticPorts_Object((1,3,6,1,4,1,3709,3,5,201,1,9,11,1,3),_IgmpSnoopMulticastStaticPorts_Type())
igmpSnoopMulticastStaticPorts.setMaxAccess(_L)
if mibBuilder.loadTexts:igmpSnoopMulticastStaticPorts.setStatus(_A)
_IpMgt_ObjectIdentity=ObjectIdentity
ipMgt=_IpMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,10))
class _IpAddressMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dhcp',2)))
_IpAddressMode_Type.__name__=_C
_IpAddressMode_Object=MibScalar
ipAddressMode=_IpAddressMode_Object((1,3,6,1,4,1,3709,3,5,201,1,10,1),_IpAddressMode_Type())
ipAddressMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ipAddressMode.setStatus(_A)
_IpDefaultGateway_Type=IpAddress
_IpDefaultGateway_Object=MibScalar
ipDefaultGateway=_IpDefaultGateway_Object((1,3,6,1,4,1,3709,3,5,201,1,10,2),_IpDefaultGateway_Type())
ipDefaultGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:ipDefaultGateway.setStatus(_A)
_IpPrimaryDnsServer_Type=IpAddress
_IpPrimaryDnsServer_Object=MibScalar
ipPrimaryDnsServer=_IpPrimaryDnsServer_Object((1,3,6,1,4,1,3709,3,5,201,1,10,3),_IpPrimaryDnsServer_Type())
ipPrimaryDnsServer.setMaxAccess(_E)
if mibBuilder.loadTexts:ipPrimaryDnsServer.setStatus(_A)
_IpSecondaryDnsServer_Type=IpAddress
_IpSecondaryDnsServer_Object=MibScalar
ipSecondaryDnsServer=_IpSecondaryDnsServer_Object((1,3,6,1,4,1,3709,3,5,201,1,10,4),_IpSecondaryDnsServer_Type())
ipSecondaryDnsServer.setMaxAccess(_E)
if mibBuilder.loadTexts:ipSecondaryDnsServer.setStatus(_A)
class _IpHttpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_IpHttpState_Type.__name__=_C
_IpHttpState_Object=MibScalar
ipHttpState=_IpHttpState_Object((1,3,6,1,4,1,3709,3,5,201,1,10,5),_IpHttpState_Type())
ipHttpState.setMaxAccess(_E)
if mibBuilder.loadTexts:ipHttpState.setStatus(_A)
class _IpHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpHttpPort_Type.__name__=_C
_IpHttpPort_Object=MibScalar
ipHttpPort=_IpHttpPort_Object((1,3,6,1,4,1,3709,3,5,201,1,10,6),_IpHttpPort_Type())
ipHttpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ipHttpPort.setStatus(_A)
class _IpHttpsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_IpHttpsState_Type.__name__=_C
_IpHttpsState_Object=MibScalar
ipHttpsState=_IpHttpsState_Object((1,3,6,1,4,1,3709,3,5,201,1,10,7),_IpHttpsState_Type())
ipHttpsState.setMaxAccess(_E)
if mibBuilder.loadTexts:ipHttpsState.setStatus(_A)
class _IpHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpHttpsPort_Type.__name__=_C
_IpHttpsPort_Object=MibScalar
ipHttpsPort=_IpHttpsPort_Object((1,3,6,1,4,1,3709,3,5,201,1,10,8),_IpHttpsPort_Type())
ipHttpsPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ipHttpsPort.setStatus(_A)
class _IpTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_IpTelnetState_Type.__name__=_C
_IpTelnetState_Object=MibScalar
ipTelnetState=_IpTelnetState_Object((1,3,6,1,4,1,3709,3,5,201,1,10,9),_IpTelnetState_Type())
ipTelnetState.setMaxAccess(_E)
if mibBuilder.loadTexts:ipTelnetState.setStatus(_A)
_BcastStormMgt_ObjectIdentity=ObjectIdentity
bcastStormMgt=_BcastStormMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,11))
_BcastStormTable_Object=MibTable
bcastStormTable=_BcastStormTable_Object((1,3,6,1,4,1,3709,3,5,201,1,11,1))
if mibBuilder.loadTexts:bcastStormTable.setStatus(_A)
_BcastStormEntry_Object=MibTableRow
bcastStormEntry=_BcastStormEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,11,1,1))
bcastStormEntry.setIndexNames((0,_B,_AM))
if mibBuilder.loadTexts:bcastStormEntry.setStatus(_A)
_BcastStormIfIndex_Type=Integer32
_BcastStormIfIndex_Object=MibTableColumn
bcastStormIfIndex=_BcastStormIfIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,11,1,1,1),_BcastStormIfIndex_Type())
bcastStormIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:bcastStormIfIndex.setStatus(_A)
class _BcastStormStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_BcastStormStatus_Type.__name__=_C
_BcastStormStatus_Object=MibTableColumn
bcastStormStatus=_BcastStormStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,11,1,1,2),_BcastStormStatus_Type())
bcastStormStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:bcastStormStatus.setStatus(_A)
_BcastStormPacketRate_Type=Integer32
_BcastStormPacketRate_Object=MibTableColumn
bcastStormPacketRate=_BcastStormPacketRate_Object((1,3,6,1,4,1,3709,3,5,201,1,11,1,1,3),_BcastStormPacketRate_Type())
bcastStormPacketRate.setMaxAccess(_E)
if mibBuilder.loadTexts:bcastStormPacketRate.setStatus(_A)
_VlanMgt_ObjectIdentity=ObjectIdentity
vlanMgt=_VlanMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,12))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,3709,3,5,201,1,12,1))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,12,1,1))
vlanEntry.setIndexNames((0,_B,_AN))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
_VlanIndex_Type=Unsigned32
_VlanIndex_Object=MibTableColumn
vlanIndex=_VlanIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,12,1,1,1),_VlanIndex_Type())
vlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:vlanIndex.setStatus(_A)
class _VlanAddressMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user',1),('dhcp',2)))
_VlanAddressMethod_Type.__name__=_C
_VlanAddressMethod_Object=MibTableColumn
vlanAddressMethod=_VlanAddressMethod_Object((1,3,6,1,4,1,3709,3,5,201,1,12,1,1,2),_VlanAddressMethod_Type())
vlanAddressMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanAddressMethod.setStatus(_A)
_PriorityMgt_ObjectIdentity=ObjectIdentity
priorityMgt=_PriorityMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,13))
_PrioWrrTable_Object=MibTable
prioWrrTable=_PrioWrrTable_Object((1,3,6,1,4,1,3709,3,5,201,1,13,1))
if mibBuilder.loadTexts:prioWrrTable.setStatus(_A)
_PrioWrrEntry_Object=MibTableRow
prioWrrEntry=_PrioWrrEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,13,1,1))
prioWrrEntry.setIndexNames((0,_B,_AO))
if mibBuilder.loadTexts:prioWrrEntry.setStatus(_A)
class _PrioWrrTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PrioWrrTrafficClass_Type.__name__=_C
_PrioWrrTrafficClass_Object=MibTableColumn
prioWrrTrafficClass=_PrioWrrTrafficClass_Object((1,3,6,1,4,1,3709,3,5,201,1,13,1,1,1),_PrioWrrTrafficClass_Type())
prioWrrTrafficClass.setMaxAccess(_J)
if mibBuilder.loadTexts:prioWrrTrafficClass.setStatus(_A)
class _PrioWrrWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_PrioWrrWeight_Type.__name__=_C
_PrioWrrWeight_Object=MibTableColumn
prioWrrWeight=_PrioWrrWeight_Object((1,3,6,1,4,1,3709,3,5,201,1,13,1,1,2),_PrioWrrWeight_Type())
prioWrrWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:prioWrrWeight.setStatus(_A)
class _PrioQueueMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wrr',1),('strict',2)))
_PrioQueueMode_Type.__name__=_C
_PrioQueueMode_Object=MibScalar
prioQueueMode=_PrioQueueMode_Object((1,3,6,1,4,1,3709,3,5,201,1,13,2),_PrioQueueMode_Type())
prioQueueMode.setMaxAccess(_E)
if mibBuilder.loadTexts:prioQueueMode.setStatus(_A)
_TrapDestMgt_ObjectIdentity=ObjectIdentity
trapDestMgt=_TrapDestMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,14))
_TrapDestTable_Object=MibTable
trapDestTable=_TrapDestTable_Object((1,3,6,1,4,1,3709,3,5,201,1,14,1))
if mibBuilder.loadTexts:trapDestTable.setStatus(_A)
_TrapDestEntry_Object=MibTableRow
trapDestEntry=_TrapDestEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,14,1,1))
trapDestEntry.setIndexNames((0,_B,_AP))
if mibBuilder.loadTexts:trapDestEntry.setStatus(_A)
_TrapDestAddress_Type=IpAddress
_TrapDestAddress_Object=MibTableColumn
trapDestAddress=_TrapDestAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,14,1,1,1),_TrapDestAddress_Type())
trapDestAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:trapDestAddress.setStatus(_A)
class _TrapDestCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TrapDestCommunity_Type.__name__=_v
_TrapDestCommunity_Object=MibTableColumn
trapDestCommunity=_TrapDestCommunity_Object((1,3,6,1,4,1,3709,3,5,201,1,14,1,1,2),_TrapDestCommunity_Type())
trapDestCommunity.setMaxAccess(_L)
if mibBuilder.loadTexts:trapDestCommunity.setStatus(_A)
class _TrapDestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_R,2)))
_TrapDestStatus_Type.__name__=_C
_TrapDestStatus_Object=MibTableColumn
trapDestStatus=_TrapDestStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,1,1,3),_TrapDestStatus_Type())
trapDestStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:trapDestStatus.setStatus(_A)
class _TrapDestVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_TrapDestVersion_Type.__name__=_C
_TrapDestVersion_Object=MibTableColumn
trapDestVersion=_TrapDestVersion_Object((1,3,6,1,4,1,3709,3,5,201,1,14,1,1,4),_TrapDestVersion_Type())
trapDestVersion.setMaxAccess(_L)
if mibBuilder.loadTexts:trapDestVersion.setStatus(_A)
_TrapVar_ObjectIdentity=ObjectIdentity
trapVar=_TrapVar_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,14,2))
class _TrapForbiddenAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('web',1),('snmp',2),('telnet',3),('ssh',4)))
_TrapForbiddenAccessMode_Type.__name__=_C
_TrapForbiddenAccessMode_Object=MibScalar
trapForbiddenAccessMode=_TrapForbiddenAccessMode_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,1),_TrapForbiddenAccessMode_Type())
trapForbiddenAccessMode.setMaxAccess(_H)
if mibBuilder.loadTexts:trapForbiddenAccessMode.setStatus(_A)
_TrapForbiddenAccessIp_Type=Integer32
_TrapForbiddenAccessIp_Object=MibScalar
trapForbiddenAccessIp=_TrapForbiddenAccessIp_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,2),_TrapForbiddenAccessIp_Type())
trapForbiddenAccessIp.setMaxAccess(_H)
if mibBuilder.loadTexts:trapForbiddenAccessIp.setStatus(_A)
_TrapLoginUserName_Type=DisplayString
_TrapLoginUserName_Object=MibScalar
trapLoginUserName=_TrapLoginUserName_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,3),_TrapLoginUserName_Type())
trapLoginUserName.setMaxAccess(_H)
if mibBuilder.loadTexts:trapLoginUserName.setStatus(_A)
_TrapConfigSavePartition_Type=Integer32
_TrapConfigSavePartition_Object=MibScalar
trapConfigSavePartition=_TrapConfigSavePartition_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,4),_TrapConfigSavePartition_Type())
trapConfigSavePartition.setMaxAccess(_H)
if mibBuilder.loadTexts:trapConfigSavePartition.setStatus(_A)
class _TrapSfpPresenceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_TrapSfpPresenceStatus_Type.__name__=_C
_TrapSfpPresenceStatus_Object=MibScalar
trapSfpPresenceStatus=_TrapSfpPresenceStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,5),_TrapSfpPresenceStatus_Type())
trapSfpPresenceStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapSfpPresenceStatus.setStatus(_A)
class _TrapInfAlarmVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),('unstable',3)))
_TrapInfAlarmVal_Type.__name__=_C
_TrapInfAlarmVal_Object=MibScalar
trapInfAlarmVal=_TrapInfAlarmVal_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,6),_TrapInfAlarmVal_Type())
trapInfAlarmVal.setMaxAccess(_H)
if mibBuilder.loadTexts:trapInfAlarmVal.setStatus(_A)
_TrapDuplicatedIpVlan_Type=Integer32
_TrapDuplicatedIpVlan_Object=MibScalar
trapDuplicatedIpVlan=_TrapDuplicatedIpVlan_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,7),_TrapDuplicatedIpVlan_Type())
trapDuplicatedIpVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDuplicatedIpVlan.setStatus(_A)
_TrapDuplicatedIpAddress_Type=Integer32
_TrapDuplicatedIpAddress_Object=MibScalar
trapDuplicatedIpAddress=_TrapDuplicatedIpAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,8),_TrapDuplicatedIpAddress_Type())
trapDuplicatedIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDuplicatedIpAddress.setStatus(_A)
_TrapDuplicatedIpMacAddress_Type=MacAddress
_TrapDuplicatedIpMacAddress_Object=MibScalar
trapDuplicatedIpMacAddress=_TrapDuplicatedIpMacAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,9),_TrapDuplicatedIpMacAddress_Type())
trapDuplicatedIpMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDuplicatedIpMacAddress.setStatus(_A)
_TrapEapsDomainName_Type=DisplayString
_TrapEapsDomainName_Object=MibScalar
trapEapsDomainName=_TrapEapsDomainName_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,10),_TrapEapsDomainName_Type())
trapEapsDomainName.setMaxAccess(_H)
if mibBuilder.loadTexts:trapEapsDomainName.setStatus(_A)
_TrapEapsDomainId_Type=Integer32
_TrapEapsDomainId_Object=MibScalar
trapEapsDomainId=_TrapEapsDomainId_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,11),_TrapEapsDomainId_Type())
trapEapsDomainId.setMaxAccess(_H)
if mibBuilder.loadTexts:trapEapsDomainId.setStatus(_A)
class _TrapEapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_k,0),('complete',1),(_l,2),('links-up',3),('links-down',4),('pre-forwarding',5)))
_TrapEapsStatus_Type.__name__=_C
_TrapEapsStatus_Object=MibScalar
trapEapsStatus=_TrapEapsStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,12),_TrapEapsStatus_Type())
trapEapsStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapEapsStatus.setStatus(_A)
_TrapTemperature_Type=Integer32
_TrapTemperature_Object=MibScalar
trapTemperature=_TrapTemperature_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,13),_TrapTemperature_Type())
trapTemperature.setMaxAccess(_H)
if mibBuilder.loadTexts:trapTemperature.setStatus(_A)
_TrapFuseId_Type=Integer32
_TrapFuseId_Object=MibScalar
trapFuseId=_TrapFuseId_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,14),_TrapFuseId_Type())
trapFuseId.setMaxAccess(_H)
if mibBuilder.loadTexts:trapFuseId.setStatus(_A)
class _TrapFuseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),(_l,2)))
_TrapFuseStatus_Type.__name__=_C
_TrapFuseStatus_Object=MibScalar
trapFuseStatus=_TrapFuseStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,15),_TrapFuseStatus_Type())
trapFuseStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapFuseStatus.setStatus(_A)
class _TrapFansBoardPresenceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_TrapFansBoardPresenceStatus_Type.__name__=_C
_TrapFansBoardPresenceStatus_Object=MibScalar
trapFansBoardPresenceStatus=_TrapFansBoardPresenceStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,16),_TrapFansBoardPresenceStatus_Type())
trapFansBoardPresenceStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapFansBoardPresenceStatus.setStatus(_A)
class _TrapStandbyMpuPresenceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_TrapStandbyMpuPresenceStatus_Type.__name__=_C
_TrapStandbyMpuPresenceStatus_Object=MibScalar
trapStandbyMpuPresenceStatus=_TrapStandbyMpuPresenceStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,17),_TrapStandbyMpuPresenceStatus_Type())
trapStandbyMpuPresenceStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapStandbyMpuPresenceStatus.setStatus(_A)
_TrapMacAddressMove_Type=MacAddress
_TrapMacAddressMove_Object=MibScalar
trapMacAddressMove=_TrapMacAddressMove_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,18),_TrapMacAddressMove_Type())
trapMacAddressMove.setMaxAccess(_H)
if mibBuilder.loadTexts:trapMacAddressMove.setStatus(_A)
_TrapMemFree_Type=Integer32
_TrapMemFree_Object=MibScalar
trapMemFree=_TrapMemFree_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,19),_TrapMemFree_Type())
trapMemFree.setMaxAccess(_H)
if mibBuilder.loadTexts:trapMemFree.setStatus(_A)
_TrapBootloaderNew_Type=DisplayString
_TrapBootloaderNew_Object=MibScalar
trapBootloaderNew=_TrapBootloaderNew_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,20),_TrapBootloaderNew_Type())
trapBootloaderNew.setMaxAccess(_H)
if mibBuilder.loadTexts:trapBootloaderNew.setStatus(_A)
_TrapDevNo_Type=Integer32
_TrapDevNo_Object=MibScalar
trapDevNo=_TrapDevNo_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,21),_TrapDevNo_Type())
trapDevNo.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDevNo.setStatus(_A)
_TrapDevLocalId_Type=Integer32
_TrapDevLocalId_Object=MibScalar
trapDevLocalId=_TrapDevLocalId_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,22),_TrapDevLocalId_Type())
trapDevLocalId.setMaxAccess(_H)
if mibBuilder.loadTexts:trapDevLocalId.setStatus(_A)
class _TrapCesopTdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('los',1),('ais',2),('lof',3)))
_TrapCesopTdmStatus_Type.__name__=_C
_TrapCesopTdmStatus_Object=MibScalar
trapCesopTdmStatus=_TrapCesopTdmStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,23),_TrapCesopTdmStatus_Type())
trapCesopTdmStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopTdmStatus.setStatus(_A)
class _TrapCesopTdmRemoteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5)));namedValues=NamedValues(*((_P,0),('ralm',5)))
_TrapCesopTdmRemoteStatus_Type.__name__=_C
_TrapCesopTdmRemoteStatus_Object=MibScalar
trapCesopTdmRemoteStatus=_TrapCesopTdmRemoteStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,24),_TrapCesopTdmRemoteStatus_Type())
trapCesopTdmRemoteStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopTdmRemoteStatus.setStatus(_A)
class _TrapCesopTdmCasStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*((_P,0),('lom',4)))
_TrapCesopTdmCasStatus_Type.__name__=_C
_TrapCesopTdmCasStatus_Object=MibScalar
trapCesopTdmCasStatus=_TrapCesopTdmCasStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,25),_TrapCesopTdmCasStatus_Type())
trapCesopTdmCasStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopTdmCasStatus.setStatus(_A)
class _TrapCesopTdmCrcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6)));namedValues=NamedValues(*((_P,0),('crc',6)))
_TrapCesopTdmCrcStatus_Type.__name__=_C
_TrapCesopTdmCrcStatus_Object=MibScalar
trapCesopTdmCrcStatus=_TrapCesopTdmCrcStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,26),_TrapCesopTdmCrcStatus_Type())
trapCesopTdmCrcStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopTdmCrcStatus.setStatus(_A)
class _TrapCesopBundleLocalTdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_Q,1),('rdi',2)))
_TrapCesopBundleLocalTdmStatus_Type.__name__=_C
_TrapCesopBundleLocalTdmStatus_Object=MibScalar
trapCesopBundleLocalTdmStatus=_TrapCesopBundleLocalTdmStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,27),_TrapCesopBundleLocalTdmStatus_Type())
trapCesopBundleLocalTdmStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopBundleLocalTdmStatus.setStatus(_A)
class _TrapCesopBundleRemoteTdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_Q,1),('rdi',2)))
_TrapCesopBundleRemoteTdmStatus_Type.__name__=_C
_TrapCesopBundleRemoteTdmStatus_Object=MibScalar
trapCesopBundleRemoteTdmStatus=_TrapCesopBundleRemoteTdmStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,28),_TrapCesopBundleRemoteTdmStatus_Type())
trapCesopBundleRemoteTdmStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopBundleRemoteTdmStatus.setStatus(_A)
class _TrapCesopBundleLocalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_TrapCesopBundleLocalStatus_Type.__name__=_C
_TrapCesopBundleLocalStatus_Object=MibScalar
trapCesopBundleLocalStatus=_TrapCesopBundleLocalStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,29),_TrapCesopBundleLocalStatus_Type())
trapCesopBundleLocalStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopBundleLocalStatus.setStatus(_A)
class _TrapCesopBundleRemoteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_TrapCesopBundleRemoteStatus_Type.__name__=_C
_TrapCesopBundleRemoteStatus_Object=MibScalar
trapCesopBundleRemoteStatus=_TrapCesopBundleRemoteStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,30),_TrapCesopBundleRemoteStatus_Type())
trapCesopBundleRemoteStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopBundleRemoteStatus.setStatus(_A)
class _TrapCesopBundlePktMismatchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3)));namedValues=NamedValues(*((_P,0),('mismatch',3)))
_TrapCesopBundlePktMismatchStatus_Type.__name__=_C
_TrapCesopBundlePktMismatchStatus_Object=MibScalar
trapCesopBundlePktMismatchStatus=_TrapCesopBundlePktMismatchStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,31),_TrapCesopBundlePktMismatchStatus_Type())
trapCesopBundlePktMismatchStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopBundlePktMismatchStatus.setStatus(_A)
class _TrapCesopBundleNextHopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*(('up',0),(_S,4)))
_TrapCesopBundleNextHopStatus_Type.__name__=_C
_TrapCesopBundleNextHopStatus_Object=MibScalar
trapCesopBundleNextHopStatus=_TrapCesopBundleNextHopStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,32),_TrapCesopBundleNextHopStatus_Type())
trapCesopBundleNextHopStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopBundleNextHopStatus.setStatus(_A)
_TrapCesopClockAdapLinkQuality_Type=Integer32
_TrapCesopClockAdapLinkQuality_Object=MibScalar
trapCesopClockAdapLinkQuality=_TrapCesopClockAdapLinkQuality_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,33),_TrapCesopClockAdapLinkQuality_Type())
trapCesopClockAdapLinkQuality.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopClockAdapLinkQuality.setStatus(_A)
class _TrapCesopClockSourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_m,1)))
_TrapCesopClockSourceStatus_Type.__name__=_C
_TrapCesopClockSourceStatus_Object=MibScalar
trapCesopClockSourceStatus=_TrapCesopClockSourceStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,34),_TrapCesopClockSourceStatus_Type())
trapCesopClockSourceStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopClockSourceStatus.setStatus(_A)
class _TrapBroadcastStormControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_m,2)))
_TrapBroadcastStormControlStatus_Type.__name__=_C
_TrapBroadcastStormControlStatus_Object=MibScalar
trapBroadcastStormControlStatus=_TrapBroadcastStormControlStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,35),_TrapBroadcastStormControlStatus_Type())
trapBroadcastStormControlStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapBroadcastStormControlStatus.setStatus(_A)
_TrapBroadcastStormControlPPS_Type=Integer32
_TrapBroadcastStormControlPPS_Object=MibScalar
trapBroadcastStormControlPPS=_TrapBroadcastStormControlPPS_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,36),_TrapBroadcastStormControlPPS_Type())
trapBroadcastStormControlPPS.setMaxAccess(_H)
if mibBuilder.loadTexts:trapBroadcastStormControlPPS.setStatus(_A)
class _TrapMulticastStormControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_m,2)))
_TrapMulticastStormControlStatus_Type.__name__=_C
_TrapMulticastStormControlStatus_Object=MibScalar
trapMulticastStormControlStatus=_TrapMulticastStormControlStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,37),_TrapMulticastStormControlStatus_Type())
trapMulticastStormControlStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapMulticastStormControlStatus.setStatus(_A)
_TrapMulticastStormControlPPS_Type=Integer32
_TrapMulticastStormControlPPS_Object=MibScalar
trapMulticastStormControlPPS=_TrapMulticastStormControlPPS_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,38),_TrapMulticastStormControlPPS_Type())
trapMulticastStormControlPPS.setMaxAccess(_H)
if mibBuilder.loadTexts:trapMulticastStormControlPPS.setStatus(_A)
class _TrapStatusLDP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_S,2),('delete',3)))
_TrapStatusLDP_Type.__name__=_C
_TrapStatusLDP_Object=MibScalar
trapStatusLDP=_TrapStatusLDP_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,39),_TrapStatusLDP_Type())
trapStatusLDP.setMaxAccess(_H)
if mibBuilder.loadTexts:trapStatusLDP.setStatus(_A)
_TrapIdLDP_Type=Integer32
_TrapIdLDP_Object=MibScalar
trapIdLDP=_TrapIdLDP_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,40),_TrapIdLDP_Type())
trapIdLDP.setMaxAccess(_H)
if mibBuilder.loadTexts:trapIdLDP.setStatus(_A)
class _TrapStatusTunnelRSVP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),(_S,2),('deleted',3),('rerouted',4)))
_TrapStatusTunnelRSVP_Type.__name__=_C
_TrapStatusTunnelRSVP_Object=MibScalar
trapStatusTunnelRSVP=_TrapStatusTunnelRSVP_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,41),_TrapStatusTunnelRSVP_Type())
trapStatusTunnelRSVP.setMaxAccess(_H)
if mibBuilder.loadTexts:trapStatusTunnelRSVP.setStatus(_A)
_TrapIdTunnelRSVP_Type=Integer32
_TrapIdTunnelRSVP_Object=MibScalar
trapIdTunnelRSVP=_TrapIdTunnelRSVP_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,42),_TrapIdTunnelRSVP_Type())
trapIdTunnelRSVP.setMaxAccess(_H)
if mibBuilder.loadTexts:trapIdTunnelRSVP.setStatus(_A)
class _TrapPanelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('closed',1),('open',2)))
_TrapPanelStatus_Type.__name__=_C
_TrapPanelStatus_Object=MibScalar
trapPanelStatus=_TrapPanelStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,43),_TrapPanelStatus_Type())
trapPanelStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapPanelStatus.setStatus(_A)
_TrapLSTGroup_Type=Integer32
_TrapLSTGroup_Object=MibScalar
trapLSTGroup=_TrapLSTGroup_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,44),_TrapLSTGroup_Type())
trapLSTGroup.setMaxAccess(_H)
if mibBuilder.loadTexts:trapLSTGroup.setStatus(_A)
_TrapMemL3Free_Type=Integer32
_TrapMemL3Free_Object=MibScalar
trapMemL3Free=_TrapMemL3Free_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,45),_TrapMemL3Free_Type())
trapMemL3Free.setMaxAccess(_H)
if mibBuilder.loadTexts:trapMemL3Free.setStatus(_A)
_TrapActiveMpuNsfId_Type=Integer32
_TrapActiveMpuNsfId_Object=MibScalar
trapActiveMpuNsfId=_TrapActiveMpuNsfId_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,46),_TrapActiveMpuNsfId_Type())
trapActiveMpuNsfId.setMaxAccess(_H)
if mibBuilder.loadTexts:trapActiveMpuNsfId.setStatus(_A)
_TrapStandByMpuNsfId_Type=Integer32
_TrapStandByMpuNsfId_Object=MibScalar
trapStandByMpuNsfId=_TrapStandByMpuNsfId_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,47),_TrapStandByMpuNsfId_Type())
trapStandByMpuNsfId.setMaxAccess(_H)
if mibBuilder.loadTexts:trapStandByMpuNsfId.setStatus(_A)
_TrapErpsDomainName_Type=DisplayString
_TrapErpsDomainName_Object=MibScalar
trapErpsDomainName=_TrapErpsDomainName_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,48),_TrapErpsDomainName_Type())
trapErpsDomainName.setMaxAccess(_H)
if mibBuilder.loadTexts:trapErpsDomainName.setStatus(_A)
_TrapErpsDomainId_Type=Integer32
_TrapErpsDomainId_Object=MibScalar
trapErpsDomainId=_TrapErpsDomainId_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,49),_TrapErpsDomainId_Type())
trapErpsDomainId.setMaxAccess(_H)
if mibBuilder.loadTexts:trapErpsDomainId.setStatus(_A)
class _TrapErpsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('init',1),(_k,2),('protection',3)))
_TrapErpsStatus_Type.__name__=_C
_TrapErpsStatus_Object=MibScalar
trapErpsStatus=_TrapErpsStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,50),_TrapErpsStatus_Type())
trapErpsStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapErpsStatus.setStatus(_A)
class _TrapCfmMdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,42))
_TrapCfmMdName_Type.__name__=_K
_TrapCfmMdName_Object=MibScalar
trapCfmMdName=_TrapCfmMdName_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,51),_TrapCfmMdName_Type())
trapCfmMdName.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCfmMdName.setStatus(_A)
class _TrapCfmMaName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,44))
_TrapCfmMaName_Type.__name__=_K
_TrapCfmMaName_Object=MibScalar
trapCfmMaName=_TrapCfmMaName_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,52),_TrapCfmMaName_Type())
trapCfmMaName.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCfmMaName.setStatus(_A)
class _TrapCfmMepId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_TrapCfmMepId_Type.__name__=_C
_TrapCfmMepId_Object=MibScalar
trapCfmMepId=_TrapCfmMepId_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,53),_TrapCfmMepId_Type())
trapCfmMepId.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCfmMepId.setStatus(_A)
class _TrapCfmVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TrapCfmVlan_Type.__name__=_C
_TrapCfmVlan_Object=MibScalar
trapCfmVlan=_TrapCfmVlan_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,54),_TrapCfmVlan_Type())
trapCfmVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCfmVlan.setStatus(_A)
class _TrapCfmDefect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('defNone',0),('defRDICCM',1),('defMACstatus',2),('defRemoteCCM',3),('defErrorCCM',4),('defXconCCM',5)))
_TrapCfmDefect_Type.__name__=_C
_TrapCfmDefect_Object=MibScalar
trapCfmDefect=_TrapCfmDefect_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,55),_TrapCfmDefect_Type())
trapCfmDefect.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCfmDefect.setStatus(_A)
_TrapEvcName_Type=DisplayString
_TrapEvcName_Object=MibScalar
trapEvcName=_TrapEvcName_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,56),_TrapEvcName_Type())
trapEvcName.setMaxAccess(_H)
if mibBuilder.loadTexts:trapEvcName.setStatus(_A)
class _TrapEvcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('notActive',0),('newAndNotActive',1),('active',2),('newAndActive',3),('partiallyActive',4),('newAndPartiallyActive',5)))
_TrapEvcStatus_Type.__name__=_C
_TrapEvcStatus_Object=MibScalar
trapEvcStatus=_TrapEvcStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,57),_TrapEvcStatus_Type())
trapEvcStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapEvcStatus.setStatus(_A)
class _TrapSyncSystemClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('freerun',1),('holdover',2),('acquiring',3),('locked',4)))
_TrapSyncSystemClockStatus_Type.__name__=_C
_TrapSyncSystemClockStatus_Object=MibScalar
trapSyncSystemClockStatus=_TrapSyncSystemClockStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,58),_TrapSyncSystemClockStatus_Type())
trapSyncSystemClockStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapSyncSystemClockStatus.setStatus(_A)
class _TrapCesopG704ClockSourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(7,9,10)));namedValues=NamedValues(*(('dontcare',7),('locked',9),(_Q,10)))
_TrapCesopG704ClockSourceStatus_Type.__name__=_C
_TrapCesopG704ClockSourceStatus_Object=MibScalar
trapCesopG704ClockSourceStatus=_TrapCesopG704ClockSourceStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,59),_TrapCesopG704ClockSourceStatus_Type())
trapCesopG704ClockSourceStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:trapCesopG704ClockSourceStatus.setStatus(_A)
class _TrapSystemWarningsUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sysWarUnitsHsEnNoError',1),('sysWarUnitsHsEnWES',2),('sysWarUnitsHsEnWHSDis',3),('sysWarUnitsHsEnWDifMod',4),('sysWarUnitsCommFail',5),('sysWarUnitsMPLS',6),('sysWarUnitsL3',7)))
_TrapSystemWarningsUnits_Type.__name__=_C
_TrapSystemWarningsUnits_Object=MibScalar
trapSystemWarningsUnits=_TrapSystemWarningsUnits_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,60),_TrapSystemWarningsUnits_Type())
trapSystemWarningsUnits.setMaxAccess(_H)
if mibBuilder.loadTexts:trapSystemWarningsUnits.setStatus(_A)
class _TrapSensorGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('boardSensors',1),('chipsetSensors',2)))
_TrapSensorGroup_Type.__name__=_C
_TrapSensorGroup_Object=MibScalar
trapSensorGroup=_TrapSensorGroup_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,61),_TrapSensorGroup_Type())
trapSensorGroup.setMaxAccess(_H)
if mibBuilder.loadTexts:trapSensorGroup.setStatus(_A)
_TrapIpNeighborLDP_Type=IpAddress
_TrapIpNeighborLDP_Object=MibScalar
trapIpNeighborLDP=_TrapIpNeighborLDP_Object((1,3,6,1,4,1,3709,3,5,201,1,14,2,62),_TrapIpNeighborLDP_Type())
trapIpNeighborLDP.setMaxAccess(_H)
if mibBuilder.loadTexts:trapIpNeighborLDP.setStatus(_A)
_RateLimitMgt_ObjectIdentity=ObjectIdentity
rateLimitMgt=_RateLimitMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,16))
_RateLimitPortTable_Object=MibTable
rateLimitPortTable=_RateLimitPortTable_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1))
if mibBuilder.loadTexts:rateLimitPortTable.setStatus(_A)
_RateLimitPortEntry_Object=MibTableRow
rateLimitPortEntry=_RateLimitPortEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1))
rateLimitPortEntry.setIndexNames((0,_B,_AQ))
if mibBuilder.loadTexts:rateLimitPortEntry.setStatus(_A)
_RlPortIndex_Type=Integer32
_RlPortIndex_Object=MibTableColumn
rlPortIndex=_RlPortIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1,1),_RlPortIndex_Type())
rlPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:rlPortIndex.setStatus(_A)
class _RlPortInputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RlPortInputStatus_Type.__name__=_C
_RlPortInputStatus_Object=MibTableColumn
rlPortInputStatus=_RlPortInputStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1,2),_RlPortInputStatus_Type())
rlPortInputStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPortInputStatus.setStatus(_A)
class _RlPortOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RlPortOutputStatus_Type.__name__=_C
_RlPortOutputStatus_Object=MibTableColumn
rlPortOutputStatus=_RlPortOutputStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1,3),_RlPortOutputStatus_Type())
rlPortOutputStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPortOutputStatus.setStatus(_A)
class _RlPortInputRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1000000))
_RlPortInputRate_Type.__name__=_C
_RlPortInputRate_Object=MibTableColumn
rlPortInputRate=_RlPortInputRate_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1,4),_RlPortInputRate_Type())
rlPortInputRate.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPortInputRate.setStatus(_A)
class _RlPortInputBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4096))
_RlPortInputBurst_Type.__name__=_C
_RlPortInputBurst_Object=MibTableColumn
rlPortInputBurst=_RlPortInputBurst_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1,5),_RlPortInputBurst_Type())
rlPortInputBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPortInputBurst.setStatus(_A)
class _RlPortOutputRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1000000))
_RlPortOutputRate_Type.__name__=_C
_RlPortOutputRate_Object=MibTableColumn
rlPortOutputRate=_RlPortOutputRate_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1,6),_RlPortOutputRate_Type())
rlPortOutputRate.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPortOutputRate.setStatus(_A)
class _RlPortOutputBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4096))
_RlPortOutputBurst_Type.__name__=_C
_RlPortOutputBurst_Object=MibTableColumn
rlPortOutputBurst=_RlPortOutputBurst_Object((1,3,6,1,4,1,3709,3,5,201,1,16,1,1,7),_RlPortOutputBurst_Type())
rlPortOutputBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPortOutputBurst.setStatus(_A)
_SecurityMgt_ObjectIdentity=ObjectIdentity
securityMgt=_SecurityMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,17))
_RadiusMgt_ObjectIdentity=ObjectIdentity
radiusMgt=_RadiusMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,17,1))
class _RadiusServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusServerPortNumber_Type.__name__=_C
_RadiusServerPortNumber_Object=MibScalar
radiusServerPortNumber=_RadiusServerPortNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,2),_RadiusServerPortNumber_Type())
radiusServerPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusServerPortNumber.setStatus(_A)
_RadiusServerKey_Type=DisplayString
_RadiusServerKey_Object=MibScalar
radiusServerKey=_RadiusServerKey_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,3),_RadiusServerKey_Type())
radiusServerKey.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusServerKey.setStatus(_A)
class _RadiusServerRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_RadiusServerRetransmit_Type.__name__=_C
_RadiusServerRetransmit_Object=MibScalar
radiusServerRetransmit=_RadiusServerRetransmit_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,4),_RadiusServerRetransmit_Type())
radiusServerRetransmit.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusServerRetransmit.setStatus(_A)
class _RadiusServerTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusServerTimeout_Type.__name__=_C
_RadiusServerTimeout_Object=MibScalar
radiusServerTimeout=_RadiusServerTimeout_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,5),_RadiusServerTimeout_Type())
radiusServerTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusServerTimeout.setStatus(_A)
_RadiusMultipleServerTable_Object=MibTable
radiusMultipleServerTable=_RadiusMultipleServerTable_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7))
if mibBuilder.loadTexts:radiusMultipleServerTable.setStatus(_A)
_RadiusMultipleServerEntry_Object=MibTableRow
radiusMultipleServerEntry=_RadiusMultipleServerEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1))
radiusMultipleServerEntry.setIndexNames((0,_B,_AR))
if mibBuilder.loadTexts:radiusMultipleServerEntry.setStatus(_A)
_RadiusMultipleServerIndex_Type=Integer32
_RadiusMultipleServerIndex_Object=MibTableColumn
radiusMultipleServerIndex=_RadiusMultipleServerIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1,1),_RadiusMultipleServerIndex_Type())
radiusMultipleServerIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:radiusMultipleServerIndex.setStatus(_A)
_RadiusMultipleServerAddress_Type=IpAddress
_RadiusMultipleServerAddress_Object=MibTableColumn
radiusMultipleServerAddress=_RadiusMultipleServerAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1,2),_RadiusMultipleServerAddress_Type())
radiusMultipleServerAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:radiusMultipleServerAddress.setStatus(_A)
class _RadiusMultipleServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusMultipleServerPortNumber_Type.__name__=_C
_RadiusMultipleServerPortNumber_Object=MibTableColumn
radiusMultipleServerPortNumber=_RadiusMultipleServerPortNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1,3),_RadiusMultipleServerPortNumber_Type())
radiusMultipleServerPortNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:radiusMultipleServerPortNumber.setStatus(_A)
_RadiusMultipleServerKey_Type=DisplayString
_RadiusMultipleServerKey_Object=MibTableColumn
radiusMultipleServerKey=_RadiusMultipleServerKey_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1,4),_RadiusMultipleServerKey_Type())
radiusMultipleServerKey.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusMultipleServerKey.setStatus(_A)
class _RadiusMultipleServerRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_RadiusMultipleServerRetransmit_Type.__name__=_C
_RadiusMultipleServerRetransmit_Object=MibTableColumn
radiusMultipleServerRetransmit=_RadiusMultipleServerRetransmit_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1,5),_RadiusMultipleServerRetransmit_Type())
radiusMultipleServerRetransmit.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusMultipleServerRetransmit.setStatus(_A)
class _RadiusMultipleServerTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusMultipleServerTimeout_Type.__name__=_C
_RadiusMultipleServerTimeout_Object=MibTableColumn
radiusMultipleServerTimeout=_RadiusMultipleServerTimeout_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1,6),_RadiusMultipleServerTimeout_Type())
radiusMultipleServerTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusMultipleServerTimeout.setStatus(_A)
_RadiusMultipleServerStatus_Type=ValidStatus
_RadiusMultipleServerStatus_Object=MibTableColumn
radiusMultipleServerStatus=_RadiusMultipleServerStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,17,1,7,1,8),_RadiusMultipleServerStatus_Type())
radiusMultipleServerStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:radiusMultipleServerStatus.setStatus(_A)
_SshMgt_ObjectIdentity=ObjectIdentity
sshMgt=_SshMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,17,2))
_SshServerStatus_Type=EnabledStatus
_SshServerStatus_Object=MibScalar
sshServerStatus=_SshServerStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,1),_SshServerStatus_Type())
sshServerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerStatus.setStatus(_A)
_SshServerMajorVersion_Type=Integer32
_SshServerMajorVersion_Object=MibScalar
sshServerMajorVersion=_SshServerMajorVersion_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,2),_SshServerMajorVersion_Type())
sshServerMajorVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:sshServerMajorVersion.setStatus(_A)
_SshServerMinorVersion_Type=Integer32
_SshServerMinorVersion_Object=MibScalar
sshServerMinorVersion=_SshServerMinorVersion_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,3),_SshServerMinorVersion_Type())
sshServerMinorVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:sshServerMinorVersion.setStatus(_A)
class _SshTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_SshTimeout_Type.__name__=_C
_SshTimeout_Object=MibScalar
sshTimeout=_SshTimeout_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,4),_SshTimeout_Type())
sshTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:sshTimeout.setStatus(_A)
if mibBuilder.loadTexts:sshTimeout.setUnits('seconds')
class _SshKeySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,896))
_SshKeySize_Type.__name__=_C
_SshKeySize_Object=MibScalar
sshKeySize=_SshKeySize_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,5),_SshKeySize_Type())
sshKeySize.setMaxAccess(_E)
if mibBuilder.loadTexts:sshKeySize.setStatus(_A)
_SshRsaHostKey_Type=KeySegment
_SshRsaHostKey_Object=MibScalar
sshRsaHostKey=_SshRsaHostKey_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,6),_SshRsaHostKey_Type())
sshRsaHostKey.setMaxAccess(_D)
if mibBuilder.loadTexts:sshRsaHostKey.setStatus(_A)
_SshDsaHostKey_Type=KeySegment
_SshDsaHostKey_Object=MibScalar
sshDsaHostKey=_SshDsaHostKey_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,7),_SshDsaHostKey_Type())
sshDsaHostKey.setMaxAccess(_D)
if mibBuilder.loadTexts:sshDsaHostKey.setStatus(_A)
class _SshHostKeyGenAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noGen',1),('genRsaKey',2),('genDsaKey',3),('genBothKeys',4)))
_SshHostKeyGenAction_Type.__name__=_C
_SshHostKeyGenAction_Object=MibScalar
sshHostKeyGenAction=_SshHostKeyGenAction_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,8),_SshHostKeyGenAction_Type())
sshHostKeyGenAction.setMaxAccess(_E)
if mibBuilder.loadTexts:sshHostKeyGenAction.setStatus(_A)
class _SshHostKeyDelAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noDel',1),('delRsaKey',2),('delDsaKey',3),('delBothKeys',4)))
_SshHostKeyDelAction_Type.__name__=_C
_SshHostKeyDelAction_Object=MibScalar
sshHostKeyDelAction=_SshHostKeyDelAction_Object((1,3,6,1,4,1,3709,3,5,201,1,17,2,9),_SshHostKeyDelAction_Type())
sshHostKeyDelAction.setMaxAccess(_E)
if mibBuilder.loadTexts:sshHostKeyDelAction.setStatus(_A)
_IpFilterMgt_ObjectIdentity=ObjectIdentity
ipFilterMgt=_IpFilterMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,17,3))
_IpFilterSnmpTable_Object=MibTable
ipFilterSnmpTable=_IpFilterSnmpTable_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,1))
if mibBuilder.loadTexts:ipFilterSnmpTable.setStatus(_A)
_IpFilterSnmpEntry_Object=MibTableRow
ipFilterSnmpEntry=_IpFilterSnmpEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,1,1))
ipFilterSnmpEntry.setIndexNames((0,_B,_AS),(0,_B,_AT))
if mibBuilder.loadTexts:ipFilterSnmpEntry.setStatus(_A)
_IpFilterSnmpAddress_Type=IpAddress
_IpFilterSnmpAddress_Object=MibTableColumn
ipFilterSnmpAddress=_IpFilterSnmpAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,1,1,1),_IpFilterSnmpAddress_Type())
ipFilterSnmpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterSnmpAddress.setStatus(_A)
_IpFilterSnmpMask_Type=IpAddress
_IpFilterSnmpMask_Object=MibTableColumn
ipFilterSnmpMask=_IpFilterSnmpMask_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,1,1,2),_IpFilterSnmpMask_Type())
ipFilterSnmpMask.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterSnmpMask.setStatus(_A)
_IpFilterSnmpStatus_Type=ValidStatus
_IpFilterSnmpStatus_Object=MibTableColumn
ipFilterSnmpStatus=_IpFilterSnmpStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,1,1,3),_IpFilterSnmpStatus_Type())
ipFilterSnmpStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:ipFilterSnmpStatus.setStatus(_A)
_IpFilterHTTPTable_Object=MibTable
ipFilterHTTPTable=_IpFilterHTTPTable_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,2))
if mibBuilder.loadTexts:ipFilterHTTPTable.setStatus(_A)
_IpFilterHTTPEntry_Object=MibTableRow
ipFilterHTTPEntry=_IpFilterHTTPEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,2,1))
ipFilterHTTPEntry.setIndexNames((0,_B,_AU),(0,_B,_AV))
if mibBuilder.loadTexts:ipFilterHTTPEntry.setStatus(_A)
_IpFilterHTTPAddress_Type=IpAddress
_IpFilterHTTPAddress_Object=MibTableColumn
ipFilterHTTPAddress=_IpFilterHTTPAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,2,1,1),_IpFilterHTTPAddress_Type())
ipFilterHTTPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterHTTPAddress.setStatus(_A)
_IpFilterHTTPMask_Type=IpAddress
_IpFilterHTTPMask_Object=MibTableColumn
ipFilterHTTPMask=_IpFilterHTTPMask_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,2,1,2),_IpFilterHTTPMask_Type())
ipFilterHTTPMask.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterHTTPMask.setStatus(_A)
_IpFilterHTTPStatus_Type=ValidStatus
_IpFilterHTTPStatus_Object=MibTableColumn
ipFilterHTTPStatus=_IpFilterHTTPStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,2,1,3),_IpFilterHTTPStatus_Type())
ipFilterHTTPStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:ipFilterHTTPStatus.setStatus(_A)
_IpFilterTelnetTable_Object=MibTable
ipFilterTelnetTable=_IpFilterTelnetTable_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,3))
if mibBuilder.loadTexts:ipFilterTelnetTable.setStatus(_A)
_IpFilterTelnetEntry_Object=MibTableRow
ipFilterTelnetEntry=_IpFilterTelnetEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,3,1))
ipFilterTelnetEntry.setIndexNames((0,_B,_AW),(0,_B,_AX))
if mibBuilder.loadTexts:ipFilterTelnetEntry.setStatus(_A)
_IpFilterTelnetAddress_Type=IpAddress
_IpFilterTelnetAddress_Object=MibTableColumn
ipFilterTelnetAddress=_IpFilterTelnetAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,3,1,1),_IpFilterTelnetAddress_Type())
ipFilterTelnetAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterTelnetAddress.setStatus(_A)
_IpFilterTelnetMask_Type=IpAddress
_IpFilterTelnetMask_Object=MibTableColumn
ipFilterTelnetMask=_IpFilterTelnetMask_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,3,1,2),_IpFilterTelnetMask_Type())
ipFilterTelnetMask.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterTelnetMask.setStatus(_A)
_IpFilterTelnetStatus_Type=ValidStatus
_IpFilterTelnetStatus_Object=MibTableColumn
ipFilterTelnetStatus=_IpFilterTelnetStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,3,1,3),_IpFilterTelnetStatus_Type())
ipFilterTelnetStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:ipFilterTelnetStatus.setStatus(_A)
_IpFilterSSHTable_Object=MibTable
ipFilterSSHTable=_IpFilterSSHTable_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,4))
if mibBuilder.loadTexts:ipFilterSSHTable.setStatus(_A)
_IpFilterSSHEntry_Object=MibTableRow
ipFilterSSHEntry=_IpFilterSSHEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,4,1))
ipFilterSSHEntry.setIndexNames((0,_B,_AY),(0,_B,_AZ))
if mibBuilder.loadTexts:ipFilterSSHEntry.setStatus(_A)
_IpFilterSSHAddress_Type=IpAddress
_IpFilterSSHAddress_Object=MibTableColumn
ipFilterSSHAddress=_IpFilterSSHAddress_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,4,1,1),_IpFilterSSHAddress_Type())
ipFilterSSHAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterSSHAddress.setStatus(_A)
_IpFilterSSHMask_Type=IpAddress
_IpFilterSSHMask_Object=MibTableColumn
ipFilterSSHMask=_IpFilterSSHMask_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,4,1,2),_IpFilterSSHMask_Type())
ipFilterSSHMask.setMaxAccess(_J)
if mibBuilder.loadTexts:ipFilterSSHMask.setStatus(_A)
_IpFilterSSHStatus_Type=ValidStatus
_IpFilterSSHStatus_Object=MibTableColumn
ipFilterSSHStatus=_IpFilterSSHStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,17,3,4,1,3),_IpFilterSSHStatus_Type())
ipFilterSSHStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:ipFilterSSHStatus.setStatus(_A)
_SysLogMgt_ObjectIdentity=ObjectIdentity
sysLogMgt=_SysLogMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,19))
class _SysLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SysLogStatus_Type.__name__=_C
_SysLogStatus_Object=MibScalar
sysLogStatus=_SysLogStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,19,1),_SysLogStatus_Type())
sysLogStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sysLogStatus.setStatus(_A)
class _SysLogHistoryFlashLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SysLogHistoryFlashLevel_Type.__name__=_C
_SysLogHistoryFlashLevel_Object=MibScalar
sysLogHistoryFlashLevel=_SysLogHistoryFlashLevel_Object((1,3,6,1,4,1,3709,3,5,201,1,19,2),_SysLogHistoryFlashLevel_Type())
sysLogHistoryFlashLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:sysLogHistoryFlashLevel.setStatus(_A)
class _SysLogHistoryRamLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SysLogHistoryRamLevel_Type.__name__=_C
_SysLogHistoryRamLevel_Object=MibScalar
sysLogHistoryRamLevel=_SysLogHistoryRamLevel_Object((1,3,6,1,4,1,3709,3,5,201,1,19,3),_SysLogHistoryRamLevel_Type())
sysLogHistoryRamLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:sysLogHistoryRamLevel.setStatus(_A)
_RemoteLogMgt_ObjectIdentity=ObjectIdentity
remoteLogMgt=_RemoteLogMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,19,6))
_RemoteLogStatus_Type=EnabledStatus
_RemoteLogStatus_Object=MibScalar
remoteLogStatus=_RemoteLogStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,19,6,1),_RemoteLogStatus_Type())
remoteLogStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:remoteLogStatus.setStatus(_A)
class _RemoteLogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RemoteLogLevel_Type.__name__=_C
_RemoteLogLevel_Object=MibScalar
remoteLogLevel=_RemoteLogLevel_Object((1,3,6,1,4,1,3709,3,5,201,1,19,6,2),_RemoteLogLevel_Type())
remoteLogLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:remoteLogLevel.setStatus(_A)
class _RemoteLogFacilityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('localUse0',16),('localUse1',17),('localUse2',18),('localUse3',19),('localUse4',20),('localUse5',21),('localUse6',22),('localUse7',23)))
_RemoteLogFacilityType_Type.__name__=_C
_RemoteLogFacilityType_Object=MibScalar
remoteLogFacilityType=_RemoteLogFacilityType_Object((1,3,6,1,4,1,3709,3,5,201,1,19,6,3),_RemoteLogFacilityType_Type())
remoteLogFacilityType.setMaxAccess(_E)
if mibBuilder.loadTexts:remoteLogFacilityType.setStatus(_A)
_RemoteLogServerTable_Object=MibTable
remoteLogServerTable=_RemoteLogServerTable_Object((1,3,6,1,4,1,3709,3,5,201,1,19,6,4))
if mibBuilder.loadTexts:remoteLogServerTable.setStatus(_A)
_RemoteLogServerEntry_Object=MibTableRow
remoteLogServerEntry=_RemoteLogServerEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,19,6,4,1))
remoteLogServerEntry.setIndexNames((0,_B,_Aa))
if mibBuilder.loadTexts:remoteLogServerEntry.setStatus(_A)
_RemoteLogServerIp_Type=IpAddress
_RemoteLogServerIp_Object=MibTableColumn
remoteLogServerIp=_RemoteLogServerIp_Object((1,3,6,1,4,1,3709,3,5,201,1,19,6,4,1,1),_RemoteLogServerIp_Type())
remoteLogServerIp.setMaxAccess(_L)
if mibBuilder.loadTexts:remoteLogServerIp.setStatus(_A)
_RemoteLogServerStatus_Type=ValidStatus
_RemoteLogServerStatus_Object=MibTableColumn
remoteLogServerStatus=_RemoteLogServerStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,19,6,4,1,2),_RemoteLogServerStatus_Type())
remoteLogServerStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:remoteLogServerStatus.setStatus(_A)
_SysTimeMgt_ObjectIdentity=ObjectIdentity
sysTimeMgt=_SysTimeMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,20))
_SntpMgt_ObjectIdentity=ObjectIdentity
sntpMgt=_SntpMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,20,1))
class _SntpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SntpStatus_Type.__name__=_C
_SntpStatus_Object=MibScalar
sntpStatus=_SntpStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,20,1,1),_SntpStatus_Type())
sntpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sntpStatus.setStatus(_A)
class _SntpPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16384))
_SntpPollInterval_Type.__name__=_C
_SntpPollInterval_Object=MibScalar
sntpPollInterval=_SntpPollInterval_Object((1,3,6,1,4,1,3709,3,5,201,1,20,1,2),_SntpPollInterval_Type())
sntpPollInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:sntpPollInterval.setStatus(_A)
_SntpServerTable_Object=MibTable
sntpServerTable=_SntpServerTable_Object((1,3,6,1,4,1,3709,3,5,201,1,20,1,3))
if mibBuilder.loadTexts:sntpServerTable.setStatus(_A)
_SntpServerEntry_Object=MibTableRow
sntpServerEntry=_SntpServerEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,20,1,3,1))
sntpServerEntry.setIndexNames((0,_B,_Ab))
if mibBuilder.loadTexts:sntpServerEntry.setStatus(_A)
_SntpServerIp_Type=IpAddress
_SntpServerIp_Object=MibTableColumn
sntpServerIp=_SntpServerIp_Object((1,3,6,1,4,1,3709,3,5,201,1,20,1,3,1,1),_SntpServerIp_Type())
sntpServerIp.setMaxAccess(_L)
if mibBuilder.loadTexts:sntpServerIp.setStatus(_A)
_SntpServerStatus_Type=ValidStatus
_SntpServerStatus_Object=MibTableColumn
sntpServerStatus=_SntpServerStatus_Object((1,3,6,1,4,1,3709,3,5,201,1,20,1,3,1,2),_SntpServerStatus_Type())
sntpServerStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:sntpServerStatus.setStatus(_A)
class _SysCurrentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_SysCurrentTime_Type.__name__=_K
_SysCurrentTime_Object=MibScalar
sysCurrentTime=_SysCurrentTime_Object((1,3,6,1,4,1,3709,3,5,201,1,20,2),_SysCurrentTime_Type())
sysCurrentTime.setMaxAccess(_E)
if mibBuilder.loadTexts:sysCurrentTime.setStatus(_A)
class _SysTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SysTimeZone_Type.__name__=_K
_SysTimeZone_Object=MibScalar
sysTimeZone=_SysTimeZone_Object((1,3,6,1,4,1,3709,3,5,201,1,20,3),_SysTimeZone_Type())
sysTimeZone.setMaxAccess(_E)
if mibBuilder.loadTexts:sysTimeZone.setStatus(_A)
class _SysTimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_SysTimeZoneName_Type.__name__=_K
_SysTimeZoneName_Object=MibScalar
sysTimeZoneName=_SysTimeZoneName_Object((1,3,6,1,4,1,3709,3,5,201,1,20,4),_SysTimeZoneName_Type())
sysTimeZoneName.setMaxAccess(_E)
if mibBuilder.loadTexts:sysTimeZoneName.setStatus(_A)
_FileMgt_ObjectIdentity=ObjectIdentity
fileMgt=_FileMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,21))
_FileInfoTable_Object=MibTable
fileInfoTable=_FileInfoTable_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1))
if mibBuilder.loadTexts:fileInfoTable.setStatus(_A)
_FileInfoEntry_Object=MibTableRow
fileInfoEntry=_FileInfoEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1))
fileInfoEntry.setIndexNames((0,_B,_Ac),(0,_B,_Ad))
if mibBuilder.loadTexts:fileInfoEntry.setStatus(_A)
_FileInfoUnitID_Type=Integer32
_FileInfoUnitID_Object=MibTableColumn
fileInfoUnitID=_FileInfoUnitID_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,1),_FileInfoUnitID_Type())
fileInfoUnitID.setMaxAccess(_J)
if mibBuilder.loadTexts:fileInfoUnitID.setStatus(_A)
_FileInfoFileIndex_Type=Integer32
_FileInfoFileIndex_Object=MibTableColumn
fileInfoFileIndex=_FileInfoFileIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,2),_FileInfoFileIndex_Type())
fileInfoFileIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fileInfoFileIndex.setStatus(_A)
_FileInfoFlashId_Type=Integer32
_FileInfoFlashId_Object=MibTableColumn
fileInfoFlashId=_FileInfoFlashId_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,3),_FileInfoFlashId_Type())
fileInfoFlashId.setMaxAccess(_D)
if mibBuilder.loadTexts:fileInfoFlashId.setStatus(_A)
class _FileInfoFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FileInfoFileName_Type.__name__=_K
_FileInfoFileName_Object=MibTableColumn
fileInfoFileName=_FileInfoFileName_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,4),_FileInfoFileName_Type())
fileInfoFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:fileInfoFileName.setStatus(_A)
class _FileInfoFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('firmware',1),('config',2)))
_FileInfoFileType_Type.__name__=_C
_FileInfoFileType_Object=MibTableColumn
fileInfoFileType=_FileInfoFileType_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,5),_FileInfoFileType_Type())
fileInfoFileType.setMaxAccess(_D)
if mibBuilder.loadTexts:fileInfoFileType.setStatus(_A)
_FileInfoIsStartUp_Type=TruthValue
_FileInfoIsStartUp_Object=MibTableColumn
fileInfoIsStartUp=_FileInfoIsStartUp_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,6),_FileInfoIsStartUp_Type())
fileInfoIsStartUp.setMaxAccess(_E)
if mibBuilder.loadTexts:fileInfoIsStartUp.setStatus(_A)
_FileInfoFileSize_Type=Integer32
_FileInfoFileSize_Object=MibTableColumn
fileInfoFileSize=_FileInfoFileSize_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,7),_FileInfoFileSize_Type())
fileInfoFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:fileInfoFileSize.setStatus(_A)
if mibBuilder.loadTexts:fileInfoFileSize.setUnits('bytes')
class _FileInfoCreationTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_FileInfoCreationTime_Type.__name__=_K
_FileInfoCreationTime_Object=MibTableColumn
fileInfoCreationTime=_FileInfoCreationTime_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,8),_FileInfoCreationTime_Type())
fileInfoCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fileInfoCreationTime.setStatus(_A)
class _FileInfoDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noDelete',1),('delete',2)))
_FileInfoDelete_Type.__name__=_C
_FileInfoDelete_Object=MibTableColumn
fileInfoDelete=_FileInfoDelete_Object((1,3,6,1,4,1,3709,3,5,201,1,21,1,1,9),_FileInfoDelete_Type())
fileInfoDelete.setMaxAccess(_E)
if mibBuilder.loadTexts:fileInfoDelete.setStatus(_A)
_CountMgt_ObjectIdentity=ObjectIdentity
countMgt=_CountMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,22))
_CountHoldPktsTable_Object=MibTable
countHoldPktsTable=_CountHoldPktsTable_Object((1,3,6,1,4,1,3709,3,5,201,1,22,1))
if mibBuilder.loadTexts:countHoldPktsTable.setStatus(_A)
_CountHoldPktsEntry_Object=MibTableRow
countHoldPktsEntry=_CountHoldPktsEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,22,1,1))
countHoldPktsEntry.setIndexNames((0,_B,_Ae))
if mibBuilder.loadTexts:countHoldPktsEntry.setStatus(_A)
_InterfaceNumber_Type=Integer32
_InterfaceNumber_Object=MibTableColumn
interfaceNumber=_InterfaceNumber_Object((1,3,6,1,4,1,3709,3,5,201,1,22,1,1,1),_InterfaceNumber_Type())
interfaceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceNumber.setStatus(_A)
_CountHoldPkts_Type=Counter64
_CountHoldPkts_Object=MibTableColumn
countHoldPkts=_CountHoldPkts_Object((1,3,6,1,4,1,3709,3,5,201,1,22,1,1,2),_CountHoldPkts_Type())
countHoldPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:countHoldPkts.setStatus(_A)
_FilterCounterMgt_ObjectIdentity=ObjectIdentity
filterCounterMgt=_FilterCounterMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,23))
_FilterCounterInfoTable_Object=MibTable
filterCounterInfoTable=_FilterCounterInfoTable_Object((1,3,6,1,4,1,3709,3,5,201,1,23,1))
if mibBuilder.loadTexts:filterCounterInfoTable.setStatus(_A)
_FilterCounterInfoEntry_Object=MibTableRow
filterCounterInfoEntry=_FilterCounterInfoEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,23,1,1))
filterCounterInfoEntry.setIndexNames((0,_B,_n))
if mibBuilder.loadTexts:filterCounterInfoEntry.setStatus(_A)
_FilterCounterInfoIndex_Type=Integer32
_FilterCounterInfoIndex_Object=MibTableColumn
filterCounterInfoIndex=_FilterCounterInfoIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,23,1,1,1),_FilterCounterInfoIndex_Type())
filterCounterInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:filterCounterInfoIndex.setStatus(_A)
class _FilterCounterInfoRemark_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FilterCounterInfoRemark_Type.__name__=_K
_FilterCounterInfoRemark_Object=MibTableColumn
filterCounterInfoRemark=_FilterCounterInfoRemark_Object((1,3,6,1,4,1,3709,3,5,201,1,23,1,1,2),_FilterCounterInfoRemark_Type())
filterCounterInfoRemark.setMaxAccess(_D)
if mibBuilder.loadTexts:filterCounterInfoRemark.setStatus(_A)
_FilterCounterValueTable_Object=MibTable
filterCounterValueTable=_FilterCounterValueTable_Object((1,3,6,1,4,1,3709,3,5,201,1,23,2))
if mibBuilder.loadTexts:filterCounterValueTable.setStatus(_A)
_FilterCounterValueEntry_Object=MibTableRow
filterCounterValueEntry=_FilterCounterValueEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,23,2,1))
filterCounterValueEntry.setIndexNames((0,_B,_n),(0,_B,_Af))
if mibBuilder.loadTexts:filterCounterValueEntry.setStatus(_A)
_FilterCounterValueIndex_Type=Integer32
_FilterCounterValueIndex_Object=MibTableColumn
filterCounterValueIndex=_FilterCounterValueIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,23,2,1,1),_FilterCounterValueIndex_Type())
filterCounterValueIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:filterCounterValueIndex.setStatus(_A)
_FilterCounterValue_Type=Counter64
_FilterCounterValue_Object=MibTableColumn
filterCounterValue=_FilterCounterValue_Object((1,3,6,1,4,1,3709,3,5,201,1,23,2,1,2),_FilterCounterValue_Type())
filterCounterValue.setMaxAccess(_D)
if mibBuilder.loadTexts:filterCounterValue.setStatus(_A)
_EapsMgt_ObjectIdentity=ObjectIdentity
eapsMgt=_EapsMgt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,24))
_EapsInfoTable_Object=MibTable
eapsInfoTable=_EapsInfoTable_Object((1,3,6,1,4,1,3709,3,5,201,1,24,1))
if mibBuilder.loadTexts:eapsInfoTable.setStatus(_A)
_EapsInfoEntry_Object=MibTableRow
eapsInfoEntry=_EapsInfoEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,24,1,1))
eapsInfoEntry.setIndexNames((0,_B,_Ag))
if mibBuilder.loadTexts:eapsInfoEntry.setStatus(_A)
_EapsInfoId_Type=Integer32
_EapsInfoId_Object=MibTableColumn
eapsInfoId=_EapsInfoId_Object((1,3,6,1,4,1,3709,3,5,201,1,24,1,1,1),_EapsInfoId_Type())
eapsInfoId.setMaxAccess(_D)
if mibBuilder.loadTexts:eapsInfoId.setStatus(_A)
class _EapsInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EapsInfoName_Type.__name__=_K
_EapsInfoName_Object=MibTableColumn
eapsInfoName=_EapsInfoName_Object((1,3,6,1,4,1,3709,3,5,201,1,24,1,1,2),_EapsInfoName_Type())
eapsInfoName.setMaxAccess(_D)
if mibBuilder.loadTexts:eapsInfoName.setStatus(_A)
class _EapsInfoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),(_w,1),('transit',2)))
_EapsInfoMode_Type.__name__=_C
_EapsInfoMode_Object=MibTableColumn
eapsInfoMode=_EapsInfoMode_Object((1,3,6,1,4,1,3709,3,5,201,1,24,1,1,3),_EapsInfoMode_Type())
eapsInfoMode.setMaxAccess(_D)
if mibBuilder.loadTexts:eapsInfoMode.setStatus(_A)
class _EapsInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_k,0),('complete',1),(_l,2),('linksup',3),('linkdown',4),('preforwarding',5),('init',6)))
_EapsInfoState_Type.__name__=_C
_EapsInfoState_Object=MibTableColumn
eapsInfoState=_EapsInfoState_Object((1,3,6,1,4,1,3709,3,5,201,1,24,1,1,4),_EapsInfoState_Type())
eapsInfoState.setMaxAccess(_D)
if mibBuilder.loadTexts:eapsInfoState.setStatus(_A)
_CfmProbeMgmt_ObjectIdentity=ObjectIdentity
cfmProbeMgmt=_CfmProbeMgmt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,25))
_CfmProbeDmTable_Object=MibTable
cfmProbeDmTable=_CfmProbeDmTable_Object((1,3,6,1,4,1,3709,3,5,201,1,25,1))
if mibBuilder.loadTexts:cfmProbeDmTable.setStatus(_A)
_CfmProbeDmEntry_Object=MibTableRow
cfmProbeDmEntry=_CfmProbeDmEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,25,1,1))
cfmProbeDmEntry.setIndexNames((0,_B,_Ah))
if mibBuilder.loadTexts:cfmProbeDmEntry.setStatus(_A)
class _CfmProbeDmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CfmProbeDmIndex_Type.__name__=_C
_CfmProbeDmIndex_Object=MibTableColumn
cfmProbeDmIndex=_CfmProbeDmIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,25,1,1,1),_CfmProbeDmIndex_Type())
cfmProbeDmIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cfmProbeDmIndex.setStatus(_A)
_CfmProbeDmAvgDelay_Type=Integer32
_CfmProbeDmAvgDelay_Object=MibTableColumn
cfmProbeDmAvgDelay=_CfmProbeDmAvgDelay_Object((1,3,6,1,4,1,3709,3,5,201,1,25,1,1,2),_CfmProbeDmAvgDelay_Type())
cfmProbeDmAvgDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cfmProbeDmAvgDelay.setStatus(_A)
_CfmProbeDmAvgJitter_Type=Integer32
_CfmProbeDmAvgJitter_Object=MibTableColumn
cfmProbeDmAvgJitter=_CfmProbeDmAvgJitter_Object((1,3,6,1,4,1,3709,3,5,201,1,25,1,1,3),_CfmProbeDmAvgJitter_Type())
cfmProbeDmAvgJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:cfmProbeDmAvgJitter.setStatus(_A)
_CfmProbeDmLoss_Type=Integer32
_CfmProbeDmLoss_Object=MibTableColumn
cfmProbeDmLoss=_CfmProbeDmLoss_Object((1,3,6,1,4,1,3709,3,5,201,1,25,1,1,4),_CfmProbeDmLoss_Type())
cfmProbeDmLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:cfmProbeDmLoss.setStatus(_A)
_CpumonMgmt_ObjectIdentity=ObjectIdentity
cpumonMgmt=_CpumonMgmt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,26))
_CpuActiveUsageTable_Object=MibTable
cpuActiveUsageTable=_CpuActiveUsageTable_Object((1,3,6,1,4,1,3709,3,5,201,1,26,1))
if mibBuilder.loadTexts:cpuActiveUsageTable.setStatus(_A)
_CpuActiveUsageEntry_Object=MibTableRow
cpuActiveUsageEntry=_CpuActiveUsageEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,26,1,1))
cpuActiveUsageEntry.setIndexNames((0,_B,_Ai))
if mibBuilder.loadTexts:cpuActiveUsageEntry.setStatus(_A)
_CpuActiveUsageIndex_Type=Integer32
_CpuActiveUsageIndex_Object=MibTableColumn
cpuActiveUsageIndex=_CpuActiveUsageIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,26,1,1,1),_CpuActiveUsageIndex_Type())
cpuActiveUsageIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpuActiveUsageIndex.setStatus(_A)
_CpuActiveUsageValue_Type=Integer32
_CpuActiveUsageValue_Object=MibTableColumn
cpuActiveUsageValue=_CpuActiveUsageValue_Object((1,3,6,1,4,1,3709,3,5,201,1,26,1,1,2),_CpuActiveUsageValue_Type())
cpuActiveUsageValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuActiveUsageValue.setStatus(_A)
_MemActiveUsageTable_Object=MibTable
memActiveUsageTable=_MemActiveUsageTable_Object((1,3,6,1,4,1,3709,3,5,201,1,26,2))
if mibBuilder.loadTexts:memActiveUsageTable.setStatus(_A)
_MemActiveUsageEntry_Object=MibTableRow
memActiveUsageEntry=_MemActiveUsageEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,26,2,1))
memActiveUsageEntry.setIndexNames((0,_B,_Aj))
if mibBuilder.loadTexts:memActiveUsageEntry.setStatus(_A)
_MemActiveUsageIndex_Type=Integer32
_MemActiveUsageIndex_Object=MibTableColumn
memActiveUsageIndex=_MemActiveUsageIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,26,2,1,1),_MemActiveUsageIndex_Type())
memActiveUsageIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:memActiveUsageIndex.setStatus(_A)
_MemActiveUsageValue_Type=Integer32
_MemActiveUsageValue_Object=MibTableColumn
memActiveUsageValue=_MemActiveUsageValue_Object((1,3,6,1,4,1,3709,3,5,201,1,26,2,1,2),_MemActiveUsageValue_Type())
memActiveUsageValue.setMaxAccess(_D)
if mibBuilder.loadTexts:memActiveUsageValue.setStatus(_A)
_CpuStandbyUsageTable_Object=MibTable
cpuStandbyUsageTable=_CpuStandbyUsageTable_Object((1,3,6,1,4,1,3709,3,5,201,1,26,3))
if mibBuilder.loadTexts:cpuStandbyUsageTable.setStatus(_A)
_CpuStandbyUsageEntry_Object=MibTableRow
cpuStandbyUsageEntry=_CpuStandbyUsageEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,26,3,1))
cpuStandbyUsageEntry.setIndexNames((0,_B,_Ak))
if mibBuilder.loadTexts:cpuStandbyUsageEntry.setStatus(_A)
_CpuStandbyUsageIndex_Type=Integer32
_CpuStandbyUsageIndex_Object=MibTableColumn
cpuStandbyUsageIndex=_CpuStandbyUsageIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,26,3,1,1),_CpuStandbyUsageIndex_Type())
cpuStandbyUsageIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpuStandbyUsageIndex.setStatus(_A)
_CpuStandbyUsageValue_Type=Integer32
_CpuStandbyUsageValue_Object=MibTableColumn
cpuStandbyUsageValue=_CpuStandbyUsageValue_Object((1,3,6,1,4,1,3709,3,5,201,1,26,3,1,2),_CpuStandbyUsageValue_Type())
cpuStandbyUsageValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cpuStandbyUsageValue.setStatus(_A)
_MemStandbyUsageTable_Object=MibTable
memStandbyUsageTable=_MemStandbyUsageTable_Object((1,3,6,1,4,1,3709,3,5,201,1,26,4))
if mibBuilder.loadTexts:memStandbyUsageTable.setStatus(_A)
_MemStandbyUsageEntry_Object=MibTableRow
memStandbyUsageEntry=_MemStandbyUsageEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,26,4,1))
memStandbyUsageEntry.setIndexNames((0,_B,_Al))
if mibBuilder.loadTexts:memStandbyUsageEntry.setStatus(_A)
_MemStandbyUsageIndex_Type=Integer32
_MemStandbyUsageIndex_Object=MibTableColumn
memStandbyUsageIndex=_MemStandbyUsageIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,26,4,1,1),_MemStandbyUsageIndex_Type())
memStandbyUsageIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:memStandbyUsageIndex.setStatus(_A)
_MemStandbyUsageValue_Type=Integer32
_MemStandbyUsageValue_Object=MibTableColumn
memStandbyUsageValue=_MemStandbyUsageValue_Object((1,3,6,1,4,1,3709,3,5,201,1,26,4,1,2),_MemStandbyUsageValue_Type())
memStandbyUsageValue.setMaxAccess(_D)
if mibBuilder.loadTexts:memStandbyUsageValue.setStatus(_A)
_QueuePortMgmt_ObjectIdentity=ObjectIdentity
queuePortMgmt=_QueuePortMgmt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,27))
_QueuePortTable_Object=MibTable
queuePortTable=_QueuePortTable_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1))
if mibBuilder.loadTexts:queuePortTable.setStatus(_A)
_QueuePortEntry_Object=MibTableRow
queuePortEntry=_QueuePortEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1,1))
queuePortEntry.setIndexNames((0,_B,_Am),(0,_B,_An))
if mibBuilder.loadTexts:queuePortEntry.setStatus(_A)
_QueuePortIfIndex_Type=Integer32
_QueuePortIfIndex_Object=MibTableColumn
queuePortIfIndex=_QueuePortIfIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1,1,1),_QueuePortIfIndex_Type())
queuePortIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:queuePortIfIndex.setStatus(_A)
_QueuePortQueueIndex_Type=Integer32
_QueuePortQueueIndex_Object=MibTableColumn
queuePortQueueIndex=_QueuePortQueueIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1,1,2),_QueuePortQueueIndex_Type())
queuePortQueueIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:queuePortQueueIndex.setStatus(_A)
_QueuePortSentPackets_Type=Counter64
_QueuePortSentPackets_Object=MibTableColumn
queuePortSentPackets=_QueuePortSentPackets_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1,1,3),_QueuePortSentPackets_Type())
queuePortSentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:queuePortSentPackets.setStatus(_A)
_QueuePortSentBytes_Type=Counter64
_QueuePortSentBytes_Object=MibTableColumn
queuePortSentBytes=_QueuePortSentBytes_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1,1,4),_QueuePortSentBytes_Type())
queuePortSentBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:queuePortSentBytes.setStatus(_A)
_QueuePortDroppedPackets_Type=Counter64
_QueuePortDroppedPackets_Object=MibTableColumn
queuePortDroppedPackets=_QueuePortDroppedPackets_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1,1,5),_QueuePortDroppedPackets_Type())
queuePortDroppedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:queuePortDroppedPackets.setStatus(_A)
_QueuePortDroppedBytes_Type=Counter64
_QueuePortDroppedBytes_Object=MibTableColumn
queuePortDroppedBytes=_QueuePortDroppedBytes_Object((1,3,6,1,4,1,3709,3,5,201,1,27,1,1,6),_QueuePortDroppedBytes_Type())
queuePortDroppedBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:queuePortDroppedBytes.setStatus(_A)
_DdTransceiversMgmt_ObjectIdentity=ObjectIdentity
ddTransceiversMgmt=_DdTransceiversMgmt_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,1,28))
_DdTransceiversTable_Object=MibTable
ddTransceiversTable=_DdTransceiversTable_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1))
if mibBuilder.loadTexts:ddTransceiversTable.setStatus(_A)
_DdTransceiversEntry_Object=MibTableRow
ddTransceiversEntry=_DdTransceiversEntry_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1))
ddTransceiversEntry.setIndexNames((0,_B,_Ao))
if mibBuilder.loadTexts:ddTransceiversEntry.setStatus(_A)
_DdTransceiversIfIndex_Type=Integer32
_DdTransceiversIfIndex_Object=MibTableColumn
ddTransceiversIfIndex=_DdTransceiversIfIndex_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,1),_DdTransceiversIfIndex_Type())
ddTransceiversIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ddTransceiversIfIndex.setStatus(_A)
class _DdTransceiversTemperature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DdTransceiversTemperature_Type.__name__=_K
_DdTransceiversTemperature_Object=MibTableColumn
ddTransceiversTemperature=_DdTransceiversTemperature_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,2),_DdTransceiversTemperature_Type())
ddTransceiversTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversTemperature.setStatus(_A)
class _DdTransceiversVcc3v3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DdTransceiversVcc3v3_Type.__name__=_K
_DdTransceiversVcc3v3_Object=MibTableColumn
ddTransceiversVcc3v3=_DdTransceiversVcc3v3_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,3),_DdTransceiversVcc3v3_Type())
ddTransceiversVcc3v3.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversVcc3v3.setStatus(_A)
class _DdTransceiversRxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DdTransceiversRxPower_Type.__name__=_K
_DdTransceiversRxPower_Object=MibTableColumn
ddTransceiversRxPower=_DdTransceiversRxPower_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,4),_DdTransceiversRxPower_Type())
ddTransceiversRxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversRxPower.setStatus(_A)
class _DdTransceiversTxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DdTransceiversTxPower_Type.__name__=_K
_DdTransceiversTxPower_Object=MibTableColumn
ddTransceiversTxPower=_DdTransceiversTxPower_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,5),_DdTransceiversTxPower_Type())
ddTransceiversTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversTxPower.setStatus(_A)
class _DdTransceiversTxBias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DdTransceiversTxBias_Type.__name__=_K
_DdTransceiversTxBias_Object=MibTableColumn
ddTransceiversTxBias=_DdTransceiversTxBias_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,6),_DdTransceiversTxBias_Type())
ddTransceiversTxBias.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversTxBias.setStatus(_A)
_DdTransceiversTemperatureValue_Type=Integer32
_DdTransceiversTemperatureValue_Object=MibScalar
ddTransceiversTemperatureValue=_DdTransceiversTemperatureValue_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,7),_DdTransceiversTemperatureValue_Type())
ddTransceiversTemperatureValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversTemperatureValue.setStatus(_A)
if mibBuilder.loadTexts:ddTransceiversTemperatureValue.setUnits('Celsius (degrees C)')
_DdTransceiversVcc3v3Value_Type=Integer32
_DdTransceiversVcc3v3Value_Object=MibScalar
ddTransceiversVcc3v3Value=_DdTransceiversVcc3v3Value_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,8),_DdTransceiversVcc3v3Value_Type())
ddTransceiversVcc3v3Value.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversVcc3v3Value.setStatus(_A)
if mibBuilder.loadTexts:ddTransceiversVcc3v3Value.setUnits('0.1 V')
_DdTransceiversRxPowerValue_Type=Integer32
_DdTransceiversRxPowerValue_Object=MibScalar
ddTransceiversRxPowerValue=_DdTransceiversRxPowerValue_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,9),_DdTransceiversRxPowerValue_Type())
ddTransceiversRxPowerValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversRxPowerValue.setStatus(_A)
if mibBuilder.loadTexts:ddTransceiversRxPowerValue.setUnits('0.1 dBm')
_DdTransceiversTxPowerValue_Type=Integer32
_DdTransceiversTxPowerValue_Object=MibScalar
ddTransceiversTxPowerValue=_DdTransceiversTxPowerValue_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,10),_DdTransceiversTxPowerValue_Type())
ddTransceiversTxPowerValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversTxPowerValue.setStatus(_A)
if mibBuilder.loadTexts:ddTransceiversTxPowerValue.setUnits('0.1 dBm')
_DdTransceiversTxBiasValue_Type=Integer32
_DdTransceiversTxBiasValue_Object=MibScalar
ddTransceiversTxBiasValue=_DdTransceiversTxBiasValue_Object((1,3,6,1,4,1,3709,3,5,201,1,28,1,1,11),_DdTransceiversTxBiasValue_Type())
ddTransceiversTxBiasValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ddTransceiversTxBiasValue.setStatus(_A)
if mibBuilder.loadTexts:ddTransceiversTxBiasValue.setUnits('0.1 mA')
_DmSwitchNotifications_ObjectIdentity=ObjectIdentity
dmSwitchNotifications=_DmSwitchNotifications_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,2))
_DmSwitchTraps_ObjectIdentity=ObjectIdentity
dmSwitchTraps=_DmSwitchTraps_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,2,1))
_DmSwitchTrapsPrefix_ObjectIdentity=ObjectIdentity
dmSwitchTrapsPrefix=_DmSwitchTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,2,1,0))
_DmSwitchConformance_ObjectIdentity=ObjectIdentity
dmSwitchConformance=_DmSwitchConformance_ObjectIdentity((1,3,6,1,4,1,3709,3,5,201,3))
swLoginFailTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40001))
swLoginFailTrap.setObjects(*((_B,_F),(_B,_G),(_B,_o)))
if mibBuilder.loadTexts:swLoginFailTrap.setStatus(_A)
swLoginSucessTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40002))
swLoginSucessTrap.setObjects(*((_B,_F),(_B,_G),(_B,_o)))
if mibBuilder.loadTexts:swLoginSucessTrap.setStatus(_A)
swStackAttachTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40003))
swStackAttachTrap.setObjects(*((_B,_M),(_B,_p)))
if mibBuilder.loadTexts:swStackAttachTrap.setStatus(_A)
swStackDetachTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40004))
swStackDetachTrap.setObjects(*((_B,_M),(_B,_p)))
if mibBuilder.loadTexts:swStackDetachTrap.setStatus(_A)
swForbiddenAccessTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40005))
swForbiddenAccessTrap.setObjects(*((_B,_F),(_B,_G),(_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:swForbiddenAccessTrap.setStatus(_A)
swSfpPresenceTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40006))
swSfpPresenceTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_Ar)))
if mibBuilder.loadTexts:swSfpPresenceTrap.setStatus(_A)
swConfigChangeTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40007))
swConfigChangeTrap.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swConfigChangeTrap.setStatus(_A)
swConfigSaveTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40008))
swConfigSaveTrap.setObjects(*((_B,_F),(_B,_G),(_B,_As)))
if mibBuilder.loadTexts:swConfigSaveTrap.setStatus(_A)
swFanStatusChangeTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40009))
swFanStatusChangeTrap.setObjects(*((_B,_F),(_B,_G),(_B,_Y),(_B,_Z),(_B,_At)))
if mibBuilder.loadTexts:swFanStatusChangeTrap.setStatus(_A)
swTrapsLostTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40010))
if mibBuilder.loadTexts:swTrapsLostTrap.setStatus(_A)
swPowerStatusChangeTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40011))
swPowerStatusChangeTrap.setObjects(*((_B,_F),(_B,_G),(_B,_W),(_B,_X),(_B,_Au)))
if mibBuilder.loadTexts:swPowerStatusChangeTrap.setStatus(_A)
swAlarmTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40012))
swAlarmTrap.setObjects(*((_B,_F),(_B,_G),(_B,_a),(_B,_b),(_B,_Av)))
if mibBuilder.loadTexts:swAlarmTrap.setStatus(_A)
swDuplicatedIp=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40013))
swDuplicatedIp.setObjects(*((_B,_F),(_B,_G),(_B,_Aw),(_B,_Ax),(_B,_Ay)))
if mibBuilder.loadTexts:swDuplicatedIp.setStatus(_A)
swLoopbackOnPortDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40014))
swLoopbackOnPortDetected.setObjects(*((_B,_F),(_B,_G),(_B,_I)))
if mibBuilder.loadTexts:swLoopbackOnPortDetected.setStatus(_A)
swLoopbackOnPortNoMoreDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40015))
swLoopbackOnPortNoMoreDetected.setObjects(*((_B,_F),(_B,_G),(_B,_I)))
if mibBuilder.loadTexts:swLoopbackOnPortNoMoreDetected.setStatus(_A)
swUnidirLinkDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40016))
swUnidirLinkDetected.setObjects(*((_B,_F),(_B,_G),(_B,_I)))
if mibBuilder.loadTexts:swUnidirLinkDetected.setStatus(_A)
swUnidirLinkRecovered=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40017))
swUnidirLinkRecovered.setObjects(*((_B,_F),(_B,_G),(_B,_I)))
if mibBuilder.loadTexts:swUnidirLinkRecovered.setStatus(_A)
swCriticalEventDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40018))
swCriticalEventDetected.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swCriticalEventDetected.setStatus(_A)
swCriticalEventRecovered=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40019))
swCriticalEventRecovered.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swCriticalEventRecovered.setStatus(_A)
swLinkFlapDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40020))
swLinkFlapDetected.setObjects((_B,_I))
if mibBuilder.loadTexts:swLinkFlapDetected.setStatus(_A)
swLinkFlapNoMoreDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40021))
swLinkFlapNoMoreDetected.setObjects((_B,_I))
if mibBuilder.loadTexts:swLinkFlapNoMoreDetected.setStatus(_A)
swEapsStatusChange=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40022))
swEapsStatusChange.setObjects(*((_B,_F),(_B,_G),(_B,_Az),(_B,_A_),(_B,_B0)))
if mibBuilder.loadTexts:swEapsStatusChange.setStatus(_A)
swPortSecurityViolation=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40023))
swPortSecurityViolation.setObjects((_B,_I))
if mibBuilder.loadTexts:swPortSecurityViolation.setStatus(_A)
swHighTemperatureDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40024))
swHighTemperatureDetected.setObjects(*((_B,_M),(_B,_F),(_B,_G),(_B,_T)))
if mibBuilder.loadTexts:swHighTemperatureDetected.setStatus(_A)
swHighTemperatureNoMoreDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40025))
swHighTemperatureNoMoreDetected.setObjects(*((_B,_M),(_B,_F),(_B,_G),(_B,_T)))
if mibBuilder.loadTexts:swHighTemperatureNoMoreDetected.setStatus(_A)
swFuseStatusChange=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40026))
swFuseStatusChange.setObjects(*((_B,_M),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:swFuseStatusChange.setStatus(_A)
swFansBoardPresenceTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40027))
swFansBoardPresenceTrap.setObjects((_B,_B1))
if mibBuilder.loadTexts:swFansBoardPresenceTrap.setStatus(_A)
swStandbyMpuTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40028))
swStandbyMpuTrap.setObjects(*((_B,_e),(_B,_B2),(_B,_B3),(_B,_B4)))
if mibBuilder.loadTexts:swStandbyMpuTrap.setStatus(_A)
swNonHomologSfpTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40029))
swNonHomologSfpTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swNonHomologSfpTrap.setStatus(_A)
swHighCpuUsageDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40030))
swHighCpuUsageDetected.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swHighCpuUsageDetected.setStatus(_A)
swHighCpuUsageNoMoreDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40031))
swHighCpuUsageNoMoreDetected.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swHighCpuUsageNoMoreDetected.setStatus(_A)
swDuplicatedMac=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40032))
swDuplicatedMac.setObjects((_B,_B5))
if mibBuilder.loadTexts:swDuplicatedMac.setStatus(_A)
swHighMemoryUsageDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40033))
swHighMemoryUsageDetected.setObjects(*((_B,_F),(_B,_G),(_B,_s)))
if mibBuilder.loadTexts:swHighMemoryUsageDetected.setStatus(_A)
swHighMemoryUsageNoMoreDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40034))
swHighMemoryUsageNoMoreDetected.setObjects(*((_B,_F),(_B,_G),(_B,_s)))
if mibBuilder.loadTexts:swHighMemoryUsageNoMoreDetected.setStatus(_A)
swNewBootloaderVersion=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40035))
swNewBootloaderVersion.setObjects(*((_B,_M),(_B,_B6)))
if mibBuilder.loadTexts:swNewBootloaderVersion.setStatus(_A)
swCesopTdmStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40036))
swCesopTdmStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_B7)))
if mibBuilder.loadTexts:swCesopTdmStatusTrap.setStatus(_A)
swCesopTdmRemoteStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40037))
swCesopTdmRemoteStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_B8)))
if mibBuilder.loadTexts:swCesopTdmRemoteStatusTrap.setStatus(_A)
swCesopTdmCasStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40038))
swCesopTdmCasStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_B9)))
if mibBuilder.loadTexts:swCesopTdmCasStatusTrap.setStatus(_A)
swCesopTdmCrcStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40039))
swCesopTdmCrcStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_BA)))
if mibBuilder.loadTexts:swCesopTdmCrcStatusTrap.setStatus(_A)
swCesopBundleLocalTdmStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40040))
swCesopBundleLocalTdmStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_BB)))
if mibBuilder.loadTexts:swCesopBundleLocalTdmStatusTrap.setStatus(_A)
swCesopBundleRemoteTdmStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40041))
swCesopBundleRemoteTdmStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_BC)))
if mibBuilder.loadTexts:swCesopBundleRemoteTdmStatusTrap.setStatus(_A)
swCesopBundleLocalStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40042))
swCesopBundleLocalStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_BD)))
if mibBuilder.loadTexts:swCesopBundleLocalStatusTrap.setStatus(_A)
swCesopBundleRemoteStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40043))
swCesopBundleRemoteStatusTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_BE)))
if mibBuilder.loadTexts:swCesopBundleRemoteStatusTrap.setStatus(_A)
swCesopBundlePktMismatchTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40044))
swCesopBundlePktMismatchTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_BF)))
if mibBuilder.loadTexts:swCesopBundlePktMismatchTrap.setStatus(_A)
swCesopBundleNextHopTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40045))
swCesopBundleNextHopTrap.setObjects(*((_B,_I),(_B,_F),(_B,_G),(_B,_BG)))
if mibBuilder.loadTexts:swCesopBundleNextHopTrap.setStatus(_A)
swCesopClockAdapLinkQualityTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40046))
swCesopClockAdapLinkQualityTrap.setObjects(*((_B,_M),(_B,_F),(_B,_G),(_B,_BH)))
if mibBuilder.loadTexts:swCesopClockAdapLinkQualityTrap.setStatus(_A)
swCesopClockSourceTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40047))
swCesopClockSourceTrap.setObjects(*((_B,_M),(_B,_F),(_B,_G),(_B,_BI)))
if mibBuilder.loadTexts:swCesopClockSourceTrap.setStatus(_A)
swRemoteDeviceReady=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40048))
swRemoteDeviceReady.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swRemoteDeviceReady.setStatus(_A)
swRemoteDeviceLost=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40049))
swRemoteDeviceLost.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swRemoteDeviceLost.setStatus(_A)
swRemoteDeviceConfigFail=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40050))
swRemoteDeviceConfigFail.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swRemoteDeviceConfigFail.setStatus(_A)
swRemoteDeviceConfigForced=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40051))
swRemoteDeviceConfigForced.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swRemoteDeviceConfigForced.setStatus(_A)
swFanFuseStatusChange=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40052))
swFanFuseStatusChange.setObjects(*((_B,_M),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:swFanFuseStatusChange.setStatus(_A)
swDyingGaspPackReceived=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40053))
swDyingGaspPackReceived.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swDyingGaspPackReceived.setStatus(_A)
swBroadcastStormCheckChange=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40054))
swBroadcastStormCheckChange.setObjects(*((_B,_F),(_B,_G),(_B,_I),(_B,_BJ),(_B,_BK)))
if mibBuilder.loadTexts:swBroadcastStormCheckChange.setStatus(_A)
swMulticastStormCheckChange=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40055))
swMulticastStormCheckChange.setObjects(*((_B,_F),(_B,_G),(_B,_I),(_B,_BL),(_B,_BM)))
if mibBuilder.loadTexts:swMulticastStormCheckChange.setStatus(_A)
swBpduProtectLimit=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40056))
swBpduProtectLimit.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swBpduProtectLimit.setStatus(_A)
swChangeStatusLDP=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40057))
swChangeStatusLDP.setObjects(*((_B,_F),(_B,_G),(_B,_BN),(_B,_BO),(_B,_BP)))
if mibBuilder.loadTexts:swChangeStatusLDP.setStatus(_A)
swChangeStatusTunnelRSVP=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40058))
swChangeStatusTunnelRSVP.setObjects(*((_B,_F),(_B,_G),(_B,_BQ),(_B,_BR)))
if mibBuilder.loadTexts:swChangeStatusTunnelRSVP.setStatus(_A)
swBpduProtect=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40059))
swBpduProtect.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swBpduProtect.setStatus(_A)
swRouteTableFull=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40060))
swRouteTableFull.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swRouteTableFull.setStatus(_A)
swPanelStatusTrap=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40061))
swPanelStatusTrap.setObjects(*((_B,_F),(_B,_G),(_B,_BS)))
if mibBuilder.loadTexts:swPanelStatusTrap.setStatus(_A)
swLSTGroupLinkStatusDown=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40062))
swLSTGroupLinkStatusDown.setObjects(*((_B,_F),(_B,_G),(_B,_t)))
if mibBuilder.loadTexts:swLSTGroupLinkStatusDown.setStatus(_A)
swLSTGroupLinkStatusUp=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40063))
swLSTGroupLinkStatusUp.setObjects(*((_B,_F),(_B,_G),(_B,_t)))
if mibBuilder.loadTexts:swLSTGroupLinkStatusUp.setStatus(_A)
swHighCpuL3UsageDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40064))
swHighCpuL3UsageDetected.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swHighCpuL3UsageDetected.setStatus(_A)
swHighCpuL3UsageNoMoreDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40065))
swHighCpuL3UsageNoMoreDetected.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swHighCpuL3UsageNoMoreDetected.setStatus(_A)
swHighMemoryL3UsageDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40066))
swHighMemoryL3UsageDetected.setObjects(*((_B,_F),(_B,_G),(_B,_u)))
if mibBuilder.loadTexts:swHighMemoryL3UsageDetected.setStatus(_A)
swHighMemoryL3UsageNoMoreDetected=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40067))
swHighMemoryL3UsageNoMoreDetected.setObjects(*((_B,_F),(_B,_G),(_B,_u)))
if mibBuilder.loadTexts:swHighMemoryL3UsageNoMoreDetected.setStatus(_A)
swMpuNsfIdDiffers=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40068))
swMpuNsfIdDiffers.setObjects(*((_B,_F),(_B,_G),(_B,_BT),(_B,_BU)))
if mibBuilder.loadTexts:swMpuNsfIdDiffers.setStatus(_A)
swErpsStatusChange=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40069))
swErpsStatusChange.setObjects(*((_B,_F),(_B,_G),(_B,_BV),(_B,_BW),(_B,_BX)))
if mibBuilder.loadTexts:swErpsStatusChange.setStatus(_A)
swCfmDefect=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40070))
swCfmDefect.setObjects(*((_B,_F),(_B,_G),(_B,_BY),(_B,_BZ),(_B,_Ba),(_B,_Bb),(_B,_Bc)))
if mibBuilder.loadTexts:swCfmDefect.setStatus(_A)
swLldpRemoteChange=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40071))
swLldpRemoteChange.setObjects(*((_B,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swLldpRemoteChange.setStatus(_A)
swPoeOverCurrent=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40072))
swPoeOverCurrent.setObjects(*((_B,_F),(_B,_G),(_B,_I)))
if mibBuilder.loadTexts:swPoeOverCurrent.setStatus(_A)
swPoePowerRestriction=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40073))
swPoePowerRestriction.setObjects(*((_B,_F),(_B,_G),(_B,_I)))
if mibBuilder.loadTexts:swPoePowerRestriction.setStatus(_A)
swCoreDump=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40074))
swCoreDump.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swCoreDump.setStatus(_A)
swElmiEvcStatus=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40075))
swElmiEvcStatus.setObjects(*((_B,_F),(_B,_G),(_B,_I),(_B,_Bd),(_B,_Be)))
if mibBuilder.loadTexts:swElmiEvcStatus.setStatus(_A)
swSyncSystemClockSwitchHier=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40076))
swSyncSystemClockSwitchHier.setObjects(*((_B,_M),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swSyncSystemClockSwitchHier.setStatus(_A)
swSyncSystemClockStatus=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40077))
swSyncSystemClockStatus.setObjects(*((_B,_M),(_B,_F),(_B,_G),(_B,_Bf)))
if mibBuilder.loadTexts:swSyncSystemClockStatus.setStatus(_A)
swHostTableFull=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40078))
swHostTableFull.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:swHostTableFull.setStatus(_A)
swSyncG704ClockStatus=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40079))
swSyncG704ClockStatus.setObjects(*((_B,_F),(_B,_G),(_B,_I),(_B,_Bg)))
if mibBuilder.loadTexts:swSyncG704ClockStatus.setStatus(_A)
swSystemWarningsUnits=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40080))
swSystemWarningsUnits.setObjects(*((_B,_F),(_B,_G),(_B,_Bh)))
if mibBuilder.loadTexts:swSystemWarningsUnits.setStatus(_A)
swRebootDueToOvertemp=NotificationType((1,3,6,1,4,1,3709,3,5,201,2,1,0,40081))
swRebootDueToOvertemp.setObjects(*((_B,_F),(_B,_G),(_B,_M),(_B,_I),(_B,_Bi),(_B,_T)))
if mibBuilder.loadTexts:swRebootDueToOvertemp.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ValidStatus':ValidStatus,'KeySegment':KeySegment,'StaPathCostMode':StaPathCostMode,'dmSwitchMIB':dmSwitchMIB,'dmSwitchMIBObjects':dmSwitchMIBObjects,'switchMgt':switchMgt,'switchNumber':switchNumber,'switchInfoTable':switchInfoTable,'switchInfoEntry':switchInfoEntry,_M:swUnitIndex,'swHardwareVer':swHardwareVer,'swBootLoaderVer':swBootLoaderVer,'swFirmwareVer':swFirmwareVer,'swPortNumber':swPortNumber,'swPowerStatus':swPowerStatus,'swRoleInSystem':swRoleInSystem,_p:swSerialNumber,'swProdName':swProdName,'swProdModelId':swProdModelId,'swFirmwareReleaseDate':swFirmwareReleaseDate,'swTemperature':swTemperature,'swG704IntfNumber':swG704IntfNumber,'swE1cIntfNumber':swE1cIntfNumber,'swBundleIntfNumber':swBundleIntfNumber,'swPtpIntfNumber':swPtpIntfNumber,'swSdhIntfNumber':swSdhIntfNumber,'swVC4Number':swVC4Number,'swVC12Number':swVC12Number,'switchProductId':switchProductId,'swProdManufacturer':swProdManufacturer,'swProdDescription':swProdDescription,'swProdUrl':swProdUrl,'swIdentifier':swIdentifier,'swVendorId':swVendorId,'switchIndivPowerTable':switchIndivPowerTable,'switchIndivPowerEntry':switchIndivPowerEntry,_W:swIndivPowerUnitIndex,_X:swIndivPowerIndex,_Au:swIndivPowerStatus,'switchIndivFanTable':switchIndivFanTable,'switchIndivFanEntry':switchIndivFanEntry,_Y:swIndivFanUnitIndex,_Z:swIndivFanIndex,_At:swIndivFanStatus,'switchIndivAlarmTable':switchIndivAlarmTable,'switchIndivAlarmEntry':switchIndivAlarmEntry,_a:swIndivAlarmUnitIndex,_b:swIndivAlarmIndex,_Av:swIndivAlarmStatus,'switchResObj':switchResObj,'swHashConfig':swHashConfig,'swHashStatus':swHashStatus,'swCpuUsage':swCpuUsage,'swMemUsage':swMemUsage,'switchMacAddrUsageTable':switchMacAddrUsageTable,'switchMacAddrUsageEntry':switchMacAddrUsageEntry,_A1:swMacAddrUnitIndex,'swMacAddrUsageValue':swMacAddrUsageValue,'swSlotNumber':swSlotNumber,'switchMpuTable':switchMpuTable,'switchMpuEntry':switchMpuEntry,_e:swMpuIndex,'swMpuBootLoaderVer':swMpuBootLoaderVer,'swMpuRoleInSystem':swMpuRoleInSystem,_B2:swMpuSerialNumber,_B3:swMpuModelId,'swHashHardware':swHashHardware,'switchIndivAlarmOutTable':switchIndivAlarmOutTable,'switchIndivAlarmOutEntry':switchIndivAlarmOutEntry,_A2:swIndivAlarmOutUnitIndex,'swIndivAlarmOutStatus':swIndivAlarmOutStatus,'swChassisModel':swChassisModel,'switchSessionTable':switchSessionTable,'switchSessionEntry':switchSessionEntry,_A3:swSessionUnitIndex,'swSessionName':swSessionName,'swSessionUptime':swSessionUptime,'swSessionPid':swSessionPid,'swSessionSrcIP':swSessionSrcIP,'portMgt':portMgt,'portTable':portTable,'portEntry':portEntry,_I:portIndex,'portName':portName,'portType':portType,'portSpeedDpxCfg':portSpeedDpxCfg,'portFlowCtrlCfg':portFlowCtrlCfg,'portCapabilities':portCapabilities,'portAutonegotiation':portAutonegotiation,'portSpeedDpxStatus':portSpeedDpxStatus,'portFlowCtrlStatus':portFlowCtrlStatus,'portMdiStatus':portMdiStatus,'portTrunkIndex':portTrunkIndex,'trunkMgt':trunkMgt,'trunkMaxId':trunkMaxId,'trunkValidNumber':trunkValidNumber,'trunkTable':trunkTable,'trunkEntry':trunkEntry,_AC:trunkIndex,'trunkPorts':trunkPorts,'trunkCreation':trunkCreation,'trunkStatus':trunkStatus,'lacpMgt':lacpMgt,'lacpPortTable':lacpPortTable,'lacpPortEntry':lacpPortEntry,_AD:lacpPortIndex,'lacpPortStatus':lacpPortStatus,'staMgt':staMgt,'staSystemStatus':staSystemStatus,'staPortTable':staPortTable,'staPortEntry':staPortEntry,_AE:staPortIndex,'staPortAdminEdgePort':staPortAdminEdgePort,'staPortOperEdgePort':staPortOperEdgePort,'staPortAdminPointToPoint':staPortAdminPointToPoint,'staPortOperPointToPoint':staPortOperPointToPoint,'staPortLongPathCost':staPortLongPathCost,'staPortSystemStatus':staPortSystemStatus,'staProtocolType':staProtocolType,'tftpMgt':tftpMgt,'tftpFile':tftpFile,'tftpFlashConfig':tftpFlashConfig,'tftpServer':tftpServer,'tftpAction':tftpAction,'restartMgt':restartMgt,'restartFirmware':restartFirmware,'restartConfig':restartConfig,'restartControl':restartControl,'mirrorMgt':mirrorMgt,'mirrorDestinationPort':mirrorDestinationPort,'mirrorTable':mirrorTable,'mirrorEntry':mirrorEntry,_AF:mirrorSourcePort,'mirrorType':mirrorType,'igmpSnoopMgt':igmpSnoopMgt,'igmpSnoopStatus':igmpSnoopStatus,'igmpSnoopQuerier':igmpSnoopQuerier,'igmpSnoopQueryCount':igmpSnoopQueryCount,'igmpSnoopQueryInterval':igmpSnoopQueryInterval,'igmpSnoopQueryMaxResponseTime':igmpSnoopQueryMaxResponseTime,'igmpSnoopQueryTimeout':igmpSnoopQueryTimeout,'igmpSnoopVersion':igmpSnoopVersion,'igmpSnoopRouterCurrentTable':igmpSnoopRouterCurrentTable,'igmpSnoopRouterCurrentEntry':igmpSnoopRouterCurrentEntry,_AG:igmpSnoopRouterCurrentVlanIndex,'igmpSnoopRouterCurrentPorts':igmpSnoopRouterCurrentPorts,'igmpSnoopRouterStaticTable':igmpSnoopRouterStaticTable,'igmpSnoopRouterStaticEntry':igmpSnoopRouterStaticEntry,_AH:igmpSnoopRouterStaticVlanIndex,'igmpSnoopRouterStaticPorts':igmpSnoopRouterStaticPorts,'igmpSnoopMulticastCurrentTable':igmpSnoopMulticastCurrentTable,'igmpSnoopMulticastCurrentEntry':igmpSnoopMulticastCurrentEntry,_AI:igmpSnoopMulticastCurrentVlanIndex,_AJ:igmpSnoopMulticastCurrentIpAddress,'igmpSnoopMulticastCurrentPorts':igmpSnoopMulticastCurrentPorts,'igmpSnoopMulticastStaticTable':igmpSnoopMulticastStaticTable,'igmpSnoopMulticastStaticEntry':igmpSnoopMulticastStaticEntry,_AK:igmpSnoopMulticastStaticVlanIndex,_AL:igmpSnoopMulticastStaticIpAddress,'igmpSnoopMulticastStaticPorts':igmpSnoopMulticastStaticPorts,'ipMgt':ipMgt,'ipAddressMode':ipAddressMode,'ipDefaultGateway':ipDefaultGateway,'ipPrimaryDnsServer':ipPrimaryDnsServer,'ipSecondaryDnsServer':ipSecondaryDnsServer,'ipHttpState':ipHttpState,'ipHttpPort':ipHttpPort,'ipHttpsState':ipHttpsState,'ipHttpsPort':ipHttpsPort,'ipTelnetState':ipTelnetState,'bcastStormMgt':bcastStormMgt,'bcastStormTable':bcastStormTable,'bcastStormEntry':bcastStormEntry,_AM:bcastStormIfIndex,'bcastStormStatus':bcastStormStatus,'bcastStormPacketRate':bcastStormPacketRate,'vlanMgt':vlanMgt,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_AN:vlanIndex,'vlanAddressMethod':vlanAddressMethod,'priorityMgt':priorityMgt,'prioWrrTable':prioWrrTable,'prioWrrEntry':prioWrrEntry,_AO:prioWrrTrafficClass,'prioWrrWeight':prioWrrWeight,'prioQueueMode':prioQueueMode,'trapDestMgt':trapDestMgt,'trapDestTable':trapDestTable,'trapDestEntry':trapDestEntry,_AP:trapDestAddress,'trapDestCommunity':trapDestCommunity,'trapDestStatus':trapDestStatus,'trapDestVersion':trapDestVersion,'trapVar':trapVar,_Ap:trapForbiddenAccessMode,_Aq:trapForbiddenAccessIp,_o:trapLoginUserName,_As:trapConfigSavePartition,_Ar:trapSfpPresenceStatus,'trapInfAlarmVal':trapInfAlarmVal,_Aw:trapDuplicatedIpVlan,_Ax:trapDuplicatedIpAddress,_Ay:trapDuplicatedIpMacAddress,_A_:trapEapsDomainName,_Az:trapEapsDomainId,_B0:trapEapsStatus,_T:trapTemperature,_q:trapFuseId,_r:trapFuseStatus,_B1:trapFansBoardPresenceStatus,_B4:trapStandbyMpuPresenceStatus,_B5:trapMacAddressMove,_s:trapMemFree,_B6:trapBootloaderNew,_F:trapDevNo,_G:trapDevLocalId,_B7:trapCesopTdmStatus,_B8:trapCesopTdmRemoteStatus,_B9:trapCesopTdmCasStatus,_BA:trapCesopTdmCrcStatus,_BB:trapCesopBundleLocalTdmStatus,_BC:trapCesopBundleRemoteTdmStatus,_BD:trapCesopBundleLocalStatus,_BE:trapCesopBundleRemoteStatus,_BF:trapCesopBundlePktMismatchStatus,_BG:trapCesopBundleNextHopStatus,_BH:trapCesopClockAdapLinkQuality,_BI:trapCesopClockSourceStatus,_BJ:trapBroadcastStormControlStatus,_BK:trapBroadcastStormControlPPS,_BL:trapMulticastStormControlStatus,_BM:trapMulticastStormControlPPS,_BN:trapStatusLDP,_BO:trapIdLDP,_BQ:trapStatusTunnelRSVP,_BR:trapIdTunnelRSVP,_BS:trapPanelStatus,_t:trapLSTGroup,_u:trapMemL3Free,_BT:trapActiveMpuNsfId,_BU:trapStandByMpuNsfId,_BW:trapErpsDomainName,_BV:trapErpsDomainId,_BX:trapErpsStatus,_BY:trapCfmMdName,_BZ:trapCfmMaName,_Ba:trapCfmMepId,_Bb:trapCfmVlan,_Bc:trapCfmDefect,_Bd:trapEvcName,_Be:trapEvcStatus,_Bf:trapSyncSystemClockStatus,_Bg:trapCesopG704ClockSourceStatus,_Bh:trapSystemWarningsUnits,_Bi:trapSensorGroup,_BP:trapIpNeighborLDP,'rateLimitMgt':rateLimitMgt,'rateLimitPortTable':rateLimitPortTable,'rateLimitPortEntry':rateLimitPortEntry,_AQ:rlPortIndex,'rlPortInputStatus':rlPortInputStatus,'rlPortOutputStatus':rlPortOutputStatus,'rlPortInputRate':rlPortInputRate,'rlPortInputBurst':rlPortInputBurst,'rlPortOutputRate':rlPortOutputRate,'rlPortOutputBurst':rlPortOutputBurst,'securityMgt':securityMgt,'radiusMgt':radiusMgt,'radiusServerPortNumber':radiusServerPortNumber,'radiusServerKey':radiusServerKey,'radiusServerRetransmit':radiusServerRetransmit,'radiusServerTimeout':radiusServerTimeout,'radiusMultipleServerTable':radiusMultipleServerTable,'radiusMultipleServerEntry':radiusMultipleServerEntry,_AR:radiusMultipleServerIndex,'radiusMultipleServerAddress':radiusMultipleServerAddress,'radiusMultipleServerPortNumber':radiusMultipleServerPortNumber,'radiusMultipleServerKey':radiusMultipleServerKey,'radiusMultipleServerRetransmit':radiusMultipleServerRetransmit,'radiusMultipleServerTimeout':radiusMultipleServerTimeout,'radiusMultipleServerStatus':radiusMultipleServerStatus,'sshMgt':sshMgt,'sshServerStatus':sshServerStatus,'sshServerMajorVersion':sshServerMajorVersion,'sshServerMinorVersion':sshServerMinorVersion,'sshTimeout':sshTimeout,'sshKeySize':sshKeySize,'sshRsaHostKey':sshRsaHostKey,'sshDsaHostKey':sshDsaHostKey,'sshHostKeyGenAction':sshHostKeyGenAction,'sshHostKeyDelAction':sshHostKeyDelAction,'ipFilterMgt':ipFilterMgt,'ipFilterSnmpTable':ipFilterSnmpTable,'ipFilterSnmpEntry':ipFilterSnmpEntry,_AS:ipFilterSnmpAddress,_AT:ipFilterSnmpMask,'ipFilterSnmpStatus':ipFilterSnmpStatus,'ipFilterHTTPTable':ipFilterHTTPTable,'ipFilterHTTPEntry':ipFilterHTTPEntry,_AU:ipFilterHTTPAddress,_AV:ipFilterHTTPMask,'ipFilterHTTPStatus':ipFilterHTTPStatus,'ipFilterTelnetTable':ipFilterTelnetTable,'ipFilterTelnetEntry':ipFilterTelnetEntry,_AW:ipFilterTelnetAddress,_AX:ipFilterTelnetMask,'ipFilterTelnetStatus':ipFilterTelnetStatus,'ipFilterSSHTable':ipFilterSSHTable,'ipFilterSSHEntry':ipFilterSSHEntry,_AY:ipFilterSSHAddress,_AZ:ipFilterSSHMask,'ipFilterSSHStatus':ipFilterSSHStatus,'sysLogMgt':sysLogMgt,'sysLogStatus':sysLogStatus,'sysLogHistoryFlashLevel':sysLogHistoryFlashLevel,'sysLogHistoryRamLevel':sysLogHistoryRamLevel,'remoteLogMgt':remoteLogMgt,'remoteLogStatus':remoteLogStatus,'remoteLogLevel':remoteLogLevel,'remoteLogFacilityType':remoteLogFacilityType,'remoteLogServerTable':remoteLogServerTable,'remoteLogServerEntry':remoteLogServerEntry,_Aa:remoteLogServerIp,'remoteLogServerStatus':remoteLogServerStatus,'sysTimeMgt':sysTimeMgt,'sntpMgt':sntpMgt,'sntpStatus':sntpStatus,'sntpPollInterval':sntpPollInterval,'sntpServerTable':sntpServerTable,'sntpServerEntry':sntpServerEntry,_Ab:sntpServerIp,'sntpServerStatus':sntpServerStatus,'sysCurrentTime':sysCurrentTime,'sysTimeZone':sysTimeZone,'sysTimeZoneName':sysTimeZoneName,'fileMgt':fileMgt,'fileInfoTable':fileInfoTable,'fileInfoEntry':fileInfoEntry,_Ac:fileInfoUnitID,_Ad:fileInfoFileIndex,'fileInfoFlashId':fileInfoFlashId,'fileInfoFileName':fileInfoFileName,'fileInfoFileType':fileInfoFileType,'fileInfoIsStartUp':fileInfoIsStartUp,'fileInfoFileSize':fileInfoFileSize,'fileInfoCreationTime':fileInfoCreationTime,'fileInfoDelete':fileInfoDelete,'countMgt':countMgt,'countHoldPktsTable':countHoldPktsTable,'countHoldPktsEntry':countHoldPktsEntry,_Ae:interfaceNumber,'countHoldPkts':countHoldPkts,'filterCounterMgt':filterCounterMgt,'filterCounterInfoTable':filterCounterInfoTable,'filterCounterInfoEntry':filterCounterInfoEntry,_n:filterCounterInfoIndex,'filterCounterInfoRemark':filterCounterInfoRemark,'filterCounterValueTable':filterCounterValueTable,'filterCounterValueEntry':filterCounterValueEntry,_Af:filterCounterValueIndex,'filterCounterValue':filterCounterValue,'eapsMgt':eapsMgt,'eapsInfoTable':eapsInfoTable,'eapsInfoEntry':eapsInfoEntry,_Ag:eapsInfoId,'eapsInfoName':eapsInfoName,'eapsInfoMode':eapsInfoMode,'eapsInfoState':eapsInfoState,'cfmProbeMgmt':cfmProbeMgmt,'cfmProbeDmTable':cfmProbeDmTable,'cfmProbeDmEntry':cfmProbeDmEntry,_Ah:cfmProbeDmIndex,'cfmProbeDmAvgDelay':cfmProbeDmAvgDelay,'cfmProbeDmAvgJitter':cfmProbeDmAvgJitter,'cfmProbeDmLoss':cfmProbeDmLoss,'cpumonMgmt':cpumonMgmt,'cpuActiveUsageTable':cpuActiveUsageTable,'cpuActiveUsageEntry':cpuActiveUsageEntry,_Ai:cpuActiveUsageIndex,'cpuActiveUsageValue':cpuActiveUsageValue,'memActiveUsageTable':memActiveUsageTable,'memActiveUsageEntry':memActiveUsageEntry,_Aj:memActiveUsageIndex,'memActiveUsageValue':memActiveUsageValue,'cpuStandbyUsageTable':cpuStandbyUsageTable,'cpuStandbyUsageEntry':cpuStandbyUsageEntry,_Ak:cpuStandbyUsageIndex,'cpuStandbyUsageValue':cpuStandbyUsageValue,'memStandbyUsageTable':memStandbyUsageTable,'memStandbyUsageEntry':memStandbyUsageEntry,_Al:memStandbyUsageIndex,'memStandbyUsageValue':memStandbyUsageValue,'queuePortMgmt':queuePortMgmt,'queuePortTable':queuePortTable,'queuePortEntry':queuePortEntry,_Am:queuePortIfIndex,_An:queuePortQueueIndex,'queuePortSentPackets':queuePortSentPackets,'queuePortSentBytes':queuePortSentBytes,'queuePortDroppedPackets':queuePortDroppedPackets,'queuePortDroppedBytes':queuePortDroppedBytes,'ddTransceiversMgmt':ddTransceiversMgmt,'ddTransceiversTable':ddTransceiversTable,'ddTransceiversEntry':ddTransceiversEntry,_Ao:ddTransceiversIfIndex,'ddTransceiversTemperature':ddTransceiversTemperature,'ddTransceiversVcc3v3':ddTransceiversVcc3v3,'ddTransceiversRxPower':ddTransceiversRxPower,'ddTransceiversTxPower':ddTransceiversTxPower,'ddTransceiversTxBias':ddTransceiversTxBias,'ddTransceiversTemperatureValue':ddTransceiversTemperatureValue,'ddTransceiversVcc3v3Value':ddTransceiversVcc3v3Value,'ddTransceiversRxPowerValue':ddTransceiversRxPowerValue,'ddTransceiversTxPowerValue':ddTransceiversTxPowerValue,'ddTransceiversTxBiasValue':ddTransceiversTxBiasValue,'dmSwitchNotifications':dmSwitchNotifications,'dmSwitchTraps':dmSwitchTraps,'dmSwitchTrapsPrefix':dmSwitchTrapsPrefix,'swLoginFailTrap':swLoginFailTrap,'swLoginSucessTrap':swLoginSucessTrap,'swStackAttachTrap':swStackAttachTrap,'swStackDetachTrap':swStackDetachTrap,'swForbiddenAccessTrap':swForbiddenAccessTrap,'swSfpPresenceTrap':swSfpPresenceTrap,'swConfigChangeTrap':swConfigChangeTrap,'swConfigSaveTrap':swConfigSaveTrap,'swFanStatusChangeTrap':swFanStatusChangeTrap,'swTrapsLostTrap':swTrapsLostTrap,'swPowerStatusChangeTrap':swPowerStatusChangeTrap,'swAlarmTrap':swAlarmTrap,'swDuplicatedIp':swDuplicatedIp,'swLoopbackOnPortDetected':swLoopbackOnPortDetected,'swLoopbackOnPortNoMoreDetected':swLoopbackOnPortNoMoreDetected,'swUnidirLinkDetected':swUnidirLinkDetected,'swUnidirLinkRecovered':swUnidirLinkRecovered,'swCriticalEventDetected':swCriticalEventDetected,'swCriticalEventRecovered':swCriticalEventRecovered,'swLinkFlapDetected':swLinkFlapDetected,'swLinkFlapNoMoreDetected':swLinkFlapNoMoreDetected,'swEapsStatusChange':swEapsStatusChange,'swPortSecurityViolation':swPortSecurityViolation,'swHighTemperatureDetected':swHighTemperatureDetected,'swHighTemperatureNoMoreDetected':swHighTemperatureNoMoreDetected,'swFuseStatusChange':swFuseStatusChange,'swFansBoardPresenceTrap':swFansBoardPresenceTrap,'swStandbyMpuTrap':swStandbyMpuTrap,'swNonHomologSfpTrap':swNonHomologSfpTrap,'swHighCpuUsageDetected':swHighCpuUsageDetected,'swHighCpuUsageNoMoreDetected':swHighCpuUsageNoMoreDetected,'swDuplicatedMac':swDuplicatedMac,'swHighMemoryUsageDetected':swHighMemoryUsageDetected,'swHighMemoryUsageNoMoreDetected':swHighMemoryUsageNoMoreDetected,'swNewBootloaderVersion':swNewBootloaderVersion,'swCesopTdmStatusTrap':swCesopTdmStatusTrap,'swCesopTdmRemoteStatusTrap':swCesopTdmRemoteStatusTrap,'swCesopTdmCasStatusTrap':swCesopTdmCasStatusTrap,'swCesopTdmCrcStatusTrap':swCesopTdmCrcStatusTrap,'swCesopBundleLocalTdmStatusTrap':swCesopBundleLocalTdmStatusTrap,'swCesopBundleRemoteTdmStatusTrap':swCesopBundleRemoteTdmStatusTrap,'swCesopBundleLocalStatusTrap':swCesopBundleLocalStatusTrap,'swCesopBundleRemoteStatusTrap':swCesopBundleRemoteStatusTrap,'swCesopBundlePktMismatchTrap':swCesopBundlePktMismatchTrap,'swCesopBundleNextHopTrap':swCesopBundleNextHopTrap,'swCesopClockAdapLinkQualityTrap':swCesopClockAdapLinkQualityTrap,'swCesopClockSourceTrap':swCesopClockSourceTrap,'swRemoteDeviceReady':swRemoteDeviceReady,'swRemoteDeviceLost':swRemoteDeviceLost,'swRemoteDeviceConfigFail':swRemoteDeviceConfigFail,'swRemoteDeviceConfigForced':swRemoteDeviceConfigForced,'swFanFuseStatusChange':swFanFuseStatusChange,'swDyingGaspPackReceived':swDyingGaspPackReceived,'swBroadcastStormCheckChange':swBroadcastStormCheckChange,'swMulticastStormCheckChange':swMulticastStormCheckChange,'swBpduProtectLimit':swBpduProtectLimit,'swChangeStatusLDP':swChangeStatusLDP,'swChangeStatusTunnelRSVP':swChangeStatusTunnelRSVP,'swBpduProtect':swBpduProtect,'swRouteTableFull':swRouteTableFull,'swPanelStatusTrap':swPanelStatusTrap,'swLSTGroupLinkStatusDown':swLSTGroupLinkStatusDown,'swLSTGroupLinkStatusUp':swLSTGroupLinkStatusUp,'swHighCpuL3UsageDetected':swHighCpuL3UsageDetected,'swHighCpuL3UsageNoMoreDetected':swHighCpuL3UsageNoMoreDetected,'swHighMemoryL3UsageDetected':swHighMemoryL3UsageDetected,'swHighMemoryL3UsageNoMoreDetected':swHighMemoryL3UsageNoMoreDetected,'swMpuNsfIdDiffers':swMpuNsfIdDiffers,'swErpsStatusChange':swErpsStatusChange,'swCfmDefect':swCfmDefect,'swLldpRemoteChange':swLldpRemoteChange,'swPoeOverCurrent':swPoeOverCurrent,'swPoePowerRestriction':swPoePowerRestriction,'swCoreDump':swCoreDump,'swElmiEvcStatus':swElmiEvcStatus,'swSyncSystemClockSwitchHier':swSyncSystemClockSwitchHier,'swSyncSystemClockStatus':swSyncSystemClockStatus,'swHostTableFull':swHostTableFull,'swSyncG704ClockStatus':swSyncG704ClockStatus,'swSystemWarningsUnits':swSystemWarningsUnits,'swRebootDueToOvertemp':swRebootDueToOvertemp,'dmSwitchConformance':dmSwitchConformance})