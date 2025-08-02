_h='currentNotificationGroup'
_g='currentObjectGroup'
_f='eventType'
_e='hwIsmEventRowStatus'
_d='hwIsmEventParameter'
_c='hwIsmEventRecoveryTime'
_b='hwIsmEventTime'
_a='hwIsmEventLevel'
_Z='hwIsmEventID'
_Y='hwIsmEventType'
_X='hwIsmTrapEventRecoveryTimeStr'
_W='hwIsmTrapEventTimeStr'
_V='hwIsmTrapEventID32Bit'
_U='forwardAddrUSMUserName'
_T='forwardAddrTrapType'
_S='forwardAddrIPNew'
_R='forwardAddrRowStatus'
_Q='forwardAddrTrapVer'
_P='forwardAddrPort'
_O='forwardAddrIP'
_N='hwIsmTrapEventParameter'
_M='hwIsmTrapEventRecoveryTime'
_L='hwIsmTrapEventTime'
_K='hwIsmTrapEventSequence'
_J='hwIsmTrapEventLevel'
_I='hwIsmTrapEventID'
_H='hwIsmTrapEventType'
_G='hwIsmEventSequence'
_F='forwardAddrIndex'
_E='read-create'
_D='read-write'
_C='accessible-for-notify'
_B='current'
_A='ISM-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
huaweistorage=ModuleIdentity((1,3,6,1,4,1,34774))
if mibBuilder.loadTexts:huaweistorage.setRevisions(('2013-04-07 19:15',))
class NodeCodeString(TextualConvention,OctetString):status=_B;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,17))
_HwStorage_ObjectIdentity=ObjectIdentity
hwStorage=_HwStorage_ObjectIdentity((1,3,6,1,4,1,34774,4))
_HwISM_ObjectIdentity=ObjectIdentity
hwISM=_HwISM_ObjectIdentity((1,3,6,1,4,1,34774,4,1))
_TrapAddress_ObjectIdentity=ObjectIdentity
trapAddress=_TrapAddress_ObjectIdentity((1,3,6,1,4,1,34774,4,1,2))
_ForwardAddrTable_Object=MibTable
forwardAddrTable=_ForwardAddrTable_Object((1,3,6,1,4,1,34774,4,1,2,1))
if mibBuilder.loadTexts:forwardAddrTable.setStatus(_B)
_ForwardAddrEntry_Object=MibTableRow
forwardAddrEntry=_ForwardAddrEntry_Object((1,3,6,1,4,1,34774,4,1,2,1,1))
forwardAddrEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:forwardAddrEntry.setStatus(_B)
_ForwardAddrIndex_Type=OctetString
_ForwardAddrIndex_Object=MibTableColumn
forwardAddrIndex=_ForwardAddrIndex_Object((1,3,6,1,4,1,34774,4,1,2,1,1,1),_ForwardAddrIndex_Type())
forwardAddrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:forwardAddrIndex.setStatus(_B)
_ForwardAddrIP_Type=IpAddress
_ForwardAddrIP_Object=MibTableColumn
forwardAddrIP=_ForwardAddrIP_Object((1,3,6,1,4,1,34774,4,1,2,1,1,2),_ForwardAddrIP_Type())
forwardAddrIP.setMaxAccess(_E)
if mibBuilder.loadTexts:forwardAddrIP.setStatus(_B)
_ForwardAddrPort_Type=Gauge32
_ForwardAddrPort_Object=MibTableColumn
forwardAddrPort=_ForwardAddrPort_Object((1,3,6,1,4,1,34774,4,1,2,1,1,3),_ForwardAddrPort_Type())
forwardAddrPort.setMaxAccess(_E)
if mibBuilder.loadTexts:forwardAddrPort.setStatus(_B)
_ForwardAddrTrapVer_Type=Integer32
_ForwardAddrTrapVer_Object=MibTableColumn
forwardAddrTrapVer=_ForwardAddrTrapVer_Object((1,3,6,1,4,1,34774,4,1,2,1,1,4),_ForwardAddrTrapVer_Type())
forwardAddrTrapVer.setMaxAccess(_E)
if mibBuilder.loadTexts:forwardAddrTrapVer.setStatus(_B)
_ForwardAddrRowStatus_Type=RowStatus
_ForwardAddrRowStatus_Object=MibTableColumn
forwardAddrRowStatus=_ForwardAddrRowStatus_Object((1,3,6,1,4,1,34774,4,1,2,1,1,5),_ForwardAddrRowStatus_Type())
forwardAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:forwardAddrRowStatus.setStatus(_B)
_ForwardAddrIPNew_Type=OctetString
_ForwardAddrIPNew_Object=MibTableColumn
forwardAddrIPNew=_ForwardAddrIPNew_Object((1,3,6,1,4,1,34774,4,1,2,1,1,6),_ForwardAddrIPNew_Type())
forwardAddrIPNew.setMaxAccess(_E)
if mibBuilder.loadTexts:forwardAddrIPNew.setStatus(_B)
_ForwardAddrTrapType_Type=Integer32
_ForwardAddrTrapType_Object=MibTableColumn
forwardAddrTrapType=_ForwardAddrTrapType_Object((1,3,6,1,4,1,34774,4,1,2,1,1,7),_ForwardAddrTrapType_Type())
forwardAddrTrapType.setMaxAccess(_E)
if mibBuilder.loadTexts:forwardAddrTrapType.setStatus(_B)
_ForwardAddrUSMUserName_Type=OctetString
_ForwardAddrUSMUserName_Object=MibTableColumn
forwardAddrUSMUserName=_ForwardAddrUSMUserName_Object((1,3,6,1,4,1,34774,4,1,2,1,1,8),_ForwardAddrUSMUserName_Type())
forwardAddrUSMUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:forwardAddrUSMUserName.setStatus(_B)
_Event_ObjectIdentity=ObjectIdentity
event=_Event_ObjectIdentity((1,3,6,1,4,1,34774,4,1,3))
_EventTable_Object=MibTable
eventTable=_EventTable_Object((1,3,6,1,4,1,34774,4,1,3,1))
if mibBuilder.loadTexts:eventTable.setStatus(_B)
_EventEntry_Object=MibTableRow
eventEntry=_EventEntry_Object((1,3,6,1,4,1,34774,4,1,3,1,1))
eventEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:eventEntry.setStatus(_B)
_HwIsmEventType_Type=Unsigned32
_HwIsmEventType_Object=MibTableColumn
hwIsmEventType=_HwIsmEventType_Object((1,3,6,1,4,1,34774,4,1,3,1,1,1),_HwIsmEventType_Type())
hwIsmEventType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmEventType.setStatus(_B)
_HwIsmEventID_Type=Counter64
_HwIsmEventID_Object=MibTableColumn
hwIsmEventID=_HwIsmEventID_Object((1,3,6,1,4,1,34774,4,1,3,1,1,2),_HwIsmEventID_Type())
hwIsmEventID.setMaxAccess('read-only')
if mibBuilder.loadTexts:hwIsmEventID.setStatus(_B)
_HwIsmEventLevel_Type=Unsigned32
_HwIsmEventLevel_Object=MibTableColumn
hwIsmEventLevel=_HwIsmEventLevel_Object((1,3,6,1,4,1,34774,4,1,3,1,1,3),_HwIsmEventLevel_Type())
hwIsmEventLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmEventLevel.setStatus(_B)
_HwIsmEventSequence_Type=Unsigned32
_HwIsmEventSequence_Object=MibTableColumn
hwIsmEventSequence=_HwIsmEventSequence_Object((1,3,6,1,4,1,34774,4,1,3,1,1,4),_HwIsmEventSequence_Type())
hwIsmEventSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmEventSequence.setStatus(_B)
_HwIsmEventTime_Type=Unsigned32
_HwIsmEventTime_Object=MibTableColumn
hwIsmEventTime=_HwIsmEventTime_Object((1,3,6,1,4,1,34774,4,1,3,1,1,5),_HwIsmEventTime_Type())
hwIsmEventTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmEventTime.setStatus(_B)
_HwIsmEventRecoveryTime_Type=Unsigned32
_HwIsmEventRecoveryTime_Object=MibTableColumn
hwIsmEventRecoveryTime=_HwIsmEventRecoveryTime_Object((1,3,6,1,4,1,34774,4,1,3,1,1,6),_HwIsmEventRecoveryTime_Type())
hwIsmEventRecoveryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmEventRecoveryTime.setStatus(_B)
_HwIsmEventParameter_Type=OctetString
_HwIsmEventParameter_Object=MibTableColumn
hwIsmEventParameter=_HwIsmEventParameter_Object((1,3,6,1,4,1,34774,4,1,3,1,1,7),_HwIsmEventParameter_Type())
hwIsmEventParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmEventParameter.setStatus(_B)
_HwIsmEventRowStatus_Type=RowStatus
_HwIsmEventRowStatus_Object=MibTableColumn
hwIsmEventRowStatus=_HwIsmEventRowStatus_Object((1,3,6,1,4,1,34774,4,1,3,1,1,20),_HwIsmEventRowStatus_Type())
hwIsmEventRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwIsmEventRowStatus.setStatus(_B)
_TrapEvent_ObjectIdentity=ObjectIdentity
trapEvent=_TrapEvent_ObjectIdentity((1,3,6,1,4,1,34774,4,1,3,3))
_HwIsmTrapEventType_Type=Unsigned32
_HwIsmTrapEventType_Object=MibScalar
hwIsmTrapEventType=_HwIsmTrapEventType_Object((1,3,6,1,4,1,34774,4,1,3,3,1),_HwIsmTrapEventType_Type())
hwIsmTrapEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventType.setStatus(_B)
_HwIsmTrapEventID_Type=Counter64
_HwIsmTrapEventID_Object=MibScalar
hwIsmTrapEventID=_HwIsmTrapEventID_Object((1,3,6,1,4,1,34774,4,1,3,3,2),_HwIsmTrapEventID_Type())
hwIsmTrapEventID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventID.setStatus(_B)
_HwIsmTrapEventLevel_Type=Unsigned32
_HwIsmTrapEventLevel_Object=MibScalar
hwIsmTrapEventLevel=_HwIsmTrapEventLevel_Object((1,3,6,1,4,1,34774,4,1,3,3,3),_HwIsmTrapEventLevel_Type())
hwIsmTrapEventLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventLevel.setStatus(_B)
_HwIsmTrapEventSequence_Type=Unsigned32
_HwIsmTrapEventSequence_Object=MibScalar
hwIsmTrapEventSequence=_HwIsmTrapEventSequence_Object((1,3,6,1,4,1,34774,4,1,3,3,4),_HwIsmTrapEventSequence_Type())
hwIsmTrapEventSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventSequence.setStatus(_B)
_HwIsmTrapEventTime_Type=Unsigned32
_HwIsmTrapEventTime_Object=MibScalar
hwIsmTrapEventTime=_HwIsmTrapEventTime_Object((1,3,6,1,4,1,34774,4,1,3,3,5),_HwIsmTrapEventTime_Type())
hwIsmTrapEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventTime.setStatus(_B)
_HwIsmTrapEventRecoveryTime_Type=Unsigned32
_HwIsmTrapEventRecoveryTime_Object=MibScalar
hwIsmTrapEventRecoveryTime=_HwIsmTrapEventRecoveryTime_Object((1,3,6,1,4,1,34774,4,1,3,3,6),_HwIsmTrapEventRecoveryTime_Type())
hwIsmTrapEventRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventRecoveryTime.setStatus(_B)
_HwIsmTrapEventParameter_Type=OctetString
_HwIsmTrapEventParameter_Object=MibScalar
hwIsmTrapEventParameter=_HwIsmTrapEventParameter_Object((1,3,6,1,4,1,34774,4,1,3,3,7),_HwIsmTrapEventParameter_Type())
hwIsmTrapEventParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventParameter.setStatus(_B)
_HwIsmTrapEventID32Bit_Type=Unsigned32
_HwIsmTrapEventID32Bit_Object=MibScalar
hwIsmTrapEventID32Bit=_HwIsmTrapEventID32Bit_Object((1,3,6,1,4,1,34774,4,1,3,3,8),_HwIsmTrapEventID32Bit_Type())
hwIsmTrapEventID32Bit.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventID32Bit.setStatus(_B)
_HwIsmTrapEventTimeStr_Type=OctetString
_HwIsmTrapEventTimeStr_Object=MibScalar
hwIsmTrapEventTimeStr=_HwIsmTrapEventTimeStr_Object((1,3,6,1,4,1,34774,4,1,3,3,9),_HwIsmTrapEventTimeStr_Type())
hwIsmTrapEventTimeStr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventTimeStr.setStatus(_B)
_HwIsmTrapEventRecoveryTimeStr_Type=OctetString
_HwIsmTrapEventRecoveryTimeStr_Object=MibScalar
hwIsmTrapEventRecoveryTimeStr=_HwIsmTrapEventRecoveryTimeStr_Object((1,3,6,1,4,1,34774,4,1,3,3,10),_HwIsmTrapEventRecoveryTimeStr_Type())
hwIsmTrapEventRecoveryTimeStr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsmTrapEventRecoveryTimeStr.setStatus(_B)
_NotificationType_ObjectIdentity=ObjectIdentity
notificationType=_NotificationType_ObjectIdentity((1,3,6,1,4,1,34774,4,1,4))
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_A,_F),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_N),(_A,_Y),(_A,_Z),(_A,_a),(_A,_G),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_B)
eventType=NotificationType((1,3,6,1,4,1,34774,4,1,4,2))
eventType.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:eventType.setStatus(_B)
currentNotificationGroup=NotificationGroup((1,6,1,2))
currentNotificationGroup.setObjects((_A,_f))
if mibBuilder.loadTexts:currentNotificationGroup.setStatus(_B)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:basicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NodeCodeString':NodeCodeString,'huaweistorage':huaweistorage,'hwStorage':hwStorage,'hwISM':hwISM,'trapAddress':trapAddress,'forwardAddrTable':forwardAddrTable,'forwardAddrEntry':forwardAddrEntry,_F:forwardAddrIndex,_O:forwardAddrIP,_P:forwardAddrPort,_Q:forwardAddrTrapVer,_R:forwardAddrRowStatus,_S:forwardAddrIPNew,_T:forwardAddrTrapType,_U:forwardAddrUSMUserName,'event':event,'eventTable':eventTable,'eventEntry':eventEntry,_Y:hwIsmEventType,_Z:hwIsmEventID,_a:hwIsmEventLevel,_G:hwIsmEventSequence,_b:hwIsmEventTime,_c:hwIsmEventRecoveryTime,_d:hwIsmEventParameter,_e:hwIsmEventRowStatus,'trapEvent':trapEvent,_H:hwIsmTrapEventType,_I:hwIsmTrapEventID,_J:hwIsmTrapEventLevel,_K:hwIsmTrapEventSequence,_L:hwIsmTrapEventTime,_M:hwIsmTrapEventRecoveryTime,_N:hwIsmTrapEventParameter,_V:hwIsmTrapEventID32Bit,_W:hwIsmTrapEventTimeStr,_X:hwIsmTrapEventRecoveryTimeStr,'notificationType':notificationType,_f:eventType,'isoConformance':isoConformance,'isoGroups':isoGroups,_g:currentObjectGroup,_h:currentNotificationGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})