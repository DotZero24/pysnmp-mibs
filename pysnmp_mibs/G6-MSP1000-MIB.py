# SNMP MIB module (G6-MSP1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-MSP1000-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:07 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Msp1000_ObjectIdentity = ObjectIdentity
msp1000 = _Msp1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94)
)
_SystemConfigTable_Object = MibTable
systemConfigTable = _SystemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 1)
)
if mibBuilder.loadTexts:
    systemConfigTable.setStatus("current")
_SystemConfigEntry_Object = MibTableRow
systemConfigEntry = _SystemConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 1, 1)
)
systemConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "systemConfigIndex"),
)
if mibBuilder.loadTexts:
    systemConfigEntry.setStatus("current")


class _SystemConfigIndex_Type(Integer32):
    """Custom type systemConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_SystemConfigIndex_Type.__name__ = "Integer32"
_SystemConfigIndex_Object = MibTableColumn
systemConfigIndex = _SystemConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 1, 1, 1),
    _SystemConfigIndex_Type()
)
systemConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemConfigIndex.setStatus("current")


class _SystemConfigNmsOperationMode_Type(Integer32):
    """Custom type systemConfigNmsOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passive", 0),
          ("active", 1))
    )


_SystemConfigNmsOperationMode_Type.__name__ = "Integer32"
_SystemConfigNmsOperationMode_Object = MibTableColumn
systemConfigNmsOperationMode = _SystemConfigNmsOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 1, 1, 2),
    _SystemConfigNmsOperationMode_Type()
)
systemConfigNmsOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigNmsOperationMode.setStatus("current")


class _SystemConfigCoreMode_Type(Integer32):
    """Custom type systemConfigCoreMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2", 1))
    )


_SystemConfigCoreMode_Type.__name__ = "Integer32"
_SystemConfigCoreMode_Object = MibTableColumn
systemConfigCoreMode = _SystemConfigCoreMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 1, 1, 3),
    _SystemConfigCoreMode_Type()
)
systemConfigCoreMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigCoreMode.setStatus("current")
_SystemConfigNodeId_Type = Unsigned32
_SystemConfigNodeId_Object = MibTableColumn
systemConfigNodeId = _SystemConfigNodeId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 1, 1, 4),
    _SystemConfigNodeId_Type()
)
systemConfigNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigNodeId.setStatus("current")


class _SystemConfigDisableLegacyAccess_Type(Integer32):
    """Custom type systemConfigDisableLegacyAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemConfigDisableLegacyAccess_Type.__name__ = "Integer32"
_SystemConfigDisableLegacyAccess_Object = MibTableColumn
systemConfigDisableLegacyAccess = _SystemConfigDisableLegacyAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 1, 1, 5),
    _SystemConfigDisableLegacyAccess_Type()
)
systemConfigDisableLegacyAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigDisableLegacyAccess.setStatus("current")
_SlotConfigTable_Object = MibTable
slotConfigTable = _SlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2)
)
if mibBuilder.loadTexts:
    slotConfigTable.setStatus("current")
_SlotConfigEntry_Object = MibTableRow
slotConfigEntry = _SlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1)
)
slotConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "slotConfigIndex"),
)
if mibBuilder.loadTexts:
    slotConfigEntry.setStatus("current")


class _SlotConfigIndex_Type(Integer32):
    """Custom type slotConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_SlotConfigIndex_Type.__name__ = "Integer32"
_SlotConfigIndex_Object = MibTableColumn
slotConfigIndex = _SlotConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1, 1),
    _SlotConfigIndex_Type()
)
slotConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotConfigIndex.setStatus("current")


class _SlotConfigModule_Type(Integer32):
    """Custom type slotConfigModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              50,
              56,
              57,
              60,
              61,
              62,
              63,
              65,
              66,
              72,
              87,
              88,
              104,
              105,
              106,
              108,
              109,
              110)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("empty", 1),
          ("legacy", 2),
          ("passive", 3),
          ("fc8Filter", 10),
          ("fc8aFilter", 11),
          ("fc8xFilter", 12),
          ("b4sFilter", 13),
          ("b4xFilter", 14),
          ("b8mFilter", 15),
          ("b8dFilter", 16),
          ("fd4Filter", 17),
          ("dc1Filter", 18),
          ("se1", 19),
          ("tdm4", 50),
          ("m2g", 56),
          ("wcm2", 57),
          ("xcm1", 60),
          ("x2g", 61),
          ("t4g", 62),
          ("txg", 63),
          ("nm1", 65),
          ("nm2", 66),
          ("os1", 72),
          ("cxg", 87),
          ("cxgp", 88),
          ("om1", 104),
          ("em2", 105),
          ("lp1", 106),
          ("nm3", 108),
          ("em3", 109),
          ("nm3p", 110))
    )


_SlotConfigModule_Type.__name__ = "Integer32"
_SlotConfigModule_Object = MibTableColumn
slotConfigModule = _SlotConfigModule_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1, 2),
    _SlotConfigModule_Type()
)
slotConfigModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigModule.setStatus("current")


class _SlotConfigSparepartMode_Type(Integer32):
    """Custom type slotConfigSparepartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SlotConfigSparepartMode_Type.__name__ = "Integer32"
_SlotConfigSparepartMode_Object = MibTableColumn
slotConfigSparepartMode = _SlotConfigSparepartMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1, 3),
    _SlotConfigSparepartMode_Type()
)
slotConfigSparepartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigSparepartMode.setStatus("current")
_SlotConfigPort1Alias_Type = DisplayString
_SlotConfigPort1Alias_Object = MibTableColumn
slotConfigPort1Alias = _SlotConfigPort1Alias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1, 4),
    _SlotConfigPort1Alias_Type()
)
slotConfigPort1Alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigPort1Alias.setStatus("current")
_SlotConfigPort2Alias_Type = DisplayString
_SlotConfigPort2Alias_Object = MibTableColumn
slotConfigPort2Alias = _SlotConfigPort2Alias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1, 5),
    _SlotConfigPort2Alias_Type()
)
slotConfigPort2Alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigPort2Alias.setStatus("current")
_SlotConfigPort3Alias_Type = DisplayString
_SlotConfigPort3Alias_Object = MibTableColumn
slotConfigPort3Alias = _SlotConfigPort3Alias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1, 6),
    _SlotConfigPort3Alias_Type()
)
slotConfigPort3Alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigPort3Alias.setStatus("current")
_SlotConfigPort4Alias_Type = DisplayString
_SlotConfigPort4Alias_Object = MibTableColumn
slotConfigPort4Alias = _SlotConfigPort4Alias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 2, 1, 7),
    _SlotConfigPort4Alias_Type()
)
slotConfigPort4Alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigPort4Alias.setStatus("current")
_X2gConfigTable_Object = MibTable
x2gConfigTable = _X2gConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3)
)
if mibBuilder.loadTexts:
    x2gConfigTable.setStatus("current")
_X2gConfigEntry_Object = MibTableRow
x2gConfigEntry = _X2gConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1)
)
x2gConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "x2gConfigIndex"),
)
if mibBuilder.loadTexts:
    x2gConfigEntry.setStatus("current")


class _X2gConfigIndex_Type(Integer32):
    """Custom type x2gConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_X2gConfigIndex_Type.__name__ = "Integer32"
_X2gConfigIndex_Object = MibTableColumn
x2gConfigIndex = _X2gConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 1),
    _X2gConfigIndex_Type()
)
x2gConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    x2gConfigIndex.setStatus("current")


class _X2gConfigPort1Datarate_Type(Integer32):
    """Custom type x2gConfigPort1Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("fix100", 1),
          ("ms100mEth", 2),
          ("oc3", 3),
          ("escon", 4),
          ("sdi", 5),
          ("oc12", 6),
          ("ms1xFc", 7),
          ("ms1gEth", 8),
          ("hdtv", 9),
          ("ms2xFc", 10),
          ("oc48", 11),
          ("m2g", 12),
          ("otu1", 13))
    )


_X2gConfigPort1Datarate_Type.__name__ = "Integer32"
_X2gConfigPort1Datarate_Object = MibTableColumn
x2gConfigPort1Datarate = _X2gConfigPort1Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 2),
    _X2gConfigPort1Datarate_Type()
)
x2gConfigPort1Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigPort1Datarate.setStatus("current")


class _X2gConfigPort2Datarate_Type(Integer32):
    """Custom type x2gConfigPort2Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("fix100", 1),
          ("ms100mEth", 2),
          ("oc3", 3),
          ("escon", 4),
          ("sdi", 5),
          ("oc12", 6),
          ("ms1xFc", 7),
          ("ms1gEth", 8),
          ("hdtv", 9),
          ("ms2xFc", 10),
          ("oc48", 11),
          ("m2g", 12),
          ("otu1", 13))
    )


_X2gConfigPort2Datarate_Type.__name__ = "Integer32"
_X2gConfigPort2Datarate_Object = MibTableColumn
x2gConfigPort2Datarate = _X2gConfigPort2Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 3),
    _X2gConfigPort2Datarate_Type()
)
x2gConfigPort2Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigPort2Datarate.setStatus("current")


class _X2gConfigPort3Datarate_Type(Integer32):
    """Custom type x2gConfigPort3Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("fix100", 1),
          ("ms100mEth", 2),
          ("oc3", 3),
          ("escon", 4),
          ("sdi", 5),
          ("oc12", 6),
          ("ms1xFc", 7),
          ("ms1gEth", 8),
          ("hdtv", 9),
          ("ms2xFc", 10),
          ("oc48", 11),
          ("m2g", 12),
          ("otu1", 13))
    )


_X2gConfigPort3Datarate_Type.__name__ = "Integer32"
_X2gConfigPort3Datarate_Object = MibTableColumn
x2gConfigPort3Datarate = _X2gConfigPort3Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 4),
    _X2gConfigPort3Datarate_Type()
)
x2gConfigPort3Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigPort3Datarate.setStatus("current")


class _X2gConfigPort4Datarate_Type(Integer32):
    """Custom type x2gConfigPort4Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("fix100", 1),
          ("ms100mEth", 2),
          ("oc3", 3),
          ("escon", 4),
          ("sdi", 5),
          ("oc12", 6),
          ("ms1xFc", 7),
          ("ms1gEth", 8),
          ("hdtv", 9),
          ("ms2xFc", 10),
          ("oc48", 11),
          ("m2g", 12),
          ("otu1", 13))
    )


_X2gConfigPort4Datarate_Type.__name__ = "Integer32"
_X2gConfigPort4Datarate_Object = MibTableColumn
x2gConfigPort4Datarate = _X2gConfigPort4Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 5),
    _X2gConfigPort4Datarate_Type()
)
x2gConfigPort4Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigPort4Datarate.setStatus("current")


class _X2gConfigCrossConnect_Type(Integer32):
    """Custom type x2gConfigCrossConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5,
              9,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 0),
          ("alternate", 1),
          ("backup", 5),
          ("ringBackupWest", 9),
          ("multicast", 11),
          ("dropContinue", 12),
          ("addDropWest", 13),
          ("addDropEast", 14),
          ("ringBackupEast", 15),
          ("crossOver", 16),
          ("switchP1P2", 17),
          ("switchP1P3", 18),
          ("switchP1P4", 19),
          ("normal", 20),
          ("bertPort4", 21))
    )


_X2gConfigCrossConnect_Type.__name__ = "Integer32"
_X2gConfigCrossConnect_Object = MibTableColumn
x2gConfigCrossConnect = _X2gConfigCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 6),
    _X2gConfigCrossConnect_Type()
)
x2gConfigCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigCrossConnect.setStatus("current")


class _X2gConfigDeactivatePort1_Type(Integer32):
    """Custom type x2gConfigDeactivatePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X2gConfigDeactivatePort1_Type.__name__ = "Integer32"
_X2gConfigDeactivatePort1_Object = MibTableColumn
x2gConfigDeactivatePort1 = _X2gConfigDeactivatePort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 7),
    _X2gConfigDeactivatePort1_Type()
)
x2gConfigDeactivatePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigDeactivatePort1.setStatus("current")


class _X2gConfigDeactivatePort2_Type(Integer32):
    """Custom type x2gConfigDeactivatePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X2gConfigDeactivatePort2_Type.__name__ = "Integer32"
_X2gConfigDeactivatePort2_Object = MibTableColumn
x2gConfigDeactivatePort2 = _X2gConfigDeactivatePort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 8),
    _X2gConfigDeactivatePort2_Type()
)
x2gConfigDeactivatePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigDeactivatePort2.setStatus("current")


class _X2gConfigDeactivatePort3_Type(Integer32):
    """Custom type x2gConfigDeactivatePort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X2gConfigDeactivatePort3_Type.__name__ = "Integer32"
_X2gConfigDeactivatePort3_Object = MibTableColumn
x2gConfigDeactivatePort3 = _X2gConfigDeactivatePort3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 9),
    _X2gConfigDeactivatePort3_Type()
)
x2gConfigDeactivatePort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigDeactivatePort3.setStatus("current")


class _X2gConfigDeactivatePort4_Type(Integer32):
    """Custom type x2gConfigDeactivatePort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X2gConfigDeactivatePort4_Type.__name__ = "Integer32"
_X2gConfigDeactivatePort4_Object = MibTableColumn
x2gConfigDeactivatePort4 = _X2gConfigDeactivatePort4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 10),
    _X2gConfigDeactivatePort4_Type()
)
x2gConfigDeactivatePort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigDeactivatePort4.setStatus("current")


class _X2gConfigFrontPanelMode_Type(Integer32):
    """Custom type x2gConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_X2gConfigFrontPanelMode_Type.__name__ = "Integer32"
_X2gConfigFrontPanelMode_Object = MibTableColumn
x2gConfigFrontPanelMode = _X2gConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 11),
    _X2gConfigFrontPanelMode_Type()
)
x2gConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigFrontPanelMode.setStatus("current")


class _X2gConfigLossOfSignalHandling_Type(Integer32):
    """Custom type x2gConfigLossOfSignalHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("percolate", 1))
    )


_X2gConfigLossOfSignalHandling_Type.__name__ = "Integer32"
_X2gConfigLossOfSignalHandling_Object = MibTableColumn
x2gConfigLossOfSignalHandling = _X2gConfigLossOfSignalHandling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 12),
    _X2gConfigLossOfSignalHandling_Type()
)
x2gConfigLossOfSignalHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigLossOfSignalHandling.setStatus("current")


class _X2gConfigOptimizedFor8b10b_Type(Integer32):
    """Custom type x2gConfigOptimizedFor8b10b based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X2gConfigOptimizedFor8b10b_Type.__name__ = "Integer32"
_X2gConfigOptimizedFor8b10b_Object = MibTableColumn
x2gConfigOptimizedFor8b10b = _X2gConfigOptimizedFor8b10b_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 13),
    _X2gConfigOptimizedFor8b10b_Type()
)
x2gConfigOptimizedFor8b10b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigOptimizedFor8b10b.setStatus("current")


class _X2gConfigBertPattern_Type(Integer32):
    """Custom type x2gConfigBertPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ms27", 0),
          ("ms223", 2),
          ("ms231", 3),
          ("cjPat", 4),
          ("crPat", 5),
          ("ms8b10bCnt", 6))
    )


_X2gConfigBertPattern_Type.__name__ = "Integer32"
_X2gConfigBertPattern_Object = MibTableColumn
x2gConfigBertPattern = _X2gConfigBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 14),
    _X2gConfigBertPattern_Type()
)
x2gConfigBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigBertPattern.setStatus("current")


class _X2gConfigSfpDeltaInterval_Type(Integer32):
    """Custom type x2gConfigSfpDeltaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1Sec", 1),
          ("ms5Sec", 2),
          ("ms10Sec", 3),
          ("ms30Sec", 4),
          ("ms60Sec", 5),
          ("ms240Sec", 6))
    )


_X2gConfigSfpDeltaInterval_Type.__name__ = "Integer32"
_X2gConfigSfpDeltaInterval_Object = MibTableColumn
x2gConfigSfpDeltaInterval = _X2gConfigSfpDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 15),
    _X2gConfigSfpDeltaInterval_Type()
)
x2gConfigSfpDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigSfpDeltaInterval.setStatus("current")


