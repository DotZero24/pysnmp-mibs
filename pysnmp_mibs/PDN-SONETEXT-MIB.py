# SNMP MIB module (PDN-SONETEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-SONETEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:59:40 2025
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

(pdnSonetMIB,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnSonetMIB")

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
 NotificationType,
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
    "NotificationType",
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

(sonetLineCurrentStatus,
 sonetPathCurrentStatus,
 sonetSectionCurrentStatus) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetLineCurrentStatus",
    "sonetPathCurrentStatus",
    "sonetSectionCurrentStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevSonetConfig_ObjectIdentity = ObjectIdentity
devSonetConfig = _DevSonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1)
)
_DevSonetConfigTable_Object = MibTable
devSonetConfigTable = _DevSonetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1)
)
if mibBuilder.loadTexts:
    devSonetConfigTable.setStatus("mandatory")
_DevSonetConfigEntry_Object = MibTableRow
devSonetConfigEntry = _DevSonetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1)
)
devSonetConfigEntry.setIndexNames(
    (0, "PDN-SONETEXT-MIB", "devSonetIfIndex"),
)
if mibBuilder.loadTexts:
    devSonetConfigEntry.setStatus("mandatory")
_DevSonetIfIndex_Type = Integer32
_DevSonetIfIndex_Object = MibTableColumn
devSonetIfIndex = _DevSonetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 1),
    _DevSonetIfIndex_Type()
)
devSonetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSonetIfIndex.setStatus("mandatory")


class _DevSonetXmitClkSrc_Type(Integer32):
    """Custom type devSonetXmitClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("systemTiming", 4))
    )


_DevSonetXmitClkSrc_Type.__name__ = "Integer32"
_DevSonetXmitClkSrc_Object = MibTableColumn
devSonetXmitClkSrc = _DevSonetXmitClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 2),
    _DevSonetXmitClkSrc_Type()
)
devSonetXmitClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSonetXmitClkSrc.setStatus("mandatory")
_DevSonetStatusLastChange_Type = TimeTicks
_DevSonetStatusLastChange_Object = MibTableColumn
devSonetStatusLastChange = _DevSonetStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 3),
    _DevSonetStatusLastChange_Type()
)
devSonetStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSonetStatusLastChange.setStatus("mandatory")


class _DevSonetStatusChangeTrapEnable_Type(Integer32):
    """Custom type devSonetStatusChangeTrapEnable based on Integer32"""
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


_DevSonetStatusChangeTrapEnable_Type.__name__ = "Integer32"
_DevSonetStatusChangeTrapEnable_Object = MibTableColumn
devSonetStatusChangeTrapEnable = _DevSonetStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 4),
    _DevSonetStatusChangeTrapEnable_Type()
)
devSonetStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSonetStatusChangeTrapEnable.setStatus("mandatory")
_DevSonetTraps_ObjectIdentity = ObjectIdentity
devSonetTraps = _DevSonetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2)
)

# Managed Objects groups


# Notification objects

devSonetStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2, 0, 1)
)
devSonetStatusChange.setObjects(
      *(("PDN-SONETEXT-MIB", "devSonetStatusLastChange"),
        ("SONET-MIB", "sonetSectionCurrentStatus"),
        ("SONET-MIB", "sonetLineCurrentStatus"),
        ("SONET-MIB", "sonetPathCurrentStatus"))
)
if mibBuilder.loadTexts:
    devSonetStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-SONETEXT-MIB",
    **{"devSonetConfig": devSonetConfig,
       "devSonetConfigTable": devSonetConfigTable,
       "devSonetConfigEntry": devSonetConfigEntry,
       "devSonetIfIndex": devSonetIfIndex,
       "devSonetXmitClkSrc": devSonetXmitClkSrc,
       "devSonetStatusLastChange": devSonetStatusLastChange,
       "devSonetStatusChangeTrapEnable": devSonetStatusChangeTrapEnable,
       "devSonetTraps": devSonetTraps,
       "devSonetStatusChange": devSonetStatusChange}
)
