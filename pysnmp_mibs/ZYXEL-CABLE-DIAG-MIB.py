_L='unsupported'
_K='unknown'
_J='crosstalk'
_I='openshort'
_H='short'
_G='open'
_F='ok'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelCableDiagnostic=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,112))
_ZyxelCableDiagnosticSetup_ObjectIdentity=ObjectIdentity
zyxelCableDiagnosticSetup=_ZyxelCableDiagnosticSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,112,1))
_ZyxelCableDiagnosticPortTable_Object=MibTable
zyxelCableDiagnosticPortTable=_ZyxelCableDiagnosticPortTable_Object((1,3,6,1,4,1,890,1,15,3,112,1,1))
if mibBuilder.loadTexts:zyxelCableDiagnosticPortTable.setStatus(_A)
_ZyxelCableDiagnosticPortEntry_Object=MibTableRow
zyxelCableDiagnosticPortEntry=_ZyxelCableDiagnosticPortEntry_Object((1,3,6,1,4,1,890,1,15,3,112,1,1,1))
zyxelCableDiagnosticPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelCableDiagnosticPortEntry.setStatus(_A)
class _ZyCableDiagnosticPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('start',1),('clear',2)))
_ZyCableDiagnosticPortAction_Type.__name__=_C
_ZyCableDiagnosticPortAction_Object=MibTableColumn
zyCableDiagnosticPortAction=_ZyCableDiagnosticPortAction_Object((1,3,6,1,4,1,890,1,15,3,112,1,1,1,1),_ZyCableDiagnosticPortAction_Type())
zyCableDiagnosticPortAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:zyCableDiagnosticPortAction.setStatus(_A)
_ZyxelCableDiagnosticStatus_ObjectIdentity=ObjectIdentity
zyxelCableDiagnosticStatus=_ZyxelCableDiagnosticStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,112,2))
_ZyxelCableDiagnosticPortStatusTable_Object=MibTable
zyxelCableDiagnosticPortStatusTable=_ZyxelCableDiagnosticPortStatusTable_Object((1,3,6,1,4,1,890,1,15,3,112,2,1))
if mibBuilder.loadTexts:zyxelCableDiagnosticPortStatusTable.setStatus(_A)
_ZyxelCableDiagnosticPortStatusEntry_Object=MibTableRow
zyxelCableDiagnosticPortStatusEntry=_ZyxelCableDiagnosticPortStatusEntry_Object((1,3,6,1,4,1,890,1,15,3,112,2,1,1))
zyxelCableDiagnosticPortStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelCableDiagnosticPortStatusEntry.setStatus(_A)
class _ZyCableDiagnosticPortStatusActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('success',1),('failure',2),('processing',3)))
_ZyCableDiagnosticPortStatusActionStatus_Type.__name__=_C
_ZyCableDiagnosticPortStatusActionStatus_Object=MibTableColumn
zyCableDiagnosticPortStatusActionStatus=_ZyCableDiagnosticPortStatusActionStatus_Object((1,3,6,1,4,1,890,1,15,3,112,2,1,1,1),_ZyCableDiagnosticPortStatusActionStatus_Type())
zyCableDiagnosticPortStatusActionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortStatusActionStatus.setStatus(_A)
_ZyxelCableDiagnosticPortResultTable_Object=MibTable
zyxelCableDiagnosticPortResultTable=_ZyxelCableDiagnosticPortResultTable_Object((1,3,6,1,4,1,890,1,15,3,112,2,2))
if mibBuilder.loadTexts:zyxelCableDiagnosticPortResultTable.setStatus(_A)
_ZyxelCableDiagnosticPortResultEntry_Object=MibTableRow
zyxelCableDiagnosticPortResultEntry=_ZyxelCableDiagnosticPortResultEntry_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1))
zyxelCableDiagnosticPortResultEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelCableDiagnosticPortResultEntry.setStatus(_A)
class _ZyCableDiagnosticPortResultPairAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7)))
_ZyCableDiagnosticPortResultPairAStatus_Type.__name__=_C
_ZyCableDiagnosticPortResultPairAStatus_Object=MibTableColumn
zyCableDiagnosticPortResultPairAStatus=_ZyCableDiagnosticPortResultPairAStatus_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,1),_ZyCableDiagnosticPortResultPairAStatus_Type())
zyCableDiagnosticPortResultPairAStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairAStatus.setStatus(_A)
class _ZyCableDiagnosticPortResultPairBStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7)))
_ZyCableDiagnosticPortResultPairBStatus_Type.__name__=_C
_ZyCableDiagnosticPortResultPairBStatus_Object=MibTableColumn
zyCableDiagnosticPortResultPairBStatus=_ZyCableDiagnosticPortResultPairBStatus_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,2),_ZyCableDiagnosticPortResultPairBStatus_Type())
zyCableDiagnosticPortResultPairBStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairBStatus.setStatus(_A)
class _ZyCableDiagnosticPortResultPairCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7)))
_ZyCableDiagnosticPortResultPairCStatus_Type.__name__=_C
_ZyCableDiagnosticPortResultPairCStatus_Object=MibTableColumn
zyCableDiagnosticPortResultPairCStatus=_ZyCableDiagnosticPortResultPairCStatus_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,3),_ZyCableDiagnosticPortResultPairCStatus_Type())
zyCableDiagnosticPortResultPairCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairCStatus.setStatus(_A)
class _ZyCableDiagnosticPortResultPairDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7)))
_ZyCableDiagnosticPortResultPairDStatus_Type.__name__=_C
_ZyCableDiagnosticPortResultPairDStatus_Object=MibTableColumn
zyCableDiagnosticPortResultPairDStatus=_ZyCableDiagnosticPortResultPairDStatus_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,4),_ZyCableDiagnosticPortResultPairDStatus_Type())
zyCableDiagnosticPortResultPairDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairDStatus.setStatus(_A)
_ZyCableDiagnosticPortResultPairALength_Type=Integer32
_ZyCableDiagnosticPortResultPairALength_Object=MibTableColumn
zyCableDiagnosticPortResultPairALength=_ZyCableDiagnosticPortResultPairALength_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,5),_ZyCableDiagnosticPortResultPairALength_Type())
zyCableDiagnosticPortResultPairALength.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairALength.setStatus(_A)
_ZyCableDiagnosticPortResultPairBLength_Type=Integer32
_ZyCableDiagnosticPortResultPairBLength_Object=MibTableColumn
zyCableDiagnosticPortResultPairBLength=_ZyCableDiagnosticPortResultPairBLength_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,6),_ZyCableDiagnosticPortResultPairBLength_Type())
zyCableDiagnosticPortResultPairBLength.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairBLength.setStatus(_A)
_ZyCableDiagnosticPortResultPairCLength_Type=Integer32
_ZyCableDiagnosticPortResultPairCLength_Object=MibTableColumn
zyCableDiagnosticPortResultPairCLength=_ZyCableDiagnosticPortResultPairCLength_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,7),_ZyCableDiagnosticPortResultPairCLength_Type())
zyCableDiagnosticPortResultPairCLength.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairCLength.setStatus(_A)
_ZyCableDiagnosticPortResultPairDLength_Type=Integer32
_ZyCableDiagnosticPortResultPairDLength_Object=MibTableColumn
zyCableDiagnosticPortResultPairDLength=_ZyCableDiagnosticPortResultPairDLength_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,8),_ZyCableDiagnosticPortResultPairDLength_Type())
zyCableDiagnosticPortResultPairDLength.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairDLength.setStatus(_A)
_ZyCableDiagnosticPortResultPairADistanceToFault_Type=Integer32
_ZyCableDiagnosticPortResultPairADistanceToFault_Object=MibTableColumn
zyCableDiagnosticPortResultPairADistanceToFault=_ZyCableDiagnosticPortResultPairADistanceToFault_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,9),_ZyCableDiagnosticPortResultPairADistanceToFault_Type())
zyCableDiagnosticPortResultPairADistanceToFault.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairADistanceToFault.setStatus(_A)
_ZyCableDiagnosticPortResultPairBDistanceToFault_Type=Integer32
_ZyCableDiagnosticPortResultPairBDistanceToFault_Object=MibTableColumn
zyCableDiagnosticPortResultPairBDistanceToFault=_ZyCableDiagnosticPortResultPairBDistanceToFault_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,10),_ZyCableDiagnosticPortResultPairBDistanceToFault_Type())
zyCableDiagnosticPortResultPairBDistanceToFault.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairBDistanceToFault.setStatus(_A)
_ZyCableDiagnosticPortResultPairCDistanceToFault_Type=Integer32
_ZyCableDiagnosticPortResultPairCDistanceToFault_Object=MibTableColumn
zyCableDiagnosticPortResultPairCDistanceToFault=_ZyCableDiagnosticPortResultPairCDistanceToFault_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,11),_ZyCableDiagnosticPortResultPairCDistanceToFault_Type())
zyCableDiagnosticPortResultPairCDistanceToFault.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairCDistanceToFault.setStatus(_A)
_ZyCableDiagnosticPortResultPairDDistanceToFault_Type=Integer32
_ZyCableDiagnosticPortResultPairDDistanceToFault_Object=MibTableColumn
zyCableDiagnosticPortResultPairDDistanceToFault=_ZyCableDiagnosticPortResultPairDDistanceToFault_Object((1,3,6,1,4,1,890,1,15,3,112,2,2,1,12),_ZyCableDiagnosticPortResultPairDDistanceToFault_Type())
zyCableDiagnosticPortResultPairDDistanceToFault.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCableDiagnosticPortResultPairDDistanceToFault.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-CABLE-DIAG-MIB',**{'zyxelCableDiagnostic':zyxelCableDiagnostic,'zyxelCableDiagnosticSetup':zyxelCableDiagnosticSetup,'zyxelCableDiagnosticPortTable':zyxelCableDiagnosticPortTable,'zyxelCableDiagnosticPortEntry':zyxelCableDiagnosticPortEntry,'zyCableDiagnosticPortAction':zyCableDiagnosticPortAction,'zyxelCableDiagnosticStatus':zyxelCableDiagnosticStatus,'zyxelCableDiagnosticPortStatusTable':zyxelCableDiagnosticPortStatusTable,'zyxelCableDiagnosticPortStatusEntry':zyxelCableDiagnosticPortStatusEntry,'zyCableDiagnosticPortStatusActionStatus':zyCableDiagnosticPortStatusActionStatus,'zyxelCableDiagnosticPortResultTable':zyxelCableDiagnosticPortResultTable,'zyxelCableDiagnosticPortResultEntry':zyxelCableDiagnosticPortResultEntry,'zyCableDiagnosticPortResultPairAStatus':zyCableDiagnosticPortResultPairAStatus,'zyCableDiagnosticPortResultPairBStatus':zyCableDiagnosticPortResultPairBStatus,'zyCableDiagnosticPortResultPairCStatus':zyCableDiagnosticPortResultPairCStatus,'zyCableDiagnosticPortResultPairDStatus':zyCableDiagnosticPortResultPairDStatus,'zyCableDiagnosticPortResultPairALength':zyCableDiagnosticPortResultPairALength,'zyCableDiagnosticPortResultPairBLength':zyCableDiagnosticPortResultPairBLength,'zyCableDiagnosticPortResultPairCLength':zyCableDiagnosticPortResultPairCLength,'zyCableDiagnosticPortResultPairDLength':zyCableDiagnosticPortResultPairDLength,'zyCableDiagnosticPortResultPairADistanceToFault':zyCableDiagnosticPortResultPairADistanceToFault,'zyCableDiagnosticPortResultPairBDistanceToFault':zyCableDiagnosticPortResultPairBDistanceToFault,'zyCableDiagnosticPortResultPairCDistanceToFault':zyCableDiagnosticPortResultPairCDistanceToFault,'zyCableDiagnosticPortResultPairDDistanceToFault':zyCableDiagnosticPortResultPairDDistanceToFault})