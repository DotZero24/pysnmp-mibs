# SNMP MIB module (ELTEX-MES-ISS-INTERFACES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-INTERFACES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:26 2025
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

(issPortCtrlEntry,) = mibBuilder.importSymbols(
    "ARICENT-ISS-MIB",
    "issPortCtrlEntry")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssInterfacesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4)
)
if mibBuilder.loadTexts:
    eltMesIssInterfacesMIB.setRevisions(
        ("2022-10-19 00:00",
         "2021-03-29 00:00",
         "2021-01-19 00:00",
         "2018-12-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssPortCtrlAutoNegBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("default", 0),
          ("unknown", 1),
          ("half10M", 2),
          ("full10M", 3),
          ("half100M", 4),
          ("full100M", 5),
          ("full1G", 7))
    )


# MIB Managed Objects in the order of their OIDs

_EltMesIssInterfacesObjects_ObjectIdentity = ObjectIdentity
eltMesIssInterfacesObjects = _EltMesIssInterfacesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1)
)
_EltMesIssInterfacesGlobals_ObjectIdentity = ObjectIdentity
eltMesIssInterfacesGlobals = _EltMesIssInterfacesGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 1)
)
_EltMesIssDefaultInterface_Type = Integer32
_EltMesIssDefaultInterface_Object = MibScalar
eltMesIssDefaultInterface = _EltMesIssDefaultInterface_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 1, 1),
    _EltMesIssDefaultInterface_Type()
)
eltMesIssDefaultInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDefaultInterface.setStatus("current")
_EltMesIssInterfacesConfig_ObjectIdentity = ObjectIdentity
eltMesIssInterfacesConfig = _EltMesIssInterfacesConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2)
)
_EltMesIssPortCtrlTable_Object = MibTable
eltMesIssPortCtrlTable = _EltMesIssPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssPortCtrlTable.setStatus("current")
_EltMesIssPortCtrlEntry_Object = MibTableRow
eltMesIssPortCtrlEntry = _EltMesIssPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssPortCtrlEntry.setStatus("current")


class _EltMesIssPortCtrlAdminComboMode_Type(Integer32):
    """Custom type eltMesIssPortCtrlAdminComboMode based on Integer32"""
    defaultValue = 3

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
        *(("force-fiber", 1),
          ("force-copper", 2),
          ("prefer-fiber", 3),
          ("prefer-copper", 4))
    )


_EltMesIssPortCtrlAdminComboMode_Type.__name__ = "Integer32"
_EltMesIssPortCtrlAdminComboMode_Object = MibTableColumn
eltMesIssPortCtrlAdminComboMode = _EltMesIssPortCtrlAdminComboMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1, 1, 1),
    _EltMesIssPortCtrlAdminComboMode_Type()
)
eltMesIssPortCtrlAdminComboMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssPortCtrlAdminComboMode.setStatus("current")


class _EltMesIssPortCtrlOperComboMode_Type(Integer32):
    """Custom type eltMesIssPortCtrlOperComboMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("copper", 2),
          ("unknown", 3))
    )


_EltMesIssPortCtrlOperComboMode_Type.__name__ = "Integer32"
_EltMesIssPortCtrlOperComboMode_Object = MibTableColumn
eltMesIssPortCtrlOperComboMode = _EltMesIssPortCtrlOperComboMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1, 1, 2),
    _EltMesIssPortCtrlOperComboMode_Type()
)
eltMesIssPortCtrlOperComboMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPortCtrlOperComboMode.setStatus("current")
_EltMesIssPortCtrlAutoNegAdminLocal_Type = EltMesIssPortCtrlAutoNegBits
_EltMesIssPortCtrlAutoNegAdminLocal_Object = MibTableColumn
eltMesIssPortCtrlAutoNegAdminLocal = _EltMesIssPortCtrlAutoNegAdminLocal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1, 1, 3),
    _EltMesIssPortCtrlAutoNegAdminLocal_Type()
)
eltMesIssPortCtrlAutoNegAdminLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssPortCtrlAutoNegAdminLocal.setStatus("current")
_EltMesIssPortCtrlAutoNegOperLocal_Type = EltMesIssPortCtrlAutoNegBits
_EltMesIssPortCtrlAutoNegOperLocal_Object = MibTableColumn
eltMesIssPortCtrlAutoNegOperLocal = _EltMesIssPortCtrlAutoNegOperLocal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1, 1, 4),
    _EltMesIssPortCtrlAutoNegOperLocal_Type()
)
eltMesIssPortCtrlAutoNegOperLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPortCtrlAutoNegOperLocal.setStatus("current")


class _EltMesIssPortCtrlTransceiverType_Type(Integer32):
    """Custom type eltMesIssPortCtrlTransceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiberOptics", 2),
          ("combo", 3))
    )


