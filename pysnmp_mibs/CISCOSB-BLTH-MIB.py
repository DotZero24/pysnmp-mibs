# SNMP MIB module (CISCOSB-BLTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ciscosb/CISCOSB-BLTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:40:37 2025
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rlBlth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246)
)
if mibBuilder.loadTexts:
    rlBlth.setRevisions(
        ("2022-04-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlBlthIfTable_Object = MibTable
rlBlthIfTable = _RlBlthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1)
)
if mibBuilder.loadTexts:
    rlBlthIfTable.setStatus("current")
_RlBlthIfTableEntry_Object = MibTableRow
rlBlthIfTableEntry = _RlBlthIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1)
)
rlBlthIfTableEntry.setIndexNames(
    (0, "CISCOSB-BLTH-MIB", "rlBlthIfIndex"),
)
if mibBuilder.loadTexts:
    rlBlthIfTableEntry.setStatus("current")
_RlBlthIfIndex_Type = InterfaceIndex
_RlBlthIfIndex_Object = MibTableColumn
rlBlthIfIndex = _RlBlthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 1),
    _RlBlthIfIndex_Type()
)
rlBlthIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBlthIfIndex.setStatus("current")
_RlBlthPin_Type = DisplayString
_RlBlthPin_Object = MibTableColumn
rlBlthPin = _RlBlthPin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 2),
    _RlBlthPin_Type()
)
rlBlthPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBlthPin.setStatus("current")
_RlBlthDeviceName_Type = DisplayString
_RlBlthDeviceName_Object = MibTableColumn
rlBlthDeviceName = _RlBlthDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 3),
    _RlBlthDeviceName_Type()
)
rlBlthDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBlthDeviceName.setStatus("current")
_RlBlthDongleMAC_Type = MacAddress
_RlBlthDongleMAC_Object = MibTableColumn
rlBlthDongleMAC = _RlBlthDongleMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 4),
    _RlBlthDongleMAC_Type()
)
rlBlthDongleMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBlthDongleMAC.setStatus("current")


class _RlBlthDonglePresent_Type(Integer32):
    """Custom type rlBlthDonglePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RlBlthDonglePresent_Type.__name__ = "Integer32"
_RlBlthDonglePresent_Object = MibTableColumn
rlBlthDonglePresent = _RlBlthDonglePresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 5),
    _RlBlthDonglePresent_Type()
)
rlBlthDonglePresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBlthDonglePresent.setStatus("current")
_RlBlthBus_Type = DisplayString
_RlBlthBus_Object = MibTableColumn
rlBlthBus = _RlBlthBus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 6),
    _RlBlthBus_Type()
)
rlBlthBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBlthBus.setStatus("current")


class _RlBlthState_Type(Integer32):
    """Custom type rlBlthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("discoverable", 1),
          ("connected", 2),
          ("admindown", 3))
    )


_RlBlthState_Type.__name__ = "Integer32"
_RlBlthState_Object = MibTableColumn
rlBlthState = _RlBlthState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 7),
    _RlBlthState_Type()
)
rlBlthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBlthState.setStatus("current")
_RlBlthPartnerName_Type = DisplayString
_RlBlthPartnerName_Object = MibTableColumn
rlBlthPartnerName = _RlBlthPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 246, 1, 1, 8),
    _RlBlthPartnerName_Type()
)
rlBlthPartnerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBlthPartnerName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-BLTH-MIB",
    **{"rlBlth": rlBlth,
       "rlBlthIfTable": rlBlthIfTable,
       "rlBlthIfTableEntry": rlBlthIfTableEntry,
       "rlBlthIfIndex": rlBlthIfIndex,
       "rlBlthPin": rlBlthPin,
       "rlBlthDeviceName": rlBlthDeviceName,
       "rlBlthDongleMAC": rlBlthDongleMAC,
       "rlBlthDonglePresent": rlBlthDonglePresent,
       "rlBlthBus": rlBlthBus,
       "rlBlthState": rlBlthState,
       "rlBlthPartnerName": rlBlthPartnerName}
)
