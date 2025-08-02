_F='pxmStaticMulticastFdbGroup'
_E='pxmStaticMulticastFdbMacAddress'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB'
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
pxmStaticMulticastFdbMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,67))
_PxmStaticMulticastFdbTable_Object=MibTable
pxmStaticMulticastFdbTable=_PxmStaticMulticastFdbTable_Object((1,3,6,1,4,1,21296,2,2,2,2,67,1))
if mibBuilder.loadTexts:pxmStaticMulticastFdbTable.setStatus(_A)
_PxmStaticMulticastFdbEntry_Object=MibTableRow
pxmStaticMulticastFdbEntry=_PxmStaticMulticastFdbEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,67,1,1))
pxmStaticMulticastFdbEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:pxmStaticMulticastFdbEntry.setStatus(_A)
_PxmStaticMulticastFdbMacAddress_Type=DisplayString
_PxmStaticMulticastFdbMacAddress_Object=MibTableColumn
pxmStaticMulticastFdbMacAddress=_PxmStaticMulticastFdbMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,67,1,1,1),_PxmStaticMulticastFdbMacAddress_Type())
pxmStaticMulticastFdbMacAddress.setMaxAccess('read-only')
if mibBuilder.loadTexts:pxmStaticMulticastFdbMacAddress.setStatus(_A)
_PxmStaticMulticastFdbConformance_ObjectIdentity=ObjectIdentity
pxmStaticMulticastFdbConformance=_PxmStaticMulticastFdbConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,67,3))
_PxmStaticMulticastFdbCompliances_ObjectIdentity=ObjectIdentity
pxmStaticMulticastFdbCompliances=_PxmStaticMulticastFdbCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,67,3,1))
_PxmStaticMulticastFdbGroups_ObjectIdentity=ObjectIdentity
pxmStaticMulticastFdbGroups=_PxmStaticMulticastFdbGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,67,3,2))
pxmStaticMulticastFdbGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,67,3,2,1))
pxmStaticMulticastFdbGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:pxmStaticMulticastFdbGroup.setStatus(_A)
pxmStaticMulticastFdbCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,67,3,1,1))
pxmStaticMulticastFdbCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:pxmStaticMulticastFdbCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmStaticMulticastFdbMIB':pxmStaticMulticastFdbMIB,'pxmStaticMulticastFdbTable':pxmStaticMulticastFdbTable,'pxmStaticMulticastFdbEntry':pxmStaticMulticastFdbEntry,_E:pxmStaticMulticastFdbMacAddress,'pxmStaticMulticastFdbConformance':pxmStaticMulticastFdbConformance,'pxmStaticMulticastFdbCompliances':pxmStaticMulticastFdbCompliances,'pxmStaticMulticastFdbCompliance':pxmStaticMulticastFdbCompliance,'pxmStaticMulticastFdbGroups':pxmStaticMulticastFdbGroups,_F:pxmStaticMulticastFdbGroup})