_EltMesIssPortCtrlTransceiverType_Type.__name__ = "Integer32"
_EltMesIssPortCtrlTransceiverType_Object = MibTableColumn
eltMesIssPortCtrlTransceiverType = _EltMesIssPortCtrlTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1, 1, 5),
    _EltMesIssPortCtrlTransceiverType_Type()
)
eltMesIssPortCtrlTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPortCtrlTransceiverType.setStatus("current")


class _EltMesIssPortCtrlType_Type(Integer32):
    """Custom type eltMesIssPortCtrlType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eth10M", 1),
          ("eth100M", 2),
          ("eth1000M", 3),
          ("eth2500M", 4),
          ("eth5G", 5),
          ("eth10G", 6),
          ("eth20G", 7),
          ("eth40G", 8),
          ("eth100G", 9),
          ("unknown", 10))
    )


_EltMesIssPortCtrlType_Type.__name__ = "Integer32"
_EltMesIssPortCtrlType_Object = MibTableColumn
eltMesIssPortCtrlType = _EltMesIssPortCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 1, 1, 6),
    _EltMesIssPortCtrlType_Type()
)
eltMesIssPortCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPortCtrlType.setStatus("current")
_EltMesIssHardwareSerdesRxConfigTable_Object = MibTable
eltMesIssHardwareSerdesRxConfigTable = _EltMesIssHardwareSerdesRxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltMesIssHardwareSerdesRxConfigTable.setStatus("current")
_EltMesIssHardwareSerdesRxConfigEntry_Object = MibTableRow
eltMesIssHardwareSerdesRxConfigEntry = _EltMesIssHardwareSerdesRxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 2, 1)
)
eltMesIssHardwareSerdesRxConfigEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-INTERFACES-MIB", "eltMesIssHardwareSerdesRxConfigIfIndex"),
    (0, "ELTEX-MES-ISS-INTERFACES-MIB", "eltMesIssHardwareSerdesRxConfigLaneNumber"),
)
if mibBuilder.loadTexts:
    eltMesIssHardwareSerdesRxConfigEntry.setStatus("current")
_EltMesIssHardwareSerdesRxConfigIfIndex_Type = Integer32
_EltMesIssHardwareSerdesRxConfigIfIndex_Object = MibTableColumn
eltMesIssHardwareSerdesRxConfigIfIndex = _EltMesIssHardwareSerdesRxConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 2, 1, 1),
    _EltMesIssHardwareSerdesRxConfigIfIndex_Type()
)
eltMesIssHardwareSerdesRxConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssHardwareSerdesRxConfigIfIndex.setStatus("current")
_EltMesIssHardwareSerdesRxConfigLaneNumber_Type = Integer32
_EltMesIssHardwareSerdesRxConfigLaneNumber_Object = MibTableColumn
eltMesIssHardwareSerdesRxConfigLaneNumber = _EltMesIssHardwareSerdesRxConfigLaneNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 2, 1, 2),
    _EltMesIssHardwareSerdesRxConfigLaneNumber_Type()
)
eltMesIssHardwareSerdesRxConfigLaneNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssHardwareSerdesRxConfigLaneNumber.setStatus("current")


class _EltMesIssHardwareSerdesRxConfigUserParamsEnable_Type(TruthValue):
    """Custom type eltMesIssHardwareSerdesRxConfigUserParamsEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssHardwareSerdesRxConfigUserParamsEnable_Type.__name__ = "TruthValue"
