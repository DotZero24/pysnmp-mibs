_A4='ciscoVismBearerConnGroupRev1'
_A3='ciscoVismAAl2CidGroup'
_A2='bearerCurrentExtRAIXmtCnts'
_A1='bearerCurrentExtAISXmtCnts'
_A0='bearerCurrentConnRDICnts'
_z='bearerCurrentConnAISCnts'
_y='bearerCurrentExtRAIRcvCnts'
_x='bearerCurrentExtAISRcvCnts'
_w='bearerCurrentRcvCellRate'
_v='bearerPeakRcvCellRate'
_u='bearerCurrentXmtCellRate'
_t='bearerPeakXmtCellRate'
_s='vismAal2CidAdminState'
_r='ciscoVismAAl2CidGroupRev1'
_q='ciscoVismBearerConnGroup'
_p='vismAal2CidFailReason'
_o='vismAal2CidState'
_n='vismAal2CidICSEnable'
_m='vismAal2CnfPktPeriod'
_l='vismAal2InitVadTimer'
_k='vismAal2CidEcanEnable'
_j='vismAal2CidCasTransport'
_i='vismAal2CidDtmfTransport'
_h='vismAal2CidCodecType'
_g='vismAal2CidProfileNum'
_f='vismAal2CidProfileType'
_e='vismAal2CidVad'
_d='vismAal2CidType3Redundancy'
_c='vismAal2CidRowStatus'
_b='vismAal2EndptNum'
_a='bearerCntClrButton'
_Z='bearerAal2ConnRDICnts'
_Y='bearerAal2ConnAISCnts'
_X='bearerAal2ExtRAICnts'
_W='bearerAal2ExtAISCnts'
_V='bearerLatency'
_U='bearerJitter'
_T='bearerLostPkts'
_S='bearerRcvdOctets'
_R='bearerSentOctets'
_Q='bearerRcvdPkts'
_P='bearerSentPkts'
_O='bearerLcn'
_N='bearerCid'
_M='milliseconds'
_L='deprecated'
_K='cells-per-second'
_J='bearerEndptNum'
_I='vismAal2CidNum'
_H='vismAal2CidLcn'
_G='TruthValue'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-VISM-ATM-TRUNK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vismChanGrp,voice=mibBuilder.importSymbols('BASIS-MIB','vismChanGrp','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
ciscoVismAtmTrunkMIB=ModuleIdentity((1,3,6,1,4,1,351,150,87))
if mibBuilder.loadTexts:ciscoVismAtmTrunkMIB.setRevisions(('2004-04-14 00:00','2004-02-05 00:00','2003-12-09 00:00'))
_VismAal2CidGrp_ObjectIdentity=ObjectIdentity
vismAal2CidGrp=_VismAal2CidGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,3,4))
_VismAal2CidCnfTable_Object=MibTable
vismAal2CidCnfTable=_VismAal2CidCnfTable_Object((1,3,6,1,4,1,351,110,5,5,3,4,1))
if mibBuilder.loadTexts:vismAal2CidCnfTable.setStatus(_B)
_VismAal2CidEntry_Object=MibTableRow
vismAal2CidEntry=_VismAal2CidEntry_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1))
vismAal2CidEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:vismAal2CidEntry.setStatus(_B)
class _VismAal2CidNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,255))
_VismAal2CidNum_Type.__name__=_D
_VismAal2CidNum_Object=MibTableColumn
vismAal2CidNum=_VismAal2CidNum_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,1),_VismAal2CidNum_Type())
vismAal2CidNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2CidNum.setStatus(_B)
class _VismAal2CidLcn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismAal2CidLcn_Type.__name__=_D
_VismAal2CidLcn_Object=MibTableColumn
vismAal2CidLcn=_VismAal2CidLcn_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,2),_VismAal2CidLcn_Type())
vismAal2CidLcn.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2CidLcn.setStatus(_B)
class _VismAal2EndptNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismAal2EndptNum_Type.__name__=_D
_VismAal2EndptNum_Object=MibTableColumn
vismAal2EndptNum=_VismAal2EndptNum_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,3),_VismAal2EndptNum_Type())
vismAal2EndptNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2EndptNum.setStatus(_B)
class _VismAal2CidRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*(('active',1),('createAndGo',4),('destroy',6)))
_VismAal2CidRowStatus_Type.__name__=_D
_VismAal2CidRowStatus_Object=MibTableColumn
vismAal2CidRowStatus=_VismAal2CidRowStatus_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,4),_VismAal2CidRowStatus_Type())
vismAal2CidRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidRowStatus.setStatus(_B)
_VismAal2CidType3Redundancy_Type=TruthValue
_VismAal2CidType3Redundancy_Object=MibTableColumn
vismAal2CidType3Redundancy=_VismAal2CidType3Redundancy_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,5),_VismAal2CidType3Redundancy_Type())
vismAal2CidType3Redundancy.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidType3Redundancy.setStatus(_B)
class _VismAal2CidVad_Type(TruthValue):defaultValue=2
_VismAal2CidVad_Type.__name__=_G
_VismAal2CidVad_Object=MibTableColumn
vismAal2CidVad=_VismAal2CidVad_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,6),_VismAal2CidVad_Type())
vismAal2CidVad.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidVad.setStatus(_B)
class _VismAal2CidProfileType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('itu',1),('atm',2),('custom',3),('none',4)))
_VismAal2CidProfileType_Type.__name__=_D
_VismAal2CidProfileType_Object=MibTableColumn
vismAal2CidProfileType=_VismAal2CidProfileType_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,7),_VismAal2CidProfileType_Type())
vismAal2CidProfileType.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidProfileType.setStatus(_B)
class _VismAal2CidProfileNum_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismAal2CidProfileNum_Type.__name__=_D
_VismAal2CidProfileNum_Object=MibTableColumn
vismAal2CidProfileNum=_VismAal2CidProfileNum_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,8),_VismAal2CidProfileNum_Type())
vismAal2CidProfileNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidProfileNum.setStatus(_B)
class _VismAal2CidCodecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,11,12,13,14,15)));namedValues=NamedValues(*(('g711u',1),('g711a',2),('g726r32000',3),('g729a',4),('g729ab',5),('clearChannel',6),('g726r16000',7),('g726r24000',8),('g726r40000',9),('g723h',11),('g723ah',12),('g723l',13),('g723al',14),('lossless',15)))
_VismAal2CidCodecType_Type.__name__=_D
_VismAal2CidCodecType_Object=MibTableColumn
vismAal2CidCodecType=_VismAal2CidCodecType_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,9),_VismAal2CidCodecType_Type())
vismAal2CidCodecType.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidCodecType.setStatus(_B)
class _VismAal2CidDtmfTransport_Type(TruthValue):defaultValue=1
_VismAal2CidDtmfTransport_Type.__name__=_G
_VismAal2CidDtmfTransport_Object=MibTableColumn
vismAal2CidDtmfTransport=_VismAal2CidDtmfTransport_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,10),_VismAal2CidDtmfTransport_Type())
vismAal2CidDtmfTransport.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidDtmfTransport.setStatus(_B)
_VismAal2CidCasTransport_Type=TruthValue
_VismAal2CidCasTransport_Object=MibTableColumn
vismAal2CidCasTransport=_VismAal2CidCasTransport_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,11),_VismAal2CidCasTransport_Type())
vismAal2CidCasTransport.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidCasTransport.setStatus(_B)
class _VismAal2CidEcanEnable_Type(TruthValue):defaultValue=1
_VismAal2CidEcanEnable_Type.__name__=_G
_VismAal2CidEcanEnable_Object=MibTableColumn
vismAal2CidEcanEnable=_VismAal2CidEcanEnable_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,12),_VismAal2CidEcanEnable_Type())
vismAal2CidEcanEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidEcanEnable.setStatus(_B)
class _VismAal2InitVadTimer_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,65535))
_VismAal2InitVadTimer_Type.__name__=_D
_VismAal2InitVadTimer_Object=MibTableColumn
vismAal2InitVadTimer=_VismAal2InitVadTimer_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,13),_VismAal2InitVadTimer_Type())
vismAal2InitVadTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2InitVadTimer.setStatus(_B)
if mibBuilder.loadTexts:vismAal2InitVadTimer.setUnits(_M)
class _VismAal2CnfPktPeriod_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,20,30,40)));namedValues=NamedValues(*(('five',5),('ten',10),('twenty',20),('thirty',30),('fourty',40)))
_VismAal2CnfPktPeriod_Type.__name__=_D
_VismAal2CnfPktPeriod_Object=MibTableColumn
vismAal2CnfPktPeriod=_VismAal2CnfPktPeriod_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,14),_VismAal2CnfPktPeriod_Type())
vismAal2CnfPktPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CnfPktPeriod.setStatus(_B)
class _VismAal2CidICSEnable_Type(TruthValue):defaultValue=2
_VismAal2CidICSEnable_Type.__name__=_G
_VismAal2CidICSEnable_Object=MibTableColumn
vismAal2CidICSEnable=_VismAal2CidICSEnable_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,15),_VismAal2CidICSEnable_Type())
vismAal2CidICSEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidICSEnable.setStatus(_B)
class _VismAal2CidState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cidStateActive',1),('cidStateFailed',2)))
_VismAal2CidState_Type.__name__=_D
_VismAal2CidState_Object=MibTableColumn
vismAal2CidState=_VismAal2CidState_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,16),_VismAal2CidState_Type())
vismAal2CidState.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2CidState.setStatus(_B)
class _VismAal2CidFailReason_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('self',1),('highLevel',2),('both',3),('notFail',4)))
_VismAal2CidFailReason_Type.__name__=_D
_VismAal2CidFailReason_Object=MibTableColumn
vismAal2CidFailReason=_VismAal2CidFailReason_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,17),_VismAal2CidFailReason_Type())
vismAal2CidFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2CidFailReason.setStatus(_B)
class _VismAal2CidAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('cidPendingInService',1),('cidInService',2),('cidCommandedOutOfService',3),('cidPendingOutOfService',4),('cidUnknownState',5)))
_VismAal2CidAdminState_Type.__name__=_D
_VismAal2CidAdminState_Object=MibTableColumn
vismAal2CidAdminState=_VismAal2CidAdminState_Object((1,3,6,1,4,1,351,110,5,5,3,4,1,1,18),_VismAal2CidAdminState_Type())
vismAal2CidAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAal2CidAdminState.setStatus(_B)
_BearerConnGrp_ObjectIdentity=ObjectIdentity
bearerConnGrp=_BearerConnGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,9))
_BearerConnTable_Object=MibTable
bearerConnTable=_BearerConnTable_Object((1,3,6,1,4,1,351,110,5,5,9,1))
if mibBuilder.loadTexts:bearerConnTable.setStatus(_B)
_BearerConnEntry_Object=MibTableRow
bearerConnEntry=_BearerConnEntry_Object((1,3,6,1,4,1,351,110,5,5,9,1,1))
bearerConnEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:bearerConnEntry.setStatus(_B)
class _BearerEndptNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BearerEndptNum_Type.__name__=_D
_BearerEndptNum_Object=MibTableColumn
bearerEndptNum=_BearerEndptNum_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,1),_BearerEndptNum_Type())
bearerEndptNum.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerEndptNum.setStatus(_B)
_BearerCid_Type=Integer32
_BearerCid_Object=MibTableColumn
bearerCid=_BearerCid_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,2),_BearerCid_Type())
bearerCid.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCid.setStatus(_B)
class _BearerLcn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_BearerLcn_Type.__name__=_D
_BearerLcn_Object=MibTableColumn
bearerLcn=_BearerLcn_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,3),_BearerLcn_Type())
bearerLcn.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerLcn.setStatus(_B)
_BearerSentPkts_Type=Counter32
_BearerSentPkts_Object=MibTableColumn
bearerSentPkts=_BearerSentPkts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,4),_BearerSentPkts_Type())
bearerSentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerSentPkts.setStatus(_B)
_BearerRcvdPkts_Type=Counter32
_BearerRcvdPkts_Object=MibTableColumn
bearerRcvdPkts=_BearerRcvdPkts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,5),_BearerRcvdPkts_Type())
bearerRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerRcvdPkts.setStatus(_B)
_BearerSentOctets_Type=Counter32
_BearerSentOctets_Object=MibTableColumn
bearerSentOctets=_BearerSentOctets_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,6),_BearerSentOctets_Type())
bearerSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerSentOctets.setStatus(_B)
_BearerRcvdOctets_Type=Counter32
_BearerRcvdOctets_Object=MibTableColumn
bearerRcvdOctets=_BearerRcvdOctets_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,7),_BearerRcvdOctets_Type())
bearerRcvdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerRcvdOctets.setStatus(_B)
_BearerLostPkts_Type=Counter32
_BearerLostPkts_Object=MibTableColumn
bearerLostPkts=_BearerLostPkts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,8),_BearerLostPkts_Type())
bearerLostPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerLostPkts.setStatus(_B)
_BearerJitter_Type=Integer32
_BearerJitter_Object=MibTableColumn
bearerJitter=_BearerJitter_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,9),_BearerJitter_Type())
bearerJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerJitter.setStatus(_B)
if mibBuilder.loadTexts:bearerJitter.setUnits(_M)
_BearerLatency_Type=Integer32
_BearerLatency_Object=MibTableColumn
bearerLatency=_BearerLatency_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,10),_BearerLatency_Type())
bearerLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerLatency.setStatus(_B)
if mibBuilder.loadTexts:bearerLatency.setUnits(_M)
_BearerAal2ExtAISCnts_Type=Counter32
_BearerAal2ExtAISCnts_Object=MibTableColumn
bearerAal2ExtAISCnts=_BearerAal2ExtAISCnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,11),_BearerAal2ExtAISCnts_Type())
bearerAal2ExtAISCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerAal2ExtAISCnts.setStatus(_B)
_BearerAal2ExtRAICnts_Type=Counter32
_BearerAal2ExtRAICnts_Object=MibTableColumn
bearerAal2ExtRAICnts=_BearerAal2ExtRAICnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,12),_BearerAal2ExtRAICnts_Type())
bearerAal2ExtRAICnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerAal2ExtRAICnts.setStatus(_B)
_BearerAal2ConnAISCnts_Type=Counter32
_BearerAal2ConnAISCnts_Object=MibTableColumn
bearerAal2ConnAISCnts=_BearerAal2ConnAISCnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,13),_BearerAal2ConnAISCnts_Type())
bearerAal2ConnAISCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerAal2ConnAISCnts.setStatus(_B)
_BearerAal2ConnRDICnts_Type=Counter32
_BearerAal2ConnRDICnts_Object=MibTableColumn
bearerAal2ConnRDICnts=_BearerAal2ConnRDICnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,14),_BearerAal2ConnRDICnts_Type())
bearerAal2ConnRDICnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerAal2ConnRDICnts.setStatus(_B)
class _BearerCntClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('clear',2)))
_BearerCntClrButton_Type.__name__=_D
_BearerCntClrButton_Object=MibTableColumn
bearerCntClrButton=_BearerCntClrButton_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,15),_BearerCntClrButton_Type())
bearerCntClrButton.setMaxAccess(_E)
if mibBuilder.loadTexts:bearerCntClrButton.setStatus(_B)
class _BearerPeakXmtCellRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BearerPeakXmtCellRate_Type.__name__=_F
_BearerPeakXmtCellRate_Object=MibTableColumn
bearerPeakXmtCellRate=_BearerPeakXmtCellRate_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,16),_BearerPeakXmtCellRate_Type())
bearerPeakXmtCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerPeakXmtCellRate.setStatus(_B)
if mibBuilder.loadTexts:bearerPeakXmtCellRate.setUnits(_K)
class _BearerCurrentXmtCellRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BearerCurrentXmtCellRate_Type.__name__=_F
_BearerCurrentXmtCellRate_Object=MibTableColumn
bearerCurrentXmtCellRate=_BearerCurrentXmtCellRate_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,17),_BearerCurrentXmtCellRate_Type())
bearerCurrentXmtCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentXmtCellRate.setStatus(_B)
if mibBuilder.loadTexts:bearerCurrentXmtCellRate.setUnits(_K)
class _BearerPeakRcvCellRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BearerPeakRcvCellRate_Type.__name__=_F
_BearerPeakRcvCellRate_Object=MibTableColumn
bearerPeakRcvCellRate=_BearerPeakRcvCellRate_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,18),_BearerPeakRcvCellRate_Type())
bearerPeakRcvCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerPeakRcvCellRate.setStatus(_B)
if mibBuilder.loadTexts:bearerPeakRcvCellRate.setUnits(_K)
class _BearerCurrentRcvCellRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BearerCurrentRcvCellRate_Type.__name__=_F
_BearerCurrentRcvCellRate_Object=MibTableColumn
bearerCurrentRcvCellRate=_BearerCurrentRcvCellRate_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,19),_BearerCurrentRcvCellRate_Type())
bearerCurrentRcvCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentRcvCellRate.setStatus(_B)
if mibBuilder.loadTexts:bearerCurrentRcvCellRate.setUnits(_K)
_BearerCurrentExtAISRcvCnts_Type=Counter32
_BearerCurrentExtAISRcvCnts_Object=MibTableColumn
bearerCurrentExtAISRcvCnts=_BearerCurrentExtAISRcvCnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,20),_BearerCurrentExtAISRcvCnts_Type())
bearerCurrentExtAISRcvCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentExtAISRcvCnts.setStatus(_B)
_BearerCurrentExtRAIRcvCnts_Type=Counter32
_BearerCurrentExtRAIRcvCnts_Object=MibTableColumn
bearerCurrentExtRAIRcvCnts=_BearerCurrentExtRAIRcvCnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,21),_BearerCurrentExtRAIRcvCnts_Type())
bearerCurrentExtRAIRcvCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentExtRAIRcvCnts.setStatus(_B)
_BearerCurrentConnAISCnts_Type=Counter32
_BearerCurrentConnAISCnts_Object=MibTableColumn
bearerCurrentConnAISCnts=_BearerCurrentConnAISCnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,22),_BearerCurrentConnAISCnts_Type())
bearerCurrentConnAISCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentConnAISCnts.setStatus(_B)
_BearerCurrentConnRDICnts_Type=Counter32
_BearerCurrentConnRDICnts_Object=MibTableColumn
bearerCurrentConnRDICnts=_BearerCurrentConnRDICnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,23),_BearerCurrentConnRDICnts_Type())
bearerCurrentConnRDICnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentConnRDICnts.setStatus(_B)
_BearerCurrentExtAISXmtCnts_Type=Counter32
_BearerCurrentExtAISXmtCnts_Object=MibTableColumn
bearerCurrentExtAISXmtCnts=_BearerCurrentExtAISXmtCnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,24),_BearerCurrentExtAISXmtCnts_Type())
bearerCurrentExtAISXmtCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentExtAISXmtCnts.setStatus(_B)
_BearerCurrentExtRAIXmtCnts_Type=Counter32
_BearerCurrentExtRAIXmtCnts_Object=MibTableColumn
bearerCurrentExtRAIXmtCnts=_BearerCurrentExtRAIXmtCnts_Object((1,3,6,1,4,1,351,110,5,5,9,1,1,25),_BearerCurrentExtRAIXmtCnts_Type())
bearerCurrentExtRAIXmtCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:bearerCurrentExtRAIXmtCnts.setStatus(_B)
_CvismAtmTrunkMIBConformance_ObjectIdentity=ObjectIdentity
cvismAtmTrunkMIBConformance=_CvismAtmTrunkMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,87,2))
_CvismAtmTrunkMIBGroups_ObjectIdentity=ObjectIdentity
cvismAtmTrunkMIBGroups=_CvismAtmTrunkMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,87,2,1))
_CvismAtmTrunkMIBCompliances_ObjectIdentity=ObjectIdentity
cvismAtmTrunkMIBCompliances=_CvismAtmTrunkMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,87,2,2))
ciscoVismBearerConnGroup=ObjectGroup((1,3,6,1,4,1,351,150,87,2,1,1))
ciscoVismBearerConnGroup.setObjects(*((_A,_J),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoVismBearerConnGroup.setStatus(_L)
ciscoVismAAl2CidGroup=ObjectGroup((1,3,6,1,4,1,351,150,87,2,1,2))
ciscoVismAAl2CidGroup.setObjects(*((_A,_I),(_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ciscoVismAAl2CidGroup.setStatus(_L)
ciscoVismAAl2CidGroupRev1=ObjectGroup((1,3,6,1,4,1,351,150,87,2,1,3))
ciscoVismAAl2CidGroupRev1.setObjects(*((_A,_I),(_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_s)))
if mibBuilder.loadTexts:ciscoVismAAl2CidGroupRev1.setStatus(_B)
ciscoVismBearerConnGroupRev1=ObjectGroup((1,3,6,1,4,1,351,150,87,2,1,4))
ciscoVismBearerConnGroupRev1.setObjects(*((_A,_J),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ciscoVismBearerConnGroupRev1.setStatus(_B)
cvismAtmTrunkCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,87,2,2,1))
cvismAtmTrunkCompliance.setObjects(*((_A,_q),(_A,_A3)))
if mibBuilder.loadTexts:cvismAtmTrunkCompliance.setStatus(_L)
cvismAtmTrunkComplianceRev1=ModuleCompliance((1,3,6,1,4,1,351,150,87,2,2,2))
cvismAtmTrunkComplianceRev1.setObjects(*((_A,_q),(_A,_r)))
if mibBuilder.loadTexts:cvismAtmTrunkComplianceRev1.setStatus(_L)
cvismAtmTrunkComplianceRev2=ModuleCompliance((1,3,6,1,4,1,351,150,87,2,2,3))
cvismAtmTrunkComplianceRev2.setObjects(*((_A,_A4),(_A,_r)))
if mibBuilder.loadTexts:cvismAtmTrunkComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vismAal2CidGrp':vismAal2CidGrp,'vismAal2CidCnfTable':vismAal2CidCnfTable,'vismAal2CidEntry':vismAal2CidEntry,_I:vismAal2CidNum,_H:vismAal2CidLcn,_b:vismAal2EndptNum,_c:vismAal2CidRowStatus,_d:vismAal2CidType3Redundancy,_e:vismAal2CidVad,_f:vismAal2CidProfileType,_g:vismAal2CidProfileNum,_h:vismAal2CidCodecType,_i:vismAal2CidDtmfTransport,_j:vismAal2CidCasTransport,_k:vismAal2CidEcanEnable,_l:vismAal2InitVadTimer,_m:vismAal2CnfPktPeriod,_n:vismAal2CidICSEnable,_o:vismAal2CidState,_p:vismAal2CidFailReason,_s:vismAal2CidAdminState,'bearerConnGrp':bearerConnGrp,'bearerConnTable':bearerConnTable,'bearerConnEntry':bearerConnEntry,_J:bearerEndptNum,_N:bearerCid,_O:bearerLcn,_P:bearerSentPkts,_Q:bearerRcvdPkts,_R:bearerSentOctets,_S:bearerRcvdOctets,_T:bearerLostPkts,_U:bearerJitter,_V:bearerLatency,_W:bearerAal2ExtAISCnts,_X:bearerAal2ExtRAICnts,_Y:bearerAal2ConnAISCnts,_Z:bearerAal2ConnRDICnts,_a:bearerCntClrButton,_t:bearerPeakXmtCellRate,_u:bearerCurrentXmtCellRate,_v:bearerPeakRcvCellRate,_w:bearerCurrentRcvCellRate,_x:bearerCurrentExtAISRcvCnts,_y:bearerCurrentExtRAIRcvCnts,_z:bearerCurrentConnAISCnts,_A0:bearerCurrentConnRDICnts,_A1:bearerCurrentExtAISXmtCnts,_A2:bearerCurrentExtRAIXmtCnts,'ciscoVismAtmTrunkMIB':ciscoVismAtmTrunkMIB,'cvismAtmTrunkMIBConformance':cvismAtmTrunkMIBConformance,'cvismAtmTrunkMIBGroups':cvismAtmTrunkMIBGroups,_q:ciscoVismBearerConnGroup,_A3:ciscoVismAAl2CidGroup,_r:ciscoVismAAl2CidGroupRev1,_A4:ciscoVismBearerConnGroupRev1,'cvismAtmTrunkMIBCompliances':cvismAtmTrunkMIBCompliances,'cvismAtmTrunkCompliance':cvismAtmTrunkCompliance,'cvismAtmTrunkComplianceRev1':cvismAtmTrunkComplianceRev1,'cvismAtmTrunkComplianceRev2':cvismAtmTrunkComplianceRev2})