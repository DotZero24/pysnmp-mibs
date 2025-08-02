_d='aniBsuWirelessFreqOperIndex'
_c='aniBsuWirelessFreqAdminIndex'
_b='ds70-us30'
_a='ds60-us40'
_Z='ds50-us50'
_Y='ds40-us60'
_X='ds30-us70'
_W='normal-mode'
_V='low-latency'
_U='vertical'
_T='ism-5-8GHz'
_S='etsi-3-5GHz-100'
_R='etsi-3-5GHz-50'
_Q='general-3-5GHz'
_P='general-2-6GHz'
_O='mmds-2-6GHz'
_N='general-5-8GHz'
_M='unii-5-8GHz'
_L='unii-5-3GHz'
_K='disable'
_J='enable'
_I='DisplayString'
_H='dBm'
_G='MHz'
_F='aniBsuWirelessPort'
_E='BSUWIRELESSIF-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsu,=mibBuilder.importSymbols('ANIROOT-MIB','bsu')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention','TruthValue')
aniBsuWirelessIf=ModuleIdentity((1,3,6,1,4,1,4325,3,2))
_AniBsuWirelessPortTable_Object=MibTable
aniBsuWirelessPortTable=_AniBsuWirelessPortTable_Object((1,3,6,1,4,1,4325,3,2,1))
if mibBuilder.loadTexts:aniBsuWirelessPortTable.setStatus(_A)
_AniBsuWirelessPortEntry_Object=MibTableRow
aniBsuWirelessPortEntry=_AniBsuWirelessPortEntry_Object((1,3,6,1,4,1,4325,3,2,1,1))
aniBsuWirelessPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuWirelessPortEntry.setStatus(_A)
class _AniBsuWirelessPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('wireless-port1',1),('wireless-port2',2),('wireless-port3',3),('wireless-port4',4),('wireless-port5',5),('wireless-port6',6)))
_AniBsuWirelessPort_Type.__name__=_D
_AniBsuWirelessPort_Object=MibTableColumn
aniBsuWirelessPort=_AniBsuWirelessPort_Object((1,3,6,1,4,1,4325,3,2,1,1,1),_AniBsuWirelessPort_Type())
aniBsuWirelessPort.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessPort.setStatus(_A)
_AniBsuPortMacAddr_Type=MacAddress
_AniBsuPortMacAddr_Object=MibTableColumn
aniBsuPortMacAddr=_AniBsuPortMacAddr_Object((1,3,6,1,4,1,4325,3,2,1,1,2),_AniBsuPortMacAddr_Type())
aniBsuPortMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuPortMacAddr.setStatus(_A)
class _AniBsuPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unavailable',1),('initial',2),('unconfig',3),('starting',4),('configured-no-radio-detected',5),('operational-radio',6),('stopped',7),('resetting',8),('disabled',9)))
_AniBsuPortState_Type.__name__=_D
_AniBsuPortState_Object=MibTableColumn
aniBsuPortState=_AniBsuPortState_Object((1,3,6,1,4,1,4325,3,2,1,1,3),_AniBsuPortState_Type())
aniBsuPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuPortState.setStatus(_A)
_AniBsuPortReset_Type=TruthValue
_AniBsuPortReset_Object=MibTableColumn
aniBsuPortReset=_AniBsuPortReset_Object((1,3,6,1,4,1,4325,3,2,1,1,4),_AniBsuPortReset_Type())
aniBsuPortReset.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuPortReset.setStatus(_A)
class _AniBsuPortFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AniBsuPortFlag_Type.__name__=_D
_AniBsuPortFlag_Object=MibTableColumn
aniBsuPortFlag=_AniBsuPortFlag_Object((1,3,6,1,4,1,4325,3,2,1,1,5),_AniBsuPortFlag_Type())
aniBsuPortFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuPortFlag.setStatus(_A)
_AniBsuChannelTable_Object=MibTable
aniBsuChannelTable=_AniBsuChannelTable_Object((1,3,6,1,4,1,4325,3,2,4))
if mibBuilder.loadTexts:aniBsuChannelTable.setStatus(_A)
_AniBsuChannelEntry_Object=MibTableRow
aniBsuChannelEntry=_AniBsuChannelEntry_Object((1,3,6,1,4,1,4325,3,2,4,1))
aniBsuChannelEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuChannelEntry.setStatus(_A)
_AniBsuChannelFrequency_Type=DisplayString
_AniBsuChannelFrequency_Object=MibTableColumn
aniBsuChannelFrequency=_AniBsuChannelFrequency_Object((1,3,6,1,4,1,4325,3,2,4,1,2),_AniBsuChannelFrequency_Type())
aniBsuChannelFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuChannelFrequency.setStatus(_A)
if mibBuilder.loadTexts:aniBsuChannelFrequency.setUnits(_G)
class _AniBsuFrequencyBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10,11,12)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,10),('fdd-3-5GHz',11),('general-5-3GHz',12)))
_AniBsuFrequencyBand_Type.__name__=_D
_AniBsuFrequencyBand_Object=MibTableColumn
aniBsuFrequencyBand=_AniBsuFrequencyBand_Object((1,3,6,1,4,1,4325,3,2,4,1,3),_AniBsuFrequencyBand_Type())
aniBsuFrequencyBand.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuFrequencyBand.setStatus(_A)
_AniBsuChannelWidth_Type=DisplayString
_AniBsuChannelWidth_Object=MibTableColumn
aniBsuChannelWidth=_AniBsuChannelWidth_Object((1,3,6,1,4,1,4325,3,2,4,1,4),_AniBsuChannelWidth_Type())
aniBsuChannelWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuChannelWidth.setStatus(_A)
_AniBsuNumServFlowsPerSu_Type=Integer32
_AniBsuNumServFlowsPerSu_Object=MibTableColumn
aniBsuNumServFlowsPerSu=_AniBsuNumServFlowsPerSu_Object((1,3,6,1,4,1,4325,3,2,4,1,6),_AniBsuNumServFlowsPerSu_Type())
aniBsuNumServFlowsPerSu.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuNumServFlowsPerSu.setStatus(_A)
_AniBsuNumSusSupported_Type=Integer32
_AniBsuNumSusSupported_Object=MibTableColumn
aniBsuNumSusSupported=_AniBsuNumSusSupported_Object((1,3,6,1,4,1,4325,3,2,4,1,7),_AniBsuNumSusSupported_Type())
aniBsuNumSusSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuNumSusSupported.setStatus(_A)
_AniBsuSuRadioRegPowerLimit_Type=Integer32
_AniBsuSuRadioRegPowerLimit_Object=MibTableColumn
aniBsuSuRadioRegPowerLimit=_AniBsuSuRadioRegPowerLimit_Object((1,3,6,1,4,1,4325,3,2,4,1,9),_AniBsuSuRadioRegPowerLimit_Type())
aniBsuSuRadioRegPowerLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuRadioRegPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:aniBsuSuRadioRegPowerLimit.setUnits(_H)
_AniBsuTargetFrequency_Type=DisplayString
_AniBsuTargetFrequency_Object=MibTableColumn
aniBsuTargetFrequency=_AniBsuTargetFrequency_Object((1,3,6,1,4,1,4325,3,2,4,1,10),_AniBsuTargetFrequency_Type())
aniBsuTargetFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuTargetFrequency.setStatus(_A)
if mibBuilder.loadTexts:aniBsuTargetFrequency.setUnits(_G)
_AniBsuQosLinkTable_Object=MibTable
aniBsuQosLinkTable=_AniBsuQosLinkTable_Object((1,3,6,1,4,1,4325,3,2,6))
if mibBuilder.loadTexts:aniBsuQosLinkTable.setStatus(_A)
_AniBsuQosLinkEntry_Object=MibTableRow
aniBsuQosLinkEntry=_AniBsuQosLinkEntry_Object((1,3,6,1,4,1,4325,3,2,6,1))
aniBsuQosLinkEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuQosLinkEntry.setStatus(_A)
_AniBsuBEBandwidth_Type=Integer32
_AniBsuBEBandwidth_Object=MibTableColumn
aniBsuBEBandwidth=_AniBsuBEBandwidth_Object((1,3,6,1,4,1,4325,3,2,6,1,1),_AniBsuBEBandwidth_Type())
aniBsuBEBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuBEBandwidth.setStatus(_A)
_AniBsuCIRBandwidth_Type=Integer32
_AniBsuCIRBandwidth_Object=MibTableColumn
aniBsuCIRBandwidth=_AniBsuCIRBandwidth_Object((1,3,6,1,4,1,4325,3,2,6,1,2),_AniBsuCIRBandwidth_Type())
aniBsuCIRBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuCIRBandwidth.setStatus(_A)
_AniBsuCBRBandwidth_Type=Integer32
_AniBsuCBRBandwidth_Object=MibTableColumn
aniBsuCBRBandwidth=_AniBsuCBRBandwidth_Object((1,3,6,1,4,1,4325,3,2,6,1,3),_AniBsuCBRBandwidth_Type())
aniBsuCBRBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuCBRBandwidth.setStatus(_A)
_AniBsuPowerControlTable_Object=MibTable
aniBsuPowerControlTable=_AniBsuPowerControlTable_Object((1,3,6,1,4,1,4325,3,2,7))
if mibBuilder.loadTexts:aniBsuPowerControlTable.setStatus(_A)
_AniBsuPowerControlEntry_Object=MibTableRow
aniBsuPowerControlEntry=_AniBsuPowerControlEntry_Object((1,3,6,1,4,1,4325,3,2,7,1))
aniBsuPowerControlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuPowerControlEntry.setStatus(_A)
class _AniBsuReceivePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-90,-60))
_AniBsuReceivePower_Type.__name__=_D
_AniBsuReceivePower_Object=MibTableColumn
aniBsuReceivePower=_AniBsuReceivePower_Object((1,3,6,1,4,1,4325,3,2,7,1,2),_AniBsuReceivePower_Type())
aniBsuReceivePower.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuReceivePower.setStatus(_A)
if mibBuilder.loadTexts:aniBsuReceivePower.setUnits(_H)
_AniBsuWssRadioRegPowerLimit_Type=Integer32
_AniBsuWssRadioRegPowerLimit_Object=MibTableColumn
aniBsuWssRadioRegPowerLimit=_AniBsuWssRadioRegPowerLimit_Object((1,3,6,1,4,1,4325,3,2,7,1,3),_AniBsuWssRadioRegPowerLimit_Type())
aniBsuWssRadioRegPowerLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWssRadioRegPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWssRadioRegPowerLimit.setUnits(_H)
_AniBsuAntennaTable_Object=MibTable
aniBsuAntennaTable=_AniBsuAntennaTable_Object((1,3,6,1,4,1,4325,3,2,8))
if mibBuilder.loadTexts:aniBsuAntennaTable.setStatus(_A)
_AniBsuAntennaEntry_Object=MibTableRow
aniBsuAntennaEntry=_AniBsuAntennaEntry_Object((1,3,6,1,4,1,4325,3,2,8,1))
aniBsuAntennaEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuAntennaEntry.setStatus(_A)
class _AniBsuAntennaDiversityFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AniBsuAntennaDiversityFlag_Type.__name__=_D
_AniBsuAntennaDiversityFlag_Object=MibTableColumn
aniBsuAntennaDiversityFlag=_AniBsuAntennaDiversityFlag_Object((1,3,6,1,4,1,4325,3,2,8,1,1),_AniBsuAntennaDiversityFlag_Type())
aniBsuAntennaDiversityFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuAntennaDiversityFlag.setStatus(_A)
class _AniBsuAntennaDiversityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync-based',1),('training-seq-based',2)))
_AniBsuAntennaDiversityMode_Type.__name__=_D
_AniBsuAntennaDiversityMode_Object=MibTableColumn
aniBsuAntennaDiversityMode=_AniBsuAntennaDiversityMode_Object((1,3,6,1,4,1,4325,3,2,8,1,2),_AniBsuAntennaDiversityMode_Type())
aniBsuAntennaDiversityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuAntennaDiversityMode.setStatus(_A)
class _AniBsuBcastAntennaPolarization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('horizontal',1),(_U,2),('horizontal-and-vertical',3)))
_AniBsuBcastAntennaPolarization_Type.__name__=_D
_AniBsuBcastAntennaPolarization_Object=MibTableColumn
aniBsuBcastAntennaPolarization=_AniBsuBcastAntennaPolarization_Object((1,3,6,1,4,1,4325,3,2,8,1,4),_AniBsuBcastAntennaPolarization_Type())
aniBsuBcastAntennaPolarization.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuBcastAntennaPolarization.setStatus(_A)
_AniBsuSectorTable_Object=MibTable
aniBsuSectorTable=_AniBsuSectorTable_Object((1,3,6,1,4,1,4325,3,2,9))
if mibBuilder.loadTexts:aniBsuSectorTable.setStatus(_A)
_AniBsuSectorEntry_Object=MibTableRow
aniBsuSectorEntry=_AniBsuSectorEntry_Object((1,3,6,1,4,1,4325,3,2,9,1))
aniBsuSectorEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuSectorEntry.setStatus(_A)
class _AniBsuSectorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniBsuSectorName_Type.__name__=_I
_AniBsuSectorName_Object=MibTableColumn
aniBsuSectorName=_AniBsuSectorName_Object((1,3,6,1,4,1,4325,3,2,9,1,2),_AniBsuSectorName_Type())
aniBsuSectorName.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSectorName.setStatus(_A)
_AniBsuWirelessPtPConfGroup_ObjectIdentity=ObjectIdentity
aniBsuWirelessPtPConfGroup=_AniBsuWirelessPtPConfGroup_ObjectIdentity((1,3,6,1,4,1,4325,3,2,10))
class _AniBsuWirelessPtPConfFrequencyBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,10)))
_AniBsuWirelessPtPConfFrequencyBand_Type.__name__=_D
_AniBsuWirelessPtPConfFrequencyBand_Object=MibScalar
aniBsuWirelessPtPConfFrequencyBand=_AniBsuWirelessPtPConfFrequencyBand_Object((1,3,6,1,4,1,4325,3,2,10,1),_AniBsuWirelessPtPConfFrequencyBand_Type())
aniBsuWirelessPtPConfFrequencyBand.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfFrequencyBand.setStatus(_A)
class _AniBsuWirelessPtPConfChannelWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2000,3000,3500,4000,5000,6000,7000)));namedValues=NamedValues(*(('width-2',2000),('width-3',3000),('width-3-5',3500),('width-4',4000),('width-5',5000),('width-6',6000),('width-7',7000)))
_AniBsuWirelessPtPConfChannelWidth_Type.__name__=_D
_AniBsuWirelessPtPConfChannelWidth_Object=MibScalar
aniBsuWirelessPtPConfChannelWidth=_AniBsuWirelessPtPConfChannelWidth_Object((1,3,6,1,4,1,4325,3,2,10,2),_AniBsuWirelessPtPConfChannelWidth_Type())
aniBsuWirelessPtPConfChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfChannelWidth.setStatus(_A)
class _AniBsuWirelessPtPConfTDDFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_AniBsuWirelessPtPConfTDDFrameSize_Type.__name__=_D
_AniBsuWirelessPtPConfTDDFrameSize_Object=MibScalar
aniBsuWirelessPtPConfTDDFrameSize=_AniBsuWirelessPtPConfTDDFrameSize_Object((1,3,6,1,4,1,4325,3,2,10,3),_AniBsuWirelessPtPConfTDDFrameSize_Type())
aniBsuWirelessPtPConfTDDFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfTDDFrameSize.setStatus(_A)
class _AniBsuWirelessPtPConfCellRadius_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10000,20000,30000,40000,50000,60000,70000,80000,90000,100000)));namedValues=NamedValues(*(('radius10km',10000),('radius20km',20000),('radius30km',30000),('radius40km',40000),('radius50km',50000),('radius60km',60000),('radius70km',70000),('radius80km',80000),('radius90km',90000),('radius100km',100000)))
_AniBsuWirelessPtPConfCellRadius_Type.__name__=_D
_AniBsuWirelessPtPConfCellRadius_Object=MibScalar
aniBsuWirelessPtPConfCellRadius=_AniBsuWirelessPtPConfCellRadius_Object((1,3,6,1,4,1,4325,3,2,10,4),_AniBsuWirelessPtPConfCellRadius_Type())
aniBsuWirelessPtPConfCellRadius.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfCellRadius.setStatus(_A)
class _AniBsuWirelessPtPConfDSUSRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(30,40,50,60,70)));namedValues=NamedValues(*((_X,30),(_Y,40),(_Z,50),(_a,60),(_b,70)))
_AniBsuWirelessPtPConfDSUSRatio_Type.__name__=_D
_AniBsuWirelessPtPConfDSUSRatio_Object=MibScalar
aniBsuWirelessPtPConfDSUSRatio=_AniBsuWirelessPtPConfDSUSRatio_Object((1,3,6,1,4,1,4325,3,2,10,5),_AniBsuWirelessPtPConfDSUSRatio_Type())
aniBsuWirelessPtPConfDSUSRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfDSUSRatio.setStatus(_A)
class _AniBsuWirelessPtPConfPolarization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_U,2))
_AniBsuWirelessPtPConfPolarization_Type.__name__=_D
_AniBsuWirelessPtPConfPolarization_Object=MibScalar
aniBsuWirelessPtPConfPolarization=_AniBsuWirelessPtPConfPolarization_Object((1,3,6,1,4,1,4325,3,2,10,6),_AniBsuWirelessPtPConfPolarization_Type())
aniBsuWirelessPtPConfPolarization.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfPolarization.setStatus(_A)
_AniBsuWirelessPtPConfTargetFrequency_Type=DisplayString
_AniBsuWirelessPtPConfTargetFrequency_Object=MibScalar
aniBsuWirelessPtPConfTargetFrequency=_AniBsuWirelessPtPConfTargetFrequency_Object((1,3,6,1,4,1,4325,3,2,10,7),_AniBsuWirelessPtPConfTargetFrequency_Type())
aniBsuWirelessPtPConfTargetFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfTargetFrequency.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfTargetFrequency.setUnits(_G)
_AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Type=Integer32
_AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Object=MibScalar
aniBsuWirelessPtPConfBsuRadioRegPowerLimit=_AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Object((1,3,6,1,4,1,4325,3,2,10,8),_AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Type())
aniBsuWirelessPtPConfBsuRadioRegPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfBsuRadioRegPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfBsuRadioRegPowerLimit.setUnits(_H)
_AniBsuWirelessPtPConfSuRadioRegPowerLimit_Type=Integer32
_AniBsuWirelessPtPConfSuRadioRegPowerLimit_Object=MibScalar
aniBsuWirelessPtPConfSuRadioRegPowerLimit=_AniBsuWirelessPtPConfSuRadioRegPowerLimit_Object((1,3,6,1,4,1,4325,3,2,10,9),_AniBsuWirelessPtPConfSuRadioRegPowerLimit_Type())
aniBsuWirelessPtPConfSuRadioRegPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfSuRadioRegPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfSuRadioRegPowerLimit.setUnits(_H)
_AniBsuWirelessPtPConfModify_Type=TruthValue
_AniBsuWirelessPtPConfModify_Object=MibScalar
aniBsuWirelessPtPConfModify=_AniBsuWirelessPtPConfModify_Object((1,3,6,1,4,1,4325,3,2,10,10),_AniBsuWirelessPtPConfModify_Type())
aniBsuWirelessPtPConfModify.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfModify.setStatus(_A)
class _AniBsuWirelessPtPConfBsuId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_AniBsuWirelessPtPConfBsuId_Type.__name__=_I
_AniBsuWirelessPtPConfBsuId_Object=MibScalar
aniBsuWirelessPtPConfBsuId=_AniBsuWirelessPtPConfBsuId_Object((1,3,6,1,4,1,4325,3,2,10,11),_AniBsuWirelessPtPConfBsuId_Type())
aniBsuWirelessPtPConfBsuId.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfBsuId.setStatus(_A)
_AniBsuWirelessPtPConfVerifyAllSu_Type=DisplayString
_AniBsuWirelessPtPConfVerifyAllSu_Object=MibScalar
aniBsuWirelessPtPConfVerifyAllSu=_AniBsuWirelessPtPConfVerifyAllSu_Object((1,3,6,1,4,1,4325,3,2,10,12),_AniBsuWirelessPtPConfVerifyAllSu_Type())
aniBsuWirelessPtPConfVerifyAllSu.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfVerifyAllSu.setStatus(_A)
_AniBsuWirelessPtPConfSwitchToFrequency_Type=DisplayString
_AniBsuWirelessPtPConfSwitchToFrequency_Object=MibScalar
aniBsuWirelessPtPConfSwitchToFrequency=_AniBsuWirelessPtPConfSwitchToFrequency_Object((1,3,6,1,4,1,4325,3,2,10,13),_AniBsuWirelessPtPConfSwitchToFrequency_Type())
aniBsuWirelessPtPConfSwitchToFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfSwitchToFrequency.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfSwitchToFrequency.setUnits(_G)
class _AniBsuWirelessPtPConfSuAFSTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AniBsuWirelessPtPConfSuAFSTimeout_Type.__name__=_D
_AniBsuWirelessPtPConfSuAFSTimeout_Object=MibScalar
aniBsuWirelessPtPConfSuAFSTimeout=_AniBsuWirelessPtPConfSuAFSTimeout_Object((1,3,6,1,4,1,4325,3,2,10,14),_AniBsuWirelessPtPConfSuAFSTimeout_Type())
aniBsuWirelessPtPConfSuAFSTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessPtPConfSuAFSTimeout.setStatus(_A)
_AniBsuWirelessPtPStatusGroup_ObjectIdentity=ObjectIdentity
aniBsuWirelessPtPStatusGroup=_AniBsuWirelessPtPStatusGroup_ObjectIdentity((1,3,6,1,4,1,4325,3,2,11))
_AniBsuWirelessPtPStatusMaxDSAvailBW_Type=DisplayString
_AniBsuWirelessPtPStatusMaxDSAvailBW_Object=MibScalar
aniBsuWirelessPtPStatusMaxDSAvailBW=_AniBsuWirelessPtPStatusMaxDSAvailBW_Object((1,3,6,1,4,1,4325,3,2,11,1),_AniBsuWirelessPtPStatusMaxDSAvailBW_Type())
aniBsuWirelessPtPStatusMaxDSAvailBW.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessPtPStatusMaxDSAvailBW.setStatus(_A)
_AniBsuWirelessPtPStatusMaxUSAvailBW_Type=DisplayString
_AniBsuWirelessPtPStatusMaxUSAvailBW_Object=MibScalar
aniBsuWirelessPtPStatusMaxUSAvailBW=_AniBsuWirelessPtPStatusMaxUSAvailBW_Object((1,3,6,1,4,1,4325,3,2,11,2),_AniBsuWirelessPtPStatusMaxUSAvailBW_Type())
aniBsuWirelessPtPStatusMaxUSAvailBW.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessPtPStatusMaxUSAvailBW.setStatus(_A)
class _AniBsuWirelessPtPStatusTDDFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_AniBsuWirelessPtPStatusTDDFrameSize_Type.__name__=_D
_AniBsuWirelessPtPStatusTDDFrameSize_Object=MibScalar
aniBsuWirelessPtPStatusTDDFrameSize=_AniBsuWirelessPtPStatusTDDFrameSize_Object((1,3,6,1,4,1,4325,3,2,11,3),_AniBsuWirelessPtPStatusTDDFrameSize_Type())
aniBsuWirelessPtPStatusTDDFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessPtPStatusTDDFrameSize.setStatus(_A)
_AniBsuWirelessFreqAdminTable_Object=MibTable
aniBsuWirelessFreqAdminTable=_AniBsuWirelessFreqAdminTable_Object((1,3,6,1,4,1,4325,3,2,12))
if mibBuilder.loadTexts:aniBsuWirelessFreqAdminTable.setStatus(_A)
_AniBsuWirelessFreqAdminEntry_Object=MibTableRow
aniBsuWirelessFreqAdminEntry=_AniBsuWirelessFreqAdminEntry_Object((1,3,6,1,4,1,4325,3,2,12,1))
aniBsuWirelessFreqAdminEntry.setIndexNames((0,_E,_F),(0,_E,_c))
if mibBuilder.loadTexts:aniBsuWirelessFreqAdminEntry.setStatus(_A)
_AniBsuWirelessFreqAdminIndex_Type=Integer32
_AniBsuWirelessFreqAdminIndex_Object=MibTableColumn
aniBsuWirelessFreqAdminIndex=_AniBsuWirelessFreqAdminIndex_Object((1,3,6,1,4,1,4325,3,2,12,1,1),_AniBsuWirelessFreqAdminIndex_Type())
aniBsuWirelessFreqAdminIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessFreqAdminIndex.setStatus(_A)
_AniBsuWirelessFreqAdminFreqValue_Type=DisplayString
_AniBsuWirelessFreqAdminFreqValue_Object=MibTableColumn
aniBsuWirelessFreqAdminFreqValue=_AniBsuWirelessFreqAdminFreqValue_Object((1,3,6,1,4,1,4325,3,2,12,1,2),_AniBsuWirelessFreqAdminFreqValue_Type())
aniBsuWirelessFreqAdminFreqValue.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessFreqAdminFreqValue.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessFreqAdminFreqValue.setUnits(_G)
_AniBsuWirelessFreqOperTable_Object=MibTable
aniBsuWirelessFreqOperTable=_AniBsuWirelessFreqOperTable_Object((1,3,6,1,4,1,4325,3,2,13))
if mibBuilder.loadTexts:aniBsuWirelessFreqOperTable.setStatus(_A)
_AniBsuWirelessFreqOperEntry_Object=MibTableRow
aniBsuWirelessFreqOperEntry=_AniBsuWirelessFreqOperEntry_Object((1,3,6,1,4,1,4325,3,2,13,1))
aniBsuWirelessFreqOperEntry.setIndexNames((0,_E,_F),(0,_E,_d))
if mibBuilder.loadTexts:aniBsuWirelessFreqOperEntry.setStatus(_A)
_AniBsuWirelessFreqOperIndex_Type=Integer32
_AniBsuWirelessFreqOperIndex_Object=MibTableColumn
aniBsuWirelessFreqOperIndex=_AniBsuWirelessFreqOperIndex_Object((1,3,6,1,4,1,4325,3,2,13,1,1),_AniBsuWirelessFreqOperIndex_Type())
aniBsuWirelessFreqOperIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessFreqOperIndex.setStatus(_A)
_AniBsuWirelessFreqOperFreqValue_Type=DisplayString
_AniBsuWirelessFreqOperFreqValue_Object=MibTableColumn
aniBsuWirelessFreqOperFreqValue=_AniBsuWirelessFreqOperFreqValue_Object((1,3,6,1,4,1,4325,3,2,13,1,2),_AniBsuWirelessFreqOperFreqValue_Type())
aniBsuWirelessFreqOperFreqValue.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessFreqOperFreqValue.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessFreqOperFreqValue.setUnits(_G)
_AniBsuWirelessSysConfGroup_ObjectIdentity=ObjectIdentity
aniBsuWirelessSysConfGroup=_AniBsuWirelessSysConfGroup_ObjectIdentity((1,3,6,1,4,1,4325,3,2,14))
class _AniBsuWirelessSysConfBsuId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_AniBsuWirelessSysConfBsuId_Type.__name__=_I
_AniBsuWirelessSysConfBsuId_Object=MibScalar
aniBsuWirelessSysConfBsuId=_AniBsuWirelessSysConfBsuId_Object((1,3,6,1,4,1,4325,3,2,14,1),_AniBsuWirelessSysConfBsuId_Type())
aniBsuWirelessSysConfBsuId.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessSysConfBsuId.setStatus(_A)
_AniBsuWirelessSysConfFrameSize_Type=Integer32
_AniBsuWirelessSysConfFrameSize_Object=MibScalar
aniBsuWirelessSysConfFrameSize=_AniBsuWirelessSysConfFrameSize_Object((1,3,6,1,4,1,4325,3,2,14,2),_AniBsuWirelessSysConfFrameSize_Type())
aniBsuWirelessSysConfFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessSysConfFrameSize.setStatus(_A)
_AniBsuWirelessSysConfFrameDownstreamSize_Type=Integer32
_AniBsuWirelessSysConfFrameDownstreamSize_Object=MibScalar
aniBsuWirelessSysConfFrameDownstreamSize=_AniBsuWirelessSysConfFrameDownstreamSize_Object((1,3,6,1,4,1,4325,3,2,14,3),_AniBsuWirelessSysConfFrameDownstreamSize_Type())
aniBsuWirelessSysConfFrameDownstreamSize.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessSysConfFrameDownstreamSize.setStatus(_A)
_AniBsuWirelessSysConfFrameUpstreamSize_Type=Integer32
_AniBsuWirelessSysConfFrameUpstreamSize_Object=MibScalar
aniBsuWirelessSysConfFrameUpstreamSize=_AniBsuWirelessSysConfFrameUpstreamSize_Object((1,3,6,1,4,1,4325,3,2,14,4),_AniBsuWirelessSysConfFrameUpstreamSize_Type())
aniBsuWirelessSysConfFrameUpstreamSize.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessSysConfFrameUpstreamSize.setStatus(_A)
class _AniBsuWirelessSysConfDSUSRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(30,40,50,60,70)));namedValues=NamedValues(*((_X,30),(_Y,40),(_Z,50),(_a,60),(_b,70)))
_AniBsuWirelessSysConfDSUSRatio_Type.__name__=_D
_AniBsuWirelessSysConfDSUSRatio_Object=MibScalar
aniBsuWirelessSysConfDSUSRatio=_AniBsuWirelessSysConfDSUSRatio_Object((1,3,6,1,4,1,4325,3,2,14,5),_AniBsuWirelessSysConfDSUSRatio_Type())
aniBsuWirelessSysConfDSUSRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessSysConfDSUSRatio.setStatus(_A)
_AniBsuWirelessIfConfTable_Object=MibTable
aniBsuWirelessIfConfTable=_AniBsuWirelessIfConfTable_Object((1,3,6,1,4,1,4325,3,2,15))
if mibBuilder.loadTexts:aniBsuWirelessIfConfTable.setStatus(_A)
_AniBsuWirelessIfConfEntry_Object=MibTableRow
aniBsuWirelessIfConfEntry=_AniBsuWirelessIfConfEntry_Object((1,3,6,1,4,1,4325,3,2,15,1))
aniBsuWirelessIfConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuWirelessIfConfEntry.setStatus(_A)
_AniBsuWirelessIfConfTargetFrequency_Type=DisplayString
_AniBsuWirelessIfConfTargetFrequency_Object=MibTableColumn
aniBsuWirelessIfConfTargetFrequency=_AniBsuWirelessIfConfTargetFrequency_Object((1,3,6,1,4,1,4325,3,2,15,1,1),_AniBsuWirelessIfConfTargetFrequency_Type())
aniBsuWirelessIfConfTargetFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessIfConfTargetFrequency.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessIfConfTargetFrequency.setUnits(_G)
_AniBsuWirelessIfConfVerifyAllSu_Type=DisplayString
_AniBsuWirelessIfConfVerifyAllSu_Object=MibTableColumn
aniBsuWirelessIfConfVerifyAllSu=_AniBsuWirelessIfConfVerifyAllSu_Object((1,3,6,1,4,1,4325,3,2,15,1,2),_AniBsuWirelessIfConfVerifyAllSu_Type())
aniBsuWirelessIfConfVerifyAllSu.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuWirelessIfConfVerifyAllSu.setStatus(_A)
_AniBsuWirelessIfConfSwitchToFrequency_Type=DisplayString
_AniBsuWirelessIfConfSwitchToFrequency_Object=MibTableColumn
aniBsuWirelessIfConfSwitchToFrequency=_AniBsuWirelessIfConfSwitchToFrequency_Object((1,3,6,1,4,1,4325,3,2,15,1,3),_AniBsuWirelessIfConfSwitchToFrequency_Type())
aniBsuWirelessIfConfSwitchToFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessIfConfSwitchToFrequency.setStatus(_A)
if mibBuilder.loadTexts:aniBsuWirelessIfConfSwitchToFrequency.setUnits(_G)
_AniBsuWirelessIfConfModify_Type=TruthValue
_AniBsuWirelessIfConfModify_Object=MibTableColumn
aniBsuWirelessIfConfModify=_AniBsuWirelessIfConfModify_Object((1,3,6,1,4,1,4325,3,2,15,1,50),_AniBsuWirelessIfConfModify_Type())
aniBsuWirelessIfConfModify.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessIfConfModify.setStatus(_A)
_AniBsuWirelessAFSTable_Object=MibTable
aniBsuWirelessAFSTable=_AniBsuWirelessAFSTable_Object((1,3,6,1,4,1,4325,3,2,16))
if mibBuilder.loadTexts:aniBsuWirelessAFSTable.setStatus(_A)
_AniBsuWirelessAFSConfEntry_Object=MibTableRow
aniBsuWirelessAFSConfEntry=_AniBsuWirelessAFSConfEntry_Object((1,3,6,1,4,1,4325,3,2,16,1))
aniBsuWirelessAFSConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniBsuWirelessAFSConfEntry.setStatus(_A)
class _AniBsuWirelessAFSFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AniBsuWirelessAFSFlag_Type.__name__=_D
_AniBsuWirelessAFSFlag_Object=MibTableColumn
aniBsuWirelessAFSFlag=_AniBsuWirelessAFSFlag_Object((1,3,6,1,4,1,4325,3,2,16,1,1),_AniBsuWirelessAFSFlag_Type())
aniBsuWirelessAFSFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessAFSFlag.setStatus(_A)
class _AniBsuWirelessAFSMinSwitchDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_AniBsuWirelessAFSMinSwitchDuration_Type.__name__=_D
_AniBsuWirelessAFSMinSwitchDuration_Object=MibTableColumn
aniBsuWirelessAFSMinSwitchDuration=_AniBsuWirelessAFSMinSwitchDuration_Object((1,3,6,1,4,1,4325,3,2,16,1,2),_AniBsuWirelessAFSMinSwitchDuration_Type())
aniBsuWirelessAFSMinSwitchDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessAFSMinSwitchDuration.setStatus(_A)
class _AniBsuWirelessAFSMinNotificationDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,540))
_AniBsuWirelessAFSMinNotificationDuration_Type.__name__=_D
_AniBsuWirelessAFSMinNotificationDuration_Object=MibTableColumn
aniBsuWirelessAFSMinNotificationDuration=_AniBsuWirelessAFSMinNotificationDuration_Object((1,3,6,1,4,1,4325,3,2,16,1,3),_AniBsuWirelessAFSMinNotificationDuration_Type())
aniBsuWirelessAFSMinNotificationDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessAFSMinNotificationDuration.setStatus(_A)
class _AniBsuWirelessAFSErrPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AniBsuWirelessAFSErrPercentage_Type.__name__=_D
_AniBsuWirelessAFSErrPercentage_Object=MibTableColumn
aniBsuWirelessAFSErrPercentage=_AniBsuWirelessAFSErrPercentage_Object((1,3,6,1,4,1,4325,3,2,16,1,4),_AniBsuWirelessAFSErrPercentage_Type())
aniBsuWirelessAFSErrPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessAFSErrPercentage.setStatus(_A)
class _AniBsuWirelessAFSMinSwitchBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,20000))
_AniBsuWirelessAFSMinSwitchBytes_Type.__name__=_D
_AniBsuWirelessAFSMinSwitchBytes_Object=MibTableColumn
aniBsuWirelessAFSMinSwitchBytes=_AniBsuWirelessAFSMinSwitchBytes_Object((1,3,6,1,4,1,4325,3,2,16,1,5),_AniBsuWirelessAFSMinSwitchBytes_Type())
aniBsuWirelessAFSMinSwitchBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuWirelessAFSMinSwitchBytes.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'aniBsuWirelessIf':aniBsuWirelessIf,'aniBsuWirelessPortTable':aniBsuWirelessPortTable,'aniBsuWirelessPortEntry':aniBsuWirelessPortEntry,_F:aniBsuWirelessPort,'aniBsuPortMacAddr':aniBsuPortMacAddr,'aniBsuPortState':aniBsuPortState,'aniBsuPortReset':aniBsuPortReset,'aniBsuPortFlag':aniBsuPortFlag,'aniBsuChannelTable':aniBsuChannelTable,'aniBsuChannelEntry':aniBsuChannelEntry,'aniBsuChannelFrequency':aniBsuChannelFrequency,'aniBsuFrequencyBand':aniBsuFrequencyBand,'aniBsuChannelWidth':aniBsuChannelWidth,'aniBsuNumServFlowsPerSu':aniBsuNumServFlowsPerSu,'aniBsuNumSusSupported':aniBsuNumSusSupported,'aniBsuSuRadioRegPowerLimit':aniBsuSuRadioRegPowerLimit,'aniBsuTargetFrequency':aniBsuTargetFrequency,'aniBsuQosLinkTable':aniBsuQosLinkTable,'aniBsuQosLinkEntry':aniBsuQosLinkEntry,'aniBsuBEBandwidth':aniBsuBEBandwidth,'aniBsuCIRBandwidth':aniBsuCIRBandwidth,'aniBsuCBRBandwidth':aniBsuCBRBandwidth,'aniBsuPowerControlTable':aniBsuPowerControlTable,'aniBsuPowerControlEntry':aniBsuPowerControlEntry,'aniBsuReceivePower':aniBsuReceivePower,'aniBsuWssRadioRegPowerLimit':aniBsuWssRadioRegPowerLimit,'aniBsuAntennaTable':aniBsuAntennaTable,'aniBsuAntennaEntry':aniBsuAntennaEntry,'aniBsuAntennaDiversityFlag':aniBsuAntennaDiversityFlag,'aniBsuAntennaDiversityMode':aniBsuAntennaDiversityMode,'aniBsuBcastAntennaPolarization':aniBsuBcastAntennaPolarization,'aniBsuSectorTable':aniBsuSectorTable,'aniBsuSectorEntry':aniBsuSectorEntry,'aniBsuSectorName':aniBsuSectorName,'aniBsuWirelessPtPConfGroup':aniBsuWirelessPtPConfGroup,'aniBsuWirelessPtPConfFrequencyBand':aniBsuWirelessPtPConfFrequencyBand,'aniBsuWirelessPtPConfChannelWidth':aniBsuWirelessPtPConfChannelWidth,'aniBsuWirelessPtPConfTDDFrameSize':aniBsuWirelessPtPConfTDDFrameSize,'aniBsuWirelessPtPConfCellRadius':aniBsuWirelessPtPConfCellRadius,'aniBsuWirelessPtPConfDSUSRatio':aniBsuWirelessPtPConfDSUSRatio,'aniBsuWirelessPtPConfPolarization':aniBsuWirelessPtPConfPolarization,'aniBsuWirelessPtPConfTargetFrequency':aniBsuWirelessPtPConfTargetFrequency,'aniBsuWirelessPtPConfBsuRadioRegPowerLimit':aniBsuWirelessPtPConfBsuRadioRegPowerLimit,'aniBsuWirelessPtPConfSuRadioRegPowerLimit':aniBsuWirelessPtPConfSuRadioRegPowerLimit,'aniBsuWirelessPtPConfModify':aniBsuWirelessPtPConfModify,'aniBsuWirelessPtPConfBsuId':aniBsuWirelessPtPConfBsuId,'aniBsuWirelessPtPConfVerifyAllSu':aniBsuWirelessPtPConfVerifyAllSu,'aniBsuWirelessPtPConfSwitchToFrequency':aniBsuWirelessPtPConfSwitchToFrequency,'aniBsuWirelessPtPConfSuAFSTimeout':aniBsuWirelessPtPConfSuAFSTimeout,'aniBsuWirelessPtPStatusGroup':aniBsuWirelessPtPStatusGroup,'aniBsuWirelessPtPStatusMaxDSAvailBW':aniBsuWirelessPtPStatusMaxDSAvailBW,'aniBsuWirelessPtPStatusMaxUSAvailBW':aniBsuWirelessPtPStatusMaxUSAvailBW,'aniBsuWirelessPtPStatusTDDFrameSize':aniBsuWirelessPtPStatusTDDFrameSize,'aniBsuWirelessFreqAdminTable':aniBsuWirelessFreqAdminTable,'aniBsuWirelessFreqAdminEntry':aniBsuWirelessFreqAdminEntry,_c:aniBsuWirelessFreqAdminIndex,'aniBsuWirelessFreqAdminFreqValue':aniBsuWirelessFreqAdminFreqValue,'aniBsuWirelessFreqOperTable':aniBsuWirelessFreqOperTable,'aniBsuWirelessFreqOperEntry':aniBsuWirelessFreqOperEntry,_d:aniBsuWirelessFreqOperIndex,'aniBsuWirelessFreqOperFreqValue':aniBsuWirelessFreqOperFreqValue,'aniBsuWirelessSysConfGroup':aniBsuWirelessSysConfGroup,'aniBsuWirelessSysConfBsuId':aniBsuWirelessSysConfBsuId,'aniBsuWirelessSysConfFrameSize':aniBsuWirelessSysConfFrameSize,'aniBsuWirelessSysConfFrameDownstreamSize':aniBsuWirelessSysConfFrameDownstreamSize,'aniBsuWirelessSysConfFrameUpstreamSize':aniBsuWirelessSysConfFrameUpstreamSize,'aniBsuWirelessSysConfDSUSRatio':aniBsuWirelessSysConfDSUSRatio,'aniBsuWirelessIfConfTable':aniBsuWirelessIfConfTable,'aniBsuWirelessIfConfEntry':aniBsuWirelessIfConfEntry,'aniBsuWirelessIfConfTargetFrequency':aniBsuWirelessIfConfTargetFrequency,'aniBsuWirelessIfConfVerifyAllSu':aniBsuWirelessIfConfVerifyAllSu,'aniBsuWirelessIfConfSwitchToFrequency':aniBsuWirelessIfConfSwitchToFrequency,'aniBsuWirelessIfConfModify':aniBsuWirelessIfConfModify,'aniBsuWirelessAFSTable':aniBsuWirelessAFSTable,'aniBsuWirelessAFSConfEntry':aniBsuWirelessAFSConfEntry,'aniBsuWirelessAFSFlag':aniBsuWirelessAFSFlag,'aniBsuWirelessAFSMinSwitchDuration':aniBsuWirelessAFSMinSwitchDuration,'aniBsuWirelessAFSMinNotificationDuration':aniBsuWirelessAFSMinNotificationDuration,'aniBsuWirelessAFSErrPercentage':aniBsuWirelessAFSErrPercentage,'aniBsuWirelessAFSMinSwitchBytes':aniBsuWirelessAFSMinSwitchBytes})