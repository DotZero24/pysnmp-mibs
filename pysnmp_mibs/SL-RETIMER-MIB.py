_E='slRetimerCurrentIndex'
_D='slRetimerLineIndex'
_C='read-only'
_B='SL-RETIMER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
slRetimer=ModuleIdentity((1,3,6,1,4,1,4515,1,1,14))
_SlRetimerConfig_ObjectIdentity=ObjectIdentity
slRetimerConfig=_SlRetimerConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,14,1))
_SlRetimerConfigTable_Object=MibTable
slRetimerConfigTable=_SlRetimerConfigTable_Object((1,3,6,1,4,1,4515,1,1,14,1,1))
if mibBuilder.loadTexts:slRetimerConfigTable.setStatus(_A)
_SlRetimerConfigEntry_Object=MibTableRow
slRetimerConfigEntry=_SlRetimerConfigEntry_Object((1,3,6,1,4,1,4515,1,1,14,1,1,1))
slRetimerConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:slRetimerConfigEntry.setStatus(_A)
_SlRetimerLineIndex_Type=InterfaceIndex
_SlRetimerLineIndex_Object=MibTableColumn
slRetimerLineIndex=_SlRetimerLineIndex_Object((1,3,6,1,4,1,4515,1,1,14,1,1,1,1),_SlRetimerLineIndex_Type())
slRetimerLineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slRetimerLineIndex.setStatus(_A)
_SlRetimerResetPmCounters_Type=Integer32
_SlRetimerResetPmCounters_Object=MibTableColumn
slRetimerResetPmCounters=_SlRetimerResetPmCounters_Object((1,3,6,1,4,1,4515,1,1,14,1,1,1,2),_SlRetimerResetPmCounters_Type())
slRetimerResetPmCounters.setMaxAccess('read-write')
if mibBuilder.loadTexts:slRetimerResetPmCounters.setStatus(_A)
_SlRetimerStat_ObjectIdentity=ObjectIdentity
slRetimerStat=_SlRetimerStat_ObjectIdentity((1,3,6,1,4,1,4515,1,1,14,2))
_SlRetimerPm_ObjectIdentity=ObjectIdentity
slRetimerPm=_SlRetimerPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,14,3))
_SlRetimerCurrentTable_Object=MibTable
slRetimerCurrentTable=_SlRetimerCurrentTable_Object((1,3,6,1,4,1,4515,1,1,14,3,1))
if mibBuilder.loadTexts:slRetimerCurrentTable.setStatus(_A)
_SlRetimerCurrentEntry_Object=MibTableRow
slRetimerCurrentEntry=_SlRetimerCurrentEntry_Object((1,3,6,1,4,1,4515,1,1,14,3,1,1))
slRetimerCurrentEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:slRetimerCurrentEntry.setStatus(_A)
_SlRetimerCurrentIndex_Type=InterfaceIndex
_SlRetimerCurrentIndex_Object=MibTableColumn
slRetimerCurrentIndex=_SlRetimerCurrentIndex_Object((1,3,6,1,4,1,4515,1,1,14,3,1,1,1),_SlRetimerCurrentIndex_Type())
slRetimerCurrentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slRetimerCurrentIndex.setStatus(_A)
_SlRetimerCurrentRxRllES_Type=Integer32
_SlRetimerCurrentRxRllES_Object=MibTableColumn
slRetimerCurrentRxRllES=_SlRetimerCurrentRxRllES_Object((1,3,6,1,4,1,4515,1,1,14,3,1,1,2),_SlRetimerCurrentRxRllES_Type())
slRetimerCurrentRxRllES.setMaxAccess(_C)
if mibBuilder.loadTexts:slRetimerCurrentRxRllES.setStatus(_A)
_SlRetimerCurrentRxK285ES_Type=Integer32
_SlRetimerCurrentRxK285ES_Object=MibTableColumn
slRetimerCurrentRxK285ES=_SlRetimerCurrentRxK285ES_Object((1,3,6,1,4,1,4515,1,1,14,3,1,1,3),_SlRetimerCurrentRxK285ES_Type())
slRetimerCurrentRxK285ES.setMaxAccess(_C)
if mibBuilder.loadTexts:slRetimerCurrentRxK285ES.setStatus(_A)
_SlRetimerTraps_ObjectIdentity=ObjectIdentity
slRetimerTraps=_SlRetimerTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,14,7))
slRetimerStatusChange=NotificationType((1,3,6,1,4,1,4515,1,1,14,7,1))
slRetimerStatusChange.setObjects((_B,_D))
if mibBuilder.loadTexts:slRetimerStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'slRetimer':slRetimer,'slRetimerConfig':slRetimerConfig,'slRetimerConfigTable':slRetimerConfigTable,'slRetimerConfigEntry':slRetimerConfigEntry,_D:slRetimerLineIndex,'slRetimerResetPmCounters':slRetimerResetPmCounters,'slRetimerStat':slRetimerStat,'slRetimerPm':slRetimerPm,'slRetimerCurrentTable':slRetimerCurrentTable,'slRetimerCurrentEntry':slRetimerCurrentEntry,_E:slRetimerCurrentIndex,'slRetimerCurrentRxRllES':slRetimerCurrentRxRllES,'slRetimerCurrentRxK285ES':slRetimerCurrentRxK285ES,'slRetimerTraps':slRetimerTraps,'slRetimerStatusChange':slRetimerStatusChange})