# SNMP MIB module (ADTRAN-GENMEVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMEVC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:26 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenMEVC,
 adGenMEVCID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenMEVC",
    "adGenMEVCID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

adGenMEVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 27, 1)
)
if mibBuilder.loadTexts:
    adGenMEVCMIB.setRevisions(
        ("2015-01-12 00:00",
         "2013-07-03 00:00",
         "2011-08-26 00:00",
         "2011-02-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMEVCEvents_ObjectIdentity = ObjectIdentity
adGenMEVCEvents = _AdGenMEVCEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 0)
)
_AdGenMEVCProvisioning_ObjectIdentity = ObjectIdentity
adGenMEVCProvisioning = _AdGenMEVCProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1)
)
_AdGenMEVCTable_Object = MibTable
adGenMEVCTable = _AdGenMEVCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMEVCTable.setStatus("current")
_AdGenMEVCEntry_Object = MibTableRow
adGenMEVCEntry = _AdGenMEVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1)
)
adGenMEVCEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENMEVC-MIB", "adGenMEVCName"),
)
if mibBuilder.loadTexts:
    adGenMEVCEntry.setStatus("current")


class _AdGenMEVCName_Type(DisplayString):
    """Custom type adGenMEVCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMEVCName_Type.__name__ = "DisplayString"
_AdGenMEVCName_Object = MibTableColumn
adGenMEVCName = _AdGenMEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 1),
    _AdGenMEVCName_Type()
)
adGenMEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMEVCName.setStatus("current")
_AdGenMEVCRowStatus_Type = RowStatus
_AdGenMEVCRowStatus_Object = MibTableColumn
adGenMEVCRowStatus = _AdGenMEVCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 2),
    _AdGenMEVCRowStatus_Type()
)
adGenMEVCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCRowStatus.setStatus("current")


class _AdGenMEVCOperStatus_Type(Integer32):
    """Custom type adGenMEVCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AdGenMEVCOperStatus_Type.__name__ = "Integer32"
_AdGenMEVCOperStatus_Object = MibTableColumn
adGenMEVCOperStatus = _AdGenMEVCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 3),
    _AdGenMEVCOperStatus_Type()
)
adGenMEVCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCOperStatus.setStatus("current")
_AdGenMEVCStatus_Type = DisplayString
_AdGenMEVCStatus_Object = MibTableColumn
adGenMEVCStatus = _AdGenMEVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 4),
    _AdGenMEVCStatus_Type()
)
adGenMEVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCStatus.setStatus("current")
_AdGenMEVCSTagVID_Type = Integer32
_AdGenMEVCSTagVID_Object = MibTableColumn
adGenMEVCSTagVID = _AdGenMEVCSTagVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 5),
    _AdGenMEVCSTagVID_Type()
)
adGenMEVCSTagVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCSTagVID.setStatus("current")


class _AdGenMEVCPreserveCEVlanId_Type(Integer32):
    """Custom type adGenMEVCPreserveCEVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenMEVCPreserveCEVlanId_Type.__name__ = "Integer32"
_AdGenMEVCPreserveCEVlanId_Object = MibTableColumn
adGenMEVCPreserveCEVlanId = _AdGenMEVCPreserveCEVlanId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 6),
    _AdGenMEVCPreserveCEVlanId_Type()
)
adGenMEVCPreserveCEVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCPreserveCEVlanId.setStatus("current")


class _AdGenMEVCMacSwitching_Type(Integer32):
    """Custom type adGenMEVCMacSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenMEVCMacSwitching_Type.__name__ = "Integer32"
_AdGenMEVCMacSwitching_Object = MibTableColumn
adGenMEVCMacSwitching = _AdGenMEVCMacSwitching_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 7),
    _AdGenMEVCMacSwitching_Type()
)
adGenMEVCMacSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCMacSwitching.setStatus("current")
_AdGenMEVCNumberOfInterfaces_Type = Integer32
_AdGenMEVCNumberOfInterfaces_Object = MibTableColumn
adGenMEVCNumberOfInterfaces = _AdGenMEVCNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 8),
    _AdGenMEVCNumberOfInterfaces_Type()
)
adGenMEVCNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCNumberOfInterfaces.setStatus("current")
_AdGenMEVCLastError_Type = DisplayString
_AdGenMEVCLastError_Object = MibTableColumn
adGenMEVCLastError = _AdGenMEVCLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 9),
    _AdGenMEVCLastError_Type()
)
adGenMEVCLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCLastError.setStatus("current")


