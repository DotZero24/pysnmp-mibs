_A3='ciscoFirewallMIBNotificationGroupRev1'
_A2='ciscoFirewallMIBEventsGroup'
_A1='cfwGenericNotification'
_A0='cfwAuthNotification'
_z='cfwAccessNotification'
_y='cfwConnNotification'
_x='cfwContentInspectNotification'
_w='cfwSecurityNotification'
_v='cfwConnectionStatValue'
_u='cfwConnectionStatCount'
_t='cfwConnectionStatDescription'
_s='cfwBufferStatValue'
_r='cfwBufferStatInformation'
_q='cfwHardwareStatusDetail'
_p='cfwHardwareStatusValue'
_o='cfwHardwareInformation'
_n='cfwNetEventDescription'
_m='cfwNetEventIdentity'
_l='cfwNetEventServiceInformation'
_k='cfwNetEventService'
_j='cfwNetEventInsideDstIpPort'
_i='cfwNetEventDstIpPort'
_h='cfwNetEventInsideSrcIpPort'
_g='cfwNetEventSrcIpPort'
_f='cfwNetEventInsideDstIpAddress'
_e='cfwNetEventDstIpAddress'
_d='cfwNetEventInsideSrcIpAddress'
_c='cfwNetEventSrcIpAddress'
_b='cfwNetEventInterface'
_a='cfwNetEventsTableLastRow'
_Z='cfwBasicEventsTableLastRow'
_Y='Connections per second'
_X='cfwConnectionStatType'
_W='cfwConnectionStatService'
_V='cfwBufferStatType'
_U='cfwBufferStatSize'
_T='cfwHardwareType'
_S='cfwNetEventIndex'
_R='cfwBasicEventIndex'
_Q='ciscoFirewallMIBStatisticsGroup'
_P='cfwBasicGenericEventType'
_O='cfwBasicAuthenticationEventType'
_N='cfwBasicAccessEventType'
_M='cfwBasicConnectionEventType'
_L='cfwBasicContentInspEventType'
_K='cfwBasicSecurityEventType'
_J='Integer32'
_I='error'
_H='not-accessible'
_G='other'
_F='cfwBasicEventDetailsTableRow'
_E='cfwBasicEventDescription'
_D='cfwBasicEventTime'
_C='read-only'
_B='current'
_A='CISCO-FIREWALL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','TextualConvention')
ciscoFirewallMIB=ModuleIdentity((1,3,6,1,4,1,9,9,147))
if mibBuilder.loadTexts:ciscoFirewallMIB.setRevisions(('2020-10-01 00:00','2005-12-06 00:00','1999-04-29 12:00'))
class ResourceStatistics(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('highUse',1),('highLoad',2),('maximum',3),('minimum',4),('low',5),('high',6),('average',7),('free',8),('inUse',9)))
class Hardware(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('memory',1),('disk',2),('power',3),('netInterface',4),('cpu',5),('primaryUnit',6),('secondaryUnit',7),(_G,8)))
class Services(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41)));namedValues=NamedValues(*(('otherFWService',1),('fileXferFtp',2),('fileXferTftp',3),('fileXferFtps',4),('loginTelnet',5),('loginRlogin',6),('loginTelnets',7),('remoteExecSunRPC',8),('remoteExecMSRPC',9),('remoteExecRsh',10),('remoteExecXserver',11),('webHttp',12),('webHttps',13),('mailSmtp',14),('multimediaStreamworks',15),('multimediaH323',16),('multimediaNetShow',17),('multimediaVDOLive',18),('multimediaRealAV',19),('multimediaRTSP',20),('dbOracle',21),('dbMSsql',22),('contInspProgLang',23),('contInspUrl',24),('directoryNis',25),('directoryDns',26),('directoryNetbiosns',27),('directoryNetbiosdgm',28),('directoryNetbiosssn',29),('directoryWins',30),('qryWhois',31),('qryFinger',32),('qryIdent',33),('fsNfsStatus',34),('fsNfs',35),('fsCifs',36),('protoIcmp',37),('protoTcp',38),('protoUdp',39),('protoIp',40),('protoSnmp',41)))
class HardwareStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),('up',2),('down',3),(_I,4),('overTemp',5),('busy',6),('noMedia',7),('backup',8),('active',9),('standby',10)))
class SecurityEvent(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_G,1),('none',2),('dos',3),('recon',4),('pakFwd',5),('addrSpoof',6),('svcSpoof',7),('thirdParty',8),('complete',9),('invalPak',10),('illegCom',11),('policy',12)))
class ContentInspectionEvent(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('okay',2),(_I,3),('found',4),('clean',5),('reject',6),('saved',7)))
class ConnectionEvent(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),('accept',2),(_I,3),('drop',4),('close',5),('timeout',6),('refused',7),('reset',8),('noResp',9)))
class ConnectionStat(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('totalOpen',2),('currentOpen',3),('currentClosing',4),('currentHalfOpen',5),('currentInUse',6),('high',7)))
class AccessEvent(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('grant',2),('deny',3),('denyMult',4),(_I,5)))
class AuthenticationEvent(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('succ',2),(_I,3),('fail',4),('succPriv',5),('failPriv',6),('failMult',7)))
class GenericEvent(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('abnormal',1),('okay',2),(_I,3)))
_CiscoFirewallMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFirewallMIBObjects=_CiscoFirewallMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,147,1))
_CfwEvents_ObjectIdentity=ObjectIdentity
cfwEvents=_CfwEvents_ObjectIdentity((1,3,6,1,4,1,9,9,147,1,1))
_CfwBasicEvents_ObjectIdentity=ObjectIdentity
cfwBasicEvents=_CfwBasicEvents_ObjectIdentity((1,3,6,1,4,1,9,9,147,1,1,1))
_CfwBasicEventsTableLastRow_Type=Unsigned32
_CfwBasicEventsTableLastRow_Object=MibScalar
cfwBasicEventsTableLastRow=_CfwBasicEventsTableLastRow_Object((1,3,6,1,4,1,9,9,147,1,1,1,1),_CfwBasicEventsTableLastRow_Type())
cfwBasicEventsTableLastRow.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicEventsTableLastRow.setStatus(_B)
_CfwBasicEventsTable_Object=MibTable
cfwBasicEventsTable=_CfwBasicEventsTable_Object((1,3,6,1,4,1,9,9,147,1,1,1,2))
if mibBuilder.loadTexts:cfwBasicEventsTable.setStatus(_B)
_CfwBasicEventsEntry_Object=MibTableRow
cfwBasicEventsEntry=_CfwBasicEventsEntry_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1))
cfwBasicEventsEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:cfwBasicEventsEntry.setStatus(_B)
_CfwBasicEventIndex_Type=Unsigned32
_CfwBasicEventIndex_Object=MibTableColumn
cfwBasicEventIndex=_CfwBasicEventIndex_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,1),_CfwBasicEventIndex_Type())
cfwBasicEventIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cfwBasicEventIndex.setStatus(_B)
_CfwBasicEventTime_Type=DateAndTime
_CfwBasicEventTime_Object=MibTableColumn
cfwBasicEventTime=_CfwBasicEventTime_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,2),_CfwBasicEventTime_Type())
cfwBasicEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicEventTime.setStatus(_B)
_CfwBasicSecurityEventType_Type=SecurityEvent
_CfwBasicSecurityEventType_Object=MibTableColumn
cfwBasicSecurityEventType=_CfwBasicSecurityEventType_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,3),_CfwBasicSecurityEventType_Type())
cfwBasicSecurityEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicSecurityEventType.setStatus(_B)
_CfwBasicContentInspEventType_Type=ContentInspectionEvent
_CfwBasicContentInspEventType_Object=MibTableColumn
cfwBasicContentInspEventType=_CfwBasicContentInspEventType_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,4),_CfwBasicContentInspEventType_Type())
cfwBasicContentInspEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicContentInspEventType.setStatus(_B)
_CfwBasicConnectionEventType_Type=ConnectionEvent
_CfwBasicConnectionEventType_Object=MibTableColumn
cfwBasicConnectionEventType=_CfwBasicConnectionEventType_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,5),_CfwBasicConnectionEventType_Type())
cfwBasicConnectionEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicConnectionEventType.setStatus(_B)
_CfwBasicAccessEventType_Type=AccessEvent
_CfwBasicAccessEventType_Object=MibTableColumn
cfwBasicAccessEventType=_CfwBasicAccessEventType_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,6),_CfwBasicAccessEventType_Type())
cfwBasicAccessEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicAccessEventType.setStatus(_B)
_CfwBasicAuthenticationEventType_Type=AuthenticationEvent
_CfwBasicAuthenticationEventType_Object=MibTableColumn
cfwBasicAuthenticationEventType=_CfwBasicAuthenticationEventType_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,7),_CfwBasicAuthenticationEventType_Type())
cfwBasicAuthenticationEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicAuthenticationEventType.setStatus(_B)
_CfwBasicGenericEventType_Type=GenericEvent
_CfwBasicGenericEventType_Object=MibTableColumn
cfwBasicGenericEventType=_CfwBasicGenericEventType_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,8),_CfwBasicGenericEventType_Type())
cfwBasicGenericEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicGenericEventType.setStatus(_B)
_CfwBasicEventDescription_Type=SnmpAdminString
_CfwBasicEventDescription_Object=MibTableColumn
cfwBasicEventDescription=_CfwBasicEventDescription_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,9),_CfwBasicEventDescription_Type())
cfwBasicEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicEventDescription.setStatus(_B)
_CfwBasicEventDetailsTableRow_Type=RowPointer
_CfwBasicEventDetailsTableRow_Object=MibTableColumn
cfwBasicEventDetailsTableRow=_CfwBasicEventDetailsTableRow_Object((1,3,6,1,4,1,9,9,147,1,1,1,2,1,10),_CfwBasicEventDetailsTableRow_Type())
cfwBasicEventDetailsTableRow.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBasicEventDetailsTableRow.setStatus(_B)
_CfwNetEvents_ObjectIdentity=ObjectIdentity
cfwNetEvents=_CfwNetEvents_ObjectIdentity((1,3,6,1,4,1,9,9,147,1,1,2))
_CfwNetEventsTableLastRow_Type=Unsigned32
_CfwNetEventsTableLastRow_Object=MibScalar
cfwNetEventsTableLastRow=_CfwNetEventsTableLastRow_Object((1,3,6,1,4,1,9,9,147,1,1,2,1),_CfwNetEventsTableLastRow_Type())
cfwNetEventsTableLastRow.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventsTableLastRow.setStatus(_B)
_CfwNetEventsTable_Object=MibTable
cfwNetEventsTable=_CfwNetEventsTable_Object((1,3,6,1,4,1,9,9,147,1,1,2,2))
if mibBuilder.loadTexts:cfwNetEventsTable.setStatus(_B)
_CfwNetEventsEntry_Object=MibTableRow
cfwNetEventsEntry=_CfwNetEventsEntry_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1))
cfwNetEventsEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:cfwNetEventsEntry.setStatus(_B)
_CfwNetEventIndex_Type=Unsigned32
_CfwNetEventIndex_Object=MibTableColumn
cfwNetEventIndex=_CfwNetEventIndex_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,1),_CfwNetEventIndex_Type())
cfwNetEventIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cfwNetEventIndex.setStatus(_B)
_CfwNetEventInterface_Type=InterfaceIndexOrZero
_CfwNetEventInterface_Object=MibTableColumn
cfwNetEventInterface=_CfwNetEventInterface_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,2),_CfwNetEventInterface_Type())
cfwNetEventInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventInterface.setStatus(_B)
_CfwNetEventSrcIpAddress_Type=IpAddress
_CfwNetEventSrcIpAddress_Object=MibTableColumn
cfwNetEventSrcIpAddress=_CfwNetEventSrcIpAddress_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,3),_CfwNetEventSrcIpAddress_Type())
cfwNetEventSrcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventSrcIpAddress.setStatus(_B)
_CfwNetEventInsideSrcIpAddress_Type=IpAddress
_CfwNetEventInsideSrcIpAddress_Object=MibTableColumn
cfwNetEventInsideSrcIpAddress=_CfwNetEventInsideSrcIpAddress_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,4),_CfwNetEventInsideSrcIpAddress_Type())
cfwNetEventInsideSrcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventInsideSrcIpAddress.setStatus(_B)
_CfwNetEventDstIpAddress_Type=IpAddress
_CfwNetEventDstIpAddress_Object=MibTableColumn
cfwNetEventDstIpAddress=_CfwNetEventDstIpAddress_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,5),_CfwNetEventDstIpAddress_Type())
cfwNetEventDstIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventDstIpAddress.setStatus(_B)
_CfwNetEventInsideDstIpAddress_Type=IpAddress
_CfwNetEventInsideDstIpAddress_Object=MibTableColumn
cfwNetEventInsideDstIpAddress=_CfwNetEventInsideDstIpAddress_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,6),_CfwNetEventInsideDstIpAddress_Type())
cfwNetEventInsideDstIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventInsideDstIpAddress.setStatus(_B)
class _CfwNetEventSrcIpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfwNetEventSrcIpPort_Type.__name__=_J
_CfwNetEventSrcIpPort_Object=MibTableColumn
cfwNetEventSrcIpPort=_CfwNetEventSrcIpPort_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,7),_CfwNetEventSrcIpPort_Type())
cfwNetEventSrcIpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventSrcIpPort.setStatus(_B)
class _CfwNetEventInsideSrcIpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfwNetEventInsideSrcIpPort_Type.__name__=_J
_CfwNetEventInsideSrcIpPort_Object=MibTableColumn
cfwNetEventInsideSrcIpPort=_CfwNetEventInsideSrcIpPort_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,8),_CfwNetEventInsideSrcIpPort_Type())
cfwNetEventInsideSrcIpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventInsideSrcIpPort.setStatus(_B)
class _CfwNetEventDstIpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfwNetEventDstIpPort_Type.__name__=_J
_CfwNetEventDstIpPort_Object=MibTableColumn
cfwNetEventDstIpPort=_CfwNetEventDstIpPort_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,9),_CfwNetEventDstIpPort_Type())
cfwNetEventDstIpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventDstIpPort.setStatus(_B)
class _CfwNetEventInsideDstIpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfwNetEventInsideDstIpPort_Type.__name__=_J
_CfwNetEventInsideDstIpPort_Object=MibTableColumn
cfwNetEventInsideDstIpPort=_CfwNetEventInsideDstIpPort_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,10),_CfwNetEventInsideDstIpPort_Type())
cfwNetEventInsideDstIpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventInsideDstIpPort.setStatus(_B)
_CfwNetEventService_Type=Services
_CfwNetEventService_Object=MibTableColumn
cfwNetEventService=_CfwNetEventService_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,11),_CfwNetEventService_Type())
cfwNetEventService.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventService.setStatus(_B)
_CfwNetEventServiceInformation_Type=SnmpAdminString
_CfwNetEventServiceInformation_Object=MibTableColumn
cfwNetEventServiceInformation=_CfwNetEventServiceInformation_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,12),_CfwNetEventServiceInformation_Type())
cfwNetEventServiceInformation.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventServiceInformation.setStatus(_B)
_CfwNetEventIdentity_Type=SnmpAdminString
_CfwNetEventIdentity_Object=MibTableColumn
cfwNetEventIdentity=_CfwNetEventIdentity_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,13),_CfwNetEventIdentity_Type())
cfwNetEventIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventIdentity.setStatus(_B)
_CfwNetEventDescription_Type=SnmpAdminString
_CfwNetEventDescription_Object=MibTableColumn
cfwNetEventDescription=_CfwNetEventDescription_Object((1,3,6,1,4,1,9,9,147,1,1,2,2,1,14),_CfwNetEventDescription_Type())
cfwNetEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwNetEventDescription.setStatus(_B)
_CfwSystem_ObjectIdentity=ObjectIdentity
cfwSystem=_CfwSystem_ObjectIdentity((1,3,6,1,4,1,9,9,147,1,2))
_CfwStatus_ObjectIdentity=ObjectIdentity
cfwStatus=_CfwStatus_ObjectIdentity((1,3,6,1,4,1,9,9,147,1,2,1))
_CfwHardwareStatusTable_Object=MibTable
cfwHardwareStatusTable=_CfwHardwareStatusTable_Object((1,3,6,1,4,1,9,9,147,1,2,1,1))
if mibBuilder.loadTexts:cfwHardwareStatusTable.setStatus(_B)
_CfwHardwareStatusEntry_Object=MibTableRow
cfwHardwareStatusEntry=_CfwHardwareStatusEntry_Object((1,3,6,1,4,1,9,9,147,1,2,1,1,1))
cfwHardwareStatusEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:cfwHardwareStatusEntry.setStatus(_B)
_CfwHardwareType_Type=Hardware
_CfwHardwareType_Object=MibTableColumn
cfwHardwareType=_CfwHardwareType_Object((1,3,6,1,4,1,9,9,147,1,2,1,1,1,1),_CfwHardwareType_Type())
cfwHardwareType.setMaxAccess(_H)
if mibBuilder.loadTexts:cfwHardwareType.setStatus(_B)
_CfwHardwareInformation_Type=SnmpAdminString
_CfwHardwareInformation_Object=MibTableColumn
cfwHardwareInformation=_CfwHardwareInformation_Object((1,3,6,1,4,1,9,9,147,1,2,1,1,1,2),_CfwHardwareInformation_Type())
cfwHardwareInformation.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwHardwareInformation.setStatus(_B)
_CfwHardwareStatusValue_Type=HardwareStatus
_CfwHardwareStatusValue_Object=MibTableColumn
cfwHardwareStatusValue=_CfwHardwareStatusValue_Object((1,3,6,1,4,1,9,9,147,1,2,1,1,1,3),_CfwHardwareStatusValue_Type())
cfwHardwareStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwHardwareStatusValue.setStatus(_B)
_CfwHardwareStatusDetail_Type=SnmpAdminString
_CfwHardwareStatusDetail_Object=MibTableColumn
cfwHardwareStatusDetail=_CfwHardwareStatusDetail_Object((1,3,6,1,4,1,9,9,147,1,2,1,1,1,4),_CfwHardwareStatusDetail_Type())
cfwHardwareStatusDetail.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwHardwareStatusDetail.setStatus(_B)
_CfwStatistics_ObjectIdentity=ObjectIdentity
cfwStatistics=_CfwStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,147,1,2,2))
_CfwBufferStatsTable_Object=MibTable
cfwBufferStatsTable=_CfwBufferStatsTable_Object((1,3,6,1,4,1,9,9,147,1,2,2,1))
if mibBuilder.loadTexts:cfwBufferStatsTable.setStatus(_B)
_CfwBufferStatsEntry_Object=MibTableRow
cfwBufferStatsEntry=_CfwBufferStatsEntry_Object((1,3,6,1,4,1,9,9,147,1,2,2,1,1))
cfwBufferStatsEntry.setIndexNames((0,_A,_U),(0,_A,_V))
if mibBuilder.loadTexts:cfwBufferStatsEntry.setStatus(_B)
_CfwBufferStatSize_Type=Unsigned32
_CfwBufferStatSize_Object=MibTableColumn
cfwBufferStatSize=_CfwBufferStatSize_Object((1,3,6,1,4,1,9,9,147,1,2,2,1,1,1),_CfwBufferStatSize_Type())
cfwBufferStatSize.setMaxAccess(_H)
if mibBuilder.loadTexts:cfwBufferStatSize.setStatus(_B)
_CfwBufferStatType_Type=ResourceStatistics
_CfwBufferStatType_Object=MibTableColumn
cfwBufferStatType=_CfwBufferStatType_Object((1,3,6,1,4,1,9,9,147,1,2,2,1,1,2),_CfwBufferStatType_Type())
cfwBufferStatType.setMaxAccess(_H)
if mibBuilder.loadTexts:cfwBufferStatType.setStatus(_B)
_CfwBufferStatInformation_Type=SnmpAdminString
_CfwBufferStatInformation_Object=MibTableColumn
cfwBufferStatInformation=_CfwBufferStatInformation_Object((1,3,6,1,4,1,9,9,147,1,2,2,1,1,3),_CfwBufferStatInformation_Type())
cfwBufferStatInformation.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBufferStatInformation.setStatus(_B)
_CfwBufferStatValue_Type=Gauge32
_CfwBufferStatValue_Object=MibTableColumn
cfwBufferStatValue=_CfwBufferStatValue_Object((1,3,6,1,4,1,9,9,147,1,2,2,1,1,4),_CfwBufferStatValue_Type())
cfwBufferStatValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwBufferStatValue.setStatus(_B)
_CfwConnectionStatTable_Object=MibTable
cfwConnectionStatTable=_CfwConnectionStatTable_Object((1,3,6,1,4,1,9,9,147,1,2,2,2))
if mibBuilder.loadTexts:cfwConnectionStatTable.setStatus(_B)
_CfwConnectionStatEntry_Object=MibTableRow
cfwConnectionStatEntry=_CfwConnectionStatEntry_Object((1,3,6,1,4,1,9,9,147,1,2,2,2,1))
cfwConnectionStatEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:cfwConnectionStatEntry.setStatus(_B)
_CfwConnectionStatService_Type=Services
_CfwConnectionStatService_Object=MibTableColumn
cfwConnectionStatService=_CfwConnectionStatService_Object((1,3,6,1,4,1,9,9,147,1,2,2,2,1,1),_CfwConnectionStatService_Type())
cfwConnectionStatService.setMaxAccess(_H)
if mibBuilder.loadTexts:cfwConnectionStatService.setStatus(_B)
_CfwConnectionStatType_Type=ConnectionStat
_CfwConnectionStatType_Object=MibTableColumn
cfwConnectionStatType=_CfwConnectionStatType_Object((1,3,6,1,4,1,9,9,147,1,2,2,2,1,2),_CfwConnectionStatType_Type())
cfwConnectionStatType.setMaxAccess(_H)
if mibBuilder.loadTexts:cfwConnectionStatType.setStatus(_B)
_CfwConnectionStatDescription_Type=SnmpAdminString
_CfwConnectionStatDescription_Object=MibTableColumn
cfwConnectionStatDescription=_CfwConnectionStatDescription_Object((1,3,6,1,4,1,9,9,147,1,2,2,2,1,3),_CfwConnectionStatDescription_Type())
cfwConnectionStatDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwConnectionStatDescription.setStatus(_B)
_CfwConnectionStatCount_Type=Counter32
_CfwConnectionStatCount_Object=MibTableColumn
cfwConnectionStatCount=_CfwConnectionStatCount_Object((1,3,6,1,4,1,9,9,147,1,2,2,2,1,4),_CfwConnectionStatCount_Type())
cfwConnectionStatCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwConnectionStatCount.setStatus(_B)
_CfwConnectionStatValue_Type=Gauge32
_CfwConnectionStatValue_Object=MibTableColumn
cfwConnectionStatValue=_CfwConnectionStatValue_Object((1,3,6,1,4,1,9,9,147,1,2,2,2,1,5),_CfwConnectionStatValue_Type())
cfwConnectionStatValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwConnectionStatValue.setStatus(_B)
_CfwConnectionPerSecond_Type=Gauge32
_CfwConnectionPerSecond_Object=MibScalar
cfwConnectionPerSecond=_CfwConnectionPerSecond_Object((1,3,6,1,4,1,9,9,147,1,2,2,3),_CfwConnectionPerSecond_Type())
cfwConnectionPerSecond.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwConnectionPerSecond.setStatus(_B)
if mibBuilder.loadTexts:cfwConnectionPerSecond.setUnits(_Y)
_CfwConnectionPerSecondPeak_Type=Gauge32
_CfwConnectionPerSecondPeak_Object=MibScalar
cfwConnectionPerSecondPeak=_CfwConnectionPerSecondPeak_Object((1,3,6,1,4,1,9,9,147,1,2,2,4),_CfwConnectionPerSecondPeak_Type())
cfwConnectionPerSecondPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:cfwConnectionPerSecondPeak.setStatus(_B)
if mibBuilder.loadTexts:cfwConnectionPerSecondPeak.setUnits(_Y)
_CiscoFirewallMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoFirewallMIBNotificationPrefix=_CiscoFirewallMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,147,2))
_CiscoFirewallMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoFirewallMIBNotifications=_CiscoFirewallMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,147,2,0))
_CiscoFirewallMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFirewallMIBConformance=_CiscoFirewallMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,147,3))
_CiscoFirewallMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFirewallMIBCompliances=_CiscoFirewallMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,147,3,1))
_CiscoFirewallMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFirewallMIBGroups=_CiscoFirewallMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,147,3,2))
ciscoFirewallMIBEventsGroup=ObjectGroup((1,3,6,1,4,1,9,9,147,3,2,1))
ciscoFirewallMIBEventsGroup.setObjects(*((_A,_Z),(_A,_D),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_E),(_A,_F),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoFirewallMIBEventsGroup.setStatus(_B)
ciscoFirewallMIBStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,147,3,2,2))
ciscoFirewallMIBStatisticsGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ciscoFirewallMIBStatisticsGroup.setStatus(_B)
ciscoFirewallMIBNotificationGroup=ObjectGroup((1,3,6,1,4,1,9,9,147,3,2,3))
ciscoFirewallMIBNotificationGroup.setObjects(*((_A,_D),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ciscoFirewallMIBNotificationGroup.setStatus('obsolete')
cfwSecurityNotification=NotificationType((1,3,6,1,4,1,9,9,147,2,0,2))
cfwSecurityNotification.setObjects(*((_A,_D),(_A,_K),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:cfwSecurityNotification.setStatus(_B)
cfwContentInspectNotification=NotificationType((1,3,6,1,4,1,9,9,147,2,0,3))
cfwContentInspectNotification.setObjects(*((_A,_D),(_A,_L),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:cfwContentInspectNotification.setStatus(_B)
cfwConnNotification=NotificationType((1,3,6,1,4,1,9,9,147,2,0,4))
cfwConnNotification.setObjects(*((_A,_D),(_A,_M),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:cfwConnNotification.setStatus(_B)
cfwAccessNotification=NotificationType((1,3,6,1,4,1,9,9,147,2,0,5))
cfwAccessNotification.setObjects(*((_A,_D),(_A,_N),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:cfwAccessNotification.setStatus(_B)
cfwAuthNotification=NotificationType((1,3,6,1,4,1,9,9,147,2,0,6))
cfwAuthNotification.setObjects(*((_A,_D),(_A,_O),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:cfwAuthNotification.setStatus(_B)
cfwGenericNotification=NotificationType((1,3,6,1,4,1,9,9,147,2,0,7))
cfwGenericNotification.setObjects(*((_A,_D),(_A,_P),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:cfwGenericNotification.setStatus(_B)
ciscoFirewallMIBNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,147,3,2,4))
ciscoFirewallMIBNotificationGroupRev1.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ciscoFirewallMIBNotificationGroupRev1.setStatus(_B)
ciscoFirewallMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,147,3,1,1))
ciscoFirewallMIBCompliance.setObjects((_A,_Q))
if mibBuilder.loadTexts:ciscoFirewallMIBCompliance.setStatus('deprecated')
ciscoFirewallMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,147,3,1,2))
ciscoFirewallMIBComplianceRev1.setObjects(*((_A,_Q),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoFirewallMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ResourceStatistics':ResourceStatistics,'Hardware':Hardware,'Services':Services,'HardwareStatus':HardwareStatus,'SecurityEvent':SecurityEvent,'ContentInspectionEvent':ContentInspectionEvent,'ConnectionEvent':ConnectionEvent,'ConnectionStat':ConnectionStat,'AccessEvent':AccessEvent,'AuthenticationEvent':AuthenticationEvent,'GenericEvent':GenericEvent,'ciscoFirewallMIB':ciscoFirewallMIB,'ciscoFirewallMIBObjects':ciscoFirewallMIBObjects,'cfwEvents':cfwEvents,'cfwBasicEvents':cfwBasicEvents,_Z:cfwBasicEventsTableLastRow,'cfwBasicEventsTable':cfwBasicEventsTable,'cfwBasicEventsEntry':cfwBasicEventsEntry,_R:cfwBasicEventIndex,_D:cfwBasicEventTime,_K:cfwBasicSecurityEventType,_L:cfwBasicContentInspEventType,_M:cfwBasicConnectionEventType,_N:cfwBasicAccessEventType,_O:cfwBasicAuthenticationEventType,_P:cfwBasicGenericEventType,_E:cfwBasicEventDescription,_F:cfwBasicEventDetailsTableRow,'cfwNetEvents':cfwNetEvents,_a:cfwNetEventsTableLastRow,'cfwNetEventsTable':cfwNetEventsTable,'cfwNetEventsEntry':cfwNetEventsEntry,_S:cfwNetEventIndex,_b:cfwNetEventInterface,_c:cfwNetEventSrcIpAddress,_d:cfwNetEventInsideSrcIpAddress,_e:cfwNetEventDstIpAddress,_f:cfwNetEventInsideDstIpAddress,_g:cfwNetEventSrcIpPort,_h:cfwNetEventInsideSrcIpPort,_i:cfwNetEventDstIpPort,_j:cfwNetEventInsideDstIpPort,_k:cfwNetEventService,_l:cfwNetEventServiceInformation,_m:cfwNetEventIdentity,_n:cfwNetEventDescription,'cfwSystem':cfwSystem,'cfwStatus':cfwStatus,'cfwHardwareStatusTable':cfwHardwareStatusTable,'cfwHardwareStatusEntry':cfwHardwareStatusEntry,_T:cfwHardwareType,_o:cfwHardwareInformation,_p:cfwHardwareStatusValue,_q:cfwHardwareStatusDetail,'cfwStatistics':cfwStatistics,'cfwBufferStatsTable':cfwBufferStatsTable,'cfwBufferStatsEntry':cfwBufferStatsEntry,_U:cfwBufferStatSize,_V:cfwBufferStatType,_r:cfwBufferStatInformation,_s:cfwBufferStatValue,'cfwConnectionStatTable':cfwConnectionStatTable,'cfwConnectionStatEntry':cfwConnectionStatEntry,_W:cfwConnectionStatService,_X:cfwConnectionStatType,_t:cfwConnectionStatDescription,_u:cfwConnectionStatCount,_v:cfwConnectionStatValue,'cfwConnectionPerSecond':cfwConnectionPerSecond,'cfwConnectionPerSecondPeak':cfwConnectionPerSecondPeak,'ciscoFirewallMIBNotificationPrefix':ciscoFirewallMIBNotificationPrefix,'ciscoFirewallMIBNotifications':ciscoFirewallMIBNotifications,_w:cfwSecurityNotification,_x:cfwContentInspectNotification,_y:cfwConnNotification,_z:cfwAccessNotification,_A0:cfwAuthNotification,_A1:cfwGenericNotification,'ciscoFirewallMIBConformance':ciscoFirewallMIBConformance,'ciscoFirewallMIBCompliances':ciscoFirewallMIBCompliances,'ciscoFirewallMIBCompliance':ciscoFirewallMIBCompliance,'ciscoFirewallMIBComplianceRev1':ciscoFirewallMIBComplianceRev1,'ciscoFirewallMIBGroups':ciscoFirewallMIBGroups,_A2:ciscoFirewallMIBEventsGroup,_Q:ciscoFirewallMIBStatisticsGroup,'ciscoFirewallMIBNotificationGroup':ciscoFirewallMIBNotificationGroup,_A3:ciscoFirewallMIBNotificationGroupRev1})