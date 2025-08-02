_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsrmon2=ModuleIdentity((1,3,6,1,4,1,29601,2,19))
if mibBuilder.loadTexts:fsrmon2.setRevisions(('2012-09-05 00:00',))
_FsRmon2Trace_Type=Unsigned32
_FsRmon2Trace_Object=MibScalar
fsRmon2Trace=_FsRmon2Trace_Object((1,3,6,1,4,1,29601,2,19,1),_FsRmon2Trace_Type())
fsRmon2Trace.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmon2Trace.setStatus(_C)
class _FsRmon2AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsRmon2AdminStatus_Type.__name__=_A
_FsRmon2AdminStatus_Object=MibScalar
fsRmon2AdminStatus=_FsRmon2AdminStatus_Object((1,3,6,1,4,1,29601,2,19,2),_FsRmon2AdminStatus_Type())
fsRmon2AdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmon2AdminStatus.setStatus(_C)
mibBuilder.exportSymbols('ARICENT-RMON2-MIB',**{'fsrmon2':fsrmon2,'fsRmon2Trace':fsRmon2Trace,'fsRmon2AdminStatus':fsRmon2AdminStatus})