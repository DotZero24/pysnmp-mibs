#
# PySNMP MIB module CRESTRON-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/crestron/CRESTRON-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
crestron = ModuleIdentity((1, 3, 6, 1, 4, 1, 3212))
if mibBuilder.loadTexts: crestron.setLastUpdated('200308181523Z')
if mibBuilder.loadTexts: crestron.setOrganization('Crestron Electronics, Inc.')
class TcpPort(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class UdpPort(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Digital(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

crestronAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 1))
crestronNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 2))
crestronObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 3))
crestronRootMIBVersion = MibScalar((1, 3, 6, 1, 4, 1, 3212, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crestronRootMIBVersion.setStatus('current')
crestronConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 5))
crestronCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 5, 2))
crestronGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 5, 3))
crestronRootAllObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 3212, 5, 3, 1)).setObjects(("CRESTRON-ROOT-MIB", "crestronRootMIBVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crestronRootAllObjects = crestronRootAllObjects.setStatus('current')
crestronCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 6))
crestronControl = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 7))
crestronTouch = MibIdentifier((1, 3, 6, 1, 4, 1, 3212, 8))
mibBuilder.exportSymbols("CRESTRON-ROOT-MIB", PYSNMP_MODULE_ID=crestron, crestronCompliances=crestronCompliances, crestronRootAllObjects=crestronRootAllObjects, crestronControl=crestronControl, UdpPort=UdpPort, crestronTouch=crestronTouch, crestronObjects=crestronObjects, crestronGroups=crestronGroups, crestronAdmin=crestronAdmin, TcpPort=TcpPort, Digital=Digital, crestron=crestron, crestronRootMIBVersion=crestronRootMIBVersion, crestronCommon=crestronCommon, crestronNotifications=crestronNotifications, crestronConformance=crestronConformance)
