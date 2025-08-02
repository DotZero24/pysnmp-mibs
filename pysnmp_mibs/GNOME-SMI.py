_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gnome=ModuleIdentity((1,3,6,1,4,1,3319))
if mibBuilder.loadTexts:gnome.setRevisions(('2007-09-07 00:00','2005-05-07 00:00','2003-12-07 00:00','1998-09-01 00:00'))
_GnomeProducts_ObjectIdentity=ObjectIdentity
gnomeProducts=_GnomeProducts_ObjectIdentity((1,3,6,1,4,1,3319,1))
if mibBuilder.loadTexts:gnomeProducts.setStatus(_A)
_GnomeMgmt_ObjectIdentity=ObjectIdentity
gnomeMgmt=_GnomeMgmt_ObjectIdentity((1,3,6,1,4,1,3319,2))
if mibBuilder.loadTexts:gnomeMgmt.setStatus(_A)
_GnomeTest_ObjectIdentity=ObjectIdentity
gnomeTest=_GnomeTest_ObjectIdentity((1,3,6,1,4,1,3319,3))
if mibBuilder.loadTexts:gnomeTest.setStatus(_A)
_GnomeSysadmin_ObjectIdentity=ObjectIdentity
gnomeSysadmin=_GnomeSysadmin_ObjectIdentity((1,3,6,1,4,1,3319,4))
if mibBuilder.loadTexts:gnomeSysadmin.setStatus(_A)
_GnomeLDAP_ObjectIdentity=ObjectIdentity
gnomeLDAP=_GnomeLDAP_ObjectIdentity((1,3,6,1,4,1,3319,5))
if mibBuilder.loadTexts:gnomeLDAP.setStatus(_A)
mibBuilder.exportSymbols('GNOME-SMI',**{'gnome':gnome,'gnomeProducts':gnomeProducts,'gnomeMgmt':gnomeMgmt,'gnomeTest':gnomeTest,'gnomeSysadmin':gnomeSysadmin,'gnomeLDAP':gnomeLDAP})