_c='acQoSQueueStatsQueueIndex'
_b='acQoSQueueStatsServiceMapIndex'
_a='acQoSQueueActionIndex'
_Z='acQoSQueueActionQueueIndex'
_Y='acQoSQueueActionServiceMapIndex'
_X='acQoSQueueIndex'
_W='acQoSQueueServiceMapIndex'
_V='acQoSServiceMapIndex'
_U='acQoSSetIndex'
_T='acQoSSetMatchMapIndex'
_S='network'
_R='internet'
_Q='critical'
_P='flash-override'
_O='immediate'
_N='routine'
_M='precedence'
_L='acQoSMatchIndex'
_K='acQoSMatchMatchMapIndex'
_J='output'
_I='acQoSMatchMapIndex'
_H='priority'
_G='SnmpAdminString'
_F='Integer32'
_E='not-accessible'
_D='AC-QOS-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acBoardMibs,acGeneric,acProducts,acRegistrations,audioCodes=mibBuilder.importSymbols('AUDIOCODES-TYPES-MIB','acBoardMibs','acGeneric','acProducts','acRegistrations','audioCodes')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,RowStatus,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','RowStatus','TAddress','TextualConvention')
acQoS=ModuleIdentity((1,3,6,1,4,1,5003,9,10,14))
_AcQoSConfiguration_ObjectIdentity=ObjectIdentity
acQoSConfiguration=_AcQoSConfiguration_ObjectIdentity((1,3,6,1,4,1,5003,9,10,14,1))
_AcQoSMatchMapTable_Object=MibTable
acQoSMatchMapTable=_AcQoSMatchMapTable_Object((1,3,6,1,4,1,5003,9,10,14,1,1))
if mibBuilder.loadTexts:acQoSMatchMapTable.setStatus(_A)
_AcQoSMatchMapEntry_Object=MibTableRow
acQoSMatchMapEntry=_AcQoSMatchMapEntry_Object((1,3,6,1,4,1,5003,9,10,14,1,1,1))
acQoSMatchMapEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:acQoSMatchMapEntry.setStatus(_A)
class _AcQoSMatchMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000000,2069099))
_AcQoSMatchMapIndex_Type.__name__=_C
_AcQoSMatchMapIndex_Object=MibTableColumn
acQoSMatchMapIndex=_AcQoSMatchMapIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,1,1,1),_AcQoSMatchMapIndex_Type())
acQoSMatchMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSMatchMapIndex.setStatus(_A)
class _AcQoSMatchMapName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AcQoSMatchMapName_Type.__name__=_G
_AcQoSMatchMapName_Object=MibTableColumn
acQoSMatchMapName=_AcQoSMatchMapName_Object((1,3,6,1,4,1,5003,9,10,14,1,1,1,2),_AcQoSMatchMapName_Type())
acQoSMatchMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchMapName.setStatus(_A)
class _AcQoSMatchMapDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),(_J,2)))
_AcQoSMatchMapDirection_Type.__name__=_F
_AcQoSMatchMapDirection_Object=MibTableColumn
acQoSMatchMapDirection=_AcQoSMatchMapDirection_Object((1,3,6,1,4,1,5003,9,10,14,1,1,1,3),_AcQoSMatchMapDirection_Type())
acQoSMatchMapDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchMapDirection.setStatus(_A)
class _AcQoSMatchMapInterface_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AcQoSMatchMapInterface_Type.__name__=_G
_AcQoSMatchMapInterface_Object=MibTableColumn
acQoSMatchMapInterface=_AcQoSMatchMapInterface_Object((1,3,6,1,4,1,5003,9,10,14,1,1,1,4),_AcQoSMatchMapInterface_Type())
acQoSMatchMapInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchMapInterface.setStatus(_A)
_AcQoSMatchTable_Object=MibTable
acQoSMatchTable=_AcQoSMatchTable_Object((1,3,6,1,4,1,5003,9,10,14,1,2))
if mibBuilder.loadTexts:acQoSMatchTable.setStatus(_A)
_AcQoSMatchEntry_Object=MibTableRow
acQoSMatchEntry=_AcQoSMatchEntry_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1))
acQoSMatchEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:acQoSMatchEntry.setStatus(_A)
class _AcQoSMatchMatchMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000000,2069099))
_AcQoSMatchMatchMapIndex_Type.__name__=_C
_AcQoSMatchMatchMapIndex_Object=MibTableColumn
acQoSMatchMatchMapIndex=_AcQoSMatchMatchMapIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,1),_AcQoSMatchMatchMapIndex_Type())
acQoSMatchMatchMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSMatchMatchMapIndex.setStatus(_A)
class _AcQoSMatchIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_AcQoSMatchIndex_Type.__name__=_C
_AcQoSMatchIndex_Object=MibTableColumn
acQoSMatchIndex=_AcQoSMatchIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,2),_AcQoSMatchIndex_Type())
acQoSMatchIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSMatchIndex.setStatus(_A)
class _AcQoSMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('any',1),('accessMap',2),('dscp',3),('dataLength',4),('packetLength',5),(_M,6),(_H,7)))
_AcQoSMatchType_Type.__name__=_F
_AcQoSMatchType_Object=MibTableColumn
acQoSMatchType=_AcQoSMatchType_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,3),_AcQoSMatchType_Type())
acQoSMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchType.setStatus(_A)
class _AcQoSMatchAccessMap_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AcQoSMatchAccessMap_Type.__name__=_G
_AcQoSMatchAccessMap_Object=MibTableColumn
acQoSMatchAccessMap=_AcQoSMatchAccessMap_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,4),_AcQoSMatchAccessMap_Type())
acQoSMatchAccessMap.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchAccessMap.setStatus(_A)
class _AcQoSMatchDscpValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AcQoSMatchDscpValue_Type.__name__=_C
_AcQoSMatchDscpValue_Object=MibTableColumn
acQoSMatchDscpValue=_AcQoSMatchDscpValue_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,5),_AcQoSMatchDscpValue_Type())
acQoSMatchDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchDscpValue.setStatus(_A)
class _AcQoSMatchMinLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcQoSMatchMinLength_Type.__name__=_C
_AcQoSMatchMinLength_Object=MibTableColumn
acQoSMatchMinLength=_AcQoSMatchMinLength_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,6),_AcQoSMatchMinLength_Type())
acQoSMatchMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchMinLength.setStatus(_A)
class _AcQoSMatchMaxLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcQoSMatchMaxLength_Type.__name__=_C
_AcQoSMatchMaxLength_Object=MibTableColumn
acQoSMatchMaxLength=_AcQoSMatchMaxLength_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,7),_AcQoSMatchMaxLength_Type())
acQoSMatchMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchMaxLength.setStatus(_A)
class _AcQoSMatchPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,0),(_H,1),(_O,2),('flash',3),(_P,4),(_Q,5),(_R,6),(_S,7)))
_AcQoSMatchPrecedenceValue_Type.__name__=_F
_AcQoSMatchPrecedenceValue_Object=MibTableColumn
acQoSMatchPrecedenceValue=_AcQoSMatchPrecedenceValue_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,8),_AcQoSMatchPrecedenceValue_Type())
acQoSMatchPrecedenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchPrecedenceValue.setStatus(_A)
class _AcQoSMatchPriorityValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcQoSMatchPriorityValue_Type.__name__=_C
_AcQoSMatchPriorityValue_Object=MibTableColumn
acQoSMatchPriorityValue=_AcQoSMatchPriorityValue_Object((1,3,6,1,4,1,5003,9,10,14,1,2,1,9),_AcQoSMatchPriorityValue_Type())
acQoSMatchPriorityValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSMatchPriorityValue.setStatus(_A)
_AcQoSSetTable_Object=MibTable
acQoSSetTable=_AcQoSSetTable_Object((1,3,6,1,4,1,5003,9,10,14,1,3))
if mibBuilder.loadTexts:acQoSSetTable.setStatus(_A)
_AcQoSSetEntry_Object=MibTableRow
acQoSSetEntry=_AcQoSSetEntry_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1))
acQoSSetEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:acQoSSetEntry.setStatus(_A)
class _AcQoSSetMatchMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000000,2069099))
_AcQoSSetMatchMapIndex_Type.__name__=_C
_AcQoSSetMatchMapIndex_Object=MibTableColumn
acQoSSetMatchMapIndex=_AcQoSSetMatchMapIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1,1),_AcQoSSetMatchMapIndex_Type())
acQoSSetMatchMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSSetMatchMapIndex.setStatus(_A)
class _AcQoSSetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AcQoSSetIndex_Type.__name__=_C
_AcQoSSetIndex_Object=MibTableColumn
acQoSSetIndex=_AcQoSSetIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1,2),_AcQoSSetIndex_Type())
acQoSSetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSSetIndex.setStatus(_A)
class _AcQoSSetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('queue',1),('dscp',2),(_M,3),(_H,4)))
_AcQoSSetType_Type.__name__=_F
_AcQoSSetType_Object=MibTableColumn
acQoSSetType=_AcQoSSetType_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1,3),_AcQoSSetType_Type())
acQoSSetType.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSSetType.setStatus(_A)
class _AcQoSSetQueueName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AcQoSSetQueueName_Type.__name__=_G
_AcQoSSetQueueName_Object=MibTableColumn
acQoSSetQueueName=_AcQoSSetQueueName_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1,4),_AcQoSSetQueueName_Type())
acQoSSetQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSSetQueueName.setStatus(_A)
class _AcQoSSetDscpValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AcQoSSetDscpValue_Type.__name__=_C
_AcQoSSetDscpValue_Object=MibTableColumn
acQoSSetDscpValue=_AcQoSSetDscpValue_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1,5),_AcQoSSetDscpValue_Type())
acQoSSetDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSSetDscpValue.setStatus(_A)
class _AcQoSSetPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,0),(_H,1),(_O,2),('flash',3),(_P,4),(_Q,5),(_R,6),(_S,7)))
_AcQoSSetPrecedenceValue_Type.__name__=_F
_AcQoSSetPrecedenceValue_Object=MibTableColumn
acQoSSetPrecedenceValue=_AcQoSSetPrecedenceValue_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1,6),_AcQoSSetPrecedenceValue_Type())
acQoSSetPrecedenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSSetPrecedenceValue.setStatus(_A)
class _AcQoSSetPriorityValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcQoSSetPriorityValue_Type.__name__=_C
_AcQoSSetPriorityValue_Object=MibTableColumn
acQoSSetPriorityValue=_AcQoSSetPriorityValue_Object((1,3,6,1,4,1,5003,9,10,14,1,3,1,7),_AcQoSSetPriorityValue_Type())
acQoSSetPriorityValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSSetPriorityValue.setStatus(_A)
_AcQoSServiceMapTable_Object=MibTable
acQoSServiceMapTable=_AcQoSServiceMapTable_Object((1,3,6,1,4,1,5003,9,10,14,1,4))
if mibBuilder.loadTexts:acQoSServiceMapTable.setStatus(_A)
_AcQoSServiceMapEntry_Object=MibTableRow
acQoSServiceMapEntry=_AcQoSServiceMapEntry_Object((1,3,6,1,4,1,5003,9,10,14,1,4,1))
acQoSServiceMapEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:acQoSServiceMapEntry.setStatus(_A)
class _AcQoSServiceMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,69))
_AcQoSServiceMapIndex_Type.__name__=_C
_AcQoSServiceMapIndex_Object=MibTableColumn
acQoSServiceMapIndex=_AcQoSServiceMapIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,4,1,1),_AcQoSServiceMapIndex_Type())
acQoSServiceMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSServiceMapIndex.setStatus(_A)
class _AcQoSServiceMapInterface_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AcQoSServiceMapInterface_Type.__name__=_G
_AcQoSServiceMapInterface_Object=MibTableColumn
acQoSServiceMapInterface=_AcQoSServiceMapInterface_Object((1,3,6,1,4,1,5003,9,10,14,1,4,1,2),_AcQoSServiceMapInterface_Type())
acQoSServiceMapInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSServiceMapInterface.setStatus(_A)
class _AcQoSServiceMapDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),(_J,2)))
_AcQoSServiceMapDirection_Type.__name__=_F
_AcQoSServiceMapDirection_Object=MibTableColumn
acQoSServiceMapDirection=_AcQoSServiceMapDirection_Object((1,3,6,1,4,1,5003,9,10,14,1,4,1,3),_AcQoSServiceMapDirection_Type())
acQoSServiceMapDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSServiceMapDirection.setStatus(_A)
class _AcQoSServiceMapBandwidthLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unlimited',1),('limited',2),('automatic',3)))
_AcQoSServiceMapBandwidthLimit_Type.__name__=_F
_AcQoSServiceMapBandwidthLimit_Object=MibTableColumn
acQoSServiceMapBandwidthLimit=_AcQoSServiceMapBandwidthLimit_Object((1,3,6,1,4,1,5003,9,10,14,1,4,1,4),_AcQoSServiceMapBandwidthLimit_Type())
acQoSServiceMapBandwidthLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSServiceMapBandwidthLimit.setStatus(_A)
_AcQoSServiceMapMaxBandwidth_Type=Unsigned32
_AcQoSServiceMapMaxBandwidth_Object=MibTableColumn
acQoSServiceMapMaxBandwidth=_AcQoSServiceMapMaxBandwidth_Object((1,3,6,1,4,1,5003,9,10,14,1,4,1,5),_AcQoSServiceMapMaxBandwidth_Type())
acQoSServiceMapMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSServiceMapMaxBandwidth.setStatus(_A)
_AcQoSQueueTable_Object=MibTable
acQoSQueueTable=_AcQoSQueueTable_Object((1,3,6,1,4,1,5003,9,10,14,1,5))
if mibBuilder.loadTexts:acQoSQueueTable.setStatus(_A)
_AcQoSQueueEntry_Object=MibTableRow
acQoSQueueEntry=_AcQoSQueueEntry_Object((1,3,6,1,4,1,5003,9,10,14,1,5,1))
acQoSQueueEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:acQoSQueueEntry.setStatus(_A)
class _AcQoSQueueServiceMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,69))
_AcQoSQueueServiceMapIndex_Type.__name__=_C
_AcQoSQueueServiceMapIndex_Object=MibTableColumn
acQoSQueueServiceMapIndex=_AcQoSQueueServiceMapIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,5,1,1),_AcQoSQueueServiceMapIndex_Type())
acQoSQueueServiceMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSQueueServiceMapIndex.setStatus(_A)
class _AcQoSQueueIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AcQoSQueueIndex_Type.__name__=_C
_AcQoSQueueIndex_Object=MibTableColumn
acQoSQueueIndex=_AcQoSQueueIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,5,1,2),_AcQoSQueueIndex_Type())
acQoSQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSQueueIndex.setStatus(_A)
class _AcQoSQueueName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AcQoSQueueName_Type.__name__=_G
_AcQoSQueueName_Object=MibTableColumn
acQoSQueueName=_AcQoSQueueName_Object((1,3,6,1,4,1,5003,9,10,14,1,5,1,3),_AcQoSQueueName_Type())
acQoSQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueName.setStatus(_A)
_AcQoSQueueActionTable_Object=MibTable
acQoSQueueActionTable=_AcQoSQueueActionTable_Object((1,3,6,1,4,1,5003,9,10,14,1,6))
if mibBuilder.loadTexts:acQoSQueueActionTable.setStatus(_A)
_AcQoSQueueActionEntry_Object=MibTableRow
acQoSQueueActionEntry=_AcQoSQueueActionEntry_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1))
acQoSQueueActionEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:acQoSQueueActionEntry.setStatus(_A)
class _AcQoSQueueActionServiceMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,69))
_AcQoSQueueActionServiceMapIndex_Type.__name__=_C
_AcQoSQueueActionServiceMapIndex_Object=MibTableColumn
acQoSQueueActionServiceMapIndex=_AcQoSQueueActionServiceMapIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,1),_AcQoSQueueActionServiceMapIndex_Type())
acQoSQueueActionServiceMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSQueueActionServiceMapIndex.setStatus(_A)
class _AcQoSQueueActionQueueIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AcQoSQueueActionQueueIndex_Type.__name__=_C
_AcQoSQueueActionQueueIndex_Object=MibTableColumn
acQoSQueueActionQueueIndex=_AcQoSQueueActionQueueIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,2),_AcQoSQueueActionQueueIndex_Type())
acQoSQueueActionQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSQueueActionQueueIndex.setStatus(_A)
class _AcQoSQueueActionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AcQoSQueueActionIndex_Type.__name__=_C
_AcQoSQueueActionIndex_Object=MibTableColumn
acQoSQueueActionIndex=_AcQoSQueueActionIndex_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,3),_AcQoSQueueActionIndex_Type())
acQoSQueueActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSQueueActionIndex.setStatus(_A)
class _AcQoSQueueActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bandwidth',1),('bandwidth-percent',2),('policy',3),(_H,4)))
_AcQoSQueueActionType_Type.__name__=_F
_AcQoSQueueActionType_Object=MibTableColumn
acQoSQueueActionType=_AcQoSQueueActionType_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,4),_AcQoSQueueActionType_Type())
acQoSQueueActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueActionType.setStatus(_A)
_AcQoSQueueActionMinBandwidth_Type=Unsigned32
_AcQoSQueueActionMinBandwidth_Object=MibTableColumn
acQoSQueueActionMinBandwidth=_AcQoSQueueActionMinBandwidth_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,5),_AcQoSQueueActionMinBandwidth_Type())
acQoSQueueActionMinBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueActionMinBandwidth.setStatus(_A)
_AcQoSQueueActionMaxBandwidth_Type=Unsigned32
_AcQoSQueueActionMaxBandwidth_Object=MibTableColumn
acQoSQueueActionMaxBandwidth=_AcQoSQueueActionMaxBandwidth_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,6),_AcQoSQueueActionMaxBandwidth_Type())
acQoSQueueActionMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueActionMaxBandwidth.setStatus(_A)
class _AcQoSQueueActionPolicyValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unknown',0),('fairness',1),('fifo',2),('random-detect',3),('strict-priority',4)))
_AcQoSQueueActionPolicyValue_Type.__name__=_F
_AcQoSQueueActionPolicyValue_Object=MibTableColumn
acQoSQueueActionPolicyValue=_AcQoSQueueActionPolicyValue_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,7),_AcQoSQueueActionPolicyValue_Type())
acQoSQueueActionPolicyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueActionPolicyValue.setStatus(_A)
class _AcQoSQueueActionPriorityValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcQoSQueueActionPriorityValue_Type.__name__=_C
_AcQoSQueueActionPriorityValue_Object=MibTableColumn
acQoSQueueActionPriorityValue=_AcQoSQueueActionPriorityValue_Object((1,3,6,1,4,1,5003,9,10,14,1,6,1,8),_AcQoSQueueActionPriorityValue_Type())
acQoSQueueActionPriorityValue.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueActionPriorityValue.setStatus(_A)
_AcQoSStatus_ObjectIdentity=ObjectIdentity
acQoSStatus=_AcQoSStatus_ObjectIdentity((1,3,6,1,4,1,5003,9,10,14,2))
_AcQoSQueueStatsTable_Object=MibTable
acQoSQueueStatsTable=_AcQoSQueueStatsTable_Object((1,3,6,1,4,1,5003,9,10,14,2,1))
if mibBuilder.loadTexts:acQoSQueueStatsTable.setStatus(_A)
_AcQoSQueueStatsEntry_Object=MibTableRow
acQoSQueueStatsEntry=_AcQoSQueueStatsEntry_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1))
acQoSQueueStatsEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:acQoSQueueStatsEntry.setStatus(_A)
class _AcQoSQueueStatsServiceMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,69))
_AcQoSQueueStatsServiceMapIndex_Type.__name__=_C
_AcQoSQueueStatsServiceMapIndex_Object=MibTableColumn
acQoSQueueStatsServiceMapIndex=_AcQoSQueueStatsServiceMapIndex_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,1),_AcQoSQueueStatsServiceMapIndex_Type())
acQoSQueueStatsServiceMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSQueueStatsServiceMapIndex.setStatus(_A)
class _AcQoSQueueStatsQueueIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AcQoSQueueStatsQueueIndex_Type.__name__=_C
_AcQoSQueueStatsQueueIndex_Object=MibTableColumn
acQoSQueueStatsQueueIndex=_AcQoSQueueStatsQueueIndex_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,2),_AcQoSQueueStatsQueueIndex_Type())
acQoSQueueStatsQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:acQoSQueueStatsQueueIndex.setStatus(_A)
_AcQoSQueueStatsPacketSent_Type=Counter32
_AcQoSQueueStatsPacketSent_Object=MibTableColumn
acQoSQueueStatsPacketSent=_AcQoSQueueStatsPacketSent_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,3),_AcQoSQueueStatsPacketSent_Type())
acQoSQueueStatsPacketSent.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueStatsPacketSent.setStatus(_A)
_AcQoSQueueStatsBytesSent_Type=Counter32
_AcQoSQueueStatsBytesSent_Object=MibTableColumn
acQoSQueueStatsBytesSent=_AcQoSQueueStatsBytesSent_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,4),_AcQoSQueueStatsBytesSent_Type())
acQoSQueueStatsBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueStatsBytesSent.setStatus(_A)
_AcQoSQueueStatsPacketsRate_Type=Counter32
_AcQoSQueueStatsPacketsRate_Object=MibTableColumn
acQoSQueueStatsPacketsRate=_AcQoSQueueStatsPacketsRate_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,5),_AcQoSQueueStatsPacketsRate_Type())
acQoSQueueStatsPacketsRate.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueStatsPacketsRate.setStatus(_A)
_AcQoSQueueStatsBytesRate_Type=Counter32
_AcQoSQueueStatsBytesRate_Object=MibTableColumn
acQoSQueueStatsBytesRate=_AcQoSQueueStatsBytesRate_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,6),_AcQoSQueueStatsBytesRate_Type())
acQoSQueueStatsBytesRate.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueStatsBytesRate.setStatus(_A)
_AcQoSQueueStatsPacketsDelayed_Type=Counter32
_AcQoSQueueStatsPacketsDelayed_Object=MibTableColumn
acQoSQueueStatsPacketsDelayed=_AcQoSQueueStatsPacketsDelayed_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,7),_AcQoSQueueStatsPacketsDelayed_Type())
acQoSQueueStatsPacketsDelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueStatsPacketsDelayed.setStatus(_A)
_AcQoSQueueStatsPacketsDropped_Type=Counter32
_AcQoSQueueStatsPacketsDropped_Object=MibTableColumn
acQoSQueueStatsPacketsDropped=_AcQoSQueueStatsPacketsDropped_Object((1,3,6,1,4,1,5003,9,10,14,2,1,1,8),_AcQoSQueueStatsPacketsDropped_Type())
acQoSQueueStatsPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:acQoSQueueStatsPacketsDropped.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'acQoS':acQoS,'acQoSConfiguration':acQoSConfiguration,'acQoSMatchMapTable':acQoSMatchMapTable,'acQoSMatchMapEntry':acQoSMatchMapEntry,_I:acQoSMatchMapIndex,'acQoSMatchMapName':acQoSMatchMapName,'acQoSMatchMapDirection':acQoSMatchMapDirection,'acQoSMatchMapInterface':acQoSMatchMapInterface,'acQoSMatchTable':acQoSMatchTable,'acQoSMatchEntry':acQoSMatchEntry,_K:acQoSMatchMatchMapIndex,_L:acQoSMatchIndex,'acQoSMatchType':acQoSMatchType,'acQoSMatchAccessMap':acQoSMatchAccessMap,'acQoSMatchDscpValue':acQoSMatchDscpValue,'acQoSMatchMinLength':acQoSMatchMinLength,'acQoSMatchMaxLength':acQoSMatchMaxLength,'acQoSMatchPrecedenceValue':acQoSMatchPrecedenceValue,'acQoSMatchPriorityValue':acQoSMatchPriorityValue,'acQoSSetTable':acQoSSetTable,'acQoSSetEntry':acQoSSetEntry,_T:acQoSSetMatchMapIndex,_U:acQoSSetIndex,'acQoSSetType':acQoSSetType,'acQoSSetQueueName':acQoSSetQueueName,'acQoSSetDscpValue':acQoSSetDscpValue,'acQoSSetPrecedenceValue':acQoSSetPrecedenceValue,'acQoSSetPriorityValue':acQoSSetPriorityValue,'acQoSServiceMapTable':acQoSServiceMapTable,'acQoSServiceMapEntry':acQoSServiceMapEntry,_V:acQoSServiceMapIndex,'acQoSServiceMapInterface':acQoSServiceMapInterface,'acQoSServiceMapDirection':acQoSServiceMapDirection,'acQoSServiceMapBandwidthLimit':acQoSServiceMapBandwidthLimit,'acQoSServiceMapMaxBandwidth':acQoSServiceMapMaxBandwidth,'acQoSQueueTable':acQoSQueueTable,'acQoSQueueEntry':acQoSQueueEntry,_W:acQoSQueueServiceMapIndex,_X:acQoSQueueIndex,'acQoSQueueName':acQoSQueueName,'acQoSQueueActionTable':acQoSQueueActionTable,'acQoSQueueActionEntry':acQoSQueueActionEntry,_Y:acQoSQueueActionServiceMapIndex,_Z:acQoSQueueActionQueueIndex,_a:acQoSQueueActionIndex,'acQoSQueueActionType':acQoSQueueActionType,'acQoSQueueActionMinBandwidth':acQoSQueueActionMinBandwidth,'acQoSQueueActionMaxBandwidth':acQoSQueueActionMaxBandwidth,'acQoSQueueActionPolicyValue':acQoSQueueActionPolicyValue,'acQoSQueueActionPriorityValue':acQoSQueueActionPriorityValue,'acQoSStatus':acQoSStatus,'acQoSQueueStatsTable':acQoSQueueStatsTable,'acQoSQueueStatsEntry':acQoSQueueStatsEntry,_b:acQoSQueueStatsServiceMapIndex,_c:acQoSQueueStatsQueueIndex,'acQoSQueueStatsPacketSent':acQoSQueueStatsPacketSent,'acQoSQueueStatsBytesSent':acQoSQueueStatsBytesSent,'acQoSQueueStatsPacketsRate':acQoSQueueStatsPacketsRate,'acQoSQueueStatsBytesRate':acQoSQueueStatsBytesRate,'acQoSQueueStatsPacketsDelayed':acQoSQueueStatsPacketsDelayed,'acQoSQueueStatsPacketsDropped':acQoSQueueStatsPacketsDropped})