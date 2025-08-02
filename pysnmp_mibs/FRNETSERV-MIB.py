_BF='frnetservMgtVCSigAdminGroup'
_BE='frnetservLportAdminGroup'
_BD='frnetservLportGroup'
_BC='frPVCConnectStatusNotif'
_BB='frPVCConnectStatusChange'
_BA='frMgtVCSigNetnT3Admin'
_B9='frMgtVCSigNetT392Admin'
_B8='frMgtVCSigNetN393Admin'
_B7='frMgtVCSigNetN392Admin'
_B6='frMgtVCSigUserT391Admin'
_B5='frMgtVCSigUserN393Admin'
_B4='frMgtVCSigUserN392Admin'
_B3='frMgtVCSigUserN391Admin'
_B2='frMgtVCSigProcedAdmin'
_B1='frLportVCSigProtocolAdmin'
_B0='frLportTypeAdmin'
_A_='frLportDLCIIndexValue'
_Az='frPVCConnectProviderName'
_Ay='frPVCConnectUserName'
_Ax='frPVCEndptAtmIwfConnIndex'
_Aw='frPVCEndptOutDEFrames'
_Av='frPVCEndptOutDECongDiscards'
_Au='frPVCEndptOutCongDiscards'
_At='frPVCEndptInDECongDiscards'
_As='frPVCEndptInCongDiscards'
_Ar='frPVCEndptOutFramesBECNSet'
_Aq='frPVCEndptInFramesBECNSet'
_Ap='frPVCEndptOutFramesFECNSet'
_Ao='frPVCEndptInFramesFECNSet'
_An='frPVCEndptInDiscardsDESet'
_Am='frLportFragSize'
_Al='frLportFragControl'
_Ak='frAccountLportOutSegments'
_Aj='frAccountLportInSegments'
_Ai='frAccountLportSegmentSize'
_Ah='frAccountPVCOutSegments'
_Ag='frAccountPVCInSegments'
_Af='frAccountPVCSegmentSize'
_Ae='frPVCConnectRowStatus'
_Ad='frPVCConnectH2lLastChange'
_Ac='frPVCConnectL2hLastChange'
_Ab='frPVCConnectAdminStatus'
_Aa='frPVCEndptOutOctets'
_AZ='frPVCEndptInOctets'
_AY='frPVCEndptInDiscards'
_AX='frPVCEndptOutExcessFrames'
_AW='frPVCEndptInExcessFrames'
_AV='frPVCEndptInDEFrames'
_AU='frPVCEndptOutFrames'
_AT='frPVCEndptInFrames'
_AS='frPVCEndptRowStatus'
_AR='frPVCEndptConnectIdentifier'
_AQ='frPVCEndptOutCIR'
_AP='frPVCEndptOutBe'
_AO='frPVCEndptOutBc'
_AN='frPVCEndptOutMaxFrameSize'
_AM='frPVCEndptInCIR'
_AL='frPVCEndptInBe'
_AK='frPVCEndptInBc'
_AJ='frPVCEndptInMaxFrameSize'
_AI='frPVCConnectIndexValue'
_AH='frMgtVCSigNetChanInactive'
_AG='frMgtVCSigNetProtErrors'
_AF='frMgtVCSigNetLinkRelErrors'
_AE='frMgtVCSigUserChanInactive'
_AD='frMgtVCSigUserProtErrors'
_AC='frMgtVCSigUserLinkRelErrors'
_AB='frMgtVCSigNetnT3'
_AA='frMgtVCSigNetnN4'
_A9='frMgtVCSigNetT392'
_A8='frMgtVCSigNetN393'
_A7='frMgtVCSigNetN392'
_A6='frMgtVCSigUserT391'
_A5='frMgtVCSigUserN393'
_A4='frMgtVCSigUserN392'
_A3='frMgtVCSigUserN391'
_A2='frMgtVCSigProced'
_A1='frLportVCSigPointer'
_A0='frAccountPVCDLCIIndex'
_z='Bits per Second'
_y='frPVCEndptDLCIIndex'
_x='u2nuser'
_w='bidirect'
_v='u2nnet'
_u='ccittQ933A'
_t='ansiT1617B'
_s='ansiT1617D'
_r='frnetservPVCNotifGroup2'
_q='frnetservPVCConnectNamesGroup'
_p='frnetservPVCEndptGroup2'
_o='frnetservLportGroup2'
_n='frLportVCSigProtocol'
_m='frLportAddrDLCILen'
_l='frLportType'
_k='frLportLocation'
_j='frLportContact'
_i='frLportNumPlan'
_h='testing'
_g='frPVCConnectHighDLCIIndex'
_f='frPVCConnectHighIfIndex'
_e='frPVCConnectLowDLCIIndex'
_d='frPVCConnectLowIfIndex'
_c='frPVCConnectIndex'
_b='frnetservAccountLportGroup'
_a='frnetservAccountPVCGroup'
_Z='frnetservPVCConnectGroup'
_Y='frnetservPVCEndptGroup'
_X='frnetservMgtVCSigGroup'
_W='frPVCConnectH2lOperStatus'
_V='frPVCConnectL2hOperStatus'
_U='frPVCEndptRcvdSigStatus'
_T='Segments'
_S='inactive'
_R='active'
_Q='Errors'
_P='none'
_O='deprecated'
_N='Bits'
_M='Seconds'
_L='ifIndex'
_K='IF-MIB'
_J='not-accessible'
_I='Octets'
_H='Events'
_G='read-create'
_F='read-write'
_E='Frames'
_D='Integer32'
_C='read-only'
_B='current'
_A='FRNETSERV-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_K,'InterfaceIndex',_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI',_N,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
frnetservMIB=ModuleIdentity((1,3,6,1,2,1,10,44))
if mibBuilder.loadTexts:frnetservMIB.setRevisions(('2000-09-28 00:00','1993-11-16 12:00'))
_FrnetservObjects_ObjectIdentity=ObjectIdentity
frnetservObjects=_FrnetservObjects_ObjectIdentity((1,3,6,1,2,1,10,44,1))
_FrLportTable_Object=MibTable
frLportTable=_FrLportTable_Object((1,3,6,1,2,1,10,44,1,1))
if mibBuilder.loadTexts:frLportTable.setStatus(_B)
_FrLportEntry_Object=MibTableRow
frLportEntry=_FrLportEntry_Object((1,3,6,1,2,1,10,44,1,1,1))
frLportEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:frLportEntry.setStatus(_B)
class _FrLportNumPlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('e164',2),('x121',3),(_P,4)))
_FrLportNumPlan_Type.__name__=_D
_FrLportNumPlan_Object=MibTableColumn
frLportNumPlan=_FrLportNumPlan_Object((1,3,6,1,2,1,10,44,1,1,1,1),_FrLportNumPlan_Type())
frLportNumPlan.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportNumPlan.setStatus(_B)
_FrLportContact_Type=SnmpAdminString
_FrLportContact_Object=MibTableColumn
frLportContact=_FrLportContact_Object((1,3,6,1,2,1,10,44,1,1,1,2),_FrLportContact_Type())
frLportContact.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportContact.setStatus(_B)
_FrLportLocation_Type=SnmpAdminString
_FrLportLocation_Object=MibTableColumn
frLportLocation=_FrLportLocation_Object((1,3,6,1,2,1,10,44,1,1,1,3),_FrLportLocation_Type())
frLportLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportLocation.setStatus(_B)
class _FrLportType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uni',1),('nni',2)))
_FrLportType_Type.__name__=_D
_FrLportType_Object=MibTableColumn
frLportType=_FrLportType_Object((1,3,6,1,2,1,10,44,1,1,1,4),_FrLportType_Type())
frLportType.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportType.setStatus(_B)
class _FrLportAddrDLCILen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('twoOctets10Bits',1),('threeOctets10Bits',2),('threeOctets16Bits',3),('fourOctets17Bits',4),('fourOctets23Bits',5)))
_FrLportAddrDLCILen_Type.__name__=_D
_FrLportAddrDLCILen_Object=MibTableColumn
frLportAddrDLCILen=_FrLportAddrDLCILen_Object((1,3,6,1,2,1,10,44,1,1,1,5),_FrLportAddrDLCILen_Type())
frLportAddrDLCILen.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportAddrDLCILen.setStatus(_B)
if mibBuilder.loadTexts:frLportAddrDLCILen.setUnits(_I)
class _FrLportVCSigProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('lmi',2),(_s,3),(_t,4),(_u,5)))
_FrLportVCSigProtocol_Type.__name__=_D
_FrLportVCSigProtocol_Object=MibTableColumn
frLportVCSigProtocol=_FrLportVCSigProtocol_Object((1,3,6,1,2,1,10,44,1,1,1,6),_FrLportVCSigProtocol_Type())
frLportVCSigProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportVCSigProtocol.setStatus(_B)
_FrLportVCSigPointer_Type=ObjectIdentifier
_FrLportVCSigPointer_Object=MibTableColumn
frLportVCSigPointer=_FrLportVCSigPointer_Object((1,3,6,1,2,1,10,44,1,1,1,7),_FrLportVCSigPointer_Type())
frLportVCSigPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportVCSigPointer.setStatus(_O)
class _FrLportDLCIIndexValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4194303))
_FrLportDLCIIndexValue_Type.__name__=_D
_FrLportDLCIIndexValue_Object=MibTableColumn
frLportDLCIIndexValue=_FrLportDLCIIndexValue_Object((1,3,6,1,2,1,10,44,1,1,1,8),_FrLportDLCIIndexValue_Type())
frLportDLCIIndexValue.setMaxAccess(_C)
if mibBuilder.loadTexts:frLportDLCIIndexValue.setStatus(_B)
class _FrLportTypeAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uni',1),('nni',2)))
_FrLportTypeAdmin_Type.__name__=_D
_FrLportTypeAdmin_Object=MibTableColumn
frLportTypeAdmin=_FrLportTypeAdmin_Object((1,3,6,1,2,1,10,44,1,1,1,9),_FrLportTypeAdmin_Type())
frLportTypeAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:frLportTypeAdmin.setStatus(_B)
class _FrLportVCSigProtocolAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('lmi',2),(_s,3),(_t,4),(_u,5)))
_FrLportVCSigProtocolAdmin_Type.__name__=_D
_FrLportVCSigProtocolAdmin_Object=MibTableColumn
frLportVCSigProtocolAdmin=_FrLportVCSigProtocolAdmin_Object((1,3,6,1,2,1,10,44,1,1,1,10),_FrLportVCSigProtocolAdmin_Type())
frLportVCSigProtocolAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:frLportVCSigProtocolAdmin.setStatus(_B)
class _FrLportFragControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_FrLportFragControl_Type.__name__=_D
_FrLportFragControl_Object=MibTableColumn
frLportFragControl=_FrLportFragControl_Object((1,3,6,1,2,1,10,44,1,1,1,11),_FrLportFragControl_Type())
frLportFragControl.setMaxAccess(_F)
if mibBuilder.loadTexts:frLportFragControl.setStatus(_B)
class _FrLportFragSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_FrLportFragSize_Type.__name__=_D
_FrLportFragSize_Object=MibTableColumn
frLportFragSize=_FrLportFragSize_Object((1,3,6,1,2,1,10,44,1,1,1,12),_FrLportFragSize_Type())
frLportFragSize.setMaxAccess(_F)
if mibBuilder.loadTexts:frLportFragSize.setStatus(_B)
if mibBuilder.loadTexts:frLportFragSize.setUnits(_I)
_FrMgtVCSigTable_Object=MibTable
frMgtVCSigTable=_FrMgtVCSigTable_Object((1,3,6,1,2,1,10,44,1,2))
if mibBuilder.loadTexts:frMgtVCSigTable.setStatus(_B)
_FrMgtVCSigEntry_Object=MibTableRow
frMgtVCSigEntry=_FrMgtVCSigEntry_Object((1,3,6,1,2,1,10,44,1,2,1))
frMgtVCSigEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:frMgtVCSigEntry.setStatus(_B)
class _FrMgtVCSigProced_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3)))
_FrMgtVCSigProced_Type.__name__=_D
_FrMgtVCSigProced_Object=MibTableColumn
frMgtVCSigProced=_FrMgtVCSigProced_Object((1,3,6,1,2,1,10,44,1,2,1,1),_FrMgtVCSigProced_Type())
frMgtVCSigProced.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigProced.setStatus(_B)
class _FrMgtVCSigUserN391_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrMgtVCSigUserN391_Type.__name__=_D
_FrMgtVCSigUserN391_Object=MibTableColumn
frMgtVCSigUserN391=_FrMgtVCSigUserN391_Object((1,3,6,1,2,1,10,44,1,2,1,2),_FrMgtVCSigUserN391_Type())
frMgtVCSigUserN391.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigUserN391.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserN391.setUnits('Polls')
class _FrMgtVCSigUserN392_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigUserN392_Type.__name__=_D
_FrMgtVCSigUserN392_Object=MibTableColumn
frMgtVCSigUserN392=_FrMgtVCSigUserN392_Object((1,3,6,1,2,1,10,44,1,2,1,3),_FrMgtVCSigUserN392_Type())
frMgtVCSigUserN392.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigUserN392.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserN392.setUnits(_H)
class _FrMgtVCSigUserN393_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigUserN393_Type.__name__=_D
_FrMgtVCSigUserN393_Object=MibTableColumn
frMgtVCSigUserN393=_FrMgtVCSigUserN393_Object((1,3,6,1,2,1,10,44,1,2,1,4),_FrMgtVCSigUserN393_Type())
frMgtVCSigUserN393.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigUserN393.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserN393.setUnits(_H)
class _FrMgtVCSigUserT391_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrMgtVCSigUserT391_Type.__name__=_D
_FrMgtVCSigUserT391_Object=MibTableColumn
frMgtVCSigUserT391=_FrMgtVCSigUserT391_Object((1,3,6,1,2,1,10,44,1,2,1,5),_FrMgtVCSigUserT391_Type())
frMgtVCSigUserT391.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigUserT391.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserT391.setUnits(_M)
class _FrMgtVCSigNetN392_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigNetN392_Type.__name__=_D
_FrMgtVCSigNetN392_Object=MibTableColumn
frMgtVCSigNetN392=_FrMgtVCSigNetN392_Object((1,3,6,1,2,1,10,44,1,2,1,6),_FrMgtVCSigNetN392_Type())
frMgtVCSigNetN392.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetN392.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetN392.setUnits(_H)
class _FrMgtVCSigNetN393_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigNetN393_Type.__name__=_D
_FrMgtVCSigNetN393_Object=MibTableColumn
frMgtVCSigNetN393=_FrMgtVCSigNetN393_Object((1,3,6,1,2,1,10,44,1,2,1,7),_FrMgtVCSigNetN393_Type())
frMgtVCSigNetN393.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetN393.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetN393.setUnits(_H)
class _FrMgtVCSigNetT392_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrMgtVCSigNetT392_Type.__name__=_D
_FrMgtVCSigNetT392_Object=MibTableColumn
frMgtVCSigNetT392=_FrMgtVCSigNetT392_Object((1,3,6,1,2,1,10,44,1,2,1,8),_FrMgtVCSigNetT392_Type())
frMgtVCSigNetT392.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetT392.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetT392.setUnits(_M)
class _FrMgtVCSigNetnN4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5))
_FrMgtVCSigNetnN4_Type.__name__=_D
_FrMgtVCSigNetnN4_Object=MibTableColumn
frMgtVCSigNetnN4=_FrMgtVCSigNetnN4_Object((1,3,6,1,2,1,10,44,1,2,1,9),_FrMgtVCSigNetnN4_Type())
frMgtVCSigNetnN4.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetnN4.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetnN4.setUnits(_H)
class _FrMgtVCSigNetnT3_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5),ValueRangeConstraint(10,10),ValueRangeConstraint(15,15),ValueRangeConstraint(20,20),ValueRangeConstraint(25,25),ValueRangeConstraint(30,30))
_FrMgtVCSigNetnT3_Type.__name__=_D
_FrMgtVCSigNetnT3_Object=MibTableColumn
frMgtVCSigNetnT3=_FrMgtVCSigNetnT3_Object((1,3,6,1,2,1,10,44,1,2,1,10),_FrMgtVCSigNetnT3_Type())
frMgtVCSigNetnT3.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetnT3.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetnT3.setUnits(_M)
_FrMgtVCSigUserLinkRelErrors_Type=Counter32
_FrMgtVCSigUserLinkRelErrors_Object=MibTableColumn
frMgtVCSigUserLinkRelErrors=_FrMgtVCSigUserLinkRelErrors_Object((1,3,6,1,2,1,10,44,1,2,1,11),_FrMgtVCSigUserLinkRelErrors_Type())
frMgtVCSigUserLinkRelErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigUserLinkRelErrors.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserLinkRelErrors.setUnits(_Q)
_FrMgtVCSigUserProtErrors_Type=Counter32
_FrMgtVCSigUserProtErrors_Object=MibTableColumn
frMgtVCSigUserProtErrors=_FrMgtVCSigUserProtErrors_Object((1,3,6,1,2,1,10,44,1,2,1,12),_FrMgtVCSigUserProtErrors_Type())
frMgtVCSigUserProtErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigUserProtErrors.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserProtErrors.setUnits(_Q)
_FrMgtVCSigUserChanInactive_Type=Counter32
_FrMgtVCSigUserChanInactive_Object=MibTableColumn
frMgtVCSigUserChanInactive=_FrMgtVCSigUserChanInactive_Object((1,3,6,1,2,1,10,44,1,2,1,13),_FrMgtVCSigUserChanInactive_Type())
frMgtVCSigUserChanInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigUserChanInactive.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserChanInactive.setUnits(_H)
_FrMgtVCSigNetLinkRelErrors_Type=Counter32
_FrMgtVCSigNetLinkRelErrors_Object=MibTableColumn
frMgtVCSigNetLinkRelErrors=_FrMgtVCSigNetLinkRelErrors_Object((1,3,6,1,2,1,10,44,1,2,1,14),_FrMgtVCSigNetLinkRelErrors_Type())
frMgtVCSigNetLinkRelErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetLinkRelErrors.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetLinkRelErrors.setUnits(_Q)
_FrMgtVCSigNetProtErrors_Type=Counter32
_FrMgtVCSigNetProtErrors_Object=MibTableColumn
frMgtVCSigNetProtErrors=_FrMgtVCSigNetProtErrors_Object((1,3,6,1,2,1,10,44,1,2,1,15),_FrMgtVCSigNetProtErrors_Type())
frMgtVCSigNetProtErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetProtErrors.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetProtErrors.setUnits(_Q)
_FrMgtVCSigNetChanInactive_Type=Counter32
_FrMgtVCSigNetChanInactive_Object=MibTableColumn
frMgtVCSigNetChanInactive=_FrMgtVCSigNetChanInactive_Object((1,3,6,1,2,1,10,44,1,2,1,16),_FrMgtVCSigNetChanInactive_Type())
frMgtVCSigNetChanInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:frMgtVCSigNetChanInactive.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetChanInactive.setUnits(_H)
class _FrMgtVCSigProcedAdmin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3)))
_FrMgtVCSigProcedAdmin_Type.__name__=_D
_FrMgtVCSigProcedAdmin_Object=MibTableColumn
frMgtVCSigProcedAdmin=_FrMgtVCSigProcedAdmin_Object((1,3,6,1,2,1,10,44,1,2,1,17),_FrMgtVCSigProcedAdmin_Type())
frMgtVCSigProcedAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigProcedAdmin.setStatus(_B)
class _FrMgtVCSigUserN391Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrMgtVCSigUserN391Admin_Type.__name__=_D
_FrMgtVCSigUserN391Admin_Object=MibTableColumn
frMgtVCSigUserN391Admin=_FrMgtVCSigUserN391Admin_Object((1,3,6,1,2,1,10,44,1,2,1,18),_FrMgtVCSigUserN391Admin_Type())
frMgtVCSigUserN391Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigUserN391Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserN391Admin.setUnits('Polls')
class _FrMgtVCSigUserN392Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigUserN392Admin_Type.__name__=_D
_FrMgtVCSigUserN392Admin_Object=MibTableColumn
frMgtVCSigUserN392Admin=_FrMgtVCSigUserN392Admin_Object((1,3,6,1,2,1,10,44,1,2,1,19),_FrMgtVCSigUserN392Admin_Type())
frMgtVCSigUserN392Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigUserN392Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserN392Admin.setUnits(_H)
class _FrMgtVCSigUserN393Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigUserN393Admin_Type.__name__=_D
_FrMgtVCSigUserN393Admin_Object=MibTableColumn
frMgtVCSigUserN393Admin=_FrMgtVCSigUserN393Admin_Object((1,3,6,1,2,1,10,44,1,2,1,20),_FrMgtVCSigUserN393Admin_Type())
frMgtVCSigUserN393Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigUserN393Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserN393Admin.setUnits(_H)
class _FrMgtVCSigUserT391Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrMgtVCSigUserT391Admin_Type.__name__=_D
_FrMgtVCSigUserT391Admin_Object=MibTableColumn
frMgtVCSigUserT391Admin=_FrMgtVCSigUserT391Admin_Object((1,3,6,1,2,1,10,44,1,2,1,21),_FrMgtVCSigUserT391Admin_Type())
frMgtVCSigUserT391Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigUserT391Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigUserT391Admin.setUnits(_M)
class _FrMgtVCSigNetN392Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigNetN392Admin_Type.__name__=_D
_FrMgtVCSigNetN392Admin_Object=MibTableColumn
frMgtVCSigNetN392Admin=_FrMgtVCSigNetN392Admin_Object((1,3,6,1,2,1,10,44,1,2,1,22),_FrMgtVCSigNetN392Admin_Type())
frMgtVCSigNetN392Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigNetN392Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetN392Admin.setUnits(_H)
class _FrMgtVCSigNetN393Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrMgtVCSigNetN393Admin_Type.__name__=_D
_FrMgtVCSigNetN393Admin_Object=MibTableColumn
frMgtVCSigNetN393Admin=_FrMgtVCSigNetN393Admin_Object((1,3,6,1,2,1,10,44,1,2,1,23),_FrMgtVCSigNetN393Admin_Type())
frMgtVCSigNetN393Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigNetN393Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetN393Admin.setUnits(_H)
class _FrMgtVCSigNetT392Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrMgtVCSigNetT392Admin_Type.__name__=_D
_FrMgtVCSigNetT392Admin_Object=MibTableColumn
frMgtVCSigNetT392Admin=_FrMgtVCSigNetT392Admin_Object((1,3,6,1,2,1,10,44,1,2,1,24),_FrMgtVCSigNetT392Admin_Type())
frMgtVCSigNetT392Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigNetT392Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetT392Admin.setUnits(_M)
class _FrMgtVCSigNetnT3Admin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5),ValueRangeConstraint(10,10),ValueRangeConstraint(15,15),ValueRangeConstraint(20,20),ValueRangeConstraint(25,25),ValueRangeConstraint(30,30))
_FrMgtVCSigNetnT3Admin_Type.__name__=_D
_FrMgtVCSigNetnT3Admin_Object=MibTableColumn
frMgtVCSigNetnT3Admin=_FrMgtVCSigNetnT3Admin_Object((1,3,6,1,2,1,10,44,1,2,1,25),_FrMgtVCSigNetnT3Admin_Type())
frMgtVCSigNetnT3Admin.setMaxAccess(_F)
if mibBuilder.loadTexts:frMgtVCSigNetnT3Admin.setStatus(_B)
if mibBuilder.loadTexts:frMgtVCSigNetnT3Admin.setUnits(_M)
_FrPVCEndptTable_Object=MibTable
frPVCEndptTable=_FrPVCEndptTable_Object((1,3,6,1,2,1,10,44,1,3))
if mibBuilder.loadTexts:frPVCEndptTable.setStatus(_B)
_FrPVCEndptEntry_Object=MibTableRow
frPVCEndptEntry=_FrPVCEndptEntry_Object((1,3,6,1,2,1,10,44,1,3,1))
frPVCEndptEntry.setIndexNames((0,_K,_L),(0,_A,_y))
if mibBuilder.loadTexts:frPVCEndptEntry.setStatus(_B)
class _FrPVCEndptDLCIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4194303))
_FrPVCEndptDLCIIndex_Type.__name__=_D
_FrPVCEndptDLCIIndex_Object=MibTableColumn
frPVCEndptDLCIIndex=_FrPVCEndptDLCIIndex_Object((1,3,6,1,2,1,10,44,1,3,1,1),_FrPVCEndptDLCIIndex_Type())
frPVCEndptDLCIIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:frPVCEndptDLCIIndex.setStatus(_B)
class _FrPVCEndptInMaxFrameSize_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FrPVCEndptInMaxFrameSize_Type.__name__=_D
_FrPVCEndptInMaxFrameSize_Object=MibTableColumn
frPVCEndptInMaxFrameSize=_FrPVCEndptInMaxFrameSize_Object((1,3,6,1,2,1,10,44,1,3,1,2),_FrPVCEndptInMaxFrameSize_Type())
frPVCEndptInMaxFrameSize.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptInMaxFrameSize.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInMaxFrameSize.setUnits(_I)
class _FrPVCEndptInBc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrPVCEndptInBc_Type.__name__=_D
_FrPVCEndptInBc_Object=MibTableColumn
frPVCEndptInBc=_FrPVCEndptInBc_Object((1,3,6,1,2,1,10,44,1,3,1,3),_FrPVCEndptInBc_Type())
frPVCEndptInBc.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptInBc.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInBc.setUnits(_N)
class _FrPVCEndptInBe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrPVCEndptInBe_Type.__name__=_D
_FrPVCEndptInBe_Object=MibTableColumn
frPVCEndptInBe=_FrPVCEndptInBe_Object((1,3,6,1,2,1,10,44,1,3,1,4),_FrPVCEndptInBe_Type())
frPVCEndptInBe.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptInBe.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInBe.setUnits(_N)
class _FrPVCEndptInCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrPVCEndptInCIR_Type.__name__=_D
_FrPVCEndptInCIR_Object=MibTableColumn
frPVCEndptInCIR=_FrPVCEndptInCIR_Object((1,3,6,1,2,1,10,44,1,3,1,5),_FrPVCEndptInCIR_Type())
frPVCEndptInCIR.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptInCIR.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInCIR.setUnits(_z)
class _FrPVCEndptOutMaxFrameSize_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FrPVCEndptOutMaxFrameSize_Type.__name__=_D
_FrPVCEndptOutMaxFrameSize_Object=MibTableColumn
frPVCEndptOutMaxFrameSize=_FrPVCEndptOutMaxFrameSize_Object((1,3,6,1,2,1,10,44,1,3,1,6),_FrPVCEndptOutMaxFrameSize_Type())
frPVCEndptOutMaxFrameSize.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptOutMaxFrameSize.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutMaxFrameSize.setUnits(_I)
class _FrPVCEndptOutBc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrPVCEndptOutBc_Type.__name__=_D
_FrPVCEndptOutBc_Object=MibTableColumn
frPVCEndptOutBc=_FrPVCEndptOutBc_Object((1,3,6,1,2,1,10,44,1,3,1,7),_FrPVCEndptOutBc_Type())
frPVCEndptOutBc.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptOutBc.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutBc.setUnits(_N)
class _FrPVCEndptOutBe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrPVCEndptOutBe_Type.__name__=_D
_FrPVCEndptOutBe_Object=MibTableColumn
frPVCEndptOutBe=_FrPVCEndptOutBe_Object((1,3,6,1,2,1,10,44,1,3,1,8),_FrPVCEndptOutBe_Type())
frPVCEndptOutBe.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptOutBe.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutBe.setUnits(_N)
class _FrPVCEndptOutCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrPVCEndptOutCIR_Type.__name__=_D
_FrPVCEndptOutCIR_Object=MibTableColumn
frPVCEndptOutCIR=_FrPVCEndptOutCIR_Object((1,3,6,1,2,1,10,44,1,3,1,9),_FrPVCEndptOutCIR_Type())
frPVCEndptOutCIR.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptOutCIR.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutCIR.setUnits(_z)
class _FrPVCEndptConnectIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrPVCEndptConnectIdentifier_Type.__name__=_D
_FrPVCEndptConnectIdentifier_Object=MibTableColumn
frPVCEndptConnectIdentifier=_FrPVCEndptConnectIdentifier_Object((1,3,6,1,2,1,10,44,1,3,1,10),_FrPVCEndptConnectIdentifier_Type())
frPVCEndptConnectIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptConnectIdentifier.setStatus(_B)
_FrPVCEndptRowStatus_Type=RowStatus
_FrPVCEndptRowStatus_Object=MibTableColumn
frPVCEndptRowStatus=_FrPVCEndptRowStatus_Object((1,3,6,1,2,1,10,44,1,3,1,11),_FrPVCEndptRowStatus_Type())
frPVCEndptRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCEndptRowStatus.setStatus(_B)
class _FrPVCEndptRcvdSigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('deleted',1),(_R,2),(_S,3),(_P,4)))
_FrPVCEndptRcvdSigStatus_Type.__name__=_D
_FrPVCEndptRcvdSigStatus_Object=MibTableColumn
frPVCEndptRcvdSigStatus=_FrPVCEndptRcvdSigStatus_Object((1,3,6,1,2,1,10,44,1,3,1,12),_FrPVCEndptRcvdSigStatus_Type())
frPVCEndptRcvdSigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptRcvdSigStatus.setStatus(_B)
_FrPVCEndptInFrames_Type=Counter32
_FrPVCEndptInFrames_Object=MibTableColumn
frPVCEndptInFrames=_FrPVCEndptInFrames_Object((1,3,6,1,2,1,10,44,1,3,1,13),_FrPVCEndptInFrames_Type())
frPVCEndptInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInFrames.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInFrames.setUnits(_E)
_FrPVCEndptOutFrames_Type=Counter32
_FrPVCEndptOutFrames_Object=MibTableColumn
frPVCEndptOutFrames=_FrPVCEndptOutFrames_Object((1,3,6,1,2,1,10,44,1,3,1,14),_FrPVCEndptOutFrames_Type())
frPVCEndptOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutFrames.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutFrames.setUnits(_E)
_FrPVCEndptInDEFrames_Type=Counter32
_FrPVCEndptInDEFrames_Object=MibTableColumn
frPVCEndptInDEFrames=_FrPVCEndptInDEFrames_Object((1,3,6,1,2,1,10,44,1,3,1,15),_FrPVCEndptInDEFrames_Type())
frPVCEndptInDEFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInDEFrames.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInDEFrames.setUnits(_E)
_FrPVCEndptInExcessFrames_Type=Counter32
_FrPVCEndptInExcessFrames_Object=MibTableColumn
frPVCEndptInExcessFrames=_FrPVCEndptInExcessFrames_Object((1,3,6,1,2,1,10,44,1,3,1,16),_FrPVCEndptInExcessFrames_Type())
frPVCEndptInExcessFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInExcessFrames.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInExcessFrames.setUnits(_E)
_FrPVCEndptOutExcessFrames_Type=Counter32
_FrPVCEndptOutExcessFrames_Object=MibTableColumn
frPVCEndptOutExcessFrames=_FrPVCEndptOutExcessFrames_Object((1,3,6,1,2,1,10,44,1,3,1,17),_FrPVCEndptOutExcessFrames_Type())
frPVCEndptOutExcessFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutExcessFrames.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutExcessFrames.setUnits(_E)
_FrPVCEndptInDiscards_Type=Counter32
_FrPVCEndptInDiscards_Object=MibTableColumn
frPVCEndptInDiscards=_FrPVCEndptInDiscards_Object((1,3,6,1,2,1,10,44,1,3,1,18),_FrPVCEndptInDiscards_Type())
frPVCEndptInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInDiscards.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInDiscards.setUnits(_E)
_FrPVCEndptInOctets_Type=Counter32
_FrPVCEndptInOctets_Object=MibTableColumn
frPVCEndptInOctets=_FrPVCEndptInOctets_Object((1,3,6,1,2,1,10,44,1,3,1,19),_FrPVCEndptInOctets_Type())
frPVCEndptInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInOctets.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInOctets.setUnits(_I)
_FrPVCEndptOutOctets_Type=Counter32
_FrPVCEndptOutOctets_Object=MibTableColumn
frPVCEndptOutOctets=_FrPVCEndptOutOctets_Object((1,3,6,1,2,1,10,44,1,3,1,20),_FrPVCEndptOutOctets_Type())
frPVCEndptOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutOctets.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutOctets.setUnits(_I)
_FrPVCEndptInDiscardsDESet_Type=Counter32
_FrPVCEndptInDiscardsDESet_Object=MibTableColumn
frPVCEndptInDiscardsDESet=_FrPVCEndptInDiscardsDESet_Object((1,3,6,1,2,1,10,44,1,3,1,21),_FrPVCEndptInDiscardsDESet_Type())
frPVCEndptInDiscardsDESet.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInDiscardsDESet.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInDiscardsDESet.setUnits(_E)
_FrPVCEndptInFramesFECNSet_Type=Counter32
_FrPVCEndptInFramesFECNSet_Object=MibTableColumn
frPVCEndptInFramesFECNSet=_FrPVCEndptInFramesFECNSet_Object((1,3,6,1,2,1,10,44,1,3,1,22),_FrPVCEndptInFramesFECNSet_Type())
frPVCEndptInFramesFECNSet.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInFramesFECNSet.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInFramesFECNSet.setUnits(_E)
_FrPVCEndptOutFramesFECNSet_Type=Counter32
_FrPVCEndptOutFramesFECNSet_Object=MibTableColumn
frPVCEndptOutFramesFECNSet=_FrPVCEndptOutFramesFECNSet_Object((1,3,6,1,2,1,10,44,1,3,1,23),_FrPVCEndptOutFramesFECNSet_Type())
frPVCEndptOutFramesFECNSet.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutFramesFECNSet.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutFramesFECNSet.setUnits(_E)
_FrPVCEndptInFramesBECNSet_Type=Counter32
_FrPVCEndptInFramesBECNSet_Object=MibTableColumn
frPVCEndptInFramesBECNSet=_FrPVCEndptInFramesBECNSet_Object((1,3,6,1,2,1,10,44,1,3,1,24),_FrPVCEndptInFramesBECNSet_Type())
frPVCEndptInFramesBECNSet.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInFramesBECNSet.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInFramesBECNSet.setUnits(_E)
_FrPVCEndptOutFramesBECNSet_Type=Counter32
_FrPVCEndptOutFramesBECNSet_Object=MibTableColumn
frPVCEndptOutFramesBECNSet=_FrPVCEndptOutFramesBECNSet_Object((1,3,6,1,2,1,10,44,1,3,1,25),_FrPVCEndptOutFramesBECNSet_Type())
frPVCEndptOutFramesBECNSet.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutFramesBECNSet.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutFramesBECNSet.setUnits(_E)
_FrPVCEndptInCongDiscards_Type=Counter32
_FrPVCEndptInCongDiscards_Object=MibTableColumn
frPVCEndptInCongDiscards=_FrPVCEndptInCongDiscards_Object((1,3,6,1,2,1,10,44,1,3,1,26),_FrPVCEndptInCongDiscards_Type())
frPVCEndptInCongDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInCongDiscards.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInCongDiscards.setUnits(_E)
_FrPVCEndptInDECongDiscards_Type=Counter32
_FrPVCEndptInDECongDiscards_Object=MibTableColumn
frPVCEndptInDECongDiscards=_FrPVCEndptInDECongDiscards_Object((1,3,6,1,2,1,10,44,1,3,1,27),_FrPVCEndptInDECongDiscards_Type())
frPVCEndptInDECongDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptInDECongDiscards.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptInDECongDiscards.setUnits(_E)
_FrPVCEndptOutCongDiscards_Type=Counter32
_FrPVCEndptOutCongDiscards_Object=MibTableColumn
frPVCEndptOutCongDiscards=_FrPVCEndptOutCongDiscards_Object((1,3,6,1,2,1,10,44,1,3,1,28),_FrPVCEndptOutCongDiscards_Type())
frPVCEndptOutCongDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutCongDiscards.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutCongDiscards.setUnits(_E)
_FrPVCEndptOutDECongDiscards_Type=Counter32
_FrPVCEndptOutDECongDiscards_Object=MibTableColumn
frPVCEndptOutDECongDiscards=_FrPVCEndptOutDECongDiscards_Object((1,3,6,1,2,1,10,44,1,3,1,29),_FrPVCEndptOutDECongDiscards_Type())
frPVCEndptOutDECongDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutDECongDiscards.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutDECongDiscards.setUnits(_E)
_FrPVCEndptOutDEFrames_Type=Counter32
_FrPVCEndptOutDEFrames_Object=MibTableColumn
frPVCEndptOutDEFrames=_FrPVCEndptOutDEFrames_Object((1,3,6,1,2,1,10,44,1,3,1,30),_FrPVCEndptOutDEFrames_Type())
frPVCEndptOutDEFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptOutDEFrames.setStatus(_B)
if mibBuilder.loadTexts:frPVCEndptOutDEFrames.setUnits(_E)
class _FrPVCEndptAtmIwfConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrPVCEndptAtmIwfConnIndex_Type.__name__=_D
_FrPVCEndptAtmIwfConnIndex_Object=MibTableColumn
frPVCEndptAtmIwfConnIndex=_FrPVCEndptAtmIwfConnIndex_Object((1,3,6,1,2,1,10,44,1,3,1,31),_FrPVCEndptAtmIwfConnIndex_Type())
frPVCEndptAtmIwfConnIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCEndptAtmIwfConnIndex.setStatus(_B)
class _FrPVCConnectIndexValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrPVCConnectIndexValue_Type.__name__=_D
_FrPVCConnectIndexValue_Object=MibScalar
frPVCConnectIndexValue=_FrPVCConnectIndexValue_Object((1,3,6,1,2,1,10,44,1,4),_FrPVCConnectIndexValue_Type())
frPVCConnectIndexValue.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCConnectIndexValue.setStatus(_B)
_FrPVCConnectTable_Object=MibTable
frPVCConnectTable=_FrPVCConnectTable_Object((1,3,6,1,2,1,10,44,1,5))
if mibBuilder.loadTexts:frPVCConnectTable.setStatus(_B)
_FrPVCConnectEntry_Object=MibTableRow
frPVCConnectEntry=_FrPVCConnectEntry_Object((1,3,6,1,2,1,10,44,1,5,1))
frPVCConnectEntry.setIndexNames((0,_A,_c),(0,_A,_d),(0,_A,_e),(0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:frPVCConnectEntry.setStatus(_B)
class _FrPVCConnectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrPVCConnectIndex_Type.__name__=_D
_FrPVCConnectIndex_Object=MibTableColumn
frPVCConnectIndex=_FrPVCConnectIndex_Object((1,3,6,1,2,1,10,44,1,5,1,1),_FrPVCConnectIndex_Type())
frPVCConnectIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:frPVCConnectIndex.setStatus(_B)
_FrPVCConnectLowIfIndex_Type=InterfaceIndex
_FrPVCConnectLowIfIndex_Object=MibTableColumn
frPVCConnectLowIfIndex=_FrPVCConnectLowIfIndex_Object((1,3,6,1,2,1,10,44,1,5,1,2),_FrPVCConnectLowIfIndex_Type())
frPVCConnectLowIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:frPVCConnectLowIfIndex.setStatus(_B)
class _FrPVCConnectLowDLCIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4194303))
_FrPVCConnectLowDLCIIndex_Type.__name__=_D
_FrPVCConnectLowDLCIIndex_Object=MibTableColumn
frPVCConnectLowDLCIIndex=_FrPVCConnectLowDLCIIndex_Object((1,3,6,1,2,1,10,44,1,5,1,3),_FrPVCConnectLowDLCIIndex_Type())
frPVCConnectLowDLCIIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:frPVCConnectLowDLCIIndex.setStatus(_B)
_FrPVCConnectHighIfIndex_Type=InterfaceIndex
_FrPVCConnectHighIfIndex_Object=MibTableColumn
frPVCConnectHighIfIndex=_FrPVCConnectHighIfIndex_Object((1,3,6,1,2,1,10,44,1,5,1,4),_FrPVCConnectHighIfIndex_Type())
frPVCConnectHighIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:frPVCConnectHighIfIndex.setStatus(_B)
class _FrPVCConnectHighDLCIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4194303))
_FrPVCConnectHighDLCIIndex_Type.__name__=_D
_FrPVCConnectHighDLCIIndex_Object=MibTableColumn
frPVCConnectHighDLCIIndex=_FrPVCConnectHighDLCIIndex_Object((1,3,6,1,2,1,10,44,1,5,1,5),_FrPVCConnectHighDLCIIndex_Type())
frPVCConnectHighDLCIIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:frPVCConnectHighDLCIIndex.setStatus(_B)
class _FrPVCConnectAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_h,3)))
_FrPVCConnectAdminStatus_Type.__name__=_D
_FrPVCConnectAdminStatus_Object=MibTableColumn
frPVCConnectAdminStatus=_FrPVCConnectAdminStatus_Object((1,3,6,1,2,1,10,44,1,5,1,6),_FrPVCConnectAdminStatus_Type())
frPVCConnectAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCConnectAdminStatus.setStatus(_B)
class _FrPVCConnectL2hOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_h,3),('unknown',4)))
_FrPVCConnectL2hOperStatus_Type.__name__=_D
_FrPVCConnectL2hOperStatus_Object=MibTableColumn
frPVCConnectL2hOperStatus=_FrPVCConnectL2hOperStatus_Object((1,3,6,1,2,1,10,44,1,5,1,7),_FrPVCConnectL2hOperStatus_Type())
frPVCConnectL2hOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCConnectL2hOperStatus.setStatus(_B)
class _FrPVCConnectH2lOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_h,3),('unknown',4)))
_FrPVCConnectH2lOperStatus_Type.__name__=_D
_FrPVCConnectH2lOperStatus_Object=MibTableColumn
frPVCConnectH2lOperStatus=_FrPVCConnectH2lOperStatus_Object((1,3,6,1,2,1,10,44,1,5,1,8),_FrPVCConnectH2lOperStatus_Type())
frPVCConnectH2lOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCConnectH2lOperStatus.setStatus(_B)
_FrPVCConnectL2hLastChange_Type=TimeStamp
_FrPVCConnectL2hLastChange_Object=MibTableColumn
frPVCConnectL2hLastChange=_FrPVCConnectL2hLastChange_Object((1,3,6,1,2,1,10,44,1,5,1,9),_FrPVCConnectL2hLastChange_Type())
frPVCConnectL2hLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCConnectL2hLastChange.setStatus(_B)
_FrPVCConnectH2lLastChange_Type=TimeStamp
_FrPVCConnectH2lLastChange_Object=MibTableColumn
frPVCConnectH2lLastChange=_FrPVCConnectH2lLastChange_Object((1,3,6,1,2,1,10,44,1,5,1,10),_FrPVCConnectH2lLastChange_Type())
frPVCConnectH2lLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:frPVCConnectH2lLastChange.setStatus(_B)
_FrPVCConnectRowStatus_Type=RowStatus
_FrPVCConnectRowStatus_Object=MibTableColumn
frPVCConnectRowStatus=_FrPVCConnectRowStatus_Object((1,3,6,1,2,1,10,44,1,5,1,11),_FrPVCConnectRowStatus_Type())
frPVCConnectRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCConnectRowStatus.setStatus(_B)
_FrPVCConnectUserName_Type=SnmpAdminString
_FrPVCConnectUserName_Object=MibTableColumn
frPVCConnectUserName=_FrPVCConnectUserName_Object((1,3,6,1,2,1,10,44,1,5,1,12),_FrPVCConnectUserName_Type())
frPVCConnectUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCConnectUserName.setStatus(_B)
_FrPVCConnectProviderName_Type=SnmpAdminString
_FrPVCConnectProviderName_Object=MibTableColumn
frPVCConnectProviderName=_FrPVCConnectProviderName_Object((1,3,6,1,2,1,10,44,1,5,1,13),_FrPVCConnectProviderName_Type())
frPVCConnectProviderName.setMaxAccess(_G)
if mibBuilder.loadTexts:frPVCConnectProviderName.setStatus(_B)
_FrAccountPVCTable_Object=MibTable
frAccountPVCTable=_FrAccountPVCTable_Object((1,3,6,1,2,1,10,44,1,6))
if mibBuilder.loadTexts:frAccountPVCTable.setStatus(_B)
_FrAccountPVCEntry_Object=MibTableRow
frAccountPVCEntry=_FrAccountPVCEntry_Object((1,3,6,1,2,1,10,44,1,6,1))
frAccountPVCEntry.setIndexNames((0,_K,_L),(0,_A,_A0))
if mibBuilder.loadTexts:frAccountPVCEntry.setStatus(_B)
class _FrAccountPVCDLCIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4194303))
_FrAccountPVCDLCIIndex_Type.__name__=_D
_FrAccountPVCDLCIIndex_Object=MibTableColumn
frAccountPVCDLCIIndex=_FrAccountPVCDLCIIndex_Object((1,3,6,1,2,1,10,44,1,6,1,1),_FrAccountPVCDLCIIndex_Type())
frAccountPVCDLCIIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:frAccountPVCDLCIIndex.setStatus(_B)
_FrAccountPVCSegmentSize_Type=Integer32
_FrAccountPVCSegmentSize_Object=MibTableColumn
frAccountPVCSegmentSize=_FrAccountPVCSegmentSize_Object((1,3,6,1,2,1,10,44,1,6,1,2),_FrAccountPVCSegmentSize_Type())
frAccountPVCSegmentSize.setMaxAccess(_C)
if mibBuilder.loadTexts:frAccountPVCSegmentSize.setStatus(_B)
if mibBuilder.loadTexts:frAccountPVCSegmentSize.setUnits(_I)
_FrAccountPVCInSegments_Type=Counter32
_FrAccountPVCInSegments_Object=MibTableColumn
frAccountPVCInSegments=_FrAccountPVCInSegments_Object((1,3,6,1,2,1,10,44,1,6,1,3),_FrAccountPVCInSegments_Type())
frAccountPVCInSegments.setMaxAccess(_C)
if mibBuilder.loadTexts:frAccountPVCInSegments.setStatus(_B)
if mibBuilder.loadTexts:frAccountPVCInSegments.setUnits(_T)
_FrAccountPVCOutSegments_Type=Counter32
_FrAccountPVCOutSegments_Object=MibTableColumn
frAccountPVCOutSegments=_FrAccountPVCOutSegments_Object((1,3,6,1,2,1,10,44,1,6,1,4),_FrAccountPVCOutSegments_Type())
frAccountPVCOutSegments.setMaxAccess(_C)
if mibBuilder.loadTexts:frAccountPVCOutSegments.setStatus(_B)
if mibBuilder.loadTexts:frAccountPVCOutSegments.setUnits(_T)
_FrAccountLportTable_Object=MibTable
frAccountLportTable=_FrAccountLportTable_Object((1,3,6,1,2,1,10,44,1,7))
if mibBuilder.loadTexts:frAccountLportTable.setStatus(_B)
_FrAccountLportEntry_Object=MibTableRow
frAccountLportEntry=_FrAccountLportEntry_Object((1,3,6,1,2,1,10,44,1,7,1))
frAccountLportEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:frAccountLportEntry.setStatus(_B)
_FrAccountLportSegmentSize_Type=Integer32
_FrAccountLportSegmentSize_Object=MibTableColumn
frAccountLportSegmentSize=_FrAccountLportSegmentSize_Object((1,3,6,1,2,1,10,44,1,7,1,1),_FrAccountLportSegmentSize_Type())
frAccountLportSegmentSize.setMaxAccess(_C)
if mibBuilder.loadTexts:frAccountLportSegmentSize.setStatus(_B)
if mibBuilder.loadTexts:frAccountLportSegmentSize.setUnits(_I)
_FrAccountLportInSegments_Type=Counter32
_FrAccountLportInSegments_Object=MibTableColumn
frAccountLportInSegments=_FrAccountLportInSegments_Object((1,3,6,1,2,1,10,44,1,7,1,2),_FrAccountLportInSegments_Type())
frAccountLportInSegments.setMaxAccess(_C)
if mibBuilder.loadTexts:frAccountLportInSegments.setStatus(_B)
if mibBuilder.loadTexts:frAccountLportInSegments.setUnits(_T)
_FrAccountLportOutSegments_Type=Counter32
_FrAccountLportOutSegments_Object=MibTableColumn
frAccountLportOutSegments=_FrAccountLportOutSegments_Object((1,3,6,1,2,1,10,44,1,7,1,3),_FrAccountLportOutSegments_Type())
frAccountLportOutSegments.setMaxAccess(_C)
if mibBuilder.loadTexts:frAccountLportOutSegments.setStatus(_B)
if mibBuilder.loadTexts:frAccountLportOutSegments.setUnits(_T)
_FrnetservTraps_ObjectIdentity=ObjectIdentity
frnetservTraps=_FrnetservTraps_ObjectIdentity((1,3,6,1,2,1,10,44,2))
_FrnetservTrapsPrefix_ObjectIdentity=ObjectIdentity
frnetservTrapsPrefix=_FrnetservTrapsPrefix_ObjectIdentity((1,3,6,1,2,1,10,44,2,0))
_FrnetservConformance_ObjectIdentity=ObjectIdentity
frnetservConformance=_FrnetservConformance_ObjectIdentity((1,3,6,1,2,1,10,44,3))
_FrnetservGroups_ObjectIdentity=ObjectIdentity
frnetservGroups=_FrnetservGroups_ObjectIdentity((1,3,6,1,2,1,10,44,3,1))
_FrnetservCompliances_ObjectIdentity=ObjectIdentity
frnetservCompliances=_FrnetservCompliances_ObjectIdentity((1,3,6,1,2,1,10,44,3,2))
frnetservLportGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,1))
frnetservLportGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_A1)))
if mibBuilder.loadTexts:frnetservLportGroup.setStatus(_O)
frnetservMgtVCSigGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,2))
frnetservMgtVCSigGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:frnetservMgtVCSigGroup.setStatus(_B)
frnetservPVCEndptGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,3))
frnetservPVCEndptGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_U),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:frnetservPVCEndptGroup.setStatus(_B)
frnetservPVCConnectGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,4))
frnetservPVCConnectGroup.setObjects(*((_A,_Ab),(_A,_V),(_A,_W),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:frnetservPVCConnectGroup.setStatus(_B)
frnetservAccountPVCGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,5))
frnetservAccountPVCGroup.setObjects(*((_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:frnetservAccountPVCGroup.setStatus(_B)
frnetservAccountLportGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,6))
frnetservAccountLportGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:frnetservAccountLportGroup.setStatus(_B)
frnetservLportGroup2=ObjectGroup((1,3,6,1,2,1,10,44,3,1,7))
frnetservLportGroup2.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:frnetservLportGroup2.setStatus(_B)
frnetservPVCEndptGroup2=ObjectGroup((1,3,6,1,2,1,10,44,3,1,8))
frnetservPVCEndptGroup2.setObjects(*((_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:frnetservPVCEndptGroup2.setStatus(_B)
frnetservPVCConnectNamesGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,9))
frnetservPVCConnectNamesGroup.setObjects(*((_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:frnetservPVCConnectNamesGroup.setStatus(_B)
frnetservLportAdminGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,10))
frnetservLportAdminGroup.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1)))
if mibBuilder.loadTexts:frnetservLportAdminGroup.setStatus(_B)
frnetservMgtVCSigAdminGroup=ObjectGroup((1,3,6,1,2,1,10,44,3,1,11))
frnetservMgtVCSigAdminGroup.setObjects(*((_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA)))
if mibBuilder.loadTexts:frnetservMgtVCSigAdminGroup.setStatus(_B)
frPVCConnectStatusNotif=NotificationType((1,3,6,1,2,1,10,44,2,0,2))
frPVCConnectStatusNotif.setObjects(*((_A,_V),(_A,_W),(_A,_U)))
if mibBuilder.loadTexts:frPVCConnectStatusNotif.setStatus(_B)
frPVCConnectStatusChange=NotificationType((1,3,6,1,2,1,10,44,2,1))
frPVCConnectStatusChange.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_V),(_A,_W),(_A,_U)))
if mibBuilder.loadTexts:frPVCConnectStatusChange.setStatus(_O)
frnetservPVCNotifGroup=NotificationGroup((1,3,6,1,2,1,10,44,3,1,12))
frnetservPVCNotifGroup.setObjects((_A,_BB))
if mibBuilder.loadTexts:frnetservPVCNotifGroup.setStatus(_O)
frnetservPVCNotifGroup2=NotificationGroup((1,3,6,1,2,1,10,44,3,1,13))
frnetservPVCNotifGroup2.setObjects((_A,_BC))
if mibBuilder.loadTexts:frnetservPVCNotifGroup2.setStatus(_B)
frnetservCompliance=ModuleCompliance((1,3,6,1,2,1,10,44,3,2,1))
frnetservCompliance.setObjects(*((_A,_BD),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:frnetservCompliance.setStatus(_O)
frnetservCompliance2=ModuleCompliance((1,3,6,1,2,1,10,44,3,2,2))
frnetservCompliance2.setObjects(*((_A,_o),(_A,_X),(_A,_Y),(_A,_p),(_A,_Z),(_A,_q),(_A,_r),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:frnetservCompliance2.setStatus(_B)
frnetSwitchCompliance=ModuleCompliance((1,3,6,1,2,1,10,44,3,2,3))
frnetSwitchCompliance.setObjects(*((_A,_o),(_A,_BE),(_A,_X),(_A,_BF),(_A,_Y),(_A,_p),(_A,_Z),(_A,_q),(_A,_r),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:frnetSwitchCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'frnetservMIB':frnetservMIB,'frnetservObjects':frnetservObjects,'frLportTable':frLportTable,'frLportEntry':frLportEntry,_i:frLportNumPlan,_j:frLportContact,_k:frLportLocation,_l:frLportType,_m:frLportAddrDLCILen,_n:frLportVCSigProtocol,_A1:frLportVCSigPointer,_A_:frLportDLCIIndexValue,_B0:frLportTypeAdmin,_B1:frLportVCSigProtocolAdmin,_Al:frLportFragControl,_Am:frLportFragSize,'frMgtVCSigTable':frMgtVCSigTable,'frMgtVCSigEntry':frMgtVCSigEntry,_A2:frMgtVCSigProced,_A3:frMgtVCSigUserN391,_A4:frMgtVCSigUserN392,_A5:frMgtVCSigUserN393,_A6:frMgtVCSigUserT391,_A7:frMgtVCSigNetN392,_A8:frMgtVCSigNetN393,_A9:frMgtVCSigNetT392,_AA:frMgtVCSigNetnN4,_AB:frMgtVCSigNetnT3,_AC:frMgtVCSigUserLinkRelErrors,_AD:frMgtVCSigUserProtErrors,_AE:frMgtVCSigUserChanInactive,_AF:frMgtVCSigNetLinkRelErrors,_AG:frMgtVCSigNetProtErrors,_AH:frMgtVCSigNetChanInactive,_B2:frMgtVCSigProcedAdmin,_B3:frMgtVCSigUserN391Admin,_B4:frMgtVCSigUserN392Admin,_B5:frMgtVCSigUserN393Admin,_B6:frMgtVCSigUserT391Admin,_B7:frMgtVCSigNetN392Admin,_B8:frMgtVCSigNetN393Admin,_B9:frMgtVCSigNetT392Admin,_BA:frMgtVCSigNetnT3Admin,'frPVCEndptTable':frPVCEndptTable,'frPVCEndptEntry':frPVCEndptEntry,_y:frPVCEndptDLCIIndex,_AJ:frPVCEndptInMaxFrameSize,_AK:frPVCEndptInBc,_AL:frPVCEndptInBe,_AM:frPVCEndptInCIR,_AN:frPVCEndptOutMaxFrameSize,_AO:frPVCEndptOutBc,_AP:frPVCEndptOutBe,_AQ:frPVCEndptOutCIR,_AR:frPVCEndptConnectIdentifier,_AS:frPVCEndptRowStatus,_U:frPVCEndptRcvdSigStatus,_AT:frPVCEndptInFrames,_AU:frPVCEndptOutFrames,_AV:frPVCEndptInDEFrames,_AW:frPVCEndptInExcessFrames,_AX:frPVCEndptOutExcessFrames,_AY:frPVCEndptInDiscards,_AZ:frPVCEndptInOctets,_Aa:frPVCEndptOutOctets,_An:frPVCEndptInDiscardsDESet,_Ao:frPVCEndptInFramesFECNSet,_Ap:frPVCEndptOutFramesFECNSet,_Aq:frPVCEndptInFramesBECNSet,_Ar:frPVCEndptOutFramesBECNSet,_As:frPVCEndptInCongDiscards,_At:frPVCEndptInDECongDiscards,_Au:frPVCEndptOutCongDiscards,_Av:frPVCEndptOutDECongDiscards,_Aw:frPVCEndptOutDEFrames,_Ax:frPVCEndptAtmIwfConnIndex,_AI:frPVCConnectIndexValue,'frPVCConnectTable':frPVCConnectTable,'frPVCConnectEntry':frPVCConnectEntry,_c:frPVCConnectIndex,_d:frPVCConnectLowIfIndex,_e:frPVCConnectLowDLCIIndex,_f:frPVCConnectHighIfIndex,_g:frPVCConnectHighDLCIIndex,_Ab:frPVCConnectAdminStatus,_V:frPVCConnectL2hOperStatus,_W:frPVCConnectH2lOperStatus,_Ac:frPVCConnectL2hLastChange,_Ad:frPVCConnectH2lLastChange,_Ae:frPVCConnectRowStatus,_Ay:frPVCConnectUserName,_Az:frPVCConnectProviderName,'frAccountPVCTable':frAccountPVCTable,'frAccountPVCEntry':frAccountPVCEntry,_A0:frAccountPVCDLCIIndex,_Af:frAccountPVCSegmentSize,_Ag:frAccountPVCInSegments,_Ah:frAccountPVCOutSegments,'frAccountLportTable':frAccountLportTable,'frAccountLportEntry':frAccountLportEntry,_Ai:frAccountLportSegmentSize,_Aj:frAccountLportInSegments,_Ak:frAccountLportOutSegments,'frnetservTraps':frnetservTraps,'frnetservTrapsPrefix':frnetservTrapsPrefix,_BC:frPVCConnectStatusNotif,_BB:frPVCConnectStatusChange,'frnetservConformance':frnetservConformance,'frnetservGroups':frnetservGroups,_BD:frnetservLportGroup,_X:frnetservMgtVCSigGroup,_Y:frnetservPVCEndptGroup,_Z:frnetservPVCConnectGroup,_a:frnetservAccountPVCGroup,_b:frnetservAccountLportGroup,_o:frnetservLportGroup2,_p:frnetservPVCEndptGroup2,_q:frnetservPVCConnectNamesGroup,_BE:frnetservLportAdminGroup,_BF:frnetservMgtVCSigAdminGroup,'frnetservPVCNotifGroup':frnetservPVCNotifGroup,_r:frnetservPVCNotifGroup2,'frnetservCompliances':frnetservCompliances,'frnetservCompliance':frnetservCompliance,'frnetservCompliance2':frnetservCompliance2,'frnetSwitchCompliance':frnetSwitchCompliance})