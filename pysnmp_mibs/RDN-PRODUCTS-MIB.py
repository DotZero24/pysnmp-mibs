if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rdnDefinitions,=mibBuilder.importSymbols('RDN-DEFINITIONS-MIB','rdnDefinitions')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdnProducts=ModuleIdentity((1,3,6,1,4,1,4981,4,1))
if mibBuilder.loadTexts:rdnProducts.setRevisions(('2008-08-08 00:00','2003-11-05 00:00','2003-04-29 00:00','2001-04-17 00:00'))
_RdnProductsUnknown_ObjectIdentity=ObjectIdentity
rdnProductsUnknown=_RdnProductsUnknown_ObjectIdentity((1,3,6,1,4,1,4981,4,1,0))
_RdnProductsBSR64000_ObjectIdentity=ObjectIdentity
rdnProductsBSR64000=_RdnProductsBSR64000_ObjectIdentity((1,3,6,1,4,1,4981,4,1,1))
_RdnProductsBSR1000B_ObjectIdentity=ObjectIdentity
rdnProductsBSR1000B=_RdnProductsBSR1000B_ObjectIdentity((1,3,6,1,4,1,4981,4,1,2))
_RdnProductsBSR1000R_ObjectIdentity=ObjectIdentity
rdnProductsBSR1000R=_RdnProductsBSR1000R_ObjectIdentity((1,3,6,1,4,1,4981,4,1,3))
_RdnProductsOSR2000_ObjectIdentity=ObjectIdentity
rdnProductsOSR2000=_RdnProductsOSR2000_ObjectIdentity((1,3,6,1,4,1,4981,4,1,4))
mibBuilder.exportSymbols('RDN-PRODUCTS-MIB',**{'rdnProducts':rdnProducts,'rdnProductsUnknown':rdnProductsUnknown,'rdnProductsBSR64000':rdnProductsBSR64000,'rdnProductsBSR1000B':rdnProductsBSR1000B,'rdnProductsBSR1000R':rdnProductsBSR1000R,'rdnProductsOSR2000':rdnProductsOSR2000})