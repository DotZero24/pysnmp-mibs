_P='bsStormControlHighWatermark'
_O='bsStormControlLowWatermark'
_N='bsStormControlIfIndex'
_M='shutdown'
_L='not-accessible'
_K='bsStormControlPollValue'
_J='TimeInterval'
_I='ifIndex'
_H='IF-MIB'
_G='packets per second'
_F='bsStormControlTrafficType'
_E='Unsigned32'
_D='Integer32'
_C='BAY-STACK-STORM-CONTROL-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J,'TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackStormControlMib=ModuleIdentity((1,3,6,1,4,1,45,5,42))
if mibBuilder.loadTexts:bayStackStormControlMib.setRevisions(('2014-03-04 00:00','2012-06-05 00:00'))
_BsStormControlNotifications_ObjectIdentity=ObjectIdentity
bsStormControlNotifications=_BsStormControlNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,42,0))
_BsStormControlObjects_ObjectIdentity=ObjectIdentity
bsStormControlObjects=_BsStormControlObjects_ObjectIdentity((1,3,6,1,4,1,45,5,42,1))
_BsStormControlScalars_ObjectIdentity=ObjectIdentity
bsStormControlScalars=_BsStormControlScalars_ObjectIdentity((1,3,6,1,4,1,45,5,42,1,1))
_BsStormControlPollValue_Type=Unsigned32
_BsStormControlPollValue_Object=MibScalar
bsStormControlPollValue=_BsStormControlPollValue_Object((1,3,6,1,4,1,45,5,42,1,1,1),_BsStormControlPollValue_Type())
bsStormControlPollValue.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:bsStormControlPollValue.setStatus(_A)
_BsStormControlTable_Object=MibTable
bsStormControlTable=_BsStormControlTable_Object((1,3,6,1,4,1,45,5,42,1,2))
if mibBuilder.loadTexts:bsStormControlTable.setStatus(_A)
_BsStormControlEntry_Object=MibTableRow
bsStormControlEntry=_BsStormControlEntry_Object((1,3,6,1,4,1,45,5,42,1,2,1))
bsStormControlEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:bsStormControlEntry.setStatus(_A)
class _BsStormControlTrafficType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('broadcast',2),('multicast',3)))
_BsStormControlTrafficType_Type.__name__=_D
_BsStormControlTrafficType_Object=MibTableColumn
bsStormControlTrafficType=_BsStormControlTrafficType_Object((1,3,6,1,4,1,45,5,42,1,2,1,1),_BsStormControlTrafficType_Type())
bsStormControlTrafficType.setMaxAccess(_L)
if mibBuilder.loadTexts:bsStormControlTrafficType.setStatus(_A)
_BsStormControlEnabled_Type=TruthValue
_BsStormControlEnabled_Object=MibTableColumn
bsStormControlEnabled=_BsStormControlEnabled_Object((1,3,6,1,4,1,45,5,42,1,2,1,2),_BsStormControlEnabled_Type())
bsStormControlEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlEnabled.setStatus(_A)
class _BsStormControlLowWatermark_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000000))
_BsStormControlLowWatermark_Type.__name__=_E
_BsStormControlLowWatermark_Object=MibTableColumn
bsStormControlLowWatermark=_BsStormControlLowWatermark_Object((1,3,6,1,4,1,45,5,42,1,2,1,3),_BsStormControlLowWatermark_Type())
bsStormControlLowWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:bsStormControlLowWatermark.setUnits(_G)
class _BsStormControlHighWatermark_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000000))
_BsStormControlHighWatermark_Type.__name__=_E
_BsStormControlHighWatermark_Object=MibTableColumn
bsStormControlHighWatermark=_BsStormControlHighWatermark_Object((1,3,6,1,4,1,45,5,42,1,2,1,4),_BsStormControlHighWatermark_Type())
bsStormControlHighWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:bsStormControlHighWatermark.setUnits(_G)
class _BsStormControlPollInterval_Type(TimeInterval):defaultValue=3000;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,30000))
_BsStormControlPollInterval_Type.__name__=_J
_BsStormControlPollInterval_Object=MibTableColumn
bsStormControlPollInterval=_BsStormControlPollInterval_Object((1,3,6,1,4,1,45,5,42,1,2,1,5),_BsStormControlPollInterval_Type())
bsStormControlPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlPollInterval.setStatus(_A)
class _BsStormControlTrapInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_BsStormControlTrapInterval_Type.__name__=_D
_BsStormControlTrapInterval_Object=MibTableColumn
bsStormControlTrapInterval=_BsStormControlTrapInterval_Object((1,3,6,1,4,1,45,5,42,1,2,1,6),_BsStormControlTrapInterval_Type())
bsStormControlTrapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlTrapInterval.setStatus(_A)
class _BsStormControlActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('drop',2),(_M,3)))
_BsStormControlActionType_Type.__name__=_D
_BsStormControlActionType_Object=MibTableColumn
bsStormControlActionType=_BsStormControlActionType_Object((1,3,6,1,4,1,45,5,42,1,2,1,7),_BsStormControlActionType_Type())
bsStormControlActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlActionType.setStatus(_A)
_BsStormControlIfTable_Object=MibTable
bsStormControlIfTable=_BsStormControlIfTable_Object((1,3,6,1,4,1,45,5,42,1,3))
if mibBuilder.loadTexts:bsStormControlIfTable.setStatus(_A)
_BsStormControlIfEntry_Object=MibTableRow
bsStormControlIfEntry=_BsStormControlIfEntry_Object((1,3,6,1,4,1,45,5,42,1,3,1))
bsStormControlIfEntry.setIndexNames((0,_C,_F),(0,_C,_N))
if mibBuilder.loadTexts:bsStormControlIfEntry.setStatus(_A)
_BsStormControlIfIndex_Type=InterfaceIndex
_BsStormControlIfIndex_Object=MibTableColumn
bsStormControlIfIndex=_BsStormControlIfIndex_Object((1,3,6,1,4,1,45,5,42,1,3,1,1),_BsStormControlIfIndex_Type())
bsStormControlIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:bsStormControlIfIndex.setStatus(_A)
_BsStormControlIfEnabled_Type=TruthValue
_BsStormControlIfEnabled_Object=MibTableColumn
bsStormControlIfEnabled=_BsStormControlIfEnabled_Object((1,3,6,1,4,1,45,5,42,1,3,1,2),_BsStormControlIfEnabled_Type())
bsStormControlIfEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlIfEnabled.setStatus(_A)
class _BsStormControlIfLowWatermark_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000000))
_BsStormControlIfLowWatermark_Type.__name__=_E
_BsStormControlIfLowWatermark_Object=MibTableColumn
bsStormControlIfLowWatermark=_BsStormControlIfLowWatermark_Object((1,3,6,1,4,1,45,5,42,1,3,1,3),_BsStormControlIfLowWatermark_Type())
bsStormControlIfLowWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlIfLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:bsStormControlIfLowWatermark.setUnits(_G)
class _BsStormControlIfHighWatermark_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000000))
_BsStormControlIfHighWatermark_Type.__name__=_E
_BsStormControlIfHighWatermark_Object=MibTableColumn
bsStormControlIfHighWatermark=_BsStormControlIfHighWatermark_Object((1,3,6,1,4,1,45,5,42,1,3,1,4),_BsStormControlIfHighWatermark_Type())
bsStormControlIfHighWatermark.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlIfHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:bsStormControlIfHighWatermark.setUnits(_G)
class _BsStormControlIfPollInterval_Type(TimeInterval):defaultValue=3000;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,30000))
_BsStormControlIfPollInterval_Type.__name__=_J
_BsStormControlIfPollInterval_Object=MibTableColumn
bsStormControlIfPollInterval=_BsStormControlIfPollInterval_Object((1,3,6,1,4,1,45,5,42,1,3,1,5),_BsStormControlIfPollInterval_Type())
bsStormControlIfPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlIfPollInterval.setStatus(_A)
class _BsStormControlIfTrapInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_BsStormControlIfTrapInterval_Type.__name__=_D
_BsStormControlIfTrapInterval_Object=MibTableColumn
bsStormControlIfTrapInterval=_BsStormControlIfTrapInterval_Object((1,3,6,1,4,1,45,5,42,1,3,1,6),_BsStormControlIfTrapInterval_Type())
bsStormControlIfTrapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlIfTrapInterval.setStatus(_A)
class _BsStormControlIfActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('drop',2),(_M,3)))
_BsStormControlIfActionType_Type.__name__=_D
_BsStormControlIfActionType_Object=MibTableColumn
bsStormControlIfActionType=_BsStormControlIfActionType_Object((1,3,6,1,4,1,45,5,42,1,3,1,7),_BsStormControlIfActionType_Type())
bsStormControlIfActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsStormControlIfActionType.setStatus(_A)
bsStormControlBelowLowWatermark=NotificationType((1,3,6,1,4,1,45,5,42,0,1))
bsStormControlBelowLowWatermark.setObjects(*((_C,_F),(_H,_I),(_C,_K),(_C,_O)))
if mibBuilder.loadTexts:bsStormControlBelowLowWatermark.setStatus(_A)
bsStormControlAboveHighWatermark=NotificationType((1,3,6,1,4,1,45,5,42,0,2))
bsStormControlAboveHighWatermark.setObjects(*((_C,_F),(_H,_I),(_C,_K),(_C,_P)))
if mibBuilder.loadTexts:bsStormControlAboveHighWatermark.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bayStackStormControlMib':bayStackStormControlMib,'bsStormControlNotifications':bsStormControlNotifications,'bsStormControlBelowLowWatermark':bsStormControlBelowLowWatermark,'bsStormControlAboveHighWatermark':bsStormControlAboveHighWatermark,'bsStormControlObjects':bsStormControlObjects,'bsStormControlScalars':bsStormControlScalars,_K:bsStormControlPollValue,'bsStormControlTable':bsStormControlTable,'bsStormControlEntry':bsStormControlEntry,_F:bsStormControlTrafficType,'bsStormControlEnabled':bsStormControlEnabled,_O:bsStormControlLowWatermark,_P:bsStormControlHighWatermark,'bsStormControlPollInterval':bsStormControlPollInterval,'bsStormControlTrapInterval':bsStormControlTrapInterval,'bsStormControlActionType':bsStormControlActionType,'bsStormControlIfTable':bsStormControlIfTable,'bsStormControlIfEntry':bsStormControlIfEntry,_N:bsStormControlIfIndex,'bsStormControlIfEnabled':bsStormControlIfEnabled,'bsStormControlIfLowWatermark':bsStormControlIfLowWatermark,'bsStormControlIfHighWatermark':bsStormControlIfHighWatermark,'bsStormControlIfPollInterval':bsStormControlIfPollInterval,'bsStormControlIfTrapInterval':bsStormControlIfTrapInterval,'bsStormControlIfActionType':bsStormControlIfActionType})