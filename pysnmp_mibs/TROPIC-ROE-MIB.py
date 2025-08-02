_BH='tnRoeEthlinkGroup'
_BG='tnRoeDeMapperGroup'
_BF='tnRoeMapperGroup'
_BE='tnRoeGroup'
_BD='tnRoeSeqProfGroup'
_BC='tnRoeEthlinkRowStatus'
_BB='tnRoeEthlinkEthertype'
_BA='tnRoeEthlinkInnerPri'
_B9='tnRoeEthlinkInnerVid'
_B8='tnRoeEthlinkInnerEthertype'
_B7='tnRoeEthlinkOuterPri'
_B6='tnRoeEthlinkOuterVid'
_B5='tnRoeEthlinkOuterEthertype'
_B4='tnRoeEthlinkTagDepth'
_B3='tnRoeEthlinkSourceMac'
_B2='tnRoeEthlinkDestMac'
_B1='tnRoeEthlinkDescription'
_B0='tnRoeDeMapperNv'
_A_='tnRoeDeMapperNc'
_Az='tnRoeDeMapperK'
_Ay='tnRoeDeMapperS'
_Ax='tnRoeDeMapperNa'
_Aw='tnRoeDeMapperPincrement'
_Av='tnRoeDeMapperSchanSize'
_Au='tnRoeDeMapperSchanStart'
_At='tnRoeDeMapperFrameStartOffset'
_As='tnRoeDeMapperPosition'
_Ar='tnRoeDeMapperBwID'
_Aq='tnRoeDeMapperSaType'
_Ap='tnRoeDeMapperAlmProfName'
_Ao='tnRoeDeMapperRowStatus'
_An='tnRoeDeMapperPmonPolicy'
_Am='tnRoeDeMapperOrderInfoType'
_Al='tnRoeDeMapperFlowID'
_Ak='tnRoeDeMapperType'
_Aj='tnRoeDeMapperShutdown'
_Ai='tnRoeDeMapperJitterBufferDepth'
_Ah='tnRoeDeMapperBfrm'
_Ag='tnRoeDeMapperHfn'
_Af='tnRoeDeMapperBfn'
_Ae='tnRoeDeMapperSyncMode'
_Ad='tnRoeDeMapperPayloadLen'
_Ac='tnRoeDeMappeEtherlinkID'
_Ab='tnRoeDeMapperDescription'
_Aa='tnRoeMapperNv'
_AZ='tnRoeMapperNc'
_AY='tnRoeMapperK'
_AX='tnRoeMapperS'
_AW='tnRoeMapperNa'
_AV='tnRoeMapperPincrement'
_AU='tnRoeMapperSchanSize'
_AT='tnRoeMapperSchanStart'
_AS='tnRoeMapperFrameStartOffset'
_AR='tnRoeMapperPosition'
_AQ='tnRoeMapperBwID'
_AP='tnRoeMapperSaType'
_AO='tnRoeMapperAlmProfName'
_AN='tnRoeMapperRowStatus'
_AM='tnRoeMapperPmonPolicy'
_AL='tnRoeMapperOrderInfoType'
_AK='tnRoeMapperType'
_AJ='tnRoeMapperShutdown'
_AI='tnRoeMapperBfrm'
_AH='tnRoeMapperHfn'
_AG='tnRoeMapperBfn'
_AF='tnRoeMapperSyncMode'
_AE='tnRoeMapperPayloadLen'
_AD='tnRoeMappeEtherlinkID'
_AC='tnRoeMapperFlowID'
_AB='tnRoeMapperDescription'
_AA='tnRoeSlowcmRate'
_A9='tnRoeMapperStatusEnable'
_A8='tnRoeCpriProtocolVer'
_A7='tnRoePPointer'
_A6='tnRoeMapperSampleWidth'
_A5='tnRoeTargetOffsetNano'
_A4='tnRoeTargetOffsetSubNano'
_A3='tnRoePresTimeOffsetNano'
_A2='tnRoePresTimeOffsetSubNano'
_A1='tnRoeAlmProfName'
_A0='tnRoeRowStatus'
_z='tnRoePmonPolicy'
_y='tnRoeAdminState'
_x='tnRoeEncapMode'
_w='tnRoeInitialTxHFN'
_v='tnRoeInitialTxBFN'
_u='tnRoeSeqNumProfID'
_t='tnRoeAutoUponChange'
_s='tnRoeCpriTxGenOffset'
_r='tnRoePresTimeOffset'
_q='tnRoeOrderInfoType'
_p='tnRoeDescription'
_o='tnRoeSeqProfRowStatus'
_n='tnRoeSeqProfQInc'
_m='tnRoeSeqProfQIncProp'
_l='tnRoeSeqProfQMax'
_k='tnRoeSeqProfPInc'
_j='tnRoeSeqProfPIncProp'
_i='tnRoeSeqProfPMax'
_h='tnRoeSeqProfType'
_g='tnRoeSeqProfDescription'
_f='tnRoeEthlinkID'
_e='tnRoeEthlinkPortID'
_d='tnRoeEthlinkCardType'
_c='tnRoeDeMapperID'
_b='tnRoeDeMapperCardType'
_a='no-shutdwn'
_Z='shutdown'
_Y='tnRoeMapperID'
_X='tnRoeMapperPortID'
_W='tnRoeMapperCardType'
_V='enable'
_U='disable'
_T='tnRoeCardType'
_S='payloadsize'
_R='tnRoeSeqProfID'
_Q='tnRoeSeqProfPortID'
_P='tnRoeSeqProfCardType'
_O='structureAwareControl'
_N='structureAware'
_M='linecodeAware'
_L='tunneling'
_K='prestime'
_J='tnRoePortID'
_I='seqnum'
_H='Unsigned32'
_G='OctetString'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='TROPIC-ROE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
TItemDescription,TmnxPortID=mibBuilder.importSymbols('TN-TC-MIB','TItemDescription','TmnxPortID')
tnPortModules,tnRoeMib=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnPortModules','tnRoeMib')
tnRoeMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,4,10))
if mibBuilder.loadTexts:tnRoeMibModule.setRevisions(('2021-04-30 12:00','2021-01-08 12:00','2020-12-18 12:00','2020-10-23 12:00','2020-06-19 12:00','2020-04-03 12:00','2020-02-28 12:00','2020-01-24 12:00','2019-09-13 12:00','2018-08-24 12:00'))
class TropicRoeCardType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('t24PS1',1),('t24PS2',2),('t12PS',3),('s24PS1',4),('s24PS2',5)))
_TnRoeNotifications_ObjectIdentity=ObjectIdentity
tnRoeNotifications=_TnRoeNotifications_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,12,0))
_TnRoeObjects_ObjectIdentity=ObjectIdentity
tnRoeObjects=_TnRoeObjects_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,12,1))
_TnRoeParameters_ObjectIdentity=ObjectIdentity
tnRoeParameters=_TnRoeParameters_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,12,1,1))
_TnRoeSeqProfTable_Object=MibTable
tnRoeSeqProfTable=_TnRoeSeqProfTable_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1))
if mibBuilder.loadTexts:tnRoeSeqProfTable.setStatus(_A)
_TnRoeSeqProfEntry_Object=MibTableRow
tnRoeSeqProfEntry=_TnRoeSeqProfEntry_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1))
tnRoeSeqProfEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:tnRoeSeqProfEntry.setStatus(_A)
_TnRoeSeqProfCardType_Type=TropicRoeCardType
_TnRoeSeqProfCardType_Object=MibTableColumn
tnRoeSeqProfCardType=_TnRoeSeqProfCardType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,1),_TnRoeSeqProfCardType_Type())
tnRoeSeqProfCardType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeSeqProfCardType.setStatus(_A)
_TnRoeSeqProfPortID_Type=TmnxPortID
_TnRoeSeqProfPortID_Object=MibTableColumn
tnRoeSeqProfPortID=_TnRoeSeqProfPortID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,2),_TnRoeSeqProfPortID_Type())
tnRoeSeqProfPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeSeqProfPortID.setStatus(_A)
class _TnRoeSeqProfID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeSeqProfID_Type.__name__=_D
_TnRoeSeqProfID_Object=MibTableColumn
tnRoeSeqProfID=_TnRoeSeqProfID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,3),_TnRoeSeqProfID_Type())
tnRoeSeqProfID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeSeqProfID.setStatus(_A)
_TnRoeSeqProfDescription_Type=TItemDescription
_TnRoeSeqProfDescription_Object=MibTableColumn
tnRoeSeqProfDescription=_TnRoeSeqProfDescription_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,4),_TnRoeSeqProfDescription_Type())
tnRoeSeqProfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfDescription.setStatus(_A)
class _TnRoeSeqProfType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('frmrnum',0),(_I,1)))
_TnRoeSeqProfType_Type.__name__=_D
_TnRoeSeqProfType_Object=MibTableColumn
tnRoeSeqProfType=_TnRoeSeqProfType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,5),_TnRoeSeqProfType_Type())
tnRoeSeqProfType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfType.setStatus(_A)
class _TnRoeSeqProfPMax_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TnRoeSeqProfPMax_Type.__name__=_H
_TnRoeSeqProfPMax_Object=MibTableColumn
tnRoeSeqProfPMax=_TnRoeSeqProfPMax_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,6),_TnRoeSeqProfPMax_Type())
tnRoeSeqProfPMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfPMax.setStatus(_A)
class _TnRoeSeqProfPIncProp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fixed',0),(_S,1)))
_TnRoeSeqProfPIncProp_Type.__name__=_D
_TnRoeSeqProfPIncProp_Object=MibTableColumn
tnRoeSeqProfPIncProp=_TnRoeSeqProfPIncProp_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,7),_TnRoeSeqProfPIncProp_Type())
tnRoeSeqProfPIncProp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfPIncProp.setStatus(_A)
class _TnRoeSeqProfPInc_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnRoeSeqProfPInc_Type.__name__=_H
_TnRoeSeqProfPInc_Object=MibTableColumn
tnRoeSeqProfPInc=_TnRoeSeqProfPInc_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,8),_TnRoeSeqProfPInc_Type())
tnRoeSeqProfPInc.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfPInc.setStatus(_A)
class _TnRoeSeqProfQMax_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TnRoeSeqProfQMax_Type.__name__=_H
_TnRoeSeqProfQMax_Object=MibTableColumn
tnRoeSeqProfQMax=_TnRoeSeqProfQMax_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,9),_TnRoeSeqProfQMax_Type())
tnRoeSeqProfQMax.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfQMax.setStatus(_A)
class _TnRoeSeqProfQIncProp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fixed',0),(_S,1)))
_TnRoeSeqProfQIncProp_Type.__name__=_D
_TnRoeSeqProfQIncProp_Object=MibTableColumn
tnRoeSeqProfQIncProp=_TnRoeSeqProfQIncProp_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,10),_TnRoeSeqProfQIncProp_Type())
tnRoeSeqProfQIncProp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfQIncProp.setStatus(_A)
class _TnRoeSeqProfQInc_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TnRoeSeqProfQInc_Type.__name__=_H
_TnRoeSeqProfQInc_Object=MibTableColumn
tnRoeSeqProfQInc=_TnRoeSeqProfQInc_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,11),_TnRoeSeqProfQInc_Type())
tnRoeSeqProfQInc.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfQInc.setStatus(_A)
_TnRoeSeqProfRowStatus_Type=RowStatus
_TnRoeSeqProfRowStatus_Object=MibTableColumn
tnRoeSeqProfRowStatus=_TnRoeSeqProfRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,1,1,12),_TnRoeSeqProfRowStatus_Type())
tnRoeSeqProfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqProfRowStatus.setStatus(_A)
_TnRoeTable_Object=MibTable
tnRoeTable=_TnRoeTable_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2))
if mibBuilder.loadTexts:tnRoeTable.setStatus(_A)
_TnRoeEntry_Object=MibTableRow
tnRoeEntry=_TnRoeEntry_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1))
tnRoeEntry.setIndexNames((0,_B,_T),(0,_B,_J))
if mibBuilder.loadTexts:tnRoeEntry.setStatus(_A)
_TnRoeCardType_Type=TropicRoeCardType
_TnRoeCardType_Object=MibTableColumn
tnRoeCardType=_TnRoeCardType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,1),_TnRoeCardType_Type())
tnRoeCardType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeCardType.setStatus(_A)
_TnRoePortID_Type=TmnxPortID
_TnRoePortID_Object=MibTableColumn
tnRoePortID=_TnRoePortID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,2),_TnRoePortID_Type())
tnRoePortID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoePortID.setStatus(_A)
_TnRoeDescription_Type=TItemDescription
_TnRoeDescription_Object=MibTableColumn
tnRoeDescription=_TnRoeDescription_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,3),_TnRoeDescription_Type())
tnRoeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDescription.setStatus(_A)
class _TnRoeOrderInfoType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_I,1)))
_TnRoeOrderInfoType_Type.__name__=_D
_TnRoeOrderInfoType_Object=MibTableColumn
tnRoeOrderInfoType=_TnRoeOrderInfoType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,4),_TnRoeOrderInfoType_Type())
tnRoeOrderInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeOrderInfoType.setStatus(_A)
class _TnRoePresTimeOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1677721600))
_TnRoePresTimeOffset_Type.__name__=_D
_TnRoePresTimeOffset_Object=MibTableColumn
tnRoePresTimeOffset=_TnRoePresTimeOffset_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,5),_TnRoePresTimeOffset_Type())
tnRoePresTimeOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoePresTimeOffset.setStatus(_A)
class _TnRoeCpriTxGenOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_TnRoeCpriTxGenOffset_Type.__name__=_G
_TnRoeCpriTxGenOffset_Object=MibTableColumn
tnRoeCpriTxGenOffset=_TnRoeCpriTxGenOffset_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,6),_TnRoeCpriTxGenOffset_Type())
tnRoeCpriTxGenOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeCpriTxGenOffset.setStatus(_A)
class _TnRoeAutoUponChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_TnRoeAutoUponChange_Type.__name__=_D
_TnRoeAutoUponChange_Object=MibTableColumn
tnRoeAutoUponChange=_TnRoeAutoUponChange_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,7),_TnRoeAutoUponChange_Type())
tnRoeAutoUponChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeAutoUponChange.setStatus(_A)
class _TnRoeSeqNumProfID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeSeqNumProfID_Type.__name__=_D
_TnRoeSeqNumProfID_Object=MibTableColumn
tnRoeSeqNumProfID=_TnRoeSeqNumProfID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,8),_TnRoeSeqNumProfID_Type())
tnRoeSeqNumProfID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSeqNumProfID.setStatus(_A)
class _TnRoeInitialTxBFN_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_TnRoeInitialTxBFN_Type.__name__=_D
_TnRoeInitialTxBFN_Object=MibTableColumn
tnRoeInitialTxBFN=_TnRoeInitialTxBFN_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,9),_TnRoeInitialTxBFN_Type())
tnRoeInitialTxBFN.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeInitialTxBFN.setStatus(_A)
class _TnRoeInitialTxHFN_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,149))
_TnRoeInitialTxHFN_Type.__name__=_D
_TnRoeInitialTxHFN_Object=MibTableColumn
tnRoeInitialTxHFN=_TnRoeInitialTxHFN_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,10),_TnRoeInitialTxHFN_Type())
tnRoeInitialTxHFN.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeInitialTxHFN.setStatus(_A)
class _TnRoeEncapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,7,8,9)));namedValues=NamedValues(*((_L,6),(_M,7),(_N,8),(_O,9)))
_TnRoeEncapMode_Type.__name__=_D
_TnRoeEncapMode_Object=MibTableColumn
tnRoeEncapMode=_TnRoeEncapMode_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,11),_TnRoeEncapMode_Type())
tnRoeEncapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeEncapMode.setStatus(_A)
class _TnRoeAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('down',2),('up',3)))
_TnRoeAdminState_Type.__name__=_D
_TnRoeAdminState_Object=MibTableColumn
tnRoeAdminState=_TnRoeAdminState_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,12),_TnRoeAdminState_Type())
tnRoeAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeAdminState.setStatus(_A)
class _TnRoePmonPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnRoePmonPolicy_Type.__name__=_D
_TnRoePmonPolicy_Object=MibTableColumn
tnRoePmonPolicy=_TnRoePmonPolicy_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,13),_TnRoePmonPolicy_Type())
tnRoePmonPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoePmonPolicy.setStatus(_A)
_TnRoeRowStatus_Type=RowStatus
_TnRoeRowStatus_Object=MibTableColumn
tnRoeRowStatus=_TnRoeRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,14),_TnRoeRowStatus_Type())
tnRoeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeRowStatus.setStatus(_A)
class _TnRoeAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnRoeAlmProfName_Type.__name__=_G
_TnRoeAlmProfName_Object=MibTableColumn
tnRoeAlmProfName=_TnRoeAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,15),_TnRoeAlmProfName_Type())
tnRoeAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeAlmProfName.setStatus(_A)
class _TnRoePresTimeOffsetSubNano_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_TnRoePresTimeOffsetSubNano_Type.__name__=_D
_TnRoePresTimeOffsetSubNano_Object=MibTableColumn
tnRoePresTimeOffsetSubNano=_TnRoePresTimeOffsetSubNano_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,16),_TnRoePresTimeOffsetSubNano_Type())
tnRoePresTimeOffsetSubNano.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoePresTimeOffsetSubNano.setStatus(_A)
class _TnRoePresTimeOffsetNano_Type(Integer32):defaultValue=100000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,16777216))
_TnRoePresTimeOffsetNano_Type.__name__=_D
_TnRoePresTimeOffsetNano_Object=MibTableColumn
tnRoePresTimeOffsetNano=_TnRoePresTimeOffsetNano_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,17),_TnRoePresTimeOffsetNano_Type())
tnRoePresTimeOffsetNano.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoePresTimeOffsetNano.setStatus(_A)
class _TnRoeTargetOffsetSubNano_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_TnRoeTargetOffsetSubNano_Type.__name__=_D
_TnRoeTargetOffsetSubNano_Object=MibTableColumn
tnRoeTargetOffsetSubNano=_TnRoeTargetOffsetSubNano_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,18),_TnRoeTargetOffsetSubNano_Type())
tnRoeTargetOffsetSubNano.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeTargetOffsetSubNano.setStatus(_A)
class _TnRoeTargetOffsetNano_Type(Integer32):defaultValue=100000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,16777216))
_TnRoeTargetOffsetNano_Type.__name__=_D
_TnRoeTargetOffsetNano_Object=MibTableColumn
tnRoeTargetOffsetNano=_TnRoeTargetOffsetNano_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,19),_TnRoeTargetOffsetNano_Type())
tnRoeTargetOffsetNano.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeTargetOffsetNano.setStatus(_A)
class _TnRoeMapperSampleWidth_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,20))
_TnRoeMapperSampleWidth_Type.__name__=_D
_TnRoeMapperSampleWidth_Object=MibTableColumn
tnRoeMapperSampleWidth=_TnRoeMapperSampleWidth_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,20),_TnRoeMapperSampleWidth_Type())
tnRoeMapperSampleWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperSampleWidth.setStatus(_A)
class _TnRoeDeMapperSampleWidth_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,20))
_TnRoeDeMapperSampleWidth_Type.__name__=_D
_TnRoeDeMapperSampleWidth_Object=MibTableColumn
tnRoeDeMapperSampleWidth=_TnRoeDeMapperSampleWidth_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,21),_TnRoeDeMapperSampleWidth_Type())
tnRoeDeMapperSampleWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperSampleWidth.setStatus(_A)
class _TnRoePPointer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,63))
_TnRoePPointer_Type.__name__=_D
_TnRoePPointer_Object=MibTableColumn
tnRoePPointer=_TnRoePPointer_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,24),_TnRoePPointer_Type())
tnRoePPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoePPointer.setStatus(_A)
class _TnRoeCpriProtocolVer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnRoeCpriProtocolVer_Type.__name__=_D
_TnRoeCpriProtocolVer_Object=MibTableColumn
tnRoeCpriProtocolVer=_TnRoeCpriProtocolVer_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,25),_TnRoeCpriProtocolVer_Type())
tnRoeCpriProtocolVer.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeCpriProtocolVer.setStatus(_A)
class _TnRoeMapperStatusEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_TnRoeMapperStatusEnable_Type.__name__=_D
_TnRoeMapperStatusEnable_Object=MibTableColumn
tnRoeMapperStatusEnable=_TnRoeMapperStatusEnable_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,26),_TnRoeMapperStatusEnable_Type())
tnRoeMapperStatusEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperStatusEnable.setStatus(_A)
class _TnRoeSlowcmRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnRoeSlowcmRate_Type.__name__=_D
_TnRoeSlowcmRate_Object=MibTableColumn
tnRoeSlowcmRate=_TnRoeSlowcmRate_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,2,1,27),_TnRoeSlowcmRate_Type())
tnRoeSlowcmRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeSlowcmRate.setStatus(_A)
_TnRoeMapperTable_Object=MibTable
tnRoeMapperTable=_TnRoeMapperTable_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3))
if mibBuilder.loadTexts:tnRoeMapperTable.setStatus(_A)
_TnRoeMapperEntry_Object=MibTableRow
tnRoeMapperEntry=_TnRoeMapperEntry_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1))
tnRoeMapperEntry.setIndexNames((0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:tnRoeMapperEntry.setStatus(_A)
_TnRoeMapperCardType_Type=TropicRoeCardType
_TnRoeMapperCardType_Object=MibTableColumn
tnRoeMapperCardType=_TnRoeMapperCardType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,1),_TnRoeMapperCardType_Type())
tnRoeMapperCardType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeMapperCardType.setStatus(_A)
_TnRoeMapperPortID_Type=TmnxPortID
_TnRoeMapperPortID_Object=MibTableColumn
tnRoeMapperPortID=_TnRoeMapperPortID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,2),_TnRoeMapperPortID_Type())
tnRoeMapperPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeMapperPortID.setStatus(_A)
class _TnRoeMapperID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeMapperID_Type.__name__=_D
_TnRoeMapperID_Object=MibTableColumn
tnRoeMapperID=_TnRoeMapperID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,3),_TnRoeMapperID_Type())
tnRoeMapperID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeMapperID.setStatus(_A)
_TnRoeMapperDescription_Type=TItemDescription
_TnRoeMapperDescription_Object=MibTableColumn
tnRoeMapperDescription=_TnRoeMapperDescription_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,4),_TnRoeMapperDescription_Type())
tnRoeMapperDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperDescription.setStatus(_A)
class _TnRoeMapperFlowID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_TnRoeMapperFlowID_Type.__name__=_D
_TnRoeMapperFlowID_Object=MibTableColumn
tnRoeMapperFlowID=_TnRoeMapperFlowID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,5),_TnRoeMapperFlowID_Type())
tnRoeMapperFlowID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperFlowID.setStatus(_A)
class _TnRoeMappeEtherlinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeMappeEtherlinkID_Type.__name__=_D
_TnRoeMappeEtherlinkID_Object=MibTableColumn
tnRoeMappeEtherlinkID=_TnRoeMappeEtherlinkID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,6),_TnRoeMappeEtherlinkID_Type())
tnRoeMappeEtherlinkID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMappeEtherlinkID.setStatus(_A)
class _TnRoeMapperPayloadLen_Type(Integer32):defaultValue=640;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1500))
_TnRoeMapperPayloadLen_Type.__name__=_D
_TnRoeMapperPayloadLen_Object=MibTableColumn
tnRoeMapperPayloadLen=_TnRoeMapperPayloadLen_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,7),_TnRoeMapperPayloadLen_Type())
tnRoeMapperPayloadLen.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperPayloadLen.setStatus(_A)
class _TnRoeMapperSyncMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('hyper',0),('radio',1),('basic',2)))
_TnRoeMapperSyncMode_Type.__name__=_D
_TnRoeMapperSyncMode_Object=MibTableColumn
tnRoeMapperSyncMode=_TnRoeMapperSyncMode_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,8),_TnRoeMapperSyncMode_Type())
tnRoeMapperSyncMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperSyncMode.setStatus(_A)
class _TnRoeMapperBfn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_TnRoeMapperBfn_Type.__name__=_D
_TnRoeMapperBfn_Object=MibTableColumn
tnRoeMapperBfn=_TnRoeMapperBfn_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,9),_TnRoeMapperBfn_Type())
tnRoeMapperBfn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperBfn.setStatus(_A)
class _TnRoeMapperHfn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,149))
_TnRoeMapperHfn_Type.__name__=_D
_TnRoeMapperHfn_Object=MibTableColumn
tnRoeMapperHfn=_TnRoeMapperHfn_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,10),_TnRoeMapperHfn_Type())
tnRoeMapperHfn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperHfn.setStatus(_A)
class _TnRoeMapperBfrm_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnRoeMapperBfrm_Type.__name__=_D
_TnRoeMapperBfrm_Object=MibTableColumn
tnRoeMapperBfrm=_TnRoeMapperBfrm_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,11),_TnRoeMapperBfrm_Type())
tnRoeMapperBfrm.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperBfrm.setStatus(_A)
class _TnRoeMapperShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Z,2),(_a,3)))
_TnRoeMapperShutdown_Type.__name__=_D
_TnRoeMapperShutdown_Object=MibTableColumn
tnRoeMapperShutdown=_TnRoeMapperShutdown_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,12),_TnRoeMapperShutdown_Type())
tnRoeMapperShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperShutdown.setStatus(_A)
class _TnRoeMapperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,7,8,9)));namedValues=NamedValues(*((_L,6),(_M,7),(_N,8),(_O,9)))
_TnRoeMapperType_Type.__name__=_D
_TnRoeMapperType_Object=MibTableColumn
tnRoeMapperType=_TnRoeMapperType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,13),_TnRoeMapperType_Type())
tnRoeMapperType.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperType.setStatus(_A)
class _TnRoeMapperOrderInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_I,1)))
_TnRoeMapperOrderInfoType_Type.__name__=_D
_TnRoeMapperOrderInfoType_Object=MibTableColumn
tnRoeMapperOrderInfoType=_TnRoeMapperOrderInfoType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,14),_TnRoeMapperOrderInfoType_Type())
tnRoeMapperOrderInfoType.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperOrderInfoType.setStatus(_A)
class _TnRoeMapperPmonPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnRoeMapperPmonPolicy_Type.__name__=_D
_TnRoeMapperPmonPolicy_Object=MibTableColumn
tnRoeMapperPmonPolicy=_TnRoeMapperPmonPolicy_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,15),_TnRoeMapperPmonPolicy_Type())
tnRoeMapperPmonPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperPmonPolicy.setStatus(_A)
_TnRoeMapperRowStatus_Type=RowStatus
_TnRoeMapperRowStatus_Object=MibTableColumn
tnRoeMapperRowStatus=_TnRoeMapperRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,16),_TnRoeMapperRowStatus_Type())
tnRoeMapperRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperRowStatus.setStatus(_A)
class _TnRoeMapperAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnRoeMapperAlmProfName_Type.__name__=_G
_TnRoeMapperAlmProfName_Object=MibTableColumn
tnRoeMapperAlmProfName=_TnRoeMapperAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,17),_TnRoeMapperAlmProfName_Type())
tnRoeMapperAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperAlmProfName.setStatus(_A)
class _TnRoeMapperSaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_TnRoeMapperSaType_Type.__name__=_D
_TnRoeMapperSaType_Object=MibTableColumn
tnRoeMapperSaType=_TnRoeMapperSaType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,18),_TnRoeMapperSaType_Type())
tnRoeMapperSaType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperSaType.setStatus(_A)
class _TnRoeMapperBwID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_TnRoeMapperBwID_Type.__name__=_D
_TnRoeMapperBwID_Object=MibTableColumn
tnRoeMapperBwID=_TnRoeMapperBwID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,19),_TnRoeMapperBwID_Type())
tnRoeMapperBwID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperBwID.setStatus(_A)
class _TnRoeMapperPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,6143))
_TnRoeMapperPosition_Type.__name__=_D
_TnRoeMapperPosition_Object=MibTableColumn
tnRoeMapperPosition=_TnRoeMapperPosition_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,20),_TnRoeMapperPosition_Type())
tnRoeMapperPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperPosition.setStatus(_A)
class _TnRoeMapperFrameStartOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,6143))
_TnRoeMapperFrameStartOffset_Type.__name__=_D
_TnRoeMapperFrameStartOffset_Object=MibTableColumn
tnRoeMapperFrameStartOffset=_TnRoeMapperFrameStartOffset_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,21),_TnRoeMapperFrameStartOffset_Type())
tnRoeMapperFrameStartOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperFrameStartOffset.setStatus(_A)
class _TnRoeMapperSchanStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,19))
_TnRoeMapperSchanStart_Type.__name__=_D
_TnRoeMapperSchanStart_Object=MibTableColumn
tnRoeMapperSchanStart=_TnRoeMapperSchanStart_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,22),_TnRoeMapperSchanStart_Type())
tnRoeMapperSchanStart.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperSchanStart.setStatus(_A)
class _TnRoeMapperSchanSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_TnRoeMapperSchanSize_Type.__name__=_D
_TnRoeMapperSchanSize_Object=MibTableColumn
tnRoeMapperSchanSize=_TnRoeMapperSchanSize_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,23),_TnRoeMapperSchanSize_Type())
tnRoeMapperSchanSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeMapperSchanSize.setStatus(_A)
_TnRoeMapperPincrement_Type=Integer32
_TnRoeMapperPincrement_Object=MibTableColumn
tnRoeMapperPincrement=_TnRoeMapperPincrement_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,24),_TnRoeMapperPincrement_Type())
tnRoeMapperPincrement.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperPincrement.setStatus(_A)
_TnRoeMapperNa_Type=Integer32
_TnRoeMapperNa_Object=MibTableColumn
tnRoeMapperNa=_TnRoeMapperNa_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,25),_TnRoeMapperNa_Type())
tnRoeMapperNa.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperNa.setStatus(_A)
_TnRoeMapperS_Type=Integer32
_TnRoeMapperS_Object=MibTableColumn
tnRoeMapperS=_TnRoeMapperS_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,26),_TnRoeMapperS_Type())
tnRoeMapperS.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperS.setStatus(_A)
_TnRoeMapperK_Type=Integer32
_TnRoeMapperK_Object=MibTableColumn
tnRoeMapperK=_TnRoeMapperK_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,27),_TnRoeMapperK_Type())
tnRoeMapperK.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperK.setStatus(_A)
_TnRoeMapperNc_Type=Integer32
_TnRoeMapperNc_Object=MibTableColumn
tnRoeMapperNc=_TnRoeMapperNc_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,28),_TnRoeMapperNc_Type())
tnRoeMapperNc.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperNc.setStatus(_A)
_TnRoeMapperNv_Type=Integer32
_TnRoeMapperNv_Object=MibTableColumn
tnRoeMapperNv=_TnRoeMapperNv_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,3,1,29),_TnRoeMapperNv_Type())
tnRoeMapperNv.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeMapperNv.setStatus(_A)
_TnRoeDeMapperTable_Object=MibTable
tnRoeDeMapperTable=_TnRoeDeMapperTable_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4))
if mibBuilder.loadTexts:tnRoeDeMapperTable.setStatus(_A)
_TnRoeDeMapperEntry_Object=MibTableRow
tnRoeDeMapperEntry=_TnRoeDeMapperEntry_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1))
tnRoeDeMapperEntry.setIndexNames((0,_B,_b),(0,_B,_J),(0,_B,_c))
if mibBuilder.loadTexts:tnRoeDeMapperEntry.setStatus(_A)
_TnRoeDeMapperCardType_Type=TropicRoeCardType
_TnRoeDeMapperCardType_Object=MibTableColumn
tnRoeDeMapperCardType=_TnRoeDeMapperCardType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,1),_TnRoeDeMapperCardType_Type())
tnRoeDeMapperCardType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeDeMapperCardType.setStatus(_A)
_TnRoeDeMapperPortID_Type=TmnxPortID
_TnRoeDeMapperPortID_Object=MibTableColumn
tnRoeDeMapperPortID=_TnRoeDeMapperPortID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,2),_TnRoeDeMapperPortID_Type())
tnRoeDeMapperPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeDeMapperPortID.setStatus(_A)
class _TnRoeDeMapperID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeDeMapperID_Type.__name__=_D
_TnRoeDeMapperID_Object=MibTableColumn
tnRoeDeMapperID=_TnRoeDeMapperID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,3),_TnRoeDeMapperID_Type())
tnRoeDeMapperID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeDeMapperID.setStatus(_A)
_TnRoeDeMapperDescription_Type=TItemDescription
_TnRoeDeMapperDescription_Object=MibTableColumn
tnRoeDeMapperDescription=_TnRoeDeMapperDescription_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,4),_TnRoeDeMapperDescription_Type())
tnRoeDeMapperDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperDescription.setStatus(_A)
class _TnRoeDeMappeEtherlinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeDeMappeEtherlinkID_Type.__name__=_D
_TnRoeDeMappeEtherlinkID_Object=MibTableColumn
tnRoeDeMappeEtherlinkID=_TnRoeDeMappeEtherlinkID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,5),_TnRoeDeMappeEtherlinkID_Type())
tnRoeDeMappeEtherlinkID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMappeEtherlinkID.setStatus(_A)
class _TnRoeDeMapperPayloadLen_Type(Integer32):defaultValue=640;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1500))
_TnRoeDeMapperPayloadLen_Type.__name__=_D
_TnRoeDeMapperPayloadLen_Object=MibTableColumn
tnRoeDeMapperPayloadLen=_TnRoeDeMapperPayloadLen_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,6),_TnRoeDeMapperPayloadLen_Type())
tnRoeDeMapperPayloadLen.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperPayloadLen.setStatus(_A)
class _TnRoeDeMapperSyncMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('hyper',0),('radio',1),('basic',2)))
_TnRoeDeMapperSyncMode_Type.__name__=_D
_TnRoeDeMapperSyncMode_Object=MibTableColumn
tnRoeDeMapperSyncMode=_TnRoeDeMapperSyncMode_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,7),_TnRoeDeMapperSyncMode_Type())
tnRoeDeMapperSyncMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperSyncMode.setStatus(_A)
class _TnRoeDeMapperBfn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_TnRoeDeMapperBfn_Type.__name__=_D
_TnRoeDeMapperBfn_Object=MibTableColumn
tnRoeDeMapperBfn=_TnRoeDeMapperBfn_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,8),_TnRoeDeMapperBfn_Type())
tnRoeDeMapperBfn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperBfn.setStatus(_A)
class _TnRoeDeMapperHfn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,149))
_TnRoeDeMapperHfn_Type.__name__=_D
_TnRoeDeMapperHfn_Object=MibTableColumn
tnRoeDeMapperHfn=_TnRoeDeMapperHfn_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,9),_TnRoeDeMapperHfn_Type())
tnRoeDeMapperHfn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperHfn.setStatus(_A)
class _TnRoeDeMapperBfrm_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnRoeDeMapperBfrm_Type.__name__=_D
_TnRoeDeMapperBfrm_Object=MibTableColumn
tnRoeDeMapperBfrm=_TnRoeDeMapperBfrm_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,10),_TnRoeDeMapperBfrm_Type())
tnRoeDeMapperBfrm.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperBfrm.setStatus(_A)
class _TnRoeDeMapperJitterBufferDepth_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,128))
_TnRoeDeMapperJitterBufferDepth_Type.__name__=_D
_TnRoeDeMapperJitterBufferDepth_Object=MibTableColumn
tnRoeDeMapperJitterBufferDepth=_TnRoeDeMapperJitterBufferDepth_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,11),_TnRoeDeMapperJitterBufferDepth_Type())
tnRoeDeMapperJitterBufferDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperJitterBufferDepth.setStatus(_A)
class _TnRoeDeMapperShutdown_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Z,2),(_a,3)))
_TnRoeDeMapperShutdown_Type.__name__=_D
_TnRoeDeMapperShutdown_Object=MibTableColumn
tnRoeDeMapperShutdown=_TnRoeDeMapperShutdown_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,12),_TnRoeDeMapperShutdown_Type())
tnRoeDeMapperShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperShutdown.setStatus(_A)
class _TnRoeDeMapperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,7,8,9)));namedValues=NamedValues(*((_L,6),(_M,7),(_N,8),(_O,9)))
_TnRoeDeMapperType_Type.__name__=_D
_TnRoeDeMapperType_Object=MibTableColumn
tnRoeDeMapperType=_TnRoeDeMapperType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,13),_TnRoeDeMapperType_Type())
tnRoeDeMapperType.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperType.setStatus(_A)
class _TnRoeDeMapperFlowID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_TnRoeDeMapperFlowID_Type.__name__=_D
_TnRoeDeMapperFlowID_Object=MibTableColumn
tnRoeDeMapperFlowID=_TnRoeDeMapperFlowID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,14),_TnRoeDeMapperFlowID_Type())
tnRoeDeMapperFlowID.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperFlowID.setStatus(_A)
class _TnRoeDeMapperOrderInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_I,1)))
_TnRoeDeMapperOrderInfoType_Type.__name__=_D
_TnRoeDeMapperOrderInfoType_Object=MibTableColumn
tnRoeDeMapperOrderInfoType=_TnRoeDeMapperOrderInfoType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,15),_TnRoeDeMapperOrderInfoType_Type())
tnRoeDeMapperOrderInfoType.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperOrderInfoType.setStatus(_A)
class _TnRoeDeMapperPmonPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TnRoeDeMapperPmonPolicy_Type.__name__=_D
_TnRoeDeMapperPmonPolicy_Object=MibTableColumn
tnRoeDeMapperPmonPolicy=_TnRoeDeMapperPmonPolicy_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,16),_TnRoeDeMapperPmonPolicy_Type())
tnRoeDeMapperPmonPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperPmonPolicy.setStatus(_A)
_TnRoeDeMapperRowStatus_Type=RowStatus
_TnRoeDeMapperRowStatus_Object=MibTableColumn
tnRoeDeMapperRowStatus=_TnRoeDeMapperRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,17),_TnRoeDeMapperRowStatus_Type())
tnRoeDeMapperRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperRowStatus.setStatus(_A)
class _TnRoeDeMapperAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnRoeDeMapperAlmProfName_Type.__name__=_G
_TnRoeDeMapperAlmProfName_Object=MibTableColumn
tnRoeDeMapperAlmProfName=_TnRoeDeMapperAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,18),_TnRoeDeMapperAlmProfName_Type())
tnRoeDeMapperAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperAlmProfName.setStatus(_A)
class _TnRoeDeMapperSaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_TnRoeDeMapperSaType_Type.__name__=_D
_TnRoeDeMapperSaType_Object=MibTableColumn
tnRoeDeMapperSaType=_TnRoeDeMapperSaType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,19),_TnRoeDeMapperSaType_Type())
tnRoeDeMapperSaType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperSaType.setStatus(_A)
class _TnRoeDeMapperBwID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_TnRoeDeMapperBwID_Type.__name__=_D
_TnRoeDeMapperBwID_Object=MibTableColumn
tnRoeDeMapperBwID=_TnRoeDeMapperBwID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,20),_TnRoeDeMapperBwID_Type())
tnRoeDeMapperBwID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperBwID.setStatus(_A)
class _TnRoeDeMapperPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,6143))
_TnRoeDeMapperPosition_Type.__name__=_D
_TnRoeDeMapperPosition_Object=MibTableColumn
tnRoeDeMapperPosition=_TnRoeDeMapperPosition_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,21),_TnRoeDeMapperPosition_Type())
tnRoeDeMapperPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperPosition.setStatus(_A)
class _TnRoeDeMapperFrameStartOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,6143))
_TnRoeDeMapperFrameStartOffset_Type.__name__=_D
_TnRoeDeMapperFrameStartOffset_Object=MibTableColumn
tnRoeDeMapperFrameStartOffset=_TnRoeDeMapperFrameStartOffset_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,22),_TnRoeDeMapperFrameStartOffset_Type())
tnRoeDeMapperFrameStartOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperFrameStartOffset.setStatus(_A)
class _TnRoeDeMapperSchanStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,19))
_TnRoeDeMapperSchanStart_Type.__name__=_D
_TnRoeDeMapperSchanStart_Object=MibTableColumn
tnRoeDeMapperSchanStart=_TnRoeDeMapperSchanStart_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,23),_TnRoeDeMapperSchanStart_Type())
tnRoeDeMapperSchanStart.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperSchanStart.setStatus(_A)
class _TnRoeDeMapperSchanSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_TnRoeDeMapperSchanSize_Type.__name__=_D
_TnRoeDeMapperSchanSize_Object=MibTableColumn
tnRoeDeMapperSchanSize=_TnRoeDeMapperSchanSize_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,24),_TnRoeDeMapperSchanSize_Type())
tnRoeDeMapperSchanSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeDeMapperSchanSize.setStatus(_A)
_TnRoeDeMapperPincrement_Type=Integer32
_TnRoeDeMapperPincrement_Object=MibTableColumn
tnRoeDeMapperPincrement=_TnRoeDeMapperPincrement_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,25),_TnRoeDeMapperPincrement_Type())
tnRoeDeMapperPincrement.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperPincrement.setStatus(_A)
_TnRoeDeMapperNa_Type=Integer32
_TnRoeDeMapperNa_Object=MibTableColumn
tnRoeDeMapperNa=_TnRoeDeMapperNa_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,26),_TnRoeDeMapperNa_Type())
tnRoeDeMapperNa.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperNa.setStatus(_A)
_TnRoeDeMapperS_Type=Integer32
_TnRoeDeMapperS_Object=MibTableColumn
tnRoeDeMapperS=_TnRoeDeMapperS_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,27),_TnRoeDeMapperS_Type())
tnRoeDeMapperS.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperS.setStatus(_A)
_TnRoeDeMapperK_Type=Integer32
_TnRoeDeMapperK_Object=MibTableColumn
tnRoeDeMapperK=_TnRoeDeMapperK_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,28),_TnRoeDeMapperK_Type())
tnRoeDeMapperK.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperK.setStatus(_A)
_TnRoeDeMapperNc_Type=Integer32
_TnRoeDeMapperNc_Object=MibTableColumn
tnRoeDeMapperNc=_TnRoeDeMapperNc_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,29),_TnRoeDeMapperNc_Type())
tnRoeDeMapperNc.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperNc.setStatus(_A)
_TnRoeDeMapperNv_Type=Integer32
_TnRoeDeMapperNv_Object=MibTableColumn
tnRoeDeMapperNv=_TnRoeDeMapperNv_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,4,1,30),_TnRoeDeMapperNv_Type())
tnRoeDeMapperNv.setMaxAccess(_E)
if mibBuilder.loadTexts:tnRoeDeMapperNv.setStatus(_A)
_TnRoeEthlinkTable_Object=MibTable
tnRoeEthlinkTable=_TnRoeEthlinkTable_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5))
if mibBuilder.loadTexts:tnRoeEthlinkTable.setStatus(_A)
_TnRoeEthlinkEntry_Object=MibTableRow
tnRoeEthlinkEntry=_TnRoeEthlinkEntry_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1))
tnRoeEthlinkEntry.setIndexNames((0,_B,_d),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:tnRoeEthlinkEntry.setStatus(_A)
_TnRoeEthlinkCardType_Type=TropicRoeCardType
_TnRoeEthlinkCardType_Object=MibTableColumn
tnRoeEthlinkCardType=_TnRoeEthlinkCardType_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,1),_TnRoeEthlinkCardType_Type())
tnRoeEthlinkCardType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeEthlinkCardType.setStatus(_A)
_TnRoeEthlinkPortID_Type=TmnxPortID
_TnRoeEthlinkPortID_Object=MibTableColumn
tnRoeEthlinkPortID=_TnRoeEthlinkPortID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,2),_TnRoeEthlinkPortID_Type())
tnRoeEthlinkPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeEthlinkPortID.setStatus(_A)
class _TnRoeEthlinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeEthlinkID_Type.__name__=_D
_TnRoeEthlinkID_Object=MibTableColumn
tnRoeEthlinkID=_TnRoeEthlinkID_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,3),_TnRoeEthlinkID_Type())
tnRoeEthlinkID.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeEthlinkID.setStatus(_A)
_TnRoeEthlinkDescription_Type=TItemDescription
_TnRoeEthlinkDescription_Object=MibTableColumn
tnRoeEthlinkDescription=_TnRoeEthlinkDescription_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,4),_TnRoeEthlinkDescription_Type())
tnRoeEthlinkDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkDescription.setStatus(_A)
_TnRoeEthlinkDestMac_Type=MacAddress
_TnRoeEthlinkDestMac_Object=MibTableColumn
tnRoeEthlinkDestMac=_TnRoeEthlinkDestMac_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,5),_TnRoeEthlinkDestMac_Type())
tnRoeEthlinkDestMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkDestMac.setStatus(_A)
_TnRoeEthlinkSourceMac_Type=MacAddress
_TnRoeEthlinkSourceMac_Object=MibTableColumn
tnRoeEthlinkSourceMac=_TnRoeEthlinkSourceMac_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,6),_TnRoeEthlinkSourceMac_Type())
tnRoeEthlinkSourceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkSourceMac.setStatus(_A)
class _TnRoeEthlinkTagDepth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('untagged',0),('single',1),('double',2)))
_TnRoeEthlinkTagDepth_Type.__name__=_D
_TnRoeEthlinkTagDepth_Object=MibTableColumn
tnRoeEthlinkTagDepth=_TnRoeEthlinkTagDepth_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,7),_TnRoeEthlinkTagDepth_Type())
tnRoeEthlinkTagDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkTagDepth.setStatus(_A)
class _TnRoeEthlinkOuterEthertype_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_TnRoeEthlinkOuterEthertype_Type.__name__=_D
_TnRoeEthlinkOuterEthertype_Object=MibTableColumn
tnRoeEthlinkOuterEthertype=_TnRoeEthlinkOuterEthertype_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,8),_TnRoeEthlinkOuterEthertype_Type())
tnRoeEthlinkOuterEthertype.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkOuterEthertype.setStatus(_A)
class _TnRoeEthlinkOuterVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_TnRoeEthlinkOuterVid_Type.__name__=_D
_TnRoeEthlinkOuterVid_Object=MibTableColumn
tnRoeEthlinkOuterVid=_TnRoeEthlinkOuterVid_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,9),_TnRoeEthlinkOuterVid_Type())
tnRoeEthlinkOuterVid.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkOuterVid.setStatus(_A)
class _TnRoeEthlinkOuterPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnRoeEthlinkOuterPri_Type.__name__=_D
_TnRoeEthlinkOuterPri_Object=MibTableColumn
tnRoeEthlinkOuterPri=_TnRoeEthlinkOuterPri_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,10),_TnRoeEthlinkOuterPri_Type())
tnRoeEthlinkOuterPri.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkOuterPri.setStatus(_A)
class _TnRoeEthlinkInnerEthertype_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_TnRoeEthlinkInnerEthertype_Type.__name__=_D
_TnRoeEthlinkInnerEthertype_Object=MibTableColumn
tnRoeEthlinkInnerEthertype=_TnRoeEthlinkInnerEthertype_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,11),_TnRoeEthlinkInnerEthertype_Type())
tnRoeEthlinkInnerEthertype.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkInnerEthertype.setStatus(_A)
class _TnRoeEthlinkInnerVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_TnRoeEthlinkInnerVid_Type.__name__=_D
_TnRoeEthlinkInnerVid_Object=MibTableColumn
tnRoeEthlinkInnerVid=_TnRoeEthlinkInnerVid_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,12),_TnRoeEthlinkInnerVid_Type())
tnRoeEthlinkInnerVid.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkInnerVid.setStatus(_A)
class _TnRoeEthlinkInnerPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnRoeEthlinkInnerPri_Type.__name__=_D
_TnRoeEthlinkInnerPri_Object=MibTableColumn
tnRoeEthlinkInnerPri=_TnRoeEthlinkInnerPri_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,13),_TnRoeEthlinkInnerPri_Type())
tnRoeEthlinkInnerPri.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkInnerPri.setStatus(_A)
class _TnRoeEthlinkEthertype_Type(Integer32):defaultValue=64573;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_TnRoeEthlinkEthertype_Type.__name__=_D
_TnRoeEthlinkEthertype_Object=MibTableColumn
tnRoeEthlinkEthertype=_TnRoeEthlinkEthertype_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,14),_TnRoeEthlinkEthertype_Type())
tnRoeEthlinkEthertype.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkEthertype.setStatus(_A)
_TnRoeEthlinkRowStatus_Type=RowStatus
_TnRoeEthlinkRowStatus_Object=MibTableColumn
tnRoeEthlinkRowStatus=_TnRoeEthlinkRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,12,1,1,5,1,15),_TnRoeEthlinkRowStatus_Type())
tnRoeEthlinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRoeEthlinkRowStatus.setStatus(_A)
_TnRoeEConf_ObjectIdentity=ObjectIdentity
tnRoeEConf=_TnRoeEConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,12,2))
_TnRoeGroups_ObjectIdentity=ObjectIdentity
tnRoeGroups=_TnRoeGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,12,2,1))
_TnEoeCompliances_ObjectIdentity=ObjectIdentity
tnEoeCompliances=_TnEoeCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,12,2,2))
tnRoeSeqProfGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,12,2,1,1))
tnRoeSeqProfGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:tnRoeSeqProfGroup.setStatus(_A)
tnRoeGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,12,2,1,2))
tnRoeGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:tnRoeGroup.setStatus(_A)
tnRoeMapperGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,12,2,1,3))
tnRoeMapperGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:tnRoeMapperGroup.setStatus(_A)
tnRoeDeMapperGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,12,2,1,4))
tnRoeDeMapperGroup.setObjects(*((_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0)))
if mibBuilder.loadTexts:tnRoeDeMapperGroup.setStatus(_A)
tnRoeEthlinkGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,12,2,1,5))
tnRoeEthlinkGroup.setObjects(*((_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC)))
if mibBuilder.loadTexts:tnRoeEthlinkGroup.setStatus(_A)
tnRoeCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,4,12,2,2,1))
tnRoeCompliance.setObjects(*((_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH)))
if mibBuilder.loadTexts:tnRoeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TropicRoeCardType':TropicRoeCardType,'tnRoeMibModule':tnRoeMibModule,'tnRoeNotifications':tnRoeNotifications,'tnRoeObjects':tnRoeObjects,'tnRoeParameters':tnRoeParameters,'tnRoeSeqProfTable':tnRoeSeqProfTable,'tnRoeSeqProfEntry':tnRoeSeqProfEntry,_P:tnRoeSeqProfCardType,_Q:tnRoeSeqProfPortID,_R:tnRoeSeqProfID,_g:tnRoeSeqProfDescription,_h:tnRoeSeqProfType,_i:tnRoeSeqProfPMax,_j:tnRoeSeqProfPIncProp,_k:tnRoeSeqProfPInc,_l:tnRoeSeqProfQMax,_m:tnRoeSeqProfQIncProp,_n:tnRoeSeqProfQInc,_o:tnRoeSeqProfRowStatus,'tnRoeTable':tnRoeTable,'tnRoeEntry':tnRoeEntry,_T:tnRoeCardType,_J:tnRoePortID,_p:tnRoeDescription,_q:tnRoeOrderInfoType,_r:tnRoePresTimeOffset,_s:tnRoeCpriTxGenOffset,_t:tnRoeAutoUponChange,_u:tnRoeSeqNumProfID,_v:tnRoeInitialTxBFN,_w:tnRoeInitialTxHFN,_x:tnRoeEncapMode,_y:tnRoeAdminState,_z:tnRoePmonPolicy,_A0:tnRoeRowStatus,_A1:tnRoeAlmProfName,_A2:tnRoePresTimeOffsetSubNano,_A3:tnRoePresTimeOffsetNano,_A4:tnRoeTargetOffsetSubNano,_A5:tnRoeTargetOffsetNano,_A6:tnRoeMapperSampleWidth,'tnRoeDeMapperSampleWidth':tnRoeDeMapperSampleWidth,_A7:tnRoePPointer,_A8:tnRoeCpriProtocolVer,_A9:tnRoeMapperStatusEnable,_AA:tnRoeSlowcmRate,'tnRoeMapperTable':tnRoeMapperTable,'tnRoeMapperEntry':tnRoeMapperEntry,_W:tnRoeMapperCardType,_X:tnRoeMapperPortID,_Y:tnRoeMapperID,_AB:tnRoeMapperDescription,_AC:tnRoeMapperFlowID,_AD:tnRoeMappeEtherlinkID,_AE:tnRoeMapperPayloadLen,_AF:tnRoeMapperSyncMode,_AG:tnRoeMapperBfn,_AH:tnRoeMapperHfn,_AI:tnRoeMapperBfrm,_AJ:tnRoeMapperShutdown,_AK:tnRoeMapperType,_AL:tnRoeMapperOrderInfoType,_AM:tnRoeMapperPmonPolicy,_AN:tnRoeMapperRowStatus,_AO:tnRoeMapperAlmProfName,_AP:tnRoeMapperSaType,_AQ:tnRoeMapperBwID,_AR:tnRoeMapperPosition,_AS:tnRoeMapperFrameStartOffset,_AT:tnRoeMapperSchanStart,_AU:tnRoeMapperSchanSize,_AV:tnRoeMapperPincrement,_AW:tnRoeMapperNa,_AX:tnRoeMapperS,_AY:tnRoeMapperK,_AZ:tnRoeMapperNc,_Aa:tnRoeMapperNv,'tnRoeDeMapperTable':tnRoeDeMapperTable,'tnRoeDeMapperEntry':tnRoeDeMapperEntry,_b:tnRoeDeMapperCardType,'tnRoeDeMapperPortID':tnRoeDeMapperPortID,_c:tnRoeDeMapperID,_Ab:tnRoeDeMapperDescription,_Ac:tnRoeDeMappeEtherlinkID,_Ad:tnRoeDeMapperPayloadLen,_Ae:tnRoeDeMapperSyncMode,_Af:tnRoeDeMapperBfn,_Ag:tnRoeDeMapperHfn,_Ah:tnRoeDeMapperBfrm,_Ai:tnRoeDeMapperJitterBufferDepth,_Aj:tnRoeDeMapperShutdown,_Ak:tnRoeDeMapperType,_Al:tnRoeDeMapperFlowID,_Am:tnRoeDeMapperOrderInfoType,_An:tnRoeDeMapperPmonPolicy,_Ao:tnRoeDeMapperRowStatus,_Ap:tnRoeDeMapperAlmProfName,_Aq:tnRoeDeMapperSaType,_Ar:tnRoeDeMapperBwID,_As:tnRoeDeMapperPosition,_At:tnRoeDeMapperFrameStartOffset,_Au:tnRoeDeMapperSchanStart,_Av:tnRoeDeMapperSchanSize,_Aw:tnRoeDeMapperPincrement,_Ax:tnRoeDeMapperNa,_Ay:tnRoeDeMapperS,_Az:tnRoeDeMapperK,_A_:tnRoeDeMapperNc,_B0:tnRoeDeMapperNv,'tnRoeEthlinkTable':tnRoeEthlinkTable,'tnRoeEthlinkEntry':tnRoeEthlinkEntry,_d:tnRoeEthlinkCardType,_e:tnRoeEthlinkPortID,_f:tnRoeEthlinkID,_B1:tnRoeEthlinkDescription,_B2:tnRoeEthlinkDestMac,_B3:tnRoeEthlinkSourceMac,_B4:tnRoeEthlinkTagDepth,_B5:tnRoeEthlinkOuterEthertype,_B6:tnRoeEthlinkOuterVid,_B7:tnRoeEthlinkOuterPri,_B8:tnRoeEthlinkInnerEthertype,_B9:tnRoeEthlinkInnerVid,_BA:tnRoeEthlinkInnerPri,_BB:tnRoeEthlinkEthertype,_BC:tnRoeEthlinkRowStatus,'tnRoeEConf':tnRoeEConf,'tnRoeGroups':tnRoeGroups,_BD:tnRoeSeqProfGroup,_BE:tnRoeGroup,_BF:tnRoeMapperGroup,_BG:tnRoeDeMapperGroup,_BH:tnRoeEthlinkGroup,'tnEoeCompliances':tnEoeCompliances,'tnRoeCompliance':tnRoeCompliance})