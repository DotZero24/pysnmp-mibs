_A5='ntcBbfOIpInConfGrpV1Standard'
_A4='ntcBbfOIpInAlBbfOverIPModNS'
_A3='ntcBbfOIpInAlBbfOverIPDiscont'
_A2='ntcBbfOIpInAlmBufferOverflow'
_A1='ntcBbfOIpInAlmNoInputData'
_A0='ntcBbfOIpInAlmGeneralBbfOverIpIn'
_z='ntcBbfOIpInMonBbfInvSignCountT'
_y='ntcBbfOIpInMonBbfByteCorCountT'
_x='ntcBbfModcodNotSupportedError'
_w='ntcBbfDiscontinuityError'
_v='ntcBbfOverflowError'
_u='ntcBbfOIpInMonBbfNoInpDataError'
_t='ntcBbfOIpInMonBbfInvSignCount'
_s='ntcBbfOIpInMonBbfByteCorCount'
_r='ntcBbfOIpInMonBbfModNS'
_q='ntcBbfOIpInMonBbfDiscontCount'
_p='ntcBbfOIpInMonBbfInvFrameCount'
_o='ntcBbfOIpInMonBbfOverflowCount'
_n='ntcBbfOIpInMonBbfDropCount'
_m='ntcBbfOIpInMonBbfByteOutCount'
_l='ntcBbfOIpInMonBbfOutCount'
_k='ntcBbfOIpInMonBbfInCount'
_j='ntcBbfOIpInMonSourceAddress'
_i='ntcBbfOIpInMonBbfInputBitRate'
_h='ntcBbfOIpInMonBbfModcodNSCountT'
_g='ntcBbfOIpInMonBbfDiscontCountT'
_f='ntcBbfOIpInMonBbfInvFrameCountT'
_e='ntcBbfOIpInMonBbfByteOutCountT'
_d='ntcBbfOIpInMonBbfOverflowCountT'
_c='ntcBbfOIpInMonBbfDropCountT'
_b='ntcBbfOIpInMonBbfOutCountT'
_a='ntcBbfOIpInMonBbfInCountT'
_Z='ntcBbfOIpInMonBbfInputBitRateT'
_Y='ntcBbfOIpInMonCounterReset'
_X='ntcBbfOIpInEpSourceRedundancy'
_W='ntcBbfOIpInEpBbfType'
_V='ntcBbfOIpInEpIpUdpPort'
_U='ntcBbfOIpInEpMulticastAddress'
_T='ntcBbfOIpInIpEpAddressType'
_S='ntcBbfOIpInEpEnable'
_R='ntcConfigurationTableRowStatus'
_Q='ntcBbfOIpInInputSelection'
_P='ntcBbfOIpInEnable'
_O='ntcStreamInx'
_N='ntcMonitoringTableName'
_M='ntcConfigurationTableName'
_L='Unsigned32'
_K='NtcEnable'
_J='not-accessible'
_I='read-write'
_H='bytes'
_G='DisplayString'
_F='Integer32'
_E='read-create'
_D='frames'
_C='read-only'
_B='NEWTEC-BBFOVERIPIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
ntcBbfOverIpIn=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1200))
if mibBuilder.loadTexts:ntcBbfOverIpIn.setRevisions(('2017-07-10 12:00','2014-09-09 09:00','2014-07-15 08:00','2013-09-18 08:00','2013-05-22 06:00','2013-03-27 10:00','2013-01-08 12:00'))
_NtcBbfOIpInObjects_ObjectIdentity=ObjectIdentity
ntcBbfOIpInObjects=_NtcBbfOIpInObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1200,1))
if mibBuilder.loadTexts:ntcBbfOIpInObjects.setStatus(_A)
class _NtcBbfOIpInEnable_Type(NtcEnable):defaultValue=0
_NtcBbfOIpInEnable_Type.__name__=_K
_NtcBbfOIpInEnable_Object=MibScalar
ntcBbfOIpInEnable=_NtcBbfOIpInEnable_Object((1,3,6,1,4,1,5835,5,2,1200,1,1),_NtcBbfOIpInEnable_Type())
ntcBbfOIpInEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcBbfOIpInEnable.setStatus(_A)
class _NtcBbfOIpInInputSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('data1',2),('data2',3),('data',4),('any',5)))
_NtcBbfOIpInInputSelection_Type.__name__=_F
_NtcBbfOIpInInputSelection_Object=MibScalar
ntcBbfOIpInInputSelection=_NtcBbfOIpInInputSelection_Object((1,3,6,1,4,1,5835,5,2,1200,1,2),_NtcBbfOIpInInputSelection_Type())
ntcBbfOIpInInputSelection.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcBbfOIpInInputSelection.setStatus(_A)
_NtcConfigurationTableTable_Object=MibTable
ntcConfigurationTableTable=_NtcConfigurationTableTable_Object((1,3,6,1,4,1,5835,5,2,1200,1,3))
if mibBuilder.loadTexts:ntcConfigurationTableTable.setStatus(_A)
_NtcConfigurationTableEntry_Object=MibTableRow
ntcConfigurationTableEntry=_NtcConfigurationTableEntry_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1))
ntcConfigurationTableEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ntcConfigurationTableEntry.setStatus(_A)
class _NtcConfigurationTableName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NtcConfigurationTableName_Type.__name__=_G
_NtcConfigurationTableName_Object=MibTableColumn
ntcConfigurationTableName=_NtcConfigurationTableName_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,1),_NtcConfigurationTableName_Type())
ntcConfigurationTableName.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcConfigurationTableName.setStatus(_A)
_NtcConfigurationTableRowStatus_Type=RowStatus
_NtcConfigurationTableRowStatus_Object=MibTableColumn
ntcConfigurationTableRowStatus=_NtcConfigurationTableRowStatus_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,2),_NtcConfigurationTableRowStatus_Type())
ntcConfigurationTableRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcConfigurationTableRowStatus.setStatus(_A)
_NtcBbfOIpInEpEnable_Type=NtcEnable
_NtcBbfOIpInEpEnable_Object=MibTableColumn
ntcBbfOIpInEpEnable=_NtcBbfOIpInEpEnable_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,3),_NtcBbfOIpInEpEnable_Type())
ntcBbfOIpInEpEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcBbfOIpInEpEnable.setStatus(_A)
class _NtcBbfOIpInIpEpAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unicast',0),('multicast',1)))
_NtcBbfOIpInIpEpAddressType_Type.__name__=_F
_NtcBbfOIpInIpEpAddressType_Object=MibTableColumn
ntcBbfOIpInIpEpAddressType=_NtcBbfOIpInIpEpAddressType_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,4),_NtcBbfOIpInIpEpAddressType_Type())
ntcBbfOIpInIpEpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcBbfOIpInIpEpAddressType.setStatus(_A)
_NtcBbfOIpInEpMulticastAddress_Type=IpAddress
_NtcBbfOIpInEpMulticastAddress_Object=MibTableColumn
ntcBbfOIpInEpMulticastAddress=_NtcBbfOIpInEpMulticastAddress_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,5),_NtcBbfOIpInEpMulticastAddress_Type())
ntcBbfOIpInEpMulticastAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcBbfOIpInEpMulticastAddress.setStatus(_A)
class _NtcBbfOIpInEpIpUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcBbfOIpInEpIpUdpPort_Type.__name__=_L
_NtcBbfOIpInEpIpUdpPort_Object=MibTableColumn
ntcBbfOIpInEpIpUdpPort=_NtcBbfOIpInEpIpUdpPort_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,6),_NtcBbfOIpInEpIpUdpPort_Type())
ntcBbfOIpInEpIpUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcBbfOIpInEpIpUdpPort.setStatus(_A)
class _NtcBbfOIpInEpBbfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dvbbbf',0),('ntcbbf',1)))
_NtcBbfOIpInEpBbfType_Type.__name__=_F
_NtcBbfOIpInEpBbfType_Object=MibTableColumn
ntcBbfOIpInEpBbfType=_NtcBbfOIpInEpBbfType_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,7),_NtcBbfOIpInEpBbfType_Type())
ntcBbfOIpInEpBbfType.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcBbfOIpInEpBbfType.setStatus(_A)
_NtcBbfOIpInEpSourceRedundancy_Type=NtcEnable
_NtcBbfOIpInEpSourceRedundancy_Object=MibTableColumn
ntcBbfOIpInEpSourceRedundancy=_NtcBbfOIpInEpSourceRedundancy_Object((1,3,6,1,4,1,5835,5,2,1200,1,3,1,8),_NtcBbfOIpInEpSourceRedundancy_Type())
ntcBbfOIpInEpSourceRedundancy.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcBbfOIpInEpSourceRedundancy.setStatus(_A)
_NtcBbfOIpInMonitor_ObjectIdentity=ObjectIdentity
ntcBbfOIpInMonitor=_NtcBbfOIpInMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1200,1,4))
if mibBuilder.loadTexts:ntcBbfOIpInMonitor.setStatus(_A)
class _NtcBbfOIpInMonCounterReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcBbfOIpInMonCounterReset_Type.__name__=_F
_NtcBbfOIpInMonCounterReset_Object=MibScalar
ntcBbfOIpInMonCounterReset=_NtcBbfOIpInMonCounterReset_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,1),_NtcBbfOIpInMonCounterReset_Type())
ntcBbfOIpInMonCounterReset.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcBbfOIpInMonCounterReset.setStatus(_A)
_NtcBbfOIpInMonBbfInputBitRateT_Type=Unsigned32
_NtcBbfOIpInMonBbfInputBitRateT_Object=MibScalar
ntcBbfOIpInMonBbfInputBitRateT=_NtcBbfOIpInMonBbfInputBitRateT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,2),_NtcBbfOIpInMonBbfInputBitRateT_Type())
ntcBbfOIpInMonBbfInputBitRateT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInputBitRateT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInputBitRateT.setUnits('bps')
_NtcBbfOIpInMonBbfInCountT_Type=Counter32
_NtcBbfOIpInMonBbfInCountT_Object=MibScalar
ntcBbfOIpInMonBbfInCountT=_NtcBbfOIpInMonBbfInCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,3),_NtcBbfOIpInMonBbfInCountT_Type())
ntcBbfOIpInMonBbfInCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInCountT.setUnits(_D)
_NtcBbfOIpInMonBbfOutCountT_Type=Counter32
_NtcBbfOIpInMonBbfOutCountT_Object=MibScalar
ntcBbfOIpInMonBbfOutCountT=_NtcBbfOIpInMonBbfOutCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,4),_NtcBbfOIpInMonBbfOutCountT_Type())
ntcBbfOIpInMonBbfOutCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOutCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOutCountT.setUnits(_D)
_NtcBbfOIpInMonBbfDropCountT_Type=Counter32
_NtcBbfOIpInMonBbfDropCountT_Object=MibScalar
ntcBbfOIpInMonBbfDropCountT=_NtcBbfOIpInMonBbfDropCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,5),_NtcBbfOIpInMonBbfDropCountT_Type())
ntcBbfOIpInMonBbfDropCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDropCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDropCountT.setUnits(_D)
_NtcBbfOIpInMonBbfOverflowCountT_Type=Counter32
_NtcBbfOIpInMonBbfOverflowCountT_Object=MibScalar
ntcBbfOIpInMonBbfOverflowCountT=_NtcBbfOIpInMonBbfOverflowCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,6),_NtcBbfOIpInMonBbfOverflowCountT_Type())
ntcBbfOIpInMonBbfOverflowCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOverflowCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOverflowCountT.setUnits(_D)
_NtcBbfOIpInMonBbfByteOutCountT_Type=Counter32
_NtcBbfOIpInMonBbfByteOutCountT_Object=MibScalar
ntcBbfOIpInMonBbfByteOutCountT=_NtcBbfOIpInMonBbfByteOutCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,7),_NtcBbfOIpInMonBbfByteOutCountT_Type())
ntcBbfOIpInMonBbfByteOutCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteOutCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteOutCountT.setUnits(_H)
_NtcBbfOIpInMonBbfInvFrameCountT_Type=Counter32
_NtcBbfOIpInMonBbfInvFrameCountT_Object=MibScalar
ntcBbfOIpInMonBbfInvFrameCountT=_NtcBbfOIpInMonBbfInvFrameCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,8),_NtcBbfOIpInMonBbfInvFrameCountT_Type())
ntcBbfOIpInMonBbfInvFrameCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvFrameCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvFrameCountT.setUnits(_D)
_NtcBbfOIpInMonBbfDiscontCountT_Type=Counter32
_NtcBbfOIpInMonBbfDiscontCountT_Object=MibScalar
ntcBbfOIpInMonBbfDiscontCountT=_NtcBbfOIpInMonBbfDiscontCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,9),_NtcBbfOIpInMonBbfDiscontCountT_Type())
ntcBbfOIpInMonBbfDiscontCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDiscontCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDiscontCountT.setUnits(_D)
_NtcBbfOIpInMonBbfModcodNSCountT_Type=Counter32
_NtcBbfOIpInMonBbfModcodNSCountT_Object=MibScalar
ntcBbfOIpInMonBbfModcodNSCountT=_NtcBbfOIpInMonBbfModcodNSCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,10),_NtcBbfOIpInMonBbfModcodNSCountT_Type())
ntcBbfOIpInMonBbfModcodNSCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfModcodNSCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfModcodNSCountT.setUnits(_D)
_NtcMonitoringTableTable_Object=MibTable
ntcMonitoringTableTable=_NtcMonitoringTableTable_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11))
if mibBuilder.loadTexts:ntcMonitoringTableTable.setStatus(_A)
_NtcMonitoringTableEntry_Object=MibTableRow
ntcMonitoringTableEntry=_NtcMonitoringTableEntry_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1))
ntcMonitoringTableEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ntcMonitoringTableEntry.setStatus(_A)
class _NtcMonitoringTableName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcMonitoringTableName_Type.__name__=_G
_NtcMonitoringTableName_Object=MibTableColumn
ntcMonitoringTableName=_NtcMonitoringTableName_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,1),_NtcMonitoringTableName_Type())
ntcMonitoringTableName.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcMonitoringTableName.setStatus(_A)
_NtcBbfOIpInMonBbfInputBitRate_Type=Unsigned32
_NtcBbfOIpInMonBbfInputBitRate_Object=MibTableColumn
ntcBbfOIpInMonBbfInputBitRate=_NtcBbfOIpInMonBbfInputBitRate_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,2),_NtcBbfOIpInMonBbfInputBitRate_Type())
ntcBbfOIpInMonBbfInputBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInputBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInputBitRate.setUnits('bps')
class _NtcBbfOIpInMonSourceAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcBbfOIpInMonSourceAddress_Type.__name__=_G
_NtcBbfOIpInMonSourceAddress_Object=MibTableColumn
ntcBbfOIpInMonSourceAddress=_NtcBbfOIpInMonSourceAddress_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,3),_NtcBbfOIpInMonSourceAddress_Type())
ntcBbfOIpInMonSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonSourceAddress.setStatus(_A)
_NtcBbfOIpInMonBbfInCount_Type=Counter32
_NtcBbfOIpInMonBbfInCount_Object=MibTableColumn
ntcBbfOIpInMonBbfInCount=_NtcBbfOIpInMonBbfInCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,4),_NtcBbfOIpInMonBbfInCount_Type())
ntcBbfOIpInMonBbfInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInCount.setUnits(_D)
_NtcBbfOIpInMonBbfOutCount_Type=Counter32
_NtcBbfOIpInMonBbfOutCount_Object=MibTableColumn
ntcBbfOIpInMonBbfOutCount=_NtcBbfOIpInMonBbfOutCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,5),_NtcBbfOIpInMonBbfOutCount_Type())
ntcBbfOIpInMonBbfOutCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOutCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOutCount.setUnits(_D)
_NtcBbfOIpInMonBbfByteOutCount_Type=Counter32
_NtcBbfOIpInMonBbfByteOutCount_Object=MibTableColumn
ntcBbfOIpInMonBbfByteOutCount=_NtcBbfOIpInMonBbfByteOutCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,6),_NtcBbfOIpInMonBbfByteOutCount_Type())
ntcBbfOIpInMonBbfByteOutCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteOutCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteOutCount.setUnits(_H)
_NtcBbfOIpInMonBbfDropCount_Type=Counter32
_NtcBbfOIpInMonBbfDropCount_Object=MibTableColumn
ntcBbfOIpInMonBbfDropCount=_NtcBbfOIpInMonBbfDropCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,7),_NtcBbfOIpInMonBbfDropCount_Type())
ntcBbfOIpInMonBbfDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDropCount.setUnits(_D)
_NtcBbfOIpInMonBbfOverflowCount_Type=Counter32
_NtcBbfOIpInMonBbfOverflowCount_Object=MibTableColumn
ntcBbfOIpInMonBbfOverflowCount=_NtcBbfOIpInMonBbfOverflowCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,8),_NtcBbfOIpInMonBbfOverflowCount_Type())
ntcBbfOIpInMonBbfOverflowCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOverflowCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfOverflowCount.setUnits(_D)
_NtcBbfOIpInMonBbfInvFrameCount_Type=Counter32
_NtcBbfOIpInMonBbfInvFrameCount_Object=MibTableColumn
ntcBbfOIpInMonBbfInvFrameCount=_NtcBbfOIpInMonBbfInvFrameCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,9),_NtcBbfOIpInMonBbfInvFrameCount_Type())
ntcBbfOIpInMonBbfInvFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvFrameCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvFrameCount.setUnits(_D)
_NtcBbfOIpInMonBbfDiscontCount_Type=Counter32
_NtcBbfOIpInMonBbfDiscontCount_Object=MibTableColumn
ntcBbfOIpInMonBbfDiscontCount=_NtcBbfOIpInMonBbfDiscontCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,10),_NtcBbfOIpInMonBbfDiscontCount_Type())
ntcBbfOIpInMonBbfDiscontCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDiscontCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfDiscontCount.setUnits(_D)
_NtcBbfOIpInMonBbfModNS_Type=Counter32
_NtcBbfOIpInMonBbfModNS_Object=MibTableColumn
ntcBbfOIpInMonBbfModNS=_NtcBbfOIpInMonBbfModNS_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,11),_NtcBbfOIpInMonBbfModNS_Type())
ntcBbfOIpInMonBbfModNS.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfModNS.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfModNS.setUnits(_D)
_NtcBbfOIpInMonBbfByteCorCount_Type=Counter32
_NtcBbfOIpInMonBbfByteCorCount_Object=MibTableColumn
ntcBbfOIpInMonBbfByteCorCount=_NtcBbfOIpInMonBbfByteCorCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,12),_NtcBbfOIpInMonBbfByteCorCount_Type())
ntcBbfOIpInMonBbfByteCorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteCorCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteCorCount.setUnits(_H)
_NtcBbfOIpInMonBbfInvSignCount_Type=Counter32
_NtcBbfOIpInMonBbfInvSignCount_Object=MibTableColumn
ntcBbfOIpInMonBbfInvSignCount=_NtcBbfOIpInMonBbfInvSignCount_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,11,1,13),_NtcBbfOIpInMonBbfInvSignCount_Type())
ntcBbfOIpInMonBbfInvSignCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvSignCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvSignCount.setUnits(_D)
_NtcAlarmStatusTableTable_Object=MibTable
ntcAlarmStatusTableTable=_NtcAlarmStatusTableTable_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,12))
if mibBuilder.loadTexts:ntcAlarmStatusTableTable.setStatus(_A)
_NtcAlarmStatusTableEntry_Object=MibTableRow
ntcAlarmStatusTableEntry=_NtcAlarmStatusTableEntry_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,12,1))
ntcAlarmStatusTableEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ntcAlarmStatusTableEntry.setStatus(_A)
class _NtcStreamInx_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcStreamInx_Type.__name__=_G
_NtcStreamInx_Object=MibTableColumn
ntcStreamInx=_NtcStreamInx_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,12,1,1),_NtcStreamInx_Type())
ntcStreamInx.setMaxAccess(_J)
if mibBuilder.loadTexts:ntcStreamInx.setStatus(_A)
_NtcBbfOIpInMonBbfNoInpDataError_Type=NtcAlarmState
_NtcBbfOIpInMonBbfNoInpDataError_Object=MibTableColumn
ntcBbfOIpInMonBbfNoInpDataError=_NtcBbfOIpInMonBbfNoInpDataError_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,12,1,2),_NtcBbfOIpInMonBbfNoInpDataError_Type())
ntcBbfOIpInMonBbfNoInpDataError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfNoInpDataError.setStatus(_A)
_NtcBbfOverflowError_Type=NtcAlarmState
_NtcBbfOverflowError_Object=MibTableColumn
ntcBbfOverflowError=_NtcBbfOverflowError_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,12,1,3),_NtcBbfOverflowError_Type())
ntcBbfOverflowError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOverflowError.setStatus(_A)
_NtcBbfDiscontinuityError_Type=NtcAlarmState
_NtcBbfDiscontinuityError_Object=MibTableColumn
ntcBbfDiscontinuityError=_NtcBbfDiscontinuityError_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,12,1,4),_NtcBbfDiscontinuityError_Type())
ntcBbfDiscontinuityError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfDiscontinuityError.setStatus(_A)
_NtcBbfModcodNotSupportedError_Type=NtcAlarmState
_NtcBbfModcodNotSupportedError_Object=MibTableColumn
ntcBbfModcodNotSupportedError=_NtcBbfModcodNotSupportedError_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,12,1,5),_NtcBbfModcodNotSupportedError_Type())
ntcBbfModcodNotSupportedError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfModcodNotSupportedError.setStatus(_A)
_NtcBbfOIpInMonBbfByteCorCountT_Type=Counter32
_NtcBbfOIpInMonBbfByteCorCountT_Object=MibScalar
ntcBbfOIpInMonBbfByteCorCountT=_NtcBbfOIpInMonBbfByteCorCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,13),_NtcBbfOIpInMonBbfByteCorCountT_Type())
ntcBbfOIpInMonBbfByteCorCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteCorCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfByteCorCountT.setUnits(_H)
_NtcBbfOIpInMonBbfInvSignCountT_Type=Counter32
_NtcBbfOIpInMonBbfInvSignCountT_Object=MibScalar
ntcBbfOIpInMonBbfInvSignCountT=_NtcBbfOIpInMonBbfInvSignCountT_Object((1,3,6,1,4,1,5835,5,2,1200,1,4,14),_NtcBbfOIpInMonBbfInvSignCountT_Type())
ntcBbfOIpInMonBbfInvSignCountT.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvSignCountT.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpInMonBbfInvSignCountT.setUnits(_D)
_NtcBbfOIpInAlarm_ObjectIdentity=ObjectIdentity
ntcBbfOIpInAlarm=_NtcBbfOIpInAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1200,1,5))
if mibBuilder.loadTexts:ntcBbfOIpInAlarm.setStatus(_A)
_NtcBbfOIpInAlmGeneralBbfOverIpIn_Type=NtcAlarmState
_NtcBbfOIpInAlmGeneralBbfOverIpIn_Object=MibScalar
ntcBbfOIpInAlmGeneralBbfOverIpIn=_NtcBbfOIpInAlmGeneralBbfOverIpIn_Object((1,3,6,1,4,1,5835,5,2,1200,1,5,1),_NtcBbfOIpInAlmGeneralBbfOverIpIn_Type())
ntcBbfOIpInAlmGeneralBbfOverIpIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInAlmGeneralBbfOverIpIn.setStatus(_A)
_NtcBbfOIpInAlmNoInputData_Type=NtcAlarmState
_NtcBbfOIpInAlmNoInputData_Object=MibScalar
ntcBbfOIpInAlmNoInputData=_NtcBbfOIpInAlmNoInputData_Object((1,3,6,1,4,1,5835,5,2,1200,1,5,2),_NtcBbfOIpInAlmNoInputData_Type())
ntcBbfOIpInAlmNoInputData.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInAlmNoInputData.setStatus(_A)
_NtcBbfOIpInAlmBufferOverflow_Type=NtcAlarmState
_NtcBbfOIpInAlmBufferOverflow_Object=MibScalar
ntcBbfOIpInAlmBufferOverflow=_NtcBbfOIpInAlmBufferOverflow_Object((1,3,6,1,4,1,5835,5,2,1200,1,5,3),_NtcBbfOIpInAlmBufferOverflow_Type())
ntcBbfOIpInAlmBufferOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInAlmBufferOverflow.setStatus(_A)
_NtcBbfOIpInAlBbfOverIPDiscont_Type=NtcAlarmState
_NtcBbfOIpInAlBbfOverIPDiscont_Object=MibScalar
ntcBbfOIpInAlBbfOverIPDiscont=_NtcBbfOIpInAlBbfOverIPDiscont_Object((1,3,6,1,4,1,5835,5,2,1200,1,5,4),_NtcBbfOIpInAlBbfOverIPDiscont_Type())
ntcBbfOIpInAlBbfOverIPDiscont.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInAlBbfOverIPDiscont.setStatus(_A)
_NtcBbfOIpInAlBbfOverIPModNS_Type=NtcAlarmState
_NtcBbfOIpInAlBbfOverIPModNS_Object=MibScalar
ntcBbfOIpInAlBbfOverIPModNS=_NtcBbfOIpInAlBbfOverIPModNS_Object((1,3,6,1,4,1,5835,5,2,1200,1,5,5),_NtcBbfOIpInAlBbfOverIPModNS_Type())
ntcBbfOIpInAlBbfOverIPModNS.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpInAlBbfOverIPModNS.setStatus(_A)
_NtcBbfOIpInConformance_ObjectIdentity=ObjectIdentity
ntcBbfOIpInConformance=_NtcBbfOIpInConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1200,2))
if mibBuilder.loadTexts:ntcBbfOIpInConformance.setStatus(_A)
_NtcBbfOIpInConfCompliance_ObjectIdentity=ObjectIdentity
ntcBbfOIpInConfCompliance=_NtcBbfOIpInConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1200,2,1))
if mibBuilder.loadTexts:ntcBbfOIpInConfCompliance.setStatus(_A)
_NtcBbfOIpInConfGroup_ObjectIdentity=ObjectIdentity
ntcBbfOIpInConfGroup=_NtcBbfOIpInConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1200,2,2))
if mibBuilder.loadTexts:ntcBbfOIpInConfGroup.setStatus(_A)
ntcBbfOIpInConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1200,2,2,1))
ntcBbfOIpInConfGrpV1Standard.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ntcBbfOIpInConfGrpV1Standard.setStatus(_A)
ntcBbfOIpInConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1200,2,1,1))
ntcBbfOIpInConfCompV1Standard.setObjects((_B,_A5))
if mibBuilder.loadTexts:ntcBbfOIpInConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcBbfOverIpIn':ntcBbfOverIpIn,'ntcBbfOIpInObjects':ntcBbfOIpInObjects,_P:ntcBbfOIpInEnable,_Q:ntcBbfOIpInInputSelection,'ntcConfigurationTableTable':ntcConfigurationTableTable,'ntcConfigurationTableEntry':ntcConfigurationTableEntry,_M:ntcConfigurationTableName,_R:ntcConfigurationTableRowStatus,_S:ntcBbfOIpInEpEnable,_T:ntcBbfOIpInIpEpAddressType,_U:ntcBbfOIpInEpMulticastAddress,_V:ntcBbfOIpInEpIpUdpPort,_W:ntcBbfOIpInEpBbfType,_X:ntcBbfOIpInEpSourceRedundancy,'ntcBbfOIpInMonitor':ntcBbfOIpInMonitor,_Y:ntcBbfOIpInMonCounterReset,_Z:ntcBbfOIpInMonBbfInputBitRateT,_a:ntcBbfOIpInMonBbfInCountT,_b:ntcBbfOIpInMonBbfOutCountT,_c:ntcBbfOIpInMonBbfDropCountT,_d:ntcBbfOIpInMonBbfOverflowCountT,_e:ntcBbfOIpInMonBbfByteOutCountT,_f:ntcBbfOIpInMonBbfInvFrameCountT,_g:ntcBbfOIpInMonBbfDiscontCountT,_h:ntcBbfOIpInMonBbfModcodNSCountT,'ntcMonitoringTableTable':ntcMonitoringTableTable,'ntcMonitoringTableEntry':ntcMonitoringTableEntry,_N:ntcMonitoringTableName,_i:ntcBbfOIpInMonBbfInputBitRate,_j:ntcBbfOIpInMonSourceAddress,_k:ntcBbfOIpInMonBbfInCount,_l:ntcBbfOIpInMonBbfOutCount,_m:ntcBbfOIpInMonBbfByteOutCount,_n:ntcBbfOIpInMonBbfDropCount,_o:ntcBbfOIpInMonBbfOverflowCount,_p:ntcBbfOIpInMonBbfInvFrameCount,_q:ntcBbfOIpInMonBbfDiscontCount,_r:ntcBbfOIpInMonBbfModNS,_s:ntcBbfOIpInMonBbfByteCorCount,_t:ntcBbfOIpInMonBbfInvSignCount,'ntcAlarmStatusTableTable':ntcAlarmStatusTableTable,'ntcAlarmStatusTableEntry':ntcAlarmStatusTableEntry,_O:ntcStreamInx,_u:ntcBbfOIpInMonBbfNoInpDataError,_v:ntcBbfOverflowError,_w:ntcBbfDiscontinuityError,_x:ntcBbfModcodNotSupportedError,_y:ntcBbfOIpInMonBbfByteCorCountT,_z:ntcBbfOIpInMonBbfInvSignCountT,'ntcBbfOIpInAlarm':ntcBbfOIpInAlarm,_A0:ntcBbfOIpInAlmGeneralBbfOverIpIn,_A1:ntcBbfOIpInAlmNoInputData,_A2:ntcBbfOIpInAlmBufferOverflow,_A3:ntcBbfOIpInAlBbfOverIPDiscont,_A4:ntcBbfOIpInAlBbfOverIPModNS,'ntcBbfOIpInConformance':ntcBbfOIpInConformance,'ntcBbfOIpInConfCompliance':ntcBbfOIpInConfCompliance,'ntcBbfOIpInConfCompV1Standard':ntcBbfOIpInConfCompV1Standard,'ntcBbfOIpInConfGroup':ntcBbfOIpInConfGroup,_A5:ntcBbfOIpInConfGrpV1Standard})