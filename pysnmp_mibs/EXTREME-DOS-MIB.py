_H='read-only'
_G='extremeDosIfIndex'
_F='extremeDosAlertLevel'
_E='EXTREME-DOS-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,extremeV2Traps,extremenetworks=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent','extremeV2Traps','extremenetworks')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
extremeDosMib=ModuleIdentity((1,3,6,1,4,1,1916,1,28))
_ExtremeDosProtect_ObjectIdentity=ObjectIdentity
extremeDosProtect=_ExtremeDosProtect_ObjectIdentity((1,3,6,1,4,1,1916,1,28,1))
class _ExtremeDosEnable_Type(TruthValue):defaultValue=2
_ExtremeDosEnable_Type.__name__=_D
_ExtremeDosEnable_Object=MibScalar
extremeDosEnable=_ExtremeDosEnable_Object((1,3,6,1,4,1,1916,1,28,1,1),_ExtremeDosEnable_Type())
extremeDosEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDosEnable.setStatus(_A)
class _ExtremeDosNoticeLevel_Type(Integer32):defaultValue=4000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,100000))
_ExtremeDosNoticeLevel_Type.__name__=_C
_ExtremeDosNoticeLevel_Object=MibScalar
extremeDosNoticeLevel=_ExtremeDosNoticeLevel_Object((1,3,6,1,4,1,1916,1,28,1,2),_ExtremeDosNoticeLevel_Type())
extremeDosNoticeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDosNoticeLevel.setStatus(_A)
class _ExtremeDosAlertLevel_Type(Integer32):defaultValue=4000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,100000))
_ExtremeDosAlertLevel_Type.__name__=_C
_ExtremeDosAlertLevel_Object=MibScalar
extremeDosAlertLevel=_ExtremeDosAlertLevel_Object((1,3,6,1,4,1,1916,1,28,1,3),_ExtremeDosAlertLevel_Type())
extremeDosAlertLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDosAlertLevel.setStatus(_A)
class _ExtremeDosFilterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('destination',1),('source',2),('destinationAndSource',3)))
_ExtremeDosFilterType_Type.__name__=_C
_ExtremeDosFilterType_Object=MibScalar
extremeDosFilterType=_ExtremeDosFilterType_Object((1,3,6,1,4,1,1916,1,28,1,4),_ExtremeDosFilterType_Type())
extremeDosFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDosFilterType.setStatus(_A)
class _ExtremeDosAclTimeout_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,300))
_ExtremeDosAclTimeout_Type.__name__=_C
_ExtremeDosAclTimeout_Object=MibScalar
extremeDosAclTimeout=_ExtremeDosAclTimeout_Object((1,3,6,1,4,1,1916,1,28,1,5),_ExtremeDosAclTimeout_Type())
extremeDosAclTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDosAclTimeout.setStatus(_A)
class _ExtremeDosAclRulePrecedence_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25588))
_ExtremeDosAclRulePrecedence_Type.__name__=_C
_ExtremeDosAclRulePrecedence_Object=MibScalar
extremeDosAclRulePrecedence=_ExtremeDosAclRulePrecedence_Object((1,3,6,1,4,1,1916,1,28,1,6),_ExtremeDosAclRulePrecedence_Type())
extremeDosAclRulePrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDosAclRulePrecedence.setStatus(_A)
class _ExtremeDosMessagesEnable_Type(TruthValue):defaultValue=1
_ExtremeDosMessagesEnable_Type.__name__=_D
_ExtremeDosMessagesEnable_Object=MibScalar
extremeDosMessagesEnable=_ExtremeDosMessagesEnable_Object((1,3,6,1,4,1,1916,1,28,1,7),_ExtremeDosMessagesEnable_Type())
extremeDosMessagesEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDosMessagesEnable.setStatus(_A)
_ExtremeDosPortTable_Object=MibTable
extremeDosPortTable=_ExtremeDosPortTable_Object((1,3,6,1,4,1,1916,1,28,1,8))
if mibBuilder.loadTexts:extremeDosPortTable.setStatus(_A)
_ExtremeDosPortEntry_Object=MibTableRow
extremeDosPortEntry=_ExtremeDosPortEntry_Object((1,3,6,1,4,1,1916,1,28,1,8,1))
extremeDosPortEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:extremeDosPortEntry.setStatus(_A)
_ExtremeDosIfIndex_Type=Integer32
_ExtremeDosIfIndex_Object=MibTableColumn
extremeDosIfIndex=_ExtremeDosIfIndex_Object((1,3,6,1,4,1,1916,1,28,1,8,1,1),_ExtremeDosIfIndex_Type())
extremeDosIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDosIfIndex.setStatus(_A)
class _ExtremeDosPortTrusted_Type(TruthValue):defaultValue=2
_ExtremeDosPortTrusted_Type.__name__=_D
_ExtremeDosPortTrusted_Object=MibTableColumn
extremeDosPortTrusted=_ExtremeDosPortTrusted_Object((1,3,6,1,4,1,1916,1,28,1,8,1,2),_ExtremeDosPortTrusted_Type())
extremeDosPortTrusted.setMaxAccess('read-create')
if mibBuilder.loadTexts:extremeDosPortTrusted.setStatus(_A)
_ExtremeDosIsDosActive_Type=TruthValue
_ExtremeDosIsDosActive_Object=MibTableColumn
extremeDosIsDosActive=_ExtremeDosIsDosActive_Object((1,3,6,1,4,1,1916,1,28,1,8,1,3),_ExtremeDosIsDosActive_Type())
extremeDosIsDosActive.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDosIsDosActive.setStatus(_A)
_ExtremeDosTraps_ObjectIdentity=ObjectIdentity
extremeDosTraps=_ExtremeDosTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,14))
_ExtremeDosTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeDosTrapsPrefix=_ExtremeDosTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,14,0))
extremeDosThresholdCleared=NotificationType((1,3,6,1,4,1,1916,4,14,0,1))
extremeDosThresholdCleared.setObjects((_E,_F))
if mibBuilder.loadTexts:extremeDosThresholdCleared.setStatus(_A)
extremeDosThresholdReached=NotificationType((1,3,6,1,4,1,1916,4,14,0,2))
extremeDosThresholdReached.setObjects((_E,_F))
if mibBuilder.loadTexts:extremeDosThresholdReached.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'extremeDosMib':extremeDosMib,'extremeDosProtect':extremeDosProtect,'extremeDosEnable':extremeDosEnable,'extremeDosNoticeLevel':extremeDosNoticeLevel,_F:extremeDosAlertLevel,'extremeDosFilterType':extremeDosFilterType,'extremeDosAclTimeout':extremeDosAclTimeout,'extremeDosAclRulePrecedence':extremeDosAclRulePrecedence,'extremeDosMessagesEnable':extremeDosMessagesEnable,'extremeDosPortTable':extremeDosPortTable,'extremeDosPortEntry':extremeDosPortEntry,_G:extremeDosIfIndex,'extremeDosPortTrusted':extremeDosPortTrusted,'extremeDosIsDosActive':extremeDosIsDosActive,'extremeDosTraps':extremeDosTraps,'extremeDosTrapsPrefix':extremeDosTrapsPrefix,'extremeDosThresholdCleared':extremeDosThresholdCleared,'extremeDosThresholdReached':extremeDosThresholdReached})