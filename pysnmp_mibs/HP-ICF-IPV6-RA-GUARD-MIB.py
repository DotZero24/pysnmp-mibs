#
# PySNMP MIB module HP-ICF-IPV6-RA-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-IPV6-RA-GUARD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hpicfIpv6RAGuard = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87))
hpicfIpv6RAGuard.setRevisions(('2011-03-16 05:24',))
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setLastUpdated('201103160524Z')
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setOrganization('Hewlett-Packard Company HP Networking')
hpicfIpv6RAGuardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1))
hpicfIpv6RAGuardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1))
hpicfRAGuardPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfRAGuardPortTable.setStatus('current')
hpicfRAGuardPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfRAGuardPortEntry.setStatus('current')
hpicfRAGuardPortBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfRAGuardPortBlocked.setStatus('current')
hpicfRAGuardPortBlockedRAs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRAs.setStatus('current')
hpicfRAGuardPortBlockedRedirs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRedirs.setStatus('current')
hpicfRAGuardPortLog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfRAGuardPortLog.setStatus('current')
hpicfRAGuardLastErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noError", 1), ("insufficientHardwareResources", 2), ("genericError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardLastErrorCode.setStatus('current')
hpicfIpv6RAGuardConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2))
hpicfIpv6RAGuardCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1))
hpicfIpv6RAGuardGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2))
hpicfIpv6RAGuardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2, 1)).setObjects(("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlocked"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRAs"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRedirs"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortLog"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardLastErrorCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfIpv6RAGuardGroup = hpicfIpv6RAGuardGroup.setStatus('current')
hpicfIpv6RAGuardCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1, 1)).setObjects(("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfIpv6RAGuardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfIpv6RAGuardCompliance = hpicfIpv6RAGuardCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-IPV6-RA-GUARD-MIB", hpicfIpv6RAGuard=hpicfIpv6RAGuard, hpicfIpv6RAGuardCompliances=hpicfIpv6RAGuardCompliances, hpicfIpv6RAGuardConfig=hpicfIpv6RAGuardConfig, hpicfIpv6RAGuardGroup=hpicfIpv6RAGuardGroup, hpicfRAGuardPortBlocked=hpicfRAGuardPortBlocked, hpicfIpv6RAGuardCompliance=hpicfIpv6RAGuardCompliance, hpicfRAGuardPortBlockedRedirs=hpicfRAGuardPortBlockedRedirs, hpicfRAGuardPortLog=hpicfRAGuardPortLog, hpicfRAGuardPortBlockedRAs=hpicfRAGuardPortBlockedRAs, hpicfIpv6RAGuardGroups=hpicfIpv6RAGuardGroups, hpicfRAGuardPortTable=hpicfRAGuardPortTable, hpicfRAGuardLastErrorCode=hpicfRAGuardLastErrorCode, hpicfIpv6RAGuardConformance=hpicfIpv6RAGuardConformance, hpicfRAGuardPortEntry=hpicfRAGuardPortEntry, PYSNMP_MODULE_ID=hpicfIpv6RAGuard, hpicfIpv6RAGuardObjects=hpicfIpv6RAGuardObjects)
