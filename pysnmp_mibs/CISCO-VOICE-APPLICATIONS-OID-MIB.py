#
# PySNMP MIB module CISCO-VOICE-APPLICATIONS-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-APPLICATIONS-OID-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceApplicationsOIDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 5))
ciscoVoiceApplicationsOIDMIB.setRevisions(('2004-06-17 00:00',))
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setLastUpdated('200406170000Z')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setOrganization('Cisco Systems, Inc.')
cvaMIBOids = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1))
ciscoCallManager = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 1))
ciscoCallManagerExpress = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 2))
ciscoSRST = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 3))
ciscoBTS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 4))
ciscoCSPS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 5))
mibBuilder.exportSymbols("CISCO-VOICE-APPLICATIONS-OID-MIB", cvaMIBOids=cvaMIBOids, ciscoBTS=ciscoBTS, ciscoCSPS=ciscoCSPS, ciscoSRST=ciscoSRST, PYSNMP_MODULE_ID=ciscoVoiceApplicationsOIDMIB, ciscoCallManager=ciscoCallManager, ciscoCallManagerExpress=ciscoCallManagerExpress, ciscoVoiceApplicationsOIDMIB=ciscoVoiceApplicationsOIDMIB)
