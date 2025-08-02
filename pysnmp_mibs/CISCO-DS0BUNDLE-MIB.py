_H='ds0BundleConfigGroup'
_G='dsx0BundleRowStatus'
_F='dsx0BundleIfIndex'
_E='dsx0BundleNextIndex'
_D='dsx0BundleIndex'
_C='Integer32'
_B='CISCO-DS0BUNDLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr')
ds0Bundle=ModuleIdentity((1,3,6,1,4,1,9,10,32))
_Dsx0BundleNextIndex_Type=TestAndIncr
_Dsx0BundleNextIndex_Object=MibScalar
dsx0BundleNextIndex=_Dsx0BundleNextIndex_Object((1,3,6,1,4,1,9,10,32,2),_Dsx0BundleNextIndex_Type())
dsx0BundleNextIndex.setMaxAccess('read-write')
if mibBuilder.loadTexts:dsx0BundleNextIndex.setStatus(_A)
_Dsx0BundleTable_Object=MibTable
dsx0BundleTable=_Dsx0BundleTable_Object((1,3,6,1,4,1,9,10,32,3))
if mibBuilder.loadTexts:dsx0BundleTable.setStatus(_A)
_Dsx0BundleEntry_Object=MibTableRow
dsx0BundleEntry=_Dsx0BundleEntry_Object((1,3,6,1,4,1,9,10,32,3,1))
dsx0BundleEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:dsx0BundleEntry.setStatus(_A)
class _Dsx0BundleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx0BundleIndex_Type.__name__=_C
_Dsx0BundleIndex_Object=MibTableColumn
dsx0BundleIndex=_Dsx0BundleIndex_Object((1,3,6,1,4,1,9,10,32,3,1,1),_Dsx0BundleIndex_Type())
dsx0BundleIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dsx0BundleIndex.setStatus(_A)
_Dsx0BundleIfIndex_Type=InterfaceIndex
_Dsx0BundleIfIndex_Object=MibTableColumn
dsx0BundleIfIndex=_Dsx0BundleIfIndex_Object((1,3,6,1,4,1,9,10,32,3,1,2),_Dsx0BundleIfIndex_Type())
dsx0BundleIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:dsx0BundleIfIndex.setStatus(_A)
_Dsx0BundleRowStatus_Type=RowStatus
_Dsx0BundleRowStatus_Object=MibTableColumn
dsx0BundleRowStatus=_Dsx0BundleRowStatus_Object((1,3,6,1,4,1,9,10,32,3,1,3),_Dsx0BundleRowStatus_Type())
dsx0BundleRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:dsx0BundleRowStatus.setStatus(_A)
_Ds0BundleConformance_ObjectIdentity=ObjectIdentity
ds0BundleConformance=_Ds0BundleConformance_ObjectIdentity((1,3,6,1,4,1,9,10,32,4))
_Ds0BundleGroups_ObjectIdentity=ObjectIdentity
ds0BundleGroups=_Ds0BundleGroups_ObjectIdentity((1,3,6,1,4,1,9,10,32,4,1))
_Ds0BundleCompliances_ObjectIdentity=ObjectIdentity
ds0BundleCompliances=_Ds0BundleCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,32,4,2))
ds0BundleConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,32,4,1,2))
ds0BundleConfigGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ds0BundleConfigGroup.setStatus(_A)
ds0BundleCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,32,4,2,1))
ds0BundleCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ds0BundleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ds0Bundle':ds0Bundle,_E:dsx0BundleNextIndex,'dsx0BundleTable':dsx0BundleTable,'dsx0BundleEntry':dsx0BundleEntry,_D:dsx0BundleIndex,_F:dsx0BundleIfIndex,_G:dsx0BundleRowStatus,'ds0BundleConformance':ds0BundleConformance,'ds0BundleGroups':ds0BundleGroups,_H:ds0BundleConfigGroup,'ds0BundleCompliances':ds0BundleCompliances,'ds0BundleCompliance':ds0BundleCompliance})