class _AdGenMevcManagement_Type(Integer32):
    """Custom type adGenMevcManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local", 2),
          ("system", 3))
    )


_AdGenMevcManagement_Type.__name__ = "Integer32"
_AdGenMevcManagement_Object = MibTableColumn
adGenMevcManagement = _AdGenMevcManagement_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 10),
    _AdGenMevcManagement_Type()
)
adGenMevcManagement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMevcManagement.setStatus("current")


class _AdGenMEVCIGMPImmediateLeave_Type(Integer32):
    """Custom type adGenMEVCIGMPImmediateLeave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenMEVCIGMPImmediateLeave_Type.__name__ = "Integer32"
_AdGenMEVCIGMPImmediateLeave_Object = MibTableColumn
adGenMEVCIGMPImmediateLeave = _AdGenMEVCIGMPImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 11),
    _AdGenMEVCIGMPImmediateLeave_Type()
)
adGenMEVCIGMPImmediateLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCIGMPImmediateLeave.setStatus("current")


class _AdGenMEVCIGMPTimeOutInterval_Type(Integer32):
    """Custom type adGenMEVCIGMPTimeOutInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdGenMEVCIGMPTimeOutInterval_Type.__name__ = "Integer32"
_AdGenMEVCIGMPTimeOutInterval_Object = MibTableColumn
adGenMEVCIGMPTimeOutInterval = _AdGenMEVCIGMPTimeOutInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 12),
    _AdGenMEVCIGMPTimeOutInterval_Type()
)
adGenMEVCIGMPTimeOutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCIGMPTimeOutInterval.setStatus("current")


class _AdGenMEVCIGMPMode_Type(Integer32):
    """Custom type adGenMEVCIGMPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("snooping", 2))
    )


_AdGenMEVCIGMPMode_Type.__name__ = "Integer32"
_AdGenMEVCIGMPMode_Object = MibTableColumn
adGenMEVCIGMPMode = _AdGenMEVCIGMPMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 1, 1, 13),
    _AdGenMEVCIGMPMode_Type()
)
adGenMEVCIGMPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCIGMPMode.setStatus("current")
_AdGenMEVCLookupTable_Object = MibTable
adGenMEVCLookupTable = _AdGenMEVCLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 2)
)
if mibBuilder.loadTexts:
    adGenMEVCLookupTable.setStatus("current")
_AdGenMEVCLookupEntry_Object = MibTableRow
adGenMEVCLookupEntry = _AdGenMEVCLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 2, 1)
)
adGenMEVCLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMEVC-MIB", "adGenMEVCLookupSTag"),
)
if mibBuilder.loadTexts:
    adGenMEVCLookupEntry.setStatus("current")
_AdGenMEVCLookupSTag_Type = Integer32
_AdGenMEVCLookupSTag_Object = MibTableColumn
adGenMEVCLookupSTag = _AdGenMEVCLookupSTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 2, 1, 1),
    _AdGenMEVCLookupSTag_Type()
)
adGenMEVCLookupSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCLookupSTag.setStatus("current")
_AdGenMEVCLookupName_Type = DisplayString
_AdGenMEVCLookupName_Object = MibTableColumn
adGenMEVCLookupName = _AdGenMEVCLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 2, 1, 2),
    _AdGenMEVCLookupName_Type()
)
adGenMEVCLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCLookupName.setStatus("current")
_AdGenMEVCErrorTable_Object = MibTable
adGenMEVCErrorTable = _AdGenMEVCErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 3)
)
if mibBuilder.loadTexts:
    adGenMEVCErrorTable.setStatus("current")
_AdGenMEVCErrorEntry_Object = MibTableRow
adGenMEVCErrorEntry = _AdGenMEVCErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 3, 1)
)
adGenMEVCErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMEVCErrorEntry.setStatus("current")
_AdGenMEVCError_Type = DisplayString
_AdGenMEVCError_Object = MibTableColumn
adGenMEVCError = _AdGenMEVCError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 3, 1, 1),
    _AdGenMEVCError_Type()
)
adGenMEVCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCError.setStatus("current")
_AdGenMEVCMenPortTable_Object = MibTable
adGenMEVCMenPortTable = _AdGenMEVCMenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 4)
)
if mibBuilder.loadTexts:
    adGenMEVCMenPortTable.setStatus("deprecated")
