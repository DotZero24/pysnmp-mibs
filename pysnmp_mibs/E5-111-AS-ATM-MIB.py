_Q='asIpqosProfileQueueIndex'
_P='nrt-vbr'
_O='rt-vbr'
_N='asChannelProfileName'
_M='asIpqosProfileName'
_L='not-accessible'
_K='asChannelVci'
_J='asChannelVpi'
_I='ifIndex'
_H='IF-MIB'
_G='DisplayString'
_F='read-write'
_E='E5-111-AS-ATM-MIB'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
accessSwitchCommonATM,=mibBuilder.importSymbols('E5-111-MIB','accessSwitchCommonATM')
ifIndex,=mibBuilder.importSymbols(_H,_I)
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
_AsMaxNumOfChannels_Type=Integer32
_AsMaxNumOfChannels_Object=MibScalar
asMaxNumOfChannels=_AsMaxNumOfChannels_Object((1,3,6,1,4,1,6321,1,2,3,2,99,1),_AsMaxNumOfChannels_Type())
asMaxNumOfChannels.setMaxAccess(_D)
if mibBuilder.loadTexts:asMaxNumOfChannels.setStatus(_A)
_AsChannelTable_Object=MibTable
asChannelTable=_AsChannelTable_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2))
if mibBuilder.loadTexts:asChannelTable.setStatus(_A)
_AsChannelEntry_Object=MibTableRow
asChannelEntry=_AsChannelEntry_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2,1))
asChannelEntry.setIndexNames((0,_H,_I),(0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:asChannelEntry.setStatus(_A)
class _AsChannelVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AsChannelVpi_Type.__name__=_B
_AsChannelVpi_Object=MibTableColumn
asChannelVpi=_AsChannelVpi_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2,1,1),_AsChannelVpi_Type())
asChannelVpi.setMaxAccess(_L)
if mibBuilder.loadTexts:asChannelVpi.setStatus(_A)
class _AsChannelVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AsChannelVci_Type.__name__=_B
_AsChannelVci_Object=MibTableColumn
asChannelVci=_AsChannelVci_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2,1,2),_AsChannelVci_Type())
asChannelVci.setMaxAccess(_L)
if mibBuilder.loadTexts:asChannelVci.setStatus(_A)
_AsChannelPvid_Type=VlanIndex
_AsChannelPvid_Object=MibTableColumn
asChannelPvid=_AsChannelPvid_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2,1,3),_AsChannelPvid_Type())
asChannelPvid.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelPvid.setStatus(_A)
class _AsChannelPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AsChannelPriority_Type.__name__=_B
_AsChannelPriority_Object=MibTableColumn
asChannelPriority=_AsChannelPriority_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2,1,5),_AsChannelPriority_Type())
asChannelPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelPriority.setStatus(_A)
class _AsChannelProfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AsChannelProfile_Type.__name__=_G
_AsChannelProfile_Object=MibTableColumn
asChannelProfile=_AsChannelProfile_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2,1,6),_AsChannelProfile_Type())
asChannelProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfile.setStatus(_A)
_AsChannelRowStatus_Type=RowStatus
_AsChannelRowStatus_Object=MibTableColumn
asChannelRowStatus=_AsChannelRowStatus_Object((1,3,6,1,4,1,6321,1,2,3,2,99,2,1,7),_AsChannelRowStatus_Type())
asChannelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelRowStatus.setStatus(_A)
_AsMaxNumOfChannelProfiles_Type=Integer32
_AsMaxNumOfChannelProfiles_Object=MibScalar
asMaxNumOfChannelProfiles=_AsMaxNumOfChannelProfiles_Object((1,3,6,1,4,1,6321,1,2,3,2,99,3),_AsMaxNumOfChannelProfiles_Type())
asMaxNumOfChannelProfiles.setMaxAccess(_D)
if mibBuilder.loadTexts:asMaxNumOfChannelProfiles.setStatus(_A)
_AsChannelProfileTable_Object=MibTable
asChannelProfileTable=_AsChannelProfileTable_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6))
if mibBuilder.loadTexts:asChannelProfileTable.setStatus(_A)
_AsChannelProfileEntry_Object=MibTableRow
asChannelProfileEntry=_AsChannelProfileEntry_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1))
asChannelProfileEntry.setIndexNames((1,_E,_N))
if mibBuilder.loadTexts:asChannelProfileEntry.setStatus(_A)
class _AsChannelProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AsChannelProfileName_Type.__name__=_G
_AsChannelProfileName_Object=MibTableColumn
asChannelProfileName=_AsChannelProfileName_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,1),_AsChannelProfileName_Type())
asChannelProfileName.setMaxAccess(_L)
if mibBuilder.loadTexts:asChannelProfileName.setStatus(_A)
class _AsChannelProfileEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('llc',1),('vc',2)))
_AsChannelProfileEncap_Type.__name__=_B
_AsChannelProfileEncap_Object=MibTableColumn
asChannelProfileEncap=_AsChannelProfileEncap_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,2),_AsChannelProfileEncap_Type())
asChannelProfileEncap.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfileEncap.setStatus(_A)
class _AsChannelProfileAAL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AsChannelProfileAAL_Type.__name__=_B
_AsChannelProfileAAL_Object=MibTableColumn
asChannelProfileAAL=_AsChannelProfileAAL_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,3),_AsChannelProfileAAL_Type())
asChannelProfileAAL.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfileAAL.setStatus(_A)
class _AsChannelProfileClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('cbr',1),(_O,2),(_P,3),('ubr',4),('abr',5)))
_AsChannelProfileClass_Type.__name__=_B
_AsChannelProfileClass_Object=MibTableColumn
asChannelProfileClass=_AsChannelProfileClass_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,4),_AsChannelProfileClass_Type())
asChannelProfileClass.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfileClass.setStatus(_A)
_AsChannelProfilePcr_Type=Unsigned32
_AsChannelProfilePcr_Object=MibTableColumn
asChannelProfilePcr=_AsChannelProfilePcr_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,5),_AsChannelProfilePcr_Type())
asChannelProfilePcr.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfilePcr.setStatus(_A)
class _AsChannelProfileCdvt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AsChannelProfileCdvt_Type.__name__=_B
_AsChannelProfileCdvt_Object=MibTableColumn
asChannelProfileCdvt=_AsChannelProfileCdvt_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,6),_AsChannelProfileCdvt_Type())
asChannelProfileCdvt.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfileCdvt.setStatus(_A)
_AsChannelProfileScrMcr_Type=Unsigned32
_AsChannelProfileScrMcr_Object=MibTableColumn
asChannelProfileScrMcr=_AsChannelProfileScrMcr_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,7),_AsChannelProfileScrMcr_Type())
asChannelProfileScrMcr.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfileScrMcr.setStatus(_A)
class _AsChannelProfileBt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AsChannelProfileBt_Type.__name__=_B
_AsChannelProfileBt_Object=MibTableColumn
asChannelProfileBt=_AsChannelProfileBt_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,8),_AsChannelProfileBt_Type())
asChannelProfileBt.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfileBt.setStatus(_A)
_AsChannelProfileRowStatus_Type=RowStatus
_AsChannelProfileRowStatus_Object=MibTableColumn
asChannelProfileRowStatus=_AsChannelProfileRowStatus_Object((1,3,6,1,4,1,6321,1,2,3,2,99,6,1,9),_AsChannelProfileRowStatus_Type())
asChannelProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:asChannelProfileRowStatus.setStatus(_A)
_AsChannelStatusTable_Object=MibTable
asChannelStatusTable=_AsChannelStatusTable_Object((1,3,6,1,4,1,6321,1,2,3,2,99,7))
if mibBuilder.loadTexts:asChannelStatusTable.setStatus(_A)
_AsChannelStatusEntry_Object=MibTableRow
asChannelStatusEntry=_AsChannelStatusEntry_Object((1,3,6,1,4,1,6321,1,2,3,2,99,7,1))
asChannelStatusEntry.setIndexNames((0,_H,_I),(0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:asChannelStatusEntry.setStatus(_A)
_AsChannelTxPackets_Type=Counter32
_AsChannelTxPackets_Object=MibTableColumn
asChannelTxPackets=_AsChannelTxPackets_Object((1,3,6,1,4,1,6321,1,2,3,2,99,7,1,1),_AsChannelTxPackets_Type())
asChannelTxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:asChannelTxPackets.setStatus(_A)
_AsChannelRxPackets_Type=Counter32
_AsChannelRxPackets_Object=MibTableColumn
asChannelRxPackets=_AsChannelRxPackets_Object((1,3,6,1,4,1,6321,1,2,3,2,99,7,1,2),_AsChannelRxPackets_Type())
asChannelRxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:asChannelRxPackets.setStatus(_A)
_AsChannelTxCells_Type=Counter32
_AsChannelTxCells_Object=MibTableColumn
asChannelTxCells=_AsChannelTxCells_Object((1,3,6,1,4,1,6321,1,2,3,2,99,7,1,3),_AsChannelTxCells_Type())
asChannelTxCells.setMaxAccess(_D)
if mibBuilder.loadTexts:asChannelTxCells.setStatus(_A)
_AsChannelRxCells_Type=Counter32
_AsChannelRxCells_Object=MibTableColumn
asChannelRxCells=_AsChannelRxCells_Object((1,3,6,1,4,1,6321,1,2,3,2,99,7,1,4),_AsChannelRxCells_Type())
asChannelRxCells.setMaxAccess(_D)
if mibBuilder.loadTexts:asChannelRxCells.setStatus(_A)
_AsMaxNumOfIpqosProfiles_Type=Integer32
_AsMaxNumOfIpqosProfiles_Object=MibScalar
asMaxNumOfIpqosProfiles=_AsMaxNumOfIpqosProfiles_Object((1,3,6,1,4,1,6321,1,2,3,2,99,8),_AsMaxNumOfIpqosProfiles_Type())
asMaxNumOfIpqosProfiles.setMaxAccess(_D)
if mibBuilder.loadTexts:asMaxNumOfIpqosProfiles.setStatus(_A)
_AsIpqosProfileTable_Object=MibTable
asIpqosProfileTable=_AsIpqosProfileTable_Object((1,3,6,1,4,1,6321,1,2,3,2,99,9))
if mibBuilder.loadTexts:asIpqosProfileTable.setStatus(_A)
_AsIpqosProfileEntry_Object=MibTableRow
asIpqosProfileEntry=_AsIpqosProfileEntry_Object((1,3,6,1,4,1,6321,1,2,3,2,99,9,1))
asIpqosProfileEntry.setIndexNames((1,_E,_M))
if mibBuilder.loadTexts:asIpqosProfileEntry.setStatus(_A)
class _AsIpqosProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AsIpqosProfileName_Type.__name__=_G
_AsIpqosProfileName_Object=MibTableColumn
asIpqosProfileName=_AsIpqosProfileName_Object((1,3,6,1,4,1,6321,1,2,3,2,99,9,1,1),_AsIpqosProfileName_Type())
asIpqosProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:asIpqosProfileName.setStatus(_A)
class _AsIpqosProfileEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('llc',1),('vc',2)))
_AsIpqosProfileEncap_Type.__name__=_B
_AsIpqosProfileEncap_Object=MibTableColumn
asIpqosProfileEncap=_AsIpqosProfileEncap_Object((1,3,6,1,4,1,6321,1,2,3,2,99,9,1,2),_AsIpqosProfileEncap_Type())
asIpqosProfileEncap.setMaxAccess(_F)
if mibBuilder.loadTexts:asIpqosProfileEncap.setStatus(_A)
class _AsIpqosProfileQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('one',1),('two',2),('four',4)))
_AsIpqosProfileQueueNumber_Type.__name__=_B
_AsIpqosProfileQueueNumber_Object=MibTableColumn
asIpqosProfileQueueNumber=_AsIpqosProfileQueueNumber_Object((1,3,6,1,4,1,6321,1,2,3,2,99,9,1,3),_AsIpqosProfileQueueNumber_Type())
asIpqosProfileQueueNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:asIpqosProfileQueueNumber.setStatus(_A)
_AsIpqosProfileRowStatus_Type=RowStatus
_AsIpqosProfileRowStatus_Object=MibTableColumn
asIpqosProfileRowStatus=_AsIpqosProfileRowStatus_Object((1,3,6,1,4,1,6321,1,2,3,2,99,9,1,4),_AsIpqosProfileRowStatus_Type())
asIpqosProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:asIpqosProfileRowStatus.setStatus(_A)
_AsIpqosProfileQueueTable_Object=MibTable
asIpqosProfileQueueTable=_AsIpqosProfileQueueTable_Object((1,3,6,1,4,1,6321,1,2,3,2,99,10))
if mibBuilder.loadTexts:asIpqosProfileQueueTable.setStatus(_A)
_AsIpqosProfileQueueEntry_Object=MibTableRow
asIpqosProfileQueueEntry=_AsIpqosProfileQueueEntry_Object((1,3,6,1,4,1,6321,1,2,3,2,99,10,1))
asIpqosProfileQueueEntry.setIndexNames((0,_E,_M),(1,_E,_Q))
if mibBuilder.loadTexts:asIpqosProfileQueueEntry.setStatus(_A)
class _AsIpqosProfileQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AsIpqosProfileQueueIndex_Type.__name__=_B
_AsIpqosProfileQueueIndex_Object=MibTableColumn
asIpqosProfileQueueIndex=_AsIpqosProfileQueueIndex_Object((1,3,6,1,4,1,6321,1,2,3,2,99,10,1,1),_AsIpqosProfileQueueIndex_Type())
asIpqosProfileQueueIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:asIpqosProfileQueueIndex.setStatus(_A)
class _AsIpqosProfileAAL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AsIpqosProfileAAL_Type.__name__=_B
_AsIpqosProfileAAL_Object=MibTableColumn
asIpqosProfileAAL=_AsIpqosProfileAAL_Object((1,3,6,1,4,1,6321,1,2,3,2,99,10,1,2),_AsIpqosProfileAAL_Type())
asIpqosProfileAAL.setMaxAccess(_F)
if mibBuilder.loadTexts:asIpqosProfileAAL.setStatus(_A)
class _AsIpqosProfileLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ubr',0),(_P,1),(_O,2),('cbr',3)))
_AsIpqosProfileLevel_Type.__name__=_B
_AsIpqosProfileLevel_Object=MibTableColumn
asIpqosProfileLevel=_AsIpqosProfileLevel_Object((1,3,6,1,4,1,6321,1,2,3,2,99,10,1,3),_AsIpqosProfileLevel_Type())
asIpqosProfileLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:asIpqosProfileLevel.setStatus(_A)
_AsIpqosProfileRate_Type=Unsigned32
_AsIpqosProfileRate_Object=MibTableColumn
asIpqosProfileRate=_AsIpqosProfileRate_Object((1,3,6,1,4,1,6321,1,2,3,2,99,10,1,4),_AsIpqosProfileRate_Type())
asIpqosProfileRate.setMaxAccess(_F)
if mibBuilder.loadTexts:asIpqosProfileRate.setStatus(_A)
class _AsShapingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('atm',1),('packet',2)))
_AsShapingMode_Type.__name__=_B
_AsShapingMode_Object=MibScalar
asShapingMode=_AsShapingMode_Object((1,3,6,1,4,1,6321,1,2,3,2,99,11),_AsShapingMode_Type())
asShapingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:asShapingMode.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'asMaxNumOfChannels':asMaxNumOfChannels,'asChannelTable':asChannelTable,'asChannelEntry':asChannelEntry,_J:asChannelVpi,_K:asChannelVci,'asChannelPvid':asChannelPvid,'asChannelPriority':asChannelPriority,'asChannelProfile':asChannelProfile,'asChannelRowStatus':asChannelRowStatus,'asMaxNumOfChannelProfiles':asMaxNumOfChannelProfiles,'asChannelProfileTable':asChannelProfileTable,'asChannelProfileEntry':asChannelProfileEntry,_N:asChannelProfileName,'asChannelProfileEncap':asChannelProfileEncap,'asChannelProfileAAL':asChannelProfileAAL,'asChannelProfileClass':asChannelProfileClass,'asChannelProfilePcr':asChannelProfilePcr,'asChannelProfileCdvt':asChannelProfileCdvt,'asChannelProfileScrMcr':asChannelProfileScrMcr,'asChannelProfileBt':asChannelProfileBt,'asChannelProfileRowStatus':asChannelProfileRowStatus,'asChannelStatusTable':asChannelStatusTable,'asChannelStatusEntry':asChannelStatusEntry,'asChannelTxPackets':asChannelTxPackets,'asChannelRxPackets':asChannelRxPackets,'asChannelTxCells':asChannelTxCells,'asChannelRxCells':asChannelRxCells,'asMaxNumOfIpqosProfiles':asMaxNumOfIpqosProfiles,'asIpqosProfileTable':asIpqosProfileTable,'asIpqosProfileEntry':asIpqosProfileEntry,_M:asIpqosProfileName,'asIpqosProfileEncap':asIpqosProfileEncap,'asIpqosProfileQueueNumber':asIpqosProfileQueueNumber,'asIpqosProfileRowStatus':asIpqosProfileRowStatus,'asIpqosProfileQueueTable':asIpqosProfileQueueTable,'asIpqosProfileQueueEntry':asIpqosProfileQueueEntry,_Q:asIpqosProfileQueueIndex,'asIpqosProfileAAL':asIpqosProfileAAL,'asIpqosProfileLevel':asIpqosProfileLevel,'asIpqosProfileRate':asIpqosProfileRate,'asShapingMode':asShapingMode})