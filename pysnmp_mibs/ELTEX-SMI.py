_Ab='omsOperationCommandOk'
_Aa='omsOperationCommandAlarm'
_AZ='mp800mkBatConnOkTrap'
_AY='mp800mkSuppOkTrap'
_AX='mp800mkIbatChOkTrap'
_AW='mp800mkIloadOkTrap'
_AV='mp800mkBatChargeOkTrap'
_AU='mp800mkACVOkTrap'
_AT='mp800mkDVcellOkTrap'
_AS='mp800mkRlsDevOkTrap'
_AR='mp800mkVbatChOkTrap'
_AQ='mp800mkVbatMOkTrap'
_AP='mp800mkIbatMOkTrap'
_AO='mp800mkACVMOkTrap'
_AN='mp800mkTMOkTrap'
_AM='mp800mkUEPConfOkTrap'
_AL='mp800mkInpParmOkTrap'
_AK='mp800mkMPStatusOkTrap'
_AJ='mp800mkBatConnAlarmTrap'
_AI='mp800mkSuppAlarmTrap'
_AH='mp800mkIbatChAlarmTrap'
_AG='mp800mkIloadAlarmTrap'
_AF='mp800mkBatChargeAlarmTrap'
_AE='mp800mkACVAlarmTrap'
_AD='mp800mkDVcellAlarmTrap'
_AC='mp800mkRlsDevAlarmTrap'
_AB='mp800mkVbatChAlarmTrap'
_AA='mp800mkVbatMAlarmTrap'
_A9='mp800mkIbatMAlarmTrap'
_A8='mp800mkACVMAlarmTrap'
_A7='mp800mkTMAlarmTrap'
_A6='mp800mkUEPConfAlarmTrap'
_A5='mp800mkInpParmAlarmTrap'
_A4='mp800mkMPStatusAlarmTrap'
_A3='dslamEthLinkOkTrap'
_A2='dslamSessionOkTrap'
_A1='dslamVoltageOkTrap'
_A0='dslamOverheatOkTrap'
_z='dslamEthLinkAlarmTrap'
_y='dslamSessionAlarmTrap'
_x='dslamVoltageAlarmTrap'
_w='dslamOverheatAlarmTrap'
_v='ponOpticalOkTrap'
_u='ponEthOkTrap'
_t='ponONUAuthOkTrap'
_s='dslamUSRateOkTrap'
_r='dslamDSRateOkTrap'
_q='dslamLinkUpTrap'
_p='mc240SensOkTrap'
_o='mc240UPSOkTrap'
_n='mxlTELEOkTrap'
_m='mxlDPSOkTrap'
_l='mc240CardOkTrap'
_k='mc240FileOkTrap'
_j='mc240ss7LinksetOkTrap'
_i='mc240ss7LinkOkTrap'
_h='mc240SyncOkTrap'
_g='mc240StreamOkTrap'
_f='ponOpticalAlarmTrap'
_e='ponEthAlarmTrap'
_d='ponONUAuthAlarmTrap'
_c='dslamUSRateAlarmTrap'
_b='dslamDSRateAlarmTrap'
_a='dslamLinkDownTrap'
_Z='mc240SensAlarmTrap'
_Y='mc240UPSAlarmTrap'
_X='mxlTELEAlarmTrap'
_W='mxlDPSAlarmTrap'
_V='mc240CardAlarmTrap'
_U='mc240FileAlarmTrap'
_T='mc240ss7LinksetAlarmTrap'
_S='mc240ss7LinkAlarmTrap'
_R='mc240SyncAlarmTrap'
_Q='mc240StreamAlarmTrap'
_P='DisplayString'
_O='read-only'
_N='mcReservedFlag'
_M='mcTrapSyncType'
_L='mcTrapRestoredAlarmID'
_K='mp800mkTrapComment'
_J='mp800mkTrapValue'
_I='mp800mkTrapParameter'
_H='mcTrapDescr'
_G='mcTrapID'
_F='mcTrapLParam3'
_E='mcTrapLParam2'
_D='mcTrapLParam1'
_C='mcTrapExState'
_B='current'
_A='ELTEX-SMI'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention','TimeStamp')
eltex=ModuleIdentity((1,3,6,1,4,1,34300))
_ElHardware_ObjectIdentity=ObjectIdentity
elHardware=_ElHardware_ObjectIdentity((1,3,6,1,4,1,34300,1))
if mibBuilder.loadTexts:elHardware.setStatus(_B)
_ElSoftware_ObjectIdentity=ObjectIdentity
elSoftware=_ElSoftware_ObjectIdentity((1,3,6,1,4,1,34300,2))
if mibBuilder.loadTexts:elSoftware.setStatus(_B)
_EltrapGroup_ObjectIdentity=ObjectIdentity
eltrapGroup=_EltrapGroup_ObjectIdentity((1,3,6,1,4,1,34300,3))
if mibBuilder.loadTexts:eltrapGroup.setStatus(_B)
_Mc240AlarmTraps_ObjectIdentity=ObjectIdentity
mc240AlarmTraps=_Mc240AlarmTraps_ObjectIdentity((1,3,6,1,4,1,34300,3,3))
_Mc240OkTraps_ObjectIdentity=ObjectIdentity
mc240OkTraps=_Mc240OkTraps_ObjectIdentity((1,3,6,1,4,1,34300,3,4))
_Mc240TrapTypes_ObjectIdentity=ObjectIdentity
mc240TrapTypes=_Mc240TrapTypes_ObjectIdentity((1,3,6,1,4,1,34300,3,5))
_McTrapExState_Type=Integer32
_McTrapExState_Object=MibScalar
mcTrapExState=_McTrapExState_Object((1,3,6,1,4,1,34300,3,5,1),_McTrapExState_Type())
mcTrapExState.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapExState.setStatus(_B)
_McTrapLParam1_Type=Integer32
_McTrapLParam1_Object=MibScalar
mcTrapLParam1=_McTrapLParam1_Object((1,3,6,1,4,1,34300,3,5,2),_McTrapLParam1_Type())
mcTrapLParam1.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapLParam1.setStatus(_B)
_McTrapLParam2_Type=Integer32
_McTrapLParam2_Object=MibScalar
mcTrapLParam2=_McTrapLParam2_Object((1,3,6,1,4,1,34300,3,5,3),_McTrapLParam2_Type())
mcTrapLParam2.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapLParam2.setStatus(_B)
_McTrapLParam3_Type=Integer32
_McTrapLParam3_Object=MibScalar
mcTrapLParam3=_McTrapLParam3_Object((1,3,6,1,4,1,34300,3,5,4),_McTrapLParam3_Type())
mcTrapLParam3.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapLParam3.setStatus(_B)
_McTrapID_Type=Integer32
_McTrapID_Object=MibScalar
mcTrapID=_McTrapID_Object((1,3,6,1,4,1,34300,3,5,5),_McTrapID_Type())
mcTrapID.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapID.setStatus(_B)
class _McTrapDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_McTrapDescr_Type.__name__=_P
_McTrapDescr_Object=MibScalar
mcTrapDescr=_McTrapDescr_Object((1,3,6,1,4,1,34300,3,5,6),_McTrapDescr_Type())
mcTrapDescr.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapDescr.setStatus(_B)
_McTrapRestoredAlarmID_Type=Integer32
_McTrapRestoredAlarmID_Object=MibScalar
mcTrapRestoredAlarmID=_McTrapRestoredAlarmID_Object((1,3,6,1,4,1,34300,3,5,7),_McTrapRestoredAlarmID_Type())
mcTrapRestoredAlarmID.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapRestoredAlarmID.setStatus(_B)
_McTrapSyncType_Type=Integer32
_McTrapSyncType_Object=MibScalar
mcTrapSyncType=_McTrapSyncType_Object((1,3,6,1,4,1,34300,3,5,8),_McTrapSyncType_Type())
mcTrapSyncType.setMaxAccess(_O)
if mibBuilder.loadTexts:mcTrapSyncType.setStatus(_B)
_McReservedFlag_Type=Integer32
_McReservedFlag_Object=MibScalar
mcReservedFlag=_McReservedFlag_Object((1,3,6,1,4,1,34300,3,5,9),_McReservedFlag_Type())
mcReservedFlag.setMaxAccess(_O)
if mibBuilder.loadTexts:mcReservedFlag.setStatus(_B)
_Mp800mkAlarmTraps_ObjectIdentity=ObjectIdentity
mp800mkAlarmTraps=_Mp800mkAlarmTraps_ObjectIdentity((1,3,6,1,4,1,34300,3,8))
_Mp800mkOkTraps_ObjectIdentity=ObjectIdentity
mp800mkOkTraps=_Mp800mkOkTraps_ObjectIdentity((1,3,6,1,4,1,34300,3,9))
_Mp800mkTrapTypes_ObjectIdentity=ObjectIdentity
mp800mkTrapTypes=_Mp800mkTrapTypes_ObjectIdentity((1,3,6,1,4,1,34300,3,10))
_Mp800mkTrapParameter_Type=DisplayString
_Mp800mkTrapParameter_Object=MibScalar
mp800mkTrapParameter=_Mp800mkTrapParameter_Object((1,3,6,1,4,1,34300,3,10,1),_Mp800mkTrapParameter_Type())
mp800mkTrapParameter.setMaxAccess(_O)
if mibBuilder.loadTexts:mp800mkTrapParameter.setStatus(_B)
_Mp800mkTrapValue_Type=DisplayString
_Mp800mkTrapValue_Object=MibScalar
mp800mkTrapValue=_Mp800mkTrapValue_Object((1,3,6,1,4,1,34300,3,10,2),_Mp800mkTrapValue_Type())
mp800mkTrapValue.setMaxAccess(_O)
if mibBuilder.loadTexts:mp800mkTrapValue.setStatus(_B)
_Mp800mkTrapComment_Type=DisplayString
_Mp800mkTrapComment_Object=MibScalar
mp800mkTrapComment=_Mp800mkTrapComment_Object((1,3,6,1,4,1,34300,3,10,3),_Mp800mkTrapComment_Type())
mp800mkTrapComment.setMaxAccess(_O)
if mibBuilder.loadTexts:mp800mkTrapComment.setStatus(_B)
_OmsOperationAlarmTraps_ObjectIdentity=ObjectIdentity
omsOperationAlarmTraps=_OmsOperationAlarmTraps_ObjectIdentity((1,3,6,1,4,1,34300,3,20))
_OmsOperationOkTraps_ObjectIdentity=ObjectIdentity
omsOperationOkTraps=_OmsOperationOkTraps_ObjectIdentity((1,3,6,1,4,1,34300,3,21))
eltrapObjectGroup=ObjectGroup((1,3,6,1,4,1,34300,3,101))
eltrapObjectGroup.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:eltrapObjectGroup.setStatus(_B)
mc240StreamAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,1))
mc240StreamAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240StreamAlarmTrap.setStatus(_B)
mc240SyncAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,2))
mc240SyncAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240SyncAlarmTrap.setStatus(_B)
mc240ss7LinkAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,3))
mc240ss7LinkAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240ss7LinkAlarmTrap.setStatus(_B)
mc240ss7LinksetAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,4))
mc240ss7LinksetAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240ss7LinksetAlarmTrap.setStatus(_B)
mc240FileAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,5))
mc240FileAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240FileAlarmTrap.setStatus(_B)
mc240CardAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,6))
mc240CardAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240CardAlarmTrap.setStatus(_B)
mxlDPSAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,7))
mxlDPSAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:mxlDPSAlarmTrap.setStatus(_B)
mxlTELEAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,8))
mxlTELEAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:mxlTELEAlarmTrap.setStatus(_B)
mc240UPSAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,9))
mc240UPSAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240UPSAlarmTrap.setStatus(_B)
mc240SensAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,10))
mc240SensAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240SensAlarmTrap.setStatus(_B)
dslamLinkDownTrap=NotificationType((1,3,6,1,4,1,34300,3,3,11))
dslamLinkDownTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamLinkDownTrap.setStatus(_B)
dslamDSRateAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,12))
dslamDSRateAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamDSRateAlarmTrap.setStatus(_B)
dslamUSRateAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,13))
dslamUSRateAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamUSRateAlarmTrap.setStatus(_B)
ponONUAuthAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,14))
ponONUAuthAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ponONUAuthAlarmTrap.setStatus(_B)
ponEthAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,15))
ponEthAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ponEthAlarmTrap.setStatus(_B)
ponOpticalAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,16))
ponOpticalAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ponOpticalAlarmTrap.setStatus(_B)
dslamOverheatAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,17))
dslamOverheatAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamOverheatAlarmTrap.setStatus(_B)
dslamVoltageAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,18))
dslamVoltageAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamVoltageAlarmTrap.setStatus(_B)
dslamSessionAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,19))
dslamSessionAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamSessionAlarmTrap.setStatus(_B)
dslamEthLinkAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,3,20))
dslamEthLinkAlarmTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamEthLinkAlarmTrap.setStatus(_B)
mc240StreamOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,1))
mc240StreamOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240StreamOkTrap.setStatus(_B)
mc240SyncOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,2))
mc240SyncOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240SyncOkTrap.setStatus(_B)
mc240ss7LinkOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,3))
mc240ss7LinkOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240ss7LinkOkTrap.setStatus(_B)
mc240ss7LinksetOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,4))
mc240ss7LinksetOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240ss7LinksetOkTrap.setStatus(_B)
mc240FileOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,5))
mc240FileOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240FileOkTrap.setStatus(_B)
mc240CardOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,6))
mc240CardOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240CardOkTrap.setStatus(_B)
mxlDPSOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,7))
mxlDPSOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:mxlDPSOkTrap.setStatus(_B)
mxlTELEOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,8))
mxlTELEOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:mxlTELEOkTrap.setStatus(_B)
mc240UPSOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,9))
mc240UPSOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240UPSOkTrap.setStatus(_B)
mc240SensOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,10))
mc240SensOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mc240SensOkTrap.setStatus(_B)
dslamLinkUpTrap=NotificationType((1,3,6,1,4,1,34300,3,4,11))
dslamLinkUpTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamLinkUpTrap.setStatus(_B)
dslamDSRateOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,12))
dslamDSRateOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamDSRateOkTrap.setStatus(_B)
dslamUSRateOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,13))
dslamUSRateOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamUSRateOkTrap.setStatus(_B)
ponONUAuthOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,14))
ponONUAuthOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ponONUAuthOkTrap.setStatus(_B)
ponEthOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,15))
ponEthOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ponEthOkTrap.setStatus(_B)
ponOpticalOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,16))
ponOpticalOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ponOpticalOkTrap.setStatus(_B)
dslamOverheatOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,17))
dslamOverheatOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamOverheatOkTrap.setStatus(_B)
dslamVoltageOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,18))
dslamVoltageOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamVoltageOkTrap.setStatus(_B)
dslamSessionOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,19))
dslamSessionOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamSessionOkTrap.setStatus(_B)
dslamEthLinkOkTrap=NotificationType((1,3,6,1,4,1,34300,3,4,20))
dslamEthLinkOkTrap.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:dslamEthLinkOkTrap.setStatus(_B)
mp800mkMPStatusAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,1))
mp800mkMPStatusAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkMPStatusAlarmTrap.setStatus(_B)
mp800mkInpParmAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,2))
mp800mkInpParmAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkInpParmAlarmTrap.setStatus(_B)
mp800mkUEPConfAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,3))
mp800mkUEPConfAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkUEPConfAlarmTrap.setStatus(_B)
mp800mkTMAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,4))
mp800mkTMAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkTMAlarmTrap.setStatus(_B)
mp800mkACVMAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,5))
mp800mkACVMAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkACVMAlarmTrap.setStatus(_B)
mp800mkIbatMAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,6))
mp800mkIbatMAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkIbatMAlarmTrap.setStatus(_B)
mp800mkVbatMAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,7))
mp800mkVbatMAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkVbatMAlarmTrap.setStatus(_B)
mp800mkVbatChAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,8))
mp800mkVbatChAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkVbatChAlarmTrap.setStatus(_B)
mp800mkRlsDevAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,9))
mp800mkRlsDevAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkRlsDevAlarmTrap.setStatus(_B)
mp800mkDVcellAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,10))
mp800mkDVcellAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkDVcellAlarmTrap.setStatus(_B)
mp800mkACVAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,11))
mp800mkACVAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkACVAlarmTrap.setStatus(_B)
mp800mkBatChargeAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,12))
mp800mkBatChargeAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkBatChargeAlarmTrap.setStatus(_B)
mp800mkIloadAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,13))
mp800mkIloadAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkIloadAlarmTrap.setStatus(_B)
mp800mkIbatChAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,14))
mp800mkIbatChAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkIbatChAlarmTrap.setStatus(_B)
mp800mkSuppAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,15))
mp800mkSuppAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkSuppAlarmTrap.setStatus(_B)
mp800mkBatConnAlarmTrap=NotificationType((1,3,6,1,4,1,34300,3,8,16))
mp800mkBatConnAlarmTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkBatConnAlarmTrap.setStatus(_B)
mp800mkMPStatusOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,1))
mp800mkMPStatusOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkMPStatusOkTrap.setStatus(_B)
mp800mkInpParmOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,2))
mp800mkInpParmOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkInpParmOkTrap.setStatus(_B)
mp800mkUEPConfOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,3))
mp800mkUEPConfOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkUEPConfOkTrap.setStatus(_B)
mp800mkTMOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,4))
mp800mkTMOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkTMOkTrap.setStatus(_B)
mp800mkACVMOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,5))
mp800mkACVMOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkACVMOkTrap.setStatus(_B)
mp800mkIbatMOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,6))
mp800mkIbatMOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkIbatMOkTrap.setStatus(_B)
mp800mkVbatMOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,7))
mp800mkVbatMOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkVbatMOkTrap.setStatus(_B)
mp800mkVbatChOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,8))
mp800mkVbatChOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkVbatChOkTrap.setStatus(_B)
mp800mkRlsDevOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,9))
mp800mkRlsDevOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkRlsDevOkTrap.setStatus(_B)
mp800mkDVcellOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,10))
mp800mkDVcellOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkDVcellOkTrap.setStatus(_B)
mp800mkACVOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,11))
mp800mkACVOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkACVOkTrap.setStatus(_B)
mp800mkBatChargeOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,12))
mp800mkBatChargeOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkBatChargeOkTrap.setStatus(_B)
mp800mkIloadOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,13))
mp800mkIloadOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkIloadOkTrap.setStatus(_B)
mp800mkIbatChOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,14))
mp800mkIbatChOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkIbatChOkTrap.setStatus(_B)
mp800mkSuppOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,15))
mp800mkSuppOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkSuppOkTrap.setStatus(_B)
mp800mkBatConnOkTrap=NotificationType((1,3,6,1,4,1,34300,3,9,16))
mp800mkBatConnOkTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:mp800mkBatConnOkTrap.setStatus(_B)
omsOperationCommandAlarm=NotificationType((1,3,6,1,4,1,34300,3,20,1))
omsOperationCommandAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:omsOperationCommandAlarm.setStatus(_B)
omsOperationCommandOk=NotificationType((1,3,6,1,4,1,34300,3,21,1))
omsOperationCommandOk.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:omsOperationCommandOk.setStatus(_B)
eltrapNotificationGroup=NotificationGroup((1,3,6,1,4,1,34300,3,100))
eltrapNotificationGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:eltrapNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'eltex':eltex,'elHardware':elHardware,'elSoftware':elSoftware,'eltrapGroup':eltrapGroup,'mc240AlarmTraps':mc240AlarmTraps,_Q:mc240StreamAlarmTrap,_R:mc240SyncAlarmTrap,_S:mc240ss7LinkAlarmTrap,_T:mc240ss7LinksetAlarmTrap,_U:mc240FileAlarmTrap,_V:mc240CardAlarmTrap,_W:mxlDPSAlarmTrap,_X:mxlTELEAlarmTrap,_Y:mc240UPSAlarmTrap,_Z:mc240SensAlarmTrap,_a:dslamLinkDownTrap,_b:dslamDSRateAlarmTrap,_c:dslamUSRateAlarmTrap,_d:ponONUAuthAlarmTrap,_e:ponEthAlarmTrap,_f:ponOpticalAlarmTrap,_w:dslamOverheatAlarmTrap,_x:dslamVoltageAlarmTrap,_y:dslamSessionAlarmTrap,_z:dslamEthLinkAlarmTrap,'mc240OkTraps':mc240OkTraps,_g:mc240StreamOkTrap,_h:mc240SyncOkTrap,_i:mc240ss7LinkOkTrap,_j:mc240ss7LinksetOkTrap,_k:mc240FileOkTrap,_l:mc240CardOkTrap,_m:mxlDPSOkTrap,_n:mxlTELEOkTrap,_o:mc240UPSOkTrap,_p:mc240SensOkTrap,_q:dslamLinkUpTrap,_r:dslamDSRateOkTrap,_s:dslamUSRateOkTrap,_t:ponONUAuthOkTrap,_u:ponEthOkTrap,_v:ponOpticalOkTrap,_A0:dslamOverheatOkTrap,_A1:dslamVoltageOkTrap,_A2:dslamSessionOkTrap,_A3:dslamEthLinkOkTrap,'mc240TrapTypes':mc240TrapTypes,_C:mcTrapExState,_D:mcTrapLParam1,_E:mcTrapLParam2,_F:mcTrapLParam3,_G:mcTrapID,_H:mcTrapDescr,_L:mcTrapRestoredAlarmID,_M:mcTrapSyncType,_N:mcReservedFlag,'mp800mkAlarmTraps':mp800mkAlarmTraps,_A4:mp800mkMPStatusAlarmTrap,_A5:mp800mkInpParmAlarmTrap,_A6:mp800mkUEPConfAlarmTrap,_A7:mp800mkTMAlarmTrap,_A8:mp800mkACVMAlarmTrap,_A9:mp800mkIbatMAlarmTrap,_AA:mp800mkVbatMAlarmTrap,_AB:mp800mkVbatChAlarmTrap,_AC:mp800mkRlsDevAlarmTrap,_AD:mp800mkDVcellAlarmTrap,_AE:mp800mkACVAlarmTrap,_AF:mp800mkBatChargeAlarmTrap,_AG:mp800mkIloadAlarmTrap,_AH:mp800mkIbatChAlarmTrap,_AI:mp800mkSuppAlarmTrap,_AJ:mp800mkBatConnAlarmTrap,'mp800mkOkTraps':mp800mkOkTraps,_AK:mp800mkMPStatusOkTrap,_AL:mp800mkInpParmOkTrap,_AM:mp800mkUEPConfOkTrap,_AN:mp800mkTMOkTrap,_AO:mp800mkACVMOkTrap,_AP:mp800mkIbatMOkTrap,_AQ:mp800mkVbatMOkTrap,_AR:mp800mkVbatChOkTrap,_AS:mp800mkRlsDevOkTrap,_AT:mp800mkDVcellOkTrap,_AU:mp800mkACVOkTrap,_AV:mp800mkBatChargeOkTrap,_AW:mp800mkIloadOkTrap,_AX:mp800mkIbatChOkTrap,_AY:mp800mkSuppOkTrap,_AZ:mp800mkBatConnOkTrap,'mp800mkTrapTypes':mp800mkTrapTypes,_I:mp800mkTrapParameter,_J:mp800mkTrapValue,_K:mp800mkTrapComment,'omsOperationAlarmTraps':omsOperationAlarmTraps,_Aa:omsOperationCommandAlarm,'omsOperationOkTraps':omsOperationOkTraps,_Ab:omsOperationCommandOk,'eltrapNotificationGroup':eltrapNotificationGroup,'eltrapObjectGroup':eltrapObjectGroup})