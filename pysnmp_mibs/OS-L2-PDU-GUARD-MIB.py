# SNMP MIB module (OS-L2-PDU-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-L2-PDU-GUARD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:24 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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

osL2PduGuard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17)
)
if mibBuilder.loadTexts:
    osL2PduGuard.setRevisions(
        ("2010-01-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class L2ProtocolId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("stp", 2),
          ("ethoam", 3),
          ("efm", 4),
          ("dot1x", 5),
          ("esmc", 6),
          ("cdp", 7),
          ("dtp", 8),
          ("udld", 9),
          ("pagp", 10),
          ("pvst", 11),
          ("vtp", 12),
          ("lacp", 13),
          ("erp", 14),
          ("lamp", 15),
          ("elmi", 16),
          ("lldp", 17),
          ("garp", 18))
    )



class L2PortState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("normal", 2),
          ("isolated", 3),
          ("inform", 4))
    )



class SupportValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )



# MIB Managed Objects in the order of their OIDs

_OsL2PduGuardCpGen_ObjectIdentity = ObjectIdentity
osL2PduGuardCpGen = _OsL2PduGuardCpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 1)
)
_OsL2PduGuardSupprt_Type = SupportValue
_OsL2PduGuardSupprt_Object = MibScalar
osL2PduGuardSupprt = _OsL2PduGuardSupprt_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 1, 1),
    _OsL2PduGuardSupprt_Type()
)
osL2PduGuardSupprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osL2PduGuardSupprt.setStatus("current")
_OsL2PduGuardTable_Object = MibTable
osL2PduGuardTable = _OsL2PduGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 2)
)
if mibBuilder.loadTexts:
    osL2PduGuardTable.setStatus("current")
_OsL2PduGuardEntry_Object = MibTableRow
osL2PduGuardEntry = _OsL2PduGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1)
)
osL2PduGuardEntry.setIndexNames(
    (0, "OS-L2-PDU-GUARD-MIB", "osL2PduGuardProtocol"),
    (0, "OS-L2-PDU-GUARD-MIB", "osL2PduGuardPort"),
)
if mibBuilder.loadTexts:
    osL2PduGuardEntry.setStatus("current")
_OsL2PduGuardProtocol_Type = L2ProtocolId
_OsL2PduGuardProtocol_Object = MibTableColumn
osL2PduGuardProtocol = _OsL2PduGuardProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 1),
    _OsL2PduGuardProtocol_Type()
)
osL2PduGuardProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osL2PduGuardProtocol.setStatus("current")


class _OsL2PduGuardPort_Type(Integer32):
    """Custom type osL2PduGuardPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsL2PduGuardPort_Type.__name__ = "Integer32"
_OsL2PduGuardPort_Object = MibTableColumn
osL2PduGuardPort = _OsL2PduGuardPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 2),
    _OsL2PduGuardPort_Type()
)
osL2PduGuardPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osL2PduGuardPort.setStatus("current")


class _OsL2PduGuardIsolateRate_Type(Unsigned32):
    """Custom type osL2PduGuardIsolateRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 300),
    )


_OsL2PduGuardIsolateRate_Type.__name__ = "Unsigned32"
_OsL2PduGuardIsolateRate_Object = MibTableColumn
osL2PduGuardIsolateRate = _OsL2PduGuardIsolateRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 3),
    _OsL2PduGuardIsolateRate_Type()
)
osL2PduGuardIsolateRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osL2PduGuardIsolateRate.setStatus("current")
if mibBuilder.loadTexts:
    osL2PduGuardIsolateRate.setUnits("packets per second")


class _OsL2PduGuardInformRate_Type(Unsigned32):
    """Custom type osL2PduGuardInformRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 300),
    )


_OsL2PduGuardInformRate_Type.__name__ = "Unsigned32"
_OsL2PduGuardInformRate_Object = MibTableColumn
osL2PduGuardInformRate = _OsL2PduGuardInformRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 4),
    _OsL2PduGuardInformRate_Type()
)
osL2PduGuardInformRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osL2PduGuardInformRate.setStatus("current")
if mibBuilder.loadTexts:
    osL2PduGuardInformRate.setUnits("packets per second")
_OsL2PduGuardState_Type = L2PortState
_OsL2PduGuardState_Object = MibTableColumn
osL2PduGuardState = _OsL2PduGuardState_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 5),
    _OsL2PduGuardState_Type()
)
osL2PduGuardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osL2PduGuardState.setStatus("current")
_OsL2PduGuardCpConformance_ObjectIdentity = ObjectIdentity
osL2PduGuardCpConformance = _OsL2PduGuardCpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 100)
)
_OsL2PduGuardCpMIBCompliances_ObjectIdentity = ObjectIdentity
osL2PduGuardCpMIBCompliances = _OsL2PduGuardCpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 1)
)
_OsL2PduGuardCpMIBGroups_ObjectIdentity = ObjectIdentity
osL2PduGuardCpMIBGroups = _OsL2PduGuardCpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 2)
)

# Managed Objects groups

osL2PduGuardMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 2, 1)
)
osL2PduGuardMandatoryGroup.setObjects(
      *(("OS-L2-PDU-GUARD-MIB", "osL2PduGuardSupprt"),
        ("OS-L2-PDU-GUARD-MIB", "osL2PduGuardIsolateRate"),
        ("OS-L2-PDU-GUARD-MIB", "osL2PduGuardInformRate"),
        ("OS-L2-PDU-GUARD-MIB", "osL2PduGuardState"))
)
if mibBuilder.loadTexts:
    osL2PduGuardMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osL2PduGuardCpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 1, 1)
)
osL2PduGuardCpMIBCompliance.setObjects(
    ("OS-L2-PDU-GUARD-MIB", "osL2PduGuardMandatoryGroup")
)
if mibBuilder.loadTexts:
    osL2PduGuardCpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-L2-PDU-GUARD-MIB",
    **{"L2ProtocolId": L2ProtocolId,
       "L2PortState": L2PortState,
       "SupportValue": SupportValue,
       "osL2PduGuard": osL2PduGuard,
       "osL2PduGuardCpGen": osL2PduGuardCpGen,
       "osL2PduGuardSupprt": osL2PduGuardSupprt,
       "osL2PduGuardTable": osL2PduGuardTable,
       "osL2PduGuardEntry": osL2PduGuardEntry,
       "osL2PduGuardProtocol": osL2PduGuardProtocol,
       "osL2PduGuardPort": osL2PduGuardPort,
       "osL2PduGuardIsolateRate": osL2PduGuardIsolateRate,
       "osL2PduGuardInformRate": osL2PduGuardInformRate,
       "osL2PduGuardState": osL2PduGuardState,
       "osL2PduGuardCpConformance": osL2PduGuardCpConformance,
       "osL2PduGuardCpMIBCompliances": osL2PduGuardCpMIBCompliances,
       "osL2PduGuardCpMIBCompliance": osL2PduGuardCpMIBCompliance,
       "osL2PduGuardCpMIBGroups": osL2PduGuardCpMIBGroups,
       "osL2PduGuardMandatoryGroup": osL2PduGuardMandatoryGroup}
)
