_n='sessionAccessGroup'
_m='sessionTrapsGroup'
_l='sessionActiveGroup'
_k='sessionConfigGroup'
_j='sessionAuthenticationTrap'
_i='sessionAuthFailure'
_h='sessionConsoleStatus'
_g='sessionXonXoffEnable'
_f='sessionCliCommandLogEnable'
_e='sessionLoginAttempt'
_d='sessionLoginTimeout'
_c='sessionReauthInterval'
_b='sessionRowStatus'
_a='sessionUserProfileName'
_Z='sessionUserWritePrivileges'
_Y='sessionUserReadPrivileges'
_X='sessionPhysicalPort'
_W='sessionDefaultPromptSysName'
_V='sessionDefaultPromptString'
_U='sessionInactivityTimerValue'
_T='sessionBannerFileName'
_S='sessionServiceType'
_R='telnet'
_Q='console'
_P='sessionUserIpAddress'
_O='sessionUserName'
_N='sessionAccessType'
_M='sessionIndex'
_L='ftp'
_K='http'
_J='sessionType'
_I='OctetString'
_H='disable'
_G='enable'
_F='DisplayString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ALCATEL-IND1-SESSION-MGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Sesmgr,switchMgtTraps=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Sesmgr','switchMgtTraps')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1SessionMgrMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,7,1))
_AlcatelIND1SessionMgrMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBObjects=_AlcatelIND1SessionMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,7,1,1))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBObjects.setStatus(_A)
_SessionMgr_ObjectIdentity=ObjectIdentity
sessionMgr=_SessionMgr_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1))
_SessionConfigTable_Object=MibTable
sessionConfigTable=_SessionConfigTable_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,1))
if mibBuilder.loadTexts:sessionConfigTable.setStatus(_A)
_SessionConfigEntry_Object=MibTableRow
sessionConfigEntry=_SessionConfigEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,1,1))
sessionConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:sessionConfigEntry.setStatus(_A)
class _SessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cli',1),(_K,2),(_L,3),('snmp',4)))
_SessionType_Type.__name__=_C
_SessionType_Object=MibTableColumn
sessionType=_SessionType_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,1,1,1),_SessionType_Type())
sessionType.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionType.setStatus(_A)
class _SessionBannerFileName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SessionBannerFileName_Type.__name__=_F
_SessionBannerFileName_Object=MibTableColumn
sessionBannerFileName=_SessionBannerFileName_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,1,1,2),_SessionBannerFileName_Type())
sessionBannerFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionBannerFileName.setStatus(_A)
class _SessionInactivityTimerValue_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,596523))
_SessionInactivityTimerValue_Type.__name__=_C
_SessionInactivityTimerValue_Object=MibTableColumn
sessionInactivityTimerValue=_SessionInactivityTimerValue_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,1,1,3),_SessionInactivityTimerValue_Type())
sessionInactivityTimerValue.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionInactivityTimerValue.setStatus(_A)
class _SessionDefaultPromptString_Type(DisplayString):defaultValue=OctetString('-> ');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_SessionDefaultPromptString_Type.__name__=_F
_SessionDefaultPromptString_Object=MibTableColumn
sessionDefaultPromptString=_SessionDefaultPromptString_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,1,1,4),_SessionDefaultPromptString_Type())
sessionDefaultPromptString.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionDefaultPromptString.setStatus(_A)
class _SessionDefaultPromptSysName_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SessionDefaultPromptSysName_Type.__name__=_C
_SessionDefaultPromptSysName_Object=MibTableColumn
sessionDefaultPromptSysName=_SessionDefaultPromptSysName_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,1,1,5),_SessionDefaultPromptSysName_Type())
sessionDefaultPromptSysName.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionDefaultPromptSysName.setStatus(_A)
_SessionActiveTable_Object=MibTable
sessionActiveTable=_SessionActiveTable_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2))
if mibBuilder.loadTexts:sessionActiveTable.setStatus(_A)
_SessionActiveEntry_Object=MibTableRow
sessionActiveEntry=_SessionActiveEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1))
sessionActiveEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:sessionActiveEntry.setStatus(_A)
class _SessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SessionIndex_Type.__name__=_C
_SessionIndex_Object=MibTableColumn
sessionIndex=_SessionIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,1),_SessionIndex_Type())
sessionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionIndex.setStatus(_A)
class _SessionAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_R,2),(_L,3),(_K,4),('ssh',5)))
_SessionAccessType_Type.__name__=_C
_SessionAccessType_Object=MibTableColumn
sessionAccessType=_SessionAccessType_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,2),_SessionAccessType_Type())
sessionAccessType.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionAccessType.setStatus(_A)
class _SessionPhysicalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notSignificant',0),('emp',1),('ni',2),('local',3)))
_SessionPhysicalPort_Type.__name__=_C
_SessionPhysicalPort_Object=MibTableColumn
sessionPhysicalPort=_SessionPhysicalPort_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,3),_SessionPhysicalPort_Type())
sessionPhysicalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionPhysicalPort.setStatus(_A)
class _SessionUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_SessionUserName_Type.__name__=_F
_SessionUserName_Object=MibTableColumn
sessionUserName=_SessionUserName_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,4),_SessionUserName_Type())
sessionUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserName.setStatus(_A)
class _SessionUserReadPrivileges_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SessionUserReadPrivileges_Type.__name__=_I
_SessionUserReadPrivileges_Object=MibTableColumn
sessionUserReadPrivileges=_SessionUserReadPrivileges_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,5),_SessionUserReadPrivileges_Type())
sessionUserReadPrivileges.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserReadPrivileges.setStatus(_A)
class _SessionUserWritePrivileges_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SessionUserWritePrivileges_Type.__name__=_I
_SessionUserWritePrivileges_Object=MibTableColumn
sessionUserWritePrivileges=_SessionUserWritePrivileges_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,6),_SessionUserWritePrivileges_Type())
sessionUserWritePrivileges.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserWritePrivileges.setStatus(_A)
class _SessionUserProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_SessionUserProfileName_Type.__name__=_F
_SessionUserProfileName_Object=MibTableColumn
sessionUserProfileName=_SessionUserProfileName_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,7),_SessionUserProfileName_Type())
sessionUserProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserProfileName.setStatus(_A)
_SessionUserIpAddress_Type=IpAddress
_SessionUserIpAddress_Object=MibTableColumn
sessionUserIpAddress=_SessionUserIpAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,8),_SessionUserIpAddress_Type())
sessionUserIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserIpAddress.setStatus(_A)
_SessionRowStatus_Type=RowStatus
_SessionRowStatus_Object=MibTableColumn
sessionRowStatus=_SessionRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,2,1,9),_SessionRowStatus_Type())
sessionRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:sessionRowStatus.setStatus(_A)
class _SessionLoginTimeout_Type(Integer32):defaultValue=55;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_SessionLoginTimeout_Type.__name__=_C
_SessionLoginTimeout_Object=MibScalar
sessionLoginTimeout=_SessionLoginTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,3),_SessionLoginTimeout_Type())
sessionLoginTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionLoginTimeout.setStatus(_A)
class _SessionLoginAttempt_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SessionLoginAttempt_Type.__name__=_C
_SessionLoginAttempt_Object=MibScalar
sessionLoginAttempt=_SessionLoginAttempt_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,4),_SessionLoginAttempt_Type())
sessionLoginAttempt.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionLoginAttempt.setStatus(_A)
class _SessionCliCommandLogEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SessionCliCommandLogEnable_Type.__name__=_C
_SessionCliCommandLogEnable_Object=MibScalar
sessionCliCommandLogEnable=_SessionCliCommandLogEnable_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,5),_SessionCliCommandLogEnable_Type())
sessionCliCommandLogEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionCliCommandLogEnable.setStatus(_A)
class _SessionXonXoffEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SessionXonXoffEnable_Type.__name__=_C
_SessionXonXoffEnable_Object=MibScalar
sessionXonXoffEnable=_SessionXonXoffEnable_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,6),_SessionXonXoffEnable_Type())
sessionXonXoffEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionXonXoffEnable.setStatus(_A)
_SessionAccessTable_Object=MibTable
sessionAccessTable=_SessionAccessTable_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,7))
if mibBuilder.loadTexts:sessionAccessTable.setStatus(_A)
_SessionAccessEntry_Object=MibTableRow
sessionAccessEntry=_SessionAccessEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,7,1))
sessionAccessEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:sessionAccessEntry.setStatus(_A)
class _SessionServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_R,2),(_L,3),(_K,4),('ssh',5),('https',6)))
_SessionServiceType_Type.__name__=_C
_SessionServiceType_Object=MibTableColumn
sessionServiceType=_SessionServiceType_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,7,1,1),_SessionServiceType_Type())
sessionServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionServiceType.setStatus(_A)
class _SessionReauthInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_SessionReauthInterval_Type.__name__=_C
_SessionReauthInterval_Object=MibTableColumn
sessionReauthInterval=_SessionReauthInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,7,1,2),_SessionReauthInterval_Type())
sessionReauthInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionReauthInterval.setStatus(_A)
if mibBuilder.loadTexts:sessionReauthInterval.setUnits('minutes')
class _SessionConsoleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SessionConsoleStatus_Type.__name__=_C
_SessionConsoleStatus_Object=MibScalar
sessionConsoleStatus=_SessionConsoleStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,8),_SessionConsoleStatus_Type())
sessionConsoleStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionConsoleStatus.setStatus(_A)
class _SessionCliAutoCompleteSpace_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SessionCliAutoCompleteSpace_Type.__name__=_C
_SessionCliAutoCompleteSpace_Object=MibScalar
sessionCliAutoCompleteSpace=_SessionCliAutoCompleteSpace_Object((1,3,6,1,4,1,6486,800,1,2,1,7,1,1,1,9),_SessionCliAutoCompleteSpace_Type())
sessionCliAutoCompleteSpace.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionCliAutoCompleteSpace.setStatus(_A)
_AlcatelIND1SessionMgrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBConformance=_AlcatelIND1SessionMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,7,1,2))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBConformance.setStatus(_A)
_AlcatelIND1SessionMgrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBGroups=_AlcatelIND1SessionMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,1))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBGroups.setStatus(_A)
_AlcatelIND1SessionMgrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBCompliances=_AlcatelIND1SessionMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,2))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBCompliances.setStatus(_A)
_SwitchMgtTrapsDesc_ObjectIdentity=ObjectIdentity
switchMgtTrapsDesc=_SwitchMgtTrapsDesc_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,11,1))
_SwitchMgtTrapsObj_ObjectIdentity=ObjectIdentity
switchMgtTrapsObj=_SwitchMgtTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,11,2))
class _SessionAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('unknownUser',1))
_SessionAuthFailure_Type.__name__=_C
_SessionAuthFailure_Object=MibScalar
sessionAuthFailure=_SessionAuthFailure_Object((1,3,6,1,4,1,6486,800,1,3,2,11,2,1),_SessionAuthFailure_Type())
sessionAuthFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionAuthFailure.setStatus(_A)
sessionConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,1,1))
sessionConfigGroup.setObjects(*((_B,_J),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:sessionConfigGroup.setStatus(_A)
sessionActiveGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,1,2))
sessionActiveGroup.setObjects(*((_B,_M),(_B,_N),(_B,_X),(_B,_O),(_B,_Y),(_B,_Z),(_B,_a),(_B,_P),(_B,_b)))
if mibBuilder.loadTexts:sessionActiveGroup.setStatus(_A)
sessionAccessGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,1,4))
sessionAccessGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:sessionAccessGroup.setStatus(_A)
sessionMgrGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,1,5))
sessionMgrGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:sessionMgrGroup.setStatus(_A)
sessionAuthenticationTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,11,1,0,1))
sessionAuthenticationTrap.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_i)))
if mibBuilder.loadTexts:sessionAuthenticationTrap.setStatus(_A)
sessionTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,1,3))
sessionTrapsGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:sessionTrapsGroup.setStatus(_A)
alcatelIND1SessionMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,7,1,2,2,1))
alcatelIND1SessionMgrMIBCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1SessionMgrMIB':alcatelIND1SessionMgrMIB,'alcatelIND1SessionMgrMIBObjects':alcatelIND1SessionMgrMIBObjects,'sessionMgr':sessionMgr,'sessionConfigTable':sessionConfigTable,'sessionConfigEntry':sessionConfigEntry,_J:sessionType,_T:sessionBannerFileName,_U:sessionInactivityTimerValue,_V:sessionDefaultPromptString,_W:sessionDefaultPromptSysName,'sessionActiveTable':sessionActiveTable,'sessionActiveEntry':sessionActiveEntry,_M:sessionIndex,_N:sessionAccessType,_X:sessionPhysicalPort,_O:sessionUserName,_Y:sessionUserReadPrivileges,_Z:sessionUserWritePrivileges,_a:sessionUserProfileName,_P:sessionUserIpAddress,_b:sessionRowStatus,_d:sessionLoginTimeout,_e:sessionLoginAttempt,_f:sessionCliCommandLogEnable,_g:sessionXonXoffEnable,'sessionAccessTable':sessionAccessTable,'sessionAccessEntry':sessionAccessEntry,_S:sessionServiceType,_c:sessionReauthInterval,_h:sessionConsoleStatus,'sessionCliAutoCompleteSpace':sessionCliAutoCompleteSpace,'alcatelIND1SessionMgrMIBConformance':alcatelIND1SessionMgrMIBConformance,'alcatelIND1SessionMgrMIBGroups':alcatelIND1SessionMgrMIBGroups,_k:sessionConfigGroup,_l:sessionActiveGroup,_m:sessionTrapsGroup,_n:sessionAccessGroup,'sessionMgrGroup':sessionMgrGroup,'alcatelIND1SessionMgrMIBCompliances':alcatelIND1SessionMgrMIBCompliances,'alcatelIND1SessionMgrMIBCompliance':alcatelIND1SessionMgrMIBCompliance,'switchMgtTrapsDesc':switchMgtTrapsDesc,_j:sessionAuthenticationTrap,'switchMgtTrapsObj':switchMgtTrapsObj,_i:sessionAuthFailure})