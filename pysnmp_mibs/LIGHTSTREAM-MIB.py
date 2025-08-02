_Ba='lightStreamVliPortWorkGroupID'
_BZ='lightStreamVliPortWorkGroupPort'
_BY='lightStreamVliPortCtlPort'
_BX='lightStreamBrFilterParmFilterId'
_BW='lightStreamBrFilterParmPort'
_BV='lightStreamBrFilterTokenIndex'
_BU='lightStreamBrFilterId'
_BT='LightStreamFilterAction'
_BS='lightStreamBrPortPort'
_BR='lwmaIndex'
_BQ='ndClientID'
_BP='ndSwudStatsIndex'
_BO='ndSwudIndex'
_BN='comingdown'
_BM='gidEventDistributionGroup'
_BL='gidInternalIpAddress'
_BK='gidPortID'
_BJ='gidPortChassis'
_BI='gidLineCardSlot'
_BH='gidLineCardChassis'
_BG='gidClientID'
_BF='gidNbrEIA'
_BE='dcPowerTray'
_BD='cellVciStatVciIndex'
_BC='cellVciStatPortIndex'
_BB='lsNpCpuWorkloadIndex'
_BA='lsLcIntervalNumber'
_B9='lsLcIntervalPortIndex'
_B8='tsuDropEventWatermarkIndex'
_B7='tsuDropEventPortIndex'
_B6='lsFsuFastDropWatermarkIndex'
_B5='fsuDropEventWatermarkIndex'
_B4='fsuDropEventPortIndex'
_B3='fsuQueueCellLenSubQIndex'
_B2='fsuQueueCellLenPortIndex'
_B1='fsuXmtCellsPriorityIndex'
_B0='fsuXmtCellsPortIndex'
_A_='lcStatPortIndex'
_Az='lcStatCardIndex'
_Ay='lsTrunkWorkloadTypeIndex'
_Ax='lsTrunkWorkloadCardIndex'
_Aw='trunkPortStatIndex'
_Av='frameForwardStatPortIndex'
_Au='lsEdgeWorkloadTypeIndex'
_At='lsEdgeWorkloadCardIndex'
_As='edgeToPortMsgLenBinIndex'
_Ar='edgeToPortMsgLenPortIndex'
_Aq='edgeToSwMsgLenBinIndex'
_Ap='edgeToSwMsgLenPortIndex'
_Ao='frameRelayDlciStatDlciIndex'
_An='frameRelayDlciStatPortIndex'
_Am='edgePortStatIndex'
_Al='edgeStatIndex'
_Ak='mcEndptLclInstance'
_Aj='mcEndptLclCktid'
_Ai='mcEndptLclIfIndex'
_Ah='pvcSrcPvcId'
_Ag='pvcSrcIfIndex'
_Af='sUniCktInfoVCI'
_Ae='sUniCktInfoIfIndex'
_Ad='sUniCktSrcVCI'
_Ac='sUniCktSrcIfIndex'
_Ab='ffCktInfoIfIndex'
_Aa='ffCktSrcIfIndex'
_AZ='frCktInfoDlci'
_AY='frCktInfoIfIndex'
_AX='frCktSrcDlci'
_AW='frCktSrcIfIndex'
_AV='frProvMiIfIndex'
_AU='edgeIfIndex'
_AT='collectDBInstance'
_AS='collectDBIndex'
_AR='collectIndex'
_AQ='mmaNumNameNumber'
_AP='externalClock'
_AO='internalClock'
_AN='scrambleDisable'
_AM='scrambleEnable'
_AL='clc1InfoIfIndex'
_AK='npInfoIfIndex'
_AJ='t3ScrambleDisable'
_AI='t3ScrambleEnable'
_AH='e3CableLength4'
_AG='e3CableLength3'
_AF='e3CableLength2'
_AE='e3CableLength1'
_AD='t3CableLength2'
_AC='t3CableLength1'
_AB='ms1InfoIfIndex'
_AA='frameForwarding'
_A9='frameRelay'
_A8='dceTTloop'
_A7='ls1InfoIfIndex'
_A6='clc18t1e1cbrac1'
_A5='clc12taxiac1Trunk'
_A4='clc12taxiac1Edge'
_A3='clc18t3ac1Trunk'
_A2='clc18t3ac1Edge'
_A1='clc12oc3ac1Trunk'
_A0='clc12oc3ac1Edge'
_z='plc18sac1Trunk'
_y='plc18sac1Edge'
_x='plc1Lstoken'
_w='plc18eac1'
_v='plc12fac1'
_u='msEdge'
_t='msTrunk'
_s='lsTrunk'
_r='lsEdge'
_q='switch'
_p='portInfoIndex'
_o='cardIndex'
_n='NotificationType'
_m='ifIndex'
_l='IF-MIB'
_k='existent'
_j='createRequest'
_i='testing'
_h='off'
_g='debug'
_f='trace'
_e='informational'
_d='operational'
_c='invalid'
_b='valid'
_a='underCreation'
_Z='atmUni'
_Y='other'
_X='trigger'
_W='external'
_V='internal'
_U='delete'
_T='none'
_S='down'
_R='OctetString'
_Q='insured'
_P='guaranteed'
_O='trunk'
_N='empty'
_M='up'
_L='disabled'
_K='enabled'
_J='not-accessible'
_I='active'
_H='inactive'
_G='DisplayString'
_F='unknown'
_E='LIGHTSTREAM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_l,_m)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_n,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_n,'TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class LightStreamStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
class LightStreamValidation(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
class LightStreamFilterAction(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('block',2)))
class LightStreamUpToMaxAge(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
class LightStreamDLCI(Integer32):0
class VCI(Integer32):0
_LightStream_ObjectIdentity=ObjectIdentity
lightStream=_LightStream_ObjectIdentity((1,3,6,1,4,1,711))
_LightStreamOIDs_ObjectIdentity=ObjectIdentity
lightStreamOIDs=_LightStreamOIDs_ObjectIdentity((1,3,6,1,4,1,711,1))
_LightStreamATM_ObjectIdentity=ObjectIdentity
lightStreamATM=_LightStreamATM_ObjectIdentity((1,3,6,1,4,1,711,1,1))
_LsOther_ObjectIdentity=ObjectIdentity
lsOther=_LsOther_ObjectIdentity((1,3,6,1,4,1,711,1,2))
_LsTrapNumber_ObjectIdentity=ObjectIdentity
lsTrapNumber=_LsTrapNumber_ObjectIdentity((1,3,6,1,4,1,711,1,2,1))
_LsTrapText_ObjectIdentity=ObjectIdentity
lsTrapText=_LsTrapText_ObjectIdentity((1,3,6,1,4,1,711,1,2,2))
_LsTrapName_ObjectIdentity=ObjectIdentity
lsTrapName=_LsTrapName_ObjectIdentity((1,3,6,1,4,1,711,1,2,3))
_LsConfig_ObjectIdentity=ObjectIdentity
lsConfig=_LsConfig_ObjectIdentity((1,3,6,1,4,1,711,1,3))
_LightStreamProducts_ObjectIdentity=ObjectIdentity
lightStreamProducts=_LightStreamProducts_ObjectIdentity((1,3,6,1,4,1,711,2))
_AtmSwitch_ObjectIdentity=ObjectIdentity
atmSwitch=_AtmSwitch_ObjectIdentity((1,3,6,1,4,1,711,2,1))
_ChassisInfo_ObjectIdentity=ObjectIdentity
chassisInfo=_ChassisInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,1))
_ChassisId_Type=Integer32
_ChassisId_Object=MibScalar
chassisId=_ChassisId_Object((1,3,6,1,4,1,711,2,1,1,2),_ChassisId_Type())
chassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisId.setStatus(_A)
_ChassisActiveIpAddr_Type=IpAddress
_ChassisActiveIpAddr_Object=MibScalar
chassisActiveIpAddr=_ChassisActiveIpAddr_Object((1,3,6,1,4,1,711,2,1,1,3),_ChassisActiveIpAddr_Type())
chassisActiveIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisActiveIpAddr.setStatus(_A)
_ChassisSecondaryIpAddr_Type=IpAddress
_ChassisSecondaryIpAddr_Object=MibScalar
chassisSecondaryIpAddr=_ChassisSecondaryIpAddr_Object((1,3,6,1,4,1,711,2,1,1,4),_ChassisSecondaryIpAddr_Type())
chassisSecondaryIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisSecondaryIpAddr.setStatus(_A)
_ChassisNetworkMask_Type=IpAddress
_ChassisNetworkMask_Object=MibScalar
chassisNetworkMask=_ChassisNetworkMask_Object((1,3,6,1,4,1,711,2,1,1,5),_ChassisNetworkMask_Type())
chassisNetworkMask.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisNetworkMask.setStatus(_A)
_ChassisEthernetIpAddr_Type=IpAddress
_ChassisEthernetIpAddr_Object=MibScalar
chassisEthernetIpAddr=_ChassisEthernetIpAddr_Object((1,3,6,1,4,1,711,2,1,1,6),_ChassisEthernetIpAddr_Type())
chassisEthernetIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisEthernetIpAddr.setStatus(_A)
_ChassisEthernetIpMask_Type=IpAddress
_ChassisEthernetIpMask_Object=MibScalar
chassisEthernetIpMask=_ChassisEthernetIpMask_Object((1,3,6,1,4,1,711,2,1,1,7),_ChassisEthernetIpMask_Type())
chassisEthernetIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisEthernetIpMask.setStatus(_A)
_ChassisDefaultIpRouter_Type=IpAddress
_ChassisDefaultIpRouter_Object=MibScalar
chassisDefaultIpRouter=_ChassisDefaultIpRouter_Object((1,3,6,1,4,1,711,2,1,1,8),_ChassisDefaultIpRouter_Type())
chassisDefaultIpRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisDefaultIpRouter.setStatus(_A)
_ChassisStatusWord_Type=Integer32
_ChassisStatusWord_Object=MibScalar
chassisStatusWord=_ChassisStatusWord_Object((1,3,6,1,4,1,711,2,1,1,9),_ChassisStatusWord_Type())
chassisStatusWord.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisStatusWord.setStatus(_A)
class _ChassisConsoleTrapLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3),(_g,4),(_h,5)))
_ChassisConsoleTrapLevel_Type.__name__=_C
_ChassisConsoleTrapLevel_Object=MibScalar
chassisConsoleTrapLevel=_ChassisConsoleTrapLevel_Object((1,3,6,1,4,1,711,2,1,1,10),_ChassisConsoleTrapLevel_Type())
chassisConsoleTrapLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisConsoleTrapLevel.setStatus(_A)
_CardInfo_ObjectIdentity=ObjectIdentity
cardInfo=_CardInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,2))
_CardTable_Object=MibTable
cardTable=_CardTable_Object((1,3,6,1,4,1,711,2,1,2,1))
if mibBuilder.loadTexts:cardTable.setStatus(_A)
_CardEntry_Object=MibTableRow
cardEntry=_CardEntry_Object((1,3,6,1,4,1,711,2,1,2,1,1))
cardEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:cardEntry.setStatus(_A)
_CardIndex_Type=Integer32
_CardIndex_Object=MibTableColumn
cardIndex=_CardIndex_Object((1,3,6,1,4,1,711,2,1,2,1,1,1),_CardIndex_Type())
cardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cardIndex.setStatus(_A)
class _CardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CardName_Type.__name__=_G
_CardName_Object=MibTableColumn
cardName=_CardName_Object((1,3,6,1,4,1,711,2,1,2,1,1,2),_CardName_Type())
cardName.setMaxAccess(_D)
if mibBuilder.loadTexts:cardName.setStatus(_A)
class _CardBoardType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CardBoardType_Type.__name__=_G
_CardBoardType_Object=MibTableColumn
cardBoardType=_CardBoardType_Object((1,3,6,1,4,1,711,2,1,2,1,1,3),_CardBoardType_Type())
cardBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:cardBoardType.setStatus(_A)
class _CardLcSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CardLcSoftwareVersion_Type.__name__=_G
_CardLcSoftwareVersion_Object=MibTableColumn
cardLcSoftwareVersion=_CardLcSoftwareVersion_Object((1,3,6,1,4,1,711,2,1,2,1,1,4),_CardLcSoftwareVersion_Type())
cardLcSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cardLcSoftwareVersion.setStatus(_A)
class _CardLccSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CardLccSoftwareVersion_Type.__name__=_G
_CardLccSoftwareVersion_Object=MibTableColumn
cardLccSoftwareVersion=_CardLccSoftwareVersion_Object((1,3,6,1,4,1,711,2,1,2,1,1,5),_CardLccSoftwareVersion_Type())
cardLccSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cardLccSoftwareVersion.setStatus(_A)
_CardPID_Type=Integer32
_CardPID_Object=MibTableColumn
cardPID=_CardPID_Object((1,3,6,1,4,1,711,2,1,2,1,1,6),_CardPID_Type())
cardPID.setMaxAccess(_B)
if mibBuilder.loadTexts:cardPID.setStatus(_A)
class _CardMaxVCs_Type(Integer32):defaultValue=800
_CardMaxVCs_Type.__name__=_C
_CardMaxVCs_Object=MibTableColumn
cardMaxVCs=_CardMaxVCs_Object((1,3,6,1,4,1,711,2,1,2,1,1,7),_CardMaxVCs_Type())
cardMaxVCs.setMaxAccess(_D)
if mibBuilder.loadTexts:cardMaxVCs.setStatus(_A)
class _CardOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_S,2),(_i,3),(_N,4)))
_CardOperStatus_Type.__name__=_C
_CardOperStatus_Object=MibTableColumn
cardOperStatus=_CardOperStatus_Object((1,3,6,1,4,1,711,2,1,2,1,1,8),_CardOperStatus_Type())
cardOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cardOperStatus.setStatus(_A)
class _CardAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_S,2),(_i,3)))
_CardAdminStatus_Type.__name__=_C
_CardAdminStatus_Object=MibTableColumn
cardAdminStatus=_CardAdminStatus_Object((1,3,6,1,4,1,711,2,1,2,1,1,9),_CardAdminStatus_Type())
cardAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cardAdminStatus.setStatus(_A)
_CardStatusWord_Type=Integer32
_CardStatusWord_Object=MibTableColumn
cardStatusWord=_CardStatusWord_Object((1,3,6,1,4,1,711,2,1,2,1,1,10),_CardStatusWord_Type())
cardStatusWord.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusWord.setStatus(_A)
class _CardConfigRegister_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_S,2),(_i,3),(_N,4)))
_CardConfigRegister_Type.__name__=_C
_CardConfigRegister_Object=MibTableColumn
cardConfigRegister=_CardConfigRegister_Object((1,3,6,1,4,1,711,2,1,2,1,1,11),_CardConfigRegister_Type())
cardConfigRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:cardConfigRegister.setStatus(_A)
_PortInfo_ObjectIdentity=ObjectIdentity
portInfo=_PortInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,3))
_PortInfoTable_Object=MibTable
portInfoTable=_PortInfoTable_Object((1,3,6,1,4,1,711,2,1,3,1))
if mibBuilder.loadTexts:portInfoTable.setStatus(_A)
_PortInfoEntry_Object=MibTableRow
portInfoEntry=_PortInfoEntry_Object((1,3,6,1,4,1,711,2,1,3,1,1))
portInfoEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:portInfoEntry.setStatus(_A)
_PortInfoIndex_Type=Integer32
_PortInfoIndex_Object=MibTableColumn
portInfoIndex=_PortInfoIndex_Object((1,3,6,1,4,1,711,2,1,3,1,1,1),_PortInfoIndex_Type())
portInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoIndex.setStatus(_A)
class _PortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10,11,12,13,14,15,30,31,32,33,34,35,36,37)));namedValues=NamedValues(*((_N,1),('error',2),(_F,3),(_q,4),('np',5),(_r,6),(_s,7),(_t,8),(_u,10),(_v,11),(_w,12),(_x,13),(_y,14),(_z,15),('clc1Gen',30),(_A0,31),(_A1,32),(_A2,33),(_A3,34),(_A4,35),(_A5,36),(_A6,37)))
_PortInfoType_Type.__name__=_C
_PortInfoType_Object=MibTableColumn
portInfoType=_PortInfoType_Object((1,3,6,1,4,1,711,2,1,3,1,1,2),_PortInfoType_Type())
portInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoType.setStatus(_A)
_PortInfoSpecific_Type=ObjectIdentifier
_PortInfoSpecific_Object=MibTableColumn
portInfoSpecific=_PortInfoSpecific_Object((1,3,6,1,4,1,711,2,1,3,1,1,3),_PortInfoSpecific_Type())
portInfoSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoSpecific.setStatus(_A)
_PortInfoName_Type=DisplayString
_PortInfoName_Object=MibTableColumn
portInfoName=_PortInfoName_Object((1,3,6,1,4,1,711,2,1,3,1,1,4),_PortInfoName_Type())
portInfoName.setMaxAccess(_D)
if mibBuilder.loadTexts:portInfoName.setStatus(_A)
_PortInfoErrorLimit_Type=Integer32
_PortInfoErrorLimit_Object=MibTableColumn
portInfoErrorLimit=_PortInfoErrorLimit_Object((1,3,6,1,4,1,711,2,1,3,1,1,5),_PortInfoErrorLimit_Type())
portInfoErrorLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:portInfoErrorLimit.setStatus(_A)
_PortTransmission_ObjectIdentity=ObjectIdentity
portTransmission=_PortTransmission_ObjectIdentity((1,3,6,1,4,1,711,2,1,4))
_Ls1InfoTable_Object=MibTable
ls1InfoTable=_Ls1InfoTable_Object((1,3,6,1,4,1,711,2,1,4,1))
if mibBuilder.loadTexts:ls1InfoTable.setStatus(_A)
_Ls1InfoEntry_Object=MibTableRow
ls1InfoEntry=_Ls1InfoEntry_Object((1,3,6,1,4,1,711,2,1,4,1,1))
ls1InfoEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:ls1InfoEntry.setStatus(_A)
_Ls1InfoIfIndex_Type=Integer32
_Ls1InfoIfIndex_Object=MibTableColumn
ls1InfoIfIndex=_Ls1InfoIfIndex_Object((1,3,6,1,4,1,711,2,1,4,1,1,1),_Ls1InfoIfIndex_Type())
ls1InfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoIfIndex.setStatus(_A)
class _Ls1InfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,99)));namedValues=NamedValues(*(('v35',1),('rs422',2),('rs530',3),('t1',4),(_F,99)))
_Ls1InfoType_Type.__name__=_C
_Ls1InfoType_Object=MibTableColumn
ls1InfoType=_Ls1InfoType_Object((1,3,6,1,4,1,711,2,1,4,1,1,2),_Ls1InfoType_Type())
ls1InfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoType.setStatus(_A)
class _Ls1InfoOperCsuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('larse',2)))
_Ls1InfoOperCsuType_Type.__name__=_C
_Ls1InfoOperCsuType_Object=MibTableColumn
ls1InfoOperCsuType=_Ls1InfoOperCsuType_Object((1,3,6,1,4,1,711,2,1,4,1,1,3),_Ls1InfoOperCsuType_Type())
ls1InfoOperCsuType.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperCsuType.setStatus(_A)
class _Ls1InfoAdminCsuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('larse',2)))
_Ls1InfoAdminCsuType_Type.__name__=_C
_Ls1InfoAdminCsuType_Object=MibTableColumn
ls1InfoAdminCsuType=_Ls1InfoAdminCsuType_Object((1,3,6,1,4,1,711,2,1,4,1,1,4),_Ls1InfoAdminCsuType_Type())
ls1InfoAdminCsuType.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminCsuType.setStatus(_A)
_Ls1InfoOperRcvBaudRate_Type=Integer32
_Ls1InfoOperRcvBaudRate_Object=MibTableColumn
ls1InfoOperRcvBaudRate=_Ls1InfoOperRcvBaudRate_Object((1,3,6,1,4,1,711,2,1,4,1,1,5),_Ls1InfoOperRcvBaudRate_Type())
ls1InfoOperRcvBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperRcvBaudRate.setStatus(_A)
_Ls1InfoAdminRcvBaudRate_Type=Integer32
_Ls1InfoAdminRcvBaudRate_Object=MibTableColumn
ls1InfoAdminRcvBaudRate=_Ls1InfoAdminRcvBaudRate_Object((1,3,6,1,4,1,711,2,1,4,1,1,6),_Ls1InfoAdminRcvBaudRate_Type())
ls1InfoAdminRcvBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminRcvBaudRate.setStatus(_A)
_Ls1InfoOperXmitBaudRate_Type=Integer32
_Ls1InfoOperXmitBaudRate_Object=MibTableColumn
ls1InfoOperXmitBaudRate=_Ls1InfoOperXmitBaudRate_Object((1,3,6,1,4,1,711,2,1,4,1,1,7),_Ls1InfoOperXmitBaudRate_Type())
ls1InfoOperXmitBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperXmitBaudRate.setStatus(_A)
_Ls1InfoAdminXmitBaudRate_Type=Integer32
_Ls1InfoAdminXmitBaudRate_Object=MibTableColumn
ls1InfoAdminXmitBaudRate=_Ls1InfoAdminXmitBaudRate_Object((1,3,6,1,4,1,711,2,1,4,1,1,8),_Ls1InfoAdminXmitBaudRate_Type())
ls1InfoAdminXmitBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminXmitBaudRate.setStatus(_A)
class _Ls1InfoOperNetIntType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dce',1),('dte',2),(_A8,3)))
_Ls1InfoOperNetIntType_Type.__name__=_C
_Ls1InfoOperNetIntType_Object=MibTableColumn
ls1InfoOperNetIntType=_Ls1InfoOperNetIntType_Object((1,3,6,1,4,1,711,2,1,4,1,1,9),_Ls1InfoOperNetIntType_Type())
ls1InfoOperNetIntType.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperNetIntType.setStatus(_A)
class _Ls1InfoAdminNetIntType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dce',1),('dte',2),(_A8,3)))
_Ls1InfoAdminNetIntType_Type.__name__=_C
_Ls1InfoAdminNetIntType_Object=MibTableColumn
ls1InfoAdminNetIntType=_Ls1InfoAdminNetIntType_Object((1,3,6,1,4,1,711,2,1,4,1,1,10),_Ls1InfoAdminNetIntType_Type())
ls1InfoAdminNetIntType.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminNetIntType.setStatus(_A)
_Ls1InfoOperModemState_Type=Integer32
_Ls1InfoOperModemState_Object=MibTableColumn
ls1InfoOperModemState=_Ls1InfoOperModemState_Object((1,3,6,1,4,1,711,2,1,4,1,1,13),_Ls1InfoOperModemState_Type())
ls1InfoOperModemState.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperModemState.setStatus(_A)
class _Ls1InfoOperProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_A9,2),(_AA,3),('ppp',4),(_F,5)))
_Ls1InfoOperProtocol_Type.__name__=_C
_Ls1InfoOperProtocol_Object=MibTableColumn
ls1InfoOperProtocol=_Ls1InfoOperProtocol_Object((1,3,6,1,4,1,711,2,1,4,1,1,15),_Ls1InfoOperProtocol_Type())
ls1InfoOperProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperProtocol.setStatus(_A)
class _Ls1InfoAdminProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_A9,2),(_AA,3),('ppp',4),(_F,5)))
_Ls1InfoAdminProtocol_Type.__name__=_C
_Ls1InfoAdminProtocol_Object=MibTableColumn
ls1InfoAdminProtocol=_Ls1InfoAdminProtocol_Object((1,3,6,1,4,1,711,2,1,4,1,1,16),_Ls1InfoAdminProtocol_Type())
ls1InfoAdminProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminProtocol.setStatus(_A)
_Ls1InfoOperControlBandwidthSize_Type=Integer32
_Ls1InfoOperControlBandwidthSize_Object=MibTableColumn
ls1InfoOperControlBandwidthSize=_Ls1InfoOperControlBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,1,1,21),_Ls1InfoOperControlBandwidthSize_Type())
ls1InfoOperControlBandwidthSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperControlBandwidthSize.setStatus(_A)
_Ls1InfoAdminControlBandwidthSize_Type=Integer32
_Ls1InfoAdminControlBandwidthSize_Object=MibTableColumn
ls1InfoAdminControlBandwidthSize=_Ls1InfoAdminControlBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,1,1,22),_Ls1InfoAdminControlBandwidthSize_Type())
ls1InfoAdminControlBandwidthSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminControlBandwidthSize.setStatus(_A)
_Ls1InfoOperDataBandwidthSize_Type=Integer32
_Ls1InfoOperDataBandwidthSize_Object=MibTableColumn
ls1InfoOperDataBandwidthSize=_Ls1InfoOperDataBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,1,1,23),_Ls1InfoOperDataBandwidthSize_Type())
ls1InfoOperDataBandwidthSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperDataBandwidthSize.setStatus(_A)
_Ls1InfoAdminDataBandwidthSize_Type=Integer32
_Ls1InfoAdminDataBandwidthSize_Object=MibTableColumn
ls1InfoAdminDataBandwidthSize=_Ls1InfoAdminDataBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,1,1,24),_Ls1InfoAdminDataBandwidthSize_Type())
ls1InfoAdminDataBandwidthSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminDataBandwidthSize.setStatus(_A)
class _Ls1InfoOperLoopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),(_V,2),(_W,3),('remote',4)))
_Ls1InfoOperLoopMode_Type.__name__=_C
_Ls1InfoOperLoopMode_Object=MibTableColumn
ls1InfoOperLoopMode=_Ls1InfoOperLoopMode_Object((1,3,6,1,4,1,711,2,1,4,1,1,25),_Ls1InfoOperLoopMode_Type())
ls1InfoOperLoopMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoOperLoopMode.setStatus(_A)
class _Ls1InfoAdminLoopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),(_V,2),(_W,3),('remote',4)))
_Ls1InfoAdminLoopMode_Type.__name__=_C
_Ls1InfoAdminLoopMode_Object=MibTableColumn
ls1InfoAdminLoopMode=_Ls1InfoAdminLoopMode_Object((1,3,6,1,4,1,711,2,1,4,1,1,26),_Ls1InfoAdminLoopMode_Type())
ls1InfoAdminLoopMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminLoopMode.setStatus(_A)
class _Ls1InfoLcAutoEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Ls1InfoLcAutoEnable_Type.__name__=_C
_Ls1InfoLcAutoEnable_Object=MibTableColumn
ls1InfoLcAutoEnable=_Ls1InfoLcAutoEnable_Object((1,3,6,1,4,1,711,2,1,4,1,1,27),_Ls1InfoLcAutoEnable_Type())
ls1InfoLcAutoEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoLcAutoEnable.setStatus(_A)
_Ls1InfoLcDebugLevel_Type=Integer32
_Ls1InfoLcDebugLevel_Object=MibTableColumn
ls1InfoLcDebugLevel=_Ls1InfoLcDebugLevel_Object((1,3,6,1,4,1,711,2,1,4,1,1,28),_Ls1InfoLcDebugLevel_Type())
ls1InfoLcDebugLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoLcDebugLevel.setStatus(_A)
_Ls1InfoDataCellCapacity_Type=Integer32
_Ls1InfoDataCellCapacity_Object=MibTableColumn
ls1InfoDataCellCapacity=_Ls1InfoDataCellCapacity_Object((1,3,6,1,4,1,711,2,1,4,1,1,29),_Ls1InfoDataCellCapacity_Type())
ls1InfoDataCellCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoDataCellCapacity.setStatus(_A)
_Ls1InfoDataCellAvailable_Type=Integer32
_Ls1InfoDataCellAvailable_Object=MibTableColumn
ls1InfoDataCellAvailable=_Ls1InfoDataCellAvailable_Object((1,3,6,1,4,1,711,2,1,4,1,1,30),_Ls1InfoDataCellAvailable_Type())
ls1InfoDataCellAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoDataCellAvailable.setStatus(_A)
_Ls1InfoMeasuredBaudRate_Type=Integer32
_Ls1InfoMeasuredBaudRate_Object=MibTableColumn
ls1InfoMeasuredBaudRate=_Ls1InfoMeasuredBaudRate_Object((1,3,6,1,4,1,711,2,1,4,1,1,31),_Ls1InfoMeasuredBaudRate_Type())
ls1InfoMeasuredBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoMeasuredBaudRate.setStatus(_A)
_Ls1InfoLinkUtilization_Type=Integer32
_Ls1InfoLinkUtilization_Object=MibTableColumn
ls1InfoLinkUtilization=_Ls1InfoLinkUtilization_Object((1,3,6,1,4,1,711,2,1,4,1,1,32),_Ls1InfoLinkUtilization_Type())
ls1InfoLinkUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:ls1InfoLinkUtilization.setStatus(_A)
class _Ls1InfoAdminOperTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,99)));namedValues=NamedValues(*((_X,1),(_Y,99)))
_Ls1InfoAdminOperTrigger_Type.__name__=_C
_Ls1InfoAdminOperTrigger_Object=MibTableColumn
ls1InfoAdminOperTrigger=_Ls1InfoAdminOperTrigger_Object((1,3,6,1,4,1,711,2,1,4,1,1,99),_Ls1InfoAdminOperTrigger_Type())
ls1InfoAdminOperTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ls1InfoAdminOperTrigger.setStatus(_A)
_Ms1InfoTable_Object=MibTable
ms1InfoTable=_Ms1InfoTable_Object((1,3,6,1,4,1,711,2,1,4,2))
if mibBuilder.loadTexts:ms1InfoTable.setStatus(_A)
_Ms1InfoEntry_Object=MibTableRow
ms1InfoEntry=_Ms1InfoEntry_Object((1,3,6,1,4,1,711,2,1,4,2,1))
ms1InfoEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:ms1InfoEntry.setStatus(_A)
_Ms1InfoIfIndex_Type=Integer32
_Ms1InfoIfIndex_Object=MibTableColumn
ms1InfoIfIndex=_Ms1InfoIfIndex_Object((1,3,6,1,4,1,711,2,1,4,2,1,1),_Ms1InfoIfIndex_Type())
ms1InfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoIfIndex.setStatus(_A)
class _Ms1InfoOperCableLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AC,1),(_AD,2),(_AE,3),(_AF,4),(_AG,5),(_AH,6)))
_Ms1InfoOperCableLength_Type.__name__=_C
_Ms1InfoOperCableLength_Object=MibTableColumn
ms1InfoOperCableLength=_Ms1InfoOperCableLength_Object((1,3,6,1,4,1,711,2,1,4,2,1,2),_Ms1InfoOperCableLength_Type())
ms1InfoOperCableLength.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoOperCableLength.setStatus(_A)
class _Ms1InfoAdminCableLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AC,1),(_AD,2),(_AE,3),(_AF,4),(_AG,5),(_AH,6)))
_Ms1InfoAdminCableLength_Type.__name__=_C
_Ms1InfoAdminCableLength_Object=MibTableColumn
ms1InfoAdminCableLength=_Ms1InfoAdminCableLength_Object((1,3,6,1,4,1,711,2,1,4,2,1,3),_Ms1InfoAdminCableLength_Type())
ms1InfoAdminCableLength.setMaxAccess(_D)
if mibBuilder.loadTexts:ms1InfoAdminCableLength.setStatus(_A)
class _Ms1InfoOperProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_Z,2),(_F,3)))
_Ms1InfoOperProtocol_Type.__name__=_C
_Ms1InfoOperProtocol_Object=MibTableColumn
ms1InfoOperProtocol=_Ms1InfoOperProtocol_Object((1,3,6,1,4,1,711,2,1,4,2,1,4),_Ms1InfoOperProtocol_Type())
ms1InfoOperProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoOperProtocol.setStatus(_A)
class _Ms1InfoAdminProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_Z,2),(_F,3)))
_Ms1InfoAdminProtocol_Type.__name__=_C
_Ms1InfoAdminProtocol_Object=MibTableColumn
ms1InfoAdminProtocol=_Ms1InfoAdminProtocol_Object((1,3,6,1,4,1,711,2,1,4,2,1,5),_Ms1InfoAdminProtocol_Type())
ms1InfoAdminProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ms1InfoAdminProtocol.setStatus(_A)
_Ms1InfoOperControlBandwidthSize_Type=Integer32
_Ms1InfoOperControlBandwidthSize_Object=MibTableColumn
ms1InfoOperControlBandwidthSize=_Ms1InfoOperControlBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,2,1,10),_Ms1InfoOperControlBandwidthSize_Type())
ms1InfoOperControlBandwidthSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoOperControlBandwidthSize.setStatus(_A)
_Ms1InfoAdminControlBandwidthSize_Type=Integer32
_Ms1InfoAdminControlBandwidthSize_Object=MibTableColumn
ms1InfoAdminControlBandwidthSize=_Ms1InfoAdminControlBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,2,1,11),_Ms1InfoAdminControlBandwidthSize_Type())
ms1InfoAdminControlBandwidthSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ms1InfoAdminControlBandwidthSize.setStatus(_A)
_Ms1InfoOperDataBandwidthSize_Type=Integer32
_Ms1InfoOperDataBandwidthSize_Object=MibTableColumn
ms1InfoOperDataBandwidthSize=_Ms1InfoOperDataBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,2,1,12),_Ms1InfoOperDataBandwidthSize_Type())
ms1InfoOperDataBandwidthSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoOperDataBandwidthSize.setStatus(_A)
_Ms1InfoAdminDataBandwidthSize_Type=Integer32
_Ms1InfoAdminDataBandwidthSize_Object=MibTableColumn
ms1InfoAdminDataBandwidthSize=_Ms1InfoAdminDataBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,2,1,13),_Ms1InfoAdminDataBandwidthSize_Type())
ms1InfoAdminDataBandwidthSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ms1InfoAdminDataBandwidthSize.setStatus(_A)
class _Ms1InfoLcAutoEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Ms1InfoLcAutoEnable_Type.__name__=_C
_Ms1InfoLcAutoEnable_Object=MibTableColumn
ms1InfoLcAutoEnable=_Ms1InfoLcAutoEnable_Object((1,3,6,1,4,1,711,2,1,4,2,1,14),_Ms1InfoLcAutoEnable_Type())
ms1InfoLcAutoEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoLcAutoEnable.setStatus(_A)
_Ms1InfoLcDebugLevel_Type=Integer32
_Ms1InfoLcDebugLevel_Object=MibTableColumn
ms1InfoLcDebugLevel=_Ms1InfoLcDebugLevel_Object((1,3,6,1,4,1,711,2,1,4,2,1,15),_Ms1InfoLcDebugLevel_Type())
ms1InfoLcDebugLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoLcDebugLevel.setStatus(_A)
class _Ms1InfoOperScramble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AI,1),(_AJ,2)))
_Ms1InfoOperScramble_Type.__name__=_C
_Ms1InfoOperScramble_Object=MibTableColumn
ms1InfoOperScramble=_Ms1InfoOperScramble_Object((1,3,6,1,4,1,711,2,1,4,2,1,16),_Ms1InfoOperScramble_Type())
ms1InfoOperScramble.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoOperScramble.setStatus(_A)
class _Ms1InfoAdminScramble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AI,1),(_AJ,2)))
_Ms1InfoAdminScramble_Type.__name__=_C
_Ms1InfoAdminScramble_Object=MibTableColumn
ms1InfoAdminScramble=_Ms1InfoAdminScramble_Object((1,3,6,1,4,1,711,2,1,4,2,1,17),_Ms1InfoAdminScramble_Type())
ms1InfoAdminScramble.setMaxAccess(_D)
if mibBuilder.loadTexts:ms1InfoAdminScramble.setStatus(_A)
_Ms1InfoDataCellCapacity_Type=Integer32
_Ms1InfoDataCellCapacity_Object=MibTableColumn
ms1InfoDataCellCapacity=_Ms1InfoDataCellCapacity_Object((1,3,6,1,4,1,711,2,1,4,2,1,18),_Ms1InfoDataCellCapacity_Type())
ms1InfoDataCellCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoDataCellCapacity.setStatus(_A)
_Ms1InfoDataCellAvailable_Type=Integer32
_Ms1InfoDataCellAvailable_Object=MibTableColumn
ms1InfoDataCellAvailable=_Ms1InfoDataCellAvailable_Object((1,3,6,1,4,1,711,2,1,4,2,1,19),_Ms1InfoDataCellAvailable_Type())
ms1InfoDataCellAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoDataCellAvailable.setStatus(_A)
_Ms1InfoLinkUtilization_Type=Integer32
_Ms1InfoLinkUtilization_Object=MibTableColumn
ms1InfoLinkUtilization=_Ms1InfoLinkUtilization_Object((1,3,6,1,4,1,711,2,1,4,2,1,20),_Ms1InfoLinkUtilization_Type())
ms1InfoLinkUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoLinkUtilization.setStatus(_A)
class _Ms1InfoOperFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('plcp',1),('t3-Hec',2),('g-804',3)))
_Ms1InfoOperFraming_Type.__name__=_C
_Ms1InfoOperFraming_Object=MibTableColumn
ms1InfoOperFraming=_Ms1InfoOperFraming_Object((1,3,6,1,4,1,711,2,1,4,2,1,21),_Ms1InfoOperFraming_Type())
ms1InfoOperFraming.setMaxAccess(_B)
if mibBuilder.loadTexts:ms1InfoOperFraming.setStatus(_A)
class _Ms1InfoAdminOperTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,99)));namedValues=NamedValues(*((_X,1),(_Y,99)))
_Ms1InfoAdminOperTrigger_Type.__name__=_C
_Ms1InfoAdminOperTrigger_Object=MibTableColumn
ms1InfoAdminOperTrigger=_Ms1InfoAdminOperTrigger_Object((1,3,6,1,4,1,711,2,1,4,2,1,99),_Ms1InfoAdminOperTrigger_Type())
ms1InfoAdminOperTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ms1InfoAdminOperTrigger.setStatus(_A)
_NpInfoTable_Object=MibTable
npInfoTable=_NpInfoTable_Object((1,3,6,1,4,1,711,2,1,4,3))
if mibBuilder.loadTexts:npInfoTable.setStatus(_A)
_NpInfoEntry_Object=MibTableRow
npInfoEntry=_NpInfoEntry_Object((1,3,6,1,4,1,711,2,1,4,3,1))
npInfoEntry.setIndexNames((0,_E,_AK))
if mibBuilder.loadTexts:npInfoEntry.setStatus(_A)
_NpInfoIfIndex_Type=Integer32
_NpInfoIfIndex_Object=MibTableColumn
npInfoIfIndex=_NpInfoIfIndex_Object((1,3,6,1,4,1,711,2,1,4,3,1,1),_NpInfoIfIndex_Type())
npInfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:npInfoIfIndex.setStatus(_A)
_NpInfoIPCommittedRate_Type=Integer32
_NpInfoIPCommittedRate_Object=MibTableColumn
npInfoIPCommittedRate=_NpInfoIPCommittedRate_Object((1,3,6,1,4,1,711,2,1,4,3,1,5),_NpInfoIPCommittedRate_Type())
npInfoIPCommittedRate.setMaxAccess(_D)
if mibBuilder.loadTexts:npInfoIPCommittedRate.setStatus(_A)
_NpInfoIPCommittedBurst_Type=Integer32
_NpInfoIPCommittedBurst_Object=MibTableColumn
npInfoIPCommittedBurst=_NpInfoIPCommittedBurst_Object((1,3,6,1,4,1,711,2,1,4,3,1,6),_NpInfoIPCommittedBurst_Type())
npInfoIPCommittedBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:npInfoIPCommittedBurst.setStatus(_A)
_NpInfoIPExcessRate_Type=Integer32
_NpInfoIPExcessRate_Object=MibTableColumn
npInfoIPExcessRate=_NpInfoIPExcessRate_Object((1,3,6,1,4,1,711,2,1,4,3,1,7),_NpInfoIPExcessRate_Type())
npInfoIPExcessRate.setMaxAccess(_D)
if mibBuilder.loadTexts:npInfoIPExcessRate.setStatus(_A)
_NpInfoIPExcessBurst_Type=Integer32
_NpInfoIPExcessBurst_Object=MibTableColumn
npInfoIPExcessBurst=_NpInfoIPExcessBurst_Object((1,3,6,1,4,1,711,2,1,4,3,1,8),_NpInfoIPExcessBurst_Type())
npInfoIPExcessBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:npInfoIPExcessBurst.setStatus(_A)
_NpInfoIPNCircuits_Type=Integer32
_NpInfoIPNCircuits_Object=MibTableColumn
npInfoIPNCircuits=_NpInfoIPNCircuits_Object((1,3,6,1,4,1,711,2,1,4,3,1,9),_NpInfoIPNCircuits_Type())
npInfoIPNCircuits.setMaxAccess(_D)
if mibBuilder.loadTexts:npInfoIPNCircuits.setStatus(_A)
class _NpInfoAdminOperTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,99)));namedValues=NamedValues(*((_X,1),(_Y,99)))
_NpInfoAdminOperTrigger_Type.__name__=_C
_NpInfoAdminOperTrigger_Object=MibTableColumn
npInfoAdminOperTrigger=_NpInfoAdminOperTrigger_Object((1,3,6,1,4,1,711,2,1,4,3,1,99),_NpInfoAdminOperTrigger_Type())
npInfoAdminOperTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:npInfoAdminOperTrigger.setStatus(_A)
_Clc1InfoTable_Object=MibTable
clc1InfoTable=_Clc1InfoTable_Object((1,3,6,1,4,1,711,2,1,4,4))
if mibBuilder.loadTexts:clc1InfoTable.setStatus(_A)
_Clc1InfoEntry_Object=MibTableRow
clc1InfoEntry=_Clc1InfoEntry_Object((1,3,6,1,4,1,711,2,1,4,4,1))
clc1InfoEntry.setIndexNames((0,_E,_AL))
if mibBuilder.loadTexts:clc1InfoEntry.setStatus(_A)
_Clc1InfoIfIndex_Type=Integer32
_Clc1InfoIfIndex_Object=MibTableColumn
clc1InfoIfIndex=_Clc1InfoIfIndex_Object((1,3,6,1,4,1,711,2,1,4,4,1,1),_Clc1InfoIfIndex_Type())
clc1InfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoIfIndex.setStatus(_A)
class _Clc1InfoOperProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_Z,2),(_F,3)))
_Clc1InfoOperProtocol_Type.__name__=_C
_Clc1InfoOperProtocol_Object=MibTableColumn
clc1InfoOperProtocol=_Clc1InfoOperProtocol_Object((1,3,6,1,4,1,711,2,1,4,4,1,4),_Clc1InfoOperProtocol_Type())
clc1InfoOperProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoOperProtocol.setStatus(_A)
class _Clc1InfoAdminProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_Z,2),(_F,3)))
_Clc1InfoAdminProtocol_Type.__name__=_C
_Clc1InfoAdminProtocol_Object=MibTableColumn
clc1InfoAdminProtocol=_Clc1InfoAdminProtocol_Object((1,3,6,1,4,1,711,2,1,4,4,1,5),_Clc1InfoAdminProtocol_Type())
clc1InfoAdminProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:clc1InfoAdminProtocol.setStatus(_A)
class _Clc1InfoOperLoopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_V,2),(_W,3)))
_Clc1InfoOperLoopMode_Type.__name__=_C
_Clc1InfoOperLoopMode_Object=MibTableColumn
clc1InfoOperLoopMode=_Clc1InfoOperLoopMode_Object((1,3,6,1,4,1,711,2,1,4,4,1,6),_Clc1InfoOperLoopMode_Type())
clc1InfoOperLoopMode.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoOperLoopMode.setStatus(_A)
class _Clc1InfoAdminLoopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_V,2),(_W,3)))
_Clc1InfoAdminLoopMode_Type.__name__=_C
_Clc1InfoAdminLoopMode_Object=MibTableColumn
clc1InfoAdminLoopMode=_Clc1InfoAdminLoopMode_Object((1,3,6,1,4,1,711,2,1,4,4,1,7),_Clc1InfoAdminLoopMode_Type())
clc1InfoAdminLoopMode.setMaxAccess(_D)
if mibBuilder.loadTexts:clc1InfoAdminLoopMode.setStatus(_A)
_Clc1InfoOperControlBandwidthSize_Type=Integer32
_Clc1InfoOperControlBandwidthSize_Object=MibTableColumn
clc1InfoOperControlBandwidthSize=_Clc1InfoOperControlBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,4,1,10),_Clc1InfoOperControlBandwidthSize_Type())
clc1InfoOperControlBandwidthSize.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoOperControlBandwidthSize.setStatus(_A)
_Clc1InfoAdminControlBandwidthSize_Type=Integer32
_Clc1InfoAdminControlBandwidthSize_Object=MibTableColumn
clc1InfoAdminControlBandwidthSize=_Clc1InfoAdminControlBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,4,1,11),_Clc1InfoAdminControlBandwidthSize_Type())
clc1InfoAdminControlBandwidthSize.setMaxAccess(_D)
if mibBuilder.loadTexts:clc1InfoAdminControlBandwidthSize.setStatus(_A)
_Clc1InfoOperDataBandwidthSize_Type=Integer32
_Clc1InfoOperDataBandwidthSize_Object=MibTableColumn
clc1InfoOperDataBandwidthSize=_Clc1InfoOperDataBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,4,1,12),_Clc1InfoOperDataBandwidthSize_Type())
clc1InfoOperDataBandwidthSize.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoOperDataBandwidthSize.setStatus(_A)
_Clc1InfoAdminDataBandwidthSize_Type=Integer32
_Clc1InfoAdminDataBandwidthSize_Object=MibTableColumn
clc1InfoAdminDataBandwidthSize=_Clc1InfoAdminDataBandwidthSize_Object((1,3,6,1,4,1,711,2,1,4,4,1,13),_Clc1InfoAdminDataBandwidthSize_Type())
clc1InfoAdminDataBandwidthSize.setMaxAccess(_D)
if mibBuilder.loadTexts:clc1InfoAdminDataBandwidthSize.setStatus(_A)
class _Clc1InfoLcAutoEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Clc1InfoLcAutoEnable_Type.__name__=_C
_Clc1InfoLcAutoEnable_Object=MibTableColumn
clc1InfoLcAutoEnable=_Clc1InfoLcAutoEnable_Object((1,3,6,1,4,1,711,2,1,4,4,1,14),_Clc1InfoLcAutoEnable_Type())
clc1InfoLcAutoEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoLcAutoEnable.setStatus(_A)
_Clc1InfoLcDebugLevel_Type=Integer32
_Clc1InfoLcDebugLevel_Object=MibTableColumn
clc1InfoLcDebugLevel=_Clc1InfoLcDebugLevel_Object((1,3,6,1,4,1,711,2,1,4,4,1,15),_Clc1InfoLcDebugLevel_Type())
clc1InfoLcDebugLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoLcDebugLevel.setStatus(_A)
class _Clc1InfoOperScramble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AM,1),(_AN,2)))
_Clc1InfoOperScramble_Type.__name__=_C
_Clc1InfoOperScramble_Object=MibTableColumn
clc1InfoOperScramble=_Clc1InfoOperScramble_Object((1,3,6,1,4,1,711,2,1,4,4,1,16),_Clc1InfoOperScramble_Type())
clc1InfoOperScramble.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoOperScramble.setStatus(_A)
class _Clc1InfoAdminScramble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AM,1),(_AN,2)))
_Clc1InfoAdminScramble_Type.__name__=_C
_Clc1InfoAdminScramble_Object=MibTableColumn
clc1InfoAdminScramble=_Clc1InfoAdminScramble_Object((1,3,6,1,4,1,711,2,1,4,4,1,17),_Clc1InfoAdminScramble_Type())
clc1InfoAdminScramble.setMaxAccess(_D)
if mibBuilder.loadTexts:clc1InfoAdminScramble.setStatus(_A)
_Clc1InfoDataCellCapacity_Type=Integer32
_Clc1InfoDataCellCapacity_Object=MibTableColumn
clc1InfoDataCellCapacity=_Clc1InfoDataCellCapacity_Object((1,3,6,1,4,1,711,2,1,4,4,1,18),_Clc1InfoDataCellCapacity_Type())
clc1InfoDataCellCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoDataCellCapacity.setStatus(_A)
_Clc1InfoDataCellAvailable_Type=Integer32
_Clc1InfoDataCellAvailable_Object=MibTableColumn
clc1InfoDataCellAvailable=_Clc1InfoDataCellAvailable_Object((1,3,6,1,4,1,711,2,1,4,4,1,19),_Clc1InfoDataCellAvailable_Type())
clc1InfoDataCellAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoDataCellAvailable.setStatus(_A)
_Clc1InfoLinkUtilization_Type=Integer32
_Clc1InfoLinkUtilization_Object=MibTableColumn
clc1InfoLinkUtilization=_Clc1InfoLinkUtilization_Object((1,3,6,1,4,1,711,2,1,4,4,1,20),_Clc1InfoLinkUtilization_Type())
clc1InfoLinkUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoLinkUtilization.setStatus(_A)
class _Clc1InfoOperClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AO,1),(_AP,2)))
_Clc1InfoOperClock_Type.__name__=_C
_Clc1InfoOperClock_Object=MibTableColumn
clc1InfoOperClock=_Clc1InfoOperClock_Object((1,3,6,1,4,1,711,2,1,4,4,1,21),_Clc1InfoOperClock_Type())
clc1InfoOperClock.setMaxAccess(_B)
if mibBuilder.loadTexts:clc1InfoOperClock.setStatus(_A)
class _Clc1InfoAdminClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AO,1),(_AP,2)))
_Clc1InfoAdminClock_Type.__name__=_C
_Clc1InfoAdminClock_Object=MibTableColumn
clc1InfoAdminClock=_Clc1InfoAdminClock_Object((1,3,6,1,4,1,711,2,1,4,4,1,22),_Clc1InfoAdminClock_Type())
clc1InfoAdminClock.setMaxAccess(_D)
if mibBuilder.loadTexts:clc1InfoAdminClock.setStatus(_A)
class _Clc1InfoAdminOperTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,99)));namedValues=NamedValues(*((_X,1),(_Y,99)))
_Clc1InfoAdminOperTrigger_Type.__name__=_C
_Clc1InfoAdminOperTrigger_Object=MibTableColumn
clc1InfoAdminOperTrigger=_Clc1InfoAdminOperTrigger_Object((1,3,6,1,4,1,711,2,1,4,4,1,99),_Clc1InfoAdminOperTrigger_Type())
clc1InfoAdminOperTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:clc1InfoAdminOperTrigger.setStatus(_A)
_Oc3InfoTable_Object=MibTable
oc3InfoTable=_Oc3InfoTable_Object((1,3,6,1,4,1,711,2,1,4,5))
if mibBuilder.loadTexts:oc3InfoTable.setStatus(_A)
_Oc3InfoEntry_Object=MibTableRow
oc3InfoEntry=_Oc3InfoEntry_Object((1,3,6,1,4,1,711,2,1,4,5,1))
oc3InfoEntry.setIndexNames((0,_l,_m))
if mibBuilder.loadTexts:oc3InfoEntry.setStatus(_A)
class _Oc3InfoReceiveSignalDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_Oc3InfoReceiveSignalDetect_Type.__name__=_C
_Oc3InfoReceiveSignalDetect_Object=MibTableColumn
oc3InfoReceiveSignalDetect=_Oc3InfoReceiveSignalDetect_Object((1,3,6,1,4,1,711,2,1,4,5,1,1),_Oc3InfoReceiveSignalDetect_Type())
oc3InfoReceiveSignalDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:oc3InfoReceiveSignalDetect.setStatus(_A)
class _Oc3InfoTransmitSafetySwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Oc3InfoTransmitSafetySwitch_Type.__name__=_C
_Oc3InfoTransmitSafetySwitch_Object=MibTableColumn
oc3InfoTransmitSafetySwitch=_Oc3InfoTransmitSafetySwitch_Object((1,3,6,1,4,1,711,2,1,4,5,1,2),_Oc3InfoTransmitSafetySwitch_Type())
oc3InfoTransmitSafetySwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:oc3InfoTransmitSafetySwitch.setStatus(_A)
class _Oc3InfoMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_Oc3InfoMediumType_Type.__name__=_C
_Oc3InfoMediumType_Object=MibTableColumn
oc3InfoMediumType=_Oc3InfoMediumType_Object((1,3,6,1,4,1,711,2,1,4,5,1,3),_Oc3InfoMediumType_Type())
oc3InfoMediumType.setMaxAccess(_D)
if mibBuilder.loadTexts:oc3InfoMediumType.setStatus(_A)
_CongestionAvoidance_ObjectIdentity=ObjectIdentity
congestionAvoidance=_CongestionAvoidance_ObjectIdentity((1,3,6,1,4,1,711,2,1,5))
_CaMaxIntervalPermitLimit_Type=Integer32
_CaMaxIntervalPermitLimit_Object=MibScalar
caMaxIntervalPermitLimit=_CaMaxIntervalPermitLimit_Object((1,3,6,1,4,1,711,2,1,5,1),_CaMaxIntervalPermitLimit_Type())
caMaxIntervalPermitLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:caMaxIntervalPermitLimit.setStatus(_A)
_CaMinIntervalPermitLimit_Type=Integer32
_CaMinIntervalPermitLimit_Object=MibScalar
caMinIntervalPermitLimit=_CaMinIntervalPermitLimit_Object((1,3,6,1,4,1,711,2,1,5,2),_CaMinIntervalPermitLimit_Type())
caMinIntervalPermitLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:caMinIntervalPermitLimit.setStatus(_A)
_CaMinIntervalCaInfo_Type=Integer32
_CaMinIntervalCaInfo_Object=MibScalar
caMinIntervalCaInfo=_CaMinIntervalCaInfo_Object((1,3,6,1,4,1,711,2,1,5,3),_CaMinIntervalCaInfo_Type())
caMinIntervalCaInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:caMinIntervalCaInfo.setStatus(_A)
_MmaInfo_ObjectIdentity=ObjectIdentity
mmaInfo=_MmaInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,6))
class _MmaDbActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('newDBactive',2)))
_MmaDbActive_Type.__name__=_C
_MmaDbActive_Object=MibScalar
mmaDbActive=_MmaDbActive_Object((1,3,6,1,4,1,711,2,1,6,1),_MmaDbActive_Type())
mmaDbActive.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaDbActive.setStatus(_A)
class _MmaTrapFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3),(_g,4)))
_MmaTrapFilter_Type.__name__=_C
_MmaTrapFilter_Object=MibScalar
mmaTrapFilter=_MmaTrapFilter_Object((1,3,6,1,4,1,711,2,1,6,2),_MmaTrapFilter_Type())
mmaTrapFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaTrapFilter.setStatus(_A)
class _MmaTrapLanguage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('english',1))
_MmaTrapLanguage_Type.__name__=_C
_MmaTrapLanguage_Object=MibScalar
mmaTrapLanguage=_MmaTrapLanguage_Object((1,3,6,1,4,1,711,2,1,6,3),_MmaTrapLanguage_Type())
mmaTrapLanguage.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaTrapLanguage.setStatus(_A)
_MmaCollectionSpace_Type=Integer32
_MmaCollectionSpace_Object=MibScalar
mmaCollectionSpace=_MmaCollectionSpace_Object((1,3,6,1,4,1,711,2,1,6,4),_MmaCollectionSpace_Type())
mmaCollectionSpace.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaCollectionSpace.setStatus(_A)
class _MmaConfigHost_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MmaConfigHost_Type.__name__=_R
_MmaConfigHost_Object=MibScalar
mmaConfigHost=_MmaConfigHost_Object((1,3,6,1,4,1,711,2,1,6,5),_MmaConfigHost_Type())
mmaConfigHost.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaConfigHost.setStatus(_A)
class _MmaConfigAuthor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MmaConfigAuthor_Type.__name__=_R
_MmaConfigAuthor_Object=MibScalar
mmaConfigAuthor=_MmaConfigAuthor_Object((1,3,6,1,4,1,711,2,1,6,6),_MmaConfigAuthor_Type())
mmaConfigAuthor.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaConfigAuthor.setStatus(_A)
_MmaConfigID_Type=Integer32
_MmaConfigID_Object=MibScalar
mmaConfigID=_MmaConfigID_Object((1,3,6,1,4,1,711,2,1,6,7),_MmaConfigID_Type())
mmaConfigID.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaConfigID.setStatus(_A)
class _MmaSetLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unlock',1),('lockVolatile',2),('lockPermanent',3)))
_MmaSetLock_Type.__name__=_C
_MmaSetLock_Object=MibScalar
mmaSetLock=_MmaSetLock_Object((1,3,6,1,4,1,711,2,1,6,8),_MmaSetLock_Type())
mmaSetLock.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaSetLock.setStatus(_A)
_MmaPID_Type=Integer32
_MmaPID_Object=MibScalar
mmaPID=_MmaPID_Object((1,3,6,1,4,1,711,2,1,6,9),_MmaPID_Type())
mmaPID.setMaxAccess(_B)
if mibBuilder.loadTexts:mmaPID.setStatus(_A)
class _MmaTrapLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_MmaTrapLog_Type.__name__=_C
_MmaTrapLog_Object=MibScalar
mmaTrapLog=_MmaTrapLog_Object((1,3,6,1,4,1,711,2,1,6,10),_MmaTrapLog_Type())
mmaTrapLog.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaTrapLog.setStatus(_A)
_MmaTrapNumber_Type=Integer32
_MmaTrapNumber_Object=MibScalar
mmaTrapNumber=_MmaTrapNumber_Object((1,3,6,1,4,1,711,2,1,6,13),_MmaTrapNumber_Type())
mmaTrapNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaTrapNumber.setStatus(_A)
class _MmaTrapOnOffState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('trapOn',1),('trapOff',2),('trapEnable',3),('trapDisable',4)))
_MmaTrapOnOffState_Type.__name__=_C
_MmaTrapOnOffState_Object=MibScalar
mmaTrapOnOffState=_MmaTrapOnOffState_Object((1,3,6,1,4,1,711,2,1,6,14),_MmaTrapOnOffState_Type())
mmaTrapOnOffState.setMaxAccess(_D)
if mibBuilder.loadTexts:mmaTrapOnOffState.setStatus(_A)
_MmaNumNameTable_Object=MibTable
mmaNumNameTable=_MmaNumNameTable_Object((1,3,6,1,4,1,711,2,1,6,16))
if mibBuilder.loadTexts:mmaNumNameTable.setStatus(_A)
_MmaNumNameEntry_Object=MibTableRow
mmaNumNameEntry=_MmaNumNameEntry_Object((1,3,6,1,4,1,711,2,1,6,16,1))
mmaNumNameEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:mmaNumNameEntry.setStatus(_A)
_MmaNumNameNumber_Type=Integer32
_MmaNumNameNumber_Object=MibTableColumn
mmaNumNameNumber=_MmaNumNameNumber_Object((1,3,6,1,4,1,711,2,1,6,16,1,1),_MmaNumNameNumber_Type())
mmaNumNameNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mmaNumNameNumber.setStatus(_A)
_MmaNumName_Type=DisplayString
_MmaNumName_Object=MibTableColumn
mmaNumName=_MmaNumName_Object((1,3,6,1,4,1,711,2,1,6,16,1,2),_MmaNumName_Type())
mmaNumName.setMaxAccess(_B)
if mibBuilder.loadTexts:mmaNumName.setStatus(_A)
_MmaLwmpTimeouts_Type=Counter32
_MmaLwmpTimeouts_Object=MibScalar
mmaLwmpTimeouts=_MmaLwmpTimeouts_Object((1,3,6,1,4,1,711,2,1,6,20),_MmaLwmpTimeouts_Type())
mmaLwmpTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:mmaLwmpTimeouts.setStatus(_A)
_CollectInfo_ObjectIdentity=ObjectIdentity
collectInfo=_CollectInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,7))
_CollectTable_Object=MibTable
collectTable=_CollectTable_Object((1,3,6,1,4,1,711,2,1,7,1))
if mibBuilder.loadTexts:collectTable.setStatus(_A)
_CollectEntry_Object=MibTableRow
collectEntry=_CollectEntry_Object((1,3,6,1,4,1,711,2,1,7,1,1))
collectEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:collectEntry.setStatus(_A)
_CollectIndex_Type=Integer32
_CollectIndex_Object=MibTableColumn
collectIndex=_CollectIndex_Object((1,3,6,1,4,1,711,2,1,7,1,1,1),_CollectIndex_Type())
collectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:collectIndex.setStatus(_A)
class _CollectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_j,2),(_a,3),(_c,4)))
_CollectStatus_Type.__name__=_C
_CollectStatus_Object=MibTableColumn
collectStatus=_CollectStatus_Object((1,3,6,1,4,1,711,2,1,7,1,1,2),_CollectStatus_Type())
collectStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:collectStatus.setStatus(_A)
_CollectStart_Type=Integer32
_CollectStart_Object=MibTableColumn
collectStart=_CollectStart_Object((1,3,6,1,4,1,711,2,1,7,1,1,3),_CollectStart_Type())
collectStart.setMaxAccess(_D)
if mibBuilder.loadTexts:collectStart.setStatus(_A)
_CollectFinish_Type=Integer32
_CollectFinish_Object=MibTableColumn
collectFinish=_CollectFinish_Object((1,3,6,1,4,1,711,2,1,7,1,1,4),_CollectFinish_Type())
collectFinish.setMaxAccess(_D)
if mibBuilder.loadTexts:collectFinish.setStatus(_A)
_CollectInterval_Type=Integer32
_CollectInterval_Object=MibTableColumn
collectInterval=_CollectInterval_Object((1,3,6,1,4,1,711,2,1,7,1,1,5),_CollectInterval_Type())
collectInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:collectInterval.setStatus(_A)
class _CollectFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CollectFileName_Type.__name__=_G
_CollectFileName_Object=MibTableColumn
collectFileName=_CollectFileName_Object((1,3,6,1,4,1,711,2,1,7,1,1,6),_CollectFileName_Type())
collectFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:collectFileName.setStatus(_A)
_CollectFileSize_Type=Integer32
_CollectFileSize_Object=MibTableColumn
collectFileSize=_CollectFileSize_Object((1,3,6,1,4,1,711,2,1,7,1,1,7),_CollectFileSize_Type())
collectFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:collectFileSize.setStatus(_A)
class _CollectOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('waiting',1),('running',2),(_a,3)))
_CollectOperStatus_Type.__name__=_C
_CollectOperStatus_Object=MibTableColumn
collectOperStatus=_CollectOperStatus_Object((1,3,6,1,4,1,711,2,1,7,1,1,8),_CollectOperStatus_Type())
collectOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:collectOperStatus.setStatus(_A)
_CollectDataBase_Object=MibTable
collectDataBase=_CollectDataBase_Object((1,3,6,1,4,1,711,2,1,7,2))
if mibBuilder.loadTexts:collectDataBase.setStatus(_A)
_CollectDbEntry_Object=MibTableRow
collectDbEntry=_CollectDbEntry_Object((1,3,6,1,4,1,711,2,1,7,2,1))
collectDbEntry.setIndexNames((0,_E,_AS),(0,_E,_AT))
if mibBuilder.loadTexts:collectDbEntry.setStatus(_A)
_CollectDBIndex_Type=Integer32
_CollectDBIndex_Object=MibTableColumn
collectDBIndex=_CollectDBIndex_Object((1,3,6,1,4,1,711,2,1,7,2,1,1),_CollectDBIndex_Type())
collectDBIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:collectDBIndex.setStatus(_A)
_CollectDBInstance_Type=Integer32
_CollectDBInstance_Object=MibTableColumn
collectDBInstance=_CollectDBInstance_Object((1,3,6,1,4,1,711,2,1,7,2,1,2),_CollectDBInstance_Type())
collectDBInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:collectDBInstance.setStatus(_A)
_CollectDBObjectID_Type=ObjectIdentifier
_CollectDBObjectID_Object=MibTableColumn
collectDBObjectID=_CollectDBObjectID_Object((1,3,6,1,4,1,711,2,1,7,2,1,3),_CollectDBObjectID_Type())
collectDBObjectID.setMaxAccess(_D)
if mibBuilder.loadTexts:collectDBObjectID.setStatus(_A)
class _CollectDBStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_j,2),(_a,3),(_c,4)))
_CollectDBStatus_Type.__name__=_C
_CollectDBStatus_Object=MibTableColumn
collectDBStatus=_CollectDBStatus_Object((1,3,6,1,4,1,711,2,1,7,2,1,4),_CollectDBStatus_Type())
collectDBStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:collectDBStatus.setStatus(_A)
class _CollectCommunityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CollectCommunityName_Type.__name__=_G
_CollectCommunityName_Object=MibScalar
collectCommunityName=_CollectCommunityName_Object((1,3,6,1,4,1,711,2,1,7,3),_CollectCommunityName_Type())
collectCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:collectCommunityName.setStatus(_A)
class _RmonCommunityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RmonCommunityName_Type.__name__=_G
_RmonCommunityName_Object=MibScalar
rmonCommunityName=_RmonCommunityName_Object((1,3,6,1,4,1,711,2,1,7,4),_RmonCommunityName_Type())
rmonCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:rmonCommunityName.setStatus(_A)
_LsPortProtocols_ObjectIdentity=ObjectIdentity
lsPortProtocols=_LsPortProtocols_ObjectIdentity((1,3,6,1,4,1,711,2,1,8))
_EdgePort_ObjectIdentity=ObjectIdentity
edgePort=_EdgePort_ObjectIdentity((1,3,6,1,4,1,711,2,1,8,1))
_EdgePortTable_Object=MibTable
edgePortTable=_EdgePortTable_Object((1,3,6,1,4,1,711,2,1,8,1,1))
if mibBuilder.loadTexts:edgePortTable.setStatus(_A)
_EdgePortEntry_Object=MibTableRow
edgePortEntry=_EdgePortEntry_Object((1,3,6,1,4,1,711,2,1,8,1,1,1))
edgePortEntry.setIndexNames((0,_E,_AU))
if mibBuilder.loadTexts:edgePortEntry.setStatus(_A)
_EdgeIfIndex_Type=Integer32
_EdgeIfIndex_Object=MibTableColumn
edgeIfIndex=_EdgeIfIndex_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,1),_EdgeIfIndex_Type())
edgeIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeIfIndex.setStatus(_A)
class _EdgeUpcType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ansiCompliant',1))
_EdgeUpcType_Type.__name__=_C
_EdgeUpcType_Object=MibTableColumn
edgeUpcType=_EdgeUpcType_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,2),_EdgeUpcType_Type())
edgeUpcType.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeUpcType.setStatus(_A)
class _EdgeUserDataPerCell_Type(Integer32):defaultValue=341;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,384))
_EdgeUserDataPerCell_Type.__name__=_C
_EdgeUserDataPerCell_Object=MibTableColumn
edgeUserDataPerCell=_EdgeUserDataPerCell_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,3),_EdgeUserDataPerCell_Type())
edgeUserDataPerCell.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeUserDataPerCell.setStatus(_A)
_EdgeCellDelayVariance_Type=Integer32
_EdgeCellDelayVariance_Object=MibTableColumn
edgeCellDelayVariance=_EdgeCellDelayVariance_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,4),_EdgeCellDelayVariance_Type())
edgeCellDelayVariance.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeCellDelayVariance.setStatus(_A)
class _EdgePrincipalScale_Type(Integer32):defaultValue=100
_EdgePrincipalScale_Type.__name__=_C
_EdgePrincipalScale_Object=MibTableColumn
edgePrincipalScale=_EdgePrincipalScale_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,5),_EdgePrincipalScale_Type())
edgePrincipalScale.setMaxAccess(_D)
if mibBuilder.loadTexts:edgePrincipalScale.setStatus(_A)
class _EdgeSecondaryScale_Type(Integer32):defaultValue=2
_EdgeSecondaryScale_Type.__name__=_C
_EdgeSecondaryScale_Object=MibTableColumn
edgeSecondaryScale=_EdgeSecondaryScale_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,6),_EdgeSecondaryScale_Type())
edgeSecondaryScale.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeSecondaryScale.setStatus(_A)
class _EdgeMeteringFactor_Type(Integer32):defaultValue=64
_EdgeMeteringFactor_Type.__name__=_C
_EdgeMeteringFactor_Object=MibTableColumn
edgeMeteringFactor=_EdgeMeteringFactor_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,7),_EdgeMeteringFactor_Type())
edgeMeteringFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeMeteringFactor.setStatus(_A)
class _EdgeMeteringBurstSize_Type(Integer32):defaultValue=5
_EdgeMeteringBurstSize_Type.__name__=_C
_EdgeMeteringBurstSize_Object=MibTableColumn
edgeMeteringBurstSize=_EdgeMeteringBurstSize_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,8),_EdgeMeteringBurstSize_Type())
edgeMeteringBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeMeteringBurstSize.setStatus(_A)
class _EdgeCallSetupRetry_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_EdgeCallSetupRetry_Type.__name__=_C
_EdgeCallSetupRetry_Object=MibTableColumn
edgeCallSetupRetry=_EdgeCallSetupRetry_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,9),_EdgeCallSetupRetry_Type())
edgeCallSetupRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeCallSetupRetry.setStatus(_A)
class _EdgeCallSetupBackoff_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EdgeCallSetupBackoff_Type.__name__=_C
_EdgeCallSetupBackoff_Object=MibTableColumn
edgeCallSetupBackoff=_EdgeCallSetupBackoff_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,10),_EdgeCallSetupBackoff_Type())
edgeCallSetupBackoff.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeCallSetupBackoff.setStatus(_A)
class _EdgeMaxFrameSize_Type(Integer32):defaultValue=1516;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(48,8152))
_EdgeMaxFrameSize_Type.__name__=_C
_EdgeMaxFrameSize_Object=MibTableColumn
edgeMaxFrameSize=_EdgeMaxFrameSize_Object((1,3,6,1,4,1,711,2,1,8,1,1,1,11),_EdgeMaxFrameSize_Type())
edgeMaxFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:edgeMaxFrameSize.setStatus(_A)
_FrDceInfo_ObjectIdentity=ObjectIdentity
frDceInfo=_FrDceInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,8,2))
_FrProvMiTable_Object=MibTable
frProvMiTable=_FrProvMiTable_Object((1,3,6,1,4,1,711,2,1,8,2,1))
if mibBuilder.loadTexts:frProvMiTable.setStatus(_A)
_FrProvMiEntry_Object=MibTableRow
frProvMiEntry=_FrProvMiEntry_Object((1,3,6,1,4,1,711,2,1,8,2,1,1))
frProvMiEntry.setIndexNames((0,_E,_AV))
if mibBuilder.loadTexts:frProvMiEntry.setStatus(_A)
_FrProvMiIfIndex_Type=Integer32
_FrProvMiIfIndex_Object=MibTableColumn
frProvMiIfIndex=_FrProvMiIfIndex_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,1),_FrProvMiIfIndex_Type())
frProvMiIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frProvMiIfIndex.setStatus(_A)
class _FrProvMiState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noLmiConfigured',1),('lmiFRIF',2),('ansiT1-617-D',3),('ccittQ-933-A',4)))
_FrProvMiState_Type.__name__=_C
_FrProvMiState_Object=MibTableColumn
frProvMiState=_FrProvMiState_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,2),_FrProvMiState_Type())
frProvMiState.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiState.setStatus(_A)
class _FrProvMiAddressLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('two-octets',2))
_FrProvMiAddressLen_Type.__name__=_C
_FrProvMiAddressLen_Object=MibTableColumn
frProvMiAddressLen=_FrProvMiAddressLen_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,3),_FrProvMiAddressLen_Type())
frProvMiAddressLen.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiAddressLen.setStatus(_A)
class _FrProvMiNetRequestInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrProvMiNetRequestInterval_Type.__name__=_C
_FrProvMiNetRequestInterval_Object=MibTableColumn
frProvMiNetRequestInterval=_FrProvMiNetRequestInterval_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,4),_FrProvMiNetRequestInterval_Type())
frProvMiNetRequestInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiNetRequestInterval.setStatus(_A)
class _FrProvMiNetErrorThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrProvMiNetErrorThreshold_Type.__name__=_C
_FrProvMiNetErrorThreshold_Object=MibTableColumn
frProvMiNetErrorThreshold=_FrProvMiNetErrorThreshold_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,5),_FrProvMiNetErrorThreshold_Type())
frProvMiNetErrorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiNetErrorThreshold.setStatus(_A)
class _FrProvMiNetMonitoredEvents_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrProvMiNetMonitoredEvents_Type.__name__=_C
_FrProvMiNetMonitoredEvents_Object=MibTableColumn
frProvMiNetMonitoredEvents=_FrProvMiNetMonitoredEvents_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,6),_FrProvMiNetMonitoredEvents_Type())
frProvMiNetMonitoredEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiNetMonitoredEvents.setStatus(_A)
_FrProvMiMaxSupportedVCs_Type=Integer32
_FrProvMiMaxSupportedVCs_Object=MibTableColumn
frProvMiMaxSupportedVCs=_FrProvMiMaxSupportedVCs_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,7),_FrProvMiMaxSupportedVCs_Type())
frProvMiMaxSupportedVCs.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiMaxSupportedVCs.setStatus(_A)
class _FrProvMiMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('nonBroadcast',1))
_FrProvMiMulticast_Type.__name__=_C
_FrProvMiMulticast_Object=MibTableColumn
frProvMiMulticast=_FrProvMiMulticast_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,8),_FrProvMiMulticast_Type())
frProvMiMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiMulticast.setStatus(_A)
class _FrProvMiUserPollingInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrProvMiUserPollingInterval_Type.__name__=_C
_FrProvMiUserPollingInterval_Object=MibTableColumn
frProvMiUserPollingInterval=_FrProvMiUserPollingInterval_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,9),_FrProvMiUserPollingInterval_Type())
frProvMiUserPollingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiUserPollingInterval.setStatus(_A)
class _FrProvMiUserFullEnquiryInterval_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrProvMiUserFullEnquiryInterval_Type.__name__=_C
_FrProvMiUserFullEnquiryInterval_Object=MibTableColumn
frProvMiUserFullEnquiryInterval=_FrProvMiUserFullEnquiryInterval_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,10),_FrProvMiUserFullEnquiryInterval_Type())
frProvMiUserFullEnquiryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiUserFullEnquiryInterval.setStatus(_A)
class _FrProvMiUserErrorThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrProvMiUserErrorThreshold_Type.__name__=_C
_FrProvMiUserErrorThreshold_Object=MibTableColumn
frProvMiUserErrorThreshold=_FrProvMiUserErrorThreshold_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,11),_FrProvMiUserErrorThreshold_Type())
frProvMiUserErrorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiUserErrorThreshold.setStatus(_A)
class _FrProvMiUserMonitoredEvents_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrProvMiUserMonitoredEvents_Type.__name__=_C
_FrProvMiUserMonitoredEvents_Object=MibTableColumn
frProvMiUserMonitoredEvents=_FrProvMiUserMonitoredEvents_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,12),_FrProvMiUserMonitoredEvents_Type())
frProvMiUserMonitoredEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiUserMonitoredEvents.setStatus(_A)
class _FrProvMiNetInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('niUNI',1),('niNNI',2)))
_FrProvMiNetInterfaceType_Type.__name__=_C
_FrProvMiNetInterfaceType_Object=MibTableColumn
frProvMiNetInterfaceType=_FrProvMiNetInterfaceType_Object((1,3,6,1,4,1,711,2,1,8,2,1,1,13),_FrProvMiNetInterfaceType_Type())
frProvMiNetInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:frProvMiNetInterfaceType.setStatus(_A)
_FrCktInfo_ObjectIdentity=ObjectIdentity
frCktInfo=_FrCktInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,8,3))
_FrCktCfgTable_Object=MibTable
frCktCfgTable=_FrCktCfgTable_Object((1,3,6,1,4,1,711,2,1,8,3,1))
if mibBuilder.loadTexts:frCktCfgTable.setStatus(_A)
_FrCktEntry_Object=MibTableRow
frCktEntry=_FrCktEntry_Object((1,3,6,1,4,1,711,2,1,8,3,1,1))
frCktEntry.setIndexNames((0,_E,_AW),(0,_E,_AX))
if mibBuilder.loadTexts:frCktEntry.setStatus(_A)
_FrCktSrcNode_Type=Integer32
_FrCktSrcNode_Object=MibTableColumn
frCktSrcNode=_FrCktSrcNode_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,1),_FrCktSrcNode_Type())
frCktSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktSrcNode.setStatus(_A)
_FrCktSrcIfIndex_Type=Integer32
_FrCktSrcIfIndex_Object=MibTableColumn
frCktSrcIfIndex=_FrCktSrcIfIndex_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,2),_FrCktSrcIfIndex_Type())
frCktSrcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktSrcIfIndex.setStatus(_A)
_FrCktSrcDlci_Type=LightStreamDLCI
_FrCktSrcDlci_Object=MibTableColumn
frCktSrcDlci=_FrCktSrcDlci_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,3),_FrCktSrcDlci_Type())
frCktSrcDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktSrcDlci.setStatus(_A)
_FrCktAdminDestNode_Type=Integer32
_FrCktAdminDestNode_Object=MibTableColumn
frCktAdminDestNode=_FrCktAdminDestNode_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,10),_FrCktAdminDestNode_Type())
frCktAdminDestNode.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminDestNode.setStatus(_A)
_FrCktOperDestNode_Type=Integer32
_FrCktOperDestNode_Object=MibTableColumn
frCktOperDestNode=_FrCktOperDestNode_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,11),_FrCktOperDestNode_Type())
frCktOperDestNode.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperDestNode.setStatus(_A)
_FrCktAdminDestIfIndex_Type=Integer32
_FrCktAdminDestIfIndex_Object=MibTableColumn
frCktAdminDestIfIndex=_FrCktAdminDestIfIndex_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,12),_FrCktAdminDestIfIndex_Type())
frCktAdminDestIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminDestIfIndex.setStatus(_A)
_FrCktOperDestIfIndex_Type=Integer32
_FrCktOperDestIfIndex_Object=MibTableColumn
frCktOperDestIfIndex=_FrCktOperDestIfIndex_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,13),_FrCktOperDestIfIndex_Type())
frCktOperDestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperDestIfIndex.setStatus(_A)
_FrCktAdminDestDlci_Type=LightStreamDLCI
_FrCktAdminDestDlci_Object=MibTableColumn
frCktAdminDestDlci=_FrCktAdminDestDlci_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,14),_FrCktAdminDestDlci_Type())
frCktAdminDestDlci.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminDestDlci.setStatus(_A)
_FrCktOperDestDlci_Type=LightStreamDLCI
_FrCktOperDestDlci_Object=MibTableColumn
frCktOperDestDlci=_FrCktOperDestDlci_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,15),_FrCktOperDestDlci_Type())
frCktOperDestDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperDestDlci.setStatus(_A)
class _FrCktAdminSrcInsuredRate_Type(Integer32):defaultValue=0
_FrCktAdminSrcInsuredRate_Type.__name__=_C
_FrCktAdminSrcInsuredRate_Object=MibTableColumn
frCktAdminSrcInsuredRate=_FrCktAdminSrcInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,25),_FrCktAdminSrcInsuredRate_Type())
frCktAdminSrcInsuredRate.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminSrcInsuredRate.setStatus(_A)
class _FrCktOperSrcInsuredRate_Type(Integer32):defaultValue=0
_FrCktOperSrcInsuredRate_Type.__name__=_C
_FrCktOperSrcInsuredRate_Object=MibTableColumn
frCktOperSrcInsuredRate=_FrCktOperSrcInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,26),_FrCktOperSrcInsuredRate_Type())
frCktOperSrcInsuredRate.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperSrcInsuredRate.setStatus(_A)
class _FrCktAdminSrcInsuredBurst_Type(Integer32):defaultValue=0
_FrCktAdminSrcInsuredBurst_Type.__name__=_C
_FrCktAdminSrcInsuredBurst_Object=MibTableColumn
frCktAdminSrcInsuredBurst=_FrCktAdminSrcInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,27),_FrCktAdminSrcInsuredBurst_Type())
frCktAdminSrcInsuredBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminSrcInsuredBurst.setStatus(_A)
class _FrCktOperSrcInsuredBurst_Type(Integer32):defaultValue=0
_FrCktOperSrcInsuredBurst_Type.__name__=_C
_FrCktOperSrcInsuredBurst_Object=MibTableColumn
frCktOperSrcInsuredBurst=_FrCktOperSrcInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,28),_FrCktOperSrcInsuredBurst_Type())
frCktOperSrcInsuredBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperSrcInsuredBurst.setStatus(_A)
class _FrCktAdminSrcMaxRate_Type(Integer32):defaultValue=0
_FrCktAdminSrcMaxRate_Type.__name__=_C
_FrCktAdminSrcMaxRate_Object=MibTableColumn
frCktAdminSrcMaxRate=_FrCktAdminSrcMaxRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,29),_FrCktAdminSrcMaxRate_Type())
frCktAdminSrcMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminSrcMaxRate.setStatus(_A)
class _FrCktOperSrcMaxRate_Type(Integer32):defaultValue=0
_FrCktOperSrcMaxRate_Type.__name__=_C
_FrCktOperSrcMaxRate_Object=MibTableColumn
frCktOperSrcMaxRate=_FrCktOperSrcMaxRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,30),_FrCktOperSrcMaxRate_Type())
frCktOperSrcMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperSrcMaxRate.setStatus(_A)
class _FrCktAdminSrcMaxBurst_Type(Integer32):defaultValue=0
_FrCktAdminSrcMaxBurst_Type.__name__=_C
_FrCktAdminSrcMaxBurst_Object=MibTableColumn
frCktAdminSrcMaxBurst=_FrCktAdminSrcMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,31),_FrCktAdminSrcMaxBurst_Type())
frCktAdminSrcMaxBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminSrcMaxBurst.setStatus(_A)
class _FrCktOperSrcMaxBurst_Type(Integer32):defaultValue=0
_FrCktOperSrcMaxBurst_Type.__name__=_C
_FrCktOperSrcMaxBurst_Object=MibTableColumn
frCktOperSrcMaxBurst=_FrCktOperSrcMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,32),_FrCktOperSrcMaxBurst_Type())
frCktOperSrcMaxBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperSrcMaxBurst.setStatus(_A)
class _FrCktAdminDestInsuredRate_Type(Integer32):defaultValue=0
_FrCktAdminDestInsuredRate_Type.__name__=_C
_FrCktAdminDestInsuredRate_Object=MibTableColumn
frCktAdminDestInsuredRate=_FrCktAdminDestInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,33),_FrCktAdminDestInsuredRate_Type())
frCktAdminDestInsuredRate.setMaxAccess(_J)
if mibBuilder.loadTexts:frCktAdminDestInsuredRate.setStatus(_A)
class _FrCktOperDestInsuredRate_Type(Integer32):defaultValue=0
_FrCktOperDestInsuredRate_Type.__name__=_C
_FrCktOperDestInsuredRate_Object=MibTableColumn
frCktOperDestInsuredRate=_FrCktOperDestInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,34),_FrCktOperDestInsuredRate_Type())
frCktOperDestInsuredRate.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperDestInsuredRate.setStatus(_A)
class _FrCktAdminDestInsuredBurst_Type(Integer32):defaultValue=0
_FrCktAdminDestInsuredBurst_Type.__name__=_C
_FrCktAdminDestInsuredBurst_Object=MibTableColumn
frCktAdminDestInsuredBurst=_FrCktAdminDestInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,35),_FrCktAdminDestInsuredBurst_Type())
frCktAdminDestInsuredBurst.setMaxAccess(_J)
if mibBuilder.loadTexts:frCktAdminDestInsuredBurst.setStatus(_A)
class _FrCktOperDestInsuredBurst_Type(Integer32):defaultValue=0
_FrCktOperDestInsuredBurst_Type.__name__=_C
_FrCktOperDestInsuredBurst_Object=MibTableColumn
frCktOperDestInsuredBurst=_FrCktOperDestInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,36),_FrCktOperDestInsuredBurst_Type())
frCktOperDestInsuredBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperDestInsuredBurst.setStatus(_A)
class _FrCktAdminDestMaxRate_Type(Integer32):defaultValue=0
_FrCktAdminDestMaxRate_Type.__name__=_C
_FrCktAdminDestMaxRate_Object=MibTableColumn
frCktAdminDestMaxRate=_FrCktAdminDestMaxRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,37),_FrCktAdminDestMaxRate_Type())
frCktAdminDestMaxRate.setMaxAccess(_J)
if mibBuilder.loadTexts:frCktAdminDestMaxRate.setStatus(_A)
class _FrCktOperDestMaxRate_Type(Integer32):defaultValue=0
_FrCktOperDestMaxRate_Type.__name__=_C
_FrCktOperDestMaxRate_Object=MibTableColumn
frCktOperDestMaxRate=_FrCktOperDestMaxRate_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,38),_FrCktOperDestMaxRate_Type())
frCktOperDestMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperDestMaxRate.setStatus(_A)
class _FrCktAdminDestMaxBurst_Type(Integer32):defaultValue=0
_FrCktAdminDestMaxBurst_Type.__name__=_C
_FrCktAdminDestMaxBurst_Object=MibTableColumn
frCktAdminDestMaxBurst=_FrCktAdminDestMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,39),_FrCktAdminDestMaxBurst_Type())
frCktAdminDestMaxBurst.setMaxAccess(_J)
if mibBuilder.loadTexts:frCktAdminDestMaxBurst.setStatus(_A)
class _FrCktOperDestMaxBurst_Type(Integer32):defaultValue=0
_FrCktOperDestMaxBurst_Type.__name__=_C
_FrCktOperDestMaxBurst_Object=MibTableColumn
frCktOperDestMaxBurst=_FrCktOperDestMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,40),_FrCktOperDestMaxBurst_Type())
frCktOperDestMaxBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperDestMaxBurst.setStatus(_A)
class _FrCktOperSecondaryScale_Type(Integer32):defaultValue=255
_FrCktOperSecondaryScale_Type.__name__=_C
_FrCktOperSecondaryScale_Object=MibTableColumn
frCktOperSecondaryScale=_FrCktOperSecondaryScale_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,41),_FrCktOperSecondaryScale_Type())
frCktOperSecondaryScale.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperSecondaryScale.setStatus(_A)
class _FrCktAdminSecondaryScale_Type(Integer32):defaultValue=255
_FrCktAdminSecondaryScale_Type.__name__=_C
_FrCktAdminSecondaryScale_Object=MibTableColumn
frCktAdminSecondaryScale=_FrCktAdminSecondaryScale_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,42),_FrCktAdminSecondaryScale_Type())
frCktAdminSecondaryScale.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminSecondaryScale.setStatus(_A)
class _FrCktOperPrinBwType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_FrCktOperPrinBwType_Type.__name__=_C
_FrCktOperPrinBwType_Object=MibTableColumn
frCktOperPrinBwType=_FrCktOperPrinBwType_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,43),_FrCktOperPrinBwType_Type())
frCktOperPrinBwType.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperPrinBwType.setStatus(_A)
class _FrCktAdminPrinBwType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_FrCktAdminPrinBwType_Type.__name__=_C
_FrCktAdminPrinBwType_Object=MibTableColumn
frCktAdminPrinBwType=_FrCktAdminPrinBwType_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,44),_FrCktAdminPrinBwType_Type())
frCktAdminPrinBwType.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminPrinBwType.setStatus(_A)
class _FrCktOperTransPri_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FrCktOperTransPri_Type.__name__=_C
_FrCktOperTransPri_Object=MibTableColumn
frCktOperTransPri=_FrCktOperTransPri_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,45),_FrCktOperTransPri_Type())
frCktOperTransPri.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperTransPri.setStatus(_A)
class _FrCktAdminTransPri_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FrCktAdminTransPri_Type.__name__=_C
_FrCktAdminTransPri_Object=MibTableColumn
frCktAdminTransPri=_FrCktAdminTransPri_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,46),_FrCktAdminTransPri_Type())
frCktAdminTransPri.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminTransPri.setStatus(_A)
class _FrCktOperUserDataPerCell_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,384))
_FrCktOperUserDataPerCell_Type.__name__=_C
_FrCktOperUserDataPerCell_Object=MibTableColumn
frCktOperUserDataPerCell=_FrCktOperUserDataPerCell_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,47),_FrCktOperUserDataPerCell_Type())
frCktOperUserDataPerCell.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktOperUserDataPerCell.setStatus(_A)
class _FrCktAdminUserDataPerCell_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,384))
_FrCktAdminUserDataPerCell_Type.__name__=_C
_FrCktAdminUserDataPerCell_Object=MibTableColumn
frCktAdminUserDataPerCell=_FrCktAdminUserDataPerCell_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,48),_FrCktAdminUserDataPerCell_Type())
frCktAdminUserDataPerCell.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktAdminUserDataPerCell.setStatus(_A)
class _FrCktStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_U,3)))
_FrCktStatus_Type.__name__=_C
_FrCktStatus_Object=MibTableColumn
frCktStatus=_FrCktStatus_Object((1,3,6,1,4,1,711,2,1,8,3,1,1,99),_FrCktStatus_Type())
frCktStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:frCktStatus.setStatus(_A)
_FrCktInfoTable_Object=MibTable
frCktInfoTable=_FrCktInfoTable_Object((1,3,6,1,4,1,711,2,1,8,3,2))
if mibBuilder.loadTexts:frCktInfoTable.setStatus(_A)
_FrCktInfoEntry_Object=MibTableRow
frCktInfoEntry=_FrCktInfoEntry_Object((1,3,6,1,4,1,711,2,1,8,3,2,1))
frCktInfoEntry.setIndexNames((0,_E,_AY),(0,_E,_AZ))
if mibBuilder.loadTexts:frCktInfoEntry.setStatus(_A)
_FrCktInfoIfIndex_Type=Integer32
_FrCktInfoIfIndex_Object=MibTableColumn
frCktInfoIfIndex=_FrCktInfoIfIndex_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,1),_FrCktInfoIfIndex_Type())
frCktInfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoIfIndex.setStatus(_A)
_FrCktInfoDlci_Type=LightStreamDLCI
_FrCktInfoDlci_Object=MibTableColumn
frCktInfoDlci=_FrCktInfoDlci_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,2),_FrCktInfoDlci_Type())
frCktInfoDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoDlci.setStatus(_A)
class _FrCktInfoLclLMI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FrCktInfoLclLMI_Type.__name__=_C
_FrCktInfoLclLMI_Object=MibTableColumn
frCktInfoLclLMI=_FrCktInfoLclLMI_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,3),_FrCktInfoLclLMI_Type())
frCktInfoLclLMI.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoLclLMI.setStatus(_A)
class _FrCktInfoRmtLMI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FrCktInfoRmtLMI_Type.__name__=_C
_FrCktInfoRmtLMI_Object=MibTableColumn
frCktInfoRmtLMI=_FrCktInfoRmtLMI_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,4),_FrCktInfoRmtLMI_Type())
frCktInfoRmtLMI.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoRmtLMI.setStatus(_A)
_FrCktInfoCallIDIncoming_Type=Integer32
_FrCktInfoCallIDIncoming_Object=MibTableColumn
frCktInfoCallIDIncoming=_FrCktInfoCallIDIncoming_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,5),_FrCktInfoCallIDIncoming_Type())
frCktInfoCallIDIncoming.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoCallIDIncoming.setStatus(_A)
_FrCktInfoCallIDOutgoing_Type=Integer32
_FrCktInfoCallIDOutgoing_Object=MibTableColumn
frCktInfoCallIDOutgoing=_FrCktInfoCallIDOutgoing_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,6),_FrCktInfoCallIDOutgoing_Type())
frCktInfoCallIDOutgoing.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoCallIDOutgoing.setStatus(_A)
class _FrCktInfoDownstreamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FrCktInfoDownstreamState_Type.__name__=_C
_FrCktInfoDownstreamState_Object=MibTableColumn
frCktInfoDownstreamState=_FrCktInfoDownstreamState_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,7),_FrCktInfoDownstreamState_Type())
frCktInfoDownstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoDownstreamState.setStatus(_A)
class _FrCktInfoUpstreamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FrCktInfoUpstreamState_Type.__name__=_C
_FrCktInfoUpstreamState_Object=MibTableColumn
frCktInfoUpstreamState=_FrCktInfoUpstreamState_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,8),_FrCktInfoUpstreamState_Type())
frCktInfoUpstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoUpstreamState.setStatus(_A)
_FrCktInfoLastAtmErr_Type=OctetString
_FrCktInfoLastAtmErr_Object=MibTableColumn
frCktInfoLastAtmErr=_FrCktInfoLastAtmErr_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,9),_FrCktInfoLastAtmErr_Type())
frCktInfoLastAtmErr.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoLastAtmErr.setStatus(_A)
_FrCktInfoDataCellsRequired_Type=Integer32
_FrCktInfoDataCellsRequired_Object=MibTableColumn
frCktInfoDataCellsRequired=_FrCktInfoDataCellsRequired_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,10),_FrCktInfoDataCellsRequired_Type())
frCktInfoDataCellsRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoDataCellsRequired.setStatus(_A)
class _FrCktInfoLastAtmLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_FrCktInfoLastAtmLocation_Type.__name__=_G
_FrCktInfoLastAtmLocation_Object=MibTableColumn
frCktInfoLastAtmLocation=_FrCktInfoLastAtmLocation_Object((1,3,6,1,4,1,711,2,1,8,3,2,1,11),_FrCktInfoLastAtmLocation_Type())
frCktInfoLastAtmLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:frCktInfoLastAtmLocation.setStatus(_A)
_FfCktInfo_ObjectIdentity=ObjectIdentity
ffCktInfo=_FfCktInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,8,4))
_FfCktCfgTable_Object=MibTable
ffCktCfgTable=_FfCktCfgTable_Object((1,3,6,1,4,1,711,2,1,8,4,1))
if mibBuilder.loadTexts:ffCktCfgTable.setStatus(_A)
_FfCktEntry_Object=MibTableRow
ffCktEntry=_FfCktEntry_Object((1,3,6,1,4,1,711,2,1,8,4,1,1))
ffCktEntry.setIndexNames((0,_E,_Aa))
if mibBuilder.loadTexts:ffCktEntry.setStatus(_A)
_FfCktSrcNode_Type=Integer32
_FfCktSrcNode_Object=MibTableColumn
ffCktSrcNode=_FfCktSrcNode_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,1),_FfCktSrcNode_Type())
ffCktSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktSrcNode.setStatus(_A)
_FfCktSrcIfIndex_Type=Integer32
_FfCktSrcIfIndex_Object=MibTableColumn
ffCktSrcIfIndex=_FfCktSrcIfIndex_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,2),_FfCktSrcIfIndex_Type())
ffCktSrcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktSrcIfIndex.setStatus(_A)
_FfCktAdminDestNode_Type=Integer32
_FfCktAdminDestNode_Object=MibTableColumn
ffCktAdminDestNode=_FfCktAdminDestNode_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,9),_FfCktAdminDestNode_Type())
ffCktAdminDestNode.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminDestNode.setStatus(_A)
_FfCktOperDestNode_Type=Integer32
_FfCktOperDestNode_Object=MibTableColumn
ffCktOperDestNode=_FfCktOperDestNode_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,10),_FfCktOperDestNode_Type())
ffCktOperDestNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperDestNode.setStatus(_A)
_FfCktAdminDestIfIndex_Type=Integer32
_FfCktAdminDestIfIndex_Object=MibTableColumn
ffCktAdminDestIfIndex=_FfCktAdminDestIfIndex_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,11),_FfCktAdminDestIfIndex_Type())
ffCktAdminDestIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminDestIfIndex.setStatus(_A)
_FfCktOperDestIfIndex_Type=Integer32
_FfCktOperDestIfIndex_Object=MibTableColumn
ffCktOperDestIfIndex=_FfCktOperDestIfIndex_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,12),_FfCktOperDestIfIndex_Type())
ffCktOperDestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperDestIfIndex.setStatus(_A)
class _FfCktAdminSrcInsuredRate_Type(Integer32):defaultValue=0
_FfCktAdminSrcInsuredRate_Type.__name__=_C
_FfCktAdminSrcInsuredRate_Object=MibTableColumn
ffCktAdminSrcInsuredRate=_FfCktAdminSrcInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,21),_FfCktAdminSrcInsuredRate_Type())
ffCktAdminSrcInsuredRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminSrcInsuredRate.setStatus(_A)
class _FfCktOperSrcInsuredRate_Type(Integer32):defaultValue=-11
_FfCktOperSrcInsuredRate_Type.__name__=_C
_FfCktOperSrcInsuredRate_Object=MibTableColumn
ffCktOperSrcInsuredRate=_FfCktOperSrcInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,22),_FfCktOperSrcInsuredRate_Type())
ffCktOperSrcInsuredRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperSrcInsuredRate.setStatus(_A)
class _FfCktAdminSrcInsuredBurst_Type(Integer32):defaultValue=-1
_FfCktAdminSrcInsuredBurst_Type.__name__=_C
_FfCktAdminSrcInsuredBurst_Object=MibTableColumn
ffCktAdminSrcInsuredBurst=_FfCktAdminSrcInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,23),_FfCktAdminSrcInsuredBurst_Type())
ffCktAdminSrcInsuredBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminSrcInsuredBurst.setStatus(_A)
class _FfCktOperSrcInsuredBurst_Type(Integer32):defaultValue=-1
_FfCktOperSrcInsuredBurst_Type.__name__=_C
_FfCktOperSrcInsuredBurst_Object=MibTableColumn
ffCktOperSrcInsuredBurst=_FfCktOperSrcInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,24),_FfCktOperSrcInsuredBurst_Type())
ffCktOperSrcInsuredBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperSrcInsuredBurst.setStatus(_A)
class _FfCktAdminSrcMaxRate_Type(Integer32):defaultValue=-1
_FfCktAdminSrcMaxRate_Type.__name__=_C
_FfCktAdminSrcMaxRate_Object=MibTableColumn
ffCktAdminSrcMaxRate=_FfCktAdminSrcMaxRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,25),_FfCktAdminSrcMaxRate_Type())
ffCktAdminSrcMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminSrcMaxRate.setStatus(_A)
class _FfCktOperSrcMaxRate_Type(Integer32):defaultValue=-1
_FfCktOperSrcMaxRate_Type.__name__=_C
_FfCktOperSrcMaxRate_Object=MibTableColumn
ffCktOperSrcMaxRate=_FfCktOperSrcMaxRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,26),_FfCktOperSrcMaxRate_Type())
ffCktOperSrcMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperSrcMaxRate.setStatus(_A)
class _FfCktAdminSrcMaxBurst_Type(Integer32):defaultValue=-1
_FfCktAdminSrcMaxBurst_Type.__name__=_C
_FfCktAdminSrcMaxBurst_Object=MibTableColumn
ffCktAdminSrcMaxBurst=_FfCktAdminSrcMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,27),_FfCktAdminSrcMaxBurst_Type())
ffCktAdminSrcMaxBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminSrcMaxBurst.setStatus(_A)
class _FfCktOperSrcMaxBurst_Type(Integer32):defaultValue=-1
_FfCktOperSrcMaxBurst_Type.__name__=_C
_FfCktOperSrcMaxBurst_Object=MibTableColumn
ffCktOperSrcMaxBurst=_FfCktOperSrcMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,28),_FfCktOperSrcMaxBurst_Type())
ffCktOperSrcMaxBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperSrcMaxBurst.setStatus(_A)
class _FfCktAdminDestInsuredRate_Type(Integer32):defaultValue=-1
_FfCktAdminDestInsuredRate_Type.__name__=_C
_FfCktAdminDestInsuredRate_Object=MibTableColumn
ffCktAdminDestInsuredRate=_FfCktAdminDestInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,29),_FfCktAdminDestInsuredRate_Type())
ffCktAdminDestInsuredRate.setMaxAccess(_J)
if mibBuilder.loadTexts:ffCktAdminDestInsuredRate.setStatus(_A)
class _FfCktOperDestInsuredRate_Type(Integer32):defaultValue=-1
_FfCktOperDestInsuredRate_Type.__name__=_C
_FfCktOperDestInsuredRate_Object=MibTableColumn
ffCktOperDestInsuredRate=_FfCktOperDestInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,30),_FfCktOperDestInsuredRate_Type())
ffCktOperDestInsuredRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperDestInsuredRate.setStatus(_A)
class _FfCktAdminDestInsuredBurst_Type(Integer32):defaultValue=-1
_FfCktAdminDestInsuredBurst_Type.__name__=_C
_FfCktAdminDestInsuredBurst_Object=MibTableColumn
ffCktAdminDestInsuredBurst=_FfCktAdminDestInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,31),_FfCktAdminDestInsuredBurst_Type())
ffCktAdminDestInsuredBurst.setMaxAccess(_J)
if mibBuilder.loadTexts:ffCktAdminDestInsuredBurst.setStatus(_A)
class _FfCktOperDestInsuredBurst_Type(Integer32):defaultValue=-1
_FfCktOperDestInsuredBurst_Type.__name__=_C
_FfCktOperDestInsuredBurst_Object=MibTableColumn
ffCktOperDestInsuredBurst=_FfCktOperDestInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,32),_FfCktOperDestInsuredBurst_Type())
ffCktOperDestInsuredBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperDestInsuredBurst.setStatus(_A)
class _FfCktAdminDestMaxRate_Type(Integer32):defaultValue=-1
_FfCktAdminDestMaxRate_Type.__name__=_C
_FfCktAdminDestMaxRate_Object=MibTableColumn
ffCktAdminDestMaxRate=_FfCktAdminDestMaxRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,33),_FfCktAdminDestMaxRate_Type())
ffCktAdminDestMaxRate.setMaxAccess(_J)
if mibBuilder.loadTexts:ffCktAdminDestMaxRate.setStatus(_A)
class _FfCktOperDestMaxRate_Type(Integer32):defaultValue=-1
_FfCktOperDestMaxRate_Type.__name__=_C
_FfCktOperDestMaxRate_Object=MibTableColumn
ffCktOperDestMaxRate=_FfCktOperDestMaxRate_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,34),_FfCktOperDestMaxRate_Type())
ffCktOperDestMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperDestMaxRate.setStatus(_A)
class _FfCktAdminDestMaxBurst_Type(Integer32):defaultValue=-1
_FfCktAdminDestMaxBurst_Type.__name__=_C
_FfCktAdminDestMaxBurst_Object=MibTableColumn
ffCktAdminDestMaxBurst=_FfCktAdminDestMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,35),_FfCktAdminDestMaxBurst_Type())
ffCktAdminDestMaxBurst.setMaxAccess(_J)
if mibBuilder.loadTexts:ffCktAdminDestMaxBurst.setStatus(_A)
class _FfCktOperDestMaxBurst_Type(Integer32):defaultValue=-1
_FfCktOperDestMaxBurst_Type.__name__=_C
_FfCktOperDestMaxBurst_Object=MibTableColumn
ffCktOperDestMaxBurst=_FfCktOperDestMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,36),_FfCktOperDestMaxBurst_Type())
ffCktOperDestMaxBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperDestMaxBurst.setStatus(_A)
class _FfCktOperPrinBwType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_FfCktOperPrinBwType_Type.__name__=_C
_FfCktOperPrinBwType_Object=MibTableColumn
ffCktOperPrinBwType=_FfCktOperPrinBwType_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,37),_FfCktOperPrinBwType_Type())
ffCktOperPrinBwType.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperPrinBwType.setStatus(_A)
class _FfCktAdminPrinBwType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_FfCktAdminPrinBwType_Type.__name__=_C
_FfCktAdminPrinBwType_Object=MibTableColumn
ffCktAdminPrinBwType=_FfCktAdminPrinBwType_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,38),_FfCktAdminPrinBwType_Type())
ffCktAdminPrinBwType.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminPrinBwType.setStatus(_A)
class _FfCktOperTransPri_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FfCktOperTransPri_Type.__name__=_C
_FfCktOperTransPri_Object=MibTableColumn
ffCktOperTransPri=_FfCktOperTransPri_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,39),_FfCktOperTransPri_Type())
ffCktOperTransPri.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktOperTransPri.setStatus(_A)
class _FfCktAdminTransPri_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FfCktAdminTransPri_Type.__name__=_C
_FfCktAdminTransPri_Object=MibTableColumn
ffCktAdminTransPri=_FfCktAdminTransPri_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,40),_FfCktAdminTransPri_Type())
ffCktAdminTransPri.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktAdminTransPri.setStatus(_A)
class _FfCktStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_U,3)))
_FfCktStatus_Type.__name__=_C
_FfCktStatus_Object=MibTableColumn
ffCktStatus=_FfCktStatus_Object((1,3,6,1,4,1,711,2,1,8,4,1,1,99),_FfCktStatus_Type())
ffCktStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ffCktStatus.setStatus(_A)
_FfCktInfoTable_Object=MibTable
ffCktInfoTable=_FfCktInfoTable_Object((1,3,6,1,4,1,711,2,1,8,4,2))
if mibBuilder.loadTexts:ffCktInfoTable.setStatus(_A)
_FfCktInfoEntry_Object=MibTableRow
ffCktInfoEntry=_FfCktInfoEntry_Object((1,3,6,1,4,1,711,2,1,8,4,2,1))
ffCktInfoEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:ffCktInfoEntry.setStatus(_A)
_FfCktInfoIfIndex_Type=Integer32
_FfCktInfoIfIndex_Object=MibTableColumn
ffCktInfoIfIndex=_FfCktInfoIfIndex_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,1),_FfCktInfoIfIndex_Type())
ffCktInfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoIfIndex.setStatus(_A)
class _FfCktInfoDownstreamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FfCktInfoDownstreamState_Type.__name__=_C
_FfCktInfoDownstreamState_Object=MibTableColumn
ffCktInfoDownstreamState=_FfCktInfoDownstreamState_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,2),_FfCktInfoDownstreamState_Type())
ffCktInfoDownstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoDownstreamState.setStatus(_A)
class _FfCktInfoUpstreamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_FfCktInfoUpstreamState_Type.__name__=_C
_FfCktInfoUpstreamState_Object=MibTableColumn
ffCktInfoUpstreamState=_FfCktInfoUpstreamState_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,3),_FfCktInfoUpstreamState_Type())
ffCktInfoUpstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoUpstreamState.setStatus(_A)
_FfCktInfoCallIDIncoming_Type=Integer32
_FfCktInfoCallIDIncoming_Object=MibTableColumn
ffCktInfoCallIDIncoming=_FfCktInfoCallIDIncoming_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,4),_FfCktInfoCallIDIncoming_Type())
ffCktInfoCallIDIncoming.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoCallIDIncoming.setStatus(_A)
_FfCktInfoCallIDOutgoing_Type=Integer32
_FfCktInfoCallIDOutgoing_Object=MibTableColumn
ffCktInfoCallIDOutgoing=_FfCktInfoCallIDOutgoing_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,5),_FfCktInfoCallIDOutgoing_Type())
ffCktInfoCallIDOutgoing.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoCallIDOutgoing.setStatus(_A)
_FfCktInfoLastAtmErr_Type=OctetString
_FfCktInfoLastAtmErr_Object=MibTableColumn
ffCktInfoLastAtmErr=_FfCktInfoLastAtmErr_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,6),_FfCktInfoLastAtmErr_Type())
ffCktInfoLastAtmErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoLastAtmErr.setStatus(_A)
_FfCktInfoDataCellsRequired_Type=Integer32
_FfCktInfoDataCellsRequired_Object=MibTableColumn
ffCktInfoDataCellsRequired=_FfCktInfoDataCellsRequired_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,7),_FfCktInfoDataCellsRequired_Type())
ffCktInfoDataCellsRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoDataCellsRequired.setStatus(_A)
class _FfCktInfoLastAtmLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_FfCktInfoLastAtmLocation_Type.__name__=_G
_FfCktInfoLastAtmLocation_Object=MibTableColumn
ffCktInfoLastAtmLocation=_FfCktInfoLastAtmLocation_Object((1,3,6,1,4,1,711,2,1,8,4,2,1,8),_FfCktInfoLastAtmLocation_Type())
ffCktInfoLastAtmLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCktInfoLastAtmLocation.setStatus(_A)
_SUniCktInfo_ObjectIdentity=ObjectIdentity
sUniCktInfo=_SUniCktInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,8,5))
_SUniCktCfgTable_Object=MibTable
sUniCktCfgTable=_SUniCktCfgTable_Object((1,3,6,1,4,1,711,2,1,8,5,1))
if mibBuilder.loadTexts:sUniCktCfgTable.setStatus(_A)
_SUniCktEntry_Object=MibTableRow
sUniCktEntry=_SUniCktEntry_Object((1,3,6,1,4,1,711,2,1,8,5,1,1))
sUniCktEntry.setIndexNames((0,_E,_Ac),(0,_E,_Ad))
if mibBuilder.loadTexts:sUniCktEntry.setStatus(_A)
_SUniCktSrcNode_Type=Integer32
_SUniCktSrcNode_Object=MibTableColumn
sUniCktSrcNode=_SUniCktSrcNode_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,1),_SUniCktSrcNode_Type())
sUniCktSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktSrcNode.setStatus(_A)
_SUniCktSrcIfIndex_Type=Integer32
_SUniCktSrcIfIndex_Object=MibTableColumn
sUniCktSrcIfIndex=_SUniCktSrcIfIndex_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,2),_SUniCktSrcIfIndex_Type())
sUniCktSrcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktSrcIfIndex.setStatus(_A)
_SUniCktSrcVCI_Type=VCI
_SUniCktSrcVCI_Object=MibTableColumn
sUniCktSrcVCI=_SUniCktSrcVCI_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,3),_SUniCktSrcVCI_Type())
sUniCktSrcVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktSrcVCI.setStatus(_A)
_SUniCktAdminDestNode_Type=Integer32
_SUniCktAdminDestNode_Object=MibTableColumn
sUniCktAdminDestNode=_SUniCktAdminDestNode_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,10),_SUniCktAdminDestNode_Type())
sUniCktAdminDestNode.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminDestNode.setStatus(_A)
_SUniCktOperDestNode_Type=Integer32
_SUniCktOperDestNode_Object=MibTableColumn
sUniCktOperDestNode=_SUniCktOperDestNode_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,11),_SUniCktOperDestNode_Type())
sUniCktOperDestNode.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperDestNode.setStatus(_A)
_SUniCktAdminDestIfIndex_Type=Integer32
_SUniCktAdminDestIfIndex_Object=MibTableColumn
sUniCktAdminDestIfIndex=_SUniCktAdminDestIfIndex_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,12),_SUniCktAdminDestIfIndex_Type())
sUniCktAdminDestIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminDestIfIndex.setStatus(_A)
_SUniCktOperDestIfIndex_Type=Integer32
_SUniCktOperDestIfIndex_Object=MibTableColumn
sUniCktOperDestIfIndex=_SUniCktOperDestIfIndex_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,13),_SUniCktOperDestIfIndex_Type())
sUniCktOperDestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperDestIfIndex.setStatus(_A)
_SUniCktAdminDestVCI_Type=VCI
_SUniCktAdminDestVCI_Object=MibTableColumn
sUniCktAdminDestVCI=_SUniCktAdminDestVCI_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,14),_SUniCktAdminDestVCI_Type())
sUniCktAdminDestVCI.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminDestVCI.setStatus(_A)
_SUniCktOperDestVCI_Type=VCI
_SUniCktOperDestVCI_Object=MibTableColumn
sUniCktOperDestVCI=_SUniCktOperDestVCI_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,15),_SUniCktOperDestVCI_Type())
sUniCktOperDestVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperDestVCI.setStatus(_A)
class _SUniCktOperPrinBwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SUniCktOperPrinBwType_Type.__name__=_C
_SUniCktOperPrinBwType_Object=MibTableColumn
sUniCktOperPrinBwType=_SUniCktOperPrinBwType_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,22),_SUniCktOperPrinBwType_Type())
sUniCktOperPrinBwType.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperPrinBwType.setStatus(_A)
class _SUniCktAdminPrinBwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SUniCktAdminPrinBwType_Type.__name__=_C
_SUniCktAdminPrinBwType_Object=MibTableColumn
sUniCktAdminPrinBwType=_SUniCktAdminPrinBwType_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,23),_SUniCktAdminPrinBwType_Type())
sUniCktAdminPrinBwType.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminPrinBwType.setStatus(_A)
class _SUniCktOperTransPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SUniCktOperTransPri_Type.__name__=_C
_SUniCktOperTransPri_Object=MibTableColumn
sUniCktOperTransPri=_SUniCktOperTransPri_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,24),_SUniCktOperTransPri_Type())
sUniCktOperTransPri.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperTransPri.setStatus(_A)
class _SUniCktAdminTransPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SUniCktAdminTransPri_Type.__name__=_C
_SUniCktAdminTransPri_Object=MibTableColumn
sUniCktAdminTransPri=_SUniCktAdminTransPri_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,25),_SUniCktAdminTransPri_Type())
sUniCktAdminTransPri.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminTransPri.setStatus(_A)
class _SUniCktAdminSrcInsuredRate_Type(Integer32):defaultValue=0
_SUniCktAdminSrcInsuredRate_Type.__name__=_C
_SUniCktAdminSrcInsuredRate_Object=MibTableColumn
sUniCktAdminSrcInsuredRate=_SUniCktAdminSrcInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,26),_SUniCktAdminSrcInsuredRate_Type())
sUniCktAdminSrcInsuredRate.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminSrcInsuredRate.setStatus(_A)
class _SUniCktOperSrcInsuredRate_Type(Integer32):defaultValue=0
_SUniCktOperSrcInsuredRate_Type.__name__=_C
_SUniCktOperSrcInsuredRate_Object=MibTableColumn
sUniCktOperSrcInsuredRate=_SUniCktOperSrcInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,27),_SUniCktOperSrcInsuredRate_Type())
sUniCktOperSrcInsuredRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperSrcInsuredRate.setStatus(_A)
class _SUniCktAdminSrcInsuredBurst_Type(Integer32):defaultValue=0
_SUniCktAdminSrcInsuredBurst_Type.__name__=_C
_SUniCktAdminSrcInsuredBurst_Object=MibTableColumn
sUniCktAdminSrcInsuredBurst=_SUniCktAdminSrcInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,28),_SUniCktAdminSrcInsuredBurst_Type())
sUniCktAdminSrcInsuredBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminSrcInsuredBurst.setStatus(_A)
class _SUniCktOperSrcInsuredBurst_Type(Integer32):defaultValue=0
_SUniCktOperSrcInsuredBurst_Type.__name__=_C
_SUniCktOperSrcInsuredBurst_Object=MibTableColumn
sUniCktOperSrcInsuredBurst=_SUniCktOperSrcInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,29),_SUniCktOperSrcInsuredBurst_Type())
sUniCktOperSrcInsuredBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperSrcInsuredBurst.setStatus(_A)
class _SUniCktAdminSrcMaxRate_Type(Integer32):defaultValue=0
_SUniCktAdminSrcMaxRate_Type.__name__=_C
_SUniCktAdminSrcMaxRate_Object=MibTableColumn
sUniCktAdminSrcMaxRate=_SUniCktAdminSrcMaxRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,30),_SUniCktAdminSrcMaxRate_Type())
sUniCktAdminSrcMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminSrcMaxRate.setStatus(_A)
class _SUniCktOperSrcMaxRate_Type(Integer32):defaultValue=0
_SUniCktOperSrcMaxRate_Type.__name__=_C
_SUniCktOperSrcMaxRate_Object=MibTableColumn
sUniCktOperSrcMaxRate=_SUniCktOperSrcMaxRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,31),_SUniCktOperSrcMaxRate_Type())
sUniCktOperSrcMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperSrcMaxRate.setStatus(_A)
class _SUniCktAdminSrcMaxBurst_Type(Integer32):defaultValue=0
_SUniCktAdminSrcMaxBurst_Type.__name__=_C
_SUniCktAdminSrcMaxBurst_Object=MibTableColumn
sUniCktAdminSrcMaxBurst=_SUniCktAdminSrcMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,32),_SUniCktAdminSrcMaxBurst_Type())
sUniCktAdminSrcMaxBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminSrcMaxBurst.setStatus(_A)
class _SUniCktOperSrcMaxBurst_Type(Integer32):defaultValue=0
_SUniCktOperSrcMaxBurst_Type.__name__=_C
_SUniCktOperSrcMaxBurst_Object=MibTableColumn
sUniCktOperSrcMaxBurst=_SUniCktOperSrcMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,33),_SUniCktOperSrcMaxBurst_Type())
sUniCktOperSrcMaxBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperSrcMaxBurst.setStatus(_A)
class _SUniCktAdminDestInsuredRate_Type(Integer32):defaultValue=0
_SUniCktAdminDestInsuredRate_Type.__name__=_C
_SUniCktAdminDestInsuredRate_Object=MibTableColumn
sUniCktAdminDestInsuredRate=_SUniCktAdminDestInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,34),_SUniCktAdminDestInsuredRate_Type())
sUniCktAdminDestInsuredRate.setMaxAccess(_J)
if mibBuilder.loadTexts:sUniCktAdminDestInsuredRate.setStatus(_A)
class _SUniCktOperDestInsuredRate_Type(Integer32):defaultValue=0
_SUniCktOperDestInsuredRate_Type.__name__=_C
_SUniCktOperDestInsuredRate_Object=MibTableColumn
sUniCktOperDestInsuredRate=_SUniCktOperDestInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,35),_SUniCktOperDestInsuredRate_Type())
sUniCktOperDestInsuredRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperDestInsuredRate.setStatus(_A)
class _SUniCktAdminDestInsuredBurst_Type(Integer32):defaultValue=0
_SUniCktAdminDestInsuredBurst_Type.__name__=_C
_SUniCktAdminDestInsuredBurst_Object=MibTableColumn
sUniCktAdminDestInsuredBurst=_SUniCktAdminDestInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,36),_SUniCktAdminDestInsuredBurst_Type())
sUniCktAdminDestInsuredBurst.setMaxAccess(_J)
if mibBuilder.loadTexts:sUniCktAdminDestInsuredBurst.setStatus(_A)
class _SUniCktOperDestInsuredBurst_Type(Integer32):defaultValue=0
_SUniCktOperDestInsuredBurst_Type.__name__=_C
_SUniCktOperDestInsuredBurst_Object=MibTableColumn
sUniCktOperDestInsuredBurst=_SUniCktOperDestInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,37),_SUniCktOperDestInsuredBurst_Type())
sUniCktOperDestInsuredBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperDestInsuredBurst.setStatus(_A)
class _SUniCktAdminDestMaxRate_Type(Integer32):defaultValue=0
_SUniCktAdminDestMaxRate_Type.__name__=_C
_SUniCktAdminDestMaxRate_Object=MibTableColumn
sUniCktAdminDestMaxRate=_SUniCktAdminDestMaxRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,38),_SUniCktAdminDestMaxRate_Type())
sUniCktAdminDestMaxRate.setMaxAccess(_J)
if mibBuilder.loadTexts:sUniCktAdminDestMaxRate.setStatus(_A)
class _SUniCktOperDestMaxRate_Type(Integer32):defaultValue=0
_SUniCktOperDestMaxRate_Type.__name__=_C
_SUniCktOperDestMaxRate_Object=MibTableColumn
sUniCktOperDestMaxRate=_SUniCktOperDestMaxRate_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,39),_SUniCktOperDestMaxRate_Type())
sUniCktOperDestMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperDestMaxRate.setStatus(_A)
class _SUniCktAdminDestMaxBurst_Type(Integer32):defaultValue=0
_SUniCktAdminDestMaxBurst_Type.__name__=_C
_SUniCktAdminDestMaxBurst_Object=MibTableColumn
sUniCktAdminDestMaxBurst=_SUniCktAdminDestMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,40),_SUniCktAdminDestMaxBurst_Type())
sUniCktAdminDestMaxBurst.setMaxAccess(_J)
if mibBuilder.loadTexts:sUniCktAdminDestMaxBurst.setStatus(_A)
class _SUniCktOperDestMaxBurst_Type(Integer32):defaultValue=0
_SUniCktOperDestMaxBurst_Type.__name__=_C
_SUniCktOperDestMaxBurst_Object=MibTableColumn
sUniCktOperDestMaxBurst=_SUniCktOperDestMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,41),_SUniCktOperDestMaxBurst_Type())
sUniCktOperDestMaxBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperDestMaxBurst.setStatus(_A)
class _SUniCktAdminSecondaryScale_Type(Integer32):defaultValue=255
_SUniCktAdminSecondaryScale_Type.__name__=_C
_SUniCktAdminSecondaryScale_Object=MibTableColumn
sUniCktAdminSecondaryScale=_SUniCktAdminSecondaryScale_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,42),_SUniCktAdminSecondaryScale_Type())
sUniCktAdminSecondaryScale.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktAdminSecondaryScale.setStatus(_A)
class _SUniCktOperSecondaryScale_Type(Integer32):defaultValue=255
_SUniCktOperSecondaryScale_Type.__name__=_C
_SUniCktOperSecondaryScale_Object=MibTableColumn
sUniCktOperSecondaryScale=_SUniCktOperSecondaryScale_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,43),_SUniCktOperSecondaryScale_Type())
sUniCktOperSecondaryScale.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktOperSecondaryScale.setStatus(_A)
class _SUniCktSts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_U,3)))
_SUniCktSts_Type.__name__=_C
_SUniCktSts_Object=MibTableColumn
sUniCktSts=_SUniCktSts_Object((1,3,6,1,4,1,711,2,1,8,5,1,1,99),_SUniCktSts_Type())
sUniCktSts.setMaxAccess(_D)
if mibBuilder.loadTexts:sUniCktSts.setStatus(_A)
_SUniCktInfoTable_Object=MibTable
sUniCktInfoTable=_SUniCktInfoTable_Object((1,3,6,1,4,1,711,2,1,8,5,2))
if mibBuilder.loadTexts:sUniCktInfoTable.setStatus(_A)
_SUniCktInfoEntry_Object=MibTableRow
sUniCktInfoEntry=_SUniCktInfoEntry_Object((1,3,6,1,4,1,711,2,1,8,5,2,1))
sUniCktInfoEntry.setIndexNames((0,_E,_Ae),(0,_E,_Af))
if mibBuilder.loadTexts:sUniCktInfoEntry.setStatus(_A)
_SUniCktInfoIfIndex_Type=Integer32
_SUniCktInfoIfIndex_Object=MibTableColumn
sUniCktInfoIfIndex=_SUniCktInfoIfIndex_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,1),_SUniCktInfoIfIndex_Type())
sUniCktInfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoIfIndex.setStatus(_A)
_SUniCktInfoVCI_Type=VCI
_SUniCktInfoVCI_Object=MibTableColumn
sUniCktInfoVCI=_SUniCktInfoVCI_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,2),_SUniCktInfoVCI_Type())
sUniCktInfoVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoVCI.setStatus(_A)
_SUniCktInfoUniToNetCallID_Type=Integer32
_SUniCktInfoUniToNetCallID_Object=MibTableColumn
sUniCktInfoUniToNetCallID=_SUniCktInfoUniToNetCallID_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,3),_SUniCktInfoUniToNetCallID_Type())
sUniCktInfoUniToNetCallID.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoUniToNetCallID.setStatus(_A)
_SUniCktInfoNetToUniCallID_Type=Integer32
_SUniCktInfoNetToUniCallID_Object=MibTableColumn
sUniCktInfoNetToUniCallID=_SUniCktInfoNetToUniCallID_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,4),_SUniCktInfoNetToUniCallID_Type())
sUniCktInfoNetToUniCallID.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoNetToUniCallID.setStatus(_A)
class _SUniCktInfoUniToNetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SUniCktInfoUniToNetState_Type.__name__=_C
_SUniCktInfoUniToNetState_Object=MibTableColumn
sUniCktInfoUniToNetState=_SUniCktInfoUniToNetState_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,5),_SUniCktInfoUniToNetState_Type())
sUniCktInfoUniToNetState.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoUniToNetState.setStatus(_A)
class _SUniCktInfoNetToUniState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SUniCktInfoNetToUniState_Type.__name__=_C
_SUniCktInfoNetToUniState_Object=MibTableColumn
sUniCktInfoNetToUniState=_SUniCktInfoNetToUniState_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,6),_SUniCktInfoNetToUniState_Type())
sUniCktInfoNetToUniState.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoNetToUniState.setStatus(_A)
_SUniCktInfoLastAtmErr_Type=OctetString
_SUniCktInfoLastAtmErr_Object=MibTableColumn
sUniCktInfoLastAtmErr=_SUniCktInfoLastAtmErr_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,7),_SUniCktInfoLastAtmErr_Type())
sUniCktInfoLastAtmErr.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoLastAtmErr.setStatus(_A)
_SUniCktInfoDataCellsRequired_Type=Integer32
_SUniCktInfoDataCellsRequired_Object=MibTableColumn
sUniCktInfoDataCellsRequired=_SUniCktInfoDataCellsRequired_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,8),_SUniCktInfoDataCellsRequired_Type())
sUniCktInfoDataCellsRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoDataCellsRequired.setStatus(_A)
class _SUniCktInfoLastAtmLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_SUniCktInfoLastAtmLocation_Type.__name__=_G
_SUniCktInfoLastAtmLocation_Object=MibTableColumn
sUniCktInfoLastAtmLocation=_SUniCktInfoLastAtmLocation_Object((1,3,6,1,4,1,711,2,1,8,5,2,1,9),_SUniCktInfoLastAtmLocation_Type())
sUniCktInfoLastAtmLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sUniCktInfoLastAtmLocation.setStatus(_A)
_PvcInfo_ObjectIdentity=ObjectIdentity
pvcInfo=_PvcInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,8,6))
_PvcCfgTable_Object=MibTable
pvcCfgTable=_PvcCfgTable_Object((1,3,6,1,4,1,711,2,1,8,6,1))
if mibBuilder.loadTexts:pvcCfgTable.setStatus(_A)
_PvcEntry_Object=MibTableRow
pvcEntry=_PvcEntry_Object((1,3,6,1,4,1,711,2,1,8,6,1,1))
pvcEntry.setIndexNames((0,_E,_Ag),(0,_E,_Ah))
if mibBuilder.loadTexts:pvcEntry.setStatus(_A)
_PvcSrcIfIndex_Type=Integer32
_PvcSrcIfIndex_Object=MibTableColumn
pvcSrcIfIndex=_PvcSrcIfIndex_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,1),_PvcSrcIfIndex_Type())
pvcSrcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pvcSrcIfIndex.setStatus(_A)
_PvcSrcPvcId_Type=Integer32
_PvcSrcPvcId_Object=MibTableColumn
pvcSrcPvcId=_PvcSrcPvcId_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,2),_PvcSrcPvcId_Type())
pvcSrcPvcId.setMaxAccess(_B)
if mibBuilder.loadTexts:pvcSrcPvcId.setStatus(_A)
_PvcSrcNode_Type=Integer32
_PvcSrcNode_Object=MibTableColumn
pvcSrcNode=_PvcSrcNode_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,3),_PvcSrcNode_Type())
pvcSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:pvcSrcNode.setStatus(_A)
class _PvcSrcInsuredRate_Type(Integer32):defaultValue=0
_PvcSrcInsuredRate_Type.__name__=_C
_PvcSrcInsuredRate_Object=MibTableColumn
pvcSrcInsuredRate=_PvcSrcInsuredRate_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,4),_PvcSrcInsuredRate_Type())
pvcSrcInsuredRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcSrcInsuredRate.setStatus(_A)
class _PvcSrcInsuredBurst_Type(Integer32):defaultValue=0
_PvcSrcInsuredBurst_Type.__name__=_C
_PvcSrcInsuredBurst_Object=MibTableColumn
pvcSrcInsuredBurst=_PvcSrcInsuredBurst_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,5),_PvcSrcInsuredBurst_Type())
pvcSrcInsuredBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcSrcInsuredBurst.setStatus(_A)
class _PvcSrcMaxRate_Type(Integer32):defaultValue=0
_PvcSrcMaxRate_Type.__name__=_C
_PvcSrcMaxRate_Object=MibTableColumn
pvcSrcMaxRate=_PvcSrcMaxRate_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,6),_PvcSrcMaxRate_Type())
pvcSrcMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcSrcMaxRate.setStatus(_A)
class _PvcSrcMaxBurst_Type(Integer32):defaultValue=0
_PvcSrcMaxBurst_Type.__name__=_C
_PvcSrcMaxBurst_Object=MibTableColumn
pvcSrcMaxBurst=_PvcSrcMaxBurst_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,7),_PvcSrcMaxBurst_Type())
pvcSrcMaxBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcSrcMaxBurst.setStatus(_A)
class _PvcSecondaryScale_Type(Integer32):defaultValue=255
_PvcSecondaryScale_Type.__name__=_C
_PvcSecondaryScale_Object=MibTableColumn
pvcSecondaryScale=_PvcSecondaryScale_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,8),_PvcSecondaryScale_Type())
pvcSecondaryScale.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcSecondaryScale.setStatus(_A)
class _PvcPrinBwType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_PvcPrinBwType_Type.__name__=_C
_PvcPrinBwType_Object=MibTableColumn
pvcPrinBwType=_PvcPrinBwType_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,9),_PvcPrinBwType_Type())
pvcPrinBwType.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcPrinBwType.setStatus(_A)
class _PvcTransPri_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_PvcTransPri_Type.__name__=_C
_PvcTransPri_Object=MibTableColumn
pvcTransPri=_PvcTransPri_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,10),_PvcTransPri_Type())
pvcTransPri.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcTransPri.setStatus(_A)
class _PvcUserDataPerCell_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,384))
_PvcUserDataPerCell_Type.__name__=_C
_PvcUserDataPerCell_Object=MibTableColumn
pvcUserDataPerCell=_PvcUserDataPerCell_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,11),_PvcUserDataPerCell_Type())
pvcUserDataPerCell.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcUserDataPerCell.setStatus(_A)
class _PvcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_U,3)))
_PvcStatus_Type.__name__=_C
_PvcStatus_Object=MibTableColumn
pvcStatus=_PvcStatus_Object((1,3,6,1,4,1,711,2,1,8,6,1,1,99),_PvcStatus_Type())
pvcStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pvcStatus.setStatus(_A)
_McEndptInfo_ObjectIdentity=ObjectIdentity
mcEndptInfo=_McEndptInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,8,7))
_McEndptCfgTable_Object=MibTable
mcEndptCfgTable=_McEndptCfgTable_Object((1,3,6,1,4,1,711,2,1,8,7,1))
if mibBuilder.loadTexts:mcEndptCfgTable.setStatus(_A)
_McEndptEntry_Object=MibTableRow
mcEndptEntry=_McEndptEntry_Object((1,3,6,1,4,1,711,2,1,8,7,1,1))
mcEndptEntry.setIndexNames((0,_E,_Ai),(0,_E,_Aj),(0,_E,_Ak))
if mibBuilder.loadTexts:mcEndptEntry.setStatus(_A)
_McEndptLclIfIndex_Type=Integer32
_McEndptLclIfIndex_Object=MibTableColumn
mcEndptLclIfIndex=_McEndptLclIfIndex_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,1),_McEndptLclIfIndex_Type())
mcEndptLclIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptLclIfIndex.setStatus(_A)
_McEndptLclCktid_Type=Integer32
_McEndptLclCktid_Object=MibTableColumn
mcEndptLclCktid=_McEndptLclCktid_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,2),_McEndptLclCktid_Type())
mcEndptLclCktid.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptLclCktid.setStatus(_A)
_McEndptLclInstance_Type=Integer32
_McEndptLclInstance_Object=MibTableColumn
mcEndptLclInstance=_McEndptLclInstance_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,3),_McEndptLclInstance_Type())
mcEndptLclInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptLclInstance.setStatus(_A)
class _McEndptDest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_McEndptDest_Type.__name__=_G
_McEndptDest_Object=MibTableColumn
mcEndptDest=_McEndptDest_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,4),_McEndptDest_Type())
mcEndptDest.setMaxAccess(_D)
if mibBuilder.loadTexts:mcEndptDest.setStatus(_A)
_McEndptServiceType_Type=Integer32
_McEndptServiceType_Object=MibTableColumn
mcEndptServiceType=_McEndptServiceType_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,5),_McEndptServiceType_Type())
mcEndptServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:mcEndptServiceType.setStatus(_A)
class _McEndptRmtVCstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_McEndptRmtVCstatus_Type.__name__=_C
_McEndptRmtVCstatus_Object=MibTableColumn
mcEndptRmtVCstatus=_McEndptRmtVCstatus_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,6),_McEndptRmtVCstatus_Type())
mcEndptRmtVCstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptRmtVCstatus.setStatus(_A)
_McEndptCallIDIncoming_Type=Integer32
_McEndptCallIDIncoming_Object=MibTableColumn
mcEndptCallIDIncoming=_McEndptCallIDIncoming_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,7),_McEndptCallIDIncoming_Type())
mcEndptCallIDIncoming.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptCallIDIncoming.setStatus(_A)
class _McEndptDownstreamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_McEndptDownstreamState_Type.__name__=_C
_McEndptDownstreamState_Object=MibTableColumn
mcEndptDownstreamState=_McEndptDownstreamState_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,8),_McEndptDownstreamState_Type())
mcEndptDownstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptDownstreamState.setStatus(_A)
class _McEndptUpstreamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_McEndptUpstreamState_Type.__name__=_C
_McEndptUpstreamState_Object=MibTableColumn
mcEndptUpstreamState=_McEndptUpstreamState_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,9),_McEndptUpstreamState_Type())
mcEndptUpstreamState.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptUpstreamState.setStatus(_A)
_McEndptLastAtmErr_Type=OctetString
_McEndptLastAtmErr_Object=MibTableColumn
mcEndptLastAtmErr=_McEndptLastAtmErr_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,10),_McEndptLastAtmErr_Type())
mcEndptLastAtmErr.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptLastAtmErr.setStatus(_A)
class _McEndptLastAtmLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_McEndptLastAtmLocation_Type.__name__=_G
_McEndptLastAtmLocation_Object=MibTableColumn
mcEndptLastAtmLocation=_McEndptLastAtmLocation_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,11),_McEndptLastAtmLocation_Type())
mcEndptLastAtmLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:mcEndptLastAtmLocation.setStatus(_A)
class _McEndptStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_L,2),(_U,3),(_j,4),(_a,5)))
_McEndptStatus_Type.__name__=_C
_McEndptStatus_Object=MibTableColumn
mcEndptStatus=_McEndptStatus_Object((1,3,6,1,4,1,711,2,1,8,7,1,1,99),_McEndptStatus_Type())
mcEndptStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mcEndptStatus.setStatus(_A)
_LsPrivate_ObjectIdentity=ObjectIdentity
lsPrivate=_LsPrivate_ObjectIdentity((1,3,6,1,4,1,711,2,1,10))
_LsExperimental_ObjectIdentity=ObjectIdentity
lsExperimental=_LsExperimental_ObjectIdentity((1,3,6,1,4,1,711,2,1,11))
_LsExperimentalStatistics_ObjectIdentity=ObjectIdentity
lsExperimentalStatistics=_LsExperimentalStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,11,1))
_LsEdgeStatistics_ObjectIdentity=ObjectIdentity
lsEdgeStatistics=_LsEdgeStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,11,1,1))
_LsEdgeStatTable_Object=MibTable
lsEdgeStatTable=_LsEdgeStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,1,1))
if mibBuilder.loadTexts:lsEdgeStatTable.setStatus(_A)
_LsEdgeStatEntry_Object=MibTableRow
lsEdgeStatEntry=_LsEdgeStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1))
lsEdgeStatEntry.setIndexNames((0,_E,_Al))
if mibBuilder.loadTexts:lsEdgeStatEntry.setStatus(_A)
_EdgeStatIndex_Type=Integer32
_EdgeStatIndex_Object=MibTableColumn
edgeStatIndex=_EdgeStatIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,1),_EdgeStatIndex_Type())
edgeStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeStatIndex.setStatus(_A)
_EdgeStatFsuRATOs_Type=Counter32
_EdgeStatFsuRATOs_Object=MibTableColumn
edgeStatFsuRATOs=_EdgeStatFsuRATOs_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,2),_EdgeStatFsuRATOs_Type())
edgeStatFsuRATOs.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeStatFsuRATOs.setStatus(_A)
_EdgeStatFsuRATOLastInfo_Type=Integer32
_EdgeStatFsuRATOLastInfo_Object=MibTableColumn
edgeStatFsuRATOLastInfo=_EdgeStatFsuRATOLastInfo_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,3),_EdgeStatFsuRATOLastInfo_Type())
edgeStatFsuRATOLastInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeStatFsuRATOLastInfo.setStatus(_A)
_EdgeStatTsuHoldQCells_Type=Gauge32
_EdgeStatTsuHoldQCells_Object=MibTableColumn
edgeStatTsuHoldQCells=_EdgeStatTsuHoldQCells_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,4),_EdgeStatTsuHoldQCells_Type())
edgeStatTsuHoldQCells.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeStatTsuHoldQCells.setStatus(_A)
_EdgeStatTsuHoldQs_Type=Gauge32
_EdgeStatTsuHoldQs_Object=MibTableColumn
edgeStatTsuHoldQs=_EdgeStatTsuHoldQs_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,5),_EdgeStatTsuHoldQs_Type())
edgeStatTsuHoldQs.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeStatTsuHoldQs.setStatus(_A)
_TluAAL5XsumErrs_Type=Counter32
_TluAAL5XsumErrs_Object=MibTableColumn
tluAAL5XsumErrs=_TluAAL5XsumErrs_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,6),_TluAAL5XsumErrs_Type())
tluAAL5XsumErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:tluAAL5XsumErrs.setStatus(_A)
_TluAAL5AbortErrs_Type=Counter32
_TluAAL5AbortErrs_Object=MibTableColumn
tluAAL5AbortErrs=_TluAAL5AbortErrs_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,7),_TluAAL5AbortErrs_Type())
tluAAL5AbortErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:tluAAL5AbortErrs.setStatus(_A)
_TluAAL5ErrLastVci_Type=Integer32
_TluAAL5ErrLastVci_Object=MibTableColumn
tluAAL5ErrLastVci=_TluAAL5ErrLastVci_Object((1,3,6,1,4,1,711,2,1,11,1,1,1,1,8),_TluAAL5ErrLastVci_Type())
tluAAL5ErrLastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:tluAAL5ErrLastVci.setStatus(_A)
_LsEdgePortStatTable_Object=MibTable
lsEdgePortStatTable=_LsEdgePortStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,1,2))
if mibBuilder.loadTexts:lsEdgePortStatTable.setStatus(_A)
_LsEdgePortStatEntry_Object=MibTableRow
lsEdgePortStatEntry=_LsEdgePortStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1))
lsEdgePortStatEntry.setIndexNames((0,_E,_Am))
if mibBuilder.loadTexts:lsEdgePortStatEntry.setStatus(_A)
_EdgePortStatIndex_Type=Integer32
_EdgePortStatIndex_Object=MibTableColumn
edgePortStatIndex=_EdgePortStatIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,1),_EdgePortStatIndex_Type())
edgePortStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortStatIndex.setStatus(_A)
_EdgePortRcvOctets_Type=Counter32
_EdgePortRcvOctets_Object=MibTableColumn
edgePortRcvOctets=_EdgePortRcvOctets_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,2),_EdgePortRcvOctets_Type())
edgePortRcvOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvOctets.setStatus(_A)
_EdgePortXmtOctets_Type=Counter32
_EdgePortXmtOctets_Object=MibTableColumn
edgePortXmtOctets=_EdgePortXmtOctets_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,3),_EdgePortXmtOctets_Type())
edgePortXmtOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortXmtOctets.setStatus(_A)
_EdgePortFsuCksmErrMsgs_Type=Counter32
_EdgePortFsuCksmErrMsgs_Object=MibTableColumn
edgePortFsuCksmErrMsgs=_EdgePortFsuCksmErrMsgs_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,4),_EdgePortFsuCksmErrMsgs_Type())
edgePortFsuCksmErrMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortFsuCksmErrMsgs.setStatus(_A)
_EdgePortCksmErrLastVci_Type=Integer32
_EdgePortCksmErrLastVci_Object=MibTableColumn
edgePortCksmErrLastVci=_EdgePortCksmErrLastVci_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,5),_EdgePortCksmErrLastVci_Type())
edgePortCksmErrLastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortCksmErrLastVci.setStatus(_A)
_EdgePortDownXmtFrames_Type=Counter32
_EdgePortDownXmtFrames_Object=MibTableColumn
edgePortDownXmtFrames=_EdgePortDownXmtFrames_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,6),_EdgePortDownXmtFrames_Type())
edgePortDownXmtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortDownXmtFrames.setStatus(_A)
_EdgePortRcvUcastPkts_Type=Counter32
_EdgePortRcvUcastPkts_Object=MibTableColumn
edgePortRcvUcastPkts=_EdgePortRcvUcastPkts_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,7),_EdgePortRcvUcastPkts_Type())
edgePortRcvUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvUcastPkts.setStatus(_A)
_EdgePortRcvNUcastPkts_Type=Counter32
_EdgePortRcvNUcastPkts_Object=MibTableColumn
edgePortRcvNUcastPkts=_EdgePortRcvNUcastPkts_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,8),_EdgePortRcvNUcastPkts_Type())
edgePortRcvNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvNUcastPkts.setStatus(_A)
_EdgePortXmtUcastPkts_Type=Counter32
_EdgePortXmtUcastPkts_Object=MibTableColumn
edgePortXmtUcastPkts=_EdgePortXmtUcastPkts_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,9),_EdgePortXmtUcastPkts_Type())
edgePortXmtUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortXmtUcastPkts.setStatus(_A)
_EdgePortXmtNUcastPkts_Type=Counter32
_EdgePortXmtNUcastPkts_Object=MibTableColumn
edgePortXmtNUcastPkts=_EdgePortXmtNUcastPkts_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,10),_EdgePortXmtNUcastPkts_Type())
edgePortXmtNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortXmtNUcastPkts.setStatus(_A)
_EdgePortRcvSmplPktSize_Type=Gauge32
_EdgePortRcvSmplPktSize_Object=MibTableColumn
edgePortRcvSmplPktSize=_EdgePortRcvSmplPktSize_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,11),_EdgePortRcvSmplPktSize_Type())
edgePortRcvSmplPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvSmplPktSize.setStatus(_A)
_EdgePortXmtSmplPktSize_Type=Gauge32
_EdgePortXmtSmplPktSize_Object=MibTableColumn
edgePortXmtSmplPktSize=_EdgePortXmtSmplPktSize_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,12),_EdgePortXmtSmplPktSize_Type())
edgePortXmtSmplPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortXmtSmplPktSize.setStatus(_A)
_EdgePortRcvL3XsumErrs_Type=Counter32
_EdgePortRcvL3XsumErrs_Object=MibTableColumn
edgePortRcvL3XsumErrs=_EdgePortRcvL3XsumErrs_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,13),_EdgePortRcvL3XsumErrs_Type())
edgePortRcvL3XsumErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvL3XsumErrs.setStatus(_A)
_EdgePortRcvL3XsumErrLastVci_Type=Integer32
_EdgePortRcvL3XsumErrLastVci_Object=MibTableColumn
edgePortRcvL3XsumErrLastVci=_EdgePortRcvL3XsumErrLastVci_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,14),_EdgePortRcvL3XsumErrLastVci_Type())
edgePortRcvL3XsumErrLastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvL3XsumErrLastVci.setStatus(_A)
_EdgePortRcvCRCErrors_Type=Counter32
_EdgePortRcvCRCErrors_Object=MibTableColumn
edgePortRcvCRCErrors=_EdgePortRcvCRCErrors_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,15),_EdgePortRcvCRCErrors_Type())
edgePortRcvCRCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvCRCErrors.setStatus(_A)
_EdgePortRcvAborts_Type=Counter32
_EdgePortRcvAborts_Object=MibTableColumn
edgePortRcvAborts=_EdgePortRcvAborts_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,16),_EdgePortRcvAborts_Type())
edgePortRcvAborts.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvAborts.setStatus(_A)
_EdgePortXmtUnderflows_Type=Counter32
_EdgePortXmtUnderflows_Object=MibTableColumn
edgePortXmtUnderflows=_EdgePortXmtUnderflows_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,17),_EdgePortXmtUnderflows_Type())
edgePortXmtUnderflows.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortXmtUnderflows.setStatus(_A)
_EdgePortRcvShortFrames_Type=Counter32
_EdgePortRcvShortFrames_Object=MibTableColumn
edgePortRcvShortFrames=_EdgePortRcvShortFrames_Object((1,3,6,1,4,1,711,2,1,11,1,1,2,1,18),_EdgePortRcvShortFrames_Type())
edgePortRcvShortFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:edgePortRcvShortFrames.setStatus(_A)
_LsFrameRelayDlciStatTable_Object=MibTable
lsFrameRelayDlciStatTable=_LsFrameRelayDlciStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,1,3))
if mibBuilder.loadTexts:lsFrameRelayDlciStatTable.setStatus(_A)
_LsFrameRelayDlciStatEntry_Object=MibTableRow
lsFrameRelayDlciStatEntry=_LsFrameRelayDlciStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1))
lsFrameRelayDlciStatEntry.setIndexNames((0,_E,_An),(0,_E,_Ao))
if mibBuilder.loadTexts:lsFrameRelayDlciStatEntry.setStatus(_A)
_FrameRelayDlciStatPortIndex_Type=Integer32
_FrameRelayDlciStatPortIndex_Object=MibTableColumn
frameRelayDlciStatPortIndex=_FrameRelayDlciStatPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,1),_FrameRelayDlciStatPortIndex_Type())
frameRelayDlciStatPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciStatPortIndex.setStatus(_A)
_FrameRelayDlciStatDlciIndex_Type=Integer32
_FrameRelayDlciStatDlciIndex_Object=MibTableColumn
frameRelayDlciStatDlciIndex=_FrameRelayDlciStatDlciIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,2),_FrameRelayDlciStatDlciIndex_Type())
frameRelayDlciStatDlciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciStatDlciIndex.setStatus(_A)
_FrameRelayDlciToSwCLP0Frames_Type=Counter32
_FrameRelayDlciToSwCLP0Frames_Object=MibTableColumn
frameRelayDlciToSwCLP0Frames=_FrameRelayDlciToSwCLP0Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,3),_FrameRelayDlciToSwCLP0Frames_Type())
frameRelayDlciToSwCLP0Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciToSwCLP0Frames.setStatus(_A)
_FrameRelayDlciToSwCLP0Cells_Type=Counter32
_FrameRelayDlciToSwCLP0Cells_Object=MibTableColumn
frameRelayDlciToSwCLP0Cells=_FrameRelayDlciToSwCLP0Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,4),_FrameRelayDlciToSwCLP0Cells_Type())
frameRelayDlciToSwCLP0Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciToSwCLP0Cells.setStatus(_A)
_FrameRelayDlciToSwCLP1Frames_Type=Counter32
_FrameRelayDlciToSwCLP1Frames_Object=MibTableColumn
frameRelayDlciToSwCLP1Frames=_FrameRelayDlciToSwCLP1Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,5),_FrameRelayDlciToSwCLP1Frames_Type())
frameRelayDlciToSwCLP1Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciToSwCLP1Frames.setStatus(_A)
_FrameRelayDlciToSwCLP1Cells_Type=Counter32
_FrameRelayDlciToSwCLP1Cells_Object=MibTableColumn
frameRelayDlciToSwCLP1Cells=_FrameRelayDlciToSwCLP1Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,6),_FrameRelayDlciToSwCLP1Cells_Type())
frameRelayDlciToSwCLP1Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciToSwCLP1Cells.setStatus(_A)
_FrameRelayDlciToSwDiscardFrames_Type=Counter32
_FrameRelayDlciToSwDiscardFrames_Object=MibTableColumn
frameRelayDlciToSwDiscardFrames=_FrameRelayDlciToSwDiscardFrames_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,7),_FrameRelayDlciToSwDiscardFrames_Type())
frameRelayDlciToSwDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciToSwDiscardFrames.setStatus(_A)
_FrameRelayDlciToSwDiscardCells_Type=Counter32
_FrameRelayDlciToSwDiscardCells_Object=MibTableColumn
frameRelayDlciToSwDiscardCells=_FrameRelayDlciToSwDiscardCells_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,8),_FrameRelayDlciToSwDiscardCells_Type())
frameRelayDlciToSwDiscardCells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciToSwDiscardCells.setStatus(_A)
_FrameRelayDlciFrSwCLP0Frames_Type=Counter32
_FrameRelayDlciFrSwCLP0Frames_Object=MibTableColumn
frameRelayDlciFrSwCLP0Frames=_FrameRelayDlciFrSwCLP0Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,9),_FrameRelayDlciFrSwCLP0Frames_Type())
frameRelayDlciFrSwCLP0Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciFrSwCLP0Frames.setStatus(_A)
_FrameRelayDlciFrSwCLP0Cells_Type=Counter32
_FrameRelayDlciFrSwCLP0Cells_Object=MibTableColumn
frameRelayDlciFrSwCLP0Cells=_FrameRelayDlciFrSwCLP0Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,10),_FrameRelayDlciFrSwCLP0Cells_Type())
frameRelayDlciFrSwCLP0Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciFrSwCLP0Cells.setStatus(_A)
_FrameRelayDlciFrSwCLP1Frames_Type=Counter32
_FrameRelayDlciFrSwCLP1Frames_Object=MibTableColumn
frameRelayDlciFrSwCLP1Frames=_FrameRelayDlciFrSwCLP1Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,11),_FrameRelayDlciFrSwCLP1Frames_Type())
frameRelayDlciFrSwCLP1Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciFrSwCLP1Frames.setStatus(_A)
_FrameRelayDlciFrSwCLP1Cells_Type=Counter32
_FrameRelayDlciFrSwCLP1Cells_Object=MibTableColumn
frameRelayDlciFrSwCLP1Cells=_FrameRelayDlciFrSwCLP1Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,3,1,12),_FrameRelayDlciFrSwCLP1Cells_Type())
frameRelayDlciFrSwCLP1Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameRelayDlciFrSwCLP1Cells.setStatus(_A)
_LsEdgePortToSwMsgLenTable_Object=MibTable
lsEdgePortToSwMsgLenTable=_LsEdgePortToSwMsgLenTable_Object((1,3,6,1,4,1,711,2,1,11,1,1,4))
if mibBuilder.loadTexts:lsEdgePortToSwMsgLenTable.setStatus(_A)
_LsEdgePortToSwMsgLenEntry_Object=MibTableRow
lsEdgePortToSwMsgLenEntry=_LsEdgePortToSwMsgLenEntry_Object((1,3,6,1,4,1,711,2,1,11,1,1,4,1))
lsEdgePortToSwMsgLenEntry.setIndexNames((0,_E,_Ap),(0,_E,_Aq))
if mibBuilder.loadTexts:lsEdgePortToSwMsgLenEntry.setStatus(_A)
_EdgeToSwMsgLenPortIndex_Type=Integer32
_EdgeToSwMsgLenPortIndex_Object=MibTableColumn
edgeToSwMsgLenPortIndex=_EdgeToSwMsgLenPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,4,1,1),_EdgeToSwMsgLenPortIndex_Type())
edgeToSwMsgLenPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeToSwMsgLenPortIndex.setStatus(_A)
_EdgeToSwMsgLenBinIndex_Type=Integer32
_EdgeToSwMsgLenBinIndex_Object=MibTableColumn
edgeToSwMsgLenBinIndex=_EdgeToSwMsgLenBinIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,4,1,2),_EdgeToSwMsgLenBinIndex_Type())
edgeToSwMsgLenBinIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeToSwMsgLenBinIndex.setStatus(_A)
_EdgeToSwMsgLenMsgs_Type=Counter32
_EdgeToSwMsgLenMsgs_Object=MibTableColumn
edgeToSwMsgLenMsgs=_EdgeToSwMsgLenMsgs_Object((1,3,6,1,4,1,711,2,1,11,1,1,4,1,3),_EdgeToSwMsgLenMsgs_Type())
edgeToSwMsgLenMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeToSwMsgLenMsgs.setStatus(_A)
_LsEdgeSwToPortMsgLenTable_Object=MibTable
lsEdgeSwToPortMsgLenTable=_LsEdgeSwToPortMsgLenTable_Object((1,3,6,1,4,1,711,2,1,11,1,1,5))
if mibBuilder.loadTexts:lsEdgeSwToPortMsgLenTable.setStatus(_A)
_LsEdgeSwToPortMsgLenEntry_Object=MibTableRow
lsEdgeSwToPortMsgLenEntry=_LsEdgeSwToPortMsgLenEntry_Object((1,3,6,1,4,1,711,2,1,11,1,1,5,1))
lsEdgeSwToPortMsgLenEntry.setIndexNames((0,_E,_Ar),(0,_E,_As))
if mibBuilder.loadTexts:lsEdgeSwToPortMsgLenEntry.setStatus(_A)
_EdgeToPortMsgLenPortIndex_Type=Integer32
_EdgeToPortMsgLenPortIndex_Object=MibTableColumn
edgeToPortMsgLenPortIndex=_EdgeToPortMsgLenPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,5,1,1),_EdgeToPortMsgLenPortIndex_Type())
edgeToPortMsgLenPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeToPortMsgLenPortIndex.setStatus(_A)
_EdgeToPortMsgLenBinIndex_Type=Integer32
_EdgeToPortMsgLenBinIndex_Object=MibTableColumn
edgeToPortMsgLenBinIndex=_EdgeToPortMsgLenBinIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,5,1,2),_EdgeToPortMsgLenBinIndex_Type())
edgeToPortMsgLenBinIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeToPortMsgLenBinIndex.setStatus(_A)
_EdgeToPortMsgLenMsgs_Type=Counter32
_EdgeToPortMsgLenMsgs_Object=MibTableColumn
edgeToPortMsgLenMsgs=_EdgeToPortMsgLenMsgs_Object((1,3,6,1,4,1,711,2,1,11,1,1,5,1,3),_EdgeToPortMsgLenMsgs_Type())
edgeToPortMsgLenMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:edgeToPortMsgLenMsgs.setStatus(_A)
_LsEdgeCpuWorkloadTable_Object=MibTable
lsEdgeCpuWorkloadTable=_LsEdgeCpuWorkloadTable_Object((1,3,6,1,4,1,711,2,1,11,1,1,6))
if mibBuilder.loadTexts:lsEdgeCpuWorkloadTable.setStatus(_A)
_LsEdgeCpuWorkloadEntry_Object=MibTableRow
lsEdgeCpuWorkloadEntry=_LsEdgeCpuWorkloadEntry_Object((1,3,6,1,4,1,711,2,1,11,1,1,6,1))
lsEdgeCpuWorkloadEntry.setIndexNames((0,_E,_At),(0,_E,_Au))
if mibBuilder.loadTexts:lsEdgeCpuWorkloadEntry.setStatus(_A)
_LsEdgeWorkloadCardIndex_Type=Integer32
_LsEdgeWorkloadCardIndex_Object=MibTableColumn
lsEdgeWorkloadCardIndex=_LsEdgeWorkloadCardIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,6,1,1),_LsEdgeWorkloadCardIndex_Type())
lsEdgeWorkloadCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsEdgeWorkloadCardIndex.setStatus(_A)
_LsEdgeWorkloadTypeIndex_Type=Integer32
_LsEdgeWorkloadTypeIndex_Object=MibTableColumn
lsEdgeWorkloadTypeIndex=_LsEdgeWorkloadTypeIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,6,1,2),_LsEdgeWorkloadTypeIndex_Type())
lsEdgeWorkloadTypeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsEdgeWorkloadTypeIndex.setStatus(_A)
_LsEdgeWorkloadEvents_Type=Counter32
_LsEdgeWorkloadEvents_Object=MibTableColumn
lsEdgeWorkloadEvents=_LsEdgeWorkloadEvents_Object((1,3,6,1,4,1,711,2,1,11,1,1,6,1,3),_LsEdgeWorkloadEvents_Type())
lsEdgeWorkloadEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lsEdgeWorkloadEvents.setStatus(_A)
_LsFrameForwardStatTable_Object=MibTable
lsFrameForwardStatTable=_LsFrameForwardStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,1,7))
if mibBuilder.loadTexts:lsFrameForwardStatTable.setStatus(_A)
_LsFrameForwardStatEntry_Object=MibTableRow
lsFrameForwardStatEntry=_LsFrameForwardStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1))
lsFrameForwardStatEntry.setIndexNames((0,_E,_Av))
if mibBuilder.loadTexts:lsFrameForwardStatEntry.setStatus(_A)
_FrameForwardStatPortIndex_Type=Integer32
_FrameForwardStatPortIndex_Object=MibTableColumn
frameForwardStatPortIndex=_FrameForwardStatPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,1),_FrameForwardStatPortIndex_Type())
frameForwardStatPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardStatPortIndex.setStatus(_A)
_FrameForwardToSwCLP0Frames_Type=Counter32
_FrameForwardToSwCLP0Frames_Object=MibTableColumn
frameForwardToSwCLP0Frames=_FrameForwardToSwCLP0Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,2),_FrameForwardToSwCLP0Frames_Type())
frameForwardToSwCLP0Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardToSwCLP0Frames.setStatus(_A)
_FrameForwardToSwCLP0Cells_Type=Counter32
_FrameForwardToSwCLP0Cells_Object=MibTableColumn
frameForwardToSwCLP0Cells=_FrameForwardToSwCLP0Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,3),_FrameForwardToSwCLP0Cells_Type())
frameForwardToSwCLP0Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardToSwCLP0Cells.setStatus(_A)
_FrameForwardToSwCLP1Frames_Type=Counter32
_FrameForwardToSwCLP1Frames_Object=MibTableColumn
frameForwardToSwCLP1Frames=_FrameForwardToSwCLP1Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,4),_FrameForwardToSwCLP1Frames_Type())
frameForwardToSwCLP1Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardToSwCLP1Frames.setStatus(_A)
_FrameForwardToSwCLP1Cells_Type=Counter32
_FrameForwardToSwCLP1Cells_Object=MibTableColumn
frameForwardToSwCLP1Cells=_FrameForwardToSwCLP1Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,5),_FrameForwardToSwCLP1Cells_Type())
frameForwardToSwCLP1Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardToSwCLP1Cells.setStatus(_A)
_FrameForwardToSwDiscardFrames_Type=Counter32
_FrameForwardToSwDiscardFrames_Object=MibTableColumn
frameForwardToSwDiscardFrames=_FrameForwardToSwDiscardFrames_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,6),_FrameForwardToSwDiscardFrames_Type())
frameForwardToSwDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardToSwDiscardFrames.setStatus(_A)
_FrameForwardToSwDiscardCells_Type=Counter32
_FrameForwardToSwDiscardCells_Object=MibTableColumn
frameForwardToSwDiscardCells=_FrameForwardToSwDiscardCells_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,7),_FrameForwardToSwDiscardCells_Type())
frameForwardToSwDiscardCells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardToSwDiscardCells.setStatus(_A)
_FrameForwardFrSwCLP0Frames_Type=Counter32
_FrameForwardFrSwCLP0Frames_Object=MibTableColumn
frameForwardFrSwCLP0Frames=_FrameForwardFrSwCLP0Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,8),_FrameForwardFrSwCLP0Frames_Type())
frameForwardFrSwCLP0Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardFrSwCLP0Frames.setStatus(_A)
_FrameForwardFrSwCLP0Cells_Type=Counter32
_FrameForwardFrSwCLP0Cells_Object=MibTableColumn
frameForwardFrSwCLP0Cells=_FrameForwardFrSwCLP0Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,9),_FrameForwardFrSwCLP0Cells_Type())
frameForwardFrSwCLP0Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardFrSwCLP0Cells.setStatus(_A)
_FrameForwardFrSwCLP1Frames_Type=Counter32
_FrameForwardFrSwCLP1Frames_Object=MibTableColumn
frameForwardFrSwCLP1Frames=_FrameForwardFrSwCLP1Frames_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,10),_FrameForwardFrSwCLP1Frames_Type())
frameForwardFrSwCLP1Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardFrSwCLP1Frames.setStatus(_A)
_FrameForwardFrSwCLP1Cells_Type=Counter32
_FrameForwardFrSwCLP1Cells_Object=MibTableColumn
frameForwardFrSwCLP1Cells=_FrameForwardFrSwCLP1Cells_Object((1,3,6,1,4,1,711,2,1,11,1,1,7,1,11),_FrameForwardFrSwCLP1Cells_Type())
frameForwardFrSwCLP1Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:frameForwardFrSwCLP1Cells.setStatus(_A)
_LsTrunkStatistics_ObjectIdentity=ObjectIdentity
lsTrunkStatistics=_LsTrunkStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,11,1,2))
_LsTrunkPortStatTable_Object=MibTable
lsTrunkPortStatTable=_LsTrunkPortStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,2,1))
if mibBuilder.loadTexts:lsTrunkPortStatTable.setStatus(_A)
_LsTrunkPortStatEntry_Object=MibTableRow
lsTrunkPortStatEntry=_LsTrunkPortStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1))
lsTrunkPortStatEntry.setIndexNames((0,_E,_Aw))
if mibBuilder.loadTexts:lsTrunkPortStatEntry.setStatus(_A)
_TrunkPortStatIndex_Type=Integer32
_TrunkPortStatIndex_Object=MibTableColumn
trunkPortStatIndex=_TrunkPortStatIndex_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,1),_TrunkPortStatIndex_Type())
trunkPortStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortStatIndex.setStatus(_A)
_TrunkPortRcvCells_Type=Counter32
_TrunkPortRcvCells_Object=MibTableColumn
trunkPortRcvCells=_TrunkPortRcvCells_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,2),_TrunkPortRcvCells_Type())
trunkPortRcvCells.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortRcvCells.setStatus(_A)
_TrunkPortXmtCells_Type=Counter32
_TrunkPortXmtCells_Object=MibTableColumn
trunkPortXmtCells=_TrunkPortXmtCells_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,3),_TrunkPortXmtCells_Type())
trunkPortXmtCells.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortXmtCells.setStatus(_A)
_TrunkPortRcvRuns_Type=Counter32
_TrunkPortRcvRuns_Object=MibTableColumn
trunkPortRcvRuns=_TrunkPortRcvRuns_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,4),_TrunkPortRcvRuns_Type())
trunkPortRcvRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortRcvRuns.setStatus(_A)
_TrunkPortDownXmtCells_Type=Counter32
_TrunkPortDownXmtCells_Object=MibTableColumn
trunkPortDownXmtCells=_TrunkPortDownXmtCells_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,5),_TrunkPortDownXmtCells_Type())
trunkPortDownXmtCells.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortDownXmtCells.setStatus(_A)
_TrunkPortRcvCRCErrors_Type=Counter32
_TrunkPortRcvCRCErrors_Object=MibTableColumn
trunkPortRcvCRCErrors=_TrunkPortRcvCRCErrors_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,6),_TrunkPortRcvCRCErrors_Type())
trunkPortRcvCRCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortRcvCRCErrors.setStatus(_A)
_TrunkPortRcvAborts_Type=Counter32
_TrunkPortRcvAborts_Object=MibTableColumn
trunkPortRcvAborts=_TrunkPortRcvAborts_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,7),_TrunkPortRcvAborts_Type())
trunkPortRcvAborts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortRcvAborts.setStatus(_A)
_TrunkPortXmtUnderflows_Type=Counter32
_TrunkPortXmtUnderflows_Object=MibTableColumn
trunkPortXmtUnderflows=_TrunkPortXmtUnderflows_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,8),_TrunkPortXmtUnderflows_Type())
trunkPortXmtUnderflows.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortXmtUnderflows.setStatus(_A)
_TrunkPortRcvShortFrames_Type=Counter32
_TrunkPortRcvShortFrames_Object=MibTableColumn
trunkPortRcvShortFrames=_TrunkPortRcvShortFrames_Object((1,3,6,1,4,1,711,2,1,11,1,2,1,1,9),_TrunkPortRcvShortFrames_Type())
trunkPortRcvShortFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPortRcvShortFrames.setStatus(_A)
_LsTrunkCpuWorkloadTable_Object=MibTable
lsTrunkCpuWorkloadTable=_LsTrunkCpuWorkloadTable_Object((1,3,6,1,4,1,711,2,1,11,1,2,2))
if mibBuilder.loadTexts:lsTrunkCpuWorkloadTable.setStatus(_A)
_LsTrunkCpuWorkloadEntry_Object=MibTableRow
lsTrunkCpuWorkloadEntry=_LsTrunkCpuWorkloadEntry_Object((1,3,6,1,4,1,711,2,1,11,1,2,2,1))
lsTrunkCpuWorkloadEntry.setIndexNames((0,_E,_Ax),(0,_E,_Ay))
if mibBuilder.loadTexts:lsTrunkCpuWorkloadEntry.setStatus(_A)
_LsTrunkWorkloadCardIndex_Type=Integer32
_LsTrunkWorkloadCardIndex_Object=MibTableColumn
lsTrunkWorkloadCardIndex=_LsTrunkWorkloadCardIndex_Object((1,3,6,1,4,1,711,2,1,11,1,2,2,1,1),_LsTrunkWorkloadCardIndex_Type())
lsTrunkWorkloadCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsTrunkWorkloadCardIndex.setStatus(_A)
class _LsTrunkWorkloadTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('average',1))
_LsTrunkWorkloadTypeIndex_Type.__name__=_C
_LsTrunkWorkloadTypeIndex_Object=MibTableColumn
lsTrunkWorkloadTypeIndex=_LsTrunkWorkloadTypeIndex_Object((1,3,6,1,4,1,711,2,1,11,1,2,2,1,2),_LsTrunkWorkloadTypeIndex_Type())
lsTrunkWorkloadTypeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsTrunkWorkloadTypeIndex.setStatus(_A)
_LsTrunkWorkloadEvents_Type=Counter32
_LsTrunkWorkloadEvents_Object=MibTableColumn
lsTrunkWorkloadEvents=_LsTrunkWorkloadEvents_Object((1,3,6,1,4,1,711,2,1,11,1,2,2,1,3),_LsTrunkWorkloadEvents_Type())
lsTrunkWorkloadEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lsTrunkWorkloadEvents.setStatus(_A)
_LsLcStatistics_ObjectIdentity=ObjectIdentity
lsLcStatistics=_LsLcStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,11,1,3))
_LcStatTable_Object=MibTable
lcStatTable=_LcStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,3,1))
if mibBuilder.loadTexts:lcStatTable.setStatus(_A)
_LcStatEntry_Object=MibTableRow
lcStatEntry=_LcStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1))
lcStatEntry.setIndexNames((0,_E,_Az))
if mibBuilder.loadTexts:lcStatEntry.setStatus(_A)
_LcStatCardIndex_Type=Integer32
_LcStatCardIndex_Object=MibTableColumn
lcStatCardIndex=_LcStatCardIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,1),_LcStatCardIndex_Type())
lcStatCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcStatCardIndex.setStatus(_A)
_TsuFreeCells_Type=Gauge32
_TsuFreeCells_Object=MibTableColumn
tsuFreeCells=_TsuFreeCells_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,2),_TsuFreeCells_Type())
tsuFreeCells.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuFreeCells.setStatus(_A)
_FsuSharedFreeCells_Type=Integer32
_FsuSharedFreeCells_Object=MibTableColumn
fsuSharedFreeCells=_FsuSharedFreeCells_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,3),_FsuSharedFreeCells_Type())
fsuSharedFreeCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuSharedFreeCells.setStatus(_A)
_TsuCellDropLastVci_Type=Integer32
_TsuCellDropLastVci_Object=MibTableColumn
tsuCellDropLastVci=_TsuCellDropLastVci_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,4),_TsuCellDropLastVci_Type())
tsuCellDropLastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuCellDropLastVci.setStatus(_A)
_SwitchCellDgRejectEvents_Type=Counter32
_SwitchCellDgRejectEvents_Object=MibTableColumn
switchCellDgRejectEvents=_SwitchCellDgRejectEvents_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,5),_SwitchCellDgRejectEvents_Type())
switchCellDgRejectEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:switchCellDgRejectEvents.setStatus(_A)
_SwitchCellSchedRejectEvents_Type=Counter32
_SwitchCellSchedRejectEvents_Object=MibTableColumn
switchCellSchedRejectEvents=_SwitchCellSchedRejectEvents_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,6),_SwitchCellSchedRejectEvents_Type())
switchCellSchedRejectEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:switchCellSchedRejectEvents.setStatus(_A)
_TsuErrFutQCellDrops_Type=Counter32
_TsuErrFutQCellDrops_Object=MibTableColumn
tsuErrFutQCellDrops=_TsuErrFutQCellDrops_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,7),_TsuErrFutQCellDrops_Type())
tsuErrFutQCellDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuErrFutQCellDrops.setStatus(_A)
_TsuErrFutQMsgDropLastVci_Type=Integer32
_TsuErrFutQMsgDropLastVci_Object=MibTableColumn
tsuErrFutQMsgDropLastVci=_TsuErrFutQMsgDropLastVci_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,8),_TsuErrFutQMsgDropLastVci_Type())
tsuErrFutQMsgDropLastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuErrFutQMsgDropLastVci.setStatus(_A)
_FsuHdrLrcErrs_Type=Counter32
_FsuHdrLrcErrs_Object=MibTableColumn
fsuHdrLrcErrs=_FsuHdrLrcErrs_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,9),_FsuHdrLrcErrs_Type())
fsuHdrLrcErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuHdrLrcErrs.setStatus(_A)
_FsuPayloadLrcErrs_Type=Counter32
_FsuPayloadLrcErrs_Object=MibTableColumn
fsuPayloadLrcErrs=_FsuPayloadLrcErrs_Object((1,3,6,1,4,1,711,2,1,11,1,3,1,1,10),_FsuPayloadLrcErrs_Type())
fsuPayloadLrcErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuPayloadLrcErrs.setStatus(_A)
_LcPortStatTable_Object=MibTable
lcPortStatTable=_LcPortStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,3,2))
if mibBuilder.loadTexts:lcPortStatTable.setStatus(_A)
_LcPortStatEntry_Object=MibTableRow
lcPortStatEntry=_LcPortStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1))
lcPortStatEntry.setIndexNames((0,_E,_A_))
if mibBuilder.loadTexts:lcPortStatEntry.setStatus(_A)
_LcStatPortIndex_Type=Integer32
_LcStatPortIndex_Object=MibTableColumn
lcStatPortIndex=_LcStatPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,1),_LcStatPortIndex_Type())
lcStatPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcStatPortIndex.setStatus(_A)
_FsuPortFreeCells_Type=Gauge32
_FsuPortFreeCells_Object=MibTableColumn
fsuPortFreeCells=_FsuPortFreeCells_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,2),_FsuPortFreeCells_Type())
fsuPortFreeCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuPortFreeCells.setStatus(_A)
_FsuCellDropLastCellHdr_Type=Integer32
_FsuCellDropLastCellHdr_Object=MibTableColumn
fsuCellDropLastCellHdr=_FsuCellDropLastCellHdr_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,3),_FsuCellDropLastCellHdr_Type())
fsuCellDropLastCellHdr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuCellDropLastCellHdr.setStatus(_A)
_TsuPortErrL1UnconfigVcis_Type=Counter32
_TsuPortErrL1UnconfigVcis_Object=MibTableColumn
tsuPortErrL1UnconfigVcis=_TsuPortErrL1UnconfigVcis_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,4),_TsuPortErrL1UnconfigVcis_Type())
tsuPortErrL1UnconfigVcis.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuPortErrL1UnconfigVcis.setStatus(_A)
_TsuPortErrL2UnconfigVcis_Type=Counter32
_TsuPortErrL2UnconfigVcis_Object=MibTableColumn
tsuPortErrL2UnconfigVcis=_TsuPortErrL2UnconfigVcis_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,5),_TsuPortErrL2UnconfigVcis_Type())
tsuPortErrL2UnconfigVcis.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuPortErrL2UnconfigVcis.setStatus(_A)
_TsuPortErrL1UnconfigLastVci_Type=Integer32
_TsuPortErrL1UnconfigLastVci_Object=MibTableColumn
tsuPortErrL1UnconfigLastVci=_TsuPortErrL1UnconfigLastVci_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,6),_TsuPortErrL1UnconfigLastVci_Type())
tsuPortErrL1UnconfigLastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuPortErrL1UnconfigLastVci.setStatus(_A)
_TsuPortErrL2UnconfigLastVci_Type=Integer32
_TsuPortErrL2UnconfigLastVci_Object=MibTableColumn
tsuPortErrL2UnconfigLastVci=_TsuPortErrL2UnconfigLastVci_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,7),_TsuPortErrL2UnconfigLastVci_Type())
tsuPortErrL2UnconfigLastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuPortErrL2UnconfigLastVci.setStatus(_A)
_TsuPortErrNonZeroGfc_Type=Counter32
_TsuPortErrNonZeroGfc_Object=MibTableColumn
tsuPortErrNonZeroGfc=_TsuPortErrNonZeroGfc_Object((1,3,6,1,4,1,711,2,1,11,1,3,2,1,8),_TsuPortErrNonZeroGfc_Type())
tsuPortErrNonZeroGfc.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuPortErrNonZeroGfc.setStatus(_A)
_FsuPortXmtCellsTable_Object=MibTable
fsuPortXmtCellsTable=_FsuPortXmtCellsTable_Object((1,3,6,1,4,1,711,2,1,11,1,3,3))
if mibBuilder.loadTexts:fsuPortXmtCellsTable.setStatus(_A)
_FsuPortXmtCellsEntry_Object=MibTableRow
fsuPortXmtCellsEntry=_FsuPortXmtCellsEntry_Object((1,3,6,1,4,1,711,2,1,11,1,3,3,1))
fsuPortXmtCellsEntry.setIndexNames((0,_E,_B0),(0,_E,_B1))
if mibBuilder.loadTexts:fsuPortXmtCellsEntry.setStatus(_A)
_FsuXmtCellsPortIndex_Type=Integer32
_FsuXmtCellsPortIndex_Object=MibTableColumn
fsuXmtCellsPortIndex=_FsuXmtCellsPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,3,1,1),_FsuXmtCellsPortIndex_Type())
fsuXmtCellsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuXmtCellsPortIndex.setStatus(_A)
class _FsuXmtCellsPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FsuXmtCellsPriorityIndex_Type.__name__=_C
_FsuXmtCellsPriorityIndex_Object=MibTableColumn
fsuXmtCellsPriorityIndex=_FsuXmtCellsPriorityIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,3,1,2),_FsuXmtCellsPriorityIndex_Type())
fsuXmtCellsPriorityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuXmtCellsPriorityIndex.setStatus(_A)
_FsuXmtCellEvents_Type=Counter32
_FsuXmtCellEvents_Object=MibTableColumn
fsuXmtCellEvents=_FsuXmtCellEvents_Object((1,3,6,1,4,1,711,2,1,11,1,3,3,1,3),_FsuXmtCellEvents_Type())
fsuXmtCellEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuXmtCellEvents.setStatus(_A)
_FsuQueueCellLengthTable_Object=MibTable
fsuQueueCellLengthTable=_FsuQueueCellLengthTable_Object((1,3,6,1,4,1,711,2,1,11,1,3,4))
if mibBuilder.loadTexts:fsuQueueCellLengthTable.setStatus(_A)
_FsuQueueCellLenEntry_Object=MibTableRow
fsuQueueCellLenEntry=_FsuQueueCellLenEntry_Object((1,3,6,1,4,1,711,2,1,11,1,3,4,1))
fsuQueueCellLenEntry.setIndexNames((0,_E,_B2),(0,_E,_B3))
if mibBuilder.loadTexts:fsuQueueCellLenEntry.setStatus(_A)
_FsuQueueCellLenPortIndex_Type=Integer32
_FsuQueueCellLenPortIndex_Object=MibTableColumn
fsuQueueCellLenPortIndex=_FsuQueueCellLenPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,4,1,1),_FsuQueueCellLenPortIndex_Type())
fsuQueueCellLenPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuQueueCellLenPortIndex.setStatus(_A)
class _FsuQueueCellLenSubQIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_FsuQueueCellLenSubQIndex_Type.__name__=_C
_FsuQueueCellLenSubQIndex_Object=MibTableColumn
fsuQueueCellLenSubQIndex=_FsuQueueCellLenSubQIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,4,1,2),_FsuQueueCellLenSubQIndex_Type())
fsuQueueCellLenSubQIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuQueueCellLenSubQIndex.setStatus(_A)
_FsuQueueCellLength_Type=Gauge32
_FsuQueueCellLength_Object=MibTableColumn
fsuQueueCellLength=_FsuQueueCellLength_Object((1,3,6,1,4,1,711,2,1,11,1,3,4,1,3),_FsuQueueCellLength_Type())
fsuQueueCellLength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuQueueCellLength.setStatus(_A)
_FsuDropEventTable_Object=MibTable
fsuDropEventTable=_FsuDropEventTable_Object((1,3,6,1,4,1,711,2,1,11,1,3,5))
if mibBuilder.loadTexts:fsuDropEventTable.setStatus(_A)
_FsuDropEventEntry_Object=MibTableRow
fsuDropEventEntry=_FsuDropEventEntry_Object((1,3,6,1,4,1,711,2,1,11,1,3,5,1))
fsuDropEventEntry.setIndexNames((0,_E,_B4),(0,_E,_B5))
if mibBuilder.loadTexts:fsuDropEventEntry.setStatus(_A)
_FsuDropEventPortIndex_Type=Integer32
_FsuDropEventPortIndex_Object=MibTableColumn
fsuDropEventPortIndex=_FsuDropEventPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,5,1,1),_FsuDropEventPortIndex_Type())
fsuDropEventPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuDropEventPortIndex.setStatus(_A)
_FsuDropEventWatermarkIndex_Type=Integer32
_FsuDropEventWatermarkIndex_Object=MibTableColumn
fsuDropEventWatermarkIndex=_FsuDropEventWatermarkIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,5,1,2),_FsuDropEventWatermarkIndex_Type())
fsuDropEventWatermarkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuDropEventWatermarkIndex.setStatus(_A)
_FsuDropEvents_Type=Counter32
_FsuDropEvents_Object=MibTableColumn
fsuDropEvents=_FsuDropEvents_Object((1,3,6,1,4,1,711,2,1,11,1,3,5,1,3),_FsuDropEvents_Type())
fsuDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:fsuDropEvents.setStatus(_A)
_LsFsuFastDropTable_Object=MibTable
lsFsuFastDropTable=_LsFsuFastDropTable_Object((1,3,6,1,4,1,711,2,1,11,1,3,6))
if mibBuilder.loadTexts:lsFsuFastDropTable.setStatus(_A)
_LsFsuFastDropEntry_Object=MibTableRow
lsFsuFastDropEntry=_LsFsuFastDropEntry_Object((1,3,6,1,4,1,711,2,1,11,1,3,6,1))
lsFsuFastDropEntry.setIndexNames((0,_E,_B6))
if mibBuilder.loadTexts:lsFsuFastDropEntry.setStatus(_A)
class _LsFsuFastDropWatermarkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('clp1',1),('clp0HiPriority',2),('clp0HiOther',3)))
_LsFsuFastDropWatermarkIndex_Type.__name__=_C
_LsFsuFastDropWatermarkIndex_Object=MibTableColumn
lsFsuFastDropWatermarkIndex=_LsFsuFastDropWatermarkIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,6,1,1),_LsFsuFastDropWatermarkIndex_Type())
lsFsuFastDropWatermarkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsFsuFastDropWatermarkIndex.setStatus(_A)
_LsFsuFastCellDropEvents_Type=Counter32
_LsFsuFastCellDropEvents_Object=MibTableColumn
lsFsuFastCellDropEvents=_LsFsuFastCellDropEvents_Object((1,3,6,1,4,1,711,2,1,11,1,3,6,1,2),_LsFsuFastCellDropEvents_Type())
lsFsuFastCellDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lsFsuFastCellDropEvents.setStatus(_A)
_TsuDropEventTable_Object=MibTable
tsuDropEventTable=_TsuDropEventTable_Object((1,3,6,1,4,1,711,2,1,11,1,3,7))
if mibBuilder.loadTexts:tsuDropEventTable.setStatus(_A)
_TsuDropEventEntry_Object=MibTableRow
tsuDropEventEntry=_TsuDropEventEntry_Object((1,3,6,1,4,1,711,2,1,11,1,3,7,1))
tsuDropEventEntry.setIndexNames((0,_E,_B7),(0,_E,_B8))
if mibBuilder.loadTexts:tsuDropEventEntry.setStatus(_A)
_TsuDropEventPortIndex_Type=Integer32
_TsuDropEventPortIndex_Object=MibTableColumn
tsuDropEventPortIndex=_TsuDropEventPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,7,1,1),_TsuDropEventPortIndex_Type())
tsuDropEventPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuDropEventPortIndex.setStatus(_A)
class _TsuDropEventWatermarkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('control',2),('scheduled',3)))
_TsuDropEventWatermarkIndex_Type.__name__=_C
_TsuDropEventWatermarkIndex_Object=MibTableColumn
tsuDropEventWatermarkIndex=_TsuDropEventWatermarkIndex_Object((1,3,6,1,4,1,711,2,1,11,1,3,7,1,2),_TsuDropEventWatermarkIndex_Type())
tsuDropEventWatermarkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuDropEventWatermarkIndex.setStatus(_A)
_TsuDropEvents_Type=Counter32
_TsuDropEvents_Object=MibTableColumn
tsuDropEvents=_TsuDropEvents_Object((1,3,6,1,4,1,711,2,1,11,1,3,7,1,3),_TsuDropEvents_Type())
tsuDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tsuDropEvents.setStatus(_A)
_LsUtStatistics_ObjectIdentity=ObjectIdentity
lsUtStatistics=_LsUtStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,11,1,4))
_LsLcFsuIntervalTable_Object=MibTable
lsLcFsuIntervalTable=_LsLcFsuIntervalTable_Object((1,3,6,1,4,1,711,2,1,11,1,4,1))
if mibBuilder.loadTexts:lsLcFsuIntervalTable.setStatus(_A)
_LsLcFsuIntervalEntry_Object=MibTableRow
lsLcFsuIntervalEntry=_LsLcFsuIntervalEntry_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1))
lsLcFsuIntervalEntry.setIndexNames((0,_E,_B9),(0,_E,_BA))
if mibBuilder.loadTexts:lsLcFsuIntervalEntry.setStatus(_A)
_LsLcIntervalPortIndex_Type=Integer32
_LsLcIntervalPortIndex_Object=MibTableColumn
lsLcIntervalPortIndex=_LsLcIntervalPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,1),_LsLcIntervalPortIndex_Type())
lsLcIntervalPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalPortIndex.setStatus(_A)
class _LsLcIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_LsLcIntervalNumber_Type.__name__=_C
_LsLcIntervalNumber_Object=MibTableColumn
lsLcIntervalNumber=_LsLcIntervalNumber_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,2),_LsLcIntervalNumber_Type())
lsLcIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalNumber.setStatus(_A)
_LsLcIntervalPSDepth_Type=Integer32
_LsLcIntervalPSDepth_Object=MibTableColumn
lsLcIntervalPSDepth=_LsLcIntervalPSDepth_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,3),_LsLcIntervalPSDepth_Type())
lsLcIntervalPSDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalPSDepth.setStatus(_A)
_LsLcIntervalASDepth_Type=Integer32
_LsLcIntervalASDepth_Object=MibTableColumn
lsLcIntervalASDepth=_LsLcIntervalASDepth_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,4),_LsLcIntervalASDepth_Type())
lsLcIntervalASDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalASDepth.setStatus(_A)
_LsLcIntervalDropEvents_Type=Integer32
_LsLcIntervalDropEvents_Object=MibTableColumn
lsLcIntervalDropEvents=_LsLcIntervalDropEvents_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,5),_LsLcIntervalDropEvents_Type())
lsLcIntervalDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalDropEvents.setStatus(_A)
_LsLcIntervalAvgCells_Type=Integer32
_LsLcIntervalAvgCells_Object=MibTableColumn
lsLcIntervalAvgCells=_LsLcIntervalAvgCells_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,6),_LsLcIntervalAvgCells_Type())
lsLcIntervalAvgCells.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalAvgCells.setStatus(_A)
_LsLcIntervalPeakCells_Type=Integer32
_LsLcIntervalPeakCells_Object=MibTableColumn
lsLcIntervalPeakCells=_LsLcIntervalPeakCells_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,7),_LsLcIntervalPeakCells_Type())
lsLcIntervalPeakCells.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalPeakCells.setStatus(_A)
_LsLcIntervalMinPermits_Type=Integer32
_LsLcIntervalMinPermits_Object=MibTableColumn
lsLcIntervalMinPermits=_LsLcIntervalMinPermits_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,8),_LsLcIntervalMinPermits_Type())
lsLcIntervalMinPermits.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalMinPermits.setStatus(_A)
_LsLcIntervalAvgPermits_Type=Integer32
_LsLcIntervalAvgPermits_Object=MibTableColumn
lsLcIntervalAvgPermits=_LsLcIntervalAvgPermits_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,9),_LsLcIntervalAvgPermits_Type())
lsLcIntervalAvgPermits.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalAvgPermits.setStatus(_A)
_LsLcIntervalMaxPermits_Type=Integer32
_LsLcIntervalMaxPermits_Object=MibTableColumn
lsLcIntervalMaxPermits=_LsLcIntervalMaxPermits_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,10),_LsLcIntervalMaxPermits_Type())
lsLcIntervalMaxPermits.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalMaxPermits.setStatus(_A)
_LsLcIntervalDecrPermits_Type=Integer32
_LsLcIntervalDecrPermits_Object=MibTableColumn
lsLcIntervalDecrPermits=_LsLcIntervalDecrPermits_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,11),_LsLcIntervalDecrPermits_Type())
lsLcIntervalDecrPermits.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalDecrPermits.setStatus(_A)
_LsLcIntervalIncrPermits_Type=Integer32
_LsLcIntervalIncrPermits_Object=MibTableColumn
lsLcIntervalIncrPermits=_LsLcIntervalIncrPermits_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,12),_LsLcIntervalIncrPermits_Type())
lsLcIntervalIncrPermits.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalIncrPermits.setStatus(_A)
_LsLcIntervalMinBwAlloc_Type=Integer32
_LsLcIntervalMinBwAlloc_Object=MibTableColumn
lsLcIntervalMinBwAlloc=_LsLcIntervalMinBwAlloc_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,13),_LsLcIntervalMinBwAlloc_Type())
lsLcIntervalMinBwAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalMinBwAlloc.setStatus(_A)
_LsLcIntervalAvgBwAlloc_Type=Integer32
_LsLcIntervalAvgBwAlloc_Object=MibTableColumn
lsLcIntervalAvgBwAlloc=_LsLcIntervalAvgBwAlloc_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,14),_LsLcIntervalAvgBwAlloc_Type())
lsLcIntervalAvgBwAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalAvgBwAlloc.setStatus(_A)
_LsLcIntervalMaxBwAlloc_Type=Integer32
_LsLcIntervalMaxBwAlloc_Object=MibTableColumn
lsLcIntervalMaxBwAlloc=_LsLcIntervalMaxBwAlloc_Object((1,3,6,1,4,1,711,2,1,11,1,4,1,1,15),_LsLcIntervalMaxBwAlloc_Type())
lsLcIntervalMaxBwAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:lsLcIntervalMaxBwAlloc.setStatus(_A)
_LsNpStatistics_ObjectIdentity=ObjectIdentity
lsNpStatistics=_LsNpStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,11,1,5))
_LsNpCpuWorkloadTable_Object=MibTable
lsNpCpuWorkloadTable=_LsNpCpuWorkloadTable_Object((1,3,6,1,4,1,711,2,1,11,1,5,1))
if mibBuilder.loadTexts:lsNpCpuWorkloadTable.setStatus(_A)
_LsNpCpuWorkloadEntry_Object=MibTableRow
lsNpCpuWorkloadEntry=_LsNpCpuWorkloadEntry_Object((1,3,6,1,4,1,711,2,1,11,1,5,1,1))
lsNpCpuWorkloadEntry.setIndexNames((0,_E,_BB))
if mibBuilder.loadTexts:lsNpCpuWorkloadEntry.setStatus(_A)
_LsNpCpuWorkloadIndex_Type=Integer32
_LsNpCpuWorkloadIndex_Object=MibTableColumn
lsNpCpuWorkloadIndex=_LsNpCpuWorkloadIndex_Object((1,3,6,1,4,1,711,2,1,11,1,5,1,1,1),_LsNpCpuWorkloadIndex_Type())
lsNpCpuWorkloadIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsNpCpuWorkloadIndex.setStatus(_A)
_LsNpCpuWorkloadEvents_Type=Counter32
_LsNpCpuWorkloadEvents_Object=MibTableColumn
lsNpCpuWorkloadEvents=_LsNpCpuWorkloadEvents_Object((1,3,6,1,4,1,711,2,1,11,1,5,1,1,2),_LsNpCpuWorkloadEvents_Type())
lsNpCpuWorkloadEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lsNpCpuWorkloadEvents.setStatus(_A)
_LsCellStatistics_ObjectIdentity=ObjectIdentity
lsCellStatistics=_LsCellStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,11,1,6))
_LsCellVciStatTable_Object=MibTable
lsCellVciStatTable=_LsCellVciStatTable_Object((1,3,6,1,4,1,711,2,1,11,1,6,1))
if mibBuilder.loadTexts:lsCellVciStatTable.setStatus(_A)
_LsCellVciStatEntry_Object=MibTableRow
lsCellVciStatEntry=_LsCellVciStatEntry_Object((1,3,6,1,4,1,711,2,1,11,1,6,1,1))
lsCellVciStatEntry.setIndexNames((0,_E,_BC),(0,_E,_BD))
if mibBuilder.loadTexts:lsCellVciStatEntry.setStatus(_A)
_CellVciStatPortIndex_Type=Integer32
_CellVciStatPortIndex_Object=MibTableColumn
cellVciStatPortIndex=_CellVciStatPortIndex_Object((1,3,6,1,4,1,711,2,1,11,1,6,1,1,1),_CellVciStatPortIndex_Type())
cellVciStatPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cellVciStatPortIndex.setStatus(_A)
_CellVciStatVciIndex_Type=Integer32
_CellVciStatVciIndex_Object=MibTableColumn
cellVciStatVciIndex=_CellVciStatVciIndex_Object((1,3,6,1,4,1,711,2,1,11,1,6,1,1,2),_CellVciStatVciIndex_Type())
cellVciStatVciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cellVciStatVciIndex.setStatus(_A)
_CellVciToSwCLP0Cells_Type=Counter32
_CellVciToSwCLP0Cells_Object=MibTableColumn
cellVciToSwCLP0Cells=_CellVciToSwCLP0Cells_Object((1,3,6,1,4,1,711,2,1,11,1,6,1,1,3),_CellVciToSwCLP0Cells_Type())
cellVciToSwCLP0Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:cellVciToSwCLP0Cells.setStatus(_A)
_CellVciToSwCLP01Cells_Type=Counter32
_CellVciToSwCLP01Cells_Object=MibTableColumn
cellVciToSwCLP01Cells=_CellVciToSwCLP01Cells_Object((1,3,6,1,4,1,711,2,1,11,1,6,1,1,4),_CellVciToSwCLP01Cells_Type())
cellVciToSwCLP01Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:cellVciToSwCLP01Cells.setStatus(_A)
_CellVciToSwCLP1Cells_Type=Counter32
_CellVciToSwCLP1Cells_Object=MibTableColumn
cellVciToSwCLP1Cells=_CellVciToSwCLP1Cells_Object((1,3,6,1,4,1,711,2,1,11,1,6,1,1,5),_CellVciToSwCLP1Cells_Type())
cellVciToSwCLP1Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:cellVciToSwCLP1Cells.setStatus(_A)
_CellVciToSwDiscardCells_Type=Counter32
_CellVciToSwDiscardCells_Object=MibTableColumn
cellVciToSwDiscardCells=_CellVciToSwDiscardCells_Object((1,3,6,1,4,1,711,2,1,11,1,6,1,1,6),_CellVciToSwDiscardCells_Type())
cellVciToSwDiscardCells.setMaxAccess(_B)
if mibBuilder.loadTexts:cellVciToSwDiscardCells.setStatus(_A)
_LsIR_ObjectIdentity=ObjectIdentity
lsIR=_LsIR_ObjectIdentity((1,3,6,1,4,1,711,2,1,12))
_IrRoutingGroup_ObjectIdentity=ObjectIdentity
irRoutingGroup=_IrRoutingGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,12,1))
_IrRoutingPathsGenerated_Type=Counter32
_IrRoutingPathsGenerated_Object=MibScalar
irRoutingPathsGenerated=_IrRoutingPathsGenerated_Object((1,3,6,1,4,1,711,2,1,12,1,1),_IrRoutingPathsGenerated_Type())
irRoutingPathsGenerated.setMaxAccess(_B)
if mibBuilder.loadTexts:irRoutingPathsGenerated.setStatus(_A)
_IrRoutingPathGenSuccess_Type=Counter32
_IrRoutingPathGenSuccess_Object=MibScalar
irRoutingPathGenSuccess=_IrRoutingPathGenSuccess_Object((1,3,6,1,4,1,711,2,1,12,1,2),_IrRoutingPathGenSuccess_Type())
irRoutingPathGenSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:irRoutingPathGenSuccess.setStatus(_A)
_IrRoutingPathGenFailedNoResources_Type=Counter32
_IrRoutingPathGenFailedNoResources_Object=MibScalar
irRoutingPathGenFailedNoResources=_IrRoutingPathGenFailedNoResources_Object((1,3,6,1,4,1,711,2,1,12,1,3),_IrRoutingPathGenFailedNoResources_Type())
irRoutingPathGenFailedNoResources.setMaxAccess(_B)
if mibBuilder.loadTexts:irRoutingPathGenFailedNoResources.setStatus(_A)
_IrRoutingPathGenFailedUnknown_Type=Counter32
_IrRoutingPathGenFailedUnknown_Object=MibScalar
irRoutingPathGenFailedUnknown=_IrRoutingPathGenFailedUnknown_Object((1,3,6,1,4,1,711,2,1,12,1,4),_IrRoutingPathGenFailedUnknown_Type())
irRoutingPathGenFailedUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:irRoutingPathGenFailedUnknown.setStatus(_A)
_IrRoutingPathGenFailedOther_Type=Counter32
_IrRoutingPathGenFailedOther_Object=MibScalar
irRoutingPathGenFailedOther=_IrRoutingPathGenFailedOther_Object((1,3,6,1,4,1,711,2,1,12,1,5),_IrRoutingPathGenFailedOther_Type())
irRoutingPathGenFailedOther.setMaxAccess(_B)
if mibBuilder.loadTexts:irRoutingPathGenFailedOther.setStatus(_A)
_IrRoutingAveragePathLength_Type=Counter32
_IrRoutingAveragePathLength_Object=MibScalar
irRoutingAveragePathLength=_IrRoutingAveragePathLength_Object((1,3,6,1,4,1,711,2,1,12,1,6),_IrRoutingAveragePathLength_Type())
irRoutingAveragePathLength.setMaxAccess(_B)
if mibBuilder.loadTexts:irRoutingAveragePathLength.setStatus(_A)
_LsStatistics_ObjectIdentity=ObjectIdentity
lsStatistics=_LsStatistics_ObjectIdentity((1,3,6,1,4,1,711,2,1,13))
_TcsInfo_ObjectIdentity=ObjectIdentity
tcsInfo=_TcsInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,14))
_TcsTable_Object=MibTable
tcsTable=_TcsTable_Object((1,3,6,1,4,1,711,2,1,14,1))
if mibBuilder.loadTexts:tcsTable.setStatus(_A)
_TcsEntry_Object=MibTableRow
tcsEntry=_TcsEntry_Object((1,3,6,1,4,1,711,2,1,14,1,1))
tcsEntry.setIndexNames((0,_E,'tcsIndex'))
if mibBuilder.loadTexts:tcsEntry.setStatus(_A)
_TcsIndex_Type=Integer32
_TcsIndex_Object=MibTableColumn
tcsIndex=_TcsIndex_Object((1,3,6,1,4,1,711,2,1,14,1,1,1),_TcsIndex_Type())
tcsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsIndex.setStatus(_A)
_TcsTemp1_Type=Integer32
_TcsTemp1_Object=MibTableColumn
tcsTemp1=_TcsTemp1_Object((1,3,6,1,4,1,711,2,1,14,1,1,2),_TcsTemp1_Type())
tcsTemp1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsTemp1.setStatus(_A)
_TcsTemp2_Type=Integer32
_TcsTemp2_Object=MibTableColumn
tcsTemp2=_TcsTemp2_Object((1,3,6,1,4,1,711,2,1,14,1,1,3),_TcsTemp2_Type())
tcsTemp2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsTemp2.setStatus(_A)
_TcsTcsVoltage_Type=Integer32
_TcsTcsVoltage_Object=MibTableColumn
tcsTcsVoltage=_TcsTcsVoltage_Object((1,3,6,1,4,1,711,2,1,14,1,1,4),_TcsTcsVoltage_Type())
tcsTcsVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsTcsVoltage.setStatus(_A)
_TcsVccVoltage_Type=Integer32
_TcsVccVoltage_Object=MibTableColumn
tcsVccVoltage=_TcsVccVoltage_Object((1,3,6,1,4,1,711,2,1,14,1,1,5),_TcsVccVoltage_Type())
tcsVccVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsVccVoltage.setStatus(_A)
_TcsScsiVoltage_Type=Integer32
_TcsScsiVoltage_Object=MibTableColumn
tcsScsiVoltage=_TcsScsiVoltage_Object((1,3,6,1,4,1,711,2,1,14,1,1,7),_TcsScsiVoltage_Type())
tcsScsiVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsScsiVoltage.setStatus(_A)
class _TcsPostResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TcsPostResult_Type.__name__=_R
_TcsPostResult_Object=MibTableColumn
tcsPostResult=_TcsPostResult_Object((1,3,6,1,4,1,711,2,1,14,1,1,8),_TcsPostResult_Type())
tcsPostResult.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPostResult.setStatus(_A)
class _TcsCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10,11,12,13,14,15,30,31,32,33,34,35,36,37,70)));namedValues=NamedValues(*((_N,1),('error',2),(_F,3),(_q,4),('np',5),(_r,6),(_s,7),(_t,8),(_u,10),(_v,11),(_w,12),(_x,13),(_y,14),(_z,15),('clc1Gen',30),(_A0,31),(_A1,32),(_A2,33),(_A3,34),(_A4,35),(_A5,36),(_A6,37),('switch2',70)))
_TcsCardType_Type.__name__=_C
_TcsCardType_Object=MibTableColumn
tcsCardType=_TcsCardType_Object((1,3,6,1,4,1,711,2,1,14,1,1,9),_TcsCardType_Type())
tcsCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsCardType.setStatus(_A)
_TcsPaddleTemp1_Type=Integer32
_TcsPaddleTemp1_Object=MibTableColumn
tcsPaddleTemp1=_TcsPaddleTemp1_Object((1,3,6,1,4,1,711,2,1,14,1,1,10),_TcsPaddleTemp1_Type())
tcsPaddleTemp1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPaddleTemp1.setStatus(_A)
_TcsPaddleTemp2_Type=Integer32
_TcsPaddleTemp2_Object=MibTableColumn
tcsPaddleTemp2=_TcsPaddleTemp2_Object((1,3,6,1,4,1,711,2,1,14,1,1,11),_TcsPaddleTemp2_Type())
tcsPaddleTemp2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPaddleTemp2.setStatus(_A)
_TcsPaddleWarnTemp1_Type=Integer32
_TcsPaddleWarnTemp1_Object=MibTableColumn
tcsPaddleWarnTemp1=_TcsPaddleWarnTemp1_Object((1,3,6,1,4,1,711,2,1,14,1,1,12),_TcsPaddleWarnTemp1_Type())
tcsPaddleWarnTemp1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPaddleWarnTemp1.setStatus(_A)
_TcsPaddleWarnTemp2_Type=Integer32
_TcsPaddleWarnTemp2_Object=MibTableColumn
tcsPaddleWarnTemp2=_TcsPaddleWarnTemp2_Object((1,3,6,1,4,1,711,2,1,14,1,1,13),_TcsPaddleWarnTemp2_Type())
tcsPaddleWarnTemp2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPaddleWarnTemp2.setStatus(_A)
_TcsPaddleShutdownTemp1_Type=Integer32
_TcsPaddleShutdownTemp1_Object=MibTableColumn
tcsPaddleShutdownTemp1=_TcsPaddleShutdownTemp1_Object((1,3,6,1,4,1,711,2,1,14,1,1,14),_TcsPaddleShutdownTemp1_Type())
tcsPaddleShutdownTemp1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPaddleShutdownTemp1.setStatus(_A)
_TcsPaddleShutdownTemp2_Type=Integer32
_TcsPaddleShutdownTemp2_Object=MibTableColumn
tcsPaddleShutdownTemp2=_TcsPaddleShutdownTemp2_Object((1,3,6,1,4,1,711,2,1,14,1,1,15),_TcsPaddleShutdownTemp2_Type())
tcsPaddleShutdownTemp2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPaddleShutdownTemp2.setStatus(_A)
_TcsWarnTemp1_Type=Integer32
_TcsWarnTemp1_Object=MibTableColumn
tcsWarnTemp1=_TcsWarnTemp1_Object((1,3,6,1,4,1,711,2,1,14,1,1,16),_TcsWarnTemp1_Type())
tcsWarnTemp1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsWarnTemp1.setStatus(_A)
_TcsWarnTemp2_Type=Integer32
_TcsWarnTemp2_Object=MibTableColumn
tcsWarnTemp2=_TcsWarnTemp2_Object((1,3,6,1,4,1,711,2,1,14,1,1,17),_TcsWarnTemp2_Type())
tcsWarnTemp2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsWarnTemp2.setStatus(_A)
_TcsShutdownTemp1_Type=Integer32
_TcsShutdownTemp1_Object=MibTableColumn
tcsShutdownTemp1=_TcsShutdownTemp1_Object((1,3,6,1,4,1,711,2,1,14,1,1,18),_TcsShutdownTemp1_Type())
tcsShutdownTemp1.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsShutdownTemp1.setStatus(_A)
_TcsShutdownTemp2_Type=Integer32
_TcsShutdownTemp2_Object=MibTableColumn
tcsShutdownTemp2=_TcsShutdownTemp2_Object((1,3,6,1,4,1,711,2,1,14,1,1,19),_TcsShutdownTemp2_Type())
tcsShutdownTemp2.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsShutdownTemp2.setStatus(_A)
class _TcsFaultLight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_h,2)))
_TcsFaultLight_Type.__name__=_C
_TcsFaultLight_Object=MibTableColumn
tcsFaultLight=_TcsFaultLight_Object((1,3,6,1,4,1,711,2,1,14,1,1,20),_TcsFaultLight_Type())
tcsFaultLight.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsFaultLight.setStatus(_A)
class _TcsReadyLight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_h,2)))
_TcsReadyLight_Type.__name__=_C
_TcsReadyLight_Object=MibTableColumn
tcsReadyLight=_TcsReadyLight_Object((1,3,6,1,4,1,711,2,1,14,1,1,21),_TcsReadyLight_Type())
tcsReadyLight.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsReadyLight.setStatus(_A)
_TcsSwitchConnectivityMask_Type=Integer32
_TcsSwitchConnectivityMask_Object=MibTableColumn
tcsSwitchConnectivityMask=_TcsSwitchConnectivityMask_Object((1,3,6,1,4,1,711,2,1,14,1,1,22),_TcsSwitchConnectivityMask_Type())
tcsSwitchConnectivityMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsSwitchConnectivityMask.setStatus(_A)
class _TcsPrimarySwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switchA',1),('switchB',2)))
_TcsPrimarySwitch_Type.__name__=_C
_TcsPrimarySwitch_Object=MibScalar
tcsPrimarySwitch=_TcsPrimarySwitch_Object((1,3,6,1,4,1,711,2,1,14,2),_TcsPrimarySwitch_Type())
tcsPrimarySwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:tcsPrimarySwitch.setStatus(_A)
class _TcsPowerSupplyA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('failed',2),('good',3)))
_TcsPowerSupplyA_Type.__name__=_C
_TcsPowerSupplyA_Object=MibScalar
tcsPowerSupplyA=_TcsPowerSupplyA_Object((1,3,6,1,4,1,711,2,1,14,3),_TcsPowerSupplyA_Type())
tcsPowerSupplyA.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPowerSupplyA.setStatus(_A)
class _TcsPowerSupplyB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('failed',2),('good',3)))
_TcsPowerSupplyB_Type.__name__=_C
_TcsPowerSupplyB_Object=MibScalar
tcsPowerSupplyB=_TcsPowerSupplyB_Object((1,3,6,1,4,1,711,2,1,14,4),_TcsPowerSupplyB_Type())
tcsPowerSupplyB.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPowerSupplyB.setStatus(_A)
class _TcsPowerSupplyTypeA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_BE,2),('toddPS',3),(_F,4)))
_TcsPowerSupplyTypeA_Type.__name__=_C
_TcsPowerSupplyTypeA_Object=MibScalar
tcsPowerSupplyTypeA=_TcsPowerSupplyTypeA_Object((1,3,6,1,4,1,711,2,1,14,5),_TcsPowerSupplyTypeA_Type())
tcsPowerSupplyTypeA.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPowerSupplyTypeA.setStatus(_A)
class _TcsPowerSupplyTypeB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_BE,2),('toddPS',3),(_F,4)))
_TcsPowerSupplyTypeB_Type.__name__=_C
_TcsPowerSupplyTypeB_Object=MibScalar
tcsPowerSupplyTypeB=_TcsPowerSupplyTypeB_Object((1,3,6,1,4,1,711,2,1,14,6),_TcsPowerSupplyTypeB_Type())
tcsPowerSupplyTypeB.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsPowerSupplyTypeB.setStatus(_A)
_TcsSwitchFaultMaskA_Type=Integer32
_TcsSwitchFaultMaskA_Object=MibScalar
tcsSwitchFaultMaskA=_TcsSwitchFaultMaskA_Object((1,3,6,1,4,1,711,2,1,14,7),_TcsSwitchFaultMaskA_Type())
tcsSwitchFaultMaskA.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsSwitchFaultMaskA.setStatus(_A)
_TcsSwitchFaultMaskB_Type=Integer32
_TcsSwitchFaultMaskB_Object=MibScalar
tcsSwitchFaultMaskB=_TcsSwitchFaultMaskB_Object((1,3,6,1,4,1,711,2,1,14,8),_TcsSwitchFaultMaskB_Type())
tcsSwitchFaultMaskB.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsSwitchFaultMaskB.setStatus(_A)
class _TcsSwitchCutoverSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('willDoLossLess',1),('wontDoLossLess',2),('cantDoLossLess',3)))
_TcsSwitchCutoverSupport_Type.__name__=_C
_TcsSwitchCutoverSupport_Object=MibScalar
tcsSwitchCutoverSupport=_TcsSwitchCutoverSupport_Object((1,3,6,1,4,1,711,2,1,14,9),_TcsSwitchCutoverSupport_Type())
tcsSwitchCutoverSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsSwitchCutoverSupport.setStatus(_A)
_TcsFCPrimarySwitchA_Type=Integer32
_TcsFCPrimarySwitchA_Object=MibScalar
tcsFCPrimarySwitchA=_TcsFCPrimarySwitchA_Object((1,3,6,1,4,1,711,2,1,14,10),_TcsFCPrimarySwitchA_Type())
tcsFCPrimarySwitchA.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsFCPrimarySwitchA.setStatus(_A)
_TcsFCPrimarySwitchB_Type=Integer32
_TcsFCPrimarySwitchB_Object=MibScalar
tcsFCPrimarySwitchB=_TcsFCPrimarySwitchB_Object((1,3,6,1,4,1,711,2,1,14,11),_TcsFCPrimarySwitchB_Type())
tcsFCPrimarySwitchB.setMaxAccess(_B)
if mibBuilder.loadTexts:tcsFCPrimarySwitchB.setStatus(_A)
_LsGID_ObjectIdentity=ObjectIdentity
lsGID=_LsGID_ObjectIdentity((1,3,6,1,4,1,711,2,1,15))
_GidGeneralGroup_ObjectIdentity=ObjectIdentity
gidGeneralGroup=_GidGeneralGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,1))
_GidSoftwareVersionNumber_Type=DisplayString
_GidSoftwareVersionNumber_Object=MibScalar
gidSoftwareVersionNumber=_GidSoftwareVersionNumber_Object((1,3,6,1,4,1,711,2,1,15,1,1),_GidSoftwareVersionNumber_Type())
gidSoftwareVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:gidSoftwareVersionNumber.setStatus(_A)
_GidProcessID_Type=Integer32
_GidProcessID_Object=MibScalar
gidProcessID=_GidProcessID_Object((1,3,6,1,4,1,711,2,1,15,1,2),_GidProcessID_Type())
gidProcessID.setMaxAccess(_B)
if mibBuilder.loadTexts:gidProcessID.setStatus(_A)
_GidUpTime_Type=Integer32
_GidUpTime_Object=MibScalar
gidUpTime=_GidUpTime_Object((1,3,6,1,4,1,711,2,1,15,1,3),_GidUpTime_Type())
gidUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gidUpTime.setStatus(_A)
_GidMemoryUse_Type=Counter32
_GidMemoryUse_Object=MibScalar
gidMemoryUse=_GidMemoryUse_Object((1,3,6,1,4,1,711,2,1,15,1,4),_GidMemoryUse_Type())
gidMemoryUse.setMaxAccess(_B)
if mibBuilder.loadTexts:gidMemoryUse.setStatus(_A)
_GidTimersProcessed_Type=Counter32
_GidTimersProcessed_Object=MibScalar
gidTimersProcessed=_GidTimersProcessed_Object((1,3,6,1,4,1,711,2,1,15,1,5),_GidTimersProcessed_Type())
gidTimersProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:gidTimersProcessed.setStatus(_A)
_GidMallocFailures_Type=Counter32
_GidMallocFailures_Object=MibScalar
gidMallocFailures=_GidMallocFailures_Object((1,3,6,1,4,1,711,2,1,15,1,6),_GidMallocFailures_Type())
gidMallocFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:gidMallocFailures.setStatus(_A)
_GidDebugFlag_Type=Integer32
_GidDebugFlag_Object=MibScalar
gidDebugFlag=_GidDebugFlag_Object((1,3,6,1,4,1,711,2,1,15,1,7),_GidDebugFlag_Type())
gidDebugFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:gidDebugFlag.setStatus(_A)
_GidDebugLevel_Type=Integer32
_GidDebugLevel_Object=MibScalar
gidDebugLevel=_GidDebugLevel_Object((1,3,6,1,4,1,711,2,1,15,1,8),_GidDebugLevel_Type())
gidDebugLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:gidDebugLevel.setStatus(_A)
_GidAcceptedBcastRateIn_Type=Integer32
_GidAcceptedBcastRateIn_Object=MibScalar
gidAcceptedBcastRateIn=_GidAcceptedBcastRateIn_Object((1,3,6,1,4,1,711,2,1,15,1,9),_GidAcceptedBcastRateIn_Type())
gidAcceptedBcastRateIn.setMaxAccess(_D)
if mibBuilder.loadTexts:gidAcceptedBcastRateIn.setStatus(_A)
_GidNbrGroup_ObjectIdentity=ObjectIdentity
gidNbrGroup=_GidNbrGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,2))
_GidNbrCount_Type=Counter32
_GidNbrCount_Object=MibScalar
gidNbrCount=_GidNbrCount_Object((1,3,6,1,4,1,711,2,1,15,2,1),_GidNbrCount_Type())
gidNbrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrCount.setStatus(_A)
_GidNbrTable_Object=MibTable
gidNbrTable=_GidNbrTable_Object((1,3,6,1,4,1,711,2,1,15,2,2))
if mibBuilder.loadTexts:gidNbrTable.setStatus(_A)
_GidNbrEntry_Object=MibTableRow
gidNbrEntry=_GidNbrEntry_Object((1,3,6,1,4,1,711,2,1,15,2,2,1))
gidNbrEntry.setIndexNames((0,_E,_BF))
if mibBuilder.loadTexts:gidNbrEntry.setStatus(_A)
_GidNbrEIA_Type=Integer32
_GidNbrEIA_Object=MibTableColumn
gidNbrEIA=_GidNbrEIA_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,1),_GidNbrEIA_Type())
gidNbrEIA.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrEIA.setStatus(_A)
_GidNbrVCI_Type=Integer32
_GidNbrVCI_Object=MibTableColumn
gidNbrVCI=_GidNbrVCI_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,2),_GidNbrVCI_Type())
gidNbrVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrVCI.setStatus(_A)
class _GidNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_k,2),('exstart',3),('exchange',4),('loading',5),('full',6)))
_GidNbrState_Type.__name__=_C
_GidNbrState_Object=MibTableColumn
gidNbrState=_GidNbrState_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,3),_GidNbrState_Type())
gidNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrState.setStatus(_A)
_GidNbrSyncEvents_Type=Counter32
_GidNbrSyncEvents_Object=MibTableColumn
gidNbrSyncEvents=_GidNbrSyncEvents_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,4),_GidNbrSyncEvents_Type())
gidNbrSyncEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrSyncEvents.setStatus(_A)
_GidNbrDBReqListLength_Type=Counter32
_GidNbrDBReqListLength_Object=MibTableColumn
gidNbrDBReqListLength=_GidNbrDBReqListLength_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,5),_GidNbrDBReqListLength_Type())
gidNbrDBReqListLength.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrDBReqListLength.setStatus(_A)
_GidNbrDBSumListLength_Type=Counter32
_GidNbrDBSumListLength_Object=MibTableColumn
gidNbrDBSumListLength=_GidNbrDBSumListLength_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,6),_GidNbrDBSumListLength_Type())
gidNbrDBSumListLength.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrDBSumListLength.setStatus(_A)
_GidNbrHellosRx_Type=Counter32
_GidNbrHellosRx_Object=MibTableColumn
gidNbrHellosRx=_GidNbrHellosRx_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,7),_GidNbrHellosRx_Type())
gidNbrHellosRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrHellosRx.setStatus(_A)
_GidNbrLinkAnnouncementsRx_Type=Counter32
_GidNbrLinkAnnouncementsRx_Object=MibTableColumn
gidNbrLinkAnnouncementsRx=_GidNbrLinkAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,8),_GidNbrLinkAnnouncementsRx_Type())
gidNbrLinkAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrLinkAnnouncementsRx.setStatus(_A)
_GidNbrNewLinkAnnouncementsRx_Type=Counter32
_GidNbrNewLinkAnnouncementsRx_Object=MibTableColumn
gidNbrNewLinkAnnouncementsRx=_GidNbrNewLinkAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,9),_GidNbrNewLinkAnnouncementsRx_Type())
gidNbrNewLinkAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrNewLinkAnnouncementsRx.setStatus(_A)
_GidNbrIPAnnouncementsRx_Type=Counter32
_GidNbrIPAnnouncementsRx_Object=MibTableColumn
gidNbrIPAnnouncementsRx=_GidNbrIPAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,10),_GidNbrIPAnnouncementsRx_Type())
gidNbrIPAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrIPAnnouncementsRx.setStatus(_A)
_GidNbrNewIPAnnouncementsRx_Type=Counter32
_GidNbrNewIPAnnouncementsRx_Object=MibTableColumn
gidNbrNewIPAnnouncementsRx=_GidNbrNewIPAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,11),_GidNbrNewIPAnnouncementsRx_Type())
gidNbrNewIPAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrNewIPAnnouncementsRx.setStatus(_A)
_GidNbrGenericAnnouncementsRx_Type=Counter32
_GidNbrGenericAnnouncementsRx_Object=MibTableColumn
gidNbrGenericAnnouncementsRx=_GidNbrGenericAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,12),_GidNbrGenericAnnouncementsRx_Type())
gidNbrGenericAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrGenericAnnouncementsRx.setStatus(_A)
_GidNbrNewGenericAnnouncementsRx_Type=Counter32
_GidNbrNewGenericAnnouncementsRx_Object=MibTableColumn
gidNbrNewGenericAnnouncementsRx=_GidNbrNewGenericAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,2,2,1,13),_GidNbrNewGenericAnnouncementsRx_Type())
gidNbrNewGenericAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidNbrNewGenericAnnouncementsRx.setStatus(_A)
_GidClientGroup_ObjectIdentity=ObjectIdentity
gidClientGroup=_GidClientGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,3))
_GidClientCount_Type=Counter32
_GidClientCount_Object=MibScalar
gidClientCount=_GidClientCount_Object((1,3,6,1,4,1,711,2,1,15,3,1),_GidClientCount_Type())
gidClientCount.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientCount.setStatus(_A)
_GidClientTable_Object=MibTable
gidClientTable=_GidClientTable_Object((1,3,6,1,4,1,711,2,1,15,3,2))
if mibBuilder.loadTexts:gidClientTable.setStatus(_A)
_GidClientEntry_Object=MibTableRow
gidClientEntry=_GidClientEntry_Object((1,3,6,1,4,1,711,2,1,15,3,2,1))
gidClientEntry.setIndexNames((0,_E,_BG))
if mibBuilder.loadTexts:gidClientEntry.setStatus(_A)
_GidClientID_Type=Integer32
_GidClientID_Object=MibTableColumn
gidClientID=_GidClientID_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,1),_GidClientID_Type())
gidClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientID.setStatus(_A)
_GidClientEIA_Type=Integer32
_GidClientEIA_Object=MibTableColumn
gidClientEIA=_GidClientEIA_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,2),_GidClientEIA_Type())
gidClientEIA.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientEIA.setStatus(_A)
_GidClientAnnouncementsRx_Type=Counter32
_GidClientAnnouncementsRx_Object=MibTableColumn
gidClientAnnouncementsRx=_GidClientAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,3),_GidClientAnnouncementsRx_Type())
gidClientAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientAnnouncementsRx.setStatus(_A)
_GidClientLinkAnnouncementsRx_Type=Counter32
_GidClientLinkAnnouncementsRx_Object=MibTableColumn
gidClientLinkAnnouncementsRx=_GidClientLinkAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,4),_GidClientLinkAnnouncementsRx_Type())
gidClientLinkAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientLinkAnnouncementsRx.setStatus(_A)
_GidClientIPAnnouncementsRx_Type=Counter32
_GidClientIPAnnouncementsRx_Object=MibTableColumn
gidClientIPAnnouncementsRx=_GidClientIPAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,5),_GidClientIPAnnouncementsRx_Type())
gidClientIPAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientIPAnnouncementsRx.setStatus(_A)
_GidClientGenericAnnouncementsRx_Type=Counter32
_GidClientGenericAnnouncementsRx_Object=MibTableColumn
gidClientGenericAnnouncementsRx=_GidClientGenericAnnouncementsRx_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,6),_GidClientGenericAnnouncementsRx_Type())
gidClientGenericAnnouncementsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientGenericAnnouncementsRx.setStatus(_A)
_GidClientEventsTx_Type=Counter32
_GidClientEventsTx_Object=MibTableColumn
gidClientEventsTx=_GidClientEventsTx_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,7),_GidClientEventsTx_Type())
gidClientEventsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientEventsTx.setStatus(_A)
_GidClientPathsGenerated_Type=Counter32
_GidClientPathsGenerated_Object=MibTableColumn
gidClientPathsGenerated=_GidClientPathsGenerated_Object((1,3,6,1,4,1,711,2,1,15,3,2,1,8),_GidClientPathsGenerated_Type())
gidClientPathsGenerated.setMaxAccess(_B)
if mibBuilder.loadTexts:gidClientPathsGenerated.setStatus(_A)
_GidIOGroup_ObjectIdentity=ObjectIdentity
gidIOGroup=_GidIOGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,4))
_GidIONbrMsgBuffersFree_Type=Counter32
_GidIONbrMsgBuffersFree_Object=MibScalar
gidIONbrMsgBuffersFree=_GidIONbrMsgBuffersFree_Object((1,3,6,1,4,1,711,2,1,15,4,1),_GidIONbrMsgBuffersFree_Type())
gidIONbrMsgBuffersFree.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIONbrMsgBuffersFree.setStatus(_A)
_GidIONbrMsgBuffersActive_Type=Counter32
_GidIONbrMsgBuffersActive_Object=MibScalar
gidIONbrMsgBuffersActive=_GidIONbrMsgBuffersActive_Object((1,3,6,1,4,1,711,2,1,15,4,2),_GidIONbrMsgBuffersActive_Type())
gidIONbrMsgBuffersActive.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIONbrMsgBuffersActive.setStatus(_A)
_GidIOClientMsgBuffersFree_Type=Counter32
_GidIOClientMsgBuffersFree_Object=MibScalar
gidIOClientMsgBuffersFree=_GidIOClientMsgBuffersFree_Object((1,3,6,1,4,1,711,2,1,15,4,3),_GidIOClientMsgBuffersFree_Type())
gidIOClientMsgBuffersFree.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIOClientMsgBuffersFree.setStatus(_A)
_GidIOClientMsgBuffersActive_Type=Counter32
_GidIOClientMsgBuffersActive_Object=MibScalar
gidIOClientMsgBuffersActive=_GidIOClientMsgBuffersActive_Object((1,3,6,1,4,1,711,2,1,15,4,4),_GidIOClientMsgBuffersActive_Type())
gidIOClientMsgBuffersActive.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIOClientMsgBuffersActive.setStatus(_A)
_GidSyncGroup_ObjectIdentity=ObjectIdentity
gidSyncGroup=_GidSyncGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,6))
_GidSyncNbrsExistent_Type=Counter32
_GidSyncNbrsExistent_Object=MibScalar
gidSyncNbrsExistent=_GidSyncNbrsExistent_Object((1,3,6,1,4,1,711,2,1,15,6,1),_GidSyncNbrsExistent_Type())
gidSyncNbrsExistent.setMaxAccess(_B)
if mibBuilder.loadTexts:gidSyncNbrsExistent.setStatus(_A)
_GidSyncNbrsExStart_Type=Counter32
_GidSyncNbrsExStart_Object=MibScalar
gidSyncNbrsExStart=_GidSyncNbrsExStart_Object((1,3,6,1,4,1,711,2,1,15,6,2),_GidSyncNbrsExStart_Type())
gidSyncNbrsExStart.setMaxAccess(_B)
if mibBuilder.loadTexts:gidSyncNbrsExStart.setStatus(_A)
_GidSyncNbrsExchange_Type=Counter32
_GidSyncNbrsExchange_Object=MibScalar
gidSyncNbrsExchange=_GidSyncNbrsExchange_Object((1,3,6,1,4,1,711,2,1,15,6,3),_GidSyncNbrsExchange_Type())
gidSyncNbrsExchange.setMaxAccess(_B)
if mibBuilder.loadTexts:gidSyncNbrsExchange.setStatus(_A)
_GidSyncNbrsLoading_Type=Counter32
_GidSyncNbrsLoading_Object=MibScalar
gidSyncNbrsLoading=_GidSyncNbrsLoading_Object((1,3,6,1,4,1,711,2,1,15,6,4),_GidSyncNbrsLoading_Type())
gidSyncNbrsLoading.setMaxAccess(_B)
if mibBuilder.loadTexts:gidSyncNbrsLoading.setStatus(_A)
_GidSyncNbrsFull_Type=Counter32
_GidSyncNbrsFull_Object=MibScalar
gidSyncNbrsFull=_GidSyncNbrsFull_Object((1,3,6,1,4,1,711,2,1,15,6,5),_GidSyncNbrsFull_Type())
gidSyncNbrsFull.setMaxAccess(_B)
if mibBuilder.loadTexts:gidSyncNbrsFull.setStatus(_A)
_GidLinkGroup_ObjectIdentity=ObjectIdentity
gidLinkGroup=_GidLinkGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,7))
_GidLinkDatabaseSize_Type=Integer32
_GidLinkDatabaseSize_Object=MibScalar
gidLinkDatabaseSize=_GidLinkDatabaseSize_Object((1,3,6,1,4,1,711,2,1,15,7,1),_GidLinkDatabaseSize_Type())
gidLinkDatabaseSize.setMaxAccess(_B)
if mibBuilder.loadTexts:gidLinkDatabaseSize.setStatus(_A)
_GidLineCardTable_Object=MibTable
gidLineCardTable=_GidLineCardTable_Object((1,3,6,1,4,1,711,2,1,15,7,2))
if mibBuilder.loadTexts:gidLineCardTable.setStatus(_A)
_GidLineCardEntry_Object=MibTableRow
gidLineCardEntry=_GidLineCardEntry_Object((1,3,6,1,4,1,711,2,1,15,7,2,1))
gidLineCardEntry.setIndexNames((0,_E,_BH),(0,_E,_BI))
if mibBuilder.loadTexts:gidLineCardEntry.setStatus(_A)
_GidLineCardChassis_Type=Integer32
_GidLineCardChassis_Object=MibTableColumn
gidLineCardChassis=_GidLineCardChassis_Object((1,3,6,1,4,1,711,2,1,15,7,2,1,1),_GidLineCardChassis_Type())
gidLineCardChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:gidLineCardChassis.setStatus(_A)
_GidLineCardSlot_Type=Integer32
_GidLineCardSlot_Object=MibTableColumn
gidLineCardSlot=_GidLineCardSlot_Object((1,3,6,1,4,1,711,2,1,15,7,2,1,2),_GidLineCardSlot_Type())
gidLineCardSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:gidLineCardSlot.setStatus(_A)
_GidLineCardEntryAge_Type=LightStreamUpToMaxAge
_GidLineCardEntryAge_Object=MibTableColumn
gidLineCardEntryAge=_GidLineCardEntryAge_Object((1,3,6,1,4,1,711,2,1,15,7,2,1,3),_GidLineCardEntryAge_Type())
gidLineCardEntryAge.setMaxAccess(_B)
if mibBuilder.loadTexts:gidLineCardEntryAge.setStatus(_A)
_GidLineCardEntrySeqno_Type=Integer32
_GidLineCardEntrySeqno_Object=MibTableColumn
gidLineCardEntrySeqno=_GidLineCardEntrySeqno_Object((1,3,6,1,4,1,711,2,1,15,7,2,1,4),_GidLineCardEntrySeqno_Type())
gidLineCardEntrySeqno.setMaxAccess(_B)
if mibBuilder.loadTexts:gidLineCardEntrySeqno.setStatus(_A)
_GidLineCardEntryAdvNP_Type=Integer32
_GidLineCardEntryAdvNP_Object=MibTableColumn
gidLineCardEntryAdvNP=_GidLineCardEntryAdvNP_Object((1,3,6,1,4,1,711,2,1,15,7,2,1,5),_GidLineCardEntryAdvNP_Type())
gidLineCardEntryAdvNP.setMaxAccess(_B)
if mibBuilder.loadTexts:gidLineCardEntryAdvNP.setStatus(_A)
_GidLineCardPorts_Type=Integer32
_GidLineCardPorts_Object=MibTableColumn
gidLineCardPorts=_GidLineCardPorts_Object((1,3,6,1,4,1,711,2,1,15,7,2,1,6),_GidLineCardPorts_Type())
gidLineCardPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:gidLineCardPorts.setStatus(_A)
_GidPortTable_Object=MibTable
gidPortTable=_GidPortTable_Object((1,3,6,1,4,1,711,2,1,15,7,3))
if mibBuilder.loadTexts:gidPortTable.setStatus(_A)
_GidPortEntry_Object=MibTableRow
gidPortEntry=_GidPortEntry_Object((1,3,6,1,4,1,711,2,1,15,7,3,1))
gidPortEntry.setIndexNames((0,_E,_BJ),(0,_E,_BK))
if mibBuilder.loadTexts:gidPortEntry.setStatus(_A)
_GidPortChassis_Type=Integer32
_GidPortChassis_Object=MibTableColumn
gidPortChassis=_GidPortChassis_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,1),_GidPortChassis_Type())
gidPortChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortChassis.setStatus(_A)
_GidPortID_Type=Integer32
_GidPortID_Object=MibTableColumn
gidPortID=_GidPortID_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,2),_GidPortID_Type())
gidPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortID.setStatus(_A)
class _GidPortService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('edge',2)))
_GidPortService_Type.__name__=_C
_GidPortService_Object=MibTableColumn
gidPortService=_GidPortService_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,3),_GidPortService_Type())
gidPortService.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortService.setStatus(_A)
class _GidPortUpDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_M,2)))
_GidPortUpDown_Type.__name__=_C
_GidPortUpDown_Object=MibTableColumn
gidPortUpDown=_GidPortUpDown_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,4),_GidPortUpDown_Type())
gidPortUpDown.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortUpDown.setStatus(_A)
_GidPortBW0_Type=Integer32
_GidPortBW0_Object=MibTableColumn
gidPortBW0=_GidPortBW0_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,5),_GidPortBW0_Type())
gidPortBW0.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortBW0.setStatus(_A)
_GidPortBW1_Type=Integer32
_GidPortBW1_Object=MibTableColumn
gidPortBW1=_GidPortBW1_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,6),_GidPortBW1_Type())
gidPortBW1.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortBW1.setStatus(_A)
_GidPortBW2_Type=Integer32
_GidPortBW2_Object=MibTableColumn
gidPortBW2=_GidPortBW2_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,7),_GidPortBW2_Type())
gidPortBW2.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortBW2.setStatus(_A)
_GidPortRemoteChassis_Type=Integer32
_GidPortRemoteChassis_Object=MibTableColumn
gidPortRemoteChassis=_GidPortRemoteChassis_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,8),_GidPortRemoteChassis_Type())
gidPortRemoteChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortRemoteChassis.setStatus(_A)
_GidPortRemotePort_Type=Integer32
_GidPortRemotePort_Object=MibTableColumn
gidPortRemotePort=_GidPortRemotePort_Object((1,3,6,1,4,1,711,2,1,15,7,3,1,9),_GidPortRemotePort_Type())
gidPortRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:gidPortRemotePort.setStatus(_A)
_GidIpAddressGroup_ObjectIdentity=ObjectIdentity
gidIpAddressGroup=_GidIpAddressGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,8))
_GidIpAddressDatabaseSize_Type=Integer32
_GidIpAddressDatabaseSize_Object=MibScalar
gidIpAddressDatabaseSize=_GidIpAddressDatabaseSize_Object((1,3,6,1,4,1,711,2,1,15,8,1),_GidIpAddressDatabaseSize_Type())
gidIpAddressDatabaseSize.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIpAddressDatabaseSize.setStatus(_A)
_GidIpAddressTable_Object=MibTable
gidIpAddressTable=_GidIpAddressTable_Object((1,3,6,1,4,1,711,2,1,15,8,2))
if mibBuilder.loadTexts:gidIpAddressTable.setStatus(_A)
_GidIpAddressEntry_Object=MibTableRow
gidIpAddressEntry=_GidIpAddressEntry_Object((1,3,6,1,4,1,711,2,1,15,8,2,1))
gidIpAddressEntry.setIndexNames((0,_E,_BL))
if mibBuilder.loadTexts:gidIpAddressEntry.setStatus(_A)
_GidInternalIpAddress_Type=IpAddress
_GidInternalIpAddress_Object=MibTableColumn
gidInternalIpAddress=_GidInternalIpAddress_Object((1,3,6,1,4,1,711,2,1,15,8,2,1,1),_GidInternalIpAddress_Type())
gidInternalIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gidInternalIpAddress.setStatus(_A)
_GidIpEntryAge_Type=LightStreamUpToMaxAge
_GidIpEntryAge_Object=MibTableColumn
gidIpEntryAge=_GidIpEntryAge_Object((1,3,6,1,4,1,711,2,1,15,8,2,1,2),_GidIpEntryAge_Type())
gidIpEntryAge.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIpEntryAge.setStatus(_A)
_GidIpEntrySeqno_Type=Integer32
_GidIpEntrySeqno_Object=MibTableColumn
gidIpEntrySeqno=_GidIpEntrySeqno_Object((1,3,6,1,4,1,711,2,1,15,8,2,1,3),_GidIpEntrySeqno_Type())
gidIpEntrySeqno.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIpEntrySeqno.setStatus(_A)
_GidIpEntryAdvNP_Type=Integer32
_GidIpEntryAdvNP_Object=MibTableColumn
gidIpEntryAdvNP=_GidIpEntryAdvNP_Object((1,3,6,1,4,1,711,2,1,15,8,2,1,4),_GidIpEntryAdvNP_Type())
gidIpEntryAdvNP.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIpEntryAdvNP.setStatus(_A)
_GidIpEntryNetMask_Type=Integer32
_GidIpEntryNetMask_Object=MibTableColumn
gidIpEntryNetMask=_GidIpEntryNetMask_Object((1,3,6,1,4,1,711,2,1,15,8,2,1,5),_GidIpEntryNetMask_Type())
gidIpEntryNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIpEntryNetMask.setStatus(_A)
class _GidIpEntryEIA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_GidIpEntryEIA_Type.__name__=_R
_GidIpEntryEIA_Object=MibTableColumn
gidIpEntryEIA=_GidIpEntryEIA_Object((1,3,6,1,4,1,711,2,1,15,8,2,1,6),_GidIpEntryEIA_Type())
gidIpEntryEIA.setMaxAccess(_B)
if mibBuilder.loadTexts:gidIpEntryEIA.setStatus(_A)
_GidEventGroup_ObjectIdentity=ObjectIdentity
gidEventGroup=_GidEventGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,15,9))
_GidEventLinkEventsDelivered_Type=Counter32
_GidEventLinkEventsDelivered_Object=MibScalar
gidEventLinkEventsDelivered=_GidEventLinkEventsDelivered_Object((1,3,6,1,4,1,711,2,1,15,9,1),_GidEventLinkEventsDelivered_Type())
gidEventLinkEventsDelivered.setMaxAccess(_B)
if mibBuilder.loadTexts:gidEventLinkEventsDelivered.setStatus(_A)
_GidEventIpEventsDelivered_Type=Counter32
_GidEventIpEventsDelivered_Object=MibScalar
gidEventIpEventsDelivered=_GidEventIpEventsDelivered_Object((1,3,6,1,4,1,711,2,1,15,9,2),_GidEventIpEventsDelivered_Type())
gidEventIpEventsDelivered.setMaxAccess(_B)
if mibBuilder.loadTexts:gidEventIpEventsDelivered.setStatus(_A)
_GidEventGenericGinfoEventsDelivered_Type=Counter32
_GidEventGenericGinfoEventsDelivered_Object=MibScalar
gidEventGenericGinfoEventsDelivered=_GidEventGenericGinfoEventsDelivered_Object((1,3,6,1,4,1,711,2,1,15,9,3),_GidEventGenericGinfoEventsDelivered_Type())
gidEventGenericGinfoEventsDelivered.setMaxAccess(_B)
if mibBuilder.loadTexts:gidEventGenericGinfoEventsDelivered.setStatus(_A)
_GidEventGenericGinfoEventTable_Object=MibTable
gidEventGenericGinfoEventTable=_GidEventGenericGinfoEventTable_Object((1,3,6,1,4,1,711,2,1,15,9,4))
if mibBuilder.loadTexts:gidEventGenericGinfoEventTable.setStatus(_A)
_GidEventGenericGinfoEventCount_Object=MibTableRow
gidEventGenericGinfoEventCount=_GidEventGenericGinfoEventCount_Object((1,3,6,1,4,1,711,2,1,15,9,4,1))
gidEventGenericGinfoEventCount.setIndexNames((0,_E,_BM))
if mibBuilder.loadTexts:gidEventGenericGinfoEventCount.setStatus(_A)
_GidEventDistributionGroup_Type=Integer32
_GidEventDistributionGroup_Object=MibTableColumn
gidEventDistributionGroup=_GidEventDistributionGroup_Object((1,3,6,1,4,1,711,2,1,15,9,4,1,1),_GidEventDistributionGroup_Type())
gidEventDistributionGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:gidEventDistributionGroup.setStatus(_A)
_GidEventGenericGinfoEvents_Type=Counter32
_GidEventGenericGinfoEvents_Object=MibTableColumn
gidEventGenericGinfoEvents=_GidEventGenericGinfoEvents_Object((1,3,6,1,4,1,711,2,1,15,9,4,1,2),_GidEventGenericGinfoEvents_Type())
gidEventGenericGinfoEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:gidEventGenericGinfoEvents.setStatus(_A)
_LsPID_ObjectIdentity=ObjectIdentity
lsPID=_LsPID_ObjectIdentity((1,3,6,1,4,1,711,2,1,16))
_PidTable_Object=MibTable
pidTable=_PidTable_Object((1,3,6,1,4,1,711,2,1,16,1))
if mibBuilder.loadTexts:pidTable.setStatus(_A)
_PidEntry_Object=MibTableRow
pidEntry=_PidEntry_Object((1,3,6,1,4,1,711,2,1,16,1,1))
pidEntry.setIndexNames((0,_E,'pidIndex'))
if mibBuilder.loadTexts:pidEntry.setStatus(_A)
_PidIndex_Type=Integer32
_PidIndex_Object=MibTableColumn
pidIndex=_PidIndex_Object((1,3,6,1,4,1,711,2,1,16,1,1,1),_PidIndex_Type())
pidIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pidIndex.setStatus(_A)
_PidName_Type=DisplayString
_PidName_Object=MibTableColumn
pidName=_PidName_Object((1,3,6,1,4,1,711,2,1,16,1,1,2),_PidName_Type())
pidName.setMaxAccess(_B)
if mibBuilder.loadTexts:pidName.setStatus(_A)
_PidCreationTime_Type=Integer32
_PidCreationTime_Object=MibTableColumn
pidCreationTime=_PidCreationTime_Object((1,3,6,1,4,1,711,2,1,16,1,1,3),_PidCreationTime_Type())
pidCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pidCreationTime.setStatus(_A)
class _PidOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_S,2)))
_PidOperStatus_Type.__name__=_C
_PidOperStatus_Object=MibTableColumn
pidOperStatus=_PidOperStatus_Object((1,3,6,1,4,1,711,2,1,16,1,1,4),_PidOperStatus_Type())
pidOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pidOperStatus.setStatus(_A)
class _PidAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_S,2)))
_PidAdminStatus_Type.__name__=_C
_PidAdminStatus_Object=MibTableColumn
pidAdminStatus=_PidAdminStatus_Object((1,3,6,1,4,1,711,2,1,16,1,1,5),_PidAdminStatus_Type())
pidAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pidAdminStatus.setStatus(_A)
_LsND_ObjectIdentity=ObjectIdentity
lsND=_LsND_ObjectIdentity((1,3,6,1,4,1,711,2,1,17))
_NdGeneralGroup_ObjectIdentity=ObjectIdentity
ndGeneralGroup=_NdGeneralGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,17,1))
_NdSoftwareVersionNumber_Type=DisplayString
_NdSoftwareVersionNumber_Object=MibScalar
ndSoftwareVersionNumber=_NdSoftwareVersionNumber_Object((1,3,6,1,4,1,711,2,1,17,1,1),_NdSoftwareVersionNumber_Type())
ndSoftwareVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ndSoftwareVersionNumber.setStatus(_A)
_NdProcessID_Type=Integer32
_NdProcessID_Object=MibScalar
ndProcessID=_NdProcessID_Object((1,3,6,1,4,1,711,2,1,17,1,2),_NdProcessID_Type())
ndProcessID.setMaxAccess(_B)
if mibBuilder.loadTexts:ndProcessID.setStatus(_A)
_NdMemoryUse_Type=Counter32
_NdMemoryUse_Object=MibScalar
ndMemoryUse=_NdMemoryUse_Object((1,3,6,1,4,1,711,2,1,17,1,4),_NdMemoryUse_Type())
ndMemoryUse.setMaxAccess(_B)
if mibBuilder.loadTexts:ndMemoryUse.setStatus(_A)
_NdTimersProcessed_Type=Counter32
_NdTimersProcessed_Object=MibScalar
ndTimersProcessed=_NdTimersProcessed_Object((1,3,6,1,4,1,711,2,1,17,1,5),_NdTimersProcessed_Type())
ndTimersProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:ndTimersProcessed.setStatus(_A)
_NdLCGroup_ObjectIdentity=ObjectIdentity
ndLCGroup=_NdLCGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,17,2))
_NdLCCount_Type=Counter32
_NdLCCount_Object=MibScalar
ndLCCount=_NdLCCount_Object((1,3,6,1,4,1,711,2,1,17,2,1),_NdLCCount_Type())
ndLCCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ndLCCount.setStatus(_A)
_NdLCTable_Object=MibTable
ndLCTable=_NdLCTable_Object((1,3,6,1,4,1,711,2,1,17,2,2))
if mibBuilder.loadTexts:ndLCTable.setStatus(_A)
_NdLCEntry_Object=MibTableRow
ndLCEntry=_NdLCEntry_Object((1,3,6,1,4,1,711,2,1,17,2,2,1))
ndLCEntry.setIndexNames((0,_E,'ndLCEIA'))
if mibBuilder.loadTexts:ndLCEntry.setStatus(_A)
_NdLCEIA_Type=Integer32
_NdLCEIA_Object=MibTableColumn
ndLCEIA=_NdLCEIA_Object((1,3,6,1,4,1,711,2,1,17,2,2,1,1),_NdLCEIA_Type())
ndLCEIA.setMaxAccess(_B)
if mibBuilder.loadTexts:ndLCEIA.setStatus(_A)
_NdLCChannel_Type=Integer32
_NdLCChannel_Object=MibTableColumn
ndLCChannel=_NdLCChannel_Object((1,3,6,1,4,1,711,2,1,17,2,2,1,2),_NdLCChannel_Type())
ndLCChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ndLCChannel.setStatus(_A)
class _NdLCState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_k,2),(_M,3),(_BN,4)))
_NdLCState_Type.__name__=_C
_NdLCState_Object=MibTableColumn
ndLCState=_NdLCState_Object((1,3,6,1,4,1,711,2,1,17,2,2,1,3),_NdLCState_Type())
ndLCState.setMaxAccess(_B)
if mibBuilder.loadTexts:ndLCState.setStatus(_A)
_NdNbrGroup_ObjectIdentity=ObjectIdentity
ndNbrGroup=_NdNbrGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,17,3))
_NdNbrCount_Type=Counter32
_NdNbrCount_Object=MibScalar
ndNbrCount=_NdNbrCount_Object((1,3,6,1,4,1,711,2,1,17,3,1),_NdNbrCount_Type())
ndNbrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ndNbrCount.setStatus(_A)
_NdNbrTable_Object=MibTable
ndNbrTable=_NdNbrTable_Object((1,3,6,1,4,1,711,2,1,17,3,2))
if mibBuilder.loadTexts:ndNbrTable.setStatus(_A)
_NdNbrEntry_Object=MibTableRow
ndNbrEntry=_NdNbrEntry_Object((1,3,6,1,4,1,711,2,1,17,3,2,1))
ndNbrEntry.setIndexNames((0,_E,'ndNbrEIA'))
if mibBuilder.loadTexts:ndNbrEntry.setStatus(_A)
_NdNbrEIA_Type=Integer32
_NdNbrEIA_Object=MibTableColumn
ndNbrEIA=_NdNbrEIA_Object((1,3,6,1,4,1,711,2,1,17,3,2,1,1),_NdNbrEIA_Type())
ndNbrEIA.setMaxAccess(_B)
if mibBuilder.loadTexts:ndNbrEIA.setStatus(_A)
_NdNbrChannel_Type=Integer32
_NdNbrChannel_Object=MibTableColumn
ndNbrChannel=_NdNbrChannel_Object((1,3,6,1,4,1,711,2,1,17,3,2,1,2),_NdNbrChannel_Type())
ndNbrChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ndNbrChannel.setStatus(_A)
class _NdNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_k,2),(_M,3),(_BN,4)))
_NdNbrState_Type.__name__=_C
_NdNbrState_Object=MibTableColumn
ndNbrState=_NdNbrState_Object((1,3,6,1,4,1,711,2,1,17,3,2,1,3),_NdNbrState_Type())
ndNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:ndNbrState.setStatus(_A)
_NdSwudGroup_ObjectIdentity=ObjectIdentity
ndSwudGroup=_NdSwudGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,17,4))
_NdSwudTable_Object=MibTable
ndSwudTable=_NdSwudTable_Object((1,3,6,1,4,1,711,2,1,17,4,1))
if mibBuilder.loadTexts:ndSwudTable.setStatus(_A)
_NdSwudEntry_Object=MibTableRow
ndSwudEntry=_NdSwudEntry_Object((1,3,6,1,4,1,711,2,1,17,4,1,1))
ndSwudEntry.setIndexNames((0,_E,_BO))
if mibBuilder.loadTexts:ndSwudEntry.setStatus(_A)
_NdSwudIndex_Type=Integer32
_NdSwudIndex_Object=MibTableColumn
ndSwudIndex=_NdSwudIndex_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,1),_NdSwudIndex_Type())
ndSwudIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ndSwudIndex.setStatus(_A)
_NdOperIntvl_Type=Integer32
_NdOperIntvl_Object=MibTableColumn
ndOperIntvl=_NdOperIntvl_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,2),_NdOperIntvl_Type())
ndOperIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:ndOperIntvl.setStatus(_A)
_NdOperJ_Type=Integer32
_NdOperJ_Object=MibTableColumn
ndOperJ=_NdOperJ_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,3),_NdOperJ_Type())
ndOperJ.setMaxAccess(_B)
if mibBuilder.loadTexts:ndOperJ.setStatus(_A)
_NdOperK_Type=Integer32
_NdOperK_Object=MibTableColumn
ndOperK=_NdOperK_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,4),_NdOperK_Type())
ndOperK.setMaxAccess(_B)
if mibBuilder.loadTexts:ndOperK.setStatus(_A)
_NdOperM_Type=Integer32
_NdOperM_Object=MibTableColumn
ndOperM=_NdOperM_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,5),_NdOperM_Type())
ndOperM.setMaxAccess(_B)
if mibBuilder.loadTexts:ndOperM.setStatus(_A)
_NdOperN_Type=Integer32
_NdOperN_Object=MibTableColumn
ndOperN=_NdOperN_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,6),_NdOperN_Type())
ndOperN.setMaxAccess(_B)
if mibBuilder.loadTexts:ndOperN.setStatus(_A)
class _NdAdminIntvl_Type(Integer32):defaultValue=3
_NdAdminIntvl_Type.__name__=_C
_NdAdminIntvl_Object=MibTableColumn
ndAdminIntvl=_NdAdminIntvl_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,7),_NdAdminIntvl_Type())
ndAdminIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:ndAdminIntvl.setStatus(_A)
class _NdAdminJ_Type(Integer32):defaultValue=1
_NdAdminJ_Type.__name__=_C
_NdAdminJ_Object=MibTableColumn
ndAdminJ=_NdAdminJ_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,8),_NdAdminJ_Type())
ndAdminJ.setMaxAccess(_D)
if mibBuilder.loadTexts:ndAdminJ.setStatus(_A)
class _NdAdminK_Type(Integer32):defaultValue=1
_NdAdminK_Type.__name__=_C
_NdAdminK_Object=MibTableColumn
ndAdminK=_NdAdminK_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,9),_NdAdminK_Type())
ndAdminK.setMaxAccess(_D)
if mibBuilder.loadTexts:ndAdminK.setStatus(_A)
class _NdAdminM_Type(Integer32):defaultValue=1
_NdAdminM_Type.__name__=_C
_NdAdminM_Object=MibTableColumn
ndAdminM=_NdAdminM_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,10),_NdAdminM_Type())
ndAdminM.setMaxAccess(_D)
if mibBuilder.loadTexts:ndAdminM.setStatus(_A)
class _NdAdminN_Type(Integer32):defaultValue=1
_NdAdminN_Type.__name__=_C
_NdAdminN_Object=MibTableColumn
ndAdminN=_NdAdminN_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,11),_NdAdminN_Type())
ndAdminN.setMaxAccess(_D)
if mibBuilder.loadTexts:ndAdminN.setStatus(_A)
_NdTrigger_Type=Integer32
_NdTrigger_Object=MibTableColumn
ndTrigger=_NdTrigger_Object((1,3,6,1,4,1,711,2,1,17,4,1,1,12),_NdTrigger_Type())
ndTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:ndTrigger.setStatus(_A)
_NdSwudStatsInputErrors_Type=Counter32
_NdSwudStatsInputErrors_Object=MibScalar
ndSwudStatsInputErrors=_NdSwudStatsInputErrors_Object((1,3,6,1,4,1,711,2,1,17,4,2),_NdSwudStatsInputErrors_Type())
ndSwudStatsInputErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ndSwudStatsInputErrors.setStatus(_A)
_NdSwudStatsTable_Object=MibTable
ndSwudStatsTable=_NdSwudStatsTable_Object((1,3,6,1,4,1,711,2,1,17,4,3))
if mibBuilder.loadTexts:ndSwudStatsTable.setStatus(_A)
_NdSwudStatsEntry_Object=MibTableRow
ndSwudStatsEntry=_NdSwudStatsEntry_Object((1,3,6,1,4,1,711,2,1,17,4,3,1))
ndSwudStatsEntry.setIndexNames((0,_E,_BP))
if mibBuilder.loadTexts:ndSwudStatsEntry.setStatus(_A)
_NdSwudStatsIndex_Type=Integer32
_NdSwudStatsIndex_Object=MibTableColumn
ndSwudStatsIndex=_NdSwudStatsIndex_Object((1,3,6,1,4,1,711,2,1,17,4,3,1,1),_NdSwudStatsIndex_Type())
ndSwudStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ndSwudStatsIndex.setStatus(_A)
_NdInputCells_Type=Counter32
_NdInputCells_Object=MibTableColumn
ndInputCells=_NdInputCells_Object((1,3,6,1,4,1,711,2,1,17,4,3,1,2),_NdInputCells_Type())
ndInputCells.setMaxAccess(_B)
if mibBuilder.loadTexts:ndInputCells.setStatus(_A)
_NdInputErrs_Type=Counter32
_NdInputErrs_Object=MibTableColumn
ndInputErrs=_NdInputErrs_Object((1,3,6,1,4,1,711,2,1,17,4,3,1,3),_NdInputErrs_Type())
ndInputErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:ndInputErrs.setStatus(_A)
_NdOutputCells_Type=Counter32
_NdOutputCells_Object=MibTableColumn
ndOutputCells=_NdOutputCells_Object((1,3,6,1,4,1,711,2,1,17,4,3,1,4),_NdOutputCells_Type())
ndOutputCells.setMaxAccess(_B)
if mibBuilder.loadTexts:ndOutputCells.setStatus(_A)
_NdOutputErrs_Type=Counter32
_NdOutputErrs_Object=MibTableColumn
ndOutputErrs=_NdOutputErrs_Object((1,3,6,1,4,1,711,2,1,17,4,3,1,5),_NdOutputErrs_Type())
ndOutputErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:ndOutputErrs.setStatus(_A)
_NdClientGroup_ObjectIdentity=ObjectIdentity
ndClientGroup=_NdClientGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,17,5))
_NdClientCount_Type=Counter32
_NdClientCount_Object=MibScalar
ndClientCount=_NdClientCount_Object((1,3,6,1,4,1,711,2,1,17,5,1),_NdClientCount_Type())
ndClientCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ndClientCount.setStatus(_A)
_NdClientTable_Object=MibTable
ndClientTable=_NdClientTable_Object((1,3,6,1,4,1,711,2,1,17,5,2))
if mibBuilder.loadTexts:ndClientTable.setStatus(_A)
_NdClientEntry_Object=MibTableRow
ndClientEntry=_NdClientEntry_Object((1,3,6,1,4,1,711,2,1,17,5,2,1))
ndClientEntry.setIndexNames((0,_E,_BQ))
if mibBuilder.loadTexts:ndClientEntry.setStatus(_A)
_NdClientID_Type=Integer32
_NdClientID_Object=MibTableColumn
ndClientID=_NdClientID_Object((1,3,6,1,4,1,711,2,1,17,5,2,1,1),_NdClientID_Type())
ndClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:ndClientID.setStatus(_A)
class _NdClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7)));namedValues=NamedValues(*(('nd',3),('gid',4),('lcc',5),('ca',6),('sys',7)))
_NdClientType_Type.__name__=_C
_NdClientType_Object=MibTableColumn
ndClientType=_NdClientType_Object((1,3,6,1,4,1,711,2,1,17,5,2,1,2),_NdClientType_Type())
ndClientType.setMaxAccess(_B)
if mibBuilder.loadTexts:ndClientType.setStatus(_A)
_NdClientSubType_Type=Integer32
_NdClientSubType_Object=MibTableColumn
ndClientSubType=_NdClientSubType_Object((1,3,6,1,4,1,711,2,1,17,5,2,1,3),_NdClientSubType_Type())
ndClientSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:ndClientSubType.setStatus(_A)
_NdClientEIA_Type=Integer32
_NdClientEIA_Object=MibTableColumn
ndClientEIA=_NdClientEIA_Object((1,3,6,1,4,1,711,2,1,17,5,2,1,4),_NdClientEIA_Type())
ndClientEIA.setMaxAccess(_B)
if mibBuilder.loadTexts:ndClientEIA.setStatus(_A)
_NdClientRegistration_Type=Integer32
_NdClientRegistration_Object=MibTableColumn
ndClientRegistration=_NdClientRegistration_Object((1,3,6,1,4,1,711,2,1,17,5,2,1,5),_NdClientRegistration_Type())
ndClientRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:ndClientRegistration.setStatus(_A)
_NdInternalGroup_ObjectIdentity=ObjectIdentity
ndInternalGroup=_NdInternalGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,17,6))
class _NdInternalDebugLevel_Type(Integer32):defaultValue=0
_NdInternalDebugLevel_Type.__name__=_C
_NdInternalDebugLevel_Object=MibScalar
ndInternalDebugLevel=_NdInternalDebugLevel_Object((1,3,6,1,4,1,711,2,1,17,6,1),_NdInternalDebugLevel_Type())
ndInternalDebugLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ndInternalDebugLevel.setStatus(_A)
class _NdInternalDebugFlags_Type(Integer32):defaultValue=0
_NdInternalDebugFlags_Type.__name__=_C
_NdInternalDebugFlags_Object=MibScalar
ndInternalDebugFlags=_NdInternalDebugFlags_Object((1,3,6,1,4,1,711,2,1,17,6,2),_NdInternalDebugFlags_Type())
ndInternalDebugFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:ndInternalDebugFlags.setStatus(_A)
_NdRedundancyGroup_ObjectIdentity=ObjectIdentity
ndRedundancyGroup=_NdRedundancyGroup_ObjectIdentity((1,3,6,1,4,1,711,2,1,17,7))
class _NdPrimaryNP_Type(Integer32):defaultValue=0
_NdPrimaryNP_Type.__name__=_C
_NdPrimaryNP_Object=MibScalar
ndPrimaryNP=_NdPrimaryNP_Object((1,3,6,1,4,1,711,2,1,17,7,1),_NdPrimaryNP_Type())
ndPrimaryNP.setMaxAccess(_B)
if mibBuilder.loadTexts:ndPrimaryNP.setStatus(_A)
_NdThisNP_Type=Integer32
_NdThisNP_Object=MibScalar
ndThisNP=_NdThisNP_Object((1,3,6,1,4,1,711,2,1,17,7,2),_NdThisNP_Type())
ndThisNP.setMaxAccess(_B)
if mibBuilder.loadTexts:ndThisNP.setStatus(_A)
_NdForceToBackup_Type=Integer32
_NdForceToBackup_Object=MibScalar
ndForceToBackup=_NdForceToBackup_Object((1,3,6,1,4,1,711,2,1,17,7,3),_NdForceToBackup_Type())
ndForceToBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:ndForceToBackup.setStatus(_A)
_LwmaInfo_ObjectIdentity=ObjectIdentity
lwmaInfo=_LwmaInfo_ObjectIdentity((1,3,6,1,4,1,711,2,1,18))
_LwmaTable_Object=MibTable
lwmaTable=_LwmaTable_Object((1,3,6,1,4,1,711,2,1,18,1))
if mibBuilder.loadTexts:lwmaTable.setStatus(_A)
_LwmaEntry_Object=MibTableRow
lwmaEntry=_LwmaEntry_Object((1,3,6,1,4,1,711,2,1,18,1,1))
lwmaEntry.setIndexNames((0,_E,_BR))
if mibBuilder.loadTexts:lwmaEntry.setStatus(_A)
_LwmaIndex_Type=Integer32
_LwmaIndex_Object=MibTableColumn
lwmaIndex=_LwmaIndex_Object((1,3,6,1,4,1,711,2,1,18,1,1,1),_LwmaIndex_Type())
lwmaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lwmaIndex.setStatus(_A)
_LwmaCreationTime_Type=Integer32
_LwmaCreationTime_Object=MibTableColumn
lwmaCreationTime=_LwmaCreationTime_Object((1,3,6,1,4,1,711,2,1,18,1,1,2),_LwmaCreationTime_Type())
lwmaCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lwmaCreationTime.setStatus(_A)
_LwmaTableNotification_Type=ObjectIdentifier
_LwmaTableNotification_Object=MibTableColumn
lwmaTableNotification=_LwmaTableNotification_Object((1,3,6,1,4,1,711,2,1,18,1,1,3),_LwmaTableNotification_Type())
lwmaTableNotification.setMaxAccess(_B)
if mibBuilder.loadTexts:lwmaTableNotification.setStatus(_A)
class _LwmaTrapLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3),(_g,4)))
_LwmaTrapLevel_Type.__name__=_C
_LwmaTrapLevel_Object=MibTableColumn
lwmaTrapLevel=_LwmaTrapLevel_Object((1,3,6,1,4,1,711,2,1,18,1,1,4),_LwmaTrapLevel_Type())
lwmaTrapLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:lwmaTrapLevel.setStatus(_A)
_LwmaTrapNumber_Type=Integer32
_LwmaTrapNumber_Object=MibTableColumn
lwmaTrapNumber=_LwmaTrapNumber_Object((1,3,6,1,4,1,711,2,1,18,1,1,5),_LwmaTrapNumber_Type())
lwmaTrapNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lwmaTrapNumber.setStatus(_A)
class _LwmaTrapOnOffState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trapOn',1),('trapOff',2)))
_LwmaTrapOnOffState_Type.__name__=_C
_LwmaTrapOnOffState_Object=MibTableColumn
lwmaTrapOnOffState=_LwmaTrapOnOffState_Object((1,3,6,1,4,1,711,2,1,18,1,1,6),_LwmaTrapOnOffState_Type())
lwmaTrapOnOffState.setMaxAccess(_D)
if mibBuilder.loadTexts:lwmaTrapOnOffState.setStatus(_A)
class _LwmaTrapCliAlias_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_LwmaTrapCliAlias_Type.__name__=_R
_LwmaTrapCliAlias_Object=MibTableColumn
lwmaTrapCliAlias=_LwmaTrapCliAlias_Object((1,3,6,1,4,1,711,2,1,18,1,1,7),_LwmaTrapCliAlias_Type())
lwmaTrapCliAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:lwmaTrapCliAlias.setStatus(_A)
_LightStreamInternet_ObjectIdentity=ObjectIdentity
lightStreamInternet=_LightStreamInternet_ObjectIdentity((1,3,6,1,4,1,711,3))
_LightStreamBridge_ObjectIdentity=ObjectIdentity
lightStreamBridge=_LightStreamBridge_ObjectIdentity((1,3,6,1,4,1,711,3,1))
_LightStreamBridgePortTable_Object=MibTable
lightStreamBridgePortTable=_LightStreamBridgePortTable_Object((1,3,6,1,4,1,711,3,1,1))
if mibBuilder.loadTexts:lightStreamBridgePortTable.setStatus(_A)
_LightStreamBridgePortEntry_Object=MibTableRow
lightStreamBridgePortEntry=_LightStreamBridgePortEntry_Object((1,3,6,1,4,1,711,3,1,1,1))
lightStreamBridgePortEntry.setIndexNames((0,_E,_BS))
if mibBuilder.loadTexts:lightStreamBridgePortEntry.setStatus(_A)
_LightStreamBrPortPort_Type=Integer32
_LightStreamBrPortPort_Object=MibTableColumn
lightStreamBrPortPort=_LightStreamBrPortPort_Object((1,3,6,1,4,1,711,3,1,1,1,1),_LightStreamBrPortPort_Type())
lightStreamBrPortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrPortPort.setStatus(_A)
class _LightStreamBrPortDefaultAction_Type(LightStreamFilterAction):defaultValue=1
_LightStreamBrPortDefaultAction_Type.__name__=_BT
_LightStreamBrPortDefaultAction_Object=MibTableColumn
lightStreamBrPortDefaultAction=_LightStreamBrPortDefaultAction_Object((1,3,6,1,4,1,711,3,1,1,1,2),_LightStreamBrPortDefaultAction_Type())
lightStreamBrPortDefaultAction.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrPortDefaultAction.setStatus(_A)
class _LightStreamBrPortBcastRateLimit_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,127))
_LightStreamBrPortBcastRateLimit_Type.__name__=_C
_LightStreamBrPortBcastRateLimit_Object=MibTableColumn
lightStreamBrPortBcastRateLimit=_LightStreamBrPortBcastRateLimit_Object((1,3,6,1,4,1,711,3,1,1,1,3),_LightStreamBrPortBcastRateLimit_Type())
lightStreamBrPortBcastRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrPortBcastRateLimit.setStatus(_A)
_LightStreamBrPortDroppedBcastPkts_Type=Counter32
_LightStreamBrPortDroppedBcastPkts_Object=MibTableColumn
lightStreamBrPortDroppedBcastPkts=_LightStreamBrPortDroppedBcastPkts_Object((1,3,6,1,4,1,711,3,1,1,1,4),_LightStreamBrPortDroppedBcastPkts_Type())
lightStreamBrPortDroppedBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrPortDroppedBcastPkts.setStatus(_A)
_LightStreamBridgeFilterTable_Object=MibTable
lightStreamBridgeFilterTable=_LightStreamBridgeFilterTable_Object((1,3,6,1,4,1,711,3,1,2))
if mibBuilder.loadTexts:lightStreamBridgeFilterTable.setStatus(_A)
_LightStreamBridgeFilterEntry_Object=MibTableRow
lightStreamBridgeFilterEntry=_LightStreamBridgeFilterEntry_Object((1,3,6,1,4,1,711,3,1,2,1))
lightStreamBridgeFilterEntry.setIndexNames((0,_E,_BU),(0,_E,_BV))
if mibBuilder.loadTexts:lightStreamBridgeFilterEntry.setStatus(_A)
class _LightStreamBrFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LightStreamBrFilterId_Type.__name__=_C
_LightStreamBrFilterId_Object=MibTableColumn
lightStreamBrFilterId=_LightStreamBrFilterId_Object((1,3,6,1,4,1,711,3,1,2,1,1),_LightStreamBrFilterId_Type())
lightStreamBrFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrFilterId.setStatus(_A)
_LightStreamBrFilterTokenIndex_Type=Integer32
_LightStreamBrFilterTokenIndex_Object=MibTableColumn
lightStreamBrFilterTokenIndex=_LightStreamBrFilterTokenIndex_Object((1,3,6,1,4,1,711,3,1,2,1,2),_LightStreamBrFilterTokenIndex_Type())
lightStreamBrFilterTokenIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrFilterTokenIndex.setStatus(_A)
class _LightStreamBrFilterTokenType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('operation',1),('frameField',2),('macAddrType',3),('etherType',4),('llcSAPType',5),('reserved',6),('snapOuiType',7)))
_LightStreamBrFilterTokenType_Type.__name__=_C
_LightStreamBrFilterTokenType_Object=MibTableColumn
lightStreamBrFilterTokenType=_LightStreamBrFilterTokenType_Object((1,3,6,1,4,1,711,3,1,2,1,3),_LightStreamBrFilterTokenType_Type())
lightStreamBrFilterTokenType.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrFilterTokenType.setStatus(_A)
_LightStreamBrFilterTokenValue_Type=DisplayString
_LightStreamBrFilterTokenValue_Object=MibTableColumn
lightStreamBrFilterTokenValue=_LightStreamBrFilterTokenValue_Object((1,3,6,1,4,1,711,3,1,2,1,4),_LightStreamBrFilterTokenValue_Type())
lightStreamBrFilterTokenValue.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrFilterTokenValue.setStatus(_A)
class _LightStreamBrFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('complete',1),(_U,2),('intermediateToken',4)))
_LightStreamBrFilterStatus_Type.__name__=_C
_LightStreamBrFilterStatus_Object=MibTableColumn
lightStreamBrFilterStatus=_LightStreamBrFilterStatus_Object((1,3,6,1,4,1,711,3,1,2,1,5),_LightStreamBrFilterStatus_Type())
lightStreamBrFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrFilterStatus.setStatus(_A)
_LightStreamBridgeFilterParameterTable_Object=MibTable
lightStreamBridgeFilterParameterTable=_LightStreamBridgeFilterParameterTable_Object((1,3,6,1,4,1,711,3,1,3))
if mibBuilder.loadTexts:lightStreamBridgeFilterParameterTable.setStatus(_A)
_LightStreamBridgeFilterParameterEntry_Object=MibTableRow
lightStreamBridgeFilterParameterEntry=_LightStreamBridgeFilterParameterEntry_Object((1,3,6,1,4,1,711,3,1,3,1))
lightStreamBridgeFilterParameterEntry.setIndexNames((0,_E,_BW),(0,_E,_BX))
if mibBuilder.loadTexts:lightStreamBridgeFilterParameterEntry.setStatus(_A)
_LightStreamBrFilterParmPort_Type=Integer32
_LightStreamBrFilterParmPort_Object=MibTableColumn
lightStreamBrFilterParmPort=_LightStreamBrFilterParmPort_Object((1,3,6,1,4,1,711,3,1,3,1,1),_LightStreamBrFilterParmPort_Type())
lightStreamBrFilterParmPort.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrFilterParmPort.setStatus(_A)
_LightStreamBrFilterParmFilterId_Type=Integer32
_LightStreamBrFilterParmFilterId_Object=MibTableColumn
lightStreamBrFilterParmFilterId=_LightStreamBrFilterParmFilterId_Object((1,3,6,1,4,1,711,3,1,3,1,2),_LightStreamBrFilterParmFilterId_Type())
lightStreamBrFilterParmFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrFilterParmFilterId.setStatus(_A)
_LightStreamBrFilterParmFilterPriority_Type=Integer32
_LightStreamBrFilterParmFilterPriority_Object=MibTableColumn
lightStreamBrFilterParmFilterPriority=_LightStreamBrFilterParmFilterPriority_Object((1,3,6,1,4,1,711,3,1,3,1,3),_LightStreamBrFilterParmFilterPriority_Type())
lightStreamBrFilterParmFilterPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrFilterParmFilterPriority.setStatus(_A)
_LightStreamBrFilterParmAction_Type=LightStreamFilterAction
_LightStreamBrFilterParmAction_Object=MibTableColumn
lightStreamBrFilterParmAction=_LightStreamBrFilterParmAction_Object((1,3,6,1,4,1,711,3,1,3,1,4),_LightStreamBrFilterParmAction_Type())
lightStreamBrFilterParmAction.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrFilterParmAction.setStatus(_A)
_LightStreamBrFilterParmMatchCounts_Type=Counter32
_LightStreamBrFilterParmMatchCounts_Object=MibTableColumn
lightStreamBrFilterParmMatchCounts=_LightStreamBrFilterParmMatchCounts_Object((1,3,6,1,4,1,711,3,1,3,1,5),_LightStreamBrFilterParmMatchCounts_Type())
lightStreamBrFilterParmMatchCounts.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrFilterParmMatchCounts.setStatus(_A)
_LightStreamBrFilterParmValidation_Type=LightStreamValidation
_LightStreamBrFilterParmValidation_Object=MibTableColumn
lightStreamBrFilterParmValidation=_LightStreamBrFilterParmValidation_Object((1,3,6,1,4,1,711,3,1,3,1,6),_LightStreamBrFilterParmValidation_Type())
lightStreamBrFilterParmValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamBrFilterParmValidation.setStatus(_A)
_LightStreamBrStaticGoToCardSize_Type=Integer32
_LightStreamBrStaticGoToCardSize_Object=MibScalar
lightStreamBrStaticGoToCardSize=_LightStreamBrStaticGoToCardSize_Object((1,3,6,1,4,1,711,3,1,4),_LightStreamBrStaticGoToCardSize_Type())
lightStreamBrStaticGoToCardSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamBrStaticGoToCardSize.setStatus(_A)
_LightStreamVli_ObjectIdentity=ObjectIdentity
lightStreamVli=_LightStreamVli_ObjectIdentity((1,3,6,1,4,1,711,4))
class _LightStreamVliVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('version-1',1))
_LightStreamVliVersion_Type.__name__=_C
_LightStreamVliVersion_Object=MibScalar
lightStreamVliVersion=_LightStreamVliVersion_Object((1,3,6,1,4,1,711,4,1),_LightStreamVliVersion_Type())
lightStreamVliVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamVliVersion.setStatus(_A)
_LightStreamVliPortCtlTable_Object=MibTable
lightStreamVliPortCtlTable=_LightStreamVliPortCtlTable_Object((1,3,6,1,4,1,711,4,4))
if mibBuilder.loadTexts:lightStreamVliPortCtlTable.setStatus(_A)
_LightStreamVliPortCtlEntry_Object=MibTableRow
lightStreamVliPortCtlEntry=_LightStreamVliPortCtlEntry_Object((1,3,6,1,4,1,711,4,4,1))
lightStreamVliPortCtlEntry.setIndexNames((0,_E,_BY))
if mibBuilder.loadTexts:lightStreamVliPortCtlEntry.setStatus(_A)
_LightStreamVliPortCtlPort_Type=Integer32
_LightStreamVliPortCtlPort_Object=MibTableColumn
lightStreamVliPortCtlPort=_LightStreamVliPortCtlPort_Object((1,3,6,1,4,1,711,4,4,1,1),_LightStreamVliPortCtlPort_Type())
lightStreamVliPortCtlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamVliPortCtlPort.setStatus(_A)
class _LightStreamVliPortCtlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_LightStreamVliPortCtlMode_Type.__name__=_C
_LightStreamVliPortCtlMode_Object=MibTableColumn
lightStreamVliPortCtlMode=_LightStreamVliPortCtlMode_Object((1,3,6,1,4,1,711,4,4,1,2),_LightStreamVliPortCtlMode_Type())
lightStreamVliPortCtlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamVliPortCtlMode.setStatus(_A)
_LightStreamVliPortWorkGroupTable_Object=MibTable
lightStreamVliPortWorkGroupTable=_LightStreamVliPortWorkGroupTable_Object((1,3,6,1,4,1,711,4,5))
if mibBuilder.loadTexts:lightStreamVliPortWorkGroupTable.setStatus(_A)
_LightStreamVliPortWorkGroupEntry_Object=MibTableRow
lightStreamVliPortWorkGroupEntry=_LightStreamVliPortWorkGroupEntry_Object((1,3,6,1,4,1,711,4,5,1))
lightStreamVliPortWorkGroupEntry.setIndexNames((0,_E,_BZ),(0,_E,_Ba))
if mibBuilder.loadTexts:lightStreamVliPortWorkGroupEntry.setStatus(_A)
_LightStreamVliPortWorkGroupPort_Type=Integer32
_LightStreamVliPortWorkGroupPort_Object=MibTableColumn
lightStreamVliPortWorkGroupPort=_LightStreamVliPortWorkGroupPort_Object((1,3,6,1,4,1,711,4,5,1,1),_LightStreamVliPortWorkGroupPort_Type())
lightStreamVliPortWorkGroupPort.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamVliPortWorkGroupPort.setStatus(_A)
class _LightStreamVliPortWorkGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LightStreamVliPortWorkGroupID_Type.__name__=_C
_LightStreamVliPortWorkGroupID_Object=MibTableColumn
lightStreamVliPortWorkGroupID=_LightStreamVliPortWorkGroupID_Object((1,3,6,1,4,1,711,4,5,1,2),_LightStreamVliPortWorkGroupID_Type())
lightStreamVliPortWorkGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamVliPortWorkGroupID.setStatus(_A)
_LightStreamVliPortWorkGroupValidation_Type=LightStreamValidation
_LightStreamVliPortWorkGroupValidation_Object=MibTableColumn
lightStreamVliPortWorkGroupValidation=_LightStreamVliPortWorkGroupValidation_Object((1,3,6,1,4,1,711,4,5,1,3),_LightStreamVliPortWorkGroupValidation_Type())
lightStreamVliPortWorkGroupValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:lightStreamVliPortWorkGroupValidation.setStatus(_A)
_LightStreamEOM_ObjectIdentity=ObjectIdentity
lightStreamEOM=_LightStreamEOM_ObjectIdentity((1,3,6,1,4,1,711,1000))
_LightStreamEndOfMib_Type=Integer32
_LightStreamEndOfMib_Object=MibScalar
lightStreamEndOfMib=_LightStreamEndOfMib_Object((1,3,6,1,4,1,711,1000,1),_LightStreamEndOfMib_Type())
lightStreamEndOfMib.setMaxAccess(_B)
if mibBuilder.loadTexts:lightStreamEndOfMib.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'LightStreamStatus':LightStreamStatus,'LightStreamValidation':LightStreamValidation,_BT:LightStreamFilterAction,'LightStreamUpToMaxAge':LightStreamUpToMaxAge,'LightStreamDLCI':LightStreamDLCI,'VCI':VCI,'lightStream':lightStream,'lightStreamOIDs':lightStreamOIDs,'lightStreamATM':lightStreamATM,'lsOther':lsOther,'lsTrapNumber':lsTrapNumber,'lsTrapText':lsTrapText,'lsTrapName':lsTrapName,'lsConfig':lsConfig,'lightStreamProducts':lightStreamProducts,'atmSwitch':atmSwitch,'chassisInfo':chassisInfo,'chassisId':chassisId,'chassisActiveIpAddr':chassisActiveIpAddr,'chassisSecondaryIpAddr':chassisSecondaryIpAddr,'chassisNetworkMask':chassisNetworkMask,'chassisEthernetIpAddr':chassisEthernetIpAddr,'chassisEthernetIpMask':chassisEthernetIpMask,'chassisDefaultIpRouter':chassisDefaultIpRouter,'chassisStatusWord':chassisStatusWord,'chassisConsoleTrapLevel':chassisConsoleTrapLevel,'cardInfo':cardInfo,'cardTable':cardTable,'cardEntry':cardEntry,_o:cardIndex,'cardName':cardName,'cardBoardType':cardBoardType,'cardLcSoftwareVersion':cardLcSoftwareVersion,'cardLccSoftwareVersion':cardLccSoftwareVersion,'cardPID':cardPID,'cardMaxVCs':cardMaxVCs,'cardOperStatus':cardOperStatus,'cardAdminStatus':cardAdminStatus,'cardStatusWord':cardStatusWord,'cardConfigRegister':cardConfigRegister,'portInfo':portInfo,'portInfoTable':portInfoTable,'portInfoEntry':portInfoEntry,_p:portInfoIndex,'portInfoType':portInfoType,'portInfoSpecific':portInfoSpecific,'portInfoName':portInfoName,'portInfoErrorLimit':portInfoErrorLimit,'portTransmission':portTransmission,'ls1InfoTable':ls1InfoTable,'ls1InfoEntry':ls1InfoEntry,_A7:ls1InfoIfIndex,'ls1InfoType':ls1InfoType,'ls1InfoOperCsuType':ls1InfoOperCsuType,'ls1InfoAdminCsuType':ls1InfoAdminCsuType,'ls1InfoOperRcvBaudRate':ls1InfoOperRcvBaudRate,'ls1InfoAdminRcvBaudRate':ls1InfoAdminRcvBaudRate,'ls1InfoOperXmitBaudRate':ls1InfoOperXmitBaudRate,'ls1InfoAdminXmitBaudRate':ls1InfoAdminXmitBaudRate,'ls1InfoOperNetIntType':ls1InfoOperNetIntType,'ls1InfoAdminNetIntType':ls1InfoAdminNetIntType,'ls1InfoOperModemState':ls1InfoOperModemState,'ls1InfoOperProtocol':ls1InfoOperProtocol,'ls1InfoAdminProtocol':ls1InfoAdminProtocol,'ls1InfoOperControlBandwidthSize':ls1InfoOperControlBandwidthSize,'ls1InfoAdminControlBandwidthSize':ls1InfoAdminControlBandwidthSize,'ls1InfoOperDataBandwidthSize':ls1InfoOperDataBandwidthSize,'ls1InfoAdminDataBandwidthSize':ls1InfoAdminDataBandwidthSize,'ls1InfoOperLoopMode':ls1InfoOperLoopMode,'ls1InfoAdminLoopMode':ls1InfoAdminLoopMode,'ls1InfoLcAutoEnable':ls1InfoLcAutoEnable,'ls1InfoLcDebugLevel':ls1InfoLcDebugLevel,'ls1InfoDataCellCapacity':ls1InfoDataCellCapacity,'ls1InfoDataCellAvailable':ls1InfoDataCellAvailable,'ls1InfoMeasuredBaudRate':ls1InfoMeasuredBaudRate,'ls1InfoLinkUtilization':ls1InfoLinkUtilization,'ls1InfoAdminOperTrigger':ls1InfoAdminOperTrigger,'ms1InfoTable':ms1InfoTable,'ms1InfoEntry':ms1InfoEntry,_AB:ms1InfoIfIndex,'ms1InfoOperCableLength':ms1InfoOperCableLength,'ms1InfoAdminCableLength':ms1InfoAdminCableLength,'ms1InfoOperProtocol':ms1InfoOperProtocol,'ms1InfoAdminProtocol':ms1InfoAdminProtocol,'ms1InfoOperControlBandwidthSize':ms1InfoOperControlBandwidthSize,'ms1InfoAdminControlBandwidthSize':ms1InfoAdminControlBandwidthSize,'ms1InfoOperDataBandwidthSize':ms1InfoOperDataBandwidthSize,'ms1InfoAdminDataBandwidthSize':ms1InfoAdminDataBandwidthSize,'ms1InfoLcAutoEnable':ms1InfoLcAutoEnable,'ms1InfoLcDebugLevel':ms1InfoLcDebugLevel,'ms1InfoOperScramble':ms1InfoOperScramble,'ms1InfoAdminScramble':ms1InfoAdminScramble,'ms1InfoDataCellCapacity':ms1InfoDataCellCapacity,'ms1InfoDataCellAvailable':ms1InfoDataCellAvailable,'ms1InfoLinkUtilization':ms1InfoLinkUtilization,'ms1InfoOperFraming':ms1InfoOperFraming,'ms1InfoAdminOperTrigger':ms1InfoAdminOperTrigger,'npInfoTable':npInfoTable,'npInfoEntry':npInfoEntry,_AK:npInfoIfIndex,'npInfoIPCommittedRate':npInfoIPCommittedRate,'npInfoIPCommittedBurst':npInfoIPCommittedBurst,'npInfoIPExcessRate':npInfoIPExcessRate,'npInfoIPExcessBurst':npInfoIPExcessBurst,'npInfoIPNCircuits':npInfoIPNCircuits,'npInfoAdminOperTrigger':npInfoAdminOperTrigger,'clc1InfoTable':clc1InfoTable,'clc1InfoEntry':clc1InfoEntry,_AL:clc1InfoIfIndex,'clc1InfoOperProtocol':clc1InfoOperProtocol,'clc1InfoAdminProtocol':clc1InfoAdminProtocol,'clc1InfoOperLoopMode':clc1InfoOperLoopMode,'clc1InfoAdminLoopMode':clc1InfoAdminLoopMode,'clc1InfoOperControlBandwidthSize':clc1InfoOperControlBandwidthSize,'clc1InfoAdminControlBandwidthSize':clc1InfoAdminControlBandwidthSize,'clc1InfoOperDataBandwidthSize':clc1InfoOperDataBandwidthSize,'clc1InfoAdminDataBandwidthSize':clc1InfoAdminDataBandwidthSize,'clc1InfoLcAutoEnable':clc1InfoLcAutoEnable,'clc1InfoLcDebugLevel':clc1InfoLcDebugLevel,'clc1InfoOperScramble':clc1InfoOperScramble,'clc1InfoAdminScramble':clc1InfoAdminScramble,'clc1InfoDataCellCapacity':clc1InfoDataCellCapacity,'clc1InfoDataCellAvailable':clc1InfoDataCellAvailable,'clc1InfoLinkUtilization':clc1InfoLinkUtilization,'clc1InfoOperClock':clc1InfoOperClock,'clc1InfoAdminClock':clc1InfoAdminClock,'clc1InfoAdminOperTrigger':clc1InfoAdminOperTrigger,'oc3InfoTable':oc3InfoTable,'oc3InfoEntry':oc3InfoEntry,'oc3InfoReceiveSignalDetect':oc3InfoReceiveSignalDetect,'oc3InfoTransmitSafetySwitch':oc3InfoTransmitSafetySwitch,'oc3InfoMediumType':oc3InfoMediumType,'congestionAvoidance':congestionAvoidance,'caMaxIntervalPermitLimit':caMaxIntervalPermitLimit,'caMinIntervalPermitLimit':caMinIntervalPermitLimit,'caMinIntervalCaInfo':caMinIntervalCaInfo,'mmaInfo':mmaInfo,'mmaDbActive':mmaDbActive,'mmaTrapFilter':mmaTrapFilter,'mmaTrapLanguage':mmaTrapLanguage,'mmaCollectionSpace':mmaCollectionSpace,'mmaConfigHost':mmaConfigHost,'mmaConfigAuthor':mmaConfigAuthor,'mmaConfigID':mmaConfigID,'mmaSetLock':mmaSetLock,'mmaPID':mmaPID,'mmaTrapLog':mmaTrapLog,'mmaTrapNumber':mmaTrapNumber,'mmaTrapOnOffState':mmaTrapOnOffState,'mmaNumNameTable':mmaNumNameTable,'mmaNumNameEntry':mmaNumNameEntry,_AQ:mmaNumNameNumber,'mmaNumName':mmaNumName,'mmaLwmpTimeouts':mmaLwmpTimeouts,'collectInfo':collectInfo,'collectTable':collectTable,'collectEntry':collectEntry,_AR:collectIndex,'collectStatus':collectStatus,'collectStart':collectStart,'collectFinish':collectFinish,'collectInterval':collectInterval,'collectFileName':collectFileName,'collectFileSize':collectFileSize,'collectOperStatus':collectOperStatus,'collectDataBase':collectDataBase,'collectDbEntry':collectDbEntry,_AS:collectDBIndex,_AT:collectDBInstance,'collectDBObjectID':collectDBObjectID,'collectDBStatus':collectDBStatus,'collectCommunityName':collectCommunityName,'rmonCommunityName':rmonCommunityName,'lsPortProtocols':lsPortProtocols,'edgePort':edgePort,'edgePortTable':edgePortTable,'edgePortEntry':edgePortEntry,_AU:edgeIfIndex,'edgeUpcType':edgeUpcType,'edgeUserDataPerCell':edgeUserDataPerCell,'edgeCellDelayVariance':edgeCellDelayVariance,'edgePrincipalScale':edgePrincipalScale,'edgeSecondaryScale':edgeSecondaryScale,'edgeMeteringFactor':edgeMeteringFactor,'edgeMeteringBurstSize':edgeMeteringBurstSize,'edgeCallSetupRetry':edgeCallSetupRetry,'edgeCallSetupBackoff':edgeCallSetupBackoff,'edgeMaxFrameSize':edgeMaxFrameSize,'frDceInfo':frDceInfo,'frProvMiTable':frProvMiTable,'frProvMiEntry':frProvMiEntry,_AV:frProvMiIfIndex,'frProvMiState':frProvMiState,'frProvMiAddressLen':frProvMiAddressLen,'frProvMiNetRequestInterval':frProvMiNetRequestInterval,'frProvMiNetErrorThreshold':frProvMiNetErrorThreshold,'frProvMiNetMonitoredEvents':frProvMiNetMonitoredEvents,'frProvMiMaxSupportedVCs':frProvMiMaxSupportedVCs,'frProvMiMulticast':frProvMiMulticast,'frProvMiUserPollingInterval':frProvMiUserPollingInterval,'frProvMiUserFullEnquiryInterval':frProvMiUserFullEnquiryInterval,'frProvMiUserErrorThreshold':frProvMiUserErrorThreshold,'frProvMiUserMonitoredEvents':frProvMiUserMonitoredEvents,'frProvMiNetInterfaceType':frProvMiNetInterfaceType,'frCktInfo':frCktInfo,'frCktCfgTable':frCktCfgTable,'frCktEntry':frCktEntry,'frCktSrcNode':frCktSrcNode,_AW:frCktSrcIfIndex,_AX:frCktSrcDlci,'frCktAdminDestNode':frCktAdminDestNode,'frCktOperDestNode':frCktOperDestNode,'frCktAdminDestIfIndex':frCktAdminDestIfIndex,'frCktOperDestIfIndex':frCktOperDestIfIndex,'frCktAdminDestDlci':frCktAdminDestDlci,'frCktOperDestDlci':frCktOperDestDlci,'frCktAdminSrcInsuredRate':frCktAdminSrcInsuredRate,'frCktOperSrcInsuredRate':frCktOperSrcInsuredRate,'frCktAdminSrcInsuredBurst':frCktAdminSrcInsuredBurst,'frCktOperSrcInsuredBurst':frCktOperSrcInsuredBurst,'frCktAdminSrcMaxRate':frCktAdminSrcMaxRate,'frCktOperSrcMaxRate':frCktOperSrcMaxRate,'frCktAdminSrcMaxBurst':frCktAdminSrcMaxBurst,'frCktOperSrcMaxBurst':frCktOperSrcMaxBurst,'frCktAdminDestInsuredRate':frCktAdminDestInsuredRate,'frCktOperDestInsuredRate':frCktOperDestInsuredRate,'frCktAdminDestInsuredBurst':frCktAdminDestInsuredBurst,'frCktOperDestInsuredBurst':frCktOperDestInsuredBurst,'frCktAdminDestMaxRate':frCktAdminDestMaxRate,'frCktOperDestMaxRate':frCktOperDestMaxRate,'frCktAdminDestMaxBurst':frCktAdminDestMaxBurst,'frCktOperDestMaxBurst':frCktOperDestMaxBurst,'frCktOperSecondaryScale':frCktOperSecondaryScale,'frCktAdminSecondaryScale':frCktAdminSecondaryScale,'frCktOperPrinBwType':frCktOperPrinBwType,'frCktAdminPrinBwType':frCktAdminPrinBwType,'frCktOperTransPri':frCktOperTransPri,'frCktAdminTransPri':frCktAdminTransPri,'frCktOperUserDataPerCell':frCktOperUserDataPerCell,'frCktAdminUserDataPerCell':frCktAdminUserDataPerCell,'frCktStatus':frCktStatus,'frCktInfoTable':frCktInfoTable,'frCktInfoEntry':frCktInfoEntry,_AY:frCktInfoIfIndex,_AZ:frCktInfoDlci,'frCktInfoLclLMI':frCktInfoLclLMI,'frCktInfoRmtLMI':frCktInfoRmtLMI,'frCktInfoCallIDIncoming':frCktInfoCallIDIncoming,'frCktInfoCallIDOutgoing':frCktInfoCallIDOutgoing,'frCktInfoDownstreamState':frCktInfoDownstreamState,'frCktInfoUpstreamState':frCktInfoUpstreamState,'frCktInfoLastAtmErr':frCktInfoLastAtmErr,'frCktInfoDataCellsRequired':frCktInfoDataCellsRequired,'frCktInfoLastAtmLocation':frCktInfoLastAtmLocation,'ffCktInfo':ffCktInfo,'ffCktCfgTable':ffCktCfgTable,'ffCktEntry':ffCktEntry,'ffCktSrcNode':ffCktSrcNode,_Aa:ffCktSrcIfIndex,'ffCktAdminDestNode':ffCktAdminDestNode,'ffCktOperDestNode':ffCktOperDestNode,'ffCktAdminDestIfIndex':ffCktAdminDestIfIndex,'ffCktOperDestIfIndex':ffCktOperDestIfIndex,'ffCktAdminSrcInsuredRate':ffCktAdminSrcInsuredRate,'ffCktOperSrcInsuredRate':ffCktOperSrcInsuredRate,'ffCktAdminSrcInsuredBurst':ffCktAdminSrcInsuredBurst,'ffCktOperSrcInsuredBurst':ffCktOperSrcInsuredBurst,'ffCktAdminSrcMaxRate':ffCktAdminSrcMaxRate,'ffCktOperSrcMaxRate':ffCktOperSrcMaxRate,'ffCktAdminSrcMaxBurst':ffCktAdminSrcMaxBurst,'ffCktOperSrcMaxBurst':ffCktOperSrcMaxBurst,'ffCktAdminDestInsuredRate':ffCktAdminDestInsuredRate,'ffCktOperDestInsuredRate':ffCktOperDestInsuredRate,'ffCktAdminDestInsuredBurst':ffCktAdminDestInsuredBurst,'ffCktOperDestInsuredBurst':ffCktOperDestInsuredBurst,'ffCktAdminDestMaxRate':ffCktAdminDestMaxRate,'ffCktOperDestMaxRate':ffCktOperDestMaxRate,'ffCktAdminDestMaxBurst':ffCktAdminDestMaxBurst,'ffCktOperDestMaxBurst':ffCktOperDestMaxBurst,'ffCktOperPrinBwType':ffCktOperPrinBwType,'ffCktAdminPrinBwType':ffCktAdminPrinBwType,'ffCktOperTransPri':ffCktOperTransPri,'ffCktAdminTransPri':ffCktAdminTransPri,'ffCktStatus':ffCktStatus,'ffCktInfoTable':ffCktInfoTable,'ffCktInfoEntry':ffCktInfoEntry,_Ab:ffCktInfoIfIndex,'ffCktInfoDownstreamState':ffCktInfoDownstreamState,'ffCktInfoUpstreamState':ffCktInfoUpstreamState,'ffCktInfoCallIDIncoming':ffCktInfoCallIDIncoming,'ffCktInfoCallIDOutgoing':ffCktInfoCallIDOutgoing,'ffCktInfoLastAtmErr':ffCktInfoLastAtmErr,'ffCktInfoDataCellsRequired':ffCktInfoDataCellsRequired,'ffCktInfoLastAtmLocation':ffCktInfoLastAtmLocation,'sUniCktInfo':sUniCktInfo,'sUniCktCfgTable':sUniCktCfgTable,'sUniCktEntry':sUniCktEntry,'sUniCktSrcNode':sUniCktSrcNode,_Ac:sUniCktSrcIfIndex,_Ad:sUniCktSrcVCI,'sUniCktAdminDestNode':sUniCktAdminDestNode,'sUniCktOperDestNode':sUniCktOperDestNode,'sUniCktAdminDestIfIndex':sUniCktAdminDestIfIndex,'sUniCktOperDestIfIndex':sUniCktOperDestIfIndex,'sUniCktAdminDestVCI':sUniCktAdminDestVCI,'sUniCktOperDestVCI':sUniCktOperDestVCI,'sUniCktOperPrinBwType':sUniCktOperPrinBwType,'sUniCktAdminPrinBwType':sUniCktAdminPrinBwType,'sUniCktOperTransPri':sUniCktOperTransPri,'sUniCktAdminTransPri':sUniCktAdminTransPri,'sUniCktAdminSrcInsuredRate':sUniCktAdminSrcInsuredRate,'sUniCktOperSrcInsuredRate':sUniCktOperSrcInsuredRate,'sUniCktAdminSrcInsuredBurst':sUniCktAdminSrcInsuredBurst,'sUniCktOperSrcInsuredBurst':sUniCktOperSrcInsuredBurst,'sUniCktAdminSrcMaxRate':sUniCktAdminSrcMaxRate,'sUniCktOperSrcMaxRate':sUniCktOperSrcMaxRate,'sUniCktAdminSrcMaxBurst':sUniCktAdminSrcMaxBurst,'sUniCktOperSrcMaxBurst':sUniCktOperSrcMaxBurst,'sUniCktAdminDestInsuredRate':sUniCktAdminDestInsuredRate,'sUniCktOperDestInsuredRate':sUniCktOperDestInsuredRate,'sUniCktAdminDestInsuredBurst':sUniCktAdminDestInsuredBurst,'sUniCktOperDestInsuredBurst':sUniCktOperDestInsuredBurst,'sUniCktAdminDestMaxRate':sUniCktAdminDestMaxRate,'sUniCktOperDestMaxRate':sUniCktOperDestMaxRate,'sUniCktAdminDestMaxBurst':sUniCktAdminDestMaxBurst,'sUniCktOperDestMaxBurst':sUniCktOperDestMaxBurst,'sUniCktAdminSecondaryScale':sUniCktAdminSecondaryScale,'sUniCktOperSecondaryScale':sUniCktOperSecondaryScale,'sUniCktSts':sUniCktSts,'sUniCktInfoTable':sUniCktInfoTable,'sUniCktInfoEntry':sUniCktInfoEntry,_Ae:sUniCktInfoIfIndex,_Af:sUniCktInfoVCI,'sUniCktInfoUniToNetCallID':sUniCktInfoUniToNetCallID,'sUniCktInfoNetToUniCallID':sUniCktInfoNetToUniCallID,'sUniCktInfoUniToNetState':sUniCktInfoUniToNetState,'sUniCktInfoNetToUniState':sUniCktInfoNetToUniState,'sUniCktInfoLastAtmErr':sUniCktInfoLastAtmErr,'sUniCktInfoDataCellsRequired':sUniCktInfoDataCellsRequired,'sUniCktInfoLastAtmLocation':sUniCktInfoLastAtmLocation,'pvcInfo':pvcInfo,'pvcCfgTable':pvcCfgTable,'pvcEntry':pvcEntry,_Ag:pvcSrcIfIndex,_Ah:pvcSrcPvcId,'pvcSrcNode':pvcSrcNode,'pvcSrcInsuredRate':pvcSrcInsuredRate,'pvcSrcInsuredBurst':pvcSrcInsuredBurst,'pvcSrcMaxRate':pvcSrcMaxRate,'pvcSrcMaxBurst':pvcSrcMaxBurst,'pvcSecondaryScale':pvcSecondaryScale,'pvcPrinBwType':pvcPrinBwType,'pvcTransPri':pvcTransPri,'pvcUserDataPerCell':pvcUserDataPerCell,'pvcStatus':pvcStatus,'mcEndptInfo':mcEndptInfo,'mcEndptCfgTable':mcEndptCfgTable,'mcEndptEntry':mcEndptEntry,_Ai:mcEndptLclIfIndex,_Aj:mcEndptLclCktid,_Ak:mcEndptLclInstance,'mcEndptDest':mcEndptDest,'mcEndptServiceType':mcEndptServiceType,'mcEndptRmtVCstatus':mcEndptRmtVCstatus,'mcEndptCallIDIncoming':mcEndptCallIDIncoming,'mcEndptDownstreamState':mcEndptDownstreamState,'mcEndptUpstreamState':mcEndptUpstreamState,'mcEndptLastAtmErr':mcEndptLastAtmErr,'mcEndptLastAtmLocation':mcEndptLastAtmLocation,'mcEndptStatus':mcEndptStatus,'lsPrivate':lsPrivate,'lsExperimental':lsExperimental,'lsExperimentalStatistics':lsExperimentalStatistics,'lsEdgeStatistics':lsEdgeStatistics,'lsEdgeStatTable':lsEdgeStatTable,'lsEdgeStatEntry':lsEdgeStatEntry,_Al:edgeStatIndex,'edgeStatFsuRATOs':edgeStatFsuRATOs,'edgeStatFsuRATOLastInfo':edgeStatFsuRATOLastInfo,'edgeStatTsuHoldQCells':edgeStatTsuHoldQCells,'edgeStatTsuHoldQs':edgeStatTsuHoldQs,'tluAAL5XsumErrs':tluAAL5XsumErrs,'tluAAL5AbortErrs':tluAAL5AbortErrs,'tluAAL5ErrLastVci':tluAAL5ErrLastVci,'lsEdgePortStatTable':lsEdgePortStatTable,'lsEdgePortStatEntry':lsEdgePortStatEntry,_Am:edgePortStatIndex,'edgePortRcvOctets':edgePortRcvOctets,'edgePortXmtOctets':edgePortXmtOctets,'edgePortFsuCksmErrMsgs':edgePortFsuCksmErrMsgs,'edgePortCksmErrLastVci':edgePortCksmErrLastVci,'edgePortDownXmtFrames':edgePortDownXmtFrames,'edgePortRcvUcastPkts':edgePortRcvUcastPkts,'edgePortRcvNUcastPkts':edgePortRcvNUcastPkts,'edgePortXmtUcastPkts':edgePortXmtUcastPkts,'edgePortXmtNUcastPkts':edgePortXmtNUcastPkts,'edgePortRcvSmplPktSize':edgePortRcvSmplPktSize,'edgePortXmtSmplPktSize':edgePortXmtSmplPktSize,'edgePortRcvL3XsumErrs':edgePortRcvL3XsumErrs,'edgePortRcvL3XsumErrLastVci':edgePortRcvL3XsumErrLastVci,'edgePortRcvCRCErrors':edgePortRcvCRCErrors,'edgePortRcvAborts':edgePortRcvAborts,'edgePortXmtUnderflows':edgePortXmtUnderflows,'edgePortRcvShortFrames':edgePortRcvShortFrames,'lsFrameRelayDlciStatTable':lsFrameRelayDlciStatTable,'lsFrameRelayDlciStatEntry':lsFrameRelayDlciStatEntry,_An:frameRelayDlciStatPortIndex,_Ao:frameRelayDlciStatDlciIndex,'frameRelayDlciToSwCLP0Frames':frameRelayDlciToSwCLP0Frames,'frameRelayDlciToSwCLP0Cells':frameRelayDlciToSwCLP0Cells,'frameRelayDlciToSwCLP1Frames':frameRelayDlciToSwCLP1Frames,'frameRelayDlciToSwCLP1Cells':frameRelayDlciToSwCLP1Cells,'frameRelayDlciToSwDiscardFrames':frameRelayDlciToSwDiscardFrames,'frameRelayDlciToSwDiscardCells':frameRelayDlciToSwDiscardCells,'frameRelayDlciFrSwCLP0Frames':frameRelayDlciFrSwCLP0Frames,'frameRelayDlciFrSwCLP0Cells':frameRelayDlciFrSwCLP0Cells,'frameRelayDlciFrSwCLP1Frames':frameRelayDlciFrSwCLP1Frames,'frameRelayDlciFrSwCLP1Cells':frameRelayDlciFrSwCLP1Cells,'lsEdgePortToSwMsgLenTable':lsEdgePortToSwMsgLenTable,'lsEdgePortToSwMsgLenEntry':lsEdgePortToSwMsgLenEntry,_Ap:edgeToSwMsgLenPortIndex,_Aq:edgeToSwMsgLenBinIndex,'edgeToSwMsgLenMsgs':edgeToSwMsgLenMsgs,'lsEdgeSwToPortMsgLenTable':lsEdgeSwToPortMsgLenTable,'lsEdgeSwToPortMsgLenEntry':lsEdgeSwToPortMsgLenEntry,_Ar:edgeToPortMsgLenPortIndex,_As:edgeToPortMsgLenBinIndex,'edgeToPortMsgLenMsgs':edgeToPortMsgLenMsgs,'lsEdgeCpuWorkloadTable':lsEdgeCpuWorkloadTable,'lsEdgeCpuWorkloadEntry':lsEdgeCpuWorkloadEntry,_At:lsEdgeWorkloadCardIndex,_Au:lsEdgeWorkloadTypeIndex,'lsEdgeWorkloadEvents':lsEdgeWorkloadEvents,'lsFrameForwardStatTable':lsFrameForwardStatTable,'lsFrameForwardStatEntry':lsFrameForwardStatEntry,_Av:frameForwardStatPortIndex,'frameForwardToSwCLP0Frames':frameForwardToSwCLP0Frames,'frameForwardToSwCLP0Cells':frameForwardToSwCLP0Cells,'frameForwardToSwCLP1Frames':frameForwardToSwCLP1Frames,'frameForwardToSwCLP1Cells':frameForwardToSwCLP1Cells,'frameForwardToSwDiscardFrames':frameForwardToSwDiscardFrames,'frameForwardToSwDiscardCells':frameForwardToSwDiscardCells,'frameForwardFrSwCLP0Frames':frameForwardFrSwCLP0Frames,'frameForwardFrSwCLP0Cells':frameForwardFrSwCLP0Cells,'frameForwardFrSwCLP1Frames':frameForwardFrSwCLP1Frames,'frameForwardFrSwCLP1Cells':frameForwardFrSwCLP1Cells,'lsTrunkStatistics':lsTrunkStatistics,'lsTrunkPortStatTable':lsTrunkPortStatTable,'lsTrunkPortStatEntry':lsTrunkPortStatEntry,_Aw:trunkPortStatIndex,'trunkPortRcvCells':trunkPortRcvCells,'trunkPortXmtCells':trunkPortXmtCells,'trunkPortRcvRuns':trunkPortRcvRuns,'trunkPortDownXmtCells':trunkPortDownXmtCells,'trunkPortRcvCRCErrors':trunkPortRcvCRCErrors,'trunkPortRcvAborts':trunkPortRcvAborts,'trunkPortXmtUnderflows':trunkPortXmtUnderflows,'trunkPortRcvShortFrames':trunkPortRcvShortFrames,'lsTrunkCpuWorkloadTable':lsTrunkCpuWorkloadTable,'lsTrunkCpuWorkloadEntry':lsTrunkCpuWorkloadEntry,_Ax:lsTrunkWorkloadCardIndex,_Ay:lsTrunkWorkloadTypeIndex,'lsTrunkWorkloadEvents':lsTrunkWorkloadEvents,'lsLcStatistics':lsLcStatistics,'lcStatTable':lcStatTable,'lcStatEntry':lcStatEntry,_Az:lcStatCardIndex,'tsuFreeCells':tsuFreeCells,'fsuSharedFreeCells':fsuSharedFreeCells,'tsuCellDropLastVci':tsuCellDropLastVci,'switchCellDgRejectEvents':switchCellDgRejectEvents,'switchCellSchedRejectEvents':switchCellSchedRejectEvents,'tsuErrFutQCellDrops':tsuErrFutQCellDrops,'tsuErrFutQMsgDropLastVci':tsuErrFutQMsgDropLastVci,'fsuHdrLrcErrs':fsuHdrLrcErrs,'fsuPayloadLrcErrs':fsuPayloadLrcErrs,'lcPortStatTable':lcPortStatTable,'lcPortStatEntry':lcPortStatEntry,_A_:lcStatPortIndex,'fsuPortFreeCells':fsuPortFreeCells,'fsuCellDropLastCellHdr':fsuCellDropLastCellHdr,'tsuPortErrL1UnconfigVcis':tsuPortErrL1UnconfigVcis,'tsuPortErrL2UnconfigVcis':tsuPortErrL2UnconfigVcis,'tsuPortErrL1UnconfigLastVci':tsuPortErrL1UnconfigLastVci,'tsuPortErrL2UnconfigLastVci':tsuPortErrL2UnconfigLastVci,'tsuPortErrNonZeroGfc':tsuPortErrNonZeroGfc,'fsuPortXmtCellsTable':fsuPortXmtCellsTable,'fsuPortXmtCellsEntry':fsuPortXmtCellsEntry,_B0:fsuXmtCellsPortIndex,_B1:fsuXmtCellsPriorityIndex,'fsuXmtCellEvents':fsuXmtCellEvents,'fsuQueueCellLengthTable':fsuQueueCellLengthTable,'fsuQueueCellLenEntry':fsuQueueCellLenEntry,_B2:fsuQueueCellLenPortIndex,_B3:fsuQueueCellLenSubQIndex,'fsuQueueCellLength':fsuQueueCellLength,'fsuDropEventTable':fsuDropEventTable,'fsuDropEventEntry':fsuDropEventEntry,_B4:fsuDropEventPortIndex,_B5:fsuDropEventWatermarkIndex,'fsuDropEvents':fsuDropEvents,'lsFsuFastDropTable':lsFsuFastDropTable,'lsFsuFastDropEntry':lsFsuFastDropEntry,_B6:lsFsuFastDropWatermarkIndex,'lsFsuFastCellDropEvents':lsFsuFastCellDropEvents,'tsuDropEventTable':tsuDropEventTable,'tsuDropEventEntry':tsuDropEventEntry,_B7:tsuDropEventPortIndex,_B8:tsuDropEventWatermarkIndex,'tsuDropEvents':tsuDropEvents,'lsUtStatistics':lsUtStatistics,'lsLcFsuIntervalTable':lsLcFsuIntervalTable,'lsLcFsuIntervalEntry':lsLcFsuIntervalEntry,_B9:lsLcIntervalPortIndex,_BA:lsLcIntervalNumber,'lsLcIntervalPSDepth':lsLcIntervalPSDepth,'lsLcIntervalASDepth':lsLcIntervalASDepth,'lsLcIntervalDropEvents':lsLcIntervalDropEvents,'lsLcIntervalAvgCells':lsLcIntervalAvgCells,'lsLcIntervalPeakCells':lsLcIntervalPeakCells,'lsLcIntervalMinPermits':lsLcIntervalMinPermits,'lsLcIntervalAvgPermits':lsLcIntervalAvgPermits,'lsLcIntervalMaxPermits':lsLcIntervalMaxPermits,'lsLcIntervalDecrPermits':lsLcIntervalDecrPermits,'lsLcIntervalIncrPermits':lsLcIntervalIncrPermits,'lsLcIntervalMinBwAlloc':lsLcIntervalMinBwAlloc,'lsLcIntervalAvgBwAlloc':lsLcIntervalAvgBwAlloc,'lsLcIntervalMaxBwAlloc':lsLcIntervalMaxBwAlloc,'lsNpStatistics':lsNpStatistics,'lsNpCpuWorkloadTable':lsNpCpuWorkloadTable,'lsNpCpuWorkloadEntry':lsNpCpuWorkloadEntry,_BB:lsNpCpuWorkloadIndex,'lsNpCpuWorkloadEvents':lsNpCpuWorkloadEvents,'lsCellStatistics':lsCellStatistics,'lsCellVciStatTable':lsCellVciStatTable,'lsCellVciStatEntry':lsCellVciStatEntry,_BC:cellVciStatPortIndex,_BD:cellVciStatVciIndex,'cellVciToSwCLP0Cells':cellVciToSwCLP0Cells,'cellVciToSwCLP01Cells':cellVciToSwCLP01Cells,'cellVciToSwCLP1Cells':cellVciToSwCLP1Cells,'cellVciToSwDiscardCells':cellVciToSwDiscardCells,'lsIR':lsIR,'irRoutingGroup':irRoutingGroup,'irRoutingPathsGenerated':irRoutingPathsGenerated,'irRoutingPathGenSuccess':irRoutingPathGenSuccess,'irRoutingPathGenFailedNoResources':irRoutingPathGenFailedNoResources,'irRoutingPathGenFailedUnknown':irRoutingPathGenFailedUnknown,'irRoutingPathGenFailedOther':irRoutingPathGenFailedOther,'irRoutingAveragePathLength':irRoutingAveragePathLength,'lsStatistics':lsStatistics,'tcsInfo':tcsInfo,'tcsTable':tcsTable,'tcsEntry':tcsEntry,'tcsIndex':tcsIndex,'tcsTemp1':tcsTemp1,'tcsTemp2':tcsTemp2,'tcsTcsVoltage':tcsTcsVoltage,'tcsVccVoltage':tcsVccVoltage,'tcsScsiVoltage':tcsScsiVoltage,'tcsPostResult':tcsPostResult,'tcsCardType':tcsCardType,'tcsPaddleTemp1':tcsPaddleTemp1,'tcsPaddleTemp2':tcsPaddleTemp2,'tcsPaddleWarnTemp1':tcsPaddleWarnTemp1,'tcsPaddleWarnTemp2':tcsPaddleWarnTemp2,'tcsPaddleShutdownTemp1':tcsPaddleShutdownTemp1,'tcsPaddleShutdownTemp2':tcsPaddleShutdownTemp2,'tcsWarnTemp1':tcsWarnTemp1,'tcsWarnTemp2':tcsWarnTemp2,'tcsShutdownTemp1':tcsShutdownTemp1,'tcsShutdownTemp2':tcsShutdownTemp2,'tcsFaultLight':tcsFaultLight,'tcsReadyLight':tcsReadyLight,'tcsSwitchConnectivityMask':tcsSwitchConnectivityMask,'tcsPrimarySwitch':tcsPrimarySwitch,'tcsPowerSupplyA':tcsPowerSupplyA,'tcsPowerSupplyB':tcsPowerSupplyB,'tcsPowerSupplyTypeA':tcsPowerSupplyTypeA,'tcsPowerSupplyTypeB':tcsPowerSupplyTypeB,'tcsSwitchFaultMaskA':tcsSwitchFaultMaskA,'tcsSwitchFaultMaskB':tcsSwitchFaultMaskB,'tcsSwitchCutoverSupport':tcsSwitchCutoverSupport,'tcsFCPrimarySwitchA':tcsFCPrimarySwitchA,'tcsFCPrimarySwitchB':tcsFCPrimarySwitchB,'lsGID':lsGID,'gidGeneralGroup':gidGeneralGroup,'gidSoftwareVersionNumber':gidSoftwareVersionNumber,'gidProcessID':gidProcessID,'gidUpTime':gidUpTime,'gidMemoryUse':gidMemoryUse,'gidTimersProcessed':gidTimersProcessed,'gidMallocFailures':gidMallocFailures,'gidDebugFlag':gidDebugFlag,'gidDebugLevel':gidDebugLevel,'gidAcceptedBcastRateIn':gidAcceptedBcastRateIn,'gidNbrGroup':gidNbrGroup,'gidNbrCount':gidNbrCount,'gidNbrTable':gidNbrTable,'gidNbrEntry':gidNbrEntry,_BF:gidNbrEIA,'gidNbrVCI':gidNbrVCI,'gidNbrState':gidNbrState,'gidNbrSyncEvents':gidNbrSyncEvents,'gidNbrDBReqListLength':gidNbrDBReqListLength,'gidNbrDBSumListLength':gidNbrDBSumListLength,'gidNbrHellosRx':gidNbrHellosRx,'gidNbrLinkAnnouncementsRx':gidNbrLinkAnnouncementsRx,'gidNbrNewLinkAnnouncementsRx':gidNbrNewLinkAnnouncementsRx,'gidNbrIPAnnouncementsRx':gidNbrIPAnnouncementsRx,'gidNbrNewIPAnnouncementsRx':gidNbrNewIPAnnouncementsRx,'gidNbrGenericAnnouncementsRx':gidNbrGenericAnnouncementsRx,'gidNbrNewGenericAnnouncementsRx':gidNbrNewGenericAnnouncementsRx,'gidClientGroup':gidClientGroup,'gidClientCount':gidClientCount,'gidClientTable':gidClientTable,'gidClientEntry':gidClientEntry,_BG:gidClientID,'gidClientEIA':gidClientEIA,'gidClientAnnouncementsRx':gidClientAnnouncementsRx,'gidClientLinkAnnouncementsRx':gidClientLinkAnnouncementsRx,'gidClientIPAnnouncementsRx':gidClientIPAnnouncementsRx,'gidClientGenericAnnouncementsRx':gidClientGenericAnnouncementsRx,'gidClientEventsTx':gidClientEventsTx,'gidClientPathsGenerated':gidClientPathsGenerated,'gidIOGroup':gidIOGroup,'gidIONbrMsgBuffersFree':gidIONbrMsgBuffersFree,'gidIONbrMsgBuffersActive':gidIONbrMsgBuffersActive,'gidIOClientMsgBuffersFree':gidIOClientMsgBuffersFree,'gidIOClientMsgBuffersActive':gidIOClientMsgBuffersActive,'gidSyncGroup':gidSyncGroup,'gidSyncNbrsExistent':gidSyncNbrsExistent,'gidSyncNbrsExStart':gidSyncNbrsExStart,'gidSyncNbrsExchange':gidSyncNbrsExchange,'gidSyncNbrsLoading':gidSyncNbrsLoading,'gidSyncNbrsFull':gidSyncNbrsFull,'gidLinkGroup':gidLinkGroup,'gidLinkDatabaseSize':gidLinkDatabaseSize,'gidLineCardTable':gidLineCardTable,'gidLineCardEntry':gidLineCardEntry,_BH:gidLineCardChassis,_BI:gidLineCardSlot,'gidLineCardEntryAge':gidLineCardEntryAge,'gidLineCardEntrySeqno':gidLineCardEntrySeqno,'gidLineCardEntryAdvNP':gidLineCardEntryAdvNP,'gidLineCardPorts':gidLineCardPorts,'gidPortTable':gidPortTable,'gidPortEntry':gidPortEntry,_BJ:gidPortChassis,_BK:gidPortID,'gidPortService':gidPortService,'gidPortUpDown':gidPortUpDown,'gidPortBW0':gidPortBW0,'gidPortBW1':gidPortBW1,'gidPortBW2':gidPortBW2,'gidPortRemoteChassis':gidPortRemoteChassis,'gidPortRemotePort':gidPortRemotePort,'gidIpAddressGroup':gidIpAddressGroup,'gidIpAddressDatabaseSize':gidIpAddressDatabaseSize,'gidIpAddressTable':gidIpAddressTable,'gidIpAddressEntry':gidIpAddressEntry,_BL:gidInternalIpAddress,'gidIpEntryAge':gidIpEntryAge,'gidIpEntrySeqno':gidIpEntrySeqno,'gidIpEntryAdvNP':gidIpEntryAdvNP,'gidIpEntryNetMask':gidIpEntryNetMask,'gidIpEntryEIA':gidIpEntryEIA,'gidEventGroup':gidEventGroup,'gidEventLinkEventsDelivered':gidEventLinkEventsDelivered,'gidEventIpEventsDelivered':gidEventIpEventsDelivered,'gidEventGenericGinfoEventsDelivered':gidEventGenericGinfoEventsDelivered,'gidEventGenericGinfoEventTable':gidEventGenericGinfoEventTable,'gidEventGenericGinfoEventCount':gidEventGenericGinfoEventCount,_BM:gidEventDistributionGroup,'gidEventGenericGinfoEvents':gidEventGenericGinfoEvents,'lsPID':lsPID,'pidTable':pidTable,'pidEntry':pidEntry,'pidIndex':pidIndex,'pidName':pidName,'pidCreationTime':pidCreationTime,'pidOperStatus':pidOperStatus,'pidAdminStatus':pidAdminStatus,'lsND':lsND,'ndGeneralGroup':ndGeneralGroup,'ndSoftwareVersionNumber':ndSoftwareVersionNumber,'ndProcessID':ndProcessID,'ndMemoryUse':ndMemoryUse,'ndTimersProcessed':ndTimersProcessed,'ndLCGroup':ndLCGroup,'ndLCCount':ndLCCount,'ndLCTable':ndLCTable,'ndLCEntry':ndLCEntry,'ndLCEIA':ndLCEIA,'ndLCChannel':ndLCChannel,'ndLCState':ndLCState,'ndNbrGroup':ndNbrGroup,'ndNbrCount':ndNbrCount,'ndNbrTable':ndNbrTable,'ndNbrEntry':ndNbrEntry,'ndNbrEIA':ndNbrEIA,'ndNbrChannel':ndNbrChannel,'ndNbrState':ndNbrState,'ndSwudGroup':ndSwudGroup,'ndSwudTable':ndSwudTable,'ndSwudEntry':ndSwudEntry,_BO:ndSwudIndex,'ndOperIntvl':ndOperIntvl,'ndOperJ':ndOperJ,'ndOperK':ndOperK,'ndOperM':ndOperM,'ndOperN':ndOperN,'ndAdminIntvl':ndAdminIntvl,'ndAdminJ':ndAdminJ,'ndAdminK':ndAdminK,'ndAdminM':ndAdminM,'ndAdminN':ndAdminN,'ndTrigger':ndTrigger,'ndSwudStatsInputErrors':ndSwudStatsInputErrors,'ndSwudStatsTable':ndSwudStatsTable,'ndSwudStatsEntry':ndSwudStatsEntry,_BP:ndSwudStatsIndex,'ndInputCells':ndInputCells,'ndInputErrs':ndInputErrs,'ndOutputCells':ndOutputCells,'ndOutputErrs':ndOutputErrs,'ndClientGroup':ndClientGroup,'ndClientCount':ndClientCount,'ndClientTable':ndClientTable,'ndClientEntry':ndClientEntry,_BQ:ndClientID,'ndClientType':ndClientType,'ndClientSubType':ndClientSubType,'ndClientEIA':ndClientEIA,'ndClientRegistration':ndClientRegistration,'ndInternalGroup':ndInternalGroup,'ndInternalDebugLevel':ndInternalDebugLevel,'ndInternalDebugFlags':ndInternalDebugFlags,'ndRedundancyGroup':ndRedundancyGroup,'ndPrimaryNP':ndPrimaryNP,'ndThisNP':ndThisNP,'ndForceToBackup':ndForceToBackup,'lwmaInfo':lwmaInfo,'lwmaTable':lwmaTable,'lwmaEntry':lwmaEntry,_BR:lwmaIndex,'lwmaCreationTime':lwmaCreationTime,'lwmaTableNotification':lwmaTableNotification,'lwmaTrapLevel':lwmaTrapLevel,'lwmaTrapNumber':lwmaTrapNumber,'lwmaTrapOnOffState':lwmaTrapOnOffState,'lwmaTrapCliAlias':lwmaTrapCliAlias,'lightStreamInternet':lightStreamInternet,'lightStreamBridge':lightStreamBridge,'lightStreamBridgePortTable':lightStreamBridgePortTable,'lightStreamBridgePortEntry':lightStreamBridgePortEntry,_BS:lightStreamBrPortPort,'lightStreamBrPortDefaultAction':lightStreamBrPortDefaultAction,'lightStreamBrPortBcastRateLimit':lightStreamBrPortBcastRateLimit,'lightStreamBrPortDroppedBcastPkts':lightStreamBrPortDroppedBcastPkts,'lightStreamBridgeFilterTable':lightStreamBridgeFilterTable,'lightStreamBridgeFilterEntry':lightStreamBridgeFilterEntry,_BU:lightStreamBrFilterId,_BV:lightStreamBrFilterTokenIndex,'lightStreamBrFilterTokenType':lightStreamBrFilterTokenType,'lightStreamBrFilterTokenValue':lightStreamBrFilterTokenValue,'lightStreamBrFilterStatus':lightStreamBrFilterStatus,'lightStreamBridgeFilterParameterTable':lightStreamBridgeFilterParameterTable,'lightStreamBridgeFilterParameterEntry':lightStreamBridgeFilterParameterEntry,_BW:lightStreamBrFilterParmPort,_BX:lightStreamBrFilterParmFilterId,'lightStreamBrFilterParmFilterPriority':lightStreamBrFilterParmFilterPriority,'lightStreamBrFilterParmAction':lightStreamBrFilterParmAction,'lightStreamBrFilterParmMatchCounts':lightStreamBrFilterParmMatchCounts,'lightStreamBrFilterParmValidation':lightStreamBrFilterParmValidation,'lightStreamBrStaticGoToCardSize':lightStreamBrStaticGoToCardSize,'lightStreamVli':lightStreamVli,'lightStreamVliVersion':lightStreamVliVersion,'lightStreamVliPortCtlTable':lightStreamVliPortCtlTable,'lightStreamVliPortCtlEntry':lightStreamVliPortCtlEntry,_BY:lightStreamVliPortCtlPort,'lightStreamVliPortCtlMode':lightStreamVliPortCtlMode,'lightStreamVliPortWorkGroupTable':lightStreamVliPortWorkGroupTable,'lightStreamVliPortWorkGroupEntry':lightStreamVliPortWorkGroupEntry,_BZ:lightStreamVliPortWorkGroupPort,_Ba:lightStreamVliPortWorkGroupID,'lightStreamVliPortWorkGroupValidation':lightStreamVliPortWorkGroupValidation,'lightStreamEOM':lightStreamEOM,'lightStreamEndOfMib':lightStreamEndOfMib})