class _X2gConfigSfpDeltaThreshold_Type(Integer32):
    """Custom type x2gConfigSfpDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ms05Db", 0),
          ("ms1Db", 1),
          ("ms15Db", 2),
          ("ms2Db", 3),
          ("ms3Db", 4),
          ("ms5Db", 5))
    )


_X2gConfigSfpDeltaThreshold_Type.__name__ = "Integer32"
_X2gConfigSfpDeltaThreshold_Object = MibTableColumn
x2gConfigSfpDeltaThreshold = _X2gConfigSfpDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 16),
    _X2gConfigSfpDeltaThreshold_Type()
)
x2gConfigSfpDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigSfpDeltaThreshold.setStatus("current")


class _X2gConfigBackupTrigger_Type(Integer32):
    """Custom type x2gConfigBackupTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("signalLoss", 1),
          ("clockLoss", 2))
    )


_X2gConfigBackupTrigger_Type.__name__ = "Integer32"
_X2gConfigBackupTrigger_Object = MibTableColumn
x2gConfigBackupTrigger = _X2gConfigBackupTrigger_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 17),
    _X2gConfigBackupTrigger_Type()
)
x2gConfigBackupTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigBackupTrigger.setStatus("current")


class _X2gConfigStayWithLastLink_Type(Integer32):
    """Custom type x2gConfigStayWithLastLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X2gConfigStayWithLastLink_Type.__name__ = "Integer32"
_X2gConfigStayWithLastLink_Object = MibTableColumn
x2gConfigStayWithLastLink = _X2gConfigStayWithLastLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 18),
    _X2gConfigStayWithLastLink_Type()
)
x2gConfigStayWithLastLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigStayWithLastLink.setStatus("current")


class _X2gConfigBackupEnd_Type(Integer32):
    """Custom type x2gConfigBackupEnd based on Integer32"""
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
        *(("noDelay", 0),
          ("ms15Seconds", 1),
          ("ms15Minutes", 2),
          ("manually", 3))
    )


_X2gConfigBackupEnd_Type.__name__ = "Integer32"
_X2gConfigBackupEnd_Object = MibTableColumn
x2gConfigBackupEnd = _X2gConfigBackupEnd_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 19),
    _X2gConfigBackupEnd_Type()
)
x2gConfigBackupEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigBackupEnd.setStatus("current")


class _X2gConfigPermitLinkOverride_Type(Integer32):
    """Custom type x2gConfigPermitLinkOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_X2gConfigPermitLinkOverride_Type.__name__ = "Integer32"
_X2gConfigPermitLinkOverride_Object = MibTableColumn
x2gConfigPermitLinkOverride = _X2gConfigPermitLinkOverride_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 3, 1, 20),
    _X2gConfigPermitLinkOverride_Type()
)
x2gConfigPermitLinkOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x2gConfigPermitLinkOverride.setStatus("current")
_TxgConfigTable_Object = MibTable
txgConfigTable = _TxgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4)
)
if mibBuilder.loadTexts:
    txgConfigTable.setStatus("current")
_TxgConfigEntry_Object = MibTableRow
txgConfigEntry = _TxgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1)
)
txgConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "txgConfigIndex"),
)
if mibBuilder.loadTexts:
    txgConfigEntry.setStatus("current")


class _TxgConfigIndex_Type(Integer32):
    """Custom type txgConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_TxgConfigIndex_Type.__name__ = "Integer32"
_TxgConfigIndex_Object = MibTableColumn
txgConfigIndex = _TxgConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 1),
    _TxgConfigIndex_Type()
)
txgConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txgConfigIndex.setStatus("current")


class _TxgConfigTxgDatarate_Type(Integer32):
    """Custom type txgConfigTxgDatarate based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("oc192", 1),
          ("ms10gEth", 2),
          ("oc192Fec", 3),
          ("otu2", 4),
          ("ms10xFc", 5),
          ("otu2e", 6),
          ("otu1f", 7),
          ("otu2f", 8))
    )


_TxgConfigTxgDatarate_Type.__name__ = "Integer32"
_TxgConfigTxgDatarate_Object = MibTableColumn
txgConfigTxgDatarate = _TxgConfigTxgDatarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 2),
    _TxgConfigTxgDatarate_Type()
)
txgConfigTxgDatarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigTxgDatarate.setStatus("current")


class _TxgConfigTxgOperationMode_Type(Integer32):
    """Custom type txgConfigTxgOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("transponder", 2),
          ("repeater", 3),
          ("bertPort1", 4),
          ("bertPort2", 5))
    )


_TxgConfigTxgOperationMode_Type.__name__ = "Integer32"
_TxgConfigTxgOperationMode_Object = MibTableColumn
txgConfigTxgOperationMode = _TxgConfigTxgOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 3),
    _TxgConfigTxgOperationMode_Type()
)
txgConfigTxgOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigTxgOperationMode.setStatus("current")


class _TxgConfigPort1ItuChannel_Type(Integer32):
    """Custom type txgConfigPort1ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_TxgConfigPort1ItuChannel_Type.__name__ = "Integer32"
_TxgConfigPort1ItuChannel_Object = MibTableColumn
txgConfigPort1ItuChannel = _TxgConfigPort1ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 4),
    _TxgConfigPort1ItuChannel_Type()
)
txgConfigPort1ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigPort1ItuChannel.setStatus("current")


class _TxgConfigPort2ItuChannel_Type(Integer32):
    """Custom type txgConfigPort2ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_TxgConfigPort2ItuChannel_Type.__name__ = "Integer32"
_TxgConfigPort2ItuChannel_Object = MibTableColumn
txgConfigPort2ItuChannel = _TxgConfigPort2ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 5),
    _TxgConfigPort2ItuChannel_Type()
)
txgConfigPort2ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigPort2ItuChannel.setStatus("current")


class _TxgConfigDeactivatePort1_Type(Integer32):
    """Custom type txgConfigDeactivatePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TxgConfigDeactivatePort1_Type.__name__ = "Integer32"
_TxgConfigDeactivatePort1_Object = MibTableColumn
txgConfigDeactivatePort1 = _TxgConfigDeactivatePort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 6),
    _TxgConfigDeactivatePort1_Type()
)
txgConfigDeactivatePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigDeactivatePort1.setStatus("current")


class _TxgConfigDeactivatePort2_Type(Integer32):
    """Custom type txgConfigDeactivatePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TxgConfigDeactivatePort2_Type.__name__ = "Integer32"
_TxgConfigDeactivatePort2_Object = MibTableColumn
txgConfigDeactivatePort2 = _TxgConfigDeactivatePort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 7),
    _TxgConfigDeactivatePort2_Type()
)
txgConfigDeactivatePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigDeactivatePort2.setStatus("current")


class _TxgConfigFrontPanelMode_Type(Integer32):
    """Custom type txgConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_TxgConfigFrontPanelMode_Type.__name__ = "Integer32"
_TxgConfigFrontPanelMode_Object = MibTableColumn
txgConfigFrontPanelMode = _TxgConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 8),
    _TxgConfigFrontPanelMode_Type()
)
txgConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigFrontPanelMode.setStatus("current")


class _TxgConfigLossOfSignalHandling_Type(Integer32):
    """Custom type txgConfigLossOfSignalHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("percolate", 1))
    )


_TxgConfigLossOfSignalHandling_Type.__name__ = "Integer32"
_TxgConfigLossOfSignalHandling_Object = MibTableColumn
txgConfigLossOfSignalHandling = _TxgConfigLossOfSignalHandling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 9),
    _TxgConfigLossOfSignalHandling_Type()
)
txgConfigLossOfSignalHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigLossOfSignalHandling.setStatus("current")


class _TxgConfigBertPattern_Type(Integer32):
    """Custom type txgConfigBertPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ms27", 0),
          ("ms223", 2),
          ("ms231", 3),
          ("cjPat", 4),
          ("crPat", 5),
          ("ms8b10bCnt", 6))
    )


_TxgConfigBertPattern_Type.__name__ = "Integer32"
_TxgConfigBertPattern_Object = MibTableColumn
txgConfigBertPattern = _TxgConfigBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 10),
    _TxgConfigBertPattern_Type()
)
txgConfigBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigBertPattern.setStatus("current")


class _TxgConfigSfpDeltaInterval_Type(Integer32):
    """Custom type txgConfigSfpDeltaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1Sec", 1),
          ("ms5Sec", 2),
          ("ms10Sec", 3),
          ("ms30Sec", 4),
          ("ms60Sec", 5),
          ("ms240Sec", 6))
    )


_TxgConfigSfpDeltaInterval_Type.__name__ = "Integer32"
_TxgConfigSfpDeltaInterval_Object = MibTableColumn
txgConfigSfpDeltaInterval = _TxgConfigSfpDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 11),
    _TxgConfigSfpDeltaInterval_Type()
)
txgConfigSfpDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigSfpDeltaInterval.setStatus("current")


class _TxgConfigSfpDeltaThreshold_Type(Integer32):
    """Custom type txgConfigSfpDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ms05Db", 0),
          ("ms1Db", 1),
          ("ms15Db", 2),
          ("ms2Db", 3),
          ("ms3Db", 4),
          ("ms5Db", 5))
    )


_TxgConfigSfpDeltaThreshold_Type.__name__ = "Integer32"
_TxgConfigSfpDeltaThreshold_Object = MibTableColumn
txgConfigSfpDeltaThreshold = _TxgConfigSfpDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 4, 1, 12),
    _TxgConfigSfpDeltaThreshold_Type()
)
txgConfigSfpDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txgConfigSfpDeltaThreshold.setStatus("current")
_CxgPlusConfigTable_Object = MibTable
cxgPlusConfigTable = _CxgPlusConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5)
)
if mibBuilder.loadTexts:
    cxgPlusConfigTable.setStatus("current")
_CxgPlusConfigEntry_Object = MibTableRow
cxgPlusConfigEntry = _CxgPlusConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1)
)
cxgPlusConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "cxgPlusConfigIndex"),
)
if mibBuilder.loadTexts:
    cxgPlusConfigEntry.setStatus("current")


class _CxgPlusConfigIndex_Type(Integer32):
    """Custom type cxgPlusConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_CxgPlusConfigIndex_Type.__name__ = "Integer32"
_CxgPlusConfigIndex_Object = MibTableColumn
cxgPlusConfigIndex = _CxgPlusConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 1),
    _CxgPlusConfigIndex_Type()
)
cxgPlusConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cxgPlusConfigIndex.setStatus("current")


class _CxgPlusConfigCxgPort12Datarate_Type(Integer32):
    """Custom type cxgPlusConfigCxgPort12Datarate based on Integer32"""
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
        *(("transparent", 0),
          ("ms8xFc", 1),
          ("ms10gEth", 2),
          ("ms10xFc16xFc", 3))
    )


_CxgPlusConfigCxgPort12Datarate_Type.__name__ = "Integer32"
_CxgPlusConfigCxgPort12Datarate_Object = MibTableColumn
cxgPlusConfigCxgPort12Datarate = _CxgPlusConfigCxgPort12Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 2),
    _CxgPlusConfigCxgPort12Datarate_Type()
)
cxgPlusConfigCxgPort12Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigCxgPort12Datarate.setStatus("current")


class _CxgPlusConfigCxgPort34Datarate_Type(Integer32):
    """Custom type cxgPlusConfigCxgPort34Datarate based on Integer32"""
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
        *(("transparent", 0),
          ("ms8xFc", 1),
          ("ms10gEth", 2),
          ("ms10xFc16xFc", 3))
    )


_CxgPlusConfigCxgPort34Datarate_Type.__name__ = "Integer32"
_CxgPlusConfigCxgPort34Datarate_Object = MibTableColumn
cxgPlusConfigCxgPort34Datarate = _CxgPlusConfigCxgPort34Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 3),
    _CxgPlusConfigCxgPort34Datarate_Type()
)
cxgPlusConfigCxgPort34Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigCxgPort34Datarate.setStatus("current")


class _CxgPlusConfigPort1ItuChannel_Type(Integer32):
    """Custom type cxgPlusConfigPort1ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_CxgPlusConfigPort1ItuChannel_Type.__name__ = "Integer32"
_CxgPlusConfigPort1ItuChannel_Object = MibTableColumn
cxgPlusConfigPort1ItuChannel = _CxgPlusConfigPort1ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 4),
    _CxgPlusConfigPort1ItuChannel_Type()
)
cxgPlusConfigPort1ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigPort1ItuChannel.setStatus("current")


class _CxgPlusConfigPort2ItuChannel_Type(Integer32):
    """Custom type cxgPlusConfigPort2ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_CxgPlusConfigPort2ItuChannel_Type.__name__ = "Integer32"
_CxgPlusConfigPort2ItuChannel_Object = MibTableColumn
cxgPlusConfigPort2ItuChannel = _CxgPlusConfigPort2ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 5),
    _CxgPlusConfigPort2ItuChannel_Type()
)
cxgPlusConfigPort2ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigPort2ItuChannel.setStatus("current")


class _CxgPlusConfigPort3ItuChannel_Type(Integer32):
    """Custom type cxgPlusConfigPort3ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_CxgPlusConfigPort3ItuChannel_Type.__name__ = "Integer32"
_CxgPlusConfigPort3ItuChannel_Object = MibTableColumn
cxgPlusConfigPort3ItuChannel = _CxgPlusConfigPort3ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 6),
    _CxgPlusConfigPort3ItuChannel_Type()
)
cxgPlusConfigPort3ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigPort3ItuChannel.setStatus("current")


class _CxgPlusConfigPort4ItuChannel_Type(Integer32):
    """Custom type cxgPlusConfigPort4ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_CxgPlusConfigPort4ItuChannel_Type.__name__ = "Integer32"
_CxgPlusConfigPort4ItuChannel_Object = MibTableColumn
cxgPlusConfigPort4ItuChannel = _CxgPlusConfigPort4ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 7),
    _CxgPlusConfigPort4ItuChannel_Type()
)
cxgPlusConfigPort4ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigPort4ItuChannel.setStatus("current")


class _CxgPlusConfigDeactivatePort1_Type(Integer32):
    """Custom type cxgPlusConfigDeactivatePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CxgPlusConfigDeactivatePort1_Type.__name__ = "Integer32"
_CxgPlusConfigDeactivatePort1_Object = MibTableColumn
cxgPlusConfigDeactivatePort1 = _CxgPlusConfigDeactivatePort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 8),
    _CxgPlusConfigDeactivatePort1_Type()
)
cxgPlusConfigDeactivatePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigDeactivatePort1.setStatus("current")


class _CxgPlusConfigDeactivatePort2_Type(Integer32):
    """Custom type cxgPlusConfigDeactivatePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CxgPlusConfigDeactivatePort2_Type.__name__ = "Integer32"
_CxgPlusConfigDeactivatePort2_Object = MibTableColumn
cxgPlusConfigDeactivatePort2 = _CxgPlusConfigDeactivatePort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 9),
    _CxgPlusConfigDeactivatePort2_Type()
)
cxgPlusConfigDeactivatePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigDeactivatePort2.setStatus("current")


class _CxgPlusConfigDeactivatePort3_Type(Integer32):
    """Custom type cxgPlusConfigDeactivatePort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CxgPlusConfigDeactivatePort3_Type.__name__ = "Integer32"
_CxgPlusConfigDeactivatePort3_Object = MibTableColumn
cxgPlusConfigDeactivatePort3 = _CxgPlusConfigDeactivatePort3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 10),
    _CxgPlusConfigDeactivatePort3_Type()
)
cxgPlusConfigDeactivatePort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigDeactivatePort3.setStatus("current")


class _CxgPlusConfigDeactivatePort4_Type(Integer32):
    """Custom type cxgPlusConfigDeactivatePort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CxgPlusConfigDeactivatePort4_Type.__name__ = "Integer32"
_CxgPlusConfigDeactivatePort4_Object = MibTableColumn
cxgPlusConfigDeactivatePort4 = _CxgPlusConfigDeactivatePort4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 11),
    _CxgPlusConfigDeactivatePort4_Type()
)
cxgPlusConfigDeactivatePort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigDeactivatePort4.setStatus("current")


class _CxgPlusConfigFrontPanelMode_Type(Integer32):
    """Custom type cxgPlusConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_CxgPlusConfigFrontPanelMode_Type.__name__ = "Integer32"
