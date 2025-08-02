_l='usbCDCEtherXmtAddressGroup'
_k='usbMibCDCEtherGroup'
_j='usbMibCDCGroup'
_i='usbCDCEtherDataCheckErrs'
_h='usbCDCEtherDataStatisticsCapabilities'
_g='usbCDCEtherPacketFilter'
_f='usbCDCEtherMacAddress'
_e='usbCDCStalls'
_d='usbCDCDataEndpoints'
_c='usbCDCDataTransferType'
_b='usbCDCVersion'
_a='usbCDCSubclass'
_Z='usbDeviceRemoteWakeupOn'
_Y='usbDeviceRemoteWakeup'
_X='usbDeviceEnumCounter'
_W='usbDeviceStatus'
_V='usbDeviceActiveClass'
_U='usbDeviceNumberConfigurations'
_T='usbDeviceProductID'
_S='usbDeviceVendorID'
_R='usbDevicePower'
_Q='usbPortRate'
_P='usbPortType'
_O='usbNumber'
_N='OctetString'
_M='usbMibBasicGroup'
_L='ifCDCEtherXmtAddress'
_K='usbCDCIfIndex'
_J='usbCDCIndex'
_I='usbDeviceIndex'
_H='usbPortIndex'
_G='Bits'
_F='usbCDCEtherIfIndex'
_E='usbCDCEtherIndex'
_D='Integer32'
_C='read-only'
_B='USB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
usbMib=ModuleIdentity((1,3,6,1,3,103))
_UsbMibObjects_ObjectIdentity=ObjectIdentity
usbMibObjects=_UsbMibObjects_ObjectIdentity((1,3,6,1,3,103,1))
class _UsbNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UsbNumber_Type.__name__=_D
_UsbNumber_Object=MibScalar
usbNumber=_UsbNumber_Object((1,3,6,1,3,103,1,1),_UsbNumber_Type())
usbNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:usbNumber.setStatus(_A)
_UsbPortTable_Object=MibTable
usbPortTable=_UsbPortTable_Object((1,3,6,1,3,103,1,2))
if mibBuilder.loadTexts:usbPortTable.setStatus(_A)
_UsbPortEntry_Object=MibTableRow
usbPortEntry=_UsbPortEntry_Object((1,3,6,1,3,103,1,2,1))
usbPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:usbPortEntry.setStatus(_A)
class _UsbPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UsbPortIndex_Type.__name__=_D
_UsbPortIndex_Object=MibTableColumn
usbPortIndex=_UsbPortIndex_Object((1,3,6,1,3,103,1,2,1,1),_UsbPortIndex_Type())
usbPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:usbPortIndex.setStatus(_A)
class _UsbPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('host',1),('device',2),('hub',3)))
_UsbPortType_Type.__name__=_D
_UsbPortType_Object=MibTableColumn
usbPortType=_UsbPortType_Object((1,3,6,1,3,103,1,2,1,2),_UsbPortType_Type())
usbPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:usbPortType.setStatus(_A)
class _UsbPortRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low-speed',1),('full-speed',2),('high-speed',3)))
_UsbPortRate_Type.__name__=_D
_UsbPortRate_Object=MibTableColumn
usbPortRate=_UsbPortRate_Object((1,3,6,1,3,103,1,2,1,3),_UsbPortRate_Type())
usbPortRate.setMaxAccess(_C)
if mibBuilder.loadTexts:usbPortRate.setStatus(_A)
_UsbDeviceTable_Object=MibTable
usbDeviceTable=_UsbDeviceTable_Object((1,3,6,1,3,103,1,3))
if mibBuilder.loadTexts:usbDeviceTable.setStatus(_A)
_UsbDeviceEntry_Object=MibTableRow
usbDeviceEntry=_UsbDeviceEntry_Object((1,3,6,1,3,103,1,3,1))
usbDeviceEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:usbDeviceEntry.setStatus(_A)
class _UsbDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UsbDeviceIndex_Type.__name__=_D
_UsbDeviceIndex_Object=MibTableColumn
usbDeviceIndex=_UsbDeviceIndex_Object((1,3,6,1,3,103,1,3,1,1),_UsbDeviceIndex_Type())
usbDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceIndex.setStatus(_A)
class _UsbDevicePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('self-powered',2),('bus-powered',3)))
_UsbDevicePower_Type.__name__=_D
_UsbDevicePower_Object=MibTableColumn
usbDevicePower=_UsbDevicePower_Object((1,3,6,1,3,103,1,3,1,2),_UsbDevicePower_Type())
usbDevicePower.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDevicePower.setStatus(_A)
_UsbDeviceVendorID_Type=OctetString
_UsbDeviceVendorID_Object=MibTableColumn
usbDeviceVendorID=_UsbDeviceVendorID_Object((1,3,6,1,3,103,1,3,1,3),_UsbDeviceVendorID_Type())
usbDeviceVendorID.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceVendorID.setStatus(_A)
_UsbDeviceProductID_Type=OctetString
_UsbDeviceProductID_Object=MibTableColumn
usbDeviceProductID=_UsbDeviceProductID_Object((1,3,6,1,3,103,1,3,1,4),_UsbDeviceProductID_Type())
usbDeviceProductID.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceProductID.setStatus(_A)
class _UsbDeviceNumberConfigurations_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UsbDeviceNumberConfigurations_Type.__name__=_D
_UsbDeviceNumberConfigurations_Object=MibTableColumn
usbDeviceNumberConfigurations=_UsbDeviceNumberConfigurations_Object((1,3,6,1,3,103,1,3,1,5),_UsbDeviceNumberConfigurations_Type())
usbDeviceNumberConfigurations.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceNumberConfigurations.setStatus(_A)
class _UsbDeviceActiveClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('cdc',2)))
_UsbDeviceActiveClass_Type.__name__=_D
_UsbDeviceActiveClass_Object=MibTableColumn
usbDeviceActiveClass=_UsbDeviceActiveClass_Object((1,3,6,1,3,103,1,3,1,6),_UsbDeviceActiveClass_Type())
usbDeviceActiveClass.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceActiveClass.setStatus(_A)
class _UsbDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unattached',1),('attached',2),('powered',3),('default',4),('address',5),('configured',6),('suspended',7)))
_UsbDeviceStatus_Type.__name__=_D
_UsbDeviceStatus_Object=MibTableColumn
usbDeviceStatus=_UsbDeviceStatus_Object((1,3,6,1,3,103,1,3,1,7),_UsbDeviceStatus_Type())
usbDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceStatus.setStatus(_A)
_UsbDeviceEnumCounter_Type=Counter32
_UsbDeviceEnumCounter_Object=MibTableColumn
usbDeviceEnumCounter=_UsbDeviceEnumCounter_Object((1,3,6,1,3,103,1,3,1,8),_UsbDeviceEnumCounter_Type())
usbDeviceEnumCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceEnumCounter.setStatus(_A)
_UsbDeviceRemoteWakeup_Type=TruthValue
_UsbDeviceRemoteWakeup_Object=MibTableColumn
usbDeviceRemoteWakeup=_UsbDeviceRemoteWakeup_Object((1,3,6,1,3,103,1,3,1,9),_UsbDeviceRemoteWakeup_Type())
usbDeviceRemoteWakeup.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceRemoteWakeup.setStatus(_A)
_UsbDeviceRemoteWakeupOn_Type=TruthValue
_UsbDeviceRemoteWakeupOn_Object=MibTableColumn
usbDeviceRemoteWakeupOn=_UsbDeviceRemoteWakeupOn_Object((1,3,6,1,3,103,1,3,1,10),_UsbDeviceRemoteWakeupOn_Type())
usbDeviceRemoteWakeupOn.setMaxAccess(_C)
if mibBuilder.loadTexts:usbDeviceRemoteWakeupOn.setStatus(_A)
_UsbCDCTable_Object=MibTable
usbCDCTable=_UsbCDCTable_Object((1,3,6,1,3,103,1,4))
if mibBuilder.loadTexts:usbCDCTable.setStatus(_A)
_UsbCDCEntry_Object=MibTableRow
usbCDCEntry=_UsbCDCEntry_Object((1,3,6,1,3,103,1,4,1))
usbCDCEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:usbCDCEntry.setStatus(_A)
class _UsbCDCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UsbCDCIndex_Type.__name__=_D
_UsbCDCIndex_Object=MibTableColumn
usbCDCIndex=_UsbCDCIndex_Object((1,3,6,1,3,103,1,4,1,1),_UsbCDCIndex_Type())
usbCDCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCIndex.setStatus(_A)
_UsbCDCIfIndex_Type=InterfaceIndexOrZero
_UsbCDCIfIndex_Object=MibTableColumn
usbCDCIfIndex=_UsbCDCIfIndex_Object((1,3,6,1,3,103,1,4,1,2),_UsbCDCIfIndex_Type())
usbCDCIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCIfIndex.setStatus(_A)
class _UsbCDCSubclass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',0),('directLine',1),('acm',2),('telephony',3),('multichannel',4),('capi',5),('ethernet',6),('atm',7)))
_UsbCDCSubclass_Type.__name__=_D
_UsbCDCSubclass_Object=MibTableColumn
usbCDCSubclass=_UsbCDCSubclass_Object((1,3,6,1,3,103,1,4,1,3),_UsbCDCSubclass_Type())
usbCDCSubclass.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCSubclass.setStatus(_A)
class _UsbCDCVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_UsbCDCVersion_Type.__name__=_N
_UsbCDCVersion_Object=MibTableColumn
usbCDCVersion=_UsbCDCVersion_Object((1,3,6,1,3,103,1,4,1,4),_UsbCDCVersion_Type())
usbCDCVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCVersion.setStatus(_A)
class _UsbCDCDataTransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('synchronous',1),('asynchronous',2)))
_UsbCDCDataTransferType_Type.__name__=_D
_UsbCDCDataTransferType_Object=MibTableColumn
usbCDCDataTransferType=_UsbCDCDataTransferType_Object((1,3,6,1,3,103,1,4,1,5),_UsbCDCDataTransferType_Type())
usbCDCDataTransferType.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCDataTransferType.setStatus(_A)
class _UsbCDCDataEndpoints_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_UsbCDCDataEndpoints_Type.__name__=_D
_UsbCDCDataEndpoints_Object=MibTableColumn
usbCDCDataEndpoints=_UsbCDCDataEndpoints_Object((1,3,6,1,3,103,1,4,1,6),_UsbCDCDataEndpoints_Type())
usbCDCDataEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCDataEndpoints.setStatus(_A)
_UsbCDCStalls_Type=Counter32
_UsbCDCStalls_Object=MibTableColumn
usbCDCStalls=_UsbCDCStalls_Object((1,3,6,1,3,103,1,4,1,7),_UsbCDCStalls_Type())
usbCDCStalls.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCStalls.setStatus(_A)
_UsbCDCEtherTable_Object=MibTable
usbCDCEtherTable=_UsbCDCEtherTable_Object((1,3,6,1,3,103,1,5))
if mibBuilder.loadTexts:usbCDCEtherTable.setStatus(_A)
_UsbCDCEtherEntry_Object=MibTableRow
usbCDCEtherEntry=_UsbCDCEtherEntry_Object((1,3,6,1,3,103,1,5,1))
usbCDCEtherEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:usbCDCEtherEntry.setStatus(_A)
class _UsbCDCEtherIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UsbCDCEtherIndex_Type.__name__=_D
_UsbCDCEtherIndex_Object=MibTableColumn
usbCDCEtherIndex=_UsbCDCEtherIndex_Object((1,3,6,1,3,103,1,5,1,1),_UsbCDCEtherIndex_Type())
usbCDCEtherIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCEtherIndex.setStatus(_A)
_UsbCDCEtherIfIndex_Type=InterfaceIndexOrZero
_UsbCDCEtherIfIndex_Object=MibTableColumn
usbCDCEtherIfIndex=_UsbCDCEtherIfIndex_Object((1,3,6,1,3,103,1,5,1,2),_UsbCDCEtherIfIndex_Type())
usbCDCEtherIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCEtherIfIndex.setStatus(_A)
_UsbCDCEtherMacAddress_Type=MacAddress
_UsbCDCEtherMacAddress_Object=MibTableColumn
usbCDCEtherMacAddress=_UsbCDCEtherMacAddress_Object((1,3,6,1,3,103,1,5,1,3),_UsbCDCEtherMacAddress_Type())
usbCDCEtherMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCEtherMacAddress.setStatus(_A)
class _UsbCDCEtherPacketFilter_Type(Bits):namedValues=NamedValues(*(('packetPromiscuous',0),('packetAllMulticast',1),('packetDirected',2),('packetBroadcast',3),('packetMulticast',4)))
_UsbCDCEtherPacketFilter_Type.__name__=_G
_UsbCDCEtherPacketFilter_Object=MibTableColumn
usbCDCEtherPacketFilter=_UsbCDCEtherPacketFilter_Object((1,3,6,1,3,103,1,5,1,4),_UsbCDCEtherPacketFilter_Type())
usbCDCEtherPacketFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCEtherPacketFilter.setStatus(_A)
class _UsbCDCEtherDataStatisticsCapabilities_Type(Bits):namedValues=NamedValues(*(('frameXmitOk',0),('frameRcvOk',1),('frameXmitErr',2),('frameRcvErr',3),('frameRcvNoBuff',4),('bytesXmitDirectOk',5),('framesXmitDirectOk',6),('bytesXmitMulticastOk',7),('framesXmitMulticastOk',8),('bytesXmitBroadcastOk',9),('framesXmitBroadcastOk',10),('bytesRcvDirectOk',11),('framesRcvDirectOk',12),('bytesRcvMulticastOk',13),('framesRcvMulticastOk',14),('bytesRcvBroadcastOk',15),('framesRcvBroadcastOk',16),('framesRcvCrcErr',17),('xmitQueueLen',18),('rcvErrAlignment',19),('xmitOneCollision',20),('xmitMoreCollisions',21),('xmitDeferred',22),('xmitMaxCollision',23),('rcvOverrun',24),('xmitUnderrun',25),('xmitHearbeatFailure',26),('xmitTimesCrsLost',27),('xmitLateCollisions',28)))
_UsbCDCEtherDataStatisticsCapabilities_Type.__name__=_G
_UsbCDCEtherDataStatisticsCapabilities_Object=MibTableColumn
usbCDCEtherDataStatisticsCapabilities=_UsbCDCEtherDataStatisticsCapabilities_Object((1,3,6,1,3,103,1,5,1,5),_UsbCDCEtherDataStatisticsCapabilities_Type())
usbCDCEtherDataStatisticsCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCEtherDataStatisticsCapabilities.setStatus(_A)
_UsbCDCEtherDataCheckErrs_Type=Counter32
_UsbCDCEtherDataCheckErrs_Object=MibTableColumn
usbCDCEtherDataCheckErrs=_UsbCDCEtherDataCheckErrs_Object((1,3,6,1,3,103,1,5,1,6),_UsbCDCEtherDataCheckErrs_Type())
usbCDCEtherDataCheckErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:usbCDCEtherDataCheckErrs.setStatus(_A)
_UsbCDCEtherXmtAddressTable_Object=MibTable
usbCDCEtherXmtAddressTable=_UsbCDCEtherXmtAddressTable_Object((1,3,6,1,3,103,1,6))
if mibBuilder.loadTexts:usbCDCEtherXmtAddressTable.setStatus(_A)
_UsbCDCEtherXmtAddressEntry_Object=MibTableRow
usbCDCEtherXmtAddressEntry=_UsbCDCEtherXmtAddressEntry_Object((1,3,6,1,3,103,1,6,1))
usbCDCEtherXmtAddressEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_L))
if mibBuilder.loadTexts:usbCDCEtherXmtAddressEntry.setStatus(_A)
_IfCDCEtherXmtAddress_Type=MacAddress
_IfCDCEtherXmtAddress_Object=MibTableColumn
ifCDCEtherXmtAddress=_IfCDCEtherXmtAddress_Object((1,3,6,1,3,103,1,6,1,1),_IfCDCEtherXmtAddress_Type())
ifCDCEtherXmtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCDCEtherXmtAddress.setStatus(_A)
_UsbMibNotification_ObjectIdentity=ObjectIdentity
usbMibNotification=_UsbMibNotification_ObjectIdentity((1,3,6,1,3,103,2))
_UsbMibConformance_ObjectIdentity=ObjectIdentity
usbMibConformance=_UsbMibConformance_ObjectIdentity((1,3,6,1,3,103,3))
_UsbMibCompliances_ObjectIdentity=ObjectIdentity
usbMibCompliances=_UsbMibCompliances_ObjectIdentity((1,3,6,1,3,103,3,1))
_UsbMibGroups_ObjectIdentity=ObjectIdentity
usbMibGroups=_UsbMibGroups_ObjectIdentity((1,3,6,1,3,103,3,2))
usbMibBasicGroup=ObjectGroup((1,3,6,1,3,103,3,2,1))
usbMibBasicGroup.setObjects(*((_B,_O),(_B,_H),(_B,_P),(_B,_Q),(_B,_I),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:usbMibBasicGroup.setStatus(_A)
usbMibCDCGroup=ObjectGroup((1,3,6,1,3,103,3,2,2))
usbMibCDCGroup.setObjects(*((_B,_J),(_B,_K),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:usbMibCDCGroup.setStatus(_A)
usbMibCDCEtherGroup=ObjectGroup((1,3,6,1,3,103,3,2,3))
usbMibCDCEtherGroup.setObjects(*((_B,_E),(_B,_F),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:usbMibCDCEtherGroup.setStatus(_A)
usbCDCEtherXmtAddressGroup=ObjectGroup((1,3,6,1,3,103,3,2,4))
usbCDCEtherXmtAddressGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:usbCDCEtherXmtAddressGroup.setStatus(_A)
usbMibBasicCompliance=ModuleCompliance((1,3,6,1,3,103,3,1,1))
usbMibBasicCompliance.setObjects(*((_B,_M),(_B,_M),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:usbMibBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'usbMib':usbMib,'usbMibObjects':usbMibObjects,_O:usbNumber,'usbPortTable':usbPortTable,'usbPortEntry':usbPortEntry,_H:usbPortIndex,_P:usbPortType,_Q:usbPortRate,'usbDeviceTable':usbDeviceTable,'usbDeviceEntry':usbDeviceEntry,_I:usbDeviceIndex,_R:usbDevicePower,_S:usbDeviceVendorID,_T:usbDeviceProductID,_U:usbDeviceNumberConfigurations,_V:usbDeviceActiveClass,_W:usbDeviceStatus,_X:usbDeviceEnumCounter,_Y:usbDeviceRemoteWakeup,_Z:usbDeviceRemoteWakeupOn,'usbCDCTable':usbCDCTable,'usbCDCEntry':usbCDCEntry,_J:usbCDCIndex,_K:usbCDCIfIndex,_a:usbCDCSubclass,_b:usbCDCVersion,_c:usbCDCDataTransferType,_d:usbCDCDataEndpoints,_e:usbCDCStalls,'usbCDCEtherTable':usbCDCEtherTable,'usbCDCEtherEntry':usbCDCEtherEntry,_E:usbCDCEtherIndex,_F:usbCDCEtherIfIndex,_f:usbCDCEtherMacAddress,_g:usbCDCEtherPacketFilter,_h:usbCDCEtherDataStatisticsCapabilities,_i:usbCDCEtherDataCheckErrs,'usbCDCEtherXmtAddressTable':usbCDCEtherXmtAddressTable,'usbCDCEtherXmtAddressEntry':usbCDCEtherXmtAddressEntry,_L:ifCDCEtherXmtAddress,'usbMibNotification':usbMibNotification,'usbMibConformance':usbMibConformance,'usbMibCompliances':usbMibCompliances,'usbMibBasicCompliance':usbMibBasicCompliance,'usbMibGroups':usbMibGroups,_M:usbMibBasicGroup,_j:usbMibCDCGroup,_k:usbMibCDCEtherGroup,_l:usbCDCEtherXmtAddressGroup})