#
# PySNMP MIB module TN-RMD-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TN-RMD-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("TN-RMD-TC-MIB", TnRmdPcp=TnRmdPcp, TnRmdVersion=TnRmdVersion, TnRmdInventory=TnRmdInventory, TnRmdOui=TnRmdOui, TnRmdItemCode=TnRmdItemCode, TnRmdAccessIfIndex=TnRmdAccessIfIndex, tnRmdTcModule=tnRmdTcModule, PYSNMP_MODULE_ID=tnRmdTcModule, TnRmdTpid=TnRmdTpid, TnRmdUserLabel=TnRmdUserLabel)