_CxgPlusConfigFrontPanelMode_Object = MibTableColumn
cxgPlusConfigFrontPanelMode = _CxgPlusConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 12),
    _CxgPlusConfigFrontPanelMode_Type()
)
cxgPlusConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigFrontPanelMode.setStatus("current")


class _CxgPlusConfigLossOfSignalHandling_Type(Integer32):
    """Custom type cxgPlusConfigLossOfSignalHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("percolate", 1))
    )


_CxgPlusConfigLossOfSignalHandling_Type.__name__ = "Integer32"
_CxgPlusConfigLossOfSignalHandling_Object = MibTableColumn
cxgPlusConfigLossOfSignalHandling = _CxgPlusConfigLossOfSignalHandling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 13),
    _CxgPlusConfigLossOfSignalHandling_Type()
)
cxgPlusConfigLossOfSignalHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigLossOfSignalHandling.setStatus("current")


class _CxgPlusConfigSfpDeltaInterval_Type(Integer32):
    """Custom type cxgPlusConfigSfpDeltaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1Sec", 1),
          ("ms5Sec", 2),
          ("ms10Sec", 3),
          ("ms30Sec", 4),
          ("ms60Sec", 5),
          ("ms240Sec", 6))
    )


_CxgPlusConfigSfpDeltaInterval_Type.__name__ = "Integer32"
_CxgPlusConfigSfpDeltaInterval_Object = MibTableColumn
cxgPlusConfigSfpDeltaInterval = _CxgPlusConfigSfpDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 14),
    _CxgPlusConfigSfpDeltaInterval_Type()
)
cxgPlusConfigSfpDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigSfpDeltaInterval.setStatus("current")


class _CxgPlusConfigSfpDeltaThreshold_Type(Integer32):
    """Custom type cxgPlusConfigSfpDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ms05Db", 0),
          ("ms1Db", 1),
          ("ms15Db", 2),
          ("ms2Db", 3),
          ("ms3Db", 4),
          ("ms5Db", 5))
    )


_CxgPlusConfigSfpDeltaThreshold_Type.__name__ = "Integer32"
_CxgPlusConfigSfpDeltaThreshold_Object = MibTableColumn
cxgPlusConfigSfpDeltaThreshold = _CxgPlusConfigSfpDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 5, 1, 15),
    _CxgPlusConfigSfpDeltaThreshold_Type()
)
cxgPlusConfigSfpDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgPlusConfigSfpDeltaThreshold.setStatus("current")
_CxgConfigTable_Object = MibTable
cxgConfigTable = _CxgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6)
)
if mibBuilder.loadTexts:
    cxgConfigTable.setStatus("current")
_CxgConfigEntry_Object = MibTableRow
cxgConfigEntry = _CxgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1)
)
cxgConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "cxgConfigIndex"),
)
if mibBuilder.loadTexts:
    cxgConfigEntry.setStatus("current")


class _CxgConfigIndex_Type(Integer32):
    """Custom type cxgConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_CxgConfigIndex_Type.__name__ = "Integer32"
_CxgConfigIndex_Object = MibTableColumn
cxgConfigIndex = _CxgConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 1),
    _CxgConfigIndex_Type()
)
cxgConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cxgConfigIndex.setStatus("current")


class _CxgConfigCxgPort12Datarate_Type(Integer32):
    """Custom type cxgConfigCxgPort12Datarate based on Integer32"""
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
        *(("transparent", 0),
          ("ms8xFc", 1),
          ("ms10gEth", 2),
          ("ms10xFc16xFc", 3))
    )


_CxgConfigCxgPort12Datarate_Type.__name__ = "Integer32"
_CxgConfigCxgPort12Datarate_Object = MibTableColumn
cxgConfigCxgPort12Datarate = _CxgConfigCxgPort12Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 2),
    _CxgConfigCxgPort12Datarate_Type()
)
cxgConfigCxgPort12Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigCxgPort12Datarate.setStatus("current")


class _CxgConfigPort1ItuChannel_Type(Integer32):
    """Custom type cxgConfigPort1ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_CxgConfigPort1ItuChannel_Type.__name__ = "Integer32"
_CxgConfigPort1ItuChannel_Object = MibTableColumn
cxgConfigPort1ItuChannel = _CxgConfigPort1ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 3),
    _CxgConfigPort1ItuChannel_Type()
)
cxgConfigPort1ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigPort1ItuChannel.setStatus("current")


class _CxgConfigPort2ItuChannel_Type(Integer32):
    """Custom type cxgConfigPort2ItuChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              66,
              68,
              70,
              72,
              74,
              76,
              78,
              80,
              82,
              84,
              86,
              88,
              90,
              92,
              94,
              96,
              98,
              100,
              102,
              104,
              106,
              108,
              110,
              112,
              114,
              116,
              118,
              120,
              122,
              124,
              126)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("ch11", 22),
          ("ch12", 24),
          ("ch13", 26),
          ("ch14", 28),
          ("ch15", 30),
          ("ch16", 32),
          ("ch17", 34),
          ("ch18", 36),
          ("ch19", 38),
          ("ch20", 40),
          ("ch21", 42),
          ("ch22", 44),
          ("ch23", 46),
          ("ch24", 48),
          ("ch25", 50),
          ("ch26", 52),
          ("ch27", 54),
          ("ch28", 56),
          ("ch29", 58),
          ("ch30", 60),
          ("ch31", 62),
          ("ch32", 64),
          ("ch33", 66),
          ("ch34", 68),
          ("ch35", 70),
          ("ch36", 72),
          ("ch37", 74),
          ("ch38", 76),
          ("ch39", 78),
          ("ch40", 80),
          ("ch41", 82),
          ("ch42", 84),
          ("ch43", 86),
          ("ch44", 88),
          ("ch45", 90),
          ("ch46", 92),
          ("ch47", 94),
          ("ch48", 96),
          ("ch49", 98),
          ("ch50", 100),
          ("ch51", 102),
          ("ch52", 104),
          ("ch53", 106),
          ("ch54", 108),
          ("ch55", 110),
          ("ch56", 112),
          ("ch57", 114),
          ("ch58", 116),
          ("ch59", 118),
          ("ch60", 120),
          ("ch61", 122),
          ("ch62", 124),
          ("ch63", 126))
    )


_CxgConfigPort2ItuChannel_Type.__name__ = "Integer32"
_CxgConfigPort2ItuChannel_Object = MibTableColumn
cxgConfigPort2ItuChannel = _CxgConfigPort2ItuChannel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 4),
    _CxgConfigPort2ItuChannel_Type()
)
cxgConfigPort2ItuChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigPort2ItuChannel.setStatus("current")


class _CxgConfigDeactivatePort1_Type(Integer32):
    """Custom type cxgConfigDeactivatePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CxgConfigDeactivatePort1_Type.__name__ = "Integer32"
_CxgConfigDeactivatePort1_Object = MibTableColumn
cxgConfigDeactivatePort1 = _CxgConfigDeactivatePort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 5),
    _CxgConfigDeactivatePort1_Type()
)
cxgConfigDeactivatePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigDeactivatePort1.setStatus("current")


class _CxgConfigDeactivatePort2_Type(Integer32):
    """Custom type cxgConfigDeactivatePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CxgConfigDeactivatePort2_Type.__name__ = "Integer32"
_CxgConfigDeactivatePort2_Object = MibTableColumn
cxgConfigDeactivatePort2 = _CxgConfigDeactivatePort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 6),
    _CxgConfigDeactivatePort2_Type()
)
cxgConfigDeactivatePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigDeactivatePort2.setStatus("current")


class _CxgConfigFrontPanelMode_Type(Integer32):
    """Custom type cxgConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_CxgConfigFrontPanelMode_Type.__name__ = "Integer32"
_CxgConfigFrontPanelMode_Object = MibTableColumn
cxgConfigFrontPanelMode = _CxgConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 7),
    _CxgConfigFrontPanelMode_Type()
)
cxgConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigFrontPanelMode.setStatus("current")


class _CxgConfigLossOfSignalHandling_Type(Integer32):
    """Custom type cxgConfigLossOfSignalHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("percolate", 1))
    )


_CxgConfigLossOfSignalHandling_Type.__name__ = "Integer32"
_CxgConfigLossOfSignalHandling_Object = MibTableColumn
cxgConfigLossOfSignalHandling = _CxgConfigLossOfSignalHandling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 8),
    _CxgConfigLossOfSignalHandling_Type()
)
cxgConfigLossOfSignalHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigLossOfSignalHandling.setStatus("current")


class _CxgConfigSfpDeltaInterval_Type(Integer32):
    """Custom type cxgConfigSfpDeltaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1Sec", 1),
          ("ms5Sec", 2),
          ("ms10Sec", 3),
          ("ms30Sec", 4),
          ("ms60Sec", 5),
          ("ms240Sec", 6))
    )


_CxgConfigSfpDeltaInterval_Type.__name__ = "Integer32"
_CxgConfigSfpDeltaInterval_Object = MibTableColumn
cxgConfigSfpDeltaInterval = _CxgConfigSfpDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 9),
    _CxgConfigSfpDeltaInterval_Type()
)
cxgConfigSfpDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigSfpDeltaInterval.setStatus("current")


class _CxgConfigSfpDeltaThreshold_Type(Integer32):
    """Custom type cxgConfigSfpDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ms05Db", 0),
          ("ms1Db", 1),
          ("ms15Db", 2),
          ("ms2Db", 3),
          ("ms3Db", 4),
          ("ms5Db", 5))
    )


_CxgConfigSfpDeltaThreshold_Type.__name__ = "Integer32"
_CxgConfigSfpDeltaThreshold_Object = MibTableColumn
cxgConfigSfpDeltaThreshold = _CxgConfigSfpDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 6, 1, 10),
    _CxgConfigSfpDeltaThreshold_Type()
)
cxgConfigSfpDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxgConfigSfpDeltaThreshold.setStatus("current")
_T4gConfigTable_Object = MibTable
t4gConfigTable = _T4gConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7)
)
if mibBuilder.loadTexts:
    t4gConfigTable.setStatus("current")
_T4gConfigEntry_Object = MibTableRow
t4gConfigEntry = _T4gConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1)
)
t4gConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "t4gConfigIndex"),
)
if mibBuilder.loadTexts:
    t4gConfigEntry.setStatus("current")


class _T4gConfigIndex_Type(Integer32):
    """Custom type t4gConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_T4gConfigIndex_Type.__name__ = "Integer32"
_T4gConfigIndex_Object = MibTableColumn
t4gConfigIndex = _T4gConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 1),
    _T4gConfigIndex_Type()
)
t4gConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t4gConfigIndex.setStatus("current")


class _T4gConfigT4gPort12Datarate_Type(Integer32):
    """Custom type t4gConfigT4gPort12Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              6,
              7,
              8,
              10,
              11,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("ms100mEth", 2),
          ("oc3", 3),
          ("escon", 4),
          ("oc12", 6),
          ("ms1xFc", 7),
          ("ms1gEth", 8),
          ("ms2xFc", 10),
          ("oc48", 11),
          ("infiniband", 12),
          ("ms4xFc", 14))
    )


_T4gConfigT4gPort12Datarate_Type.__name__ = "Integer32"
_T4gConfigT4gPort12Datarate_Object = MibTableColumn
t4gConfigT4gPort12Datarate = _T4gConfigT4gPort12Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 2),
    _T4gConfigT4gPort12Datarate_Type()
)
t4gConfigT4gPort12Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigT4gPort12Datarate.setStatus("current")


class _T4gConfigT4gPort34Datarate_Type(Integer32):
    """Custom type t4gConfigT4gPort34Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              6,
              7,
              8,
              10,
              11,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("ms100mEth", 2),
          ("oc3", 3),
          ("escon", 4),
          ("oc12", 6),
          ("ms1xFc", 7),
          ("ms1gEth", 8),
          ("ms2xFc", 10),
          ("oc48", 11),
          ("infiniband", 12),
          ("ms4xFc", 14))
    )


_T4gConfigT4gPort34Datarate_Type.__name__ = "Integer32"
_T4gConfigT4gPort34Datarate_Object = MibTableColumn
t4gConfigT4gPort34Datarate = _T4gConfigT4gPort34Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 3),
    _T4gConfigT4gPort34Datarate_Type()
)
t4gConfigT4gPort34Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigT4gPort34Datarate.setStatus("current")


class _T4gConfigT4gOperationMode_Type(Integer32):
    """Custom type t4gConfigT4gOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("transponder", 1),
          ("bertPort4", 2))
    )


_T4gConfigT4gOperationMode_Type.__name__ = "Integer32"
_T4gConfigT4gOperationMode_Object = MibTableColumn
t4gConfigT4gOperationMode = _T4gConfigT4gOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 4),
    _T4gConfigT4gOperationMode_Type()
)
t4gConfigT4gOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigT4gOperationMode.setStatus("current")


class _T4gConfigDeactivatePort1_Type(Integer32):
    """Custom type t4gConfigDeactivatePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_T4gConfigDeactivatePort1_Type.__name__ = "Integer32"
_T4gConfigDeactivatePort1_Object = MibTableColumn
t4gConfigDeactivatePort1 = _T4gConfigDeactivatePort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 5),
    _T4gConfigDeactivatePort1_Type()
)
t4gConfigDeactivatePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigDeactivatePort1.setStatus("current")


class _T4gConfigDeactivatePort2_Type(Integer32):
    """Custom type t4gConfigDeactivatePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_T4gConfigDeactivatePort2_Type.__name__ = "Integer32"
_T4gConfigDeactivatePort2_Object = MibTableColumn
t4gConfigDeactivatePort2 = _T4gConfigDeactivatePort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 6),
    _T4gConfigDeactivatePort2_Type()
)
t4gConfigDeactivatePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigDeactivatePort2.setStatus("current")


class _T4gConfigDeactivatePort3_Type(Integer32):
    """Custom type t4gConfigDeactivatePort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_T4gConfigDeactivatePort3_Type.__name__ = "Integer32"
_T4gConfigDeactivatePort3_Object = MibTableColumn
t4gConfigDeactivatePort3 = _T4gConfigDeactivatePort3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 7),
    _T4gConfigDeactivatePort3_Type()
)
t4gConfigDeactivatePort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigDeactivatePort3.setStatus("current")


class _T4gConfigDeactivatePort4_Type(Integer32):
    """Custom type t4gConfigDeactivatePort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_T4gConfigDeactivatePort4_Type.__name__ = "Integer32"
_T4gConfigDeactivatePort4_Object = MibTableColumn
t4gConfigDeactivatePort4 = _T4gConfigDeactivatePort4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 8),
    _T4gConfigDeactivatePort4_Type()
)
t4gConfigDeactivatePort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigDeactivatePort4.setStatus("current")


class _T4gConfigFrontPanelMode_Type(Integer32):
    """Custom type t4gConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_T4gConfigFrontPanelMode_Type.__name__ = "Integer32"
_T4gConfigFrontPanelMode_Object = MibTableColumn
t4gConfigFrontPanelMode = _T4gConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 9),
    _T4gConfigFrontPanelMode_Type()
)
t4gConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigFrontPanelMode.setStatus("current")


class _T4gConfigLossOfSignalHandling_Type(Integer32):
    """Custom type t4gConfigLossOfSignalHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("percolate", 1))
    )


_T4gConfigLossOfSignalHandling_Type.__name__ = "Integer32"
_T4gConfigLossOfSignalHandling_Object = MibTableColumn
t4gConfigLossOfSignalHandling = _T4gConfigLossOfSignalHandling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 10),
    _T4gConfigLossOfSignalHandling_Type()
)
t4gConfigLossOfSignalHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigLossOfSignalHandling.setStatus("current")


class _T4gConfigBertPattern_Type(Integer32):
    """Custom type t4gConfigBertPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ms27", 0),
          ("ms223", 2),
          ("ms231", 3),
          ("cjPat", 4),
          ("crPat", 5),
          ("ms8b10bCnt", 6))
    )


_T4gConfigBertPattern_Type.__name__ = "Integer32"
_T4gConfigBertPattern_Object = MibTableColumn
t4gConfigBertPattern = _T4gConfigBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 11),
    _T4gConfigBertPattern_Type()
)
t4gConfigBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigBertPattern.setStatus("current")


class _T4gConfigSfpDeltaInterval_Type(Integer32):
    """Custom type t4gConfigSfpDeltaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1Sec", 1),
          ("ms5Sec", 2),
          ("ms10Sec", 3),
          ("ms30Sec", 4),
          ("ms60Sec", 5),
          ("ms240Sec", 6))
    )


