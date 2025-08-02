_Q='ntwsInfoRFDetectCurrentXmtrTableSizeGroup'
_P='ntwsInfoRFDetectXmtrClassificationGroup'
_O='ntwsInfoRFDetectXmtrGroup'
_N='ntwsInfoRFDetectCurrentXmtrTableSize'
_M='ntwsInfoRFDetectXmtrClassificationReason'
_L='ntwsInfoRFDetectXmtrClassification'
_K='ntwsInfoRFDetectXmtrNetworkingMode'
_J='ntwsInfoRFDetectXmtrSsid'
_I='ntwsInfoRFDetectXmtrRssi'
_H='ntwsInfoRFDetectXmtrChannelNum'
_G='ntwsInfoRFDetectXmtrListenerMacAddress'
_F='ntwsInfoRFDetectXmtrTransmitterMacAddress'
_E='DisplayString'
_D='not-accessible'
_C='read-only'
_B='NTWS-INFO-RF-DETECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtwsChannelNum,NtwsRssi=mibBuilder.importSymbols('NTWS-AP-TC','NtwsChannelNum','NtwsRssi')
NtwsRFDetectClassification,NtwsRFDetectClassificationReason,NtwsRFDetectNetworkingMode=mibBuilder.importSymbols('NTWS-RF-DETECT-TC','NtwsRFDetectClassification','NtwsRFDetectClassificationReason','NtwsRFDetectNetworkingMode')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention')
ntwsInfoRFDetectMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,9))
if mibBuilder.loadTexts:ntwsInfoRFDetectMib.setRevisions(('2007-09-25 00:12','2007-06-27 00:11','2007-04-18 00:10','2006-10-11 00:03'))
_NtwsInfoRFDetectObjects_ObjectIdentity=ObjectIdentity
ntwsInfoRFDetectObjects=_NtwsInfoRFDetectObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,9,1))
_NtwsInfoRFDetectDataObjects_ObjectIdentity=ObjectIdentity
ntwsInfoRFDetectDataObjects=_NtwsInfoRFDetectDataObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,9,1,1))
_NtwsInfoRFDetectXmtrTable_Object=MibTable
ntwsInfoRFDetectXmtrTable=_NtwsInfoRFDetectXmtrTable_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1))
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrTable.setStatus(_A)
_NtwsInfoRFDetectXmtrEntry_Object=MibTableRow
ntwsInfoRFDetectXmtrEntry=_NtwsInfoRFDetectXmtrEntry_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1))
ntwsInfoRFDetectXmtrEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrEntry.setStatus(_A)
_NtwsInfoRFDetectXmtrTransmitterMacAddress_Type=MacAddress
_NtwsInfoRFDetectXmtrTransmitterMacAddress_Object=MibTableColumn
ntwsInfoRFDetectXmtrTransmitterMacAddress=_NtwsInfoRFDetectXmtrTransmitterMacAddress_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,1),_NtwsInfoRFDetectXmtrTransmitterMacAddress_Type())
ntwsInfoRFDetectXmtrTransmitterMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrTransmitterMacAddress.setStatus(_A)
_NtwsInfoRFDetectXmtrListenerMacAddress_Type=MacAddress
_NtwsInfoRFDetectXmtrListenerMacAddress_Object=MibTableColumn
ntwsInfoRFDetectXmtrListenerMacAddress=_NtwsInfoRFDetectXmtrListenerMacAddress_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,2),_NtwsInfoRFDetectXmtrListenerMacAddress_Type())
ntwsInfoRFDetectXmtrListenerMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrListenerMacAddress.setStatus(_A)
_NtwsInfoRFDetectXmtrChannelNum_Type=NtwsChannelNum
_NtwsInfoRFDetectXmtrChannelNum_Object=MibTableColumn
ntwsInfoRFDetectXmtrChannelNum=_NtwsInfoRFDetectXmtrChannelNum_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,3),_NtwsInfoRFDetectXmtrChannelNum_Type())
ntwsInfoRFDetectXmtrChannelNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrChannelNum.setStatus(_A)
_NtwsInfoRFDetectXmtrRssi_Type=NtwsRssi
_NtwsInfoRFDetectXmtrRssi_Object=MibTableColumn
ntwsInfoRFDetectXmtrRssi=_NtwsInfoRFDetectXmtrRssi_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,4),_NtwsInfoRFDetectXmtrRssi_Type())
ntwsInfoRFDetectXmtrRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrRssi.setStatus(_A)
class _NtwsInfoRFDetectXmtrSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsInfoRFDetectXmtrSsid_Type.__name__=_E
_NtwsInfoRFDetectXmtrSsid_Object=MibTableColumn
ntwsInfoRFDetectXmtrSsid=_NtwsInfoRFDetectXmtrSsid_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,5),_NtwsInfoRFDetectXmtrSsid_Type())
ntwsInfoRFDetectXmtrSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrSsid.setStatus(_A)
_NtwsInfoRFDetectXmtrNetworkingMode_Type=NtwsRFDetectNetworkingMode
_NtwsInfoRFDetectXmtrNetworkingMode_Object=MibTableColumn
ntwsInfoRFDetectXmtrNetworkingMode=_NtwsInfoRFDetectXmtrNetworkingMode_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,6),_NtwsInfoRFDetectXmtrNetworkingMode_Type())
ntwsInfoRFDetectXmtrNetworkingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrNetworkingMode.setStatus(_A)
_NtwsInfoRFDetectXmtrClassification_Type=NtwsRFDetectClassification
_NtwsInfoRFDetectXmtrClassification_Object=MibTableColumn
ntwsInfoRFDetectXmtrClassification=_NtwsInfoRFDetectXmtrClassification_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,7),_NtwsInfoRFDetectXmtrClassification_Type())
ntwsInfoRFDetectXmtrClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrClassification.setStatus(_A)
_NtwsInfoRFDetectXmtrClassificationReason_Type=NtwsRFDetectClassificationReason
_NtwsInfoRFDetectXmtrClassificationReason_Object=MibTableColumn
ntwsInfoRFDetectXmtrClassificationReason=_NtwsInfoRFDetectXmtrClassificationReason_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,1,1,8),_NtwsInfoRFDetectXmtrClassificationReason_Type())
ntwsInfoRFDetectXmtrClassificationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrClassificationReason.setStatus(_A)
_NtwsInfoRFDetectCurrentXmtrTableSize_Type=Gauge32
_NtwsInfoRFDetectCurrentXmtrTableSize_Object=MibScalar
ntwsInfoRFDetectCurrentXmtrTableSize=_NtwsInfoRFDetectCurrentXmtrTableSize_Object((1,3,6,1,4,1,45,6,1,4,9,1,1,2),_NtwsInfoRFDetectCurrentXmtrTableSize_Type())
ntwsInfoRFDetectCurrentXmtrTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsInfoRFDetectCurrentXmtrTableSize.setStatus(_A)
_NtwsInfoRFDetectConformance_ObjectIdentity=ObjectIdentity
ntwsInfoRFDetectConformance=_NtwsInfoRFDetectConformance_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,9,1,2))
_NtwsInfoRFDetectCompliances_ObjectIdentity=ObjectIdentity
ntwsInfoRFDetectCompliances=_NtwsInfoRFDetectCompliances_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,9,1,2,1))
_NtwsInfoRFDetectGroups_ObjectIdentity=ObjectIdentity
ntwsInfoRFDetectGroups=_NtwsInfoRFDetectGroups_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,9,1,2,2))
ntwsInfoRFDetectXmtrGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,9,1,2,2,1))
ntwsInfoRFDetectXmtrGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrGroup.setStatus(_A)
ntwsInfoRFDetectXmtrClassificationGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,9,1,2,2,2))
ntwsInfoRFDetectXmtrClassificationGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ntwsInfoRFDetectXmtrClassificationGroup.setStatus(_A)
ntwsInfoRFDetectCurrentXmtrTableSizeGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,9,1,2,2,3))
ntwsInfoRFDetectCurrentXmtrTableSizeGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:ntwsInfoRFDetectCurrentXmtrTableSizeGroup.setStatus(_A)
ntwsInfoRFDetectCompliance=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,9,1,2,1,1))
ntwsInfoRFDetectCompliance.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ntwsInfoRFDetectCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntwsInfoRFDetectMib':ntwsInfoRFDetectMib,'ntwsInfoRFDetectObjects':ntwsInfoRFDetectObjects,'ntwsInfoRFDetectDataObjects':ntwsInfoRFDetectDataObjects,'ntwsInfoRFDetectXmtrTable':ntwsInfoRFDetectXmtrTable,'ntwsInfoRFDetectXmtrEntry':ntwsInfoRFDetectXmtrEntry,_F:ntwsInfoRFDetectXmtrTransmitterMacAddress,_G:ntwsInfoRFDetectXmtrListenerMacAddress,_H:ntwsInfoRFDetectXmtrChannelNum,_I:ntwsInfoRFDetectXmtrRssi,_J:ntwsInfoRFDetectXmtrSsid,_K:ntwsInfoRFDetectXmtrNetworkingMode,_L:ntwsInfoRFDetectXmtrClassification,_M:ntwsInfoRFDetectXmtrClassificationReason,_N:ntwsInfoRFDetectCurrentXmtrTableSize,'ntwsInfoRFDetectConformance':ntwsInfoRFDetectConformance,'ntwsInfoRFDetectCompliances':ntwsInfoRFDetectCompliances,'ntwsInfoRFDetectCompliance':ntwsInfoRFDetectCompliance,'ntwsInfoRFDetectGroups':ntwsInfoRFDetectGroups,_O:ntwsInfoRFDetectXmtrGroup,_P:ntwsInfoRFDetectXmtrClassificationGroup,_Q:ntwsInfoRFDetectCurrentXmtrTableSizeGroup})