_AdGenMEVCMenPortEntry_Object = MibTableRow
adGenMEVCMenPortEntry = _AdGenMEVCMenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 4, 1)
)
adGenMEVCMenPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEVC-MIB", "adGenProvisionedMEVCName"),
)
if mibBuilder.loadTexts:
    adGenMEVCMenPortEntry.setStatus("deprecated")


class _AdGenProvisionedMEVCName_Type(OctetString):
    """Custom type adGenProvisionedMEVCName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenProvisionedMEVCName_Type.__name__ = "OctetString"
_AdGenProvisionedMEVCName_Object = MibTableColumn
adGenProvisionedMEVCName = _AdGenProvisionedMEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 4, 1, 1),
    _AdGenProvisionedMEVCName_Type()
)
adGenProvisionedMEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenProvisionedMEVCName.setStatus("deprecated")
_AdGenMEVCMenPortRowStatus_Type = RowStatus
_AdGenMEVCMenPortRowStatus_Object = MibTableColumn
adGenMEVCMenPortRowStatus = _AdGenMEVCMenPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 4, 1, 2),
    _AdGenMEVCMenPortRowStatus_Type()
)
adGenMEVCMenPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCMenPortRowStatus.setStatus("deprecated")


class _AdGenMEVCMenPortConnectionType_Type(Integer32):
    """Custom type adGenMEVCMenPortConnectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("root", 1),
          ("leaf", 2))
    )


_AdGenMEVCMenPortConnectionType_Type.__name__ = "Integer32"
_AdGenMEVCMenPortConnectionType_Object = MibTableColumn
adGenMEVCMenPortConnectionType = _AdGenMEVCMenPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 4, 1, 3),
    _AdGenMEVCMenPortConnectionType_Type()
)
adGenMEVCMenPortConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCMenPortConnectionType.setStatus("deprecated")
_AdGenMEVCMenPortConnectionErrorTable_Object = MibTable
adGenMEVCMenPortConnectionErrorTable = _AdGenMEVCMenPortConnectionErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 5)
)
if mibBuilder.loadTexts:
    adGenMEVCMenPortConnectionErrorTable.setStatus("current")
_AdGenMEVCMenPortConnectionErrorEntry_Object = MibTableRow
adGenMEVCMenPortConnectionErrorEntry = _AdGenMEVCMenPortConnectionErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 5, 1)
)
adGenMEVCMenPortConnectionErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMEVC-MIB", "adGenProvisionedMenPortMEVCName"),
)
if mibBuilder.loadTexts:
    adGenMEVCMenPortConnectionErrorEntry.setStatus("current")


class _AdGenProvisionedMenPortMEVCName_Type(OctetString):
    """Custom type adGenProvisionedMenPortMEVCName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenProvisionedMenPortMEVCName_Type.__name__ = "OctetString"
_AdGenProvisionedMenPortMEVCName_Object = MibTableColumn
adGenProvisionedMenPortMEVCName = _AdGenProvisionedMenPortMEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 5, 1, 1),
    _AdGenProvisionedMenPortMEVCName_Type()
)
adGenProvisionedMenPortMEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenProvisionedMenPortMEVCName.setStatus("current")
_AdGenMEVCMenPortConnectionError_Type = DisplayString
_AdGenMEVCMenPortConnectionError_Object = MibTableColumn
adGenMEVCMenPortConnectionError = _AdGenMEVCMenPortConnectionError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 5, 1, 2),
    _AdGenMEVCMenPortConnectionError_Type()
)
adGenMEVCMenPortConnectionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCMenPortConnectionError.setStatus("current")
_AdGenMEVCMenPortProvisioningTable_Object = MibTable
adGenMEVCMenPortProvisioningTable = _AdGenMEVCMenPortProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 6)
)
if mibBuilder.loadTexts:
    adGenMEVCMenPortProvisioningTable.setStatus("current")
_AdGenMEVCMenPortProvisioningEntry_Object = MibTableRow
adGenMEVCMenPortProvisioningEntry = _AdGenMEVCMenPortProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 6, 1)
)
adGenMEVCMenPortProvisioningEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEVCMenPortProvisioningEntry.setStatus("current")


class _AdGenMEVCMenPortStagDei_Type(Integer32):
    """Custom type adGenMEVCMenPortStagDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenMEVCMenPortStagDei_Type.__name__ = "Integer32"