_T4gConfigSfpDeltaInterval_Type.__name__ = "Integer32"
_T4gConfigSfpDeltaInterval_Object = MibTableColumn
t4gConfigSfpDeltaInterval = _T4gConfigSfpDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 12),
    _T4gConfigSfpDeltaInterval_Type()
)
t4gConfigSfpDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigSfpDeltaInterval.setStatus("current")


class _T4gConfigSfpDeltaThreshold_Type(Integer32):
    """Custom type t4gConfigSfpDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ms05Db", 0),
          ("ms1Db", 1),
          ("ms15Db", 2),
          ("ms2Db", 3),
          ("ms3Db", 4),
          ("ms5Db", 5))
    )


_T4gConfigSfpDeltaThreshold_Type.__name__ = "Integer32"
_T4gConfigSfpDeltaThreshold_Object = MibTableColumn
t4gConfigSfpDeltaThreshold = _T4gConfigSfpDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 7, 1, 13),
    _T4gConfigSfpDeltaThreshold_Type()
)
t4gConfigSfpDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t4gConfigSfpDeltaThreshold.setStatus("current")
_M2gConfigTable_Object = MibTable
m2gConfigTable = _M2gConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8)
)
if mibBuilder.loadTexts:
    m2gConfigTable.setStatus("current")
_M2gConfigEntry_Object = MibTableRow
m2gConfigEntry = _M2gConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1)
)
m2gConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "m2gConfigIndex"),
)
if mibBuilder.loadTexts:
    m2gConfigEntry.setStatus("current")


class _M2gConfigIndex_Type(Integer32):
    """Custom type m2gConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_M2gConfigIndex_Type.__name__ = "Integer32"
_M2gConfigIndex_Object = MibTableColumn
m2gConfigIndex = _M2gConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 1),
    _M2gConfigIndex_Type()
)
m2gConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    m2gConfigIndex.setStatus("current")


class _M2gConfigChannel1Datarate_Type(Integer32):
    """Custom type m2gConfigChannel1Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1gEth", 1),
          ("ms1xFc", 2))
    )


_M2gConfigChannel1Datarate_Type.__name__ = "Integer32"
_M2gConfigChannel1Datarate_Object = MibTableColumn
m2gConfigChannel1Datarate = _M2gConfigChannel1Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 2),
    _M2gConfigChannel1Datarate_Type()
)
m2gConfigChannel1Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigChannel1Datarate.setStatus("current")


class _M2gConfigChannel2Datarate_Type(Integer32):
    """Custom type m2gConfigChannel2Datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1gEth", 1),
          ("ms1xFc", 2))
    )


_M2gConfigChannel2Datarate_Type.__name__ = "Integer32"
_M2gConfigChannel2Datarate_Object = MibTableColumn
m2gConfigChannel2Datarate = _M2gConfigChannel2Datarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 3),
    _M2gConfigChannel2Datarate_Type()
)
m2gConfigChannel2Datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigChannel2Datarate.setStatus("current")


class _M2gConfigPort1CopperSfp_Type(Integer32):
    """Custom type m2gConfigPort1CopperSfp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_M2gConfigPort1CopperSfp_Type.__name__ = "Integer32"
_M2gConfigPort1CopperSfp_Object = MibTableColumn
m2gConfigPort1CopperSfp = _M2gConfigPort1CopperSfp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 4),
    _M2gConfigPort1CopperSfp_Type()
)
m2gConfigPort1CopperSfp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigPort1CopperSfp.setStatus("current")


class _M2gConfigPort2CopperSfp_Type(Integer32):
    """Custom type m2gConfigPort2CopperSfp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_M2gConfigPort2CopperSfp_Type.__name__ = "Integer32"
_M2gConfigPort2CopperSfp_Object = MibTableColumn
m2gConfigPort2CopperSfp = _M2gConfigPort2CopperSfp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 5),
    _M2gConfigPort2CopperSfp_Type()
)
m2gConfigPort2CopperSfp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigPort2CopperSfp.setStatus("current")


class _M2gConfigSfpDeltaInterval_Type(Integer32):
    """Custom type m2gConfigSfpDeltaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ms1Sec", 1),
          ("ms5Sec", 2),
          ("ms10Sec", 3),
          ("ms30Sec", 4),
          ("ms60Sec", 5),
          ("ms240Sec", 6))
    )


_M2gConfigSfpDeltaInterval_Type.__name__ = "Integer32"
_M2gConfigSfpDeltaInterval_Object = MibTableColumn
m2gConfigSfpDeltaInterval = _M2gConfigSfpDeltaInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 6),
    _M2gConfigSfpDeltaInterval_Type()
)
m2gConfigSfpDeltaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigSfpDeltaInterval.setStatus("current")


class _M2gConfigSfpDeltaThreshold_Type(Integer32):
    """Custom type m2gConfigSfpDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ms05Db", 0),
          ("ms1Db", 1),
          ("ms15Db", 2),
          ("ms2Db", 3),
          ("ms3Db", 4),
          ("ms5Db", 5))
    )


_M2gConfigSfpDeltaThreshold_Type.__name__ = "Integer32"
_M2gConfigSfpDeltaThreshold_Object = MibTableColumn
m2gConfigSfpDeltaThreshold = _M2gConfigSfpDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 7),
    _M2gConfigSfpDeltaThreshold_Type()
)
m2gConfigSfpDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigSfpDeltaThreshold.setStatus("current")


class _M2gConfigLinkBackupTrigger_Type(Integer32):
    """Custom type m2gConfigLinkBackupTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("signalLoss", 1),
          ("errorBurst", 2))
    )


_M2gConfigLinkBackupTrigger_Type.__name__ = "Integer32"
_M2gConfigLinkBackupTrigger_Object = MibTableColumn
m2gConfigLinkBackupTrigger = _M2gConfigLinkBackupTrigger_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 8),
    _M2gConfigLinkBackupTrigger_Type()
)
m2gConfigLinkBackupTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigLinkBackupTrigger.setStatus("current")


class _M2gConfigStayWithLastLink_Type(Integer32):
    """Custom type m2gConfigStayWithLastLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_M2gConfigStayWithLastLink_Type.__name__ = "Integer32"
_M2gConfigStayWithLastLink_Object = MibTableColumn
m2gConfigStayWithLastLink = _M2gConfigStayWithLastLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 9),
    _M2gConfigStayWithLastLink_Type()
)
m2gConfigStayWithLastLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigStayWithLastLink.setStatus("current")


class _M2gConfigBackupEnd_Type(Integer32):
    """Custom type m2gConfigBackupEnd based on Integer32"""
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
        *(("noDelay", 0),
          ("ms15Seconds", 1),
          ("ms15Minutes", 2),
          ("manually", 3))
    )


_M2gConfigBackupEnd_Type.__name__ = "Integer32"
_M2gConfigBackupEnd_Object = MibTableColumn
m2gConfigBackupEnd = _M2gConfigBackupEnd_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 10),
    _M2gConfigBackupEnd_Type()
)
m2gConfigBackupEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigBackupEnd.setStatus("current")


class _M2gConfigPermitLinkOverride_Type(Integer32):
    """Custom type m2gConfigPermitLinkOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_M2gConfigPermitLinkOverride_Type.__name__ = "Integer32"
_M2gConfigPermitLinkOverride_Object = MibTableColumn
m2gConfigPermitLinkOverride = _M2gConfigPermitLinkOverride_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 8, 1, 11),
    _M2gConfigPermitLinkOverride_Type()
)
m2gConfigPermitLinkOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2gConfigPermitLinkOverride.setStatus("current")
_Om1ConfigTable_Object = MibTable
om1ConfigTable = _Om1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9)
)
if mibBuilder.loadTexts:
    om1ConfigTable.setStatus("current")
_Om1ConfigEntry_Object = MibTableRow
om1ConfigEntry = _Om1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1)
)
om1ConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "om1ConfigIndex"),
)
if mibBuilder.loadTexts:
    om1ConfigEntry.setStatus("current")


class _Om1ConfigIndex_Type(Integer32):
    """Custom type om1ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Om1ConfigIndex_Type.__name__ = "Integer32"
_Om1ConfigIndex_Object = MibTableColumn
om1ConfigIndex = _Om1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 1),
    _Om1ConfigIndex_Type()
)
om1ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    om1ConfigIndex.setStatus("current")


class _Om1ConfigWavelengthPortA_Type(Integer32):
    """Custom type om1ConfigWavelengthPortA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1550nm", 0),
          ("ms1310nm", 1),
          ("disabled", 3))
    )


_Om1ConfigWavelengthPortA_Type.__name__ = "Integer32"
_Om1ConfigWavelengthPortA_Object = MibTableColumn
om1ConfigWavelengthPortA = _Om1ConfigWavelengthPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 2),
    _Om1ConfigWavelengthPortA_Type()
)
om1ConfigWavelengthPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    om1ConfigWavelengthPortA.setStatus("current")
_Om1ConfigLowThresholdPortA_Type = DisplayString
_Om1ConfigLowThresholdPortA_Object = MibTableColumn
om1ConfigLowThresholdPortA = _Om1ConfigLowThresholdPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 3),
    _Om1ConfigLowThresholdPortA_Type()
)
om1ConfigLowThresholdPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    om1ConfigLowThresholdPortA.setStatus("current")
_Om1ConfigHighThresholdPortA_Type = DisplayString
_Om1ConfigHighThresholdPortA_Object = MibTableColumn
om1ConfigHighThresholdPortA = _Om1ConfigHighThresholdPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 4),
    _Om1ConfigHighThresholdPortA_Type()
)
om1ConfigHighThresholdPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    om1ConfigHighThresholdPortA.setStatus("current")


class _Om1ConfigWavelengthPortB_Type(Integer32):
    """Custom type om1ConfigWavelengthPortB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1550nm", 0),
          ("ms1310nm", 1),
          ("disabled", 3))
    )


_Om1ConfigWavelengthPortB_Type.__name__ = "Integer32"
_Om1ConfigWavelengthPortB_Object = MibTableColumn
om1ConfigWavelengthPortB = _Om1ConfigWavelengthPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 5),
    _Om1ConfigWavelengthPortB_Type()
)
om1ConfigWavelengthPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    om1ConfigWavelengthPortB.setStatus("current")
_Om1ConfigLowThresholdPortB_Type = DisplayString
_Om1ConfigLowThresholdPortB_Object = MibTableColumn
om1ConfigLowThresholdPortB = _Om1ConfigLowThresholdPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 6),
    _Om1ConfigLowThresholdPortB_Type()
)
om1ConfigLowThresholdPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    om1ConfigLowThresholdPortB.setStatus("current")
_Om1ConfigHighThresholdPortB_Type = DisplayString
_Om1ConfigHighThresholdPortB_Object = MibTableColumn
om1ConfigHighThresholdPortB = _Om1ConfigHighThresholdPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 7),
    _Om1ConfigHighThresholdPortB_Type()
)
om1ConfigHighThresholdPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    om1ConfigHighThresholdPortB.setStatus("current")


class _Om1ConfigFrontPanelMode_Type(Integer32):
    """Custom type om1ConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_Om1ConfigFrontPanelMode_Type.__name__ = "Integer32"
_Om1ConfigFrontPanelMode_Object = MibTableColumn
om1ConfigFrontPanelMode = _Om1ConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 9, 1, 8),
    _Om1ConfigFrontPanelMode_Type()
)
om1ConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    om1ConfigFrontPanelMode.setStatus("current")
_Lp1ConfigTable_Object = MibTable
lp1ConfigTable = _Lp1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10)
)
if mibBuilder.loadTexts:
    lp1ConfigTable.setStatus("current")
_Lp1ConfigEntry_Object = MibTableRow
lp1ConfigEntry = _Lp1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1)
)
lp1ConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "lp1ConfigIndex"),
)
if mibBuilder.loadTexts:
    lp1ConfigEntry.setStatus("current")


class _Lp1ConfigIndex_Type(Integer32):
    """Custom type lp1ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Lp1ConfigIndex_Type.__name__ = "Integer32"
_Lp1ConfigIndex_Object = MibTableColumn
lp1ConfigIndex = _Lp1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 1),
    _Lp1ConfigIndex_Type()
)
lp1ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lp1ConfigIndex.setStatus("current")


class _Lp1ConfigWavelengthPortA_Type(Integer32):
    """Custom type lp1ConfigWavelengthPortA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1550nm", 0),
          ("ms1310nm", 1),
          ("disabled", 3))
    )


_Lp1ConfigWavelengthPortA_Type.__name__ = "Integer32"
_Lp1ConfigWavelengthPortA_Object = MibTableColumn
lp1ConfigWavelengthPortA = _Lp1ConfigWavelengthPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 2),
    _Lp1ConfigWavelengthPortA_Type()
)
lp1ConfigWavelengthPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigWavelengthPortA.setStatus("current")
_Lp1ConfigLowThresholdPortA_Type = DisplayString
_Lp1ConfigLowThresholdPortA_Object = MibTableColumn
lp1ConfigLowThresholdPortA = _Lp1ConfigLowThresholdPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 3),
    _Lp1ConfigLowThresholdPortA_Type()
)
lp1ConfigLowThresholdPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigLowThresholdPortA.setStatus("current")
_Lp1ConfigHighThresholdPortA_Type = DisplayString
_Lp1ConfigHighThresholdPortA_Object = MibTableColumn
lp1ConfigHighThresholdPortA = _Lp1ConfigHighThresholdPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 4),
    _Lp1ConfigHighThresholdPortA_Type()
)
lp1ConfigHighThresholdPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigHighThresholdPortA.setStatus("current")


class _Lp1ConfigWavelengthPortB_Type(Integer32):
    """Custom type lp1ConfigWavelengthPortB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1550nm", 0),
          ("ms1310nm", 1),
          ("disabled", 3))
    )


_Lp1ConfigWavelengthPortB_Type.__name__ = "Integer32"
_Lp1ConfigWavelengthPortB_Object = MibTableColumn
lp1ConfigWavelengthPortB = _Lp1ConfigWavelengthPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 5),
    _Lp1ConfigWavelengthPortB_Type()
)
lp1ConfigWavelengthPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigWavelengthPortB.setStatus("current")
_Lp1ConfigLowThresholdPortB_Type = DisplayString
_Lp1ConfigLowThresholdPortB_Object = MibTableColumn
lp1ConfigLowThresholdPortB = _Lp1ConfigLowThresholdPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 6),
    _Lp1ConfigLowThresholdPortB_Type()
)
lp1ConfigLowThresholdPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigLowThresholdPortB.setStatus("current")
_Lp1ConfigHighThresholdPortB_Type = DisplayString
_Lp1ConfigHighThresholdPortB_Object = MibTableColumn
lp1ConfigHighThresholdPortB = _Lp1ConfigHighThresholdPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 7),
    _Lp1ConfigHighThresholdPortB_Type()
)
lp1ConfigHighThresholdPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigHighThresholdPortB.setStatus("current")


class _Lp1ConfigBackupCriteria_Type(Integer32):
    """Custom type lp1ConfigBackupCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signalLow", 0),
          ("signalHigh", 1),
          ("manually", 2))
    )


_Lp1ConfigBackupCriteria_Type.__name__ = "Integer32"
_Lp1ConfigBackupCriteria_Object = MibTableColumn
lp1ConfigBackupCriteria = _Lp1ConfigBackupCriteria_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 8),
    _Lp1ConfigBackupCriteria_Type()
)
lp1ConfigBackupCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigBackupCriteria.setStatus("current")


class _Lp1ConfigStayWithLastLink_Type(Integer32):
    """Custom type lp1ConfigStayWithLastLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Lp1ConfigStayWithLastLink_Type.__name__ = "Integer32"
