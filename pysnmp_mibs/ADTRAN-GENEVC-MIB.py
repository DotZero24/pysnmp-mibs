# SNMP MIB module (ADTRAN-GENEVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENEVC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:23 2025
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

(adGenIpHostEntryIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENIPHOST-MIB",
    "adGenIpHostEntryIndex")

(adGenEVC,
 adGenEVCID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenEVC",
    "adGenEVCID")

(GenSystemInterfaceType,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "GenSystemInterfaceType")

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

adGenEVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 10, 1)
)
if mibBuilder.loadTexts:
    adGenEVCMIB.setRevisions(
        ("2013-09-06 00:00",
         "2012-03-21 00:00",
         "2010-02-10 00:00",
         "2009-04-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEVCEvents_ObjectIdentity = ObjectIdentity
adGenEVCEvents = _AdGenEVCEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 0)
)
_AdGenEVCProvisioning_ObjectIdentity = ObjectIdentity
adGenEVCProvisioning = _AdGenEVCProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1)
)
_AdGenEVCTable_Object = MibTable
adGenEVCTable = _AdGenEVCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEVCTable.setStatus("current")
_AdGenEVCEntry_Object = MibTableRow
adGenEVCEntry = _AdGenEVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1)
)
adGenEVCEntry.setIndexNames(
    (1, "ADTRAN-GENEVC-MIB", "adGenEVCName"),
)
if mibBuilder.loadTexts:
    adGenEVCEntry.setStatus("current")


class _AdGenEVCName_Type(DisplayString):
    """Custom type adGenEVCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEVCName_Type.__name__ = "DisplayString"
_AdGenEVCName_Object = MibTableColumn
adGenEVCName = _AdGenEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 1),
    _AdGenEVCName_Type()
)
adGenEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCName.setStatus("current")
_AdGenEVCRowStatus_Type = RowStatus
_AdGenEVCRowStatus_Object = MibTableColumn
adGenEVCRowStatus = _AdGenEVCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 2),
    _AdGenEVCRowStatus_Type()
)
adGenEVCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCRowStatus.setStatus("current")


class _AdGenEVCOperStatus_Type(Integer32):
    """Custom type adGenEVCOperStatus based on Integer32"""
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


_AdGenEVCOperStatus_Type.__name__ = "Integer32"
_AdGenEVCOperStatus_Object = MibTableColumn
adGenEVCOperStatus = _AdGenEVCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 3),
    _AdGenEVCOperStatus_Type()
)
adGenEVCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCOperStatus.setStatus("current")
_AdGenEVCStatus_Type = DisplayString
_AdGenEVCStatus_Object = MibTableColumn
adGenEVCStatus = _AdGenEVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 4),
    _AdGenEVCStatus_Type()
)
adGenEVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCStatus.setStatus("current")
_AdGenEVCSTagVID_Type = Integer32
_AdGenEVCSTagVID_Object = MibTableColumn
adGenEVCSTagVID = _AdGenEVCSTagVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 5),
    _AdGenEVCSTagVID_Type()
)
adGenEVCSTagVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCSTagVID.setStatus("current")


class _AdGenEVCPreserveCEVlanId_Type(Integer32):
    """Custom type adGenEVCPreserveCEVlanId based on Integer32"""
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


_AdGenEVCPreserveCEVlanId_Type.__name__ = "Integer32"
_AdGenEVCPreserveCEVlanId_Object = MibTableColumn
adGenEVCPreserveCEVlanId = _AdGenEVCPreserveCEVlanId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 6),
    _AdGenEVCPreserveCEVlanId_Type()
)
adGenEVCPreserveCEVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCPreserveCEVlanId.setStatus("current")


class _AdGenEVCMacSwitching_Type(Integer32):
    """Custom type adGenEVCMacSwitching based on Integer32"""
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


_AdGenEVCMacSwitching_Type.__name__ = "Integer32"
_AdGenEVCMacSwitching_Object = MibTableColumn
adGenEVCMacSwitching = _AdGenEVCMacSwitching_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 7),
    _AdGenEVCMacSwitching_Type()
)
adGenEVCMacSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMacSwitching.setStatus("current")
_AdGenEVCNumberOfInterfaces_Type = Integer32
_AdGenEVCNumberOfInterfaces_Object = MibTableColumn
adGenEVCNumberOfInterfaces = _AdGenEVCNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 8),
    _AdGenEVCNumberOfInterfaces_Type()
)
adGenEVCNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCNumberOfInterfaces.setStatus("current")
_AdGenEVCLastError_Type = DisplayString
_AdGenEVCLastError_Object = MibTableColumn
adGenEVCLastError = _AdGenEVCLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 9),
    _AdGenEVCLastError_Type()
)
adGenEVCLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCLastError.setStatus("current")


class _AdGenEVCDoubleTagSwitching_Type(Integer32):
    """Custom type adGenEVCDoubleTagSwitching based on Integer32"""
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


_AdGenEVCDoubleTagSwitching_Type.__name__ = "Integer32"
_AdGenEVCDoubleTagSwitching_Object = MibTableColumn
adGenEVCDoubleTagSwitching = _AdGenEVCDoubleTagSwitching_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 1, 1, 10),
    _AdGenEVCDoubleTagSwitching_Type()
)
adGenEVCDoubleTagSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCDoubleTagSwitching.setStatus("current")
_AdGenEVCLookupTable_Object = MibTable
adGenEVCLookupTable = _AdGenEVCLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 2)
)
if mibBuilder.loadTexts:
    adGenEVCLookupTable.setStatus("current")
_AdGenEVCLookupEntry_Object = MibTableRow
adGenEVCLookupEntry = _AdGenEVCLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 2, 1)
)
adGenEVCLookupEntry.setIndexNames(
    (0, "ADTRAN-GENEVC-MIB", "adGenEVCLookupSTag"),
)
if mibBuilder.loadTexts:
    adGenEVCLookupEntry.setStatus("current")
_AdGenEVCLookupSTag_Type = Integer32
_AdGenEVCLookupSTag_Object = MibTableColumn
adGenEVCLookupSTag = _AdGenEVCLookupSTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 2, 1, 1),
    _AdGenEVCLookupSTag_Type()
)
adGenEVCLookupSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCLookupSTag.setStatus("current")
_AdGenEVCLookupName_Type = DisplayString
_AdGenEVCLookupName_Object = MibTableColumn
adGenEVCLookupName = _AdGenEVCLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 2, 1, 2),
    _AdGenEVCLookupName_Type()
)
adGenEVCLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCLookupName.setStatus("current")
_AdGenEVCMenPortTable_Object = MibTable
adGenEVCMenPortTable = _AdGenEVCMenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 3)
)
if mibBuilder.loadTexts:
    adGenEVCMenPortTable.setStatus("current")
_AdGenEVCMenPortEntry_Object = MibTableRow
adGenEVCMenPortEntry = _AdGenEVCMenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 3, 1)
)
adGenEVCMenPortEntry.setIndexNames(
    (0, "ADTRAN-GENEVC-MIB", "adGenEVCNameFixedLen"),
    (0, "ADTRAN-GENEVC-MIB", "adGenMenPortIfIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCMenPortEntry.setStatus("current")


class _AdGenEVCNameFixedLen_Type(OctetString):
    """Custom type adGenEVCNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_AdGenEVCNameFixedLen_Type.__name__ = "OctetString"
