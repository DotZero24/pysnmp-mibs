#
# PySNMP MIB module ZTE-AN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZTE-AN-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("ZTE-AN-TC-MIB", zte=zte, PYSNMP_MODULE_ID=zxAnTcMib, zxAnTcMib=zxAnTcMib, ZxAnIfindex=ZxAnIfindex, zxAn=zxAn, VlanId=VlanId, ZxAnPortList=ZxAnPortList, ZxAnIdList=ZxAnIdList)
