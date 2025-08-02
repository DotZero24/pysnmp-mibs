_B9='tmnxCellularV20ConfigGroup'
_B8='tmnxCellularV19ConfigGroup'
_B7='tmnxCellNotificationV16v0Group'
_B6='tmnxCellularV16v0StatusGroup'
_B5='tmnxCellularV16v0ConfigGroup'
_B4='tmnxCellularStatusGroup'
_B3='tmnxCellularConfigGroup'
_B2='tmnxCellularActiveSimChange'
_B1='tmnxCellularNoServiceReset'
_B0='tmnxCellularBearerModified'
_A_='tmnxCellularBearerDeleted'
_Az='tmnxCellularBearerCreated'
_Ay='tmnxCellMdaMaxTxPower'
_Ax='tmnxCellMdaSpecFirmwareVersion'
_Aw='tmnxCellPdnProfProtocol'
_Av='tmnxCellMdaSimCardLastSwitchTime'
_Au='tmnxCellMdaSimCardSwitchTime'
_At='tmnxCellMdaSimCardSwitchPending'
_As='tmnxCellMdaPreferredSim'
_Ar='tmnxCellSimCardFirmwareVersion'
_Aq='tmnxCellPortTftTosMask'
_Ap='tmnxCellPortTftTos'
_Ao='tmnxCellPortTftDirection'
_An='tmnxCellPortTftEvalPrecedence'
_Am='tmnxCellPortBearerDlMbr'
_Al='tmnxCellPortBearerDlGbr'
_Ak='tmnxCellPortBearerUlMbr'
_Aj='tmnxCellPortBearerUlGbr'
_Ai='tmnxCellPortBearerQci'
_Ah='tmnxCellPortBearerType'
_Ag='tmnxCellSimCardBgpStateSwitch'
_Af='tmnxCellSimCardPortStateSwitch'
_Ae='tmnxCellSimCardFailureDuration'
_Ad='tmnxCellMdaDownResetTime'
_Ac='tmnxCellMdaDownResetPending'
_Ab='tmnxCellMdaDownResetCriteria'
_Aa='tmnxCellMdaDownResetInterval'
_AZ='tmnxCellMdaLastChanged'
_AY='tmnxCellPdnMtu'
_AX='tmnxCellPdnApn'
_AW='tmnxCellPdnSecondaryDnsAddress'
_AV='tmnxCellPdnSecondaryDnsAddrType'
_AU='tmnxCellPdnPrimaryDnsAddress'
_AT='tmnxCellPdnPrimaryDnsAddrType'
_AS='tmnxCellPdnIpAddress'
_AR='tmnxCellPdnIpAddrType'
_AQ='tmnxCellPdnConnectionState'
_AP='tmnxCellSimCardPukRetries'
_AO='tmnxCellSimCardPinRetries'
_AN='tmnxCellSimCardPinStatus'
_AM='tmnxCellSimCardLocked'
_AL='tmnxCellSimCardImsi'
_AK='tmnxCellSimCardIccid'
_AJ='tmnxCellSimCardEquipped'
_AI='tmnxCellPortRscp'
_AH='tmnxCellPortRsrp'
_AG='tmnxCellPortRssi'
_AF='tmnxCellPortCellIdentity'
_AE='tmnxCellPortAreaCode'
_AD='tmnxCellPortChannelNumber'
_AC='tmnxCellPortFrequencyBand'
_AB='tmnxCellPortWirelessTechnology'
_AA='tmnxCellPortRegistrationStatus'
_A9='tmnxCellPortImei'
_A8='tmnxCellPortBand125MaxPowerLevel'
_A7='tmnxCellPortLastChanged'
_A6='tmnxCellPortTblLastChanged'
_A5='tmnxCellPdnProfile'
_A4='tmnxCellPdnLastChanged'
_A3='tmnxCellPdnRowStatus'
_A2='tmnxCellPdnTblLastChanged'
_A1='tmnxCellSimCardPin'
_A0='tmnxCellSimCardDescription'
_z='tmnxCellSimCardLastChanged'
_y='tmnxCellSimCardTableLastChanged'
_x='tmnxCellPdnProfPassword'
_w='tmnxCellPdnProfUsername'
_v='tmnxCellPdnProfAuthType'
_u='tmnxCellPdnProfApn'
_t='tmnxCellPdnProfDescription'
_s='tmnxCellPdnProfLastChanged'
_r='tmnxCellPdnProfRowStatus'
_q='tmnxCellPdnProfileTblLastChanged'
_p='tmnxCellularPdnStatusEntry'
_o='tmnxCellularSimCardStatusEntry'
_n='accessible-for-notify'
_m='no-bgp-neighbor'
_l='cellular-port-down'
_k='TmnxCellularSimCardNumber'
_j='seconds'
_i='TmnxCellularPdnProfileId'
_h='tmnxCellPdnId'
_g='minutes'
_f='tmnxCellSimCardId'
_e='TmnxCellularAccessPointName'
_d='tmnxCellPdnProfileId'
_c='TmnxAuthPassword'
_b='tmnxPortNotifyPortId'
_a='tmnxMDASlotNum'
_Z='tmnxCardSlotNum'
_Y='OctetString'
_X='tmnxCellMdaNoServiceResetReason'
_W='tmnxCellMdaSimLastSwitchReason'
_V='tmnxCellMdaOperActiveSim'
_U='tmnxCellMdaAdminActiveSim'
_T='tmnxCellPortTftPacketFilterId'
_S='none'
_R='not-accessible'
_Q='TItemDescription'
_P='TIMETRA-CHASSIS-MIB'
_O='TruthValue'
_N='decibel-milliwatts'
_M='DisplayString'
_L='InetAddress'
_K='tmnxCellularNotifyPdnId'
_J='tmnxCellPortBearerId'
_I='tmnxPortPortID'
_H='TIMETRA-PORT-MIB'
_G='read-create'
_F='read-write'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='TIMETRA-CELLULAR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_O)
tmnxCardSlotNum,tmnxMDASlotNum=mibBuilder.importSymbols(_P,_Z,_a)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
tmnxPortNotifyPortId,tmnxPortPortID=mibBuilder.importSymbols(_H,_b,_I)
TItemDescription,TmnxAuthPassword=mibBuilder.importSymbols('TIMETRA-TC-MIB',_Q,_c)
timetraCellularMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,109))
if mibBuilder.loadTexts:timetraCellularMIBModule.setRevisions(('2016-07-18 00:00',))
class TmnxCellularPdnProfileId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
class TmnxCellularAccessPointName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
class TmnxCellularImei(DisplayString):status=_A;displayHint='2a-6a-6a-2a';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(15,16))
class TmnxCellularSimCardNumber(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
class TmnxCellularSimCardIccid(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class TmnxCellularImsi(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
class TmnxCellularPdnId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
class TmnxCellularChannelNumber(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262143))
class TmnxCellularBearerRate(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_TmnxCellularConformance_ObjectIdentity=ObjectIdentity
tmnxCellularConformance=_TmnxCellularConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,109))
_TmnxCellularCompliances_ObjectIdentity=ObjectIdentity
tmnxCellularCompliances=_TmnxCellularCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,109,1))
_TmnxCellularGroups_ObjectIdentity=ObjectIdentity
tmnxCellularGroups=_TmnxCellularGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,109,2))
_TmnxCellularV15v0Groups_ObjectIdentity=ObjectIdentity
tmnxCellularV15v0Groups=_TmnxCellularV15v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,109,2,1))
_TmnxCellularV16v0Groups_ObjectIdentity=ObjectIdentity
tmnxCellularV16v0Groups=_TmnxCellularV16v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,109,2,2))
_TmnxCellularV19Groups_ObjectIdentity=ObjectIdentity
tmnxCellularV19Groups=_TmnxCellularV19Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,109,2,3))
_TmnxCellularV20Groups_ObjectIdentity=ObjectIdentity
tmnxCellularV20Groups=_TmnxCellularV20Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,109,2,4))
_TmnxCellularObjs_ObjectIdentity=ObjectIdentity
tmnxCellularObjs=_TmnxCellularObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109))
_TmnxCellularConfigObjs_ObjectIdentity=ObjectIdentity
tmnxCellularConfigObjs=_TmnxCellularConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109,2))
_TmnxCellularConfigTimestamps_ObjectIdentity=ObjectIdentity
tmnxCellularConfigTimestamps=_TmnxCellularConfigTimestamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109,2,1))
_TmnxCellPdnProfileTblLastChanged_Type=TimeStamp
_TmnxCellPdnProfileTblLastChanged_Object=MibScalar
tmnxCellPdnProfileTblLastChanged=_TmnxCellPdnProfileTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,1,1),_TmnxCellPdnProfileTblLastChanged_Type())
tmnxCellPdnProfileTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnProfileTblLastChanged.setStatus(_A)
_TmnxCellSimCardTableLastChanged_Type=TimeStamp
_TmnxCellSimCardTableLastChanged_Object=MibScalar
tmnxCellSimCardTableLastChanged=_TmnxCellSimCardTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,1,2),_TmnxCellSimCardTableLastChanged_Type())
tmnxCellSimCardTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardTableLastChanged.setStatus(_A)
_TmnxCellPdnTblLastChanged_Type=TimeStamp
_TmnxCellPdnTblLastChanged_Object=MibScalar
tmnxCellPdnTblLastChanged=_TmnxCellPdnTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,1,3),_TmnxCellPdnTblLastChanged_Type())
tmnxCellPdnTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnTblLastChanged.setStatus(_A)
_TmnxCellPortTblLastChanged_Type=TimeStamp
_TmnxCellPortTblLastChanged_Object=MibScalar
tmnxCellPortTblLastChanged=_TmnxCellPortTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,1,4),_TmnxCellPortTblLastChanged_Type())
tmnxCellPortTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortTblLastChanged.setStatus(_A)
_TmnxCellularSystemConfigObjs_ObjectIdentity=ObjectIdentity
tmnxCellularSystemConfigObjs=_TmnxCellularSystemConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109,2,2))
_TmnxCellularPdnProfileTable_Object=MibTable
tmnxCellularPdnProfileTable=_TmnxCellularPdnProfileTable_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1))
if mibBuilder.loadTexts:tmnxCellularPdnProfileTable.setStatus(_A)
_TmnxCellPdnProfileEntry_Object=MibTableRow
tmnxCellPdnProfileEntry=_TmnxCellPdnProfileEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1))
tmnxCellPdnProfileEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:tmnxCellPdnProfileEntry.setStatus(_A)
_TmnxCellPdnProfileId_Type=TmnxCellularPdnProfileId
_TmnxCellPdnProfileId_Object=MibTableColumn
tmnxCellPdnProfileId=_TmnxCellPdnProfileId_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,1),_TmnxCellPdnProfileId_Type())
tmnxCellPdnProfileId.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxCellPdnProfileId.setStatus(_A)
_TmnxCellPdnProfRowStatus_Type=RowStatus
_TmnxCellPdnProfRowStatus_Object=MibTableColumn
tmnxCellPdnProfRowStatus=_TmnxCellPdnProfRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,2),_TmnxCellPdnProfRowStatus_Type())
tmnxCellPdnProfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfRowStatus.setStatus(_A)
_TmnxCellPdnProfLastChanged_Type=TimeStamp
_TmnxCellPdnProfLastChanged_Object=MibTableColumn
tmnxCellPdnProfLastChanged=_TmnxCellPdnProfLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,3),_TmnxCellPdnProfLastChanged_Type())
tmnxCellPdnProfLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnProfLastChanged.setStatus(_A)
class _TmnxCellPdnProfDescription_Type(TItemDescription):defaultHexValue=''
_TmnxCellPdnProfDescription_Type.__name__=_Q
_TmnxCellPdnProfDescription_Object=MibTableColumn
tmnxCellPdnProfDescription=_TmnxCellPdnProfDescription_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,4),_TmnxCellPdnProfDescription_Type())
tmnxCellPdnProfDescription.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfDescription.setStatus(_A)
class _TmnxCellPdnProfApn_Type(TmnxCellularAccessPointName):defaultHexValue=''
_TmnxCellPdnProfApn_Type.__name__=_e
_TmnxCellPdnProfApn_Object=MibTableColumn
tmnxCellPdnProfApn=_TmnxCellPdnProfApn_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,5),_TmnxCellPdnProfApn_Type())
tmnxCellPdnProfApn.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfApn.setStatus(_A)
class _TmnxCellPdnProfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('pap',1),('chap',2)))
_TmnxCellPdnProfAuthType_Type.__name__=_D
_TmnxCellPdnProfAuthType_Object=MibTableColumn
tmnxCellPdnProfAuthType=_TmnxCellPdnProfAuthType_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,6),_TmnxCellPdnProfAuthType_Type())
tmnxCellPdnProfAuthType.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfAuthType.setStatus(_A)
class _TmnxCellPdnProfUsername_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxCellPdnProfUsername_Type.__name__=_M
_TmnxCellPdnProfUsername_Object=MibTableColumn
tmnxCellPdnProfUsername=_TmnxCellPdnProfUsername_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,7),_TmnxCellPdnProfUsername_Type())
tmnxCellPdnProfUsername.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfUsername.setStatus(_A)
class _TmnxCellPdnProfPassword_Type(TmnxAuthPassword):defaultHexValue=''
_TmnxCellPdnProfPassword_Type.__name__=_c
_TmnxCellPdnProfPassword_Object=MibTableColumn
tmnxCellPdnProfPassword=_TmnxCellPdnProfPassword_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,8),_TmnxCellPdnProfPassword_Type())
tmnxCellPdnProfPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfPassword.setStatus(_A)
class _TmnxCellPdnProfProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_TmnxCellPdnProfProtocol_Type.__name__=_D
_TmnxCellPdnProfProtocol_Object=MibTableColumn
tmnxCellPdnProfProtocol=_TmnxCellPdnProfProtocol_Object((1,3,6,1,4,1,6527,3,1,2,109,2,2,1,1,9),_TmnxCellPdnProfProtocol_Type())
tmnxCellPdnProfProtocol.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfProtocol.setStatus(_A)
_TmnxCellularPortConfigObjs_ObjectIdentity=ObjectIdentity
tmnxCellularPortConfigObjs=_TmnxCellularPortConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109,2,3))
_TmnxCellularSimCardTable_Object=MibTable
tmnxCellularSimCardTable=_TmnxCellularSimCardTable_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1))
if mibBuilder.loadTexts:tmnxCellularSimCardTable.setStatus(_A)
_TmnxCellularSimCardEntry_Object=MibTableRow
tmnxCellularSimCardEntry=_TmnxCellularSimCardEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1))
tmnxCellularSimCardEntry.setIndexNames((0,_H,_I),(0,_B,_f))
if mibBuilder.loadTexts:tmnxCellularSimCardEntry.setStatus(_A)
_TmnxCellSimCardId_Type=TmnxCellularSimCardNumber
_TmnxCellSimCardId_Object=MibTableColumn
tmnxCellSimCardId=_TmnxCellSimCardId_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1,1),_TmnxCellSimCardId_Type())
tmnxCellSimCardId.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxCellSimCardId.setStatus(_A)
_TmnxCellSimCardLastChanged_Type=TimeStamp
_TmnxCellSimCardLastChanged_Object=MibTableColumn
tmnxCellSimCardLastChanged=_TmnxCellSimCardLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1,2),_TmnxCellSimCardLastChanged_Type())
tmnxCellSimCardLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardLastChanged.setStatus(_A)
class _TmnxCellSimCardDescription_Type(TItemDescription):defaultHexValue=''
_TmnxCellSimCardDescription_Type.__name__=_Q
_TmnxCellSimCardDescription_Object=MibTableColumn
tmnxCellSimCardDescription=_TmnxCellSimCardDescription_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1,3),_TmnxCellSimCardDescription_Type())
tmnxCellSimCardDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellSimCardDescription.setStatus(_A)
class _TmnxCellSimCardPin_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,8))
_TmnxCellSimCardPin_Type.__name__=_Y
_TmnxCellSimCardPin_Object=MibTableColumn
tmnxCellSimCardPin=_TmnxCellSimCardPin_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1,4),_TmnxCellSimCardPin_Type())
tmnxCellSimCardPin.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellSimCardPin.setStatus(_A)
class _TmnxCellSimCardFailureDuration_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_TmnxCellSimCardFailureDuration_Type.__name__=_E
_TmnxCellSimCardFailureDuration_Object=MibTableColumn
tmnxCellSimCardFailureDuration=_TmnxCellSimCardFailureDuration_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1,5),_TmnxCellSimCardFailureDuration_Type())
tmnxCellSimCardFailureDuration.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellSimCardFailureDuration.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellSimCardFailureDuration.setUnits(_g)
class _TmnxCellSimCardPortStateSwitch_Type(TruthValue):defaultValue=1
_TmnxCellSimCardPortStateSwitch_Type.__name__=_O
_TmnxCellSimCardPortStateSwitch_Object=MibTableColumn
tmnxCellSimCardPortStateSwitch=_TmnxCellSimCardPortStateSwitch_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1,6),_TmnxCellSimCardPortStateSwitch_Type())
tmnxCellSimCardPortStateSwitch.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellSimCardPortStateSwitch.setStatus(_A)
class _TmnxCellSimCardBgpStateSwitch_Type(TruthValue):defaultValue=2
_TmnxCellSimCardBgpStateSwitch_Type.__name__=_O
_TmnxCellSimCardBgpStateSwitch_Object=MibTableColumn
tmnxCellSimCardBgpStateSwitch=_TmnxCellSimCardBgpStateSwitch_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,1,1,7),_TmnxCellSimCardBgpStateSwitch_Type())
tmnxCellSimCardBgpStateSwitch.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellSimCardBgpStateSwitch.setStatus(_A)
_TmnxCellularPdnTable_Object=MibTable
tmnxCellularPdnTable=_TmnxCellularPdnTable_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,2))
if mibBuilder.loadTexts:tmnxCellularPdnTable.setStatus(_A)
_TmnxCellularPdnEntry_Object=MibTableRow
tmnxCellularPdnEntry=_TmnxCellularPdnEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,2,1))
tmnxCellularPdnEntry.setIndexNames((0,_H,_I),(0,_B,_h))
if mibBuilder.loadTexts:tmnxCellularPdnEntry.setStatus(_A)
_TmnxCellPdnId_Type=TmnxCellularPdnId
_TmnxCellPdnId_Object=MibTableColumn
tmnxCellPdnId=_TmnxCellPdnId_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,2,1,1),_TmnxCellPdnId_Type())
tmnxCellPdnId.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxCellPdnId.setStatus(_A)
_TmnxCellPdnRowStatus_Type=RowStatus
_TmnxCellPdnRowStatus_Object=MibTableColumn
tmnxCellPdnRowStatus=_TmnxCellPdnRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,2,1,2),_TmnxCellPdnRowStatus_Type())
tmnxCellPdnRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnRowStatus.setStatus(_A)
_TmnxCellPdnLastChanged_Type=TimeStamp
_TmnxCellPdnLastChanged_Object=MibTableColumn
tmnxCellPdnLastChanged=_TmnxCellPdnLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,2,1,3),_TmnxCellPdnLastChanged_Type())
tmnxCellPdnLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnLastChanged.setStatus(_A)
class _TmnxCellPdnProfile_Type(TmnxCellularPdnProfileId):defaultValue=0
_TmnxCellPdnProfile_Type.__name__=_i
_TmnxCellPdnProfile_Object=MibTableColumn
tmnxCellPdnProfile=_TmnxCellPdnProfile_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,2,1,4),_TmnxCellPdnProfile_Type())
tmnxCellPdnProfile.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxCellPdnProfile.setStatus(_A)
_TmnxCellularPortTable_Object=MibTable
tmnxCellularPortTable=_TmnxCellularPortTable_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,3))
if mibBuilder.loadTexts:tmnxCellularPortTable.setStatus(_A)
_TmnxCellularPortEntry_Object=MibTableRow
tmnxCellularPortEntry=_TmnxCellularPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,3,1))
tmnxCellularPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:tmnxCellularPortEntry.setStatus(_A)
_TmnxCellPortLastChanged_Type=TimeStamp
_TmnxCellPortLastChanged_Object=MibTableColumn
tmnxCellPortLastChanged=_TmnxCellPortLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,3,1,1),_TmnxCellPortLastChanged_Type())
tmnxCellPortLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortLastChanged.setStatus(_A)
class _TmnxCellPortBand125MaxPowerLevel_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_TmnxCellPortBand125MaxPowerLevel_Type.__name__=_E
_TmnxCellPortBand125MaxPowerLevel_Object=MibTableColumn
tmnxCellPortBand125MaxPowerLevel=_TmnxCellPortBand125MaxPowerLevel_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,3,1,2),_TmnxCellPortBand125MaxPowerLevel_Type())
tmnxCellPortBand125MaxPowerLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellPortBand125MaxPowerLevel.setStatus(_A)
_TmnxCellularMdaTable_Object=MibTable
tmnxCellularMdaTable=_TmnxCellularMdaTable_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4))
if mibBuilder.loadTexts:tmnxCellularMdaTable.setStatus(_A)
_TmnxCellularMdaEntry_Object=MibTableRow
tmnxCellularMdaEntry=_TmnxCellularMdaEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1))
tmnxCellularMdaEntry.setIndexNames((0,_P,_Z),(0,_P,_a))
if mibBuilder.loadTexts:tmnxCellularMdaEntry.setStatus(_A)
_TmnxCellMdaLastChanged_Type=TimeStamp
_TmnxCellMdaLastChanged_Object=MibTableColumn
tmnxCellMdaLastChanged=_TmnxCellMdaLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,1),_TmnxCellMdaLastChanged_Type())
tmnxCellMdaLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaLastChanged.setStatus(_A)
class _TmnxCellMdaAdminActiveSim_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sim-1',1),('sim-2',2),('automatic',3)))
_TmnxCellMdaAdminActiveSim_Type.__name__=_D
_TmnxCellMdaAdminActiveSim_Object=MibTableColumn
tmnxCellMdaAdminActiveSim=_TmnxCellMdaAdminActiveSim_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,2),_TmnxCellMdaAdminActiveSim_Type())
tmnxCellMdaAdminActiveSim.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellMdaAdminActiveSim.setStatus(_A)
class _TmnxCellMdaDownResetInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_TmnxCellMdaDownResetInterval_Type.__name__=_E
_TmnxCellMdaDownResetInterval_Object=MibTableColumn
tmnxCellMdaDownResetInterval=_TmnxCellMdaDownResetInterval_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,3),_TmnxCellMdaDownResetInterval_Type())
tmnxCellMdaDownResetInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellMdaDownResetInterval.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellMdaDownResetInterval.setUnits(_g)
class _TmnxCellMdaDownResetCriteria_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*(('port',0),('bgp',1)))
_TmnxCellMdaDownResetCriteria_Type.__name__='Bits'
_TmnxCellMdaDownResetCriteria_Object=MibTableColumn
tmnxCellMdaDownResetCriteria=_TmnxCellMdaDownResetCriteria_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,4),_TmnxCellMdaDownResetCriteria_Type())
tmnxCellMdaDownResetCriteria.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellMdaDownResetCriteria.setStatus(_A)
_TmnxCellMdaDownResetPending_Type=TruthValue
_TmnxCellMdaDownResetPending_Object=MibTableColumn
tmnxCellMdaDownResetPending=_TmnxCellMdaDownResetPending_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,5),_TmnxCellMdaDownResetPending_Type())
tmnxCellMdaDownResetPending.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaDownResetPending.setStatus(_A)
class _TmnxCellMdaDownResetTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_TmnxCellMdaDownResetTime_Type.__name__=_E
_TmnxCellMdaDownResetTime_Object=MibTableColumn
tmnxCellMdaDownResetTime=_TmnxCellMdaDownResetTime_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,6),_TmnxCellMdaDownResetTime_Type())
tmnxCellMdaDownResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaDownResetTime.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellMdaDownResetTime.setUnits(_j)
class _TmnxCellMdaPreferredSim_Type(TmnxCellularSimCardNumber):defaultValue=1
_TmnxCellMdaPreferredSim_Type.__name__=_k
_TmnxCellMdaPreferredSim_Object=MibTableColumn
tmnxCellMdaPreferredSim=_TmnxCellMdaPreferredSim_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,7),_TmnxCellMdaPreferredSim_Type())
tmnxCellMdaPreferredSim.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellMdaPreferredSim.setStatus(_A)
_TmnxCellMdaOperActiveSim_Type=TmnxCellularSimCardNumber
_TmnxCellMdaOperActiveSim_Object=MibTableColumn
tmnxCellMdaOperActiveSim=_TmnxCellMdaOperActiveSim_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,8),_TmnxCellMdaOperActiveSim_Type())
tmnxCellMdaOperActiveSim.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaOperActiveSim.setStatus(_A)
_TmnxCellMdaSimCardSwitchPending_Type=TruthValue
_TmnxCellMdaSimCardSwitchPending_Object=MibTableColumn
tmnxCellMdaSimCardSwitchPending=_TmnxCellMdaSimCardSwitchPending_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,9),_TmnxCellMdaSimCardSwitchPending_Type())
tmnxCellMdaSimCardSwitchPending.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaSimCardSwitchPending.setStatus(_A)
class _TmnxCellMdaSimCardSwitchTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_TmnxCellMdaSimCardSwitchTime_Type.__name__=_E
_TmnxCellMdaSimCardSwitchTime_Object=MibTableColumn
tmnxCellMdaSimCardSwitchTime=_TmnxCellMdaSimCardSwitchTime_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,10),_TmnxCellMdaSimCardSwitchTime_Type())
tmnxCellMdaSimCardSwitchTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaSimCardSwitchTime.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellMdaSimCardSwitchTime.setUnits(_j)
_TmnxCellMdaSimCardLastSwitchTime_Type=TimeStamp
_TmnxCellMdaSimCardLastSwitchTime_Object=MibTableColumn
tmnxCellMdaSimCardLastSwitchTime=_TmnxCellMdaSimCardLastSwitchTime_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,11),_TmnxCellMdaSimCardLastSwitchTime_Type())
tmnxCellMdaSimCardLastSwitchTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaSimCardLastSwitchTime.setStatus(_A)
class _TmnxCellMdaSimLastSwitchReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_S,0),('manual-configuration',1),('forced-switch',2),(_l,3),(_m,4)))
_TmnxCellMdaSimLastSwitchReason_Type.__name__=_D
_TmnxCellMdaSimLastSwitchReason_Object=MibTableColumn
tmnxCellMdaSimLastSwitchReason=_TmnxCellMdaSimLastSwitchReason_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,12),_TmnxCellMdaSimLastSwitchReason_Type())
tmnxCellMdaSimLastSwitchReason.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaSimLastSwitchReason.setStatus(_A)
_TmnxCellMdaSpecFirmwareVersion_Type=DisplayString
_TmnxCellMdaSpecFirmwareVersion_Object=MibTableColumn
tmnxCellMdaSpecFirmwareVersion=_TmnxCellMdaSpecFirmwareVersion_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,13),_TmnxCellMdaSpecFirmwareVersion_Type())
tmnxCellMdaSpecFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellMdaSpecFirmwareVersion.setStatus(_A)
class _TmnxCellMdaMaxTxPower_Type(Integer32):defaultValue=23;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_TmnxCellMdaMaxTxPower_Type.__name__=_D
_TmnxCellMdaMaxTxPower_Object=MibTableColumn
tmnxCellMdaMaxTxPower=_TmnxCellMdaMaxTxPower_Object((1,3,6,1,4,1,6527,3,1,2,109,2,3,4,1,14),_TmnxCellMdaMaxTxPower_Type())
tmnxCellMdaMaxTxPower.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxCellMdaMaxTxPower.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellMdaMaxTxPower.setUnits(_N)
_TmnxCellularStatusObjs_ObjectIdentity=ObjectIdentity
tmnxCellularStatusObjs=_TmnxCellularStatusObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109,3))
_TmnxCellularPortStatusObjs_ObjectIdentity=ObjectIdentity
tmnxCellularPortStatusObjs=_TmnxCellularPortStatusObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109,3,1))
_TmnxCellularPortStatusTable_Object=MibTable
tmnxCellularPortStatusTable=_TmnxCellularPortStatusTable_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1))
if mibBuilder.loadTexts:tmnxCellularPortStatusTable.setStatus(_A)
_TmnxCellularPortStatusEntry_Object=MibTableRow
tmnxCellularPortStatusEntry=_TmnxCellularPortStatusEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1))
tmnxCellularPortStatusEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:tmnxCellularPortStatusEntry.setStatus(_A)
_TmnxCellPortImei_Type=TmnxCellularImei
_TmnxCellPortImei_Object=MibTableColumn
tmnxCellPortImei=_TmnxCellPortImei_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,1),_TmnxCellPortImei_Type())
tmnxCellPortImei.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortImei.setStatus(_A)
class _TmnxCellPortRegistrationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('not-registered',0),('registered-home',1),('searching',2),('denied',3),('no-network',4),('registered-roaming',5),('sms-only-home',6),('sms-only-roaming',7),('emergency-only',8),('csfb-not-preferred-home',9),('csfb-not-preferred-roaming',10)))
_TmnxCellPortRegistrationStatus_Type.__name__=_D
_TmnxCellPortRegistrationStatus_Object=MibTableColumn
tmnxCellPortRegistrationStatus=_TmnxCellPortRegistrationStatus_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,2),_TmnxCellPortRegistrationStatus_Type())
tmnxCellPortRegistrationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortRegistrationStatus.setStatus(_A)
class _TmnxCellPortWirelessTechnology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),('lte',1),('wcdma',2),('gsm',3)))
_TmnxCellPortWirelessTechnology_Type.__name__=_D
_TmnxCellPortWirelessTechnology_Object=MibTableColumn
tmnxCellPortWirelessTechnology=_TmnxCellPortWirelessTechnology_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,3),_TmnxCellPortWirelessTechnology_Type())
tmnxCellPortWirelessTechnology.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortWirelessTechnology.setStatus(_A)
_TmnxCellPortFrequencyBand_Type=Unsigned32
_TmnxCellPortFrequencyBand_Object=MibTableColumn
tmnxCellPortFrequencyBand=_TmnxCellPortFrequencyBand_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,4),_TmnxCellPortFrequencyBand_Type())
tmnxCellPortFrequencyBand.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortFrequencyBand.setStatus(_A)
_TmnxCellPortChannelNumber_Type=TmnxCellularChannelNumber
_TmnxCellPortChannelNumber_Object=MibTableColumn
tmnxCellPortChannelNumber=_TmnxCellPortChannelNumber_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,5),_TmnxCellPortChannelNumber_Type())
tmnxCellPortChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortChannelNumber.setStatus(_A)
class _TmnxCellPortAreaCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_TmnxCellPortAreaCode_Type.__name__=_M
_TmnxCellPortAreaCode_Object=MibTableColumn
tmnxCellPortAreaCode=_TmnxCellPortAreaCode_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,6),_TmnxCellPortAreaCode_Type())
tmnxCellPortAreaCode.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortAreaCode.setStatus(_A)
class _TmnxCellPortCellIdentity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_TmnxCellPortCellIdentity_Type.__name__=_M
_TmnxCellPortCellIdentity_Object=MibTableColumn
tmnxCellPortCellIdentity=_TmnxCellPortCellIdentity_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,7),_TmnxCellPortCellIdentity_Type())
tmnxCellPortCellIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortCellIdentity.setStatus(_A)
class _TmnxCellPortRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-113,-51),ValueRangeConstraint(0,0))
_TmnxCellPortRssi_Type.__name__=_D
_TmnxCellPortRssi_Object=MibTableColumn
tmnxCellPortRssi=_TmnxCellPortRssi_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,8),_TmnxCellPortRssi_Type())
tmnxCellPortRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortRssi.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellPortRssi.setUnits(_N)
class _TmnxCellPortRsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,-44),ValueRangeConstraint(0,0))
_TmnxCellPortRsrp_Type.__name__=_D
_TmnxCellPortRsrp_Object=MibTableColumn
tmnxCellPortRsrp=_TmnxCellPortRsrp_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,9),_TmnxCellPortRsrp_Type())
tmnxCellPortRsrp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortRsrp.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellPortRsrp.setUnits(_N)
class _TmnxCellPortRscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-120,-25),ValueRangeConstraint(0,0))
_TmnxCellPortRscp_Type.__name__=_D
_TmnxCellPortRscp_Object=MibTableColumn
tmnxCellPortRscp=_TmnxCellPortRscp_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,1,1,10),_TmnxCellPortRscp_Type())
tmnxCellPortRscp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortRscp.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellPortRscp.setUnits(_N)
_TmnxCellularSimCardStatusTable_Object=MibTable
tmnxCellularSimCardStatusTable=_TmnxCellularSimCardStatusTable_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3))
if mibBuilder.loadTexts:tmnxCellularSimCardStatusTable.setStatus(_A)
_TmnxCellularSimCardStatusEntry_Object=MibTableRow
tmnxCellularSimCardStatusEntry=_TmnxCellularSimCardStatusEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1))
if mibBuilder.loadTexts:tmnxCellularSimCardStatusEntry.setStatus(_A)
_TmnxCellSimCardEquipped_Type=TruthValue
_TmnxCellSimCardEquipped_Object=MibTableColumn
tmnxCellSimCardEquipped=_TmnxCellSimCardEquipped_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,1),_TmnxCellSimCardEquipped_Type())
tmnxCellSimCardEquipped.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardEquipped.setStatus(_A)
_TmnxCellSimCardIccid_Type=TmnxCellularSimCardIccid
_TmnxCellSimCardIccid_Object=MibTableColumn
tmnxCellSimCardIccid=_TmnxCellSimCardIccid_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,2),_TmnxCellSimCardIccid_Type())
tmnxCellSimCardIccid.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardIccid.setStatus(_A)
_TmnxCellSimCardImsi_Type=TmnxCellularImsi
_TmnxCellSimCardImsi_Object=MibTableColumn
tmnxCellSimCardImsi=_TmnxCellSimCardImsi_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,3),_TmnxCellSimCardImsi_Type())
tmnxCellSimCardImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardImsi.setStatus(_A)
_TmnxCellSimCardLocked_Type=TruthValue
_TmnxCellSimCardLocked_Object=MibTableColumn
tmnxCellSimCardLocked=_TmnxCellSimCardLocked_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,4),_TmnxCellSimCardLocked_Type())
tmnxCellSimCardLocked.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardLocked.setStatus(_A)
class _TmnxCellSimCardPinStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('waiting-for-pin',1),('waiting-for-puk',2),('ready',3)))
_TmnxCellSimCardPinStatus_Type.__name__=_D
_TmnxCellSimCardPinStatus_Object=MibTableColumn
tmnxCellSimCardPinStatus=_TmnxCellSimCardPinStatus_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,5),_TmnxCellSimCardPinStatus_Type())
tmnxCellSimCardPinStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardPinStatus.setStatus(_A)
_TmnxCellSimCardPinRetries_Type=Unsigned32
_TmnxCellSimCardPinRetries_Object=MibTableColumn
tmnxCellSimCardPinRetries=_TmnxCellSimCardPinRetries_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,6),_TmnxCellSimCardPinRetries_Type())
tmnxCellSimCardPinRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardPinRetries.setStatus(_A)
_TmnxCellSimCardPukRetries_Type=Unsigned32
_TmnxCellSimCardPukRetries_Object=MibTableColumn
tmnxCellSimCardPukRetries=_TmnxCellSimCardPukRetries_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,7),_TmnxCellSimCardPukRetries_Type())
tmnxCellSimCardPukRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardPukRetries.setStatus(_A)
_TmnxCellSimCardFirmwareVersion_Type=DisplayString
_TmnxCellSimCardFirmwareVersion_Object=MibTableColumn
tmnxCellSimCardFirmwareVersion=_TmnxCellSimCardFirmwareVersion_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,3,1,8),_TmnxCellSimCardFirmwareVersion_Type())
tmnxCellSimCardFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellSimCardFirmwareVersion.setStatus(_A)
_TmnxCellularPdnStatusTable_Object=MibTable
tmnxCellularPdnStatusTable=_TmnxCellularPdnStatusTable_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4))
if mibBuilder.loadTexts:tmnxCellularPdnStatusTable.setStatus(_A)
_TmnxCellularPdnStatusEntry_Object=MibTableRow
tmnxCellularPdnStatusEntry=_TmnxCellularPdnStatusEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1))
if mibBuilder.loadTexts:tmnxCellularPdnStatusEntry.setStatus(_A)
class _TmnxCellPdnConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notConnected',0),('connected',1)))
_TmnxCellPdnConnectionState_Type.__name__=_D
_TmnxCellPdnConnectionState_Object=MibTableColumn
tmnxCellPdnConnectionState=_TmnxCellPdnConnectionState_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,1),_TmnxCellPdnConnectionState_Type())
tmnxCellPdnConnectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnConnectionState.setStatus(_A)
_TmnxCellPdnIpAddrType_Type=InetAddressType
_TmnxCellPdnIpAddrType_Object=MibTableColumn
tmnxCellPdnIpAddrType=_TmnxCellPdnIpAddrType_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,2),_TmnxCellPdnIpAddrType_Type())
tmnxCellPdnIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnIpAddrType.setStatus(_A)
class _TmnxCellPdnIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxCellPdnIpAddress_Type.__name__=_L
_TmnxCellPdnIpAddress_Object=MibTableColumn
tmnxCellPdnIpAddress=_TmnxCellPdnIpAddress_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,3),_TmnxCellPdnIpAddress_Type())
tmnxCellPdnIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnIpAddress.setStatus(_A)
_TmnxCellPdnPrimaryDnsAddrType_Type=InetAddressType
_TmnxCellPdnPrimaryDnsAddrType_Object=MibTableColumn
tmnxCellPdnPrimaryDnsAddrType=_TmnxCellPdnPrimaryDnsAddrType_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,4),_TmnxCellPdnPrimaryDnsAddrType_Type())
tmnxCellPdnPrimaryDnsAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnPrimaryDnsAddrType.setStatus(_A)
class _TmnxCellPdnPrimaryDnsAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxCellPdnPrimaryDnsAddress_Type.__name__=_L
_TmnxCellPdnPrimaryDnsAddress_Object=MibTableColumn
tmnxCellPdnPrimaryDnsAddress=_TmnxCellPdnPrimaryDnsAddress_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,5),_TmnxCellPdnPrimaryDnsAddress_Type())
tmnxCellPdnPrimaryDnsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnPrimaryDnsAddress.setStatus(_A)
_TmnxCellPdnSecondaryDnsAddrType_Type=InetAddressType
_TmnxCellPdnSecondaryDnsAddrType_Object=MibTableColumn
tmnxCellPdnSecondaryDnsAddrType=_TmnxCellPdnSecondaryDnsAddrType_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,6),_TmnxCellPdnSecondaryDnsAddrType_Type())
tmnxCellPdnSecondaryDnsAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnSecondaryDnsAddrType.setStatus(_A)
class _TmnxCellPdnSecondaryDnsAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxCellPdnSecondaryDnsAddress_Type.__name__=_L
_TmnxCellPdnSecondaryDnsAddress_Object=MibTableColumn
tmnxCellPdnSecondaryDnsAddress=_TmnxCellPdnSecondaryDnsAddress_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,7),_TmnxCellPdnSecondaryDnsAddress_Type())
tmnxCellPdnSecondaryDnsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnSecondaryDnsAddress.setStatus(_A)
_TmnxCellPdnApn_Type=TmnxCellularAccessPointName
_TmnxCellPdnApn_Object=MibTableColumn
tmnxCellPdnApn=_TmnxCellPdnApn_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,8),_TmnxCellPdnApn_Type())
tmnxCellPdnApn.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnApn.setStatus(_A)
_TmnxCellPdnMtu_Type=Unsigned32
_TmnxCellPdnMtu_Object=MibTableColumn
tmnxCellPdnMtu=_TmnxCellPdnMtu_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,4,1,9),_TmnxCellPdnMtu_Type())
tmnxCellPdnMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPdnMtu.setStatus(_A)
if mibBuilder.loadTexts:tmnxCellPdnMtu.setUnits('bytes')
_TmnxCellularPortBearerTable_Object=MibTable
tmnxCellularPortBearerTable=_TmnxCellularPortBearerTable_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5))
if mibBuilder.loadTexts:tmnxCellularPortBearerTable.setStatus(_A)
_TmnxCellularPortBearerEntry_Object=MibTableRow
tmnxCellularPortBearerEntry=_TmnxCellularPortBearerEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1))
tmnxCellularPortBearerEntry.setIndexNames((0,_H,_I),(0,_B,_J))
if mibBuilder.loadTexts:tmnxCellularPortBearerEntry.setStatus(_A)
class _TmnxCellPortBearerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TmnxCellPortBearerId_Type.__name__=_E
_TmnxCellPortBearerId_Object=MibTableColumn
tmnxCellPortBearerId=_TmnxCellPortBearerId_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1,1),_TmnxCellPortBearerId_Type())
tmnxCellPortBearerId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortBearerId.setStatus(_A)
class _TmnxCellPortBearerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('dedicated',2)))
_TmnxCellPortBearerType_Type.__name__=_D
_TmnxCellPortBearerType_Object=MibTableColumn
tmnxCellPortBearerType=_TmnxCellPortBearerType_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1,2),_TmnxCellPortBearerType_Type())
tmnxCellPortBearerType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortBearerType.setStatus(_A)
class _TmnxCellPortBearerQci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_TmnxCellPortBearerQci_Type.__name__=_E
_TmnxCellPortBearerQci_Object=MibTableColumn
tmnxCellPortBearerQci=_TmnxCellPortBearerQci_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1,3),_TmnxCellPortBearerQci_Type())
tmnxCellPortBearerQci.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortBearerQci.setStatus(_A)
_TmnxCellPortBearerUlGbr_Type=TmnxCellularBearerRate
_TmnxCellPortBearerUlGbr_Object=MibTableColumn
tmnxCellPortBearerUlGbr=_TmnxCellPortBearerUlGbr_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1,4),_TmnxCellPortBearerUlGbr_Type())
tmnxCellPortBearerUlGbr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortBearerUlGbr.setStatus(_A)
_TmnxCellPortBearerUlMbr_Type=TmnxCellularBearerRate
_TmnxCellPortBearerUlMbr_Object=MibTableColumn
tmnxCellPortBearerUlMbr=_TmnxCellPortBearerUlMbr_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1,5),_TmnxCellPortBearerUlMbr_Type())
tmnxCellPortBearerUlMbr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortBearerUlMbr.setStatus(_A)
_TmnxCellPortBearerDlGbr_Type=TmnxCellularBearerRate
_TmnxCellPortBearerDlGbr_Object=MibTableColumn
tmnxCellPortBearerDlGbr=_TmnxCellPortBearerDlGbr_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1,6),_TmnxCellPortBearerDlGbr_Type())
tmnxCellPortBearerDlGbr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortBearerDlGbr.setStatus(_A)
_TmnxCellPortBearerDlMbr_Type=TmnxCellularBearerRate
_TmnxCellPortBearerDlMbr_Object=MibTableColumn
tmnxCellPortBearerDlMbr=_TmnxCellPortBearerDlMbr_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,5,1,7),_TmnxCellPortBearerDlMbr_Type())
tmnxCellPortBearerDlMbr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortBearerDlMbr.setStatus(_A)
_TmnxCellularPortTftTable_Object=MibTable
tmnxCellularPortTftTable=_TmnxCellularPortTftTable_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,6))
if mibBuilder.loadTexts:tmnxCellularPortTftTable.setStatus(_A)
_TmnxCellularPortTftEntry_Object=MibTableRow
tmnxCellularPortTftEntry=_TmnxCellularPortTftEntry_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,6,1))
tmnxCellularPortTftEntry.setIndexNames((0,_H,_I),(0,_B,_J),(0,_B,_T))
if mibBuilder.loadTexts:tmnxCellularPortTftEntry.setStatus(_A)
class _TmnxCellPortTftPacketFilterId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_TmnxCellPortTftPacketFilterId_Type.__name__=_E
_TmnxCellPortTftPacketFilterId_Object=MibTableColumn
tmnxCellPortTftPacketFilterId=_TmnxCellPortTftPacketFilterId_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,6,1,1),_TmnxCellPortTftPacketFilterId_Type())
tmnxCellPortTftPacketFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortTftPacketFilterId.setStatus(_A)
class _TmnxCellPortTftEvalPrecedence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TmnxCellPortTftEvalPrecedence_Type.__name__=_E
_TmnxCellPortTftEvalPrecedence_Object=MibTableColumn
tmnxCellPortTftEvalPrecedence=_TmnxCellPortTftEvalPrecedence_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,6,1,2),_TmnxCellPortTftEvalPrecedence_Type())
tmnxCellPortTftEvalPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortTftEvalPrecedence.setStatus(_A)
class _TmnxCellPortTftDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('pre-release-7',0),('uplink',1),('downlink',2),('bidirectional',3)))
_TmnxCellPortTftDirection_Type.__name__=_D
_TmnxCellPortTftDirection_Object=MibTableColumn
tmnxCellPortTftDirection=_TmnxCellPortTftDirection_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,6,1,3),_TmnxCellPortTftDirection_Type())
tmnxCellPortTftDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortTftDirection.setStatus(_A)
class _TmnxCellPortTftTos_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TmnxCellPortTftTos_Type.__name__=_E
_TmnxCellPortTftTos_Object=MibTableColumn
tmnxCellPortTftTos=_TmnxCellPortTftTos_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,6,1,4),_TmnxCellPortTftTos_Type())
tmnxCellPortTftTos.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortTftTos.setStatus(_A)
class _TmnxCellPortTftTosMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TmnxCellPortTftTosMask_Type.__name__=_E
_TmnxCellPortTftTosMask_Object=MibTableColumn
tmnxCellPortTftTosMask=_TmnxCellPortTftTosMask_Object((1,3,6,1,4,1,6527,3,1,2,109,3,1,6,1,5),_TmnxCellPortTftTosMask_Type())
tmnxCellPortTftTosMask.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxCellPortTftTosMask.setStatus(_A)
_TmnxCellularNotifyObjects_ObjectIdentity=ObjectIdentity
tmnxCellularNotifyObjects=_TmnxCellularNotifyObjects_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,109,4))
_TmnxCellularNotifyPdnId_Type=TmnxCellularPdnId
_TmnxCellularNotifyPdnId_Object=MibScalar
tmnxCellularNotifyPdnId=_TmnxCellularNotifyPdnId_Object((1,3,6,1,4,1,6527,3,1,2,109,4,1),_TmnxCellularNotifyPdnId_Type())
tmnxCellularNotifyPdnId.setMaxAccess(_n)
if mibBuilder.loadTexts:tmnxCellularNotifyPdnId.setStatus(_A)
class _TmnxCellMdaNoServiceResetReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_TmnxCellMdaNoServiceResetReason_Type.__name__=_D
_TmnxCellMdaNoServiceResetReason_Object=MibScalar
tmnxCellMdaNoServiceResetReason=_TmnxCellMdaNoServiceResetReason_Object((1,3,6,1,4,1,6527,3,1,2,109,4,2),_TmnxCellMdaNoServiceResetReason_Type())
tmnxCellMdaNoServiceResetReason.setMaxAccess(_n)
if mibBuilder.loadTexts:tmnxCellMdaNoServiceResetReason.setStatus(_A)
_TmnxCellularNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxCellularNotifyPrefix=_TmnxCellularNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,109))
_TmnxCellularNotifications_ObjectIdentity=ObjectIdentity
tmnxCellularNotifications=_TmnxCellularNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,109,0))
tmnxCellularSimCardEntry.registerAugmentions((_B,_o))
tmnxCellularSimCardStatusEntry.setIndexNames(*tmnxCellularSimCardEntry.getIndexNames())
tmnxCellularPdnEntry.registerAugmentions((_B,_p))
tmnxCellularPdnStatusEntry.setIndexNames(*tmnxCellularPdnEntry.getIndexNames())
tmnxCellularConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,109,2,1,1))
tmnxCellularConfigGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:tmnxCellularConfigGroup.setStatus(_A)
tmnxCellularStatusGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,109,2,1,2))
tmnxCellularStatusGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:tmnxCellularStatusGroup.setStatus(_A)
tmnxCellularV16v0ConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,109,2,2,1))
tmnxCellularV16v0ConfigGroup.setObjects(*((_B,_AZ),(_B,_U),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:tmnxCellularV16v0ConfigGroup.setStatus(_A)
tmnxCellularV16v0StatusGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,109,2,2,2))
tmnxCellularV16v0StatusGroup.setObjects(*((_B,_J),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_T),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_V),(_B,_At),(_B,_Au),(_B,_Av),(_B,_W)))
if mibBuilder.loadTexts:tmnxCellularV16v0StatusGroup.setStatus(_A)
tmnxCellularNotifyObjsGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,109,2,2,3))
tmnxCellularNotifyObjsGroup.setObjects(*((_B,_K),(_B,_X)))
if mibBuilder.loadTexts:tmnxCellularNotifyObjsGroup.setStatus(_A)
tmnxCellularV19ConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,109,2,3,1))
tmnxCellularV19ConfigGroup.setObjects((_B,_Aw))
if mibBuilder.loadTexts:tmnxCellularV19ConfigGroup.setStatus(_A)
tmnxCellularV20ConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,109,2,4,1))
tmnxCellularV20ConfigGroup.setObjects(*((_B,_Ax),(_B,_Ay)))
if mibBuilder.loadTexts:tmnxCellularV20ConfigGroup.setStatus(_A)
tmnxCellularBearerCreated=NotificationType((1,3,6,1,4,1,6527,3,1,3,109,0,1))
tmnxCellularBearerCreated.setObjects(*((_B,_K),(_B,_J)))
if mibBuilder.loadTexts:tmnxCellularBearerCreated.setStatus(_A)
tmnxCellularBearerDeleted=NotificationType((1,3,6,1,4,1,6527,3,1,3,109,0,2))
tmnxCellularBearerDeleted.setObjects(*((_B,_K),(_B,_J)))
if mibBuilder.loadTexts:tmnxCellularBearerDeleted.setStatus(_A)
tmnxCellularBearerModified=NotificationType((1,3,6,1,4,1,6527,3,1,3,109,0,3))
tmnxCellularBearerModified.setObjects(*((_B,_K),(_B,_J)))
if mibBuilder.loadTexts:tmnxCellularBearerModified.setStatus(_A)
tmnxCellularNoServiceReset=NotificationType((1,3,6,1,4,1,6527,3,1,3,109,0,4))
tmnxCellularNoServiceReset.setObjects(*((_H,_b),(_B,_X)))
if mibBuilder.loadTexts:tmnxCellularNoServiceReset.setStatus(_A)
tmnxCellularActiveSimChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,109,0,5))
tmnxCellularActiveSimChange.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:tmnxCellularActiveSimChange.setStatus(_A)
tmnxCellNotificationV16v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,109,2,2,4))
tmnxCellNotificationV16v0Group.setObjects(*((_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:tmnxCellNotificationV16v0Group.setStatus(_A)
tmnxCellularCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,109,1,1))
tmnxCellularCompliance.setObjects(*((_B,_B3),(_B,_B4)))
if mibBuilder.loadTexts:tmnxCellularCompliance.setStatus(_A)
tmnxCellularComplianceV16v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,109,1,2))
tmnxCellularComplianceV16v0.setObjects(*((_B,_B5),(_B,_B6),(_B,_B7)))
if mibBuilder.loadTexts:tmnxCellularComplianceV16v0.setStatus(_A)
tmnxCellularComplianceV19=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,109,1,3))
tmnxCellularComplianceV19.setObjects((_B,_B8))
if mibBuilder.loadTexts:tmnxCellularComplianceV19.setStatus(_A)
tmnxCellularComplianceV20=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,109,1,4))
tmnxCellularComplianceV20.setObjects((_B,_B9))
if mibBuilder.loadTexts:tmnxCellularComplianceV20.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_i:TmnxCellularPdnProfileId,_e:TmnxCellularAccessPointName,'TmnxCellularImei':TmnxCellularImei,_k:TmnxCellularSimCardNumber,'TmnxCellularSimCardIccid':TmnxCellularSimCardIccid,'TmnxCellularImsi':TmnxCellularImsi,'TmnxCellularPdnId':TmnxCellularPdnId,'TmnxCellularChannelNumber':TmnxCellularChannelNumber,'TmnxCellularBearerRate':TmnxCellularBearerRate,'timetraCellularMIBModule':timetraCellularMIBModule,'tmnxCellularConformance':tmnxCellularConformance,'tmnxCellularCompliances':tmnxCellularCompliances,'tmnxCellularCompliance':tmnxCellularCompliance,'tmnxCellularComplianceV16v0':tmnxCellularComplianceV16v0,'tmnxCellularComplianceV19':tmnxCellularComplianceV19,'tmnxCellularComplianceV20':tmnxCellularComplianceV20,'tmnxCellularGroups':tmnxCellularGroups,'tmnxCellularV15v0Groups':tmnxCellularV15v0Groups,_B3:tmnxCellularConfigGroup,_B4:tmnxCellularStatusGroup,'tmnxCellularV16v0Groups':tmnxCellularV16v0Groups,_B5:tmnxCellularV16v0ConfigGroup,_B6:tmnxCellularV16v0StatusGroup,'tmnxCellularNotifyObjsGroup':tmnxCellularNotifyObjsGroup,_B7:tmnxCellNotificationV16v0Group,'tmnxCellularV19Groups':tmnxCellularV19Groups,_B8:tmnxCellularV19ConfigGroup,'tmnxCellularV20Groups':tmnxCellularV20Groups,_B9:tmnxCellularV20ConfigGroup,'tmnxCellularObjs':tmnxCellularObjs,'tmnxCellularConfigObjs':tmnxCellularConfigObjs,'tmnxCellularConfigTimestamps':tmnxCellularConfigTimestamps,_q:tmnxCellPdnProfileTblLastChanged,_y:tmnxCellSimCardTableLastChanged,_A2:tmnxCellPdnTblLastChanged,_A6:tmnxCellPortTblLastChanged,'tmnxCellularSystemConfigObjs':tmnxCellularSystemConfigObjs,'tmnxCellularPdnProfileTable':tmnxCellularPdnProfileTable,'tmnxCellPdnProfileEntry':tmnxCellPdnProfileEntry,_d:tmnxCellPdnProfileId,_r:tmnxCellPdnProfRowStatus,_s:tmnxCellPdnProfLastChanged,_t:tmnxCellPdnProfDescription,_u:tmnxCellPdnProfApn,_v:tmnxCellPdnProfAuthType,_w:tmnxCellPdnProfUsername,_x:tmnxCellPdnProfPassword,_Aw:tmnxCellPdnProfProtocol,'tmnxCellularPortConfigObjs':tmnxCellularPortConfigObjs,'tmnxCellularSimCardTable':tmnxCellularSimCardTable,'tmnxCellularSimCardEntry':tmnxCellularSimCardEntry,_f:tmnxCellSimCardId,_z:tmnxCellSimCardLastChanged,_A0:tmnxCellSimCardDescription,_A1:tmnxCellSimCardPin,_Ae:tmnxCellSimCardFailureDuration,_Af:tmnxCellSimCardPortStateSwitch,_Ag:tmnxCellSimCardBgpStateSwitch,'tmnxCellularPdnTable':tmnxCellularPdnTable,'tmnxCellularPdnEntry':tmnxCellularPdnEntry,_h:tmnxCellPdnId,_A3:tmnxCellPdnRowStatus,_A4:tmnxCellPdnLastChanged,_A5:tmnxCellPdnProfile,'tmnxCellularPortTable':tmnxCellularPortTable,'tmnxCellularPortEntry':tmnxCellularPortEntry,_A7:tmnxCellPortLastChanged,_A8:tmnxCellPortBand125MaxPowerLevel,'tmnxCellularMdaTable':tmnxCellularMdaTable,'tmnxCellularMdaEntry':tmnxCellularMdaEntry,_AZ:tmnxCellMdaLastChanged,_U:tmnxCellMdaAdminActiveSim,_Aa:tmnxCellMdaDownResetInterval,_Ab:tmnxCellMdaDownResetCriteria,_Ac:tmnxCellMdaDownResetPending,_Ad:tmnxCellMdaDownResetTime,_As:tmnxCellMdaPreferredSim,_V:tmnxCellMdaOperActiveSim,_At:tmnxCellMdaSimCardSwitchPending,_Au:tmnxCellMdaSimCardSwitchTime,_Av:tmnxCellMdaSimCardLastSwitchTime,_W:tmnxCellMdaSimLastSwitchReason,_Ax:tmnxCellMdaSpecFirmwareVersion,_Ay:tmnxCellMdaMaxTxPower,'tmnxCellularStatusObjs':tmnxCellularStatusObjs,'tmnxCellularPortStatusObjs':tmnxCellularPortStatusObjs,'tmnxCellularPortStatusTable':tmnxCellularPortStatusTable,'tmnxCellularPortStatusEntry':tmnxCellularPortStatusEntry,_A9:tmnxCellPortImei,_AA:tmnxCellPortRegistrationStatus,_AB:tmnxCellPortWirelessTechnology,_AC:tmnxCellPortFrequencyBand,_AD:tmnxCellPortChannelNumber,_AE:tmnxCellPortAreaCode,_AF:tmnxCellPortCellIdentity,_AG:tmnxCellPortRssi,_AH:tmnxCellPortRsrp,_AI:tmnxCellPortRscp,'tmnxCellularSimCardStatusTable':tmnxCellularSimCardStatusTable,_o:tmnxCellularSimCardStatusEntry,_AJ:tmnxCellSimCardEquipped,_AK:tmnxCellSimCardIccid,_AL:tmnxCellSimCardImsi,_AM:tmnxCellSimCardLocked,_AN:tmnxCellSimCardPinStatus,_AO:tmnxCellSimCardPinRetries,_AP:tmnxCellSimCardPukRetries,_Ar:tmnxCellSimCardFirmwareVersion,'tmnxCellularPdnStatusTable':tmnxCellularPdnStatusTable,_p:tmnxCellularPdnStatusEntry,_AQ:tmnxCellPdnConnectionState,_AR:tmnxCellPdnIpAddrType,_AS:tmnxCellPdnIpAddress,_AT:tmnxCellPdnPrimaryDnsAddrType,_AU:tmnxCellPdnPrimaryDnsAddress,_AV:tmnxCellPdnSecondaryDnsAddrType,_AW:tmnxCellPdnSecondaryDnsAddress,_AX:tmnxCellPdnApn,_AY:tmnxCellPdnMtu,'tmnxCellularPortBearerTable':tmnxCellularPortBearerTable,'tmnxCellularPortBearerEntry':tmnxCellularPortBearerEntry,_J:tmnxCellPortBearerId,_Ah:tmnxCellPortBearerType,_Ai:tmnxCellPortBearerQci,_Aj:tmnxCellPortBearerUlGbr,_Ak:tmnxCellPortBearerUlMbr,_Al:tmnxCellPortBearerDlGbr,_Am:tmnxCellPortBearerDlMbr,'tmnxCellularPortTftTable':tmnxCellularPortTftTable,'tmnxCellularPortTftEntry':tmnxCellularPortTftEntry,_T:tmnxCellPortTftPacketFilterId,_An:tmnxCellPortTftEvalPrecedence,_Ao:tmnxCellPortTftDirection,_Ap:tmnxCellPortTftTos,_Aq:tmnxCellPortTftTosMask,'tmnxCellularNotifyObjects':tmnxCellularNotifyObjects,_K:tmnxCellularNotifyPdnId,_X:tmnxCellMdaNoServiceResetReason,'tmnxCellularNotifyPrefix':tmnxCellularNotifyPrefix,'tmnxCellularNotifications':tmnxCellularNotifications,_Az:tmnxCellularBearerCreated,_A_:tmnxCellularBearerDeleted,_B0:tmnxCellularBearerModified,_B1:tmnxCellularNoServiceReset,_B2:tmnxCellularActiveSimChange})