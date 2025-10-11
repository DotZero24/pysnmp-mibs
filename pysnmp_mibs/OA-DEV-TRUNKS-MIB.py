# SNMP MIB module (OA-DEV-TRUNKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-DEV-TRUNKS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:59 2025
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

oaDeviceTrunks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23)
)
if mibBuilder.loadTexts:
    oaDeviceTrunks.setRevisions(
        ("2007-12-11 00:00",
         "2007-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbDeviceConfig_ObjectIdentity = ObjectIdentity
nbDeviceConfig = _NbDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11)
)
_NbDevGen_ObjectIdentity = ObjectIdentity
nbDevGen = _NbDevGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1)
)
_OaDevTrunkGen_ObjectIdentity = ObjectIdentity
oaDevTrunkGen = _OaDevTrunkGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 1)
)


class _OaDevTrunkGenSupport_Type(Integer32):
    """Custom type oaDevTrunkGenSupport based on Integer32"""
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


_OaDevTrunkGenSupport_Type.__name__ = "Integer32"
_OaDevTrunkGenSupport_Object = MibScalar
oaDevTrunkGenSupport = _OaDevTrunkGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 1, 1),
    _OaDevTrunkGenSupport_Type()
)
oaDevTrunkGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrunkGenSupport.setStatus("current")
_OaDevTrunks_ObjectIdentity = ObjectIdentity
oaDevTrunks = _OaDevTrunks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2)
)
_OaDevTrunkGrNumber_Type = Integer32
_OaDevTrunkGrNumber_Object = MibScalar
oaDevTrunkGrNumber = _OaDevTrunkGrNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 1),
    _OaDevTrunkGrNumber_Type()
)
oaDevTrunkGrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrunkGrNumber.setStatus("current")
_OaDevTrunkGrTable_Object = MibTable
oaDevTrunkGrTable = _OaDevTrunkGrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5)
)
if mibBuilder.loadTexts:
    oaDevTrunkGrTable.setStatus("current")
_OaDevTrunkGrEntry_Object = MibTableRow
oaDevTrunkGrEntry = _OaDevTrunkGrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5, 1)
)
oaDevTrunkGrEntry.setIndexNames(
    (0, "OA-DEV-TRUNKS-MIB", "oaDevTrunkGrId"),
)
if mibBuilder.loadTexts:
    oaDevTrunkGrEntry.setStatus("current")


class _OaDevTrunkGrId_Type(Integer32):
    """Custom type oaDevTrunkGrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OaDevTrunkGrId_Type.__name__ = "Integer32"
_OaDevTrunkGrId_Object = MibTableColumn
oaDevTrunkGrId = _OaDevTrunkGrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5, 1, 1),
    _OaDevTrunkGrId_Type()
)
oaDevTrunkGrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaDevTrunkGrId.setStatus("current")


class _OaDevTrunkGrDescription_Type(DisplayString):
    """Custom type oaDevTrunkGrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OaDevTrunkGrDescription_Type.__name__ = "DisplayString"
_OaDevTrunkGrDescription_Object = MibTableColumn
oaDevTrunkGrDescription = _OaDevTrunkGrDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5, 1, 2),
    _OaDevTrunkGrDescription_Type()
)
oaDevTrunkGrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevTrunkGrDescription.setStatus("current")


class _OaDevTrunkGrPortMembers_Type(OctetString):
    """Custom type oaDevTrunkGrPortMembers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OaDevTrunkGrPortMembers_Type.__name__ = "OctetString"
_OaDevTrunkGrPortMembers_Object = MibTableColumn
oaDevTrunkGrPortMembers = _OaDevTrunkGrPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5, 1, 3),
    _OaDevTrunkGrPortMembers_Type()
)
oaDevTrunkGrPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevTrunkGrPortMembers.setStatus("current")
_OaDevTrunkGrPortsNumber_Type = Integer32
_OaDevTrunkGrPortsNumber_Object = MibTableColumn
oaDevTrunkGrPortsNumber = _OaDevTrunkGrPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5, 1, 4),
    _OaDevTrunkGrPortsNumber_Type()
)
oaDevTrunkGrPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrunkGrPortsNumber.setStatus("current")


class _OaDevTrunkGrAdminStatus_Type(Integer32):
    """Custom type oaDevTrunkGrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("validId", 1),
          ("invalid", 2),
          ("validNoId", 3))
    )