_Lp1ConfigStayWithLastLink_Object = MibTableColumn
lp1ConfigStayWithLastLink = _Lp1ConfigStayWithLastLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 9),
    _Lp1ConfigStayWithLastLink_Type()
)
lp1ConfigStayWithLastLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigStayWithLastLink.setStatus("current")


class _Lp1ConfigBackupEnd_Type(Integer32):
    """Custom type lp1ConfigBackupEnd based on Integer32"""
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
        *(("noDelay", 0),
          ("ms15Seconds", 1),
          ("ms15Minutes", 2),
          ("manually", 3))
    )


_Lp1ConfigBackupEnd_Type.__name__ = "Integer32"
_Lp1ConfigBackupEnd_Object = MibTableColumn
lp1ConfigBackupEnd = _Lp1ConfigBackupEnd_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 10),
    _Lp1ConfigBackupEnd_Type()
)
lp1ConfigBackupEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigBackupEnd.setStatus("current")


class _Lp1ConfigFrontPanelMode_Type(Integer32):
    """Custom type lp1ConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_Lp1ConfigFrontPanelMode_Type.__name__ = "Integer32"
_Lp1ConfigFrontPanelMode_Object = MibTableColumn
lp1ConfigFrontPanelMode = _Lp1ConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 10, 1, 11),
    _Lp1ConfigFrontPanelMode_Type()
)
lp1ConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lp1ConfigFrontPanelMode.setStatus("current")
_EmConfigTable_Object = MibTable
emConfigTable = _EmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11)
)
if mibBuilder.loadTexts:
    emConfigTable.setStatus("current")
_EmConfigEntry_Object = MibTableRow
emConfigEntry = _EmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1)
)
emConfigEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "emConfigIndex"),
)
if mibBuilder.loadTexts:
    emConfigEntry.setStatus("current")


class _EmConfigIndex_Type(Integer32):
    """Custom type emConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_EmConfigIndex_Type.__name__ = "Integer32"
_EmConfigIndex_Object = MibTableColumn
emConfigIndex = _EmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 1),
    _EmConfigIndex_Type()
)
emConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emConfigIndex.setStatus("current")


class _EmConfigEdfaOperationMode_Type(Integer32):
    """Custom type emConfigEdfaOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preAmp", 0),
          ("booster", 1),
          ("pumpDisabled", 3))
    )


_EmConfigEdfaOperationMode_Type.__name__ = "Integer32"
_EmConfigEdfaOperationMode_Object = MibTableColumn
emConfigEdfaOperationMode = _EmConfigEdfaOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 2),
    _EmConfigEdfaOperationMode_Type()
)
emConfigEdfaOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigEdfaOperationMode.setStatus("current")


class _EmConfigLossOfSignalHandling_Type(Integer32):
    """Custom type emConfigLossOfSignalHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("percolate", 1))
    )


_EmConfigLossOfSignalHandling_Type.__name__ = "Integer32"
_EmConfigLossOfSignalHandling_Object = MibTableColumn
emConfigLossOfSignalHandling = _EmConfigLossOfSignalHandling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 3),
    _EmConfigLossOfSignalHandling_Type()
)
emConfigLossOfSignalHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigLossOfSignalHandling.setStatus("current")
_EmConfigSignalGain_Type = DisplayString
_EmConfigSignalGain_Object = MibTableColumn
emConfigSignalGain = _EmConfigSignalGain_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 4),
    _EmConfigSignalGain_Type()
)
emConfigSignalGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigSignalGain.setStatus("current")
_EmConfigMaxOutputPower_Type = DisplayString
_EmConfigMaxOutputPower_Object = MibTableColumn
emConfigMaxOutputPower = _EmConfigMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 5),
    _EmConfigMaxOutputPower_Type()
)
emConfigMaxOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigMaxOutputPower.setStatus("current")
_EmConfigLowThresholdEdfaIn_Type = DisplayString
_EmConfigLowThresholdEdfaIn_Object = MibTableColumn
emConfigLowThresholdEdfaIn = _EmConfigLowThresholdEdfaIn_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 6),
    _EmConfigLowThresholdEdfaIn_Type()
)
emConfigLowThresholdEdfaIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigLowThresholdEdfaIn.setStatus("current")
_EmConfigHighThresholdEdfaIn_Type = DisplayString
_EmConfigHighThresholdEdfaIn_Object = MibTableColumn
emConfigHighThresholdEdfaIn = _EmConfigHighThresholdEdfaIn_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 7),
    _EmConfigHighThresholdEdfaIn_Type()
)
emConfigHighThresholdEdfaIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigHighThresholdEdfaIn.setStatus("current")
_EmConfigLowThresholdPortB_Type = DisplayString
_EmConfigLowThresholdPortB_Object = MibTableColumn
emConfigLowThresholdPortB = _EmConfigLowThresholdPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 8),
    _EmConfigLowThresholdPortB_Type()
)
emConfigLowThresholdPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigLowThresholdPortB.setStatus("current")
_EmConfigHighThresholdPortB_Type = DisplayString
_EmConfigHighThresholdPortB_Object = MibTableColumn
emConfigHighThresholdPortB = _EmConfigHighThresholdPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 9),
    _EmConfigHighThresholdPortB_Type()
)
emConfigHighThresholdPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigHighThresholdPortB.setStatus("current")


class _EmConfigFrontPanelMode_Type(Integer32):
    """Custom type emConfigFrontPanelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("extended", 1),
          ("normalLocked", 4),
          ("extendedLocked", 5),
          ("remote", 7))
    )


_EmConfigFrontPanelMode_Type.__name__ = "Integer32"
_EmConfigFrontPanelMode_Object = MibTableColumn
emConfigFrontPanelMode = _EmConfigFrontPanelMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 11, 1, 10),
    _EmConfigFrontPanelMode_Type()
)
emConfigFrontPanelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emConfigFrontPanelMode.setStatus("current")
_ModuleControlTable_Object = MibTable
moduleControlTable = _ModuleControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12)
)
if mibBuilder.loadTexts:
    moduleControlTable.setStatus("current")
_ModuleControlEntry_Object = MibTableRow
moduleControlEntry = _ModuleControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1)
)
moduleControlEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "moduleControlIndex"),
)
if mibBuilder.loadTexts:
    moduleControlEntry.setStatus("current")


class _ModuleControlIndex_Type(Integer32):
    """Custom type moduleControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_ModuleControlIndex_Type.__name__ = "Integer32"
_ModuleControlIndex_Object = MibTableColumn
moduleControlIndex = _ModuleControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 1),
    _ModuleControlIndex_Type()
)
moduleControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleControlIndex.setStatus("current")
_ModuleControlEnterPassword_Type = DisplayString
_ModuleControlEnterPassword_Object = MibTableColumn
moduleControlEnterPassword = _ModuleControlEnterPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 2),
    _ModuleControlEnterPassword_Type()
)
moduleControlEnterPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlEnterPassword.setStatus("current")
_ModuleControlRebootModule_Type = DisplayString
_ModuleControlRebootModule_Object = MibTableColumn
moduleControlRebootModule = _ModuleControlRebootModule_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 3),
    _ModuleControlRebootModule_Type()
)
moduleControlRebootModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlRebootModule.setStatus("current")
_ModuleControlWarmStart_Type = DisplayString
_ModuleControlWarmStart_Object = MibTableColumn
moduleControlWarmStart = _ModuleControlWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 4),
    _ModuleControlWarmStart_Type()
)
moduleControlWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlWarmStart.setStatus("current")
_ModuleControlClearCounter_Type = DisplayString
_ModuleControlClearCounter_Object = MibTableColumn
moduleControlClearCounter = _ModuleControlClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 5),
    _ModuleControlClearCounter_Type()
)
moduleControlClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlClearCounter.setStatus("current")
_ModuleControlSwitchOffBackup_Type = DisplayString
_ModuleControlSwitchOffBackup_Object = MibTableColumn
moduleControlSwitchOffBackup = _ModuleControlSwitchOffBackup_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 6),
    _ModuleControlSwitchOffBackup_Type()
)
moduleControlSwitchOffBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlSwitchOffBackup.setStatus("current")
_ModuleControlSwitchToBackup_Type = DisplayString
_ModuleControlSwitchToBackup_Object = MibTableColumn
moduleControlSwitchToBackup = _ModuleControlSwitchToBackup_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 7),
    _ModuleControlSwitchToBackup_Type()
)
moduleControlSwitchToBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlSwitchToBackup.setStatus("current")
_ModuleControlAutomaticBackup_Type = DisplayString
_ModuleControlAutomaticBackup_Object = MibTableColumn
moduleControlAutomaticBackup = _ModuleControlAutomaticBackup_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 8),
    _ModuleControlAutomaticBackup_Type()
)
moduleControlAutomaticBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlAutomaticBackup.setStatus("current")
_ModuleControlWriteDisplay_Type = DisplayString
_ModuleControlWriteDisplay_Object = MibTableColumn
moduleControlWriteDisplay = _ModuleControlWriteDisplay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 9),
    _ModuleControlWriteDisplay_Type()
)
moduleControlWriteDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlWriteDisplay.setStatus("current")
_ModuleControlLedTest_Type = DisplayString
_ModuleControlLedTest_Object = MibTableColumn
moduleControlLedTest = _ModuleControlLedTest_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 10),
    _ModuleControlLedTest_Type()
)
moduleControlLedTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlLedTest.setStatus("current")
_ModuleControlLoopOff_Type = DisplayString
_ModuleControlLoopOff_Object = MibTableColumn
moduleControlLoopOff = _ModuleControlLoopOff_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 11),
    _ModuleControlLoopOff_Type()
)
moduleControlLoopOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlLoopOff.setStatus("current")
_ModuleControlLoopPort1_Type = DisplayString
_ModuleControlLoopPort1_Object = MibTableColumn
moduleControlLoopPort1 = _ModuleControlLoopPort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 12),
    _ModuleControlLoopPort1_Type()
)
moduleControlLoopPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlLoopPort1.setStatus("current")
_ModuleControlLoopPort2_Type = DisplayString
_ModuleControlLoopPort2_Object = MibTableColumn
moduleControlLoopPort2 = _ModuleControlLoopPort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 13),
    _ModuleControlLoopPort2_Type()
)
moduleControlLoopPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlLoopPort2.setStatus("current")
_ModuleControlLoopPort3_Type = DisplayString
_ModuleControlLoopPort3_Object = MibTableColumn
moduleControlLoopPort3 = _ModuleControlLoopPort3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 14),
    _ModuleControlLoopPort3_Type()
)
moduleControlLoopPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlLoopPort3.setStatus("current")
_ModuleControlLoopPort4_Type = DisplayString
_ModuleControlLoopPort4_Object = MibTableColumn
moduleControlLoopPort4 = _ModuleControlLoopPort4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 15),
    _ModuleControlLoopPort4_Type()
)
moduleControlLoopPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlLoopPort4.setStatus("current")
_ModuleControlBertRestart_Type = DisplayString
_ModuleControlBertRestart_Object = MibTableColumn
moduleControlBertRestart = _ModuleControlBertRestart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 16),
    _ModuleControlBertRestart_Type()
)
moduleControlBertRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlBertRestart.setStatus("current")
_ModuleControlBertInsertError_Type = DisplayString
_ModuleControlBertInsertError_Object = MibTableColumn
moduleControlBertInsertError = _ModuleControlBertInsertError_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 17),
    _ModuleControlBertInsertError_Type()
)
moduleControlBertInsertError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlBertInsertError.setStatus("current")
_ModuleControlBertClearCounter_Type = DisplayString
_ModuleControlBertClearCounter_Object = MibTableColumn
moduleControlBertClearCounter = _ModuleControlBertClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 12, 1, 18),
    _ModuleControlBertClearCounter_Type()
)
moduleControlBertClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlBertClearCounter.setStatus("current")
_SystemStatusTable_Object = MibTable
systemStatusTable = _SystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100)
)
if mibBuilder.loadTexts:
    systemStatusTable.setStatus("current")
_SystemStatusEntry_Object = MibTableRow
systemStatusEntry = _SystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1)
)
systemStatusEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "systemStatusIndex"),
)
if mibBuilder.loadTexts:
    systemStatusEntry.setStatus("current")


class _SystemStatusIndex_Type(Integer32):
    """Custom type systemStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_SystemStatusIndex_Type.__name__ = "Integer32"
_SystemStatusIndex_Object = MibTableColumn
systemStatusIndex = _SystemStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1, 1),
    _SystemStatusIndex_Type()
)
systemStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemStatusIndex.setStatus("current")


class _SystemStatusAnyErrorCondition_Type(Integer32):
    """Custom type systemStatusAnyErrorCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SystemStatusAnyErrorCondition_Type.__name__ = "Integer32"
_SystemStatusAnyErrorCondition_Object = MibTableColumn
systemStatusAnyErrorCondition = _SystemStatusAnyErrorCondition_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1, 2),
    _SystemStatusAnyErrorCondition_Type()
)
systemStatusAnyErrorCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusAnyErrorCondition.setStatus("current")


class _SystemStatusAnyTestMode_Type(Integer32):
    """Custom type systemStatusAnyTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SystemStatusAnyTestMode_Type.__name__ = "Integer32"
_SystemStatusAnyTestMode_Object = MibTableColumn
systemStatusAnyTestMode = _SystemStatusAnyTestMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1, 3),
    _SystemStatusAnyTestMode_Type()
)
systemStatusAnyTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusAnyTestMode.setStatus("current")


class _SystemStatusAnySparePart_Type(Integer32):
    """Custom type systemStatusAnySparePart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SystemStatusAnySparePart_Type.__name__ = "Integer32"
_SystemStatusAnySparePart_Object = MibTableColumn
systemStatusAnySparePart = _SystemStatusAnySparePart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1, 4),
    _SystemStatusAnySparePart_Type()
)
systemStatusAnySparePart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusAnySparePart.setStatus("current")
_SystemStatusUsedNodeId_Type = Unsigned32
_SystemStatusUsedNodeId_Object = MibTableColumn
systemStatusUsedNodeId = _SystemStatusUsedNodeId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1, 5),
    _SystemStatusUsedNodeId_Type()
)
systemStatusUsedNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusUsedNodeId.setStatus("current")
_SystemStatusLocalRack_Type = Unsigned32
_SystemStatusLocalRack_Object = MibTableColumn
systemStatusLocalRack = _SystemStatusLocalRack_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1, 6),
    _SystemStatusLocalRack_Type()
)
systemStatusLocalRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusLocalRack.setStatus("current")
_SystemStatusLocalSlot_Type = Unsigned32
_SystemStatusLocalSlot_Object = MibTableColumn
systemStatusLocalSlot = _SystemStatusLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 100, 1, 7),
    _SystemStatusLocalSlot_Type()
)
systemStatusLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusLocalSlot.setStatus("current")
_ModuleInventoryTable_Object = MibTable
moduleInventoryTable = _ModuleInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101)
)
if mibBuilder.loadTexts:
    moduleInventoryTable.setStatus("current")
_ModuleInventoryEntry_Object = MibTableRow
moduleInventoryEntry = _ModuleInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1)
)
moduleInventoryEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "moduleInventoryIndex"),
)
if mibBuilder.loadTexts:
    moduleInventoryEntry.setStatus("current")


class _ModuleInventoryIndex_Type(Integer32):
    """Custom type moduleInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_ModuleInventoryIndex_Type.__name__ = "Integer32"
_ModuleInventoryIndex_Object = MibTableColumn
moduleInventoryIndex = _ModuleInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 1),
    _ModuleInventoryIndex_Type()
)
moduleInventoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleInventoryIndex.setStatus("current")
_ModuleInventoryExpectedModule_Type = DisplayString
_ModuleInventoryExpectedModule_Object = MibTableColumn
moduleInventoryExpectedModule = _ModuleInventoryExpectedModule_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 2),
    _ModuleInventoryExpectedModule_Type()
)
moduleInventoryExpectedModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryExpectedModule.setStatus("current")
_ModuleInventoryModule_Type = DisplayString
_ModuleInventoryModule_Object = MibTableColumn
moduleInventoryModule = _ModuleInventoryModule_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 3),
    _ModuleInventoryModule_Type()
)
moduleInventoryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryModule.setStatus("current")


class _ModuleInventoryType_Type(Integer32):
    """Custom type moduleInventoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("unknown", 1),
          ("transponder", 2),
          ("measurement", 3),
          ("amplifier", 4),
          ("management", 5),
          ("passive", 6),
          ("occupied", 7))
    )


