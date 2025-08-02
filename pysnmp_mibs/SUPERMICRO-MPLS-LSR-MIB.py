_I='fsMplsOutSegmentEntry'
_H='fsMplsInSegmentEntry'
_G='read-create'
_F='reverse'
_E='forward'
_D='TruthValue'
_C='SUPERMICRO-MPLS-LSR-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mplsInSegmentEntry,mplsOutSegmentEntry=mibBuilder.importSymbols('MPLS-LSR-STD-MIB','mplsInSegmentEntry','mplsOutSegmentEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
fsMplsLsrMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,13,13))
if mibBuilder.loadTexts:fsMplsLsrMIB.setRevisions(('2012-09-05 00:00',))
_FsMplsLsrNotifications_ObjectIdentity=ObjectIdentity
fsMplsLsrNotifications=_FsMplsLsrNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,13,0))
_FsMplsLsrObjects_ObjectIdentity=ObjectIdentity
fsMplsLsrObjects=_FsMplsLsrObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,13,1))
_FsMplsLsrScalarObjects_ObjectIdentity=ObjectIdentity
fsMplsLsrScalarObjects=_FsMplsLsrScalarObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,13,1,1))
class _FsMplsLsrRfc6428CompatibleCodePoint_Type(TruthValue):defaultValue=2
_FsMplsLsrRfc6428CompatibleCodePoint_Type.__name__=_D
_FsMplsLsrRfc6428CompatibleCodePoint_Object=MibScalar
fsMplsLsrRfc6428CompatibleCodePoint=_FsMplsLsrRfc6428CompatibleCodePoint_Object((1,3,6,1,4,1,10876,101,1,13,13,1,1,1),_FsMplsLsrRfc6428CompatibleCodePoint_Type())
fsMplsLsrRfc6428CompatibleCodePoint.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsMplsLsrRfc6428CompatibleCodePoint.setStatus(_A)
_FsMplsInSegmentTable_Object=MibTable
fsMplsInSegmentTable=_FsMplsInSegmentTable_Object((1,3,6,1,4,1,10876,101,1,13,13,1,2))
if mibBuilder.loadTexts:fsMplsInSegmentTable.setStatus(_A)
_FsMplsInSegmentEntry_Object=MibTableRow
fsMplsInSegmentEntry=_FsMplsInSegmentEntry_Object((1,3,6,1,4,1,10876,101,1,13,13,1,2,1))
if mibBuilder.loadTexts:fsMplsInSegmentEntry.setStatus(_A)
class _FsMplsInSegmentDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMplsInSegmentDirection_Type.__name__=_B
_FsMplsInSegmentDirection_Object=MibTableColumn
fsMplsInSegmentDirection=_FsMplsInSegmentDirection_Object((1,3,6,1,4,1,10876,101,1,13,13,1,2,1,1),_FsMplsInSegmentDirection_Type())
fsMplsInSegmentDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMplsInSegmentDirection.setStatus(_A)
_FsMplsOutSegmentTable_Object=MibTable
fsMplsOutSegmentTable=_FsMplsOutSegmentTable_Object((1,3,6,1,4,1,10876,101,1,13,13,1,3))
if mibBuilder.loadTexts:fsMplsOutSegmentTable.setStatus(_A)
_FsMplsOutSegmentEntry_Object=MibTableRow
fsMplsOutSegmentEntry=_FsMplsOutSegmentEntry_Object((1,3,6,1,4,1,10876,101,1,13,13,1,3,1))
if mibBuilder.loadTexts:fsMplsOutSegmentEntry.setStatus(_A)
class _FsMplsOutSegmentDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMplsOutSegmentDirection_Type.__name__=_B
_FsMplsOutSegmentDirection_Object=MibTableColumn
fsMplsOutSegmentDirection=_FsMplsOutSegmentDirection_Object((1,3,6,1,4,1,10876,101,1,13,13,1,3,1,1),_FsMplsOutSegmentDirection_Type())
fsMplsOutSegmentDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMplsOutSegmentDirection.setStatus(_A)
_FsMplsLsrConformance_ObjectIdentity=ObjectIdentity
fsMplsLsrConformance=_FsMplsLsrConformance_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,13,2))
mplsInSegmentEntry.registerAugmentions((_C,_H))
fsMplsInSegmentEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions((_C,_I))
fsMplsOutSegmentEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'fsMplsLsrMIB':fsMplsLsrMIB,'fsMplsLsrNotifications':fsMplsLsrNotifications,'fsMplsLsrObjects':fsMplsLsrObjects,'fsMplsLsrScalarObjects':fsMplsLsrScalarObjects,'fsMplsLsrRfc6428CompatibleCodePoint':fsMplsLsrRfc6428CompatibleCodePoint,'fsMplsInSegmentTable':fsMplsInSegmentTable,_H:fsMplsInSegmentEntry,'fsMplsInSegmentDirection':fsMplsInSegmentDirection,'fsMplsOutSegmentTable':fsMplsOutSegmentTable,_I:fsMplsOutSegmentEntry,'fsMplsOutSegmentDirection':fsMplsOutSegmentDirection,'fsMplsLsrConformance':fsMplsLsrConformance})