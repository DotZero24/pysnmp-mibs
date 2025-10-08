#
# PySNMP MIB module CISCO-ROUTE-POLICIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ROUTE-POLICIES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRoutePoliciesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578))
ciscoRoutePoliciesMIB.setRevisions(('2006-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setLastUpdated('200608180000Z')
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setOrganization('Cisco Systems, Inc. ')
ciscoRoutePoliciesMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 0))
ciscoRoutePoliciesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 1))
ciscoRoutePoliciesMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 2))
crpPolicies = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1))
if mibBuilder.loadTexts: crpPolicies.setStatus('current')
crpPolicyIfIndex = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1, 1))
if mibBuilder.loadTexts: crpPolicyIfIndex.setStatus('current')
mibBuilder.exportSymbols("CISCO-ROUTE-POLICIES-MIB", ciscoRoutePoliciesMIB=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIBConform=ciscoRoutePoliciesMIBConform, ciscoRoutePoliciesMIBNotifs=ciscoRoutePoliciesMIBNotifs, crpPolicyIfIndex=crpPolicyIfIndex, crpPolicies=crpPolicies, PYSNMP_MODULE_ID=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIBObjects=ciscoRoutePoliciesMIBObjects)
