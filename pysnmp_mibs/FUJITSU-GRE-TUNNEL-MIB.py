# SNMP MIB module (FUJITSU-GRE-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fujitsu/FUJITSU-GRE-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:31 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(fssInterfaces,) = mibBuilder.importSymbols(
    "FSS-COMMON-SMI",
    "fssInterfaces")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fSS_GRE_TUNNEL_INTERFACE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000)
)
if mibBuilder.loadTexts:
    fSS_GRE_TUNNEL_INTERFACE.setRevisions(
        ("2017-01-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_Interfaces_stateInterfaceFssGRETable_Object = MibTable
interfaces_stateInterfaceFssGRETable = _Interfaces_stateInterfaceFssGRETable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1)
)
if mibBuilder.loadTexts:
    interfaces_stateInterfaceFssGRETable.setStatus("current")
_Interfaces_stateInterfaceFssGREEntry_Object = MibTableRow
interfaces_stateInterfaceFssGREEntry = _Interfaces_stateInterfaceFssGREEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1)
)
interfaces_stateInterfaceFssGREEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaces_stateInterfaceFssGREEntry.setStatus("current")
_Tunnel_stateMTU_Type = Unsigned32
_Tunnel_stateMTU_Object = MibTableColumn
tunnel_stateMTU = _Tunnel_stateMTU_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 1),
    _Tunnel_stateMTU_Type()
)
tunnel_stateMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnel_stateMTU.setStatus("current")
_Tunnel_statePackets_input_Type = Counter64
_Tunnel_statePackets_input_Object = MibTableColumn
tunnel_statePackets_input = _Tunnel_statePackets_input_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 2),
    _Tunnel_statePackets_input_Type()
)
tunnel_statePackets_input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnel_statePackets_input.setStatus("current")
_Tunnel_stateInput_errors_Type = Counter64
_Tunnel_stateInput_errors_Object = MibTableColumn
tunnel_stateInput_errors = _Tunnel_stateInput_errors_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 3),
    _Tunnel_stateInput_errors_Type()
)
tunnel_stateInput_errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnel_stateInput_errors.setStatus("current")
_Tunnel_statePackets_output_Type = Counter64
_Tunnel_statePackets_output_Object = MibTableColumn
tunnel_statePackets_output = _Tunnel_statePackets_output_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 4),
    _Tunnel_statePackets_output_Type()
)
tunnel_statePackets_output.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnel_statePackets_output.setStatus("current")
_Tunnel_stateOutput_errors_Type = Counter64
_Tunnel_stateOutput_errors_Object = MibTableColumn
tunnel_stateOutput_errors = _Tunnel_stateOutput_errors_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 5),
    _Tunnel_stateOutput_errors_Type()
)
tunnel_stateOutput_errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnel_stateOutput_errors.setStatus("current")
_Tunnel_stateBytes_Type = Counter64
_Tunnel_stateBytes_Object = MibTableColumn
tunnel_stateBytes = _Tunnel_stateBytes_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 700, 1000, 1, 1, 6),
    _Tunnel_stateBytes_Type()
)
tunnel_stateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnel_stateBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUJITSU-GRE-TUNNEL-MIB",
    **{"UnsignedByte": UnsignedByte,
       "String": String,
       "fSS-GRE-TUNNEL-INTERFACE": fSS_GRE_TUNNEL_INTERFACE,
       "interfaces-stateInterfaceFssGRETable": interfaces_stateInterfaceFssGRETable,
       "interfaces-stateInterfaceFssGREEntry": interfaces_stateInterfaceFssGREEntry,
       "tunnel-stateMTU": tunnel_stateMTU,
       "tunnel-statePackets-input": tunnel_statePackets_input,
       "tunnel-stateInput-errors": tunnel_stateInput_errors,
       "tunnel-statePackets-output": tunnel_statePackets_output,
       "tunnel-stateOutput-errors": tunnel_stateOutput_errors,
       "tunnel-stateBytes": tunnel_stateBytes}
)
