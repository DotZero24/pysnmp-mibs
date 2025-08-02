_L='hpicfReloadDateTime'
_K='hpicfReloadControl'
_J='hpicfReloadAt'
_I='hpicfReloadAfter'
_H='hpicfReloadState'
_G='Integer32'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='hpicfReloadGroup'
_C='read-write'
_B='HP-ICF-RELOAD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
hpicfBasic,=mibBuilder.importSymbols('HP-ICF-BASIC','hpicfBasic')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
hpicfReloadMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,1,4,20))
if mibBuilder.loadTexts:hpicfReloadMIB.setRevisions(('2009-12-03 00:00','2009-10-01 00:00'))
class ReloadControl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reloadSlotNone',1),('fullPowerCycleReload',2)))
_HpicfReloadObjects_ObjectIdentity=ObjectIdentity
hpicfReloadObjects=_HpicfReloadObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,4,20,1))
class _HpicfReloadState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notScheduled',1),('reloadAfter',2),('reloadAt',3)))
_HpicfReloadState_Type.__name__=_G
_HpicfReloadState_Object=MibScalar
hpicfReloadState=_HpicfReloadState_Object((1,3,6,1,4,1,11,2,14,11,1,4,20,1,1),_HpicfReloadState_Type())
hpicfReloadState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfReloadState.setStatus(_A)
_HpicfReloadAfter_Type=Integer32
_HpicfReloadAfter_Object=MibScalar
hpicfReloadAfter=_HpicfReloadAfter_Object((1,3,6,1,4,1,11,2,14,11,1,4,20,1,2),_HpicfReloadAfter_Type())
hpicfReloadAfter.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfReloadAfter.setStatus(_A)
_HpicfReloadAt_Type=DateAndTime
_HpicfReloadAt_Object=MibScalar
hpicfReloadAt=_HpicfReloadAt_Object((1,3,6,1,4,1,11,2,14,11,1,4,20,1,3),_HpicfReloadAt_Type())
hpicfReloadAt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfReloadAt.setStatus(_A)
_HpicfEntityReload_ObjectIdentity=ObjectIdentity
hpicfEntityReload=_HpicfEntityReload_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,4,20,2))
_HpicfReloadTable_Object=MibTable
hpicfReloadTable=_HpicfReloadTable_Object((1,3,6,1,4,1,11,2,14,11,1,4,20,2,2))
if mibBuilder.loadTexts:hpicfReloadTable.setStatus(_A)
_HpicfReloadEntry_Object=MibTableRow
hpicfReloadEntry=_HpicfReloadEntry_Object((1,3,6,1,4,1,11,2,14,11,1,4,20,2,2,1))
hpicfReloadEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfReloadEntry.setStatus(_A)
_HpicfReloadControl_Type=ReloadControl
_HpicfReloadControl_Object=MibTableColumn
hpicfReloadControl=_HpicfReloadControl_Object((1,3,6,1,4,1,11,2,14,11,1,4,20,2,2,1,1),_HpicfReloadControl_Type())
hpicfReloadControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfReloadControl.setStatus(_A)
_HpicfReloadDateTime_Type=DateAndTime
_HpicfReloadDateTime_Object=MibTableColumn
hpicfReloadDateTime=_HpicfReloadDateTime_Object((1,3,6,1,4,1,11,2,14,11,1,4,20,2,2,1,2),_HpicfReloadDateTime_Type())
hpicfReloadDateTime.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpicfReloadDateTime.setStatus(_A)
_HpicfReloadConformance_ObjectIdentity=ObjectIdentity
hpicfReloadConformance=_HpicfReloadConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,4,20,3))
_HpicfReloadGroups_ObjectIdentity=ObjectIdentity
hpicfReloadGroups=_HpicfReloadGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,4,20,3,1))
_HpicfReloadCompliances_ObjectIdentity=ObjectIdentity
hpicfReloadCompliances=_HpicfReloadCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,4,20,3,2))
hpicfReloadGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,4,20,3,1,1))
hpicfReloadGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpicfReloadGroup.setStatus(_A)
hpicfReloadFullCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,4,20,3,2,1))
hpicfReloadFullCompliance1.setObjects((_B,_D))
if mibBuilder.loadTexts:hpicfReloadFullCompliance1.setStatus(_A)
hpicfReloadFullCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,4,20,3,2,2))
hpicfReloadFullCompliance2.setObjects((_B,_D))
if mibBuilder.loadTexts:hpicfReloadFullCompliance2.setStatus(_A)
hpicfReloadReadOnlyCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,4,20,3,2,3))
hpicfReloadReadOnlyCompliance1.setObjects((_B,_D))
if mibBuilder.loadTexts:hpicfReloadReadOnlyCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ReloadControl':ReloadControl,'hpicfReloadMIB':hpicfReloadMIB,'hpicfReloadObjects':hpicfReloadObjects,_H:hpicfReloadState,_I:hpicfReloadAfter,_J:hpicfReloadAt,'hpicfEntityReload':hpicfEntityReload,'hpicfReloadTable':hpicfReloadTable,'hpicfReloadEntry':hpicfReloadEntry,_K:hpicfReloadControl,_L:hpicfReloadDateTime,'hpicfReloadConformance':hpicfReloadConformance,'hpicfReloadGroups':hpicfReloadGroups,_D:hpicfReloadGroup,'hpicfReloadCompliances':hpicfReloadCompliances,'hpicfReloadFullCompliance1':hpicfReloadFullCompliance1,'hpicfReloadFullCompliance2':hpicfReloadFullCompliance2,'hpicfReloadReadOnlyCompliance1':hpicfReloadReadOnlyCompliance1})