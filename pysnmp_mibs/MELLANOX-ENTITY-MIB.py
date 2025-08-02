_D='read-only'
_C='entPhysicalIndex'
_B='ENTITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_B,_C)
mellanoxEntity,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxEntity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxEntityMib=ModuleIdentity((1,3,6,1,4,1,33049,5,1))
if mibBuilder.loadTexts:mellanoxEntityMib.setRevisions(('2013-06-30 00:00',))
_MellanoxPhysicalEntityTable_Object=MibTable
mellanoxPhysicalEntityTable=_MellanoxPhysicalEntityTable_Object((1,3,6,1,4,1,33049,5,1,1))
if mibBuilder.loadTexts:mellanoxPhysicalEntityTable.setStatus(_A)
_MellanoxPhysicalEntityEntry_Object=MibTableRow
mellanoxPhysicalEntityEntry=_MellanoxPhysicalEntityEntry_Object((1,3,6,1,4,1,33049,5,1,1,1))
mellanoxPhysicalEntityEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:mellanoxPhysicalEntityEntry.setStatus(_A)
_MellanoxPhysicalEntityGUID_Type=OctetString
_MellanoxPhysicalEntityGUID_Object=MibTableColumn
mellanoxPhysicalEntityGUID=_MellanoxPhysicalEntityGUID_Object((1,3,6,1,4,1,33049,5,1,1,1,1),_MellanoxPhysicalEntityGUID_Type())
mellanoxPhysicalEntityGUID.setMaxAccess(_D)
if mibBuilder.loadTexts:mellanoxPhysicalEntityGUID.setStatus(_A)
_MellanoxPhysicalEntityAsicRev_Type=Integer32
_MellanoxPhysicalEntityAsicRev_Object=MibTableColumn
mellanoxPhysicalEntityAsicRev=_MellanoxPhysicalEntityAsicRev_Object((1,3,6,1,4,1,33049,5,1,1,1,2),_MellanoxPhysicalEntityAsicRev_Type())
mellanoxPhysicalEntityAsicRev.setMaxAccess(_D)
if mibBuilder.loadTexts:mellanoxPhysicalEntityAsicRev.setStatus(_A)
mibBuilder.exportSymbols('MELLANOX-ENTITY-MIB',**{'mellanoxEntityMib':mellanoxEntityMib,'mellanoxPhysicalEntityTable':mellanoxPhysicalEntityTable,'mellanoxPhysicalEntityEntry':mellanoxPhysicalEntityEntry,'mellanoxPhysicalEntityGUID':mellanoxPhysicalEntityGUID,'mellanoxPhysicalEntityAsicRev':mellanoxPhysicalEntityAsicRev})