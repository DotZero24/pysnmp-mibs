_AN='componentLinkDescrIndication'
_AM='teLinkDescrIndication'
_AL='componentLinkDescrInterfaceMtu'
_AK='teLinkDescrInterfaceMtu'
_AJ='componentLinkBandwidthStorageType'
_AI='componentLinkBandwidthRowStatus'
_AH='componentLinkBandwidthUnreserved'
_AG='componentLinkDescrMaxLspBandwidthPrio7'
_AF='componentLinkDescrMaxLspBandwidthPrio6'
_AE='componentLinkDescrMaxLspBandwidthPrio5'
_AD='componentLinkDescrMaxLspBandwidthPrio4'
_AC='componentLinkDescrMaxLspBandwidthPrio3'
_AB='componentLinkDescrMaxLspBandwidthPrio2'
_AA='componentLinkDescrMaxLspBandwidthPrio1'
_A9='componentLinkDescrMaxLspBandwidthPrio0'
_A8='componentLinkMaxResBandwidth'
_A7='teLinkBandwidthStorageType'
_A6='teLinkBandwidthRowStatus'
_A5='teLinkBandwidthUnreserved'
_A4='teLinkDescrMaxLspBandwidthPrio7'
_A3='teLinkDescrMaxLspBandwidthPrio6'
_A2='teLinkDescrMaxLspBandwidthPrio5'
_A1='teLinkDescrMaxLspBandwidthPrio4'
_A0='teLinkDescrMaxLspBandwidthPrio3'
_z='teLinkDescrMaxLspBandwidthPrio2'
_y='teLinkDescrMaxLspBandwidthPrio1'
_x='teLinkDescrMaxLspBandwidthPrio0'
_w='teLinkMaximumReservableBandwidth'
_v='teLinkSrlgStorageType'
_u='teLinkSrlgRowStatus'
_t='componentLinkDescrStorageType'
_s='componentLinkDescrRowStatus'
_r='componentLinkDescrEncodingType'
_q='componentLinkDescrSwitchingCapability'
_p='componentLinkStorageType'
_o='componentLinkRowStatus'
_n='componentLinkCurrentProtection'
_m='componentLinkPreferredProtection'
_l='teLinkDescrStorageType'
_k='teLinkDescrRowStatus'
_j='teLinkDescrEncodingType'
_i='teLinkDescrSwitchingCapability'
_h='teLinkStorageType'
_g='teLinkRowStatus'
_f='teLinkOutgoingIfId'
_e='teLinkIncomingIfId'
_d='teLinkResourceClass'
_c='teLinkWorkingPriority'
_b='teLinkProtectionType'
_a='teLinkMetric'
_Z='teLinkRemoteIpAddr'
_Y='teLinkLocalIpAddr'
_X='teLinkAddressType'
_W='componentLinkBandwidthPriority'
_V='componentLinkDescrId'
_U='teLinkBandwidthPriority'
_T='teLinkSrlg'
_S='teLinkDescriptorId'
_R='teLinkTdmGroup'
_Q='teLinkPscGroup'
_P='teLinkSrlgGroup'
_O='componentLinkBandwidthGroup'
_N='teLinkBandwidthGroup'
_M='teLinkGroup'
_L='componentLinkDescrMinLspBandwidth'
_K='teLinkDescrMinLspBandwidth'
_J='Integer32'
_I='read-only'
_H='not-accessible'
_G='Unsigned32'
_F='ifIndex'
_E='IF-MIB'
_D='bps'
_C='read-create'
_B='TE-LINK-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndexOrZero',_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
teLinkStdMIB=ModuleIdentity((1,3,6,1,2,1,10,200))
if mibBuilder.loadTexts:teLinkStdMIB.setRevisions(('2005-10-11 00:00',))
class TeLinkBandwidth(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class TeLinkPriority(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class TeLinkProtection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
class TeLinkSwitchingCapability(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,51,100,150,200)));namedValues=NamedValues(*(('packetSwitch1',1),('packetSwitch2',2),('packetSwitch3',3),('packetSwitch4',4),('layer2Switch',51),('tdm',100),('lambdaSwitch',150),('fiberSwitch',200)))
class TeLinkEncodingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,7,8,9,11)));namedValues=NamedValues(*(('packet',1),('ethernet',2),('ansiEtsiPdh',3),('sdhItuSonetAnsi',5),('digitalWrapper',7),('lambda',8),('fiber',9),('fiberChannel',11)))
class TeLinkSonetSdhIndication(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('standard',0),('arbitrary',1)))
_TeLinkNotifications_ObjectIdentity=ObjectIdentity
teLinkNotifications=_TeLinkNotifications_ObjectIdentity((1,3,6,1,2,1,10,200,0))
_TeLinkObjects_ObjectIdentity=ObjectIdentity
teLinkObjects=_TeLinkObjects_ObjectIdentity((1,3,6,1,2,1,10,200,1))
_TeLinkTable_Object=MibTable
teLinkTable=_TeLinkTable_Object((1,3,6,1,2,1,10,200,1,1))
if mibBuilder.loadTexts:teLinkTable.setStatus(_A)
_TeLinkEntry_Object=MibTableRow
teLinkEntry=_TeLinkEntry_Object((1,3,6,1,2,1,10,200,1,1,1))
teLinkEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:teLinkEntry.setStatus(_A)
_TeLinkAddressType_Type=InetAddressType
_TeLinkAddressType_Object=MibTableColumn
teLinkAddressType=_TeLinkAddressType_Object((1,3,6,1,2,1,10,200,1,1,1,1),_TeLinkAddressType_Type())
teLinkAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkAddressType.setStatus(_A)
_TeLinkLocalIpAddr_Type=InetAddress
_TeLinkLocalIpAddr_Object=MibTableColumn
teLinkLocalIpAddr=_TeLinkLocalIpAddr_Object((1,3,6,1,2,1,10,200,1,1,1,2),_TeLinkLocalIpAddr_Type())
teLinkLocalIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkLocalIpAddr.setStatus(_A)
_TeLinkRemoteIpAddr_Type=InetAddress
_TeLinkRemoteIpAddr_Object=MibTableColumn
teLinkRemoteIpAddr=_TeLinkRemoteIpAddr_Object((1,3,6,1,2,1,10,200,1,1,1,3),_TeLinkRemoteIpAddr_Type())
teLinkRemoteIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkRemoteIpAddr.setStatus(_A)
_TeLinkMetric_Type=Unsigned32
_TeLinkMetric_Object=MibTableColumn
teLinkMetric=_TeLinkMetric_Object((1,3,6,1,2,1,10,200,1,1,1,4),_TeLinkMetric_Type())
teLinkMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkMetric.setStatus(_A)
_TeLinkMaximumReservableBandwidth_Type=TeLinkBandwidth
_TeLinkMaximumReservableBandwidth_Object=MibTableColumn
teLinkMaximumReservableBandwidth=_TeLinkMaximumReservableBandwidth_Object((1,3,6,1,2,1,10,200,1,1,1,5),_TeLinkMaximumReservableBandwidth_Type())
teLinkMaximumReservableBandwidth.setMaxAccess(_I)
if mibBuilder.loadTexts:teLinkMaximumReservableBandwidth.setStatus(_A)
if mibBuilder.loadTexts:teLinkMaximumReservableBandwidth.setUnits(_D)
class _TeLinkProtectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('extraTraffic',1),('unprotected',2),('shared',3),('dedicated1For1',4),('dedicated1Plus1',5),('enhanced',6)))
_TeLinkProtectionType_Type.__name__=_J
_TeLinkProtectionType_Object=MibTableColumn
teLinkProtectionType=_TeLinkProtectionType_Object((1,3,6,1,2,1,10,200,1,1,1,6),_TeLinkProtectionType_Type())
teLinkProtectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkProtectionType.setStatus(_A)
_TeLinkWorkingPriority_Type=TeLinkPriority
_TeLinkWorkingPriority_Object=MibTableColumn
teLinkWorkingPriority=_TeLinkWorkingPriority_Object((1,3,6,1,2,1,10,200,1,1,1,7),_TeLinkWorkingPriority_Type())
teLinkWorkingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkWorkingPriority.setStatus(_A)
_TeLinkResourceClass_Type=Unsigned32
_TeLinkResourceClass_Object=MibTableColumn
teLinkResourceClass=_TeLinkResourceClass_Object((1,3,6,1,2,1,10,200,1,1,1,8),_TeLinkResourceClass_Type())
teLinkResourceClass.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkResourceClass.setStatus(_A)
class _TeLinkIncomingIfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TeLinkIncomingIfId_Type.__name__=_J
_TeLinkIncomingIfId_Object=MibTableColumn
teLinkIncomingIfId=_TeLinkIncomingIfId_Object((1,3,6,1,2,1,10,200,1,1,1,9),_TeLinkIncomingIfId_Type())
teLinkIncomingIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkIncomingIfId.setStatus(_A)
_TeLinkOutgoingIfId_Type=InterfaceIndexOrZero
_TeLinkOutgoingIfId_Object=MibTableColumn
teLinkOutgoingIfId=_TeLinkOutgoingIfId_Object((1,3,6,1,2,1,10,200,1,1,1,10),_TeLinkOutgoingIfId_Type())
teLinkOutgoingIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkOutgoingIfId.setStatus(_A)
_TeLinkRowStatus_Type=RowStatus
_TeLinkRowStatus_Object=MibTableColumn
teLinkRowStatus=_TeLinkRowStatus_Object((1,3,6,1,2,1,10,200,1,1,1,11),_TeLinkRowStatus_Type())
teLinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkRowStatus.setStatus(_A)
_TeLinkStorageType_Type=StorageType
_TeLinkStorageType_Object=MibTableColumn
teLinkStorageType=_TeLinkStorageType_Object((1,3,6,1,2,1,10,200,1,1,1,12),_TeLinkStorageType_Type())
teLinkStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkStorageType.setStatus(_A)
_TeLinkDescriptorTable_Object=MibTable
teLinkDescriptorTable=_TeLinkDescriptorTable_Object((1,3,6,1,2,1,10,200,1,2))
if mibBuilder.loadTexts:teLinkDescriptorTable.setStatus(_A)
_TeLinkDescriptorEntry_Object=MibTableRow
teLinkDescriptorEntry=_TeLinkDescriptorEntry_Object((1,3,6,1,2,1,10,200,1,2,1))
teLinkDescriptorEntry.setIndexNames((0,_E,_F),(0,_B,_S))
if mibBuilder.loadTexts:teLinkDescriptorEntry.setStatus(_A)
class _TeLinkDescriptorId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TeLinkDescriptorId_Type.__name__=_G
_TeLinkDescriptorId_Object=MibTableColumn
teLinkDescriptorId=_TeLinkDescriptorId_Object((1,3,6,1,2,1,10,200,1,2,1,1),_TeLinkDescriptorId_Type())
teLinkDescriptorId.setMaxAccess(_H)
if mibBuilder.loadTexts:teLinkDescriptorId.setStatus(_A)
_TeLinkDescrSwitchingCapability_Type=TeLinkSwitchingCapability
_TeLinkDescrSwitchingCapability_Object=MibTableColumn
teLinkDescrSwitchingCapability=_TeLinkDescrSwitchingCapability_Object((1,3,6,1,2,1,10,200,1,2,1,2),_TeLinkDescrSwitchingCapability_Type())
teLinkDescrSwitchingCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrSwitchingCapability.setStatus(_A)
_TeLinkDescrEncodingType_Type=TeLinkEncodingType
_TeLinkDescrEncodingType_Object=MibTableColumn
teLinkDescrEncodingType=_TeLinkDescrEncodingType_Object((1,3,6,1,2,1,10,200,1,2,1,3),_TeLinkDescrEncodingType_Type())
teLinkDescrEncodingType.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrEncodingType.setStatus(_A)
_TeLinkDescrMinLspBandwidth_Type=TeLinkBandwidth
_TeLinkDescrMinLspBandwidth_Object=MibTableColumn
teLinkDescrMinLspBandwidth=_TeLinkDescrMinLspBandwidth_Object((1,3,6,1,2,1,10,200,1,2,1,4),_TeLinkDescrMinLspBandwidth_Type())
teLinkDescrMinLspBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMinLspBandwidth.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMinLspBandwidth.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio0_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio0_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio0=_TeLinkDescrMaxLspBandwidthPrio0_Object((1,3,6,1,2,1,10,200,1,2,1,5),_TeLinkDescrMaxLspBandwidthPrio0_Type())
teLinkDescrMaxLspBandwidthPrio0.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio0.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio0.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio1_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio1_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio1=_TeLinkDescrMaxLspBandwidthPrio1_Object((1,3,6,1,2,1,10,200,1,2,1,6),_TeLinkDescrMaxLspBandwidthPrio1_Type())
teLinkDescrMaxLspBandwidthPrio1.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio1.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio1.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio2_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio2_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio2=_TeLinkDescrMaxLspBandwidthPrio2_Object((1,3,6,1,2,1,10,200,1,2,1,7),_TeLinkDescrMaxLspBandwidthPrio2_Type())
teLinkDescrMaxLspBandwidthPrio2.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio2.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio2.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio3_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio3_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio3=_TeLinkDescrMaxLspBandwidthPrio3_Object((1,3,6,1,2,1,10,200,1,2,1,8),_TeLinkDescrMaxLspBandwidthPrio3_Type())
teLinkDescrMaxLspBandwidthPrio3.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio3.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio3.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio4_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio4_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio4=_TeLinkDescrMaxLspBandwidthPrio4_Object((1,3,6,1,2,1,10,200,1,2,1,9),_TeLinkDescrMaxLspBandwidthPrio4_Type())
teLinkDescrMaxLspBandwidthPrio4.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio4.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio4.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio5_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio5_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio5=_TeLinkDescrMaxLspBandwidthPrio5_Object((1,3,6,1,2,1,10,200,1,2,1,10),_TeLinkDescrMaxLspBandwidthPrio5_Type())
teLinkDescrMaxLspBandwidthPrio5.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio5.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio5.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio6_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio6_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio6=_TeLinkDescrMaxLspBandwidthPrio6_Object((1,3,6,1,2,1,10,200,1,2,1,11),_TeLinkDescrMaxLspBandwidthPrio6_Type())
teLinkDescrMaxLspBandwidthPrio6.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio6.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio6.setUnits(_D)
_TeLinkDescrMaxLspBandwidthPrio7_Type=TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio7_Object=MibTableColumn
teLinkDescrMaxLspBandwidthPrio7=_TeLinkDescrMaxLspBandwidthPrio7_Object((1,3,6,1,2,1,10,200,1,2,1,12),_TeLinkDescrMaxLspBandwidthPrio7_Type())
teLinkDescrMaxLspBandwidthPrio7.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio7.setStatus(_A)
if mibBuilder.loadTexts:teLinkDescrMaxLspBandwidthPrio7.setUnits(_D)
class _TeLinkDescrInterfaceMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TeLinkDescrInterfaceMtu_Type.__name__=_G
_TeLinkDescrInterfaceMtu_Object=MibTableColumn
teLinkDescrInterfaceMtu=_TeLinkDescrInterfaceMtu_Object((1,3,6,1,2,1,10,200,1,2,1,13),_TeLinkDescrInterfaceMtu_Type())
teLinkDescrInterfaceMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrInterfaceMtu.setStatus(_A)
_TeLinkDescrIndication_Type=TeLinkSonetSdhIndication
_TeLinkDescrIndication_Object=MibTableColumn
teLinkDescrIndication=_TeLinkDescrIndication_Object((1,3,6,1,2,1,10,200,1,2,1,14),_TeLinkDescrIndication_Type())
teLinkDescrIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrIndication.setStatus(_A)
_TeLinkDescrRowStatus_Type=RowStatus
_TeLinkDescrRowStatus_Object=MibTableColumn
teLinkDescrRowStatus=_TeLinkDescrRowStatus_Object((1,3,6,1,2,1,10,200,1,2,1,15),_TeLinkDescrRowStatus_Type())
teLinkDescrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrRowStatus.setStatus(_A)
_TeLinkDescrStorageType_Type=StorageType
_TeLinkDescrStorageType_Object=MibTableColumn
teLinkDescrStorageType=_TeLinkDescrStorageType_Object((1,3,6,1,2,1,10,200,1,2,1,16),_TeLinkDescrStorageType_Type())
teLinkDescrStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkDescrStorageType.setStatus(_A)
_TeLinkSrlgTable_Object=MibTable
teLinkSrlgTable=_TeLinkSrlgTable_Object((1,3,6,1,2,1,10,200,1,3))
if mibBuilder.loadTexts:teLinkSrlgTable.setStatus(_A)
_TeLinkSrlgEntry_Object=MibTableRow
teLinkSrlgEntry=_TeLinkSrlgEntry_Object((1,3,6,1,2,1,10,200,1,3,1))
teLinkSrlgEntry.setIndexNames((0,_E,_F),(0,_B,_T))
if mibBuilder.loadTexts:teLinkSrlgEntry.setStatus(_A)
class _TeLinkSrlg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TeLinkSrlg_Type.__name__=_G
_TeLinkSrlg_Object=MibTableColumn
teLinkSrlg=_TeLinkSrlg_Object((1,3,6,1,2,1,10,200,1,3,1,1),_TeLinkSrlg_Type())
teLinkSrlg.setMaxAccess(_H)
if mibBuilder.loadTexts:teLinkSrlg.setStatus(_A)
_TeLinkSrlgRowStatus_Type=RowStatus
_TeLinkSrlgRowStatus_Object=MibTableColumn
teLinkSrlgRowStatus=_TeLinkSrlgRowStatus_Object((1,3,6,1,2,1,10,200,1,3,1,2),_TeLinkSrlgRowStatus_Type())
teLinkSrlgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkSrlgRowStatus.setStatus(_A)
_TeLinkSrlgStorageType_Type=StorageType
_TeLinkSrlgStorageType_Object=MibTableColumn
teLinkSrlgStorageType=_TeLinkSrlgStorageType_Object((1,3,6,1,2,1,10,200,1,3,1,3),_TeLinkSrlgStorageType_Type())
teLinkSrlgStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkSrlgStorageType.setStatus(_A)
_TeLinkBandwidthTable_Object=MibTable
teLinkBandwidthTable=_TeLinkBandwidthTable_Object((1,3,6,1,2,1,10,200,1,4))
if mibBuilder.loadTexts:teLinkBandwidthTable.setStatus(_A)
_TeLinkBandwidthEntry_Object=MibTableRow
teLinkBandwidthEntry=_TeLinkBandwidthEntry_Object((1,3,6,1,2,1,10,200,1,4,1))
teLinkBandwidthEntry.setIndexNames((0,_E,_F),(0,_B,_U))
if mibBuilder.loadTexts:teLinkBandwidthEntry.setStatus(_A)
_TeLinkBandwidthPriority_Type=TeLinkPriority
_TeLinkBandwidthPriority_Object=MibTableColumn
teLinkBandwidthPriority=_TeLinkBandwidthPriority_Object((1,3,6,1,2,1,10,200,1,4,1,1),_TeLinkBandwidthPriority_Type())
teLinkBandwidthPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:teLinkBandwidthPriority.setStatus(_A)
_TeLinkBandwidthUnreserved_Type=TeLinkBandwidth
_TeLinkBandwidthUnreserved_Object=MibTableColumn
teLinkBandwidthUnreserved=_TeLinkBandwidthUnreserved_Object((1,3,6,1,2,1,10,200,1,4,1,2),_TeLinkBandwidthUnreserved_Type())
teLinkBandwidthUnreserved.setMaxAccess(_I)
if mibBuilder.loadTexts:teLinkBandwidthUnreserved.setStatus(_A)
if mibBuilder.loadTexts:teLinkBandwidthUnreserved.setUnits(_D)
_TeLinkBandwidthRowStatus_Type=RowStatus
_TeLinkBandwidthRowStatus_Object=MibTableColumn
teLinkBandwidthRowStatus=_TeLinkBandwidthRowStatus_Object((1,3,6,1,2,1,10,200,1,4,1,3),_TeLinkBandwidthRowStatus_Type())
teLinkBandwidthRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkBandwidthRowStatus.setStatus(_A)
_TeLinkBandwidthStorageType_Type=StorageType
_TeLinkBandwidthStorageType_Object=MibTableColumn
teLinkBandwidthStorageType=_TeLinkBandwidthStorageType_Object((1,3,6,1,2,1,10,200,1,4,1,4),_TeLinkBandwidthStorageType_Type())
teLinkBandwidthStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:teLinkBandwidthStorageType.setStatus(_A)
_ComponentLinkTable_Object=MibTable
componentLinkTable=_ComponentLinkTable_Object((1,3,6,1,2,1,10,200,1,5))
if mibBuilder.loadTexts:componentLinkTable.setStatus(_A)
_ComponentLinkEntry_Object=MibTableRow
componentLinkEntry=_ComponentLinkEntry_Object((1,3,6,1,2,1,10,200,1,5,1))
componentLinkEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:componentLinkEntry.setStatus(_A)
_ComponentLinkMaxResBandwidth_Type=TeLinkBandwidth
_ComponentLinkMaxResBandwidth_Object=MibTableColumn
componentLinkMaxResBandwidth=_ComponentLinkMaxResBandwidth_Object((1,3,6,1,2,1,10,200,1,5,1,1),_ComponentLinkMaxResBandwidth_Type())
componentLinkMaxResBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkMaxResBandwidth.setStatus(_A)
if mibBuilder.loadTexts:componentLinkMaxResBandwidth.setUnits(_D)
_ComponentLinkPreferredProtection_Type=TeLinkProtection
_ComponentLinkPreferredProtection_Object=MibTableColumn
componentLinkPreferredProtection=_ComponentLinkPreferredProtection_Object((1,3,6,1,2,1,10,200,1,5,1,2),_ComponentLinkPreferredProtection_Type())
componentLinkPreferredProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkPreferredProtection.setStatus(_A)
_ComponentLinkCurrentProtection_Type=TeLinkProtection
_ComponentLinkCurrentProtection_Object=MibTableColumn
componentLinkCurrentProtection=_ComponentLinkCurrentProtection_Object((1,3,6,1,2,1,10,200,1,5,1,3),_ComponentLinkCurrentProtection_Type())
componentLinkCurrentProtection.setMaxAccess(_I)
if mibBuilder.loadTexts:componentLinkCurrentProtection.setStatus(_A)
_ComponentLinkRowStatus_Type=RowStatus
_ComponentLinkRowStatus_Object=MibTableColumn
componentLinkRowStatus=_ComponentLinkRowStatus_Object((1,3,6,1,2,1,10,200,1,5,1,4),_ComponentLinkRowStatus_Type())
componentLinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkRowStatus.setStatus(_A)
_ComponentLinkStorageType_Type=StorageType
_ComponentLinkStorageType_Object=MibTableColumn
componentLinkStorageType=_ComponentLinkStorageType_Object((1,3,6,1,2,1,10,200,1,5,1,5),_ComponentLinkStorageType_Type())
componentLinkStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkStorageType.setStatus(_A)
_ComponentLinkDescriptorTable_Object=MibTable
componentLinkDescriptorTable=_ComponentLinkDescriptorTable_Object((1,3,6,1,2,1,10,200,1,6))
if mibBuilder.loadTexts:componentLinkDescriptorTable.setStatus(_A)
_ComponentLinkDescriptorEntry_Object=MibTableRow
componentLinkDescriptorEntry=_ComponentLinkDescriptorEntry_Object((1,3,6,1,2,1,10,200,1,6,1))
componentLinkDescriptorEntry.setIndexNames((0,_E,_F),(0,_B,_V))
if mibBuilder.loadTexts:componentLinkDescriptorEntry.setStatus(_A)
class _ComponentLinkDescrId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ComponentLinkDescrId_Type.__name__=_G
_ComponentLinkDescrId_Object=MibTableColumn
componentLinkDescrId=_ComponentLinkDescrId_Object((1,3,6,1,2,1,10,200,1,6,1,1),_ComponentLinkDescrId_Type())
componentLinkDescrId.setMaxAccess(_H)
if mibBuilder.loadTexts:componentLinkDescrId.setStatus(_A)
_ComponentLinkDescrSwitchingCapability_Type=TeLinkSwitchingCapability
_ComponentLinkDescrSwitchingCapability_Object=MibTableColumn
componentLinkDescrSwitchingCapability=_ComponentLinkDescrSwitchingCapability_Object((1,3,6,1,2,1,10,200,1,6,1,2),_ComponentLinkDescrSwitchingCapability_Type())
componentLinkDescrSwitchingCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrSwitchingCapability.setStatus(_A)
_ComponentLinkDescrEncodingType_Type=TeLinkEncodingType
_ComponentLinkDescrEncodingType_Object=MibTableColumn
componentLinkDescrEncodingType=_ComponentLinkDescrEncodingType_Object((1,3,6,1,2,1,10,200,1,6,1,3),_ComponentLinkDescrEncodingType_Type())
componentLinkDescrEncodingType.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrEncodingType.setStatus(_A)
_ComponentLinkDescrMinLspBandwidth_Type=TeLinkBandwidth
_ComponentLinkDescrMinLspBandwidth_Object=MibTableColumn
componentLinkDescrMinLspBandwidth=_ComponentLinkDescrMinLspBandwidth_Object((1,3,6,1,2,1,10,200,1,6,1,4),_ComponentLinkDescrMinLspBandwidth_Type())
componentLinkDescrMinLspBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMinLspBandwidth.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMinLspBandwidth.setUnits(_D)
_ComponentLinkDescrMaxLspBandwidthPrio0_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio0_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio0=_ComponentLinkDescrMaxLspBandwidthPrio0_Object((1,3,6,1,2,1,10,200,1,6,1,5),_ComponentLinkDescrMaxLspBandwidthPrio0_Type())
componentLinkDescrMaxLspBandwidthPrio0.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio0.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio0.setUnits(_D)
_ComponentLinkDescrMaxLspBandwidthPrio1_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio1_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio1=_ComponentLinkDescrMaxLspBandwidthPrio1_Object((1,3,6,1,2,1,10,200,1,6,1,6),_ComponentLinkDescrMaxLspBandwidthPrio1_Type())
componentLinkDescrMaxLspBandwidthPrio1.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio1.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio1.setUnits(_D)
_ComponentLinkDescrMaxLspBandwidthPrio2_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio2_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio2=_ComponentLinkDescrMaxLspBandwidthPrio2_Object((1,3,6,1,2,1,10,200,1,6,1,7),_ComponentLinkDescrMaxLspBandwidthPrio2_Type())
componentLinkDescrMaxLspBandwidthPrio2.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio2.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio2.setUnits(_D)
_ComponentLinkDescrMaxLspBandwidthPrio3_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio3_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio3=_ComponentLinkDescrMaxLspBandwidthPrio3_Object((1,3,6,1,2,1,10,200,1,6,1,8),_ComponentLinkDescrMaxLspBandwidthPrio3_Type())
componentLinkDescrMaxLspBandwidthPrio3.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio3.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio3.setUnits(_D)
_ComponentLinkDescrMaxLspBandwidthPrio4_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio4_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio4=_ComponentLinkDescrMaxLspBandwidthPrio4_Object((1,3,6,1,2,1,10,200,1,6,1,9),_ComponentLinkDescrMaxLspBandwidthPrio4_Type())
componentLinkDescrMaxLspBandwidthPrio4.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio4.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio4.setUnits(_D)
_ComponentLinkDescrMaxLspBandwidthPrio5_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio5_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio5=_ComponentLinkDescrMaxLspBandwidthPrio5_Object((1,3,6,1,2,1,10,200,1,6,1,10),_ComponentLinkDescrMaxLspBandwidthPrio5_Type())
componentLinkDescrMaxLspBandwidthPrio5.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio5.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio5.setUnits('thousand bps')
_ComponentLinkDescrMaxLspBandwidthPrio6_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio6_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio6=_ComponentLinkDescrMaxLspBandwidthPrio6_Object((1,3,6,1,2,1,10,200,1,6,1,11),_ComponentLinkDescrMaxLspBandwidthPrio6_Type())
componentLinkDescrMaxLspBandwidthPrio6.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio6.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio6.setUnits(_D)
_ComponentLinkDescrMaxLspBandwidthPrio7_Type=TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio7_Object=MibTableColumn
componentLinkDescrMaxLspBandwidthPrio7=_ComponentLinkDescrMaxLspBandwidthPrio7_Object((1,3,6,1,2,1,10,200,1,6,1,12),_ComponentLinkDescrMaxLspBandwidthPrio7_Type())
componentLinkDescrMaxLspBandwidthPrio7.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio7.setStatus(_A)
if mibBuilder.loadTexts:componentLinkDescrMaxLspBandwidthPrio7.setUnits(_D)
class _ComponentLinkDescrInterfaceMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ComponentLinkDescrInterfaceMtu_Type.__name__=_G
_ComponentLinkDescrInterfaceMtu_Object=MibTableColumn
componentLinkDescrInterfaceMtu=_ComponentLinkDescrInterfaceMtu_Object((1,3,6,1,2,1,10,200,1,6,1,13),_ComponentLinkDescrInterfaceMtu_Type())
componentLinkDescrInterfaceMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrInterfaceMtu.setStatus(_A)
_ComponentLinkDescrIndication_Type=TeLinkSonetSdhIndication
_ComponentLinkDescrIndication_Object=MibTableColumn
componentLinkDescrIndication=_ComponentLinkDescrIndication_Object((1,3,6,1,2,1,10,200,1,6,1,14),_ComponentLinkDescrIndication_Type())
componentLinkDescrIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrIndication.setStatus(_A)
_ComponentLinkDescrRowStatus_Type=RowStatus
_ComponentLinkDescrRowStatus_Object=MibTableColumn
componentLinkDescrRowStatus=_ComponentLinkDescrRowStatus_Object((1,3,6,1,2,1,10,200,1,6,1,15),_ComponentLinkDescrRowStatus_Type())
componentLinkDescrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrRowStatus.setStatus(_A)
_ComponentLinkDescrStorageType_Type=StorageType
_ComponentLinkDescrStorageType_Object=MibTableColumn
componentLinkDescrStorageType=_ComponentLinkDescrStorageType_Object((1,3,6,1,2,1,10,200,1,6,1,16),_ComponentLinkDescrStorageType_Type())
componentLinkDescrStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkDescrStorageType.setStatus(_A)
_ComponentLinkBandwidthTable_Object=MibTable
componentLinkBandwidthTable=_ComponentLinkBandwidthTable_Object((1,3,6,1,2,1,10,200,1,7))
if mibBuilder.loadTexts:componentLinkBandwidthTable.setStatus(_A)
_ComponentLinkBandwidthEntry_Object=MibTableRow
componentLinkBandwidthEntry=_ComponentLinkBandwidthEntry_Object((1,3,6,1,2,1,10,200,1,7,1))
componentLinkBandwidthEntry.setIndexNames((0,_E,_F),(0,_B,_W))
if mibBuilder.loadTexts:componentLinkBandwidthEntry.setStatus(_A)
_ComponentLinkBandwidthPriority_Type=TeLinkPriority
_ComponentLinkBandwidthPriority_Object=MibTableColumn
componentLinkBandwidthPriority=_ComponentLinkBandwidthPriority_Object((1,3,6,1,2,1,10,200,1,7,1,1),_ComponentLinkBandwidthPriority_Type())
componentLinkBandwidthPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:componentLinkBandwidthPriority.setStatus(_A)
_ComponentLinkBandwidthUnreserved_Type=TeLinkBandwidth
_ComponentLinkBandwidthUnreserved_Object=MibTableColumn
componentLinkBandwidthUnreserved=_ComponentLinkBandwidthUnreserved_Object((1,3,6,1,2,1,10,200,1,7,1,2),_ComponentLinkBandwidthUnreserved_Type())
componentLinkBandwidthUnreserved.setMaxAccess(_I)
if mibBuilder.loadTexts:componentLinkBandwidthUnreserved.setStatus(_A)
if mibBuilder.loadTexts:componentLinkBandwidthUnreserved.setUnits(_D)
_ComponentLinkBandwidthRowStatus_Type=RowStatus
_ComponentLinkBandwidthRowStatus_Object=MibTableColumn
componentLinkBandwidthRowStatus=_ComponentLinkBandwidthRowStatus_Object((1,3,6,1,2,1,10,200,1,7,1,3),_ComponentLinkBandwidthRowStatus_Type())
componentLinkBandwidthRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkBandwidthRowStatus.setStatus(_A)
_ComponentLinkBandwidthStorageType_Type=StorageType
_ComponentLinkBandwidthStorageType_Object=MibTableColumn
componentLinkBandwidthStorageType=_ComponentLinkBandwidthStorageType_Object((1,3,6,1,2,1,10,200,1,7,1,4),_ComponentLinkBandwidthStorageType_Type())
componentLinkBandwidthStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:componentLinkBandwidthStorageType.setStatus(_A)
_TeLinkConformance_ObjectIdentity=ObjectIdentity
teLinkConformance=_TeLinkConformance_ObjectIdentity((1,3,6,1,2,1,10,200,2))
_TeLinkCompliances_ObjectIdentity=ObjectIdentity
teLinkCompliances=_TeLinkCompliances_ObjectIdentity((1,3,6,1,2,1,10,200,2,1))
_TeLinkGroups_ObjectIdentity=ObjectIdentity
teLinkGroups=_TeLinkGroups_ObjectIdentity((1,3,6,1,2,1,10,200,2,2))
teLinkGroup=ObjectGroup((1,3,6,1,2,1,10,200,2,2,1))
teLinkGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:teLinkGroup.setStatus(_A)
teLinkSrlgGroup=ObjectGroup((1,3,6,1,2,1,10,200,2,2,2))
teLinkSrlgGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:teLinkSrlgGroup.setStatus(_A)
teLinkBandwidthGroup=ObjectGroup((1,3,6,1,2,1,10,200,2,2,3))
teLinkBandwidthGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:teLinkBandwidthGroup.setStatus(_A)
componentLinkBandwidthGroup=ObjectGroup((1,3,6,1,2,1,10,200,2,2,4))
componentLinkBandwidthGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:componentLinkBandwidthGroup.setStatus(_A)
teLinkPscGroup=ObjectGroup((1,3,6,1,2,1,10,200,2,2,5))
teLinkPscGroup.setObjects(*((_B,_K),(_B,_AK),(_B,_L),(_B,_AL)))
if mibBuilder.loadTexts:teLinkPscGroup.setStatus(_A)
teLinkTdmGroup=ObjectGroup((1,3,6,1,2,1,10,200,2,2,6))
teLinkTdmGroup.setObjects(*((_B,_K),(_B,_AM),(_B,_L),(_B,_AN)))
if mibBuilder.loadTexts:teLinkTdmGroup.setStatus(_A)
teLinkModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,200,2,1,1))
teLinkModuleFullCompliance.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:teLinkModuleFullCompliance.setStatus(_A)
teLinkModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,200,2,1,2))
teLinkModuleReadOnlyCompliance.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:teLinkModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TeLinkBandwidth':TeLinkBandwidth,'TeLinkPriority':TeLinkPriority,'TeLinkProtection':TeLinkProtection,'TeLinkSwitchingCapability':TeLinkSwitchingCapability,'TeLinkEncodingType':TeLinkEncodingType,'TeLinkSonetSdhIndication':TeLinkSonetSdhIndication,'teLinkStdMIB':teLinkStdMIB,'teLinkNotifications':teLinkNotifications,'teLinkObjects':teLinkObjects,'teLinkTable':teLinkTable,'teLinkEntry':teLinkEntry,_X:teLinkAddressType,_Y:teLinkLocalIpAddr,_Z:teLinkRemoteIpAddr,_a:teLinkMetric,_w:teLinkMaximumReservableBandwidth,_b:teLinkProtectionType,_c:teLinkWorkingPriority,_d:teLinkResourceClass,_e:teLinkIncomingIfId,_f:teLinkOutgoingIfId,_g:teLinkRowStatus,_h:teLinkStorageType,'teLinkDescriptorTable':teLinkDescriptorTable,'teLinkDescriptorEntry':teLinkDescriptorEntry,_S:teLinkDescriptorId,_i:teLinkDescrSwitchingCapability,_j:teLinkDescrEncodingType,_K:teLinkDescrMinLspBandwidth,_x:teLinkDescrMaxLspBandwidthPrio0,_y:teLinkDescrMaxLspBandwidthPrio1,_z:teLinkDescrMaxLspBandwidthPrio2,_A0:teLinkDescrMaxLspBandwidthPrio3,_A1:teLinkDescrMaxLspBandwidthPrio4,_A2:teLinkDescrMaxLspBandwidthPrio5,_A3:teLinkDescrMaxLspBandwidthPrio6,_A4:teLinkDescrMaxLspBandwidthPrio7,_AK:teLinkDescrInterfaceMtu,_AM:teLinkDescrIndication,_k:teLinkDescrRowStatus,_l:teLinkDescrStorageType,'teLinkSrlgTable':teLinkSrlgTable,'teLinkSrlgEntry':teLinkSrlgEntry,_T:teLinkSrlg,_u:teLinkSrlgRowStatus,_v:teLinkSrlgStorageType,'teLinkBandwidthTable':teLinkBandwidthTable,'teLinkBandwidthEntry':teLinkBandwidthEntry,_U:teLinkBandwidthPriority,_A5:teLinkBandwidthUnreserved,_A6:teLinkBandwidthRowStatus,_A7:teLinkBandwidthStorageType,'componentLinkTable':componentLinkTable,'componentLinkEntry':componentLinkEntry,_A8:componentLinkMaxResBandwidth,_m:componentLinkPreferredProtection,_n:componentLinkCurrentProtection,_o:componentLinkRowStatus,_p:componentLinkStorageType,'componentLinkDescriptorTable':componentLinkDescriptorTable,'componentLinkDescriptorEntry':componentLinkDescriptorEntry,_V:componentLinkDescrId,_q:componentLinkDescrSwitchingCapability,_r:componentLinkDescrEncodingType,_L:componentLinkDescrMinLspBandwidth,_A9:componentLinkDescrMaxLspBandwidthPrio0,_AA:componentLinkDescrMaxLspBandwidthPrio1,_AB:componentLinkDescrMaxLspBandwidthPrio2,_AC:componentLinkDescrMaxLspBandwidthPrio3,_AD:componentLinkDescrMaxLspBandwidthPrio4,_AE:componentLinkDescrMaxLspBandwidthPrio5,_AF:componentLinkDescrMaxLspBandwidthPrio6,_AG:componentLinkDescrMaxLspBandwidthPrio7,_AL:componentLinkDescrInterfaceMtu,_AN:componentLinkDescrIndication,_s:componentLinkDescrRowStatus,_t:componentLinkDescrStorageType,'componentLinkBandwidthTable':componentLinkBandwidthTable,'componentLinkBandwidthEntry':componentLinkBandwidthEntry,_W:componentLinkBandwidthPriority,_AH:componentLinkBandwidthUnreserved,_AI:componentLinkBandwidthRowStatus,_AJ:componentLinkBandwidthStorageType,'teLinkConformance':teLinkConformance,'teLinkCompliances':teLinkCompliances,'teLinkModuleFullCompliance':teLinkModuleFullCompliance,'teLinkModuleReadOnlyCompliance':teLinkModuleReadOnlyCompliance,'teLinkGroups':teLinkGroups,_M:teLinkGroup,_P:teLinkSrlgGroup,_N:teLinkBandwidthGroup,_O:componentLinkBandwidthGroup,_Q:teLinkPscGroup,_R:teLinkTdmGroup})