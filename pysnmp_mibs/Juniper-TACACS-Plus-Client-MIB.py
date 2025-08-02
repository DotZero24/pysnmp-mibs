_m='juniTacacsPlusClientHostConfigGroup2'
_l='juniTacacsPlusClientHostConfigGroup'
_k='juniTacacsPlusClientHostOrder'
_j='juniTacacsPlusClientHostDiscontinuityTime'
_i='juniTacacsPlusClientHostAcctTimeouts'
_h='juniTacacsPlusClientHostAcctPending'
_g='juniTacacsPlusClientHostAcctReplies'
_f='juniTacacsPlusClientHostAcctRequests'
_e='juniTacacsPlusClientHostAuthorTimeouts'
_d='juniTacacsPlusClientHostAuthorPending'
_c='juniTacacsPlusClientHostAuthorReplies'
_b='juniTacacsPlusClientHostAuthorRequests'
_a='juniTacacsPlusClientHostAuthTimeouts'
_Z='juniTacacsPlusClientHostAuthPending'
_Y='juniTacacsPlusClientHostAuthReplies'
_X='juniTacacsPlusClientHostAuthRequests'
_W='obsolete'
_V='juniTacacsPlusClientSourceIp'
_U='juniTacacsPlusClientKey'
_T='juniTacacsPlusClientTimeout'
_S='juniTacacsPlusClientDirectedRequest'
_R='juniTacacsPlusClientHostStatsEntry'
_Q='JuniKeyString'
_P='juniTacacsPlusClientHostAddr'
_O='juniTacacsPlusClientHostStatsGroup'
_N='juniTacacsPlusClientCommonGroup'
_M='juniTacacsPlusClientHostStatus'
_L='juniTacacsPlusClientHostKey'
_K='juniTacacsPlusClientHostTimeout'
_J='juniTacacsPlusClientHostSingleConnection'
_I='juniTacacsPlusClientHostPrimary'
_H='juniTacacsPlusClientHostPort'
_G='TruthValue'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='Juniper-TACACS-Plus-Client-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
juniTacacsPlusClientMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,60))
if mibBuilder.loadTexts:juniTacacsPlusClientMIB.setRevisions(('2004-03-02 17:31','2002-09-16 21:44','2002-07-12 13:49'))
class JuniKeyString(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_JuniTacacsPlusClientObjects_ObjectIdentity=ObjectIdentity
juniTacacsPlusClientObjects=_JuniTacacsPlusClientObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,60,1))
_JuniTacacsPlusClientCommonConfig_ObjectIdentity=ObjectIdentity
juniTacacsPlusClientCommonConfig=_JuniTacacsPlusClientCommonConfig_ObjectIdentity((1,3,6,1,4,1,4874,2,2,60,1,1))
class _JuniTacacsPlusClientDirectedRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notRestrictedAndTruncated',1),('disabled',2),('notRestrictedAndNotTruncated',3),('restrictedAndTruncated',4),('restrictedAndNotTruncated',5)))
_JuniTacacsPlusClientDirectedRequest_Type.__name__=_E
_JuniTacacsPlusClientDirectedRequest_Object=MibScalar
juniTacacsPlusClientDirectedRequest=_JuniTacacsPlusClientDirectedRequest_Object((1,3,6,1,4,1,4874,2,2,60,1,1,1),_JuniTacacsPlusClientDirectedRequest_Type())
juniTacacsPlusClientDirectedRequest.setMaxAccess(_F)
if mibBuilder.loadTexts:juniTacacsPlusClientDirectedRequest.setStatus(_B)
class _JuniTacacsPlusClientTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniTacacsPlusClientTimeout_Type.__name__=_E
_JuniTacacsPlusClientTimeout_Object=MibScalar
juniTacacsPlusClientTimeout=_JuniTacacsPlusClientTimeout_Object((1,3,6,1,4,1,4874,2,2,60,1,1,2),_JuniTacacsPlusClientTimeout_Type())
juniTacacsPlusClientTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:juniTacacsPlusClientTimeout.setStatus(_B)
_JuniTacacsPlusClientKey_Type=JuniKeyString
_JuniTacacsPlusClientKey_Object=MibScalar
juniTacacsPlusClientKey=_JuniTacacsPlusClientKey_Object((1,3,6,1,4,1,4874,2,2,60,1,1,3),_JuniTacacsPlusClientKey_Type())
juniTacacsPlusClientKey.setMaxAccess(_F)
if mibBuilder.loadTexts:juniTacacsPlusClientKey.setStatus(_B)
_JuniTacacsPlusClientSourceIp_Type=IpAddress
_JuniTacacsPlusClientSourceIp_Object=MibScalar
juniTacacsPlusClientSourceIp=_JuniTacacsPlusClientSourceIp_Object((1,3,6,1,4,1,4874,2,2,60,1,1,4),_JuniTacacsPlusClientSourceIp_Type())
juniTacacsPlusClientSourceIp.setMaxAccess(_F)
if mibBuilder.loadTexts:juniTacacsPlusClientSourceIp.setStatus(_B)
_JuniTacacsPlusClientHostConfig_ObjectIdentity=ObjectIdentity
juniTacacsPlusClientHostConfig=_JuniTacacsPlusClientHostConfig_ObjectIdentity((1,3,6,1,4,1,4874,2,2,60,1,2))
_JuniTacacsPlusClientHostConfigTable_Object=MibTable
juniTacacsPlusClientHostConfigTable=_JuniTacacsPlusClientHostConfigTable_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1))
if mibBuilder.loadTexts:juniTacacsPlusClientHostConfigTable.setStatus(_B)
_JuniTacacsPlusClientHostConfigEntry_Object=MibTableRow
juniTacacsPlusClientHostConfigEntry=_JuniTacacsPlusClientHostConfigEntry_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1))
juniTacacsPlusClientHostConfigEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:juniTacacsPlusClientHostConfigEntry.setStatus(_B)
_JuniTacacsPlusClientHostAddr_Type=IpAddress
_JuniTacacsPlusClientHostAddr_Object=MibTableColumn
juniTacacsPlusClientHostAddr=_JuniTacacsPlusClientHostAddr_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,1),_JuniTacacsPlusClientHostAddr_Type())
juniTacacsPlusClientHostAddr.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniTacacsPlusClientHostAddr.setStatus(_B)
class _JuniTacacsPlusClientHostPort_Type(Integer32):defaultValue=49;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniTacacsPlusClientHostPort_Type.__name__=_E
_JuniTacacsPlusClientHostPort_Object=MibTableColumn
juniTacacsPlusClientHostPort=_JuniTacacsPlusClientHostPort_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,2),_JuniTacacsPlusClientHostPort_Type())
juniTacacsPlusClientHostPort.setMaxAccess(_D)
if mibBuilder.loadTexts:juniTacacsPlusClientHostPort.setStatus(_B)
class _JuniTacacsPlusClientHostPrimary_Type(TruthValue):defaultValue=2
_JuniTacacsPlusClientHostPrimary_Type.__name__=_G
_JuniTacacsPlusClientHostPrimary_Object=MibTableColumn
juniTacacsPlusClientHostPrimary=_JuniTacacsPlusClientHostPrimary_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,3),_JuniTacacsPlusClientHostPrimary_Type())
juniTacacsPlusClientHostPrimary.setMaxAccess(_D)
if mibBuilder.loadTexts:juniTacacsPlusClientHostPrimary.setStatus(_B)
class _JuniTacacsPlusClientHostSingleConnection_Type(TruthValue):defaultValue=2
_JuniTacacsPlusClientHostSingleConnection_Type.__name__=_G
_JuniTacacsPlusClientHostSingleConnection_Object=MibTableColumn
juniTacacsPlusClientHostSingleConnection=_JuniTacacsPlusClientHostSingleConnection_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,4),_JuniTacacsPlusClientHostSingleConnection_Type())
juniTacacsPlusClientHostSingleConnection.setMaxAccess(_D)
if mibBuilder.loadTexts:juniTacacsPlusClientHostSingleConnection.setStatus(_B)
class _JuniTacacsPlusClientHostTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniTacacsPlusClientHostTimeout_Type.__name__=_E
_JuniTacacsPlusClientHostTimeout_Object=MibTableColumn
juniTacacsPlusClientHostTimeout=_JuniTacacsPlusClientHostTimeout_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,5),_JuniTacacsPlusClientHostTimeout_Type())
juniTacacsPlusClientHostTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:juniTacacsPlusClientHostTimeout.setStatus(_B)
class _JuniTacacsPlusClientHostKey_Type(JuniKeyString):defaultValue=OctetString('')
_JuniTacacsPlusClientHostKey_Type.__name__=_Q
_JuniTacacsPlusClientHostKey_Object=MibTableColumn
juniTacacsPlusClientHostKey=_JuniTacacsPlusClientHostKey_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,6),_JuniTacacsPlusClientHostKey_Type())
juniTacacsPlusClientHostKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniTacacsPlusClientHostKey.setStatus(_B)
_JuniTacacsPlusClientHostStatus_Type=RowStatus
_JuniTacacsPlusClientHostStatus_Object=MibTableColumn
juniTacacsPlusClientHostStatus=_JuniTacacsPlusClientHostStatus_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,7),_JuniTacacsPlusClientHostStatus_Type())
juniTacacsPlusClientHostStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniTacacsPlusClientHostStatus.setStatus(_B)
_JuniTacacsPlusClientHostOrder_Type=Integer32
_JuniTacacsPlusClientHostOrder_Object=MibTableColumn
juniTacacsPlusClientHostOrder=_JuniTacacsPlusClientHostOrder_Object((1,3,6,1,4,1,4874,2,2,60,1,2,1,1,8),_JuniTacacsPlusClientHostOrder_Type())
juniTacacsPlusClientHostOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostOrder.setStatus(_B)
_JuniTacacsPlusClientHostStats_ObjectIdentity=ObjectIdentity
juniTacacsPlusClientHostStats=_JuniTacacsPlusClientHostStats_ObjectIdentity((1,3,6,1,4,1,4874,2,2,60,1,3))
_JuniTacacsPlusClientHostStatsTable_Object=MibTable
juniTacacsPlusClientHostStatsTable=_JuniTacacsPlusClientHostStatsTable_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1))
if mibBuilder.loadTexts:juniTacacsPlusClientHostStatsTable.setStatus(_B)
_JuniTacacsPlusClientHostStatsEntry_Object=MibTableRow
juniTacacsPlusClientHostStatsEntry=_JuniTacacsPlusClientHostStatsEntry_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1))
if mibBuilder.loadTexts:juniTacacsPlusClientHostStatsEntry.setStatus(_B)
_JuniTacacsPlusClientHostAuthRequests_Type=Counter32
_JuniTacacsPlusClientHostAuthRequests_Object=MibTableColumn
juniTacacsPlusClientHostAuthRequests=_JuniTacacsPlusClientHostAuthRequests_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,1),_JuniTacacsPlusClientHostAuthRequests_Type())
juniTacacsPlusClientHostAuthRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthRequests.setStatus(_B)
_JuniTacacsPlusClientHostAuthReplies_Type=Counter32
_JuniTacacsPlusClientHostAuthReplies_Object=MibTableColumn
juniTacacsPlusClientHostAuthReplies=_JuniTacacsPlusClientHostAuthReplies_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,2),_JuniTacacsPlusClientHostAuthReplies_Type())
juniTacacsPlusClientHostAuthReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthReplies.setStatus(_B)
_JuniTacacsPlusClientHostAuthPending_Type=Counter32
_JuniTacacsPlusClientHostAuthPending_Object=MibTableColumn
juniTacacsPlusClientHostAuthPending=_JuniTacacsPlusClientHostAuthPending_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,3),_JuniTacacsPlusClientHostAuthPending_Type())
juniTacacsPlusClientHostAuthPending.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthPending.setStatus(_B)
_JuniTacacsPlusClientHostAuthTimeouts_Type=Counter32
_JuniTacacsPlusClientHostAuthTimeouts_Object=MibTableColumn
juniTacacsPlusClientHostAuthTimeouts=_JuniTacacsPlusClientHostAuthTimeouts_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,4),_JuniTacacsPlusClientHostAuthTimeouts_Type())
juniTacacsPlusClientHostAuthTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthTimeouts.setStatus(_B)
_JuniTacacsPlusClientHostAuthorRequests_Type=Counter32
_JuniTacacsPlusClientHostAuthorRequests_Object=MibTableColumn
juniTacacsPlusClientHostAuthorRequests=_JuniTacacsPlusClientHostAuthorRequests_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,5),_JuniTacacsPlusClientHostAuthorRequests_Type())
juniTacacsPlusClientHostAuthorRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthorRequests.setStatus(_B)
_JuniTacacsPlusClientHostAuthorReplies_Type=Counter32
_JuniTacacsPlusClientHostAuthorReplies_Object=MibTableColumn
juniTacacsPlusClientHostAuthorReplies=_JuniTacacsPlusClientHostAuthorReplies_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,6),_JuniTacacsPlusClientHostAuthorReplies_Type())
juniTacacsPlusClientHostAuthorReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthorReplies.setStatus(_B)
_JuniTacacsPlusClientHostAuthorPending_Type=Counter32
_JuniTacacsPlusClientHostAuthorPending_Object=MibTableColumn
juniTacacsPlusClientHostAuthorPending=_JuniTacacsPlusClientHostAuthorPending_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,7),_JuniTacacsPlusClientHostAuthorPending_Type())
juniTacacsPlusClientHostAuthorPending.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthorPending.setStatus(_B)
_JuniTacacsPlusClientHostAuthorTimeouts_Type=Counter32
_JuniTacacsPlusClientHostAuthorTimeouts_Object=MibTableColumn
juniTacacsPlusClientHostAuthorTimeouts=_JuniTacacsPlusClientHostAuthorTimeouts_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,8),_JuniTacacsPlusClientHostAuthorTimeouts_Type())
juniTacacsPlusClientHostAuthorTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAuthorTimeouts.setStatus(_B)
_JuniTacacsPlusClientHostAcctRequests_Type=Counter32
_JuniTacacsPlusClientHostAcctRequests_Object=MibTableColumn
juniTacacsPlusClientHostAcctRequests=_JuniTacacsPlusClientHostAcctRequests_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,9),_JuniTacacsPlusClientHostAcctRequests_Type())
juniTacacsPlusClientHostAcctRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAcctRequests.setStatus(_B)
_JuniTacacsPlusClientHostAcctReplies_Type=Counter32
_JuniTacacsPlusClientHostAcctReplies_Object=MibTableColumn
juniTacacsPlusClientHostAcctReplies=_JuniTacacsPlusClientHostAcctReplies_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,10),_JuniTacacsPlusClientHostAcctReplies_Type())
juniTacacsPlusClientHostAcctReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAcctReplies.setStatus(_B)
_JuniTacacsPlusClientHostAcctPending_Type=Counter32
_JuniTacacsPlusClientHostAcctPending_Object=MibTableColumn
juniTacacsPlusClientHostAcctPending=_JuniTacacsPlusClientHostAcctPending_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,11),_JuniTacacsPlusClientHostAcctPending_Type())
juniTacacsPlusClientHostAcctPending.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAcctPending.setStatus(_B)
_JuniTacacsPlusClientHostAcctTimeouts_Type=Counter32
_JuniTacacsPlusClientHostAcctTimeouts_Object=MibTableColumn
juniTacacsPlusClientHostAcctTimeouts=_JuniTacacsPlusClientHostAcctTimeouts_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,12),_JuniTacacsPlusClientHostAcctTimeouts_Type())
juniTacacsPlusClientHostAcctTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostAcctTimeouts.setStatus(_B)
_JuniTacacsPlusClientHostDiscontinuityTime_Type=TimeStamp
_JuniTacacsPlusClientHostDiscontinuityTime_Object=MibTableColumn
juniTacacsPlusClientHostDiscontinuityTime=_JuniTacacsPlusClientHostDiscontinuityTime_Object((1,3,6,1,4,1,4874,2,2,60,1,3,1,1,13),_JuniTacacsPlusClientHostDiscontinuityTime_Type())
juniTacacsPlusClientHostDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniTacacsPlusClientHostDiscontinuityTime.setStatus(_B)
_JuniTacacsPlusClientConformance_ObjectIdentity=ObjectIdentity
juniTacacsPlusClientConformance=_JuniTacacsPlusClientConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,60,2))
_JuniTacacsPlusClientCompliances_ObjectIdentity=ObjectIdentity
juniTacacsPlusClientCompliances=_JuniTacacsPlusClientCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,60,2,1))
_JuniTacacsPlusClientGroups_ObjectIdentity=ObjectIdentity
juniTacacsPlusClientGroups=_JuniTacacsPlusClientGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,60,2,2))
juniTacacsPlusClientHostConfigEntry.registerAugmentions((_A,_R))
juniTacacsPlusClientHostStatsEntry.setIndexNames(*juniTacacsPlusClientHostConfigEntry.getIndexNames())
juniTacacsPlusClientCommonGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,60,2,2,1))
juniTacacsPlusClientCommonGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:juniTacacsPlusClientCommonGroup.setStatus(_B)
juniTacacsPlusClientHostConfigGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,60,2,2,2))
juniTacacsPlusClientHostConfigGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:juniTacacsPlusClientHostConfigGroup.setStatus(_W)
juniTacacsPlusClientHostStatsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,60,2,2,3))
juniTacacsPlusClientHostStatsGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:juniTacacsPlusClientHostStatsGroup.setStatus(_B)
juniTacacsPlusClientHostConfigGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,60,2,2,4))
juniTacacsPlusClientHostConfigGroup2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_k)))
if mibBuilder.loadTexts:juniTacacsPlusClientHostConfigGroup2.setStatus(_B)
juniTacacsPlusCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,60,2,1,1))
juniTacacsPlusCompliance.setObjects(*((_A,_N),(_A,_l),(_A,_O)))
if mibBuilder.loadTexts:juniTacacsPlusCompliance.setStatus(_W)
juniTacacsPlusCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,60,2,1,2))
juniTacacsPlusCompliance2.setObjects(*((_A,_N),(_A,_m),(_A,_O)))
if mibBuilder.loadTexts:juniTacacsPlusCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_Q:JuniKeyString,'juniTacacsPlusClientMIB':juniTacacsPlusClientMIB,'juniTacacsPlusClientObjects':juniTacacsPlusClientObjects,'juniTacacsPlusClientCommonConfig':juniTacacsPlusClientCommonConfig,_S:juniTacacsPlusClientDirectedRequest,_T:juniTacacsPlusClientTimeout,_U:juniTacacsPlusClientKey,_V:juniTacacsPlusClientSourceIp,'juniTacacsPlusClientHostConfig':juniTacacsPlusClientHostConfig,'juniTacacsPlusClientHostConfigTable':juniTacacsPlusClientHostConfigTable,'juniTacacsPlusClientHostConfigEntry':juniTacacsPlusClientHostConfigEntry,_P:juniTacacsPlusClientHostAddr,_H:juniTacacsPlusClientHostPort,_I:juniTacacsPlusClientHostPrimary,_J:juniTacacsPlusClientHostSingleConnection,_K:juniTacacsPlusClientHostTimeout,_L:juniTacacsPlusClientHostKey,_M:juniTacacsPlusClientHostStatus,_k:juniTacacsPlusClientHostOrder,'juniTacacsPlusClientHostStats':juniTacacsPlusClientHostStats,'juniTacacsPlusClientHostStatsTable':juniTacacsPlusClientHostStatsTable,_R:juniTacacsPlusClientHostStatsEntry,_X:juniTacacsPlusClientHostAuthRequests,_Y:juniTacacsPlusClientHostAuthReplies,_Z:juniTacacsPlusClientHostAuthPending,_a:juniTacacsPlusClientHostAuthTimeouts,_b:juniTacacsPlusClientHostAuthorRequests,_c:juniTacacsPlusClientHostAuthorReplies,_d:juniTacacsPlusClientHostAuthorPending,_e:juniTacacsPlusClientHostAuthorTimeouts,_f:juniTacacsPlusClientHostAcctRequests,_g:juniTacacsPlusClientHostAcctReplies,_h:juniTacacsPlusClientHostAcctPending,_i:juniTacacsPlusClientHostAcctTimeouts,_j:juniTacacsPlusClientHostDiscontinuityTime,'juniTacacsPlusClientConformance':juniTacacsPlusClientConformance,'juniTacacsPlusClientCompliances':juniTacacsPlusClientCompliances,'juniTacacsPlusCompliance':juniTacacsPlusCompliance,'juniTacacsPlusCompliance2':juniTacacsPlusCompliance2,'juniTacacsPlusClientGroups':juniTacacsPlusClientGroups,_N:juniTacacsPlusClientCommonGroup,_l:juniTacacsPlusClientHostConfigGroup,_O:juniTacacsPlusClientHostStatsGroup,_m:juniTacacsPlusClientHostConfigGroup2})