_ModuleInventoryType_Type.__name__ = "Integer32"
_ModuleInventoryType_Object = MibTableColumn
moduleInventoryType = _ModuleInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 4),
    _ModuleInventoryType_Type()
)
moduleInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryType.setStatus("current")


class _ModuleInventoryBoardCode_Type(Integer32):
    """Custom type moduleInventoryBoardCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleInventoryBoardCode_Type.__name__ = "Integer32"
_ModuleInventoryBoardCode_Object = MibTableColumn
moduleInventoryBoardCode = _ModuleInventoryBoardCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 5),
    _ModuleInventoryBoardCode_Type()
)
moduleInventoryBoardCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryBoardCode.setStatus("current")
_ModuleInventoryAdditionalInfo_Type = DisplayString
_ModuleInventoryAdditionalInfo_Object = MibTableColumn
moduleInventoryAdditionalInfo = _ModuleInventoryAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 6),
    _ModuleInventoryAdditionalInfo_Type()
)
moduleInventoryAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryAdditionalInfo.setStatus("current")
_ModuleInventorySerialNumber_Type = DisplayString
_ModuleInventorySerialNumber_Object = MibTableColumn
moduleInventorySerialNumber = _ModuleInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 7),
    _ModuleInventorySerialNumber_Type()
)
moduleInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventorySerialNumber.setStatus("current")
_ModuleInventoryOccupiedSlots_Type = Unsigned32
_ModuleInventoryOccupiedSlots_Object = MibTableColumn
moduleInventoryOccupiedSlots = _ModuleInventoryOccupiedSlots_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 8),
    _ModuleInventoryOccupiedSlots_Type()
)
moduleInventoryOccupiedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryOccupiedSlots.setStatus("current")
_ModuleInventoryProjectNumber_Type = DisplayString
_ModuleInventoryProjectNumber_Object = MibTableColumn
moduleInventoryProjectNumber = _ModuleInventoryProjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 9),
    _ModuleInventoryProjectNumber_Type()
)
moduleInventoryProjectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryProjectNumber.setStatus("current")
_ModuleInventoryBuildVersion_Type = DisplayString
_ModuleInventoryBuildVersion_Object = MibTableColumn
moduleInventoryBuildVersion = _ModuleInventoryBuildVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 10),
    _ModuleInventoryBuildVersion_Type()
)
moduleInventoryBuildVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryBuildVersion.setStatus("current")
_ModuleInventoryProductionDate_Type = DisplayString
_ModuleInventoryProductionDate_Object = MibTableColumn
moduleInventoryProductionDate = _ModuleInventoryProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 11),
    _ModuleInventoryProductionDate_Type()
)
moduleInventoryProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryProductionDate.setStatus("current")
_ModuleInventoryMfgTestInfo_Type = DisplayString
_ModuleInventoryMfgTestInfo_Object = MibTableColumn
moduleInventoryMfgTestInfo = _ModuleInventoryMfgTestInfo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 12),
    _ModuleInventoryMfgTestInfo_Type()
)
moduleInventoryMfgTestInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryMfgTestInfo.setStatus("current")


class _ModuleInventoryNumberOfOpticalPorts_Type(Integer32):
    """Custom type moduleInventoryNumberOfOpticalPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleInventoryNumberOfOpticalPorts_Type.__name__ = "Integer32"
_ModuleInventoryNumberOfOpticalPorts_Object = MibTableColumn
moduleInventoryNumberOfOpticalPorts = _ModuleInventoryNumberOfOpticalPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 13),
    _ModuleInventoryNumberOfOpticalPorts_Type()
)
moduleInventoryNumberOfOpticalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryNumberOfOpticalPorts.setStatus("current")


class _ModuleInventoryNumberOfSfpPorts_Type(Integer32):
    """Custom type moduleInventoryNumberOfSfpPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleInventoryNumberOfSfpPorts_Type.__name__ = "Integer32"
_ModuleInventoryNumberOfSfpPorts_Object = MibTableColumn
moduleInventoryNumberOfSfpPorts = _ModuleInventoryNumberOfSfpPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 14),
    _ModuleInventoryNumberOfSfpPorts_Type()
)
moduleInventoryNumberOfSfpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryNumberOfSfpPorts.setStatus("current")


class _ModuleInventoryNumberOfXfpPorts_Type(Integer32):
    """Custom type moduleInventoryNumberOfXfpPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleInventoryNumberOfXfpPorts_Type.__name__ = "Integer32"
_ModuleInventoryNumberOfXfpPorts_Object = MibTableColumn
moduleInventoryNumberOfXfpPorts = _ModuleInventoryNumberOfXfpPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 15),
    _ModuleInventoryNumberOfXfpPorts_Type()
)
moduleInventoryNumberOfXfpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryNumberOfXfpPorts.setStatus("current")
_ModuleInventoryCoreFirmwareVersion_Type = DisplayString
_ModuleInventoryCoreFirmwareVersion_Object = MibTableColumn
moduleInventoryCoreFirmwareVersion = _ModuleInventoryCoreFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 16),
    _ModuleInventoryCoreFirmwareVersion_Type()
)
moduleInventoryCoreFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryCoreFirmwareVersion.setStatus("current")
_ModuleInventoryCoreFirmwareDate_Type = DisplayString
_ModuleInventoryCoreFirmwareDate_Object = MibTableColumn
moduleInventoryCoreFirmwareDate = _ModuleInventoryCoreFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 17),
    _ModuleInventoryCoreFirmwareDate_Type()
)
moduleInventoryCoreFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryCoreFirmwareDate.setStatus("current")
_ModuleInventoryApplFirmwareVersion_Type = DisplayString
_ModuleInventoryApplFirmwareVersion_Object = MibTableColumn
moduleInventoryApplFirmwareVersion = _ModuleInventoryApplFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 18),
    _ModuleInventoryApplFirmwareVersion_Type()
)
moduleInventoryApplFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryApplFirmwareVersion.setStatus("current")
_ModuleInventoryApplFirmwareDate_Type = DisplayString
_ModuleInventoryApplFirmwareDate_Object = MibTableColumn
moduleInventoryApplFirmwareDate = _ModuleInventoryApplFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 101, 1, 19),
    _ModuleInventoryApplFirmwareDate_Type()
)
moduleInventoryApplFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInventoryApplFirmwareDate.setStatus("current")
_ModuleStatusTable_Object = MibTable
moduleStatusTable = _ModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102)
)
if mibBuilder.loadTexts:
    moduleStatusTable.setStatus("current")
_ModuleStatusEntry_Object = MibTableRow
moduleStatusEntry = _ModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1)
)
moduleStatusEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "moduleStatusIndex"),
)
if mibBuilder.loadTexts:
    moduleStatusEntry.setStatus("current")


class _ModuleStatusIndex_Type(Integer32):
    """Custom type moduleStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_ModuleStatusIndex_Type.__name__ = "Integer32"
_ModuleStatusIndex_Object = MibTableColumn
moduleStatusIndex = _ModuleStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 1),
    _ModuleStatusIndex_Type()
)
moduleStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleStatusIndex.setStatus("current")
_ModuleStatusModule_Type = DisplayString
_ModuleStatusModule_Object = MibTableColumn
moduleStatusModule = _ModuleStatusModule_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 2),
    _ModuleStatusModule_Type()
)
moduleStatusModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusModule.setStatus("current")


class _ModuleStatusSystemOk_Type(Integer32):
    """Custom type moduleStatusSystemOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ModuleStatusSystemOk_Type.__name__ = "Integer32"
_ModuleStatusSystemOk_Object = MibTableColumn
moduleStatusSystemOk = _ModuleStatusSystemOk_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 3),
    _ModuleStatusSystemOk_Type()
)
moduleStatusSystemOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusSystemOk.setStatus("current")


class _ModuleStatusErrorCondition_Type(Integer32):
    """Custom type moduleStatusErrorCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ModuleStatusErrorCondition_Type.__name__ = "Integer32"
_ModuleStatusErrorCondition_Object = MibTableColumn
moduleStatusErrorCondition = _ModuleStatusErrorCondition_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 4),
    _ModuleStatusErrorCondition_Type()
)
moduleStatusErrorCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusErrorCondition.setStatus("current")


class _ModuleStatusTestMode_Type(Integer32):
    """Custom type moduleStatusTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ModuleStatusTestMode_Type.__name__ = "Integer32"
_ModuleStatusTestMode_Object = MibTableColumn
moduleStatusTestMode = _ModuleStatusTestMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 5),
    _ModuleStatusTestMode_Type()
)
moduleStatusTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusTestMode.setStatus("current")


class _ModuleStatusSparePart_Type(Integer32):
    """Custom type moduleStatusSparePart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ModuleStatusSparePart_Type.__name__ = "Integer32"
_ModuleStatusSparePart_Object = MibTableColumn
moduleStatusSparePart = _ModuleStatusSparePart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 6),
    _ModuleStatusSparePart_Type()
)
moduleStatusSparePart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusSparePart.setStatus("current")
_ModuleStatusUptime_Type = Counter32
_ModuleStatusUptime_Object = MibTableColumn
moduleStatusUptime = _ModuleStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 7),
    _ModuleStatusUptime_Type()
)
moduleStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusUptime.setStatus("current")
_ModuleStatusTimeSinceCounterReset_Type = Counter32
_ModuleStatusTimeSinceCounterReset_Object = MibTableColumn
moduleStatusTimeSinceCounterReset = _ModuleStatusTimeSinceCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 8),
    _ModuleStatusTimeSinceCounterReset_Type()
)
moduleStatusTimeSinceCounterReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusTimeSinceCounterReset.setStatus("current")


class _ModuleStatusTemperature_Type(Integer32):
    """Custom type moduleStatusTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleStatusTemperature_Type.__name__ = "Integer32"
_ModuleStatusTemperature_Object = MibTableColumn
moduleStatusTemperature = _ModuleStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 9),
    _ModuleStatusTemperature_Type()
)
moduleStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusTemperature.setStatus("current")


class _ModuleStatusTooHot_Type(Integer32):
    """Custom type moduleStatusTooHot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ModuleStatusTooHot_Type.__name__ = "Integer32"
_ModuleStatusTooHot_Object = MibTableColumn
moduleStatusTooHot = _ModuleStatusTooHot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 10),
    _ModuleStatusTooHot_Type()
)
moduleStatusTooHot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusTooHot.setStatus("current")


class _ModuleStatusBackupState_Type(Bits):
    """Custom type moduleStatusBackupState based on Bits"""
    namedValues = NamedValues(
        *(("disrupted", 0),
          ("backup", 1),
          ("awaitSwitchback", 2),
          ("manual", 3))
    )

_ModuleStatusBackupState_Type.__name__ = "Bits"
_ModuleStatusBackupState_Object = MibTableColumn
moduleStatusBackupState = _ModuleStatusBackupState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 11),
    _ModuleStatusBackupState_Type()
)
moduleStatusBackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusBackupState.setStatus("current")
_ModuleStatusBackupCounter_Type = Unsigned32
_ModuleStatusBackupCounter_Object = MibTableColumn
moduleStatusBackupCounter = _ModuleStatusBackupCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 12),
    _ModuleStatusBackupCounter_Type()
)
moduleStatusBackupCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusBackupCounter.setStatus("current")
_ModuleStatusBackupDuration_Type = Counter32
_ModuleStatusBackupDuration_Object = MibTableColumn
moduleStatusBackupDuration = _ModuleStatusBackupDuration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 102, 1, 13),
    _ModuleStatusBackupDuration_Type()
)
moduleStatusBackupDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatusBackupDuration.setStatus("current")
_PortStatusTable_Object = MibTable
portStatusTable = _PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103)
)
if mibBuilder.loadTexts:
    portStatusTable.setStatus("current")
_PortStatusEntry_Object = MibTableRow
portStatusEntry = _PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1)
)
portStatusEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "portStatusPortIndex"),
)
if mibBuilder.loadTexts:
    portStatusEntry.setStatus("current")


class _PortStatusPortIndex_Type(Integer32):
    """Custom type portStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_PortStatusPortIndex_Type.__name__ = "Integer32"
_PortStatusPortIndex_Object = MibTableColumn
portStatusPortIndex = _PortStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 1),
    _PortStatusPortIndex_Type()
)
portStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portStatusPortIndex.setStatus("current")
_PortStatusModule_Type = DisplayString
_PortStatusModule_Object = MibTableColumn
portStatusModule = _PortStatusModule_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 2),
    _PortStatusModule_Type()
)
portStatusModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusModule.setStatus("current")
_PortStatusLocation_Type = DisplayString
_PortStatusLocation_Object = MibTableColumn
portStatusLocation = _PortStatusLocation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 3),
    _PortStatusLocation_Type()
)
portStatusLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLocation.setStatus("current")
_PortStatusSnmpPort_Type = Unsigned32
_PortStatusSnmpPort_Object = MibTableColumn
portStatusSnmpPort = _PortStatusSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 4),
    _PortStatusSnmpPort_Type()
)
portStatusSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusSnmpPort.setStatus("current")
_PortStatusAlias_Type = DisplayString
_PortStatusAlias_Object = MibTableColumn
portStatusAlias = _PortStatusAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 5),
    _PortStatusAlias_Type()
)
portStatusAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusAlias.setStatus("current")


class _PortStatusAdminStatus_Type(Integer32):
    """Custom type portStatusAdminStatus based on Integer32"""
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
        *(("none", 0),
          ("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_PortStatusAdminStatus_Type.__name__ = "Integer32"
_PortStatusAdminStatus_Object = MibTableColumn
portStatusAdminStatus = _PortStatusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 6),
    _PortStatusAdminStatus_Type()
)
portStatusAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusAdminStatus.setStatus("current")


class _PortStatusOperStatus_Type(Integer32):
    """Custom type portStatusOperStatus based on Integer32"""
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
        *(("none", 0),
          ("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_PortStatusOperStatus_Type.__name__ = "Integer32"
_PortStatusOperStatus_Object = MibTableColumn
portStatusOperStatus = _PortStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 7),
    _PortStatusOperStatus_Type()
)
portStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusOperStatus.setStatus("current")


class _PortStatusDetailedStatus_Type(Bits):
    """Custom type portStatusDetailedStatus based on Bits"""
    namedValues = NamedValues(
        *(("disabled", 0),
          ("sfpMissing", 1),
          ("pllNotLocked", 2),
          ("signalLow", 3),
          ("tooHigh", 4),
          ("laserOff", 5),
          ("loop", 6),
          ("reserved", 7),
          ("unknown", 8),
          ("none", 9))
    )

_PortStatusDetailedStatus_Type.__name__ = "Bits"
_PortStatusDetailedStatus_Object = MibTableColumn
portStatusDetailedStatus = _PortStatusDetailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 8),
    _PortStatusDetailedStatus_Type()
)
portStatusDetailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDetailedStatus.setStatus("current")


