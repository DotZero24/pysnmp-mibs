#
# PySNMP MIB module CISCO-DMN-DSG-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSPVTG = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429))
ciscoSPVTG.setRevisions(('2010-08-30 11:00', '2009-11-26 15:00',))
if mibBuilder.loadTexts: ciscoSPVTG.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoSPVTG.setOrganization('Cisco Systems, Inc.')
ciscoSat = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2))
ciscoDMN = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2))
ciscoDSGUtilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5))
ciscoDSGProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 6))
mibBuilder.exportSymbols("CISCO-DMN-DSG-ROOT-MIB", PYSNMP_MODULE_ID=ciscoSPVTG, ciscoSPVTG=ciscoSPVTG, ciscoSat=ciscoSat, ciscoDMN=ciscoDMN, ciscoDSGUtilities=ciscoDSGUtilities, ciscoDSGProducts=ciscoDSGProducts)
