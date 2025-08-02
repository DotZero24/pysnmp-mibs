_i='cfcspNotificationGroup'
_h='cfcspIfStatsGroup'
_g='cfcspLocalPasswdGroup'
_f='cfcspConfigGroup'
_e='cfcspAuthFailNotification'
_d='cfcspIfAuthByPassed'
_c='cfcspIfAuthFailed'
_b='cfcspIfAuthSucceeded'
_a='cfcspRemotePassRowStatus'
_Z='cfcspRemotePasswd'
_Y='cfcspLocalPassRowStatus'
_X='cfcspLocalPasswd'
_W='cfcspDhChapGenericPasswd'
_V='cfcspDhChapGroupList'
_U='cfcspDhChapHashList'
_T='cfcspTimeout'
_S='cfcspAuthProtocols'
_R='cfcspReauthenticate'
_Q='cfcspReauthInterval'
_P='cfcspMode'
_O='cfcspRemoteSwitchWwn'
_N='not-accessible'
_M='cfcspSwitchWwn'
_L='ifDescr'
_K='read-only'
_J='Unsigned32'
_I='ifIndex'
_H='OctetString'
_G='read-create'
_F='Integer32'
_E='SnmpAdminString'
_D='IF-MIB'
_C='read-write'
_B='CISCO-FCSP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,=mibBuilder.importSymbols('CISCO-ST-TC','FcNameId')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_L,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoFcspMIB=ModuleIdentity((1,3,6,1,4,1,9,9,391))
if mibBuilder.loadTexts:ciscoFcspMIB.setRevisions(('2004-07-02 00:00',))
_CiscoFcspMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoFcspMIBNotifications=_CiscoFcspMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,391,0))
_CiscoFcspMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcspMIBObjects=_CiscoFcspMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,391,1))
_CfcspConfig_ObjectIdentity=ObjectIdentity
cfcspConfig=_CfcspConfig_ObjectIdentity((1,3,6,1,4,1,9,9,391,1,1))
_CfcspIfTable_Object=MibTable
cfcspIfTable=_CfcspIfTable_Object((1,3,6,1,4,1,9,9,391,1,1,1))
if mibBuilder.loadTexts:cfcspIfTable.setStatus(_A)
_CfcspIfEntry_Object=MibTableRow
cfcspIfEntry=_CfcspIfEntry_Object((1,3,6,1,4,1,9,9,391,1,1,1,1))
cfcspIfEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:cfcspIfEntry.setStatus(_A)
class _CfcspMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('autoPassive',2),('autoActive',3),('on',4)))
_CfcspMode_Type.__name__=_F
_CfcspMode_Object=MibTableColumn
cfcspMode=_CfcspMode_Object((1,3,6,1,4,1,9,9,391,1,1,1,1,1),_CfcspMode_Type())
cfcspMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspMode.setStatus(_A)
class _CfcspReauthInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CfcspReauthInterval_Type.__name__=_J
_CfcspReauthInterval_Object=MibTableColumn
cfcspReauthInterval=_CfcspReauthInterval_Object((1,3,6,1,4,1,9,9,391,1,1,1,1,2),_CfcspReauthInterval_Type())
cfcspReauthInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspReauthInterval.setStatus(_A)
if mibBuilder.loadTexts:cfcspReauthInterval.setUnits('minutes')
class _CfcspReauthenticate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('noOp',2)))
_CfcspReauthenticate_Type.__name__=_F
_CfcspReauthenticate_Object=MibTableColumn
cfcspReauthenticate=_CfcspReauthenticate_Object((1,3,6,1,4,1,9,9,391,1,1,1,1,3),_CfcspReauthenticate_Type())
cfcspReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspReauthenticate.setStatus(_A)
class _CfcspAuthProtocols_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dhChap',0),('fcCap',1)))
_CfcspAuthProtocols_Type.__name__=_F
_CfcspAuthProtocols_Object=MibScalar
cfcspAuthProtocols=_CfcspAuthProtocols_Object((1,3,6,1,4,1,9,9,391,1,1,2),_CfcspAuthProtocols_Type())
cfcspAuthProtocols.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspAuthProtocols.setStatus(_A)
class _CfcspTimeout_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1000))
_CfcspTimeout_Type.__name__=_J
_CfcspTimeout_Object=MibScalar
cfcspTimeout=_CfcspTimeout_Object((1,3,6,1,4,1,9,9,391,1,1,3),_CfcspTimeout_Type())
cfcspTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspTimeout.setStatus(_A)
if mibBuilder.loadTexts:cfcspTimeout.setUnits('seconds')
_CfcspDhChapObjects_ObjectIdentity=ObjectIdentity
cfcspDhChapObjects=_CfcspDhChapObjects_ObjectIdentity((1,3,6,1,4,1,9,9,391,1,1,4))
class _CfcspDhChapHashList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CfcspDhChapHashList_Type.__name__=_H
_CfcspDhChapHashList_Object=MibScalar
cfcspDhChapHashList=_CfcspDhChapHashList_Object((1,3,6,1,4,1,9,9,391,1,1,4,1),_CfcspDhChapHashList_Type())
cfcspDhChapHashList.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspDhChapHashList.setStatus(_A)
class _CfcspDhChapGroupList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_CfcspDhChapGroupList_Type.__name__=_H
_CfcspDhChapGroupList_Object=MibScalar
cfcspDhChapGroupList=_CfcspDhChapGroupList_Object((1,3,6,1,4,1,9,9,391,1,1,4,2),_CfcspDhChapGroupList_Type())
cfcspDhChapGroupList.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspDhChapGroupList.setStatus(_A)
class _CfcspDhChapGenericPasswd_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CfcspDhChapGenericPasswd_Type.__name__=_E
_CfcspDhChapGenericPasswd_Object=MibScalar
cfcspDhChapGenericPasswd=_CfcspDhChapGenericPasswd_Object((1,3,6,1,4,1,9,9,391,1,1,4,3),_CfcspDhChapGenericPasswd_Type())
cfcspDhChapGenericPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcspDhChapGenericPasswd.setStatus(_A)
_CfcspLocalPasswdTable_Object=MibTable
cfcspLocalPasswdTable=_CfcspLocalPasswdTable_Object((1,3,6,1,4,1,9,9,391,1,1,5))
if mibBuilder.loadTexts:cfcspLocalPasswdTable.setStatus(_A)
_CfcspLocalPasswdEntry_Object=MibTableRow
cfcspLocalPasswdEntry=_CfcspLocalPasswdEntry_Object((1,3,6,1,4,1,9,9,391,1,1,5,1))
cfcspLocalPasswdEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cfcspLocalPasswdEntry.setStatus(_A)
_CfcspSwitchWwn_Type=FcNameId
_CfcspSwitchWwn_Object=MibTableColumn
cfcspSwitchWwn=_CfcspSwitchWwn_Object((1,3,6,1,4,1,9,9,391,1,1,5,1,1),_CfcspSwitchWwn_Type())
cfcspSwitchWwn.setMaxAccess(_N)
if mibBuilder.loadTexts:cfcspSwitchWwn.setStatus(_A)
class _CfcspLocalPasswd_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CfcspLocalPasswd_Type.__name__=_E
_CfcspLocalPasswd_Object=MibTableColumn
cfcspLocalPasswd=_CfcspLocalPasswd_Object((1,3,6,1,4,1,9,9,391,1,1,5,1,2),_CfcspLocalPasswd_Type())
cfcspLocalPasswd.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcspLocalPasswd.setStatus(_A)
_CfcspLocalPassRowStatus_Type=RowStatus
_CfcspLocalPassRowStatus_Object=MibTableColumn
cfcspLocalPassRowStatus=_CfcspLocalPassRowStatus_Object((1,3,6,1,4,1,9,9,391,1,1,5,1,3),_CfcspLocalPassRowStatus_Type())
cfcspLocalPassRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcspLocalPassRowStatus.setStatus(_A)
_CfcspRemotePasswdTable_Object=MibTable
cfcspRemotePasswdTable=_CfcspRemotePasswdTable_Object((1,3,6,1,4,1,9,9,391,1,1,6))
if mibBuilder.loadTexts:cfcspRemotePasswdTable.setStatus(_A)
_CfcspRemotePasswdEntry_Object=MibTableRow
cfcspRemotePasswdEntry=_CfcspRemotePasswdEntry_Object((1,3,6,1,4,1,9,9,391,1,1,6,1))
cfcspRemotePasswdEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cfcspRemotePasswdEntry.setStatus(_A)
_CfcspRemoteSwitchWwn_Type=FcNameId
_CfcspRemoteSwitchWwn_Object=MibTableColumn
cfcspRemoteSwitchWwn=_CfcspRemoteSwitchWwn_Object((1,3,6,1,4,1,9,9,391,1,1,6,1,1),_CfcspRemoteSwitchWwn_Type())
cfcspRemoteSwitchWwn.setMaxAccess(_N)
if mibBuilder.loadTexts:cfcspRemoteSwitchWwn.setStatus(_A)
class _CfcspRemotePasswd_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CfcspRemotePasswd_Type.__name__=_E
_CfcspRemotePasswd_Object=MibTableColumn
cfcspRemotePasswd=_CfcspRemotePasswd_Object((1,3,6,1,4,1,9,9,391,1,1,6,1,2),_CfcspRemotePasswd_Type())
cfcspRemotePasswd.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcspRemotePasswd.setStatus(_A)
_CfcspRemotePassRowStatus_Type=RowStatus
_CfcspRemotePassRowStatus_Object=MibTableColumn
cfcspRemotePassRowStatus=_CfcspRemotePassRowStatus_Object((1,3,6,1,4,1,9,9,391,1,1,6,1,3),_CfcspRemotePassRowStatus_Type())
cfcspRemotePassRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcspRemotePassRowStatus.setStatus(_A)
_CfcspInfo_ObjectIdentity=ObjectIdentity
cfcspInfo=_CfcspInfo_ObjectIdentity((1,3,6,1,4,1,9,9,391,1,2))
_CfcspStatistics_ObjectIdentity=ObjectIdentity
cfcspStatistics=_CfcspStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,391,1,3))
_CfcspIfStatsTable_Object=MibTable
cfcspIfStatsTable=_CfcspIfStatsTable_Object((1,3,6,1,4,1,9,9,391,1,3,1))
if mibBuilder.loadTexts:cfcspIfStatsTable.setStatus(_A)
_CfcspIfStatsEntry_Object=MibTableRow
cfcspIfStatsEntry=_CfcspIfStatsEntry_Object((1,3,6,1,4,1,9,9,391,1,3,1,1))
cfcspIfStatsEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:cfcspIfStatsEntry.setStatus(_A)
_CfcspIfAuthSucceeded_Type=Counter32
_CfcspIfAuthSucceeded_Object=MibTableColumn
cfcspIfAuthSucceeded=_CfcspIfAuthSucceeded_Object((1,3,6,1,4,1,9,9,391,1,3,1,1,1),_CfcspIfAuthSucceeded_Type())
cfcspIfAuthSucceeded.setMaxAccess(_K)
if mibBuilder.loadTexts:cfcspIfAuthSucceeded.setStatus(_A)
_CfcspIfAuthFailed_Type=Counter32
_CfcspIfAuthFailed_Object=MibTableColumn
cfcspIfAuthFailed=_CfcspIfAuthFailed_Object((1,3,6,1,4,1,9,9,391,1,3,1,1,2),_CfcspIfAuthFailed_Type())
cfcspIfAuthFailed.setMaxAccess(_K)
if mibBuilder.loadTexts:cfcspIfAuthFailed.setStatus(_A)
_CfcspIfAuthByPassed_Type=Counter32
_CfcspIfAuthByPassed_Object=MibTableColumn
cfcspIfAuthByPassed=_CfcspIfAuthByPassed_Object((1,3,6,1,4,1,9,9,391,1,3,1,1,3),_CfcspIfAuthByPassed_Type())
cfcspIfAuthByPassed.setMaxAccess(_K)
if mibBuilder.loadTexts:cfcspIfAuthByPassed.setStatus(_A)
_CfcspNotificationObjects_ObjectIdentity=ObjectIdentity
cfcspNotificationObjects=_CfcspNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9,9,391,1,4))
_CiscoFcspMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFcspMIBConformance=_CiscoFcspMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,391,2))
_CiscoFcspMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFcspMIBCompliances=_CiscoFcspMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,391,2,1))
_CiscoFcspMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFcspMIBGroups=_CiscoFcspMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,391,2,2))
cfcspConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,391,2,2,1))
cfcspConfigGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cfcspConfigGroup.setStatus(_A)
cfcspLocalPasswdGroup=ObjectGroup((1,3,6,1,4,1,9,9,391,2,2,2))
cfcspLocalPasswdGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cfcspLocalPasswdGroup.setStatus(_A)
cfcspIfStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,391,2,2,3))
cfcspIfStatsGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:cfcspIfStatsGroup.setStatus(_A)
cfcspAuthFailNotification=NotificationType((1,3,6,1,4,1,9,9,391,0,1))
cfcspAuthFailNotification.setObjects((_D,_L))
if mibBuilder.loadTexts:cfcspAuthFailNotification.setStatus(_A)
cfcspNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,391,2,2,4))
cfcspNotificationGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:cfcspNotificationGroup.setStatus(_A)
ciscoFcspMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,391,2,1,1))
ciscoFcspMIBCompliance.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ciscoFcspMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFcspMIB':ciscoFcspMIB,'ciscoFcspMIBNotifications':ciscoFcspMIBNotifications,_e:cfcspAuthFailNotification,'ciscoFcspMIBObjects':ciscoFcspMIBObjects,'cfcspConfig':cfcspConfig,'cfcspIfTable':cfcspIfTable,'cfcspIfEntry':cfcspIfEntry,_P:cfcspMode,_Q:cfcspReauthInterval,_R:cfcspReauthenticate,_S:cfcspAuthProtocols,_T:cfcspTimeout,'cfcspDhChapObjects':cfcspDhChapObjects,_U:cfcspDhChapHashList,_V:cfcspDhChapGroupList,_W:cfcspDhChapGenericPasswd,'cfcspLocalPasswdTable':cfcspLocalPasswdTable,'cfcspLocalPasswdEntry':cfcspLocalPasswdEntry,_M:cfcspSwitchWwn,_X:cfcspLocalPasswd,_Y:cfcspLocalPassRowStatus,'cfcspRemotePasswdTable':cfcspRemotePasswdTable,'cfcspRemotePasswdEntry':cfcspRemotePasswdEntry,_O:cfcspRemoteSwitchWwn,_Z:cfcspRemotePasswd,_a:cfcspRemotePassRowStatus,'cfcspInfo':cfcspInfo,'cfcspStatistics':cfcspStatistics,'cfcspIfStatsTable':cfcspIfStatsTable,'cfcspIfStatsEntry':cfcspIfStatsEntry,_b:cfcspIfAuthSucceeded,_c:cfcspIfAuthFailed,_d:cfcspIfAuthByPassed,'cfcspNotificationObjects':cfcspNotificationObjects,'ciscoFcspMIBConformance':ciscoFcspMIBConformance,'ciscoFcspMIBCompliances':ciscoFcspMIBCompliances,'ciscoFcspMIBCompliance':ciscoFcspMIBCompliance,'ciscoFcspMIBGroups':ciscoFcspMIBGroups,_f:cfcspConfigGroup,_g:cfcspLocalPasswdGroup,_h:cfcspIfStatsGroup,_i:cfcspNotificationGroup})