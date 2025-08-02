_A6='pktcEventNotificationGroup'
_A5='pktcEventGroup'
_A4='pktcEventNotification'
_A3='pktcEventClassSeverity'
_A2='pktcEventClassStatus'
_A1='pktcEventClassName'
_A0='pktcEventClass'
_z='pktcEventLogAdditionalInfo'
_y='pktcEventLogTargetInfo'
_x='pktcEventLogType'
_w='pktcEventLogText'
_v='pktcEventText'
_u='pktcEventReporting'
_t='pktcEventSeverityLevel'
_s='pktcEventFacility'
_r='pktcEventTransmissionStatus'
_q='pktcEventThrottleInterval'
_p='pktcEventThrottleThreshold'
_o='pktcEventThrottleAdminStatus'
_n='pktcEventSyslogMessageFormat'
_m='pktcEventSyslogPort'
_l='pktcEventSyslogTransport'
_k='pktcEventSyslogAddress'
_j='pktcEventSyslogAddressType'
_i='pktcEventSyslogCapabilities'
_h='pktcEventReset'
_g='pktcEventLogIndex'
_f='snmpInform'
_e='snmpTrap'
_d='syslog'
_c='pktcEventIdentifier'
_b='pktcEventOrganization'
_a='pktcEventClassIndex'
_Z='formatSyslogProtocol'
_Y='formatBSDSyslog'
_X='snmpTargetResponseGroup'
_W='snmpTargetBasicGroup'
_V='snmpNotifyGroup'
_U='snmpNotifyFilterGroup'
_T='InetPortNumber'
_S='InetAddressType'
_R='InetAddress'
_Q='ifPhysAddress'
_P='IF-MIB'
_O='pktcEventLogCorrelationId'
_N='pktcEventLogEndpointName'
_M='pktcEventLogIdentifier'
_L='pktcEventLogOrganization'
_K='pktcEventLogTime'
_J='SNMP-NOTIFICATION-MIB'
_I='not-accessible'
_H='Integer32'
_G='Bits'
_F='Unsigned32'
_E='SnmpAdminString'
_D='read-only'
_C='read-write'
_B='PKTC-IETF-EVENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifPhysAddress,=mibBuilder.importSymbols(_P,_Q)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_R,_S,_T)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
snmpNotifyFilterGroup,snmpNotifyGroup=mibBuilder.importSymbols(_J,_U,_V)
snmpTargetBasicGroup,snmpTargetResponseGroup=mibBuilder.importSymbols('SNMP-TARGET-MIB',_W,_X)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
SyslogFacility,SyslogSeverity=mibBuilder.importSymbols('SYSLOG-TC-MIB','SyslogFacility','SyslogSeverity')
pktcIetfEventMib=ModuleIdentity((1,3,6,1,2,1,182))
if mibBuilder.loadTexts:pktcIetfEventMib.setRevisions(('2009-03-30 00:00',))
class SyslogSeverityMask(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('emerg',0),('alert',1),('crit',2),('err',3),('warning',4),('notice',5),('info',6),('debug',7)))
_PktcEventNotifications_ObjectIdentity=ObjectIdentity
pktcEventNotifications=_PktcEventNotifications_ObjectIdentity((1,3,6,1,2,1,182,0))
_PktcEventMibObjects_ObjectIdentity=ObjectIdentity
pktcEventMibObjects=_PktcEventMibObjects_ObjectIdentity((1,3,6,1,2,1,182,1))
_PktcEventControl_ObjectIdentity=ObjectIdentity
pktcEventControl=_PktcEventControl_ObjectIdentity((1,3,6,1,2,1,182,1,1))
class _PktcEventReset_Type(Bits):namedValues=NamedValues(*(('resetEventLogTable',0),('resetEventTable',1)))
_PktcEventReset_Type.__name__=_G
_PktcEventReset_Object=MibScalar
pktcEventReset=_PktcEventReset_Object((1,3,6,1,2,1,182,1,1,1),_PktcEventReset_Type())
pktcEventReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventReset.setStatus(_A)
_PktcEventSyslog_ObjectIdentity=ObjectIdentity
pktcEventSyslog=_PktcEventSyslog_ObjectIdentity((1,3,6,1,2,1,182,1,1,2))
class _PktcEventSyslogCapabilities_Type(Bits):namedValues=NamedValues(*((_Y,0),(_Z,1),('transportUDP',2),('transportTLS',3),('transportBEEP',4)))
_PktcEventSyslogCapabilities_Type.__name__=_G
_PktcEventSyslogCapabilities_Object=MibScalar
pktcEventSyslogCapabilities=_PktcEventSyslogCapabilities_Object((1,3,6,1,2,1,182,1,1,2,1),_PktcEventSyslogCapabilities_Type())
pktcEventSyslogCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventSyslogCapabilities.setStatus(_A)
class _PktcEventSyslogAddressType_Type(InetAddressType):defaultValue=1
_PktcEventSyslogAddressType_Type.__name__=_S
_PktcEventSyslogAddressType_Object=MibScalar
pktcEventSyslogAddressType=_PktcEventSyslogAddressType_Object((1,3,6,1,2,1,182,1,1,2,2),_PktcEventSyslogAddressType_Type())
pktcEventSyslogAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventSyslogAddressType.setStatus(_A)
class _PktcEventSyslogAddress_Type(InetAddress):defaultValue=OctetString('0.0.0.0')
_PktcEventSyslogAddress_Type.__name__=_R
_PktcEventSyslogAddress_Object=MibScalar
pktcEventSyslogAddress=_PktcEventSyslogAddress_Object((1,3,6,1,2,1,182,1,1,2,3),_PktcEventSyslogAddress_Type())
pktcEventSyslogAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventSyslogAddress.setStatus(_A)
class _PktcEventSyslogMessageFormat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_PktcEventSyslogMessageFormat_Type.__name__=_H
_PktcEventSyslogMessageFormat_Object=MibScalar
pktcEventSyslogMessageFormat=_PktcEventSyslogMessageFormat_Object((1,3,6,1,2,1,182,1,1,2,4),_PktcEventSyslogMessageFormat_Type())
pktcEventSyslogMessageFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventSyslogMessageFormat.setStatus(_A)
class _PktcEventSyslogTransport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tls',2),('beep',3)))
_PktcEventSyslogTransport_Type.__name__=_H
_PktcEventSyslogTransport_Object=MibScalar
pktcEventSyslogTransport=_PktcEventSyslogTransport_Object((1,3,6,1,2,1,182,1,1,2,5),_PktcEventSyslogTransport_Type())
pktcEventSyslogTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventSyslogTransport.setStatus(_A)
class _PktcEventSyslogPort_Type(InetPortNumber):defaultValue=6514
_PktcEventSyslogPort_Type.__name__=_T
_PktcEventSyslogPort_Object=MibScalar
pktcEventSyslogPort=_PktcEventSyslogPort_Object((1,3,6,1,2,1,182,1,1,2,6),_PktcEventSyslogPort_Type())
pktcEventSyslogPort.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventSyslogPort.setStatus(_A)
_PktcEventClassTable_Object=MibTable
pktcEventClassTable=_PktcEventClassTable_Object((1,3,6,1,2,1,182,1,1,3))
if mibBuilder.loadTexts:pktcEventClassTable.setStatus(_A)
_PktcEventClassEntry_Object=MibTableRow
pktcEventClassEntry=_PktcEventClassEntry_Object((1,3,6,1,2,1,182,1,1,3,1))
pktcEventClassEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:pktcEventClassEntry.setStatus(_A)
class _PktcEventClassIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PktcEventClassIndex_Type.__name__=_F
_PktcEventClassIndex_Object=MibTableColumn
pktcEventClassIndex=_PktcEventClassIndex_Object((1,3,6,1,2,1,182,1,1,3,1,1),_PktcEventClassIndex_Type())
pktcEventClassIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcEventClassIndex.setStatus(_A)
class _PktcEventClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_PktcEventClassName_Type.__name__=_E
_PktcEventClassName_Object=MibTableColumn
pktcEventClassName=_PktcEventClassName_Object((1,3,6,1,2,1,182,1,1,3,1,2),_PktcEventClassName_Type())
pktcEventClassName.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventClassName.setStatus(_A)
_PktcEventClassStatus_Type=TruthValue
_PktcEventClassStatus_Object=MibTableColumn
pktcEventClassStatus=_PktcEventClassStatus_Object((1,3,6,1,2,1,182,1,1,3,1,3),_PktcEventClassStatus_Type())
pktcEventClassStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventClassStatus.setStatus(_A)
_PktcEventClassSeverity_Type=SyslogSeverityMask
_PktcEventClassSeverity_Object=MibTableColumn
pktcEventClassSeverity=_PktcEventClassSeverity_Object((1,3,6,1,2,1,182,1,1,3,1,4),_PktcEventClassSeverity_Type())
pktcEventClassSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventClassSeverity.setStatus(_A)
_PktcEventThrottle_ObjectIdentity=ObjectIdentity
pktcEventThrottle=_PktcEventThrottle_ObjectIdentity((1,3,6,1,2,1,182,1,2))
class _PktcEventThrottleAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unconstrained',1),('maintainBelowThreshold',2),('stopAtThreshold',3),('inhibited',4)))
_PktcEventThrottleAdminStatus_Type.__name__=_H
_PktcEventThrottleAdminStatus_Object=MibScalar
pktcEventThrottleAdminStatus=_PktcEventThrottleAdminStatus_Object((1,3,6,1,2,1,182,1,2,1),_PktcEventThrottleAdminStatus_Type())
pktcEventThrottleAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventThrottleAdminStatus.setStatus(_A)
class _PktcEventThrottleThreshold_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_PktcEventThrottleThreshold_Type.__name__=_F
_PktcEventThrottleThreshold_Object=MibScalar
pktcEventThrottleThreshold=_PktcEventThrottleThreshold_Object((1,3,6,1,2,1,182,1,2,2),_PktcEventThrottleThreshold_Type())
pktcEventThrottleThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventThrottleThreshold.setStatus(_A)
class _PktcEventThrottleInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_PktcEventThrottleInterval_Type.__name__=_F
_PktcEventThrottleInterval_Object=MibScalar
pktcEventThrottleInterval=_PktcEventThrottleInterval_Object((1,3,6,1,2,1,182,1,2,3),_PktcEventThrottleInterval_Type())
pktcEventThrottleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventThrottleInterval.setStatus(_A)
if mibBuilder.loadTexts:pktcEventThrottleInterval.setUnits('seconds')
_PktcEventStatus_ObjectIdentity=ObjectIdentity
pktcEventStatus=_PktcEventStatus_ObjectIdentity((1,3,6,1,2,1,182,1,3))
class _PktcEventTransmissionStatus_Type(Bits):namedValues=NamedValues(*(('syslogThrottled',0),('snmpThrottled',1),('validsyslogServerAbsent',2),('validSnmpManagerAbsent',3),('syslogTransmitError',4),('snmpTransmitError',5)))
_PktcEventTransmissionStatus_Type.__name__=_G
_PktcEventTransmissionStatus_Object=MibScalar
pktcEventTransmissionStatus=_PktcEventTransmissionStatus_Object((1,3,6,1,2,1,182,1,3,1),_PktcEventTransmissionStatus_Type())
pktcEventTransmissionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventTransmissionStatus.setStatus(_A)
_PktcEvents_ObjectIdentity=ObjectIdentity
pktcEvents=_PktcEvents_ObjectIdentity((1,3,6,1,2,1,182,1,4))
_PktcEventTable_Object=MibTable
pktcEventTable=_PktcEventTable_Object((1,3,6,1,2,1,182,1,4,1))
if mibBuilder.loadTexts:pktcEventTable.setStatus(_A)
_PktcEventEntry_Object=MibTableRow
pktcEventEntry=_PktcEventEntry_Object((1,3,6,1,2,1,182,1,4,1,1))
pktcEventEntry.setIndexNames((0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:pktcEventEntry.setStatus(_A)
class _PktcEventOrganization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PktcEventOrganization_Type.__name__=_F
_PktcEventOrganization_Object=MibTableColumn
pktcEventOrganization=_PktcEventOrganization_Object((1,3,6,1,2,1,182,1,4,1,1,1),_PktcEventOrganization_Type())
pktcEventOrganization.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcEventOrganization.setStatus(_A)
class _PktcEventIdentifier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PktcEventIdentifier_Type.__name__=_F
_PktcEventIdentifier_Object=MibTableColumn
pktcEventIdentifier=_PktcEventIdentifier_Object((1,3,6,1,2,1,182,1,4,1,1,2),_PktcEventIdentifier_Type())
pktcEventIdentifier.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcEventIdentifier.setStatus(_A)
_PktcEventFacility_Type=SyslogFacility
_PktcEventFacility_Object=MibTableColumn
pktcEventFacility=_PktcEventFacility_Object((1,3,6,1,2,1,182,1,4,1,1,3),_PktcEventFacility_Type())
pktcEventFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventFacility.setStatus(_A)
_PktcEventSeverityLevel_Type=SyslogSeverity
_PktcEventSeverityLevel_Object=MibTableColumn
pktcEventSeverityLevel=_PktcEventSeverityLevel_Object((1,3,6,1,2,1,182,1,4,1,1,4),_PktcEventSeverityLevel_Type())
pktcEventSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventSeverityLevel.setStatus(_A)
class _PktcEventReporting_Type(Bits):namedValues=NamedValues(*(('local',0),(_d,1),(_e,2),(_f,3)))
_PktcEventReporting_Type.__name__=_G
_PktcEventReporting_Object=MibTableColumn
pktcEventReporting=_PktcEventReporting_Object((1,3,6,1,2,1,182,1,4,1,1,5),_PktcEventReporting_Type())
pktcEventReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventReporting.setStatus(_A)
class _PktcEventText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PktcEventText_Type.__name__=_E
_PktcEventText_Object=MibTableColumn
pktcEventText=_PktcEventText_Object((1,3,6,1,2,1,182,1,4,1,1,6),_PktcEventText_Type())
pktcEventText.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEventText.setStatus(_A)
class _PktcEventClass_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_PktcEventClass_Type.__name__=_E
_PktcEventClass_Object=MibTableColumn
pktcEventClass=_PktcEventClass_Object((1,3,6,1,2,1,182,1,4,1,1,7),_PktcEventClass_Type())
pktcEventClass.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventClass.setStatus(_A)
_PktcEventLog_ObjectIdentity=ObjectIdentity
pktcEventLog=_PktcEventLog_ObjectIdentity((1,3,6,1,2,1,182,1,5))
_PktcEventLogTable_Object=MibTable
pktcEventLogTable=_PktcEventLogTable_Object((1,3,6,1,2,1,182,1,5,1))
if mibBuilder.loadTexts:pktcEventLogTable.setStatus(_A)
_PktcEventLogEntry_Object=MibTableRow
pktcEventLogEntry=_PktcEventLogEntry_Object((1,3,6,1,2,1,182,1,5,1,1))
pktcEventLogEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:pktcEventLogEntry.setStatus(_A)
class _PktcEventLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PktcEventLogIndex_Type.__name__=_F
_PktcEventLogIndex_Object=MibTableColumn
pktcEventLogIndex=_PktcEventLogIndex_Object((1,3,6,1,2,1,182,1,5,1,1,1),_PktcEventLogIndex_Type())
pktcEventLogIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcEventLogIndex.setStatus(_A)
_PktcEventLogTime_Type=DateAndTime
_PktcEventLogTime_Object=MibTableColumn
pktcEventLogTime=_PktcEventLogTime_Object((1,3,6,1,2,1,182,1,5,1,1,2),_PktcEventLogTime_Type())
pktcEventLogTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogTime.setStatus(_A)
class _PktcEventLogOrganization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PktcEventLogOrganization_Type.__name__=_F
_PktcEventLogOrganization_Object=MibTableColumn
pktcEventLogOrganization=_PktcEventLogOrganization_Object((1,3,6,1,2,1,182,1,5,1,1,3),_PktcEventLogOrganization_Type())
pktcEventLogOrganization.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogOrganization.setStatus(_A)
_PktcEventLogIdentifier_Type=Unsigned32
_PktcEventLogIdentifier_Object=MibTableColumn
pktcEventLogIdentifier=_PktcEventLogIdentifier_Object((1,3,6,1,2,1,182,1,5,1,1,4),_PktcEventLogIdentifier_Type())
pktcEventLogIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogIdentifier.setStatus(_A)
class _PktcEventLogText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PktcEventLogText_Type.__name__=_E
_PktcEventLogText_Object=MibTableColumn
pktcEventLogText=_PktcEventLogText_Object((1,3,6,1,2,1,182,1,5,1,1,5),_PktcEventLogText_Type())
pktcEventLogText.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogText.setStatus(_A)
class _PktcEventLogEndpointName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PktcEventLogEndpointName_Type.__name__=_E
_PktcEventLogEndpointName_Object=MibTableColumn
pktcEventLogEndpointName=_PktcEventLogEndpointName_Object((1,3,6,1,2,1,182,1,5,1,1,6),_PktcEventLogEndpointName_Type())
pktcEventLogEndpointName.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogEndpointName.setStatus(_A)
class _PktcEventLogType_Type(Bits):namedValues=NamedValues(*(('local',0),(_d,1),(_e,2),(_f,3)))
_PktcEventLogType_Type.__name__=_G
_PktcEventLogType_Object=MibTableColumn
pktcEventLogType=_PktcEventLogType_Object((1,3,6,1,2,1,182,1,5,1,1,7),_PktcEventLogType_Type())
pktcEventLogType.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogType.setStatus(_A)
class _PktcEventLogTargetInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PktcEventLogTargetInfo_Type.__name__=_E
_PktcEventLogTargetInfo_Object=MibTableColumn
pktcEventLogTargetInfo=_PktcEventLogTargetInfo_Object((1,3,6,1,2,1,182,1,5,1,1,8),_PktcEventLogTargetInfo_Type())
pktcEventLogTargetInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogTargetInfo.setStatus(_A)
_PktcEventLogCorrelationId_Type=Unsigned32
_PktcEventLogCorrelationId_Object=MibTableColumn
pktcEventLogCorrelationId=_PktcEventLogCorrelationId_Object((1,3,6,1,2,1,182,1,5,1,1,9),_PktcEventLogCorrelationId_Type())
pktcEventLogCorrelationId.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogCorrelationId.setStatus(_A)
class _PktcEventLogAdditionalInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PktcEventLogAdditionalInfo_Type.__name__=_E
_PktcEventLogAdditionalInfo_Object=MibTableColumn
pktcEventLogAdditionalInfo=_PktcEventLogAdditionalInfo_Object((1,3,6,1,2,1,182,1,5,1,1,10),_PktcEventLogAdditionalInfo_Type())
pktcEventLogAdditionalInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEventLogAdditionalInfo.setStatus(_A)
_PktcEventConformance_ObjectIdentity=ObjectIdentity
pktcEventConformance=_PktcEventConformance_ObjectIdentity((1,3,6,1,2,1,182,2))
_PktcEventCompliances_ObjectIdentity=ObjectIdentity
pktcEventCompliances=_PktcEventCompliances_ObjectIdentity((1,3,6,1,2,1,182,2,1))
_PktcEventGroups_ObjectIdentity=ObjectIdentity
pktcEventGroups=_PktcEventGroups_ObjectIdentity((1,3,6,1,2,1,182,2,2))
pktcEventGroup=ObjectGroup((1,3,6,1,2,1,182,2,2,1))
pktcEventGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_K),(_B,_L),(_B,_M),(_B,_w),(_B,_N),(_B,_x),(_B,_y),(_B,_O),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:pktcEventGroup.setStatus(_A)
pktcEventNotification=NotificationType((1,3,6,1,2,1,182,0,1))
pktcEventNotification.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_P,_Q)))
if mibBuilder.loadTexts:pktcEventNotification.setStatus(_A)
pktcEventNotificationGroup=NotificationGroup((1,3,6,1,2,1,182,2,2,2))
pktcEventNotificationGroup.setObjects((_B,_A4))
if mibBuilder.loadTexts:pktcEventNotificationGroup.setStatus(_A)
pktcEventBasicCompliance=ModuleCompliance((1,3,6,1,2,1,182,2,1,3))
pktcEventBasicCompliance.setObjects(*((_B,_A5),(_B,_A6),(_B,_W),(_B,_X),(_J,_V),(_J,_U)))
if mibBuilder.loadTexts:pktcEventBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SyslogSeverityMask':SyslogSeverityMask,'pktcIetfEventMib':pktcIetfEventMib,'pktcEventNotifications':pktcEventNotifications,_A4:pktcEventNotification,'pktcEventMibObjects':pktcEventMibObjects,'pktcEventControl':pktcEventControl,_h:pktcEventReset,'pktcEventSyslog':pktcEventSyslog,_i:pktcEventSyslogCapabilities,_j:pktcEventSyslogAddressType,_k:pktcEventSyslogAddress,_n:pktcEventSyslogMessageFormat,_l:pktcEventSyslogTransport,_m:pktcEventSyslogPort,'pktcEventClassTable':pktcEventClassTable,'pktcEventClassEntry':pktcEventClassEntry,_a:pktcEventClassIndex,_A1:pktcEventClassName,_A2:pktcEventClassStatus,_A3:pktcEventClassSeverity,'pktcEventThrottle':pktcEventThrottle,_o:pktcEventThrottleAdminStatus,_p:pktcEventThrottleThreshold,_q:pktcEventThrottleInterval,'pktcEventStatus':pktcEventStatus,_r:pktcEventTransmissionStatus,'pktcEvents':pktcEvents,'pktcEventTable':pktcEventTable,'pktcEventEntry':pktcEventEntry,_b:pktcEventOrganization,_c:pktcEventIdentifier,_s:pktcEventFacility,_t:pktcEventSeverityLevel,_u:pktcEventReporting,_v:pktcEventText,_A0:pktcEventClass,'pktcEventLog':pktcEventLog,'pktcEventLogTable':pktcEventLogTable,'pktcEventLogEntry':pktcEventLogEntry,_g:pktcEventLogIndex,_K:pktcEventLogTime,_L:pktcEventLogOrganization,_M:pktcEventLogIdentifier,_w:pktcEventLogText,_N:pktcEventLogEndpointName,_x:pktcEventLogType,_y:pktcEventLogTargetInfo,_O:pktcEventLogCorrelationId,_z:pktcEventLogAdditionalInfo,'pktcEventConformance':pktcEventConformance,'pktcEventCompliances':pktcEventCompliances,'pktcEventBasicCompliance':pktcEventBasicCompliance,'pktcEventGroups':pktcEventGroups,_A5:pktcEventGroup,_A6:pktcEventNotificationGroup})