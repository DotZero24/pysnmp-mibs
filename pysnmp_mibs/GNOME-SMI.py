#
# PySNMP MIB module GNOME-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/gnome/GNOME-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("GNOME-SMI", gnomeTest=gnomeTest, gnomeMgmt=gnomeMgmt, PYSNMP_MODULE_ID=gnome, gnomeProducts=gnomeProducts, gnomeSysadmin=gnomeSysadmin, gnome=gnome, gnomeLDAP=gnomeLDAP)
