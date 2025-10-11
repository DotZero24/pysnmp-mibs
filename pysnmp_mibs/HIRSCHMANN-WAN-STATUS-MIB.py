# SNMP MIB module (HIRSCHMANN-WAN-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-WAN-STATUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:52:11 2025
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

(hmWanMgmt,) = mibBuilder.importSymbols(
    "HIRSCHMANN-WAN-MIB",
    "hmWanMgmt")

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

hmWanStatusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 3)
)
if mibBuilder.loadTexts:
    hmWanStatusMib.setRevisions(
        ("2015-02-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HmWanStatusMBusOverload1_Type(Integer32):
    """Custom type hmWanStatusMBusOverload1 based on Integer32"""
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


_HmWanStatusMBusOverload1_Type.__name__ = "Integer32"
_HmWanStatusMBusOverload1_Object = MibScalar
hmWanStatusMBusOverload1 = _HmWanStatusMBusOverload1_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 1),
    _HmWanStatusMBusOverload1_Type()
)
hmWanStatusMBusOverload1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanStatusMBusOverload1.setStatus("current")


class _HmWanStatusMBusOverload2_Type(Integer32):
    """Custom type hmWanStatusMBusOverload2 based on Integer32"""
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


_HmWanStatusMBusOverload2_Type.__name__ = "Integer32"
_HmWanStatusMBusOverload2_Object = MibScalar
hmWanStatusMBusOverload2 = _HmWanStatusMBusOverload2_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 2),
    _HmWanStatusMBusOverload2_Type()
)
hmWanStatusMBusOverload2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanStatusMBusOverload2.setStatus("current")
_HmWanStatusTemperature_Type = Integer32
_HmWanStatusTemperature_Object = MibScalar
hmWanStatusTemperature = _HmWanStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 3),
    _HmWanStatusTemperature_Type()
)
hmWanStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanStatusTemperature.setStatus("current")
_HmWanStatusVoltage_Type = Integer32
_HmWanStatusVoltage_Object = MibScalar
hmWanStatusVoltage = _HmWanStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 4),
    _HmWanStatusVoltage_Type()
)
hmWanStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanStatusVoltage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-WAN-STATUS-MIB",
    **{"hmWanStatusMib": hmWanStatusMib,
       "hmWanStatusMBusOverload1": hmWanStatusMBusOverload1,
       "hmWanStatusMBusOverload2": hmWanStatusMBusOverload2,
       "hmWanStatusTemperature": hmWanStatusTemperature,
       "hmWanStatusVoltage": hmWanStatusVoltage}
)
