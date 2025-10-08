#
# PySNMP MIB module LANOPTICS-BRIDGE-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/LANOPTICS-BRIDGE-OPTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsBridgeProxyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6))
lanOpticsLMGRAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6, 8))
lanOpticsLMGRLinkID = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsLMGRLinkID.setStatus('mandatory')
lanOpticsLMGRCaptCntrlLink = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsLMGRCaptCntrlLink.setStatus('mandatory')
mibBuilder.exportSymbols("LANOPTICS-BRIDGE-OPTION-MIB", lanOpticsLMGRLinkID=lanOpticsLMGRLinkID, lanOpticsLMGRCaptCntrlLink=lanOpticsLMGRCaptCntrlLink, lanOpticsBridgeProxyAgent=lanOpticsBridgeProxyAgent, lanOptics=lanOptics, lanOpticsLMGRAgent=lanOpticsLMGRAgent)
