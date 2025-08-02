_AF='avSurvNfasIndex'
_AE='avSurvNfasSigGroupRefNumber'
_AD='avSurvIncomingRoutingIndex'
_AC='avSurvIncomingRoutingGroupRefNumber'
_AB='avSurvBriIndex'
_AA='avSurvSigGroupIndex'
_A9='country25'
_A8='country24'
_A7='country23'
_A6='country22'
_A5='country21'
_A4='country20'
_A3='country19'
_A2='country18'
_A1='country17'
_A0='country16'
_z='country15'
_y='country14'
_x='country13'
_w='country12'
_v='country11'
_u='country10'
_t='country9'
_s='country8'
_r='country7'
_q='country6'
_p='country5'
_o='country4'
_n='country3'
_m='country2'
_l='country1'
_k='peerSlave'
_j='peerMaster'
_i='avSurvDs1Index'
_h='avSurvSlotConfigIndex'
_g='unused'
_f='avSurvIpVoiceCodecSetIndex'
_e='avSurvIpVoiceCodecSetNum'
_d='avSurvFacIndex'
_c='avSurvDialIndex'
_b='avSurvTrunkIndex'
_a='avSurvTrunkGroupRefNumber'
_Z='operator'
_Y='restricted'
_X='codeset7'
_W='codeset6'
_V='avSurvTrunkGroupNum'
_U='emergency'
_T='avSurvStationIndex'
_S='OctetString'
_R='network'
_Q='none'
_P='aea'
_O='aes'
_N='passthru'
_M='off'
_L='disabled'
_K='enabled'
_J='read-only'
_I='avSurvNotificationSeverity'
_H='read-write'
_G='no'
_F='yes'
_E='AVAYA-SURV-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
avGatewayMibs,=mibBuilder.importSymbols('AVAYAGEN-MIB','avGatewayMibs')
InetAddress,InetAddressIPv6,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','RowStatus','TextualConvention','TimeInterval','TruthValue')
avSurvMib=ModuleIdentity((1,3,6,1,4,1,6889,2,6,4))
_AvSurvNotification_ObjectIdentity=ObjectIdentity
avSurvNotification=_AvSurvNotification_ObjectIdentity((1,3,6,1,4,1,6889,2,6,4,0))
_AvSurvConfig_ObjectIdentity=ObjectIdentity
avSurvConfig=_AvSurvConfig_ObjectIdentity((1,3,6,1,4,1,6889,2,6,4,1))
class _AvSurvAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AvSurvAdminState_Type.__name__=_C
_AvSurvAdminState_Object=MibScalar
avSurvAdminState=_AvSurvAdminState_Object((1,3,6,1,4,1,6889,2,6,4,1,1),_AvSurvAdminState_Type())
avSurvAdminState.setMaxAccess(_H)
if mibBuilder.loadTexts:avSurvAdminState.setStatus(_A)
class _AvSurvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_AvSurvStatus_Type.__name__=_C
_AvSurvStatus_Object=MibScalar
avSurvStatus=_AvSurvStatus_Object((1,3,6,1,4,1,6889,2,6,4,1,2),_AvSurvStatus_Type())
avSurvStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:avSurvStatus.setStatus(_A)
class _AvSurvMaxIPReg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_AvSurvMaxIPReg_Type.__name__=_C
_AvSurvMaxIPReg_Object=MibScalar
avSurvMaxIPReg=_AvSurvMaxIPReg_Object((1,3,6,1,4,1,6889,2,6,4,1,3),_AvSurvMaxIPReg_Type())
avSurvMaxIPReg.setMaxAccess(_H)
if mibBuilder.loadTexts:avSurvMaxIPReg.setStatus(_A)
class _AvSurvDateFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mmDdYy',1),('ddMmYy',2),('yyMmDd',3)))
_AvSurvDateFormat_Type.__name__=_C
_AvSurvDateFormat_Object=MibScalar
avSurvDateFormat=_AvSurvDateFormat_Object((1,3,6,1,4,1,6889,2,6,4,1,4),_AvSurvDateFormat_Type())
avSurvDateFormat.setMaxAccess(_H)
if mibBuilder.loadTexts:avSurvDateFormat.setStatus(_A)
_AvSurvEndDLTimeStamp_Type=DateAndTime
_AvSurvEndDLTimeStamp_Object=MibScalar
avSurvEndDLTimeStamp=_AvSurvEndDLTimeStamp_Object((1,3,6,1,4,1,6889,2,6,4,1,5),_AvSurvEndDLTimeStamp_Type())
avSurvEndDLTimeStamp.setMaxAccess(_H)
if mibBuilder.loadTexts:avSurvEndDLTimeStamp.setStatus(_A)
class _AvSurvNotificationSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6)))
_AvSurvNotificationSeverity_Type.__name__=_C
_AvSurvNotificationSeverity_Object=MibScalar
avSurvNotificationSeverity=_AvSurvNotificationSeverity_Object((1,3,6,1,4,1,6889,2,6,4,1,6),_AvSurvNotificationSeverity_Type())
avSurvNotificationSeverity.setMaxAccess(_J)
if mibBuilder.loadTexts:avSurvNotificationSeverity.setStatus(_A)
class _AvSurvConfigCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_AvSurvConfigCommand_Type.__name__=_C
_AvSurvConfigCommand_Object=MibScalar
avSurvConfigCommand=_AvSurvConfigCommand_Object((1,3,6,1,4,1,6889,2,6,4,1,7),_AvSurvConfigCommand_Type())
avSurvConfigCommand.setMaxAccess(_H)
if mibBuilder.loadTexts:avSurvConfigCommand.setStatus(_A)
class _AvSurvGatewayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_AvSurvGatewayNumber_Type.__name__=_C
_AvSurvGatewayNumber_Object=MibScalar
avSurvGatewayNumber=_AvSurvGatewayNumber_Object((1,3,6,1,4,1,6889,2,6,4,1,8),_AvSurvGatewayNumber_Type())
avSurvGatewayNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:avSurvGatewayNumber.setStatus(_A)
class _AvSurvPimLockout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AvSurvPimLockout_Type.__name__=_C
_AvSurvPimLockout_Object=MibScalar
avSurvPimLockout=_AvSurvPimLockout_Object((1,3,6,1,4,1,6889,2,6,4,1,9),_AvSurvPimLockout_Type())
avSurvPimLockout.setMaxAccess(_H)
if mibBuilder.loadTexts:avSurvPimLockout.setStatus(_A)
class _AvSurvAttendantAccessCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,3))
_AvSurvAttendantAccessCode_Type.__name__=_D
_AvSurvAttendantAccessCode_Object=MibScalar
avSurvAttendantAccessCode=_AvSurvAttendantAccessCode_Object((1,3,6,1,4,1,6889,2,6,4,1,10),_AvSurvAttendantAccessCode_Type())
avSurvAttendantAccessCode.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvAttendantAccessCode.setStatus(_A)
class _AvSurvAttendantExtension_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,13))
_AvSurvAttendantExtension_Type.__name__=_D
_AvSurvAttendantExtension_Object=MibScalar
avSurvAttendantExtension=_AvSurvAttendantExtension_Object((1,3,6,1,4,1,6889,2,6,4,1,11),_AvSurvAttendantExtension_Type())
avSurvAttendantExtension.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvAttendantExtension.setStatus(_A)
_AvSurvStationTable_Object=MibTable
avSurvStationTable=_AvSurvStationTable_Object((1,3,6,1,4,1,6889,2,6,4,2))
if mibBuilder.loadTexts:avSurvStationTable.setStatus(_A)
_AvSurvStationEntry_Object=MibTableRow
avSurvStationEntry=_AvSurvStationEntry_Object((1,3,6,1,4,1,6889,2,6,4,2,1))
avSurvStationEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:avSurvStationEntry.setStatus(_A)
class _AvSurvStationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,340))
_AvSurvStationIndex_Type.__name__=_C
_AvSurvStationIndex_Object=MibTableColumn
avSurvStationIndex=_AvSurvStationIndex_Object((1,3,6,1,4,1,6889,2,6,4,2,1,1),_AvSurvStationIndex_Type())
avSurvStationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationIndex.setStatus(_A)
class _AvSurvStationExt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,13))
_AvSurvStationExt_Type.__name__=_D
_AvSurvStationExt_Object=MibTableColumn
avSurvStationExt=_AvSurvStationExt_Object((1,3,6,1,4,1,6889,2,6,4,2,1,2),_AvSurvStationExt_Type())
avSurvStationExt.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationExt.setStatus(_A)
class _AvSurvStationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,20,21,22,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49)));namedValues=NamedValues(*(('ip4601',1),('ip4602',2),('ip4602Sw',3),('ip4606',4),('ip4610Sw',5),('ip4612',6),('ip4620',7),('ip4620Sw',8),('ip4624',9),('analog2500',10),('ip4621',11),('ip4622',12),('ip4625',13),('dcp2402',20),('dcp2410',21),('dcp2420',22),('dcp6402',30),('dcp6402D',31),('dcp6408',32),('dcp6408plus',33),('dcp6408D',34),('dcp6408Dplus',35),('dcp6416Dplus',36),('dcp6424Dplus',37),('dcp8403B',40),('dcp8405B',41),('dcp8405Bplus',42),('dcp8405D',43),('dcp8405Dplus',44),('dcp8410B',45),('dcp8410D',46),('dcp8411B',47),('dcp8411D',48),('dcp8434D',49)))
_AvSurvStationType_Type.__name__=_C
_AvSurvStationType_Object=MibTableColumn
avSurvStationType=_AvSurvStationType_Object((1,3,6,1,4,1,6889,2,6,4,2,1,3),_AvSurvStationType_Type())
avSurvStationType.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationType.setStatus(_A)
class _AvSurvStationInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AvSurvStationInterfaceIndex_Type.__name__=_C
_AvSurvStationInterfaceIndex_Object=MibTableColumn
avSurvStationInterfaceIndex=_AvSurvStationInterfaceIndex_Object((1,3,6,1,4,1,6889,2,6,4,2,1,4),_AvSurvStationInterfaceIndex_Type())
avSurvStationInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationInterfaceIndex.setStatus(_A)
class _AvSurvStationCOR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),('internal',2),('local',3),('toll',4),('unrestricted',5)))
_AvSurvStationCOR_Type.__name__=_C
_AvSurvStationCOR_Object=MibTableColumn
avSurvStationCOR=_AvSurvStationCOR_Object((1,3,6,1,4,1,6889,2,6,4,2,1,5),_AvSurvStationCOR_Type())
avSurvStationCOR.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationCOR.setStatus(_A)
_AvSurvStationTrunkDest_Type=TruthValue
_AvSurvStationTrunkDest_Object=MibTableColumn
avSurvStationTrunkDest=_AvSurvStationTrunkDest_Object((1,3,6,1,4,1,6889,2,6,4,2,1,6),_AvSurvStationTrunkDest_Type())
avSurvStationTrunkDest.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationTrunkDest.setStatus(_A)
_AvSurvStationRowStatus_Type=RowStatus
_AvSurvStationRowStatus_Object=MibTableColumn
avSurvStationRowStatus=_AvSurvStationRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,2,1,7),_AvSurvStationRowStatus_Type())
avSurvStationRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationRowStatus.setStatus(_A)
_AvSurvStationExpansionModule_Type=TruthValue
_AvSurvStationExpansionModule_Object=MibTableColumn
avSurvStationExpansionModule=_AvSurvStationExpansionModule_Object((1,3,6,1,4,1,6889,2,6,4,2,1,8),_AvSurvStationExpansionModule_Type())
avSurvStationExpansionModule.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationExpansionModule.setStatus(_A)
class _AvSurvStationSlotPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AvSurvStationSlotPort_Type.__name__=_D
_AvSurvStationSlotPort_Object=MibTableColumn
avSurvStationSlotPort=_AvSurvStationSlotPort_Object((1,3,6,1,4,1,6889,2,6,4,2,1,9),_AvSurvStationSlotPort_Type())
avSurvStationSlotPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationSlotPort.setStatus(_A)
_AvSurvStationSwitchHookFlash_Type=TruthValue
_AvSurvStationSwitchHookFlash_Object=MibTableColumn
avSurvStationSwitchHookFlash=_AvSurvStationSwitchHookFlash_Object((1,3,6,1,4,1,6889,2,6,4,2,1,10),_AvSurvStationSwitchHookFlash_Type())
avSurvStationSwitchHookFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationSwitchHookFlash.setStatus(_A)
class _AvSurvStationIpAddressRegistered_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_AvSurvStationIpAddressRegistered_Type.__name__=_S
_AvSurvStationIpAddressRegistered_Object=MibTableColumn
avSurvStationIpAddressRegistered=_AvSurvStationIpAddressRegistered_Object((1,3,6,1,4,1,6889,2,6,4,2,1,11),_AvSurvStationIpAddressRegistered_Type())
avSurvStationIpAddressRegistered.setMaxAccess(_J)
if mibBuilder.loadTexts:avSurvStationIpAddressRegistered.setStatus(_A)
class _AvSurvStationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,27))
_AvSurvStationName_Type.__name__=_D
_AvSurvStationName_Object=MibTableColumn
avSurvStationName=_AvSurvStationName_Object((1,3,6,1,4,1,6889,2,6,4,2,1,12),_AvSurvStationName_Type())
avSurvStationName.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvStationName.setStatus(_A)
_AvSurvTrunkGroupTable_Object=MibTable
avSurvTrunkGroupTable=_AvSurvTrunkGroupTable_Object((1,3,6,1,4,1,6889,2,6,4,3))
if mibBuilder.loadTexts:avSurvTrunkGroupTable.setStatus(_A)
_AvSurvTrunkGroupEntry_Object=MibTableRow
avSurvTrunkGroupEntry=_AvSurvTrunkGroupEntry_Object((1,3,6,1,4,1,6889,2,6,4,3,1))
avSurvTrunkGroupEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:avSurvTrunkGroupEntry.setStatus(_A)
class _AvSurvTrunkGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_AvSurvTrunkGroupNum_Type.__name__=_C
_AvSurvTrunkGroupNum_Object=MibTableColumn
avSurvTrunkGroupNum=_AvSurvTrunkGroupNum_Object((1,3,6,1,4,1,6889,2,6,4,3,1,1),_AvSurvTrunkGroupNum_Type())
avSurvTrunkGroupNum.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupNum.setStatus(_A)
class _AvSurvTrunkGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('analogLoopStart',1),('analogDid',2),('analogGroundStart',3),('bri',4),('t1InBandSignaling',5),('t1IsdnSignaling',6),('e1InBandSignaling',7),('e1IsdnSignaling',8)))
_AvSurvTrunkGroupType_Type.__name__=_C
_AvSurvTrunkGroupType_Object=MibTableColumn
avSurvTrunkGroupType=_AvSurvTrunkGroupType_Object((1,3,6,1,4,1,6889,2,6,4,3,1,2),_AvSurvTrunkGroupType_Type())
avSurvTrunkGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupType.setStatus(_A)
class _AvSurvTrunkGroupTAC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_AvSurvTrunkGroupTAC_Type.__name__=_D
_AvSurvTrunkGroupTAC_Object=MibTableColumn
avSurvTrunkGroupTAC=_AvSurvTrunkGroupTAC_Object((1,3,6,1,4,1,6889,2,6,4,3,1,3),_AvSurvTrunkGroupTAC_Type())
avSurvTrunkGroupTAC.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupTAC.setStatus(_A)
class _AvSurvTrunkGroupDial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rotary',1),('dtmf',2),('mf',3)))
_AvSurvTrunkGroupDial_Type.__name__=_C
_AvSurvTrunkGroupDial_Object=MibTableColumn
avSurvTrunkGroupDial=_AvSurvTrunkGroupDial_Object((1,3,6,1,4,1,6889,2,6,4,3,1,4),_AvSurvTrunkGroupDial_Type())
avSurvTrunkGroupDial.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupDial.setStatus(_A)
_AvSurvTrunkGroupRowStatus_Type=RowStatus
_AvSurvTrunkGroupRowStatus_Object=MibTableColumn
avSurvTrunkGroupRowStatus=_AvSurvTrunkGroupRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,3,1,5),_AvSurvTrunkGroupRowStatus_Type())
avSurvTrunkGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupRowStatus.setStatus(_A)
class _AvSurvTrunkGroupDidDigitTreatment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,11,12,13,14,99)));namedValues=NamedValues(*(('absorb1',1),('absorb2',2),('absorb3',3),('absorb4',4),('absorb5',5),('insert1',11),('insert2',12),('insert3',13),('insert4',14),('blank',99)))
_AvSurvTrunkGroupDidDigitTreatment_Type.__name__=_C
_AvSurvTrunkGroupDidDigitTreatment_Object=MibTableColumn
avSurvTrunkGroupDidDigitTreatment=_AvSurvTrunkGroupDidDigitTreatment_Object((1,3,6,1,4,1,6889,2,6,4,3,1,6),_AvSurvTrunkGroupDidDigitTreatment_Type())
avSurvTrunkGroupDidDigitTreatment.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupDidDigitTreatment.setStatus(_A)
class _AvSurvTrunkGroupDidDigitsInsert_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AvSurvTrunkGroupDidDigitsInsert_Type.__name__=_D
_AvSurvTrunkGroupDidDigitsInsert_Object=MibTableColumn
avSurvTrunkGroupDidDigitsInsert=_AvSurvTrunkGroupDidDigitsInsert_Object((1,3,6,1,4,1,6889,2,6,4,3,1,7),_AvSurvTrunkGroupDidDigitsInsert_Type())
avSurvTrunkGroupDidDigitsInsert.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupDidDigitsInsert.setStatus(_A)
class _AvSurvTrunkGroupDidSupervision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('immediate',1),('wink',2)))
_AvSurvTrunkGroupDidSupervision_Type.__name__=_C
_AvSurvTrunkGroupDidSupervision_Object=MibTableColumn
avSurvTrunkGroupDidSupervision=_AvSurvTrunkGroupDidSupervision_Object((1,3,6,1,4,1,6889,2,6,4,3,1,8),_AvSurvTrunkGroupDidSupervision_Type())
avSurvTrunkGroupDidSupervision.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupDidSupervision.setStatus(_A)
class _AvSurvTrunkGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,27))
_AvSurvTrunkGroupName_Type.__name__=_D
_AvSurvTrunkGroupName_Object=MibTableColumn
avSurvTrunkGroupName=_AvSurvTrunkGroupName_Object((1,3,6,1,4,1,6889,2,6,4,3,1,9),_AvSurvTrunkGroupName_Type())
avSurvTrunkGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupName.setStatus(_A)
class _AvSurvTrunkGroupCodesetDisplay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,7)));namedValues=NamedValues(*(('codeset0',0),(_W,6),(_X,7)))
_AvSurvTrunkGroupCodesetDisplay_Type.__name__=_C
_AvSurvTrunkGroupCodesetDisplay_Object=MibTableColumn
avSurvTrunkGroupCodesetDisplay=_AvSurvTrunkGroupCodesetDisplay_Object((1,3,6,1,4,1,6889,2,6,4,3,1,10),_AvSurvTrunkGroupCodesetDisplay_Type())
avSurvTrunkGroupCodesetDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupCodesetDisplay.setStatus(_A)
class _AvSurvTrunkGroupCodesetNational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,7)));namedValues=NamedValues(*((_W,6),(_X,7)))
_AvSurvTrunkGroupCodesetNational_Type.__name__=_C
_AvSurvTrunkGroupCodesetNational_Object=MibTableColumn
avSurvTrunkGroupCodesetNational=_AvSurvTrunkGroupCodesetNational_Object((1,3,6,1,4,1,6889,2,6,4,3,1,11),_AvSurvTrunkGroupCodesetNational_Type())
avSurvTrunkGroupCodesetNational.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupCodesetNational.setStatus(_A)
class _AvSurvTrunkGroupChannelPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exclusive',1),('preferred',2)))
_AvSurvTrunkGroupChannelPreference_Type.__name__=_C
_AvSurvTrunkGroupChannelPreference_Object=MibTableColumn
avSurvTrunkGroupChannelPreference=_AvSurvTrunkGroupChannelPreference_Object((1,3,6,1,4,1,6889,2,6,4,3,1,12),_AvSurvTrunkGroupChannelPreference_Type())
avSurvTrunkGroupChannelPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupChannelPreference.setStatus(_A)
class _AvSurvTrunkGroupDigitHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('enblocEnbloc',0),('enblocOverlap',1),('overlapEnbloc',2),('overlapOverlap',3)))
_AvSurvTrunkGroupDigitHandling_Type.__name__=_C
_AvSurvTrunkGroupDigitHandling_Object=MibTableColumn
avSurvTrunkGroupDigitHandling=_AvSurvTrunkGroupDigitHandling_Object((1,3,6,1,4,1,6889,2,6,4,3,1,13),_AvSurvTrunkGroupDigitHandling_Type())
avSurvTrunkGroupDigitHandling.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupDigitHandling.setStatus(_A)
class _AvSurvTrunkGroupJapanDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AvSurvTrunkGroupJapanDisconnect_Type.__name__=_C
_AvSurvTrunkGroupJapanDisconnect_Object=MibTableColumn
avSurvTrunkGroupJapanDisconnect=_AvSurvTrunkGroupJapanDisconnect_Object((1,3,6,1,4,1,6889,2,6,4,3,1,14),_AvSurvTrunkGroupJapanDisconnect_Type())
avSurvTrunkGroupJapanDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupJapanDisconnect.setStatus(_A)
class _AvSurvTrunkGroupSendName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_Y,3)))
_AvSurvTrunkGroupSendName_Type.__name__=_C
_AvSurvTrunkGroupSendName_Object=MibTableColumn
avSurvTrunkGroupSendName=_AvSurvTrunkGroupSendName_Object((1,3,6,1,4,1,6889,2,6,4,3,1,15),_AvSurvTrunkGroupSendName_Type())
avSurvTrunkGroupSendName.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupSendName.setStatus(_A)
class _AvSurvTrunkGroupSendCallingNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_Y,3)))
_AvSurvTrunkGroupSendCallingNumber_Type.__name__=_C
_AvSurvTrunkGroupSendCallingNumber_Object=MibTableColumn
avSurvTrunkGroupSendCallingNumber=_AvSurvTrunkGroupSendCallingNumber_Object((1,3,6,1,4,1,6889,2,6,4,3,1,16),_AvSurvTrunkGroupSendCallingNumber_Type())
avSurvTrunkGroupSendCallingNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupSendCallingNumber.setStatus(_A)
class _AvSurvTrunkGroupNumberingFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('public',2),('private',3),('unknownPrivate',4)))
_AvSurvTrunkGroupNumberingFormat_Type.__name__=_C
_AvSurvTrunkGroupNumberingFormat_Object=MibTableColumn
avSurvTrunkGroupNumberingFormat=_AvSurvTrunkGroupNumberingFormat_Object((1,3,6,1,4,1,6889,2,6,4,3,1,17),_AvSurvTrunkGroupNumberingFormat_Type())
avSurvTrunkGroupNumberingFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupNumberingFormat.setStatus(_A)
class _AvSurvTrunkGroupIncomingDestination_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_AvSurvTrunkGroupIncomingDestination_Type.__name__=_D
_AvSurvTrunkGroupIncomingDestination_Object=MibTableColumn
avSurvTrunkGroupIncomingDestination=_AvSurvTrunkGroupIncomingDestination_Object((1,3,6,1,4,1,6889,2,6,4,3,1,18),_AvSurvTrunkGroupIncomingDestination_Type())
avSurvTrunkGroupIncomingDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupIncomingDestination.setStatus(_A)
class _AvSurvTrunkGroupIncomingDialTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AvSurvTrunkGroupIncomingDialTone_Type.__name__=_C
_AvSurvTrunkGroupIncomingDialTone_Object=MibTableColumn
avSurvTrunkGroupIncomingDialTone=_AvSurvTrunkGroupIncomingDialTone_Object((1,3,6,1,4,1,6889,2,6,4,3,1,19),_AvSurvTrunkGroupIncomingDialTone_Type())
avSurvTrunkGroupIncomingDialTone.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupIncomingDialTone.setStatus(_A)
class _AvSurvTrunkGroupR2MFCSignaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('set1',1),('set2',2),('set3',3),('set4',4),('set5',5),('set6',6),('set7',7),('set8',8)))
_AvSurvTrunkGroupR2MFCSignaling_Type.__name__=_C
_AvSurvTrunkGroupR2MFCSignaling_Object=MibTableColumn
avSurvTrunkGroupR2MFCSignaling=_AvSurvTrunkGroupR2MFCSignaling_Object((1,3,6,1,4,1,6889,2,6,4,3,1,20),_AvSurvTrunkGroupR2MFCSignaling_Type())
avSurvTrunkGroupR2MFCSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupR2MFCSignaling.setStatus(_A)
class _AvSurvTrunkGroupTrunkHunt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ascend',1),('cyclical',2),('descend',3)))
_AvSurvTrunkGroupTrunkHunt_Type.__name__=_C
_AvSurvTrunkGroupTrunkHunt_Object=MibTableColumn
avSurvTrunkGroupTrunkHunt=_AvSurvTrunkGroupTrunkHunt_Object((1,3,6,1,4,1,6889,2,6,4,3,1,21),_AvSurvTrunkGroupTrunkHunt_Type())
avSurvTrunkGroupTrunkHunt.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupTrunkHunt.setStatus(_A)
class _AvSurvTrunkGroupDs1Supervision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('loopStart',3),('groundStart',4),('winkWink',5),('winkImmediate',6),('winkAuto',7),('immediateImmediate',8),('autoAuto',9),('autoWink',10)))
_AvSurvTrunkGroupDs1Supervision_Type.__name__=_C
_AvSurvTrunkGroupDs1Supervision_Object=MibTableColumn
avSurvTrunkGroupDs1Supervision=_AvSurvTrunkGroupDs1Supervision_Object((1,3,6,1,4,1,6889,2,6,4,3,1,22),_AvSurvTrunkGroupDs1Supervision_Type())
avSurvTrunkGroupDs1Supervision.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupDs1Supervision.setStatus(_A)
class _AvSurvTrunkGroupCbc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AvSurvTrunkGroupCbc_Type.__name__=_C
_AvSurvTrunkGroupCbc_Object=MibTableColumn
avSurvTrunkGroupCbc=_AvSurvTrunkGroupCbc_Object((1,3,6,1,4,1,6889,2,6,4,3,1,23),_AvSurvTrunkGroupCbc_Type())
avSurvTrunkGroupCbc.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupCbc.setStatus(_A)
class _AvSurvTrunkGroupCbcServiceFeature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(197,198,225,227,231,246)));namedValues=NamedValues(*((_Z,197),('suboperator',198),('sdn',225),('megacom',227),('lds',231),('scocs',246)))
_AvSurvTrunkGroupCbcServiceFeature_Type.__name__=_C
_AvSurvTrunkGroupCbcServiceFeature_Object=MibTableColumn
avSurvTrunkGroupCbcServiceFeature=_AvSurvTrunkGroupCbcServiceFeature_Object((1,3,6,1,4,1,6889,2,6,4,3,1,24),_AvSurvTrunkGroupCbcServiceFeature_Type())
avSurvTrunkGroupCbcServiceFeature.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupCbcServiceFeature.setStatus(_A)
class _AvSurvTrunkGroupCbcParameter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_AvSurvTrunkGroupCbcParameter_Type.__name__=_C
_AvSurvTrunkGroupCbcParameter_Object=MibTableColumn
avSurvTrunkGroupCbcParameter=_AvSurvTrunkGroupCbcParameter_Object((1,3,6,1,4,1,6889,2,6,4,3,1,25),_AvSurvTrunkGroupCbcParameter_Type())
avSurvTrunkGroupCbcParameter.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupCbcParameter.setStatus(_A)
class _AvSurvTrunkGroupBusyDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AvSurvTrunkGroupBusyDisconnect_Type.__name__=_C
_AvSurvTrunkGroupBusyDisconnect_Object=MibTableColumn
avSurvTrunkGroupBusyDisconnect=_AvSurvTrunkGroupBusyDisconnect_Object((1,3,6,1,4,1,6889,2,6,4,3,1,26),_AvSurvTrunkGroupBusyDisconnect_Type())
avSurvTrunkGroupBusyDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupBusyDisconnect.setStatus(_A)
_AvSurvTrunkTable_Object=MibTable
avSurvTrunkTable=_AvSurvTrunkTable_Object((1,3,6,1,4,1,6889,2,6,4,4))
if mibBuilder.loadTexts:avSurvTrunkTable.setStatus(_A)
_AvSurvTrunkEntry_Object=MibTableRow
avSurvTrunkEntry=_AvSurvTrunkEntry_Object((1,3,6,1,4,1,6889,2,6,4,4,1))
avSurvTrunkEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:avSurvTrunkEntry.setStatus(_A)
class _AvSurvTrunkGroupRefNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_AvSurvTrunkGroupRefNumber_Type.__name__=_C
_AvSurvTrunkGroupRefNumber_Object=MibTableColumn
avSurvTrunkGroupRefNumber=_AvSurvTrunkGroupRefNumber_Object((1,3,6,1,4,1,6889,2,6,4,4,1,1),_AvSurvTrunkGroupRefNumber_Type())
avSurvTrunkGroupRefNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkGroupRefNumber.setStatus(_A)
class _AvSurvTrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AvSurvTrunkIndex_Type.__name__=_C
_AvSurvTrunkIndex_Object=MibTableColumn
avSurvTrunkIndex=_AvSurvTrunkIndex_Object((1,3,6,1,4,1,6889,2,6,4,4,1,2),_AvSurvTrunkIndex_Type())
avSurvTrunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkIndex.setStatus(_A)
class _AvSurvTrunkInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AvSurvTrunkInterfaceIndex_Type.__name__=_C
_AvSurvTrunkInterfaceIndex_Object=MibTableColumn
avSurvTrunkInterfaceIndex=_AvSurvTrunkInterfaceIndex_Object((1,3,6,1,4,1,6889,2,6,4,4,1,3),_AvSurvTrunkInterfaceIndex_Type())
avSurvTrunkInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkInterfaceIndex.setStatus(_A)
_AvSurvTrunkRowStatus_Type=RowStatus
_AvSurvTrunkRowStatus_Object=MibTableColumn
avSurvTrunkRowStatus=_AvSurvTrunkRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,4,1,4),_AvSurvTrunkRowStatus_Type())
avSurvTrunkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkRowStatus.setStatus(_A)
class _AvSurvTrunkSlotPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AvSurvTrunkSlotPort_Type.__name__=_D
_AvSurvTrunkSlotPort_Object=MibTableColumn
avSurvTrunkSlotPort=_AvSurvTrunkSlotPort_Object((1,3,6,1,4,1,6889,2,6,4,4,1,5),_AvSurvTrunkSlotPort_Type())
avSurvTrunkSlotPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkSlotPort.setStatus(_A)
class _AvSurvTrunkSigGroupRefNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_AvSurvTrunkSigGroupRefNumber_Type.__name__=_C
_AvSurvTrunkSigGroupRefNumber_Object=MibTableColumn
avSurvTrunkSigGroupRefNumber=_AvSurvTrunkSigGroupRefNumber_Object((1,3,6,1,4,1,6889,2,6,4,4,1,6),_AvSurvTrunkSigGroupRefNumber_Type())
avSurvTrunkSigGroupRefNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvTrunkSigGroupRefNumber.setStatus(_A)
_AvSurvArsTable_Object=MibTable
avSurvArsTable=_AvSurvArsTable_Object((1,3,6,1,4,1,6889,2,6,4,5))
if mibBuilder.loadTexts:avSurvArsTable.setStatus(_A)
_AvSurvArsEntry_Object=MibTableRow
avSurvArsEntry=_AvSurvArsEntry_Object((1,3,6,1,4,1,6889,2,6,4,5,1))
avSurvArsEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:avSurvArsEntry.setStatus(_A)
class _AvSurvDialIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AvSurvDialIndex_Type.__name__=_C
_AvSurvDialIndex_Object=MibTableColumn
avSurvDialIndex=_AvSurvDialIndex_Object((1,3,6,1,4,1,6889,2,6,4,5,1,1),_AvSurvDialIndex_Type())
avSurvDialIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialIndex.setStatus(_A)
class _AvSurvDialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,18))
_AvSurvDialString_Type.__name__=_D
_AvSurvDialString_Object=MibTableColumn
avSurvDialString=_AvSurvDialString_Object((1,3,6,1,4,1,6889,2,6,4,5,1,2),_AvSurvDialString_Type())
avSurvDialString.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialString.setStatus(_A)
class _AvSurvDialType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_U,1),('foreignNumberingPlanArea',2),('homeNumberingPlanArea',3),('international',4),('internationalOperator',5),('local',6),('national',7),(_Z,8),('service',9)))
_AvSurvDialType_Type.__name__=_C
_AvSurvDialType_Object=MibTableColumn
avSurvDialType=_AvSurvDialType_Object((1,3,6,1,4,1,6889,2,6,4,5,1,3),_AvSurvDialType_Type())
avSurvDialType.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialType.setStatus(_A)
class _AvSurvDialMaximumLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_AvSurvDialMaximumLength_Type.__name__=_C
_AvSurvDialMaximumLength_Object=MibTableColumn
avSurvDialMaximumLength=_AvSurvDialMaximumLength_Object((1,3,6,1,4,1,6889,2,6,4,5,1,4),_AvSurvDialMaximumLength_Type())
avSurvDialMaximumLength.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialMaximumLength.setStatus(_A)
class _AvSurvDialGroupRefNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_AvSurvDialGroupRefNumber_Type.__name__=_C
_AvSurvDialGroupRefNumber_Object=MibTableColumn
avSurvDialGroupRefNumber=_AvSurvDialGroupRefNumber_Object((1,3,6,1,4,1,6889,2,6,4,5,1,5),_AvSurvDialGroupRefNumber_Type())
avSurvDialGroupRefNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialGroupRefNumber.setStatus(_A)
class _AvSurvDialAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('denyCall',1),('allowCall',2)))
_AvSurvDialAction_Type.__name__=_C
_AvSurvDialAction_Object=MibTableColumn
avSurvDialAction=_AvSurvDialAction_Object((1,3,6,1,4,1,6889,2,6,4,5,1,6),_AvSurvDialAction_Type())
avSurvDialAction.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialAction.setStatus(_A)
_AvSurvDialRowStatus_Type=RowStatus
_AvSurvDialRowStatus_Object=MibTableColumn
avSurvDialRowStatus=_AvSurvDialRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,5,1,7),_AvSurvDialRowStatus_Type())
avSurvDialRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialRowStatus.setStatus(_A)
class _AvSurvDialDeleteDigits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_AvSurvDialDeleteDigits_Type.__name__=_C
_AvSurvDialDeleteDigits_Object=MibTableColumn
avSurvDialDeleteDigits=_AvSurvDialDeleteDigits_Object((1,3,6,1,4,1,6889,2,6,4,5,1,8),_AvSurvDialDeleteDigits_Type())
avSurvDialDeleteDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialDeleteDigits.setStatus(_A)
class _AvSurvDialInsertDigits_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_AvSurvDialInsertDigits_Type.__name__=_D
_AvSurvDialInsertDigits_Object=MibTableColumn
avSurvDialInsertDigits=_AvSurvDialInsertDigits_Object((1,3,6,1,4,1,6889,2,6,4,5,1,9),_AvSurvDialInsertDigits_Type())
avSurvDialInsertDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialInsertDigits.setStatus(_A)
class _AvSurvDialMinimumLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_AvSurvDialMinimumLength_Type.__name__=_C
_AvSurvDialMinimumLength_Object=MibTableColumn
avSurvDialMinimumLength=_AvSurvDialMinimumLength_Object((1,3,6,1,4,1,6889,2,6,4,5,1,10),_AvSurvDialMinimumLength_Type())
avSurvDialMinimumLength.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDialMinimumLength.setStatus(_A)
_AvSurvFacTable_Object=MibTable
avSurvFacTable=_AvSurvFacTable_Object((1,3,6,1,4,1,6889,2,6,4,6))
if mibBuilder.loadTexts:avSurvFacTable.setStatus(_A)
_AvSurvFacEntry_Object=MibTableRow
avSurvFacEntry=_AvSurvFacEntry_Object((1,3,6,1,4,1,6889,2,6,4,6,1))
avSurvFacEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:avSurvFacEntry.setStatus(_A)
class _AvSurvFacIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_AvSurvFacIndex_Type.__name__=_C
_AvSurvFacIndex_Object=MibTableColumn
avSurvFacIndex=_AvSurvFacIndex_Object((1,3,6,1,4,1,6889,2,6,4,6,1,1),_AvSurvFacIndex_Type())
avSurvFacIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvFacIndex.setStatus(_A)
class _AvSurvFacId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_AvSurvFacId_Type.__name__=_D
_AvSurvFacId_Object=MibTableColumn
avSurvFacId=_AvSurvFacId_Object((1,3,6,1,4,1,6889,2,6,4,6,1,2),_AvSurvFacId_Type())
avSurvFacId.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvFacId.setStatus(_A)
_AvSurvFacRowStatus_Type=RowStatus
_AvSurvFacRowStatus_Object=MibTableColumn
avSurvFacRowStatus=_AvSurvFacRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,6,1,3),_AvSurvFacRowStatus_Type())
avSurvFacRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvFacRowStatus.setStatus(_A)
class _AvSurvFacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ars1',1),('ars2',2),('hold',3),('contactOpen',4),('contactClose',5),('contactPulse',6)))
_AvSurvFacType_Type.__name__=_C
_AvSurvFacType_Object=MibTableColumn
avSurvFacType=_AvSurvFacType_Object((1,3,6,1,4,1,6889,2,6,4,6,1,4),_AvSurvFacType_Type())
avSurvFacType.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvFacType.setStatus(_A)
_AvSurvIpVoiceCodecSetTable_Object=MibTable
avSurvIpVoiceCodecSetTable=_AvSurvIpVoiceCodecSetTable_Object((1,3,6,1,4,1,6889,2,6,4,7))
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetTable.setStatus(_A)
_AvSurvIpVoiceCodecSetEntry_Object=MibTableRow
avSurvIpVoiceCodecSetEntry=_AvSurvIpVoiceCodecSetEntry_Object((1,3,6,1,4,1,6889,2,6,4,7,1))
avSurvIpVoiceCodecSetEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetEntry.setStatus(_A)
class _AvSurvIpVoiceCodecSetNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AvSurvIpVoiceCodecSetNum_Type.__name__=_C
_AvSurvIpVoiceCodecSetNum_Object=MibTableColumn
avSurvIpVoiceCodecSetNum=_AvSurvIpVoiceCodecSetNum_Object((1,3,6,1,4,1,6889,2,6,4,7,1,1),_AvSurvIpVoiceCodecSetNum_Type())
avSurvIpVoiceCodecSetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetNum.setStatus(_A)
class _AvSurvIpVoiceCodecSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AvSurvIpVoiceCodecSetIndex_Type.__name__=_C
_AvSurvIpVoiceCodecSetIndex_Object=MibTableColumn
avSurvIpVoiceCodecSetIndex=_AvSurvIpVoiceCodecSetIndex_Object((1,3,6,1,4,1,6889,2,6,4,7,1,2),_AvSurvIpVoiceCodecSetIndex_Type())
avSurvIpVoiceCodecSetIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetIndex.setStatus(_A)
class _AvSurvIpVoiceCodecSetPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AvSurvIpVoiceCodecSetPriority_Type.__name__=_C
_AvSurvIpVoiceCodecSetPriority_Object=MibTableColumn
avSurvIpVoiceCodecSetPriority=_AvSurvIpVoiceCodecSetPriority_Object((1,3,6,1,4,1,6889,2,6,4,7,1,3),_AvSurvIpVoiceCodecSetPriority_Type())
avSurvIpVoiceCodecSetPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetPriority.setStatus(_A)
class _AvSurvIpVoiceCodecSetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('g711u',1),('g711a',2),('g723',3),('g729',4),('g729a',5),('g729b',6),('g729ab',7)))
_AvSurvIpVoiceCodecSetType_Type.__name__=_C
_AvSurvIpVoiceCodecSetType_Object=MibTableColumn
avSurvIpVoiceCodecSetType=_AvSurvIpVoiceCodecSetType_Object((1,3,6,1,4,1,6889,2,6,4,7,1,4),_AvSurvIpVoiceCodecSetType_Type())
avSurvIpVoiceCodecSetType.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetType.setStatus(_A)
_AvSurvIpVoiceCodecSetSilence_Type=TruthValue
_AvSurvIpVoiceCodecSetSilence_Object=MibTableColumn
avSurvIpVoiceCodecSetSilence=_AvSurvIpVoiceCodecSetSilence_Object((1,3,6,1,4,1,6889,2,6,4,7,1,5),_AvSurvIpVoiceCodecSetSilence_Type())
avSurvIpVoiceCodecSetSilence.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetSilence.setStatus(_A)
class _AvSurvIpVoiceCodecSetFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_AvSurvIpVoiceCodecSetFrames_Type.__name__=_C
_AvSurvIpVoiceCodecSetFrames_Object=MibTableColumn
avSurvIpVoiceCodecSetFrames=_AvSurvIpVoiceCodecSetFrames_Object((1,3,6,1,4,1,6889,2,6,4,7,1,6),_AvSurvIpVoiceCodecSetFrames_Type())
avSurvIpVoiceCodecSetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetFrames.setStatus(_A)
_AvSurvIpVoiceCodecSetRowStatus_Type=RowStatus
_AvSurvIpVoiceCodecSetRowStatus_Object=MibTableColumn
avSurvIpVoiceCodecSetRowStatus=_AvSurvIpVoiceCodecSetRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,7,1,7),_AvSurvIpVoiceCodecSetRowStatus_Type())
avSurvIpVoiceCodecSetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpVoiceCodecSetRowStatus.setStatus(_A)
_AvSurvIpCodecSetConfig_ObjectIdentity=ObjectIdentity
avSurvIpCodecSetConfig=_AvSurvIpCodecSetConfig_ObjectIdentity((1,3,6,1,4,1,6889,2,6,4,8))
class _AvSurvIpCodecSetFaxMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('relay',2),(_N,3),('t38',4)))
_AvSurvIpCodecSetFaxMode_Type.__name__=_C
_AvSurvIpCodecSetFaxMode_Object=MibScalar
avSurvIpCodecSetFaxMode=_AvSurvIpCodecSetFaxMode_Object((1,3,6,1,4,1,6889,2,6,4,8,1),_AvSurvIpCodecSetFaxMode_Type())
avSurvIpCodecSetFaxMode.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetFaxMode.setStatus(_A)
class _AvSurvIpCodecSetFaxRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AvSurvIpCodecSetFaxRedundancy_Type.__name__=_C
_AvSurvIpCodecSetFaxRedundancy_Object=MibScalar
avSurvIpCodecSetFaxRedundancy=_AvSurvIpCodecSetFaxRedundancy_Object((1,3,6,1,4,1,6889,2,6,4,8,2),_AvSurvIpCodecSetFaxRedundancy_Type())
avSurvIpCodecSetFaxRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetFaxRedundancy.setStatus(_A)
class _AvSurvIpCodecSetModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('relay',2),(_N,3)))
_AvSurvIpCodecSetModemMode_Type.__name__=_C
_AvSurvIpCodecSetModemMode_Object=MibScalar
avSurvIpCodecSetModemMode=_AvSurvIpCodecSetModemMode_Object((1,3,6,1,4,1,6889,2,6,4,8,3),_AvSurvIpCodecSetModemMode_Type())
avSurvIpCodecSetModemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetModemMode.setStatus(_A)
class _AvSurvIpCodecSetModemRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AvSurvIpCodecSetModemRedundancy_Type.__name__=_C
_AvSurvIpCodecSetModemRedundancy_Object=MibScalar
avSurvIpCodecSetModemRedundancy=_AvSurvIpCodecSetModemRedundancy_Object((1,3,6,1,4,1,6889,2,6,4,8,4),_AvSurvIpCodecSetModemRedundancy_Type())
avSurvIpCodecSetModemRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetModemRedundancy.setStatus(_A)
class _AvSurvIpCodecSetTtyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('us',2),('uk',3),(_N,4)))
_AvSurvIpCodecSetTtyMode_Type.__name__=_C
_AvSurvIpCodecSetTtyMode_Object=MibScalar
avSurvIpCodecSetTtyMode=_AvSurvIpCodecSetTtyMode_Object((1,3,6,1,4,1,6889,2,6,4,8,5),_AvSurvIpCodecSetTtyMode_Type())
avSurvIpCodecSetTtyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetTtyMode.setStatus(_A)
class _AvSurvIpCodecSetTtyRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AvSurvIpCodecSetTtyRedundancy_Type.__name__=_C
_AvSurvIpCodecSetTtyRedundancy_Object=MibScalar
avSurvIpCodecSetTtyRedundancy=_AvSurvIpCodecSetTtyRedundancy_Object((1,3,6,1,4,1,6889,2,6,4,8,6),_AvSurvIpCodecSetTtyRedundancy_Type())
avSurvIpCodecSetTtyRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetTtyRedundancy.setStatus(_A)
class _AvSurvIpCodecSetClearChanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_AvSurvIpCodecSetClearChanMode_Type.__name__=_C
_AvSurvIpCodecSetClearChanMode_Object=MibScalar
avSurvIpCodecSetClearChanMode=_AvSurvIpCodecSetClearChanMode_Object((1,3,6,1,4,1,6889,2,6,4,8,7),_AvSurvIpCodecSetClearChanMode_Type())
avSurvIpCodecSetClearChanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetClearChanMode.setStatus(_A)
class _AvSurvIpCodecSetClearChanRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AvSurvIpCodecSetClearChanRedundancy_Type.__name__=_C
_AvSurvIpCodecSetClearChanRedundancy_Object=MibScalar
avSurvIpCodecSetClearChanRedundancy=_AvSurvIpCodecSetClearChanRedundancy_Object((1,3,6,1,4,1,6889,2,6,4,8,8),_AvSurvIpCodecSetClearChanRedundancy_Type())
avSurvIpCodecSetClearChanRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetClearChanRedundancy.setStatus(_A)
class _AvSurvIpCodecSetEncryptPriority1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3)))
_AvSurvIpCodecSetEncryptPriority1_Type.__name__=_C
_AvSurvIpCodecSetEncryptPriority1_Object=MibScalar
avSurvIpCodecSetEncryptPriority1=_AvSurvIpCodecSetEncryptPriority1_Object((1,3,6,1,4,1,6889,2,6,4,8,9),_AvSurvIpCodecSetEncryptPriority1_Type())
avSurvIpCodecSetEncryptPriority1.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetEncryptPriority1.setStatus(_A)
class _AvSurvIpCodecSetEncryptPriority2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_g,4)))
_AvSurvIpCodecSetEncryptPriority2_Type.__name__=_C
_AvSurvIpCodecSetEncryptPriority2_Object=MibScalar
avSurvIpCodecSetEncryptPriority2=_AvSurvIpCodecSetEncryptPriority2_Object((1,3,6,1,4,1,6889,2,6,4,8,10),_AvSurvIpCodecSetEncryptPriority2_Type())
avSurvIpCodecSetEncryptPriority2.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetEncryptPriority2.setStatus(_A)
class _AvSurvIpCodecSetEncryptPriority3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_g,4)))
_AvSurvIpCodecSetEncryptPriority3_Type.__name__=_C
_AvSurvIpCodecSetEncryptPriority3_Object=MibScalar
avSurvIpCodecSetEncryptPriority3=_AvSurvIpCodecSetEncryptPriority3_Object((1,3,6,1,4,1,6889,2,6,4,8,11),_AvSurvIpCodecSetEncryptPriority3_Type())
avSurvIpCodecSetEncryptPriority3.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIpCodecSetEncryptPriority3.setStatus(_A)
_AvSurvSlotConfigTable_Object=MibTable
avSurvSlotConfigTable=_AvSurvSlotConfigTable_Object((1,3,6,1,4,1,6889,2,6,4,9))
if mibBuilder.loadTexts:avSurvSlotConfigTable.setStatus(_A)
_AvSurvSlotConfigEntry_Object=MibTableRow
avSurvSlotConfigEntry=_AvSurvSlotConfigEntry_Object((1,3,6,1,4,1,6889,2,6,4,9,1))
avSurvSlotConfigEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:avSurvSlotConfigEntry.setStatus(_A)
class _AvSurvSlotConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AvSurvSlotConfigIndex_Type.__name__=_C
_AvSurvSlotConfigIndex_Object=MibTableColumn
avSurvSlotConfigIndex=_AvSurvSlotConfigIndex_Object((1,3,6,1,4,1,6889,2,6,4,9,1,1),_AvSurvSlotConfigIndex_Type())
avSurvSlotConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSlotConfigIndex.setStatus(_A)
class _AvSurvSlotConfigNumberId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AvSurvSlotConfigNumberId_Type.__name__=_D
_AvSurvSlotConfigNumberId_Object=MibTableColumn
avSurvSlotConfigNumberId=_AvSurvSlotConfigNumberId_Object((1,3,6,1,4,1,6889,2,6,4,9,1,2),_AvSurvSlotConfigNumberId_Type())
avSurvSlotConfigNumberId.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSlotConfigNumberId.setStatus(_A)
class _AvSurvSlotConfigBoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,7,8,9,14,16,17,18,19,22,23,24,25,26,29,30,31,32)));namedValues=NamedValues(*(('mm720',2),('mm712',3),('mm711',4),('mm710',5),('mm714',7),('mm722',8),('anaImm1t2l',9),('mm717',14),('anaImm4t2l',16),('briImm',17),('dcpImm',18),('ds1Imm',19),('mm716',22),('tgm550',23),('tim514',24),('tim510',25),('tim521',26),('tim508',29),('tim516',30),('tim518',31),('mm312',32)))
_AvSurvSlotConfigBoardType_Type.__name__=_C
_AvSurvSlotConfigBoardType_Object=MibTableColumn
avSurvSlotConfigBoardType=_AvSurvSlotConfigBoardType_Object((1,3,6,1,4,1,6889,2,6,4,9,1,3),_AvSurvSlotConfigBoardType_Type())
avSurvSlotConfigBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSlotConfigBoardType.setStatus(_A)
_AvSurvSlotConfigRowStatus_Type=RowStatus
_AvSurvSlotConfigRowStatus_Object=MibTableColumn
avSurvSlotConfigRowStatus=_AvSurvSlotConfigRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,9,1,4),_AvSurvSlotConfigRowStatus_Type())
avSurvSlotConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSlotConfigRowStatus.setStatus(_A)
_AvSurvDs1Table_Object=MibTable
avSurvDs1Table=_AvSurvDs1Table_Object((1,3,6,1,4,1,6889,2,6,4,10))
if mibBuilder.loadTexts:avSurvDs1Table.setStatus(_A)
_AvSurvDs1Entry_Object=MibTableRow
avSurvDs1Entry=_AvSurvDs1Entry_Object((1,3,6,1,4,1,6889,2,6,4,10,1))
avSurvDs1Entry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:avSurvDs1Entry.setStatus(_A)
class _AvSurvDs1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AvSurvDs1Index_Type.__name__=_C
_AvSurvDs1Index_Object=MibTableColumn
avSurvDs1Index=_AvSurvDs1Index_Object((1,3,6,1,4,1,6889,2,6,4,10,1,1),_AvSurvDs1Index_Type())
avSurvDs1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1Index.setStatus(_A)
class _AvSurvDs1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AvSurvDs1Name_Type.__name__=_D
_AvSurvDs1Name_Object=MibTableColumn
avSurvDs1Name=_AvSurvDs1Name_Object((1,3,6,1,4,1,6889,2,6,4,10,1,2),_AvSurvDs1Name_Type())
avSurvDs1Name.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1Name.setStatus(_A)
class _AvSurvDs1BitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rate1544',1),('rate2048',2)))
_AvSurvDs1BitRate_Type.__name__=_C
_AvSurvDs1BitRate_Object=MibTableColumn
avSurvDs1BitRate=_AvSurvDs1BitRate_Object((1,3,6,1,4,1,6889,2,6,4,10,1,3),_AvSurvDs1BitRate_Type())
avSurvDs1BitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1BitRate.setStatus(_A)
class _AvSurvDs1SignalingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cas',1),('robbedBit',2),('isdnPri',3),('isdnExt',4)))
_AvSurvDs1SignalingMode_Type.__name__=_C
_AvSurvDs1SignalingMode_Object=MibTableColumn
avSurvDs1SignalingMode=_AvSurvDs1SignalingMode_Object((1,3,6,1,4,1,6889,2,6,4,10,1,4),_AvSurvDs1SignalingMode_Type())
avSurvDs1SignalingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1SignalingMode.setStatus(_A)
class _AvSurvDs1ChannelNumbering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sequential',1),('timeSlot',2)))
_AvSurvDs1ChannelNumbering_Type.__name__=_C
_AvSurvDs1ChannelNumbering_Object=MibTableColumn
avSurvDs1ChannelNumbering=_AvSurvDs1ChannelNumbering_Object((1,3,6,1,4,1,6889,2,6,4,10,1,5),_AvSurvDs1ChannelNumbering_Type())
avSurvDs1ChannelNumbering.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1ChannelNumbering.setStatus(_A)
class _AvSurvDs1Connect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('host',1),(_R,2),('pbx',3),('lineSide',4)))
_AvSurvDs1Connect_Type.__name__=_C
_AvSurvDs1Connect_Object=MibTableColumn
avSurvDs1Connect=_AvSurvDs1Connect_Object((1,3,6,1,4,1,6889,2,6,4,10,1,6),_AvSurvDs1Connect_Type())
avSurvDs1Connect.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1Connect.setStatus(_A)
class _AvSurvDs1Interface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4)));namedValues=NamedValues(*(('user',0),(_R,1),(_j,3),(_k,4)))
_AvSurvDs1Interface_Type.__name__=_C
_AvSurvDs1Interface_Object=MibTableColumn
avSurvDs1Interface=_AvSurvDs1Interface_Object((1,3,6,1,4,1,6889,2,6,4,10,1,7),_AvSurvDs1Interface_Type())
avSurvDs1Interface.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1Interface.setStatus(_A)
class _AvSurvDs1Side_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('a',0),('b',1)))
_AvSurvDs1Side_Type.__name__=_C
_AvSurvDs1Side_Object=MibTableColumn
avSurvDs1Side=_AvSurvDs1Side_Object((1,3,6,1,4,1,6889,2,6,4,10,1,8),_AvSurvDs1Side_Type())
avSurvDs1Side.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1Side.setStatus(_A)
class _AvSurvDs1CountryProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,62,63)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),(_p,5),(_q,6),(_r,7),(_s,8),(_t,9),(_u,10),(_v,11),(_w,12),(_x,13),(_y,14),(_z,15),(_A0,16),(_A1,17),(_A2,18),(_A3,19),(_A4,20),(_A5,21),(_A6,22),(_A7,23),(_A8,24),(_A9,25),('etsi',62),('qsig',63)))
_AvSurvDs1CountryProtocol_Type.__name__=_C
_AvSurvDs1CountryProtocol_Object=MibTableColumn
avSurvDs1CountryProtocol=_AvSurvDs1CountryProtocol_Object((1,3,6,1,4,1,6889,2,6,4,10,1,9),_AvSurvDs1CountryProtocol_Type())
avSurvDs1CountryProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1CountryProtocol.setStatus(_A)
class _AvSurvDs1ProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('a',0),('b',1),('c',2),('d',3)))
_AvSurvDs1ProtocolVersion_Type.__name__=_C
_AvSurvDs1ProtocolVersion_Object=MibTableColumn
avSurvDs1ProtocolVersion=_AvSurvDs1ProtocolVersion_Object((1,3,6,1,4,1,6889,2,6,4,10,1,10),_AvSurvDs1ProtocolVersion_Type())
avSurvDs1ProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1ProtocolVersion.setStatus(_A)
class _AvSurvDs1BearerCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('threeKhz',0),('speech',1)))
_AvSurvDs1BearerCapability_Type.__name__=_C
_AvSurvDs1BearerCapability_Object=MibTableColumn
avSurvDs1BearerCapability=_AvSurvDs1BearerCapability_Object((1,3,6,1,4,1,6889,2,6,4,10,1,11),_AvSurvDs1BearerCapability_Type())
avSurvDs1BearerCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1BearerCapability.setStatus(_A)
class _AvSurvDs1InterfaceCompanding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alaw',1),('ulaw',2)))
_AvSurvDs1InterfaceCompanding_Type.__name__=_C
_AvSurvDs1InterfaceCompanding_Object=MibTableColumn
avSurvDs1InterfaceCompanding=_AvSurvDs1InterfaceCompanding_Object((1,3,6,1,4,1,6889,2,6,4,10,1,12),_AvSurvDs1InterfaceCompanding_Type())
avSurvDs1InterfaceCompanding.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1InterfaceCompanding.setStatus(_A)
class _AvSurvDs1LongTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_AvSurvDs1LongTimer_Type.__name__=_C
_AvSurvDs1LongTimer_Object=MibTableColumn
avSurvDs1LongTimer=_AvSurvDs1LongTimer_Object((1,3,6,1,4,1,6889,2,6,4,10,1,13),_AvSurvDs1LongTimer_Type())
avSurvDs1LongTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1LongTimer.setStatus(_A)
_AvSurvDs1RowStatus_Type=RowStatus
_AvSurvDs1RowStatus_Object=MibTableColumn
avSurvDs1RowStatus=_AvSurvDs1RowStatus_Object((1,3,6,1,4,1,6889,2,6,4,10,1,14),_AvSurvDs1RowStatus_Type())
avSurvDs1RowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1RowStatus.setStatus(_A)
class _AvSurvDs1SlotNumberId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AvSurvDs1SlotNumberId_Type.__name__=_D
_AvSurvDs1SlotNumberId_Object=MibTableColumn
avSurvDs1SlotNumberId=_AvSurvDs1SlotNumberId_Object((1,3,6,1,4,1,6889,2,6,4,10,1,15),_AvSurvDs1SlotNumberId_Type())
avSurvDs1SlotNumberId.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvDs1SlotNumberId.setStatus(_A)
_AvSurvSigGroupTable_Object=MibTable
avSurvSigGroupTable=_AvSurvSigGroupTable_Object((1,3,6,1,4,1,6889,2,6,4,11))
if mibBuilder.loadTexts:avSurvSigGroupTable.setStatus(_A)
_AvSurvSigGroupEntry_Object=MibTableRow
avSurvSigGroupEntry=_AvSurvSigGroupEntry_Object((1,3,6,1,4,1,6889,2,6,4,11,1))
avSurvSigGroupEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:avSurvSigGroupEntry.setStatus(_A)
class _AvSurvSigGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_AvSurvSigGroupIndex_Type.__name__=_C
_AvSurvSigGroupIndex_Object=MibTableColumn
avSurvSigGroupIndex=_AvSurvSigGroupIndex_Object((1,3,6,1,4,1,6889,2,6,4,11,1,1),_AvSurvSigGroupIndex_Type())
avSurvSigGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSigGroupIndex.setStatus(_A)
class _AvSurvSigGroupChannelSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_AvSurvSigGroupChannelSelection_Type.__name__=_C
_AvSurvSigGroupChannelSelection_Object=MibTableColumn
avSurvSigGroupChannelSelection=_AvSurvSigGroupChannelSelection_Object((1,3,6,1,4,1,6889,2,6,4,11,1,2),_AvSurvSigGroupChannelSelection_Type())
avSurvSigGroupChannelSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSigGroupChannelSelection.setStatus(_A)
class _AvSurvSigGroupAssociatedSignaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AvSurvSigGroupAssociatedSignaling_Type.__name__=_C
_AvSurvSigGroupAssociatedSignaling_Object=MibTableColumn
avSurvSigGroupAssociatedSignaling=_AvSurvSigGroupAssociatedSignaling_Object((1,3,6,1,4,1,6889,2,6,4,11,1,3),_AvSurvSigGroupAssociatedSignaling_Type())
avSurvSigGroupAssociatedSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSigGroupAssociatedSignaling.setStatus(_A)
class _AvSurvSigGroupPrimaryDChannel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_AvSurvSigGroupPrimaryDChannel_Type.__name__=_D
_AvSurvSigGroupPrimaryDChannel_Object=MibTableColumn
avSurvSigGroupPrimaryDChannel=_AvSurvSigGroupPrimaryDChannel_Object((1,3,6,1,4,1,6889,2,6,4,11,1,4),_AvSurvSigGroupPrimaryDChannel_Type())
avSurvSigGroupPrimaryDChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSigGroupPrimaryDChannel.setStatus(_A)
_AvSurvSigGroupRowStatus_Type=RowStatus
_AvSurvSigGroupRowStatus_Object=MibTableColumn
avSurvSigGroupRowStatus=_AvSurvSigGroupRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,11,1,5),_AvSurvSigGroupRowStatus_Type())
avSurvSigGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvSigGroupRowStatus.setStatus(_A)
_AvSurvBriTable_Object=MibTable
avSurvBriTable=_AvSurvBriTable_Object((1,3,6,1,4,1,6889,2,6,4,12))
if mibBuilder.loadTexts:avSurvBriTable.setStatus(_A)
_AvSurvBriEntry_Object=MibTableRow
avSurvBriEntry=_AvSurvBriEntry_Object((1,3,6,1,4,1,6889,2,6,4,12,1))
avSurvBriEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:avSurvBriEntry.setStatus(_A)
class _AvSurvBriIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_AvSurvBriIndex_Type.__name__=_C
_AvSurvBriIndex_Object=MibTableColumn
avSurvBriIndex=_AvSurvBriIndex_Object((1,3,6,1,4,1,6889,2,6,4,12,1,1),_AvSurvBriIndex_Type())
avSurvBriIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriIndex.setStatus(_A)
class _AvSurvBriName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AvSurvBriName_Type.__name__=_D
_AvSurvBriName_Object=MibTableColumn
avSurvBriName=_AvSurvBriName_Object((1,3,6,1,4,1,6889,2,6,4,12,1,2),_AvSurvBriName_Type())
avSurvBriName.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriName.setStatus(_A)
class _AvSurvBriInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4)));namedValues=NamedValues(*(('user',0),(_R,1),(_j,3),(_k,4)))
_AvSurvBriInterface_Type.__name__=_C
_AvSurvBriInterface_Object=MibTableColumn
avSurvBriInterface=_AvSurvBriInterface_Object((1,3,6,1,4,1,6889,2,6,4,12,1,3),_AvSurvBriInterface_Type())
avSurvBriInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriInterface.setStatus(_A)
class _AvSurvBriSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('a',0),('b',1)))
_AvSurvBriSide_Type.__name__=_C
_AvSurvBriSide_Object=MibTableColumn
avSurvBriSide=_AvSurvBriSide_Object((1,3,6,1,4,1,6889,2,6,4,12,1,4),_AvSurvBriSide_Type())
avSurvBriSide.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriSide.setStatus(_A)
class _AvSurvBriCountryProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,62,63)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),(_p,5),(_q,6),(_r,7),(_s,8),(_t,9),(_u,10),(_v,11),(_w,12),(_x,13),(_y,14),(_z,15),(_A0,16),(_A1,17),(_A2,18),(_A3,19),(_A4,20),(_A5,21),(_A6,22),(_A7,23),(_A8,24),(_A9,25),('etsi',62),('qsig',63)))
_AvSurvBriCountryProtocol_Type.__name__=_C
_AvSurvBriCountryProtocol_Object=MibTableColumn
avSurvBriCountryProtocol=_AvSurvBriCountryProtocol_Object((1,3,6,1,4,1,6889,2,6,4,12,1,5),_AvSurvBriCountryProtocol_Type())
avSurvBriCountryProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriCountryProtocol.setStatus(_A)
class _AvSurvBriBearerCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('threeKhz',0),('speech',1)))
_AvSurvBriBearerCapability_Type.__name__=_C
_AvSurvBriBearerCapability_Object=MibTableColumn
avSurvBriBearerCapability=_AvSurvBriBearerCapability_Object((1,3,6,1,4,1,6889,2,6,4,12,1,6),_AvSurvBriBearerCapability_Type())
avSurvBriBearerCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriBearerCapability.setStatus(_A)
class _AvSurvBriInterfaceCompanding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alaw',1),('ulaw',2)))
_AvSurvBriInterfaceCompanding_Type.__name__=_C
_AvSurvBriInterfaceCompanding_Object=MibTableColumn
avSurvBriInterfaceCompanding=_AvSurvBriInterfaceCompanding_Object((1,3,6,1,4,1,6889,2,6,4,12,1,7),_AvSurvBriInterfaceCompanding_Type())
avSurvBriInterfaceCompanding.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriInterfaceCompanding.setStatus(_A)
class _AvSurvBriTeiAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('zero',2)))
_AvSurvBriTeiAssignment_Type.__name__=_C
_AvSurvBriTeiAssignment_Object=MibTableColumn
avSurvBriTeiAssignment=_AvSurvBriTeiAssignment_Object((1,3,6,1,4,1,6889,2,6,4,12,1,8),_AvSurvBriTeiAssignment_Type())
avSurvBriTeiAssignment.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriTeiAssignment.setStatus(_A)
class _AvSurvBriDirectoryNumberA_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_AvSurvBriDirectoryNumberA_Type.__name__=_D
_AvSurvBriDirectoryNumberA_Object=MibTableColumn
avSurvBriDirectoryNumberA=_AvSurvBriDirectoryNumberA_Object((1,3,6,1,4,1,6889,2,6,4,12,1,9),_AvSurvBriDirectoryNumberA_Type())
avSurvBriDirectoryNumberA.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriDirectoryNumberA.setStatus(_A)
class _AvSurvBriDirectoryNumberB_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_AvSurvBriDirectoryNumberB_Type.__name__=_D
_AvSurvBriDirectoryNumberB_Object=MibTableColumn
avSurvBriDirectoryNumberB=_AvSurvBriDirectoryNumberB_Object((1,3,6,1,4,1,6889,2,6,4,12,1,10),_AvSurvBriDirectoryNumberB_Type())
avSurvBriDirectoryNumberB.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriDirectoryNumberB.setStatus(_A)
class _AvSurvBriSpidA_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_AvSurvBriSpidA_Type.__name__=_D
_AvSurvBriSpidA_Object=MibTableColumn
avSurvBriSpidA=_AvSurvBriSpidA_Object((1,3,6,1,4,1,6889,2,6,4,12,1,11),_AvSurvBriSpidA_Type())
avSurvBriSpidA.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriSpidA.setStatus(_A)
class _AvSurvBriSpidB_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_AvSurvBriSpidB_Type.__name__=_D
_AvSurvBriSpidB_Object=MibTableColumn
avSurvBriSpidB=_AvSurvBriSpidB_Object((1,3,6,1,4,1,6889,2,6,4,12,1,12),_AvSurvBriSpidB_Type())
avSurvBriSpidB.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriSpidB.setStatus(_A)
class _AvSurvBriEndpointInit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AvSurvBriEndpointInit_Type.__name__=_C
_AvSurvBriEndpointInit_Object=MibTableColumn
avSurvBriEndpointInit=_AvSurvBriEndpointInit_Object((1,3,6,1,4,1,6889,2,6,4,12,1,13),_AvSurvBriEndpointInit_Type())
avSurvBriEndpointInit.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriEndpointInit.setStatus(_A)
class _AvSurvBriLayer1Stable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AvSurvBriLayer1Stable_Type.__name__=_C
_AvSurvBriLayer1Stable_Object=MibTableColumn
avSurvBriLayer1Stable=_AvSurvBriLayer1Stable_Object((1,3,6,1,4,1,6889,2,6,4,12,1,14),_AvSurvBriLayer1Stable_Type())
avSurvBriLayer1Stable.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriLayer1Stable.setStatus(_A)
_AvSurvBriRowStatus_Type=RowStatus
_AvSurvBriRowStatus_Object=MibTableColumn
avSurvBriRowStatus=_AvSurvBriRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,12,1,15),_AvSurvBriRowStatus_Type())
avSurvBriRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriRowStatus.setStatus(_A)
class _AvSurvBriSlotPortNumberId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AvSurvBriSlotPortNumberId_Type.__name__=_D
_AvSurvBriSlotPortNumberId_Object=MibTableColumn
avSurvBriSlotPortNumberId=_AvSurvBriSlotPortNumberId_Object((1,3,6,1,4,1,6889,2,6,4,12,1,16),_AvSurvBriSlotPortNumberId_Type())
avSurvBriSlotPortNumberId.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvBriSlotPortNumberId.setStatus(_A)
_AvSurvIncomingRoutingTable_Object=MibTable
avSurvIncomingRoutingTable=_AvSurvIncomingRoutingTable_Object((1,3,6,1,4,1,6889,2,6,4,13))
if mibBuilder.loadTexts:avSurvIncomingRoutingTable.setStatus(_A)
_AvSurvIncomingRoutingEntry_Object=MibTableRow
avSurvIncomingRoutingEntry=_AvSurvIncomingRoutingEntry_Object((1,3,6,1,4,1,6889,2,6,4,13,1))
avSurvIncomingRoutingEntry.setIndexNames((0,_E,_AC),(0,_E,_AD))
if mibBuilder.loadTexts:avSurvIncomingRoutingEntry.setStatus(_A)
class _AvSurvIncomingRoutingGroupRefNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_AvSurvIncomingRoutingGroupRefNumber_Type.__name__=_C
_AvSurvIncomingRoutingGroupRefNumber_Object=MibTableColumn
avSurvIncomingRoutingGroupRefNumber=_AvSurvIncomingRoutingGroupRefNumber_Object((1,3,6,1,4,1,6889,2,6,4,13,1,1),_AvSurvIncomingRoutingGroupRefNumber_Type())
avSurvIncomingRoutingGroupRefNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingGroupRefNumber.setStatus(_A)
class _AvSurvIncomingRoutingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_AvSurvIncomingRoutingIndex_Type.__name__=_C
_AvSurvIncomingRoutingIndex_Object=MibTableColumn
avSurvIncomingRoutingIndex=_AvSurvIncomingRoutingIndex_Object((1,3,6,1,4,1,6889,2,6,4,13,1,2),_AvSurvIncomingRoutingIndex_Type())
avSurvIncomingRoutingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingIndex.setStatus(_A)
class _AvSurvIncomingRoutingMatchPattern_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AvSurvIncomingRoutingMatchPattern_Type.__name__=_D
_AvSurvIncomingRoutingMatchPattern_Object=MibTableColumn
avSurvIncomingRoutingMatchPattern=_AvSurvIncomingRoutingMatchPattern_Object((1,3,6,1,4,1,6889,2,6,4,13,1,3),_AvSurvIncomingRoutingMatchPattern_Type())
avSurvIncomingRoutingMatchPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingMatchPattern.setStatus(_A)
class _AvSurvIncomingRoutingLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,99)));namedValues=NamedValues(*(('len0',0),('len1',1),('len2',2),('len3',3),('len4',4),('len5',5),('len6',6),('len7',7),('len8',8),('len9',9),('len10',10),('len11',11),('len12',12),('len13',13),('len14',14),('len15',15),('len16',16),('len17',17),('len18',18),('len19',19),('len20',20),('len21',21),('blank',99)))
_AvSurvIncomingRoutingLength_Type.__name__=_C
_AvSurvIncomingRoutingLength_Object=MibTableColumn
avSurvIncomingRoutingLength=_AvSurvIncomingRoutingLength_Object((1,3,6,1,4,1,6889,2,6,4,13,1,4),_AvSurvIncomingRoutingLength_Type())
avSurvIncomingRoutingLength.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingLength.setStatus(_A)
class _AvSurvIncomingRoutingDeleteDigits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21))
_AvSurvIncomingRoutingDeleteDigits_Type.__name__=_C
_AvSurvIncomingRoutingDeleteDigits_Object=MibTableColumn
avSurvIncomingRoutingDeleteDigits=_AvSurvIncomingRoutingDeleteDigits_Object((1,3,6,1,4,1,6889,2,6,4,13,1,5),_AvSurvIncomingRoutingDeleteDigits_Type())
avSurvIncomingRoutingDeleteDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingDeleteDigits.setStatus(_A)
class _AvSurvIncomingRoutingInsertDigits_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AvSurvIncomingRoutingInsertDigits_Type.__name__=_D
_AvSurvIncomingRoutingInsertDigits_Object=MibTableColumn
avSurvIncomingRoutingInsertDigits=_AvSurvIncomingRoutingInsertDigits_Object((1,3,6,1,4,1,6889,2,6,4,13,1,6),_AvSurvIncomingRoutingInsertDigits_Type())
avSurvIncomingRoutingInsertDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingInsertDigits.setStatus(_A)
class _AvSurvIncomingRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enbloc',0),('overlap',1)))
_AvSurvIncomingRoutingMode_Type.__name__=_C
_AvSurvIncomingRoutingMode_Object=MibTableColumn
avSurvIncomingRoutingMode=_AvSurvIncomingRoutingMode_Object((1,3,6,1,4,1,6889,2,6,4,13,1,7),_AvSurvIncomingRoutingMode_Type())
avSurvIncomingRoutingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingMode.setStatus(_A)
_AvSurvIncomingRoutingRowStatus_Type=RowStatus
_AvSurvIncomingRoutingRowStatus_Object=MibTableColumn
avSurvIncomingRoutingRowStatus=_AvSurvIncomingRoutingRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,13,1,8),_AvSurvIncomingRoutingRowStatus_Type())
avSurvIncomingRoutingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvIncomingRoutingRowStatus.setStatus(_A)
_AvSurvNfasTable_Object=MibTable
avSurvNfasTable=_AvSurvNfasTable_Object((1,3,6,1,4,1,6889,2,6,4,14))
if mibBuilder.loadTexts:avSurvNfasTable.setStatus(_A)
_AvSurvNfasEntry_Object=MibTableRow
avSurvNfasEntry=_AvSurvNfasEntry_Object((1,3,6,1,4,1,6889,2,6,4,14,1))
avSurvNfasEntry.setIndexNames((0,_E,_AE),(0,_E,_AF))
if mibBuilder.loadTexts:avSurvNfasEntry.setStatus(_A)
class _AvSurvNfasSigGroupRefNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_AvSurvNfasSigGroupRefNumber_Type.__name__=_C
_AvSurvNfasSigGroupRefNumber_Object=MibTableColumn
avSurvNfasSigGroupRefNumber=_AvSurvNfasSigGroupRefNumber_Object((1,3,6,1,4,1,6889,2,6,4,14,1,1),_AvSurvNfasSigGroupRefNumber_Type())
avSurvNfasSigGroupRefNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvNfasSigGroupRefNumber.setStatus(_A)
class _AvSurvNfasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AvSurvNfasIndex_Type.__name__=_C
_AvSurvNfasIndex_Object=MibTableColumn
avSurvNfasIndex=_AvSurvNfasIndex_Object((1,3,6,1,4,1,6889,2,6,4,14,1,2),_AvSurvNfasIndex_Type())
avSurvNfasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvNfasIndex.setStatus(_A)
class _AvSurvNfasInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_AvSurvNfasInterface_Type.__name__=_D
_AvSurvNfasInterface_Object=MibTableColumn
avSurvNfasInterface=_AvSurvNfasInterface_Object((1,3,6,1,4,1,6889,2,6,4,14,1,3),_AvSurvNfasInterface_Type())
avSurvNfasInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvNfasInterface.setStatus(_A)
class _AvSurvNfasInterfaceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AvSurvNfasInterfaceId_Type.__name__=_C
_AvSurvNfasInterfaceId_Object=MibTableColumn
avSurvNfasInterfaceId=_AvSurvNfasInterfaceId_Object((1,3,6,1,4,1,6889,2,6,4,14,1,4),_AvSurvNfasInterfaceId_Type())
avSurvNfasInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvNfasInterfaceId.setStatus(_A)
_AvSurvNfasRowStatus_Type=RowStatus
_AvSurvNfasRowStatus_Object=MibTableColumn
avSurvNfasRowStatus=_AvSurvNfasRowStatus_Object((1,3,6,1,4,1,6889,2,6,4,14,1,5),_AvSurvNfasRowStatus_Type())
avSurvNfasRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avSurvNfasRowStatus.setStatus(_A)
avSurvEnabled=NotificationType((1,3,6,1,4,1,6889,2,6,4,0,1))
avSurvEnabled.setObjects((_E,_I))
if mibBuilder.loadTexts:avSurvEnabled.setStatus(_A)
avSurvDisabled=NotificationType((1,3,6,1,4,1,6889,2,6,4,0,2))
avSurvDisabled.setObjects((_E,_I))
if mibBuilder.loadTexts:avSurvDisabled.setStatus(_A)
avSurvActive=NotificationType((1,3,6,1,4,1,6889,2,6,4,0,3))
avSurvActive.setObjects((_E,_I))
if mibBuilder.loadTexts:avSurvActive.setStatus(_A)
avSurvInactive=NotificationType((1,3,6,1,4,1,6889,2,6,4,0,4))
avSurvInactive.setObjects((_E,_I))
if mibBuilder.loadTexts:avSurvInactive.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'avSurvMib':avSurvMib,'avSurvNotification':avSurvNotification,'avSurvEnabled':avSurvEnabled,'avSurvDisabled':avSurvDisabled,'avSurvActive':avSurvActive,'avSurvInactive':avSurvInactive,'avSurvConfig':avSurvConfig,'avSurvAdminState':avSurvAdminState,'avSurvStatus':avSurvStatus,'avSurvMaxIPReg':avSurvMaxIPReg,'avSurvDateFormat':avSurvDateFormat,'avSurvEndDLTimeStamp':avSurvEndDLTimeStamp,_I:avSurvNotificationSeverity,'avSurvConfigCommand':avSurvConfigCommand,'avSurvGatewayNumber':avSurvGatewayNumber,'avSurvPimLockout':avSurvPimLockout,'avSurvAttendantAccessCode':avSurvAttendantAccessCode,'avSurvAttendantExtension':avSurvAttendantExtension,'avSurvStationTable':avSurvStationTable,'avSurvStationEntry':avSurvStationEntry,_T:avSurvStationIndex,'avSurvStationExt':avSurvStationExt,'avSurvStationType':avSurvStationType,'avSurvStationInterfaceIndex':avSurvStationInterfaceIndex,'avSurvStationCOR':avSurvStationCOR,'avSurvStationTrunkDest':avSurvStationTrunkDest,'avSurvStationRowStatus':avSurvStationRowStatus,'avSurvStationExpansionModule':avSurvStationExpansionModule,'avSurvStationSlotPort':avSurvStationSlotPort,'avSurvStationSwitchHookFlash':avSurvStationSwitchHookFlash,'avSurvStationIpAddressRegistered':avSurvStationIpAddressRegistered,'avSurvStationName':avSurvStationName,'avSurvTrunkGroupTable':avSurvTrunkGroupTable,'avSurvTrunkGroupEntry':avSurvTrunkGroupEntry,_V:avSurvTrunkGroupNum,'avSurvTrunkGroupType':avSurvTrunkGroupType,'avSurvTrunkGroupTAC':avSurvTrunkGroupTAC,'avSurvTrunkGroupDial':avSurvTrunkGroupDial,'avSurvTrunkGroupRowStatus':avSurvTrunkGroupRowStatus,'avSurvTrunkGroupDidDigitTreatment':avSurvTrunkGroupDidDigitTreatment,'avSurvTrunkGroupDidDigitsInsert':avSurvTrunkGroupDidDigitsInsert,'avSurvTrunkGroupDidSupervision':avSurvTrunkGroupDidSupervision,'avSurvTrunkGroupName':avSurvTrunkGroupName,'avSurvTrunkGroupCodesetDisplay':avSurvTrunkGroupCodesetDisplay,'avSurvTrunkGroupCodesetNational':avSurvTrunkGroupCodesetNational,'avSurvTrunkGroupChannelPreference':avSurvTrunkGroupChannelPreference,'avSurvTrunkGroupDigitHandling':avSurvTrunkGroupDigitHandling,'avSurvTrunkGroupJapanDisconnect':avSurvTrunkGroupJapanDisconnect,'avSurvTrunkGroupSendName':avSurvTrunkGroupSendName,'avSurvTrunkGroupSendCallingNumber':avSurvTrunkGroupSendCallingNumber,'avSurvTrunkGroupNumberingFormat':avSurvTrunkGroupNumberingFormat,'avSurvTrunkGroupIncomingDestination':avSurvTrunkGroupIncomingDestination,'avSurvTrunkGroupIncomingDialTone':avSurvTrunkGroupIncomingDialTone,'avSurvTrunkGroupR2MFCSignaling':avSurvTrunkGroupR2MFCSignaling,'avSurvTrunkGroupTrunkHunt':avSurvTrunkGroupTrunkHunt,'avSurvTrunkGroupDs1Supervision':avSurvTrunkGroupDs1Supervision,'avSurvTrunkGroupCbc':avSurvTrunkGroupCbc,'avSurvTrunkGroupCbcServiceFeature':avSurvTrunkGroupCbcServiceFeature,'avSurvTrunkGroupCbcParameter':avSurvTrunkGroupCbcParameter,'avSurvTrunkGroupBusyDisconnect':avSurvTrunkGroupBusyDisconnect,'avSurvTrunkTable':avSurvTrunkTable,'avSurvTrunkEntry':avSurvTrunkEntry,_a:avSurvTrunkGroupRefNumber,_b:avSurvTrunkIndex,'avSurvTrunkInterfaceIndex':avSurvTrunkInterfaceIndex,'avSurvTrunkRowStatus':avSurvTrunkRowStatus,'avSurvTrunkSlotPort':avSurvTrunkSlotPort,'avSurvTrunkSigGroupRefNumber':avSurvTrunkSigGroupRefNumber,'avSurvArsTable':avSurvArsTable,'avSurvArsEntry':avSurvArsEntry,_c:avSurvDialIndex,'avSurvDialString':avSurvDialString,'avSurvDialType':avSurvDialType,'avSurvDialMaximumLength':avSurvDialMaximumLength,'avSurvDialGroupRefNumber':avSurvDialGroupRefNumber,'avSurvDialAction':avSurvDialAction,'avSurvDialRowStatus':avSurvDialRowStatus,'avSurvDialDeleteDigits':avSurvDialDeleteDigits,'avSurvDialInsertDigits':avSurvDialInsertDigits,'avSurvDialMinimumLength':avSurvDialMinimumLength,'avSurvFacTable':avSurvFacTable,'avSurvFacEntry':avSurvFacEntry,_d:avSurvFacIndex,'avSurvFacId':avSurvFacId,'avSurvFacRowStatus':avSurvFacRowStatus,'avSurvFacType':avSurvFacType,'avSurvIpVoiceCodecSetTable':avSurvIpVoiceCodecSetTable,'avSurvIpVoiceCodecSetEntry':avSurvIpVoiceCodecSetEntry,_e:avSurvIpVoiceCodecSetNum,_f:avSurvIpVoiceCodecSetIndex,'avSurvIpVoiceCodecSetPriority':avSurvIpVoiceCodecSetPriority,'avSurvIpVoiceCodecSetType':avSurvIpVoiceCodecSetType,'avSurvIpVoiceCodecSetSilence':avSurvIpVoiceCodecSetSilence,'avSurvIpVoiceCodecSetFrames':avSurvIpVoiceCodecSetFrames,'avSurvIpVoiceCodecSetRowStatus':avSurvIpVoiceCodecSetRowStatus,'avSurvIpCodecSetConfig':avSurvIpCodecSetConfig,'avSurvIpCodecSetFaxMode':avSurvIpCodecSetFaxMode,'avSurvIpCodecSetFaxRedundancy':avSurvIpCodecSetFaxRedundancy,'avSurvIpCodecSetModemMode':avSurvIpCodecSetModemMode,'avSurvIpCodecSetModemRedundancy':avSurvIpCodecSetModemRedundancy,'avSurvIpCodecSetTtyMode':avSurvIpCodecSetTtyMode,'avSurvIpCodecSetTtyRedundancy':avSurvIpCodecSetTtyRedundancy,'avSurvIpCodecSetClearChanMode':avSurvIpCodecSetClearChanMode,'avSurvIpCodecSetClearChanRedundancy':avSurvIpCodecSetClearChanRedundancy,'avSurvIpCodecSetEncryptPriority1':avSurvIpCodecSetEncryptPriority1,'avSurvIpCodecSetEncryptPriority2':avSurvIpCodecSetEncryptPriority2,'avSurvIpCodecSetEncryptPriority3':avSurvIpCodecSetEncryptPriority3,'avSurvSlotConfigTable':avSurvSlotConfigTable,'avSurvSlotConfigEntry':avSurvSlotConfigEntry,_h:avSurvSlotConfigIndex,'avSurvSlotConfigNumberId':avSurvSlotConfigNumberId,'avSurvSlotConfigBoardType':avSurvSlotConfigBoardType,'avSurvSlotConfigRowStatus':avSurvSlotConfigRowStatus,'avSurvDs1Table':avSurvDs1Table,'avSurvDs1Entry':avSurvDs1Entry,_i:avSurvDs1Index,'avSurvDs1Name':avSurvDs1Name,'avSurvDs1BitRate':avSurvDs1BitRate,'avSurvDs1SignalingMode':avSurvDs1SignalingMode,'avSurvDs1ChannelNumbering':avSurvDs1ChannelNumbering,'avSurvDs1Connect':avSurvDs1Connect,'avSurvDs1Interface':avSurvDs1Interface,'avSurvDs1Side':avSurvDs1Side,'avSurvDs1CountryProtocol':avSurvDs1CountryProtocol,'avSurvDs1ProtocolVersion':avSurvDs1ProtocolVersion,'avSurvDs1BearerCapability':avSurvDs1BearerCapability,'avSurvDs1InterfaceCompanding':avSurvDs1InterfaceCompanding,'avSurvDs1LongTimer':avSurvDs1LongTimer,'avSurvDs1RowStatus':avSurvDs1RowStatus,'avSurvDs1SlotNumberId':avSurvDs1SlotNumberId,'avSurvSigGroupTable':avSurvSigGroupTable,'avSurvSigGroupEntry':avSurvSigGroupEntry,_AA:avSurvSigGroupIndex,'avSurvSigGroupChannelSelection':avSurvSigGroupChannelSelection,'avSurvSigGroupAssociatedSignaling':avSurvSigGroupAssociatedSignaling,'avSurvSigGroupPrimaryDChannel':avSurvSigGroupPrimaryDChannel,'avSurvSigGroupRowStatus':avSurvSigGroupRowStatus,'avSurvBriTable':avSurvBriTable,'avSurvBriEntry':avSurvBriEntry,_AB:avSurvBriIndex,'avSurvBriName':avSurvBriName,'avSurvBriInterface':avSurvBriInterface,'avSurvBriSide':avSurvBriSide,'avSurvBriCountryProtocol':avSurvBriCountryProtocol,'avSurvBriBearerCapability':avSurvBriBearerCapability,'avSurvBriInterfaceCompanding':avSurvBriInterfaceCompanding,'avSurvBriTeiAssignment':avSurvBriTeiAssignment,'avSurvBriDirectoryNumberA':avSurvBriDirectoryNumberA,'avSurvBriDirectoryNumberB':avSurvBriDirectoryNumberB,'avSurvBriSpidA':avSurvBriSpidA,'avSurvBriSpidB':avSurvBriSpidB,'avSurvBriEndpointInit':avSurvBriEndpointInit,'avSurvBriLayer1Stable':avSurvBriLayer1Stable,'avSurvBriRowStatus':avSurvBriRowStatus,'avSurvBriSlotPortNumberId':avSurvBriSlotPortNumberId,'avSurvIncomingRoutingTable':avSurvIncomingRoutingTable,'avSurvIncomingRoutingEntry':avSurvIncomingRoutingEntry,_AC:avSurvIncomingRoutingGroupRefNumber,_AD:avSurvIncomingRoutingIndex,'avSurvIncomingRoutingMatchPattern':avSurvIncomingRoutingMatchPattern,'avSurvIncomingRoutingLength':avSurvIncomingRoutingLength,'avSurvIncomingRoutingDeleteDigits':avSurvIncomingRoutingDeleteDigits,'avSurvIncomingRoutingInsertDigits':avSurvIncomingRoutingInsertDigits,'avSurvIncomingRoutingMode':avSurvIncomingRoutingMode,'avSurvIncomingRoutingRowStatus':avSurvIncomingRoutingRowStatus,'avSurvNfasTable':avSurvNfasTable,'avSurvNfasEntry':avSurvNfasEntry,_AE:avSurvNfasSigGroupRefNumber,_AF:avSurvNfasIndex,'avSurvNfasInterface':avSurvNfasInterface,'avSurvNfasInterfaceId':avSurvNfasInterfaceId,'avSurvNfasRowStatus':avSurvNfasRowStatus})