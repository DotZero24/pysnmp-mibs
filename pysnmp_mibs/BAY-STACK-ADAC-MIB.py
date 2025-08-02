_K='bsAdacPortOperEnable'
_J='bsAdacPortConfigStatus'
_I='bsAdacMacAddrRangeHighEndIndex'
_H='bsAdacMacAddrRangeLowEndIndex'
_G='bsAdacPortIndex'
_F='not-accessible'
_E='read-only'
_D='BAY-STACK-ADAC-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
PortList,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIdOrNone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackAdacMib=ModuleIdentity((1,3,6,1,4,1,45,5,9))
if mibBuilder.loadTexts:bayStackAdacMib.setRevisions(('2014-04-14 00:00','2009-05-20 00:00','2006-10-16 00:00','2006-05-24 00:00','2006-03-13 00:00','2005-04-12 00:00','2004-12-13 00:00'))
_BsAdacNotifications_ObjectIdentity=ObjectIdentity
bsAdacNotifications=_BsAdacNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,9,0))
_BsAdacObjects_ObjectIdentity=ObjectIdentity
bsAdacObjects=_BsAdacObjects_ObjectIdentity((1,3,6,1,4,1,45,5,9,1))
_BsAdacScalars_ObjectIdentity=ObjectIdentity
bsAdacScalars=_BsAdacScalars_ObjectIdentity((1,3,6,1,4,1,45,5,9,1,1))
_BsAdacAdminEnable_Type=TruthValue
_BsAdacAdminEnable_Object=MibScalar
bsAdacAdminEnable=_BsAdacAdminEnable_Object((1,3,6,1,4,1,45,5,9,1,1,2),_BsAdacAdminEnable_Type())
bsAdacAdminEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacAdminEnable.setStatus(_A)
class _BsAdacOperatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('untaggedFramesBasic',1),('untaggedFramesAdvanced',2),('taggedFrames',3)))
_BsAdacOperatingMode_Type.__name__=_C
_BsAdacOperatingMode_Object=MibScalar
bsAdacOperatingMode=_BsAdacOperatingMode_Object((1,3,6,1,4,1,45,5,9,1,1,3),_BsAdacOperatingMode_Type())
bsAdacOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacOperatingMode.setStatus(_A)
_BsAdacCallServerPort_Type=InterfaceIndexOrZero
_BsAdacCallServerPort_Object=MibScalar
bsAdacCallServerPort=_BsAdacCallServerPort_Object((1,3,6,1,4,1,45,5,9,1,1,4),_BsAdacCallServerPort_Type())
bsAdacCallServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacCallServerPort.setStatus(_A)
_BsAdacUplinkPort_Type=InterfaceIndexOrZero
_BsAdacUplinkPort_Object=MibScalar
bsAdacUplinkPort=_BsAdacUplinkPort_Object((1,3,6,1,4,1,45,5,9,1,1,5),_BsAdacUplinkPort_Type())
bsAdacUplinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacUplinkPort.setStatus(_A)
_BsAdacVoiceVlan_Type=VlanIdOrNone
_BsAdacVoiceVlan_Object=MibScalar
bsAdacVoiceVlan=_BsAdacVoiceVlan_Object((1,3,6,1,4,1,45,5,9,1,1,6),_BsAdacVoiceVlan_Type())
bsAdacVoiceVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacVoiceVlan.setStatus(_A)
_BsAdacNotificationControlEnable_Type=TruthValue
_BsAdacNotificationControlEnable_Object=MibScalar
bsAdacNotificationControlEnable=_BsAdacNotificationControlEnable_Object((1,3,6,1,4,1,45,5,9,1,1,7),_BsAdacNotificationControlEnable_Type())
bsAdacNotificationControlEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacNotificationControlEnable.setStatus(_A)
class _BsAdacMacAddrRangeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('clearTable',2),('defaultTable',3)))
_BsAdacMacAddrRangeControl_Type.__name__=_C
_BsAdacMacAddrRangeControl_Object=MibScalar
bsAdacMacAddrRangeControl=_BsAdacMacAddrRangeControl_Object((1,3,6,1,4,1,45,5,9,1,1,8),_BsAdacMacAddrRangeControl_Type())
bsAdacMacAddrRangeControl.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacMacAddrRangeControl.setStatus(_A)
_BsAdacOperEnable_Type=TruthValue
_BsAdacOperEnable_Object=MibScalar
bsAdacOperEnable=_BsAdacOperEnable_Object((1,3,6,1,4,1,45,5,9,1,1,9),_BsAdacOperEnable_Type())
bsAdacOperEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:bsAdacOperEnable.setStatus(_A)
_BsAdacCallServerPortList_Type=PortList
_BsAdacCallServerPortList_Object=MibScalar
bsAdacCallServerPortList=_BsAdacCallServerPortList_Object((1,3,6,1,4,1,45,5,9,1,1,10),_BsAdacCallServerPortList_Type())
bsAdacCallServerPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacCallServerPortList.setStatus(_A)
_BsAdacUplinkPortList_Type=PortList
_BsAdacUplinkPortList_Object=MibScalar
bsAdacUplinkPortList=_BsAdacUplinkPortList_Object((1,3,6,1,4,1,45,5,9,1,1,11),_BsAdacUplinkPortList_Type())
bsAdacUplinkPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacUplinkPortList.setStatus(_A)
class _BsAdacUplinkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('spbm',2)))
_BsAdacUplinkType_Type.__name__=_C
_BsAdacUplinkType_Object=MibScalar
bsAdacUplinkType=_BsAdacUplinkType_Object((1,3,6,1,4,1,45,5,9,1,1,12),_BsAdacUplinkType_Type())
bsAdacUplinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacUplinkType.setStatus(_A)
_BsAdacPortTable_Object=MibTable
bsAdacPortTable=_BsAdacPortTable_Object((1,3,6,1,4,1,45,5,9,1,2))
if mibBuilder.loadTexts:bsAdacPortTable.setStatus(_A)
_BsAdacPortEntry_Object=MibTableRow
bsAdacPortEntry=_BsAdacPortEntry_Object((1,3,6,1,4,1,45,5,9,1,2,1))
bsAdacPortEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:bsAdacPortEntry.setStatus(_A)
_BsAdacPortIndex_Type=InterfaceIndex
_BsAdacPortIndex_Object=MibTableColumn
bsAdacPortIndex=_BsAdacPortIndex_Object((1,3,6,1,4,1,45,5,9,1,2,1,1),_BsAdacPortIndex_Type())
bsAdacPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsAdacPortIndex.setStatus(_A)
_BsAdacPortAdminEnable_Type=TruthValue
_BsAdacPortAdminEnable_Object=MibTableColumn
bsAdacPortAdminEnable=_BsAdacPortAdminEnable_Object((1,3,6,1,4,1,45,5,9,1,2,1,2),_BsAdacPortAdminEnable_Type())
bsAdacPortAdminEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacPortAdminEnable.setStatus(_A)
class _BsAdacPortConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configApplied',1),('configNotApplied',2)))
_BsAdacPortConfigStatus_Type.__name__=_C
_BsAdacPortConfigStatus_Object=MibTableColumn
bsAdacPortConfigStatus=_BsAdacPortConfigStatus_Object((1,3,6,1,4,1,45,5,9,1,2,1,3),_BsAdacPortConfigStatus_Type())
bsAdacPortConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:bsAdacPortConfigStatus.setStatus(_A)
class _BsAdacPortTaggedFramesPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_BsAdacPortTaggedFramesPvid_Type.__name__=_C
_BsAdacPortTaggedFramesPvid_Object=MibTableColumn
bsAdacPortTaggedFramesPvid=_BsAdacPortTaggedFramesPvid_Object((1,3,6,1,4,1,45,5,9,1,2,1,4),_BsAdacPortTaggedFramesPvid_Type())
bsAdacPortTaggedFramesPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacPortTaggedFramesPvid.setStatus(_A)
class _BsAdacPortTaggedFramesTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tagAll',1),('tagPvidOnly',2),('untagPvidOnly',3),('noChange',4)))
_BsAdacPortTaggedFramesTagging_Type.__name__=_C
_BsAdacPortTaggedFramesTagging_Object=MibTableColumn
bsAdacPortTaggedFramesTagging=_BsAdacPortTaggedFramesTagging_Object((1,3,6,1,4,1,45,5,9,1,2,1,5),_BsAdacPortTaggedFramesTagging_Type())
bsAdacPortTaggedFramesTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacPortTaggedFramesTagging.setStatus(_A)
class _BsAdacPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('telephony',1),('callServer',2),('uplink',3),('other',4)))
_BsAdacPortType_Type.__name__=_C
_BsAdacPortType_Object=MibTableColumn
bsAdacPortType=_BsAdacPortType_Object((1,3,6,1,4,1,45,5,9,1,2,1,6),_BsAdacPortType_Type())
bsAdacPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:bsAdacPortType.setStatus(_A)
_BsAdacPortOperEnable_Type=TruthValue
_BsAdacPortOperEnable_Object=MibTableColumn
bsAdacPortOperEnable=_BsAdacPortOperEnable_Object((1,3,6,1,4,1,45,5,9,1,2,1,7),_BsAdacPortOperEnable_Type())
bsAdacPortOperEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:bsAdacPortOperEnable.setStatus(_A)
_BsAdacPortMacDetectionEnable_Type=TruthValue
_BsAdacPortMacDetectionEnable_Object=MibTableColumn
bsAdacPortMacDetectionEnable=_BsAdacPortMacDetectionEnable_Object((1,3,6,1,4,1,45,5,9,1,2,1,8),_BsAdacPortMacDetectionEnable_Type())
bsAdacPortMacDetectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacPortMacDetectionEnable.setStatus(_A)
_BsAdacPortLldpDetectionEnable_Type=TruthValue
_BsAdacPortLldpDetectionEnable_Object=MibTableColumn
bsAdacPortLldpDetectionEnable=_BsAdacPortLldpDetectionEnable_Object((1,3,6,1,4,1,45,5,9,1,2,1,9),_BsAdacPortLldpDetectionEnable_Type())
bsAdacPortLldpDetectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bsAdacPortLldpDetectionEnable.setStatus(_A)
_BsAdacMacAddrRangeTable_Object=MibTable
bsAdacMacAddrRangeTable=_BsAdacMacAddrRangeTable_Object((1,3,6,1,4,1,45,5,9,1,3))
if mibBuilder.loadTexts:bsAdacMacAddrRangeTable.setStatus(_A)
_BsAdacMacAddrRangeEntry_Object=MibTableRow
bsAdacMacAddrRangeEntry=_BsAdacMacAddrRangeEntry_Object((1,3,6,1,4,1,45,5,9,1,3,1))
bsAdacMacAddrRangeEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:bsAdacMacAddrRangeEntry.setStatus(_A)
_BsAdacMacAddrRangeLowEndIndex_Type=MacAddress
_BsAdacMacAddrRangeLowEndIndex_Object=MibTableColumn
bsAdacMacAddrRangeLowEndIndex=_BsAdacMacAddrRangeLowEndIndex_Object((1,3,6,1,4,1,45,5,9,1,3,1,1),_BsAdacMacAddrRangeLowEndIndex_Type())
bsAdacMacAddrRangeLowEndIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsAdacMacAddrRangeLowEndIndex.setStatus(_A)
_BsAdacMacAddrRangeHighEndIndex_Type=MacAddress
_BsAdacMacAddrRangeHighEndIndex_Object=MibTableColumn
bsAdacMacAddrRangeHighEndIndex=_BsAdacMacAddrRangeHighEndIndex_Object((1,3,6,1,4,1,45,5,9,1,3,1,2),_BsAdacMacAddrRangeHighEndIndex_Type())
bsAdacMacAddrRangeHighEndIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsAdacMacAddrRangeHighEndIndex.setStatus(_A)
_BsAdacMacAddrRangeRowStatus_Type=RowStatus
_BsAdacMacAddrRangeRowStatus_Object=MibTableColumn
bsAdacMacAddrRangeRowStatus=_BsAdacMacAddrRangeRowStatus_Object((1,3,6,1,4,1,45,5,9,1,3,1,3),_BsAdacMacAddrRangeRowStatus_Type())
bsAdacMacAddrRangeRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:bsAdacMacAddrRangeRowStatus.setStatus(_A)
bsAdacPortConfigNotification=NotificationType((1,3,6,1,4,1,45,5,9,0,1))
bsAdacPortConfigNotification.setObjects((_D,_J))
if mibBuilder.loadTexts:bsAdacPortConfigNotification.setStatus(_A)
bsAdacPortOperDisabledNotification=NotificationType((1,3,6,1,4,1,45,5,9,0,2))
bsAdacPortOperDisabledNotification.setObjects((_D,_K))
if mibBuilder.loadTexts:bsAdacPortOperDisabledNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bayStackAdacMib':bayStackAdacMib,'bsAdacNotifications':bsAdacNotifications,'bsAdacPortConfigNotification':bsAdacPortConfigNotification,'bsAdacPortOperDisabledNotification':bsAdacPortOperDisabledNotification,'bsAdacObjects':bsAdacObjects,'bsAdacScalars':bsAdacScalars,'bsAdacAdminEnable':bsAdacAdminEnable,'bsAdacOperatingMode':bsAdacOperatingMode,'bsAdacCallServerPort':bsAdacCallServerPort,'bsAdacUplinkPort':bsAdacUplinkPort,'bsAdacVoiceVlan':bsAdacVoiceVlan,'bsAdacNotificationControlEnable':bsAdacNotificationControlEnable,'bsAdacMacAddrRangeControl':bsAdacMacAddrRangeControl,'bsAdacOperEnable':bsAdacOperEnable,'bsAdacCallServerPortList':bsAdacCallServerPortList,'bsAdacUplinkPortList':bsAdacUplinkPortList,'bsAdacUplinkType':bsAdacUplinkType,'bsAdacPortTable':bsAdacPortTable,'bsAdacPortEntry':bsAdacPortEntry,_G:bsAdacPortIndex,'bsAdacPortAdminEnable':bsAdacPortAdminEnable,_J:bsAdacPortConfigStatus,'bsAdacPortTaggedFramesPvid':bsAdacPortTaggedFramesPvid,'bsAdacPortTaggedFramesTagging':bsAdacPortTaggedFramesTagging,'bsAdacPortType':bsAdacPortType,_K:bsAdacPortOperEnable,'bsAdacPortMacDetectionEnable':bsAdacPortMacDetectionEnable,'bsAdacPortLldpDetectionEnable':bsAdacPortLldpDetectionEnable,'bsAdacMacAddrRangeTable':bsAdacMacAddrRangeTable,'bsAdacMacAddrRangeEntry':bsAdacMacAddrRangeEntry,_H:bsAdacMacAddrRangeLowEndIndex,_I:bsAdacMacAddrRangeHighEndIndex,'bsAdacMacAddrRangeRowStatus':bsAdacMacAddrRangeRowStatus})