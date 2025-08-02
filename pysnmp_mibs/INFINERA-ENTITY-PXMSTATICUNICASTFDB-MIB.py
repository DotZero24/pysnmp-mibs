_F='pxmStaticUnicastFdbGroup'
_E='pxmStaticUnicastFdbMacAddress'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmStaticUnicastFdbMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,65))
_PxmStaticUnicastFdbTable_Object=MibTable
pxmStaticUnicastFdbTable=_PxmStaticUnicastFdbTable_Object((1,3,6,1,4,1,21296,2,2,2,2,65,1))
if mibBuilder.loadTexts:pxmStaticUnicastFdbTable.setStatus(_A)
_PxmStaticUnicastFdbEntry_Object=MibTableRow
pxmStaticUnicastFdbEntry=_PxmStaticUnicastFdbEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,65,1,1))
pxmStaticUnicastFdbEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:pxmStaticUnicastFdbEntry.setStatus(_A)
_PxmStaticUnicastFdbMacAddress_Type=DisplayString
_PxmStaticUnicastFdbMacAddress_Object=MibTableColumn
pxmStaticUnicastFdbMacAddress=_PxmStaticUnicastFdbMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,65,1,1,1),_PxmStaticUnicastFdbMacAddress_Type())
pxmStaticUnicastFdbMacAddress.setMaxAccess('read-only')
if mibBuilder.loadTexts:pxmStaticUnicastFdbMacAddress.setStatus(_A)
_PxmStaticUnicastFdbConformance_ObjectIdentity=ObjectIdentity
pxmStaticUnicastFdbConformance=_PxmStaticUnicastFdbConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,65,3))
_PxmStaticUnicastFdbCompliances_ObjectIdentity=ObjectIdentity
pxmStaticUnicastFdbCompliances=_PxmStaticUnicastFdbCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,65,3,1))
_PxmStaticUnicastFdbGroups_ObjectIdentity=ObjectIdentity
pxmStaticUnicastFdbGroups=_PxmStaticUnicastFdbGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,65,3,2))
pxmStaticUnicastFdbGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,65,3,2,1))
pxmStaticUnicastFdbGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:pxmStaticUnicastFdbGroup.setStatus(_A)
pxmStaticUnicastFdbCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,65,3,1,1))
pxmStaticUnicastFdbCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:pxmStaticUnicastFdbCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmStaticUnicastFdbMIB':pxmStaticUnicastFdbMIB,'pxmStaticUnicastFdbTable':pxmStaticUnicastFdbTable,'pxmStaticUnicastFdbEntry':pxmStaticUnicastFdbEntry,_E:pxmStaticUnicastFdbMacAddress,'pxmStaticUnicastFdbConformance':pxmStaticUnicastFdbConformance,'pxmStaticUnicastFdbCompliances':pxmStaticUnicastFdbCompliances,'pxmStaticUnicastFdbCompliance':pxmStaticUnicastFdbCompliance,'pxmStaticUnicastFdbGroups':pxmStaticUnicastFdbGroups,_F:pxmStaticUnicastFdbGroup})