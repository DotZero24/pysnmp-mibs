# SNMP MIB module (SUPERMICRO-RMON2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RMON2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:05:24 2025
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

fsrmon2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 19)
)
if mibBuilder.loadTexts:
    fsrmon2.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRmon2Trace_Type = Unsigned32
_FsRmon2Trace_Object = MibScalar
fsRmon2Trace = _FsRmon2Trace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 19, 1),
    _FsRmon2Trace_Type()
)
fsRmon2Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmon2Trace.setStatus("current")


class _FsRmon2AdminStatus_Type(Integer32):
    """Custom type fsRmon2AdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsRmon2AdminStatus_Type.__name__ = "Integer32"
_FsRmon2AdminStatus_Object = MibScalar
fsRmon2AdminStatus = _FsRmon2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 19, 2),
    _FsRmon2AdminStatus_Type()
)
fsRmon2AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmon2AdminStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RMON2-MIB",
    **{"fsrmon2": fsrmon2,
       "fsRmon2Trace": fsRmon2Trace,
       "fsRmon2AdminStatus": fsRmon2AdminStatus}
)
