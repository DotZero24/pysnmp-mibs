#
# PySNMP MIB module ADTRAN-SHARED-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-DS1-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adDS1Identity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 78))
adDS1Identity.setRevisions(('2008-09-18 00:00',))
if mibBuilder.loadTexts: adDS1Identity.setLastUpdated('200809180000Z')
if mibBuilder.loadTexts: adDS1Identity.setOrganization('Adtran, Inc.')
adDS1 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 78))
adGenDS1Test = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 78, 1))
adGenDS1TestID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 78, 1))
mibBuilder.exportSymbols("ADTRAN-SHARED-DS1-MIB", adDS1=adDS1, PYSNMP_MODULE_ID=adDS1Identity, adGenDS1Test=adGenDS1Test, adGenDS1TestID=adGenDS1TestID, adDS1Identity=adDS1Identity)