_EltMesIssHardwareSerdesRxConfigUserParamsEnable_Object = MibTableColumn
eltMesIssHardwareSerdesRxConfigUserParamsEnable = _EltMesIssHardwareSerdesRxConfigUserParamsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 2, 1, 3),
    _EltMesIssHardwareSerdesRxConfigUserParamsEnable_Type()
)
eltMesIssHardwareSerdesRxConfigUserParamsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssHardwareSerdesRxConfigUserParamsEnable.setStatus("current")


class _EltMesIssHardwareSerdesRxConfigLeq_Type(Integer32):
    """Custom type eltMesIssHardwareSerdesRxConfigLeq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_EltMesIssHardwareSerdesRxConfigLeq_Type.__name__ = "Integer32"
_EltMesIssHardwareSerdesRxConfigLeq_Object = MibTableColumn
eltMesIssHardwareSerdesRxConfigLeq = _EltMesIssHardwareSerdesRxConfigLeq_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4, 1, 2, 2, 1, 4),
    _EltMesIssHardwareSerdesRxConfigLeq_Type()
)
eltMesIssHardwareSerdesRxConfigLeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssHardwareSerdesRxConfigLeq.setStatus("current")
issPortCtrlEntry.registerAugmentions(
    ("ELTEX-MES-ISS-INTERFACES-MIB",
     "eltMesIssPortCtrlEntry")
)
eltMesIssPortCtrlEntry.setIndexNames(*issPortCtrlEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-INTERFACES-MIB",
    **{"EltMesIssPortCtrlAutoNegBits": EltMesIssPortCtrlAutoNegBits,
       "eltMesIssInterfacesMIB": eltMesIssInterfacesMIB,
       "eltMesIssInterfacesObjects": eltMesIssInterfacesObjects,
       "eltMesIssInterfacesGlobals": eltMesIssInterfacesGlobals,
       "eltMesIssDefaultInterface": eltMesIssDefaultInterface,
       "eltMesIssInterfacesConfig": eltMesIssInterfacesConfig,
       "eltMesIssPortCtrlTable": eltMesIssPortCtrlTable,
       "eltMesIssPortCtrlEntry": eltMesIssPortCtrlEntry,
       "eltMesIssPortCtrlAdminComboMode": eltMesIssPortCtrlAdminComboMode,
       "eltMesIssPortCtrlOperComboMode": eltMesIssPortCtrlOperComboMode,
       "eltMesIssPortCtrlAutoNegAdminLocal": eltMesIssPortCtrlAutoNegAdminLocal,
       "eltMesIssPortCtrlAutoNegOperLocal": eltMesIssPortCtrlAutoNegOperLocal,
       "eltMesIssPortCtrlTransceiverType": eltMesIssPortCtrlTransceiverType,
       "eltMesIssPortCtrlType": eltMesIssPortCtrlType,
       "eltMesIssHardwareSerdesRxConfigTable": eltMesIssHardwareSerdesRxConfigTable,
       "eltMesIssHardwareSerdesRxConfigEntry": eltMesIssHardwareSerdesRxConfigEntry,
       "eltMesIssHardwareSerdesRxConfigIfIndex": eltMesIssHardwareSerdesRxConfigIfIndex,
       "eltMesIssHardwareSerdesRxConfigLaneNumber": eltMesIssHardwareSerdesRxConfigLaneNumber,
       "eltMesIssHardwareSerdesRxConfigUserParamsEnable": eltMesIssHardwareSerdesRxConfigUserParamsEnable,
       "eltMesIssHardwareSerdesRxConfigLeq": eltMesIssHardwareSerdesRxConfigLeq}
)
