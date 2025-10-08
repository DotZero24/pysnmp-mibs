#
# PySNMP MIB module TRIPLE-DES-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/TRIPLE-DES-CONSORTIUM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, iso, Counter32, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "iso", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
tripleDESConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
tripleDESConsortiumMIB.setRevisions(('2003-02-03 00:00',))
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setLastUpdated('200302030000Z')
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setOrganization('Triple DES Consortium')
tripleDESConsortiumPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
mibBuilder.exportSymbols("TRIPLE-DES-CONSORTIUM-MIB", PYSNMP_MODULE_ID=tripleDESConsortiumMIB, tripleDESConsortiumMIB=tripleDESConsortiumMIB, usm3DESPrivProtocol=usm3DESPrivProtocol, tripleDESConsortiumPrivProtocols=tripleDESConsortiumPrivProtocols)
