# SNMP MIB module (ADTRAN-GENIGMPCACHE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENIGMPCACHE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:25 2025
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

(adGenIGMPCache,
 adGenIGMPCacheID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenIGMPCache",
    "adGenIGMPCacheID")

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

adGenIGMPCacheMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 11, 11)
)
if mibBuilder.loadTexts:
    adGenIGMPCacheMIB.setRevisions(
        ("2013-03-05 00:00",
         "2011-10-31 00:00",
         "2011-10-28 00:00",
         "2009-05-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenIGMPCacheTable_Object = MibTable
adGenIGMPCacheTable = _AdGenIGMPCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1)
)
if mibBuilder.loadTexts:
    adGenIGMPCacheTable.setStatus("current")
_AdGenIGMPCacheEntry_Object = MibTableRow
adGenIGMPCacheEntry = _AdGenIGMPCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1)
)
adGenIGMPCacheEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENIGMPCACHE-MIB", "adGenIGMPCacheAddress"),
    (0, "ADTRAN-GENIGMPCACHE-MIB", "adGenIGMPCacheIndex"),
)
if mibBuilder.loadTexts:
    adGenIGMPCacheEntry.setStatus("current")
_AdGenIGMPCacheAddress_Type = IpAddress
_AdGenIGMPCacheAddress_Object = MibTableColumn
adGenIGMPCacheAddress = _AdGenIGMPCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 1),
    _AdGenIGMPCacheAddress_Type()
)
adGenIGMPCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIGMPCacheAddress.setStatus("current")
_AdGenIGMPCacheIndex_Type = Integer32
_AdGenIGMPCacheIndex_Object = MibTableColumn
adGenIGMPCacheIndex = _AdGenIGMPCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 2),
    _AdGenIGMPCacheIndex_Type()
)
adGenIGMPCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIGMPCacheIndex.setStatus("current")
_AdGenIGMPCacheLastReporter_Type = IpAddress
_AdGenIGMPCacheLastReporter_Object = MibTableColumn
adGenIGMPCacheLastReporter = _AdGenIGMPCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 3),
    _AdGenIGMPCacheLastReporter_Type()
)
adGenIGMPCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPCacheLastReporter.setStatus("current")
_AdGenIGMPCacheUpTime_Type = TimeTicks
_AdGenIGMPCacheUpTime_Object = MibTableColumn
adGenIGMPCacheUpTime = _AdGenIGMPCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 4),
    _AdGenIGMPCacheUpTime_Type()
)
adGenIGMPCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPCacheUpTime.setStatus("current")
_AdGenIGMPCacheExpiryTime_Type = TimeTicks
_AdGenIGMPCacheExpiryTime_Object = MibTableColumn
adGenIGMPCacheExpiryTime = _AdGenIGMPCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 5),
    _AdGenIGMPCacheExpiryTime_Type()
)
adGenIGMPCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPCacheExpiryTime.setStatus("current")
_AdGenIGMPCacheInterfaceDescription_Type = DisplayString
_AdGenIGMPCacheInterfaceDescription_Object = MibTableColumn
adGenIGMPCacheInterfaceDescription = _AdGenIGMPCacheInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 6),
    _AdGenIGMPCacheInterfaceDescription_Type()
)
adGenIGMPCacheInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPCacheInterfaceDescription.setStatus("current")
_AdGenIGMPCacheInterfaceName_Type = DisplayString
_AdGenIGMPCacheInterfaceName_Object = MibTableColumn
adGenIGMPCacheInterfaceName = _AdGenIGMPCacheInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 7),
    _AdGenIGMPCacheInterfaceName_Type()
)
adGenIGMPCacheInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPCacheInterfaceName.setStatus("current")


class _AdGenIGMPCacheMode_Type(Integer32):
    """Custom type adGenIGMPCacheMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3lite", 2),
          ("v2Compatibility", 3))
    )


_AdGenIGMPCacheMode_Type.__name__ = "Integer32"
_AdGenIGMPCacheMode_Object = MibTableColumn
adGenIGMPCacheMode = _AdGenIGMPCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 11, 1, 1, 8),
    _AdGenIGMPCacheMode_Type()
)
adGenIGMPCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPCacheMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENIGMPCACHE-MIB",
    **{"adGenIGMPCacheTable": adGenIGMPCacheTable,
       "adGenIGMPCacheEntry": adGenIGMPCacheEntry,
       "adGenIGMPCacheAddress": adGenIGMPCacheAddress,
       "adGenIGMPCacheIndex": adGenIGMPCacheIndex,
       "adGenIGMPCacheLastReporter": adGenIGMPCacheLastReporter,
       "adGenIGMPCacheUpTime": adGenIGMPCacheUpTime,
       "adGenIGMPCacheExpiryTime": adGenIGMPCacheExpiryTime,
       "adGenIGMPCacheInterfaceDescription": adGenIGMPCacheInterfaceDescription,
       "adGenIGMPCacheInterfaceName": adGenIGMPCacheInterfaceName,
       "adGenIGMPCacheMode": adGenIGMPCacheMode,
       "adGenIGMPCacheMIB": adGenIGMPCacheMIB}
)
