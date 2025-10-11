# SNMP MIB module (CTRON-IMIM-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cabletron/CTRON-IMIM-ADDRESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:54:17 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_CommsDevice_ObjectIdentity = ObjectIdentity
commsDevice = _CommsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1)
)
_Subsystem_ObjectIdentity = ObjectIdentity
subsystem = _Subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6)
)
_BackplaneProtocol_ObjectIdentity = ObjectIdentity
backplaneProtocol = _BackplaneProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5)
)
_ImimAddress_ObjectIdentity = ObjectIdentity
imimAddress = _ImimAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1)
)
_ImimAddressTable_Object = MibTable
imimAddressTable = _ImimAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1)
)
if mibBuilder.loadTexts:
    imimAddressTable.setStatus("mandatory")
_ImimAddressEntry_Object = MibTableRow
imimAddressEntry = _ImimAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1)
)
imimAddressEntry.setIndexNames(
    (0, "CTRON-IMIM-ADDRESS-MIB", "imimAddressChassisSlot"),
)
if mibBuilder.loadTexts:
    imimAddressEntry.setStatus("mandatory")


class _ImimAddressChassisSlot_Type(Integer32):
    """Custom type imimAddressChassisSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ImimAddressChassisSlot_Type.__name__ = "Integer32"
_ImimAddressChassisSlot_Object = MibTableColumn
imimAddressChassisSlot = _ImimAddressChassisSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 1),
    _ImimAddressChassisSlot_Type()
)
imimAddressChassisSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imimAddressChassisSlot.setStatus("mandatory")


class _ImimAddressMAC_Type(OctetString):
    """Custom type imimAddressMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_ImimAddressMAC_Type.__name__ = "OctetString"
_ImimAddressMAC_Object = MibTableColumn
imimAddressMAC = _ImimAddressMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 2),
    _ImimAddressMAC_Type()
)
imimAddressMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imimAddressMAC.setStatus("mandatory")


class _ImimAddressIP_Type(OctetString):
    """Custom type imimAddressIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ImimAddressIP_Type.__name__ = "OctetString"
_ImimAddressIP_Object = MibTableColumn
imimAddressIP = _ImimAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 3),
    _ImimAddressIP_Type()
)
imimAddressIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imimAddressIP.setStatus("mandatory")


class _BackplaneHeartbeat_Type(Integer32):
    """Custom type backplaneHeartbeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("heartBeatPresent", 1),
          ("heartBeatAbsent", 2),
          ("notSupported", 3))
    )


_BackplaneHeartbeat_Type.__name__ = "Integer32"
_BackplaneHeartbeat_Object = MibScalar
backplaneHeartbeat = _BackplaneHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 2),
    _BackplaneHeartbeat_Type()
)
backplaneHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneHeartbeat.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-IMIM-ADDRESS-MIB",
    **{"cabletron": cabletron,
       "commsDevice": commsDevice,
       "subsystem": subsystem,
       "backplaneProtocol": backplaneProtocol,
       "imimAddress": imimAddress,
       "imimAddressTable": imimAddressTable,
       "imimAddressEntry": imimAddressEntry,
       "imimAddressChassisSlot": imimAddressChassisSlot,
       "imimAddressMAC": imimAddressMAC,
       "imimAddressIP": imimAddressIP,
       "backplaneHeartbeat": backplaneHeartbeat}
)
