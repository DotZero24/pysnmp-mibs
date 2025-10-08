#
# PySNMP MIB module ONEACCESS-VRF-TO-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-VRF-TO-IF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMIp, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("ONEACCESS-VRF-TO-IF-MIB", oacExpIMIPVrfToIf=oacExpIMIPVrfToIf, OacExpVrfName=OacExpVrfName, PYSNMP_MODULE_ID=oacExpIMIPVrfToIf, oacExpIMIPVrfToIfTable=oacExpIMIPVrfToIfTable, oacVrfName=oacVrfName, oacExpIMIPVrfToIfEntry=oacExpIMIPVrfToIfEntry)
