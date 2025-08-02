if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ligowave=ModuleIdentity((1,3,6,1,4,1,32750))
if mibBuilder.loadTexts:ligowave.setRevisions(('2008-09-05 00:00',))
_LigoProducts_ObjectIdentity=ObjectIdentity
ligoProducts=_LigoProducts_ObjectIdentity((1,3,6,1,4,1,32750,1))
_LigoAdmin_ObjectIdentity=ObjectIdentity
ligoAdmin=_LigoAdmin_ObjectIdentity((1,3,6,1,4,1,32750,2))
_LigoMgmt_ObjectIdentity=ObjectIdentity
ligoMgmt=_LigoMgmt_ObjectIdentity((1,3,6,1,4,1,32750,3))
_LigoExperimental_ObjectIdentity=ObjectIdentity
ligoExperimental=_LigoExperimental_ObjectIdentity((1,3,6,1,4,1,32750,7))
mibBuilder.exportSymbols('LIGOWAVE-MIB',**{'ligowave':ligowave,'ligoProducts':ligoProducts,'ligoAdmin':ligoAdmin,'ligoMgmt':ligoMgmt,'ligoExperimental':ligoExperimental})