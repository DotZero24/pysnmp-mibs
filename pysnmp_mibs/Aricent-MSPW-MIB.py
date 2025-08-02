_G='not-accessible'
_F='fsMsPwIndex2'
_E='fsMsPwIndex1'
_D='read-write'
_C='Unsigned32'
_B='Aricent-MSPW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PwIndexType,PwOperStatusTC=mibBuilder.importSymbols('PW-TC-STD-MIB','PwIndexType','PwOperStatusTC')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsMspwMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,57))
if mibBuilder.loadTexts:fsMspwMIB.setRevisions(('2012-09-05 00:00',))
_FsMsPwConfigObjects_ObjectIdentity=ObjectIdentity
fsMsPwConfigObjects=_FsMsPwConfigObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,57,1))
class _FsMsPwMaxEntries_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32766))
_FsMsPwMaxEntries_Type.__name__=_C
_FsMsPwMaxEntries_Object=MibScalar
fsMsPwMaxEntries=_FsMsPwMaxEntries_Object((1,3,6,1,4,1,29601,2,57,1,1),_FsMsPwMaxEntries_Type())
fsMsPwMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMsPwMaxEntries.setStatus(_A)
_FsMsPwConfigTable_Object=MibTable
fsMsPwConfigTable=_FsMsPwConfigTable_Object((1,3,6,1,4,1,29601,2,57,1,2))
if mibBuilder.loadTexts:fsMsPwConfigTable.setStatus(_A)
_FsMsPwConfigEntry_Object=MibTableRow
fsMsPwConfigEntry=_FsMsPwConfigEntry_Object((1,3,6,1,4,1,29601,2,57,1,2,1))
fsMsPwConfigEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:fsMsPwConfigEntry.setStatus(_A)
_FsMsPwIndex1_Type=PwIndexType
_FsMsPwIndex1_Object=MibTableColumn
fsMsPwIndex1=_FsMsPwIndex1_Object((1,3,6,1,4,1,29601,2,57,1,2,1,1),_FsMsPwIndex1_Type())
fsMsPwIndex1.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsPwIndex1.setStatus(_A)
_FsMsPwIndex2_Type=PwIndexType
_FsMsPwIndex2_Object=MibTableColumn
fsMsPwIndex2=_FsMsPwIndex2_Object((1,3,6,1,4,1,29601,2,57,1,2,1,2),_FsMsPwIndex2_Type())
fsMsPwIndex2.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsPwIndex2.setStatus(_A)
_FsMsPwOperStatus_Type=PwOperStatusTC
_FsMsPwOperStatus_Object=MibTableColumn
fsMsPwOperStatus=_FsMsPwOperStatus_Object((1,3,6,1,4,1,29601,2,57,1,2,1,3),_FsMsPwOperStatus_Type())
fsMsPwOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsMsPwOperStatus.setStatus(_A)
_FsMsPwRowStatus_Type=RowStatus
_FsMsPwRowStatus_Object=MibTableColumn
fsMsPwRowStatus=_FsMsPwRowStatus_Object((1,3,6,1,4,1,29601,2,57,1,2,1,4),_FsMsPwRowStatus_Type())
fsMsPwRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMsPwRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsMspwMIB':fsMspwMIB,'fsMsPwConfigObjects':fsMsPwConfigObjects,'fsMsPwMaxEntries':fsMsPwMaxEntries,'fsMsPwConfigTable':fsMsPwConfigTable,'fsMsPwConfigEntry':fsMsPwConfigEntry,_E:fsMsPwIndex1,_F:fsMsPwIndex2,'fsMsPwOperStatus':fsMsPwOperStatus,'fsMsPwRowStatus':fsMsPwRowStatus})