_BS='efmCuPme10PStatusGroup'
_BR='efmCuPAFErrorsGroup'
_BQ='ifStackCapabilityGroup'
_BP='efmCuPAFGroup'
_BO='efmCuPme10PProfileGroup'
_BN='efmCuPme2BProfileGroup'
_BM='efmCuNotificationGroup'
_BL='efmCuAlarmConfGroup'
_BK='efmCuPmeGroup'
_BJ='efmCuBasicGroup'
_BI='efmCuPmeSnrMgnCrossingClear'
_BH='efmCuPmeProtocolInitFailure'
_BG='efmCuPmeConfigInitFailure'
_BF='efmCuPmeDeviceFault'
_BE='efmCuPmeSnrMgnCrossing'
_BD='efmCuPmeLineAtnCrossing'
_BC='efmCuLowBandwidth'
_BB='efmCuPmeErrorThreshMonClrInterval'
_BA='efmCuPmeErrorThreshMonInterval'
_B9='efmCuPme10PFECUncorrectedBlocks'
_B8='efmCuPme10PFECCorrectedBlocks'
_B7='efmCuPme10PElectricalLength'
_B6='efmCuPme10PProfileRowStatus'
_B5='efmCuPme10PPayloadDRateProfile'
_B4='efmCuPme10PPayloadURateProfile'
_B3='efmCuPme10PBandNotchProfiles'
_B2='efmCuPme10PUPBOReferenceProfile'
_B1='efmCuPme10PBandplanPSDMskProfile'
_B0='efmCuPme10PProfileDescr'
_A_='efmCuPme2BProfileRowStatus'
_Az='efmCuPme2BConstellation'
_Ay='efmCuPme2BPower'
_Ax='efmCuPme2BDataRate'
_Aw='efmCuPme2BRegion'
_Av='efmCuPme2BProfileDescr'
_Au='efmCuPmeSnrMonitoringInterval'
_At='efmCuPmeMaintenanceEndTime'
_As='efmCuPmeMaintenanceStartTime'
_Ar='efmCuPmeMaintenanceMode'
_Aq='efmCuPmeProtocolInitFailEnable'
_Ap='efmCuPmeConfigInitFailEnable'
_Ao='efmCuPmeDeviceFaultEnable'
_An='efmCuPmeSnrMgnCrossingTrapEnable'
_Am='efmCuLowBandwidthEnable'
_Al='efmCuPmeTCCrcErrors'
_Ak='efmCuPmeTCCodingErrors'
_Aj='efmCuPmePeerLineAtn'
_Ai='efmCuPmePeerSnrMgn'
_Ah='efmCuPmeOperProfile'
_Ag='efmCuPmeAdminSubType'
_Af='efmCuPmeSubTypesSupported'
_Ae='efmCuPmeOperStatus'
_Ad='efmCuPAFInOverflows'
_Ac='efmCuPAFInLostEnds'
_Ab='efmCuPAFInLostStarts'
_Aa='efmCuPAFInLostFragments'
_AZ='efmCuPAFInBadFragments'
_AY='efmCuPAFInLargeFragments'
_AX='efmCuPAFInSmallFragments'
_AW='efmCuPAFInErrors'
_AV='efmCuNumPMEs'
_AU='efmCuPAFDiscoveryCode'
_AT='efmCuPAFAdminState'
_AS='efmCuPeerPAFCapacity'
_AR='efmCuPAFCapacity'
_AQ='efmCuPeerPAFSupported'
_AP='efmCuTargetWorstCaseMode'
_AO='efmCuTargetCurrentConditionSnrMgn'
_AN='efmCuTargetCurrentConditionMode'
_AM='efmCuFltStatus'
_AL='efmCuPortSide'
_AK='efmCuTargetWorstCaseSnrMgn'
_AJ='efmCuTargetDataRate'
_AI='efmCuPAFSupported'
_AH='efmCuPme10PStatusEntry'
_AG='tenths of dB'
_AF='efmCuRegenSide'
_AE='efmCuRegenIndex'
_AD='ifAvailableStackLowerLayer'
_AC='ifAvailableStackHigherLayer'
_AB='profile100'
_AA='profile70'
_A9='profile50'
_A8='profile30'
_A7='profile11'
_A6='efmCuPme10PProfileIndex'
_A5='efmCuPme2BProfileIndex'
_A4='ProfileIndexOrZero'
_A3='clearStats'
_A2='normalStats'
_A1='ProfileIndexList'
_A0='000000000000'
_z='enabled'
_y='unknown'
_x='ifSpeed'
_w='efmCuPmeLineAtnCrossingEnable'
_v='efmCuThreshLowBandwidth'
_u='efmCuPmeLineAtn'
_t='efmCuPmeOperSubType'
_s='efmCuPmeAdminProfile'
_r='ifAvailableStackStatus'
_q='efmCuPAFRemoteDiscoveryCode'
_p='efmCuAdminProfile'
_o='profile25'
_n='profile20'
_m='profile15'
_l='profile9'
_k='profile8'
_j='profile7'
_i='profile6'
_h='profile4'
_g='profile3'
_f='profile2'
_e='profile1'
_d='ieee10PassTSR'
_c='ieee10PassTSO'
_b='ieee2BaseTLR'
_a='ieee2BaseTLO'
_Z='Kbps'
_Y='disabled'
_X='PhysAddress'
_W='SnmpAdminString'
_V='efmCuPmeThreshLineAtn'
_U='efmCuPmeSnrMgn'
_T='Seconds'
_S='profile10'
_R='DisplayString'
_Q='efmCuPmeThreshMaxSnrMgnDelta'
_P='efmCuPmeThreshMinSnrMgn'
_O='efmCuPmeFltStatus'
_N='profile5'
_M='Bits'
_L='not-accessible'
_K='ifIndex'
_J='dB'
_I='IF-MIB'
_H='Unsigned32'
_G='TruthValue'
_F='read-create'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='EFM-CU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex,ifSpeed=mibBuilder.importSymbols(_I,'InterfaceIndex',_K,_x)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_W)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_M,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_R,_X,'RowStatus','TextualConvention',_G)
ietfDrafts,=mibBuilder.importSymbols('Zhone','ietfDrafts')
efmCuMIB=ModuleIdentity((1,3,6,1,4,1,5504,10,1,7))
if mibBuilder.loadTexts:efmCuMIB.setRevisions(('2012-06-29 00:00','2005-04-04 00:00'))
class ProfileIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class ProfileIndexOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ProfileIndexList(TextualConvention,OctetString):status=_A;displayHint='1d:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
class TruthValueOrUnknown(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_y,0),('true',1),('false',2)))
_EfmCuObjects_ObjectIdentity=ObjectIdentity
efmCuObjects=_EfmCuObjects_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1))
_EfmCuPort_ObjectIdentity=ObjectIdentity
efmCuPort=_EfmCuPort_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1,1))
_EfmCuPortNotifications_ObjectIdentity=ObjectIdentity
efmCuPortNotifications=_EfmCuPortNotifications_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1,1,0))
_EfmCuPortConfTable_Object=MibTable
efmCuPortConfTable=_EfmCuPortConfTable_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1))
if mibBuilder.loadTexts:efmCuPortConfTable.setStatus(_A)
_EfmCuPortConfEntry_Object=MibTableRow
efmCuPortConfEntry=_EfmCuPortConfEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1))
efmCuPortConfEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:efmCuPortConfEntry.setStatus(_A)
class _EfmCuPAFAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_z,1),(_Y,2)))
_EfmCuPAFAdminState_Type.__name__=_E
_EfmCuPAFAdminState_Object=MibTableColumn
efmCuPAFAdminState=_EfmCuPAFAdminState_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,1),_EfmCuPAFAdminState_Type())
efmCuPAFAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPAFAdminState.setStatus(_A)
class _EfmCuPAFDiscoveryCode_Type(PhysAddress):defaultHexValue=_A0
_EfmCuPAFDiscoveryCode_Type.__name__=_X
_EfmCuPAFDiscoveryCode_Object=MibTableColumn
efmCuPAFDiscoveryCode=_EfmCuPAFDiscoveryCode_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,2),_EfmCuPAFDiscoveryCode_Type())
efmCuPAFDiscoveryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPAFDiscoveryCode.setStatus(_A)
class _EfmCuAdminProfile_Type(ProfileIndexList):defaultHexValue='01'
_EfmCuAdminProfile_Type.__name__=_A1
_EfmCuAdminProfile_Object=MibTableColumn
efmCuAdminProfile=_EfmCuAdminProfile_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,3),_EfmCuAdminProfile_Type())
efmCuAdminProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuAdminProfile.setStatus(_A)
class _EfmCuTargetDataRate_Type(Unsigned32):defaultValue=50000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000),ValueRangeConstraint(999999,999999))
_EfmCuTargetDataRate_Type.__name__=_H
_EfmCuTargetDataRate_Object=MibTableColumn
efmCuTargetDataRate=_EfmCuTargetDataRate_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,4),_EfmCuTargetDataRate_Type())
efmCuTargetDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuTargetDataRate.setStatus(_A)
if mibBuilder.loadTexts:efmCuTargetDataRate.setUnits(_Z)
class _EfmCuTargetWorstCaseSnrMgn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,21))
_EfmCuTargetWorstCaseSnrMgn_Type.__name__=_E
_EfmCuTargetWorstCaseSnrMgn_Object=MibTableColumn
efmCuTargetWorstCaseSnrMgn=_EfmCuTargetWorstCaseSnrMgn_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,5),_EfmCuTargetWorstCaseSnrMgn_Type())
efmCuTargetWorstCaseSnrMgn.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuTargetWorstCaseSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:efmCuTargetWorstCaseSnrMgn.setUnits(_J)
class _EfmCuThreshLowBandwidth_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_EfmCuThreshLowBandwidth_Type.__name__=_H
_EfmCuThreshLowBandwidth_Object=MibTableColumn
efmCuThreshLowBandwidth=_EfmCuThreshLowBandwidth_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,6),_EfmCuThreshLowBandwidth_Type())
efmCuThreshLowBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuThreshLowBandwidth.setStatus(_A)
if mibBuilder.loadTexts:efmCuThreshLowBandwidth.setUnits(_Z)
class _EfmCuLowBandwidthEnable_Type(TruthValue):defaultValue=2
_EfmCuLowBandwidthEnable_Type.__name__=_G
_EfmCuLowBandwidthEnable_Object=MibTableColumn
efmCuLowBandwidthEnable=_EfmCuLowBandwidthEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,7),_EfmCuLowBandwidthEnable_Type())
efmCuLowBandwidthEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuLowBandwidthEnable.setStatus(_A)
class _EfmCuTargetCurrentConditionMode_Type(TruthValue):defaultValue=2
_EfmCuTargetCurrentConditionMode_Type.__name__=_G
_EfmCuTargetCurrentConditionMode_Object=MibTableColumn
efmCuTargetCurrentConditionMode=_EfmCuTargetCurrentConditionMode_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,8),_EfmCuTargetCurrentConditionMode_Type())
efmCuTargetCurrentConditionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuTargetCurrentConditionMode.setStatus(_A)
class _EfmCuTargetCurrentConditionSnrMgn_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,21))
_EfmCuTargetCurrentConditionSnrMgn_Type.__name__=_E
_EfmCuTargetCurrentConditionSnrMgn_Object=MibTableColumn
efmCuTargetCurrentConditionSnrMgn=_EfmCuTargetCurrentConditionSnrMgn_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,9),_EfmCuTargetCurrentConditionSnrMgn_Type())
efmCuTargetCurrentConditionSnrMgn.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuTargetCurrentConditionSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:efmCuTargetCurrentConditionSnrMgn.setUnits(_J)
class _EfmCuTargetWorstCaseMode_Type(TruthValue):defaultValue=1
_EfmCuTargetWorstCaseMode_Type.__name__=_G
_EfmCuTargetWorstCaseMode_Object=MibTableColumn
efmCuTargetWorstCaseMode=_EfmCuTargetWorstCaseMode_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,10),_EfmCuTargetWorstCaseMode_Type())
efmCuTargetWorstCaseMode.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuTargetWorstCaseMode.setStatus(_A)
class _EfmCuPAFAutoDiscovery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),('optional',2),('required',3)))
_EfmCuPAFAutoDiscovery_Type.__name__=_E
_EfmCuPAFAutoDiscovery_Object=MibTableColumn
efmCuPAFAutoDiscovery=_EfmCuPAFAutoDiscovery_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,11),_EfmCuPAFAutoDiscovery_Type())
efmCuPAFAutoDiscovery.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPAFAutoDiscovery.setStatus(_A)
class _EfmCuPmeErrorClearStats_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A2,1),(_A3,2)))
_EfmCuPmeErrorClearStats_Type.__name__=_E
_EfmCuPmeErrorClearStats_Object=MibTableColumn
efmCuPmeErrorClearStats=_EfmCuPmeErrorClearStats_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,12),_EfmCuPmeErrorClearStats_Type())
efmCuPmeErrorClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeErrorClearStats.setStatus(_A)
class _EfmCuPmeSnrClearStats_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A2,1),(_A3,2)))
_EfmCuPmeSnrClearStats_Type.__name__=_E
_EfmCuPmeSnrClearStats_Object=MibTableColumn
efmCuPmeSnrClearStats=_EfmCuPmeSnrClearStats_Object((1,3,6,1,4,1,5504,10,1,7,1,1,1,1,13),_EfmCuPmeSnrClearStats_Type())
efmCuPmeSnrClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeSnrClearStats.setStatus(_A)
_EfmCuPortCapabilityTable_Object=MibTable
efmCuPortCapabilityTable=_EfmCuPortCapabilityTable_Object((1,3,6,1,4,1,5504,10,1,7,1,1,2))
if mibBuilder.loadTexts:efmCuPortCapabilityTable.setStatus(_A)
_EfmCuPortCapabilityEntry_Object=MibTableRow
efmCuPortCapabilityEntry=_EfmCuPortCapabilityEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,1,2,1))
efmCuPortCapabilityEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:efmCuPortCapabilityEntry.setStatus(_A)
_EfmCuPAFSupported_Type=TruthValue
_EfmCuPAFSupported_Object=MibTableColumn
efmCuPAFSupported=_EfmCuPAFSupported_Object((1,3,6,1,4,1,5504,10,1,7,1,1,2,1,1),_EfmCuPAFSupported_Type())
efmCuPAFSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFSupported.setStatus(_A)
_EfmCuPeerPAFSupported_Type=TruthValueOrUnknown
_EfmCuPeerPAFSupported_Object=MibTableColumn
efmCuPeerPAFSupported=_EfmCuPeerPAFSupported_Object((1,3,6,1,4,1,5504,10,1,7,1,1,2,1,2),_EfmCuPeerPAFSupported_Type())
efmCuPeerPAFSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPeerPAFSupported.setStatus(_A)
class _EfmCuPAFCapacity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_EfmCuPAFCapacity_Type.__name__=_H
_EfmCuPAFCapacity_Object=MibTableColumn
efmCuPAFCapacity=_EfmCuPAFCapacity_Object((1,3,6,1,4,1,5504,10,1,7,1,1,2,1,3),_EfmCuPAFCapacity_Type())
efmCuPAFCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFCapacity.setStatus(_A)
class _EfmCuPeerPAFCapacity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,32))
_EfmCuPeerPAFCapacity_Type.__name__=_H
_EfmCuPeerPAFCapacity_Object=MibTableColumn
efmCuPeerPAFCapacity=_EfmCuPeerPAFCapacity_Object((1,3,6,1,4,1,5504,10,1,7,1,1,2,1,4),_EfmCuPeerPAFCapacity_Type())
efmCuPeerPAFCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPeerPAFCapacity.setStatus(_A)
_EfmCuPortStatusTable_Object=MibTable
efmCuPortStatusTable=_EfmCuPortStatusTable_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3))
if mibBuilder.loadTexts:efmCuPortStatusTable.setStatus(_A)
_EfmCuPortStatusEntry_Object=MibTableRow
efmCuPortStatusEntry=_EfmCuPortStatusEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1))
efmCuPortStatusEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:efmCuPortStatusEntry.setStatus(_A)
class _EfmCuFltStatus_Type(Bits):namedValues=NamedValues(*(('noPeer',0),('pmeSubTypeMismatch',1),('lowBandwidth',2)))
_EfmCuFltStatus_Type.__name__=_M
_EfmCuFltStatus_Object=MibTableColumn
efmCuFltStatus=_EfmCuFltStatus_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,1),_EfmCuFltStatus_Type())
efmCuFltStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuFltStatus.setStatus(_A)
class _EfmCuPortSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('subscriber',1),('office',2),(_y,3)))
_EfmCuPortSide_Type.__name__=_E
_EfmCuPortSide_Object=MibTableColumn
efmCuPortSide=_EfmCuPortSide_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,2),_EfmCuPortSide_Type())
efmCuPortSide.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPortSide.setStatus(_A)
class _EfmCuNumPMEs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_EfmCuNumPMEs_Type.__name__=_H
_EfmCuNumPMEs_Object=MibTableColumn
efmCuNumPMEs=_EfmCuNumPMEs_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,3),_EfmCuNumPMEs_Type())
efmCuNumPMEs.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuNumPMEs.setStatus(_A)
_EfmCuPAFInErrors_Type=Counter32
_EfmCuPAFInErrors_Object=MibTableColumn
efmCuPAFInErrors=_EfmCuPAFInErrors_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,4),_EfmCuPAFInErrors_Type())
efmCuPAFInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInErrors.setStatus(_A)
_EfmCuPAFInSmallFragments_Type=Counter32
_EfmCuPAFInSmallFragments_Object=MibTableColumn
efmCuPAFInSmallFragments=_EfmCuPAFInSmallFragments_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,5),_EfmCuPAFInSmallFragments_Type())
efmCuPAFInSmallFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInSmallFragments.setStatus(_A)
_EfmCuPAFInLargeFragments_Type=Counter32
_EfmCuPAFInLargeFragments_Object=MibTableColumn
efmCuPAFInLargeFragments=_EfmCuPAFInLargeFragments_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,6),_EfmCuPAFInLargeFragments_Type())
efmCuPAFInLargeFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInLargeFragments.setStatus(_A)
_EfmCuPAFInBadFragments_Type=Counter32
_EfmCuPAFInBadFragments_Object=MibTableColumn
efmCuPAFInBadFragments=_EfmCuPAFInBadFragments_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,7),_EfmCuPAFInBadFragments_Type())
efmCuPAFInBadFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInBadFragments.setStatus(_A)
_EfmCuPAFInLostFragments_Type=Counter32
_EfmCuPAFInLostFragments_Object=MibTableColumn
efmCuPAFInLostFragments=_EfmCuPAFInLostFragments_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,8),_EfmCuPAFInLostFragments_Type())
efmCuPAFInLostFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInLostFragments.setStatus(_A)
_EfmCuPAFInLostStarts_Type=Counter32
_EfmCuPAFInLostStarts_Object=MibTableColumn
efmCuPAFInLostStarts=_EfmCuPAFInLostStarts_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,9),_EfmCuPAFInLostStarts_Type())
efmCuPAFInLostStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInLostStarts.setStatus(_A)
_EfmCuPAFInLostEnds_Type=Counter32
_EfmCuPAFInLostEnds_Object=MibTableColumn
efmCuPAFInLostEnds=_EfmCuPAFInLostEnds_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,10),_EfmCuPAFInLostEnds_Type())
efmCuPAFInLostEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInLostEnds.setStatus(_A)
_EfmCuPAFInOverflows_Type=Counter32
_EfmCuPAFInOverflows_Object=MibTableColumn
efmCuPAFInOverflows=_EfmCuPAFInOverflows_Object((1,3,6,1,4,1,5504,10,1,7,1,1,3,1,11),_EfmCuPAFInOverflows_Type())
efmCuPAFInOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPAFInOverflows.setStatus(_A)
_EfmCuPme_ObjectIdentity=ObjectIdentity
efmCuPme=_EfmCuPme_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1,2))
_EfmCuPmeNotifications_ObjectIdentity=ObjectIdentity
efmCuPmeNotifications=_EfmCuPmeNotifications_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1,2,0))
_EfmCuPmeConfTable_Object=MibTable
efmCuPmeConfTable=_EfmCuPmeConfTable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1))
if mibBuilder.loadTexts:efmCuPmeConfTable.setStatus(_A)
_EfmCuPmeConfEntry_Object=MibTableRow
efmCuPmeConfEntry=_EfmCuPmeConfEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1))
efmCuPmeConfEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:efmCuPmeConfEntry.setStatus(_A)
class _EfmCuPmeAdminSubType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),(_d,4),('ieee2BaseTLor10PassTSR',5),('ieee2BaseTLor10PassTSO',6),('ieee10PassTSor2BaseTLO',7)))
_EfmCuPmeAdminSubType_Type.__name__=_E
_EfmCuPmeAdminSubType_Object=MibTableColumn
efmCuPmeAdminSubType=_EfmCuPmeAdminSubType_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,1),_EfmCuPmeAdminSubType_Type())
efmCuPmeAdminSubType.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeAdminSubType.setStatus(_A)
class _EfmCuPmeAdminProfile_Type(ProfileIndexOrZero):defaultValue=0
_EfmCuPmeAdminProfile_Type.__name__=_A4
_EfmCuPmeAdminProfile_Object=MibTableColumn
efmCuPmeAdminProfile=_EfmCuPmeAdminProfile_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,2),_EfmCuPmeAdminProfile_Type())
efmCuPmeAdminProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeAdminProfile.setStatus(_A)
class _EfmCuPAFRemoteDiscoveryCode_Type(PhysAddress):defaultHexValue=_A0
_EfmCuPAFRemoteDiscoveryCode_Type.__name__=_X
_EfmCuPAFRemoteDiscoveryCode_Object=MibTableColumn
efmCuPAFRemoteDiscoveryCode=_EfmCuPAFRemoteDiscoveryCode_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,3),_EfmCuPAFRemoteDiscoveryCode_Type())
efmCuPAFRemoteDiscoveryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPAFRemoteDiscoveryCode.setStatus(_A)
class _EfmCuPmeThreshLineAtn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128))
_EfmCuPmeThreshLineAtn_Type.__name__=_E
_EfmCuPmeThreshLineAtn_Object=MibTableColumn
efmCuPmeThreshLineAtn=_EfmCuPmeThreshLineAtn_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,4),_EfmCuPmeThreshLineAtn_Type())
efmCuPmeThreshLineAtn.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeThreshLineAtn.setStatus(_A)
if mibBuilder.loadTexts:efmCuPmeThreshLineAtn.setUnits(_J)
class _EfmCuPmeThreshMinSnrMgn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128))
_EfmCuPmeThreshMinSnrMgn_Type.__name__=_E
_EfmCuPmeThreshMinSnrMgn_Object=MibTableColumn
efmCuPmeThreshMinSnrMgn=_EfmCuPmeThreshMinSnrMgn_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,5),_EfmCuPmeThreshMinSnrMgn_Type())
efmCuPmeThreshMinSnrMgn.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeThreshMinSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:efmCuPmeThreshMinSnrMgn.setUnits(_J)
class _EfmCuPmeLineAtnCrossingEnable_Type(TruthValue):defaultValue=2
_EfmCuPmeLineAtnCrossingEnable_Type.__name__=_G
_EfmCuPmeLineAtnCrossingEnable_Object=MibTableColumn
efmCuPmeLineAtnCrossingEnable=_EfmCuPmeLineAtnCrossingEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,6),_EfmCuPmeLineAtnCrossingEnable_Type())
efmCuPmeLineAtnCrossingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeLineAtnCrossingEnable.setStatus(_A)
class _EfmCuPmeSnrMgnCrossingTrapEnable_Type(TruthValue):defaultValue=2
_EfmCuPmeSnrMgnCrossingTrapEnable_Type.__name__=_G
_EfmCuPmeSnrMgnCrossingTrapEnable_Object=MibTableColumn
efmCuPmeSnrMgnCrossingTrapEnable=_EfmCuPmeSnrMgnCrossingTrapEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,7),_EfmCuPmeSnrMgnCrossingTrapEnable_Type())
efmCuPmeSnrMgnCrossingTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeSnrMgnCrossingTrapEnable.setStatus(_A)
class _EfmCuPmeDeviceFaultEnable_Type(TruthValue):defaultValue=2
_EfmCuPmeDeviceFaultEnable_Type.__name__=_G
_EfmCuPmeDeviceFaultEnable_Object=MibTableColumn
efmCuPmeDeviceFaultEnable=_EfmCuPmeDeviceFaultEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,8),_EfmCuPmeDeviceFaultEnable_Type())
efmCuPmeDeviceFaultEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeDeviceFaultEnable.setStatus(_A)
class _EfmCuPmeConfigInitFailEnable_Type(TruthValue):defaultValue=2
_EfmCuPmeConfigInitFailEnable_Type.__name__=_G
_EfmCuPmeConfigInitFailEnable_Object=MibTableColumn
efmCuPmeConfigInitFailEnable=_EfmCuPmeConfigInitFailEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,9),_EfmCuPmeConfigInitFailEnable_Type())
efmCuPmeConfigInitFailEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeConfigInitFailEnable.setStatus(_A)
class _EfmCuPmeProtocolInitFailEnable_Type(TruthValue):defaultValue=2
_EfmCuPmeProtocolInitFailEnable_Type.__name__=_G
_EfmCuPmeProtocolInitFailEnable_Object=MibTableColumn
efmCuPmeProtocolInitFailEnable=_EfmCuPmeProtocolInitFailEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,10),_EfmCuPmeProtocolInitFailEnable_Type())
efmCuPmeProtocolInitFailEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeProtocolInitFailEnable.setStatus(_A)
class _EfmCuPmeThreshMaxSnrMgnDelta_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_EfmCuPmeThreshMaxSnrMgnDelta_Type.__name__=_E
_EfmCuPmeThreshMaxSnrMgnDelta_Object=MibTableColumn
efmCuPmeThreshMaxSnrMgnDelta=_EfmCuPmeThreshMaxSnrMgnDelta_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,11),_EfmCuPmeThreshMaxSnrMgnDelta_Type())
efmCuPmeThreshMaxSnrMgnDelta.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeThreshMaxSnrMgnDelta.setStatus(_A)
if mibBuilder.loadTexts:efmCuPmeThreshMaxSnrMgnDelta.setUnits(_J)
class _EfmCuPmeMaintenanceMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('manual',2),('automaticOnce',3),('automaticDaily',4),('automaticContinuous',5)))
_EfmCuPmeMaintenanceMode_Type.__name__=_E
_EfmCuPmeMaintenanceMode_Object=MibTableColumn
efmCuPmeMaintenanceMode=_EfmCuPmeMaintenanceMode_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,12),_EfmCuPmeMaintenanceMode_Type())
efmCuPmeMaintenanceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeMaintenanceMode.setStatus(_A)
class _EfmCuPmeMaintenanceStartTime_Type(DisplayString):defaultValue=OctetString('00:00')
_EfmCuPmeMaintenanceStartTime_Type.__name__=_R
_EfmCuPmeMaintenanceStartTime_Object=MibTableColumn
efmCuPmeMaintenanceStartTime=_EfmCuPmeMaintenanceStartTime_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,13),_EfmCuPmeMaintenanceStartTime_Type())
efmCuPmeMaintenanceStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeMaintenanceStartTime.setStatus(_A)
class _EfmCuPmeMaintenanceEndTime_Type(DisplayString):defaultValue=OctetString('23:59')
_EfmCuPmeMaintenanceEndTime_Type.__name__=_R
_EfmCuPmeMaintenanceEndTime_Object=MibTableColumn
efmCuPmeMaintenanceEndTime=_EfmCuPmeMaintenanceEndTime_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,14),_EfmCuPmeMaintenanceEndTime_Type())
efmCuPmeMaintenanceEndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeMaintenanceEndTime.setStatus(_A)
class _EfmCuPmeSnrMonitoringInterval_Type(DisplayString):defaultValue=OctetString('01:00')
_EfmCuPmeSnrMonitoringInterval_Type.__name__=_R
_EfmCuPmeSnrMonitoringInterval_Object=MibTableColumn
efmCuPmeSnrMonitoringInterval=_EfmCuPmeSnrMonitoringInterval_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,15),_EfmCuPmeSnrMonitoringInterval_Type())
efmCuPmeSnrMonitoringInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeSnrMonitoringInterval.setStatus(_A)
class _EfmCuPmeErrorThreshMonEnable_Type(TruthValue):defaultValue=2
_EfmCuPmeErrorThreshMonEnable_Type.__name__=_G
_EfmCuPmeErrorThreshMonEnable_Object=MibTableColumn
efmCuPmeErrorThreshMonEnable=_EfmCuPmeErrorThreshMonEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,16),_EfmCuPmeErrorThreshMonEnable_Type())
efmCuPmeErrorThreshMonEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeErrorThreshMonEnable.setStatus(_A)
class _EfmCuPmeErrorThreshMonNotifyEnable_Type(TruthValue):defaultValue=2
_EfmCuPmeErrorThreshMonNotifyEnable_Type.__name__=_G
_EfmCuPmeErrorThreshMonNotifyEnable_Object=MibTableColumn
efmCuPmeErrorThreshMonNotifyEnable=_EfmCuPmeErrorThreshMonNotifyEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,17),_EfmCuPmeErrorThreshMonNotifyEnable_Type())
efmCuPmeErrorThreshMonNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeErrorThreshMonNotifyEnable.setStatus(_A)
class _EfmCuPmeErrorThreshMonInterval_Type(Unsigned32):defaultValue=12;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65535))
_EfmCuPmeErrorThreshMonInterval_Type.__name__=_H
_EfmCuPmeErrorThreshMonInterval_Object=MibTableColumn
efmCuPmeErrorThreshMonInterval=_EfmCuPmeErrorThreshMonInterval_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,18),_EfmCuPmeErrorThreshMonInterval_Type())
efmCuPmeErrorThreshMonInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeErrorThreshMonInterval.setStatus(_A)
class _EfmCuPmeErrorThreshMonClrInterval_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65535))
_EfmCuPmeErrorThreshMonClrInterval_Type.__name__=_H
_EfmCuPmeErrorThreshMonClrInterval_Object=MibTableColumn
efmCuPmeErrorThreshMonClrInterval=_EfmCuPmeErrorThreshMonClrInterval_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,19),_EfmCuPmeErrorThreshMonClrInterval_Type())
efmCuPmeErrorThreshMonClrInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeErrorThreshMonClrInterval.setStatus(_A)
class _EfmCuPmeLinkTrfcDisablTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_z,1),(_Y,2)))
_EfmCuPmeLinkTrfcDisablTrapEnable_Type.__name__=_E
_EfmCuPmeLinkTrfcDisablTrapEnable_Object=MibTableColumn
efmCuPmeLinkTrfcDisablTrapEnable=_EfmCuPmeLinkTrfcDisablTrapEnable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,1,1,20),_EfmCuPmeLinkTrfcDisablTrapEnable_Type())
efmCuPmeLinkTrfcDisablTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuPmeLinkTrfcDisablTrapEnable.setStatus(_A)
_EfmCuPmeCapabilityTable_Object=MibTable
efmCuPmeCapabilityTable=_EfmCuPmeCapabilityTable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,2))
if mibBuilder.loadTexts:efmCuPmeCapabilityTable.setStatus(_A)
_EfmCuPmeCapabilityEntry_Object=MibTableRow
efmCuPmeCapabilityEntry=_EfmCuPmeCapabilityEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,2,2,1))
efmCuPmeCapabilityEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:efmCuPmeCapabilityEntry.setStatus(_A)
class _EfmCuPmeSubTypesSupported_Type(Bits):namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3)))
_EfmCuPmeSubTypesSupported_Type.__name__=_M
_EfmCuPmeSubTypesSupported_Object=MibTableColumn
efmCuPmeSubTypesSupported=_EfmCuPmeSubTypesSupported_Object((1,3,6,1,4,1,5504,10,1,7,1,2,2,1,1),_EfmCuPmeSubTypesSupported_Type())
efmCuPmeSubTypesSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeSubTypesSupported.setStatus(_A)
_EfmCuPmeStatusTable_Object=MibTable
efmCuPmeStatusTable=_EfmCuPmeStatusTable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3))
if mibBuilder.loadTexts:efmCuPmeStatusTable.setStatus(_A)
_EfmCuPmeStatusEntry_Object=MibTableRow
efmCuPmeStatusEntry=_EfmCuPmeStatusEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1))
efmCuPmeStatusEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:efmCuPmeStatusEntry.setStatus(_A)
class _EfmCuPmeOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('downNotReady',2),('downReady',3),('init',4)))
_EfmCuPmeOperStatus_Type.__name__=_E
_EfmCuPmeOperStatus_Object=MibTableColumn
efmCuPmeOperStatus=_EfmCuPmeOperStatus_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,1),_EfmCuPmeOperStatus_Type())
efmCuPmeOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeOperStatus.setStatus(_A)
class _EfmCuPmeFltStatus_Type(Bits):namedValues=NamedValues(*(('lossOfFraming',0),('snrMgnDefect',1),('lineAtnDefect',2),('deviceFault',3),('configInitFailure',4),('protocolInitFailure',5)))
_EfmCuPmeFltStatus_Type.__name__=_M
_EfmCuPmeFltStatus_Object=MibTableColumn
efmCuPmeFltStatus=_EfmCuPmeFltStatus_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,2),_EfmCuPmeFltStatus_Type())
efmCuPmeFltStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeFltStatus.setStatus(_A)
class _EfmCuPmeOperSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),(_d,4)))
_EfmCuPmeOperSubType_Type.__name__=_E
_EfmCuPmeOperSubType_Object=MibTableColumn
efmCuPmeOperSubType=_EfmCuPmeOperSubType_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,3),_EfmCuPmeOperSubType_Type())
efmCuPmeOperSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeOperSubType.setStatus(_A)
_EfmCuPmeOperProfile_Type=ProfileIndexOrZero
_EfmCuPmeOperProfile_Object=MibTableColumn
efmCuPmeOperProfile=_EfmCuPmeOperProfile_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,4),_EfmCuPmeOperProfile_Type())
efmCuPmeOperProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeOperProfile.setStatus(_A)
class _EfmCuPmeSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128),ValueRangeConstraint(65535,65535))
_EfmCuPmeSnrMgn_Type.__name__=_E
_EfmCuPmeSnrMgn_Object=MibTableColumn
efmCuPmeSnrMgn=_EfmCuPmeSnrMgn_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,5),_EfmCuPmeSnrMgn_Type())
efmCuPmeSnrMgn.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:efmCuPmeSnrMgn.setUnits(_J)
class _EfmCuPmePeerSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128),ValueRangeConstraint(65535,65535))
_EfmCuPmePeerSnrMgn_Type.__name__=_E
_EfmCuPmePeerSnrMgn_Object=MibTableColumn
efmCuPmePeerSnrMgn=_EfmCuPmePeerSnrMgn_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,6),_EfmCuPmePeerSnrMgn_Type())
efmCuPmePeerSnrMgn.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmePeerSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:efmCuPmePeerSnrMgn.setUnits(_J)
class _EfmCuPmeLineAtn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128),ValueRangeConstraint(65535,65535))
_EfmCuPmeLineAtn_Type.__name__=_E
_EfmCuPmeLineAtn_Object=MibTableColumn
efmCuPmeLineAtn=_EfmCuPmeLineAtn_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,7),_EfmCuPmeLineAtn_Type())
efmCuPmeLineAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeLineAtn.setStatus(_A)
if mibBuilder.loadTexts:efmCuPmeLineAtn.setUnits(_J)
class _EfmCuPmePeerLineAtn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128),ValueRangeConstraint(65535,65535))
_EfmCuPmePeerLineAtn_Type.__name__=_E
_EfmCuPmePeerLineAtn_Object=MibTableColumn
efmCuPmePeerLineAtn=_EfmCuPmePeerLineAtn_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,8),_EfmCuPmePeerLineAtn_Type())
efmCuPmePeerLineAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmePeerLineAtn.setStatus(_A)
if mibBuilder.loadTexts:efmCuPmePeerLineAtn.setUnits(_J)
_EfmCuPmeTCCodingErrors_Type=Counter32
_EfmCuPmeTCCodingErrors_Object=MibTableColumn
efmCuPmeTCCodingErrors=_EfmCuPmeTCCodingErrors_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,9),_EfmCuPmeTCCodingErrors_Type())
efmCuPmeTCCodingErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeTCCodingErrors.setStatus(_A)
_EfmCuPmeTCCrcErrors_Type=Counter32
_EfmCuPmeTCCrcErrors_Object=MibTableColumn
efmCuPmeTCCrcErrors=_EfmCuPmeTCCrcErrors_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,10),_EfmCuPmeTCCrcErrors_Type())
efmCuPmeTCCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeTCCrcErrors.setStatus(_A)
_EfmCuPmeSnrCrossingCnt_Type=Counter32
_EfmCuPmeSnrCrossingCnt_Object=MibTableColumn
efmCuPmeSnrCrossingCnt=_EfmCuPmeSnrCrossingCnt_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,11),_EfmCuPmeSnrCrossingCnt_Type())
efmCuPmeSnrCrossingCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeSnrCrossingCnt.setStatus(_A)
_EfmCuPmeTCDownCnt_Type=Counter32
_EfmCuPmeTCDownCnt_Object=MibTableColumn
efmCuPmeTCDownCnt=_EfmCuPmeTCDownCnt_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,12),_EfmCuPmeTCDownCnt_Type())
efmCuPmeTCDownCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeTCDownCnt.setStatus(_A)
_EfmCuPmeErrorTCDownCnt_Type=Counter32
_EfmCuPmeErrorTCDownCnt_Object=MibTableColumn
efmCuPmeErrorTCDownCnt=_EfmCuPmeErrorTCDownCnt_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,13),_EfmCuPmeErrorTCDownCnt_Type())
efmCuPmeErrorTCDownCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeErrorTCDownCnt.setStatus(_A)
_EfmCuPmeErrorRestartCnt_Type=Counter32
_EfmCuPmeErrorRestartCnt_Object=MibTableColumn
efmCuPmeErrorRestartCnt=_EfmCuPmeErrorRestartCnt_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,14),_EfmCuPmeErrorRestartCnt_Type())
efmCuPmeErrorRestartCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeErrorRestartCnt.setStatus(_A)
_EfmCuPmeSnrRestartCnt_Type=Counter32
_EfmCuPmeSnrRestartCnt_Object=MibTableColumn
efmCuPmeSnrRestartCnt=_EfmCuPmeSnrRestartCnt_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,15),_EfmCuPmeSnrRestartCnt_Type())
efmCuPmeSnrRestartCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeSnrRestartCnt.setStatus(_A)
_EfmCuPmeErrorConsecutiveSec_Type=Counter32
_EfmCuPmeErrorConsecutiveSec_Object=MibTableColumn
efmCuPmeErrorConsecutiveSec=_EfmCuPmeErrorConsecutiveSec_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,16),_EfmCuPmeErrorConsecutiveSec_Type())
efmCuPmeErrorConsecutiveSec.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeErrorConsecutiveSec.setStatus(_A)
_EfmCuPmeErrorMaxConsecutiveSec_Type=Counter32
_EfmCuPmeErrorMaxConsecutiveSec_Object=MibTableColumn
efmCuPmeErrorMaxConsecutiveSec=_EfmCuPmeErrorMaxConsecutiveSec_Object((1,3,6,1,4,1,5504,10,1,7,1,2,3,1,17),_EfmCuPmeErrorMaxConsecutiveSec_Type())
efmCuPmeErrorMaxConsecutiveSec.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPmeErrorMaxConsecutiveSec.setStatus(_A)
_EfmCuPme2B_ObjectIdentity=ObjectIdentity
efmCuPme2B=_EfmCuPme2B_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1,2,5))
_EfmCuPme2BProfileTable_Object=MibTable
efmCuPme2BProfileTable=_EfmCuPme2BProfileTable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2))
if mibBuilder.loadTexts:efmCuPme2BProfileTable.setStatus(_A)
_EfmCuPme2BProfileEntry_Object=MibTableRow
efmCuPme2BProfileEntry=_EfmCuPme2BProfileEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1))
efmCuPme2BProfileEntry.setIndexNames((0,_B,_A5))
if mibBuilder.loadTexts:efmCuPme2BProfileEntry.setStatus(_A)
_EfmCuPme2BProfileIndex_Type=ProfileIndex
_EfmCuPme2BProfileIndex_Object=MibTableColumn
efmCuPme2BProfileIndex=_EfmCuPme2BProfileIndex_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,1),_EfmCuPme2BProfileIndex_Type())
efmCuPme2BProfileIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:efmCuPme2BProfileIndex.setStatus(_A)
class _EfmCuPme2BProfileDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EfmCuPme2BProfileDescr_Type.__name__=_W
_EfmCuPme2BProfileDescr_Object=MibTableColumn
efmCuPme2BProfileDescr=_EfmCuPme2BProfileDescr_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,2),_EfmCuPme2BProfileDescr_Type())
efmCuPme2BProfileDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme2BProfileDescr.setStatus(_A)
class _EfmCuPme2BRegion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('region1',1),('region2',2)))
_EfmCuPme2BRegion_Type.__name__=_E
_EfmCuPme2BRegion_Object=MibTableColumn
efmCuPme2BRegion=_EfmCuPme2BRegion_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,3),_EfmCuPme2BRegion_Type())
efmCuPme2BRegion.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme2BRegion.setStatus(_A)
class _EfmCuPme2BDataRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15352))
_EfmCuPme2BDataRate_Type.__name__=_H
_EfmCuPme2BDataRate_Object=MibTableColumn
efmCuPme2BDataRate=_EfmCuPme2BDataRate_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,4),_EfmCuPme2BDataRate_Type())
efmCuPme2BDataRate.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme2BDataRate.setStatus(_A)
if mibBuilder.loadTexts:efmCuPme2BDataRate.setUnits(_Z)
class _EfmCuPme2BPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,42))
_EfmCuPme2BPower_Type.__name__=_H
_EfmCuPme2BPower_Object=MibTableColumn
efmCuPme2BPower=_EfmCuPme2BPower_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,5),_EfmCuPme2BPower_Type())
efmCuPme2BPower.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme2BPower.setStatus(_A)
if mibBuilder.loadTexts:efmCuPme2BPower.setUnits('0.5 dBm')
class _EfmCuPme2BConstellation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('adaptive',0),('tcpam16',1),('tcpam32',2),('tcpam4',3),('tcpam8',4),('tcpam64',5),('tcpam128',6)))
_EfmCuPme2BConstellation_Type.__name__=_E
_EfmCuPme2BConstellation_Object=MibTableColumn
efmCuPme2BConstellation=_EfmCuPme2BConstellation_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,6),_EfmCuPme2BConstellation_Type())
efmCuPme2BConstellation.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme2BConstellation.setStatus(_A)
_EfmCuPme2BProfileRowStatus_Type=RowStatus
_EfmCuPme2BProfileRowStatus_Object=MibTableColumn
efmCuPme2BProfileRowStatus=_EfmCuPme2BProfileRowStatus_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,7),_EfmCuPme2BProfileRowStatus_Type())
efmCuPme2BProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme2BProfileRowStatus.setStatus(_A)
class _EfmCuPmeNtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localOsc',1),('refClk8khz',2)))
_EfmCuPmeNtr_Type.__name__=_E
_EfmCuPmeNtr_Object=MibTableColumn
efmCuPmeNtr=_EfmCuPmeNtr_Object((1,3,6,1,4,1,5504,10,1,7,1,2,5,2,1,8),_EfmCuPmeNtr_Type())
efmCuPmeNtr.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPmeNtr.setStatus(_A)
_EfmCuPme10P_ObjectIdentity=ObjectIdentity
efmCuPme10P=_EfmCuPme10P_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1,2,6))
_EfmCuPme10PProfileTable_Object=MibTable
efmCuPme10PProfileTable=_EfmCuPme10PProfileTable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1))
if mibBuilder.loadTexts:efmCuPme10PProfileTable.setStatus(_A)
_EfmCuPme10PProfileEntry_Object=MibTableRow
efmCuPme10PProfileEntry=_EfmCuPme10PProfileEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1))
efmCuPme10PProfileEntry.setIndexNames((0,_B,_A6))
if mibBuilder.loadTexts:efmCuPme10PProfileEntry.setStatus(_A)
_EfmCuPme10PProfileIndex_Type=ProfileIndex
_EfmCuPme10PProfileIndex_Object=MibTableColumn
efmCuPme10PProfileIndex=_EfmCuPme10PProfileIndex_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,1),_EfmCuPme10PProfileIndex_Type())
efmCuPme10PProfileIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:efmCuPme10PProfileIndex.setStatus(_A)
class _EfmCuPme10PProfileDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EfmCuPme10PProfileDescr_Type.__name__=_W
_EfmCuPme10PProfileDescr_Object=MibTableColumn
efmCuPme10PProfileDescr=_EfmCuPme10PProfileDescr_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,2),_EfmCuPme10PProfileDescr_Type())
efmCuPme10PProfileDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme10PProfileDescr.setStatus(_A)
class _EfmCuPme10PBandplanPSDMskProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4),(_N,5),(_i,6),(_j,7),(_k,8),(_l,9),(_S,10),(_A7,11),('profile12',12),('profile13',13),('profile14',14),(_m,15),('profile16',16),('profile17',17),('profile18',18),('profile19',19),(_n,20),('profile21',21),('profile22',22),('profile23',23),('profile24',24),(_o,25),('profile26',26),('profile27',27),('profile28',28),('profile29',29)))
_EfmCuPme10PBandplanPSDMskProfile_Type.__name__=_E
_EfmCuPme10PBandplanPSDMskProfile_Object=MibTableColumn
efmCuPme10PBandplanPSDMskProfile=_EfmCuPme10PBandplanPSDMskProfile_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,3),_EfmCuPme10PBandplanPSDMskProfile_Type())
efmCuPme10PBandplanPSDMskProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme10PBandplanPSDMskProfile.setStatus(_A)
class _EfmCuPme10PUPBOReferenceProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4),(_N,5),(_i,6),(_j,7),(_k,8),(_l,9)))
_EfmCuPme10PUPBOReferenceProfile_Type.__name__=_E
_EfmCuPme10PUPBOReferenceProfile_Object=MibTableColumn
efmCuPme10PUPBOReferenceProfile=_EfmCuPme10PUPBOReferenceProfile_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,4),_EfmCuPme10PUPBOReferenceProfile_Type())
efmCuPme10PUPBOReferenceProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme10PUPBOReferenceProfile.setStatus(_A)
class _EfmCuPme10PBandNotchProfiles_Type(Bits):namedValues=NamedValues(*(('profile0',0),(_e,1),(_f,2),(_g,3),(_h,4),(_N,5),(_i,6),(_j,7),(_k,8),(_l,9),(_S,10),(_A7,11)))
_EfmCuPme10PBandNotchProfiles_Type.__name__=_M
_EfmCuPme10PBandNotchProfiles_Object=MibTableColumn
efmCuPme10PBandNotchProfiles=_EfmCuPme10PBandNotchProfiles_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,5),_EfmCuPme10PBandNotchProfiles_Type())
efmCuPme10PBandNotchProfiles.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme10PBandNotchProfiles.setStatus(_A)
class _EfmCuPme10PPayloadURateProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,15,20,25,30,50,70,100)));namedValues=NamedValues(*((_N,5),(_S,10),(_m,15),(_n,20),(_o,25),(_A8,30),(_A9,50),(_AA,70),(_AB,100)))
_EfmCuPme10PPayloadURateProfile_Type.__name__=_E
_EfmCuPme10PPayloadURateProfile_Object=MibTableColumn
efmCuPme10PPayloadURateProfile=_EfmCuPme10PPayloadURateProfile_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,6),_EfmCuPme10PPayloadURateProfile_Type())
efmCuPme10PPayloadURateProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme10PPayloadURateProfile.setStatus(_A)
class _EfmCuPme10PPayloadDRateProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,15,20,25,30,50,70,100,140,200)));namedValues=NamedValues(*((_N,5),(_S,10),(_m,15),(_n,20),(_o,25),(_A8,30),(_A9,50),(_AA,70),(_AB,100),('profile140',140),('profile200',200)))
_EfmCuPme10PPayloadDRateProfile_Type.__name__=_E
_EfmCuPme10PPayloadDRateProfile_Object=MibTableColumn
efmCuPme10PPayloadDRateProfile=_EfmCuPme10PPayloadDRateProfile_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,7),_EfmCuPme10PPayloadDRateProfile_Type())
efmCuPme10PPayloadDRateProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme10PPayloadDRateProfile.setStatus(_A)
_EfmCuPme10PProfileRowStatus_Type=RowStatus
_EfmCuPme10PProfileRowStatus_Object=MibTableColumn
efmCuPme10PProfileRowStatus=_EfmCuPme10PProfileRowStatus_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,1,1,8),_EfmCuPme10PProfileRowStatus_Type())
efmCuPme10PProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:efmCuPme10PProfileRowStatus.setStatus(_A)
_EfmCuPme10PStatusTable_Object=MibTable
efmCuPme10PStatusTable=_EfmCuPme10PStatusTable_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,2))
if mibBuilder.loadTexts:efmCuPme10PStatusTable.setStatus(_A)
_EfmCuPme10PStatusEntry_Object=MibTableRow
efmCuPme10PStatusEntry=_EfmCuPme10PStatusEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,2,1))
if mibBuilder.loadTexts:efmCuPme10PStatusEntry.setStatus(_A)
class _EfmCuPme10PElectricalLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192),ValueRangeConstraint(65535,65535))
_EfmCuPme10PElectricalLength_Type.__name__=_E
_EfmCuPme10PElectricalLength_Object=MibTableColumn
efmCuPme10PElectricalLength=_EfmCuPme10PElectricalLength_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,2,1,1),_EfmCuPme10PElectricalLength_Type())
efmCuPme10PElectricalLength.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPme10PElectricalLength.setStatus(_A)
if mibBuilder.loadTexts:efmCuPme10PElectricalLength.setUnits('m')
_EfmCuPme10PFECCorrectedBlocks_Type=Counter32
_EfmCuPme10PFECCorrectedBlocks_Object=MibTableColumn
efmCuPme10PFECCorrectedBlocks=_EfmCuPme10PFECCorrectedBlocks_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,2,1,2),_EfmCuPme10PFECCorrectedBlocks_Type())
efmCuPme10PFECCorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPme10PFECCorrectedBlocks.setStatus(_A)
_EfmCuPme10PFECUncorrectedBlocks_Type=Counter32
_EfmCuPme10PFECUncorrectedBlocks_Object=MibTableColumn
efmCuPme10PFECUncorrectedBlocks=_EfmCuPme10PFECUncorrectedBlocks_Object((1,3,6,1,4,1,5504,10,1,7,1,2,6,2,1,3),_EfmCuPme10PFECUncorrectedBlocks_Type())
efmCuPme10PFECUncorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuPme10PFECUncorrectedBlocks.setStatus(_A)
_IfAvailableStackTable_Object=MibTable
ifAvailableStackTable=_IfAvailableStackTable_Object((1,3,6,1,4,1,5504,10,1,7,1,3))
if mibBuilder.loadTexts:ifAvailableStackTable.setStatus(_A)
_IfAvailableStackEntry_Object=MibTableRow
ifAvailableStackEntry=_IfAvailableStackEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,3,1))
ifAvailableStackEntry.setIndexNames((0,_B,_AC),(0,_B,_AD))
if mibBuilder.loadTexts:ifAvailableStackEntry.setStatus(_A)
_IfAvailableStackHigherLayer_Type=InterfaceIndex
_IfAvailableStackHigherLayer_Object=MibTableColumn
ifAvailableStackHigherLayer=_IfAvailableStackHigherLayer_Object((1,3,6,1,4,1,5504,10,1,7,1,3,1,1),_IfAvailableStackHigherLayer_Type())
ifAvailableStackHigherLayer.setMaxAccess(_L)
if mibBuilder.loadTexts:ifAvailableStackHigherLayer.setStatus(_A)
_IfAvailableStackLowerLayer_Type=InterfaceIndex
_IfAvailableStackLowerLayer_Object=MibTableColumn
ifAvailableStackLowerLayer=_IfAvailableStackLowerLayer_Object((1,3,6,1,4,1,5504,10,1,7,1,3,1,2),_IfAvailableStackLowerLayer_Type())
ifAvailableStackLowerLayer.setMaxAccess(_L)
if mibBuilder.loadTexts:ifAvailableStackLowerLayer.setStatus(_A)
class _IfAvailableStackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('capable',1),('outOfService',2)))
_IfAvailableStackStatus_Type.__name__=_E
_IfAvailableStackStatus_Object=MibTableColumn
ifAvailableStackStatus=_IfAvailableStackStatus_Object((1,3,6,1,4,1,5504,10,1,7,1,3,1,3),_IfAvailableStackStatus_Type())
ifAvailableStackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAvailableStackStatus.setStatus(_A)
_EfmCuRegeneratorStats_ObjectIdentity=ObjectIdentity
efmCuRegeneratorStats=_EfmCuRegeneratorStats_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,1,4))
_EfmCuRegeneratorStatusTable_Object=MibTable
efmCuRegeneratorStatusTable=_EfmCuRegeneratorStatusTable_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1))
if mibBuilder.loadTexts:efmCuRegeneratorStatusTable.setStatus(_A)
_EfmCuRegeneratorStatusEntry_Object=MibTableRow
efmCuRegeneratorStatusEntry=_EfmCuRegeneratorStatusEntry_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1))
efmCuRegeneratorStatusEntry.setIndexNames((0,_I,_K),(0,_B,_AE),(0,_B,_AF))
if mibBuilder.loadTexts:efmCuRegeneratorStatusEntry.setStatus(_A)
class _EfmCuRegenIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ltu-c',1),('ltu-r',2),('regenerator-1',3),('regenerator-2',4),('regenerator-3',5),('regenerator-4',6),('regenerator-5',7),('regenerator-6',8),('regenerator-7',9),('regenerator-8',10)))
_EfmCuRegenIndex_Type.__name__=_E
_EfmCuRegenIndex_Object=MibTableColumn
efmCuRegenIndex=_EfmCuRegenIndex_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,1),_EfmCuRegenIndex_Type())
efmCuRegenIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:efmCuRegenIndex.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenIndex.setUnits('Address')
class _EfmCuRegenSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('network',1),('customer',2)))
_EfmCuRegenSide_Type.__name__=_E
_EfmCuRegenSide_Object=MibTableColumn
efmCuRegenSide=_EfmCuRegenSide_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,2),_EfmCuRegenSide_Type())
efmCuRegenSide.setMaxAccess(_L)
if mibBuilder.loadTexts:efmCuRegenSide.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenSide.setUnits('Side')
_EfmCuRegenSNR_Type=Integer32
_EfmCuRegenSNR_Object=MibTableColumn
efmCuRegenSNR=_EfmCuRegenSNR_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,3),_EfmCuRegenSNR_Type())
efmCuRegenSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenSNR.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenSNR.setUnits(_AG)
_EfmCuRegenLineAttn_Type=Integer32
_EfmCuRegenLineAttn_Object=MibTableColumn
efmCuRegenLineAttn=_EfmCuRegenLineAttn_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,4),_EfmCuRegenLineAttn_Type())
efmCuRegenLineAttn.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenLineAttn.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenLineAttn.setUnits(_AG)
_EfmCuRegenCRC_Type=Counter32
_EfmCuRegenCRC_Object=MibTableColumn
efmCuRegenCRC=_EfmCuRegenCRC_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,5),_EfmCuRegenCRC_Type())
efmCuRegenCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenCRC.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenCRC.setUnits('Errors')
_EfmCuRegenES_Type=Counter32
_EfmCuRegenES_Object=MibTableColumn
efmCuRegenES=_EfmCuRegenES_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,6),_EfmCuRegenES_Type())
efmCuRegenES.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenES.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenES.setUnits(_T)
_EfmCuRegenSES_Type=Counter32
_EfmCuRegenSES_Object=MibTableColumn
efmCuRegenSES=_EfmCuRegenSES_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,7),_EfmCuRegenSES_Type())
efmCuRegenSES.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenSES.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenSES.setUnits(_T)
_EfmCuRegenUAS_Type=Counter32
_EfmCuRegenUAS_Object=MibTableColumn
efmCuRegenUAS=_EfmCuRegenUAS_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,8),_EfmCuRegenUAS_Type())
efmCuRegenUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenUAS.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenUAS.setUnits(_T)
_EfmCuRegenLOSWS_Type=Counter32
_EfmCuRegenLOSWS_Object=MibTableColumn
efmCuRegenLOSWS=_EfmCuRegenLOSWS_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,9),_EfmCuRegenLOSWS_Type())
efmCuRegenLOSWS.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenLOSWS.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenLOSWS.setUnits(_T)
class _EfmCuRegenDCAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_EfmCuRegenDCAlarm_Type.__name__=_E
_EfmCuRegenDCAlarm_Object=MibTableColumn
efmCuRegenDCAlarm=_EfmCuRegenDCAlarm_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,10),_EfmCuRegenDCAlarm_Type())
efmCuRegenDCAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:efmCuRegenDCAlarm.setStatus(_A)
if mibBuilder.loadTexts:efmCuRegenDCAlarm.setUnits('Alarm')
class _EfmCuRegenClearCounts_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normalCounts',1),('clearCounts',2)))
_EfmCuRegenClearCounts_Type.__name__=_E
_EfmCuRegenClearCounts_Object=MibTableColumn
efmCuRegenClearCounts=_EfmCuRegenClearCounts_Object((1,3,6,1,4,1,5504,10,1,7,1,4,1,1,11),_EfmCuRegenClearCounts_Type())
efmCuRegenClearCounts.setMaxAccess(_D)
if mibBuilder.loadTexts:efmCuRegenClearCounts.setStatus(_A)
_EfmCuConformance_ObjectIdentity=ObjectIdentity
efmCuConformance=_EfmCuConformance_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,2))
_EfmCuGroups_ObjectIdentity=ObjectIdentity
efmCuGroups=_EfmCuGroups_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,2,1))
_EfmCuCompliances_ObjectIdentity=ObjectIdentity
efmCuCompliances=_EfmCuCompliances_ObjectIdentity((1,3,6,1,4,1,5504,10,1,7,2,2))
efmCuPmeStatusEntry.registerAugmentions((_B,_AH))
efmCuPme10PStatusEntry.setIndexNames(*efmCuPmeStatusEntry.getIndexNames())
efmCuBasicGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,1))
efmCuBasicGroup.setObjects(*((_B,_AI),(_B,_p),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:efmCuBasicGroup.setStatus(_A)
efmCuPAFGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,2))
efmCuPAFGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_q),(_B,_AV),(_B,_r)))
if mibBuilder.loadTexts:efmCuPAFGroup.setStatus(_A)
ifStackCapabilityGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,3))
ifStackCapabilityGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:ifStackCapabilityGroup.setStatus(_A)
efmCuPAFErrorsGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,4))
efmCuPAFErrorsGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:efmCuPAFErrorsGroup.setStatus(_A)
efmCuPmeGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,5))
efmCuPmeGroup.setObjects(*((_B,_s),(_B,_Ae),(_B,_O),(_B,_Af),(_B,_Ag),(_B,_t),(_B,_q),(_B,_Ah),(_B,_U),(_B,_Ai),(_B,_u),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_V),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:efmCuPmeGroup.setStatus(_A)
efmCuAlarmConfGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,6))
efmCuAlarmConfGroup.setObjects(*((_B,_v),(_B,_Am),(_B,_V),(_B,_w),(_B,_P),(_B,_An),(_B,_w),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Q),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:efmCuAlarmConfGroup.setStatus(_A)
efmCuPme2BProfileGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,8))
efmCuPme2BProfileGroup.setObjects(*((_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_)))
if mibBuilder.loadTexts:efmCuPme2BProfileGroup.setStatus(_A)
efmCuPme10PProfileGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,9))
efmCuPme10PProfileGroup.setObjects(*((_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:efmCuPme10PProfileGroup.setStatus(_A)
efmCuPme10PStatusGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,7,2,1,10))
efmCuPme10PStatusGroup.setObjects(*((_B,_B7),(_B,_B8),(_B,_B9)))
if mibBuilder.loadTexts:efmCuPme10PStatusGroup.setStatus(_A)
efmCuLowBandwidth=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,1,0,1))
efmCuLowBandwidth.setObjects(*((_I,_x),(_B,_v)))
if mibBuilder.loadTexts:efmCuLowBandwidth.setStatus(_A)
efmCuPmeLineAtnCrossing=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,1))
efmCuPmeLineAtnCrossing.setObjects(*((_B,_u),(_B,_V)))
if mibBuilder.loadTexts:efmCuPmeLineAtnCrossing.setStatus(_A)
efmCuPmeSnrMgnCrossing=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,2))
efmCuPmeSnrMgnCrossing.setObjects(*((_B,_U),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:efmCuPmeSnrMgnCrossing.setStatus(_A)
efmCuPmeDeviceFault=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,3))
efmCuPmeDeviceFault.setObjects((_B,_O))
if mibBuilder.loadTexts:efmCuPmeDeviceFault.setStatus(_A)
efmCuPmeConfigInitFailure=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,4))
efmCuPmeConfigInitFailure.setObjects(*((_B,_O),(_B,_p),(_B,_s)))
if mibBuilder.loadTexts:efmCuPmeConfigInitFailure.setStatus(_A)
efmCuPmeProtocolInitFailure=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,5))
efmCuPmeProtocolInitFailure.setObjects(*((_B,_O),(_B,_t)))
if mibBuilder.loadTexts:efmCuPmeProtocolInitFailure.setStatus(_A)
efmCuPmeSnrMgnCrossingClear=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,6))
efmCuPmeSnrMgnCrossingClear.setObjects(*((_B,_U),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:efmCuPmeSnrMgnCrossingClear.setStatus(_A)
efmCuPmeErrorThreshEfmTrafficDisable=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,7))
efmCuPmeErrorThreshEfmTrafficDisable.setObjects((_B,_BA))
if mibBuilder.loadTexts:efmCuPmeErrorThreshEfmTrafficDisable.setStatus(_A)
efmCuPmeErrorThreshEfmTrafficEnable=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,8))
efmCuPmeErrorThreshEfmTrafficEnable.setObjects((_B,_BB))
if mibBuilder.loadTexts:efmCuPmeErrorThreshEfmTrafficEnable.setStatus(_A)
efmCuPmeBondGroupTrafficDisabled=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,9))
if mibBuilder.loadTexts:efmCuPmeBondGroupTrafficDisabled.setStatus(_A)
efmCuPmeBondGroupTrafficEnabled=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,10))
if mibBuilder.loadTexts:efmCuPmeBondGroupTrafficEnabled.setStatus(_A)
efmCuPmeLinkTrafficDisabled=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,11))
if mibBuilder.loadTexts:efmCuPmeLinkTrafficDisabled.setStatus(_A)
efmCuPmeLinkTrafficEnabled=NotificationType((1,3,6,1,4,1,5504,10,1,7,1,2,0,12))
if mibBuilder.loadTexts:efmCuPmeLinkTrafficEnabled.setStatus(_A)
efmCuNotificationGroup=NotificationGroup((1,3,6,1,4,1,5504,10,1,7,2,1,7))
efmCuNotificationGroup.setObjects(*((_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI)))
if mibBuilder.loadTexts:efmCuNotificationGroup.setStatus(_A)
efmCuCompliance=ModuleCompliance((1,3,6,1,4,1,5504,10,1,7,2,2,1))
efmCuCompliance.setObjects(*((_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS)))
if mibBuilder.loadTexts:efmCuCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ProfileIndex':ProfileIndex,_A4:ProfileIndexOrZero,_A1:ProfileIndexList,'TruthValueOrUnknown':TruthValueOrUnknown,'efmCuMIB':efmCuMIB,'efmCuObjects':efmCuObjects,'efmCuPort':efmCuPort,'efmCuPortNotifications':efmCuPortNotifications,_BC:efmCuLowBandwidth,'efmCuPortConfTable':efmCuPortConfTable,'efmCuPortConfEntry':efmCuPortConfEntry,_AT:efmCuPAFAdminState,_AU:efmCuPAFDiscoveryCode,_p:efmCuAdminProfile,_AJ:efmCuTargetDataRate,_AK:efmCuTargetWorstCaseSnrMgn,_v:efmCuThreshLowBandwidth,_Am:efmCuLowBandwidthEnable,_AN:efmCuTargetCurrentConditionMode,_AO:efmCuTargetCurrentConditionSnrMgn,_AP:efmCuTargetWorstCaseMode,'efmCuPAFAutoDiscovery':efmCuPAFAutoDiscovery,'efmCuPmeErrorClearStats':efmCuPmeErrorClearStats,'efmCuPmeSnrClearStats':efmCuPmeSnrClearStats,'efmCuPortCapabilityTable':efmCuPortCapabilityTable,'efmCuPortCapabilityEntry':efmCuPortCapabilityEntry,_AI:efmCuPAFSupported,_AQ:efmCuPeerPAFSupported,_AR:efmCuPAFCapacity,_AS:efmCuPeerPAFCapacity,'efmCuPortStatusTable':efmCuPortStatusTable,'efmCuPortStatusEntry':efmCuPortStatusEntry,_AM:efmCuFltStatus,_AL:efmCuPortSide,_AV:efmCuNumPMEs,_AW:efmCuPAFInErrors,_AX:efmCuPAFInSmallFragments,_AY:efmCuPAFInLargeFragments,_AZ:efmCuPAFInBadFragments,_Aa:efmCuPAFInLostFragments,_Ab:efmCuPAFInLostStarts,_Ac:efmCuPAFInLostEnds,_Ad:efmCuPAFInOverflows,'efmCuPme':efmCuPme,'efmCuPmeNotifications':efmCuPmeNotifications,_BD:efmCuPmeLineAtnCrossing,_BE:efmCuPmeSnrMgnCrossing,_BF:efmCuPmeDeviceFault,_BG:efmCuPmeConfigInitFailure,_BH:efmCuPmeProtocolInitFailure,_BI:efmCuPmeSnrMgnCrossingClear,'efmCuPmeErrorThreshEfmTrafficDisable':efmCuPmeErrorThreshEfmTrafficDisable,'efmCuPmeErrorThreshEfmTrafficEnable':efmCuPmeErrorThreshEfmTrafficEnable,'efmCuPmeBondGroupTrafficDisabled':efmCuPmeBondGroupTrafficDisabled,'efmCuPmeBondGroupTrafficEnabled':efmCuPmeBondGroupTrafficEnabled,'efmCuPmeLinkTrafficDisabled':efmCuPmeLinkTrafficDisabled,'efmCuPmeLinkTrafficEnabled':efmCuPmeLinkTrafficEnabled,'efmCuPmeConfTable':efmCuPmeConfTable,'efmCuPmeConfEntry':efmCuPmeConfEntry,_Ag:efmCuPmeAdminSubType,_s:efmCuPmeAdminProfile,_q:efmCuPAFRemoteDiscoveryCode,_V:efmCuPmeThreshLineAtn,_P:efmCuPmeThreshMinSnrMgn,_w:efmCuPmeLineAtnCrossingEnable,_An:efmCuPmeSnrMgnCrossingTrapEnable,_Ao:efmCuPmeDeviceFaultEnable,_Ap:efmCuPmeConfigInitFailEnable,_Aq:efmCuPmeProtocolInitFailEnable,_Q:efmCuPmeThreshMaxSnrMgnDelta,_Ar:efmCuPmeMaintenanceMode,_As:efmCuPmeMaintenanceStartTime,_At:efmCuPmeMaintenanceEndTime,_Au:efmCuPmeSnrMonitoringInterval,'efmCuPmeErrorThreshMonEnable':efmCuPmeErrorThreshMonEnable,'efmCuPmeErrorThreshMonNotifyEnable':efmCuPmeErrorThreshMonNotifyEnable,_BA:efmCuPmeErrorThreshMonInterval,_BB:efmCuPmeErrorThreshMonClrInterval,'efmCuPmeLinkTrfcDisablTrapEnable':efmCuPmeLinkTrfcDisablTrapEnable,'efmCuPmeCapabilityTable':efmCuPmeCapabilityTable,'efmCuPmeCapabilityEntry':efmCuPmeCapabilityEntry,_Af:efmCuPmeSubTypesSupported,'efmCuPmeStatusTable':efmCuPmeStatusTable,'efmCuPmeStatusEntry':efmCuPmeStatusEntry,_Ae:efmCuPmeOperStatus,_O:efmCuPmeFltStatus,_t:efmCuPmeOperSubType,_Ah:efmCuPmeOperProfile,_U:efmCuPmeSnrMgn,_Ai:efmCuPmePeerSnrMgn,_u:efmCuPmeLineAtn,_Aj:efmCuPmePeerLineAtn,_Ak:efmCuPmeTCCodingErrors,_Al:efmCuPmeTCCrcErrors,'efmCuPmeSnrCrossingCnt':efmCuPmeSnrCrossingCnt,'efmCuPmeTCDownCnt':efmCuPmeTCDownCnt,'efmCuPmeErrorTCDownCnt':efmCuPmeErrorTCDownCnt,'efmCuPmeErrorRestartCnt':efmCuPmeErrorRestartCnt,'efmCuPmeSnrRestartCnt':efmCuPmeSnrRestartCnt,'efmCuPmeErrorConsecutiveSec':efmCuPmeErrorConsecutiveSec,'efmCuPmeErrorMaxConsecutiveSec':efmCuPmeErrorMaxConsecutiveSec,'efmCuPme2B':efmCuPme2B,'efmCuPme2BProfileTable':efmCuPme2BProfileTable,'efmCuPme2BProfileEntry':efmCuPme2BProfileEntry,_A5:efmCuPme2BProfileIndex,_Av:efmCuPme2BProfileDescr,_Aw:efmCuPme2BRegion,_Ax:efmCuPme2BDataRate,_Ay:efmCuPme2BPower,_Az:efmCuPme2BConstellation,_A_:efmCuPme2BProfileRowStatus,'efmCuPmeNtr':efmCuPmeNtr,'efmCuPme10P':efmCuPme10P,'efmCuPme10PProfileTable':efmCuPme10PProfileTable,'efmCuPme10PProfileEntry':efmCuPme10PProfileEntry,_A6:efmCuPme10PProfileIndex,_B0:efmCuPme10PProfileDescr,_B1:efmCuPme10PBandplanPSDMskProfile,_B2:efmCuPme10PUPBOReferenceProfile,_B3:efmCuPme10PBandNotchProfiles,_B4:efmCuPme10PPayloadURateProfile,_B5:efmCuPme10PPayloadDRateProfile,_B6:efmCuPme10PProfileRowStatus,'efmCuPme10PStatusTable':efmCuPme10PStatusTable,_AH:efmCuPme10PStatusEntry,_B7:efmCuPme10PElectricalLength,_B8:efmCuPme10PFECCorrectedBlocks,_B9:efmCuPme10PFECUncorrectedBlocks,'ifAvailableStackTable':ifAvailableStackTable,'ifAvailableStackEntry':ifAvailableStackEntry,_AC:ifAvailableStackHigherLayer,_AD:ifAvailableStackLowerLayer,_r:ifAvailableStackStatus,'efmCuRegeneratorStats':efmCuRegeneratorStats,'efmCuRegeneratorStatusTable':efmCuRegeneratorStatusTable,'efmCuRegeneratorStatusEntry':efmCuRegeneratorStatusEntry,_AE:efmCuRegenIndex,_AF:efmCuRegenSide,'efmCuRegenSNR':efmCuRegenSNR,'efmCuRegenLineAttn':efmCuRegenLineAttn,'efmCuRegenCRC':efmCuRegenCRC,'efmCuRegenES':efmCuRegenES,'efmCuRegenSES':efmCuRegenSES,'efmCuRegenUAS':efmCuRegenUAS,'efmCuRegenLOSWS':efmCuRegenLOSWS,'efmCuRegenDCAlarm':efmCuRegenDCAlarm,'efmCuRegenClearCounts':efmCuRegenClearCounts,'efmCuConformance':efmCuConformance,'efmCuGroups':efmCuGroups,_BJ:efmCuBasicGroup,_BP:efmCuPAFGroup,_BQ:ifStackCapabilityGroup,_BR:efmCuPAFErrorsGroup,_BK:efmCuPmeGroup,_BL:efmCuAlarmConfGroup,_BM:efmCuNotificationGroup,_BN:efmCuPme2BProfileGroup,_BO:efmCuPme10PProfileGroup,_BS:efmCuPme10PStatusGroup,'efmCuCompliances':efmCuCompliances,'efmCuCompliance':efmCuCompliance})