_AdGenMEVCMenPortStagDei_Object = MibTableColumn
adGenMEVCMenPortStagDei = _AdGenMEVCMenPortStagDei_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 6, 1, 1),
    _AdGenMEVCMenPortStagDei_Type()
)
adGenMEVCMenPortStagDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEVCMenPortStagDei.setStatus("current")
_AdGenMEVCNumberOfMEVCsTable_Object = MibTable
adGenMEVCNumberOfMEVCsTable = _AdGenMEVCNumberOfMEVCsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 7)
)
if mibBuilder.loadTexts:
    adGenMEVCNumberOfMEVCsTable.setStatus("current")
_AdGenMEVCNumberOfMEVCsEntry_Object = MibTableRow
adGenMEVCNumberOfMEVCsEntry = _AdGenMEVCNumberOfMEVCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 7, 1)
)
adGenMEVCNumberOfMEVCsEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMEVCNumberOfMEVCsEntry.setStatus("current")
_AdGenMEVCNumberOfMEVCs_Type = Integer32
_AdGenMEVCNumberOfMEVCs_Object = MibTableColumn
adGenMEVCNumberOfMEVCs = _AdGenMEVCNumberOfMEVCs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 7, 1, 1),
    _AdGenMEVCNumberOfMEVCs_Type()
)
adGenMEVCNumberOfMEVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCNumberOfMEVCs.setStatus("current")
_AdGenVLANInUseLookupTable_Object = MibTable
adGenVLANInUseLookupTable = _AdGenVLANInUseLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 8)
)
if mibBuilder.loadTexts:
    adGenVLANInUseLookupTable.setStatus("current")
_AdGenVLANInUseLookupEntry_Object = MibTableRow
adGenVLANInUseLookupEntry = _AdGenVLANInUseLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 8, 1)
)
adGenVLANInUseLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVLANInUseLookupEntry.setStatus("current")


class _AdGenVLANInUseLookupData_Type(OctetString):
    """Custom type adGenVLANInUseLookupData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_AdGenVLANInUseLookupData_Type.__name__ = "OctetString"
_AdGenVLANInUseLookupData_Object = MibTableColumn
adGenVLANInUseLookupData = _AdGenVLANInUseLookupData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 8, 1, 1),
    _AdGenVLANInUseLookupData_Type()
)
adGenVLANInUseLookupData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVLANInUseLookupData.setStatus("current")
_AdGenMEVCEnhMenPortTable_Object = MibTable
adGenMEVCEnhMenPortTable = _AdGenMEVCEnhMenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 9)
)
if mibBuilder.loadTexts:
    adGenMEVCEnhMenPortTable.setStatus("current")
_AdGenMEVCEnhMenPortEntry_Object = MibTableRow
adGenMEVCEnhMenPortEntry = _AdGenMEVCEnhMenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 9, 1)
)
adGenMEVCEnhMenPortEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMEVC-MIB", "adGenMEVCMenPortIfIndex"),
    (0, "ADTRAN-GENMEVC-MIB", "adGenProvMEVCName"),
)
if mibBuilder.loadTexts:
    adGenMEVCEnhMenPortEntry.setStatus("current")
_AdGenMEVCMenPortIfIndex_Type = InterfaceIndex
_AdGenMEVCMenPortIfIndex_Object = MibTableColumn
adGenMEVCMenPortIfIndex = _AdGenMEVCMenPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 9, 1, 1),
    _AdGenMEVCMenPortIfIndex_Type()
)
adGenMEVCMenPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMEVCMenPortIfIndex.setStatus("current")


class _AdGenProvMEVCName_Type(OctetString):
    """Custom type adGenProvMEVCName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenProvMEVCName_Type.__name__ = "OctetString"
_AdGenProvMEVCName_Object = MibTableColumn
adGenProvMEVCName = _AdGenProvMEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 9, 1, 2),
    _AdGenProvMEVCName_Type()
)
adGenProvMEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenProvMEVCName.setStatus("current")
_AdGenMEVCEnhMenPortRowStatus_Type = RowStatus
_AdGenMEVCEnhMenPortRowStatus_Object = MibTableColumn
adGenMEVCEnhMenPortRowStatus = _AdGenMEVCEnhMenPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 9, 1, 3),
    _AdGenMEVCEnhMenPortRowStatus_Type()
)
adGenMEVCEnhMenPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCEnhMenPortRowStatus.setStatus("current")


