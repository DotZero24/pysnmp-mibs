#
# PySNMP MIB module GSM7224-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/GSM7224-REF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
snmpManagedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1))
gsm7224 = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 8))
gsm7224.setRevisions(('2003-05-06 12:00',))
if mibBuilder.loadTexts: gsm7224.setLastUpdated('200311101200Z')
if mibBuilder.loadTexts: gsm7224.setOrganization('Netgear')
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("GSM7224-REF-MIB", snmpManagedSwitch=snmpManagedSwitch, PYSNMP_MODULE_ID=gsm7224, gsm7224=gsm7224, netgear=netgear, AgentPortMask=AgentPortMask)
