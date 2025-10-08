#
# PySNMP MIB module FDRY-IPV6-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/FDRY-IPV6-IP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
RtrStatus, = mibBuilder.importSymbols("FOUNDRY-SN-IP-MIB", "RtrStatus")
fdryIpv6, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryIpv6")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fdryIpv6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1))
fdryIpv6MIB.setRevisions(('2017-08-07 00:00', '2010-05-06 00:00',))
if mibBuilder.loadTexts: fdryIpv6MIB.setLastUpdated('201708070000Z')
if mibBuilder.loadTexts: fdryIpv6MIB.setOrganization('Ruckus Wireless, Inc.')
fdryIpv6GlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1))
fdryIpv6LoadShare = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 1), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpv6LoadShare.setStatus('current')
fdryIpv6LoadShareNumOfPaths = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpv6LoadShareNumOfPaths.setStatus('current')
mibBuilder.exportSymbols("FDRY-IPV6-IP-MIB", PYSNMP_MODULE_ID=fdryIpv6MIB, fdryIpv6MIB=fdryIpv6MIB, fdryIpv6LoadShareNumOfPaths=fdryIpv6LoadShareNumOfPaths, fdryIpv6LoadShare=fdryIpv6LoadShare, fdryIpv6GlobalObjects=fdryIpv6GlobalObjects)
