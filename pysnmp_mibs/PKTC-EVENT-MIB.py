_n='pktcEventNotificationGroup'
_m='pktcEventGroup'
_l='pktcDevEvTrap'
_k='pktcDevEvInform'
_j='pktcDevEvLogAdditionalInfo'
_i='pktcDevEvLogTargetInfo'
_h='pktcDevEvLogType'
_g='pktcDevEvLogText'
_f='pktcDevEventDescrText'
_e='pktcDevEventDescrReporting'
_d='pktcDevEventDescrLevel'
_c='pktcDevEventDescrFacility'
_b='pktcDevEvTransmissionStatus'
_a='pktcDevEvThrottleInterval'
_Z='pktcDevEvThrottleThreshold'
_Y='pktcDevEvThrottleAdminStatus'
_X='pktcDevEvSyslogUdpPort'
_W='pktcDevEvSyslogAddress'
_V='pktcDevEvSyslogAddressType'
_U='pktcDevEvControl'
_T='pktcDevEventDescrId'
_S='SnmpAdminString'
_R='InetPortNumber'
_Q='syslog'
_P='pktcDevEventDescrEnterprise'
_O='Unsigned32'
_N='ifPhysAddress'
_M='IF-MIB'
_L='pktcDevEvLogCorrelationId'
_K='pktcDevEvLogEndpointName'
_J='pktcDevEvLogId'
_I='pktcDevEvLogEnterprise'
_H='pktcDevEvLogTime'
_G='Integer32'
_F='pktcDevEvLogIndex'
_E='Bits'
_D='read-write'
_C='read-only'
_B='current'
_A='PKTC-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjPacketCable,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjPacketCable')
ifPhysAddress,=mibBuilder.importSymbols(_M,_N)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_R)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
pktcEventMib=ModuleIdentity((1,3,6,1,4,1,4491,2,2,3))
_PktcDevEventControl_ObjectIdentity=ObjectIdentity
pktcDevEventControl=_PktcDevEventControl_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,1))
class _PktcDevEvControl_Type(Bits):namedValues=NamedValues(*(('resetEventLogTable',0),('resetEventDescrTable',1)))
_PktcDevEvControl_Type.__name__=_E
_PktcDevEvControl_Object=MibScalar
pktcDevEvControl=_PktcDevEvControl_Object((1,3,6,1,4,1,4491,2,2,3,1,1),_PktcDevEvControl_Type())
pktcDevEvControl.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEvControl.setStatus(_B)
_PktcDevEvSyslogAddressType_Type=InetAddressType
_PktcDevEvSyslogAddressType_Object=MibScalar
pktcDevEvSyslogAddressType=_PktcDevEvSyslogAddressType_Object((1,3,6,1,4,1,4491,2,2,3,1,2),_PktcDevEvSyslogAddressType_Type())
pktcDevEvSyslogAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEvSyslogAddressType.setStatus(_B)
_PktcDevEvSyslogAddress_Type=InetAddress
_PktcDevEvSyslogAddress_Object=MibScalar
pktcDevEvSyslogAddress=_PktcDevEvSyslogAddress_Object((1,3,6,1,4,1,4491,2,2,3,1,3),_PktcDevEvSyslogAddress_Type())
pktcDevEvSyslogAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEvSyslogAddress.setStatus(_B)
class _PktcDevEvSyslogUdpPort_Type(InetPortNumber):defaultValue=514
_PktcDevEvSyslogUdpPort_Type.__name__=_R
_PktcDevEvSyslogUdpPort_Object=MibScalar
pktcDevEvSyslogUdpPort=_PktcDevEvSyslogUdpPort_Object((1,3,6,1,4,1,4491,2,2,3,1,4),_PktcDevEvSyslogUdpPort_Type())
pktcDevEvSyslogUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEvSyslogUdpPort.setStatus(_B)
_PktcDevEventThrottle_ObjectIdentity=ObjectIdentity
pktcDevEventThrottle=_PktcDevEventThrottle_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,2))
class _PktcDevEvThrottleAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unconstrained',1),('maintainBelowThreshold',2),('stopAtThreshold',3),('inhibited',4)))
_PktcDevEvThrottleAdminStatus_Type.__name__=_G
_PktcDevEvThrottleAdminStatus_Object=MibScalar
pktcDevEvThrottleAdminStatus=_PktcDevEvThrottleAdminStatus_Object((1,3,6,1,4,1,4491,2,2,3,2,1),_PktcDevEvThrottleAdminStatus_Type())
pktcDevEvThrottleAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEvThrottleAdminStatus.setStatus(_B)
class _PktcDevEvThrottleThreshold_Type(Unsigned32):defaultValue=2
_PktcDevEvThrottleThreshold_Type.__name__=_O
_PktcDevEvThrottleThreshold_Object=MibScalar
pktcDevEvThrottleThreshold=_PktcDevEvThrottleThreshold_Object((1,3,6,1,4,1,4491,2,2,3,2,2),_PktcDevEvThrottleThreshold_Type())
pktcDevEvThrottleThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEvThrottleThreshold.setStatus(_B)
class _PktcDevEvThrottleInterval_Type(Unsigned32):defaultValue=1
_PktcDevEvThrottleInterval_Type.__name__=_O
_PktcDevEvThrottleInterval_Object=MibScalar
pktcDevEvThrottleInterval=_PktcDevEvThrottleInterval_Object((1,3,6,1,4,1,4491,2,2,3,2,3),_PktcDevEvThrottleInterval_Type())
pktcDevEvThrottleInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEvThrottleInterval.setStatus(_B)
if mibBuilder.loadTexts:pktcDevEvThrottleInterval.setUnits('seconds')
_PktcDevEventStatus_ObjectIdentity=ObjectIdentity
pktcDevEventStatus=_PktcDevEventStatus_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,3))
class _PktcDevEvTransmissionStatus_Type(Bits):namedValues=NamedValues(*(('syslogThrottled',0),('snmpThrottled',1),('validSyslogServerAbsent',2),('validSnmpManagerAbsent',3),('syslogTransmitError',4),('snmpTransmitError',5)))
_PktcDevEvTransmissionStatus_Type.__name__=_E
_PktcDevEvTransmissionStatus_Object=MibScalar
pktcDevEvTransmissionStatus=_PktcDevEvTransmissionStatus_Object((1,3,6,1,4,1,4491,2,2,3,3,1),_PktcDevEvTransmissionStatus_Type())
pktcDevEvTransmissionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvTransmissionStatus.setStatus(_B)
_PktcDevEventDescr_ObjectIdentity=ObjectIdentity
pktcDevEventDescr=_PktcDevEventDescr_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,4))
_PktcDevEventDescrTable_Object=MibTable
pktcDevEventDescrTable=_PktcDevEventDescrTable_Object((1,3,6,1,4,1,4491,2,2,3,4,1))
if mibBuilder.loadTexts:pktcDevEventDescrTable.setStatus(_B)
_PktcDevEventDescrEntry_Object=MibTableRow
pktcDevEventDescrEntry=_PktcDevEventDescrEntry_Object((1,3,6,1,4,1,4491,2,2,3,4,1,1))
pktcDevEventDescrEntry.setIndexNames((0,_A,_T),(0,_A,_P))
if mibBuilder.loadTexts:pktcDevEventDescrEntry.setStatus(_B)
_PktcDevEventDescrId_Type=Unsigned32
_PktcDevEventDescrId_Object=MibTableColumn
pktcDevEventDescrId=_PktcDevEventDescrId_Object((1,3,6,1,4,1,4491,2,2,3,4,1,1,1),_PktcDevEventDescrId_Type())
pktcDevEventDescrId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pktcDevEventDescrId.setStatus(_B)
_PktcDevEventDescrEnterprise_Type=Unsigned32
_PktcDevEventDescrEnterprise_Object=MibTableColumn
pktcDevEventDescrEnterprise=_PktcDevEventDescrEnterprise_Object((1,3,6,1,4,1,4491,2,2,3,4,1,1,2),_PktcDevEventDescrEnterprise_Type())
pktcDevEventDescrEnterprise.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEventDescrEnterprise.setStatus(_B)
class _PktcDevEventDescrFacility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('user',1),('mail',2),('daemon',3),('auth',4),(_Q,5),('lpr',6),('news',7),('uucp',8),('cron',9),('authPriv',10),('ftp',11),('ntp',12),('security',13),('console',14),('clockDaemon',15),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
_PktcDevEventDescrFacility_Type.__name__=_G
_PktcDevEventDescrFacility_Object=MibTableColumn
pktcDevEventDescrFacility=_PktcDevEventDescrFacility_Object((1,3,6,1,4,1,4491,2,2,3,4,1,1,3),_PktcDevEventDescrFacility_Type())
pktcDevEventDescrFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEventDescrFacility.setStatus(_B)
class _PktcDevEventDescrLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_PktcDevEventDescrLevel_Type.__name__=_G
_PktcDevEventDescrLevel_Object=MibTableColumn
pktcDevEventDescrLevel=_PktcDevEventDescrLevel_Object((1,3,6,1,4,1,4491,2,2,3,4,1,1,4),_PktcDevEventDescrLevel_Type())
pktcDevEventDescrLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEventDescrLevel.setStatus(_B)
class _PktcDevEventDescrReporting_Type(Bits):namedValues=NamedValues(*(('local',0),(_Q,1),('snmpTrap',2),('snmpInform',3)))
_PktcDevEventDescrReporting_Type.__name__=_E
_PktcDevEventDescrReporting_Object=MibTableColumn
pktcDevEventDescrReporting=_PktcDevEventDescrReporting_Object((1,3,6,1,4,1,4491,2,2,3,4,1,1,5),_PktcDevEventDescrReporting_Type())
pktcDevEventDescrReporting.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEventDescrReporting.setStatus(_B)
class _PktcDevEventDescrText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PktcDevEventDescrText_Type.__name__=_S
_PktcDevEventDescrText_Object=MibTableColumn
pktcDevEventDescrText=_PktcDevEventDescrText_Object((1,3,6,1,4,1,4491,2,2,3,4,1,1,6),_PktcDevEventDescrText_Type())
pktcDevEventDescrText.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDevEventDescrText.setStatus(_B)
_PktcDevEventLog_ObjectIdentity=ObjectIdentity
pktcDevEventLog=_PktcDevEventLog_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,5))
_PktcDevEventLogTable_Object=MibTable
pktcDevEventLogTable=_PktcDevEventLogTable_Object((1,3,6,1,4,1,4491,2,2,3,5,1))
if mibBuilder.loadTexts:pktcDevEventLogTable.setStatus(_B)
_PktcDevEventLogEntry_Object=MibTableRow
pktcDevEventLogEntry=_PktcDevEventLogEntry_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1))
pktcDevEventLogEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:pktcDevEventLogEntry.setStatus(_B)
_PktcDevEvLogIndex_Type=Unsigned32
_PktcDevEvLogIndex_Object=MibTableColumn
pktcDevEvLogIndex=_PktcDevEvLogIndex_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,1),_PktcDevEvLogIndex_Type())
pktcDevEvLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogIndex.setStatus(_B)
_PktcDevEvLogTime_Type=DateAndTime
_PktcDevEvLogTime_Object=MibTableColumn
pktcDevEvLogTime=_PktcDevEvLogTime_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,2),_PktcDevEvLogTime_Type())
pktcDevEvLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogTime.setStatus(_B)
_PktcDevEvLogEnterprise_Type=Unsigned32
_PktcDevEvLogEnterprise_Object=MibTableColumn
pktcDevEvLogEnterprise=_PktcDevEvLogEnterprise_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,3),_PktcDevEvLogEnterprise_Type())
pktcDevEvLogEnterprise.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogEnterprise.setStatus(_B)
_PktcDevEvLogId_Type=Unsigned32
_PktcDevEvLogId_Object=MibTableColumn
pktcDevEvLogId=_PktcDevEvLogId_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,4),_PktcDevEvLogId_Type())
pktcDevEvLogId.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogId.setStatus(_B)
_PktcDevEvLogText_Type=SnmpAdminString
_PktcDevEvLogText_Object=MibTableColumn
pktcDevEvLogText=_PktcDevEvLogText_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,5),_PktcDevEvLogText_Type())
pktcDevEvLogText.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogText.setStatus(_B)
_PktcDevEvLogEndpointName_Type=SnmpAdminString
_PktcDevEvLogEndpointName_Object=MibTableColumn
pktcDevEvLogEndpointName=_PktcDevEvLogEndpointName_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,6),_PktcDevEvLogEndpointName_Type())
pktcDevEvLogEndpointName.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogEndpointName.setStatus(_B)
class _PktcDevEvLogType_Type(Bits):namedValues=NamedValues(*(('local',0),(_Q,1),('trap',2),('inform',3)))
_PktcDevEvLogType_Type.__name__=_E
_PktcDevEvLogType_Object=MibTableColumn
pktcDevEvLogType=_PktcDevEvLogType_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,7),_PktcDevEvLogType_Type())
pktcDevEvLogType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogType.setStatus(_B)
_PktcDevEvLogTargetInfo_Type=SnmpAdminString
_PktcDevEvLogTargetInfo_Object=MibTableColumn
pktcDevEvLogTargetInfo=_PktcDevEvLogTargetInfo_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,8),_PktcDevEvLogTargetInfo_Type())
pktcDevEvLogTargetInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogTargetInfo.setStatus(_B)
_PktcDevEvLogCorrelationId_Type=Unsigned32
_PktcDevEvLogCorrelationId_Object=MibTableColumn
pktcDevEvLogCorrelationId=_PktcDevEvLogCorrelationId_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,9),_PktcDevEvLogCorrelationId_Type())
pktcDevEvLogCorrelationId.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogCorrelationId.setStatus(_B)
_PktcDevEvLogAdditionalInfo_Type=SnmpAdminString
_PktcDevEvLogAdditionalInfo_Object=MibTableColumn
pktcDevEvLogAdditionalInfo=_PktcDevEvLogAdditionalInfo_Object((1,3,6,1,4,1,4491,2,2,3,5,1,1,10),_PktcDevEvLogAdditionalInfo_Type())
pktcDevEvLogAdditionalInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDevEvLogAdditionalInfo.setStatus(_B)
_PktcDevEvNotification_ObjectIdentity=ObjectIdentity
pktcDevEvNotification=_PktcDevEvNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,6))
_PktcDevEvNotificationIndex_ObjectIdentity=ObjectIdentity
pktcDevEvNotificationIndex=_PktcDevEvNotificationIndex_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,6,0))
_PktcEventConformance_ObjectIdentity=ObjectIdentity
pktcEventConformance=_PktcEventConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,7))
_PktcEventCompliances_ObjectIdentity=ObjectIdentity
pktcEventCompliances=_PktcEventCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,7,1))
_PktcEventGroups_ObjectIdentity=ObjectIdentity
pktcEventGroups=_PktcEventGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,3,7,2))
pktcEventGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,3,7,2,1))
pktcEventGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_P),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_g),(_A,_K),(_A,_h),(_A,_i),(_A,_L),(_A,_j)))
if mibBuilder.loadTexts:pktcEventGroup.setStatus(_B)
pktcDevEvInform=NotificationType((1,3,6,1,4,1,4491,2,2,3,6,0,1))
pktcDevEvInform.setObjects(*((_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_M,_N)))
if mibBuilder.loadTexts:pktcDevEvInform.setStatus(_B)
pktcDevEvTrap=NotificationType((1,3,6,1,4,1,4491,2,2,3,6,0,2))
pktcDevEvTrap.setObjects(*((_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_M,_N)))
if mibBuilder.loadTexts:pktcDevEvTrap.setStatus(_B)
pktcEventNotificationGroup=NotificationGroup((1,3,6,1,4,1,4491,2,2,3,7,2,2))
pktcEventNotificationGroup.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:pktcEventNotificationGroup.setStatus(_B)
pktcEventBasicCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,3,7,1,3))
pktcEventBasicCompliance.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:pktcEventBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pktcEventMib':pktcEventMib,'pktcDevEventControl':pktcDevEventControl,_U:pktcDevEvControl,_V:pktcDevEvSyslogAddressType,_W:pktcDevEvSyslogAddress,_X:pktcDevEvSyslogUdpPort,'pktcDevEventThrottle':pktcDevEventThrottle,_Y:pktcDevEvThrottleAdminStatus,_Z:pktcDevEvThrottleThreshold,_a:pktcDevEvThrottleInterval,'pktcDevEventStatus':pktcDevEventStatus,_b:pktcDevEvTransmissionStatus,'pktcDevEventDescr':pktcDevEventDescr,'pktcDevEventDescrTable':pktcDevEventDescrTable,'pktcDevEventDescrEntry':pktcDevEventDescrEntry,_T:pktcDevEventDescrId,_P:pktcDevEventDescrEnterprise,_c:pktcDevEventDescrFacility,_d:pktcDevEventDescrLevel,_e:pktcDevEventDescrReporting,_f:pktcDevEventDescrText,'pktcDevEventLog':pktcDevEventLog,'pktcDevEventLogTable':pktcDevEventLogTable,'pktcDevEventLogEntry':pktcDevEventLogEntry,_F:pktcDevEvLogIndex,_H:pktcDevEvLogTime,_I:pktcDevEvLogEnterprise,_J:pktcDevEvLogId,_g:pktcDevEvLogText,_K:pktcDevEvLogEndpointName,_h:pktcDevEvLogType,_i:pktcDevEvLogTargetInfo,_L:pktcDevEvLogCorrelationId,_j:pktcDevEvLogAdditionalInfo,'pktcDevEvNotification':pktcDevEvNotification,'pktcDevEvNotificationIndex':pktcDevEvNotificationIndex,_k:pktcDevEvInform,_l:pktcDevEvTrap,'pktcEventConformance':pktcEventConformance,'pktcEventCompliances':pktcEventCompliances,'pktcEventBasicCompliance':pktcEventBasicCompliance,'pktcEventGroups':pktcEventGroups,_m:pktcEventGroup,_n:pktcEventNotificationGroup})