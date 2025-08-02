_M='futRMTeLinkBandwidthPriority'
_L='futRMTeLinkSrlg'
_K='futRMTeLinkSwDescrMaxBwPriority'
_J='futRMTeLinkSwDescriptorId'
_I='Unsigned32'
_H='not-accessible'
_G='bytes per second'
_F='Integer32'
_E='ARICENT-RM-TE-LINK-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_C,'InterfaceIndexOrZero',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futRMTe=ModuleIdentity((1,3,6,1,4,1,2076,72,10))
if mibBuilder.loadTexts:futRMTe.setRevisions(('2012-09-05 00:00',))
class TeLinkPriority(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class TeLinkEncodingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,7,8,9,11)));namedValues=NamedValues(*(('packet',1),('ethernet',2),('ansiEtsiPdh',3),('sdhItuSonetAnsi',5),('digitalWrapper',7),('lambda',8),('fiber',9),('fiberChannel',11)))
_FutRMTeLinkNotifications_ObjectIdentity=ObjectIdentity
futRMTeLinkNotifications=_FutRMTeLinkNotifications_ObjectIdentity((1,3,6,1,4,1,2076,72,10,0))
_FutRMTeLinkObjects_ObjectIdentity=ObjectIdentity
futRMTeLinkObjects=_FutRMTeLinkObjects_ObjectIdentity((1,3,6,1,4,1,2076,72,10,1))
_FutRmTeLinkGeneralGroup_ObjectIdentity=ObjectIdentity
futRmTeLinkGeneralGroup=_FutRmTeLinkGeneralGroup_ObjectIdentity((1,3,6,1,4,1,2076,72,10,1,1))
class _FutRmTeLinkRegDeregistration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('register',1),('deregister',2)))
_FutRmTeLinkRegDeregistration_Type.__name__=_F
_FutRmTeLinkRegDeregistration_Object=MibScalar
futRmTeLinkRegDeregistration=_FutRmTeLinkRegDeregistration_Object((1,3,6,1,4,1,2076,72,10,1,1,1),_FutRmTeLinkRegDeregistration_Type())
futRmTeLinkRegDeregistration.setMaxAccess('read-write')
if mibBuilder.loadTexts:futRmTeLinkRegDeregistration.setStatus(_A)
_FutRMTeLinkTable_Object=MibTable
futRMTeLinkTable=_FutRMTeLinkTable_Object((1,3,6,1,4,1,2076,72,10,1,2))
if mibBuilder.loadTexts:futRMTeLinkTable.setStatus(_A)
_FutRMTeLinkEntry_Object=MibTableRow
futRMTeLinkEntry=_FutRMTeLinkEntry_Object((1,3,6,1,4,1,2076,72,10,1,2,1))
futRMTeLinkEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:futRMTeLinkEntry.setStatus(_A)
_FutRMTeLinkLocalIpAddr_Type=IpAddress
_FutRMTeLinkLocalIpAddr_Object=MibTableColumn
futRMTeLinkLocalIpAddr=_FutRMTeLinkLocalIpAddr_Object((1,3,6,1,4,1,2076,72,10,1,2,1,1),_FutRMTeLinkLocalIpAddr_Type())
futRMTeLinkLocalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkLocalIpAddr.setStatus(_A)
_FutRMTeLinkRemoteIpAddr_Type=IpAddress
_FutRMTeLinkRemoteIpAddr_Object=MibTableColumn
futRMTeLinkRemoteIpAddr=_FutRMTeLinkRemoteIpAddr_Object((1,3,6,1,4,1,2076,72,10,1,2,1,2),_FutRMTeLinkRemoteIpAddr_Type())
futRMTeLinkRemoteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkRemoteIpAddr.setStatus(_A)
_FutRMTeLinkRemoteRtrId_Type=IpAddress
_FutRMTeLinkRemoteRtrId_Object=MibTableColumn
futRMTeLinkRemoteRtrId=_FutRMTeLinkRemoteRtrId_Object((1,3,6,1,4,1,2076,72,10,1,2,1,3),_FutRMTeLinkRemoteRtrId_Type())
futRMTeLinkRemoteRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkRemoteRtrId.setStatus(_A)
_FutRMTeLinkMetric_Type=Unsigned32
_FutRMTeLinkMetric_Object=MibTableColumn
futRMTeLinkMetric=_FutRMTeLinkMetric_Object((1,3,6,1,4,1,2076,72,10,1,2,1,4),_FutRMTeLinkMetric_Type())
futRMTeLinkMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkMetric.setStatus(_A)
class _FutRMTeLinkProtectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64,128)));namedValues=NamedValues(*(('extraTraffic',1),('unprotected',2),('shared',4),('dedicated1For1',8),('dedicated1Plus1',16),('enhanced',32),('reserved1',64),('reserved2',128)))
_FutRMTeLinkProtectionType_Type.__name__=_F
_FutRMTeLinkProtectionType_Object=MibTableColumn
futRMTeLinkProtectionType=_FutRMTeLinkProtectionType_Object((1,3,6,1,4,1,2076,72,10,1,2,1,5),_FutRMTeLinkProtectionType_Type())
futRMTeLinkProtectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkProtectionType.setStatus(_A)
_FutRMTeLinkResourceClass_Type=Unsigned32
_FutRMTeLinkResourceClass_Object=MibTableColumn
futRMTeLinkResourceClass=_FutRMTeLinkResourceClass_Object((1,3,6,1,4,1,2076,72,10,1,2,1,6),_FutRMTeLinkResourceClass_Type())
futRMTeLinkResourceClass.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkResourceClass.setStatus(_A)
_FutRMTeLinkIncomingIfId_Type=InterfaceIndexOrZero
_FutRMTeLinkIncomingIfId_Object=MibTableColumn
futRMTeLinkIncomingIfId=_FutRMTeLinkIncomingIfId_Object((1,3,6,1,4,1,2076,72,10,1,2,1,7),_FutRMTeLinkIncomingIfId_Type())
futRMTeLinkIncomingIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkIncomingIfId.setStatus(_A)
_FutRMTeLinkOutgoingIfId_Type=InterfaceIndexOrZero
_FutRMTeLinkOutgoingIfId_Object=MibTableColumn
futRMTeLinkOutgoingIfId=_FutRMTeLinkOutgoingIfId_Object((1,3,6,1,4,1,2076,72,10,1,2,1,8),_FutRMTeLinkOutgoingIfId_Type())
futRMTeLinkOutgoingIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkOutgoingIfId.setStatus(_A)
_FutRMTeLinkMaxBw_Type=Unsigned32
_FutRMTeLinkMaxBw_Object=MibTableColumn
futRMTeLinkMaxBw=_FutRMTeLinkMaxBw_Object((1,3,6,1,4,1,2076,72,10,1,2,1,9),_FutRMTeLinkMaxBw_Type())
futRMTeLinkMaxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkMaxBw.setStatus(_A)
if mibBuilder.loadTexts:futRMTeLinkMaxBw.setUnits(_G)
_FutRMTeLinkMaxResBw_Type=Unsigned32
_FutRMTeLinkMaxResBw_Object=MibTableColumn
futRMTeLinkMaxResBw=_FutRMTeLinkMaxResBw_Object((1,3,6,1,4,1,2076,72,10,1,2,1,10),_FutRMTeLinkMaxResBw_Type())
futRMTeLinkMaxResBw.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkMaxResBw.setStatus(_A)
if mibBuilder.loadTexts:futRMTeLinkMaxResBw.setUnits(_G)
_FutRMTeLinkAreaId_Type=Unsigned32
_FutRMTeLinkAreaId_Object=MibTableColumn
futRMTeLinkAreaId=_FutRMTeLinkAreaId_Object((1,3,6,1,4,1,2076,72,10,1,2,1,11),_FutRMTeLinkAreaId_Type())
futRMTeLinkAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkAreaId.setStatus(_A)
class _FutRMTeLinkInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('areaIdInfo',1),('datachannel',2),('dataAndControlChannel',3)))
_FutRMTeLinkInfoType_Type.__name__=_F
_FutRMTeLinkInfoType_Object=MibTableColumn
futRMTeLinkInfoType=_FutRMTeLinkInfoType_Object((1,3,6,1,4,1,2076,72,10,1,2,1,12),_FutRMTeLinkInfoType_Type())
futRMTeLinkInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkInfoType.setStatus(_A)
_FutRMTeLinkRowStatus_Type=RowStatus
_FutRMTeLinkRowStatus_Object=MibTableColumn
futRMTeLinkRowStatus=_FutRMTeLinkRowStatus_Object((1,3,6,1,4,1,2076,72,10,1,2,1,13),_FutRMTeLinkRowStatus_Type())
futRMTeLinkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkRowStatus.setStatus(_A)
_FutRMTeLinkSwDescriptorTable_Object=MibTable
futRMTeLinkSwDescriptorTable=_FutRMTeLinkSwDescriptorTable_Object((1,3,6,1,4,1,2076,72,10,1,3))
if mibBuilder.loadTexts:futRMTeLinkSwDescriptorTable.setStatus(_A)
_FutRMTeLinkSwDescriptorEntry_Object=MibTableRow
futRMTeLinkSwDescriptorEntry=_FutRMTeLinkSwDescriptorEntry_Object((1,3,6,1,4,1,2076,72,10,1,3,1))
futRMTeLinkSwDescriptorEntry.setIndexNames((0,_C,_D),(0,_E,_J))
if mibBuilder.loadTexts:futRMTeLinkSwDescriptorEntry.setStatus(_A)
class _FutRMTeLinkSwDescriptorId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FutRMTeLinkSwDescriptorId_Type.__name__=_I
_FutRMTeLinkSwDescriptorId_Object=MibTableColumn
futRMTeLinkSwDescriptorId=_FutRMTeLinkSwDescriptorId_Object((1,3,6,1,4,1,2076,72,10,1,3,1,1),_FutRMTeLinkSwDescriptorId_Type())
futRMTeLinkSwDescriptorId.setMaxAccess(_H)
if mibBuilder.loadTexts:futRMTeLinkSwDescriptorId.setStatus(_A)
class _FutRMTeLinkSwDescrSwitchingCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,51,100,150,200)));namedValues=NamedValues(*(('psc1',1),('psc2',2),('psc3',3),('psc4',4),('l2sc',51),('tdm',100),('lsc',150),('fsc',200)))
_FutRMTeLinkSwDescrSwitchingCap_Type.__name__=_F
_FutRMTeLinkSwDescrSwitchingCap_Object=MibTableColumn
futRMTeLinkSwDescrSwitchingCap=_FutRMTeLinkSwDescrSwitchingCap_Object((1,3,6,1,4,1,2076,72,10,1,3,1,2),_FutRMTeLinkSwDescrSwitchingCap_Type())
futRMTeLinkSwDescrSwitchingCap.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrSwitchingCap.setStatus(_A)
_FutRMTeLinkSwDescrEncodingType_Type=TeLinkEncodingType
_FutRMTeLinkSwDescrEncodingType_Object=MibTableColumn
futRMTeLinkSwDescrEncodingType=_FutRMTeLinkSwDescrEncodingType_Object((1,3,6,1,4,1,2076,72,10,1,3,1,3),_FutRMTeLinkSwDescrEncodingType_Type())
futRMTeLinkSwDescrEncodingType.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrEncodingType.setStatus(_A)
_FutRMTeLinkSwDescrMinLSPBandwidth_Type=Unsigned32
_FutRMTeLinkSwDescrMinLSPBandwidth_Object=MibTableColumn
futRMTeLinkSwDescrMinLSPBandwidth=_FutRMTeLinkSwDescrMinLSPBandwidth_Object((1,3,6,1,4,1,2076,72,10,1,3,1,4),_FutRMTeLinkSwDescrMinLSPBandwidth_Type())
futRMTeLinkSwDescrMinLSPBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrMinLSPBandwidth.setStatus(_A)
if mibBuilder.loadTexts:futRMTeLinkSwDescrMinLSPBandwidth.setUnits(_G)
_FutRMTeLinkSwDescrMTU_Type=Unsigned32
_FutRMTeLinkSwDescrMTU_Object=MibTableColumn
futRMTeLinkSwDescrMTU=_FutRMTeLinkSwDescrMTU_Object((1,3,6,1,4,1,2076,72,10,1,3,1,5),_FutRMTeLinkSwDescrMTU_Type())
futRMTeLinkSwDescrMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrMTU.setStatus(_A)
_FutRMTeLinkSwDescrIndication_Type=Unsigned32
_FutRMTeLinkSwDescrIndication_Object=MibTableColumn
futRMTeLinkSwDescrIndication=_FutRMTeLinkSwDescrIndication_Object((1,3,6,1,4,1,2076,72,10,1,3,1,6),_FutRMTeLinkSwDescrIndication_Type())
futRMTeLinkSwDescrIndication.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrIndication.setStatus(_A)
_FutRMTeLinkSwDescrRowStatus_Type=RowStatus
_FutRMTeLinkSwDescrRowStatus_Object=MibTableColumn
futRMTeLinkSwDescrRowStatus=_FutRMTeLinkSwDescrRowStatus_Object((1,3,6,1,4,1,2076,72,10,1,3,1,7),_FutRMTeLinkSwDescrRowStatus_Type())
futRMTeLinkSwDescrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrRowStatus.setStatus(_A)
_FutRMTeLinkSwDescrMaxBwTable_Object=MibTable
futRMTeLinkSwDescrMaxBwTable=_FutRMTeLinkSwDescrMaxBwTable_Object((1,3,6,1,4,1,2076,72,10,1,4))
if mibBuilder.loadTexts:futRMTeLinkSwDescrMaxBwTable.setStatus(_A)
_FutRMTeLinkSwDescrMaxBwEntry_Object=MibTableRow
futRMTeLinkSwDescrMaxBwEntry=_FutRMTeLinkSwDescrMaxBwEntry_Object((1,3,6,1,4,1,2076,72,10,1,4,1))
futRMTeLinkSwDescrMaxBwEntry.setIndexNames((0,_C,_D),(0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:futRMTeLinkSwDescrMaxBwEntry.setStatus(_A)
_FutRMTeLinkSwDescrMaxBwPriority_Type=TeLinkPriority
_FutRMTeLinkSwDescrMaxBwPriority_Object=MibTableColumn
futRMTeLinkSwDescrMaxBwPriority=_FutRMTeLinkSwDescrMaxBwPriority_Object((1,3,6,1,4,1,2076,72,10,1,4,1,1),_FutRMTeLinkSwDescrMaxBwPriority_Type())
futRMTeLinkSwDescrMaxBwPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:futRMTeLinkSwDescrMaxBwPriority.setStatus(_A)
_FutRMTeLinkSwDescrMaxLSPBandwidth_Type=Unsigned32
_FutRMTeLinkSwDescrMaxLSPBandwidth_Object=MibTableColumn
futRMTeLinkSwDescrMaxLSPBandwidth=_FutRMTeLinkSwDescrMaxLSPBandwidth_Object((1,3,6,1,4,1,2076,72,10,1,4,1,2),_FutRMTeLinkSwDescrMaxLSPBandwidth_Type())
futRMTeLinkSwDescrMaxLSPBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrMaxLSPBandwidth.setStatus(_A)
if mibBuilder.loadTexts:futRMTeLinkSwDescrMaxLSPBandwidth.setUnits(_G)
_FutRMTeLinkSwDescrMaxBwRowStatus_Type=RowStatus
_FutRMTeLinkSwDescrMaxBwRowStatus_Object=MibTableColumn
futRMTeLinkSwDescrMaxBwRowStatus=_FutRMTeLinkSwDescrMaxBwRowStatus_Object((1,3,6,1,4,1,2076,72,10,1,4,1,3),_FutRMTeLinkSwDescrMaxBwRowStatus_Type())
futRMTeLinkSwDescrMaxBwRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSwDescrMaxBwRowStatus.setStatus(_A)
_FutRMTeLinkSrlgTable_Object=MibTable
futRMTeLinkSrlgTable=_FutRMTeLinkSrlgTable_Object((1,3,6,1,4,1,2076,72,10,1,5))
if mibBuilder.loadTexts:futRMTeLinkSrlgTable.setStatus(_A)
_FutRMTeLinkSrlgEntry_Object=MibTableRow
futRMTeLinkSrlgEntry=_FutRMTeLinkSrlgEntry_Object((1,3,6,1,4,1,2076,72,10,1,5,1))
futRMTeLinkSrlgEntry.setIndexNames((0,_C,_D),(0,_E,_L))
if mibBuilder.loadTexts:futRMTeLinkSrlgEntry.setStatus(_A)
class _FutRMTeLinkSrlg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FutRMTeLinkSrlg_Type.__name__=_I
_FutRMTeLinkSrlg_Object=MibTableColumn
futRMTeLinkSrlg=_FutRMTeLinkSrlg_Object((1,3,6,1,4,1,2076,72,10,1,5,1,1),_FutRMTeLinkSrlg_Type())
futRMTeLinkSrlg.setMaxAccess(_H)
if mibBuilder.loadTexts:futRMTeLinkSrlg.setStatus(_A)
_FutRMTeLinkSrlgRowStatus_Type=RowStatus
_FutRMTeLinkSrlgRowStatus_Object=MibTableColumn
futRMTeLinkSrlgRowStatus=_FutRMTeLinkSrlgRowStatus_Object((1,3,6,1,4,1,2076,72,10,1,5,1,2),_FutRMTeLinkSrlgRowStatus_Type())
futRMTeLinkSrlgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkSrlgRowStatus.setStatus(_A)
_FutRMTeLinkBandwidthTable_Object=MibTable
futRMTeLinkBandwidthTable=_FutRMTeLinkBandwidthTable_Object((1,3,6,1,4,1,2076,72,10,1,6))
if mibBuilder.loadTexts:futRMTeLinkBandwidthTable.setStatus(_A)
_FutRMTeLinkBandwidthEntry_Object=MibTableRow
futRMTeLinkBandwidthEntry=_FutRMTeLinkBandwidthEntry_Object((1,3,6,1,4,1,2076,72,10,1,6,1))
futRMTeLinkBandwidthEntry.setIndexNames((0,_C,_D),(0,_E,_M))
if mibBuilder.loadTexts:futRMTeLinkBandwidthEntry.setStatus(_A)
_FutRMTeLinkBandwidthPriority_Type=TeLinkPriority
_FutRMTeLinkBandwidthPriority_Object=MibTableColumn
futRMTeLinkBandwidthPriority=_FutRMTeLinkBandwidthPriority_Object((1,3,6,1,4,1,2076,72,10,1,6,1,1),_FutRMTeLinkBandwidthPriority_Type())
futRMTeLinkBandwidthPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:futRMTeLinkBandwidthPriority.setStatus(_A)
_FutRMTeLinkUnreservedBandwidth_Type=Unsigned32
_FutRMTeLinkUnreservedBandwidth_Object=MibTableColumn
futRMTeLinkUnreservedBandwidth=_FutRMTeLinkUnreservedBandwidth_Object((1,3,6,1,4,1,2076,72,10,1,6,1,2),_FutRMTeLinkUnreservedBandwidth_Type())
futRMTeLinkUnreservedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkUnreservedBandwidth.setStatus(_A)
if mibBuilder.loadTexts:futRMTeLinkUnreservedBandwidth.setUnits(_G)
_FutRMTeLinkBandwidthRowStatus_Type=RowStatus
_FutRMTeLinkBandwidthRowStatus_Object=MibTableColumn
futRMTeLinkBandwidthRowStatus=_FutRMTeLinkBandwidthRowStatus_Object((1,3,6,1,4,1,2076,72,10,1,6,1,3),_FutRMTeLinkBandwidthRowStatus_Type())
futRMTeLinkBandwidthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:futRMTeLinkBandwidthRowStatus.setStatus(_A)
_FutRMTeLinkConformance_ObjectIdentity=ObjectIdentity
futRMTeLinkConformance=_FutRMTeLinkConformance_ObjectIdentity((1,3,6,1,4,1,2076,72,10,2))
mibBuilder.exportSymbols(_E,**{'TeLinkPriority':TeLinkPriority,'TeLinkEncodingType':TeLinkEncodingType,'futRMTe':futRMTe,'futRMTeLinkNotifications':futRMTeLinkNotifications,'futRMTeLinkObjects':futRMTeLinkObjects,'futRmTeLinkGeneralGroup':futRmTeLinkGeneralGroup,'futRmTeLinkRegDeregistration':futRmTeLinkRegDeregistration,'futRMTeLinkTable':futRMTeLinkTable,'futRMTeLinkEntry':futRMTeLinkEntry,'futRMTeLinkLocalIpAddr':futRMTeLinkLocalIpAddr,'futRMTeLinkRemoteIpAddr':futRMTeLinkRemoteIpAddr,'futRMTeLinkRemoteRtrId':futRMTeLinkRemoteRtrId,'futRMTeLinkMetric':futRMTeLinkMetric,'futRMTeLinkProtectionType':futRMTeLinkProtectionType,'futRMTeLinkResourceClass':futRMTeLinkResourceClass,'futRMTeLinkIncomingIfId':futRMTeLinkIncomingIfId,'futRMTeLinkOutgoingIfId':futRMTeLinkOutgoingIfId,'futRMTeLinkMaxBw':futRMTeLinkMaxBw,'futRMTeLinkMaxResBw':futRMTeLinkMaxResBw,'futRMTeLinkAreaId':futRMTeLinkAreaId,'futRMTeLinkInfoType':futRMTeLinkInfoType,'futRMTeLinkRowStatus':futRMTeLinkRowStatus,'futRMTeLinkSwDescriptorTable':futRMTeLinkSwDescriptorTable,'futRMTeLinkSwDescriptorEntry':futRMTeLinkSwDescriptorEntry,_J:futRMTeLinkSwDescriptorId,'futRMTeLinkSwDescrSwitchingCap':futRMTeLinkSwDescrSwitchingCap,'futRMTeLinkSwDescrEncodingType':futRMTeLinkSwDescrEncodingType,'futRMTeLinkSwDescrMinLSPBandwidth':futRMTeLinkSwDescrMinLSPBandwidth,'futRMTeLinkSwDescrMTU':futRMTeLinkSwDescrMTU,'futRMTeLinkSwDescrIndication':futRMTeLinkSwDescrIndication,'futRMTeLinkSwDescrRowStatus':futRMTeLinkSwDescrRowStatus,'futRMTeLinkSwDescrMaxBwTable':futRMTeLinkSwDescrMaxBwTable,'futRMTeLinkSwDescrMaxBwEntry':futRMTeLinkSwDescrMaxBwEntry,_K:futRMTeLinkSwDescrMaxBwPriority,'futRMTeLinkSwDescrMaxLSPBandwidth':futRMTeLinkSwDescrMaxLSPBandwidth,'futRMTeLinkSwDescrMaxBwRowStatus':futRMTeLinkSwDescrMaxBwRowStatus,'futRMTeLinkSrlgTable':futRMTeLinkSrlgTable,'futRMTeLinkSrlgEntry':futRMTeLinkSrlgEntry,_L:futRMTeLinkSrlg,'futRMTeLinkSrlgRowStatus':futRMTeLinkSrlgRowStatus,'futRMTeLinkBandwidthTable':futRMTeLinkBandwidthTable,'futRMTeLinkBandwidthEntry':futRMTeLinkBandwidthEntry,_M:futRMTeLinkBandwidthPriority,'futRMTeLinkUnreservedBandwidth':futRMTeLinkUnreservedBandwidth,'futRMTeLinkBandwidthRowStatus':futRMTeLinkBandwidthRowStatus,'futRMTeLinkConformance':futRMTeLinkConformance})