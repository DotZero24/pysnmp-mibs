_W='hneLANGWMappingIndex'
_V='hneLANIndex'
_U='hneWiFiGWSupportedIndex'
_T='width20and40Mhz'
_S='width20MHz'
_R='unknown'
_Q='percent100'
_P='percent75'
_O='percent50'
_N='percent25'
_M='percent12'
_L='hneWiFiGWIndex'
_K='read-create'
_J='TruthValue'
_I='gatewayDefault'
_H='not-accessible'
_G='HNE-DEVICE-MIB'
_F='DisplayString'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdRouter,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdRouter')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
hneMib=ModuleIdentity((1,3,6,1,4,1,4115,1,20,3))
if mibBuilder.loadTexts:hneMib.setRevisions(('2015-01-14 00:00','2015-01-07 00:00'))
_HneMibObjects_ObjectIdentity=ObjectIdentity
hneMibObjects=_HneMibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,3,1))
_HneWiFiGWSupport_ObjectIdentity=ObjectIdentity
hneWiFiGWSupport=_HneWiFiGWSupport_ObjectIdentity((1,3,6,1,4,1,4115,1,20,3,1,1))
_HneWiFiGWSearch_Type=TruthValue
_HneWiFiGWSearch_Object=MibScalar
hneWiFiGWSearch=_HneWiFiGWSearch_Object((1,3,6,1,4,1,4115,1,20,3,1,1,1),_HneWiFiGWSearch_Type())
hneWiFiGWSearch.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWSearch.setStatus(_A)
_HneWiFiGWTable_Object=MibTable
hneWiFiGWTable=_HneWiFiGWTable_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2))
if mibBuilder.loadTexts:hneWiFiGWTable.setStatus(_A)
_HneWiFiGWEntry_Object=MibTableRow
hneWiFiGWEntry=_HneWiFiGWEntry_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1))
hneWiFiGWEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:hneWiFiGWEntry.setStatus(_A)
_HneWiFiGWIndex_Type=Unsigned32
_HneWiFiGWIndex_Object=MibTableColumn
hneWiFiGWIndex=_HneWiFiGWIndex_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,1),_HneWiFiGWIndex_Type())
hneWiFiGWIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hneWiFiGWIndex.setStatus(_A)
_HneWiFiGWMACAddr_Type=MacAddress
_HneWiFiGWMACAddr_Object=MibTableColumn
hneWiFiGWMACAddr=_HneWiFiGWMACAddr_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,2),_HneWiFiGWMACAddr_Type())
hneWiFiGWMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWMACAddr.setStatus(_A)
_HneWiFiGWIPAddrType_Type=InetAddressType
_HneWiFiGWIPAddrType_Object=MibTableColumn
hneWiFiGWIPAddrType=_HneWiFiGWIPAddrType_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,3),_HneWiFiGWIPAddrType_Type())
hneWiFiGWIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWIPAddrType.setStatus(_A)
_HneWiFiGWIPAddress_Type=InetAddress
_HneWiFiGWIPAddress_Object=MibTableColumn
hneWiFiGWIPAddress=_HneWiFiGWIPAddress_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,4),_HneWiFiGWIPAddress_Type())
hneWiFiGWIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWIPAddress.setStatus(_A)
_HneWiFiGWARRISAutoCfgSupport_Type=TruthValue
_HneWiFiGWARRISAutoCfgSupport_Object=MibTableColumn
hneWiFiGWARRISAutoCfgSupport=_HneWiFiGWARRISAutoCfgSupport_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,5),_HneWiFiGWARRISAutoCfgSupport_Type())
hneWiFiGWARRISAutoCfgSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWARRISAutoCfgSupport.setStatus(_A)
_HneWiFiGWLocation_Type=DisplayString
_HneWiFiGWLocation_Object=MibTableColumn
hneWiFiGWLocation=_HneWiFiGWLocation_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,6),_HneWiFiGWLocation_Type())
hneWiFiGWLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWLocation.setStatus(_A)
class _HneWiFiGWManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HneWiFiGWManufacturer_Type.__name__=_F
_HneWiFiGWManufacturer_Object=MibTableColumn
hneWiFiGWManufacturer=_HneWiFiGWManufacturer_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,7),_HneWiFiGWManufacturer_Type())
hneWiFiGWManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWManufacturer.setStatus(_A)
class _HneWiFiGWModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HneWiFiGWModelName_Type.__name__=_F
_HneWiFiGWModelName_Object=MibTableColumn
hneWiFiGWModelName=_HneWiFiGWModelName_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,8),_HneWiFiGWModelName_Type())
hneWiFiGWModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWModelName.setStatus(_A)
class _HneWiFiGWModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HneWiFiGWModelNumber_Type.__name__=_F
_HneWiFiGWModelNumber_Object=MibTableColumn
hneWiFiGWModelNumber=_HneWiFiGWModelNumber_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,9),_HneWiFiGWModelNumber_Type())
hneWiFiGWModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWModelNumber.setStatus(_A)
class _HneWiFiGWConfigurationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_HneWiFiGWConfigurationId_Type.__name__=_E
_HneWiFiGWConfigurationId_Object=MibTableColumn
hneWiFiGWConfigurationId=_HneWiFiGWConfigurationId_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,10),_HneWiFiGWConfigurationId_Type())
hneWiFiGWConfigurationId.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWConfigurationId.setStatus(_A)
_HneWiFiGWLastSynchAttemptTime_Type=DateAndTime
_HneWiFiGWLastSynchAttemptTime_Object=MibTableColumn
hneWiFiGWLastSynchAttemptTime=_HneWiFiGWLastSynchAttemptTime_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,11),_HneWiFiGWLastSynchAttemptTime_Type())
hneWiFiGWLastSynchAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWLastSynchAttemptTime.setStatus(_A)
class _HneWiFiGWLastSynchAttemptResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*(('uninitialized',-1),('pass',0),('failHTTPSSessionEstablishment',1),('failHTTPSPUT',2)))
_HneWiFiGWLastSynchAttemptResult_Type.__name__=_D
_HneWiFiGWLastSynchAttemptResult_Object=MibTableColumn
hneWiFiGWLastSynchAttemptResult=_HneWiFiGWLastSynchAttemptResult_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,12),_HneWiFiGWLastSynchAttemptResult_Type())
hneWiFiGWLastSynchAttemptResult.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWLastSynchAttemptResult.setStatus(_A)
_HneWiFiGWSynchedWithGW_Type=TruthValue
_HneWiFiGWSynchedWithGW_Object=MibTableColumn
hneWiFiGWSynchedWithGW=_HneWiFiGWSynchedWithGW_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,13),_HneWiFiGWSynchedWithGW_Type())
hneWiFiGWSynchedWithGW.setMaxAccess(_B)
if mibBuilder.loadTexts:hneWiFiGWSynchedWithGW.setStatus(_A)
class _HneWiFiGWOverride24OutputPower_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,12,25,50,75,100)));namedValues=NamedValues(*((_I,0),(_M,12),(_N,25),(_O,50),(_P,75),(_Q,100)))
_HneWiFiGWOverride24OutputPower_Type.__name__=_D
_HneWiFiGWOverride24OutputPower_Object=MibTableColumn
hneWiFiGWOverride24OutputPower=_HneWiFiGWOverride24OutputPower_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,14),_HneWiFiGWOverride24OutputPower_Type())
hneWiFiGWOverride24OutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWOverride24OutputPower.setStatus(_A)
class _HneWiFiGWOverride50OutputPower_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,12,25,50,75,100)));namedValues=NamedValues(*((_I,0),(_M,12),(_N,25),(_O,50),(_P,75),(_Q,100)))
_HneWiFiGWOverride50OutputPower_Type.__name__=_D
_HneWiFiGWOverride50OutputPower_Object=MibTableColumn
hneWiFiGWOverride50OutputPower=_HneWiFiGWOverride50OutputPower_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,15),_HneWiFiGWOverride50OutputPower_Type())
hneWiFiGWOverride50OutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWOverride50OutputPower.setStatus(_A)
class _HneWiFiGWOverride24Channel_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216),ValueRangeConstraint(255,255))
_HneWiFiGWOverride24Channel_Type.__name__=_E
_HneWiFiGWOverride24Channel_Object=MibTableColumn
hneWiFiGWOverride24Channel=_HneWiFiGWOverride24Channel_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,16),_HneWiFiGWOverride24Channel_Type())
hneWiFiGWOverride24Channel.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWOverride24Channel.setStatus(_A)
class _HneWiFiGWOverride50Channel_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216),ValueRangeConstraint(255,255))
_HneWiFiGWOverride50Channel_Type.__name__=_E
_HneWiFiGWOverride50Channel_Object=MibTableColumn
hneWiFiGWOverride50Channel=_HneWiFiGWOverride50Channel_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,17),_HneWiFiGWOverride50Channel_Type())
hneWiFiGWOverride50Channel.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWOverride50Channel.setStatus(_A)
class _HneWiFiGWOverride24ChannelBW_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,-1,0,1,2)));namedValues=NamedValues(*((_I,-2),(_R,-1),(_S,0),('width40MHz',1),(_T,2)))
_HneWiFiGWOverride24ChannelBW_Type.__name__=_D
_HneWiFiGWOverride24ChannelBW_Object=MibTableColumn
hneWiFiGWOverride24ChannelBW=_HneWiFiGWOverride24ChannelBW_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,18),_HneWiFiGWOverride24ChannelBW_Type())
hneWiFiGWOverride24ChannelBW.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWOverride24ChannelBW.setStatus(_A)
class _HneWiFiGWOverride50ChannelBW_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,-1,0,2,3)));namedValues=NamedValues(*((_I,-2),(_R,-1),(_S,0),(_T,2),('width20and40and80Mhz',3)))
_HneWiFiGWOverride50ChannelBW_Type.__name__=_D
_HneWiFiGWOverride50ChannelBW_Object=MibTableColumn
hneWiFiGWOverride50ChannelBW=_HneWiFiGWOverride50ChannelBW_Object((1,3,6,1,4,1,4115,1,20,3,1,1,2,1,19),_HneWiFiGWOverride50ChannelBW_Type())
hneWiFiGWOverride50ChannelBW.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWOverride50ChannelBW.setStatus(_A)
_HneWiFiGWSupportedTable_Object=MibTable
hneWiFiGWSupportedTable=_HneWiFiGWSupportedTable_Object((1,3,6,1,4,1,4115,1,20,3,1,1,3))
if mibBuilder.loadTexts:hneWiFiGWSupportedTable.setStatus(_A)
_HneWiFiGWSupportedEntry_Object=MibTableRow
hneWiFiGWSupportedEntry=_HneWiFiGWSupportedEntry_Object((1,3,6,1,4,1,4115,1,20,3,1,1,3,1))
hneWiFiGWSupportedEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:hneWiFiGWSupportedEntry.setStatus(_A)
_HneWiFiGWSupportedIndex_Type=Unsigned32
_HneWiFiGWSupportedIndex_Object=MibTableColumn
hneWiFiGWSupportedIndex=_HneWiFiGWSupportedIndex_Object((1,3,6,1,4,1,4115,1,20,3,1,1,3,1,1),_HneWiFiGWSupportedIndex_Type())
hneWiFiGWSupportedIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hneWiFiGWSupportedIndex.setStatus(_A)
class _HneWiFiGWSupportedManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HneWiFiGWSupportedManufacturer_Type.__name__=_F
_HneWiFiGWSupportedManufacturer_Object=MibTableColumn
hneWiFiGWSupportedManufacturer=_HneWiFiGWSupportedManufacturer_Object((1,3,6,1,4,1,4115,1,20,3,1,1,3,1,2),_HneWiFiGWSupportedManufacturer_Type())
hneWiFiGWSupportedManufacturer.setMaxAccess(_K)
if mibBuilder.loadTexts:hneWiFiGWSupportedManufacturer.setStatus(_A)
class _HneWiFiGWSupportedModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HneWiFiGWSupportedModelNumber_Type.__name__=_F
_HneWiFiGWSupportedModelNumber_Object=MibTableColumn
hneWiFiGWSupportedModelNumber=_HneWiFiGWSupportedModelNumber_Object((1,3,6,1,4,1,4115,1,20,3,1,1,3,1,3),_HneWiFiGWSupportedModelNumber_Type())
hneWiFiGWSupportedModelNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:hneWiFiGWSupportedModelNumber.setStatus(_A)
_HneWiFiGWSupportedRowStatus_Type=RowStatus
_HneWiFiGWSupportedRowStatus_Object=MibTableColumn
hneWiFiGWSupportedRowStatus=_HneWiFiGWSupportedRowStatus_Object((1,3,6,1,4,1,4115,1,20,3,1,1,3,1,4),_HneWiFiGWSupportedRowStatus_Type())
hneWiFiGWSupportedRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hneWiFiGWSupportedRowStatus.setStatus(_A)
class _HneWiFiGWConfigAttempts_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HneWiFiGWConfigAttempts_Type.__name__=_E
_HneWiFiGWConfigAttempts_Object=MibScalar
hneWiFiGWConfigAttempts=_HneWiFiGWConfigAttempts_Object((1,3,6,1,4,1,4115,1,20,3,1,1,4),_HneWiFiGWConfigAttempts_Type())
hneWiFiGWConfigAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWConfigAttempts.setStatus(_A)
class _HneWiFiGWConfigDuration_Type(Unsigned32):defaultValue=3600
_HneWiFiGWConfigDuration_Type.__name__=_E
_HneWiFiGWConfigDuration_Object=MibScalar
hneWiFiGWConfigDuration=_HneWiFiGWConfigDuration_Object((1,3,6,1,4,1,4115,1,20,3,1,1,5),_HneWiFiGWConfigDuration_Type())
hneWiFiGWConfigDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWConfigDuration.setStatus(_A)
if mibBuilder.loadTexts:hneWiFiGWConfigDuration.setUnits('seconds')
class _HneWiFiGWAutoConfigurationEnable_Type(TruthValue):defaultValue=2
_HneWiFiGWAutoConfigurationEnable_Type.__name__=_J
_HneWiFiGWAutoConfigurationEnable_Object=MibScalar
hneWiFiGWAutoConfigurationEnable=_HneWiFiGWAutoConfigurationEnable_Object((1,3,6,1,4,1,4115,1,20,3,1,1,6),_HneWiFiGWAutoConfigurationEnable_Type())
hneWiFiGWAutoConfigurationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWAutoConfigurationEnable.setStatus(_A)
class _HneWiFiGWSecurityEnable_Type(TruthValue):defaultValue=1
_HneWiFiGWSecurityEnable_Type.__name__=_J
_HneWiFiGWSecurityEnable_Object=MibScalar
hneWiFiGWSecurityEnable=_HneWiFiGWSecurityEnable_Object((1,3,6,1,4,1,4115,1,20,3,1,1,7),_HneWiFiGWSecurityEnable_Type())
hneWiFiGWSecurityEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hneWiFiGWSecurityEnable.setStatus(_A)
_HneLAN_ObjectIdentity=ObjectIdentity
hneLAN=_HneLAN_ObjectIdentity((1,3,6,1,4,1,4115,1,20,3,1,2))
_HneLANTable_Object=MibTable
hneLANTable=_HneLANTable_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1))
if mibBuilder.loadTexts:hneLANTable.setStatus(_A)
_HneLANEntry_Object=MibTableRow
hneLANEntry=_HneLANEntry_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1,1))
hneLANEntry.setIndexNames((0,_G,_V),(0,_G,_W))
if mibBuilder.loadTexts:hneLANEntry.setStatus(_A)
_HneLANIndex_Type=Unsigned32
_HneLANIndex_Object=MibTableColumn
hneLANIndex=_HneLANIndex_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1,1,1),_HneLANIndex_Type())
hneLANIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hneLANIndex.setStatus(_A)
_HneLANGWMappingIndex_Type=Unsigned32
_HneLANGWMappingIndex_Object=MibTableColumn
hneLANGWMappingIndex=_HneLANGWMappingIndex_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1,1,2),_HneLANGWMappingIndex_Type())
hneLANGWMappingIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hneLANGWMappingIndex.setStatus(_A)
_HneLANInterface_Type=DisplayString
_HneLANInterface_Object=MibTableColumn
hneLANInterface=_HneLANInterface_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1,1,3),_HneLANInterface_Type())
hneLANInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hneLANInterface.setStatus(_A)
class _HneLANInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('radio24Ghz',0),('radio50Ghz',1),('radio24GhzSsid',2),('radio50GhzSsid',3),('ethernet',4)))
_HneLANInterfaceType_Type.__name__=_D
_HneLANInterfaceType_Object=MibTableColumn
hneLANInterfaceType=_HneLANInterfaceType_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1,1,4),_HneLANInterfaceType_Type())
hneLANInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hneLANInterfaceType.setStatus(_A)
_HneLANBridgingMgmtPortInterface_Type=DisplayString
_HneLANBridgingMgmtPortInterface_Object=MibTableColumn
hneLANBridgingMgmtPortInterface=_HneLANBridgingMgmtPortInterface_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1,1,5),_HneLANBridgingMgmtPortInterface_Type())
hneLANBridgingMgmtPortInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hneLANBridgingMgmtPortInterface.setStatus(_A)
_HneLANVLANID_Type=Unsigned32
_HneLANVLANID_Object=MibTableColumn
hneLANVLANID=_HneLANVLANID_Object((1,3,6,1,4,1,4115,1,20,3,1,2,1,1,6),_HneLANVLANID_Type())
hneLANVLANID.setMaxAccess(_B)
if mibBuilder.loadTexts:hneLANVLANID.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hneMib':hneMib,'hneMibObjects':hneMibObjects,'hneWiFiGWSupport':hneWiFiGWSupport,'hneWiFiGWSearch':hneWiFiGWSearch,'hneWiFiGWTable':hneWiFiGWTable,'hneWiFiGWEntry':hneWiFiGWEntry,_L:hneWiFiGWIndex,'hneWiFiGWMACAddr':hneWiFiGWMACAddr,'hneWiFiGWIPAddrType':hneWiFiGWIPAddrType,'hneWiFiGWIPAddress':hneWiFiGWIPAddress,'hneWiFiGWARRISAutoCfgSupport':hneWiFiGWARRISAutoCfgSupport,'hneWiFiGWLocation':hneWiFiGWLocation,'hneWiFiGWManufacturer':hneWiFiGWManufacturer,'hneWiFiGWModelName':hneWiFiGWModelName,'hneWiFiGWModelNumber':hneWiFiGWModelNumber,'hneWiFiGWConfigurationId':hneWiFiGWConfigurationId,'hneWiFiGWLastSynchAttemptTime':hneWiFiGWLastSynchAttemptTime,'hneWiFiGWLastSynchAttemptResult':hneWiFiGWLastSynchAttemptResult,'hneWiFiGWSynchedWithGW':hneWiFiGWSynchedWithGW,'hneWiFiGWOverride24OutputPower':hneWiFiGWOverride24OutputPower,'hneWiFiGWOverride50OutputPower':hneWiFiGWOverride50OutputPower,'hneWiFiGWOverride24Channel':hneWiFiGWOverride24Channel,'hneWiFiGWOverride50Channel':hneWiFiGWOverride50Channel,'hneWiFiGWOverride24ChannelBW':hneWiFiGWOverride24ChannelBW,'hneWiFiGWOverride50ChannelBW':hneWiFiGWOverride50ChannelBW,'hneWiFiGWSupportedTable':hneWiFiGWSupportedTable,'hneWiFiGWSupportedEntry':hneWiFiGWSupportedEntry,_U:hneWiFiGWSupportedIndex,'hneWiFiGWSupportedManufacturer':hneWiFiGWSupportedManufacturer,'hneWiFiGWSupportedModelNumber':hneWiFiGWSupportedModelNumber,'hneWiFiGWSupportedRowStatus':hneWiFiGWSupportedRowStatus,'hneWiFiGWConfigAttempts':hneWiFiGWConfigAttempts,'hneWiFiGWConfigDuration':hneWiFiGWConfigDuration,'hneWiFiGWAutoConfigurationEnable':hneWiFiGWAutoConfigurationEnable,'hneWiFiGWSecurityEnable':hneWiFiGWSecurityEnable,'hneLAN':hneLAN,'hneLANTable':hneLANTable,'hneLANEntry':hneLANEntry,_V:hneLANIndex,_W:hneLANGWMappingIndex,'hneLANInterface':hneLANInterface,'hneLANInterfaceType':hneLANInterfaceType,'hneLANBridgingMgmtPortInterface':hneLANBridgingMgmtPortInterface,'hneLANVLANID':hneLANVLANID})