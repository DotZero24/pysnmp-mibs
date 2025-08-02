_b='mgcRedundancyProtocolGroup'
_a='mgcRedundancyParamGroup'
_Z='mgcRedundancyGroup'
_Y='mgcRedGrpProtCancelGraceful'
_X='mgcRedGrpProtDisconnectProcedure'
_W='mgcRedGrpProtResponseAckAttr'
_V='mgcRedGrpProtProvisionalResponse'
_U='mgcRedGrpProtSigEvtOnOffPolicy'
_T='mgcRedGrpProtQuarantinePolicy'
_S='mgcRedGrpProtPersistEvtPolicy'
_R='mgcRedundancyGrpProtocolRowStatus'
_Q='mgcRedundancyGrpPriority'
_P='mgcRedundancyGrpCommState'
_O='mgcRedundancyGrpStateChangeNtfy'
_N='mgcRedundancyGrpRowStatus'
_M='mgcRedundancyGrpActState'
_L='mgcRedundancyGrpPref'
_K='read-write'
_J='read-only'
_I='TruthValue'
_H='mgcNumber'
_G='mgProtocolNumber'
_F='CISCO-WAN-MG-MIB'
_E='mgcRedundancyGrpNum'
_D='read-create'
_C='Integer32'
_B='CISCO-WAN-MGC-REDUN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mgProtocolNumber,mgcNumber=mibBuilder.importSymbols(_F,_G,_H)
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
ciscoWanMgcRedunMIB=ModuleIdentity((1,3,6,1,4,1,351,150,22))
if mibBuilder.loadTexts:ciscoWanMgcRedunMIB.setRevisions(('2004-01-19 00:00','2001-12-26 00:00','2001-07-19 15:00'))
_MgcRedundancyObjects_ObjectIdentity=ObjectIdentity
mgcRedundancyObjects=_MgcRedundancyObjects_ObjectIdentity((1,3,6,1,4,1,351,150,22,1))
_MgcRedundancyGrpTable_Object=MibTable
mgcRedundancyGrpTable=_MgcRedundancyGrpTable_Object((1,3,6,1,4,1,351,150,22,1,1))
if mibBuilder.loadTexts:mgcRedundancyGrpTable.setStatus(_A)
_MgcRedundancyGrpEntry_Object=MibTableRow
mgcRedundancyGrpEntry=_MgcRedundancyGrpEntry_Object((1,3,6,1,4,1,351,150,22,1,1,1))
mgcRedundancyGrpEntry.setIndexNames((0,_B,_E),(0,_F,_H))
if mibBuilder.loadTexts:mgcRedundancyGrpEntry.setStatus(_A)
class _MgcRedundancyGrpNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgcRedundancyGrpNum_Type.__name__=_C
_MgcRedundancyGrpNum_Object=MibTableColumn
mgcRedundancyGrpNum=_MgcRedundancyGrpNum_Object((1,3,6,1,4,1,351,150,22,1,1,1,1),_MgcRedundancyGrpNum_Type())
mgcRedundancyGrpNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mgcRedundancyGrpNum.setStatus(_A)
class _MgcRedundancyGrpPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgcRedundancyGrpPref_Type.__name__=_C
_MgcRedundancyGrpPref_Object=MibTableColumn
mgcRedundancyGrpPref=_MgcRedundancyGrpPref_Object((1,3,6,1,4,1,351,150,22,1,1,1,2),_MgcRedundancyGrpPref_Type())
mgcRedundancyGrpPref.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedundancyGrpPref.setStatus(_A)
class _MgcRedundancyGrpActState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgcActive',1),('mgcInactive',2)))
_MgcRedundancyGrpActState_Type.__name__=_C
_MgcRedundancyGrpActState_Object=MibTableColumn
mgcRedundancyGrpActState=_MgcRedundancyGrpActState_Object((1,3,6,1,4,1,351,150,22,1,1,1,3),_MgcRedundancyGrpActState_Type())
mgcRedundancyGrpActState.setMaxAccess(_J)
if mibBuilder.loadTexts:mgcRedundancyGrpActState.setStatus(_A)
_MgcRedundancyGrpRowStatus_Type=RowStatus
_MgcRedundancyGrpRowStatus_Object=MibTableColumn
mgcRedundancyGrpRowStatus=_MgcRedundancyGrpRowStatus_Object((1,3,6,1,4,1,351,150,22,1,1,1,4),_MgcRedundancyGrpRowStatus_Type())
mgcRedundancyGrpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedundancyGrpRowStatus.setStatus(_A)
_MgcRedundancyGrpParamTable_Object=MibTable
mgcRedundancyGrpParamTable=_MgcRedundancyGrpParamTable_Object((1,3,6,1,4,1,351,150,22,1,2))
if mibBuilder.loadTexts:mgcRedundancyGrpParamTable.setStatus(_A)
_MgcRedundancyGrpParamEntry_Object=MibTableRow
mgcRedundancyGrpParamEntry=_MgcRedundancyGrpParamEntry_Object((1,3,6,1,4,1,351,150,22,1,2,1))
mgcRedundancyGrpParamEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:mgcRedundancyGrpParamEntry.setStatus(_A)
class _MgcRedundancyGrpStateChangeNtfy_Type(TruthValue):defaultValue=1
_MgcRedundancyGrpStateChangeNtfy_Type.__name__=_I
_MgcRedundancyGrpStateChangeNtfy_Object=MibTableColumn
mgcRedundancyGrpStateChangeNtfy=_MgcRedundancyGrpStateChangeNtfy_Object((1,3,6,1,4,1,351,150,22,1,2,1,1),_MgcRedundancyGrpStateChangeNtfy_Type())
mgcRedundancyGrpStateChangeNtfy.setMaxAccess(_K)
if mibBuilder.loadTexts:mgcRedundancyGrpStateChangeNtfy.setStatus(_A)
class _MgcRedundancyGrpCommState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('commOk',1),('commLoss',2)))
_MgcRedundancyGrpCommState_Type.__name__=_C
_MgcRedundancyGrpCommState_Object=MibTableColumn
mgcRedundancyGrpCommState=_MgcRedundancyGrpCommState_Object((1,3,6,1,4,1,351,150,22,1,2,1,2),_MgcRedundancyGrpCommState_Type())
mgcRedundancyGrpCommState.setMaxAccess(_J)
if mibBuilder.loadTexts:mgcRedundancyGrpCommState.setStatus(_A)
class _MgcRedundancyGrpPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MgcRedundancyGrpPriority_Type.__name__=_C
_MgcRedundancyGrpPriority_Object=MibTableColumn
mgcRedundancyGrpPriority=_MgcRedundancyGrpPriority_Object((1,3,6,1,4,1,351,150,22,1,2,1,3),_MgcRedundancyGrpPriority_Type())
mgcRedundancyGrpPriority.setMaxAccess(_K)
if mibBuilder.loadTexts:mgcRedundancyGrpPriority.setStatus(_A)
_MgcRedundancyGrpProtocolTable_Object=MibTable
mgcRedundancyGrpProtocolTable=_MgcRedundancyGrpProtocolTable_Object((1,3,6,1,4,1,351,150,22,1,3))
if mibBuilder.loadTexts:mgcRedundancyGrpProtocolTable.setStatus(_A)
_MgcRedundancyGrpProtocolEntry_Object=MibTableRow
mgcRedundancyGrpProtocolEntry=_MgcRedundancyGrpProtocolEntry_Object((1,3,6,1,4,1,351,150,22,1,3,1))
mgcRedundancyGrpProtocolEntry.setIndexNames((0,_B,_E),(0,_F,_G))
if mibBuilder.loadTexts:mgcRedundancyGrpProtocolEntry.setStatus(_A)
_MgcRedundancyGrpProtocolRowStatus_Type=RowStatus
_MgcRedundancyGrpProtocolRowStatus_Object=MibTableColumn
mgcRedundancyGrpProtocolRowStatus=_MgcRedundancyGrpProtocolRowStatus_Object((1,3,6,1,4,1,351,150,22,1,3,1,1),_MgcRedundancyGrpProtocolRowStatus_Type())
mgcRedundancyGrpProtocolRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedundancyGrpProtocolRowStatus.setStatus(_A)
class _MgcRedGrpProtPersistEvtPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('quarantinePersistEvts',1),('notQuarantinePersistEvts',2)))
_MgcRedGrpProtPersistEvtPolicy_Type.__name__=_C
_MgcRedGrpProtPersistEvtPolicy_Object=MibTableColumn
mgcRedGrpProtPersistEvtPolicy=_MgcRedGrpProtPersistEvtPolicy_Object((1,3,6,1,4,1,351,150,22,1,3,1,2),_MgcRedGrpProtPersistEvtPolicy_Type())
mgcRedGrpProtPersistEvtPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedGrpProtPersistEvtPolicy.setStatus(_A)
class _MgcRedGrpProtQuarantinePolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stepProcess',1),('stepDiscard',2),('loopProcess',3),('loopDiscard',4)))
_MgcRedGrpProtQuarantinePolicy_Type.__name__=_C
_MgcRedGrpProtQuarantinePolicy_Object=MibTableColumn
mgcRedGrpProtQuarantinePolicy=_MgcRedGrpProtQuarantinePolicy_Object((1,3,6,1,4,1,351,150,22,1,3,1,3),_MgcRedGrpProtQuarantinePolicy_Type())
mgcRedGrpProtQuarantinePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedGrpProtQuarantinePolicy.setStatus(_A)
class _MgcRedGrpProtSigEvtOnOffPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deleteEventNotPresent',1),('deleteOnlyNegatedEvent',2)))
_MgcRedGrpProtSigEvtOnOffPolicy_Type.__name__=_C
_MgcRedGrpProtSigEvtOnOffPolicy_Object=MibTableColumn
mgcRedGrpProtSigEvtOnOffPolicy=_MgcRedGrpProtSigEvtOnOffPolicy_Object((1,3,6,1,4,1,351,150,22,1,3,1,4),_MgcRedGrpProtSigEvtOnOffPolicy_Type())
mgcRedGrpProtSigEvtOnOffPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedGrpProtSigEvtOnOffPolicy.setStatus(_A)
class _MgcRedGrpProtProvisionalResponse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sendProvisionalResponse',1),('notSendProvisionalResponse',2)))
_MgcRedGrpProtProvisionalResponse_Type.__name__=_C
_MgcRedGrpProtProvisionalResponse_Object=MibTableColumn
mgcRedGrpProtProvisionalResponse=_MgcRedGrpProtProvisionalResponse_Object((1,3,6,1,4,1,351,150,22,1,3,1,5),_MgcRedGrpProtProvisionalResponse_Type())
mgcRedGrpProtProvisionalResponse.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedGrpProtProvisionalResponse.setStatus(_A)
class _MgcRedGrpProtResponseAckAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sendResponseAckAttr',1),('notSendResponseAckAttr',2)))
_MgcRedGrpProtResponseAckAttr_Type.__name__=_C
_MgcRedGrpProtResponseAckAttr_Object=MibTableColumn
mgcRedGrpProtResponseAckAttr=_MgcRedGrpProtResponseAckAttr_Object((1,3,6,1,4,1,351,150,22,1,3,1,6),_MgcRedGrpProtResponseAckAttr_Type())
mgcRedGrpProtResponseAckAttr.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedGrpProtResponseAckAttr.setStatus(_A)
class _MgcRedGrpProtDisconnectProcedure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doDisconnectProcedure',1),('notDoDisconnectProcedure',2)))
_MgcRedGrpProtDisconnectProcedure_Type.__name__=_C
_MgcRedGrpProtDisconnectProcedure_Object=MibTableColumn
mgcRedGrpProtDisconnectProcedure=_MgcRedGrpProtDisconnectProcedure_Object((1,3,6,1,4,1,351,150,22,1,3,1,7),_MgcRedGrpProtDisconnectProcedure_Type())
mgcRedGrpProtDisconnectProcedure.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedGrpProtDisconnectProcedure.setStatus(_A)
class _MgcRedGrpProtCancelGraceful_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sendCancelGraceful',1),('notSendCancelGraceful',2)))
_MgcRedGrpProtCancelGraceful_Type.__name__=_C
_MgcRedGrpProtCancelGraceful_Object=MibTableColumn
mgcRedGrpProtCancelGraceful=_MgcRedGrpProtCancelGraceful_Object((1,3,6,1,4,1,351,150,22,1,3,1,8),_MgcRedGrpProtCancelGraceful_Type())
mgcRedGrpProtCancelGraceful.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRedGrpProtCancelGraceful.setStatus(_A)
_MgcRedunNotificationPrefix_ObjectIdentity=ObjectIdentity
mgcRedunNotificationPrefix=_MgcRedunNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,351,150,22,2))
_MgcRedunNotifications_ObjectIdentity=ObjectIdentity
mgcRedunNotifications=_MgcRedunNotifications_ObjectIdentity((1,3,6,1,4,1,351,150,22,2,0))
_MgcRedunMIBConformance_ObjectIdentity=ObjectIdentity
mgcRedunMIBConformance=_MgcRedunMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,22,3))
_MgcRedunMIBCompliances_ObjectIdentity=ObjectIdentity
mgcRedunMIBCompliances=_MgcRedunMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,22,3,1))
_MgcRedunMIBGroups_ObjectIdentity=ObjectIdentity
mgcRedunMIBGroups=_MgcRedunMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,22,3,2))
mgcRedundancyGroup=ObjectGroup((1,3,6,1,4,1,351,150,22,3,2,1))
mgcRedundancyGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mgcRedundancyGroup.setStatus(_A)
mgcRedundancyParamGroup=ObjectGroup((1,3,6,1,4,1,351,150,22,3,2,2))
mgcRedundancyParamGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:mgcRedundancyParamGroup.setStatus(_A)
mgcRedundancyProtocolGroup=ObjectGroup((1,3,6,1,4,1,351,150,22,3,2,3))
mgcRedundancyProtocolGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:mgcRedundancyProtocolGroup.setStatus(_A)
mgcRedunMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,22,3,1,1))
mgcRedunMIBCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:mgcRedunMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWanMgcRedunMIB':ciscoWanMgcRedunMIB,'mgcRedundancyObjects':mgcRedundancyObjects,'mgcRedundancyGrpTable':mgcRedundancyGrpTable,'mgcRedundancyGrpEntry':mgcRedundancyGrpEntry,_E:mgcRedundancyGrpNum,_L:mgcRedundancyGrpPref,_M:mgcRedundancyGrpActState,_N:mgcRedundancyGrpRowStatus,'mgcRedundancyGrpParamTable':mgcRedundancyGrpParamTable,'mgcRedundancyGrpParamEntry':mgcRedundancyGrpParamEntry,_O:mgcRedundancyGrpStateChangeNtfy,_P:mgcRedundancyGrpCommState,_Q:mgcRedundancyGrpPriority,'mgcRedundancyGrpProtocolTable':mgcRedundancyGrpProtocolTable,'mgcRedundancyGrpProtocolEntry':mgcRedundancyGrpProtocolEntry,_R:mgcRedundancyGrpProtocolRowStatus,_S:mgcRedGrpProtPersistEvtPolicy,_T:mgcRedGrpProtQuarantinePolicy,_U:mgcRedGrpProtSigEvtOnOffPolicy,_V:mgcRedGrpProtProvisionalResponse,_W:mgcRedGrpProtResponseAckAttr,_X:mgcRedGrpProtDisconnectProcedure,_Y:mgcRedGrpProtCancelGraceful,'mgcRedunNotificationPrefix':mgcRedunNotificationPrefix,'mgcRedunNotifications':mgcRedunNotifications,'mgcRedunMIBConformance':mgcRedunMIBConformance,'mgcRedunMIBCompliances':mgcRedunMIBCompliances,'mgcRedunMIBCompliance':mgcRedunMIBCompliance,'mgcRedunMIBGroups':mgcRedunMIBGroups,_Z:mgcRedundancyGroup,_a:mgcRedundancyParamGroup,_b:mgcRedundancyProtocolGroup})