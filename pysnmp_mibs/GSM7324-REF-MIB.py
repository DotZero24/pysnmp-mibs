#
# PySNMP MIB module GSM7324-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/GSM7324-REF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:51:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
snmpManagedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1))
gsm7324 = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 7))
gsm7324.setRevisions(('2003-05-06 12:00',))
if mibBuilder.loadTexts: gsm7324.setLastUpdated('200305061200Z')
if mibBuilder.loadTexts: gsm7324.setOrganization('Netgear')
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("GSM7324-REF-MIB", gsm7324=gsm7324, snmpManagedSwitch=snmpManagedSwitch, PYSNMP_MODULE_ID=gsm7324, AgentPortMask=AgentPortMask, netgear=netgear)
