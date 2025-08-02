_X='alvarionDeviceDot1xStatsMIBGroup'
_W='alvarionDeviceDot1xStatusMIBGroup'
_V='coDev1xStaBackendAuthFails'
_U='coDev1xStaBackendAuthSuccesses'
_T='coDev1xStaBackendChallenges'
_S='coDev1xStaBackendResponses'
_R='coDev1xStaEapolTxFrame'
_Q='coDev1xStaEapolRxFrame'
_P='coDev1xStaTerminateCause'
_O='coDev1xStaSessionTime'
_N='coDev1xStaPortStatus'
_M='coDev1xStaBackendAuthState'
_L='coDev1xStaPaeState'
_K='coDev1xStaUserName'
_J='coDev1xStaMacAddress'
_I='coDeviceDot1xStatsEntry'
_H='initialize'
_G='coDev1xStaIndex'
_F='coDevDisIndex'
_E='ALVARION-DEVICE-MIB'
_D='Integer32'
_C='read-only'
_B='ALVARION-DEVICE-DOT1X-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
coDevDisIndex,=mibBuilder.importSymbols(_E,_F)
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
alvarionDeviceDot1xMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,32))
_AlvarionDeviceDot1xMIBObjects_ObjectIdentity=ObjectIdentity
alvarionDeviceDot1xMIBObjects=_AlvarionDeviceDot1xMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,32,1))
_CoDeviceDot1xConfigGroup_ObjectIdentity=ObjectIdentity
coDeviceDot1xConfigGroup=_CoDeviceDot1xConfigGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,32,1,1))
_CoDeviceDot1xStatusGroup_ObjectIdentity=ObjectIdentity
coDeviceDot1xStatusGroup=_CoDeviceDot1xStatusGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,32,1,2))
_CoDeviceDot1xStatusTable_Object=MibTable
coDeviceDot1xStatusTable=_CoDeviceDot1xStatusTable_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1))
if mibBuilder.loadTexts:coDeviceDot1xStatusTable.setStatus(_A)
_CoDeviceDot1xStatusEntry_Object=MibTableRow
coDeviceDot1xStatusEntry=_CoDeviceDot1xStatusEntry_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1))
coDeviceDot1xStatusEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:coDeviceDot1xStatusEntry.setStatus(_A)
class _CoDev1xStaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDev1xStaIndex_Type.__name__=_D
_CoDev1xStaIndex_Object=MibTableColumn
coDev1xStaIndex=_CoDev1xStaIndex_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,1),_CoDev1xStaIndex_Type())
coDev1xStaIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coDev1xStaIndex.setStatus(_A)
_CoDev1xStaMacAddress_Type=MacAddress
_CoDev1xStaMacAddress_Object=MibTableColumn
coDev1xStaMacAddress=_CoDev1xStaMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,2),_CoDev1xStaMacAddress_Type())
coDev1xStaMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaMacAddress.setStatus(_A)
_CoDev1xStaUserName_Type=DisplayString
_CoDev1xStaUserName_Object=MibTableColumn
coDev1xStaUserName=_CoDev1xStaUserName_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,3),_CoDev1xStaUserName_Type())
coDev1xStaUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaUserName.setStatus(_A)
class _CoDev1xStaPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_CoDev1xStaPaeState_Type.__name__=_D
_CoDev1xStaPaeState_Object=MibTableColumn
coDev1xStaPaeState=_CoDev1xStaPaeState_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,4),_CoDev1xStaPaeState_Type())
coDev1xStaPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaPaeState.setStatus(_A)
class _CoDev1xStaBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_H,7)))
_CoDev1xStaBackendAuthState_Type.__name__=_D
_CoDev1xStaBackendAuthState_Object=MibTableColumn
coDev1xStaBackendAuthState=_CoDev1xStaBackendAuthState_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,5),_CoDev1xStaBackendAuthState_Type())
coDev1xStaBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaBackendAuthState.setStatus(_A)
class _CoDev1xStaPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2)))
_CoDev1xStaPortStatus_Type.__name__=_D
_CoDev1xStaPortStatus_Object=MibTableColumn
coDev1xStaPortStatus=_CoDev1xStaPortStatus_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,6),_CoDev1xStaPortStatus_Type())
coDev1xStaPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaPortStatus.setStatus(_A)
_CoDev1xStaSessionTime_Type=Counter32
_CoDev1xStaSessionTime_Object=MibTableColumn
coDev1xStaSessionTime=_CoDev1xStaSessionTime_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,7),_CoDev1xStaSessionTime_Type())
coDev1xStaSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaSessionTime.setStatus(_A)
if mibBuilder.loadTexts:coDev1xStaSessionTime.setUnits('seconds')
class _CoDev1xStaTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*(('supplicantLogoff',1),('portFailure',2),('supplicantRestart',3),('reauthFailed',4),('authControlForceUnauth',5),('portReInit',6),('portAdminDisabled',7),('notTerminatedYet',999)))
_CoDev1xStaTerminateCause_Type.__name__=_D
_CoDev1xStaTerminateCause_Object=MibTableColumn
coDev1xStaTerminateCause=_CoDev1xStaTerminateCause_Object((1,3,6,1,4,1,12394,1,10,5,32,1,2,1,1,8),_CoDev1xStaTerminateCause_Type())
coDev1xStaTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaTerminateCause.setStatus(_A)
_CoDeviceDot1xStatsGroup_ObjectIdentity=ObjectIdentity
coDeviceDot1xStatsGroup=_CoDeviceDot1xStatsGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,32,1,3))
_CoDeviceDot1xStatsTable_Object=MibTable
coDeviceDot1xStatsTable=_CoDeviceDot1xStatsTable_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1))
if mibBuilder.loadTexts:coDeviceDot1xStatsTable.setStatus(_A)
_CoDeviceDot1xStatsEntry_Object=MibTableRow
coDeviceDot1xStatsEntry=_CoDeviceDot1xStatsEntry_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1,1))
if mibBuilder.loadTexts:coDeviceDot1xStatsEntry.setStatus(_A)
_CoDev1xStaEapolRxFrame_Type=Counter32
_CoDev1xStaEapolRxFrame_Object=MibTableColumn
coDev1xStaEapolRxFrame=_CoDev1xStaEapolRxFrame_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1,1,1),_CoDev1xStaEapolRxFrame_Type())
coDev1xStaEapolRxFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaEapolRxFrame.setStatus(_A)
_CoDev1xStaEapolTxFrame_Type=Counter32
_CoDev1xStaEapolTxFrame_Object=MibTableColumn
coDev1xStaEapolTxFrame=_CoDev1xStaEapolTxFrame_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1,1,2),_CoDev1xStaEapolTxFrame_Type())
coDev1xStaEapolTxFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaEapolTxFrame.setStatus(_A)
_CoDev1xStaBackendResponses_Type=Counter32
_CoDev1xStaBackendResponses_Object=MibTableColumn
coDev1xStaBackendResponses=_CoDev1xStaBackendResponses_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1,1,3),_CoDev1xStaBackendResponses_Type())
coDev1xStaBackendResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaBackendResponses.setStatus(_A)
_CoDev1xStaBackendChallenges_Type=Counter32
_CoDev1xStaBackendChallenges_Object=MibTableColumn
coDev1xStaBackendChallenges=_CoDev1xStaBackendChallenges_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1,1,4),_CoDev1xStaBackendChallenges_Type())
coDev1xStaBackendChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaBackendChallenges.setStatus(_A)
_CoDev1xStaBackendAuthSuccesses_Type=Counter32
_CoDev1xStaBackendAuthSuccesses_Object=MibTableColumn
coDev1xStaBackendAuthSuccesses=_CoDev1xStaBackendAuthSuccesses_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1,1,5),_CoDev1xStaBackendAuthSuccesses_Type())
coDev1xStaBackendAuthSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaBackendAuthSuccesses.setStatus(_A)
_CoDev1xStaBackendAuthFails_Type=Counter32
_CoDev1xStaBackendAuthFails_Object=MibTableColumn
coDev1xStaBackendAuthFails=_CoDev1xStaBackendAuthFails_Object((1,3,6,1,4,1,12394,1,10,5,32,1,3,1,1,6),_CoDev1xStaBackendAuthFails_Type())
coDev1xStaBackendAuthFails.setMaxAccess(_C)
if mibBuilder.loadTexts:coDev1xStaBackendAuthFails.setStatus(_A)
_AlvarionDeviceDot1xMIBConformance_ObjectIdentity=ObjectIdentity
alvarionDeviceDot1xMIBConformance=_AlvarionDeviceDot1xMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,32,2))
_AlvarionDeviceDot1xMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionDeviceDot1xMIBCompliances=_AlvarionDeviceDot1xMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,32,2,1))
_AlvarionDeviceDot1xMIBGroups_ObjectIdentity=ObjectIdentity
alvarionDeviceDot1xMIBGroups=_AlvarionDeviceDot1xMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,32,2,2))
coDeviceDot1xStatusEntry.registerAugmentions((_B,_I))
coDeviceDot1xStatsEntry.setIndexNames(*coDeviceDot1xStatusEntry.getIndexNames())
alvarionDeviceDot1xStatusMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,32,2,2,1))
alvarionDeviceDot1xStatusMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:alvarionDeviceDot1xStatusMIBGroup.setStatus(_A)
alvarionDeviceDot1xStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,32,2,2,2))
alvarionDeviceDot1xStatsMIBGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:alvarionDeviceDot1xStatsMIBGroup.setStatus(_A)
alvarionDeviceDot1xMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,32,2,1,1))
alvarionDeviceDot1xMIBCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:alvarionDeviceDot1xMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionDeviceDot1xMIB':alvarionDeviceDot1xMIB,'alvarionDeviceDot1xMIBObjects':alvarionDeviceDot1xMIBObjects,'coDeviceDot1xConfigGroup':coDeviceDot1xConfigGroup,'coDeviceDot1xStatusGroup':coDeviceDot1xStatusGroup,'coDeviceDot1xStatusTable':coDeviceDot1xStatusTable,'coDeviceDot1xStatusEntry':coDeviceDot1xStatusEntry,_G:coDev1xStaIndex,_J:coDev1xStaMacAddress,_K:coDev1xStaUserName,_L:coDev1xStaPaeState,_M:coDev1xStaBackendAuthState,_N:coDev1xStaPortStatus,_O:coDev1xStaSessionTime,_P:coDev1xStaTerminateCause,'coDeviceDot1xStatsGroup':coDeviceDot1xStatsGroup,'coDeviceDot1xStatsTable':coDeviceDot1xStatsTable,_I:coDeviceDot1xStatsEntry,_Q:coDev1xStaEapolRxFrame,_R:coDev1xStaEapolTxFrame,_S:coDev1xStaBackendResponses,_T:coDev1xStaBackendChallenges,_U:coDev1xStaBackendAuthSuccesses,_V:coDev1xStaBackendAuthFails,'alvarionDeviceDot1xMIBConformance':alvarionDeviceDot1xMIBConformance,'alvarionDeviceDot1xMIBCompliances':alvarionDeviceDot1xMIBCompliances,'alvarionDeviceDot1xMIBCompliance':alvarionDeviceDot1xMIBCompliance,'alvarionDeviceDot1xMIBGroups':alvarionDeviceDot1xMIBGroups,_W:alvarionDeviceDot1xStatusMIBGroup,_X:alvarionDeviceDot1xStatsMIBGroup})