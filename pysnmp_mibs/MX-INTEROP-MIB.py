#
# PySNMP MIB module MX-INTEROP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-INTEROP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MX-INTEROP-MIB", mxInteropGroups=mxInteropGroups, PYSNMP_MODULE_ID=mxInteropMIB, mxInteropCompliances=mxInteropCompliances, mxInteropBasicComplVer1=mxInteropBasicComplVer1, mxInteropConformance=mxInteropConformance, mxInteropHttpUAHeaderConfig=mxInteropHttpUAHeaderConfig, mxInteropMIB=mxInteropMIB, mxInteropGroupVer1=mxInteropGroupVer1, mxInteropMIBObjects=mxInteropMIBObjects)
