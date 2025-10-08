#
# PySNMP MIB module GNOME-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/gnome/GNOME-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gnome = ModuleIdentity((1, 3, 6, 1, 4, 1, 3319))
gnome.setRevisions(('2007-09-07 00:00', '2005-05-07 00:00', '2003-12-07 00:00', '1998-09-01 00:00',))
if mibBuilder.loadTexts: gnome.setLastUpdated('200709070000Z')
if mibBuilder.loadTexts: gnome.setOrganization('GNOME project')
gnomeProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1))
if mibBuilder.loadTexts: gnomeProducts.setStatus('current')
gnomeMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 2))
if mibBuilder.loadTexts: gnomeMgmt.setStatus('current')
gnomeTest = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 3))
if mibBuilder.loadTexts: gnomeTest.setStatus('current')
gnomeSysadmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 4))
if mibBuilder.loadTexts: gnomeSysadmin.setStatus('current')
gnomeLDAP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 5))
if mibBuilder.loadTexts: gnomeLDAP.setStatus('current')
mibBuilder.exportSymbols("GNOME-SMI", PYSNMP_MODULE_ID=gnome, gnome=gnome, gnomeLDAP=gnomeLDAP, gnomeMgmt=gnomeMgmt, gnomeTest=gnomeTest, gnomeSysadmin=gnomeSysadmin, gnomeProducts=gnomeProducts)