_AdGenEVCNameFixedLen_Object = MibTableColumn
adGenEVCNameFixedLen = _AdGenEVCNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 3, 1, 1),
    _AdGenEVCNameFixedLen_Type()
)
adGenEVCNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCNameFixedLen.setStatus("current")
_AdGenMenPortIfIndex_Type = InterfaceIndex
_AdGenMenPortIfIndex_Object = MibTableColumn
adGenMenPortIfIndex = _AdGenMenPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 3, 1, 2),
    _AdGenMenPortIfIndex_Type()
)
adGenMenPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMenPortIfIndex.setStatus("current")
_AdGenMenPortRowStatus_Type = RowStatus
_AdGenMenPortRowStatus_Object = MibTableColumn
adGenMenPortRowStatus = _AdGenMenPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 3, 1, 3),
    _AdGenMenPortRowStatus_Type()
)
adGenMenPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMenPortRowStatus.setStatus("current")


class _AdGenMenPortConnectionType_Type(Integer32):
    """Custom type adGenMenPortConnectionType based on Integer32"""
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


_AdGenMenPortConnectionType_Type.__name__ = "Integer32"
_AdGenMenPortConnectionType_Object = MibTableColumn
adGenMenPortConnectionType = _AdGenMenPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 3, 1, 4),
    _AdGenMenPortConnectionType_Type()
)
adGenMenPortConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMenPortConnectionType.setStatus("current")
_AdGenMenPortInterfaceType_Type = GenSystemInterfaceType
_AdGenMenPortInterfaceType_Object = MibTableColumn
adGenMenPortInterfaceType = _AdGenMenPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 3, 1, 5),
    _AdGenMenPortInterfaceType_Type()
)
adGenMenPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMenPortInterfaceType.setStatus("current")
_AdGenEVCMenPortConnectionError_Type = DisplayString
_AdGenEVCMenPortConnectionError_Object = MibScalar
adGenEVCMenPortConnectionError = _AdGenEVCMenPortConnectionError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 4),
    _AdGenEVCMenPortConnectionError_Type()
)
adGenEVCMenPortConnectionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMenPortConnectionError.setStatus("current")
_AdGenEVCMenPortProvisioningTable_Object = MibTable
adGenEVCMenPortProvisioningTable = _AdGenEVCMenPortProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 5)
)
if mibBuilder.loadTexts:
    adGenEVCMenPortProvisioningTable.setStatus("current")
