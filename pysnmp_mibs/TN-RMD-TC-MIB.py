#
# PySNMP MIB module TN-RMD-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TN-RMD-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tnRmdMIBModules, = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnRmdMIBModules")
tnRmdTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 5, 1, 4, 5))
tnRmdTcModule.setRevisions(('2018-02-23 12:00', '2016-11-16 00:00', '2013-08-09 00:00', '2012-11-28 00:00',))
if mibBuilder.loadTexts: tnRmdTcModule.setLastUpdated('201802231200Z')
if mibBuilder.loadTexts: tnRmdTcModule.setOrganization('Nokia')
class TnRmdAccessIfIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 32)

class TnRmdInventory(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(256, 256)
    fixedLength = 256

class TnRmdPcp(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class TnRmdTpid(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TnRmdVersion(DisplayString):
    status = 'current'

class TnRmdItemCode(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 7)

class TnRmdOui(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TnRmdUserLabel(DisplayString):
    status = 'current'

mibBuilder.exportSymbols("TN-RMD-TC-MIB", TnRmdVersion=TnRmdVersion, tnRmdTcModule=tnRmdTcModule, TnRmdUserLabel=TnRmdUserLabel, TnRmdTpid=TnRmdTpid, TnRmdInventory=TnRmdInventory, TnRmdPcp=TnRmdPcp, PYSNMP_MODULE_ID=tnRmdTcModule, TnRmdOui=TnRmdOui, TnRmdItemCode=TnRmdItemCode, TnRmdAccessIfIndex=TnRmdAccessIfIndex)
