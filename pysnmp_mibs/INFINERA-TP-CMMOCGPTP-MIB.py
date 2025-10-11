# SNMP MIB module (INFINERA-TP-CMMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-CMMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:45 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cmmOcgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28)
)
if mibBuilder.loadTexts:
    cmmOcgPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmOcgPtpTable_Object = MibTable
cmmOcgPtpTable = _CmmOcgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1)
)
if mibBuilder.loadTexts:
    cmmOcgPtpTable.setStatus("current")
_CmmOcgPtpEntry_Object = MibTableRow
cmmOcgPtpEntry = _CmmOcgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1)
)
cmmOcgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmmOcgPtpEntry.setStatus("current")
_CmmOcgPtpDiscoveredRemoteTP_Type = DisplayString
_CmmOcgPtpDiscoveredRemoteTP_Object = MibTableColumn
cmmOcgPtpDiscoveredRemoteTP = _CmmOcgPtpDiscoveredRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 1),
    _CmmOcgPtpDiscoveredRemoteTP_Type()
)
cmmOcgPtpDiscoveredRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpDiscoveredRemoteTP.setStatus("current")


class _CmmOcgPtpAutoDiscoveryState_Type(Integer32):
    """Custom type cmmOcgPtpAutoDiscoveryState based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("completed", 2),
          ("unknown", 3),
          ("notValidOrShutdown", 4),
          ("failed", 5))
    )


_CmmOcgPtpAutoDiscoveryState_Type.__name__ = "Integer32"
_CmmOcgPtpAutoDiscoveryState_Object = MibTableColumn
cmmOcgPtpAutoDiscoveryState = _CmmOcgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 2),
    _CmmOcgPtpAutoDiscoveryState_Type()
)
cmmOcgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpAutoDiscoveryState.setStatus("current")


class _CmmOcgPtpPmHistStatsEnable_Type(Integer32):
    """Custom type cmmOcgPtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

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


_CmmOcgPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_CmmOcgPtpPmHistStatsEnable_Object = MibTableColumn
cmmOcgPtpPmHistStatsEnable = _CmmOcgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 3),
    _CmmOcgPtpPmHistStatsEnable_Type()
)
cmmOcgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOcgPtpPmHistStatsEnable.setStatus("current")


class _CmmOcgPtpOperatingMode_Type(Integer32):
    """Custom type cmmOcgPtpOperatingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gen1", 1),
          ("gen2", 2))
    )


_CmmOcgPtpOperatingMode_Type.__name__ = "Integer32"
_CmmOcgPtpOperatingMode_Object = MibTableColumn
cmmOcgPtpOperatingMode = _CmmOcgPtpOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 4),
    _CmmOcgPtpOperatingMode_Type()
)
cmmOcgPtpOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmmOcgPtpOperatingMode.setStatus("current")


class _CmmOcgPtpOcgPowerControlLoop_Type(Integer32):
    """Custom type cmmOcgPtpOcgPowerControlLoop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmmOcgPtpOcgPowerControlLoop_Type.__name__ = "Integer32"
_CmmOcgPtpOcgPowerControlLoop_Object = MibTableColumn
cmmOcgPtpOcgPowerControlLoop = _CmmOcgPtpOcgPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 5),
    _CmmOcgPtpOcgPowerControlLoop_Type()
)
cmmOcgPtpOcgPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOcgPtpOcgPowerControlLoop.setStatus("current")


class _CmmOcgPtpProvisionedOcgNumber_Type(Integer32):
    """Custom type cmmOcgPtpProvisionedOcgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CmmOcgPtpProvisionedOcgNumber_Type.__name__ = "Integer32"
_CmmOcgPtpProvisionedOcgNumber_Object = MibTableColumn
cmmOcgPtpProvisionedOcgNumber = _CmmOcgPtpProvisionedOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 6),
    _CmmOcgPtpProvisionedOcgNumber_Type()
)
cmmOcgPtpProvisionedOcgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpProvisionedOcgNumber.setStatus("current")
_CmmOcgPtpConformance_ObjectIdentity = ObjectIdentity
cmmOcgPtpConformance = _CmmOcgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3)
)
_CmmOcgPtpCompliances_ObjectIdentity = ObjectIdentity
cmmOcgPtpCompliances = _CmmOcgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 1)
)
_CmmOcgPtpGroups_ObjectIdentity = ObjectIdentity
cmmOcgPtpGroups = _CmmOcgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 2)
)

# Managed Objects groups

cmmOcgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 2, 1)
)
cmmOcgPtpGroup.setObjects(
      *(("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpDiscoveredRemoteTP"),
        ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpAutoDiscoveryState"),
        ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpPmHistStatsEnable"),
        ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpOcgPowerControlLoop"),
        ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpProvisionedOcgNumber"))
)
if mibBuilder.loadTexts:
    cmmOcgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmmOcgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 1, 1)
)
cmmOcgPtpCompliance.setObjects(
    ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpGroup")
)
if mibBuilder.loadTexts:
    cmmOcgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-CMMOCGPTP-MIB",
    **{"cmmOcgPtpMIB": cmmOcgPtpMIB,
       "cmmOcgPtpTable": cmmOcgPtpTable,
       "cmmOcgPtpEntry": cmmOcgPtpEntry,
       "cmmOcgPtpDiscoveredRemoteTP": cmmOcgPtpDiscoveredRemoteTP,
       "cmmOcgPtpAutoDiscoveryState": cmmOcgPtpAutoDiscoveryState,
       "cmmOcgPtpPmHistStatsEnable": cmmOcgPtpPmHistStatsEnable,
       "cmmOcgPtpOperatingMode": cmmOcgPtpOperatingMode,
       "cmmOcgPtpOcgPowerControlLoop": cmmOcgPtpOcgPowerControlLoop,
       "cmmOcgPtpProvisionedOcgNumber": cmmOcgPtpProvisionedOcgNumber,
       "cmmOcgPtpConformance": cmmOcgPtpConformance,
       "cmmOcgPtpCompliances": cmmOcgPtpCompliances,
       "cmmOcgPtpCompliance": cmmOcgPtpCompliance,
       "cmmOcgPtpGroups": cmmOcgPtpGroups,
       "cmmOcgPtpGroup": cmmOcgPtpGroup}
)
