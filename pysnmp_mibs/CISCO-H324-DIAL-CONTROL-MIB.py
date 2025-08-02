_f='cH324CallActiveGroup'
_e='cH324CallHistoryGroup'
_d='cH324CallActiveRxVideoBytes'
_c='cH324CallActiveRxVideoPackets'
_b='cH324CallActiveRxVideoCodec'
_a='cH324CallActiveTxVideoBytes'
_Z='cH324CallActiveTxVideoPackets'
_Y='cH324CallActiveTxVideoCodec'
_X='cH324CallActiveUsedBandwidth'
_W='cH324CallActiveH324CallType'
_V='cH324CallActiveIncomingConnectionId'
_U='cH324CallActiveConnectionId'
_T='cH324CallHistoryRxVideoBytes'
_S='cH324CallHistoryRxVideoPackets'
_R='cH324CallHistoryRxVideoCodec'
_Q='cH324CallHistoryTxVideoBytes'
_P='cH324CallHistoryTxVideoPackets'
_O='cH324CallHistoryTxVideoCodec'
_N='cH324CallHistoryUsedBandwidth'
_M='cH324CallHistoryH324CallType'
_L='cH324CallHistoryIncomingConnectionId'
_K='cH324CallHistoryConnectionId'
_J='kilobits per second'
_I='callActiveSetupTime'
_H='callActiveIndex'
_G='cCallHistoryIndex'
_F='CISCO-DIAL-CONTROL-MIB'
_E='Unsigned32'
_D='DIAL-CONTROL-MIB'
_C='read-only'
_B='CISCO-H324-DIAL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_F,_G)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CvcGUid,CvcVideoCoderRate=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB','CvcGUid','CvcVideoCoderRate')
AbsoluteCounter32,callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_D,'AbsoluteCounter32',_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoH324DialControlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,621))
if mibBuilder.loadTexts:ciscoH324DialControlMIB.setRevisions(('2007-02-06 00:00',))
class CH324CallType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('h324',1))
_CiscoH324DialControlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoH324DialControlMIBObjects=_CiscoH324DialControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,621,1))
_CH324DialControlCallHistory_ObjectIdentity=ObjectIdentity
cH324DialControlCallHistory=_CH324DialControlCallHistory_ObjectIdentity((1,3,6,1,4,1,9,9,621,1,1))
_CH324CallHistoryTable_Object=MibTable
cH324CallHistoryTable=_CH324CallHistoryTable_Object((1,3,6,1,4,1,9,9,621,1,1,1))
if mibBuilder.loadTexts:cH324CallHistoryTable.setStatus(_A)
_CH324CallHistoryEntry_Object=MibTableRow
cH324CallHistoryEntry=_CH324CallHistoryEntry_Object((1,3,6,1,4,1,9,9,621,1,1,1,1))
cH324CallHistoryEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cH324CallHistoryEntry.setStatus(_A)
_CH324CallHistoryConnectionId_Type=CvcGUid
_CH324CallHistoryConnectionId_Object=MibTableColumn
cH324CallHistoryConnectionId=_CH324CallHistoryConnectionId_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,1),_CH324CallHistoryConnectionId_Type())
cH324CallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryConnectionId.setStatus(_A)
_CH324CallHistoryIncomingConnectionId_Type=CvcGUid
_CH324CallHistoryIncomingConnectionId_Object=MibTableColumn
cH324CallHistoryIncomingConnectionId=_CH324CallHistoryIncomingConnectionId_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,2),_CH324CallHistoryIncomingConnectionId_Type())
cH324CallHistoryIncomingConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryIncomingConnectionId.setStatus(_A)
_CH324CallHistoryH324CallType_Type=CH324CallType
_CH324CallHistoryH324CallType_Object=MibTableColumn
cH324CallHistoryH324CallType=_CH324CallHistoryH324CallType_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,3),_CH324CallHistoryH324CallType_Type())
cH324CallHistoryH324CallType.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryH324CallType.setStatus(_A)
class _CH324CallHistoryUsedBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CH324CallHistoryUsedBandwidth_Type.__name__=_E
_CH324CallHistoryUsedBandwidth_Object=MibTableColumn
cH324CallHistoryUsedBandwidth=_CH324CallHistoryUsedBandwidth_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,4),_CH324CallHistoryUsedBandwidth_Type())
cH324CallHistoryUsedBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryUsedBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cH324CallHistoryUsedBandwidth.setUnits(_J)
_CH324CallHistoryTxVideoCodec_Type=CvcVideoCoderRate
_CH324CallHistoryTxVideoCodec_Object=MibTableColumn
cH324CallHistoryTxVideoCodec=_CH324CallHistoryTxVideoCodec_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,5),_CH324CallHistoryTxVideoCodec_Type())
cH324CallHistoryTxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryTxVideoCodec.setStatus(_A)
_CH324CallHistoryTxVideoPackets_Type=AbsoluteCounter32
_CH324CallHistoryTxVideoPackets_Object=MibTableColumn
cH324CallHistoryTxVideoPackets=_CH324CallHistoryTxVideoPackets_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,6),_CH324CallHistoryTxVideoPackets_Type())
cH324CallHistoryTxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryTxVideoPackets.setStatus(_A)
_CH324CallHistoryTxVideoBytes_Type=AbsoluteCounter32
_CH324CallHistoryTxVideoBytes_Object=MibTableColumn
cH324CallHistoryTxVideoBytes=_CH324CallHistoryTxVideoBytes_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,7),_CH324CallHistoryTxVideoBytes_Type())
cH324CallHistoryTxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryTxVideoBytes.setStatus(_A)
_CH324CallHistoryRxVideoCodec_Type=CvcVideoCoderRate
_CH324CallHistoryRxVideoCodec_Object=MibTableColumn
cH324CallHistoryRxVideoCodec=_CH324CallHistoryRxVideoCodec_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,8),_CH324CallHistoryRxVideoCodec_Type())
cH324CallHistoryRxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryRxVideoCodec.setStatus(_A)
_CH324CallHistoryRxVideoPackets_Type=AbsoluteCounter32
_CH324CallHistoryRxVideoPackets_Object=MibTableColumn
cH324CallHistoryRxVideoPackets=_CH324CallHistoryRxVideoPackets_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,9),_CH324CallHistoryRxVideoPackets_Type())
cH324CallHistoryRxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryRxVideoPackets.setStatus(_A)
_CH324CallHistoryRxVideoBytes_Type=AbsoluteCounter32
_CH324CallHistoryRxVideoBytes_Object=MibTableColumn
cH324CallHistoryRxVideoBytes=_CH324CallHistoryRxVideoBytes_Object((1,3,6,1,4,1,9,9,621,1,1,1,1,10),_CH324CallHistoryRxVideoBytes_Type())
cH324CallHistoryRxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallHistoryRxVideoBytes.setStatus(_A)
_CH324DialControlCallActive_ObjectIdentity=ObjectIdentity
cH324DialControlCallActive=_CH324DialControlCallActive_ObjectIdentity((1,3,6,1,4,1,9,9,621,1,2))
_CH324CallActiveTable_Object=MibTable
cH324CallActiveTable=_CH324CallActiveTable_Object((1,3,6,1,4,1,9,9,621,1,2,1))
if mibBuilder.loadTexts:cH324CallActiveTable.setStatus(_A)
_CH324CallActiveEntry_Object=MibTableRow
cH324CallActiveEntry=_CH324CallActiveEntry_Object((1,3,6,1,4,1,9,9,621,1,2,1,1))
cH324CallActiveEntry.setIndexNames((0,_D,_I),(0,_D,_H))
if mibBuilder.loadTexts:cH324CallActiveEntry.setStatus(_A)
_CH324CallActiveConnectionId_Type=CvcGUid
_CH324CallActiveConnectionId_Object=MibTableColumn
cH324CallActiveConnectionId=_CH324CallActiveConnectionId_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,1),_CH324CallActiveConnectionId_Type())
cH324CallActiveConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveConnectionId.setStatus(_A)
_CH324CallActiveIncomingConnectionId_Type=CvcGUid
_CH324CallActiveIncomingConnectionId_Object=MibTableColumn
cH324CallActiveIncomingConnectionId=_CH324CallActiveIncomingConnectionId_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,2),_CH324CallActiveIncomingConnectionId_Type())
cH324CallActiveIncomingConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveIncomingConnectionId.setStatus(_A)
_CH324CallActiveH324CallType_Type=CH324CallType
_CH324CallActiveH324CallType_Object=MibTableColumn
cH324CallActiveH324CallType=_CH324CallActiveH324CallType_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,3),_CH324CallActiveH324CallType_Type())
cH324CallActiveH324CallType.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveH324CallType.setStatus(_A)
class _CH324CallActiveUsedBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CH324CallActiveUsedBandwidth_Type.__name__=_E
_CH324CallActiveUsedBandwidth_Object=MibTableColumn
cH324CallActiveUsedBandwidth=_CH324CallActiveUsedBandwidth_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,4),_CH324CallActiveUsedBandwidth_Type())
cH324CallActiveUsedBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveUsedBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cH324CallActiveUsedBandwidth.setUnits(_J)
_CH324CallActiveTxVideoCodec_Type=CvcVideoCoderRate
_CH324CallActiveTxVideoCodec_Object=MibTableColumn
cH324CallActiveTxVideoCodec=_CH324CallActiveTxVideoCodec_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,5),_CH324CallActiveTxVideoCodec_Type())
cH324CallActiveTxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveTxVideoCodec.setStatus(_A)
_CH324CallActiveTxVideoPackets_Type=AbsoluteCounter32
_CH324CallActiveTxVideoPackets_Object=MibTableColumn
cH324CallActiveTxVideoPackets=_CH324CallActiveTxVideoPackets_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,6),_CH324CallActiveTxVideoPackets_Type())
cH324CallActiveTxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveTxVideoPackets.setStatus(_A)
_CH324CallActiveTxVideoBytes_Type=AbsoluteCounter32
_CH324CallActiveTxVideoBytes_Object=MibTableColumn
cH324CallActiveTxVideoBytes=_CH324CallActiveTxVideoBytes_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,7),_CH324CallActiveTxVideoBytes_Type())
cH324CallActiveTxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveTxVideoBytes.setStatus(_A)
_CH324CallActiveRxVideoCodec_Type=CvcVideoCoderRate
_CH324CallActiveRxVideoCodec_Object=MibTableColumn
cH324CallActiveRxVideoCodec=_CH324CallActiveRxVideoCodec_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,8),_CH324CallActiveRxVideoCodec_Type())
cH324CallActiveRxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveRxVideoCodec.setStatus(_A)
_CH324CallActiveRxVideoPackets_Type=AbsoluteCounter32
_CH324CallActiveRxVideoPackets_Object=MibTableColumn
cH324CallActiveRxVideoPackets=_CH324CallActiveRxVideoPackets_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,9),_CH324CallActiveRxVideoPackets_Type())
cH324CallActiveRxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveRxVideoPackets.setStatus(_A)
_CH324CallActiveRxVideoBytes_Type=AbsoluteCounter32
_CH324CallActiveRxVideoBytes_Object=MibTableColumn
cH324CallActiveRxVideoBytes=_CH324CallActiveRxVideoBytes_Object((1,3,6,1,4,1,9,9,621,1,2,1,1,10),_CH324CallActiveRxVideoBytes_Type())
cH324CallActiveRxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cH324CallActiveRxVideoBytes.setStatus(_A)
_CiscoH324DialControlMIBConform_ObjectIdentity=ObjectIdentity
ciscoH324DialControlMIBConform=_CiscoH324DialControlMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,621,2))
_CiscoH324DialControlMIBConformance_ObjectIdentity=ObjectIdentity
ciscoH324DialControlMIBConformance=_CiscoH324DialControlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,621,2,1))
_CiscoH324DialControlMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoH324DialControlMIBCompliances=_CiscoH324DialControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,621,2,1,1))
_CiscoH324DialControlMIBGroups_ObjectIdentity=ObjectIdentity
ciscoH324DialControlMIBGroups=_CiscoH324DialControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,621,2,1,2))
cH324CallHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,621,2,1,2,1))
cH324CallHistoryGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cH324CallHistoryGroup.setStatus(_A)
cH324CallActiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,621,2,1,2,2))
cH324CallActiveGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:cH324CallActiveGroup.setStatus(_A)
ciscoH324DialControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,621,2,1,1,1))
ciscoH324DialControlMIBCompliance.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoH324DialControlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CH324CallType':CH324CallType,'ciscoH324DialControlMIB':ciscoH324DialControlMIB,'ciscoH324DialControlMIBObjects':ciscoH324DialControlMIBObjects,'cH324DialControlCallHistory':cH324DialControlCallHistory,'cH324CallHistoryTable':cH324CallHistoryTable,'cH324CallHistoryEntry':cH324CallHistoryEntry,_K:cH324CallHistoryConnectionId,_L:cH324CallHistoryIncomingConnectionId,_M:cH324CallHistoryH324CallType,_N:cH324CallHistoryUsedBandwidth,_O:cH324CallHistoryTxVideoCodec,_P:cH324CallHistoryTxVideoPackets,_Q:cH324CallHistoryTxVideoBytes,_R:cH324CallHistoryRxVideoCodec,_S:cH324CallHistoryRxVideoPackets,_T:cH324CallHistoryRxVideoBytes,'cH324DialControlCallActive':cH324DialControlCallActive,'cH324CallActiveTable':cH324CallActiveTable,'cH324CallActiveEntry':cH324CallActiveEntry,_U:cH324CallActiveConnectionId,_V:cH324CallActiveIncomingConnectionId,_W:cH324CallActiveH324CallType,_X:cH324CallActiveUsedBandwidth,_Y:cH324CallActiveTxVideoCodec,_Z:cH324CallActiveTxVideoPackets,_a:cH324CallActiveTxVideoBytes,_b:cH324CallActiveRxVideoCodec,_c:cH324CallActiveRxVideoPackets,_d:cH324CallActiveRxVideoBytes,'ciscoH324DialControlMIBConform':ciscoH324DialControlMIBConform,'ciscoH324DialControlMIBConformance':ciscoH324DialControlMIBConformance,'ciscoH324DialControlMIBCompliances':ciscoH324DialControlMIBCompliances,'ciscoH324DialControlMIBCompliance':ciscoH324DialControlMIBCompliance,'ciscoH324DialControlMIBGroups':ciscoH324DialControlMIBGroups,_e:cH324CallHistoryGroup,_f:cH324CallActiveGroup})