#
# PySNMP MIB module ADTRAN-SHARED-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-DS1-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:02 2025
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
adDS1Identity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 78))
adDS1Identity.setRevisions(('2008-09-18 00:00',))
if mibBuilder.loadTexts: adDS1Identity.setLastUpdated('200809180000Z')
if mibBuilder.loadTexts: adDS1Identity.setOrganization('Adtran, Inc.')
adDS1 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 78))
adGenDS1Test = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 78, 1))
adGenDS1TestID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 78, 1))
mibBuilder.exportSymbols("ADTRAN-SHARED-DS1-MIB", adGenDS1TestID=adGenDS1TestID, adDS1Identity=adDS1Identity, adDS1=adDS1, adGenDS1Test=adGenDS1Test, PYSNMP_MODULE_ID=adDS1Identity)
