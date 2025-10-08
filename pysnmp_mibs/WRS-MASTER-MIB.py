#
# PySNMP MIB module WRS-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/WRS-MASTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zte = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902))
zte.setRevisions(('1901-10-29 00:00',))
if mibBuilder.loadTexts: zte.setLastUpdated('0110290000Z')
if mibBuilder.loadTexts: zte.setOrganization('Zhongxing Telcom Co. Ltd.')
zxEdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008))
zxEdslOwn = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1))
zxEdslLR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1))
tms = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1))
idb = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 1))
tmsGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 2))
oemSwapi = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 3))
oemProd = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 4))
rmonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 1, 1))
mibBuilder.exportSymbols("WRS-MASTER-MIB", oemSwapi=oemSwapi, zxEdslLR1=zxEdslLR1, rmonMib=rmonMib, tms=tms, zxEdsl=zxEdsl, zte=zte, idb=idb, oemProd=oemProd, tmsGeneric=tmsGeneric, zxEdslOwn=zxEdslOwn, PYSNMP_MODULE_ID=zte)