class _PortStatusPortDatarate_Type(Integer32):
    """Custom type portStatusPortDatarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              10,
              11,
              12,
              13,
              14,
              15,
              20,
              21,
              22,
              23,
              30,
              31,
              32,
              33,
              34,
              35,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("txp", 1),
          ("ms100mEth", 2),
          ("ms1gEth", 3),
          ("ms10gEth", 4),
          ("ms1xFc", 10),
          ("ms2xFc", 11),
          ("ms4xFc", 12),
          ("ms8xFc", 13),
          ("ms10xFc", 14),
          ("ms16xFc", 15),
          ("oc3", 20),
          ("oc12", 21),
          ("oc48", 22),
          ("oc192", 23),
          ("otu1", 30),
          ("otu1e", 31),
          ("otu1f", 32),
          ("otu2", 33),
          ("otu2e", 34),
          ("otu2f", 35),
          ("fix100", 40),
          ("escon", 41),
          ("sdi", 42),
          ("hdtv", 43),
          ("tdm2", 44),
          ("other", 45))
    )


_PortStatusPortDatarate_Type.__name__ = "Integer32"
_PortStatusPortDatarate_Object = MibTableColumn
portStatusPortDatarate = _PortStatusPortDatarate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 9),
    _PortStatusPortDatarate_Type()
)
portStatusPortDatarate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusPortDatarate.setStatus("current")
_PortStatusUpdateTimeStamp_Type = DisplayString
_PortStatusUpdateTimeStamp_Object = MibTableColumn
portStatusUpdateTimeStamp = _PortStatusUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 10),
    _PortStatusUpdateTimeStamp_Type()
)
portStatusUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusUpdateTimeStamp.setStatus("current")
_PortStatusTimeSinceValueReset_Type = Counter32
_PortStatusTimeSinceValueReset_Object = MibTableColumn
portStatusTimeSinceValueReset = _PortStatusTimeSinceValueReset_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 11),
    _PortStatusTimeSinceValueReset_Type()
)
portStatusTimeSinceValueReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusTimeSinceValueReset.setStatus("current")
_PortStatusTimeSinceLastError_Type = Counter32
_PortStatusTimeSinceLastError_Object = MibTableColumn
portStatusTimeSinceLastError = _PortStatusTimeSinceLastError_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 12),
    _PortStatusTimeSinceLastError_Type()
)
portStatusTimeSinceLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusTimeSinceLastError.setStatus("current")
_PortStatusTimeSignalTooLow_Type = Counter32
_PortStatusTimeSignalTooLow_Object = MibTableColumn
portStatusTimeSignalTooLow = _PortStatusTimeSignalTooLow_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 13),
    _PortStatusTimeSignalTooLow_Type()
)
portStatusTimeSignalTooLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusTimeSignalTooLow.setStatus("current")
_PortStatusSignalTooLowCounter_Type = Unsigned32
_PortStatusSignalTooLowCounter_Object = MibTableColumn
portStatusSignalTooLowCounter = _PortStatusSignalTooLowCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 14),
    _PortStatusSignalTooLowCounter_Type()
)
portStatusSignalTooLowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusSignalTooLowCounter.setStatus("current")
_PortStatusTimeSignalTooHigh_Type = Counter32
_PortStatusTimeSignalTooHigh_Object = MibTableColumn
portStatusTimeSignalTooHigh = _PortStatusTimeSignalTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 15),
    _PortStatusTimeSignalTooHigh_Type()
)
portStatusTimeSignalTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusTimeSignalTooHigh.setStatus("current")
_PortStatusSignalTooHighCounter_Type = Unsigned32
_PortStatusSignalTooHighCounter_Object = MibTableColumn
portStatusSignalTooHighCounter = _PortStatusSignalTooHighCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 16),
    _PortStatusSignalTooHighCounter_Type()
)
portStatusSignalTooHighCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusSignalTooHighCounter.setStatus("current")
_PortStatusLowThreshold_Type = DisplayString
_PortStatusLowThreshold_Object = MibTableColumn
portStatusLowThreshold = _PortStatusLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 17),
    _PortStatusLowThreshold_Type()
)
portStatusLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLowThreshold.setStatus("current")
_PortStatusCurrentInputSignal_Type = DisplayString
_PortStatusCurrentInputSignal_Object = MibTableColumn
portStatusCurrentInputSignal = _PortStatusCurrentInputSignal_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 18),
    _PortStatusCurrentInputSignal_Type()
)
portStatusCurrentInputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusCurrentInputSignal.setStatus("current")
_PortStatusHighThreshold_Type = DisplayString
_PortStatusHighThreshold_Object = MibTableColumn
portStatusHighThreshold = _PortStatusHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 103, 1, 19),
    _PortStatusHighThreshold_Type()
)
portStatusHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusHighThreshold.setStatus("current")
_EmStatusTable_Object = MibTable
emStatusTable = _EmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104)
)
if mibBuilder.loadTexts:
    emStatusTable.setStatus("current")
_EmStatusEntry_Object = MibTableRow
emStatusEntry = _EmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1)
)
emStatusEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "emStatusIndex"),
)
if mibBuilder.loadTexts:
    emStatusEntry.setStatus("current")


class _EmStatusIndex_Type(Integer32):
    """Custom type emStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_EmStatusIndex_Type.__name__ = "Integer32"
_EmStatusIndex_Object = MibTableColumn
emStatusIndex = _EmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 1),
    _EmStatusIndex_Type()
)
emStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emStatusIndex.setStatus("current")


class _EmStatusSystemOk_Type(Integer32):
    """Custom type emStatusSystemOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_EmStatusSystemOk_Type.__name__ = "Integer32"
_EmStatusSystemOk_Object = MibTableColumn
emStatusSystemOk = _EmStatusSystemOk_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 2),
    _EmStatusSystemOk_Type()
)
emStatusSystemOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusSystemOk.setStatus("current")


class _EmStatusErrors_Type(Bits):
    """Custom type emStatusErrors based on Bits"""
    namedValues = NamedValues(
        *(("lossOfInput", 0),
          ("lossOfOutput", 1),
          ("tooHot", 2),
          ("eyeSafetyShutdown", 3),
          ("backReflection", 4),
          ("powerLimit", 5),
          ("overCurrent", 6),
          ("pumpDown", 7))
    )

_EmStatusErrors_Type.__name__ = "Bits"
_EmStatusErrors_Object = MibTableColumn
emStatusErrors = _EmStatusErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 3),
    _EmStatusErrors_Type()
)
emStatusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusErrors.setStatus("current")
_EmStatusHardwareCode_Type = DisplayString
_EmStatusHardwareCode_Object = MibTableColumn
emStatusHardwareCode = _EmStatusHardwareCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 4),
    _EmStatusHardwareCode_Type()
)
emStatusHardwareCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusHardwareCode.setStatus("current")
_EmStatusTimeSincePowerError_Type = Counter32
_EmStatusTimeSincePowerError_Object = MibTableColumn
emStatusTimeSincePowerError = _EmStatusTimeSincePowerError_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 5),
    _EmStatusTimeSincePowerError_Type()
)
emStatusTimeSincePowerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusTimeSincePowerError.setStatus("current")
_EmStatusTimeWithPowerLoss_Type = Counter32
_EmStatusTimeWithPowerLoss_Object = MibTableColumn
emStatusTimeWithPowerLoss = _EmStatusTimeWithPowerLoss_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 6),
    _EmStatusTimeWithPowerLoss_Type()
)
emStatusTimeWithPowerLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusTimeWithPowerLoss.setStatus("current")
_EmStatusInputSignalLowCounter_Type = Unsigned32
_EmStatusInputSignalLowCounter_Object = MibTableColumn
emStatusInputSignalLowCounter = _EmStatusInputSignalLowCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 7),
    _EmStatusInputSignalLowCounter_Type()
)
emStatusInputSignalLowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusInputSignalLowCounter.setStatus("current")
_EmStatusInputPower_Type = DisplayString
_EmStatusInputPower_Object = MibTableColumn
emStatusInputPower = _EmStatusInputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 8),
    _EmStatusInputPower_Type()
)
emStatusInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusInputPower.setStatus("current")
_EmStatusSignalGain_Type = DisplayString
_EmStatusSignalGain_Object = MibTableColumn
emStatusSignalGain = _EmStatusSignalGain_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 9),
    _EmStatusSignalGain_Type()
)
emStatusSignalGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusSignalGain.setStatus("current")
_EmStatusOptimalFlatGain_Type = DisplayString
_EmStatusOptimalFlatGain_Object = MibTableColumn
emStatusOptimalFlatGain = _EmStatusOptimalFlatGain_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 10),
    _EmStatusOptimalFlatGain_Type()
)
emStatusOptimalFlatGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusOptimalFlatGain.setStatus("current")
_EmStatusBackReflection_Type = DisplayString
_EmStatusBackReflection_Object = MibTableColumn
emStatusBackReflection = _EmStatusBackReflection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 11),
    _EmStatusBackReflection_Type()
)
emStatusBackReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusBackReflection.setStatus("current")
_EmStatusSignalOutputPower_Type = DisplayString
_EmStatusSignalOutputPower_Object = MibTableColumn
emStatusSignalOutputPower = _EmStatusSignalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 12),
    _EmStatusSignalOutputPower_Type()
)
emStatusSignalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusSignalOutputPower.setStatus("current")
_EmStatusTotalOutputPower_Type = DisplayString
_EmStatusTotalOutputPower_Object = MibTableColumn
emStatusTotalOutputPower = _EmStatusTotalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 13),
    _EmStatusTotalOutputPower_Type()
)
emStatusTotalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusTotalOutputPower.setStatus("current")
_EmStatusMinOutputPower_Type = DisplayString
_EmStatusMinOutputPower_Object = MibTableColumn
emStatusMinOutputPower = _EmStatusMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 14),
    _EmStatusMinOutputPower_Type()
)
emStatusMinOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusMinOutputPower.setStatus("current")
_EmStatusMaxOutputPower_Type = DisplayString
_EmStatusMaxOutputPower_Object = MibTableColumn
emStatusMaxOutputPower = _EmStatusMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 15),
    _EmStatusMaxOutputPower_Type()
)
emStatusMaxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusMaxOutputPower.setStatus("current")
_EmStatusCfgOutputPower_Type = DisplayString
_EmStatusCfgOutputPower_Object = MibTableColumn
emStatusCfgOutputPower = _EmStatusCfgOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 104, 1, 16),
    _EmStatusCfgOutputPower_Type()
)
emStatusCfgOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emStatusCfgOutputPower.setStatus("current")
_BertStatusTable_Object = MibTable
bertStatusTable = _BertStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105)
)
if mibBuilder.loadTexts:
    bertStatusTable.setStatus("current")
_BertStatusEntry_Object = MibTableRow
bertStatusEntry = _BertStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1)
)
bertStatusEntry.setIndexNames(
    (0, "G6-MSP1000-MIB", "bertStatusIndex"),
)
if mibBuilder.loadTexts:
    bertStatusEntry.setStatus("current")


class _BertStatusIndex_Type(Integer32):
    """Custom type bertStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_BertStatusIndex_Type.__name__ = "Integer32"
_BertStatusIndex_Object = MibTableColumn
bertStatusIndex = _BertStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 1),
    _BertStatusIndex_Type()
)
bertStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bertStatusIndex.setStatus("current")
_BertStatusLocation_Type = DisplayString
_BertStatusLocation_Object = MibTableColumn
bertStatusLocation = _BertStatusLocation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 2),
    _BertStatusLocation_Type()
)
bertStatusLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusLocation.setStatus("current")


class _BertStatusBertOperation_Type(Integer32):
    """Custom type bertStatusBertOperation based on Integer32"""
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
        *(("unused", 0),
          ("inSync", 1),
          ("wasOutOfSync", 2),
          ("outOfSync", 3))
    )