_OaDevTrunkGrAdminStatus_Type.__name__ = "Integer32"
_OaDevTrunkGrAdminStatus_Object = MibTableColumn
oaDevTrunkGrAdminStatus = _OaDevTrunkGrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5, 1, 5),
    _OaDevTrunkGrAdminStatus_Type()
)
oaDevTrunkGrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevTrunkGrAdminStatus.setStatus("current")
_OaDevTrunkGrPortLogicalNumber_Type = Integer32
_OaDevTrunkGrPortLogicalNumber_Object = MibTableColumn
oaDevTrunkGrPortLogicalNumber = _OaDevTrunkGrPortLogicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 2, 5, 1, 6),
    _OaDevTrunkGrPortLogicalNumber_Type()
)
oaDevTrunkGrPortLogicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevTrunkGrPortLogicalNumber.setStatus("current")
_OaDevTrunkConformance_ObjectIdentity = ObjectIdentity
oaDevTrunkConformance = _OaDevTrunkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 101)
)
_OaDevTrunkMIBCompliances_ObjectIdentity = ObjectIdentity
oaDevTrunkMIBCompliances = _OaDevTrunkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 101, 1)
)
_OaDevTrunkMIBGroups_ObjectIdentity = ObjectIdentity
oaDevTrunkMIBGroups = _OaDevTrunkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 101, 2)
)

# Managed Objects groups

oaDevTrunkMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 101, 2, 1)
)
oaDevTrunkMandatoryGroup.setObjects(
      *(("OA-DEV-TRUNKS-MIB", "oaDevTrunkGenSupport"),
        ("OA-DEV-TRUNKS-MIB", "oaDevTrunkGrNumber"),
        ("OA-DEV-TRUNKS-MIB", "oaDevTrunkGrDescription"),
        ("OA-DEV-TRUNKS-MIB", "oaDevTrunkGrPortMembers"),
        ("OA-DEV-TRUNKS-MIB", "oaDevTrunkGrPortsNumber"),
        ("OA-DEV-TRUNKS-MIB", "oaDevTrunkGrAdminStatus"),
        ("OA-DEV-TRUNKS-MIB", "oaDevTrunkGrPortLogicalNumber"))
)
if mibBuilder.loadTexts:
    oaDevTrunkMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaDevTrunkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 23, 101, 1, 1)
)
oaDevTrunkMIBCompliance.setObjects(
    ("OA-DEV-TRUNKS-MIB", "oaDevTrunkMandatoryGroup")
)
if mibBuilder.loadTexts:
    oaDevTrunkMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-DEV-TRUNKS-MIB",
    **{"nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbDeviceConfig": nbDeviceConfig,
       "nbDevGen": nbDevGen,
       "oaDeviceTrunks": oaDeviceTrunks,
       "oaDevTrunkGen": oaDevTrunkGen,
       "oaDevTrunkGenSupport": oaDevTrunkGenSupport,
       "oaDevTrunks": oaDevTrunks,
       "oaDevTrunkGrNumber": oaDevTrunkGrNumber,
       "oaDevTrunkGrTable": oaDevTrunkGrTable,
       "oaDevTrunkGrEntry": oaDevTrunkGrEntry,
       "oaDevTrunkGrId": oaDevTrunkGrId,
       "oaDevTrunkGrDescription": oaDevTrunkGrDescription,
       "oaDevTrunkGrPortMembers": oaDevTrunkGrPortMembers,
       "oaDevTrunkGrPortsNumber": oaDevTrunkGrPortsNumber,
       "oaDevTrunkGrAdminStatus": oaDevTrunkGrAdminStatus,
       "oaDevTrunkGrPortLogicalNumber": oaDevTrunkGrPortLogicalNumber,
       "oaDevTrunkConformance": oaDevTrunkConformance,
       "oaDevTrunkMIBCompliances": oaDevTrunkMIBCompliances,
       "oaDevTrunkMIBCompliance": oaDevTrunkMIBCompliance,
       "oaDevTrunkMIBGroups": oaDevTrunkMIBGroups,
       "oaDevTrunkMandatoryGroup": oaDevTrunkMandatoryGroup}
)
