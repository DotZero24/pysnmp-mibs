_Q='rbtwsInfoRFDetectCurrentXmtrTableSizeGroup'
_P='rbtwsInfoRFDetectXmtrClassificationGroup'
_O='rbtwsInfoRFDetectXmtrGroup'
_N='rbtwsInfoRFDetectCurrentXmtrTableSize'
_M='rbtwsInfoRFDetectXmtrClassificationReason'
_L='rbtwsInfoRFDetectXmtrClassification'
_K='rbtwsInfoRFDetectXmtrNetworkingMode'
_J='rbtwsInfoRFDetectXmtrSsid'
_I='rbtwsInfoRFDetectXmtrRssi'
_H='rbtwsInfoRFDetectXmtrChannelNum'
_G='rbtwsInfoRFDetectXmtrListenerMacAddress'
_F='rbtwsInfoRFDetectXmtrTransmitterMacAddress'
_E='DisplayString'
_D='not-accessible'
_C='read-only'
_B='RBTWS-INFO-RF-DETECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
RbtwsChannelNum,RbtwsRssi=mibBuilder.importSymbols('RBTWS-AP-TC','RbtwsChannelNum','RbtwsRssi')
RbtwsRFDetectClassification,RbtwsRFDetectClassificationReason,RbtwsRFDetectNetworkingMode=mibBuilder.importSymbols('RBTWS-RF-DETECT-TC','RbtwsRFDetectClassification','RbtwsRFDetectClassificationReason','RbtwsRFDetectNetworkingMode')
rbtwsMibs,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention')
rbtwsInfoRFDetectMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,4,9))
if mibBuilder.loadTexts:rbtwsInfoRFDetectMib.setRevisions(('2007-06-27 00:11','2007-04-18 00:10','2006-10-11 00:03'))
_RbtwsInfoRFDetectObjects_ObjectIdentity=ObjectIdentity
rbtwsInfoRFDetectObjects=_RbtwsInfoRFDetectObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,9,1))
_RbtwsInfoRFDetectDataObjects_ObjectIdentity=ObjectIdentity
rbtwsInfoRFDetectDataObjects=_RbtwsInfoRFDetectDataObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,9,1,1))
_RbtwsInfoRFDetectXmtrTable_Object=MibTable
rbtwsInfoRFDetectXmtrTable=_RbtwsInfoRFDetectXmtrTable_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1))
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrTable.setStatus(_A)
_RbtwsInfoRFDetectXmtrEntry_Object=MibTableRow
rbtwsInfoRFDetectXmtrEntry=_RbtwsInfoRFDetectXmtrEntry_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1))
rbtwsInfoRFDetectXmtrEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrEntry.setStatus(_A)
_RbtwsInfoRFDetectXmtrTransmitterMacAddress_Type=MacAddress
_RbtwsInfoRFDetectXmtrTransmitterMacAddress_Object=MibTableColumn
rbtwsInfoRFDetectXmtrTransmitterMacAddress=_RbtwsInfoRFDetectXmtrTransmitterMacAddress_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,1),_RbtwsInfoRFDetectXmtrTransmitterMacAddress_Type())
rbtwsInfoRFDetectXmtrTransmitterMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrTransmitterMacAddress.setStatus(_A)
_RbtwsInfoRFDetectXmtrListenerMacAddress_Type=MacAddress
_RbtwsInfoRFDetectXmtrListenerMacAddress_Object=MibTableColumn
rbtwsInfoRFDetectXmtrListenerMacAddress=_RbtwsInfoRFDetectXmtrListenerMacAddress_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,2),_RbtwsInfoRFDetectXmtrListenerMacAddress_Type())
rbtwsInfoRFDetectXmtrListenerMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrListenerMacAddress.setStatus(_A)
_RbtwsInfoRFDetectXmtrChannelNum_Type=RbtwsChannelNum
_RbtwsInfoRFDetectXmtrChannelNum_Object=MibTableColumn
rbtwsInfoRFDetectXmtrChannelNum=_RbtwsInfoRFDetectXmtrChannelNum_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,3),_RbtwsInfoRFDetectXmtrChannelNum_Type())
rbtwsInfoRFDetectXmtrChannelNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrChannelNum.setStatus(_A)
_RbtwsInfoRFDetectXmtrRssi_Type=RbtwsRssi
_RbtwsInfoRFDetectXmtrRssi_Object=MibTableColumn
rbtwsInfoRFDetectXmtrRssi=_RbtwsInfoRFDetectXmtrRssi_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,4),_RbtwsInfoRFDetectXmtrRssi_Type())
rbtwsInfoRFDetectXmtrRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrRssi.setStatus(_A)
class _RbtwsInfoRFDetectXmtrSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbtwsInfoRFDetectXmtrSsid_Type.__name__=_E
_RbtwsInfoRFDetectXmtrSsid_Object=MibTableColumn
rbtwsInfoRFDetectXmtrSsid=_RbtwsInfoRFDetectXmtrSsid_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,5),_RbtwsInfoRFDetectXmtrSsid_Type())
rbtwsInfoRFDetectXmtrSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrSsid.setStatus(_A)
_RbtwsInfoRFDetectXmtrNetworkingMode_Type=RbtwsRFDetectNetworkingMode
_RbtwsInfoRFDetectXmtrNetworkingMode_Object=MibTableColumn
rbtwsInfoRFDetectXmtrNetworkingMode=_RbtwsInfoRFDetectXmtrNetworkingMode_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,6),_RbtwsInfoRFDetectXmtrNetworkingMode_Type())
rbtwsInfoRFDetectXmtrNetworkingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrNetworkingMode.setStatus(_A)
_RbtwsInfoRFDetectXmtrClassification_Type=RbtwsRFDetectClassification
_RbtwsInfoRFDetectXmtrClassification_Object=MibTableColumn
rbtwsInfoRFDetectXmtrClassification=_RbtwsInfoRFDetectXmtrClassification_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,7),_RbtwsInfoRFDetectXmtrClassification_Type())
rbtwsInfoRFDetectXmtrClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrClassification.setStatus(_A)
_RbtwsInfoRFDetectXmtrClassificationReason_Type=RbtwsRFDetectClassificationReason
_RbtwsInfoRFDetectXmtrClassificationReason_Object=MibTableColumn
rbtwsInfoRFDetectXmtrClassificationReason=_RbtwsInfoRFDetectXmtrClassificationReason_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,1,1,8),_RbtwsInfoRFDetectXmtrClassificationReason_Type())
rbtwsInfoRFDetectXmtrClassificationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrClassificationReason.setStatus(_A)
_RbtwsInfoRFDetectCurrentXmtrTableSize_Type=Gauge32
_RbtwsInfoRFDetectCurrentXmtrTableSize_Object=MibScalar
rbtwsInfoRFDetectCurrentXmtrTableSize=_RbtwsInfoRFDetectCurrentXmtrTableSize_Object((1,3,6,1,4,1,52,4,15,1,4,9,1,1,2),_RbtwsInfoRFDetectCurrentXmtrTableSize_Type())
rbtwsInfoRFDetectCurrentXmtrTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsInfoRFDetectCurrentXmtrTableSize.setStatus(_A)
_RbtwsInfoRFDetectConformance_ObjectIdentity=ObjectIdentity
rbtwsInfoRFDetectConformance=_RbtwsInfoRFDetectConformance_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,9,1,2))
_RbtwsInfoRFDetectCompliances_ObjectIdentity=ObjectIdentity
rbtwsInfoRFDetectCompliances=_RbtwsInfoRFDetectCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,9,1,2,1))
_RbtwsInfoRFDetectGroups_ObjectIdentity=ObjectIdentity
rbtwsInfoRFDetectGroups=_RbtwsInfoRFDetectGroups_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,9,1,2,2))
rbtwsInfoRFDetectXmtrGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,9,1,2,2,1))
rbtwsInfoRFDetectXmtrGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrGroup.setStatus(_A)
rbtwsInfoRFDetectXmtrClassificationGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,9,1,2,2,2))
rbtwsInfoRFDetectXmtrClassificationGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:rbtwsInfoRFDetectXmtrClassificationGroup.setStatus(_A)
rbtwsInfoRFDetectCurrentXmtrTableSizeGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,9,1,2,2,3))
rbtwsInfoRFDetectCurrentXmtrTableSizeGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:rbtwsInfoRFDetectCurrentXmtrTableSizeGroup.setStatus(_A)
rbtwsInfoRFDetectCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,15,1,4,9,1,2,1,1))
rbtwsInfoRFDetectCompliance.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:rbtwsInfoRFDetectCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbtwsInfoRFDetectMib':rbtwsInfoRFDetectMib,'rbtwsInfoRFDetectObjects':rbtwsInfoRFDetectObjects,'rbtwsInfoRFDetectDataObjects':rbtwsInfoRFDetectDataObjects,'rbtwsInfoRFDetectXmtrTable':rbtwsInfoRFDetectXmtrTable,'rbtwsInfoRFDetectXmtrEntry':rbtwsInfoRFDetectXmtrEntry,_F:rbtwsInfoRFDetectXmtrTransmitterMacAddress,_G:rbtwsInfoRFDetectXmtrListenerMacAddress,_H:rbtwsInfoRFDetectXmtrChannelNum,_I:rbtwsInfoRFDetectXmtrRssi,_J:rbtwsInfoRFDetectXmtrSsid,_K:rbtwsInfoRFDetectXmtrNetworkingMode,_L:rbtwsInfoRFDetectXmtrClassification,_M:rbtwsInfoRFDetectXmtrClassificationReason,_N:rbtwsInfoRFDetectCurrentXmtrTableSize,'rbtwsInfoRFDetectConformance':rbtwsInfoRFDetectConformance,'rbtwsInfoRFDetectCompliances':rbtwsInfoRFDetectCompliances,'rbtwsInfoRFDetectCompliance':rbtwsInfoRFDetectCompliance,'rbtwsInfoRFDetectGroups':rbtwsInfoRFDetectGroups,_O:rbtwsInfoRFDetectXmtrGroup,_P:rbtwsInfoRFDetectXmtrClassificationGroup,_Q:rbtwsInfoRFDetectCurrentXmtrTableSizeGroup})