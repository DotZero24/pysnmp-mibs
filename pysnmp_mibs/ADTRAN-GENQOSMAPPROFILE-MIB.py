# SNMP MIB module (ADTRAN-GENQOSMAPPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENQOSMAPPROFILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:52 2025
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

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

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

adGenQosMapProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 83)
)
if mibBuilder.loadTexts:
    adGenQosMapProfileMIB.setRevisions(
        ("2012-05-17 00:00",
         "2012-04-09 04:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenQosMapProfile_ObjectIdentity = ObjectIdentity
adGenQosMapProfile = _AdGenQosMapProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 83)
)
_AdGenQosMapProfileProvisioning_ObjectIdentity = ObjectIdentity
adGenQosMapProfileProvisioning = _AdGenQosMapProfileProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 1)
)
_AdGenQosMapProfileProvisioningTable_Object = MibTable
adGenQosMapProfileProvisioningTable = _AdGenQosMapProfileProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 1, 1)
)
if mibBuilder.loadTexts:
    adGenQosMapProfileProvisioningTable.setStatus("current")
_AdGenQosMapProfileProvisioningEntry_Object = MibTableRow
adGenQosMapProfileProvisioningEntry = _AdGenQosMapProfileProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 1, 1, 1)
)
adGenQosMapProfileProvisioningEntry.setIndexNames(
    (1, "ADTRAN-GENQOSMAPPROFILE-MIB", "adGenQosMapProfileName"),
)
if mibBuilder.loadTexts:
    adGenQosMapProfileProvisioningEntry.setStatus("current")


class _AdGenQosMapProfileName_Type(DisplayString):
    """Custom type adGenQosMapProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenQosMapProfileName_Type.__name__ = "DisplayString"
_AdGenQosMapProfileName_Object = MibTableColumn
adGenQosMapProfileName = _AdGenQosMapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 1, 1, 1, 1),
    _AdGenQosMapProfileName_Type()
)
adGenQosMapProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenQosMapProfileName.setStatus("current")
_AdGenQosMapProfileClassification_Type = OctetString
_AdGenQosMapProfileClassification_Object = MibTableColumn
adGenQosMapProfileClassification = _AdGenQosMapProfileClassification_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 1, 1, 1, 2),
    _AdGenQosMapProfileClassification_Type()
)
adGenQosMapProfileClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenQosMapProfileClassification.setStatus("current")
_AdGenQosMapProfileRowStatus_Type = RowStatus
_AdGenQosMapProfileRowStatus_Object = MibTableColumn
adGenQosMapProfileRowStatus = _AdGenQosMapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 1, 1, 1, 3),
    _AdGenQosMapProfileRowStatus_Type()
)
adGenQosMapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenQosMapProfileRowStatus.setStatus("current")


class _AdGenQosMapProfileDescription_Type(DisplayString):
    """Custom type adGenQosMapProfileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenQosMapProfileDescription_Type.__name__ = "DisplayString"
_AdGenQosMapProfileDescription_Object = MibTableColumn
adGenQosMapProfileDescription = _AdGenQosMapProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 1, 1, 1, 4),
    _AdGenQosMapProfileDescription_Type()
)
adGenQosMapProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenQosMapProfileDescription.setStatus("current")
_AdGenQosMapProfileStatus_ObjectIdentity = ObjectIdentity
adGenQosMapProfileStatus = _AdGenQosMapProfileStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 2)
)
_AdGenQosMapProfileLastInsertStatus_Type = DisplayString
_AdGenQosMapProfileLastInsertStatus_Object = MibScalar
adGenQosMapProfileLastInsertStatus = _AdGenQosMapProfileLastInsertStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 2, 1),
    _AdGenQosMapProfileLastInsertStatus_Type()
)
adGenQosMapProfileLastInsertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenQosMapProfileLastInsertStatus.setStatus("current")
_AdGenQosMapProfileMaxAllowedProfiles_Type = Unsigned32
_AdGenQosMapProfileMaxAllowedProfiles_Object = MibScalar
adGenQosMapProfileMaxAllowedProfiles = _AdGenQosMapProfileMaxAllowedProfiles_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 2, 2),
    _AdGenQosMapProfileMaxAllowedProfiles_Type()
)
adGenQosMapProfileMaxAllowedProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenQosMapProfileMaxAllowedProfiles.setStatus("current")
_AdGenQosMapProfileCurrentProfileCount_Type = Unsigned32
_AdGenQosMapProfileCurrentProfileCount_Object = MibScalar
adGenQosMapProfileCurrentProfileCount = _AdGenQosMapProfileCurrentProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 83, 2, 3),
    _AdGenQosMapProfileCurrentProfileCount_Type()
)
adGenQosMapProfileCurrentProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenQosMapProfileCurrentProfileCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENQOSMAPPROFILE-MIB",
    **{"adGenQosMapProfile": adGenQosMapProfile,
       "adGenQosMapProfileProvisioning": adGenQosMapProfileProvisioning,
       "adGenQosMapProfileProvisioningTable": adGenQosMapProfileProvisioningTable,
       "adGenQosMapProfileProvisioningEntry": adGenQosMapProfileProvisioningEntry,
       "adGenQosMapProfileName": adGenQosMapProfileName,
       "adGenQosMapProfileClassification": adGenQosMapProfileClassification,
       "adGenQosMapProfileRowStatus": adGenQosMapProfileRowStatus,
       "adGenQosMapProfileDescription": adGenQosMapProfileDescription,
       "adGenQosMapProfileStatus": adGenQosMapProfileStatus,
       "adGenQosMapProfileLastInsertStatus": adGenQosMapProfileLastInsertStatus,
       "adGenQosMapProfileMaxAllowedProfiles": adGenQosMapProfileMaxAllowedProfiles,
       "adGenQosMapProfileCurrentProfileCount": adGenQosMapProfileCurrentProfileCount,
       "adGenQosMapProfileMIB": adGenQosMapProfileMIB}
)
