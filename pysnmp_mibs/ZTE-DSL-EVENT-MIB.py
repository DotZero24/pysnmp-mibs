_E='disable'
_D='enable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zte,zxDsl=mibBuilder.importSymbols('ZTE-DSL-MIB','zte','zxDsl')
zxDslEventMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,37))
_ZxDslEventObjects_ObjectIdentity=ObjectIdentity
zxDslEventObjects=_ZxDslEventObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,37,1))
class _ZxDslTrapSendEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxDslTrapSendEnable_Type.__name__=_C
_ZxDslTrapSendEnable_Object=MibScalar
zxDslTrapSendEnable=_ZxDslTrapSendEnable_Object((1,3,6,1,4,1,3902,1004,37,1,1),_ZxDslTrapSendEnable_Type())
zxDslTrapSendEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrapSendEnable.setStatus(_A)
class _ZxDslEventCurrentEventId_Type(Integer32):defaultValue=0
_ZxDslEventCurrentEventId_Type.__name__=_C
_ZxDslEventCurrentEventId_Object=MibScalar
zxDslEventCurrentEventId=_ZxDslEventCurrentEventId_Object((1,3,6,1,4,1,3902,1004,37,1,2),_ZxDslEventCurrentEventId_Type())
zxDslEventCurrentEventId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEventCurrentEventId.setStatus(_A)
_ZxDslEventConfirmEventId_Type=Integer32
_ZxDslEventConfirmEventId_Object=MibScalar
zxDslEventConfirmEventId=_ZxDslEventConfirmEventId_Object((1,3,6,1,4,1,3902,1004,37,1,3),_ZxDslEventConfirmEventId_Type())
zxDslEventConfirmEventId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEventConfirmEventId.setStatus(_A)
_ZxDslEventSynchUnconfirmedEvents_Type=Integer32
_ZxDslEventSynchUnconfirmedEvents_Object=MibScalar
zxDslEventSynchUnconfirmedEvents=_ZxDslEventSynchUnconfirmedEvents_Object((1,3,6,1,4,1,3902,1004,37,1,4),_ZxDslEventSynchUnconfirmedEvents_Type())
zxDslEventSynchUnconfirmedEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEventSynchUnconfirmedEvents.setStatus(_A)
_ZxDslEventCurrUnconfirmedEventCounter_Type=Integer32
_ZxDslEventCurrUnconfirmedEventCounter_Object=MibScalar
zxDslEventCurrUnconfirmedEventCounter=_ZxDslEventCurrUnconfirmedEventCounter_Object((1,3,6,1,4,1,3902,1004,37,1,5),_ZxDslEventCurrUnconfirmedEventCounter_Type())
zxDslEventCurrUnconfirmedEventCounter.setMaxAccess('read-only')
if mibBuilder.loadTexts:zxDslEventCurrUnconfirmedEventCounter.setStatus(_A)
_ZxDslEventNmsHelloTrapMgmt_ObjectIdentity=ObjectIdentity
zxDslEventNmsHelloTrapMgmt=_ZxDslEventNmsHelloTrapMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1004,37,1,6))
class _ZxDslEventNmsHelloTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxDslEventNmsHelloTrapEnable_Type.__name__=_C
_ZxDslEventNmsHelloTrapEnable_Object=MibScalar
zxDslEventNmsHelloTrapEnable=_ZxDslEventNmsHelloTrapEnable_Object((1,3,6,1,4,1,3902,1004,37,1,6,1),_ZxDslEventNmsHelloTrapEnable_Type())
zxDslEventNmsHelloTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEventNmsHelloTrapEnable.setStatus(_A)
class _ZxDslEventNmsHelloTrapInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_ZxDslEventNmsHelloTrapInterval_Type.__name__=_C
_ZxDslEventNmsHelloTrapInterval_Object=MibScalar
zxDslEventNmsHelloTrapInterval=_ZxDslEventNmsHelloTrapInterval_Object((1,3,6,1,4,1,3902,1004,37,1,6,2),_ZxDslEventNmsHelloTrapInterval_Type())
zxDslEventNmsHelloTrapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEventNmsHelloTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:zxDslEventNmsHelloTrapInterval.setUnits('second')
_ZxDslEventTrapObjects_ObjectIdentity=ObjectIdentity
zxDslEventTrapObjects=_ZxDslEventTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,37,2))
zxDslDisabledTrapSend=NotificationType((1,3,6,1,4,1,3902,1004,37,2,1))
if mibBuilder.loadTexts:zxDslDisabledTrapSend.setStatus(_A)
zxDslEnabledTrapSend=NotificationType((1,3,6,1,4,1,3902,1004,37,2,2))
if mibBuilder.loadTexts:zxDslEnabledTrapSend.setStatus(_A)
zxAnEventNmsHelloTrap=NotificationType((1,3,6,1,4,1,3902,1015,190,6,2))
if mibBuilder.loadTexts:zxAnEventNmsHelloTrap.setStatus(_A)
mibBuilder.exportSymbols('ZTE-DSL-EVENT-MIB',**{'zxDslEventMib':zxDslEventMib,'zxDslEventObjects':zxDslEventObjects,'zxDslTrapSendEnable':zxDslTrapSendEnable,'zxDslEventCurrentEventId':zxDslEventCurrentEventId,'zxDslEventConfirmEventId':zxDslEventConfirmEventId,'zxDslEventSynchUnconfirmedEvents':zxDslEventSynchUnconfirmedEvents,'zxDslEventCurrUnconfirmedEventCounter':zxDslEventCurrUnconfirmedEventCounter,'zxDslEventNmsHelloTrapMgmt':zxDslEventNmsHelloTrapMgmt,'zxDslEventNmsHelloTrapEnable':zxDslEventNmsHelloTrapEnable,'zxDslEventNmsHelloTrapInterval':zxDslEventNmsHelloTrapInterval,'zxDslEventTrapObjects':zxDslEventTrapObjects,'zxDslDisabledTrapSend':zxDslDisabledTrapSend,'zxDslEnabledTrapSend':zxDslEnabledTrapSend,'zxAnEventNmsHelloTrap':zxAnEventNmsHelloTrap})