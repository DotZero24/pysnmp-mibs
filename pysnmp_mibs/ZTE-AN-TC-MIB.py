#
# PySNMP MIB module ZTE-AN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-AN-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxAnTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 200))
zxAnTcMib.setRevisions(('2006-05-18 14:00',))
if mibBuilder.loadTexts: zxAnTcMib.setLastUpdated('200605181400Z')
if mibBuilder.loadTexts: zxAnTcMib.setOrganization('ZTE Corporation')
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxAn = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015))
class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class ZxAnIfindex(TextualConvention, Integer32):
    status = 'current'

class ZxAnPortList(TextualConvention, OctetString):
    status = 'current'

class ZxAnIdList(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("ZTE-AN-TC-MIB", zxAn=zxAn, ZxAnPortList=ZxAnPortList, zxAnTcMib=zxAnTcMib, zte=zte, ZxAnIdList=ZxAnIdList, ZxAnIfindex=ZxAnIfindex, PYSNMP_MODULE_ID=zxAnTcMib, VlanId=VlanId)
