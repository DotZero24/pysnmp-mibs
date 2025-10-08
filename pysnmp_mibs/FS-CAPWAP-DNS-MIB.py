#
# PySNMP MIB module FS-CAPWAP-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-CAPWAP-DNS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsIfIndex, = mibBuilder.importSymbols("FS-INTERFACE-MIB", "fsIfIndex")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-CAPWAP-DNS-MIB", fsCapwapDnsMIB=fsCapwapDnsMIB, fsCapwapDnsMIBObjects=fsCapwapDnsMIBObjects, fsCapwapDnsMIBCompliances=fsCapwapDnsMIBCompliances, fsCapwapDnsGlobalConfig=fsCapwapDnsGlobalConfig, fsCapwapDnsMIBGroup=fsCapwapDnsMIBGroup, fsCapwapDnsMIBCompliance=fsCapwapDnsMIBCompliance, fsCapwapDnsMIBGroups=fsCapwapDnsMIBGroups, fsLDnsFirstServer=fsLDnsFirstServer, PYSNMP_MODULE_ID=fsCapwapDnsMIB, fsCapwapDnsMIBConformance=fsCapwapDnsMIBConformance, fsLDnsSecondServer=fsLDnsSecondServer)
