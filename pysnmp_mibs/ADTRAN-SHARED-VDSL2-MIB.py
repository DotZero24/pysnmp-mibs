#
# PySNMP MIB module ADTRAN-SHARED-VDSL2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-VDSL2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:37 2025
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
adVdsl2Identity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 65))
adVdsl2Identity.setRevisions(('2008-07-08 00:00',))
if mibBuilder.loadTexts: adVdsl2Identity.setLastUpdated('200807080000Z')
if mibBuilder.loadTexts: adVdsl2Identity.setOrganization('Adtran, Inc.')
adVdsl2 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 65))
adGenVdsl2 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 65, 1))
adGenVdsl2ID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 65, 1))
mibBuilder.exportSymbols("ADTRAN-SHARED-VDSL2-MIB", adGenVdsl2=adGenVdsl2, PYSNMP_MODULE_ID=adVdsl2Identity, adGenVdsl2ID=adGenVdsl2ID, adVdsl2Identity=adVdsl2Identity, adVdsl2=adVdsl2)
