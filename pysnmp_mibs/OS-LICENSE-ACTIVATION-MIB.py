# SNMP MIB module (OS-LICENSE-ACTIVATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-LICENSE-ACTIVATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:56 2025
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

osLicenseActivation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27)
)
if mibBuilder.loadTexts:
    osLicenseActivation.setRevisions(
        ("2014-02-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OsActivationLicense(TextualConvention, OctetString):
    status = "current"
    displayHint = "12a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12



class OsActivationStatus(TextualConvention, Integer32):
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
          ("active", 2),
          ("notActive", 3),
          ("notSupported", 4))
    )



# MIB Managed Objects in the order of their OIDs

_OsRoutingProtocolsActivation_ObjectIdentity = ObjectIdentity
osRoutingProtocolsActivation = _OsRoutingProtocolsActivation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 1)
)
_OsRoutingProtocolsActivationLicense_Type = OsActivationLicense
_OsRoutingProtocolsActivationLicense_Object = MibScalar
osRoutingProtocolsActivationLicense = _OsRoutingProtocolsActivationLicense_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 1, 1),
    _OsRoutingProtocolsActivationLicense_Type()
)
osRoutingProtocolsActivationLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osRoutingProtocolsActivationLicense.setStatus("current")
_OsRoutingProtocolsActivationSatus_Type = OsActivationStatus
_OsRoutingProtocolsActivationSatus_Object = MibScalar
osRoutingProtocolsActivationSatus = _OsRoutingProtocolsActivationSatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 1, 2),
    _OsRoutingProtocolsActivationSatus_Type()
)
osRoutingProtocolsActivationSatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osRoutingProtocolsActivationSatus.setStatus("current")
_OsMplsActivation_ObjectIdentity = ObjectIdentity
osMplsActivation = _OsMplsActivation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 2)
)
_OsMplsActivationLicense_Type = OsActivationLicense
_OsMplsActivationLicense_Object = MibScalar
osMplsActivationLicense = _OsMplsActivationLicense_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 2, 1),
    _OsMplsActivationLicense_Type()
)
osMplsActivationLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osMplsActivationLicense.setStatus("current")
_OsMplsActivationSatus_Type = OsActivationStatus
_OsMplsActivationSatus_Object = MibScalar
osMplsActivationSatus = _OsMplsActivationSatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 2, 2),
    _OsMplsActivationSatus_Type()
)
osMplsActivationSatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osMplsActivationSatus.setStatus("current")
_OsActvFeatMgmtTable_Object = MibTable
osActvFeatMgmtTable = _OsActvFeatMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 8)
)
if mibBuilder.loadTexts:
    osActvFeatMgmtTable.setStatus("current")
_OsActvFeatMgmtEntry_Object = MibTableRow
osActvFeatMgmtEntry = _OsActvFeatMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1)
)
osActvFeatMgmtEntry.setIndexNames(
    (0, "OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtId"),
)
if mibBuilder.loadTexts:
    osActvFeatMgmtEntry.setStatus("current")


class _OsActvFeatMgmtId_Type(Integer32):
    """Custom type osActvFeatMgmtId based on Integer32"""
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
        *(("os600withGigaPorts", 1),
          ("securePush", 2),
          ("routingProtocols", 3),
          ("mplsProtocols", 4))
    )


_OsActvFeatMgmtId_Type.__name__ = "Integer32"
_OsActvFeatMgmtId_Object = MibTableColumn
osActvFeatMgmtId = _OsActvFeatMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 1),
    _OsActvFeatMgmtId_Type()
)
osActvFeatMgmtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osActvFeatMgmtId.setStatus("current")
_OsActvFeatMgmtStatus_Type = OsActivationStatus
_OsActvFeatMgmtStatus_Object = MibTableColumn
osActvFeatMgmtStatus = _OsActvFeatMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 2),
    _OsActvFeatMgmtStatus_Type()
)
osActvFeatMgmtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osActvFeatMgmtStatus.setStatus("current")
_OsActvFeatMgmtParam_Type = Unsigned32
_OsActvFeatMgmtParam_Object = MibTableColumn
osActvFeatMgmtParam = _OsActvFeatMgmtParam_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 3),
    _OsActvFeatMgmtParam_Type()
)
osActvFeatMgmtParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osActvFeatMgmtParam.setStatus("current")
_OsActvFeatMgmtKey_Type = OsActivationLicense
_OsActvFeatMgmtKey_Object = MibTableColumn
osActvFeatMgmtKey = _OsActvFeatMgmtKey_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 4),
    _OsActvFeatMgmtKey_Type()
)
osActvFeatMgmtKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osActvFeatMgmtKey.setStatus("current")
_OsLicenseActivationConformance_ObjectIdentity = ObjectIdentity
osLicenseActivationConformance = _OsLicenseActivationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 100)
)
_OsLicenseActivationMIBCompliances_ObjectIdentity = ObjectIdentity
osLicenseActivationMIBCompliances = _OsLicenseActivationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 1)
)
_OsLicenseActivationMIBGroups_ObjectIdentity = ObjectIdentity
osLicenseActivationMIBGroups = _OsLicenseActivationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 2)
)

# Managed Objects groups

osLicenseActivationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 2, 1)
)
osLicenseActivationMIBGroup.setObjects(
      *(("OS-LICENSE-ACTIVATION-MIB", "osRoutingProtocolsActivationLicense"),
        ("OS-LICENSE-ACTIVATION-MIB", "osRoutingProtocolsActivationSatus"),
        ("OS-LICENSE-ACTIVATION-MIB", "osMplsActivationLicense"),
        ("OS-LICENSE-ACTIVATION-MIB", "osMplsActivationSatus"),
        ("OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtStatus"),
        ("OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtParam"),
        ("OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtKey"))
)
if mibBuilder.loadTexts:
    osLicenseActivationMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osLicenseActivationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 1, 1)
)
osLicenseActivationMIBCompliance.setObjects(
    ("OS-LICENSE-ACTIVATION-MIB", "osLicenseActivationMIBGroup")
)
if mibBuilder.loadTexts:
    osLicenseActivationMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-LICENSE-ACTIVATION-MIB",
    **{"OsActivationLicense": OsActivationLicense,
       "OsActivationStatus": OsActivationStatus,
       "osLicenseActivation": osLicenseActivation,
       "osRoutingProtocolsActivation": osRoutingProtocolsActivation,
       "osRoutingProtocolsActivationLicense": osRoutingProtocolsActivationLicense,
       "osRoutingProtocolsActivationSatus": osRoutingProtocolsActivationSatus,
       "osMplsActivation": osMplsActivation,
       "osMplsActivationLicense": osMplsActivationLicense,
       "osMplsActivationSatus": osMplsActivationSatus,
       "osActvFeatMgmtTable": osActvFeatMgmtTable,
       "osActvFeatMgmtEntry": osActvFeatMgmtEntry,
       "osActvFeatMgmtId": osActvFeatMgmtId,
       "osActvFeatMgmtStatus": osActvFeatMgmtStatus,
       "osActvFeatMgmtParam": osActvFeatMgmtParam,
       "osActvFeatMgmtKey": osActvFeatMgmtKey,
       "osLicenseActivationConformance": osLicenseActivationConformance,
       "osLicenseActivationMIBCompliances": osLicenseActivationMIBCompliances,
       "osLicenseActivationMIBCompliance": osLicenseActivationMIBCompliance,
       "osLicenseActivationMIBGroups": osLicenseActivationMIBGroups,
       "osLicenseActivationMIBGroup": osLicenseActivationMIBGroup}
)
