#
# PySNMP MIB module FS-CAPWAP-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-CAPWAP-DNS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsIfIndex, = mibBuilder.importSymbols("FS-INTERFACE-MIB", "fsIfIndex")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
fsCapwapDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88))
fsCapwapDnsMIB.setRevisions(('2010-07-09 00:00',))
if mibBuilder.loadTexts: fsCapwapDnsMIB.setLastUpdated('201007090000Z')
if mibBuilder.loadTexts: fsCapwapDnsMIB.setOrganization('FS.COM Inc..')
fsCapwapDnsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0))
fsCapwapDnsGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0, 1))
fsLDnsFirstServer = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsLDnsFirstServer.setStatus('current')
fsLDnsSecondServer = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 0, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsLDnsSecondServer.setStatus('current')
fsCapwapDnsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2))
fsCapwapDnsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 1))
fsCapwapDnsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 2))
fsCapwapDnsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 1, 1)).setObjects(("FS-CAPWAP-DNS-MIB", "fsCapwapDnsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsCapwapDnsMIBCompliance = fsCapwapDnsMIBCompliance.setStatus('current')
fsCapwapDnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 88, 2, 2, 1)).setObjects(("FS-CAPWAP-DNS-MIB", "fsLDnsFirstServer"), ("FS-CAPWAP-DNS-MIB", "fsLDnsSecondServer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsCapwapDnsMIBGroup = fsCapwapDnsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-CAPWAP-DNS-MIB", fsCapwapDnsMIBGroups=fsCapwapDnsMIBGroups, fsCapwapDnsMIBGroup=fsCapwapDnsMIBGroup, PYSNMP_MODULE_ID=fsCapwapDnsMIB, fsCapwapDnsMIBCompliance=fsCapwapDnsMIBCompliance, fsCapwapDnsMIBObjects=fsCapwapDnsMIBObjects, fsCapwapDnsMIB=fsCapwapDnsMIB, fsLDnsSecondServer=fsLDnsSecondServer, fsCapwapDnsGlobalConfig=fsCapwapDnsGlobalConfig, fsCapwapDnsMIBCompliances=fsCapwapDnsMIBCompliances, fsLDnsFirstServer=fsLDnsFirstServer, fsCapwapDnsMIBConformance=fsCapwapDnsMIBConformance)
