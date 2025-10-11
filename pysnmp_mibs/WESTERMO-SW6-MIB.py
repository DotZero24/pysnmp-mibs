# SNMP MIB module (WESTERMO-SW6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-SW6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:21 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

base = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1)
)
if mibBuilder.loadTexts:
    base.setRevisions(
        ("2019-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1)
)
_CfgSystem_ObjectIdentity = ObjectIdentity
cfgSystem = _CfgSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 1)
)


class _CfgSysHostname_Type(DisplayString):
    """Custom type cfgSysHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSysHostname_Type.__name__ = "DisplayString"
_CfgSysHostname_Object = MibScalar
cfgSysHostname = _CfgSysHostname_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 1, 1),
    _CfgSysHostname_Type()
)
cfgSysHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSysHostname.setStatus("current")


class _CfgSysTimezone_Type(DisplayString):
    """Custom type cfgSysTimezone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSysTimezone_Type.__name__ = "DisplayString"
_CfgSysTimezone_Object = MibScalar
cfgSysTimezone = _CfgSysTimezone_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 1, 2),
    _CfgSysTimezone_Type()
)
cfgSysTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSysTimezone.setStatus("current")
_CfgNetwork_ObjectIdentity = ObjectIdentity
cfgNetwork = _CfgNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2)
)
_CfgNetEthernetTable_Object = MibTable
cfgNetEthernetTable = _CfgNetEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfgNetEthernetTable.setStatus("current")
_CfgNetEthernetTableEntry_Object = MibTableRow
cfgNetEthernetTableEntry = _CfgNetEthernetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1)
)
cfgNetEthernetTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNetEthIndex"),
)
if mibBuilder.loadTexts:
    cfgNetEthernetTableEntry.setStatus("current")


class _CfgNetEthIndex_Type(Integer32):
    """Custom type cfgNetEthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CfgNetEthIndex_Type.__name__ = "Integer32"
_CfgNetEthIndex_Object = MibTableColumn
cfgNetEthIndex = _CfgNetEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 1),
    _CfgNetEthIndex_Type()
)
cfgNetEthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetEthIndex.setStatus("current")


class _CfgNetEthName_Type(DisplayString):
    """Custom type cfgNetEthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetEthName_Type.__name__ = "DisplayString"
_CfgNetEthName_Object = MibTableColumn
cfgNetEthName = _CfgNetEthName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 2),
    _CfgNetEthName_Type()
)
cfgNetEthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetEthName.setStatus("current")


class _CfgNetEthEnabled_Type(Integer32):
    """Custom type cfgNetEthEnabled based on Integer32"""
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


_CfgNetEthEnabled_Type.__name__ = "Integer32"
_CfgNetEthEnabled_Object = MibTableColumn
cfgNetEthEnabled = _CfgNetEthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 3),
    _CfgNetEthEnabled_Type()
)
cfgNetEthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthEnabled.setStatus("current")
_CfgNetEthBridge_Type = Integer32
_CfgNetEthBridge_Object = MibTableColumn
cfgNetEthBridge = _CfgNetEthBridge_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 7),
    _CfgNetEthBridge_Type()
)
cfgNetEthBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthBridge.setStatus("current")


class _CfgNetEthAutoneg_Type(Integer32):
    """Custom type cfgNetEthAutoneg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forced", 0),
          ("auto", 1))
    )


_CfgNetEthAutoneg_Type.__name__ = "Integer32"
_CfgNetEthAutoneg_Object = MibTableColumn
cfgNetEthAutoneg = _CfgNetEthAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 8),
    _CfgNetEthAutoneg_Type()
)
cfgNetEthAutoneg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthAutoneg.setStatus("current")
_CfgNetEthSpeed_Type = Integer32
_CfgNetEthSpeed_Object = MibTableColumn
cfgNetEthSpeed = _CfgNetEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 9),
    _CfgNetEthSpeed_Type()
)
cfgNetEthSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthSpeed.setStatus("current")


class _CfgNetEthTrunk_Type(DisplayString):
    """Custom type cfgNetEthTrunk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetEthTrunk_Type.__name__ = "DisplayString"
_CfgNetEthTrunk_Object = MibTableColumn
cfgNetEthTrunk = _CfgNetEthTrunk_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 10),
    _CfgNetEthTrunk_Type()
)
cfgNetEthTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthTrunk.setStatus("current")


class _CfgNetEthTag_Type(Integer32):
    """Custom type cfgNetEthTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_CfgNetEthTag_Type.__name__ = "Integer32"
_CfgNetEthTag_Object = MibTableColumn
cfgNetEthTag = _CfgNetEthTag_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 11),
    _CfgNetEthTag_Type()
)
cfgNetEthTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthTag.setStatus("current")


class _CfgNetEthVlanMode_Type(Integer32):
    """Custom type cfgNetEthVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trunk", 0),
          ("access", 1),
          ("nativeuntagged", 3))
    )


_CfgNetEthVlanMode_Type.__name__ = "Integer32"
_CfgNetEthVlanMode_Object = MibTableColumn
cfgNetEthVlanMode = _CfgNetEthVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 12),
    _CfgNetEthVlanMode_Type()
)
cfgNetEthVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthVlanMode.setStatus("current")


class _CfgNetEthLldpEnabled_Type(Integer32):
    """Custom type cfgNetEthLldpEnabled based on Integer32"""
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


_CfgNetEthLldpEnabled_Type.__name__ = "Integer32"
_CfgNetEthLldpEnabled_Object = MibTableColumn
cfgNetEthLldpEnabled = _CfgNetEthLldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 1, 1, 15),
    _CfgNetEthLldpEnabled_Type()
)
cfgNetEthLldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetEthLldpEnabled.setStatus("current")
_CfgNetWlanTable_Object = MibTable
cfgNetWlanTable = _CfgNetWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfgNetWlanTable.setStatus("current")
_CfgNetWlanTableEntry_Object = MibTableRow
cfgNetWlanTableEntry = _CfgNetWlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1)
)
cfgNetWlanTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNetWlanIndex"),
)
if mibBuilder.loadTexts:
    cfgNetWlanTableEntry.setStatus("current")


class _CfgNetWlanIndex_Type(Integer32):
    """Custom type cfgNetWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgNetWlanIndex_Type.__name__ = "Integer32"
_CfgNetWlanIndex_Object = MibTableColumn
cfgNetWlanIndex = _CfgNetWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 1),
    _CfgNetWlanIndex_Type()
)
cfgNetWlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetWlanIndex.setStatus("current")


class _CfgNetWlanName_Type(DisplayString):
    """Custom type cfgNetWlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetWlanName_Type.__name__ = "DisplayString"
_CfgNetWlanName_Object = MibTableColumn
cfgNetWlanName = _CfgNetWlanName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 2),
    _CfgNetWlanName_Type()
)
cfgNetWlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetWlanName.setStatus("current")


class _CfgNetWlanEnabled_Type(Integer32):
    """Custom type cfgNetWlanEnabled based on Integer32"""
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


_CfgNetWlanEnabled_Type.__name__ = "Integer32"
_CfgNetWlanEnabled_Object = MibTableColumn
cfgNetWlanEnabled = _CfgNetWlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 3),
    _CfgNetWlanEnabled_Type()
)
cfgNetWlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWlanEnabled.setStatus("current")
_CfgNetWlanBridge_Type = Integer32
_CfgNetWlanBridge_Object = MibTableColumn
cfgNetWlanBridge = _CfgNetWlanBridge_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 7),
    _CfgNetWlanBridge_Type()
)
cfgNetWlanBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWlanBridge.setStatus("current")


class _CfgNetWlanTrunk_Type(DisplayString):
    """Custom type cfgNetWlanTrunk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetWlanTrunk_Type.__name__ = "DisplayString"
_CfgNetWlanTrunk_Object = MibTableColumn
cfgNetWlanTrunk = _CfgNetWlanTrunk_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 10),
    _CfgNetWlanTrunk_Type()
)
cfgNetWlanTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWlanTrunk.setStatus("current")


class _CfgNetWlanTag_Type(Integer32):
    """Custom type cfgNetWlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_CfgNetWlanTag_Type.__name__ = "Integer32"
_CfgNetWlanTag_Object = MibTableColumn
cfgNetWlanTag = _CfgNetWlanTag_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 11),
    _CfgNetWlanTag_Type()
)
cfgNetWlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWlanTag.setStatus("current")


class _CfgNetWlanVlanMode_Type(Integer32):
    """Custom type cfgNetWlanVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trunk", 0),
          ("access", 1),
          ("nativeuntagged", 3))
    )


_CfgNetWlanVlanMode_Type.__name__ = "Integer32"
_CfgNetWlanVlanMode_Object = MibTableColumn
cfgNetWlanVlanMode = _CfgNetWlanVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 12),
    _CfgNetWlanVlanMode_Type()
)
cfgNetWlanVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWlanVlanMode.setStatus("current")


class _CfgNetWlanLldpEnabled_Type(Integer32):
    """Custom type cfgNetWlanLldpEnabled based on Integer32"""
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


_CfgNetWlanLldpEnabled_Type.__name__ = "Integer32"
_CfgNetWlanLldpEnabled_Object = MibTableColumn
cfgNetWlanLldpEnabled = _CfgNetWlanLldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 2, 1, 15),
    _CfgNetWlanLldpEnabled_Type()
)
cfgNetWlanLldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWlanLldpEnabled.setStatus("current")
_CfgNetVlanTable_Object = MibTable
cfgNetVlanTable = _CfgNetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cfgNetVlanTable.setStatus("current")
_CfgNetVlanTableEntry_Object = MibTableRow
cfgNetVlanTableEntry = _CfgNetVlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3, 1)
)
cfgNetVlanTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNetVlanIndex"),
)
if mibBuilder.loadTexts:
    cfgNetVlanTableEntry.setStatus("current")


class _CfgNetVlanIndex_Type(Integer32):
    """Custom type cfgNetVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CfgNetVlanIndex_Type.__name__ = "Integer32"
_CfgNetVlanIndex_Object = MibTableColumn
cfgNetVlanIndex = _CfgNetVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3, 1, 1),
    _CfgNetVlanIndex_Type()
)
cfgNetVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetVlanIndex.setStatus("current")


class _CfgNetVlanName_Type(DisplayString):
    """Custom type cfgNetVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetVlanName_Type.__name__ = "DisplayString"
_CfgNetVlanName_Object = MibTableColumn
cfgNetVlanName = _CfgNetVlanName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3, 1, 2),
    _CfgNetVlanName_Type()
)
cfgNetVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetVlanName.setStatus("current")


class _CfgNetVlanEnabled_Type(Integer32):
    """Custom type cfgNetVlanEnabled based on Integer32"""
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


_CfgNetVlanEnabled_Type.__name__ = "Integer32"
_CfgNetVlanEnabled_Object = MibTableColumn
cfgNetVlanEnabled = _CfgNetVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3, 1, 3),
    _CfgNetVlanEnabled_Type()
)
cfgNetVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetVlanEnabled.setStatus("current")
_CfgNetVlanBridge_Type = Integer32
_CfgNetVlanBridge_Object = MibTableColumn
cfgNetVlanBridge = _CfgNetVlanBridge_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3, 1, 7),
    _CfgNetVlanBridge_Type()
)
cfgNetVlanBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetVlanBridge.setStatus("current")


class _CfgNetVlanParent_Type(DisplayString):
    """Custom type cfgNetVlanParent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetVlanParent_Type.__name__ = "DisplayString"
_CfgNetVlanParent_Object = MibTableColumn
cfgNetVlanParent = _CfgNetVlanParent_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3, 1, 8),
    _CfgNetVlanParent_Type()
)
cfgNetVlanParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetVlanParent.setStatus("current")


class _CfgNetVlanVid_Type(Integer32):
    """Custom type cfgNetVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CfgNetVlanVid_Type.__name__ = "Integer32"
_CfgNetVlanVid_Object = MibTableColumn
cfgNetVlanVid = _CfgNetVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 3, 1, 9),
    _CfgNetVlanVid_Type()
)
cfgNetVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetVlanVid.setStatus("current")
_CfgNetIpTable_Object = MibTable
cfgNetIpTable = _CfgNetIpTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cfgNetIpTable.setStatus("current")
_CfgNetIpTableEntry_Object = MibTableRow
cfgNetIpTableEntry = _CfgNetIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6, 1)
)
cfgNetIpTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNetIpIndex"),
)
if mibBuilder.loadTexts:
    cfgNetIpTableEntry.setStatus("current")


class _CfgNetIpIndex_Type(Integer32):
    """Custom type cfgNetIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CfgNetIpIndex_Type.__name__ = "Integer32"
_CfgNetIpIndex_Object = MibTableColumn
cfgNetIpIndex = _CfgNetIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6, 1, 1),
    _CfgNetIpIndex_Type()
)
cfgNetIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetIpIndex.setStatus("current")


class _CfgNetIpEnabled_Type(Integer32):
    """Custom type cfgNetIpEnabled based on Integer32"""
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


_CfgNetIpEnabled_Type.__name__ = "Integer32"
_CfgNetIpEnabled_Object = MibTableColumn
cfgNetIpEnabled = _CfgNetIpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6, 1, 3),
    _CfgNetIpEnabled_Type()
)
cfgNetIpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetIpEnabled.setStatus("current")


class _CfgNetIpAddr_Type(DisplayString):
    """Custom type cfgNetIpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 19),
    )


_CfgNetIpAddr_Type.__name__ = "DisplayString"
_CfgNetIpAddr_Object = MibTableColumn
cfgNetIpAddr = _CfgNetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6, 1, 4),
    _CfgNetIpAddr_Type()
)
cfgNetIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetIpAddr.setStatus("current")


class _CfgNetIpProto_Type(Integer32):
    """Custom type cfgNetIpProto based on Integer32"""
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
        *(("static", 0),
          ("dhcp", 1),
          ("dhcpForceRenew", 2),
          ("dhcpForceRelease", 3),
          ("linkLocal", 4),
          ("carp", 5))
    )


_CfgNetIpProto_Type.__name__ = "Integer32"
_CfgNetIpProto_Object = MibTableColumn
cfgNetIpProto = _CfgNetIpProto_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6, 1, 6),
    _CfgNetIpProto_Type()
)
cfgNetIpProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetIpProto.setStatus("current")


class _CfgNetIpInterface_Type(DisplayString):
    """Custom type cfgNetIpInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetIpInterface_Type.__name__ = "DisplayString"
_CfgNetIpInterface_Object = MibTableColumn
cfgNetIpInterface = _CfgNetIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6, 1, 8),
    _CfgNetIpInterface_Type()
)
cfgNetIpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetIpInterface.setStatus("current")


class _CfgNetIpCarpId_Type(Integer32):
    """Custom type cfgNetIpCarpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CfgNetIpCarpId_Type.__name__ = "Integer32"
_CfgNetIpCarpId_Object = MibTableColumn
cfgNetIpCarpId = _CfgNetIpCarpId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 6, 1, 10),
    _CfgNetIpCarpId_Type()
)
cfgNetIpCarpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetIpCarpId.setStatus("current")
_CfgNetCarpTable_Object = MibTable
cfgNetCarpTable = _CfgNetCarpTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cfgNetCarpTable.setStatus("current")
_CfgNetCarpTableEntry_Object = MibTableRow
cfgNetCarpTableEntry = _CfgNetCarpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1)
)
cfgNetCarpTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNetCarpIndex"),
)
if mibBuilder.loadTexts:
    cfgNetCarpTableEntry.setStatus("current")


class _CfgNetCarpIndex_Type(Integer32):
    """Custom type cfgNetCarpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CfgNetCarpIndex_Type.__name__ = "Integer32"
_CfgNetCarpIndex_Object = MibTableColumn
cfgNetCarpIndex = _CfgNetCarpIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 1),
    _CfgNetCarpIndex_Type()
)
cfgNetCarpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetCarpIndex.setStatus("current")


class _CfgNetCarpEnabled_Type(Integer32):
    """Custom type cfgNetCarpEnabled based on Integer32"""
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


_CfgNetCarpEnabled_Type.__name__ = "Integer32"
_CfgNetCarpEnabled_Object = MibTableColumn
cfgNetCarpEnabled = _CfgNetCarpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 3),
    _CfgNetCarpEnabled_Type()
)
cfgNetCarpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpEnabled.setStatus("current")


class _CfgNetCarpVhid_Type(Integer32):
    """Custom type cfgNetCarpVhid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CfgNetCarpVhid_Type.__name__ = "Integer32"
_CfgNetCarpVhid_Object = MibTableColumn
cfgNetCarpVhid = _CfgNetCarpVhid_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 10),
    _CfgNetCarpVhid_Type()
)
cfgNetCarpVhid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpVhid.setStatus("current")


class _CfgNetCarpPassword_Type(DisplayString):
    """Custom type cfgNetCarpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetCarpPassword_Type.__name__ = "DisplayString"
_CfgNetCarpPassword_Object = MibTableColumn
cfgNetCarpPassword = _CfgNetCarpPassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 11),
    _CfgNetCarpPassword_Type()
)
cfgNetCarpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpPassword.setStatus("current")


class _CfgNetCarpAdvbase_Type(Integer32):
    """Custom type cfgNetCarpAdvbase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CfgNetCarpAdvbase_Type.__name__ = "Integer32"
_CfgNetCarpAdvbase_Object = MibTableColumn
cfgNetCarpAdvbase = _CfgNetCarpAdvbase_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 12),
    _CfgNetCarpAdvbase_Type()
)
cfgNetCarpAdvbase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpAdvbase.setStatus("current")


class _CfgNetCarpAdvskew_Type(Integer32):
    """Custom type cfgNetCarpAdvskew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_CfgNetCarpAdvskew_Type.__name__ = "Integer32"
_CfgNetCarpAdvskew_Object = MibTableColumn
cfgNetCarpAdvskew = _CfgNetCarpAdvskew_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 13),
    _CfgNetCarpAdvskew_Type()
)
cfgNetCarpAdvskew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpAdvskew.setStatus("current")


class _CfgNetCarpAdvdivider_Type(Integer32):
    """Custom type cfgNetCarpAdvdivider based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfgNetCarpAdvdivider_Type.__name__ = "Integer32"
_CfgNetCarpAdvdivider_Object = MibTableColumn
cfgNetCarpAdvdivider = _CfgNetCarpAdvdivider_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 14),
    _CfgNetCarpAdvdivider_Type()
)
cfgNetCarpAdvdivider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpAdvdivider.setStatus("current")


class _CfgNetCarpRatio_Type(Integer32):
    """Custom type cfgNetCarpRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfgNetCarpRatio_Type.__name__ = "Integer32"
_CfgNetCarpRatio_Object = MibTableColumn
cfgNetCarpRatio = _CfgNetCarpRatio_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 15),
    _CfgNetCarpRatio_Type()
)
cfgNetCarpRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpRatio.setStatus("current")


class _CfgNetCarpPreempt_Type(Integer32):
    """Custom type cfgNetCarpPreempt based on Integer32"""
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


_CfgNetCarpPreempt_Type.__name__ = "Integer32"
_CfgNetCarpPreempt_Object = MibTableColumn
cfgNetCarpPreempt = _CfgNetCarpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 16),
    _CfgNetCarpPreempt_Type()
)
cfgNetCarpPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpPreempt.setStatus("current")


class _CfgNetCarpPreemptdemote_Type(Integer32):
    """Custom type cfgNetCarpPreemptdemote based on Integer32"""
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


_CfgNetCarpPreemptdemote_Type.__name__ = "Integer32"
_CfgNetCarpPreemptdemote_Object = MibTableColumn
cfgNetCarpPreemptdemote = _CfgNetCarpPreemptdemote_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 17),
    _CfgNetCarpPreemptdemote_Type()
)
cfgNetCarpPreemptdemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpPreemptdemote.setStatus("current")


class _CfgNetCarpLocalInterfaceGroup_Type(Integer32):
    """Custom type cfgNetCarpLocalInterfaceGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CfgNetCarpLocalInterfaceGroup_Type.__name__ = "Integer32"
_CfgNetCarpLocalInterfaceGroup_Object = MibTableColumn
cfgNetCarpLocalInterfaceGroup = _CfgNetCarpLocalInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 18),
    _CfgNetCarpLocalInterfaceGroup_Type()
)
cfgNetCarpLocalInterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpLocalInterfaceGroup.setStatus("current")


class _CfgNetCarpSyncInterface_Type(DisplayString):
    """Custom type cfgNetCarpSyncInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetCarpSyncInterface_Type.__name__ = "DisplayString"
_CfgNetCarpSyncInterface_Object = MibTableColumn
cfgNetCarpSyncInterface = _CfgNetCarpSyncInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 19),
    _CfgNetCarpSyncInterface_Type()
)
cfgNetCarpSyncInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpSyncInterface.setStatus("current")
_CfgNetCarpMcastIp_Type = IpAddress
_CfgNetCarpMcastIp_Object = MibTableColumn
cfgNetCarpMcastIp = _CfgNetCarpMcastIp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 7, 1, 21),
    _CfgNetCarpMcastIp_Type()
)
cfgNetCarpMcastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetCarpMcastIp.setStatus("current")
_CfgNetMacVlanTable_Object = MibTable
cfgNetMacVlanTable = _CfgNetMacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cfgNetMacVlanTable.setStatus("current")
_CfgNetMacVlanTableEntry_Object = MibTableRow
cfgNetMacVlanTableEntry = _CfgNetMacVlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 9, 1)
)
cfgNetMacVlanTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNetMacVlanIndex"),
)
if mibBuilder.loadTexts:
    cfgNetMacVlanTableEntry.setStatus("current")


class _CfgNetMacVlanIndex_Type(Integer32):
    """Custom type cfgNetMacVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgNetMacVlanIndex_Type.__name__ = "Integer32"
_CfgNetMacVlanIndex_Object = MibTableColumn
cfgNetMacVlanIndex = _CfgNetMacVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 9, 1, 1),
    _CfgNetMacVlanIndex_Type()
)
cfgNetMacVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetMacVlanIndex.setStatus("current")


class _CfgNetMacVlanName_Type(DisplayString):
    """Custom type cfgNetMacVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetMacVlanName_Type.__name__ = "DisplayString"
_CfgNetMacVlanName_Object = MibTableColumn
cfgNetMacVlanName = _CfgNetMacVlanName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 9, 1, 2),
    _CfgNetMacVlanName_Type()
)
cfgNetMacVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetMacVlanName.setStatus("current")


class _CfgNetMacVlanEnabled_Type(Integer32):
    """Custom type cfgNetMacVlanEnabled based on Integer32"""
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


_CfgNetMacVlanEnabled_Type.__name__ = "Integer32"
_CfgNetMacVlanEnabled_Object = MibTableColumn
cfgNetMacVlanEnabled = _CfgNetMacVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 9, 1, 3),
    _CfgNetMacVlanEnabled_Type()
)
cfgNetMacVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetMacVlanEnabled.setStatus("current")


class _CfgNetMacVlanParent_Type(DisplayString):
    """Custom type cfgNetMacVlanParent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNetMacVlanParent_Type.__name__ = "DisplayString"
_CfgNetMacVlanParent_Object = MibTableColumn
cfgNetMacVlanParent = _CfgNetMacVlanParent_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 9, 1, 8),
    _CfgNetMacVlanParent_Type()
)
cfgNetMacVlanParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetMacVlanParent.setStatus("current")


class _CfgNetMacVlanMac_Type(DisplayString):
    """Custom type cfgNetMacVlanMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgNetMacVlanMac_Type.__name__ = "DisplayString"
_CfgNetMacVlanMac_Object = MibTableColumn
cfgNetMacVlanMac = _CfgNetMacVlanMac_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 9, 1, 15),
    _CfgNetMacVlanMac_Type()
)
cfgNetMacVlanMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetMacVlanMac.setStatus("current")
_CfgNetWwanTable_Object = MibTable
cfgNetWwanTable = _CfgNetWwanTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cfgNetWwanTable.setStatus("current")
_CfgNetWwanTableEntry_Object = MibTableRow
cfgNetWwanTableEntry = _CfgNetWwanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 11, 1)
)
cfgNetWwanTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNetWwanIndex"),
)
if mibBuilder.loadTexts:
    cfgNetWwanTableEntry.setStatus("current")


class _CfgNetWwanIndex_Type(Integer32):
    """Custom type cfgNetWwanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CfgNetWwanIndex_Type.__name__ = "Integer32"
_CfgNetWwanIndex_Object = MibTableColumn
cfgNetWwanIndex = _CfgNetWwanIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 11, 1, 1),
    _CfgNetWwanIndex_Type()
)
cfgNetWwanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetWwanIndex.setStatus("current")


class _CfgNetWwanName_Type(DisplayString):
    """Custom type cfgNetWwanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_CfgNetWwanName_Type.__name__ = "DisplayString"
_CfgNetWwanName_Object = MibTableColumn
cfgNetWwanName = _CfgNetWwanName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 11, 1, 2),
    _CfgNetWwanName_Type()
)
cfgNetWwanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetWwanName.setStatus("current")


class _CfgNetWwanEnabled_Type(Integer32):
    """Custom type cfgNetWwanEnabled based on Integer32"""
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


_CfgNetWwanEnabled_Type.__name__ = "Integer32"
_CfgNetWwanEnabled_Object = MibTableColumn
cfgNetWwanEnabled = _CfgNetWwanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 11, 1, 3),
    _CfgNetWwanEnabled_Type()
)
cfgNetWwanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWwanEnabled.setStatus("current")
_CfgNetWwanPrimarySim_Type = Integer32
_CfgNetWwanPrimarySim_Object = MibTableColumn
cfgNetWwanPrimarySim = _CfgNetWwanPrimarySim_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 11, 1, 4),
    _CfgNetWwanPrimarySim_Type()
)
cfgNetWwanPrimarySim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWwanPrimarySim.setStatus("current")
_CfgNetWwanSecondarySim_Type = Integer32
_CfgNetWwanSecondarySim_Object = MibTableColumn
cfgNetWwanSecondarySim = _CfgNetWwanSecondarySim_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 2, 11, 1, 5),
    _CfgNetWwanSecondarySim_Type()
)
cfgNetWwanSecondarySim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetWwanSecondarySim.setStatus("current")
_CfgWireless_ObjectIdentity = ObjectIdentity
cfgWireless = _CfgWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3)
)
_CfgWlanDeviceTable_Object = MibTable
cfgWlanDeviceTable = _CfgWlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfgWlanDeviceTable.setStatus("current")
_CfgWlanDeviceTableEntry_Object = MibTableRow
cfgWlanDeviceTableEntry = _CfgWlanDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1)
)
cfgWlanDeviceTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanDevIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanDeviceTableEntry.setStatus("current")


class _CfgWlanDevIndex_Type(Integer32):
    """Custom type cfgWlanDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CfgWlanDevIndex_Type.__name__ = "Integer32"
_CfgWlanDevIndex_Object = MibTableColumn
cfgWlanDevIndex = _CfgWlanDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 1),
    _CfgWlanDevIndex_Type()
)
cfgWlanDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanDevIndex.setStatus("current")


class _CfgWlanDevName_Type(DisplayString):
    """Custom type cfgWlanDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanDevName_Type.__name__ = "DisplayString"
_CfgWlanDevName_Object = MibTableColumn
cfgWlanDevName = _CfgWlanDevName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 2),
    _CfgWlanDevName_Type()
)
cfgWlanDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlanDevName.setStatus("current")


class _CfgWlanDevModulation_Type(Integer32):
    """Custom type cfgWlanDevModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              10,
              12,
              28)
        )
    )
    namedValues = NamedValues(
        *(("g", 2),
          ("bg", 3),
          ("a", 4),
          ("ng", 10),
          ("na", 12),
          ("ac", 28))
    )


_CfgWlanDevModulation_Type.__name__ = "Integer32"
_CfgWlanDevModulation_Object = MibTableColumn
cfgWlanDevModulation = _CfgWlanDevModulation_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 4),
    _CfgWlanDevModulation_Type()
)
cfgWlanDevModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevModulation.setStatus("current")


class _CfgWlanDevBandwidth_Type(Integer32):
    """Custom type cfgWlanDevBandwidth based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bw20", 0),
          ("bw40Plus", 1),
          ("bw40Minus", 2),
          ("bwQuarter", 3),
          ("bwHalf", 4),
          ("bw80", 5),
          ("bw160", 6),
          ("bw8080", 7),
          ("bwAuto", 8))
    )


_CfgWlanDevBandwidth_Type.__name__ = "Integer32"
_CfgWlanDevBandwidth_Object = MibTableColumn
cfgWlanDevBandwidth = _CfgWlanDevBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 5),
    _CfgWlanDevBandwidth_Type()
)
cfgWlanDevBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevBandwidth.setStatus("current")
_CfgWlanDevFrequency_Type = Integer32
_CfgWlanDevFrequency_Object = MibTableColumn
cfgWlanDevFrequency = _CfgWlanDevFrequency_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 6),
    _CfgWlanDevFrequency_Type()
)
cfgWlanDevFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevFrequency.setStatus("current")


class _CfgWlanDevPower_Type(Integer32):
    """Custom type cfgWlanDevPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 50),
    )


_CfgWlanDevPower_Type.__name__ = "Integer32"
_CfgWlanDevPower_Object = MibTableColumn
cfgWlanDevPower = _CfgWlanDevPower_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 8),
    _CfgWlanDevPower_Type()
)
cfgWlanDevPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevPower.setStatus("current")


class _CfgWlanDevDistance_Type(Integer32):
    """Custom type cfgWlanDevDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 114750),
    )


_CfgWlanDevDistance_Type.__name__ = "Integer32"
_CfgWlanDevDistance_Object = MibTableColumn
cfgWlanDevDistance = _CfgWlanDevDistance_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 10),
    _CfgWlanDevDistance_Type()
)
cfgWlanDevDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevDistance.setStatus("current")


class _CfgWlanDevRts_Type(Integer32):
    """Custom type cfgWlanDevRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgWlanDevRts_Type.__name__ = "Integer32"
_CfgWlanDevRts_Object = MibTableColumn
cfgWlanDevRts = _CfgWlanDevRts_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 11),
    _CfgWlanDevRts_Type()
)
cfgWlanDevRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevRts.setStatus("current")


class _CfgWlanDevFragments_Type(Integer32):
    """Custom type cfgWlanDevFragments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2346),
    )


_CfgWlanDevFragments_Type.__name__ = "Integer32"
_CfgWlanDevFragments_Object = MibTableColumn
cfgWlanDevFragments = _CfgWlanDevFragments_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 12),
    _CfgWlanDevFragments_Type()
)
cfgWlanDevFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevFragments.setStatus("current")


class _CfgWlanDevShortRetry_Type(Integer32):
    """Custom type cfgWlanDevShortRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CfgWlanDevShortRetry_Type.__name__ = "Integer32"
_CfgWlanDevShortRetry_Object = MibTableColumn
cfgWlanDevShortRetry = _CfgWlanDevShortRetry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 13),
    _CfgWlanDevShortRetry_Type()
)
cfgWlanDevShortRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevShortRetry.setStatus("current")


class _CfgWlanDevLongRetry_Type(Integer32):
    """Custom type cfgWlanDevLongRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CfgWlanDevLongRetry_Type.__name__ = "Integer32"
_CfgWlanDevLongRetry_Object = MibTableColumn
cfgWlanDevLongRetry = _CfgWlanDevLongRetry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 14),
    _CfgWlanDevLongRetry_Type()
)
cfgWlanDevLongRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevLongRetry.setStatus("current")
_CfgWlanDevAntennaGain_Type = Integer32
_CfgWlanDevAntennaGain_Object = MibTableColumn
cfgWlanDevAntennaGain = _CfgWlanDevAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 15),
    _CfgWlanDevAntennaGain_Type()
)
cfgWlanDevAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevAntennaGain.setStatus("current")
_CfgWlanDevTxAntenna_Type = Integer32
_CfgWlanDevTxAntenna_Object = MibTableColumn
cfgWlanDevTxAntenna = _CfgWlanDevTxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 16),
    _CfgWlanDevTxAntenna_Type()
)
cfgWlanDevTxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevTxAntenna.setStatus("current")
_CfgWlanDevRxAntenna_Type = Integer32
_CfgWlanDevRxAntenna_Object = MibTableColumn
cfgWlanDevRxAntenna = _CfgWlanDevRxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 17),
    _CfgWlanDevRxAntenna_Type()
)
cfgWlanDevRxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevRxAntenna.setStatus("current")


class _CfgWlanDevPhy_Type(DisplayString):
    """Custom type cfgWlanDevPhy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanDevPhy_Type.__name__ = "DisplayString"
_CfgWlanDevPhy_Object = MibTableColumn
cfgWlanDevPhy = _CfgWlanDevPhy_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 18),
    _CfgWlanDevPhy_Type()
)
cfgWlanDevPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlanDevPhy.setStatus("current")


class _CfgWlanDevHtCapabilities_Type(Integer32):
    """Custom type cfgWlanDevHtCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfgWlanDevHtCapabilities_Type.__name__ = "Integer32"
_CfgWlanDevHtCapabilities_Object = MibTableColumn
cfgWlanDevHtCapabilities = _CfgWlanDevHtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 24),
    _CfgWlanDevHtCapabilities_Type()
)
cfgWlanDevHtCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevHtCapabilities.setStatus("current")
_CfgWlanDevQmrrString_Type = DisplayString
_CfgWlanDevQmrrString_Object = MibTableColumn
cfgWlanDevQmrrString = _CfgWlanDevQmrrString_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 1, 1, 26),
    _CfgWlanDevQmrrString_Type()
)
cfgWlanDevQmrrString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDevQmrrString.setStatus("current")
_CfgWlanInterfaceTable_Object = MibTable
cfgWlanInterfaceTable = _CfgWlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cfgWlanInterfaceTable.setStatus("current")
_CfgWlanInterfaceTableEntry_Object = MibTableRow
cfgWlanInterfaceTableEntry = _CfgWlanInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1)
)
cfgWlanInterfaceTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanIfaceIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanInterfaceTableEntry.setStatus("current")


class _CfgWlanIfaceIndex_Type(Integer32):
    """Custom type cfgWlanIfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgWlanIfaceIndex_Type.__name__ = "Integer32"
_CfgWlanIfaceIndex_Object = MibTableColumn
cfgWlanIfaceIndex = _CfgWlanIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 1),
    _CfgWlanIfaceIndex_Type()
)
cfgWlanIfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanIfaceIndex.setStatus("current")


class _CfgWlanIfaceName_Type(DisplayString):
    """Custom type cfgWlanIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanIfaceName_Type.__name__ = "DisplayString"
_CfgWlanIfaceName_Object = MibTableColumn
cfgWlanIfaceName = _CfgWlanIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 2),
    _CfgWlanIfaceName_Type()
)
cfgWlanIfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlanIfaceName.setStatus("current")


class _CfgWlanIfaceDevice_Type(Integer32):
    """Custom type cfgWlanIfaceDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("radio0", 0),
          ("radio1", 1))
    )


_CfgWlanIfaceDevice_Type.__name__ = "Integer32"
_CfgWlanIfaceDevice_Object = MibTableColumn
cfgWlanIfaceDevice = _CfgWlanIfaceDevice_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 3),
    _CfgWlanIfaceDevice_Type()
)
cfgWlanIfaceDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceDevice.setStatus("current")


class _CfgWlanIfaceMode_Type(Integer32):
    """Custom type cfgWlanIfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 0),
          ("sta", 1),
          ("monitor", 2))
    )


_CfgWlanIfaceMode_Type.__name__ = "Integer32"
_CfgWlanIfaceMode_Object = MibTableColumn
cfgWlanIfaceMode = _CfgWlanIfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 4),
    _CfgWlanIfaceMode_Type()
)
cfgWlanIfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceMode.setStatus("current")


class _CfgWlanIfaceSsid_Type(DisplayString):
    """Custom type cfgWlanIfaceSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CfgWlanIfaceSsid_Type.__name__ = "DisplayString"
_CfgWlanIfaceSsid_Object = MibTableColumn
cfgWlanIfaceSsid = _CfgWlanIfaceSsid_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 5),
    _CfgWlanIfaceSsid_Type()
)
cfgWlanIfaceSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceSsid.setStatus("current")


class _CfgWlanIfaceEncryption_Type(Integer32):
    """Custom type cfgWlanIfaceEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("wpa2", 3),
          ("wpa2eap", 6),
          ("sae", 7))
    )


_CfgWlanIfaceEncryption_Type.__name__ = "Integer32"
_CfgWlanIfaceEncryption_Object = MibTableColumn
cfgWlanIfaceEncryption = _CfgWlanIfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 6),
    _CfgWlanIfaceEncryption_Type()
)
cfgWlanIfaceEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceEncryption.setStatus("current")


class _CfgWlanIfacePassword_Type(DisplayString):
    """Custom type cfgWlanIfacePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_CfgWlanIfacePassword_Type.__name__ = "DisplayString"
_CfgWlanIfacePassword_Object = MibTableColumn
cfgWlanIfacePassword = _CfgWlanIfacePassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 7),
    _CfgWlanIfacePassword_Type()
)
cfgWlanIfacePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfacePassword.setStatus("current")


class _CfgWlanIfacePassiveScanning_Type(Integer32):
    """Custom type cfgWlanIfacePassiveScanning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("passive", 1))
    )


_CfgWlanIfacePassiveScanning_Type.__name__ = "Integer32"
_CfgWlanIfacePassiveScanning_Object = MibTableColumn
cfgWlanIfacePassiveScanning = _CfgWlanIfacePassiveScanning_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 8),
    _CfgWlanIfacePassiveScanning_Type()
)
cfgWlanIfacePassiveScanning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfacePassiveScanning.setStatus("current")
_CfgWlanIfaceBeaconMiss_Type = Integer32
_CfgWlanIfaceBeaconMiss_Object = MibTableColumn
cfgWlanIfaceBeaconMiss = _CfgWlanIfaceBeaconMiss_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 9),
    _CfgWlanIfaceBeaconMiss_Type()
)
cfgWlanIfaceBeaconMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceBeaconMiss.setStatus("current")


class _CfgWlanIfaceDtim_Type(Integer32):
    """Custom type cfgWlanIfaceDtim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CfgWlanIfaceDtim_Type.__name__ = "Integer32"
_CfgWlanIfaceDtim_Object = MibTableColumn
cfgWlanIfaceDtim = _CfgWlanIfaceDtim_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 10),
    _CfgWlanIfaceDtim_Type()
)
cfgWlanIfaceDtim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceDtim.setStatus("current")
_CfgWlanIfaceBitrates_Type = DisplayString
_CfgWlanIfaceBitrates_Object = MibTableColumn
cfgWlanIfaceBitrates = _CfgWlanIfaceBitrates_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 11),
    _CfgWlanIfaceBitrates_Type()
)
cfgWlanIfaceBitrates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceBitrates.setStatus("current")


class _CfgWlanIfaceBeaconInterval_Type(Integer32):
    """Custom type cfgWlanIfaceBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1000),
    )


_CfgWlanIfaceBeaconInterval_Type.__name__ = "Integer32"
_CfgWlanIfaceBeaconInterval_Object = MibTableColumn
cfgWlanIfaceBeaconInterval = _CfgWlanIfaceBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 12),
    _CfgWlanIfaceBeaconInterval_Type()
)
cfgWlanIfaceBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceBeaconInterval.setStatus("current")
_CfgWlanIfaceWmeParameter_Type = Integer32
_CfgWlanIfaceWmeParameter_Object = MibTableColumn
cfgWlanIfaceWmeParameter = _CfgWlanIfaceWmeParameter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 13),
    _CfgWlanIfaceWmeParameter_Type()
)
cfgWlanIfaceWmeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceWmeParameter.setStatus("current")


class _CfgWlanIfaceWmeEnabled_Type(Integer32):
    """Custom type cfgWlanIfaceWmeEnabled based on Integer32"""
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


_CfgWlanIfaceWmeEnabled_Type.__name__ = "Integer32"
_CfgWlanIfaceWmeEnabled_Object = MibTableColumn
cfgWlanIfaceWmeEnabled = _CfgWlanIfaceWmeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 14),
    _CfgWlanIfaceWmeEnabled_Type()
)
cfgWlanIfaceWmeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceWmeEnabled.setStatus("current")
_CfgWlanIfaceScanList_Type = Integer32
_CfgWlanIfaceScanList_Object = MibTableColumn
cfgWlanIfaceScanList = _CfgWlanIfaceScanList_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 15),
    _CfgWlanIfaceScanList_Type()
)
cfgWlanIfaceScanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceScanList.setStatus("current")


class _CfgWlanIfaceIgnoreBroadcastSsid_Type(Integer32):
    """Custom type cfgWlanIfaceIgnoreBroadcastSsid based on Integer32"""
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


_CfgWlanIfaceIgnoreBroadcastSsid_Type.__name__ = "Integer32"
_CfgWlanIfaceIgnoreBroadcastSsid_Object = MibTableColumn
cfgWlanIfaceIgnoreBroadcastSsid = _CfgWlanIfaceIgnoreBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 16),
    _CfgWlanIfaceIgnoreBroadcastSsid_Type()
)
cfgWlanIfaceIgnoreBroadcastSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceIgnoreBroadcastSsid.setStatus("current")


class _CfgWlanIfaceMacaddrAcl_Type(Integer32):
    """Custom type cfgWlanIfaceMacaddrAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acceptunlessdeny", 0),
          ("denyunlessaccept", 1),
          ("radius", 2))
    )


_CfgWlanIfaceMacaddrAcl_Type.__name__ = "Integer32"
_CfgWlanIfaceMacaddrAcl_Object = MibTableColumn
cfgWlanIfaceMacaddrAcl = _CfgWlanIfaceMacaddrAcl_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 17),
    _CfgWlanIfaceMacaddrAcl_Type()
)
cfgWlanIfaceMacaddrAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceMacaddrAcl.setStatus("current")


class _CfgWlanIfaceMaxNumSta_Type(Integer32):
    """Custom type cfgWlanIfaceMaxNumSta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CfgWlanIfaceMaxNumSta_Type.__name__ = "Integer32"
_CfgWlanIfaceMaxNumSta_Object = MibTableColumn
cfgWlanIfaceMaxNumSta = _CfgWlanIfaceMaxNumSta_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 18),
    _CfgWlanIfaceMaxNumSta_Type()
)
cfgWlanIfaceMaxNumSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceMaxNumSta.setStatus("current")


class _CfgWlanIfaceBssid_Type(DisplayString):
    """Custom type cfgWlanIfaceBssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlanIfaceBssid_Type.__name__ = "DisplayString"
_CfgWlanIfaceBssid_Object = MibTableColumn
cfgWlanIfaceBssid = _CfgWlanIfaceBssid_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 19),
    _CfgWlanIfaceBssid_Type()
)
cfgWlanIfaceBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceBssid.setStatus("current")


class _CfgWlanIfaceLegacyRates_Type(Integer32):
    """Custom type cfgWlanIfaceLegacyRates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CfgWlanIfaceLegacyRates_Type.__name__ = "Integer32"
_CfgWlanIfaceLegacyRates_Object = MibTableColumn
cfgWlanIfaceLegacyRates = _CfgWlanIfaceLegacyRates_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 20),
    _CfgWlanIfaceLegacyRates_Type()
)
cfgWlanIfaceLegacyRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceLegacyRates.setStatus("current")


class _CfgWlanIface4addr_Type(Integer32):
    """Custom type cfgWlanIface4addr based on Integer32"""
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


_CfgWlanIface4addr_Type.__name__ = "Integer32"
_CfgWlanIface4addr_Object = MibTableColumn
cfgWlanIface4addr = _CfgWlanIface4addr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 21),
    _CfgWlanIface4addr_Type()
)
cfgWlanIface4addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIface4addr.setStatus("current")


class _CfgWlanIfaceInactivityTimeout_Type(Integer32):
    """Custom type cfgWlanIfaceInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_CfgWlanIfaceInactivityTimeout_Type.__name__ = "Integer32"
_CfgWlanIfaceInactivityTimeout_Object = MibTableColumn
cfgWlanIfaceInactivityTimeout = _CfgWlanIfaceInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 23),
    _CfgWlanIfaceInactivityTimeout_Type()
)
cfgWlanIfaceInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceInactivityTimeout.setStatus("current")


class _CfgWlanIfaceUseVendorSsid_Type(Integer32):
    """Custom type cfgWlanIfaceUseVendorSsid based on Integer32"""
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


_CfgWlanIfaceUseVendorSsid_Type.__name__ = "Integer32"
_CfgWlanIfaceUseVendorSsid_Object = MibTableColumn
cfgWlanIfaceUseVendorSsid = _CfgWlanIfaceUseVendorSsid_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 26),
    _CfgWlanIfaceUseVendorSsid_Type()
)
cfgWlanIfaceUseVendorSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceUseVendorSsid.setStatus("current")


class _CfgWlanIfaceIeee80211w_Type(Integer32):
    """Custom type cfgWlanIfaceIeee80211w based on Integer32"""
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
          ("optional", 1),
          ("required", 2))
    )


_CfgWlanIfaceIeee80211w_Type.__name__ = "Integer32"
_CfgWlanIfaceIeee80211w_Object = MibTableColumn
cfgWlanIfaceIeee80211w = _CfgWlanIfaceIeee80211w_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 30),
    _CfgWlanIfaceIeee80211w_Type()
)
cfgWlanIfaceIeee80211w.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceIeee80211w.setStatus("current")


class _CfgWlanIfaceIeee80211wMaxTimeout_Type(Integer32):
    """Custom type cfgWlanIfaceIeee80211wMaxTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_CfgWlanIfaceIeee80211wMaxTimeout_Type.__name__ = "Integer32"
_CfgWlanIfaceIeee80211wMaxTimeout_Object = MibTableColumn
cfgWlanIfaceIeee80211wMaxTimeout = _CfgWlanIfaceIeee80211wMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 31),
    _CfgWlanIfaceIeee80211wMaxTimeout_Type()
)
cfgWlanIfaceIeee80211wMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceIeee80211wMaxTimeout.setStatus("current")


class _CfgWlanIfaceIeee80211wRetryTimeout_Type(Integer32):
    """Custom type cfgWlanIfaceIeee80211wRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_CfgWlanIfaceIeee80211wRetryTimeout_Type.__name__ = "Integer32"
_CfgWlanIfaceIeee80211wRetryTimeout_Object = MibTableColumn
cfgWlanIfaceIeee80211wRetryTimeout = _CfgWlanIfaceIeee80211wRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 32),
    _CfgWlanIfaceIeee80211wRetryTimeout_Type()
)
cfgWlanIfaceIeee80211wRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceIeee80211wRetryTimeout.setStatus("current")
_CfgWlanIfaceAcsList_Type = Integer32
_CfgWlanIfaceAcsList_Object = MibTableColumn
cfgWlanIfaceAcsList = _CfgWlanIfaceAcsList_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 40),
    _CfgWlanIfaceAcsList_Type()
)
cfgWlanIfaceAcsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceAcsList.setStatus("current")


class _CfgWlanIfaceNeighbourReport_Type(Integer32):
    """Custom type cfgWlanIfaceNeighbourReport based on Integer32"""
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


_CfgWlanIfaceNeighbourReport_Type.__name__ = "Integer32"
_CfgWlanIfaceNeighbourReport_Object = MibTableColumn
cfgWlanIfaceNeighbourReport = _CfgWlanIfaceNeighbourReport_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 60),
    _CfgWlanIfaceNeighbourReport_Type()
)
cfgWlanIfaceNeighbourReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceNeighbourReport.setStatus("current")
_CfgWlanIfaceNeighbourParameter_Type = Integer32
_CfgWlanIfaceNeighbourParameter_Object = MibTableColumn
cfgWlanIfaceNeighbourParameter = _CfgWlanIfaceNeighbourParameter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 61),
    _CfgWlanIfaceNeighbourParameter_Type()
)
cfgWlanIfaceNeighbourParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceNeighbourParameter.setStatus("current")


class _CfgWlanIfaceL2nat_Type(Integer32):
    """Custom type cfgWlanIfaceL2nat based on Integer32"""
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


_CfgWlanIfaceL2nat_Type.__name__ = "Integer32"
_CfgWlanIfaceL2nat_Object = MibTableColumn
cfgWlanIfaceL2nat = _CfgWlanIfaceL2nat_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 80),
    _CfgWlanIfaceL2nat_Type()
)
cfgWlanIfaceL2nat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceL2nat.setStatus("current")


class _CfgWlanIfaceL2natLearningMode_Type(Integer32):
    """Custom type cfgWlanIfaceL2natLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("arp", 1))
    )


_CfgWlanIfaceL2natLearningMode_Type.__name__ = "Integer32"
_CfgWlanIfaceL2natLearningMode_Object = MibTableColumn
cfgWlanIfaceL2natLearningMode = _CfgWlanIfaceL2natLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 81),
    _CfgWlanIfaceL2natLearningMode_Type()
)
cfgWlanIfaceL2natLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceL2natLearningMode.setStatus("current")


class _CfgWlanIfaceL2natDefaultDestination_Type(DisplayString):
    """Custom type cfgWlanIfaceL2natDefaultDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlanIfaceL2natDefaultDestination_Type.__name__ = "DisplayString"
_CfgWlanIfaceL2natDefaultDestination_Object = MibTableColumn
cfgWlanIfaceL2natDefaultDestination = _CfgWlanIfaceL2natDefaultDestination_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 82),
    _CfgWlanIfaceL2natDefaultDestination_Type()
)
cfgWlanIfaceL2natDefaultDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceL2natDefaultDestination.setStatus("current")


class _CfgWlanIfaceTimeAdvertisement_Type(Integer32):
    """Custom type cfgWlanIfaceTimeAdvertisement based on Integer32"""
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


_CfgWlanIfaceTimeAdvertisement_Type.__name__ = "Integer32"
_CfgWlanIfaceTimeAdvertisement_Object = MibTableColumn
cfgWlanIfaceTimeAdvertisement = _CfgWlanIfaceTimeAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 90),
    _CfgWlanIfaceTimeAdvertisement_Type()
)
cfgWlanIfaceTimeAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceTimeAdvertisement.setStatus("current")


class _CfgWlanIfaceApIsolate_Type(Integer32):
    """Custom type cfgWlanIfaceApIsolate based on Integer32"""
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


_CfgWlanIfaceApIsolate_Type.__name__ = "Integer32"
_CfgWlanIfaceApIsolate_Object = MibTableColumn
cfgWlanIfaceApIsolate = _CfgWlanIfaceApIsolate_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 2, 1, 100),
    _CfgWlanIfaceApIsolate_Type()
)
cfgWlanIfaceApIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanIfaceApIsolate.setStatus("current")
_CfgWlanHandoffTable_Object = MibTable
cfgWlanHandoffTable = _CfgWlanHandoffTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cfgWlanHandoffTable.setStatus("current")
_CfgWlanHandoffTableEntry_Object = MibTableRow
cfgWlanHandoffTableEntry = _CfgWlanHandoffTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1)
)
cfgWlanHandoffTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanHoIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanHandoffTableEntry.setStatus("current")


class _CfgWlanHoIndex_Type(Integer32):
    """Custom type cfgWlanHoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgWlanHoIndex_Type.__name__ = "Integer32"
_CfgWlanHoIndex_Object = MibTableColumn
cfgWlanHoIndex = _CfgWlanHoIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 1),
    _CfgWlanHoIndex_Type()
)
cfgWlanHoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanHoIndex.setStatus("current")


class _CfgWlanHoIfaceName_Type(DisplayString):
    """Custom type cfgWlanHoIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanHoIfaceName_Type.__name__ = "DisplayString"
_CfgWlanHoIfaceName_Object = MibTableColumn
cfgWlanHoIfaceName = _CfgWlanHoIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 2),
    _CfgWlanHoIfaceName_Type()
)
cfgWlanHoIfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlanHoIfaceName.setStatus("current")


class _CfgWlanHoProfile_Type(Integer32):
    """Custom type cfgWlanHoProfile based on Integer32"""
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
        *(("t2gv1", 1),
          ("t2gv2", 2),
          ("t2gv2fg", 3),
          ("t2gv3", 4))
    )


_CfgWlanHoProfile_Type.__name__ = "Integer32"
_CfgWlanHoProfile_Object = MibTableColumn
cfgWlanHoProfile = _CfgWlanHoProfile_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 3),
    _CfgWlanHoProfile_Type()
)
cfgWlanHoProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoProfile.setStatus("current")


class _CfgWlanHoScanningLevel_Type(Integer32):
    """Custom type cfgWlanHoScanningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 95),
    )


_CfgWlanHoScanningLevel_Type.__name__ = "Integer32"
_CfgWlanHoScanningLevel_Object = MibTableColumn
cfgWlanHoScanningLevel = _CfgWlanHoScanningLevel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 5),
    _CfgWlanHoScanningLevel_Type()
)
cfgWlanHoScanningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoScanningLevel.setStatus("current")


class _CfgWlanHoBeacons_Type(Integer32):
    """Custom type cfgWlanHoBeacons based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_CfgWlanHoBeacons_Type.__name__ = "Integer32"
_CfgWlanHoBeacons_Object = MibTableColumn
cfgWlanHoBeacons = _CfgWlanHoBeacons_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 6),
    _CfgWlanHoBeacons_Type()
)
cfgWlanHoBeacons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoBeacons.setStatus("current")


class _CfgWlanHoRecovery_Type(Integer32):
    """Custom type cfgWlanHoRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_CfgWlanHoRecovery_Type.__name__ = "Integer32"
_CfgWlanHoRecovery_Object = MibTableColumn
cfgWlanHoRecovery = _CfgWlanHoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 7),
    _CfgWlanHoRecovery_Type()
)
cfgWlanHoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoRecovery.setStatus("current")


class _CfgWlanHoFilterMode_Type(Integer32):
    """Custom type cfgWlanHoFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("long", 1))
    )


_CfgWlanHoFilterMode_Type.__name__ = "Integer32"
_CfgWlanHoFilterMode_Object = MibTableColumn
cfgWlanHoFilterMode = _CfgWlanHoFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 9),
    _CfgWlanHoFilterMode_Type()
)
cfgWlanHoFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoFilterMode.setStatus("current")
_CfgWlanHoFilterLongX_Type = Integer32
_CfgWlanHoFilterLongX_Object = MibTableColumn
cfgWlanHoFilterLongX = _CfgWlanHoFilterLongX_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 10),
    _CfgWlanHoFilterLongX_Type()
)
cfgWlanHoFilterLongX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoFilterLongX.setStatus("current")
_CfgWlanHoFilterLongY_Type = Integer32
_CfgWlanHoFilterLongY_Object = MibTableColumn
cfgWlanHoFilterLongY = _CfgWlanHoFilterLongY_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 11),
    _CfgWlanHoFilterLongY_Type()
)
cfgWlanHoFilterLongY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoFilterLongY.setStatus("current")
_CfgWlanHoScanRateLimitTime_Type = Integer32
_CfgWlanHoScanRateLimitTime_Object = MibTableColumn
cfgWlanHoScanRateLimitTime = _CfgWlanHoScanRateLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 12),
    _CfgWlanHoScanRateLimitTime_Type()
)
cfgWlanHoScanRateLimitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoScanRateLimitTime.setStatus("current")
_CfgWlanHoScanRateLimitTries_Type = Integer32
_CfgWlanHoScanRateLimitTries_Object = MibTableColumn
cfgWlanHoScanRateLimitTries = _CfgWlanHoScanRateLimitTries_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 13),
    _CfgWlanHoScanRateLimitTries_Type()
)
cfgWlanHoScanRateLimitTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoScanRateLimitTries.setStatus("current")


class _CfgWlanHoPassiveChanTime_Type(Integer32):
    """Custom type cfgWlanHoPassiveChanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CfgWlanHoPassiveChanTime_Type.__name__ = "Integer32"
_CfgWlanHoPassiveChanTime_Object = MibTableColumn
cfgWlanHoPassiveChanTime = _CfgWlanHoPassiveChanTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 16),
    _CfgWlanHoPassiveChanTime_Type()
)
cfgWlanHoPassiveChanTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoPassiveChanTime.setStatus("current")
_CfgWlanHoLevelLow_Type = Integer32
_CfgWlanHoLevelLow_Object = MibTableColumn
cfgWlanHoLevelLow = _CfgWlanHoLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 18),
    _CfgWlanHoLevelLow_Type()
)
cfgWlanHoLevelLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoLevelLow.setStatus("current")
_CfgWlanHoLevelHigh_Type = Integer32
_CfgWlanHoLevelHigh_Object = MibTableColumn
cfgWlanHoLevelHigh = _CfgWlanHoLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 19),
    _CfgWlanHoLevelHigh_Type()
)
cfgWlanHoLevelHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoLevelHigh.setStatus("current")


class _CfgWlanHoDistanceNear_Type(Integer32):
    """Custom type cfgWlanHoDistanceNear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 114750),
    )


_CfgWlanHoDistanceNear_Type.__name__ = "Integer32"
_CfgWlanHoDistanceNear_Object = MibTableColumn
cfgWlanHoDistanceNear = _CfgWlanHoDistanceNear_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 20),
    _CfgWlanHoDistanceNear_Type()
)
cfgWlanHoDistanceNear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoDistanceNear.setStatus("current")


class _CfgWlanHoDistanceFar_Type(Integer32):
    """Custom type cfgWlanHoDistanceFar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 114750),
    )


_CfgWlanHoDistanceFar_Type.__name__ = "Integer32"
_CfgWlanHoDistanceFar_Object = MibTableColumn
cfgWlanHoDistanceFar = _CfgWlanHoDistanceFar_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 21),
    _CfgWlanHoDistanceFar_Type()
)
cfgWlanHoDistanceFar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoDistanceFar.setStatus("current")


class _CfgWlanHoDistanceMeasurementPeriod_Type(Integer32):
    """Custom type cfgWlanHoDistanceMeasurementPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CfgWlanHoDistanceMeasurementPeriod_Type.__name__ = "Integer32"
_CfgWlanHoDistanceMeasurementPeriod_Object = MibTableColumn
cfgWlanHoDistanceMeasurementPeriod = _CfgWlanHoDistanceMeasurementPeriod_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 22),
    _CfgWlanHoDistanceMeasurementPeriod_Type()
)
cfgWlanHoDistanceMeasurementPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoDistanceMeasurementPeriod.setStatus("current")
_CfgWlanHoDistanceFilterX_Type = Integer32
_CfgWlanHoDistanceFilterX_Object = MibTableColumn
cfgWlanHoDistanceFilterX = _CfgWlanHoDistanceFilterX_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 23),
    _CfgWlanHoDistanceFilterX_Type()
)
cfgWlanHoDistanceFilterX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoDistanceFilterX.setStatus("current")
_CfgWlanHoDistanceFilterY_Type = Integer32
_CfgWlanHoDistanceFilterY_Object = MibTableColumn
cfgWlanHoDistanceFilterY = _CfgWlanHoDistanceFilterY_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 3, 1, 24),
    _CfgWlanHoDistanceFilterY_Type()
)
cfgWlanHoDistanceFilterY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanHoDistanceFilterY.setStatus("current")
_CfgWlanFreqTable_Object = MibTable
cfgWlanFreqTable = _CfgWlanFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cfgWlanFreqTable.setStatus("current")
_CfgWlanFreqTableEntry_Object = MibTableRow
cfgWlanFreqTableEntry = _CfgWlanFreqTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1)
)
cfgWlanFreqTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanFIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanFreqTableEntry.setStatus("current")


class _CfgWlanFIndex_Type(Integer32):
    """Custom type cfgWlanFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CfgWlanFIndex_Type.__name__ = "Integer32"
_CfgWlanFIndex_Object = MibTableColumn
cfgWlanFIndex = _CfgWlanFIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 1),
    _CfgWlanFIndex_Type()
)
cfgWlanFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanFIndex.setStatus("current")
_CfgWlanFFreq0_Type = Integer32
_CfgWlanFFreq0_Object = MibTableColumn
cfgWlanFFreq0 = _CfgWlanFFreq0_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 2),
    _CfgWlanFFreq0_Type()
)
cfgWlanFFreq0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq0.setStatus("current")
_CfgWlanFFreq1_Type = Integer32
_CfgWlanFFreq1_Object = MibTableColumn
cfgWlanFFreq1 = _CfgWlanFFreq1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 3),
    _CfgWlanFFreq1_Type()
)
cfgWlanFFreq1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq1.setStatus("current")
_CfgWlanFFreq2_Type = Integer32
_CfgWlanFFreq2_Object = MibTableColumn
cfgWlanFFreq2 = _CfgWlanFFreq2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 4),
    _CfgWlanFFreq2_Type()
)
cfgWlanFFreq2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq2.setStatus("current")
_CfgWlanFFreq3_Type = Integer32
_CfgWlanFFreq3_Object = MibTableColumn
cfgWlanFFreq3 = _CfgWlanFFreq3_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 5),
    _CfgWlanFFreq3_Type()
)
cfgWlanFFreq3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq3.setStatus("current")
_CfgWlanFFreq4_Type = Integer32
_CfgWlanFFreq4_Object = MibTableColumn
cfgWlanFFreq4 = _CfgWlanFFreq4_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 6),
    _CfgWlanFFreq4_Type()
)
cfgWlanFFreq4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq4.setStatus("current")
_CfgWlanFFreq5_Type = Integer32
_CfgWlanFFreq5_Object = MibTableColumn
cfgWlanFFreq5 = _CfgWlanFFreq5_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 7),
    _CfgWlanFFreq5_Type()
)
cfgWlanFFreq5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq5.setStatus("current")
_CfgWlanFFreq6_Type = Integer32
_CfgWlanFFreq6_Object = MibTableColumn
cfgWlanFFreq6 = _CfgWlanFFreq6_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 8),
    _CfgWlanFFreq6_Type()
)
cfgWlanFFreq6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq6.setStatus("current")
_CfgWlanFFreq7_Type = Integer32
_CfgWlanFFreq7_Object = MibTableColumn
cfgWlanFFreq7 = _CfgWlanFFreq7_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 9),
    _CfgWlanFFreq7_Type()
)
cfgWlanFFreq7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq7.setStatus("current")
_CfgWlanFFreq8_Type = Integer32
_CfgWlanFFreq8_Object = MibTableColumn
cfgWlanFFreq8 = _CfgWlanFFreq8_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 10),
    _CfgWlanFFreq8_Type()
)
cfgWlanFFreq8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq8.setStatus("current")
_CfgWlanFFreq9_Type = Integer32
_CfgWlanFFreq9_Object = MibTableColumn
cfgWlanFFreq9 = _CfgWlanFFreq9_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 11),
    _CfgWlanFFreq9_Type()
)
cfgWlanFFreq9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq9.setStatus("current")
_CfgWlanFFreq10_Type = Integer32
_CfgWlanFFreq10_Object = MibTableColumn
cfgWlanFFreq10 = _CfgWlanFFreq10_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 12),
    _CfgWlanFFreq10_Type()
)
cfgWlanFFreq10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq10.setStatus("current")
_CfgWlanFFreq11_Type = Integer32
_CfgWlanFFreq11_Object = MibTableColumn
cfgWlanFFreq11 = _CfgWlanFFreq11_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 13),
    _CfgWlanFFreq11_Type()
)
cfgWlanFFreq11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq11.setStatus("current")
_CfgWlanFFreq12_Type = Integer32
_CfgWlanFFreq12_Object = MibTableColumn
cfgWlanFFreq12 = _CfgWlanFFreq12_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 14),
    _CfgWlanFFreq12_Type()
)
cfgWlanFFreq12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq12.setStatus("current")
_CfgWlanFFreq13_Type = Integer32
_CfgWlanFFreq13_Object = MibTableColumn
cfgWlanFFreq13 = _CfgWlanFFreq13_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 15),
    _CfgWlanFFreq13_Type()
)
cfgWlanFFreq13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq13.setStatus("current")
_CfgWlanFFreq14_Type = Integer32
_CfgWlanFFreq14_Object = MibTableColumn
cfgWlanFFreq14 = _CfgWlanFFreq14_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 16),
    _CfgWlanFFreq14_Type()
)
cfgWlanFFreq14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq14.setStatus("current")
_CfgWlanFFreq15_Type = Integer32
_CfgWlanFFreq15_Object = MibTableColumn
cfgWlanFFreq15 = _CfgWlanFFreq15_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 17),
    _CfgWlanFFreq15_Type()
)
cfgWlanFFreq15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq15.setStatus("current")
_CfgWlanFFreq16_Type = Integer32
_CfgWlanFFreq16_Object = MibTableColumn
cfgWlanFFreq16 = _CfgWlanFFreq16_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 18),
    _CfgWlanFFreq16_Type()
)
cfgWlanFFreq16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq16.setStatus("current")
_CfgWlanFFreq17_Type = Integer32
_CfgWlanFFreq17_Object = MibTableColumn
cfgWlanFFreq17 = _CfgWlanFFreq17_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 19),
    _CfgWlanFFreq17_Type()
)
cfgWlanFFreq17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq17.setStatus("current")
_CfgWlanFFreq18_Type = Integer32
_CfgWlanFFreq18_Object = MibTableColumn
cfgWlanFFreq18 = _CfgWlanFFreq18_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 20),
    _CfgWlanFFreq18_Type()
)
cfgWlanFFreq18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq18.setStatus("current")
_CfgWlanFFreq19_Type = Integer32
_CfgWlanFFreq19_Object = MibTableColumn
cfgWlanFFreq19 = _CfgWlanFFreq19_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 21),
    _CfgWlanFFreq19_Type()
)
cfgWlanFFreq19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq19.setStatus("current")
_CfgWlanFFreq20_Type = Integer32
_CfgWlanFFreq20_Object = MibTableColumn
cfgWlanFFreq20 = _CfgWlanFFreq20_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 22),
    _CfgWlanFFreq20_Type()
)
cfgWlanFFreq20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq20.setStatus("current")
_CfgWlanFFreq21_Type = Integer32
_CfgWlanFFreq21_Object = MibTableColumn
cfgWlanFFreq21 = _CfgWlanFFreq21_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 23),
    _CfgWlanFFreq21_Type()
)
cfgWlanFFreq21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq21.setStatus("current")
_CfgWlanFFreq22_Type = Integer32
_CfgWlanFFreq22_Object = MibTableColumn
cfgWlanFFreq22 = _CfgWlanFFreq22_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 24),
    _CfgWlanFFreq22_Type()
)
cfgWlanFFreq22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq22.setStatus("current")
_CfgWlanFFreq23_Type = Integer32
_CfgWlanFFreq23_Object = MibTableColumn
cfgWlanFFreq23 = _CfgWlanFFreq23_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 4, 1, 25),
    _CfgWlanFFreq23_Type()
)
cfgWlanFFreq23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanFFreq23.setStatus("current")
_CfgWlanWmeTable_Object = MibTable
cfgWlanWmeTable = _CfgWlanWmeTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cfgWlanWmeTable.setStatus("current")
_CfgWlanWmeTableEntry_Object = MibTableRow
cfgWlanWmeTableEntry = _CfgWlanWmeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1)
)
cfgWlanWmeTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanWmeIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanWmeTableEntry.setStatus("current")


class _CfgWlanWmeIndex_Type(Integer32):
    """Custom type cfgWlanWmeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CfgWlanWmeIndex_Type.__name__ = "Integer32"
_CfgWlanWmeIndex_Object = MibTableColumn
cfgWlanWmeIndex = _CfgWlanWmeIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 1),
    _CfgWlanWmeIndex_Type()
)
cfgWlanWmeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanWmeIndex.setStatus("current")
_CfgWlanWmeId_Type = Integer32
_CfgWlanWmeId_Object = MibTableColumn
cfgWlanWmeId = _CfgWlanWmeId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 2),
    _CfgWlanWmeId_Type()
)
cfgWlanWmeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeId.setStatus("current")


class _CfgWlanWmeAc_Type(Integer32):
    """Custom type cfgWlanWmeAc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("background", 1),
          ("besteffort", 2),
          ("video", 3),
          ("voice", 4))
    )


_CfgWlanWmeAc_Type.__name__ = "Integer32"
_CfgWlanWmeAc_Object = MibTableColumn
cfgWlanWmeAc = _CfgWlanWmeAc_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 3),
    _CfgWlanWmeAc_Type()
)
cfgWlanWmeAc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeAc.setStatus("current")


class _CfgWlanWmeCwMin_Type(Integer32):
    """Custom type cfgWlanWmeCwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_CfgWlanWmeCwMin_Type.__name__ = "Integer32"
_CfgWlanWmeCwMin_Object = MibTableColumn
cfgWlanWmeCwMin = _CfgWlanWmeCwMin_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 4),
    _CfgWlanWmeCwMin_Type()
)
cfgWlanWmeCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeCwMin.setStatus("current")


class _CfgWlanWmeCwMax_Type(Integer32):
    """Custom type cfgWlanWmeCwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_CfgWlanWmeCwMax_Type.__name__ = "Integer32"
_CfgWlanWmeCwMax_Object = MibTableColumn
cfgWlanWmeCwMax = _CfgWlanWmeCwMax_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 5),
    _CfgWlanWmeCwMax_Type()
)
cfgWlanWmeCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeCwMax.setStatus("current")


class _CfgWlanWmeAifs_Type(Integer32):
    """Custom type cfgWlanWmeAifs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CfgWlanWmeAifs_Type.__name__ = "Integer32"
_CfgWlanWmeAifs_Object = MibTableColumn
cfgWlanWmeAifs = _CfgWlanWmeAifs_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 6),
    _CfgWlanWmeAifs_Type()
)
cfgWlanWmeAifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeAifs.setStatus("current")


class _CfgWlanWmeTxOpMax_Type(Integer32):
    """Custom type cfgWlanWmeTxOpMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgWlanWmeTxOpMax_Type.__name__ = "Integer32"
_CfgWlanWmeTxOpMax_Object = MibTableColumn
cfgWlanWmeTxOpMax = _CfgWlanWmeTxOpMax_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 7),
    _CfgWlanWmeTxOpMax_Type()
)
cfgWlanWmeTxOpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeTxOpMax.setStatus("current")


class _CfgWlanWmeApCwMin_Type(Integer32):
    """Custom type cfgWlanWmeApCwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CfgWlanWmeApCwMin_Type.__name__ = "Integer32"
_CfgWlanWmeApCwMin_Object = MibTableColumn
cfgWlanWmeApCwMin = _CfgWlanWmeApCwMin_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 8),
    _CfgWlanWmeApCwMin_Type()
)
cfgWlanWmeApCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeApCwMin.setStatus("current")


class _CfgWlanWmeApCwMax_Type(Integer32):
    """Custom type cfgWlanWmeApCwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CfgWlanWmeApCwMax_Type.__name__ = "Integer32"
_CfgWlanWmeApCwMax_Object = MibTableColumn
cfgWlanWmeApCwMax = _CfgWlanWmeApCwMax_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 9),
    _CfgWlanWmeApCwMax_Type()
)
cfgWlanWmeApCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeApCwMax.setStatus("current")


class _CfgWlanWmeApAifs_Type(Integer32):
    """Custom type cfgWlanWmeApAifs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgWlanWmeApAifs_Type.__name__ = "Integer32"
_CfgWlanWmeApAifs_Object = MibTableColumn
cfgWlanWmeApAifs = _CfgWlanWmeApAifs_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 10),
    _CfgWlanWmeApAifs_Type()
)
cfgWlanWmeApAifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeApAifs.setStatus("current")


class _CfgWlanWmeApBurst_Type(Integer32):
    """Custom type cfgWlanWmeApBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgWlanWmeApBurst_Type.__name__ = "Integer32"
_CfgWlanWmeApBurst_Object = MibTableColumn
cfgWlanWmeApBurst = _CfgWlanWmeApBurst_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 5, 1, 11),
    _CfgWlanWmeApBurst_Type()
)
cfgWlanWmeApBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanWmeApBurst.setStatus("current")
_CfgWlanDbgTable_Object = MibTable
cfgWlanDbgTable = _CfgWlanDbgTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cfgWlanDbgTable.setStatus("current")
_CfgWlanDbgTableEntry_Object = MibTableRow
cfgWlanDbgTableEntry = _CfgWlanDbgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1)
)
cfgWlanDbgTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanDbgIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanDbgTableEntry.setStatus("current")


class _CfgWlanDbgIndex_Type(Integer32):
    """Custom type cfgWlanDbgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgWlanDbgIndex_Type.__name__ = "Integer32"
_CfgWlanDbgIndex_Object = MibTableColumn
cfgWlanDbgIndex = _CfgWlanDbgIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 1),
    _CfgWlanDbgIndex_Type()
)
cfgWlanDbgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanDbgIndex.setStatus("current")


class _CfgWlanDbgIfaceName_Type(DisplayString):
    """Custom type cfgWlanDbgIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanDbgIfaceName_Type.__name__ = "DisplayString"
_CfgWlanDbgIfaceName_Object = MibTableColumn
cfgWlanDbgIfaceName = _CfgWlanDbgIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 2),
    _CfgWlanDbgIfaceName_Type()
)
cfgWlanDbgIfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlanDbgIfaceName.setStatus("current")


class _CfgWlanDbgHandoff_Type(Integer32):
    """Custom type cfgWlanDbgHandoff based on Integer32"""
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


_CfgWlanDbgHandoff_Type.__name__ = "Integer32"
_CfgWlanDbgHandoff_Object = MibTableColumn
cfgWlanDbgHandoff = _CfgWlanDbgHandoff_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 3),
    _CfgWlanDbgHandoff_Type()
)
cfgWlanDbgHandoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgHandoff.setStatus("current")


class _CfgWlanDbgScan_Type(Integer32):
    """Custom type cfgWlanDbgScan based on Integer32"""
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


_CfgWlanDbgScan_Type.__name__ = "Integer32"
_CfgWlanDbgScan_Object = MibTableColumn
cfgWlanDbgScan = _CfgWlanDbgScan_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 4),
    _CfgWlanDbgScan_Type()
)
cfgWlanDbgScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgScan.setStatus("current")


class _CfgWlanDbgMlme_Type(Integer32):
    """Custom type cfgWlanDbgMlme based on Integer32"""
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


_CfgWlanDbgMlme_Type.__name__ = "Integer32"
_CfgWlanDbgMlme_Object = MibTableColumn
cfgWlanDbgMlme = _CfgWlanDbgMlme_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 5),
    _CfgWlanDbgMlme_Type()
)
cfgWlanDbgMlme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgMlme.setStatus("current")


class _CfgWlanDbgEvents_Type(Integer32):
    """Custom type cfgWlanDbgEvents based on Integer32"""
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


_CfgWlanDbgEvents_Type.__name__ = "Integer32"
_CfgWlanDbgEvents_Object = MibTableColumn
cfgWlanDbgEvents = _CfgWlanDbgEvents_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 6),
    _CfgWlanDbgEvents_Type()
)
cfgWlanDbgEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgEvents.setStatus("current")


class _CfgWlanDbgBeaconrssi_Type(Integer32):
    """Custom type cfgWlanDbgBeaconrssi based on Integer32"""
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


_CfgWlanDbgBeaconrssi_Type.__name__ = "Integer32"
_CfgWlanDbgBeaconrssi_Object = MibTableColumn
cfgWlanDbgBeaconrssi = _CfgWlanDbgBeaconrssi_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 7),
    _CfgWlanDbgBeaconrssi_Type()
)
cfgWlanDbgBeaconrssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgBeaconrssi.setStatus("current")


class _CfgWlanDbgAckrssi_Type(Integer32):
    """Custom type cfgWlanDbgAckrssi based on Integer32"""
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


_CfgWlanDbgAckrssi_Type.__name__ = "Integer32"
_CfgWlanDbgAckrssi_Object = MibTableColumn
cfgWlanDbgAckrssi = _CfgWlanDbgAckrssi_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 8),
    _CfgWlanDbgAckrssi_Type()
)
cfgWlanDbgAckrssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgAckrssi.setStatus("current")


class _CfgWlanDbgBeaconfiltered_Type(Integer32):
    """Custom type cfgWlanDbgBeaconfiltered based on Integer32"""
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


_CfgWlanDbgBeaconfiltered_Type.__name__ = "Integer32"
_CfgWlanDbgBeaconfiltered_Object = MibTableColumn
cfgWlanDbgBeaconfiltered = _CfgWlanDbgBeaconfiltered_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 9),
    _CfgWlanDbgBeaconfiltered_Type()
)
cfgWlanDbgBeaconfiltered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgBeaconfiltered.setStatus("current")


class _CfgWlanDbgRatelimit_Type(Integer32):
    """Custom type cfgWlanDbgRatelimit based on Integer32"""
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


_CfgWlanDbgRatelimit_Type.__name__ = "Integer32"
_CfgWlanDbgRatelimit_Object = MibTableColumn
cfgWlanDbgRatelimit = _CfgWlanDbgRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 10),
    _CfgWlanDbgRatelimit_Type()
)
cfgWlanDbgRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgRatelimit.setStatus("current")


class _CfgWlanDbgLinkmonitor_Type(Integer32):
    """Custom type cfgWlanDbgLinkmonitor based on Integer32"""
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


_CfgWlanDbgLinkmonitor_Type.__name__ = "Integer32"
_CfgWlanDbgLinkmonitor_Object = MibTableColumn
cfgWlanDbgLinkmonitor = _CfgWlanDbgLinkmonitor_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 11),
    _CfgWlanDbgLinkmonitor_Type()
)
cfgWlanDbgLinkmonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgLinkmonitor.setStatus("current")


class _CfgWlanDbgBeacontsf_Type(Integer32):
    """Custom type cfgWlanDbgBeacontsf based on Integer32"""
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


_CfgWlanDbgBeacontsf_Type.__name__ = "Integer32"
_CfgWlanDbgBeacontsf_Object = MibTableColumn
cfgWlanDbgBeacontsf = _CfgWlanDbgBeacontsf_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 12),
    _CfgWlanDbgBeacontsf_Type()
)
cfgWlanDbgBeacontsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgBeacontsf.setStatus("current")


class _CfgWlanDbgRange_Type(Integer32):
    """Custom type cfgWlanDbgRange based on Integer32"""
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


_CfgWlanDbgRange_Type.__name__ = "Integer32"
_CfgWlanDbgRange_Object = MibTableColumn
cfgWlanDbgRange = _CfgWlanDbgRange_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 13),
    _CfgWlanDbgRange_Type()
)
cfgWlanDbgRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgRange.setStatus("current")


class _CfgWlanDbgReports_Type(Integer32):
    """Custom type cfgWlanDbgReports based on Integer32"""
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


_CfgWlanDbgReports_Type.__name__ = "Integer32"
_CfgWlanDbgReports_Object = MibTableColumn
cfgWlanDbgReports = _CfgWlanDbgReports_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 6, 1, 14),
    _CfgWlanDbgReports_Type()
)
cfgWlanDbgReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanDbgReports.setStatus("current")
_CfgWlanAclWhiteTable_Object = MibTable
cfgWlanAclWhiteTable = _CfgWlanAclWhiteTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cfgWlanAclWhiteTable.setStatus("current")
_CfgWlanAclWhiteTableEntry_Object = MibTableRow
cfgWlanAclWhiteTableEntry = _CfgWlanAclWhiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 7, 1)
)
cfgWlanAclWhiteTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanAclWhiteIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanAclWhiteTableEntry.setStatus("current")


class _CfgWlanAclWhiteIndex_Type(Integer32):
    """Custom type cfgWlanAclWhiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgWlanAclWhiteIndex_Type.__name__ = "Integer32"
_CfgWlanAclWhiteIndex_Object = MibTableColumn
cfgWlanAclWhiteIndex = _CfgWlanAclWhiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 7, 1, 1),
    _CfgWlanAclWhiteIndex_Type()
)
cfgWlanAclWhiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanAclWhiteIndex.setStatus("current")


class _CfgWlanAclWhiteEnabled_Type(Integer32):
    """Custom type cfgWlanAclWhiteEnabled based on Integer32"""
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


_CfgWlanAclWhiteEnabled_Type.__name__ = "Integer32"
_CfgWlanAclWhiteEnabled_Object = MibTableColumn
cfgWlanAclWhiteEnabled = _CfgWlanAclWhiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 7, 1, 2),
    _CfgWlanAclWhiteEnabled_Type()
)
cfgWlanAclWhiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclWhiteEnabled.setStatus("current")


class _CfgWlanAclWhiteInterface_Type(DisplayString):
    """Custom type cfgWlanAclWhiteInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanAclWhiteInterface_Type.__name__ = "DisplayString"
_CfgWlanAclWhiteInterface_Object = MibTableColumn
cfgWlanAclWhiteInterface = _CfgWlanAclWhiteInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 7, 1, 3),
    _CfgWlanAclWhiteInterface_Type()
)
cfgWlanAclWhiteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclWhiteInterface.setStatus("current")


class _CfgWlanAclWhiteAddr_Type(DisplayString):
    """Custom type cfgWlanAclWhiteAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlanAclWhiteAddr_Type.__name__ = "DisplayString"
_CfgWlanAclWhiteAddr_Object = MibTableColumn
cfgWlanAclWhiteAddr = _CfgWlanAclWhiteAddr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 7, 1, 4),
    _CfgWlanAclWhiteAddr_Type()
)
cfgWlanAclWhiteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclWhiteAddr.setStatus("current")


class _CfgWlanAclWhiteMask_Type(Integer32):
    """Custom type cfgWlanAclWhiteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_CfgWlanAclWhiteMask_Type.__name__ = "Integer32"
_CfgWlanAclWhiteMask_Object = MibTableColumn
cfgWlanAclWhiteMask = _CfgWlanAclWhiteMask_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 7, 1, 5),
    _CfgWlanAclWhiteMask_Type()
)
cfgWlanAclWhiteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclWhiteMask.setStatus("current")
_CfgWlanAclBlackTable_Object = MibTable
cfgWlanAclBlackTable = _CfgWlanAclBlackTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cfgWlanAclBlackTable.setStatus("current")
_CfgWlanAclBlackTableEntry_Object = MibTableRow
cfgWlanAclBlackTableEntry = _CfgWlanAclBlackTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 8, 1)
)
cfgWlanAclBlackTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanAclBlackIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanAclBlackTableEntry.setStatus("current")


class _CfgWlanAclBlackIndex_Type(Integer32):
    """Custom type cfgWlanAclBlackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgWlanAclBlackIndex_Type.__name__ = "Integer32"
_CfgWlanAclBlackIndex_Object = MibTableColumn
cfgWlanAclBlackIndex = _CfgWlanAclBlackIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 8, 1, 1),
    _CfgWlanAclBlackIndex_Type()
)
cfgWlanAclBlackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanAclBlackIndex.setStatus("current")


class _CfgWlanAclBlackEnabled_Type(Integer32):
    """Custom type cfgWlanAclBlackEnabled based on Integer32"""
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


_CfgWlanAclBlackEnabled_Type.__name__ = "Integer32"
_CfgWlanAclBlackEnabled_Object = MibTableColumn
cfgWlanAclBlackEnabled = _CfgWlanAclBlackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 8, 1, 2),
    _CfgWlanAclBlackEnabled_Type()
)
cfgWlanAclBlackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclBlackEnabled.setStatus("current")


class _CfgWlanAclBlackInterface_Type(DisplayString):
    """Custom type cfgWlanAclBlackInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanAclBlackInterface_Type.__name__ = "DisplayString"
_CfgWlanAclBlackInterface_Object = MibTableColumn
cfgWlanAclBlackInterface = _CfgWlanAclBlackInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 8, 1, 3),
    _CfgWlanAclBlackInterface_Type()
)
cfgWlanAclBlackInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclBlackInterface.setStatus("current")


class _CfgWlanAclBlackAddr_Type(DisplayString):
    """Custom type cfgWlanAclBlackAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlanAclBlackAddr_Type.__name__ = "DisplayString"
_CfgWlanAclBlackAddr_Object = MibTableColumn
cfgWlanAclBlackAddr = _CfgWlanAclBlackAddr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 8, 1, 4),
    _CfgWlanAclBlackAddr_Type()
)
cfgWlanAclBlackAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclBlackAddr.setStatus("current")


class _CfgWlanAclBlackMask_Type(Integer32):
    """Custom type cfgWlanAclBlackMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_CfgWlanAclBlackMask_Type.__name__ = "Integer32"
_CfgWlanAclBlackMask_Object = MibTableColumn
cfgWlanAclBlackMask = _CfgWlanAclBlackMask_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 8, 1, 5),
    _CfgWlanAclBlackMask_Type()
)
cfgWlanAclBlackMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanAclBlackMask.setStatus("current")
_CfgWlanGlobal_ObjectIdentity = ObjectIdentity
cfgWlanGlobal = _CfgWlanGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 9)
)


class _CfgWlanGlblCountry_Type(DisplayString):
    """Custom type cfgWlanGlblCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanGlblCountry_Type.__name__ = "DisplayString"
_CfgWlanGlblCountry_Object = MibScalar
cfgWlanGlblCountry = _CfgWlanGlblCountry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 9, 1),
    _CfgWlanGlblCountry_Type()
)
cfgWlanGlblCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanGlblCountry.setStatus("current")


class _CfgWlanGlblLinkmonitorInterval_Type(Integer32):
    """Custom type cfgWlanGlblLinkmonitorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 60000),
    )


_CfgWlanGlblLinkmonitorInterval_Type.__name__ = "Integer32"
_CfgWlanGlblLinkmonitorInterval_Object = MibScalar
cfgWlanGlblLinkmonitorInterval = _CfgWlanGlblLinkmonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 9, 2),
    _CfgWlanGlblLinkmonitorInterval_Type()
)
cfgWlanGlblLinkmonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanGlblLinkmonitorInterval.setStatus("current")


class _CfgWlanGlblLinkmonitorQmrrlogging_Type(Integer32):
    """Custom type cfgWlanGlblLinkmonitorQmrrlogging based on Integer32"""
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


_CfgWlanGlblLinkmonitorQmrrlogging_Type.__name__ = "Integer32"
_CfgWlanGlblLinkmonitorQmrrlogging_Object = MibScalar
cfgWlanGlblLinkmonitorQmrrlogging = _CfgWlanGlblLinkmonitorQmrrlogging_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 9, 3),
    _CfgWlanGlblLinkmonitorQmrrlogging_Type()
)
cfgWlanGlblLinkmonitorQmrrlogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanGlblLinkmonitorQmrrlogging.setStatus("current")


class _CfgWlanGlblConnectionStatusWlanInterface_Type(DisplayString):
    """Custom type cfgWlanGlblConnectionStatusWlanInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 17),
    )


_CfgWlanGlblConnectionStatusWlanInterface_Type.__name__ = "DisplayString"
_CfgWlanGlblConnectionStatusWlanInterface_Object = MibScalar
cfgWlanGlblConnectionStatusWlanInterface = _CfgWlanGlblConnectionStatusWlanInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 9, 4),
    _CfgWlanGlblConnectionStatusWlanInterface_Type()
)
cfgWlanGlblConnectionStatusWlanInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanGlblConnectionStatusWlanInterface.setStatus("current")
_CfgWlan802dot1xTable_Object = MibTable
cfgWlan802dot1xTable = _CfgWlan802dot1xTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cfgWlan802dot1xTable.setStatus("current")
_CfgWlan802dot1xTableEntry_Object = MibTableRow
cfgWlan802dot1xTableEntry = _CfgWlan802dot1xTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1)
)
cfgWlan802dot1xTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlan802dot1xIndex"),
)
if mibBuilder.loadTexts:
    cfgWlan802dot1xTableEntry.setStatus("current")


class _CfgWlan802dot1xIndex_Type(Integer32):
    """Custom type cfgWlan802dot1xIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgWlan802dot1xIndex_Type.__name__ = "Integer32"
_CfgWlan802dot1xIndex_Object = MibTableColumn
cfgWlan802dot1xIndex = _CfgWlan802dot1xIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 1),
    _CfgWlan802dot1xIndex_Type()
)
cfgWlan802dot1xIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlan802dot1xIndex.setStatus("current")


class _CfgWlan802dot1xName_Type(DisplayString):
    """Custom type cfgWlan802dot1xName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlan802dot1xName_Type.__name__ = "DisplayString"
_CfgWlan802dot1xName_Object = MibTableColumn
cfgWlan802dot1xName = _CfgWlan802dot1xName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 2),
    _CfgWlan802dot1xName_Type()
)
cfgWlan802dot1xName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlan802dot1xName.setStatus("current")
_CfgWlan802dot1xOwnIpAddr_Type = IpAddress
_CfgWlan802dot1xOwnIpAddr_Object = MibTableColumn
cfgWlan802dot1xOwnIpAddr = _CfgWlan802dot1xOwnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 3),
    _CfgWlan802dot1xOwnIpAddr_Type()
)
cfgWlan802dot1xOwnIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xOwnIpAddr.setStatus("current")
_CfgWlan802dot1xAuthServerParameter_Type = Integer32
_CfgWlan802dot1xAuthServerParameter_Object = MibTableColumn
cfgWlan802dot1xAuthServerParameter = _CfgWlan802dot1xAuthServerParameter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 4),
    _CfgWlan802dot1xAuthServerParameter_Type()
)
cfgWlan802dot1xAuthServerParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthServerParameter.setStatus("current")
_CfgWlan802dot1xAcctServerParameter_Type = Integer32
_CfgWlan802dot1xAcctServerParameter_Object = MibTableColumn
cfgWlan802dot1xAcctServerParameter = _CfgWlan802dot1xAcctServerParameter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 5),
    _CfgWlan802dot1xAcctServerParameter_Type()
)
cfgWlan802dot1xAcctServerParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctServerParameter.setStatus("current")


class _CfgWlan802dot1xRetryPrimaryInterval_Type(Integer32):
    """Custom type cfgWlan802dot1xRetryPrimaryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CfgWlan802dot1xRetryPrimaryInterval_Type.__name__ = "Integer32"
_CfgWlan802dot1xRetryPrimaryInterval_Object = MibTableColumn
cfgWlan802dot1xRetryPrimaryInterval = _CfgWlan802dot1xRetryPrimaryInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 6),
    _CfgWlan802dot1xRetryPrimaryInterval_Type()
)
cfgWlan802dot1xRetryPrimaryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xRetryPrimaryInterval.setStatus("current")


class _CfgWlan802dot1xInterimAccountingInterval_Type(Integer32):
    """Custom type cfgWlan802dot1xInterimAccountingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CfgWlan802dot1xInterimAccountingInterval_Type.__name__ = "Integer32"
_CfgWlan802dot1xInterimAccountingInterval_Object = MibTableColumn
cfgWlan802dot1xInterimAccountingInterval = _CfgWlan802dot1xInterimAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 7),
    _CfgWlan802dot1xInterimAccountingInterval_Type()
)
cfgWlan802dot1xInterimAccountingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xInterimAccountingInterval.setStatus("current")


class _CfgWlan802dot1xNasId_Type(DisplayString):
    """Custom type cfgWlan802dot1xNasId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CfgWlan802dot1xNasId_Type.__name__ = "DisplayString"
_CfgWlan802dot1xNasId_Object = MibTableColumn
cfgWlan802dot1xNasId = _CfgWlan802dot1xNasId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 8),
    _CfgWlan802dot1xNasId_Type()
)
cfgWlan802dot1xNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xNasId.setStatus("current")


class _CfgWlan802dot1xEapType_Type(Integer32):
    """Custom type cfgWlan802dot1xEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tls", 0),
          ("peap", 1),
          ("ttls", 2))
    )


_CfgWlan802dot1xEapType_Type.__name__ = "Integer32"
_CfgWlan802dot1xEapType_Object = MibTableColumn
cfgWlan802dot1xEapType = _CfgWlan802dot1xEapType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 9),
    _CfgWlan802dot1xEapType_Type()
)
cfgWlan802dot1xEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xEapType.setStatus("current")


class _CfgWlan802dot1xIdentity_Type(DisplayString):
    """Custom type cfgWlan802dot1xIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlan802dot1xIdentity_Type.__name__ = "DisplayString"
_CfgWlan802dot1xIdentity_Object = MibTableColumn
cfgWlan802dot1xIdentity = _CfgWlan802dot1xIdentity_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 10),
    _CfgWlan802dot1xIdentity_Type()
)
cfgWlan802dot1xIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xIdentity.setStatus("current")
_CfgWlan802dot1xClientKeyPassword_Type = DisplayString
_CfgWlan802dot1xClientKeyPassword_Object = MibTableColumn
cfgWlan802dot1xClientKeyPassword = _CfgWlan802dot1xClientKeyPassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 17),
    _CfgWlan802dot1xClientKeyPassword_Type()
)
cfgWlan802dot1xClientKeyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xClientKeyPassword.setStatus("current")


class _CfgWlan802dot1xTlsControlParams_Type(Integer32):
    """Custom type cfgWlan802dot1xTlsControlParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CfgWlan802dot1xTlsControlParams_Type.__name__ = "Integer32"
_CfgWlan802dot1xTlsControlParams_Object = MibTableColumn
cfgWlan802dot1xTlsControlParams = _CfgWlan802dot1xTlsControlParams_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 10, 1, 18),
    _CfgWlan802dot1xTlsControlParams_Type()
)
cfgWlan802dot1xTlsControlParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xTlsControlParams.setStatus("current")
_CfgWlan802dot1xAuthServerTable_Object = MibTable
cfgWlan802dot1xAuthServerTable = _CfgWlan802dot1xAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthServerTable.setStatus("current")
_CfgWlan802dot1xAuthServerTableEntry_Object = MibTableRow
cfgWlan802dot1xAuthServerTableEntry = _CfgWlan802dot1xAuthServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11, 1)
)
cfgWlan802dot1xAuthServerTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlan802dot1xAuthSrvIndex"),
)
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthServerTableEntry.setStatus("current")


class _CfgWlan802dot1xAuthSrvIndex_Type(Integer32):
    """Custom type cfgWlan802dot1xAuthSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgWlan802dot1xAuthSrvIndex_Type.__name__ = "Integer32"
_CfgWlan802dot1xAuthSrvIndex_Object = MibTableColumn
cfgWlan802dot1xAuthSrvIndex = _CfgWlan802dot1xAuthSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11, 1, 1),
    _CfgWlan802dot1xAuthSrvIndex_Type()
)
cfgWlan802dot1xAuthSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthSrvIndex.setStatus("current")


class _CfgWlan802dot1xAuthSrvEnabled_Type(Integer32):
    """Custom type cfgWlan802dot1xAuthSrvEnabled based on Integer32"""
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


_CfgWlan802dot1xAuthSrvEnabled_Type.__name__ = "Integer32"
_CfgWlan802dot1xAuthSrvEnabled_Object = MibTableColumn
cfgWlan802dot1xAuthSrvEnabled = _CfgWlan802dot1xAuthSrvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11, 1, 2),
    _CfgWlan802dot1xAuthSrvEnabled_Type()
)
cfgWlan802dot1xAuthSrvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthSrvEnabled.setStatus("current")
_CfgWlan802dot1xAuthSrvId_Type = Integer32
_CfgWlan802dot1xAuthSrvId_Object = MibTableColumn
cfgWlan802dot1xAuthSrvId = _CfgWlan802dot1xAuthSrvId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11, 1, 3),
    _CfgWlan802dot1xAuthSrvId_Type()
)
cfgWlan802dot1xAuthSrvId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthSrvId.setStatus("current")
_CfgWlan802dot1xAuthSrvIpAddr_Type = IpAddress
_CfgWlan802dot1xAuthSrvIpAddr_Object = MibTableColumn
cfgWlan802dot1xAuthSrvIpAddr = _CfgWlan802dot1xAuthSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11, 1, 4),
    _CfgWlan802dot1xAuthSrvIpAddr_Type()
)
cfgWlan802dot1xAuthSrvIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthSrvIpAddr.setStatus("current")
_CfgWlan802dot1xAuthSrvPort_Type = Integer32
_CfgWlan802dot1xAuthSrvPort_Object = MibTableColumn
cfgWlan802dot1xAuthSrvPort = _CfgWlan802dot1xAuthSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11, 1, 5),
    _CfgWlan802dot1xAuthSrvPort_Type()
)
cfgWlan802dot1xAuthSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthSrvPort.setStatus("current")


class _CfgWlan802dot1xAuthSrvSharedSecret_Type(DisplayString):
    """Custom type cfgWlan802dot1xAuthSrvSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlan802dot1xAuthSrvSharedSecret_Type.__name__ = "DisplayString"
_CfgWlan802dot1xAuthSrvSharedSecret_Object = MibTableColumn
cfgWlan802dot1xAuthSrvSharedSecret = _CfgWlan802dot1xAuthSrvSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 11, 1, 6),
    _CfgWlan802dot1xAuthSrvSharedSecret_Type()
)
cfgWlan802dot1xAuthSrvSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAuthSrvSharedSecret.setStatus("current")
_CfgWlan802dot1xAcctServerTable_Object = MibTable
cfgWlan802dot1xAcctServerTable = _CfgWlan802dot1xAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctServerTable.setStatus("current")
_CfgWlan802dot1xAcctServerTableEntry_Object = MibTableRow
cfgWlan802dot1xAcctServerTableEntry = _CfgWlan802dot1xAcctServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12, 1)
)
cfgWlan802dot1xAcctServerTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlan802dot1xAcctSrvIndex"),
)
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctServerTableEntry.setStatus("current")


class _CfgWlan802dot1xAcctSrvIndex_Type(Integer32):
    """Custom type cfgWlan802dot1xAcctSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgWlan802dot1xAcctSrvIndex_Type.__name__ = "Integer32"
_CfgWlan802dot1xAcctSrvIndex_Object = MibTableColumn
cfgWlan802dot1xAcctSrvIndex = _CfgWlan802dot1xAcctSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12, 1, 1),
    _CfgWlan802dot1xAcctSrvIndex_Type()
)
cfgWlan802dot1xAcctSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctSrvIndex.setStatus("current")


class _CfgWlan802dot1xAcctSrvEnabled_Type(Integer32):
    """Custom type cfgWlan802dot1xAcctSrvEnabled based on Integer32"""
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


_CfgWlan802dot1xAcctSrvEnabled_Type.__name__ = "Integer32"
_CfgWlan802dot1xAcctSrvEnabled_Object = MibTableColumn
cfgWlan802dot1xAcctSrvEnabled = _CfgWlan802dot1xAcctSrvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12, 1, 2),
    _CfgWlan802dot1xAcctSrvEnabled_Type()
)
cfgWlan802dot1xAcctSrvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctSrvEnabled.setStatus("current")
_CfgWlan802dot1xAcctSrvId_Type = Integer32
_CfgWlan802dot1xAcctSrvId_Object = MibTableColumn
cfgWlan802dot1xAcctSrvId = _CfgWlan802dot1xAcctSrvId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12, 1, 3),
    _CfgWlan802dot1xAcctSrvId_Type()
)
cfgWlan802dot1xAcctSrvId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctSrvId.setStatus("current")
_CfgWlan802dot1xAcctSrvIpAddr_Type = IpAddress
_CfgWlan802dot1xAcctSrvIpAddr_Object = MibTableColumn
cfgWlan802dot1xAcctSrvIpAddr = _CfgWlan802dot1xAcctSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12, 1, 4),
    _CfgWlan802dot1xAcctSrvIpAddr_Type()
)
cfgWlan802dot1xAcctSrvIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctSrvIpAddr.setStatus("current")
_CfgWlan802dot1xAcctSrvPort_Type = Integer32
_CfgWlan802dot1xAcctSrvPort_Object = MibTableColumn
cfgWlan802dot1xAcctSrvPort = _CfgWlan802dot1xAcctSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12, 1, 5),
    _CfgWlan802dot1xAcctSrvPort_Type()
)
cfgWlan802dot1xAcctSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctSrvPort.setStatus("current")


class _CfgWlan802dot1xAcctSrvSharedSecret_Type(DisplayString):
    """Custom type cfgWlan802dot1xAcctSrvSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlan802dot1xAcctSrvSharedSecret_Type.__name__ = "DisplayString"
_CfgWlan802dot1xAcctSrvSharedSecret_Object = MibTableColumn
cfgWlan802dot1xAcctSrvSharedSecret = _CfgWlan802dot1xAcctSrvSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 12, 1, 6),
    _CfgWlan802dot1xAcctSrvSharedSecret_Type()
)
cfgWlan802dot1xAcctSrvSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot1xAcctSrvSharedSecret.setStatus("current")
_CfgWlan802dot11rTable_Object = MibTable
cfgWlan802dot11rTable = _CfgWlan802dot11rTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    cfgWlan802dot11rTable.setStatus("current")
_CfgWlan802dot11rTableEntry_Object = MibTableRow
cfgWlan802dot11rTableEntry = _CfgWlan802dot11rTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1)
)
cfgWlan802dot11rTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlan802dot11rIndex"),
)
if mibBuilder.loadTexts:
    cfgWlan802dot11rTableEntry.setStatus("current")


class _CfgWlan802dot11rIndex_Type(Integer32):
    """Custom type cfgWlan802dot11rIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgWlan802dot11rIndex_Type.__name__ = "Integer32"
_CfgWlan802dot11rIndex_Object = MibTableColumn
cfgWlan802dot11rIndex = _CfgWlan802dot11rIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 1),
    _CfgWlan802dot11rIndex_Type()
)
cfgWlan802dot11rIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlan802dot11rIndex.setStatus("current")


class _CfgWlan802dot11rName_Type(DisplayString):
    """Custom type cfgWlan802dot11rName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlan802dot11rName_Type.__name__ = "DisplayString"
_CfgWlan802dot11rName_Object = MibTableColumn
cfgWlan802dot11rName = _CfgWlan802dot11rName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 2),
    _CfgWlan802dot11rName_Type()
)
cfgWlan802dot11rName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlan802dot11rName.setStatus("current")


class _CfgWlan802dot11rEnabled_Type(Integer32):
    """Custom type cfgWlan802dot11rEnabled based on Integer32"""
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


_CfgWlan802dot11rEnabled_Type.__name__ = "Integer32"
_CfgWlan802dot11rEnabled_Object = MibTableColumn
cfgWlan802dot11rEnabled = _CfgWlan802dot11rEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 3),
    _CfgWlan802dot11rEnabled_Type()
)
cfgWlan802dot11rEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rEnabled.setStatus("current")


class _CfgWlan802dot11rMobilityDomain_Type(DisplayString):
    """Custom type cfgWlan802dot11rMobilityDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_CfgWlan802dot11rMobilityDomain_Type.__name__ = "DisplayString"
_CfgWlan802dot11rMobilityDomain_Object = MibTableColumn
cfgWlan802dot11rMobilityDomain = _CfgWlan802dot11rMobilityDomain_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 4),
    _CfgWlan802dot11rMobilityDomain_Type()
)
cfgWlan802dot11rMobilityDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rMobilityDomain.setStatus("current")


class _CfgWlan802dot11rPmkR0KeyHolderIdentifier_Type(DisplayString):
    """Custom type cfgWlan802dot11rPmkR0KeyHolderIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CfgWlan802dot11rPmkR0KeyHolderIdentifier_Type.__name__ = "DisplayString"
_CfgWlan802dot11rPmkR0KeyHolderIdentifier_Object = MibTableColumn
cfgWlan802dot11rPmkR0KeyHolderIdentifier = _CfgWlan802dot11rPmkR0KeyHolderIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 5),
    _CfgWlan802dot11rPmkR0KeyHolderIdentifier_Type()
)
cfgWlan802dot11rPmkR0KeyHolderIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWlan802dot11rPmkR0KeyHolderIdentifier.setStatus("current")


class _CfgWlan802dot11rPmkR0Lifetime_Type(Integer32):
    """Custom type cfgWlan802dot11rPmkR0Lifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfgWlan802dot11rPmkR0Lifetime_Type.__name__ = "Integer32"
_CfgWlan802dot11rPmkR0Lifetime_Object = MibTableColumn
cfgWlan802dot11rPmkR0Lifetime = _CfgWlan802dot11rPmkR0Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 6),
    _CfgWlan802dot11rPmkR0Lifetime_Type()
)
cfgWlan802dot11rPmkR0Lifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rPmkR0Lifetime.setStatus("current")


class _CfgWlan802dot11rPmkR1KeyHolderIdentifier_Type(DisplayString):
    """Custom type cfgWlan802dot11rPmkR1KeyHolderIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_CfgWlan802dot11rPmkR1KeyHolderIdentifier_Type.__name__ = "DisplayString"
_CfgWlan802dot11rPmkR1KeyHolderIdentifier_Object = MibTableColumn
cfgWlan802dot11rPmkR1KeyHolderIdentifier = _CfgWlan802dot11rPmkR1KeyHolderIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 7),
    _CfgWlan802dot11rPmkR1KeyHolderIdentifier_Type()
)
cfgWlan802dot11rPmkR1KeyHolderIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rPmkR1KeyHolderIdentifier.setStatus("current")


class _CfgWlan802dot11rPmkR1Push_Type(Integer32):
    """Custom type cfgWlan802dot11rPmkR1Push based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("donotpush", 0),
          ("push", 1))
    )


_CfgWlan802dot11rPmkR1Push_Type.__name__ = "Integer32"
_CfgWlan802dot11rPmkR1Push_Object = MibTableColumn
cfgWlan802dot11rPmkR1Push = _CfgWlan802dot11rPmkR1Push_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 9),
    _CfgWlan802dot11rPmkR1Push_Type()
)
cfgWlan802dot11rPmkR1Push.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rPmkR1Push.setStatus("current")
_CfgWlan802dot11rR0KHParameter_Type = Integer32
_CfgWlan802dot11rR0KHParameter_Object = MibTableColumn
cfgWlan802dot11rR0KHParameter = _CfgWlan802dot11rR0KHParameter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 10),
    _CfgWlan802dot11rR0KHParameter_Type()
)
cfgWlan802dot11rR0KHParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHParameter.setStatus("current")
_CfgWlan802dot11rR1KHParameter_Type = Integer32
_CfgWlan802dot11rR1KHParameter_Object = MibTableColumn
cfgWlan802dot11rR1KHParameter = _CfgWlan802dot11rR1KHParameter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 11),
    _CfgWlan802dot11rR1KHParameter_Type()
)
cfgWlan802dot11rR1KHParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHParameter.setStatus("current")


class _CfgWlan802dot11rExpirationEnabled_Type(Integer32):
    """Custom type cfgWlan802dot11rExpirationEnabled based on Integer32"""
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


_CfgWlan802dot11rExpirationEnabled_Type.__name__ = "Integer32"
_CfgWlan802dot11rExpirationEnabled_Object = MibTableColumn
cfgWlan802dot11rExpirationEnabled = _CfgWlan802dot11rExpirationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 12),
    _CfgWlan802dot11rExpirationEnabled_Type()
)
cfgWlan802dot11rExpirationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rExpirationEnabled.setStatus("current")


class _CfgWlan802dot11rExpirationTime_Type(DisplayString):
    """Custom type cfgWlan802dot11rExpirationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_CfgWlan802dot11rExpirationTime_Type.__name__ = "DisplayString"
_CfgWlan802dot11rExpirationTime_Object = MibTableColumn
cfgWlan802dot11rExpirationTime = _CfgWlan802dot11rExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 13),
    _CfgWlan802dot11rExpirationTime_Type()
)
cfgWlan802dot11rExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rExpirationTime.setStatus("current")


class _CfgWlan802dot11rVlan_Type(Integer32):
    """Custom type cfgWlan802dot11rVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CfgWlan802dot11rVlan_Type.__name__ = "Integer32"
_CfgWlan802dot11rVlan_Object = MibTableColumn
cfgWlan802dot11rVlan = _CfgWlan802dot11rVlan_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 13, 1, 14),
    _CfgWlan802dot11rVlan_Type()
)
cfgWlan802dot11rVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rVlan.setStatus("current")
_CfgWlan802dot11rR0KHTable_Object = MibTable
cfgWlan802dot11rR0KHTable = _CfgWlan802dot11rR0KHTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14)
)
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHTable.setStatus("current")
_CfgWlan802dot11rR0KHTableEntry_Object = MibTableRow
cfgWlan802dot11rR0KHTableEntry = _CfgWlan802dot11rR0KHTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14, 1)
)
cfgWlan802dot11rR0KHTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlan802dot11rR0KHIndex"),
)
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHTableEntry.setStatus("current")


class _CfgWlan802dot11rR0KHIndex_Type(Integer32):
    """Custom type cfgWlan802dot11rR0KHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CfgWlan802dot11rR0KHIndex_Type.__name__ = "Integer32"
_CfgWlan802dot11rR0KHIndex_Object = MibTableColumn
cfgWlan802dot11rR0KHIndex = _CfgWlan802dot11rR0KHIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14, 1, 1),
    _CfgWlan802dot11rR0KHIndex_Type()
)
cfgWlan802dot11rR0KHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHIndex.setStatus("current")
_CfgWlan802dot11rR0KHId_Type = Integer32
_CfgWlan802dot11rR0KHId_Object = MibTableColumn
cfgWlan802dot11rR0KHId = _CfgWlan802dot11rR0KHId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14, 1, 2),
    _CfgWlan802dot11rR0KHId_Type()
)
cfgWlan802dot11rR0KHId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHId.setStatus("current")


class _CfgWlan802dot11rR0KHEnabled_Type(Integer32):
    """Custom type cfgWlan802dot11rR0KHEnabled based on Integer32"""
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


_CfgWlan802dot11rR0KHEnabled_Type.__name__ = "Integer32"
_CfgWlan802dot11rR0KHEnabled_Object = MibTableColumn
cfgWlan802dot11rR0KHEnabled = _CfgWlan802dot11rR0KHEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14, 1, 3),
    _CfgWlan802dot11rR0KHEnabled_Type()
)
cfgWlan802dot11rR0KHEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHEnabled.setStatus("current")


class _CfgWlan802dot11rR0KHDestinationMac_Type(DisplayString):
    """Custom type cfgWlan802dot11rR0KHDestinationMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlan802dot11rR0KHDestinationMac_Type.__name__ = "DisplayString"
_CfgWlan802dot11rR0KHDestinationMac_Object = MibTableColumn
cfgWlan802dot11rR0KHDestinationMac = _CfgWlan802dot11rR0KHDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14, 1, 4),
    _CfgWlan802dot11rR0KHDestinationMac_Type()
)
cfgWlan802dot11rR0KHDestinationMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHDestinationMac.setStatus("current")


class _CfgWlan802dot11rR0KHHID_Type(DisplayString):
    """Custom type cfgWlan802dot11rR0KHHID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CfgWlan802dot11rR0KHHID_Type.__name__ = "DisplayString"
_CfgWlan802dot11rR0KHHID_Object = MibTableColumn
cfgWlan802dot11rR0KHHID = _CfgWlan802dot11rR0KHHID_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14, 1, 5),
    _CfgWlan802dot11rR0KHHID_Type()
)
cfgWlan802dot11rR0KHHID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHHID.setStatus("current")


class _CfgWlan802dot11rR0KHKey_Type(DisplayString):
    """Custom type cfgWlan802dot11rR0KHKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_CfgWlan802dot11rR0KHKey_Type.__name__ = "DisplayString"
_CfgWlan802dot11rR0KHKey_Object = MibTableColumn
cfgWlan802dot11rR0KHKey = _CfgWlan802dot11rR0KHKey_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 14, 1, 6),
    _CfgWlan802dot11rR0KHKey_Type()
)
cfgWlan802dot11rR0KHKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR0KHKey.setStatus("current")
_CfgWlan802dot11rR1KHTable_Object = MibTable
cfgWlan802dot11rR1KHTable = _CfgWlan802dot11rR1KHTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15)
)
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHTable.setStatus("current")
_CfgWlan802dot11rR1KHTableEntry_Object = MibTableRow
cfgWlan802dot11rR1KHTableEntry = _CfgWlan802dot11rR1KHTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15, 1)
)
cfgWlan802dot11rR1KHTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlan802dot11rR1KHIndex"),
)
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHTableEntry.setStatus("current")


class _CfgWlan802dot11rR1KHIndex_Type(Integer32):
    """Custom type cfgWlan802dot11rR1KHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CfgWlan802dot11rR1KHIndex_Type.__name__ = "Integer32"
_CfgWlan802dot11rR1KHIndex_Object = MibTableColumn
cfgWlan802dot11rR1KHIndex = _CfgWlan802dot11rR1KHIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15, 1, 1),
    _CfgWlan802dot11rR1KHIndex_Type()
)
cfgWlan802dot11rR1KHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHIndex.setStatus("current")
_CfgWlan802dot11rR1KHId_Type = Integer32
_CfgWlan802dot11rR1KHId_Object = MibTableColumn
cfgWlan802dot11rR1KHId = _CfgWlan802dot11rR1KHId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15, 1, 2),
    _CfgWlan802dot11rR1KHId_Type()
)
cfgWlan802dot11rR1KHId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHId.setStatus("current")


class _CfgWlan802dot11rR1KHEnabled_Type(Integer32):
    """Custom type cfgWlan802dot11rR1KHEnabled based on Integer32"""
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


_CfgWlan802dot11rR1KHEnabled_Type.__name__ = "Integer32"
_CfgWlan802dot11rR1KHEnabled_Object = MibTableColumn
cfgWlan802dot11rR1KHEnabled = _CfgWlan802dot11rR1KHEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15, 1, 3),
    _CfgWlan802dot11rR1KHEnabled_Type()
)
cfgWlan802dot11rR1KHEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHEnabled.setStatus("current")


class _CfgWlan802dot11rR1KHDestinationMac_Type(DisplayString):
    """Custom type cfgWlan802dot11rR1KHDestinationMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlan802dot11rR1KHDestinationMac_Type.__name__ = "DisplayString"
_CfgWlan802dot11rR1KHDestinationMac_Object = MibTableColumn
cfgWlan802dot11rR1KHDestinationMac = _CfgWlan802dot11rR1KHDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15, 1, 4),
    _CfgWlan802dot11rR1KHDestinationMac_Type()
)
cfgWlan802dot11rR1KHDestinationMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHDestinationMac.setStatus("current")


class _CfgWlan802dot11rR1KHHID_Type(DisplayString):
    """Custom type cfgWlan802dot11rR1KHHID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlan802dot11rR1KHHID_Type.__name__ = "DisplayString"
_CfgWlan802dot11rR1KHHID_Object = MibTableColumn
cfgWlan802dot11rR1KHHID = _CfgWlan802dot11rR1KHHID_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15, 1, 5),
    _CfgWlan802dot11rR1KHHID_Type()
)
cfgWlan802dot11rR1KHHID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHHID.setStatus("current")


class _CfgWlan802dot11rR1KHKey_Type(DisplayString):
    """Custom type cfgWlan802dot11rR1KHKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_CfgWlan802dot11rR1KHKey_Type.__name__ = "DisplayString"
_CfgWlan802dot11rR1KHKey_Object = MibTableColumn
cfgWlan802dot11rR1KHKey = _CfgWlan802dot11rR1KHKey_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 15, 1, 6),
    _CfgWlan802dot11rR1KHKey_Type()
)
cfgWlan802dot11rR1KHKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlan802dot11rR1KHKey.setStatus("current")
_CfgWlanNeighbourTable_Object = MibTable
cfgWlanNeighbourTable = _CfgWlanNeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 16)
)
if mibBuilder.loadTexts:
    cfgWlanNeighbourTable.setStatus("current")
_CfgWlanNeighbourTableEntry_Object = MibTableRow
cfgWlanNeighbourTableEntry = _CfgWlanNeighbourTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 16, 1)
)
cfgWlanNeighbourTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgWlanNeighbourIndex"),
)
if mibBuilder.loadTexts:
    cfgWlanNeighbourTableEntry.setStatus("current")


class _CfgWlanNeighbourIndex_Type(Integer32):
    """Custom type cfgWlanNeighbourIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CfgWlanNeighbourIndex_Type.__name__ = "Integer32"
_CfgWlanNeighbourIndex_Object = MibTableColumn
cfgWlanNeighbourIndex = _CfgWlanNeighbourIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 16, 1, 1),
    _CfgWlanNeighbourIndex_Type()
)
cfgWlanNeighbourIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgWlanNeighbourIndex.setStatus("current")
_CfgWlanNeighbourId_Type = Integer32
_CfgWlanNeighbourId_Object = MibTableColumn
cfgWlanNeighbourId = _CfgWlanNeighbourId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 16, 1, 2),
    _CfgWlanNeighbourId_Type()
)
cfgWlanNeighbourId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanNeighbourId.setStatus("current")


class _CfgWlanNeighbourEnabled_Type(Integer32):
    """Custom type cfgWlanNeighbourEnabled based on Integer32"""
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


_CfgWlanNeighbourEnabled_Type.__name__ = "Integer32"
_CfgWlanNeighbourEnabled_Object = MibTableColumn
cfgWlanNeighbourEnabled = _CfgWlanNeighbourEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 16, 1, 3),
    _CfgWlanNeighbourEnabled_Type()
)
cfgWlanNeighbourEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanNeighbourEnabled.setStatus("current")


class _CfgWlanNeighbourBSSID_Type(DisplayString):
    """Custom type cfgWlanNeighbourBSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_CfgWlanNeighbourBSSID_Type.__name__ = "DisplayString"
_CfgWlanNeighbourBSSID_Object = MibTableColumn
cfgWlanNeighbourBSSID = _CfgWlanNeighbourBSSID_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 16, 1, 4),
    _CfgWlanNeighbourBSSID_Type()
)
cfgWlanNeighbourBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanNeighbourBSSID.setStatus("current")


class _CfgWlanNeighbourFrequency_Type(Integer32):
    """Custom type cfgWlanNeighbourFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_CfgWlanNeighbourFrequency_Type.__name__ = "Integer32"
_CfgWlanNeighbourFrequency_Object = MibTableColumn
cfgWlanNeighbourFrequency = _CfgWlanNeighbourFrequency_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 3, 16, 1, 5),
    _CfgWlanNeighbourFrequency_Type()
)
cfgWlanNeighbourFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanNeighbourFrequency.setStatus("current")
_CfgRouting_ObjectIdentity = ObjectIdentity
cfgRouting = _CfgRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4)
)
_CfgRouteDefault_ObjectIdentity = ObjectIdentity
cfgRouteDefault = _CfgRouteDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 1)
)
_CfgRouteDefGateway_Type = IpAddress
_CfgRouteDefGateway_Object = MibScalar
cfgRouteDefGateway = _CfgRouteDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 1, 1),
    _CfgRouteDefGateway_Type()
)
cfgRouteDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRouteDefGateway.setStatus("current")


class _CfgRouteDefGwOverride_Type(Integer32):
    """Custom type cfgRouteDefGwOverride based on Integer32"""
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


_CfgRouteDefGwOverride_Type.__name__ = "Integer32"
_CfgRouteDefGwOverride_Object = MibScalar
cfgRouteDefGwOverride = _CfgRouteDefGwOverride_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 1, 2),
    _CfgRouteDefGwOverride_Type()
)
cfgRouteDefGwOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRouteDefGwOverride.setStatus("current")
_CfgRouteTable_Object = MibTable
cfgRouteTable = _CfgRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cfgRouteTable.setStatus("current")
_CfgRouteTableEntry_Object = MibTableRow
cfgRouteTableEntry = _CfgRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2, 1)
)
cfgRouteTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgRouteTableIndex"),
)
if mibBuilder.loadTexts:
    cfgRouteTableEntry.setStatus("current")


class _CfgRouteTableIndex_Type(Integer32):
    """Custom type cfgRouteTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 265),
    )


_CfgRouteTableIndex_Type.__name__ = "Integer32"
_CfgRouteTableIndex_Object = MibTableColumn
cfgRouteTableIndex = _CfgRouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2, 1, 1),
    _CfgRouteTableIndex_Type()
)
cfgRouteTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgRouteTableIndex.setStatus("current")


class _CfgRouteTableEnabled_Type(Integer32):
    """Custom type cfgRouteTableEnabled based on Integer32"""
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


_CfgRouteTableEnabled_Type.__name__ = "Integer32"
_CfgRouteTableEnabled_Object = MibTableColumn
cfgRouteTableEnabled = _CfgRouteTableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2, 1, 2),
    _CfgRouteTableEnabled_Type()
)
cfgRouteTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRouteTableEnabled.setStatus("current")
_CfgRouteTableDestinationNetwork_Type = DisplayString
_CfgRouteTableDestinationNetwork_Object = MibTableColumn
cfgRouteTableDestinationNetwork = _CfgRouteTableDestinationNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2, 1, 3),
    _CfgRouteTableDestinationNetwork_Type()
)
cfgRouteTableDestinationNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRouteTableDestinationNetwork.setStatus("current")
_CfgRouteTableGateway_Type = IpAddress
_CfgRouteTableGateway_Object = MibTableColumn
cfgRouteTableGateway = _CfgRouteTableGateway_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2, 1, 5),
    _CfgRouteTableGateway_Type()
)
cfgRouteTableGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRouteTableGateway.setStatus("current")
_CfgRouteTableSource_Type = IpAddress
_CfgRouteTableSource_Object = MibTableColumn
cfgRouteTableSource = _CfgRouteTableSource_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2, 1, 6),
    _CfgRouteTableSource_Type()
)
cfgRouteTableSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRouteTableSource.setStatus("current")


class _CfgRouteTableCarpId_Type(Integer32):
    """Custom type cfgRouteTableCarpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_CfgRouteTableCarpId_Type.__name__ = "Integer32"
_CfgRouteTableCarpId_Object = MibTableColumn
cfgRouteTableCarpId = _CfgRouteTableCarpId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 2, 1, 8),
    _CfgRouteTableCarpId_Type()
)
cfgRouteTableCarpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRouteTableCarpId.setStatus("current")
_CfgMRouteTable_Object = MibTable
cfgMRouteTable = _CfgMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cfgMRouteTable.setStatus("current")
_CfgMRouteTableEntry_Object = MibTableRow
cfgMRouteTableEntry = _CfgMRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3, 1)
)
cfgMRouteTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgMRouteTableIndex"),
)
if mibBuilder.loadTexts:
    cfgMRouteTableEntry.setStatus("current")


class _CfgMRouteTableIndex_Type(Integer32):
    """Custom type cfgMRouteTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgMRouteTableIndex_Type.__name__ = "Integer32"
_CfgMRouteTableIndex_Object = MibTableColumn
cfgMRouteTableIndex = _CfgMRouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3, 1, 1),
    _CfgMRouteTableIndex_Type()
)
cfgMRouteTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgMRouteTableIndex.setStatus("current")


class _CfgMRouteTableEnabled_Type(Integer32):
    """Custom type cfgMRouteTableEnabled based on Integer32"""
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


_CfgMRouteTableEnabled_Type.__name__ = "Integer32"
_CfgMRouteTableEnabled_Object = MibTableColumn
cfgMRouteTableEnabled = _CfgMRouteTableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3, 1, 2),
    _CfgMRouteTableEnabled_Type()
)
cfgMRouteTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMRouteTableEnabled.setStatus("current")


class _CfgMRouteTableInput_Type(DisplayString):
    """Custom type cfgMRouteTableInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgMRouteTableInput_Type.__name__ = "DisplayString"
_CfgMRouteTableInput_Object = MibTableColumn
cfgMRouteTableInput = _CfgMRouteTableInput_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3, 1, 3),
    _CfgMRouteTableInput_Type()
)
cfgMRouteTableInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMRouteTableInput.setStatus("current")
_CfgMRouteTableSource_Type = IpAddress
_CfgMRouteTableSource_Object = MibTableColumn
cfgMRouteTableSource = _CfgMRouteTableSource_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3, 1, 4),
    _CfgMRouteTableSource_Type()
)
cfgMRouteTableSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMRouteTableSource.setStatus("current")
_CfgMRouteTableGroup_Type = IpAddress
_CfgMRouteTableGroup_Object = MibTableColumn
cfgMRouteTableGroup = _CfgMRouteTableGroup_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3, 1, 5),
    _CfgMRouteTableGroup_Type()
)
cfgMRouteTableGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMRouteTableGroup.setStatus("current")


class _CfgMRouteTableOutput_Type(DisplayString):
    """Custom type cfgMRouteTableOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgMRouteTableOutput_Type.__name__ = "DisplayString"
_CfgMRouteTableOutput_Object = MibTableColumn
cfgMRouteTableOutput = _CfgMRouteTableOutput_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 4, 3, 1, 6),
    _CfgMRouteTableOutput_Type()
)
cfgMRouteTableOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMRouteTableOutput.setStatus("current")
_CfgIpTables_ObjectIdentity = ObjectIdentity
cfgIpTables = _CfgIpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 5)
)
_CfgQos_ObjectIdentity = ObjectIdentity
cfgQos = _CfgQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6)
)


class _CfgQosL3PrioEnabled_Type(Integer32):
    """Custom type cfgQosL3PrioEnabled based on Integer32"""
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


_CfgQosL3PrioEnabled_Type.__name__ = "Integer32"
_CfgQosL3PrioEnabled_Object = MibScalar
cfgQosL3PrioEnabled = _CfgQosL3PrioEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 1),
    _CfgQosL3PrioEnabled_Type()
)
cfgQosL3PrioEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosL3PrioEnabled.setStatus("current")
_CfgQosDscpToTidMapTable_Object = MibTable
cfgQosDscpToTidMapTable = _CfgQosDscpToTidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cfgQosDscpToTidMapTable.setStatus("current")
_CfgQosDscpToTidMapTableEntry_Object = MibTableRow
cfgQosDscpToTidMapTableEntry = _CfgQosDscpToTidMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 2, 1)
)
cfgQosDscpToTidMapTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgQosDscpToTidMapTableIndex"),
)
if mibBuilder.loadTexts:
    cfgQosDscpToTidMapTableEntry.setStatus("current")


class _CfgQosDscpToTidMapTableIndex_Type(Integer32):
    """Custom type cfgQosDscpToTidMapTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CfgQosDscpToTidMapTableIndex_Type.__name__ = "Integer32"
_CfgQosDscpToTidMapTableIndex_Object = MibTableColumn
cfgQosDscpToTidMapTableIndex = _CfgQosDscpToTidMapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 2, 1, 1),
    _CfgQosDscpToTidMapTableIndex_Type()
)
cfgQosDscpToTidMapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgQosDscpToTidMapTableIndex.setStatus("current")


class _CfgQosDscpToTidMapValue_Type(Integer32):
    """Custom type cfgQosDscpToTidMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CfgQosDscpToTidMapValue_Type.__name__ = "Integer32"
_CfgQosDscpToTidMapValue_Object = MibTableColumn
cfgQosDscpToTidMapValue = _CfgQosDscpToTidMapValue_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 2, 1, 2),
    _CfgQosDscpToTidMapValue_Type()
)
cfgQosDscpToTidMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosDscpToTidMapValue.setStatus("current")
_CfgQosVlanToTidMapTable_Object = MibTable
cfgQosVlanToTidMapTable = _CfgQosVlanToTidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cfgQosVlanToTidMapTable.setStatus("current")
_CfgQosVlanToTidMapTableEntry_Object = MibTableRow
cfgQosVlanToTidMapTableEntry = _CfgQosVlanToTidMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 3, 1)
)
cfgQosVlanToTidMapTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgQosVlanToTidMapTableIndex"),
)
if mibBuilder.loadTexts:
    cfgQosVlanToTidMapTableEntry.setStatus("current")


class _CfgQosVlanToTidMapTableIndex_Type(Integer32):
    """Custom type cfgQosVlanToTidMapTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CfgQosVlanToTidMapTableIndex_Type.__name__ = "Integer32"
_CfgQosVlanToTidMapTableIndex_Object = MibTableColumn
cfgQosVlanToTidMapTableIndex = _CfgQosVlanToTidMapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 3, 1, 1),
    _CfgQosVlanToTidMapTableIndex_Type()
)
cfgQosVlanToTidMapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgQosVlanToTidMapTableIndex.setStatus("current")


class _CfgQosVlanToTidMapValue_Type(Integer32):
    """Custom type cfgQosVlanToTidMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CfgQosVlanToTidMapValue_Type.__name__ = "Integer32"
_CfgQosVlanToTidMapValue_Object = MibTableColumn
cfgQosVlanToTidMapValue = _CfgQosVlanToTidMapValue_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 3, 1, 2),
    _CfgQosVlanToTidMapValue_Type()
)
cfgQosVlanToTidMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosVlanToTidMapValue.setStatus("current")
_CfgQosIpToTidMapTable_Object = MibTable
cfgQosIpToTidMapTable = _CfgQosIpToTidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cfgQosIpToTidMapTable.setStatus("current")
_CfgQosIpToTidMapTableEntry_Object = MibTableRow
cfgQosIpToTidMapTableEntry = _CfgQosIpToTidMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1)
)
cfgQosIpToTidMapTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgQosIpToTidMapTableIndex"),
)
if mibBuilder.loadTexts:
    cfgQosIpToTidMapTableEntry.setStatus("current")


class _CfgQosIpToTidMapTableIndex_Type(Integer32):
    """Custom type cfgQosIpToTidMapTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CfgQosIpToTidMapTableIndex_Type.__name__ = "Integer32"
_CfgQosIpToTidMapTableIndex_Object = MibTableColumn
cfgQosIpToTidMapTableIndex = _CfgQosIpToTidMapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 1),
    _CfgQosIpToTidMapTableIndex_Type()
)
cfgQosIpToTidMapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapTableIndex.setStatus("current")
_CfgQosIpToTidMapSrcNet_Type = OctetString
_CfgQosIpToTidMapSrcNet_Object = MibTableColumn
cfgQosIpToTidMapSrcNet = _CfgQosIpToTidMapSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 2),
    _CfgQosIpToTidMapSrcNet_Type()
)
cfgQosIpToTidMapSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapSrcNet.setStatus("current")
_CfgQosIpToTidMapDestNet_Type = OctetString
_CfgQosIpToTidMapDestNet_Object = MibTableColumn
cfgQosIpToTidMapDestNet = _CfgQosIpToTidMapDestNet_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 3),
    _CfgQosIpToTidMapDestNet_Type()
)
cfgQosIpToTidMapDestNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapDestNet.setStatus("current")


class _CfgQosIpToTidMapProto_Type(Integer32):
    """Custom type cfgQosIpToTidMapProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("udp", 1),
          ("tcp", 2))
    )


_CfgQosIpToTidMapProto_Type.__name__ = "Integer32"
_CfgQosIpToTidMapProto_Object = MibTableColumn
cfgQosIpToTidMapProto = _CfgQosIpToTidMapProto_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 4),
    _CfgQosIpToTidMapProto_Type()
)
cfgQosIpToTidMapProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapProto.setStatus("current")


class _CfgQosIpToTidMapSrcPort_Type(Integer32):
    """Custom type cfgQosIpToTidMapSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )


_CfgQosIpToTidMapSrcPort_Type.__name__ = "Integer32"
_CfgQosIpToTidMapSrcPort_Object = MibTableColumn
cfgQosIpToTidMapSrcPort = _CfgQosIpToTidMapSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 5),
    _CfgQosIpToTidMapSrcPort_Type()
)
cfgQosIpToTidMapSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapSrcPort.setStatus("current")


class _CfgQosIpToTidMapDestPort_Type(Integer32):
    """Custom type cfgQosIpToTidMapDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )


_CfgQosIpToTidMapDestPort_Type.__name__ = "Integer32"
_CfgQosIpToTidMapDestPort_Object = MibTableColumn
cfgQosIpToTidMapDestPort = _CfgQosIpToTidMapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 6),
    _CfgQosIpToTidMapDestPort_Type()
)
cfgQosIpToTidMapDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapDestPort.setStatus("current")


class _CfgQosIpToTidMapPrecedence_Type(Integer32):
    """Custom type cfgQosIpToTidMapPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CfgQosIpToTidMapPrecedence_Type.__name__ = "Integer32"
_CfgQosIpToTidMapPrecedence_Object = MibTableColumn
cfgQosIpToTidMapPrecedence = _CfgQosIpToTidMapPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 7),
    _CfgQosIpToTidMapPrecedence_Type()
)
cfgQosIpToTidMapPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapPrecedence.setStatus("current")


class _CfgQosIpToTidMapEnabled_Type(Integer32):
    """Custom type cfgQosIpToTidMapEnabled based on Integer32"""
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


_CfgQosIpToTidMapEnabled_Type.__name__ = "Integer32"
_CfgQosIpToTidMapEnabled_Object = MibTableColumn
cfgQosIpToTidMapEnabled = _CfgQosIpToTidMapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 6, 4, 1, 8),
    _CfgQosIpToTidMapEnabled_Type()
)
cfgQosIpToTidMapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgQosIpToTidMapEnabled.setStatus("current")
_CfgLogging_ObjectIdentity = ObjectIdentity
cfgLogging = _CfgLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11)
)
_CfgLogRemote_ObjectIdentity = ObjectIdentity
cfgLogRemote = _CfgLogRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2)
)
_CfgLogRemoteTable_Object = MibTable
cfgLogRemoteTable = _CfgLogRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    cfgLogRemoteTable.setStatus("current")
_CfgLogRemoteTableEntry_Object = MibTableRow
cfgLogRemoteTableEntry = _CfgLogRemoteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1, 1)
)
cfgLogRemoteTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgLogRemoteIndex"),
)
if mibBuilder.loadTexts:
    cfgLogRemoteTableEntry.setStatus("current")


class _CfgLogRemoteIndex_Type(Integer32):
    """Custom type cfgLogRemoteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CfgLogRemoteIndex_Type.__name__ = "Integer32"
_CfgLogRemoteIndex_Object = MibTableColumn
cfgLogRemoteIndex = _CfgLogRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1, 1, 1),
    _CfgLogRemoteIndex_Type()
)
cfgLogRemoteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgLogRemoteIndex.setStatus("current")


class _CfgLogRemoteEnabled_Type(Integer32):
    """Custom type cfgLogRemoteEnabled based on Integer32"""
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


_CfgLogRemoteEnabled_Type.__name__ = "Integer32"
_CfgLogRemoteEnabled_Object = MibTableColumn
cfgLogRemoteEnabled = _CfgLogRemoteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1, 1, 2),
    _CfgLogRemoteEnabled_Type()
)
cfgLogRemoteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLogRemoteEnabled.setStatus("current")


class _CfgLogRemoteLevel_Type(Integer32):
    """Custom type cfgLogRemoteLevel based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_CfgLogRemoteLevel_Type.__name__ = "Integer32"
_CfgLogRemoteLevel_Object = MibTableColumn
cfgLogRemoteLevel = _CfgLogRemoteLevel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1, 1, 3),
    _CfgLogRemoteLevel_Type()
)
cfgLogRemoteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgLogRemoteLevel.setStatus("current")


class _CfgLogRemoteProtocol_Type(Integer32):
    """Custom type cfgLogRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1))
    )


_CfgLogRemoteProtocol_Type.__name__ = "Integer32"
_CfgLogRemoteProtocol_Object = MibTableColumn
cfgLogRemoteProtocol = _CfgLogRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1, 1, 4),
    _CfgLogRemoteProtocol_Type()
)
cfgLogRemoteProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLogRemoteProtocol.setStatus("current")
_CfgLogRemoteIp_Type = IpAddress
_CfgLogRemoteIp_Object = MibTableColumn
cfgLogRemoteIp = _CfgLogRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1, 1, 5),
    _CfgLogRemoteIp_Type()
)
cfgLogRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLogRemoteIp.setStatus("current")
_CfgLogRemotePort_Type = Integer32
_CfgLogRemotePort_Object = MibTableColumn
cfgLogRemotePort = _CfgLogRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 11, 2, 1, 1, 6),
    _CfgLogRemotePort_Type()
)
cfgLogRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLogRemotePort.setStatus("current")
_CfgSnmp_ObjectIdentity = ObjectIdentity
cfgSnmp = _CfgSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12)
)
_CfgSnmpd_ObjectIdentity = ObjectIdentity
cfgSnmpd = _CfgSnmpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1)
)


class _CfgSnmpdLocation_Type(DisplayString):
    """Custom type cfgSnmpdLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpdLocation_Type.__name__ = "DisplayString"
_CfgSnmpdLocation_Object = MibScalar
cfgSnmpdLocation = _CfgSnmpdLocation_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 1),
    _CfgSnmpdLocation_Type()
)
cfgSnmpdLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdLocation.setStatus("current")


class _CfgSnmpdContact_Type(DisplayString):
    """Custom type cfgSnmpdContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpdContact_Type.__name__ = "DisplayString"
_CfgSnmpdContact_Object = MibScalar
cfgSnmpdContact = _CfgSnmpdContact_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 2),
    _CfgSnmpdContact_Type()
)
cfgSnmpdContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdContact.setStatus("current")


class _CfgSnmpdVersion_Type(Integer32):
    """Custom type cfgSnmpdVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v2c", 0),
          ("v3usm", 1))
    )


_CfgSnmpdVersion_Type.__name__ = "Integer32"
_CfgSnmpdVersion_Object = MibScalar
cfgSnmpdVersion = _CfgSnmpdVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 3),
    _CfgSnmpdVersion_Type()
)
cfgSnmpdVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdVersion.setStatus("current")


class _CfgSnmpdName_Type(DisplayString):
    """Custom type cfgSnmpdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpdName_Type.__name__ = "DisplayString"
_CfgSnmpdName_Object = MibScalar
cfgSnmpdName = _CfgSnmpdName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 4),
    _CfgSnmpdName_Type()
)
cfgSnmpdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdName.setStatus("current")


class _CfgSnmpdEnabled_Type(Integer32):
    """Custom type cfgSnmpdEnabled based on Integer32"""
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


_CfgSnmpdEnabled_Type.__name__ = "Integer32"
_CfgSnmpdEnabled_Object = MibScalar
cfgSnmpdEnabled = _CfgSnmpdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 5),
    _CfgSnmpdEnabled_Type()
)
cfgSnmpdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdEnabled.setStatus("current")


class _CfgSnmpdAddress_Type(DisplayString):
    """Custom type cfgSnmpdAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpdAddress_Type.__name__ = "DisplayString"
_CfgSnmpdAddress_Object = MibScalar
cfgSnmpdAddress = _CfgSnmpdAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 6),
    _CfgSnmpdAddress_Type()
)
cfgSnmpdAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdAddress.setStatus("current")
_CfgSnmpdCommunity_ObjectIdentity = ObjectIdentity
cfgSnmpdCommunity = _CfgSnmpdCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 100)
)


class _CfgSnmpdComAdmin_Type(DisplayString):
    """Custom type cfgSnmpdComAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpdComAdmin_Type.__name__ = "DisplayString"
_CfgSnmpdComAdmin_Object = MibScalar
cfgSnmpdComAdmin = _CfgSnmpdComAdmin_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 100, 1),
    _CfgSnmpdComAdmin_Type()
)
cfgSnmpdComAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdComAdmin.setStatus("current")


class _CfgSnmpdComMaintainer_Type(DisplayString):
    """Custom type cfgSnmpdComMaintainer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpdComMaintainer_Type.__name__ = "DisplayString"
_CfgSnmpdComMaintainer_Object = MibScalar
cfgSnmpdComMaintainer = _CfgSnmpdComMaintainer_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 100, 2),
    _CfgSnmpdComMaintainer_Type()
)
cfgSnmpdComMaintainer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdComMaintainer.setStatus("current")


class _CfgSnmpdComMonitor_Type(DisplayString):
    """Custom type cfgSnmpdComMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpdComMonitor_Type.__name__ = "DisplayString"
_CfgSnmpdComMonitor_Object = MibScalar
cfgSnmpdComMonitor = _CfgSnmpdComMonitor_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 1, 100, 3),
    _CfgSnmpdComMonitor_Type()
)
cfgSnmpdComMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpdComMonitor.setStatus("current")
_CfgSnmpTrap_ObjectIdentity = ObjectIdentity
cfgSnmpTrap = _CfgSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 10)
)


class _CfgSnmpTrapEnabled_Type(Integer32):
    """Custom type cfgSnmpTrapEnabled based on Integer32"""
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


_CfgSnmpTrapEnabled_Type.__name__ = "Integer32"
_CfgSnmpTrapEnabled_Object = MibScalar
cfgSnmpTrapEnabled = _CfgSnmpTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 10, 1),
    _CfgSnmpTrapEnabled_Type()
)
cfgSnmpTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpTrapEnabled.setStatus("current")


class _CfgSnmpTrapVersion_Type(Integer32):
    """Custom type cfgSnmpTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3usm", 2))
    )


_CfgSnmpTrapVersion_Type.__name__ = "Integer32"
_CfgSnmpTrapVersion_Object = MibScalar
cfgSnmpTrapVersion = _CfgSnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 10, 2),
    _CfgSnmpTrapVersion_Type()
)
cfgSnmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpTrapVersion.setStatus("current")


class _CfgSnmpTrapCommunity_Type(DisplayString):
    """Custom type cfgSnmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgSnmpTrapCommunity_Type.__name__ = "DisplayString"
_CfgSnmpTrapCommunity_Object = MibScalar
cfgSnmpTrapCommunity = _CfgSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 10, 3),
    _CfgSnmpTrapCommunity_Type()
)
cfgSnmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpTrapCommunity.setStatus("current")
_CfgSnmpTrapDest_Type = IpAddress
_CfgSnmpTrapDest_Object = MibScalar
cfgSnmpTrapDest = _CfgSnmpTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 12, 10, 4),
    _CfgSnmpTrapDest_Type()
)
cfgSnmpTrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpTrapDest.setStatus("current")
_CfgDhcp_ObjectIdentity = ObjectIdentity
cfgDhcp = _CfgDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13)
)
_CfgDhcpGlobal_ObjectIdentity = ObjectIdentity
cfgDhcpGlobal = _CfgDhcpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 1)
)


class _CfgDhcpGlobalEnabled_Type(Integer32):
    """Custom type cfgDhcpGlobalEnabled based on Integer32"""
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


_CfgDhcpGlobalEnabled_Type.__name__ = "Integer32"
_CfgDhcpGlobalEnabled_Object = MibScalar
cfgDhcpGlobalEnabled = _CfgDhcpGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 1, 1),
    _CfgDhcpGlobalEnabled_Type()
)
cfgDhcpGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpGlobalEnabled.setStatus("current")
_CfgDhcpDnsmasqTable_Object = MibTable
cfgDhcpDnsmasqTable = _CfgDhcpDnsmasqTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    cfgDhcpDnsmasqTable.setStatus("current")
_CfgDhcpDnsmasqTableEntry_Object = MibTableRow
cfgDhcpDnsmasqTableEntry = _CfgDhcpDnsmasqTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 2, 1)
)
cfgDhcpDnsmasqTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgDhcpDnsmasqIndex"),
)
if mibBuilder.loadTexts:
    cfgDhcpDnsmasqTableEntry.setStatus("current")


class _CfgDhcpDnsmasqIndex_Type(Integer32):
    """Custom type cfgDhcpDnsmasqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CfgDhcpDnsmasqIndex_Type.__name__ = "Integer32"
_CfgDhcpDnsmasqIndex_Object = MibTableColumn
cfgDhcpDnsmasqIndex = _CfgDhcpDnsmasqIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 2, 1, 1),
    _CfgDhcpDnsmasqIndex_Type()
)
cfgDhcpDnsmasqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgDhcpDnsmasqIndex.setStatus("current")


class _CfgDhcpDnsmasqScopeParameter_Type(Integer32):
    """Custom type cfgDhcpDnsmasqScopeParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CfgDhcpDnsmasqScopeParameter_Type.__name__ = "Integer32"
_CfgDhcpDnsmasqScopeParameter_Object = MibTableColumn
cfgDhcpDnsmasqScopeParameter = _CfgDhcpDnsmasqScopeParameter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 2, 1, 2),
    _CfgDhcpDnsmasqScopeParameter_Type()
)
cfgDhcpDnsmasqScopeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpDnsmasqScopeParameter.setStatus("current")
_CfgDhcpScopeTable_Object = MibTable
cfgDhcpScopeTable = _CfgDhcpScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3)
)
if mibBuilder.loadTexts:
    cfgDhcpScopeTable.setStatus("current")
_CfgDhcpScopeTableEntry_Object = MibTableRow
cfgDhcpScopeTableEntry = _CfgDhcpScopeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1)
)
cfgDhcpScopeTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgDhcpScopeIndex"),
)
if mibBuilder.loadTexts:
    cfgDhcpScopeTableEntry.setStatus("current")


class _CfgDhcpScopeIndex_Type(Integer32):
    """Custom type cfgDhcpScopeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CfgDhcpScopeIndex_Type.__name__ = "Integer32"
_CfgDhcpScopeIndex_Object = MibTableColumn
cfgDhcpScopeIndex = _CfgDhcpScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 1),
    _CfgDhcpScopeIndex_Type()
)
cfgDhcpScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgDhcpScopeIndex.setStatus("current")


class _CfgDhcpScopeId_Type(Integer32):
    """Custom type cfgDhcpScopeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CfgDhcpScopeId_Type.__name__ = "Integer32"
_CfgDhcpScopeId_Object = MibTableColumn
cfgDhcpScopeId = _CfgDhcpScopeId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 2),
    _CfgDhcpScopeId_Type()
)
cfgDhcpScopeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeId.setStatus("current")


class _CfgDhcpScopeInterface_Type(DisplayString):
    """Custom type cfgDhcpScopeInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgDhcpScopeInterface_Type.__name__ = "DisplayString"
_CfgDhcpScopeInterface_Object = MibTableColumn
cfgDhcpScopeInterface = _CfgDhcpScopeInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 3),
    _CfgDhcpScopeInterface_Type()
)
cfgDhcpScopeInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeInterface.setStatus("current")
_CfgDhcpScopeStart_Type = Integer32
_CfgDhcpScopeStart_Object = MibTableColumn
cfgDhcpScopeStart = _CfgDhcpScopeStart_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 4),
    _CfgDhcpScopeStart_Type()
)
cfgDhcpScopeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeStart.setStatus("current")
_CfgDhcpScopeLimit_Type = Integer32
_CfgDhcpScopeLimit_Object = MibTableColumn
cfgDhcpScopeLimit = _CfgDhcpScopeLimit_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 5),
    _CfgDhcpScopeLimit_Type()
)
cfgDhcpScopeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeLimit.setStatus("current")


class _CfgDhcpScopeLeasetime_Type(DisplayString):
    """Custom type cfgDhcpScopeLeasetime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgDhcpScopeLeasetime_Type.__name__ = "DisplayString"
_CfgDhcpScopeLeasetime_Object = MibTableColumn
cfgDhcpScopeLeasetime = _CfgDhcpScopeLeasetime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 6),
    _CfgDhcpScopeLeasetime_Type()
)
cfgDhcpScopeLeasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeLeasetime.setStatus("current")
_CfgDhcpScopeGateway_Type = IpAddress
_CfgDhcpScopeGateway_Object = MibTableColumn
cfgDhcpScopeGateway = _CfgDhcpScopeGateway_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 7),
    _CfgDhcpScopeGateway_Type()
)
cfgDhcpScopeGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeGateway.setStatus("current")
_CfgDhcpScopeDnsServer1_Type = IpAddress
_CfgDhcpScopeDnsServer1_Object = MibTableColumn
cfgDhcpScopeDnsServer1 = _CfgDhcpScopeDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 8),
    _CfgDhcpScopeDnsServer1_Type()
)
cfgDhcpScopeDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeDnsServer1.setStatus("current")
_CfgDhcpScopeDnsServer2_Type = IpAddress
_CfgDhcpScopeDnsServer2_Object = MibTableColumn
cfgDhcpScopeDnsServer2 = _CfgDhcpScopeDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 13, 3, 1, 9),
    _CfgDhcpScopeDnsServer2_Type()
)
cfgDhcpScopeDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhcpScopeDnsServer2.setStatus("current")
_CfgNtp_ObjectIdentity = ObjectIdentity
cfgNtp = _CfgNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 14)
)


class _CfgNtpEnabled_Type(Integer32):
    """Custom type cfgNtpEnabled based on Integer32"""
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


_CfgNtpEnabled_Type.__name__ = "Integer32"
_CfgNtpEnabled_Object = MibScalar
cfgNtpEnabled = _CfgNtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 14, 1),
    _CfgNtpEnabled_Type()
)
cfgNtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNtpEnabled.setStatus("current")
_CfgNtpServer1_Type = IpAddress
_CfgNtpServer1_Object = MibScalar
cfgNtpServer1 = _CfgNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 14, 2),
    _CfgNtpServer1_Type()
)
cfgNtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNtpServer1.setStatus("current")
_CfgNtpServer2_Type = IpAddress
_CfgNtpServer2_Object = MibScalar
cfgNtpServer2 = _CfgNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 14, 3),
    _CfgNtpServer2_Type()
)
cfgNtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNtpServer2.setStatus("current")
_CfgHttp_ObjectIdentity = ObjectIdentity
cfgHttp = _CfgHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 15)
)


class _CfgHttpUser_Type(DisplayString):
    """Custom type cfgHttpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgHttpUser_Type.__name__ = "DisplayString"
_CfgHttpUser_Object = MibScalar
cfgHttpUser = _CfgHttpUser_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 15, 1),
    _CfgHttpUser_Type()
)
cfgHttpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgHttpUser.setStatus("current")


class _CfgHttpPassword_Type(DisplayString):
    """Custom type cfgHttpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 126),
    )


_CfgHttpPassword_Type.__name__ = "DisplayString"
_CfgHttpPassword_Object = MibScalar
cfgHttpPassword = _CfgHttpPassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 15, 2),
    _CfgHttpPassword_Type()
)
cfgHttpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHttpPassword.setStatus("current")


class _CfgHttpEnabled_Type(Integer32):
    """Custom type cfgHttpEnabled based on Integer32"""
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


_CfgHttpEnabled_Type.__name__ = "Integer32"
_CfgHttpEnabled_Object = MibScalar
cfgHttpEnabled = _CfgHttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 15, 3),
    _CfgHttpEnabled_Type()
)
cfgHttpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHttpEnabled.setStatus("current")


class _CfgHttpRedirectEnabled_Type(Integer32):
    """Custom type cfgHttpRedirectEnabled based on Integer32"""
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


_CfgHttpRedirectEnabled_Type.__name__ = "Integer32"
_CfgHttpRedirectEnabled_Object = MibScalar
cfgHttpRedirectEnabled = _CfgHttpRedirectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 15, 4),
    _CfgHttpRedirectEnabled_Type()
)
cfgHttpRedirectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHttpRedirectEnabled.setStatus("current")


class _CfgHttpHttpAddress_Type(DisplayString):
    """Custom type cfgHttpHttpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgHttpHttpAddress_Type.__name__ = "DisplayString"
_CfgHttpHttpAddress_Object = MibScalar
cfgHttpHttpAddress = _CfgHttpHttpAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 15, 5),
    _CfgHttpHttpAddress_Type()
)
cfgHttpHttpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHttpHttpAddress.setStatus("current")


class _CfgHttpHttpsAddress_Type(DisplayString):
    """Custom type cfgHttpHttpsAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgHttpHttpsAddress_Type.__name__ = "DisplayString"
_CfgHttpHttpsAddress_Object = MibScalar
cfgHttpHttpsAddress = _CfgHttpHttpsAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 15, 6),
    _CfgHttpHttpsAddress_Type()
)
cfgHttpHttpsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHttpHttpsAddress.setStatus("current")
_CfgLldp_ObjectIdentity = ObjectIdentity
cfgLldp = _CfgLldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 16)
)


class _CfgLldpEnabled_Type(Integer32):
    """Custom type cfgLldpEnabled based on Integer32"""
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


_CfgLldpEnabled_Type.__name__ = "Integer32"
_CfgLldpEnabled_Object = MibScalar
cfgLldpEnabled = _CfgLldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 16, 1),
    _CfgLldpEnabled_Type()
)
cfgLldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLldpEnabled.setStatus("current")


class _CfgLldpDescription_Type(DisplayString):
    """Custom type cfgLldpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfgLldpDescription_Type.__name__ = "DisplayString"
_CfgLldpDescription_Object = MibScalar
cfgLldpDescription = _CfgLldpDescription_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 16, 2),
    _CfgLldpDescription_Type()
)
cfgLldpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLldpDescription.setStatus("current")
_CfgMdns_ObjectIdentity = ObjectIdentity
cfgMdns = _CfgMdns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 17)
)


class _CfgMdnsEnabled_Type(Integer32):
    """Custom type cfgMdnsEnabled based on Integer32"""
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


_CfgMdnsEnabled_Type.__name__ = "Integer32"
_CfgMdnsEnabled_Object = MibScalar
cfgMdnsEnabled = _CfgMdnsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 17, 1),
    _CfgMdnsEnabled_Type()
)
cfgMdnsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMdnsEnabled.setStatus("current")


class _CfgMdnsNetwork_Type(DisplayString):
    """Custom type cfgMdnsNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgMdnsNetwork_Type.__name__ = "DisplayString"
_CfgMdnsNetwork_Object = MibScalar
cfgMdnsNetwork = _CfgMdnsNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 17, 2),
    _CfgMdnsNetwork_Type()
)
cfgMdnsNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMdnsNetwork.setStatus("current")
_CfgNlm_ObjectIdentity = ObjectIdentity
cfgNlm = _CfgNlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40)
)
_CfgNlmGlobal_ObjectIdentity = ObjectIdentity
cfgNlmGlobal = _CfgNlmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 1)
)


class _CfgNlmGlblEnabled_Type(Integer32):
    """Custom type cfgNlmGlblEnabled based on Integer32"""
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


_CfgNlmGlblEnabled_Type.__name__ = "Integer32"
_CfgNlmGlblEnabled_Object = MibScalar
cfgNlmGlblEnabled = _CfgNlmGlblEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 1, 1),
    _CfgNlmGlblEnabled_Type()
)
cfgNlmGlblEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmGlblEnabled.setStatus("current")
_CfgNlmMonitorTable_Object = MibTable
cfgNlmMonitorTable = _CfgNlmMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2)
)
if mibBuilder.loadTexts:
    cfgNlmMonitorTable.setStatus("current")
_CfgNlmMonitorTableEntry_Object = MibTableRow
cfgNlmMonitorTableEntry = _CfgNlmMonitorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1)
)
cfgNlmMonitorTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgNlmMonIndex"),
)
if mibBuilder.loadTexts:
    cfgNlmMonitorTableEntry.setStatus("current")


class _CfgNlmMonIndex_Type(Integer32):
    """Custom type cfgNlmMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgNlmMonIndex_Type.__name__ = "Integer32"
_CfgNlmMonIndex_Object = MibTableColumn
cfgNlmMonIndex = _CfgNlmMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 1),
    _CfgNlmMonIndex_Type()
)
cfgNlmMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNlmMonIndex.setStatus("current")


class _CfgNlmMonEnabled_Type(Integer32):
    """Custom type cfgNlmMonEnabled based on Integer32"""
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


_CfgNlmMonEnabled_Type.__name__ = "Integer32"
_CfgNlmMonEnabled_Object = MibTableColumn
cfgNlmMonEnabled = _CfgNlmMonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 2),
    _CfgNlmMonEnabled_Type()
)
cfgNlmMonEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonEnabled.setStatus("current")


class _CfgNlmMonInterval_Type(Integer32):
    """Custom type cfgNlmMonInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfgNlmMonInterval_Type.__name__ = "Integer32"
_CfgNlmMonInterval_Object = MibTableColumn
cfgNlmMonInterval = _CfgNlmMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 3),
    _CfgNlmMonInterval_Type()
)
cfgNlmMonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonInterval.setStatus("current")


class _CfgNlmMonCount_Type(Integer32):
    """Custom type cfgNlmMonCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfgNlmMonCount_Type.__name__ = "Integer32"
_CfgNlmMonCount_Object = MibTableColumn
cfgNlmMonCount = _CfgNlmMonCount_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 4),
    _CfgNlmMonCount_Type()
)
cfgNlmMonCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonCount.setStatus("current")


class _CfgNlmMonType_Type(Integer32):
    """Custom type cfgNlmMonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phy", 0),
          ("icmp", 1),
          ("wlan", 2))
    )


_CfgNlmMonType_Type.__name__ = "Integer32"
_CfgNlmMonType_Object = MibTableColumn
cfgNlmMonType = _CfgNlmMonType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 5),
    _CfgNlmMonType_Type()
)
cfgNlmMonType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonType.setStatus("current")


class _CfgNlmMonInterfaces_Type(DisplayString):
    """Custom type cfgNlmMonInterfaces based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgNlmMonInterfaces_Type.__name__ = "DisplayString"
_CfgNlmMonInterfaces_Object = MibTableColumn
cfgNlmMonInterfaces = _CfgNlmMonInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 6),
    _CfgNlmMonInterfaces_Type()
)
cfgNlmMonInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonInterfaces.setStatus("current")
_CfgNlmMonDestination_Type = IpAddress
_CfgNlmMonDestination_Object = MibTableColumn
cfgNlmMonDestination = _CfgNlmMonDestination_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 7),
    _CfgNlmMonDestination_Type()
)
cfgNlmMonDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonDestination.setStatus("current")


class _CfgNlmMonUpAction_Type(Integer32):
    """Custom type cfgNlmMonUpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2255),
    )


_CfgNlmMonUpAction_Type.__name__ = "Integer32"
_CfgNlmMonUpAction_Object = MibTableColumn
cfgNlmMonUpAction = _CfgNlmMonUpAction_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 10),
    _CfgNlmMonUpAction_Type()
)
cfgNlmMonUpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonUpAction.setStatus("current")


class _CfgNlmMonDownAction_Type(Integer32):
    """Custom type cfgNlmMonDownAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2255),
    )


_CfgNlmMonDownAction_Type.__name__ = "Integer32"
_CfgNlmMonDownAction_Object = MibTableColumn
cfgNlmMonDownAction = _CfgNlmMonDownAction_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 11),
    _CfgNlmMonDownAction_Type()
)
cfgNlmMonDownAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonDownAction.setStatus("current")


class _CfgNlmMonScanLoopInterval_Type(Integer32):
    """Custom type cfgNlmMonScanLoopInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfgNlmMonScanLoopInterval_Type.__name__ = "Integer32"
_CfgNlmMonScanLoopInterval_Object = MibTableColumn
cfgNlmMonScanLoopInterval = _CfgNlmMonScanLoopInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 40, 2, 1, 12),
    _CfgNlmMonScanLoopInterval_Type()
)
cfgNlmMonScanLoopInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNlmMonScanLoopInterval.setStatus("current")
_CfgCli_ObjectIdentity = ObjectIdentity
cfgCli = _CfgCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100)
)


class _CfgCliEnabled_Type(Integer32):
    """Custom type cfgCliEnabled based on Integer32"""
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


_CfgCliEnabled_Type.__name__ = "Integer32"
_CfgCliEnabled_Object = MibScalar
cfgCliEnabled = _CfgCliEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100, 1),
    _CfgCliEnabled_Type()
)
cfgCliEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCliEnabled.setStatus("current")


class _CfgCliUsername_Type(DisplayString):
    """Custom type cfgCliUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CfgCliUsername_Type.__name__ = "DisplayString"
_CfgCliUsername_Object = MibScalar
cfgCliUsername = _CfgCliUsername_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100, 2),
    _CfgCliUsername_Type()
)
cfgCliUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCliUsername.setStatus("current")


class _CfgCliPassword_Type(DisplayString):
    """Custom type cfgCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CfgCliPassword_Type.__name__ = "DisplayString"
_CfgCliPassword_Object = MibScalar
cfgCliPassword = _CfgCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100, 3),
    _CfgCliPassword_Type()
)
cfgCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCliPassword.setStatus("current")


class _CfgCliTelnetEnabled_Type(Integer32):
    """Custom type cfgCliTelnetEnabled based on Integer32"""
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


_CfgCliTelnetEnabled_Type.__name__ = "Integer32"
_CfgCliTelnetEnabled_Object = MibScalar
cfgCliTelnetEnabled = _CfgCliTelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100, 4),
    _CfgCliTelnetEnabled_Type()
)
cfgCliTelnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCliTelnetEnabled.setStatus("current")


class _CfgCliSshEnabled_Type(Integer32):
    """Custom type cfgCliSshEnabled based on Integer32"""
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


_CfgCliSshEnabled_Type.__name__ = "Integer32"
_CfgCliSshEnabled_Object = MibScalar
cfgCliSshEnabled = _CfgCliSshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100, 6),
    _CfgCliSshEnabled_Type()
)
cfgCliSshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCliSshEnabled.setStatus("current")


class _CfgCliTelnetAddress_Type(DisplayString):
    """Custom type cfgCliTelnetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgCliTelnetAddress_Type.__name__ = "DisplayString"
_CfgCliTelnetAddress_Object = MibScalar
cfgCliTelnetAddress = _CfgCliTelnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100, 8),
    _CfgCliTelnetAddress_Type()
)
cfgCliTelnetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCliTelnetAddress.setStatus("current")


class _CfgCliSshAddress_Type(DisplayString):
    """Custom type cfgCliSshAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgCliSshAddress_Type.__name__ = "DisplayString"
_CfgCliSshAddress_Object = MibScalar
cfgCliSshAddress = _CfgCliSshAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 100, 9),
    _CfgCliSshAddress_Type()
)
cfgCliSshAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCliSshAddress.setStatus("current")
_CfgCellular_ObjectIdentity = ObjectIdentity
cfgCellular = _CfgCellular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101)
)
_CfgCellSimTable_Object = MibTable
cfgCellSimTable = _CfgCellSimTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1)
)
if mibBuilder.loadTexts:
    cfgCellSimTable.setStatus("current")
_CfgCellSimTableEntry_Object = MibTableRow
cfgCellSimTableEntry = _CfgCellSimTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1)
)
cfgCellSimTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "cfgCellSimIndex"),
)
if mibBuilder.loadTexts:
    cfgCellSimTableEntry.setStatus("current")


class _CfgCellSimIndex_Type(Integer32):
    """Custom type cfgCellSimIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CfgCellSimIndex_Type.__name__ = "Integer32"
_CfgCellSimIndex_Object = MibTableColumn
cfgCellSimIndex = _CfgCellSimIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1, 1),
    _CfgCellSimIndex_Type()
)
cfgCellSimIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgCellSimIndex.setStatus("current")


class _CfgCellSimApn_Type(DisplayString):
    """Custom type cfgCellSimApn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgCellSimApn_Type.__name__ = "DisplayString"
_CfgCellSimApn_Object = MibTableColumn
cfgCellSimApn = _CfgCellSimApn_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1, 2),
    _CfgCellSimApn_Type()
)
cfgCellSimApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCellSimApn.setStatus("current")


class _CfgCellSimUsername_Type(DisplayString):
    """Custom type cfgCellSimUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgCellSimUsername_Type.__name__ = "DisplayString"
_CfgCellSimUsername_Object = MibTableColumn
cfgCellSimUsername = _CfgCellSimUsername_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1, 3),
    _CfgCellSimUsername_Type()
)
cfgCellSimUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCellSimUsername.setStatus("current")


class _CfgCellSimPassword_Type(DisplayString):
    """Custom type cfgCellSimPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgCellSimPassword_Type.__name__ = "DisplayString"
_CfgCellSimPassword_Object = MibTableColumn
cfgCellSimPassword = _CfgCellSimPassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1, 4),
    _CfgCellSimPassword_Type()
)
cfgCellSimPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCellSimPassword.setStatus("current")


class _CfgCellSimPinEnabled_Type(Integer32):
    """Custom type cfgCellSimPinEnabled based on Integer32"""
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


_CfgCellSimPinEnabled_Type.__name__ = "Integer32"
_CfgCellSimPinEnabled_Object = MibTableColumn
cfgCellSimPinEnabled = _CfgCellSimPinEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1, 5),
    _CfgCellSimPinEnabled_Type()
)
cfgCellSimPinEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCellSimPinEnabled.setStatus("current")


class _CfgCellSimPin_Type(DisplayString):
    """Custom type cfgCellSimPin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_CfgCellSimPin_Type.__name__ = "DisplayString"
_CfgCellSimPin_Object = MibTableColumn
cfgCellSimPin = _CfgCellSimPin_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1, 6),
    _CfgCellSimPin_Type()
)
cfgCellSimPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCellSimPin.setStatus("current")


class _CfgCellSimAuthType_Type(Integer32):
    """Custom type cfgCellSimAuthType based on Integer32"""
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
          ("pap", 1),
          ("chap", 2),
          ("both", 3))
    )


_CfgCellSimAuthType_Type.__name__ = "Integer32"
_CfgCellSimAuthType_Object = MibTableColumn
cfgCellSimAuthType = _CfgCellSimAuthType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 1, 101, 1, 1, 7),
    _CfgCellSimAuthType_Type()
)
cfgCellSimAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCellSimAuthType.setStatus("current")
_Rpc_ObjectIdentity = ObjectIdentity
rpc = _Rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3)
)
_RpcConfiguration_ObjectIdentity = ObjectIdentity
rpcConfiguration = _RpcConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 1)
)


class _RpcCfgRevert_Type(Integer32):
    """Custom type rpcCfgRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allError", -1),
          ("nop", 0),
          ("all", 1))
    )


_RpcCfgRevert_Type.__name__ = "Integer32"
_RpcCfgRevert_Object = MibScalar
rpcCfgRevert = _RpcCfgRevert_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 1, 1),
    _RpcCfgRevert_Type()
)
rpcCfgRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcCfgRevert.setStatus("current")


class _RpcCfgApply_Type(Integer32):
    """Custom type rpcCfgApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allError", -1),
          ("nop", 0),
          ("all", 1))
    )


_RpcCfgApply_Type.__name__ = "Integer32"
_RpcCfgApply_Object = MibScalar
rpcCfgApply = _RpcCfgApply_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 1, 2),
    _RpcCfgApply_Type()
)
rpcCfgApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcCfgApply.setStatus("current")


class _RpcCfgFile_Type(Integer32):
    """Custom type rpcCfgFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("errorImport", -2),
          ("errorExport", -1),
          ("nop", 0),
          ("export", 1),
          ("import", 2))
    )


_RpcCfgFile_Type.__name__ = "Integer32"
_RpcCfgFile_Object = MibScalar
rpcCfgFile = _RpcCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 1, 4),
    _RpcCfgFile_Type()
)
rpcCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcCfgFile.setStatus("current")
_RpcFirmware_ObjectIdentity = ObjectIdentity
rpcFirmware = _RpcFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 2)
)


class _RpcFwFlash_Type(Integer32):
    """Custom type rpcFwFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flashError", -2),
          ("downloadError", -1),
          ("nop", 0),
          ("download", 1),
          ("flash", 2),
          ("flashWithConfig", 3))
    )


_RpcFwFlash_Type.__name__ = "Integer32"
_RpcFwFlash_Object = MibScalar
rpcFwFlash = _RpcFwFlash_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 2, 1),
    _RpcFwFlash_Type()
)
rpcFwFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcFwFlash.setStatus("current")
_RpcSystem_ObjectIdentity = ObjectIdentity
rpcSystem = _RpcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 3)
)
_RpcSysReboot_Type = Integer32
_RpcSysReboot_Object = MibScalar
rpcSysReboot = _RpcSysReboot_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 3, 1),
    _RpcSysReboot_Type()
)
rpcSysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcSysReboot.setStatus("current")


class _RpcSysFactoryReset_Type(Integer32):
    """Custom type rpcSysFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("reset", 1))
    )


_RpcSysFactoryReset_Type.__name__ = "Integer32"
_RpcSysFactoryReset_Object = MibScalar
rpcSysFactoryReset = _RpcSysFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 3, 2),
    _RpcSysFactoryReset_Type()
)
rpcSysFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcSysFactoryReset.setStatus("current")


class _RpcSysErrorReset_Type(Integer32):
    """Custom type rpcSysErrorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("reset", 1))
    )


_RpcSysErrorReset_Type.__name__ = "Integer32"
_RpcSysErrorReset_Object = MibScalar
rpcSysErrorReset = _RpcSysErrorReset_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 3, 3),
    _RpcSysErrorReset_Type()
)
rpcSysErrorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcSysErrorReset.setStatus("current")


class _RpcSysKernelLogReset_Type(Integer32):
    """Custom type rpcSysKernelLogReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("reset", 1))
    )


_RpcSysKernelLogReset_Type.__name__ = "Integer32"
_RpcSysKernelLogReset_Object = MibScalar
rpcSysKernelLogReset = _RpcSysKernelLogReset_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 3, 4),
    _RpcSysKernelLogReset_Type()
)
rpcSysKernelLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcSysKernelLogReset.setStatus("current")
_RpcCertificate_ObjectIdentity = ObjectIdentity
rpcCertificate = _RpcCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 4)
)


class _RpcCrtFile_Type(Integer32):
    """Custom type rpcCrtFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-4,
              -3,
              -2,
              -1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("validateerror", -4),
          ("deleteerror", -3),
          ("exporterror", -2),
          ("importerror", -1),
          ("nop", 0),
          ("import", 1),
          ("export", 2),
          ("delete", 3))
    )


_RpcCrtFile_Type.__name__ = "Integer32"
_RpcCrtFile_Object = MibScalar
rpcCrtFile = _RpcCrtFile_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 4, 1),
    _RpcCrtFile_Type()
)
rpcCrtFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcCrtFile.setStatus("current")
_RpcDriver_ObjectIdentity = ObjectIdentity
rpcDriver = _RpcDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 6)
)
_RpcDrvTable_Object = MibTable
rpcDrvTable = _RpcDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    rpcDrvTable.setStatus("current")
_RpcDrvTableEntry_Object = MibTableRow
rpcDrvTableEntry = _RpcDrvTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 6, 1, 1)
)
rpcDrvTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "rpcDrvIndex"),
)
if mibBuilder.loadTexts:
    rpcDrvTableEntry.setStatus("current")


class _RpcDrvIndex_Type(Integer32):
    """Custom type rpcDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RpcDrvIndex_Type.__name__ = "Integer32"
_RpcDrvIndex_Object = MibTableColumn
rpcDrvIndex = _RpcDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 6, 1, 1, 1),
    _RpcDrvIndex_Type()
)
rpcDrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpcDrvIndex.setStatus("current")


class _RpcDrvName_Type(DisplayString):
    """Custom type rpcDrvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RpcDrvName_Type.__name__ = "DisplayString"
_RpcDrvName_Object = MibTableColumn
rpcDrvName = _RpcDrvName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 6, 1, 1, 2),
    _RpcDrvName_Type()
)
rpcDrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcDrvName.setStatus("current")


class _RpcDrvDfsSimulateRadar_Type(Integer32):
    """Custom type rpcDrvDfsSimulateRadar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("fire", 1))
    )


_RpcDrvDfsSimulateRadar_Type.__name__ = "Integer32"
_RpcDrvDfsSimulateRadar_Object = MibTableColumn
rpcDrvDfsSimulateRadar = _RpcDrvDfsSimulateRadar_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 3, 6, 1, 1, 5),
    _RpcDrvDfsSimulateRadar_Type()
)
rpcDrvDfsSimulateRadar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcDrvDfsSimulateRadar.setStatus("current")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4)
)
_SetConfiguration_ObjectIdentity = ObjectIdentity
setConfiguration = _SetConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 1)
)


class _SetCfgFileUrl_Type(DisplayString):
    """Custom type setCfgFileUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SetCfgFileUrl_Type.__name__ = "DisplayString"
_SetCfgFileUrl_Object = MibScalar
setCfgFileUrl = _SetCfgFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 1, 1),
    _SetCfgFileUrl_Type()
)
setCfgFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCfgFileUrl.setStatus("current")
_SetWireless_ObjectIdentity = ObjectIdentity
setWireless = _SetWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3)
)
_SetWlanDeviceTable_Object = MibTable
setWlanDeviceTable = _SetWlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    setWlanDeviceTable.setStatus("current")
_SetWlanDeviceTableEntry_Object = MibTableRow
setWlanDeviceTableEntry = _SetWlanDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 1, 1)
)
setWlanDeviceTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "setWlanDevIndex"),
)
if mibBuilder.loadTexts:
    setWlanDeviceTableEntry.setStatus("current")


class _SetWlanDevIndex_Type(Integer32):
    """Custom type setWlanDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SetWlanDevIndex_Type.__name__ = "Integer32"
_SetWlanDevIndex_Object = MibTableColumn
setWlanDevIndex = _SetWlanDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 1, 1, 1),
    _SetWlanDevIndex_Type()
)
setWlanDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setWlanDevIndex.setStatus("current")


class _SetWlanDevName_Type(DisplayString):
    """Custom type setWlanDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SetWlanDevName_Type.__name__ = "DisplayString"
_SetWlanDevName_Object = MibTableColumn
setWlanDevName = _SetWlanDevName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 1, 1, 2),
    _SetWlanDevName_Type()
)
setWlanDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setWlanDevName.setStatus("current")


class _SetWlanDevRfOutput_Type(Integer32):
    """Custom type setWlanDevRfOutput based on Integer32"""
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


_SetWlanDevRfOutput_Type.__name__ = "Integer32"
_SetWlanDevRfOutput_Object = MibTableColumn
setWlanDevRfOutput = _SetWlanDevRfOutput_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 1, 1, 3),
    _SetWlanDevRfOutput_Type()
)
setWlanDevRfOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDevRfOutput.setStatus("current")
_SetWlanDevFrequency_Type = Integer32
_SetWlanDevFrequency_Object = MibTableColumn
setWlanDevFrequency = _SetWlanDevFrequency_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 1, 1, 6),
    _SetWlanDevFrequency_Type()
)
setWlanDevFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDevFrequency.setStatus("current")
_SetWlanDevPower_Type = Integer32
_SetWlanDevPower_Object = MibTableColumn
setWlanDevPower = _SetWlanDevPower_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 1, 1, 8),
    _SetWlanDevPower_Type()
)
setWlanDevPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDevPower.setStatus("current")
_SetWlanDbgTable_Object = MibTable
setWlanDbgTable = _SetWlanDbgTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6)
)
if mibBuilder.loadTexts:
    setWlanDbgTable.setStatus("current")
_SetWlanDbgTableEntry_Object = MibTableRow
setWlanDbgTableEntry = _SetWlanDbgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1)
)
setWlanDbgTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "setWlanDbgIndex"),
)
if mibBuilder.loadTexts:
    setWlanDbgTableEntry.setStatus("current")


class _SetWlanDbgIndex_Type(Integer32):
    """Custom type setWlanDbgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SetWlanDbgIndex_Type.__name__ = "Integer32"
_SetWlanDbgIndex_Object = MibTableColumn
setWlanDbgIndex = _SetWlanDbgIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 1),
    _SetWlanDbgIndex_Type()
)
setWlanDbgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setWlanDbgIndex.setStatus("current")


class _SetWlanDbgIfaceName_Type(DisplayString):
    """Custom type setWlanDbgIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SetWlanDbgIfaceName_Type.__name__ = "DisplayString"
_SetWlanDbgIfaceName_Object = MibTableColumn
setWlanDbgIfaceName = _SetWlanDbgIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 2),
    _SetWlanDbgIfaceName_Type()
)
setWlanDbgIfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setWlanDbgIfaceName.setStatus("current")


class _SetWlanDbgHandoff_Type(Integer32):
    """Custom type setWlanDbgHandoff based on Integer32"""
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


_SetWlanDbgHandoff_Type.__name__ = "Integer32"
_SetWlanDbgHandoff_Object = MibTableColumn
setWlanDbgHandoff = _SetWlanDbgHandoff_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 3),
    _SetWlanDbgHandoff_Type()
)
setWlanDbgHandoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgHandoff.setStatus("current")


class _SetWlanDbgScan_Type(Integer32):
    """Custom type setWlanDbgScan based on Integer32"""
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


_SetWlanDbgScan_Type.__name__ = "Integer32"
_SetWlanDbgScan_Object = MibTableColumn
setWlanDbgScan = _SetWlanDbgScan_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 4),
    _SetWlanDbgScan_Type()
)
setWlanDbgScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgScan.setStatus("current")


class _SetWlanDbgMlme_Type(Integer32):
    """Custom type setWlanDbgMlme based on Integer32"""
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


_SetWlanDbgMlme_Type.__name__ = "Integer32"
_SetWlanDbgMlme_Object = MibTableColumn
setWlanDbgMlme = _SetWlanDbgMlme_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 5),
    _SetWlanDbgMlme_Type()
)
setWlanDbgMlme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgMlme.setStatus("current")


class _SetWlanDbgEvents_Type(Integer32):
    """Custom type setWlanDbgEvents based on Integer32"""
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


_SetWlanDbgEvents_Type.__name__ = "Integer32"
_SetWlanDbgEvents_Object = MibTableColumn
setWlanDbgEvents = _SetWlanDbgEvents_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 6),
    _SetWlanDbgEvents_Type()
)
setWlanDbgEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgEvents.setStatus("current")


class _SetWlanDbgBeaconrssi_Type(Integer32):
    """Custom type setWlanDbgBeaconrssi based on Integer32"""
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


_SetWlanDbgBeaconrssi_Type.__name__ = "Integer32"
_SetWlanDbgBeaconrssi_Object = MibTableColumn
setWlanDbgBeaconrssi = _SetWlanDbgBeaconrssi_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 7),
    _SetWlanDbgBeaconrssi_Type()
)
setWlanDbgBeaconrssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgBeaconrssi.setStatus("current")


class _SetWlanDbgAckrssi_Type(Integer32):
    """Custom type setWlanDbgAckrssi based on Integer32"""
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


_SetWlanDbgAckrssi_Type.__name__ = "Integer32"
_SetWlanDbgAckrssi_Object = MibTableColumn
setWlanDbgAckrssi = _SetWlanDbgAckrssi_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 8),
    _SetWlanDbgAckrssi_Type()
)
setWlanDbgAckrssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgAckrssi.setStatus("current")


class _SetWlanDbgBeaconfiltered_Type(Integer32):
    """Custom type setWlanDbgBeaconfiltered based on Integer32"""
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


_SetWlanDbgBeaconfiltered_Type.__name__ = "Integer32"
_SetWlanDbgBeaconfiltered_Object = MibTableColumn
setWlanDbgBeaconfiltered = _SetWlanDbgBeaconfiltered_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 9),
    _SetWlanDbgBeaconfiltered_Type()
)
setWlanDbgBeaconfiltered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgBeaconfiltered.setStatus("current")


class _SetWlanDbgRatelimit_Type(Integer32):
    """Custom type setWlanDbgRatelimit based on Integer32"""
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


_SetWlanDbgRatelimit_Type.__name__ = "Integer32"
_SetWlanDbgRatelimit_Object = MibTableColumn
setWlanDbgRatelimit = _SetWlanDbgRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 10),
    _SetWlanDbgRatelimit_Type()
)
setWlanDbgRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgRatelimit.setStatus("current")


class _SetWlanDbgBeacontsf_Type(Integer32):
    """Custom type setWlanDbgBeacontsf based on Integer32"""
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


_SetWlanDbgBeacontsf_Type.__name__ = "Integer32"
_SetWlanDbgBeacontsf_Object = MibTableColumn
setWlanDbgBeacontsf = _SetWlanDbgBeacontsf_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 12),
    _SetWlanDbgBeacontsf_Type()
)
setWlanDbgBeacontsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgBeacontsf.setStatus("current")


class _SetWlanDbgRange_Type(Integer32):
    """Custom type setWlanDbgRange based on Integer32"""
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


_SetWlanDbgRange_Type.__name__ = "Integer32"
_SetWlanDbgRange_Object = MibTableColumn
setWlanDbgRange = _SetWlanDbgRange_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 13),
    _SetWlanDbgRange_Type()
)
setWlanDbgRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgRange.setStatus("current")


class _SetWlanDbgReports_Type(Integer32):
    """Custom type setWlanDbgReports based on Integer32"""
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


_SetWlanDbgReports_Type.__name__ = "Integer32"
_SetWlanDbgReports_Object = MibTableColumn
setWlanDbgReports = _SetWlanDbgReports_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 3, 6, 1, 14),
    _SetWlanDbgReports_Type()
)
setWlanDbgReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWlanDbgReports.setStatus("current")
_SetConfmgmtd_ObjectIdentity = ObjectIdentity
setConfmgmtd = _SetConfmgmtd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 4)
)
_SetCfgdLogLevel_Type = Integer32
_SetCfgdLogLevel_Object = MibScalar
setCfgdLogLevel = _SetCfgdLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 4, 1),
    _SetCfgdLogLevel_Type()
)
setCfgdLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCfgdLogLevel.setStatus("current")
_SetFirmware_ObjectIdentity = ObjectIdentity
setFirmware = _SetFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 5)
)


class _SetFwFileUrl_Type(DisplayString):
    """Custom type setFwFileUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SetFwFileUrl_Type.__name__ = "DisplayString"
_SetFwFileUrl_Object = MibScalar
setFwFileUrl = _SetFwFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 5, 1),
    _SetFwFileUrl_Type()
)
setFwFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setFwFileUrl.setStatus("current")


class _SetFwKeepConfig_Type(Integer32):
    """Custom type setFwKeepConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reset", 0),
          ("keep", 1))
    )


_SetFwKeepConfig_Type.__name__ = "Integer32"
_SetFwKeepConfig_Object = MibScalar
setFwKeepConfig = _SetFwKeepConfig_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 5, 2),
    _SetFwKeepConfig_Type()
)
setFwKeepConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setFwKeepConfig.setStatus("current")
_SetCertificate_ObjectIdentity = ObjectIdentity
setCertificate = _SetCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 6)
)


class _SetCrtFileUrl_Type(DisplayString):
    """Custom type setCrtFileUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SetCrtFileUrl_Type.__name__ = "DisplayString"
_SetCrtFileUrl_Object = MibScalar
setCrtFileUrl = _SetCrtFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 6, 1),
    _SetCrtFileUrl_Type()
)
setCrtFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCrtFileUrl.setStatus("current")


class _SetCrtFileSelector_Type(Integer32):
    """Custom type setCrtFileSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10715),
    )


_SetCrtFileSelector_Type.__name__ = "Integer32"
_SetCrtFileSelector_Object = MibScalar
setCrtFileSelector = _SetCrtFileSelector_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 6, 2),
    _SetCrtFileSelector_Type()
)
setCrtFileSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCrtFileSelector.setStatus("current")


class _SetCrtFileFormat_Type(Integer32):
    """Custom type setCrtFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pem", 0),
          ("der", 1))
    )


_SetCrtFileFormat_Type.__name__ = "Integer32"
_SetCrtFileFormat_Object = MibScalar
setCrtFileFormat = _SetCrtFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 6, 3),
    _SetCrtFileFormat_Type()
)
setCrtFileFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCrtFileFormat.setStatus("current")


class _SetCrtFilePkcs12Passphrase_Type(DisplayString):
    """Custom type setCrtFilePkcs12Passphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SetCrtFilePkcs12Passphrase_Type.__name__ = "DisplayString"
_SetCrtFilePkcs12Passphrase_Object = MibScalar
setCrtFilePkcs12Passphrase = _SetCrtFilePkcs12Passphrase_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 6, 4),
    _SetCrtFilePkcs12Passphrase_Type()
)
setCrtFilePkcs12Passphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCrtFilePkcs12Passphrase.setStatus("current")
_SetSystem_ObjectIdentity = ObjectIdentity
setSystem = _SetSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 7)
)
_SetSysTime_Type = Integer32
_SetSysTime_Object = MibScalar
setSysTime = _SetSysTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 4, 7, 1),
    _SetSysTime_Type()
)
setSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSysTime.setStatus("current")
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5)
)
_HwSystem_ObjectIdentity = ObjectIdentity
hwSystem = _HwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 1)
)


class _HwSysProduct_Type(DisplayString):
    """Custom type hwSysProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSysProduct_Type.__name__ = "DisplayString"
_HwSysProduct_Object = MibScalar
hwSysProduct = _HwSysProduct_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 1, 1),
    _HwSysProduct_Type()
)
hwSysProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysProduct.setStatus("current")


class _HwSysSerial_Type(DisplayString):
    """Custom type hwSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSysSerial_Type.__name__ = "DisplayString"
_HwSysSerial_Object = MibScalar
hwSysSerial = _HwSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 1, 2),
    _HwSysSerial_Type()
)
hwSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysSerial.setStatus("current")
_HwSysRevision_Type = Integer32
_HwSysRevision_Object = MibScalar
hwSysRevision = _HwSysRevision_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 1, 3),
    _HwSysRevision_Type()
)
hwSysRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysRevision.setStatus("current")
_HwSysVersion_Type = Integer32
_HwSysVersion_Object = MibScalar
hwSysVersion = _HwSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 1, 4),
    _HwSysVersion_Type()
)
hwSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysVersion.setStatus("current")
_HwNetwork_ObjectIdentity = ObjectIdentity
hwNetwork = _HwNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2)
)
_HwNetEthernetTable_Object = MibTable
hwNetEthernetTable = _HwNetEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hwNetEthernetTable.setStatus("current")
_HwNetEthernetTableEntry_Object = MibTableRow
hwNetEthernetTableEntry = _HwNetEthernetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1)
)
hwNetEthernetTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "hwNetEthIndex"),
)
if mibBuilder.loadTexts:
    hwNetEthernetTableEntry.setStatus("current")


class _HwNetEthIndex_Type(Integer32):
    """Custom type hwNetEthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwNetEthIndex_Type.__name__ = "Integer32"
_HwNetEthIndex_Object = MibTableColumn
hwNetEthIndex = _HwNetEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1, 1),
    _HwNetEthIndex_Type()
)
hwNetEthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNetEthIndex.setStatus("current")


class _HwNetEthName_Type(DisplayString):
    """Custom type hwNetEthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNetEthName_Type.__name__ = "DisplayString"
_HwNetEthName_Object = MibTableColumn
hwNetEthName = _HwNetEthName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1, 2),
    _HwNetEthName_Type()
)
hwNetEthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetEthName.setStatus("current")


class _HwNetEthAssembled_Type(Integer32):
    """Custom type hwNetEthAssembled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inexistent", 0),
          ("present", 1))
    )


_HwNetEthAssembled_Type.__name__ = "Integer32"
_HwNetEthAssembled_Object = MibTableColumn
hwNetEthAssembled = _HwNetEthAssembled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1, 3),
    _HwNetEthAssembled_Type()
)
hwNetEthAssembled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetEthAssembled.setStatus("current")


class _HwNetEthMacAddress_Type(DisplayString):
    """Custom type hwNetEthMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNetEthMacAddress_Type.__name__ = "DisplayString"
_HwNetEthMacAddress_Object = MibTableColumn
hwNetEthMacAddress = _HwNetEthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1, 4),
    _HwNetEthMacAddress_Type()
)
hwNetEthMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetEthMacAddress.setStatus("current")


class _HwNetEthOperation_Type(Integer32):
    """Custom type hwNetEthOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwNetEthOperation_Type.__name__ = "Integer32"
_HwNetEthOperation_Object = MibTableColumn
hwNetEthOperation = _HwNetEthOperation_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1, 5),
    _HwNetEthOperation_Type()
)
hwNetEthOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetEthOperation.setStatus("current")
_HwNetEthSpeed_Type = Integer32
_HwNetEthSpeed_Object = MibTableColumn
hwNetEthSpeed = _HwNetEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1, 6),
    _HwNetEthSpeed_Type()
)
hwNetEthSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetEthSpeed.setStatus("current")
_HwNetEthHwIndex_Type = Integer32
_HwNetEthHwIndex_Object = MibTableColumn
hwNetEthHwIndex = _HwNetEthHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 2, 1, 1, 7),
    _HwNetEthHwIndex_Type()
)
hwNetEthHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetEthHwIndex.setStatus("current")
_HwWireless_ObjectIdentity = ObjectIdentity
hwWireless = _HwWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3)
)
_HwWlanDeviceTable_Object = MibTable
hwWlanDeviceTable = _HwWlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hwWlanDeviceTable.setStatus("current")
_HwWlanDeviceTableEntry_Object = MibTableRow
hwWlanDeviceTableEntry = _HwWlanDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1)
)
hwWlanDeviceTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "hwWlanDevIndex"),
)
if mibBuilder.loadTexts:
    hwWlanDeviceTableEntry.setStatus("current")


class _HwWlanDevIndex_Type(Integer32):
    """Custom type hwWlanDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwWlanDevIndex_Type.__name__ = "Integer32"
_HwWlanDevIndex_Object = MibTableColumn
hwWlanDevIndex = _HwWlanDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 1),
    _HwWlanDevIndex_Type()
)
hwWlanDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanDevIndex.setStatus("current")


class _HwWlanDevAssembled_Type(Integer32):
    """Custom type hwWlanDevAssembled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inexistent", 0),
          ("present", 1))
    )


_HwWlanDevAssembled_Type.__name__ = "Integer32"
_HwWlanDevAssembled_Object = MibTableColumn
hwWlanDevAssembled = _HwWlanDevAssembled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 2),
    _HwWlanDevAssembled_Type()
)
hwWlanDevAssembled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevAssembled.setStatus("current")


class _HwWlanDevType_Type(DisplayString):
    """Custom type hwWlanDevType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwWlanDevType_Type.__name__ = "DisplayString"
_HwWlanDevType_Object = MibTableColumn
hwWlanDevType = _HwWlanDevType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 3),
    _HwWlanDevType_Type()
)
hwWlanDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevType.setStatus("current")


class _HwWlanDevSerial_Type(DisplayString):
    """Custom type hwWlanDevSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwWlanDevSerial_Type.__name__ = "DisplayString"
_HwWlanDevSerial_Object = MibTableColumn
hwWlanDevSerial = _HwWlanDevSerial_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 4),
    _HwWlanDevSerial_Type()
)
hwWlanDevSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevSerial.setStatus("current")
_HwWlanDevRevision_Type = Integer32
_HwWlanDevRevision_Object = MibTableColumn
hwWlanDevRevision = _HwWlanDevRevision_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 5),
    _HwWlanDevRevision_Type()
)
hwWlanDevRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevRevision.setStatus("current")
_HwWlanDevVersion_Type = Integer32
_HwWlanDevVersion_Object = MibTableColumn
hwWlanDevVersion = _HwWlanDevVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 6),
    _HwWlanDevVersion_Type()
)
hwWlanDevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevVersion.setStatus("current")
_HwWlanDevPcbId_Type = Integer32
_HwWlanDevPcbId_Object = MibTableColumn
hwWlanDevPcbId = _HwWlanDevPcbId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 7),
    _HwWlanDevPcbId_Type()
)
hwWlanDevPcbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevPcbId.setStatus("current")
_HwWlanDevAssemblyId_Type = Integer32
_HwWlanDevAssemblyId_Object = MibTableColumn
hwWlanDevAssemblyId = _HwWlanDevAssemblyId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 8),
    _HwWlanDevAssemblyId_Type()
)
hwWlanDevAssemblyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevAssemblyId.setStatus("current")


class _HwWlanDevMacAddress_Type(DisplayString):
    """Custom type hwWlanDevMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwWlanDevMacAddress_Type.__name__ = "DisplayString"
_HwWlanDevMacAddress_Object = MibTableColumn
hwWlanDevMacAddress = _HwWlanDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 9),
    _HwWlanDevMacAddress_Type()
)
hwWlanDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevMacAddress.setStatus("current")
_HwWlanDevAntennaProfileId_Type = Integer32
_HwWlanDevAntennaProfileId_Object = MibTableColumn
hwWlanDevAntennaProfileId = _HwWlanDevAntennaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 10),
    _HwWlanDevAntennaProfileId_Type()
)
hwWlanDevAntennaProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevAntennaProfileId.setStatus("current")
_HwWlanDevAntennaGain_Type = Integer32
_HwWlanDevAntennaGain_Object = MibTableColumn
hwWlanDevAntennaGain = _HwWlanDevAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 11),
    _HwWlanDevAntennaGain_Type()
)
hwWlanDevAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevAntennaGain.setStatus("current")
_HwWlanDevCableLoss_Type = Integer32
_HwWlanDevCableLoss_Object = MibTableColumn
hwWlanDevCableLoss = _HwWlanDevCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 1, 1, 12),
    _HwWlanDevCableLoss_Type()
)
hwWlanDevCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanDevCableLoss.setStatus("current")
_HwWlanGlobal_ObjectIdentity = ObjectIdentity
hwWlanGlobal = _HwWlanGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 2)
)


class _HwWlanGlblRegulatoryRegionId_Type(DisplayString):
    """Custom type hwWlanGlblRegulatoryRegionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwWlanGlblRegulatoryRegionId_Type.__name__ = "DisplayString"
_HwWlanGlblRegulatoryRegionId_Object = MibScalar
hwWlanGlblRegulatoryRegionId = _HwWlanGlblRegulatoryRegionId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 3, 2, 2),
    _HwWlanGlblRegulatoryRegionId_Type()
)
hwWlanGlblRegulatoryRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanGlblRegulatoryRegionId.setStatus("current")
_HwBaseBoard_ObjectIdentity = ObjectIdentity
hwBaseBoard = _HwBaseBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 10)
)


class _HwBbType_Type(DisplayString):
    """Custom type hwBbType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwBbType_Type.__name__ = "DisplayString"
_HwBbType_Object = MibScalar
hwBbType = _HwBbType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 10, 1),
    _HwBbType_Type()
)
hwBbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBbType.setStatus("current")


class _HwBbSerial_Type(DisplayString):
    """Custom type hwBbSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwBbSerial_Type.__name__ = "DisplayString"
_HwBbSerial_Object = MibScalar
hwBbSerial = _HwBbSerial_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 10, 2),
    _HwBbSerial_Type()
)
hwBbSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBbSerial.setStatus("current")
_HwBbRevision_Type = Integer32
_HwBbRevision_Object = MibScalar
hwBbRevision = _HwBbRevision_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 10, 3),
    _HwBbRevision_Type()
)
hwBbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBbRevision.setStatus("current")
_HwBbVersion_Type = Integer32
_HwBbVersion_Object = MibScalar
hwBbVersion = _HwBbVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 10, 4),
    _HwBbVersion_Type()
)
hwBbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBbVersion.setStatus("current")
_HwBbPcbId_Type = Integer32
_HwBbPcbId_Object = MibScalar
hwBbPcbId = _HwBbPcbId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 10, 5),
    _HwBbPcbId_Type()
)
hwBbPcbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBbPcbId.setStatus("current")
_HwBbAssemblyId_Type = Integer32
_HwBbAssemblyId_Object = MibScalar
hwBbAssemblyId = _HwBbAssemblyId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 10, 6),
    _HwBbAssemblyId_Type()
)
hwBbAssemblyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBbAssemblyId.setStatus("current")
_HwIfaceBoard_ObjectIdentity = ObjectIdentity
hwIfaceBoard = _HwIfaceBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11)
)


class _HwIfBrdAssembled_Type(Integer32):
    """Custom type hwIfBrdAssembled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inexistent", 0),
          ("present", 1))
    )


_HwIfBrdAssembled_Type.__name__ = "Integer32"
_HwIfBrdAssembled_Object = MibScalar
hwIfBrdAssembled = _HwIfBrdAssembled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11, 1),
    _HwIfBrdAssembled_Type()
)
hwIfBrdAssembled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfBrdAssembled.setStatus("current")


class _HwIfBrdType_Type(DisplayString):
    """Custom type hwIfBrdType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIfBrdType_Type.__name__ = "DisplayString"
_HwIfBrdType_Object = MibScalar
hwIfBrdType = _HwIfBrdType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11, 2),
    _HwIfBrdType_Type()
)
hwIfBrdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfBrdType.setStatus("current")


class _HwIfBrdSerial_Type(DisplayString):
    """Custom type hwIfBrdSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIfBrdSerial_Type.__name__ = "DisplayString"
_HwIfBrdSerial_Object = MibScalar
hwIfBrdSerial = _HwIfBrdSerial_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11, 3),
    _HwIfBrdSerial_Type()
)
hwIfBrdSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfBrdSerial.setStatus("current")
_HwIfBrdRevision_Type = Integer32
_HwIfBrdRevision_Object = MibScalar
hwIfBrdRevision = _HwIfBrdRevision_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11, 4),
    _HwIfBrdRevision_Type()
)
hwIfBrdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfBrdRevision.setStatus("current")
_HwIfBrdVersion_Type = Integer32
_HwIfBrdVersion_Object = MibScalar
hwIfBrdVersion = _HwIfBrdVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11, 5),
    _HwIfBrdVersion_Type()
)
hwIfBrdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfBrdVersion.setStatus("current")
_HwIfBrdPcbId_Type = Integer32
_HwIfBrdPcbId_Object = MibScalar
hwIfBrdPcbId = _HwIfBrdPcbId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11, 6),
    _HwIfBrdPcbId_Type()
)
hwIfBrdPcbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfBrdPcbId.setStatus("current")
_HwIfBrdAssemblyId_Type = Integer32
_HwIfBrdAssemblyId_Object = MibScalar
hwIfBrdAssemblyId = _HwIfBrdAssemblyId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 11, 7),
    _HwIfBrdAssemblyId_Type()
)
hwIfBrdAssemblyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfBrdAssemblyId.setStatus("current")
_HwSensor_ObjectIdentity = ObjectIdentity
hwSensor = _HwSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 21)
)
_HwSensorTable_Object = MibTable
hwSensorTable = _HwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 21, 1)
)
if mibBuilder.loadTexts:
    hwSensorTable.setStatus("current")
_HwSensorTableEntry_Object = MibTableRow
hwSensorTableEntry = _HwSensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 21, 1, 1)
)
hwSensorTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "hwSensorIndex"),
)
if mibBuilder.loadTexts:
    hwSensorTableEntry.setStatus("current")


class _HwSensorIndex_Type(Integer32):
    """Custom type hwSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwSensorIndex_Type.__name__ = "Integer32"
_HwSensorIndex_Object = MibTableColumn
hwSensorIndex = _HwSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 21, 1, 1, 1),
    _HwSensorIndex_Type()
)
hwSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSensorIndex.setStatus("current")


class _HwSensorName_Type(DisplayString):
    """Custom type hwSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSensorName_Type.__name__ = "DisplayString"
_HwSensorName_Object = MibTableColumn
hwSensorName = _HwSensorName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 21, 1, 1, 2),
    _HwSensorName_Type()
)
hwSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensorName.setStatus("current")


class _HwSensorUnit_Type(DisplayString):
    """Custom type hwSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSensorUnit_Type.__name__ = "DisplayString"
_HwSensorUnit_Object = MibTableColumn
hwSensorUnit = _HwSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 21, 1, 1, 3),
    _HwSensorUnit_Type()
)
hwSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensorUnit.setStatus("current")


class _HwSensorValue_Type(DisplayString):
    """Custom type hwSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSensorValue_Type.__name__ = "DisplayString"
_HwSensorValue_Object = MibTableColumn
hwSensorValue = _HwSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 5, 21, 1, 1, 4),
    _HwSensorValue_Type()
)
hwSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSensorValue.setStatus("current")
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6)
)
_SwFirmware_ObjectIdentity = ObjectIdentity
swFirmware = _SwFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 2)
)


class _SwFwName_Type(DisplayString):
    """Custom type swFwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwFwName_Type.__name__ = "DisplayString"
_SwFwName_Object = MibScalar
swFwName = _SwFwName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 2, 1),
    _SwFwName_Type()
)
swFwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwName.setStatus("current")


class _SwFwVersion_Type(DisplayString):
    """Custom type swFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwFwVersion_Type.__name__ = "DisplayString"
_SwFwVersion_Object = MibScalar
swFwVersion = _SwFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 2, 2),
    _SwFwVersion_Type()
)
swFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwVersion.setStatus("current")


class _SwFwRevision_Type(DisplayString):
    """Custom type swFwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwFwRevision_Type.__name__ = "DisplayString"
_SwFwRevision_Object = MibScalar
swFwRevision = _SwFwRevision_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 2, 3),
    _SwFwRevision_Type()
)
swFwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwRevision.setStatus("current")
_SwSystem_ObjectIdentity = ObjectIdentity
swSystem = _SwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3)
)


class _SwSysRebootReason_Type(Integer32):
    """Custom type swSysRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("coldstart", 0),
          ("warmstart", 1),
          ("watchdog", 2),
          ("oops", 3),
          ("unknown", 9))
    )


_SwSysRebootReason_Type.__name__ = "Integer32"
_SwSysRebootReason_Object = MibScalar
swSysRebootReason = _SwSysRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 1),
    _SwSysRebootReason_Type()
)
swSysRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysRebootReason.setStatus("current")


class _SwSysBootStatus_Type(Integer32):
    """Custom type swSysBootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("done", 0),
          ("booting", 1))
    )


_SwSysBootStatus_Type.__name__ = "Integer32"
_SwSysBootStatus_Object = MibScalar
swSysBootStatus = _SwSysBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 2),
    _SwSysBootStatus_Type()
)
swSysBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBootStatus.setStatus("current")
_SwSysMessageTable_Object = MibTable
swSysMessageTable = _SwSysMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 100)
)
if mibBuilder.loadTexts:
    swSysMessageTable.setStatus("current")
_SwSysMessageTableEntry_Object = MibTableRow
swSysMessageTableEntry = _SwSysMessageTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 100, 1)
)
swSysMessageTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "swSysMsgIndex"),
)
if mibBuilder.loadTexts:
    swSysMessageTableEntry.setStatus("current")


class _SwSysMsgIndex_Type(Integer32):
    """Custom type swSysMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwSysMsgIndex_Type.__name__ = "Integer32"
_SwSysMsgIndex_Object = MibTableColumn
swSysMsgIndex = _SwSysMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 100, 1, 1),
    _SwSysMsgIndex_Type()
)
swSysMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSysMsgIndex.setStatus("current")


class _SwSysMsgPriority_Type(Integer32):
    """Custom type swSysMsgPriority based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_SwSysMsgPriority_Type.__name__ = "Integer32"
_SwSysMsgPriority_Object = MibTableColumn
swSysMsgPriority = _SwSysMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 100, 1, 2),
    _SwSysMsgPriority_Type()
)
swSysMsgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysMsgPriority.setStatus("current")
_SwSysMsgCode_Type = Integer32
_SwSysMsgCode_Object = MibTableColumn
swSysMsgCode = _SwSysMsgCode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 100, 1, 3),
    _SwSysMsgCode_Type()
)
swSysMsgCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysMsgCode.setStatus("current")


class _SwSysMsgText_Type(DisplayString):
    """Custom type swSysMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwSysMsgText_Type.__name__ = "DisplayString"
_SwSysMsgText_Object = MibTableColumn
swSysMsgText = _SwSysMsgText_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 3, 100, 1, 4),
    _SwSysMsgText_Type()
)
swSysMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysMsgText.setStatus("current")
_SwOperatingSystem_ObjectIdentity = ObjectIdentity
swOperatingSystem = _SwOperatingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 4)
)


class _SwOsName_Type(DisplayString):
    """Custom type swOsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwOsName_Type.__name__ = "DisplayString"
_SwOsName_Object = MibScalar
swOsName = _SwOsName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 4, 1),
    _SwOsName_Type()
)
swOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOsName.setStatus("current")


class _SwOsVersion_Type(DisplayString):
    """Custom type swOsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwOsVersion_Type.__name__ = "DisplayString"
_SwOsVersion_Object = MibScalar
swOsVersion = _SwOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 4, 2),
    _SwOsVersion_Type()
)
swOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOsVersion.setStatus("current")


class _SwOsRevision_Type(DisplayString):
    """Custom type swOsRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwOsRevision_Type.__name__ = "DisplayString"
_SwOsRevision_Object = MibScalar
swOsRevision = _SwOsRevision_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 4, 3),
    _SwOsRevision_Type()
)
swOsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOsRevision.setStatus("current")
_SwOsUptime_Type = TimeTicks
_SwOsUptime_Object = MibScalar
swOsUptime = _SwOsUptime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 4, 4),
    _SwOsUptime_Type()
)
swOsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOsUptime.setStatus("current")
_SwDriver_ObjectIdentity = ObjectIdentity
swDriver = _SwDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5)
)
_SwDrvDfsTable_Object = MibTable
swDrvDfsTable = _SwDrvDfsTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    swDrvDfsTable.setStatus("current")
_SwDrvDfsTableEntry_Object = MibTableRow
swDrvDfsTableEntry = _SwDrvDfsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 1, 1)
)
swDrvDfsTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "swDrvDfsIndex"),
)
if mibBuilder.loadTexts:
    swDrvDfsTableEntry.setStatus("current")


class _SwDrvDfsIndex_Type(Integer32):
    """Custom type swDrvDfsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SwDrvDfsIndex_Type.__name__ = "Integer32"
_SwDrvDfsIndex_Object = MibTableColumn
swDrvDfsIndex = _SwDrvDfsIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 1, 1, 1),
    _SwDrvDfsIndex_Type()
)
swDrvDfsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDrvDfsIndex.setStatus("current")


class _SwDrvDfsName_Type(DisplayString):
    """Custom type swDrvDfsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvDfsName_Type.__name__ = "DisplayString"
_SwDrvDfsName_Object = MibTableColumn
swDrvDfsName = _SwDrvDfsName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 1, 1, 2),
    _SwDrvDfsName_Type()
)
swDrvDfsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvDfsName.setStatus("current")
_SwDrvDfsPulsesDetected_Type = Integer32
_SwDrvDfsPulsesDetected_Object = MibTableColumn
swDrvDfsPulsesDetected = _SwDrvDfsPulsesDetected_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 1, 1, 3),
    _SwDrvDfsPulsesDetected_Type()
)
swDrvDfsPulsesDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDrvDfsPulsesDetected.setStatus("current")
_SwDrvDfsPulsesProcessed_Type = Integer32
_SwDrvDfsPulsesProcessed_Object = MibTableColumn
swDrvDfsPulsesProcessed = _SwDrvDfsPulsesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 1, 1, 4),
    _SwDrvDfsPulsesProcessed_Type()
)
swDrvDfsPulsesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDrvDfsPulsesProcessed.setStatus("current")
_SwDrvDfsRadarDetected_Type = Integer32
_SwDrvDfsRadarDetected_Object = MibTableColumn
swDrvDfsRadarDetected = _SwDrvDfsRadarDetected_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 1, 1, 5),
    _SwDrvDfsRadarDetected_Type()
)
swDrvDfsRadarDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDrvDfsRadarDetected.setStatus("current")
_SwDrvCntWlanMacTable_Object = MibTable
swDrvCntWlanMacTable = _SwDrvCntWlanMacTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4)
)
if mibBuilder.loadTexts:
    swDrvCntWlanMacTable.setStatus("current")
_SwDrvCntWlanMacTableEntry_Object = MibTableRow
swDrvCntWlanMacTableEntry = _SwDrvCntWlanMacTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1)
)
swDrvCntWlanMacTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "swDrvCntWlanMacIndex"),
)
if mibBuilder.loadTexts:
    swDrvCntWlanMacTableEntry.setStatus("current")


class _SwDrvCntWlanMacIndex_Type(Integer32):
    """Custom type swDrvCntWlanMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwDrvCntWlanMacIndex_Type.__name__ = "Integer32"
_SwDrvCntWlanMacIndex_Object = MibTableColumn
swDrvCntWlanMacIndex = _SwDrvCntWlanMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 1),
    _SwDrvCntWlanMacIndex_Type()
)
swDrvCntWlanMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDrvCntWlanMacIndex.setStatus("current")


class _SwDrvCntWlanMacName_Type(DisplayString):
    """Custom type swDrvCntWlanMacName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvCntWlanMacName_Type.__name__ = "DisplayString"
_SwDrvCntWlanMacName_Object = MibTableColumn
swDrvCntWlanMacName = _SwDrvCntWlanMacName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 2),
    _SwDrvCntWlanMacName_Type()
)
swDrvCntWlanMacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacName.setStatus("current")
_SwDrvCntWlanMacTxHandlersDrop_Type = Integer32
_SwDrvCntWlanMacTxHandlersDrop_Object = MibTableColumn
swDrvCntWlanMacTxHandlersDrop = _SwDrvCntWlanMacTxHandlersDrop_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 3),
    _SwDrvCntWlanMacTxHandlersDrop_Type()
)
swDrvCntWlanMacTxHandlersDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxHandlersDrop.setStatus("current")
_SwDrvCntWlanMacTxHandlersQueued_Type = Integer32
_SwDrvCntWlanMacTxHandlersQueued_Object = MibTableColumn
swDrvCntWlanMacTxHandlersQueued = _SwDrvCntWlanMacTxHandlersQueued_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 4),
    _SwDrvCntWlanMacTxHandlersQueued_Type()
)
swDrvCntWlanMacTxHandlersQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxHandlersQueued.setStatus("current")
_SwDrvCntWlanMacTxHandlersDropUnencrypted_Type = Integer32
_SwDrvCntWlanMacTxHandlersDropUnencrypted_Object = MibTableColumn
swDrvCntWlanMacTxHandlersDropUnencrypted = _SwDrvCntWlanMacTxHandlersDropUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 5),
    _SwDrvCntWlanMacTxHandlersDropUnencrypted_Type()
)
swDrvCntWlanMacTxHandlersDropUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxHandlersDropUnencrypted.setStatus("current")
_SwDrvCntWlanMacTxHandlersDropFragment_Type = Integer32
_SwDrvCntWlanMacTxHandlersDropFragment_Object = MibTableColumn
swDrvCntWlanMacTxHandlersDropFragment = _SwDrvCntWlanMacTxHandlersDropFragment_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 6),
    _SwDrvCntWlanMacTxHandlersDropFragment_Type()
)
swDrvCntWlanMacTxHandlersDropFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxHandlersDropFragment.setStatus("current")
_SwDrvCntWlanMacTxHandlersDropWep_Type = Integer32
_SwDrvCntWlanMacTxHandlersDropWep_Object = MibTableColumn
swDrvCntWlanMacTxHandlersDropWep = _SwDrvCntWlanMacTxHandlersDropWep_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 7),
    _SwDrvCntWlanMacTxHandlersDropWep_Type()
)
swDrvCntWlanMacTxHandlersDropWep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxHandlersDropWep.setStatus("current")
_SwDrvCntWlanMacTxHandlersDropNotAssoc_Type = Integer32
_SwDrvCntWlanMacTxHandlersDropNotAssoc_Object = MibTableColumn
swDrvCntWlanMacTxHandlersDropNotAssoc = _SwDrvCntWlanMacTxHandlersDropNotAssoc_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 8),
    _SwDrvCntWlanMacTxHandlersDropNotAssoc_Type()
)
swDrvCntWlanMacTxHandlersDropNotAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxHandlersDropNotAssoc.setStatus("current")
_SwDrvCntWlanMacTxHandlersDropUnauthPort_Type = Integer32
_SwDrvCntWlanMacTxHandlersDropUnauthPort_Object = MibTableColumn
swDrvCntWlanMacTxHandlersDropUnauthPort = _SwDrvCntWlanMacTxHandlersDropUnauthPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 9),
    _SwDrvCntWlanMacTxHandlersDropUnauthPort_Type()
)
swDrvCntWlanMacTxHandlersDropUnauthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxHandlersDropUnauthPort.setStatus("current")
_SwDrvCntWlanMacRxHandlersDrop_Type = Integer32
_SwDrvCntWlanMacRxHandlersDrop_Object = MibTableColumn
swDrvCntWlanMacRxHandlersDrop = _SwDrvCntWlanMacRxHandlersDrop_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 10),
    _SwDrvCntWlanMacRxHandlersDrop_Type()
)
swDrvCntWlanMacRxHandlersDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxHandlersDrop.setStatus("current")
_SwDrvCntWlanMacRxHandlersQueued_Type = Integer32
_SwDrvCntWlanMacRxHandlersQueued_Object = MibTableColumn
swDrvCntWlanMacRxHandlersQueued = _SwDrvCntWlanMacRxHandlersQueued_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 11),
    _SwDrvCntWlanMacRxHandlersQueued_Type()
)
swDrvCntWlanMacRxHandlersQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxHandlersQueued.setStatus("current")
_SwDrvCntWlanMacRxHandlersDropNullfunc_Type = Integer32
_SwDrvCntWlanMacRxHandlersDropNullfunc_Object = MibTableColumn
swDrvCntWlanMacRxHandlersDropNullfunc = _SwDrvCntWlanMacRxHandlersDropNullfunc_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 12),
    _SwDrvCntWlanMacRxHandlersDropNullfunc_Type()
)
swDrvCntWlanMacRxHandlersDropNullfunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxHandlersDropNullfunc.setStatus("current")
_SwDrvCntWlanMacRxHandlersDropDefrag_Type = Integer32
_SwDrvCntWlanMacRxHandlersDropDefrag_Object = MibTableColumn
swDrvCntWlanMacRxHandlersDropDefrag = _SwDrvCntWlanMacRxHandlersDropDefrag_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 13),
    _SwDrvCntWlanMacRxHandlersDropDefrag_Type()
)
swDrvCntWlanMacRxHandlersDropDefrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxHandlersDropDefrag.setStatus("current")
_SwDrvCntWlanMacRxHandlersDropShort_Type = Integer32
_SwDrvCntWlanMacRxHandlersDropShort_Object = MibTableColumn
swDrvCntWlanMacRxHandlersDropShort = _SwDrvCntWlanMacRxHandlersDropShort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 14),
    _SwDrvCntWlanMacRxHandlersDropShort_Type()
)
swDrvCntWlanMacRxHandlersDropShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxHandlersDropShort.setStatus("current")
_SwDrvCntWlanMacTxExpandSkbHead_Type = Integer32
_SwDrvCntWlanMacTxExpandSkbHead_Object = MibTableColumn
swDrvCntWlanMacTxExpandSkbHead = _SwDrvCntWlanMacTxExpandSkbHead_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 15),
    _SwDrvCntWlanMacTxExpandSkbHead_Type()
)
swDrvCntWlanMacTxExpandSkbHead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxExpandSkbHead.setStatus("current")
_SwDrvCntWlanMacTxExpandSkbHeadCloned_Type = Integer32
_SwDrvCntWlanMacTxExpandSkbHeadCloned_Object = MibTableColumn
swDrvCntWlanMacTxExpandSkbHeadCloned = _SwDrvCntWlanMacTxExpandSkbHeadCloned_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 16),
    _SwDrvCntWlanMacTxExpandSkbHeadCloned_Type()
)
swDrvCntWlanMacTxExpandSkbHeadCloned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxExpandSkbHeadCloned.setStatus("current")
_SwDrvCntWlanMacRxExpandSkbHead_Type = Integer32
_SwDrvCntWlanMacRxExpandSkbHead_Object = MibTableColumn
swDrvCntWlanMacRxExpandSkbHead = _SwDrvCntWlanMacRxExpandSkbHead_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 17),
    _SwDrvCntWlanMacRxExpandSkbHead_Type()
)
swDrvCntWlanMacRxExpandSkbHead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxExpandSkbHead.setStatus("current")
_SwDrvCntWlanMacRxExpandSkbHead2_Type = Integer32
_SwDrvCntWlanMacRxExpandSkbHead2_Object = MibTableColumn
swDrvCntWlanMacRxExpandSkbHead2 = _SwDrvCntWlanMacRxExpandSkbHead2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 18),
    _SwDrvCntWlanMacRxExpandSkbHead2_Type()
)
swDrvCntWlanMacRxExpandSkbHead2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxExpandSkbHead2.setStatus("current")
_SwDrvCntWlanMacRxHandlersFragments_Type = Integer32
_SwDrvCntWlanMacRxHandlersFragments_Object = MibTableColumn
swDrvCntWlanMacRxHandlersFragments = _SwDrvCntWlanMacRxHandlersFragments_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 19),
    _SwDrvCntWlanMacRxHandlersFragments_Type()
)
swDrvCntWlanMacRxHandlersFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacRxHandlersFragments.setStatus("current")
_SwDrvCntWlanMacTxstatusDrop_Type = Integer32
_SwDrvCntWlanMacTxstatusDrop_Object = MibTableColumn
swDrvCntWlanMacTxstatusDrop = _SwDrvCntWlanMacTxstatusDrop_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 4, 1, 20),
    _SwDrvCntWlanMacTxstatusDrop_Type()
)
swDrvCntWlanMacTxstatusDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanMacTxstatusDrop.setStatus("current")
_SwDrvCntWlanWmmTable_Object = MibTable
swDrvCntWlanWmmTable = _SwDrvCntWlanWmmTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6)
)
if mibBuilder.loadTexts:
    swDrvCntWlanWmmTable.setStatus("current")
_SwDrvCntWlanWmmTableEntry_Object = MibTableRow
swDrvCntWlanWmmTableEntry = _SwDrvCntWlanWmmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1)
)
swDrvCntWlanWmmTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "swDrvCntWlanWmmTableIndex"),
)
if mibBuilder.loadTexts:
    swDrvCntWlanWmmTableEntry.setStatus("current")


class _SwDrvCntWlanWmmTableIndex_Type(Integer32):
    """Custom type swDrvCntWlanWmmTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SwDrvCntWlanWmmTableIndex_Type.__name__ = "Integer32"
_SwDrvCntWlanWmmTableIndex_Object = MibTableColumn
swDrvCntWlanWmmTableIndex = _SwDrvCntWlanWmmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1, 1),
    _SwDrvCntWlanWmmTableIndex_Type()
)
swDrvCntWlanWmmTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDrvCntWlanWmmTableIndex.setStatus("current")


class _SwDrvCntWlanWmmName_Type(DisplayString):
    """Custom type swDrvCntWlanWmmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvCntWlanWmmName_Type.__name__ = "DisplayString"
_SwDrvCntWlanWmmName_Object = MibTableColumn
swDrvCntWlanWmmName = _SwDrvCntWlanWmmName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1, 2),
    _SwDrvCntWlanWmmName_Type()
)
swDrvCntWlanWmmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanWmmName.setStatus("current")
_SwDrvCntWlanWmmTx_Type = Integer32
_SwDrvCntWlanWmmTx_Object = MibTableColumn
swDrvCntWlanWmmTx = _SwDrvCntWlanWmmTx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1, 3),
    _SwDrvCntWlanWmmTx_Type()
)
swDrvCntWlanWmmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanWmmTx.setStatus("current")
_SwDrvCntWlanWmmRx_Type = Integer32
_SwDrvCntWlanWmmRx_Object = MibTableColumn
swDrvCntWlanWmmRx = _SwDrvCntWlanWmmRx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1, 4),
    _SwDrvCntWlanWmmRx_Type()
)
swDrvCntWlanWmmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanWmmRx.setStatus("current")
_SwDrvCntWlanWmmShortRetries_Type = Integer32
_SwDrvCntWlanWmmShortRetries_Object = MibTableColumn
swDrvCntWlanWmmShortRetries = _SwDrvCntWlanWmmShortRetries_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1, 5),
    _SwDrvCntWlanWmmShortRetries_Type()
)
swDrvCntWlanWmmShortRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanWmmShortRetries.setStatus("current")
_SwDrvCntWlanWmmLongRetries_Type = Integer32
_SwDrvCntWlanWmmLongRetries_Object = MibTableColumn
swDrvCntWlanWmmLongRetries = _SwDrvCntWlanWmmLongRetries_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1, 6),
    _SwDrvCntWlanWmmLongRetries_Type()
)
swDrvCntWlanWmmLongRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanWmmLongRetries.setStatus("current")
_SwDrvCntWlanWmmExceededRetries_Type = Integer32
_SwDrvCntWlanWmmExceededRetries_Object = MibTableColumn
swDrvCntWlanWmmExceededRetries = _SwDrvCntWlanWmmExceededRetries_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 6, 1, 7),
    _SwDrvCntWlanWmmExceededRetries_Type()
)
swDrvCntWlanWmmExceededRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanWmmExceededRetries.setStatus("current")


class _SwDrvConStatWlanIf_Type(DisplayString):
    """Custom type swDrvConStatWlanIf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 17),
    )


_SwDrvConStatWlanIf_Type.__name__ = "DisplayString"
_SwDrvConStatWlanIf_Object = MibScalar
swDrvConStatWlanIf = _SwDrvConStatWlanIf_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 7),
    _SwDrvConStatWlanIf_Type()
)
swDrvConStatWlanIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDrvConStatWlanIf.setStatus("current")
_SwDrvConStatTable_Object = MibTable
swDrvConStatTable = _SwDrvConStatTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8)
)
if mibBuilder.loadTexts:
    swDrvConStatTable.setStatus("current")
_SwDrvConStatTableEntry_Object = MibTableRow
swDrvConStatTableEntry = _SwDrvConStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1)
)
swDrvConStatTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "swDrvConStatIndex"),
)
if mibBuilder.loadTexts:
    swDrvConStatTableEntry.setStatus("current")


class _SwDrvConStatIndex_Type(Integer32):
    """Custom type swDrvConStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_SwDrvConStatIndex_Type.__name__ = "Integer32"
_SwDrvConStatIndex_Object = MibTableColumn
swDrvConStatIndex = _SwDrvConStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 1),
    _SwDrvConStatIndex_Type()
)
swDrvConStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDrvConStatIndex.setStatus("current")


class _SwDrvConStatWlanName_Type(DisplayString):
    """Custom type swDrvConStatWlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 5),
    )


_SwDrvConStatWlanName_Type.__name__ = "DisplayString"
_SwDrvConStatWlanName_Object = MibTableColumn
swDrvConStatWlanName = _SwDrvConStatWlanName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 2),
    _SwDrvConStatWlanName_Type()
)
swDrvConStatWlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatWlanName.setStatus("current")


class _SwDrvConStatMacName_Type(DisplayString):
    """Custom type swDrvConStatMacName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SwDrvConStatMacName_Type.__name__ = "DisplayString"
_SwDrvConStatMacName_Object = MibTableColumn
swDrvConStatMacName = _SwDrvConStatMacName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 3),
    _SwDrvConStatMacName_Type()
)
swDrvConStatMacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatMacName.setStatus("current")


class _SwDrvConStatRxBrExtra_Type(DisplayString):
    """Custom type swDrvConStatRxBrExtra based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvConStatRxBrExtra_Type.__name__ = "DisplayString"
_SwDrvConStatRxBrExtra_Object = MibTableColumn
swDrvConStatRxBrExtra = _SwDrvConStatRxBrExtra_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 4),
    _SwDrvConStatRxBrExtra_Type()
)
swDrvConStatRxBrExtra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatRxBrExtra.setStatus("current")


class _SwDrvConStatRxBrType_Type(DisplayString):
    """Custom type swDrvConStatRxBrType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvConStatRxBrType_Type.__name__ = "DisplayString"
_SwDrvConStatRxBrType_Object = MibTableColumn
swDrvConStatRxBrType = _SwDrvConStatRxBrType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 5),
    _SwDrvConStatRxBrType_Type()
)
swDrvConStatRxBrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatRxBrType.setStatus("current")
_SwDrvConStatRxBrValue_Type = Integer32
_SwDrvConStatRxBrValue_Object = MibTableColumn
swDrvConStatRxBrValue = _SwDrvConStatRxBrValue_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 6),
    _SwDrvConStatRxBrValue_Type()
)
swDrvConStatRxBrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatRxBrValue.setStatus("current")
_SwDrvConStatRxBytes_Type = Integer32
_SwDrvConStatRxBytes_Object = MibTableColumn
swDrvConStatRxBytes = _SwDrvConStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 7),
    _SwDrvConStatRxBytes_Type()
)
swDrvConStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatRxBytes.setStatus("current")
_SwDrvConStatRxPackets_Type = Integer32
_SwDrvConStatRxPackets_Object = MibTableColumn
swDrvConStatRxPackets = _SwDrvConStatRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 8),
    _SwDrvConStatRxPackets_Type()
)
swDrvConStatRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatRxPackets.setStatus("current")


class _SwDrvConStatTxBrExtra_Type(DisplayString):
    """Custom type swDrvConStatTxBrExtra based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvConStatTxBrExtra_Type.__name__ = "DisplayString"
_SwDrvConStatTxBrExtra_Object = MibTableColumn
swDrvConStatTxBrExtra = _SwDrvConStatTxBrExtra_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 9),
    _SwDrvConStatTxBrExtra_Type()
)
swDrvConStatTxBrExtra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatTxBrExtra.setStatus("current")


class _SwDrvConStatTxBrType_Type(DisplayString):
    """Custom type swDrvConStatTxBrType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvConStatTxBrType_Type.__name__ = "DisplayString"
_SwDrvConStatTxBrType_Object = MibTableColumn
swDrvConStatTxBrType = _SwDrvConStatTxBrType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 10),
    _SwDrvConStatTxBrType_Type()
)
swDrvConStatTxBrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatTxBrType.setStatus("current")
_SwDrvConStatTxBrValue_Type = Integer32
_SwDrvConStatTxBrValue_Object = MibTableColumn
swDrvConStatTxBrValue = _SwDrvConStatTxBrValue_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 11),
    _SwDrvConStatTxBrValue_Type()
)
swDrvConStatTxBrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatTxBrValue.setStatus("current")
_SwDrvConStatTxBytes_Type = Integer32
_SwDrvConStatTxBytes_Object = MibTableColumn
swDrvConStatTxBytes = _SwDrvConStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 12),
    _SwDrvConStatTxBytes_Type()
)
swDrvConStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatTxBytes.setStatus("current")
_SwDrvConStatTxPackets_Type = Integer32
_SwDrvConStatTxPackets_Object = MibTableColumn
swDrvConStatTxPackets = _SwDrvConStatTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 13),
    _SwDrvConStatTxPackets_Type()
)
swDrvConStatTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatTxPackets.setStatus("current")
_SwDrvConStatSigChain0_Type = Integer32
_SwDrvConStatSigChain0_Object = MibTableColumn
swDrvConStatSigChain0 = _SwDrvConStatSigChain0_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 14),
    _SwDrvConStatSigChain0_Type()
)
swDrvConStatSigChain0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigChain0.setStatus("current")
_SwDrvConStatSigChain1_Type = Integer32
_SwDrvConStatSigChain1_Object = MibTableColumn
swDrvConStatSigChain1 = _SwDrvConStatSigChain1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 15),
    _SwDrvConStatSigChain1_Type()
)
swDrvConStatSigChain1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigChain1.setStatus("current")
_SwDrvConStatSigChain2_Type = Integer32
_SwDrvConStatSigChain2_Object = MibTableColumn
swDrvConStatSigChain2 = _SwDrvConStatSigChain2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 16),
    _SwDrvConStatSigChain2_Type()
)
swDrvConStatSigChain2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigChain2.setStatus("current")
_SwDrvConStatSigAvgChain0_Type = Integer32
_SwDrvConStatSigAvgChain0_Object = MibTableColumn
swDrvConStatSigAvgChain0 = _SwDrvConStatSigAvgChain0_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 17),
    _SwDrvConStatSigAvgChain0_Type()
)
swDrvConStatSigAvgChain0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigAvgChain0.setStatus("current")
_SwDrvConStatSigAvgChain1_Type = Integer32
_SwDrvConStatSigAvgChain1_Object = MibTableColumn
swDrvConStatSigAvgChain1 = _SwDrvConStatSigAvgChain1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 18),
    _SwDrvConStatSigAvgChain1_Type()
)
swDrvConStatSigAvgChain1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigAvgChain1.setStatus("current")
_SwDrvConStatSigAvgChain2_Type = Integer32
_SwDrvConStatSigAvgChain2_Object = MibTableColumn
swDrvConStatSigAvgChain2 = _SwDrvConStatSigAvgChain2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 19),
    _SwDrvConStatSigAvgChain2_Type()
)
swDrvConStatSigAvgChain2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigAvgChain2.setStatus("current")
_SwDrvConStatTxRetries_Type = Integer32
_SwDrvConStatTxRetries_Object = MibTableColumn
swDrvConStatTxRetries = _SwDrvConStatTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 20),
    _SwDrvConStatTxRetries_Type()
)
swDrvConStatTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatTxRetries.setStatus("current")
_SwDrvConStatTxFailed_Type = Integer32
_SwDrvConStatTxFailed_Object = MibTableColumn
swDrvConStatTxFailed = _SwDrvConStatTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 21),
    _SwDrvConStatTxFailed_Type()
)
swDrvConStatTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatTxFailed.setStatus("current")
_SwDrvConStatCacheNo_Type = Integer32
_SwDrvConStatCacheNo_Object = MibTableColumn
swDrvConStatCacheNo = _SwDrvConStatCacheNo_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 22),
    _SwDrvConStatCacheNo_Type()
)
swDrvConStatCacheNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatCacheNo.setStatus("current")
_SwDrvConStatSigCombined_Type = Integer32
_SwDrvConStatSigCombined_Object = MibTableColumn
swDrvConStatSigCombined = _SwDrvConStatSigCombined_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 23),
    _SwDrvConStatSigCombined_Type()
)
swDrvConStatSigCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigCombined.setStatus("current")
_SwDrvConStatSigAvgCombined_Type = Integer32
_SwDrvConStatSigAvgCombined_Object = MibTableColumn
swDrvConStatSigAvgCombined = _SwDrvConStatSigAvgCombined_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 8, 1, 24),
    _SwDrvConStatSigAvgCombined_Type()
)
swDrvConStatSigAvgCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvConStatSigAvgCombined.setStatus("current")
_SwDrvCntWlanTable_Object = MibTable
swDrvCntWlanTable = _SwDrvCntWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9)
)
if mibBuilder.loadTexts:
    swDrvCntWlanTable.setStatus("current")
_SwDrvCntWlanTableEntry_Object = MibTableRow
swDrvCntWlanTableEntry = _SwDrvCntWlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1)
)
swDrvCntWlanTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-MIB", "swDrvCntWlanIndex"),
)
if mibBuilder.loadTexts:
    swDrvCntWlanTableEntry.setStatus("current")


class _SwDrvCntWlanIndex_Type(Integer32):
    """Custom type swDrvCntWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwDrvCntWlanIndex_Type.__name__ = "Integer32"
_SwDrvCntWlanIndex_Object = MibTableColumn
swDrvCntWlanIndex = _SwDrvCntWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 1),
    _SwDrvCntWlanIndex_Type()
)
swDrvCntWlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDrvCntWlanIndex.setStatus("current")


class _SwDrvCntWlanName_Type(DisplayString):
    """Custom type swDrvCntWlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwDrvCntWlanName_Type.__name__ = "DisplayString"
_SwDrvCntWlanName_Object = MibTableColumn
swDrvCntWlanName = _SwDrvCntWlanName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 2),
    _SwDrvCntWlanName_Type()
)
swDrvCntWlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanName.setStatus("current")
_SwDrvCntWlanAssocSuccess_Type = Counter32
_SwDrvCntWlanAssocSuccess_Object = MibTableColumn
swDrvCntWlanAssocSuccess = _SwDrvCntWlanAssocSuccess_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 4),
    _SwDrvCntWlanAssocSuccess_Type()
)
swDrvCntWlanAssocSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanAssocSuccess.setStatus("current")
_SwDrvCntWlanAssocFailure_Type = Counter32
_SwDrvCntWlanAssocFailure_Object = MibTableColumn
swDrvCntWlanAssocFailure = _SwDrvCntWlanAssocFailure_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 5),
    _SwDrvCntWlanAssocFailure_Type()
)
swDrvCntWlanAssocFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanAssocFailure.setStatus("current")
_SwDrvCntWlanAssocFailureMaxSta_Type = Counter32
_SwDrvCntWlanAssocFailureMaxSta_Object = MibTableColumn
swDrvCntWlanAssocFailureMaxSta = _SwDrvCntWlanAssocFailureMaxSta_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 6),
    _SwDrvCntWlanAssocFailureMaxSta_Type()
)
swDrvCntWlanAssocFailureMaxSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanAssocFailureMaxSta.setStatus("current")
_SwDrvCntWlanNumAssocSta_Type = Counter32
_SwDrvCntWlanNumAssocSta_Object = MibTableColumn
swDrvCntWlanNumAssocSta = _SwDrvCntWlanNumAssocSta_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 7),
    _SwDrvCntWlanNumAssocSta_Type()
)
swDrvCntWlanNumAssocSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanNumAssocSta.setStatus("current")
_SwDrvCntWlanEapAuthStarted_Type = Counter32
_SwDrvCntWlanEapAuthStarted_Object = MibTableColumn
swDrvCntWlanEapAuthStarted = _SwDrvCntWlanEapAuthStarted_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 8),
    _SwDrvCntWlanEapAuthStarted_Type()
)
swDrvCntWlanEapAuthStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanEapAuthStarted.setStatus("current")
_SwDrvCntWlanEapAuthFailed_Type = Counter32
_SwDrvCntWlanEapAuthFailed_Object = MibTableColumn
swDrvCntWlanEapAuthFailed = _SwDrvCntWlanEapAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 9),
    _SwDrvCntWlanEapAuthFailed_Type()
)
swDrvCntWlanEapAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanEapAuthFailed.setStatus("current")
_SwDrvCntWlanChannelActive_Type = Counter32
_SwDrvCntWlanChannelActive_Object = MibTableColumn
swDrvCntWlanChannelActive = _SwDrvCntWlanChannelActive_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 10),
    _SwDrvCntWlanChannelActive_Type()
)
swDrvCntWlanChannelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanChannelActive.setStatus("current")
_SwDrvCntWlanChannelBusy_Type = Counter32
_SwDrvCntWlanChannelBusy_Object = MibTableColumn
swDrvCntWlanChannelBusy = _SwDrvCntWlanChannelBusy_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 11),
    _SwDrvCntWlanChannelBusy_Type()
)
swDrvCntWlanChannelBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanChannelBusy.setStatus("current")
_SwDrvCntWlanChannelTransmit_Type = Counter32
_SwDrvCntWlanChannelTransmit_Object = MibTableColumn
swDrvCntWlanChannelTransmit = _SwDrvCntWlanChannelTransmit_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 12),
    _SwDrvCntWlanChannelTransmit_Type()
)
swDrvCntWlanChannelTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanChannelTransmit.setStatus("current")
_SwDrvCntWlanChannelReceive_Type = Counter32
_SwDrvCntWlanChannelReceive_Object = MibTableColumn
swDrvCntWlanChannelReceive = _SwDrvCntWlanChannelReceive_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 13),
    _SwDrvCntWlanChannelReceive_Type()
)
swDrvCntWlanChannelReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanChannelReceive.setStatus("current")
_SwDrvCntWlanChannelNoise_Type = Counter32
_SwDrvCntWlanChannelNoise_Object = MibTableColumn
swDrvCntWlanChannelNoise = _SwDrvCntWlanChannelNoise_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 14),
    _SwDrvCntWlanChannelNoise_Type()
)
swDrvCntWlanChannelNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanChannelNoise.setStatus("current")
_SwDrvCntWlanEapAuthStartedFT_Type = Counter32
_SwDrvCntWlanEapAuthStartedFT_Object = MibTableColumn
swDrvCntWlanEapAuthStartedFT = _SwDrvCntWlanEapAuthStartedFT_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 20),
    _SwDrvCntWlanEapAuthStartedFT_Type()
)
swDrvCntWlanEapAuthStartedFT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanEapAuthStartedFT.setStatus("current")
_SwDrvCntWlanEapAuthStartedFILS_Type = Counter32
_SwDrvCntWlanEapAuthStartedFILS_Object = MibTableColumn
swDrvCntWlanEapAuthStartedFILS = _SwDrvCntWlanEapAuthStartedFILS_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 21),
    _SwDrvCntWlanEapAuthStartedFILS_Type()
)
swDrvCntWlanEapAuthStartedFILS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanEapAuthStartedFILS.setStatus("current")
_SwDrvCntWlanEapAuthStartedPKMSA_Type = Counter32
_SwDrvCntWlanEapAuthStartedPKMSA_Object = MibTableColumn
swDrvCntWlanEapAuthStartedPKMSA = _SwDrvCntWlanEapAuthStartedPKMSA_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 5, 9, 1, 22),
    _SwDrvCntWlanEapAuthStartedPKMSA_Type()
)
swDrvCntWlanEapAuthStartedPKMSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDrvCntWlanEapAuthStartedPKMSA.setStatus("current")
_SwRdm_ObjectIdentity = ObjectIdentity
swRdm = _SwRdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 6)
)
_SwRdmMaxEirp_Type = Integer32
_SwRdmMaxEirp_Object = MibScalar
swRdmMaxEirp = _SwRdmMaxEirp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 6, 1),
    _SwRdmMaxEirp_Type()
)
swRdmMaxEirp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRdmMaxEirp.setStatus("current")
_SwRdmMaxApp_Type = Integer32
_SwRdmMaxApp_Object = MibScalar
swRdmMaxApp = _SwRdmMaxApp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 6, 2),
    _SwRdmMaxApp_Type()
)
swRdmMaxApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRdmMaxApp.setStatus("current")
_SwBootloader_ObjectIdentity = ObjectIdentity
swBootloader = _SwBootloader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 20)
)


class _SwBootName_Type(DisplayString):
    """Custom type swBootName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwBootName_Type.__name__ = "DisplayString"
_SwBootName_Object = MibScalar
swBootName = _SwBootName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 20, 1),
    _SwBootName_Type()
)
swBootName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootName.setStatus("current")


class _SwBootVersion_Type(DisplayString):
    """Custom type swBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwBootVersion_Type.__name__ = "DisplayString"
_SwBootVersion_Object = MibScalar
swBootVersion = _SwBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 20, 2),
    _SwBootVersion_Type()
)
swBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootVersion.setStatus("current")


class _SwBootBuildDate_Type(DisplayString):
    """Custom type swBootBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwBootBuildDate_Type.__name__ = "DisplayString"
_SwBootBuildDate_Object = MibScalar
swBootBuildDate = _SwBootBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 20, 3),
    _SwBootBuildDate_Type()
)
swBootBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootBuildDate.setStatus("current")
_SwConfiguration_ObjectIdentity = ObjectIdentity
swConfiguration = _SwConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 30)
)
_SwCfgChangesCount_Type = Integer32
_SwCfgChangesCount_Object = MibScalar
swCfgChangesCount = _SwCfgChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 6, 30, 1),
    _SwCfgChangesCount_Type()
)
swCfgChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCfgChangesCount.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1)
)
_GroupConfiguration_ObjectIdentity = ObjectIdentity
groupConfiguration = _GroupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1)
)
_GroupCfgNetwork_ObjectIdentity = ObjectIdentity
groupCfgNetwork = _GroupCfgNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2)
)
_GroupCfgWireless_ObjectIdentity = ObjectIdentity
groupCfgWireless = _GroupCfgWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3)
)
_GroupCfgRouting_ObjectIdentity = ObjectIdentity
groupCfgRouting = _GroupCfgRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 4)
)
_GroupCfgSnmp_ObjectIdentity = ObjectIdentity
groupCfgSnmp = _GroupCfgSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 12)
)
_GroupCfgDhcp_ObjectIdentity = ObjectIdentity
groupCfgDhcp = _GroupCfgDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 13)
)
_GroupCfgQos_ObjectIdentity = ObjectIdentity
groupCfgQos = _GroupCfgQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 18)
)
_GroupCfgCellular_ObjectIdentity = ObjectIdentity
groupCfgCellular = _GroupCfgCellular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 101)
)
_GroupStatus_ObjectIdentity = ObjectIdentity
groupStatus = _GroupStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 2)
)
_GroupRpc_ObjectIdentity = ObjectIdentity
groupRpc = _GroupRpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 3)
)
_GroupSettings_ObjectIdentity = ObjectIdentity
groupSettings = _GroupSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4)
)
_GroupHardware_ObjectIdentity = ObjectIdentity
groupHardware = _GroupHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 5)
)
_GroupSoftware_ObjectIdentity = ObjectIdentity
groupSoftware = _GroupSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6)
)
_GroupFeatures_ObjectIdentity = ObjectIdentity
groupFeatures = _GroupFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 7)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 2)
)

# Managed Objects groups

groupCfgSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 1)
)
groupCfgSystem.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgSysHostname"),
        ("WESTERMO-SW6-MIB", "cfgSysTimezone"))
)
if mibBuilder.loadTexts:
    groupCfgSystem.setStatus("current")

groupCfgNetEthernet = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2, 1)
)
groupCfgNetEthernet.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNetEthName"),
        ("WESTERMO-SW6-MIB", "cfgNetEthEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNetEthBridge"),
        ("WESTERMO-SW6-MIB", "cfgNetEthAutoneg"),
        ("WESTERMO-SW6-MIB", "cfgNetEthSpeed"),
        ("WESTERMO-SW6-MIB", "cfgNetEthTrunk"),
        ("WESTERMO-SW6-MIB", "cfgNetEthTag"),
        ("WESTERMO-SW6-MIB", "cfgNetEthVlanMode"),
        ("WESTERMO-SW6-MIB", "cfgNetEthLldpEnabled"))
)
if mibBuilder.loadTexts:
    groupCfgNetEthernet.setStatus("current")

groupCfgNetWlan = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2, 2)
)
groupCfgNetWlan.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNetWlanName"),
        ("WESTERMO-SW6-MIB", "cfgNetWlanEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNetWlanBridge"),
        ("WESTERMO-SW6-MIB", "cfgNetWlanTrunk"),
        ("WESTERMO-SW6-MIB", "cfgNetWlanTag"),
        ("WESTERMO-SW6-MIB", "cfgNetWlanVlanMode"),
        ("WESTERMO-SW6-MIB", "cfgNetWlanLldpEnabled"))
)
if mibBuilder.loadTexts:
    groupCfgNetWlan.setStatus("current")

groupCfgNetVlan = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2, 3)
)
groupCfgNetVlan.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNetVlanName"),
        ("WESTERMO-SW6-MIB", "cfgNetVlanEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNetVlanBridge"),
        ("WESTERMO-SW6-MIB", "cfgNetVlanParent"),
        ("WESTERMO-SW6-MIB", "cfgNetVlanVid"))
)
if mibBuilder.loadTexts:
    groupCfgNetVlan.setStatus("current")

groupCfgNetIp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2, 6)
)
groupCfgNetIp.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNetIpEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNetIpAddr"),
        ("WESTERMO-SW6-MIB", "cfgNetIpProto"),
        ("WESTERMO-SW6-MIB", "cfgNetIpInterface"),
        ("WESTERMO-SW6-MIB", "cfgNetIpCarpId"))
)
if mibBuilder.loadTexts:
    groupCfgNetIp.setStatus("current")

groupCfgNetCarp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2, 7)
)
groupCfgNetCarp.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNetCarpEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpVhid"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpPassword"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpAdvbase"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpAdvskew"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpAdvdivider"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpRatio"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpPreempt"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpPreemptdemote"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpLocalInterfaceGroup"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpSyncInterface"),
        ("WESTERMO-SW6-MIB", "cfgNetCarpMcastIp"))
)
if mibBuilder.loadTexts:
    groupCfgNetCarp.setStatus("current")

groupCfgNetMacVLan = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2, 9)
)
groupCfgNetMacVLan.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNetMacVlanName"),
        ("WESTERMO-SW6-MIB", "cfgNetMacVlanEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNetMacVlanParent"),
        ("WESTERMO-SW6-MIB", "cfgNetMacVlanMac"))
)
if mibBuilder.loadTexts:
    groupCfgNetMacVLan.setStatus("current")

groupCfgNetWwan = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 2, 11)
)
groupCfgNetWwan.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNetWwanName"),
        ("WESTERMO-SW6-MIB", "cfgNetWwanEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNetWwanPrimarySim"),
        ("WESTERMO-SW6-MIB", "cfgNetWwanSecondarySim"))
)
if mibBuilder.loadTexts:
    groupCfgNetWwan.setStatus("current")

groupCfgWlanDevice = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 1)
)
groupCfgWlanDevice.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanDevName"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevModulation"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevBandwidth"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevFrequency"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevPower"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevDistance"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevRts"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevFragments"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevShortRetry"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevLongRetry"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevAntennaGain"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevTxAntenna"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevRxAntenna"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevPhy"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevHtCapabilities"),
        ("WESTERMO-SW6-MIB", "cfgWlanDevQmrrString"))
)
if mibBuilder.loadTexts:
    groupCfgWlanDevice.setStatus("current")

groupCfgWlanInterface = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 2)
)
groupCfgWlanInterface.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanIfaceName"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceDevice"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceMode"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceSsid"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceEncryption"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfacePassword"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfacePassiveScanning"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceBeaconMiss"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceDtim"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceBitrates"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceBeaconInterval"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceWmeParameter"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceWmeEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceScanList"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceIgnoreBroadcastSsid"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceMacaddrAcl"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceMaxNumSta"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceBssid"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceLegacyRates"),
        ("WESTERMO-SW6-MIB", "cfgWlanIface4addr"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceInactivityTimeout"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceUseVendorSsid"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceIeee80211w"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceIeee80211wMaxTimeout"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceIeee80211wRetryTimeout"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceAcsList"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceNeighbourReport"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceNeighbourParameter"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceL2nat"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceL2natLearningMode"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceL2natDefaultDestination"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceTimeAdvertisement"),
        ("WESTERMO-SW6-MIB", "cfgWlanIfaceApIsolate"))
)
if mibBuilder.loadTexts:
    groupCfgWlanInterface.setStatus("current")

groupCfgWlanHandoff = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 3)
)
groupCfgWlanHandoff.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanHoIfaceName"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoProfile"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoScanningLevel"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoBeacons"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoRecovery"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoFilterMode"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoFilterLongX"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoFilterLongY"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoScanRateLimitTime"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoScanRateLimitTries"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoPassiveChanTime"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoLevelLow"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoLevelHigh"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoDistanceNear"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoDistanceFar"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoDistanceMeasurementPeriod"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoDistanceFilterX"),
        ("WESTERMO-SW6-MIB", "cfgWlanHoDistanceFilterY"))
)
if mibBuilder.loadTexts:
    groupCfgWlanHandoff.setStatus("current")

groupCfgWlanScanFreq = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 4)
)
groupCfgWlanScanFreq.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanFFreq0"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq1"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq2"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq3"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq4"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq5"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq6"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq7"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq8"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq9"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq10"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq11"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq12"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq13"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq14"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq15"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq16"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq17"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq18"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq19"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq20"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq21"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq22"),
        ("WESTERMO-SW6-MIB", "cfgWlanFFreq23"))
)
if mibBuilder.loadTexts:
    groupCfgWlanScanFreq.setStatus("current")

groupCfgWlanWme = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 5)
)
groupCfgWlanWme.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanWmeId"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeAc"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeCwMin"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeCwMax"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeAifs"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeTxOpMax"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeApCwMin"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeApCwMax"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeApAifs"),
        ("WESTERMO-SW6-MIB", "cfgWlanWmeApBurst"))
)
if mibBuilder.loadTexts:
    groupCfgWlanWme.setStatus("current")

groupCfgWlanDbg = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 6)
)
groupCfgWlanDbg.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanDbgIfaceName"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgHandoff"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgScan"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgMlme"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgEvents"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgBeaconrssi"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgAckrssi"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgBeaconfiltered"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgRatelimit"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgLinkmonitor"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgBeacontsf"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgRange"),
        ("WESTERMO-SW6-MIB", "cfgWlanDbgReports"))
)
if mibBuilder.loadTexts:
    groupCfgWlanDbg.setStatus("current")

groupCfgWlanAclBlack = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 7)
)
groupCfgWlanAclBlack.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanAclBlackEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlanAclBlackInterface"),
        ("WESTERMO-SW6-MIB", "cfgWlanAclBlackAddr"),
        ("WESTERMO-SW6-MIB", "cfgWlanAclBlackMask"))
)
if mibBuilder.loadTexts:
    groupCfgWlanAclBlack.setStatus("current")

groupCfgWlanAclWhite = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 8)
)
groupCfgWlanAclWhite.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanAclWhiteEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlanAclWhiteInterface"),
        ("WESTERMO-SW6-MIB", "cfgWlanAclWhiteAddr"),
        ("WESTERMO-SW6-MIB", "cfgWlanAclWhiteMask"))
)
if mibBuilder.loadTexts:
    groupCfgWlanAclWhite.setStatus("current")

groupCfgWlanGlobal = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 9)
)
groupCfgWlanGlobal.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanGlblCountry"),
        ("WESTERMO-SW6-MIB", "cfgWlanGlblLinkmonitorInterval"),
        ("WESTERMO-SW6-MIB", "cfgWlanGlblLinkmonitorQmrrlogging"),
        ("WESTERMO-SW6-MIB", "cfgWlanGlblConnectionStatusWlanInterface"))
)
if mibBuilder.loadTexts:
    groupCfgWlanGlobal.setStatus("current")

groupCfgWlan802dot1x = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 10)
)
groupCfgWlan802dot1x.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlan802dot1xName"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xOwnIpAddr"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAuthServerParameter"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAcctServerParameter"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xRetryPrimaryInterval"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xInterimAccountingInterval"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xNasId"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xEapType"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xIdentity"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xClientKeyPassword"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xTlsControlParams"))
)
if mibBuilder.loadTexts:
    groupCfgWlan802dot1x.setStatus("current")

groupCfgWlan802dot1xAuth = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 11)
)
groupCfgWlan802dot1xAuth.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlan802dot1xAuthSrvEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAuthSrvId"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAuthSrvIpAddr"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAuthSrvPort"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAuthSrvSharedSecret"))
)
if mibBuilder.loadTexts:
    groupCfgWlan802dot1xAuth.setStatus("current")

groupCfgWlan802dot1xAcct = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 12)
)
groupCfgWlan802dot1xAcct.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlan802dot1xAcctSrvEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAcctSrvId"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAcctSrvIpAddr"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAcctSrvPort"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot1xAcctSrvSharedSecret"))
)
if mibBuilder.loadTexts:
    groupCfgWlan802dot1xAcct.setStatus("current")

groupCfgWlan802dot11r = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 13)
)
groupCfgWlan802dot11r.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlan802dot11rName"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rMobilityDomain"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rPmkR0KeyHolderIdentifier"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rPmkR0Lifetime"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rPmkR1KeyHolderIdentifier"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rPmkR1Push"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR0KHParameter"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR1KHParameter"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rExpirationEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rExpirationTime"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rVlan"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR0KHId"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR0KHEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR0KHDestinationMac"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR0KHHID"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR0KHKey"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR1KHId"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR1KHEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR1KHDestinationMac"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR1KHHID"),
        ("WESTERMO-SW6-MIB", "cfgWlan802dot11rR1KHKey"))
)
if mibBuilder.loadTexts:
    groupCfgWlan802dot11r.setStatus("current")

groupCfgWlanNeighbour = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 3, 14)
)
groupCfgWlanNeighbour.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgWlanNeighbourId"),
        ("WESTERMO-SW6-MIB", "cfgWlanNeighbourEnabled"),
        ("WESTERMO-SW6-MIB", "cfgWlanNeighbourBSSID"),
        ("WESTERMO-SW6-MIB", "cfgWlanNeighbourFrequency"))
)
if mibBuilder.loadTexts:
    groupCfgWlanNeighbour.setStatus("current")

groupCfgRouteDefault = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 4, 1)
)
groupCfgRouteDefault.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgRouteDefGateway"),
        ("WESTERMO-SW6-MIB", "cfgRouteDefGwOverride"))
)
if mibBuilder.loadTexts:
    groupCfgRouteDefault.setStatus("current")

groupCfgRouteTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 4, 2)
)
groupCfgRouteTable.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgRouteTableDestinationNetwork"),
        ("WESTERMO-SW6-MIB", "cfgRouteTableGateway"),
        ("WESTERMO-SW6-MIB", "cfgRouteTableEnabled"),
        ("WESTERMO-SW6-MIB", "cfgRouteTableSource"),
        ("WESTERMO-SW6-MIB", "cfgRouteTableCarpId"))
)
if mibBuilder.loadTexts:
    groupCfgRouteTable.setStatus("current")

groupCfgMRouteTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 4, 3)
)
groupCfgMRouteTable.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgMRouteTableEnabled"),
        ("WESTERMO-SW6-MIB", "cfgMRouteTableInput"),
        ("WESTERMO-SW6-MIB", "cfgMRouteTableSource"),
        ("WESTERMO-SW6-MIB", "cfgMRouteTableGroup"),
        ("WESTERMO-SW6-MIB", "cfgMRouteTableOutput"))
)
if mibBuilder.loadTexts:
    groupCfgMRouteTable.setStatus("current")

groupCfgLogging = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 11)
)
groupCfgLogging.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgLogRemoteEnabled"),
        ("WESTERMO-SW6-MIB", "cfgLogRemoteLevel"),
        ("WESTERMO-SW6-MIB", "cfgLogRemoteProtocol"),
        ("WESTERMO-SW6-MIB", "cfgLogRemoteIp"),
        ("WESTERMO-SW6-MIB", "cfgLogRemotePort"))
)
if mibBuilder.loadTexts:
    groupCfgLogging.setStatus("current")

groupCfgSnmpd = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 12, 1)
)
groupCfgSnmpd.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgSnmpdLocation"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdContact"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdVersion"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdName"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdEnabled"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdAddress"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdComAdmin"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdComMaintainer"),
        ("WESTERMO-SW6-MIB", "cfgSnmpdComMonitor"))
)
if mibBuilder.loadTexts:
    groupCfgSnmpd.setStatus("current")

groupCfgSnmpTrap = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 12, 10)
)
groupCfgSnmpTrap.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgSnmpTrapEnabled"),
        ("WESTERMO-SW6-MIB", "cfgSnmpTrapVersion"),
        ("WESTERMO-SW6-MIB", "cfgSnmpTrapCommunity"),
        ("WESTERMO-SW6-MIB", "cfgSnmpTrapDest"))
)
if mibBuilder.loadTexts:
    groupCfgSnmpTrap.setStatus("current")

groupCfgDhcpGlobal = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 13, 1)
)
groupCfgDhcpGlobal.setObjects(
    ("WESTERMO-SW6-MIB", "cfgDhcpGlobalEnabled")
)
if mibBuilder.loadTexts:
    groupCfgDhcpGlobal.setStatus("current")

groupCfgDhcpDnsmasq = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 13, 2)
)
groupCfgDhcpDnsmasq.setObjects(
    ("WESTERMO-SW6-MIB", "cfgDhcpDnsmasqScopeParameter")
)
if mibBuilder.loadTexts:
    groupCfgDhcpDnsmasq.setStatus("current")

groupCfgDhcpScope = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 13, 3)
)
groupCfgDhcpScope.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgDhcpScopeId"),
        ("WESTERMO-SW6-MIB", "cfgDhcpScopeInterface"),
        ("WESTERMO-SW6-MIB", "cfgDhcpScopeStart"),
        ("WESTERMO-SW6-MIB", "cfgDhcpScopeLimit"),
        ("WESTERMO-SW6-MIB", "cfgDhcpScopeLeasetime"),
        ("WESTERMO-SW6-MIB", "cfgDhcpScopeGateway"),
        ("WESTERMO-SW6-MIB", "cfgDhcpScopeDnsServer1"),
        ("WESTERMO-SW6-MIB", "cfgDhcpScopeDnsServer2"))
)
if mibBuilder.loadTexts:
    groupCfgDhcpScope.setStatus("current")

groupCfgNtp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 14)
)
groupCfgNtp.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNtpEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNtpServer1"),
        ("WESTERMO-SW6-MIB", "cfgNtpServer2"))
)
if mibBuilder.loadTexts:
    groupCfgNtp.setStatus("current")

groupCfgHttp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 15)
)
groupCfgHttp.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgHttpUser"),
        ("WESTERMO-SW6-MIB", "cfgHttpPassword"),
        ("WESTERMO-SW6-MIB", "cfgHttpEnabled"),
        ("WESTERMO-SW6-MIB", "cfgHttpRedirectEnabled"),
        ("WESTERMO-SW6-MIB", "cfgHttpHttpAddress"),
        ("WESTERMO-SW6-MIB", "cfgHttpHttpsAddress"))
)
if mibBuilder.loadTexts:
    groupCfgHttp.setStatus("current")

groupCfgLldp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 16)
)
groupCfgLldp.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgLldpEnabled"),
        ("WESTERMO-SW6-MIB", "cfgLldpDescription"))
)
if mibBuilder.loadTexts:
    groupCfgLldp.setStatus("current")

groupCfgMdns = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 17)
)
groupCfgMdns.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgMdnsEnabled"),
        ("WESTERMO-SW6-MIB", "cfgMdnsNetwork"))
)
if mibBuilder.loadTexts:
    groupCfgMdns.setStatus("current")

groupCfgQosGlobal = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 18, 1)
)
groupCfgQosGlobal.setObjects(
    ("WESTERMO-SW6-MIB", "cfgQosL3PrioEnabled")
)
if mibBuilder.loadTexts:
    groupCfgQosGlobal.setStatus("current")

groupCfgQosDscpToTidMapTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 18, 2)
)
groupCfgQosDscpToTidMapTable.setObjects(
    ("WESTERMO-SW6-MIB", "cfgQosDscpToTidMapValue")
)
if mibBuilder.loadTexts:
    groupCfgQosDscpToTidMapTable.setStatus("current")

groupCfgQosVlanToTidMapTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 18, 3)
)
groupCfgQosVlanToTidMapTable.setObjects(
    ("WESTERMO-SW6-MIB", "cfgQosVlanToTidMapValue")
)
if mibBuilder.loadTexts:
    groupCfgQosVlanToTidMapTable.setStatus("current")

groupCfgQosIpToTidMapTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 18, 4)
)
groupCfgQosIpToTidMapTable.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgQosIpToTidMapSrcNet"),
        ("WESTERMO-SW6-MIB", "cfgQosIpToTidMapDestNet"),
        ("WESTERMO-SW6-MIB", "cfgQosIpToTidMapProto"),
        ("WESTERMO-SW6-MIB", "cfgQosIpToTidMapSrcPort"),
        ("WESTERMO-SW6-MIB", "cfgQosIpToTidMapDestPort"),
        ("WESTERMO-SW6-MIB", "cfgQosIpToTidMapPrecedence"),
        ("WESTERMO-SW6-MIB", "cfgQosIpToTidMapEnabled"))
)
if mibBuilder.loadTexts:
    groupCfgQosIpToTidMapTable.setStatus("current")

groupCfgNlm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 40)
)
groupCfgNlm.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgNlmGlblEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonEnabled"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonInterval"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonCount"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonType"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonInterfaces"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonDestination"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonUpAction"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonDownAction"),
        ("WESTERMO-SW6-MIB", "cfgNlmMonScanLoopInterval"))
)
if mibBuilder.loadTexts:
    groupCfgNlm.setStatus("current")

groupCfgCli = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 100)
)
groupCfgCli.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgCliEnabled"),
        ("WESTERMO-SW6-MIB", "cfgCliUsername"),
        ("WESTERMO-SW6-MIB", "cfgCliPassword"),
        ("WESTERMO-SW6-MIB", "cfgCliTelnetEnabled"),
        ("WESTERMO-SW6-MIB", "cfgCliSshEnabled"),
        ("WESTERMO-SW6-MIB", "cfgCliTelnetAddress"),
        ("WESTERMO-SW6-MIB", "cfgCliSshAddress"))
)
if mibBuilder.loadTexts:
    groupCfgCli.setStatus("current")

groupCfgCellSim = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 1, 101, 1)
)
groupCfgCellSim.setObjects(
      *(("WESTERMO-SW6-MIB", "cfgCellSimApn"),
        ("WESTERMO-SW6-MIB", "cfgCellSimUsername"),
        ("WESTERMO-SW6-MIB", "cfgCellSimPassword"),
        ("WESTERMO-SW6-MIB", "cfgCellSimPinEnabled"),
        ("WESTERMO-SW6-MIB", "cfgCellSimPin"),
        ("WESTERMO-SW6-MIB", "cfgCellSimAuthType"))
)
if mibBuilder.loadTexts:
    groupCfgCellSim.setStatus("current")

groupRpcConfiguration = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 3, 1)
)
groupRpcConfiguration.setObjects(
      *(("WESTERMO-SW6-MIB", "rpcCfgRevert"),
        ("WESTERMO-SW6-MIB", "rpcCfgApply"),
        ("WESTERMO-SW6-MIB", "rpcCfgFile"))
)
if mibBuilder.loadTexts:
    groupRpcConfiguration.setStatus("current")

groupRpcFirmware = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 3, 2)
)
groupRpcFirmware.setObjects(
    ("WESTERMO-SW6-MIB", "rpcFwFlash")
)
if mibBuilder.loadTexts:
    groupRpcFirmware.setStatus("current")

groupRpcSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 3, 3)
)
groupRpcSystem.setObjects(
      *(("WESTERMO-SW6-MIB", "rpcSysReboot"),
        ("WESTERMO-SW6-MIB", "rpcSysFactoryReset"),
        ("WESTERMO-SW6-MIB", "rpcSysErrorReset"),
        ("WESTERMO-SW6-MIB", "rpcSysKernelLogReset"))
)
if mibBuilder.loadTexts:
    groupRpcSystem.setStatus("current")

groupRpcCertificate = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 3, 4)
)
groupRpcCertificate.setObjects(
    ("WESTERMO-SW6-MIB", "rpcCrtFile")
)
if mibBuilder.loadTexts:
    groupRpcCertificate.setStatus("current")

groupRpcDriver = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 3, 6)
)
groupRpcDriver.setObjects(
      *(("WESTERMO-SW6-MIB", "rpcDrvName"),
        ("WESTERMO-SW6-MIB", "rpcDrvDfsSimulateRadar"))
)
if mibBuilder.loadTexts:
    groupRpcDriver.setStatus("current")

groupSetConfigurationFile = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4, 1)
)
groupSetConfigurationFile.setObjects(
    ("WESTERMO-SW6-MIB", "setCfgFileUrl")
)
if mibBuilder.loadTexts:
    groupSetConfigurationFile.setStatus("current")

groupSetWireless = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4, 3)
)
groupSetWireless.setObjects(
      *(("WESTERMO-SW6-MIB", "setWlanDevName"),
        ("WESTERMO-SW6-MIB", "setWlanDevRfOutput"),
        ("WESTERMO-SW6-MIB", "setWlanDevFrequency"),
        ("WESTERMO-SW6-MIB", "setWlanDevPower"))
)
if mibBuilder.loadTexts:
    groupSetWireless.setStatus("current")

groupSetWlanDbg = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4, 4)
)
groupSetWlanDbg.setObjects(
      *(("WESTERMO-SW6-MIB", "setWlanDbgIfaceName"),
        ("WESTERMO-SW6-MIB", "setWlanDbgHandoff"),
        ("WESTERMO-SW6-MIB", "setWlanDbgScan"),
        ("WESTERMO-SW6-MIB", "setWlanDbgMlme"),
        ("WESTERMO-SW6-MIB", "setWlanDbgEvents"),
        ("WESTERMO-SW6-MIB", "setWlanDbgBeaconrssi"),
        ("WESTERMO-SW6-MIB", "setWlanDbgAckrssi"),
        ("WESTERMO-SW6-MIB", "setWlanDbgBeaconfiltered"),
        ("WESTERMO-SW6-MIB", "setWlanDbgRatelimit"),
        ("WESTERMO-SW6-MIB", "setWlanDbgBeacontsf"),
        ("WESTERMO-SW6-MIB", "setWlanDbgRange"),
        ("WESTERMO-SW6-MIB", "setWlanDbgReports"))
)
if mibBuilder.loadTexts:
    groupSetWlanDbg.setStatus("current")

groupSetConfmgmtd = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4, 5)
)
groupSetConfmgmtd.setObjects(
    ("WESTERMO-SW6-MIB", "setCfgdLogLevel")
)
if mibBuilder.loadTexts:
    groupSetConfmgmtd.setStatus("current")

groupSetFirmware = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4, 6)
)
groupSetFirmware.setObjects(
      *(("WESTERMO-SW6-MIB", "setFwFileUrl"),
        ("WESTERMO-SW6-MIB", "setFwKeepConfig"))
)
if mibBuilder.loadTexts:
    groupSetFirmware.setStatus("current")

groupSetCertificate = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4, 7)
)
groupSetCertificate.setObjects(
      *(("WESTERMO-SW6-MIB", "setCrtFileUrl"),
        ("WESTERMO-SW6-MIB", "setCrtFileSelector"),
        ("WESTERMO-SW6-MIB", "setCrtFileFormat"),
        ("WESTERMO-SW6-MIB", "setCrtFilePkcs12Passphrase"))
)
if mibBuilder.loadTexts:
    groupSetCertificate.setStatus("current")

groupSetSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 4, 8)
)
groupSetSystem.setObjects(
    ("WESTERMO-SW6-MIB", "setSysTime")
)
if mibBuilder.loadTexts:
    groupSetSystem.setStatus("current")

groupHwSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 5, 1)
)
groupHwSystem.setObjects(
      *(("WESTERMO-SW6-MIB", "hwSysProduct"),
        ("WESTERMO-SW6-MIB", "hwSysSerial"),
        ("WESTERMO-SW6-MIB", "hwSysRevision"),
        ("WESTERMO-SW6-MIB", "hwSysVersion"))
)
if mibBuilder.loadTexts:
    groupHwSystem.setStatus("current")

groupHwNetwork = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 5, 2)
)
groupHwNetwork.setObjects(
      *(("WESTERMO-SW6-MIB", "hwNetEthName"),
        ("WESTERMO-SW6-MIB", "hwNetEthAssembled"),
        ("WESTERMO-SW6-MIB", "hwNetEthMacAddress"),
        ("WESTERMO-SW6-MIB", "hwNetEthOperation"),
        ("WESTERMO-SW6-MIB", "hwNetEthSpeed"),
        ("WESTERMO-SW6-MIB", "hwNetEthHwIndex"))
)
if mibBuilder.loadTexts:
    groupHwNetwork.setStatus("current")

groupHwWireless = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 5, 3)
)
groupHwWireless.setObjects(
      *(("WESTERMO-SW6-MIB", "hwWlanDevAssembled"),
        ("WESTERMO-SW6-MIB", "hwWlanDevType"),
        ("WESTERMO-SW6-MIB", "hwWlanDevSerial"),
        ("WESTERMO-SW6-MIB", "hwWlanDevRevision"),
        ("WESTERMO-SW6-MIB", "hwWlanDevVersion"),
        ("WESTERMO-SW6-MIB", "hwWlanDevPcbId"),
        ("WESTERMO-SW6-MIB", "hwWlanDevAssemblyId"),
        ("WESTERMO-SW6-MIB", "hwWlanDevMacAddress"),
        ("WESTERMO-SW6-MIB", "hwWlanDevAntennaProfileId"),
        ("WESTERMO-SW6-MIB", "hwWlanDevAntennaGain"),
        ("WESTERMO-SW6-MIB", "hwWlanDevCableLoss"),
        ("WESTERMO-SW6-MIB", "hwWlanGlblRegulatoryRegionId"))
)
if mibBuilder.loadTexts:
    groupHwWireless.setStatus("current")

groupHwBaseBoard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 5, 4)
)
groupHwBaseBoard.setObjects(
      *(("WESTERMO-SW6-MIB", "hwBbType"),
        ("WESTERMO-SW6-MIB", "hwBbSerial"),
        ("WESTERMO-SW6-MIB", "hwBbRevision"),
        ("WESTERMO-SW6-MIB", "hwBbVersion"),
        ("WESTERMO-SW6-MIB", "hwBbPcbId"),
        ("WESTERMO-SW6-MIB", "hwBbAssemblyId"))
)
if mibBuilder.loadTexts:
    groupHwBaseBoard.setStatus("current")

groupHwIfaceBoard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 5, 5)
)
groupHwIfaceBoard.setObjects(
      *(("WESTERMO-SW6-MIB", "hwIfBrdAssembled"),
        ("WESTERMO-SW6-MIB", "hwIfBrdType"),
        ("WESTERMO-SW6-MIB", "hwIfBrdSerial"),
        ("WESTERMO-SW6-MIB", "hwIfBrdRevision"),
        ("WESTERMO-SW6-MIB", "hwIfBrdVersion"),
        ("WESTERMO-SW6-MIB", "hwIfBrdPcbId"),
        ("WESTERMO-SW6-MIB", "hwIfBrdAssemblyId"))
)
if mibBuilder.loadTexts:
    groupHwIfaceBoard.setStatus("current")

groupHwSensor = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 5, 7)
)
groupHwSensor.setObjects(
      *(("WESTERMO-SW6-MIB", "hwSensorName"),
        ("WESTERMO-SW6-MIB", "hwSensorUnit"),
        ("WESTERMO-SW6-MIB", "hwSensorValue"))
)
if mibBuilder.loadTexts:
    groupHwSensor.setStatus("current")

groupSwFirmware = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 1)
)
groupSwFirmware.setObjects(
      *(("WESTERMO-SW6-MIB", "swFwName"),
        ("WESTERMO-SW6-MIB", "swFwVersion"),
        ("WESTERMO-SW6-MIB", "swFwRevision"))
)
if mibBuilder.loadTexts:
    groupSwFirmware.setStatus("current")

groupSwSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 2)
)
groupSwSystem.setObjects(
      *(("WESTERMO-SW6-MIB", "swSysRebootReason"),
        ("WESTERMO-SW6-MIB", "swSysBootStatus"),
        ("WESTERMO-SW6-MIB", "swSysMsgPriority"),
        ("WESTERMO-SW6-MIB", "swSysMsgCode"),
        ("WESTERMO-SW6-MIB", "swSysMsgText"))
)
if mibBuilder.loadTexts:
    groupSwSystem.setStatus("current")

groupSwOperatingSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 3)
)
groupSwOperatingSystem.setObjects(
      *(("WESTERMO-SW6-MIB", "swOsName"),
        ("WESTERMO-SW6-MIB", "swOsVersion"),
        ("WESTERMO-SW6-MIB", "swOsRevision"),
        ("WESTERMO-SW6-MIB", "swOsUptime"))
)
if mibBuilder.loadTexts:
    groupSwOperatingSystem.setStatus("current")

groupSwDrvDfs = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 4)
)
groupSwDrvDfs.setObjects(
      *(("WESTERMO-SW6-MIB", "swDrvDfsName"),
        ("WESTERMO-SW6-MIB", "swDrvDfsPulsesDetected"),
        ("WESTERMO-SW6-MIB", "swDrvDfsPulsesProcessed"),
        ("WESTERMO-SW6-MIB", "swDrvDfsRadarDetected"))
)
if mibBuilder.loadTexts:
    groupSwDrvDfs.setStatus("current")

groupSwDrvCntWlanMac = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 7)
)
groupSwDrvCntWlanMac.setObjects(
      *(("WESTERMO-SW6-MIB", "swDrvCntWlanMacName"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxHandlersDrop"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxHandlersQueued"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxHandlersDropUnencrypted"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxHandlersDropFragment"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxHandlersDropWep"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxHandlersDropNotAssoc"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxHandlersDropUnauthPort"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxHandlersDrop"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxHandlersQueued"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxHandlersDropNullfunc"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxHandlersDropDefrag"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxHandlersDropShort"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxExpandSkbHead"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxExpandSkbHeadCloned"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxExpandSkbHead"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxExpandSkbHead2"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacRxHandlersFragments"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanMacTxstatusDrop"))
)
if mibBuilder.loadTexts:
    groupSwDrvCntWlanMac.setStatus("current")

groupSwDrvCntWlanWmm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 8)
)
groupSwDrvCntWlanWmm.setObjects(
      *(("WESTERMO-SW6-MIB", "swDrvCntWlanWmmName"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanWmmTx"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanWmmRx"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanWmmShortRetries"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanWmmLongRetries"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanWmmExceededRetries"))
)
if mibBuilder.loadTexts:
    groupSwDrvCntWlanWmm.setStatus("current")

groupSwDrvConStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 9)
)
groupSwDrvConStat.setObjects(
      *(("WESTERMO-SW6-MIB", "swDrvConStatWlanName"),
        ("WESTERMO-SW6-MIB", "swDrvConStatMacName"),
        ("WESTERMO-SW6-MIB", "swDrvConStatRxBrExtra"),
        ("WESTERMO-SW6-MIB", "swDrvConStatRxBrType"),
        ("WESTERMO-SW6-MIB", "swDrvConStatRxBrValue"),
        ("WESTERMO-SW6-MIB", "swDrvConStatRxBytes"),
        ("WESTERMO-SW6-MIB", "swDrvConStatRxPackets"),
        ("WESTERMO-SW6-MIB", "swDrvConStatTxBrExtra"),
        ("WESTERMO-SW6-MIB", "swDrvConStatTxBrType"),
        ("WESTERMO-SW6-MIB", "swDrvConStatTxBrValue"),
        ("WESTERMO-SW6-MIB", "swDrvConStatTxBytes"),
        ("WESTERMO-SW6-MIB", "swDrvConStatTxPackets"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigChain0"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigChain1"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigChain2"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigAvgChain0"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigAvgChain1"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigAvgChain2"),
        ("WESTERMO-SW6-MIB", "swDrvConStatTxRetries"),
        ("WESTERMO-SW6-MIB", "swDrvConStatTxFailed"),
        ("WESTERMO-SW6-MIB", "swDrvConStatCacheNo"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigCombined"),
        ("WESTERMO-SW6-MIB", "swDrvConStatSigAvgCombined"),
        ("WESTERMO-SW6-MIB", "swDrvConStatWlanIf"))
)
if mibBuilder.loadTexts:
    groupSwDrvConStat.setStatus("current")

groupSwDrvCntWlanTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 10)
)
groupSwDrvCntWlanTable.setObjects(
      *(("WESTERMO-SW6-MIB", "swDrvCntWlanName"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanAssocSuccess"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanAssocFailure"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanAssocFailureMaxSta"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanNumAssocSta"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanEapAuthStarted"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanEapAuthFailed"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanChannelActive"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanChannelBusy"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanChannelTransmit"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanChannelReceive"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanChannelNoise"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanEapAuthStartedFT"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanEapAuthStartedFILS"),
        ("WESTERMO-SW6-MIB", "swDrvCntWlanEapAuthStartedPKMSA"))
)
if mibBuilder.loadTexts:
    groupSwDrvCntWlanTable.setStatus("current")

groupSwRdm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 11)
)
groupSwRdm.setObjects(
      *(("WESTERMO-SW6-MIB", "swRdmMaxEirp"),
        ("WESTERMO-SW6-MIB", "swRdmMaxApp"))
)
if mibBuilder.loadTexts:
    groupSwRdm.setStatus("current")

groupSwBootloader = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 20)
)
groupSwBootloader.setObjects(
      *(("WESTERMO-SW6-MIB", "swBootName"),
        ("WESTERMO-SW6-MIB", "swBootVersion"),
        ("WESTERMO-SW6-MIB", "swBootBuildDate"))
)
if mibBuilder.loadTexts:
    groupSwBootloader.setStatus("current")

groupSwConfiguration = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 1, 6, 30)
)
groupSwConfiguration.setObjects(
    ("WESTERMO-SW6-MIB", "swCfgChangesCount")
)
if mibBuilder.loadTexts:
    groupSwConfiguration.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 1, 100, 2, 1)
)
compliance.setObjects(
      *(("WESTERMO-SW6-MIB", "groupCfgSystem"),
        ("WESTERMO-SW6-MIB", "groupCfgNetEthernet"),
        ("WESTERMO-SW6-MIB", "groupCfgNetWlan"),
        ("WESTERMO-SW6-MIB", "groupCfgNetVlan"),
        ("WESTERMO-SW6-MIB", "groupCfgNetIp"),
        ("WESTERMO-SW6-MIB", "groupCfgNetCarp"),
        ("WESTERMO-SW6-MIB", "groupCfgNetMacVLan"),
        ("WESTERMO-SW6-MIB", "groupCfgNetWwan"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanDevice"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanInterface"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanHandoff"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanScanFreq"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanWme"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanDbg"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanAclBlack"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanAclWhite"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanGlobal"),
        ("WESTERMO-SW6-MIB", "groupCfgWlan802dot1x"),
        ("WESTERMO-SW6-MIB", "groupCfgWlan802dot1xAuth"),
        ("WESTERMO-SW6-MIB", "groupCfgWlan802dot1xAcct"),
        ("WESTERMO-SW6-MIB", "groupCfgWlan802dot11r"),
        ("WESTERMO-SW6-MIB", "groupCfgWlanNeighbour"),
        ("WESTERMO-SW6-MIB", "groupCfgRouteDefault"),
        ("WESTERMO-SW6-MIB", "groupCfgRouteTable"),
        ("WESTERMO-SW6-MIB", "groupCfgMRouteTable"),
        ("WESTERMO-SW6-MIB", "groupCfgLogging"),
        ("WESTERMO-SW6-MIB", "groupCfgSnmpd"),
        ("WESTERMO-SW6-MIB", "groupCfgSnmpTrap"),
        ("WESTERMO-SW6-MIB", "groupCfgDhcpGlobal"),
        ("WESTERMO-SW6-MIB", "groupCfgDhcpDnsmasq"),
        ("WESTERMO-SW6-MIB", "groupCfgDhcpScope"),
        ("WESTERMO-SW6-MIB", "groupCfgNtp"),
        ("WESTERMO-SW6-MIB", "groupCfgHttp"),
        ("WESTERMO-SW6-MIB", "groupCfgLldp"),
        ("WESTERMO-SW6-MIB", "groupCfgMdns"),
        ("WESTERMO-SW6-MIB", "groupCfgQos"),
        ("WESTERMO-SW6-MIB", "groupCfgQosGlobal"),
        ("WESTERMO-SW6-MIB", "groupCfgQosDscpToTidMapTable"),
        ("WESTERMO-SW6-MIB", "groupCfgQosVlanToTidMapTable"),
        ("WESTERMO-SW6-MIB", "groupCfgQosIpToTidMapTable"),
        ("WESTERMO-SW6-MIB", "groupCfgNlm"),
        ("WESTERMO-SW6-MIB", "groupCfgCli"),
        ("WESTERMO-SW6-MIB", "groupCfgCellSim"),
        ("WESTERMO-SW6-MIB", "groupRpcConfiguration"),
        ("WESTERMO-SW6-MIB", "groupRpcFirmware"),
        ("WESTERMO-SW6-MIB", "groupRpcSystem"),
        ("WESTERMO-SW6-MIB", "groupRpcCertificate"),
        ("WESTERMO-SW6-MIB", "groupRpcDriver"),
        ("WESTERMO-SW6-MIB", "groupSetConfigurationFile"),
        ("WESTERMO-SW6-MIB", "groupSetWireless"),
        ("WESTERMO-SW6-MIB", "groupSetWlanDbg"),
        ("WESTERMO-SW6-MIB", "groupSetConfmgmtd"),
        ("WESTERMO-SW6-MIB", "groupSetFirmware"),
        ("WESTERMO-SW6-MIB", "groupSetCertificate"),
        ("WESTERMO-SW6-MIB", "groupSetSystem"),
        ("WESTERMO-SW6-MIB", "groupHwSystem"),
        ("WESTERMO-SW6-MIB", "groupHwNetwork"),
        ("WESTERMO-SW6-MIB", "groupHwWireless"),
        ("WESTERMO-SW6-MIB", "groupHwBaseBoard"),
        ("WESTERMO-SW6-MIB", "groupHwIfaceBoard"),
        ("WESTERMO-SW6-MIB", "groupHwSensor"),
        ("WESTERMO-SW6-MIB", "groupSwFirmware"),
        ("WESTERMO-SW6-MIB", "groupSwSystem"),
        ("WESTERMO-SW6-MIB", "groupSwOperatingSystem"),
        ("WESTERMO-SW6-MIB", "groupSwDrvDfs"),
        ("WESTERMO-SW6-MIB", "groupSwDrvCntWlanMac"),
        ("WESTERMO-SW6-MIB", "groupSwDrvCntWlanWmm"),
        ("WESTERMO-SW6-MIB", "groupSwDrvConStat"),
        ("WESTERMO-SW6-MIB", "groupSwDrvCntWlanTable"),
        ("WESTERMO-SW6-MIB", "groupSwRdm"),
        ("WESTERMO-SW6-MIB", "groupSwBootloader"),
        ("WESTERMO-SW6-MIB", "groupSwConfiguration"))
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-SW6-MIB",
    **{"base": base,
       "configuration": configuration,
       "cfgSystem": cfgSystem,
       "cfgSysHostname": cfgSysHostname,
       "cfgSysTimezone": cfgSysTimezone,
       "cfgNetwork": cfgNetwork,
       "cfgNetEthernetTable": cfgNetEthernetTable,
       "cfgNetEthernetTableEntry": cfgNetEthernetTableEntry,
       "cfgNetEthIndex": cfgNetEthIndex,
       "cfgNetEthName": cfgNetEthName,
       "cfgNetEthEnabled": cfgNetEthEnabled,
       "cfgNetEthBridge": cfgNetEthBridge,
       "cfgNetEthAutoneg": cfgNetEthAutoneg,
       "cfgNetEthSpeed": cfgNetEthSpeed,
       "cfgNetEthTrunk": cfgNetEthTrunk,
       "cfgNetEthTag": cfgNetEthTag,
       "cfgNetEthVlanMode": cfgNetEthVlanMode,
       "cfgNetEthLldpEnabled": cfgNetEthLldpEnabled,
       "cfgNetWlanTable": cfgNetWlanTable,
       "cfgNetWlanTableEntry": cfgNetWlanTableEntry,
       "cfgNetWlanIndex": cfgNetWlanIndex,
       "cfgNetWlanName": cfgNetWlanName,
       "cfgNetWlanEnabled": cfgNetWlanEnabled,
       "cfgNetWlanBridge": cfgNetWlanBridge,
       "cfgNetWlanTrunk": cfgNetWlanTrunk,
       "cfgNetWlanTag": cfgNetWlanTag,
       "cfgNetWlanVlanMode": cfgNetWlanVlanMode,
       "cfgNetWlanLldpEnabled": cfgNetWlanLldpEnabled,
       "cfgNetVlanTable": cfgNetVlanTable,
       "cfgNetVlanTableEntry": cfgNetVlanTableEntry,
       "cfgNetVlanIndex": cfgNetVlanIndex,
       "cfgNetVlanName": cfgNetVlanName,
       "cfgNetVlanEnabled": cfgNetVlanEnabled,
       "cfgNetVlanBridge": cfgNetVlanBridge,
       "cfgNetVlanParent": cfgNetVlanParent,
       "cfgNetVlanVid": cfgNetVlanVid,
       "cfgNetIpTable": cfgNetIpTable,
       "cfgNetIpTableEntry": cfgNetIpTableEntry,
       "cfgNetIpIndex": cfgNetIpIndex,
       "cfgNetIpEnabled": cfgNetIpEnabled,
       "cfgNetIpAddr": cfgNetIpAddr,
       "cfgNetIpProto": cfgNetIpProto,
       "cfgNetIpInterface": cfgNetIpInterface,
       "cfgNetIpCarpId": cfgNetIpCarpId,
       "cfgNetCarpTable": cfgNetCarpTable,
       "cfgNetCarpTableEntry": cfgNetCarpTableEntry,
       "cfgNetCarpIndex": cfgNetCarpIndex,
       "cfgNetCarpEnabled": cfgNetCarpEnabled,
       "cfgNetCarpVhid": cfgNetCarpVhid,
       "cfgNetCarpPassword": cfgNetCarpPassword,
       "cfgNetCarpAdvbase": cfgNetCarpAdvbase,
       "cfgNetCarpAdvskew": cfgNetCarpAdvskew,
       "cfgNetCarpAdvdivider": cfgNetCarpAdvdivider,
       "cfgNetCarpRatio": cfgNetCarpRatio,
       "cfgNetCarpPreempt": cfgNetCarpPreempt,
       "cfgNetCarpPreemptdemote": cfgNetCarpPreemptdemote,
       "cfgNetCarpLocalInterfaceGroup": cfgNetCarpLocalInterfaceGroup,
       "cfgNetCarpSyncInterface": cfgNetCarpSyncInterface,
       "cfgNetCarpMcastIp": cfgNetCarpMcastIp,
       "cfgNetMacVlanTable": cfgNetMacVlanTable,
       "cfgNetMacVlanTableEntry": cfgNetMacVlanTableEntry,
       "cfgNetMacVlanIndex": cfgNetMacVlanIndex,
       "cfgNetMacVlanName": cfgNetMacVlanName,
       "cfgNetMacVlanEnabled": cfgNetMacVlanEnabled,
       "cfgNetMacVlanParent": cfgNetMacVlanParent,
       "cfgNetMacVlanMac": cfgNetMacVlanMac,
       "cfgNetWwanTable": cfgNetWwanTable,
       "cfgNetWwanTableEntry": cfgNetWwanTableEntry,
       "cfgNetWwanIndex": cfgNetWwanIndex,
       "cfgNetWwanName": cfgNetWwanName,
       "cfgNetWwanEnabled": cfgNetWwanEnabled,
       "cfgNetWwanPrimarySim": cfgNetWwanPrimarySim,
       "cfgNetWwanSecondarySim": cfgNetWwanSecondarySim,
       "cfgWireless": cfgWireless,
       "cfgWlanDeviceTable": cfgWlanDeviceTable,
       "cfgWlanDeviceTableEntry": cfgWlanDeviceTableEntry,
       "cfgWlanDevIndex": cfgWlanDevIndex,
       "cfgWlanDevName": cfgWlanDevName,
       "cfgWlanDevModulation": cfgWlanDevModulation,
       "cfgWlanDevBandwidth": cfgWlanDevBandwidth,
       "cfgWlanDevFrequency": cfgWlanDevFrequency,
       "cfgWlanDevPower": cfgWlanDevPower,
       "cfgWlanDevDistance": cfgWlanDevDistance,
       "cfgWlanDevRts": cfgWlanDevRts,
       "cfgWlanDevFragments": cfgWlanDevFragments,
       "cfgWlanDevShortRetry": cfgWlanDevShortRetry,
       "cfgWlanDevLongRetry": cfgWlanDevLongRetry,
       "cfgWlanDevAntennaGain": cfgWlanDevAntennaGain,
       "cfgWlanDevTxAntenna": cfgWlanDevTxAntenna,
       "cfgWlanDevRxAntenna": cfgWlanDevRxAntenna,
       "cfgWlanDevPhy": cfgWlanDevPhy,
       "cfgWlanDevHtCapabilities": cfgWlanDevHtCapabilities,
       "cfgWlanDevQmrrString": cfgWlanDevQmrrString,
       "cfgWlanInterfaceTable": cfgWlanInterfaceTable,
       "cfgWlanInterfaceTableEntry": cfgWlanInterfaceTableEntry,
       "cfgWlanIfaceIndex": cfgWlanIfaceIndex,
       "cfgWlanIfaceName": cfgWlanIfaceName,
       "cfgWlanIfaceDevice": cfgWlanIfaceDevice,
       "cfgWlanIfaceMode": cfgWlanIfaceMode,
       "cfgWlanIfaceSsid": cfgWlanIfaceSsid,
       "cfgWlanIfaceEncryption": cfgWlanIfaceEncryption,
       "cfgWlanIfacePassword": cfgWlanIfacePassword,
       "cfgWlanIfacePassiveScanning": cfgWlanIfacePassiveScanning,
       "cfgWlanIfaceBeaconMiss": cfgWlanIfaceBeaconMiss,
       "cfgWlanIfaceDtim": cfgWlanIfaceDtim,
       "cfgWlanIfaceBitrates": cfgWlanIfaceBitrates,
       "cfgWlanIfaceBeaconInterval": cfgWlanIfaceBeaconInterval,
       "cfgWlanIfaceWmeParameter": cfgWlanIfaceWmeParameter,
       "cfgWlanIfaceWmeEnabled": cfgWlanIfaceWmeEnabled,
       "cfgWlanIfaceScanList": cfgWlanIfaceScanList,
       "cfgWlanIfaceIgnoreBroadcastSsid": cfgWlanIfaceIgnoreBroadcastSsid,
       "cfgWlanIfaceMacaddrAcl": cfgWlanIfaceMacaddrAcl,
       "cfgWlanIfaceMaxNumSta": cfgWlanIfaceMaxNumSta,
       "cfgWlanIfaceBssid": cfgWlanIfaceBssid,
       "cfgWlanIfaceLegacyRates": cfgWlanIfaceLegacyRates,
       "cfgWlanIface4addr": cfgWlanIface4addr,
       "cfgWlanIfaceInactivityTimeout": cfgWlanIfaceInactivityTimeout,
       "cfgWlanIfaceUseVendorSsid": cfgWlanIfaceUseVendorSsid,
       "cfgWlanIfaceIeee80211w": cfgWlanIfaceIeee80211w,
       "cfgWlanIfaceIeee80211wMaxTimeout": cfgWlanIfaceIeee80211wMaxTimeout,
       "cfgWlanIfaceIeee80211wRetryTimeout": cfgWlanIfaceIeee80211wRetryTimeout,
       "cfgWlanIfaceAcsList": cfgWlanIfaceAcsList,
       "cfgWlanIfaceNeighbourReport": cfgWlanIfaceNeighbourReport,
       "cfgWlanIfaceNeighbourParameter": cfgWlanIfaceNeighbourParameter,
       "cfgWlanIfaceL2nat": cfgWlanIfaceL2nat,
       "cfgWlanIfaceL2natLearningMode": cfgWlanIfaceL2natLearningMode,
       "cfgWlanIfaceL2natDefaultDestination": cfgWlanIfaceL2natDefaultDestination,
       "cfgWlanIfaceTimeAdvertisement": cfgWlanIfaceTimeAdvertisement,
       "cfgWlanIfaceApIsolate": cfgWlanIfaceApIsolate,
       "cfgWlanHandoffTable": cfgWlanHandoffTable,
       "cfgWlanHandoffTableEntry": cfgWlanHandoffTableEntry,
       "cfgWlanHoIndex": cfgWlanHoIndex,
       "cfgWlanHoIfaceName": cfgWlanHoIfaceName,
       "cfgWlanHoProfile": cfgWlanHoProfile,
       "cfgWlanHoScanningLevel": cfgWlanHoScanningLevel,
       "cfgWlanHoBeacons": cfgWlanHoBeacons,
       "cfgWlanHoRecovery": cfgWlanHoRecovery,
       "cfgWlanHoFilterMode": cfgWlanHoFilterMode,
       "cfgWlanHoFilterLongX": cfgWlanHoFilterLongX,
       "cfgWlanHoFilterLongY": cfgWlanHoFilterLongY,
       "cfgWlanHoScanRateLimitTime": cfgWlanHoScanRateLimitTime,
       "cfgWlanHoScanRateLimitTries": cfgWlanHoScanRateLimitTries,
       "cfgWlanHoPassiveChanTime": cfgWlanHoPassiveChanTime,
       "cfgWlanHoLevelLow": cfgWlanHoLevelLow,
       "cfgWlanHoLevelHigh": cfgWlanHoLevelHigh,
       "cfgWlanHoDistanceNear": cfgWlanHoDistanceNear,
       "cfgWlanHoDistanceFar": cfgWlanHoDistanceFar,
       "cfgWlanHoDistanceMeasurementPeriod": cfgWlanHoDistanceMeasurementPeriod,
       "cfgWlanHoDistanceFilterX": cfgWlanHoDistanceFilterX,
       "cfgWlanHoDistanceFilterY": cfgWlanHoDistanceFilterY,
       "cfgWlanFreqTable": cfgWlanFreqTable,
       "cfgWlanFreqTableEntry": cfgWlanFreqTableEntry,
       "cfgWlanFIndex": cfgWlanFIndex,
       "cfgWlanFFreq0": cfgWlanFFreq0,
       "cfgWlanFFreq1": cfgWlanFFreq1,
       "cfgWlanFFreq2": cfgWlanFFreq2,
       "cfgWlanFFreq3": cfgWlanFFreq3,
       "cfgWlanFFreq4": cfgWlanFFreq4,
       "cfgWlanFFreq5": cfgWlanFFreq5,
       "cfgWlanFFreq6": cfgWlanFFreq6,
       "cfgWlanFFreq7": cfgWlanFFreq7,
       "cfgWlanFFreq8": cfgWlanFFreq8,
       "cfgWlanFFreq9": cfgWlanFFreq9,
       "cfgWlanFFreq10": cfgWlanFFreq10,
       "cfgWlanFFreq11": cfgWlanFFreq11,
       "cfgWlanFFreq12": cfgWlanFFreq12,
       "cfgWlanFFreq13": cfgWlanFFreq13,
       "cfgWlanFFreq14": cfgWlanFFreq14,
       "cfgWlanFFreq15": cfgWlanFFreq15,
       "cfgWlanFFreq16": cfgWlanFFreq16,
       "cfgWlanFFreq17": cfgWlanFFreq17,
       "cfgWlanFFreq18": cfgWlanFFreq18,
       "cfgWlanFFreq19": cfgWlanFFreq19,
       "cfgWlanFFreq20": cfgWlanFFreq20,
       "cfgWlanFFreq21": cfgWlanFFreq21,
       "cfgWlanFFreq22": cfgWlanFFreq22,
       "cfgWlanFFreq23": cfgWlanFFreq23,
       "cfgWlanWmeTable": cfgWlanWmeTable,
       "cfgWlanWmeTableEntry": cfgWlanWmeTableEntry,
       "cfgWlanWmeIndex": cfgWlanWmeIndex,
       "cfgWlanWmeId": cfgWlanWmeId,
       "cfgWlanWmeAc": cfgWlanWmeAc,
       "cfgWlanWmeCwMin": cfgWlanWmeCwMin,
       "cfgWlanWmeCwMax": cfgWlanWmeCwMax,
       "cfgWlanWmeAifs": cfgWlanWmeAifs,
       "cfgWlanWmeTxOpMax": cfgWlanWmeTxOpMax,
       "cfgWlanWmeApCwMin": cfgWlanWmeApCwMin,
       "cfgWlanWmeApCwMax": cfgWlanWmeApCwMax,
       "cfgWlanWmeApAifs": cfgWlanWmeApAifs,
       "cfgWlanWmeApBurst": cfgWlanWmeApBurst,
       "cfgWlanDbgTable": cfgWlanDbgTable,
       "cfgWlanDbgTableEntry": cfgWlanDbgTableEntry,
       "cfgWlanDbgIndex": cfgWlanDbgIndex,
       "cfgWlanDbgIfaceName": cfgWlanDbgIfaceName,
       "cfgWlanDbgHandoff": cfgWlanDbgHandoff,
       "cfgWlanDbgScan": cfgWlanDbgScan,
       "cfgWlanDbgMlme": cfgWlanDbgMlme,
       "cfgWlanDbgEvents": cfgWlanDbgEvents,
       "cfgWlanDbgBeaconrssi": cfgWlanDbgBeaconrssi,
       "cfgWlanDbgAckrssi": cfgWlanDbgAckrssi,
       "cfgWlanDbgBeaconfiltered": cfgWlanDbgBeaconfiltered,
       "cfgWlanDbgRatelimit": cfgWlanDbgRatelimit,
       "cfgWlanDbgLinkmonitor": cfgWlanDbgLinkmonitor,
       "cfgWlanDbgBeacontsf": cfgWlanDbgBeacontsf,
       "cfgWlanDbgRange": cfgWlanDbgRange,
       "cfgWlanDbgReports": cfgWlanDbgReports,
       "cfgWlanAclWhiteTable": cfgWlanAclWhiteTable,
       "cfgWlanAclWhiteTableEntry": cfgWlanAclWhiteTableEntry,
       "cfgWlanAclWhiteIndex": cfgWlanAclWhiteIndex,
       "cfgWlanAclWhiteEnabled": cfgWlanAclWhiteEnabled,
       "cfgWlanAclWhiteInterface": cfgWlanAclWhiteInterface,
       "cfgWlanAclWhiteAddr": cfgWlanAclWhiteAddr,
       "cfgWlanAclWhiteMask": cfgWlanAclWhiteMask,
       "cfgWlanAclBlackTable": cfgWlanAclBlackTable,
       "cfgWlanAclBlackTableEntry": cfgWlanAclBlackTableEntry,
       "cfgWlanAclBlackIndex": cfgWlanAclBlackIndex,
       "cfgWlanAclBlackEnabled": cfgWlanAclBlackEnabled,
       "cfgWlanAclBlackInterface": cfgWlanAclBlackInterface,
       "cfgWlanAclBlackAddr": cfgWlanAclBlackAddr,
       "cfgWlanAclBlackMask": cfgWlanAclBlackMask,
       "cfgWlanGlobal": cfgWlanGlobal,
       "cfgWlanGlblCountry": cfgWlanGlblCountry,
       "cfgWlanGlblLinkmonitorInterval": cfgWlanGlblLinkmonitorInterval,
       "cfgWlanGlblLinkmonitorQmrrlogging": cfgWlanGlblLinkmonitorQmrrlogging,
       "cfgWlanGlblConnectionStatusWlanInterface": cfgWlanGlblConnectionStatusWlanInterface,
       "cfgWlan802dot1xTable": cfgWlan802dot1xTable,
       "cfgWlan802dot1xTableEntry": cfgWlan802dot1xTableEntry,
       "cfgWlan802dot1xIndex": cfgWlan802dot1xIndex,
       "cfgWlan802dot1xName": cfgWlan802dot1xName,
       "cfgWlan802dot1xOwnIpAddr": cfgWlan802dot1xOwnIpAddr,
       "cfgWlan802dot1xAuthServerParameter": cfgWlan802dot1xAuthServerParameter,
       "cfgWlan802dot1xAcctServerParameter": cfgWlan802dot1xAcctServerParameter,
       "cfgWlan802dot1xRetryPrimaryInterval": cfgWlan802dot1xRetryPrimaryInterval,
       "cfgWlan802dot1xInterimAccountingInterval": cfgWlan802dot1xInterimAccountingInterval,
       "cfgWlan802dot1xNasId": cfgWlan802dot1xNasId,
       "cfgWlan802dot1xEapType": cfgWlan802dot1xEapType,
       "cfgWlan802dot1xIdentity": cfgWlan802dot1xIdentity,
       "cfgWlan802dot1xClientKeyPassword": cfgWlan802dot1xClientKeyPassword,
       "cfgWlan802dot1xTlsControlParams": cfgWlan802dot1xTlsControlParams,
       "cfgWlan802dot1xAuthServerTable": cfgWlan802dot1xAuthServerTable,
       "cfgWlan802dot1xAuthServerTableEntry": cfgWlan802dot1xAuthServerTableEntry,
       "cfgWlan802dot1xAuthSrvIndex": cfgWlan802dot1xAuthSrvIndex,
       "cfgWlan802dot1xAuthSrvEnabled": cfgWlan802dot1xAuthSrvEnabled,
       "cfgWlan802dot1xAuthSrvId": cfgWlan802dot1xAuthSrvId,
       "cfgWlan802dot1xAuthSrvIpAddr": cfgWlan802dot1xAuthSrvIpAddr,
       "cfgWlan802dot1xAuthSrvPort": cfgWlan802dot1xAuthSrvPort,
       "cfgWlan802dot1xAuthSrvSharedSecret": cfgWlan802dot1xAuthSrvSharedSecret,
       "cfgWlan802dot1xAcctServerTable": cfgWlan802dot1xAcctServerTable,
       "cfgWlan802dot1xAcctServerTableEntry": cfgWlan802dot1xAcctServerTableEntry,
       "cfgWlan802dot1xAcctSrvIndex": cfgWlan802dot1xAcctSrvIndex,
       "cfgWlan802dot1xAcctSrvEnabled": cfgWlan802dot1xAcctSrvEnabled,
       "cfgWlan802dot1xAcctSrvId": cfgWlan802dot1xAcctSrvId,
       "cfgWlan802dot1xAcctSrvIpAddr": cfgWlan802dot1xAcctSrvIpAddr,
       "cfgWlan802dot1xAcctSrvPort": cfgWlan802dot1xAcctSrvPort,
       "cfgWlan802dot1xAcctSrvSharedSecret": cfgWlan802dot1xAcctSrvSharedSecret,
       "cfgWlan802dot11rTable": cfgWlan802dot11rTable,
       "cfgWlan802dot11rTableEntry": cfgWlan802dot11rTableEntry,
       "cfgWlan802dot11rIndex": cfgWlan802dot11rIndex,
       "cfgWlan802dot11rName": cfgWlan802dot11rName,
       "cfgWlan802dot11rEnabled": cfgWlan802dot11rEnabled,
       "cfgWlan802dot11rMobilityDomain": cfgWlan802dot11rMobilityDomain,
       "cfgWlan802dot11rPmkR0KeyHolderIdentifier": cfgWlan802dot11rPmkR0KeyHolderIdentifier,
       "cfgWlan802dot11rPmkR0Lifetime": cfgWlan802dot11rPmkR0Lifetime,
       "cfgWlan802dot11rPmkR1KeyHolderIdentifier": cfgWlan802dot11rPmkR1KeyHolderIdentifier,
       "cfgWlan802dot11rPmkR1Push": cfgWlan802dot11rPmkR1Push,
       "cfgWlan802dot11rR0KHParameter": cfgWlan802dot11rR0KHParameter,
       "cfgWlan802dot11rR1KHParameter": cfgWlan802dot11rR1KHParameter,
       "cfgWlan802dot11rExpirationEnabled": cfgWlan802dot11rExpirationEnabled,
       "cfgWlan802dot11rExpirationTime": cfgWlan802dot11rExpirationTime,
       "cfgWlan802dot11rVlan": cfgWlan802dot11rVlan,
       "cfgWlan802dot11rR0KHTable": cfgWlan802dot11rR0KHTable,
       "cfgWlan802dot11rR0KHTableEntry": cfgWlan802dot11rR0KHTableEntry,
       "cfgWlan802dot11rR0KHIndex": cfgWlan802dot11rR0KHIndex,
       "cfgWlan802dot11rR0KHId": cfgWlan802dot11rR0KHId,
       "cfgWlan802dot11rR0KHEnabled": cfgWlan802dot11rR0KHEnabled,
       "cfgWlan802dot11rR0KHDestinationMac": cfgWlan802dot11rR0KHDestinationMac,
       "cfgWlan802dot11rR0KHHID": cfgWlan802dot11rR0KHHID,
       "cfgWlan802dot11rR0KHKey": cfgWlan802dot11rR0KHKey,
       "cfgWlan802dot11rR1KHTable": cfgWlan802dot11rR1KHTable,
       "cfgWlan802dot11rR1KHTableEntry": cfgWlan802dot11rR1KHTableEntry,
       "cfgWlan802dot11rR1KHIndex": cfgWlan802dot11rR1KHIndex,
       "cfgWlan802dot11rR1KHId": cfgWlan802dot11rR1KHId,
       "cfgWlan802dot11rR1KHEnabled": cfgWlan802dot11rR1KHEnabled,
       "cfgWlan802dot11rR1KHDestinationMac": cfgWlan802dot11rR1KHDestinationMac,
       "cfgWlan802dot11rR1KHHID": cfgWlan802dot11rR1KHHID,
       "cfgWlan802dot11rR1KHKey": cfgWlan802dot11rR1KHKey,
       "cfgWlanNeighbourTable": cfgWlanNeighbourTable,
       "cfgWlanNeighbourTableEntry": cfgWlanNeighbourTableEntry,
       "cfgWlanNeighbourIndex": cfgWlanNeighbourIndex,
       "cfgWlanNeighbourId": cfgWlanNeighbourId,
       "cfgWlanNeighbourEnabled": cfgWlanNeighbourEnabled,
       "cfgWlanNeighbourBSSID": cfgWlanNeighbourBSSID,
       "cfgWlanNeighbourFrequency": cfgWlanNeighbourFrequency,
       "cfgRouting": cfgRouting,
       "cfgRouteDefault": cfgRouteDefault,
       "cfgRouteDefGateway": cfgRouteDefGateway,
       "cfgRouteDefGwOverride": cfgRouteDefGwOverride,
       "cfgRouteTable": cfgRouteTable,
       "cfgRouteTableEntry": cfgRouteTableEntry,
       "cfgRouteTableIndex": cfgRouteTableIndex,
       "cfgRouteTableEnabled": cfgRouteTableEnabled,
       "cfgRouteTableDestinationNetwork": cfgRouteTableDestinationNetwork,
       "cfgRouteTableGateway": cfgRouteTableGateway,
       "cfgRouteTableSource": cfgRouteTableSource,
       "cfgRouteTableCarpId": cfgRouteTableCarpId,
       "cfgMRouteTable": cfgMRouteTable,
       "cfgMRouteTableEntry": cfgMRouteTableEntry,
       "cfgMRouteTableIndex": cfgMRouteTableIndex,
       "cfgMRouteTableEnabled": cfgMRouteTableEnabled,
       "cfgMRouteTableInput": cfgMRouteTableInput,
       "cfgMRouteTableSource": cfgMRouteTableSource,
       "cfgMRouteTableGroup": cfgMRouteTableGroup,
       "cfgMRouteTableOutput": cfgMRouteTableOutput,
       "cfgIpTables": cfgIpTables,
       "cfgQos": cfgQos,
       "cfgQosL3PrioEnabled": cfgQosL3PrioEnabled,
       "cfgQosDscpToTidMapTable": cfgQosDscpToTidMapTable,
       "cfgQosDscpToTidMapTableEntry": cfgQosDscpToTidMapTableEntry,
       "cfgQosDscpToTidMapTableIndex": cfgQosDscpToTidMapTableIndex,
       "cfgQosDscpToTidMapValue": cfgQosDscpToTidMapValue,
       "cfgQosVlanToTidMapTable": cfgQosVlanToTidMapTable,
       "cfgQosVlanToTidMapTableEntry": cfgQosVlanToTidMapTableEntry,
       "cfgQosVlanToTidMapTableIndex": cfgQosVlanToTidMapTableIndex,
       "cfgQosVlanToTidMapValue": cfgQosVlanToTidMapValue,
       "cfgQosIpToTidMapTable": cfgQosIpToTidMapTable,
       "cfgQosIpToTidMapTableEntry": cfgQosIpToTidMapTableEntry,
       "cfgQosIpToTidMapTableIndex": cfgQosIpToTidMapTableIndex,
       "cfgQosIpToTidMapSrcNet": cfgQosIpToTidMapSrcNet,
       "cfgQosIpToTidMapDestNet": cfgQosIpToTidMapDestNet,
       "cfgQosIpToTidMapProto": cfgQosIpToTidMapProto,
       "cfgQosIpToTidMapSrcPort": cfgQosIpToTidMapSrcPort,
       "cfgQosIpToTidMapDestPort": cfgQosIpToTidMapDestPort,
       "cfgQosIpToTidMapPrecedence": cfgQosIpToTidMapPrecedence,
       "cfgQosIpToTidMapEnabled": cfgQosIpToTidMapEnabled,
       "cfgLogging": cfgLogging,
       "cfgLogRemote": cfgLogRemote,
       "cfgLogRemoteTable": cfgLogRemoteTable,
       "cfgLogRemoteTableEntry": cfgLogRemoteTableEntry,
       "cfgLogRemoteIndex": cfgLogRemoteIndex,
       "cfgLogRemoteEnabled": cfgLogRemoteEnabled,
       "cfgLogRemoteLevel": cfgLogRemoteLevel,
       "cfgLogRemoteProtocol": cfgLogRemoteProtocol,
       "cfgLogRemoteIp": cfgLogRemoteIp,
       "cfgLogRemotePort": cfgLogRemotePort,
       "cfgSnmp": cfgSnmp,
       "cfgSnmpd": cfgSnmpd,
       "cfgSnmpdLocation": cfgSnmpdLocation,
       "cfgSnmpdContact": cfgSnmpdContact,
       "cfgSnmpdVersion": cfgSnmpdVersion,
       "cfgSnmpdName": cfgSnmpdName,
       "cfgSnmpdEnabled": cfgSnmpdEnabled,
       "cfgSnmpdAddress": cfgSnmpdAddress,
       "cfgSnmpdCommunity": cfgSnmpdCommunity,
       "cfgSnmpdComAdmin": cfgSnmpdComAdmin,
       "cfgSnmpdComMaintainer": cfgSnmpdComMaintainer,
       "cfgSnmpdComMonitor": cfgSnmpdComMonitor,
       "cfgSnmpTrap": cfgSnmpTrap,
       "cfgSnmpTrapEnabled": cfgSnmpTrapEnabled,
       "cfgSnmpTrapVersion": cfgSnmpTrapVersion,
       "cfgSnmpTrapCommunity": cfgSnmpTrapCommunity,
       "cfgSnmpTrapDest": cfgSnmpTrapDest,
       "cfgDhcp": cfgDhcp,
       "cfgDhcpGlobal": cfgDhcpGlobal,
       "cfgDhcpGlobalEnabled": cfgDhcpGlobalEnabled,
       "cfgDhcpDnsmasqTable": cfgDhcpDnsmasqTable,
       "cfgDhcpDnsmasqTableEntry": cfgDhcpDnsmasqTableEntry,
       "cfgDhcpDnsmasqIndex": cfgDhcpDnsmasqIndex,
       "cfgDhcpDnsmasqScopeParameter": cfgDhcpDnsmasqScopeParameter,
       "cfgDhcpScopeTable": cfgDhcpScopeTable,
       "cfgDhcpScopeTableEntry": cfgDhcpScopeTableEntry,
       "cfgDhcpScopeIndex": cfgDhcpScopeIndex,
       "cfgDhcpScopeId": cfgDhcpScopeId,
       "cfgDhcpScopeInterface": cfgDhcpScopeInterface,
       "cfgDhcpScopeStart": cfgDhcpScopeStart,
       "cfgDhcpScopeLimit": cfgDhcpScopeLimit,
       "cfgDhcpScopeLeasetime": cfgDhcpScopeLeasetime,
       "cfgDhcpScopeGateway": cfgDhcpScopeGateway,
       "cfgDhcpScopeDnsServer1": cfgDhcpScopeDnsServer1,
       "cfgDhcpScopeDnsServer2": cfgDhcpScopeDnsServer2,
       "cfgNtp": cfgNtp,
       "cfgNtpEnabled": cfgNtpEnabled,
       "cfgNtpServer1": cfgNtpServer1,
       "cfgNtpServer2": cfgNtpServer2,
       "cfgHttp": cfgHttp,
       "cfgHttpUser": cfgHttpUser,
       "cfgHttpPassword": cfgHttpPassword,
       "cfgHttpEnabled": cfgHttpEnabled,
       "cfgHttpRedirectEnabled": cfgHttpRedirectEnabled,
       "cfgHttpHttpAddress": cfgHttpHttpAddress,
       "cfgHttpHttpsAddress": cfgHttpHttpsAddress,
       "cfgLldp": cfgLldp,
       "cfgLldpEnabled": cfgLldpEnabled,
       "cfgLldpDescription": cfgLldpDescription,
       "cfgMdns": cfgMdns,
       "cfgMdnsEnabled": cfgMdnsEnabled,
       "cfgMdnsNetwork": cfgMdnsNetwork,
       "cfgNlm": cfgNlm,
       "cfgNlmGlobal": cfgNlmGlobal,
       "cfgNlmGlblEnabled": cfgNlmGlblEnabled,
       "cfgNlmMonitorTable": cfgNlmMonitorTable,
       "cfgNlmMonitorTableEntry": cfgNlmMonitorTableEntry,
       "cfgNlmMonIndex": cfgNlmMonIndex,
       "cfgNlmMonEnabled": cfgNlmMonEnabled,
       "cfgNlmMonInterval": cfgNlmMonInterval,
       "cfgNlmMonCount": cfgNlmMonCount,
       "cfgNlmMonType": cfgNlmMonType,
       "cfgNlmMonInterfaces": cfgNlmMonInterfaces,
       "cfgNlmMonDestination": cfgNlmMonDestination,
       "cfgNlmMonUpAction": cfgNlmMonUpAction,
       "cfgNlmMonDownAction": cfgNlmMonDownAction,
       "cfgNlmMonScanLoopInterval": cfgNlmMonScanLoopInterval,
       "cfgCli": cfgCli,
       "cfgCliEnabled": cfgCliEnabled,
       "cfgCliUsername": cfgCliUsername,
       "cfgCliPassword": cfgCliPassword,
       "cfgCliTelnetEnabled": cfgCliTelnetEnabled,
       "cfgCliSshEnabled": cfgCliSshEnabled,
       "cfgCliTelnetAddress": cfgCliTelnetAddress,
       "cfgCliSshAddress": cfgCliSshAddress,
       "cfgCellular": cfgCellular,
       "cfgCellSimTable": cfgCellSimTable,
       "cfgCellSimTableEntry": cfgCellSimTableEntry,
       "cfgCellSimIndex": cfgCellSimIndex,
       "cfgCellSimApn": cfgCellSimApn,
       "cfgCellSimUsername": cfgCellSimUsername,
       "cfgCellSimPassword": cfgCellSimPassword,
       "cfgCellSimPinEnabled": cfgCellSimPinEnabled,
       "cfgCellSimPin": cfgCellSimPin,
       "cfgCellSimAuthType": cfgCellSimAuthType,
       "rpc": rpc,
       "rpcConfiguration": rpcConfiguration,
       "rpcCfgRevert": rpcCfgRevert,
       "rpcCfgApply": rpcCfgApply,
       "rpcCfgFile": rpcCfgFile,
       "rpcFirmware": rpcFirmware,
       "rpcFwFlash": rpcFwFlash,
       "rpcSystem": rpcSystem,
       "rpcSysReboot": rpcSysReboot,
       "rpcSysFactoryReset": rpcSysFactoryReset,
       "rpcSysErrorReset": rpcSysErrorReset,
       "rpcSysKernelLogReset": rpcSysKernelLogReset,
       "rpcCertificate": rpcCertificate,
       "rpcCrtFile": rpcCrtFile,
       "rpcDriver": rpcDriver,
       "rpcDrvTable": rpcDrvTable,
       "rpcDrvTableEntry": rpcDrvTableEntry,
       "rpcDrvIndex": rpcDrvIndex,
       "rpcDrvName": rpcDrvName,
       "rpcDrvDfsSimulateRadar": rpcDrvDfsSimulateRadar,
       "settings": settings,
       "setConfiguration": setConfiguration,
       "setCfgFileUrl": setCfgFileUrl,
       "setWireless": setWireless,
       "setWlanDeviceTable": setWlanDeviceTable,
       "setWlanDeviceTableEntry": setWlanDeviceTableEntry,
       "setWlanDevIndex": setWlanDevIndex,
       "setWlanDevName": setWlanDevName,
       "setWlanDevRfOutput": setWlanDevRfOutput,
       "setWlanDevFrequency": setWlanDevFrequency,
       "setWlanDevPower": setWlanDevPower,
       "setWlanDbgTable": setWlanDbgTable,
       "setWlanDbgTableEntry": setWlanDbgTableEntry,
       "setWlanDbgIndex": setWlanDbgIndex,
       "setWlanDbgIfaceName": setWlanDbgIfaceName,
       "setWlanDbgHandoff": setWlanDbgHandoff,
       "setWlanDbgScan": setWlanDbgScan,
       "setWlanDbgMlme": setWlanDbgMlme,
       "setWlanDbgEvents": setWlanDbgEvents,
       "setWlanDbgBeaconrssi": setWlanDbgBeaconrssi,
       "setWlanDbgAckrssi": setWlanDbgAckrssi,
       "setWlanDbgBeaconfiltered": setWlanDbgBeaconfiltered,
       "setWlanDbgRatelimit": setWlanDbgRatelimit,
       "setWlanDbgBeacontsf": setWlanDbgBeacontsf,
       "setWlanDbgRange": setWlanDbgRange,
       "setWlanDbgReports": setWlanDbgReports,
       "setConfmgmtd": setConfmgmtd,
       "setCfgdLogLevel": setCfgdLogLevel,
       "setFirmware": setFirmware,
       "setFwFileUrl": setFwFileUrl,
       "setFwKeepConfig": setFwKeepConfig,
       "setCertificate": setCertificate,
       "setCrtFileUrl": setCrtFileUrl,
       "setCrtFileSelector": setCrtFileSelector,
       "setCrtFileFormat": setCrtFileFormat,
       "setCrtFilePkcs12Passphrase": setCrtFilePkcs12Passphrase,
       "setSystem": setSystem,
       "setSysTime": setSysTime,
       "hardware": hardware,
       "hwSystem": hwSystem,
       "hwSysProduct": hwSysProduct,
       "hwSysSerial": hwSysSerial,
       "hwSysRevision": hwSysRevision,
       "hwSysVersion": hwSysVersion,
       "hwNetwork": hwNetwork,
       "hwNetEthernetTable": hwNetEthernetTable,
       "hwNetEthernetTableEntry": hwNetEthernetTableEntry,
       "hwNetEthIndex": hwNetEthIndex,
       "hwNetEthName": hwNetEthName,
       "hwNetEthAssembled": hwNetEthAssembled,
       "hwNetEthMacAddress": hwNetEthMacAddress,
       "hwNetEthOperation": hwNetEthOperation,
       "hwNetEthSpeed": hwNetEthSpeed,
       "hwNetEthHwIndex": hwNetEthHwIndex,
       "hwWireless": hwWireless,
       "hwWlanDeviceTable": hwWlanDeviceTable,
       "hwWlanDeviceTableEntry": hwWlanDeviceTableEntry,
       "hwWlanDevIndex": hwWlanDevIndex,
       "hwWlanDevAssembled": hwWlanDevAssembled,
       "hwWlanDevType": hwWlanDevType,
       "hwWlanDevSerial": hwWlanDevSerial,
       "hwWlanDevRevision": hwWlanDevRevision,
       "hwWlanDevVersion": hwWlanDevVersion,
       "hwWlanDevPcbId": hwWlanDevPcbId,
       "hwWlanDevAssemblyId": hwWlanDevAssemblyId,
       "hwWlanDevMacAddress": hwWlanDevMacAddress,
       "hwWlanDevAntennaProfileId": hwWlanDevAntennaProfileId,
       "hwWlanDevAntennaGain": hwWlanDevAntennaGain,
       "hwWlanDevCableLoss": hwWlanDevCableLoss,
       "hwWlanGlobal": hwWlanGlobal,
       "hwWlanGlblRegulatoryRegionId": hwWlanGlblRegulatoryRegionId,
       "hwBaseBoard": hwBaseBoard,
       "hwBbType": hwBbType,
       "hwBbSerial": hwBbSerial,
       "hwBbRevision": hwBbRevision,
       "hwBbVersion": hwBbVersion,
       "hwBbPcbId": hwBbPcbId,
       "hwBbAssemblyId": hwBbAssemblyId,
       "hwIfaceBoard": hwIfaceBoard,
       "hwIfBrdAssembled": hwIfBrdAssembled,
       "hwIfBrdType": hwIfBrdType,
       "hwIfBrdSerial": hwIfBrdSerial,
       "hwIfBrdRevision": hwIfBrdRevision,
       "hwIfBrdVersion": hwIfBrdVersion,
       "hwIfBrdPcbId": hwIfBrdPcbId,
       "hwIfBrdAssemblyId": hwIfBrdAssemblyId,
       "hwSensor": hwSensor,
       "hwSensorTable": hwSensorTable,
       "hwSensorTableEntry": hwSensorTableEntry,
       "hwSensorIndex": hwSensorIndex,
       "hwSensorName": hwSensorName,
       "hwSensorUnit": hwSensorUnit,
       "hwSensorValue": hwSensorValue,
       "software": software,
       "swFirmware": swFirmware,
       "swFwName": swFwName,
       "swFwVersion": swFwVersion,
       "swFwRevision": swFwRevision,
       "swSystem": swSystem,
       "swSysRebootReason": swSysRebootReason,
       "swSysBootStatus": swSysBootStatus,
       "swSysMessageTable": swSysMessageTable,
       "swSysMessageTableEntry": swSysMessageTableEntry,
       "swSysMsgIndex": swSysMsgIndex,
       "swSysMsgPriority": swSysMsgPriority,
       "swSysMsgCode": swSysMsgCode,
       "swSysMsgText": swSysMsgText,
       "swOperatingSystem": swOperatingSystem,
       "swOsName": swOsName,
       "swOsVersion": swOsVersion,
       "swOsRevision": swOsRevision,
       "swOsUptime": swOsUptime,
       "swDriver": swDriver,
       "swDrvDfsTable": swDrvDfsTable,
       "swDrvDfsTableEntry": swDrvDfsTableEntry,
       "swDrvDfsIndex": swDrvDfsIndex,
       "swDrvDfsName": swDrvDfsName,
       "swDrvDfsPulsesDetected": swDrvDfsPulsesDetected,
       "swDrvDfsPulsesProcessed": swDrvDfsPulsesProcessed,
       "swDrvDfsRadarDetected": swDrvDfsRadarDetected,
       "swDrvCntWlanMacTable": swDrvCntWlanMacTable,
       "swDrvCntWlanMacTableEntry": swDrvCntWlanMacTableEntry,
       "swDrvCntWlanMacIndex": swDrvCntWlanMacIndex,
       "swDrvCntWlanMacName": swDrvCntWlanMacName,
       "swDrvCntWlanMacTxHandlersDrop": swDrvCntWlanMacTxHandlersDrop,
       "swDrvCntWlanMacTxHandlersQueued": swDrvCntWlanMacTxHandlersQueued,
       "swDrvCntWlanMacTxHandlersDropUnencrypted": swDrvCntWlanMacTxHandlersDropUnencrypted,
       "swDrvCntWlanMacTxHandlersDropFragment": swDrvCntWlanMacTxHandlersDropFragment,
       "swDrvCntWlanMacTxHandlersDropWep": swDrvCntWlanMacTxHandlersDropWep,
       "swDrvCntWlanMacTxHandlersDropNotAssoc": swDrvCntWlanMacTxHandlersDropNotAssoc,
       "swDrvCntWlanMacTxHandlersDropUnauthPort": swDrvCntWlanMacTxHandlersDropUnauthPort,
       "swDrvCntWlanMacRxHandlersDrop": swDrvCntWlanMacRxHandlersDrop,
       "swDrvCntWlanMacRxHandlersQueued": swDrvCntWlanMacRxHandlersQueued,
       "swDrvCntWlanMacRxHandlersDropNullfunc": swDrvCntWlanMacRxHandlersDropNullfunc,
       "swDrvCntWlanMacRxHandlersDropDefrag": swDrvCntWlanMacRxHandlersDropDefrag,
       "swDrvCntWlanMacRxHandlersDropShort": swDrvCntWlanMacRxHandlersDropShort,
       "swDrvCntWlanMacTxExpandSkbHead": swDrvCntWlanMacTxExpandSkbHead,
       "swDrvCntWlanMacTxExpandSkbHeadCloned": swDrvCntWlanMacTxExpandSkbHeadCloned,
       "swDrvCntWlanMacRxExpandSkbHead": swDrvCntWlanMacRxExpandSkbHead,
       "swDrvCntWlanMacRxExpandSkbHead2": swDrvCntWlanMacRxExpandSkbHead2,
       "swDrvCntWlanMacRxHandlersFragments": swDrvCntWlanMacRxHandlersFragments,
       "swDrvCntWlanMacTxstatusDrop": swDrvCntWlanMacTxstatusDrop,
       "swDrvCntWlanWmmTable": swDrvCntWlanWmmTable,
       "swDrvCntWlanWmmTableEntry": swDrvCntWlanWmmTableEntry,
       "swDrvCntWlanWmmTableIndex": swDrvCntWlanWmmTableIndex,
       "swDrvCntWlanWmmName": swDrvCntWlanWmmName,
       "swDrvCntWlanWmmTx": swDrvCntWlanWmmTx,
       "swDrvCntWlanWmmRx": swDrvCntWlanWmmRx,
       "swDrvCntWlanWmmShortRetries": swDrvCntWlanWmmShortRetries,
       "swDrvCntWlanWmmLongRetries": swDrvCntWlanWmmLongRetries,
       "swDrvCntWlanWmmExceededRetries": swDrvCntWlanWmmExceededRetries,
       "swDrvConStatWlanIf": swDrvConStatWlanIf,
       "swDrvConStatTable": swDrvConStatTable,
       "swDrvConStatTableEntry": swDrvConStatTableEntry,
       "swDrvConStatIndex": swDrvConStatIndex,
       "swDrvConStatWlanName": swDrvConStatWlanName,
       "swDrvConStatMacName": swDrvConStatMacName,
       "swDrvConStatRxBrExtra": swDrvConStatRxBrExtra,
       "swDrvConStatRxBrType": swDrvConStatRxBrType,
       "swDrvConStatRxBrValue": swDrvConStatRxBrValue,
       "swDrvConStatRxBytes": swDrvConStatRxBytes,
       "swDrvConStatRxPackets": swDrvConStatRxPackets,
       "swDrvConStatTxBrExtra": swDrvConStatTxBrExtra,
       "swDrvConStatTxBrType": swDrvConStatTxBrType,
       "swDrvConStatTxBrValue": swDrvConStatTxBrValue,
       "swDrvConStatTxBytes": swDrvConStatTxBytes,
       "swDrvConStatTxPackets": swDrvConStatTxPackets,
       "swDrvConStatSigChain0": swDrvConStatSigChain0,
       "swDrvConStatSigChain1": swDrvConStatSigChain1,
       "swDrvConStatSigChain2": swDrvConStatSigChain2,
       "swDrvConStatSigAvgChain0": swDrvConStatSigAvgChain0,
       "swDrvConStatSigAvgChain1": swDrvConStatSigAvgChain1,
       "swDrvConStatSigAvgChain2": swDrvConStatSigAvgChain2,
       "swDrvConStatTxRetries": swDrvConStatTxRetries,
       "swDrvConStatTxFailed": swDrvConStatTxFailed,
       "swDrvConStatCacheNo": swDrvConStatCacheNo,
       "swDrvConStatSigCombined": swDrvConStatSigCombined,
       "swDrvConStatSigAvgCombined": swDrvConStatSigAvgCombined,
       "swDrvCntWlanTable": swDrvCntWlanTable,
       "swDrvCntWlanTableEntry": swDrvCntWlanTableEntry,
       "swDrvCntWlanIndex": swDrvCntWlanIndex,
       "swDrvCntWlanName": swDrvCntWlanName,
       "swDrvCntWlanAssocSuccess": swDrvCntWlanAssocSuccess,
       "swDrvCntWlanAssocFailure": swDrvCntWlanAssocFailure,
       "swDrvCntWlanAssocFailureMaxSta": swDrvCntWlanAssocFailureMaxSta,
       "swDrvCntWlanNumAssocSta": swDrvCntWlanNumAssocSta,
       "swDrvCntWlanEapAuthStarted": swDrvCntWlanEapAuthStarted,
       "swDrvCntWlanEapAuthFailed": swDrvCntWlanEapAuthFailed,
       "swDrvCntWlanChannelActive": swDrvCntWlanChannelActive,
       "swDrvCntWlanChannelBusy": swDrvCntWlanChannelBusy,
       "swDrvCntWlanChannelTransmit": swDrvCntWlanChannelTransmit,
       "swDrvCntWlanChannelReceive": swDrvCntWlanChannelReceive,
       "swDrvCntWlanChannelNoise": swDrvCntWlanChannelNoise,
       "swDrvCntWlanEapAuthStartedFT": swDrvCntWlanEapAuthStartedFT,
       "swDrvCntWlanEapAuthStartedFILS": swDrvCntWlanEapAuthStartedFILS,
       "swDrvCntWlanEapAuthStartedPKMSA": swDrvCntWlanEapAuthStartedPKMSA,
       "swRdm": swRdm,
       "swRdmMaxEirp": swRdmMaxEirp,
       "swRdmMaxApp": swRdmMaxApp,
       "swBootloader": swBootloader,
       "swBootName": swBootName,
       "swBootVersion": swBootVersion,
       "swBootBuildDate": swBootBuildDate,
       "swConfiguration": swConfiguration,
       "swCfgChangesCount": swCfgChangesCount,
       "conformance": conformance,
       "groups": groups,
       "groupConfiguration": groupConfiguration,
       "groupCfgSystem": groupCfgSystem,
       "groupCfgNetwork": groupCfgNetwork,
       "groupCfgNetEthernet": groupCfgNetEthernet,
       "groupCfgNetWlan": groupCfgNetWlan,
       "groupCfgNetVlan": groupCfgNetVlan,
       "groupCfgNetIp": groupCfgNetIp,
       "groupCfgNetCarp": groupCfgNetCarp,
       "groupCfgNetMacVLan": groupCfgNetMacVLan,
       "groupCfgNetWwan": groupCfgNetWwan,
       "groupCfgWireless": groupCfgWireless,
       "groupCfgWlanDevice": groupCfgWlanDevice,
       "groupCfgWlanInterface": groupCfgWlanInterface,
       "groupCfgWlanHandoff": groupCfgWlanHandoff,
       "groupCfgWlanScanFreq": groupCfgWlanScanFreq,
       "groupCfgWlanWme": groupCfgWlanWme,
       "groupCfgWlanDbg": groupCfgWlanDbg,
       "groupCfgWlanAclBlack": groupCfgWlanAclBlack,
       "groupCfgWlanAclWhite": groupCfgWlanAclWhite,
       "groupCfgWlanGlobal": groupCfgWlanGlobal,
       "groupCfgWlan802dot1x": groupCfgWlan802dot1x,
       "groupCfgWlan802dot1xAuth": groupCfgWlan802dot1xAuth,
       "groupCfgWlan802dot1xAcct": groupCfgWlan802dot1xAcct,
       "groupCfgWlan802dot11r": groupCfgWlan802dot11r,
       "groupCfgWlanNeighbour": groupCfgWlanNeighbour,
       "groupCfgRouting": groupCfgRouting,
       "groupCfgRouteDefault": groupCfgRouteDefault,
       "groupCfgRouteTable": groupCfgRouteTable,
       "groupCfgMRouteTable": groupCfgMRouteTable,
       "groupCfgLogging": groupCfgLogging,
       "groupCfgSnmp": groupCfgSnmp,
       "groupCfgSnmpd": groupCfgSnmpd,
       "groupCfgSnmpTrap": groupCfgSnmpTrap,
       "groupCfgDhcp": groupCfgDhcp,
       "groupCfgDhcpGlobal": groupCfgDhcpGlobal,
       "groupCfgDhcpDnsmasq": groupCfgDhcpDnsmasq,
       "groupCfgDhcpScope": groupCfgDhcpScope,
       "groupCfgNtp": groupCfgNtp,
       "groupCfgHttp": groupCfgHttp,
       "groupCfgLldp": groupCfgLldp,
       "groupCfgMdns": groupCfgMdns,
       "groupCfgQos": groupCfgQos,
       "groupCfgQosGlobal": groupCfgQosGlobal,
       "groupCfgQosDscpToTidMapTable": groupCfgQosDscpToTidMapTable,
       "groupCfgQosVlanToTidMapTable": groupCfgQosVlanToTidMapTable,
       "groupCfgQosIpToTidMapTable": groupCfgQosIpToTidMapTable,
       "groupCfgNlm": groupCfgNlm,
       "groupCfgCli": groupCfgCli,
       "groupCfgCellular": groupCfgCellular,
       "groupCfgCellSim": groupCfgCellSim,
       "groupStatus": groupStatus,
       "groupRpc": groupRpc,
       "groupRpcConfiguration": groupRpcConfiguration,
       "groupRpcFirmware": groupRpcFirmware,
       "groupRpcSystem": groupRpcSystem,
       "groupRpcCertificate": groupRpcCertificate,
       "groupRpcDriver": groupRpcDriver,
       "groupSettings": groupSettings,
       "groupSetConfigurationFile": groupSetConfigurationFile,
       "groupSetWireless": groupSetWireless,
       "groupSetWlanDbg": groupSetWlanDbg,
       "groupSetConfmgmtd": groupSetConfmgmtd,
       "groupSetFirmware": groupSetFirmware,
       "groupSetCertificate": groupSetCertificate,
       "groupSetSystem": groupSetSystem,
       "groupHardware": groupHardware,
       "groupHwSystem": groupHwSystem,
       "groupHwNetwork": groupHwNetwork,
       "groupHwWireless": groupHwWireless,
       "groupHwBaseBoard": groupHwBaseBoard,
       "groupHwIfaceBoard": groupHwIfaceBoard,
       "groupHwSensor": groupHwSensor,
       "groupSoftware": groupSoftware,
       "groupSwFirmware": groupSwFirmware,
       "groupSwSystem": groupSwSystem,
       "groupSwOperatingSystem": groupSwOperatingSystem,
       "groupSwDrvDfs": groupSwDrvDfs,
       "groupSwDrvCntWlanMac": groupSwDrvCntWlanMac,
       "groupSwDrvCntWlanWmm": groupSwDrvCntWlanWmm,
       "groupSwDrvConStat": groupSwDrvConStat,
       "groupSwDrvCntWlanTable": groupSwDrvCntWlanTable,
       "groupSwRdm": groupSwRdm,
       "groupSwBootloader": groupSwBootloader,
       "groupSwConfiguration": groupSwConfiguration,
       "groupFeatures": groupFeatures,
       "compliances": compliances,
       "compliance": compliance}
)