class _AdGenMEVCEnhMenPortConnectionType_Type(Integer32):
    """Custom type adGenMEVCEnhMenPortConnectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("root", 1),
          ("leaf", 2))
    )


_AdGenMEVCEnhMenPortConnectionType_Type.__name__ = "Integer32"
_AdGenMEVCEnhMenPortConnectionType_Object = MibTableColumn
adGenMEVCEnhMenPortConnectionType = _AdGenMEVCEnhMenPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 9, 1, 4),
    _AdGenMEVCEnhMenPortConnectionType_Type()
)
adGenMEVCEnhMenPortConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCEnhMenPortConnectionType.setStatus("current")
_AdGenMEVCIGMPTable_Object = MibTable
adGenMEVCIGMPTable = _AdGenMEVCIGMPTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 10)
)
if mibBuilder.loadTexts:
    adGenMEVCIGMPTable.setStatus("current")
_AdGenMEVCIGMPEntry_Object = MibTableRow
adGenMEVCIGMPEntry = _AdGenMEVCIGMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 10, 1)
)
adGenMEVCIGMPEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMEVC-MIB", "adGenMEVCIGMPInterfaceIndex"),
    (0, "ADTRAN-GENMEVC-MIB", "adGenMEVCIGMPEVCName"),
)
if mibBuilder.loadTexts:
    adGenMEVCIGMPEntry.setStatus("current")
_AdGenMEVCIGMPInterfaceIndex_Type = InterfaceIndex
_AdGenMEVCIGMPInterfaceIndex_Object = MibTableColumn
adGenMEVCIGMPInterfaceIndex = _AdGenMEVCIGMPInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 10, 1, 1),
    _AdGenMEVCIGMPInterfaceIndex_Type()
)
adGenMEVCIGMPInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMEVCIGMPInterfaceIndex.setStatus("current")


class _AdGenMEVCIGMPEVCName_Type(OctetString):
    """Custom type adGenMEVCIGMPEVCName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMEVCIGMPEVCName_Type.__name__ = "OctetString"
_AdGenMEVCIGMPEVCName_Object = MibTableColumn
adGenMEVCIGMPEVCName = _AdGenMEVCIGMPEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 10, 1, 2),
    _AdGenMEVCIGMPEVCName_Type()
)
adGenMEVCIGMPEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMEVCIGMPEVCName.setStatus("current")


