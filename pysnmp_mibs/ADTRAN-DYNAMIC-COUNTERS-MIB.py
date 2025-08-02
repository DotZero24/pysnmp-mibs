_R='multicast'
_Q='unicast'
_P='not-accessible'
_O='adGenDCProfileIndex'
_N='read-write'
_M='exclude'
_L='include'
_K='adGenDCConfigIndex'
_J='none'
_I='any'
_H='ADTRAN-DYNAMIC-COUNTERS-MIB'
_G='adGenSlotInfoIndex'
_F='ADTRAN-GENSLOT-MIB'
_E='noMatching'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_F,_G)
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
adGenDynamicCounter,adGenDynamicCounterID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenDynamicCounter','adGenDynamicCounterID')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
adGenDynamicCounterMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,53,1))
if mibBuilder.loadTexts:adGenDynamicCounterMIB.setRevisions(('2014-07-31 00:00','2014-06-05 00:00','2013-02-11 00:00'))
_AdGenDynamicCounterTables_ObjectIdentity=ObjectIdentity
adGenDynamicCounterTables=_AdGenDynamicCounterTables_ObjectIdentity((1,3,6,1,4,1,664,5,70,53,1))
_AdGenDCSlotTable_Object=MibTable
adGenDCSlotTable=_AdGenDCSlotTable_Object((1,3,6,1,4,1,664,5,70,53,1,1))
if mibBuilder.loadTexts:adGenDCSlotTable.setStatus(_A)
_AdGenDCSlotEntry_Object=MibTableRow
adGenDCSlotEntry=_AdGenDCSlotEntry_Object((1,3,6,1,4,1,664,5,70,53,1,1,1))
adGenDCSlotEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenDCSlotEntry.setStatus(_A)
class _AdGenDCSlotSupport_Type(Bits):namedValues=NamedValues(*(('color',0),('pBit',1),('sTag',2),('destMacByType',3),('destMac',4),('destIpByType',5),('destIp',6),('srcMacByType',7),('srcMac',8),('srcIpByType',9),('srcIp',10),('ipAndMac',11),('destAndSrc',12),('tx',13),('rx',14),('queue',15),(_L,16),(_M,17)))
_AdGenDCSlotSupport_Type.__name__='Bits'
_AdGenDCSlotSupport_Object=MibTableColumn
adGenDCSlotSupport=_AdGenDCSlotSupport_Object((1,3,6,1,4,1,664,5,70,53,1,1,1,1),_AdGenDCSlotSupport_Type())
adGenDCSlotSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCSlotSupport.setStatus(_A)
_AdGenDCSlotMaxDCProfileIndex_Type=Integer32
_AdGenDCSlotMaxDCProfileIndex_Object=MibTableColumn
adGenDCSlotMaxDCProfileIndex=_AdGenDCSlotMaxDCProfileIndex_Object((1,3,6,1,4,1,664,5,70,53,1,1,1,2),_AdGenDCSlotMaxDCProfileIndex_Type())
adGenDCSlotMaxDCProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCSlotMaxDCProfileIndex.setStatus(_A)
_AdGenDCSlotNextDCProfileIndex_Type=Integer32
_AdGenDCSlotNextDCProfileIndex_Object=MibTableColumn
adGenDCSlotNextDCProfileIndex=_AdGenDCSlotNextDCProfileIndex_Object((1,3,6,1,4,1,664,5,70,53,1,1,1,3),_AdGenDCSlotNextDCProfileIndex_Type())
adGenDCSlotNextDCProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCSlotNextDCProfileIndex.setStatus(_A)
_AdGenDCSlotMaxDCIndex_Type=Integer32
_AdGenDCSlotMaxDCIndex_Object=MibTableColumn
adGenDCSlotMaxDCIndex=_AdGenDCSlotMaxDCIndex_Object((1,3,6,1,4,1,664,5,70,53,1,1,1,4),_AdGenDCSlotMaxDCIndex_Type())
adGenDCSlotMaxDCIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCSlotMaxDCIndex.setStatus(_A)
_AdGenDCSlotNextDCIndex_Type=Integer32
_AdGenDCSlotNextDCIndex_Object=MibTableColumn
adGenDCSlotNextDCIndex=_AdGenDCSlotNextDCIndex_Object((1,3,6,1,4,1,664,5,70,53,1,1,1,5),_AdGenDCSlotNextDCIndex_Type())
adGenDCSlotNextDCIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCSlotNextDCIndex.setStatus(_A)
class _AdGenDCSlotClearAllDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clearAll',1),('idle',2)))
_AdGenDCSlotClearAllDC_Type.__name__=_C
_AdGenDCSlotClearAllDC_Object=MibTableColumn
adGenDCSlotClearAllDC=_AdGenDCSlotClearAllDC_Object((1,3,6,1,4,1,664,5,70,53,1,1,1,6),_AdGenDCSlotClearAllDC_Type())
adGenDCSlotClearAllDC.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenDCSlotClearAllDC.setStatus(_A)
_AdGenDCSlotLastError_Type=DisplayString
_AdGenDCSlotLastError_Object=MibTableColumn
adGenDCSlotLastError=_AdGenDCSlotLastError_Object((1,3,6,1,4,1,664,5,70,53,1,1,1,7),_AdGenDCSlotLastError_Type())
adGenDCSlotLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCSlotLastError.setStatus(_A)
_AdGenDCProfileTable_Object=MibTable
adGenDCProfileTable=_AdGenDCProfileTable_Object((1,3,6,1,4,1,664,5,70,53,1,2))
if mibBuilder.loadTexts:adGenDCProfileTable.setStatus(_A)
_AdGenDCProfileEntry_Object=MibTableRow
adGenDCProfileEntry=_AdGenDCProfileEntry_Object((1,3,6,1,4,1,664,5,70,53,1,2,1))
adGenDCProfileEntry.setIndexNames((0,_F,_G),(0,_H,_O))
if mibBuilder.loadTexts:adGenDCProfileEntry.setStatus(_A)
_AdGenDCProfileIndex_Type=Integer32
_AdGenDCProfileIndex_Object=MibTableColumn
adGenDCProfileIndex=_AdGenDCProfileIndex_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,1),_AdGenDCProfileIndex_Type())
adGenDCProfileIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:adGenDCProfileIndex.setStatus(_A)
_AdGenDCProfileRowStatus_Type=RowStatus
_AdGenDCProfileRowStatus_Object=MibTableColumn
adGenDCProfileRowStatus=_AdGenDCProfileRowStatus_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,2),_AdGenDCProfileRowStatus_Type())
adGenDCProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileRowStatus.setStatus(_A)
class _AdGenDCProfileColorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('green',2),('yellow',3),('red',4)))
_AdGenDCProfileColorType_Type.__name__=_C
_AdGenDCProfileColorType_Object=MibTableColumn
adGenDCProfileColorType=_AdGenDCProfileColorType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,3),_AdGenDCProfileColorType_Type())
adGenDCProfileColorType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileColorType.setStatus(_A)
class _AdGenDCProfilePBitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('pBit',2)))
_AdGenDCProfilePBitType_Type.__name__=_C
_AdGenDCProfilePBitType_Object=MibTableColumn
adGenDCProfilePBitType=_AdGenDCProfilePBitType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,4),_AdGenDCProfilePBitType_Type())
adGenDCProfilePBitType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfilePBitType.setStatus(_A)
class _AdGenDCProfilePBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenDCProfilePBit_Type.__name__=_C
_AdGenDCProfilePBit_Object=MibTableColumn
adGenDCProfilePBit=_AdGenDCProfilePBit_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,5),_AdGenDCProfilePBit_Type())
adGenDCProfilePBit.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfilePBit.setStatus(_A)
class _AdGenDCProfileSTagType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('sTag',2),('allSTags',3),('noSTag',4)))
_AdGenDCProfileSTagType_Type.__name__=_C
_AdGenDCProfileSTagType_Object=MibTableColumn
adGenDCProfileSTagType=_AdGenDCProfileSTagType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,6),_AdGenDCProfileSTagType_Type())
adGenDCProfileSTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileSTagType.setStatus(_A)
class _AdGenDCProfileSTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AdGenDCProfileSTag_Type.__name__=_C
_AdGenDCProfileSTag_Object=MibTableColumn
adGenDCProfileSTag=_AdGenDCProfileSTag_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,7),_AdGenDCProfileSTag_Type())
adGenDCProfileSTag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileSTag.setStatus(_A)
class _AdGenDCProfileDestMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('mac',2),(_Q,3),(_R,4),('broadcast',5)))
_AdGenDCProfileDestMacType_Type.__name__=_C
_AdGenDCProfileDestMacType_Object=MibTableColumn
adGenDCProfileDestMacType=_AdGenDCProfileDestMacType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,8),_AdGenDCProfileDestMacType_Type())
adGenDCProfileDestMacType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileDestMacType.setStatus(_A)
_AdGenDCProfileDestMacAddress_Type=PhysAddress
_AdGenDCProfileDestMacAddress_Object=MibTableColumn
adGenDCProfileDestMacAddress=_AdGenDCProfileDestMacAddress_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,9),_AdGenDCProfileDestMacAddress_Type())
adGenDCProfileDestMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileDestMacAddress.setStatus(_A)
class _AdGenDCProfileDestIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('ip',2),(_Q,3),(_R,4),(_I,5),(_J,6)))
_AdGenDCProfileDestIpType_Type.__name__=_C
_AdGenDCProfileDestIpType_Object=MibTableColumn
adGenDCProfileDestIpType=_AdGenDCProfileDestIpType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,10),_AdGenDCProfileDestIpType_Type())
adGenDCProfileDestIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileDestIpType.setStatus(_A)
_AdGenDCProfileDestIpAddress_Type=IpAddress
_AdGenDCProfileDestIpAddress_Object=MibTableColumn
adGenDCProfileDestIpAddress=_AdGenDCProfileDestIpAddress_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,11),_AdGenDCProfileDestIpAddress_Type())
adGenDCProfileDestIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileDestIpAddress.setStatus(_A)
class _AdGenDCProfileSrcMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('mac',2)))
_AdGenDCProfileSrcMacType_Type.__name__=_C
_AdGenDCProfileSrcMacType_Object=MibTableColumn
adGenDCProfileSrcMacType=_AdGenDCProfileSrcMacType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,12),_AdGenDCProfileSrcMacType_Type())
adGenDCProfileSrcMacType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileSrcMacType.setStatus(_A)
_AdGenDCProfileSrcMacAddress_Type=PhysAddress
_AdGenDCProfileSrcMacAddress_Object=MibTableColumn
adGenDCProfileSrcMacAddress=_AdGenDCProfileSrcMacAddress_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,13),_AdGenDCProfileSrcMacAddress_Type())
adGenDCProfileSrcMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileSrcMacAddress.setStatus(_A)
class _AdGenDCProfileSrcIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('ip',2),(_I,3),(_J,4)))
_AdGenDCProfileSrcIpType_Type.__name__=_C
_AdGenDCProfileSrcIpType_Object=MibTableColumn
adGenDCProfileSrcIpType=_AdGenDCProfileSrcIpType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,14),_AdGenDCProfileSrcIpType_Type())
adGenDCProfileSrcIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileSrcIpType.setStatus(_A)
_AdGenDCProfileSrcIpAddress_Type=IpAddress
_AdGenDCProfileSrcIpAddress_Object=MibTableColumn
adGenDCProfileSrcIpAddress=_AdGenDCProfileSrcIpAddress_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,15),_AdGenDCProfileSrcIpAddress_Type())
adGenDCProfileSrcIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileSrcIpAddress.setStatus(_A)
_AdGenDCProfileLastError_Type=DisplayString
_AdGenDCProfileLastError_Object=MibTableColumn
adGenDCProfileLastError=_AdGenDCProfileLastError_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,16),_AdGenDCProfileLastError_Type())
adGenDCProfileLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCProfileLastError.setStatus(_A)
class _AdGenDCProfileEgressQueueType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('egressQueue',2)))
_AdGenDCProfileEgressQueueType_Type.__name__=_C
_AdGenDCProfileEgressQueueType_Object=MibTableColumn
adGenDCProfileEgressQueueType=_AdGenDCProfileEgressQueueType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,17),_AdGenDCProfileEgressQueueType_Type())
adGenDCProfileEgressQueueType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileEgressQueueType.setStatus(_A)
class _AdGenDCProfileEgressQueue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenDCProfileEgressQueue_Type.__name__=_C
_AdGenDCProfileEgressQueue_Object=MibTableColumn
adGenDCProfileEgressQueue=_AdGenDCProfileEgressQueue_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,18),_AdGenDCProfileEgressQueue_Type())
adGenDCProfileEgressQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileEgressQueue.setStatus(_A)
class _AdGenDCProfileCtagVlanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('cTag',2),('allCTags',3),('noCTag',4)))
_AdGenDCProfileCtagVlanType_Type.__name__=_C
_AdGenDCProfileCtagVlanType_Object=MibTableColumn
adGenDCProfileCtagVlanType=_AdGenDCProfileCtagVlanType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,19),_AdGenDCProfileCtagVlanType_Type())
adGenDCProfileCtagVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileCtagVlanType.setStatus(_A)
class _AdGenDCProfileCtagVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AdGenDCProfileCtagVlan_Type.__name__=_C
_AdGenDCProfileCtagVlan_Object=MibTableColumn
adGenDCProfileCtagVlan=_AdGenDCProfileCtagVlan_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,20),_AdGenDCProfileCtagVlan_Type())
adGenDCProfileCtagVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileCtagVlan.setStatus(_A)
class _AdGenDCProfileCtagPriType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('cTagPri',2)))
_AdGenDCProfileCtagPriType_Type.__name__=_C
_AdGenDCProfileCtagPriType_Object=MibTableColumn
adGenDCProfileCtagPriType=_AdGenDCProfileCtagPriType_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,21),_AdGenDCProfileCtagPriType_Type())
adGenDCProfileCtagPriType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileCtagPriType.setStatus(_A)
class _AdGenDCProfileCtagPri_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenDCProfileCtagPri_Type.__name__=_C
_AdGenDCProfileCtagPri_Object=MibTableColumn
adGenDCProfileCtagPri=_AdGenDCProfileCtagPri_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,22),_AdGenDCProfileCtagPri_Type())
adGenDCProfileCtagPri.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileCtagPri.setStatus(_A)
_AdGenDCProfileEvcMap_Type=DisplayString
_AdGenDCProfileEvcMap_Object=MibTableColumn
adGenDCProfileEvcMap=_AdGenDCProfileEvcMap_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,23),_AdGenDCProfileEvcMap_Type())
adGenDCProfileEvcMap.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileEvcMap.setStatus(_A)
class _AdGenDCProfileDiscardReason_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),(_I,2),('stagMatchFailed',3),('egressRecDrop',4),('forwardingFailed',5),('fullQueue',6),('invalidQueueDrop',7),('lagNotValid',8),('multicastBufferFull',9),('macsaMatchFailed',10),(_J,11)))
_AdGenDCProfileDiscardReason_Type.__name__=_C
_AdGenDCProfileDiscardReason_Object=MibTableColumn
adGenDCProfileDiscardReason=_AdGenDCProfileDiscardReason_Object((1,3,6,1,4,1,664,5,70,53,1,2,1,24),_AdGenDCProfileDiscardReason_Type())
adGenDCProfileDiscardReason.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCProfileDiscardReason.setStatus(_A)
_AdGenDCConfigTable_Object=MibTable
adGenDCConfigTable=_AdGenDCConfigTable_Object((1,3,6,1,4,1,664,5,70,53,1,3))
if mibBuilder.loadTexts:adGenDCConfigTable.setStatus(_A)
_AdGenDCConfigEntry_Object=MibTableRow
adGenDCConfigEntry=_AdGenDCConfigEntry_Object((1,3,6,1,4,1,664,5,70,53,1,3,1))
adGenDCConfigEntry.setIndexNames((0,_F,_G),(0,_H,_K))
if mibBuilder.loadTexts:adGenDCConfigEntry.setStatus(_A)
_AdGenDCConfigIndex_Type=Integer32
_AdGenDCConfigIndex_Object=MibTableColumn
adGenDCConfigIndex=_AdGenDCConfigIndex_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,1),_AdGenDCConfigIndex_Type())
adGenDCConfigIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:adGenDCConfigIndex.setStatus(_A)
_AdGenDCConfigRowStatus_Type=RowStatus
_AdGenDCConfigRowStatus_Object=MibTableColumn
adGenDCConfigRowStatus=_AdGenDCConfigRowStatus_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,2),_AdGenDCConfigRowStatus_Type())
adGenDCConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCConfigRowStatus.setStatus(_A)
_AdGenDCConfigProfile_Type=Integer32
_AdGenDCConfigProfile_Object=MibTableColumn
adGenDCConfigProfile=_AdGenDCConfigProfile_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,3),_AdGenDCConfigProfile_Type())
adGenDCConfigProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCConfigProfile.setStatus(_A)
_AdGenDCConfigInterface_Type=InterfaceIndexOrZero
_AdGenDCConfigInterface_Object=MibTableColumn
adGenDCConfigInterface=_AdGenDCConfigInterface_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,4),_AdGenDCConfigInterface_Type())
adGenDCConfigInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCConfigInterface.setStatus(_A)
class _AdGenDCConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tx',1),('rx',2),('queue',3)))
_AdGenDCConfigType_Type.__name__=_C
_AdGenDCConfigType_Object=MibTableColumn
adGenDCConfigType=_AdGenDCConfigType_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,5),_AdGenDCConfigType_Type())
adGenDCConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCConfigType.setStatus(_A)
_AdGenDCConfigInterfaceQueue_Type=Integer32
_AdGenDCConfigInterfaceQueue_Object=MibTableColumn
adGenDCConfigInterfaceQueue=_AdGenDCConfigInterfaceQueue_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,6),_AdGenDCConfigInterfaceQueue_Type())
adGenDCConfigInterfaceQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCConfigInterfaceQueue.setStatus(_A)
class _AdGenDCConfigInclude_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AdGenDCConfigInclude_Type.__name__=_C
_AdGenDCConfigInclude_Object=MibTableColumn
adGenDCConfigInclude=_AdGenDCConfigInclude_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,7),_AdGenDCConfigInclude_Type())
adGenDCConfigInclude.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDCConfigInclude.setStatus(_A)
_AdGenDCConfigLastError_Type=DisplayString
_AdGenDCConfigLastError_Object=MibTableColumn
adGenDCConfigLastError=_AdGenDCConfigLastError_Object((1,3,6,1,4,1,664,5,70,53,1,3,1,8),_AdGenDCConfigLastError_Type())
adGenDCConfigLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCConfigLastError.setStatus(_A)
_AdGenDCStatusTable_Object=MibTable
adGenDCStatusTable=_AdGenDCStatusTable_Object((1,3,6,1,4,1,664,5,70,53,1,4))
if mibBuilder.loadTexts:adGenDCStatusTable.setStatus(_A)
_AdGenDCStatusEntry_Object=MibTableRow
adGenDCStatusEntry=_AdGenDCStatusEntry_Object((1,3,6,1,4,1,664,5,70,53,1,4,1))
adGenDCStatusEntry.setIndexNames((0,_F,_G),(0,_H,_K))
if mibBuilder.loadTexts:adGenDCStatusEntry.setStatus(_A)
_AdGenDCStatusRowStatus_Type=RowStatus
_AdGenDCStatusRowStatus_Object=MibTableColumn
adGenDCStatusRowStatus=_AdGenDCStatusRowStatus_Object((1,3,6,1,4,1,664,5,70,53,1,4,1,1),_AdGenDCStatusRowStatus_Type())
adGenDCStatusRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCStatusRowStatus.setStatus(_A)
_AdGenDCStatusOctets_Type=Counter64
_AdGenDCStatusOctets_Object=MibTableColumn
adGenDCStatusOctets=_AdGenDCStatusOctets_Object((1,3,6,1,4,1,664,5,70,53,1,4,1,2),_AdGenDCStatusOctets_Type())
adGenDCStatusOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCStatusOctets.setStatus(_A)
_AdGenDCStatusPkts_Type=Counter64
_AdGenDCStatusPkts_Object=MibTableColumn
adGenDCStatusPkts=_AdGenDCStatusPkts_Object((1,3,6,1,4,1,664,5,70,53,1,4,1,3),_AdGenDCStatusPkts_Type())
adGenDCStatusPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCStatusPkts.setStatus(_A)
_AdGenDCStatusAvgBitsPerSec_Type=Gauge32
_AdGenDCStatusAvgBitsPerSec_Object=MibTableColumn
adGenDCStatusAvgBitsPerSec=_AdGenDCStatusAvgBitsPerSec_Object((1,3,6,1,4,1,664,5,70,53,1,4,1,4),_AdGenDCStatusAvgBitsPerSec_Type())
adGenDCStatusAvgBitsPerSec.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDCStatusAvgBitsPerSec.setStatus(_A)
class _AdGenDCStatusClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('idle',2)))
_AdGenDCStatusClear_Type.__name__=_C
_AdGenDCStatusClear_Object=MibTableColumn
adGenDCStatusClear=_AdGenDCStatusClear_Object((1,3,6,1,4,1,664,5,70,53,1,4,1,5),_AdGenDCStatusClear_Type())
adGenDCStatusClear.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenDCStatusClear.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'adGenDynamicCounterTables':adGenDynamicCounterTables,'adGenDCSlotTable':adGenDCSlotTable,'adGenDCSlotEntry':adGenDCSlotEntry,'adGenDCSlotSupport':adGenDCSlotSupport,'adGenDCSlotMaxDCProfileIndex':adGenDCSlotMaxDCProfileIndex,'adGenDCSlotNextDCProfileIndex':adGenDCSlotNextDCProfileIndex,'adGenDCSlotMaxDCIndex':adGenDCSlotMaxDCIndex,'adGenDCSlotNextDCIndex':adGenDCSlotNextDCIndex,'adGenDCSlotClearAllDC':adGenDCSlotClearAllDC,'adGenDCSlotLastError':adGenDCSlotLastError,'adGenDCProfileTable':adGenDCProfileTable,'adGenDCProfileEntry':adGenDCProfileEntry,_O:adGenDCProfileIndex,'adGenDCProfileRowStatus':adGenDCProfileRowStatus,'adGenDCProfileColorType':adGenDCProfileColorType,'adGenDCProfilePBitType':adGenDCProfilePBitType,'adGenDCProfilePBit':adGenDCProfilePBit,'adGenDCProfileSTagType':adGenDCProfileSTagType,'adGenDCProfileSTag':adGenDCProfileSTag,'adGenDCProfileDestMacType':adGenDCProfileDestMacType,'adGenDCProfileDestMacAddress':adGenDCProfileDestMacAddress,'adGenDCProfileDestIpType':adGenDCProfileDestIpType,'adGenDCProfileDestIpAddress':adGenDCProfileDestIpAddress,'adGenDCProfileSrcMacType':adGenDCProfileSrcMacType,'adGenDCProfileSrcMacAddress':adGenDCProfileSrcMacAddress,'adGenDCProfileSrcIpType':adGenDCProfileSrcIpType,'adGenDCProfileSrcIpAddress':adGenDCProfileSrcIpAddress,'adGenDCProfileLastError':adGenDCProfileLastError,'adGenDCProfileEgressQueueType':adGenDCProfileEgressQueueType,'adGenDCProfileEgressQueue':adGenDCProfileEgressQueue,'adGenDCProfileCtagVlanType':adGenDCProfileCtagVlanType,'adGenDCProfileCtagVlan':adGenDCProfileCtagVlan,'adGenDCProfileCtagPriType':adGenDCProfileCtagPriType,'adGenDCProfileCtagPri':adGenDCProfileCtagPri,'adGenDCProfileEvcMap':adGenDCProfileEvcMap,'adGenDCProfileDiscardReason':adGenDCProfileDiscardReason,'adGenDCConfigTable':adGenDCConfigTable,'adGenDCConfigEntry':adGenDCConfigEntry,_K:adGenDCConfigIndex,'adGenDCConfigRowStatus':adGenDCConfigRowStatus,'adGenDCConfigProfile':adGenDCConfigProfile,'adGenDCConfigInterface':adGenDCConfigInterface,'adGenDCConfigType':adGenDCConfigType,'adGenDCConfigInterfaceQueue':adGenDCConfigInterfaceQueue,'adGenDCConfigInclude':adGenDCConfigInclude,'adGenDCConfigLastError':adGenDCConfigLastError,'adGenDCStatusTable':adGenDCStatusTable,'adGenDCStatusEntry':adGenDCStatusEntry,'adGenDCStatusRowStatus':adGenDCStatusRowStatus,'adGenDCStatusOctets':adGenDCStatusOctets,'adGenDCStatusPkts':adGenDCStatusPkts,'adGenDCStatusAvgBitsPerSec':adGenDCStatusAvgBitsPerSec,'adGenDCStatusClear':adGenDCStatusClear,'adGenDynamicCounterMIB':adGenDynamicCounterMIB})