# SNMP MIB module (BRCM-PARENTALCONTROL-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-PARENTALCONTROL-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:17 2025
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

(cableDataMgmtMIBObjects,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtMIBObjects")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

parentalControlMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    parentalControlMgmt.setRevisions(
        ("2007-02-05 00:00",
         "2003-07-30 00:00",
         "2003-04-17 00:00",
         "2003-04-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PctlService_ObjectIdentity = ObjectIdentity
pctlService = _PctlService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1)
)
_PctlSubscriptionURL_Type = DisplayString
_PctlSubscriptionURL_Object = MibScalar
pctlSubscriptionURL = _PctlSubscriptionURL_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 1),
    _PctlSubscriptionURL_Type()
)
pctlSubscriptionURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlSubscriptionURL.setStatus("current")


class _PctlServiceModel_Type(Integer32):
    """Custom type pctlServiceModel based on Integer32"""
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
          ("cerberianCMR", 1),
          ("cerberianADR", 2),
          ("rulespace", 3))
    )


_PctlServiceModel_Type.__name__ = "Integer32"
_PctlServiceModel_Object = MibScalar
pctlServiceModel = _PctlServiceModel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 2),
    _PctlServiceModel_Type()
)
pctlServiceModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlServiceModel.setStatus("current")
_PctlServicePrimaryURL_Type = DisplayString
_PctlServicePrimaryURL_Object = MibScalar
pctlServicePrimaryURL = _PctlServicePrimaryURL_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 3),
    _PctlServicePrimaryURL_Type()
)
pctlServicePrimaryURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlServicePrimaryURL.setStatus("current")
_PctlServiceSecondaryURL_Type = DisplayString
_PctlServiceSecondaryURL_Object = MibScalar
pctlServiceSecondaryURL = _PctlServiceSecondaryURL_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 4),
    _PctlServiceSecondaryURL_Type()
)
pctlServiceSecondaryURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlServiceSecondaryURL.setStatus("current")
_PctlLicenseKey_Type = OctetString
_PctlLicenseKey_Object = MibScalar
pctlLicenseKey = _PctlLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 5),
    _PctlLicenseKey_Type()
)
pctlLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlLicenseKey.setStatus("current")
_PctlLicenseExpiration_Type = DateAndTime
_PctlLicenseExpiration_Object = MibScalar
pctlLicenseExpiration = _PctlLicenseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 6),
    _PctlLicenseExpiration_Type()
)
pctlLicenseExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlLicenseExpiration.setStatus("current")
_PctlServiceSubscribeNow_Type = TruthValue
_PctlServiceSubscribeNow_Object = MibScalar
pctlServiceSubscribeNow = _PctlServiceSubscribeNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 7),
    _PctlServiceSubscribeNow_Type()
)
pctlServiceSubscribeNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlServiceSubscribeNow.setStatus("current")


class _PctlServiceSubscriptionStatus_Type(Integer32):
    """Custom type pctlServiceSubscriptionStatus based on Integer32"""
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
        *(("notAttempted", 0),
          ("readyToSubscribe", 1),
          ("subscribedServiceNotStarted", 2),
          ("subscribedEstablishingService", 3),
          ("subscribedServiceRunning", 4),
          ("subscribedServiceError", 5),
          ("subscriptionFailed", 6),
          ("subscriptionExpired", 7))
    )


_PctlServiceSubscriptionStatus_Type.__name__ = "Integer32"
_PctlServiceSubscriptionStatus_Object = MibScalar
pctlServiceSubscriptionStatus = _PctlServiceSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 8),
    _PctlServiceSubscriptionStatus_Type()
)
pctlServiceSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctlServiceSubscriptionStatus.setStatus("current")


class _PctlCategoryList_Type(OctetString):
    """Custom type pctlCategoryList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PctlCategoryList_Type.__name__ = "OctetString"
_PctlCategoryList_Object = MibScalar
pctlCategoryList = _PctlCategoryList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 8, 1, 9),
    _PctlCategoryList_Type()
)
pctlCategoryList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctlCategoryList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-PARENTALCONTROL-MGMT-MIB",
    **{"parentalControlMgmt": parentalControlMgmt,
       "pctlService": pctlService,
       "pctlSubscriptionURL": pctlSubscriptionURL,
       "pctlServiceModel": pctlServiceModel,
       "pctlServicePrimaryURL": pctlServicePrimaryURL,
       "pctlServiceSecondaryURL": pctlServiceSecondaryURL,
       "pctlLicenseKey": pctlLicenseKey,
       "pctlLicenseExpiration": pctlLicenseExpiration,
       "pctlServiceSubscribeNow": pctlServiceSubscribeNow,
       "pctlServiceSubscriptionStatus": pctlServiceSubscriptionStatus,
       "pctlCategoryList": pctlCategoryList}
)
