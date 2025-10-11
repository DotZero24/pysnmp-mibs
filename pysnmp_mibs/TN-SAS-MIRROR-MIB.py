# SNMP MIB module (TN-SAS-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-SAS-MIRROR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:56:11 2025
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

(tnMirrorDestinationEntry,
 tnMirrorSourcePortEntry) = mibBuilder.importSymbols(
    "TN-MIRROR-MIB",
    "tnMirrorDestinationEntry",
    "tnMirrorSourcePortEntry")

(TProfileOrNone,) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TProfileOrNone")

(tnSASModules,
 tnSASObjs,
 tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSASModules",
    "tnSASObjs",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")


# MODULE-IDENTITY

tnSASMirrorMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    tnSASMirrorMIBModule.setRevisions(
        ("2011-05-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSASMirrorObjects_ObjectIdentity = ObjectIdentity
tnSASMirrorObjects = _TnSASMirrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13)
)
_TnMirrorSourcePortExtnTable_Object = MibTable
tnMirrorSourcePortExtnTable = _TnMirrorSourcePortExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    tnMirrorSourcePortExtnTable.setStatus("current")
_TnMirrorSourcePortExtnEntry_Object = MibTableRow
tnMirrorSourcePortExtnEntry = _TnMirrorSourcePortExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tnMirrorSourcePortExtnEntry.setStatus("current")


class _TnMirrorSourcePortEgressMirroringType_Type(Integer32):
    """Custom type tnMirrorSourcePortEgressMirroringType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true-egress-mirroring", 1),
          ("normal-egress-mirroring", 2))
    )


_TnMirrorSourcePortEgressMirroringType_Type.__name__ = "Integer32"
_TnMirrorSourcePortEgressMirroringType_Object = MibTableColumn
tnMirrorSourcePortEgressMirroringType = _TnMirrorSourcePortEgressMirroringType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13, 1, 1, 1),
    _TnMirrorSourcePortEgressMirroringType_Type()
)
tnMirrorSourcePortEgressMirroringType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorSourcePortEgressMirroringType.setStatus("current")
_TnMirrorDestinationExtnTable_Object = MibTable
tnMirrorDestinationExtnTable = _TnMirrorDestinationExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13, 2)
)
if mibBuilder.loadTexts:
    tnMirrorDestinationExtnTable.setStatus("current")
_TnMirrorDestinationExtnEntry_Object = MibTableRow
tnMirrorDestinationExtnEntry = _TnMirrorDestinationExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    tnMirrorDestinationExtnEntry.setStatus("current")


class _TnMirrorDestinationFCProfile_Type(TProfileOrNone):
    """Custom type tnMirrorDestinationFCProfile based on TProfileOrNone"""
    defaultValue = 2


_TnMirrorDestinationFCProfile_Type.__name__ = "TProfileOrNone"
_TnMirrorDestinationFCProfile_Object = MibTableColumn
tnMirrorDestinationFCProfile = _TnMirrorDestinationFCProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13, 2, 1, 1),
    _TnMirrorDestinationFCProfile_Type()
)
tnMirrorDestinationFCProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationFCProfile.setStatus("current")


class _TnMirrorDestinationMirrorSourceType_Type(Integer32):
    """Custom type tnMirrorDestinationMirrorSourceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("both", 3))
    )


_TnMirrorDestinationMirrorSourceType_Type.__name__ = "Integer32"
_TnMirrorDestinationMirrorSourceType_Object = MibTableColumn
tnMirrorDestinationMirrorSourceType = _TnMirrorDestinationMirrorSourceType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 13, 2, 1, 2),
    _TnMirrorDestinationMirrorSourceType_Type()
)
tnMirrorDestinationMirrorSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMirrorDestinationMirrorSourceType.setStatus("current")
tnMirrorSourcePortEntry.registerAugmentions(
    ("TN-SAS-MIRROR-MIB",
     "tnMirrorSourcePortExtnEntry")
)
tnMirrorSourcePortExtnEntry.setIndexNames(*tnMirrorSourcePortEntry.getIndexNames())
tnMirrorDestinationEntry.registerAugmentions(
    ("TN-SAS-MIRROR-MIB",
     "tnMirrorDestinationExtnEntry")
)
tnMirrorDestinationExtnEntry.setIndexNames(*tnMirrorDestinationEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAS-MIRROR-MIB",
    **{"tnSASMirrorMIBModule": tnSASMirrorMIBModule,
       "tnSASMirrorObjects": tnSASMirrorObjects,
       "tnMirrorSourcePortExtnTable": tnMirrorSourcePortExtnTable,
       "tnMirrorSourcePortExtnEntry": tnMirrorSourcePortExtnEntry,
       "tnMirrorSourcePortEgressMirroringType": tnMirrorSourcePortEgressMirroringType,
       "tnMirrorDestinationExtnTable": tnMirrorDestinationExtnTable,
       "tnMirrorDestinationExtnEntry": tnMirrorDestinationExtnEntry,
       "tnMirrorDestinationFCProfile": tnMirrorDestinationFCProfile,
       "tnMirrorDestinationMirrorSourceType": tnMirrorDestinationMirrorSourceType}
)