_BertStatusBertOperation_Type.__name__ = "Integer32"
_BertStatusBertOperation_Object = MibTableColumn
bertStatusBertOperation = _BertStatusBertOperation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 3),
    _BertStatusBertOperation_Type()
)
bertStatusBertOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusBertOperation.setStatus("current")
_BertStatusTotalErrors_Type = Unsigned32
_BertStatusTotalErrors_Object = MibTableColumn
bertStatusTotalErrors = _BertStatusTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 4),
    _BertStatusTotalErrors_Type()
)
bertStatusTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusTotalErrors.setStatus("current")
_BertStatusTimeSinceLastError_Type = Counter32
_BertStatusTimeSinceLastError_Object = MibTableColumn
bertStatusTimeSinceLastError = _BertStatusTimeSinceLastError_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 5),
    _BertStatusTimeSinceLastError_Type()
)
bertStatusTimeSinceLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusTimeSinceLastError.setStatus("current")
_BertStatusTotalTestTime_Type = Counter32
_BertStatusTotalTestTime_Object = MibTableColumn
bertStatusTotalTestTime = _BertStatusTotalTestTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 6),
    _BertStatusTotalTestTime_Type()
)
bertStatusTotalTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusTotalTestTime.setStatus("current")
_BertStatusErroredTime_Type = Counter32
_BertStatusErroredTime_Object = MibTableColumn
bertStatusErroredTime = _BertStatusErroredTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 7),
    _BertStatusErroredTime_Type()
)
bertStatusErroredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusErroredTime.setStatus("current")
_BertStatusBitErrorRate_Type = DisplayString
_BertStatusBitErrorRate_Object = MibTableColumn
bertStatusBitErrorRate = _BertStatusBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 8),
    _BertStatusBitErrorRate_Type()
)
bertStatusBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusBitErrorRate.setStatus("current")
_BertStatusBerSinceLastError_Type = DisplayString
_BertStatusBerSinceLastError_Object = MibTableColumn
bertStatusBerSinceLastError = _BertStatusBerSinceLastError_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 9),
    _BertStatusBerSinceLastError_Type()
)
bertStatusBerSinceLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusBerSinceLastError.setStatus("current")
_BertStatusTheoreticalBer_Type = DisplayString
_BertStatusTheoreticalBer_Object = MibTableColumn
bertStatusTheoreticalBer = _BertStatusTheoreticalBer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 10),
    _BertStatusTheoreticalBer_Type()
)
bertStatusTheoreticalBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusTheoreticalBer.setStatus("current")
_BertStatusAvailability_Type = DisplayString
_BertStatusAvailability_Object = MibTableColumn
bertStatusAvailability = _BertStatusAvailability_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 94, 105, 1, 11),
    _BertStatusAvailability_Type()
)
bertStatusAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatusAvailability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-MSP1000-MIB",
    **{"device": device,
       "msp1000": msp1000,
       "systemConfigTable": systemConfigTable,
       "systemConfigEntry": systemConfigEntry,
       "systemConfigIndex": systemConfigIndex,
       "systemConfigNmsOperationMode": systemConfigNmsOperationMode,
       "systemConfigCoreMode": systemConfigCoreMode,
       "systemConfigNodeId": systemConfigNodeId,
       "systemConfigDisableLegacyAccess": systemConfigDisableLegacyAccess,
       "slotConfigTable": slotConfigTable,
       "slotConfigEntry": slotConfigEntry,
       "slotConfigIndex": slotConfigIndex,
       "slotConfigModule": slotConfigModule,
       "slotConfigSparepartMode": slotConfigSparepartMode,
       "slotConfigPort1Alias": slotConfigPort1Alias,
       "slotConfigPort2Alias": slotConfigPort2Alias,
       "slotConfigPort3Alias": slotConfigPort3Alias,
       "slotConfigPort4Alias": slotConfigPort4Alias,
       "x2gConfigTable": x2gConfigTable,
       "x2gConfigEntry": x2gConfigEntry,
       "x2gConfigIndex": x2gConfigIndex,
       "x2gConfigPort1Datarate": x2gConfigPort1Datarate,
       "x2gConfigPort2Datarate": x2gConfigPort2Datarate,
       "x2gConfigPort3Datarate": x2gConfigPort3Datarate,
       "x2gConfigPort4Datarate": x2gConfigPort4Datarate,
       "x2gConfigCrossConnect": x2gConfigCrossConnect,
       "x2gConfigDeactivatePort1": x2gConfigDeactivatePort1,
       "x2gConfigDeactivatePort2": x2gConfigDeactivatePort2,
       "x2gConfigDeactivatePort3": x2gConfigDeactivatePort3,
       "x2gConfigDeactivatePort4": x2gConfigDeactivatePort4,
       "x2gConfigFrontPanelMode": x2gConfigFrontPanelMode,
       "x2gConfigLossOfSignalHandling": x2gConfigLossOfSignalHandling,
       "x2gConfigOptimizedFor8b10b": x2gConfigOptimizedFor8b10b,
       "x2gConfigBertPattern": x2gConfigBertPattern,
       "x2gConfigSfpDeltaInterval": x2gConfigSfpDeltaInterval,
       "x2gConfigSfpDeltaThreshold": x2gConfigSfpDeltaThreshold,
       "x2gConfigBackupTrigger": x2gConfigBackupTrigger,
       "x2gConfigStayWithLastLink": x2gConfigStayWithLastLink,
       "x2gConfigBackupEnd": x2gConfigBackupEnd,
       "x2gConfigPermitLinkOverride": x2gConfigPermitLinkOverride,
       "txgConfigTable": txgConfigTable,
       "txgConfigEntry": txgConfigEntry,
       "txgConfigIndex": txgConfigIndex,
       "txgConfigTxgDatarate": txgConfigTxgDatarate,
       "txgConfigTxgOperationMode": txgConfigTxgOperationMode,
       "txgConfigPort1ItuChannel": txgConfigPort1ItuChannel,
       "txgConfigPort2ItuChannel": txgConfigPort2ItuChannel,
       "txgConfigDeactivatePort1": txgConfigDeactivatePort1,
       "txgConfigDeactivatePort2": txgConfigDeactivatePort2,
       "txgConfigFrontPanelMode": txgConfigFrontPanelMode,
       "txgConfigLossOfSignalHandling": txgConfigLossOfSignalHandling,
       "txgConfigBertPattern": txgConfigBertPattern,
       "txgConfigSfpDeltaInterval": txgConfigSfpDeltaInterval,
       "txgConfigSfpDeltaThreshold": txgConfigSfpDeltaThreshold,
       "cxgPlusConfigTable": cxgPlusConfigTable,
       "cxgPlusConfigEntry": cxgPlusConfigEntry,
       "cxgPlusConfigIndex": cxgPlusConfigIndex,
       "cxgPlusConfigCxgPort12Datarate": cxgPlusConfigCxgPort12Datarate,
       "cxgPlusConfigCxgPort34Datarate": cxgPlusConfigCxgPort34Datarate,
       "cxgPlusConfigPort1ItuChannel": cxgPlusConfigPort1ItuChannel,
       "cxgPlusConfigPort2ItuChannel": cxgPlusConfigPort2ItuChannel,
       "cxgPlusConfigPort3ItuChannel": cxgPlusConfigPort3ItuChannel,
       "cxgPlusConfigPort4ItuChannel": cxgPlusConfigPort4ItuChannel,
       "cxgPlusConfigDeactivatePort1": cxgPlusConfigDeactivatePort1,
       "cxgPlusConfigDeactivatePort2": cxgPlusConfigDeactivatePort2,
       "cxgPlusConfigDeactivatePort3": cxgPlusConfigDeactivatePort3,
       "cxgPlusConfigDeactivatePort4": cxgPlusConfigDeactivatePort4,
       "cxgPlusConfigFrontPanelMode": cxgPlusConfigFrontPanelMode,
       "cxgPlusConfigLossOfSignalHandling": cxgPlusConfigLossOfSignalHandling,
       "cxgPlusConfigSfpDeltaInterval": cxgPlusConfigSfpDeltaInterval,
       "cxgPlusConfigSfpDeltaThreshold": cxgPlusConfigSfpDeltaThreshold,
       "cxgConfigTable": cxgConfigTable,
       "cxgConfigEntry": cxgConfigEntry,
       "cxgConfigIndex": cxgConfigIndex,
       "cxgConfigCxgPort12Datarate": cxgConfigCxgPort12Datarate,
       "cxgConfigPort1ItuChannel": cxgConfigPort1ItuChannel,
       "cxgConfigPort2ItuChannel": cxgConfigPort2ItuChannel,
       "cxgConfigDeactivatePort1": cxgConfigDeactivatePort1,
       "cxgConfigDeactivatePort2": cxgConfigDeactivatePort2,
       "cxgConfigFrontPanelMode": cxgConfigFrontPanelMode,
       "cxgConfigLossOfSignalHandling": cxgConfigLossOfSignalHandling,
       "cxgConfigSfpDeltaInterval": cxgConfigSfpDeltaInterval,
       "cxgConfigSfpDeltaThreshold": cxgConfigSfpDeltaThreshold,
       "t4gConfigTable": t4gConfigTable,
       "t4gConfigEntry": t4gConfigEntry,
       "t4gConfigIndex": t4gConfigIndex,
       "t4gConfigT4gPort12Datarate": t4gConfigT4gPort12Datarate,
       "t4gConfigT4gPort34Datarate": t4gConfigT4gPort34Datarate,
       "t4gConfigT4gOperationMode": t4gConfigT4gOperationMode,
       "t4gConfigDeactivatePort1": t4gConfigDeactivatePort1,
       "t4gConfigDeactivatePort2": t4gConfigDeactivatePort2,
       "t4gConfigDeactivatePort3": t4gConfigDeactivatePort3,
       "t4gConfigDeactivatePort4": t4gConfigDeactivatePort4,
       "t4gConfigFrontPanelMode": t4gConfigFrontPanelMode,
       "t4gConfigLossOfSignalHandling": t4gConfigLossOfSignalHandling,
       "t4gConfigBertPattern": t4gConfigBertPattern,
       "t4gConfigSfpDeltaInterval": t4gConfigSfpDeltaInterval,
       "t4gConfigSfpDeltaThreshold": t4gConfigSfpDeltaThreshold,
       "m2gConfigTable": m2gConfigTable,
       "m2gConfigEntry": m2gConfigEntry,
       "m2gConfigIndex": m2gConfigIndex,
       "m2gConfigChannel1Datarate": m2gConfigChannel1Datarate,
       "m2gConfigChannel2Datarate": m2gConfigChannel2Datarate,
       "m2gConfigPort1CopperSfp": m2gConfigPort1CopperSfp,
       "m2gConfigPort2CopperSfp": m2gConfigPort2CopperSfp,
       "m2gConfigSfpDeltaInterval": m2gConfigSfpDeltaInterval,
       "m2gConfigSfpDeltaThreshold": m2gConfigSfpDeltaThreshold,
       "m2gConfigLinkBackupTrigger": m2gConfigLinkBackupTrigger,
       "m2gConfigStayWithLastLink": m2gConfigStayWithLastLink,
       "m2gConfigBackupEnd": m2gConfigBackupEnd,
       "m2gConfigPermitLinkOverride": m2gConfigPermitLinkOverride,
       "om1ConfigTable": om1ConfigTable,
       "om1ConfigEntry": om1ConfigEntry,
       "om1ConfigIndex": om1ConfigIndex,
       "om1ConfigWavelengthPortA": om1ConfigWavelengthPortA,
       "om1ConfigLowThresholdPortA": om1ConfigLowThresholdPortA,
       "om1ConfigHighThresholdPortA": om1ConfigHighThresholdPortA,
       "om1ConfigWavelengthPortB": om1ConfigWavelengthPortB,
       "om1ConfigLowThresholdPortB": om1ConfigLowThresholdPortB,
       "om1ConfigHighThresholdPortB": om1ConfigHighThresholdPortB,
       "om1ConfigFrontPanelMode": om1ConfigFrontPanelMode,
       "lp1ConfigTable": lp1ConfigTable,
       "lp1ConfigEntry": lp1ConfigEntry,
       "lp1ConfigIndex": lp1ConfigIndex,
       "lp1ConfigWavelengthPortA": lp1ConfigWavelengthPortA,
       "lp1ConfigLowThresholdPortA": lp1ConfigLowThresholdPortA,
       "lp1ConfigHighThresholdPortA": lp1ConfigHighThresholdPortA,
       "lp1ConfigWavelengthPortB": lp1ConfigWavelengthPortB,
       "lp1ConfigLowThresholdPortB": lp1ConfigLowThresholdPortB,
       "lp1ConfigHighThresholdPortB": lp1ConfigHighThresholdPortB,
       "lp1ConfigBackupCriteria": lp1ConfigBackupCriteria,
       "lp1ConfigStayWithLastLink": lp1ConfigStayWithLastLink,
       "lp1ConfigBackupEnd": lp1ConfigBackupEnd,
       "lp1ConfigFrontPanelMode": lp1ConfigFrontPanelMode,
       "emConfigTable": emConfigTable,
       "emConfigEntry": emConfigEntry,
       "emConfigIndex": emConfigIndex,
       "emConfigEdfaOperationMode": emConfigEdfaOperationMode,
       "emConfigLossOfSignalHandling": emConfigLossOfSignalHandling,
       "emConfigSignalGain": emConfigSignalGain,
       "emConfigMaxOutputPower": emConfigMaxOutputPower,
       "emConfigLowThresholdEdfaIn": emConfigLowThresholdEdfaIn,
       "emConfigHighThresholdEdfaIn": emConfigHighThresholdEdfaIn,
       "emConfigLowThresholdPortB": emConfigLowThresholdPortB,
       "emConfigHighThresholdPortB": emConfigHighThresholdPortB,
       "emConfigFrontPanelMode": emConfigFrontPanelMode,
       "moduleControlTable": moduleControlTable,
       "moduleControlEntry": moduleControlEntry,
       "moduleControlIndex": moduleControlIndex,
       "moduleControlEnterPassword": moduleControlEnterPassword,
       "moduleControlRebootModule": moduleControlRebootModule,
       "moduleControlWarmStart": moduleControlWarmStart,
       "moduleControlClearCounter": moduleControlClearCounter,
       "moduleControlSwitchOffBackup": moduleControlSwitchOffBackup,
       "moduleControlSwitchToBackup": moduleControlSwitchToBackup,
       "moduleControlAutomaticBackup": moduleControlAutomaticBackup,
       "moduleControlWriteDisplay": moduleControlWriteDisplay,
       "moduleControlLedTest": moduleControlLedTest,
       "moduleControlLoopOff": moduleControlLoopOff,
       "moduleControlLoopPort1": moduleControlLoopPort1,
       "moduleControlLoopPort2": moduleControlLoopPort2,
       "moduleControlLoopPort3": moduleControlLoopPort3,
       "moduleControlLoopPort4": moduleControlLoopPort4,
       "moduleControlBertRestart": moduleControlBertRestart,
       "moduleControlBertInsertError": moduleControlBertInsertError,
       "moduleControlBertClearCounter": moduleControlBertClearCounter,
       "systemStatusTable": systemStatusTable,
       "systemStatusEntry": systemStatusEntry,
       "systemStatusIndex": systemStatusIndex,
       "systemStatusAnyErrorCondition": systemStatusAnyErrorCondition,
       "systemStatusAnyTestMode": systemStatusAnyTestMode,
       "systemStatusAnySparePart": systemStatusAnySparePart,
       "systemStatusUsedNodeId": systemStatusUsedNodeId,
       "systemStatusLocalRack": systemStatusLocalRack,
       "systemStatusLocalSlot": systemStatusLocalSlot,
       "moduleInventoryTable": moduleInventoryTable,
       "moduleInventoryEntry": moduleInventoryEntry,
       "moduleInventoryIndex": moduleInventoryIndex,
       "moduleInventoryExpectedModule": moduleInventoryExpectedModule,
       "moduleInventoryModule": moduleInventoryModule,
       "moduleInventoryType": moduleInventoryType,
       "moduleInventoryBoardCode": moduleInventoryBoardCode,
       "moduleInventoryAdditionalInfo": moduleInventoryAdditionalInfo,
       "moduleInventorySerialNumber": moduleInventorySerialNumber,
       "moduleInventoryOccupiedSlots": moduleInventoryOccupiedSlots,
       "moduleInventoryProjectNumber": moduleInventoryProjectNumber,
       "moduleInventoryBuildVersion": moduleInventoryBuildVersion,
       "moduleInventoryProductionDate": moduleInventoryProductionDate,
       "moduleInventoryMfgTestInfo": moduleInventoryMfgTestInfo,
       "moduleInventoryNumberOfOpticalPorts": moduleInventoryNumberOfOpticalPorts,
       "moduleInventoryNumberOfSfpPorts": moduleInventoryNumberOfSfpPorts,
       "moduleInventoryNumberOfXfpPorts": moduleInventoryNumberOfXfpPorts,
       "moduleInventoryCoreFirmwareVersion": moduleInventoryCoreFirmwareVersion,
       "moduleInventoryCoreFirmwareDate": moduleInventoryCoreFirmwareDate,
       "moduleInventoryApplFirmwareVersion": moduleInventoryApplFirmwareVersion,
       "moduleInventoryApplFirmwareDate": moduleInventoryApplFirmwareDate,
       "moduleStatusTable": moduleStatusTable,
       "moduleStatusEntry": moduleStatusEntry,
       "moduleStatusIndex": moduleStatusIndex,
       "moduleStatusModule": moduleStatusModule,
       "moduleStatusSystemOk": moduleStatusSystemOk,
       "moduleStatusErrorCondition": moduleStatusErrorCondition,
       "moduleStatusTestMode": moduleStatusTestMode,
       "moduleStatusSparePart": moduleStatusSparePart,
       "moduleStatusUptime": moduleStatusUptime,
       "moduleStatusTimeSinceCounterReset": moduleStatusTimeSinceCounterReset,
       "moduleStatusTemperature": moduleStatusTemperature,
       "moduleStatusTooHot": moduleStatusTooHot,
       "moduleStatusBackupState": moduleStatusBackupState,
       "moduleStatusBackupCounter": moduleStatusBackupCounter,
       "moduleStatusBackupDuration": moduleStatusBackupDuration,
       "portStatusTable": portStatusTable,
       "portStatusEntry": portStatusEntry,
       "portStatusPortIndex": portStatusPortIndex,
       "portStatusModule": portStatusModule,
       "portStatusLocation": portStatusLocation,
       "portStatusSnmpPort": portStatusSnmpPort,
       "portStatusAlias": portStatusAlias,
       "portStatusAdminStatus": portStatusAdminStatus,
       "portStatusOperStatus": portStatusOperStatus,
       "portStatusDetailedStatus": portStatusDetailedStatus,
       "portStatusPortDatarate": portStatusPortDatarate,
       "portStatusUpdateTimeStamp": portStatusUpdateTimeStamp,
       "portStatusTimeSinceValueReset": portStatusTimeSinceValueReset,
       "portStatusTimeSinceLastError": portStatusTimeSinceLastError,
       "portStatusTimeSignalTooLow": portStatusTimeSignalTooLow,
       "portStatusSignalTooLowCounter": portStatusSignalTooLowCounter,
       "portStatusTimeSignalTooHigh": portStatusTimeSignalTooHigh,
       "portStatusSignalTooHighCounter": portStatusSignalTooHighCounter,
       "portStatusLowThreshold": portStatusLowThreshold,
       "portStatusCurrentInputSignal": portStatusCurrentInputSignal,
       "portStatusHighThreshold": portStatusHighThreshold,
       "emStatusTable": emStatusTable,
       "emStatusEntry": emStatusEntry,
       "emStatusIndex": emStatusIndex,
       "emStatusSystemOk": emStatusSystemOk,
       "emStatusErrors": emStatusErrors,
       "emStatusHardwareCode": emStatusHardwareCode,
       "emStatusTimeSincePowerError": emStatusTimeSincePowerError,
       "emStatusTimeWithPowerLoss": emStatusTimeWithPowerLoss,
       "emStatusInputSignalLowCounter": emStatusInputSignalLowCounter,
       "emStatusInputPower": emStatusInputPower,
       "emStatusSignalGain": emStatusSignalGain,
       "emStatusOptimalFlatGain": emStatusOptimalFlatGain,
       "emStatusBackReflection": emStatusBackReflection,
       "emStatusSignalOutputPower": emStatusSignalOutputPower,
       "emStatusTotalOutputPower": emStatusTotalOutputPower,
       "emStatusMinOutputPower": emStatusMinOutputPower,
       "emStatusMaxOutputPower": emStatusMaxOutputPower,
       "emStatusCfgOutputPower": emStatusCfgOutputPower,
       "bertStatusTable": bertStatusTable,
       "bertStatusEntry": bertStatusEntry,
       "bertStatusIndex": bertStatusIndex,
       "bertStatusLocation": bertStatusLocation,
       "bertStatusBertOperation": bertStatusBertOperation,
       "bertStatusTotalErrors": bertStatusTotalErrors,
       "bertStatusTimeSinceLastError": bertStatusTimeSinceLastError,
       "bertStatusTotalTestTime": bertStatusTotalTestTime,
       "bertStatusErroredTime": bertStatusErroredTime,
       "bertStatusBitErrorRate": bertStatusBitErrorRate,
       "bertStatusBerSinceLastError": bertStatusBerSinceLastError,
       "bertStatusTheoreticalBer": bertStatusTheoreticalBer,
       "bertStatusAvailability": bertStatusAvailability}
)
