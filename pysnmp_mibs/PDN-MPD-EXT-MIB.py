#
# PySNMP MIB module PDN-MPD-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-MPD-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pdnMpdExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnMpdExt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnMpdExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1))
if mibBuilder.loadTexts: pdnMpdExtMIB.setLastUpdated('200304081900Z')
if mibBuilder.loadTexts: pdnMpdExtMIB.setOrganization('Paradyne Corporation MIB Working Group')
pdnMpdExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1))
pdnMpdExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2))
class PdnMpdExtSecurityMode(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("snmpv1NoAuthNoPriv", 1), ("snmpv2cNoAuthNoPriv", 2), ("snmpv3NoAuthNoPriv", 3), ("snmpv3AuthNoPriv", 4), ("snmpv3AuthPriv", 5))

pdnMpdExtSecurityModeConfig = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1, 1), PdnMpdExtSecurityMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMpdExtSecurityModeConfig.setStatus('current')
pdnMpdExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1))
pdnMpdExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2))
pdnMpdExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1, 1)).setObjects(("PDN-MPD-EXT-MIB", "pdnMpdExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMpdExtCompliance = pdnMpdExtCompliance.setStatus('current')
pdnMpdExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2, 1)).setObjects(("PDN-MPD-EXT-MIB", "pdnMpdExtSecurityModeConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMpdExtGroup = pdnMpdExtGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-MPD-EXT-MIB", pdnMpdExtSecurityModeConfig=pdnMpdExtSecurityModeConfig, pdnMpdExtGroup=pdnMpdExtGroup, PYSNMP_MODULE_ID=pdnMpdExtMIB, pdnMpdExtCompliance=pdnMpdExtCompliance, pdnMpdExtMIB=pdnMpdExtMIB, PdnMpdExtSecurityMode=PdnMpdExtSecurityMode, pdnMpdExtGroups=pdnMpdExtGroups, pdnMpdExtMIBObjects=pdnMpdExtMIBObjects, pdnMpdExtCompliances=pdnMpdExtCompliances, pdnMpdExtMIBConformance=pdnMpdExtMIBConformance)
