#
# PySNMP MIB module BAY-STACK-ERROR-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/BAY-STACK-ERROR-MESSAGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BAY-STACK-ERROR-MESSAGE-MIB", bsemErrorMessageRequestId=bsemErrorMessageRequestId, bsemObjects=bsemObjects, bsemErrorMessageString=bsemErrorMessageString, bsemErrorMessageTable=bsemErrorMessageTable, bsemErrorMessageAddress=bsemErrorMessageAddress, PYSNMP_MODULE_ID=bayStackErrorMessageMib, bayStackErrorMessageMib=bayStackErrorMessageMib, bsemErrorMessageAddressType=bsemErrorMessageAddressType, bsemErrorMessageEntry=bsemErrorMessageEntry)
