_J='adGenSystemFeatureSupportByteMap'
_I='adGenSystemFeatureSupport'
_H='adGenSystemProductSnmpIdentifier'
_G='adGenSystemFeatureSupportVersionIndex'
_F='2017-08-10 00:00'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='read-only'
_B='ADTRAN-GENSYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adShared,=mibBuilder.importSymbols('ADTRAN-MIB','adShared')
adGenSystemProduct,adGenSystemProductID,adGenSystemProductMg=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenSystemProduct','adGenSystemProductID','adGenSystemProductMg')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenSystemsMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,1,1))
if mibBuilder.loadTexts:adGenSystemsMIB.setRevisions(('2022-05-31 00:00','2022-03-30 00:00','2022-03-29 00:00','2022-03-11 00:00','2022-02-23 00:00','2022-01-07 00:00','2021-07-06 00:00','2020-12-01 00:00','2020-05-11 00:00','2020-04-13 00:00','2019-10-09 00:00','2019-07-31 00:00','2019-04-04 00:00','2019-03-21 00:00','2018-01-09 00:00','2018-08-29 00:00','2018-07-16 00:00','2018-04-02 00:00','2018-02-22 00:00','2018-01-26 00:00','2018-01-17 00:00','2017-10-16 00:00','2017-10-12 00:00','2017-09-23 00:00',_F,_F,'2017-06-06 00:00','2017-04-14 00:00','2016-12-07 00:00','2016-11-28 00:00','2016-10-10 00:00','2016-09-15 00:00','2016-06-13 00:00','2016-04-01 00:00','2016-03-16 00:00','2016-02-22 00:00','2016-01-04 00:00','2015-10-29 00:00','2015-10-07 00:00','2015-10-06 00:00','2015-09-30 00:00','2015-08-12 00:00','2015-08-05 00:00','2015-05-07 00:00','2015-03-19 00:00','2015-02-23 00:00','2015-01-22 00:00','2015-01-06 00:00','2014-12-17 00:00','2014-12-15 00:00','2014-12-10 00:00','2014-12-09 00:00','2014-12-05 00:00','2014-10-31 00:00','2014-10-15 00:00','2014-10-13 00:00','2014-09-30 00:00','2014-09-22 00:00','2014-09-15 00:00','2014-06-27 00:00','2014-06-25 00:00','2014-06-21 00:00','2014-06-20 00:00','2014-06-16 00:00','2014-06-10 00:00','2014-05-16 00:00','2014-05-13 00:00','2014-05-08 00:00','2014-04-22 00:00','2014-04-02 00:00','2014-03-14 00:00','2014-03-06 00:00','2014-02-18 00:00','2014-02-07 00:00','2014-01-30 00:00','2014-01-06 00:00','2013-12-12 00:00','2013-11-08 00:00','2013-10-17 00:00','2013-10-09 00:00','2013-10-07 00:00','2013-10-04 00:00','2013-09-13 00:00','2013-09-04 00:00','2013-08-26 00:00','2013-07-18 00:00','2013-06-11 00:00','2013-05-02 00:00','2013-04-10 00:00','2013-03-11 00:00','2013-02-21 00:00','2013-01-16 00:00','2012-11-08 00:00','2012-11-06 00:00','2012-10-08 00:00','2012-10-04 00:00','2012-09-05 00:00','2012-08-23 00:00','2012-08-09 00:00','2012-07-31 00:00','2012-07-23 00:00','2012-05-22 08:25','2012-05-03 00:00','2012-04-30 00:00','2012-04-20 00:00','2012-04-17 00:00','2012-03-06 00:00','2012-02-06 00:00','2011-10-19 00:00','2011-09-20 00:00','2011-08-29 00:00','2011-08-22 00:00','2011-06-22 00:00','2011-05-09 00:00','2011-04-18 00:00','2011-04-14 00:00','2011-04-12 00:00','2011-04-11 15:51','2011-04-07 19:02','2011-03-28 15:00','2011-03-24 14:23','2011-03-24 11:00','2011-03-24 00:00','2011-03-21 00:00','2011-03-08 00:00','2007-05-01 00:00'))
_AdGenSystemProductTable_Object=MibTable
adGenSystemProductTable=_AdGenSystemProductTable_Object((1,3,6,1,4,1,664,5,70,1,1))
if mibBuilder.loadTexts:adGenSystemProductTable.setStatus(_A)
_AdGenSystemProductEntry_Object=MibTableRow
adGenSystemProductEntry=_AdGenSystemProductEntry_Object((1,3,6,1,4,1,664,5,70,1,1,1))
adGenSystemProductEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenSystemProductEntry.setStatus(_A)
_AdGenSystemProductSnmpIdentifier_Type=DisplayString
_AdGenSystemProductSnmpIdentifier_Object=MibTableColumn
adGenSystemProductSnmpIdentifier=_AdGenSystemProductSnmpIdentifier_Object((1,3,6,1,4,1,664,5,70,1,1,1,1),_AdGenSystemProductSnmpIdentifier_Type())
adGenSystemProductSnmpIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSystemProductSnmpIdentifier.setStatus(_A)
_AdGenSystemFeatureSupport_Type=DisplayString
_AdGenSystemFeatureSupport_Object=MibTableColumn
adGenSystemFeatureSupport=_AdGenSystemFeatureSupport_Object((1,3,6,1,4,1,664,5,70,1,1,1,2),_AdGenSystemFeatureSupport_Type())
adGenSystemFeatureSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSystemFeatureSupport.setStatus(_A)
_AdGenSystemFeatureSupportByteMap_Type=OctetString
_AdGenSystemFeatureSupportByteMap_Object=MibTableColumn
adGenSystemFeatureSupportByteMap=_AdGenSystemFeatureSupportByteMap_Object((1,3,6,1,4,1,664,5,70,1,1,1,3),_AdGenSystemFeatureSupportByteMap_Type())
adGenSystemFeatureSupportByteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSystemFeatureSupportByteMap.setStatus(_A)
_AdGenSystemMibConformance_ObjectIdentity=ObjectIdentity
adGenSystemMibConformance=_AdGenSystemMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,70,1,2))
_AdGenSystemMibGroups_ObjectIdentity=ObjectIdentity
adGenSystemMibGroups=_AdGenSystemMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,70,1,2,1))
_AdGenSystemProductMgGrp_ObjectIdentity=ObjectIdentity
adGenSystemProductMgGrp=_AdGenSystemProductMgGrp_ObjectIdentity((1,3,6,1,4,1,664,5,70,6,1))
_AdGenSystemFeatureSupportVersionTable_Object=MibTable
adGenSystemFeatureSupportVersionTable=_AdGenSystemFeatureSupportVersionTable_Object((1,3,6,1,4,1,664,5,70,6,1,1))
if mibBuilder.loadTexts:adGenSystemFeatureSupportVersionTable.setStatus(_A)
_AdGenSystemFeatureSupportVersionEntry_Object=MibTableRow
adGenSystemFeatureSupportVersionEntry=_AdGenSystemFeatureSupportVersionEntry_Object((1,3,6,1,4,1,664,5,70,6,1,1,1))
adGenSystemFeatureSupportVersionEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:adGenSystemFeatureSupportVersionEntry.setStatus(_A)
_AdGenSystemFeatureSupportVersionIndex_Type=Integer32
_AdGenSystemFeatureSupportVersionIndex_Object=MibTableColumn
adGenSystemFeatureSupportVersionIndex=_AdGenSystemFeatureSupportVersionIndex_Object((1,3,6,1,4,1,664,5,70,6,1,1,1,1),_AdGenSystemFeatureSupportVersionIndex_Type())
adGenSystemFeatureSupportVersionIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenSystemFeatureSupportVersionIndex.setStatus(_A)
_AdGenSystemFeatureSupportVersionQuery_Type=OctetString
_AdGenSystemFeatureSupportVersionQuery_Object=MibTableColumn
adGenSystemFeatureSupportVersionQuery=_AdGenSystemFeatureSupportVersionQuery_Object((1,3,6,1,4,1,664,5,70,6,1,1,1,2),_AdGenSystemFeatureSupportVersionQuery_Type())
adGenSystemFeatureSupportVersionQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSystemFeatureSupportVersionQuery.setStatus(_A)
adGenSystemProductGroup=ObjectGroup((1,3,6,1,4,1,664,5,70,1,2,1,1))
adGenSystemProductGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adGenSystemProductGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenSystemProductTable':adGenSystemProductTable,'adGenSystemProductEntry':adGenSystemProductEntry,_H:adGenSystemProductSnmpIdentifier,_I:adGenSystemFeatureSupport,_J:adGenSystemFeatureSupportByteMap,'adGenSystemMibConformance':adGenSystemMibConformance,'adGenSystemMibGroups':adGenSystemMibGroups,'adGenSystemProductGroup':adGenSystemProductGroup,'adGenSystemProductMgGrp':adGenSystemProductMgGrp,'adGenSystemFeatureSupportVersionTable':adGenSystemFeatureSupportVersionTable,'adGenSystemFeatureSupportVersionEntry':adGenSystemFeatureSupportVersionEntry,_G:adGenSystemFeatureSupportVersionIndex,'adGenSystemFeatureSupportVersionQuery':adGenSystemFeatureSupportVersionQuery,'adGenSystemsMIB':adGenSystemsMIB})