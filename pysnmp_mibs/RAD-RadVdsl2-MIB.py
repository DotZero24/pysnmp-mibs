_O='vdsl2LinkDownReason'
_N='vdsl2SideIdx'
_M='alarmEventReason'
_L='alarmEventLogSourceName'
_K='alarmEventLogSeverity'
_J='alarmEventLogDescription'
_I='alarmEventLogDateAndTime'
_H='alarmEventLogAlarmOrEventId'
_G='ifIndex'
_F='ifAlias'
_E='RAD-RadVdsl2-MIB'
_D='Integer32'
_C='IF-MIB'
_B='current'
_A='RAD-GEN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifAlias,ifIndex=mibBuilder.importSymbols(_C,_F,_G)
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_A,_H,_I,_J,_K,_L,_M)
diverseIfWanGen,=mibBuilder.importSymbols('RAD-SMI-MIB','diverseIfWanGen')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vdsl2If=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,19))
_Vdsl2Events_ObjectIdentity=ObjectIdentity
vdsl2Events=_Vdsl2Events_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,19,0))
_Vdsl2Objects_ObjectIdentity=ObjectIdentity
vdsl2Objects=_Vdsl2Objects_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,19,1))
_Vdsl2IfNotifVarbindTable_Object=MibTable
vdsl2IfNotifVarbindTable=_Vdsl2IfNotifVarbindTable_Object((1,3,6,1,4,1,164,3,1,6,19,1,2))
if mibBuilder.loadTexts:vdsl2IfNotifVarbindTable.setStatus(_B)
_Vdsl2IfNotifVarbindEntry_Object=MibTableRow
vdsl2IfNotifVarbindEntry=_Vdsl2IfNotifVarbindEntry_Object((1,3,6,1,4,1,164,3,1,6,19,1,2,1))
vdsl2IfNotifVarbindEntry.setIndexNames((0,_C,_G),(0,_E,_N))
if mibBuilder.loadTexts:vdsl2IfNotifVarbindEntry.setStatus(_B)
class _Vdsl2SideIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('nearEnd',2),('farEnd',3)))
_Vdsl2SideIdx_Type.__name__=_D
_Vdsl2SideIdx_Object=MibTableColumn
vdsl2SideIdx=_Vdsl2SideIdx_Object((1,3,6,1,4,1,164,3,1,6,19,1,2,1,1),_Vdsl2SideIdx_Type())
vdsl2SideIdx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vdsl2SideIdx.setStatus(_B)
class _Vdsl2LinkDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lossOfFraming',1),('lossOfSignal',2),('lossOfPower',3),('initFailure',4)))
_Vdsl2LinkDownReason_Type.__name__=_D
_Vdsl2LinkDownReason_Object=MibTableColumn
vdsl2LinkDownReason=_Vdsl2LinkDownReason_Object((1,3,6,1,4,1,164,3,1,6,19,1,2,1,2),_Vdsl2LinkDownReason_Type())
vdsl2LinkDownReason.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:vdsl2LinkDownReason.setStatus(_B)
vdsl2LinkDown=NotificationType((1,3,6,1,4,1,164,3,1,6,19,0,1))
vdsl2LinkDown.setObjects(*((_A,_L),(_A,_H),(_A,_J),(_A,_K),(_A,_I),(_A,_M),(_C,_F),(_E,_O)))
if mibBuilder.loadTexts:vdsl2LinkDown.setStatus(_B)
mibBuilder.exportSymbols(_E,**{'vdsl2If':vdsl2If,'vdsl2Events':vdsl2Events,'vdsl2LinkDown':vdsl2LinkDown,'vdsl2Objects':vdsl2Objects,'vdsl2IfNotifVarbindTable':vdsl2IfNotifVarbindTable,'vdsl2IfNotifVarbindEntry':vdsl2IfNotifVarbindEntry,_N:vdsl2SideIdx,_O:vdsl2LinkDownReason})