_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsSec=ModuleIdentity((1,3,6,1,4,1,29601,2,64))
if mibBuilder.loadTexts:fsSec.setRevisions(('2012-09-05 00:00',))
_FsSecSystem_ObjectIdentity=ObjectIdentity
fsSecSystem=_FsSecSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,64,1))
class _FsSecDebugOption_Type(Integer32):defaultValue=0
_FsSecDebugOption_Type.__name__=_A
_FsSecDebugOption_Object=MibScalar
fsSecDebugOption=_FsSecDebugOption_Object((1,3,6,1,4,1,29601,2,64,1,1),_FsSecDebugOption_Type())
fsSecDebugOption.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsSecDebugOption.setStatus('current')
mibBuilder.exportSymbols('ARICENT-Sec-MIB',**{'fsSec':fsSec,'fsSecSystem':fsSecSystem,'fsSecDebugOption':fsSecDebugOption})