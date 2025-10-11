# SNMP MIB module (NEWTEC-SIMPEDECAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-SIMPEDECAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:55 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcSiMpeDecaps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500)
)
if mibBuilder.loadTexts:
    ntcSiMpeDecaps.setRevisions(
        ("2017-07-10 12:00",
         "2014-09-09 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcSiMpeDeObjects_ObjectIdentity = ObjectIdentity
ntcSiMpeDeObjects = _NtcSiMpeDeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1)
)
if mibBuilder.loadTexts:
    ntcSiMpeDeObjects.setStatus("current")
_NtcSiMpeDeConfiguration_ObjectIdentity = ObjectIdentity
ntcSiMpeDeConfiguration = _NtcSiMpeDeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 1)
)
if mibBuilder.loadTexts:
    ntcSiMpeDeConfiguration.setStatus("current")


class _NtcSiMpeDeEnable_Type(NtcEnable):
    """Custom type ntcSiMpeDeEnable based on NtcEnable"""
    defaultValue = 0


_NtcSiMpeDeEnable_Type.__name__ = "NtcEnable"
_NtcSiMpeDeEnable_Object = MibScalar
ntcSiMpeDeEnable = _NtcSiMpeDeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 1, 1),
    _NtcSiMpeDeEnable_Type()
)
ntcSiMpeDeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcSiMpeDeEnable.setStatus("current")


class _NtcSiMpeDeDataPid_Type(Unsigned32):
    """Custom type ntcSiMpeDeDataPid based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 8190),
    )


_NtcSiMpeDeDataPid_Type.__name__ = "Unsigned32"
_NtcSiMpeDeDataPid_Object = MibScalar
ntcSiMpeDeDataPid = _NtcSiMpeDeDataPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 1, 2),
    _NtcSiMpeDeDataPid_Type()
)
ntcSiMpeDeDataPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcSiMpeDeDataPid.setStatus("current")
_NtcSiMpeDeMacAddress_Type = MacAddress
_NtcSiMpeDeMacAddress_Object = MibScalar
ntcSiMpeDeMacAddress = _NtcSiMpeDeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 1, 3),
    _NtcSiMpeDeMacAddress_Type()
)
ntcSiMpeDeMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcSiMpeDeMacAddress.setStatus("current")
_NtcSiMpeDeMonitoring_ObjectIdentity = ObjectIdentity
ntcSiMpeDeMonitoring = _NtcSiMpeDeMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 2)
)
if mibBuilder.loadTexts:
    ntcSiMpeDeMonitoring.setStatus("current")


class _NtcSiMpeDeCounterReset_Type(Integer32):
    """Custom type ntcSiMpeDeCounterReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcSiMpeDeCounterReset_Type.__name__ = "Integer32"
_NtcSiMpeDeCounterReset_Object = MibScalar
ntcSiMpeDeCounterReset = _NtcSiMpeDeCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 2, 1),
    _NtcSiMpeDeCounterReset_Type()
)
ntcSiMpeDeCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcSiMpeDeCounterReset.setStatus("current")
_NtcSiMpeDeForwardBitRate_Type = Counter64
_NtcSiMpeDeForwardBitRate_Object = MibScalar
ntcSiMpeDeForwardBitRate = _NtcSiMpeDeForwardBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 2, 2),
    _NtcSiMpeDeForwardBitRate_Type()
)
ntcSiMpeDeForwardBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcSiMpeDeForwardBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcSiMpeDeForwardBitRate.setUnits("bps")
_NtcSiMpeDeDroppedPackets_Type = Counter64
_NtcSiMpeDeDroppedPackets_Object = MibScalar
ntcSiMpeDeDroppedPackets = _NtcSiMpeDeDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 2, 3),
    _NtcSiMpeDeDroppedPackets_Type()
)
ntcSiMpeDeDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcSiMpeDeDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcSiMpeDeDroppedPackets.setUnits("packets")
_NtcSiMpeDeAlarms_ObjectIdentity = ObjectIdentity
ntcSiMpeDeAlarms = _NtcSiMpeDeAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 3)
)
if mibBuilder.loadTexts:
    ntcSiMpeDeAlarms.setStatus("current")
