# SNMP MIB module (ADTRAN-GENREMOTEDOWNLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENREMOTEDOWNLOAD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:56 2025
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

(adGenRemoteDownload,
 adGenRemoteDownloadID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenRemoteDownload",
    "adGenRemoteDownloadID")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenRemoteDownloadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 33, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenRemoteDownloadProvisioning_ObjectIdentity = ObjectIdentity
adGenRemoteDownloadProvisioning = _AdGenRemoteDownloadProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 1)
)
_AdGenRemoteDownloadProvTable_Object = MibTable
adGenRemoteDownloadProvTable = _AdGenRemoteDownloadProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 1, 1)
)
if mibBuilder.loadTexts:
    adGenRemoteDownloadProvTable.setStatus("current")
_AdGenRemoteDownloadProvEntry_Object = MibTableRow
adGenRemoteDownloadProvEntry = _AdGenRemoteDownloadProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 1, 1, 1)
)
adGenRemoteDownloadProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenRemoteDownloadProvEntry.setStatus("current")
_AdGenRemoteDownloadFilename_Type = DisplayString
_AdGenRemoteDownloadFilename_Object = MibTableColumn
adGenRemoteDownloadFilename = _AdGenRemoteDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 1, 1, 1, 1),
    _AdGenRemoteDownloadFilename_Type()
)
adGenRemoteDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenRemoteDownloadFilename.setStatus("current")


class _AdGenRemoteDownloadInitiate_Type(Integer32):
    """Custom type adGenRemoteDownloadInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiate", 1)
    )


_AdGenRemoteDownloadInitiate_Type.__name__ = "Integer32"
_AdGenRemoteDownloadInitiate_Object = MibTableColumn
adGenRemoteDownloadInitiate = _AdGenRemoteDownloadInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 1, 1, 1, 2),
    _AdGenRemoteDownloadInitiate_Type()
)
adGenRemoteDownloadInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenRemoteDownloadInitiate.setStatus("current")


class _AdGenRemoteDownloadReboot_Type(Integer32):
    """Custom type adGenRemoteDownloadReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_AdGenRemoteDownloadReboot_Type.__name__ = "Integer32"
_AdGenRemoteDownloadReboot_Object = MibTableColumn
adGenRemoteDownloadReboot = _AdGenRemoteDownloadReboot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 1, 1, 1, 3),
    _AdGenRemoteDownloadReboot_Type()
)
adGenRemoteDownloadReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenRemoteDownloadReboot.setStatus("current")
_AdGenRemoteDownloadStatus_ObjectIdentity = ObjectIdentity
adGenRemoteDownloadStatus = _AdGenRemoteDownloadStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 2)
)
_AdGenRemoteDownloadStatusTable_Object = MibTable
adGenRemoteDownloadStatusTable = _AdGenRemoteDownloadStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 2, 1)
)
if mibBuilder.loadTexts:
    adGenRemoteDownloadStatusTable.setStatus("current")
_AdGenRemoteDownloadStatusEntry_Object = MibTableRow
adGenRemoteDownloadStatusEntry = _AdGenRemoteDownloadStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 2, 1, 1)
)
adGenRemoteDownloadStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenRemoteDownloadStatusEntry.setStatus("current")


class _AdGenRemoteDownloadStatusSummary_Type(Integer32):
    """Custom type adGenRemoteDownloadStatusSummary based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("error", 3),
          ("success", 4))
    )


_AdGenRemoteDownloadStatusSummary_Type.__name__ = "Integer32"
_AdGenRemoteDownloadStatusSummary_Object = MibTableColumn
adGenRemoteDownloadStatusSummary = _AdGenRemoteDownloadStatusSummary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 2, 1, 1, 1),
    _AdGenRemoteDownloadStatusSummary_Type()
)
adGenRemoteDownloadStatusSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRemoteDownloadStatusSummary.setStatus("current")
_AdGenRemoteDownloadStatusString_Type = DisplayString
_AdGenRemoteDownloadStatusString_Object = MibTableColumn
adGenRemoteDownloadStatusString = _AdGenRemoteDownloadStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 33, 2, 1, 1, 2),
    _AdGenRemoteDownloadStatusString_Type()
)
adGenRemoteDownloadStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRemoteDownloadStatusString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENREMOTEDOWNLOAD-MIB",
    **{"adGenRemoteDownloadProvisioning": adGenRemoteDownloadProvisioning,
       "adGenRemoteDownloadProvTable": adGenRemoteDownloadProvTable,
       "adGenRemoteDownloadProvEntry": adGenRemoteDownloadProvEntry,
       "adGenRemoteDownloadFilename": adGenRemoteDownloadFilename,
       "adGenRemoteDownloadInitiate": adGenRemoteDownloadInitiate,
       "adGenRemoteDownloadReboot": adGenRemoteDownloadReboot,
       "adGenRemoteDownloadStatus": adGenRemoteDownloadStatus,
       "adGenRemoteDownloadStatusTable": adGenRemoteDownloadStatusTable,
       "adGenRemoteDownloadStatusEntry": adGenRemoteDownloadStatusEntry,
       "adGenRemoteDownloadStatusSummary": adGenRemoteDownloadStatusSummary,
       "adGenRemoteDownloadStatusString": adGenRemoteDownloadStatusString,
       "adGenRemoteDownloadMIB": adGenRemoteDownloadMIB}
)
