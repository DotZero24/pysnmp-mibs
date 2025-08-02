_M='bsUnicastStormControlHighWatermark'
_L='bsUnicastStormControlLowWatermark'
_K='bsUnicastStormControlIfIndex'
_J='packets per second'
_I='TimeInterval'
_H='Integer32'
_G='bsUnicastStormControlPollValue'
_F='Unsigned32'
_E='ifIndex'
_D='IF-MIB'
_C='BAY-STACK-UNICAST-STORM-CONTROL-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I,'TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackUnicastStormControlMib=ModuleIdentity((1,3,6,1,4,1,45,5,22))
if mibBuilder.loadTexts:bayStackUnicastStormControlMib.setRevisions(('2007-06-07 00:00',))
_BsUnicastStormControlNotifications_ObjectIdentity=ObjectIdentity
bsUnicastStormControlNotifications=_BsUnicastStormControlNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,22,0))
_BsUnicastStormControlObjects_ObjectIdentity=ObjectIdentity
bsUnicastStormControlObjects=_BsUnicastStormControlObjects_ObjectIdentity((1,3,6,1,4,1,45,5,22,1))
_BsUnicastStormControlScalars_ObjectIdentity=ObjectIdentity
bsUnicastStormControlScalars=_BsUnicastStormControlScalars_ObjectIdentity((1,3,6,1,4,1,45,5,22,1,1))
_BsUnicastStormControlEnabled_Type=TruthValue
_BsUnicastStormControlEnabled_Object=MibScalar
bsUnicastStormControlEnabled=_BsUnicastStormControlEnabled_Object((1,3,6,1,4,1,45,5,22,1,1,1),_BsUnicastStormControlEnabled_Type())
bsUnicastStormControlEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsUnicastStormControlEnabled.setStatus(_A)
class _BsUnicastStormControlLowWatermark_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000000))
_BsUnicastStormControlLowWatermark_Type.__name__=_F
_BsUnicastStormControlLowWatermark_Object=MibScalar
bsUnicastStormControlLowWatermark=_BsUnicastStormControlLowWatermark_Object((1,3,6,1,4,1,45,5,22,1,1,2),_BsUnicastStormControlLowWatermark_Type())
bsUnicastStormControlLowWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:bsUnicastStormControlLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:bsUnicastStormControlLowWatermark.setUnits(_J)
class _BsUnicastStormControlHighWatermark_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000000))
_BsUnicastStormControlHighWatermark_Type.__name__=_F
_BsUnicastStormControlHighWatermark_Object=MibScalar
bsUnicastStormControlHighWatermark=_BsUnicastStormControlHighWatermark_Object((1,3,6,1,4,1,45,5,22,1,1,3),_BsUnicastStormControlHighWatermark_Type())
bsUnicastStormControlHighWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:bsUnicastStormControlHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:bsUnicastStormControlHighWatermark.setUnits(_J)
class _BsUnicastStormControlPollInterval_Type(TimeInterval):defaultValue=3000;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,30000))
_BsUnicastStormControlPollInterval_Type.__name__=_I
_BsUnicastStormControlPollInterval_Object=MibScalar
bsUnicastStormControlPollInterval=_BsUnicastStormControlPollInterval_Object((1,3,6,1,4,1,45,5,22,1,1,4),_BsUnicastStormControlPollInterval_Type())
bsUnicastStormControlPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bsUnicastStormControlPollInterval.setStatus(_A)
class _BsUnicastStormControlTrapInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_BsUnicastStormControlTrapInterval_Type.__name__=_H
_BsUnicastStormControlTrapInterval_Object=MibScalar
bsUnicastStormControlTrapInterval=_BsUnicastStormControlTrapInterval_Object((1,3,6,1,4,1,45,5,22,1,1,5),_BsUnicastStormControlTrapInterval_Type())
bsUnicastStormControlTrapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bsUnicastStormControlTrapInterval.setStatus(_A)
_BsUnicastStormControlPollValue_Type=Unsigned32
_BsUnicastStormControlPollValue_Object=MibScalar
bsUnicastStormControlPollValue=_BsUnicastStormControlPollValue_Object((1,3,6,1,4,1,45,5,22,1,1,6),_BsUnicastStormControlPollValue_Type())
bsUnicastStormControlPollValue.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:bsUnicastStormControlPollValue.setStatus(_A)
_BsUnicastStormControlIfTable_Object=MibTable
bsUnicastStormControlIfTable=_BsUnicastStormControlIfTable_Object((1,3,6,1,4,1,45,5,22,1,2))
if mibBuilder.loadTexts:bsUnicastStormControlIfTable.setStatus(_A)
_BsUnicastStormControlIfEntry_Object=MibTableRow
bsUnicastStormControlIfEntry=_BsUnicastStormControlIfEntry_Object((1,3,6,1,4,1,45,5,22,1,2,1))
bsUnicastStormControlIfEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:bsUnicastStormControlIfEntry.setStatus(_A)
_BsUnicastStormControlIfIndex_Type=InterfaceIndex
_BsUnicastStormControlIfIndex_Object=MibTableColumn
bsUnicastStormControlIfIndex=_BsUnicastStormControlIfIndex_Object((1,3,6,1,4,1,45,5,22,1,2,1,1),_BsUnicastStormControlIfIndex_Type())
bsUnicastStormControlIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bsUnicastStormControlIfIndex.setStatus(_A)
_BsUnicastStormControlIfEnabled_Type=TruthValue
_BsUnicastStormControlIfEnabled_Object=MibTableColumn
bsUnicastStormControlIfEnabled=_BsUnicastStormControlIfEnabled_Object((1,3,6,1,4,1,45,5,22,1,2,1,2),_BsUnicastStormControlIfEnabled_Type())
bsUnicastStormControlIfEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsUnicastStormControlIfEnabled.setStatus(_A)
bsUnicastStormControlBelowLowWatermark=NotificationType((1,3,6,1,4,1,45,5,22,0,1))
bsUnicastStormControlBelowLowWatermark.setObjects(*((_D,_E),(_C,_G),(_C,_L)))
if mibBuilder.loadTexts:bsUnicastStormControlBelowLowWatermark.setStatus(_A)
bsUnicastStormControlAboveHighWatermark=NotificationType((1,3,6,1,4,1,45,5,22,0,2))
bsUnicastStormControlAboveHighWatermark.setObjects(*((_D,_E),(_C,_G),(_C,_M)))
if mibBuilder.loadTexts:bsUnicastStormControlAboveHighWatermark.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bayStackUnicastStormControlMib':bayStackUnicastStormControlMib,'bsUnicastStormControlNotifications':bsUnicastStormControlNotifications,'bsUnicastStormControlBelowLowWatermark':bsUnicastStormControlBelowLowWatermark,'bsUnicastStormControlAboveHighWatermark':bsUnicastStormControlAboveHighWatermark,'bsUnicastStormControlObjects':bsUnicastStormControlObjects,'bsUnicastStormControlScalars':bsUnicastStormControlScalars,'bsUnicastStormControlEnabled':bsUnicastStormControlEnabled,_L:bsUnicastStormControlLowWatermark,_M:bsUnicastStormControlHighWatermark,'bsUnicastStormControlPollInterval':bsUnicastStormControlPollInterval,'bsUnicastStormControlTrapInterval':bsUnicastStormControlTrapInterval,_G:bsUnicastStormControlPollValue,'bsUnicastStormControlIfTable':bsUnicastStormControlIfTable,'bsUnicastStormControlIfEntry':bsUnicastStormControlIfEntry,_K:bsUnicastStormControlIfIndex,'bsUnicastStormControlIfEnabled':bsUnicastStormControlIfEnabled})