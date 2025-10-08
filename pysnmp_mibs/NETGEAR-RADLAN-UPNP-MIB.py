#
# PySNMP MIB module NETGEAR-RADLAN-UPNP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-UPNP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlUPnP = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 17, 109))
rlUPnP.setRevisions(('2006-03-26 00:00',))
if mibBuilder.loadTexts: rlUPnP.setLastUpdated('200603260000Z')
if mibBuilder.loadTexts: rlUPnP.setOrganization('Radlan Computer Communications Ltd.')
rlUPnPUniqueDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 109, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUPnPUniqueDeviceName.setStatus('current')
rlUPnPEnabling = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 109, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUPnPEnabling.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-UPNP-MIB", rlUPnPUniqueDeviceName=rlUPnPUniqueDeviceName, PYSNMP_MODULE_ID=rlUPnP, rlUPnPEnabling=rlUPnPEnabling, rlUPnP=rlUPnP)
