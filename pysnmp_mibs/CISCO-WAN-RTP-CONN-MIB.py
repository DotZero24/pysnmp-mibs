_m='vismRtpBearerStatsGroupSup1'
_l='vismRtpLatency'
_k='vismRtpInterArrivalJitter'
_j='vismRtpCntsCleared'
_i='vismRtpPktsLost'
_h='vismRtpOctsRcv'
_g='vismRtpOctsSent'
_f='vismRtpPktsRcv'
_e='vismRtpPktsSent'
_d='vismRtpPayloadType'
_c='vismRtpFailReason'
_b='vismRtpLcn'
_a='vismRtpRowStatus'
_Z='vismRtpConnAlarmState'
_Y='vismRtpICSEnable'
_X='vismRtpVad'
_W='vismRtpCasTransport'
_V='vismRtpDtmfTransport'
_U='vismRtpTriRedundancy'
_T='vismRtpEcanEnable'
_S='vismRtpVadTimer'
_R='vismRtpPktPeriod'
_Q='vismRtpCodecType'
_P='vismRtpBearerTos'
_O='vismRtpConnMode'
_N='vismRtpRmtPort'
_M='vismRtpRmtIp'
_L='vismRtpLocPort'
_K='vismRtpEndptNum'
_J='milliseconds'
_I='vismRtpBearerStatsGroup'
_H='vismRtpConnGroup'
_G='vismRtpConnNum'
_F='TruthValue'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='CISCO-WAN-RTP-CONN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
ciscoWanRtpConnMIB=ModuleIdentity((1,3,6,1,4,1,351,150,20))
if mibBuilder.loadTexts:ciscoWanRtpConnMIB.setRevisions(('2005-04-12 00:00','2003-10-20 00:00','2003-05-23 00:00','2002-05-20 00:00','2001-11-28 00:00','2001-03-15 15:00'))
_CiscoWanRtpConnMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanRtpConnMIBObjects=_CiscoWanRtpConnMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,20,1))
_VismRtpConnGrp_ObjectIdentity=ObjectIdentity
vismRtpConnGrp=_VismRtpConnGrp_ObjectIdentity((1,3,6,1,4,1,351,150,20,1,1))
_VismRtpConnGrpTable_Object=MibTable
vismRtpConnGrpTable=_VismRtpConnGrpTable_Object((1,3,6,1,4,1,351,150,20,1,1,1))
if mibBuilder.loadTexts:vismRtpConnGrpTable.setStatus(_A)
_VismRtpConnGrpEntry_Object=MibTableRow
vismRtpConnGrpEntry=_VismRtpConnGrpEntry_Object((1,3,6,1,4,1,351,150,20,1,1,1,1))
vismRtpConnGrpEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vismRtpConnGrpEntry.setStatus(_A)
class _VismRtpConnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,248))
_VismRtpConnNum_Type.__name__=_D
_VismRtpConnNum_Object=MibTableColumn
vismRtpConnNum=_VismRtpConnNum_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,1),_VismRtpConnNum_Type())
vismRtpConnNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vismRtpConnNum.setStatus(_A)
class _VismRtpEndptNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,248))
_VismRtpEndptNum_Type.__name__=_D
_VismRtpEndptNum_Object=MibTableColumn
vismRtpEndptNum=_VismRtpEndptNum_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,2),_VismRtpEndptNum_Type())
vismRtpEndptNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpEndptNum.setStatus(_A)
class _VismRtpLocPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(49648,50142))
_VismRtpLocPort_Type.__name__=_D
_VismRtpLocPort_Object=MibTableColumn
vismRtpLocPort=_VismRtpLocPort_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,3),_VismRtpLocPort_Type())
vismRtpLocPort.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpLocPort.setStatus(_A)
_VismRtpRmtIp_Type=IpAddress
_VismRtpRmtIp_Object=MibTableColumn
vismRtpRmtIp=_VismRtpRmtIp_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,4),_VismRtpRmtIp_Type())
vismRtpRmtIp.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpRmtIp.setStatus(_A)
class _VismRtpRmtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16384,50142))
_VismRtpRmtPort_Type.__name__=_D
_VismRtpRmtPort_Object=MibTableColumn
vismRtpRmtPort=_VismRtpRmtPort_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,5),_VismRtpRmtPort_Type())
vismRtpRmtPort.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpRmtPort.setStatus(_A)
class _VismRtpConnMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sendOnly',1),('rcvOnly',2),('sendAndRcv',3),('inactive',4)))
_VismRtpConnMode_Type.__name__=_D
_VismRtpConnMode_Object=MibTableColumn
vismRtpConnMode=_VismRtpConnMode_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,6),_VismRtpConnMode_Type())
vismRtpConnMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpConnMode.setStatus(_A)
class _VismRtpBearerTos_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismRtpBearerTos_Type.__name__=_D
_VismRtpBearerTos_Object=MibTableColumn
vismRtpBearerTos=_VismRtpBearerTos_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,7),_VismRtpBearerTos_Type())
vismRtpBearerTos.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpBearerTos.setStatus(_A)
class _VismRtpCodecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,11,12,13,14,15)));namedValues=NamedValues(*(('g711u',1),('g711a',2),('g726r32000',3),('g729a',4),('g729ab',5),('clearChannel',6),('g726r16000',7),('g726r24000',8),('g726r40000',9),('g723h',11),('g723ah',12),('g723l',13),('g723al',14),('lossless',15)))
_VismRtpCodecType_Type.__name__=_D
_VismRtpCodecType_Object=MibTableColumn
vismRtpCodecType=_VismRtpCodecType_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,8),_VismRtpCodecType_Type())
vismRtpCodecType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpCodecType.setStatus(_A)
class _VismRtpPktPeriod_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30,40,60)));namedValues=NamedValues(*(('tenms',10),('twentyms',20),('thirtyms',30),('fourtyms',40),('sixtyms',60)))
_VismRtpPktPeriod_Type.__name__=_D
_VismRtpPktPeriod_Object=MibTableColumn
vismRtpPktPeriod=_VismRtpPktPeriod_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,9),_VismRtpPktPeriod_Type())
vismRtpPktPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpPktPeriod.setStatus(_A)
class _VismRtpVadTimer_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,65535))
_VismRtpVadTimer_Type.__name__=_D
_VismRtpVadTimer_Object=MibTableColumn
vismRtpVadTimer=_VismRtpVadTimer_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,10),_VismRtpVadTimer_Type())
vismRtpVadTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpVadTimer.setStatus(_A)
class _VismRtpEcanEnable_Type(TruthValue):defaultValue=1
_VismRtpEcanEnable_Type.__name__=_F
_VismRtpEcanEnable_Object=MibTableColumn
vismRtpEcanEnable=_VismRtpEcanEnable_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,11),_VismRtpEcanEnable_Type())
vismRtpEcanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpEcanEnable.setStatus(_A)
_VismRtpTriRedundancy_Type=TruthValue
_VismRtpTriRedundancy_Object=MibTableColumn
vismRtpTriRedundancy=_VismRtpTriRedundancy_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,12),_VismRtpTriRedundancy_Type())
vismRtpTriRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpTriRedundancy.setStatus(_A)
class _VismRtpDtmfTransport_Type(TruthValue):defaultValue=1
_VismRtpDtmfTransport_Type.__name__=_F
_VismRtpDtmfTransport_Object=MibTableColumn
vismRtpDtmfTransport=_VismRtpDtmfTransport_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,13),_VismRtpDtmfTransport_Type())
vismRtpDtmfTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpDtmfTransport.setStatus(_A)
_VismRtpCasTransport_Type=TruthValue
_VismRtpCasTransport_Object=MibTableColumn
vismRtpCasTransport=_VismRtpCasTransport_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,14),_VismRtpCasTransport_Type())
vismRtpCasTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpCasTransport.setStatus(_A)
class _VismRtpVad_Type(TruthValue):defaultValue=2
_VismRtpVad_Type.__name__=_F
_VismRtpVad_Object=MibTableColumn
vismRtpVad=_VismRtpVad_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,15),_VismRtpVad_Type())
vismRtpVad.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpVad.setStatus(_A)
class _VismRtpICSEnable_Type(TruthValue):defaultValue=2
_VismRtpICSEnable_Type.__name__=_F
_VismRtpICSEnable_Object=MibTableColumn
vismRtpICSEnable=_VismRtpICSEnable_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,16),_VismRtpICSEnable_Type())
vismRtpICSEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpICSEnable.setStatus(_A)
class _VismRtpConnAlarmState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('failed',2)))
_VismRtpConnAlarmState_Type.__name__=_D
_VismRtpConnAlarmState_Object=MibTableColumn
vismRtpConnAlarmState=_VismRtpConnAlarmState_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,17),_VismRtpConnAlarmState_Type())
vismRtpConnAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpConnAlarmState.setStatus(_A)
_VismRtpRowStatus_Type=RowStatus
_VismRtpRowStatus_Object=MibTableColumn
vismRtpRowStatus=_VismRtpRowStatus_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,18),_VismRtpRowStatus_Type())
vismRtpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpRowStatus.setStatus(_A)
class _VismRtpLcn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismRtpLcn_Type.__name__=_D
_VismRtpLcn_Object=MibTableColumn
vismRtpLcn=_VismRtpLcn_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,19),_VismRtpLcn_Type())
vismRtpLcn.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpLcn.setStatus(_A)
class _VismRtpFailReason_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('self',1),('highLevel',2),('both',3),('notFail',4)))
_VismRtpFailReason_Type.__name__=_D
_VismRtpFailReason_Object=MibTableColumn
vismRtpFailReason=_VismRtpFailReason_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,20),_VismRtpFailReason_Type())
vismRtpFailReason.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpFailReason.setStatus(_A)
class _VismRtpPayloadType_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_VismRtpPayloadType_Type.__name__=_D
_VismRtpPayloadType_Object=MibTableColumn
vismRtpPayloadType=_VismRtpPayloadType_Object((1,3,6,1,4,1,351,150,20,1,1,1,1,21),_VismRtpPayloadType_Type())
vismRtpPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpPayloadType.setStatus(_A)
_VismRtpBearerStatsGrp_ObjectIdentity=ObjectIdentity
vismRtpBearerStatsGrp=_VismRtpBearerStatsGrp_ObjectIdentity((1,3,6,1,4,1,351,150,20,1,2))
_VismRtpBearerStatsTable_Object=MibTable
vismRtpBearerStatsTable=_VismRtpBearerStatsTable_Object((1,3,6,1,4,1,351,150,20,1,2,1))
if mibBuilder.loadTexts:vismRtpBearerStatsTable.setStatus(_A)
_VismRtpBearerStatsEntry_Object=MibTableRow
vismRtpBearerStatsEntry=_VismRtpBearerStatsEntry_Object((1,3,6,1,4,1,351,150,20,1,2,1,1))
vismRtpBearerStatsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vismRtpBearerStatsEntry.setStatus(_A)
_VismRtpPktsSent_Type=Counter32
_VismRtpPktsSent_Object=MibTableColumn
vismRtpPktsSent=_VismRtpPktsSent_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,1),_VismRtpPktsSent_Type())
vismRtpPktsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpPktsSent.setStatus(_A)
_VismRtpPktsRcv_Type=Counter32
_VismRtpPktsRcv_Object=MibTableColumn
vismRtpPktsRcv=_VismRtpPktsRcv_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,2),_VismRtpPktsRcv_Type())
vismRtpPktsRcv.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpPktsRcv.setStatus(_A)
_VismRtpOctsSent_Type=Counter32
_VismRtpOctsSent_Object=MibTableColumn
vismRtpOctsSent=_VismRtpOctsSent_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,3),_VismRtpOctsSent_Type())
vismRtpOctsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpOctsSent.setStatus(_A)
_VismRtpOctsRcv_Type=Counter32
_VismRtpOctsRcv_Object=MibTableColumn
vismRtpOctsRcv=_VismRtpOctsRcv_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,4),_VismRtpOctsRcv_Type())
vismRtpOctsRcv.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpOctsRcv.setStatus(_A)
_VismRtpPktsLost_Type=Counter32
_VismRtpPktsLost_Object=MibTableColumn
vismRtpPktsLost=_VismRtpPktsLost_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,5),_VismRtpPktsLost_Type())
vismRtpPktsLost.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpPktsLost.setStatus(_A)
_VismRtpCntsCleared_Type=TruthValue
_VismRtpCntsCleared_Object=MibTableColumn
vismRtpCntsCleared=_VismRtpCntsCleared_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,6),_VismRtpCntsCleared_Type())
vismRtpCntsCleared.setMaxAccess('read-write')
if mibBuilder.loadTexts:vismRtpCntsCleared.setStatus(_A)
_VismRtpInterArrivalJitter_Type=Unsigned32
_VismRtpInterArrivalJitter_Object=MibTableColumn
vismRtpInterArrivalJitter=_VismRtpInterArrivalJitter_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,7),_VismRtpInterArrivalJitter_Type())
vismRtpInterArrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpInterArrivalJitter.setStatus(_A)
if mibBuilder.loadTexts:vismRtpInterArrivalJitter.setUnits(_J)
_VismRtpLatency_Type=Unsigned32
_VismRtpLatency_Object=MibTableColumn
vismRtpLatency=_VismRtpLatency_Object((1,3,6,1,4,1,351,150,20,1,2,1,1,8),_VismRtpLatency_Type())
vismRtpLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRtpLatency.setStatus(_A)
if mibBuilder.loadTexts:vismRtpLatency.setUnits(_J)
_VismRtpConnNotificationPrefix_ObjectIdentity=ObjectIdentity
vismRtpConnNotificationPrefix=_VismRtpConnNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,351,150,20,2))
_VismRtpConnNotifications_ObjectIdentity=ObjectIdentity
vismRtpConnNotifications=_VismRtpConnNotifications_ObjectIdentity((1,3,6,1,4,1,351,150,20,2,0))
_VismRtpConnMIBConformance_ObjectIdentity=ObjectIdentity
vismRtpConnMIBConformance=_VismRtpConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,20,3))
_VismRtpConnMIBCompliances_ObjectIdentity=ObjectIdentity
vismRtpConnMIBCompliances=_VismRtpConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,20,3,1))
_VismRtpConnMIBGroups_ObjectIdentity=ObjectIdentity
vismRtpConnMIBGroups=_VismRtpConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,20,3,2))
vismRtpConnGroup=ObjectGroup((1,3,6,1,4,1,351,150,20,3,2,1))
vismRtpConnGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:vismRtpConnGroup.setStatus(_A)
vismRtpBearerStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,20,3,2,2))
vismRtpBearerStatsGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:vismRtpBearerStatsGroup.setStatus(_A)
vismRtpBearerStatsGroupSup1=ObjectGroup((1,3,6,1,4,1,351,150,20,3,2,3))
vismRtpBearerStatsGroupSup1.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:vismRtpBearerStatsGroupSup1.setStatus(_A)
vismRtpConnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,20,3,1,1))
vismRtpConnMIBCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:vismRtpConnMIBCompliance.setStatus('deprecated')
vismRtpConnMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,351,150,20,3,1,2))
vismRtpConnMIBComplianceRev1.setObjects(*((_B,_H),(_B,_I),(_B,_m)))
if mibBuilder.loadTexts:vismRtpConnMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWanRtpConnMIB':ciscoWanRtpConnMIB,'ciscoWanRtpConnMIBObjects':ciscoWanRtpConnMIBObjects,'vismRtpConnGrp':vismRtpConnGrp,'vismRtpConnGrpTable':vismRtpConnGrpTable,'vismRtpConnGrpEntry':vismRtpConnGrpEntry,_G:vismRtpConnNum,_K:vismRtpEndptNum,_L:vismRtpLocPort,_M:vismRtpRmtIp,_N:vismRtpRmtPort,_O:vismRtpConnMode,_P:vismRtpBearerTos,_Q:vismRtpCodecType,_R:vismRtpPktPeriod,_S:vismRtpVadTimer,_T:vismRtpEcanEnable,_U:vismRtpTriRedundancy,_V:vismRtpDtmfTransport,_W:vismRtpCasTransport,_X:vismRtpVad,_Y:vismRtpICSEnable,_Z:vismRtpConnAlarmState,_a:vismRtpRowStatus,_b:vismRtpLcn,_c:vismRtpFailReason,_d:vismRtpPayloadType,'vismRtpBearerStatsGrp':vismRtpBearerStatsGrp,'vismRtpBearerStatsTable':vismRtpBearerStatsTable,'vismRtpBearerStatsEntry':vismRtpBearerStatsEntry,_e:vismRtpPktsSent,_f:vismRtpPktsRcv,_g:vismRtpOctsSent,_h:vismRtpOctsRcv,_i:vismRtpPktsLost,_j:vismRtpCntsCleared,_k:vismRtpInterArrivalJitter,_l:vismRtpLatency,'vismRtpConnNotificationPrefix':vismRtpConnNotificationPrefix,'vismRtpConnNotifications':vismRtpConnNotifications,'vismRtpConnMIBConformance':vismRtpConnMIBConformance,'vismRtpConnMIBCompliances':vismRtpConnMIBCompliances,'vismRtpConnMIBCompliance':vismRtpConnMIBCompliance,'vismRtpConnMIBComplianceRev1':vismRtpConnMIBComplianceRev1,'vismRtpConnMIBGroups':vismRtpConnMIBGroups,_H:vismRtpConnGroup,_I:vismRtpBearerStatsGroup,_m:vismRtpBearerStatsGroupSup1})