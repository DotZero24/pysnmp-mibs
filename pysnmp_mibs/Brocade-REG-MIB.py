#
# PySNMP MIB module Brocade-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/Brocade-REG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsi = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588))
bcsi.setRevisions(('2012-02-03 00:00',))
if mibBuilder.loadTexts: bcsi.setLastUpdated('201202030000Z')
if mibBuilder.loadTexts: bcsi.setOrganization(' Brocade Communications Systems, Inc.')
commDev = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2))
if mibBuilder.loadTexts: commDev.setStatus('current')
fibrechannel = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1))
if mibBuilder.loadTexts: fibrechannel.setStatus('current')
nos = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 2))
if mibBuilder.loadTexts: nos.setStatus('current')
fcSwitch = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1))
if mibBuilder.loadTexts: fcSwitch.setStatus('current')
bcsiReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3))
if mibBuilder.loadTexts: bcsiReg.setStatus('current')
bcsiModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1))
if mibBuilder.loadTexts: bcsiModules.setStatus('current')
brocadeAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 2))
if mibBuilder.loadTexts: brocadeAgentCapability.setStatus('current')
mibBuilder.exportSymbols("Brocade-REG-MIB", brocadeAgentCapability=brocadeAgentCapability, commDev=commDev, PYSNMP_MODULE_ID=bcsi, bcsi=bcsi, bcsiReg=bcsiReg, nos=nos, fibrechannel=fibrechannel, bcsiModules=bcsiModules, fcSwitch=fcSwitch)
