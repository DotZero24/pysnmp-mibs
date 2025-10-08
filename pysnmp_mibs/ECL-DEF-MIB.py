#
# PySNMP MIB module ECL-DEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/ECL-DEF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ECL-DEF-MIB", eclFunction=eclFunction, pktcEclSecurity=pktcEclSecurity, eclProjPacketCable=eclProjPacketCable, pktcEclEnMtaMib=pktcEclEnMtaMib, pktcEclLawfulIntercept=pktcEclLawfulIntercept, pktcEclEnEventMib=pktcEclEnEventMib, pktcEclEnSecurityMib=pktcEclEnSecurityMib, euroCableLabs=euroCableLabs, pktcEclSigMib=pktcEclSigMib, eclCommon=eclCommon, eclSecurity=eclSecurity, pktcEclEnSigMib=pktcEclEnSigMib, pktcEclEventMib=pktcEclEventMib, pktcEclMtaMib=pktcEclMtaMib, PYSNMP_MODULE_ID=euroCableLabs, pktcEclEnhancements=pktcEclEnhancements, eclProjDocsis=eclProjDocsis, eclProject=eclProject)