_AdGenEVCMenPortProvisioningEntry_Object = MibTableRow
adGenEVCMenPortProvisioningEntry = _AdGenEVCMenPortProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 5, 1)
)
adGenEVCMenPortProvisioningEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCMenPortProvisioningEntry.setStatus("current")


class _AdGenMenPortStagDei_Type(Integer32):
    """Custom type adGenMenPortStagDei based on Integer32"""
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


_AdGenMenPortStagDei_Type.__name__ = "Integer32"
_AdGenMenPortStagDei_Object = MibTableColumn
adGenMenPortStagDei = _AdGenMenPortStagDei_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 5, 1, 1),
    _AdGenMenPortStagDei_Type()
)
adGenMenPortStagDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMenPortStagDei.setStatus("current")
_AdGenEVCProvScalars_ObjectIdentity = ObjectIdentity
adGenEVCProvScalars = _AdGenEVCProvScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 6)
)
_AdGenEVCNumberOfEvcs_Type = Integer32
_AdGenEVCNumberOfEvcs_Object = MibScalar
adGenEVCNumberOfEvcs = _AdGenEVCNumberOfEvcs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 6, 1),
    _AdGenEVCNumberOfEvcs_Type()
)
adGenEVCNumberOfEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCNumberOfEvcs.setStatus("current")
_AdGenEVCLastChange_Type = TimeStamp
_AdGenEVCLastChange_Object = MibScalar
adGenEVCLastChange = _AdGenEVCLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 6, 2),
    _AdGenEVCLastChange_Type()
)
adGenEVCLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCLastChange.setStatus("current")
_AdGenEVCSysMgmtEVCScalars_ObjectIdentity = ObjectIdentity
adGenEVCSysMgmtEVCScalars = _AdGenEVCSysMgmtEVCScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 7)
)
_AdGenEVCSysMgmtEVCSTagVID_Type = Integer32
_AdGenEVCSysMgmtEVCSTagVID_Object = MibScalar
adGenEVCSysMgmtEVCSTagVID = _AdGenEVCSysMgmtEVCSTagVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 7, 1),
    _AdGenEVCSysMgmtEVCSTagVID_Type()
)
adGenEVCSysMgmtEVCSTagVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCSysMgmtEVCSTagVID.setStatus("current")


class _AdGenEVCSysMgmtEVCSTagPriority_Type(Integer32):
    """Custom type adGenEVCSysMgmtEVCSTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEVCSysMgmtEVCSTagPriority_Type.__name__ = "Integer32"
_AdGenEVCSysMgmtEVCSTagPriority_Object = MibScalar
adGenEVCSysMgmtEVCSTagPriority = _AdGenEVCSysMgmtEVCSTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 7, 2),
    _AdGenEVCSysMgmtEVCSTagPriority_Type()
)
adGenEVCSysMgmtEVCSTagPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCSysMgmtEVCSTagPriority.setStatus("current")
_AdGenEVCSysMgmtEVCNumberOfInterfaces_Type = Integer32
_AdGenEVCSysMgmtEVCNumberOfInterfaces_Object = MibScalar
adGenEVCSysMgmtEVCNumberOfInterfaces = _AdGenEVCSysMgmtEVCNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 7, 3),
    _AdGenEVCSysMgmtEVCNumberOfInterfaces_Type()
)
adGenEVCSysMgmtEVCNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCSysMgmtEVCNumberOfInterfaces.setStatus("current")
_AdGenEVCSysMgmtEVCInterfaceTable_Object = MibTable
adGenEVCSysMgmtEVCInterfaceTable = _AdGenEVCSysMgmtEVCInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 8)
)
if mibBuilder.loadTexts:
    adGenEVCSysMgmtEVCInterfaceTable.setStatus("current")
_AdGenEVCSysMgmtEVCInterfaceEntry_Object = MibTableRow
adGenEVCSysMgmtEVCInterfaceEntry = _AdGenEVCSysMgmtEVCInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 8, 1)
)
adGenEVCSysMgmtEVCInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCSysMgmtEVCInterfaceEntry.setStatus("current")


class _AdGenSysMgmtEVCInterfaceConnectionType_Type(Integer32):
    """Custom type adGenSysMgmtEVCInterfaceConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("menPort", 1),
          ("uni", 2))
    )


