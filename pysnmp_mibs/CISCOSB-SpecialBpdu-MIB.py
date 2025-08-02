_G='rlSpecialBpduProtId'
_F='rlSpecialBpduEncap'
_E='OctetString'
_D='not-accessible'
_C='rlSpecialBpduMacAddr'
_B='CISCOSB-SpecialBpdu-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlSpecialBpdu=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,144))
if mibBuilder.loadTexts:rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))
class EncapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('ethernet-v2',2),('llc',3),('llc-snap',4)))
class Action(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('discard',2)))
class HwAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forward',1),('drop',2),('trap',3)))
_RlSpecialBpduTable_Object=MibTable
rlSpecialBpduTable=_RlSpecialBpduTable_Object((1,3,6,1,4,1,9,6,1,101,144,1))
if mibBuilder.loadTexts:rlSpecialBpduTable.setStatus(_A)
_RlSpecialBpduEntry_Object=MibTableRow
rlSpecialBpduEntry=_RlSpecialBpduEntry_Object((1,3,6,1,4,1,9,6,1,101,144,1,1))
rlSpecialBpduEntry.setIndexNames((0,_B,_C),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:rlSpecialBpduEntry.setStatus(_A)
_RlSpecialBpduMacAddr_Type=MacAddress
_RlSpecialBpduMacAddr_Object=MibTableColumn
rlSpecialBpduMacAddr=_RlSpecialBpduMacAddr_Object((1,3,6,1,4,1,9,6,1,101,144,1,1,1),_RlSpecialBpduMacAddr_Type())
rlSpecialBpduMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSpecialBpduMacAddr.setStatus(_A)
_RlSpecialBpduEncap_Type=EncapType
_RlSpecialBpduEncap_Object=MibTableColumn
rlSpecialBpduEncap=_RlSpecialBpduEncap_Object((1,3,6,1,4,1,9,6,1,101,144,1,1,2),_RlSpecialBpduEncap_Type())
rlSpecialBpduEncap.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSpecialBpduEncap.setStatus(_A)
class _RlSpecialBpduProtId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_RlSpecialBpduProtId_Type.__name__=_E
_RlSpecialBpduProtId_Object=MibTableColumn
rlSpecialBpduProtId=_RlSpecialBpduProtId_Object((1,3,6,1,4,1,9,6,1,101,144,1,1,3),_RlSpecialBpduProtId_Type())
rlSpecialBpduProtId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSpecialBpduProtId.setStatus(_A)
_RlSpecialBpduAction_Type=Action
_RlSpecialBpduAction_Object=MibTableColumn
rlSpecialBpduAction=_RlSpecialBpduAction_Object((1,3,6,1,4,1,9,6,1,101,144,1,1,4),_RlSpecialBpduAction_Type())
rlSpecialBpduAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlSpecialBpduAction.setStatus(_A)
_RlSpecialBpduRowStatus_Type=RowStatus
_RlSpecialBpduRowStatus_Object=MibTableColumn
rlSpecialBpduRowStatus=_RlSpecialBpduRowStatus_Object((1,3,6,1,4,1,9,6,1,101,144,1,1,5),_RlSpecialBpduRowStatus_Type())
rlSpecialBpduRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rlSpecialBpduRowStatus.setStatus(_A)
_RlSpecialBpduHwTable_Object=MibTable
rlSpecialBpduHwTable=_RlSpecialBpduHwTable_Object((1,3,6,1,4,1,9,6,1,101,144,2))
if mibBuilder.loadTexts:rlSpecialBpduHwTable.setStatus(_A)
_RlSpecialBpduHwEntry_Object=MibTableRow
rlSpecialBpduHwEntry=_RlSpecialBpduHwEntry_Object((1,3,6,1,4,1,9,6,1,101,144,2,1))
rlSpecialBpduHwEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rlSpecialBpduHwEntry.setStatus(_A)
_RlSpecialBpduHwAction_Type=HwAction
_RlSpecialBpduHwAction_Object=MibTableColumn
rlSpecialBpduHwAction=_RlSpecialBpduHwAction_Object((1,3,6,1,4,1,9,6,1,101,144,2,1,2),_RlSpecialBpduHwAction_Type())
rlSpecialBpduHwAction.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlSpecialBpduHwAction.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EncapType':EncapType,'Action':Action,'HwAction':HwAction,'rlSpecialBpdu':rlSpecialBpdu,'rlSpecialBpduTable':rlSpecialBpduTable,'rlSpecialBpduEntry':rlSpecialBpduEntry,_C:rlSpecialBpduMacAddr,_F:rlSpecialBpduEncap,_G:rlSpecialBpduProtId,'rlSpecialBpduAction':rlSpecialBpduAction,'rlSpecialBpduRowStatus':rlSpecialBpduRowStatus,'rlSpecialBpduHwTable':rlSpecialBpduHwTable,'rlSpecialBpduHwEntry':rlSpecialBpduHwEntry,'rlSpecialBpduHwAction':rlSpecialBpduHwAction})