_e='ciscoIsdnMibGroupRev1'
_d='ciscoIsdnMibGroup'
_c='seconds'
_b='not-accessible'
_a='demandNbrId'
_Z='demandNbrPhysIf'
_Y='isdnSignalingIfIndex'
_X='isdnLapdOperStatus'
_W='demandNbrCallOrigin'
_V='demandNbrStatus'
_U='demandNbrLastAttemptTime'
_T='demandNbrRefuseCalls'
_S='demandNbrAcceptCalls'
_R='demandNbrFailCalls'
_Q='demandNbrSuccessCalls'
_P='demandNbrMaxDuration'
_O='demandNbrPermission'
_N='ISDN-MIB'
_M='ifIndex'
_L='IF-MIB'
_K='demandNbrClearCode'
_J='demandNbrClearReason'
_I='demandNbrLastDuration'
_H='demandNbrAddress'
_G='demandNbrName'
_F='demandNbrLogIf'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-ISDN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_L,_M)
isdnLapdOperStatus,isdnSignalingIfIndex,isdnSignalingIndex=mibBuilder.importSymbols(_N,_X,_Y,'isdnSignalingIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoIsdnMib=ModuleIdentity((1,3,6,1,4,1,9,9,26))
if mibBuilder.loadTexts:ciscoIsdnMib.setRevisions(('2001-02-09 00:00','2000-03-27 00:00','2000-02-23 00:00','1999-05-07 00:00','1996-02-21 00:00','1995-08-15 00:00','1995-01-30 00:00'))
_CiscoIsdnMibObjects_ObjectIdentity=ObjectIdentity
ciscoIsdnMibObjects=_CiscoIsdnMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,26,1))
_IsdnNeighbor_ObjectIdentity=ObjectIdentity
isdnNeighbor=_IsdnNeighbor_ObjectIdentity((1,3,6,1,4,1,9,9,26,1,1))
_DemandNbrTable_Object=MibTable
demandNbrTable=_DemandNbrTable_Object((1,3,6,1,4,1,9,9,26,1,1,1))
if mibBuilder.loadTexts:demandNbrTable.setStatus(_B)
_DemandNbrEntry_Object=MibTableRow
demandNbrEntry=_DemandNbrEntry_Object((1,3,6,1,4,1,9,9,26,1,1,1,1))
demandNbrEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:demandNbrEntry.setStatus(_B)
class _DemandNbrPhysIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DemandNbrPhysIf_Type.__name__=_D
_DemandNbrPhysIf_Object=MibTableColumn
demandNbrPhysIf=_DemandNbrPhysIf_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,1),_DemandNbrPhysIf_Type())
demandNbrPhysIf.setMaxAccess(_b)
if mibBuilder.loadTexts:demandNbrPhysIf.setStatus(_B)
class _DemandNbrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DemandNbrId_Type.__name__=_D
_DemandNbrId_Object=MibTableColumn
demandNbrId=_DemandNbrId_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,2),_DemandNbrId_Type())
demandNbrId.setMaxAccess(_b)
if mibBuilder.loadTexts:demandNbrId.setStatus(_B)
class _DemandNbrLogIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DemandNbrLogIf_Type.__name__=_D
_DemandNbrLogIf_Object=MibTableColumn
demandNbrLogIf=_DemandNbrLogIf_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,3),_DemandNbrLogIf_Type())
demandNbrLogIf.setMaxAccess(_E)
if mibBuilder.loadTexts:demandNbrLogIf.setStatus(_B)
_DemandNbrName_Type=DisplayString
_DemandNbrName_Object=MibTableColumn
demandNbrName=_DemandNbrName_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,4),_DemandNbrName_Type())
demandNbrName.setMaxAccess(_E)
if mibBuilder.loadTexts:demandNbrName.setStatus(_B)
_DemandNbrAddress_Type=DisplayString
_DemandNbrAddress_Object=MibTableColumn
demandNbrAddress=_DemandNbrAddress_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,5),_DemandNbrAddress_Type())
demandNbrAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:demandNbrAddress.setStatus(_B)
class _DemandNbrPermission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('iCanCallHim',1),('heCanCallMe',2),('weCanCallEachOther',3)))
_DemandNbrPermission_Type.__name__=_D
_DemandNbrPermission_Object=MibTableColumn
demandNbrPermission=_DemandNbrPermission_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,6),_DemandNbrPermission_Type())
demandNbrPermission.setMaxAccess(_E)
if mibBuilder.loadTexts:demandNbrPermission.setStatus(_B)
class _DemandNbrMaxDuration_Type(Integer32):defaultValue=2147483647;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DemandNbrMaxDuration_Type.__name__=_D
_DemandNbrMaxDuration_Object=MibTableColumn
demandNbrMaxDuration=_DemandNbrMaxDuration_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,7),_DemandNbrMaxDuration_Type())
demandNbrMaxDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:demandNbrMaxDuration.setStatus(_B)
if mibBuilder.loadTexts:demandNbrMaxDuration.setUnits(_c)
class _DemandNbrLastDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DemandNbrLastDuration_Type.__name__=_D
_DemandNbrLastDuration_Object=MibTableColumn
demandNbrLastDuration=_DemandNbrLastDuration_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,8),_DemandNbrLastDuration_Type())
demandNbrLastDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrLastDuration.setStatus(_B)
if mibBuilder.loadTexts:demandNbrLastDuration.setUnits(_c)
_DemandNbrClearReason_Type=DisplayString
_DemandNbrClearReason_Object=MibTableColumn
demandNbrClearReason=_DemandNbrClearReason_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,9),_DemandNbrClearReason_Type())
demandNbrClearReason.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrClearReason.setStatus(_B)
_DemandNbrClearCode_Type=OctetString
_DemandNbrClearCode_Object=MibTableColumn
demandNbrClearCode=_DemandNbrClearCode_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,10),_DemandNbrClearCode_Type())
demandNbrClearCode.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrClearCode.setStatus(_B)
_DemandNbrSuccessCalls_Type=Counter32
_DemandNbrSuccessCalls_Object=MibTableColumn
demandNbrSuccessCalls=_DemandNbrSuccessCalls_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,11),_DemandNbrSuccessCalls_Type())
demandNbrSuccessCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrSuccessCalls.setStatus(_B)
_DemandNbrFailCalls_Type=Counter32
_DemandNbrFailCalls_Object=MibTableColumn
demandNbrFailCalls=_DemandNbrFailCalls_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,12),_DemandNbrFailCalls_Type())
demandNbrFailCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrFailCalls.setStatus(_B)
_DemandNbrAcceptCalls_Type=Counter32
_DemandNbrAcceptCalls_Object=MibTableColumn
demandNbrAcceptCalls=_DemandNbrAcceptCalls_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,13),_DemandNbrAcceptCalls_Type())
demandNbrAcceptCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrAcceptCalls.setStatus(_B)
_DemandNbrRefuseCalls_Type=Counter32
_DemandNbrRefuseCalls_Object=MibTableColumn
demandNbrRefuseCalls=_DemandNbrRefuseCalls_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,14),_DemandNbrRefuseCalls_Type())
demandNbrRefuseCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrRefuseCalls.setStatus(_B)
_DemandNbrLastAttemptTime_Type=TimeStamp
_DemandNbrLastAttemptTime_Object=MibTableColumn
demandNbrLastAttemptTime=_DemandNbrLastAttemptTime_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,15),_DemandNbrLastAttemptTime_Type())
demandNbrLastAttemptTime.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrLastAttemptTime.setStatus(_B)
_DemandNbrStatus_Type=RowStatus
_DemandNbrStatus_Object=MibTableColumn
demandNbrStatus=_DemandNbrStatus_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,16),_DemandNbrStatus_Type())
demandNbrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:demandNbrStatus.setStatus(_B)
class _DemandNbrCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('originate',1),('answer',2),('callback',3)))
_DemandNbrCallOrigin_Type.__name__=_D
_DemandNbrCallOrigin_Object=MibTableColumn
demandNbrCallOrigin=_DemandNbrCallOrigin_Object((1,3,6,1,4,1,9,9,26,1,1,1,1,17),_DemandNbrCallOrigin_Type())
demandNbrCallOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:demandNbrCallOrigin.setStatus(_B)
_CiscoIsdnMibTrapPrefix_ObjectIdentity=ObjectIdentity
ciscoIsdnMibTrapPrefix=_CiscoIsdnMibTrapPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,26,2))
_CiscoIsdnMibTraps_ObjectIdentity=ObjectIdentity
ciscoIsdnMibTraps=_CiscoIsdnMibTraps_ObjectIdentity((1,3,6,1,4,1,9,9,26,2,0))
_CiscoIsdnMibConformance_ObjectIdentity=ObjectIdentity
ciscoIsdnMibConformance=_CiscoIsdnMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,26,3))
_CiscoIsdnMibCompliances_ObjectIdentity=ObjectIdentity
ciscoIsdnMibCompliances=_CiscoIsdnMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,26,3,1))
_CiscoIsdnMibGroups_ObjectIdentity=ObjectIdentity
ciscoIsdnMibGroups=_CiscoIsdnMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,26,3,2))
ciscoIsdnMibGroup=ObjectGroup((1,3,6,1,4,1,9,9,26,3,2,1))
ciscoIsdnMibGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_I),(_A,_J),(_A,_K),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoIsdnMibGroup.setStatus(_B)
ciscoIsdnMibGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,26,3,2,2))
ciscoIsdnMibGroupRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_I),(_A,_J),(_A,_K),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoIsdnMibGroupRev1.setStatus(_B)
demandNbrCallInformation=NotificationType((1,3,6,1,4,1,9,9,26,2,0,1))
demandNbrCallInformation.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:demandNbrCallInformation.setStatus('obsolete')
demandNbrCallDetails=NotificationType((1,3,6,1,4,1,9,9,26,2,0,2))
demandNbrCallDetails.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_W)))
if mibBuilder.loadTexts:demandNbrCallDetails.setStatus(_B)
demandNbrLayer2Change=NotificationType((1,3,6,1,4,1,9,9,26,2,0,3))
demandNbrLayer2Change.setObjects(*((_L,_M),(_N,_X)))
if mibBuilder.loadTexts:demandNbrLayer2Change.setStatus(_B)
demandNbrCNANotification=NotificationType((1,3,6,1,4,1,9,9,26,2,0,4))
demandNbrCNANotification.setObjects(*((_N,_Y),(_L,_M)))
if mibBuilder.loadTexts:demandNbrCNANotification.setStatus(_B)
ciscoIsdnMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,26,3,1,1))
ciscoIsdnMibCompliance.setObjects((_A,_d))
if mibBuilder.loadTexts:ciscoIsdnMibCompliance.setStatus(_B)
ciscoIsdnMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,26,3,1,2))
ciscoIsdnMibComplianceRev1.setObjects((_A,_e))
if mibBuilder.loadTexts:ciscoIsdnMibComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoIsdnMib':ciscoIsdnMib,'ciscoIsdnMibObjects':ciscoIsdnMibObjects,'isdnNeighbor':isdnNeighbor,'demandNbrTable':demandNbrTable,'demandNbrEntry':demandNbrEntry,_Z:demandNbrPhysIf,_a:demandNbrId,_F:demandNbrLogIf,_G:demandNbrName,_H:demandNbrAddress,_O:demandNbrPermission,_P:demandNbrMaxDuration,_I:demandNbrLastDuration,_J:demandNbrClearReason,_K:demandNbrClearCode,_Q:demandNbrSuccessCalls,_R:demandNbrFailCalls,_S:demandNbrAcceptCalls,_T:demandNbrRefuseCalls,_U:demandNbrLastAttemptTime,_V:demandNbrStatus,_W:demandNbrCallOrigin,'ciscoIsdnMibTrapPrefix':ciscoIsdnMibTrapPrefix,'ciscoIsdnMibTraps':ciscoIsdnMibTraps,'demandNbrCallInformation':demandNbrCallInformation,'demandNbrCallDetails':demandNbrCallDetails,'demandNbrLayer2Change':demandNbrLayer2Change,'demandNbrCNANotification':demandNbrCNANotification,'ciscoIsdnMibConformance':ciscoIsdnMibConformance,'ciscoIsdnMibCompliances':ciscoIsdnMibCompliances,'ciscoIsdnMibCompliance':ciscoIsdnMibCompliance,'ciscoIsdnMibComplianceRev1':ciscoIsdnMibComplianceRev1,'ciscoIsdnMibGroups':ciscoIsdnMibGroups,_d:ciscoIsdnMibGroup,_e:ciscoIsdnMibGroupRev1})