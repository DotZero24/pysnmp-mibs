#
# PySNMP MIB module TRIPLE-DES-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/TRIPLE-DES-CONSORTIUM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, snmpModules, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "snmpModules", "Gauge32")
AutonomousType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString")
tripleDESConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
tripleDESConsortiumMIB.setRevisions(('2003-02-03 00:00',))
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setLastUpdated('200302030000Z')
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setOrganization('Triple DES Consortium')
tripleDESConsortiumPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
mibBuilder.exportSymbols("TRIPLE-DES-CONSORTIUM-MIB", usm3DESPrivProtocol=usm3DESPrivProtocol, tripleDESConsortiumPrivProtocols=tripleDESConsortiumPrivProtocols, PYSNMP_MODULE_ID=tripleDESConsortiumMIB, tripleDESConsortiumMIB=tripleDESConsortiumMIB)
