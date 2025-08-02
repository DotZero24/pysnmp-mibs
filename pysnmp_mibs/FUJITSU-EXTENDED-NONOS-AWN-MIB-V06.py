_B3='awnStatisticsDlciDlci'
_B2='awnStatisticsDlciTimeslot'
_B1='awnStatisticsDlciPort'
_B0='awnStatisticsDlciCard'
_A_='awnStatisticsDlciUnit'
_Az='awnStatisticsIpFrameAddr'
_Ay='awnStatisticsLsTsTs'
_Ax='awnStatisticsLsTsPort'
_Aw='awnStatisticsLsTsCard'
_Av='awnStatisticsLsTsUnit'
_Au='awnStatisticsComAtmLineVpi'
_At='awnStatisticsComAtmLinePort'
_As='awnStatisticsComAtmLineAdapter'
_Ar='awnStatisticsComAtmLineSlot'
_Aq='awnStatisticsLsWanVpRtType'
_Ap='awnStatisticsLsWanVpRtCategory'
_Ao='awnStatisticsLsWanVpRtVpi'
_An='awnStatisticsLsWanVpRtPort'
_Am='awnStatisticsLsWanVpRtCard'
_Al='awnStatisticsLsWanVpRtUnit'
_Ak='awnStatisticsLsWanVpVpi'
_Aj='awnStatisticsLsWanVpPort'
_Ai='awnStatisticsLsWanVpCard'
_Ah='awnStatisticsLsWanVpUnit'
_Ag='awnStatisticsVccFfLineType'
_Af='awnStatisticsVccFfLineTimeslot'
_Ae='awnStatisticsVccFfLinePort'
_Ad='awnStatisticsVccFfLineCard'
_Ac='awnStatisticsVccFfLineUnit'
_Ab='awnStatisticsVccFrLineType'
_Aa='awnStatisticsVccFrLineDlci'
_AZ='awnStatisticsVccFrLineTimeslot'
_AY='awnStatisticsVccFrLinePort'
_AX='awnStatisticsVccFrLineCard'
_AW='awnStatisticsVccFrLineUnit'
_AV='awnStatisticsVccWanTsType'
_AU='awnStatisticsVccWanTsVci'
_AT='awnStatisticsVccWanTsVpi'
_AS='awnStatisticsVccWanTsTs'
_AR='awnStatisticsVccWanTsPort'
_AQ='awnStatisticsVccWanTsCard'
_AP='awnStatisticsVccWanTsUnit'
_AO='awnStatisticsVpcAtmLineType'
_AN='awnStatisticsVpcAtmLineVpi'
_AM='awnStatisticsVpcAtmLinePort'
_AL='awnStatisticsVpcAtmLineAdapter'
_AK='awnStatisticsVpcAtmLineSlot'
_AJ='awnStatisticsVccAtmLineType'
_AI='awnStatisticsVccAtmLineVci'
_AH='awnStatisticsVccAtmLineVpi'
_AG='awnStatisticsVccAtmLinePort'
_AF='awnStatisticsVccAtmLineAdapter'
_AE='awnStatisticsVccAtmLineSlot'
_AD='awnStatisticsLsWanTsRtType'
_AC='awnStatisticsLsWanTsRtCategory'
_AB='awnStatisticsLsWanTsRtTs'
_AA='awnStatisticsLsWanTsRtPort'
_A9='awnStatisticsLsWanTsRtCard'
_A8='awnStatisticsLsWanTsRtUnit'
_A7='awnStatisticsComNniVpRtType'
_A6='awnStatisticsComNniVpRtCategory'
_A5='awnStatisticsComNniVpRtVpi'
_A4='awnStatisticsComNniVpRtPort'
_A3='awnStatisticsComNniVpRtAdapter'
_A2='awnStatisticsComNniVpRtSlot'
_A1='awnStatisticsComNniPortRtType'
_A0='awnStatisticsComNniPortRtCategory'
_z='awnStatisticsComNniPortRtPort'
_y='awnStatisticsComNniPortRtAdapter'
_x='awnStatisticsComNniPortRtSlot'
_w='awnStatisticsLsWanTsTs'
_v='awnStatisticsLsWanTsPort'
_u='awnStatisticsLsWanTsCard'
_t='awnStatisticsLsWanTsUnit'
_s='awnStatisticsComNniVpVpi'
_r='awnStatisticsComNniVpPort'
_q='awnStatisticsComNniVpAdapter'
_p='awnStatisticsComNniVpSlot'
_o='awnStatisticsComNniPortPort'
_n='awnStatisticsComNniPortAdapter'
_m='awnStatisticsComNniPortSlot'
_l='awnStatisticsLsLinePort'
_k='awnStatisticsLsLineCard'
_j='awnStatisticsLsLineUnit'
_i='awnStatisticsComLinePort'
_h='awnStatisticsComLineAdapter'
_g='awnStatisticsComLineSlot'
_f='awnStatisticsLinePort'
_e='awnStatisticsLineCard'
_d='awnStatisticsLineUnit'
_c='awnSysConnLsVccVci'
_b='awnSysConnLsVccVpi'
_a='awnSysConnLsVccTimeslot'
_Z='awnSysConnLsVccPort'
_Y='awnSysConnLsVccUnit'
_X='awnSysConnComVccVci'
_W='awnSysConnComVccVpi'
_V='awnSysConnComVccPort'
_U='awnSysConnComVccAdapter'
_T='awnSysConnComVccSlot'
_S='awnSysPortPort'
_R='awnSysPortAdapter'
_Q='awnSysPortSlot'
_P='awnSysChannelTimeslot'
_O='awnSysChannelPort'
_N='awnSysChannelCard'
_M='awnSysChannelUnit'
_L='awnSysLinePort'
_K='awnSysLineCard'
_J='awnSysLineUnit'
_I='awnSysLsUnit'
_H='not-accessible'
_G='obsolete'
_F='Gauge32'
_E='OctetString'
_D='Integer32'
_C='FUJITSU-EXTENDED-NONOS-AWN-MIB-V06'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_F,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Fujitsu_ObjectIdentity=ObjectIdentity
fujitsu=_Fujitsu_ObjectIdentity((1,3,6,1,4,1,211))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,211,1))
_Nonos_ObjectIdentity=ObjectIdentity
nonos=_Nonos_ObjectIdentity((1,3,6,1,4,1,211,1,127))
_Awn_ObjectIdentity=ObjectIdentity
awn=_Awn_ObjectIdentity((1,3,6,1,4,1,211,1,127,29))
_AwnSystem_ObjectIdentity=ObjectIdentity
awnSystem=_AwnSystem_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1))
_AwnSysNode_ObjectIdentity=ObjectIdentity
awnSysNode=_AwnSysNode_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,1))
class _AwnSysNodeInformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_AwnSysNodeInformation_Type.__name__=_E
_AwnSysNodeInformation_Object=MibScalar
awnSysNodeInformation=_AwnSysNodeInformation_Object((1,3,6,1,4,1,211,1,127,29,1,1,1),_AwnSysNodeInformation_Type())
awnSysNodeInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysNodeInformation.setStatus(_A)
class _AwnSysNodeCommonStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_AwnSysNodeCommonStatus_Type.__name__=_E
_AwnSysNodeCommonStatus_Object=MibScalar
awnSysNodeCommonStatus=_AwnSysNodeCommonStatus_Object((1,3,6,1,4,1,211,1,127,29,1,1,2),_AwnSysNodeCommonStatus_Type())
awnSysNodeCommonStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysNodeCommonStatus.setStatus(_A)
class _AwnSysNodeClk_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AwnSysNodeClk_Type.__name__=_E
_AwnSysNodeClk_Object=MibScalar
awnSysNodeClk=_AwnSysNodeClk_Object((1,3,6,1,4,1,211,1,127,29,1,1,3),_AwnSysNodeClk_Type())
awnSysNodeClk.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysNodeClk.setStatus(_A)
_AwnSysCom_ObjectIdentity=ObjectIdentity
awnSysCom=_AwnSysCom_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,2))
class _AwnSysComDevice_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(80,80));fixedLength=80
_AwnSysComDevice_Type.__name__=_E
_AwnSysComDevice_Object=MibScalar
awnSysComDevice=_AwnSysComDevice_Object((1,3,6,1,4,1,211,1,127,29,1,2,1),_AwnSysComDevice_Type())
awnSysComDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysComDevice.setStatus(_A)
class _AwnSysComPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(192,192));fixedLength=192
_AwnSysComPort_Type.__name__=_E
_AwnSysComPort_Object=MibScalar
awnSysComPort=_AwnSysComPort_Object((1,3,6,1,4,1,211,1,127,29,1,2,2),_AwnSysComPort_Type())
awnSysComPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysComPort.setStatus(_A)
class _AwnSysComDevice2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(68,68));fixedLength=68
_AwnSysComDevice2_Type.__name__=_E
_AwnSysComDevice2_Object=MibScalar
awnSysComDevice2=_AwnSysComDevice2_Object((1,3,6,1,4,1,211,1,127,29,1,2,3),_AwnSysComDevice2_Type())
awnSysComDevice2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysComDevice2.setStatus(_A)
class _AwnSysComPort2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(120,120));fixedLength=120
_AwnSysComPort2_Type.__name__=_E
_AwnSysComPort2_Object=MibScalar
awnSysComPort2=_AwnSysComPort2_Object((1,3,6,1,4,1,211,1,127,29,1,2,4),_AwnSysComPort2_Type())
awnSysComPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysComPort2.setStatus(_A)
_AwnSysLs_ObjectIdentity=ObjectIdentity
awnSysLs=_AwnSysLs_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,3))
_AwnSysLsTable_Object=MibTable
awnSysLsTable=_AwnSysLsTable_Object((1,3,6,1,4,1,211,1,127,29,1,3,1))
if mibBuilder.loadTexts:awnSysLsTable.setStatus(_A)
_AwnSysLsEntry_Object=MibTableRow
awnSysLsEntry=_AwnSysLsEntry_Object((1,3,6,1,4,1,211,1,127,29,1,3,1,1))
awnSysLsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:awnSysLsEntry.setStatus(_A)
class _AwnSysLsUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnSysLsUnit_Type.__name__=_D
_AwnSysLsUnit_Object=MibTableColumn
awnSysLsUnit=_AwnSysLsUnit_Object((1,3,6,1,4,1,211,1,127,29,1,3,1,1,1),_AwnSysLsUnit_Type())
awnSysLsUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLsUnit.setStatus(_A)
class _AwnSysLsDevice_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_AwnSysLsDevice_Type.__name__=_E
_AwnSysLsDevice_Object=MibTableColumn
awnSysLsDevice=_AwnSysLsDevice_Object((1,3,6,1,4,1,211,1,127,29,1,3,1,1,2),_AwnSysLsDevice_Type())
awnSysLsDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLsDevice.setStatus(_A)
class _AwnSysLsPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(560,560));fixedLength=560
_AwnSysLsPort_Type.__name__=_E
_AwnSysLsPort_Object=MibTableColumn
awnSysLsPort=_AwnSysLsPort_Object((1,3,6,1,4,1,211,1,127,29,1,3,1,1,3),_AwnSysLsPort_Type())
awnSysLsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLsPort.setStatus(_A)
class _AwnSysLsDevice2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(80,80));fixedLength=80
_AwnSysLsDevice2_Type.__name__=_E
_AwnSysLsDevice2_Object=MibScalar
awnSysLsDevice2=_AwnSysLsDevice2_Object((1,3,6,1,4,1,211,1,127,29,1,3,1,1,4),_AwnSysLsDevice2_Type())
awnSysLsDevice2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLsDevice2.setStatus(_A)
class _AwnSysLsPort2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(720,720));fixedLength=720
_AwnSysLsPort2_Type.__name__=_E
_AwnSysLsPort2_Object=MibScalar
awnSysLsPort2=_AwnSysLsPort2_Object((1,3,6,1,4,1,211,1,127,29,1,3,1,1,5),_AwnSysLsPort2_Type())
awnSysLsPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLsPort2.setStatus(_A)
_AwnSysLine_ObjectIdentity=ObjectIdentity
awnSysLine=_AwnSysLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,4))
_AwnSysLineTable_Object=MibTable
awnSysLineTable=_AwnSysLineTable_Object((1,3,6,1,4,1,211,1,127,29,1,4,1))
if mibBuilder.loadTexts:awnSysLineTable.setStatus(_A)
_AwnSysLineEntry_Object=MibTableRow
awnSysLineEntry=_AwnSysLineEntry_Object((1,3,6,1,4,1,211,1,127,29,1,4,1,1))
awnSysLineEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:awnSysLineEntry.setStatus(_A)
class _AwnSysLineUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnSysLineUnit_Type.__name__=_D
_AwnSysLineUnit_Object=MibTableColumn
awnSysLineUnit=_AwnSysLineUnit_Object((1,3,6,1,4,1,211,1,127,29,1,4,1,1,1),_AwnSysLineUnit_Type())
awnSysLineUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLineUnit.setStatus(_A)
class _AwnSysLineCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnSysLineCard_Type.__name__=_D
_AwnSysLineCard_Object=MibTableColumn
awnSysLineCard=_AwnSysLineCard_Object((1,3,6,1,4,1,211,1,127,29,1,4,1,1,2),_AwnSysLineCard_Type())
awnSysLineCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLineCard.setStatus(_A)
class _AwnSysLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnSysLinePort_Type.__name__=_D
_AwnSysLinePort_Object=MibTableColumn
awnSysLinePort=_AwnSysLinePort_Object((1,3,6,1,4,1,211,1,127,29,1,4,1,1,3),_AwnSysLinePort_Type())
awnSysLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLinePort.setStatus(_A)
class _AwnSysLineChannel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(384,384));fixedLength=384
_AwnSysLineChannel_Type.__name__=_E
_AwnSysLineChannel_Object=MibTableColumn
awnSysLineChannel=_AwnSysLineChannel_Object((1,3,6,1,4,1,211,1,127,29,1,4,1,1,4),_AwnSysLineChannel_Type())
awnSysLineChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLineChannel.setStatus(_A)
class _AwnSysLineMegalink_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_AwnSysLineMegalink_Type.__name__=_E
_AwnSysLineMegalink_Object=MibTableColumn
awnSysLineMegalink=_AwnSysLineMegalink_Object((1,3,6,1,4,1,211,1,127,29,1,4,1,1,5),_AwnSysLineMegalink_Type())
awnSysLineMegalink.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysLineMegalink.setStatus(_A)
_AwnSysError_ObjectIdentity=ObjectIdentity
awnSysError=_AwnSysError_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,5))
_AwnSysErrorLog_Type=DisplayString
_AwnSysErrorLog_Object=MibScalar
awnSysErrorLog=_AwnSysErrorLog_Object((1,3,6,1,4,1,211,1,127,29,1,5,1),_AwnSysErrorLog_Type())
awnSysErrorLog.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysErrorLog.setStatus(_A)
_AwnSysChannel_ObjectIdentity=ObjectIdentity
awnSysChannel=_AwnSysChannel_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,6))
_AwnSysChannelTable_Object=MibTable
awnSysChannelTable=_AwnSysChannelTable_Object((1,3,6,1,4,1,211,1,127,29,1,6,1))
if mibBuilder.loadTexts:awnSysChannelTable.setStatus(_A)
_AwnSysChannelEntry_Object=MibTableRow
awnSysChannelEntry=_AwnSysChannelEntry_Object((1,3,6,1,4,1,211,1,127,29,1,6,1,1))
awnSysChannelEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:awnSysChannelEntry.setStatus(_A)
class _AwnSysChannelUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnSysChannelUnit_Type.__name__=_D
_AwnSysChannelUnit_Object=MibTableColumn
awnSysChannelUnit=_AwnSysChannelUnit_Object((1,3,6,1,4,1,211,1,127,29,1,6,1,1,1),_AwnSysChannelUnit_Type())
awnSysChannelUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysChannelUnit.setStatus(_A)
class _AwnSysChannelCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnSysChannelCard_Type.__name__=_D
_AwnSysChannelCard_Object=MibTableColumn
awnSysChannelCard=_AwnSysChannelCard_Object((1,3,6,1,4,1,211,1,127,29,1,6,1,1,2),_AwnSysChannelCard_Type())
awnSysChannelCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysChannelCard.setStatus(_A)
class _AwnSysChannelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnSysChannelPort_Type.__name__=_D
_AwnSysChannelPort_Object=MibTableColumn
awnSysChannelPort=_AwnSysChannelPort_Object((1,3,6,1,4,1,211,1,127,29,1,6,1,1,3),_AwnSysChannelPort_Type())
awnSysChannelPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysChannelPort.setStatus(_A)
class _AwnSysChannelTimeslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AwnSysChannelTimeslot_Type.__name__=_D
_AwnSysChannelTimeslot_Object=MibTableColumn
awnSysChannelTimeslot=_AwnSysChannelTimeslot_Object((1,3,6,1,4,1,211,1,127,29,1,6,1,1,4),_AwnSysChannelTimeslot_Type())
awnSysChannelTimeslot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysChannelTimeslot.setStatus(_A)
class _AwnSysChannelBackup_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(576,576));fixedLength=576
_AwnSysChannelBackup_Type.__name__=_E
_AwnSysChannelBackup_Object=MibTableColumn
awnSysChannelBackup=_AwnSysChannelBackup_Object((1,3,6,1,4,1,211,1,127,29,1,6,1,1,5),_AwnSysChannelBackup_Type())
awnSysChannelBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysChannelBackup.setStatus(_A)
class _AwnSysChannelBackup2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_AwnSysChannelBackup2_Type.__name__=_E
_AwnSysChannelBackup2_Object=MibTableColumn
awnSysChannelBackup2=_AwnSysChannelBackup2_Object((1,3,6,1,4,1,211,1,127,29,1,6,1,1,6),_AwnSysChannelBackup2_Type())
awnSysChannelBackup2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysChannelBackup2.setStatus(_A)
_AwnSysEvent_ObjectIdentity=ObjectIdentity
awnSysEvent=_AwnSysEvent_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,7))
_AwnSysEventTable_Object=MibTable
awnSysEventTable=_AwnSysEventTable_Object((1,3,6,1,4,1,211,1,127,29,1,7,1))
if mibBuilder.loadTexts:awnSysEventTable.setStatus(_A)
_AwnSysEventEntry_Object=MibTableRow
awnSysEventEntry=_AwnSysEventEntry_Object((1,3,6,1,4,1,211,1,127,29,1,7,1,1))
if mibBuilder.loadTexts:awnSysEventEntry.setStatus(_A)
_AwnSysEventThreshold_Type=DisplayString
_AwnSysEventThreshold_Object=MibTableColumn
awnSysEventThreshold=_AwnSysEventThreshold_Object((1,3,6,1,4,1,211,1,127,29,1,7,1,1,1),_AwnSysEventThreshold_Type())
awnSysEventThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:awnSysEventThreshold.setStatus(_A)
_AwnSysPort_ObjectIdentity=ObjectIdentity
awnSysPort=_AwnSysPort_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,8))
_AwnSysPortTable_Object=MibTable
awnSysPortTable=_AwnSysPortTable_Object((1,3,6,1,4,1,211,1,127,29,1,8,1))
if mibBuilder.loadTexts:awnSysPortTable.setStatus(_A)
_AwnSysPortEntry_Object=MibTableRow
awnSysPortEntry=_AwnSysPortEntry_Object((1,3,6,1,4,1,211,1,127,29,1,8,1,1))
awnSysPortEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:awnSysPortEntry.setStatus(_A)
class _AwnSysPortSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnSysPortSlot_Type.__name__=_D
_AwnSysPortSlot_Object=MibTableColumn
awnSysPortSlot=_AwnSysPortSlot_Object((1,3,6,1,4,1,211,1,127,29,1,8,1,1,1),_AwnSysPortSlot_Type())
awnSysPortSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysPortSlot.setStatus(_A)
class _AwnSysPortAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnSysPortAdapter_Type.__name__=_D
_AwnSysPortAdapter_Object=MibTableColumn
awnSysPortAdapter=_AwnSysPortAdapter_Object((1,3,6,1,4,1,211,1,127,29,1,8,1,1,2),_AwnSysPortAdapter_Type())
awnSysPortAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysPortAdapter.setStatus(_A)
class _AwnSysPortPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnSysPortPort_Type.__name__=_D
_AwnSysPortPort_Object=MibTableColumn
awnSysPortPort=_AwnSysPortPort_Object((1,3,6,1,4,1,211,1,127,29,1,8,1,1,3),_AwnSysPortPort_Type())
awnSysPortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysPortPort.setStatus(_A)
class _AwnSysPortMegalink_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(244,244));fixedLength=244
_AwnSysPortMegalink_Type.__name__=_E
_AwnSysPortMegalink_Object=MibTableColumn
awnSysPortMegalink=_AwnSysPortMegalink_Object((1,3,6,1,4,1,211,1,127,29,1,8,1,1,4),_AwnSysPortMegalink_Type())
awnSysPortMegalink.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysPortMegalink.setStatus(_A)
class _AwnSysPortMegalink2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_AwnSysPortMegalink2_Type.__name__=_E
_AwnSysPortMegalink2_Object=MibTableColumn
awnSysPortMegalink2=_AwnSysPortMegalink2_Object((1,3,6,1,4,1,211,1,127,29,1,8,1,1,5),_AwnSysPortMegalink2_Type())
awnSysPortMegalink2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysPortMegalink2.setStatus(_A)
_AwnSysConnComVcc_ObjectIdentity=ObjectIdentity
awnSysConnComVcc=_AwnSysConnComVcc_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,9))
_AwnSysConnComVccTable_Object=MibTable
awnSysConnComVccTable=_AwnSysConnComVccTable_Object((1,3,6,1,4,1,211,1,127,29,1,9,1))
if mibBuilder.loadTexts:awnSysConnComVccTable.setStatus(_A)
_AwnSysConnComVccEntry_Object=MibTableRow
awnSysConnComVccEntry=_AwnSysConnComVccEntry_Object((1,3,6,1,4,1,211,1,127,29,1,9,1,1))
awnSysConnComVccEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_V),(0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:awnSysConnComVccEntry.setStatus(_A)
class _AwnSysConnComVccSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnSysConnComVccSlot_Type.__name__=_D
_AwnSysConnComVccSlot_Object=MibTableColumn
awnSysConnComVccSlot=_AwnSysConnComVccSlot_Object((1,3,6,1,4,1,211,1,127,29,1,9,1,1,1),_AwnSysConnComVccSlot_Type())
awnSysConnComVccSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnComVccSlot.setStatus(_A)
class _AwnSysConnComVccAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnSysConnComVccAdapter_Type.__name__=_D
_AwnSysConnComVccAdapter_Object=MibTableColumn
awnSysConnComVccAdapter=_AwnSysConnComVccAdapter_Object((1,3,6,1,4,1,211,1,127,29,1,9,1,1,2),_AwnSysConnComVccAdapter_Type())
awnSysConnComVccAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnComVccAdapter.setStatus(_A)
class _AwnSysConnComVccPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnSysConnComVccPort_Type.__name__=_D
_AwnSysConnComVccPort_Object=MibTableColumn
awnSysConnComVccPort=_AwnSysConnComVccPort_Object((1,3,6,1,4,1,211,1,127,29,1,9,1,1,3),_AwnSysConnComVccPort_Type())
awnSysConnComVccPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnComVccPort.setStatus(_A)
class _AwnSysConnComVccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AwnSysConnComVccVpi_Type.__name__=_D
_AwnSysConnComVccVpi_Object=MibTableColumn
awnSysConnComVccVpi=_AwnSysConnComVccVpi_Object((1,3,6,1,4,1,211,1,127,29,1,9,1,1,4),_AwnSysConnComVccVpi_Type())
awnSysConnComVccVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnComVccVpi.setStatus(_A)
class _AwnSysConnComVccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AwnSysConnComVccVci_Type.__name__=_D
_AwnSysConnComVccVci_Object=MibTableColumn
awnSysConnComVccVci=_AwnSysConnComVccVci_Object((1,3,6,1,4,1,211,1,127,29,1,9,1,1,5),_AwnSysConnComVccVci_Type())
awnSysConnComVccVci.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnComVccVci.setStatus(_A)
class _AwnSysConnComVccState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(100,100));fixedLength=100
_AwnSysConnComVccState_Type.__name__=_E
_AwnSysConnComVccState_Object=MibTableColumn
awnSysConnComVccState=_AwnSysConnComVccState_Object((1,3,6,1,4,1,211,1,127,29,1,9,1,1,6),_AwnSysConnComVccState_Type())
awnSysConnComVccState.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnComVccState.setStatus(_A)
_AwnSysConnLsVcc_ObjectIdentity=ObjectIdentity
awnSysConnLsVcc=_AwnSysConnLsVcc_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,10))
_AwnSysConnLsVccTable_Object=MibTable
awnSysConnLsVccTable=_AwnSysConnLsVccTable_Object((1,3,6,1,4,1,211,1,127,29,1,10,1))
if mibBuilder.loadTexts:awnSysConnLsVccTable.setStatus(_A)
_AwnSysConnLsVccEntry_Object=MibTableRow
awnSysConnLsVccEntry=_AwnSysConnLsVccEntry_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1))
awnSysConnLsVccEntry.setIndexNames((0,_C,'awnSysConnLsVccSlot'),(0,_C,_Y),(0,_C,'awnSysConnLsVccCard'),(0,_C,_Z),(0,_C,_a),(0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:awnSysConnLsVccEntry.setStatus(_A)
class _AwnSysConnLsVccUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnSysConnLsVccUnit_Type.__name__=_D
_AwnSysConnLsVccUnit_Object=MibTableColumn
awnSysConnLsVccUnit=_AwnSysConnLsVccUnit_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1,1),_AwnSysConnLsVccUnit_Type())
awnSysConnLsVccUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnLsVccUnit.setStatus(_A)
class _AwnSysConnLSVccCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnSysConnLSVccCard_Type.__name__=_D
_AwnSysConnLSVccCard_Object=MibScalar
awnSysConnLSVccCard=_AwnSysConnLSVccCard_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1,2),_AwnSysConnLSVccCard_Type())
awnSysConnLSVccCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnLSVccCard.setStatus(_A)
class _AwnSysConnLsVccPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnSysConnLsVccPort_Type.__name__=_D
_AwnSysConnLsVccPort_Object=MibTableColumn
awnSysConnLsVccPort=_AwnSysConnLsVccPort_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1,3),_AwnSysConnLsVccPort_Type())
awnSysConnLsVccPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnLsVccPort.setStatus(_A)
class _AwnSysConnLsVccTimeslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AwnSysConnLsVccTimeslot_Type.__name__=_D
_AwnSysConnLsVccTimeslot_Object=MibTableColumn
awnSysConnLsVccTimeslot=_AwnSysConnLsVccTimeslot_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1,4),_AwnSysConnLsVccTimeslot_Type())
awnSysConnLsVccTimeslot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnLsVccTimeslot.setStatus(_A)
class _AwnSysConnLsVccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AwnSysConnLsVccVpi_Type.__name__=_D
_AwnSysConnLsVccVpi_Object=MibTableColumn
awnSysConnLsVccVpi=_AwnSysConnLsVccVpi_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1,5),_AwnSysConnLsVccVpi_Type())
awnSysConnLsVccVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnLsVccVpi.setStatus(_A)
class _AwnSysConnLsVccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AwnSysConnLsVccVci_Type.__name__=_D
_AwnSysConnLsVccVci_Object=MibTableColumn
awnSysConnLsVccVci=_AwnSysConnLsVccVci_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1,6),_AwnSysConnLsVccVci_Type())
awnSysConnLsVccVci.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnLsVccVci.setStatus(_A)
class _AwnSysConnLsVccState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(100,100));fixedLength=100
_AwnSysConnLsVccState_Type.__name__=_E
_AwnSysConnLsVccState_Object=MibTableColumn
awnSysConnLsVccState=_AwnSysConnLsVccState_Object((1,3,6,1,4,1,211,1,127,29,1,10,1,1,7),_AwnSysConnLsVccState_Type())
awnSysConnLsVccState.setMaxAccess(_B)
if mibBuilder.loadTexts:awnSysConnLsVccState.setStatus(_A)
_AwnSysBackIpAddr_ObjectIdentity=ObjectIdentity
awnSysBackIpAddr=_AwnSysBackIpAddr_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,1,11))
_AwnStatistics_ObjectIdentity=ObjectIdentity
awnStatistics=_AwnStatistics_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2))
_AwnStatisticsSw_ObjectIdentity=ObjectIdentity
awnStatisticsSw=_AwnStatisticsSw_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,1))
class _AwnStatisticsSwport_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AwnStatisticsSwport_Type.__name__=_E
_AwnStatisticsSwport_Object=MibScalar
awnStatisticsSwport=_AwnStatisticsSwport_Object((1,3,6,1,4,1,211,1,127,29,2,1,1),_AwnStatisticsSwport_Type())
awnStatisticsSwport.setMaxAccess(_H)
if mibBuilder.loadTexts:awnStatisticsSwport.setStatus(_G)
_AwnStatisticsLine_ObjectIdentity=ObjectIdentity
awnStatisticsLine=_AwnStatisticsLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,2))
_AwnStatisticsLineTable_Object=MibTable
awnStatisticsLineTable=_AwnStatisticsLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,2,1))
if mibBuilder.loadTexts:awnStatisticsLineTable.setStatus(_G)
_AwnStatisticsLineEntry_Object=MibTableRow
awnStatisticsLineEntry=_AwnStatisticsLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,2,1,1))
awnStatisticsLineEntry.setIndexNames((0,_C,_d),(0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:awnStatisticsLineEntry.setStatus(_G)
_AwnStatisticsLineUnit_Type=Integer32
_AwnStatisticsLineUnit_Object=MibTableColumn
awnStatisticsLineUnit=_AwnStatisticsLineUnit_Object((1,3,6,1,4,1,211,1,127,29,2,2,1,1,1),_AwnStatisticsLineUnit_Type())
awnStatisticsLineUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLineUnit.setStatus(_G)
_AwnStatisticsLineCard_Type=Integer32
_AwnStatisticsLineCard_Object=MibTableColumn
awnStatisticsLineCard=_AwnStatisticsLineCard_Object((1,3,6,1,4,1,211,1,127,29,2,2,1,1,2),_AwnStatisticsLineCard_Type())
awnStatisticsLineCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLineCard.setStatus(_G)
_AwnStatisticsLinePort_Type=Integer32
_AwnStatisticsLinePort_Object=MibTableColumn
awnStatisticsLinePort=_AwnStatisticsLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,2,1,1,3),_AwnStatisticsLinePort_Type())
awnStatisticsLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLinePort.setStatus(_G)
class _AwnStatisticsLinePriWan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_AwnStatisticsLinePriWan_Type.__name__=_E
_AwnStatisticsLinePriWan_Object=MibTableColumn
awnStatisticsLinePriWan=_AwnStatisticsLinePriWan_Object((1,3,6,1,4,1,211,1,127,29,2,2,1,1,4),_AwnStatisticsLinePriWan_Type())
awnStatisticsLinePriWan.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLinePriWan.setStatus(_G)
class _AwnStatisticsLineSriWan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_AwnStatisticsLineSriWan_Type.__name__=_E
_AwnStatisticsLineSriWan_Object=MibTableColumn
awnStatisticsLineSriWan=_AwnStatisticsLineSriWan_Object((1,3,6,1,4,1,211,1,127,29,2,2,1,1,5),_AwnStatisticsLineSriWan_Type())
awnStatisticsLineSriWan.setMaxAccess(_H)
if mibBuilder.loadTexts:awnStatisticsLineSriWan.setStatus(_G)
class _AwnStatisticsLineBriWan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_AwnStatisticsLineBriWan_Type.__name__=_E
_AwnStatisticsLineBriWan_Object=MibTableColumn
awnStatisticsLineBriWan=_AwnStatisticsLineBriWan_Object((1,3,6,1,4,1,211,1,127,29,2,2,1,1,6),_AwnStatisticsLineBriWan_Type())
awnStatisticsLineBriWan.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLineBriWan.setStatus(_G)
_AwnStatisticsComLine_ObjectIdentity=ObjectIdentity
awnStatisticsComLine=_AwnStatisticsComLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,3))
_AwnStatisticsComLineTable_Object=MibTable
awnStatisticsComLineTable=_AwnStatisticsComLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,3,1))
if mibBuilder.loadTexts:awnStatisticsComLineTable.setStatus(_A)
_AwnStatisticsComLineEntry_Object=MibTableRow
awnStatisticsComLineEntry=_AwnStatisticsComLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,3,1,1))
awnStatisticsComLineEntry.setIndexNames((0,_C,_g),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:awnStatisticsComLineEntry.setStatus(_A)
class _AwnStatisticsComLineSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComLineSlot_Type.__name__=_D
_AwnStatisticsComLineSlot_Object=MibTableColumn
awnStatisticsComLineSlot=_AwnStatisticsComLineSlot_Object((1,3,6,1,4,1,211,1,127,29,2,3,1,1,1),_AwnStatisticsComLineSlot_Type())
awnStatisticsComLineSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComLineSlot.setStatus(_A)
class _AwnStatisticsComLineAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsComLineAdapter_Type.__name__=_D
_AwnStatisticsComLineAdapter_Object=MibTableColumn
awnStatisticsComLineAdapter=_AwnStatisticsComLineAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,3,1,1,2),_AwnStatisticsComLineAdapter_Type())
awnStatisticsComLineAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComLineAdapter.setStatus(_A)
class _AwnStatisticsComLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComLinePort_Type.__name__=_D
_AwnStatisticsComLinePort_Object=MibTableColumn
awnStatisticsComLinePort=_AwnStatisticsComLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,3,1,1,3),_AwnStatisticsComLinePort_Type())
awnStatisticsComLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComLinePort.setStatus(_A)
class _AwnStatisticsComLineAtm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(132,132));fixedLength=132
_AwnStatisticsComLineAtm_Type.__name__=_E
_AwnStatisticsComLineAtm_Object=MibTableColumn
awnStatisticsComLineAtm=_AwnStatisticsComLineAtm_Object((1,3,6,1,4,1,211,1,127,29,2,3,1,1,4),_AwnStatisticsComLineAtm_Type())
awnStatisticsComLineAtm.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComLineAtm.setStatus(_A)
class _AwnStatisticsComLan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(264,264));fixedLength=264
_AwnStatisticsComLan_Type.__name__=_E
_AwnStatisticsComLan_Object=MibTableColumn
awnStatisticsComLan=_AwnStatisticsComLan_Object((1,3,6,1,4,1,211,1,127,29,2,3,1,1,5),_AwnStatisticsComLan_Type())
awnStatisticsComLan.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComLan.setStatus(_A)
_AwnStatisticsLsLine_ObjectIdentity=ObjectIdentity
awnStatisticsLsLine=_AwnStatisticsLsLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,4))
_AwnStatisticsLsLineTable_Object=MibTable
awnStatisticsLsLineTable=_AwnStatisticsLsLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,4,1))
if mibBuilder.loadTexts:awnStatisticsLsLineTable.setStatus(_A)
_AwnStatisticsLsLineEntry_Object=MibTableRow
awnStatisticsLsLineEntry=_AwnStatisticsLsLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1))
awnStatisticsLsLineEntry.setIndexNames((0,_C,_j),(0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:awnStatisticsLsLineEntry.setStatus(_A)
class _AwnStatisticsLsLineUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsLineUnit_Type.__name__=_D
_AwnStatisticsLsLineUnit_Object=MibScalar
awnStatisticsLsLineUnit=_AwnStatisticsLsLineUnit_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,1),_AwnStatisticsLsLineUnit_Type())
awnStatisticsLsLineUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineUnit.setStatus(_A)
class _AwnStatisticsLsLineCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsLsLineCard_Type.__name__=_D
_AwnStatisticsLsLineCard_Object=MibScalar
awnStatisticsLsLineCard=_AwnStatisticsLsLineCard_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,2),_AwnStatisticsLsLineCard_Type())
awnStatisticsLsLineCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineCard.setStatus(_A)
class _AwnStatisticsLsLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsLinePort_Type.__name__=_D
_AwnStatisticsLsLinePort_Object=MibTableColumn
awnStatisticsLsLinePort=_AwnStatisticsLsLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,3),_AwnStatisticsLsLinePort_Type())
awnStatisticsLsLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLinePort.setStatus(_A)
class _AwnStatisticsLsLinePriWan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(504,504));fixedLength=504
_AwnStatisticsLsLinePriWan_Type.__name__=_E
_AwnStatisticsLsLinePriWan_Object=MibTableColumn
awnStatisticsLsLinePriWan=_AwnStatisticsLsLinePriWan_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,4),_AwnStatisticsLsLinePriWan_Type())
awnStatisticsLsLinePriWan.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLinePriWan.setStatus(_A)
class _AwnStatisticsLsLineBriWan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(120,120));fixedLength=120
_AwnStatisticsLsLineBriWan_Type.__name__=_E
_AwnStatisticsLsLineBriWan_Object=MibTableColumn
awnStatisticsLsLineBriWan=_AwnStatisticsLsLineBriWan_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,5),_AwnStatisticsLsLineBriWan_Type())
awnStatisticsLsLineBriWan.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineBriWan.setStatus(_A)
class _AwnStatisticsLsLinePriBup_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(120,120));fixedLength=120
_AwnStatisticsLsLinePriBup_Type.__name__=_E
_AwnStatisticsLsLinePriBup_Object=MibTableColumn
awnStatisticsLsLinePriBup=_AwnStatisticsLsLinePriBup_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,6),_AwnStatisticsLsLinePriBup_Type())
awnStatisticsLsLinePriBup.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLinePriBup.setStatus(_A)
class _AwnStatisticsLsLineFrclad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(504,504));fixedLength=504
_AwnStatisticsLsLineFrclad_Type.__name__=_E
_AwnStatisticsLsLineFrclad_Object=MibTableColumn
awnStatisticsLsLineFrclad=_AwnStatisticsLsLineFrclad_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,7),_AwnStatisticsLsLineFrclad_Type())
awnStatisticsLsLineFrclad.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineFrclad.setStatus(_A)
class _AwnStatisticsLsLineFrclad2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(584,584));fixedLength=584
_AwnStatisticsLsLineFrclad2_Type.__name__=_E
_AwnStatisticsLsLineFrclad2_Object=MibTableColumn
awnStatisticsLsLineFrclad2=_AwnStatisticsLsLineFrclad2_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,8),_AwnStatisticsLsLineFrclad2_Type())
awnStatisticsLsLineFrclad2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineFrclad2.setStatus(_A)
class _AwnStatisticsLsLineFrclad3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(584,584));fixedLength=584
_AwnStatisticsLsLineFrclad3_Type.__name__=_E
_AwnStatisticsLsLineFrclad3_Object=MibTableColumn
awnStatisticsLsLineFrclad3=_AwnStatisticsLsLineFrclad3_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,9),_AwnStatisticsLsLineFrclad3_Type())
awnStatisticsLsLineFrclad3.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineFrclad3.setStatus(_A)
class _AwnStatisticsLsLineLineDif_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_AwnStatisticsLsLineLineDif_Type.__name__=_E
_AwnStatisticsLsLineLineDif_Object=MibScalar
awnStatisticsLsLineLineDif=_AwnStatisticsLsLineLineDif_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,10),_AwnStatisticsLsLineLineDif_Type())
awnStatisticsLsLineLineDif.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineLineDif.setStatus(_A)
class _AwnStatisticsLsLineDifFrclad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(160,160));fixedLength=160
_AwnStatisticsLsLineDifFrclad_Type.__name__=_E
_AwnStatisticsLsLineDifFrclad_Object=MibTableColumn
awnStatisticsLsLineDifFrclad=_AwnStatisticsLsLineDifFrclad_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,11),_AwnStatisticsLsLineDifFrclad_Type())
awnStatisticsLsLineDifFrclad.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineDifFrclad.setStatus(_A)
class _AwnStatisticsLsLinePriCes_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(328,328));fixedLength=328
_AwnStatisticsLsLinePriCes_Type.__name__=_E
_AwnStatisticsLsLinePriCes_Object=MibTableColumn
awnStatisticsLsLinePriCes=_AwnStatisticsLsLinePriCes_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,12),_AwnStatisticsLsLinePriCes_Type())
awnStatisticsLsLinePriCes.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLinePriCes.setStatus(_A)
class _AwnStatisticsLsLineDtkCodec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(724,724));fixedLength=724
_AwnStatisticsLsLineDtkCodec_Type.__name__=_E
_AwnStatisticsLsLineDtkCodec_Object=MibTableColumn
awnStatisticsLsLineDtkCodec=_AwnStatisticsLsLineDtkCodec_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,13),_AwnStatisticsLsLineDtkCodec_Type())
awnStatisticsLsLineDtkCodec.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineDtkCodec.setStatus(_A)
class _AwnStatisticsLsLineDtkDclad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(600,600));fixedLength=600
_AwnStatisticsLsLineDtkDclad_Type.__name__=_E
_AwnStatisticsLsLineDtkDclad_Object=MibTableColumn
awnStatisticsLsLineDtkDclad=_AwnStatisticsLsLineDtkDclad_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,14),_AwnStatisticsLsLineDtkDclad_Type())
awnStatisticsLsLineDtkDclad.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineDtkDclad.setStatus(_A)
class _AwnStatisticsLsLineDtkDclad2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(352,352));fixedLength=352
_AwnStatisticsLsLineDtkDclad2_Type.__name__=_E
_AwnStatisticsLsLineDtkDclad2_Object=MibTableColumn
awnStatisticsLsLineDtkDclad2=_AwnStatisticsLsLineDtkDclad2_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,15),_AwnStatisticsLsLineDtkDclad2_Type())
awnStatisticsLsLineDtkDclad2.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineDtkDclad2.setStatus(_A)
class _AwnStatisticsLsLineOdtCodec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(124,124));fixedLength=124
_AwnStatisticsLsLineOdtCodec_Type.__name__=_E
_AwnStatisticsLsLineOdtCodec_Object=MibTableColumn
awnStatisticsLsLineOdtCodec=_AwnStatisticsLsLineOdtCodec_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,16),_AwnStatisticsLsLineOdtCodec_Type())
awnStatisticsLsLineOdtCodec.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineOdtCodec.setStatus(_A)
class _AwnStatisticsLsLineOdtDclad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_AwnStatisticsLsLineOdtDclad_Type.__name__=_E
_AwnStatisticsLsLineOdtDclad_Object=MibTableColumn
awnStatisticsLsLineOdtDclad=_AwnStatisticsLsLineOdtDclad_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,17),_AwnStatisticsLsLineOdtDclad_Type())
awnStatisticsLsLineOdtDclad.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineOdtDclad.setStatus(_A)
class _AwnStatisticsLsLineSriCes_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(112,112));fixedLength=112
_AwnStatisticsLsLineSriCes_Type.__name__=_E
_AwnStatisticsLsLineSriCes_Object=MibTableColumn
awnStatisticsLsLineSriCes=_AwnStatisticsLsLineSriCes_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,18),_AwnStatisticsLsLineSriCes_Type())
awnStatisticsLsLineSriCes.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineSriCes.setStatus(_A)
class _AwnStatisticsLsLineBriBup_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(120,120));fixedLength=120
_AwnStatisticsLsLineBriBup_Type.__name__=_E
_AwnStatisticsLsLineBriBup_Object=MibTableColumn
awnStatisticsLsLineBriBup=_AwnStatisticsLsLineBriBup_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,19),_AwnStatisticsLsLineBriBup_Type())
awnStatisticsLsLineBriBup.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineBriBup.setStatus(_A)
class _AwnStatisticsLsLineLrcrad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(124,124));fixedLength=124
_AwnStatisticsLsLineLrcrad_Type.__name__=_E
_AwnStatisticsLsLineLrcrad_Object=MibScalar
awnStatisticsLsLineLrcrad=_AwnStatisticsLsLineLrcrad_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,20),_AwnStatisticsLsLineLrcrad_Type())
awnStatisticsLsLineLrcrad.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineLrcrad.setStatus(_A)
class _AwnStatisticsLsLine45Mwan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(152,152));fixedLength=152
_AwnStatisticsLsLine45Mwan_Type.__name__=_E
_AwnStatisticsLsLine45Mwan_Object=MibTableColumn
awnStatisticsLsLine45Mwan=_AwnStatisticsLsLine45Mwan_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,21),_AwnStatisticsLsLine45Mwan_Type())
awnStatisticsLsLine45Mwan.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLine45Mwan.setStatus(_A)
class _AwnStatisticsLsLineOdtCodecS_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(144,144));fixedLength=144
_AwnStatisticsLsLineOdtCodecS_Type.__name__=_E
_AwnStatisticsLsLineOdtCodecS_Object=MibTableColumn
awnStatisticsLsLineOdtCodecS=_AwnStatisticsLsLineOdtCodecS_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,22),_AwnStatisticsLsLineOdtCodecS_Type())
awnStatisticsLsLineOdtCodecS.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineOdtCodecS.setStatus(_A)
class _AwnStatisticsLsLinePriWan24_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(500,500));fixedLength=500
_AwnStatisticsLsLinePriWan24_Type.__name__=_E
_AwnStatisticsLsLinePriWan24_Object=MibTableColumn
awnStatisticsLsLinePriWan24=_AwnStatisticsLsLinePriWan24_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,23),_AwnStatisticsLsLinePriWan24_Type())
awnStatisticsLsLinePriWan24.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLinePriWan24.setStatus(_A)
class _AwnStatisticsLsLineFfclad24a_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(496,496));fixedLength=496
_AwnStatisticsLsLineFfclad24a_Type.__name__=_E
_AwnStatisticsLsLineFfclad24a_Object=MibTableColumn
awnStatisticsLsLineFfclad24a=_AwnStatisticsLsLineFfclad24a_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,24),_AwnStatisticsLsLineFfclad24a_Type())
awnStatisticsLsLineFfclad24a.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineFfclad24a.setStatus(_A)
class _AwnStatisticsLsLineFfclad24b_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(584,584));fixedLength=584
_AwnStatisticsLsLineFfclad24b_Type.__name__=_E
_AwnStatisticsLsLineFfclad24b_Object=MibTableColumn
awnStatisticsLsLineFfclad24b=_AwnStatisticsLsLineFfclad24b_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,25),_AwnStatisticsLsLineFfclad24b_Type())
awnStatisticsLsLineFfclad24b.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineFfclad24b.setStatus(_A)
class _AwnStatisticsLsLineFfclad24c_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(588,588));fixedLength=588
_AwnStatisticsLsLineFfclad24c_Type.__name__=_E
_AwnStatisticsLsLineFfclad24c_Object=MibTableColumn
awnStatisticsLsLineFfclad24c=_AwnStatisticsLsLineFfclad24c_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,26),_AwnStatisticsLsLineFfclad24c_Type())
awnStatisticsLsLineFfclad24c.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineFfclad24c.setStatus(_A)
class _AwnStatisticsLsLineVxaWan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(116,116));fixedLength=116
_AwnStatisticsLsLineVxaWan_Type.__name__=_E
_AwnStatisticsLsLineVxaWan_Object=MibTableColumn
awnStatisticsLsLineVxaWan=_AwnStatisticsLsLineVxaWan_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,27),_AwnStatisticsLsLineVxaWan_Type())
awnStatisticsLsLineVxaWan.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineVxaWan.setStatus(_A)
class _AwnStatisticsLsLineBriClad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(160,160));fixedLength=160
_AwnStatisticsLsLineBriClad_Type.__name__=_E
_AwnStatisticsLsLineBriClad_Object=MibTableColumn
awnStatisticsLsLineBriClad=_AwnStatisticsLsLineBriClad_Object((1,3,6,1,4,1,211,1,127,29,2,4,1,1,28),_AwnStatisticsLsLineBriClad_Type())
awnStatisticsLsLineBriClad.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsLineBriClad.setStatus(_A)
_AwnStatisticsComNniPort_ObjectIdentity=ObjectIdentity
awnStatisticsComNniPort=_AwnStatisticsComNniPort_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,5))
_AwnStatisticsComNniPortTable_Object=MibTable
awnStatisticsComNniPortTable=_AwnStatisticsComNniPortTable_Object((1,3,6,1,4,1,211,1,127,29,2,5,1))
if mibBuilder.loadTexts:awnStatisticsComNniPortTable.setStatus(_A)
_AwnStatisticsComNniPortEntry_Object=MibTableRow
awnStatisticsComNniPortEntry=_AwnStatisticsComNniPortEntry_Object((1,3,6,1,4,1,211,1,127,29,2,5,1,1))
awnStatisticsComNniPortEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_o))
if mibBuilder.loadTexts:awnStatisticsComNniPortEntry.setStatus(_A)
class _AwnStatisticsComNniPortSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniPortSlot_Type.__name__=_D
_AwnStatisticsComNniPortSlot_Object=MibTableColumn
awnStatisticsComNniPortSlot=_AwnStatisticsComNniPortSlot_Object((1,3,6,1,4,1,211,1,127,29,2,5,1,1,1),_AwnStatisticsComNniPortSlot_Type())
awnStatisticsComNniPortSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortSlot.setStatus(_A)
class _AwnStatisticsComNniPortAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsComNniPortAdapter_Type.__name__=_D
_AwnStatisticsComNniPortAdapter_Object=MibTableColumn
awnStatisticsComNniPortAdapter=_AwnStatisticsComNniPortAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,5,1,1,2),_AwnStatisticsComNniPortAdapter_Type())
awnStatisticsComNniPortAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortAdapter.setStatus(_A)
class _AwnStatisticsComNniPortPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniPortPort_Type.__name__=_D
_AwnStatisticsComNniPortPort_Object=MibTableColumn
awnStatisticsComNniPortPort=_AwnStatisticsComNniPortPort_Object((1,3,6,1,4,1,211,1,127,29,2,5,1,1,3),_AwnStatisticsComNniPortPort_Type())
awnStatisticsComNniPortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortPort.setStatus(_A)
class _AwnStatisticsComNniPortData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(456,456));fixedLength=456
_AwnStatisticsComNniPortData_Type.__name__=_E
_AwnStatisticsComNniPortData_Object=MibTableColumn
awnStatisticsComNniPortData=_AwnStatisticsComNniPortData_Object((1,3,6,1,4,1,211,1,127,29,2,5,1,1,4),_AwnStatisticsComNniPortData_Type())
awnStatisticsComNniPortData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortData.setStatus(_A)
_AwnStatisticsComNniVp_ObjectIdentity=ObjectIdentity
awnStatisticsComNniVp=_AwnStatisticsComNniVp_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,6))
_AwnStatisticsComNniVpTable_Object=MibTable
awnStatisticsComNniVpTable=_AwnStatisticsComNniVpTable_Object((1,3,6,1,4,1,211,1,127,29,2,6,1))
if mibBuilder.loadTexts:awnStatisticsComNniVpTable.setStatus(_A)
_AwnStatisticsComNniVpEntry_Object=MibTableRow
awnStatisticsComNniVpEntry=_AwnStatisticsComNniVpEntry_Object((1,3,6,1,4,1,211,1,127,29,2,6,1,1))
awnStatisticsComNniVpEntry.setIndexNames((0,_C,_p),(0,_C,_q),(0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:awnStatisticsComNniVpEntry.setStatus(_A)
class _AwnStatisticsComNniVpSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniVpSlot_Type.__name__=_D
_AwnStatisticsComNniVpSlot_Object=MibTableColumn
awnStatisticsComNniVpSlot=_AwnStatisticsComNniVpSlot_Object((1,3,6,1,4,1,211,1,127,29,2,6,1,1,1),_AwnStatisticsComNniVpSlot_Type())
awnStatisticsComNniVpSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpSlot.setStatus(_A)
class _AwnStatisticsComNniVpAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsComNniVpAdapter_Type.__name__=_D
_AwnStatisticsComNniVpAdapter_Object=MibTableColumn
awnStatisticsComNniVpAdapter=_AwnStatisticsComNniVpAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,6,1,1,2),_AwnStatisticsComNniVpAdapter_Type())
awnStatisticsComNniVpAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpAdapter.setStatus(_A)
class _AwnStatisticsComNniVpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniVpPort_Type.__name__=_D
_AwnStatisticsComNniVpPort_Object=MibTableColumn
awnStatisticsComNniVpPort=_AwnStatisticsComNniVpPort_Object((1,3,6,1,4,1,211,1,127,29,2,6,1,1,3),_AwnStatisticsComNniVpPort_Type())
awnStatisticsComNniVpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpPort.setStatus(_A)
class _AwnStatisticsComNniVpVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AwnStatisticsComNniVpVpi_Type.__name__=_D
_AwnStatisticsComNniVpVpi_Object=MibTableColumn
awnStatisticsComNniVpVpi=_AwnStatisticsComNniVpVpi_Object((1,3,6,1,4,1,211,1,127,29,2,6,1,1,4),_AwnStatisticsComNniVpVpi_Type())
awnStatisticsComNniVpVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpVpi.setStatus(_A)
class _AwnStatisticsComNniVptData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(456,456));fixedLength=456
_AwnStatisticsComNniVptData_Type.__name__=_E
_AwnStatisticsComNniVptData_Object=MibScalar
awnStatisticsComNniVptData=_AwnStatisticsComNniVptData_Object((1,3,6,1,4,1,211,1,127,29,2,6,1,1,5),_AwnStatisticsComNniVptData_Type())
awnStatisticsComNniVptData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVptData.setStatus(_A)
_AwnStatisticsLsWanTs_ObjectIdentity=ObjectIdentity
awnStatisticsLsWanTs=_AwnStatisticsLsWanTs_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,7))
_AwnStatisticsLsWanTsTable_Object=MibTable
awnStatisticsLsWanTsTable=_AwnStatisticsLsWanTsTable_Object((1,3,6,1,4,1,211,1,127,29,2,7,1))
if mibBuilder.loadTexts:awnStatisticsLsWanTsTable.setStatus(_A)
_AwnStatisticsLsWanTsEntry_Object=MibTableRow
awnStatisticsLsWanTsEntry=_AwnStatisticsLsWanTsEntry_Object((1,3,6,1,4,1,211,1,127,29,2,7,1,1))
awnStatisticsLsWanTsEntry.setIndexNames((0,_C,_t),(0,_C,_u),(0,_C,_v),(0,_C,_w))
if mibBuilder.loadTexts:awnStatisticsLsWanTsEntry.setStatus(_A)
class _AwnStatisticsLsWanTsUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsWanTsUnit_Type.__name__=_D
_AwnStatisticsLsWanTsUnit_Object=MibTableColumn
awnStatisticsLsWanTsUnit=_AwnStatisticsLsWanTsUnit_Object((1,3,6,1,4,1,211,1,127,29,2,7,1,1,1),_AwnStatisticsLsWanTsUnit_Type())
awnStatisticsLsWanTsUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsUnit.setStatus(_A)
class _AwnStatisticsLsWanTsCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsLsWanTsCard_Type.__name__=_D
_AwnStatisticsLsWanTsCard_Object=MibTableColumn
awnStatisticsLsWanTsCard=_AwnStatisticsLsWanTsCard_Object((1,3,6,1,4,1,211,1,127,29,2,7,1,1,2),_AwnStatisticsLsWanTsCard_Type())
awnStatisticsLsWanTsCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsCard.setStatus(_A)
class _AwnStatisticsLsWanTsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsWanTsPort_Type.__name__=_D
_AwnStatisticsLsWanTsPort_Object=MibTableColumn
awnStatisticsLsWanTsPort=_AwnStatisticsLsWanTsPort_Object((1,3,6,1,4,1,211,1,127,29,2,7,1,1,3),_AwnStatisticsLsWanTsPort_Type())
awnStatisticsLsWanTsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsPort.setStatus(_A)
class _AwnStatisticsLsWanTsTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AwnStatisticsLsWanTsTs_Type.__name__=_D
_AwnStatisticsLsWanTsTs_Object=MibTableColumn
awnStatisticsLsWanTsTs=_AwnStatisticsLsWanTsTs_Object((1,3,6,1,4,1,211,1,127,29,2,7,1,1,4),_AwnStatisticsLsWanTsTs_Type())
awnStatisticsLsWanTsTs.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsTs.setStatus(_A)
class _AwnStatisticsLsWanTsData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(456,456));fixedLength=456
_AwnStatisticsLsWanTsData_Type.__name__=_E
_AwnStatisticsLsWanTsData_Object=MibTableColumn
awnStatisticsLsWanTsData=_AwnStatisticsLsWanTsData_Object((1,3,6,1,4,1,211,1,127,29,2,7,1,1,5),_AwnStatisticsLsWanTsData_Type())
awnStatisticsLsWanTsData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsData.setStatus(_A)
_AwnStatisticsComNniPortRt_ObjectIdentity=ObjectIdentity
awnStatisticsComNniPortRt=_AwnStatisticsComNniPortRt_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,8))
_AwnStatisticsComNniPortRtTable_Object=MibTable
awnStatisticsComNniPortRtTable=_AwnStatisticsComNniPortRtTable_Object((1,3,6,1,4,1,211,1,127,29,2,8,1))
if mibBuilder.loadTexts:awnStatisticsComNniPortRtTable.setStatus(_A)
_AwnStatisticsComNniPortRtEntry_Object=MibTableRow
awnStatisticsComNniPortRtEntry=_AwnStatisticsComNniPortRtEntry_Object((1,3,6,1,4,1,211,1,127,29,2,8,1,1))
awnStatisticsComNniPortRtEntry.setIndexNames((0,_C,_x),(0,_C,_y),(0,_C,_z),(0,_C,_A0),(0,_C,_A1))
if mibBuilder.loadTexts:awnStatisticsComNniPortRtEntry.setStatus(_A)
class _AwnStatisticsComNniPortRtSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniPortRtSlot_Type.__name__=_D
_AwnStatisticsComNniPortRtSlot_Object=MibTableColumn
awnStatisticsComNniPortRtSlot=_AwnStatisticsComNniPortRtSlot_Object((1,3,6,1,4,1,211,1,127,29,2,8,1,1,1),_AwnStatisticsComNniPortRtSlot_Type())
awnStatisticsComNniPortRtSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortRtSlot.setStatus(_A)
class _AwnStatisticsComNniPortRtAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsComNniPortRtAdapter_Type.__name__=_D
_AwnStatisticsComNniPortRtAdapter_Object=MibTableColumn
awnStatisticsComNniPortRtAdapter=_AwnStatisticsComNniPortRtAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,8,1,1,2),_AwnStatisticsComNniPortRtAdapter_Type())
awnStatisticsComNniPortRtAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortRtAdapter.setStatus(_A)
class _AwnStatisticsComNniPortRtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniPortRtPort_Type.__name__=_D
_AwnStatisticsComNniPortRtPort_Object=MibTableColumn
awnStatisticsComNniPortRtPort=_AwnStatisticsComNniPortRtPort_Object((1,3,6,1,4,1,211,1,127,29,2,8,1,1,3),_AwnStatisticsComNniPortRtPort_Type())
awnStatisticsComNniPortRtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortRtPort.setStatus(_A)
class _AwnStatisticsComNniPortRtCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_AwnStatisticsComNniPortRtCategory_Type.__name__=_D
_AwnStatisticsComNniPortRtCategory_Object=MibTableColumn
awnStatisticsComNniPortRtCategory=_AwnStatisticsComNniPortRtCategory_Object((1,3,6,1,4,1,211,1,127,29,2,8,1,1,4),_AwnStatisticsComNniPortRtCategory_Type())
awnStatisticsComNniPortRtCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortRtCategory.setStatus(_A)
class _AwnStatisticsComNniPortRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsComNniPortRtType_Type.__name__=_D
_AwnStatisticsComNniPortRtType_Object=MibTableColumn
awnStatisticsComNniPortRtType=_AwnStatisticsComNniPortRtType_Object((1,3,6,1,4,1,211,1,127,29,2,8,1,1,5),_AwnStatisticsComNniPortRtType_Type())
awnStatisticsComNniPortRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortRtType.setStatus(_A)
class _AwnStatisticsComNniPortRtData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AwnStatisticsComNniPortRtData_Type.__name__=_F
_AwnStatisticsComNniPortRtData_Object=MibTableColumn
awnStatisticsComNniPortRtData=_AwnStatisticsComNniPortRtData_Object((1,3,6,1,4,1,211,1,127,29,2,8,1,1,6),_AwnStatisticsComNniPortRtData_Type())
awnStatisticsComNniPortRtData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniPortRtData.setStatus(_A)
_AwnStatisticsComNniVpRt_ObjectIdentity=ObjectIdentity
awnStatisticsComNniVpRt=_AwnStatisticsComNniVpRt_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,9))
_AwnStatisticsComNniVpRtTable_Object=MibTable
awnStatisticsComNniVpRtTable=_AwnStatisticsComNniVpRtTable_Object((1,3,6,1,4,1,211,1,127,29,2,9,1))
if mibBuilder.loadTexts:awnStatisticsComNniVpRtTable.setStatus(_A)
_AwnStatisticsComNniVpRtEntry_Object=MibTableRow
awnStatisticsComNniVpRtEntry=_AwnStatisticsComNniVpRtEntry_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1))
awnStatisticsComNniVpRtEntry.setIndexNames((0,_C,_A2),(0,_C,_A3),(0,_C,_A4),(0,_C,_A5),(0,_C,_A6),(0,_C,_A7))
if mibBuilder.loadTexts:awnStatisticsComNniVpRtEntry.setStatus(_A)
class _AwnStatisticsComNniVpRtSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniVpRtSlot_Type.__name__=_D
_AwnStatisticsComNniVpRtSlot_Object=MibScalar
awnStatisticsComNniVpRtSlot=_AwnStatisticsComNniVpRtSlot_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1,1),_AwnStatisticsComNniVpRtSlot_Type())
awnStatisticsComNniVpRtSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpRtSlot.setStatus(_A)
class _AwnStatisticsComNniVpRtAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsComNniVpRtAdapter_Type.__name__=_D
_AwnStatisticsComNniVpRtAdapter_Object=MibTableColumn
awnStatisticsComNniVpRtAdapter=_AwnStatisticsComNniVpRtAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1,2),_AwnStatisticsComNniVpRtAdapter_Type())
awnStatisticsComNniVpRtAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpRtAdapter.setStatus(_A)
class _AwnStatisticsComNniVpRtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComNniVpRtPort_Type.__name__=_D
_AwnStatisticsComNniVpRtPort_Object=MibTableColumn
awnStatisticsComNniVpRtPort=_AwnStatisticsComNniVpRtPort_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1,3),_AwnStatisticsComNniVpRtPort_Type())
awnStatisticsComNniVpRtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpRtPort.setStatus(_A)
class _AwnStatisticsComNniVpRtVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AwnStatisticsComNniVpRtVpi_Type.__name__=_D
_AwnStatisticsComNniVpRtVpi_Object=MibTableColumn
awnStatisticsComNniVpRtVpi=_AwnStatisticsComNniVpRtVpi_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1,4),_AwnStatisticsComNniVpRtVpi_Type())
awnStatisticsComNniVpRtVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpRtVpi.setStatus(_A)
class _AwnStatisticsComNniVpRtCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_AwnStatisticsComNniVpRtCategory_Type.__name__=_D
_AwnStatisticsComNniVpRtCategory_Object=MibTableColumn
awnStatisticsComNniVpRtCategory=_AwnStatisticsComNniVpRtCategory_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1,5),_AwnStatisticsComNniVpRtCategory_Type())
awnStatisticsComNniVpRtCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpRtCategory.setStatus(_A)
class _AwnStatisticsComNniVpRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsComNniVpRtType_Type.__name__=_D
_AwnStatisticsComNniVpRtType_Object=MibTableColumn
awnStatisticsComNniVpRtType=_AwnStatisticsComNniVpRtType_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1,6),_AwnStatisticsComNniVpRtType_Type())
awnStatisticsComNniVpRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpRtType.setStatus(_A)
class _AwnStatisticsComNniVpRtData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AwnStatisticsComNniVpRtData_Type.__name__=_F
_AwnStatisticsComNniVpRtData_Object=MibTableColumn
awnStatisticsComNniVpRtData=_AwnStatisticsComNniVpRtData_Object((1,3,6,1,4,1,211,1,127,29,2,9,1,1,7),_AwnStatisticsComNniVpRtData_Type())
awnStatisticsComNniVpRtData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComNniVpRtData.setStatus(_A)
_AwnStatisticsLsWanTsRt_ObjectIdentity=ObjectIdentity
awnStatisticsLsWanTsRt=_AwnStatisticsLsWanTsRt_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,10))
_AwnStatisticsLsWanTsRtTable_Object=MibTable
awnStatisticsLsWanTsRtTable=_AwnStatisticsLsWanTsRtTable_Object((1,3,6,1,4,1,211,1,127,29,2,10,1))
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtTable.setStatus(_A)
_AwnStatisticsLsWanTsRtEntry_Object=MibTableRow
awnStatisticsLsWanTsRtEntry=_AwnStatisticsLsWanTsRtEntry_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1))
awnStatisticsLsWanTsRtEntry.setIndexNames((0,_C,_A8),(0,_C,_A9),(0,_C,_AA),(0,_C,_AB),(0,_C,_AC),(0,_C,_AD))
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtEntry.setStatus(_A)
class _AwnStatisticsLsWanTsRtUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsWanTsRtUnit_Type.__name__=_D
_AwnStatisticsLsWanTsRtUnit_Object=MibTableColumn
awnStatisticsLsWanTsRtUnit=_AwnStatisticsLsWanTsRtUnit_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1,1),_AwnStatisticsLsWanTsRtUnit_Type())
awnStatisticsLsWanTsRtUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtUnit.setStatus(_A)
class _AwnStatisticsLsWanTsRtCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsLsWanTsRtCard_Type.__name__=_D
_AwnStatisticsLsWanTsRtCard_Object=MibTableColumn
awnStatisticsLsWanTsRtCard=_AwnStatisticsLsWanTsRtCard_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1,2),_AwnStatisticsLsWanTsRtCard_Type())
awnStatisticsLsWanTsRtCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtCard.setStatus(_A)
class _AwnStatisticsLsWanTsRtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsWanTsRtPort_Type.__name__=_D
_AwnStatisticsLsWanTsRtPort_Object=MibTableColumn
awnStatisticsLsWanTsRtPort=_AwnStatisticsLsWanTsRtPort_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1,3),_AwnStatisticsLsWanTsRtPort_Type())
awnStatisticsLsWanTsRtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtPort.setStatus(_A)
class _AwnStatisticsLsWanTsRtTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AwnStatisticsLsWanTsRtTs_Type.__name__=_D
_AwnStatisticsLsWanTsRtTs_Object=MibTableColumn
awnStatisticsLsWanTsRtTs=_AwnStatisticsLsWanTsRtTs_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1,4),_AwnStatisticsLsWanTsRtTs_Type())
awnStatisticsLsWanTsRtTs.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtTs.setStatus(_A)
class _AwnStatisticsLsWanTsRtCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_AwnStatisticsLsWanTsRtCategory_Type.__name__=_D
_AwnStatisticsLsWanTsRtCategory_Object=MibTableColumn
awnStatisticsLsWanTsRtCategory=_AwnStatisticsLsWanTsRtCategory_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1,5),_AwnStatisticsLsWanTsRtCategory_Type())
awnStatisticsLsWanTsRtCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtCategory.setStatus(_A)
class _AwnStatisticsLsWanTsRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsLsWanTsRtType_Type.__name__=_D
_AwnStatisticsLsWanTsRtType_Object=MibTableColumn
awnStatisticsLsWanTsRtType=_AwnStatisticsLsWanTsRtType_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1,6),_AwnStatisticsLsWanTsRtType_Type())
awnStatisticsLsWanTsRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtType.setStatus(_A)
class _AwnStatisticsLsWanTsRtData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AwnStatisticsLsWanTsRtData_Type.__name__=_F
_AwnStatisticsLsWanTsRtData_Object=MibTableColumn
awnStatisticsLsWanTsRtData=_AwnStatisticsLsWanTsRtData_Object((1,3,6,1,4,1,211,1,127,29,2,10,1,1,7),_AwnStatisticsLsWanTsRtData_Type())
awnStatisticsLsWanTsRtData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanTsRtData.setStatus(_A)
_AwnStatisticsVccAtmLine_ObjectIdentity=ObjectIdentity
awnStatisticsVccAtmLine=_AwnStatisticsVccAtmLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,11))
_AwnStatisticsVccAtmLineTable_Object=MibTable
awnStatisticsVccAtmLineTable=_AwnStatisticsVccAtmLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,11,1))
if mibBuilder.loadTexts:awnStatisticsVccAtmLineTable.setStatus(_A)
_AwnStatisticsVccAtmLineEntry_Object=MibTableRow
awnStatisticsVccAtmLineEntry=_AwnStatisticsVccAtmLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1))
awnStatisticsVccAtmLineEntry.setIndexNames((0,_C,_AE),(0,_C,_AF),(0,_C,_AG),(0,_C,_AH),(0,_C,_AI),(0,_C,_AJ))
if mibBuilder.loadTexts:awnStatisticsVccAtmLineEntry.setStatus(_A)
class _AwnStatisticsVccAtmLineSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsVccAtmLineSlot_Type.__name__=_D
_AwnStatisticsVccAtmLineSlot_Object=MibTableColumn
awnStatisticsVccAtmLineSlot=_AwnStatisticsVccAtmLineSlot_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1,1),_AwnStatisticsVccAtmLineSlot_Type())
awnStatisticsVccAtmLineSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccAtmLineSlot.setStatus(_A)
class _AwnStatisticsVccAtmLineAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsVccAtmLineAdapter_Type.__name__=_D
_AwnStatisticsVccAtmLineAdapter_Object=MibTableColumn
awnStatisticsVccAtmLineAdapter=_AwnStatisticsVccAtmLineAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1,2),_AwnStatisticsVccAtmLineAdapter_Type())
awnStatisticsVccAtmLineAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccAtmLineAdapter.setStatus(_A)
class _AwnStatisticsVccAtmLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsVccAtmLinePort_Type.__name__=_D
_AwnStatisticsVccAtmLinePort_Object=MibTableColumn
awnStatisticsVccAtmLinePort=_AwnStatisticsVccAtmLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1,3),_AwnStatisticsVccAtmLinePort_Type())
awnStatisticsVccAtmLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccAtmLinePort.setStatus(_A)
class _AwnStatisticsVccAtmLineVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AwnStatisticsVccAtmLineVpi_Type.__name__=_D
_AwnStatisticsVccAtmLineVpi_Object=MibTableColumn
awnStatisticsVccAtmLineVpi=_AwnStatisticsVccAtmLineVpi_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1,4),_AwnStatisticsVccAtmLineVpi_Type())
awnStatisticsVccAtmLineVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccAtmLineVpi.setStatus(_A)
class _AwnStatisticsVccAtmLineVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4095))
_AwnStatisticsVccAtmLineVci_Type.__name__=_D
_AwnStatisticsVccAtmLineVci_Object=MibTableColumn
awnStatisticsVccAtmLineVci=_AwnStatisticsVccAtmLineVci_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1,5),_AwnStatisticsVccAtmLineVci_Type())
awnStatisticsVccAtmLineVci.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccAtmLineVci.setStatus(_A)
class _AwnStatisticsVccAtmLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsVccAtmLineType_Type.__name__=_D
_AwnStatisticsVccAtmLineType_Object=MibTableColumn
awnStatisticsVccAtmLineType=_AwnStatisticsVccAtmLineType_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1,6),_AwnStatisticsVccAtmLineType_Type())
awnStatisticsVccAtmLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccAtmLineType.setStatus(_A)
class _AwnStatisticsVccAtmLineData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AwnStatisticsVccAtmLineData_Type.__name__=_F
_AwnStatisticsVccAtmLineData_Object=MibTableColumn
awnStatisticsVccAtmLineData=_AwnStatisticsVccAtmLineData_Object((1,3,6,1,4,1,211,1,127,29,2,11,1,1,7),_AwnStatisticsVccAtmLineData_Type())
awnStatisticsVccAtmLineData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccAtmLineData.setStatus(_A)
_AwnStatisticsVpcAtmLine_ObjectIdentity=ObjectIdentity
awnStatisticsVpcAtmLine=_AwnStatisticsVpcAtmLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,12))
_AwnStatisticsVpcAtmLineTable_Object=MibTable
awnStatisticsVpcAtmLineTable=_AwnStatisticsVpcAtmLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,12,1))
if mibBuilder.loadTexts:awnStatisticsVpcAtmLineTable.setStatus(_A)
_AwnStatisticsVpcAtmLineEntry_Object=MibTableRow
awnStatisticsVpcAtmLineEntry=_AwnStatisticsVpcAtmLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,12,1,1))
awnStatisticsVpcAtmLineEntry.setIndexNames((0,_C,_AK),(0,_C,_AL),(0,_C,_AM),(0,_C,_AN),(0,_C,_AO))
if mibBuilder.loadTexts:awnStatisticsVpcAtmLineEntry.setStatus(_A)
class _AwnStatisticsVpcAtmLineSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsVpcAtmLineSlot_Type.__name__=_D
_AwnStatisticsVpcAtmLineSlot_Object=MibTableColumn
awnStatisticsVpcAtmLineSlot=_AwnStatisticsVpcAtmLineSlot_Object((1,3,6,1,4,1,211,1,127,29,2,12,1,1,1),_AwnStatisticsVpcAtmLineSlot_Type())
awnStatisticsVpcAtmLineSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVpcAtmLineSlot.setStatus(_A)
class _AwnStatisticsVpcAtmLineAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsVpcAtmLineAdapter_Type.__name__=_D
_AwnStatisticsVpcAtmLineAdapter_Object=MibTableColumn
awnStatisticsVpcAtmLineAdapter=_AwnStatisticsVpcAtmLineAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,12,1,1,2),_AwnStatisticsVpcAtmLineAdapter_Type())
awnStatisticsVpcAtmLineAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVpcAtmLineAdapter.setStatus(_A)
class _AwnStatisticsVpcAtmLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsVpcAtmLinePort_Type.__name__=_D
_AwnStatisticsVpcAtmLinePort_Object=MibTableColumn
awnStatisticsVpcAtmLinePort=_AwnStatisticsVpcAtmLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,12,1,1,3),_AwnStatisticsVpcAtmLinePort_Type())
awnStatisticsVpcAtmLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVpcAtmLinePort.setStatus(_A)
class _AwnStatisticsVpcAtmLineVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AwnStatisticsVpcAtmLineVpi_Type.__name__=_D
_AwnStatisticsVpcAtmLineVpi_Object=MibTableColumn
awnStatisticsVpcAtmLineVpi=_AwnStatisticsVpcAtmLineVpi_Object((1,3,6,1,4,1,211,1,127,29,2,12,1,1,4),_AwnStatisticsVpcAtmLineVpi_Type())
awnStatisticsVpcAtmLineVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVpcAtmLineVpi.setStatus(_A)
class _AwnStatisticsVpcAtmLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsVpcAtmLineType_Type.__name__=_D
_AwnStatisticsVpcAtmLineType_Object=MibTableColumn
awnStatisticsVpcAtmLineType=_AwnStatisticsVpcAtmLineType_Object((1,3,6,1,4,1,211,1,127,29,2,12,1,1,5),_AwnStatisticsVpcAtmLineType_Type())
awnStatisticsVpcAtmLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVpcAtmLineType.setStatus(_A)
class _AwnStatisticsVpcAtmLineData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AwnStatisticsVpcAtmLineData_Type.__name__=_F
_AwnStatisticsVpcAtmLineData_Object=MibTableColumn
awnStatisticsVpcAtmLineData=_AwnStatisticsVpcAtmLineData_Object((1,3,6,1,4,1,211,1,127,29,2,12,1,1,6),_AwnStatisticsVpcAtmLineData_Type())
awnStatisticsVpcAtmLineData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVpcAtmLineData.setStatus(_A)
_AwnStatisticsVccWanTs_ObjectIdentity=ObjectIdentity
awnStatisticsVccWanTs=_AwnStatisticsVccWanTs_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,13))
_AwnStatisticsVccWanTsTable_Object=MibTable
awnStatisticsVccWanTsTable=_AwnStatisticsVccWanTsTable_Object((1,3,6,1,4,1,211,1,127,29,2,13,1))
if mibBuilder.loadTexts:awnStatisticsVccWanTsTable.setStatus(_A)
_AwnStatisticsVccWanTsEntry_Object=MibTableRow
awnStatisticsVccWanTsEntry=_AwnStatisticsVccWanTsEntry_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1))
awnStatisticsVccWanTsEntry.setIndexNames((0,_C,_AP),(0,_C,_AQ),(0,_C,_AR),(0,_C,_AS),(0,_C,_AT),(0,_C,_AU),(0,_C,_AV))
if mibBuilder.loadTexts:awnStatisticsVccWanTsEntry.setStatus(_A)
class _AwnStatisticsVccWanTsUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsVccWanTsUnit_Type.__name__=_D
_AwnStatisticsVccWanTsUnit_Object=MibTableColumn
awnStatisticsVccWanTsUnit=_AwnStatisticsVccWanTsUnit_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,1),_AwnStatisticsVccWanTsUnit_Type())
awnStatisticsVccWanTsUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsUnit.setStatus(_A)
class _AwnStatisticsVccWanTsCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsVccWanTsCard_Type.__name__=_D
_AwnStatisticsVccWanTsCard_Object=MibTableColumn
awnStatisticsVccWanTsCard=_AwnStatisticsVccWanTsCard_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,2),_AwnStatisticsVccWanTsCard_Type())
awnStatisticsVccWanTsCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsCard.setStatus(_A)
class _AwnStatisticsVccWanTsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsVccWanTsPort_Type.__name__=_D
_AwnStatisticsVccWanTsPort_Object=MibTableColumn
awnStatisticsVccWanTsPort=_AwnStatisticsVccWanTsPort_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,3),_AwnStatisticsVccWanTsPort_Type())
awnStatisticsVccWanTsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsPort.setStatus(_A)
class _AwnStatisticsVccWanTsTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AwnStatisticsVccWanTsTs_Type.__name__=_D
_AwnStatisticsVccWanTsTs_Object=MibTableColumn
awnStatisticsVccWanTsTs=_AwnStatisticsVccWanTsTs_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,4),_AwnStatisticsVccWanTsTs_Type())
awnStatisticsVccWanTsTs.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsTs.setStatus(_A)
class _AwnStatisticsVccWanTsVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AwnStatisticsVccWanTsVpi_Type.__name__=_D
_AwnStatisticsVccWanTsVpi_Object=MibTableColumn
awnStatisticsVccWanTsVpi=_AwnStatisticsVccWanTsVpi_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,5),_AwnStatisticsVccWanTsVpi_Type())
awnStatisticsVccWanTsVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsVpi.setStatus(_A)
class _AwnStatisticsVccWanTsVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AwnStatisticsVccWanTsVci_Type.__name__=_D
_AwnStatisticsVccWanTsVci_Object=MibTableColumn
awnStatisticsVccWanTsVci=_AwnStatisticsVccWanTsVci_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,6),_AwnStatisticsVccWanTsVci_Type())
awnStatisticsVccWanTsVci.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsVci.setStatus(_A)
class _AwnStatisticsVccWanTsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsVccWanTsType_Type.__name__=_D
_AwnStatisticsVccWanTsType_Object=MibTableColumn
awnStatisticsVccWanTsType=_AwnStatisticsVccWanTsType_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,7),_AwnStatisticsVccWanTsType_Type())
awnStatisticsVccWanTsType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsType.setStatus(_A)
class _AwnStatisticsVccWanTsData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AwnStatisticsVccWanTsData_Type.__name__=_F
_AwnStatisticsVccWanTsData_Object=MibTableColumn
awnStatisticsVccWanTsData=_AwnStatisticsVccWanTsData_Object((1,3,6,1,4,1,211,1,127,29,2,13,1,1,8),_AwnStatisticsVccWanTsData_Type())
awnStatisticsVccWanTsData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccWanTsData.setStatus(_A)
_AwnStatisticsVccFrLine_ObjectIdentity=ObjectIdentity
awnStatisticsVccFrLine=_AwnStatisticsVccFrLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,14))
_AwnStatisticsVccFrLineTable_Object=MibTable
awnStatisticsVccFrLineTable=_AwnStatisticsVccFrLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,14,1))
if mibBuilder.loadTexts:awnStatisticsVccFrLineTable.setStatus(_A)
_AwnStatisticsVccFrLineEntry_Object=MibTableRow
awnStatisticsVccFrLineEntry=_AwnStatisticsVccFrLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1))
awnStatisticsVccFrLineEntry.setIndexNames((0,_C,_AW),(0,_C,_AX),(0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa),(0,_C,_Ab))
if mibBuilder.loadTexts:awnStatisticsVccFrLineEntry.setStatus(_A)
class _AwnStatisticsVccFrLineUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsVccFrLineUnit_Type.__name__=_D
_AwnStatisticsVccFrLineUnit_Object=MibTableColumn
awnStatisticsVccFrLineUnit=_AwnStatisticsVccFrLineUnit_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1,1),_AwnStatisticsVccFrLineUnit_Type())
awnStatisticsVccFrLineUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFrLineUnit.setStatus(_A)
class _AwnStatisticsVccFrLineCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsVccFrLineCard_Type.__name__=_D
_AwnStatisticsVccFrLineCard_Object=MibTableColumn
awnStatisticsVccFrLineCard=_AwnStatisticsVccFrLineCard_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1,2),_AwnStatisticsVccFrLineCard_Type())
awnStatisticsVccFrLineCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFrLineCard.setStatus(_A)
class _AwnStatisticsVccFrLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsVccFrLinePort_Type.__name__=_D
_AwnStatisticsVccFrLinePort_Object=MibTableColumn
awnStatisticsVccFrLinePort=_AwnStatisticsVccFrLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1,3),_AwnStatisticsVccFrLinePort_Type())
awnStatisticsVccFrLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFrLinePort.setStatus(_A)
class _AwnStatisticsVccFrLineTimeslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AwnStatisticsVccFrLineTimeslot_Type.__name__=_D
_AwnStatisticsVccFrLineTimeslot_Object=MibTableColumn
awnStatisticsVccFrLineTimeslot=_AwnStatisticsVccFrLineTimeslot_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1,4),_AwnStatisticsVccFrLineTimeslot_Type())
awnStatisticsVccFrLineTimeslot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFrLineTimeslot.setStatus(_A)
class _AwnStatisticsVccFrLineDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1022))
_AwnStatisticsVccFrLineDlci_Type.__name__=_D
_AwnStatisticsVccFrLineDlci_Object=MibTableColumn
awnStatisticsVccFrLineDlci=_AwnStatisticsVccFrLineDlci_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1,5),_AwnStatisticsVccFrLineDlci_Type())
awnStatisticsVccFrLineDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFrLineDlci.setStatus(_A)
class _AwnStatisticsVccFrLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsVccFrLineType_Type.__name__=_D
_AwnStatisticsVccFrLineType_Object=MibTableColumn
awnStatisticsVccFrLineType=_AwnStatisticsVccFrLineType_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1,6),_AwnStatisticsVccFrLineType_Type())
awnStatisticsVccFrLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFrLineType.setStatus(_A)
class _AwnStatisticsVccFrLineData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AwnStatisticsVccFrLineData_Type.__name__=_F
_AwnStatisticsVccFrLineData_Object=MibTableColumn
awnStatisticsVccFrLineData=_AwnStatisticsVccFrLineData_Object((1,3,6,1,4,1,211,1,127,29,2,14,1,1,7),_AwnStatisticsVccFrLineData_Type())
awnStatisticsVccFrLineData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFrLineData.setStatus(_A)
_AwnStatisticsVccFfLine_ObjectIdentity=ObjectIdentity
awnStatisticsVccFfLine=_AwnStatisticsVccFfLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,15))
_AwnStatisticsVccFfLineTable_Object=MibTable
awnStatisticsVccFfLineTable=_AwnStatisticsVccFfLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,15,1))
if mibBuilder.loadTexts:awnStatisticsVccFfLineTable.setStatus(_A)
_AwnStatisticsVccFfLineEntry_Object=MibTableRow
awnStatisticsVccFfLineEntry=_AwnStatisticsVccFfLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,15,1,1))
awnStatisticsVccFfLineEntry.setIndexNames((0,_C,_Ac),(0,_C,_Ad),(0,_C,_Ae),(0,_C,_Af),(0,_C,_Ag))
if mibBuilder.loadTexts:awnStatisticsVccFfLineEntry.setStatus(_A)
class _AwnStatisticsVccFfLineUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsVccFfLineUnit_Type.__name__=_D
_AwnStatisticsVccFfLineUnit_Object=MibTableColumn
awnStatisticsVccFfLineUnit=_AwnStatisticsVccFfLineUnit_Object((1,3,6,1,4,1,211,1,127,29,2,15,1,1,1),_AwnStatisticsVccFfLineUnit_Type())
awnStatisticsVccFfLineUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFfLineUnit.setStatus(_A)
class _AwnStatisticsVccFfLineCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsVccFfLineCard_Type.__name__=_D
_AwnStatisticsVccFfLineCard_Object=MibTableColumn
awnStatisticsVccFfLineCard=_AwnStatisticsVccFfLineCard_Object((1,3,6,1,4,1,211,1,127,29,2,15,1,1,2),_AwnStatisticsVccFfLineCard_Type())
awnStatisticsVccFfLineCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFfLineCard.setStatus(_A)
class _AwnStatisticsVccFfLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsVccFfLinePort_Type.__name__=_D
_AwnStatisticsVccFfLinePort_Object=MibTableColumn
awnStatisticsVccFfLinePort=_AwnStatisticsVccFfLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,15,1,1,3),_AwnStatisticsVccFfLinePort_Type())
awnStatisticsVccFfLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFfLinePort.setStatus(_A)
class _AwnStatisticsVccFfLineTimeslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AwnStatisticsVccFfLineTimeslot_Type.__name__=_D
_AwnStatisticsVccFfLineTimeslot_Object=MibTableColumn
awnStatisticsVccFfLineTimeslot=_AwnStatisticsVccFfLineTimeslot_Object((1,3,6,1,4,1,211,1,127,29,2,15,1,1,4),_AwnStatisticsVccFfLineTimeslot_Type())
awnStatisticsVccFfLineTimeslot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFfLineTimeslot.setStatus(_A)
class _AwnStatisticsVccFfLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsVccFfLineType_Type.__name__=_D
_AwnStatisticsVccFfLineType_Object=MibTableColumn
awnStatisticsVccFfLineType=_AwnStatisticsVccFfLineType_Object((1,3,6,1,4,1,211,1,127,29,2,15,1,1,5),_AwnStatisticsVccFfLineType_Type())
awnStatisticsVccFfLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFfLineType.setStatus(_A)
class _AwnStatisticsVccFfLineData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AwnStatisticsVccFfLineData_Type.__name__=_F
_AwnStatisticsVccFfLineData_Object=MibTableColumn
awnStatisticsVccFfLineData=_AwnStatisticsVccFfLineData_Object((1,3,6,1,4,1,211,1,127,29,2,15,1,1,6),_AwnStatisticsVccFfLineData_Type())
awnStatisticsVccFfLineData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsVccFfLineData.setStatus(_A)
_AwnStatisticsLsWanVp_ObjectIdentity=ObjectIdentity
awnStatisticsLsWanVp=_AwnStatisticsLsWanVp_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,16))
_AwnStatisticsLsWanVpTable_Object=MibTable
awnStatisticsLsWanVpTable=_AwnStatisticsLsWanVpTable_Object((1,3,6,1,4,1,211,1,127,29,2,16,1))
if mibBuilder.loadTexts:awnStatisticsLsWanVpTable.setStatus(_A)
_AwnStatisticsLsWanVpEntry_Object=MibTableRow
awnStatisticsLsWanVpEntry=_AwnStatisticsLsWanVpEntry_Object((1,3,6,1,4,1,211,1,127,29,2,16,1,1))
awnStatisticsLsWanVpEntry.setIndexNames((0,_C,_Ah),(0,_C,_Ai),(0,_C,_Aj),(0,_C,_Ak))
if mibBuilder.loadTexts:awnStatisticsLsWanVpEntry.setStatus(_A)
class _AwnStatisticsLsWanVpUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsWanVpUnit_Type.__name__=_D
_AwnStatisticsLsWanVpUnit_Object=MibTableColumn
awnStatisticsLsWanVpUnit=_AwnStatisticsLsWanVpUnit_Object((1,3,6,1,4,1,211,1,127,29,2,16,1,1,1),_AwnStatisticsLsWanVpUnit_Type())
awnStatisticsLsWanVpUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpUnit.setStatus(_A)
class _AwnStatisticsLsWanVpCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsLsWanVpCard_Type.__name__=_D
_AwnStatisticsLsWanVpCard_Object=MibTableColumn
awnStatisticsLsWanVpCard=_AwnStatisticsLsWanVpCard_Object((1,3,6,1,4,1,211,1,127,29,2,16,1,1,2),_AwnStatisticsLsWanVpCard_Type())
awnStatisticsLsWanVpCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpCard.setStatus(_A)
class _AwnStatisticsLsWanVpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsWanVpPort_Type.__name__=_D
_AwnStatisticsLsWanVpPort_Object=MibTableColumn
awnStatisticsLsWanVpPort=_AwnStatisticsLsWanVpPort_Object((1,3,6,1,4,1,211,1,127,29,2,16,1,1,3),_AwnStatisticsLsWanVpPort_Type())
awnStatisticsLsWanVpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpPort.setStatus(_A)
class _AwnStatisticsLsWanVpVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_AwnStatisticsLsWanVpVpi_Type.__name__=_D
_AwnStatisticsLsWanVpVpi_Object=MibTableColumn
awnStatisticsLsWanVpVpi=_AwnStatisticsLsWanVpVpi_Object((1,3,6,1,4,1,211,1,127,29,2,16,1,1,4),_AwnStatisticsLsWanVpVpi_Type())
awnStatisticsLsWanVpVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpVpi.setStatus(_A)
class _AwnStatisticsLsWanVpData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(456,456));fixedLength=456
_AwnStatisticsLsWanVpData_Type.__name__=_E
_AwnStatisticsLsWanVpData_Object=MibTableColumn
awnStatisticsLsWanVpData=_AwnStatisticsLsWanVpData_Object((1,3,6,1,4,1,211,1,127,29,2,16,1,1,5),_AwnStatisticsLsWanVpData_Type())
awnStatisticsLsWanVpData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpData.setStatus(_A)
_AwnStatisticsLsWanVpRt_ObjectIdentity=ObjectIdentity
awnStatisticsLsWanVpRt=_AwnStatisticsLsWanVpRt_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,17))
_AwnStatisticsLsWanVpRtTable_Object=MibTable
awnStatisticsLsWanVpRtTable=_AwnStatisticsLsWanVpRtTable_Object((1,3,6,1,4,1,211,1,127,29,2,17,1))
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtTable.setStatus(_A)
_AwnStatisticsLsWanVpRtEntry_Object=MibTableRow
awnStatisticsLsWanVpRtEntry=_AwnStatisticsLsWanVpRtEntry_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1))
awnStatisticsLsWanVpRtEntry.setIndexNames((0,_C,_Al),(0,_C,_Am),(0,_C,_An),(0,_C,_Ao),(0,_C,_Ap),(0,_C,_Aq))
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtEntry.setStatus(_A)
class _AwnStatisticsLsWanVpRtUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsWanVpRtUnit_Type.__name__=_D
_AwnStatisticsLsWanVpRtUnit_Object=MibTableColumn
awnStatisticsLsWanVpRtUnit=_AwnStatisticsLsWanVpRtUnit_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1,1),_AwnStatisticsLsWanVpRtUnit_Type())
awnStatisticsLsWanVpRtUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtUnit.setStatus(_A)
class _AwnStatisticsLsWanVpRtCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsLsWanVpRtCard_Type.__name__=_D
_AwnStatisticsLsWanVpRtCard_Object=MibTableColumn
awnStatisticsLsWanVpRtCard=_AwnStatisticsLsWanVpRtCard_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1,2),_AwnStatisticsLsWanVpRtCard_Type())
awnStatisticsLsWanVpRtCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtCard.setStatus(_A)
class _AwnStatisticsLsWanVpRtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AwnStatisticsLsWanVpRtPort_Type.__name__=_D
_AwnStatisticsLsWanVpRtPort_Object=MibTableColumn
awnStatisticsLsWanVpRtPort=_AwnStatisticsLsWanVpRtPort_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1,3),_AwnStatisticsLsWanVpRtPort_Type())
awnStatisticsLsWanVpRtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtPort.setStatus(_A)
class _AwnStatisticsLsWanVpRtVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_AwnStatisticsLsWanVpRtVpi_Type.__name__=_D
_AwnStatisticsLsWanVpRtVpi_Object=MibTableColumn
awnStatisticsLsWanVpRtVpi=_AwnStatisticsLsWanVpRtVpi_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1,4),_AwnStatisticsLsWanVpRtVpi_Type())
awnStatisticsLsWanVpRtVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtVpi.setStatus(_A)
class _AwnStatisticsLsWanVpRtCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_AwnStatisticsLsWanVpRtCategory_Type.__name__=_D
_AwnStatisticsLsWanVpRtCategory_Object=MibTableColumn
awnStatisticsLsWanVpRtCategory=_AwnStatisticsLsWanVpRtCategory_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1,5),_AwnStatisticsLsWanVpRtCategory_Type())
awnStatisticsLsWanVpRtCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtCategory.setStatus(_A)
class _AwnStatisticsLsWanVpRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AwnStatisticsLsWanVpRtType_Type.__name__=_D
_AwnStatisticsLsWanVpRtType_Object=MibTableColumn
awnStatisticsLsWanVpRtType=_AwnStatisticsLsWanVpRtType_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1,6),_AwnStatisticsLsWanVpRtType_Type())
awnStatisticsLsWanVpRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtType.setStatus(_A)
class _AwnStatisticsLsWanVpRtData_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AwnStatisticsLsWanVpRtData_Type.__name__=_F
_AwnStatisticsLsWanVpRtData_Object=MibTableColumn
awnStatisticsLsWanVpRtData=_AwnStatisticsLsWanVpRtData_Object((1,3,6,1,4,1,211,1,127,29,2,17,1,1,7),_AwnStatisticsLsWanVpRtData_Type())
awnStatisticsLsWanVpRtData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsWanVpRtData.setStatus(_A)
_AwnStatisticsComAtmLine_ObjectIdentity=ObjectIdentity
awnStatisticsComAtmLine=_AwnStatisticsComAtmLine_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,18))
_AwnStatisticsComAtmLineTable_Object=MibTable
awnStatisticsComAtmLineTable=_AwnStatisticsComAtmLineTable_Object((1,3,6,1,4,1,211,1,127,29,2,18,1))
if mibBuilder.loadTexts:awnStatisticsComAtmLineTable.setStatus(_A)
_AwnStatisticsComAtmLineEntry_Object=MibTableRow
awnStatisticsComAtmLineEntry=_AwnStatisticsComAtmLineEntry_Object((1,3,6,1,4,1,211,1,127,29,2,18,1,1))
awnStatisticsComAtmLineEntry.setIndexNames((0,_C,_Ar),(0,_C,_As),(0,_C,_At),(0,_C,_Au))
if mibBuilder.loadTexts:awnStatisticsComAtmLineEntry.setStatus(_A)
class _AwnStatisticsComAtmLineSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComAtmLineSlot_Type.__name__=_D
_AwnStatisticsComAtmLineSlot_Object=MibTableColumn
awnStatisticsComAtmLineSlot=_AwnStatisticsComAtmLineSlot_Object((1,3,6,1,4,1,211,1,127,29,2,18,1,1,1),_AwnStatisticsComAtmLineSlot_Type())
awnStatisticsComAtmLineSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComAtmLineSlot.setStatus(_A)
class _AwnStatisticsComAtmLineAdapter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AwnStatisticsComAtmLineAdapter_Type.__name__=_D
_AwnStatisticsComAtmLineAdapter_Object=MibTableColumn
awnStatisticsComAtmLineAdapter=_AwnStatisticsComAtmLineAdapter_Object((1,3,6,1,4,1,211,1,127,29,2,18,1,1,2),_AwnStatisticsComAtmLineAdapter_Type())
awnStatisticsComAtmLineAdapter.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComAtmLineAdapter.setStatus(_A)
class _AwnStatisticsComAtmLinePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwnStatisticsComAtmLinePort_Type.__name__=_D
_AwnStatisticsComAtmLinePort_Object=MibTableColumn
awnStatisticsComAtmLinePort=_AwnStatisticsComAtmLinePort_Object((1,3,6,1,4,1,211,1,127,29,2,18,1,1,3),_AwnStatisticsComAtmLinePort_Type())
awnStatisticsComAtmLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComAtmLinePort.setStatus(_A)
class _AwnStatisticsComAtmLineVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AwnStatisticsComAtmLineVpi_Type.__name__=_D
_AwnStatisticsComAtmLineVpi_Object=MibTableColumn
awnStatisticsComAtmLineVpi=_AwnStatisticsComAtmLineVpi_Object((1,3,6,1,4,1,211,1,127,29,2,18,1,1,4),_AwnStatisticsComAtmLineVpi_Type())
awnStatisticsComAtmLineVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComAtmLineVpi.setStatus(_A)
class _AwnStatisticsComAtmLineData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(104,104));fixedLength=104
_AwnStatisticsComAtmLineData_Type.__name__=_E
_AwnStatisticsComAtmLineData_Object=MibScalar
awnStatisticsComAtmLineData=_AwnStatisticsComAtmLineData_Object((1,3,6,1,4,1,211,1,127,29,2,18,1,1,5),_AwnStatisticsComAtmLineData_Type())
awnStatisticsComAtmLineData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsComAtmLineData.setStatus(_A)
_AwnStatisticsLsTs_ObjectIdentity=ObjectIdentity
awnStatisticsLsTs=_AwnStatisticsLsTs_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,19))
_AwnStatisticsLsTsTable_Object=MibTable
awnStatisticsLsTsTable=_AwnStatisticsLsTsTable_Object((1,3,6,1,4,1,211,1,127,29,2,19,1))
if mibBuilder.loadTexts:awnStatisticsLsTsTable.setStatus(_A)
_AwnStatisticsLsTsEntry_Object=MibTableRow
awnStatisticsLsTsEntry=_AwnStatisticsLsTsEntry_Object((1,3,6,1,4,1,211,1,127,29,2,19,1,1))
awnStatisticsLsTsEntry.setIndexNames((0,_C,_Av),(0,_C,_Aw),(0,_C,_Ax),(0,_C,_Ay))
if mibBuilder.loadTexts:awnStatisticsLsTsEntry.setStatus(_A)
class _AwnStatisticsLsTsUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsTsUnit_Type.__name__=_D
_AwnStatisticsLsTsUnit_Object=MibTableColumn
awnStatisticsLsTsUnit=_AwnStatisticsLsTsUnit_Object((1,3,6,1,4,1,211,1,127,29,2,19,1,1,1),_AwnStatisticsLsTsUnit_Type())
awnStatisticsLsTsUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsTsUnit.setStatus(_A)
class _AwnStatisticsLsTsCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsLsTsCard_Type.__name__=_D
_AwnStatisticsLsTsCard_Object=MibTableColumn
awnStatisticsLsTsCard=_AwnStatisticsLsTsCard_Object((1,3,6,1,4,1,211,1,127,29,2,19,1,1,2),_AwnStatisticsLsTsCard_Type())
awnStatisticsLsTsCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsTsCard.setStatus(_A)
class _AwnStatisticsLsTsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsLsTsPort_Type.__name__=_D
_AwnStatisticsLsTsPort_Object=MibTableColumn
awnStatisticsLsTsPort=_AwnStatisticsLsTsPort_Object((1,3,6,1,4,1,211,1,127,29,2,19,1,1,3),_AwnStatisticsLsTsPort_Type())
awnStatisticsLsTsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsTsPort.setStatus(_A)
class _AwnStatisticsLsTsTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_AwnStatisticsLsTsTs_Type.__name__=_D
_AwnStatisticsLsTsTs_Object=MibTableColumn
awnStatisticsLsTsTs=_AwnStatisticsLsTsTs_Object((1,3,6,1,4,1,211,1,127,29,2,19,1,1,4),_AwnStatisticsLsTsTs_Type())
awnStatisticsLsTsTs.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsTsTs.setStatus(_A)
class _AwnStatisticsLsTsData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(104,104));fixedLength=104
_AwnStatisticsLsTsData_Type.__name__=_E
_AwnStatisticsLsTsData_Object=MibTableColumn
awnStatisticsLsTsData=_AwnStatisticsLsTsData_Object((1,3,6,1,4,1,211,1,127,29,2,19,1,1,5),_AwnStatisticsLsTsData_Type())
awnStatisticsLsTsData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsLsTsData.setStatus(_A)
_AwnStatisticsSys_ObjectIdentity=ObjectIdentity
awnStatisticsSys=_AwnStatisticsSys_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,20))
class _AwnStatisticsSysDroppedCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(100,100));fixedLength=100
_AwnStatisticsSysDroppedCells_Type.__name__=_E
_AwnStatisticsSysDroppedCells_Object=MibScalar
awnStatisticsSysDroppedCells=_AwnStatisticsSysDroppedCells_Object((1,3,6,1,4,1,211,1,127,29,2,20,1),_AwnStatisticsSysDroppedCells_Type())
awnStatisticsSysDroppedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsSysDroppedCells.setStatus(_A)
_AwnStatisticsIpFrame_ObjectIdentity=ObjectIdentity
awnStatisticsIpFrame=_AwnStatisticsIpFrame_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,21))
_AwnStatisticsIpFrameTable_Object=MibTable
awnStatisticsIpFrameTable=_AwnStatisticsIpFrameTable_Object((1,3,6,1,4,1,211,1,127,29,2,21,1))
if mibBuilder.loadTexts:awnStatisticsIpFrameTable.setStatus(_A)
_AwnStatisticsIpFrameEntry_Object=MibTableRow
awnStatisticsIpFrameEntry=_AwnStatisticsIpFrameEntry_Object((1,3,6,1,4,1,211,1,127,29,2,21,1,1))
awnStatisticsIpFrameEntry.setIndexNames((0,_C,_Az))
if mibBuilder.loadTexts:awnStatisticsIpFrameEntry.setStatus(_A)
_AwnStatisticsIpFrameAddr_Type=IpAddress
_AwnStatisticsIpFrameAddr_Object=MibTableColumn
awnStatisticsIpFrameAddr=_AwnStatisticsIpFrameAddr_Object((1,3,6,1,4,1,211,1,127,29,2,21,1,1,1),_AwnStatisticsIpFrameAddr_Type())
awnStatisticsIpFrameAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsIpFrameAddr.setStatus(_A)
class _AwnStatisticsIpFrameData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(108,108));fixedLength=108
_AwnStatisticsIpFrameData_Type.__name__=_E
_AwnStatisticsIpFrameData_Object=MibTableColumn
awnStatisticsIpFrameData=_AwnStatisticsIpFrameData_Object((1,3,6,1,4,1,211,1,127,29,2,21,1,1,2),_AwnStatisticsIpFrameData_Type())
awnStatisticsIpFrameData.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsIpFrameData.setStatus(_A)
_AwnStatisticsDlci_ObjectIdentity=ObjectIdentity
awnStatisticsDlci=_AwnStatisticsDlci_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,2,22))
_AwnStatisticsDlciTable_Object=MibTable
awnStatisticsDlciTable=_AwnStatisticsDlciTable_Object((1,3,6,1,4,1,211,1,127,29,2,22,1))
if mibBuilder.loadTexts:awnStatisticsDlciTable.setStatus(_A)
_AwnStatisticsDlciEntry_Object=MibTableRow
awnStatisticsDlciEntry=_AwnStatisticsDlciEntry_Object((1,3,6,1,4,1,211,1,127,29,2,22,1,1))
awnStatisticsDlciEntry.setIndexNames((0,_C,_A_),(0,_C,_B0),(0,_C,_B1),(0,_C,_B2),(0,_C,_B3))
if mibBuilder.loadTexts:awnStatisticsDlciEntry.setStatus(_A)
class _AwnStatisticsDlciUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsDlciUnit_Type.__name__=_D
_AwnStatisticsDlciUnit_Object=MibTableColumn
awnStatisticsDlciUnit=_AwnStatisticsDlciUnit_Object((1,3,6,1,4,1,211,1,127,29,2,22,1,1,1),_AwnStatisticsDlciUnit_Type())
awnStatisticsDlciUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsDlciUnit.setStatus(_A)
class _AwnStatisticsDlciCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_AwnStatisticsDlciCard_Type.__name__=_D
_AwnStatisticsDlciCard_Object=MibTableColumn
awnStatisticsDlciCard=_AwnStatisticsDlciCard_Object((1,3,6,1,4,1,211,1,127,29,2,22,1,1,2),_AwnStatisticsDlciCard_Type())
awnStatisticsDlciCard.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsDlciCard.setStatus(_A)
class _AwnStatisticsDlciPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AwnStatisticsDlciPort_Type.__name__=_D
_AwnStatisticsDlciPort_Object=MibTableColumn
awnStatisticsDlciPort=_AwnStatisticsDlciPort_Object((1,3,6,1,4,1,211,1,127,29,2,22,1,1,3),_AwnStatisticsDlciPort_Type())
awnStatisticsDlciPort.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsDlciPort.setStatus(_A)
class _AwnStatisticsDlciTimeslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AwnStatisticsDlciTimeslot_Type.__name__=_D
_AwnStatisticsDlciTimeslot_Object=MibTableColumn
awnStatisticsDlciTimeslot=_AwnStatisticsDlciTimeslot_Object((1,3,6,1,4,1,211,1,127,29,2,22,1,1,4),_AwnStatisticsDlciTimeslot_Type())
awnStatisticsDlciTimeslot.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsDlciTimeslot.setStatus(_A)
class _AwnStatisticsDlciDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1022))
_AwnStatisticsDlciDlci_Type.__name__=_D
_AwnStatisticsDlciDlci_Object=MibTableColumn
awnStatisticsDlciDlci=_AwnStatisticsDlciDlci_Object((1,3,6,1,4,1,211,1,127,29,2,22,1,1,5),_AwnStatisticsDlciDlci_Type())
awnStatisticsDlciDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsDlciDlci.setStatus(_A)
class _AwnStatisticsDlciBriClad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(168,168));fixedLength=168
_AwnStatisticsDlciBriClad_Type.__name__=_E
_AwnStatisticsDlciBriClad_Object=MibTableColumn
awnStatisticsDlciBriClad=_AwnStatisticsDlciBriClad_Object((1,3,6,1,4,1,211,1,127,29,2,22,1,1,6),_AwnStatisticsDlciBriClad_Type())
awnStatisticsDlciBriClad.setMaxAccess(_B)
if mibBuilder.loadTexts:awnStatisticsDlciBriClad.setStatus(_A)
_AwnIlmi_ObjectIdentity=ObjectIdentity
awnIlmi=_AwnIlmi_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,3))
_AwnIlmiIns_ObjectIdentity=ObjectIdentity
awnIlmiIns=_AwnIlmiIns_ObjectIdentity((1,3,6,1,4,1,211,1,127,29,3,1))
_AwnIlmiInsRouteadd_Type=Integer32
_AwnIlmiInsRouteadd_Object=MibScalar
awnIlmiInsRouteadd=_AwnIlmiInsRouteadd_Object((1,3,6,1,4,1,211,1,127,29,3,1,1),_AwnIlmiInsRouteadd_Type())
awnIlmiInsRouteadd.setMaxAccess(_B)
if mibBuilder.loadTexts:awnIlmiInsRouteadd.setStatus(_A)
_AwnIlmiInsRoutedel_Type=Integer32
_AwnIlmiInsRoutedel_Object=MibScalar
awnIlmiInsRoutedel=_AwnIlmiInsRoutedel_Object((1,3,6,1,4,1,211,1,127,29,3,1,2),_AwnIlmiInsRoutedel_Type())
awnIlmiInsRoutedel.setMaxAccess(_B)
if mibBuilder.loadTexts:awnIlmiInsRoutedel.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fujitsu':fujitsu,'product':product,'nonos':nonos,'awn':awn,'awnSystem':awnSystem,'awnSysNode':awnSysNode,'awnSysNodeInformation':awnSysNodeInformation,'awnSysNodeCommonStatus':awnSysNodeCommonStatus,'awnSysNodeClk':awnSysNodeClk,'awnSysCom':awnSysCom,'awnSysComDevice':awnSysComDevice,'awnSysComPort':awnSysComPort,'awnSysComDevice2':awnSysComDevice2,'awnSysComPort2':awnSysComPort2,'awnSysLs':awnSysLs,'awnSysLsTable':awnSysLsTable,'awnSysLsEntry':awnSysLsEntry,_I:awnSysLsUnit,'awnSysLsDevice':awnSysLsDevice,'awnSysLsPort':awnSysLsPort,'awnSysLsDevice2':awnSysLsDevice2,'awnSysLsPort2':awnSysLsPort2,'awnSysLine':awnSysLine,'awnSysLineTable':awnSysLineTable,'awnSysLineEntry':awnSysLineEntry,_J:awnSysLineUnit,_K:awnSysLineCard,_L:awnSysLinePort,'awnSysLineChannel':awnSysLineChannel,'awnSysLineMegalink':awnSysLineMegalink,'awnSysError':awnSysError,'awnSysErrorLog':awnSysErrorLog,'awnSysChannel':awnSysChannel,'awnSysChannelTable':awnSysChannelTable,'awnSysChannelEntry':awnSysChannelEntry,_M:awnSysChannelUnit,_N:awnSysChannelCard,_O:awnSysChannelPort,_P:awnSysChannelTimeslot,'awnSysChannelBackup':awnSysChannelBackup,'awnSysChannelBackup2':awnSysChannelBackup2,'awnSysEvent':awnSysEvent,'awnSysEventTable':awnSysEventTable,'awnSysEventEntry':awnSysEventEntry,'awnSysEventThreshold':awnSysEventThreshold,'awnSysPort':awnSysPort,'awnSysPortTable':awnSysPortTable,'awnSysPortEntry':awnSysPortEntry,_Q:awnSysPortSlot,_R:awnSysPortAdapter,_S:awnSysPortPort,'awnSysPortMegalink':awnSysPortMegalink,'awnSysPortMegalink2':awnSysPortMegalink2,'awnSysConnComVcc':awnSysConnComVcc,'awnSysConnComVccTable':awnSysConnComVccTable,'awnSysConnComVccEntry':awnSysConnComVccEntry,_T:awnSysConnComVccSlot,_U:awnSysConnComVccAdapter,_V:awnSysConnComVccPort,_W:awnSysConnComVccVpi,_X:awnSysConnComVccVci,'awnSysConnComVccState':awnSysConnComVccState,'awnSysConnLsVcc':awnSysConnLsVcc,'awnSysConnLsVccTable':awnSysConnLsVccTable,'awnSysConnLsVccEntry':awnSysConnLsVccEntry,_Y:awnSysConnLsVccUnit,'awnSysConnLSVccCard':awnSysConnLSVccCard,_Z:awnSysConnLsVccPort,_a:awnSysConnLsVccTimeslot,_b:awnSysConnLsVccVpi,_c:awnSysConnLsVccVci,'awnSysConnLsVccState':awnSysConnLsVccState,'awnSysBackIpAddr':awnSysBackIpAddr,'awnStatistics':awnStatistics,'awnStatisticsSw':awnStatisticsSw,'awnStatisticsSwport':awnStatisticsSwport,'awnStatisticsLine':awnStatisticsLine,'awnStatisticsLineTable':awnStatisticsLineTable,'awnStatisticsLineEntry':awnStatisticsLineEntry,_d:awnStatisticsLineUnit,_e:awnStatisticsLineCard,_f:awnStatisticsLinePort,'awnStatisticsLinePriWan':awnStatisticsLinePriWan,'awnStatisticsLineSriWan':awnStatisticsLineSriWan,'awnStatisticsLineBriWan':awnStatisticsLineBriWan,'awnStatisticsComLine':awnStatisticsComLine,'awnStatisticsComLineTable':awnStatisticsComLineTable,'awnStatisticsComLineEntry':awnStatisticsComLineEntry,_g:awnStatisticsComLineSlot,_h:awnStatisticsComLineAdapter,_i:awnStatisticsComLinePort,'awnStatisticsComLineAtm':awnStatisticsComLineAtm,'awnStatisticsComLan':awnStatisticsComLan,'awnStatisticsLsLine':awnStatisticsLsLine,'awnStatisticsLsLineTable':awnStatisticsLsLineTable,'awnStatisticsLsLineEntry':awnStatisticsLsLineEntry,_j:awnStatisticsLsLineUnit,_k:awnStatisticsLsLineCard,_l:awnStatisticsLsLinePort,'awnStatisticsLsLinePriWan':awnStatisticsLsLinePriWan,'awnStatisticsLsLineBriWan':awnStatisticsLsLineBriWan,'awnStatisticsLsLinePriBup':awnStatisticsLsLinePriBup,'awnStatisticsLsLineFrclad':awnStatisticsLsLineFrclad,'awnStatisticsLsLineFrclad2':awnStatisticsLsLineFrclad2,'awnStatisticsLsLineFrclad3':awnStatisticsLsLineFrclad3,'awnStatisticsLsLineLineDif':awnStatisticsLsLineLineDif,'awnStatisticsLsLineDifFrclad':awnStatisticsLsLineDifFrclad,'awnStatisticsLsLinePriCes':awnStatisticsLsLinePriCes,'awnStatisticsLsLineDtkCodec':awnStatisticsLsLineDtkCodec,'awnStatisticsLsLineDtkDclad':awnStatisticsLsLineDtkDclad,'awnStatisticsLsLineDtkDclad2':awnStatisticsLsLineDtkDclad2,'awnStatisticsLsLineOdtCodec':awnStatisticsLsLineOdtCodec,'awnStatisticsLsLineOdtDclad':awnStatisticsLsLineOdtDclad,'awnStatisticsLsLineSriCes':awnStatisticsLsLineSriCes,'awnStatisticsLsLineBriBup':awnStatisticsLsLineBriBup,'awnStatisticsLsLineLrcrad':awnStatisticsLsLineLrcrad,'awnStatisticsLsLine45Mwan':awnStatisticsLsLine45Mwan,'awnStatisticsLsLineOdtCodecS':awnStatisticsLsLineOdtCodecS,'awnStatisticsLsLinePriWan24':awnStatisticsLsLinePriWan24,'awnStatisticsLsLineFfclad24a':awnStatisticsLsLineFfclad24a,'awnStatisticsLsLineFfclad24b':awnStatisticsLsLineFfclad24b,'awnStatisticsLsLineFfclad24c':awnStatisticsLsLineFfclad24c,'awnStatisticsLsLineVxaWan':awnStatisticsLsLineVxaWan,'awnStatisticsLsLineBriClad':awnStatisticsLsLineBriClad,'awnStatisticsComNniPort':awnStatisticsComNniPort,'awnStatisticsComNniPortTable':awnStatisticsComNniPortTable,'awnStatisticsComNniPortEntry':awnStatisticsComNniPortEntry,_m:awnStatisticsComNniPortSlot,_n:awnStatisticsComNniPortAdapter,_o:awnStatisticsComNniPortPort,'awnStatisticsComNniPortData':awnStatisticsComNniPortData,'awnStatisticsComNniVp':awnStatisticsComNniVp,'awnStatisticsComNniVpTable':awnStatisticsComNniVpTable,'awnStatisticsComNniVpEntry':awnStatisticsComNniVpEntry,_p:awnStatisticsComNniVpSlot,_q:awnStatisticsComNniVpAdapter,_r:awnStatisticsComNniVpPort,_s:awnStatisticsComNniVpVpi,'awnStatisticsComNniVptData':awnStatisticsComNniVptData,'awnStatisticsLsWanTs':awnStatisticsLsWanTs,'awnStatisticsLsWanTsTable':awnStatisticsLsWanTsTable,'awnStatisticsLsWanTsEntry':awnStatisticsLsWanTsEntry,_t:awnStatisticsLsWanTsUnit,_u:awnStatisticsLsWanTsCard,_v:awnStatisticsLsWanTsPort,_w:awnStatisticsLsWanTsTs,'awnStatisticsLsWanTsData':awnStatisticsLsWanTsData,'awnStatisticsComNniPortRt':awnStatisticsComNniPortRt,'awnStatisticsComNniPortRtTable':awnStatisticsComNniPortRtTable,'awnStatisticsComNniPortRtEntry':awnStatisticsComNniPortRtEntry,_x:awnStatisticsComNniPortRtSlot,_y:awnStatisticsComNniPortRtAdapter,_z:awnStatisticsComNniPortRtPort,_A0:awnStatisticsComNniPortRtCategory,_A1:awnStatisticsComNniPortRtType,'awnStatisticsComNniPortRtData':awnStatisticsComNniPortRtData,'awnStatisticsComNniVpRt':awnStatisticsComNniVpRt,'awnStatisticsComNniVpRtTable':awnStatisticsComNniVpRtTable,'awnStatisticsComNniVpRtEntry':awnStatisticsComNniVpRtEntry,_A2:awnStatisticsComNniVpRtSlot,_A3:awnStatisticsComNniVpRtAdapter,_A4:awnStatisticsComNniVpRtPort,_A5:awnStatisticsComNniVpRtVpi,_A6:awnStatisticsComNniVpRtCategory,_A7:awnStatisticsComNniVpRtType,'awnStatisticsComNniVpRtData':awnStatisticsComNniVpRtData,'awnStatisticsLsWanTsRt':awnStatisticsLsWanTsRt,'awnStatisticsLsWanTsRtTable':awnStatisticsLsWanTsRtTable,'awnStatisticsLsWanTsRtEntry':awnStatisticsLsWanTsRtEntry,_A8:awnStatisticsLsWanTsRtUnit,_A9:awnStatisticsLsWanTsRtCard,_AA:awnStatisticsLsWanTsRtPort,_AB:awnStatisticsLsWanTsRtTs,_AC:awnStatisticsLsWanTsRtCategory,_AD:awnStatisticsLsWanTsRtType,'awnStatisticsLsWanTsRtData':awnStatisticsLsWanTsRtData,'awnStatisticsVccAtmLine':awnStatisticsVccAtmLine,'awnStatisticsVccAtmLineTable':awnStatisticsVccAtmLineTable,'awnStatisticsVccAtmLineEntry':awnStatisticsVccAtmLineEntry,_AE:awnStatisticsVccAtmLineSlot,_AF:awnStatisticsVccAtmLineAdapter,_AG:awnStatisticsVccAtmLinePort,_AH:awnStatisticsVccAtmLineVpi,_AI:awnStatisticsVccAtmLineVci,_AJ:awnStatisticsVccAtmLineType,'awnStatisticsVccAtmLineData':awnStatisticsVccAtmLineData,'awnStatisticsVpcAtmLine':awnStatisticsVpcAtmLine,'awnStatisticsVpcAtmLineTable':awnStatisticsVpcAtmLineTable,'awnStatisticsVpcAtmLineEntry':awnStatisticsVpcAtmLineEntry,_AK:awnStatisticsVpcAtmLineSlot,_AL:awnStatisticsVpcAtmLineAdapter,_AM:awnStatisticsVpcAtmLinePort,_AN:awnStatisticsVpcAtmLineVpi,_AO:awnStatisticsVpcAtmLineType,'awnStatisticsVpcAtmLineData':awnStatisticsVpcAtmLineData,'awnStatisticsVccWanTs':awnStatisticsVccWanTs,'awnStatisticsVccWanTsTable':awnStatisticsVccWanTsTable,'awnStatisticsVccWanTsEntry':awnStatisticsVccWanTsEntry,_AP:awnStatisticsVccWanTsUnit,_AQ:awnStatisticsVccWanTsCard,_AR:awnStatisticsVccWanTsPort,_AS:awnStatisticsVccWanTsTs,_AT:awnStatisticsVccWanTsVpi,_AU:awnStatisticsVccWanTsVci,_AV:awnStatisticsVccWanTsType,'awnStatisticsVccWanTsData':awnStatisticsVccWanTsData,'awnStatisticsVccFrLine':awnStatisticsVccFrLine,'awnStatisticsVccFrLineTable':awnStatisticsVccFrLineTable,'awnStatisticsVccFrLineEntry':awnStatisticsVccFrLineEntry,_AW:awnStatisticsVccFrLineUnit,_AX:awnStatisticsVccFrLineCard,_AY:awnStatisticsVccFrLinePort,_AZ:awnStatisticsVccFrLineTimeslot,_Aa:awnStatisticsVccFrLineDlci,_Ab:awnStatisticsVccFrLineType,'awnStatisticsVccFrLineData':awnStatisticsVccFrLineData,'awnStatisticsVccFfLine':awnStatisticsVccFfLine,'awnStatisticsVccFfLineTable':awnStatisticsVccFfLineTable,'awnStatisticsVccFfLineEntry':awnStatisticsVccFfLineEntry,_Ac:awnStatisticsVccFfLineUnit,_Ad:awnStatisticsVccFfLineCard,_Ae:awnStatisticsVccFfLinePort,_Af:awnStatisticsVccFfLineTimeslot,_Ag:awnStatisticsVccFfLineType,'awnStatisticsVccFfLineData':awnStatisticsVccFfLineData,'awnStatisticsLsWanVp':awnStatisticsLsWanVp,'awnStatisticsLsWanVpTable':awnStatisticsLsWanVpTable,'awnStatisticsLsWanVpEntry':awnStatisticsLsWanVpEntry,_Ah:awnStatisticsLsWanVpUnit,_Ai:awnStatisticsLsWanVpCard,_Aj:awnStatisticsLsWanVpPort,_Ak:awnStatisticsLsWanVpVpi,'awnStatisticsLsWanVpData':awnStatisticsLsWanVpData,'awnStatisticsLsWanVpRt':awnStatisticsLsWanVpRt,'awnStatisticsLsWanVpRtTable':awnStatisticsLsWanVpRtTable,'awnStatisticsLsWanVpRtEntry':awnStatisticsLsWanVpRtEntry,_Al:awnStatisticsLsWanVpRtUnit,_Am:awnStatisticsLsWanVpRtCard,_An:awnStatisticsLsWanVpRtPort,_Ao:awnStatisticsLsWanVpRtVpi,_Ap:awnStatisticsLsWanVpRtCategory,_Aq:awnStatisticsLsWanVpRtType,'awnStatisticsLsWanVpRtData':awnStatisticsLsWanVpRtData,'awnStatisticsComAtmLine':awnStatisticsComAtmLine,'awnStatisticsComAtmLineTable':awnStatisticsComAtmLineTable,'awnStatisticsComAtmLineEntry':awnStatisticsComAtmLineEntry,_Ar:awnStatisticsComAtmLineSlot,_As:awnStatisticsComAtmLineAdapter,_At:awnStatisticsComAtmLinePort,_Au:awnStatisticsComAtmLineVpi,'awnStatisticsComAtmLineData':awnStatisticsComAtmLineData,'awnStatisticsLsTs':awnStatisticsLsTs,'awnStatisticsLsTsTable':awnStatisticsLsTsTable,'awnStatisticsLsTsEntry':awnStatisticsLsTsEntry,_Av:awnStatisticsLsTsUnit,_Aw:awnStatisticsLsTsCard,_Ax:awnStatisticsLsTsPort,_Ay:awnStatisticsLsTsTs,'awnStatisticsLsTsData':awnStatisticsLsTsData,'awnStatisticsSys':awnStatisticsSys,'awnStatisticsSysDroppedCells':awnStatisticsSysDroppedCells,'awnStatisticsIpFrame':awnStatisticsIpFrame,'awnStatisticsIpFrameTable':awnStatisticsIpFrameTable,'awnStatisticsIpFrameEntry':awnStatisticsIpFrameEntry,_Az:awnStatisticsIpFrameAddr,'awnStatisticsIpFrameData':awnStatisticsIpFrameData,'awnStatisticsDlci':awnStatisticsDlci,'awnStatisticsDlciTable':awnStatisticsDlciTable,'awnStatisticsDlciEntry':awnStatisticsDlciEntry,_A_:awnStatisticsDlciUnit,_B0:awnStatisticsDlciCard,_B1:awnStatisticsDlciPort,_B2:awnStatisticsDlciTimeslot,_B3:awnStatisticsDlciDlci,'awnStatisticsDlciBriClad':awnStatisticsDlciBriClad,'awnIlmi':awnIlmi,'awnIlmiIns':awnIlmiIns,'awnIlmiInsRouteadd':awnIlmiInsRouteadd,'awnIlmiInsRoutedel':awnIlmiInsRoutedel})