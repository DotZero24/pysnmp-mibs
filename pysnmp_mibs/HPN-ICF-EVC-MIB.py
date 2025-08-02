_L='packets'
_K='read-write'
_J='TruthValue'
_I='Integer32'
_H='hpnicfEvcSrvInstId'
_G='HPN-ICF-EVC-MIB'
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
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
hpnicfEvc=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,106))
if mibBuilder.loadTexts:hpnicfEvc.setRevisions(('2009-08-08 10:00',))
_HpnicfEvcObjects_ObjectIdentity=ObjectIdentity
hpnicfEvcObjects=_HpnicfEvcObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,106,1))
_HpnicfEvcScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfEvcScalarGroup=_HpnicfEvcScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,106,1,1))
class _HpnicfEvcSrvInstEncapCapabilities_Type(Bits):namedValues=NamedValues(*(('encapDefault',0),('encapUntagged',1),('encapTagged',2),('encapSvlanId',3),('encapSvlanIdList',4),('encapSvlanIdOnlyTagged',5),('encapSvlanIdCvlanId',6),('encapSvlanIdCvlanIdList',7),('encapCvlanId',8),('encapCvlanIdList',9)))
_HpnicfEvcSrvInstEncapCapabilities_Type.__name__='Bits'
_HpnicfEvcSrvInstEncapCapabilities_Object=MibScalar
hpnicfEvcSrvInstEncapCapabilities=_HpnicfEvcSrvInstEncapCapabilities_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,1,1),_HpnicfEvcSrvInstEncapCapabilities_Type())
hpnicfEvcSrvInstEncapCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvcSrvInstEncapCapabilities.setStatus(_A)
_HpnicfEvcPortMaxSrvInstNum_Type=Integer32
_HpnicfEvcPortMaxSrvInstNum_Object=MibScalar
hpnicfEvcPortMaxSrvInstNum=_HpnicfEvcPortMaxSrvInstNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,1,2),_HpnicfEvcPortMaxSrvInstNum_Type())
hpnicfEvcPortMaxSrvInstNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvcPortMaxSrvInstNum.setStatus(_A)
_HpnicfEvcSrvInstTable_Object=MibTable
hpnicfEvcSrvInstTable=_HpnicfEvcSrvInstTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2))
if mibBuilder.loadTexts:hpnicfEvcSrvInstTable.setStatus(_A)
_HpnicfEvcSrvInstEntry_Object=MibTableRow
hpnicfEvcSrvInstEntry=_HpnicfEvcSrvInstEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1))
hpnicfEvcSrvInstEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:hpnicfEvcSrvInstEntry.setStatus(_A)
class _HpnicfEvcSrvInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfEvcSrvInstId_Type.__name__=_I
_HpnicfEvcSrvInstId_Object=MibTableColumn
hpnicfEvcSrvInstId=_HpnicfEvcSrvInstId_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,1),_HpnicfEvcSrvInstId_Type())
hpnicfEvcSrvInstId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfEvcSrvInstId.setStatus(_A)
class _HpnicfEvcSrvInstEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',0),('default',1),('untagged',2),('tagged',3),('svlanIdList',4),('svlanIdListOnlyTagged',5),('svlanIdCvlanId',6),('svlanIdCvlanIdList',7),('svlanIdCvlanIdAll',8),('cvlanIdList',9)))
_HpnicfEvcSrvInstEncap_Type.__name__=_I
_HpnicfEvcSrvInstEncap_Object=MibTableColumn
hpnicfEvcSrvInstEncap=_HpnicfEvcSrvInstEncap_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,2),_HpnicfEvcSrvInstEncap_Type())
hpnicfEvcSrvInstEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstEncap.setStatus(_A)
class _HpnicfEvcSrvInstSvlanIdListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfEvcSrvInstSvlanIdListLow_Type.__name__=_D
_HpnicfEvcSrvInstSvlanIdListLow_Object=MibTableColumn
hpnicfEvcSrvInstSvlanIdListLow=_HpnicfEvcSrvInstSvlanIdListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,3),_HpnicfEvcSrvInstSvlanIdListLow_Type())
hpnicfEvcSrvInstSvlanIdListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstSvlanIdListLow.setStatus(_A)
class _HpnicfEvcSrvInstSvlanIdListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfEvcSrvInstSvlanIdListHigh_Type.__name__=_D
_HpnicfEvcSrvInstSvlanIdListHigh_Object=MibTableColumn
hpnicfEvcSrvInstSvlanIdListHigh=_HpnicfEvcSrvInstSvlanIdListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,4),_HpnicfEvcSrvInstSvlanIdListHigh_Type())
hpnicfEvcSrvInstSvlanIdListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstSvlanIdListHigh.setStatus(_A)
_HpnicfEvcSrvInstRowStatus_Type=RowStatus
_HpnicfEvcSrvInstRowStatus_Object=MibTableColumn
hpnicfEvcSrvInstRowStatus=_HpnicfEvcSrvInstRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,5),_HpnicfEvcSrvInstRowStatus_Type())
hpnicfEvcSrvInstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstRowStatus.setStatus(_A)
class _HpnicfEvcSrvInstEnableInStat_Type(TruthValue):defaultValue=2
_HpnicfEvcSrvInstEnableInStat_Type.__name__=_J
_HpnicfEvcSrvInstEnableInStat_Object=MibTableColumn
hpnicfEvcSrvInstEnableInStat=_HpnicfEvcSrvInstEnableInStat_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,6),_HpnicfEvcSrvInstEnableInStat_Type())
hpnicfEvcSrvInstEnableInStat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstEnableInStat.setStatus(_A)
class _HpnicfEvcSrvInstEnableOutStat_Type(TruthValue):defaultValue=2
_HpnicfEvcSrvInstEnableOutStat_Type.__name__=_J
_HpnicfEvcSrvInstEnableOutStat_Object=MibTableColumn
hpnicfEvcSrvInstEnableOutStat=_HpnicfEvcSrvInstEnableOutStat_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,7),_HpnicfEvcSrvInstEnableOutStat_Type())
hpnicfEvcSrvInstEnableOutStat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstEnableOutStat.setStatus(_A)
class _HpnicfEvcSrvInstCvlanIdListLow_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfEvcSrvInstCvlanIdListLow_Type.__name__=_D
_HpnicfEvcSrvInstCvlanIdListLow_Object=MibTableColumn
hpnicfEvcSrvInstCvlanIdListLow=_HpnicfEvcSrvInstCvlanIdListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,8),_HpnicfEvcSrvInstCvlanIdListLow_Type())
hpnicfEvcSrvInstCvlanIdListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstCvlanIdListLow.setStatus(_A)
class _HpnicfEvcSrvInstCvlanIdListHigh_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfEvcSrvInstCvlanIdListHigh_Type.__name__=_D
_HpnicfEvcSrvInstCvlanIdListHigh_Object=MibTableColumn
hpnicfEvcSrvInstCvlanIdListHigh=_HpnicfEvcSrvInstCvlanIdListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,2,1,9),_HpnicfEvcSrvInstCvlanIdListHigh_Type())
hpnicfEvcSrvInstCvlanIdListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEvcSrvInstCvlanIdListHigh.setStatus(_A)
_HpnicfEvcSrvInstCarTable_Object=MibTable
hpnicfEvcSrvInstCarTable=_HpnicfEvcSrvInstCarTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,3))
if mibBuilder.loadTexts:hpnicfEvcSrvInstCarTable.setStatus(_A)
_HpnicfEvcSrvInstCarEntry_Object=MibTableRow
hpnicfEvcSrvInstCarEntry=_HpnicfEvcSrvInstCarEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,3,1))
hpnicfEvcSrvInstCarEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:hpnicfEvcSrvInstCarEntry.setStatus(_A)
_HpnicfEvcSrvInstInCarIndex_Type=Integer32
_HpnicfEvcSrvInstInCarIndex_Object=MibTableColumn
hpnicfEvcSrvInstInCarIndex=_HpnicfEvcSrvInstInCarIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,3,1,1),_HpnicfEvcSrvInstInCarIndex_Type())
hpnicfEvcSrvInstInCarIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEvcSrvInstInCarIndex.setStatus(_A)
_HpnicfEvcSrvInstOutCarIndex_Type=Integer32
_HpnicfEvcSrvInstOutCarIndex_Object=MibTableColumn
hpnicfEvcSrvInstOutCarIndex=_HpnicfEvcSrvInstOutCarIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,3,1,2),_HpnicfEvcSrvInstOutCarIndex_Type())
hpnicfEvcSrvInstOutCarIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEvcSrvInstOutCarIndex.setStatus(_A)
_HpnicfEvcSrvInstStatInfoTable_Object=MibTable
hpnicfEvcSrvInstStatInfoTable=_HpnicfEvcSrvInstStatInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,4))
if mibBuilder.loadTexts:hpnicfEvcSrvInstStatInfoTable.setStatus(_A)
_HpnicfEvcSrvInstStatInfoEntry_Object=MibTableRow
hpnicfEvcSrvInstStatInfoEntry=_HpnicfEvcSrvInstStatInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,4,1))
hpnicfEvcSrvInstStatInfoEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:hpnicfEvcSrvInstStatInfoEntry.setStatus(_A)
_HpnicfEvcSrvInstInPackets_Type=Counter64
_HpnicfEvcSrvInstInPackets_Object=MibTableColumn
hpnicfEvcSrvInstInPackets=_HpnicfEvcSrvInstInPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,4,1,1),_HpnicfEvcSrvInstInPackets_Type())
hpnicfEvcSrvInstInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvcSrvInstInPackets.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEvcSrvInstInPackets.setUnits(_L)
_HpnicfEvcSrvInstInBytes_Type=Counter64
_HpnicfEvcSrvInstInBytes_Object=MibTableColumn
hpnicfEvcSrvInstInBytes=_HpnicfEvcSrvInstInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,4,1,2),_HpnicfEvcSrvInstInBytes_Type())
hpnicfEvcSrvInstInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvcSrvInstInBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEvcSrvInstInBytes.setUnits('bytes')
_HpnicfEvcSrvInstOutPackets_Type=Counter64
_HpnicfEvcSrvInstOutPackets_Object=MibTableColumn
hpnicfEvcSrvInstOutPackets=_HpnicfEvcSrvInstOutPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,4,1,3),_HpnicfEvcSrvInstOutPackets_Type())
hpnicfEvcSrvInstOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvcSrvInstOutPackets.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEvcSrvInstOutPackets.setUnits(_L)
_HpnicfEvcSrvInstOutBytes_Type=Counter64
_HpnicfEvcSrvInstOutBytes_Object=MibTableColumn
hpnicfEvcSrvInstOutBytes=_HpnicfEvcSrvInstOutBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,106,1,4,1,4),_HpnicfEvcSrvInstOutBytes_Type())
hpnicfEvcSrvInstOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEvcSrvInstOutBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfEvcSrvInstOutBytes.setUnits('bytes')
mibBuilder.exportSymbols(_G,**{'hpnicfEvc':hpnicfEvc,'hpnicfEvcObjects':hpnicfEvcObjects,'hpnicfEvcScalarGroup':hpnicfEvcScalarGroup,'hpnicfEvcSrvInstEncapCapabilities':hpnicfEvcSrvInstEncapCapabilities,'hpnicfEvcPortMaxSrvInstNum':hpnicfEvcPortMaxSrvInstNum,'hpnicfEvcSrvInstTable':hpnicfEvcSrvInstTable,'hpnicfEvcSrvInstEntry':hpnicfEvcSrvInstEntry,_H:hpnicfEvcSrvInstId,'hpnicfEvcSrvInstEncap':hpnicfEvcSrvInstEncap,'hpnicfEvcSrvInstSvlanIdListLow':hpnicfEvcSrvInstSvlanIdListLow,'hpnicfEvcSrvInstSvlanIdListHigh':hpnicfEvcSrvInstSvlanIdListHigh,'hpnicfEvcSrvInstRowStatus':hpnicfEvcSrvInstRowStatus,'hpnicfEvcSrvInstEnableInStat':hpnicfEvcSrvInstEnableInStat,'hpnicfEvcSrvInstEnableOutStat':hpnicfEvcSrvInstEnableOutStat,'hpnicfEvcSrvInstCvlanIdListLow':hpnicfEvcSrvInstCvlanIdListLow,'hpnicfEvcSrvInstCvlanIdListHigh':hpnicfEvcSrvInstCvlanIdListHigh,'hpnicfEvcSrvInstCarTable':hpnicfEvcSrvInstCarTable,'hpnicfEvcSrvInstCarEntry':hpnicfEvcSrvInstCarEntry,'hpnicfEvcSrvInstInCarIndex':hpnicfEvcSrvInstInCarIndex,'hpnicfEvcSrvInstOutCarIndex':hpnicfEvcSrvInstOutCarIndex,'hpnicfEvcSrvInstStatInfoTable':hpnicfEvcSrvInstStatInfoTable,'hpnicfEvcSrvInstStatInfoEntry':hpnicfEvcSrvInstStatInfoEntry,'hpnicfEvcSrvInstInPackets':hpnicfEvcSrvInstInPackets,'hpnicfEvcSrvInstInBytes':hpnicfEvcSrvInstInBytes,'hpnicfEvcSrvInstOutPackets':hpnicfEvcSrvInstOutPackets,'hpnicfEvcSrvInstOutBytes':hpnicfEvcSrvInstOutBytes})