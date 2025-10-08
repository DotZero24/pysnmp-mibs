#
# PySNMP MIB module FUJITSU-GRE-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fujitsu/FUJITSU-GRE-TUNNEL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fssInterfaces, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssInterfaces")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
fSS_GRE_TUNNEL_INTERFACE = ModuleIdentity((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000)).setLabel("fSS-GRE-TUNNEL-INTERFACE")
fSS_GRE_TUNNEL_INTERFACE.setRevisions(('2017-01-12 00:00',))
if mibBuilder.loadTexts: fSS_GRE_TUNNEL_INTERFACE.setLastUpdated('201701120000Z')
if mibBuilder.loadTexts: fSS_GRE_TUNNEL_INTERFACE.setOrganization('@ORGANIZATION')
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

interfaces_stateInterfaceFssGRETable = MibTable((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1), ).setLabel("interfaces-stateInterfaceFssGRETable")
if mibBuilder.loadTexts: interfaces_stateInterfaceFssGRETable.setStatus('current')
interfaces_stateInterfaceFssGREEntry = MibTableRow((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1), ).setLabel("interfaces-stateInterfaceFssGREEntry").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: interfaces_stateInterfaceFssGREEntry.setStatus('current')
tunnel_stateMTU = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 1), Unsigned32()).setLabel("tunnel-stateMTU").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnel_stateMTU.setStatus('current')
tunnel_statePackets_input = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 2), Counter64()).setLabel("tunnel-statePackets-input").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnel_statePackets_input.setStatus('current')
tunnel_stateInput_errors = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 3), Counter64()).setLabel("tunnel-stateInput-errors").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnel_stateInput_errors.setStatus('current')
tunnel_statePackets_output = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 4), Counter64()).setLabel("tunnel-statePackets-output").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnel_statePackets_output.setStatus('current')
tunnel_stateOutput_errors = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 5), Counter64()).setLabel("tunnel-stateOutput-errors").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnel_stateOutput_errors.setStatus('current')
tunnel_stateBytes = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 6), Counter64()).setLabel("tunnel-stateBytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnel_stateBytes.setStatus('current')
mibBuilder.exportSymbols("FUJITSU-GRE-TUNNEL-MIB", tunnel_statePackets_input=tunnel_statePackets_input, PYSNMP_MODULE_ID=fSS_GRE_TUNNEL_INTERFACE, tunnel_stateMTU=tunnel_stateMTU, interfaces_stateInterfaceFssGREEntry=interfaces_stateInterfaceFssGREEntry, fSS_GRE_TUNNEL_INTERFACE=fSS_GRE_TUNNEL_INTERFACE, tunnel_stateOutput_errors=tunnel_stateOutput_errors, UnsignedByte=UnsignedByte, tunnel_stateInput_errors=tunnel_stateInput_errors, interfaces_stateInterfaceFssGRETable=interfaces_stateInterfaceFssGRETable, tunnel_statePackets_output=tunnel_statePackets_output, String=String, tunnel_stateBytes=tunnel_stateBytes)
