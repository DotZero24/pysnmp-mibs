#
# PySNMP MIB module SIAE-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siaemic/SIAE-IP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:46:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
smIpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 29601, 100, 1, 10))
if mibBuilder.loadTexts: smIpMIB.setLastUpdated('201802010000Z')
if mibBuilder.loadTexts: smIpMIB.setOrganization('SIAE MICROELETTRONICA spa')
smIpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 29601, 100, 1, 10, 1))
smIpForwardingStatus = MibScalar((1, 3, 6, 1, 4, 1, 29601, 100, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smIpForwardingStatus.setStatus('current')
mibBuilder.exportSymbols("SIAE-IP-MIB", PYSNMP_MODULE_ID=smIpMIB, smIpForwardingStatus=smIpForwardingStatus, smIpMIB=smIpMIB, smIpGlobal=smIpGlobal)
