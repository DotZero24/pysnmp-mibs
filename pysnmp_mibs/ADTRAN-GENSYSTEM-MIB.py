# SNMP MIB module (ADTRAN-GENSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENSYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:32 2025
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

(adShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adShared")

(adGenSystemProduct,
 adGenSystemProductID,
 adGenSystemProductMg) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenSystemProduct",
    "adGenSystemProductID",
    "adGenSystemProductMg")

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

adGenSystemsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSystemsMIB.setRevisions(
        ("2022-05-31 00:00",
         "2022-03-30 00:00",
         "2022-03-29 00:00",
         "2022-03-11 00:00",
         "2022-02-23 00:00",
         "2022-01-07 00:00",
         "2021-07-06 00:00",
         "2020-12-01 00:00",
         "2020-05-11 00:00",
         "2020-04-13 00:00",
         "2019-10-09 00:00",
         "2019-07-31 00:00",
         "2019-04-04 00:00",
         "2019-03-21 00:00",
         "2018-01-09 00:00",
         "2018-08-29 00:00",
         "2018-07-16 00:00",
         "2018-04-02 00:00",
         "2018-02-22 00:00",
         "2018-01-26 00:00",
         "2018-01-17 00:00",
         "2017-10-16 00:00",
         "2017-10-12 00:00",
         "2017-09-23 00:00",
         "2017-08-10 00:00",
         "2017-08-10 00:00",
         "2017-06-06 00:00",
         "2017-04-14 00:00",
         "2016-12-07 00:00",
         "2016-11-28 00:00",
         "2016-10-10 00:00",
         "2016-09-15 00:00",
         "2016-06-13 00:00",
         "2016-04-01 00:00",
         "2016-03-16 00:00",
         "2016-02-22 00:00",
         "2016-01-04 00:00",
         "2015-10-29 00:00",
         "2015-10-07 00:00",
         "2015-10-06 00:00",
         "2015-09-30 00:00",
         "2015-08-12 00:00",
         "2015-08-05 00:00",
         "2015-05-07 00:00",
         "2015-03-19 00:00",
         "2015-02-23 00:00",
         "2015-01-22 00:00",
         "2015-01-06 00:00",
         "2014-12-17 00:00",
         "2014-12-15 00:00",
         "2014-12-10 00:00",
         "2014-12-09 00:00",
         "2014-12-05 00:00",
         "2014-10-31 00:00",
         "2014-10-15 00:00",
         "2014-10-13 00:00",
         "2014-09-30 00:00",
         "2014-09-22 00:00",
         "2014-09-15 00:00",
         "2014-06-27 00:00",
         "2014-06-25 00:00",
         "2014-06-21 00:00",
         "2014-06-20 00:00",
         "2014-06-16 00:00",
         "2014-06-10 00:00",
         "2014-05-16 00:00",
         "2014-05-13 00:00",
         "2014-05-08 00:00",
         "2014-04-22 00:00",
         "2014-04-02 00:00",
         "2014-03-14 00:00",
         "2014-03-06 00:00",
         "2014-02-18 00:00",
         "2014-02-07 00:00",
         "2014-01-30 00:00",
         "2014-01-06 00:00",
         "2013-12-12 00:00",
         "2013-11-08 00:00",
         "2013-10-17 00:00",
         "2013-10-09 00:00",
         "2013-10-07 00:00",
         "2013-10-04 00:00",
         "2013-09-13 00:00",
         "2013-09-04 00:00",
         "2013-08-26 00:00",
         "2013-07-18 00:00",
         "2013-06-11 00:00",
         "2013-05-02 00:00",
         "2013-04-10 00:00",
         "2013-03-11 00:00",
         "2013-02-21 00:00",
         "2013-01-16 00:00",
         "2012-11-08 00:00",
         "2012-11-06 00:00",
         "2012-10-08 00:00",
         "2012-10-04 00:00",
         "2012-09-05 00:00",
         "2012-08-23 00:00",
         "2012-08-09 00:00",
         "2012-07-31 00:00",
         "2012-07-23 00:00",
         "2012-05-22 08:25",
         "2012-05-03 00:00",
         "2012-04-30 00:00",
         "2012-04-20 00:00",
         "2012-04-17 00:00",
         "2012-03-06 00:00",
         "2012-02-06 00:00",
         "2011-10-19 00:00",
         "2011-09-20 00:00",
         "2011-08-29 00:00",
         "2011-08-22 00:00",
         "2011-06-22 00:00",
         "2011-05-09 00:00",
         "2011-04-18 00:00",
         "2011-04-14 00:00",
         "2011-04-12 00:00",
         "2011-04-11 15:51",
         "2011-04-07 19:02",
         "2011-03-28 15:00",
         "2011-03-24 14:23",
         "2011-03-24 11:00",
         "2011-03-24 00:00",
         "2011-03-21 00:00",
         "2011-03-08 00:00",
         "2007-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenSystemProductTable_Object = MibTable
adGenSystemProductTable = _AdGenSystemProductTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSystemProductTable.setStatus("current")
_AdGenSystemProductEntry_Object = MibTableRow
adGenSystemProductEntry = _AdGenSystemProductEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 1, 1)
)
adGenSystemProductEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenSystemProductEntry.setStatus("current")
_AdGenSystemProductSnmpIdentifier_Type = DisplayString
_AdGenSystemProductSnmpIdentifier_Object = MibTableColumn
adGenSystemProductSnmpIdentifier = _AdGenSystemProductSnmpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 1, 1, 1),
    _AdGenSystemProductSnmpIdentifier_Type()
)
adGenSystemProductSnmpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemProductSnmpIdentifier.setStatus("current")
_AdGenSystemFeatureSupport_Type = DisplayString
_AdGenSystemFeatureSupport_Object = MibTableColumn
adGenSystemFeatureSupport = _AdGenSystemFeatureSupport_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 1, 1, 2),
    _AdGenSystemFeatureSupport_Type()
)
adGenSystemFeatureSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemFeatureSupport.setStatus("current")
_AdGenSystemFeatureSupportByteMap_Type = OctetString
_AdGenSystemFeatureSupportByteMap_Object = MibTableColumn
adGenSystemFeatureSupportByteMap = _AdGenSystemFeatureSupportByteMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 1, 1, 3),
    _AdGenSystemFeatureSupportByteMap_Type()
)
adGenSystemFeatureSupportByteMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemFeatureSupportByteMap.setStatus("current")
_AdGenSystemMibConformance_ObjectIdentity = ObjectIdentity
adGenSystemMibConformance = _AdGenSystemMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 2)
)
_AdGenSystemMibGroups_ObjectIdentity = ObjectIdentity
adGenSystemMibGroups = _AdGenSystemMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 2, 1)
)
_AdGenSystemProductMgGrp_ObjectIdentity = ObjectIdentity
adGenSystemProductMgGrp = _AdGenSystemProductMgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 6, 1)
)
_AdGenSystemFeatureSupportVersionTable_Object = MibTable
adGenSystemFeatureSupportVersionTable = _AdGenSystemFeatureSupportVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 6, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSystemFeatureSupportVersionTable.setStatus("current")
_AdGenSystemFeatureSupportVersionEntry_Object = MibTableRow
adGenSystemFeatureSupportVersionEntry = _AdGenSystemFeatureSupportVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 6, 1, 1, 1)
)
adGenSystemFeatureSupportVersionEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENSYSTEM-MIB", "adGenSystemFeatureSupportVersionIndex"),
)
if mibBuilder.loadTexts:
    adGenSystemFeatureSupportVersionEntry.setStatus("current")
