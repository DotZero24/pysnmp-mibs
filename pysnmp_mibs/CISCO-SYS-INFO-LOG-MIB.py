_g='csilCommandConfigGroup'
_f='csilServerConfigGroup'
_e='csilGlobalConfigGroup'
_d='csilLoggingFailNotif'
_c='csilSysInfoLogNotifEnabled'
_b='csilCommandStatus'
_a='csilCommandExecOrder'
_Z='csilCommandString'
_Y='csilMaxCommandPerProfile'
_X='csilServerRowStatus'
_W='csilServerRcpUserName'
_V='csilServerLoggingFileName'
_U='csilServerInterval'
_T='csilServerProtocol'
_S='csilServerProfileIndex'
_R='csilServerAddressType'
_Q='csilServerAddress'
_P='csilMaxProfilePerServerAllowed'
_O='csilMaxServerAllowed'
_N='csilSysInfoLogEnabled'
_M='csilCommandIndex'
_L='csilCommandProfileIndex'
_K='csilServerIndex'
_J='read-only'
_I='csilServerLastStatus'
_H='not-accessible'
_G='Unsigned32'
_F='Integer32'
_E='SnmpAdminString'
_D='read-write'
_C='read-create'
_B='CISCO-SYS-INFO-LOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoSysInfoLogMIB=ModuleIdentity((1,3,6,1,4,1,9,9,330))
if mibBuilder.loadTexts:ciscoSysInfoLogMIB.setRevisions(('2005-08-12 10:00','2003-01-24 10:00'))
_CiscoSysInfoLogMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSysInfoLogMIBNotifs=_CiscoSysInfoLogMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,330,0))
_CiscoSysInfoLogMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSysInfoLogMIBObjects=_CiscoSysInfoLogMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,330,1))
_CsilGlobalConfig_ObjectIdentity=ObjectIdentity
csilGlobalConfig=_CsilGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,330,1,1))
_CsilSysInfoLogEnabled_Type=TruthValue
_CsilSysInfoLogEnabled_Object=MibScalar
csilSysInfoLogEnabled=_CsilSysInfoLogEnabled_Object((1,3,6,1,4,1,9,9,330,1,1,1),_CsilSysInfoLogEnabled_Type())
csilSysInfoLogEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:csilSysInfoLogEnabled.setStatus(_A)
_CsilSysInfoLogNotifEnabled_Type=TruthValue
_CsilSysInfoLogNotifEnabled_Object=MibScalar
csilSysInfoLogNotifEnabled=_CsilSysInfoLogNotifEnabled_Object((1,3,6,1,4,1,9,9,330,1,1,2),_CsilSysInfoLogNotifEnabled_Type())
csilSysInfoLogNotifEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:csilSysInfoLogNotifEnabled.setStatus(_A)
_CsilServerConfig_ObjectIdentity=ObjectIdentity
csilServerConfig=_CsilServerConfig_ObjectIdentity((1,3,6,1,4,1,9,9,330,1,2))
class _CsilMaxServerAllowed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CsilMaxServerAllowed_Type.__name__=_G
_CsilMaxServerAllowed_Object=MibScalar
csilMaxServerAllowed=_CsilMaxServerAllowed_Object((1,3,6,1,4,1,9,9,330,1,2,1),_CsilMaxServerAllowed_Type())
csilMaxServerAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:csilMaxServerAllowed.setStatus(_A)
if mibBuilder.loadTexts:csilMaxServerAllowed.setUnits('servers')
_CsilMaxProfilePerServerAllowed_Type=Unsigned32
_CsilMaxProfilePerServerAllowed_Object=MibScalar
csilMaxProfilePerServerAllowed=_CsilMaxProfilePerServerAllowed_Object((1,3,6,1,4,1,9,9,330,1,2,2),_CsilMaxProfilePerServerAllowed_Type())
csilMaxProfilePerServerAllowed.setMaxAccess(_J)
if mibBuilder.loadTexts:csilMaxProfilePerServerAllowed.setStatus(_A)
if mibBuilder.loadTexts:csilMaxProfilePerServerAllowed.setUnits('profiles')
_CsilServerTable_Object=MibTable
csilServerTable=_CsilServerTable_Object((1,3,6,1,4,1,9,9,330,1,2,3))
if mibBuilder.loadTexts:csilServerTable.setStatus(_A)
_CsilServerEntry_Object=MibTableRow
csilServerEntry=_CsilServerEntry_Object((1,3,6,1,4,1,9,9,330,1,2,3,1))
csilServerEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:csilServerEntry.setStatus(_A)
_CsilServerIndex_Type=Unsigned32
_CsilServerIndex_Object=MibTableColumn
csilServerIndex=_CsilServerIndex_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,1),_CsilServerIndex_Type())
csilServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:csilServerIndex.setStatus(_A)
_CsilServerAddressType_Type=InetAddressType
_CsilServerAddressType_Object=MibTableColumn
csilServerAddressType=_CsilServerAddressType_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,2),_CsilServerAddressType_Type())
csilServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerAddressType.setStatus(_A)
_CsilServerAddress_Type=InetAddress
_CsilServerAddress_Object=MibTableColumn
csilServerAddress=_CsilServerAddress_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,3),_CsilServerAddress_Type())
csilServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerAddress.setStatus(_A)
_CsilServerProfileIndex_Type=Unsigned32
_CsilServerProfileIndex_Object=MibTableColumn
csilServerProfileIndex=_CsilServerProfileIndex_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,4),_CsilServerProfileIndex_Type())
csilServerProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerProfileIndex.setStatus(_A)
class _CsilServerProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('rcp',2),('ftp',3)))
_CsilServerProtocol_Type.__name__=_F
_CsilServerProtocol_Object=MibTableColumn
csilServerProtocol=_CsilServerProtocol_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,5),_CsilServerProtocol_Type())
csilServerProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerProtocol.setStatus(_A)
class _CsilServerRcpUserName_Type(SnmpAdminString):defaultValue=OctetString('')
_CsilServerRcpUserName_Type.__name__=_E
_CsilServerRcpUserName_Object=MibTableColumn
csilServerRcpUserName=_CsilServerRcpUserName_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,6),_CsilServerRcpUserName_Type())
csilServerRcpUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerRcpUserName.setStatus(_A)
class _CsilServerInterval_Type(Unsigned32):defaultValue=1440
_CsilServerInterval_Type.__name__=_G
_CsilServerInterval_Object=MibTableColumn
csilServerInterval=_CsilServerInterval_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,7),_CsilServerInterval_Type())
csilServerInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerInterval.setStatus(_A)
if mibBuilder.loadTexts:csilServerInterval.setUnits('minutes')
_CsilServerLoggingFileName_Type=SnmpAdminString
_CsilServerLoggingFileName_Object=MibTableColumn
csilServerLoggingFileName=_CsilServerLoggingFileName_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,8),_CsilServerLoggingFileName_Type())
csilServerLoggingFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerLoggingFileName.setStatus(_A)
class _CsilServerLastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',1),('noLogFile',2),('noCommand',3),('linkBlock',4),('authError',5),('addrError',6),('copying',7),('writeError',8),('success',9),('ftpError',10)))
_CsilServerLastStatus_Type.__name__=_F
_CsilServerLastStatus_Object=MibTableColumn
csilServerLastStatus=_CsilServerLastStatus_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,9),_CsilServerLastStatus_Type())
csilServerLastStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:csilServerLastStatus.setStatus(_A)
_CsilServerRowStatus_Type=RowStatus
_CsilServerRowStatus_Object=MibTableColumn
csilServerRowStatus=_CsilServerRowStatus_Object((1,3,6,1,4,1,9,9,330,1,2,3,1,10),_CsilServerRowStatus_Type())
csilServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csilServerRowStatus.setStatus(_A)
_CsilCommandConfig_ObjectIdentity=ObjectIdentity
csilCommandConfig=_CsilCommandConfig_ObjectIdentity((1,3,6,1,4,1,9,9,330,1,3))
_CsilMaxCommandPerProfile_Type=Unsigned32
_CsilMaxCommandPerProfile_Object=MibScalar
csilMaxCommandPerProfile=_CsilMaxCommandPerProfile_Object((1,3,6,1,4,1,9,9,330,1,3,1),_CsilMaxCommandPerProfile_Type())
csilMaxCommandPerProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:csilMaxCommandPerProfile.setStatus(_A)
_CsilCommandsTable_Object=MibTable
csilCommandsTable=_CsilCommandsTable_Object((1,3,6,1,4,1,9,9,330,1,3,2))
if mibBuilder.loadTexts:csilCommandsTable.setStatus(_A)
_CsilCommandsEntry_Object=MibTableRow
csilCommandsEntry=_CsilCommandsEntry_Object((1,3,6,1,4,1,9,9,330,1,3,2,1))
csilCommandsEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:csilCommandsEntry.setStatus(_A)
_CsilCommandProfileIndex_Type=Unsigned32
_CsilCommandProfileIndex_Object=MibTableColumn
csilCommandProfileIndex=_CsilCommandProfileIndex_Object((1,3,6,1,4,1,9,9,330,1,3,2,1,1),_CsilCommandProfileIndex_Type())
csilCommandProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:csilCommandProfileIndex.setStatus(_A)
_CsilCommandIndex_Type=Unsigned32
_CsilCommandIndex_Object=MibTableColumn
csilCommandIndex=_CsilCommandIndex_Object((1,3,6,1,4,1,9,9,330,1,3,2,1,2),_CsilCommandIndex_Type())
csilCommandIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:csilCommandIndex.setStatus(_A)
class _CsilCommandString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CsilCommandString_Type.__name__=_E
_CsilCommandString_Object=MibTableColumn
csilCommandString=_CsilCommandString_Object((1,3,6,1,4,1,9,9,330,1,3,2,1,3),_CsilCommandString_Type())
csilCommandString.setMaxAccess(_C)
if mibBuilder.loadTexts:csilCommandString.setStatus(_A)
_CsilCommandExecOrder_Type=Unsigned32
_CsilCommandExecOrder_Object=MibTableColumn
csilCommandExecOrder=_CsilCommandExecOrder_Object((1,3,6,1,4,1,9,9,330,1,3,2,1,4),_CsilCommandExecOrder_Type())
csilCommandExecOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:csilCommandExecOrder.setStatus(_A)
_CsilCommandStatus_Type=RowStatus
_CsilCommandStatus_Object=MibTableColumn
csilCommandStatus=_CsilCommandStatus_Object((1,3,6,1,4,1,9,9,330,1,3,2,1,5),_CsilCommandStatus_Type())
csilCommandStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csilCommandStatus.setStatus(_A)
_CiscoSysInfoLogMIBConform_ObjectIdentity=ObjectIdentity
ciscoSysInfoLogMIBConform=_CiscoSysInfoLogMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,330,2))
_CiscoSysInfoLogMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSysInfoLogMIBCompliances=_CiscoSysInfoLogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,330,2,1))
_CiscoSysInfoLogMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSysInfoLogMIBGroups=_CiscoSysInfoLogMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,330,2,2))
csilGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,330,2,2,1))
csilGlobalConfigGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:csilGlobalConfigGroup.setStatus(_A)
csilServerConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,330,2,2,2))
csilServerConfigGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_I),(_B,_X)))
if mibBuilder.loadTexts:csilServerConfigGroup.setStatus(_A)
csilCommandConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,330,2,2,3))
csilCommandConfigGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:csilCommandConfigGroup.setStatus(_A)
csilNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,330,2,2,4))
csilNotifControlGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:csilNotifControlGroup.setStatus(_A)
csilLoggingFailNotif=NotificationType((1,3,6,1,4,1,9,9,330,0,1))
csilLoggingFailNotif.setObjects((_B,_I))
if mibBuilder.loadTexts:csilLoggingFailNotif.setStatus(_A)
csilLoggingFailNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,330,2,2,5))
csilLoggingFailNotifGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:csilLoggingFailNotifGroup.setStatus(_A)
ciscoSysInfoLogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,330,2,1,1))
ciscoSysInfoLogMIBCompliance.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciscoSysInfoLogMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSysInfoLogMIB':ciscoSysInfoLogMIB,'ciscoSysInfoLogMIBNotifs':ciscoSysInfoLogMIBNotifs,_d:csilLoggingFailNotif,'ciscoSysInfoLogMIBObjects':ciscoSysInfoLogMIBObjects,'csilGlobalConfig':csilGlobalConfig,_N:csilSysInfoLogEnabled,_c:csilSysInfoLogNotifEnabled,'csilServerConfig':csilServerConfig,_O:csilMaxServerAllowed,_P:csilMaxProfilePerServerAllowed,'csilServerTable':csilServerTable,'csilServerEntry':csilServerEntry,_K:csilServerIndex,_R:csilServerAddressType,_Q:csilServerAddress,_S:csilServerProfileIndex,_T:csilServerProtocol,_W:csilServerRcpUserName,_U:csilServerInterval,_V:csilServerLoggingFileName,_I:csilServerLastStatus,_X:csilServerRowStatus,'csilCommandConfig':csilCommandConfig,_Y:csilMaxCommandPerProfile,'csilCommandsTable':csilCommandsTable,'csilCommandsEntry':csilCommandsEntry,_L:csilCommandProfileIndex,_M:csilCommandIndex,_Z:csilCommandString,_a:csilCommandExecOrder,_b:csilCommandStatus,'ciscoSysInfoLogMIBConform':ciscoSysInfoLogMIBConform,'ciscoSysInfoLogMIBCompliances':ciscoSysInfoLogMIBCompliances,'ciscoSysInfoLogMIBCompliance':ciscoSysInfoLogMIBCompliance,'ciscoSysInfoLogMIBGroups':ciscoSysInfoLogMIBGroups,_e:csilGlobalConfigGroup,_f:csilServerConfigGroup,_g:csilCommandConfigGroup,'csilNotifControlGroup':csilNotifControlGroup,'csilLoggingFailNotifGroup':csilLoggingFailNotifGroup})