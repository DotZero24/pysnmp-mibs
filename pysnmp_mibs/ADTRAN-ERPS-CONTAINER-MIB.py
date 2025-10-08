#
# PySNMP MIB module ADTRAN-ERPS-CONTAINER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-ERPS-CONTAINER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adShared, adComplianceShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adComplianceShared", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenErpsModuleIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 79))
if mibBuilder.loadTexts: adGenErpsModuleIdentity.setLastUpdated('200809301344Z')
if mibBuilder.loadTexts: adGenErpsModuleIdentity.setOrganization('ADTRAN, Inc.')
adGenErpsModule = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 79))
adGenErpsCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 10000, 79))
adGenErps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 79, 1))
adGenErpsID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 79, 1))
mibBuilder.exportSymbols("ADTRAN-ERPS-CONTAINER-MIB", adGenErpsModuleIdentity=adGenErpsModuleIdentity, adGenErpsID=adGenErpsID, adGenErps=adGenErps, PYSNMP_MODULE_ID=adGenErpsModuleIdentity, adGenErpsModule=adGenErpsModule, adGenErpsCompliance=adGenErpsCompliance)