class _AdGenMEVCIGMPInterfaceMode_Type(Integer32):
    """Custom type adGenMEVCIGMPInterfaceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )


_AdGenMEVCIGMPInterfaceMode_Type.__name__ = "Integer32"
_AdGenMEVCIGMPInterfaceMode_Object = MibTableColumn
adGenMEVCIGMPInterfaceMode = _AdGenMEVCIGMPInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 10, 1, 3),
    _AdGenMEVCIGMPInterfaceMode_Type()
)
adGenMEVCIGMPInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCIGMPInterfaceMode.setStatus("current")
_AdGenMEVCIGMPRowStatus_Type = RowStatus
_AdGenMEVCIGMPRowStatus_Object = MibTableColumn
adGenMEVCIGMPRowStatus = _AdGenMEVCIGMPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 10, 1, 4),
    _AdGenMEVCIGMPRowStatus_Type()
)
adGenMEVCIGMPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEVCIGMPRowStatus.setStatus("current")
_AdGenMEVCIGMPLastError_Type = DisplayString
_AdGenMEVCIGMPLastError_Object = MibTableColumn
adGenMEVCIGMPLastError = _AdGenMEVCIGMPLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 27, 1, 10, 1, 5),
    _AdGenMEVCIGMPLastError_Type()
)
adGenMEVCIGMPLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEVCIGMPLastError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMEVC-MIB",
    **{"adGenMEVCEvents": adGenMEVCEvents,
       "adGenMEVCProvisioning": adGenMEVCProvisioning,
       "adGenMEVCTable": adGenMEVCTable,
       "adGenMEVCEntry": adGenMEVCEntry,
       "adGenMEVCName": adGenMEVCName,
       "adGenMEVCRowStatus": adGenMEVCRowStatus,
       "adGenMEVCOperStatus": adGenMEVCOperStatus,
       "adGenMEVCStatus": adGenMEVCStatus,
       "adGenMEVCSTagVID": adGenMEVCSTagVID,
       "adGenMEVCPreserveCEVlanId": adGenMEVCPreserveCEVlanId,
       "adGenMEVCMacSwitching": adGenMEVCMacSwitching,
       "adGenMEVCNumberOfInterfaces": adGenMEVCNumberOfInterfaces,
       "adGenMEVCLastError": adGenMEVCLastError,
       "adGenMevcManagement": adGenMevcManagement,
       "adGenMEVCIGMPImmediateLeave": adGenMEVCIGMPImmediateLeave,
       "adGenMEVCIGMPTimeOutInterval": adGenMEVCIGMPTimeOutInterval,
       "adGenMEVCIGMPMode": adGenMEVCIGMPMode,
       "adGenMEVCLookupTable": adGenMEVCLookupTable,
       "adGenMEVCLookupEntry": adGenMEVCLookupEntry,
       "adGenMEVCLookupSTag": adGenMEVCLookupSTag,
       "adGenMEVCLookupName": adGenMEVCLookupName,
       "adGenMEVCErrorTable": adGenMEVCErrorTable,
       "adGenMEVCErrorEntry": adGenMEVCErrorEntry,
       "adGenMEVCError": adGenMEVCError,
       "adGenMEVCMenPortTable": adGenMEVCMenPortTable,
       "adGenMEVCMenPortEntry": adGenMEVCMenPortEntry,
       "adGenProvisionedMEVCName": adGenProvisionedMEVCName,
       "adGenMEVCMenPortRowStatus": adGenMEVCMenPortRowStatus,
       "adGenMEVCMenPortConnectionType": adGenMEVCMenPortConnectionType,
       "adGenMEVCMenPortConnectionErrorTable": adGenMEVCMenPortConnectionErrorTable,
       "adGenMEVCMenPortConnectionErrorEntry": adGenMEVCMenPortConnectionErrorEntry,
       "adGenProvisionedMenPortMEVCName": adGenProvisionedMenPortMEVCName,
       "adGenMEVCMenPortConnectionError": adGenMEVCMenPortConnectionError,
       "adGenMEVCMenPortProvisioningTable": adGenMEVCMenPortProvisioningTable,
       "adGenMEVCMenPortProvisioningEntry": adGenMEVCMenPortProvisioningEntry,
       "adGenMEVCMenPortStagDei": adGenMEVCMenPortStagDei,
       "adGenMEVCNumberOfMEVCsTable": adGenMEVCNumberOfMEVCsTable,
       "adGenMEVCNumberOfMEVCsEntry": adGenMEVCNumberOfMEVCsEntry,
       "adGenMEVCNumberOfMEVCs": adGenMEVCNumberOfMEVCs,
       "adGenVLANInUseLookupTable": adGenVLANInUseLookupTable,
       "adGenVLANInUseLookupEntry": adGenVLANInUseLookupEntry,
       "adGenVLANInUseLookupData": adGenVLANInUseLookupData,
       "adGenMEVCEnhMenPortTable": adGenMEVCEnhMenPortTable,
       "adGenMEVCEnhMenPortEntry": adGenMEVCEnhMenPortEntry,
       "adGenMEVCMenPortIfIndex": adGenMEVCMenPortIfIndex,
       "adGenProvMEVCName": adGenProvMEVCName,
       "adGenMEVCEnhMenPortRowStatus": adGenMEVCEnhMenPortRowStatus,
       "adGenMEVCEnhMenPortConnectionType": adGenMEVCEnhMenPortConnectionType,
       "adGenMEVCIGMPTable": adGenMEVCIGMPTable,
       "adGenMEVCIGMPEntry": adGenMEVCIGMPEntry,
       "adGenMEVCIGMPInterfaceIndex": adGenMEVCIGMPInterfaceIndex,
       "adGenMEVCIGMPEVCName": adGenMEVCIGMPEVCName,
       "adGenMEVCIGMPInterfaceMode": adGenMEVCIGMPInterfaceMode,
       "adGenMEVCIGMPRowStatus": adGenMEVCIGMPRowStatus,
       "adGenMEVCIGMPLastError": adGenMEVCIGMPLastError,
       "adGenMEVCMIB": adGenMEVCMIB}
)
