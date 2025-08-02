_O='nncfgEventSaveNotification'
_N='nncfgEventChangeNotification'
_M='nncfgEventIndex'
_L='not-accessible'
_K='nncfgNetOperRandomNumber'
_J='nncfgEventConfigDst'
_I='nncfgEventConfigSrc'
_H='nncfgEventConfigProtocol'
_G='TruthValue'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='CONFIG-MGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention',_G)
nnconfigMgmtMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,4))
if mibBuilder.loadTexts:nnconfigMgmtMib.setRevisions(('1900-08-16 00:00',))
class CfgMedium(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('commandSource',1),(_A,2),('flash',3),('erase-flash',4),('network',5)))
_NncfgOperations_ObjectIdentity=ObjectIdentity
nncfgOperations=_NncfgOperations_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,4,1))
_NncfgNetOperTable_Object=MibTable
nncfgNetOperTable=_NncfgNetOperTable_Object((1,3,6,1,4,1,562,73,1,1,1,4,1,1))
if mibBuilder.loadTexts:nncfgNetOperTable.setStatus(_A)
_NncfgNetOperEntry_Object=MibTableRow
nncfgNetOperEntry=_NncfgNetOperEntry_Object((1,3,6,1,4,1,562,73,1,1,1,4,1,1,1))
nncfgNetOperEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:nncfgNetOperEntry.setStatus(_A)
_NncfgNetOperRandomNumber_Type=Integer32
_NncfgNetOperRandomNumber_Object=MibTableColumn
nncfgNetOperRandomNumber=_NncfgNetOperRandomNumber_Object((1,3,6,1,4,1,562,73,1,1,1,4,1,1,1,1),_NncfgNetOperRandomNumber_Type())
nncfgNetOperRandomNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:nncfgNetOperRandomNumber.setStatus(_A)
class _NncfgNetOperCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('config',1),('save',2)))
_NncfgNetOperCommand_Type.__name__=_D
_NncfgNetOperCommand_Object=MibTableColumn
nncfgNetOperCommand=_NncfgNetOperCommand_Object((1,3,6,1,4,1,562,73,1,1,1,4,1,1,1,2),_NncfgNetOperCommand_Type())
nncfgNetOperCommand.setMaxAccess(_E)
if mibBuilder.loadTexts:nncfgNetOperCommand.setStatus(_A)
_NncfgNetOperAddress_Type=IpAddress
_NncfgNetOperAddress_Object=MibTableColumn
nncfgNetOperAddress=_NncfgNetOperAddress_Object((1,3,6,1,4,1,562,73,1,1,1,4,1,1,1,3),_NncfgNetOperAddress_Type())
nncfgNetOperAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nncfgNetOperAddress.setStatus(_A)
class _NncfgNetOperFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NncfgNetOperFileName_Type.__name__=_F
_NncfgNetOperFileName_Object=MibTableColumn
nncfgNetOperFileName=_NncfgNetOperFileName_Object((1,3,6,1,4,1,562,73,1,1,1,4,1,1,1,4),_NncfgNetOperFileName_Type())
nncfgNetOperFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:nncfgNetOperFileName.setStatus(_A)
class _NncfgNetOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('idle',0),('inProgress',1),('operationSuccess',2),('networkError',3),('fileAccessError',4),('serverAccessError',5),('fileOpenError',6),('notEnoughMemory',7),('unknownFailure',8)))
_NncfgNetOperStatus_Type.__name__=_D
_NncfgNetOperStatus_Object=MibTableColumn
nncfgNetOperStatus=_NncfgNetOperStatus_Object((1,3,6,1,4,1,562,73,1,1,1,4,1,1,1,5),_NncfgNetOperStatus_Type())
nncfgNetOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgNetOperStatus.setStatus(_A)
_NncfgMgmtEvents_ObjectIdentity=ObjectIdentity
nncfgMgmtEvents=_NncfgMgmtEvents_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,4,2))
_NncfgCurrentLastChanged_Type=TimeTicks
_NncfgCurrentLastChanged_Object=MibScalar
nncfgCurrentLastChanged=_NncfgCurrentLastChanged_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,1),_NncfgCurrentLastChanged_Type())
nncfgCurrentLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgCurrentLastChanged.setStatus(_A)
_NncfgCurrentLastSaved_Type=TimeTicks
_NncfgCurrentLastSaved_Object=MibScalar
nncfgCurrentLastSaved=_NncfgCurrentLastSaved_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,2),_NncfgCurrentLastSaved_Type())
nncfgCurrentLastSaved.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgCurrentLastSaved.setStatus(_A)
class _NncfgMaxEvents_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_NncfgMaxEvents_Type.__name__=_D
_NncfgMaxEvents_Object=MibScalar
nncfgMaxEvents=_NncfgMaxEvents_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,3),_NncfgMaxEvents_Type())
nncfgMaxEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgMaxEvents.setStatus(_A)
_NncfgEventTable_Object=MibTable
nncfgEventTable=_NncfgEventTable_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4))
if mibBuilder.loadTexts:nncfgEventTable.setStatus(_A)
_NncfgEventEntry_Object=MibTableRow
nncfgEventEntry=_NncfgEventEntry_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1))
nncfgEventEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:nncfgEventEntry.setStatus(_A)
class _NncfgEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_NncfgEventIndex_Type.__name__=_D
_NncfgEventIndex_Object=MibTableColumn
nncfgEventIndex=_NncfgEventIndex_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,1),_NncfgEventIndex_Type())
nncfgEventIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:nncfgEventIndex.setStatus(_A)
_NncfgEventTime_Type=TimeTicks
_NncfgEventTime_Object=MibTableColumn
nncfgEventTime=_NncfgEventTime_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,2),_NncfgEventTime_Type())
nncfgEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventTime.setStatus(_A)
class _NncfgEventConfigProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commandLine',1),('snmp',2),('http',3)))
_NncfgEventConfigProtocol_Type.__name__=_D
_NncfgEventConfigProtocol_Object=MibTableColumn
nncfgEventConfigProtocol=_NncfgEventConfigProtocol_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,3),_NncfgEventConfigProtocol_Type())
nncfgEventConfigProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventConfigProtocol.setStatus(_A)
_NncfgEventConfigSrc_Type=CfgMedium
_NncfgEventConfigSrc_Object=MibTableColumn
nncfgEventConfigSrc=_NncfgEventConfigSrc_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,4),_NncfgEventConfigSrc_Type())
nncfgEventConfigSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventConfigSrc.setStatus(_A)
_NncfgEventConfigDst_Type=CfgMedium
_NncfgEventConfigDst_Object=MibTableColumn
nncfgEventConfigDst=_NncfgEventConfigDst_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,5),_NncfgEventConfigDst_Type())
nncfgEventConfigDst.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventConfigDst.setStatus(_A)
class _NncfgEventLoginType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('console',2),('telnet',3),('rlogin',4),('dial',5),('other',6)))
_NncfgEventLoginType_Type.__name__=_D
_NncfgEventLoginType_Object=MibTableColumn
nncfgEventLoginType=_NncfgEventLoginType_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,6),_NncfgEventLoginType_Type())
nncfgEventLoginType.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventLoginType.setStatus(_A)
class _NncfgEventTerminalUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NncfgEventTerminalUser_Type.__name__=_F
_NncfgEventTerminalUser_Object=MibTableColumn
nncfgEventTerminalUser=_NncfgEventTerminalUser_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,7),_NncfgEventTerminalUser_Type())
nncfgEventTerminalUser.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventTerminalUser.setStatus(_A)
_NncfgEventConfigSrcAddress_Type=IpAddress
_NncfgEventConfigSrcAddress_Object=MibTableColumn
nncfgEventConfigSrcAddress=_NncfgEventConfigSrcAddress_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,8),_NncfgEventConfigSrcAddress_Type())
nncfgEventConfigSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventConfigSrcAddress.setStatus(_A)
class _NncfgEventFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NncfgEventFileName_Type.__name__=_F
_NncfgEventFileName_Object=MibTableColumn
nncfgEventFileName=_NncfgEventFileName_Object((1,3,6,1,4,1,562,73,1,1,1,4,2,4,1,9),_NncfgEventFileName_Type())
nncfgEventFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:nncfgEventFileName.setStatus(_A)
_NncfgNotificationEnables_ObjectIdentity=ObjectIdentity
nncfgNotificationEnables=_NncfgNotificationEnables_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,4,3))
class _NncfgEnableChangeNotification_Type(TruthValue):defaultValue=1
_NncfgEnableChangeNotification_Type.__name__=_G
_NncfgEnableChangeNotification_Object=MibScalar
nncfgEnableChangeNotification=_NncfgEnableChangeNotification_Object((1,3,6,1,4,1,562,73,1,1,1,4,3,1),_NncfgEnableChangeNotification_Type())
nncfgEnableChangeNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:nncfgEnableChangeNotification.setStatus(_A)
class _NncfgEnableSaveNotification_Type(TruthValue):defaultValue=1
_NncfgEnableSaveNotification_Type.__name__=_G
_NncfgEnableSaveNotification_Object=MibScalar
nncfgEnableSaveNotification=_NncfgEnableSaveNotification_Object((1,3,6,1,4,1,562,73,1,1,1,4,3,2),_NncfgEnableSaveNotification_Type())
nncfgEnableSaveNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:nncfgEnableSaveNotification.setStatus(_A)
_NncfgMgmtNotifications_ObjectIdentity=ObjectIdentity
nncfgMgmtNotifications=_NncfgMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,4,4))
_NncfgMgmtTraps_ObjectIdentity=ObjectIdentity
nncfgMgmtTraps=_NncfgMgmtTraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,4,4,0))
nncfgEventChangeNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,4,4,0,1))
nncfgEventChangeNotification.setObjects(*((_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:nncfgEventChangeNotification.setStatus(_A)
nncfgEventSaveNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,4,4,0,2))
nncfgEventSaveNotification.setObjects(*((_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:nncfgEventSaveNotification.setStatus(_A)
nnconfigMgmtNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,73,1,1,1,4,5))
nnconfigMgmtNotificationGroup.setObjects(*((_C,_N),(_C,_O)))
if mibBuilder.loadTexts:nnconfigMgmtNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'CfgMedium':CfgMedium,'nnconfigMgmtMib':nnconfigMgmtMib,'nncfgOperations':nncfgOperations,'nncfgNetOperTable':nncfgNetOperTable,'nncfgNetOperEntry':nncfgNetOperEntry,_K:nncfgNetOperRandomNumber,'nncfgNetOperCommand':nncfgNetOperCommand,'nncfgNetOperAddress':nncfgNetOperAddress,'nncfgNetOperFileName':nncfgNetOperFileName,'nncfgNetOperStatus':nncfgNetOperStatus,'nncfgMgmtEvents':nncfgMgmtEvents,'nncfgCurrentLastChanged':nncfgCurrentLastChanged,'nncfgCurrentLastSaved':nncfgCurrentLastSaved,'nncfgMaxEvents':nncfgMaxEvents,'nncfgEventTable':nncfgEventTable,'nncfgEventEntry':nncfgEventEntry,_M:nncfgEventIndex,'nncfgEventTime':nncfgEventTime,_H:nncfgEventConfigProtocol,_I:nncfgEventConfigSrc,_J:nncfgEventConfigDst,'nncfgEventLoginType':nncfgEventLoginType,'nncfgEventTerminalUser':nncfgEventTerminalUser,'nncfgEventConfigSrcAddress':nncfgEventConfigSrcAddress,'nncfgEventFileName':nncfgEventFileName,'nncfgNotificationEnables':nncfgNotificationEnables,'nncfgEnableChangeNotification':nncfgEnableChangeNotification,'nncfgEnableSaveNotification':nncfgEnableSaveNotification,'nncfgMgmtNotifications':nncfgMgmtNotifications,'nncfgMgmtTraps':nncfgMgmtTraps,_N:nncfgEventChangeNotification,_O:nncfgEventSaveNotification,'nnconfigMgmtNotificationGroup':nnconfigMgmtNotificationGroup})