_G='tmnxLogApExtnEntry'
_F='TIMETRA-SAS-LOG-MIB'
_E='TruthValue'
_D='Integer32'
_C='SnmpAdminString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,SnmpMessageProcessingModel,SnmpSecurityLevel=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C,'SnmpMessageProcessingModel','SnmpSecurityLevel')
snmpNotifyEntry,=mibBuilder.importSymbols('SNMP-NOTIFICATION-MIB','snmpNotifyEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysDescr,sysObjectID=mibBuilder.importSymbols('SNMPv2-MIB','sysDescr','sysObjectID')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_E)
TFilterAction,TFilterActionOrDefault=mibBuilder.importSymbols('TIMETRA-FILTER-MIB','TFilterAction','TFilterActionOrDefault')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxLogIdIndex,tmnxLogApEntry,tmnxSnmpTrapDestEntry=mibBuilder.importSymbols('TIMETRA-LOG-MIB','TmnxLogIdIndex','tmnxLogApEntry','tmnxSnmpTrapDestEntry')
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
THsmdaCounterIdOrZero,THsmdaCounterIdOrZeroOrAll,TItemDescription,TNamedItem,TNamedItemOrEmpty,TQueueId,TQueueIdOrAll,TmnxAccPlcyAACounters,TmnxAccPlcyOECounters,TmnxAccPlcyOICounters,TmnxAccPlcyQECounters,TmnxAccPlcyQICounters,TmnxActionType,TmnxAdminState,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB','THsmdaCounterIdOrZero','THsmdaCounterIdOrZeroOrAll','TItemDescription','TNamedItem','TNamedItemOrEmpty','TQueueId','TQueueIdOrAll','TmnxAccPlcyAACounters','TmnxAccPlcyOECounters','TmnxAccPlcyOICounters','TmnxAccPlcyQECounters','TmnxAccPlcyQICounters','TmnxActionType','TmnxAdminState','TmnxOperState')
timetraSASLogMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,14))
if mibBuilder.loadTexts:timetraSASLogMIBModule.setRevisions(('1911-08-01 00:00',))
class TLogMemSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TmnxSASLogConformance_ObjectIdentity=ObjectIdentity
tmnxSASLogConformance=_TmnxSASLogConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,9))
_TmnxSASLogGroups_ObjectIdentity=ObjectIdentity
tmnxSASLogGroups=_TmnxSASLogGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,9,1))
_TmnxSASLogObjs_ObjectIdentity=ObjectIdentity
tmnxSASLogObjs=_TmnxSASLogObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,14))
_TmnxSASLogGlobObjs_ObjectIdentity=ObjectIdentity
tmnxSASLogGlobObjs=_TmnxSASLogGlobObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,14,1))
class _TmnxDygGaspPriLogId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TmnxDygGaspPriLogId_Type.__name__=_D
_TmnxDygGaspPriLogId_Object=MibScalar
tmnxDygGaspPriLogId=_TmnxDygGaspPriLogId_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,1),_TmnxDygGaspPriLogId_Type())
tmnxDygGaspPriLogId.setMaxAccess(_B)
if mibBuilder.loadTexts:tmnxDygGaspPriLogId.setStatus(_A)
class _TmnxDygGaspPriTgtName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,28))
_TmnxDygGaspPriTgtName_Type.__name__=_C
_TmnxDygGaspPriTgtName_Object=MibScalar
tmnxDygGaspPriTgtName=_TmnxDygGaspPriTgtName_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,2),_TmnxDygGaspPriTgtName_Type())
tmnxDygGaspPriTgtName.setMaxAccess(_B)
if mibBuilder.loadTexts:tmnxDygGaspPriTgtName.setStatus(_A)
class _TmnxDygGaspSecLogId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TmnxDygGaspSecLogId_Type.__name__=_D
_TmnxDygGaspSecLogId_Object=MibScalar
tmnxDygGaspSecLogId=_TmnxDygGaspSecLogId_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,3),_TmnxDygGaspSecLogId_Type())
tmnxDygGaspSecLogId.setMaxAccess(_B)
if mibBuilder.loadTexts:tmnxDygGaspSecLogId.setStatus(_A)
class _TmnxDygGaspSecTgtName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,28))
_TmnxDygGaspSecTgtName_Type.__name__=_C
_TmnxDygGaspSecTgtName_Object=MibScalar
tmnxDygGaspSecTgtName=_TmnxDygGaspSecTgtName_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,4),_TmnxDygGaspSecTgtName_Type())
tmnxDygGaspSecTgtName.setMaxAccess(_B)
if mibBuilder.loadTexts:tmnxDygGaspSecTgtName.setStatus(_A)
class _TmnxDygGaspTerLogId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TmnxDygGaspTerLogId_Type.__name__=_D
_TmnxDygGaspTerLogId_Object=MibScalar
tmnxDygGaspTerLogId=_TmnxDygGaspTerLogId_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,5),_TmnxDygGaspTerLogId_Type())
tmnxDygGaspTerLogId.setMaxAccess(_B)
if mibBuilder.loadTexts:tmnxDygGaspTerLogId.setStatus(_A)
class _TmnxDygGaspTerTgtName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,28))
_TmnxDygGaspTerTgtName_Type.__name__=_C
_TmnxDygGaspTerTgtName_Object=MibScalar
tmnxDygGaspTerTgtName=_TmnxDygGaspTerTgtName_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,6),_TmnxDygGaspTerTgtName_Type())
tmnxDygGaspTerTgtName.setMaxAccess(_B)
if mibBuilder.loadTexts:tmnxDygGaspTerTgtName.setStatus(_A)
_TmnxLogApExtnTable_Object=MibTable
tmnxLogApExtnTable=_TmnxLogApExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,7))
if mibBuilder.loadTexts:tmnxLogApExtnTable.setStatus(_A)
_TmnxLogApExtnEntry_Object=MibTableRow
tmnxLogApExtnEntry=_TmnxLogApExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,7,1))
if mibBuilder.loadTexts:tmnxLogApExtnEntry.setStatus(_A)
class _TmnxLogApLogMemory_Type(TruthValue):defaultValue=2
_TmnxLogApLogMemory_Type.__name__=_E
_TmnxLogApLogMemory_Object=MibTableColumn
tmnxLogApLogMemory=_TmnxLogApLogMemory_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,7,1,1),_TmnxLogApLogMemory_Type())
tmnxLogApLogMemory.setMaxAccess('read-create')
if mibBuilder.loadTexts:tmnxLogApLogMemory.setStatus(_A)
_TmnxLogApLogMemSize_Type=TLogMemSize
_TmnxLogApLogMemSize_Object=MibTableColumn
tmnxLogApLogMemSize=_TmnxLogApLogMemSize_Object((1,3,6,1,4,1,6527,6,2,2,2,14,1,7,1,2),_TmnxLogApLogMemSize_Type())
tmnxLogApLogMemSize.setMaxAccess('read-only')
if mibBuilder.loadTexts:tmnxLogApLogMemSize.setStatus(_A)
tmnxLogApEntry.registerAugmentions((_F,_G))
tmnxLogApExtnEntry.setIndexNames(*tmnxLogApEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'TLogMemSize':TLogMemSize,'timetraSASLogMIBModule':timetraSASLogMIBModule,'tmnxSASLogConformance':tmnxSASLogConformance,'tmnxSASLogGroups':tmnxSASLogGroups,'tmnxSASLogObjs':tmnxSASLogObjs,'tmnxSASLogGlobObjs':tmnxSASLogGlobObjs,'tmnxDygGaspPriLogId':tmnxDygGaspPriLogId,'tmnxDygGaspPriTgtName':tmnxDygGaspPriTgtName,'tmnxDygGaspSecLogId':tmnxDygGaspSecLogId,'tmnxDygGaspSecTgtName':tmnxDygGaspSecTgtName,'tmnxDygGaspTerLogId':tmnxDygGaspTerLogId,'tmnxDygGaspTerTgtName':tmnxDygGaspTerTgtName,'tmnxLogApExtnTable':tmnxLogApExtnTable,_G:tmnxLogApExtnEntry,'tmnxLogApLogMemory':tmnxLogApLogMemory,'tmnxLogApLogMemSize':tmnxLogApLogMemSize})