#
# PySNMP MIB module MX-INTEROP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-INTEROP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mxInteropMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 3))
mxInteropMIB.setRevisions(('1911-01-21 00:00',))
if mibBuilder.loadTexts: mxInteropMIB.setLastUpdated('1101210000Z')
if mibBuilder.loadTexts: mxInteropMIB.setOrganization('Media5 Corporation')
mxInteropMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 3, 1))
mxInteropConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 3, 2))
mxInteropHttpUAHeaderConfig = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('%product%')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mxInteropHttpUAHeaderConfig.setStatus('current')
mxInteropCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 1))
mxInteropBasicComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 1, 1)).setObjects(("MX-INTEROP-MIB", "mxInteropGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mxInteropBasicComplVer1 = mxInteropBasicComplVer1.setStatus('current')
mxInteropGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 2))
mxInteropGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 2, 5)).setObjects(("MX-INTEROP-MIB", "mxInteropHttpUAHeaderConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mxInteropGroupVer1 = mxInteropGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-INTEROP-MIB", mxInteropCompliances=mxInteropCompliances, mxInteropMIBObjects=mxInteropMIBObjects, mxInteropConformance=mxInteropConformance, PYSNMP_MODULE_ID=mxInteropMIB, mxInteropGroups=mxInteropGroups, mxInteropBasicComplVer1=mxInteropBasicComplVer1, mxInteropHttpUAHeaderConfig=mxInteropHttpUAHeaderConfig, mxInteropGroupVer1=mxInteropGroupVer1, mxInteropMIB=mxInteropMIB)
