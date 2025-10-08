#
# PySNMP MIB module NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nnchassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2))
nnchassisMib.setRevisions(('1999-07-01 00:00',))
if mibBuilder.loadTexts: nnchassisMib.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: nnchassisMib.setOrganization('Nortel')
nnchassisType = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnchassisType.setStatus('current')
nnchassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnchassisSerialNumber.setStatus('current')
mibBuilder.exportSymbols("NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB", nnchassisMib=nnchassisMib, nnchassisType=nnchassisType, nnchassisSerialNumber=nnchassisSerialNumber, PYSNMP_MODULE_ID=nnchassisMib)
