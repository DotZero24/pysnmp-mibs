#
# PySNMP MIB module PDN-MPD-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-MPD-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pdnMpdExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnMpdExt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("PDN-MPD-EXT-MIB", pdnMpdExtMIBConformance=pdnMpdExtMIBConformance, pdnMpdExtCompliance=pdnMpdExtCompliance, pdnMpdExtSecurityModeConfig=pdnMpdExtSecurityModeConfig, pdnMpdExtMIBObjects=pdnMpdExtMIBObjects, pdnMpdExtGroups=pdnMpdExtGroups, pdnMpdExtMIB=pdnMpdExtMIB, pdnMpdExtCompliances=pdnMpdExtCompliances, pdnMpdExtGroup=pdnMpdExtGroup, PYSNMP_MODULE_ID=pdnMpdExtMIB, PdnMpdExtSecurityMode=PdnMpdExtSecurityMode)
