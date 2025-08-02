_K='h3cLpbkdtPortIfIndex'
_J='H3cLpbkdtActionType'
_I='Integer32'
_H='h3cLpbkdtVlanID'
_G='OctetString'
_F='H3C-LPBKDT-MIB'
_E='read-write'
_D='ifIndex'
_C='ifDescr'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_B,'InterfaceIndex',_C,_D)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cLpbkdt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,95))
if mibBuilder.loadTexts:h3cLpbkdt.setRevisions(('2014-07-26 15:18','2009-03-30 17:41','2008-09-27 15:04'))
class H3cLpbkdtActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('block',2),('nolearning',3),('shutdown',4)))
_H3cLpbkdtNotifications_ObjectIdentity=ObjectIdentity
h3cLpbkdtNotifications=_H3cLpbkdtNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,95,1))
_H3cLpbkdtTrapPrefix_ObjectIdentity=ObjectIdentity
h3cLpbkdtTrapPrefix=_H3cLpbkdtTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,95,1,0))
_H3cLpbkdtObjects_ObjectIdentity=ObjectIdentity
h3cLpbkdtObjects=_H3cLpbkdtObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,95,2))
_H3cLpbkdtVlanID_Type=VlanId
_H3cLpbkdtVlanID_Object=MibScalar
h3cLpbkdtVlanID=_H3cLpbkdtVlanID_Object((1,3,6,1,4,1,2011,10,2,95,2,1),_H3cLpbkdtVlanID_Type())
h3cLpbkdtVlanID.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cLpbkdtVlanID.setStatus(_A)
class _H3cLpbkdtVlanEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_H3cLpbkdtVlanEnable_Type.__name__=_G
_H3cLpbkdtVlanEnable_Object=MibScalar
h3cLpbkdtVlanEnable=_H3cLpbkdtVlanEnable_Object((1,3,6,1,4,1,2011,10,2,95,2,2),_H3cLpbkdtVlanEnable_Type())
h3cLpbkdtVlanEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cLpbkdtVlanEnable.setStatus(_A)
class _H3cLpbkdtAction_Type(H3cLpbkdtActionType):defaultValue=1
_H3cLpbkdtAction_Type.__name__=_J
_H3cLpbkdtAction_Object=MibScalar
h3cLpbkdtAction=_H3cLpbkdtAction_Object((1,3,6,1,4,1,2011,10,2,95,2,3),_H3cLpbkdtAction_Type())
h3cLpbkdtAction.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cLpbkdtAction.setStatus(_A)
class _H3cLpbkdtIntervalTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_H3cLpbkdtIntervalTime_Type.__name__=_I
_H3cLpbkdtIntervalTime_Object=MibScalar
h3cLpbkdtIntervalTime=_H3cLpbkdtIntervalTime_Object((1,3,6,1,4,1,2011,10,2,95,2,4),_H3cLpbkdtIntervalTime_Type())
h3cLpbkdtIntervalTime.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cLpbkdtIntervalTime.setStatus(_A)
_H3cLpbkdtPortTable_Object=MibTable
h3cLpbkdtPortTable=_H3cLpbkdtPortTable_Object((1,3,6,1,4,1,2011,10,2,95,2,5))
if mibBuilder.loadTexts:h3cLpbkdtPortTable.setStatus(_A)
_H3cLpbkdtPortEntry_Object=MibTableRow
h3cLpbkdtPortEntry=_H3cLpbkdtPortEntry_Object((1,3,6,1,4,1,2011,10,2,95,2,5,1))
h3cLpbkdtPortEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:h3cLpbkdtPortEntry.setStatus(_A)
_H3cLpbkdtPortIfIndex_Type=InterfaceIndex
_H3cLpbkdtPortIfIndex_Object=MibTableColumn
h3cLpbkdtPortIfIndex=_H3cLpbkdtPortIfIndex_Object((1,3,6,1,4,1,2011,10,2,95,2,5,1,1),_H3cLpbkdtPortIfIndex_Type())
h3cLpbkdtPortIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cLpbkdtPortIfIndex.setStatus(_A)
class _H3cLpbkdtPortVlanEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_H3cLpbkdtPortVlanEnable_Type.__name__=_G
_H3cLpbkdtPortVlanEnable_Object=MibTableColumn
h3cLpbkdtPortVlanEnable=_H3cLpbkdtPortVlanEnable_Object((1,3,6,1,4,1,2011,10,2,95,2,5,1,2),_H3cLpbkdtPortVlanEnable_Type())
h3cLpbkdtPortVlanEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cLpbkdtPortVlanEnable.setStatus(_A)
_H3cLpbkdtPortAction_Type=H3cLpbkdtActionType
_H3cLpbkdtPortAction_Object=MibTableColumn
h3cLpbkdtPortAction=_H3cLpbkdtPortAction_Object((1,3,6,1,4,1,2011,10,2,95,2,5,1,3),_H3cLpbkdtPortAction_Type())
h3cLpbkdtPortAction.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cLpbkdtPortAction.setStatus(_A)
_H3cLpbkdtPortLoopbacked_Type=TruthValue
_H3cLpbkdtPortLoopbacked_Object=MibTableColumn
h3cLpbkdtPortLoopbacked=_H3cLpbkdtPortLoopbacked_Object((1,3,6,1,4,1,2011,10,2,95,2,5,1,4),_H3cLpbkdtPortLoopbacked_Type())
h3cLpbkdtPortLoopbacked.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cLpbkdtPortLoopbacked.setStatus(_A)
h3cLpbkdtTrapLoopbacked=NotificationType((1,3,6,1,4,1,2011,10,2,95,1,0,1))
h3cLpbkdtTrapLoopbacked.setObjects(*((_B,_D),(_B,_C)))
if mibBuilder.loadTexts:h3cLpbkdtTrapLoopbacked.setStatus(_A)
h3cLpbkdtTrapRecovered=NotificationType((1,3,6,1,4,1,2011,10,2,95,1,0,2))
h3cLpbkdtTrapRecovered.setObjects(*((_B,_D),(_B,_C)))
if mibBuilder.loadTexts:h3cLpbkdtTrapRecovered.setStatus(_A)
h3cLpbkdtTrapPerVlanLoopbacked=NotificationType((1,3,6,1,4,1,2011,10,2,95,1,0,3))
h3cLpbkdtTrapPerVlanLoopbacked.setObjects(*((_B,_D),(_B,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cLpbkdtTrapPerVlanLoopbacked.setStatus(_A)
h3cLpbkdtTrapPerVlanRecovered=NotificationType((1,3,6,1,4,1,2011,10,2,95,1,0,4))
h3cLpbkdtTrapPerVlanRecovered.setObjects(*((_B,_D),(_B,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cLpbkdtTrapPerVlanRecovered.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_J:H3cLpbkdtActionType,'h3cLpbkdt':h3cLpbkdt,'h3cLpbkdtNotifications':h3cLpbkdtNotifications,'h3cLpbkdtTrapPrefix':h3cLpbkdtTrapPrefix,'h3cLpbkdtTrapLoopbacked':h3cLpbkdtTrapLoopbacked,'h3cLpbkdtTrapRecovered':h3cLpbkdtTrapRecovered,'h3cLpbkdtTrapPerVlanLoopbacked':h3cLpbkdtTrapPerVlanLoopbacked,'h3cLpbkdtTrapPerVlanRecovered':h3cLpbkdtTrapPerVlanRecovered,'h3cLpbkdtObjects':h3cLpbkdtObjects,_H:h3cLpbkdtVlanID,'h3cLpbkdtVlanEnable':h3cLpbkdtVlanEnable,'h3cLpbkdtAction':h3cLpbkdtAction,'h3cLpbkdtIntervalTime':h3cLpbkdtIntervalTime,'h3cLpbkdtPortTable':h3cLpbkdtPortTable,'h3cLpbkdtPortEntry':h3cLpbkdtPortEntry,_K:h3cLpbkdtPortIfIndex,'h3cLpbkdtPortVlanEnable':h3cLpbkdtPortVlanEnable,'h3cLpbkdtPortAction':h3cLpbkdtPortAction,'h3cLpbkdtPortLoopbacked':h3cLpbkdtPortLoopbacked})