_NtcSiMpeDeAlDataOverflow_Type = NtcAlarmState
_NtcSiMpeDeAlDataOverflow_Object = MibScalar
ntcSiMpeDeAlDataOverflow = _NtcSiMpeDeAlDataOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 1, 3, 1),
    _NtcSiMpeDeAlDataOverflow_Type()
)
ntcSiMpeDeAlDataOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcSiMpeDeAlDataOverflow.setStatus("current")
_NtcSiMpeDeConformance_ObjectIdentity = ObjectIdentity
ntcSiMpeDeConformance = _NtcSiMpeDeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 2)
)
if mibBuilder.loadTexts:
    ntcSiMpeDeConformance.setStatus("current")
_NtcSiMpeDeConfCompliance_ObjectIdentity = ObjectIdentity
ntcSiMpeDeConfCompliance = _NtcSiMpeDeConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 2, 1)
)
if mibBuilder.loadTexts:
    ntcSiMpeDeConfCompliance.setStatus("current")
_NtcSiMpeDeConfGroup_ObjectIdentity = ObjectIdentity
ntcSiMpeDeConfGroup = _NtcSiMpeDeConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 2, 2)
)
if mibBuilder.loadTexts:
    ntcSiMpeDeConfGroup.setStatus("current")

# Managed Objects groups

ntcSiMpeDeConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 2, 2, 1)
)
ntcSiMpeDeConfGrpV1Standard.setObjects(
      *(("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeEnable"),
        ("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeDataPid"),
        ("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeMacAddress"),
        ("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeCounterReset"),
        ("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeForwardBitRate"),
        ("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeDroppedPackets"),
        ("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeAlDataOverflow"))
)
if mibBuilder.loadTexts:
    ntcSiMpeDeConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcSiMpeDeConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8500, 2, 1, 1)
)
ntcSiMpeDeConfCompV1Standard.setObjects(
    ("NEWTEC-SIMPEDECAPS-MIB", "ntcSiMpeDeConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcSiMpeDeConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-SIMPEDECAPS-MIB",
    **{"ntcSiMpeDecaps": ntcSiMpeDecaps,
       "ntcSiMpeDeObjects": ntcSiMpeDeObjects,
       "ntcSiMpeDeConfiguration": ntcSiMpeDeConfiguration,
       "ntcSiMpeDeEnable": ntcSiMpeDeEnable,
       "ntcSiMpeDeDataPid": ntcSiMpeDeDataPid,
       "ntcSiMpeDeMacAddress": ntcSiMpeDeMacAddress,
       "ntcSiMpeDeMonitoring": ntcSiMpeDeMonitoring,
       "ntcSiMpeDeCounterReset": ntcSiMpeDeCounterReset,
       "ntcSiMpeDeForwardBitRate": ntcSiMpeDeForwardBitRate,
       "ntcSiMpeDeDroppedPackets": ntcSiMpeDeDroppedPackets,
       "ntcSiMpeDeAlarms": ntcSiMpeDeAlarms,
       "ntcSiMpeDeAlDataOverflow": ntcSiMpeDeAlDataOverflow,
       "ntcSiMpeDeConformance": ntcSiMpeDeConformance,
       "ntcSiMpeDeConfCompliance": ntcSiMpeDeConfCompliance,
       "ntcSiMpeDeConfCompV1Standard": ntcSiMpeDeConfCompV1Standard,
       "ntcSiMpeDeConfGroup": ntcSiMpeDeConfGroup,
       "ntcSiMpeDeConfGrpV1Standard": ntcSiMpeDeConfGrpV1Standard}
)
