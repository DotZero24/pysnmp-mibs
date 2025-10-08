#
# PySNMP MIB module ONEACCESS-VRF-TO-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-VRF-TO-IF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMIp, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacExpIMIPVrfToIf = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11))
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setLastUpdated('1204051200Z')
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setOrganization('ONE ACCESS')
class OacExpVrfName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

oacExpIMIPVrfToIfTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1), )
if mibBuilder.loadTexts: oacExpIMIPVrfToIfTable.setStatus('current')
oacExpIMIPVrfToIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacExpIMIPVrfToIfEntry.setStatus('current')
oacVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1, 1, 1), OacExpVrfName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacVrfName.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-VRF-TO-IF-MIB", oacVrfName=oacVrfName, PYSNMP_MODULE_ID=oacExpIMIPVrfToIf, oacExpIMIPVrfToIf=oacExpIMIPVrfToIf, oacExpIMIPVrfToIfEntry=oacExpIMIPVrfToIfEntry, OacExpVrfName=OacExpVrfName, oacExpIMIPVrfToIfTable=oacExpIMIPVrfToIfTable)
