_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pcube=ModuleIdentity((1,3,6,1,4,1,5655))
if mibBuilder.loadTexts:pcube.setRevisions(('2002-01-14 20:00',))
_PcubeProducts_ObjectIdentity=ObjectIdentity
pcubeProducts=_PcubeProducts_ObjectIdentity((1,3,6,1,4,1,5655,1))
if mibBuilder.loadTexts:pcubeProducts.setStatus(_A)
_PcubeModules_ObjectIdentity=ObjectIdentity
pcubeModules=_PcubeModules_ObjectIdentity((1,3,6,1,4,1,5655,2))
if mibBuilder.loadTexts:pcubeModules.setStatus(_A)
_PcubeMgmt_ObjectIdentity=ObjectIdentity
pcubeMgmt=_PcubeMgmt_ObjectIdentity((1,3,6,1,4,1,5655,3))
if mibBuilder.loadTexts:pcubeMgmt.setStatus(_A)
_PcubeWorkgroup_ObjectIdentity=ObjectIdentity
pcubeWorkgroup=_PcubeWorkgroup_ObjectIdentity((1,3,6,1,4,1,5655,4))
if mibBuilder.loadTexts:pcubeWorkgroup.setStatus(_A)
mibBuilder.exportSymbols('PCUBE-SMI',**{'pcube':pcube,'pcubeProducts':pcubeProducts,'pcubeModules':pcubeModules,'pcubeMgmt':pcubeMgmt,'pcubeWorkgroup':pcubeWorkgroup})