_L='packets'
_K='read-write'
_J='TruthValue'
_I='Integer32'
_H='h3cEvcSrvInstId'
_G='H3C-EVC-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
h3cEvc=ModuleIdentity((1,3,6,1,4,1,2011,10,2,106))
if mibBuilder.loadTexts:h3cEvc.setRevisions(('2009-08-08 10:00',))
_H3cEvcObjects_ObjectIdentity=ObjectIdentity
h3cEvcObjects=_H3cEvcObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,106,1))
_H3cEvcScalarGroup_ObjectIdentity=ObjectIdentity
h3cEvcScalarGroup=_H3cEvcScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,106,1,1))
class _H3cEvcSrvInstEncapCapabilities_Type(Bits):namedValues=NamedValues(*(('encapDefault',0),('encapUntagged',1),('encapTagged',2),('encapSvlanId',3),('encapSvlanIdList',4),('encapSvlanIdOnlyTagged',5),('encapSvlanIdCvlanId',6),('encapSvlanIdCvlanIdList',7),('encapCvlanId',8),('encapCvlanIdList',9)))
_H3cEvcSrvInstEncapCapabilities_Type.__name__='Bits'
_H3cEvcSrvInstEncapCapabilities_Object=MibScalar
h3cEvcSrvInstEncapCapabilities=_H3cEvcSrvInstEncapCapabilities_Object((1,3,6,1,4,1,2011,10,2,106,1,1,1),_H3cEvcSrvInstEncapCapabilities_Type())
h3cEvcSrvInstEncapCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEvcSrvInstEncapCapabilities.setStatus(_A)
_H3cEvcPortMaxSrvInstNum_Type=Integer32
_H3cEvcPortMaxSrvInstNum_Object=MibScalar
h3cEvcPortMaxSrvInstNum=_H3cEvcPortMaxSrvInstNum_Object((1,3,6,1,4,1,2011,10,2,106,1,1,2),_H3cEvcPortMaxSrvInstNum_Type())
h3cEvcPortMaxSrvInstNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEvcPortMaxSrvInstNum.setStatus(_A)
_H3cEvcSrvInstTable_Object=MibTable
h3cEvcSrvInstTable=_H3cEvcSrvInstTable_Object((1,3,6,1,4,1,2011,10,2,106,1,2))
if mibBuilder.loadTexts:h3cEvcSrvInstTable.setStatus(_A)
_H3cEvcSrvInstEntry_Object=MibTableRow
h3cEvcSrvInstEntry=_H3cEvcSrvInstEntry_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1))
h3cEvcSrvInstEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:h3cEvcSrvInstEntry.setStatus(_A)
class _H3cEvcSrvInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cEvcSrvInstId_Type.__name__=_I
_H3cEvcSrvInstId_Object=MibTableColumn
h3cEvcSrvInstId=_H3cEvcSrvInstId_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,1),_H3cEvcSrvInstId_Type())
h3cEvcSrvInstId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cEvcSrvInstId.setStatus(_A)
class _H3cEvcSrvInstEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',0),('default',1),('untagged',2),('tagged',3),('svlanIdList',4),('svlanIdListOnlyTagged',5),('svlanIdCvlanId',6),('svlanIdCvlanIdList',7),('svlanIdCvlanIdAll',8),('cvlanIdList',9)))
_H3cEvcSrvInstEncap_Type.__name__=_I
_H3cEvcSrvInstEncap_Object=MibTableColumn
h3cEvcSrvInstEncap=_H3cEvcSrvInstEncap_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,2),_H3cEvcSrvInstEncap_Type())
h3cEvcSrvInstEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstEncap.setStatus(_A)
class _H3cEvcSrvInstSvlanIdListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cEvcSrvInstSvlanIdListLow_Type.__name__=_D
_H3cEvcSrvInstSvlanIdListLow_Object=MibTableColumn
h3cEvcSrvInstSvlanIdListLow=_H3cEvcSrvInstSvlanIdListLow_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,3),_H3cEvcSrvInstSvlanIdListLow_Type())
h3cEvcSrvInstSvlanIdListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstSvlanIdListLow.setStatus(_A)
class _H3cEvcSrvInstSvlanIdListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cEvcSrvInstSvlanIdListHigh_Type.__name__=_D
_H3cEvcSrvInstSvlanIdListHigh_Object=MibTableColumn
h3cEvcSrvInstSvlanIdListHigh=_H3cEvcSrvInstSvlanIdListHigh_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,4),_H3cEvcSrvInstSvlanIdListHigh_Type())
h3cEvcSrvInstSvlanIdListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstSvlanIdListHigh.setStatus(_A)
_H3cEvcSrvInstRowStatus_Type=RowStatus
_H3cEvcSrvInstRowStatus_Object=MibTableColumn
h3cEvcSrvInstRowStatus=_H3cEvcSrvInstRowStatus_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,5),_H3cEvcSrvInstRowStatus_Type())
h3cEvcSrvInstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstRowStatus.setStatus(_A)
class _H3cEvcSrvInstEnableInStat_Type(TruthValue):defaultValue=2
_H3cEvcSrvInstEnableInStat_Type.__name__=_J
_H3cEvcSrvInstEnableInStat_Object=MibTableColumn
h3cEvcSrvInstEnableInStat=_H3cEvcSrvInstEnableInStat_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,6),_H3cEvcSrvInstEnableInStat_Type())
h3cEvcSrvInstEnableInStat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstEnableInStat.setStatus(_A)
class _H3cEvcSrvInstEnableOutStat_Type(TruthValue):defaultValue=2
_H3cEvcSrvInstEnableOutStat_Type.__name__=_J
_H3cEvcSrvInstEnableOutStat_Object=MibTableColumn
h3cEvcSrvInstEnableOutStat=_H3cEvcSrvInstEnableOutStat_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,7),_H3cEvcSrvInstEnableOutStat_Type())
h3cEvcSrvInstEnableOutStat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstEnableOutStat.setStatus(_A)
class _H3cEvcSrvInstCvlanIdListLow_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cEvcSrvInstCvlanIdListLow_Type.__name__=_D
_H3cEvcSrvInstCvlanIdListLow_Object=MibTableColumn
h3cEvcSrvInstCvlanIdListLow=_H3cEvcSrvInstCvlanIdListLow_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,8),_H3cEvcSrvInstCvlanIdListLow_Type())
h3cEvcSrvInstCvlanIdListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstCvlanIdListLow.setStatus(_A)
class _H3cEvcSrvInstCvlanIdListHigh_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cEvcSrvInstCvlanIdListHigh_Type.__name__=_D
_H3cEvcSrvInstCvlanIdListHigh_Object=MibTableColumn
h3cEvcSrvInstCvlanIdListHigh=_H3cEvcSrvInstCvlanIdListHigh_Object((1,3,6,1,4,1,2011,10,2,106,1,2,1,9),_H3cEvcSrvInstCvlanIdListHigh_Type())
h3cEvcSrvInstCvlanIdListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEvcSrvInstCvlanIdListHigh.setStatus(_A)
_H3cEvcSrvInstCarTable_Object=MibTable
h3cEvcSrvInstCarTable=_H3cEvcSrvInstCarTable_Object((1,3,6,1,4,1,2011,10,2,106,1,3))
if mibBuilder.loadTexts:h3cEvcSrvInstCarTable.setStatus(_A)
_H3cEvcSrvInstCarEntry_Object=MibTableRow
h3cEvcSrvInstCarEntry=_H3cEvcSrvInstCarEntry_Object((1,3,6,1,4,1,2011,10,2,106,1,3,1))
h3cEvcSrvInstCarEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:h3cEvcSrvInstCarEntry.setStatus(_A)
_H3cEvcSrvInstInCarIndex_Type=Integer32
_H3cEvcSrvInstInCarIndex_Object=MibTableColumn
h3cEvcSrvInstInCarIndex=_H3cEvcSrvInstInCarIndex_Object((1,3,6,1,4,1,2011,10,2,106,1,3,1,1),_H3cEvcSrvInstInCarIndex_Type())
h3cEvcSrvInstInCarIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEvcSrvInstInCarIndex.setStatus(_A)
_H3cEvcSrvInstOutCarIndex_Type=Integer32
_H3cEvcSrvInstOutCarIndex_Object=MibTableColumn
h3cEvcSrvInstOutCarIndex=_H3cEvcSrvInstOutCarIndex_Object((1,3,6,1,4,1,2011,10,2,106,1,3,1,2),_H3cEvcSrvInstOutCarIndex_Type())
h3cEvcSrvInstOutCarIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEvcSrvInstOutCarIndex.setStatus(_A)
_H3cEvcSrvInstStatInfoTable_Object=MibTable
h3cEvcSrvInstStatInfoTable=_H3cEvcSrvInstStatInfoTable_Object((1,3,6,1,4,1,2011,10,2,106,1,4))
if mibBuilder.loadTexts:h3cEvcSrvInstStatInfoTable.setStatus(_A)
_H3cEvcSrvInstStatInfoEntry_Object=MibTableRow
h3cEvcSrvInstStatInfoEntry=_H3cEvcSrvInstStatInfoEntry_Object((1,3,6,1,4,1,2011,10,2,106,1,4,1))
h3cEvcSrvInstStatInfoEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:h3cEvcSrvInstStatInfoEntry.setStatus(_A)
_H3cEvcSrvInstInPackets_Type=Counter64
_H3cEvcSrvInstInPackets_Object=MibTableColumn
h3cEvcSrvInstInPackets=_H3cEvcSrvInstInPackets_Object((1,3,6,1,4,1,2011,10,2,106,1,4,1,1),_H3cEvcSrvInstInPackets_Type())
h3cEvcSrvInstInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEvcSrvInstInPackets.setStatus(_A)
if mibBuilder.loadTexts:h3cEvcSrvInstInPackets.setUnits(_L)
_H3cEvcSrvInstInBytes_Type=Counter64
_H3cEvcSrvInstInBytes_Object=MibTableColumn
h3cEvcSrvInstInBytes=_H3cEvcSrvInstInBytes_Object((1,3,6,1,4,1,2011,10,2,106,1,4,1,2),_H3cEvcSrvInstInBytes_Type())
h3cEvcSrvInstInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEvcSrvInstInBytes.setStatus(_A)
if mibBuilder.loadTexts:h3cEvcSrvInstInBytes.setUnits('bytes')
_H3cEvcSrvInstOutPackets_Type=Counter64
_H3cEvcSrvInstOutPackets_Object=MibTableColumn
h3cEvcSrvInstOutPackets=_H3cEvcSrvInstOutPackets_Object((1,3,6,1,4,1,2011,10,2,106,1,4,1,3),_H3cEvcSrvInstOutPackets_Type())
h3cEvcSrvInstOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEvcSrvInstOutPackets.setStatus(_A)
if mibBuilder.loadTexts:h3cEvcSrvInstOutPackets.setUnits(_L)
_H3cEvcSrvInstOutBytes_Type=Counter64
_H3cEvcSrvInstOutBytes_Object=MibTableColumn
h3cEvcSrvInstOutBytes=_H3cEvcSrvInstOutBytes_Object((1,3,6,1,4,1,2011,10,2,106,1,4,1,4),_H3cEvcSrvInstOutBytes_Type())
h3cEvcSrvInstOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cEvcSrvInstOutBytes.setStatus(_A)
if mibBuilder.loadTexts:h3cEvcSrvInstOutBytes.setUnits('bytes')
mibBuilder.exportSymbols(_G,**{'h3cEvc':h3cEvc,'h3cEvcObjects':h3cEvcObjects,'h3cEvcScalarGroup':h3cEvcScalarGroup,'h3cEvcSrvInstEncapCapabilities':h3cEvcSrvInstEncapCapabilities,'h3cEvcPortMaxSrvInstNum':h3cEvcPortMaxSrvInstNum,'h3cEvcSrvInstTable':h3cEvcSrvInstTable,'h3cEvcSrvInstEntry':h3cEvcSrvInstEntry,_H:h3cEvcSrvInstId,'h3cEvcSrvInstEncap':h3cEvcSrvInstEncap,'h3cEvcSrvInstSvlanIdListLow':h3cEvcSrvInstSvlanIdListLow,'h3cEvcSrvInstSvlanIdListHigh':h3cEvcSrvInstSvlanIdListHigh,'h3cEvcSrvInstRowStatus':h3cEvcSrvInstRowStatus,'h3cEvcSrvInstEnableInStat':h3cEvcSrvInstEnableInStat,'h3cEvcSrvInstEnableOutStat':h3cEvcSrvInstEnableOutStat,'h3cEvcSrvInstCvlanIdListLow':h3cEvcSrvInstCvlanIdListLow,'h3cEvcSrvInstCvlanIdListHigh':h3cEvcSrvInstCvlanIdListHigh,'h3cEvcSrvInstCarTable':h3cEvcSrvInstCarTable,'h3cEvcSrvInstCarEntry':h3cEvcSrvInstCarEntry,'h3cEvcSrvInstInCarIndex':h3cEvcSrvInstInCarIndex,'h3cEvcSrvInstOutCarIndex':h3cEvcSrvInstOutCarIndex,'h3cEvcSrvInstStatInfoTable':h3cEvcSrvInstStatInfoTable,'h3cEvcSrvInstStatInfoEntry':h3cEvcSrvInstStatInfoEntry,'h3cEvcSrvInstInPackets':h3cEvcSrvInstInPackets,'h3cEvcSrvInstInBytes':h3cEvcSrvInstInBytes,'h3cEvcSrvInstOutPackets':h3cEvcSrvInstOutPackets,'h3cEvcSrvInstOutBytes':h3cEvcSrvInstOutBytes})