#
# PySNMP MIB module PKTC-SEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/PKTC-SEC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
clabProjPacketCable, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjPacketCable")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysDescr, = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("PKTC-SEC-MIB", pktcSecErrorIpsec=pktcSecErrorIpsec, us=us, pktcSecErrorCodes=pktcSecErrorCodes, ansiX942=ansiX942, pktcSecErrorSnmpv3=pktcSecErrorSnmpv3, PYSNMP_MODULE_ID=pktcSecMib, pktcSecMib=pktcSecMib, memberBody=memberBody, dhPublicNumber=dhPublicNumber, numberType=numberType, pktcSecErrorFqdn=pktcSecErrorFqdn)
