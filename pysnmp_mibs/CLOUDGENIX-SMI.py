if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cloudgenix=ModuleIdentity((1,3,6,1,4,1,50114))
if mibBuilder.loadTexts:cloudgenix.setRevisions(('2017-06-19 18:00',))
_CgxObjects_ObjectIdentity=ObjectIdentity
cgxObjects=_CgxObjects_ObjectIdentity((1,3,6,1,4,1,50114,1))
_CgxConformance_ObjectIdentity=ObjectIdentity
cgxConformance=_CgxConformance_ObjectIdentity((1,3,6,1,4,1,50114,2))
_CgxCompliances_ObjectIdentity=ObjectIdentity
cgxCompliances=_CgxCompliances_ObjectIdentity((1,3,6,1,4,1,50114,2,1))
_CgxGroups_ObjectIdentity=ObjectIdentity
cgxGroups=_CgxGroups_ObjectIdentity((1,3,6,1,4,1,50114,2,2))
_CgxMgmt_ObjectIdentity=ObjectIdentity
cgxMgmt=_CgxMgmt_ObjectIdentity((1,3,6,1,4,1,50114,10))
cloudgenixCompliance=ModuleCompliance((1,3,6,1,4,1,50114,2,1,1))
if mibBuilder.loadTexts:cloudgenixCompliance.setStatus('current')
mibBuilder.exportSymbols('CLOUDGENIX-SMI',**{'cloudgenix':cloudgenix,'cgxObjects':cgxObjects,'cgxConformance':cgxConformance,'cgxCompliances':cgxCompliances,'cloudgenixCompliance':cloudgenixCompliance,'cgxGroups':cgxGroups,'cgxMgmt':cgxMgmt})