#
# PySNMP MIB module PKTC-SEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/PKTC-SEC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
clabProjPacketCable, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjPacketCable")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysDescr, = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
pktcSecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 4))
pktcSecMib.setRevisions(('2003-07-28 00:00',))
if mibBuilder.loadTexts: pktcSecMib.setLastUpdated('200307280000Z')
if mibBuilder.loadTexts: pktcSecMib.setOrganization('Packet Cable OSS Group')
pktcSecErrorCodes = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1))
pktcSecErrorIpsec = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1, 1))
pktcSecErrorSnmpv3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1, 2))
pktcSecErrorFqdn = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1, 3))
memberBody = MibIdentifier((1, 2))
us = MibIdentifier((1, 2, 840))
ansiX942 = MibIdentifier((1, 2, 840, 10046))
numberType = MibIdentifier((1, 2, 840, 10046, 2))
dhPublicNumber = MibIdentifier((1, 2, 840, 10046, 2, 1))
mibBuilder.exportSymbols("PKTC-SEC-MIB", pktcSecErrorCodes=pktcSecErrorCodes, memberBody=memberBody, pktcSecMib=pktcSecMib, pktcSecErrorFqdn=pktcSecErrorFqdn, PYSNMP_MODULE_ID=pktcSecMib, dhPublicNumber=dhPublicNumber, pktcSecErrorIpsec=pktcSecErrorIpsec, ansiX942=ansiX942, pktcSecErrorSnmpv3=pktcSecErrorSnmpv3, numberType=numberType, us=us)
