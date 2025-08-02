_t='ciscoRfSupNotifGroupRev1'
_s='ciscoRfSupNotifGroup'
_r='ciscoRfSupPeerLinkStateChangeEvent'
_q='ciscoRfSupHAFailureEvent'
_p='ciscoRfSupTimeZoneChangeEvent'
_o='cRfSupSysErrorType'
_n='cRfSupSysSeverity'
_m='cRfSupSysFailureReason'
_l='cRfSupSysIfCounterSync'
_k='cRfSupNotificationsEnabled'
_j='cRfSupCpuInitTime'
_i='cRfSupCpuActiveSeverity'
_h='cRfSupSysStandbyBootFile'
_g='cRfSupSysBootImageOper'
_f='cRfSupSysBootImageAdmin'
_e='cRfSupSysBootImageSyncTime'
_d='cRfSupSysStartupConfigOper'
_c='cRfSupSysStartupConfigAdmin'
_b='cRfSupSysRunningConfigOper'
_a='cRfSupSysRunningConfigAdmin'
_Z='cRfSupSysSwitchovers'
_Y='cRfSupCpuUniqueIndex'
_X='TruthValue'
_W='SnmpAdminString'
_V='ifOperStatus'
_U='ifIndex'
_T='ifAdminStatus'
_S='ciscoRfSupSysOptionalSyncGroup'
_R='ciscoRfSupTimeChangeEvent'
_Q='cRfSupActionLastSyncResult'
_P='cRfSupActionManualSync'
_O='cRfSupSysStartupConfigSyncTime'
_N='cRfSupSysRunningConfigSyncTime'
_M='ciscoRfSupSysOptionalGroup'
_L='deprecated'
_K='cRfSupSysSwitchoverTime'
_J='cRfSupSysAvailableStartTime'
_I='IF-MIB'
_H='ciscoRfSupCpuGroup'
_G='ciscoRfSupActionGroup'
_F='ciscoRfSupSysGroup'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-RF-SUPPLEMENTAL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ConfigCopyState,=mibBuilder.importSymbols('CISCO-CONFIG-COPY-MIB','ConfigCopyState')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
ifAdminStatus,ifIndex,ifOperStatus=mibBuilder.importSymbols(_I,_T,_U,_V)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_W)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_X)
ciscoRfSupMIB=ModuleIdentity((1,3,6,1,4,1,9,9,198))
if mibBuilder.loadTexts:ciscoRfSupMIB.setRevisions(('2019-02-22 00:00','2004-05-27 00:00','2004-03-04 00:00','2001-03-16 00:00'))
class RfSupSyncAdminState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableAutoSync',1),('disableAutoSync',2)))
class RfSupSyncOperState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inSync',1),('lastUpdateFailed',2),('commDown',3),('syncDisabled',4),('noStandbyPresent',5)))
_CiscoRfSupMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoRfSupMIBNotifs=_CiscoRfSupMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,198,0))
_CiscoRfSupMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRfSupMIBObjects=_CiscoRfSupMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,198,1))
_CRfSupSystem_ObjectIdentity=ObjectIdentity
cRfSupSystem=_CRfSupSystem_ObjectIdentity((1,3,6,1,4,1,9,9,198,1,1))
_CRfSupSysAvailableStartTime_Type=DateAndTime
_CRfSupSysAvailableStartTime_Object=MibScalar
cRfSupSysAvailableStartTime=_CRfSupSysAvailableStartTime_Object((1,3,6,1,4,1,9,9,198,1,1,1),_CRfSupSysAvailableStartTime_Type())
cRfSupSysAvailableStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysAvailableStartTime.setStatus(_B)
_CRfSupSysSwitchoverTime_Type=DateAndTime
_CRfSupSysSwitchoverTime_Object=MibScalar
cRfSupSysSwitchoverTime=_CRfSupSysSwitchoverTime_Object((1,3,6,1,4,1,9,9,198,1,1,2),_CRfSupSysSwitchoverTime_Type())
cRfSupSysSwitchoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysSwitchoverTime.setStatus(_B)
_CRfSupSysSwitchovers_Type=Counter32
_CRfSupSysSwitchovers_Object=MibScalar
cRfSupSysSwitchovers=_CRfSupSysSwitchovers_Object((1,3,6,1,4,1,9,9,198,1,1,3),_CRfSupSysSwitchovers_Type())
cRfSupSysSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysSwitchovers.setStatus(_B)
_CRfSupSysRunningConfigSyncTime_Type=DateAndTime
_CRfSupSysRunningConfigSyncTime_Object=MibScalar
cRfSupSysRunningConfigSyncTime=_CRfSupSysRunningConfigSyncTime_Object((1,3,6,1,4,1,9,9,198,1,1,4),_CRfSupSysRunningConfigSyncTime_Type())
cRfSupSysRunningConfigSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysRunningConfigSyncTime.setStatus(_B)
_CRfSupSysRunningConfigAdmin_Type=RfSupSyncAdminState
_CRfSupSysRunningConfigAdmin_Object=MibScalar
cRfSupSysRunningConfigAdmin=_CRfSupSysRunningConfigAdmin_Object((1,3,6,1,4,1,9,9,198,1,1,5),_CRfSupSysRunningConfigAdmin_Type())
cRfSupSysRunningConfigAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:cRfSupSysRunningConfigAdmin.setStatus(_B)
_CRfSupSysRunningConfigOper_Type=RfSupSyncOperState
_CRfSupSysRunningConfigOper_Object=MibScalar
cRfSupSysRunningConfigOper=_CRfSupSysRunningConfigOper_Object((1,3,6,1,4,1,9,9,198,1,1,6),_CRfSupSysRunningConfigOper_Type())
cRfSupSysRunningConfigOper.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysRunningConfigOper.setStatus(_B)
_CRfSupSysStartupConfigSyncTime_Type=DateAndTime
_CRfSupSysStartupConfigSyncTime_Object=MibScalar
cRfSupSysStartupConfigSyncTime=_CRfSupSysStartupConfigSyncTime_Object((1,3,6,1,4,1,9,9,198,1,1,7),_CRfSupSysStartupConfigSyncTime_Type())
cRfSupSysStartupConfigSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysStartupConfigSyncTime.setStatus(_B)
_CRfSupSysStartupConfigAdmin_Type=RfSupSyncAdminState
_CRfSupSysStartupConfigAdmin_Object=MibScalar
cRfSupSysStartupConfigAdmin=_CRfSupSysStartupConfigAdmin_Object((1,3,6,1,4,1,9,9,198,1,1,8),_CRfSupSysStartupConfigAdmin_Type())
cRfSupSysStartupConfigAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:cRfSupSysStartupConfigAdmin.setStatus(_B)
_CRfSupSysStartupConfigOper_Type=RfSupSyncOperState
_CRfSupSysStartupConfigOper_Object=MibScalar
cRfSupSysStartupConfigOper=_CRfSupSysStartupConfigOper_Object((1,3,6,1,4,1,9,9,198,1,1,9),_CRfSupSysStartupConfigOper_Type())
cRfSupSysStartupConfigOper.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysStartupConfigOper.setStatus(_B)
_CRfSupSysBootImageSyncTime_Type=DateAndTime
_CRfSupSysBootImageSyncTime_Object=MibScalar
cRfSupSysBootImageSyncTime=_CRfSupSysBootImageSyncTime_Object((1,3,6,1,4,1,9,9,198,1,1,10),_CRfSupSysBootImageSyncTime_Type())
cRfSupSysBootImageSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysBootImageSyncTime.setStatus(_B)
_CRfSupSysBootImageAdmin_Type=RfSupSyncAdminState
_CRfSupSysBootImageAdmin_Object=MibScalar
cRfSupSysBootImageAdmin=_CRfSupSysBootImageAdmin_Object((1,3,6,1,4,1,9,9,198,1,1,11),_CRfSupSysBootImageAdmin_Type())
cRfSupSysBootImageAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:cRfSupSysBootImageAdmin.setStatus(_B)
_CRfSupSysBootImageOper_Type=RfSupSyncOperState
_CRfSupSysBootImageOper_Object=MibScalar
cRfSupSysBootImageOper=_CRfSupSysBootImageOper_Object((1,3,6,1,4,1,9,9,198,1,1,12),_CRfSupSysBootImageOper_Type())
cRfSupSysBootImageOper.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysBootImageOper.setStatus(_B)
class _CRfSupSysStandbyBootFile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CRfSupSysStandbyBootFile_Type.__name__=_W
_CRfSupSysStandbyBootFile_Object=MibScalar
cRfSupSysStandbyBootFile=_CRfSupSysStandbyBootFile_Object((1,3,6,1,4,1,9,9,198,1,1,13),_CRfSupSysStandbyBootFile_Type())
cRfSupSysStandbyBootFile.setMaxAccess(_D)
if mibBuilder.loadTexts:cRfSupSysStandbyBootFile.setStatus(_B)
class _CRfSupNotificationsEnabled_Type(TruthValue):defaultValue=2
_CRfSupNotificationsEnabled_Type.__name__=_X
_CRfSupNotificationsEnabled_Object=MibScalar
cRfSupNotificationsEnabled=_CRfSupNotificationsEnabled_Object((1,3,6,1,4,1,9,9,198,1,1,14),_CRfSupNotificationsEnabled_Type())
cRfSupNotificationsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cRfSupNotificationsEnabled.setStatus(_B)
_CRfSupSysIfCounterSync_Type=TruthValue
_CRfSupSysIfCounterSync_Object=MibScalar
cRfSupSysIfCounterSync=_CRfSupSysIfCounterSync_Object((1,3,6,1,4,1,9,9,198,1,1,15),_CRfSupSysIfCounterSync_Type())
cRfSupSysIfCounterSync.setMaxAccess(_D)
if mibBuilder.loadTexts:cRfSupSysIfCounterSync.setStatus(_B)
_CRfSupSysFailureReason_Type=OctetString
_CRfSupSysFailureReason_Object=MibScalar
cRfSupSysFailureReason=_CRfSupSysFailureReason_Object((1,3,6,1,4,1,9,9,198,1,1,16),_CRfSupSysFailureReason_Type())
cRfSupSysFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysFailureReason.setStatus(_B)
class _CRfSupSysSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('informational',4),('clear',5)))
_CRfSupSysSeverity_Type.__name__=_E
_CRfSupSysSeverity_Object=MibScalar
cRfSupSysSeverity=_CRfSupSysSeverity_Object((1,3,6,1,4,1,9,9,198,1,1,17),_CRfSupSysSeverity_Type())
cRfSupSysSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysSeverity.setStatus(_B)
class _CRfSupSysErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35)));namedValues=NamedValues(*(('download-config',1),('download-code',2),('download-icon',3),('download-image',4),('download-signature',5),('download-webadmincert',6),('download-webauthcert',7),('download-webauthbundle',8),('download-eapdevcert',9),('download-eapcacert',10),('download-login-banner',11),('upload-config',12),('upload-debug-file',13),('upload-crashfile',14),('upload-watchdog-crash-file',15),('upload-panic-crash-file',16),('upload-coredump',17),('upload-errorlog',18),('upload-invalid-config',19),('upload-pac',20),('upload-radio-core-dump',21),('upload-ap-crash-data',22),('upload-signature',23),('upload-systemtrace',24),('upload-packet-capture',25),('upload-traplog',26),('route-add',27),('route-del',28),('interface-service-port',29),('reset',30),('other',31),('config-sync-fail',32),('peer-maintenance',33),('peer-loss',34),('rfTrapClearTemplist',35)))
_CRfSupSysErrorType_Type.__name__=_E
_CRfSupSysErrorType_Object=MibScalar
cRfSupSysErrorType=_CRfSupSysErrorType_Object((1,3,6,1,4,1,9,9,198,1,1,18),_CRfSupSysErrorType_Type())
cRfSupSysErrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupSysErrorType.setStatus(_B)
_CRfSupCpu_ObjectIdentity=ObjectIdentity
cRfSupCpu=_CRfSupCpu_ObjectIdentity((1,3,6,1,4,1,9,9,198,1,2))
_CRfSupCpuTable_Object=MibTable
cRfSupCpuTable=_CRfSupCpuTable_Object((1,3,6,1,4,1,9,9,198,1,2,1))
if mibBuilder.loadTexts:cRfSupCpuTable.setStatus(_B)
_CRfSupCpuEntry_Object=MibTableRow
cRfSupCpuEntry=_CRfSupCpuEntry_Object((1,3,6,1,4,1,9,9,198,1,2,1,1))
cRfSupCpuEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:cRfSupCpuEntry.setStatus(_B)
_CRfSupCpuUniqueIndex_Type=PhysicalIndex
_CRfSupCpuUniqueIndex_Object=MibTableColumn
cRfSupCpuUniqueIndex=_CRfSupCpuUniqueIndex_Object((1,3,6,1,4,1,9,9,198,1,2,1,1,1),_CRfSupCpuUniqueIndex_Type())
cRfSupCpuUniqueIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cRfSupCpuUniqueIndex.setStatus(_B)
class _CRfSupCpuActiveSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('nonFaulty',0),('nonTrafficAffectingFault',1),('partialTrafficAffectingFault',2),('fullyTrafficAffectingFault',3),('unknown',4)))
_CRfSupCpuActiveSeverity_Type.__name__=_E
_CRfSupCpuActiveSeverity_Object=MibTableColumn
cRfSupCpuActiveSeverity=_CRfSupCpuActiveSeverity_Object((1,3,6,1,4,1,9,9,198,1,2,1,1,2),_CRfSupCpuActiveSeverity_Type())
cRfSupCpuActiveSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupCpuActiveSeverity.setStatus(_B)
_CRfSupCpuInitTime_Type=DateAndTime
_CRfSupCpuInitTime_Object=MibTableColumn
cRfSupCpuInitTime=_CRfSupCpuInitTime_Object((1,3,6,1,4,1,9,9,198,1,2,1,1,3),_CRfSupCpuInitTime_Type())
cRfSupCpuInitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupCpuInitTime.setStatus(_B)
_CRfSupAction_ObjectIdentity=ObjectIdentity
cRfSupAction=_CRfSupAction_ObjectIdentity((1,3,6,1,4,1,9,9,198,1,3))
class _CRfSupActionManualSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noAction',1),('runningConfig',2),('startupConfig',3),('bootImage',4)))
_CRfSupActionManualSync_Type.__name__=_E
_CRfSupActionManualSync_Object=MibScalar
cRfSupActionManualSync=_CRfSupActionManualSync_Object((1,3,6,1,4,1,9,9,198,1,3,1),_CRfSupActionManualSync_Type())
cRfSupActionManualSync.setMaxAccess(_D)
if mibBuilder.loadTexts:cRfSupActionManualSync.setStatus(_B)
_CRfSupActionLastSyncResult_Type=ConfigCopyState
_CRfSupActionLastSyncResult_Object=MibScalar
cRfSupActionLastSyncResult=_CRfSupActionLastSyncResult_Object((1,3,6,1,4,1,9,9,198,1,3,2),_CRfSupActionLastSyncResult_Type())
cRfSupActionLastSyncResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cRfSupActionLastSyncResult.setStatus(_B)
_CiscoRfSupMibConformance_ObjectIdentity=ObjectIdentity
ciscoRfSupMibConformance=_CiscoRfSupMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,198,2))
_CiscoRfSupMibCompliances_ObjectIdentity=ObjectIdentity
ciscoRfSupMibCompliances=_CiscoRfSupMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,198,2,1))
_CiscoRfSupMibGroups_ObjectIdentity=ObjectIdentity
ciscoRfSupMibGroups=_CiscoRfSupMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,198,2,2))
ciscoRfSupSysGroup=ObjectGroup((1,3,6,1,4,1,9,9,198,2,2,1))
ciscoRfSupSysGroup.setObjects(*((_A,_J),(_A,_K),(_A,_Z),(_A,_N),(_A,_a),(_A,_b),(_A,_O),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ciscoRfSupSysGroup.setStatus(_B)
ciscoRfSupCpuGroup=ObjectGroup((1,3,6,1,4,1,9,9,198,2,2,2))
ciscoRfSupCpuGroup.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoRfSupCpuGroup.setStatus(_B)
ciscoRfSupActionGroup=ObjectGroup((1,3,6,1,4,1,9,9,198,2,2,3))
ciscoRfSupActionGroup.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoRfSupActionGroup.setStatus(_B)
ciscoRfSupSysOptionalGroup=ObjectGroup((1,3,6,1,4,1,9,9,198,2,2,4))
ciscoRfSupSysOptionalGroup.setObjects((_A,_k))
if mibBuilder.loadTexts:ciscoRfSupSysOptionalGroup.setStatus(_B)
ciscoRfSupSysOptionalSyncGroup=ObjectGroup((1,3,6,1,4,1,9,9,198,2,2,6))
ciscoRfSupSysOptionalSyncGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:ciscoRfSupSysOptionalSyncGroup.setStatus(_B)
ciscoRfSupTimeChangeEvent=NotificationType((1,3,6,1,4,1,9,9,198,0,1))
ciscoRfSupTimeChangeEvent.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoRfSupTimeChangeEvent.setStatus(_B)
ciscoRfSupTimeZoneChangeEvent=NotificationType((1,3,6,1,4,1,9,9,198,0,2))
ciscoRfSupTimeZoneChangeEvent.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoRfSupTimeZoneChangeEvent.setStatus(_B)
ciscoRfSupHAFailureEvent=NotificationType((1,3,6,1,4,1,9,9,198,0,3))
ciscoRfSupHAFailureEvent.setObjects(*((_A,_O),(_A,_N),(_A,_P),(_A,_Q),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciscoRfSupHAFailureEvent.setStatus(_B)
ciscoRfSupPeerLinkStateChangeEvent=NotificationType((1,3,6,1,4,1,9,9,198,0,4))
ciscoRfSupPeerLinkStateChangeEvent.setObjects(*((_I,_U),(_I,_T),(_I,_V)))
if mibBuilder.loadTexts:ciscoRfSupPeerLinkStateChangeEvent.setStatus(_B)
ciscoRfSupNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,198,2,2,5))
ciscoRfSupNotifGroup.setObjects((_A,_R))
if mibBuilder.loadTexts:ciscoRfSupNotifGroup.setStatus(_L)
ciscoRfSupNotifGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,198,2,2,7))
ciscoRfSupNotifGroupRev1.setObjects(*((_A,_R),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:ciscoRfSupNotifGroupRev1.setStatus(_B)
ciscoRfSupMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,198,2,1,1))
ciscoRfSupMibCompliance.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoRfSupMibCompliance.setStatus(_L)
ciscoRfSupMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,198,2,1,2))
ciscoRfSupMibComplianceRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_M)))
if mibBuilder.loadTexts:ciscoRfSupMibComplianceRev1.setStatus(_L)
ciscoRfSupMibComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,198,2,1,3))
ciscoRfSupMibComplianceRev2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_M),(_A,_s),(_A,_S)))
if mibBuilder.loadTexts:ciscoRfSupMibComplianceRev2.setStatus(_L)
ciscoRfSupMibComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,198,2,1,4))
ciscoRfSupMibComplianceRev3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_M),(_A,_t),(_A,_S)))
if mibBuilder.loadTexts:ciscoRfSupMibComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RfSupSyncAdminState':RfSupSyncAdminState,'RfSupSyncOperState':RfSupSyncOperState,'ciscoRfSupMIB':ciscoRfSupMIB,'ciscoRfSupMIBNotifs':ciscoRfSupMIBNotifs,_R:ciscoRfSupTimeChangeEvent,_p:ciscoRfSupTimeZoneChangeEvent,_q:ciscoRfSupHAFailureEvent,_r:ciscoRfSupPeerLinkStateChangeEvent,'ciscoRfSupMIBObjects':ciscoRfSupMIBObjects,'cRfSupSystem':cRfSupSystem,_J:cRfSupSysAvailableStartTime,_K:cRfSupSysSwitchoverTime,_Z:cRfSupSysSwitchovers,_N:cRfSupSysRunningConfigSyncTime,_a:cRfSupSysRunningConfigAdmin,_b:cRfSupSysRunningConfigOper,_O:cRfSupSysStartupConfigSyncTime,_c:cRfSupSysStartupConfigAdmin,_d:cRfSupSysStartupConfigOper,_e:cRfSupSysBootImageSyncTime,_f:cRfSupSysBootImageAdmin,_g:cRfSupSysBootImageOper,_h:cRfSupSysStandbyBootFile,_k:cRfSupNotificationsEnabled,_l:cRfSupSysIfCounterSync,_m:cRfSupSysFailureReason,_n:cRfSupSysSeverity,_o:cRfSupSysErrorType,'cRfSupCpu':cRfSupCpu,'cRfSupCpuTable':cRfSupCpuTable,'cRfSupCpuEntry':cRfSupCpuEntry,_Y:cRfSupCpuUniqueIndex,_i:cRfSupCpuActiveSeverity,_j:cRfSupCpuInitTime,'cRfSupAction':cRfSupAction,_P:cRfSupActionManualSync,_Q:cRfSupActionLastSyncResult,'ciscoRfSupMibConformance':ciscoRfSupMibConformance,'ciscoRfSupMibCompliances':ciscoRfSupMibCompliances,'ciscoRfSupMibCompliance':ciscoRfSupMibCompliance,'ciscoRfSupMibComplianceRev1':ciscoRfSupMibComplianceRev1,'ciscoRfSupMibComplianceRev2':ciscoRfSupMibComplianceRev2,'ciscoRfSupMibComplianceRev3':ciscoRfSupMibComplianceRev3,'ciscoRfSupMibGroups':ciscoRfSupMibGroups,_F:ciscoRfSupSysGroup,_H:ciscoRfSupCpuGroup,_G:ciscoRfSupActionGroup,_M:ciscoRfSupSysOptionalGroup,_s:ciscoRfSupNotifGroup,_S:ciscoRfSupSysOptionalSyncGroup,_t:ciscoRfSupNotifGroupRev1})