_AdGenSysMgmtEVCInterfaceConnectionType_Type.__name__ = "Integer32"
_AdGenSysMgmtEVCInterfaceConnectionType_Object = MibTableColumn
adGenSysMgmtEVCInterfaceConnectionType = _AdGenSysMgmtEVCInterfaceConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 8, 1, 1),
    _AdGenSysMgmtEVCInterfaceConnectionType_Type()
)
adGenSysMgmtEVCInterfaceConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSysMgmtEVCInterfaceConnectionType.setStatus("current")
_AdGenEVCIPHostTable_Object = MibTable
adGenEVCIPHostTable = _AdGenEVCIPHostTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 9)
)
if mibBuilder.loadTexts:
    adGenEVCIPHostTable.setStatus("current")
_AdGenEVCIPHostEntry_Object = MibTableRow
adGenEVCIPHostEntry = _AdGenEVCIPHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 9, 1)
)
adGenEVCIPHostEntry.setIndexNames(
    (0, "ADTRAN-GENEVC-MIB", "adGenEVCNameFixedLen"),
    (0, "IF-MIB", "ifIndex"),
    (1, "ADTRAN-GENIPHOST-MIB", "adGenIpHostEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCIPHostEntry.setStatus("current")
_AdGenEVCIPHostRowStatus_Type = RowStatus
_AdGenEVCIPHostRowStatus_Object = MibTableColumn
adGenEVCIPHostRowStatus = _AdGenEVCIPHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 10, 1, 9, 1, 1),
    _AdGenEVCIPHostRowStatus_Type()
)
adGenEVCIPHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCIPHostRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENEVC-MIB",
    **{"adGenEVCEvents": adGenEVCEvents,
       "adGenEVCProvisioning": adGenEVCProvisioning,
       "adGenEVCTable": adGenEVCTable,
       "adGenEVCEntry": adGenEVCEntry,
       "adGenEVCName": adGenEVCName,
       "adGenEVCRowStatus": adGenEVCRowStatus,
       "adGenEVCOperStatus": adGenEVCOperStatus,
       "adGenEVCStatus": adGenEVCStatus,
       "adGenEVCSTagVID": adGenEVCSTagVID,
       "adGenEVCPreserveCEVlanId": adGenEVCPreserveCEVlanId,
       "adGenEVCMacSwitching": adGenEVCMacSwitching,
       "adGenEVCNumberOfInterfaces": adGenEVCNumberOfInterfaces,
       "adGenEVCLastError": adGenEVCLastError,
       "adGenEVCDoubleTagSwitching": adGenEVCDoubleTagSwitching,
       "adGenEVCLookupTable": adGenEVCLookupTable,
       "adGenEVCLookupEntry": adGenEVCLookupEntry,
       "adGenEVCLookupSTag": adGenEVCLookupSTag,
       "adGenEVCLookupName": adGenEVCLookupName,
       "adGenEVCMenPortTable": adGenEVCMenPortTable,
       "adGenEVCMenPortEntry": adGenEVCMenPortEntry,
       "adGenEVCNameFixedLen": adGenEVCNameFixedLen,
       "adGenMenPortIfIndex": adGenMenPortIfIndex,
       "adGenMenPortRowStatus": adGenMenPortRowStatus,
       "adGenMenPortConnectionType": adGenMenPortConnectionType,
       "adGenMenPortInterfaceType": adGenMenPortInterfaceType,
       "adGenEVCMenPortConnectionError": adGenEVCMenPortConnectionError,
       "adGenEVCMenPortProvisioningTable": adGenEVCMenPortProvisioningTable,
       "adGenEVCMenPortProvisioningEntry": adGenEVCMenPortProvisioningEntry,
       "adGenMenPortStagDei": adGenMenPortStagDei,
       "adGenEVCProvScalars": adGenEVCProvScalars,
       "adGenEVCNumberOfEvcs": adGenEVCNumberOfEvcs,
       "adGenEVCLastChange": adGenEVCLastChange,
       "adGenEVCSysMgmtEVCScalars": adGenEVCSysMgmtEVCScalars,
       "adGenEVCSysMgmtEVCSTagVID": adGenEVCSysMgmtEVCSTagVID,
       "adGenEVCSysMgmtEVCSTagPriority": adGenEVCSysMgmtEVCSTagPriority,
       "adGenEVCSysMgmtEVCNumberOfInterfaces": adGenEVCSysMgmtEVCNumberOfInterfaces,
       "adGenEVCSysMgmtEVCInterfaceTable": adGenEVCSysMgmtEVCInterfaceTable,
       "adGenEVCSysMgmtEVCInterfaceEntry": adGenEVCSysMgmtEVCInterfaceEntry,
       "adGenSysMgmtEVCInterfaceConnectionType": adGenSysMgmtEVCInterfaceConnectionType,
       "adGenEVCIPHostTable": adGenEVCIPHostTable,
       "adGenEVCIPHostEntry": adGenEVCIPHostEntry,
       "adGenEVCIPHostRowStatus": adGenEVCIPHostRowStatus,
       "adGenEVCMIB": adGenEVCMIB}
)
