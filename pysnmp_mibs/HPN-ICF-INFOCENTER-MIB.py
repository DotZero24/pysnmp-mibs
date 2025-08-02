_Q='ICFacilityType'
_P='hpnicfICLoghostIndex'
_O='hpnicfICLogbufferContIndex'
_N='TruthValue'
_M='Integer32'
_L='InetAddressType'
_K='hpnicfICModuleName'
_J='hpnicfICDirectionIndex'
_I='ICTimeStampType'
_H='not-accessible'
_G='Unsigned32'
_F='DisplayString'
_E='read-write'
_D='HPN-ICF-INFOCENTER-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TAddress','TextualConvention',_N)
hpnicfInfoCenter=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119))
if mibBuilder.loadTexts:hpnicfInfoCenter.setRevisions(('2012-03-07 19:00',))
class ICMessageLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('informational',6),('debug',7),('invalid',8)))
class ICFacilityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('userLevel',1),('mailSystem',2),('systemDaemons',3),('securityAuthorization',4),('internallyMessages',5),('linePrinter',6),('networkNews',7),('uucp',8),('clockDaemon',9),('securityAuthorization2',10),('ftpDaemon',11),('ntp',12),('logAudit',13),('logAlert',14),('clockDaemon2',15),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
class ICTimeStampType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('date',0),('boot',1),('iso',2),('dateWithoutYear',3),('none',4)))
_HpnicfICLogbuffer_ObjectIdentity=ObjectIdentity
hpnicfICLogbuffer=_HpnicfICLogbuffer_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,1))
_HpnicfICLogbufferObjects_ObjectIdentity=ObjectIdentity
hpnicfICLogbufferObjects=_HpnicfICLogbufferObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,1,1))
_HpnicfICMaxLogbufferSize_Type=Unsigned32
_HpnicfICMaxLogbufferSize_Object=MibScalar
hpnicfICMaxLogbufferSize=_HpnicfICMaxLogbufferSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,1,1),_HpnicfICMaxLogbufferSize_Type())
hpnicfICMaxLogbufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICMaxLogbufferSize.setStatus(_A)
class _HpnicfICLogbufferSize_Type(Unsigned32):defaultValue=512
_HpnicfICLogbufferSize_Type.__name__=_G
_HpnicfICLogbufferSize_Object=MibScalar
hpnicfICLogbufferSize=_HpnicfICLogbufferSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,1,2),_HpnicfICLogbufferSize_Type())
hpnicfICLogbufferSize.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfICLogbufferSize.setStatus(_A)
_HpnicfICLogbufferCurrentMessages_Type=Unsigned32
_HpnicfICLogbufferCurrentMessages_Object=MibScalar
hpnicfICLogbufferCurrentMessages=_HpnicfICLogbufferCurrentMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,1,3),_HpnicfICLogbufferCurrentMessages_Type())
hpnicfICLogbufferCurrentMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICLogbufferCurrentMessages.setStatus(_A)
_HpnicfICLogbufferOverwrittenMessages_Type=Counter32
_HpnicfICLogbufferOverwrittenMessages_Object=MibScalar
hpnicfICLogbufferOverwrittenMessages=_HpnicfICLogbufferOverwrittenMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,1,4),_HpnicfICLogbufferOverwrittenMessages_Type())
hpnicfICLogbufferOverwrittenMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICLogbufferOverwrittenMessages.setStatus(_A)
_HpnicfICLogbufferDroppedMessages_Type=Counter32
_HpnicfICLogbufferDroppedMessages_Object=MibScalar
hpnicfICLogbufferDroppedMessages=_HpnicfICLogbufferDroppedMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,1,5),_HpnicfICLogbufferDroppedMessages_Type())
hpnicfICLogbufferDroppedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICLogbufferDroppedMessages.setStatus(_A)
_HpnicfICLogbufferContTable_Object=MibTable
hpnicfICLogbufferContTable=_HpnicfICLogbufferContTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,2))
if mibBuilder.loadTexts:hpnicfICLogbufferContTable.setStatus(_A)
_HpnicfICLogbufferContEntry_Object=MibTableRow
hpnicfICLogbufferContEntry=_HpnicfICLogbufferContEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,2,1))
hpnicfICLogbufferContEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:hpnicfICLogbufferContEntry.setStatus(_A)
class _HpnicfICLogbufferContIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfICLogbufferContIndex_Type.__name__=_M
_HpnicfICLogbufferContIndex_Object=MibTableColumn
hpnicfICLogbufferContIndex=_HpnicfICLogbufferContIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,2,1,1),_HpnicfICLogbufferContIndex_Type())
hpnicfICLogbufferContIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfICLogbufferContIndex.setStatus(_A)
class _HpnicfICLogbufferContDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1600))
_HpnicfICLogbufferContDescription_Type.__name__=_F
_HpnicfICLogbufferContDescription_Object=MibTableColumn
hpnicfICLogbufferContDescription=_HpnicfICLogbufferContDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,1,2,1,2),_HpnicfICLogbufferContDescription_Type())
hpnicfICLogbufferContDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICLogbufferContDescription.setStatus(_A)
_HpnicfICLoghost_ObjectIdentity=ObjectIdentity
hpnicfICLoghost=_HpnicfICLoghost_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,2))
_HpnicfICLoghostObjects_ObjectIdentity=ObjectIdentity
hpnicfICLoghostObjects=_HpnicfICLoghostObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,2,1))
_HpnicfICMaxLoghost_Type=Unsigned32
_HpnicfICMaxLoghost_Object=MibScalar
hpnicfICMaxLoghost=_HpnicfICMaxLoghost_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,1,1),_HpnicfICMaxLoghost_Type())
hpnicfICMaxLoghost.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICMaxLoghost.setStatus(_A)
_HpnicfICLoghostSourceInterface_Type=InterfaceIndexOrZero
_HpnicfICLoghostSourceInterface_Object=MibScalar
hpnicfICLoghostSourceInterface=_HpnicfICLoghostSourceInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,1,2),_HpnicfICLoghostSourceInterface_Type())
hpnicfICLoghostSourceInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfICLoghostSourceInterface.setStatus(_A)
class _HpnicfICLoghostTimestampType_Type(ICTimeStampType):defaultValue=0
_HpnicfICLoghostTimestampType_Type.__name__=_I
_HpnicfICLoghostTimestampType_Object=MibScalar
hpnicfICLoghostTimestampType=_HpnicfICLoghostTimestampType_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,1,3),_HpnicfICLoghostTimestampType_Type())
hpnicfICLoghostTimestampType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfICLoghostTimestampType.setStatus(_A)
_HpnicfICLoghostTable_Object=MibTable
hpnicfICLoghostTable=_HpnicfICLoghostTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2))
if mibBuilder.loadTexts:hpnicfICLoghostTable.setStatus(_A)
_HpnicfICLoghostEntry_Object=MibTableRow
hpnicfICLoghostEntry=_HpnicfICLoghostEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1))
hpnicfICLoghostEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:hpnicfICLoghostEntry.setStatus(_A)
class _HpnicfICLoghostIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfICLoghostIndex_Type.__name__=_G
_HpnicfICLoghostIndex_Object=MibTableColumn
hpnicfICLoghostIndex=_HpnicfICLoghostIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,1),_HpnicfICLoghostIndex_Type())
hpnicfICLoghostIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfICLoghostIndex.setStatus(_A)
class _HpnicfICLoghostIpaddressType_Type(InetAddressType):defaultValue=1
_HpnicfICLoghostIpaddressType_Type.__name__=_L
_HpnicfICLoghostIpaddressType_Object=MibTableColumn
hpnicfICLoghostIpaddressType=_HpnicfICLoghostIpaddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,2),_HpnicfICLoghostIpaddressType_Type())
hpnicfICLoghostIpaddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLoghostIpaddressType.setStatus(_A)
_HpnicfICLoghostIpaddress_Type=InetAddress
_HpnicfICLoghostIpaddress_Object=MibTableColumn
hpnicfICLoghostIpaddress=_HpnicfICLoghostIpaddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,3),_HpnicfICLoghostIpaddress_Type())
hpnicfICLoghostIpaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLoghostIpaddress.setStatus(_A)
class _HpnicfICLoghostVPNName_Type(DisplayString):defaultValue=OctetString('')
_HpnicfICLoghostVPNName_Type.__name__=_F
_HpnicfICLoghostVPNName_Object=MibTableColumn
hpnicfICLoghostVPNName=_HpnicfICLoghostVPNName_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,4),_HpnicfICLoghostVPNName_Type())
hpnicfICLoghostVPNName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLoghostVPNName.setStatus(_A)
class _HpnicfICLoghostFacility_Type(ICFacilityType):defaultValue=23
_HpnicfICLoghostFacility_Type.__name__=_Q
_HpnicfICLoghostFacility_Object=MibTableColumn
hpnicfICLoghostFacility=_HpnicfICLoghostFacility_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,5),_HpnicfICLoghostFacility_Type())
hpnicfICLoghostFacility.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLoghostFacility.setStatus(_A)
_HpnicfICLoghostOperateRowStatus_Type=RowStatus
_HpnicfICLoghostOperateRowStatus_Object=MibTableColumn
hpnicfICLoghostOperateRowStatus=_HpnicfICLoghostOperateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,6),_HpnicfICLoghostOperateRowStatus_Type())
hpnicfICLoghostOperateRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLoghostOperateRowStatus.setStatus(_A)
class _HpnicfICLoghostIpaddressPort_Type(Unsigned32):defaultValue=514;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfICLoghostIpaddressPort_Type.__name__=_G
_HpnicfICLoghostIpaddressPort_Object=MibTableColumn
hpnicfICLoghostIpaddressPort=_HpnicfICLoghostIpaddressPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,7),_HpnicfICLoghostIpaddressPort_Type())
hpnicfICLoghostIpaddressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLoghostIpaddressPort.setStatus(_A)
_HpnicfICLoghostTAddress_Type=TAddress
_HpnicfICLoghostTAddress_Object=MibTableColumn
hpnicfICLoghostTAddress=_HpnicfICLoghostTAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,2,2,1,8),_HpnicfICLoghostTAddress_Type())
hpnicfICLoghostTAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLoghostTAddress.setStatus(_A)
_HpnicfICDirection_ObjectIdentity=ObjectIdentity
hpnicfICDirection=_HpnicfICDirection_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,3))
_HpnicfICDirectionTable_Object=MibTable
hpnicfICDirectionTable=_HpnicfICDirectionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,3,1))
if mibBuilder.loadTexts:hpnicfICDirectionTable.setStatus(_A)
_HpnicfICDirectionEntry_Object=MibTableRow
hpnicfICDirectionEntry=_HpnicfICDirectionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,3,1,1))
hpnicfICDirectionEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfICDirectionEntry.setStatus(_A)
_HpnicfICDirectionIndex_Type=Unsigned32
_HpnicfICDirectionIndex_Object=MibTableColumn
hpnicfICDirectionIndex=_HpnicfICDirectionIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,3,1,1,1),_HpnicfICDirectionIndex_Type())
hpnicfICDirectionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfICDirectionIndex.setStatus(_A)
class _HpnicfICDirectionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_HpnicfICDirectionName_Type.__name__=_F
_HpnicfICDirectionName_Object=MibTableColumn
hpnicfICDirectionName=_HpnicfICDirectionName_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,3,1,1,2),_HpnicfICDirectionName_Type())
hpnicfICDirectionName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICDirectionName.setStatus(_A)
_HpnicfICDirectionState_Type=TruthValue
_HpnicfICDirectionState_Object=MibTableColumn
hpnicfICDirectionState=_HpnicfICDirectionState_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,3,1,1,3),_HpnicfICDirectionState_Type())
hpnicfICDirectionState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfICDirectionState.setStatus(_A)
_HpnicfICModule_ObjectIdentity=ObjectIdentity
hpnicfICModule=_HpnicfICModule_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,4))
_HpnicfICModuleTable_Object=MibTable
hpnicfICModuleTable=_HpnicfICModuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,4,1))
if mibBuilder.loadTexts:hpnicfICModuleTable.setStatus(_A)
_HpnicfICModuleEntry_Object=MibTableRow
hpnicfICModuleEntry=_HpnicfICModuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,4,1,1))
hpnicfICModuleEntry.setIndexNames((1,_D,_K))
if mibBuilder.loadTexts:hpnicfICModuleEntry.setStatus(_A)
class _HpnicfICModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_HpnicfICModuleName_Type.__name__=_F
_HpnicfICModuleName_Object=MibTableColumn
hpnicfICModuleName=_HpnicfICModuleName_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,4,1,1,1),_HpnicfICModuleName_Type())
hpnicfICModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfICModuleName.setStatus(_A)
_HpnicfICLog_ObjectIdentity=ObjectIdentity
hpnicfICLog=_HpnicfICLog_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,5))
_HpnicfICLogObjects_ObjectIdentity=ObjectIdentity
hpnicfICLogObjects=_HpnicfICLogObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,119,5,1))
class _HpnicfICLogGlobalState_Type(TruthValue):defaultValue=1
_HpnicfICLogGlobalState_Type.__name__=_N
_HpnicfICLogGlobalState_Object=MibScalar
hpnicfICLogGlobalState=_HpnicfICLogGlobalState_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,5,1,1),_HpnicfICLogGlobalState_Type())
hpnicfICLogGlobalState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfICLogGlobalState.setStatus(_A)
class _HpnicfICLogTimestampType_Type(ICTimeStampType):defaultValue=0
_HpnicfICLogTimestampType_Type.__name__=_I
_HpnicfICLogTimestampType_Object=MibScalar
hpnicfICLogTimestampType=_HpnicfICLogTimestampType_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,5,1,2),_HpnicfICLogTimestampType_Type())
hpnicfICLogTimestampType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfICLogTimestampType.setStatus(_A)
_HpnicfICLogTable_Object=MibTable
hpnicfICLogTable=_HpnicfICLogTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,5,2))
if mibBuilder.loadTexts:hpnicfICLogTable.setStatus(_A)
_HpnicfICLogEntry_Object=MibTableRow
hpnicfICLogEntry=_HpnicfICLogEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,5,2,1))
hpnicfICLogEntry.setIndexNames((0,_D,_J),(1,_D,_K))
if mibBuilder.loadTexts:hpnicfICLogEntry.setStatus(_A)
_HpnicfICLogLevel_Type=ICMessageLevelType
_HpnicfICLogLevel_Object=MibTableColumn
hpnicfICLogLevel=_HpnicfICLogLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,5,2,1,1),_HpnicfICLogLevel_Type())
hpnicfICLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLogLevel.setStatus(_A)
_HpnicfICLogRowStatus_Type=RowStatus
_HpnicfICLogRowStatus_Object=MibTableColumn
hpnicfICLogRowStatus=_HpnicfICLogRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,119,5,2,1,2),_HpnicfICLogRowStatus_Type())
hpnicfICLogRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfICLogRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ICMessageLevelType':ICMessageLevelType,_Q:ICFacilityType,_I:ICTimeStampType,'hpnicfInfoCenter':hpnicfInfoCenter,'hpnicfICLogbuffer':hpnicfICLogbuffer,'hpnicfICLogbufferObjects':hpnicfICLogbufferObjects,'hpnicfICMaxLogbufferSize':hpnicfICMaxLogbufferSize,'hpnicfICLogbufferSize':hpnicfICLogbufferSize,'hpnicfICLogbufferCurrentMessages':hpnicfICLogbufferCurrentMessages,'hpnicfICLogbufferOverwrittenMessages':hpnicfICLogbufferOverwrittenMessages,'hpnicfICLogbufferDroppedMessages':hpnicfICLogbufferDroppedMessages,'hpnicfICLogbufferContTable':hpnicfICLogbufferContTable,'hpnicfICLogbufferContEntry':hpnicfICLogbufferContEntry,_O:hpnicfICLogbufferContIndex,'hpnicfICLogbufferContDescription':hpnicfICLogbufferContDescription,'hpnicfICLoghost':hpnicfICLoghost,'hpnicfICLoghostObjects':hpnicfICLoghostObjects,'hpnicfICMaxLoghost':hpnicfICMaxLoghost,'hpnicfICLoghostSourceInterface':hpnicfICLoghostSourceInterface,'hpnicfICLoghostTimestampType':hpnicfICLoghostTimestampType,'hpnicfICLoghostTable':hpnicfICLoghostTable,'hpnicfICLoghostEntry':hpnicfICLoghostEntry,_P:hpnicfICLoghostIndex,'hpnicfICLoghostIpaddressType':hpnicfICLoghostIpaddressType,'hpnicfICLoghostIpaddress':hpnicfICLoghostIpaddress,'hpnicfICLoghostVPNName':hpnicfICLoghostVPNName,'hpnicfICLoghostFacility':hpnicfICLoghostFacility,'hpnicfICLoghostOperateRowStatus':hpnicfICLoghostOperateRowStatus,'hpnicfICLoghostIpaddressPort':hpnicfICLoghostIpaddressPort,'hpnicfICLoghostTAddress':hpnicfICLoghostTAddress,'hpnicfICDirection':hpnicfICDirection,'hpnicfICDirectionTable':hpnicfICDirectionTable,'hpnicfICDirectionEntry':hpnicfICDirectionEntry,_J:hpnicfICDirectionIndex,'hpnicfICDirectionName':hpnicfICDirectionName,'hpnicfICDirectionState':hpnicfICDirectionState,'hpnicfICModule':hpnicfICModule,'hpnicfICModuleTable':hpnicfICModuleTable,'hpnicfICModuleEntry':hpnicfICModuleEntry,_K:hpnicfICModuleName,'hpnicfICLog':hpnicfICLog,'hpnicfICLogObjects':hpnicfICLogObjects,'hpnicfICLogGlobalState':hpnicfICLogGlobalState,'hpnicfICLogTimestampType':hpnicfICLogTimestampType,'hpnicfICLogTable':hpnicfICLogTable,'hpnicfICLogEntry':hpnicfICLogEntry,'hpnicfICLogLevel':hpnicfICLogLevel,'hpnicfICLogRowStatus':hpnicfICLogRowStatus})