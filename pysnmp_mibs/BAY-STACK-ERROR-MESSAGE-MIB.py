#
# PySNMP MIB module BAY-STACK-ERROR-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/BAY-STACK-ERROR-MESSAGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackErrorMessageMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 19))
bayStackErrorMessageMib.setRevisions(('2013-10-11 00:00', '2006-11-14 00:00',))
if mibBuilder.loadTexts: bayStackErrorMessageMib.setLastUpdated('201310110000Z')
if mibBuilder.loadTexts: bayStackErrorMessageMib.setOrganization('Nortel Networks')
bsemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 19, 1))
bsemErrorMessageTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1), )
if mibBuilder.loadTexts: bsemErrorMessageTable.setStatus('current')
bsemErrorMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageAddressType"), (0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageAddress"), (0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageRequestId"))
if mibBuilder.loadTexts: bsemErrorMessageEntry.setStatus('current')
bsemErrorMessageAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: bsemErrorMessageAddressType.setStatus('current')
bsemErrorMessageAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: bsemErrorMessageAddress.setStatus('current')
bsemErrorMessageRequestId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: bsemErrorMessageRequestId.setStatus('current')
bsemErrorMessageString = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsemErrorMessageString.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-ERROR-MESSAGE-MIB", bayStackErrorMessageMib=bayStackErrorMessageMib, bsemErrorMessageAddressType=bsemErrorMessageAddressType, bsemErrorMessageRequestId=bsemErrorMessageRequestId, bsemObjects=bsemObjects, bsemErrorMessageString=bsemErrorMessageString, bsemErrorMessageAddress=bsemErrorMessageAddress, PYSNMP_MODULE_ID=bayStackErrorMessageMib, bsemErrorMessageTable=bsemErrorMessageTable, bsemErrorMessageEntry=bsemErrorMessageEntry)
