# SNMP MIB module (HP-ICF-DEVICEIDENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ICF-DEVICEIDENTITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:02 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfDeviceIdentityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135)
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityMIB.setRevisions(
        ("2019-07-16 00:00",
         "2017-12-05 00:00",
         "2017-01-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDeviceIdentityConfig_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityConfig = _HpicfDeviceIdentityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1)
)
_HpicfDeviceIdentityTable_Object = MibTable
hpicfDeviceIdentityTable = _HpicfDeviceIdentityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityTable.setStatus("current")
_HpicfDeviceIdentityEntry_Object = MibTableRow
hpicfDeviceIdentityEntry = _HpicfDeviceIdentityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1)
)
hpicfDeviceIdentityEntry.setIndexNames(
    (0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityIndex"),
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityEntry.setStatus("current")


class _HpicfDeviceIdentityIndex_Type(Unsigned32):
    """Custom type hpicfDeviceIdentityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfDeviceIdentityIndex_Type.__name__ = "Unsigned32"
_HpicfDeviceIdentityIndex_Object = MibTableColumn
hpicfDeviceIdentityIndex = _HpicfDeviceIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 1),
    _HpicfDeviceIdentityIndex_Type()
)
hpicfDeviceIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityIndex.setStatus("current")
_HpicfDeviceIdentityRowStatus_Type = RowStatus
_HpicfDeviceIdentityRowStatus_Object = MibTableColumn
hpicfDeviceIdentityRowStatus = _HpicfDeviceIdentityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 2),
    _HpicfDeviceIdentityRowStatus_Type()
)
hpicfDeviceIdentityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityRowStatus.setStatus("current")


class _HpicfDeviceIdentityName_Type(OctetString):
    """Custom type hpicfDeviceIdentityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HpicfDeviceIdentityName_Type.__name__ = "OctetString"
_HpicfDeviceIdentityName_Object = MibTableColumn
hpicfDeviceIdentityName = _HpicfDeviceIdentityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 3),
    _HpicfDeviceIdentityName_Type()
)
hpicfDeviceIdentityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityName.setStatus("current")


class _HpicfDeviceIdentityLldpOui_Type(OctetString):
    """Custom type hpicfDeviceIdentityLldpOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_HpicfDeviceIdentityLldpOui_Type.__name__ = "OctetString"
_HpicfDeviceIdentityLldpOui_Object = MibTableColumn
hpicfDeviceIdentityLldpOui = _HpicfDeviceIdentityLldpOui_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 4),
    _HpicfDeviceIdentityLldpOui_Type()
)
hpicfDeviceIdentityLldpOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityLldpOui.setStatus("current")


class _HpicfDeviceIdentityLldpSubType_Type(Integer32):
    """Custom type hpicfDeviceIdentityLldpSubType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfDeviceIdentityLldpSubType_Type.__name__ = "Integer32"
_HpicfDeviceIdentityLldpSubType_Object = MibTableColumn
hpicfDeviceIdentityLldpSubType = _HpicfDeviceIdentityLldpSubType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 5),
    _HpicfDeviceIdentityLldpSubType_Type()
)
hpicfDeviceIdentityLldpSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityLldpSubType.setStatus("current")


class _HpicfDeviceIdentityLldpSysName_Type(OctetString):
    """Custom type hpicfDeviceIdentityLldpSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_HpicfDeviceIdentityLldpSysName_Type.__name__ = "OctetString"
_HpicfDeviceIdentityLldpSysName_Object = MibTableColumn
hpicfDeviceIdentityLldpSysName = _HpicfDeviceIdentityLldpSysName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 6),
    _HpicfDeviceIdentityLldpSysName_Type()
)
hpicfDeviceIdentityLldpSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityLldpSysName.setStatus("current")


class _HpicfDeviceIdentityLldpSysDescr_Type(OctetString):
    """Custom type hpicfDeviceIdentityLldpSysDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_HpicfDeviceIdentityLldpSysDescr_Type.__name__ = "OctetString"
