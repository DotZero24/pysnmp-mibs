#
# PySNMP MIB module ADTRAN-SHARED-ADSL2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-ADSL2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adAdsl2Identity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 82))
adAdsl2Identity.setRevisions(('2011-10-25 00:00',))
if mibBuilder.loadTexts: adAdsl2Identity.setLastUpdated('201110250000Z')
if mibBuilder.loadTexts: adAdsl2Identity.setOrganization('Adtran, Inc.')
adAdsl2 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 82))
adGenAdsl2 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 82, 1))
adGenAdsl2ID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 82, 1))
mibBuilder.exportSymbols("ADTRAN-SHARED-ADSL2-MIB", PYSNMP_MODULE_ID=adAdsl2Identity, adAdsl2Identity=adAdsl2Identity, adGenAdsl2=adGenAdsl2, adAdsl2=adAdsl2, adGenAdsl2ID=adGenAdsl2ID)
