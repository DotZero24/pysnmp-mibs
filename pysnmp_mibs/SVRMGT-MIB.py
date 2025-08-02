_a='svrThrResetValue'
_Z='svrControlModifyOID'
_Y='svrTrapDestinationIndex'
_X='svrThrIndex'
_W='not-accessible'
_V='lessThan'
_U='lessThanOrEqualTo'
_T='equalTo'
_S='greaterThanOrEqualTo'
_R='greaterThan'
_Q='unknown'
_P='svrTrapCommunityIndex'
_O='Integer32'
_N='read-only'
_M='svrThrThresholdValue'
_L='svrThrLastValue'
_K='svrThrValueType'
_J='svrThrSeverity'
_I='svrThrCreatedBy'
_H='svrThrAlarmCategory'
_G='svrThrUserDefinedTrapData'
_F='svrThrManagerDefinedTrapData'
_E='svrThrDescr'
_D='svrThrVariableName'
_C='read-write'
_B='mandatory'
_A='SVRMGT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class Boolean(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
class SnmpErrors(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noError',1),('tooBig',2),('readonly',3),('genericError',4),('noSuchName',5),('badValue',6)))
class Severity(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('high',1),('medium',2),('low',3),('informational',4)))
class AlarmCategory(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)));namedValues=NamedValues(*((_Q,1),('other',2),('processorStatus',3),('diskStatus',4),('fanStatus',5),('voltageStatus',6),('powerSupplyStatus',7),('temperatureStatus',8),('memoryStatus',9),('fileUsage',10),('temperatureReading',11),('cpuUsage',12),('networkInboundErrors',13),('networkOutboundErrors',14),('networkInboundPackets',15),('networkOutboundPackets',16),('networkInboundDiscards',17),('networkOutboundDiscards',18),('networkInboundUnicastPackets',19),('networkOutboundUnicastPackets',20),('networkInboundNonUnicastPackets',21),('networkOutboundNonUnicastPackets',22),('networkInboundOctets',23),('networkOutboundOctets',24),('networkUnknownProtocol',25),('voltageReading',26),('clusterGroupStatus',27),('secureBoxStatus',28),('secureBoxBreakInCount',29)))
class ResetRelationalOperators(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5),('notEqualTo',6)))
class ThresholdOwner(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Q,1),('other',2),('serverWorks',3),('serverWorksMinimalHealth',4),('netView',5),('openView',6),('uniCenter',7),('distributedMonitor',8),('bmcPatrol',9),('eminate',10)))
_Dec_ObjectIdentity=ObjectIdentity
dec=_Dec_ObjectIdentity((1,3,6,1,4,1,36))
_Ema_ObjectIdentity=ObjectIdentity
ema=_Ema_ObjectIdentity((1,3,6,1,4,1,36,2))
_Mib_extensions_1_ObjectIdentity=ObjectIdentity
mib_extensions_1=_Mib_extensions_1_ObjectIdentity((1,3,6,1,4,1,36,2,18))
_SvrSystem_ObjectIdentity=ObjectIdentity
svrSystem=_SvrSystem_ObjectIdentity((1,3,6,1,4,1,36,2,18,22))
_SvrMgt_ObjectIdentity=ObjectIdentity
svrMgt=_SvrMgt_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,2))
_SvrMgtMibInfo_ObjectIdentity=ObjectIdentity
svrMgtMibInfo=_SvrMgtMibInfo_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,2,1))
_SvrMgtMibMajorRev_Type=Integer32
_SvrMgtMibMajorRev_Object=MibScalar
svrMgtMibMajorRev=_SvrMgtMibMajorRev_Object((1,3,6,1,4,1,36,2,18,22,2,1,1),_SvrMgtMibMajorRev_Type())
svrMgtMibMajorRev.setMaxAccess(_N)
if mibBuilder.loadTexts:svrMgtMibMajorRev.setStatus(_B)
_SvrMgtMibMinorRev_Type=Integer32
_SvrMgtMibMinorRev_Object=MibScalar
svrMgtMibMinorRev=_SvrMgtMibMinorRev_Object((1,3,6,1,4,1,36,2,18,22,2,1,2),_SvrMgtMibMinorRev_Type())
svrMgtMibMinorRev.setMaxAccess(_N)
if mibBuilder.loadTexts:svrMgtMibMinorRev.setStatus(_B)
_SvrAlarms_ObjectIdentity=ObjectIdentity
svrAlarms=_SvrAlarms_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,2,2))
_SvrAlarmNextThrIndex_Type=Integer32
_SvrAlarmNextThrIndex_Object=MibScalar
svrAlarmNextThrIndex=_SvrAlarmNextThrIndex_Object((1,3,6,1,4,1,36,2,18,22,2,2,1),_SvrAlarmNextThrIndex_Type())
svrAlarmNextThrIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:svrAlarmNextThrIndex.setStatus(_B)
_SvrAlarmEnableTraps_Type=Boolean
_SvrAlarmEnableTraps_Object=MibScalar
svrAlarmEnableTraps=_SvrAlarmEnableTraps_Object((1,3,6,1,4,1,36,2,18,22,2,2,2),_SvrAlarmEnableTraps_Type())
svrAlarmEnableTraps.setMaxAccess(_W)
if mibBuilder.loadTexts:svrAlarmEnableTraps.setStatus('obsolete')
_SvrThresholdTable_Object=MibTable
svrThresholdTable=_SvrThresholdTable_Object((1,3,6,1,4,1,36,2,18,22,2,2,3))
if mibBuilder.loadTexts:svrThresholdTable.setStatus(_B)
_SvrThresholdEntry_Object=MibTableRow
svrThresholdEntry=_SvrThresholdEntry_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1))
svrThresholdEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:svrThresholdEntry.setStatus(_B)
_SvrThrIndex_Type=Integer32
_SvrThrIndex_Object=MibTableColumn
svrThrIndex=_SvrThrIndex_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,1),_SvrThrIndex_Type())
svrThrIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:svrThrIndex.setStatus(_B)
class _SvrThrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('underCreation',1),('rowInvalid',2),('rowEnabled',3),('rowDisabled',4),('rowError',5)))
_SvrThrStatus_Type.__name__=_O
_SvrThrStatus_Object=MibTableColumn
svrThrStatus=_SvrThrStatus_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,2),_SvrThrStatus_Type())
svrThrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrStatus.setStatus(_B)
_SvrThrVariableName_Type=ObjectIdentifier
_SvrThrVariableName_Object=MibTableColumn
svrThrVariableName=_SvrThrVariableName_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,3),_SvrThrVariableName_Type())
svrThrVariableName.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrVariableName.setStatus(_B)
class _SvrThrValueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2)))
_SvrThrValueType_Type.__name__=_O
_SvrThrValueType_Object=MibTableColumn
svrThrValueType=_SvrThrValueType_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,4),_SvrThrValueType_Type())
svrThrValueType.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrValueType.setStatus(_B)
class _SvrThrAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_SvrThrAlarmType_Type.__name__=_O
_SvrThrAlarmType_Object=MibTableColumn
svrThrAlarmType=_SvrThrAlarmType_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,5),_SvrThrAlarmType_Type())
svrThrAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrAlarmType.setStatus(_B)
_SvrThrSampleInterval_Type=Integer32
_SvrThrSampleInterval_Object=MibTableColumn
svrThrSampleInterval=_SvrThrSampleInterval_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,6),_SvrThrSampleInterval_Type())
svrThrSampleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrSampleInterval.setStatus(_B)
_SvrThrPersistent_Type=Boolean
_SvrThrPersistent_Object=MibTableColumn
svrThrPersistent=_SvrThrPersistent_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,7),_SvrThrPersistent_Type())
svrThrPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrPersistent.setStatus(_B)
_SvrThrThresholdValue_Type=Integer32
_SvrThrThresholdValue_Object=MibTableColumn
svrThrThresholdValue=_SvrThrThresholdValue_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,8),_SvrThrThresholdValue_Type())
svrThrThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrThresholdValue.setStatus(_B)
_SvrThrResetValue_Type=Integer32
_SvrThrResetValue_Object=MibTableColumn
svrThrResetValue=_SvrThrResetValue_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,9),_SvrThrResetValue_Type())
svrThrResetValue.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrResetValue.setStatus(_B)
_SvrThrLastValue_Type=Integer32
_SvrThrLastValue_Object=MibTableColumn
svrThrLastValue=_SvrThrLastValue_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,10),_SvrThrLastValue_Type())
svrThrLastValue.setMaxAccess(_N)
if mibBuilder.loadTexts:svrThrLastValue.setStatus(_B)
class _SvrThrAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('reset',2)))
_SvrThrAlarmState_Type.__name__=_O
_SvrThrAlarmState_Object=MibTableColumn
svrThrAlarmState=_SvrThrAlarmState_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,11),_SvrThrAlarmState_Type())
svrThrAlarmState.setMaxAccess(_N)
if mibBuilder.loadTexts:svrThrAlarmState.setStatus(_B)
_SvrThrLogEvent_Type=Boolean
_SvrThrLogEvent_Object=MibTableColumn
svrThrLogEvent=_SvrThrLogEvent_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,12),_SvrThrLogEvent_Type())
svrThrLogEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrLogEvent.setStatus(_B)
_SvrThrInvokeLocalHandler_Type=Boolean
_SvrThrInvokeLocalHandler_Object=MibTableColumn
svrThrInvokeLocalHandler=_SvrThrInvokeLocalHandler_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,13),_SvrThrInvokeLocalHandler_Type())
svrThrInvokeLocalHandler.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrInvokeLocalHandler.setStatus(_B)
_SvrThrLocalHandlerPath_Type=DisplayString
_SvrThrLocalHandlerPath_Object=MibTableColumn
svrThrLocalHandlerPath=_SvrThrLocalHandlerPath_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,14),_SvrThrLocalHandlerPath_Type())
svrThrLocalHandlerPath.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrLocalHandlerPath.setStatus(_B)
_SvrThrDescr_Type=DisplayString
_SvrThrDescr_Object=MibTableColumn
svrThrDescr=_SvrThrDescr_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,15),_SvrThrDescr_Type())
svrThrDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrDescr.setStatus(_B)
_SvrThrErrorValue_Type=SnmpErrors
_SvrThrErrorValue_Object=MibTableColumn
svrThrErrorValue=_SvrThrErrorValue_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,16),_SvrThrErrorValue_Type())
svrThrErrorValue.setMaxAccess(_N)
if mibBuilder.loadTexts:svrThrErrorValue.setStatus(_B)
_SvrThrComparisonName_Type=ObjectIdentifier
_SvrThrComparisonName_Object=MibTableColumn
svrThrComparisonName=_SvrThrComparisonName_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,17),_SvrThrComparisonName_Type())
svrThrComparisonName.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrComparisonName.setStatus(_B)
_SvrThrComparisonValue_Type=DisplayString
_SvrThrComparisonValue_Object=MibTableColumn
svrThrComparisonValue=_SvrThrComparisonValue_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,18),_SvrThrComparisonValue_Type())
svrThrComparisonValue.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrComparisonValue.setStatus(_B)
_SvrThrSeverity_Type=Severity
_SvrThrSeverity_Object=MibTableColumn
svrThrSeverity=_SvrThrSeverity_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,19),_SvrThrSeverity_Type())
svrThrSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrSeverity.setStatus(_B)
_SvrThrTrapEnabler_Type=Boolean
_SvrThrTrapEnabler_Object=MibTableColumn
svrThrTrapEnabler=_SvrThrTrapEnabler_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,20),_SvrThrTrapEnabler_Type())
svrThrTrapEnabler.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrTrapEnabler.setStatus(_B)
_SvrThrLocalHandlerArguments1_Type=DisplayString
_SvrThrLocalHandlerArguments1_Object=MibTableColumn
svrThrLocalHandlerArguments1=_SvrThrLocalHandlerArguments1_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,21),_SvrThrLocalHandlerArguments1_Type())
svrThrLocalHandlerArguments1.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrLocalHandlerArguments1.setStatus(_B)
_SvrThrLocalHandlerArguments2_Type=DisplayString
_SvrThrLocalHandlerArguments2_Object=MibTableColumn
svrThrLocalHandlerArguments2=_SvrThrLocalHandlerArguments2_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,22),_SvrThrLocalHandlerArguments2_Type())
svrThrLocalHandlerArguments2.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrLocalHandlerArguments2.setStatus(_B)
_SvrThrLocalHandlerArguments3_Type=DisplayString
_SvrThrLocalHandlerArguments3_Object=MibTableColumn
svrThrLocalHandlerArguments3=_SvrThrLocalHandlerArguments3_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,23),_SvrThrLocalHandlerArguments3_Type())
svrThrLocalHandlerArguments3.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrLocalHandlerArguments3.setStatus(_B)
_SvrThrLocalHandlerArguments4_Type=DisplayString
_SvrThrLocalHandlerArguments4_Object=MibTableColumn
svrThrLocalHandlerArguments4=_SvrThrLocalHandlerArguments4_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,24),_SvrThrLocalHandlerArguments4_Type())
svrThrLocalHandlerArguments4.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrLocalHandlerArguments4.setStatus(_B)
_SvrThrTrapsSendingInterval_Type=Integer32
_SvrThrTrapsSendingInterval_Object=MibTableColumn
svrThrTrapsSendingInterval=_SvrThrTrapsSendingInterval_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,25),_SvrThrTrapsSendingInterval_Type())
svrThrTrapsSendingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrTrapsSendingInterval.setStatus(_B)
_SvrThrManagerDefinedTrapData_Type=DisplayString
_SvrThrManagerDefinedTrapData_Object=MibTableColumn
svrThrManagerDefinedTrapData=_SvrThrManagerDefinedTrapData_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,26),_SvrThrManagerDefinedTrapData_Type())
svrThrManagerDefinedTrapData.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrManagerDefinedTrapData.setStatus(_B)
_SvrThrUserDefinedTrapData_Type=DisplayString
_SvrThrUserDefinedTrapData_Object=MibTableColumn
svrThrUserDefinedTrapData=_SvrThrUserDefinedTrapData_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,27),_SvrThrUserDefinedTrapData_Type())
svrThrUserDefinedTrapData.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrUserDefinedTrapData.setStatus(_B)
_SvrThrRetryCount_Type=Integer32
_SvrThrRetryCount_Object=MibTableColumn
svrThrRetryCount=_SvrThrRetryCount_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,28),_SvrThrRetryCount_Type())
svrThrRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrRetryCount.setStatus(_B)
_SvrThrResetType_Type=ResetRelationalOperators
_SvrThrResetType_Object=MibTableColumn
svrThrResetType=_SvrThrResetType_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,29),_SvrThrResetType_Type())
svrThrResetType.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrResetType.setStatus(_B)
_SvrThrAlarmCategory_Type=AlarmCategory
_SvrThrAlarmCategory_Object=MibTableColumn
svrThrAlarmCategory=_SvrThrAlarmCategory_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,30),_SvrThrAlarmCategory_Type())
svrThrAlarmCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrAlarmCategory.setStatus(_B)
_SvrThrTrapOid_Type=ObjectIdentifier
_SvrThrTrapOid_Object=MibTableColumn
svrThrTrapOid=_SvrThrTrapOid_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,31),_SvrThrTrapOid_Type())
svrThrTrapOid.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrTrapOid.setStatus(_B)
_SvrThrCreatedBy_Type=ThresholdOwner
_SvrThrCreatedBy_Object=MibTableColumn
svrThrCreatedBy=_SvrThrCreatedBy_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,32),_SvrThrCreatedBy_Type())
svrThrCreatedBy.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrCreatedBy.setStatus(_B)
_SvrThrModifiable_Type=Boolean
_SvrThrModifiable_Object=MibTableColumn
svrThrModifiable=_SvrThrModifiable_Object((1,3,6,1,4,1,36,2,18,22,2,2,3,1,33),_SvrThrModifiable_Type())
svrThrModifiable.setMaxAccess(_C)
if mibBuilder.loadTexts:svrThrModifiable.setStatus(_B)
_SvrControl_ObjectIdentity=ObjectIdentity
svrControl=_SvrControl_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,2,3))
_SvrControlEnableTraps_Type=Boolean
_SvrControlEnableTraps_Object=MibScalar
svrControlEnableTraps=_SvrControlEnableTraps_Object((1,3,6,1,4,1,36,2,18,22,2,3,1),_SvrControlEnableTraps_Type())
svrControlEnableTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:svrControlEnableTraps.setStatus(_B)
_SvrControlEnableModifyTraps_Type=Boolean
_SvrControlEnableModifyTraps_Object=MibScalar
svrControlEnableModifyTraps=_SvrControlEnableModifyTraps_Object((1,3,6,1,4,1,36,2,18,22,2,3,2),_SvrControlEnableModifyTraps_Type())
svrControlEnableModifyTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:svrControlEnableModifyTraps.setStatus(_B)
_SvrControlEnableResetTraps_Type=Boolean
_SvrControlEnableResetTraps_Object=MibScalar
svrControlEnableResetTraps=_SvrControlEnableResetTraps_Object((1,3,6,1,4,1,36,2,18,22,2,3,3),_SvrControlEnableResetTraps_Type())
svrControlEnableResetTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:svrControlEnableResetTraps.setStatus(_B)
_SvrControlModifyOID_Type=ObjectIdentifier
_SvrControlModifyOID_Object=MibScalar
svrControlModifyOID=_SvrControlModifyOID_Object((1,3,6,1,4,1,36,2,18,22,2,3,4),_SvrControlModifyOID_Type())
svrControlModifyOID.setMaxAccess(_W)
if mibBuilder.loadTexts:svrControlModifyOID.setStatus(_B)
_SvrTrap_ObjectIdentity=ObjectIdentity
svrTrap=_SvrTrap_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,2,4))
class _SvrTrapReconfigureEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SvrTrapReconfigureEvent_Type.__name__=_O
_SvrTrapReconfigureEvent_Object=MibScalar
svrTrapReconfigureEvent=_SvrTrapReconfigureEvent_Object((1,3,6,1,4,1,36,2,18,22,2,4,1),_SvrTrapReconfigureEvent_Type())
svrTrapReconfigureEvent.setMaxAccess('write-only')
if mibBuilder.loadTexts:svrTrapReconfigureEvent.setStatus(_B)
_SvrTrapCommunityNextIndex_Type=Integer32
_SvrTrapCommunityNextIndex_Object=MibScalar
svrTrapCommunityNextIndex=_SvrTrapCommunityNextIndex_Object((1,3,6,1,4,1,36,2,18,22,2,4,2),_SvrTrapCommunityNextIndex_Type())
svrTrapCommunityNextIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:svrTrapCommunityNextIndex.setStatus(_B)
_SvrTrapCommunityTable_Object=MibTable
svrTrapCommunityTable=_SvrTrapCommunityTable_Object((1,3,6,1,4,1,36,2,18,22,2,4,6))
if mibBuilder.loadTexts:svrTrapCommunityTable.setStatus(_B)
_SvrTrapCommunityEntry_Object=MibTableRow
svrTrapCommunityEntry=_SvrTrapCommunityEntry_Object((1,3,6,1,4,1,36,2,18,22,2,4,6,1))
svrTrapCommunityEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:svrTrapCommunityEntry.setStatus(_B)
_SvrTrapCommunityIndex_Type=Integer32
_SvrTrapCommunityIndex_Object=MibTableColumn
svrTrapCommunityIndex=_SvrTrapCommunityIndex_Object((1,3,6,1,4,1,36,2,18,22,2,4,6,1,1),_SvrTrapCommunityIndex_Type())
svrTrapCommunityIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:svrTrapCommunityIndex.setStatus(_B)
_SvrTrapCommunityName_Type=DisplayString
_SvrTrapCommunityName_Object=MibTableColumn
svrTrapCommunityName=_SvrTrapCommunityName_Object((1,3,6,1,4,1,36,2,18,22,2,4,6,1,2),_SvrTrapCommunityName_Type())
svrTrapCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:svrTrapCommunityName.setStatus(_B)
_SvrTrapDestinationNextIndex_Type=Integer32
_SvrTrapDestinationNextIndex_Object=MibTableColumn
svrTrapDestinationNextIndex=_SvrTrapDestinationNextIndex_Object((1,3,6,1,4,1,36,2,18,22,2,4,6,1,3),_SvrTrapDestinationNextIndex_Type())
svrTrapDestinationNextIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:svrTrapDestinationNextIndex.setStatus(_B)
_SvrTrapDestinationTable_Object=MibTable
svrTrapDestinationTable=_SvrTrapDestinationTable_Object((1,3,6,1,4,1,36,2,18,22,2,4,7))
if mibBuilder.loadTexts:svrTrapDestinationTable.setStatus(_B)
_SvrTrapDestinationEntry_Object=MibTableRow
svrTrapDestinationEntry=_SvrTrapDestinationEntry_Object((1,3,6,1,4,1,36,2,18,22,2,4,7,1))
svrTrapDestinationEntry.setIndexNames((0,_A,_P),(0,_A,_Y))
if mibBuilder.loadTexts:svrTrapDestinationEntry.setStatus(_B)
_SvrTrapDestinationIndex_Type=Integer32
_SvrTrapDestinationIndex_Object=MibTableColumn
svrTrapDestinationIndex=_SvrTrapDestinationIndex_Object((1,3,6,1,4,1,36,2,18,22,2,4,7,1,1),_SvrTrapDestinationIndex_Type())
svrTrapDestinationIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:svrTrapDestinationIndex.setStatus(_B)
_SvrTrapDestination_Type=DisplayString
_SvrTrapDestination_Object=MibTableColumn
svrTrapDestination=_SvrTrapDestination_Object((1,3,6,1,4,1,36,2,18,22,2,4,7,1,2),_SvrTrapDestination_Type())
svrTrapDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:svrTrapDestination.setStatus(_B)
_SvrMinimalHealth_ObjectIdentity=ObjectIdentity
svrMinimalHealth=_SvrMinimalHealth_ObjectIdentity((1,3,6,1,4,1,36,2,18,22,2,5))
_SvrMinimalHealthMajorRev_Type=Integer32
_SvrMinimalHealthMajorRev_Object=MibScalar
svrMinimalHealthMajorRev=_SvrMinimalHealthMajorRev_Object((1,3,6,1,4,1,36,2,18,22,2,5,1),_SvrMinimalHealthMajorRev_Type())
svrMinimalHealthMajorRev.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthMajorRev.setStatus(_B)
_SvrMinimalHealthMinorRev_Type=Integer32
_SvrMinimalHealthMinorRev_Object=MibScalar
svrMinimalHealthMinorRev=_SvrMinimalHealthMinorRev_Object((1,3,6,1,4,1,36,2,18,22,2,5,2),_SvrMinimalHealthMinorRev_Type())
svrMinimalHealthMinorRev.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthMinorRev.setStatus(_B)
_SvrMinimalHealthEnable_Type=Boolean
_SvrMinimalHealthEnable_Object=MibScalar
svrMinimalHealthEnable=_SvrMinimalHealthEnable_Object((1,3,6,1,4,1,36,2,18,22,2,5,3),_SvrMinimalHealthEnable_Type())
svrMinimalHealthEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthEnable.setStatus(_B)
_SvrMinimalHealthDesiredTemplateName_Type=DisplayString
_SvrMinimalHealthDesiredTemplateName_Object=MibScalar
svrMinimalHealthDesiredTemplateName=_SvrMinimalHealthDesiredTemplateName_Object((1,3,6,1,4,1,36,2,18,22,2,5,4),_SvrMinimalHealthDesiredTemplateName_Type())
svrMinimalHealthDesiredTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthDesiredTemplateName.setStatus(_B)
_SvrMinimalHealthDesiredTemplateRevision_Type=DisplayString
_SvrMinimalHealthDesiredTemplateRevision_Object=MibScalar
svrMinimalHealthDesiredTemplateRevision=_SvrMinimalHealthDesiredTemplateRevision_Object((1,3,6,1,4,1,36,2,18,22,2,5,5),_SvrMinimalHealthDesiredTemplateRevision_Type())
svrMinimalHealthDesiredTemplateRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthDesiredTemplateRevision.setStatus(_B)
_SvrMinimalHealthDesiredTemplateRevisionDate_Type=DisplayString
_SvrMinimalHealthDesiredTemplateRevisionDate_Object=MibScalar
svrMinimalHealthDesiredTemplateRevisionDate=_SvrMinimalHealthDesiredTemplateRevisionDate_Object((1,3,6,1,4,1,36,2,18,22,2,5,6),_SvrMinimalHealthDesiredTemplateRevisionDate_Type())
svrMinimalHealthDesiredTemplateRevisionDate.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthDesiredTemplateRevisionDate.setStatus(_B)
_SvrMinimalHealthActualTemplateName_Type=DisplayString
_SvrMinimalHealthActualTemplateName_Object=MibScalar
svrMinimalHealthActualTemplateName=_SvrMinimalHealthActualTemplateName_Object((1,3,6,1,4,1,36,2,18,22,2,5,7),_SvrMinimalHealthActualTemplateName_Type())
svrMinimalHealthActualTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthActualTemplateName.setStatus(_B)
_SvrMinimalHealthActualTemplateRevision_Type=DisplayString
_SvrMinimalHealthActualTemplateRevision_Object=MibScalar
svrMinimalHealthActualTemplateRevision=_SvrMinimalHealthActualTemplateRevision_Object((1,3,6,1,4,1,36,2,18,22,2,5,8),_SvrMinimalHealthActualTemplateRevision_Type())
svrMinimalHealthActualTemplateRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthActualTemplateRevision.setStatus(_B)
_SvrMinimalHealthActualTemplateRevisionDate_Type=DisplayString
_SvrMinimalHealthActualTemplateRevisionDate_Object=MibScalar
svrMinimalHealthActualTemplateRevisionDate=_SvrMinimalHealthActualTemplateRevisionDate_Object((1,3,6,1,4,1,36,2,18,22,2,5,9),_SvrMinimalHealthActualTemplateRevisionDate_Type())
svrMinimalHealthActualTemplateRevisionDate.setMaxAccess(_C)
if mibBuilder.loadTexts:svrMinimalHealthActualTemplateRevisionDate.setStatus(_B)
svrThrModifyTrap=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,99))
svrThrModifyTrap.setObjects(*((_A,_D),(_A,_E),(_A,_Z),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrModifyTrap.setStatus('')
svrThrResetTrap=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,100))
svrThrResetTrap.setObjects(*((_A,_D),(_A,_K),(_A,_a),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrResetTrap.setStatus('')
svrThrHighExceptTrap=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,101))
svrThrHighExceptTrap.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrHighExceptTrap.setStatus('')
svrThrMediumExceptTrap=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,102))
svrThrMediumExceptTrap.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrMediumExceptTrap.setStatus('')
svrThrLowExceptTrap=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,103))
svrThrLowExceptTrap.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrLowExceptTrap.setStatus('')
svrThrInformationalExceptTrap=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,104))
svrThrInformationalExceptTrap.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrInformationalExceptTrap.setStatus('')
svrThrDiskDown=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,105))
svrThrDiskDown.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrDiskDown.setStatus('')
svrThrDiskWarning=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,106))
svrThrDiskWarning.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrDiskWarning.setStatus('')
svrThrDiskOk=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,107))
svrThrDiskOk.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrDiskOk.setStatus('')
svrThrFileSystemUsage=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,108))
svrThrFileSystemUsage.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrFileSystemUsage.setStatus('')
svrThrTemperatureOk=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,109))
svrThrTemperatureOk.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrTemperatureOk.setStatus('')
svrThrTemperatureCritical=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,110))
svrThrTemperatureCritical.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrTemperatureCritical.setStatus('')
svrThrTemperatureWarning=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,111))
svrThrTemperatureWarning.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrTemperatureWarning.setStatus('')
svrThrFanFailed=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,112))
svrThrFanFailed.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrFanFailed.setStatus('')
svrThrFanOk=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,113))
svrThrFanOk.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrFanOk.setStatus('')
svrThrFanBackup=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,114))
svrThrFanBackup.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrFanBackup.setStatus('')
svrThrVoltageOk=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,115))
svrThrVoltageOk.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrVoltageOk.setStatus('')
svrThrVoltageCritical=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,116))
svrThrVoltageCritical.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrVoltageCritical.setStatus('')
svrThrVoltageWarning=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,117))
svrThrVoltageWarning.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrVoltageWarning.setStatus('')
svrThrPowerSupplyFailed=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,118))
svrThrPowerSupplyFailed.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrPowerSupplyFailed.setStatus('')
svrThrPowerSupplyWarning=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,119))
svrThrPowerSupplyWarning.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrPowerSupplyWarning.setStatus('')
svrThrPowerSupplyOk=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,120))
svrThrPowerSupplyOk.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrPowerSupplyOk.setStatus('')
svrThrPowerSupplyBackup=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,121))
svrThrPowerSupplyBackup.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrPowerSupplyBackup.setStatus('')
svrThrMemoryEltFailed=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,122))
svrThrMemoryEltFailed.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrMemoryEltFailed.setStatus('')
svrThrMemoryEltWarning=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,123))
svrThrMemoryEltWarning.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrMemoryEltWarning.setStatus('')
svrThrMemoryEltOk=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,124))
svrThrMemoryEltOk.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrMemoryEltOk.setStatus('')
svrThrNetworkIfInErrors=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,125))
svrThrNetworkIfInErrors.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrNetworkIfInErrors.setStatus('')
svrThrNetworkIfInOctets=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,126))
svrThrNetworkIfInOctets.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrNetworkIfInOctets.setStatus('')
svrThrNetworkIfOutOctets=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,127))
svrThrNetworkIfOutOctets.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrNetworkIfOutOctets.setStatus('')
svrThrNetworkIfInPkts=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,128))
svrThrNetworkIfInPkts.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrNetworkIfInPkts.setStatus('')
svrThrNetworkIfOutPkts=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,129))
svrThrNetworkIfOutPkts.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrNetworkIfOutPkts.setStatus('')
svrThrNetworkIfOutErrors=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,130))
svrThrNetworkIfOutErrors.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrNetworkIfOutErrors.setStatus('')
svrThrNetworkIfInDiscards=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,131))
svrThrNetworkIfInDiscards.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrNetworkIfInDiscards.setStatus('')
svrThrProcessorDown=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,132))
svrThrProcessorDown.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrProcessorDown.setStatus('')
svrThrProcessorWarning=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,133))
svrThrProcessorWarning.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrProcessorWarning.setStatus('')
svrThrProcessorOk=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,134))
svrThrProcessorOk.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrProcessorOk.setStatus('')
svrThrCpuUsage=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,135))
svrThrCpuUsage.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrCpuUsage.setStatus('')
svrThrClusterFailOverOwner=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,136))
svrThrClusterFailOverOwner.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrClusterFailOverOwner.setStatus('')
svrThrClusterFailOverNotOwner=NotificationType((1,3,6,1,4,1,36,2,18,22,2,0,137))
svrThrClusterFailOverNotOwner.setObjects(*((_A,_D),(_A,_K),(_A,_M),(_A,_L),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:svrThrClusterFailOverNotOwner.setStatus('')
mibBuilder.exportSymbols(_A,**{'Boolean':Boolean,'SnmpErrors':SnmpErrors,'Severity':Severity,'AlarmCategory':AlarmCategory,'ResetRelationalOperators':ResetRelationalOperators,'ThresholdOwner':ThresholdOwner,'dec':dec,'ema':ema,'mib-extensions-1':mib_extensions_1,'svrSystem':svrSystem,'svrMgt':svrMgt,'svrThrModifyTrap':svrThrModifyTrap,'svrThrResetTrap':svrThrResetTrap,'svrThrHighExceptTrap':svrThrHighExceptTrap,'svrThrMediumExceptTrap':svrThrMediumExceptTrap,'svrThrLowExceptTrap':svrThrLowExceptTrap,'svrThrInformationalExceptTrap':svrThrInformationalExceptTrap,'svrThrDiskDown':svrThrDiskDown,'svrThrDiskWarning':svrThrDiskWarning,'svrThrDiskOk':svrThrDiskOk,'svrThrFileSystemUsage':svrThrFileSystemUsage,'svrThrTemperatureOk':svrThrTemperatureOk,'svrThrTemperatureCritical':svrThrTemperatureCritical,'svrThrTemperatureWarning':svrThrTemperatureWarning,'svrThrFanFailed':svrThrFanFailed,'svrThrFanOk':svrThrFanOk,'svrThrFanBackup':svrThrFanBackup,'svrThrVoltageOk':svrThrVoltageOk,'svrThrVoltageCritical':svrThrVoltageCritical,'svrThrVoltageWarning':svrThrVoltageWarning,'svrThrPowerSupplyFailed':svrThrPowerSupplyFailed,'svrThrPowerSupplyWarning':svrThrPowerSupplyWarning,'svrThrPowerSupplyOk':svrThrPowerSupplyOk,'svrThrPowerSupplyBackup':svrThrPowerSupplyBackup,'svrThrMemoryEltFailed':svrThrMemoryEltFailed,'svrThrMemoryEltWarning':svrThrMemoryEltWarning,'svrThrMemoryEltOk':svrThrMemoryEltOk,'svrThrNetworkIfInErrors':svrThrNetworkIfInErrors,'svrThrNetworkIfInOctets':svrThrNetworkIfInOctets,'svrThrNetworkIfOutOctets':svrThrNetworkIfOutOctets,'svrThrNetworkIfInPkts':svrThrNetworkIfInPkts,'svrThrNetworkIfOutPkts':svrThrNetworkIfOutPkts,'svrThrNetworkIfOutErrors':svrThrNetworkIfOutErrors,'svrThrNetworkIfInDiscards':svrThrNetworkIfInDiscards,'svrThrProcessorDown':svrThrProcessorDown,'svrThrProcessorWarning':svrThrProcessorWarning,'svrThrProcessorOk':svrThrProcessorOk,'svrThrCpuUsage':svrThrCpuUsage,'svrThrClusterFailOverOwner':svrThrClusterFailOverOwner,'svrThrClusterFailOverNotOwner':svrThrClusterFailOverNotOwner,'svrMgtMibInfo':svrMgtMibInfo,'svrMgtMibMajorRev':svrMgtMibMajorRev,'svrMgtMibMinorRev':svrMgtMibMinorRev,'svrAlarms':svrAlarms,'svrAlarmNextThrIndex':svrAlarmNextThrIndex,'svrAlarmEnableTraps':svrAlarmEnableTraps,'svrThresholdTable':svrThresholdTable,'svrThresholdEntry':svrThresholdEntry,_X:svrThrIndex,'svrThrStatus':svrThrStatus,_D:svrThrVariableName,_K:svrThrValueType,'svrThrAlarmType':svrThrAlarmType,'svrThrSampleInterval':svrThrSampleInterval,'svrThrPersistent':svrThrPersistent,_M:svrThrThresholdValue,_a:svrThrResetValue,_L:svrThrLastValue,'svrThrAlarmState':svrThrAlarmState,'svrThrLogEvent':svrThrLogEvent,'svrThrInvokeLocalHandler':svrThrInvokeLocalHandler,'svrThrLocalHandlerPath':svrThrLocalHandlerPath,_E:svrThrDescr,'svrThrErrorValue':svrThrErrorValue,'svrThrComparisonName':svrThrComparisonName,'svrThrComparisonValue':svrThrComparisonValue,_J:svrThrSeverity,'svrThrTrapEnabler':svrThrTrapEnabler,'svrThrLocalHandlerArguments1':svrThrLocalHandlerArguments1,'svrThrLocalHandlerArguments2':svrThrLocalHandlerArguments2,'svrThrLocalHandlerArguments3':svrThrLocalHandlerArguments3,'svrThrLocalHandlerArguments4':svrThrLocalHandlerArguments4,'svrThrTrapsSendingInterval':svrThrTrapsSendingInterval,_F:svrThrManagerDefinedTrapData,_G:svrThrUserDefinedTrapData,'svrThrRetryCount':svrThrRetryCount,'svrThrResetType':svrThrResetType,_H:svrThrAlarmCategory,'svrThrTrapOid':svrThrTrapOid,_I:svrThrCreatedBy,'svrThrModifiable':svrThrModifiable,'svrControl':svrControl,'svrControlEnableTraps':svrControlEnableTraps,'svrControlEnableModifyTraps':svrControlEnableModifyTraps,'svrControlEnableResetTraps':svrControlEnableResetTraps,_Z:svrControlModifyOID,'svrTrap':svrTrap,'svrTrapReconfigureEvent':svrTrapReconfigureEvent,'svrTrapCommunityNextIndex':svrTrapCommunityNextIndex,'svrTrapCommunityTable':svrTrapCommunityTable,'svrTrapCommunityEntry':svrTrapCommunityEntry,_P:svrTrapCommunityIndex,'svrTrapCommunityName':svrTrapCommunityName,'svrTrapDestinationNextIndex':svrTrapDestinationNextIndex,'svrTrapDestinationTable':svrTrapDestinationTable,'svrTrapDestinationEntry':svrTrapDestinationEntry,_Y:svrTrapDestinationIndex,'svrTrapDestination':svrTrapDestination,'svrMinimalHealth':svrMinimalHealth,'svrMinimalHealthMajorRev':svrMinimalHealthMajorRev,'svrMinimalHealthMinorRev':svrMinimalHealthMinorRev,'svrMinimalHealthEnable':svrMinimalHealthEnable,'svrMinimalHealthDesiredTemplateName':svrMinimalHealthDesiredTemplateName,'svrMinimalHealthDesiredTemplateRevision':svrMinimalHealthDesiredTemplateRevision,'svrMinimalHealthDesiredTemplateRevisionDate':svrMinimalHealthDesiredTemplateRevisionDate,'svrMinimalHealthActualTemplateName':svrMinimalHealthActualTemplateName,'svrMinimalHealthActualTemplateRevision':svrMinimalHealthActualTemplateRevision,'svrMinimalHealthActualTemplateRevisionDate':svrMinimalHealthActualTemplateRevisionDate})