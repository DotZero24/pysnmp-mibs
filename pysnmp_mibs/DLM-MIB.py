_R='snmpOIDSequence'
_Q='snmpOIDOwner'
_P='snmpOIDDestination'
_O='alarm-condition'
_N='active'
_M='suspend'
_L='activate'
_K='public'
_J='snmpPollOwner'
_I='snmpPollDestination'
_H='TimeTicks'
_G='inactive'
_F='OctetString'
_E='DLM-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctronDLM,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctronDLM')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_SnmpPollTable_Object=MibTable
snmpPollTable=_SnmpPollTable_Object((1,3,6,1,4,1,52,4,2,1,1))
if mibBuilder.loadTexts:snmpPollTable.setStatus(_A)
_SnmpPollEntry_Object=MibTableRow
snmpPollEntry=_SnmpPollEntry_Object((1,3,6,1,4,1,52,4,2,1,1,1))
snmpPollEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:snmpPollEntry.setStatus(_A)
_SnmpPollDestination_Type=IpAddress
_SnmpPollDestination_Object=MibTableColumn
snmpPollDestination=_SnmpPollDestination_Object((1,3,6,1,4,1,52,4,2,1,1,1,1),_SnmpPollDestination_Type())
snmpPollDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpPollDestination.setStatus(_A)
_SnmpPollOwner_Type=IpAddress
_SnmpPollOwner_Object=MibTableColumn
snmpPollOwner=_SnmpPollOwner_Object((1,3,6,1,4,1,52,4,2,1,1,1,2),_SnmpPollOwner_Type())
snmpPollOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpPollOwner.setStatus(_A)
class _SnmpPollCommunity_Type(OctetString):defaultValue=OctetString(_K)
_SnmpPollCommunity_Type.__name__=_F
_SnmpPollCommunity_Object=MibTableColumn
snmpPollCommunity=_SnmpPollCommunity_Object((1,3,6,1,4,1,52,4,2,1,1,1,3),_SnmpPollCommunity_Type())
snmpPollCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollCommunity.setStatus(_A)
class _SnmpPollInterval_Type(Integer32):defaultValue=60
_SnmpPollInterval_Type.__name__=_C
_SnmpPollInterval_Object=MibTableColumn
snmpPollInterval=_SnmpPollInterval_Object((1,3,6,1,4,1,52,4,2,1,1,1,4),_SnmpPollInterval_Type())
snmpPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollInterval.setStatus(_A)
class _SnmpPollRetry_Type(Integer32):defaultValue=3
_SnmpPollRetry_Type.__name__=_C
_SnmpPollRetry_Object=MibTableColumn
snmpPollRetry=_SnmpPollRetry_Object((1,3,6,1,4,1,52,4,2,1,1,1,5),_SnmpPollRetry_Type())
snmpPollRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollRetry.setStatus(_A)
class _SnmpPollAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no-action',1),('send-trap',2)))
_SnmpPollAction_Type.__name__=_C
_SnmpPollAction_Object=MibTableColumn
snmpPollAction=_SnmpPollAction_Object((1,3,6,1,4,1,52,4,2,1,1,1,6),_SnmpPollAction_Type())
snmpPollAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollAction.setStatus(_A)
_SnmpPollTrapAddress_Type=IpAddress
_SnmpPollTrapAddress_Object=MibTableColumn
snmpPollTrapAddress=_SnmpPollTrapAddress_Object((1,3,6,1,4,1,52,4,2,1,1,1,7),_SnmpPollTrapAddress_Type())
snmpPollTrapAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollTrapAddress.setStatus(_A)
class _SnmpPollType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('invalid',2),(_L,3),(_M,4)))
_SnmpPollType_Type.__name__=_C
_SnmpPollType_Object=MibTableColumn
snmpPollType=_SnmpPollType_Object((1,3,6,1,4,1,52,4,2,1,1,1,8),_SnmpPollType_Type())
snmpPollType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollType.setStatus(_A)
class _SnmpPollStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_N,2),('lost-contact',3),(_O,4),('general-failure',5)))
_SnmpPollStatus_Type.__name__=_C
_SnmpPollStatus_Object=MibTableColumn
snmpPollStatus=_SnmpPollStatus_Object((1,3,6,1,4,1,52,4,2,1,1,1,9),_SnmpPollStatus_Type())
snmpPollStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpPollStatus.setStatus(_A)
_SnmpPollRequests_Type=Counter32
_SnmpPollRequests_Object=MibTableColumn
snmpPollRequests=_SnmpPollRequests_Object((1,3,6,1,4,1,52,4,2,1,1,1,10),_SnmpPollRequests_Type())
snmpPollRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpPollRequests.setStatus(_A)
_SnmpPollLastContact_Type=TimeTicks
_SnmpPollLastContact_Object=MibTableColumn
snmpPollLastContact=_SnmpPollLastContact_Object((1,3,6,1,4,1,52,4,2,1,1,1,11),_SnmpPollLastContact_Type())
snmpPollLastContact.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpPollLastContact.setStatus(_A)
_SnmpPollLastAlarm_Type=TimeTicks
_SnmpPollLastAlarm_Object=MibTableColumn
snmpPollLastAlarm=_SnmpPollLastAlarm_Object((1,3,6,1,4,1,52,4,2,1,1,1,12),_SnmpPollLastAlarm_Type())
snmpPollLastAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpPollLastAlarm.setStatus(_A)
class _SnmpPollAlarmWait_Type(Integer32):defaultValue=60
_SnmpPollAlarmWait_Type.__name__=_C
_SnmpPollAlarmWait_Object=MibTableColumn
snmpPollAlarmWait=_SnmpPollAlarmWait_Object((1,3,6,1,4,1,52,4,2,1,1,1,13),_SnmpPollAlarmWait_Type())
snmpPollAlarmWait.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollAlarmWait.setStatus(_A)
class _SnmpPollTrapCommunity_Type(OctetString):defaultValue=OctetString(_K)
_SnmpPollTrapCommunity_Type.__name__=_F
_SnmpPollTrapCommunity_Object=MibTableColumn
snmpPollTrapCommunity=_SnmpPollTrapCommunity_Object((1,3,6,1,4,1,52,4,2,1,1,1,14),_SnmpPollTrapCommunity_Type())
snmpPollTrapCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollTrapCommunity.setStatus(_A)
class _SnmpPollProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internet-ping',1),('snmp',2)))
_SnmpPollProtocol_Type.__name__=_C
_SnmpPollProtocol_Object=MibTableColumn
snmpPollProtocol=_SnmpPollProtocol_Object((1,3,6,1,4,1,52,4,2,1,1,1,15),_SnmpPollProtocol_Type())
snmpPollProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpPollProtocol.setStatus(_A)
_SnmpOIDTable_Object=MibTable
snmpOIDTable=_SnmpOIDTable_Object((1,3,6,1,4,1,52,4,2,1,2))
if mibBuilder.loadTexts:snmpOIDTable.setStatus(_A)
_SnmpOIDEntry_Object=MibTableRow
snmpOIDEntry=_SnmpOIDEntry_Object((1,3,6,1,4,1,52,4,2,1,2,1))
snmpOIDEntry.setIndexNames((0,_E,_P),(0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:snmpOIDEntry.setStatus(_A)
_SnmpOIDDestination_Type=IpAddress
_SnmpOIDDestination_Object=MibTableColumn
snmpOIDDestination=_SnmpOIDDestination_Object((1,3,6,1,4,1,52,4,2,1,2,1,1),_SnmpOIDDestination_Type())
snmpOIDDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDDestination.setStatus(_A)
_SnmpOIDOwner_Type=IpAddress
_SnmpOIDOwner_Object=MibTableColumn
snmpOIDOwner=_SnmpOIDOwner_Object((1,3,6,1,4,1,52,4,2,1,2,1,2),_SnmpOIDOwner_Type())
snmpOIDOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDOwner.setStatus(_A)
_SnmpOIDSequence_Type=Integer32
_SnmpOIDSequence_Object=MibTableColumn
snmpOIDSequence=_SnmpOIDSequence_Object((1,3,6,1,4,1,52,4,2,1,2,1,3),_SnmpOIDSequence_Type())
snmpOIDSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDSequence.setStatus(_A)
_SnmpOIDObject_Type=ObjectIdentifier
_SnmpOIDObject_Object=MibTableColumn
snmpOIDObject=_SnmpOIDObject_Object((1,3,6,1,4,1,52,4,2,1,2,1,4),_SnmpOIDObject_Type())
snmpOIDObject.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDObject.setStatus(_A)
class _SnmpOIDComparator_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('equal',1),('greater',2),('less',3),('greater-or-equal',4),('less-or-equal',5),('trap-always',6),('dont-compare',7),('not-equal',8)))
_SnmpOIDComparator_Type.__name__=_C
_SnmpOIDComparator_Object=MibTableColumn
snmpOIDComparator=_SnmpOIDComparator_Object((1,3,6,1,4,1,52,4,2,1,2,1,5),_SnmpOIDComparator_Type())
snmpOIDComparator.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDComparator.setStatus(_A)
class _SnmpOIDEnumType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('integer',1),('counter',2),('gauge',3),('ticks',4)))
_SnmpOIDEnumType_Type.__name__=_C
_SnmpOIDEnumType_Object=MibTableColumn
snmpOIDEnumType=_SnmpOIDEnumType_Object((1,3,6,1,4,1,52,4,2,1,2,1,6),_SnmpOIDEnumType_Type())
snmpOIDEnumType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDEnumType.setStatus(_A)
class _SnmpOIDThresholdInteger_Type(Integer32):defaultValue=0
_SnmpOIDThresholdInteger_Type.__name__=_C
_SnmpOIDThresholdInteger_Object=MibTableColumn
snmpOIDThresholdInteger=_SnmpOIDThresholdInteger_Object((1,3,6,1,4,1,52,4,2,1,2,1,7),_SnmpOIDThresholdInteger_Type())
snmpOIDThresholdInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDThresholdInteger.setStatus(_A)
_SnmpOIDThresholdCounter_Type=Counter32
_SnmpOIDThresholdCounter_Object=MibTableColumn
snmpOIDThresholdCounter=_SnmpOIDThresholdCounter_Object((1,3,6,1,4,1,52,4,2,1,2,1,8),_SnmpOIDThresholdCounter_Type())
snmpOIDThresholdCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDThresholdCounter.setStatus(_A)
_SnmpOIDThresholdGauge_Type=Gauge32
_SnmpOIDThresholdGauge_Object=MibTableColumn
snmpOIDThresholdGauge=_SnmpOIDThresholdGauge_Object((1,3,6,1,4,1,52,4,2,1,2,1,9),_SnmpOIDThresholdGauge_Type())
snmpOIDThresholdGauge.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDThresholdGauge.setStatus(_A)
class _SnmpOIDThresholdTicks_Type(TimeTicks):defaultValue=0
_SnmpOIDThresholdTicks_Type.__name__=_H
_SnmpOIDThresholdTicks_Object=MibTableColumn
snmpOIDThresholdTicks=_SnmpOIDThresholdTicks_Object((1,3,6,1,4,1,52,4,2,1,2,1,10),_SnmpOIDThresholdTicks_Type())
snmpOIDThresholdTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDThresholdTicks.setStatus(_A)
class _SnmpOIDType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_G,2),(_L,3),(_M,4)))
_SnmpOIDType_Type.__name__=_C
_SnmpOIDType_Object=MibTableColumn
snmpOIDType=_SnmpOIDType_Object((1,3,6,1,4,1,52,4,2,1,2,1,11),_SnmpOIDType_Type())
snmpOIDType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOIDType.setStatus(_A)
class _SnmpOIDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_N,2),(_O,3)))
_SnmpOIDStatus_Type.__name__=_C
_SnmpOIDStatus_Object=MibTableColumn
snmpOIDStatus=_SnmpOIDStatus_Object((1,3,6,1,4,1,52,4,2,1,2,1,12),_SnmpOIDStatus_Type())
snmpOIDStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpOIDStatus.setStatus(_A)
_SnmpOIDLastValue_Type=Integer32
_SnmpOIDLastValue_Object=MibTableColumn
snmpOIDLastValue=_SnmpOIDLastValue_Object((1,3,6,1,4,1,52,4,2,1,2,1,13),_SnmpOIDLastValue_Type())
snmpOIDLastValue.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpOIDLastValue.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'snmpPollTable':snmpPollTable,'snmpPollEntry':snmpPollEntry,_I:snmpPollDestination,_J:snmpPollOwner,'snmpPollCommunity':snmpPollCommunity,'snmpPollInterval':snmpPollInterval,'snmpPollRetry':snmpPollRetry,'snmpPollAction':snmpPollAction,'snmpPollTrapAddress':snmpPollTrapAddress,'snmpPollType':snmpPollType,'snmpPollStatus':snmpPollStatus,'snmpPollRequests':snmpPollRequests,'snmpPollLastContact':snmpPollLastContact,'snmpPollLastAlarm':snmpPollLastAlarm,'snmpPollAlarmWait':snmpPollAlarmWait,'snmpPollTrapCommunity':snmpPollTrapCommunity,'snmpPollProtocol':snmpPollProtocol,'snmpOIDTable':snmpOIDTable,'snmpOIDEntry':snmpOIDEntry,_P:snmpOIDDestination,_Q:snmpOIDOwner,_R:snmpOIDSequence,'snmpOIDObject':snmpOIDObject,'snmpOIDComparator':snmpOIDComparator,'snmpOIDEnumType':snmpOIDEnumType,'snmpOIDThresholdInteger':snmpOIDThresholdInteger,'snmpOIDThresholdCounter':snmpOIDThresholdCounter,'snmpOIDThresholdGauge':snmpOIDThresholdGauge,'snmpOIDThresholdTicks':snmpOIDThresholdTicks,'snmpOIDType':snmpOIDType,'snmpOIDStatus':snmpOIDStatus,'snmpOIDLastValue':snmpOIDLastValue})