# SNMP MIB module (OS-FEAT-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-FEAT-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:01 2025
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

osFeatMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21)
)
if mibBuilder.loadTexts:
    osFeatMgmt.setRevisions(
        ("2010-10-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsFeatMgmtObjects_ObjectIdentity = ObjectIdentity
osFeatMgmtObjects = _OsFeatMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 1)
)
_OsFeatMgmtTable_Object = MibTable
osFeatMgmtTable = _OsFeatMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3)
)
if mibBuilder.loadTexts:
    osFeatMgmtTable.setStatus("current")
_OsFeatMgmtEntry_Object = MibTableRow
osFeatMgmtEntry = _OsFeatMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1)
)
osFeatMgmtEntry.setIndexNames(
    (0, "OS-FEAT-MGMT-MIB", "osFeatMgmtId"),
)
if mibBuilder.loadTexts:
    osFeatMgmtEntry.setStatus("current")


class _OsFeatMgmtId_Type(Integer32):
    """Custom type osFeatMgmtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("os940rTL10Gports", 1)
    )


_OsFeatMgmtId_Type.__name__ = "Integer32"
_OsFeatMgmtId_Object = MibTableColumn
osFeatMgmtId = _OsFeatMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 1),
    _OsFeatMgmtId_Type()
)
osFeatMgmtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osFeatMgmtId.setStatus("current")


class _OsFeatMgmtStatus_Type(Integer32):
    """Custom type osFeatMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("deny", 1),
          ("permit", 2))
    )


_OsFeatMgmtStatus_Type.__name__ = "Integer32"
_OsFeatMgmtStatus_Object = MibTableColumn
osFeatMgmtStatus = _OsFeatMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 2),
    _OsFeatMgmtStatus_Type()
)
osFeatMgmtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osFeatMgmtStatus.setStatus("current")
_OsFeatMgmtParam_Type = Unsigned32
_OsFeatMgmtParam_Object = MibTableColumn
osFeatMgmtParam = _OsFeatMgmtParam_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 3),
    _OsFeatMgmtParam_Type()
)
osFeatMgmtParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osFeatMgmtParam.setStatus("current")


class _OsFeatMgmtKey_Type(OctetString):
    """Custom type osFeatMgmtKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_OsFeatMgmtKey_Type.__name__ = "OctetString"
_OsFeatMgmtKey_Object = MibTableColumn
osFeatMgmtKey = _OsFeatMgmtKey_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 4),
    _OsFeatMgmtKey_Type()
)
osFeatMgmtKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osFeatMgmtKey.setStatus("current")
_OsFeatMgmtConformance_ObjectIdentity = ObjectIdentity
osFeatMgmtConformance = _OsFeatMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 100)
)
_OsFeatMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
osFeatMgmtMIBCompliances = _OsFeatMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 1)
)
_OsFeatMgmtMIBGroups_ObjectIdentity = ObjectIdentity
osFeatMgmtMIBGroups = _OsFeatMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 2)
)

# Managed Objects groups

osFeatMgmtMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 2, 1)
)
osFeatMgmtMandatoryGroup.setObjects(
      *(("OS-FEAT-MGMT-MIB", "osFeatMgmtStatus"),
        ("OS-FEAT-MGMT-MIB", "osFeatMgmtParam"),
        ("OS-FEAT-MGMT-MIB", "osFeatMgmtKey"))
)
if mibBuilder.loadTexts:
    osFeatMgmtMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osFeatMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 1, 1)
)
osFeatMgmtMIBCompliance.setObjects(
    ("OS-FEAT-MGMT-MIB", "osFeatMgmtMandatoryGroup")
)
if mibBuilder.loadTexts:
    osFeatMgmtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-FEAT-MGMT-MIB",
    **{"osFeatMgmt": osFeatMgmt,
       "osFeatMgmtObjects": osFeatMgmtObjects,
       "osFeatMgmtTable": osFeatMgmtTable,
       "osFeatMgmtEntry": osFeatMgmtEntry,
       "osFeatMgmtId": osFeatMgmtId,
       "osFeatMgmtStatus": osFeatMgmtStatus,
       "osFeatMgmtParam": osFeatMgmtParam,
       "osFeatMgmtKey": osFeatMgmtKey,
       "osFeatMgmtConformance": osFeatMgmtConformance,
       "osFeatMgmtMIBCompliances": osFeatMgmtMIBCompliances,
       "osFeatMgmtMIBCompliance": osFeatMgmtMIBCompliance,
       "osFeatMgmtMIBGroups": osFeatMgmtMIBGroups,
       "osFeatMgmtMandatoryGroup": osFeatMgmtMandatoryGroup}
)
