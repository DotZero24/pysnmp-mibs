_b='trpzInfoRFDetectClientGroup'
_a='trpzInfoRFDetectClientClassification'
_Z='trpzInfoRFDetectClientRssi'
_Y='trpzInfoRFDetectClientRate'
_X='trpzInfoRFDetectClientChannelNum'
_W='trpzInfoRFDetectClientModulation'
_V='trpzInfoRFDetectClientApRadioIndex'
_U='trpzInfoRFDetectClientApNum'
_T='trpzInfoRFDetectClientConnectedBssid'
_S='trpzInfoRFDetectCurrentXmtrTableSize'
_R='trpzInfoRFDetectXmtrClassificationReason'
_Q='trpzInfoRFDetectXmtrClassification'
_P='trpzInfoRFDetectXmtrNetworkingMode'
_O='trpzInfoRFDetectXmtrSsid'
_N='trpzInfoRFDetectXmtrRssi'
_M='trpzInfoRFDetectClientListenerMacAddress'
_L='trpzInfoRFDetectClientMacAddress'
_K='trpzInfoRFDetectXmtrChannelNum'
_J='trpzInfoRFDetectXmtrListenerMacAddress'
_I='trpzInfoRFDetectXmtrTransmitterMacAddress'
_H='DisplayString'
_G='trpzInfoRFDetectCurrentXmtrTableSizeGroup'
_F='trpzInfoRFDetectXmtrClassificationGroup'
_E='trpzInfoRFDetectXmtrGroup'
_D='not-accessible'
_C='read-only'
_B='TRAPEZE-NETWORKS-INFO-RF-DETECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','TextualConvention')
TrpzApNum,TrpzApRadioIndex,TrpzChannelNum,TrpzRadioRateEx,TrpzRssi=mibBuilder.importSymbols('TRAPEZE-NETWORKS-AP-TC','TrpzApNum','TrpzApRadioIndex','TrpzChannelNum','TrpzRadioRateEx','TrpzRssi')
TrpzRFDetectClassification,TrpzRFDetectClassificationReason,TrpzRFDetectDot11ModulationStandard,TrpzRFDetectNetworkingMode=mibBuilder.importSymbols('TRAPEZE-NETWORKS-RF-DETECT-TC','TrpzRFDetectClassification','TrpzRFDetectClassificationReason','TrpzRFDetectDot11ModulationStandard','TrpzRFDetectNetworkingMode')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzInfoRFDetectMib=ModuleIdentity((1,3,6,1,4,1,14525,4,9))
if mibBuilder.loadTexts:trpzInfoRFDetectMib.setRevisions(('2011-07-27 00:22','2009-08-18 00:21','2007-06-27 00:11','2007-04-18 00:10','2006-10-11 00:03'))
_TrpzInfoRFDetectObjects_ObjectIdentity=ObjectIdentity
trpzInfoRFDetectObjects=_TrpzInfoRFDetectObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,9,1))
_TrpzInfoRFDetectDataObjects_ObjectIdentity=ObjectIdentity
trpzInfoRFDetectDataObjects=_TrpzInfoRFDetectDataObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,9,1,1))
_TrpzInfoRFDetectXmtrTable_Object=MibTable
trpzInfoRFDetectXmtrTable=_TrpzInfoRFDetectXmtrTable_Object((1,3,6,1,4,1,14525,4,9,1,1,1))
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrTable.setStatus(_A)
_TrpzInfoRFDetectXmtrEntry_Object=MibTableRow
trpzInfoRFDetectXmtrEntry=_TrpzInfoRFDetectXmtrEntry_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1))
trpzInfoRFDetectXmtrEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrEntry.setStatus(_A)
_TrpzInfoRFDetectXmtrTransmitterMacAddress_Type=MacAddress
_TrpzInfoRFDetectXmtrTransmitterMacAddress_Object=MibTableColumn
trpzInfoRFDetectXmtrTransmitterMacAddress=_TrpzInfoRFDetectXmtrTransmitterMacAddress_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,1),_TrpzInfoRFDetectXmtrTransmitterMacAddress_Type())
trpzInfoRFDetectXmtrTransmitterMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrTransmitterMacAddress.setStatus(_A)
_TrpzInfoRFDetectXmtrListenerMacAddress_Type=MacAddress
_TrpzInfoRFDetectXmtrListenerMacAddress_Object=MibTableColumn
trpzInfoRFDetectXmtrListenerMacAddress=_TrpzInfoRFDetectXmtrListenerMacAddress_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,2),_TrpzInfoRFDetectXmtrListenerMacAddress_Type())
trpzInfoRFDetectXmtrListenerMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrListenerMacAddress.setStatus(_A)
_TrpzInfoRFDetectXmtrChannelNum_Type=TrpzChannelNum
_TrpzInfoRFDetectXmtrChannelNum_Object=MibTableColumn
trpzInfoRFDetectXmtrChannelNum=_TrpzInfoRFDetectXmtrChannelNum_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,3),_TrpzInfoRFDetectXmtrChannelNum_Type())
trpzInfoRFDetectXmtrChannelNum.setMaxAccess(_D)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrChannelNum.setStatus(_A)
_TrpzInfoRFDetectXmtrRssi_Type=TrpzRssi
_TrpzInfoRFDetectXmtrRssi_Object=MibTableColumn
trpzInfoRFDetectXmtrRssi=_TrpzInfoRFDetectXmtrRssi_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,4),_TrpzInfoRFDetectXmtrRssi_Type())
trpzInfoRFDetectXmtrRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrRssi.setStatus(_A)
class _TrpzInfoRFDetectXmtrSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TrpzInfoRFDetectXmtrSsid_Type.__name__=_H
_TrpzInfoRFDetectXmtrSsid_Object=MibTableColumn
trpzInfoRFDetectXmtrSsid=_TrpzInfoRFDetectXmtrSsid_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,5),_TrpzInfoRFDetectXmtrSsid_Type())
trpzInfoRFDetectXmtrSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrSsid.setStatus(_A)
_TrpzInfoRFDetectXmtrNetworkingMode_Type=TrpzRFDetectNetworkingMode
_TrpzInfoRFDetectXmtrNetworkingMode_Object=MibTableColumn
trpzInfoRFDetectXmtrNetworkingMode=_TrpzInfoRFDetectXmtrNetworkingMode_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,6),_TrpzInfoRFDetectXmtrNetworkingMode_Type())
trpzInfoRFDetectXmtrNetworkingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrNetworkingMode.setStatus(_A)
_TrpzInfoRFDetectXmtrClassification_Type=TrpzRFDetectClassification
_TrpzInfoRFDetectXmtrClassification_Object=MibTableColumn
trpzInfoRFDetectXmtrClassification=_TrpzInfoRFDetectXmtrClassification_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,7),_TrpzInfoRFDetectXmtrClassification_Type())
trpzInfoRFDetectXmtrClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrClassification.setStatus(_A)
_TrpzInfoRFDetectXmtrClassificationReason_Type=TrpzRFDetectClassificationReason
_TrpzInfoRFDetectXmtrClassificationReason_Object=MibTableColumn
trpzInfoRFDetectXmtrClassificationReason=_TrpzInfoRFDetectXmtrClassificationReason_Object((1,3,6,1,4,1,14525,4,9,1,1,1,1,8),_TrpzInfoRFDetectXmtrClassificationReason_Type())
trpzInfoRFDetectXmtrClassificationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrClassificationReason.setStatus(_A)
_TrpzInfoRFDetectCurrentXmtrTableSize_Type=Gauge32
_TrpzInfoRFDetectCurrentXmtrTableSize_Object=MibScalar
trpzInfoRFDetectCurrentXmtrTableSize=_TrpzInfoRFDetectCurrentXmtrTableSize_Object((1,3,6,1,4,1,14525,4,9,1,1,2),_TrpzInfoRFDetectCurrentXmtrTableSize_Type())
trpzInfoRFDetectCurrentXmtrTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectCurrentXmtrTableSize.setStatus(_A)
_TrpzInfoRFDetectClientTable_Object=MibTable
trpzInfoRFDetectClientTable=_TrpzInfoRFDetectClientTable_Object((1,3,6,1,4,1,14525,4,9,1,1,3))
if mibBuilder.loadTexts:trpzInfoRFDetectClientTable.setStatus(_A)
_TrpzInfoRFDetectClientEntry_Object=MibTableRow
trpzInfoRFDetectClientEntry=_TrpzInfoRFDetectClientEntry_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1))
trpzInfoRFDetectClientEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:trpzInfoRFDetectClientEntry.setStatus(_A)
_TrpzInfoRFDetectClientMacAddress_Type=MacAddress
_TrpzInfoRFDetectClientMacAddress_Object=MibTableColumn
trpzInfoRFDetectClientMacAddress=_TrpzInfoRFDetectClientMacAddress_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,1),_TrpzInfoRFDetectClientMacAddress_Type())
trpzInfoRFDetectClientMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:trpzInfoRFDetectClientMacAddress.setStatus(_A)
_TrpzInfoRFDetectClientListenerMacAddress_Type=MacAddress
_TrpzInfoRFDetectClientListenerMacAddress_Object=MibTableColumn
trpzInfoRFDetectClientListenerMacAddress=_TrpzInfoRFDetectClientListenerMacAddress_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,2),_TrpzInfoRFDetectClientListenerMacAddress_Type())
trpzInfoRFDetectClientListenerMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:trpzInfoRFDetectClientListenerMacAddress.setStatus(_A)
_TrpzInfoRFDetectClientConnectedBssid_Type=MacAddress
_TrpzInfoRFDetectClientConnectedBssid_Object=MibTableColumn
trpzInfoRFDetectClientConnectedBssid=_TrpzInfoRFDetectClientConnectedBssid_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,3),_TrpzInfoRFDetectClientConnectedBssid_Type())
trpzInfoRFDetectClientConnectedBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientConnectedBssid.setStatus(_A)
_TrpzInfoRFDetectClientApNum_Type=TrpzApNum
_TrpzInfoRFDetectClientApNum_Object=MibTableColumn
trpzInfoRFDetectClientApNum=_TrpzInfoRFDetectClientApNum_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,4),_TrpzInfoRFDetectClientApNum_Type())
trpzInfoRFDetectClientApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientApNum.setStatus(_A)
_TrpzInfoRFDetectClientApRadioIndex_Type=TrpzApRadioIndex
_TrpzInfoRFDetectClientApRadioIndex_Object=MibTableColumn
trpzInfoRFDetectClientApRadioIndex=_TrpzInfoRFDetectClientApRadioIndex_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,5),_TrpzInfoRFDetectClientApRadioIndex_Type())
trpzInfoRFDetectClientApRadioIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientApRadioIndex.setStatus(_A)
_TrpzInfoRFDetectClientModulation_Type=TrpzRFDetectDot11ModulationStandard
_TrpzInfoRFDetectClientModulation_Object=MibTableColumn
trpzInfoRFDetectClientModulation=_TrpzInfoRFDetectClientModulation_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,6),_TrpzInfoRFDetectClientModulation_Type())
trpzInfoRFDetectClientModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientModulation.setStatus(_A)
_TrpzInfoRFDetectClientChannelNum_Type=TrpzChannelNum
_TrpzInfoRFDetectClientChannelNum_Object=MibTableColumn
trpzInfoRFDetectClientChannelNum=_TrpzInfoRFDetectClientChannelNum_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,7),_TrpzInfoRFDetectClientChannelNum_Type())
trpzInfoRFDetectClientChannelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientChannelNum.setStatus(_A)
_TrpzInfoRFDetectClientRate_Type=TrpzRadioRateEx
_TrpzInfoRFDetectClientRate_Object=MibTableColumn
trpzInfoRFDetectClientRate=_TrpzInfoRFDetectClientRate_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,8),_TrpzInfoRFDetectClientRate_Type())
trpzInfoRFDetectClientRate.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientRate.setStatus(_A)
_TrpzInfoRFDetectClientRssi_Type=TrpzRssi
_TrpzInfoRFDetectClientRssi_Object=MibTableColumn
trpzInfoRFDetectClientRssi=_TrpzInfoRFDetectClientRssi_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,9),_TrpzInfoRFDetectClientRssi_Type())
trpzInfoRFDetectClientRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientRssi.setStatus(_A)
_TrpzInfoRFDetectClientClassification_Type=TrpzRFDetectClassification
_TrpzInfoRFDetectClientClassification_Object=MibTableColumn
trpzInfoRFDetectClientClassification=_TrpzInfoRFDetectClientClassification_Object((1,3,6,1,4,1,14525,4,9,1,1,3,1,10),_TrpzInfoRFDetectClientClassification_Type())
trpzInfoRFDetectClientClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzInfoRFDetectClientClassification.setStatus(_A)
_TrpzInfoRFDetectConformance_ObjectIdentity=ObjectIdentity
trpzInfoRFDetectConformance=_TrpzInfoRFDetectConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,9,1,2))
_TrpzInfoRFDetectCompliances_ObjectIdentity=ObjectIdentity
trpzInfoRFDetectCompliances=_TrpzInfoRFDetectCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,9,1,2,1))
_TrpzInfoRFDetectGroups_ObjectIdentity=ObjectIdentity
trpzInfoRFDetectGroups=_TrpzInfoRFDetectGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,9,1,2,2))
trpzInfoRFDetectXmtrGroup=ObjectGroup((1,3,6,1,4,1,14525,4,9,1,2,2,1))
trpzInfoRFDetectXmtrGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrGroup.setStatus(_A)
trpzInfoRFDetectXmtrClassificationGroup=ObjectGroup((1,3,6,1,4,1,14525,4,9,1,2,2,2))
trpzInfoRFDetectXmtrClassificationGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:trpzInfoRFDetectXmtrClassificationGroup.setStatus(_A)
trpzInfoRFDetectCurrentXmtrTableSizeGroup=ObjectGroup((1,3,6,1,4,1,14525,4,9,1,2,2,3))
trpzInfoRFDetectCurrentXmtrTableSizeGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:trpzInfoRFDetectCurrentXmtrTableSizeGroup.setStatus(_A)
trpzInfoRFDetectClientGroup=ObjectGroup((1,3,6,1,4,1,14525,4,9,1,2,2,4))
trpzInfoRFDetectClientGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:trpzInfoRFDetectClientGroup.setStatus(_A)
trpzInfoRFDetectCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,9,1,2,1,1))
trpzInfoRFDetectCompliance.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:trpzInfoRFDetectCompliance.setStatus('obsolete')
trpzInfoRFDetectComplianceRev2=ModuleCompliance((1,3,6,1,4,1,14525,4,9,1,2,1,2))
trpzInfoRFDetectComplianceRev2.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_b)))
if mibBuilder.loadTexts:trpzInfoRFDetectComplianceRev2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'trpzInfoRFDetectMib':trpzInfoRFDetectMib,'trpzInfoRFDetectObjects':trpzInfoRFDetectObjects,'trpzInfoRFDetectDataObjects':trpzInfoRFDetectDataObjects,'trpzInfoRFDetectXmtrTable':trpzInfoRFDetectXmtrTable,'trpzInfoRFDetectXmtrEntry':trpzInfoRFDetectXmtrEntry,_I:trpzInfoRFDetectXmtrTransmitterMacAddress,_J:trpzInfoRFDetectXmtrListenerMacAddress,_K:trpzInfoRFDetectXmtrChannelNum,_N:trpzInfoRFDetectXmtrRssi,_O:trpzInfoRFDetectXmtrSsid,_P:trpzInfoRFDetectXmtrNetworkingMode,_Q:trpzInfoRFDetectXmtrClassification,_R:trpzInfoRFDetectXmtrClassificationReason,_S:trpzInfoRFDetectCurrentXmtrTableSize,'trpzInfoRFDetectClientTable':trpzInfoRFDetectClientTable,'trpzInfoRFDetectClientEntry':trpzInfoRFDetectClientEntry,_L:trpzInfoRFDetectClientMacAddress,_M:trpzInfoRFDetectClientListenerMacAddress,_T:trpzInfoRFDetectClientConnectedBssid,_U:trpzInfoRFDetectClientApNum,_V:trpzInfoRFDetectClientApRadioIndex,_W:trpzInfoRFDetectClientModulation,_X:trpzInfoRFDetectClientChannelNum,_Y:trpzInfoRFDetectClientRate,_Z:trpzInfoRFDetectClientRssi,_a:trpzInfoRFDetectClientClassification,'trpzInfoRFDetectConformance':trpzInfoRFDetectConformance,'trpzInfoRFDetectCompliances':trpzInfoRFDetectCompliances,'trpzInfoRFDetectCompliance':trpzInfoRFDetectCompliance,'trpzInfoRFDetectComplianceRev2':trpzInfoRFDetectComplianceRev2,'trpzInfoRFDetectGroups':trpzInfoRFDetectGroups,_E:trpzInfoRFDetectXmtrGroup,_F:trpzInfoRFDetectXmtrClassificationGroup,_G:trpzInfoRFDetectCurrentXmtrTableSizeGroup,_b:trpzInfoRFDetectClientGroup})