#
# PySNMP MIB module ELTEX-MES-SNMP-COMMUNITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-SNMP-COMMUNITY-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesSnmpCommExtMIB, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesSnmpCommExtMIB")
snmpCommunityEntry, = mibBuilder.importSymbols("SNMP-COMMUNITY-MIB", "snmpCommunityEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1), )
if mibBuilder.loadTexts: eltSnmpCommunityTable.setStatus('current')
eltSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1, 1), )
snmpCommunityEntry.registerAugmentions(("ELTEX-MES-SNMP-COMMUNITY-EXT-MIB", "eltSnmpCommunityEntry"))
eltSnmpCommunityEntry.setIndexNames(*snmpCommunityEntry.getIndexNames())
if mibBuilder.loadTexts: eltSnmpCommunityEntry.setStatus('current')
eltSnmpCommunityAccessList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltSnmpCommunityAccessList.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-SNMP-COMMUNITY-EXT-MIB", eltSnmpCommunityTable=eltSnmpCommunityTable, eltSnmpCommunityAccessList=eltSnmpCommunityAccessList, eltSnmpCommunityEntry=eltSnmpCommunityEntry)
