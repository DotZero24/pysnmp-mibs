_BM='brzaccVLTrapNewIP'
_BL='brzaccVLTrapParameterGroupCode'
_BK='brzaccVLTrapSWVersion'
_BJ='brzaccVLNewUnitTypeTrap'
_BI='brzaccVLTrapMACAddress'
_BH='brzaccVLTrapSubscriberType'
_BG='brzaccVLEthBroadcastThresholdExceeded'
_BF='brzaccVLDFSMoveFreqNew'
_BE='brzaccVLDFSMoveFreq'
_BD='brzaccVLTrapFtpOrTftpStatus'
_BC='brzaccVLTrapParameterChanged'
_BB='brzaccVLTrapAccessRights'
_BA='brzaccVLTrapTelnetUserIpAddress'
_B9='brzaccVLTrapLog'
_B8='brzaccVLTrapRTx'
_B7='brzaccVLAssociatedAU'
_B6='brzaccVLHiddenESSIDMacAddress'
_B5='brzaccVLDrapGatewayIndex'
_B4='mptEthernetStationMACAddress'
_B3='brzaccVLNewAdbMacAddress'
_B2='notAuthenticated'
_B1='authenticated'
_B0='associated'
_A_='brzaccVLAdbIndex'
_Az='brzaccVLSUPerModulationLevelCountersTableIdx'
_Ay='brzaccVLNewIpID'
_Ax='brzaccVLIpFilterIdx'
_Aw='brzaccVLTcpPortRangeIdx'
_Av='brzaccVLUdpPortRangeIdx'
_Au='rtpANDrtcp'
_At='brzaccVLInterferenceMitigationOutputFrequency'
_As='typeNoLOS'
_Ar='brzaccVLNewMaxModulationLevelIdx'
_Aq='brzaccVLNewModulationLevelIdx'
_Ap='brzaccVLCCParamsIndex'
_Ao='brzaccVLCCNumberIdx'
_An='brzaccVLCCNumber'
_Am='brzaccVLSpectrumAnalysisInformationTableIdx'
_Al='resetCounters'
_Ak='currentlyBlocked'
_Aj='activateNow'
_Ai='brzaccVLAutoSubBandFrequencySubsetFrequencyIdx'
_Ah='brzaccVLAutoSubBandFrequencySubsetBandIdx'
_Ag='radarDetected'
_Af='adjacentToRadar'
_Ae='radarFree'
_Ad='brzaccVLDFSChannelIdx'
_Ac='brzaccVLCurrentFrequencySubsetTableIdx'
_Ab='notActive'
_Aa='brzaccVLFrequencySubsetTableIdx'
_AZ='brzaccVLNeighborAuIdx'
_AY='brzaccVLMaximumTransmitPowerIdx'
_AX='level1to5'
_AW='brzaccVLTransmitPowerIdx'
_AV='brzaccVLNewMacAddressDenyListId'
_AU='brzaccVLMacAddressDenyListTableIdx'
_AT='brzaccVLVlanExtendedAccessRulesTableIdx'
_AS='brzaccVLNewVlanIdRelaying'
_AR='brzaccVLVlanRelayingTableIdx'
_AQ='brzaccVLNewVlanIdForwarding'
_AP='brzaccVLVlanForwardingTableIdx'
_AO='brzaccVLNewMngIpRangeStart'
_AN='brzaccVLNewNwMngTrapAddress'
_AM='brzaccVLNewNwMngIpAddress'
_AL='brzaccVLTrapHistorySequenceNumber'
_AK='brzaccVLErrHandlingRequestId'
_AJ='brzaccVLErrHandlingNMSId'
_AI='rangeDefinedByStartAddrMask'
_AH='rangeDefinedByStartEndAddr'
_AG='brzaccVLMngIpRangeIdx'
_AF='brzaccVLNwTrapTableIdx'
_AE='brzaccVLNwMngIpTableIdx'
_AD='fromBothWirelessAndEthernet'
_AC='fromEthernetOnly'
_AB='fromWirelessOnly'
_AA='brzaccVLThresholdLEDnum'
_A9='successful'
_A8='brzaccVLCountryDependentParameterTableIdx'
_A7='brzaccVLTrapToggle'
_A6='modLevel-8'
_A5='modLevel-7'
_A4='modLevel-6'
_A3='modLevel-5'
_A2='modLevel-4'
_A1='modLevel-3'
_A0='modLevel-2'
_z='modLevel-1'
_y='currentlyActive'
_x='inactive'
_w='below-2-Km'
_v='off'
_u='failed'
_t='Unsigned32'
_s='brzaccVLUnitMacAddress'
_r='sharedKey'
_q='openSystem'
_p='fips197'
_o='wep'
_n='automatic'
_m='none'
_l='hwRevisionG'
_k='hwRevisionF'
_j='hwRevisionE'
_i='hwRevisionD'
_h='hwRevisionC'
_g='hwRevisionB'
_f='hwRevisionA'
_e='brzaccVLTrapUnitMacAddr'
_d='brzaccVLTrapSUMacAddr'
_c='deleteAll'
_b='level5'
_a='level4'
_Z='level3'
_Y='level2'
_X='level1'
_W='destroy'
_V='createAndWait'
_U='createAndGo'
_T='notReady'
_S='notInService'
_R='level8'
_Q='level7'
_P='level6'
_O='active'
_N='notSupported'
_M='supported'
_L='cancelOperation'
_K='cancel'
_J='brzaccVLTrapSequenceNumber'
_I='DisplayString'
_H='enable'
_G='disable'
_F='na'
_E='ALVARION-DOT11-WLAN-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_t,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
breezeAccessVLMib=ModuleIdentity((1,3,6,1,4,1,12394,1,1))
if mibBuilder.loadTexts:breezeAccessVLMib.setRevisions(('1910-09-23 11:30',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class DisplayString(OctetString):0
_Alvarion_ObjectIdentity=ObjectIdentity
alvarion=_Alvarion_ObjectIdentity((1,3,6,1,4,1,12394))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,12394,1))
_BrzaccVLSysInfo_ObjectIdentity=ObjectIdentity
brzaccVLSysInfo=_BrzaccVLSysInfo_ObjectIdentity((1,3,6,1,4,1,12394,1,1,1))
class _BrzaccVLUnitHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLUnitHwVersion_Type.__name__=_I
_BrzaccVLUnitHwVersion_Object=MibScalar
brzaccVLUnitHwVersion=_BrzaccVLUnitHwVersion_Object((1,3,6,1,4,1,12394,1,1,1,1),_BrzaccVLUnitHwVersion_Type())
brzaccVLUnitHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUnitHwVersion.setStatus(_A)
class _BrzaccVLRunningSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLRunningSoftwareVersion_Type.__name__=_I
_BrzaccVLRunningSoftwareVersion_Object=MibScalar
brzaccVLRunningSoftwareVersion=_BrzaccVLRunningSoftwareVersion_Object((1,3,6,1,4,1,12394,1,1,1,2),_BrzaccVLRunningSoftwareVersion_Type())
brzaccVLRunningSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRunningSoftwareVersion.setStatus(_A)
class _BrzaccVLRunningFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mainVersion',1),('shadowVersion',2)))
_BrzaccVLRunningFrom_Type.__name__=_C
_BrzaccVLRunningFrom_Object=MibScalar
brzaccVLRunningFrom=_BrzaccVLRunningFrom_Object((1,3,6,1,4,1,12394,1,1,1,3),_BrzaccVLRunningFrom_Type())
brzaccVLRunningFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRunningFrom.setStatus(_A)
class _BrzaccVLMainVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLMainVersionNumber_Type.__name__=_I
_BrzaccVLMainVersionNumber_Object=MibScalar
brzaccVLMainVersionNumber=_BrzaccVLMainVersionNumber_Object((1,3,6,1,4,1,12394,1,1,1,4),_BrzaccVLMainVersionNumber_Type())
brzaccVLMainVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMainVersionNumber.setStatus(_A)
class _BrzaccVLMainVersionFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLMainVersionFileName_Type.__name__=_I
_BrzaccVLMainVersionFileName_Object=MibScalar
brzaccVLMainVersionFileName=_BrzaccVLMainVersionFileName_Object((1,3,6,1,4,1,12394,1,1,1,5),_BrzaccVLMainVersionFileName_Type())
brzaccVLMainVersionFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMainVersionFileName.setStatus(_A)
class _BrzaccVLShadowVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLShadowVersionNumber_Type.__name__=_I
_BrzaccVLShadowVersionNumber_Object=MibScalar
brzaccVLShadowVersionNumber=_BrzaccVLShadowVersionNumber_Object((1,3,6,1,4,1,12394,1,1,1,6),_BrzaccVLShadowVersionNumber_Type())
brzaccVLShadowVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLShadowVersionNumber.setStatus(_A)
class _BrzaccVLShadowVersionFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLShadowVersionFileName_Type.__name__=_I
_BrzaccVLShadowVersionFileName_Object=MibScalar
brzaccVLShadowVersionFileName=_BrzaccVLShadowVersionFileName_Object((1,3,6,1,4,1,12394,1,1,1,7),_BrzaccVLShadowVersionFileName_Type())
brzaccVLShadowVersionFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLShadowVersionFileName.setStatus(_A)
_BrzaccVLUnitMacAddress_Type=MacAddress
_BrzaccVLUnitMacAddress_Object=MibScalar
brzaccVLUnitMacAddress=_BrzaccVLUnitMacAddress_Object((1,3,6,1,4,1,12394,1,1,1,8),_BrzaccVLUnitMacAddress_Type())
brzaccVLUnitMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUnitMacAddress.setStatus(_A)
class _BrzaccVLUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('auBS',1),('auSA',2),('su-6-1D',3),('su-6-BD',4),('su-24-BD',5),('bu-B14',6),('bu-B28',7),('rb-B14',8),('rb-B28',9),('su-BD',10),('su-54-BD',11),('su-3-1D',12),('su-3-4D',13),('ausBS',14),('ausSA',15),('auBS4900',16),('auSA4900',17),('su4900',18),('bu-B100',19),('rb-B100',20),('su-I',21),('au-EZ',22),('su-EZ',23),('su-V',24),('bu-B10',25),('rb-B10',26),('su-8-BD',27),('su-1-BD',28),('su-3-L',29),('su-6-L',30),('su-12-L',31),('au',32),('su',33)))
_BrzaccVLUnitType_Type.__name__=_C
_BrzaccVLUnitType_Object=MibScalar
brzaccVLUnitType=_BrzaccVLUnitType_Object((1,3,6,1,4,1,12394,1,1,1,9),_BrzaccVLUnitType_Type())
brzaccVLUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUnitType.setStatus(_A)
_BrzaccVLAssociatedAU_Type=MacAddress
_BrzaccVLAssociatedAU_Object=MibScalar
brzaccVLAssociatedAU=_BrzaccVLAssociatedAU_Object((1,3,6,1,4,1,12394,1,1,1,10),_BrzaccVLAssociatedAU_Type())
brzaccVLAssociatedAU.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAssociatedAU.setStatus(_A)
_BrzaccVLNumOfAssociationsSinceLastReset_Type=Integer32
_BrzaccVLNumOfAssociationsSinceLastReset_Object=MibScalar
brzaccVLNumOfAssociationsSinceLastReset=_BrzaccVLNumOfAssociationsSinceLastReset_Object((1,3,6,1,4,1,12394,1,1,1,11),_BrzaccVLNumOfAssociationsSinceLastReset_Type())
brzaccVLNumOfAssociationsSinceLastReset.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNumOfAssociationsSinceLastReset.setStatus(_A)
_BrzaccVLCurrentNumOfAssociations_Type=Integer32
_BrzaccVLCurrentNumOfAssociations_Object=MibScalar
brzaccVLCurrentNumOfAssociations=_BrzaccVLCurrentNumOfAssociations_Object((1,3,6,1,4,1,12394,1,1,1,13),_BrzaccVLCurrentNumOfAssociations_Type())
brzaccVLCurrentNumOfAssociations.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentNumOfAssociations.setStatus(_A)
class _BrzaccVLUnitBootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLUnitBootVersion_Type.__name__=_I
_BrzaccVLUnitBootVersion_Object=MibScalar
brzaccVLUnitBootVersion=_BrzaccVLUnitBootVersion_Object((1,3,6,1,4,1,12394,1,1,1,14),_BrzaccVLUnitBootVersion_Type())
brzaccVLUnitBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUnitBootVersion.setStatus(_A)
class _BrzaccVLRadioBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('band-5-8GHz',1),('band-5-4GHz',2),('band-4-9GHz',3),('band-5-2GHz',4),('band-2-4GHz',5),('band-5-3GHz',6),('band-4-9GHzJapan',7),('band-900MHz',8)))
_BrzaccVLRadioBand_Type.__name__=_C
_BrzaccVLRadioBand_Object=MibScalar
brzaccVLRadioBand=_BrzaccVLRadioBand_Object((1,3,6,1,4,1,12394,1,1,1,15),_BrzaccVLRadioBand_Type())
brzaccVLRadioBand.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRadioBand.setStatus(_A)
class _BrzaccVLCurrentEthernetPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('halfDuplexAnd10Mbps',1),('fullDuplexAnd10Mbps',2),('halfDuplexAnd100Mbps',3),('fullDuplexAnd100Mbps',4),('linkDown',5)))
_BrzaccVLCurrentEthernetPortState_Type.__name__=_C
_BrzaccVLCurrentEthernetPortState_Object=MibScalar
brzaccVLCurrentEthernetPortState=_BrzaccVLCurrentEthernetPortState_Object((1,3,6,1,4,1,12394,1,1,1,16),_BrzaccVLCurrentEthernetPortState_Type())
brzaccVLCurrentEthernetPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentEthernetPortState.setStatus(_A)
class _BrzaccVLTimeSinceLastReset_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLTimeSinceLastReset_Type.__name__=_I
_BrzaccVLTimeSinceLastReset_Object=MibScalar
brzaccVLTimeSinceLastReset=_BrzaccVLTimeSinceLastReset_Object((1,3,6,1,4,1,12394,1,1,1,17),_BrzaccVLTimeSinceLastReset_Type())
brzaccVLTimeSinceLastReset.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTimeSinceLastReset.setStatus(_A)
_BrzaccVLCountryDependentParameters_ObjectIdentity=ObjectIdentity
brzaccVLCountryDependentParameters=_BrzaccVLCountryDependentParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,1,18))
class _BrzaccVLCountryCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLCountryCode_Type.__name__=_I
_BrzaccVLCountryCode_Object=MibScalar
brzaccVLCountryCode=_BrzaccVLCountryCode_Object((1,3,6,1,4,1,12394,1,1,1,18,1),_BrzaccVLCountryCode_Type())
brzaccVLCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCountryCode.setStatus(_A)
_BrzaccVLCountryDependentParamsTable_Object=MibTable
brzaccVLCountryDependentParamsTable=_BrzaccVLCountryDependentParamsTable_Object((1,3,6,1,4,1,12394,1,1,1,18,2))
if mibBuilder.loadTexts:brzaccVLCountryDependentParamsTable.setStatus(_A)
_BrzaccVLCountryDependentParameterEntry_Object=MibTableRow
brzaccVLCountryDependentParameterEntry=_BrzaccVLCountryDependentParameterEntry_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1))
brzaccVLCountryDependentParameterEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:brzaccVLCountryDependentParameterEntry.setStatus(_A)
class _BrzaccVLCountryDependentParameterTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_BrzaccVLCountryDependentParameterTableIdx_Type.__name__=_C
_BrzaccVLCountryDependentParameterTableIdx_Object=MibTableColumn
brzaccVLCountryDependentParameterTableIdx=_BrzaccVLCountryDependentParameterTableIdx_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,1),_BrzaccVLCountryDependentParameterTableIdx_Type())
brzaccVLCountryDependentParameterTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCountryDependentParameterTableIdx.setStatus(_A)
_BrzaccVLCountryDependentParameterFrequencies_Type=DisplayString
_BrzaccVLCountryDependentParameterFrequencies_Object=MibTableColumn
brzaccVLCountryDependentParameterFrequencies=_BrzaccVLCountryDependentParameterFrequencies_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,2),_BrzaccVLCountryDependentParameterFrequencies_Type())
brzaccVLCountryDependentParameterFrequencies.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCountryDependentParameterFrequencies.setStatus(_A)
_BrzaccVLAllowedBandwidth_Type=Integer32
_BrzaccVLAllowedBandwidth_Object=MibTableColumn
brzaccVLAllowedBandwidth=_BrzaccVLAllowedBandwidth_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,3),_BrzaccVLAllowedBandwidth_Type())
brzaccVLAllowedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAllowedBandwidth.setStatus(_A)
_BrzaccVLRegulationMaxTxPowerAtAntennaPort_Type=Integer32
_BrzaccVLRegulationMaxTxPowerAtAntennaPort_Object=MibTableColumn
brzaccVLRegulationMaxTxPowerAtAntennaPort=_BrzaccVLRegulationMaxTxPowerAtAntennaPort_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,4),_BrzaccVLRegulationMaxTxPowerAtAntennaPort_Type())
brzaccVLRegulationMaxTxPowerAtAntennaPort.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRegulationMaxTxPowerAtAntennaPort.setStatus(_A)
_BrzaccVLRegulationMaxEIRP_Type=Integer32
_BrzaccVLRegulationMaxEIRP_Object=MibTableColumn
brzaccVLRegulationMaxEIRP=_BrzaccVLRegulationMaxEIRP_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,5),_BrzaccVLRegulationMaxEIRP_Type())
brzaccVLRegulationMaxEIRP.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRegulationMaxEIRP.setStatus(_A)
class _BrzaccVLMinModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_P,6),(_Q,7),(_R,8)))
_BrzaccVLMinModulationLevel_Type.__name__=_C
_BrzaccVLMinModulationLevel_Object=MibTableColumn
brzaccVLMinModulationLevel=_BrzaccVLMinModulationLevel_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,6),_BrzaccVLMinModulationLevel_Type())
brzaccVLMinModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMinModulationLevel.setStatus(_A)
class _BrzaccVLMaxModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_P,6),(_Q,7),(_R,8)))
_BrzaccVLMaxModulationLevel_Type.__name__=_C
_BrzaccVLMaxModulationLevel_Object=MibTableColumn
brzaccVLMaxModulationLevel=_BrzaccVLMaxModulationLevel_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,7),_BrzaccVLMaxModulationLevel_Type())
brzaccVLMaxModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMaxModulationLevel.setStatus(_A)
class _BrzaccVLBurstModeSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLBurstModeSupport_Type.__name__=_C
_BrzaccVLBurstModeSupport_Object=MibTableColumn
brzaccVLBurstModeSupport=_BrzaccVLBurstModeSupport_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,8),_BrzaccVLBurstModeSupport_Type())
brzaccVLBurstModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLBurstModeSupport.setStatus(_A)
_BrzaccVLMaximumBurstDuration_Type=Integer32
_BrzaccVLMaximumBurstDuration_Object=MibTableColumn
brzaccVLMaximumBurstDuration=_BrzaccVLMaximumBurstDuration_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,9),_BrzaccVLMaximumBurstDuration_Type())
brzaccVLMaximumBurstDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMaximumBurstDuration.setStatus(_A)
class _BrzaccVLDfsSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLDfsSupport_Type.__name__=_C
_BrzaccVLDfsSupport_Object=MibTableColumn
brzaccVLDfsSupport=_BrzaccVLDfsSupport_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,10),_BrzaccVLDfsSupport_Type())
brzaccVLDfsSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDfsSupport.setStatus(_A)
class _BrzaccVLMinimumHwRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_F,255)))
_BrzaccVLMinimumHwRevision_Type.__name__=_C
_BrzaccVLMinimumHwRevision_Object=MibTableColumn
brzaccVLMinimumHwRevision=_BrzaccVLMinimumHwRevision_Object((1,3,6,1,4,1,12394,1,1,1,18,2,1,11),_BrzaccVLMinimumHwRevision_Type())
brzaccVLMinimumHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMinimumHwRevision.setStatus(_A)
class _BrzaccVLAuthenticationEncryptionSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLAuthenticationEncryptionSupport_Type.__name__=_C
_BrzaccVLAuthenticationEncryptionSupport_Object=MibScalar
brzaccVLAuthenticationEncryptionSupport=_BrzaccVLAuthenticationEncryptionSupport_Object((1,3,6,1,4,1,12394,1,1,1,18,3),_BrzaccVLAuthenticationEncryptionSupport_Type())
brzaccVLAuthenticationEncryptionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAuthenticationEncryptionSupport.setStatus(_A)
class _BrzaccVLDataEncryptionSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLDataEncryptionSupport_Type.__name__=_C
_BrzaccVLDataEncryptionSupport_Object=MibScalar
brzaccVLDataEncryptionSupport=_BrzaccVLDataEncryptionSupport_Object((1,3,6,1,4,1,12394,1,1,1,18,4),_BrzaccVLDataEncryptionSupport_Type())
brzaccVLDataEncryptionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDataEncryptionSupport.setStatus(_A)
class _BrzaccVLAESEncryptionSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLAESEncryptionSupport_Type.__name__=_C
_BrzaccVLAESEncryptionSupport_Object=MibScalar
brzaccVLAESEncryptionSupport=_BrzaccVLAESEncryptionSupport_Object((1,3,6,1,4,1,12394,1,1,1,18,5),_BrzaccVLAESEncryptionSupport_Type())
brzaccVLAESEncryptionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAESEncryptionSupport.setStatus(_A)
class _BrzaccVLAntennaGainChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLAntennaGainChange_Type.__name__=_C
_BrzaccVLAntennaGainChange_Object=MibScalar
brzaccVLAntennaGainChange=_BrzaccVLAntennaGainChange_Object((1,3,6,1,4,1,12394,1,1,1,19),_BrzaccVLAntennaGainChange_Type())
brzaccVLAntennaGainChange.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAntennaGainChange.setStatus(_A)
class _BrzaccVLAteTestResults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_m,0),('pass',1),('fail',2)))
_BrzaccVLAteTestResults_Type.__name__=_C
_BrzaccVLAteTestResults_Object=MibScalar
brzaccVLAteTestResults=_BrzaccVLAteTestResults_Object((1,3,6,1,4,1,12394,1,1,1,20),_BrzaccVLAteTestResults_Type())
brzaccVLAteTestResults.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAteTestResults.setStatus(_A)
class _BrzaccVLSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_BrzaccVLSerialNumber_Type.__name__=_I
_BrzaccVLSerialNumber_Object=MibScalar
brzaccVLSerialNumber=_BrzaccVLSerialNumber_Object((1,3,6,1,4,1,12394,1,1,1,21),_BrzaccVLSerialNumber_Type())
brzaccVLSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSerialNumber.setStatus(_A)
class _BrzaccVLAUSSupportSU54_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('true',1),('false',2),(_F,255)))
_BrzaccVLAUSSupportSU54_Type.__name__=_C
_BrzaccVLAUSSupportSU54_Object=MibScalar
brzaccVLAUSSupportSU54=_BrzaccVLAUSSupportSU54_Object((1,3,6,1,4,1,12394,1,1,1,22),_BrzaccVLAUSSupportSU54_Type())
brzaccVLAUSSupportSU54.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAUSSupportSU54.setStatus(_A)
_BrzaccVLNumOfRejectionsSinceLastReset_Type=Integer32
_BrzaccVLNumOfRejectionsSinceLastReset_Object=MibScalar
brzaccVLNumOfRejectionsSinceLastReset=_BrzaccVLNumOfRejectionsSinceLastReset_Object((1,3,6,1,4,1,12394,1,1,1,23),_BrzaccVLNumOfRejectionsSinceLastReset_Type())
brzaccVLNumOfRejectionsSinceLastReset.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNumOfRejectionsSinceLastReset.setStatus(_A)
class _BrzaccVLAUSSupportSU8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('true',1),('false',2),(_F,255)))
_BrzaccVLAUSSupportSU8_Type.__name__=_C
_BrzaccVLAUSSupportSU8_Object=MibScalar
brzaccVLAUSSupportSU8=_BrzaccVLAUSSupportSU8_Object((1,3,6,1,4,1,12394,1,1,1,24),_BrzaccVLAUSSupportSU8_Type())
brzaccVLAUSSupportSU8.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAUSSupportSU8.setStatus(_A)
_BrzaccVLUnitControl_ObjectIdentity=ObjectIdentity
brzaccVLUnitControl=_BrzaccVLUnitControl_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2))
class _BrzaccVLResetUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('resetSystemNow',2)))
_BrzaccVLResetUnit_Type.__name__=_C
_BrzaccVLResetUnit_Object=MibScalar
brzaccVLResetUnit=_BrzaccVLResetUnit_Object((1,3,6,1,4,1,12394,1,1,2,1),_BrzaccVLResetUnit_Type())
brzaccVLResetUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLResetUnit.setStatus(_A)
class _BrzaccVLSetDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noDefaultSettingRequested',0),('completeFactory',1),('partialFactory',2),('completeOperator',3),('partialOperator',4),('cancelCurrentPendingRequest',5)))
_BrzaccVLSetDefaults_Type.__name__=_C
_BrzaccVLSetDefaults_Object=MibScalar
brzaccVLSetDefaults=_BrzaccVLSetDefaults_Object((1,3,6,1,4,1,12394,1,1,2,2),_BrzaccVLSetDefaults_Type())
brzaccVLSetDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSetDefaults.setStatus(_A)
class _BrzaccVLUnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLUnitName_Type.__name__=_I
_BrzaccVLUnitName_Object=MibScalar
brzaccVLUnitName=_BrzaccVLUnitName_Object((1,3,6,1,4,1,12394,1,1,2,3),_BrzaccVLUnitName_Type())
brzaccVLUnitName.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUnitName.setStatus(_A)
class _BrzaccVLFlashMemoryControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('resetAndBootFromShadowVersion',1),('useRunningVersionAfterReset',2),(_K,3)))
_BrzaccVLFlashMemoryControl_Type.__name__=_C
_BrzaccVLFlashMemoryControl_Object=MibScalar
brzaccVLFlashMemoryControl=_BrzaccVLFlashMemoryControl_Object((1,3,6,1,4,1,12394,1,1,2,4),_BrzaccVLFlashMemoryControl_Type())
brzaccVLFlashMemoryControl.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFlashMemoryControl.setStatus(_A)
_BrzaccVLTelnetLogoutTimer_Type=Integer32
_BrzaccVLTelnetLogoutTimer_Object=MibScalar
brzaccVLTelnetLogoutTimer=_BrzaccVLTelnetLogoutTimer_Object((1,3,6,1,4,1,12394,1,1,2,5),_BrzaccVLTelnetLogoutTimer_Type())
brzaccVLTelnetLogoutTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTelnetLogoutTimer.setStatus(_A)
class _BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('saveAsDefaults',1),(_K,2)))
_BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Type.__name__=_C
_BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Object=MibScalar
brzaccVLSaveCurrentConfigurationAsOperatorDefaults=_BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Object((1,3,6,1,4,1,12394,1,1,2,6),_BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Type())
brzaccVLSaveCurrentConfigurationAsOperatorDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSaveCurrentConfigurationAsOperatorDefaults.setStatus(_A)
class _BrzaccVLExitTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('exit',2)))
_BrzaccVLExitTelnet_Type.__name__=_C
_BrzaccVLExitTelnet_Object=MibScalar
brzaccVLExitTelnet=_BrzaccVLExitTelnet_Object((1,3,6,1,4,1,12394,1,1,2,7),_BrzaccVLExitTelnet_Type())
brzaccVLExitTelnet.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLExitTelnet.setStatus(_A)
_BrzaccVLUnitPasswords_ObjectIdentity=ObjectIdentity
brzaccVLUnitPasswords=_BrzaccVLUnitPasswords_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,8))
class _BrzaccVLReadOnlyPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_BrzaccVLReadOnlyPassword_Type.__name__=_I
_BrzaccVLReadOnlyPassword_Object=MibScalar
brzaccVLReadOnlyPassword=_BrzaccVLReadOnlyPassword_Object((1,3,6,1,4,1,12394,1,1,2,8,1),_BrzaccVLReadOnlyPassword_Type())
brzaccVLReadOnlyPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLReadOnlyPassword.setStatus(_A)
class _BrzaccVLInstallerPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_BrzaccVLInstallerPassword_Type.__name__=_I
_BrzaccVLInstallerPassword_Object=MibScalar
brzaccVLInstallerPassword=_BrzaccVLInstallerPassword_Object((1,3,6,1,4,1,12394,1,1,2,8,2),_BrzaccVLInstallerPassword_Type())
brzaccVLInstallerPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInstallerPassword.setStatus(_A)
class _BrzaccVLAdminPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_BrzaccVLAdminPassword_Type.__name__=_I
_BrzaccVLAdminPassword_Object=MibScalar
brzaccVLAdminPassword=_BrzaccVLAdminPassword_Object((1,3,6,1,4,1,12394,1,1,2,8,3),_BrzaccVLAdminPassword_Type())
brzaccVLAdminPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdminPassword.setStatus(_A)
class _BrzaccVLEthernetNegotiationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('force10MbpsAndHalfDuplex',1),('force10MbpsAndFullDuplex',2),('force100MbpsAndHalfDuplex',3),('force100MbpsAndFullDuplex',4),('autoNegotiationMode',5)))
_BrzaccVLEthernetNegotiationMode_Type.__name__=_C
_BrzaccVLEthernetNegotiationMode_Object=MibScalar
brzaccVLEthernetNegotiationMode=_BrzaccVLEthernetNegotiationMode_Object((1,3,6,1,4,1,12394,1,1,2,9),_BrzaccVLEthernetNegotiationMode_Type())
brzaccVLEthernetNegotiationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthernetNegotiationMode.setStatus(_A)
_BrzaccVLFTPParameters_ObjectIdentity=ObjectIdentity
brzaccVLFTPParameters=_BrzaccVLFTPParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,10))
_BrzaccVLFTPServerParams_ObjectIdentity=ObjectIdentity
brzaccVLFTPServerParams=_BrzaccVLFTPServerParams_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,10,1))
class _BrzaccVLFTPServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_BrzaccVLFTPServerUserName_Type.__name__=_I
_BrzaccVLFTPServerUserName_Object=MibScalar
brzaccVLFTPServerUserName=_BrzaccVLFTPServerUserName_Object((1,3,6,1,4,1,12394,1,1,2,10,1,1),_BrzaccVLFTPServerUserName_Type())
brzaccVLFTPServerUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPServerUserName.setStatus(_A)
class _BrzaccVLFTPServerPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_BrzaccVLFTPServerPassword_Type.__name__=_I
_BrzaccVLFTPServerPassword_Object=MibScalar
brzaccVLFTPServerPassword=_BrzaccVLFTPServerPassword_Object((1,3,6,1,4,1,12394,1,1,2,10,1,2),_BrzaccVLFTPServerPassword_Type())
brzaccVLFTPServerPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPServerPassword.setStatus(_A)
_BrzaccVLFTPClientIPAddress_Type=IpAddress
_BrzaccVLFTPClientIPAddress_Object=MibScalar
brzaccVLFTPClientIPAddress=_BrzaccVLFTPClientIPAddress_Object((1,3,6,1,4,1,12394,1,1,2,10,1,3),_BrzaccVLFTPClientIPAddress_Type())
brzaccVLFTPClientIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPClientIPAddress.setStatus(_A)
_BrzaccVLFTPServerIpAddress_Type=IpAddress
_BrzaccVLFTPServerIpAddress_Object=MibScalar
brzaccVLFTPServerIpAddress=_BrzaccVLFTPServerIpAddress_Object((1,3,6,1,4,1,12394,1,1,2,10,1,4),_BrzaccVLFTPServerIpAddress_Type())
brzaccVLFTPServerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPServerIpAddress.setStatus(_A)
_BrzaccVLFTPClientMask_Type=IpAddress
_BrzaccVLFTPClientMask_Object=MibScalar
brzaccVLFTPClientMask=_BrzaccVLFTPClientMask_Object((1,3,6,1,4,1,12394,1,1,2,10,1,5),_BrzaccVLFTPClientMask_Type())
brzaccVLFTPClientMask.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPClientMask.setStatus(_A)
_BrzaccVLFTPGatewayIpAddress_Type=IpAddress
_BrzaccVLFTPGatewayIpAddress_Object=MibScalar
brzaccVLFTPGatewayIpAddress=_BrzaccVLFTPGatewayIpAddress_Object((1,3,6,1,4,1,12394,1,1,2,10,1,6),_BrzaccVLFTPGatewayIpAddress_Type())
brzaccVLFTPGatewayIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPGatewayIpAddress.setStatus(_A)
_BrzaccVLFTPSwDownload_ObjectIdentity=ObjectIdentity
brzaccVLFTPSwDownload=_BrzaccVLFTPSwDownload_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,10,2))
class _BrzaccVLFTPSwFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_BrzaccVLFTPSwFileName_Type.__name__=_I
_BrzaccVLFTPSwFileName_Object=MibScalar
brzaccVLFTPSwFileName=_BrzaccVLFTPSwFileName_Object((1,3,6,1,4,1,12394,1,1,2,10,2,1),_BrzaccVLFTPSwFileName_Type())
brzaccVLFTPSwFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPSwFileName.setStatus(_A)
class _BrzaccVLFTPSwSourceDir_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_BrzaccVLFTPSwSourceDir_Type.__name__=_I
_BrzaccVLFTPSwSourceDir_Object=MibScalar
brzaccVLFTPSwSourceDir=_BrzaccVLFTPSwSourceDir_Object((1,3,6,1,4,1,12394,1,1,2,10,2,2),_BrzaccVLFTPSwSourceDir_Type())
brzaccVLFTPSwSourceDir.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPSwSourceDir.setStatus(_A)
class _BrzaccVLFTPDownloadSwFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('downloadFile',1),(_K,2)))
_BrzaccVLFTPDownloadSwFile_Type.__name__=_C
_BrzaccVLFTPDownloadSwFile_Object=MibScalar
brzaccVLFTPDownloadSwFile=_BrzaccVLFTPDownloadSwFile_Object((1,3,6,1,4,1,12394,1,1,2,10,2,3),_BrzaccVLFTPDownloadSwFile_Type())
brzaccVLFTPDownloadSwFile.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPDownloadSwFile.setStatus(_A)
_BrzaccVLConfigurationFileLoading_ObjectIdentity=ObjectIdentity
brzaccVLConfigurationFileLoading=_BrzaccVLConfigurationFileLoading_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,10,3))
class _BrzaccVLConfigurationFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_BrzaccVLConfigurationFileName_Type.__name__=_I
_BrzaccVLConfigurationFileName_Object=MibScalar
brzaccVLConfigurationFileName=_BrzaccVLConfigurationFileName_Object((1,3,6,1,4,1,12394,1,1,2,10,3,1),_BrzaccVLConfigurationFileName_Type())
brzaccVLConfigurationFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLConfigurationFileName.setStatus(_A)
class _BrzaccVLOperatorDefaultsFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_BrzaccVLOperatorDefaultsFileName_Type.__name__=_I
_BrzaccVLOperatorDefaultsFileName_Object=MibScalar
brzaccVLOperatorDefaultsFileName=_BrzaccVLOperatorDefaultsFileName_Object((1,3,6,1,4,1,12394,1,1,2,10,3,2),_BrzaccVLOperatorDefaultsFileName_Type())
brzaccVLOperatorDefaultsFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLOperatorDefaultsFileName.setStatus(_A)
class _BrzaccVLFTPConfigurationFileSourceDir_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_BrzaccVLFTPConfigurationFileSourceDir_Type.__name__=_I
_BrzaccVLFTPConfigurationFileSourceDir_Object=MibScalar
brzaccVLFTPConfigurationFileSourceDir=_BrzaccVLFTPConfigurationFileSourceDir_Object((1,3,6,1,4,1,12394,1,1,2,10,3,3),_BrzaccVLFTPConfigurationFileSourceDir_Type())
brzaccVLFTPConfigurationFileSourceDir.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFTPConfigurationFileSourceDir.setStatus(_A)
class _BrzaccVLExecuteFTPConfigurationFileLoading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('executeFTPGetConfigurationFile',1),('executeFTPPutConfigurationFile',2),('executeFTPGetOperatorDefaults',3),('executeFTPPutOperatorDefaults',4),(_K,5)))
_BrzaccVLExecuteFTPConfigurationFileLoading_Type.__name__=_C
_BrzaccVLExecuteFTPConfigurationFileLoading_Object=MibScalar
brzaccVLExecuteFTPConfigurationFileLoading=_BrzaccVLExecuteFTPConfigurationFileLoading_Object((1,3,6,1,4,1,12394,1,1,2,10,3,4),_BrzaccVLExecuteFTPConfigurationFileLoading_Type())
brzaccVLExecuteFTPConfigurationFileLoading.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLExecuteFTPConfigurationFileLoading.setStatus(_A)
_BrzaccVLEventLogFileUploading_ObjectIdentity=ObjectIdentity
brzaccVLEventLogFileUploading=_BrzaccVLEventLogFileUploading_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,10,4))
class _BrzaccVLEventLogFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_BrzaccVLEventLogFileName_Type.__name__=_I
_BrzaccVLEventLogFileName_Object=MibScalar
brzaccVLEventLogFileName=_BrzaccVLEventLogFileName_Object((1,3,6,1,4,1,12394,1,1,2,10,4,1),_BrzaccVLEventLogFileName_Type())
brzaccVLEventLogFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEventLogFileName.setStatus(_A)
class _BrzaccVLEventLogDestinationDir_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_BrzaccVLEventLogDestinationDir_Type.__name__=_I
_BrzaccVLEventLogDestinationDir_Object=MibScalar
brzaccVLEventLogDestinationDir=_BrzaccVLEventLogDestinationDir_Object((1,3,6,1,4,1,12394,1,1,2,10,4,2),_BrzaccVLEventLogDestinationDir_Type())
brzaccVLEventLogDestinationDir.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEventLogDestinationDir.setStatus(_A)
class _BrzaccVLUploadEventLogFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uploadFile',1),(_K,2)))
_BrzaccVLUploadEventLogFile_Type.__name__=_C
_BrzaccVLUploadEventLogFile_Object=MibScalar
brzaccVLUploadEventLogFile=_BrzaccVLUploadEventLogFile_Object((1,3,6,1,4,1,12394,1,1,2,10,4,3),_BrzaccVLUploadEventLogFile_Type())
brzaccVLUploadEventLogFile.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUploadEventLogFile.setStatus(_A)
class _BrzaccVLLoadingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inProcess',1),(_A9,2),(_u,3)))
_BrzaccVLLoadingStatus_Type.__name__=_C
_BrzaccVLLoadingStatus_Object=MibScalar
brzaccVLLoadingStatus=_BrzaccVLLoadingStatus_Object((1,3,6,1,4,1,12394,1,1,2,11),_BrzaccVLLoadingStatus_Type())
brzaccVLLoadingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLLoadingStatus.setStatus(_A)
_BrzaccVLEventLogFileParams_ObjectIdentity=ObjectIdentity
brzaccVLEventLogFileParams=_BrzaccVLEventLogFileParams_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,12))
class _BrzaccVLEventLogPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('message',1),('warning',2),('error',3),('fatal',4),('logNone',5)))
_BrzaccVLEventLogPolicy_Type.__name__=_C
_BrzaccVLEventLogPolicy_Object=MibScalar
brzaccVLEventLogPolicy=_BrzaccVLEventLogPolicy_Object((1,3,6,1,4,1,12394,1,1,2,12,1),_BrzaccVLEventLogPolicy_Type())
brzaccVLEventLogPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEventLogPolicy.setStatus(_A)
class _BrzaccVLEraseEventLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eraseEventLog',1),(_K,2)))
_BrzaccVLEraseEventLog_Type.__name__=_C
_BrzaccVLEraseEventLog_Object=MibScalar
brzaccVLEraseEventLog=_BrzaccVLEraseEventLog_Object((1,3,6,1,4,1,12394,1,1,2,12,2),_BrzaccVLEraseEventLog_Type())
brzaccVLEraseEventLog.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEraseEventLog.setStatus(_A)
class _BrzaccVLSystemLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,34))
_BrzaccVLSystemLocation_Type.__name__=_I
_BrzaccVLSystemLocation_Object=MibScalar
brzaccVLSystemLocation=_BrzaccVLSystemLocation_Object((1,3,6,1,4,1,12394,1,1,2,13),_BrzaccVLSystemLocation_Type())
brzaccVLSystemLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSystemLocation.setStatus(_A)
_BrzaccVLFeatureUpgrade_ObjectIdentity=ObjectIdentity
brzaccVLFeatureUpgrade=_BrzaccVLFeatureUpgrade_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,14))
class _BrzaccVLFeatureUpgradeManually_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,64))
_BrzaccVLFeatureUpgradeManually_Type.__name__=_I
_BrzaccVLFeatureUpgradeManually_Object=MibScalar
brzaccVLFeatureUpgradeManually=_BrzaccVLFeatureUpgradeManually_Object((1,3,6,1,4,1,12394,1,1,2,14,1),_BrzaccVLFeatureUpgradeManually_Type())
brzaccVLFeatureUpgradeManually.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFeatureUpgradeManually.setStatus(_A)
class _BrzaccVLChangeUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bu',1),('rb',2),(_K,3)))
_BrzaccVLChangeUnitType_Type.__name__=_C
_BrzaccVLChangeUnitType_Object=MibScalar
brzaccVLChangeUnitType=_BrzaccVLChangeUnitType_Object((1,3,6,1,4,1,12394,1,1,2,15),_BrzaccVLChangeUnitType_Type())
brzaccVLChangeUnitType.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLChangeUnitType.setStatus(_A)
class _BrzaccVLApWorkingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*(('ezMode',1),(_F,255)))
_BrzaccVLApWorkingMode_Type.__name__=_C
_BrzaccVLApWorkingMode_Object=MibScalar
brzaccVLApWorkingMode=_BrzaccVLApWorkingMode_Object((1,3,6,1,4,1,12394,1,1,2,16),_BrzaccVLApWorkingMode_Type())
brzaccVLApWorkingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLApWorkingMode.setStatus(_A)
_BrzaccVLLEDsettings_ObjectIdentity=ObjectIdentity
brzaccVLLEDsettings=_BrzaccVLLEDsettings_ObjectIdentity((1,3,6,1,4,1,12394,1,1,2,17))
class _BrzaccVLLEDmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('threshold',2)))
_BrzaccVLLEDmode_Type.__name__=_C
_BrzaccVLLEDmode_Object=MibScalar
brzaccVLLEDmode=_BrzaccVLLEDmode_Object((1,3,6,1,4,1,12394,1,1,2,17,1),_BrzaccVLLEDmode_Type())
brzaccVLLEDmode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLLEDmode.setStatus(_A)
_BrzaccVLThresholdTable_Object=MibTable
brzaccVLThresholdTable=_BrzaccVLThresholdTable_Object((1,3,6,1,4,1,12394,1,1,2,17,2))
if mibBuilder.loadTexts:brzaccVLThresholdTable.setStatus(_A)
_BrzaccVLThresholdTableEntry_Object=MibTableRow
brzaccVLThresholdTableEntry=_BrzaccVLThresholdTableEntry_Object((1,3,6,1,4,1,12394,1,1,2,17,2,1))
brzaccVLThresholdTableEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:brzaccVLThresholdTableEntry.setStatus(_A)
class _BrzaccVLThresholdLEDnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BrzaccVLThresholdLEDnum_Type.__name__=_C
_BrzaccVLThresholdLEDnum_Object=MibTableColumn
brzaccVLThresholdLEDnum=_BrzaccVLThresholdLEDnum_Object((1,3,6,1,4,1,12394,1,1,2,17,2,1,1),_BrzaccVLThresholdLEDnum_Type())
brzaccVLThresholdLEDnum.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLThresholdLEDnum.setStatus(_A)
class _BrzaccVLThresholdLEDtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('typeDisabled',1),('typeRSSI',2),('typeCRC',3),('typeSNR',4),('typeAverageModulation',5)))
_BrzaccVLThresholdLEDtype_Type.__name__=_C
_BrzaccVLThresholdLEDtype_Object=MibTableColumn
brzaccVLThresholdLEDtype=_BrzaccVLThresholdLEDtype_Object((1,3,6,1,4,1,12394,1,1,2,17,2,1,2),_BrzaccVLThresholdLEDtype_Type())
brzaccVLThresholdLEDtype.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLThresholdLEDtype.setStatus(_A)
class _BrzaccVLThresholdLEDmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('equalOrLower',1),('equalOrHigher',2),('equal',3)))
_BrzaccVLThresholdLEDmode_Type.__name__=_C
_BrzaccVLThresholdLEDmode_Object=MibTableColumn
brzaccVLThresholdLEDmode=_BrzaccVLThresholdLEDmode_Object((1,3,6,1,4,1,12394,1,1,2,17,2,1,3),_BrzaccVLThresholdLEDmode_Type())
brzaccVLThresholdLEDmode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLThresholdLEDmode.setStatus(_A)
class _BrzaccVLThresholdLEDtarget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-108,100))
_BrzaccVLThresholdLEDtarget_Type.__name__=_C
_BrzaccVLThresholdLEDtarget_Object=MibTableColumn
brzaccVLThresholdLEDtarget=_BrzaccVLThresholdLEDtarget_Object((1,3,6,1,4,1,12394,1,1,2,17,2,1,4),_BrzaccVLThresholdLEDtarget_Type())
brzaccVLThresholdLEDtarget.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLThresholdLEDtarget.setStatus(_A)
_BrzaccVLNwMngParameters_ObjectIdentity=ObjectIdentity
brzaccVLNwMngParameters=_BrzaccVLNwMngParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,3))
class _BrzaccVLAccessToNwMng_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_AB,1),(_AC,2),(_AD,3),(_F,255)))
_BrzaccVLAccessToNwMng_Type.__name__=_C
_BrzaccVLAccessToNwMng_Object=MibScalar
brzaccVLAccessToNwMng=_BrzaccVLAccessToNwMng_Object((1,3,6,1,4,1,12394,1,1,3,1),_BrzaccVLAccessToNwMng_Type())
brzaccVLAccessToNwMng.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAccessToNwMng.setStatus(_A)
class _BrzaccVLNwMngFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_G,1),('activateOnEthernetPort',2),('activateOnWirelessPort',3),('activateOnBothWirelessAndEthernet',4),(_F,255)))
_BrzaccVLNwMngFilter_Type.__name__=_C
_BrzaccVLNwMngFilter_Object=MibScalar
brzaccVLNwMngFilter=_BrzaccVLNwMngFilter_Object((1,3,6,1,4,1,12394,1,1,3,2),_BrzaccVLNwMngFilter_Type())
brzaccVLNwMngFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNwMngFilter.setStatus(_A)
_MngIpFilterTable_Object=MibTable
mngIpFilterTable=_MngIpFilterTable_Object((1,3,6,1,4,1,12394,1,1,3,3))
if mibBuilder.loadTexts:mngIpFilterTable.setStatus(_A)
_MngIpFilterEntry_Object=MibTableRow
mngIpFilterEntry=_MngIpFilterEntry_Object((1,3,6,1,4,1,12394,1,1,3,3,1))
mngIpFilterEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:mngIpFilterEntry.setStatus(_A)
_BrzaccVLNwMngIpAddress_Type=IpAddress
_BrzaccVLNwMngIpAddress_Object=MibTableColumn
brzaccVLNwMngIpAddress=_BrzaccVLNwMngIpAddress_Object((1,3,6,1,4,1,12394,1,1,3,3,1,1),_BrzaccVLNwMngIpAddress_Type())
brzaccVLNwMngIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNwMngIpAddress.setStatus(_A)
class _BrzaccVLNwMngIpTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BrzaccVLNwMngIpTableIdx_Type.__name__=_C
_BrzaccVLNwMngIpTableIdx_Object=MibTableColumn
brzaccVLNwMngIpTableIdx=_BrzaccVLNwMngIpTableIdx_Object((1,3,6,1,4,1,12394,1,1,3,3,1,2),_BrzaccVLNwMngIpTableIdx_Type())
brzaccVLNwMngIpTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNwMngIpTableIdx.setStatus(_A)
class _BrzaccVLDeleteOneNwIpAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,10),ValueRangeConstraint(255,255))
_BrzaccVLDeleteOneNwIpAddr_Type.__name__=_C
_BrzaccVLDeleteOneNwIpAddr_Object=MibScalar
brzaccVLDeleteOneNwIpAddr=_BrzaccVLDeleteOneNwIpAddr_Object((1,3,6,1,4,1,12394,1,1,3,4),_BrzaccVLDeleteOneNwIpAddr_Type())
brzaccVLDeleteOneNwIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteOneNwIpAddr.setStatus(_A)
class _BrzaccVLDeleteAllNwIpAddrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_c,1),(_L,2),(_F,255)))
_BrzaccVLDeleteAllNwIpAddrs_Type.__name__=_C
_BrzaccVLDeleteAllNwIpAddrs_Object=MibScalar
brzaccVLDeleteAllNwIpAddrs=_BrzaccVLDeleteAllNwIpAddrs_Object((1,3,6,1,4,1,12394,1,1,3,5),_BrzaccVLDeleteAllNwIpAddrs_Type())
brzaccVLDeleteAllNwIpAddrs.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteAllNwIpAddrs.setStatus(_A)
class _BrzaccVLAccessToNwTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BrzaccVLAccessToNwTrap_Type.__name__=_C
_BrzaccVLAccessToNwTrap_Object=MibScalar
brzaccVLAccessToNwTrap=_BrzaccVLAccessToNwTrap_Object((1,3,6,1,4,1,12394,1,1,3,6),_BrzaccVLAccessToNwTrap_Type())
brzaccVLAccessToNwTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAccessToNwTrap.setStatus(_A)
_MngTrapTable_Object=MibTable
mngTrapTable=_MngTrapTable_Object((1,3,6,1,4,1,12394,1,1,3,7))
if mibBuilder.loadTexts:mngTrapTable.setStatus(_A)
_MngTrapEntry_Object=MibTableRow
mngTrapEntry=_MngTrapEntry_Object((1,3,6,1,4,1,12394,1,1,3,7,1))
mngTrapEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:mngTrapEntry.setStatus(_A)
class _BrzaccVLNwMngTrapCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_BrzaccVLNwMngTrapCommunity_Type.__name__=_I
_BrzaccVLNwMngTrapCommunity_Object=MibTableColumn
brzaccVLNwMngTrapCommunity=_BrzaccVLNwMngTrapCommunity_Object((1,3,6,1,4,1,12394,1,1,3,7,1,1),_BrzaccVLNwMngTrapCommunity_Type())
brzaccVLNwMngTrapCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNwMngTrapCommunity.setStatus(_A)
_BrzaccVLNwMngTrapAddress_Type=IpAddress
_BrzaccVLNwMngTrapAddress_Object=MibTableColumn
brzaccVLNwMngTrapAddress=_BrzaccVLNwMngTrapAddress_Object((1,3,6,1,4,1,12394,1,1,3,7,1,2),_BrzaccVLNwMngTrapAddress_Type())
brzaccVLNwMngTrapAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNwMngTrapAddress.setStatus(_A)
class _BrzaccVLNwTrapTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BrzaccVLNwTrapTableIdx_Type.__name__=_C
_BrzaccVLNwTrapTableIdx_Object=MibTableColumn
brzaccVLNwTrapTableIdx=_BrzaccVLNwTrapTableIdx_Object((1,3,6,1,4,1,12394,1,1,3,7,1,3),_BrzaccVLNwTrapTableIdx_Type())
brzaccVLNwTrapTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNwTrapTableIdx.setStatus(_A)
class _BrzaccVLDeleteOneTrapAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,10),ValueRangeConstraint(255,255))
_BrzaccVLDeleteOneTrapAddr_Type.__name__=_C
_BrzaccVLDeleteOneTrapAddr_Object=MibScalar
brzaccVLDeleteOneTrapAddr=_BrzaccVLDeleteOneTrapAddr_Object((1,3,6,1,4,1,12394,1,1,3,8),_BrzaccVLDeleteOneTrapAddr_Type())
brzaccVLDeleteOneTrapAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteOneTrapAddr.setStatus(_A)
class _BrzaccVLDeleteAllTrapAddrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_c,1),(_L,2),(_F,255)))
_BrzaccVLDeleteAllTrapAddrs_Type.__name__=_C
_BrzaccVLDeleteAllTrapAddrs_Object=MibScalar
brzaccVLDeleteAllTrapAddrs=_BrzaccVLDeleteAllTrapAddrs_Object((1,3,6,1,4,1,12394,1,1,3,9),_BrzaccVLDeleteAllTrapAddrs_Type())
brzaccVLDeleteAllTrapAddrs.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteAllTrapAddrs.setStatus(_A)
_BrzaccVLMngIpRangesTable_Object=MibTable
brzaccVLMngIpRangesTable=_BrzaccVLMngIpRangesTable_Object((1,3,6,1,4,1,12394,1,1,3,10))
if mibBuilder.loadTexts:brzaccVLMngIpRangesTable.setStatus(_A)
_BrzaccVLMngIpRangeEntry_Object=MibTableRow
brzaccVLMngIpRangeEntry=_BrzaccVLMngIpRangeEntry_Object((1,3,6,1,4,1,12394,1,1,3,10,1))
brzaccVLMngIpRangeEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:brzaccVLMngIpRangeEntry.setStatus(_A)
class _BrzaccVLMngIpRangeIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BrzaccVLMngIpRangeIdx_Type.__name__=_C
_BrzaccVLMngIpRangeIdx_Object=MibTableColumn
brzaccVLMngIpRangeIdx=_BrzaccVLMngIpRangeIdx_Object((1,3,6,1,4,1,12394,1,1,3,10,1,1),_BrzaccVLMngIpRangeIdx_Type())
brzaccVLMngIpRangeIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMngIpRangeIdx.setStatus(_A)
class _BrzaccVLMngIpRangeFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AH,1),(_AI,2)))
_BrzaccVLMngIpRangeFlag_Type.__name__=_C
_BrzaccVLMngIpRangeFlag_Object=MibTableColumn
brzaccVLMngIpRangeFlag=_BrzaccVLMngIpRangeFlag_Object((1,3,6,1,4,1,12394,1,1,3,10,1,2),_BrzaccVLMngIpRangeFlag_Type())
brzaccVLMngIpRangeFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMngIpRangeFlag.setStatus(_A)
_BrzaccVLMngIpRangeStart_Type=IpAddress
_BrzaccVLMngIpRangeStart_Object=MibTableColumn
brzaccVLMngIpRangeStart=_BrzaccVLMngIpRangeStart_Object((1,3,6,1,4,1,12394,1,1,3,10,1,3),_BrzaccVLMngIpRangeStart_Type())
brzaccVLMngIpRangeStart.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMngIpRangeStart.setStatus(_A)
_BrzaccVLMngIpRangeEnd_Type=IpAddress
_BrzaccVLMngIpRangeEnd_Object=MibTableColumn
brzaccVLMngIpRangeEnd=_BrzaccVLMngIpRangeEnd_Object((1,3,6,1,4,1,12394,1,1,3,10,1,4),_BrzaccVLMngIpRangeEnd_Type())
brzaccVLMngIpRangeEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMngIpRangeEnd.setStatus(_A)
_BrzaccVLMngIpRangeMask_Type=IpAddress
_BrzaccVLMngIpRangeMask_Object=MibTableColumn
brzaccVLMngIpRangeMask=_BrzaccVLMngIpRangeMask_Object((1,3,6,1,4,1,12394,1,1,3,10,1,5),_BrzaccVLMngIpRangeMask_Type())
brzaccVLMngIpRangeMask.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMngIpRangeMask.setStatus(_A)
class _BrzaccVLDeleteOneNwIpRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,10),ValueRangeConstraint(255,255))
_BrzaccVLDeleteOneNwIpRange_Type.__name__=_C
_BrzaccVLDeleteOneNwIpRange_Object=MibScalar
brzaccVLDeleteOneNwIpRange=_BrzaccVLDeleteOneNwIpRange_Object((1,3,6,1,4,1,12394,1,1,3,11),_BrzaccVLDeleteOneNwIpRange_Type())
brzaccVLDeleteOneNwIpRange.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteOneNwIpRange.setStatus(_A)
class _BrzaccVLDeleteAllNwIpRanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_c,1),(_L,2),(_F,255)))
_BrzaccVLDeleteAllNwIpRanges_Type.__name__=_C
_BrzaccVLDeleteAllNwIpRanges_Object=MibScalar
brzaccVLDeleteAllNwIpRanges=_BrzaccVLDeleteAllNwIpRanges_Object((1,3,6,1,4,1,12394,1,1,3,12),_BrzaccVLDeleteAllNwIpRanges_Type())
brzaccVLDeleteAllNwIpRanges.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteAllNwIpRanges.setStatus(_A)
_BrzaccVLWi2IpAddress_Type=IpAddress
_BrzaccVLWi2IpAddress_Object=MibScalar
brzaccVLWi2IpAddress=_BrzaccVLWi2IpAddress_Object((1,3,6,1,4,1,12394,1,1,3,13),_BrzaccVLWi2IpAddress_Type())
brzaccVLWi2IpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLWi2IpAddress.setStatus(_A)
_BrzaccVLNewNMngSystem_ObjectIdentity=ObjectIdentity
brzaccVLNewNMngSystem=_BrzaccVLNewNMngSystem_ObjectIdentity((1,3,6,1,4,1,12394,1,1,3,14))
_BrzaccVLErrorHandling_ObjectIdentity=ObjectIdentity
brzaccVLErrorHandling=_BrzaccVLErrorHandling_ObjectIdentity((1,3,6,1,4,1,12394,1,1,3,14,1))
_BrzaccVLErrHandlingSetNMSId_Type=Integer32
_BrzaccVLErrHandlingSetNMSId_Object=MibScalar
brzaccVLErrHandlingSetNMSId=_BrzaccVLErrHandlingSetNMSId_Object((1,3,6,1,4,1,12394,1,1,3,14,1,1),_BrzaccVLErrHandlingSetNMSId_Type())
brzaccVLErrHandlingSetNMSId.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLErrHandlingSetNMSId.setStatus(_A)
_BrzaccVLErrHandlingTable_Object=MibTable
brzaccVLErrHandlingTable=_BrzaccVLErrHandlingTable_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2))
if mibBuilder.loadTexts:brzaccVLErrHandlingTable.setStatus(_A)
_BrzaccVLErrHandlingEntry_Object=MibTableRow
brzaccVLErrHandlingEntry=_BrzaccVLErrHandlingEntry_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1))
brzaccVLErrHandlingEntry.setIndexNames((0,_E,_AJ),(0,_E,_AK))
if mibBuilder.loadTexts:brzaccVLErrHandlingEntry.setStatus(_A)
class _BrzaccVLErrHandlingNMSId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_BrzaccVLErrHandlingNMSId_Type.__name__=_t
_BrzaccVLErrHandlingNMSId_Object=MibTableColumn
brzaccVLErrHandlingNMSId=_BrzaccVLErrHandlingNMSId_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,1),_BrzaccVLErrHandlingNMSId_Type())
brzaccVLErrHandlingNMSId.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingNMSId.setStatus(_A)
class _BrzaccVLErrHandlingRequestId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_BrzaccVLErrHandlingRequestId_Type.__name__=_t
_BrzaccVLErrHandlingRequestId_Object=MibTableColumn
brzaccVLErrHandlingRequestId=_BrzaccVLErrHandlingRequestId_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,2),_BrzaccVLErrHandlingRequestId_Type())
brzaccVLErrHandlingRequestId.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingRequestId.setStatus(_A)
_BrzaccVLErrHandlingErrorCode_Type=Integer32
_BrzaccVLErrHandlingErrorCode_Object=MibTableColumn
brzaccVLErrHandlingErrorCode=_BrzaccVLErrHandlingErrorCode_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,3),_BrzaccVLErrHandlingErrorCode_Type())
brzaccVLErrHandlingErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingErrorCode.setStatus(_A)
_BrzaccVLErrHandlingParameter1_Type=Integer32
_BrzaccVLErrHandlingParameter1_Object=MibTableColumn
brzaccVLErrHandlingParameter1=_BrzaccVLErrHandlingParameter1_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,4),_BrzaccVLErrHandlingParameter1_Type())
brzaccVLErrHandlingParameter1.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingParameter1.setStatus(_A)
_BrzaccVLErrHandlingParameter2_Type=Integer32
_BrzaccVLErrHandlingParameter2_Object=MibTableColumn
brzaccVLErrHandlingParameter2=_BrzaccVLErrHandlingParameter2_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,5),_BrzaccVLErrHandlingParameter2_Type())
brzaccVLErrHandlingParameter2.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingParameter2.setStatus(_A)
_BrzaccVLErrHandlingParameter3_Type=Integer32
_BrzaccVLErrHandlingParameter3_Object=MibTableColumn
brzaccVLErrHandlingParameter3=_BrzaccVLErrHandlingParameter3_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,6),_BrzaccVLErrHandlingParameter3_Type())
brzaccVLErrHandlingParameter3.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingParameter3.setStatus(_A)
_BrzaccVLErrHandlingParameter4_Type=Integer32
_BrzaccVLErrHandlingParameter4_Object=MibTableColumn
brzaccVLErrHandlingParameter4=_BrzaccVLErrHandlingParameter4_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,7),_BrzaccVLErrHandlingParameter4_Type())
brzaccVLErrHandlingParameter4.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingParameter4.setStatus(_A)
_BrzaccVLErrHandlingParameter5_Type=Integer32
_BrzaccVLErrHandlingParameter5_Object=MibTableColumn
brzaccVLErrHandlingParameter5=_BrzaccVLErrHandlingParameter5_Object((1,3,6,1,4,1,12394,1,1,3,14,1,2,1,8),_BrzaccVLErrHandlingParameter5_Type())
brzaccVLErrHandlingParameter5.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLErrHandlingParameter5.setStatus(_A)
_BrzaccVLTrapHistory_ObjectIdentity=ObjectIdentity
brzaccVLTrapHistory=_BrzaccVLTrapHistory_ObjectIdentity((1,3,6,1,4,1,12394,1,1,3,14,2))
_BrzaccVLLastTrapSequenceNumber_Type=Integer32
_BrzaccVLLastTrapSequenceNumber_Object=MibScalar
brzaccVLLastTrapSequenceNumber=_BrzaccVLLastTrapSequenceNumber_Object((1,3,6,1,4,1,12394,1,1,3,14,2,1),_BrzaccVLLastTrapSequenceNumber_Type())
brzaccVLLastTrapSequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLLastTrapSequenceNumber.setStatus(_A)
_BrzaccVLTrapHistoryTable_Object=MibTable
brzaccVLTrapHistoryTable=_BrzaccVLTrapHistoryTable_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2))
if mibBuilder.loadTexts:brzaccVLTrapHistoryTable.setStatus(_A)
_BrzaccVLTrapHistoryEntry_Object=MibTableRow
brzaccVLTrapHistoryEntry=_BrzaccVLTrapHistoryEntry_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1))
brzaccVLTrapHistoryEntry.setIndexNames((0,_E,_AL))
if mibBuilder.loadTexts:brzaccVLTrapHistoryEntry.setStatus(_A)
class _BrzaccVLTrapHistorySequenceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrzaccVLTrapHistorySequenceNumber_Type.__name__=_C
_BrzaccVLTrapHistorySequenceNumber_Object=MibTableColumn
brzaccVLTrapHistorySequenceNumber=_BrzaccVLTrapHistorySequenceNumber_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1,1),_BrzaccVLTrapHistorySequenceNumber_Type())
brzaccVLTrapHistorySequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapHistorySequenceNumber.setStatus(_A)
_BrzaccVLTrapType_Type=Integer32
_BrzaccVLTrapType_Object=MibTableColumn
brzaccVLTrapType=_BrzaccVLTrapType_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1,2),_BrzaccVLTrapType_Type())
brzaccVLTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapType.setStatus(_A)
_BrzaccVLTrapMacAddrParam_Type=MacAddress
_BrzaccVLTrapMacAddrParam_Object=MibTableColumn
brzaccVLTrapMacAddrParam=_BrzaccVLTrapMacAddrParam_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1,3),_BrzaccVLTrapMacAddrParam_Type())
brzaccVLTrapMacAddrParam.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapMacAddrParam.setStatus(_A)
_BrzaccVLTrapIntParam1_Type=Integer32
_BrzaccVLTrapIntParam1_Object=MibTableColumn
brzaccVLTrapIntParam1=_BrzaccVLTrapIntParam1_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1,4),_BrzaccVLTrapIntParam1_Type())
brzaccVLTrapIntParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapIntParam1.setStatus(_A)
_BrzaccVLTrapIntParam2_Type=Integer32
_BrzaccVLTrapIntParam2_Object=MibTableColumn
brzaccVLTrapIntParam2=_BrzaccVLTrapIntParam2_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1,5),_BrzaccVLTrapIntParam2_Type())
brzaccVLTrapIntParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapIntParam2.setStatus(_A)
_BrzaccVLTrapIntParam3_Type=Integer32
_BrzaccVLTrapIntParam3_Object=MibTableColumn
brzaccVLTrapIntParam3=_BrzaccVLTrapIntParam3_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1,6),_BrzaccVLTrapIntParam3_Type())
brzaccVLTrapIntParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapIntParam3.setStatus(_A)
_BrzaccVLTrapStrParam_Type=DisplayString
_BrzaccVLTrapStrParam_Object=MibTableColumn
brzaccVLTrapStrParam=_BrzaccVLTrapStrParam_Object((1,3,6,1,4,1,12394,1,1,3,14,2,2,1,7),_BrzaccVLTrapStrParam_Type())
brzaccVLTrapStrParam.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapStrParam.setStatus(_A)
_NewMngIpFilterTable_Object=MibTable
newMngIpFilterTable=_NewMngIpFilterTable_Object((1,3,6,1,4,1,12394,1,1,3,15))
if mibBuilder.loadTexts:newMngIpFilterTable.setStatus(_A)
_NewMngIpFilterEntry_Object=MibTableRow
newMngIpFilterEntry=_NewMngIpFilterEntry_Object((1,3,6,1,4,1,12394,1,1,3,15,1))
newMngIpFilterEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:newMngIpFilterEntry.setStatus(_A)
_BrzaccVLNewNwMngIpAddress_Type=IpAddress
_BrzaccVLNewNwMngIpAddress_Object=MibTableColumn
brzaccVLNewNwMngIpAddress=_BrzaccVLNewNwMngIpAddress_Object((1,3,6,1,4,1,12394,1,1,3,15,1,1),_BrzaccVLNewNwMngIpAddress_Type())
brzaccVLNewNwMngIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewNwMngIpAddress.setStatus(_A)
class _BrzaccVLNewNwMngIpAddressCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_BrzaccVLNewNwMngIpAddressCommand_Type.__name__=_C
_BrzaccVLNewNwMngIpAddressCommand_Object=MibTableColumn
brzaccVLNewNwMngIpAddressCommand=_BrzaccVLNewNwMngIpAddressCommand_Object((1,3,6,1,4,1,12394,1,1,3,15,1,2),_BrzaccVLNewNwMngIpAddressCommand_Type())
brzaccVLNewNwMngIpAddressCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewNwMngIpAddressCommand.setStatus(_A)
_NewMngTrapTable_Object=MibTable
newMngTrapTable=_NewMngTrapTable_Object((1,3,6,1,4,1,12394,1,1,3,16))
if mibBuilder.loadTexts:newMngTrapTable.setStatus(_A)
_NewMngTrapEntry_Object=MibTableRow
newMngTrapEntry=_NewMngTrapEntry_Object((1,3,6,1,4,1,12394,1,1,3,16,1))
newMngTrapEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:newMngTrapEntry.setStatus(_A)
class _BrzaccVLNewNwMngTrapCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_BrzaccVLNewNwMngTrapCommunity_Type.__name__=_I
_BrzaccVLNewNwMngTrapCommunity_Object=MibTableColumn
brzaccVLNewNwMngTrapCommunity=_BrzaccVLNewNwMngTrapCommunity_Object((1,3,6,1,4,1,12394,1,1,3,16,1,1),_BrzaccVLNewNwMngTrapCommunity_Type())
brzaccVLNewNwMngTrapCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewNwMngTrapCommunity.setStatus(_A)
_BrzaccVLNewNwMngTrapAddress_Type=IpAddress
_BrzaccVLNewNwMngTrapAddress_Object=MibTableColumn
brzaccVLNewNwMngTrapAddress=_BrzaccVLNewNwMngTrapAddress_Object((1,3,6,1,4,1,12394,1,1,3,16,1,2),_BrzaccVLNewNwMngTrapAddress_Type())
brzaccVLNewNwMngTrapAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewNwMngTrapAddress.setStatus(_A)
class _BrzaccVLNewNwTrapCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_BrzaccVLNewNwTrapCommand_Type.__name__=_C
_BrzaccVLNewNwTrapCommand_Object=MibTableColumn
brzaccVLNewNwTrapCommand=_BrzaccVLNewNwTrapCommand_Object((1,3,6,1,4,1,12394,1,1,3,16,1,3),_BrzaccVLNewNwTrapCommand_Type())
brzaccVLNewNwTrapCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewNwTrapCommand.setStatus(_A)
_BrzaccVLNewMngIpRangesTable_Object=MibTable
brzaccVLNewMngIpRangesTable=_BrzaccVLNewMngIpRangesTable_Object((1,3,6,1,4,1,12394,1,1,3,17))
if mibBuilder.loadTexts:brzaccVLNewMngIpRangesTable.setStatus(_A)
_BrzaccVLNewMngIpRangeEntry_Object=MibTableRow
brzaccVLNewMngIpRangeEntry=_BrzaccVLNewMngIpRangeEntry_Object((1,3,6,1,4,1,12394,1,1,3,17,1))
brzaccVLNewMngIpRangeEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:brzaccVLNewMngIpRangeEntry.setStatus(_A)
_BrzaccVLNewMngIpRangeStart_Type=IpAddress
_BrzaccVLNewMngIpRangeStart_Object=MibTableColumn
brzaccVLNewMngIpRangeStart=_BrzaccVLNewMngIpRangeStart_Object((1,3,6,1,4,1,12394,1,1,3,17,1,1),_BrzaccVLNewMngIpRangeStart_Type())
brzaccVLNewMngIpRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewMngIpRangeStart.setStatus(_A)
_BrzaccVLNewMngIpRangeEnd_Type=IpAddress
_BrzaccVLNewMngIpRangeEnd_Object=MibTableColumn
brzaccVLNewMngIpRangeEnd=_BrzaccVLNewMngIpRangeEnd_Object((1,3,6,1,4,1,12394,1,1,3,17,1,2),_BrzaccVLNewMngIpRangeEnd_Type())
brzaccVLNewMngIpRangeEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewMngIpRangeEnd.setStatus(_A)
_BrzaccVLNewMngIpRangeMask_Type=IpAddress
_BrzaccVLNewMngIpRangeMask_Object=MibTableColumn
brzaccVLNewMngIpRangeMask=_BrzaccVLNewMngIpRangeMask_Object((1,3,6,1,4,1,12394,1,1,3,17,1,3),_BrzaccVLNewMngIpRangeMask_Type())
brzaccVLNewMngIpRangeMask.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewMngIpRangeMask.setStatus(_A)
class _BrzaccVLNewMngIpRangeFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AH,1),(_AI,2)))
_BrzaccVLNewMngIpRangeFlag_Type.__name__=_C
_BrzaccVLNewMngIpRangeFlag_Object=MibTableColumn
brzaccVLNewMngIpRangeFlag=_BrzaccVLNewMngIpRangeFlag_Object((1,3,6,1,4,1,12394,1,1,3,17,1,4),_BrzaccVLNewMngIpRangeFlag_Type())
brzaccVLNewMngIpRangeFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewMngIpRangeFlag.setStatus(_A)
class _BrzaccVLNewMngIpRangeCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_BrzaccVLNewMngIpRangeCommand_Type.__name__=_C
_BrzaccVLNewMngIpRangeCommand_Object=MibTableColumn
brzaccVLNewMngIpRangeCommand=_BrzaccVLNewMngIpRangeCommand_Object((1,3,6,1,4,1,12394,1,1,3,17,1,5),_BrzaccVLNewMngIpRangeCommand_Type())
brzaccVLNewMngIpRangeCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewMngIpRangeCommand.setStatus(_A)
_BrzaccVLIpParams_ObjectIdentity=ObjectIdentity
brzaccVLIpParams=_BrzaccVLIpParams_ObjectIdentity((1,3,6,1,4,1,12394,1,1,4))
_BrzaccVLUnitIpAddress_Type=IpAddress
_BrzaccVLUnitIpAddress_Object=MibScalar
brzaccVLUnitIpAddress=_BrzaccVLUnitIpAddress_Object((1,3,6,1,4,1,12394,1,1,4,1),_BrzaccVLUnitIpAddress_Type())
brzaccVLUnitIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUnitIpAddress.setStatus(_A)
_BrzaccVLSubNetMask_Type=IpAddress
_BrzaccVLSubNetMask_Object=MibScalar
brzaccVLSubNetMask=_BrzaccVLSubNetMask_Object((1,3,6,1,4,1,12394,1,1,4,2),_BrzaccVLSubNetMask_Type())
brzaccVLSubNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSubNetMask.setStatus(_A)
_BrzaccVLDefaultGWAddress_Type=IpAddress
_BrzaccVLDefaultGWAddress_Object=MibScalar
brzaccVLDefaultGWAddress=_BrzaccVLDefaultGWAddress_Object((1,3,6,1,4,1,12394,1,1,4,3),_BrzaccVLDefaultGWAddress_Type())
brzaccVLDefaultGWAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDefaultGWAddress.setStatus(_A)
class _BrzaccVLUseDhcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('dhcpOnly',2),(_n,3)))
_BrzaccVLUseDhcp_Type.__name__=_C
_BrzaccVLUseDhcp_Object=MibScalar
brzaccVLUseDhcp=_BrzaccVLUseDhcp_Object((1,3,6,1,4,1,12394,1,1,4,4),_BrzaccVLUseDhcp_Type())
brzaccVLUseDhcp.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUseDhcp.setStatus(_A)
class _BrzaccVLAccessToDHCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AB,1),(_AC,2),(_AD,3)))
_BrzaccVLAccessToDHCP_Type.__name__=_C
_BrzaccVLAccessToDHCP_Object=MibScalar
brzaccVLAccessToDHCP=_BrzaccVLAccessToDHCP_Object((1,3,6,1,4,1,12394,1,1,4,5),_BrzaccVLAccessToDHCP_Type())
brzaccVLAccessToDHCP.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAccessToDHCP.setStatus(_A)
_BrzaccVLRunTimeIPaddr_Type=IpAddress
_BrzaccVLRunTimeIPaddr_Object=MibScalar
brzaccVLRunTimeIPaddr=_BrzaccVLRunTimeIPaddr_Object((1,3,6,1,4,1,12394,1,1,4,6),_BrzaccVLRunTimeIPaddr_Type())
brzaccVLRunTimeIPaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRunTimeIPaddr.setStatus(_A)
_BrzaccVLRunTimeSubNetMask_Type=IpAddress
_BrzaccVLRunTimeSubNetMask_Object=MibScalar
brzaccVLRunTimeSubNetMask=_BrzaccVLRunTimeSubNetMask_Object((1,3,6,1,4,1,12394,1,1,4,7),_BrzaccVLRunTimeSubNetMask_Type())
brzaccVLRunTimeSubNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRunTimeSubNetMask.setStatus(_A)
_BrzaccVLRunTimeDefaultIPGateway_Type=IpAddress
_BrzaccVLRunTimeDefaultIPGateway_Object=MibScalar
brzaccVLRunTimeDefaultIPGateway=_BrzaccVLRunTimeDefaultIPGateway_Object((1,3,6,1,4,1,12394,1,1,4,8),_BrzaccVLRunTimeDefaultIPGateway_Type())
brzaccVLRunTimeDefaultIPGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRunTimeDefaultIPGateway.setStatus(_A)
_BrzaccVLBridgeParameters_ObjectIdentity=ObjectIdentity
brzaccVLBridgeParameters=_BrzaccVLBridgeParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5))
_BrzaccVLVLANSupport_ObjectIdentity=ObjectIdentity
brzaccVLVLANSupport=_BrzaccVLVLANSupport_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,1))
_BrzaccVLVlanID_Type=Integer32
_BrzaccVLVlanID_Object=MibScalar
brzaccVLVlanID=_BrzaccVLVlanID_Object((1,3,6,1,4,1,12394,1,1,5,1,1),_BrzaccVLVlanID_Type())
brzaccVLVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanID.setStatus(_A)
class _BrzaccVLEthernetLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('accessLink',1),('trunkLink',2),('hybridLink',3),('serviceProviderLink',4),('extAccessLink',5),('extTrunkLink',6)))
_BrzaccVLEthernetLinkType_Type.__name__=_C
_BrzaccVLEthernetLinkType_Object=MibScalar
brzaccVLEthernetLinkType=_BrzaccVLEthernetLinkType_Object((1,3,6,1,4,1,12394,1,1,5,1,2),_BrzaccVLEthernetLinkType_Type())
brzaccVLEthernetLinkType.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthernetLinkType.setStatus(_A)
_BrzaccVLManagementVlanID_Type=Integer32
_BrzaccVLManagementVlanID_Object=MibScalar
brzaccVLManagementVlanID=_BrzaccVLManagementVlanID_Object((1,3,6,1,4,1,12394,1,1,5,1,3),_BrzaccVLManagementVlanID_Type())
brzaccVLManagementVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLManagementVlanID.setStatus(_A)
_BrzaccVLVLANForwarding_ObjectIdentity=ObjectIdentity
brzaccVLVLANForwarding=_BrzaccVLVLANForwarding_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,1,4))
class _BrzaccVLVlanForwardingSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLVlanForwardingSupport_Type.__name__=_C
_BrzaccVLVlanForwardingSupport_Object=MibScalar
brzaccVLVlanForwardingSupport=_BrzaccVLVlanForwardingSupport_Object((1,3,6,1,4,1,12394,1,1,5,1,4,1),_BrzaccVLVlanForwardingSupport_Type())
brzaccVLVlanForwardingSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanForwardingSupport.setStatus(_A)
_BrzaccVLVlanForwardingTable_Object=MibTable
brzaccVLVlanForwardingTable=_BrzaccVLVlanForwardingTable_Object((1,3,6,1,4,1,12394,1,1,5,1,4,2))
if mibBuilder.loadTexts:brzaccVLVlanForwardingTable.setStatus(_A)
_BrzaccVLVlanForwardingEntry_Object=MibTableRow
brzaccVLVlanForwardingEntry=_BrzaccVLVlanForwardingEntry_Object((1,3,6,1,4,1,12394,1,1,5,1,4,2,1))
brzaccVLVlanForwardingEntry.setIndexNames((0,_E,_AP))
if mibBuilder.loadTexts:brzaccVLVlanForwardingEntry.setStatus(_A)
class _BrzaccVLVlanForwardingTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_BrzaccVLVlanForwardingTableIdx_Type.__name__=_C
_BrzaccVLVlanForwardingTableIdx_Object=MibTableColumn
brzaccVLVlanForwardingTableIdx=_BrzaccVLVlanForwardingTableIdx_Object((1,3,6,1,4,1,12394,1,1,5,1,4,2,1,1),_BrzaccVLVlanForwardingTableIdx_Type())
brzaccVLVlanForwardingTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLVlanForwardingTableIdx.setStatus(_A)
_BrzaccVLVlanIdForwarding_Type=Integer32
_BrzaccVLVlanIdForwarding_Object=MibTableColumn
brzaccVLVlanIdForwarding=_BrzaccVLVlanIdForwarding_Object((1,3,6,1,4,1,12394,1,1,5,1,4,2,1,2),_BrzaccVLVlanIdForwarding_Type())
brzaccVLVlanIdForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanIdForwarding.setStatus(_A)
_BrzaccVLNewVlanForwardingTable_Object=MibTable
brzaccVLNewVlanForwardingTable=_BrzaccVLNewVlanForwardingTable_Object((1,3,6,1,4,1,12394,1,1,5,1,4,3))
if mibBuilder.loadTexts:brzaccVLNewVlanForwardingTable.setStatus(_A)
_BrzaccVLNewVlanForwardingEntry_Object=MibTableRow
brzaccVLNewVlanForwardingEntry=_BrzaccVLNewVlanForwardingEntry_Object((1,3,6,1,4,1,12394,1,1,5,1,4,3,1))
brzaccVLNewVlanForwardingEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:brzaccVLNewVlanForwardingEntry.setStatus(_A)
class _BrzaccVLNewVlanIdForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BrzaccVLNewVlanIdForwarding_Type.__name__=_C
_BrzaccVLNewVlanIdForwarding_Object=MibTableColumn
brzaccVLNewVlanIdForwarding=_BrzaccVLNewVlanIdForwarding_Object((1,3,6,1,4,1,12394,1,1,5,1,4,3,1,1),_BrzaccVLNewVlanIdForwarding_Type())
brzaccVLNewVlanIdForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewVlanIdForwarding.setStatus(_A)
class _BrzaccVLNewVlanForwardingCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_BrzaccVLNewVlanForwardingCommand_Type.__name__=_C
_BrzaccVLNewVlanForwardingCommand_Object=MibTableColumn
brzaccVLNewVlanForwardingCommand=_BrzaccVLNewVlanForwardingCommand_Object((1,3,6,1,4,1,12394,1,1,5,1,4,3,1,2),_BrzaccVLNewVlanForwardingCommand_Type())
brzaccVLNewVlanForwardingCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewVlanForwardingCommand.setStatus(_A)
_BrzaccVLVlanRelaying_ObjectIdentity=ObjectIdentity
brzaccVLVlanRelaying=_BrzaccVLVlanRelaying_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,1,5))
class _BrzaccVLVlanRelayingSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLVlanRelayingSupport_Type.__name__=_C
_BrzaccVLVlanRelayingSupport_Object=MibScalar
brzaccVLVlanRelayingSupport=_BrzaccVLVlanRelayingSupport_Object((1,3,6,1,4,1,12394,1,1,5,1,5,1),_BrzaccVLVlanRelayingSupport_Type())
brzaccVLVlanRelayingSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanRelayingSupport.setStatus(_A)
_BrzaccVLVlanRelayingTable_Object=MibTable
brzaccVLVlanRelayingTable=_BrzaccVLVlanRelayingTable_Object((1,3,6,1,4,1,12394,1,1,5,1,5,2))
if mibBuilder.loadTexts:brzaccVLVlanRelayingTable.setStatus(_A)
_BrzaccVLVlanRelayingEntry_Object=MibTableRow
brzaccVLVlanRelayingEntry=_BrzaccVLVlanRelayingEntry_Object((1,3,6,1,4,1,12394,1,1,5,1,5,2,1))
brzaccVLVlanRelayingEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:brzaccVLVlanRelayingEntry.setStatus(_A)
class _BrzaccVLVlanRelayingTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_BrzaccVLVlanRelayingTableIdx_Type.__name__=_C
_BrzaccVLVlanRelayingTableIdx_Object=MibTableColumn
brzaccVLVlanRelayingTableIdx=_BrzaccVLVlanRelayingTableIdx_Object((1,3,6,1,4,1,12394,1,1,5,1,5,2,1,1),_BrzaccVLVlanRelayingTableIdx_Type())
brzaccVLVlanRelayingTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLVlanRelayingTableIdx.setStatus(_A)
_BrzaccVLVlanIdRelaying_Type=Integer32
_BrzaccVLVlanIdRelaying_Object=MibTableColumn
brzaccVLVlanIdRelaying=_BrzaccVLVlanIdRelaying_Object((1,3,6,1,4,1,12394,1,1,5,1,5,2,1,2),_BrzaccVLVlanIdRelaying_Type())
brzaccVLVlanIdRelaying.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanIdRelaying.setStatus(_A)
_BrzaccVLNewVlanRelayingTable_Object=MibTable
brzaccVLNewVlanRelayingTable=_BrzaccVLNewVlanRelayingTable_Object((1,3,6,1,4,1,12394,1,1,5,1,5,3))
if mibBuilder.loadTexts:brzaccVLNewVlanRelayingTable.setStatus(_A)
_BrzaccVLNewVlanRelayingEntry_Object=MibTableRow
brzaccVLNewVlanRelayingEntry=_BrzaccVLNewVlanRelayingEntry_Object((1,3,6,1,4,1,12394,1,1,5,1,5,3,1))
brzaccVLNewVlanRelayingEntry.setIndexNames((0,_E,_AS))
if mibBuilder.loadTexts:brzaccVLNewVlanRelayingEntry.setStatus(_A)
class _BrzaccVLNewVlanIdRelaying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BrzaccVLNewVlanIdRelaying_Type.__name__=_C
_BrzaccVLNewVlanIdRelaying_Object=MibTableColumn
brzaccVLNewVlanIdRelaying=_BrzaccVLNewVlanIdRelaying_Object((1,3,6,1,4,1,12394,1,1,5,1,5,3,1,1),_BrzaccVLNewVlanIdRelaying_Type())
brzaccVLNewVlanIdRelaying.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewVlanIdRelaying.setStatus(_A)
class _BrzaccVLNewVlanRelayingTableCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_BrzaccVLNewVlanRelayingTableCommand_Type.__name__=_C
_BrzaccVLNewVlanRelayingTableCommand_Object=MibTableColumn
brzaccVLNewVlanRelayingTableCommand=_BrzaccVLNewVlanRelayingTableCommand_Object((1,3,6,1,4,1,12394,1,1,5,1,5,3,1,2),_BrzaccVLNewVlanRelayingTableCommand_Type())
brzaccVLNewVlanRelayingTableCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewVlanRelayingTableCommand.setStatus(_A)
_BrzaccVLVLANTrafficPriority_ObjectIdentity=ObjectIdentity
brzaccVLVLANTrafficPriority=_BrzaccVLVLANTrafficPriority_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,1,6))
class _BrzaccVLVlanDataPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(255));namedValues=NamedValues((_F,255))
_BrzaccVLVlanDataPriority_Type.__name__=_C
_BrzaccVLVlanDataPriority_Object=MibScalar
brzaccVLVlanDataPriority=_BrzaccVLVlanDataPriority_Object((1,3,6,1,4,1,12394,1,1,5,1,6,1),_BrzaccVLVlanDataPriority_Type())
brzaccVLVlanDataPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanDataPriority.setStatus(_A)
class _BrzaccVLVlanManagementPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrzaccVLVlanManagementPriority_Type.__name__=_C
_BrzaccVLVlanManagementPriority_Object=MibScalar
brzaccVLVlanManagementPriority=_BrzaccVLVlanManagementPriority_Object((1,3,6,1,4,1,12394,1,1,5,1,6,2),_BrzaccVLVlanManagementPriority_Type())
brzaccVLVlanManagementPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanManagementPriority.setStatus(_A)
class _BrzaccVLVlanPriorityThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(255));namedValues=NamedValues((_F,255))
_BrzaccVLVlanPriorityThreshold_Type.__name__=_C
_BrzaccVLVlanPriorityThreshold_Object=MibScalar
brzaccVLVlanPriorityThreshold=_BrzaccVLVlanPriorityThreshold_Object((1,3,6,1,4,1,12394,1,1,5,1,6,3),_BrzaccVLVlanPriorityThreshold_Type())
brzaccVLVlanPriorityThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanPriorityThreshold.setStatus(_A)
_BrzaccVLVLANQinQ_ObjectIdentity=ObjectIdentity
brzaccVLVLANQinQ=_BrzaccVLVLANQinQ_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,1,7))
class _BrzaccVLQinQEthertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(33024,36864),ValueRangeConstraint(37120,37120),ValueRangeConstraint(37376,37376))
_BrzaccVLQinQEthertype_Type.__name__=_C
_BrzaccVLQinQEthertype_Object=MibScalar
brzaccVLQinQEthertype=_BrzaccVLQinQEthertype_Object((1,3,6,1,4,1,12394,1,1,5,1,7,1),_BrzaccVLQinQEthertype_Type())
brzaccVLQinQEthertype.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLQinQEthertype.setStatus(_A)
class _BrzaccVLQinQProviderVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BrzaccVLQinQProviderVlanID_Type.__name__=_C
_BrzaccVLQinQProviderVlanID_Object=MibScalar
brzaccVLQinQProviderVlanID=_BrzaccVLQinQProviderVlanID_Object((1,3,6,1,4,1,12394,1,1,5,1,7,2),_BrzaccVLQinQProviderVlanID_Type())
brzaccVLQinQProviderVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLQinQProviderVlanID.setStatus(_A)
_BrzaccVLVlanExtendedAccessRulesTable_Object=MibTable
brzaccVLVlanExtendedAccessRulesTable=_BrzaccVLVlanExtendedAccessRulesTable_Object((1,3,6,1,4,1,12394,1,1,5,1,8))
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRulesTable.setStatus(_A)
_BrzaccVLVlanExtendedAccessRulesEntry_Object=MibTableRow
brzaccVLVlanExtendedAccessRulesEntry=_BrzaccVLVlanExtendedAccessRulesEntry_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1))
brzaccVLVlanExtendedAccessRulesEntry.setIndexNames((0,_E,_AT))
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRulesEntry.setStatus(_A)
class _BrzaccVLVlanExtendedAccessRulesTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BrzaccVLVlanExtendedAccessRulesTableIdx_Type.__name__=_C
_BrzaccVLVlanExtendedAccessRulesTableIdx_Object=MibTableColumn
brzaccVLVlanExtendedAccessRulesTableIdx=_BrzaccVLVlanExtendedAccessRulesTableIdx_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1,1),_BrzaccVLVlanExtendedAccessRulesTableIdx_Type())
brzaccVLVlanExtendedAccessRulesTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRulesTableIdx.setStatus(_A)
class _BrzaccVLVlanExtendedAccessRuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('noRule',1),('sourceMacAddress',2),('destinationMacAddress',3),('sourceIpAddress',4),('destinationIpAddress',5),('sourceUdpPort',6),('destinationUdpPort',7),('sourceTcpPort',8),('destinationTcpPort',9),('ipProtocol',10),('default',11)))
_BrzaccVLVlanExtendedAccessRuleId_Type.__name__=_C
_BrzaccVLVlanExtendedAccessRuleId_Object=MibTableColumn
brzaccVLVlanExtendedAccessRuleId=_BrzaccVLVlanExtendedAccessRuleId_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1,2),_BrzaccVLVlanExtendedAccessRuleId_Type())
brzaccVLVlanExtendedAccessRuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRuleId.setStatus(_A)
class _BrzaccVLVlanExtendedAccessRuleVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_BrzaccVLVlanExtendedAccessRuleVlanId_Type.__name__=_C
_BrzaccVLVlanExtendedAccessRuleVlanId_Object=MibTableColumn
brzaccVLVlanExtendedAccessRuleVlanId=_BrzaccVLVlanExtendedAccessRuleVlanId_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1,3),_BrzaccVLVlanExtendedAccessRuleVlanId_Type())
brzaccVLVlanExtendedAccessRuleVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRuleVlanId.setStatus(_A)
class _BrzaccVLVlanExtendedAccessRulePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_BrzaccVLVlanExtendedAccessRulePriority_Type.__name__=_C
_BrzaccVLVlanExtendedAccessRulePriority_Object=MibTableColumn
brzaccVLVlanExtendedAccessRulePriority=_BrzaccVLVlanExtendedAccessRulePriority_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1,4),_BrzaccVLVlanExtendedAccessRulePriority_Type())
brzaccVLVlanExtendedAccessRulePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRulePriority.setStatus(_A)
class _BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('allowed',1),('notAllowed',2),(_F,255)))
_BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Type.__name__=_C
_BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Object=MibTableColumn
brzaccVLVlanExtendedAccessRuleMulticastAllowed=_BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1,5),_BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Type())
brzaccVLVlanExtendedAccessRuleMulticastAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRuleMulticastAllowed.setStatus(_A)
class _BrzaccVLVlanExtendedAccessRuleOpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('value',1),('range',2),('mask',3),('enumeration',4),(_F,255)))
_BrzaccVLVlanExtendedAccessRuleOpType_Type.__name__=_C
_BrzaccVLVlanExtendedAccessRuleOpType_Object=MibTableColumn
brzaccVLVlanExtendedAccessRuleOpType=_BrzaccVLVlanExtendedAccessRuleOpType_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1,6),_BrzaccVLVlanExtendedAccessRuleOpType_Type())
brzaccVLVlanExtendedAccessRuleOpType.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRuleOpType.setStatus(_A)
class _BrzaccVLVlanExtendedAccessRuleOperands_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_BrzaccVLVlanExtendedAccessRuleOperands_Type.__name__=_I
_BrzaccVLVlanExtendedAccessRuleOperands_Object=MibTableColumn
brzaccVLVlanExtendedAccessRuleOperands=_BrzaccVLVlanExtendedAccessRuleOperands_Object((1,3,6,1,4,1,12394,1,1,5,1,8,1,7),_BrzaccVLVlanExtendedAccessRuleOperands_Type())
brzaccVLVlanExtendedAccessRuleOperands.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanExtendedAccessRuleOperands.setStatus(_A)
class _BrzaccVLVlanExtendedTrunkVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BrzaccVLVlanExtendedTrunkVlanID_Type.__name__=_C
_BrzaccVLVlanExtendedTrunkVlanID_Object=MibScalar
brzaccVLVlanExtendedTrunkVlanID=_BrzaccVLVlanExtendedTrunkVlanID_Object((1,3,6,1,4,1,12394,1,1,5,1,9),_BrzaccVLVlanExtendedTrunkVlanID_Type())
brzaccVLVlanExtendedTrunkVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVlanExtendedTrunkVlanID.setStatus(_A)
_BrzaccVLBridgeAgingTime_Type=Integer32
_BrzaccVLBridgeAgingTime_Object=MibScalar
brzaccVLBridgeAgingTime=_BrzaccVLBridgeAgingTime_Object((1,3,6,1,4,1,12394,1,1,5,2),_BrzaccVLBridgeAgingTime_Type())
brzaccVLBridgeAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLBridgeAgingTime.setStatus(_A)
class _BrzaccVLBroadcastRelaying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_G,1),('broadcastMulticastEnable',2),('broadcastEnable',3),('multicastEnable',4),(_F,255)))
_BrzaccVLBroadcastRelaying_Type.__name__=_C
_BrzaccVLBroadcastRelaying_Object=MibScalar
brzaccVLBroadcastRelaying=_BrzaccVLBroadcastRelaying_Object((1,3,6,1,4,1,12394,1,1,5,4),_BrzaccVLBroadcastRelaying_Type())
brzaccVLBroadcastRelaying.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLBroadcastRelaying.setStatus(_A)
class _BrzaccVLUnicastRelaying_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLUnicastRelaying_Type.__name__=_C
_BrzaccVLUnicastRelaying_Object=MibScalar
brzaccVLUnicastRelaying=_BrzaccVLUnicastRelaying_Object((1,3,6,1,4,1,12394,1,1,5,5),_BrzaccVLUnicastRelaying_Type())
brzaccVLUnicastRelaying.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUnicastRelaying.setStatus(_A)
class _BrzaccVLEthBroadcastFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_G,1),('onEthernetOnly',2),('onWirelessOnly',3),('onBothWirelessAndEthernet',4),(_F,255)))
_BrzaccVLEthBroadcastFiltering_Type.__name__=_C
_BrzaccVLEthBroadcastFiltering_Object=MibScalar
brzaccVLEthBroadcastFiltering=_BrzaccVLEthBroadcastFiltering_Object((1,3,6,1,4,1,12394,1,1,5,6),_BrzaccVLEthBroadcastFiltering_Type())
brzaccVLEthBroadcastFiltering.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthBroadcastFiltering.setStatus(_A)
_BrzaccVLEthBroadcastingParameters_ObjectIdentity=ObjectIdentity
brzaccVLEthBroadcastingParameters=_BrzaccVLEthBroadcastingParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,7))
class _BrzaccVLDHCPBroadcastOverrideFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLDHCPBroadcastOverrideFilter_Type.__name__=_C
_BrzaccVLDHCPBroadcastOverrideFilter_Object=MibScalar
brzaccVLDHCPBroadcastOverrideFilter=_BrzaccVLDHCPBroadcastOverrideFilter_Object((1,3,6,1,4,1,12394,1,1,5,7,1),_BrzaccVLDHCPBroadcastOverrideFilter_Type())
brzaccVLDHCPBroadcastOverrideFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDHCPBroadcastOverrideFilter.setStatus(_A)
class _BrzaccVLPPPoEBroadcastOverrideFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLPPPoEBroadcastOverrideFilter_Type.__name__=_C
_BrzaccVLPPPoEBroadcastOverrideFilter_Object=MibScalar
brzaccVLPPPoEBroadcastOverrideFilter=_BrzaccVLPPPoEBroadcastOverrideFilter_Object((1,3,6,1,4,1,12394,1,1,5,7,2),_BrzaccVLPPPoEBroadcastOverrideFilter_Type())
brzaccVLPPPoEBroadcastOverrideFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLPPPoEBroadcastOverrideFilter.setStatus(_A)
class _BrzaccVLARPBroadcastOverrideFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLARPBroadcastOverrideFilter_Type.__name__=_C
_BrzaccVLARPBroadcastOverrideFilter_Object=MibScalar
brzaccVLARPBroadcastOverrideFilter=_BrzaccVLARPBroadcastOverrideFilter_Object((1,3,6,1,4,1,12394,1,1,5,7,3),_BrzaccVLARPBroadcastOverrideFilter_Type())
brzaccVLARPBroadcastOverrideFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLARPBroadcastOverrideFilter.setStatus(_A)
class _BrzaccVLEthBroadcastMulticastLimiterOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('limitOnlyBroadcasts',2),('limitMulticastsExceptBroadcasts',3),('limitAllMulticasts',4)))
_BrzaccVLEthBroadcastMulticastLimiterOption_Type.__name__=_C
_BrzaccVLEthBroadcastMulticastLimiterOption_Object=MibScalar
brzaccVLEthBroadcastMulticastLimiterOption=_BrzaccVLEthBroadcastMulticastLimiterOption_Object((1,3,6,1,4,1,12394,1,1,5,7,4),_BrzaccVLEthBroadcastMulticastLimiterOption_Type())
brzaccVLEthBroadcastMulticastLimiterOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthBroadcastMulticastLimiterOption.setStatus(_A)
_BrzaccVLEthBroadcastMulticastLimiterThreshold_Type=Integer32
_BrzaccVLEthBroadcastMulticastLimiterThreshold_Object=MibScalar
brzaccVLEthBroadcastMulticastLimiterThreshold=_BrzaccVLEthBroadcastMulticastLimiterThreshold_Object((1,3,6,1,4,1,12394,1,1,5,7,5),_BrzaccVLEthBroadcastMulticastLimiterThreshold_Type())
brzaccVLEthBroadcastMulticastLimiterThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthBroadcastMulticastLimiterThreshold.setStatus(_A)
_BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Type=Integer32
_BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Object=MibScalar
brzaccVLEthBroadcastMulticastLimiterSendTrapInterval=_BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Object((1,3,6,1,4,1,12394,1,1,5,7,6),_BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Type())
brzaccVLEthBroadcastMulticastLimiterSendTrapInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthBroadcastMulticastLimiterSendTrapInterval.setStatus(_A)
_BrzaccVLToSPriorityParameters_ObjectIdentity=ObjectIdentity
brzaccVLToSPriorityParameters=_BrzaccVLToSPriorityParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,8))
_BrzaccVLToSPrecedenceThreshold_Type=Integer32
_BrzaccVLToSPrecedenceThreshold_Object=MibScalar
brzaccVLToSPrecedenceThreshold=_BrzaccVLToSPrecedenceThreshold_Object((1,3,6,1,4,1,12394,1,1,5,8,1),_BrzaccVLToSPrecedenceThreshold_Type())
brzaccVLToSPrecedenceThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLToSPrecedenceThreshold.setStatus(_A)
class _BrzaccVLRoamingOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLRoamingOption_Type.__name__=_C
_BrzaccVLRoamingOption_Object=MibScalar
brzaccVLRoamingOption=_BrzaccVLRoamingOption_Object((1,3,6,1,4,1,12394,1,1,5,9),_BrzaccVLRoamingOption_Type())
brzaccVLRoamingOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLRoamingOption.setStatus(_A)
_BrzaccVLMacAddressDenyList_ObjectIdentity=ObjectIdentity
brzaccVLMacAddressDenyList=_BrzaccVLMacAddressDenyList_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,10))
_BrzaccVLMacAddressDenyListTable_Object=MibTable
brzaccVLMacAddressDenyListTable=_BrzaccVLMacAddressDenyListTable_Object((1,3,6,1,4,1,12394,1,1,5,10,1))
if mibBuilder.loadTexts:brzaccVLMacAddressDenyListTable.setStatus(_A)
_BrzaccVLMacAddressDenyListEntry_Object=MibTableRow
brzaccVLMacAddressDenyListEntry=_BrzaccVLMacAddressDenyListEntry_Object((1,3,6,1,4,1,12394,1,1,5,10,1,1))
brzaccVLMacAddressDenyListEntry.setIndexNames((0,_E,_AU))
if mibBuilder.loadTexts:brzaccVLMacAddressDenyListEntry.setStatus(_A)
class _BrzaccVLMacAddressDenyListTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_BrzaccVLMacAddressDenyListTableIdx_Type.__name__=_C
_BrzaccVLMacAddressDenyListTableIdx_Object=MibTableColumn
brzaccVLMacAddressDenyListTableIdx=_BrzaccVLMacAddressDenyListTableIdx_Object((1,3,6,1,4,1,12394,1,1,5,10,1,1,1),_BrzaccVLMacAddressDenyListTableIdx_Type())
brzaccVLMacAddressDenyListTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMacAddressDenyListTableIdx.setStatus(_A)
_BrzaccVLMacAddressDenyListId_Type=MacAddress
_BrzaccVLMacAddressDenyListId_Object=MibTableColumn
brzaccVLMacAddressDenyListId=_BrzaccVLMacAddressDenyListId_Object((1,3,6,1,4,1,12394,1,1,5,10,1,1,2),_BrzaccVLMacAddressDenyListId_Type())
brzaccVLMacAddressDenyListId.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMacAddressDenyListId.setStatus(_A)
_BrzaccVLMacAddressDenyListAdd_Type=MacAddress
_BrzaccVLMacAddressDenyListAdd_Object=MibScalar
brzaccVLMacAddressDenyListAdd=_BrzaccVLMacAddressDenyListAdd_Object((1,3,6,1,4,1,12394,1,1,5,10,2),_BrzaccVLMacAddressDenyListAdd_Type())
brzaccVLMacAddressDenyListAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMacAddressDenyListAdd.setStatus(_A)
_BrzaccVLMacAddressDenyListRemove_Type=MacAddress
_BrzaccVLMacAddressDenyListRemove_Object=MibScalar
brzaccVLMacAddressDenyListRemove=_BrzaccVLMacAddressDenyListRemove_Object((1,3,6,1,4,1,12394,1,1,5,10,3),_BrzaccVLMacAddressDenyListRemove_Type())
brzaccVLMacAddressDenyListRemove.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMacAddressDenyListRemove.setStatus(_A)
class _BrzaccVLNumberOfMacAddressesInDenyList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(255));namedValues=NamedValues((_F,255))
_BrzaccVLNumberOfMacAddressesInDenyList_Type.__name__=_C
_BrzaccVLNumberOfMacAddressesInDenyList_Object=MibScalar
brzaccVLNumberOfMacAddressesInDenyList=_BrzaccVLNumberOfMacAddressesInDenyList_Object((1,3,6,1,4,1,12394,1,1,5,10,4),_BrzaccVLNumberOfMacAddressesInDenyList_Type())
brzaccVLNumberOfMacAddressesInDenyList.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNumberOfMacAddressesInDenyList.setStatus(_A)
class _BrzaccVLMacAddressDenyListAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('denyList',1),('allowedList',2),(_F,255)))
_BrzaccVLMacAddressDenyListAction_Type.__name__=_C
_BrzaccVLMacAddressDenyListAction_Object=MibScalar
brzaccVLMacAddressDenyListAction=_BrzaccVLMacAddressDenyListAction_Object((1,3,6,1,4,1,12394,1,1,5,10,5),_BrzaccVLMacAddressDenyListAction_Type())
brzaccVLMacAddressDenyListAction.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMacAddressDenyListAction.setStatus(_A)
_BrzaccVLNewMacAddressDenyListTable_Object=MibTable
brzaccVLNewMacAddressDenyListTable=_BrzaccVLNewMacAddressDenyListTable_Object((1,3,6,1,4,1,12394,1,1,5,10,6))
if mibBuilder.loadTexts:brzaccVLNewMacAddressDenyListTable.setStatus(_A)
_BrzaccVLNewMacAddressDenyListEntry_Object=MibTableRow
brzaccVLNewMacAddressDenyListEntry=_BrzaccVLNewMacAddressDenyListEntry_Object((1,3,6,1,4,1,12394,1,1,5,10,6,1))
brzaccVLNewMacAddressDenyListEntry.setIndexNames((0,_E,_AV))
if mibBuilder.loadTexts:brzaccVLNewMacAddressDenyListEntry.setStatus(_A)
_BrzaccVLNewMacAddressDenyListId_Type=MacAddress
_BrzaccVLNewMacAddressDenyListId_Object=MibTableColumn
brzaccVLNewMacAddressDenyListId=_BrzaccVLNewMacAddressDenyListId_Object((1,3,6,1,4,1,12394,1,1,5,10,6,1,1),_BrzaccVLNewMacAddressDenyListId_Type())
brzaccVLNewMacAddressDenyListId.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewMacAddressDenyListId.setStatus(_A)
class _BrzaccVLNewMacAddressDenyListCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_BrzaccVLNewMacAddressDenyListCommand_Type.__name__=_C
_BrzaccVLNewMacAddressDenyListCommand_Object=MibTableColumn
brzaccVLNewMacAddressDenyListCommand=_BrzaccVLNewMacAddressDenyListCommand_Object((1,3,6,1,4,1,12394,1,1,5,10,6,1,2),_BrzaccVLNewMacAddressDenyListCommand_Type())
brzaccVLNewMacAddressDenyListCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewMacAddressDenyListCommand.setStatus(_A)
_BrzAccVLPortsControl_ObjectIdentity=ObjectIdentity
brzAccVLPortsControl=_BrzAccVLPortsControl_ObjectIdentity((1,3,6,1,4,1,12394,1,1,5,11))
class _BrzaccVLEthernetPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLEthernetPortControl_Type.__name__=_C
_BrzaccVLEthernetPortControl_Object=MibScalar
brzaccVLEthernetPortControl=_BrzaccVLEthernetPortControl_Object((1,3,6,1,4,1,12394,1,1,5,11,1),_BrzaccVLEthernetPortControl_Type())
brzaccVLEthernetPortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthernetPortControl.setStatus(_A)
class _BrzaccVLSendBroadcastsMulticastsAsUnicasts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BrzaccVLSendBroadcastsMulticastsAsUnicasts_Type.__name__=_C
_BrzaccVLSendBroadcastsMulticastsAsUnicasts_Object=MibScalar
brzaccVLSendBroadcastsMulticastsAsUnicasts=_BrzaccVLSendBroadcastsMulticastsAsUnicasts_Object((1,3,6,1,4,1,12394,1,1,5,12),_BrzaccVLSendBroadcastsMulticastsAsUnicasts_Type())
brzaccVLSendBroadcastsMulticastsAsUnicasts.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSendBroadcastsMulticastsAsUnicasts.setStatus(_A)
_BrzaccVLAirInterface_ObjectIdentity=ObjectIdentity
brzaccVLAirInterface=_BrzaccVLAirInterface_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6))
_BrzaccVLESSIDParameters_ObjectIdentity=ObjectIdentity
brzaccVLESSIDParameters=_BrzaccVLESSIDParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,1))
class _BrzaccVLESSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BrzaccVLESSID_Type.__name__=_I
_BrzaccVLESSID_Object=MibScalar
brzaccVLESSID=_BrzaccVLESSID_Object((1,3,6,1,4,1,12394,1,1,6,1,1),_BrzaccVLESSID_Type())
brzaccVLESSID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLESSID.setStatus(_A)
class _BrzaccVLOperatorESSIDOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLOperatorESSIDOption_Type.__name__=_C
_BrzaccVLOperatorESSIDOption_Object=MibScalar
brzaccVLOperatorESSIDOption=_BrzaccVLOperatorESSIDOption_Object((1,3,6,1,4,1,12394,1,1,6,1,2),_BrzaccVLOperatorESSIDOption_Type())
brzaccVLOperatorESSIDOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLOperatorESSIDOption.setStatus(_A)
class _BrzaccVLOperatorESSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BrzaccVLOperatorESSID_Type.__name__=_I
_BrzaccVLOperatorESSID_Object=MibScalar
brzaccVLOperatorESSID=_BrzaccVLOperatorESSID_Object((1,3,6,1,4,1,12394,1,1,6,1,3),_BrzaccVLOperatorESSID_Type())
brzaccVLOperatorESSID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLOperatorESSID.setStatus(_A)
class _BrzaccVLRunTimeESSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(31,31));fixedLength=31
_BrzaccVLRunTimeESSID_Type.__name__=_I
_BrzaccVLRunTimeESSID_Object=MibScalar
brzaccVLRunTimeESSID=_BrzaccVLRunTimeESSID_Object((1,3,6,1,4,1,12394,1,1,6,1,4),_BrzaccVLRunTimeESSID_Type())
brzaccVLRunTimeESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRunTimeESSID.setStatus(_A)
_BrzaccVLHiddenESSIDParameters_ObjectIdentity=ObjectIdentity
brzaccVLHiddenESSIDParameters=_BrzaccVLHiddenESSIDParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,1,5))
class _BrzaccVLAUHiddenESSIDOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_F,255)))
_BrzaccVLAUHiddenESSIDOption_Type.__name__=_C
_BrzaccVLAUHiddenESSIDOption_Object=MibScalar
brzaccVLAUHiddenESSIDOption=_BrzaccVLAUHiddenESSIDOption_Object((1,3,6,1,4,1,12394,1,1,6,1,5,1),_BrzaccVLAUHiddenESSIDOption_Type())
brzaccVLAUHiddenESSIDOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAUHiddenESSIDOption.setStatus(_A)
class _BrzaccVLSUHiddenESSIDSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_F,255)))
_BrzaccVLSUHiddenESSIDSupport_Type.__name__=_C
_BrzaccVLSUHiddenESSIDSupport_Object=MibScalar
brzaccVLSUHiddenESSIDSupport=_BrzaccVLSUHiddenESSIDSupport_Object((1,3,6,1,4,1,12394,1,1,6,1,5,2),_BrzaccVLSUHiddenESSIDSupport_Type())
brzaccVLSUHiddenESSIDSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSUHiddenESSIDSupport.setStatus(_A)
class _BrzaccVLSUHiddenESSIDTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_BrzaccVLSUHiddenESSIDTimeout_Type.__name__=_C
_BrzaccVLSUHiddenESSIDTimeout_Object=MibScalar
brzaccVLSUHiddenESSIDTimeout=_BrzaccVLSUHiddenESSIDTimeout_Object((1,3,6,1,4,1,12394,1,1,6,1,5,3),_BrzaccVLSUHiddenESSIDTimeout_Type())
brzaccVLSUHiddenESSIDTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSUHiddenESSIDTimeout.setStatus(_A)
_BrzaccVLMaximumCellRadius_Type=Integer32
_BrzaccVLMaximumCellRadius_Object=MibScalar
brzaccVLMaximumCellRadius=_BrzaccVLMaximumCellRadius_Object((1,3,6,1,4,1,12394,1,1,6,2),_BrzaccVLMaximumCellRadius_Type())
brzaccVLMaximumCellRadius.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaximumCellRadius.setStatus(_A)
class _BrzaccVLAIFS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_BrzaccVLAIFS_Type.__name__=_C
_BrzaccVLAIFS_Object=MibScalar
brzaccVLAIFS=_BrzaccVLAIFS_Object((1,3,6,1,4,1,12394,1,1,6,3),_BrzaccVLAIFS_Type())
brzaccVLAIFS.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAIFS.setStatus(_A)
_BrzaccVLWirelessTrapThreshold_Type=Integer32
_BrzaccVLWirelessTrapThreshold_Object=MibScalar
brzaccVLWirelessTrapThreshold=_BrzaccVLWirelessTrapThreshold_Object((1,3,6,1,4,1,12394,1,1,6,4),_BrzaccVLWirelessTrapThreshold_Type())
brzaccVLWirelessTrapThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLWirelessTrapThreshold.setStatus(_A)
_BrzaccVLTransmitPowerTable_Object=MibTable
brzaccVLTransmitPowerTable=_BrzaccVLTransmitPowerTable_Object((1,3,6,1,4,1,12394,1,1,6,5))
if mibBuilder.loadTexts:brzaccVLTransmitPowerTable.setStatus(_A)
_BrzaccVLTransmitPowerEntry_Object=MibTableRow
brzaccVLTransmitPowerEntry=_BrzaccVLTransmitPowerEntry_Object((1,3,6,1,4,1,12394,1,1,6,5,1))
brzaccVLTransmitPowerEntry.setIndexNames((0,_E,_AW))
if mibBuilder.loadTexts:brzaccVLTransmitPowerEntry.setStatus(_A)
class _BrzaccVLTransmitPowerIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrzaccVLTransmitPowerIdx_Type.__name__=_C
_BrzaccVLTransmitPowerIdx_Object=MibTableColumn
brzaccVLTransmitPowerIdx=_BrzaccVLTransmitPowerIdx_Object((1,3,6,1,4,1,12394,1,1,6,5,1,1),_BrzaccVLTransmitPowerIdx_Type())
brzaccVLTransmitPowerIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTransmitPowerIdx.setStatus(_A)
class _BrzaccVLApplicableModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AX,1),(_P,2),(_Q,3),(_R,4)))
_BrzaccVLApplicableModulationLevel_Type.__name__=_C
_BrzaccVLApplicableModulationLevel_Object=MibTableColumn
brzaccVLApplicableModulationLevel=_BrzaccVLApplicableModulationLevel_Object((1,3,6,1,4,1,12394,1,1,6,5,1,2),_BrzaccVLApplicableModulationLevel_Type())
brzaccVLApplicableModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLApplicableModulationLevel.setStatus(_A)
_BrzaccVLMaximumTxPowerRange_Type=DisplayString
_BrzaccVLMaximumTxPowerRange_Object=MibTableColumn
brzaccVLMaximumTxPowerRange=_BrzaccVLMaximumTxPowerRange_Object((1,3,6,1,4,1,12394,1,1,6,5,1,3),_BrzaccVLMaximumTxPowerRange_Type())
brzaccVLMaximumTxPowerRange.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMaximumTxPowerRange.setStatus(_A)
_BrzaccVLTxPower_Type=DisplayString
_BrzaccVLTxPower_Object=MibTableColumn
brzaccVLTxPower=_BrzaccVLTxPower_Object((1,3,6,1,4,1,12394,1,1,6,5,1,4),_BrzaccVLTxPower_Type())
brzaccVLTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTxPower.setStatus(_A)
_BrzaccVLCurrentTxPower_Type=DisplayString
_BrzaccVLCurrentTxPower_Object=MibTableColumn
brzaccVLCurrentTxPower=_BrzaccVLCurrentTxPower_Object((1,3,6,1,4,1,12394,1,1,6,5,1,5),_BrzaccVLCurrentTxPower_Type())
brzaccVLCurrentTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentTxPower.setStatus(_A)
_BrzaccVLMaximumTransmitPowerTable_Object=MibTable
brzaccVLMaximumTransmitPowerTable=_BrzaccVLMaximumTransmitPowerTable_Object((1,3,6,1,4,1,12394,1,1,6,6))
if mibBuilder.loadTexts:brzaccVLMaximumTransmitPowerTable.setStatus(_A)
_BrzaccVLMaximumTransmitPowerEntry_Object=MibTableRow
brzaccVLMaximumTransmitPowerEntry=_BrzaccVLMaximumTransmitPowerEntry_Object((1,3,6,1,4,1,12394,1,1,6,6,1))
brzaccVLMaximumTransmitPowerEntry.setIndexNames((0,_E,_AY))
if mibBuilder.loadTexts:brzaccVLMaximumTransmitPowerEntry.setStatus(_A)
class _BrzaccVLMaximumTransmitPowerIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrzaccVLMaximumTransmitPowerIdx_Type.__name__=_C
_BrzaccVLMaximumTransmitPowerIdx_Object=MibTableColumn
brzaccVLMaximumTransmitPowerIdx=_BrzaccVLMaximumTransmitPowerIdx_Object((1,3,6,1,4,1,12394,1,1,6,6,1,1),_BrzaccVLMaximumTransmitPowerIdx_Type())
brzaccVLMaximumTransmitPowerIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMaximumTransmitPowerIdx.setStatus(_A)
class _BrzaccVLMaxTxApplicableModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AX,1),(_P,2),(_Q,3),(_R,4)))
_BrzaccVLMaxTxApplicableModulationLevel_Type.__name__=_C
_BrzaccVLMaxTxApplicableModulationLevel_Object=MibTableColumn
brzaccVLMaxTxApplicableModulationLevel=_BrzaccVLMaxTxApplicableModulationLevel_Object((1,3,6,1,4,1,12394,1,1,6,6,1,2),_BrzaccVLMaxTxApplicableModulationLevel_Type())
brzaccVLMaxTxApplicableModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMaxTxApplicableModulationLevel.setStatus(_A)
_BrzaccVLDefinedMaximumTxPowerRange_Type=DisplayString
_BrzaccVLDefinedMaximumTxPowerRange_Object=MibTableColumn
brzaccVLDefinedMaximumTxPowerRange=_BrzaccVLDefinedMaximumTxPowerRange_Object((1,3,6,1,4,1,12394,1,1,6,6,1,3),_BrzaccVLDefinedMaximumTxPowerRange_Type())
brzaccVLDefinedMaximumTxPowerRange.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDefinedMaximumTxPowerRange.setStatus(_A)
_BrzaccVLMaxTxPower_Type=DisplayString
_BrzaccVLMaxTxPower_Object=MibTableColumn
brzaccVLMaxTxPower=_BrzaccVLMaxTxPower_Object((1,3,6,1,4,1,12394,1,1,6,6,1,4),_BrzaccVLMaxTxPower_Type())
brzaccVLMaxTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaxTxPower.setStatus(_A)
_BrzaccVLMaxNumOfAssociations_Type=Integer32
_BrzaccVLMaxNumOfAssociations_Object=MibScalar
brzaccVLMaxNumOfAssociations=_BrzaccVLMaxNumOfAssociations_Object((1,3,6,1,4,1,12394,1,1,6,10),_BrzaccVLMaxNumOfAssociations_Type())
brzaccVLMaxNumOfAssociations.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaxNumOfAssociations.setStatus(_A)
_BrzaccVLBestAu_ObjectIdentity=ObjectIdentity
brzaccVLBestAu=_BrzaccVLBestAu_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,11))
class _BrzaccVLBestAuSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLBestAuSupport_Type.__name__=_C
_BrzaccVLBestAuSupport_Object=MibScalar
brzaccVLBestAuSupport=_BrzaccVLBestAuSupport_Object((1,3,6,1,4,1,12394,1,1,6,11,1),_BrzaccVLBestAuSupport_Type())
brzaccVLBestAuSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLBestAuSupport.setStatus(_A)
_BrzaccVLBestAuNoOfScanningAttempts_Type=Integer32
_BrzaccVLBestAuNoOfScanningAttempts_Object=MibScalar
brzaccVLBestAuNoOfScanningAttempts=_BrzaccVLBestAuNoOfScanningAttempts_Object((1,3,6,1,4,1,12394,1,1,6,11,2),_BrzaccVLBestAuNoOfScanningAttempts_Type())
brzaccVLBestAuNoOfScanningAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLBestAuNoOfScanningAttempts.setStatus(_A)
_BrzaccVLPreferredAuMacAddress_Type=MacAddress
_BrzaccVLPreferredAuMacAddress_Object=MibScalar
brzaccVLPreferredAuMacAddress=_BrzaccVLPreferredAuMacAddress_Object((1,3,6,1,4,1,12394,1,1,6,11,3),_BrzaccVLPreferredAuMacAddress_Type())
brzaccVLPreferredAuMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLPreferredAuMacAddress.setStatus(_A)
_BrzaccVLNeighborAuTable_Object=MibTable
brzaccVLNeighborAuTable=_BrzaccVLNeighborAuTable_Object((1,3,6,1,4,1,12394,1,1,6,11,4))
if mibBuilder.loadTexts:brzaccVLNeighborAuTable.setStatus(_A)
_BrzaccVLNeighborAuEntry_Object=MibTableRow
brzaccVLNeighborAuEntry=_BrzaccVLNeighborAuEntry_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1))
brzaccVLNeighborAuEntry.setIndexNames((0,_E,_AZ))
if mibBuilder.loadTexts:brzaccVLNeighborAuEntry.setStatus(_A)
class _BrzaccVLNeighborAuIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_BrzaccVLNeighborAuIdx_Type.__name__=_C
_BrzaccVLNeighborAuIdx_Object=MibTableColumn
brzaccVLNeighborAuIdx=_BrzaccVLNeighborAuIdx_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,1),_BrzaccVLNeighborAuIdx_Type())
brzaccVLNeighborAuIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuIdx.setStatus(_A)
_BrzaccVLNeighborAuMacAdd_Type=MacAddress
_BrzaccVLNeighborAuMacAdd_Object=MibTableColumn
brzaccVLNeighborAuMacAdd=_BrzaccVLNeighborAuMacAdd_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,2),_BrzaccVLNeighborAuMacAdd_Type())
brzaccVLNeighborAuMacAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuMacAdd.setStatus(_A)
_BrzaccVLNeighborAuESSID_Type=DisplayString
_BrzaccVLNeighborAuESSID_Object=MibTableColumn
brzaccVLNeighborAuESSID=_BrzaccVLNeighborAuESSID_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,3),_BrzaccVLNeighborAuESSID_Type())
brzaccVLNeighborAuESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuESSID.setStatus(_A)
class _BrzaccVLNeighborAuSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(255));namedValues=NamedValues((_F,255))
_BrzaccVLNeighborAuSNR_Type.__name__=_C
_BrzaccVLNeighborAuSNR_Object=MibTableColumn
brzaccVLNeighborAuSNR=_BrzaccVLNeighborAuSNR_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,4),_BrzaccVLNeighborAuSNR_Type())
brzaccVLNeighborAuSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuSNR.setStatus(_A)
class _BrzaccVLNeighborAuAssocLoadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('full',1),('notFull',2),(_F,255)))
_BrzaccVLNeighborAuAssocLoadStatus_Type.__name__=_C
_BrzaccVLNeighborAuAssocLoadStatus_Object=MibTableColumn
brzaccVLNeighborAuAssocLoadStatus=_BrzaccVLNeighborAuAssocLoadStatus_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,5),_BrzaccVLNeighborAuAssocLoadStatus_Type())
brzaccVLNeighborAuAssocLoadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuAssocLoadStatus.setStatus(_A)
_BrzaccVLNeighborAuMark_Type=Integer32
_BrzaccVLNeighborAuMark_Object=MibTableColumn
brzaccVLNeighborAuMark=_BrzaccVLNeighborAuMark_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,6),_BrzaccVLNeighborAuMark_Type())
brzaccVLNeighborAuMark.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuMark.setStatus(_A)
class _BrzaccVLNeighborAuHwRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_F,255)))
_BrzaccVLNeighborAuHwRevision_Type.__name__=_C
_BrzaccVLNeighborAuHwRevision_Object=MibTableColumn
brzaccVLNeighborAuHwRevision=_BrzaccVLNeighborAuHwRevision_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,7),_BrzaccVLNeighborAuHwRevision_Type())
brzaccVLNeighborAuHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuHwRevision.setStatus(_A)
_BrzaccVLNeighborAuCountryCode_Type=Integer32
_BrzaccVLNeighborAuCountryCode_Object=MibTableColumn
brzaccVLNeighborAuCountryCode=_BrzaccVLNeighborAuCountryCode_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,8),_BrzaccVLNeighborAuCountryCode_Type())
brzaccVLNeighborAuCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuCountryCode.setStatus(_A)
_BrzaccVLNeighborAuSwVer_Type=DisplayString
_BrzaccVLNeighborAuSwVer_Object=MibTableColumn
brzaccVLNeighborAuSwVer=_BrzaccVLNeighborAuSwVer_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,9),_BrzaccVLNeighborAuSwVer_Type())
brzaccVLNeighborAuSwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuSwVer.setStatus(_A)
class _BrzaccVLNeighborAuAtpcOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuAtpcOption_Type.__name__=_C
_BrzaccVLNeighborAuAtpcOption_Object=MibTableColumn
brzaccVLNeighborAuAtpcOption=_BrzaccVLNeighborAuAtpcOption_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,10),_BrzaccVLNeighborAuAtpcOption_Type())
brzaccVLNeighborAuAtpcOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuAtpcOption.setStatus(_A)
class _BrzaccVLNeighborAuAdapModOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuAdapModOption_Type.__name__=_C
_BrzaccVLNeighborAuAdapModOption_Object=MibTableColumn
brzaccVLNeighborAuAdapModOption=_BrzaccVLNeighborAuAdapModOption_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,11),_BrzaccVLNeighborAuAdapModOption_Type())
brzaccVLNeighborAuAdapModOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuAdapModOption.setStatus(_A)
class _BrzaccVLNeighborAuBurstModeOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuBurstModeOption_Type.__name__=_C
_BrzaccVLNeighborAuBurstModeOption_Object=MibTableColumn
brzaccVLNeighborAuBurstModeOption=_BrzaccVLNeighborAuBurstModeOption_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,12),_BrzaccVLNeighborAuBurstModeOption_Type())
brzaccVLNeighborAuBurstModeOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuBurstModeOption.setStatus(_A)
class _BrzaccVLNeighborAuDfsOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuDfsOption_Type.__name__=_C
_BrzaccVLNeighborAuDfsOption_Object=MibTableColumn
brzaccVLNeighborAuDfsOption=_BrzaccVLNeighborAuDfsOption_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,14),_BrzaccVLNeighborAuDfsOption_Type())
brzaccVLNeighborAuDfsOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuDfsOption.setStatus(_A)
class _BrzaccVLNeighborAuConcatenationOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuConcatenationOption_Type.__name__=_C
_BrzaccVLNeighborAuConcatenationOption_Object=MibTableColumn
brzaccVLNeighborAuConcatenationOption=_BrzaccVLNeighborAuConcatenationOption_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,15),_BrzaccVLNeighborAuConcatenationOption_Type())
brzaccVLNeighborAuConcatenationOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuConcatenationOption.setStatus(_A)
class _BrzaccVLNeighborAuLearnCountryCodeBySU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuLearnCountryCodeBySU_Type.__name__=_C
_BrzaccVLNeighborAuLearnCountryCodeBySU_Object=MibTableColumn
brzaccVLNeighborAuLearnCountryCodeBySU=_BrzaccVLNeighborAuLearnCountryCodeBySU_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,17),_BrzaccVLNeighborAuLearnCountryCodeBySU_Type())
brzaccVLNeighborAuLearnCountryCodeBySU.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuLearnCountryCodeBySU.setStatus(_A)
class _BrzaccVLNeighborAuSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_o,1),('aesOCB',2),(_p,3),(_F,255)))
_BrzaccVLNeighborAuSecurityMode_Type.__name__=_C
_BrzaccVLNeighborAuSecurityMode_Object=MibTableColumn
brzaccVLNeighborAuSecurityMode=_BrzaccVLNeighborAuSecurityMode_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,18),_BrzaccVLNeighborAuSecurityMode_Type())
brzaccVLNeighborAuSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuSecurityMode.setStatus(_A)
class _BrzaccVLNeighborAuAuthOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_q,1),(_r,2),(_F,255)))
_BrzaccVLNeighborAuAuthOption_Type.__name__=_C
_BrzaccVLNeighborAuAuthOption_Object=MibTableColumn
brzaccVLNeighborAuAuthOption=_BrzaccVLNeighborAuAuthOption_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,19),_BrzaccVLNeighborAuAuthOption_Type())
brzaccVLNeighborAuAuthOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuAuthOption.setStatus(_A)
class _BrzaccVLNeighborAuDataEncyptOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuDataEncyptOption_Type.__name__=_C
_BrzaccVLNeighborAuDataEncyptOption_Object=MibTableColumn
brzaccVLNeighborAuDataEncyptOption=_BrzaccVLNeighborAuDataEncyptOption_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,20),_BrzaccVLNeighborAuDataEncyptOption_Type())
brzaccVLNeighborAuDataEncyptOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuDataEncyptOption.setStatus(_A)
class _BrzaccVLNeighborAuPerSuDistanceLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNeighborAuPerSuDistanceLearning_Type.__name__=_C
_BrzaccVLNeighborAuPerSuDistanceLearning_Object=MibTableColumn
brzaccVLNeighborAuPerSuDistanceLearning=_BrzaccVLNeighborAuPerSuDistanceLearning_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,21),_BrzaccVLNeighborAuPerSuDistanceLearning_Type())
brzaccVLNeighborAuPerSuDistanceLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuPerSuDistanceLearning.setStatus(_A)
class _BrzaccVLNeighborAuRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(255));namedValues=NamedValues((_F,255))
_BrzaccVLNeighborAuRSSI_Type.__name__=_C
_BrzaccVLNeighborAuRSSI_Object=MibTableColumn
brzaccVLNeighborAuRSSI=_BrzaccVLNeighborAuRSSI_Object((1,3,6,1,4,1,12394,1,1,6,11,4,1,22),_BrzaccVLNeighborAuRSSI_Type())
brzaccVLNeighborAuRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNeighborAuRSSI.setStatus(_A)
_BrzaccVLFrequencyDefinition_ObjectIdentity=ObjectIdentity
brzaccVLFrequencyDefinition=_BrzaccVLFrequencyDefinition_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,12))
_BrzaccVLSubBandLowerFrequency_Type=Integer32
_BrzaccVLSubBandLowerFrequency_Object=MibScalar
brzaccVLSubBandLowerFrequency=_BrzaccVLSubBandLowerFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,1),_BrzaccVLSubBandLowerFrequency_Type())
brzaccVLSubBandLowerFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSubBandLowerFrequency.setStatus('obsolete')
_BrzaccVLSubBandUpperFrequency_Type=Integer32
_BrzaccVLSubBandUpperFrequency_Object=MibScalar
brzaccVLSubBandUpperFrequency=_BrzaccVLSubBandUpperFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,2),_BrzaccVLSubBandUpperFrequency_Type())
brzaccVLSubBandUpperFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSubBandUpperFrequency.setStatus('obsolete')
class _BrzaccVLScanningStep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*(('mhz-5',1),('mhz-10',2),('mhz-20',3),('khz-500',4),('mhz-1',5),(_F,255)))
_BrzaccVLScanningStep_Type.__name__=_C
_BrzaccVLScanningStep_Object=MibScalar
brzaccVLScanningStep=_BrzaccVLScanningStep_Object((1,3,6,1,4,1,12394,1,1,6,12,3),_BrzaccVLScanningStep_Type())
brzaccVLScanningStep.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLScanningStep.setStatus(_A)
_BrzaccVLFrequencySubsetTable_Object=MibTable
brzaccVLFrequencySubsetTable=_BrzaccVLFrequencySubsetTable_Object((1,3,6,1,4,1,12394,1,1,6,12,4))
if mibBuilder.loadTexts:brzaccVLFrequencySubsetTable.setStatus(_A)
_BrzaccVLFrequencySubsetEntry_Object=MibTableRow
brzaccVLFrequencySubsetEntry=_BrzaccVLFrequencySubsetEntry_Object((1,3,6,1,4,1,12394,1,1,6,12,4,1))
brzaccVLFrequencySubsetEntry.setIndexNames((0,_E,_Aa))
if mibBuilder.loadTexts:brzaccVLFrequencySubsetEntry.setStatus(_A)
class _BrzaccVLFrequencySubsetTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_BrzaccVLFrequencySubsetTableIdx_Type.__name__=_C
_BrzaccVLFrequencySubsetTableIdx_Object=MibTableColumn
brzaccVLFrequencySubsetTableIdx=_BrzaccVLFrequencySubsetTableIdx_Object((1,3,6,1,4,1,12394,1,1,6,12,4,1,1),_BrzaccVLFrequencySubsetTableIdx_Type())
brzaccVLFrequencySubsetTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFrequencySubsetTableIdx.setStatus(_A)
_BrzaccVLFrequencySubsetFrequency_Type=Integer32
_BrzaccVLFrequencySubsetFrequency_Object=MibTableColumn
brzaccVLFrequencySubsetFrequency=_BrzaccVLFrequencySubsetFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,4,1,2),_BrzaccVLFrequencySubsetFrequency_Type())
brzaccVLFrequencySubsetFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFrequencySubsetFrequency.setStatus(_A)
class _BrzaccVLFrequencySubsetActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_Ab,2)))
_BrzaccVLFrequencySubsetActive_Type.__name__=_C
_BrzaccVLFrequencySubsetActive_Object=MibTableColumn
brzaccVLFrequencySubsetActive=_BrzaccVLFrequencySubsetActive_Object((1,3,6,1,4,1,12394,1,1,6,12,4,1,3),_BrzaccVLFrequencySubsetActive_Type())
brzaccVLFrequencySubsetActive.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFrequencySubsetActive.setStatus(_A)
_BrzaccVLFrequencySubsetFrequencyNew_Type=DisplayString
_BrzaccVLFrequencySubsetFrequencyNew_Object=MibTableColumn
brzaccVLFrequencySubsetFrequencyNew=_BrzaccVLFrequencySubsetFrequencyNew_Object((1,3,6,1,4,1,12394,1,1,6,12,4,1,4),_BrzaccVLFrequencySubsetFrequencyNew_Type())
brzaccVLFrequencySubsetFrequencyNew.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFrequencySubsetFrequencyNew.setStatus(_A)
class _BrzaccVLSetSelectedFreqSubset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setSelectedFreqsSubset',1),(_K,2)))
_BrzaccVLSetSelectedFreqSubset_Type.__name__=_C
_BrzaccVLSetSelectedFreqSubset_Object=MibScalar
brzaccVLSetSelectedFreqSubset=_BrzaccVLSetSelectedFreqSubset_Object((1,3,6,1,4,1,12394,1,1,6,12,5),_BrzaccVLSetSelectedFreqSubset_Type())
brzaccVLSetSelectedFreqSubset.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSetSelectedFreqSubset.setStatus(_A)
_BrzaccVLCurrentFrequencySubsetTable_Object=MibTable
brzaccVLCurrentFrequencySubsetTable=_BrzaccVLCurrentFrequencySubsetTable_Object((1,3,6,1,4,1,12394,1,1,6,12,6))
if mibBuilder.loadTexts:brzaccVLCurrentFrequencySubsetTable.setStatus(_A)
_BrzaccVLCurrentFrequencySubsetEntry_Object=MibTableRow
brzaccVLCurrentFrequencySubsetEntry=_BrzaccVLCurrentFrequencySubsetEntry_Object((1,3,6,1,4,1,12394,1,1,6,12,6,1))
brzaccVLCurrentFrequencySubsetEntry.setIndexNames((0,_E,_Ac))
if mibBuilder.loadTexts:brzaccVLCurrentFrequencySubsetEntry.setStatus(_A)
class _BrzaccVLCurrentFrequencySubsetTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_BrzaccVLCurrentFrequencySubsetTableIdx_Type.__name__=_C
_BrzaccVLCurrentFrequencySubsetTableIdx_Object=MibTableColumn
brzaccVLCurrentFrequencySubsetTableIdx=_BrzaccVLCurrentFrequencySubsetTableIdx_Object((1,3,6,1,4,1,12394,1,1,6,12,6,1,1),_BrzaccVLCurrentFrequencySubsetTableIdx_Type())
brzaccVLCurrentFrequencySubsetTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentFrequencySubsetTableIdx.setStatus(_A)
_BrzaccVLCurrentFrequencySubsetFrequency_Type=Integer32
_BrzaccVLCurrentFrequencySubsetFrequency_Object=MibTableColumn
brzaccVLCurrentFrequencySubsetFrequency=_BrzaccVLCurrentFrequencySubsetFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,6,1,2),_BrzaccVLCurrentFrequencySubsetFrequency_Type())
brzaccVLCurrentFrequencySubsetFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentFrequencySubsetFrequency.setStatus(_A)
_BrzaccVLCurrentFrequencySubsetFrequencyNew_Type=DisplayString
_BrzaccVLCurrentFrequencySubsetFrequencyNew_Object=MibTableColumn
brzaccVLCurrentFrequencySubsetFrequencyNew=_BrzaccVLCurrentFrequencySubsetFrequencyNew_Object((1,3,6,1,4,1,12394,1,1,6,12,6,1,3),_BrzaccVLCurrentFrequencySubsetFrequencyNew_Type())
brzaccVLCurrentFrequencySubsetFrequencyNew.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentFrequencySubsetFrequencyNew.setStatus(_A)
_BrzaccVLCurrentAUOperatingFrequency_Type=Integer32
_BrzaccVLCurrentAUOperatingFrequency_Object=MibScalar
brzaccVLCurrentAUOperatingFrequency=_BrzaccVLCurrentAUOperatingFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,7),_BrzaccVLCurrentAUOperatingFrequency_Type())
brzaccVLCurrentAUOperatingFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentAUOperatingFrequency.setStatus(_A)
_BrzaccVLAUDefinedFrequency_Type=Integer32
_BrzaccVLAUDefinedFrequency_Object=MibScalar
brzaccVLAUDefinedFrequency=_BrzaccVLAUDefinedFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,8),_BrzaccVLAUDefinedFrequency_Type())
brzaccVLAUDefinedFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAUDefinedFrequency.setStatus(_A)
_BrzaccVLCurrentSUOperatingFrequency_Type=DisplayString
_BrzaccVLCurrentSUOperatingFrequency_Object=MibScalar
brzaccVLCurrentSUOperatingFrequency=_BrzaccVLCurrentSUOperatingFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,9),_BrzaccVLCurrentSUOperatingFrequency_Type())
brzaccVLCurrentSUOperatingFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentSUOperatingFrequency.setStatus(_A)
_BrzaccVLSubBandSelect_ObjectIdentity=ObjectIdentity
brzaccVLSubBandSelect=_BrzaccVLSubBandSelect_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,12,10))
_BrzaccVLSelectSubBandIndex_Type=Integer32
_BrzaccVLSelectSubBandIndex_Object=MibScalar
brzaccVLSelectSubBandIndex=_BrzaccVLSelectSubBandIndex_Object((1,3,6,1,4,1,12394,1,1,6,12,10,1),_BrzaccVLSelectSubBandIndex_Type())
brzaccVLSelectSubBandIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSelectSubBandIndex.setStatus(_A)
_BrzaccVLDFSParameters_ObjectIdentity=ObjectIdentity
brzaccVLDFSParameters=_BrzaccVLDFSParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,12,11))
class _BrzaccVLDFSOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLDFSOption_Type.__name__=_C
_BrzaccVLDFSOption_Object=MibScalar
brzaccVLDFSOption=_BrzaccVLDFSOption_Object((1,3,6,1,4,1,12394,1,1,6,12,11,1),_BrzaccVLDFSOption_Type())
brzaccVLDFSOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSOption.setStatus(_A)
_BrzaccVLDFSChannelCheckTime_Type=Integer32
_BrzaccVLDFSChannelCheckTime_Object=MibScalar
brzaccVLDFSChannelCheckTime=_BrzaccVLDFSChannelCheckTime_Object((1,3,6,1,4,1,12394,1,1,6,12,11,3),_BrzaccVLDFSChannelCheckTime_Type())
brzaccVLDFSChannelCheckTime.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSChannelCheckTime.setStatus(_A)
_BrzaccVLDFSChannelAvoidancePeriod_Type=Integer32
_BrzaccVLDFSChannelAvoidancePeriod_Object=MibScalar
brzaccVLDFSChannelAvoidancePeriod=_BrzaccVLDFSChannelAvoidancePeriod_Object((1,3,6,1,4,1,12394,1,1,6,12,11,4),_BrzaccVLDFSChannelAvoidancePeriod_Type())
brzaccVLDFSChannelAvoidancePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSChannelAvoidancePeriod.setStatus(_A)
class _BrzaccVLDFSSuWaitingOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLDFSSuWaitingOption_Type.__name__=_C
_BrzaccVLDFSSuWaitingOption_Object=MibScalar
brzaccVLDFSSuWaitingOption=_BrzaccVLDFSSuWaitingOption_Object((1,3,6,1,4,1,12394,1,1,6,12,11,5),_BrzaccVLDFSSuWaitingOption_Type())
brzaccVLDFSSuWaitingOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSSuWaitingOption.setStatus(_A)
class _BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_K,1),('clearRadarChannels',2),(_F,255)))
_BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Type.__name__=_C
_BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Object=MibScalar
brzaccVLDFSClearRadarDetectedChannelsAfterReset=_BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Object((1,3,6,1,4,1,12394,1,1,6,12,11,6),_BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Type())
brzaccVLDFSClearRadarDetectedChannelsAfterReset.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSClearRadarDetectedChannelsAfterReset.setStatus(_A)
_BrzaccVLDFSRadarDetectionChannelsTable_Object=MibTable
brzaccVLDFSRadarDetectionChannelsTable=_BrzaccVLDFSRadarDetectionChannelsTable_Object((1,3,6,1,4,1,12394,1,1,6,12,11,7))
if mibBuilder.loadTexts:brzaccVLDFSRadarDetectionChannelsTable.setStatus(_A)
_BrzaccVLDFSRadarDetectionChannelsEntry_Object=MibTableRow
brzaccVLDFSRadarDetectionChannelsEntry=_BrzaccVLDFSRadarDetectionChannelsEntry_Object((1,3,6,1,4,1,12394,1,1,6,12,11,7,1))
brzaccVLDFSRadarDetectionChannelsEntry.setIndexNames((0,_E,_Ad))
if mibBuilder.loadTexts:brzaccVLDFSRadarDetectionChannelsEntry.setStatus(_A)
class _BrzaccVLDFSChannelIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_BrzaccVLDFSChannelIdx_Type.__name__=_C
_BrzaccVLDFSChannelIdx_Object=MibTableColumn
brzaccVLDFSChannelIdx=_BrzaccVLDFSChannelIdx_Object((1,3,6,1,4,1,12394,1,1,6,12,11,7,1,1),_BrzaccVLDFSChannelIdx_Type())
brzaccVLDFSChannelIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDFSChannelIdx.setStatus(_A)
_BrzaccVLDFSChannelFrequency_Type=Integer32
_BrzaccVLDFSChannelFrequency_Object=MibTableColumn
brzaccVLDFSChannelFrequency=_BrzaccVLDFSChannelFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,11,7,1,2),_BrzaccVLDFSChannelFrequency_Type())
brzaccVLDFSChannelFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDFSChannelFrequency.setStatus(_A)
class _BrzaccVLDFSChannelRadarStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Ae,1),(_Af,2),(_Ag,3)))
_BrzaccVLDFSChannelRadarStatus_Type.__name__=_C
_BrzaccVLDFSChannelRadarStatus_Object=MibTableColumn
brzaccVLDFSChannelRadarStatus=_BrzaccVLDFSChannelRadarStatus_Object((1,3,6,1,4,1,12394,1,1,6,12,11,7,1,3),_BrzaccVLDFSChannelRadarStatus_Type())
brzaccVLDFSChannelRadarStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDFSChannelRadarStatus.setStatus(_A)
_BrzaccVLDFSChannelFrequencyNew_Type=DisplayString
_BrzaccVLDFSChannelFrequencyNew_Object=MibTableColumn
brzaccVLDFSChannelFrequencyNew=_BrzaccVLDFSChannelFrequencyNew_Object((1,3,6,1,4,1,12394,1,1,6,12,11,7,1,4),_BrzaccVLDFSChannelFrequencyNew_Type())
brzaccVLDFSChannelFrequencyNew.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDFSChannelFrequencyNew.setStatus(_A)
_BrzaccVLDFSMinimumPulsesToDetect_Type=Integer32
_BrzaccVLDFSMinimumPulsesToDetect_Object=MibScalar
brzaccVLDFSMinimumPulsesToDetect=_BrzaccVLDFSMinimumPulsesToDetect_Object((1,3,6,1,4,1,12394,1,1,6,12,11,8),_BrzaccVLDFSMinimumPulsesToDetect_Type())
brzaccVLDFSMinimumPulsesToDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSMinimumPulsesToDetect.setStatus(_A)
_BrzaccVLDFSChannelReuseParameters_ObjectIdentity=ObjectIdentity
brzaccVLDFSChannelReuseParameters=_BrzaccVLDFSChannelReuseParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,12,11,9))
class _BrzaccVLDFSChannelReuseOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLDFSChannelReuseOption_Type.__name__=_C
_BrzaccVLDFSChannelReuseOption_Object=MibScalar
brzaccVLDFSChannelReuseOption=_BrzaccVLDFSChannelReuseOption_Object((1,3,6,1,4,1,12394,1,1,6,12,11,9,1),_BrzaccVLDFSChannelReuseOption_Type())
brzaccVLDFSChannelReuseOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSChannelReuseOption.setStatus(_A)
_BrzaccVLDFSRadarActivityAssessmentPeriod_Type=Integer32
_BrzaccVLDFSRadarActivityAssessmentPeriod_Object=MibScalar
brzaccVLDFSRadarActivityAssessmentPeriod=_BrzaccVLDFSRadarActivityAssessmentPeriod_Object((1,3,6,1,4,1,12394,1,1,6,12,11,9,2),_BrzaccVLDFSRadarActivityAssessmentPeriod_Type())
brzaccVLDFSRadarActivityAssessmentPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSRadarActivityAssessmentPeriod.setStatus(_A)
_BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Type=Integer32
_BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Object=MibScalar
brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod=_BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Object((1,3,6,1,4,1,12394,1,1,6,12,11,9,3),_BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Type())
brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod.setStatus(_A)
class _BrzaccVLDFSDetectionAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('etsi',1),('fcc',2),(_F,255)))
_BrzaccVLDFSDetectionAlgorithm_Type.__name__=_C
_BrzaccVLDFSDetectionAlgorithm_Object=MibScalar
brzaccVLDFSDetectionAlgorithm=_BrzaccVLDFSDetectionAlgorithm_Object((1,3,6,1,4,1,12394,1,1,6,12,11,10),_BrzaccVLDFSDetectionAlgorithm_Type())
brzaccVLDFSDetectionAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSDetectionAlgorithm.setStatus(_A)
_BrzaccVLDFSRemoteRadarEventReports_Type=Integer32
_BrzaccVLDFSRemoteRadarEventReports_Object=MibScalar
brzaccVLDFSRemoteRadarEventReports=_BrzaccVLDFSRemoteRadarEventReports_Object((1,3,6,1,4,1,12394,1,1,6,12,11,11),_BrzaccVLDFSRemoteRadarEventReports_Type())
brzaccVLDFSRemoteRadarEventReports.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSRemoteRadarEventReports.setStatus(_A)
_BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Type=Integer32
_BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Object=MibScalar
brzaccVLDFSRemoteRadarEventMonitoringPeriod=_BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Object((1,3,6,1,4,1,12394,1,1,6,12,11,12),_BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Type())
brzaccVLDFSRemoteRadarEventMonitoringPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDFSRemoteRadarEventMonitoringPeriod.setStatus(_A)
class _BrzaccVLEnhancedETSIRadarDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),('on',2)))
_BrzaccVLEnhancedETSIRadarDetection_Type.__name__=_C
_BrzaccVLEnhancedETSIRadarDetection_Object=MibScalar
brzaccVLEnhancedETSIRadarDetection=_BrzaccVLEnhancedETSIRadarDetection_Object((1,3,6,1,4,1,12394,1,1,6,12,11,13),_BrzaccVLEnhancedETSIRadarDetection_Type())
brzaccVLEnhancedETSIRadarDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEnhancedETSIRadarDetection.setStatus(_A)
class _BrzaccVLCountryCodeLearningBySU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLCountryCodeLearningBySU_Type.__name__=_C
_BrzaccVLCountryCodeLearningBySU_Object=MibScalar
brzaccVLCountryCodeLearningBySU=_BrzaccVLCountryCodeLearningBySU_Object((1,3,6,1,4,1,12394,1,1,6,12,12),_BrzaccVLCountryCodeLearningBySU_Type())
brzaccVLCountryCodeLearningBySU.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLCountryCodeLearningBySU.setStatus(_A)
_BrzaccVLCurrentAUOperatingFrequencyNew_Type=DisplayString
_BrzaccVLCurrentAUOperatingFrequencyNew_Object=MibScalar
brzaccVLCurrentAUOperatingFrequencyNew=_BrzaccVLCurrentAUOperatingFrequencyNew_Object((1,3,6,1,4,1,12394,1,1,6,12,13),_BrzaccVLCurrentAUOperatingFrequencyNew_Type())
brzaccVLCurrentAUOperatingFrequencyNew.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentAUOperatingFrequencyNew.setStatus(_A)
_BrzaccVLAUDefinedFrequencyNew_Type=DisplayString
_BrzaccVLAUDefinedFrequencyNew_Object=MibScalar
brzaccVLAUDefinedFrequencyNew=_BrzaccVLAUDefinedFrequencyNew_Object((1,3,6,1,4,1,12394,1,1,6,12,14),_BrzaccVLAUDefinedFrequencyNew_Type())
brzaccVLAUDefinedFrequencyNew.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAUDefinedFrequencyNew.setStatus(_A)
_BrzaccVLAutoSubBandSelect_ObjectIdentity=ObjectIdentity
brzaccVLAutoSubBandSelect=_BrzaccVLAutoSubBandSelect_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,12,15))
class _BrzaccVLAutoSubBandSelectedFreqSubset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setAllSelectedFreqsSubset',1),(_K,2)))
_BrzaccVLAutoSubBandSelectedFreqSubset_Type.__name__=_C
_BrzaccVLAutoSubBandSelectedFreqSubset_Object=MibScalar
brzaccVLAutoSubBandSelectedFreqSubset=_BrzaccVLAutoSubBandSelectedFreqSubset_Object((1,3,6,1,4,1,12394,1,1,6,12,15,1),_BrzaccVLAutoSubBandSelectedFreqSubset_Type())
brzaccVLAutoSubBandSelectedFreqSubset.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAutoSubBandSelectedFreqSubset.setStatus(_A)
_BrzaccVLAutoSubBandFrequencySubsetTable_Object=MibTable
brzaccVLAutoSubBandFrequencySubsetTable=_BrzaccVLAutoSubBandFrequencySubsetTable_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2))
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetTable.setStatus(_A)
_BrzaccVLAutoSubBandFrequencySubsetEntry_Object=MibTableRow
brzaccVLAutoSubBandFrequencySubsetEntry=_BrzaccVLAutoSubBandFrequencySubsetEntry_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2,1))
brzaccVLAutoSubBandFrequencySubsetEntry.setIndexNames((0,_E,_Ah),(0,_E,_Ai))
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetEntry.setStatus(_A)
class _BrzaccVLAutoSubBandFrequencySubsetBandIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_BrzaccVLAutoSubBandFrequencySubsetBandIdx_Type.__name__=_C
_BrzaccVLAutoSubBandFrequencySubsetBandIdx_Object=MibTableColumn
brzaccVLAutoSubBandFrequencySubsetBandIdx=_BrzaccVLAutoSubBandFrequencySubsetBandIdx_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2,1,1),_BrzaccVLAutoSubBandFrequencySubsetBandIdx_Type())
brzaccVLAutoSubBandFrequencySubsetBandIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetBandIdx.setStatus(_A)
class _BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Type.__name__=_C
_BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Object=MibTableColumn
brzaccVLAutoSubBandFrequencySubsetFrequencyIdx=_BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2,1,2),_BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Type())
brzaccVLAutoSubBandFrequencySubsetFrequencyIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetFrequencyIdx.setStatus(_A)
class _BrzaccVLAutoSubBandFrequencySubsetActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_Ab,2)))
_BrzaccVLAutoSubBandFrequencySubsetActive_Type.__name__=_C
_BrzaccVLAutoSubBandFrequencySubsetActive_Object=MibTableColumn
brzaccVLAutoSubBandFrequencySubsetActive=_BrzaccVLAutoSubBandFrequencySubsetActive_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2,1,3),_BrzaccVLAutoSubBandFrequencySubsetActive_Type())
brzaccVLAutoSubBandFrequencySubsetActive.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetActive.setStatus(_A)
_BrzaccVLAutoSubBandFrequencySubsetFrequency_Type=DisplayString
_BrzaccVLAutoSubBandFrequencySubsetFrequency_Object=MibTableColumn
brzaccVLAutoSubBandFrequencySubsetFrequency=_BrzaccVLAutoSubBandFrequencySubsetFrequency_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2,1,4),_BrzaccVLAutoSubBandFrequencySubsetFrequency_Type())
brzaccVLAutoSubBandFrequencySubsetFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetFrequency.setStatus(_A)
_BrzaccVLAutoSubBandFrequencySubsetBandwidth_Type=Integer32
_BrzaccVLAutoSubBandFrequencySubsetBandwidth_Object=MibTableColumn
brzaccVLAutoSubBandFrequencySubsetBandwidth=_BrzaccVLAutoSubBandFrequencySubsetBandwidth_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2,1,5),_BrzaccVLAutoSubBandFrequencySubsetBandwidth_Type())
brzaccVLAutoSubBandFrequencySubsetBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetBandwidth.setStatus(_A)
class _BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Ae,1),(_Af,2),(_Ag,3)))
_BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Type.__name__=_C
_BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Object=MibTableColumn
brzaccVLAutoSubBandFrequencySubsetDFSStatus=_BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Object((1,3,6,1,4,1,12394,1,1,6,12,15,2,1,6),_BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Type())
brzaccVLAutoSubBandFrequencySubsetDFSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAutoSubBandFrequencySubsetDFSStatus.setStatus(_A)
_BrzaccVLATPC_ObjectIdentity=ObjectIdentity
brzaccVLATPC=_BrzaccVLATPC_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,13))
class _BrzaccVLAtpcOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAtpcOption_Type.__name__=_C
_BrzaccVLAtpcOption_Object=MibScalar
brzaccVLAtpcOption=_BrzaccVLAtpcOption_Object((1,3,6,1,4,1,12394,1,1,6,13,1),_BrzaccVLAtpcOption_Type())
brzaccVLAtpcOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAtpcOption.setStatus(_A)
_BrzaccVLDeltaFromMinSNRLevel_Type=Integer32
_BrzaccVLDeltaFromMinSNRLevel_Object=MibScalar
brzaccVLDeltaFromMinSNRLevel=_BrzaccVLDeltaFromMinSNRLevel_Object((1,3,6,1,4,1,12394,1,1,6,13,2),_BrzaccVLDeltaFromMinSNRLevel_Type())
brzaccVLDeltaFromMinSNRLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeltaFromMinSNRLevel.setStatus(_A)
_BrzaccVLMinimumSNRLevel_Type=Integer32
_BrzaccVLMinimumSNRLevel_Object=MibScalar
brzaccVLMinimumSNRLevel=_BrzaccVLMinimumSNRLevel_Object((1,3,6,1,4,1,12394,1,1,6,13,3),_BrzaccVLMinimumSNRLevel_Type())
brzaccVLMinimumSNRLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMinimumSNRLevel.setStatus(_A)
_BrzaccVLMinimumIntervalBetweenATPCMessages_Type=Integer32
_BrzaccVLMinimumIntervalBetweenATPCMessages_Object=MibScalar
brzaccVLMinimumIntervalBetweenATPCMessages=_BrzaccVLMinimumIntervalBetweenATPCMessages_Object((1,3,6,1,4,1,12394,1,1,6,13,4),_BrzaccVLMinimumIntervalBetweenATPCMessages_Type())
brzaccVLMinimumIntervalBetweenATPCMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMinimumIntervalBetweenATPCMessages.setStatus(_A)
_BrzaccVLPowerLevelSteps_Type=Integer32
_BrzaccVLPowerLevelSteps_Object=MibScalar
brzaccVLPowerLevelSteps=_BrzaccVLPowerLevelSteps_Object((1,3,6,1,4,1,12394,1,1,6,13,6),_BrzaccVLPowerLevelSteps_Type())
brzaccVLPowerLevelSteps.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLPowerLevelSteps.setStatus(_A)
class _BrzaccVLAtpcOptionEZ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAtpcOptionEZ_Type.__name__=_C
_BrzaccVLAtpcOptionEZ_Object=MibScalar
brzaccVLAtpcOptionEZ=_BrzaccVLAtpcOptionEZ_Object((1,3,6,1,4,1,12394,1,1,6,13,7),_BrzaccVLAtpcOptionEZ_Type())
brzaccVLAtpcOptionEZ.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAtpcOptionEZ.setStatus(_A)
_BrzaccVLCellDistanceParameters_ObjectIdentity=ObjectIdentity
brzaccVLCellDistanceParameters=_BrzaccVLCellDistanceParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,15))
class _BrzaccVLCellDistanceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_n,1),('manual',2),(_F,255)))
_BrzaccVLCellDistanceMode_Type.__name__=_C
_BrzaccVLCellDistanceMode_Object=MibScalar
brzaccVLCellDistanceMode=_BrzaccVLCellDistanceMode_Object((1,3,6,1,4,1,12394,1,1,6,15,1),_BrzaccVLCellDistanceMode_Type())
brzaccVLCellDistanceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLCellDistanceMode.setStatus(_A)
_BrzaccVLFairnessFactor_Type=Integer32
_BrzaccVLFairnessFactor_Object=MibScalar
brzaccVLFairnessFactor=_BrzaccVLFairnessFactor_Object((1,3,6,1,4,1,12394,1,1,6,15,2),_BrzaccVLFairnessFactor_Type())
brzaccVLFairnessFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLFairnessFactor.setStatus(_A)
class _BrzaccVLMeasuredCellDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_w,1))
_BrzaccVLMeasuredCellDistance_Type.__name__=_C
_BrzaccVLMeasuredCellDistance_Object=MibScalar
brzaccVLMeasuredCellDistance=_BrzaccVLMeasuredCellDistance_Object((1,3,6,1,4,1,12394,1,1,6,15,3),_BrzaccVLMeasuredCellDistance_Type())
brzaccVLMeasuredCellDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMeasuredCellDistance.setStatus(_A)
_BrzaccVLUnitWithMaxDistance_Type=MacAddress
_BrzaccVLUnitWithMaxDistance_Object=MibScalar
brzaccVLUnitWithMaxDistance=_BrzaccVLUnitWithMaxDistance_Object((1,3,6,1,4,1,12394,1,1,6,15,4),_BrzaccVLUnitWithMaxDistance_Type())
brzaccVLUnitWithMaxDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUnitWithMaxDistance.setStatus(_A)
class _BrzaccVLPerSuDistanceLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLPerSuDistanceLearning_Type.__name__=_C
_BrzaccVLPerSuDistanceLearning_Object=MibScalar
brzaccVLPerSuDistanceLearning=_BrzaccVLPerSuDistanceLearning_Object((1,3,6,1,4,1,12394,1,1,6,15,5),_BrzaccVLPerSuDistanceLearning_Type())
brzaccVLPerSuDistanceLearning.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLPerSuDistanceLearning.setStatus(_A)
class _BrzaccVLScanningMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passive',1),(_O,2)))
_BrzaccVLScanningMode_Type.__name__=_C
_BrzaccVLScanningMode_Object=MibScalar
brzaccVLScanningMode=_BrzaccVLScanningMode_Object((1,3,6,1,4,1,12394,1,1,6,16),_BrzaccVLScanningMode_Type())
brzaccVLScanningMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLScanningMode.setStatus(_A)
_BrzaccVLAntennaGain_Type=DisplayString
_BrzaccVLAntennaGain_Object=MibScalar
brzaccVLAntennaGain=_BrzaccVLAntennaGain_Object((1,3,6,1,4,1,12394,1,1,6,17),_BrzaccVLAntennaGain_Type())
brzaccVLAntennaGain.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAntennaGain.setStatus(_A)
_BrzaccVLSpectrumAnalysisParameters_ObjectIdentity=ObjectIdentity
brzaccVLSpectrumAnalysisParameters=_BrzaccVLSpectrumAnalysisParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,18))
_BrzaccVLSpectrumAnalysisChannelScanPeriod_Type=Integer32
_BrzaccVLSpectrumAnalysisChannelScanPeriod_Object=MibScalar
brzaccVLSpectrumAnalysisChannelScanPeriod=_BrzaccVLSpectrumAnalysisChannelScanPeriod_Object((1,3,6,1,4,1,12394,1,1,6,18,1),_BrzaccVLSpectrumAnalysisChannelScanPeriod_Type())
brzaccVLSpectrumAnalysisChannelScanPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisChannelScanPeriod.setStatus(_A)
_BrzaccVLSpectrumAnalysisScanCycles_Type=Integer32
_BrzaccVLSpectrumAnalysisScanCycles_Object=MibScalar
brzaccVLSpectrumAnalysisScanCycles=_BrzaccVLSpectrumAnalysisScanCycles_Object((1,3,6,1,4,1,12394,1,1,6,18,2),_BrzaccVLSpectrumAnalysisScanCycles_Type())
brzaccVLSpectrumAnalysisScanCycles.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisScanCycles.setStatus(_A)
class _BrzaccVLAutomaticChannelSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAutomaticChannelSelection_Type.__name__=_C
_BrzaccVLAutomaticChannelSelection_Object=MibScalar
brzaccVLAutomaticChannelSelection=_BrzaccVLAutomaticChannelSelection_Object((1,3,6,1,4,1,12394,1,1,6,18,3),_BrzaccVLAutomaticChannelSelection_Type())
brzaccVLAutomaticChannelSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAutomaticChannelSelection.setStatus(_A)
class _BrzaccVLSpectrumAnalysisActivation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_Aj,2)))
_BrzaccVLSpectrumAnalysisActivation_Type.__name__=_C
_BrzaccVLSpectrumAnalysisActivation_Object=MibScalar
brzaccVLSpectrumAnalysisActivation=_BrzaccVLSpectrumAnalysisActivation_Object((1,3,6,1,4,1,12394,1,1,6,18,4),_BrzaccVLSpectrumAnalysisActivation_Type())
brzaccVLSpectrumAnalysisActivation.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisActivation.setStatus(_A)
class _BrzaccVLSpectrumAnalysisStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_x,1),(_y,2),(_Ak,3)))
_BrzaccVLSpectrumAnalysisStatus_Type.__name__=_C
_BrzaccVLSpectrumAnalysisStatus_Object=MibScalar
brzaccVLSpectrumAnalysisStatus=_BrzaccVLSpectrumAnalysisStatus_Object((1,3,6,1,4,1,12394,1,1,6,18,5),_BrzaccVLSpectrumAnalysisStatus_Type())
brzaccVLSpectrumAnalysisStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisStatus.setStatus(_A)
class _BrzaccVLResetSpectrumCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_Al,2)))
_BrzaccVLResetSpectrumCounters_Type.__name__=_C
_BrzaccVLResetSpectrumCounters_Object=MibScalar
brzaccVLResetSpectrumCounters=_BrzaccVLResetSpectrumCounters_Object((1,3,6,1,4,1,12394,1,1,6,18,6),_BrzaccVLResetSpectrumCounters_Type())
brzaccVLResetSpectrumCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLResetSpectrumCounters.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationTable_Object=MibTable
brzaccVLSpectrumAnalysisInformationTable=_BrzaccVLSpectrumAnalysisInformationTable_Object((1,3,6,1,4,1,12394,1,1,6,18,7))
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationTable.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationEntry_Object=MibTableRow
brzaccVLSpectrumAnalysisInformationEntry=_BrzaccVLSpectrumAnalysisInformationEntry_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1))
brzaccVLSpectrumAnalysisInformationEntry.setIndexNames((0,_E,_Am))
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationEntry.setStatus(_A)
class _BrzaccVLSpectrumAnalysisInformationTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_BrzaccVLSpectrumAnalysisInformationTableIdx_Type.__name__=_C
_BrzaccVLSpectrumAnalysisInformationTableIdx_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationTableIdx=_BrzaccVLSpectrumAnalysisInformationTableIdx_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,1),_BrzaccVLSpectrumAnalysisInformationTableIdx_Type())
brzaccVLSpectrumAnalysisInformationTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationTableIdx.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationChannel_Type=DisplayString
_BrzaccVLSpectrumAnalysisInformationChannel_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationChannel=_BrzaccVLSpectrumAnalysisInformationChannel_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,2),_BrzaccVLSpectrumAnalysisInformationChannel_Type())
brzaccVLSpectrumAnalysisInformationChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationChannel.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationSignalCount_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationSignalCount_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalCount=_BrzaccVLSpectrumAnalysisInformationSignalCount_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,3),_BrzaccVLSpectrumAnalysisInformationSignalCount_Type())
brzaccVLSpectrumAnalysisInformationSignalCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationSignalCount.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationSignalSNR_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationSignalSNR_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalSNR=_BrzaccVLSpectrumAnalysisInformationSignalSNR_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,4),_BrzaccVLSpectrumAnalysisInformationSignalSNR_Type())
brzaccVLSpectrumAnalysisInformationSignalSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationSignalSNR.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationSignalWidth_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationSignalWidth_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalWidth=_BrzaccVLSpectrumAnalysisInformationSignalWidth_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,5),_BrzaccVLSpectrumAnalysisInformationSignalWidth_Type())
brzaccVLSpectrumAnalysisInformationSignalWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationSignalWidth.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationOFDMFrames_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationOFDMFrames_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationOFDMFrames=_BrzaccVLSpectrumAnalysisInformationOFDMFrames_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,6),_BrzaccVLSpectrumAnalysisInformationOFDMFrames_Type())
brzaccVLSpectrumAnalysisInformationOFDMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationOFDMFrames.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationOFDMAvgSnr=_BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,7),_BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Type())
brzaccVLSpectrumAnalysisInformationOFDMAvgSnr.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationOFDMAvgSnr.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationAvgNoiseFloor=_BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,8),_BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Type())
brzaccVLSpectrumAnalysisInformationAvgNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationAvgNoiseFloor.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationMaxNoiseFloor=_BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,9),_BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Type())
brzaccVLSpectrumAnalysisInformationMaxNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationMaxNoiseFloor.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalMaxSNR=_BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,10),_BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Type())
brzaccVLSpectrumAnalysisInformationSignalMaxSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationSignalMaxSNR.setStatus(_A)
_BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Type=Integer32
_BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Object=MibTableColumn
brzaccVLSpectrumAnalysisInformationOFDMMaxSNR=_BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Object((1,3,6,1,4,1,12394,1,1,6,18,7,1,11),_BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Type())
brzaccVLSpectrumAnalysisInformationOFDMMaxSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSpectrumAnalysisInformationOFDMMaxSNR.setStatus(_A)
_BrzaccVLMaxNumOfAssociationsLimit_Type=Integer32
_BrzaccVLMaxNumOfAssociationsLimit_Object=MibScalar
brzaccVLMaxNumOfAssociationsLimit=_BrzaccVLMaxNumOfAssociationsLimit_Object((1,3,6,1,4,1,12394,1,1,6,19),_BrzaccVLMaxNumOfAssociationsLimit_Type())
brzaccVLMaxNumOfAssociationsLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLMaxNumOfAssociationsLimit.setStatus(_A)
_BrzaccVLDisassociate_ObjectIdentity=ObjectIdentity
brzaccVLDisassociate=_BrzaccVLDisassociate_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,20))
class _BrzaccVLDisassociateAllSUs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('disassociateAllSUs',2)))
_BrzaccVLDisassociateAllSUs_Type.__name__=_C
_BrzaccVLDisassociateAllSUs_Object=MibScalar
brzaccVLDisassociateAllSUs=_BrzaccVLDisassociateAllSUs_Object((1,3,6,1,4,1,12394,1,1,6,20,1),_BrzaccVLDisassociateAllSUs_Type())
brzaccVLDisassociateAllSUs.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDisassociateAllSUs.setStatus(_A)
_BrzaccVLDisassociateSuByMacAddress_Type=MacAddress
_BrzaccVLDisassociateSuByMacAddress_Object=MibScalar
brzaccVLDisassociateSuByMacAddress=_BrzaccVLDisassociateSuByMacAddress_Object((1,3,6,1,4,1,12394,1,1,6,20,2),_BrzaccVLDisassociateSuByMacAddress_Type())
brzaccVLDisassociateSuByMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDisassociateSuByMacAddress.setStatus(_A)
class _BrzaccVLTxControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_v,2),('ethernetStatusControl',3)))
_BrzaccVLTxControl_Type.__name__=_C
_BrzaccVLTxControl_Object=MibScalar
brzaccVLTxControl=_BrzaccVLTxControl_Object((1,3,6,1,4,1,12394,1,1,6,21),_BrzaccVLTxControl_Type())
brzaccVLTxControl.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTxControl.setStatus(_A)
class _BrzaccVLLostBeaconsWatchdogThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(100,1000))
_BrzaccVLLostBeaconsWatchdogThreshold_Type.__name__=_C
_BrzaccVLLostBeaconsWatchdogThreshold_Object=MibScalar
brzaccVLLostBeaconsWatchdogThreshold=_BrzaccVLLostBeaconsWatchdogThreshold_Object((1,3,6,1,4,1,12394,1,1,6,22),_BrzaccVLLostBeaconsWatchdogThreshold_Type())
brzaccVLLostBeaconsWatchdogThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLLostBeaconsWatchdogThreshold.setStatus(_A)
_BrzaccVLTransmitPower_Type=Integer32
_BrzaccVLTransmitPower_Object=MibScalar
brzaccVLTransmitPower=_BrzaccVLTransmitPower_Object((1,3,6,1,4,1,12394,1,1,6,23),_BrzaccVLTransmitPower_Type())
brzaccVLTransmitPower.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTransmitPower.setStatus(_A)
_BrzaccVLMaximumTxPower_Type=Integer32
_BrzaccVLMaximumTxPower_Object=MibScalar
brzaccVLMaximumTxPower=_BrzaccVLMaximumTxPower_Object((1,3,6,1,4,1,12394,1,1,6,24),_BrzaccVLMaximumTxPower_Type())
brzaccVLMaximumTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaximumTxPower.setStatus(_A)
_BrzaccVLCountryCodeParameters_ObjectIdentity=ObjectIdentity
brzaccVLCountryCodeParameters=_BrzaccVLCountryCodeParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,25))
class _BrzaccVLCountryCodeReApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('reapply',1),(_K,2),(_F,255)))
_BrzaccVLCountryCodeReApply_Type.__name__=_C
_BrzaccVLCountryCodeReApply_Object=MibScalar
brzaccVLCountryCodeReApply=_BrzaccVLCountryCodeReApply_Object((1,3,6,1,4,1,12394,1,1,6,25,1),_BrzaccVLCountryCodeReApply_Type())
brzaccVLCountryCodeReApply.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLCountryCodeReApply.setStatus(_A)
_BrzaccVLCountryCodeTable_Object=MibTable
brzaccVLCountryCodeTable=_BrzaccVLCountryCodeTable_Object((1,3,6,1,4,1,12394,1,1,6,25,2))
if mibBuilder.loadTexts:brzaccVLCountryCodeTable.setStatus(_A)
_BrzaccVLCountryCodeEntry_Object=MibTableRow
brzaccVLCountryCodeEntry=_BrzaccVLCountryCodeEntry_Object((1,3,6,1,4,1,12394,1,1,6,25,2,1))
brzaccVLCountryCodeEntry.setIndexNames((0,_E,_An))
if mibBuilder.loadTexts:brzaccVLCountryCodeEntry.setStatus(_A)
class _BrzaccVLCCNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrzaccVLCCNumber_Type.__name__=_C
_BrzaccVLCCNumber_Object=MibTableColumn
brzaccVLCCNumber=_BrzaccVLCCNumber_Object((1,3,6,1,4,1,12394,1,1,6,25,2,1,1),_BrzaccVLCCNumber_Type())
brzaccVLCCNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCNumber.setStatus(_A)
class _BrzaccVLCCName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrzaccVLCCName_Type.__name__=_I
_BrzaccVLCCName_Object=MibTableColumn
brzaccVLCCName=_BrzaccVLCCName_Object((1,3,6,1,4,1,12394,1,1,6,25,2,1,2),_BrzaccVLCCName_Type())
brzaccVLCCName.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCName.setStatus(_A)
class _BrzaccVLCCAuthenticationEncryptionSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLCCAuthenticationEncryptionSupport_Type.__name__=_C
_BrzaccVLCCAuthenticationEncryptionSupport_Object=MibTableColumn
brzaccVLCCAuthenticationEncryptionSupport=_BrzaccVLCCAuthenticationEncryptionSupport_Object((1,3,6,1,4,1,12394,1,1,6,25,2,1,3),_BrzaccVLCCAuthenticationEncryptionSupport_Type())
brzaccVLCCAuthenticationEncryptionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCAuthenticationEncryptionSupport.setStatus(_A)
class _BrzaccVLCCDataEncryptionSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLCCDataEncryptionSupport_Type.__name__=_C
_BrzaccVLCCDataEncryptionSupport_Object=MibTableColumn
brzaccVLCCDataEncryptionSupport=_BrzaccVLCCDataEncryptionSupport_Object((1,3,6,1,4,1,12394,1,1,6,25,2,1,4),_BrzaccVLCCDataEncryptionSupport_Type())
brzaccVLCCDataEncryptionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCDataEncryptionSupport.setStatus(_A)
class _BrzaccVLCCAESEncryptionSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLCCAESEncryptionSupport_Type.__name__=_C
_BrzaccVLCCAESEncryptionSupport_Object=MibTableColumn
brzaccVLCCAESEncryptionSupport=_BrzaccVLCCAESEncryptionSupport_Object((1,3,6,1,4,1,12394,1,1,6,25,2,1,5),_BrzaccVLCCAESEncryptionSupport_Type())
brzaccVLCCAESEncryptionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCAESEncryptionSupport.setStatus(_A)
_BrzaccVLCCParamsTable_Object=MibTable
brzaccVLCCParamsTable=_BrzaccVLCCParamsTable_Object((1,3,6,1,4,1,12394,1,1,6,25,3))
if mibBuilder.loadTexts:brzaccVLCCParamsTable.setStatus(_A)
_BrzaccVLCCParamsEntry_Object=MibTableRow
brzaccVLCCParamsEntry=_BrzaccVLCCParamsEntry_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1))
brzaccVLCCParamsEntry.setIndexNames((0,_E,_Ao),(0,_E,_Ap))
if mibBuilder.loadTexts:brzaccVLCCParamsEntry.setStatus(_A)
class _BrzaccVLCCNumberIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrzaccVLCCNumberIdx_Type.__name__=_C
_BrzaccVLCCNumberIdx_Object=MibTableColumn
brzaccVLCCNumberIdx=_BrzaccVLCCNumberIdx_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,1),_BrzaccVLCCNumberIdx_Type())
brzaccVLCCNumberIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCNumberIdx.setStatus(_A)
class _BrzaccVLCCParamsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_BrzaccVLCCParamsIndex_Type.__name__=_C
_BrzaccVLCCParamsIndex_Object=MibTableColumn
brzaccVLCCParamsIndex=_BrzaccVLCCParamsIndex_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,2),_BrzaccVLCCParamsIndex_Type())
brzaccVLCCParamsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCParamsIndex.setStatus(_A)
_BrzaccVLCCParamsFrequencies_Type=DisplayString
_BrzaccVLCCParamsFrequencies_Object=MibTableColumn
brzaccVLCCParamsFrequencies=_BrzaccVLCCParamsFrequencies_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,3),_BrzaccVLCCParamsFrequencies_Type())
brzaccVLCCParamsFrequencies.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCParamsFrequencies.setStatus(_A)
_BrzaccVLCCAllowedBandwidth_Type=Integer32
_BrzaccVLCCAllowedBandwidth_Object=MibTableColumn
brzaccVLCCAllowedBandwidth=_BrzaccVLCCAllowedBandwidth_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,4),_BrzaccVLCCAllowedBandwidth_Type())
brzaccVLCCAllowedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCAllowedBandwidth.setStatus(_A)
_BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Type=Integer32
_BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Object=MibTableColumn
brzaccVLCCRegulationMaxTxPowerAtAntennaPort=_BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,5),_BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Type())
brzaccVLCCRegulationMaxTxPowerAtAntennaPort.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCRegulationMaxTxPowerAtAntennaPort.setStatus(_A)
_BrzaccVLCCRegulationMaxEIRP_Type=Integer32
_BrzaccVLCCRegulationMaxEIRP_Object=MibTableColumn
brzaccVLCCRegulationMaxEIRP=_BrzaccVLCCRegulationMaxEIRP_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,6),_BrzaccVLCCRegulationMaxEIRP_Type())
brzaccVLCCRegulationMaxEIRP.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCRegulationMaxEIRP.setStatus(_A)
class _BrzaccVLCCMinModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_P,6),(_Q,7),(_R,8)))
_BrzaccVLCCMinModulationLevel_Type.__name__=_C
_BrzaccVLCCMinModulationLevel_Object=MibTableColumn
brzaccVLCCMinModulationLevel=_BrzaccVLCCMinModulationLevel_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,7),_BrzaccVLCCMinModulationLevel_Type())
brzaccVLCCMinModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCMinModulationLevel.setStatus(_A)
class _BrzaccVLCCMaxModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_P,6),(_Q,7),(_R,8)))
_BrzaccVLCCMaxModulationLevel_Type.__name__=_C
_BrzaccVLCCMaxModulationLevel_Object=MibTableColumn
brzaccVLCCMaxModulationLevel=_BrzaccVLCCMaxModulationLevel_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,8),_BrzaccVLCCMaxModulationLevel_Type())
brzaccVLCCMaxModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCMaxModulationLevel.setStatus(_A)
class _BrzaccVLCCBurstModeSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLCCBurstModeSupport_Type.__name__=_C
_BrzaccVLCCBurstModeSupport_Object=MibTableColumn
brzaccVLCCBurstModeSupport=_BrzaccVLCCBurstModeSupport_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,9),_BrzaccVLCCBurstModeSupport_Type())
brzaccVLCCBurstModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCBurstModeSupport.setStatus(_A)
_BrzaccVLCCMaximumBurstDuration_Type=Integer32
_BrzaccVLCCMaximumBurstDuration_Object=MibTableColumn
brzaccVLCCMaximumBurstDuration=_BrzaccVLCCMaximumBurstDuration_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,10),_BrzaccVLCCMaximumBurstDuration_Type())
brzaccVLCCMaximumBurstDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCMaximumBurstDuration.setStatus(_A)
class _BrzaccVLCCDfsSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_BrzaccVLCCDfsSupport_Type.__name__=_C
_BrzaccVLCCDfsSupport_Object=MibTableColumn
brzaccVLCCDfsSupport=_BrzaccVLCCDfsSupport_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,11),_BrzaccVLCCDfsSupport_Type())
brzaccVLCCDfsSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCDfsSupport.setStatus(_A)
class _BrzaccVLCCMinimumHwRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_F,255)))
_BrzaccVLCCMinimumHwRevision_Type.__name__=_C
_BrzaccVLCCMinimumHwRevision_Object=MibTableColumn
brzaccVLCCMinimumHwRevision=_BrzaccVLCCMinimumHwRevision_Object((1,3,6,1,4,1,12394,1,1,6,25,3,1,12),_BrzaccVLCCMinimumHwRevision_Type())
brzaccVLCCMinimumHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCCMinimumHwRevision.setStatus(_A)
_BrzaccVLCountryCodeSelect_Type=Integer32
_BrzaccVLCountryCodeSelect_Object=MibScalar
brzaccVLCountryCodeSelect=_BrzaccVLCountryCodeSelect_Object((1,3,6,1,4,1,12394,1,1,6,25,4),_BrzaccVLCountryCodeSelect_Type())
brzaccVLCountryCodeSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLCountryCodeSelect.setStatus(_A)
_BrzaccVLNoiseImmunityParameters_ObjectIdentity=ObjectIdentity
brzaccVLNoiseImmunityParameters=_BrzaccVLNoiseImmunityParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,26))
class _BrzaccVLNoiseImmunityAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('manual',1),(_n,2),(_F,255)))
_BrzaccVLNoiseImmunityAlgorithm_Type.__name__=_C
_BrzaccVLNoiseImmunityAlgorithm_Object=MibScalar
brzaccVLNoiseImmunityAlgorithm=_BrzaccVLNoiseImmunityAlgorithm_Object((1,3,6,1,4,1,12394,1,1,6,26,1),_BrzaccVLNoiseImmunityAlgorithm_Type())
brzaccVLNoiseImmunityAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNoiseImmunityAlgorithm.setStatus(_A)
class _BrzaccVLNoiseImmunityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4),ValueRangeConstraint(255,255))
_BrzaccVLNoiseImmunityLevel_Type.__name__=_C
_BrzaccVLNoiseImmunityLevel_Object=MibScalar
brzaccVLNoiseImmunityLevel=_BrzaccVLNoiseImmunityLevel_Object((1,3,6,1,4,1,12394,1,1,6,26,2),_BrzaccVLNoiseImmunityLevel_Type())
brzaccVLNoiseImmunityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNoiseImmunityLevel.setStatus(_A)
class _BrzaccVLSpuriousImmunityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_BrzaccVLSpuriousImmunityLevel_Type.__name__=_C
_BrzaccVLSpuriousImmunityLevel_Object=MibScalar
brzaccVLSpuriousImmunityLevel=_BrzaccVLSpuriousImmunityLevel_Object((1,3,6,1,4,1,12394,1,1,6,26,3),_BrzaccVLSpuriousImmunityLevel_Type())
brzaccVLSpuriousImmunityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSpuriousImmunityLevel.setStatus(_A)
class _BrzaccVLOFDMWeakSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_F,255)))
_BrzaccVLOFDMWeakSignal_Type.__name__=_C
_BrzaccVLOFDMWeakSignal_Object=MibScalar
brzaccVLOFDMWeakSignal=_BrzaccVLOFDMWeakSignal_Object((1,3,6,1,4,1,12394,1,1,6,26,4),_BrzaccVLOFDMWeakSignal_Type())
brzaccVLOFDMWeakSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLOFDMWeakSignal.setStatus(_A)
class _BrzaccVLPulseDetectionSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_BrzaccVLPulseDetectionSensitivity_Type.__name__=_C
_BrzaccVLPulseDetectionSensitivity_Object=MibScalar
brzaccVLPulseDetectionSensitivity=_BrzaccVLPulseDetectionSensitivity_Object((1,3,6,1,4,1,12394,1,1,6,26,5),_BrzaccVLPulseDetectionSensitivity_Type())
brzaccVLPulseDetectionSensitivity.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLPulseDetectionSensitivity.setStatus(_A)
_BrzaccVLNewTransmitPowerTable_Object=MibTable
brzaccVLNewTransmitPowerTable=_BrzaccVLNewTransmitPowerTable_Object((1,3,6,1,4,1,12394,1,1,6,27))
if mibBuilder.loadTexts:brzaccVLNewTransmitPowerTable.setStatus(_A)
_BrzaccVLNewTransmitPowerEntry_Object=MibTableRow
brzaccVLNewTransmitPowerEntry=_BrzaccVLNewTransmitPowerEntry_Object((1,3,6,1,4,1,12394,1,1,6,27,1))
brzaccVLNewTransmitPowerEntry.setIndexNames((0,_E,_Aq))
if mibBuilder.loadTexts:brzaccVLNewTransmitPowerEntry.setStatus(_A)
class _BrzaccVLNewModulationLevelIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BrzaccVLNewModulationLevelIdx_Type.__name__=_C
_BrzaccVLNewModulationLevelIdx_Object=MibTableColumn
brzaccVLNewModulationLevelIdx=_BrzaccVLNewModulationLevelIdx_Object((1,3,6,1,4,1,12394,1,1,6,27,1,1),_BrzaccVLNewModulationLevelIdx_Type())
brzaccVLNewModulationLevelIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewModulationLevelIdx.setStatus(_A)
_BrzaccVLNewMaximumTxPowerRange_Type=DisplayString
_BrzaccVLNewMaximumTxPowerRange_Object=MibTableColumn
brzaccVLNewMaximumTxPowerRange=_BrzaccVLNewMaximumTxPowerRange_Object((1,3,6,1,4,1,12394,1,1,6,27,1,2),_BrzaccVLNewMaximumTxPowerRange_Type())
brzaccVLNewMaximumTxPowerRange.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewMaximumTxPowerRange.setStatus(_A)
_BrzaccVLNewTxPower_Type=DisplayString
_BrzaccVLNewTxPower_Object=MibTableColumn
brzaccVLNewTxPower=_BrzaccVLNewTxPower_Object((1,3,6,1,4,1,12394,1,1,6,27,1,3),_BrzaccVLNewTxPower_Type())
brzaccVLNewTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewTxPower.setStatus(_A)
_BrzaccVLNewCurrentTxPower_Type=DisplayString
_BrzaccVLNewCurrentTxPower_Object=MibTableColumn
brzaccVLNewCurrentTxPower=_BrzaccVLNewCurrentTxPower_Object((1,3,6,1,4,1,12394,1,1,6,27,1,4),_BrzaccVLNewCurrentTxPower_Type())
brzaccVLNewCurrentTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewCurrentTxPower.setStatus(_A)
_BrzaccVLNewMaximumTransmitPowerTable_Object=MibTable
brzaccVLNewMaximumTransmitPowerTable=_BrzaccVLNewMaximumTransmitPowerTable_Object((1,3,6,1,4,1,12394,1,1,6,28))
if mibBuilder.loadTexts:brzaccVLNewMaximumTransmitPowerTable.setStatus(_A)
_BrzaccVLNewMaximumTransmitPowerEntry_Object=MibTableRow
brzaccVLNewMaximumTransmitPowerEntry=_BrzaccVLNewMaximumTransmitPowerEntry_Object((1,3,6,1,4,1,12394,1,1,6,28,1))
brzaccVLNewMaximumTransmitPowerEntry.setIndexNames((0,_E,_Ar))
if mibBuilder.loadTexts:brzaccVLNewMaximumTransmitPowerEntry.setStatus(_A)
class _BrzaccVLNewMaxModulationLevelIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BrzaccVLNewMaxModulationLevelIdx_Type.__name__=_C
_BrzaccVLNewMaxModulationLevelIdx_Object=MibTableColumn
brzaccVLNewMaxModulationLevelIdx=_BrzaccVLNewMaxModulationLevelIdx_Object((1,3,6,1,4,1,12394,1,1,6,28,1,1),_BrzaccVLNewMaxModulationLevelIdx_Type())
brzaccVLNewMaxModulationLevelIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewMaxModulationLevelIdx.setStatus(_A)
_BrzaccVLNewDefinedMaximumTxPowerRange_Type=DisplayString
_BrzaccVLNewDefinedMaximumTxPowerRange_Object=MibTableColumn
brzaccVLNewDefinedMaximumTxPowerRange=_BrzaccVLNewDefinedMaximumTxPowerRange_Object((1,3,6,1,4,1,12394,1,1,6,28,1,2),_BrzaccVLNewDefinedMaximumTxPowerRange_Type())
brzaccVLNewDefinedMaximumTxPowerRange.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewDefinedMaximumTxPowerRange.setStatus(_A)
_BrzaccVLNewMaxTxPower_Type=DisplayString
_BrzaccVLNewMaxTxPower_Object=MibTableColumn
brzaccVLNewMaxTxPower=_BrzaccVLNewMaxTxPower_Object((1,3,6,1,4,1,12394,1,1,6,28,1,3),_BrzaccVLNewMaxTxPower_Type())
brzaccVLNewMaxTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewMaxTxPower.setStatus(_A)
_BrzaccVLNoiseFloorCalculationParameters_ObjectIdentity=ObjectIdentity
brzaccVLNoiseFloorCalculationParameters=_BrzaccVLNoiseFloorCalculationParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,29))
class _BrzaccVLNoiseFloorCalculationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),('forced',2),('minimumlevel',3)))
_BrzaccVLNoiseFloorCalculationMode_Type.__name__=_C
_BrzaccVLNoiseFloorCalculationMode_Object=MibScalar
brzaccVLNoiseFloorCalculationMode=_BrzaccVLNoiseFloorCalculationMode_Object((1,3,6,1,4,1,12394,1,1,6,29,1),_BrzaccVLNoiseFloorCalculationMode_Type())
brzaccVLNoiseFloorCalculationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNoiseFloorCalculationMode.setStatus(_A)
_BrzaccVLNoiseFloorForcedValue_Type=Integer32
_BrzaccVLNoiseFloorForcedValue_Object=MibScalar
brzaccVLNoiseFloorForcedValue=_BrzaccVLNoiseFloorForcedValue_Object((1,3,6,1,4,1,12394,1,1,6,29,2),_BrzaccVLNoiseFloorForcedValue_Type())
brzaccVLNoiseFloorForcedValue.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNoiseFloorForcedValue.setStatus(_A)
_BrzaccVLNoiseFloorCalibrationParameters_ObjectIdentity=ObjectIdentity
brzaccVLNoiseFloorCalibrationParameters=_BrzaccVLNoiseFloorCalibrationParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,30))
class _BrzaccVLNoiseFloorRunCalibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('run',1),(_K,2),(_F,255)))
_BrzaccVLNoiseFloorRunCalibration_Type.__name__=_C
_BrzaccVLNoiseFloorRunCalibration_Object=MibScalar
brzaccVLNoiseFloorRunCalibration=_BrzaccVLNoiseFloorRunCalibration_Object((1,3,6,1,4,1,12394,1,1,6,30,1),_BrzaccVLNoiseFloorRunCalibration_Type())
brzaccVLNoiseFloorRunCalibration.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNoiseFloorRunCalibration.setStatus(_A)
class _BrzaccVLNoiseFloorFieldCalibrationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_BrzaccVLNoiseFloorFieldCalibrationStatus_Type.__name__=_C
_BrzaccVLNoiseFloorFieldCalibrationStatus_Object=MibScalar
brzaccVLNoiseFloorFieldCalibrationStatus=_BrzaccVLNoiseFloorFieldCalibrationStatus_Object((1,3,6,1,4,1,12394,1,1,6,30,2),_BrzaccVLNoiseFloorFieldCalibrationStatus_Type())
brzaccVLNoiseFloorFieldCalibrationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNoiseFloorFieldCalibrationStatus.setStatus(_A)
class _BrzaccVLNoiseFloorLastFieldCalibrationResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('passed',1),(_u,2),(_m,3)))
_BrzaccVLNoiseFloorLastFieldCalibrationResult_Type.__name__=_C
_BrzaccVLNoiseFloorLastFieldCalibrationResult_Object=MibScalar
brzaccVLNoiseFloorLastFieldCalibrationResult=_BrzaccVLNoiseFloorLastFieldCalibrationResult_Object((1,3,6,1,4,1,12394,1,1,6,30,3),_BrzaccVLNoiseFloorLastFieldCalibrationResult_Type())
brzaccVLNoiseFloorLastFieldCalibrationResult.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNoiseFloorLastFieldCalibrationResult.setStatus(_A)
class _BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,10,20,40)));namedValues=NamedValues(*((_m,0),('bandwidth-5MHz',5),('bandwidth-10MHz',10),('bandwidth-20MHz',20),('bandwidth-40MHz',40)))
_BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Type.__name__=_C
_BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Object=MibScalar
brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration=_BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Object((1,3,6,1,4,1,12394,1,1,6,30,4),_BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Type())
brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration.setStatus(_A)
class _BrzaccVLNoiseFloorAvailableCalibrationOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notCalibrated',1),('factoryOnly',2),('fieldOnly',3),('factoryAndField',4)))
_BrzaccVLNoiseFloorAvailableCalibrationOptions_Type.__name__=_C
_BrzaccVLNoiseFloorAvailableCalibrationOptions_Object=MibScalar
brzaccVLNoiseFloorAvailableCalibrationOptions=_BrzaccVLNoiseFloorAvailableCalibrationOptions_Object((1,3,6,1,4,1,12394,1,1,6,30,5),_BrzaccVLNoiseFloorAvailableCalibrationOptions_Type())
brzaccVLNoiseFloorAvailableCalibrationOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNoiseFloorAvailableCalibrationOptions.setStatus(_A)
class _BrzaccVLNoiseFloorUseCalibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),('fieldCalibration',2),('factoryCalibration',3)))
_BrzaccVLNoiseFloorUseCalibration_Type.__name__=_C
_BrzaccVLNoiseFloorUseCalibration_Object=MibScalar
brzaccVLNoiseFloorUseCalibration=_BrzaccVLNoiseFloorUseCalibration_Object((1,3,6,1,4,1,12394,1,1,6,30,6),_BrzaccVLNoiseFloorUseCalibration_Type())
brzaccVLNoiseFloorUseCalibration.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNoiseFloorUseCalibration.setStatus(_A)
_BrzaccVLInterferenceMitigationParameters_ObjectIdentity=ObjectIdentity
brzaccVLInterferenceMitigationParameters=_BrzaccVLInterferenceMitigationParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,6,31))
_BrzaccVLInterferenceMitigationChannelScanPeriod_Type=Integer32
_BrzaccVLInterferenceMitigationChannelScanPeriod_Object=MibScalar
brzaccVLInterferenceMitigationChannelScanPeriod=_BrzaccVLInterferenceMitigationChannelScanPeriod_Object((1,3,6,1,4,1,12394,1,1,6,31,1),_BrzaccVLInterferenceMitigationChannelScanPeriod_Type())
brzaccVLInterferenceMitigationChannelScanPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationChannelScanPeriod.setStatus(_A)
_BrzaccVLInterferenceMitigationAutomaticScanPeriod_Type=Integer32
_BrzaccVLInterferenceMitigationAutomaticScanPeriod_Object=MibScalar
brzaccVLInterferenceMitigationAutomaticScanPeriod=_BrzaccVLInterferenceMitigationAutomaticScanPeriod_Object((1,3,6,1,4,1,12394,1,1,6,31,2),_BrzaccVLInterferenceMitigationAutomaticScanPeriod_Type())
brzaccVLInterferenceMitigationAutomaticScanPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationAutomaticScanPeriod.setStatus(_A)
class _BrzaccVLInterferenceMitigationScanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('clearChannelAndAutomaticNoiseFloorSelection',1),('automaticNoiseFloorSelectionOnly',2),('clearChannelSelectionOnly',3),('statisticsOnly',4)))
_BrzaccVLInterferenceMitigationScanType_Type.__name__=_C
_BrzaccVLInterferenceMitigationScanType_Object=MibScalar
brzaccVLInterferenceMitigationScanType=_BrzaccVLInterferenceMitigationScanType_Object((1,3,6,1,4,1,12394,1,1,6,31,3),_BrzaccVLInterferenceMitigationScanType_Type())
brzaccVLInterferenceMitigationScanType.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationScanType.setStatus(_A)
class _BrzaccVLInterferenceMitigationScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('optimizePerformanceForMinimumDesiredDistance',1),('optimizeDistanceForMinimumDesiredPerformance',2)))
_BrzaccVLInterferenceMitigationScanMode_Type.__name__=_C
_BrzaccVLInterferenceMitigationScanMode_Object=MibScalar
brzaccVLInterferenceMitigationScanMode=_BrzaccVLInterferenceMitigationScanMode_Object((1,3,6,1,4,1,12394,1,1,6,31,4),_BrzaccVLInterferenceMitigationScanMode_Type())
brzaccVLInterferenceMitigationScanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationScanMode.setStatus(_A)
_BrzaccVLInterferenceMitigationDistance_Type=Integer32
_BrzaccVLInterferenceMitigationDistance_Object=MibScalar
brzaccVLInterferenceMitigationDistance=_BrzaccVLInterferenceMitigationDistance_Object((1,3,6,1,4,1,12394,1,1,6,31,5),_BrzaccVLInterferenceMitigationDistance_Type())
brzaccVLInterferenceMitigationDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationDistance.setStatus(_A)
_BrzaccVLInterferenceMitigationThroughput_Type=Integer32
_BrzaccVLInterferenceMitigationThroughput_Object=MibScalar
brzaccVLInterferenceMitigationThroughput=_BrzaccVLInterferenceMitigationThroughput_Object((1,3,6,1,4,1,12394,1,1,6,31,6),_BrzaccVLInterferenceMitigationThroughput_Type())
brzaccVLInterferenceMitigationThroughput.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationThroughput.setStatus(_A)
class _BrzaccVLInterferenceMitigationActivation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_Aj,2),('notAvailable',3)))
_BrzaccVLInterferenceMitigationActivation_Type.__name__=_C
_BrzaccVLInterferenceMitigationActivation_Object=MibScalar
brzaccVLInterferenceMitigationActivation=_BrzaccVLInterferenceMitigationActivation_Object((1,3,6,1,4,1,12394,1,1,6,31,8),_BrzaccVLInterferenceMitigationActivation_Type())
brzaccVLInterferenceMitigationActivation.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationActivation.setStatus(_A)
class _BrzaccVLInterferenceMitigationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_x,1),(_y,2),(_Ak,3)))
_BrzaccVLInterferenceMitigationStatus_Type.__name__=_C
_BrzaccVLInterferenceMitigationStatus_Object=MibScalar
brzaccVLInterferenceMitigationStatus=_BrzaccVLInterferenceMitigationStatus_Object((1,3,6,1,4,1,12394,1,1,6,31,9),_BrzaccVLInterferenceMitigationStatus_Type())
brzaccVLInterferenceMitigationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationStatus.setStatus(_A)
class _BrzaccVLInterferenceMitigationDeleteStatisticsFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('delete',2)))
_BrzaccVLInterferenceMitigationDeleteStatisticsFile_Type.__name__=_C
_BrzaccVLInterferenceMitigationDeleteStatisticsFile_Object=MibScalar
brzaccVLInterferenceMitigationDeleteStatisticsFile=_BrzaccVLInterferenceMitigationDeleteStatisticsFile_Object((1,3,6,1,4,1,12394,1,1,6,31,10),_BrzaccVLInterferenceMitigationDeleteStatisticsFile_Type())
brzaccVLInterferenceMitigationDeleteStatisticsFile.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationDeleteStatisticsFile.setStatus(_A)
class _BrzaccVLInterferenceMitigationModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('typeLOS',1),('typenLOS',2),(_As,3)))
_BrzaccVLInterferenceMitigationModel_Type.__name__=_C
_BrzaccVLInterferenceMitigationModel_Object=MibScalar
brzaccVLInterferenceMitigationModel=_BrzaccVLInterferenceMitigationModel_Object((1,3,6,1,4,1,12394,1,1,6,31,11),_BrzaccVLInterferenceMitigationModel_Type())
brzaccVLInterferenceMitigationModel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationModel.setStatus(_A)
_BrzaccVLInterferenceMitigationScanTime_Type=Integer32
_BrzaccVLInterferenceMitigationScanTime_Object=MibScalar
brzaccVLInterferenceMitigationScanTime=_BrzaccVLInterferenceMitigationScanTime_Object((1,3,6,1,4,1,12394,1,1,6,31,12),_BrzaccVLInterferenceMitigationScanTime_Type())
brzaccVLInterferenceMitigationScanTime.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationScanTime.setStatus(_A)
_BrzaccVLInterferenceMitigationAUheight_Type=Integer32
_BrzaccVLInterferenceMitigationAUheight_Object=MibScalar
brzaccVLInterferenceMitigationAUheight=_BrzaccVLInterferenceMitigationAUheight_Object((1,3,6,1,4,1,12394,1,1,6,31,13),_BrzaccVLInterferenceMitigationAUheight_Type())
brzaccVLInterferenceMitigationAUheight.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationAUheight.setStatus(_A)
_BrzaccVLInterferenceMitigationAntennaGain_Type=Integer32
_BrzaccVLInterferenceMitigationAntennaGain_Object=MibScalar
brzaccVLInterferenceMitigationAntennaGain=_BrzaccVLInterferenceMitigationAntennaGain_Object((1,3,6,1,4,1,12394,1,1,6,31,14),_BrzaccVLInterferenceMitigationAntennaGain_Type())
brzaccVLInterferenceMitigationAntennaGain.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationAntennaGain.setStatus(_A)
_BrzaccVLInterferenceMitigationMaxModulation_Type=Integer32
_BrzaccVLInterferenceMitigationMaxModulation_Object=MibScalar
brzaccVLInterferenceMitigationMaxModulation=_BrzaccVLInterferenceMitigationMaxModulation_Object((1,3,6,1,4,1,12394,1,1,6,31,15),_BrzaccVLInterferenceMitigationMaxModulation_Type())
brzaccVLInterferenceMitigationMaxModulation.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationMaxModulation.setStatus(_A)
class _BrzaccVLInterferenceMitigationKeepLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_BrzaccVLInterferenceMitigationKeepLink_Type.__name__=_C
_BrzaccVLInterferenceMitigationKeepLink_Object=MibScalar
brzaccVLInterferenceMitigationKeepLink=_BrzaccVLInterferenceMitigationKeepLink_Object((1,3,6,1,4,1,12394,1,1,6,31,16),_BrzaccVLInterferenceMitigationKeepLink_Type())
brzaccVLInterferenceMitigationKeepLink.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationKeepLink.setStatus(_A)
_BrzaccVLInterferenceMitigationOutputTable_Object=MibTable
brzaccVLInterferenceMitigationOutputTable=_BrzaccVLInterferenceMitigationOutputTable_Object((1,3,6,1,4,1,12394,1,1,6,31,17))
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputTable.setStatus(_A)
_BrzaccVLInterferenceMitigationOutputEntry_Object=MibTableRow
brzaccVLInterferenceMitigationOutputEntry=_BrzaccVLInterferenceMitigationOutputEntry_Object((1,3,6,1,4,1,12394,1,1,6,31,17,1))
brzaccVLInterferenceMitigationOutputEntry.setIndexNames((0,_E,_At))
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputEntry.setStatus(_A)
class _BrzaccVLInterferenceMitigationOutputFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(905,925))
_BrzaccVLInterferenceMitigationOutputFrequency_Type.__name__=_C
_BrzaccVLInterferenceMitigationOutputFrequency_Object=MibTableColumn
brzaccVLInterferenceMitigationOutputFrequency=_BrzaccVLInterferenceMitigationOutputFrequency_Object((1,3,6,1,4,1,12394,1,1,6,31,17,1,1),_BrzaccVLInterferenceMitigationOutputFrequency_Type())
brzaccVLInterferenceMitigationOutputFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputFrequency.setStatus(_A)
class _BrzaccVLInterferenceMitigationOutputScanningType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('typeCCSandANFS',1),('typeANFS',2),('typeCCS',3),('typeStatistics',4)))
_BrzaccVLInterferenceMitigationOutputScanningType_Type.__name__=_C
_BrzaccVLInterferenceMitigationOutputScanningType_Object=MibTableColumn
brzaccVLInterferenceMitigationOutputScanningType=_BrzaccVLInterferenceMitigationOutputScanningType_Object((1,3,6,1,4,1,12394,1,1,6,31,17,1,2),_BrzaccVLInterferenceMitigationOutputScanningType_Type())
brzaccVLInterferenceMitigationOutputScanningType.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputScanningType.setStatus(_A)
class _BrzaccVLInterferenceMitigationOutputInstallationModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('typeLOS',1),('typeNearLOS',2),(_As,3)))
_BrzaccVLInterferenceMitigationOutputInstallationModel_Type.__name__=_C
_BrzaccVLInterferenceMitigationOutputInstallationModel_Object=MibTableColumn
brzaccVLInterferenceMitigationOutputInstallationModel=_BrzaccVLInterferenceMitigationOutputInstallationModel_Object((1,3,6,1,4,1,12394,1,1,6,31,17,1,3),_BrzaccVLInterferenceMitigationOutputInstallationModel_Type())
brzaccVLInterferenceMitigationOutputInstallationModel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputInstallationModel.setStatus(_A)
class _BrzaccVLInterferenceMitigationOutputNoiseFloor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-55))
_BrzaccVLInterferenceMitigationOutputNoiseFloor_Type.__name__=_C
_BrzaccVLInterferenceMitigationOutputNoiseFloor_Object=MibTableColumn
brzaccVLInterferenceMitigationOutputNoiseFloor=_BrzaccVLInterferenceMitigationOutputNoiseFloor_Object((1,3,6,1,4,1,12394,1,1,6,31,17,1,4),_BrzaccVLInterferenceMitigationOutputNoiseFloor_Type())
brzaccVLInterferenceMitigationOutputNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputNoiseFloor.setStatus(_A)
_BrzaccVLInterferenceMitigationOutputDistance_Type=Integer32
_BrzaccVLInterferenceMitigationOutputDistance_Object=MibTableColumn
brzaccVLInterferenceMitigationOutputDistance=_BrzaccVLInterferenceMitigationOutputDistance_Object((1,3,6,1,4,1,12394,1,1,6,31,17,1,5),_BrzaccVLInterferenceMitigationOutputDistance_Type())
brzaccVLInterferenceMitigationOutputDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputDistance.setStatus(_A)
_BrzaccVLInterferenceMitigationOutputPerformance_Type=Integer32
_BrzaccVLInterferenceMitigationOutputPerformance_Object=MibTableColumn
brzaccVLInterferenceMitigationOutputPerformance=_BrzaccVLInterferenceMitigationOutputPerformance_Object((1,3,6,1,4,1,12394,1,1,6,31,17,1,6),_BrzaccVLInterferenceMitigationOutputPerformance_Type())
brzaccVLInterferenceMitigationOutputPerformance.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLInterferenceMitigationOutputPerformance.setStatus(_A)
_BrzaccVLBeaconPeriod_Type=Integer32
_BrzaccVLBeaconPeriod_Object=MibScalar
brzaccVLBeaconPeriod=_BrzaccVLBeaconPeriod_Object((1,3,6,1,4,1,12394,1,1,6,32),_BrzaccVLBeaconPeriod_Type())
brzaccVLBeaconPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLBeaconPeriod.setStatus(_A)
_BrzaccVLMaxBeaconsLost_Type=Integer32
_BrzaccVLMaxBeaconsLost_Object=MibScalar
brzaccVLMaxBeaconsLost=_BrzaccVLMaxBeaconsLost_Object((1,3,6,1,4,1,12394,1,1,6,33),_BrzaccVLMaxBeaconsLost_Type())
brzaccVLMaxBeaconsLost.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaxBeaconsLost.setStatus(_A)
_BrzaccVLServiceParameters_ObjectIdentity=ObjectIdentity
brzaccVLServiceParameters=_BrzaccVLServiceParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7))
_BrzaccVLMirDownlink_Type=Integer32
_BrzaccVLMirDownlink_Object=MibScalar
brzaccVLMirDownlink=_BrzaccVLMirDownlink_Object((1,3,6,1,4,1,12394,1,1,7,2),_BrzaccVLMirDownlink_Type())
brzaccVLMirDownlink.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMirDownlink.setStatus(_A)
_BrzaccVLMirUplink_Type=Integer32
_BrzaccVLMirUplink_Object=MibScalar
brzaccVLMirUplink=_BrzaccVLMirUplink_Object((1,3,6,1,4,1,12394,1,1,7,3),_BrzaccVLMirUplink_Type())
brzaccVLMirUplink.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMirUplink.setStatus(_A)
_BrzaccVLCirDownlink_Type=Integer32
_BrzaccVLCirDownlink_Object=MibScalar
brzaccVLCirDownlink=_BrzaccVLCirDownlink_Object((1,3,6,1,4,1,12394,1,1,7,4),_BrzaccVLCirDownlink_Type())
brzaccVLCirDownlink.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLCirDownlink.setStatus(_A)
_BrzaccVLCirUplink_Type=Integer32
_BrzaccVLCirUplink_Object=MibScalar
brzaccVLCirUplink=_BrzaccVLCirUplink_Object((1,3,6,1,4,1,12394,1,1,7,5),_BrzaccVLCirUplink_Type())
brzaccVLCirUplink.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLCirUplink.setStatus(_A)
_BrzaccVLMaxDelay_Type=Integer32
_BrzaccVLMaxDelay_Object=MibScalar
brzaccVLMaxDelay=_BrzaccVLMaxDelay_Object((1,3,6,1,4,1,12394,1,1,7,6),_BrzaccVLMaxDelay_Type())
brzaccVLMaxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaxDelay.setStatus(_A)
_BrzaccVLMaxBurstDuration_Type=Integer32
_BrzaccVLMaxBurstDuration_Object=MibScalar
brzaccVLMaxBurstDuration=_BrzaccVLMaxBurstDuration_Object((1,3,6,1,4,1,12394,1,1,7,7),_BrzaccVLMaxBurstDuration_Type())
brzaccVLMaxBurstDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaxBurstDuration.setStatus(_A)
_BrzaccVLGracefulDegradationLimit_Type=Integer32
_BrzaccVLGracefulDegradationLimit_Object=MibScalar
brzaccVLGracefulDegradationLimit=_BrzaccVLGracefulDegradationLimit_Object((1,3,6,1,4,1,12394,1,1,7,8),_BrzaccVLGracefulDegradationLimit_Type())
brzaccVLGracefulDegradationLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLGracefulDegradationLimit.setStatus(_A)
class _BrzaccVLMirOnlyOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLMirOnlyOption_Type.__name__=_C
_BrzaccVLMirOnlyOption_Object=MibScalar
brzaccVLMirOnlyOption=_BrzaccVLMirOnlyOption_Object((1,3,6,1,4,1,12394,1,1,7,9),_BrzaccVLMirOnlyOption_Type())
brzaccVLMirOnlyOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMirOnlyOption.setStatus(_A)
_BrzaccVLTrafficPrioritization_ObjectIdentity=ObjectIdentity
brzaccVLTrafficPrioritization=_BrzaccVLTrafficPrioritization_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10))
_BrzaccVLTrafficPriVLAN_ObjectIdentity=ObjectIdentity
brzaccVLTrafficPriVLAN=_BrzaccVLTrafficPriVLAN_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10,1))
class _BrzaccVLVLANPriorityThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_BrzaccVLVLANPriorityThreshold_Type.__name__=_C
_BrzaccVLVLANPriorityThreshold_Object=MibScalar
brzaccVLVLANPriorityThreshold=_BrzaccVLVLANPriorityThreshold_Object((1,3,6,1,4,1,12394,1,1,7,10,1,1),_BrzaccVLVLANPriorityThreshold_Type())
brzaccVLVLANPriorityThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLVLANPriorityThreshold.setStatus(_A)
_BrzaccVLTrafficPriIPToS_ObjectIdentity=ObjectIdentity
brzaccVLTrafficPriIPToS=_BrzaccVLTrafficPriIPToS_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10,2))
class _BrzaccVLToSPrioritizationOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('ipPrecedence',2),('dSCP',3)))
_BrzaccVLToSPrioritizationOption_Type.__name__=_C
_BrzaccVLToSPrioritizationOption_Object=MibScalar
brzaccVLToSPrioritizationOption=_BrzaccVLToSPrioritizationOption_Object((1,3,6,1,4,1,12394,1,1,7,10,2,1),_BrzaccVLToSPrioritizationOption_Type())
brzaccVLToSPrioritizationOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLToSPrioritizationOption.setStatus(_A)
class _BrzaccVLIPPrecedenceThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrzaccVLIPPrecedenceThreshold_Type.__name__=_C
_BrzaccVLIPPrecedenceThreshold_Object=MibScalar
brzaccVLIPPrecedenceThreshold=_BrzaccVLIPPrecedenceThreshold_Object((1,3,6,1,4,1,12394,1,1,7,10,2,2),_BrzaccVLIPPrecedenceThreshold_Type())
brzaccVLIPPrecedenceThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLIPPrecedenceThreshold.setStatus(_A)
class _BrzaccVLIPDSCPThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_BrzaccVLIPDSCPThreshold_Type.__name__=_C
_BrzaccVLIPDSCPThreshold_Object=MibScalar
brzaccVLIPDSCPThreshold=_BrzaccVLIPDSCPThreshold_Object((1,3,6,1,4,1,12394,1,1,7,10,2,3),_BrzaccVLIPDSCPThreshold_Type())
brzaccVLIPDSCPThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLIPDSCPThreshold.setStatus(_A)
_BrzaccVLTrafficPriUdpTcpPortRange_ObjectIdentity=ObjectIdentity
brzaccVLTrafficPriUdpTcpPortRange=_BrzaccVLTrafficPriUdpTcpPortRange_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10,3))
class _BrzaccVLUdpTcpPortRangePrioritizationOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('udpOnly',2),('tcpOnly',3),('udpANDtcp',4)))
_BrzaccVLUdpTcpPortRangePrioritizationOption_Type.__name__=_C
_BrzaccVLUdpTcpPortRangePrioritizationOption_Object=MibScalar
brzaccVLUdpTcpPortRangePrioritizationOption=_BrzaccVLUdpTcpPortRangePrioritizationOption_Object((1,3,6,1,4,1,12394,1,1,7,10,3,1),_BrzaccVLUdpTcpPortRangePrioritizationOption_Type())
brzaccVLUdpTcpPortRangePrioritizationOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUdpTcpPortRangePrioritizationOption.setStatus(_A)
_BrzaccVLUdpPortRangeConfig_ObjectIdentity=ObjectIdentity
brzaccVLUdpPortRangeConfig=_BrzaccVLUdpPortRangeConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10,3,2))
class _BrzaccVLUdpPortPriRTPRTCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Au,1),('rtpOnly',2)))
_BrzaccVLUdpPortPriRTPRTCP_Type.__name__=_C
_BrzaccVLUdpPortPriRTPRTCP_Object=MibScalar
brzaccVLUdpPortPriRTPRTCP=_BrzaccVLUdpPortPriRTPRTCP_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,1),_BrzaccVLUdpPortPriRTPRTCP_Type())
brzaccVLUdpPortPriRTPRTCP.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUdpPortPriRTPRTCP.setStatus(_A)
_BrzaccVLUdpPortRangeNum_Type=Integer32
_BrzaccVLUdpPortRangeNum_Object=MibScalar
brzaccVLUdpPortRangeNum=_BrzaccVLUdpPortRangeNum_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,2),_BrzaccVLUdpPortRangeNum_Type())
brzaccVLUdpPortRangeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUdpPortRangeNum.setStatus(_A)
_BrzaccVLUdpPortRangeTable_Object=MibTable
brzaccVLUdpPortRangeTable=_BrzaccVLUdpPortRangeTable_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,3))
if mibBuilder.loadTexts:brzaccVLUdpPortRangeTable.setStatus(_A)
_BrzaccVLUdpPortRangeEntry_Object=MibTableRow
brzaccVLUdpPortRangeEntry=_BrzaccVLUdpPortRangeEntry_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,3,1))
brzaccVLUdpPortRangeEntry.setIndexNames((0,_E,_Av))
if mibBuilder.loadTexts:brzaccVLUdpPortRangeEntry.setStatus(_A)
class _BrzaccVLUdpPortRangeStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrzaccVLUdpPortRangeStart_Type.__name__=_C
_BrzaccVLUdpPortRangeStart_Object=MibTableColumn
brzaccVLUdpPortRangeStart=_BrzaccVLUdpPortRangeStart_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,3,1,1),_BrzaccVLUdpPortRangeStart_Type())
brzaccVLUdpPortRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUdpPortRangeStart.setStatus(_A)
class _BrzaccVLUdpPortRangeEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrzaccVLUdpPortRangeEnd_Type.__name__=_C
_BrzaccVLUdpPortRangeEnd_Object=MibTableColumn
brzaccVLUdpPortRangeEnd=_BrzaccVLUdpPortRangeEnd_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,3,1,2),_BrzaccVLUdpPortRangeEnd_Type())
brzaccVLUdpPortRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUdpPortRangeEnd.setStatus(_A)
class _BrzaccVLUdpPortRangeIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_BrzaccVLUdpPortRangeIdx_Type.__name__=_C
_BrzaccVLUdpPortRangeIdx_Object=MibTableColumn
brzaccVLUdpPortRangeIdx=_BrzaccVLUdpPortRangeIdx_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,3,1,3),_BrzaccVLUdpPortRangeIdx_Type())
brzaccVLUdpPortRangeIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUdpPortRangeIdx.setStatus(_A)
class _BrzaccVLUdpPortRangeAdd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_BrzaccVLUdpPortRangeAdd_Type.__name__=_I
_BrzaccVLUdpPortRangeAdd_Object=MibScalar
brzaccVLUdpPortRangeAdd=_BrzaccVLUdpPortRangeAdd_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,4),_BrzaccVLUdpPortRangeAdd_Type())
brzaccVLUdpPortRangeAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUdpPortRangeAdd.setStatus(_A)
class _BrzaccVLUdpPortRangeDelete_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_BrzaccVLUdpPortRangeDelete_Type.__name__=_I
_BrzaccVLUdpPortRangeDelete_Object=MibScalar
brzaccVLUdpPortRangeDelete=_BrzaccVLUdpPortRangeDelete_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,5),_BrzaccVLUdpPortRangeDelete_Type())
brzaccVLUdpPortRangeDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUdpPortRangeDelete.setStatus(_A)
class _BrzaccVLUdpPortRangeDeleteAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_L,2)))
_BrzaccVLUdpPortRangeDeleteAll_Type.__name__=_C
_BrzaccVLUdpPortRangeDeleteAll_Object=MibScalar
brzaccVLUdpPortRangeDeleteAll=_BrzaccVLUdpPortRangeDeleteAll_Object((1,3,6,1,4,1,12394,1,1,7,10,3,2,6),_BrzaccVLUdpPortRangeDeleteAll_Type())
brzaccVLUdpPortRangeDeleteAll.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUdpPortRangeDeleteAll.setStatus(_A)
_BrzaccVLTcpPortRangeConfig_ObjectIdentity=ObjectIdentity
brzaccVLTcpPortRangeConfig=_BrzaccVLTcpPortRangeConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10,3,3))
class _BrzaccVLTcpPortPriRTPRTCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Au,1),('rtpOnly',2)))
_BrzaccVLTcpPortPriRTPRTCP_Type.__name__=_C
_BrzaccVLTcpPortPriRTPRTCP_Object=MibScalar
brzaccVLTcpPortPriRTPRTCP=_BrzaccVLTcpPortPriRTPRTCP_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,1),_BrzaccVLTcpPortPriRTPRTCP_Type())
brzaccVLTcpPortPriRTPRTCP.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTcpPortPriRTPRTCP.setStatus(_A)
_BrzaccVLTcpPortRangeNum_Type=Integer32
_BrzaccVLTcpPortRangeNum_Object=MibScalar
brzaccVLTcpPortRangeNum=_BrzaccVLTcpPortRangeNum_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,2),_BrzaccVLTcpPortRangeNum_Type())
brzaccVLTcpPortRangeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTcpPortRangeNum.setStatus(_A)
_BrzaccVLTcpPortRangeTable_Object=MibTable
brzaccVLTcpPortRangeTable=_BrzaccVLTcpPortRangeTable_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,3))
if mibBuilder.loadTexts:brzaccVLTcpPortRangeTable.setStatus(_A)
_BrzaccVLTcpPortRangeEntry_Object=MibTableRow
brzaccVLTcpPortRangeEntry=_BrzaccVLTcpPortRangeEntry_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,3,1))
brzaccVLTcpPortRangeEntry.setIndexNames((0,_E,_Aw))
if mibBuilder.loadTexts:brzaccVLTcpPortRangeEntry.setStatus(_A)
class _BrzaccVLTcpPortRangeStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrzaccVLTcpPortRangeStart_Type.__name__=_C
_BrzaccVLTcpPortRangeStart_Object=MibTableColumn
brzaccVLTcpPortRangeStart=_BrzaccVLTcpPortRangeStart_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,3,1,1),_BrzaccVLTcpPortRangeStart_Type())
brzaccVLTcpPortRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTcpPortRangeStart.setStatus(_A)
class _BrzaccVLTcpPortRangeEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrzaccVLTcpPortRangeEnd_Type.__name__=_C
_BrzaccVLTcpPortRangeEnd_Object=MibTableColumn
brzaccVLTcpPortRangeEnd=_BrzaccVLTcpPortRangeEnd_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,3,1,2),_BrzaccVLTcpPortRangeEnd_Type())
brzaccVLTcpPortRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTcpPortRangeEnd.setStatus(_A)
class _BrzaccVLTcpPortRangeIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_BrzaccVLTcpPortRangeIdx_Type.__name__=_C
_BrzaccVLTcpPortRangeIdx_Object=MibTableColumn
brzaccVLTcpPortRangeIdx=_BrzaccVLTcpPortRangeIdx_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,3,1,3),_BrzaccVLTcpPortRangeIdx_Type())
brzaccVLTcpPortRangeIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTcpPortRangeIdx.setStatus(_A)
class _BrzaccVLTcpPortRangeAdd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_BrzaccVLTcpPortRangeAdd_Type.__name__=_I
_BrzaccVLTcpPortRangeAdd_Object=MibScalar
brzaccVLTcpPortRangeAdd=_BrzaccVLTcpPortRangeAdd_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,4),_BrzaccVLTcpPortRangeAdd_Type())
brzaccVLTcpPortRangeAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTcpPortRangeAdd.setStatus(_A)
class _BrzaccVLTcpPortRangeDelete_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_BrzaccVLTcpPortRangeDelete_Type.__name__=_I
_BrzaccVLTcpPortRangeDelete_Object=MibScalar
brzaccVLTcpPortRangeDelete=_BrzaccVLTcpPortRangeDelete_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,5),_BrzaccVLTcpPortRangeDelete_Type())
brzaccVLTcpPortRangeDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTcpPortRangeDelete.setStatus(_A)
class _BrzaccVLTcpPortRangeDeleteAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_L,2)))
_BrzaccVLTcpPortRangeDeleteAll_Type.__name__=_C
_BrzaccVLTcpPortRangeDeleteAll_Object=MibScalar
brzaccVLTcpPortRangeDeleteAll=_BrzaccVLTcpPortRangeDeleteAll_Object((1,3,6,1,4,1,12394,1,1,7,10,3,3,6),_BrzaccVLTcpPortRangeDeleteAll_Type())
brzaccVLTcpPortRangeDeleteAll.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTcpPortRangeDeleteAll.setStatus(_A)
_BrzaccVLWirelessLinkPrioritization_ObjectIdentity=ObjectIdentity
brzaccVLWirelessLinkPrioritization=_BrzaccVLWirelessLinkPrioritization_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10,4))
class _BrzaccVLWirelessLinkPrioritizationOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLWirelessLinkPrioritizationOption_Type.__name__=_C
_BrzaccVLWirelessLinkPrioritizationOption_Object=MibScalar
brzaccVLWirelessLinkPrioritizationOption=_BrzaccVLWirelessLinkPrioritizationOption_Object((1,3,6,1,4,1,12394,1,1,7,10,4,1),_BrzaccVLWirelessLinkPrioritizationOption_Type())
brzaccVLWirelessLinkPrioritizationOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLWirelessLinkPrioritizationOption.setStatus(_A)
class _BrzaccVLlowPriorityAIFS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,50))
_BrzaccVLlowPriorityAIFS_Type.__name__=_C
_BrzaccVLlowPriorityAIFS_Object=MibScalar
brzaccVLlowPriorityAIFS=_BrzaccVLlowPriorityAIFS_Object((1,3,6,1,4,1,12394,1,1,7,10,4,2),_BrzaccVLlowPriorityAIFS_Type())
brzaccVLlowPriorityAIFS.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLlowPriorityAIFS.setStatus(_A)
class _BrzaccVLHWRetriesHighPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_BrzaccVLHWRetriesHighPriority_Type.__name__=_C
_BrzaccVLHWRetriesHighPriority_Object=MibScalar
brzaccVLHWRetriesHighPriority=_BrzaccVLHWRetriesHighPriority_Object((1,3,6,1,4,1,12394,1,1,7,10,4,3),_BrzaccVLHWRetriesHighPriority_Type())
brzaccVLHWRetriesHighPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLHWRetriesHighPriority.setStatus(_A)
class _BrzaccVLHWRetriesLowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_BrzaccVLHWRetriesLowPriority_Type.__name__=_C
_BrzaccVLHWRetriesLowPriority_Object=MibScalar
brzaccVLHWRetriesLowPriority=_BrzaccVLHWRetriesLowPriority_Object((1,3,6,1,4,1,12394,1,1,7,10,4,4),_BrzaccVLHWRetriesLowPriority_Type())
brzaccVLHWRetriesLowPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLHWRetriesLowPriority.setStatus(_A)
class _BrzaccVLAUBurstDurationHighPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_BrzaccVLAUBurstDurationHighPriority_Type.__name__=_C
_BrzaccVLAUBurstDurationHighPriority_Object=MibScalar
brzaccVLAUBurstDurationHighPriority=_BrzaccVLAUBurstDurationHighPriority_Object((1,3,6,1,4,1,12394,1,1,7,10,4,5),_BrzaccVLAUBurstDurationHighPriority_Type())
brzaccVLAUBurstDurationHighPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAUBurstDurationHighPriority.setStatus(_A)
class _BrzaccVLAUBurstDurationLowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_BrzaccVLAUBurstDurationLowPriority_Type.__name__=_C
_BrzaccVLAUBurstDurationLowPriority_Object=MibScalar
brzaccVLAUBurstDurationLowPriority=_BrzaccVLAUBurstDurationLowPriority_Object((1,3,6,1,4,1,12394,1,1,7,10,4,6),_BrzaccVLAUBurstDurationLowPriority_Type())
brzaccVLAUBurstDurationLowPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAUBurstDurationLowPriority.setStatus(_A)
class _BrzaccVLSUBurstDurationHighPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_BrzaccVLSUBurstDurationHighPriority_Type.__name__=_C
_BrzaccVLSUBurstDurationHighPriority_Object=MibScalar
brzaccVLSUBurstDurationHighPriority=_BrzaccVLSUBurstDurationHighPriority_Object((1,3,6,1,4,1,12394,1,1,7,10,4,7),_BrzaccVLSUBurstDurationHighPriority_Type())
brzaccVLSUBurstDurationHighPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSUBurstDurationHighPriority.setStatus(_A)
class _BrzaccVLSUBurstDurationLowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_BrzaccVLSUBurstDurationLowPriority_Type.__name__=_C
_BrzaccVLSUBurstDurationLowPriority_Object=MibScalar
brzaccVLSUBurstDurationLowPriority=_BrzaccVLSUBurstDurationLowPriority_Object((1,3,6,1,4,1,12394,1,1,7,10,4,8),_BrzaccVLSUBurstDurationLowPriority_Type())
brzaccVLSUBurstDurationLowPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSUBurstDurationLowPriority.setStatus(_A)
_BrzaccVLTrafficPriIpRange_ObjectIdentity=ObjectIdentity
brzaccVLTrafficPriIpRange=_BrzaccVLTrafficPriIpRange_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,10,5))
class _BrzaccVLTrafficPriIpRangeOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('ipSource',2),('ipDestination',3),('ipSourceOrDestination',4)))
_BrzaccVLTrafficPriIpRangeOption_Type.__name__=_C
_BrzaccVLTrafficPriIpRangeOption_Object=MibScalar
brzaccVLTrafficPriIpRangeOption=_BrzaccVLTrafficPriIpRangeOption_Object((1,3,6,1,4,1,12394,1,1,7,10,5,1),_BrzaccVLTrafficPriIpRangeOption_Type())
brzaccVLTrafficPriIpRangeOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTrafficPriIpRangeOption.setStatus(_A)
_BrzaccVLTrafficPriIpRangeIpAddress_Type=IpAddress
_BrzaccVLTrafficPriIpRangeIpAddress_Object=MibScalar
brzaccVLTrafficPriIpRangeIpAddress=_BrzaccVLTrafficPriIpRangeIpAddress_Object((1,3,6,1,4,1,12394,1,1,7,10,5,2),_BrzaccVLTrafficPriIpRangeIpAddress_Type())
brzaccVLTrafficPriIpRangeIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTrafficPriIpRangeIpAddress.setStatus(_A)
_BrzaccVLTrafficPriIpRangeIpMask_Type=IpAddress
_BrzaccVLTrafficPriIpRangeIpMask_Object=MibScalar
brzaccVLTrafficPriIpRangeIpMask=_BrzaccVLTrafficPriIpRangeIpMask_Object((1,3,6,1,4,1,12394,1,1,7,10,5,3),_BrzaccVLTrafficPriIpRangeIpMask_Type())
brzaccVLTrafficPriIpRangeIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLTrafficPriIpRangeIpMask.setStatus(_A)
_BrzaccVLDrap_ObjectIdentity=ObjectIdentity
brzaccVLDrap=_BrzaccVLDrap_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,11))
class _BrzaccVLDrapSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLDrapSupport_Type.__name__=_C
_BrzaccVLDrapSupport_Object=MibScalar
brzaccVLDrapSupport=_BrzaccVLDrapSupport_Object((1,3,6,1,4,1,12394,1,1,7,11,1),_BrzaccVLDrapSupport_Type())
brzaccVLDrapSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDrapSupport.setStatus(_A)
class _BrzaccVLDrapUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,8200))
_BrzaccVLDrapUdpPort_Type.__name__=_C
_BrzaccVLDrapUdpPort_Object=MibScalar
brzaccVLDrapUdpPort=_BrzaccVLDrapUdpPort_Object((1,3,6,1,4,1,12394,1,1,7,11,2),_BrzaccVLDrapUdpPort_Type())
brzaccVLDrapUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDrapUdpPort.setStatus(_A)
class _BrzaccVLDrapMaxNumberOfVoiceCalls_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrzaccVLDrapMaxNumberOfVoiceCalls_Type.__name__=_C
_BrzaccVLDrapMaxNumberOfVoiceCalls_Object=MibScalar
brzaccVLDrapMaxNumberOfVoiceCalls=_BrzaccVLDrapMaxNumberOfVoiceCalls_Object((1,3,6,1,4,1,12394,1,1,7,11,3),_BrzaccVLDrapMaxNumberOfVoiceCalls_Type())
brzaccVLDrapMaxNumberOfVoiceCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDrapMaxNumberOfVoiceCalls.setStatus(_A)
class _BrzaccVLDrapTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrzaccVLDrapTTL_Type.__name__=_C
_BrzaccVLDrapTTL_Object=MibScalar
brzaccVLDrapTTL=_BrzaccVLDrapTTL_Object((1,3,6,1,4,1,12394,1,1,7,11,4),_BrzaccVLDrapTTL_Type())
brzaccVLDrapTTL.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDrapTTL.setStatus(_A)
_BrzaccVLDrapNoOfActiveVoiceCalls_Type=Integer32
_BrzaccVLDrapNoOfActiveVoiceCalls_Object=MibScalar
brzaccVLDrapNoOfActiveVoiceCalls=_BrzaccVLDrapNoOfActiveVoiceCalls_Object((1,3,6,1,4,1,12394,1,1,7,11,5),_BrzaccVLDrapNoOfActiveVoiceCalls_Type())
brzaccVLDrapNoOfActiveVoiceCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDrapNoOfActiveVoiceCalls.setStatus(_A)
class _BrzaccVLLowPriorityTrafficMinimumPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrzaccVLLowPriorityTrafficMinimumPercent_Type.__name__=_C
_BrzaccVLLowPriorityTrafficMinimumPercent_Object=MibScalar
brzaccVLLowPriorityTrafficMinimumPercent=_BrzaccVLLowPriorityTrafficMinimumPercent_Object((1,3,6,1,4,1,12394,1,1,7,12),_BrzaccVLLowPriorityTrafficMinimumPercent_Type())
brzaccVLLowPriorityTrafficMinimumPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLLowPriorityTrafficMinimumPercent.setStatus(_A)
_BrzaccVLSUEZMirDownlink_Type=Integer32
_BrzaccVLSUEZMirDownlink_Object=MibScalar
brzaccVLSUEZMirDownlink=_BrzaccVLSUEZMirDownlink_Object((1,3,6,1,4,1,12394,1,1,7,13),_BrzaccVLSUEZMirDownlink_Type())
brzaccVLSUEZMirDownlink.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSUEZMirDownlink.setStatus(_A)
class _BrzaccVLMIRThresholdPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrzaccVLMIRThresholdPercent_Type.__name__=_C
_BrzaccVLMIRThresholdPercent_Object=MibScalar
brzaccVLMIRThresholdPercent=_BrzaccVLMIRThresholdPercent_Object((1,3,6,1,4,1,12394,1,1,7,14),_BrzaccVLMIRThresholdPercent_Type())
brzaccVLMIRThresholdPercent.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMIRThresholdPercent.setStatus(_A)
_BrzaccVLProportionalIRParameters_ObjectIdentity=ObjectIdentity
brzaccVLProportionalIRParameters=_BrzaccVLProportionalIRParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,7,15))
class _BrzaccVLProportionalIRFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrzaccVLProportionalIRFactor_Type.__name__=_C
_BrzaccVLProportionalIRFactor_Object=MibScalar
brzaccVLProportionalIRFactor=_BrzaccVLProportionalIRFactor_Object((1,3,6,1,4,1,12394,1,1,7,15,1),_BrzaccVLProportionalIRFactor_Type())
brzaccVLProportionalIRFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLProportionalIRFactor.setStatus(_A)
class _BrzaccVLProportionalIRUpdatePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_BrzaccVLProportionalIRUpdatePeriod_Type.__name__=_C
_BrzaccVLProportionalIRUpdatePeriod_Object=MibScalar
brzaccVLProportionalIRUpdatePeriod=_BrzaccVLProportionalIRUpdatePeriod_Object((1,3,6,1,4,1,12394,1,1,7,15,2),_BrzaccVLProportionalIRUpdatePeriod_Type())
brzaccVLProportionalIRUpdatePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLProportionalIRUpdatePeriod.setStatus(_A)
class _BrzaccVLProportionalIRThresholdPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrzaccVLProportionalIRThresholdPercentage_Type.__name__=_C
_BrzaccVLProportionalIRThresholdPercentage_Object=MibScalar
brzaccVLProportionalIRThresholdPercentage=_BrzaccVLProportionalIRThresholdPercentage_Object((1,3,6,1,4,1,12394,1,1,7,15,3),_BrzaccVLProportionalIRThresholdPercentage_Type())
brzaccVLProportionalIRThresholdPercentage.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLProportionalIRThresholdPercentage.setStatus(_A)
class _BrzaccVLProportionalIRThresholdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BrzaccVLProportionalIRThresholdRate_Type.__name__=_C
_BrzaccVLProportionalIRThresholdRate_Object=MibScalar
brzaccVLProportionalIRThresholdRate=_BrzaccVLProportionalIRThresholdRate_Object((1,3,6,1,4,1,12394,1,1,7,15,4),_BrzaccVLProportionalIRThresholdRate_Type())
brzaccVLProportionalIRThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLProportionalIRThresholdRate.setStatus(_A)
_BrzaccVLUserFilterParams_ObjectIdentity=ObjectIdentity
brzaccVLUserFilterParams=_BrzaccVLUserFilterParams_ObjectIdentity((1,3,6,1,4,1,12394,1,1,8))
class _BrzaccVLUserFilterOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_G,1),('ipOnly',2),('userDefinedAddrOnly',3),('pPPoEOnly',4),(_F,255)))
_BrzaccVLUserFilterOption_Type.__name__=_C
_BrzaccVLUserFilterOption_Object=MibScalar
brzaccVLUserFilterOption=_BrzaccVLUserFilterOption_Object((1,3,6,1,4,1,12394,1,1,8,1),_BrzaccVLUserFilterOption_Type())
brzaccVLUserFilterOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLUserFilterOption.setStatus(_A)
_BrzaccVLIpFilterTable_Object=MibTable
brzaccVLIpFilterTable=_BrzaccVLIpFilterTable_Object((1,3,6,1,4,1,12394,1,1,8,2))
if mibBuilder.loadTexts:brzaccVLIpFilterTable.setStatus(_A)
_BrzaccVLIpFilterEntry_Object=MibTableRow
brzaccVLIpFilterEntry=_BrzaccVLIpFilterEntry_Object((1,3,6,1,4,1,12394,1,1,8,2,1))
brzaccVLIpFilterEntry.setIndexNames((0,_E,_Ax))
if mibBuilder.loadTexts:brzaccVLIpFilterEntry.setStatus(_A)
_BrzaccVLIpID_Type=IpAddress
_BrzaccVLIpID_Object=MibTableColumn
brzaccVLIpID=_BrzaccVLIpID_Object((1,3,6,1,4,1,12394,1,1,8,2,1,1),_BrzaccVLIpID_Type())
brzaccVLIpID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLIpID.setStatus(_A)
_BrzaccVLMaskID_Type=IpAddress
_BrzaccVLMaskID_Object=MibTableColumn
brzaccVLMaskID=_BrzaccVLMaskID_Object((1,3,6,1,4,1,12394,1,1,8,2,1,2),_BrzaccVLMaskID_Type())
brzaccVLMaskID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaskID.setStatus(_A)
_BrzaccVLIpFilterRange_Type=Integer32
_BrzaccVLIpFilterRange_Object=MibTableColumn
brzaccVLIpFilterRange=_BrzaccVLIpFilterRange_Object((1,3,6,1,4,1,12394,1,1,8,2,1,3),_BrzaccVLIpFilterRange_Type())
brzaccVLIpFilterRange.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLIpFilterRange.setStatus(_A)
class _BrzaccVLIpFilterIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BrzaccVLIpFilterIdx_Type.__name__=_C
_BrzaccVLIpFilterIdx_Object=MibTableColumn
brzaccVLIpFilterIdx=_BrzaccVLIpFilterIdx_Object((1,3,6,1,4,1,12394,1,1,8,2,1,4),_BrzaccVLIpFilterIdx_Type())
brzaccVLIpFilterIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLIpFilterIdx.setStatus(_A)
class _BrzaccVLDeleteOneUserFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('deletefirstEntry',1),('deletesecondEntry',2),('deletethirdEntry',3),('deletefourthEntry',4),('deletefifthEntry',5),('deletesixthEntry',6),('deleteseventhEntry',7),('deleteeighthEntry',8),(_L,9),(_F,255)))
_BrzaccVLDeleteOneUserFilter_Type.__name__=_C
_BrzaccVLDeleteOneUserFilter_Object=MibScalar
brzaccVLDeleteOneUserFilter=_BrzaccVLDeleteOneUserFilter_Object((1,3,6,1,4,1,12394,1,1,8,3),_BrzaccVLDeleteOneUserFilter_Type())
brzaccVLDeleteOneUserFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteOneUserFilter.setStatus(_A)
class _BrzaccVLDeleteAllUserFilters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_c,1),(_L,2),(_F,255)))
_BrzaccVLDeleteAllUserFilters_Type.__name__=_C
_BrzaccVLDeleteAllUserFilters_Object=MibScalar
brzaccVLDeleteAllUserFilters=_BrzaccVLDeleteAllUserFilters_Object((1,3,6,1,4,1,12394,1,1,8,4),_BrzaccVLDeleteAllUserFilters_Type())
brzaccVLDeleteAllUserFilters.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDeleteAllUserFilters.setStatus(_A)
class _BrzaccVLDHCPUnicastOverrideFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLDHCPUnicastOverrideFilter_Type.__name__=_C
_BrzaccVLDHCPUnicastOverrideFilter_Object=MibScalar
brzaccVLDHCPUnicastOverrideFilter=_BrzaccVLDHCPUnicastOverrideFilter_Object((1,3,6,1,4,1,12394,1,1,8,5),_BrzaccVLDHCPUnicastOverrideFilter_Type())
brzaccVLDHCPUnicastOverrideFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDHCPUnicastOverrideFilter.setStatus(_A)
_BrzaccVLNewIpFilterTable_Object=MibTable
brzaccVLNewIpFilterTable=_BrzaccVLNewIpFilterTable_Object((1,3,6,1,4,1,12394,1,1,8,6))
if mibBuilder.loadTexts:brzaccVLNewIpFilterTable.setStatus(_A)
_BrzaccVLNewIpFilterEntry_Object=MibTableRow
brzaccVLNewIpFilterEntry=_BrzaccVLNewIpFilterEntry_Object((1,3,6,1,4,1,12394,1,1,8,6,1))
brzaccVLNewIpFilterEntry.setIndexNames((0,_E,_Ay))
if mibBuilder.loadTexts:brzaccVLNewIpFilterEntry.setStatus(_A)
_BrzaccVLNewIpID_Type=IpAddress
_BrzaccVLNewIpID_Object=MibTableColumn
brzaccVLNewIpID=_BrzaccVLNewIpID_Object((1,3,6,1,4,1,12394,1,1,8,6,1,1),_BrzaccVLNewIpID_Type())
brzaccVLNewIpID.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewIpID.setStatus(_A)
_BrzaccVLNewMaskID_Type=IpAddress
_BrzaccVLNewMaskID_Object=MibTableColumn
brzaccVLNewMaskID=_BrzaccVLNewMaskID_Object((1,3,6,1,4,1,12394,1,1,8,6,1,2),_BrzaccVLNewMaskID_Type())
brzaccVLNewMaskID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewMaskID.setStatus(_A)
_BrzaccVLNewIpFilterRange_Type=Integer32
_BrzaccVLNewIpFilterRange_Object=MibTableColumn
brzaccVLNewIpFilterRange=_BrzaccVLNewIpFilterRange_Object((1,3,6,1,4,1,12394,1,1,8,6,1,3),_BrzaccVLNewIpFilterRange_Type())
brzaccVLNewIpFilterRange.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewIpFilterRange.setStatus(_A)
class _BrzaccVLNewIpFilterCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_BrzaccVLNewIpFilterCommand_Type.__name__=_C
_BrzaccVLNewIpFilterCommand_Object=MibTableColumn
brzaccVLNewIpFilterCommand=_BrzaccVLNewIpFilterCommand_Object((1,3,6,1,4,1,12394,1,1,8,6,1,4),_BrzaccVLNewIpFilterCommand_Type())
brzaccVLNewIpFilterCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNewIpFilterCommand.setStatus(_A)
class _BrzaccVLDHCPPPPoEOverrideFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLDHCPPPPoEOverrideFilter_Type.__name__=_C
_BrzaccVLDHCPPPPoEOverrideFilter_Object=MibScalar
brzaccVLDHCPPPPoEOverrideFilter=_BrzaccVLDHCPPPPoEOverrideFilter_Object((1,3,6,1,4,1,12394,1,1,8,7),_BrzaccVLDHCPPPPoEOverrideFilter_Type())
brzaccVLDHCPPPPoEOverrideFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDHCPPPPoEOverrideFilter.setStatus(_A)
_BrzaccVLSecurityParameters_ObjectIdentity=ObjectIdentity
brzaccVLSecurityParameters=_BrzaccVLSecurityParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,9))
class _BrzaccVLAuthenticationAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),(_r,2)))
_BrzaccVLAuthenticationAlgorithm_Type.__name__=_C
_BrzaccVLAuthenticationAlgorithm_Object=MibScalar
brzaccVLAuthenticationAlgorithm=_BrzaccVLAuthenticationAlgorithm_Object((1,3,6,1,4,1,12394,1,1,9,1),_BrzaccVLAuthenticationAlgorithm_Type())
brzaccVLAuthenticationAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAuthenticationAlgorithm.setStatus(_A)
_BrzaccVLSUDefaultKeyID_Type=Integer32
_BrzaccVLSUDefaultKeyID_Object=MibScalar
brzaccVLSUDefaultKeyID=_BrzaccVLSUDefaultKeyID_Object((1,3,6,1,4,1,12394,1,1,9,2),_BrzaccVLSUDefaultKeyID_Type())
brzaccVLSUDefaultKeyID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSUDefaultKeyID.setStatus(_A)
class _BrzaccVLDataEncryptionOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BrzaccVLDataEncryptionOption_Type.__name__=_C
_BrzaccVLDataEncryptionOption_Object=MibScalar
brzaccVLDataEncryptionOption=_BrzaccVLDataEncryptionOption_Object((1,3,6,1,4,1,12394,1,1,9,3),_BrzaccVLDataEncryptionOption_Type())
brzaccVLDataEncryptionOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLDataEncryptionOption.setStatus(_A)
_BrzaccVLAUDefaultMulticastKeyID_Type=Integer32
_BrzaccVLAUDefaultMulticastKeyID_Object=MibScalar
brzaccVLAUDefaultMulticastKeyID=_BrzaccVLAUDefaultMulticastKeyID_Object((1,3,6,1,4,1,12394,1,1,9,4),_BrzaccVLAUDefaultMulticastKeyID_Type())
brzaccVLAUDefaultMulticastKeyID.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAUDefaultMulticastKeyID.setStatus(_A)
class _BrzaccVLSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),('aesOCB',2),(_p,3)))
_BrzaccVLSecurityMode_Type.__name__=_C
_BrzaccVLSecurityMode_Object=MibScalar
brzaccVLSecurityMode=_BrzaccVLSecurityMode_Object((1,3,6,1,4,1,12394,1,1,9,5),_BrzaccVLSecurityMode_Type())
brzaccVLSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSecurityMode.setStatus(_A)
class _BrzaccVLAuthenticationPromiscuousMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BrzaccVLAuthenticationPromiscuousMode_Type.__name__=_C
_BrzaccVLAuthenticationPromiscuousMode_Object=MibScalar
brzaccVLAuthenticationPromiscuousMode=_BrzaccVLAuthenticationPromiscuousMode_Object((1,3,6,1,4,1,12394,1,1,9,6),_BrzaccVLAuthenticationPromiscuousMode_Type())
brzaccVLAuthenticationPromiscuousMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAuthenticationPromiscuousMode.setStatus(_A)
class _BrzaccVLKey1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_BrzaccVLKey1_Type.__name__=_I
_BrzaccVLKey1_Object=MibScalar
brzaccVLKey1=_BrzaccVLKey1_Object((1,3,6,1,4,1,12394,1,1,9,7),_BrzaccVLKey1_Type())
brzaccVLKey1.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLKey1.setStatus(_A)
class _BrzaccVLKey2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_BrzaccVLKey2_Type.__name__=_I
_BrzaccVLKey2_Object=MibScalar
brzaccVLKey2=_BrzaccVLKey2_Object((1,3,6,1,4,1,12394,1,1,9,8),_BrzaccVLKey2_Type())
brzaccVLKey2.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLKey2.setStatus(_A)
class _BrzaccVLKey3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_BrzaccVLKey3_Type.__name__=_I
_BrzaccVLKey3_Object=MibScalar
brzaccVLKey3=_BrzaccVLKey3_Object((1,3,6,1,4,1,12394,1,1,9,9),_BrzaccVLKey3_Type())
brzaccVLKey3.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLKey3.setStatus(_A)
class _BrzaccVLKey4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_BrzaccVLKey4_Type.__name__=_I
_BrzaccVLKey4_Object=MibScalar
brzaccVLKey4=_BrzaccVLKey4_Object((1,3,6,1,4,1,12394,1,1,9,10),_BrzaccVLKey4_Type())
brzaccVLKey4.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLKey4.setStatus(_A)
class _BrzaccVLSecurityModeSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrzaccVLSecurityModeSupport_Type.__name__=_C
_BrzaccVLSecurityModeSupport_Object=MibScalar
brzaccVLSecurityModeSupport=_BrzaccVLSecurityModeSupport_Object((1,3,6,1,4,1,12394,1,1,9,12),_BrzaccVLSecurityModeSupport_Type())
brzaccVLSecurityModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSecurityModeSupport.setStatus(_A)
_BrzaccVLPerformanceParams_ObjectIdentity=ObjectIdentity
brzaccVLPerformanceParams=_BrzaccVLPerformanceParams_ObjectIdentity((1,3,6,1,4,1,12394,1,1,10))
_BrzaccVLRTSThreshold_Type=Integer32
_BrzaccVLRTSThreshold_Object=MibScalar
brzaccVLRTSThreshold=_BrzaccVLRTSThreshold_Object((1,3,6,1,4,1,12394,1,1,10,1),_BrzaccVLRTSThreshold_Type())
brzaccVLRTSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLRTSThreshold.setStatus(_A)
_BrzaccVLMinContentionWindow_Type=Integer32
_BrzaccVLMinContentionWindow_Object=MibScalar
brzaccVLMinContentionWindow=_BrzaccVLMinContentionWindow_Object((1,3,6,1,4,1,12394,1,1,10,3),_BrzaccVLMinContentionWindow_Type())
brzaccVLMinContentionWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMinContentionWindow.setStatus(_A)
_BrzaccVLMaxContentionWindow_Type=Integer32
_BrzaccVLMaxContentionWindow_Object=MibScalar
brzaccVLMaxContentionWindow=_BrzaccVLMaxContentionWindow_Object((1,3,6,1,4,1,12394,1,1,10,4),_BrzaccVLMaxContentionWindow_Type())
brzaccVLMaxContentionWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaxContentionWindow.setStatus(_A)
class _BrzaccVLMaximumModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_P,6),(_Q,7),(_R,8)))
_BrzaccVLMaximumModulationLevel_Type.__name__=_C
_BrzaccVLMaximumModulationLevel_Object=MibScalar
brzaccVLMaximumModulationLevel=_BrzaccVLMaximumModulationLevel_Object((1,3,6,1,4,1,12394,1,1,10,5),_BrzaccVLMaximumModulationLevel_Type())
brzaccVLMaximumModulationLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMaximumModulationLevel.setStatus(_A)
class _BrzaccVLMulticastModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_P,6),(_Q,7),(_R,8)))
_BrzaccVLMulticastModulationLevel_Type.__name__=_C
_BrzaccVLMulticastModulationLevel_Object=MibScalar
brzaccVLMulticastModulationLevel=_BrzaccVLMulticastModulationLevel_Object((1,3,6,1,4,1,12394,1,1,10,6),_BrzaccVLMulticastModulationLevel_Type())
brzaccVLMulticastModulationLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMulticastModulationLevel.setStatus(_A)
_BrzaccVLAvgSNRMemoryFactor_Type=DisplayString
_BrzaccVLAvgSNRMemoryFactor_Object=MibScalar
brzaccVLAvgSNRMemoryFactor=_BrzaccVLAvgSNRMemoryFactor_Object((1,3,6,1,4,1,12394,1,1,10,7),_BrzaccVLAvgSNRMemoryFactor_Type())
brzaccVLAvgSNRMemoryFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAvgSNRMemoryFactor.setStatus(_A)
_BrzaccVLHardwareRetries_Type=Integer32
_BrzaccVLHardwareRetries_Object=MibScalar
brzaccVLHardwareRetries=_BrzaccVLHardwareRetries_Object((1,3,6,1,4,1,12394,1,1,10,8),_BrzaccVLHardwareRetries_Type())
brzaccVLHardwareRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLHardwareRetries.setStatus(_A)
_BrzaccVLAdaptiveModulationParams_ObjectIdentity=ObjectIdentity
brzaccVLAdaptiveModulationParams=_BrzaccVLAdaptiveModulationParams_ObjectIdentity((1,3,6,1,4,1,12394,1,1,10,9))
class _BrzaccVLAdaptiveModulationAlgorithmOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAdaptiveModulationAlgorithmOption_Type.__name__=_C
_BrzaccVLAdaptiveModulationAlgorithmOption_Object=MibScalar
brzaccVLAdaptiveModulationAlgorithmOption=_BrzaccVLAdaptiveModulationAlgorithmOption_Object((1,3,6,1,4,1,12394,1,1,10,9,1),_BrzaccVLAdaptiveModulationAlgorithmOption_Type())
brzaccVLAdaptiveModulationAlgorithmOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationAlgorithmOption.setStatus(_A)
class _BrzaccVLSoftwareRetrySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLSoftwareRetrySupport_Type.__name__=_C
_BrzaccVLSoftwareRetrySupport_Object=MibScalar
brzaccVLSoftwareRetrySupport=_BrzaccVLSoftwareRetrySupport_Object((1,3,6,1,4,1,12394,1,1,10,9,2),_BrzaccVLSoftwareRetrySupport_Type())
brzaccVLSoftwareRetrySupport.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLSoftwareRetrySupport.setStatus(_A)
class _BrzaccVLNumOfSoftwareRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(255));namedValues=NamedValues((_F,255))
_BrzaccVLNumOfSoftwareRetries_Type.__name__=_C
_BrzaccVLNumOfSoftwareRetries_Object=MibScalar
brzaccVLNumOfSoftwareRetries=_BrzaccVLNumOfSoftwareRetries_Object((1,3,6,1,4,1,12394,1,1,10,9,3),_BrzaccVLNumOfSoftwareRetries_Type())
brzaccVLNumOfSoftwareRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLNumOfSoftwareRetries.setStatus(_A)
_BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Type=Integer32
_BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Object=MibScalar
brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages=_BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Object((1,3,6,1,4,1,12394,1,1,10,9,4),_BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Type())
brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages.setStatus(_A)
class _BrzaccVLAdaptiveModulationDecisionThresholds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('normal',1),('high',2),(_F,255)))
_BrzaccVLAdaptiveModulationDecisionThresholds_Type.__name__=_C
_BrzaccVLAdaptiveModulationDecisionThresholds_Object=MibScalar
brzaccVLAdaptiveModulationDecisionThresholds=_BrzaccVLAdaptiveModulationDecisionThresholds_Object((1,3,6,1,4,1,12394,1,1,10,9,5),_BrzaccVLAdaptiveModulationDecisionThresholds_Type())
brzaccVLAdaptiveModulationDecisionThresholds.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationDecisionThresholds.setStatus(_A)
class _BrzaccVLAdaptiveModulationHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,25))
_BrzaccVLAdaptiveModulationHistorySize_Type.__name__=_C
_BrzaccVLAdaptiveModulationHistorySize_Object=MibScalar
brzaccVLAdaptiveModulationHistorySize=_BrzaccVLAdaptiveModulationHistorySize_Object((1,3,6,1,4,1,12394,1,1,10,9,7),_BrzaccVLAdaptiveModulationHistorySize_Type())
brzaccVLAdaptiveModulationHistorySize.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationHistorySize.setStatus(_A)
class _BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Type.__name__=_C
_BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Object=MibScalar
brzaccVLAdaptiveModulationPacketThresholdToTestUpRate=_BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Object((1,3,6,1,4,1,12394,1,1,10,9,8),_BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Type())
brzaccVLAdaptiveModulationPacketThresholdToTestUpRate.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationPacketThresholdToTestUpRate.setStatus(_A)
class _BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Type.__name__=_C
_BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Object=MibScalar
brzaccVLAdaptiveModulationPacketNoOnUpperRate=_BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Object((1,3,6,1,4,1,12394,1,1,10,9,9),_BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Type())
brzaccVLAdaptiveModulationPacketNoOnUpperRate.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationPacketNoOnUpperRate.setStatus(_A)
class _BrzaccVLAdaptiveModulationAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('adaptiveModulation',1),('statisticsBasedRateControl',2),(_F,255)))
_BrzaccVLAdaptiveModulationAlgorithm_Type.__name__=_C
_BrzaccVLAdaptiveModulationAlgorithm_Object=MibScalar
brzaccVLAdaptiveModulationAlgorithm=_BrzaccVLAdaptiveModulationAlgorithm_Object((1,3,6,1,4,1,12394,1,1,10,9,10),_BrzaccVLAdaptiveModulationAlgorithm_Type())
brzaccVLAdaptiveModulationAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationAlgorithm.setStatus(_A)
class _BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Type.__name__=_C
_BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Object=MibScalar
brzaccVLAdaptiveModulationRetriesOnLowerModulations=_BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Object((1,3,6,1,4,1,12394,1,1,10,9,11),_BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Type())
brzaccVLAdaptiveModulationRetriesOnLowerModulations.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationRetriesOnLowerModulations.setStatus(_A)
class _BrzaccVLAdaptiveModulationRTSDurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shortRTSDuration',1),('longRTSDuration',2)))
_BrzaccVLAdaptiveModulationRTSDurationMode_Type.__name__=_C
_BrzaccVLAdaptiveModulationRTSDurationMode_Object=MibScalar
brzaccVLAdaptiveModulationRTSDurationMode=_BrzaccVLAdaptiveModulationRTSDurationMode_Object((1,3,6,1,4,1,12394,1,1,10,9,12),_BrzaccVLAdaptiveModulationRTSDurationMode_Type())
brzaccVLAdaptiveModulationRTSDurationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAdaptiveModulationRTSDurationMode.setStatus(_A)
_BrzaccVLBurstMode_ObjectIdentity=ObjectIdentity
brzaccVLBurstMode=_BrzaccVLBurstMode_ObjectIdentity((1,3,6,1,4,1,12394,1,1,10,10))
class _BrzaccVLBurstModeOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_G,1),(_H,2),('blocked',3),(_F,255)))
_BrzaccVLBurstModeOption_Type.__name__=_C
_BrzaccVLBurstModeOption_Object=MibScalar
brzaccVLBurstModeOption=_BrzaccVLBurstModeOption_Object((1,3,6,1,4,1,12394,1,1,10,10,1),_BrzaccVLBurstModeOption_Type())
brzaccVLBurstModeOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLBurstModeOption.setStatus(_A)
_BrzaccVLBurstInterval_Type=Integer32
_BrzaccVLBurstInterval_Object=MibScalar
brzaccVLBurstInterval=_BrzaccVLBurstInterval_Object((1,3,6,1,4,1,12394,1,1,10,10,2),_BrzaccVLBurstInterval_Type())
brzaccVLBurstInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLBurstInterval.setStatus(_A)
_BrzaccVLConcatenationParameters_ObjectIdentity=ObjectIdentity
brzaccVLConcatenationParameters=_BrzaccVLConcatenationParameters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,10,11))
class _BrzaccVLConcatenationOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLConcatenationOption_Type.__name__=_C
_BrzaccVLConcatenationOption_Object=MibScalar
brzaccVLConcatenationOption=_BrzaccVLConcatenationOption_Object((1,3,6,1,4,1,12394,1,1,10,11,1),_BrzaccVLConcatenationOption_Type())
brzaccVLConcatenationOption.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLConcatenationOption.setStatus(_A)
class _BrzaccVLConcatenationMaximumNumberOfFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8))
_BrzaccVLConcatenationMaximumNumberOfFrames_Type.__name__=_C
_BrzaccVLConcatenationMaximumNumberOfFrames_Object=MibScalar
brzaccVLConcatenationMaximumNumberOfFrames=_BrzaccVLConcatenationMaximumNumberOfFrames_Object((1,3,6,1,4,1,12394,1,1,10,11,2),_BrzaccVLConcatenationMaximumNumberOfFrames_Type())
brzaccVLConcatenationMaximumNumberOfFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLConcatenationMaximumNumberOfFrames.setStatus(_A)
_BrzaccVLConcatenationMaxFrameSize_Type=Integer32
_BrzaccVLConcatenationMaxFrameSize_Object=MibScalar
brzaccVLConcatenationMaxFrameSize=_BrzaccVLConcatenationMaxFrameSize_Object((1,3,6,1,4,1,12394,1,1,10,11,3),_BrzaccVLConcatenationMaxFrameSize_Type())
brzaccVLConcatenationMaxFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLConcatenationMaxFrameSize.setStatus(_A)
class _BrzaccVLControlModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basicRate',1),('modulationLevel1',2)))
_BrzaccVLControlModulationLevel_Type.__name__=_C
_BrzaccVLControlModulationLevel_Object=MibScalar
brzaccVLControlModulationLevel=_BrzaccVLControlModulationLevel_Object((1,3,6,1,4,1,12394,1,1,10,13),_BrzaccVLControlModulationLevel_Type())
brzaccVLControlModulationLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLControlModulationLevel.setStatus(_A)
class _BrzaccVLEthernetFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('size1600',1),('size2000',2)))
_BrzaccVLEthernetFrameSize_Type.__name__=_C
_BrzaccVLEthernetFrameSize_Object=MibScalar
brzaccVLEthernetFrameSize=_BrzaccVLEthernetFrameSize_Object((1,3,6,1,4,1,12394,1,1,10,14),_BrzaccVLEthernetFrameSize_Type())
brzaccVLEthernetFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLEthernetFrameSize.setStatus(_A)
_BrzaccVLRunningEthernetFrameSize_Type=Integer32
_BrzaccVLRunningEthernetFrameSize_Object=MibScalar
brzaccVLRunningEthernetFrameSize=_BrzaccVLRunningEthernetFrameSize_Object((1,3,6,1,4,1,12394,1,1,10,15),_BrzaccVLRunningEthernetFrameSize_Type())
brzaccVLRunningEthernetFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRunningEthernetFrameSize.setStatus(_A)
_BrzaccVLSiteSurvey_ObjectIdentity=ObjectIdentity
brzaccVLSiteSurvey=_BrzaccVLSiteSurvey_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11))
_BrzaccVLAverageReceiveSNR_Type=Integer32
_BrzaccVLAverageReceiveSNR_Object=MibScalar
brzaccVLAverageReceiveSNR=_BrzaccVLAverageReceiveSNR_Object((1,3,6,1,4,1,12394,1,1,11,1),_BrzaccVLAverageReceiveSNR_Type())
brzaccVLAverageReceiveSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAverageReceiveSNR.setStatus(_A)
_BrzaccVLTrafficStatistics_ObjectIdentity=ObjectIdentity
brzaccVLTrafficStatistics=_BrzaccVLTrafficStatistics_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2))
class _BrzaccVLResetTrafficCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_K,2)))
_BrzaccVLResetTrafficCounters_Type.__name__=_C
_BrzaccVLResetTrafficCounters_Object=MibScalar
brzaccVLResetTrafficCounters=_BrzaccVLResetTrafficCounters_Object((1,3,6,1,4,1,12394,1,1,11,2,1),_BrzaccVLResetTrafficCounters_Type())
brzaccVLResetTrafficCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLResetTrafficCounters.setStatus(_A)
_BrzaccVLEthCounters_ObjectIdentity=ObjectIdentity
brzaccVLEthCounters=_BrzaccVLEthCounters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,2))
_BrzaccVLTotalRxFramesViaEthernet_Type=Counter32
_BrzaccVLTotalRxFramesViaEthernet_Object=MibScalar
brzaccVLTotalRxFramesViaEthernet=_BrzaccVLTotalRxFramesViaEthernet_Object((1,3,6,1,4,1,12394,1,1,11,2,2,1),_BrzaccVLTotalRxFramesViaEthernet_Type())
brzaccVLTotalRxFramesViaEthernet.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRxFramesViaEthernet.setStatus(_A)
_BrzaccVLTxWirelessToEthernet_Type=Counter32
_BrzaccVLTxWirelessToEthernet_Object=MibScalar
brzaccVLTxWirelessToEthernet=_BrzaccVLTxWirelessToEthernet_Object((1,3,6,1,4,1,12394,1,1,11,2,2,2),_BrzaccVLTxWirelessToEthernet_Type())
brzaccVLTxWirelessToEthernet.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTxWirelessToEthernet.setStatus(_A)
_BrzaccVLWirelessLinkCounters_ObjectIdentity=ObjectIdentity
brzaccVLWirelessLinkCounters=_BrzaccVLWirelessLinkCounters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,3))
_BrzaccVLTxFramesToWireless_ObjectIdentity=ObjectIdentity
brzaccVLTxFramesToWireless=_BrzaccVLTxFramesToWireless_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,3,1))
_BrzaccVLAUBeaconsToWireless_Type=Counter32
_BrzaccVLAUBeaconsToWireless_Object=MibScalar
brzaccVLAUBeaconsToWireless=_BrzaccVLAUBeaconsToWireless_Object((1,3,6,1,4,1,12394,1,1,11,2,3,1,1),_BrzaccVLAUBeaconsToWireless_Type())
brzaccVLAUBeaconsToWireless.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAUBeaconsToWireless.setStatus(_A)
_BrzaccVLDataAndOtherMngFramesToWireless_Type=Counter32
_BrzaccVLDataAndOtherMngFramesToWireless_Object=MibScalar
brzaccVLDataAndOtherMngFramesToWireless=_BrzaccVLDataAndOtherMngFramesToWireless_Object((1,3,6,1,4,1,12394,1,1,11,2,3,1,3),_BrzaccVLDataAndOtherMngFramesToWireless_Type())
brzaccVLDataAndOtherMngFramesToWireless.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDataAndOtherMngFramesToWireless.setStatus(_A)
_BrzaccVLTotalTxFramesToWireless_Type=Counter32
_BrzaccVLTotalTxFramesToWireless_Object=MibScalar
brzaccVLTotalTxFramesToWireless=_BrzaccVLTotalTxFramesToWireless_Object((1,3,6,1,4,1,12394,1,1,11,2,3,1,4),_BrzaccVLTotalTxFramesToWireless_Type())
brzaccVLTotalTxFramesToWireless.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalTxFramesToWireless.setStatus(_A)
_BrzaccVLTotalTransmittedUnicasts_Type=Counter32
_BrzaccVLTotalTransmittedUnicasts_Object=MibScalar
brzaccVLTotalTransmittedUnicasts=_BrzaccVLTotalTransmittedUnicasts_Object((1,3,6,1,4,1,12394,1,1,11,2,3,1,5),_BrzaccVLTotalTransmittedUnicasts_Type())
brzaccVLTotalTransmittedUnicasts.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalTransmittedUnicasts.setStatus(_A)
_BrzaccVLTotalTransmittedConcatenatedFramesDouble_Type=Counter32
_BrzaccVLTotalTransmittedConcatenatedFramesDouble_Object=MibScalar
brzaccVLTotalTransmittedConcatenatedFramesDouble=_BrzaccVLTotalTransmittedConcatenatedFramesDouble_Object((1,3,6,1,4,1,12394,1,1,11,2,3,1,6),_BrzaccVLTotalTransmittedConcatenatedFramesDouble_Type())
brzaccVLTotalTransmittedConcatenatedFramesDouble.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalTransmittedConcatenatedFramesDouble.setStatus(_A)
_BrzaccVLTotalTransmittedConcatenatedFramesSingle_Type=Counter32
_BrzaccVLTotalTransmittedConcatenatedFramesSingle_Object=MibScalar
brzaccVLTotalTransmittedConcatenatedFramesSingle=_BrzaccVLTotalTransmittedConcatenatedFramesSingle_Object((1,3,6,1,4,1,12394,1,1,11,2,3,1,7),_BrzaccVLTotalTransmittedConcatenatedFramesSingle_Type())
brzaccVLTotalTransmittedConcatenatedFramesSingle.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalTransmittedConcatenatedFramesSingle.setStatus(_A)
_BrzaccVLTotalTransmittedConcatenatedFramesMore_Type=Counter32
_BrzaccVLTotalTransmittedConcatenatedFramesMore_Object=MibScalar
brzaccVLTotalTransmittedConcatenatedFramesMore=_BrzaccVLTotalTransmittedConcatenatedFramesMore_Object((1,3,6,1,4,1,12394,1,1,11,2,3,1,8),_BrzaccVLTotalTransmittedConcatenatedFramesMore_Type())
brzaccVLTotalTransmittedConcatenatedFramesMore.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalTransmittedConcatenatedFramesMore.setStatus(_A)
_BrzaccVLTotalRxFramesFromWireless_Type=Counter32
_BrzaccVLTotalRxFramesFromWireless_Object=MibScalar
brzaccVLTotalRxFramesFromWireless=_BrzaccVLTotalRxFramesFromWireless_Object((1,3,6,1,4,1,12394,1,1,11,2,3,2),_BrzaccVLTotalRxFramesFromWireless_Type())
brzaccVLTotalRxFramesFromWireless.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRxFramesFromWireless.setStatus(_A)
_BrzaccVLTotalRetransmittedFrames_Type=Counter32
_BrzaccVLTotalRetransmittedFrames_Object=MibScalar
brzaccVLTotalRetransmittedFrames=_BrzaccVLTotalRetransmittedFrames_Object((1,3,6,1,4,1,12394,1,1,11,2,3,3),_BrzaccVLTotalRetransmittedFrames_Type())
brzaccVLTotalRetransmittedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRetransmittedFrames.setStatus(_A)
_BrzaccVLFramesDropped_Type=Counter32
_BrzaccVLFramesDropped_Object=MibScalar
brzaccVLFramesDropped=_BrzaccVLFramesDropped_Object((1,3,6,1,4,1,12394,1,1,11,2,3,4),_BrzaccVLFramesDropped_Type())
brzaccVLFramesDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFramesDropped.setStatus(_A)
_BrzaccVLDataFramesSubmittedToBridge_ObjectIdentity=ObjectIdentity
brzaccVLDataFramesSubmittedToBridge=_BrzaccVLDataFramesSubmittedToBridge_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,3,5))
_BrzaccVLFramesSubmittedViaHighQueue_Type=Counter32
_BrzaccVLFramesSubmittedViaHighQueue_Object=MibScalar
brzaccVLFramesSubmittedViaHighQueue=_BrzaccVLFramesSubmittedViaHighQueue_Object((1,3,6,1,4,1,12394,1,1,11,2,3,5,1),_BrzaccVLFramesSubmittedViaHighQueue_Type())
brzaccVLFramesSubmittedViaHighQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFramesSubmittedViaHighQueue.setStatus(_A)
_BrzaccVLFramesSubmittedViaMidQueue_Type=Counter32
_BrzaccVLFramesSubmittedViaMidQueue_Object=MibScalar
brzaccVLFramesSubmittedViaMidQueue=_BrzaccVLFramesSubmittedViaMidQueue_Object((1,3,6,1,4,1,12394,1,1,11,2,3,5,2),_BrzaccVLFramesSubmittedViaMidQueue_Type())
brzaccVLFramesSubmittedViaMidQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFramesSubmittedViaMidQueue.setStatus(_A)
_BrzaccVLFramesSubmittedViaLowQueue_Type=Counter32
_BrzaccVLFramesSubmittedViaLowQueue_Object=MibScalar
brzaccVLFramesSubmittedViaLowQueue=_BrzaccVLFramesSubmittedViaLowQueue_Object((1,3,6,1,4,1,12394,1,1,11,2,3,5,3),_BrzaccVLFramesSubmittedViaLowQueue_Type())
brzaccVLFramesSubmittedViaLowQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFramesSubmittedViaLowQueue.setStatus(_A)
_BrzaccVLTotalNoOfDataFramesSubmitted_Type=Counter32
_BrzaccVLTotalNoOfDataFramesSubmitted_Object=MibScalar
brzaccVLTotalNoOfDataFramesSubmitted=_BrzaccVLTotalNoOfDataFramesSubmitted_Object((1,3,6,1,4,1,12394,1,1,11,2,3,5,4),_BrzaccVLTotalNoOfDataFramesSubmitted_Type())
brzaccVLTotalNoOfDataFramesSubmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalNoOfDataFramesSubmitted.setStatus(_A)
_BrzaccVLTotalRecievedDataFrames_Type=Counter32
_BrzaccVLTotalRecievedDataFrames_Object=MibScalar
brzaccVLTotalRecievedDataFrames=_BrzaccVLTotalRecievedDataFrames_Object((1,3,6,1,4,1,12394,1,1,11,2,3,6),_BrzaccVLTotalRecievedDataFrames_Type())
brzaccVLTotalRecievedDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRecievedDataFrames.setStatus(_A)
_BrzaccVLRecievedBadFrames_Type=Counter32
_BrzaccVLRecievedBadFrames_Object=MibScalar
brzaccVLRecievedBadFrames=_BrzaccVLRecievedBadFrames_Object((1,3,6,1,4,1,12394,1,1,11,2,3,7),_BrzaccVLRecievedBadFrames_Type())
brzaccVLRecievedBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRecievedBadFrames.setStatus(_A)
_BrzaccVLNoOfDuplicateFramesDiscarded_Type=Counter32
_BrzaccVLNoOfDuplicateFramesDiscarded_Object=MibScalar
brzaccVLNoOfDuplicateFramesDiscarded=_BrzaccVLNoOfDuplicateFramesDiscarded_Object((1,3,6,1,4,1,12394,1,1,11,2,3,8),_BrzaccVLNoOfDuplicateFramesDiscarded_Type())
brzaccVLNoOfDuplicateFramesDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNoOfDuplicateFramesDiscarded.setStatus(_A)
_BrzaccVLNoOfInternallyDiscardedMirCir_Type=Counter32
_BrzaccVLNoOfInternallyDiscardedMirCir_Object=MibScalar
brzaccVLNoOfInternallyDiscardedMirCir=_BrzaccVLNoOfInternallyDiscardedMirCir_Object((1,3,6,1,4,1,12394,1,1,11,2,3,9),_BrzaccVLNoOfInternallyDiscardedMirCir_Type())
brzaccVLNoOfInternallyDiscardedMirCir.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNoOfInternallyDiscardedMirCir.setStatus(_A)
_BrzaccVLTotalRxConcatenatedFramesDouble_Type=Counter32
_BrzaccVLTotalRxConcatenatedFramesDouble_Object=MibScalar
brzaccVLTotalRxConcatenatedFramesDouble=_BrzaccVLTotalRxConcatenatedFramesDouble_Object((1,3,6,1,4,1,12394,1,1,11,2,3,10),_BrzaccVLTotalRxConcatenatedFramesDouble_Type())
brzaccVLTotalRxConcatenatedFramesDouble.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRxConcatenatedFramesDouble.setStatus(_A)
_BrzaccVLTotalRxConcatenatedFramesSingle_Type=Counter32
_BrzaccVLTotalRxConcatenatedFramesSingle_Object=MibScalar
brzaccVLTotalRxConcatenatedFramesSingle=_BrzaccVLTotalRxConcatenatedFramesSingle_Object((1,3,6,1,4,1,12394,1,1,11,2,3,11),_BrzaccVLTotalRxConcatenatedFramesSingle_Type())
brzaccVLTotalRxConcatenatedFramesSingle.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRxConcatenatedFramesSingle.setStatus(_A)
_BrzaccVLTotalRxConcatenatedFramesMore_Type=Counter32
_BrzaccVLTotalRxConcatenatedFramesMore_Object=MibScalar
brzaccVLTotalRxConcatenatedFramesMore=_BrzaccVLTotalRxConcatenatedFramesMore_Object((1,3,6,1,4,1,12394,1,1,11,2,3,12),_BrzaccVLTotalRxConcatenatedFramesMore_Type())
brzaccVLTotalRxConcatenatedFramesMore.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRxConcatenatedFramesMore.setStatus(_A)
_BrzaccVLTXRetransmissionPercentage_Type=Counter32
_BrzaccVLTXRetransmissionPercentage_Object=MibScalar
brzaccVLTXRetransmissionPercentage=_BrzaccVLTXRetransmissionPercentage_Object((1,3,6,1,4,1,12394,1,1,11,2,3,13),_BrzaccVLTXRetransmissionPercentage_Type())
brzaccVLTXRetransmissionPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTXRetransmissionPercentage.setStatus(_A)
_BrzaccVLRXCRCPercentage_Type=Counter32
_BrzaccVLRXCRCPercentage_Object=MibScalar
brzaccVLRXCRCPercentage=_BrzaccVLRXCRCPercentage_Object((1,3,6,1,4,1,12394,1,1,11,2,3,14),_BrzaccVLRXCRCPercentage_Type())
brzaccVLRXCRCPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRXCRCPercentage.setStatus(_A)
_BrzaccVLWirelessLinkEvents_ObjectIdentity=ObjectIdentity
brzaccVLWirelessLinkEvents=_BrzaccVLWirelessLinkEvents_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,4))
_BrzaccVLTxEvents_ObjectIdentity=ObjectIdentity
brzaccVLTxEvents=_BrzaccVLTxEvents_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,4,1))
_BrzaccVLDroppedFrameEvents_Type=Counter32
_BrzaccVLDroppedFrameEvents_Object=MibScalar
brzaccVLDroppedFrameEvents=_BrzaccVLDroppedFrameEvents_Object((1,3,6,1,4,1,12394,1,1,11,2,4,1,1),_BrzaccVLDroppedFrameEvents_Type())
brzaccVLDroppedFrameEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDroppedFrameEvents.setStatus(_A)
_BrzaccVLFramesDelayedDueToSwRetry_Type=Counter32
_BrzaccVLFramesDelayedDueToSwRetry_Object=MibScalar
brzaccVLFramesDelayedDueToSwRetry=_BrzaccVLFramesDelayedDueToSwRetry_Object((1,3,6,1,4,1,12394,1,1,11,2,4,1,2),_BrzaccVLFramesDelayedDueToSwRetry_Type())
brzaccVLFramesDelayedDueToSwRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLFramesDelayedDueToSwRetry.setStatus(_A)
_BrzaccVLUnderrunEvents_Type=Counter32
_BrzaccVLUnderrunEvents_Object=MibScalar
brzaccVLUnderrunEvents=_BrzaccVLUnderrunEvents_Object((1,3,6,1,4,1,12394,1,1,11,2,4,1,3),_BrzaccVLUnderrunEvents_Type())
brzaccVLUnderrunEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUnderrunEvents.setStatus(_A)
_BrzaccVLOthersTxEvents_Type=Counter32
_BrzaccVLOthersTxEvents_Object=MibScalar
brzaccVLOthersTxEvents=_BrzaccVLOthersTxEvents_Object((1,3,6,1,4,1,12394,1,1,11,2,4,1,4),_BrzaccVLOthersTxEvents_Type())
brzaccVLOthersTxEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLOthersTxEvents.setStatus(_A)
_BrzaccVLTotalTxEvents_Type=Counter32
_BrzaccVLTotalTxEvents_Object=MibScalar
brzaccVLTotalTxEvents=_BrzaccVLTotalTxEvents_Object((1,3,6,1,4,1,12394,1,1,11,2,4,1,5),_BrzaccVLTotalTxEvents_Type())
brzaccVLTotalTxEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalTxEvents.setStatus(_A)
_BrzaccVLRxEvents_ObjectIdentity=ObjectIdentity
brzaccVLRxEvents=_BrzaccVLRxEvents_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,4,2))
_BrzaccVLPhyErrors_Type=Counter32
_BrzaccVLPhyErrors_Object=MibScalar
brzaccVLPhyErrors=_BrzaccVLPhyErrors_Object((1,3,6,1,4,1,12394,1,1,11,2,4,2,1),_BrzaccVLPhyErrors_Type())
brzaccVLPhyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLPhyErrors.setStatus(_A)
_BrzaccVLCRCErrors_Type=Counter32
_BrzaccVLCRCErrors_Object=MibScalar
brzaccVLCRCErrors=_BrzaccVLCRCErrors_Object((1,3,6,1,4,1,12394,1,1,11,2,4,2,2),_BrzaccVLCRCErrors_Type())
brzaccVLCRCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCRCErrors.setStatus(_A)
_BrzaccVLOverrunEvents_Type=Counter32
_BrzaccVLOverrunEvents_Object=MibScalar
brzaccVLOverrunEvents=_BrzaccVLOverrunEvents_Object((1,3,6,1,4,1,12394,1,1,11,2,4,2,3),_BrzaccVLOverrunEvents_Type())
brzaccVLOverrunEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLOverrunEvents.setStatus(_A)
_BrzaccVLRxDecryptEvents_Type=Counter32
_BrzaccVLRxDecryptEvents_Object=MibScalar
brzaccVLRxDecryptEvents=_BrzaccVLRxDecryptEvents_Object((1,3,6,1,4,1,12394,1,1,11,2,4,2,4),_BrzaccVLRxDecryptEvents_Type())
brzaccVLRxDecryptEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLRxDecryptEvents.setStatus(_A)
_BrzaccVLTotalRxEvents_Type=Counter32
_BrzaccVLTotalRxEvents_Object=MibScalar
brzaccVLTotalRxEvents=_BrzaccVLTotalRxEvents_Object((1,3,6,1,4,1,12394,1,1,11,2,4,2,5),_BrzaccVLTotalRxEvents_Type())
brzaccVLTotalRxEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTotalRxEvents.setStatus(_A)
_BrzaccVLPerModulationLevelCounters_ObjectIdentity=ObjectIdentity
brzaccVLPerModulationLevelCounters=_BrzaccVLPerModulationLevelCounters_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,2,5))
class _BrzaccVLResetPerModulationLevelCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Al,1),(_K,2)))
_BrzaccVLResetPerModulationLevelCounters_Type.__name__=_C
_BrzaccVLResetPerModulationLevelCounters_Object=MibScalar
brzaccVLResetPerModulationLevelCounters=_BrzaccVLResetPerModulationLevelCounters_Object((1,3,6,1,4,1,12394,1,1,11,2,5,1),_BrzaccVLResetPerModulationLevelCounters_Type())
brzaccVLResetPerModulationLevelCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLResetPerModulationLevelCounters.setStatus(_A)
_BrzaccVLSUPerModulationLevelCountersTable_Object=MibTable
brzaccVLSUPerModulationLevelCountersTable=_BrzaccVLSUPerModulationLevelCountersTable_Object((1,3,6,1,4,1,12394,1,1,11,2,5,2))
if mibBuilder.loadTexts:brzaccVLSUPerModulationLevelCountersTable.setStatus(_A)
_BrzaccVLSUPerModulationLevelCountersEntry_Object=MibTableRow
brzaccVLSUPerModulationLevelCountersEntry=_BrzaccVLSUPerModulationLevelCountersEntry_Object((1,3,6,1,4,1,12394,1,1,11,2,5,2,1))
brzaccVLSUPerModulationLevelCountersEntry.setIndexNames((0,_E,_Az))
if mibBuilder.loadTexts:brzaccVLSUPerModulationLevelCountersEntry.setStatus(_A)
class _BrzaccVLSUPerModulationLevelCountersTableIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BrzaccVLSUPerModulationLevelCountersTableIdx_Type.__name__=_C
_BrzaccVLSUPerModulationLevelCountersTableIdx_Object=MibTableColumn
brzaccVLSUPerModulationLevelCountersTableIdx=_BrzaccVLSUPerModulationLevelCountersTableIdx_Object((1,3,6,1,4,1,12394,1,1,11,2,5,2,1,1),_BrzaccVLSUPerModulationLevelCountersTableIdx_Type())
brzaccVLSUPerModulationLevelCountersTableIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSUPerModulationLevelCountersTableIdx.setStatus(_A)
class _BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3),(_A2,4),(_A3,5),(_A4,6),(_A5,7),(_A6,8)))
_BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Type.__name__=_C
_BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Object=MibTableColumn
brzaccVLSUPerModulationLevelCountersApplicableModLevel=_BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Object((1,3,6,1,4,1,12394,1,1,11,2,5,2,1,2),_BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Type())
brzaccVLSUPerModulationLevelCountersApplicableModLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSUPerModulationLevelCountersApplicableModLevel.setStatus(_A)
_BrzaccVLSUPerModulationLevelCountersTxSuccess_Type=Counter32
_BrzaccVLSUPerModulationLevelCountersTxSuccess_Object=MibTableColumn
brzaccVLSUPerModulationLevelCountersTxSuccess=_BrzaccVLSUPerModulationLevelCountersTxSuccess_Object((1,3,6,1,4,1,12394,1,1,11,2,5,2,1,3),_BrzaccVLSUPerModulationLevelCountersTxSuccess_Type())
brzaccVLSUPerModulationLevelCountersTxSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSUPerModulationLevelCountersTxSuccess.setStatus(_A)
_BrzaccVLSUPerModulationLevelCountersTxFailed_Type=Counter32
_BrzaccVLSUPerModulationLevelCountersTxFailed_Object=MibTableColumn
brzaccVLSUPerModulationLevelCountersTxFailed=_BrzaccVLSUPerModulationLevelCountersTxFailed_Object((1,3,6,1,4,1,12394,1,1,11,2,5,2,1,4),_BrzaccVLSUPerModulationLevelCountersTxFailed_Type())
brzaccVLSUPerModulationLevelCountersTxFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLSUPerModulationLevelCountersTxFailed.setStatus(_A)
_BrzaccVLAverageModulationLevel_Type=Integer32
_BrzaccVLAverageModulationLevel_Object=MibScalar
brzaccVLAverageModulationLevel=_BrzaccVLAverageModulationLevel_Object((1,3,6,1,4,1,12394,1,1,11,2,5,3),_BrzaccVLAverageModulationLevel_Type())
brzaccVLAverageModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAverageModulationLevel.setStatus(_A)
_BrzaccVLMacAddressDatabase_ObjectIdentity=ObjectIdentity
brzaccVLMacAddressDatabase=_BrzaccVLMacAddressDatabase_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,5))
_BrzaccVLAUMacAddressDatabase_ObjectIdentity=ObjectIdentity
brzaccVLAUMacAddressDatabase=_BrzaccVLAUMacAddressDatabase_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,5,1))
class _BrzaccVLAUAdbResetAllModulationLevelCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_K,2)))
_BrzaccVLAUAdbResetAllModulationLevelCounters_Type.__name__=_C
_BrzaccVLAUAdbResetAllModulationLevelCounters_Object=MibScalar
brzaccVLAUAdbResetAllModulationLevelCounters=_BrzaccVLAUAdbResetAllModulationLevelCounters_Object((1,3,6,1,4,1,12394,1,1,11,5,1,1),_BrzaccVLAUAdbResetAllModulationLevelCounters_Type())
brzaccVLAUAdbResetAllModulationLevelCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLAUAdbResetAllModulationLevelCounters.setStatus(_A)
_BrzaccVLAUAdbTable_Object=MibTable
brzaccVLAUAdbTable=_BrzaccVLAUAdbTable_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2))
if mibBuilder.loadTexts:brzaccVLAUAdbTable.setStatus(_A)
_BrzaccVLAUAdbEntry_Object=MibTableRow
brzaccVLAUAdbEntry=_BrzaccVLAUAdbEntry_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1))
brzaccVLAUAdbEntry.setIndexNames((0,_E,_A_))
if mibBuilder.loadTexts:brzaccVLAUAdbEntry.setStatus(_A)
class _BrzaccVLAdbIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_BrzaccVLAdbIndex_Type.__name__=_C
_BrzaccVLAdbIndex_Object=MibTableColumn
brzaccVLAdbIndex=_BrzaccVLAdbIndex_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,1),_BrzaccVLAdbIndex_Type())
brzaccVLAdbIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbIndex.setStatus(_A)
_BrzaccVLAdbMacAddress_Type=MacAddress
_BrzaccVLAdbMacAddress_Object=MibTableColumn
brzaccVLAdbMacAddress=_BrzaccVLAdbMacAddress_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,2),_BrzaccVLAdbMacAddress_Type())
brzaccVLAdbMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbMacAddress.setStatus(_A)
class _BrzaccVLAdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_B0,1),(_B1,2),(_B2,3)))
_BrzaccVLAdbStatus_Type.__name__=_C
_BrzaccVLAdbStatus_Object=MibTableColumn
brzaccVLAdbStatus=_BrzaccVLAdbStatus_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,3),_BrzaccVLAdbStatus_Type())
brzaccVLAdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbStatus.setStatus(_A)
_BrzaccVLAdbSwVersion_Type=DisplayString
_BrzaccVLAdbSwVersion_Object=MibTableColumn
brzaccVLAdbSwVersion=_BrzaccVLAdbSwVersion_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,4),_BrzaccVLAdbSwVersion_Type())
brzaccVLAdbSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbSwVersion.setStatus(_A)
_BrzaccVLAdbSNR_Type=Integer32
_BrzaccVLAdbSNR_Object=MibTableColumn
brzaccVLAdbSNR=_BrzaccVLAdbSNR_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,5),_BrzaccVLAdbSNR_Type())
brzaccVLAdbSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbSNR.setStatus(_A)
class _BrzaccVLAdbMaxModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3),(_A2,4),(_A3,5),(_A4,6),(_A5,7),(_A6,8),(_F,255)))
_BrzaccVLAdbMaxModulationLevel_Type.__name__=_C
_BrzaccVLAdbMaxModulationLevel_Object=MibTableColumn
brzaccVLAdbMaxModulationLevel=_BrzaccVLAdbMaxModulationLevel_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,6),_BrzaccVLAdbMaxModulationLevel_Type())
brzaccVLAdbMaxModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbMaxModulationLevel.setStatus(_A)
_BrzaccVLAdbTxFramesTotal_Type=Counter32
_BrzaccVLAdbTxFramesTotal_Object=MibTableColumn
brzaccVLAdbTxFramesTotal=_BrzaccVLAdbTxFramesTotal_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,7),_BrzaccVLAdbTxFramesTotal_Type())
brzaccVLAdbTxFramesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFramesTotal.setStatus(_A)
_BrzaccVLAdbDroppedFramesTotal_Type=Counter32
_BrzaccVLAdbDroppedFramesTotal_Object=MibTableColumn
brzaccVLAdbDroppedFramesTotal=_BrzaccVLAdbDroppedFramesTotal_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,8),_BrzaccVLAdbDroppedFramesTotal_Type())
brzaccVLAdbDroppedFramesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbDroppedFramesTotal.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel1_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel1_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel1=_BrzaccVLAdbTxSuccessModLevel1_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,9),_BrzaccVLAdbTxSuccessModLevel1_Type())
brzaccVLAdbTxSuccessModLevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel1.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel2_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel2_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel2=_BrzaccVLAdbTxSuccessModLevel2_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,10),_BrzaccVLAdbTxSuccessModLevel2_Type())
brzaccVLAdbTxSuccessModLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel2.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel3_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel3_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel3=_BrzaccVLAdbTxSuccessModLevel3_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,11),_BrzaccVLAdbTxSuccessModLevel3_Type())
brzaccVLAdbTxSuccessModLevel3.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel3.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel4_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel4_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel4=_BrzaccVLAdbTxSuccessModLevel4_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,12),_BrzaccVLAdbTxSuccessModLevel4_Type())
brzaccVLAdbTxSuccessModLevel4.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel4.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel5_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel5_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel5=_BrzaccVLAdbTxSuccessModLevel5_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,13),_BrzaccVLAdbTxSuccessModLevel5_Type())
brzaccVLAdbTxSuccessModLevel5.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel5.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel6_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel6_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel6=_BrzaccVLAdbTxSuccessModLevel6_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,14),_BrzaccVLAdbTxSuccessModLevel6_Type())
brzaccVLAdbTxSuccessModLevel6.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel6.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel7_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel7_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel7=_BrzaccVLAdbTxSuccessModLevel7_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,15),_BrzaccVLAdbTxSuccessModLevel7_Type())
brzaccVLAdbTxSuccessModLevel7.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel7.setStatus(_A)
_BrzaccVLAdbTxSuccessModLevel8_Type=Counter32
_BrzaccVLAdbTxSuccessModLevel8_Object=MibTableColumn
brzaccVLAdbTxSuccessModLevel8=_BrzaccVLAdbTxSuccessModLevel8_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,16),_BrzaccVLAdbTxSuccessModLevel8_Type())
brzaccVLAdbTxSuccessModLevel8.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxSuccessModLevel8.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel1_Type=Counter32
_BrzaccVLAdbTxFailedModLevel1_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel1=_BrzaccVLAdbTxFailedModLevel1_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,17),_BrzaccVLAdbTxFailedModLevel1_Type())
brzaccVLAdbTxFailedModLevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel1.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel2_Type=Counter32
_BrzaccVLAdbTxFailedModLevel2_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel2=_BrzaccVLAdbTxFailedModLevel2_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,18),_BrzaccVLAdbTxFailedModLevel2_Type())
brzaccVLAdbTxFailedModLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel2.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel3_Type=Counter32
_BrzaccVLAdbTxFailedModLevel3_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel3=_BrzaccVLAdbTxFailedModLevel3_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,19),_BrzaccVLAdbTxFailedModLevel3_Type())
brzaccVLAdbTxFailedModLevel3.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel3.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel4_Type=Counter32
_BrzaccVLAdbTxFailedModLevel4_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel4=_BrzaccVLAdbTxFailedModLevel4_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,20),_BrzaccVLAdbTxFailedModLevel4_Type())
brzaccVLAdbTxFailedModLevel4.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel4.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel5_Type=Counter32
_BrzaccVLAdbTxFailedModLevel5_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel5=_BrzaccVLAdbTxFailedModLevel5_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,21),_BrzaccVLAdbTxFailedModLevel5_Type())
brzaccVLAdbTxFailedModLevel5.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel5.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel6_Type=Counter32
_BrzaccVLAdbTxFailedModLevel6_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel6=_BrzaccVLAdbTxFailedModLevel6_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,22),_BrzaccVLAdbTxFailedModLevel6_Type())
brzaccVLAdbTxFailedModLevel6.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel6.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel7_Type=Counter32
_BrzaccVLAdbTxFailedModLevel7_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel7=_BrzaccVLAdbTxFailedModLevel7_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,23),_BrzaccVLAdbTxFailedModLevel7_Type())
brzaccVLAdbTxFailedModLevel7.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel7.setStatus(_A)
_BrzaccVLAdbTxFailedModLevel8_Type=Counter32
_BrzaccVLAdbTxFailedModLevel8_Object=MibTableColumn
brzaccVLAdbTxFailedModLevel8=_BrzaccVLAdbTxFailedModLevel8_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,24),_BrzaccVLAdbTxFailedModLevel8_Type())
brzaccVLAdbTxFailedModLevel8.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbTxFailedModLevel8.setStatus(_A)
_BrzaccVLAdbCirTx_Type=Integer32
_BrzaccVLAdbCirTx_Object=MibTableColumn
brzaccVLAdbCirTx=_BrzaccVLAdbCirTx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,25),_BrzaccVLAdbCirTx_Type())
brzaccVLAdbCirTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbCirTx.setStatus(_A)
_BrzaccVLAdbMirTx_Type=Integer32
_BrzaccVLAdbMirTx_Object=MibTableColumn
brzaccVLAdbMirTx=_BrzaccVLAdbMirTx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,26),_BrzaccVLAdbMirTx_Type())
brzaccVLAdbMirTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbMirTx.setStatus(_A)
_BrzaccVLAdbCirRx_Type=Integer32
_BrzaccVLAdbCirRx_Object=MibTableColumn
brzaccVLAdbCirRx=_BrzaccVLAdbCirRx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,27),_BrzaccVLAdbCirRx_Type())
brzaccVLAdbCirRx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbCirRx.setStatus(_A)
_BrzaccVLAdbMirRx_Type=Integer32
_BrzaccVLAdbMirRx_Object=MibTableColumn
brzaccVLAdbMirRx=_BrzaccVLAdbMirRx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,28),_BrzaccVLAdbMirRx_Type())
brzaccVLAdbMirRx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbMirRx.setStatus(_A)
_BrzaccVLAdbCirMaxDelay_Type=Integer32
_BrzaccVLAdbCirMaxDelay_Object=MibTableColumn
brzaccVLAdbCirMaxDelay=_BrzaccVLAdbCirMaxDelay_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,29),_BrzaccVLAdbCirMaxDelay_Type())
brzaccVLAdbCirMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbCirMaxDelay.setStatus(_A)
class _BrzaccVLAdbDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_w,1))
_BrzaccVLAdbDistance_Type.__name__=_C
_BrzaccVLAdbDistance_Object=MibTableColumn
brzaccVLAdbDistance=_BrzaccVLAdbDistance_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,30),_BrzaccVLAdbDistance_Type())
brzaccVLAdbDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbDistance.setStatus(_A)
class _BrzaccVLAdbHwRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_F,255)))
_BrzaccVLAdbHwRevision_Type.__name__=_C
_BrzaccVLAdbHwRevision_Object=MibTableColumn
brzaccVLAdbHwRevision=_BrzaccVLAdbHwRevision_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,31),_BrzaccVLAdbHwRevision_Type())
brzaccVLAdbHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbHwRevision.setStatus(_A)
_BrzaccVLAdbCpldVer_Type=DisplayString
_BrzaccVLAdbCpldVer_Object=MibTableColumn
brzaccVLAdbCpldVer=_BrzaccVLAdbCpldVer_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,32),_BrzaccVLAdbCpldVer_Type())
brzaccVLAdbCpldVer.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbCpldVer.setStatus(_A)
_BrzaccVLAdbCountryCode_Type=Integer32
_BrzaccVLAdbCountryCode_Object=MibTableColumn
brzaccVLAdbCountryCode=_BrzaccVLAdbCountryCode_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,33),_BrzaccVLAdbCountryCode_Type())
brzaccVLAdbCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbCountryCode.setStatus(_A)
_BrzaccVLAdbBootVer_Type=DisplayString
_BrzaccVLAdbBootVer_Object=MibTableColumn
brzaccVLAdbBootVer=_BrzaccVLAdbBootVer_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,34),_BrzaccVLAdbBootVer_Type())
brzaccVLAdbBootVer.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbBootVer.setStatus(_A)
class _BrzaccVLAdbAtpcOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAdbAtpcOption_Type.__name__=_C
_BrzaccVLAdbAtpcOption_Object=MibTableColumn
brzaccVLAdbAtpcOption=_BrzaccVLAdbAtpcOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,35),_BrzaccVLAdbAtpcOption_Type())
brzaccVLAdbAtpcOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbAtpcOption.setStatus(_A)
class _BrzaccVLAdbAdapModOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAdbAdapModOption_Type.__name__=_C
_BrzaccVLAdbAdapModOption_Object=MibTableColumn
brzaccVLAdbAdapModOption=_BrzaccVLAdbAdapModOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,36),_BrzaccVLAdbAdapModOption_Type())
brzaccVLAdbAdapModOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbAdapModOption.setStatus(_A)
class _BrzaccVLAdbBurstModeOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAdbBurstModeOption_Type.__name__=_C
_BrzaccVLAdbBurstModeOption_Object=MibTableColumn
brzaccVLAdbBurstModeOption=_BrzaccVLAdbBurstModeOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,37),_BrzaccVLAdbBurstModeOption_Type())
brzaccVLAdbBurstModeOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbBurstModeOption.setStatus(_A)
class _BrzaccVLAdbConcatenationOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAdbConcatenationOption_Type.__name__=_C
_BrzaccVLAdbConcatenationOption_Object=MibTableColumn
brzaccVLAdbConcatenationOption=_BrzaccVLAdbConcatenationOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,39),_BrzaccVLAdbConcatenationOption_Type())
brzaccVLAdbConcatenationOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbConcatenationOption.setStatus(_A)
class _BrzaccVLAdbSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_o,1),('aes',2),(_p,3),(_F,255)))
_BrzaccVLAdbSecurityMode_Type.__name__=_C
_BrzaccVLAdbSecurityMode_Object=MibTableColumn
brzaccVLAdbSecurityMode=_BrzaccVLAdbSecurityMode_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,41),_BrzaccVLAdbSecurityMode_Type())
brzaccVLAdbSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbSecurityMode.setStatus(_A)
class _BrzaccVLAdbAuthOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_q,1),(_r,2),(_F,255)))
_BrzaccVLAdbAuthOption_Type.__name__=_C
_BrzaccVLAdbAuthOption_Object=MibTableColumn
brzaccVLAdbAuthOption=_BrzaccVLAdbAuthOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,42),_BrzaccVLAdbAuthOption_Type())
brzaccVLAdbAuthOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbAuthOption.setStatus(_A)
class _BrzaccVLAdbDataEncyptOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLAdbDataEncyptOption_Type.__name__=_C
_BrzaccVLAdbDataEncyptOption_Object=MibTableColumn
brzaccVLAdbDataEncyptOption=_BrzaccVLAdbDataEncyptOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,43),_BrzaccVLAdbDataEncyptOption_Type())
brzaccVLAdbDataEncyptOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbDataEncyptOption.setStatus(_A)
_BrzaccVLAdbAge_Type=Integer32
_BrzaccVLAdbAge_Object=MibTableColumn
brzaccVLAdbAge=_BrzaccVLAdbAge_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,44),_BrzaccVLAdbAge_Type())
brzaccVLAdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbAge.setStatus(_A)
_BrzaccVLAdbUnitName_Type=DisplayString
_BrzaccVLAdbUnitName_Object=MibTableColumn
brzaccVLAdbUnitName=_BrzaccVLAdbUnitName_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,45),_BrzaccVLAdbUnitName_Type())
brzaccVLAdbUnitName.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbUnitName.setStatus(_A)
_BrzaccVLAdbRSSI_Type=Integer32
_BrzaccVLAdbRSSI_Object=MibTableColumn
brzaccVLAdbRSSI=_BrzaccVLAdbRSSI_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,46),_BrzaccVLAdbRSSI_Type())
brzaccVLAdbRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbRSSI.setStatus(_A)
_BrzaccVLAdbIpAddress_Type=IpAddress
_BrzaccVLAdbIpAddress_Object=MibTableColumn
brzaccVLAdbIpAddress=_BrzaccVLAdbIpAddress_Object((1,3,6,1,4,1,12394,1,1,11,5,1,2,1,47),_BrzaccVLAdbIpAddress_Type())
brzaccVLAdbIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbIpAddress.setStatus(_A)
_BrzaccVLAUNewAdbTable_Object=MibTable
brzaccVLAUNewAdbTable=_BrzaccVLAUNewAdbTable_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3))
if mibBuilder.loadTexts:brzaccVLAUNewAdbTable.setStatus(_A)
_BrzaccVLAUNewAdbEntry_Object=MibTableRow
brzaccVLAUNewAdbEntry=_BrzaccVLAUNewAdbEntry_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1))
brzaccVLAUNewAdbEntry.setIndexNames((0,_E,_B3))
if mibBuilder.loadTexts:brzaccVLAUNewAdbEntry.setStatus(_A)
_BrzaccVLNewAdbMacAddress_Type=MacAddress
_BrzaccVLNewAdbMacAddress_Object=MibTableColumn
brzaccVLNewAdbMacAddress=_BrzaccVLNewAdbMacAddress_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,1),_BrzaccVLNewAdbMacAddress_Type())
brzaccVLNewAdbMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbMacAddress.setStatus(_A)
_BrzaccVLNewAdbIPaddress_Type=IpAddress
_BrzaccVLNewAdbIPaddress_Object=MibTableColumn
brzaccVLNewAdbIPaddress=_BrzaccVLNewAdbIPaddress_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,2),_BrzaccVLNewAdbIPaddress_Type())
brzaccVLNewAdbIPaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbIPaddress.setStatus(_A)
_BrzaccVLNewAdbUnitName_Type=DisplayString
_BrzaccVLNewAdbUnitName_Object=MibTableColumn
brzaccVLNewAdbUnitName=_BrzaccVLNewAdbUnitName_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,3),_BrzaccVLNewAdbUnitName_Type())
brzaccVLNewAdbUnitName.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbUnitName.setStatus(_A)
class _BrzaccVLNewAdbUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,8,9,10,11,12,13,18,20,21,23,24,26,27,28,29,30,31,33,255)));namedValues=NamedValues(*(('su-6-1D',3),('su-6-BD',4),('su-24-BD',5),('rb-B14',8),('rb-B28',9),('su-BD',10),('su-54-BD',11),('su-3-1D',12),('su-3-4D',13),('su4900',18),('rb-B100',20),('su-I',21),('su-EZ',23),('su-V',24),('rb-B10',26),('su-8-BD',27),('su-1-BD',28),('su-3-L',29),('su-6-L',30),('su-12-L',31),('su',33),(_F,255)))
_BrzaccVLNewAdbUnitType_Type.__name__=_C
_BrzaccVLNewAdbUnitType_Object=MibTableColumn
brzaccVLNewAdbUnitType=_BrzaccVLNewAdbUnitType_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,4),_BrzaccVLNewAdbUnitType_Type())
brzaccVLNewAdbUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbUnitType.setStatus(_A)
_BrzaccVLNewAdbSwVersion_Type=DisplayString
_BrzaccVLNewAdbSwVersion_Object=MibTableColumn
brzaccVLNewAdbSwVersion=_BrzaccVLNewAdbSwVersion_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,5),_BrzaccVLNewAdbSwVersion_Type())
brzaccVLNewAdbSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbSwVersion.setStatus(_A)
class _BrzaccVLNewAdbHwRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7),(_F,255)))
_BrzaccVLNewAdbHwRevision_Type.__name__=_C
_BrzaccVLNewAdbHwRevision_Object=MibTableColumn
brzaccVLNewAdbHwRevision=_BrzaccVLNewAdbHwRevision_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,6),_BrzaccVLNewAdbHwRevision_Type())
brzaccVLNewAdbHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbHwRevision.setStatus(_A)
_BrzaccVLNewAdbCpldVer_Type=DisplayString
_BrzaccVLNewAdbCpldVer_Object=MibTableColumn
brzaccVLNewAdbCpldVer=_BrzaccVLNewAdbCpldVer_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,7),_BrzaccVLNewAdbCpldVer_Type())
brzaccVLNewAdbCpldVer.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbCpldVer.setStatus(_A)
_BrzaccVLNewAdbBootVer_Type=DisplayString
_BrzaccVLNewAdbBootVer_Object=MibTableColumn
brzaccVLNewAdbBootVer=_BrzaccVLNewAdbBootVer_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,8),_BrzaccVLNewAdbBootVer_Type())
brzaccVLNewAdbBootVer.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbBootVer.setStatus(_A)
_BrzaccVLNewAdbCountryCode_Type=Integer32
_BrzaccVLNewAdbCountryCode_Object=MibTableColumn
brzaccVLNewAdbCountryCode=_BrzaccVLNewAdbCountryCode_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,9),_BrzaccVLNewAdbCountryCode_Type())
brzaccVLNewAdbCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbCountryCode.setStatus(_A)
_BrzaccVLNewAdbCirTx_Type=Integer32
_BrzaccVLNewAdbCirTx_Object=MibTableColumn
brzaccVLNewAdbCirTx=_BrzaccVLNewAdbCirTx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,10),_BrzaccVLNewAdbCirTx_Type())
brzaccVLNewAdbCirTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbCirTx.setStatus(_A)
_BrzaccVLNewAdbMirTx_Type=Integer32
_BrzaccVLNewAdbMirTx_Object=MibTableColumn
brzaccVLNewAdbMirTx=_BrzaccVLNewAdbMirTx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,11),_BrzaccVLNewAdbMirTx_Type())
brzaccVLNewAdbMirTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbMirTx.setStatus(_A)
_BrzaccVLNewAdbCirRx_Type=Integer32
_BrzaccVLNewAdbCirRx_Object=MibTableColumn
brzaccVLNewAdbCirRx=_BrzaccVLNewAdbCirRx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,12),_BrzaccVLNewAdbCirRx_Type())
brzaccVLNewAdbCirRx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbCirRx.setStatus(_A)
_BrzaccVLNewAdbMirRx_Type=Integer32
_BrzaccVLNewAdbMirRx_Object=MibTableColumn
brzaccVLNewAdbMirRx=_BrzaccVLNewAdbMirRx_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,13),_BrzaccVLNewAdbMirRx_Type())
brzaccVLNewAdbMirRx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbMirRx.setStatus(_A)
_BrzaccVLNewAdbCirMaxDelay_Type=Integer32
_BrzaccVLNewAdbCirMaxDelay_Object=MibTableColumn
brzaccVLNewAdbCirMaxDelay=_BrzaccVLNewAdbCirMaxDelay_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,14),_BrzaccVLNewAdbCirMaxDelay_Type())
brzaccVLNewAdbCirMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbCirMaxDelay.setStatus(_A)
class _BrzaccVLNewAdbAtpcOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNewAdbAtpcOption_Type.__name__=_C
_BrzaccVLNewAdbAtpcOption_Object=MibTableColumn
brzaccVLNewAdbAtpcOption=_BrzaccVLNewAdbAtpcOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,15),_BrzaccVLNewAdbAtpcOption_Type())
brzaccVLNewAdbAtpcOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbAtpcOption.setStatus(_A)
class _BrzaccVLNewAdbAdapModOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNewAdbAdapModOption_Type.__name__=_C
_BrzaccVLNewAdbAdapModOption_Object=MibTableColumn
brzaccVLNewAdbAdapModOption=_BrzaccVLNewAdbAdapModOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,16),_BrzaccVLNewAdbAdapModOption_Type())
brzaccVLNewAdbAdapModOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbAdapModOption.setStatus(_A)
class _BrzaccVLNewAdbBurstModeOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNewAdbBurstModeOption_Type.__name__=_C
_BrzaccVLNewAdbBurstModeOption_Object=MibTableColumn
brzaccVLNewAdbBurstModeOption=_BrzaccVLNewAdbBurstModeOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,17),_BrzaccVLNewAdbBurstModeOption_Type())
brzaccVLNewAdbBurstModeOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbBurstModeOption.setStatus(_A)
class _BrzaccVLNewAdbConcatenationOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNewAdbConcatenationOption_Type.__name__=_C
_BrzaccVLNewAdbConcatenationOption_Object=MibTableColumn
brzaccVLNewAdbConcatenationOption=_BrzaccVLNewAdbConcatenationOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,18),_BrzaccVLNewAdbConcatenationOption_Type())
brzaccVLNewAdbConcatenationOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbConcatenationOption.setStatus(_A)
class _BrzaccVLNewAdbSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_o,1),('aes',2),(_p,3),(_F,255)))
_BrzaccVLNewAdbSecurityMode_Type.__name__=_C
_BrzaccVLNewAdbSecurityMode_Object=MibTableColumn
brzaccVLNewAdbSecurityMode=_BrzaccVLNewAdbSecurityMode_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,19),_BrzaccVLNewAdbSecurityMode_Type())
brzaccVLNewAdbSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbSecurityMode.setStatus(_A)
class _BrzaccVLNewAdbAuthOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_q,1),(_r,2),(_F,255)))
_BrzaccVLNewAdbAuthOption_Type.__name__=_C
_BrzaccVLNewAdbAuthOption_Object=MibTableColumn
brzaccVLNewAdbAuthOption=_BrzaccVLNewAdbAuthOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,20),_BrzaccVLNewAdbAuthOption_Type())
brzaccVLNewAdbAuthOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbAuthOption.setStatus(_A)
class _BrzaccVLNewAdbDataEncyptOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_F,255)))
_BrzaccVLNewAdbDataEncyptOption_Type.__name__=_C
_BrzaccVLNewAdbDataEncyptOption_Object=MibTableColumn
brzaccVLNewAdbDataEncyptOption=_BrzaccVLNewAdbDataEncyptOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,21),_BrzaccVLNewAdbDataEncyptOption_Type())
brzaccVLNewAdbDataEncyptOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbDataEncyptOption.setStatus(_A)
_BrzaccVLAdbWi2IPaddress_Type=IpAddress
_BrzaccVLAdbWi2IPaddress_Object=MibTableColumn
brzaccVLAdbWi2IPaddress=_BrzaccVLAdbWi2IPaddress_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,22),_BrzaccVLAdbWi2IPaddress_Type())
brzaccVLAdbWi2IPaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAdbWi2IPaddress.setStatus(_A)
class _BrzaccVLNewAdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_B0,1),(_B1,2),(_B2,3)))
_BrzaccVLNewAdbStatus_Type.__name__=_C
_BrzaccVLNewAdbStatus_Object=MibTableColumn
brzaccVLNewAdbStatus=_BrzaccVLNewAdbStatus_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,23),_BrzaccVLNewAdbStatus_Type())
brzaccVLNewAdbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbStatus.setStatus(_A)
_BrzaccVLNewAdbAge_Type=Integer32
_BrzaccVLNewAdbAge_Object=MibTableColumn
brzaccVLNewAdbAge=_BrzaccVLNewAdbAge_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,24),_BrzaccVLNewAdbAge_Type())
brzaccVLNewAdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbAge.setStatus(_A)
class _BrzaccVLNewAdbDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_w,1))
_BrzaccVLNewAdbDistance_Type.__name__=_C
_BrzaccVLNewAdbDistance_Object=MibTableColumn
brzaccVLNewAdbDistance=_BrzaccVLNewAdbDistance_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,25),_BrzaccVLNewAdbDistance_Type())
brzaccVLNewAdbDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbDistance.setStatus(_A)
_BrzaccVLNewAdbSNR_Type=Integer32
_BrzaccVLNewAdbSNR_Object=MibTableColumn
brzaccVLNewAdbSNR=_BrzaccVLNewAdbSNR_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,26),_BrzaccVLNewAdbSNR_Type())
brzaccVLNewAdbSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbSNR.setStatus(_A)
class _BrzaccVLNewAdbMaxModulationLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3),(_A2,4),(_A3,5),(_A4,6),(_A5,7),(_A6,8),(_F,255)))
_BrzaccVLNewAdbMaxModulationLevel_Type.__name__=_C
_BrzaccVLNewAdbMaxModulationLevel_Object=MibTableColumn
brzaccVLNewAdbMaxModulationLevel=_BrzaccVLNewAdbMaxModulationLevel_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,27),_BrzaccVLNewAdbMaxModulationLevel_Type())
brzaccVLNewAdbMaxModulationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbMaxModulationLevel.setStatus(_A)
_BrzaccVLNewAdbTxFramesTotal_Type=Counter32
_BrzaccVLNewAdbTxFramesTotal_Object=MibTableColumn
brzaccVLNewAdbTxFramesTotal=_BrzaccVLNewAdbTxFramesTotal_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,28),_BrzaccVLNewAdbTxFramesTotal_Type())
brzaccVLNewAdbTxFramesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFramesTotal.setStatus(_A)
_BrzaccVLNewAdbDroppedFramesTotal_Type=Counter32
_BrzaccVLNewAdbDroppedFramesTotal_Object=MibTableColumn
brzaccVLNewAdbDroppedFramesTotal=_BrzaccVLNewAdbDroppedFramesTotal_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,29),_BrzaccVLNewAdbDroppedFramesTotal_Type())
brzaccVLNewAdbDroppedFramesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbDroppedFramesTotal.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel1_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel1_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel1=_BrzaccVLNewAdbTxSuccessModLevel1_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,30),_BrzaccVLNewAdbTxSuccessModLevel1_Type())
brzaccVLNewAdbTxSuccessModLevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel1.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel2_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel2_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel2=_BrzaccVLNewAdbTxSuccessModLevel2_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,31),_BrzaccVLNewAdbTxSuccessModLevel2_Type())
brzaccVLNewAdbTxSuccessModLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel2.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel3_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel3_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel3=_BrzaccVLNewAdbTxSuccessModLevel3_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,32),_BrzaccVLNewAdbTxSuccessModLevel3_Type())
brzaccVLNewAdbTxSuccessModLevel3.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel3.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel4_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel4_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel4=_BrzaccVLNewAdbTxSuccessModLevel4_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,33),_BrzaccVLNewAdbTxSuccessModLevel4_Type())
brzaccVLNewAdbTxSuccessModLevel4.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel4.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel5_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel5_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel5=_BrzaccVLNewAdbTxSuccessModLevel5_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,34),_BrzaccVLNewAdbTxSuccessModLevel5_Type())
brzaccVLNewAdbTxSuccessModLevel5.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel5.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel6_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel6_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel6=_BrzaccVLNewAdbTxSuccessModLevel6_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,35),_BrzaccVLNewAdbTxSuccessModLevel6_Type())
brzaccVLNewAdbTxSuccessModLevel6.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel6.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel7_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel7_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel7=_BrzaccVLNewAdbTxSuccessModLevel7_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,36),_BrzaccVLNewAdbTxSuccessModLevel7_Type())
brzaccVLNewAdbTxSuccessModLevel7.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel7.setStatus(_A)
_BrzaccVLNewAdbTxSuccessModLevel8_Type=Counter32
_BrzaccVLNewAdbTxSuccessModLevel8_Object=MibTableColumn
brzaccVLNewAdbTxSuccessModLevel8=_BrzaccVLNewAdbTxSuccessModLevel8_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,37),_BrzaccVLNewAdbTxSuccessModLevel8_Type())
brzaccVLNewAdbTxSuccessModLevel8.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxSuccessModLevel8.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel1_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel1_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel1=_BrzaccVLNewAdbTxFailedModLevel1_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,38),_BrzaccVLNewAdbTxFailedModLevel1_Type())
brzaccVLNewAdbTxFailedModLevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel1.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel2_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel2_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel2=_BrzaccVLNewAdbTxFailedModLevel2_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,39),_BrzaccVLNewAdbTxFailedModLevel2_Type())
brzaccVLNewAdbTxFailedModLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel2.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel3_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel3_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel3=_BrzaccVLNewAdbTxFailedModLevel3_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,40),_BrzaccVLNewAdbTxFailedModLevel3_Type())
brzaccVLNewAdbTxFailedModLevel3.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel3.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel4_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel4_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel4=_BrzaccVLNewAdbTxFailedModLevel4_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,41),_BrzaccVLNewAdbTxFailedModLevel4_Type())
brzaccVLNewAdbTxFailedModLevel4.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel4.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel5_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel5_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel5=_BrzaccVLNewAdbTxFailedModLevel5_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,42),_BrzaccVLNewAdbTxFailedModLevel5_Type())
brzaccVLNewAdbTxFailedModLevel5.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel5.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel6_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel6_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel6=_BrzaccVLNewAdbTxFailedModLevel6_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,43),_BrzaccVLNewAdbTxFailedModLevel6_Type())
brzaccVLNewAdbTxFailedModLevel6.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel6.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel7_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel7_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel7=_BrzaccVLNewAdbTxFailedModLevel7_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,44),_BrzaccVLNewAdbTxFailedModLevel7_Type())
brzaccVLNewAdbTxFailedModLevel7.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel7.setStatus(_A)
_BrzaccVLNewAdbTxFailedModLevel8_Type=Counter32
_BrzaccVLNewAdbTxFailedModLevel8_Object=MibTableColumn
brzaccVLNewAdbTxFailedModLevel8=_BrzaccVLNewAdbTxFailedModLevel8_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,45),_BrzaccVLNewAdbTxFailedModLevel8_Type())
brzaccVLNewAdbTxFailedModLevel8.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbTxFailedModLevel8.setStatus(_A)
class _BrzaccVLNewAdbMainSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_BrzaccVLNewAdbMainSwVersion_Type.__name__=_I
_BrzaccVLNewAdbMainSwVersion_Object=MibTableColumn
brzaccVLNewAdbMainSwVersion=_BrzaccVLNewAdbMainSwVersion_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,46),_BrzaccVLNewAdbMainSwVersion_Type())
brzaccVLNewAdbMainSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbMainSwVersion.setStatus(_A)
class _BrzaccVLNewAdbShadowSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_BrzaccVLNewAdbShadowSwVersion_Type.__name__=_I
_BrzaccVLNewAdbShadowSwVersion_Object=MibTableColumn
brzaccVLNewAdbShadowSwVersion=_BrzaccVLNewAdbShadowSwVersion_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,47),_BrzaccVLNewAdbShadowSwVersion_Type())
brzaccVLNewAdbShadowSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbShadowSwVersion.setStatus(_A)
class _BrzaccVLNewAdbReadOnlyCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_BrzaccVLNewAdbReadOnlyCommunity_Type.__name__=_I
_BrzaccVLNewAdbReadOnlyCommunity_Object=MibTableColumn
brzaccVLNewAdbReadOnlyCommunity=_BrzaccVLNewAdbReadOnlyCommunity_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,48),_BrzaccVLNewAdbReadOnlyCommunity_Type())
brzaccVLNewAdbReadOnlyCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbReadOnlyCommunity.setStatus(_A)
class _BrzaccVLNewAdbWriteCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_BrzaccVLNewAdbWriteCommunity_Type.__name__=_I
_BrzaccVLNewAdbWriteCommunity_Object=MibTableColumn
brzaccVLNewAdbWriteCommunity=_BrzaccVLNewAdbWriteCommunity_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,49),_BrzaccVLNewAdbWriteCommunity_Type())
brzaccVLNewAdbWriteCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbWriteCommunity.setStatus(_A)
_BrzaccVLNewAdbAIFS_Type=Integer32
_BrzaccVLNewAdbAIFS_Object=MibTableColumn
brzaccVLNewAdbAIFS=_BrzaccVLNewAdbAIFS_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,50),_BrzaccVLNewAdbAIFS_Type())
brzaccVLNewAdbAIFS.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbAIFS.setStatus(_A)
_BrzaccVLNewAdbMinimumCW_Type=Integer32
_BrzaccVLNewAdbMinimumCW_Object=MibTableColumn
brzaccVLNewAdbMinimumCW=_BrzaccVLNewAdbMinimumCW_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,51),_BrzaccVLNewAdbMinimumCW_Type())
brzaccVLNewAdbMinimumCW.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbMinimumCW.setStatus(_A)
_BrzaccVLNewAdbMaximumCW_Type=Integer32
_BrzaccVLNewAdbMaximumCW_Object=MibTableColumn
brzaccVLNewAdbMaximumCW=_BrzaccVLNewAdbMaximumCW_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,52),_BrzaccVLNewAdbMaximumCW_Type())
brzaccVLNewAdbMaximumCW.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbMaximumCW.setStatus(_A)
class _BrzaccVLNewAdbESSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_BrzaccVLNewAdbESSID_Type.__name__=_I
_BrzaccVLNewAdbESSID_Object=MibTableColumn
brzaccVLNewAdbESSID=_BrzaccVLNewAdbESSID_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,53),_BrzaccVLNewAdbESSID_Type())
brzaccVLNewAdbESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbESSID.setStatus(_A)
_BrzaccVLNewAdbRSSI_Type=Integer32
_BrzaccVLNewAdbRSSI_Object=MibTableColumn
brzaccVLNewAdbRSSI=_BrzaccVLNewAdbRSSI_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,54),_BrzaccVLNewAdbRSSI_Type())
brzaccVLNewAdbRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbRSSI.setStatus(_A)
class _BrzaccVLNewAdbDfsOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BrzaccVLNewAdbDfsOption_Type.__name__=_C
_BrzaccVLNewAdbDfsOption_Object=MibTableColumn
brzaccVLNewAdbDfsOption=_BrzaccVLNewAdbDfsOption_Object((1,3,6,1,4,1,12394,1,1,11,5,1,3,1,55),_BrzaccVLNewAdbDfsOption_Type())
brzaccVLNewAdbDfsOption.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewAdbDfsOption.setStatus(_A)
_BrzaccVLAggregateMIRCIR_ObjectIdentity=ObjectIdentity
brzaccVLAggregateMIRCIR=_BrzaccVLAggregateMIRCIR_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,5,1,4))
_BrzaccVLAggregateMIRUplink_Type=Integer32
_BrzaccVLAggregateMIRUplink_Object=MibScalar
brzaccVLAggregateMIRUplink=_BrzaccVLAggregateMIRUplink_Object((1,3,6,1,4,1,12394,1,1,11,5,1,4,1),_BrzaccVLAggregateMIRUplink_Type())
brzaccVLAggregateMIRUplink.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAggregateMIRUplink.setStatus(_A)
_BrzaccVLAggregateMIRDownlink_Type=Integer32
_BrzaccVLAggregateMIRDownlink_Object=MibScalar
brzaccVLAggregateMIRDownlink=_BrzaccVLAggregateMIRDownlink_Object((1,3,6,1,4,1,12394,1,1,11,5,1,4,2),_BrzaccVLAggregateMIRDownlink_Type())
brzaccVLAggregateMIRDownlink.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAggregateMIRDownlink.setStatus(_A)
_BrzaccVLAggregateCIRUplink_Type=Integer32
_BrzaccVLAggregateCIRUplink_Object=MibScalar
brzaccVLAggregateCIRUplink=_BrzaccVLAggregateCIRUplink_Object((1,3,6,1,4,1,12394,1,1,11,5,1,4,3),_BrzaccVLAggregateCIRUplink_Type())
brzaccVLAggregateCIRUplink.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAggregateCIRUplink.setStatus(_A)
_BrzaccVLAggregateCIRDownlink_Type=Integer32
_BrzaccVLAggregateCIRDownlink_Object=MibScalar
brzaccVLAggregateCIRDownlink=_BrzaccVLAggregateCIRDownlink_Object((1,3,6,1,4,1,12394,1,1,11,5,1,4,4),_BrzaccVLAggregateCIRDownlink_Type())
brzaccVLAggregateCIRDownlink.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAggregateCIRDownlink.setStatus(_A)
_BrzaccVLUpLinkQualityIndicator_ObjectIdentity=ObjectIdentity
brzaccVLUpLinkQualityIndicator=_BrzaccVLUpLinkQualityIndicator_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,6))
class _BrzaccVLMeasureUpLinkQualityIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),(_K,2)))
_BrzaccVLMeasureUpLinkQualityIndicator_Type.__name__=_C
_BrzaccVLMeasureUpLinkQualityIndicator_Object=MibScalar
brzaccVLMeasureUpLinkQualityIndicator=_BrzaccVLMeasureUpLinkQualityIndicator_Object((1,3,6,1,4,1,12394,1,1,11,6,1),_BrzaccVLMeasureUpLinkQualityIndicator_Type())
brzaccVLMeasureUpLinkQualityIndicator.setMaxAccess(_D)
if mibBuilder.loadTexts:brzaccVLMeasureUpLinkQualityIndicator.setStatus(_A)
_BrzaccVLReadUpLinkQualityIndicator_Type=Integer32
_BrzaccVLReadUpLinkQualityIndicator_Object=MibScalar
brzaccVLReadUpLinkQualityIndicator=_BrzaccVLReadUpLinkQualityIndicator_Object((1,3,6,1,4,1,12394,1,1,11,6,2),_BrzaccVLReadUpLinkQualityIndicator_Type())
brzaccVLReadUpLinkQualityIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLReadUpLinkQualityIndicator.setStatus(_A)
class _BrzaccVLUpLinkQualityIndicatorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fullTest',1),('limitedTest',2)))
_BrzaccVLUpLinkQualityIndicatorStatus_Type.__name__=_C
_BrzaccVLUpLinkQualityIndicatorStatus_Object=MibScalar
brzaccVLUpLinkQualityIndicatorStatus=_BrzaccVLUpLinkQualityIndicatorStatus_Object((1,3,6,1,4,1,12394,1,1,11,6,3),_BrzaccVLUpLinkQualityIndicatorStatus_Type())
brzaccVLUpLinkQualityIndicatorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLUpLinkQualityIndicatorStatus.setStatus(_A)
_BrzaccVLMacPinpoint_ObjectIdentity=ObjectIdentity
brzaccVLMacPinpoint=_BrzaccVLMacPinpoint_ObjectIdentity((1,3,6,1,4,1,12394,1,1,11,7))
_BrzaccVLMacPinpointTable_Object=MibTable
brzaccVLMacPinpointTable=_BrzaccVLMacPinpointTable_Object((1,3,6,1,4,1,12394,1,1,11,7,1))
if mibBuilder.loadTexts:brzaccVLMacPinpointTable.setStatus(_A)
_BrzaccVLMacPinpointEntry_Object=MibTableRow
brzaccVLMacPinpointEntry=_BrzaccVLMacPinpointEntry_Object((1,3,6,1,4,1,12394,1,1,11,7,1,1))
brzaccVLMacPinpointEntry.setIndexNames((0,_E,_B4))
if mibBuilder.loadTexts:brzaccVLMacPinpointEntry.setStatus(_A)
_MptEthernetStationMACAddress_Type=MacAddress
_MptEthernetStationMACAddress_Object=MibTableColumn
mptEthernetStationMACAddress=_MptEthernetStationMACAddress_Object((1,3,6,1,4,1,12394,1,1,11,7,1,1,1),_MptEthernetStationMACAddress_Type())
mptEthernetStationMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mptEthernetStationMACAddress.setStatus(_A)
_MptUnitMACAddress_Type=MacAddress
_MptUnitMACAddress_Object=MibTableColumn
mptUnitMACAddress=_MptUnitMACAddress_Object((1,3,6,1,4,1,12394,1,1,11,7,1,1,2),_MptUnitMACAddress_Type())
mptUnitMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mptUnitMACAddress.setStatus(_A)
_BrzaccVLDrapGatewaysTable_Object=MibTable
brzaccVLDrapGatewaysTable=_BrzaccVLDrapGatewaysTable_Object((1,3,6,1,4,1,12394,1,1,11,8))
if mibBuilder.loadTexts:brzaccVLDrapGatewaysTable.setStatus(_A)
_BrzaccVLDrapGatewayEntry_Object=MibTableRow
brzaccVLDrapGatewayEntry=_BrzaccVLDrapGatewayEntry_Object((1,3,6,1,4,1,12394,1,1,11,8,1))
brzaccVLDrapGatewayEntry.setIndexNames((0,_E,_B5))
if mibBuilder.loadTexts:brzaccVLDrapGatewayEntry.setStatus(_A)
class _BrzaccVLDrapGatewayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_BrzaccVLDrapGatewayIndex_Type.__name__=_C
_BrzaccVLDrapGatewayIndex_Object=MibTableColumn
brzaccVLDrapGatewayIndex=_BrzaccVLDrapGatewayIndex_Object((1,3,6,1,4,1,12394,1,1,11,8,1,1),_BrzaccVLDrapGatewayIndex_Type())
brzaccVLDrapGatewayIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDrapGatewayIndex.setStatus(_A)
_BrzaccVLDrapGatewayIP_Type=IpAddress
_BrzaccVLDrapGatewayIP_Object=MibTableColumn
brzaccVLDrapGatewayIP=_BrzaccVLDrapGatewayIP_Object((1,3,6,1,4,1,12394,1,1,11,8,1,2),_BrzaccVLDrapGatewayIP_Type())
brzaccVLDrapGatewayIP.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDrapGatewayIP.setStatus(_A)
class _BrzaccVLDrapGatewayType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6,7,11,255)));namedValues=NamedValues(*(('vgDataVoice',4),('vgData1Voice1',5),('vgData4Voice2',6),('vgDataVoice2',7),('ngData4Wireless',11),('vgUnknown',255)))
_BrzaccVLDrapGatewayType_Type.__name__=_C
_BrzaccVLDrapGatewayType_Object=MibTableColumn
brzaccVLDrapGatewayType=_BrzaccVLDrapGatewayType_Object((1,3,6,1,4,1,12394,1,1,11,8,1,3),_BrzaccVLDrapGatewayType_Type())
brzaccVLDrapGatewayType.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDrapGatewayType.setStatus(_A)
_BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Type=Integer32
_BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Object=MibTableColumn
brzaccVLDrapGatewayNoOfActiveVoiceCalls=_BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Object((1,3,6,1,4,1,12394,1,1,11,8,1,4),_BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Type())
brzaccVLDrapGatewayNoOfActiveVoiceCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDrapGatewayNoOfActiveVoiceCalls.setStatus(_A)
_BrzaccVLHiddenESSIDTable_Object=MibTable
brzaccVLHiddenESSIDTable=_BrzaccVLHiddenESSIDTable_Object((1,3,6,1,4,1,12394,1,1,11,9))
if mibBuilder.loadTexts:brzaccVLHiddenESSIDTable.setStatus(_A)
_BrzaccVLHiddenESSIDEntry_Object=MibTableRow
brzaccVLHiddenESSIDEntry=_BrzaccVLHiddenESSIDEntry_Object((1,3,6,1,4,1,12394,1,1,11,9,1))
brzaccVLHiddenESSIDEntry.setIndexNames((0,_E,_B6))
if mibBuilder.loadTexts:brzaccVLHiddenESSIDEntry.setStatus(_A)
_BrzaccVLHiddenESSIDMacAddress_Type=MacAddress
_BrzaccVLHiddenESSIDMacAddress_Object=MibTableColumn
brzaccVLHiddenESSIDMacAddress=_BrzaccVLHiddenESSIDMacAddress_Object((1,3,6,1,4,1,12394,1,1,11,9,1,1),_BrzaccVLHiddenESSIDMacAddress_Type())
brzaccVLHiddenESSIDMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLHiddenESSIDMacAddress.setStatus(_A)
_BrzaccVLHiddenESSIDAge_Type=Integer32
_BrzaccVLHiddenESSIDAge_Object=MibTableColumn
brzaccVLHiddenESSIDAge=_BrzaccVLHiddenESSIDAge_Object((1,3,6,1,4,1,12394,1,1,11,9,1,2),_BrzaccVLHiddenESSIDAge_Type())
brzaccVLHiddenESSIDAge.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLHiddenESSIDAge.setStatus(_A)
_BrzaccVLAverageReceiveRSSI_Type=Integer32
_BrzaccVLAverageReceiveRSSI_Object=MibScalar
brzaccVLAverageReceiveRSSI=_BrzaccVLAverageReceiveRSSI_Object((1,3,6,1,4,1,12394,1,1,11,10),_BrzaccVLAverageReceiveRSSI_Type())
brzaccVLAverageReceiveRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAverageReceiveRSSI.setStatus(_A)
_BrzaccVLCurrentNoiseFloor_Type=Integer32
_BrzaccVLCurrentNoiseFloor_Object=MibScalar
brzaccVLCurrentNoiseFloor=_BrzaccVLCurrentNoiseFloor_Object((1,3,6,1,4,1,12394,1,1,11,11),_BrzaccVLCurrentNoiseFloor_Type())
brzaccVLCurrentNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLCurrentNoiseFloor.setStatus(_A)
_BrzaccVLAverageSignalInterferenceRatio_Type=Integer32
_BrzaccVLAverageSignalInterferenceRatio_Object=MibScalar
brzaccVLAverageSignalInterferenceRatio=_BrzaccVLAverageSignalInterferenceRatio_Object((1,3,6,1,4,1,12394,1,1,11,12),_BrzaccVLAverageSignalInterferenceRatio_Type())
brzaccVLAverageSignalInterferenceRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLAverageSignalInterferenceRatio.setStatus(_A)
_BrzaccVLTraps_ObjectIdentity=ObjectIdentity
brzaccVLTraps=_BrzaccVLTraps_ObjectIdentity((1,3,6,1,4,1,12394,1,1,14))
_BrzaccVLTrapSUMacAddr_Type=MacAddress
_BrzaccVLTrapSUMacAddr_Object=MibScalar
brzaccVLTrapSUMacAddr=_BrzaccVLTrapSUMacAddr_Object((1,3,6,1,4,1,12394,1,1,14,1),_BrzaccVLTrapSUMacAddr_Type())
brzaccVLTrapSUMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapSUMacAddr.setStatus(_A)
_BrzaccVLTrapText_Type=DisplayString
_BrzaccVLTrapText_Object=MibScalar
brzaccVLTrapText=_BrzaccVLTrapText_Object((1,3,6,1,4,1,12394,1,1,14,3),_BrzaccVLTrapText_Type())
brzaccVLTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapText.setStatus(_A)
class _BrzaccVLTrapToggle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_v,2)))
_BrzaccVLTrapToggle_Type.__name__=_C
_BrzaccVLTrapToggle_Object=MibScalar
brzaccVLTrapToggle=_BrzaccVLTrapToggle_Object((1,3,6,1,4,1,12394,1,1,14,4),_BrzaccVLTrapToggle_Type())
brzaccVLTrapToggle.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapToggle.setStatus(_A)
class _BrzaccVLTrapParameterChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('cirOrMir',1),('ipFilter',2),('vlan',4)))
_BrzaccVLTrapParameterChanged_Type.__name__=_C
_BrzaccVLTrapParameterChanged_Object=MibScalar
brzaccVLTrapParameterChanged=_BrzaccVLTrapParameterChanged_Object((1,3,6,1,4,1,12394,1,1,14,5),_BrzaccVLTrapParameterChanged_Type())
brzaccVLTrapParameterChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapParameterChanged.setStatus(_A)
class _BrzaccVLTrapAccessRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notLoggedIn',1),('readOnly',2),('installer',3),('administrator',4),('factory',5)))
_BrzaccVLTrapAccessRights_Type.__name__=_C
_BrzaccVLTrapAccessRights_Object=MibScalar
brzaccVLTrapAccessRights=_BrzaccVLTrapAccessRights_Object((1,3,6,1,4,1,12394,1,1,14,6),_BrzaccVLTrapAccessRights_Type())
brzaccVLTrapAccessRights.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapAccessRights.setStatus(_A)
class _BrzaccVLTrapLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('telnetLogin',3),('telnetLogout',4)))
_BrzaccVLTrapLog_Type.__name__=_C
_BrzaccVLTrapLog_Object=MibScalar
brzaccVLTrapLog=_BrzaccVLTrapLog_Object((1,3,6,1,4,1,12394,1,1,14,7),_BrzaccVLTrapLog_Type())
brzaccVLTrapLog.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapLog.setStatus(_A)
_BrzaccVLTrapTelnetUserIpAddress_Type=IpAddress
_BrzaccVLTrapTelnetUserIpAddress_Object=MibScalar
brzaccVLTrapTelnetUserIpAddress=_BrzaccVLTrapTelnetUserIpAddress_Object((1,3,6,1,4,1,12394,1,1,14,8),_BrzaccVLTrapTelnetUserIpAddress_Type())
brzaccVLTrapTelnetUserIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapTelnetUserIpAddress.setStatus(_A)
_BrzaccVLTrapRTx_Type=Integer32
_BrzaccVLTrapRTx_Object=MibScalar
brzaccVLTrapRTx=_BrzaccVLTrapRTx_Object((1,3,6,1,4,1,12394,1,1,14,9),_BrzaccVLTrapRTx_Type())
brzaccVLTrapRTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapRTx.setStatus(_A)
class _BrzaccVLTrapFtpOrTftpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A9,1),(_u,2)))
_BrzaccVLTrapFtpOrTftpStatus_Type.__name__=_C
_BrzaccVLTrapFtpOrTftpStatus_Object=MibScalar
brzaccVLTrapFtpOrTftpStatus=_BrzaccVLTrapFtpOrTftpStatus_Object((1,3,6,1,4,1,12394,1,1,14,10),_BrzaccVLTrapFtpOrTftpStatus_Type())
brzaccVLTrapFtpOrTftpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapFtpOrTftpStatus.setStatus(_A)
_BrzaccVLDFSMoveFreq_Type=Integer32
_BrzaccVLDFSMoveFreq_Object=MibScalar
brzaccVLDFSMoveFreq=_BrzaccVLDFSMoveFreq_Object((1,3,6,1,4,1,12394,1,1,14,11),_BrzaccVLDFSMoveFreq_Type())
brzaccVLDFSMoveFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDFSMoveFreq.setStatus(_A)
_BrzaccVLDFSMoveFreqNew_Type=DisplayString
_BrzaccVLDFSMoveFreqNew_Object=MibScalar
brzaccVLDFSMoveFreqNew=_BrzaccVLDFSMoveFreqNew_Object((1,3,6,1,4,1,12394,1,1,14,12),_BrzaccVLDFSMoveFreqNew_Type())
brzaccVLDFSMoveFreqNew.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLDFSMoveFreqNew.setStatus(_A)
_BrzaccVLEthBroadcastThresholdExceeded_Type=Integer32
_BrzaccVLEthBroadcastThresholdExceeded_Object=MibScalar
brzaccVLEthBroadcastThresholdExceeded=_BrzaccVLEthBroadcastThresholdExceeded_Object((1,3,6,1,4,1,12394,1,1,14,13),_BrzaccVLEthBroadcastThresholdExceeded_Type())
brzaccVLEthBroadcastThresholdExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLEthBroadcastThresholdExceeded.setStatus(_A)
class _BrzaccVLTrapSubscriberType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,6,8,14,24,28,54,100)));namedValues=NamedValues(*(('unknownSubscriberType',0),('su-3',3),('su-6',6),('su-8',8),('rb-14',14),('su-24',24),('rb-28',28),('su-54',54),('rb-100',100)))
_BrzaccVLTrapSubscriberType_Type.__name__=_C
_BrzaccVLTrapSubscriberType_Object=MibScalar
brzaccVLTrapSubscriberType=_BrzaccVLTrapSubscriberType_Object((1,3,6,1,4,1,12394,1,1,14,14),_BrzaccVLTrapSubscriberType_Type())
brzaccVLTrapSubscriberType.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapSubscriberType.setStatus(_A)
_BrzaccVLTrapMACAddress_Type=MacAddress
_BrzaccVLTrapMACAddress_Object=MibScalar
brzaccVLTrapMACAddress=_BrzaccVLTrapMACAddress_Object((1,3,6,1,4,1,12394,1,1,14,15),_BrzaccVLTrapMACAddress_Type())
brzaccVLTrapMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapMACAddress.setStatus(_A)
class _BrzaccVLNewUnitTypeTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bu',1),('rb',2)))
_BrzaccVLNewUnitTypeTrap_Type.__name__=_C
_BrzaccVLNewUnitTypeTrap_Object=MibScalar
brzaccVLNewUnitTypeTrap=_BrzaccVLNewUnitTypeTrap_Object((1,3,6,1,4,1,12394,1,1,14,16),_BrzaccVLNewUnitTypeTrap_Type())
brzaccVLNewUnitTypeTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLNewUnitTypeTrap.setStatus(_A)
_BrzaccVLTrapSWVersion_Type=DisplayString
_BrzaccVLTrapSWVersion_Object=MibScalar
brzaccVLTrapSWVersion=_BrzaccVLTrapSWVersion_Object((1,3,6,1,4,1,12394,1,1,14,17),_BrzaccVLTrapSWVersion_Type())
brzaccVLTrapSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapSWVersion.setStatus(_A)
_BrzaccVLTrapSequenceNumber_Type=Integer32
_BrzaccVLTrapSequenceNumber_Object=MibScalar
brzaccVLTrapSequenceNumber=_BrzaccVLTrapSequenceNumber_Object((1,3,6,1,4,1,12394,1,1,14,18),_BrzaccVLTrapSequenceNumber_Type())
brzaccVLTrapSequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapSequenceNumber.setStatus(_A)
_BrzaccVLTrapUnitMacAddr_Type=MacAddress
_BrzaccVLTrapUnitMacAddr_Object=MibScalar
brzaccVLTrapUnitMacAddr=_BrzaccVLTrapUnitMacAddr_Object((1,3,6,1,4,1,12394,1,1,14,19),_BrzaccVLTrapUnitMacAddr_Type())
brzaccVLTrapUnitMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapUnitMacAddr.setStatus(_A)
_BrzaccVLTrapParameterGroupCode_Type=Integer32
_BrzaccVLTrapParameterGroupCode_Object=MibScalar
brzaccVLTrapParameterGroupCode=_BrzaccVLTrapParameterGroupCode_Object((1,3,6,1,4,1,12394,1,1,14,20),_BrzaccVLTrapParameterGroupCode_Type())
brzaccVLTrapParameterGroupCode.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapParameterGroupCode.setStatus(_A)
_BrzaccVLTrapNewIP_Type=IpAddress
_BrzaccVLTrapNewIP_Object=MibScalar
brzaccVLTrapNewIP=_BrzaccVLTrapNewIP_Object((1,3,6,1,4,1,12394,1,1,14,21),_BrzaccVLTrapNewIP_Type())
brzaccVLTrapNewIP.setMaxAccess(_B)
if mibBuilder.loadTexts:brzaccVLTrapNewIP.setStatus(_A)
_AlvarionOID_ObjectIdentity=ObjectIdentity
alvarionOID=_AlvarionOID_ObjectIdentity((1,3,6,1,4,1,12394,4))
_BrzAccessVLOID_ObjectIdentity=ObjectIdentity
brzAccessVLOID=_BrzAccessVLOID_ObjectIdentity((1,3,6,1,4,1,12394,4,1))
_BrzAccessVLAU_ObjectIdentity=ObjectIdentity
brzAccessVLAU=_BrzAccessVLAU_ObjectIdentity((1,3,6,1,4,1,12394,4,1,1))
_BrzAccessVLSU_ObjectIdentity=ObjectIdentity
brzAccessVLSU=_BrzAccessVLSU_ObjectIdentity((1,3,6,1,4,1,12394,4,1,2))
_BrzAccessVLProducts_ObjectIdentity=ObjectIdentity
brzAccessVLProducts=_BrzAccessVLProducts_ObjectIdentity((1,3,6,1,4,1,12394,4,1,3))
_BrzAccessVLAU_BS_ObjectIdentity=ObjectIdentity
brzAccessVLAU_BS=_BrzAccessVLAU_BS_ObjectIdentity((1,3,6,1,4,1,12394,4,1,4))
_BrzAccessVLAU_SA_ObjectIdentity=ObjectIdentity
brzAccessVLAU_SA=_BrzAccessVLAU_SA_ObjectIdentity((1,3,6,1,4,1,12394,4,1,5))
_BrzAccessVLAUS_BS_ObjectIdentity=ObjectIdentity
brzAccessVLAUS_BS=_BrzAccessVLAUS_BS_ObjectIdentity((1,3,6,1,4,1,12394,4,1,6))
_BrzAccessVLAUS_SA_ObjectIdentity=ObjectIdentity
brzAccessVLAUS_SA=_BrzAccessVLAUS_SA_ObjectIdentity((1,3,6,1,4,1,12394,4,1,7))
_BrzAccessAU_EZ_ObjectIdentity=ObjectIdentity
brzAccessAU_EZ=_BrzAccessAU_EZ_ObjectIdentity((1,3,6,1,4,1,12394,4,1,8))
_BrzAccessVLSU_6_1D_ObjectIdentity=ObjectIdentity
brzAccessVLSU_6_1D=_BrzAccessVLSU_6_1D_ObjectIdentity((1,3,6,1,4,1,12394,4,1,11))
_BrzAccessVLSU_6_BD_ObjectIdentity=ObjectIdentity
brzAccessVLSU_6_BD=_BrzAccessVLSU_6_BD_ObjectIdentity((1,3,6,1,4,1,12394,4,1,12))
_BrzAccessVLSU_24_BD_ObjectIdentity=ObjectIdentity
brzAccessVLSU_24_BD=_BrzAccessVLSU_24_BD_ObjectIdentity((1,3,6,1,4,1,12394,4,1,13))
_BrzAccessVLSU_BD_ObjectIdentity=ObjectIdentity
brzAccessVLSU_BD=_BrzAccessVLSU_BD_ObjectIdentity((1,3,6,1,4,1,12394,4,1,14))
_BrzAccessVLSU_54_BD_ObjectIdentity=ObjectIdentity
brzAccessVLSU_54_BD=_BrzAccessVLSU_54_BD_ObjectIdentity((1,3,6,1,4,1,12394,4,1,15))
_BrzAccessVLSU_3_1D_ObjectIdentity=ObjectIdentity
brzAccessVLSU_3_1D=_BrzAccessVLSU_3_1D_ObjectIdentity((1,3,6,1,4,1,12394,4,1,16))
_BrzAccessVLSU_3_4D_ObjectIdentity=ObjectIdentity
brzAccessVLSU_3_4D=_BrzAccessVLSU_3_4D_ObjectIdentity((1,3,6,1,4,1,12394,4,1,17))
_BrzAccessVLSU_I_ObjectIdentity=ObjectIdentity
brzAccessVLSU_I=_BrzAccessVLSU_I_ObjectIdentity((1,3,6,1,4,1,12394,4,1,18))
_BrzAccessVLSU_EZ_ObjectIdentity=ObjectIdentity
brzAccessVLSU_EZ=_BrzAccessVLSU_EZ_ObjectIdentity((1,3,6,1,4,1,12394,4,1,19))
_BrzAccessVLSU_V_ObjectIdentity=ObjectIdentity
brzAccessVLSU_V=_BrzAccessVLSU_V_ObjectIdentity((1,3,6,1,4,1,12394,4,1,20))
_BrzNetB_BU_B14_ObjectIdentity=ObjectIdentity
brzNetB_BU_B14=_BrzNetB_BU_B14_ObjectIdentity((1,3,6,1,4,1,12394,4,1,21))
_BrzNetB_BU_B28_ObjectIdentity=ObjectIdentity
brzNetB_BU_B28=_BrzNetB_BU_B28_ObjectIdentity((1,3,6,1,4,1,12394,4,1,22))
_BrzNetB_BU_B100_ObjectIdentity=ObjectIdentity
brzNetB_BU_B100=_BrzNetB_BU_B100_ObjectIdentity((1,3,6,1,4,1,12394,4,1,23))
_BrzNetB_BU_B10_ObjectIdentity=ObjectIdentity
brzNetB_BU_B10=_BrzNetB_BU_B10_ObjectIdentity((1,3,6,1,4,1,12394,4,1,24))
_BrzNetB_RB_B14_ObjectIdentity=ObjectIdentity
brzNetB_RB_B14=_BrzNetB_RB_B14_ObjectIdentity((1,3,6,1,4,1,12394,4,1,31))
_BrzNetB_RB_B28_ObjectIdentity=ObjectIdentity
brzNetB_RB_B28=_BrzNetB_RB_B28_ObjectIdentity((1,3,6,1,4,1,12394,4,1,32))
_BrzNetB_RB_B100_ObjectIdentity=ObjectIdentity
brzNetB_RB_B100=_BrzNetB_RB_B100_ObjectIdentity((1,3,6,1,4,1,12394,4,1,33))
_BrzNetB_RB_B10_ObjectIdentity=ObjectIdentity
brzNetB_RB_B10=_BrzNetB_RB_B10_ObjectIdentity((1,3,6,1,4,1,12394,4,1,34))
_BrzAccess4900_AU_BS_ObjectIdentity=ObjectIdentity
brzAccess4900_AU_BS=_BrzAccess4900_AU_BS_ObjectIdentity((1,3,6,1,4,1,12394,4,1,41))
_BrzAccess4900_AU_SA_ObjectIdentity=ObjectIdentity
brzAccess4900_AU_SA=_BrzAccess4900_AU_SA_ObjectIdentity((1,3,6,1,4,1,12394,4,1,42))
_BrzAccess4900_SU_BD_ObjectIdentity=ObjectIdentity
brzAccess4900_SU_BD=_BrzAccess4900_SU_BD_ObjectIdentity((1,3,6,1,4,1,12394,4,1,51))
_BrzAccessVLSU_8_BD_ObjectIdentity=ObjectIdentity
brzAccessVLSU_8_BD=_BrzAccessVLSU_8_BD_ObjectIdentity((1,3,6,1,4,1,12394,4,1,61))
_BrzAccessVLSU_1_BD_ObjectIdentity=ObjectIdentity
brzAccessVLSU_1_BD=_BrzAccessVLSU_1_BD_ObjectIdentity((1,3,6,1,4,1,12394,4,1,62))
_BrzAccessVLSU_3_L_ObjectIdentity=ObjectIdentity
brzAccessVLSU_3_L=_BrzAccessVLSU_3_L_ObjectIdentity((1,3,6,1,4,1,12394,4,1,63))
_BrzAccessVLSU_6_L_ObjectIdentity=ObjectIdentity
brzAccessVLSU_6_L=_BrzAccessVLSU_6_L_ObjectIdentity((1,3,6,1,4,1,12394,4,1,64))
_BrzAccessVLSU_12_L_ObjectIdentity=ObjectIdentity
brzAccessVLSU_12_L=_BrzAccessVLSU_12_L_ObjectIdentity((1,3,6,1,4,1,12394,4,1,65))
_BrzAccessVL_AU_ObjectIdentity=ObjectIdentity
brzAccessVL_AU=_BrzAccessVL_AU_ObjectIdentity((1,3,6,1,4,1,12394,4,1,70))
_BrzAccessVL_SU_ObjectIdentity=ObjectIdentity
brzAccessVL_SU=_BrzAccessVL_SU_ObjectIdentity((1,3,6,1,4,1,12394,4,1,75))
brzaccVLSUassociatedAUTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,2))
brzaccVLSUassociatedAUTRAP.setObjects(*((_E,_d),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLSUassociatedAUTRAP.setStatus(_A)
brzaccVLAUdisassociatedTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,3))
brzaccVLAUdisassociatedTRAP.setObjects(*((_E,_d),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLAUdisassociatedTRAP.setStatus(_A)
brzaccVLAUagingTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,4))
brzaccVLAUagingTRAP.setObjects(*((_E,_d),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLAUagingTRAP.setStatus(_A)
brzaccVLSUassociatedTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,6))
brzaccVLSUassociatedTRAP.setObjects((_E,_B7))
if mibBuilder.loadTexts:brzaccVLSUassociatedTRAP.setStatus(_A)
brzaccVLAUwirelessQualityTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,20))
brzaccVLAUwirelessQualityTRAP.setObjects(*((_E,_A7),(_E,_e),(_E,_B8),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLAUwirelessQualityTRAP.setStatus(_A)
brzaccVLPowerUpFromReset=NotificationType((1,3,6,1,4,1,12394,4,1,3,101))
brzaccVLPowerUpFromReset.setObjects(*((_E,_s),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLPowerUpFromReset.setStatus(_A)
brzaccVLTelnetStatusTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,102))
brzaccVLTelnetStatusTRAP.setObjects(*((_E,_B9),(_E,_BA),(_E,_BB),(_E,_e),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLTelnetStatusTRAP.setStatus(_A)
brzaccVLParameterChangedTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,103))
brzaccVLParameterChangedTRAP.setObjects(*((_E,_BC),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLParameterChangedTRAP.setStatus(_A)
brzaccVLLoadingStatusTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,104))
brzaccVLLoadingStatusTRAP.setObjects(*((_E,_BD),(_E,_s),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLLoadingStatusTRAP.setStatus(_A)
brzaccVLPromiscuousModeTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,105))
brzaccVLPromiscuousModeTRAP.setObjects(*((_E,_A7),(_E,_s),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLPromiscuousModeTRAP.setStatus(_A)
brzaccVLDFSRadarDetectedTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,106))
brzaccVLDFSRadarDetectedTRAP.setObjects((_E,_J))
if mibBuilder.loadTexts:brzaccVLDFSRadarDetectedTRAP.setStatus(_A)
brzaccVLDFSFrequencyTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,107))
brzaccVLDFSFrequencyTRAP.setObjects(*((_E,_BE),(_E,_BF),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLDFSFrequencyTRAP.setStatus(_A)
brzaccVLDFSNoFreeChannelsExistsTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,108))
brzaccVLDFSNoFreeChannelsExistsTRAP.setObjects((_E,_J))
if mibBuilder.loadTexts:brzaccVLDFSNoFreeChannelsExistsTRAP.setStatus(_A)
brzaccVLEthBroadcastMulticastLimiterTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,109))
brzaccVLEthBroadcastMulticastLimiterTRAP.setObjects(*((_E,_BG),(_E,_e),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLEthBroadcastMulticastLimiterTRAP.setStatus(_A)
brzaccVLAUSUnsupportedSubscriberTypeTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,110))
brzaccVLAUSUnsupportedSubscriberTypeTRAP.setObjects(*((_E,_d),(_E,_BH),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLAUSUnsupportedSubscriberTypeTRAP.setStatus(_A)
brzaccVLUnitTypeChangedTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,111))
brzaccVLUnitTypeChangedTRAP.setObjects(*((_E,_BI),(_E,_BJ),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLUnitTypeChangedTRAP.setStatus(_A)
brzaccVLWLPrioritizationNotSupportedBySUTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,112))
brzaccVLWLPrioritizationNotSupportedBySUTRAP.setObjects(*((_E,_d),(_E,_BK),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLWLPrioritizationNotSupportedBySUTRAP.setStatus(_A)
brzaccVLParameterChangeTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,113))
brzaccVLParameterChangeTRAP.setObjects(*((_E,_e),(_E,_BL),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLParameterChangeTRAP.setStatus(_A)
brzaccVLRunTimeIPChangeTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,114))
brzaccVLRunTimeIPChangeTRAP.setObjects(*((_E,_e),(_E,_BM),(_E,_J)))
if mibBuilder.loadTexts:brzaccVLRunTimeIPChangeTRAP.setStatus(_A)
brzaccVLDisassociateAllStationsTRAP=NotificationType((1,3,6,1,4,1,12394,4,1,3,115))
brzaccVLDisassociateAllStationsTRAP.setObjects((_E,_J))
if mibBuilder.loadTexts:brzaccVLDisassociateAllStationsTRAP.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,_I:DisplayString,'alvarion':alvarion,'products':products,'breezeAccessVLMib':breezeAccessVLMib,'brzaccVLSysInfo':brzaccVLSysInfo,'brzaccVLUnitHwVersion':brzaccVLUnitHwVersion,'brzaccVLRunningSoftwareVersion':brzaccVLRunningSoftwareVersion,'brzaccVLRunningFrom':brzaccVLRunningFrom,'brzaccVLMainVersionNumber':brzaccVLMainVersionNumber,'brzaccVLMainVersionFileName':brzaccVLMainVersionFileName,'brzaccVLShadowVersionNumber':brzaccVLShadowVersionNumber,'brzaccVLShadowVersionFileName':brzaccVLShadowVersionFileName,_s:brzaccVLUnitMacAddress,'brzaccVLUnitType':brzaccVLUnitType,_B7:brzaccVLAssociatedAU,'brzaccVLNumOfAssociationsSinceLastReset':brzaccVLNumOfAssociationsSinceLastReset,'brzaccVLCurrentNumOfAssociations':brzaccVLCurrentNumOfAssociations,'brzaccVLUnitBootVersion':brzaccVLUnitBootVersion,'brzaccVLRadioBand':brzaccVLRadioBand,'brzaccVLCurrentEthernetPortState':brzaccVLCurrentEthernetPortState,'brzaccVLTimeSinceLastReset':brzaccVLTimeSinceLastReset,'brzaccVLCountryDependentParameters':brzaccVLCountryDependentParameters,'brzaccVLCountryCode':brzaccVLCountryCode,'brzaccVLCountryDependentParamsTable':brzaccVLCountryDependentParamsTable,'brzaccVLCountryDependentParameterEntry':brzaccVLCountryDependentParameterEntry,_A8:brzaccVLCountryDependentParameterTableIdx,'brzaccVLCountryDependentParameterFrequencies':brzaccVLCountryDependentParameterFrequencies,'brzaccVLAllowedBandwidth':brzaccVLAllowedBandwidth,'brzaccVLRegulationMaxTxPowerAtAntennaPort':brzaccVLRegulationMaxTxPowerAtAntennaPort,'brzaccVLRegulationMaxEIRP':brzaccVLRegulationMaxEIRP,'brzaccVLMinModulationLevel':brzaccVLMinModulationLevel,'brzaccVLMaxModulationLevel':brzaccVLMaxModulationLevel,'brzaccVLBurstModeSupport':brzaccVLBurstModeSupport,'brzaccVLMaximumBurstDuration':brzaccVLMaximumBurstDuration,'brzaccVLDfsSupport':brzaccVLDfsSupport,'brzaccVLMinimumHwRevision':brzaccVLMinimumHwRevision,'brzaccVLAuthenticationEncryptionSupport':brzaccVLAuthenticationEncryptionSupport,'brzaccVLDataEncryptionSupport':brzaccVLDataEncryptionSupport,'brzaccVLAESEncryptionSupport':brzaccVLAESEncryptionSupport,'brzaccVLAntennaGainChange':brzaccVLAntennaGainChange,'brzaccVLAteTestResults':brzaccVLAteTestResults,'brzaccVLSerialNumber':brzaccVLSerialNumber,'brzaccVLAUSSupportSU54':brzaccVLAUSSupportSU54,'brzaccVLNumOfRejectionsSinceLastReset':brzaccVLNumOfRejectionsSinceLastReset,'brzaccVLAUSSupportSU8':brzaccVLAUSSupportSU8,'brzaccVLUnitControl':brzaccVLUnitControl,'brzaccVLResetUnit':brzaccVLResetUnit,'brzaccVLSetDefaults':brzaccVLSetDefaults,'brzaccVLUnitName':brzaccVLUnitName,'brzaccVLFlashMemoryControl':brzaccVLFlashMemoryControl,'brzaccVLTelnetLogoutTimer':brzaccVLTelnetLogoutTimer,'brzaccVLSaveCurrentConfigurationAsOperatorDefaults':brzaccVLSaveCurrentConfigurationAsOperatorDefaults,'brzaccVLExitTelnet':brzaccVLExitTelnet,'brzaccVLUnitPasswords':brzaccVLUnitPasswords,'brzaccVLReadOnlyPassword':brzaccVLReadOnlyPassword,'brzaccVLInstallerPassword':brzaccVLInstallerPassword,'brzaccVLAdminPassword':brzaccVLAdminPassword,'brzaccVLEthernetNegotiationMode':brzaccVLEthernetNegotiationMode,'brzaccVLFTPParameters':brzaccVLFTPParameters,'brzaccVLFTPServerParams':brzaccVLFTPServerParams,'brzaccVLFTPServerUserName':brzaccVLFTPServerUserName,'brzaccVLFTPServerPassword':brzaccVLFTPServerPassword,'brzaccVLFTPClientIPAddress':brzaccVLFTPClientIPAddress,'brzaccVLFTPServerIpAddress':brzaccVLFTPServerIpAddress,'brzaccVLFTPClientMask':brzaccVLFTPClientMask,'brzaccVLFTPGatewayIpAddress':brzaccVLFTPGatewayIpAddress,'brzaccVLFTPSwDownload':brzaccVLFTPSwDownload,'brzaccVLFTPSwFileName':brzaccVLFTPSwFileName,'brzaccVLFTPSwSourceDir':brzaccVLFTPSwSourceDir,'brzaccVLFTPDownloadSwFile':brzaccVLFTPDownloadSwFile,'brzaccVLConfigurationFileLoading':brzaccVLConfigurationFileLoading,'brzaccVLConfigurationFileName':brzaccVLConfigurationFileName,'brzaccVLOperatorDefaultsFileName':brzaccVLOperatorDefaultsFileName,'brzaccVLFTPConfigurationFileSourceDir':brzaccVLFTPConfigurationFileSourceDir,'brzaccVLExecuteFTPConfigurationFileLoading':brzaccVLExecuteFTPConfigurationFileLoading,'brzaccVLEventLogFileUploading':brzaccVLEventLogFileUploading,'brzaccVLEventLogFileName':brzaccVLEventLogFileName,'brzaccVLEventLogDestinationDir':brzaccVLEventLogDestinationDir,'brzaccVLUploadEventLogFile':brzaccVLUploadEventLogFile,'brzaccVLLoadingStatus':brzaccVLLoadingStatus,'brzaccVLEventLogFileParams':brzaccVLEventLogFileParams,'brzaccVLEventLogPolicy':brzaccVLEventLogPolicy,'brzaccVLEraseEventLog':brzaccVLEraseEventLog,'brzaccVLSystemLocation':brzaccVLSystemLocation,'brzaccVLFeatureUpgrade':brzaccVLFeatureUpgrade,'brzaccVLFeatureUpgradeManually':brzaccVLFeatureUpgradeManually,'brzaccVLChangeUnitType':brzaccVLChangeUnitType,'brzaccVLApWorkingMode':brzaccVLApWorkingMode,'brzaccVLLEDsettings':brzaccVLLEDsettings,'brzaccVLLEDmode':brzaccVLLEDmode,'brzaccVLThresholdTable':brzaccVLThresholdTable,'brzaccVLThresholdTableEntry':brzaccVLThresholdTableEntry,_AA:brzaccVLThresholdLEDnum,'brzaccVLThresholdLEDtype':brzaccVLThresholdLEDtype,'brzaccVLThresholdLEDmode':brzaccVLThresholdLEDmode,'brzaccVLThresholdLEDtarget':brzaccVLThresholdLEDtarget,'brzaccVLNwMngParameters':brzaccVLNwMngParameters,'brzaccVLAccessToNwMng':brzaccVLAccessToNwMng,'brzaccVLNwMngFilter':brzaccVLNwMngFilter,'mngIpFilterTable':mngIpFilterTable,'mngIpFilterEntry':mngIpFilterEntry,'brzaccVLNwMngIpAddress':brzaccVLNwMngIpAddress,_AE:brzaccVLNwMngIpTableIdx,'brzaccVLDeleteOneNwIpAddr':brzaccVLDeleteOneNwIpAddr,'brzaccVLDeleteAllNwIpAddrs':brzaccVLDeleteAllNwIpAddrs,'brzaccVLAccessToNwTrap':brzaccVLAccessToNwTrap,'mngTrapTable':mngTrapTable,'mngTrapEntry':mngTrapEntry,'brzaccVLNwMngTrapCommunity':brzaccVLNwMngTrapCommunity,'brzaccVLNwMngTrapAddress':brzaccVLNwMngTrapAddress,_AF:brzaccVLNwTrapTableIdx,'brzaccVLDeleteOneTrapAddr':brzaccVLDeleteOneTrapAddr,'brzaccVLDeleteAllTrapAddrs':brzaccVLDeleteAllTrapAddrs,'brzaccVLMngIpRangesTable':brzaccVLMngIpRangesTable,'brzaccVLMngIpRangeEntry':brzaccVLMngIpRangeEntry,_AG:brzaccVLMngIpRangeIdx,'brzaccVLMngIpRangeFlag':brzaccVLMngIpRangeFlag,'brzaccVLMngIpRangeStart':brzaccVLMngIpRangeStart,'brzaccVLMngIpRangeEnd':brzaccVLMngIpRangeEnd,'brzaccVLMngIpRangeMask':brzaccVLMngIpRangeMask,'brzaccVLDeleteOneNwIpRange':brzaccVLDeleteOneNwIpRange,'brzaccVLDeleteAllNwIpRanges':brzaccVLDeleteAllNwIpRanges,'brzaccVLWi2IpAddress':brzaccVLWi2IpAddress,'brzaccVLNewNMngSystem':brzaccVLNewNMngSystem,'brzaccVLErrorHandling':brzaccVLErrorHandling,'brzaccVLErrHandlingSetNMSId':brzaccVLErrHandlingSetNMSId,'brzaccVLErrHandlingTable':brzaccVLErrHandlingTable,'brzaccVLErrHandlingEntry':brzaccVLErrHandlingEntry,_AJ:brzaccVLErrHandlingNMSId,_AK:brzaccVLErrHandlingRequestId,'brzaccVLErrHandlingErrorCode':brzaccVLErrHandlingErrorCode,'brzaccVLErrHandlingParameter1':brzaccVLErrHandlingParameter1,'brzaccVLErrHandlingParameter2':brzaccVLErrHandlingParameter2,'brzaccVLErrHandlingParameter3':brzaccVLErrHandlingParameter3,'brzaccVLErrHandlingParameter4':brzaccVLErrHandlingParameter4,'brzaccVLErrHandlingParameter5':brzaccVLErrHandlingParameter5,'brzaccVLTrapHistory':brzaccVLTrapHistory,'brzaccVLLastTrapSequenceNumber':brzaccVLLastTrapSequenceNumber,'brzaccVLTrapHistoryTable':brzaccVLTrapHistoryTable,'brzaccVLTrapHistoryEntry':brzaccVLTrapHistoryEntry,_AL:brzaccVLTrapHistorySequenceNumber,'brzaccVLTrapType':brzaccVLTrapType,'brzaccVLTrapMacAddrParam':brzaccVLTrapMacAddrParam,'brzaccVLTrapIntParam1':brzaccVLTrapIntParam1,'brzaccVLTrapIntParam2':brzaccVLTrapIntParam2,'brzaccVLTrapIntParam3':brzaccVLTrapIntParam3,'brzaccVLTrapStrParam':brzaccVLTrapStrParam,'newMngIpFilterTable':newMngIpFilterTable,'newMngIpFilterEntry':newMngIpFilterEntry,_AM:brzaccVLNewNwMngIpAddress,'brzaccVLNewNwMngIpAddressCommand':brzaccVLNewNwMngIpAddressCommand,'newMngTrapTable':newMngTrapTable,'newMngTrapEntry':newMngTrapEntry,'brzaccVLNewNwMngTrapCommunity':brzaccVLNewNwMngTrapCommunity,_AN:brzaccVLNewNwMngTrapAddress,'brzaccVLNewNwTrapCommand':brzaccVLNewNwTrapCommand,'brzaccVLNewMngIpRangesTable':brzaccVLNewMngIpRangesTable,'brzaccVLNewMngIpRangeEntry':brzaccVLNewMngIpRangeEntry,_AO:brzaccVLNewMngIpRangeStart,'brzaccVLNewMngIpRangeEnd':brzaccVLNewMngIpRangeEnd,'brzaccVLNewMngIpRangeMask':brzaccVLNewMngIpRangeMask,'brzaccVLNewMngIpRangeFlag':brzaccVLNewMngIpRangeFlag,'brzaccVLNewMngIpRangeCommand':brzaccVLNewMngIpRangeCommand,'brzaccVLIpParams':brzaccVLIpParams,'brzaccVLUnitIpAddress':brzaccVLUnitIpAddress,'brzaccVLSubNetMask':brzaccVLSubNetMask,'brzaccVLDefaultGWAddress':brzaccVLDefaultGWAddress,'brzaccVLUseDhcp':brzaccVLUseDhcp,'brzaccVLAccessToDHCP':brzaccVLAccessToDHCP,'brzaccVLRunTimeIPaddr':brzaccVLRunTimeIPaddr,'brzaccVLRunTimeSubNetMask':brzaccVLRunTimeSubNetMask,'brzaccVLRunTimeDefaultIPGateway':brzaccVLRunTimeDefaultIPGateway,'brzaccVLBridgeParameters':brzaccVLBridgeParameters,'brzaccVLVLANSupport':brzaccVLVLANSupport,'brzaccVLVlanID':brzaccVLVlanID,'brzaccVLEthernetLinkType':brzaccVLEthernetLinkType,'brzaccVLManagementVlanID':brzaccVLManagementVlanID,'brzaccVLVLANForwarding':brzaccVLVLANForwarding,'brzaccVLVlanForwardingSupport':brzaccVLVlanForwardingSupport,'brzaccVLVlanForwardingTable':brzaccVLVlanForwardingTable,'brzaccVLVlanForwardingEntry':brzaccVLVlanForwardingEntry,_AP:brzaccVLVlanForwardingTableIdx,'brzaccVLVlanIdForwarding':brzaccVLVlanIdForwarding,'brzaccVLNewVlanForwardingTable':brzaccVLNewVlanForwardingTable,'brzaccVLNewVlanForwardingEntry':brzaccVLNewVlanForwardingEntry,_AQ:brzaccVLNewVlanIdForwarding,'brzaccVLNewVlanForwardingCommand':brzaccVLNewVlanForwardingCommand,'brzaccVLVlanRelaying':brzaccVLVlanRelaying,'brzaccVLVlanRelayingSupport':brzaccVLVlanRelayingSupport,'brzaccVLVlanRelayingTable':brzaccVLVlanRelayingTable,'brzaccVLVlanRelayingEntry':brzaccVLVlanRelayingEntry,_AR:brzaccVLVlanRelayingTableIdx,'brzaccVLVlanIdRelaying':brzaccVLVlanIdRelaying,'brzaccVLNewVlanRelayingTable':brzaccVLNewVlanRelayingTable,'brzaccVLNewVlanRelayingEntry':brzaccVLNewVlanRelayingEntry,_AS:brzaccVLNewVlanIdRelaying,'brzaccVLNewVlanRelayingTableCommand':brzaccVLNewVlanRelayingTableCommand,'brzaccVLVLANTrafficPriority':brzaccVLVLANTrafficPriority,'brzaccVLVlanDataPriority':brzaccVLVlanDataPriority,'brzaccVLVlanManagementPriority':brzaccVLVlanManagementPriority,'brzaccVLVlanPriorityThreshold':brzaccVLVlanPriorityThreshold,'brzaccVLVLANQinQ':brzaccVLVLANQinQ,'brzaccVLQinQEthertype':brzaccVLQinQEthertype,'brzaccVLQinQProviderVlanID':brzaccVLQinQProviderVlanID,'brzaccVLVlanExtendedAccessRulesTable':brzaccVLVlanExtendedAccessRulesTable,'brzaccVLVlanExtendedAccessRulesEntry':brzaccVLVlanExtendedAccessRulesEntry,_AT:brzaccVLVlanExtendedAccessRulesTableIdx,'brzaccVLVlanExtendedAccessRuleId':brzaccVLVlanExtendedAccessRuleId,'brzaccVLVlanExtendedAccessRuleVlanId':brzaccVLVlanExtendedAccessRuleVlanId,'brzaccVLVlanExtendedAccessRulePriority':brzaccVLVlanExtendedAccessRulePriority,'brzaccVLVlanExtendedAccessRuleMulticastAllowed':brzaccVLVlanExtendedAccessRuleMulticastAllowed,'brzaccVLVlanExtendedAccessRuleOpType':brzaccVLVlanExtendedAccessRuleOpType,'brzaccVLVlanExtendedAccessRuleOperands':brzaccVLVlanExtendedAccessRuleOperands,'brzaccVLVlanExtendedTrunkVlanID':brzaccVLVlanExtendedTrunkVlanID,'brzaccVLBridgeAgingTime':brzaccVLBridgeAgingTime,'brzaccVLBroadcastRelaying':brzaccVLBroadcastRelaying,'brzaccVLUnicastRelaying':brzaccVLUnicastRelaying,'brzaccVLEthBroadcastFiltering':brzaccVLEthBroadcastFiltering,'brzaccVLEthBroadcastingParameters':brzaccVLEthBroadcastingParameters,'brzaccVLDHCPBroadcastOverrideFilter':brzaccVLDHCPBroadcastOverrideFilter,'brzaccVLPPPoEBroadcastOverrideFilter':brzaccVLPPPoEBroadcastOverrideFilter,'brzaccVLARPBroadcastOverrideFilter':brzaccVLARPBroadcastOverrideFilter,'brzaccVLEthBroadcastMulticastLimiterOption':brzaccVLEthBroadcastMulticastLimiterOption,'brzaccVLEthBroadcastMulticastLimiterThreshold':brzaccVLEthBroadcastMulticastLimiterThreshold,'brzaccVLEthBroadcastMulticastLimiterSendTrapInterval':brzaccVLEthBroadcastMulticastLimiterSendTrapInterval,'brzaccVLToSPriorityParameters':brzaccVLToSPriorityParameters,'brzaccVLToSPrecedenceThreshold':brzaccVLToSPrecedenceThreshold,'brzaccVLRoamingOption':brzaccVLRoamingOption,'brzaccVLMacAddressDenyList':brzaccVLMacAddressDenyList,'brzaccVLMacAddressDenyListTable':brzaccVLMacAddressDenyListTable,'brzaccVLMacAddressDenyListEntry':brzaccVLMacAddressDenyListEntry,_AU:brzaccVLMacAddressDenyListTableIdx,'brzaccVLMacAddressDenyListId':brzaccVLMacAddressDenyListId,'brzaccVLMacAddressDenyListAdd':brzaccVLMacAddressDenyListAdd,'brzaccVLMacAddressDenyListRemove':brzaccVLMacAddressDenyListRemove,'brzaccVLNumberOfMacAddressesInDenyList':brzaccVLNumberOfMacAddressesInDenyList,'brzaccVLMacAddressDenyListAction':brzaccVLMacAddressDenyListAction,'brzaccVLNewMacAddressDenyListTable':brzaccVLNewMacAddressDenyListTable,'brzaccVLNewMacAddressDenyListEntry':brzaccVLNewMacAddressDenyListEntry,_AV:brzaccVLNewMacAddressDenyListId,'brzaccVLNewMacAddressDenyListCommand':brzaccVLNewMacAddressDenyListCommand,'brzAccVLPortsControl':brzAccVLPortsControl,'brzaccVLEthernetPortControl':brzaccVLEthernetPortControl,'brzaccVLSendBroadcastsMulticastsAsUnicasts':brzaccVLSendBroadcastsMulticastsAsUnicasts,'brzaccVLAirInterface':brzaccVLAirInterface,'brzaccVLESSIDParameters':brzaccVLESSIDParameters,'brzaccVLESSID':brzaccVLESSID,'brzaccVLOperatorESSIDOption':brzaccVLOperatorESSIDOption,'brzaccVLOperatorESSID':brzaccVLOperatorESSID,'brzaccVLRunTimeESSID':brzaccVLRunTimeESSID,'brzaccVLHiddenESSIDParameters':brzaccVLHiddenESSIDParameters,'brzaccVLAUHiddenESSIDOption':brzaccVLAUHiddenESSIDOption,'brzaccVLSUHiddenESSIDSupport':brzaccVLSUHiddenESSIDSupport,'brzaccVLSUHiddenESSIDTimeout':brzaccVLSUHiddenESSIDTimeout,'brzaccVLMaximumCellRadius':brzaccVLMaximumCellRadius,'brzaccVLAIFS':brzaccVLAIFS,'brzaccVLWirelessTrapThreshold':brzaccVLWirelessTrapThreshold,'brzaccVLTransmitPowerTable':brzaccVLTransmitPowerTable,'brzaccVLTransmitPowerEntry':brzaccVLTransmitPowerEntry,_AW:brzaccVLTransmitPowerIdx,'brzaccVLApplicableModulationLevel':brzaccVLApplicableModulationLevel,'brzaccVLMaximumTxPowerRange':brzaccVLMaximumTxPowerRange,'brzaccVLTxPower':brzaccVLTxPower,'brzaccVLCurrentTxPower':brzaccVLCurrentTxPower,'brzaccVLMaximumTransmitPowerTable':brzaccVLMaximumTransmitPowerTable,'brzaccVLMaximumTransmitPowerEntry':brzaccVLMaximumTransmitPowerEntry,_AY:brzaccVLMaximumTransmitPowerIdx,'brzaccVLMaxTxApplicableModulationLevel':brzaccVLMaxTxApplicableModulationLevel,'brzaccVLDefinedMaximumTxPowerRange':brzaccVLDefinedMaximumTxPowerRange,'brzaccVLMaxTxPower':brzaccVLMaxTxPower,'brzaccVLMaxNumOfAssociations':brzaccVLMaxNumOfAssociations,'brzaccVLBestAu':brzaccVLBestAu,'brzaccVLBestAuSupport':brzaccVLBestAuSupport,'brzaccVLBestAuNoOfScanningAttempts':brzaccVLBestAuNoOfScanningAttempts,'brzaccVLPreferredAuMacAddress':brzaccVLPreferredAuMacAddress,'brzaccVLNeighborAuTable':brzaccVLNeighborAuTable,'brzaccVLNeighborAuEntry':brzaccVLNeighborAuEntry,_AZ:brzaccVLNeighborAuIdx,'brzaccVLNeighborAuMacAdd':brzaccVLNeighborAuMacAdd,'brzaccVLNeighborAuESSID':brzaccVLNeighborAuESSID,'brzaccVLNeighborAuSNR':brzaccVLNeighborAuSNR,'brzaccVLNeighborAuAssocLoadStatus':brzaccVLNeighborAuAssocLoadStatus,'brzaccVLNeighborAuMark':brzaccVLNeighborAuMark,'brzaccVLNeighborAuHwRevision':brzaccVLNeighborAuHwRevision,'brzaccVLNeighborAuCountryCode':brzaccVLNeighborAuCountryCode,'brzaccVLNeighborAuSwVer':brzaccVLNeighborAuSwVer,'brzaccVLNeighborAuAtpcOption':brzaccVLNeighborAuAtpcOption,'brzaccVLNeighborAuAdapModOption':brzaccVLNeighborAuAdapModOption,'brzaccVLNeighborAuBurstModeOption':brzaccVLNeighborAuBurstModeOption,'brzaccVLNeighborAuDfsOption':brzaccVLNeighborAuDfsOption,'brzaccVLNeighborAuConcatenationOption':brzaccVLNeighborAuConcatenationOption,'brzaccVLNeighborAuLearnCountryCodeBySU':brzaccVLNeighborAuLearnCountryCodeBySU,'brzaccVLNeighborAuSecurityMode':brzaccVLNeighborAuSecurityMode,'brzaccVLNeighborAuAuthOption':brzaccVLNeighborAuAuthOption,'brzaccVLNeighborAuDataEncyptOption':brzaccVLNeighborAuDataEncyptOption,'brzaccVLNeighborAuPerSuDistanceLearning':brzaccVLNeighborAuPerSuDistanceLearning,'brzaccVLNeighborAuRSSI':brzaccVLNeighborAuRSSI,'brzaccVLFrequencyDefinition':brzaccVLFrequencyDefinition,'brzaccVLSubBandLowerFrequency':brzaccVLSubBandLowerFrequency,'brzaccVLSubBandUpperFrequency':brzaccVLSubBandUpperFrequency,'brzaccVLScanningStep':brzaccVLScanningStep,'brzaccVLFrequencySubsetTable':brzaccVLFrequencySubsetTable,'brzaccVLFrequencySubsetEntry':brzaccVLFrequencySubsetEntry,_Aa:brzaccVLFrequencySubsetTableIdx,'brzaccVLFrequencySubsetFrequency':brzaccVLFrequencySubsetFrequency,'brzaccVLFrequencySubsetActive':brzaccVLFrequencySubsetActive,'brzaccVLFrequencySubsetFrequencyNew':brzaccVLFrequencySubsetFrequencyNew,'brzaccVLSetSelectedFreqSubset':brzaccVLSetSelectedFreqSubset,'brzaccVLCurrentFrequencySubsetTable':brzaccVLCurrentFrequencySubsetTable,'brzaccVLCurrentFrequencySubsetEntry':brzaccVLCurrentFrequencySubsetEntry,_Ac:brzaccVLCurrentFrequencySubsetTableIdx,'brzaccVLCurrentFrequencySubsetFrequency':brzaccVLCurrentFrequencySubsetFrequency,'brzaccVLCurrentFrequencySubsetFrequencyNew':brzaccVLCurrentFrequencySubsetFrequencyNew,'brzaccVLCurrentAUOperatingFrequency':brzaccVLCurrentAUOperatingFrequency,'brzaccVLAUDefinedFrequency':brzaccVLAUDefinedFrequency,'brzaccVLCurrentSUOperatingFrequency':brzaccVLCurrentSUOperatingFrequency,'brzaccVLSubBandSelect':brzaccVLSubBandSelect,'brzaccVLSelectSubBandIndex':brzaccVLSelectSubBandIndex,'brzaccVLDFSParameters':brzaccVLDFSParameters,'brzaccVLDFSOption':brzaccVLDFSOption,'brzaccVLDFSChannelCheckTime':brzaccVLDFSChannelCheckTime,'brzaccVLDFSChannelAvoidancePeriod':brzaccVLDFSChannelAvoidancePeriod,'brzaccVLDFSSuWaitingOption':brzaccVLDFSSuWaitingOption,'brzaccVLDFSClearRadarDetectedChannelsAfterReset':brzaccVLDFSClearRadarDetectedChannelsAfterReset,'brzaccVLDFSRadarDetectionChannelsTable':brzaccVLDFSRadarDetectionChannelsTable,'brzaccVLDFSRadarDetectionChannelsEntry':brzaccVLDFSRadarDetectionChannelsEntry,_Ad:brzaccVLDFSChannelIdx,'brzaccVLDFSChannelFrequency':brzaccVLDFSChannelFrequency,'brzaccVLDFSChannelRadarStatus':brzaccVLDFSChannelRadarStatus,'brzaccVLDFSChannelFrequencyNew':brzaccVLDFSChannelFrequencyNew,'brzaccVLDFSMinimumPulsesToDetect':brzaccVLDFSMinimumPulsesToDetect,'brzaccVLDFSChannelReuseParameters':brzaccVLDFSChannelReuseParameters,'brzaccVLDFSChannelReuseOption':brzaccVLDFSChannelReuseOption,'brzaccVLDFSRadarActivityAssessmentPeriod':brzaccVLDFSRadarActivityAssessmentPeriod,'brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod':brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod,'brzaccVLDFSDetectionAlgorithm':brzaccVLDFSDetectionAlgorithm,'brzaccVLDFSRemoteRadarEventReports':brzaccVLDFSRemoteRadarEventReports,'brzaccVLDFSRemoteRadarEventMonitoringPeriod':brzaccVLDFSRemoteRadarEventMonitoringPeriod,'brzaccVLEnhancedETSIRadarDetection':brzaccVLEnhancedETSIRadarDetection,'brzaccVLCountryCodeLearningBySU':brzaccVLCountryCodeLearningBySU,'brzaccVLCurrentAUOperatingFrequencyNew':brzaccVLCurrentAUOperatingFrequencyNew,'brzaccVLAUDefinedFrequencyNew':brzaccVLAUDefinedFrequencyNew,'brzaccVLAutoSubBandSelect':brzaccVLAutoSubBandSelect,'brzaccVLAutoSubBandSelectedFreqSubset':brzaccVLAutoSubBandSelectedFreqSubset,'brzaccVLAutoSubBandFrequencySubsetTable':brzaccVLAutoSubBandFrequencySubsetTable,'brzaccVLAutoSubBandFrequencySubsetEntry':brzaccVLAutoSubBandFrequencySubsetEntry,_Ah:brzaccVLAutoSubBandFrequencySubsetBandIdx,_Ai:brzaccVLAutoSubBandFrequencySubsetFrequencyIdx,'brzaccVLAutoSubBandFrequencySubsetActive':brzaccVLAutoSubBandFrequencySubsetActive,'brzaccVLAutoSubBandFrequencySubsetFrequency':brzaccVLAutoSubBandFrequencySubsetFrequency,'brzaccVLAutoSubBandFrequencySubsetBandwidth':brzaccVLAutoSubBandFrequencySubsetBandwidth,'brzaccVLAutoSubBandFrequencySubsetDFSStatus':brzaccVLAutoSubBandFrequencySubsetDFSStatus,'brzaccVLATPC':brzaccVLATPC,'brzaccVLAtpcOption':brzaccVLAtpcOption,'brzaccVLDeltaFromMinSNRLevel':brzaccVLDeltaFromMinSNRLevel,'brzaccVLMinimumSNRLevel':brzaccVLMinimumSNRLevel,'brzaccVLMinimumIntervalBetweenATPCMessages':brzaccVLMinimumIntervalBetweenATPCMessages,'brzaccVLPowerLevelSteps':brzaccVLPowerLevelSteps,'brzaccVLAtpcOptionEZ':brzaccVLAtpcOptionEZ,'brzaccVLCellDistanceParameters':brzaccVLCellDistanceParameters,'brzaccVLCellDistanceMode':brzaccVLCellDistanceMode,'brzaccVLFairnessFactor':brzaccVLFairnessFactor,'brzaccVLMeasuredCellDistance':brzaccVLMeasuredCellDistance,'brzaccVLUnitWithMaxDistance':brzaccVLUnitWithMaxDistance,'brzaccVLPerSuDistanceLearning':brzaccVLPerSuDistanceLearning,'brzaccVLScanningMode':brzaccVLScanningMode,'brzaccVLAntennaGain':brzaccVLAntennaGain,'brzaccVLSpectrumAnalysisParameters':brzaccVLSpectrumAnalysisParameters,'brzaccVLSpectrumAnalysisChannelScanPeriod':brzaccVLSpectrumAnalysisChannelScanPeriod,'brzaccVLSpectrumAnalysisScanCycles':brzaccVLSpectrumAnalysisScanCycles,'brzaccVLAutomaticChannelSelection':brzaccVLAutomaticChannelSelection,'brzaccVLSpectrumAnalysisActivation':brzaccVLSpectrumAnalysisActivation,'brzaccVLSpectrumAnalysisStatus':brzaccVLSpectrumAnalysisStatus,'brzaccVLResetSpectrumCounters':brzaccVLResetSpectrumCounters,'brzaccVLSpectrumAnalysisInformationTable':brzaccVLSpectrumAnalysisInformationTable,'brzaccVLSpectrumAnalysisInformationEntry':brzaccVLSpectrumAnalysisInformationEntry,_Am:brzaccVLSpectrumAnalysisInformationTableIdx,'brzaccVLSpectrumAnalysisInformationChannel':brzaccVLSpectrumAnalysisInformationChannel,'brzaccVLSpectrumAnalysisInformationSignalCount':brzaccVLSpectrumAnalysisInformationSignalCount,'brzaccVLSpectrumAnalysisInformationSignalSNR':brzaccVLSpectrumAnalysisInformationSignalSNR,'brzaccVLSpectrumAnalysisInformationSignalWidth':brzaccVLSpectrumAnalysisInformationSignalWidth,'brzaccVLSpectrumAnalysisInformationOFDMFrames':brzaccVLSpectrumAnalysisInformationOFDMFrames,'brzaccVLSpectrumAnalysisInformationOFDMAvgSnr':brzaccVLSpectrumAnalysisInformationOFDMAvgSnr,'brzaccVLSpectrumAnalysisInformationAvgNoiseFloor':brzaccVLSpectrumAnalysisInformationAvgNoiseFloor,'brzaccVLSpectrumAnalysisInformationMaxNoiseFloor':brzaccVLSpectrumAnalysisInformationMaxNoiseFloor,'brzaccVLSpectrumAnalysisInformationSignalMaxSNR':brzaccVLSpectrumAnalysisInformationSignalMaxSNR,'brzaccVLSpectrumAnalysisInformationOFDMMaxSNR':brzaccVLSpectrumAnalysisInformationOFDMMaxSNR,'brzaccVLMaxNumOfAssociationsLimit':brzaccVLMaxNumOfAssociationsLimit,'brzaccVLDisassociate':brzaccVLDisassociate,'brzaccVLDisassociateAllSUs':brzaccVLDisassociateAllSUs,'brzaccVLDisassociateSuByMacAddress':brzaccVLDisassociateSuByMacAddress,'brzaccVLTxControl':brzaccVLTxControl,'brzaccVLLostBeaconsWatchdogThreshold':brzaccVLLostBeaconsWatchdogThreshold,'brzaccVLTransmitPower':brzaccVLTransmitPower,'brzaccVLMaximumTxPower':brzaccVLMaximumTxPower,'brzaccVLCountryCodeParameters':brzaccVLCountryCodeParameters,'brzaccVLCountryCodeReApply':brzaccVLCountryCodeReApply,'brzaccVLCountryCodeTable':brzaccVLCountryCodeTable,'brzaccVLCountryCodeEntry':brzaccVLCountryCodeEntry,_An:brzaccVLCCNumber,'brzaccVLCCName':brzaccVLCCName,'brzaccVLCCAuthenticationEncryptionSupport':brzaccVLCCAuthenticationEncryptionSupport,'brzaccVLCCDataEncryptionSupport':brzaccVLCCDataEncryptionSupport,'brzaccVLCCAESEncryptionSupport':brzaccVLCCAESEncryptionSupport,'brzaccVLCCParamsTable':brzaccVLCCParamsTable,'brzaccVLCCParamsEntry':brzaccVLCCParamsEntry,_Ao:brzaccVLCCNumberIdx,_Ap:brzaccVLCCParamsIndex,'brzaccVLCCParamsFrequencies':brzaccVLCCParamsFrequencies,'brzaccVLCCAllowedBandwidth':brzaccVLCCAllowedBandwidth,'brzaccVLCCRegulationMaxTxPowerAtAntennaPort':brzaccVLCCRegulationMaxTxPowerAtAntennaPort,'brzaccVLCCRegulationMaxEIRP':brzaccVLCCRegulationMaxEIRP,'brzaccVLCCMinModulationLevel':brzaccVLCCMinModulationLevel,'brzaccVLCCMaxModulationLevel':brzaccVLCCMaxModulationLevel,'brzaccVLCCBurstModeSupport':brzaccVLCCBurstModeSupport,'brzaccVLCCMaximumBurstDuration':brzaccVLCCMaximumBurstDuration,'brzaccVLCCDfsSupport':brzaccVLCCDfsSupport,'brzaccVLCCMinimumHwRevision':brzaccVLCCMinimumHwRevision,'brzaccVLCountryCodeSelect':brzaccVLCountryCodeSelect,'brzaccVLNoiseImmunityParameters':brzaccVLNoiseImmunityParameters,'brzaccVLNoiseImmunityAlgorithm':brzaccVLNoiseImmunityAlgorithm,'brzaccVLNoiseImmunityLevel':brzaccVLNoiseImmunityLevel,'brzaccVLSpuriousImmunityLevel':brzaccVLSpuriousImmunityLevel,'brzaccVLOFDMWeakSignal':brzaccVLOFDMWeakSignal,'brzaccVLPulseDetectionSensitivity':brzaccVLPulseDetectionSensitivity,'brzaccVLNewTransmitPowerTable':brzaccVLNewTransmitPowerTable,'brzaccVLNewTransmitPowerEntry':brzaccVLNewTransmitPowerEntry,_Aq:brzaccVLNewModulationLevelIdx,'brzaccVLNewMaximumTxPowerRange':brzaccVLNewMaximumTxPowerRange,'brzaccVLNewTxPower':brzaccVLNewTxPower,'brzaccVLNewCurrentTxPower':brzaccVLNewCurrentTxPower,'brzaccVLNewMaximumTransmitPowerTable':brzaccVLNewMaximumTransmitPowerTable,'brzaccVLNewMaximumTransmitPowerEntry':brzaccVLNewMaximumTransmitPowerEntry,_Ar:brzaccVLNewMaxModulationLevelIdx,'brzaccVLNewDefinedMaximumTxPowerRange':brzaccVLNewDefinedMaximumTxPowerRange,'brzaccVLNewMaxTxPower':brzaccVLNewMaxTxPower,'brzaccVLNoiseFloorCalculationParameters':brzaccVLNoiseFloorCalculationParameters,'brzaccVLNoiseFloorCalculationMode':brzaccVLNoiseFloorCalculationMode,'brzaccVLNoiseFloorForcedValue':brzaccVLNoiseFloorForcedValue,'brzaccVLNoiseFloorCalibrationParameters':brzaccVLNoiseFloorCalibrationParameters,'brzaccVLNoiseFloorRunCalibration':brzaccVLNoiseFloorRunCalibration,'brzaccVLNoiseFloorFieldCalibrationStatus':brzaccVLNoiseFloorFieldCalibrationStatus,'brzaccVLNoiseFloorLastFieldCalibrationResult':brzaccVLNoiseFloorLastFieldCalibrationResult,'brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration':brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration,'brzaccVLNoiseFloorAvailableCalibrationOptions':brzaccVLNoiseFloorAvailableCalibrationOptions,'brzaccVLNoiseFloorUseCalibration':brzaccVLNoiseFloorUseCalibration,'brzaccVLInterferenceMitigationParameters':brzaccVLInterferenceMitigationParameters,'brzaccVLInterferenceMitigationChannelScanPeriod':brzaccVLInterferenceMitigationChannelScanPeriod,'brzaccVLInterferenceMitigationAutomaticScanPeriod':brzaccVLInterferenceMitigationAutomaticScanPeriod,'brzaccVLInterferenceMitigationScanType':brzaccVLInterferenceMitigationScanType,'brzaccVLInterferenceMitigationScanMode':brzaccVLInterferenceMitigationScanMode,'brzaccVLInterferenceMitigationDistance':brzaccVLInterferenceMitigationDistance,'brzaccVLInterferenceMitigationThroughput':brzaccVLInterferenceMitigationThroughput,'brzaccVLInterferenceMitigationActivation':brzaccVLInterferenceMitigationActivation,'brzaccVLInterferenceMitigationStatus':brzaccVLInterferenceMitigationStatus,'brzaccVLInterferenceMitigationDeleteStatisticsFile':brzaccVLInterferenceMitigationDeleteStatisticsFile,'brzaccVLInterferenceMitigationModel':brzaccVLInterferenceMitigationModel,'brzaccVLInterferenceMitigationScanTime':brzaccVLInterferenceMitigationScanTime,'brzaccVLInterferenceMitigationAUheight':brzaccVLInterferenceMitigationAUheight,'brzaccVLInterferenceMitigationAntennaGain':brzaccVLInterferenceMitigationAntennaGain,'brzaccVLInterferenceMitigationMaxModulation':brzaccVLInterferenceMitigationMaxModulation,'brzaccVLInterferenceMitigationKeepLink':brzaccVLInterferenceMitigationKeepLink,'brzaccVLInterferenceMitigationOutputTable':brzaccVLInterferenceMitigationOutputTable,'brzaccVLInterferenceMitigationOutputEntry':brzaccVLInterferenceMitigationOutputEntry,_At:brzaccVLInterferenceMitigationOutputFrequency,'brzaccVLInterferenceMitigationOutputScanningType':brzaccVLInterferenceMitigationOutputScanningType,'brzaccVLInterferenceMitigationOutputInstallationModel':brzaccVLInterferenceMitigationOutputInstallationModel,'brzaccVLInterferenceMitigationOutputNoiseFloor':brzaccVLInterferenceMitigationOutputNoiseFloor,'brzaccVLInterferenceMitigationOutputDistance':brzaccVLInterferenceMitigationOutputDistance,'brzaccVLInterferenceMitigationOutputPerformance':brzaccVLInterferenceMitigationOutputPerformance,'brzaccVLBeaconPeriod':brzaccVLBeaconPeriod,'brzaccVLMaxBeaconsLost':brzaccVLMaxBeaconsLost,'brzaccVLServiceParameters':brzaccVLServiceParameters,'brzaccVLMirDownlink':brzaccVLMirDownlink,'brzaccVLMirUplink':brzaccVLMirUplink,'brzaccVLCirDownlink':brzaccVLCirDownlink,'brzaccVLCirUplink':brzaccVLCirUplink,'brzaccVLMaxDelay':brzaccVLMaxDelay,'brzaccVLMaxBurstDuration':brzaccVLMaxBurstDuration,'brzaccVLGracefulDegradationLimit':brzaccVLGracefulDegradationLimit,'brzaccVLMirOnlyOption':brzaccVLMirOnlyOption,'brzaccVLTrafficPrioritization':brzaccVLTrafficPrioritization,'brzaccVLTrafficPriVLAN':brzaccVLTrafficPriVLAN,'brzaccVLVLANPriorityThreshold':brzaccVLVLANPriorityThreshold,'brzaccVLTrafficPriIPToS':brzaccVLTrafficPriIPToS,'brzaccVLToSPrioritizationOption':brzaccVLToSPrioritizationOption,'brzaccVLIPPrecedenceThreshold':brzaccVLIPPrecedenceThreshold,'brzaccVLIPDSCPThreshold':brzaccVLIPDSCPThreshold,'brzaccVLTrafficPriUdpTcpPortRange':brzaccVLTrafficPriUdpTcpPortRange,'brzaccVLUdpTcpPortRangePrioritizationOption':brzaccVLUdpTcpPortRangePrioritizationOption,'brzaccVLUdpPortRangeConfig':brzaccVLUdpPortRangeConfig,'brzaccVLUdpPortPriRTPRTCP':brzaccVLUdpPortPriRTPRTCP,'brzaccVLUdpPortRangeNum':brzaccVLUdpPortRangeNum,'brzaccVLUdpPortRangeTable':brzaccVLUdpPortRangeTable,'brzaccVLUdpPortRangeEntry':brzaccVLUdpPortRangeEntry,'brzaccVLUdpPortRangeStart':brzaccVLUdpPortRangeStart,'brzaccVLUdpPortRangeEnd':brzaccVLUdpPortRangeEnd,_Av:brzaccVLUdpPortRangeIdx,'brzaccVLUdpPortRangeAdd':brzaccVLUdpPortRangeAdd,'brzaccVLUdpPortRangeDelete':brzaccVLUdpPortRangeDelete,'brzaccVLUdpPortRangeDeleteAll':brzaccVLUdpPortRangeDeleteAll,'brzaccVLTcpPortRangeConfig':brzaccVLTcpPortRangeConfig,'brzaccVLTcpPortPriRTPRTCP':brzaccVLTcpPortPriRTPRTCP,'brzaccVLTcpPortRangeNum':brzaccVLTcpPortRangeNum,'brzaccVLTcpPortRangeTable':brzaccVLTcpPortRangeTable,'brzaccVLTcpPortRangeEntry':brzaccVLTcpPortRangeEntry,'brzaccVLTcpPortRangeStart':brzaccVLTcpPortRangeStart,'brzaccVLTcpPortRangeEnd':brzaccVLTcpPortRangeEnd,_Aw:brzaccVLTcpPortRangeIdx,'brzaccVLTcpPortRangeAdd':brzaccVLTcpPortRangeAdd,'brzaccVLTcpPortRangeDelete':brzaccVLTcpPortRangeDelete,'brzaccVLTcpPortRangeDeleteAll':brzaccVLTcpPortRangeDeleteAll,'brzaccVLWirelessLinkPrioritization':brzaccVLWirelessLinkPrioritization,'brzaccVLWirelessLinkPrioritizationOption':brzaccVLWirelessLinkPrioritizationOption,'brzaccVLlowPriorityAIFS':brzaccVLlowPriorityAIFS,'brzaccVLHWRetriesHighPriority':brzaccVLHWRetriesHighPriority,'brzaccVLHWRetriesLowPriority':brzaccVLHWRetriesLowPriority,'brzaccVLAUBurstDurationHighPriority':brzaccVLAUBurstDurationHighPriority,'brzaccVLAUBurstDurationLowPriority':brzaccVLAUBurstDurationLowPriority,'brzaccVLSUBurstDurationHighPriority':brzaccVLSUBurstDurationHighPriority,'brzaccVLSUBurstDurationLowPriority':brzaccVLSUBurstDurationLowPriority,'brzaccVLTrafficPriIpRange':brzaccVLTrafficPriIpRange,'brzaccVLTrafficPriIpRangeOption':brzaccVLTrafficPriIpRangeOption,'brzaccVLTrafficPriIpRangeIpAddress':brzaccVLTrafficPriIpRangeIpAddress,'brzaccVLTrafficPriIpRangeIpMask':brzaccVLTrafficPriIpRangeIpMask,'brzaccVLDrap':brzaccVLDrap,'brzaccVLDrapSupport':brzaccVLDrapSupport,'brzaccVLDrapUdpPort':brzaccVLDrapUdpPort,'brzaccVLDrapMaxNumberOfVoiceCalls':brzaccVLDrapMaxNumberOfVoiceCalls,'brzaccVLDrapTTL':brzaccVLDrapTTL,'brzaccVLDrapNoOfActiveVoiceCalls':brzaccVLDrapNoOfActiveVoiceCalls,'brzaccVLLowPriorityTrafficMinimumPercent':brzaccVLLowPriorityTrafficMinimumPercent,'brzaccVLSUEZMirDownlink':brzaccVLSUEZMirDownlink,'brzaccVLMIRThresholdPercent':brzaccVLMIRThresholdPercent,'brzaccVLProportionalIRParameters':brzaccVLProportionalIRParameters,'brzaccVLProportionalIRFactor':brzaccVLProportionalIRFactor,'brzaccVLProportionalIRUpdatePeriod':brzaccVLProportionalIRUpdatePeriod,'brzaccVLProportionalIRThresholdPercentage':brzaccVLProportionalIRThresholdPercentage,'brzaccVLProportionalIRThresholdRate':brzaccVLProportionalIRThresholdRate,'brzaccVLUserFilterParams':brzaccVLUserFilterParams,'brzaccVLUserFilterOption':brzaccVLUserFilterOption,'brzaccVLIpFilterTable':brzaccVLIpFilterTable,'brzaccVLIpFilterEntry':brzaccVLIpFilterEntry,'brzaccVLIpID':brzaccVLIpID,'brzaccVLMaskID':brzaccVLMaskID,'brzaccVLIpFilterRange':brzaccVLIpFilterRange,_Ax:brzaccVLIpFilterIdx,'brzaccVLDeleteOneUserFilter':brzaccVLDeleteOneUserFilter,'brzaccVLDeleteAllUserFilters':brzaccVLDeleteAllUserFilters,'brzaccVLDHCPUnicastOverrideFilter':brzaccVLDHCPUnicastOverrideFilter,'brzaccVLNewIpFilterTable':brzaccVLNewIpFilterTable,'brzaccVLNewIpFilterEntry':brzaccVLNewIpFilterEntry,_Ay:brzaccVLNewIpID,'brzaccVLNewMaskID':brzaccVLNewMaskID,'brzaccVLNewIpFilterRange':brzaccVLNewIpFilterRange,'brzaccVLNewIpFilterCommand':brzaccVLNewIpFilterCommand,'brzaccVLDHCPPPPoEOverrideFilter':brzaccVLDHCPPPPoEOverrideFilter,'brzaccVLSecurityParameters':brzaccVLSecurityParameters,'brzaccVLAuthenticationAlgorithm':brzaccVLAuthenticationAlgorithm,'brzaccVLSUDefaultKeyID':brzaccVLSUDefaultKeyID,'brzaccVLDataEncryptionOption':brzaccVLDataEncryptionOption,'brzaccVLAUDefaultMulticastKeyID':brzaccVLAUDefaultMulticastKeyID,'brzaccVLSecurityMode':brzaccVLSecurityMode,'brzaccVLAuthenticationPromiscuousMode':brzaccVLAuthenticationPromiscuousMode,'brzaccVLKey1':brzaccVLKey1,'brzaccVLKey2':brzaccVLKey2,'brzaccVLKey3':brzaccVLKey3,'brzaccVLKey4':brzaccVLKey4,'brzaccVLSecurityModeSupport':brzaccVLSecurityModeSupport,'brzaccVLPerformanceParams':brzaccVLPerformanceParams,'brzaccVLRTSThreshold':brzaccVLRTSThreshold,'brzaccVLMinContentionWindow':brzaccVLMinContentionWindow,'brzaccVLMaxContentionWindow':brzaccVLMaxContentionWindow,'brzaccVLMaximumModulationLevel':brzaccVLMaximumModulationLevel,'brzaccVLMulticastModulationLevel':brzaccVLMulticastModulationLevel,'brzaccVLAvgSNRMemoryFactor':brzaccVLAvgSNRMemoryFactor,'brzaccVLHardwareRetries':brzaccVLHardwareRetries,'brzaccVLAdaptiveModulationParams':brzaccVLAdaptiveModulationParams,'brzaccVLAdaptiveModulationAlgorithmOption':brzaccVLAdaptiveModulationAlgorithmOption,'brzaccVLSoftwareRetrySupport':brzaccVLSoftwareRetrySupport,'brzaccVLNumOfSoftwareRetries':brzaccVLNumOfSoftwareRetries,'brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages':brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages,'brzaccVLAdaptiveModulationDecisionThresholds':brzaccVLAdaptiveModulationDecisionThresholds,'brzaccVLAdaptiveModulationHistorySize':brzaccVLAdaptiveModulationHistorySize,'brzaccVLAdaptiveModulationPacketThresholdToTestUpRate':brzaccVLAdaptiveModulationPacketThresholdToTestUpRate,'brzaccVLAdaptiveModulationPacketNoOnUpperRate':brzaccVLAdaptiveModulationPacketNoOnUpperRate,'brzaccVLAdaptiveModulationAlgorithm':brzaccVLAdaptiveModulationAlgorithm,'brzaccVLAdaptiveModulationRetriesOnLowerModulations':brzaccVLAdaptiveModulationRetriesOnLowerModulations,'brzaccVLAdaptiveModulationRTSDurationMode':brzaccVLAdaptiveModulationRTSDurationMode,'brzaccVLBurstMode':brzaccVLBurstMode,'brzaccVLBurstModeOption':brzaccVLBurstModeOption,'brzaccVLBurstInterval':brzaccVLBurstInterval,'brzaccVLConcatenationParameters':brzaccVLConcatenationParameters,'brzaccVLConcatenationOption':brzaccVLConcatenationOption,'brzaccVLConcatenationMaximumNumberOfFrames':brzaccVLConcatenationMaximumNumberOfFrames,'brzaccVLConcatenationMaxFrameSize':brzaccVLConcatenationMaxFrameSize,'brzaccVLControlModulationLevel':brzaccVLControlModulationLevel,'brzaccVLEthernetFrameSize':brzaccVLEthernetFrameSize,'brzaccVLRunningEthernetFrameSize':brzaccVLRunningEthernetFrameSize,'brzaccVLSiteSurvey':brzaccVLSiteSurvey,'brzaccVLAverageReceiveSNR':brzaccVLAverageReceiveSNR,'brzaccVLTrafficStatistics':brzaccVLTrafficStatistics,'brzaccVLResetTrafficCounters':brzaccVLResetTrafficCounters,'brzaccVLEthCounters':brzaccVLEthCounters,'brzaccVLTotalRxFramesViaEthernet':brzaccVLTotalRxFramesViaEthernet,'brzaccVLTxWirelessToEthernet':brzaccVLTxWirelessToEthernet,'brzaccVLWirelessLinkCounters':brzaccVLWirelessLinkCounters,'brzaccVLTxFramesToWireless':brzaccVLTxFramesToWireless,'brzaccVLAUBeaconsToWireless':brzaccVLAUBeaconsToWireless,'brzaccVLDataAndOtherMngFramesToWireless':brzaccVLDataAndOtherMngFramesToWireless,'brzaccVLTotalTxFramesToWireless':brzaccVLTotalTxFramesToWireless,'brzaccVLTotalTransmittedUnicasts':brzaccVLTotalTransmittedUnicasts,'brzaccVLTotalTransmittedConcatenatedFramesDouble':brzaccVLTotalTransmittedConcatenatedFramesDouble,'brzaccVLTotalTransmittedConcatenatedFramesSingle':brzaccVLTotalTransmittedConcatenatedFramesSingle,'brzaccVLTotalTransmittedConcatenatedFramesMore':brzaccVLTotalTransmittedConcatenatedFramesMore,'brzaccVLTotalRxFramesFromWireless':brzaccVLTotalRxFramesFromWireless,'brzaccVLTotalRetransmittedFrames':brzaccVLTotalRetransmittedFrames,'brzaccVLFramesDropped':brzaccVLFramesDropped,'brzaccVLDataFramesSubmittedToBridge':brzaccVLDataFramesSubmittedToBridge,'brzaccVLFramesSubmittedViaHighQueue':brzaccVLFramesSubmittedViaHighQueue,'brzaccVLFramesSubmittedViaMidQueue':brzaccVLFramesSubmittedViaMidQueue,'brzaccVLFramesSubmittedViaLowQueue':brzaccVLFramesSubmittedViaLowQueue,'brzaccVLTotalNoOfDataFramesSubmitted':brzaccVLTotalNoOfDataFramesSubmitted,'brzaccVLTotalRecievedDataFrames':brzaccVLTotalRecievedDataFrames,'brzaccVLRecievedBadFrames':brzaccVLRecievedBadFrames,'brzaccVLNoOfDuplicateFramesDiscarded':brzaccVLNoOfDuplicateFramesDiscarded,'brzaccVLNoOfInternallyDiscardedMirCir':brzaccVLNoOfInternallyDiscardedMirCir,'brzaccVLTotalRxConcatenatedFramesDouble':brzaccVLTotalRxConcatenatedFramesDouble,'brzaccVLTotalRxConcatenatedFramesSingle':brzaccVLTotalRxConcatenatedFramesSingle,'brzaccVLTotalRxConcatenatedFramesMore':brzaccVLTotalRxConcatenatedFramesMore,'brzaccVLTXRetransmissionPercentage':brzaccVLTXRetransmissionPercentage,'brzaccVLRXCRCPercentage':brzaccVLRXCRCPercentage,'brzaccVLWirelessLinkEvents':brzaccVLWirelessLinkEvents,'brzaccVLTxEvents':brzaccVLTxEvents,'brzaccVLDroppedFrameEvents':brzaccVLDroppedFrameEvents,'brzaccVLFramesDelayedDueToSwRetry':brzaccVLFramesDelayedDueToSwRetry,'brzaccVLUnderrunEvents':brzaccVLUnderrunEvents,'brzaccVLOthersTxEvents':brzaccVLOthersTxEvents,'brzaccVLTotalTxEvents':brzaccVLTotalTxEvents,'brzaccVLRxEvents':brzaccVLRxEvents,'brzaccVLPhyErrors':brzaccVLPhyErrors,'brzaccVLCRCErrors':brzaccVLCRCErrors,'brzaccVLOverrunEvents':brzaccVLOverrunEvents,'brzaccVLRxDecryptEvents':brzaccVLRxDecryptEvents,'brzaccVLTotalRxEvents':brzaccVLTotalRxEvents,'brzaccVLPerModulationLevelCounters':brzaccVLPerModulationLevelCounters,'brzaccVLResetPerModulationLevelCounters':brzaccVLResetPerModulationLevelCounters,'brzaccVLSUPerModulationLevelCountersTable':brzaccVLSUPerModulationLevelCountersTable,'brzaccVLSUPerModulationLevelCountersEntry':brzaccVLSUPerModulationLevelCountersEntry,_Az:brzaccVLSUPerModulationLevelCountersTableIdx,'brzaccVLSUPerModulationLevelCountersApplicableModLevel':brzaccVLSUPerModulationLevelCountersApplicableModLevel,'brzaccVLSUPerModulationLevelCountersTxSuccess':brzaccVLSUPerModulationLevelCountersTxSuccess,'brzaccVLSUPerModulationLevelCountersTxFailed':brzaccVLSUPerModulationLevelCountersTxFailed,'brzaccVLAverageModulationLevel':brzaccVLAverageModulationLevel,'brzaccVLMacAddressDatabase':brzaccVLMacAddressDatabase,'brzaccVLAUMacAddressDatabase':brzaccVLAUMacAddressDatabase,'brzaccVLAUAdbResetAllModulationLevelCounters':brzaccVLAUAdbResetAllModulationLevelCounters,'brzaccVLAUAdbTable':brzaccVLAUAdbTable,'brzaccVLAUAdbEntry':brzaccVLAUAdbEntry,_A_:brzaccVLAdbIndex,'brzaccVLAdbMacAddress':brzaccVLAdbMacAddress,'brzaccVLAdbStatus':brzaccVLAdbStatus,'brzaccVLAdbSwVersion':brzaccVLAdbSwVersion,'brzaccVLAdbSNR':brzaccVLAdbSNR,'brzaccVLAdbMaxModulationLevel':brzaccVLAdbMaxModulationLevel,'brzaccVLAdbTxFramesTotal':brzaccVLAdbTxFramesTotal,'brzaccVLAdbDroppedFramesTotal':brzaccVLAdbDroppedFramesTotal,'brzaccVLAdbTxSuccessModLevel1':brzaccVLAdbTxSuccessModLevel1,'brzaccVLAdbTxSuccessModLevel2':brzaccVLAdbTxSuccessModLevel2,'brzaccVLAdbTxSuccessModLevel3':brzaccVLAdbTxSuccessModLevel3,'brzaccVLAdbTxSuccessModLevel4':brzaccVLAdbTxSuccessModLevel4,'brzaccVLAdbTxSuccessModLevel5':brzaccVLAdbTxSuccessModLevel5,'brzaccVLAdbTxSuccessModLevel6':brzaccVLAdbTxSuccessModLevel6,'brzaccVLAdbTxSuccessModLevel7':brzaccVLAdbTxSuccessModLevel7,'brzaccVLAdbTxSuccessModLevel8':brzaccVLAdbTxSuccessModLevel8,'brzaccVLAdbTxFailedModLevel1':brzaccVLAdbTxFailedModLevel1,'brzaccVLAdbTxFailedModLevel2':brzaccVLAdbTxFailedModLevel2,'brzaccVLAdbTxFailedModLevel3':brzaccVLAdbTxFailedModLevel3,'brzaccVLAdbTxFailedModLevel4':brzaccVLAdbTxFailedModLevel4,'brzaccVLAdbTxFailedModLevel5':brzaccVLAdbTxFailedModLevel5,'brzaccVLAdbTxFailedModLevel6':brzaccVLAdbTxFailedModLevel6,'brzaccVLAdbTxFailedModLevel7':brzaccVLAdbTxFailedModLevel7,'brzaccVLAdbTxFailedModLevel8':brzaccVLAdbTxFailedModLevel8,'brzaccVLAdbCirTx':brzaccVLAdbCirTx,'brzaccVLAdbMirTx':brzaccVLAdbMirTx,'brzaccVLAdbCirRx':brzaccVLAdbCirRx,'brzaccVLAdbMirRx':brzaccVLAdbMirRx,'brzaccVLAdbCirMaxDelay':brzaccVLAdbCirMaxDelay,'brzaccVLAdbDistance':brzaccVLAdbDistance,'brzaccVLAdbHwRevision':brzaccVLAdbHwRevision,'brzaccVLAdbCpldVer':brzaccVLAdbCpldVer,'brzaccVLAdbCountryCode':brzaccVLAdbCountryCode,'brzaccVLAdbBootVer':brzaccVLAdbBootVer,'brzaccVLAdbAtpcOption':brzaccVLAdbAtpcOption,'brzaccVLAdbAdapModOption':brzaccVLAdbAdapModOption,'brzaccVLAdbBurstModeOption':brzaccVLAdbBurstModeOption,'brzaccVLAdbConcatenationOption':brzaccVLAdbConcatenationOption,'brzaccVLAdbSecurityMode':brzaccVLAdbSecurityMode,'brzaccVLAdbAuthOption':brzaccVLAdbAuthOption,'brzaccVLAdbDataEncyptOption':brzaccVLAdbDataEncyptOption,'brzaccVLAdbAge':brzaccVLAdbAge,'brzaccVLAdbUnitName':brzaccVLAdbUnitName,'brzaccVLAdbRSSI':brzaccVLAdbRSSI,'brzaccVLAdbIpAddress':brzaccVLAdbIpAddress,'brzaccVLAUNewAdbTable':brzaccVLAUNewAdbTable,'brzaccVLAUNewAdbEntry':brzaccVLAUNewAdbEntry,_B3:brzaccVLNewAdbMacAddress,'brzaccVLNewAdbIPaddress':brzaccVLNewAdbIPaddress,'brzaccVLNewAdbUnitName':brzaccVLNewAdbUnitName,'brzaccVLNewAdbUnitType':brzaccVLNewAdbUnitType,'brzaccVLNewAdbSwVersion':brzaccVLNewAdbSwVersion,'brzaccVLNewAdbHwRevision':brzaccVLNewAdbHwRevision,'brzaccVLNewAdbCpldVer':brzaccVLNewAdbCpldVer,'brzaccVLNewAdbBootVer':brzaccVLNewAdbBootVer,'brzaccVLNewAdbCountryCode':brzaccVLNewAdbCountryCode,'brzaccVLNewAdbCirTx':brzaccVLNewAdbCirTx,'brzaccVLNewAdbMirTx':brzaccVLNewAdbMirTx,'brzaccVLNewAdbCirRx':brzaccVLNewAdbCirRx,'brzaccVLNewAdbMirRx':brzaccVLNewAdbMirRx,'brzaccVLNewAdbCirMaxDelay':brzaccVLNewAdbCirMaxDelay,'brzaccVLNewAdbAtpcOption':brzaccVLNewAdbAtpcOption,'brzaccVLNewAdbAdapModOption':brzaccVLNewAdbAdapModOption,'brzaccVLNewAdbBurstModeOption':brzaccVLNewAdbBurstModeOption,'brzaccVLNewAdbConcatenationOption':brzaccVLNewAdbConcatenationOption,'brzaccVLNewAdbSecurityMode':brzaccVLNewAdbSecurityMode,'brzaccVLNewAdbAuthOption':brzaccVLNewAdbAuthOption,'brzaccVLNewAdbDataEncyptOption':brzaccVLNewAdbDataEncyptOption,'brzaccVLAdbWi2IPaddress':brzaccVLAdbWi2IPaddress,'brzaccVLNewAdbStatus':brzaccVLNewAdbStatus,'brzaccVLNewAdbAge':brzaccVLNewAdbAge,'brzaccVLNewAdbDistance':brzaccVLNewAdbDistance,'brzaccVLNewAdbSNR':brzaccVLNewAdbSNR,'brzaccVLNewAdbMaxModulationLevel':brzaccVLNewAdbMaxModulationLevel,'brzaccVLNewAdbTxFramesTotal':brzaccVLNewAdbTxFramesTotal,'brzaccVLNewAdbDroppedFramesTotal':brzaccVLNewAdbDroppedFramesTotal,'brzaccVLNewAdbTxSuccessModLevel1':brzaccVLNewAdbTxSuccessModLevel1,'brzaccVLNewAdbTxSuccessModLevel2':brzaccVLNewAdbTxSuccessModLevel2,'brzaccVLNewAdbTxSuccessModLevel3':brzaccVLNewAdbTxSuccessModLevel3,'brzaccVLNewAdbTxSuccessModLevel4':brzaccVLNewAdbTxSuccessModLevel4,'brzaccVLNewAdbTxSuccessModLevel5':brzaccVLNewAdbTxSuccessModLevel5,'brzaccVLNewAdbTxSuccessModLevel6':brzaccVLNewAdbTxSuccessModLevel6,'brzaccVLNewAdbTxSuccessModLevel7':brzaccVLNewAdbTxSuccessModLevel7,'brzaccVLNewAdbTxSuccessModLevel8':brzaccVLNewAdbTxSuccessModLevel8,'brzaccVLNewAdbTxFailedModLevel1':brzaccVLNewAdbTxFailedModLevel1,'brzaccVLNewAdbTxFailedModLevel2':brzaccVLNewAdbTxFailedModLevel2,'brzaccVLNewAdbTxFailedModLevel3':brzaccVLNewAdbTxFailedModLevel3,'brzaccVLNewAdbTxFailedModLevel4':brzaccVLNewAdbTxFailedModLevel4,'brzaccVLNewAdbTxFailedModLevel5':brzaccVLNewAdbTxFailedModLevel5,'brzaccVLNewAdbTxFailedModLevel6':brzaccVLNewAdbTxFailedModLevel6,'brzaccVLNewAdbTxFailedModLevel7':brzaccVLNewAdbTxFailedModLevel7,'brzaccVLNewAdbTxFailedModLevel8':brzaccVLNewAdbTxFailedModLevel8,'brzaccVLNewAdbMainSwVersion':brzaccVLNewAdbMainSwVersion,'brzaccVLNewAdbShadowSwVersion':brzaccVLNewAdbShadowSwVersion,'brzaccVLNewAdbReadOnlyCommunity':brzaccVLNewAdbReadOnlyCommunity,'brzaccVLNewAdbWriteCommunity':brzaccVLNewAdbWriteCommunity,'brzaccVLNewAdbAIFS':brzaccVLNewAdbAIFS,'brzaccVLNewAdbMinimumCW':brzaccVLNewAdbMinimumCW,'brzaccVLNewAdbMaximumCW':brzaccVLNewAdbMaximumCW,'brzaccVLNewAdbESSID':brzaccVLNewAdbESSID,'brzaccVLNewAdbRSSI':brzaccVLNewAdbRSSI,'brzaccVLNewAdbDfsOption':brzaccVLNewAdbDfsOption,'brzaccVLAggregateMIRCIR':brzaccVLAggregateMIRCIR,'brzaccVLAggregateMIRUplink':brzaccVLAggregateMIRUplink,'brzaccVLAggregateMIRDownlink':brzaccVLAggregateMIRDownlink,'brzaccVLAggregateCIRUplink':brzaccVLAggregateCIRUplink,'brzaccVLAggregateCIRDownlink':brzaccVLAggregateCIRDownlink,'brzaccVLUpLinkQualityIndicator':brzaccVLUpLinkQualityIndicator,'brzaccVLMeasureUpLinkQualityIndicator':brzaccVLMeasureUpLinkQualityIndicator,'brzaccVLReadUpLinkQualityIndicator':brzaccVLReadUpLinkQualityIndicator,'brzaccVLUpLinkQualityIndicatorStatus':brzaccVLUpLinkQualityIndicatorStatus,'brzaccVLMacPinpoint':brzaccVLMacPinpoint,'brzaccVLMacPinpointTable':brzaccVLMacPinpointTable,'brzaccVLMacPinpointEntry':brzaccVLMacPinpointEntry,_B4:mptEthernetStationMACAddress,'mptUnitMACAddress':mptUnitMACAddress,'brzaccVLDrapGatewaysTable':brzaccVLDrapGatewaysTable,'brzaccVLDrapGatewayEntry':brzaccVLDrapGatewayEntry,_B5:brzaccVLDrapGatewayIndex,'brzaccVLDrapGatewayIP':brzaccVLDrapGatewayIP,'brzaccVLDrapGatewayType':brzaccVLDrapGatewayType,'brzaccVLDrapGatewayNoOfActiveVoiceCalls':brzaccVLDrapGatewayNoOfActiveVoiceCalls,'brzaccVLHiddenESSIDTable':brzaccVLHiddenESSIDTable,'brzaccVLHiddenESSIDEntry':brzaccVLHiddenESSIDEntry,_B6:brzaccVLHiddenESSIDMacAddress,'brzaccVLHiddenESSIDAge':brzaccVLHiddenESSIDAge,'brzaccVLAverageReceiveRSSI':brzaccVLAverageReceiveRSSI,'brzaccVLCurrentNoiseFloor':brzaccVLCurrentNoiseFloor,'brzaccVLAverageSignalInterferenceRatio':brzaccVLAverageSignalInterferenceRatio,'brzaccVLTraps':brzaccVLTraps,_d:brzaccVLTrapSUMacAddr,'brzaccVLTrapText':brzaccVLTrapText,_A7:brzaccVLTrapToggle,_BC:brzaccVLTrapParameterChanged,_BB:brzaccVLTrapAccessRights,_B9:brzaccVLTrapLog,_BA:brzaccVLTrapTelnetUserIpAddress,_B8:brzaccVLTrapRTx,_BD:brzaccVLTrapFtpOrTftpStatus,_BE:brzaccVLDFSMoveFreq,_BF:brzaccVLDFSMoveFreqNew,_BG:brzaccVLEthBroadcastThresholdExceeded,_BH:brzaccVLTrapSubscriberType,_BI:brzaccVLTrapMACAddress,_BJ:brzaccVLNewUnitTypeTrap,_BK:brzaccVLTrapSWVersion,_J:brzaccVLTrapSequenceNumber,_e:brzaccVLTrapUnitMacAddr,_BL:brzaccVLTrapParameterGroupCode,_BM:brzaccVLTrapNewIP,'alvarionOID':alvarionOID,'brzAccessVLOID':brzAccessVLOID,'brzAccessVLAU':brzAccessVLAU,'brzAccessVLSU':brzAccessVLSU,'brzAccessVLProducts':brzAccessVLProducts,'brzaccVLSUassociatedAUTRAP':brzaccVLSUassociatedAUTRAP,'brzaccVLAUdisassociatedTRAP':brzaccVLAUdisassociatedTRAP,'brzaccVLAUagingTRAP':brzaccVLAUagingTRAP,'brzaccVLSUassociatedTRAP':brzaccVLSUassociatedTRAP,'brzaccVLAUwirelessQualityTRAP':brzaccVLAUwirelessQualityTRAP,'brzaccVLPowerUpFromReset':brzaccVLPowerUpFromReset,'brzaccVLTelnetStatusTRAP':brzaccVLTelnetStatusTRAP,'brzaccVLParameterChangedTRAP':brzaccVLParameterChangedTRAP,'brzaccVLLoadingStatusTRAP':brzaccVLLoadingStatusTRAP,'brzaccVLPromiscuousModeTRAP':brzaccVLPromiscuousModeTRAP,'brzaccVLDFSRadarDetectedTRAP':brzaccVLDFSRadarDetectedTRAP,'brzaccVLDFSFrequencyTRAP':brzaccVLDFSFrequencyTRAP,'brzaccVLDFSNoFreeChannelsExistsTRAP':brzaccVLDFSNoFreeChannelsExistsTRAP,'brzaccVLEthBroadcastMulticastLimiterTRAP':brzaccVLEthBroadcastMulticastLimiterTRAP,'brzaccVLAUSUnsupportedSubscriberTypeTRAP':brzaccVLAUSUnsupportedSubscriberTypeTRAP,'brzaccVLUnitTypeChangedTRAP':brzaccVLUnitTypeChangedTRAP,'brzaccVLWLPrioritizationNotSupportedBySUTRAP':brzaccVLWLPrioritizationNotSupportedBySUTRAP,'brzaccVLParameterChangeTRAP':brzaccVLParameterChangeTRAP,'brzaccVLRunTimeIPChangeTRAP':brzaccVLRunTimeIPChangeTRAP,'brzaccVLDisassociateAllStationsTRAP':brzaccVLDisassociateAllStationsTRAP,'brzAccessVLAU-BS':brzAccessVLAU_BS,'brzAccessVLAU-SA':brzAccessVLAU_SA,'brzAccessVLAUS-BS':brzAccessVLAUS_BS,'brzAccessVLAUS-SA':brzAccessVLAUS_SA,'brzAccessAU-EZ':brzAccessAU_EZ,'brzAccessVLSU-6-1D':brzAccessVLSU_6_1D,'brzAccessVLSU-6-BD':brzAccessVLSU_6_BD,'brzAccessVLSU-24-BD':brzAccessVLSU_24_BD,'brzAccessVLSU-BD':brzAccessVLSU_BD,'brzAccessVLSU-54-BD':brzAccessVLSU_54_BD,'brzAccessVLSU-3-1D':brzAccessVLSU_3_1D,'brzAccessVLSU-3-4D':brzAccessVLSU_3_4D,'brzAccessVLSU-I':brzAccessVLSU_I,'brzAccessVLSU-EZ':brzAccessVLSU_EZ,'brzAccessVLSU-V':brzAccessVLSU_V,'brzNetB-BU-B14':brzNetB_BU_B14,'brzNetB-BU-B28':brzNetB_BU_B28,'brzNetB-BU-B100':brzNetB_BU_B100,'brzNetB-BU-B10':brzNetB_BU_B10,'brzNetB-RB-B14':brzNetB_RB_B14,'brzNetB-RB-B28':brzNetB_RB_B28,'brzNetB-RB-B100':brzNetB_RB_B100,'brzNetB-RB-B10':brzNetB_RB_B10,'brzAccess4900-AU-BS':brzAccess4900_AU_BS,'brzAccess4900-AU-SA':brzAccess4900_AU_SA,'brzAccess4900-SU-BD':brzAccess4900_SU_BD,'brzAccessVLSU-8-BD':brzAccessVLSU_8_BD,'brzAccessVLSU-1-BD':brzAccessVLSU_1_BD,'brzAccessVLSU-3-L':brzAccessVLSU_3_L,'brzAccessVLSU-6-L':brzAccessVLSU_6_L,'brzAccessVLSU-12-L':brzAccessVLSU_12_L,'brzAccessVL-AU':brzAccessVL_AU,'brzAccessVL-SU':brzAccessVL_SU})