_HpicfDeviceIdentityLldpSysDescr_Object = MibTableColumn
hpicfDeviceIdentityLldpSysDescr = _HpicfDeviceIdentityLldpSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 7),
    _HpicfDeviceIdentityLldpSysDescr_Type()
)
hpicfDeviceIdentityLldpSysDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityLldpSysDescr.setStatus("current")
_HpicfCdpBypassTable_Object = MibTable
hpicfCdpBypassTable = _HpicfCdpBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfCdpBypassTable.setStatus("current")
_HpicfCdpBypassEntry_Object = MibTableRow
hpicfCdpBypassEntry = _HpicfCdpBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1)
)
hpicfCdpBypassEntry.setIndexNames(
    (0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityIndex"),
    (0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpType"),
)
if mibBuilder.loadTexts:
    hpicfCdpBypassEntry.setStatus("current")


class _HpicfDevIdentityCdpType_Type(Integer32):
    """Custom type hpicfDevIdentityCdpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_HpicfDevIdentityCdpType_Type.__name__ = "Integer32"
_HpicfDevIdentityCdpType_Object = MibTableColumn
hpicfDevIdentityCdpType = _HpicfDevIdentityCdpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1, 1),
    _HpicfDevIdentityCdpType_Type()
)
hpicfDevIdentityCdpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDevIdentityCdpType.setStatus("current")


class _HpicfDevIdentityCdpValue_Type(OctetString):
    """Custom type hpicfDevIdentityCdpValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDevIdentityCdpValue_Type.__name__ = "OctetString"
_HpicfDevIdentityCdpValue_Object = MibTableColumn
hpicfDevIdentityCdpValue = _HpicfDevIdentityCdpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1, 2),
    _HpicfDevIdentityCdpValue_Type()
)
hpicfDevIdentityCdpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDevIdentityCdpValue.setStatus("current")
_HpicfDevIdentityCdpRowStatus_Type = RowStatus
_HpicfDevIdentityCdpRowStatus_Object = MibTableColumn
hpicfDevIdentityCdpRowStatus = _HpicfDevIdentityCdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1, 3),
    _HpicfDevIdentityCdpRowStatus_Type()
)
hpicfDevIdentityCdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDevIdentityCdpRowStatus.setStatus("current")
_HpicfDeviceIdentityConformance_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityConformance = _HpicfDeviceIdentityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2)
)
_HpicfDeviceIdentityGroups_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityGroups = _HpicfDeviceIdentityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1)
)
_HpicfDeviceIdentityCompliances_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityCompliances = _HpicfDeviceIdentityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2)
)

# Managed Objects groups

hpicfDeviceIdentityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 1)
)
hpicfDeviceIdentityGroup.setObjects(
      *(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"))
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityGroup.setStatus("deprecated")

hpicfDeviceIdentityGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 2)
)
hpicfDeviceIdentityGroup1.setObjects(
      *(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpValue"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityGroup1.setStatus("deprecated")

hpicfDeviceIdentityGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 3)
)
hpicfDeviceIdentityGroup2.setObjects(
      *(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSysName"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSysDescr"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpValue"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfiDeviceIdentityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 1)
)
hpicfiDeviceIdentityCompliance.setObjects(
    ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityGroup")
)
if mibBuilder.loadTexts:
    hpicfiDeviceIdentityCompliance.setStatus(
        "deprecated"
    )

hpicfiDeviceIdentityCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 2)
)
hpicfiDeviceIdentityCompliance1.setObjects(
    ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityGroup1")
)
if mibBuilder.loadTexts:
    hpicfiDeviceIdentityCompliance1.setStatus(
        "deprecated"
    )

hpicfDeviceIdentityCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 3)
)
hpicfDeviceIdentityCompliance2.setObjects(
    ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityGroup2")
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DEVICEIDENTITY-MIB",
    **{"hpicfDeviceIdentityMIB": hpicfDeviceIdentityMIB,
       "hpicfDeviceIdentityConfig": hpicfDeviceIdentityConfig,
       "hpicfDeviceIdentityTable": hpicfDeviceIdentityTable,
       "hpicfDeviceIdentityEntry": hpicfDeviceIdentityEntry,
       "hpicfDeviceIdentityIndex": hpicfDeviceIdentityIndex,
       "hpicfDeviceIdentityRowStatus": hpicfDeviceIdentityRowStatus,
       "hpicfDeviceIdentityName": hpicfDeviceIdentityName,
       "hpicfDeviceIdentityLldpOui": hpicfDeviceIdentityLldpOui,
       "hpicfDeviceIdentityLldpSubType": hpicfDeviceIdentityLldpSubType,
       "hpicfDeviceIdentityLldpSysName": hpicfDeviceIdentityLldpSysName,
       "hpicfDeviceIdentityLldpSysDescr": hpicfDeviceIdentityLldpSysDescr,
       "hpicfCdpBypassTable": hpicfCdpBypassTable,
       "hpicfCdpBypassEntry": hpicfCdpBypassEntry,
       "hpicfDevIdentityCdpType": hpicfDevIdentityCdpType,
       "hpicfDevIdentityCdpValue": hpicfDevIdentityCdpValue,
       "hpicfDevIdentityCdpRowStatus": hpicfDevIdentityCdpRowStatus,
       "hpicfDeviceIdentityConformance": hpicfDeviceIdentityConformance,
       "hpicfDeviceIdentityGroups": hpicfDeviceIdentityGroups,
       "hpicfDeviceIdentityGroup": hpicfDeviceIdentityGroup,
       "hpicfDeviceIdentityGroup1": hpicfDeviceIdentityGroup1,
       "hpicfDeviceIdentityGroup2": hpicfDeviceIdentityGroup2,
       "hpicfDeviceIdentityCompliances": hpicfDeviceIdentityCompliances,
       "hpicfiDeviceIdentityCompliance": hpicfiDeviceIdentityCompliance,
       "hpicfiDeviceIdentityCompliance1": hpicfiDeviceIdentityCompliance1,
       "hpicfDeviceIdentityCompliance2": hpicfDeviceIdentityCompliance2}
)
