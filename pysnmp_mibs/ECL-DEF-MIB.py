#
# PySNMP MIB module ECL-DEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/ECL-DEF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
euroCableLabs = ModuleIdentity((1, 3, 6, 1, 4, 1, 24624))
euroCableLabs.setRevisions(('2006-01-05 10:00',))
if mibBuilder.loadTexts: euroCableLabs.setLastUpdated('200601051000Z')
if mibBuilder.loadTexts: euroCableLabs.setOrganization('EuroCableLabs')
eclFunction = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 1))
eclProject = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2))
eclProjDocsis = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 1))
eclProjPacketCable = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2))
eclSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 3))
eclCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 4))
pktcEclMtaMib = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 1))
pktcEclSigMib = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 2))
pktcEclEventMib = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 3))
pktcEclSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 4))
pktcEclLawfulIntercept = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 5))
pktcEclEnhancements = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6))
pktcEclEnMtaMib = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1))
pktcEclEnSigMib = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 2))
pktcEclEnEventMib = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 3))
pktcEclEnSecurityMib = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 4))
mibBuilder.exportSymbols("ECL-DEF-MIB", pktcEclSecurity=pktcEclSecurity, eclProject=eclProject, eclProjPacketCable=eclProjPacketCable, eclFunction=eclFunction, pktcEclEnMtaMib=pktcEclEnMtaMib, eclSecurity=eclSecurity, pktcEclEnSecurityMib=pktcEclEnSecurityMib, euroCableLabs=euroCableLabs, PYSNMP_MODULE_ID=euroCableLabs, eclProjDocsis=eclProjDocsis, eclCommon=eclCommon, pktcEclLawfulIntercept=pktcEclLawfulIntercept, pktcEclSigMib=pktcEclSigMib, pktcEclEventMib=pktcEclEventMib, pktcEclEnEventMib=pktcEclEnEventMib, pktcEclEnSigMib=pktcEclEnSigMib, pktcEclMtaMib=pktcEclMtaMib, pktcEclEnhancements=pktcEclEnhancements)
