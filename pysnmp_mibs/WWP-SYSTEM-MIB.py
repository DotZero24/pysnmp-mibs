_F='read-only'
_E='TruthValue'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention',_E)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpSystemMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,2))
if mibBuilder.loadTexts:wwpSystemMIB.setRevisions(('2003-03-11 00:00','2001-04-03 17:00'))
_WwpSystemMIBObjects_ObjectIdentity=ObjectIdentity
wwpSystemMIBObjects=_WwpSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,2,1))
_WwpSystemClock_ObjectIdentity=ObjectIdentity
wwpSystemClock=_WwpSystemClock_ObjectIdentity((1,3,6,1,4,1,6141,2,2,1,1))
_WwpSysClockDateTime_Type=DateAndTime
_WwpSysClockDateTime_Object=MibScalar
wwpSysClockDateTime=_WwpSysClockDateTime_Object((1,3,6,1,4,1,6141,2,2,1,1,1),_WwpSysClockDateTime_Type())
wwpSysClockDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSysClockDateTime.setStatus(_A)
class _WwpSysClockTimeOffset_Type(Integer32):defaultValue=0
_WwpSysClockTimeOffset_Type.__name__=_C
_WwpSysClockTimeOffset_Object=MibScalar
wwpSysClockTimeOffset=_WwpSysClockTimeOffset_Object((1,3,6,1,4,1,6141,2,2,1,1,2),_WwpSysClockTimeOffset_Type())
wwpSysClockTimeOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSysClockTimeOffset.setStatus(_A)
_WwpSystemBootp_ObjectIdentity=ObjectIdentity
wwpSystemBootp=_WwpSystemBootp_ObjectIdentity((1,3,6,1,4,1,6141,2,2,1,2))
class _WwpSystemBootpMsgFreq_Type(Unsigned32):defaultValue=12;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpSystemBootpMsgFreq_Type.__name__=_D
_WwpSystemBootpMsgFreq_Object=MibScalar
wwpSystemBootpMsgFreq=_WwpSystemBootpMsgFreq_Object((1,3,6,1,4,1,6141,2,2,1,2,1),_WwpSystemBootpMsgFreq_Type())
wwpSystemBootpMsgFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemBootpMsgFreq.setStatus('deprecated')
if mibBuilder.loadTexts:wwpSystemBootpMsgFreq.setUnits('in seconds')
_WwpSystemAttr_ObjectIdentity=ObjectIdentity
wwpSystemAttr=_WwpSystemAttr_ObjectIdentity((1,3,6,1,4,1,6141,2,2,1,3))
_WwpSystemStartMacAddr_Type=MacAddress
_WwpSystemStartMacAddr_Object=MibScalar
wwpSystemStartMacAddr=_WwpSystemStartMacAddr_Object((1,3,6,1,4,1,6141,2,2,1,3,1),_WwpSystemStartMacAddr_Type())
wwpSystemStartMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpSystemStartMacAddr.setStatus(_A)
_WwpSystemDefaultGateway_Type=IpAddress
_WwpSystemDefaultGateway_Object=MibScalar
wwpSystemDefaultGateway=_WwpSystemDefaultGateway_Object((1,3,6,1,4,1,6141,2,2,1,3,2),_WwpSystemDefaultGateway_Type())
wwpSystemDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemDefaultGateway.setStatus(_A)
_WwpSystemTftpServer_Type=IpAddress
_WwpSystemTftpServer_Object=MibScalar
wwpSystemTftpServer=_WwpSystemTftpServer_Object((1,3,6,1,4,1,6141,2,2,1,3,3),_WwpSystemTftpServer_Type())
wwpSystemTftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemTftpServer.setStatus(_A)
_WwpSystemBootFile_Type=DisplayString
_WwpSystemBootFile_Object=MibScalar
wwpSystemBootFile=_WwpSystemBootFile_Object((1,3,6,1,4,1,6141,2,2,1,3,4),_WwpSystemBootFile_Type())
wwpSystemBootFile.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemBootFile.setStatus(_A)
_WwpSystemInterfaceHostName_Type=DisplayString
_WwpSystemInterfaceHostName_Object=MibScalar
wwpSystemInterfaceHostName=_WwpSystemInterfaceHostName_Object((1,3,6,1,4,1,6141,2,2,1,3,5),_WwpSystemInterfaceHostName_Type())
wwpSystemInterfaceHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemInterfaceHostName.setStatus(_A)
_WwpSystemCfg_ObjectIdentity=ObjectIdentity
wwpSystemCfg=_WwpSystemCfg_ObjectIdentity((1,3,6,1,4,1,6141,2,2,1,4))
class _WwpSystemCfgControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('save',1),('updatePasswords',2),('updateSnmpCfg',3),('mfgDefaultCfg',4)))
_WwpSystemCfgControl_Type.__name__=_C
_WwpSystemCfgControl_Object=MibScalar
wwpSystemCfgControl=_WwpSystemCfgControl_Object((1,3,6,1,4,1,6141,2,2,1,4,1),_WwpSystemCfgControl_Type())
wwpSystemCfgControl.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemCfgControl.setStatus(_A)
_WwpSystemCfgFilepath_Type=DisplayString
_WwpSystemCfgFilepath_Object=MibScalar
wwpSystemCfgFilepath=_WwpSystemCfgFilepath_Object((1,3,6,1,4,1,6141,2,2,1,4,2),_WwpSystemCfgFilepath_Type())
wwpSystemCfgFilepath.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpSystemCfgFilepath.setStatus(_A)
_WwpSystemDebug_ObjectIdentity=ObjectIdentity
wwpSystemDebug=_WwpSystemDebug_ObjectIdentity((1,3,6,1,4,1,6141,2,2,1,5))
class _WwpSystemConsolePortEnable_Type(TruthValue):defaultValue=2
_WwpSystemConsolePortEnable_Type.__name__=_E
_WwpSystemConsolePortEnable_Object=MibScalar
wwpSystemConsolePortEnable=_WwpSystemConsolePortEnable_Object((1,3,6,1,4,1,6141,2,2,1,5,1),_WwpSystemConsolePortEnable_Type())
wwpSystemConsolePortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemConsolePortEnable.setStatus(_A)
_WwpSystemMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpSystemMIBNotificationPrefix=_WwpSystemMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,2,2))
_WwpSystemMIBNotifications_ObjectIdentity=ObjectIdentity
wwpSystemMIBNotifications=_WwpSystemMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,2,2,0))
_WwpSystemMIBConformance_ObjectIdentity=ObjectIdentity
wwpSystemMIBConformance=_WwpSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,2,3))
_WwpSystemMIBCompliances_ObjectIdentity=ObjectIdentity
wwpSystemMIBCompliances=_WwpSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,2,3,1))
_WwpSystemMIBGroups_ObjectIdentity=ObjectIdentity
wwpSystemMIBGroups=_WwpSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,2,3,2))
mibBuilder.exportSymbols('WWP-SYSTEM-MIB',**{'wwpSystemMIB':wwpSystemMIB,'wwpSystemMIBObjects':wwpSystemMIBObjects,'wwpSystemClock':wwpSystemClock,'wwpSysClockDateTime':wwpSysClockDateTime,'wwpSysClockTimeOffset':wwpSysClockTimeOffset,'wwpSystemBootp':wwpSystemBootp,'wwpSystemBootpMsgFreq':wwpSystemBootpMsgFreq,'wwpSystemAttr':wwpSystemAttr,'wwpSystemStartMacAddr':wwpSystemStartMacAddr,'wwpSystemDefaultGateway':wwpSystemDefaultGateway,'wwpSystemTftpServer':wwpSystemTftpServer,'wwpSystemBootFile':wwpSystemBootFile,'wwpSystemInterfaceHostName':wwpSystemInterfaceHostName,'wwpSystemCfg':wwpSystemCfg,'wwpSystemCfgControl':wwpSystemCfgControl,'wwpSystemCfgFilepath':wwpSystemCfgFilepath,'wwpSystemDebug':wwpSystemDebug,'wwpSystemConsolePortEnable':wwpSystemConsolePortEnable,'wwpSystemMIBNotificationPrefix':wwpSystemMIBNotificationPrefix,'wwpSystemMIBNotifications':wwpSystemMIBNotifications,'wwpSystemMIBConformance':wwpSystemMIBConformance,'wwpSystemMIBCompliances':wwpSystemMIBCompliances,'wwpSystemMIBGroups':wwpSystemMIBGroups})