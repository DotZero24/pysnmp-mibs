_j='clogNotificationsGroup'
_i='clogOriginIDGroup'
_h='clogServerGroup'
_g='clogMessageGenerated'
_f='clogOriginID'
_e='clogOriginIDType'
_d='clogServerStatus'
_c='clogMaxServers'
_b='clogHistMsgsFlushed'
_a='clogHistTableMaxLength'
_Z='clogMsgDrops'
_Y='clogMsgIgnores'
_X='clogMaxSeverity'
_W='clogNotificationsEnabled'
_V='clogNotificationsSent'
_U='clogServerAddr'
_T='clogServerAddrType'
_S='clogHistIndex'
_R='SyslogSeverity'
_Q='TruthValue'
_P='SnmpAdminString'
_O='InetAddress'
_N='ciscoSyslogMIBGroup'
_M='clogHistTimestamp'
_L='clogHistMsgText'
_K='clogHistMsgName'
_J='clogHistSeverity'
_I='clogHistFacility'
_H='not-accessible'
_G='messages'
_F='DisplayString'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-SYSLOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_Q)
ciscoSyslogMIB=ModuleIdentity((1,3,6,1,4,1,9,9,41))
if mibBuilder.loadTexts:ciscoSyslogMIB.setRevisions(('2005-12-03 00:00','2005-08-11 00:00','2005-06-01 00:00','1995-08-07 00:00'))
class SyslogSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('info',7),('debug',8)))
_CiscoSyslogMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSyslogMIBObjects=_CiscoSyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,41,1))
_ClogBasic_ObjectIdentity=ObjectIdentity
clogBasic=_ClogBasic_ObjectIdentity((1,3,6,1,4,1,9,9,41,1,1))
_ClogNotificationsSent_Type=Counter32
_ClogNotificationsSent_Object=MibScalar
clogNotificationsSent=_ClogNotificationsSent_Object((1,3,6,1,4,1,9,9,41,1,1,1),_ClogNotificationsSent_Type())
clogNotificationsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clogNotificationsSent.setStatus(_B)
if mibBuilder.loadTexts:clogNotificationsSent.setUnits('notifications')
class _ClogNotificationsEnabled_Type(TruthValue):defaultValue=2
_ClogNotificationsEnabled_Type.__name__=_Q
_ClogNotificationsEnabled_Object=MibScalar
clogNotificationsEnabled=_ClogNotificationsEnabled_Object((1,3,6,1,4,1,9,9,41,1,1,2),_ClogNotificationsEnabled_Type())
clogNotificationsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:clogNotificationsEnabled.setStatus(_B)
class _ClogMaxSeverity_Type(SyslogSeverity):defaultValue=5
_ClogMaxSeverity_Type.__name__=_R
_ClogMaxSeverity_Object=MibScalar
clogMaxSeverity=_ClogMaxSeverity_Object((1,3,6,1,4,1,9,9,41,1,1,3),_ClogMaxSeverity_Type())
clogMaxSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:clogMaxSeverity.setStatus(_B)
_ClogMsgIgnores_Type=Counter32
_ClogMsgIgnores_Object=MibScalar
clogMsgIgnores=_ClogMsgIgnores_Object((1,3,6,1,4,1,9,9,41,1,1,4),_ClogMsgIgnores_Type())
clogMsgIgnores.setMaxAccess(_C)
if mibBuilder.loadTexts:clogMsgIgnores.setStatus(_B)
if mibBuilder.loadTexts:clogMsgIgnores.setUnits(_G)
_ClogMsgDrops_Type=Counter32
_ClogMsgDrops_Object=MibScalar
clogMsgDrops=_ClogMsgDrops_Object((1,3,6,1,4,1,9,9,41,1,1,5),_ClogMsgDrops_Type())
clogMsgDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:clogMsgDrops.setStatus(_B)
if mibBuilder.loadTexts:clogMsgDrops.setUnits(_G)
class _ClogOriginIDType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('other',2),('hostName',3),('ipv4Address',4),('contextName',5),('userDefined',6)))
_ClogOriginIDType_Type.__name__=_E
_ClogOriginIDType_Object=MibScalar
clogOriginIDType=_ClogOriginIDType_Object((1,3,6,1,4,1,9,9,41,1,1,6),_ClogOriginIDType_Type())
clogOriginIDType.setMaxAccess(_D)
if mibBuilder.loadTexts:clogOriginIDType.setStatus(_B)
class _ClogOriginID_Type(SnmpAdminString):defaultValue=OctetString('')
_ClogOriginID_Type.__name__=_P
_ClogOriginID_Object=MibScalar
clogOriginID=_ClogOriginID_Object((1,3,6,1,4,1,9,9,41,1,1,7),_ClogOriginID_Type())
clogOriginID.setMaxAccess(_D)
if mibBuilder.loadTexts:clogOriginID.setStatus(_B)
_ClogHistory_ObjectIdentity=ObjectIdentity
clogHistory=_ClogHistory_ObjectIdentity((1,3,6,1,4,1,9,9,41,1,2))
class _ClogHistTableMaxLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_ClogHistTableMaxLength_Type.__name__=_E
_ClogHistTableMaxLength_Object=MibScalar
clogHistTableMaxLength=_ClogHistTableMaxLength_Object((1,3,6,1,4,1,9,9,41,1,2,1),_ClogHistTableMaxLength_Type())
clogHistTableMaxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:clogHistTableMaxLength.setStatus(_B)
if mibBuilder.loadTexts:clogHistTableMaxLength.setUnits('entries')
_ClogHistMsgsFlushed_Type=Counter32
_ClogHistMsgsFlushed_Object=MibScalar
clogHistMsgsFlushed=_ClogHistMsgsFlushed_Object((1,3,6,1,4,1,9,9,41,1,2,2),_ClogHistMsgsFlushed_Type())
clogHistMsgsFlushed.setMaxAccess(_C)
if mibBuilder.loadTexts:clogHistMsgsFlushed.setStatus(_B)
if mibBuilder.loadTexts:clogHistMsgsFlushed.setUnits(_G)
_ClogHistoryTable_Object=MibTable
clogHistoryTable=_ClogHistoryTable_Object((1,3,6,1,4,1,9,9,41,1,2,3))
if mibBuilder.loadTexts:clogHistoryTable.setStatus(_B)
_ClogHistoryEntry_Object=MibTableRow
clogHistoryEntry=_ClogHistoryEntry_Object((1,3,6,1,4,1,9,9,41,1,2,3,1))
clogHistoryEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:clogHistoryEntry.setStatus(_B)
class _ClogHistIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ClogHistIndex_Type.__name__=_E
_ClogHistIndex_Object=MibTableColumn
clogHistIndex=_ClogHistIndex_Object((1,3,6,1,4,1,9,9,41,1,2,3,1,1),_ClogHistIndex_Type())
clogHistIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:clogHistIndex.setStatus(_B)
class _ClogHistFacility_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ClogHistFacility_Type.__name__=_F
_ClogHistFacility_Object=MibTableColumn
clogHistFacility=_ClogHistFacility_Object((1,3,6,1,4,1,9,9,41,1,2,3,1,2),_ClogHistFacility_Type())
clogHistFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:clogHistFacility.setStatus(_B)
_ClogHistSeverity_Type=SyslogSeverity
_ClogHistSeverity_Object=MibTableColumn
clogHistSeverity=_ClogHistSeverity_Object((1,3,6,1,4,1,9,9,41,1,2,3,1,3),_ClogHistSeverity_Type())
clogHistSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:clogHistSeverity.setStatus(_B)
class _ClogHistMsgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_ClogHistMsgName_Type.__name__=_F
_ClogHistMsgName_Object=MibTableColumn
clogHistMsgName=_ClogHistMsgName_Object((1,3,6,1,4,1,9,9,41,1,2,3,1,4),_ClogHistMsgName_Type())
clogHistMsgName.setMaxAccess(_C)
if mibBuilder.loadTexts:clogHistMsgName.setStatus(_B)
class _ClogHistMsgText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ClogHistMsgText_Type.__name__=_F
_ClogHistMsgText_Object=MibTableColumn
clogHistMsgText=_ClogHistMsgText_Object((1,3,6,1,4,1,9,9,41,1,2,3,1,5),_ClogHistMsgText_Type())
clogHistMsgText.setMaxAccess(_C)
if mibBuilder.loadTexts:clogHistMsgText.setStatus(_B)
_ClogHistTimestamp_Type=TimeStamp
_ClogHistTimestamp_Object=MibTableColumn
clogHistTimestamp=_ClogHistTimestamp_Object((1,3,6,1,4,1,9,9,41,1,2,3,1,6),_ClogHistTimestamp_Type())
clogHistTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:clogHistTimestamp.setStatus(_B)
_ClogServer_ObjectIdentity=ObjectIdentity
clogServer=_ClogServer_ObjectIdentity((1,3,6,1,4,1,9,9,41,1,3))
_ClogMaxServers_Type=Unsigned32
_ClogMaxServers_Object=MibScalar
clogMaxServers=_ClogMaxServers_Object((1,3,6,1,4,1,9,9,41,1,3,1),_ClogMaxServers_Type())
clogMaxServers.setMaxAccess(_C)
if mibBuilder.loadTexts:clogMaxServers.setStatus(_B)
_ClogServerConfigTable_Object=MibTable
clogServerConfigTable=_ClogServerConfigTable_Object((1,3,6,1,4,1,9,9,41,1,3,2))
if mibBuilder.loadTexts:clogServerConfigTable.setStatus(_B)
_ClogServerConfigEntry_Object=MibTableRow
clogServerConfigEntry=_ClogServerConfigEntry_Object((1,3,6,1,4,1,9,9,41,1,3,2,1))
clogServerConfigEntry.setIndexNames((0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:clogServerConfigEntry.setStatus(_B)
_ClogServerAddrType_Type=InetAddressType
_ClogServerAddrType_Object=MibTableColumn
clogServerAddrType=_ClogServerAddrType_Object((1,3,6,1,4,1,9,9,41,1,3,2,1,1),_ClogServerAddrType_Type())
clogServerAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:clogServerAddrType.setStatus(_B)
class _ClogServerAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ClogServerAddr_Type.__name__=_O
_ClogServerAddr_Object=MibTableColumn
clogServerAddr=_ClogServerAddr_Object((1,3,6,1,4,1,9,9,41,1,3,2,1,2),_ClogServerAddr_Type())
clogServerAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:clogServerAddr.setStatus(_B)
_ClogServerStatus_Type=RowStatus
_ClogServerStatus_Object=MibTableColumn
clogServerStatus=_ClogServerStatus_Object((1,3,6,1,4,1,9,9,41,1,3,2,1,3),_ClogServerStatus_Type())
clogServerStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:clogServerStatus.setStatus(_B)
_CiscoSyslogMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoSyslogMIBNotificationPrefix=_CiscoSyslogMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,41,2))
_CiscoSyslogMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoSyslogMIBNotifications=_CiscoSyslogMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,41,2,0))
_CiscoSyslogMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSyslogMIBConformance=_CiscoSyslogMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,41,3))
_CiscoSyslogMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSyslogMIBCompliances=_CiscoSyslogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,41,3,1))
_CiscoSyslogMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSyslogMIBGroups=_CiscoSyslogMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,41,3,2))
ciscoSyslogMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,41,3,2,1))
ciscoSyslogMIBGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoSyslogMIBGroup.setStatus(_B)
clogServerGroup=ObjectGroup((1,3,6,1,4,1,9,9,41,3,2,3))
clogServerGroup.setObjects(*((_A,_c),(_A,_d)))
if mibBuilder.loadTexts:clogServerGroup.setStatus(_B)
clogOriginIDGroup=ObjectGroup((1,3,6,1,4,1,9,9,41,3,2,4))
clogOriginIDGroup.setObjects(*((_A,_e),(_A,_f)))
if mibBuilder.loadTexts:clogOriginIDGroup.setStatus(_B)
clogMessageGenerated=NotificationType((1,3,6,1,4,1,9,9,41,2,0,1))
clogMessageGenerated.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:clogMessageGenerated.setStatus(_B)
clogNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,41,3,2,2))
clogNotificationsGroup.setObjects((_A,_g))
if mibBuilder.loadTexts:clogNotificationsGroup.setStatus(_B)
ciscoSyslogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,41,3,1,1))
ciscoSyslogMIBCompliance.setObjects((_A,_N))
if mibBuilder.loadTexts:ciscoSyslogMIBCompliance.setStatus('deprecated')
ciscoSyslogMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,41,3,1,2))
ciscoSyslogMIBComplianceRev1.setObjects(*((_A,_N),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoSyslogMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_R:SyslogSeverity,'ciscoSyslogMIB':ciscoSyslogMIB,'ciscoSyslogMIBObjects':ciscoSyslogMIBObjects,'clogBasic':clogBasic,_V:clogNotificationsSent,_W:clogNotificationsEnabled,_X:clogMaxSeverity,_Y:clogMsgIgnores,_Z:clogMsgDrops,_e:clogOriginIDType,_f:clogOriginID,'clogHistory':clogHistory,_a:clogHistTableMaxLength,_b:clogHistMsgsFlushed,'clogHistoryTable':clogHistoryTable,'clogHistoryEntry':clogHistoryEntry,_S:clogHistIndex,_I:clogHistFacility,_J:clogHistSeverity,_K:clogHistMsgName,_L:clogHistMsgText,_M:clogHistTimestamp,'clogServer':clogServer,_c:clogMaxServers,'clogServerConfigTable':clogServerConfigTable,'clogServerConfigEntry':clogServerConfigEntry,_T:clogServerAddrType,_U:clogServerAddr,_d:clogServerStatus,'ciscoSyslogMIBNotificationPrefix':ciscoSyslogMIBNotificationPrefix,'ciscoSyslogMIBNotifications':ciscoSyslogMIBNotifications,_g:clogMessageGenerated,'ciscoSyslogMIBConformance':ciscoSyslogMIBConformance,'ciscoSyslogMIBCompliances':ciscoSyslogMIBCompliances,'ciscoSyslogMIBCompliance':ciscoSyslogMIBCompliance,'ciscoSyslogMIBComplianceRev1':ciscoSyslogMIBComplianceRev1,'ciscoSyslogMIBGroups':ciscoSyslogMIBGroups,_N:ciscoSyslogMIBGroup,_j:clogNotificationsGroup,_h:clogServerGroup,_i:clogOriginIDGroup})