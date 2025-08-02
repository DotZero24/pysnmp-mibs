_O='tnEquipDiagStatusGroup'
_N='tnEquipDiagStatusResult'
_M='tnEquipDiagStatusDescr'
_L='read-only'
_K='tnEquipDiagUnit'
_J='tnEquipDiagId'
_I='tnEquipDiagPort'
_H='tnSlotIndex'
_G='TROPIC-SLOT-MIB'
_F='tnShelfIndex'
_E='TROPIC-SHELF-MIB'
_D='Integer32'
_C='not-accessible'
_B='TROPIC-DIAGNOSTIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnDiagnosticMIB,tnSystemModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnDiagnosticMIB','tnSystemModules')
tnShelfIndex,=mibBuilder.importSymbols(_E,_F)
tnSlotIndex,=mibBuilder.importSymbols(_G,_H)
tnDiagnosticMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,1,4))
if mibBuilder.loadTexts:tnDiagnosticMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2010-07-15 12:00'))
class TnEquipDiagDescription(SnmpAdminString):status=_A;subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_TnDiagnosticConf_ObjectIdentity=ObjectIdentity
tnDiagnosticConf=_TnDiagnosticConf_ObjectIdentity((1,3,6,1,4,1,7483,2,1,4,1))
_TnDiagnosticGroups_ObjectIdentity=ObjectIdentity
tnDiagnosticGroups=_TnDiagnosticGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,1,4,1,1))
_TnDiagnosticCompliances_ObjectIdentity=ObjectIdentity
tnDiagnosticCompliances=_TnDiagnosticCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,1,4,1,2))
_TnDiagnosticObjs_ObjectIdentity=ObjectIdentity
tnDiagnosticObjs=_TnDiagnosticObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,1,4,2))
_TnEquipmentDiagnosticStatusTable_Object=MibTable
tnEquipmentDiagnosticStatusTable=_TnEquipmentDiagnosticStatusTable_Object((1,3,6,1,4,1,7483,2,1,4,2,1))
if mibBuilder.loadTexts:tnEquipmentDiagnosticStatusTable.setStatus(_A)
_TnEquipDiagStatusEntry_Object=MibTableRow
tnEquipDiagStatusEntry=_TnEquipDiagStatusEntry_Object((1,3,6,1,4,1,7483,2,1,4,2,1,1))
tnEquipDiagStatusEntry.setIndexNames((0,_E,_F),(0,_G,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:tnEquipDiagStatusEntry.setStatus(_A)
_TnEquipDiagPort_Type=Unsigned32
_TnEquipDiagPort_Object=MibTableColumn
tnEquipDiagPort=_TnEquipDiagPort_Object((1,3,6,1,4,1,7483,2,1,4,2,1,1,1),_TnEquipDiagPort_Type())
tnEquipDiagPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEquipDiagPort.setStatus(_A)
_TnEquipDiagId_Type=Unsigned32
_TnEquipDiagId_Object=MibTableColumn
tnEquipDiagId=_TnEquipDiagId_Object((1,3,6,1,4,1,7483,2,1,4,2,1,1,2),_TnEquipDiagId_Type())
tnEquipDiagId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEquipDiagId.setStatus(_A)
_TnEquipDiagUnit_Type=Unsigned32
_TnEquipDiagUnit_Object=MibTableColumn
tnEquipDiagUnit=_TnEquipDiagUnit_Object((1,3,6,1,4,1,7483,2,1,4,2,1,1,3),_TnEquipDiagUnit_Type())
tnEquipDiagUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEquipDiagUnit.setStatus(_A)
_TnEquipDiagStatusDescr_Type=TnEquipDiagDescription
_TnEquipDiagStatusDescr_Object=MibTableColumn
tnEquipDiagStatusDescr=_TnEquipDiagStatusDescr_Object((1,3,6,1,4,1,7483,2,1,4,2,1,1,4),_TnEquipDiagStatusDescr_Type())
tnEquipDiagStatusDescr.setMaxAccess(_L)
if mibBuilder.loadTexts:tnEquipDiagStatusDescr.setStatus(_A)
class _TnEquipDiagStatusResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('failed',1),('passed',2),('willNotRun',3),('notExecuted',4)))
_TnEquipDiagStatusResult_Type.__name__=_D
_TnEquipDiagStatusResult_Object=MibTableColumn
tnEquipDiagStatusResult=_TnEquipDiagStatusResult_Object((1,3,6,1,4,1,7483,2,1,4,2,1,1,5),_TnEquipDiagStatusResult_Type())
tnEquipDiagStatusResult.setMaxAccess(_L)
if mibBuilder.loadTexts:tnEquipDiagStatusResult.setStatus(_A)
tnEquipDiagStatusGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,4,1,1,1))
tnEquipDiagStatusGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:tnEquipDiagStatusGroup.setStatus(_A)
tnDiagnosticCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,1,4,1,2,1))
tnDiagnosticCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:tnDiagnosticCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TnEquipDiagDescription':TnEquipDiagDescription,'tnDiagnosticMibModule':tnDiagnosticMibModule,'tnDiagnosticConf':tnDiagnosticConf,'tnDiagnosticGroups':tnDiagnosticGroups,_O:tnEquipDiagStatusGroup,'tnDiagnosticCompliances':tnDiagnosticCompliances,'tnDiagnosticCompliance':tnDiagnosticCompliance,'tnDiagnosticObjs':tnDiagnosticObjs,'tnEquipmentDiagnosticStatusTable':tnEquipmentDiagnosticStatusTable,'tnEquipDiagStatusEntry':tnEquipDiagStatusEntry,_I:tnEquipDiagPort,_J:tnEquipDiagId,_K:tnEquipDiagUnit,_M:tnEquipDiagStatusDescr,_N:tnEquipDiagStatusResult})