_R='ds0BondingGroup'
_Q='ds0BundleConfigGroup'
_P='dsx0BundleRowStatus'
_O='dsx0BundleCircuitIdentifier'
_N='dsx0BundleIfIndex'
_M='dsx0BundleNextIndex'
_L='dsx0BondRowStatus'
_K='dsx0BondStatus'
_J='dsx0BondMode'
_I='dsx0BundleIndex'
_H='read-only'
_G='DisplayString'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='Integer32'
_B='DS0BUNDLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TestAndIncr')
ds0Bundle=ModuleIdentity((1,3,6,1,2,1,10,82))
if mibBuilder.loadTexts:ds0Bundle.setRevisions(('1998-05-24 20:10',))
_Dsx0BondingTable_Object=MibTable
dsx0BondingTable=_Dsx0BondingTable_Object((1,3,6,1,2,1,10,82,1))
if mibBuilder.loadTexts:dsx0BondingTable.setStatus(_A)
_Dsx0BondingEntry_Object=MibTableRow
dsx0BondingEntry=_Dsx0BondingEntry_Object((1,3,6,1,2,1,10,82,1,1))
dsx0BondingEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dsx0BondingEntry.setStatus(_A)
class _Dsx0BondMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('other',2),('mode0',3),('mode1',4),('mode2',5),('mode3',6)))
_Dsx0BondMode_Type.__name__=_C
_Dsx0BondMode_Object=MibTableColumn
dsx0BondMode=_Dsx0BondMode_Object((1,3,6,1,2,1,10,82,1,1,1),_Dsx0BondMode_Type())
dsx0BondMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0BondMode.setStatus(_A)
class _Dsx0BondStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('callSetup',2),('dataTransfer',3)))
_Dsx0BondStatus_Type.__name__=_C
_Dsx0BondStatus_Object=MibTableColumn
dsx0BondStatus=_Dsx0BondStatus_Object((1,3,6,1,2,1,10,82,1,1,2),_Dsx0BondStatus_Type())
dsx0BondStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:dsx0BondStatus.setStatus(_A)
_Dsx0BondRowStatus_Type=RowStatus
_Dsx0BondRowStatus_Object=MibTableColumn
dsx0BondRowStatus=_Dsx0BondRowStatus_Object((1,3,6,1,2,1,10,82,1,1,3),_Dsx0BondRowStatus_Type())
dsx0BondRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0BondRowStatus.setStatus(_A)
_Dsx0BundleNextIndex_Type=TestAndIncr
_Dsx0BundleNextIndex_Object=MibScalar
dsx0BundleNextIndex=_Dsx0BundleNextIndex_Object((1,3,6,1,2,1,10,82,2),_Dsx0BundleNextIndex_Type())
dsx0BundleNextIndex.setMaxAccess('read-write')
if mibBuilder.loadTexts:dsx0BundleNextIndex.setStatus(_A)
_Dsx0BundleTable_Object=MibTable
dsx0BundleTable=_Dsx0BundleTable_Object((1,3,6,1,2,1,10,82,3))
if mibBuilder.loadTexts:dsx0BundleTable.setStatus(_A)
_Dsx0BundleEntry_Object=MibTableRow
dsx0BundleEntry=_Dsx0BundleEntry_Object((1,3,6,1,2,1,10,82,3,1))
dsx0BundleEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:dsx0BundleEntry.setStatus(_A)
class _Dsx0BundleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx0BundleIndex_Type.__name__=_C
_Dsx0BundleIndex_Object=MibTableColumn
dsx0BundleIndex=_Dsx0BundleIndex_Object((1,3,6,1,2,1,10,82,3,1,1),_Dsx0BundleIndex_Type())
dsx0BundleIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dsx0BundleIndex.setStatus(_A)
_Dsx0BundleIfIndex_Type=InterfaceIndex
_Dsx0BundleIfIndex_Object=MibTableColumn
dsx0BundleIfIndex=_Dsx0BundleIfIndex_Object((1,3,6,1,2,1,10,82,3,1,2),_Dsx0BundleIfIndex_Type())
dsx0BundleIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dsx0BundleIfIndex.setStatus(_A)
class _Dsx0BundleCircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Dsx0BundleCircuitIdentifier_Type.__name__=_G
_Dsx0BundleCircuitIdentifier_Object=MibTableColumn
dsx0BundleCircuitIdentifier=_Dsx0BundleCircuitIdentifier_Object((1,3,6,1,2,1,10,82,3,1,3),_Dsx0BundleCircuitIdentifier_Type())
dsx0BundleCircuitIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0BundleCircuitIdentifier.setStatus(_A)
_Dsx0BundleRowStatus_Type=RowStatus
_Dsx0BundleRowStatus_Object=MibTableColumn
dsx0BundleRowStatus=_Dsx0BundleRowStatus_Object((1,3,6,1,2,1,10,82,3,1,4),_Dsx0BundleRowStatus_Type())
dsx0BundleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0BundleRowStatus.setStatus(_A)
_Ds0BundleConformance_ObjectIdentity=ObjectIdentity
ds0BundleConformance=_Ds0BundleConformance_ObjectIdentity((1,3,6,1,2,1,10,82,4))
_Ds0BundleGroups_ObjectIdentity=ObjectIdentity
ds0BundleGroups=_Ds0BundleGroups_ObjectIdentity((1,3,6,1,2,1,10,82,4,1))
_Ds0BundleCompliances_ObjectIdentity=ObjectIdentity
ds0BundleCompliances=_Ds0BundleCompliances_ObjectIdentity((1,3,6,1,2,1,10,82,4,2))
ds0BondingGroup=ObjectGroup((1,3,6,1,2,1,10,82,4,1,1))
ds0BondingGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ds0BondingGroup.setStatus(_A)
ds0BundleConfigGroup=ObjectGroup((1,3,6,1,2,1,10,82,4,1,2))
ds0BundleConfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ds0BundleConfigGroup.setStatus(_A)
ds0BundleCompliance=ModuleCompliance((1,3,6,1,2,1,10,82,4,2,1))
ds0BundleCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ds0BundleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ds0Bundle':ds0Bundle,'dsx0BondingTable':dsx0BondingTable,'dsx0BondingEntry':dsx0BondingEntry,_J:dsx0BondMode,_K:dsx0BondStatus,_L:dsx0BondRowStatus,_M:dsx0BundleNextIndex,'dsx0BundleTable':dsx0BundleTable,'dsx0BundleEntry':dsx0BundleEntry,_I:dsx0BundleIndex,_N:dsx0BundleIfIndex,_O:dsx0BundleCircuitIdentifier,_P:dsx0BundleRowStatus,'ds0BundleConformance':ds0BundleConformance,'ds0BundleGroups':ds0BundleGroups,_R:ds0BondingGroup,_Q:ds0BundleConfigGroup,'ds0BundleCompliances':ds0BundleCompliances,'ds0BundleCompliance':ds0BundleCompliance})