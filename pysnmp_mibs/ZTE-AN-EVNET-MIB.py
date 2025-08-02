_r='zxAnEventReceiverIpAddr'
_q='zxAnEventRptCtrlResId'
_p='zxAnEventRptCtrlPrfRuleIndex'
_o='zxAnEventDefineReportChannelType'
_n='zxAnEventDefineCode'
_m='zxAnEventSyslogSvrIpAddr'
_l='notification'
_k='cleared'
_j='processingErrorEvent'
_i='environmentEvent'
_h='communicationsEvent'
_g='qualityOfServiceEvent'
_f='equipmentEvent'
_e='zxAnEventReceiverIndex'
_d='zxAnEventVlanCfgVlanId'
_c='zxAnEventIfCfgLogicalId'
_b='zxAnEventIfCfgIfType'
_a='zxAnEventIfCfgOnu'
_Z='zxAnEventIfCfgPort'
_Y='zxAnEventIfCfgSlot'
_X='zxAnEventIfCfgShelf'
_W='zxAnEventIfCfgRack'
_V='zxAnEventReportChannelType'
_U='zxAnEventCode'
_T='zxAnEventCtrlProfileName'
_S='critical'
_R='zxAnEventConfTrapOid'
_Q='zxAnEventRptCtrlPrfName'
_P='indeterminate'
_O='warning'
_N='minor'
_M='major'
_L='seconds'
_K='DisplayString'
_J='Bits'
_I='read-only'
_H='disable'
_G='enable'
_F='not-accessible'
_E='ZTE-AN-EVNET-MIB'
_D='read-write'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnEventMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,190))
if mibBuilder.loadTexts:zxAnEventMib.setRevisions(('2010-01-20 12:00',))
class ResourceId(TextualConvention,ObjectIdentifier):status=_A
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnEventSysObjects_ObjectIdentity=ObjectIdentity
zxAnEventSysObjects=_ZxAnEventSysObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,1))
class _ZxAnEventCurrentEventId_Type(Integer32):defaultValue=0
_ZxAnEventCurrentEventId_Type.__name__=_B
_ZxAnEventCurrentEventId_Object=MibScalar
zxAnEventCurrentEventId=_ZxAnEventCurrentEventId_Object((1,3,6,1,4,1,3902,1015,190,1,1),_ZxAnEventCurrentEventId_Type())
zxAnEventCurrentEventId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventCurrentEventId.setStatus(_A)
_ZxAnEventNmsHelloTrapMgmt_ObjectIdentity=ObjectIdentity
zxAnEventNmsHelloTrapMgmt=_ZxAnEventNmsHelloTrapMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,1,2))
class _ZxAnEventNmsHelloTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventNmsHelloTrapEnable_Type.__name__=_B
_ZxAnEventNmsHelloTrapEnable_Object=MibScalar
zxAnEventNmsHelloTrapEnable=_ZxAnEventNmsHelloTrapEnable_Object((1,3,6,1,4,1,3902,1015,190,1,2,1),_ZxAnEventNmsHelloTrapEnable_Type())
zxAnEventNmsHelloTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventNmsHelloTrapEnable.setStatus(_A)
class _ZxAnEventNmsHelloTrapInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_ZxAnEventNmsHelloTrapInterval_Type.__name__=_B
_ZxAnEventNmsHelloTrapInterval_Object=MibScalar
zxAnEventNmsHelloTrapInterval=_ZxAnEventNmsHelloTrapInterval_Object((1,3,6,1,4,1,3902,1015,190,1,2,2),_ZxAnEventNmsHelloTrapInterval_Type())
zxAnEventNmsHelloTrapInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventNmsHelloTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnEventNmsHelloTrapInterval.setUnits('second')
class _ZxAnEventCapabilities_Type(Bits):namedValues=NamedValues(*(('snmpOperType',0),('reserved',1),('receiverPort',2),('securityLevel',3)))
_ZxAnEventCapabilities_Type.__name__=_J
_ZxAnEventCapabilities_Object=MibScalar
zxAnEventCapabilities=_ZxAnEventCapabilities_Object((1,3,6,1,4,1,3902,1015,190,1,3),_ZxAnEventCapabilities_Type())
zxAnEventCapabilities.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEventCapabilities.setStatus(_A)
class _ZxAnEventSendingLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_ZxAnEventSendingLimit_Type.__name__=_B
_ZxAnEventSendingLimit_Object=MibScalar
zxAnEventSendingLimit=_ZxAnEventSendingLimit_Object((1,3,6,1,4,1,3902,1015,190,1,4),_ZxAnEventSendingLimit_Type())
zxAnEventSendingLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventSendingLimit.setStatus(_A)
class _ZxAnEventMaskEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventMaskEnable_Type.__name__=_B
_ZxAnEventMaskEnable_Object=MibScalar
zxAnEventMaskEnable=_ZxAnEventMaskEnable_Object((1,3,6,1,4,1,3902,1015,190,1,5),_ZxAnEventMaskEnable_Type())
zxAnEventMaskEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventMaskEnable.setStatus(_A)
_ZxAnEventConfirmObjects_ObjectIdentity=ObjectIdentity
zxAnEventConfirmObjects=_ZxAnEventConfirmObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,2))
_ZxAnEventConfirmEventId_Type=Integer32
_ZxAnEventConfirmEventId_Object=MibScalar
zxAnEventConfirmEventId=_ZxAnEventConfirmEventId_Object((1,3,6,1,4,1,3902,1015,190,2,1),_ZxAnEventConfirmEventId_Type())
zxAnEventConfirmEventId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventConfirmEventId.setStatus(_A)
_ZxAnEventConfirmClearedEventId_Type=Integer32
_ZxAnEventConfirmClearedEventId_Object=MibScalar
zxAnEventConfirmClearedEventId=_ZxAnEventConfirmClearedEventId_Object((1,3,6,1,4,1,3902,1015,190,2,2),_ZxAnEventConfirmClearedEventId_Type())
zxAnEventConfirmClearedEventId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventConfirmClearedEventId.setStatus(_A)
class _ZxAnEventConfirmTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,1800))
_ZxAnEventConfirmTimeout_Type.__name__=_B
_ZxAnEventConfirmTimeout_Object=MibScalar
zxAnEventConfirmTimeout=_ZxAnEventConfirmTimeout_Object((1,3,6,1,4,1,3902,1015,190,2,3),_ZxAnEventConfirmTimeout_Type())
zxAnEventConfirmTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventConfirmTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnEventConfirmTimeout.setUnits(_L)
class _ZxAnEventResendingTimes_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_ZxAnEventResendingTimes_Type.__name__=_B
_ZxAnEventResendingTimes_Object=MibScalar
zxAnEventResendingTimes=_ZxAnEventResendingTimes_Object((1,3,6,1,4,1,3902,1015,190,2,4),_ZxAnEventResendingTimes_Type())
zxAnEventResendingTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventResendingTimes.setStatus(_A)
_ZxAnEventSynchObjects_ObjectIdentity=ObjectIdentity
zxAnEventSynchObjects=_ZxAnEventSynchObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,3))
_ZxAnEventSyncUnconfirmedEvents_Type=Integer32
_ZxAnEventSyncUnconfirmedEvents_Object=MibScalar
zxAnEventSyncUnconfirmedEvents=_ZxAnEventSyncUnconfirmedEvents_Object((1,3,6,1,4,1,3902,1015,190,3,1),_ZxAnEventSyncUnconfirmedEvents_Type())
zxAnEventSyncUnconfirmedEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventSyncUnconfirmedEvents.setStatus(_A)
_ZxAnEventSyncSpecificEvents_Type=ObjectIdentifier
_ZxAnEventSyncSpecificEvents_Object=MibScalar
zxAnEventSyncSpecificEvents=_ZxAnEventSyncSpecificEvents_Object((1,3,6,1,4,1,3902,1015,190,3,2),_ZxAnEventSyncSpecificEvents_Type())
zxAnEventSyncSpecificEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventSyncSpecificEvents.setStatus(_A)
_ZxAnEventSyncNextEventIdList_Type=ObjectIdentifier
_ZxAnEventSyncNextEventIdList_Object=MibScalar
zxAnEventSyncNextEventIdList=_ZxAnEventSyncNextEventIdList_Object((1,3,6,1,4,1,3902,1015,190,3,3),_ZxAnEventSyncNextEventIdList_Type())
zxAnEventSyncNextEventIdList.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEventSyncNextEventIdList.setStatus(_A)
_ZxAnEventSyncStartEventId_Type=Integer32
_ZxAnEventSyncStartEventId_Object=MibScalar
zxAnEventSyncStartEventId=_ZxAnEventSyncStartEventId_Object((1,3,6,1,4,1,3902,1015,190,3,4),_ZxAnEventSyncStartEventId_Type())
zxAnEventSyncStartEventId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventSyncStartEventId.setStatus(_A)
_ZxAnEventConfObjects_ObjectIdentity=ObjectIdentity
zxAnEventConfObjects=_ZxAnEventConfObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,4))
_ZxAnEventConfTable_Object=MibTable
zxAnEventConfTable=_ZxAnEventConfTable_Object((1,3,6,1,4,1,3902,1015,190,4,1))
if mibBuilder.loadTexts:zxAnEventConfTable.setStatus(_A)
_ZxAnEventConfEntry_Object=MibTableRow
zxAnEventConfEntry=_ZxAnEventConfEntry_Object((1,3,6,1,4,1,3902,1015,190,4,1,1))
zxAnEventConfEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:zxAnEventConfEntry.setStatus(_A)
_ZxAnEventConfTrapOid_Type=ObjectIdentifier
_ZxAnEventConfTrapOid_Object=MibTableColumn
zxAnEventConfTrapOid=_ZxAnEventConfTrapOid_Object((1,3,6,1,4,1,3902,1015,190,4,1,1,1),_ZxAnEventConfTrapOid_Type())
zxAnEventConfTrapOid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventConfTrapOid.setStatus(_A)
class _ZxAnEventName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnEventName_Type.__name__=_K
_ZxAnEventName_Object=MibTableColumn
zxAnEventName=_ZxAnEventName_Object((1,3,6,1,4,1,3902,1015,190,4,1,1,2),_ZxAnEventName_Type())
zxAnEventName.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEventName.setStatus(_A)
class _ZxAnEventConfSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_S,0),(_M,1),(_N,2),(_O,3),(_P,4)))
_ZxAnEventConfSeverityLevel_Type.__name__=_B
_ZxAnEventConfSeverityLevel_Object=MibTableColumn
zxAnEventConfSeverityLevel=_ZxAnEventConfSeverityLevel_Object((1,3,6,1,4,1,3902,1015,190,4,1,1,3),_ZxAnEventConfSeverityLevel_Type())
zxAnEventConfSeverityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventConfSeverityLevel.setStatus(_A)
_ZxAnEventDeleteEventId_Type=Integer32
_ZxAnEventDeleteEventId_Object=MibScalar
zxAnEventDeleteEventId=_ZxAnEventDeleteEventId_Object((1,3,6,1,4,1,3902,1015,190,4,2),_ZxAnEventDeleteEventId_Type())
zxAnEventDeleteEventId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventDeleteEventId.setStatus(_A)
_ZxAnEventCtrlProfileTable_Object=MibTable
zxAnEventCtrlProfileTable=_ZxAnEventCtrlProfileTable_Object((1,3,6,1,4,1,3902,1015,190,4,3))
if mibBuilder.loadTexts:zxAnEventCtrlProfileTable.setStatus(_A)
_ZxAnEventCtrlProfileEntry_Object=MibTableRow
zxAnEventCtrlProfileEntry=_ZxAnEventCtrlProfileEntry_Object((1,3,6,1,4,1,3902,1015,190,4,3,1))
zxAnEventCtrlProfileEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:zxAnEventCtrlProfileEntry.setStatus(_A)
_ZxAnEventCtrlProfileName_Type=DisplayString
_ZxAnEventCtrlProfileName_Object=MibTableColumn
zxAnEventCtrlProfileName=_ZxAnEventCtrlProfileName_Object((1,3,6,1,4,1,3902,1015,190,4,3,1,1),_ZxAnEventCtrlProfileName_Type())
zxAnEventCtrlProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventCtrlProfileName.setStatus(_A)
_ZxAnEventCode_Type=Integer32
_ZxAnEventCode_Object=MibTableColumn
zxAnEventCode=_ZxAnEventCode_Object((1,3,6,1,4,1,3902,1015,190,4,3,1,2),_ZxAnEventCode_Type())
zxAnEventCode.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventCode.setStatus(_A)
class _ZxAnEventReportChannelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmp',1),('extendedOam',2),('omci',3)))
_ZxAnEventReportChannelType_Type.__name__=_B
_ZxAnEventReportChannelType_Object=MibTableColumn
zxAnEventReportChannelType=_ZxAnEventReportChannelType_Object((1,3,6,1,4,1,3902,1015,190,4,3,1,3),_ZxAnEventReportChannelType_Type())
zxAnEventReportChannelType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventReportChannelType.setStatus(_A)
_ZxAnEventCtrlProfileRowStatus_Type=RowStatus
_ZxAnEventCtrlProfileRowStatus_Object=MibTableColumn
zxAnEventCtrlProfileRowStatus=_ZxAnEventCtrlProfileRowStatus_Object((1,3,6,1,4,1,3902,1015,190,4,3,1,50),_ZxAnEventCtrlProfileRowStatus_Type())
zxAnEventCtrlProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventCtrlProfileRowStatus.setStatus(_A)
_ZxAnEventIfCfgTable_Object=MibTable
zxAnEventIfCfgTable=_ZxAnEventIfCfgTable_Object((1,3,6,1,4,1,3902,1015,190,4,4))
if mibBuilder.loadTexts:zxAnEventIfCfgTable.setStatus(_A)
_ZxAnEventIfCfgEntry_Object=MibTableRow
zxAnEventIfCfgEntry=_ZxAnEventIfCfgEntry_Object((1,3,6,1,4,1,3902,1015,190,4,4,1))
zxAnEventIfCfgEntry.setIndexNames((0,_E,_W),(0,_E,_X),(0,_E,_Y),(0,_E,_Z),(0,_E,_a),(0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:zxAnEventIfCfgEntry.setStatus(_A)
_ZxAnEventIfCfgRack_Type=Integer32
_ZxAnEventIfCfgRack_Object=MibTableColumn
zxAnEventIfCfgRack=_ZxAnEventIfCfgRack_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,1),_ZxAnEventIfCfgRack_Type())
zxAnEventIfCfgRack.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventIfCfgRack.setStatus(_A)
_ZxAnEventIfCfgShelf_Type=Integer32
_ZxAnEventIfCfgShelf_Object=MibTableColumn
zxAnEventIfCfgShelf=_ZxAnEventIfCfgShelf_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,2),_ZxAnEventIfCfgShelf_Type())
zxAnEventIfCfgShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventIfCfgShelf.setStatus(_A)
_ZxAnEventIfCfgSlot_Type=Integer32
_ZxAnEventIfCfgSlot_Object=MibTableColumn
zxAnEventIfCfgSlot=_ZxAnEventIfCfgSlot_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,3),_ZxAnEventIfCfgSlot_Type())
zxAnEventIfCfgSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventIfCfgSlot.setStatus(_A)
_ZxAnEventIfCfgPort_Type=Integer32
_ZxAnEventIfCfgPort_Object=MibTableColumn
zxAnEventIfCfgPort=_ZxAnEventIfCfgPort_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,4),_ZxAnEventIfCfgPort_Type())
zxAnEventIfCfgPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventIfCfgPort.setStatus(_A)
_ZxAnEventIfCfgOnu_Type=Integer32
_ZxAnEventIfCfgOnu_Object=MibTableColumn
zxAnEventIfCfgOnu=_ZxAnEventIfCfgOnu_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,5),_ZxAnEventIfCfgOnu_Type())
zxAnEventIfCfgOnu.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventIfCfgOnu.setStatus(_A)
class _ZxAnEventIfCfgIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,11,12,255)));namedValues=NamedValues(*(('physicalPort',1),('bridgePort',2),('ponOnu',3),('ponVPort',4),('onuUni',5),('servicePort',11),('vlan',12),('card',255)))
_ZxAnEventIfCfgIfType_Type.__name__=_B
_ZxAnEventIfCfgIfType_Object=MibTableColumn
zxAnEventIfCfgIfType=_ZxAnEventIfCfgIfType_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,6),_ZxAnEventIfCfgIfType_Type())
zxAnEventIfCfgIfType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventIfCfgIfType.setStatus(_A)
_ZxAnEventIfCfgLogicalId_Type=ObjectIdentifier
_ZxAnEventIfCfgLogicalId_Object=MibTableColumn
zxAnEventIfCfgLogicalId=_ZxAnEventIfCfgLogicalId_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,7),_ZxAnEventIfCfgLogicalId_Type())
zxAnEventIfCfgLogicalId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventIfCfgLogicalId.setStatus(_A)
class _ZxAnEventIfCfgMaskEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventIfCfgMaskEnable_Type.__name__=_B
_ZxAnEventIfCfgMaskEnable_Object=MibTableColumn
zxAnEventIfCfgMaskEnable=_ZxAnEventIfCfgMaskEnable_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,8),_ZxAnEventIfCfgMaskEnable_Type())
zxAnEventIfCfgMaskEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventIfCfgMaskEnable.setStatus(_A)
_ZxAnEventIfCfgProfileName_Type=DisplayString
_ZxAnEventIfCfgProfileName_Object=MibTableColumn
zxAnEventIfCfgProfileName=_ZxAnEventIfCfgProfileName_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,9),_ZxAnEventIfCfgProfileName_Type())
zxAnEventIfCfgProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventIfCfgProfileName.setStatus(_A)
_ZxAnEventIfCfgRowStatus_Type=RowStatus
_ZxAnEventIfCfgRowStatus_Object=MibTableColumn
zxAnEventIfCfgRowStatus=_ZxAnEventIfCfgRowStatus_Object((1,3,6,1,4,1,3902,1015,190,4,4,1,50),_ZxAnEventIfCfgRowStatus_Type())
zxAnEventIfCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventIfCfgRowStatus.setStatus(_A)
_ZxAnEventVlanCfgTable_Object=MibTable
zxAnEventVlanCfgTable=_ZxAnEventVlanCfgTable_Object((1,3,6,1,4,1,3902,1015,190,4,5))
if mibBuilder.loadTexts:zxAnEventVlanCfgTable.setStatus(_A)
_ZxAnEventVlanCfgEntry_Object=MibTableRow
zxAnEventVlanCfgEntry=_ZxAnEventVlanCfgEntry_Object((1,3,6,1,4,1,3902,1015,190,4,5,1))
zxAnEventVlanCfgEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:zxAnEventVlanCfgEntry.setStatus(_A)
class _ZxAnEventVlanCfgVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnEventVlanCfgVlanId_Type.__name__=_B
_ZxAnEventVlanCfgVlanId_Object=MibTableColumn
zxAnEventVlanCfgVlanId=_ZxAnEventVlanCfgVlanId_Object((1,3,6,1,4,1,3902,1015,190,4,5,1,1),_ZxAnEventVlanCfgVlanId_Type())
zxAnEventVlanCfgVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventVlanCfgVlanId.setStatus(_A)
class _ZxAnEventVlanCfgMaskEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventVlanCfgMaskEnable_Type.__name__=_B
_ZxAnEventVlanCfgMaskEnable_Object=MibTableColumn
zxAnEventVlanCfgMaskEnable=_ZxAnEventVlanCfgMaskEnable_Object((1,3,6,1,4,1,3902,1015,190,4,5,1,2),_ZxAnEventVlanCfgMaskEnable_Type())
zxAnEventVlanCfgMaskEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventVlanCfgMaskEnable.setStatus(_A)
_ZxAnEventVlanCfgProfileName_Type=DisplayString
_ZxAnEventVlanCfgProfileName_Object=MibTableColumn
zxAnEventVlanCfgProfileName=_ZxAnEventVlanCfgProfileName_Object((1,3,6,1,4,1,3902,1015,190,4,5,1,3),_ZxAnEventVlanCfgProfileName_Type())
zxAnEventVlanCfgProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventVlanCfgProfileName.setStatus(_A)
_ZxAnEventVlanCfgRowStatus_Type=RowStatus
_ZxAnEventVlanCfgRowStatus_Object=MibTableColumn
zxAnEventVlanCfgRowStatus=_ZxAnEventVlanCfgRowStatus_Object((1,3,6,1,4,1,3902,1015,190,4,5,1,50),_ZxAnEventVlanCfgRowStatus_Type())
zxAnEventVlanCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventVlanCfgRowStatus.setStatus(_A)
_ZxAnEventRecieverObjects_ObjectIdentity=ObjectIdentity
zxAnEventRecieverObjects=_ZxAnEventRecieverObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,5))
_ZxAnEventRecieverTable_Object=MibTable
zxAnEventRecieverTable=_ZxAnEventRecieverTable_Object((1,3,6,1,4,1,3902,1015,190,5,1))
if mibBuilder.loadTexts:zxAnEventRecieverTable.setStatus(_A)
_ZxAnEventRecieverEntry_Object=MibTableRow
zxAnEventRecieverEntry=_ZxAnEventRecieverEntry_Object((1,3,6,1,4,1,3902,1015,190,5,1,1))
zxAnEventRecieverEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:zxAnEventRecieverEntry.setStatus(_A)
class _ZxAnEventReceiverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnEventReceiverIndex_Type.__name__=_B
_ZxAnEventReceiverIndex_Object=MibTableColumn
zxAnEventReceiverIndex=_ZxAnEventReceiverIndex_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,1),_ZxAnEventReceiverIndex_Type())
zxAnEventReceiverIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventReceiverIndex.setStatus(_A)
_ZxAnEventReceiverIpAddr_Type=IpAddress
_ZxAnEventReceiverIpAddr_Object=MibTableColumn
zxAnEventReceiverIpAddr=_ZxAnEventReceiverIpAddr_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,2),_ZxAnEventReceiverIpAddr_Type())
zxAnEventReceiverIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverIpAddr.setStatus(_A)
class _ZxAnEventReceiverSnmpVer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmpV1',1),('snmpV2c',2),('snmpV3',3)))
_ZxAnEventReceiverSnmpVer_Type.__name__=_B
_ZxAnEventReceiverSnmpVer_Object=MibTableColumn
zxAnEventReceiverSnmpVer=_ZxAnEventReceiverSnmpVer_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,3),_ZxAnEventReceiverSnmpVer_Type())
zxAnEventReceiverSnmpVer.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverSnmpVer.setStatus(_A)
class _ZxAnEventReceiverCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_ZxAnEventReceiverCommunity_Type.__name__=_K
_ZxAnEventReceiverCommunity_Object=MibTableColumn
zxAnEventReceiverCommunity=_ZxAnEventReceiverCommunity_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,4),_ZxAnEventReceiverCommunity_Type())
zxAnEventReceiverCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverCommunity.setStatus(_A)
class _ZxAnEventReceiverEventFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmpTrap',1),('snmpInform',2),('snmpTrapForPccw',3)))
_ZxAnEventReceiverEventFormat_Type.__name__=_B
_ZxAnEventReceiverEventFormat_Object=MibTableColumn
zxAnEventReceiverEventFormat=_ZxAnEventReceiverEventFormat_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,5),_ZxAnEventReceiverEventFormat_Type())
zxAnEventReceiverEventFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverEventFormat.setStatus(_A)
class _ZxAnEventReceiverEventType_Type(Bits):defaultBinValue='11111';namedValues=NamedValues(*((_f,0),(_g,1),(_h,2),(_i,3),(_j,4)))
_ZxAnEventReceiverEventType_Type.__name__=_J
_ZxAnEventReceiverEventType_Object=MibTableColumn
zxAnEventReceiverEventType=_ZxAnEventReceiverEventType_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,6),_ZxAnEventReceiverEventType_Type())
zxAnEventReceiverEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverEventType.setStatus(_A)
class _ZxAnEventReceiverMinEventLevel_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,0),(_M,1),(_N,2),(_O,3),(_P,4),(_k,5),(_l,6)))
_ZxAnEventReceiverMinEventLevel_Type.__name__=_B
_ZxAnEventReceiverMinEventLevel_Object=MibTableColumn
zxAnEventReceiverMinEventLevel=_ZxAnEventReceiverMinEventLevel_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,7),_ZxAnEventReceiverMinEventLevel_Type())
zxAnEventReceiverMinEventLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverMinEventLevel.setStatus(_A)
class _ZxAnEventReceiverEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventReceiverEnable_Type.__name__=_B
_ZxAnEventReceiverEnable_Object=MibTableColumn
zxAnEventReceiverEnable=_ZxAnEventReceiverEnable_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,8),_ZxAnEventReceiverEnable_Type())
zxAnEventReceiverEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverEnable.setStatus(_A)
_ZxAnEventReceiverIsZteNmsSever_Type=TruthValue
_ZxAnEventReceiverIsZteNmsSever_Object=MibTableColumn
zxAnEventReceiverIsZteNmsSever=_ZxAnEventReceiverIsZteNmsSever_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,9),_ZxAnEventReceiverIsZteNmsSever_Type())
zxAnEventReceiverIsZteNmsSever.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverIsZteNmsSever.setStatus(_A)
class _ZxAnEventReceiverSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthNoPriv',1),('authNoPriv',2),('authPriv',3)))
_ZxAnEventReceiverSecurityLevel_Type.__name__=_B
_ZxAnEventReceiverSecurityLevel_Object=MibTableColumn
zxAnEventReceiverSecurityLevel=_ZxAnEventReceiverSecurityLevel_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,10),_ZxAnEventReceiverSecurityLevel_Type())
zxAnEventReceiverSecurityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverSecurityLevel.setStatus(_A)
class _ZxAnEventReceiverPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnEventReceiverPort_Type.__name__=_B
_ZxAnEventReceiverPort_Object=MibTableColumn
zxAnEventReceiverPort=_ZxAnEventReceiverPort_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,11),_ZxAnEventReceiverPort_Type())
zxAnEventReceiverPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverPort.setStatus(_A)
_ZxAnEventReceiverRowStatus_Type=RowStatus
_ZxAnEventReceiverRowStatus_Object=MibTableColumn
zxAnEventReceiverRowStatus=_ZxAnEventReceiverRowStatus_Object((1,3,6,1,4,1,3902,1015,190,5,1,1,15),_ZxAnEventReceiverRowStatus_Type())
zxAnEventReceiverRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventReceiverRowStatus.setStatus(_A)
_ZxAnEventTrapObjects_ObjectIdentity=ObjectIdentity
zxAnEventTrapObjects=_ZxAnEventTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,6))
_ZxAnEventSyslogObjects_ObjectIdentity=ObjectIdentity
zxAnEventSyslogObjects=_ZxAnEventSyslogObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,7))
_ZxAnEventSyslogTable_Object=MibTable
zxAnEventSyslogTable=_ZxAnEventSyslogTable_Object((1,3,6,1,4,1,3902,1015,190,7,1))
if mibBuilder.loadTexts:zxAnEventSyslogTable.setStatus(_A)
_ZxAnEventSyslogEntry_Object=MibTableRow
zxAnEventSyslogEntry=_ZxAnEventSyslogEntry_Object((1,3,6,1,4,1,3902,1015,190,7,1,1))
zxAnEventSyslogEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:zxAnEventSyslogEntry.setStatus(_A)
_ZxAnEventSyslogSvrIpAddr_Type=IpAddress
_ZxAnEventSyslogSvrIpAddr_Object=MibTableColumn
zxAnEventSyslogSvrIpAddr=_ZxAnEventSyslogSvrIpAddr_Object((1,3,6,1,4,1,3902,1015,190,7,1,1,1),_ZxAnEventSyslogSvrIpAddr_Type())
zxAnEventSyslogSvrIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventSyslogSvrIpAddr.setStatus(_A)
class _ZxAnEventSyslogSvrPort_Type(Integer32):defaultValue=514
_ZxAnEventSyslogSvrPort_Type.__name__=_B
_ZxAnEventSyslogSvrPort_Object=MibTableColumn
zxAnEventSyslogSvrPort=_ZxAnEventSyslogSvrPort_Object((1,3,6,1,4,1,3902,1015,190,7,1,1,2),_ZxAnEventSyslogSvrPort_Type())
zxAnEventSyslogSvrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventSyslogSvrPort.setStatus(_A)
class _ZxAnEventSyslogType_Type(Bits):defaultBinValue='1111';namedValues=NamedValues(*(('cmdlog',0),('snmplog',1),('debugmsg',2),('alarmlog',3)))
_ZxAnEventSyslogType_Type.__name__=_J
_ZxAnEventSyslogType_Object=MibTableColumn
zxAnEventSyslogType=_ZxAnEventSyslogType_Object((1,3,6,1,4,1,3902,1015,190,7,1,1,3),_ZxAnEventSyslogType_Type())
zxAnEventSyslogType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventSyslogType.setStatus(_A)
class _ZxAnEventSyslogMinAlarmLevel_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_k,5),(_l,6)))
_ZxAnEventSyslogMinAlarmLevel_Type.__name__=_B
_ZxAnEventSyslogMinAlarmLevel_Object=MibTableColumn
zxAnEventSyslogMinAlarmLevel=_ZxAnEventSyslogMinAlarmLevel_Object((1,3,6,1,4,1,3902,1015,190,7,1,1,4),_ZxAnEventSyslogMinAlarmLevel_Type())
zxAnEventSyslogMinAlarmLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventSyslogMinAlarmLevel.setStatus(_A)
class _ZxAnEventSyslogEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventSyslogEnable_Type.__name__=_B
_ZxAnEventSyslogEnable_Object=MibTableColumn
zxAnEventSyslogEnable=_ZxAnEventSyslogEnable_Object((1,3,6,1,4,1,3902,1015,190,7,1,1,5),_ZxAnEventSyslogEnable_Type())
zxAnEventSyslogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventSyslogEnable.setStatus(_A)
class _ZxAnEventSyslogSnmpOperType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('get',2),('set',3)))
_ZxAnEventSyslogSnmpOperType_Type.__name__=_B
_ZxAnEventSyslogSnmpOperType_Object=MibTableColumn
zxAnEventSyslogSnmpOperType=_ZxAnEventSyslogSnmpOperType_Object((1,3,6,1,4,1,3902,1015,190,7,1,1,6),_ZxAnEventSyslogSnmpOperType_Type())
zxAnEventSyslogSnmpOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventSyslogSnmpOperType.setStatus(_A)
_ZxAnEventSyslogRowStatus_Type=RowStatus
_ZxAnEventSyslogRowStatus_Object=MibTableColumn
zxAnEventSyslogRowStatus=_ZxAnEventSyslogRowStatus_Object((1,3,6,1,4,1,3902,1015,190,7,1,1,30),_ZxAnEventSyslogRowStatus_Type())
zxAnEventSyslogRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventSyslogRowStatus.setStatus(_A)
_ZxAnEventSyslogGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnEventSyslogGlobalObjects=_ZxAnEventSyslogGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,7,2))
class _ZxAnEventSyslogFacility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_ZxAnEventSyslogFacility_Type.__name__=_B
_ZxAnEventSyslogFacility_Object=MibScalar
zxAnEventSyslogFacility=_ZxAnEventSyslogFacility_Object((1,3,6,1,4,1,3902,1015,190,7,2,1),_ZxAnEventSyslogFacility_Type())
zxAnEventSyslogFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventSyslogFacility.setStatus(_A)
class _ZxAnEventSyslogSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnEventSyslogSeverity_Type.__name__=_B
_ZxAnEventSyslogSeverity_Object=MibScalar
zxAnEventSyslogSeverity=_ZxAnEventSyslogSeverity_Object((1,3,6,1,4,1,3902,1015,190,7,2,2),_ZxAnEventSyslogSeverity_Type())
zxAnEventSyslogSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventSyslogSeverity.setStatus(_A)
class _ZxAnEventSyslogSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEventSyslogSourcePort_Type.__name__=_B
_ZxAnEventSyslogSourcePort_Object=MibScalar
zxAnEventSyslogSourcePort=_ZxAnEventSyslogSourcePort_Object((1,3,6,1,4,1,3902,1015,190,7,2,3),_ZxAnEventSyslogSourcePort_Type())
zxAnEventSyslogSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventSyslogSourcePort.setStatus(_A)
_ZxAnEventDefineObjects_ObjectIdentity=ObjectIdentity
zxAnEventDefineObjects=_ZxAnEventDefineObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,8))
_ZxAnEventDefineTable_Object=MibTable
zxAnEventDefineTable=_ZxAnEventDefineTable_Object((1,3,6,1,4,1,3902,1015,190,8,2))
if mibBuilder.loadTexts:zxAnEventDefineTable.setStatus(_A)
_ZxAnEventDefineEntry_Object=MibTableRow
zxAnEventDefineEntry=_ZxAnEventDefineEntry_Object((1,3,6,1,4,1,3902,1015,190,8,2,1))
zxAnEventDefineEntry.setIndexNames((0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:zxAnEventDefineEntry.setStatus(_A)
_ZxAnEventDefineCode_Type=Integer32
_ZxAnEventDefineCode_Object=MibTableColumn
zxAnEventDefineCode=_ZxAnEventDefineCode_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,1),_ZxAnEventDefineCode_Type())
zxAnEventDefineCode.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventDefineCode.setStatus(_A)
class _ZxAnEventDefineReportChannelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmp',1),('ponExtendedOam',2),('ponOmci',3)))
_ZxAnEventDefineReportChannelType_Type.__name__=_B
_ZxAnEventDefineReportChannelType_Object=MibTableColumn
zxAnEventDefineReportChannelType=_ZxAnEventDefineReportChannelType_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,2),_ZxAnEventDefineReportChannelType_Type())
zxAnEventDefineReportChannelType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventDefineReportChannelType.setStatus(_A)
_ZxAnEventDefineName_Type=DisplayString
_ZxAnEventDefineName_Object=MibTableColumn
zxAnEventDefineName=_ZxAnEventDefineName_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,3),_ZxAnEventDefineName_Type())
zxAnEventDefineName.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEventDefineName.setStatus(_A)
_ZxAnEventDefineStandardAlarmCode_Type=Integer32
_ZxAnEventDefineStandardAlarmCode_Object=MibTableColumn
zxAnEventDefineStandardAlarmCode=_ZxAnEventDefineStandardAlarmCode_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,4),_ZxAnEventDefineStandardAlarmCode_Type())
zxAnEventDefineStandardAlarmCode.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEventDefineStandardAlarmCode.setStatus(_A)
class _ZxAnEventDefineEventType_Type(Bits):namedValues=NamedValues(*((_f,0),(_g,1),(_h,2),(_i,3),(_j,4)))
_ZxAnEventDefineEventType_Type.__name__=_J
_ZxAnEventDefineEventType_Object=MibTableColumn
zxAnEventDefineEventType=_ZxAnEventDefineEventType_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,5),_ZxAnEventDefineEventType_Type())
zxAnEventDefineEventType.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnEventDefineEventType.setStatus(_A)
class _ZxAnEventDefineAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventDefineAdminStatus_Type.__name__=_B
_ZxAnEventDefineAdminStatus_Object=MibTableColumn
zxAnEventDefineAdminStatus=_ZxAnEventDefineAdminStatus_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,6),_ZxAnEventDefineAdminStatus_Type())
zxAnEventDefineAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventDefineAdminStatus.setStatus(_A)
class _ZxAnEventDefineMaskEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventDefineMaskEnable_Type.__name__=_B
_ZxAnEventDefineMaskEnable_Object=MibTableColumn
zxAnEventDefineMaskEnable=_ZxAnEventDefineMaskEnable_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,7),_ZxAnEventDefineMaskEnable_Type())
zxAnEventDefineMaskEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventDefineMaskEnable.setStatus(_A)
class _ZxAnEventDefineSendingDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_ZxAnEventDefineSendingDelay_Type.__name__=_B
_ZxAnEventDefineSendingDelay_Object=MibTableColumn
zxAnEventDefineSendingDelay=_ZxAnEventDefineSendingDelay_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,8),_ZxAnEventDefineSendingDelay_Type())
zxAnEventDefineSendingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventDefineSendingDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnEventDefineSendingDelay.setUnits(_L)
class _ZxAnEventDefineSendingLimit_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_ZxAnEventDefineSendingLimit_Type.__name__=_B
_ZxAnEventDefineSendingLimit_Object=MibTableColumn
zxAnEventDefineSendingLimit=_ZxAnEventDefineSendingLimit_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,9),_ZxAnEventDefineSendingLimit_Type())
zxAnEventDefineSendingLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventDefineSendingLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnEventDefineSendingLimit.setUnits(_L)
class _ZxAnEventDefineReversalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnEventDefineReversalEnable_Type.__name__=_B
_ZxAnEventDefineReversalEnable_Object=MibTableColumn
zxAnEventDefineReversalEnable=_ZxAnEventDefineReversalEnable_Object((1,3,6,1,4,1,3902,1015,190,8,2,1,10),_ZxAnEventDefineReversalEnable_Type())
zxAnEventDefineReversalEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEventDefineReversalEnable.setStatus(_A)
_ZxAnEventReportingObjects_ObjectIdentity=ObjectIdentity
zxAnEventReportingObjects=_ZxAnEventReportingObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,9))
_ZxAnEventReportCtrlObjects_ObjectIdentity=ObjectIdentity
zxAnEventReportCtrlObjects=_ZxAnEventReportCtrlObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,190,9,2))
_ZxAnEventRptCtrlProfileTable_Object=MibTable
zxAnEventRptCtrlProfileTable=_ZxAnEventRptCtrlProfileTable_Object((1,3,6,1,4,1,3902,1015,190,9,2,1))
if mibBuilder.loadTexts:zxAnEventRptCtrlProfileTable.setStatus(_A)
_ZxAnEventRptCtrlProfileEntry_Object=MibTableRow
zxAnEventRptCtrlProfileEntry=_ZxAnEventRptCtrlProfileEntry_Object((1,3,6,1,4,1,3902,1015,190,9,2,1,1))
zxAnEventRptCtrlProfileEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:zxAnEventRptCtrlProfileEntry.setStatus(_A)
class _ZxAnEventRptCtrlPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEventRptCtrlPrfName_Type.__name__=_K
_ZxAnEventRptCtrlPrfName_Object=MibTableColumn
zxAnEventRptCtrlPrfName=_ZxAnEventRptCtrlPrfName_Object((1,3,6,1,4,1,3902,1015,190,9,2,1,1,1),_ZxAnEventRptCtrlPrfName_Type())
zxAnEventRptCtrlPrfName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventRptCtrlPrfName.setStatus(_A)
_ZxAnEventRptCtrlPrfRowStatus_Type=RowStatus
_ZxAnEventRptCtrlPrfRowStatus_Object=MibTableColumn
zxAnEventRptCtrlPrfRowStatus=_ZxAnEventRptCtrlPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,190,9,2,1,1,50),_ZxAnEventRptCtrlPrfRowStatus_Type())
zxAnEventRptCtrlPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventRptCtrlPrfRowStatus.setStatus(_A)
_ZxAnEventRptCtrlProfileRuleTable_Object=MibTable
zxAnEventRptCtrlProfileRuleTable=_ZxAnEventRptCtrlProfileRuleTable_Object((1,3,6,1,4,1,3902,1015,190,9,2,2))
if mibBuilder.loadTexts:zxAnEventRptCtrlProfileRuleTable.setStatus(_A)
_ZxAnEventRptCtrlProfileRuleEntry_Object=MibTableRow
zxAnEventRptCtrlProfileRuleEntry=_ZxAnEventRptCtrlProfileRuleEntry_Object((1,3,6,1,4,1,3902,1015,190,9,2,2,1))
zxAnEventRptCtrlProfileRuleEntry.setIndexNames((0,_E,_Q),(0,_E,_p))
if mibBuilder.loadTexts:zxAnEventRptCtrlProfileRuleEntry.setStatus(_A)
class _ZxAnEventRptCtrlPrfRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ZxAnEventRptCtrlPrfRuleIndex_Type.__name__=_B
_ZxAnEventRptCtrlPrfRuleIndex_Object=MibTableColumn
zxAnEventRptCtrlPrfRuleIndex=_ZxAnEventRptCtrlPrfRuleIndex_Object((1,3,6,1,4,1,3902,1015,190,9,2,2,1,1),_ZxAnEventRptCtrlPrfRuleIndex_Type())
zxAnEventRptCtrlPrfRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventRptCtrlPrfRuleIndex.setStatus(_A)
_ZxAnEventRptCtrlEventCode_Type=Integer32
_ZxAnEventRptCtrlEventCode_Object=MibTableColumn
zxAnEventRptCtrlEventCode=_ZxAnEventRptCtrlEventCode_Object((1,3,6,1,4,1,3902,1015,190,9,2,2,1,2),_ZxAnEventRptCtrlEventCode_Type())
zxAnEventRptCtrlEventCode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventRptCtrlEventCode.setStatus(_A)
class _ZxAnEventRptCtrlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nalm',1),('nalmQI',2)))
_ZxAnEventRptCtrlAdminStatus_Type.__name__=_B
_ZxAnEventRptCtrlAdminStatus_Object=MibTableColumn
zxAnEventRptCtrlAdminStatus=_ZxAnEventRptCtrlAdminStatus_Object((1,3,6,1,4,1,3902,1015,190,9,2,2,1,21),_ZxAnEventRptCtrlAdminStatus_Type())
zxAnEventRptCtrlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventRptCtrlAdminStatus.setStatus(_A)
_ZxAnEventRptCtrlPrfRuleRowStatus_Type=RowStatus
_ZxAnEventRptCtrlPrfRuleRowStatus_Object=MibTableColumn
zxAnEventRptCtrlPrfRuleRowStatus=_ZxAnEventRptCtrlPrfRuleRowStatus_Object((1,3,6,1,4,1,3902,1015,190,9,2,2,1,50),_ZxAnEventRptCtrlPrfRuleRowStatus_Type())
zxAnEventRptCtrlPrfRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventRptCtrlPrfRuleRowStatus.setStatus(_A)
_ZxAnEventRptCtrlResourceTable_Object=MibTable
zxAnEventRptCtrlResourceTable=_ZxAnEventRptCtrlResourceTable_Object((1,3,6,1,4,1,3902,1015,190,9,2,3))
if mibBuilder.loadTexts:zxAnEventRptCtrlResourceTable.setStatus(_A)
_ZxAnEventRptCtrlResourceEntry_Object=MibTableRow
zxAnEventRptCtrlResourceEntry=_ZxAnEventRptCtrlResourceEntry_Object((1,3,6,1,4,1,3902,1015,190,9,2,3,1))
zxAnEventRptCtrlResourceEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:zxAnEventRptCtrlResourceEntry.setStatus(_A)
_ZxAnEventRptCtrlResId_Type=ResourceId
_ZxAnEventRptCtrlResId_Object=MibTableColumn
zxAnEventRptCtrlResId=_ZxAnEventRptCtrlResId_Object((1,3,6,1,4,1,3902,1015,190,9,2,3,1,1),_ZxAnEventRptCtrlResId_Type())
zxAnEventRptCtrlResId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnEventRptCtrlResId.setStatus(_A)
class _ZxAnEventRptCtrlResPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnEventRptCtrlResPrfName_Type.__name__=_K
_ZxAnEventRptCtrlResPrfName_Object=MibTableColumn
zxAnEventRptCtrlResPrfName=_ZxAnEventRptCtrlResPrfName_Object((1,3,6,1,4,1,3902,1015,190,9,2,3,1,2),_ZxAnEventRptCtrlResPrfName_Type())
zxAnEventRptCtrlResPrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventRptCtrlResPrfName.setStatus(_A)
_ZxAnEventRptCtrlResRowStatus_Type=RowStatus
_ZxAnEventRptCtrlResRowStatus_Object=MibTableColumn
zxAnEventRptCtrlResRowStatus=_ZxAnEventRptCtrlResRowStatus_Object((1,3,6,1,4,1,3902,1015,190,9,2,3,1,50),_ZxAnEventRptCtrlResRowStatus_Type())
zxAnEventRptCtrlResRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnEventRptCtrlResRowStatus.setStatus(_A)
zxAnEventRequestCurrentEventId=NotificationType((1,3,6,1,4,1,3902,1015,190,6,1))
if mibBuilder.loadTexts:zxAnEventRequestCurrentEventId.setStatus(_A)
zxAnEventNmsHelloTrap=NotificationType((1,3,6,1,4,1,3902,1015,190,6,2))
if mibBuilder.loadTexts:zxAnEventNmsHelloTrap.setStatus(_A)
zxAnEventReceiverDeleteNotify=NotificationType((1,3,6,1,4,1,3902,1015,190,6,3))
zxAnEventReceiverDeleteNotify.setObjects((_E,_r))
if mibBuilder.loadTexts:zxAnEventReceiverDeleteNotify.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ResourceId':ResourceId,'zte':zte,'zxAn':zxAn,'zxAnEventMib':zxAnEventMib,'zxAnEventSysObjects':zxAnEventSysObjects,'zxAnEventCurrentEventId':zxAnEventCurrentEventId,'zxAnEventNmsHelloTrapMgmt':zxAnEventNmsHelloTrapMgmt,'zxAnEventNmsHelloTrapEnable':zxAnEventNmsHelloTrapEnable,'zxAnEventNmsHelloTrapInterval':zxAnEventNmsHelloTrapInterval,'zxAnEventCapabilities':zxAnEventCapabilities,'zxAnEventSendingLimit':zxAnEventSendingLimit,'zxAnEventMaskEnable':zxAnEventMaskEnable,'zxAnEventConfirmObjects':zxAnEventConfirmObjects,'zxAnEventConfirmEventId':zxAnEventConfirmEventId,'zxAnEventConfirmClearedEventId':zxAnEventConfirmClearedEventId,'zxAnEventConfirmTimeout':zxAnEventConfirmTimeout,'zxAnEventResendingTimes':zxAnEventResendingTimes,'zxAnEventSynchObjects':zxAnEventSynchObjects,'zxAnEventSyncUnconfirmedEvents':zxAnEventSyncUnconfirmedEvents,'zxAnEventSyncSpecificEvents':zxAnEventSyncSpecificEvents,'zxAnEventSyncNextEventIdList':zxAnEventSyncNextEventIdList,'zxAnEventSyncStartEventId':zxAnEventSyncStartEventId,'zxAnEventConfObjects':zxAnEventConfObjects,'zxAnEventConfTable':zxAnEventConfTable,'zxAnEventConfEntry':zxAnEventConfEntry,_R:zxAnEventConfTrapOid,'zxAnEventName':zxAnEventName,'zxAnEventConfSeverityLevel':zxAnEventConfSeverityLevel,'zxAnEventDeleteEventId':zxAnEventDeleteEventId,'zxAnEventCtrlProfileTable':zxAnEventCtrlProfileTable,'zxAnEventCtrlProfileEntry':zxAnEventCtrlProfileEntry,_T:zxAnEventCtrlProfileName,_U:zxAnEventCode,_V:zxAnEventReportChannelType,'zxAnEventCtrlProfileRowStatus':zxAnEventCtrlProfileRowStatus,'zxAnEventIfCfgTable':zxAnEventIfCfgTable,'zxAnEventIfCfgEntry':zxAnEventIfCfgEntry,_W:zxAnEventIfCfgRack,_X:zxAnEventIfCfgShelf,_Y:zxAnEventIfCfgSlot,_Z:zxAnEventIfCfgPort,_a:zxAnEventIfCfgOnu,_b:zxAnEventIfCfgIfType,_c:zxAnEventIfCfgLogicalId,'zxAnEventIfCfgMaskEnable':zxAnEventIfCfgMaskEnable,'zxAnEventIfCfgProfileName':zxAnEventIfCfgProfileName,'zxAnEventIfCfgRowStatus':zxAnEventIfCfgRowStatus,'zxAnEventVlanCfgTable':zxAnEventVlanCfgTable,'zxAnEventVlanCfgEntry':zxAnEventVlanCfgEntry,_d:zxAnEventVlanCfgVlanId,'zxAnEventVlanCfgMaskEnable':zxAnEventVlanCfgMaskEnable,'zxAnEventVlanCfgProfileName':zxAnEventVlanCfgProfileName,'zxAnEventVlanCfgRowStatus':zxAnEventVlanCfgRowStatus,'zxAnEventRecieverObjects':zxAnEventRecieverObjects,'zxAnEventRecieverTable':zxAnEventRecieverTable,'zxAnEventRecieverEntry':zxAnEventRecieverEntry,_e:zxAnEventReceiverIndex,_r:zxAnEventReceiverIpAddr,'zxAnEventReceiverSnmpVer':zxAnEventReceiverSnmpVer,'zxAnEventReceiverCommunity':zxAnEventReceiverCommunity,'zxAnEventReceiverEventFormat':zxAnEventReceiverEventFormat,'zxAnEventReceiverEventType':zxAnEventReceiverEventType,'zxAnEventReceiverMinEventLevel':zxAnEventReceiverMinEventLevel,'zxAnEventReceiverEnable':zxAnEventReceiverEnable,'zxAnEventReceiverIsZteNmsSever':zxAnEventReceiverIsZteNmsSever,'zxAnEventReceiverSecurityLevel':zxAnEventReceiverSecurityLevel,'zxAnEventReceiverPort':zxAnEventReceiverPort,'zxAnEventReceiverRowStatus':zxAnEventReceiverRowStatus,'zxAnEventTrapObjects':zxAnEventTrapObjects,'zxAnEventRequestCurrentEventId':zxAnEventRequestCurrentEventId,'zxAnEventNmsHelloTrap':zxAnEventNmsHelloTrap,'zxAnEventReceiverDeleteNotify':zxAnEventReceiverDeleteNotify,'zxAnEventSyslogObjects':zxAnEventSyslogObjects,'zxAnEventSyslogTable':zxAnEventSyslogTable,'zxAnEventSyslogEntry':zxAnEventSyslogEntry,_m:zxAnEventSyslogSvrIpAddr,'zxAnEventSyslogSvrPort':zxAnEventSyslogSvrPort,'zxAnEventSyslogType':zxAnEventSyslogType,'zxAnEventSyslogMinAlarmLevel':zxAnEventSyslogMinAlarmLevel,'zxAnEventSyslogEnable':zxAnEventSyslogEnable,'zxAnEventSyslogSnmpOperType':zxAnEventSyslogSnmpOperType,'zxAnEventSyslogRowStatus':zxAnEventSyslogRowStatus,'zxAnEventSyslogGlobalObjects':zxAnEventSyslogGlobalObjects,'zxAnEventSyslogFacility':zxAnEventSyslogFacility,'zxAnEventSyslogSeverity':zxAnEventSyslogSeverity,'zxAnEventSyslogSourcePort':zxAnEventSyslogSourcePort,'zxAnEventDefineObjects':zxAnEventDefineObjects,'zxAnEventDefineTable':zxAnEventDefineTable,'zxAnEventDefineEntry':zxAnEventDefineEntry,_n:zxAnEventDefineCode,_o:zxAnEventDefineReportChannelType,'zxAnEventDefineName':zxAnEventDefineName,'zxAnEventDefineStandardAlarmCode':zxAnEventDefineStandardAlarmCode,'zxAnEventDefineEventType':zxAnEventDefineEventType,'zxAnEventDefineAdminStatus':zxAnEventDefineAdminStatus,'zxAnEventDefineMaskEnable':zxAnEventDefineMaskEnable,'zxAnEventDefineSendingDelay':zxAnEventDefineSendingDelay,'zxAnEventDefineSendingLimit':zxAnEventDefineSendingLimit,'zxAnEventDefineReversalEnable':zxAnEventDefineReversalEnable,'zxAnEventReportingObjects':zxAnEventReportingObjects,'zxAnEventReportCtrlObjects':zxAnEventReportCtrlObjects,'zxAnEventRptCtrlProfileTable':zxAnEventRptCtrlProfileTable,'zxAnEventRptCtrlProfileEntry':zxAnEventRptCtrlProfileEntry,_Q:zxAnEventRptCtrlPrfName,'zxAnEventRptCtrlPrfRowStatus':zxAnEventRptCtrlPrfRowStatus,'zxAnEventRptCtrlProfileRuleTable':zxAnEventRptCtrlProfileRuleTable,'zxAnEventRptCtrlProfileRuleEntry':zxAnEventRptCtrlProfileRuleEntry,_p:zxAnEventRptCtrlPrfRuleIndex,'zxAnEventRptCtrlEventCode':zxAnEventRptCtrlEventCode,'zxAnEventRptCtrlAdminStatus':zxAnEventRptCtrlAdminStatus,'zxAnEventRptCtrlPrfRuleRowStatus':zxAnEventRptCtrlPrfRuleRowStatus,'zxAnEventRptCtrlResourceTable':zxAnEventRptCtrlResourceTable,'zxAnEventRptCtrlResourceEntry':zxAnEventRptCtrlResourceEntry,_q:zxAnEventRptCtrlResId,'zxAnEventRptCtrlResPrfName':zxAnEventRptCtrlResPrfName,'zxAnEventRptCtrlResRowStatus':zxAnEventRptCtrlResRowStatus})