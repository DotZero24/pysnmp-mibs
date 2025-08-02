_f='sessionTrapsGroup'
_e='sessionObjectGroup'
_d='sessionActiveGroup'
_c='sessionConfigGroup'
_b='sessionAuthenticationTrap'
_a='sessionXonXoffEnable'
_Z='sessionCliCommandLogEnable'
_Y='sessionLoginAttempt'
_X='sessionLoginTimeout'
_W='sessionRowStatus'
_V='sessionUserProfileName'
_U='sessionUserWritePrivileges'
_T='sessionUserReadPrivileges'
_S='sessionPhysicalPort'
_R='sessionDefaultPromptString'
_Q='sessionInactivityTimerValue'
_P='sessionBannerFileName'
_O='disable'
_N='enable'
_M='sessionAuthFailure'
_L='sessionUserIpAddress'
_K='sessionUserName'
_J='sessionAccessType'
_I='sessionIndex'
_H='sessionType'
_G='OctetString'
_F='SnmpAdminString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ALCATEL-ENT1-SESSION-MGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Sesmgr,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Sesmgr')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1SessionMgrMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIB.setRevisions(('2010-05-13 00:00',))
_AlcatelIND1SessionMgrMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBNotifications=_AlcatelIND1SessionMgrMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1,0))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBNotifications.setStatus(_A)
_AlcatelIND1SessionMgrMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBObjects=_AlcatelIND1SessionMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1,1))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBObjects.setStatus(_A)
_SessionMgr_ObjectIdentity=ObjectIdentity
sessionMgr=_SessionMgr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1))
_SessionConfigTable_Object=MibTable
sessionConfigTable=_SessionConfigTable_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,1))
if mibBuilder.loadTexts:sessionConfigTable.setStatus(_A)
_SessionConfigEntry_Object=MibTableRow
sessionConfigEntry=_SessionConfigEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,1,1))
sessionConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:sessionConfigEntry.setStatus(_A)
class _SessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cli',1),('http',2),('ftp',3)))
_SessionType_Type.__name__=_C
_SessionType_Object=MibTableColumn
sessionType=_SessionType_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,1,1,1),_SessionType_Type())
sessionType.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionType.setStatus(_A)
class _SessionBannerFileName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SessionBannerFileName_Type.__name__=_F
_SessionBannerFileName_Object=MibTableColumn
sessionBannerFileName=_SessionBannerFileName_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,1,1,2),_SessionBannerFileName_Type())
sessionBannerFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionBannerFileName.setStatus(_A)
class _SessionInactivityTimerValue_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,596523))
_SessionInactivityTimerValue_Type.__name__=_C
_SessionInactivityTimerValue_Object=MibTableColumn
sessionInactivityTimerValue=_SessionInactivityTimerValue_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,1,1,3),_SessionInactivityTimerValue_Type())
sessionInactivityTimerValue.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionInactivityTimerValue.setStatus(_A)
class _SessionDefaultPromptString_Type(SnmpAdminString):defaultValue=OctetString('-> ');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_SessionDefaultPromptString_Type.__name__=_F
_SessionDefaultPromptString_Object=MibTableColumn
sessionDefaultPromptString=_SessionDefaultPromptString_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,1,1,4),_SessionDefaultPromptString_Type())
sessionDefaultPromptString.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionDefaultPromptString.setStatus(_A)
_SessionActiveTable_Object=MibTable
sessionActiveTable=_SessionActiveTable_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2))
if mibBuilder.loadTexts:sessionActiveTable.setStatus(_A)
_SessionActiveEntry_Object=MibTableRow
sessionActiveEntry=_SessionActiveEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1))
sessionActiveEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:sessionActiveEntry.setStatus(_A)
class _SessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SessionIndex_Type.__name__=_C
_SessionIndex_Object=MibTableColumn
sessionIndex=_SessionIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,1),_SessionIndex_Type())
sessionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionIndex.setStatus(_A)
class _SessionAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('console',1),('telnet',2),('ftp',3),('http',4),('ssh',5),('https',6)))
_SessionAccessType_Type.__name__=_C
_SessionAccessType_Object=MibTableColumn
sessionAccessType=_SessionAccessType_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,2),_SessionAccessType_Type())
sessionAccessType.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionAccessType.setStatus(_A)
class _SessionPhysicalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notSignificant',0),('local',1),('ether',2)))
_SessionPhysicalPort_Type.__name__=_C
_SessionPhysicalPort_Object=MibTableColumn
sessionPhysicalPort=_SessionPhysicalPort_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,3),_SessionPhysicalPort_Type())
sessionPhysicalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionPhysicalPort.setStatus(_A)
class _SessionUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_SessionUserName_Type.__name__=_F
_SessionUserName_Object=MibTableColumn
sessionUserName=_SessionUserName_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,4),_SessionUserName_Type())
sessionUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserName.setStatus(_A)
class _SessionUserReadPrivileges_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SessionUserReadPrivileges_Type.__name__=_G
_SessionUserReadPrivileges_Object=MibTableColumn
sessionUserReadPrivileges=_SessionUserReadPrivileges_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,5),_SessionUserReadPrivileges_Type())
sessionUserReadPrivileges.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserReadPrivileges.setStatus(_A)
class _SessionUserWritePrivileges_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SessionUserWritePrivileges_Type.__name__=_G
_SessionUserWritePrivileges_Object=MibTableColumn
sessionUserWritePrivileges=_SessionUserWritePrivileges_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,6),_SessionUserWritePrivileges_Type())
sessionUserWritePrivileges.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserWritePrivileges.setStatus(_A)
class _SessionUserProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_SessionUserProfileName_Type.__name__=_F
_SessionUserProfileName_Object=MibTableColumn
sessionUserProfileName=_SessionUserProfileName_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,7),_SessionUserProfileName_Type())
sessionUserProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserProfileName.setStatus('obsolete')
_SessionUserIpAddress_Type=IpAddress
_SessionUserIpAddress_Object=MibTableColumn
sessionUserIpAddress=_SessionUserIpAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,8),_SessionUserIpAddress_Type())
sessionUserIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionUserIpAddress.setStatus(_A)
_SessionRowStatus_Type=RowStatus
_SessionRowStatus_Object=MibTableColumn
sessionRowStatus=_SessionRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,2,1,9),_SessionRowStatus_Type())
sessionRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:sessionRowStatus.setStatus(_A)
class _SessionLoginTimeout_Type(Integer32):defaultValue=55;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_SessionLoginTimeout_Type.__name__=_C
_SessionLoginTimeout_Object=MibScalar
sessionLoginTimeout=_SessionLoginTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,3),_SessionLoginTimeout_Type())
sessionLoginTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionLoginTimeout.setStatus(_A)
class _SessionLoginAttempt_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SessionLoginAttempt_Type.__name__=_C
_SessionLoginAttempt_Object=MibScalar
sessionLoginAttempt=_SessionLoginAttempt_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,4),_SessionLoginAttempt_Type())
sessionLoginAttempt.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionLoginAttempt.setStatus(_A)
class _SessionCliCommandLogEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SessionCliCommandLogEnable_Type.__name__=_C
_SessionCliCommandLogEnable_Object=MibScalar
sessionCliCommandLogEnable=_SessionCliCommandLogEnable_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,5),_SessionCliCommandLogEnable_Type())
sessionCliCommandLogEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionCliCommandLogEnable.setStatus(_A)
class _SessionXonXoffEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SessionXonXoffEnable_Type.__name__=_C
_SessionXonXoffEnable_Object=MibScalar
sessionXonXoffEnable=_SessionXonXoffEnable_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,6),_SessionXonXoffEnable_Type())
sessionXonXoffEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionXonXoffEnable.setStatus(_A)
_SwitchMgtTrapsObj_ObjectIdentity=ObjectIdentity
switchMgtTrapsObj=_SwitchMgtTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,7))
class _SessionAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('unknownUser',1))
_SessionAuthFailure_Type.__name__=_C
_SessionAuthFailure_Object=MibScalar
sessionAuthFailure=_SessionAuthFailure_Object((1,3,6,1,4,1,6486,801,1,2,1,7,1,1,1,7,1),_SessionAuthFailure_Type())
sessionAuthFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:sessionAuthFailure.setStatus(_A)
_AlcatelIND1SessionMgrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBConformance=_AlcatelIND1SessionMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1,2))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBConformance.setStatus(_A)
_AlcatelIND1SessionMgrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBGroups=_AlcatelIND1SessionMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1,2,1))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBGroups.setStatus(_A)
_AlcatelIND1SessionMgrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1SessionMgrMIBCompliances=_AlcatelIND1SessionMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7,1,2,2))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBCompliances.setStatus(_A)
sessionConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,7,1,2,1,1))
sessionConfigGroup.setObjects(*((_B,_H),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:sessionConfigGroup.setStatus(_A)
sessionActiveGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,7,1,2,1,2))
sessionActiveGroup.setObjects(*((_B,_I),(_B,_J),(_B,_S),(_B,_K),(_B,_T),(_B,_U),(_B,_V),(_B,_L),(_B,_W)))
if mibBuilder.loadTexts:sessionActiveGroup.setStatus(_A)
sessionObjectGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,7,1,2,1,4))
sessionObjectGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_M)))
if mibBuilder.loadTexts:sessionObjectGroup.setStatus(_A)
sessionAuthenticationTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,7,1,0,1))
sessionAuthenticationTrap.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:sessionAuthenticationTrap.setStatus(_A)
sessionTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,7,1,2,1,3))
sessionTrapsGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:sessionTrapsGroup.setStatus(_A)
alcatelIND1SessionMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,7,1,2,2,1))
alcatelIND1SessionMgrMIBCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:alcatelIND1SessionMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1SessionMgrMIB':alcatelIND1SessionMgrMIB,'alcatelIND1SessionMgrMIBNotifications':alcatelIND1SessionMgrMIBNotifications,_b:sessionAuthenticationTrap,'alcatelIND1SessionMgrMIBObjects':alcatelIND1SessionMgrMIBObjects,'sessionMgr':sessionMgr,'sessionConfigTable':sessionConfigTable,'sessionConfigEntry':sessionConfigEntry,_H:sessionType,_P:sessionBannerFileName,_Q:sessionInactivityTimerValue,_R:sessionDefaultPromptString,'sessionActiveTable':sessionActiveTable,'sessionActiveEntry':sessionActiveEntry,_I:sessionIndex,_J:sessionAccessType,_S:sessionPhysicalPort,_K:sessionUserName,_T:sessionUserReadPrivileges,_U:sessionUserWritePrivileges,_V:sessionUserProfileName,_L:sessionUserIpAddress,_W:sessionRowStatus,_X:sessionLoginTimeout,_Y:sessionLoginAttempt,_Z:sessionCliCommandLogEnable,_a:sessionXonXoffEnable,'switchMgtTrapsObj':switchMgtTrapsObj,_M:sessionAuthFailure,'alcatelIND1SessionMgrMIBConformance':alcatelIND1SessionMgrMIBConformance,'alcatelIND1SessionMgrMIBGroups':alcatelIND1SessionMgrMIBGroups,_c:sessionConfigGroup,_d:sessionActiveGroup,_f:sessionTrapsGroup,_e:sessionObjectGroup,'alcatelIND1SessionMgrMIBCompliances':alcatelIND1SessionMgrMIBCompliances,'alcatelIND1SessionMgrMIBCompliance':alcatelIND1SessionMgrMIBCompliance})