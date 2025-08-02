_g='cvH320CallActiveGroup'
_f='cvH320CallHistoryGroup'
_e='cvH320CallActiveRxVideoBytes'
_d='cvH320CallActiveRxVideoPackets'
_c='cvH320CallActiveRxVideoCodec'
_b='cvH320CallActiveTxVideoBytes'
_a='cvH320CallActiveTxVideoPackets'
_Z='cvH320CallActiveTxVideoCodec'
_Y='cvH320CallActiveUsedBandwidth'
_X='cvH320CallActiveH320CallType'
_W='cvH320CallActiveIncomingConnectionId'
_V='cvH320CallActiveConnectionId'
_U='cvH320CallHistoryRxVideoBytes'
_T='cvH320CallHistoryRxVideoPackets'
_S='cvH320CallHistoryRxVideoCodec'
_R='cvH320CallHistoryTxVideoBytes'
_Q='cvH320CallHistoryTxVideoPackets'
_P='cvH320CallHistoryTxVideoCodec'
_O='cvH320CallHistoryUsedBandwidth'
_N='cvH320CallHistoryH320CallType'
_M='cvH320CallHistoryIncomingConnectionId'
_L='cvH320CallHistoryConnectionId'
_K='kilobits per second'
_J='callActiveSetupTime'
_I='callActiveIndex'
_H='cCallHistoryIndex'
_G='CISCO-DIAL-CONTROL-MIB'
_F='Integer32'
_E='DIAL-CONTROL-MIB'
_D='bytes'
_C='read-only'
_B='CISCO-H320-DIAL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_G,_H)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CvcGUid,CvcH320CallType,CvcVideoCoderRate=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB','CvcGUid','CvcH320CallType','CvcVideoCoderRate')
AbsoluteCounter32,callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_E,'AbsoluteCounter32',_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoH320DialControlMIB=ModuleIdentity((1,3,6,1,4,1,9,10,128))
if mibBuilder.loadTexts:ciscoH320DialControlMIB.setRevisions(('2006-02-23 00:00','2005-09-28 00:00'))
_CiscoH320DialControlMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoH320DialControlMIBNotifs=_CiscoH320DialControlMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,128,0))
_CiscoH320DialControlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoH320DialControlMIBObjects=_CiscoH320DialControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,128,1))
_CvH320CallHistory_ObjectIdentity=ObjectIdentity
cvH320CallHistory=_CvH320CallHistory_ObjectIdentity((1,3,6,1,4,1,9,10,128,1,1))
_CvH320CallHistoryTable_Object=MibTable
cvH320CallHistoryTable=_CvH320CallHistoryTable_Object((1,3,6,1,4,1,9,10,128,1,1,1))
if mibBuilder.loadTexts:cvH320CallHistoryTable.setStatus(_A)
_CvH320CallHistoryEntry_Object=MibTableRow
cvH320CallHistoryEntry=_CvH320CallHistoryEntry_Object((1,3,6,1,4,1,9,10,128,1,1,1,1))
cvH320CallHistoryEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cvH320CallHistoryEntry.setStatus(_A)
_CvH320CallHistoryConnectionId_Type=CvcGUid
_CvH320CallHistoryConnectionId_Object=MibTableColumn
cvH320CallHistoryConnectionId=_CvH320CallHistoryConnectionId_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,1),_CvH320CallHistoryConnectionId_Type())
cvH320CallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryConnectionId.setStatus(_A)
_CvH320CallHistoryIncomingConnectionId_Type=CvcGUid
_CvH320CallHistoryIncomingConnectionId_Object=MibTableColumn
cvH320CallHistoryIncomingConnectionId=_CvH320CallHistoryIncomingConnectionId_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,2),_CvH320CallHistoryIncomingConnectionId_Type())
cvH320CallHistoryIncomingConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryIncomingConnectionId.setStatus(_A)
_CvH320CallHistoryH320CallType_Type=CvcH320CallType
_CvH320CallHistoryH320CallType_Object=MibTableColumn
cvH320CallHistoryH320CallType=_CvH320CallHistoryH320CallType_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,3),_CvH320CallHistoryH320CallType_Type())
cvH320CallHistoryH320CallType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryH320CallType.setStatus(_A)
class _CvH320CallHistoryUsedBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CvH320CallHistoryUsedBandwidth_Type.__name__=_F
_CvH320CallHistoryUsedBandwidth_Object=MibTableColumn
cvH320CallHistoryUsedBandwidth=_CvH320CallHistoryUsedBandwidth_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,4),_CvH320CallHistoryUsedBandwidth_Type())
cvH320CallHistoryUsedBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryUsedBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cvH320CallHistoryUsedBandwidth.setUnits(_K)
_CvH320CallHistoryTxVideoCodec_Type=CvcVideoCoderRate
_CvH320CallHistoryTxVideoCodec_Object=MibTableColumn
cvH320CallHistoryTxVideoCodec=_CvH320CallHistoryTxVideoCodec_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,5),_CvH320CallHistoryTxVideoCodec_Type())
cvH320CallHistoryTxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryTxVideoCodec.setStatus(_A)
_CvH320CallHistoryTxVideoPackets_Type=AbsoluteCounter32
_CvH320CallHistoryTxVideoPackets_Object=MibTableColumn
cvH320CallHistoryTxVideoPackets=_CvH320CallHistoryTxVideoPackets_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,6),_CvH320CallHistoryTxVideoPackets_Type())
cvH320CallHistoryTxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryTxVideoPackets.setStatus(_A)
_CvH320CallHistoryTxVideoBytes_Type=AbsoluteCounter32
_CvH320CallHistoryTxVideoBytes_Object=MibTableColumn
cvH320CallHistoryTxVideoBytes=_CvH320CallHistoryTxVideoBytes_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,7),_CvH320CallHistoryTxVideoBytes_Type())
cvH320CallHistoryTxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryTxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cvH320CallHistoryTxVideoBytes.setUnits(_D)
_CvH320CallHistoryRxVideoCodec_Type=CvcVideoCoderRate
_CvH320CallHistoryRxVideoCodec_Object=MibTableColumn
cvH320CallHistoryRxVideoCodec=_CvH320CallHistoryRxVideoCodec_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,8),_CvH320CallHistoryRxVideoCodec_Type())
cvH320CallHistoryRxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryRxVideoCodec.setStatus(_A)
_CvH320CallHistoryRxVideoPackets_Type=AbsoluteCounter32
_CvH320CallHistoryRxVideoPackets_Object=MibTableColumn
cvH320CallHistoryRxVideoPackets=_CvH320CallHistoryRxVideoPackets_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,9),_CvH320CallHistoryRxVideoPackets_Type())
cvH320CallHistoryRxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryRxVideoPackets.setStatus(_A)
_CvH320CallHistoryRxVideoBytes_Type=AbsoluteCounter32
_CvH320CallHistoryRxVideoBytes_Object=MibTableColumn
cvH320CallHistoryRxVideoBytes=_CvH320CallHistoryRxVideoBytes_Object((1,3,6,1,4,1,9,10,128,1,1,1,1,10),_CvH320CallHistoryRxVideoBytes_Type())
cvH320CallHistoryRxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallHistoryRxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cvH320CallHistoryRxVideoBytes.setUnits(_D)
_CvH320CallActive_ObjectIdentity=ObjectIdentity
cvH320CallActive=_CvH320CallActive_ObjectIdentity((1,3,6,1,4,1,9,10,128,1,2))
_CvH320CallActiveTable_Object=MibTable
cvH320CallActiveTable=_CvH320CallActiveTable_Object((1,3,6,1,4,1,9,10,128,1,2,1))
if mibBuilder.loadTexts:cvH320CallActiveTable.setStatus(_A)
_CvH320CallActiveEntry_Object=MibTableRow
cvH320CallActiveEntry=_CvH320CallActiveEntry_Object((1,3,6,1,4,1,9,10,128,1,2,1,1))
cvH320CallActiveEntry.setIndexNames((0,_E,_J),(0,_E,_I))
if mibBuilder.loadTexts:cvH320CallActiveEntry.setStatus(_A)
_CvH320CallActiveConnectionId_Type=CvcGUid
_CvH320CallActiveConnectionId_Object=MibTableColumn
cvH320CallActiveConnectionId=_CvH320CallActiveConnectionId_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,1),_CvH320CallActiveConnectionId_Type())
cvH320CallActiveConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveConnectionId.setStatus(_A)
_CvH320CallActiveIncomingConnectionId_Type=CvcGUid
_CvH320CallActiveIncomingConnectionId_Object=MibTableColumn
cvH320CallActiveIncomingConnectionId=_CvH320CallActiveIncomingConnectionId_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,2),_CvH320CallActiveIncomingConnectionId_Type())
cvH320CallActiveIncomingConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveIncomingConnectionId.setStatus(_A)
_CvH320CallActiveH320CallType_Type=CvcH320CallType
_CvH320CallActiveH320CallType_Object=MibTableColumn
cvH320CallActiveH320CallType=_CvH320CallActiveH320CallType_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,3),_CvH320CallActiveH320CallType_Type())
cvH320CallActiveH320CallType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveH320CallType.setStatus(_A)
class _CvH320CallActiveUsedBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CvH320CallActiveUsedBandwidth_Type.__name__=_F
_CvH320CallActiveUsedBandwidth_Object=MibTableColumn
cvH320CallActiveUsedBandwidth=_CvH320CallActiveUsedBandwidth_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,4),_CvH320CallActiveUsedBandwidth_Type())
cvH320CallActiveUsedBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveUsedBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cvH320CallActiveUsedBandwidth.setUnits(_K)
_CvH320CallActiveTxVideoCodec_Type=CvcVideoCoderRate
_CvH320CallActiveTxVideoCodec_Object=MibTableColumn
cvH320CallActiveTxVideoCodec=_CvH320CallActiveTxVideoCodec_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,5),_CvH320CallActiveTxVideoCodec_Type())
cvH320CallActiveTxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveTxVideoCodec.setStatus(_A)
_CvH320CallActiveTxVideoPackets_Type=AbsoluteCounter32
_CvH320CallActiveTxVideoPackets_Object=MibTableColumn
cvH320CallActiveTxVideoPackets=_CvH320CallActiveTxVideoPackets_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,6),_CvH320CallActiveTxVideoPackets_Type())
cvH320CallActiveTxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveTxVideoPackets.setStatus(_A)
_CvH320CallActiveTxVideoBytes_Type=AbsoluteCounter32
_CvH320CallActiveTxVideoBytes_Object=MibTableColumn
cvH320CallActiveTxVideoBytes=_CvH320CallActiveTxVideoBytes_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,7),_CvH320CallActiveTxVideoBytes_Type())
cvH320CallActiveTxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveTxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cvH320CallActiveTxVideoBytes.setUnits(_D)
_CvH320CallActiveRxVideoCodec_Type=CvcVideoCoderRate
_CvH320CallActiveRxVideoCodec_Object=MibTableColumn
cvH320CallActiveRxVideoCodec=_CvH320CallActiveRxVideoCodec_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,8),_CvH320CallActiveRxVideoCodec_Type())
cvH320CallActiveRxVideoCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveRxVideoCodec.setStatus(_A)
_CvH320CallActiveRxVideoPackets_Type=AbsoluteCounter32
_CvH320CallActiveRxVideoPackets_Object=MibTableColumn
cvH320CallActiveRxVideoPackets=_CvH320CallActiveRxVideoPackets_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,9),_CvH320CallActiveRxVideoPackets_Type())
cvH320CallActiveRxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveRxVideoPackets.setStatus(_A)
_CvH320CallActiveRxVideoBytes_Type=AbsoluteCounter32
_CvH320CallActiveRxVideoBytes_Object=MibTableColumn
cvH320CallActiveRxVideoBytes=_CvH320CallActiveRxVideoBytes_Object((1,3,6,1,4,1,9,10,128,1,2,1,1,10),_CvH320CallActiveRxVideoBytes_Type())
cvH320CallActiveRxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cvH320CallActiveRxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cvH320CallActiveRxVideoBytes.setUnits(_D)
_CiscoH320DialControlMIBConform_ObjectIdentity=ObjectIdentity
ciscoH320DialControlMIBConform=_CiscoH320DialControlMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,128,2))
_CiscoH320DialControlMIBConformance_ObjectIdentity=ObjectIdentity
ciscoH320DialControlMIBConformance=_CiscoH320DialControlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,128,2,1))
_CiscoH320DialControlMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoH320DialControlMIBCompliances=_CiscoH320DialControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,128,2,1,1))
_CiscoH320DialControlMIBGroups_ObjectIdentity=ObjectIdentity
ciscoH320DialControlMIBGroups=_CiscoH320DialControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,128,2,1,2))
cvH320CallHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,10,128,2,1,2,1))
cvH320CallHistoryGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cvH320CallHistoryGroup.setStatus(_A)
cvH320CallActiveGroup=ObjectGroup((1,3,6,1,4,1,9,10,128,2,1,2,2))
cvH320CallActiveGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cvH320CallActiveGroup.setStatus(_A)
ciscoH320DialControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,128,2,1,1,1))
ciscoH320DialControlMIBCompliance.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciscoH320DialControlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoH320DialControlMIB':ciscoH320DialControlMIB,'ciscoH320DialControlMIBNotifs':ciscoH320DialControlMIBNotifs,'ciscoH320DialControlMIBObjects':ciscoH320DialControlMIBObjects,'cvH320CallHistory':cvH320CallHistory,'cvH320CallHistoryTable':cvH320CallHistoryTable,'cvH320CallHistoryEntry':cvH320CallHistoryEntry,_L:cvH320CallHistoryConnectionId,_M:cvH320CallHistoryIncomingConnectionId,_N:cvH320CallHistoryH320CallType,_O:cvH320CallHistoryUsedBandwidth,_P:cvH320CallHistoryTxVideoCodec,_Q:cvH320CallHistoryTxVideoPackets,_R:cvH320CallHistoryTxVideoBytes,_S:cvH320CallHistoryRxVideoCodec,_T:cvH320CallHistoryRxVideoPackets,_U:cvH320CallHistoryRxVideoBytes,'cvH320CallActive':cvH320CallActive,'cvH320CallActiveTable':cvH320CallActiveTable,'cvH320CallActiveEntry':cvH320CallActiveEntry,_V:cvH320CallActiveConnectionId,_W:cvH320CallActiveIncomingConnectionId,_X:cvH320CallActiveH320CallType,_Y:cvH320CallActiveUsedBandwidth,_Z:cvH320CallActiveTxVideoCodec,_a:cvH320CallActiveTxVideoPackets,_b:cvH320CallActiveTxVideoBytes,_c:cvH320CallActiveRxVideoCodec,_d:cvH320CallActiveRxVideoPackets,_e:cvH320CallActiveRxVideoBytes,'ciscoH320DialControlMIBConform':ciscoH320DialControlMIBConform,'ciscoH320DialControlMIBConformance':ciscoH320DialControlMIBConformance,'ciscoH320DialControlMIBCompliances':ciscoH320DialControlMIBCompliances,'ciscoH320DialControlMIBCompliance':ciscoH320DialControlMIBCompliance,'ciscoH320DialControlMIBGroups':ciscoH320DialControlMIBGroups,_f:cvH320CallHistoryGroup,_g:cvH320CallActiveGroup})