_AdGenSystemFeatureSupportVersionIndex_Type = Integer32
_AdGenSystemFeatureSupportVersionIndex_Object = MibTableColumn
adGenSystemFeatureSupportVersionIndex = _AdGenSystemFeatureSupportVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 6, 1, 1, 1, 1),
    _AdGenSystemFeatureSupportVersionIndex_Type()
)
adGenSystemFeatureSupportVersionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSystemFeatureSupportVersionIndex.setStatus("current")
_AdGenSystemFeatureSupportVersionQuery_Type = OctetString
_AdGenSystemFeatureSupportVersionQuery_Object = MibTableColumn
adGenSystemFeatureSupportVersionQuery = _AdGenSystemFeatureSupportVersionQuery_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 6, 1, 1, 1, 2),
    _AdGenSystemFeatureSupportVersionQuery_Type()
)
adGenSystemFeatureSupportVersionQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSystemFeatureSupportVersionQuery.setStatus("current")

# Managed Objects groups

adGenSystemProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 1, 2, 1, 1)
)
adGenSystemProductGroup.setObjects(
      *(("ADTRAN-GENSYSTEM-MIB", "adGenSystemProductSnmpIdentifier"),
        ("ADTRAN-GENSYSTEM-MIB", "adGenSystemFeatureSupport"),
        ("ADTRAN-GENSYSTEM-MIB", "adGenSystemFeatureSupportByteMap"))
)
if mibBuilder.loadTexts:
    adGenSystemProductGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENSYSTEM-MIB",
    **{"adGenSystemProductTable": adGenSystemProductTable,
       "adGenSystemProductEntry": adGenSystemProductEntry,
       "adGenSystemProductSnmpIdentifier": adGenSystemProductSnmpIdentifier,
       "adGenSystemFeatureSupport": adGenSystemFeatureSupport,
       "adGenSystemFeatureSupportByteMap": adGenSystemFeatureSupportByteMap,
       "adGenSystemMibConformance": adGenSystemMibConformance,
       "adGenSystemMibGroups": adGenSystemMibGroups,
       "adGenSystemProductGroup": adGenSystemProductGroup,
       "adGenSystemProductMgGrp": adGenSystemProductMgGrp,
       "adGenSystemFeatureSupportVersionTable": adGenSystemFeatureSupportVersionTable,
       "adGenSystemFeatureSupportVersionEntry": adGenSystemFeatureSupportVersionEntry,
       "adGenSystemFeatureSupportVersionIndex": adGenSystemFeatureSupportVersionIndex,
       "adGenSystemFeatureSupportVersionQuery": adGenSystemFeatureSupportVersionQuery,
       "adGenSystemsMIB": adGenSystemsMIB}
)
